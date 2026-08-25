# 260833-7 — Tooling pass: move `transcribe_yt.py` into version control, fix an auth-probe defect, record the cookie write-back rule

**Pass artifacts:** `passes/260833-7_transcribe-yt-tooling-move.diff` (as applied — captured by staging `tools/transcribe_yt.py` and `PROJECT_STATE.md`, running `git diff --cached`, then unstaging without committing) · this file.
**Gate:** HEAD `6b83dd6f69d812c74154ad3e491f05019eecb4a8` (*"260833-6: Discord intake — RPW recapture and DQ-20 onward, new Assurance archive registered, Known Gap 5 current-voice side filled"*), working tree clean — exactly as briefed. No Batch 8 intake had landed; HEAD matched `PROJECT_STATE.md`'s own `Last updated: 260833-6` exactly.
**Validator BEFORE:** `78 ok · 6 warnings · 0 errors` — C1 (`src/SRC_Discord_RPW.md`, 1 relative timestamp), C3 (`Calvin_Luther_and_Anglican_Formularies_on_Iconography.md`, unparseable stamp), C4 (`St_Francis_EMC_Distinctives.md`, 2 answered-as-pending), C5 ×2 (`RJ_Final_Question_List.md` 17 / `RJ_Incense_Analysis.md` 9 volatile-state assertions), C11 (outline 4 findings behind the DQ ledger head).
**Validator AFTER:** `79 ok · 7 warnings · 0 errors` — the same six, plus exactly one new, precedented warning: `WARN [C3] tools/transcribe_yt.py: no parseable 'Last updated' stamp; registry says '260833-7'`. Same shape as the pre-existing `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` warning — a registered file without an in-file stamp line WARNs, does not ERROR. **Not fixed this pass**, deliberately: the brief scoped script edits to Step 3 (the auth-probe fix) only, and adding a stamp line to `transcribe_yt.py`'s docstring would be a further content edit outside that scope. Flagged here as owed work, not silently left unexplained.
**Stamp reasoning:** the corpus's `yymmdd-iteration` stamps are a project-internal sequence, not literal calendar dates (already past `260833`, i.e. "day 33" of a month with 31 days, confirmed by the `260833-6` gate commit itself) — today's real calendar date (2026-08-25) does **not** correspond to a free stamp; `grep`, run before use, showed `260825-1` is already consumed (from an earlier pass in this same internal sequence). The true highest stamp anywhere in the repo, `grep`-verified across every `.md`/`.py` file, is `260833-6`. `260833-7` was chosen as the next iteration on the same day-bucket (no evidence found for a day-bucket-increment rule, so the more conservative choice was made) and `grep -rn "260833-7"` returned zero hits before this pass's first edit.
**No finding minted. No `IP`/`RV`/`DQ`/`LS`/`BLOG`/`POD` number consumed.** Nothing committed or pushed — `git add`/`git commit` are left for JD.

---

## 0. This pass's actual scope

This closes out a chain of chat-only work (cookie auth diagnosis → auth-probe diff proposed and applied to the untracked `~/bin/transcribe_yt.py` → the probe's own self-rewrite defect found and fixed) by moving the script into this repo and recording what was learned. It is **not** an intake pass: no audio was transcribed, no source was read for content, nothing was added to any findings corpus.

## 1. Step 1 — auth-probe self-rewrite defect

**Defect:** `check_youtube_auth()` (added to `transcribe_yt.py` in the prior chat-only pass) passed `cookie_flags` straight through to its probe `yt-dlp` invocation. When `cookie_flags` carried a `--cookies <file>` pair, the probe rewrote that file — the exact read-write behavior the operational rule below exists to warn about, except now firing from the auth check meant to *protect* against silent failure, before the real download even ran. Confirmed empirically in the prior task: probing the quarantined `youtube-cookies.txt.BROKEN-20260825` moved its mtime.

**Fix applied** (see the diff for the exact patch — this pass's diff only covers the repo move; the fix itself was applied and verified against `~/bin/transcribe_yt.py` before this pass began, so it travels into the repo as part of the moved file rather than as a separate hunk here): `check_youtube_auth()` now detects a `--cookies` flag in its input, copies that file to a `tempfile.mkstemp()` throwaway path, probes the copy, and unlinks the copy in a `finally` block regardless of outcome. `--cookies-from-browser` needs no such handling — it reads the browser's live cookie store and never writes back, confirmed both by yt-dlp's own behavior (repeated identical extractions) and by the absence of any file-write target for that flag.

**Verification, direct:** copied `youtube-cookies.txt.BROKEN-20260825` to a scratch path (1,620 bytes, 13 cookie names, sha256 `cdd1c4...`), called `check_youtube_auth(['--cookies', '<copy>'])` directly via `importlib`, and confirmed all three (size, name list, sha256) **byte-identical** after the call. `check_youtube_auth` correctly still returned `False` (this jar has no `LOGIN_INFO` and does not authenticate — that fact is unaffected by the fix, which only stops the probe from *writing*, not from correctly *reading*).

**Guard re-test, both directions, against the fixed script:**
- **Good path** (`--cookies-from-browser chrome`): auth check printed and passed silently; the run proceeded through video-metadata fetch and download, stopping only later at a deliberately fake `ASSEMBLYAI_API_KEY` (401) — unrelated to the guard.
- **Bad path** (`--cookies-file` pointed at the quarantined jar): blocked with the expected message, citing `--cookies-from-browser chrome` as the known-working path and warning about the write-back rule. **This time the quarantined file's sha256/size were unchanged after the run** — confirming the fix closes the loop the same test exposed as open in the prior pass.

## 2. Step 2 — repo placement, checked rather than assumed

Before creating `tools/`, the repo was checked for an existing convention:
- **`src/`** — inspected directly. Its own repo-layout note in `PROJECT_STATE.md` §4 states plainly it holds `SRC_Discord_*` raw archives only ("⚠️ THE ARCHIVES ARE NOT FLAT"), a distinct purpose from tooling. Not a match.
- **`validate_project.py`** — the one existing file classed "Tooling" in the §4 registry. It sits **flat at repo root**, not in any subdirectory. This is a real discrepancy from this pass's `tools/transcribe_yt.py` placement, recorded here rather than silently resolved: the brief specified the `tools/` path explicitly, so this pass followed that instruction rather than overriding it on the strength of one prior example. Left for JD's call whether `validate_project.py` should eventually move to match, or `tools/` was the wrong call.
- **`.gitignore`** (`.DS_Store`, `backups/`) — checked with `git check-ignore -v tools/transcribe_yt.py`, exit 1 (not ignored). No edit needed or made.
- **`validate_project.py`'s own file-discovery mechanism** — read directly (§0 of that file). It derives its expected file set purely from the `PROJECT_STATE.md` §4 registry table (explicit paths, `registry_rows()`), then resolves each registered path against a full recursive tree walk (`build_index()`, `os.walk`) that already excludes only `.git`/`node_modules`/`__pycache__`/`.venv`/`venv`. This is precisely the fix the file's own top-of-file note describes for the `260725-1` defect (glob-based discovery missing `src/`'s nesting). **No code change was needed or made** — the mechanism is already directory-agnostic; confirmed by the AFTER validator run resolving `tools/transcribe_yt.py` at `[C0]` with zero special-casing.

## 3. Step 3 — gate check

- `git rev-parse HEAD` → `6b83dd6f69d812c74154ad3e491f05019eecb4a8`.
- `python3 validate_project.py` BEFORE → `78 ok · 6 warnings · 0 errors` (full check-code breakdown in the header above).
- `PROJECT_STATE.md`'s `Last updated` stamp → `260833-6`, matching HEAD's own commit message exactly. **No Batch 8 drift** — HEAD had not moved since the prior chat task; the stamp was re-derived from a repo-wide grep regardless, per instruction, rather than trusted as an assumption.

## 4. Step 4 — registration and pass note

- **`tools/transcribe_yt.py`** registered in `PROJECT_STATE.md` §4, grouped beside `validate_project.py` (the other Tooling-classed entry), version `260833-7`, class describing the move and the symlink, audience `JD + Claude`.
- **`PROJECT_STATE.md`'s own self-registry row** updated in the same edit as its top `Last updated` stamp (`260833-6` → `260833-7`), specifically to avoid the self-referential version-drift near-miss recorded in the `260833-2` close-out (top stamp bumped before its own §4 cell, briefly tripping `[C3] PROJECT_STATE.md: VERSION DRIFT`). Confirmed clean this time: AFTER run shows `ok [C3] PROJECT_STATE.md: version agrees with registry (260833-7)`.
- **Pass note** added at the top of `PROJECT_STATE.md`, immediately before the `260833-6` note (reverse-chronological, matching the file's existing convention), recording: the move, the symlink, and — as its own load-bearing paragraph — the operational rule: `--cookies <path>` is read-write and rewrites the jar on every yt-dlp invocation, pass or fail, so it must never point at a file worth preserving. Also records that this cost a real signed-in cookie jar to learn, so it doesn't live only in a chat log.
- **`youtube-cookies.txt.BROKEN-20260825`** and its README note live in `~/EMC/`, **outside this repo** (`~/EMC/theology/`) — not tracked here, not touched by this pass's `git diff`, mentioned in the pass note for context only.

## 5. Move verification

- `~/bin/transcribe_yt.py` (mode `-rwx--x--x`) copied with `cp -p` (mode preserved) to `tools/transcribe_yt.py`, original removed, symlink created: `~/bin/transcribe_yt.py -> /Users/jd/EMC/theology/tools/transcribe_yt.py`.
- `~/.zshrc` **not edited** — confirmed by leaving it untouched throughout; the existing alias (`alias transcribe="~/.venvs/transcribe/bin/python ~/bin/transcribe_yt.py"`) resolves the literal path, which the symlink now satisfies transparently.
- Verified three ways: `py_compile` on the symlinked path (clean), `~/.venvs/transcribe/bin/python ~/bin/transcribe_yt.py --help` (exit 0, renders), and the actual alias invoked through a real interactive-mode zsh subshell — `zsh -ic "source ~/.zshrc; transcribe --help"` — which also resolved and rendered correctly.

## 6. Constraint confirmations

- `~/EMC/theology` (this repo) touched only via the changes described above; nothing outside `PROJECT_STATE.md` and the new `tools/`/`passes/` entries was edited.
- `~/bin/transcribe_yt.py` was edited (as the file that became `tools/transcribe_yt.py`) only for the Step-1 probe fix — no other functional change accompanied the move.
- `~/.zshrc` not edited.
- Nothing committed, nothing pushed, nothing left staged (`git add` was used only transiently, to capture the diff artifact, then reversed with `git reset` before this pass ended).
- No finding minted; no `IP`/`RV`/`DQ`/`LS`/`BLOG`/`POD` number consumed.

## 7. What is left for JD

`git status --short` (see the chat close-out for the literal output) shows `M PROJECT_STATE.md` and `?? tools/` (plus the two new, currently-untracked `passes/260833-7_*` artifact files, per this folder's own convention that they are committed alongside the change they describe). To commit this pass:

```
git add PROJECT_STATE.md tools/transcribe_yt.py passes/260833-7_transcribe-yt-tooling-move.diff passes/260833-7_transcribe-yt-tooling-move_close-out.md
git commit -m "260833-7: move transcribe_yt.py into version control, fix auth-probe self-rewrite defect"
```

Nothing else is staged or proposed for staging by this pass.
