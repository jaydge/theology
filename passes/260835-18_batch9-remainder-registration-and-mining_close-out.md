# 260835-18 — Batch 9 remainder: registration, attribution and targeted mining

**Pass type:** source registration, attribution, and targeted mining. ⛔⛔ **NO FINDING MINTED. NO NUMBER OF ANY PREFIX CONSUMED EXCEPT `File`.**

---

## ⛔⛔ READ THIS FIRST — FOUR THINGS THE BRIEF GOT WRONG, REPORTED RATHER THAN COMPLIED WITH

Stated at the top because three of them would have caused duplicate or false work.

1. ⚠️ **"Thirteen files" is FOURTEEN.** The groups the brief itself lists total **6 + 1 + 5 + 2 = 14**. All fourteen were handled; the arithmetic is reported, not silently reconciled.
2. ⛔⛔ **SEVEN OF THE FOURTEEN WERE ALREADY REGISTERED.** All of Group C and all of Group D are `File 57`…`File 63`, registered at `260835-14`. The brief says *"Register"* for five of them. **This pass EXTENDED their rows with dated notes rather than duplicating them.** No File number was wasted.
3. ⛔⛔⛔ **TWO OF THE SIX "never registered or mined" GROUP A FILES WERE ALREADY MINED.** `UmIAkdRtzhw` is the source of `BP-1`/`BP-2`/`BP-Icons`; `imipCdI7B9s` is the source of `BP-19`/`BP-20`/`BP-23`/`BP-24`/`BP-25`/`BP-26`/`BP-Switch`. Both from `260619-2`, whose own changelog names the `BP` batch as *"5 videos: **icons**, sacrament validity, **switching traditions**, five reasons for Anglicanism, and a response to Matthew Everhard on the regulative principle."* ⭐⭐ **This is the FOURTH failed "unmined" premise today** (`260835-4` on `a201.txt`, `260835-6` on `a202`, `260835-11` on `TeachingTheMass`).
4. ⚠️⚠️ **THE READ-ALOUD LAYER IS OWED ON FOUR FILES, NOT ONE.** The brief applies it only to `IGNmKMXhL1Q`. **`File 68` and `File 69` need it far more — they are read-aloud END TO END, 100%, with zero own-voice content** — and `File 65` and `File 66` quote at length.

---

## Gate

| Item | Value |
|---|---|
| HEAD | `5c30223572826ed61ff7b0ef84a3888aca0068e7`, branch `main` — matches the briefed `5c30223` |
| `git --no-optional-locks status --short` before first edit | ⭐ **EMPTY** — captured directly, not reconstructed |
| Validator BEFORE | **`82 ok · 9 warnings · 0 errors`** |
| Validator AFTER | **`82 ok · 9 warnings · 0 errors`** — identical, same nine codes, **no regression** |
| `PROJECT_STATE.md` stamp at gate | **`260835-16`** |
| This pass | **`260835-18`** |
| Next-free `File` at gate | **`File 65`** · now **`File 72`** |
| Next-free `LS` | **`LS-129`** — free, **NOT consumed** |

**Nine firing codes, individually, before and after (unchanged):** `[C1]` `src/SRC_Discord_RPW.md` 2 relative timestamps outside message headers · `[C3]` `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` no parseable stamp · `[C3]` `tools/transcribe_yt.py` no parseable stamp · `[C4]` `St_Francis_EMC_Distinctives.md` 2 stale answered-question passages · `[C5]` `RJ_Final_Question_List.md` 17 volatile-state assertions · `[C5]` `RJ_Incense_Analysis.md` 9 · `[C5]` `St_Francis_EMC_Distinctives.md` 7 · `[C10]` §15 eight findings behind the `LS` ledger head · `[C11]` outline eleven `IP` findings unreviewed. **None of this pass's business.**

**Stamp derivation, fresh and by grep — the brief's three-collisions warning was honoured.** A repo-wide content grep for `26[0-9]{4}-[0-9]+` tops out at **`260835-17`**. ⭐ **`260835-17` is a REAL consumed stamp, not a next-free assertion**: it has a committed artifact (`passes/260835-17_rc6-gate-halt_read-and-report_close-out.md`) and is named in `5c30223`'s own commit message. `grep -rn "260835-18"` returned **zero matches repo-wide.** **This pass is `260835-18`.**

**`File` re-derived independently.** Highest REGISTERED is `File 64`; every `File 65` occurrence repo-wide was opened and read, and all are next-free assertions inside `260835-16`/`260835-17` prose. **`File 65` was free.**

**`LS` re-derived independently.** Highest is `LS-128`; every `LS-129` occurrence is a next-free registry assertion. **`LS-129` free, not consumed.**

**FUSE lock.** The `260835-3` diagnosis was **applied, not re-derived** — every git read used `git --no-optional-locks`; no lock created, none removed, no `rm` attempted.

---

## ⭐⭐⭐ THE HEADLINE — A DATED CONTRADICTION ON THE PROJECT'S CENTRAL QUESTION, WITH ITS OWN COUNTER-EVIDENCE

### The counter-reading goes first, because it comes from the same file

⚠️⚠️ **In `File 65` he demonstrably uses *"we hold"* for a position he personally rejects.** @7232-7290: *"the superstition of the Middle Ages is **we hold** to the understanding of real presence or transubstantiation, **which I don't hold to**, but for general sake, real presence."*

⛔⛔ **So *"we hold"* in his mouth is NOT reliably a first-person subscription — he marks his own dissent explicitly when he means to.** This materially weakens the datum below and must be quoted alongside it.

### The datum

**`File 65`** (`gA-ELOCiwC8`, **2020-04-09**), @8388-8439 and @8661-8732:

> *"So Lutherans and Anglicans — **you know, Anglican here** — **we hold to what is known as the normative principle of worship**. … The regulative principle is the belief that unless Scripture explicitly says to worship in this way, you cannot worship in this way. **The normative principle is, unless Scripture forbids it, you can worship in this way.**"*

### Why it is nonetheless load-bearing

⭐⭐⭐ **It supplies precisely what `LS-47` was DECLINED from §15 for lacking.** That decline reads: *"He places Anglicans under the normative principle **descriptively** and **does not subscribe in the first person**."* Here, five months **earlier**, the self-locating aside *"you know, Anglican here"* attaches him personally to the "we."

⛔⛔ **Against `IP-2` and `BP-35` (both 2026):** *"I would say **I hold to the regulative principle**"*, with the normative label **explicitly rejected** as *"too loosey-goosey."*

⚠️ **Three readings, none adopted:**
- **(a)** a genuine development 2020 → 2026;
- **(b)** no change at all — the 2020 line is descriptive in the `LS-47` sense, which the real-presence sentence above makes live;
- **(c)** stable substance under shifting labels — which is **`IP-2`'s own `[Analysis]`**: the rule he OPERATES is *"functionally the NORMATIVE principle wearing RPW vocabulary."* ⭐ **Reading (c) is the most economical and therefore the one to be most suspicious of.**

⛔⛔ **`DQ-9` IS NOT MOVED. NOT MINTED**, on the `260835-4`/`260835-14` locate-and-hand-over precedent. Byte ranges registered so a minting decision costs nothing.

---

## ⭐⭐⭐ `RC1-10` LOCATED, `QC-b` ANSWERED — AND IT RUNS AGAINST JD's OWN LEVER

⭐ **`260835-16` concluded *"`RC1-10` remains NOT FOUND anywhere in the corpus."*** That was **correct against the sources then held** and is now **superseded, not contradicted** — by a source registered this pass.

**`File 66`** (`9SMGzwSsMSI`, 2021-07-05) @9282-9327, unprompted, in a confirmed-solo recording:

> *"But then I, as somewhat more of a high churchman, **I'm not a fan of the homilies that talk about how evil iconography is** and things like that."*

⛔⛔ **`St_Francis_EMC_Distinctives.md` L1283 PREDICTED THIS AND NAMED THE COST:** *"The anti-image Homily … is the natural candidate; **if he rejects it, the Q2 'by your own standard' lever weakens.**"* **He rejects it, by name, in his own voice. THE `Q2` LEVER WEAKENS.**

⭐ A prediction the corpus made and then had confirmed **against its own interest** is worth more than one confirmed in its favour, and it is recorded that way.

⭐ **It also settles the entry's own either/or** in favour of the second option: **general affirmation with a now-specified exception, not a development.** He affirms the Homilies as formularies at @6392-7451 of the **same recording** (quoting Article XXXV in full) while excepting the anti-iconography ones. ⚠️ **Both halves are minutes apart in one recording, so a chronological "development" reading is not available for this source.**

⛔ **`QC-b` is RE-SCOPED, not closed:** the open question is no longer *which* Homilies he excepts — that is answered — but whether the exception is **principled or preferential** (*"I'm not a fan"* is a taste register, not an argument).

---

## ✅⭐⭐⭐ A BLOCKING EAR-CHECK DISCHARGED FROM CONTENT — `E2` NEEDED A DIFFERENT TEST, NOT AN EAR

`260835-14` listed `E2` as one of two **blocking** items and judged that *"content cannot decide it."* ⭐ **It can, and the reason the earlier pass could not is instructive.**

**That pass asked *which texts* each label carries** — and rightly found that label `B` holds the congregational response, the officiant's versicle **and** the homily, which no single role does.

⭐⭐ **The decisive test is different: whether a single continuous text is split ACROSS labels mid-unit.** It is, **three times**:

| # | Text | Turns | What happens |
|---|---|---|---|
| 1 | **The homily** | t11 `B` → t12 `A` → t13 `B` | *"Brothers and sisters, we cannot bring ourselves back from the dead."* (`A`) → *"We cannot even bring others back from the dead."* (`B`) — **one sentence-pair, one argument, cut in half across labels** |
| 2 | **The Apostles' Creed** | t14 `A` → t15 `B` → t16 `A` | Cut **mid-creed** |
| 3 | **The Lord's Prayer** | t19 `B` → t20 `A` → t21 `B` → t22 `A` | Cut **mid-petition** |

⛔⛔ **No two-officiant arrangement produces a creed or a Lord's Prayer split mid-sentence between two men. The diarizer is splitting ONE voice at register changes.** ✅ **`E2` IS CLOSED AND NEEDS NO EAR-CHECK.**

### ⛔⛔ But minability stays narrow, for the other reason the brief named

**~84% of `File 60` is read-aloud BCP and Scripture.** Of ~3,567 words, **only turns 11-13 (14:45-19:14, ~555 words — the homily) are his own composed words**, plus the rubrical aside at t34. **Everything else is the office, the canticles, John 11, the creed, the Lord's Prayer and the collects.**

⭐⭐ **And the homily yields something real: the corpus's first definition of an idol in his own composed words** (@11744-11788):

> *"**They do not have to be made of stone or wood and physically bowed down to in order to be an idol. An idol is someone or something that you enslave yourself to apart from God.**"*

⛔⛔ **This broadens *idolatry* away from physical images toward interior enslavement — structurally, it is the move that makes room for keeping images.** ⭐ Same move as `File 70`'s *"you can have images as long as you don't worship them"*, stated **three months earlier, from the pulpit, and generalised past images altogether.** ⚠️⚠️ **HONEST QUALIFICATION: he is preaching on Lent, sin and Lazarus — NOT on iconography, and NOT answering any objection about images. He is not defending icons here, and reading it as a defence would put an intention in his mouth.** Logged as a definition he holds **from which a defence follows**, not as the defence.

---

## ✅⭐⭐ `File 62`'s MINING BLOCK RESOLVED — AGAINST MINING

`260835-14` left owed: *"settle whether `6Z68nITG1Is` is the `[S]` twin of `A101-2026-08-09`… mining risks re-mining `IP-45`…`IP-68`."* **It refused out of caution. The refusal now rests on positive evidence.**

⭐ An 8-gram shingle probe of `File 62`'s **speaker-`A` text only** against the live corpus returns a load-bearing match: the invocation-of-saints material — ***"asking the Father to have the saints in heaven pray for us"*** — **is `IP-47`'s own core datum** (`St_Francis_EMC_Distinctives.md` L1386, L2192, L3274; anchored §12, dual-ASR verified).

⛔⛔ **`File 62`'s CONTENT IS ALREADY HELD. DO NOT MINE.**

⚠️ **Stated at its real strength:** this establishes substantial **verbatim OVERLAP** with already-mined material. **It does NOT by itself establish that `6Z68nITG1Is` and `A101-2026-08-09` are the same event** — `260835-14`'s content analysis (Articles XVII-XXII vs. 08-09's Article XVII plus Lent and calendar) still cuts the other way, and the manifest's own *"existence is NOT established"* warning on that stream row stands. ⛔ **NO dual-capture row created**, per the `260833-3` established-not-assumed standard.

### ⭐ `File 63`'s `RV` de-duplication probe — clean, and the limit stated

`260835-14` left it *"UNVERIFIED, not verified."* The same probe returns **7 hits, all opened and read: every one is `260835-14`'s OWN quotation of this file** in `SRC_Manifest.md` L3587 and `PROJECT_STATE.md`. **Zero hits against any `RV` finding.**

⚠️⚠️ **NOT PROOF, and said so plainly:** the probe compares exact 8-grams of **this** ASR rendering against a corpus built from **other** renderings, so ASR divergence alone can produce a true negative — the `260835-4` lesson. ⛔⛔ **And mining stays blocked on the unchanged ground: `File 63` is a CONFIRMED COLLAPSED-LABEL FILE**, requiring a sentence-by-sentence register check, which is more than targeted mining.

---

## Group A — six files, single-voice verification

⛔ **Per the brief, the auto-detect label was NOT trusted. Every file was checked for a second voice in content** — audience address, named individuals, Q&A, congregational response.

| File | Video | Solo? | Evidence from content |
|---|---|---|---|
| **66** | `9SMGzwSsMSI` | ✅ **YES** | ⭐⭐⭐ **The file states its own warrant** @45-73: *"These next few sessions are just going to be **recorded without an audience** because I will be gone for the next few weeks."* **The strongest content warrant for solo status in the corpus.** All apparent second-voice markers are self-corrections (*"Sorry, I'm throwing a little bit too much"*, *"Excuse me"*). |
| **70** | `UmIAkdRtzhw` | ✅ YES | Rhetorical questions posed and self-answered; *"Sorry, I'm moving, and I'm on a table"* is a self-aside. |
| **68** | `xcNz2wdI2P8` | ✅ YES | 19 `Amen.` and 3 `Father,` are all **read liturgical text**, not responses from a room. |
| **69** | `M7iSL5mznTk` | ✅ YES | Same; 194 seconds, one continuous devotion. |
| **71** | `imipCdI7B9s` | ✅ YES | *"I'm sort of an intro to help **you guys** out"* — a **video** audience, not a room. |
| **65** | `gA-ELOCiwC8` | ✅ YES | *"whatever **you guys** are calling it in the future. **Hello from the past**, by the way"* @459 — decisively a video audience. |

⭐ **Six for six confirmed solo — but the assumption the brief warned against was still worth checking, because it changed the disposition of three files.**

---

## Group B — `MLvweRO41bo`, speaker identification

⭐⭐⭐ **SETTLED BY SELF-IDENTIFICATION AT TURN 0, @60-77:**

> *"Again, welcome to the Barely Protestant YouTube channel. **I am Father James**, and tonight we have a special guest. **This is Austin from Gospel Simplicity.**"*

**`A` = Rev. James. `B` = Austin (Gospel Simplicity), a guest — NON-QUOTABLE as him.**

⚠️⚠️ **THE DURATION TRAP FIRED EXACTLY AS THE STANDING HAZARD PREDICTS: the GUEST has MORE material than the host** — `B` 266 sentences / 4,920 words against `A`'s 207 / 3,253. ⛔ **Turn order and duration would BOTH have got this backwards. Only the self-identification was used.**

⚠️ **Labels verified CLEAN across the whole file.** An initial concatenation of all `A` sentences appeared to interleave questions and answers; **that was an artifact of concatenation, not a merge.** Checked against actual turn boundaries, the file is a clean alternating interview. **Reported because the false alarm is itself instructive: never diagnose a merge from concatenated text.**

⚠️⚠️ **A SECOND, SHARPER TRAP IN THE SAME FILE — BOTH MEN NARRATE A MEGACHURCH BACKGROUND.** `A` @29584: *"my old church … was a **Southern Baptist** megachurch."* `B` at 08:48: *"growing up I was in like a **non-denominational** quasi-megachurch."* ⛔ **Two different men's biographies. NEVER CONFLATE.** ⚠️ Also: this "Austin" is **not** `File 14`'s guest "James Austin" — a different person entirely.

---

## Group D — formal exclusion

⛔⛔⛔ **DISPOSITION RECORDED: `EXCLUDED` — CONFIRMED NOT REV. JAMES. NO FINDINGS MINED, AND NONE EVER TO BE MINED FOR HIS POSITIONS.** A **formal closure, not a silent skip**, so no future pass reopens it. Both files stay registered, hashed and locatable precisely so the exclusion is a matter of record. Grounds **re-checked, not assumed**: the four in-recording anchors naming Ray, plus the 2017 uploads against his 2020 diaconate.

⭐⭐⭐ **AND AN INDEPENDENT LINE FROM ELSEWHERE IN THE CORPUS CONVERTS THIS FROM AN ANOMALY INTO AN EXPLAINED FACT.** `St_Francis_EMC_Distinctives.md` L430 already records, from the `RC` batch, that Rev. James ***"names his first priest and mentor 'Father Ray.'"***

⭐⭐ **The Fr. Ray videos are on his channel because Fr. Ray was his own priest and mentor — he recorded and uploaded his rector's classes.** ⛔ **This is CORROBORATION of the exclusion, not a qualification of it** — it explains the upload without making one word of the teaching his. It also **strengthens the `EXT-2`-is-not-a-speaker-warrant rule by supplying its mechanism**: the channel carries the teaching of the man who formed him.

**Inventory decision cells for both set to `DECLINED — NOT REV. JAMES`, per the brief.**

---

## ⛔⛔⛔ A `GV-50`-CLASS TRAP, FLAGGED BEFORE ANYONE HITS IT — AND IT SITS ON THE BRIEF'S OWN TARGET LIST

**`File 69`** (`M7iSL5mznTk`) is 2,447 bytes of **pure read-aloud devotion with one confirmed speaker** — the configuration most likely to be mined flat. It contains, **in the first person singular**:

> *"**I believe that Thou art truly present in the Holy Sacrament**"*
>
> *"with the faithful at every altar of Thy Church, where **Thy Blessed Body and Blood are being offered to the Father**"*

⛔⛔ **THAT IS EUCHARISTIC PRESENCE AND EUCHARISTIC SACRIFICE LANGUAGE, IN THE FIRST PERSON, IN A CONFIRMED-SOLO FILE — AND IT IS THE PRAYER BOOK'S WORDS, NOT HIS.**

⛔⛔⛔ **The brief's own target list names *"eucharistic presence and sacrifice."* A targeted mining pass aimed at exactly that phrase-set would have landed here first.** **He recited a traditional devotion. He asserted nothing.**

### ⭐⭐ What `File 68` and `File 69` DO yield: practice, not content

The read-aloud rule removes the text but **not the act**. Evidenced by the recordings themselves: **in March 2020 he publicly led the Stations of the Cross from St. Augustine's Prayer Book (2nd ed.) and an Act of Spiritual Communion in the traditional rite.** ⭐ These are **Anglo-Catholic devotional practices**, and the practice datum is his own — it rests on what he **did**, not on what the text says. **[Stated-Analysis]** ⛔ **NOT MINTED.** It coheres with `LS-9`/`LS-80`/`VP-5` (Pusey-wing) without being cited by any of them.

---

## ⭐ METHOD NOTE — THE DE-DUPLICATION PROBE, AND ITS ONE ESSENTIAL REFINEMENT

An **8-gram shingle probe** of each new transcript against the live corpus (`St_Francis_EMC_Distinctives.md`, `RJ_Incense_Analysis.md`, `RJ_Final_Question_List.md`, `SRC_Manifest.md`, `RJ_Open_Questions_and_Divergences.md`, `On_Incense_and_the_Altar.md`, `Calvin_Luther…md`, `Incense_Conversational_Outline.md`).

⛔⛔ **THE RAW COUNT IS WORTHLESS WITHOUT DISCRIMINATING QUOTED TEXT FROM OWN VOICE.**

| File | Hits | Verdict | Why |
|---|---|---|---|
| `File 66` | **11** | ✅ **VIRGIN** | Every hit is **formulary text** — Article VI's *"nor may be proved thereby"*, Homily 11's *"the same lesson doth the Holy Ghost also teach"*, Article XXIX's *"the wicked which eat not the body of Christ"* — which the corpus quotes from **other** sources |
| `File 65` | **1** | ✅ **VIRGIN** | The hit is **Colossians 2:17** |
| `File 70` | **10** | ⛔ **ALREADY MINED** | Hits are **his own words** — *"few icons myself… packed in my car"* (`BP-1`), *"I don't see why images would not be allowed in worship"* |
| `File 71` | **2** | ⛔ **ALREADY MINED** | *"Edward Pusey is one of my favorite theologians"* (`BP-23`) |
| `File 67`, `68`, `69` | **0** | ✅ VIRGIN | — |

⭐⭐⭐ **A naive shingle count would have wrongly excluded the two most valuable files in the batch and wrongly admitted the two already-mined ones. READ THE HITS; NEVER COUNT THEM.**

---

## §8 — Registrations: `File 65` … `File 71`

| File | Artifact | Bytes | sha256 (first 8) | Video | Date | Attribution / minability |
|---|---|---|---|---|---|---|
| **65** ⭐⭐⭐ | `CoronavirusEasterClaim-transcript.txt` | 24,156 | `a7dfa485…` | `gA-ELOCiwC8` | 2020-04-09 | ✅ SOLO confirmed · ⚠️ partial read-aloud · ⭐⭐⭐ **richest RPW file in the batch** |
| **66** ⭐⭐ | `A101-Session2-ConfessionalStandards-transcript.txt` | 33,679 | `90e2bf0f…` | `9SMGzwSsMSI` | 2021-07-05 | ✅ SOLO, **self-warranting** · ⚠️ heavy read-aloud |
| **67** ⭐⭐ | `Talk-Austin-GospelSimplicity-transcript.txt` | 43,805 | `77069383…` | `MLvweRO41bo` | 2021-03-03 | ✅ `A` = Rev. James (**self-ID**) · ⛔ `B` = **Austin, NON-QUOTABLE** |
| **68** ⛔⛔ | `StationsOfTheCross-transcript.txt` | 17,700 | `80dbccf5…` | `xcNz2wdI2P8` | 2020-03-27 | ✅ SOLO · ⛔⛔⛔ **100% read-aloud. PRACTICE ONLY.** |
| **69** ⛔⛔ | `SpiritualCommunionLiturgy-transcript.txt` | 2,447 | `809ae7d9…` | `M7iSL5mznTk` | 2020-03-20 | ✅ SOLO · ⛔⛔⛔ **100% read-aloud; `GV-50` TRAP. PRACTICE ONLY.** |
| **70** ⚠️ | `IconsIdolatrous-transcript.txt` | 12,338 | `e8c134f8…` | `UmIAkdRtzhw` | 2020-07-03 | ✅ SOLO · ⛔⛔ **ALREADY MINED (`BP-1`/`BP-2`). DO NOT RE-MINE.** |
| **71** ⚠️ | `AdviceSwitchingTraditions-transcript.txt` | 15,768 | `e04470ed…` | `imipCdI7B9s` | 2021-01-13 | ✅ SOLO · ⛔⛔ **ALREADY MINED (`BP-19`…`BP-26`). DO NOT RE-MINE.** |

Hashes computed fresh with `sha256sum` over the raw bytes of each `-transcript.txt`, **not** the `-meta.json` `sha256` (which is of the audio). **No collision with any previously registered hash.** **Next free File is now `File 72`.**

⛔⛔ **NO OTHER NUMBER CONSUMED. Next-free values re-derived and unchanged: `DQ-25`, `IP-109`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EXT-4`, `W47`.**

---

## §9 — Other material located and handed over, none minted

- ⭐⭐ **The corpus's earliest direct incense argument** (`File 65`, 2020, @9887-9934 / @10337-10380): he names incense as a thing RPW followers disallow, and answers — *"**incense is all throughout the Old Testament and is in the New Testament too. It's in the Book of Revelation.**"* ⭐ **The Revelation prong and the OT-continuity prong of `IP-3`, together, six years before their earliest current attestation.** ⛔⛔ **The two-way caveat `260835-4` and `260835-14` both recorded applies again and is recorded again: it is stated inside a defence of KEEPING EASTER, not of incense as such. NOT logged as supporting the incense lever.**
- ⭐ **A third independent 2020 burden-rule attestation** (`File 65` @16701-16752): *"**where in the Bible does it say that you are allowed** to go through a book of the Bible every Sunday…?"* — a burden-inversion *tu quoque* on a third topic. ⛔ The `DQ-19`/burden-rule numbering judgment remains JD's, exactly as `260835-14` left it.
- ⭐ **The RPW subjectivity critique** (`File 65` @9237-9808): chapter-and-verse divisions, books vs. scrolls.
- ⭐⭐ **§12 gains its first sustained icon apologetic** (`File 66` @20732-25317) including ⭐ **the first RESTRICTION he places on images** (*"what we cannot do is depict the divine nature of Christ or depict the Father… Those are considered wrong"*), his readings of Luther and Calvin, and the Elizabeth I crucifix anecdote.
- ⭐⭐⭐ **The transferable one is about the ALTAR, not icons** (`File 66` @26443-26486): *"**you can reverence items used within worship without actually worshiping those items**,"* argued from OT precedent and received Anglican practice. ⛔⛔ **This is the reverence/worship distinction as a GENERAL principle about physical objects in worship — the form in which it would license incense and the altar. NOT MINTED, and NOT logged as incense support: whether it does that work is the contested question itself.**
- ⭐⭐ **A third ranked authority-ordering in his own voice** (`File 66` @5384, @32919-32967): *"we have again Scripture as the highest authority. Under that … the ecumenical councils … And then under that … the uniquely Anglican formularies."* ⭐⭐ **`260834-5`'s finding SURVIVES: *tradition* is still NOT a discrete ranked item.** The axis is closer to `IP-40`'s than to `DQ-24`'s. ⚠️ Whether it is a `DQ-24` antecedent is a judgment `260834-5` reserved, and it stays reserved.
- ⭐⭐ **Four conversion-chain additions** (`File 67`, `File 61`): an **agnosticism/deconstruction stage** absent from `BP-20`/`BP-26` (@7097, with the datable *"didn't finish [college] until I was 27 or so"*); the **EO brake SPECIFIED** (@27820, *"wasn't as catechetical as I wanted it to be"*) — ⚠️⚠️ **a LITURGICAL objection, not one of the "dogmatic reasons" the corpus logs as missing; the gap NARROWS, it does NOT close**; a **fourth self-label, *"Bible Catholic"*** (@3334); and the **infant-baptism-by-liturgical-experience** datum (@36908) — ⛔⛔ **`[Stated-Analysis]`, and expressly NOT to be deployed as a gotcha.**
- ⭐⭐ **`File 61`'s `E1` gains independent content support** (@35611): *"This church right here, **we left under Bishop Pike**… **St. Paul's here.**"* — Pike was Bishop of California 1958-66, a Bay Area parish. ⚠️ **Recorded as corroboration of a resolution JD already made via the Los Altos comment, not as this pass re-deriving it.**

---

## §10 — What was NOT touched

⛔ **`Incense_Conversational_Outline.md` and `RJ_Incense_Analysis.md` NOT touched.** ⛔ **Nothing drafted, altered or posted to Rev. James.** ⛔ **No existing finding altered, renumbered, re-pointed or corrected** — every addition is a **dated note beside the original**. ⛔ **No byte offset in any existing entry altered. No existing hash changed.** ⛔ **`validate_project.py`, `RJ_Final_Question_List.md`, `RJ_Open_Questions_and_Divergences.md`, `On_Incense_and_the_Altar.md`, `ORCHESTRATION.md`, `SRC_Coverage_Register.md`, `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` NOT touched.** ⛔ `DQ-9` unmoved · `DQ-24` untouched · `IP-2` untouched · `LS-47` untouched · no Discord state touched · no `VP-` pair, `DELTA`, gate or channel state moved · no attendee or private individual named.

**Touched four tracked files:** `PROJECT_STATE.md`, `SRC_Manifest.md`, `SRC_Channel_Inventory.md`, `St_Francis_EMC_Distinctives.md` — plus this new `passes/` artifact.

---

## §11 — Owed

- ⏳⏳ **JD's ruling on the `File 65` normative/regulative datum** — new finding, corroboration, or nothing. **This is the largest open item in the pass and it sits on `DQ-9`.**
- ⏳ **`QC-b` re-scoped** — principled exception or preferential one?
- ⏳ **The `Q2` lever needs re-weighting** now that `RC1-10` is specified against it.
- ⏳ **`260835-14`'s remaining ear-checks**: `E3`, `E4`, `E5` (all confirmations, none blocking). **`E1` and `E2` are now both discharged.**
- ⏳ Recovery of the original `96a9c5a9` `[R]` markdown (unchanged from `260835-14`).
- ⏳ **`ORCHESTRATION.md` §8 amendment: `EXT-2` channel ownership is NOT a speaker warrant** — still owed from `260835-14`; ⭐ **this pass supplies its mechanism (Fr. Ray was his own rector) but does not write the amendment.**
- ⏳ **`File 55` remains a better mining candidate than its row suggests** (unchanged from `260835-14`).
- ⏳ Whether `6Z68nITG1Is` and `A101-2026-08-09` are the same event — **still open**, though the practical mining question it blocked is now answered.

*(§5 rule 11 — this note makes no claim about its own commit state.)*
