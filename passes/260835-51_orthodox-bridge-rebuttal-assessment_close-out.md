# 260835-51 — Orthodox Bridge rebuttal to Brattston assessed — CLOSE-OUT

**Date:** 2026-09-01 · **Mode:** RECONCILE · **Ledger numbers consumed:** ⛔ **NONE, of any prefix.**

---

## 1. Gate — ⛔⛔ TWO OF THE BRIEF'S THREE GATE FACTS HAD DRIFTED

| Gate item | Brief said | Actually found | Disposition |
|---|---|---|---|
| **HEAD** | `d0d63e1247b613ba85f8c21693df305a16061fdb` | **`9116faef799eecf02f6a4a2474927d5d6d4a49f3`** | ⛔ **BRIEF STALE BY ONE PASS.** `d0d63e1` is `260835-50`'s own gate hash and is now `HEAD~2`. `816e250` = `260835-50` pass artifacts; `9116fae` = `260835-50` corpus commit. **Verified by `git rev-parse HEAD~1`/`~2` and `git log`, not assumed.** |
| **Validator baseline** | `90 ok · 11 warnings · 0 errors` | **`92 ok · 11 warnings · 0 errors`** | ⛔ **BRIEF STALE.** `90` is `260835-50`'s BEFORE figure; its own close-out predicted and delivered `+2`. Reproduced directly this pass. |
| **Working tree** | (clean assumed) | **EMPTY** `git --no-optional-locks status --short` before first edit | ✅ Confirmed |
| **`PROJECT_STATE.md` own stamp at gate** | — | `260835-50`, agreeing with its §4 registry cell | ✅ No drift |

⭐⭐ **STAMP DERIVED FRESH BY GREP, AND THE `260835-12`/`260835-14` HAZARD NOTE WAS READ FIRST, AS THE BRIEF REQUIRED.** Both re-confirmed **REAL and CONSUMED** (commits `530d987`, `68bf1d8`); neither in play at this end of the range. The note warns a naive content-grep misleads in both directions — `260835-12` reads as available inside prose asserting its absence but is consumed; `260835-14` exists only as committed filenames and a commit message, its own internal prose still reading `260835-12`, and is likewise consumed.

**Derivation actually used.** A distinct-stamp sweep (`git ls-files '*.md' '*.py' '*.txt' | xargs grep -rhoE '\b26[0-9]{4}-[0-9]+\b'`), **numerically sorted**, returns an unbroken run **`260835-1 … 260835-50`**, no gaps. ⚠️ **`260835-99` re-checked in context and re-confirmed NOT a stamp** — the upper endpoint of an absence-assertion range in earlier close-out prose (read at `passes/260835-42_…_close-out.md` L45 and `passes/260835-31_…_close-out.md` L46). `260836-<digit>` returns **ZERO** real stamps. ✅ **`260835-51` returned ZERO matches repo-wide, ZERO in `passes/`, ZERO in `git log --all`; `260835-52` and `260835-53` likewise ZERO.** ⭐ **AND SOMETHING WORTH RECORDING BECAUSE IT DIFFERS FROM `260835-45`/`46`/`47`: `260835-51` produced no predecessor forward-absence-assertion hits at all — the hazard shape did not arise this time. That is reported rather than assumed.** ⛔ **`ls passes/` was read under numeric sort, not lexical, for the reason `260835-45` recorded.** **This pass is `260835-51`.**

⚠️⚠️ **THE `260835-3` FUSE `.git/index.lock` HAZARD RECURRED AND IS FLAGGED FOR JD, NOT REPAIRED.** A `git reset` run while generating the diff artifact emitted `warning: unable to unlink '…/.git/index.lock': Operation not permitted`. ⛔⛔ **NO `rm` WAS ATTEMPTED AND NO LOCK WAS REMOVED.** Git operations before and after the warning completed correctly and `git status --short` reports the expected tree (two modified, two untracked). ⛔ **Flagged for JD exactly as `260835-44` flagged the same class.**

---

## 2. What the pass was asked to do, and what it did

**Task.** Read the Orthodox Bridge rebuttal to Brattston in full; enumerate every distinct counter-argument; check each against `Patristic_Citations_Incense_Verification.md` (`260835-47`), `Tertullian_Incense_Passages.md` (`260835-48`), `Brattston_Article_Assessment.md` (`260835-49`) and `Ritualist_Case…` §2g/§7d; verdict each as addressed / new / needs-checking; run two named checks (the Tertullian counter-evidence; Frere's prudential explanation); flag every citation outside the verified set; produce a new file and a ranked closing section.

**Source.** Robert Arakaki, "Defending Incense: A Response to David W.T. Brattston's 'Incense in Ante-Nicene Christianity'," *Orthodox-Reformed Bridge*, 25 January 2013. <https://orthodoxbridge.com/2013/01/25/defending-incense/>. **Article body read in full** (the printed piece runs from the title through "Why Incense Matters" and the author signature). ⛔ **The 20-comment thread below it was NOT assessed**; one comment is quoted once in the new file, at §5.3, solely to record where the argument tends in live conversation, and is expressly **not** attributed to the article's author.

**Deliverable.** `Orthodox_Bridge_Rebuttal_Assessment.md` — **83,135 bytes, 547 lines, `sha256` = `6c1e4fb9be6c3b1a59c1ff26168e586c4af32a5081a4f046d0431dd1eb271c71`**.

---

## 3. ⭐⭐⭐ Headline results

### 3.1 The count

**FIFTEEN distinct counter-arguments identified, in the order the article presents them.**

- ✅ **Already addressed by repo material — 9** (CA-2 context filter · CA-3 Barnabas/hypocrisy · CA-5 argument-from-silence · CA-7 *Apostolic Canons* 3 · CA-10 the Gnostic exception · CA-11 prevalence/Vincentian · CA-13 the central conclusion · CA-14 the retraction call · CA-15 "Why Incense Matters")
- ⭐ **Genuinely new, not previously considered — 4** (CA-1 source-weighting · CA-4 Eusebius *DE* 1.10 · CA-9 the "Malachi 1:33" typo · CA-12's *lex orandi* framing)
- ⛔ **Rests on a citation or claim needing checking — 4** (CA-4 Eusebius · CA-6 the three ancient liturgies · CA-8's Irenaeus limb · CA-7's canon text)

*(Categories overlap by design: CA-4 is both new and unchecked; CA-8 is mostly addressed with one unchecked limb.)*

### 3.2 ⭐⭐⭐ The finding that governs everything else

**ARAKAKI'S CENTRAL MOVE IS `260835-47` §3, REACHED INDEPENDENTLY BY THIS PROJECT FIRST AND STATED MORE SHARPLY THERE.** His whole case is that the ante-Nicene condemnations target *pagan* (and hypocritical *Jewish*) incense and never Christian ceremonial use. `260835-47` §3 states the same result as a **contrast-class** finding, verified passage by passage: every theological argument among the eight targets incense as a **sacrificial oblation**, the contrast class always a victim on an altar, and **not one addresses incense in Christian assembly**.

⭐⭐⭐ **AND HIS CONCLUSION IS CONCEDED IN ADVANCE.** *"Brattston presented not a single shred of evidence of an early church father objecting to the use of incense in Christian worship"* is `260835-47` §5's own sentence in substance: *"They do not support the proposition that the Fathers spoke against incense in Christian worship, because none of them addresses it."* ⭐⭐ **The strategic consequence, recorded in the new file at §3.13 and §7.4: JD can grant the article's headline sentence flatly and first, at no cost, because what he holds is the narrower proposition the sentence does not touch — and anything less than a clean concession reads as evasion.**

### 3.3 ⛔⛔ Brief item 5 — the Tertullian counter-evidence: THE ANSWER IS THE OPPOSITE OF WHAT WAS ANTICIPATED

The brief anticipated the article would deploy the domestic-frankincense and funerary-purchase passages **as evidence FOR its position**, requiring a flag because `260835-47`/`48` already determined they do not establish liturgical use. ⛔⛔ **It does neither.**

- ⛔⛔ ***De Corona* 10 — ABSENT ENTIRELY.** The article never cites *De Corona* at all, at any chapter. The single passage `260835-47` #1 calls *"the pass's sharpest warning"* and a *"gift"* to the opponent — Tertullian saying in the first person *"if the smell of some place or other offends me, I burn the Arabian product myself"* — **is missing from the one article that would have profited most from it.** ***De Idololatria* 11**, which `260835-48` §5c calls the single most systematic Tertullian statement on the question, is likewise absent.
- ⛔⛔⛔ ***Apology* 42 — PRESENT AND MISREAD AGAINST ITS OWN INTEREST.** The article's entire treatment is: *"Brattston's first citation is Tertullian's* Apology *42 in which he **criticizes the burial custom** of using frankincense to cover up the smell of the dead body."* ⛔ **That inverts the chapter.** The double-attested text (`260835-48` §5) has Tertullian reassuring the incense trade that Sabaean merchandise *"is expended as largely in the burying of Christians as in the fumigating of the gods."* **He is not criticising the custom; he is citing it, almost with pride, as proof Christians are not economically useless.** ⭐⭐ **A pro-incense advocate turns his own best available evidence into a condemnation.**
- ⭐⭐⭐ **AND THE COMPARISON IS THE POINT: BRATTSTON HANDLES BOTH PASSAGES MORE ACCURATELY THAN THIS PRO-INCENSE REBUTTAL DOES.** `260835-49` Task 1 graded Brattston's footnote 11 (*De Corona* 10's secular-use concession) **honest** and *"an accurate summary of what chapter 10 actually says,"* and his footnote 12 (*De Idololatria* 11's medicinal/funerary carve-out) *"better than adequate."* ⚠️ Brattston's own defect on *Apology* 42 — the *"instead of"* paraphrase — **obscures** the point; **Arakaki reverses its valence.**
- ⛔⛔ **THE GUARD RUNS IN BOTH DIRECTIONS AND IS RESTATED IN THE NEW FILE AT §5.3.** `260835-48` §5: funerary use is distinguished from *cultic* use, and Christian **liturgical** incense is *"a third category this passage never raises at all."* ⛔ **JD must not present these as evidence FOR liturgical incense either — that would be the mirror image of the error he is noting.**

### 3.4 ⛔⛔ Brief item 6 — Frere's prudential explanation: NOT INVOKED, AND THE REGISTER FINDING DOES NOT ENGAGE THIS ARTICLE

⛔⛔⛔ **THE ARTICLE INVOKES NO IMPERIAL-CULT EXPLANATION AND NO PRUDENTIAL ARGUMENT OF ANY KIND, ANYWHERE.**

⭐⭐⭐ **AND THE REASON IS STRUCTURAL, NOT ACCIDENTAL — THIS IS THE PASS'S MOST CONSEQUENTIAL STRUCTURAL FINDING.** The prudential escape presupposes there *was* an ante-Nicene abstention to explain away. **Arakaki's case is that there was none** — the Fathers were only ever condemning pagan incense — and he then argues affirmatively that the ante-Nicene Church *did* use it. **A man arguing they used it has no use for a theory of why they didn't.**

⛔⛔ **CONSEQUENCE, STATED PLAINLY: THE `260835-47` REGISTER RESULT (6 THEOLOGICAL · 1 PRUDENTIAL · 1 DESCRIPTIVE) DOES NOT ENGAGE THIS ARTICLE, AND DEPLOYING IT AGAINST IT WOULD BE A CATEGORY ERROR.** `260835-47` §2 names its own target exactly — *"that ante-Nicene abstention was **purely circumstantial**"* — which is **Frere's** escape, not Arakaki's. Showing the six gave theological rather than prudential reasons establishes their refusal was **principled**; it does nothing to establish it was **directed at Christian ceremonial rather than pagan sacrifice**, which is the only thing Arakaki disputes.

⚠️ **WHAT DOES ENGAGE HIM IS `260835-47` §2's OWN SELF-RECORDED QUALIFICATION**, written before this article was read: *"the apologetic setting is prudential; the reason given inside it is not… but it does mean **none of the six is a liturgical directive, and none was written to a church about its own worship.**"* ⭐⭐ **That last clause is Arakaki's thesis, conceded by this project in advance.** The only reply available is the middle sentence — that a polemical *occasion* does not confine a stated *reason* — and the new file records it as narrow.

⭐⭐ **THE REGISTER FINDING STILL HAS A TARGET, AND IT IS FRERE.** `Ritualist_Case` §2g / §7d(2)(f): Frere concedes the first three centuries outright, reads the Fathers as *"disproving (so far as they go) the liturgical use of Incense,"* declines the argument-from-silence escape, adds the rarely-quoted second limb (Levitical precedent *"would have told against the use of incense rather than for it"*), puts liturgical-book evidence at c. 700–800, calls altar-censing *"one of the later forms,"* and closes by declaring the patristic question legally irrelevant. ⭐ **Against that, the register finding is a real answer — sharpest at `260835-47` #8, where Lactantius states a theological objection as the persecution ends, the moment a prudential theory predicts it should relax.** ⛔ **But `Ritualist_Case` §2g's warning governs the deployment and is restated in the new file: refuting the ritualist case by showing the primitive Church did not use incense refutes a claim their own expert made first.**

### 3.5 ⛔ Brief item 7 — citations outside the verified set

**Sixteen citation classes tabled as ⛔ UNVERIFIED at the new file's §4, none opened this pass, none vouched for in either direction.** The material ones:

| Citation | Note |
|---|---|
| **Eusebius, *Demonstratio Evangelica* 1.10** — *"So, then, we sacrifice and offer incense"* | ⛔⛔ **The article's load-bearing positive citation, and ⏳ THE HIGHEST-VALUE OUTSTANDING ITEM.** Eusebius appears nowhere in `260835-47`/`48`/`49`. ⚠️ Three provisional observations recorded and **none is a verdict**: (i) the article's own excerpt glosses the word metaphorically two sentences earlier (*"offering it in our prayers to Him"*), and its own *DE* 1.6 quotation has Eusebius reading Malachi's incense clause as *"the incense of prayer"* explicitly; (ii) Eusebius is fourth-century and post-Constantinian — the `260835-47` #8 dating problem, **cutting both ways**; (iii) Frere, surveying the same verse for the pro-incense side, reported the patristic result as prayer-or-silence and did not produce this passage |
| **Eusebius, *DE* 1.6, 3.3, 3.6 ×2** | ⛔ UNVERIFIED |
| **Liturgies of St James ("first century"), St Mark, Addai & Mari** | ⛔⛔ UNVERIFIED, **text and date**. ⭐ The *"ante-Nicene witness"* framing is already answerable from `Ritualist_Case` §7d(2)(f) — Frere's liturgical-book-evidence-from-c.-700 concession. ⚠️ ANF vol. 7's placement is an 1886 editorial decision, not a dating finding; the article treats the volume title as evidence |
| ***Apostolic Canons*, Canon 3** | ⛔ UNVERIFIED **as text**; ✅ its **dating dispute IS covered** at `260835-49` Task 2 — and ⛔ **Arakaki does not mention the dispute at all**, offering Trullo (692) as though it argued for earliness |
| **Irenaeus, *Against Heresies* 4.17** | ⛔ UNVERIFIED — ⚠️ **and the article's gloss exceeds its own block quotation**: the continuing item Irenaeus names is *sacrifice* and the *pure offering*, not incense |
| **Arnobius 7.26** | ⚠️ **PARTLY** — `260835-49` Task 4 confirmed **a different sentence** in the same chapter verbatim; Arakaki's sentence is unverified. ⚠️ **Citation slip:** the article calls the work *"Ad Nationes"* (Tertullian's title) in one place and *"Against the Heathen"* in the attribution |
| **Hippolytus (*Canticles*, *Apostolic Tradition*), Origen *Hom. Lev.*, *Second Book of Jeu*** | ⛔ UNVERIFIED; the *Apostolic Tradition* was also left unchecked by `260835-49` |
| ***NIDCC* on Arnobius; *Catholic Encyclopedia* on Lactantius** | ⛔ UNVERIFIED secondary characterisations — **load-bearing**, since they are the basis on which two witnesses are discounted (CA-1) |

⚠️ **Two minor factual slips recorded and marked DO-NOT-DEPLOY** (Justin's *1 Apology* said to address *"the Roman emperor Titus"* — defensible via Antoninus Pius's full style; Tertullian called *"second century"* when *De Corona* is c. 211). ⛔ **Neither is deployable, and both are exactly what `CLAUDE.md`'s tone rule and `BLOG-53`'s record-only guard exist to keep out of a conversation.**

### 3.6 ⭐⭐⭐ The observation that outranks the ranking (new file §7.2)

**THE ARTICLE ARGUES FOR A STRONGER POSITION THAN `DQ-28` RECORDS REV. JAMES HOLDING.** Its conclusion is not that incense is *permitted* but that it is *"a marker of right worship"* whose loss left Protestants having *"lost their way."* `DQ-28`(c)/(d) records him, asked directly, affirming that levels (1)–(3) **allow and do not demand** incense, and answering *"Correct."* to the proposition that a parish never using incense would not be failing at (1)–(3).

⛔⛔⛔ **NOTHING IS INFERRED FROM THAT ABOUT REV. JAMES AND NOTHING IS ASSERTED.** The new file records the gap as the shape of a **question**, not a charge, per `CLAUDE.md`'s *"keep both readings live and ask which he means."* ⛔ **`DQ-28`(e)'s `IP-118` non-adjudication is expressly left undisturbed**, and `DQ-28`(d)'s wording guard (the *"Correct."* must never be quoted detached from the 4:01 PM question) is restated.

---

## 4. Files touched

| File | Before | After | What changed |
|---|---|---|---|
| `Orthodox_Bridge_Rebuttal_Assessment.md` | *(did not exist)* | **260835-51** | ⭐ **NEW.** 83,135 B, 547 lines, `sha256 6c1e4fb9…b271c71` |
| `SRC_Manifest.md` | 260835-50 | **260835-51** | Stamp + one **dated note** in §External Primary Texts registering the new file, **UNNUMBERED** per the `260835-35` class-wide ruling — the section's **seventh** external-research document. ⛔ **No existing row, hash, byte count, path, provenance or registration cell touched** |
| `PROJECT_STATE.md` | 260835-50 | **260835-51** | Stamp + gate note + pass note; **ONE NEW §4 ROW** for the new file; this row and `SRC_Manifest.md`'s row bumped. ⛔ **No next-free number moved; no §1/§2/§3/§5/§7 state altered** |

⚠️ **NAMED DEPARTURE FROM THE BRIEF, REPORTED RATHER THAN TAKEN SILENTLY — the same one `260835-44`/`47`/`49`/`50` each had to make.** The brief's deliverable list named only the new file and the `SRC_Manifest.md` registration. That registration raises validator `[C3] VERSION DRIFT` as a hard **ERROR** unless the registry cell moves with the stamp, and `CLAUDE.md` close-out rule 3 binds the two together. **The minimum `PROJECT_STATE.md` edit was made and nothing else in that file was altered.**

**Pass artifacts** (not in the diff, by convention): `passes/260835-51_orthodox-bridge-rebuttal-assessment.diff` (632 lines) and this close-out.

---

## 5. Validator

**BEFORE:** `92 ok · 11 warnings · 0 errors` — reproduced directly at gate, ⛔ **not the `90` the brief asserted.**
**AFTER:** ✅ **`94 ok · 11 warnings · 0 errors`.**

⭐ **Exactly the `+2` the brief predicted, and the warning set is unchanged — but the brief named the wrong two checks, and that is corrected rather than glossed.** The `+2` falls on **`[C0]`** (*"Orthodox_Bridge_Rebuttal_Assessment.md: resolved at registered path"*) and **`[C3]`** (*"version agrees with registry (260835-51)"*). ⛔ **`[C8]`'s ok count is structural — two rows, `QA-*` citations and `VP-` labels — and does not move with file count.** The new file also appears as a coverage sub-entry under `[C6]`, `[C7]`, `[C8]` and `[C13]`-class list checks, which add sub-lines without adding ok rows.

**Warning set, verified identical to baseline** (11): `[C1]` RPW relative timestamps ×4 · `[C3]` no parseable stamp ×2 (`Calvin_Luther…`, `tools/transcribe_yt.py`) · `[C4]` answered-as-pending ×2 · `[C5]` volatile-state assertions ×3 (`RJ_Final_Question_List` 17, `RJ_Incense_Analysis` 9, `St_Francis_EMC_Distinctives` 7) · `[C10]` ×2 (`IP-108` vs `IP-125`; `LS-120` vs `LS-141`) · `[C11]` ×2 (`DQ-26` vs `DQ-28`; `IP-108` vs `IP-125`). ⛔ **No warning introduced, none cleared.**

---

## 6. ⛔⛔⛔ What this pass deliberately did NOT do

- ⛔⛔ **PRODUCED NOTHING FOR PUBLIC CIRCULATION.** The new file is **JD's own preparation material** and says so in its own scope block, its `SRC_Manifest.md` registration and its `PROJECT_STATE.md` §4 row.
- ⛔⛔ **The Discord draft, `RJ_Incense_Analysis.md` and `Incense_Conversational_Outline.md` NOT TOUCHED.**
- ⛔ **`St_Francis_EMC_Distinctives.md`, `RJ_Final_Question_List.md`, `RJ_Open_Questions_and_Divergences.md`, `Patristic_Citations_Incense_Verification.md`, `Tertullian_Incense_Passages.md`, `Brattston_Article_Assessment.md`, `Ritualist_Case_For_Incense_and_the_1899_Opinion.md`, `Protestant_Commentary_Survey_Malachi_1_11.md`, `Frere_Appendix_A_Translated.md`, `On_Incense_and_the_Altar.md` — ALL UNTOUCHED.**
- ⛔ **`SRC_Coverage_Register.md` NOT touched** (§12 ruling).
- ⛔⛔ **NO PRIMARY TEXT OPENED.** Not one. Every verdict turning on a primary text turns on one already verified at `260835-47`/`48`/`49`. ⏳ **Owed if any of this becomes live: Eusebius *DE* 1.10 (highest value), the three ancient liturgies in ANF 7 with a stratum-vs-redaction dating position, *Apostolic Canons* 3's text, Irenaeus *AH* 4.17.**
- ⛔ **The article NOT captured to `src/`** — read live over the web; nothing hash-verifiable; the same divergence `260835-44`/`47`/`48`/`50` each recorded, and the standing capture flag now covers this file too.
- ⛔⛔ **NOTHING IS A FINDING ABOUT REV. JAMES.** `IP-111`, `IP-98`, `IP-118`, `DQ-27`, `DQ-28`, `BLOG-53`, `BLOG-121` and `LS-25` are **pointed at**, never restated as new attributions, never extended, never adjudicated. **`DQ-27`(b)'s recorded ambiguity NOT resolved. `DQ-27`(f)/`DQ-28`(f)'s axis-question coverage fact NOT discharged. `DQ-28`(e)'s `IP-118` non-adjudication NOT disturbed. `IP-98`'s cross-reference at `DQ-27`(a) NOT adjudicated. `BLOG-121`'s inline both-readings guard NOT resolved and expressly restated.**
- ⛔⛔⛔ **`BLOG-53` IS NAMED WITH ITS RECORD-ONLY GUARD RESTATED AND IS NOT A LEVER.** It is used only for JD's own calibration (Rev. James's own St James dating is *three centuries later* than Arakaki's, so the weaker form is the likelier one) and the new file states twice that it must never be produced at him.
- ⛔ **Nothing drafted, altered or posted to Rev. James. No gate moved. `OQ20`/`OQ21` not moved. `DQ-9` not moved.**
- ⛔⛔⛔ **NOTHING MINTED AND NO LEDGER NUMBER OF ANY PREFIX CONSUMED** — no `IP`, `LS`, `DQ`, `RV`, `Rev`, `BLOG`, `POD`, `VP`, `GV`, `RC`, `BP`, `EXT`, `W`, `File` or `DELTA`. **Next free values re-derived and UNCHANGED: `IP-126`, `LS-142`, `File 86`, `DQ-29`.**
- ⛔ **NOT COMMITTED.** `passes/` artifacts written; JD applies, validates, commits and pushes from his own terminal. *(§5 rule 11 — this note makes no claim about its own commit state.)*

---

## 7. ⏳ Owed, flagged, not done

1. ⏳⏳ **Read Eusebius, *Demonstratio Evangelica* Book 1 ch. 10 in full at Tier 1** and determine whether *"So, then, we sacrifice and offer incense"* is literal or is the prayer-metaphor continued. **The single highest-value unfinished item.** The article's own linked host is `tertullian.org/fathers/eusebius_de_03_book1.htm` (Ferrar).
2. ⏳ **Read the Liturgies of St James, St Mark and Addai & Mari in ANF 7** for the incense material, and establish a dating position for each, **separately for earliest stratum and surviving redaction.**
3. ⏳ **Verify *Apostolic Canons* Canon 3's text** (its dating dispute is already covered) and **Irenaeus *AH* 4.17.**
4. ⏳ **Standing, unchanged, now covering a seventh file:** capture external-research sources to `src/` as real rows before any outward verbatim deployment, per `CLAUDE.md`.
5. ⚠️ **`.git/index.lock` FUSE hazard recurred — flagged for JD, no `rm` attempted, no lock removed.**
6. ⚠️ **Brief-hygiene note for the next brief-writer:** two of three gate facts in this brief were one pass stale, in both cases because they were copied from the *previous* pass's gate rather than from its close-out. Recorded as an observation about brief construction, not as a defect in any document.
