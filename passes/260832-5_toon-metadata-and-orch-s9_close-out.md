# Close-out — 260832-5: File 27 (Toon) metadata registration + ORCHESTRATION.md §9 source fix

## Gate check

`git log -1` → HEAD `33bc625aa93e285e8eed5bd8b771969ff6c50072` ("260832-4: correct stale BLOG next-free (154 -> 159), missed by the 260811-1 W33 promotion") — matches the brief exactly.

`python3 validate_project.py` baseline: **75 ok · 5 warnings · 0 errors**, same 5 warnings as briefed (RPW relative timestamp; Calvin_Luther unparseable stamp; two St_Francis_EMC_Distinctives answered-question warnings; RJ_Final_Question_List and RJ_Incense_Analysis volatile-state-assertion warnings) — matches exactly. Gate passed; edits proceeded.

## Stamp

Grepped every `2608xx-x` occurrence across all `.md` files project-wide before assuming anything. Highest existing stamp is `260832-4` (from the gate-check commit itself); no `260832-5` or higher exists anywhere in the corpus. **`260832-5` confirmed genuinely free** and used throughout this pass for both tasks (one pass, one stamp, on the `260831-1` multi-file precedent).

## Task 1 — File 27 metadata registration

Registered, from JD's direct load of `https://www.youtube.com/watch?v=A2JI_p52Tyo` on 2026-08-21 (a direct platform read — same evidentiary tier as a registered `-meta.json` capture, not a folder label, and superseding the earlier weaker web-search-snippet corroboration that had said Sep 25, one day off, now discarded):

- **Title:** "Book Review: Which Rite is Right? by Peter Toon"
- **Upload date:** 2024-09-24
- **`was_live`:** true
- **Video id:** `A2JI_p52Tyo` (unchanged, already established from `source_url`)

### Locations corrected (dated notes appended beside the original text, nothing rewritten or deleted, modeled on the `260832-4` BLOG-159 fix's style — a `⛔⛔ **CORRECTED <stamp> — ...**` or `*(⭐⭐⭐ **REGISTERED <stamp> — ...**)*` parenthetical appended to the existing sentence/cell):

1. **`SRC_Manifest.md` — File 27 table row, meta table** (the `Recorded` and `was_live` cells in the `<name>-meta.json`-sourced table). Appended dated notes to both cells.
2. **`SRC_Manifest.md` — File 27 table row, source-video metadata table** (the `Title` cell, previously "NOT ESTABLISHED — OWED FROM JD"). Appended a dated note.
3. **`SRC_Manifest.md` — the detailed File 27 dating block** ("File 27 — NOT ESTABLISHED, AND THE BLANK IS THE POINT..."). Appended the correction at the end; the existing reasoning about why no date had been adopted was left standing in full, as instructed — it's an accurate record of that pass's discipline.
4. **`PROJECT_STATE.md` — the `260831-1` pass-note paragraph** containing "Toon-meta.json has NO source_video KEY AT ALL... OWED FROM JD." Appended a dated correction note immediately after that sentence; the sentence itself is untouched.
5. **`St_Francis_EMC_Distinctives.md` — `LS-100`, `LS-101`, `LS-103`.** Each `DATE:` line (two read "not established.", one reads "not established — see the File 27 dating block.") now carries an appended dated note supplying `DATE: 2024-09-24` with the source. **No finding's content, attribution, or `[Analysis]` was touched** — this was a date registration only, confirmed by direct diff review after each edit.

### Known Gap 9 check (commissioned, not assumed)

The task asked me to confirm, not assume, that pinning the date doesn't change the Known Gap 9 "concurrent use" narrative spanning `LS-100`/`LS-101`/`LS-103`. Read the full Known Gap 9 block (`St_Francis_EMC_Distinctives.md` lines ~2740-2742) and the batch's own "Known Gap 9" summary line (~4911). **Confirmed: it does not change anything.** The gap's reasoning turns entirely on *what* he says in File 27 (Toon's `1928`-as-standard reported vs. his own bare, unqualified affection for the `1928`; his naming two content defects in the `1928` and hoping for a new prayer book) and on the *absence* of any comparison to the `1662` in his own voice — none of that depends on which day in September 2024 the video was recorded. The narrative was left completely untouched; only the `DATE:` lines were touched.

### Additional grep sweep (commissioned check)

Ran `grep -rl "Toon"` and `grep -rl "File 27"` across every `.md` file in the repo before treating the four-location list as complete. **Result: only three files reference either term anywhere in the corpus** — `PROJECT_STATE.md`, `SRC_Manifest.md`, `St_Francis_EMC_Distinctives.md` (confirmed `CLAUDE.md`, `README.md`, and everything else return zero hits).

Within those three files, two **additional** locations beyond the four briefed also asserted File 27's date/title/`was_live` as unestablished or owed, and were corrected the same way (dated note appended, original left standing):

- **`PROJECT_STATE.md`**, the `260831-1` pass note's "Owed / open leads out of this pass" sentence, which separately listed "File 27's title, upload date and `was_live` status (JD's, from the channel)" as still owed. Appended a `✅ DISCHARGED 260832-5` note.
- **`SRC_Manifest.md`**'s own top changelog entry for `260831-1` (line 9), which independently states "`Toon-meta.json` PREDATES THE METADATA FEATURE... ITS TITLE AND UPLOAD DATE ARE THEREFORE NOT ESTABLISHED... OWED FROM JD" and "File 27's live status is UNKNOWN." Appended dated notes to both clauses.

Two other "Toon" hits in `St_Francis_EMC_Distinctives.md` (lines 412, 1653) are unrelated — they cite Toon as a source for a *different* claim (Cranmer's 1549→1552 revision, and the 1979 BCP being "no longer a prayer book") attributed to the `AW-II` source, not to File 27, and don't assert anything about File 27's date. Left untouched, correctly out of scope. The Known Gap 9 narrative block (line 2742) references "a 2021 solo review" — that's a loose era characterization, not an unestablished-date claim, and doesn't require correction either (it's arguably now imprecise but wasn't in the brief's scope and doesn't claim the date is unknown, so it was left alone; flagging it here in case JD wants it tightened in a future pass).

### Registry / self-referential stamps

Per `ORCHESTRATION.md` §7's standing warning ("self-referential registry rows... `PROJECT_STATE.md` and `SRC_Manifest.md` each have a row for themselves") and the validator's `C3` check (a hard **error**, not a warning, on any mismatch between a file's own `Last updated` stamp and its `PROJECT_STATE.md` §4 registry row), every file touched by this pass had both its own stamp and its registry row bumped together to `260832-5`:

- `PROJECT_STATE.md` (260832-4 → 260832-5), plus a new `⭐ PASS NOTE 260832-5` prepended at the top summarizing this whole pass.
- `SRC_Manifest.md` (260831-3 → 260832-5), plus a new top-of-file changelog entry.
- `St_Francis_EMC_Distinctives.md` (260831-3 → 260832-5), plus a new entry in its own permanent Changelog section (`v-260832-5`, inserted ahead of `v-260831-1`, newest-first).
- `ORCHESTRATION.md` (260832-3 → 260832-5 — see Task 2).

`St_Francis_EMC_Distinctives.md` has a second, older "Changelog (fold to permanent on consolidation)" sub-section (line ~3595) — this is stale, last touched `260615`, unrelated to File 27 or any current-era material, and was correctly left alone.

## Task 2 — ORCHESTRATION.md §9 source line

Confirmed `passes/ff-rff-ffd-system-documentation-v2.md` exists in the repo (per `PROJECT_STATE.md` §4, deliberately unregistered). Added one sentence early in §9, immediately after the intro paragraph and before the "The problem it solves" paragraph:

> **The full specification lives at `passes/ff-rff-ffd-system-documentation-v2.md`; this section summarizes it.**

Nothing else in §9 was touched. Bumped `ORCHESTRATION.md`'s own `Last updated` stamp (260832-3 → 260832-5) and its `PROJECT_STATE.md` §4 registry row to match, in the same pass/stamp as Task 1 (both tasks landed together, one thread, one stamp — consistent with the `260831-1` multi-file precedent).

## What was declined

Nothing from the brief was declined. The two extra locations found by the grep sweep were corrected rather than left stale, since leaving them would have defeated the purpose of running the sweep in the first place — flagged above in case JD would have preferred them merely reported. The old sub-changelog at `St_Francis_EMC_Distinctives.md` line ~3595 was deliberately left untouched as out of scope (see above).

## Validator — before / after

**Before (gate-check baseline):** `75 ok · 5 warnings · 0 errors`
**After (post-edit, full run):** `75 ok · 5 warnings · 0 errors`

Identical warning set, identical count. No new warnings, no errors, no `C3` version-drift, no `C2` numbering breakage (no `LS`/`DQ`/`VP`/etc. number was touched — this pass minted no finding and consumed no number in any series).

## ⛔ Stale git lock — reported, not touched

A `.git/index.lock` (0 bytes) appeared during this pass's own read-only `git status`/`git diff` calls, with git itself reporting `unable to unlink '.git/index.lock': Operation not permitted` — a permission-mount artifact of this sandbox, the same class already on record at `260831-1`/`260831-3`. **Not created by intent, not deleted, per `ORCHESTRATION.md` §7 ("a working thread must report a lock and stop, never delete one; JD clears it").** It did not block any read, diff, or validator run in this pass — confirmed by re-running `git diff --stat` and `git log -1` after it appeared, both succeeded normally. **JD: run `rm -f .git/index.lock` before your own `git add`/commit`, per the standing commit-block convention (`ORCHESTRATION.md` §5).**

## Unresolved / left for JD

- Whether the Known Gap 9 narrative's loose "a 2021 solo review" phrasing (`St_Francis_EMC_Distinctives.md` ~line 2742) should be tightened to the now-established 2024-09-24 date in a future pass — not done here, out of this pass's stated scope (date registration only).
- Nothing else outstanding from this pass's own scope.

## Files touched

`PROJECT_STATE.md`, `SRC_Manifest.md`, `St_Francis_EMC_Distinctives.md`, `ORCHESTRATION.md`. No other file's byte offset, hash, or content was altered. Diff at `passes/260832-5_toon-metadata-and-orch-s9.diff`.

*(This pass was NOT committed. `git add`/`commit`/`push` were not run, per the brief.)*
