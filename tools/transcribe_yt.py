#!/usr/bin/env python3
"""
transcribe_yt.py — YouTube URL (or a local audio file) in, project-shaped
transcript files out.

Downloads audio with yt-dlp, encodes to a small mono m4a, submits to
AssemblyAI (Universal-3.5 Pro) with the project's key-terms list and a
per-video contextual prompt, then writes the four files this project
registers, plus a meta file recording the exact settings used.

Two input modes
----------------
  --url   <youtube url>   Normal mode: download audio + captions from YouTube.
  --audio <path>          Local-audio mode: skip the download entirely and
                           run an already-downloaded/recorded audio file
                           straight through the same AssemblyAI step.
                           Exactly one of --url / --audio is required.

  Local-audio mode still fetches YouTube's metadata and its own captions
  (the independent second rendering this project's cross-check depends on)
  if you also pass --caption-url pointing at the matching video. Omit
  --caption-url and both are simply skipped — meta.json records that
  explicitly rather than guessing.

Usage
-----
  export ASSEMBLYAI_API_KEY=<your key>

  # normal: YouTube URL in
  python3 transcribe_yt.py \
      --url "https://www.youtube.com/watch?v=XXXX" \
      --name Findley \
      --speakers 2 \
      --prompt "An Anglican priest interviews Fr Chris Findley about liturgical worship and the Book of Common Prayer." \
      --outdir "~/EMC/original transcripts/video transcripts/batch5"

  # local audio file in, AssemblyAI step only
  python3 transcribe_yt.py \
      --audio "~/Downloads/some_sermon.m4a" \
      --name SomeSermon \
      --speakers 1 \
      --prompt "A solo sermon on the Eucharist." \
      --outdir "~/EMC/original transcripts/video transcripts/batch6"

  # local audio file, but still cross-check against YouTube's own captions
  python3 transcribe_yt.py \
      --audio "~/Downloads/some_sermon.m4a" \
      --caption-url "https://www.youtube.com/watch?v=XXXX" \
      --name SomeSermon \
      --outdir "~/EMC/original transcripts/video transcripts/batch6"

Outputs (matching this project's existing naming convention)
------------------------------------------------------------
  <name>-sentences.json     sentence-level, with speaker labels  <- PRIMARY
  <name>-timestamps.json    word-level timings
  <name>-transcript.srt     caption form
  <name>-transcript.txt     plain text
  <name>-youtube.srt        YouTube's own captions (only if --url, or
                             --audio with --caption-url)
  <name>-meta.json          settings used, transcript id, hashes, duration

Requires: ffmpeg always; yt-dlp only if --url or --caption-url is used.
          pip install requests
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import requests

BASE_URL = "https://api.assemblyai.com"
# The API deprecated the singular `speech_model` in favour of a list; the
# second entry is the fallback if the first can't serve the request.
SPEECH_MODELS = ["universal-3-5-pro", "universal-2"]

# Default location of the project's key-terms file, relative to this script's
# parent. Override with --keyterms.
DEFAULT_KEYTERMS = Path.home() / "EMC" / "theology" / "asr_keyterms_A101.md"


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def die(msg):
    print(f"\nERROR: {msg}\n", file=sys.stderr)
    sys.exit(1)


def need(binary):
    if shutil.which(binary) is None:
        die(f"'{binary}' not found on PATH. Install it and try again.")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_keyterms(path):
    """Pull the fenced list under '## The list' out of the key-terms file.

    Tolerates the project's comma-delimited-one-per-line format as well as
    a bare newline list. Returns a de-duplicated list of strings.
    """
    if not path.exists():
        print(f"  ! key-terms file not found at {path} — continuing without it")
        return []

    text = path.read_text(encoding="utf-8")
    i = text.find("## The list")
    if i < 0:
        print(f"  ! '## The list' heading not found in {path} — continuing without it")
        return []

    start = text.find("```", i)
    end = text.find("```", start + 3)
    if start < 0 or end < 0:
        print(f"  ! no fenced block after '## The list' — continuing without it")
        return []

    block = text[start + 3:end]
    raw = re.split(r"[,\n]", block)

    terms, seen = [], set()
    for t in raw:
        t = t.strip()
        if t and t.lower() not in seen:
            seen.add(t.lower())
            terms.append(t)
    return terms


YTDLP_CHECK_STAMP = Path.home() / ".cache" / "transcribe_yt" / "ytdlp_checked"


def ytdlp_installer():
    """How was yt-dlp installed? Determines which updater to use."""
    path = shutil.which("yt-dlp") or ""
    real = os.path.realpath(path)
    if "/Cellar/" in real or "/homebrew/" in real or "/linuxbrew/" in real:
        return "brew"
    if "/pipx/" in real or "/.local/pipx/" in real:
        return "pipx"
    if "/site-packages/" in real or "/.venv" in real or "/venv/" in real:
        return "pip"
    return "self"  # standalone binary; yt-dlp -U works


def maybe_update_ytdlp(mode, max_age_hours=24):
    """Keep yt-dlp current. YouTube breaks it often, so this is worth doing.

    mode: 'auto'  — check at most once per max_age_hours, update if behind
          'force' — check and update now, ignoring the cache
          'skip'  — do nothing
    ⚠️ Never fatal. A failed check or update warns and proceeds — the
    download may well work on the current version anyway.
    """
    if mode == "skip":
        return

    if mode == "auto" and YTDLP_CHECK_STAMP.exists():
        age_h = (time.time() - YTDLP_CHECK_STAMP.stat().st_mtime) / 3600
        if age_h < max_age_hours:
            print(f"  · yt-dlp version checked {age_h:.0f}h ago — skipping "
                  f"(use --update-ytdlp force to recheck)")
            return

    installer = ytdlp_installer()
    try:
        cur = subprocess.run(["yt-dlp", "--version"], capture_output=True,
                             text=True, timeout=30).stdout.strip()
    except Exception as e:
        print(f"  ! could not read yt-dlp version ({e}) — proceeding anyway")
        return

    print(f"  · yt-dlp {cur} (installed via {installer}); checking for updates …")

    cmds = {
        "brew": ["brew", "upgrade", "yt-dlp"],
        "pipx": ["pipx", "upgrade", "yt-dlp"],
        "pip":  [sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"],
        "self": ["yt-dlp", "-U"],
    }
    cmd = cmds[installer]

    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    except subprocess.TimeoutExpired:
        print("  ! update timed out after 5 min — proceeding on current version")
        return
    except Exception as e:
        print(f"  ! update could not run ({e}) — proceeding on current version")
        return

    try:
        new = subprocess.run(["yt-dlp", "--version"], capture_output=True,
                             text=True, timeout=30).stdout.strip()
    except Exception:
        new = cur

    if new != cur:
        print(f"  · yt-dlp updated: {cur} -> {new}")
    elif r.returncode != 0:
        tail = (r.stderr or r.stdout or "").strip().splitlines()
        hint = tail[-1] if tail else "no output"
        print(f"  ! update command failed ({hint}) — proceeding on {cur}")
    else:
        print(f"  · yt-dlp already current ({cur})")

    YTDLP_CHECK_STAMP.parent.mkdir(parents=True, exist_ok=True)
    YTDLP_CHECK_STAMP.touch()


def cookie_args(cookies_file, cookies_browser):
    """Cookie flags for yt-dlp.

    A cookies FILE is preferred over reading the browser live: Chrome locks
    its cookie store while running, and a partial extraction silently yields
    a degraded cookie set, which changes which client YouTube offers and can
    make an audio-only format disappear. A file has no such failure mode and
    stays valid for months.
    """
    if cookies_file:
        path = Path(os.path.expanduser(cookies_file))
        if not path.exists():
            die(f"cookies file not found: {path}")
        return ["--cookies", str(path)], f"file {path.name}"
    if cookies_browser and cookies_browser.lower() != "none":
        return ["--cookies-from-browser", cookies_browser], f"browser {cookies_browser}"
    return [], "none"


def check_youtube_auth(cookie_flags):
    """Verify the resolved cookies actually authenticate, using YouTube's own
    Watch Later playlist as the probe — WL only exists for a signed-in
    account, so its response is a definitive signal (unlike yt-dlp's own
    "cookies no longer valid" warning, which is heuristic and can be silent
    even when the session is anonymous). Invokes the bare "yt-dlp" command,
    same as every other call in this file, so it is guaranteed to resolve
    to the identical binary as the download that follows it. Never raises;
    returns True/False.

    ⚠️ yt-dlp REWRITES whatever file --cookies points at, on every
    invocation, success or failure — this is what turned a real signed-in
    jar into a dead anonymous one. If cookie_flags carries a --cookies FILE,
    the probe runs against a throwaway copy so it can never touch the
    caller's jar. --cookies-from-browser needs no such handling: it reads
    the browser's live store and never writes back.
    """
    probe_flags = cookie_flags
    tmp_copy = None
    if "--cookies" in cookie_flags:
        idx = cookie_flags.index("--cookies")
        src = Path(cookie_flags[idx + 1])
        fd, tmp_path = tempfile.mkstemp(suffix=".txt", prefix="ytdlp-authprobe-")
        os.close(fd)
        tmp_copy = Path(tmp_path)
        shutil.copyfile(src, tmp_copy)
        probe_flags = cookie_flags[:idx] + ["--cookies", str(tmp_copy)] + cookie_flags[idx + 2:]

    cmd = ["yt-dlp", "--flat-playlist", "--playlist-items", "0",
           "--dump-single-json"] + probe_flags + [
           "https://www.youtube.com/playlist?list=WL"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    except Exception:
        return False
    finally:
        if tmp_copy is not None:
            tmp_copy.unlink(missing_ok=True)
    return r.returncode == 0


def fetch_video_metadata(url, cookie_flags):
    """Pull YouTube's own metadata so the manifest doesn't need hand-entry.

    ⚠️ Returns {} on any failure — metadata is a convenience, never a reason
    to abort a transcription that would otherwise succeed.
    """
    print("  · fetching video metadata …")
    cmd = ["yt-dlp", "--dump-single-json", "--no-playlist", "--skip-download"]
    cmd += cookie_flags
    cmd.append(url)
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if r.returncode != 0:
            print("  ! metadata fetch failed — continuing without it")
            return {}
        d = json.loads(r.stdout)
    except Exception as e:
        print(f"  ! metadata fetch failed ({e}) — continuing without it")
        return {}

    # upload_date arrives as YYYYMMDD; give the manifest the ISO form too.
    raw_date = d.get("upload_date") or ""
    iso_date = (f"{raw_date[0:4]}-{raw_date[4:6]}-{raw_date[6:8]}"
                if len(raw_date) == 8 else None)

    meta = {
        "title": d.get("title"),
        "video_id": d.get("id"),
        "webpage_url": d.get("webpage_url"),
        "channel": d.get("channel") or d.get("uploader"),
        "channel_id": d.get("channel_id"),
        "channel_url": d.get("channel_url") or d.get("uploader_url"),
        "upload_date": iso_date,
        "upload_date_raw": raw_date or None,
        "release_date": d.get("release_date"),
        "duration_seconds": d.get("duration"),
        "view_count": d.get("view_count"),
        "was_live": d.get("was_live"),
        "live_status": d.get("live_status"),
        "description": d.get("description"),
    }
    if meta["title"]:
        print(f"    title  : {meta['title']}")
    if meta["upload_date"]:
        live = " (livestream)" if meta.get("was_live") else ""
        print(f"    posted : {meta['upload_date']}{live}")
    if meta["channel"]:
        print(f"    channel: {meta['channel']}")
    return meta


def fetch_youtube_captions(url, outdir, name, cookie_flags):
    """Grab YouTube's own auto-captions as an INDEPENDENT second rendering.

    ⭐ This is the cross-check that catches the class of ASR error a single
    engine cannot see — e.g. `Eucharist` heard as "the universe", or
    `Lateran` as "lad ladan". Where two unrelated engines agree, a quote is
    corroborated; where they diverge, it is a flag.

    ⚠️ Returns None on any failure. Captions are a bonus, never a reason to
    fail a run — plenty of videos have none.
    """
    print("  · fetching YouTube's own captions (second rendering) …")
    tmp = outdir / f".{name}-subs"
    tmp.mkdir(parents=True, exist_ok=True)

    cmd = ["yt-dlp", "--skip-download", "--write-subs", "--write-auto-subs",
           "--sub-langs", "en.*", "--convert-subs", "srt", "--no-playlist",
           "-o", str(tmp / "cap.%(ext)s")]
    cmd += cookie_flags
    cmd.append(url)

    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except Exception as e:
        print(f"    ! caption fetch failed ({e}) — continuing without it")
        shutil.rmtree(tmp, ignore_errors=True)
        return None

    found = sorted(tmp.glob("*.srt"))
    if not found:
        note = "no English captions published for this video"
        if r.returncode != 0:
            tail = (r.stderr or "").strip().splitlines()
            if tail:
                note = tail[-1][:120]
        print(f"    ! no captions retrieved — {note}")
        shutil.rmtree(tmp, ignore_errors=True)
        return None

    # Prefer a manually-authored track over an auto-generated one when both
    # exist: human captions are a genuinely stronger comparison rendering.
    manual = [f for f in found if "orig" not in f.name and "auto" not in f.name]
    pick = manual[0] if manual else found[0]

    dest = outdir / f"{name}-youtube.srt"
    shutil.move(str(pick), str(dest))
    shutil.rmtree(tmp, ignore_errors=True)

    kind = "manual" if manual else "auto-generated"
    print(f"    · {dest.name} ({kind}, {dest.stat().st_size / 1000:.0f} KB)")
    return dest


def encode_audio(src, workdir, bitrate, mono, sample_rate, final_name="audio.m4a"):
    """ffmpeg -> small m4a, from whatever src is (raw download or a local
    file handed in via --audio). Skips re-encoding if the target already
    exists in workdir (matches the old download_audio's resume behaviour).
    """
    final = workdir / final_name
    if final.exists():
        print(f"  · reusing existing {final.name}")
        return final

    print(f"  · encoding to m4a ({bitrate}, {'mono' if mono else 'stereo'}, {sample_rate} Hz) …")
    cmd = ["ffmpeg", "-y", "-i", str(src), "-c:a", "aac", "-b:a", bitrate]
    if mono:
        cmd += ["-ac", "1"]
    cmd += ["-ar", str(sample_rate), str(final)]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    mb = final.stat().st_size / 1e6
    print(f"  · audio ready: {final.name} ({mb:.1f} MB)")
    return final


def download_audio(url, workdir, bitrate, mono, sample_rate, cookie_flags, cookie_desc, fmt):
    """yt-dlp -> best audio, then ffmpeg -> small m4a. Skips if already done."""
    final = workdir / "audio.m4a"
    if final.exists():
        print(f"  · reusing existing {final.name}")
        return final

    raw_tpl = str(workdir / "raw.%(ext)s")
    cmd = ["yt-dlp", "-f", fmt, "--no-playlist", "-o", raw_tpl]
    cmd += cookie_flags
    cmd.append(url)
    print(f"  · downloading audio with yt-dlp (cookies: {cookie_desc}) …")

    result = subprocess.run(cmd)
    if result.returncode != 0:
        die(
            "yt-dlp could not download the audio.\n\n"
            "  ⚠️  FIRST SUSPECT: COOKIES. YouTube blocks or limits requests\n"
            "  that don't carry a valid signed-in session, and exported cookies\n"
            "  do eventually expire. Things to try, in order:\n\n"
            "    1. Re-export your cookies file. Use the 'Get cookies.txt LOCALLY'\n"
            "       extension on youtube.com while signed in, and overwrite the\n"
            "       file at $YTDLP_COOKIES. This fixes most failures.\n"
            "    2. If reading the browser directly (--cookies-from-browser),\n"
            "       quit it fully first — a running browser locks its cookie\n"
            "       store and yields a partial, degraded set.\n"
            "    3. Try a different browser:  --cookies-from-browser safari\n"
            "    4. Update yt-dlp:            --update-ytdlp force\n"
            "    5. Try without cookies:      --cookies-from-browser none\n"
            "    6. Loosen the format:        --format best\n\n"
            "  The command that failed is printed above with its own error."
        )

    raws = [p for p in workdir.glob("raw.*")]
    if not raws:
        die("yt-dlp finished but produced no file")
    raw = raws[0]

    final = encode_audio(raw, workdir, bitrate, mono, sample_rate)
    raw.unlink(missing_ok=True)
    return final


class _ProgressReader:
    """Wraps a file object so requests can stream it while we report progress.

    requests treats any object with .read() as a stream, so counting bytes as
    they are consumed gives real upload progress rather than a spinner.
    __len__ is required or requests falls back to chunked encoding.
    """

    # 5s was too slow: a 33 MB upload on a fast link finishes inside one
    # interval, so the only frame that ever printed was the final 100%.
    def __init__(self, path, interval=0.2):
        self.path = path
        self.total = path.stat().st_size
        self.sent = 0
        self.interval = interval
        self.start = time.time()
        self.last = 0.0
        self.done = False
        self._f = open(path, "rb")

    def __len__(self):
        return self.total

    # Cap how much is handed over per call. requests/urllib3 loops until read()
    # returns empty, so short reads are safe — and capping them is what makes
    # the bar track the network rather than a single gulp into the send buffer.
    CHUNK = 512 * 1024

    def read(self, size=-1):
        want = self.CHUNK if size is None or size < 0 else min(size, self.CHUNK)
        chunk = self._f.read(want)
        self.sent += len(chunk)
        now = time.time()
        finished = self.sent >= self.total
        first = self.last == 0.0
        if not self.done and (first or now - self.last >= self.interval or finished):
            self.last = now
            self._report(final=finished)
            self.done = finished   # the 100% line prints exactly once
        return chunk

    def _report(self, final=False):
        elapsed = max(time.time() - self.start, 0.001)
        pct = self.sent / self.total * 100 if self.total else 100.0
        mbps = (self.sent / 1e6) / elapsed
        filled = int(pct // 5)
        bar = "#" * filled + "-" * (20 - filled)
        if final:
            line = (f"    [{bar}] 100%  {self.total / 1e6:.1f} MB "
                    f"in {elapsed:.0f}s ({mbps:.1f} MB/s)")
            print(f"\r{line:<78}")
        else:
            remaining = (self.total - self.sent) / 1e6 / mbps if mbps > 0 else 0
            line = (f"    [{bar}] {pct:4.1f}%  {self.sent / 1e6:5.1f}/"
                    f"{self.total / 1e6:.1f} MB  {mbps:.1f} MB/s  "
                    f"~{remaining:.0f}s left")
            print(f"\r{line:<78}", end="", flush=True)

    def close(self):
        self._f.close()


def upload(path, headers):
    mb = path.stat().st_size / 1e6
    print(f"  · uploading to AssemblyAI ({mb:.1f} MB) …")
    reader = _ProgressReader(path)
    try:
        r = requests.post(f"{BASE_URL}/v2/upload", headers=headers, data=reader)
    finally:
        sent, total = reader.sent, reader.total
        reader.close()

    # ⛔ Guard against a truncated upload silently producing a partial
    # transcript — a short body would be far worse than a failed run.
    if sent != total:
        die(f"upload was truncated: sent {sent:,} of {total:,} bytes. "
            f"Nothing was transcribed. Re-run; if it recurs, report it.")

    if r.status_code != 200:
        die(f"upload failed [{r.status_code}]: {r.text[:400]}")
    return r.json()["upload_url"]


def submit(config, headers):
    r = requests.post(f"{BASE_URL}/v2/transcript", headers=headers, json=config)
    if r.status_code != 200:
        die(f"submit failed [{r.status_code}]: {r.text[:400]}")
    return r.json()["id"]


def poll(tid, headers, interval=5):
    url = f"{BASE_URL}/v2/transcript/{tid}"
    waited = 0
    while True:
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            die(f"poll failed [{r.status_code}]: {r.text[:400]}")
        t = r.json()
        status = t["status"]
        if status == "completed":
            print(f"\n  · completed after {waited // 60}m {waited % 60}s")
            return t
        if status == "error":
            die(f"transcription failed: {t.get('error')}")
        print(f"\r  · {status} … {waited // 60}m {waited % 60}s", end="", flush=True)
        time.sleep(interval)
        waited += interval


def get_json(tid, headers, suffix):
    r = requests.get(f"{BASE_URL}/v2/transcript/{tid}/{suffix}", headers=headers)
    if r.status_code != 200:
        print(f"  ! could not fetch /{suffix} [{r.status_code}] — skipping")
        return None
    return r.json()


def get_srt(tid, headers):
    r = requests.get(f"{BASE_URL}/v2/transcript/{tid}/srt", headers=headers)
    if r.status_code != 200:
        print(f"  ! could not fetch /srt [{r.status_code}] — skipping")
        return None
    return r.text


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--url", help="YouTube URL. Downloads audio (+ captions) from it.")
    src.add_argument("--audio", help="Path to an already-downloaded/recorded local "
                                      "audio file. Skips yt-dlp download entirely; "
                                      "runs the AssemblyAI step on this file directly. "
                                      "Pair with --caption-url to still fetch YouTube's "
                                      "captions and metadata for the cross-check.")
    ap.add_argument("--caption-url", default=None,
                    help="Only meaningful with --audio. If the local audio file "
                         "corresponds to a known YouTube video, pass its URL here to "
                         "still fetch YouTube's own captions (independent second "
                         "rendering) and video metadata, without re-downloading audio.")
    ap.add_argument("--name", required=True,
                    help="Output basename, e.g. Findley -> Findley-sentences.json")
    ap.add_argument("--speakers", type=int, default=None,
                    help="Expected speaker count. Omit for auto-detect. "
                         "Use 1 for solo videos (still label them).")
    ap.add_argument("--prompt", default="",
                    help="Contextual prompt: one plain sentence describing the "
                         "recording. NOT a keyword list.")
    ap.add_argument("--outdir", required=True, help="Where to write the output files")
    ap.add_argument("--keyterms", default=str(DEFAULT_KEYTERMS),
                    help=f"Path to the key-terms .md file (default: {DEFAULT_KEYTERMS})")
    ap.add_argument("--no-diarize", action="store_true",
                    help="Disable speaker labels entirely")
    ap.add_argument("--no-disfluencies", action="store_true",
                    help="Strip filler words. NOT recommended for this project — "
                         "it logs what is actually said.")
    ap.add_argument("--format", default="bestaudio/best",
                    help="yt-dlp format selector (only used with --url). Default "
                         "'bestaudio/best' takes an audio-only stream when offered "
                         "and otherwise falls back to any stream, letting ffmpeg "
                         "strip the audio — video is fine, only the audio is kept.")
    ap.add_argument("--update-ytdlp", choices=["auto", "force", "skip"],
                    default="auto",
                    help="Keep yt-dlp current. 'auto' (default) checks at most "
                         "once a day; 'force' checks now; 'skip' never checks. "
                         "A failed check never blocks the transcription. Only "
                         "relevant when yt-dlp is actually used (--url, or --audio "
                         "with --caption-url).")
    ap.add_argument("--no-youtube-captions", action="store_true",
                    help="Skip downloading YouTube's own captions (only relevant "
                         "with --url). NOT recommended — they are an independent "
                         "second rendering, and the cross-check against them is "
                         "what catches single-engine mishearings.")
    ap.add_argument("--cookies-file", default=os.environ.get("YTDLP_COOKIES", ""),
                    help="Path to a Netscape-format cookies.txt. PREFERRED over "
                         "--cookies-from-browser: reading a running browser's "
                         "store can yield a partial cookie set, which silently "
                         "changes which formats YouTube offers. Defaults to the "
                         "YTDLP_COOKIES env var if set. Export once with the "
                         "'Get cookies.txt LOCALLY' extension; valid for months.")
    ap.add_argument("--cookies-from-browser", default="chrome",
                    help="Browser to pull YouTube cookies from (chrome, safari, "
                         "firefox, brave, edge). Use 'none' to skip cookies. "
                         "YouTube blocks anonymous downloads intermittently, so "
                         "cookies are the reliable route. Quit the browser first "
                         "if it complains the cookie store is locked.")
    ap.add_argument("--bitrate", default="64k")
    ap.add_argument("--sample-rate", type=int, default=16000)
    ap.add_argument("--stereo", action="store_true", help="Keep stereo (default: mono)")
    ap.add_argument("--keep-audio", action="store_true",
                    help="Keep the downloaded/encoded m4a next to the outputs")
    args = ap.parse_args()

    key = os.environ.get("ASSEMBLYAI_API_KEY")
    if not key:
        die("ASSEMBLYAI_API_KEY is not set.  export ASSEMBLYAI_API_KEY=<your key>")

    if args.caption_url and not args.audio:
        die("--caption-url only makes sense together with --audio "
            "(with --url the captions already come from --url itself).")

    local_audio_path = None
    if args.audio:
        local_audio_path = Path(os.path.expanduser(args.audio))
        if not local_audio_path.exists():
            die(f"--audio file not found: {local_audio_path}")

    needs_ytdlp = bool(args.url) or bool(args.caption_url)

    need("ffmpeg")
    if needs_ytdlp:
        need("yt-dlp")
        maybe_update_ytdlp(args.update_ytdlp)

    outdir = Path(os.path.expanduser(args.outdir))
    outdir.mkdir(parents=True, exist_ok=True)
    workdir = outdir / f".{args.name}-work"
    workdir.mkdir(exist_ok=True)

    headers = {"authorization": key}

    print(f"\n=== {args.name} ===")

    # 1. cookies, metadata, captions, audio
    cflags, cdesc = (cookie_args(args.cookies_file, args.cookies_from_browser)
                     if needs_ytdlp else ([], "n/a"))

    video_meta = {}
    captions = None
    local_audio_record = None

    if args.url:
        print("  · verifying YouTube auth …")
        if not check_youtube_auth(cflags):
            die(
                f"cookies ({cdesc}) do not authenticate to YouTube — this run "
                "would silently fall back to an anonymous session, which can "
                "download public videos but will fail or silently degrade for "
                "age-restricted/member content and is more likely to be "
                "rate-limited.\n\n"
                "  Known-working path on this machine: --cookies-from-browser "
                "chrome (confirmed 2026-08-25). If using a --cookies-file "
                "instead, note that yt-dlp REWRITES that file on every run, "
                "success or failure — never point it at a jar you want to "
                "preserve.\n\n"
                "  Fix, then re-run with the same flags: sign in to YouTube "
                "in Chrome, or supply working cookies another way."
            )
        video_meta = fetch_video_metadata(args.url, cflags)
        if not args.no_youtube_captions:
            captions = fetch_youtube_captions(args.url, outdir, args.name, cflags)
        audio = download_audio(args.url, workdir, args.bitrate,
                               not args.stereo, args.sample_rate,
                               cflags, cdesc, args.format)
    else:
        print(f"  · using local audio file: {local_audio_path}")
        local_audio_record = {
            "path": str(local_audio_path),
            "bytes": local_audio_path.stat().st_size,
            "sha256": sha256_of(local_audio_path),
        }
        if args.caption_url:
            video_meta = fetch_video_metadata(args.caption_url, cflags)
            captions = fetch_youtube_captions(args.caption_url, outdir, args.name, cflags)
        else:
            print("  · no --caption-url given — skipping YouTube metadata/captions "
                  "(meta.json will record this explicitly)")
        audio = encode_audio(local_audio_path, workdir, args.bitrate,
                             not args.stereo, args.sample_rate)

    audio_sha = sha256_of(audio)

    # 2. key terms
    terms = load_keyterms(Path(os.path.expanduser(args.keyterms)))
    print(f"  · key terms loaded: {len(terms)}")

    # 3. config
    config = {
        "audio_url": upload(audio, headers),
        "speech_models": SPEECH_MODELS,
        "language_code": "en",
        "disfluencies": not args.no_disfluencies,
        "speaker_labels": not args.no_diarize,
    }
    if terms:
        config["keyterms_prompt"] = terms
    if args.prompt:
        config["prompt"] = args.prompt
    if args.speakers and not args.no_diarize:
        config["speakers_expected"] = args.speakers

    print("  · submitting …")
    tid = submit(config, headers)
    print(f"  · transcript id: {tid}")

    transcript = poll(tid, headers)

    # 4. outputs
    base = outdir / args.name

    sentences = get_json(tid, headers, "sentences")
    if sentences:
        (base.with_name(f"{args.name}-sentences.json")).write_text(
            json.dumps(sentences, indent=2, ensure_ascii=False), encoding="utf-8")

    words = transcript.get("words")
    if words:
        (base.with_name(f"{args.name}-timestamps.json")).write_text(
            json.dumps({"words": words}, indent=2, ensure_ascii=False), encoding="utf-8")

    srt = get_srt(tid, headers)
    if srt:
        (base.with_name(f"{args.name}-transcript.srt")).write_text(srt, encoding="utf-8")

    (base.with_name(f"{args.name}-transcript.txt")).write_text(
        transcript.get("text") or "", encoding="utf-8")

    # 5. meta — the provenance record this project registers
    written = {}
    for suffix in ("sentences.json", "timestamps.json", "transcript.srt",
                   "transcript.txt", "youtube.srt"):
        p = base.with_name(f"{args.name}-{suffix}")
        if p.exists():
            written[p.name] = {"bytes": p.stat().st_size, "sha256": sha256_of(p)}

    meta = {
        "name": args.name,
        "input_mode": "url" if args.url else "local_audio",
        "source_url": args.url,
        "source_audio_file": local_audio_record,
        "caption_url": args.caption_url,
        "source_video": video_meta,
        "transcript_id": tid,
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "audio": {
            "sha256": audio_sha,
            "bytes": audio.stat().st_size,
            "bitrate": args.bitrate,
            "sample_rate": args.sample_rate,
            "channels": 2 if args.stereo else 1,
            "cookies_source": cdesc,
            "format_selector": args.format if args.url else None,
            "ytdlp_version": (subprocess.run(
                ["yt-dlp", "--version"], capture_output=True, text=True
            ).stdout.strip() or "unknown") if needs_ytdlp else None,
        },
        "assemblyai_config": {k: v for k, v in config.items() if k != "audio_url"},
        "youtube_captions": (
            {"file": captions.name, "note": "independent second rendering, "
             "for cross-checking wording"} if captions else None),
        "keyterms_count": len(terms),
        "keyterms_source": str(Path(os.path.expanduser(args.keyterms))),
        "audio_duration_seconds": transcript.get("audio_duration"),
        "speakers_detected": sorted({u["speaker"] for u in (transcript.get("utterances") or [])}),
        "outputs": written,
    }
    (base.with_name(f"{args.name}-meta.json")).write_text(
        json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")

    # 6. tidy
    if args.keep_audio:
        shutil.move(str(audio), str(outdir / f"{args.name}-audio.m4a"))
    shutil.rmtree(workdir, ignore_errors=True)

    dur = meta["audio_duration_seconds"] or 0
    if video_meta.get("title"):
        print(f"\n  title    : {video_meta['title']}")
        print(f"  posted   : {video_meta.get('upload_date') or 'unknown'}")
        print(f"  video id : {video_meta.get('video_id') or 'unknown'}")
        print(f"  duration : {dur // 60}m {dur % 60}s")
    else:
        print(f"\n  duration : {dur // 60}m {dur % 60}s")
    print(f"  speakers : {meta['speakers_detected'] or 'n/a'}")
    print(f"  written  : {len(written) + 1} files in {outdir}")
    for n in sorted(written):
        print(f"             {n}")
    print(f"             {args.name}-meta.json\n")


if __name__ == "__main__":
    main()
