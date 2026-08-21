# ORCHESTRATION — how work gets done on this project

**Last updated: 260832-5** (date-stamped, format yymmdd-iteration)

> **What this file is.** The durable *working conventions* — how a batch
> gets from a YouTube URL to a committed finding, and which mistakes keep
> recurring. ⛔ **It holds NO volatile state.** Next-free numbers, open
> questions, gate status, and current owed items live in
> `PROJECT_STATE.md`, which is read first, always. Evidence and
> attribution rules live in `PROJECT_STATE.md` §5 and are not duplicated
> here.
>
> **Read order for any new thread:** `PROJECT_STATE.md` → this file →
> whatever the task names.

---

## 1. The core pattern: delegate, then verify independently

**One git repository is the single source of truth.** Nothing important
lives only in a chat thread.

**The orchestration thread does not edit the repo**, except for small,
fully self-verified fixes — a handful of lines, checked against the real
file, validator run, diff reverse-apply-tested. Anything larger is
delegated.

**Substantive work is delegated** to a Cowork task ("On your computer"
mode) or Claude Code, via a detailed written prompt with explicit
gate-checks.

⭐⭐⭐ **Every returned diff is independently verified before JD commits.**
Orchestration clones the repo fresh, applies the diff to that clean
clone, runs the validator, and spot-checks the load-bearing claims
against the actual corpus text. ⛔ **This is not optional and has caught
real errors repeatedly** — stale baselines, phantom numbering, a
misattributed quote, a silently duplicated source, a hash computed before
the file's own changelog entry was added.

**JD commits and pushes from his own terminal**, never from inside the
working-thread tool. Final human gate; stays a hard boundary.

⚠️⚠️ **One thread touching this repo at a time.** ⛔ **Parallel threads
editing the same files have caused real collisions** — a `DQ` posted in
one thread and never captured by another, a diff test-applying clean in
orchestration's own sandbox while a stale clone masked that it had
already landed via a different path. If a second thread must run, tell
orchestration explicitly before it starts, not after.

---

## 2. Paths

Everything under `~/EMC/`:

| Path | What |
|---|---|
| `~/EMC/theology` | the git repo |
| `~/EMC/original transcripts/video transcripts/` | livestream/video sources, in `batchN/` subfolders |
| `~/EMC/original transcripts/in person classes/` | A101 and other live-class sources, in date folders |
| `~/EMC/blog_archives/` | blog corpus |
| `~/EMC/downloads/` | patch/diff files handed to JD |
| `~/EMC/theology/passes/` | ⭐ pass artifacts, committed — see §4 |

⛔ **Not `/Users/jd/Downloads`** (the macOS one) and not Dropbox — the
repo was moved out of Dropbox at `260828-2` because its sync daemon
contended with `.git/`. Attach `~/EMC` to a Cowork task and both the repo
and the archive are covered.

---

## 3. The batch workflow, end to end

1. **JD transcribes.** `transcribe` (§6) turns a YouTube URL into the
   project's standard six-file set.
2. **Orchestration writes the intake prompt** — naming the exact HEAD to
   gate on, the exact validator baseline, the sources, what to read the
   material against by finding number, and the deliverables.
3. **The working thread runs intake and reconcile together**, applies
   edits directly, re-runs the validator, and **stops before committing**.
4. **It writes two artifacts** into `passes/` (§4) and commits nothing.
5. **Orchestration verifies** against a fresh clone (§1).
6. **JD applies, validates, commits, pushes** from his own terminal.

⛔ **Never two intakes before a reconcile.** Each batch lands fully —
applied, verified, committed — before the next begins.

**Any new file created for the project — a research document, an
analysis, anything — is created inside a working session with actual
repo access (Cowork or Claude Code), not drafted in an ordinary chat and
handed over afterward.** ⚠️ **A file assembled in a plain chat thread has
no repo, no git, nothing to commit — "commit this" in that context is not
actionable, and the file ends up untracked and undiscussed until someone
notices it later.** If research produces something worth keeping,
generate it (or move it) inside a session that can actually register it,
and tell orchestration before it lands, not after.

---

## 4. ⭐ Pass artifacts live in the repo, not in chat attachments

**Every delegated pass writes two files into `passes/`:**

```
passes/<stamp>_<short-name>.diff
passes/<stamp>_<short-name>_close-out.md
```

e.g. `passes/260831-1_batch5.diff`.

⭐⭐ **They are committed alongside the change they describe**, in the same
commit. That makes the reasoning behind every pass permanently
recoverable from git history, and it means **orchestration reads them
from a fresh clone rather than needing them uploaded** — which is the
point: chat attachments are a finite resource and this workflow no longer
spends them per batch.

**The close-out is a real document, not a receipt.** It records what was
found, what was declined and why, what was checked and came back empty,
and anything the pass could not resolve. ⛔ **A pass that reports only
success is under-reporting.**

⚠️ **The diff in `passes/` is the diff as applied.** Since JD applies it
before committing, the committed diff file describes the very commit it
travels in — self-referential but accurate, and far more useful than
having it live outside the repo.

⚠️ **A file can land in `passes/` without being registered in
`PROJECT_STATE.md`'s file table** if it's reference material rather than
a pass artifact proper (e.g. process documentation JD drops in for
orchestration's own benefit). ⛔ **That's fine and doesn't need forcing
into the registration discipline** — only source transcripts, findings
corpora, and documents a future pass might cite need a registry row.

---

## 5. Hand-off format

Every hand-off from orchestration to JD ends with a block naming:

- **📥 any file to download first** — stated in bold at the TOP of the
  message, not the bottom. ⚠️ **JD has repeatedly run commands before
  noticing a file needed downloading; this is a real, recurring cost.**
- **venue** — Cowork desktop "On your computer", or Claude Code
- **approval setting**
- **what to attach** — normally just `~/EMC`
- **what to expect back**

**Commit blocks are given verbatim, ready to paste**, and always include
`rm -f .git/index.lock` before `git add` (§7).

---

## 6. Transcription pipeline

**`~/bin/transcribe`** → wrapper → `~/bin/transcribe_yt.py`, running in
the venv at `~/.venvs/transcribe`.

```
transcribe --url "<youtube url>" --name <Basename> --speakers <n> \
  --prompt "<one plain sentence describing the recording>" \
  --outdir "~/EMC/original transcripts/video transcripts/batchN"
```

**Produces six files per video:** `-sentences.json` (⭐ PRIMARY,
diarized), `-timestamps.json` (word-level, navigation only),
`-transcript.srt`, `-transcript.txt`, `-youtube.srt` (⭐⭐ YouTube's own
captions — an INDEPENDENT second rendering), and `-meta.json`.

⭐⭐⭐ **`-meta.json` is the source of record for registration** — title,
video id, url, channel, ISO upload date, `was_live`, duration, the exact
AssemblyAI config, the key-terms list used, and sha256 of every output.
⛔ **Do not re-derive by hand what it supplies. Do verify its recorded
hashes against the files.**

**Key terms** are read automatically from `asr_keyterms_A101.md`. ⚠️
**Watch for `key terms loaded: N` in the output** — Batches P1-P3 ran
without it, which is a real difference in capture quality and is recorded
in their registrations.

**Cookies** come from a file at `$YTDLP_COOKIES` (exported once with a
browser extension; valid for months). ⛔ **Reading a running browser's
cookie store directly yields a partial set and silently changes which
formats YouTube offers** — that failure cost a debugging cycle.

**Running several at once:** `~/bin/run_batch4.sh` is the template —
background jobs staggered ~8s apart, each logging to `batchN/logs/`.
⚠️ **Scripts run under `/bin/sh`, which does not read `~/.zshrc`** — call
`"$HOME/bin/transcribe"` by full path inside a script, never bare.

⏳ **Known issue, do not re-fix blindly:** the upload progress bar still
reports 100% immediately. Two attempts (capped reads; faster refresh)
did not resolve it. **Next attempt should investigate what
requests/urllib3 actually does with the reader object rather than
refining the current approach.**

---

## 7. Recurring failure modes — each has bitten at least once

**Stale git locks.** `.git/index.lock` or `.git/HEAD.lock` left behind by
a sandboxed tool that can create files but not always unlink them.
⛔ **A working thread must report a lock and stop, never delete one.**
JD clears it. Every commit block includes `rm -f .git/index.lock`
pre-emptively.

**Self-referential registry rows.** Bumping a file's own `Last updated:`
stamp while forgetting its row in `PROJECT_STATE.md` §4 — C3 catches it.
⚠️ **`PROJECT_STATE.md` and `SRC_Manifest.md` each have a row for
themselves.**

**Hashes computed too early.** Hashing a file *before* adding its own
changelog entry makes the recorded hash stale the moment the entry lands.
⛔ **Hash last, after every edit to that file is complete.**

**Attribution by adjacency.** Turn-tracing and topical fit are weaker
evidence than a speaker label or a doctrinal impossibility. **`LS-39` was
misattributed exactly this way** — a guest's clause read as his — and was
only caught by a later cross-check. ⛔ **Where diarization exists, it
governs.**

**Diarization establishes whose VOICE, not whose WORDS.** Chat questions,
quoted opponents, and read-aloud documents all carry the speaker's own
label. ⛔ **Response and review videos are the high-risk class: by
construction he characterizes positions that are not his.**

**Count-matching is not content-matching.** Two renderings both showing a
term N times does not mean they agree — `regulative` was 5·5 with two
sites differing.

**Term scans need speaker splits.** `element ×25` looked like `DQ-9`
movement; all 25 were false positives traced individually.

**Duplicate sources arrive disguised as new.** `a304`, `a303`, and the
`-youtube.en-orig.srt` files were all near- or byte-identical re-supplies.
⛔ **Duplicate-check by content before minting any tag.**

**Briefs can be wrong.** A prompt's stated premise has been falsified by
the repo more than once. ⛔ **The repo wins; flag the discrepancy, do not
silently reconcile it.**

**A local sandbox's `git apply --check` can fail while the same patch
lands cleanly on JD's actual machine.** ⚠️ **If orchestration's own clone
was made even slightly stale, a `--check` failure there is not
authoritative — re-clone fresh and re-check before assuming a real
conflict.** This produced a false "possible collision" scare once already.

**A working thread offering to "commit this" in a plain chat, without
repo access, cannot actually do so** — the file ends up untracked,
undiscussed, and discovered later. See §3's note on where new files get
created.

---

## 8. Standing instructions

⭐⭐⭐ **Any mention of incense or icons, in any source, however tangential,
is flagged as high priority** and reported explicitly in every close-out
— including when the result is a confirmed zero.

⛔ **Nothing is ever drafted, altered, or posted to Rev. James by a
delegated pass.** Discord access is manual, always: JD copies the full
thread himself and pastes it for comparison. ⛔ **Full-thread recapture,
never an append** (`260801-3`) — because he has edited a message after
posting before, and only a full comparison catches that.

**Corrections are dated notes beside the original, never silent
rewrites** — the never-alter rule, project-wide.

---

## 9. Thread lifecycle — how JD manages long conversations

**Separate from this project's own git-based delegate-and-verify loop, JD
runs a memory-stored, cross-thread system for managing the cost and
staleness of long chat conversations generally.** Not part of this
project's data discipline, but worth knowing about, since orchestration
threads are exactly the kind of long-running conversation this system
exists to handle.

**The full specification lives at
`passes/ff-rff-ffd-system-documentation-v2.md`; this section summarizes
it.**

**The problem it solves:** a chat thread resends its full history every
turn, an interface has no native fork or compaction, and a long thread
eventually buries active work under stale context.

**Three memory-stored commands, `FF` / `RFF` / `FFD`:**
- **`FF`**, run in a heavy or pivoting thread, produces a dense,
  copy-pasteable handoff block ending in a unique **fork tag** (e.g.
  `FORKTAG-CS-p4k9m2`) generated in that thread's own text.
- **JD pastes the block as the first message of a fresh thread** and
  continues there at far lower per-turn cost.
- **`RFF`**, run in the new thread, retrieves anything the handoff didn't
  carry — either directly via `conversation_search` (the fork tag exists
  in exactly the source and forked threads, so it identifies the source
  precisely rather than by fuzzy keyword match) or by generating a
  retrieval prompt for JD to relay manually.
- **`FFD`**, run in the *source* thread, produces incremental delta
  passes if that thread keeps accumulating information after the first
  handoff — so a second fork later isn't working from a stale snapshot.

⚠️ **v1 (this description) is live and in use. A v2 (doc-backed state) is
specified but untested** as of `260832-2` — this project's own
`ORCHESTRATION.md`/`PROJECT_STATE.md` pair is, in effect, one instance of
exactly that doc-backed-state pattern already.

**Relevance to this repo specifically:** if a hand-off into a *fresh*
orchestration thread ever uses `FF`/`RFF` rather than the simple "read
`PROJECT_STATE.md` then this file" pointer already established, the new
thread should expect a fork-tag-bearing block as its first message and
can treat it the same way — confirm the tag survived the paste verbatim,
then proceed. ⛔ **Neither replaces the other:** `FF`/`RFF`/`FFD` manage
*conversation* continuity; `PROJECT_STATE.md` and this file manage
*project* continuity. A fresh thread benefits from both if both are
available, but the project state is authoritative if they ever disagree.
