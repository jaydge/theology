# 260835-37 — Duplicate-registration sweep, `LS-123` earliest-instance correction, and consolidated owed-items sweep (close-out)

**Mode:** Small-items pass, three tasks. **Committed:** nothing — per the brief, JD pushes `passes/` first, then corpus edits separately. No `.diff` accompanies this close-out; the corpus edits are described in full below and are visible in `git status --short` / `git diff` on request.

---

## Gate

| Item | Value |
|---|---|
| `git rev-parse HEAD` | `e0c1c985084a559260cb1f6044e6293fb90ca160` |
| Matches briefed `e0c1c98` | ✅ Yes, exactly |
| Branch | `main` |
| `git --no-optional-locks status --short` before first edit | **EMPTY** (captured directly, not reconstructed) |
| Validator BEFORE | **`85 ok · 8 warnings · 0 errors`** |
| `[C10]` gap at gate | **17** findings (`LS-120` vs `LS-137`) — ⭐ confirmed exactly as the brief flagged it should read after `260835-36`'s minting, not assumed |
| `PROJECT_STATE.md`'s own stamp at gate | `260835-36` |
| Next-free pass stamp | `260835-37` — derived fresh by grep after reading the `260835-12`/`260835-14` hazard note first (both re-confirmed REAL and CONSUMED, commits `530d987`/`68bf1d8`); distinct-stamp sweep over tracked `*.md`/`*.py`/`*.txt` tops out at `260835-36` with no gaps; `ls passes/` and `git log --all` (HEAD commit `e0c1c98`) independently agree; `260835-99` re-checked and re-confirmed as a false-positive absence-assertion, not a stamp; `260835-37` and `260836-*` both return zero live matches repo-wide |

Baseline warnings (all eight, unchanged from `260835-36`'s own gate, reproduced verbatim, not touched by this pass):

1. `[C1] src/SRC_Discord_RPW.md` — 2 relative timestamps outside message headers.
2. `[C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` — no parseable stamp; registry says `260832-2`.
3. `[C3] tools/transcribe_yt.py` — no parseable stamp; registry says `260833-7`.
4. `[C4] St_Francis_EMC_Distinctives.md` — 2 stale answered-question passages.
5. `[C5] RJ_Final_Question_List.md` — 17 volatile-state assertions.
6. `[C5] RJ_Incense_Analysis.md` — 9 volatile-state assertions.
7. `[C5] St_Francis_EMC_Distinctives.md` — 7 volatile-state assertions.
8. `[C10]` — §15's newest `LS` citation 17 findings behind the ledger head.

---

## Item 1 — Duplicate-registration sweep (priority item)

**The defect, restated.** `260833-8` keyed `SRC_Channel_Inventory.md` on video ID. `260834-1` registered five `batch5b` videos in `SRC_Manifest.md` keyed on source basename. Nothing ever reconciled the two keys. `260835-36` discovered that two of the five (`RBkgXuUT_jw` = `File 37`, `TePiEoY1N1o` = `File 39`) were already registered and already mined, yet still carried a live `INCLUDE — T1` verdict in the inventory — and corrected both. **But `260835-36` checked only the two videos its own delegating brief happened to name, not the rest of the same five-video batch it had just re-examined.**

**Method.** Every `SRC_Channel_Inventory.md` row NOT already marked `INGESTED`/`REGISTERED` (240 rows: 183 `INCLUDE`, 34 `DECLINED`, 11 `DECLINED-office`, 8 `UNCERTAIN`, 4 `EXCLUDE-*`) was checked against `SRC_Manifest.md` on **multiple keys, never a single one**: (a) every backtick-enclosed 11-character token in the manifest (the video-ID key space, exhaustive — 142 distinct tokens found, checked both with and without the backtick requirement to rule out prose mentions outside markdown formatting); (b) a full-title and 4-word-phrase substring match against the whole manifest, normalized for case and markdown emphasis, to catch anything a video-ID-only check would miss (a basename-only registration, a title recorded without its video ID nearby).

**Confirmed collisions — three, all part of the same `260834-1` `batch5b` five-video intake `260835-36` partly caught:**

| Video ID | File | Findings | Title | Prior inventory verdict |
|---|---|---|---|---|
| `ZGntccYaUn0` | `File 35` | `LS-124`, `LS-125` | *Can (Should) We Pray to the Saints?* | `INCLUDE — T1`, 260835-23 |
| `Pf1cKIB-HtU` | `File 36` | `LS-122`, `LS-123` | *Must Prayer Be Directed ONLY to the Father?* | `INCLUDE — T1`, 260835-23 |
| `qiY_-16GMrs` | `File 38` | `LS-121` | *Anglican Identity (Adult Formation Class)* | `INCLUDE — T1`, 260835-23 |

The finding-to-File mapping was verified directly against `St_Francis_EMC_Distinctives.md`'s own `LS-121`…`LS-128` entries (each names its source File and date explicitly), not inferred from the manifest's summary prose alone.

**Corrections applied.** All three rows in `SRC_Channel_Inventory.md` corrected as **dated reclassifications retaining the prior verdict verbatim** after `*Previously:*`, per the never-alter rule — the same convention the file's own header describes, though `260835-36`'s own File 37/39 corrections did not in fact retain the prior text (an inconsistency noted here, not corrected there — those rows are not this pass's business to re-touch). `ZGntccYaUn0`'s row also retains its own pre-existing DEDUPE-FIRST flag against `IP-47`/`File 62` (`6Z68nITG1Is`) as a still-open, separate content question, not resolved by this reclassification.

**Everything else checked, one flag, no other collisions.** The remaining 237 target rows returned clean on both the video-ID and title-phrase checks. The title-phrase check surfaced two candidates on inspection:

- `uJIYRal3Qnc` ("How to Use the 1928 (US) Book of Common Prayer for Matins/Evensong") against the manifest's registered "How to Use the **2019** Book of Common Prayer" — different prayer-book edition, different video ID (`ulrD_RdI6Q0`), different upload date. **Ruled out — not a match, a coincidental phrase overlap.**
- `pHqKPBpQR7c` ("Anglican Class, Session I: Introduction (**But Sideways**)", `EXT-3`, uploaded 2026-06-29, 4062s, 57 views) against the registered `A101-2026-06-14-P1` `[S]` capture, titled "Anglican Class, Session I: Introduction" (header-dated 2026-06-14, held outside the repo with **no video ID recorded against it**). **Plausible but unproven — flagged, not reclassified.** The upload date is 15 days later than the registered session; the "(But Sideways)" suffix is unexplained by anything on record (could denote a rotated re-upload of the same broadcast, or a genuinely distinct recording); and the registered capture carries no video ID to cross-check against, so the one durable key this sweep otherwise relies on is unavailable here. A note is added to the row in `SRC_Channel_Inventory.md` recording the flag and the reasoning, per the `260835-30` precedent (a whole batch found already-registered on an unswept assumption) — the caution that precedent teaches.

**Structural lesson recorded.** A new §8 standing instruction added to `ORCHESTRATION.md`: reconcile the channel inventory against the manifest on video ID, and only video ID — titles are edited by the channel after posting (the `260835-25` session-renumbering precedent) and basenames are chosen per-batch with no cross-batch discipline. The procedure: before minting a File number, grep the whole manifest for the row's video ID as a bare 11-character token; after any batch registration, sweep every video ID in that batch against the inventory's decision cells, not only the video(s) a brief happens to name. Title/basename matching keeps a supplementary role (it is how the pre-`-meta.json` Files 1-26 were reconciled at `260833-8`) but is never a substitute for the video-ID sweep where a video ID exists on both sides.

**Nothing minted.** No File, finding, or number of any prefix consumed. Nothing re-mined — the three corrections carry only the pre-existing File numbers and finding ranges already on record in `SRC_Manifest.md`.

---

## Item 2 — `LS-123`'s earliest-instance claim

`260835-36` already established, evidenced, and recorded the correction: `LS-130` (`File 39`, 2024-08-31) is the same Malachi 1:11 → incense-as-practice move as `LS-123` (`File 36`, 2024-09-18), eighteen days earlier. That correction was written up inside `LS-127`'s own dated note in `St_Francis_EMC_Distinctives.md` (the note explains `LS-130`'s discovery, which falsified part of `LS-127`, and mentions the `LS-123` supersession as a secondary point) — but no note was ever placed directly beside `LS-123`'s own entry.

**Repeat-occurrence check.** `RJ_Incense_Analysis.md` does not mention `LS-123` anywhere (`git grep` verified, zero hits) and contains no "earliest" claim about the Malachi 1:11 incense move at all. `PROJECT_STATE.md`'s occurrences of `LS-123` are exclusively inside historical, append-only gate/pass-note prose (the `260835-36` note itself, quoted and requoted at each subsequent gate) — these are the permanent record of what each pass knew at the time and are not live claims requiring correction. **No other document repeats the "earliest-dated" characterization.**

**Correction applied.** A dated note (260835-37) placed directly beside `LS-123`'s own entry in `St_Francis_EMC_Distinctives.md`, between `LS-123` and `LS-124`, stating plainly that `LS-130` is now the earliest instance, eighteen days earlier, and that this is a priority correction, not a falsification — `LS-123`'s own quotation, attribution, and analysis stand unchanged. `LS-123` itself is **not** altered. `RJ_Incense_Analysis.md` §4.6/§4.8/§4.10 **not** touched (still falsified-pending-revision, per the brief's explicit prohibition).

---

## Item 3 — Consolidated owed/flagged/reserved-to-JD sweep, `260835-27` through `260835-36`

Read-and-report only. **Nothing below is resolved, ruled on, or acted on by this pass**, except where explicitly marked discharged by Item 1 above.

### A. RPW Discord thread / reception-criterion (`DQ`) material

1. Missing `CAPTURED …` line in `src/SRC_Discord_RPW-raw.txt` — owed before JD's next recapture (flagged `260835-26`, restated `260835-28`). **Open.**
2. Message-19 `U+202F` Unicode anomaly — "still unmoved, still awaiting JD's ruling" (`260835-28`). **Open.**
3. `OQ20` — durational threshold for "received" still unstated (moves `260835-26`/`-28`/`-31`, never closes). **Open.**
4. Whether the burden rule and `LS-23`/`LS-24`'s consensus-authority ranking are one rule or two — "his to say" (`260835-31`/`-32`). **Open.**
5. Whether allowance is the TEST or only EVIDENCE of church-wide reception (`DQ-26`(g) hedge) — undecided (`260835-31`/`-32`). **Open.**
6. Characterization of the `DQ-25`→`DQ-26` amendment (developed / clarified / inconsistent) — expressly reserved as "JD's judgment" (`260835-28`/`-31`). **Open.**
7. JD's `260835-27` circularity objection to the reception criterion — `OQ21`'s reserve condition is satisfied, but the objection itself is "JD's to spend, not a pass's" (`260835-32`). **Open.**
8. Flagged-but-unrevised outline passages: Step 3(c)/(d)'s non-exhaustive fork, Step 4's falsified first horn, Step 5's falsified "intramural" claim, Step 10's overstated universality prong (`260835-31`/`-32`). **Open.**
9. The word "knowingly" in Step 4's note vs. `IP-98`'s "by the way" guard — called "JD's one-word call" (`260835-32`). **Open.**
10. Sequencing decisions: fix flagged sentences before or after opening the incense topic; write the pedagogy step before or after naming incense — "his calls, flagged not made" (`260835-32`). **Open.**
11. `IP-101` pedagogy-warrant gap — no outline step covers it; "the scoped pass is owed" (`260835-32`). **Open.**
12. `IP-98` byte-range discrepancy (`PROJECT_STATE.md` L29 vs. the §13 bullet) — "owed to a pass with `a101-2.md` in scope, not this one" (`260835-32`). **Open.**
13. `C11`'s pointer-regex truncation defect — the check's own regex is `rf'\b{{pfx}}-(\d+)[a-z]?\s*@\s*(\d{{6}}-\d)'`, six digits/dash/**one** digit — the identical truncation shape `C3` carried until it was fixed at `260835-22`, still live in `C11`. Found and reported `260835-31`, restated `260835-32`, never repaired. **Open.**

### B. `RJ_Incense_Analysis.md` / outline

14. §4.6/§4.8/§4.10 falsified-pending-revision — open since `260835-15`, restated in every close-out through `260835-36`. **Open** (explicitly out of scope for this pass, per the brief).
15. §4.13's cross-reference to `LS-127` inherits `LS-127`'s now-corrected error (the "never engages incense as practice" claim `LS-130` falsified) — the file is off-limits to the pass that found this (`260835-36`). **Open.**
16. `LS-133`(a) vs. `IP-52` (the monstrance) — flagged for JD, neither entry edited (`260835-36`). **Open.**
17. `LS-137` vs. `IP-69` (blasphemy) — flagged for JD, three readings offered, none chosen (`260835-36`). **Open.**
18. §15's `LS`-citation staleness (`[C10]`, now 17 findings behind the ledger head, confirmed at this pass's own gate) — not swept, flagged rather than silently left (`260835-36`). **Open.**

### C. Batch-11 Anglican Class attribution (`260835-30`)

19. `File 62` canonical date vs. the "session identity vs `A101-2026-08-09` UNRESOLVED" flag — corroborated by date coincidence, but the standing do-not-mine flag is explicitly not discharged. **Open.**
20. `SRC_Coverage_Register.md` §3's full `EXT-3` recount — explicitly left owed rather than forced. **Open.**
21. Session VI "Father Brian" discrepancy — JD's recollection not corroborated by that session's own content; recorded as a discrepancy, not reconciled. **Open.**
22. ~~A systematic `SRC_Channel_Inventory.md` video-ID reconciliation, flagged as owed at `260835-36`~~ — **DISCHARGED by this pass's own Item 1, above.** No longer open.

### D. Westall / Purchas / 1899-Opinion research (`260835-33` through `-35`)

23. The `260835-35` folio-locator divergence's underlying cause — the wrong `§§1–5` locators were corrected value-by-value, but *why* they diverge non-monotonically from the printed folios (a constant-offset JSON mapping can't explain it) remains an unresolved diagnosis. **Open** — matches the brief's own flagged item.
24. The final appendix's letter, "I" vs. "J" — genuinely ambiguous in the OCR scan (heading reads "I," contents page prints "J"); noted as cheaply closable, not attempted. **Open.**
25. Hope's four OCR-corrupt Appendix-G table cells (Worcestershire/Cumberland/Surrey/Essex) — recovered only by arithmetic, not read from source. **Open** (minor).
26. Lacey's Cotton MS reference — unchecked, external manuscript. **Open.**
27. *Directorium Anglicanum* — never read; standing gap since `260835-33`. **Open.**
28. Full texts of *Hebbert v. Purchas* and *Ridsdale v. Clifton* — not read; flagged as now more load-bearing (`260835-34`). **Open.**
29. Full text of the Lincoln Judgment (89 pp.) — not read. **Open.**
30. Two minor page-citation slips in `260835-34`'s own §4b, and the 1549/1552 table columns not proof-read line-by-line — flagged, not corrected. **Open** (minor).

### For contrast — resolved within this span, not open

`DQ-24`'s offset breakage and the changelog-prepend offset hazard (`260835-29`); the `C11` outline review's `DQ` arm (`260835-31`) and `IP` arm (`260835-32`, both arms now current); the Westall Appendices B–J retrieval (`260835-34`); the Purchas correction to `RJ_Incense_Analysis.md` §8 (`260835-35`); the folio locators themselves, Appendix D's table, and the Geldart footnote-attachment question (`260835-35`).

---

## Files touched

| File | What changed |
|---|---|
| `SRC_Channel_Inventory.md` | Three rows reclassified `INCLUDE` → `INGESTED` (dated, prior verdict retained); one row flagged (not reclassified); header stamp/pass-note updated. |
| `ORCHESTRATION.md` | One new §8 standing instruction (video-ID reconciliation); header stamp updated. |
| `St_Francis_EMC_Distinctives.md` | One dated note beside `LS-123`; header stamp and changelog updated. |
| `PROJECT_STATE.md` | Gate/pass note prepended; §4 registry rows bumped for all three files above plus this one. |

`Incense_Conversational_Outline.md` — **not touched.** Nothing drafted, altered, or posted to Rev. James. No finding minted. No ledger number of any prefix consumed.

## Validator AFTER

**`85 ok · 8 warnings · 0 errors`** — byte-identical to baseline. No regression, no new warning class, all eight baseline warnings reproduced exactly (including `[C10]`'s 17-behind gap, unchanged by this pass since nothing was minted). `[C3]` passes clean on all four touched files' registry cells.

## `git status --short` at close

See the delegating session's own report for the live listing at hand-off — this pass makes no commit and stages nothing, per the brief's explicit instruction (JD pushes `passes/` first, then corpus edits separately).

*(§5 rule 11 — this note makes no claim about its own commit state.)*
