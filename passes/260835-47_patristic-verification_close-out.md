# 260835-47 — Patristic citations on incense, verified against primary texts

**Pass type:** verification-only, external research. ⛔ **Nothing minted. No ledger number of any prefix consumed. Not committed.**

---

## 1. Gate

✅ **HEAD `c33bd5b399b053213237ffa5643dfedfb2c9fec2`** — matches the briefed HEAD **exactly**; branch `main`; commit *"260835-46: DQ-28 minted…"*.

✅ **`git --no-optional-locks status --short` returned EMPTY before this pass's first edit**, captured directly and not reconstructed. Every git read used `git --no-optional-locks` per the `260835-3` FUSE-lock diagnosis. ⛔ **No lock observed, none created, no `rm` performed against one.**

✅ **Validator BEFORE: `84 ok · 11 warnings · 0 errors`** — matching the briefed baseline on totals.

✅ **Web access confirmed working before any verification began**, as the gate required — a live fetch was performed and returned content, rather than the capability being assumed.

⛔ **No ledger number of any prefix consumed.** Next free re-derived and **UNCHANGED**: `IP-126`, `LS-142`, `File 86`, `DQ-29`.

### 1a. Stamp derivation

**The `260835-12`/`260835-14` hazard note was read first**, as the brief required — the `260835-15` account that the pass note internally labelled `260835-12` describes work whose committed artifacts are `260835-14`, so a content-grep alone under-counts. Both re-confirmed **REAL and CONSUMED**; neither in play at this end of the range.

**Derivation actually used.** `260835-47` returns **exactly THREE repo-wide hits, and all three were opened and read in context** — every one is `260835-46`'s own forward absence-assertion (*"`260835-47` and above return ZERO"*), in `PROJECT_STATE.md` L7, `passes/260835-46_dq28-discord-mint.diff` L13 and `passes/260835-46_dq28-discord-mint_close-out.md` L34. ⭐ **Exactly the shape the hazard note warns about: a predecessor's absence-assertion is a content hit, not a consumption.**

⚠️ **`260835-99` re-checked in context and re-confirmed NOT a stamp** — the upper endpoint of an absence-assertion range in earlier close-out prose.

✅ **`260835-48` and above return ZERO.** A numeric-sorted distinct-stamp sweep returns an unbroken run **`260835-1 … 260835-46`**; `git log --all` tops out at the `260835-46` commit `c33bd5b`. ⛔ `ls passes/` again tops out misleadingly under lexical sort and was not relied on. **`260835-47` is FREE and was taken.**

---

## 2. ⚠️⚠️ Two stale figures in the inherited baseline — corrected, not copied forward

Per `ORCHESTRATION.md` §7. **Neither is this pass's doing and neither is repaired here.**

**(i) `[C1]` reads FOUR relative timestamps at `HEAD`, not the TWO the brief and `260835-46`'s own gate record.**

⭐ **Verified properly rather than asserted: `HEAD` `c33bd5b` was cloned to a clean tree and the validator run there**, before the working-tree figure was trusted. The clean-`HEAD` run returns `84 ok · 11 warnings · 0 errors` with `[C1]` at **four**.

**Mechanism.** `260835-46`'s gate read two *before its own edits*; that pass then appended messages 42-46 to `src/SRC_Discord_RPW.md`, and the append carried two further `Yesterday at …` timestamps. Its AFTER figure of `84 ok · 11 warnings · 0 errors` was **correct on totals**, and the detail line moved underneath it unnoticed.

⛔ **The warning SET is unchanged and the warning COUNT is unchanged. Only this one code's instance count moved, and it moved at `260835-46`.** `src/SRC_Discord_RPW.md` is **NOT touched** by this pass; the figure is corrected **in the record only**.

⭐ **The general lesson is worth more than the instance, and this project has been bitten by its shape before: an unchanged TOTAL is not evidence that the underlying detail is unchanged.**

**(ii) The brief's `[C11]` expectation is stated against a `DQ` ledger running to `DQ-27`.** It runs to **`DQ-28`**, `260835-46` having minted it. Warning count unaffected.

---

## 3. What was done

**One new standalone file: `Patristic_Citations_Incense_Verification.md`** — 32,361 bytes, 309 lines, `sha256 41b0265ed8888d7bca80d001f800f633b0756aed7e9733ca568fa0a6c0e13d29`. External research on the `Protestant_Commentary_Survey_Malachi_1_11.md` (`260835-44`) model. Registered in `PROJECT_STATE.md` §4 and in `SRC_Manifest.md`'s unnumbered **External Primary Texts** section, per the `260835-35` class-wide ruling — its **third** application.

⛔ **NOT a finding about Rev. James. Does NOT enter `SRC_Coverage_Register.md`** (§12 ruling). ⛔ **The Brattston article itself was NOT evaluated** — only the primary texts its citations point at, per brief.

### 3a. Verdicts — all eight

| # | Citation | Verdict | Register |
|---|---|---|---|
| 1 | Tertullian, *De Corona* 10 | **(C) WRONG CHAPTER** — incense line is ch. 11; ⛔ ch. 10 holds counter-evidence | PRUDENTIAL |
| 2 | Tertullian, *Apology* 30 | **(B) confirmed, misframed** — object is wrong, and correcting it strengthens it | THEOLOGICAL |
| 3 | Tertullian, *Apology* 42 | **(A) confirmed as claimed** — ⛔ and it cuts against its own deployment | DESCRIPTIVE |
| 4 | Justin, *1 Apology* 13 | **(A) confirmed as claimed** | THEOLOGICAL |
| 5 | Justin, *2 Apology* 5 | **(A) confirmed** — one wording precision, one scope caveat | THEOLOGICAL |
| 6 | Barnabas 2.5 | **(B) overstated** — quoted list; abolition clause is 2.6 with a broader object | THEOLOGICAL |
| 7 | Athenagoras, *Plea* 13 | **(A) confirmed as claimed** — ⭐ strongest of the eight | THEOLOGICAL |
| 8 | Lactantius, *Div. Inst.* 6.25 | **(B) overstated** — ⛔ not a quotation | THEOLOGICAL |

**(A) 4 · (B) 3 · (C) 1 · (D) 0 · (E) 0.** **Register: THEOLOGICAL 6 · PRUDENTIAL 1 · DESCRIPTIVE 1.**

---

## 4. The three results that matter

### ⭐⭐⭐ (1) Nothing is fabricated

Every Father named really wrote about incense, in the work named, in the sense broadly claimed. **Zero misattributions, zero unverifiable.** That is a materially better result than the commentary survey's modern control group produced at `260835-44`, and it is worth stating before the qualifications start.

### ⭐⭐⭐ (2) The register question is answered, and in JD's favour

The brief raised this against a specific anticipated counter-argument: that ante-Nicene abstention was purely circumstantial, the imperial cult having made incense look like emperor-worship. **That reading is not supported by these eight texts, and the margin is wide.** Six of eight give an explicitly theological reason, stated as a cause, in the author's own voice — divine non-need (Justin, Athenagoras, Lactantius), supersession by the new law (Barnabas), God's own requirement (Tertullian *Apol.* 30), demonic origin (Justin *2 Apol.* 5).

⛔ **Exactly one is prudential — `De Corona` 11 — and it is the one the source table cites at the wrong chapter.**

⚠️ **One honest qualification carried rather than dropped:** Athenagoras's and Tertullian's chapters are framed as rebuttals to hostile emperors, so the **setting** is apologetic even though the **reasons given inside it** are not prudential. None of the six is a liturgical directive, and none was written to a church about its own worship.

### ⛔⛔⛔ (3) The finding the brief did not anticipate — and it governs deployment

**Winning the register argument does not win the argument.**

**Every theological argument among the eight is directed at incense as a SACRIFICIAL OBLATION offered *to* God, made while refusing pagan or Jewish sacrificial cult. The contrast class is a victim on an altar in every case — blood, libations, burnt-offerings, hecatombs, the fat of lambs, the blood of a worthless ox. NOT ONE of the eight addresses incense used ceremonially or honorifically in a Christian assembly, which is the practice actually at issue.**

⛔ **On the ceremonial question these eight are SILENT, and `Protestant_Commentary_Survey_Malachi_1_11.md` §1's own B-explicit / B-silent rule applies unmodified: counting their silence about censers as a denial of censers is the identical error to reading Rev. James's silence as agreement.** No ritualist defender of the thurible asserts that incense is a propitiatory sacrifice or that God is fed by it — so if that is what the Fathers deny, the denial does not reach the practice.

⛔⛔ **And two of the eight carry positive counter-evidence, which is worse than silence. Both are Tertullian.**

- ***De Corona* 10 — the very chapter the table cites — has Tertullian burning frankincense himself** to clear a bad smell, holding the substance an innocent creature of God and the *ceremony* the thing that defiles.
- ***Apology* 42 asserts that Christians consume Arabian and Sabaean incense as largely in burying their dead as pagans do in fumigating their gods.** Christians were buying incense in quantity.

⭐ **ANF's own editor Coxe reads *De Corona* 10 as showing Tertullian *"seems to know no use for incense except for burials and for fumigation"*** — recorded as a nineteenth-century Anglican editor's opinion, not as primary text. It cuts JD's way on **liturgical** use while conceding **domestic** use.

**So the strongest defensible form of the claim is narrower than the source table's:** these texts establish that the early Fathers rejected incense **as a sacrificial offering**, on theological grounds. They do **not** establish that the Fathers spoke against incense as such.

---

## 5. Deployment guidance recorded in the file

**Safe as cited — three:** Athenagoras *Plea* 13 (lead with it), Justin *1 Apol.* 13, Tertullian *Apol.* 42 (⛔ only with the burial sentence attached).

**Deployable with a caveat that must travel — three:** Tertullian *Apol.* 30 (reframe: not *"no incense to emperors"* but *"the sacrifice God requires is prayer, not purchased incense"*), Barnabas 2 (do not say *"Barnabas says God abolished incense"*), Justin *2 Apol.* 5 (an aetiology of **pagan** cult; the extension to Christian ceremonial proves too much).

⛔⛔ **Do NOT deploy as cited — two:**

- ***De Corona* 10** — wrong chapter, and the cited chapter hands the opponent Tertullian burning incense in his own house. If the soldier point is wanted, cite **ch. 11** and state honestly that its reason is idolatry-avoidance.
- ***Divine Institutes* 6.25 — NEVER as a quotation.** The submitted sentence conflates three separate ones: the word *incense* occurs **exactly once in all of Book VI** and it is inside **Lactantius's quotation of Hermes Trismegistus** (which he endorses — *"And he spoke rightly"*), while the *"ignorant of what God is"* clause has **garments and jewels** as its subject. ⚠️ And Lactantius is early-fourth-century, not ante-Nicene in the useful sense — ⭐ which cuts both ways: a theological objection stated as the persecution lifted is harder to explain away as prudence.

---

## 6. Sourcing — and it is a tier stronger than the commentary survey's

⭐⭐ **All eight read at Tier 1** — complete works from text-archive hosts (New Advent's ANF; CCEL's Schaff ANF) — with **no aggregator text used anywhere**, against `260835-44`'s 13 of 17 resting on Tier 2.

⭐⭐⭐ **The three Tertullian passages are DOUBLE-ATTESTED**, each read twice on two independent hosts. **This was deliberate: all three of this pass's corrections fall on Tertullian, and a transcription error would have manufactured a false correction.** The readings agree.

⚠️⚠️ **The `260835-44` limitation applies unchanged and is restated rather than assumed carried forward: NO SOURCE WAS CAPTURED TO `src/`.** Nothing here is hash-verifiable, no page number in the file is citable to a printed edition, and the ⏳ flag to capture pages before any outward verbatim deployment is **still owed and now covers this file too**.

### 6a. Retrieval defects, reported not papered over

- ⛔ **The brief's own primary URLs for ALL THREE Tertullian citations returned an EMPTY BODY** — `tertullian.org/anf/anf03/anf03-18.htm` and `…anf03-05.htm`, on repeated attempts. The authorised New Advent and CCEL fallbacks were used; **no secondary paraphrase was touched at any point.**
- ⚠️ **The Athenagoras page's printed footer was never seen** (the fetch truncated before it). Its translator attribution is **inferred** from the companion Athenagoras work on the same host and ANF volume, and is **labelled as inference in the file itself**, not presented as transcription.
- ⚠️ **Lactantius Book VI is at `newadvent.org/fathers/07016.htm`** — none of the numbers the brief suggested; reached via the *Divine Institutes* table of contents, and read through a browser because the page exceeded the fetcher's limit.

---

## 7. Named departure from the brief

⚠️ **The same departure `260835-44` had to make, and reported rather than taken silently.** The brief's deliverable list named only the new file and the `SRC_Manifest.md` registration. That registration raises validator **`[C3] VERSION DRIFT` as a hard ERROR** unless the registry cell moves with the stamp, and `CLAUDE.md` close-out rule 3 binds them together.

**The MINIMUM registry edit was made:** `PROJECT_STATE.md`'s stamp, its gate and pass note, `SRC_Manifest.md`'s stamp, and **two §4 rows** — one new row for the new file, one bump for `SRC_Manifest.md`. **Nothing else in `PROJECT_STATE.md` was altered.**

⚠️ **One smaller widening, also reported:** the brief specified one quotation under fifteen words per entry, and that is what §4 of the file carries. **Where a verdict turns on which words are actually in the text — the three corrections, `#1`, `#6` and `#8` — short additional fragments are shown, every one under fifteen words**, because a correction that cannot show the words is not checkable. Stated on the file's own face at §0.

---

## 8. What this pass deliberately did NOT do

- ⛔ **Drafted nothing for Discord; posted nothing; nothing shown to Rev. James.**
- ⛔ **`St_Francis_EMC_Distinctives.md`, `RJ_Incense_Analysis.md`, `Incense_Conversational_Outline.md` and `Protestant_Commentary_Survey_Malachi_1_11.md` NOT touched.**
- ⛔ **`src/SRC_Discord_RPW.md` NOT touched** — the `[C1]` figure is corrected in the record only.
- ⛔ **The Brattston article NOT evaluated.**
- ⛔ **`SRC_Coverage_Register.md` NOT touched** (§12 ruling).
- ⛔ **No search made for ante-Nicene texts beyond the eight named.** ⏳ Whether any ante-Nicene text refuses incense **in Christian assembly** is **flagged and expressly not answered** — none of the eight is one. ⚠️ Cross-referenced rather than adjudicated: `LS-25` already records Rev. James conceding the early patristics run *"continually"* against incense, so the historical direction is not in dispute between the parties; what follows from it is.
- ⛔ **Nothing minted. `DQ-9` not moved; `OQ20` not moved; no gate moved; no channel state changed.**
- ⛔ **NOT COMMITTED.**

---

## 9. Validator and artifacts

| | Result |
|---|---|
| **BEFORE** (working tree, and clean `HEAD` clone) | `84 ok · 11 warnings · 0 errors` |
| **AFTER** | **`86 ok · 11 warnings · 0 errors`** |

✅ **Exactly the brief's stated expectation.** The two new `ok` results are the new file entering **`C3`** (stamp parse) and **`C8`** (coverage). ⭐ **The warning set is unchanged** — same eleven codes, same files. ⚠️ The `[C1]` instance count reads four both before and after; see §2, it was already four at `HEAD`.

### Artifacts written

- `passes/260835-47_patristic-verification.diff` — 176,806 bytes
- `passes/260835-47_patristic-verification_close-out.md` — this file

### Diff verification — done properly, not asserted

- ✅ **Reverse-apply check CLEAN** (`git apply --reverse --check`).
- ✅ **Forward-apply check CLEAN against a pristine `HEAD` `c33bd5b` clone**, then **actually applied** there.
- ✅ **Validator run in that clean applied tree returns `86 ok · 11 warnings · 0 errors`** — the AFTER figure is reproduced from the diff alone, not merely observed in the working tree.
- ✅ **`sha256` of the new file in the applied tree = `41b0265e…`, an EXACT match to the digest registered in `SRC_Manifest.md`.**
- ✅ **Exactly three files in the diff**, as intended: `PROJECT_STATE.md`, `SRC_Manifest.md`, and the new `Patristic_Citations_Incense_Verification.md`.
- ⭐ The new file was staged `--intent-to-add` solely to generate the diff, and **the index was reset immediately afterwards**; `git status --short` before and after is identical.

---

## 10. Commit sequence for JD

```bash
cd ~/EMC/theology
rm -f .git/index.lock
git add passes/
git commit -m "260835-47: patristic verification — pass artifacts"
git push
git log -1
```

Corpus edits second, after review.

*(§5 rule 11 — this close-out makes no claim about its own commit state.)*
