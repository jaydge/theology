# 260835-38 — Perseus Men's Conference 2024, the two liturgies: attribution, observed ceremonial practice, and mining (close-out)

**Mode:** Intake-and-reconcile, two new `[S]` sources. **Committed:** nothing — per the brief, JD pushes `passes/` first, then corpus edits separately. No `.diff` accompanies this close-out; the corpus edits are described in full below and are visible in `git status --short` / `git diff` on request.

---

## Gate

| Item | Value |
|---|---|
| `git rev-parse HEAD` | `7a09b007d13a984922966b3a5cd6e3bd7b454448` |
| HEAD commit message | `260835-37: duplicate-registration sweep completed — three more videos …` |
| Matches where the small-items pass left the repo | ✅ **Yes.** `260835-37` is the last pass; `PROJECT_STATE.md`'s own stamp reads `260835-37`; `ls passes/` tops out at `260835-37`; `git log --all` tops out at `260835-37` (`7a09b00`). All four agree. |
| Branch | `main` |
| `git --no-optional-locks status --short` before first edit | **EMPTY** — captured directly, not reconstructed. Every git read in this pass used `git --no-optional-locks`. |
| Validator BEFORE | **`85 ok · 8 warnings · 0 errors`** |
| `PROJECT_STATE.md`'s own stamp at gate | **`260835-37`** |
| Next-free pass stamp | **`260835-38`** — derivation below |
| Next-free `LS` at gate | **`LS-138`** (re-derived fresh) — ⭐ **CONSUMED** `LS-138`…`LS-141`; next free **`LS-142`** |
| Next-free `File` at gate | **`File 83`** (re-derived fresh) — ⭐ **CONSUMED** `File 83`, `File 84`; next free **`File 85`** |
| Other prefixes consumed | ⛔ **NONE** — no `DQ`, `IP`, `RV`, `Rev`, `BLOG`, `POD`, `VP`, `GV`, `RC`, `BP`, `EXT`, `W` or `DELTA`. |

### Baseline warnings — all eight reproduced, not summarised

1. `[C1] src/SRC_Discord_RPW.md` — 2 relative timestamp(s) outside message headers (`'Yesterday at …'`).
2. `[C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` — no parseable `Last updated` stamp; registry says `260832-2`.
3. `[C3] tools/transcribe_yt.py` — no parseable `Last updated` stamp; registry says `260833-7`.
4. `[C4] St_Francis_EMC_Distinctives.md` — 2 passage(s) describe an ANSWERED question as pending with no supersede marker.
5. `[C5] RJ_Final_Question_List.md` — 17 volatile-state assertions.
6. `[C5] RJ_Incense_Analysis.md` — 9 volatile-state assertions.
7. `[C5] St_Francis_EMC_Distinctives.md` — 7 volatile-state assertions.
8. `[C10]` — §15's newest `LS` citation is **17** findings behind the ledger head (`LS-120` vs `LS-137`).

✅ `C11` clear on all three arms. ✅ `C2` reports `LS-1..137` unbroken, no duplicates; `File` continuity checked separately below.

### Stamp derivation — hazard note read FIRST

⭐⭐ **The `260835-12`/`260835-14` hazard note was read before anything was derived, as the brief required.** It warns that a naive content-grep misleads **in both directions**: `260835-12` reads as *available* inside prose asserting its own absence but is **REAL and CONSUMED** (the `CLAUDE.md`/Bootstrap divergence audit, commit `530d987`); `260835-14` exists **only** as committed filenames and a commit message, its own internal prose still reading `260835-12`, and is likewise **REAL and CONSUMED** (commit `68bf1d8`). ✅ **Both treated as consumed; neither is in play at this end of the range.**

**Derivation used.** A distinct-stamp sweep over tracked `*.md`/`*.py`/`*.txt` returns an unbroken run `260835-1 … 260835-37` with no gaps. `ls passes/` independently tops out at `260835-37`. `git log --all` tops out at `260835-37` (`7a09b00`). ⚠️ **The one apparent higher hit, `260835-99`, was re-checked in context and re-confirmed NOT a stamp** — the upper endpoint of an absence-assertion range inside earlier close-out prose. ✅ **`260835-38` returns ZERO matches repo-wide, ZERO in `passes/`, ZERO in `git log --all`; `260835-39` likewise ZERO; `260836-<digit>` returns ZERO real stamps** (the 51 raw hits on the bare string `260836-` are all absence-assertion prose inside earlier close-outs, checked). **This pass is `260835-38`.**

**Next-free `LS` and `File` re-derived fresh and independently of the brief.** `LS-1`…`LS-137` unbroken (validator `C2` concurs); `LS-138` appears repo-wide **only** as a next-free assertion (`SRC_Coverage_Register.md` L25, `passes/260835-36_…` L36, `PROJECT_STATE.md` L21) and never as a spent number — **free.** `File 1`…`File 82` unbroken; `File 83` appears **only** as a next-free assertion in the same three places — **free.**

---

## ⛔⛔⛔ THE HEADLINE, STATED FIRST BECAUSE IT INVERTS THE BRIEF'S PREMISE

The brief's framing is: *"Every other source in the corpus is Rev. James arguing about or describing worship. These are recordings of him actually celebrating Evensong and Holy Communion."*

⛔⛔ **That premise is not established by either recording, and this pass could not establish it.** Neither file contains a self-identification, a direct address by name, or any other content warrant for any of its three voices. **The name "James" does not occur in either recording. Neither does "Gadomski", "Father <anything>", "Reverend", "Fr", "priest", "deacon" or "celebrant".** Both files are therefore registered **ATTRIBUTION OPEN**, per the `260835-22` standing instruction (*channel ownership is not a speaker warrant*, and *registration is not a speaker warrant*), and **neither is mined for anyone's positions.**

⚠️ **This is not a new discovery so much as a hardening of one the project already made.** `passes/260835-23_broadened-re-triage_pull-list.md` L25 already records, of these two exact videos: *"The two Perseus liturgies (`egHdlotth9c`, `layuF4wDDMI`) have **no established celebrant**."* The present brief's premise contradicts the pull-list note that recovered them. **Reported per ORCHESTRATION §7, not silently reconciled.**

⭐ **What that costs, precisely.** It does not cost the ceremonial description — the *rite as celebrated* is a fact about the recording and is documented in full below. It costs the inference from the rite to **his** practice. In particular it blocks the single most valuable test these recordings offered, which is set out at `LS-139` and repeated here because it is the reason the pass exists:

> ⭐⭐⭐ **`LS-123` (2024-09-18) is a first-person standing-practice claim — *"I use incense for every form of public worship, right? Whenever we're doing public worship, we have incense."* These two liturgies are dated 2024-10-24 and 2024-10-25 — THIRTY-SIX AND THIRTY-SEVEN DAYS LATER. If he is the celebrant, they are a direct observational test of that claim at the closest date the corpus holds.** ⛔ **The test cannot be run from the audio, for two independent reasons, either of which alone would be fatal: attribution is open, and incense is silent.**

---

## Task 1 — the three speakers, established separately for each recording

⛔ **No label mapping was carried between the two recordings.** They are different services on different days; each was worked from its own content.

### `File 83` / `egHdlotth9c` — Friday Evensong and Holy Communion

| Label | Words | Turns | What the content establishes |
|---|---|---|---|
| `A` | 1,829 | 21 | **The officiant/celebrant — by ROLE, not by name.** Announces the psalm and its page (s5-s6), reads both lessons, recites the Decalogue, reads the long Exhortation (s320), pronounces the Absolution (s333), prays the Prayer of Consecration (s343 ff.), gives the Blessing. ⛔ **NOT a clean single voice — see the trap below.** |
| `B` | 67 | 16 | Almost entirely one-word congregational responses (`Amen`). ⛔ **But it also carries at least one line that is the PRIEST's in the rite** — s58 [18:18] *"Thou shalt not commit adultery."* **Collapsed/scrambled label; unusable as a warrant.** |
| `C` | 3,515 | 10 | **The preacher, and POSITIVELY ELIMINATED as Rev. James — see below.** A guest, preaching on Matthew 25 (sheep and goats), [22:56]–[50:07]. |

⭐⭐⭐ **`C` IS NOT REV. JAMES, AND THIS IS ESTABLISHED FROM CONTENT, NOT ASSUMED.** Two independent grounds, the first decisive:

1. **Adult conversion at 25, roughly twenty years before 2024.** *"I thought I was doing great when I first became a Christian at 25"* (s233, [42:55]); *"now, uh 20-some-odd years later, I'm more shocked every day that Jesus has anything to do with me"* (s234-s235, [42:59]). That places his conversion c. 2000-2004 and his birth c. 1975-1980. ⛔ **Rev. James was raised Independent Fundamental Baptist** (`BLOG-78`, `BLOG-116`, `St_Francis_EMC_Distinctives.md` L562/L579) — not an adult convert — **and was an undergraduate in 2014** (`St_Francis_EMC_Distinctives.md` L557: W16, 2014-07-01, *"undergraduate, three years before seminary, five before the diaconate"*), i.e. roughly fifteen years younger than this speaker.
2. **Self-description as *"a Reformed guy"*** (s78, [29:10]) and *"at my church on Sunday morning, I preach for 40 minutes"* (s73, [28:44]) — a visiting pastor of a different congregation. ⚠️ **Recorded as the weaker of the two grounds and flagged as such**, since the corpus does hold *"Reformed Catholic"* as one of his own self-labels (`St_Francis_EMC_Distinctives.md` L447); it is ground 1 that does the work.

⭐ **`C` also places two other conference speakers in the third person** — *"as Calvin was saying"* (s253, [44:56]; = Fr Calvin Robinson, whose Perseus session is `T_R7AQQ9nsQ` on the same channel) and *"I think JD mentioned it earlier"* (s230, [42:39]). ⛔ **These are recorded as corroborating that he is a guest among several speakers. They do NOT name him, and no name is inferred.**

⛔⛔⛔ **THE LABEL TRAP IN `File 83`, ENUMERATED SO NO LATER PASS WALKS INTO IT: LABELS `A` AND `B` EACH CARRY BOTH THE MINISTER'S PART AND THE PEOPLE'S.** In the Decalogue the priest says the commandment and the people answer *"Lord, have mercy upon us, and incline our hearts to keep this law."* The recording assigns **both halves to `A`** at s55/s56 ([18:11]/[18:13]) and s52/s53, and then assigns **the priest's own line to `B`** at s58 ([18:18]) with the people's answer back on `A` at s59. During the sermon, six congregational interjections land on `A` (*"Amen"* s?, *"Uh-huh"*, *"Yeah"*, *"Only sheep"* [46:19]). ⛔ **No versicle, response, or short interjection in this file may be attributed to any individual on the strength of its label.**

### `File 84` / `layuF4wDDMI` — Mighty Men of Valour (Evensong and Holy Communion)

| Label | Words | Turns | What the content establishes |
|---|---|---|---|
| `A` | 2,872 | 20 | **The officiant/celebrant — by ROLE, not by name.** *"Evening prayer begins on page 21"* (s0), the opening versicle (s2), the Magnificat and Nunc Dimittis leads, the Decalogue, the collects, the Epistle and Gospel, the offertory announcement (s220), the Exhortation (s231), the Absolution (s248), the Prayer of Consecration (s257 ff.), the administration, the post-communion. ⛔ **NOT a clean single voice** — s149 @10884-10890 [31:34] *"Sword."* is an **audience member answering the preacher's question**, on label `A`. |
| `B` | 546 | 18 | ⛔⛔ **A COLLAPSED LABEL SPANNING AT LEAST TWO SOURCES: a LECTOR and the CONGREGATION.** It reads both lessons in full and solo (s14-s27, [09:24]–[11:02]; s42-s61, [13:05]–[15:21]) **and** carries every congregational response in the file (`Amen` ×9; *"According to thy word"* s65; *"The Lord have mercy upon us"* s85; *"Praise to you, Lord Jesus Christ"* s130; *"And with your spirit"* s256). **Unusable as a single-person warrant.** |
| `C` | 1,048 | 6 | **The conference HOST, who then preaches.** *"First of all, announcements. Welcome to the first Perseus Men's Conference. It's good to see you all here. Unfortunately, uh, Bishop Chad Jones fell ill… He was supposed to be preaching tonight"* (s134-s140, @10132-10437, [30:46]–[31:01]) — **so this sermon is a substitution for the billed preacher.** Then the Ephesians 6 armour-of-God homily, [31:11]–[41:14], closing *"In the name of the Father, and of the Son, and of the Holy Ghost"* (s218). |

⚠️⚠️ **`C` IS THE ONE VOICE IN EITHER FILE WHERE A NAME WOULD BE WORTH HAVING, AND THE FILE DOES NOT SUPPLY ONE.** What the content does establish: he is the host of the conference; he speaks in a clergy register (*"Are we doing Matins daily and Evensong, whether with people at our church or by ourselves or with our families?"*, s207, [39:51]); he closes a sermon with the trinitarian formula; and **he is NOT the celebrant** (`A` and `C` are distinct and both are audible in the same minute). ⛔⛔ **He is NOT identified as Rev. James. The inference from "host of a conference announced on his channel" to "Rev. James" is exactly the channel-ownership inference `260835-22` forbids, and it is not made here.** ⚠️ Recorded for completeness and labelled as **title-derived, not content-derived**: the same channel carries a Perseus 2024 session titled *"Fr James Gadomski"* (`rPg4G3u_l-Q`), which places him at the conference as **a speaker** — it does not place him behind the altar or in this pulpit.

⛔ **`A` and `C` in `File 84` are NOT asserted to be the same people as `A` and `C` in `File 83`.** No cross-file identity claim of any kind is made.

### ⏳ EAR/EYE-CHECKS QUEUED — both BLOCKING for any use of this material as his

- **`E6` (BLOCKING) — `File 83` `egHdlotth9c`, celebrant identity.** Is the officiant Rev. James? Best windows: the announcements at [03:27]–[03:38], the Exhortation at [59:30]–[60:20], the Consecration at [66:50]–[69:48].
- **`E7` (BLOCKING) — `File 84` `layuF4wDDMI`, both the celebrant (`A`) and the host/preacher (`C`).** Best windows: `A` at [04:21] and [41:46]; `C` at [30:47]–[31:32] (announcements, where a host would most naturally be recognisable).

---

## ⛔⛔⛔ The read-aloud attribution layer — required, and it covers nearly everything

⭐ **Applied throughout, as the brief required, and the result is more extreme than the brief anticipated: essentially ALL of the transcribed content in both files is either read-aloud liturgy or a sermon, and there is almost no extemporaneous own-voice remark of any kind.**

**Own-voice, non-liturgical content in the two files, ENUMERATED IN FULL — this is the complete list, not a sample:**

| File | Locator | Content | Speaker |
|---|---|---|---|
| 83 | s5-s6 @181-264, [03:27] | *"The Psalm appointed for this evening is 116. It can be found beginning on page 400."* | `A` (rubric-direction spoken aloud) |
| 83 | s7 (in T000), [~03:45] | *"You'll say it responsibly by action"* (ASR: = "responsively by verse/half-verse") | `A` |
| 83 | within T002, [~08:00] | *"Get ready for lesson"*; *"Next stage, we will bow"* (T006) | `A` |
| 83 | s73-s268, [22:56]–[50:07] | **The whole sermon** | `C` |
| 84 | s0 @0-33, [04:21] | *"Evening prayer begins on page 21."* | `A` |
| 84 | s8 @375-456, [05:18] | *"The song appointed for this evening is the 119th, going from verse 1 to verse 32. This will be said responsively by us."* | `A` |
| 84 | s13, s41, [09:19]/[12:48] | *"You may be seated for the first lesson"* / *"…for the second lesson"* | `A` |
| 84 | s220 @15665-15731, [41:46] | *"So the offertory for this evening is going to be for Papa Francis."* ⚠️ low confidence on the name (`Papa` 0.74 / `Francis` 0.61) — **the beneficiary is NOT established** | `A` |
| 84 | s135-s218, [30:47]–[41:14] | **Announcements + the whole sermon** | `C` |

⛔⛔⛔ **EVERYTHING ELSE IS THE PRAYER BOOK, AND SOME OF IT IS THE `File 69`/`GV-50` TRAP IN ITS PUREST FORM.** Both files contain, in the first person, on labels that a flat read would attribute to a person:

- *"a full, perfect, and sufficient sacrifice, oblation, and satisfaction, for the sins of the whole world"* — `File 83` s343 @26062-26178 [66:50]; `File 84` s257 @19923-20224 [59:59].
- *"we earnestly desire… mercifully to accept this our sacrifice of praise and thanksgiving"* — `File 83` s353 @26804-27134 [68:06]; `File 84` s265 @21787-21879 [62:54].
- *"And here we offer and present unto thee, O Lord, ourselves, our souls and bodies, to be a reasonable, holy [and living] sacrifice"* — `File 83` s355 @27141-27257 [69:23]; `File 84` s268 @22124-22261 [63:16].
- *"these thy holy gifts which we now offer to thee, the memorial [thy Son hath commanded us to make]"* — `File 84` s263 @20923-21408 [62:02].

⛔⛔ **THESE ARE THE 1928 PRAYER OF CONSECRATION'S WORDS, NOT ANYONE'S TESTIMONY. They sit exactly on §9 (Eucharist — Sacrifice) and would read as first-person eucharistic-sacrifice doctrine to any reader who met them without this layer. NOTHING IN EITHER FILE'S LITURGICAL TEXT IS QUOTABLE AS ANY PERSON'S POSITION.** This is the identical hazard `260835-18` recorded for `File 69` and `LS-134` recorded for `File 82`; it recurs here at much greater volume.

---

## ⭐⭐⭐ Task 2 — the primary task: observed ceremonial practice

### (a) INCENSE — the plain answer

⛔⛔⛔ **THERE IS NO AUDIBLE OR VERBAL INDICATION OF INCENSE ANYWHERE IN EITHER RECORDING, IN ANY RENDERING. `incense` IS AN ABSOLUTE ZERO.**

**Tested against the full ASR-mangling battery, in `File 83`'s AssemblyAI rendering, `File 83`'s independent YouTube rendering, and `File 84`'s single rendering — 0 · 0 · 0 on every one of:** `incense` · `incens` · `censer` · `censing` · `cense` · `thurible` · `thurib` · `thurif` · `frankincense` · `smoke` · `smok` · `sweet savour` · `sweet savor` · `odour of` · `fragrance` · `charcoal` · `in sense` · `insense` · `incents` · `sensor` · `censor` · `censure`. A regex sweep for **any token containing** `cens`, `sens`, `thur`, `incen`, `frankin`, `myrrh`, `fragr` or `burn` across the raw YouTube caption stream returned nothing relevant.

**Also absolute zero across all three renderings:** `vestment` · `chasuble` · `cope` · `stole` · `alb` · `surplice` · `cassock` · `biretta` · `maniple` · `candle` · `taper` · `torch` · `acolyte` · `server` · `crucifer` · `procession` · `asperg` · `holy water` · `genuflect` · `sign of the cross` · `elevat` · `sanctus bell` · `chime` · `tabernacle` · `aumbry` · `monstrance` · `pyx`.

⚠️⚠️⚠️ **AND THE ZERO MUST NOT BE READ AS "NO INCENSE WAS USED." IT IS A REAL RESULT AND IT IS A WEAK ONE, FOR THREE REASONS, ALL OF WHICH ARE STATED HERE SO THAT NO LATER PASS OVERREADS IT:**

1. ⭐⭐⭐ **INCENSE IS SILENT.** Censing an altar, the gospel book, the elements or the people produces essentially no transcribable sound. In Anglican ceremonial use it is very commonly done **without any accompanying spoken text at all**. An audio transcript is close to the worst possible instrument for detecting it. ⛔ **The same applies to every other item in the "also absolute zero" list above — vestments, candles, bowing, the sign of the cross, elevation. Their zeros carry no information whatever.** The brief anticipated this for vestments; **it applies identically to incense, and that is the pass's central methodological result.**
2. ⭐⭐⭐ **ONLY ABOUT A QUARTER OF EACH SERVICE IS TRANSCRIBED AT ALL.** Measured from word-level timings: `File 83` carries **5,411 words / 24.0 minutes of word-time in a 94.5-minute recording = 25.4%**; `File 84` carries **4,466 words / 20.5 minutes in 96.4 minutes = 21.3%**. The remainder is sung, chanted, instrumental or silent. ✅ **Independently corroborated from `File 83`'s YouTube captions, which carry explicit `[Music]` markers: 210 of 1,557 caption cues are `[Music]`/`[Applause]`, and they cluster across the WHOLE service EXCEPT minutes 30–50 — which is exactly the sermon.** The Sanctus, Sursum Corda, Gloria in excelsis, Agnus Dei, Prayer of Humble Access, Lord's Prayer, Nunc Dimittis and Te Deum are **all lexically absent from both files** — not because they were omitted, but because they were sung and the ASR dropped them. **A sung censing versicle would have been dropped by exactly the same mechanism.**
3. ⛔⛔ **`File 84` HAS NO SECOND RENDERING.** Confirmed at the meta file: `"youtube_captions": null`. Its `-timestamps.json` was checked and is **the same AssemblyAI pass re-serialised word-by-word, not an independent model output** — so there is no in-file cross-check either. ⚠️ **This is a STANDING LIMITATION on everything mined from `File 84` and is recorded as such at its manifest row and at every finding that cites it.**

### (b) ⚠️⚠️⚠️ THE ONE POSITIVE LEAD, AND IT IS UNRESOLVED — `File 84`'s OPENING VERSICLE

⭐⭐⭐ **`File 84` DOES NOT OPEN WITH THE PRAYER BOOK'S OPENING VERSICLE. IT OPENS WITH WHAT IS, ON ITS FACE, PSALM 141:2 — AND PSALM 141:2 IS THE INCENSE VERSICLE.**

`File 84` s2, **@49-198**, t=285.6-299.6, **[04:45]–[04:59]**, label `A`, immediately after *"Evening prayer begins on page 21"* and immediately before the Gloria Patri — i.e. **in the slot the 1928 book fills with "O Lord, open thou our lips"**:

> *"Let my prayer be set forth in thy sight, **that these cups, from** the lifting up of my hands, may be acceptable unto thee, O Lord, whom thou hast loved."*

**The Coverdale/1928 Psalter text of Psalm 141:2 is:** *"Let my prayer be set forth in thy sight **as the incense**; and let the lifting up of my hands be an evening sacrifice."*

⭐⭐ **The bolded ASR span sits EXACTLY where "as the incense" belongs, and it is the lowest-confidence span in the sentence.** Word-level confidences, read off the primary and reproduced here rather than characterised: `Let`[0.67] `my`[0.93] `prayer`[0.86] `be`[1.00] `set`[0.97] `forth`[1.00] `in`[0.97] `thy`[0.68] `sight,`[0.81] **`that`[0.35] `these`[0.53] `cups,`[0.48] `from`[0.24]** `the`[0.69] `lifting`[0.98] `up`[1.00] `of`[1.00] `my`[0.77] `hands,`[0.88] `may`[0.96] `be`[0.98] `acceptable`[0.19] `unto`[0.70] `thee,`[0.89] `O`[0.99] `Lord,`[0.97] …

⛔⛔ **THIS IS NOT ASSERTED TO BE A CENSING. IT IS ASSERTED TO BE UNRESOLVED, AND THE READING IS NOT CHOSEN.** Three things are established and the fourth is not:

- ✅ **Established:** the versicle is Psalm 141:2. *"Let my prayer be set forth in thy sight"*, *"the lifting up of my hands"* are high-confidence and verbatim.
- ✅ **Established:** Psalm 141 is **not** part of the 1928 Order for Daily Evening Prayer. Its use as an opening versicle is a **ceremonial import**, whatever was or was not burning — and its traditional ceremonial home is the censing of the altar at Vespers/Solemn Evensong.
- ✅ **Established:** `File 83` does **not** do this. Its independent YouTube rendering carries *"oh Lord open th our lips"* at **[03:09]** — the standard Prayer Book opening. ⭐ **The two services differ at exactly this point**, which is a real, cross-checked difference and not an ASR artefact.
- ⛔ **NOT established:** whether the word *"incense"* was spoken. The ASR does not resolve it, and `File 84` **has no second rendering to appeal to** — the standing limitation lands precisely on the one span in this pass where it matters most.

⏳⏳⏳ **EAR-CHECK `E8`, THE HIGHEST-VALUE CHECK IN THIS PASS AND THE CHEAPEST: `layuF4wDDMI` at [04:45]–[04:59]. Fourteen seconds. Does the celebrant say "as the incense"?**

### (c) ⭐ WHERE TO LOOK IF THE QUESTION IS SETTLED VISUALLY — the untranscribed windows

⭐⭐ **The brief is right that this is a video question, and JD has the video. These are the windows the audio cannot see into, computed from word-level gaps ≥ 90 s, and they are where ceremonial action would sit.**

**`File 83` / `egHdlotth9c` — 4 windows, 11.9 min total:** **00:00–03:11** (3.2 min — *entrance/procession; the classic opening-censing window*) · 53:02–55:16 (2.2 min) · **77:46–79:41** (1.9 min — *post-consecration/communion*) · 90:01–94:32 (4.5 min, tail).

**`File 84` / `layuF4wDDMI` — 10 windows, 25.7 min total:** **00:00–04:21** (4.4 min — *entrance*) · 15:22–17:22 (2.0) · **43:09–45:17** (2.1) and **46:54–50:22** (3.5) — ⭐ *both immediately after the offertory announcement at [41:46]; the offertory censing window* · **58:13–59:59** (1.8) — ⭐⭐ *sits between the Sursum Corda dialogue ([58:09]–[58:13]) and the first word of the Prayer of Consecration ([59:59]); this is where the Sanctus is sung and where the censing of the oblations and altar occurs in ceremonial use* · 69:08–70:45 (1.6) · 72:22–74:04 (1.7) · 79:34–81:33 (2.0) · 86:40–88:47 (2.1) · 91:52–96:25 (4.5, tail).

### (d) ⭐⭐ THE RITE ITSELF — what the spoken text DOES establish

Everything in this section is derived from read-aloud text and is a fact about **the service**, not about any person.

**Both services are the same compound shape: Evening Prayer running straight into Holy Communion**, matching both titles. Both are **overwhelmingly sung** (see the `[Music]` evidence above); the sermon is the only substantial spoken block in each.

**The book.** `File 84` s0 [04:21]: *"Evening prayer begins on page 21."* ✅ **The Order for Daily Evening Prayer begins on page 21 of the 1928 American Book of Common Prayer.** ⚠️ **`File 83`'s counterpart locator does NOT reconcile and is reported unresolved rather than forced:** s5-s6 [03:27]–[03:38], *"The Psalm appointed for this evening is 116. It can be found beginning on page 400"* — Psalm 116 sits at roughly p. 484 in the standard 1928 Psalter, and at roughly p. 440 in the 2019 ACNA Psalter. **Neither matches 400.** `400` carries ASR confidence 0.75. ⛔ **Flagged, not resolved; no book is inferred for `File 83` from it.**

**The Prayer of Consecration is the 1928 American shape, and this is the firmest structural result in the pass.** `File 84` s257–s268 ([59:59]–[63:16]) runs, in order: the preface (*"who made thereby his one oblation of himself… a full, perfect, and sufficient sacrifice, oblation and satisfaction, for the sins of the whole world"*) → **the Words of Institution** → ⭐ **the Oblation** (*"Wherefore, O Lord… we thy holy servants do celebrate and appear before thy divine presence with these thy holy gifts which we now offer to thee, the memorial of thy Son"*, s263 @20923-21408) → ⭐ **the Invocation** (*"…bless and sanctify with thy word… these thy gifts and creatures of bread and wine"*) → the sacrifice of praise and thanksgiving → *"And here we offer and present to thee, O Lord, ourselves, our souls and bodies"* (s268 @22124-22261) → *"although we are [unworthy]… yet we beseech thee to accept this our [bounden duty and service]"*. `File 83` s343–s359 ([66:50]–[69:48]) carries the same elements in the same order. ✅ **Retaining the Oblation and Invocation AFTER the Institution EXCLUDES the 1662 rite decisively.** ⛔ **It does NOT distinguish the 1928 from the 2019 ACNA Anglican Standard Text, which inherits the same shape — stated plainly rather than glossed, and no choice between them is made on this evidence.**

**Traditional elements retained in both, each of which is optional or commonly omitted:** the **full Decalogue** with the people's response to each commandment; the **long Exhortation** (*"Dearly beloved in the Lord, ye who mind to come to the Holy Communion…"*, `File 83` s320 @23686-23963 [59:30]; `File 84` s231 @16972-17240 [53:09]); the **Comfortable Words**; the **Prayer for the Whole State of Christ's Church** (`File 83` s315 @23251-23321 [50:50] — ⚠️ the ASR renders it *"the whole state of West Virginia"*, a mangling, flagged here so it is not later mistaken for a local intercession).

⭐ **The fraction anthem is an EXPANDED Pascha Nostrum in both, not the bare 1662/1928 form.** `File 84` s272 @22478-22640 [64:14]: *"Christ our Passover Lamb, who was offered up for us once for all, when he bore our sins on his body upon the cross. For he is the very Lamb of God that takes away the sins of the world. Therefore let us keep the [feast]. Alleluia."* `File 83` s361 @27826-28004 [71:07] carries the same expanded form. ⚠️ **In both, the ASR corrupts the closing clause** — *"a joyful and holy feast of Easter"* (`File 83`) and *"the joyous day of Pentecost"* (`File 84`), at a conference held in October; **both are ASR corruptions of "let us keep the feast" and neither is a real seasonal reference.** ⭐⭐ **This expanded form is the one printed in the 2019 BCP and in Missal-derived books, not in the 1928 — i.e. a supplement to a 1928-shaped rite.**

⭐⭐ **`File 84` commemorates a saint the 1928 kalendar does not have.** s103 @7246-7598 [22:49]: *"Almighty God, who hast called us… and hast compassed us about with so great a cloud of witnesses, grant that we, encouraged by the good examples of thy saints, and especially thy servant **Saint Raphael**, may persevere in running the race…"* ⚠️ **`Saint` 0.53 / `Raphael` 0.73 — moderate confidence, flagged.** ⭐ **If correct it is internally consistent and non-trivial: the video's `release_date` is 2024-10-24, and 24 October is St Raphael the Archangel in the pre-1969 Roman kalendar — a feast absent from the 1928 BCP.** ⛔ **Recorded as a lead with its confidence stated, not as an established datum. Ear-check `E9`, non-blocking.**

### (e) ⭐ Element/circumstance and ceremonial warrant *as practiced*

⛔⛔ **Nothing in either recording argues, mentions, or alludes to the element/circumstance distinction, ceremonial warrant, Article 34, the regulative or normative principle, or adiaphora.** Confirmed zeros across all three renderings on: `element` · `circumstance` · `indifferent` · `things indifferent` · `adiaphora` · `ceremony` · `ceremonies` · `rite and ceremon` · `edification` · `decency` · `comeliness` · `Article 34` · `Article XXXIV` · `regulative` · `normative`.

⭐ **What the material contributes to that question is therefore of one kind only, and it is worth stating exactly:** it is an instance of the **practice** the argument is about — a 1928-shaped rite carrying a series of accretions (an expanded fraction anthem, a non-1928 saint's collect, and in `File 84` a non-Prayer-Book opening versicle) sung throughout — **without a word of justification offered for any of them.** ⚠️ **Whose practice it is remains open, so it cannot yet be set against `LS-134`'s own description of inserting *"a lot of the improvements… into the 1928, usually basically using the American Missal."* The resemblance is recorded and the inference is NOT drawn.**

---

## Task 3 — mining the spoken commentary against the standing questions

⛔⛔ **NOTHING WAS MINED AS ANY PERSON'S POSITION, because attribution is open in both files.** The sweep below was run in full anyway, so that the absences are on record and no later pass re-runs it.

⭐ **The result is a near-total absence, and the reason is structural rather than accidental:** the only own-voice non-liturgical content in either file is two sermons by two unidentified preachers, one on Matthew 25 (sheep and goats) and one on Ephesians 6 (the armour of God). **Neither sermon touches the corpus's live questions at any point.**

| Standing question | Result | Search terms, all across `File 83` AAI + `File 83` YouTube + `File 84` |
|---|---|---|
| **`DQ-24`/`DQ-25`/`DQ-26` reception criterion** | ⛔ **ABSOLUTE ZERO** | `consensus` · `church fathers` · `the fathers` · `patristic` · `antiquity` · `undivided` · `ecumenical` · `universally` · `received by` · `reception` · `always, everywhere` · `Vincent` · `Vincentian` · `catholic faith` · `tradition` · `council` · `canon` · `primitive`. *(Only `authority` is non-zero — 1·3, inside the sermon's *"no authority over you spiritually or temporally"* about modern monarchs. Not load-bearing.)* |
| **Element / circumstance** | ⛔ **ABSOLUTE ZERO** | See §(e) above — sixteen terms, all zero. *(`order` is non-zero at 2·1·6 and every hit is ordinary English.)* |
| **Malachi 1:11, in any form** | ⛔ **ABSOLUTE ZERO** | `Malachi` · `pure offering` · `from the rising of the sun` · `incense shall be offered` · `great among the heathen` · `every place`. |
| **Eucharistic sacrifice** | ⚠️ **PRESENT BUT ENTIRELY READ-ALOUD** | `sacrifice` 3·4·0, `oblation` 1·2·0, `memorial` 0·1·0, `offer` 6·5·13 — ⛔ **every single occurrence is inside the Prayer of Consecration or the fraction anthem.** Enumerated in the read-aloud table above. **NOT quotable as anyone's position.** |
| **Eucharistic presence** | ⛔ **ZERO as doctrine** | `transubstant` · `real present` · `reserved sacrament` · `spiritual food` all zero. `presence` 0·1·0 is *"appear before thy divine presence"* (Prayer of Consecration); `propitiat` 0·1·0 is the Comfortable Words quoting 1 John 2:2. **Both read-aloud.** |

⭐ **One genuinely new datum does come out of the sweep, and it is a datum about the CONFERENCE, not about doctrine:** `File 84` s134-s140 @10132-10437 [30:46]–[31:01] establishes that **Bishop Chad Jones was the billed preacher for that evening and withdrew through illness**, and that the sermon delivered instead was a substitution by the host. ⭐ Recorded because it bears on how the two sermons should be weighted by anyone reading this material later — **neither preacher is the one the conference programmed.**

---

## Numbers minted

| Number | Anchor | One line |
|---|---|---|
| **`LS-138`** | attribution-risk documentation | Both liturgies **ATTRIBUTION OPEN**; `File 83`'s preacher positively eliminated as Rev. James; the label-collapse traps and the full read-aloud layer for both files. |
| **`LS-139`** | §10 Eucharistic Ceremonial *(secondary: §0 standing instruction)* | **Incense: absolute zero, and why the zero is weak.** The Psalm 141:2 low-confidence slot in `File 84`. The blocked `LS-123` test. |
| **`LS-140`** | §14 Liturgy, Prayer Book, Calendar, Fasts *(secondary: §10)* | **The rite as observed** — sung throughout; 1928-shaped Consecration with Oblation and Invocation after Institution; retained Decalogue and long Exhortation; expanded fraction anthem; the `File 84`/`File 83` opening divergence; the unreconciled `page 400`. |
| **`LS-141`** | §13 Worship Theology *(secondary: batch documentation)* | **The standing-questions term scan** — the confirmed zeros with every search term listed, and the structural reason for them. |

⛔ **`File 83`** = `egHdlotth9c`, **`File 84`** = `layuF4wDDMI`. Next free `File` is **`File 85`**; next free `LS` is **`LS-142`**.

✅ **All 18 meta-recorded `sha256`/byte values across the two artifact sets verified against disk this pass — 18/18 exact, zero divergence.**

✅ **Every byte range cited anywhere in this pass was re-extracted from the transcript file at its logged offset and compared to the quoted text.** Final state: **`LS-138`…`LS-141` — 62 ranges, 58 exact single-sentence spans re-extracted and matched, 4 contiguous multi-sentence spans, 0 unresolved. `SRC_Manifest.md`'s new section — 9 ranges, 0 unresolved. This close-out — 23 ranges, 0 unresolved.** *(⚠️ `s`-numbers are ZERO-BASED indices into the `-sentences.json`; byte ranges are into the `-transcript.txt` and were computed programmatically this pass, not copied from any brief.)*

⭐⭐ **THE VERIFICATION CAUGHT A REAL DEFECT AND IT IS REPORTED RATHER THAN QUIETLY FIXED, because it is the kind that would have propagated.** The announcement block in `File 84` was first cited as **`s135-s138` @10161-10285** in three places. **Both halves were wrong and in opposite directions:** the byte range `@10161-10285` actually spans `s135`–`s137` and stops at *"…Bishop Chad Jones fell ill."*, while `s135-s138` actually runs to `@10318`; and the quoted text attached to it included *"He was supposed to be preaching tonight, but he will not be here for preaching"*, **which is `s139` @10319-10398 and sat OUTSIDE the cited range entirely.** ⛔ **A quotation was therefore carried on an offset that does not contain it — exactly the defect class `260835-19`/`260835-29` had to repair retrospectively for `DQ-24`.** ✅ **Corrected before commit in all three places to `s134-s140` @10132-10437 [30:46]–[31:01], with `s137` and `s139` given their own individual ranges where they are quoted individually. Caught only because the check re-extracted rather than re-read.**

---

## Duplicate-registration check (ORCHESTRATION §8, video-ID reconciliation)

✅ **Run before any edit, on video ID, per the `260835-37` standing instruction.** `egHdlotth9c` and `layuF4wDDMI` were each checked against every backtick-enclosed 11-character token in `SRC_Manifest.md`: **neither occurs there.** Both appear only in `SRC_Channel_Inventory.md` (their `INCLUDE — T2` rows), `PROJECT_STATE.md`, and three `passes/` artifacts — **all triage and pull-list material, no registration.** A title-phrase sweep on *"Perseus"* returned the same. ✅ **Not previously registered; not previously mined. The brief's unmined premise HOLDS for both.**

---

## Files touched

| File | What changed |
|---|---|
| `SRC_Manifest.md` | New section: `File 83`/`File 84` registered with hashes, byte counts, speaker attribution (ATTRIBUTION OPEN, from content), source-video metadata, and `File 84`'s no-second-rendering standing limitation. Stamp bumped. |
| `St_Francis_EMC_Distinctives.md` | `LS-138`…`LS-141` minted with byte-range citations; changelog entry; §15 not touched. Stamp bumped. |
| `SRC_Channel_Inventory.md` | The two `egHdlotth9c`/`layuF4wDDMI` rows set to `INGESTED` with File numbers and finding range, as dated reclassifications retaining the prior verdict verbatim. Stamp bumped. |
| `SRC_Coverage_Register.md` | New coverage entry for the pair. Stamp bumped. |
| `PROJECT_STATE.md` | Gate block + pass note + §4 registry rows. Stamp bumped. |
| `passes/260835-38_…_close-out.md` | This file (new). |

## ⛔ NOT DONE, DELIBERATELY

⛔ `Incense_Conversational_Outline.md` **NOT touched.** ⛔ `RJ_Incense_Analysis.md` **NOT touched** — §4.6/§4.8/§4.10 remain falsified-pending-revision, and §2.2's `LS-123` cross-reference is **not** amended by this pass even though `LS-139` bears on it. ⛔ **Nothing drafted, altered or posted to Rev. James.** ⛔ `LS-123`, `LS-127`, `LS-133`, `LS-134`, `IP-12`, `IP-52`, `IP-69` **NOT edited, superseded or re-pointed.** ⛔ **`DQ-9` NOT moved; `DQ-24`/`DQ-25`/`DQ-26` NOT moved** (the reception criterion is an absolute zero here). ⛔ **No gate moved, no `VP-` pair or `DELTA` created, no registered byte offset or hash altered, no `C10` §15 credit claimed.** ⛔ **The `260835-37` open-items list was NOT worked** — out of scope for this brief.
