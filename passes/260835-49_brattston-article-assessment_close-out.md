# Close-out — `260835-49`: Brattston article assessment, registration pass

## Gate

- **HEAD confirmed:** `37be89a` ("260835-47, 260835-48: patristic citations verified — 4 of 8
  confirmed as claimed…"), matching the brief's stated value exactly.
- **`git status --short` at gate:** two untracked files only —
  `Brattston_Article_Assessment.md` and
  `src/SRC_PRIMARY_2003_Brattston_Incense_in_Ante-Nicene_Christianity.txt` — both written by
  the prior agent in this same task, before any edit this pass made. No tracked file carried
  an uncommitted change. Confirmed clean otherwise.
- **`260835-49` re-derived as FREE, not merely taken on the prior agent's word.** Repo-wide
  grep (all files, not just `.md`) for `260835-49` returned **exactly one hit**, and it was
  opened and read in context: `Brattston_Article_Assessment.md` line 3, this pass's own
  deliverable referring to itself ("Assessed 260835-49 (2026-09-01)…") — not a predecessor's
  forward absence-assertion of the `260835-12`/`260835-14` hazard-note shape, but also
  independently re-checked against `passes/` directory contents: the numeric-sorted run is
  unbroken `260835-1…48`, and `git log --all` tops out at `37be89a` (`260835-47, 260835-48`).
  **`260835-49` confirmed FREE.**
- **Validator baseline, fresh, run before any edit:** `88 ok · 11 warnings · 0 errors`,
  matching the committed baseline at `37be89a` exactly (re-run afterward against a pristine
  clone of that commit and reproduced byte-for-byte).
- **Hash independently re-verified, not copied from the hand-off.** `sha256sum` on
  `src/SRC_PRIMARY_2003_Brattston_Incense_in_Ante-Nicene_Christianity.txt` returns
  `4845fbef9c4a47f48595c319410c8d5ba7bc38f4d230a9b63445e5b9731dc1d9` — an exact match to the
  figure supplied at hand-off, confirmed by direct string comparison, not eyeballed.
- **Ledger number consumed: NONE.** This is a registration pass only, exactly as briefed.

### ⚠️ An environment defect hit at gate, worked around, reported rather than silently fixed

`.git/index.lock` existed as a stale 0-byte file at gate and could not be removed
(`rm -f .git/index.lock` returned `Operation not permitted` despite matching UID/GID
ownership — a sandbox-level restriction on this environment, not a permissions bug in the
usual sense). This blocked every git operation that writes the index, including
`git add --intent-to-add`, which the brief's diff-generation method depends on. **Read-only
git operations (`git status`, `git diff`, `git log`, `git diff --no-index`) were unaffected**
and this is what the diff below is built from — see "Diff verification" below for the
substituted method. No `rm` was forced past the permission error; the workaround avoids
touching the index at all rather than fighting the lock.

---

## What was done

Four files touched, all per brief:

1. **`Brattston_Article_Assessment.md`** — one edit only, adding
   `**Last updated: 260835-49** (created 260835-49; date-stamped, format yymmdd-iteration)`
   as its own line directly under the H1 title, before the first `---`, matching the format
   at the top of `Patristic_Citations_Incense_Verification.md` and
   `Tertullian_Incense_Passages.md`. **No other line in the file touched** — its substance is
   the prior agent's, not this pass's, per the brief. Final state: 80 lines, 15,020 bytes,
   `sha256` = `016e4fd1f01febf07916fe3cebd918b5576859594283780b0c629697653113d9`.
2. **`PROJECT_STATE.md` §4** — one new registry row added, for `Brattston_Article_Assessment.md`
   at `260835-49`, inserted immediately after the `Tertullian_Incense_Passages.md` row, in the
   same dense evidence-forward cell style `260835-47`/`260835-48` used for their own rows.
   Anchor-based insertion (the unique string spanning the end of the Tertullian row and the
   start of the next row), never line-number based.
3. **`SRC_Manifest.md` § External Primary Texts**:
   - **(a)** a genuine new table row for `src/SRC_PRIMARY_2003_Brattston_Incense_in_Ante-Nicene_Christianity.txt`
     in the section's own table (alongside the Westall/BCP rows) — path, work, byte count,
     line count, `sha256`, provenance, registered-at stamp — not merely a dated-note mention.
   - **(b)** a dated note registering `Brattston_Article_Assessment.md` itself as the section's
     **fifth** unnumbered external-research document, per the `260835-35` class-wide ruling.
     No `File`/`W`/`IP`/`LS`/`DQ` or other ledger number consumed.
4. **`PROJECT_STATE.md` §4 / `SRC_Manifest.md`'s own top-of-file stamp**, moved together in
   this same pass per `CLAUDE.md` close-out rule 3 (the exact rule `260835-48`'s close-out
   records having to fix as an unbriefed correction after missing it — see below): the
   `SRC_Manifest.md` registry cell and the file's own `**Last updated:**` line were both
   bumped to `260835-49` in the same set of edits, before running the validator, so `[C3]`
   never had a window to fire VERSION DRIFT.

### The provenance gap, flagged rather than smoothed over

The source `.txt` file carries no internal header recording where it was retrieved from (no
`CAPTURED …` line, no URL, no host name) — unlike the Westall/BCP rows above it in the same
table, each of which names an Internet Archive item or a named site (`satucket.com`). This
pass did not capture the file itself (it existed at gate, written by the prior agent in this
task) and has no record of the retrieval host to supply. **The new table row and the dated
note both state this gap explicitly** rather than inventing a provenance line — the row's
Provenance cell says so directly, flagged with ⚠️, consistent with the repo's practice of
naming a gap rather than papering over it. The content (hash, byte count, line count,
pp. 225–233 matching the citation in the assessment doc's own header) is independently
re-verified and solid; only the *retrieval* provenance is unrecorded.

### The genuine positive divergence stated, per brief

Unlike `260835-44`/`47`/`48`, all of which read every source live over the web and captured
nothing to `src/`, this pass's own primary source — the Brattston article — **is** captured
locally with a real, independently-verified `sha256`, entered as a proper table row rather
than only named in prose. This is stated plainly in both the `PROJECT_STATE.md` §4 row and
the `SRC_Manifest.md` dated note, scoped honestly: the Task 4 spot-check sources (four New
Advent pages) were still read live and not captured, so the improvement covers this one
document's own primary source, not the whole pass's sourcing.

---

## Validator, before and after

| | ok | warnings | errors |
|---|---|---|---|
| **BEFORE** (working tree at gate, and a pristine clone of `37be89a`) | 88 | 11 | 0 |
| **AFTER** (working tree, post-edit) | **90** | **11** | **0** |

**Delta: +2 ok, 0 change to warnings or errors — verified by diffing the full validator
output line-for-line, not just the totals.** The warning lines are **byte-for-byte identical**
before and after (`diff` on the extracted `WARN` lines returns empty, exit 0) — same 11
warnings, same codes, same files. The +2 in `ok` resolves to exactly two new individual
check-passes, confirmed by diffing the full output, not assumed from the total: `[C0]
Brattston_Article_Assessment.md: resolved at registered path` and `[C3]
Brattston_Article_Assessment.md: version agrees with registry (260835-49)`. Two further
checks' **coverage counts** move (`C5` 17→18 files scanned, `C8` 26→27) because those checks
run one aggregate `ok()` call over all files rather than one per file, so a newly-registered
file widens their scan without adding a separate `ok` line — reported here because the brief
asked for the real delta mechanism, not an assumed one. **The new source `.txt` file is
registered only in `SRC_Manifest.md`'s External Primary Texts table, which sits outside the
`PROJECT_STATE.md` §4 registry the C0/C3/C5/C8 checks scan — so it contributes zero new `ok`
lines, by design, matching how the Westall/BCP rows above it behave.**

---

## Diff verification — done properly, not asserted

The brief's suggested method (`git add --intent-to-add` on the two new files, then reset the
index) **could not be used**: the stale, unremovable `.git/index.lock` at gate (see Gate
section) blocks every index-writing git command, `git add` included. **Substituted method,
which never touches the index at all:** the diff was assembled by concatenating
`git diff -- PROJECT_STATE.md`, `git diff -- SRC_Manifest.md` (both tracked-file, read-only
diffs against `HEAD`) with `git diff --no-index -- /dev/null <newfile>` run once per new file
(also read-only; `--no-index` bypasses the index entirely and diffs two paths on disk
directly). This produces the same `diff --git a/… b/…` / `new file mode` hunks `git add
--intent-to-add` + `git diff` would have produced, verified below, and it has the advantage of
never staging anything, so there is no index state to reset.

- ✅ **Reverse-apply check CLEAN** (`git apply --reverse --check`, against the working tree).
- ✅ **Forward-apply check CLEAN against a pristine clone of `HEAD` `37be89a`**, then **actually
  applied** there (`git apply`, no `--check`).
- ✅ **Validator run in that clean applied tree returns `90 ok · 11 warnings · 0 errors`** — the
  AFTER figure reproduced from the diff alone, in a tree this pass never edited directly.
- ✅ **`sha256` of both new files in the applied tree exact-match the values registered in
  `SRC_Manifest.md`**: the source `.txt` at `4845fbef9c4a47f48595c319410c8d5ba7bc38f4d230a9b63445e5b9731dc1d9`,
  the assessment doc at `016e4fd1f01febf07916fe3cebd918b5576859594283780b0c629697653113d9`.
- ✅ **Exactly four files in the diff**: `PROJECT_STATE.md`, `SRC_Manifest.md`,
  `Brattston_Article_Assessment.md`, `src/SRC_PRIMARY_2003_Brattston_Incense_in_Ante-Nicene_Christianity.txt`.
- ✅ **`git status --short` in the real working tree, checked before this pass's first edit and
  again at close, shows the same two untracked-file shape plus this pass's own tracked-file
  edits — nothing was ever staged**, because the substituted diff method never calls `git add`.
  (The brief's own before/after `git status` identity check is satisfied trivially here: the
  index was never touched, so there is nothing to reset.)

### Artifacts written

- `passes/260835-49_brattston-article-assessment.diff` — 144,155 bytes, four files.
- `passes/260835-49_brattston-article-assessment_close-out.md` — this file.

---

## What this pass deliberately did NOT do

- ⛔ **`Patristic_Citations_Incense_Verification.md` and `Tertullian_Incense_Passages.md` NOT
  touched** — referenced by path and by citation, never edited.
- ⛔ **`St_Francis_EMC_Distinctives.md`, `RJ_Incense_Analysis.md`,
  `Incense_Conversational_Outline.md`, `Protestant_Commentary_Survey_Malachi_1_11.md` NOT
  touched.**
- ⛔ **`SRC_Coverage_Register.md` NOT touched** — per the `260835-35` §12 ruling this pass's
  own registry rows cite.
- ⛔ **`ORCHESTRATION.md` NOT touched. No `SRC_Discord_*` file touched.**
- ⛔ **`CLAUDE.md` NOT touched** — no change to this pass's own governing conventions was
  needed or made.
- ⛔ **Drafted nothing for Discord; posted nothing; nothing shown to Rev. James.**
- ⛔ **No content edit to `Brattston_Article_Assessment.md` beyond the one stamp line** — its
  research substance is the prior agent's work, not re-derived or second-guessed here.
- ⛔ **No `File`, `W`, `IP`, `LS`, `DQ`, `RC`, `BP`, `RV`, `EXT`, `GV`, `VP` or any other
  ledger-number prefix consumed.** This is registration of a third-party document, not a
  finding about Rev. James.
- ⛔ **No existing changelog entry, dated note, or registry row's text altered.** Every
  addition is a new dated note or a new row appended after the existing content, which is
  retained verbatim, per `CLAUDE.md`'s numbering-and-versioning rule.
- ⛔ **NOT COMMITTED.** `git commit` and `git push` were never run.

---

## Commit sequence for JD

```bash
cd ~/EMC/theology
rm -f .git/index.lock
git add Brattston_Article_Assessment.md src/SRC_PRIMARY_2003_Brattston_Incense_in_Ante-Nicene_Christianity.txt PROJECT_STATE.md SRC_Manifest.md passes/260835-49_brattston-article-assessment.diff passes/260835-49_brattston-article-assessment_close-out.md
git commit -m "260835-49: Brattston article assessed and registered — safe to circulate with one caveat (Apology 42 paraphrase reverses the funerary-purchase point); source article captured locally and hash-verified, a first for this document class; validator 90 ok / 11 warnings / 0 errors"
git push
git log -1
```

*(This close-out makes no claim about its own commit state — see "What this pass deliberately
did NOT do," last line.)*
