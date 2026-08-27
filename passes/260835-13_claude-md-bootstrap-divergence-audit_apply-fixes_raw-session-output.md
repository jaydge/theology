# Raw session output — 260835-13: apply fixes from the `260835-12` CLAUDE.md/Bootstrap divergence audit

Unsummarized commands and their output, supporting the close-out at
`passes/260835-13_claude-md-bootstrap-divergence-audit_apply-fixes_close-out.md`.

## Gate

```
$ git --no-optional-locks rev-parse HEAD
530d987fed5e3a9510cfdb837f40df7f70acc36d
$ git --no-optional-locks status --short
 M PROJECT_STATE.md
 M SRC_Channel_Inventory.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
?? passes/260835-12_diarization-verification-a101-room-and-batch9.diff
?? passes/260835-12_diarization-verification-a101-room-and-batch9_close-out.md
```
Tree was NOT clean at gate — see close-out's "pre-existing dirty tree" flag. None of the
five paths above were touched by this pass.

```
$ python3 validate_project.py
... (full run; coverage summary + all lines identical to the reproduction below) ...
82 ok · 9 warnings · 0 errors
```

```
$ head -30 PROJECT_STATE.md
# PROJECT_STATE — the single source of truth for VOLATILE state
**Last updated: 260835-12** (created 260724-3). Read this file first, before any other project document.
> ✅ GATE (260835-12). HEAD `98660cab...` ...
```
`PROJECT_STATE.md`'s own stamp: `260835-12`. Note this is the uncommitted diarization
pass's gate note, sitting on top of the `260835-11` gate note beneath it in the same file.

```
$ git log --oneline -5
530d987 260835-12: CLAUDE.md/Bootstrap divergence audit (read-and-report) ...
98660ca 260835-11: RC/BP retro-verification ...
07031e7 260835-11: Batch 9 selection ...
83bf85b 260835-10: never-triaged sweep ...
4363efa 260835-9: SRC_Coverage_Register.md created ...
```

```
$ grep -rhoE '26[0-9]{4}-[0-9]+' --include='*.md' --include='*.py' . | sort -u | tail -12
260834-9
260835-1
260835-10
260835-11
260835-12
260835-2 ... 260835-9
```
Highest real stamp: `260835-12` — appearing both as the committed audit commit and as the
uncommitted diarization pass's own gate note / filenames (the collision flagged in the
close-out). **This pass claims `260835-13`.**

## Verify-before-write

Both `CLAUDE.md` (197 lines) and `Project_Bootstrap_Prompt.md` (207 lines) were read in
full via the file tool before any edit. Every audit claim checked against current text:
line-for-line match, no drift. No item was skipped on a failed re-verification — all
verifications held.

## Edits applied

Three `Edit` calls total:

1. `Project_Bootstrap_Prompt.md` — transcript git-exclusion wording (item 1) + `SRC_Manifest.md`
   description rewrite (items 5, 6), single call, two adjacent bullets.
2. `Project_Bootstrap_Prompt.md` — Numbering and versioning: `RV` added to prefix list
   (item 10) + changelog-correction corollary appended (item 8), single call.
3. `Project_Bootstrap_Prompt.md` — new changelog entry prepended (covers items 1, 5, 6, 7
   [declined, recorded], 8, 10), single call.
4. `CLAUDE.md` — three new bullets inserted into §Source handling after the Anglican 101
   bullet: trimmed-original marking + dual-ASR protocol (item 3), Discord cross-reference
   (item 4), single call.

(Numbered 1-4 here for clarity; 3 total files touched across 4 `Edit` tool calls, all
succeeded on first attempt, no retries.)

## Validator AFTER

```
$ python3 validate_project.py 2>&1 | grep -E '^\s*(WARN|ERROR)'
  WARN  [C1] src/SRC_Discord_RPW.md: 2 relative timestamp(s) outside message headers ('Yesterday at …'). ...
  WARN  [C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: no parseable 'Last updated' stamp; registry says '260832-2'
  WARN  [C3] tools/transcribe_yt.py: no parseable 'Last updated' stamp; registry says '260833-7'
  WARN  [C4] St_Francis_EMC_Distinctives.md: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby. Review manually.
  WARN  [C5] RJ_Final_Question_List.md: 17 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] RJ_Incense_Analysis.md: 9 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] St_Francis_EMC_Distinctives.md: 7 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C10] §15's newest LS citation is 8 findings behind the ledger (LS-120 vs LS-128). Sweep the interval for creditable material.
  WARN  [C11] outline last checked against IP-97 (260833-5); the IP ledger now runs to IP-108. 11 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.
82 ok · 9 warnings · 0 errors
```
Identical to baseline, cell for cell. Zero new warnings, zero errors — expected, since
neither edited file's stamp moved and neither warning check reads the sections touched.

## Git status at close

```
$ git --no-optional-locks status --short
 M CLAUDE.md
 M PROJECT_STATE.md
 M Project_Bootstrap_Prompt.md
 M SRC_Channel_Inventory.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
?? passes/260835-12_diarization-verification-a101-room-and-batch9.diff
?? passes/260835-12_diarization-verification-a101-room-and-batch9_close-out.md
?? passes/260835-13_claude-md-bootstrap-divergence-audit_apply-fixes_close-out.md
```
This pass's own two files (`CLAUDE.md`, `Project_Bootstrap_Prompt.md`) plus this
close-out. The remaining five lines predate this pass. Nothing staged, nothing committed.

## Full diff (this pass's two files only)

See `git diff -- CLAUDE.md Project_Bootstrap_Prompt.md`, 109 lines, reproduced in full in
the session's final chat response and in the close-out file.
