# 260835-35 — Small items: the Purchas correction, the folio locators, Appendix D recovered, and two queued rulings

**Date:** 2026-08-29 · **Class:** external research, repair and registration · **Ledger numbers consumed: NONE**

⛔⛔ **Nothing in this pass is a finding about Rev. James.** No `DQ`, `IP`, `LS`, `RV`, `Rev`, `BLOG`, `POD`, `VP`, `GV`, `RC`, `BP`, `EXT`, `W` or `File` number was consumed, and none was re-derived (none was needed — nothing was pulled and nothing mined).

---

## 1. Gate

| Item | Value |
|---|---|
| Briefed HEAD | `44fd502` |
| Actual HEAD | `44fd502fe81e7aa35dfe1f63487fcca2d21d0b2b` — ✅ **matches exactly**; branch `main` |
| `git --no-optional-locks status --short` before first edit | ✅ **EMPTY**, captured directly, not reconstructed |
| Validator BEFORE | **`85 ok · 8 warnings · 0 errors`** — ✅ matches the briefed expectation |
| `PROJECT_STATE.md` stamp at gate | **`260835-34`** |

Every git read used `git --no-optional-locks`, per the `260835-3` FUSE-lock diagnosis.

### Every firing validator code at gate — reproduced, not summarised

1. `[C1]` `src/SRC_Discord_RPW.md`: 2 relative timestamp(s) outside message headers (`Yesterday at …`).
2. `[C3]` `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md`: no parseable `Last updated` stamp; registry says `260832-2`.
3. `[C3]` `tools/transcribe_yt.py`: no parseable `Last updated` stamp; registry says `260833-7`.
4. `[C4]` `St_Francis_EMC_Distinctives.md`: 2 passages describe an ANSWERED question as pending with no supersede marker.
5. `[C5]` `RJ_Final_Question_List.md`: 17 volatile-state assertions.
6. `[C5]` `RJ_Incense_Analysis.md`: 9 volatile-state assertions.
7. `[C5]` `St_Francis_EMC_Distinctives.md`: 7 volatile-state assertions.
8. `[C10]` §15's newest `LS` citation is 9 findings behind the ledger head (`LS-120` vs `LS-129`).

✅ **`C11` clear on all three arms.**

### Stamp derivation — hazard note read FIRST

⭐⭐ **The `260835-12`/`260835-14` hazard note was read before anything was derived, as required.** It warns that a naive content-grep misleads **in both directions**: `260835-12` reads as *available* inside prose asserting its own absence but is **REAL and CONSUMED** (the `CLAUDE.md`/Bootstrap divergence audit, commit `530d987`); `260835-14` exists **only** as committed filenames and a commit message, its internal prose still reading `260835-12`, and is likewise **REAL and CONSUMED** (commit `68bf1d8`). ✅ **Both treated as consumed; neither in play at this end of the range.**

**Derivation used.** A distinct-stamp sweep over tracked `*.md`/`*.py`/`*.txt` returns an unbroken run `260835-1 … 260835-34` with no gaps; `ls passes/` independently tops out at `260835-34`; `git log --all` tops out at `260835-34`. ⚠️ **The one apparent higher hit, `260835-99`, was opened and re-confirmed in context as NOT a stamp** — the upper endpoint of an absence-assertion range inside earlier close-out prose. ✅ **`260835-35` returns ZERO matches repo-wide, ZERO in `passes/`, ZERO in `git log --all`; `260836-` returns only quoted shell lines and absence-assertions. This pass is `260835-35`.**

---

## 2. Item 1 — the Purchas correction, applied and discharged

⭐ **JD authorised touching `RJ_Incense_Analysis.md` for this one edit only. The authorisation was read as covering `§8` and nothing else, and was applied that narrowly.**

The debt was recorded at `260835-33` §9, restated with ready-to-paste text at `260835-34` §9, and blocked there by that pass's own file prohibition — the instruction conflict `260835-34` §7 reported rather than resolving unilaterally. **It is now discharged.**

**Applied as a dated note beside the original bullet, which is retained exactly as written, per never-alter.** The note supplies:

- *Elphinstone v. Purchas* — **Sir Robert Phillimore, Dean of the Arches, 3 February 1870**;
- ⭐ **that Phillimore's decision was in other respects FAVOURABLE to the ritualists** — it upheld eucharistic vestments, **which is precisely why the prosecutor appealed for a fuller condemnation**;
- ***Hebbert v. Purchas* (Privy Council, 1871)** as the sweeping ruling — a different court, a different case name, and the decision that held eucharistic vestments, the eastward position, the mixed chalice and wafer bread illegal;
- **Purchas's non-compliance** — suspended twelve months, never made to pay costs, continuing his services **until his death in 1872**.

⭐ **One thing was added beyond the drafted text, and it is recorded so it is not mistaken for drafting drift.** A short handling consequence: cite *Elphinstone* for the incense holding and *Hebbert* for the general one, and expect an informed Anglo-Catholic interlocutor to know both facts — **and note that an unenforced judgment the defendant defied to his death SUPPORTS §8's own Phase 1 "defiance" and "legalization by attrition" readings rather than weakening them.** The same addition is recorded in the research file's §9 discharge note, so both files carry it.

⛔⛔⛔ **§4.6, §4.8 and §4.10 NOT TOUCHED.** They remain flagged falsified-pending-revision since `260835-15`; their rewrite is separately deferred and was not authorised here.

---

## 3. Items 2 and 3 — the folio locators

### The JSON was verified before it was trusted

The brief supplied `src/SRC_PRIMARY_1899_Westall_Case_For_Incense-page-numbers.json` — Internet Archive's scan-sequence-to-printed-folio map for item `bwb_C0-AUU-939` — and required a sample check against the OCR before trusting it wholesale, with the OCR governing on any disagreement.

**What the JSON asserts.** A **strictly linear** relation: `printed folio = leaf − 12`, unbroken from leaf 16 (p. 4) to leaf 185 (p. 173). 190 leaf records, 170 carrying a folio; no interior renumbering, no unmapped plates.

**Checked two independent ways, and the check was widened past a sample because it was cheap:**

1. **Folio-marker sweep of the OCR text.** Returns a monotone run **4 → 173**, no folio out of order, **18 markers OCR-dropped** — expected, and they fall on half-titles, blanks and the rotated table pages.
2. **Every one of the 190 page images.** The folio printed on each page was extracted and compared leaf by leaf. **138 leaves carry a legible bare folio marker; 135 agree with the JSON exactly.**

⚠️ **The 3 apparent disagreements are OCR digit-misreads, not mapping errors, and each is bracketed by agreeing neighbours:**

| Leaf | OCR read | Actual | Neighbours |
|---|---|---|---|
| 47 | `30` | **35** | 34 \| _35_ \| 36 |
| 95 | `838` | **83** | 82 \| _83_ \| 84 |
| 175 | `168` | **163** | 162 \| _163_ \| 164 |

✅ **ZERO substantive disagreement between the JSON and the OCR. The standing "OCR governs" rule was never engaged, and that is reported rather than left to be assumed.**

### ⛔⛔ But the JSON does not explain the wrong locators — and the `260835-34` diagnosis is now doubted

Because the JSON's mapping is a **constant −12**, it cannot generate a variable offset. **`260835-34`'s diagnosis — that `§§1–5`'s numbers are a differently-paginated rendering's sequence numbers, most probably the `rec-dcs.org` PDF's — is NOT CONFIRMED.**

⚠️⚠️ **And it is worse than "not a constant offset": the divergence is NOT MONOTONE.** Cited p. 13 stands on printed p. 24 (**+11**), while the *later* cited p. 22 stands on printed p. 31 (**+9**). **No single alternative pagination can produce that.**

⭐ **The likelier explanation, consistent with `§0`'s own account of a partial retrieval that believed the Statement ran "pp. 3–21" and the Outline "pp. 22–27"** (printed: **1–30** and **31–40**) **is that the numbers were APPROXIMATED from position within a retrieved text rather than read off folios.** ⛔ **Recorded as an unresolved diagnosis rather than resolved silently.**

⚠️ **Further evidence for approximation, worth stating: two cited pages each resolve to TWO printed folios** — cited p. 4 → printed 5 *and* 6; cited p. 12 → printed 20 *and* 21; cited p. 24 → printed 36 *and* 37.

### All fourteen located individually — none computed by offset

✅ **ZERO not found, ZERO guessed.** Each quotation was searched in the text of the page images and its printed folio read off. ⭐ **Every quotation matched, which independently confirms `260835-34`'s finding that the quotations are sound and only the locators wrong.**

| § | Quotation (short form) | Cited | **Actual** | Leaf |
|---|---|---|---|---|
| 1 | statutory force / "has statutory authority" | p. 24 | **37** | 49 |
| 2a | "is fixed as the date which in the first place determines" | p. 9 | **13** | 25 |
| 2b | "The Approach to the Altar, the Gospel, the Offertory…" | p. 12 | **20** | 32 |
| 2b | "the accustomed use of a censer includes the censing of persons…" | p. 12 | **21** | 33 |
| 2b | "…is not an additional ceremony, but is either not a ceremony at all…" | p. 24 | **36** | 48 |
| 2c | "But whether the reference to the second year means the second year…" | p. 10 | **17** | 29 |
| 2d | "…exhaustive and complete set of directions…" | p. 6 | **7** | 19 |
| 2d | "…in the Hereford Missal no mention is made of Incense except at the Gospel…" | p. 6 | **7** | 19 |
| 2d | the three prohibitory rubrics / "without all manner of print" | pp. 10–11 | **18** | 30 |
| 2d | "…the use of coloured altar cloths, and the cross, and credence table…" | p. 25 | **38** | 50 |
| 2d | "…no reference to 'a fair linen cloth'…" | p. 25 | **38** | 50 |
| 2d | "Now a Statute loses none of its validity by disuse…" | p. 24 | **37** | 49 |
| 2e | "steadily, and without flinching, has declared her intention…" | p. 4 | **5** | 17 |
| 2e | "It is not claimed that no alteration of ceremonial took place…" | p. 4 | **6** | 18 |
| 2f | "…the traditional use had, in some places, been forgotten…" | p. 13 | **24** | 36 |
| 2g | "it would be difficult to name any adjunct of worship…" | p. 22 | **31** | 43 |
| 2g | Frere's patristic concession, "The only conclusion to be drawn…" | p. 31 | **47** | 59 |

**Recorded as a dated concordance table in the file's `§0`, with a standing pointer note placed before `§1`. ⛔ No existing citation in the body was rewritten; the originals stand per never-alter and the table governs.**

### ⛔ Two page numbers deliberately NOT converted

`§2f` cites **other books**: *Acts of the Privy Council* (Dasent, N.S. iii, **p. 225**) and *English Church Furniture* (Peacock, **pp. 53, 92**). ⚠️ **A blanket find-and-replace across `§§1–5` would have corrupted both. It was not run, and the exclusion is recorded in the concordance note so a later pass does not "fix" them.**

### Item 3 — the sweep for the same defect elsewhere

- ⭐⭐ **`RJ_Incense_Analysis.md`: CONFIRMED NEGATIVE, not assumed.** The file **never cites *The Case for Incense* at all** — zero occurrences of *Case for Incense* or *Westall* anywhere in it, and zero page locators in `§8`'s ritualist material. **The defect cannot have propagated there.**
- ✅ **Other sections of the research file: clean.** Every page locator outside `§§1–5` was written at `260835-34` or later in the form *"printed p. N"* and is a printed folio.
- ⚠️⚠️ **Two slips found in `260835-34`'s OWN printed-folio citations — flagged, NOT rewritten, and expressly recorded as a DIFFERENT defect rather than more of the same.** In `§4b`: the Sandys proviso is cited at *"printed pp. 17 and 36"* and stands at **pp. 15 and 36**; the Statement's *"has never, since that date, decreed…"* sentence is cited at p. 37 and stands at **p. 36**. ✅ **`260835-34`'s third such citation — the Royal-assent reconciliation at printed p. 32 — was checked and is CORRECT.** ⭐ **Neither slip disturbs any argument; both passages are where `§4b` says they are in substance.**

---

## 4. ⛔⛔⛔ Item 4 — Appendix D's synoptic table is RECOVERED

**`260835-34` recorded it as unrecoverable from the OCR and requiring page images. JD supplied the page images. It is recovered, and it is fully legible.**

⭐ **The method, stated because it generalises to any sideways-printed matter in this scan:** the pages are printed landscape on portrait leaves; the scan's text layer transposes them into reversed gibberish. **Rendering the page images at 300 dpi and rotating them 90° clockwise before re-reading yields clean type.** ⚠️ **The limitation was in the TEXT LAYER, not in the scan** — which is exactly why the page-image artifact is worth keeping.

### ⛔⛔ Three corrections to the record, each established from the images

**(1) IT IS A THREE-COLUMN TABLE, NOT FOUR. THERE IS NO 1559 COLUMN.** The columns are **`1548 | 1549 | 1552`**, headed *"THE RUBRICS OF THE LORD'S SUPPER COMPARED — AS IN"*, with sub-headings **1548 "THE ORDER OF THE COMMUNION"** *(…"without varying any rite or ceremony"…)*, **1549 "THE SUPPER OF THE LORD… commonly called the Mass"**, **1552 "THE ORDER FOR THE ADMINISTRATION OF THE… HOLY COMMUNION."** The header is repeated on each **verso**; rectos carry the same three columns unlabelled. ⚠️ **The string `1559` does not occur anywhere in the table. Both `260835-34` and this pass's own brief describe it as "the four-column comparison of 1548/1549/1552/1559"; that description is wrong.**

**(2) THE TABLE RUNS PRINTED pp. 104–121, NOT 104–122.** ⭐ **Printed p. 122 is the FIRST page of Geldart's essay**, headed *"THE EVIDENTIAL VALUE OF THE RUBRICS IN THE LITURGIES OF EDWARD VI., AND SPECIALLY IN THE BOOK OF 1549"* — so the essay is **pp. 122–135**, not 123–135. Printed p. 103 is the appendix's title page.

**(3) ⭐⭐ THE `[Incense.]` MARKERS SIT IN THE 1548 COLUMN, AND THAT IS THE POINT OF THE EXHIBIT.** Geldart is not marking incense in the Prayer Books; he is marking it in **the Order of the Communion of 1548** — the document of the second year of Edward VI to which the Ornaments Rubric points — and setting 1549 and 1552 beside it to show what they do and do not say. **The table is a silence-exhibit whose argument is visual: the reader looks across the row and finds no prohibition.**

### All four markers, located individually

| Printed p. | 1548-column entry, verbatim |
|---|---|
| **106** | `Introit.  [Incense.]` |
| **108** | `Gospel in English.  [Incense.]` |
| **110** | `Offertory.  [Incense.]` |
| **111** | `Canon Missae.  [Incense].*` |

### ✅ The footnote question is resolved — and the answer cuts both ways

`260835-34` gap item 10 left the footnote's attachment *"very likely but NOT certain"* and instructed that it not be quoted as attached without checking the page image. **The page image was checked.**

✅ **On printed p. 111 the asterisk on `[Incense].*` is THE ONLY ASTERISK ON THE PAGE**, and the footnote rule beneath reads: ***"* This was not, however, a general use, nor is it ordered by old rubrics."*** **Attachment is CERTAIN and the note may now be quoted as attached.**

⚠️⚠️ **BUT THE CONCESSION IS WEAKER THAN IT LOOKED, AND THIS IS REPORTED BECAUSE IT CUTS AGAINST THE EARLIER READING RATHER THAN FOR IT.** The identical footnote appears again on **printed p. 112**, serving two *different* asterisked entries — `* Fraction of Host. Agnus Dei.` and `* Priest's Communion.` ⭐ **So it is Geldart's standard disclaimer for any item he supplies into the 1548 column that the old rubrics do not order — not a special admission about incense.** ⛔ **It should not be deployed as "Geldart's most damaging footnote."** ✅ **What it does still establish is not small: Geldart himself marks the Canon censing as neither general nor rubrically ordered, in the column on which the entire "second year of Edward VI" case rests.**

⭐ **One further Geldart insertion, not previously recorded** — a bracketed editorial note at printed p. 116: *"[This Blessing dismissed the Communicants from the Altar, but **not** from the Church, since the Post-Communion and dismissal followed.]"*

### ⛔ What the table is NOT — so the closure is not overstated

Its eighteen pages are otherwise **the text of the Communion service itself, set out three times in parallel** — Prayer Book rubrics and prayers, not argument. ⛔ **It is not reproduced in the corpus and should not be: nothing in it is evidence about incense except the four markers, the two footnotes and the arrangement.** ✅ **The 1548 column — Geldart's editorial spine, where every marker lives — was extracted in full and read end to end; the 1549 and 1552 columns were read for incense content and contain none.** ⚠️ **The four marker lines and both footnotes were additionally confirmed against the page image by eye, and only those are quoted verbatim.**

**Written to the research file as new `§2h-bis`**, and `§8`'s gap list updated by dated note.

---

## 5. Item 5 — the two new source files registered

Both added to `SRC_Manifest.md`'s **`External Primary Texts`** section, **hashes and byte counts computed by this pass**, plain whole-file `sha256sum` per that section's stated convention.

| Path | Bytes | sha256 |
|---|---|---|
| `src/SRC_PRIMARY_1899_Westall_Case_For_Incense-bwb_C0-AUU-939.pdf` | **8,153,783** | `68cc1f05621c9a1e2fd0ca40c09be5ce7c85a1a20af3417c66ad054f1a7d8e7b` |
| `src/SRC_PRIMARY_1899_Westall_Case_For_Incense-page-numbers.json` | **31,878** | `3589fb7873a58a4760cf66c870c0bb7912f4647c1a5e6f1463631f718ed76978` |

⛔⛔ **NO `File` OR `W` NUMBER CONSUMED BY EITHER ROW.** JD ruled `260835-34`'s reasoning correct: a third-party 1899 book is a **category difference** from a source of Rev. James's own words, and putting it in the numbered series would force every later sweep to special-case it forever.

⚠️ **Identifier corrected:** it is **`bwb_C0-AUU-939`**. The `owb_C0O-AUU-939` recorded in the existing `.txt` row is an **OCR misreading of the same string** (printed at line 118 of the text artifact). ⛔ **Left standing per never-alter; the correct identifier is named in the dated note.**

The manifest's dated note also carries the JSON verification result, the superseded "table not recoverable" verdict, and the corrected structure figures.

---

## 6. Item 6 — the coverage-register ruling, recorded

New **`SRC_Coverage_Register.md` §12**, plus changelog `v1.2`.

⭐⭐ **JD agrees with `260835-34`'s judgement, and it is now a RULING rather than the reversible flag that pass left.** **The register's subject is coverage of REV. JAMES'S OWN MATERIAL.** A third-party historical text by Frere, Birkbeck, Percival, Stone, Geldart, Lacey and St John Hope is a **category difference, not a thinly-covered source**; forcing a row would misclassify it and would make every coverage count in §§1–11 ambiguous as to what universe it counts.

⭐ **Scope: CLASS-WIDE, not one-off.** It governs every artifact in `SRC_Manifest.md`'s `External Primary Texts` section — the three now there and any added later. **Their absence from the register is CORRECT rather than a gap.**

✅ **Where their coverage IS tracked, so nothing is untracked:** registration/hashes/limits in that manifest section; what has been read and what has not in the research document's own `§8` gap list.

⚠️ **The one thing the ruling does not decide, stated so the boundary is visible:** it says nothing about *external research documents* that draw on Rev. James's own material. **The test is the SOURCE's subject, not the document that cites it.**

⛔⛔ **Nothing counted, no figure in §§1–11 touched.**

---

## 7. Gap list — net movement

| # | Before | After |
|---|---|---|
| 8 Appendix D table unrecoverable | ⏳ OPEN | ✅⭐⭐ **CLOSED — recovered in full; item's own description corrected** |
| 9 Hope's four cells derived not read | ⏳ OPEN | ⏳ **OPEN, unchanged** ⚠️ now cheaply closable from the page images |
| 10 Geldart footnote attachment | ⏳ OPEN | ✅ **CLOSED — confirmed by eye; framing corrected** |
| 11 Final appendix's letter (J or I) | ⏳ OPEN | ⏳ **OPEN, unchanged** ⚠️ now cheaply closable |
| 12 Lacey's Cotton MS | ⏳ OPEN | ⏳ **OPEN, unchanged** — external MS |
| 13 §§1–5 folio mismatch | ⏳ OPEN | ✅⭐ **CLOSED — all fourteen corrected; its diagnosis doubted** |
| **14** *(new)* | — | ⏳ 1549/1552 columns read for incense content, not proof-read line by line; nothing quoted from them |
| **15** *(new)* | — | ⏳ two `260835-34` printed-folio slips in `§4b`, flagged not rewritten |

---

## 8. What was checked and came back empty, and what was declined

- ⛔ **`Incense_Conversational_Outline.md`** — not opened, not read for any purpose, not modified.
- ⛔ **`RJ_Incense_Analysis.md` §4.6, §4.8, §4.10** — not touched; still falsified-pending-revision. **The file was opened for edit ONLY at §8, under JD's express one-edit authorisation.**
- ⛔ **No question or reply to Rev. James drafted, altered or posted.** Nothing here is deployable at him and nothing here is evidence about him.
- ⛔ **No finding minted; no ledger number of any prefix consumed; no `File` number re-derived** — none needed.
- ⛔ **The two new `src/` artifacts were READ, not modified** — they arrived committed at `44fd502`.
- ⚠️ **Gap items 9 and 11 were NOT attempted** — both are now cheaply closable from the page images, but neither is in this brief, and taking them would have been scope creep. **Recorded as available work, not as omissions.**
- ⚠️ **The `260835-21` missing-changelog gap in `SRC_Coverage_Register.md` was NOT retro-filled**, on the same reasoning `260835-26` gave: this pass did not do that work.
- ⭐ **Standing instruction (`ORCHESTRATION.md` §8) — incense mentions reported explicitly:** this pass is wholly about incense; every substantive result above is an incense result. **No icon material of any kind was encountered: a confirmed zero.**

---

## 9. ⚠️ Three places this pass contradicted what it was told, reported rather than complied with

1. **The brief describes Appendix D's table as "the four-column comparison of 1548/1549/1552/1559."** It is **three columns**, and `1559` does not appear in it.
2. **The brief gives the table as "printed pp. 104–122."** It runs **104–121**; p. 122 is the essay's first page.
3. **The brief directs the JSON be used "to convert the wrong locators systematically."** ⛔ **The JSON cannot do that** — its mapping is a constant −12 and cannot generate a variable offset. **It was instead used for what it can do: verifying the printed-folio sequence and confirming the page-image leaf numbering.** ✅ **Every locator was then found individually in the page images, which is stronger than a conversion would have been, and is why the instruction not to correct arithmetically was easy to honour.**

---

## 10. Validator and git state

| Item | Value |
|---|---|
| Validator BEFORE | `85 ok · 8 warnings · 0 errors` |
| Validator AFTER | **`85 ok · 8 warnings · 0 errors`** |
| Delta | ✅ **NONE — no regression, no new warning class; all eight codes byte-identical to baseline** |

**Files touched — five tracked, plus this artifact:**

```
 M PROJECT_STATE.md
 M RJ_Incense_Analysis.md
 M Ritualist_Case_For_Incense_and_the_1899_Opinion.md
 M SRC_Manifest.md
 M SRC_Coverage_Register.md
?? passes/260835-35_small-items-purchas-folios-appendix-d_close-out.md
```

⭐ **Staging recommendation, per the brief's two-commit split.** **Commit 1 (`passes/` first):** `passes/260835-35_small-items-purchas-folios-appendix-d_close-out.md` alone. **Commit 2 (corpus edits):** the five modified tracked files. ✅ **Unlike `260835-34`, no rename spans the two halves, so the split is clean this time and needs no special handling.**

⛔ **NOTHING WAS COMMITTED AND NOTHING WAS STAGED BY THIS PASS.**

---

*260835-35 (2026-08-29). External research, repair and registration; not a finding about Rev. James; no ledger number consumed.*

---

## 11. Validator AFTER — every firing code, reproduced

1. `[C1]` `src/SRC_Discord_RPW.md`: 2 relative timestamp(s) outside message headers.
2. `[C3]` `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md`: no parseable stamp; registry says `260832-2`.
3. `[C3]` `tools/transcribe_yt.py`: no parseable stamp; registry says `260833-7`.
4. `[C4]` `St_Francis_EMC_Distinctives.md`: 2 answered-question passages described as pending.
5. `[C5]` `RJ_Final_Question_List.md`: 17 volatile-state assertions.
6. `[C5]` `RJ_Incense_Analysis.md`: 9 volatile-state assertions.
7. `[C5]` `St_Francis_EMC_Distinctives.md`: 7 volatile-state assertions.
8. `[C10]` §15's newest `LS` citation 9 findings behind the ledger head (`LS-120` vs `LS-129`).

✅ **`85 ok · 8 warnings · 0 errors` — IDENTICAL TO BASELINE. No regression, no new warning class, and the `[C5]` count on `RJ_Incense_Analysis.md` did NOT move despite this pass editing that file.**

⚠️ **ONE TRANSIENT ERROR, REPORTED RATHER THAN QUIETLY FIXED.** An intermediate run returned **`84 ok · 8 warnings · 1 errors`** — `[C3] PROJECT_STATE.md: VERSION DRIFT — registry says '260835-34', document says '260835-35'`. **Cause: this file's own §4 registry row had not yet been bumped when its header stamp was.** ✅ **Corrected in the same pass by bumping the row; the final run is clean.** ⭐ **Recorded because it is a real ordering hazard for any pass that bumps `PROJECT_STATE.md`'s stamp: the document stamp and its own registry row must move together, and `[C3]` catches it as an ERROR, not a warning.**
