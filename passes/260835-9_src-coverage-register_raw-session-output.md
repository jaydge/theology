# Raw session output — 260835-9: `SRC_Coverage_Register.md`

Unsummarized commands and their output, supporting the close-out at `passes/260835-9_src-coverage-register_close-out.md`. Full validator AFTER run is a separate file, `passes/260835-9_validator-after.txt`, referenced rather than duplicated here.

## Gate

```
$ git --no-optional-locks rev-parse HEAD
b3f4c53e75f375c601be1cfc6cd0aa08d4065c0d
$ git --no-optional-locks status --short
(no output — clean)
```

## Next-free pass stamp derivation

```
$ grep -rhoE '26[0-9]{4}-[0-9]+' --include='*.md' --include='*.py' --include='*.txt' . | sort -u
... highest actual usage: 260835-8 ...
$ grep -rln "260835-9\|260835-10\|260835-11\|260836-" --include='*.md' --include='*.py' .
./passes/260835-8_readme-reconcile-and-project-knowledge-cleanup_close-out.md
```
That file's own text (lines 20, 262) states it already verified `260835-9`…`260835-12` and `260836-*` absent everywhere in tracked `*.md`/`*.py` at its own gate. This pass's independent grep agrees. **260835-9 confirmed free and used by this pass.**

## Validator BEFORE (3 independent runs, identical)

```
80 ok · 9 warnings · 0 errors
```
Nine WARN lines (verbatim, reproduced in `PROJECT_STATE.md`'s new gate note):
```
WARN [C1] src/SRC_Discord_RPW.md: 2 relative timestamp(s) outside message headers ('Yesterday at …')...
WARN [C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: no parseable 'Last updated' stamp; registry says '260832-2'
WARN [C3] tools/transcribe_yt.py: no parseable 'Last updated' stamp; registry says '260833-7'
WARN [C4] St_Francis_EMC_Distinctives.md: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby.
WARN [C5] RJ_Final_Question_List.md: 17 volatile-state assertions.
WARN [C5] RJ_Incense_Analysis.md: 9 volatile-state assertions.
WARN [C5] St_Francis_EMC_Distinctives.md: 7 volatile-state assertions.
WARN [C10] §15's newest LS citation is 8 findings behind the ledger (LS-120 vs LS-128).
WARN [C11] outline last checked against IP-97 (260833-5); the IP ledger now runs to IP-108. 11 finding(s) unreviewed.
```
(A stray, permission-denied `/tmp/baseline_validate.txt` from an unrelated prior sandbox boot was briefly misread as this session's own output — root `vigilant-optimistic-dijkstra` vs this session's `clever-great-clarke` — and discarded once noticed; it played no part in any finding below. Recorded here rather than silently dropped.)

## EXT-3 decision-cell cross-reference

```
$ grep -E "^\| \`[A-Za-z0-9_-]+\` \|.*EXT-3" SRC_Channel_Inventory.md > /tmp/e3.txt; wc -l < /tmp/e3.txt
62
$ grep -Ec "File 8\b|File 9\b|File 10\b|File 11\b|File 12\b|File 41\b" /tmp/e3.txt
20
$ grep -cE "INGESTED|DECLINED|CANDIDATE|UNRESOLVED" /tmp/e3.txt
47
$ grep -vcE "INGESTED|DECLINED|CANDIDATE|UNRESOLVED" /tmp/e3.txt
15
```
20 + 27 (other-registration decisions) = 47; 47 + 15 = 62. Confirmed against the table directly, not inferred.

## EXT-2 scope figures

```
$ grep -n "306" SRC_Channel_Inventory.md
3: ... @barelyprotestant5365 (EXT-2, 306 videos) and @StFrancisAnglicanSpartanburg (EXT-3, 62 videos) ...
18: ... 82 of the 306 EXT-2 rows here carry source_tab = videos; the remaining 224 carry source_tab = streams ...
```
`SRC_Disk_Reconcile_report.md` (external, `~/EMC/`, run 2026-08-25, gate HEAD `6b01d3992cb2cae8cc1b72813ff918c311199a65`) §7 Q4, read in full this pass: confirms `livestream-videos-list.txt` is 219 entries, all reading `Streamed`, zero `Uploaded` — settling the tab as `/streams`, falsifying `SRC_Channel_Inventory.md:18`'s own `/videos` guess. 224 − 219 = 5.

## Verification layer — full per-file hash check (this pass, fresh)

Script and full output (Files 1-35, 40-46, 42 files, direct sha256 against `SRC_Manifest.md`'s registered raw value):

```
$ python3 <hash-check script, run from ~/EMC/original transcripts/>
File 1: OK   File 2: OK   File 3: OK   File 4: OK   File 5: OK
File 6: OK   File 7: OK   File 8: OK   File 9: OK   File 10: OK
File 11: OK  File 12: OK  File 13: OK  File 14: OK  File 15: OK
File 16: OK  File 17: OK  File 18: OK  File 19: OK  File 20: OK
File 21: OK  File 22: OK  File 23: OK  File 24: OK  File 25: OK
File 26: OK  File 27: OK  File 28: OK  File 29: OK  File 30: OK
File 31: OK  File 32: OK  File 33: OK  File 34: OK  File 35: OK
File 40: OK  File 41: OK  File 42: OK  File 43: OK  File 44: OK
File 45: OK  File 46: OK

TOTAL checked: 42  present+match=42  mismatch=0  absent=0
```

Files 36-39 (hash of record held in each source's own `-meta.json` `outputs` block, not inline in `SRC_Manifest.md`) checked separately, against `BarelyProtestant-<name>-meta.json`:

```
36 PrayerOnlyToFather                    recorded=actual  MATCH
37 RomanTraditionAnglicansShouldEmulate  recorded=actual  MATCH
38 AnglicanIdentity                      recorded=actual  MATCH
39 JustinMartyrEucharistResponseToDrWhite recorded=actual MATCH
```

`a301-Classical-Theism.md` (rejected re-supply, not a registered File, checked for completeness): fresh sha256 `3551973355aa3518ca877f1d3e9de56ade8e560025d3fa19c3712b8e7bd56585`, size 29,338 — matches `SRC_Manifest.md`'s recorded value exactly.

**Combined: 46 of 46 registered File numbers present and hash-verified. Zero mismatches. Zero absences.**

## Absence re-check

```
$ find "/EMC" -iname "*A101-20260726-JD-recording*"
(no output)
$ find "/EMC" -iname "*07-26*" -o -iname "*0726*" | grep -v ".git"
.../in person classes/A101-20260726-official-video.md
.../in person classes/A101-20260726-handout-anglicanism-outline.pdf
.../downloads/ORCH_Handoff_260726-1.md
.../downloads/A101-20260726_260809-1_closeout.md
.../downloads/A101-20260726_260809-1_full.diff
```
The `[R]` primary itself (`A101-20260726-JD-recording-with-q-and-a.md`) is confirmed absent — only the `[S]` official-video rendering and pass artifacts referencing the session exist on disk.

## Validator AFTER

Full run in `passes/260835-9_validator-after.txt`. Summary: **82 ok · 9 warnings · 0 errors** — the same nine WARN codes as BEFORE, verbatim, zero new warnings, zero errors. The two new `ok` lines are `[C0] SRC_Coverage_Register.md: resolved at registered path` and `[C3] SRC_Coverage_Register.md: version agrees with registry (260835-9)`.

## Git status at close

```
$ git --no-optional-locks status --short
 M PROJECT_STATE.md
?? SRC_Coverage_Register.md
```
Nothing committed by this pass. Two untracked/modified pass artifacts also on disk under `passes/` (`260835-9_src-coverage-register.diff`, `_close-out.md`, `_raw-session-output.md`, `_validator-after.txt`) are new files pending the same commit as the two above, per `ORCHESTRATION.md` §4 (pass artifacts are committed with the change they describe).
