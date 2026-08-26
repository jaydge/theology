# 260834-4 — `DQ-24`(b) italicization flag discharged; Discord emphasis-loss capture rule registered

## Gate check (run, not assumed)

- `git rev-parse HEAD` → `24a0a5046d41f197ca9e1c4128f4f770b9fb35e8` (`24a0a50`), exactly as briefed.
- `python3 validate_project.py` baseline: **80 ok · 9 warnings · 0 errors**, confirmed by running, not assumed. Firing codes (from the run's own coverage listing): C1 (relative timestamps outside message headers), C3 ×2 (unstamped files), C4 (unmarked-pending passages), C5 ×3 (volatile-state assertions), C6 (archive hash integrity — OK, listed for coverage), C7 (relay-clean firewall, WARN-only, suspended — OK), C8 (dangling question-ID cross-references — OK), C9 (do-not-deploy consistency — OK), C10 (§15 staleness — OK), C11 (outline-vs-findings drift — OK), C12 (session-registry integrity / dual capture — OK). Total: **80 ok · 9 warnings · 0 errors**, matching the brief's expectation exactly.
- `git status --short` before any edit: clean (no output).
- `PROJECT_STATE.md`'s "Last updated" stamp: **`260834-3`**, exactly as briefed.

## Pass stamp derivation

Repo-wide grep for `26[0-9]{4}-[0-9]+` across every `.md`/`.py` file, sorted: highest is `260834-3`. Derived pass stamp: **`260834-4`**.

## Item 1 — `DQ-24`(b)'s italicization flag discharged by dated note, never rewritten

`St_Francis_EMC_Distinctives.md`'s `DQ-24`(b) entry (minted `260834-3`) flags that the claimed italicization of *"must"* in Rev. James's reply could not be verified against either `src/SRC_Discord_RPW.md` or the committed raw `src/SRC_Discord_RPW-raw.txt` — no markdown emphasis markup surrounds the word in either source.

JD has since supplied a direct screenshot of the Discord client showing his original message with both *"must"* **and** *"anyone"* italicized (the second word not previously flagged as missing from the brief — it wasn't in scope of the original claim, so its absence from the entry isn't an error, but the entry now records it per this pass's instruction).

**Action taken, per the never-alter rule:** the original flag at `DQ-24`(b) is left standing exactly as written — it remains an accurate record of what the archived `.md` and `.txt` show, and that has not changed (still no markup around either word in either archive). A dated note (`260834-4`) is added immediately beside it, recording:
- The warrant: JD's own direct screenshot of the Discord client — a platform-rendered capture, not a re-typed recollection, and evidentially stronger than the copy/paste archive for the purpose of confirming emphasis.
- That *"anyone"* is also italicized in the original, which the flag entry did not note.
- That the archived `.md`/`.txt` text is **not** retroactively marked up — the quote as reproduced in the `DQ-24`(b) entry remains in plain form, and a reader who needs the emphasis should consult the screenshot rather than the archive.

This is deliberate: per the newly registered capture-method limitation (Item 2 below), Discord copy/paste cannot be trusted to preserve emphasis even going forward, so adding italics markup to the archive on the strength of one screenshot would misrepresent what the archive itself is capable of attesting.

## Item 2 — Discord emphasis-loss capture rule registered in `SRC_Manifest.md`

**Finding:** Discord's copy/paste capture method (the standing capture method for every `SRC_Discord_*.md` file in this corpus) preserves paragraph breaks but does **not** preserve markdown emphasis (italic/bold) — it strips it silently, with no marker or artifact indicating emphasis was present in the original.

**Placement:** registered as a dated note (`260834-4`) directly beside the `260801-3` changelog entry — the entry that originally tested and put on record the three existing capture-method limitations: (1) no `(edited)` marker survives copy/paste, (2) same-day timestamps render bare, (3) paragraph breaks *are* preserved. The new finding is written as a fourth item in that same list, beside the original (never-alter — the `260801-3` entry itself is untouched).

**Consequence, stated plainly per instruction, not acted on:**
- No archived Discord message in this corpus can be relied on for emphasis.
- Any existing finding resting on emphasis is unwarranted unless separately verified.
- A corpus-wide sweep for findings that rest on emphasis is **owed** and is **deliberately not run this pass** — the instruction was to register the rule, not hunt for affected findings.

**Forward-looking implication, recorded:** where emphasis is argumentatively load-bearing, a screenshot taken alongside the paste is the reliable capture method going forward — exactly the method that discharged Item 1 above.

## Files touched, and why

- `St_Francis_EMC_Distinctives.md` — dated note added beside `DQ-24`(b)'s flag; changelog entry added; stamp bumped `260834-3` → `260834-4`.
- `SRC_Manifest.md` — dated note added beside the `260801-3` capture-method-limitations entry; changelog entry added; stamp bumped `260834-3` → `260834-4`.
- `PROJECT_STATE.md` — gate note and pass note added; §4 registry version cells for `PROJECT_STATE.md` itself, `St_Francis_EMC_Distinctives.md`, and `SRC_Manifest.md` all bumped to `260834-4` (kept in lockstep with the documents' own stamps per C3, which errors on version drift between a document's own "Last updated" line and this file's registry cell).

## Files deliberately NOT touched

- `RJ_Incense_Analysis.md` — not opened.
- `On_Incense_and_the_Altar.md` — not opened.
- `src/SRC_Discord_RPW.md` and its raw artifact `src/SRC_Discord_RPW-raw.txt` — not touched. No message body text was altered; no hash, byte offset, or coverage figure for either file changed.
- No sweep was run for other findings that might rest on emphasis, per explicit instruction that this is owed to a future pass.
- Nothing drafted, altered, or posted toward Rev. James.

## Post-pass validator result

`python3 validate_project.py`: **80 ok · 9 warnings · 0 errors** — identical totals to baseline, same firing codes (C1, C3 ×2, C4, C5 ×3, C10, C11, C12, plus the WARN-only-suspended C7 and the coverage-only C6/C8/C9 listed OK). No new warnings or errors introduced by either edit: both additions are dated notes beside existing entries, adding no relative timestamps, no version-stamp mismatch (both documents' own stamps and the `PROJECT_STATE.md` §4 cells were bumped together), no new volatile-state duplication, and no touched question-ID cross-reference.

## Environment note, recorded rather than acted on

A `.git/index.lock` file (0 bytes) is present in the working tree, and one `git` invocation during this pass emitted `warning: unable to unlink '.git/index.lock': Operation not permitted` while otherwise completing successfully. This pass did **not** create or attempt to remove this lock file deliberately — it was not created by any command this pass issued to write content, and `git status`/`git diff` both completed correctly despite it. This is the same permission-mount lock behavior already on record in this project's history (see `PROJECT_STATE.md`'s `260831-2` gate note, which records an identical `.git/index.lock` presence with the same cause). Reported here as environment state, not as a defect this pass introduced or attempted to fix.

## What JD should stage

All three modified files belong in a single commit for this pass — they form one coherent change (a discharge note plus the capture-rule registration it depends on, plus the bookkeeping stamps that keep C3 clean):

```
git add PROJECT_STATE.md SRC_Manifest.md St_Francis_EMC_Distinctives.md
git commit -m "260834-4: DQ-24(b) italics flag discharged (screenshot); Discord emphasis-loss capture rule registered"
```

No other files are modified. `git status --short` shows exactly these three lines:

```
 M PROJECT_STATE.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
```

## Declined / not run

- No sweep of the corpus for emphasis-dependent findings (explicitly owed to a future pass).
- No edit to `src/SRC_Discord_RPW.md`, its raw artifact, `RJ_Incense_Analysis.md`, or `On_Incense_and_the_Altar.md`.
- Nothing drafted, altered, or posted to Rev. James.
- The `.git/index.lock` file was not removed or investigated further — outside this pass's scope and not blocking any command it needed to run.
