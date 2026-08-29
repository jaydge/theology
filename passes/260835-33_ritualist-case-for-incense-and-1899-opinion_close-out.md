# 260835-33 — The 19th-century ritualist case for incense, and the 1899 Lambeth ruling in context

**Pass type:** external research, layered into the corpus as a new standalone research document.
**Date:** 2026-08-29.
**Artifacts:** this close-out; `260835-33_ritualist-case-for-incense-and-1899-opinion.diff`.

⛔⛔⛔ **NOTHING IN THIS PASS IS A FINDING ABOUT REV. JAMES. No ledger number of any kind was consumed. No question or reply to him was drafted. `Incense_Conversational_Outline.md` was not touched. `RJ_Incense_Analysis.md` was not edited — including §8 and the three flagged sections.**

---

## 1. Gate

✅ **HEAD `761560b7e7a36b8bb22341f8dd352963571e7f0a`** — matches the briefed `761560b` exactly; branch `main`.

✅ **`git --no-optional-locks status --short` returned EMPTY** before this pass's first edit, captured directly and not reconstructed. Every git read in this pass used `git --no-optional-locks` per the `260835-3` FUSE-lock diagnosis; no lock created, none removed, no `rm` attempted.

✅ **Validator BEFORE: `83 ok · 8 warnings · 0 errors`** — matching the briefed expectation exactly. All eight firing codes reproduced rather than summarised:

| Code | File | Warning |
|---|---|---|
| `[C1]` | `src/SRC_Discord_RPW.md` | 2 relative timestamps outside message headers ("Yesterday at …") |
| `[C3]` | `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` | no parseable "Last updated" stamp; registry says `260832-2` |
| `[C3]` | `tools/transcribe_yt.py` | no parseable "Last updated" stamp; registry says `260833-7` |
| `[C4]` | `St_Francis_EMC_Distinctives.md` | 2 passages describe an ANSWERED question as pending, no supersede marker |
| `[C5]` | `RJ_Final_Question_List.md` | 17 volatile-state assertions |
| `[C5]` | `RJ_Incense_Analysis.md` | 9 volatile-state assertions |
| `[C5]` | `St_Francis_EMC_Distinctives.md` | 7 volatile-state assertions |
| `[C10]` | §15 | newest `LS` citation 9 findings behind the ledger head (`LS-120` vs `LS-129`) |

✅⭐ **`C11` CONFIRMED CLEAR ON ALL THREE ARMS RATHER THAN ASSUMED**, as the brief required — the validator's own three `ok` lines were read individually: `DQ-26 @ 260835-3` vs ledger `DQ-26`; `IP-108 @ 260835-3` vs ledger `IP-108`; `RV-63 @ 260830-1` vs ledger `RV-63`.

✅ **`PROJECT_STATE.md`'s own stamp at gate: `260835-30`** (header line 3, read directly; corroborated by its own §4 registry cell).

### Stamp derivation

⭐⭐ **The `260835-12`/`260835-14` hazard note was read FIRST, as the brief required.** It warns that a naive content-grep misleads **in both directions**: `260835-12` reads as *available* inside prose asserting its own absence, but is **REAL and CONSUMED** (the `CLAUDE.md`/Bootstrap divergence audit, commit `530d987`); `260835-14` exists **only** as committed filenames and a commit message, its internal prose still reading `260835-12`, and is likewise **REAL and CONSUMED** (commit `68bf1d8`). ✅ **Both treated as consumed; neither is in play at this end of the range and neither was treated as free.**

**Derivation actually used:**

- A distinct-stamp sweep over tracked `*.md`/`*.py`/`*.txt` returns an unbroken run **`260835-1 … 260835-32`** with no gaps.
- `ls passes/` independently tops out at **`260835-32`**.
- `git log --all` (subjects) independently tops out at **`260835-32`**.
- ⚠️ **The one apparent higher hit, `260835-99`, was opened and re-confirmed as NOT a stamp** — the upper endpoint of an absence-assertion range inside earlier close-out prose, verified in context rather than assumed from the prior passes' say-so.
- ✅ **`260835-33` returns ZERO matches repo-wide, ZERO in `passes/`, ZERO in `git log --all`.** `260836-` returns only quoted shell lines and absence-assertions inside earlier close-outs.

⭐ **Highest REAL stamp is `260835-32`, corroborated by three independent authoritative witnesses — the committed artifact `passes/260835-32_c11-outline-review-ip-arm_close-out.md`, the `git log --all` subject line, and `Incense_Conversational_Outline.md`'s own registry cell. This pass is `260835-33`.**

⛔⛔ **NO NUMBER OF ANY KIND CONSUMED** — no `DQ`, `IP`, `LS`, `RV`, `BLOG`, `POD`, `VP`, `GV`, `RC`, `BP`, `EXT`, `W` or `File`. **No `File` number re-derived and none needed: this pass pulled no source and mined no recording.**

---

## 2. The brief's premises, verified — two corrections

⛔ **All state figures derived by this pass, not taken from the brief.**

| Brief's claim | Verified? | Actual |
|---|---|---|
| `Ornaments Rubric` 0× in `RJ_Incense_Analysis.md` | ✅ **CONFIRMED** | 0 |
| `Ornaments Rubric` 0× in `Incense_Conversational_Outline.md` | ✅ **CONFIRMED** | 0 |
| `Ornaments Rubric` 1× in the entire findings corpus | ⚠️ **NEEDS A SCOPE** | **1× in `St_Francis_EMC_Distinctives.md`** (the findings ledger) — correct on that reading. But **also 1× in `RJ_Final_Question_List.md`**, giving **2 occurrences across 2 documents**, and **2 repo-wide across tracked `*.md` including `passes/`.** |
| `Directorium Anglicanum` appears nowhere | ✅ **CONFIRMED** | 0 repo-wide (searched as `Directorium`, case-insensitive) |
| `Purchas` 3× in `RJ_Incense_Analysis.md`, 1× in the outline | ✅ **CONFIRMED** | 3 and 1 exactly. ⚠️ The brief did not mention that `St_Francis_EMC_Distinctives.md` has **6** and `RJ_Final_Question_List.md` **2**; 14 repo-wide. Not a contradiction — the brief was scoped to two documents — but recorded so the figure is not later mistaken for a repo-wide count. |
| `Lambeth` 1× per document | ⚠️ **FALSIFIED AS STATED FOR ONE OF THE TWO** | `Incense_Conversational_Outline.md`: **1** ✅. `RJ_Incense_Analysis.md`: **2**, not 1 — line 497 (the substantive §8 treatment) **and** line 703 (a changelog entry). ⭐ **The brief's point survives intact: there is exactly one substantive treatment per document. But the literal count is 2, and the corrected figure is what this pass used.** |

⭐ **The asymmetry the brief identified is REAL and is confirmed:** the corpus's §8 holds the 1899 Opinion, Purchas, the Church of Ireland prohibition and a three-phase aftermath — **the conclusion** — with **no trace whatever of the argument it ruled against.**

---

## 3. What was produced

**New file: `Ritualist_Case_For_Incense_and_the_1899_Opinion.md`** (63,203 bytes), registered in `PROJECT_STATE.md` §4.

Structure: §0 sourcing tiers · §1 what the rubric says · §2 the ritualist case on its own strongest terms · §3 `Directorium Anglicanum` and the handbooks · §4 the legal history 1868–1890 · §5 the 1899 Opinion in context · §6 the ritualists' stated grounds for continuing · §7 the honest assessment, both directions · §8 unverified claims and gaps · §9 cross-references and one owed correction · Sources.

### 3.1 Sources actually obtained

⭐⭐ **Two primary texts read IN FULL:**

1. **The 1899 Opinion itself**, complete — *The Archbishops on the Lawfulness of the Liturgical Use of Incense and the Carrying of Lights in Procession*, Lambeth Palace, 31 July 1899 (Macmillan, 1899), via Project Canterbury.
2. **The 1906 Royal Commission on Ecclesiastical Discipline, ch. IV §§9–12**, complete — which prints the post-1899 correspondence verbatim.

⭐⭐ **One primary text read IN PART, and the limit is stated rather than papered over:**

3. ***The Case for Incense Submitted to His Grace the Archbishop of Canterbury on behalf of the Rev. H. Westall on Monday, May 8, 1899*** (Longmans, Green & Co., 1899) — **the ritualists' own submission.** ⚠️ **Retrieved text covers the title page, contents, the Statement (pp. 3–21), the Outline of Legal Arguments (pp. 22–27), and Appendix A only as far as p. 37, breaking off mid-sentence. APPENDICES B–J WERE NOT RETRIEVED**, including Frere's Appendix H (post-Reformation uses, pp. 104–113) and St John Hope's Appendix G (Edwardian inventories, pp. 99–103) — **precisely where the detailed evidentiary case lives.** This limit is stated at §0 of the new file, repeated at §2f, and enumerated at §8(1).

Plus the 1900 Lords debate (Hansard, HL Deb 16 July 1900 vol 86 cc10–36) read in full, and secondary legal commentary for the Lincoln Judgment, PWRA 1874 and *Ridsdale v. Clifton*.

### 3.2 The findings that matter most

⭐⭐⭐ **(a) THE RITUALISTS' STATED GROUNDS FOR CONTINUING, IN THEIR OWN WORDS — the single most valuable recovery of the pass.** The corpus already recorded *that* clergy continued; it did not hold *why they said they were entitled to*. The 1906 Royal Commission prints it. About twenty-five London incumbents protested to Bishop Creighton, 16 October 1899:

> "we dare not abandon altogether 'a laudable practice of the whole Catholic Church of Christ,' conspicuously scriptural and hitherto held to be sanctioned by the Ornaments Rubric of the Book of Common Prayer… Moreover, we find ourselves utterly unable to do anything by which we may be held, either explicitly or implicitly, to admit the binding authority of the Archbishops' Opinion or the force of the reasons on which that opinion is based."

⭐ **Four separable grounds** — catholic obligation (the phrase lifted from the Prayer Book's own Preface *Of Ceremonies*), scriptural warrant, the Ornaments Rubric, and forty years' episcopal acquiescence — followed by **two distinct denials**, of the Opinion's *authority* and of its *reasoning*.

⭐⭐ **And the compromise letter of 30 October 1899 gives the structure of the live position exactly:** obedience to the **person** of the bishop, coupled with express denial that the **ruling** binds — "made without any reference on our part to the Archbishops' Opinion, the binding authority of which we have felt it our duty respectfully to deny… solely in compliance with the wish of our Diocesan."

⭐⭐⭐ **(b) THE JURISDICTIONAL OBJECTION WAS PRE-REGISTERED, IN WRITING, BEFORE THE HEARING.** Westall's submission opens by reserving that "the only authority which I can recognize as competent finally to determine and settle such matters is the Synod of the Province." ⛔ **It was therefore not an excuse invented after an adverse result** — which is the obvious rejoinder and is not available.

⚠️⚠️ **(c) TWO RESULTS THAT CUT AGAINST THE CORPUS'S OWN FLANK, RECORDED BECAUSE THEY ARE TRUE, NOT BECAUSE THEY HELP.**

1. ⭐ **The ritualists' own expert conceded the patristic point.** W. H. Frere, in Appendix A of their own submission: *"The only conclusion to be drawn is then that the liturgical use of Incense is not attested during the first three centuries, except in so far as its use in funerals can be called liturgical."* He surveys Athenagoras, Tertullian, Clement, Origen, Arnobius, Lactantius and Augustine **as evidence against** liturgical use, and volunteers the negative evidence too. **This is the SAME point the Archbishops gave as their third reason for the omission.** ⛔ **Anyone who "refutes" the ritualist case by producing that fact is producing the ritualists' own finding and has not touched their argument, which is legal and needs no patristic antiquity.**
2. ⭐ **The 1899 Opinion's authority is genuinely thin, and the ritualists were right about it as a matter of law.** Temple, unprompted, in the Lords on 16 July 1900: *"I know perfectly well that the Prayer-book does not constitute the Archbishop or the two Archbishops a court with power to punish. I know all I can do is simply to declare what, in my opinion… is within the Church's law or outside it."* ⚠️ **Both sides in that debate further conceded it bound a clergyman only where his own diocesan took it up.** ⛔ **Treating the 1899 Opinion as a binding judicial determination is overclaiming and an informed Anglo-Catholic will say so at once.** Its real weight is that of the most considered interpretation ever rendered by the highest interpretative authority the Prayer Book's own machinery supplies — which is considerable, but different.

⭐ **(d) THE INVERSION ARGUMENT is, on this pass's reading, the strongest single point on either side**, and the ritualists have no good answer to it. From the Opinion: an interpretation on which ordering an ornament *per se* orders its ceremonies "inverts the relation between a ceremony and an ornament… The very meaning of an ornament is that it is a thing to be used for the fitting performance of a ceremony, and if no ceremony be prescribed the so-called ornament has no place." ⚠️ **Recorded as this pass's judgement and labelled as such, not as an established corpus finding.**

⭐ **(e) A DETAIL WORTH HAVING: the man who argued the case at Lambeth got a private accommodation.** Shortly before his death in December 1900, Bishop Creighton arranged that **St Cuthbert's, Philbeach Gardens (Westall's own church)** and St Alban's, Holborn should suspend incense on ordinary occasions but keep "their full accustomed use" on great festivals — a term never defined, and construed by some clergy to include All Souls' Day.

⭐ **(f) HARD NUMBERS, replacing a soft secondary figure.** The 1906 Commission: incense used **ceremonially in 99** and non-ceremonially in 10 of **559** churches reported on; the *Tourist's Church Guide* 1902 gave **393** for England and Wales. Of the London churches where incense was customary, **2** abandoned it, **25** adopted a compromise, **6** altered slightly or resumed during the vacancy, **8** made no change at all; **6** were placed under "discipline." ⚠️ **The widely repeated "25 London churches used incense after the Opinion" traces to the Earl of Portsmouth in the 1900 Lords debate, offered with NO baseline; the same speech uses "twenty-five" for something entirely different. The reliable figures are the Commission's. Flagged so the weaker figure is not adopted.**

### 3.3 §7 — the assessment, stated in both directions

⛔ **The brief was explicit that the case must not be stated only in its weak form. §7a gives six grounds on which the ritualist case has REAL force**, of which the two that most need saying:

- **The "silence is permissive" reductio has never been squarely answered.** Coloured altar cloths, the credence table, turning east for the Creed, "Glory be to Thee, O Lord," hymns — **all unauthorised by the letter of the Prayer Book, all universally practised, including by the strictest opponents of ritualism.** ⭐ **The 1899 Opinion CONCEDES the principle** (the Gospel responses, the General Thanksgiving said aloud and the shortened Exhortation are "probably in strictness all illegal") and then draws its line at what is "conspicuous, not sanctioned by long-continued custom… and of such a nature as to change the general character and aspect of the service." ⚠️ **That is a real distinction, but one of degree applied by judgement, not a rule derived from the text.**
- **The ornament/ceremony asymmetry is textually real.** The Preface *Of Ceremonies* is subtitled "why some be abolished, and some retained," supporting a closed list for **ceremonies**; the Ornaments Rubric contains **no comparable language** and on its face requires some ornaments without forbidding others. ⭐ **Benson's Lincoln Judgment treated candles as ornaments rather than ceremony and reached a ritualist-friendly result by doing so — and the Privy Council, given the chance to overrule him, declined and disposed of the appeal on a technicality.** The ritualist classification move is therefore not eccentric.

§7b gives six grounds on which it fails; §7c records the one point both sides agreed on (no primitive liturgical use).

---

## 4. Placement decision, and the reasoning the brief asked for

⭐⭐ **A NEW STANDALONE DOCUMENT was chosen over a section inside `RJ_Incense_Analysis.md`, on three independent grounds, any one of which would suffice.**

1. **CATEGORY — the decisive one.** `RJ_Incense_Analysis.md` is by name and content an analysis **of him**. This material is external legal-historical research about the nineteenth-century Church of England and contains **no datum about him at all**. ⛔ **Layering it there would blur exactly the distinction the brief insists on, and would make it materially easier for a future pass to mistake a nineteenth-century ritualist's argument for something he said.**
2. **THE FALSIFICATION FLAGS.** §4.6/§4.8/§4.10 have stood marked **falsified-pending-revision** since `260835-15`. Adding substantial new material to a file carrying three live falsification flags (a) risks the new work being read under the same cloud, and (b) forces the owed revision pass to navigate around unrelated new content. ⚠️ **The brief asked whether adding to that file is wise while they stand. On this pass's reading it is not — and the point holds independently of ground 1.**
3. **PRECEDENT.** `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` is the established home-shape for exactly this: external research, registered in §4, no findings originating, no numbering series advancing. ⭐ **One difference is recorded in the new registry cell rather than glossed over: unlike that file, this one WAS built and verified by Claude directly against primary sources.**

⭐ **`RJ_Incense_Analysis.md` §8 remains the natural cross-reference point.** The new file names §8 as its complement at §9. ⛔ **A pointer note AT §8 was deliberately NOT written — it is a second corpus edit, §8 is not flagged but is adjacent to sections that are, and the brief reserved deployment decisions to JD.**

---

## 5. Owed correction, recorded and NOT applied

⚠️⚠️ **`RJ_Incense_Analysis.md` §8 states: *"The Court of Arches held the ceremonial use **illegal** in **Elphinstone v. Purchas (1870)**."*** That is **accurate** as to court, holding and date, and is **not falsified**. But two adjacent facts should travel with it and currently do not:

1. ⭐ **Phillimore's 1870 Arches decision was in other respects FAVOURABLE to the ritualists** — it upheld eucharistic vestments, which is precisely why the prosecutor appealed for "a fuller condemnation." **The sweeping adverse ruling is the Privy Council's in *Hebbert v. Purchas*, 1871** — a different court and a different case name, Elphinstone having died before the appeal and Hebbert being substituted. ⛔ **Citing "the Purchas judgment (1871)" and "Elphinstone v. Purchas (1870)" as the same thing is an error waiting to be caught by anyone who knows the case.**
2. ⭐ **Purchas never complied** — suspended twelve months, could not be made to pay costs (having put his property out of his hands), and continued his services until his death in 1872. ⚠️ **This matters because §8's "Phase 1, DEFIANCE (1899-1974)" framing implicitly dates the defiance from 1899; in fact the very defendant in the leading case defied it from 1871.**

⛔⛔ **NOT APPLIED. Flagged for JD as a scoped follow-on.** The full text of *Hebbert v. Purchas* was not read; the correction rests on the ODNB-derived account and secondary legal commentary, and a pass that applies it should verify against the report.

---

## 6. Not done, deliberately

- ⛔ **No question or reply to Rev. James drafted.**
- ⛔ **`Incense_Conversational_Outline.md` NOT touched** — read only for the gate greps. Folding this into the outline is JD's separate decision.
- ⛔ **No finding minted; no ledger number consumed.**
- ⛔ **`RJ_Incense_Analysis.md` NOT edited** — including §8 and the three flagged sections §4.6/§4.8/§4.10.
- ⛔ **The earlier finding that Rev. James has not used the Ornaments Rubric argument is NOT revised.** It stands. This pass changes readiness, not the record of what he has said.

---

## 7. Validator AFTER, and git status

✅ **Validator AFTER: `85 ok · 8 warnings · 0 errors`.**

**Against baseline `83 ok · 8 warnings · 0 errors`:**

- **+2 `ok`**, both attributable and both from the new file: `[C0] Ritualist_Case_For_Incense_and_the_1899_Opinion.md: resolved at registered path` and `[C3] … version agrees with registry (260835-33)`.
- **Warnings unchanged — all eight, same codes, same files, same counts. No regression, no new warning class.** ⭐ Specifically confirmed: the new file did **not** trip `[C5]` (volatile-state assertions), and `PROJECT_STATE.md`'s own `[C3]` still agrees with its registry cell after both were bumped to `260835-33`.
- **0 errors throughout.**

### `git status --short` — every line

Captured **after** all artifacts were written, so this is the complete final state — **four lines, every one listed**:

```
 M PROJECT_STATE.md
?? Ritualist_Case_For_Incense_and_the_1899_Opinion.md
?? passes/260835-33_ritualist-case-for-incense-and-1899-opinion.diff
?? passes/260835-33_ritualist-case-for-incense-and-1899-opinion_close-out.md
```

Line by line:

| Line | File | What it is |
|---|---|---|
| ` M` | `PROJECT_STATE.md` | header stamp `260835-30`→`260835-33`; gate block, stamp-derivation block and pass note added; own §4 registry cell bumped (prior cell retained verbatim); **one new §4 registry row** for the new document |
| `??` | `Ritualist_Case_For_Incense_and_the_1899_Opinion.md` | **new** — the research document, 63,203 bytes |
| `??` | `passes/…-33_….diff` | **new** — captured diff of the `PROJECT_STATE.md` change |
| `??` | `passes/…-33_…_close-out.md` | **new** — this file |

⚠️ **`git diff --stat` reports `PROJECT_STATE.md | 21 +++++++++++++++++++--  1 file changed, 19 insertions(+), 2 deletions(-)`. It names only ONE file because the other three are untracked and invisible to `git diff`** — the diff artifact therefore covers the `PROJECT_STATE.md` change only, and the new research document is preserved by the working tree and by commit 2 below, not by the `.diff`. Stated so the artifact is not later mistaken for a complete record of the pass.

### What to stage

⛔⛔ **COMMITTED NOTHING. Per the brief, `passes/` goes first, then the corpus edits separately.**

**Commit 1 — `passes/` only:**

```
passes/260835-33_ritualist-case-for-incense-and-1899-opinion.diff
passes/260835-33_ritualist-case-for-incense-and-1899-opinion_close-out.md
```

**Commit 2 — corpus:**

```
PROJECT_STATE.md
Ritualist_Case_For_Incense_and_the_1899_Opinion.md
```

⚠️ **`Ritualist_Case_For_Incense_and_the_1899_Opinion.md` is untracked and must be `git add`-ed explicitly; it will not be picked up by `git commit -a`.**

---

## 8. Gaps, stated so nothing here is relied on beyond what was established

1. ⚠️ **Appendices B–J of *The Case for Incense* were not retrieved** — the largest gap. The 27% / 1,402-churches inventory statistic is quoted from the Statement's own summary, **not verified against St John Hope's underlying table**.
2. ⚠️ **The *Directorium Anglicanum* itself was not read.** §3 of the new file rests on secondary description and says so.
3. ⚠️ **Whether the ritualist party argued the Advertisements-of-1566 / "further order" point at Lambeth is unknown** — only that it is **absent from the portion read**, along with any mention of *Hebbert v. Purchas*. ⭐ **Recorded as an observed silence in the text read, NOT as a demonstrated omission from the case as a whole.**
4. ⚠️ **The full texts of *Hebbert v. Purchas*, *Ridsdale v. Clifton* and the Lincoln Judgment (89 pp.) were not read.** §4 rests on legal commentary cross-checked against the 1899 Opinion's own references.
5. ⚠️ **The 1899 submission carries an internal, unreconciled date discrepancy** about when the 1549 Act took parliamentary effect (21 January vs 14 March 1549). Neither the document nor this pass resolves it.
6. ⚠️ **Jurisdiction.** All of this is Church of England law and never bound American Anglicanism. The standing caution at `RJ_Incense_Analysis.md` §8 applies to the whole new file and is stated there once rather than repeated point by point.

*(§5 rule 11 — this close-out makes no claim about its own commit state.)*
