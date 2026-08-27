# 260835-11 — RC/BP RETRO-VERIFICATION AGAINST THE RECOVERED TRANSCRIPTS, AND THE PAPACY-DEBATE SPEAKER MAPPING

**Pass stamp:** `260835-11` · **Date:** 2026-08-27 · **Type:** retro-registration + verification. Corrects and registers.

---

## 0. GATE

| Item | Value |
|---|---|
| `git rev-parse HEAD` | **`07031e718559f522d6c5fc6c731174eb5ce9280d`** · branch `main` |
| `git --no-optional-locks status --short` **before first edit** | **EMPTY** (exit 0). Captured directly, not reconstructed. |
| Lock handling | The `260835-3` FUSE-mount `index.lock` diagnosis was **applied, not re-derived**. Every git read this pass used `git --no-optional-locks`. No lock created, none removed, no `rm` attempted. |
| Validator BEFORE | **`82 ok · 9 warnings · 0 errors`** |
| `PROJECT_STATE.md`'s own stamp at gate | **`260835-10`** |
| Next-free pass stamp | **`260835-11`** — derived fresh (below) |
| Next-free `File` number | **`File 47`** — derived fresh (below) |

### 0.1 All nine firing validator codes, recorded individually

1. `[C1]` `src/SRC_Discord_RPW.md`: 2 relative timestamp(s) outside message headers (`'Yesterday at …'`).
2. `[C3]` `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md`: no parseable `Last updated` stamp; registry says `260832-2`.
3. `[C3]` `tools/transcribe_yt.py`: no parseable `Last updated` stamp; registry says `260833-7`.
4. `[C4]` `St_Francis_EMC_Distinctives.md`: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby.
5. `[C5]` `RJ_Final_Question_List.md`: 17 volatile-state assertions.
6. `[C5]` `RJ_Incense_Analysis.md`: 9 volatile-state assertions.
7. `[C5]` `St_Francis_EMC_Distinctives.md`: 7 volatile-state assertions.
8. `[C10]` §15's newest `LS` citation is 8 findings behind the ledger (`LS-120` vs `LS-128`).
9. `[C11]` outline last checked against `IP-97` (`260833-5`); the `IP` ledger now runs to `IP-108`; 11 findings unreviewed.

**Unchanged from the `260835-10` gate. None of this pass's business; none touched.**

### 0.2 Stamp derivation — showing the work, because the naive grep lies here

`grep -rhoE '\b26[0-9]{4}-[0-9]+\b'` across all `*.md` / `*.py` returns apparent hits for `260835-11` and `260835-12`. **Every one was opened and read.** All are prose *inside earlier passes' own close-outs, describing searches for their own absence*:

- `passes/260835-9_..._raw-session-output.md:19` — a literal shell command line, `grep -rln "260835-9\|260835-10\|260835-11\|260836-"`.
- `passes/260835-8_..._close-out.md:20,262` · `passes/260835-9_..._close-out.md:3` · `passes/260835-10_..._close-out.md:11` · `PROJECT_STATE.md:5,9` — all of the form *"verified: no `260835-8`…`260835-12` exists anywhere."*

**Highest REAL stamp = `260835-10`** (`PROJECT_STATE.md`'s own `Last updated` line, and `passes/260835-10_never-triaged-sweep_close-out.md`). **This pass is `260835-11`.**

### 0.3 `File` number derivation, re-derived fresh

Highest **registered** File in `SRC_Manifest.md` = **File 46** (`a202.txt`). Every repo-wide occurrence of `File 47` was opened: all are *next-free* assertions (`260834-9`'s registration close, `260835-1`/`-2`/`-3`/`-4`/`-6`'s next-free lines, `PROJECT_STATE.md` §4). **`File 47` was free. This pass consumes `File 47`…`File 55` — nine File numbers, and nothing else.**

⛔⛔ **NO FINDING, AND NO `LS`, `IP`, `RV`, `DQ`, `BLOG`, `POD`, `VP`, `DELTA`, `EXT`, `W`, `GV`, `RC` OR `BP` NUMBER WAS MINTED.** Next-free values re-derived and unchanged: `DQ-25`, `IP-109`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EXT-4`, `W47`.

---

## 1. WHAT WAS ACTUALLY IN `redownloads/`, AND A CORRECTION TO THE BRIEF'S ARITHMETIC — WHICH HOLDS

The brief says *"Nine recovery transcripts now sit in `redownloads/` (eight from the recovery pull, plus a corrected re-run of one)."* **Confirmed exactly**, and the check is worth recording because the directory contains twelve transcript sets, not nine.

Three sets — `Kennedy-Assurance-*`, `HolyOrders-Debate-ApostolicaeCurae-*`, `HolyOrders-Debate-Minton-*` — carry `generated_utc` of **2026-08-26T05:20–05:26Z** and belong to the **earlier** pull already consumed by `260835-4` (Kennedy) and `260835-7` (the two Holy Orders debates). They are **not** part of this recovery pull and are **not** registered by this pass.

The recovery pull proper is the eight sets stamped `2026-08-27T02:02–02:15Z`, plus the corrected re-run stamped `2026-08-27T13:48:14Z`. **8 + 1 = 9. The brief is exact.**

And the sub-count holds: 8 recordings − 1 debate = **7 non-debate recordings**, which is precisely the scope of JD's manual single-speaker warrant. ✅

---

## 2. TASK 1 — REGISTRATION. `File 47`…`File 55`

⭐ **Every hash and byte count below was computed fresh this pass** with `hashlib.sha256` over the raw bytes of the `-transcript.txt`, **not copied** from any `-meta.json` or prior report. Where a `-meta.json` also carries a hash it is of the **audio**, a different object, and is recorded separately. **No collision with any previously registered hash; none of the nine had ever been registered.**

⛔ **Convention, stated so it is not guessed:** the **raw** hash of the `-transcript.txt` is the value of record, on the Files 8-9 / Files 40-46 precedent, because every byte range this pass registers resolves against the raw bytes of that file.

| File | Filename | SHA-256 (raw bytes, `-transcript.txt`) | Bytes | Video ID | Title | Upload | Dur (s) | Speakers detected | Batch |
|---|---|---|---|---|---|---|---|---|---|
| **File 47** | `GatewayToCatholicismResponse-transcript.txt` | `8099c16e9675c12c1d5da005ad2e32874f97190dd2c7b74fa2197730c1bbe1b4` | 51,968 | `KsLqJIPrpCg` | Response to "Why is Anglicanism a Gateway to (Roman) Catholicism?" | **2020-04-30** | 3389 | `['A']` | **`RC-1`** |
| **File 48** | `PapacyDebateThoughts-Edmonds-transcript.txt` | `8938f3aed7e0200cfafc9f02d95d20aefe2c0bfa891566942bd721835e804025` | 8,393 | `sO-_EJbq_oQ` | Thoughts on the Papacy Debate with Noah Edmonds | **2020-06-04** | 593 | `['A']` | **`RC-2`** |
| **File 49** | `TeachingTheMass-transcript.txt` | `b74925bdae5fd09cd1e801e7c1f5387565327c923b3e507c24ffa0a52f9a519e` | 83,380 | `Nxx1QEhvIB0` | Teaching the Mass | **2025-09-22** | 5685 | `['A']` ⚠️ see §2.2 | **`RC-3`** |
| **File 50** | `Apocrypha-transcript.txt` | `a0cffb080901fb2d184ad22f543a8e6f21bd88e6fcd68488f42701544f8ed458` | 25,645 | `s2-jIFFBiJg` | What About the Apocrypha? (Anglican Perspectives) | **2020-05-22** | 1790 | `['A']` | **`RC-4`** |
| **File 51** | `BadArgumentsRomanCatholicism-transcript.txt` | `410fc7ca49904f658b43d47386038ab9aa955b8769e209fca5a1bcd5540ef626` | 23,834 | `wvpJL0DzBto` | Bad Arguments for Roman Catholicism | **2021-01-24** | 1566 | `['A']` | **`RC-5`** |
| **File 52** ⭐ | `PapacyDebate-ScriptureCouncils-3spk-transcript.txt` | `05ba228fc833bc7506c097e6da12fe5da2a76607b2c7c65df3976c4939757175` | 81,288 | `auiLAv8BYpk` | Debate on the Papacy: Scripture and the Seven Ecumenical Councils (Deacon James and Noah Edmonds) | **2020-06-02** | 4567 | `['A','B','C']` | **`RC-7` — AUTHORITATIVE RENDERING** |
| **File 53** ⛔⛔ | `PapacyDebate-ScriptureCouncils-transcript.txt` | `39918735387250b2e3b44034619dfbf9254e600cd1bd54463685610085da31b0` | 81,261 | `auiLAv8BYpk` | *(same video)* | 2020-06-02 | 4567 | `['A','B']` | ⛔⛔ **DEFECTIVE RENDERING — NON-QUOTABLE. PRESERVED AS EVIDENCE, NOT AS A SOURCE.** |
| **File 54** | `SacramentValidity-transcript.txt` | `2dd73fa0471592f6d78ed4bf25b7881966da74bff2775ee6c997d40dfd9c4af5` | 8,309 | `p-jeXC7sokY` | What Makes a Sacrament Valid? | **2025-10-17** | 689 | `['A']` | **`BP-Sac`** (`BP-11`…`BP-18`) |
| **File 55** | `2019BCP-MorningPrayer-transcript.txt` | `2ed9b590dbb07e8e586324e379e2ec366d2a8c8ad00e2d23018afc4fa076cf1a` | 26,483 | `xySXFYRQ9tI` | How to Use the Book of Common Prayer for Morning Prayer | **2020-03-28** | 1753 | `['A']` | ⛔ **NONE — REGISTERED, UNMINED** |

**Common provenance for all nine:** channel *Barely Protestant (Fr James)*, `UCWrx0o3G0laSrpOMuApxTMg`. ASR: AssemblyAI, `speech_models` `universal-3-5-pro` / `universal-2`, `language_code` `en`, `disfluencies: true`, `speaker_labels: true`, 61 keyterms from `asr_keyterms_A101.md`. Audio via `yt-dlp 2026.08.19`, 64k / 16 kHz / mono. Each set also carries a `-youtube.srt` — **YouTube's own captions, an INDEPENDENT second rendering**, used throughout this pass to cross-check wording. ⛔ **Transcripts held OUTSIDE the repo**, at `~/EMC/original transcripts/video transcripts/redownloads/`.

⭐⭐ **`File 52` AND `File 53` SHARE ONE AUDIO SHA-256 — `7967806870b348c8acf53484baf4f4acbb33ae1dacb88bc48eca2435976b3078` — AND THAT IS THE POINT.** Identical audio, two AssemblyAI passes differing only in `speakers_expected` (absent → auto-detect, vs `3`). The 27-byte text difference and the entirely different speaker partition are therefore attributable to diarization alone, not to a different recording. **This is the evidence that auto-detect undercounted, and it is why `File 53` is registered rather than deleted.**

### 2.1 ⭐ JD's human-verification warrant — recorded, dated, and SCOPED

⭐⭐ **WARRANT (JD, 2026-08-27).** JD has **manually verified by ear** that the **seven non-debate recordings of this recovery pull** — `File 47`, `File 48`, `File 49`, `File 50`, `File 51`, `File 54`, `File 55` — are **single-speaker, Rev. James only**.

⭐ **This is recorded ALONGSIDE, not instead of, the machine result.** AssemblyAI auto-detect independently returned `speakers_detected: ['A']` for all seven. **Two independent methods agreeing is stronger evidence than either alone**, and the pairing is the reason this warrant is worth more than the `a105` warrant it follows.

⛔⛔ **SCOPE LIMIT, BINDING, ON THE `a105` PRECEDENT (`260835-3`, where a similar warrant was correctly confined to a single file).** This warrant covers **these seven recordings and nothing else**. It does **NOT** generalise:

- ⛔ **NOT** to `File 52` or `File 53` — three-voice debate, expressly outside the warrant.
- ⛔ **NOT** to any other file in the corpus, registered or unregistered.
- ⛔ **NOT** to any future recovery pull.
- ⛔ **NOT** to any other recording on the same channel, however similar in format.

### 2.2 ⚠️⚠️ AND THE WARRANT IS CONTRADICTED FOR `File 49` — FLAGGED, NOT RESOLVED

⛔⛔ **`File 49` (`TeachingTheMass`) IS SINGLE-*LABEL* BUT NOT SINGLE-*VOICE*.** All 1,156 sentences carry label `A` and `meta.json` reads `speakers_detected: ['A']` — so the machine result and JD's warrant agree, **and both are wrong about this file.** The recording is a live parish class, and diarization collapsed attendee turns into `A`. Confirmed attendee utterances, by byte offset:

| Bytes | Time | Utterance |
|---|---|---|
| 18,062–18,084 | 0:21:36.830 | attendee question (aumbry) |
| 21,745–21,751 | 0:25:37.540 | attendee question (aumbry) |
| 15,502 | 0:18:42 | *"Church of Scotland."* |
| 42,090 | 0:48:16 | *"14th."* |
| 60,150–60,212 | 1:08:36.207 | attendee |
| 77,491–77,543 | 1:28:07.205 | attendee |
| 78,681–78,751 | 1:29:22.543 | attendee |
| 80,841–80,875 | 1:31:50.070 | attendee |
| **83,366–83,380** | **1:34:39.996** | ⛔ **`"Thanks, Frank."` — the FINAL LINE OF THE FILE, and it is not Rev. James's.** |

⭐ **The practical exposure is currently nil and that is stated plainly: no existing `RC3` finding rests on an attendee turn** — every `RC3` byte range registered in §4 was checked against this list and none intersects it. ⛔⛔ **But `File 49` MUST NOT BE USED AS A SPEAKER WARRANT**, and the seven-file warrant above must be read as covering six files cleanly and `File 49` with this exception noted.

⛔ **NOT RESOLVED. This is JD's to rule on** — whether to narrow the warrant to six files, or to keep seven with the exception recorded. The warrant text above is left exactly as JD gave it, with this note beside it, per the never-alter rule.

---

## 3. TASK 5 — THE PAPACY DEBATE. MAPPING, DIFF, AND THE `RC-7` CROSS-CHECK

### 3.1 ⭐⭐⭐ THE MAPPING, DERIVED FROM THE TIMESTAMPS AS INSTRUCTED, AND LOCKED AT SIX INDEPENDENT ANCHORS

> ## **`A` = Evan Minton (moderator) · `B` = Noah Edmonds · `C` = Rev. James Gadomski**

⛔ **The speaker stats do NOT settle this and were not used to settle it.** `B` = 34.1 min / 324 sentences; `C` = 30.8 min / 341 sentences. **Noah speaks LONGER than Rev. James**, so the intuitive "it's his channel, he speaks most" heuristic would have produced the WRONG answer. The mapping below is derived from timestamps and content only.

| # | Anchor | Evidence | Yields |
|---|---|---|---|
| 1 | **`A` = Evan** | `A` opens 0:03–1:09: *"…uh I'm your moderator tonight. My name is Evan Minton. I run a blog and podcast over at www.cerebralfaith.net."* **24 turns, 78 sentences, 5.1 min**, clustering at 0–1.2, ~20, ~36, ~46, ~62, 75–76 min — **matching the brief's stated profile exactly, independently re-derived.** | `A` = Evan ✅ |
| 2 | **The 1:15 anchor** (brief's own) | Evan's cue *"So Noah, why don't you just go right ahead and give us your opening"* is followed immediately by the first opening statement, **1:15 → 20:00**, arguing that *"papal infallibility and papal jurisdiction are evident doctrines"* — the Roman Catholic affirmative. Speaker: **`B`**. | `B` = Noah ✅ |
| 3 | **The 20:52 anchor** (brief's own) | After Evan's transition at 20:01–20:50, the second opening statement runs **20:50 → 35:47**. Speaker: **`C`**. | `C` = Rev. James ✅ |
| 4 | **Direct address, both ways** | `C` @20:50: *"thank you very much, **Noah**, for a wonderful 20 minutes"* → `C` ≠ Noah. `B` @36:42: *"it is always great to get to debate with **James**"* → `B` ≠ James. `B` @67:48 closing: *"just ending by thanking **James**."* | Confirms 2 & 3 ✅ |
| 5 | **Named floor handoffs** ⭐ | Evan @41:39: *"Okay, so, um, **James**, it is now your turn."* → next speaker is **`C`**. Evan @67:45: *"Okay, and **Noah**, now it is your turn."* → next speaker is **`B`**. | Independent lock ✅ |
| 6 | **The corpus's own `RC-7` finding** ⭐⭐ | `C` @30:28: *"Saint Peter, as well as his successors in Rome, can be seen and have been seen as the first among equals, **which is the position I hold to**, as well as the position of the Eastern Orthodox."* This is **verbatim the sentence `St_Francis_EMC_Distinctives.md` L693 already attributes to Rev. James as `RC7-1`/`RC7-8`.** | The corpus confirms `C` = Rev. James ✅ |

⭐ **Evan introduces the debaters *"Noah Edmonds of The Eccentric Naturalist and James Gadomski of Barely Protestant"* — Noah first — independently corroborating the opening-statement order, exactly as the brief says.**

### 3.2 ⚠️ ONE BRIEF ANCHOR NEEDS A PRECISION NOTE — REPORTED, NOT GLOSSED

The brief states: *"at 61:43–62:37 the speaker is Rev. James, with Noah also speaking in that window."*

**What the tape shows.** In the strict span 61:47–62:33, the speaker is **`B` = Noah** (*"I don't have a good answer to that… I don't know enough about this council in particular"*), and **`C` = Rev. James** enters at **62:37**, on the boundary. So both speak in the window, as the brief says, but Noah holds most of it and Rev. James enters at its close.

⭐ **This does not unsettle the mapping — it independently confirms it, on content.** Widening to 61:01 shows the exchange whole: `C` is the one **pressing** (*"why did they see themselves as having the right to judge… the letter of Pope Celestine… **If he's infallible. Why?**"*, 61:15–61:32) and again at 62:37 (*"the problem with that due process concept is that it would presuppose that the ecumenical council has the ability to override the Pope"*). **That is the negative case against papal infallibility — Rev. James's side by the debate's own structure.** `B` is the one *defending* the Pope's authority while conceding he doesn't know the council. **The argument's direction fixes the speakers independently of any label.**

⛔ **No label mapping was carried into this recording from `MLCh-d15F_o` or `7_egBtP9H1I`**, per the `260835-7` standing hazard. This mapping was derived from `auiLAv8BYpk`'s own self-identifications, floor handoffs and argument direction, from scratch.

### 3.3 ⭐ THE DIFF — WHERE THE TWO RENDERINGS DISAGREE

Alignment method: 743 (3spk) vs 747 (2spk) sentences, matched on sentence-midpoint containment. **All 743 aligned.**

#### The structural result — the whole defect in one table

| 3-speaker (File 52) | → 2-speaker `A` | → 2-speaker `B` |
|---|---|---|
| `A` = **Evan (moderator)** | **77** | 1 |
| `B` = **Noah Edmonds** | **321** | 3 |
| `C` = **Rev. James** | 4 | **337** |

> ## ⛔⛔⛔ **2-speaker `A` = EVAN + NOAH MERGED. 2-speaker `B` = REV. JAMES.**
>
> The moderator was folded into **Noah's** side, not Rev. James's. 2spk `A` = 402 sentences / 39.3 min = exactly Evan (78 / 5.1) + Noah (324 / 34.1). 2spk `B` = 345 / 30.7 min ≈ Rev. James (341 / 30.8).

#### ⭐⭐ THE CONSEQUENCE FOR `RC-7`, WHICH IS THE GOOD NEWS AND IS STATED PLAINLY

The `GV-50` error class is *a moderator's words attributed to a debater*. Here the moderator was merged into **Noah**. `RC-7` logs **only Rev. James's turns** (`St_Francis_EMC_Distinctives.md` L363). **So the contaminated label is not the one `RC-7` reads.** The exposure is confined to the four sentences the defective rendering wrongly places inside Rev. James's label — and **all four are single-word backchannels**:

| Time | TRUE speaker | 2spk said | Text |
|---|---|---|---|
| 20:10 | Noah | `B` (Rev. James) | *"No."* |
| 30:26 | Noah | `B` (Rev. James) | *"Okay."* |
| 55:46 | Noah | `B` (Rev. James) | *"Yeah."* |
| 76:03 | **Evan** | `B` (Rev. James) | *"Bye-bye."* |

And four sentences truly Rev. James's that the defective rendering gave away to `A` — also all backchannels: *"Uh-huh."* (10:21), *"Um, all right."* (20:56), *"Nice pun."* (30:27), *"Yeah."* (56:39).

> ✅ **ZERO SUBSTANTIVE CONTENT IS MISATTRIBUTED AT THE REV. JAMES BOUNDARY IN EITHER DIRECTION. `RC-7` DID NOT INHERIT A `GV-50` ERROR.** Stated plainly because a clean result is a real finding.

#### ⛔ Every stretch where the moderator was merged — the 24 Evan turns, all inside 2spk `A`

These are the stretches the brief asks for: read out of `File 53`, **every one of them would be attributed to Noah Edmonds.** The nine substantive ones (≥3 sentences):

| Time | Sent | What it is |
|---|---|---|
| **0:03–1:09** | 13 | ⛔ **The entire debate introduction** — topic, both debaters named, Evan's own self-identification, the format. |
| 20:01–20:09 | 3 | clock reset; *"you guys can't— you You can't see me, can you?"* |
| **20:10–20:50** | 9 | ⛔ **The webcam apology to the audience** — 40 s of first-person narrative about a broken camera, entirely Evan's. |
| 36:16–36:26 | 3 | segment transition into the discussion period |
| 36:31–36:41 | 4 | *"I have this in the wrong order in my notes here. That, that was my mistake."* |
| **46:55–47:30** | 7 | ⛔ **The auctioneer joke** — *"have either of you ever considered becoming auctioneers?"*, plus Evan's account of his own debating. |
| 47:39–47:48 | 3 | *"And on YouTube you can slow it down."* |
| 62:57–63:09 | 4 | *"Yep, I don't even have to say anything. The phone just beeps."* |
| 63:13–63:34 | 7 | *"I missed both. I meant closing statement… I said rebuttal, I didn't mean rebuttal… yeah, it's late."* |
| **70:21–70:58** | 4 | ⛔ **Evan's own self-description** — *"you're both Much better read on church history than I am. I mostly just do philosophy, religion, and exegesis."* |
| **74:57–76:04** | 8 | ⛔ **The entire closing** — thanks, channel plugs, sign-off. |

Plus 13 short turns: *"Hmm."* ×2 (7:41, 15:52), *"Canon."* (35:47), *"Okay, well, you both finished with a few minutes to spare"* (36:08), *"Uh, 2 minutes."* (39:40), *"I hate it when the train of thought derails."* (41:30), **"Okay, so, um, James, it is now your turn."** (41:39), *"48 Seconds."* (45:57), *"I don't know."* (61:47), *"Okay, so now."* (63:37), **"Okay, and Noah, now it is your turn."** (67:45), *"Okay. Uh Noah, would you like to provide any sources?"* (72:27).

⚠️ **One boundary defect survives into `File 52` and is recorded rather than smoothed:** the `B` turn beginning at 1:15 opens with Evan's cue sentence *"So Noah, why don't you just go right ahead and give us your opening"* merged into Noah's turn. **`File 52` is the authoritative rendering; it is not a perfect one.**

### 3.4 ⭐ `RC-7` CROSS-CHECK — EVERY QUOTED PHRASE, AGAINST THE THREE-SPEAKER RENDERING

Run **only after** the mapping was established, as instructed. Every distinctive string in every `RC-7` finding (L589, L693, L694, L695, L768) was located in `File 52` and its speaker read off.

| `RC-7` finding | Anchor phrase | Time | Speaker | Verdict |
|---|---|---|---|---|
| L589 (`RC-7` header) | *"As a traditionalist Anglican, I hold to both scripture and… the ecumenical councils as authoritative, with the scriptures above the councils."* | 26:01 | **`C`** | ✅ Rev. James |
| `RC7-1`/`RC7-8` | *"first among equals, **which is the position I hold to**, as well as the position of the Eastern Orthodox"* | 30:28 | **`C`** | ✅ Rev. James |
| `RC7-1`/`RC7-8` | *"This would never allow, however, for papal supremacy or universal jurisdiction or papal infallibility."* | 30:38 | **`C`** | ✅ Rev. James |
| `RC7-1` | *"I do not deny that Saint Peter was the head of the apostles."* | 44:12 | **`C`** | ✅ Rev. James |
| `RC7-4` | *"the consensus of the fathers agree that the rock Jesus refers to… is not talking about the apostle himself"*; Augustine *"switching instead to the idea that his confession was the rock"* | 27:39, 28:10 | **`C`** | ✅ Rev. James |
| `RC7-4` | Eph 2:20 — *"Jesus Christ himself the chief cornerstone"*; *"The apostles are mentioned in conjunction with him"* | 28:37, 29:01 | **`C`** | ✅ Rev. James |
| `RC7-5` | *"Matthew 18, the keys are given to all of them… the power of binding and loosing is defined in Matthew 18 where it is the power of this appe[llate]…"* | 46:12 | **`C`** | ✅ Rev. James |
| `RC7-6`/`RC7-7` | Meletius presiding at the Second Council, in schism with Rome, *"considered today a saint by the Roman Catholics"* | 31:21, 31:33 | **`C`** | ✅ Rev. James |
| `RC7-6`/`RC7-7` | Leo's Tome — *"considered itself able to judge his tome"* | 33:32, 33:57, 65:25 | **`C`** | ✅ Rev. James |
| `RC7-6`/`RC7-7` | Vigilius arrested / recanted / condemned | 34:11, 34:36, 43:27, 45:25 | **`C`** | ✅ Rev. James |
| `RC7-6`/`RC7-7` | Honorius — *"to Honorius the heretic, anathema"* | 34:42, 34:54 | **`C`** | ✅ Rev. James |
| `RC7-6`/`RC7-7` | jurisdiction canons — *"specifically limit jurisdictions of every bishop, including the Bishop of Rome, by name"* | 35:48 | **`C`** | ✅ Rev. James |
| `RC7-12` | Acts 15 — *"James actually is the one who judges in verse 19"* | 64:15 | **`C`** | ✅ Rev. James |
| `RC7-9` (L768) | Monophysitism / Monothelitism / Three Chapters, *"which you and I both agree is a heresy, by the way"* | 34:11, 34:42, 43:38 | **`C`** | ✅ Rev. James |

> ## ✅✅ **NOTHING CURRENTLY ATTRIBUTED TO REV. JAMES IN `RC-7` IS IN FACT NOAH'S OR EVAN'S. ALL TWELVE `RC7-n` FINDINGS' QUOTED MATERIAL IS SPEAKER `C`.**

⛔ **BUT A REAL FORWARD HAZARD IS REGISTERED, because it nearly bit:**

- ⚠️⚠️ **`"first among equals"` occurs FIVE times in `File 52`, and FOUR of them are NOAH'S** — 6:49, 14:40, 17:44, 19:14 — all *characterising* Rev. James's position or arguing against it, **all before** Rev. James says it himself at 30:28. **A locator search on that phrase alone lands on the opponent four times out of five.**
- ⚠️ **`"Acts 15"` occurs three times; the first two (3:20, 8:34) are Noah's**, and Rev. James's `RC7-12` instance is the third, at 64:15.
- ⚠️ **`"the rock"` occurs seven times; the first (8:09) is Noah's.**

**Forward rule: in `File 52`, never take the first hit. Read the speaker label on every match.**

### 3.5 ⛔ `File 53` — WHY IT IS PRESERVED AND HOW IT IS MARKED

⛔⛔ **`File 53` IS REGISTERED AS A DEFECTIVE RENDERING AND IS EXPLICITLY NON-QUOTABLE.** No finding may cite it. No byte offset in it is registered. It is **not deleted**, because its existence *is* the evidence that AssemblyAI auto-detect undercounted a three-voice recording as two — a defect class with no other documented instance in this corpus, and one that a future pass needs to be able to see rather than take on trust.

---

## 4. TASK 2 — `RC` VERIFICATION AND BYTE-RANGE RETRO-REGISTRATION

**Method.** For each finding: collect its claim and quoted strings from `St_Francis_EMC_Distinctives.md`; locate in the registered transcript by exact-string search over the raw bytes; record the byte range and the sentence timestamp; cross-check load-bearing passages against the independent `-youtube.srt` rendering; classify.

⛔⛔ **NO FINDING TEXT WAS REWRITTEN.** Where the modern re-transcription words something differently, **both wordings are recorded** and the corpus text stands. Where a finding is unsupported or contradicted, **it is flagged for JD, not resolved.**

### 4.1 Headline counts

| Source | File | Distinct findings | ✅ VERIFIED | ⚠️ VERIFIED, WORDING DISCREPANCY | ⛔ NOT FOUND | ⛔⛔ CONTRADICTED |
|---|---|---|---|---|---|---|
| `RC-1` | 47 | `RC1-1`…`RC1-15` (15) | 7 | 7 | 1 (`RC1-10`) | 0 |
| `RC-2` | 48 | `RC2-1`, `RC2-2` (2) | 1 | 1 | 0 | 0 |
| `RC-3` | 49 | `RC3-1`…`RC3-29` less `RC3-2` (28) | 11 | 15 | 1 (`RC3-20`) | **1** |
| `RC-4` | 50 | `RC4-1`…`RC4-7` (7) | 7 | 0 | 0 | 0 |
| `RC-5` | 51 | `RC5-1`…`RC5-7` (7) | 6 | 1 | 3 clauses of `RC5-1` | 0 |
| `RC-7` | 52 | `RC7-1`…`RC7-12` (12) | 12 | 0 | 0 | 0 |
| **`RC-6`** | **—** | — | ⛔⛔ **NO RECOVERY TRANSCRIPT EXISTS — see §4.2** | | | |

### 4.2 ⛔⛔ `RC-6` HAS NO SUBSTRATE AND STILL DOES NOT

⭐ **The six confirmed matches are `RC-1`, `RC-2`, `RC-3`, `RC-4`, `RC-5`, `RC-7`** — identified by title AND video ID AND upload date, all six consistent with the corpus's own dating note at L363 with no mismatch anywhere:

| Finding | Corpus dating (L363) | Recovered upload | Agreement |
|---|---|---|---|
| `RC-1` | deacon-era ~2020-21 | 2020-04-30 | ✅ |
| `RC-2` | deacon-era ~2020-21 | 2020-06-04 | ✅ |
| `RC-3` | 2025, ~September | **2025-09-22** | ✅ **to the month** |
| `RC-4` | deacon-era ~2020-21 | 2020-05-22 | ✅ |
| `RC-5` | deacon-era ~2020-21 | 2021-01-24 | ✅ |
| `RC-7` | deacon-era ~2020-21 | 2020-06-02 | ✅ — and the video's own **title** reads *"**Deacon** James"* |

⛔⛔ **`RC-6` — *"Is Mary the Mother of God?"*, dated 2023 — IS NOT IN THE RECOVERY PULL.** No transcript, no video ID, no hash. **The findings resting on it (`RC6-n`, and L767's Theotokos finding, and L1278's Marian-restraint finding, and `RC6-4`'s share of the L429 biography composite) remain exactly as `RC-1`…`RC-7` were before this pass: minted from a vanished chat-thread paste, with no locatable substrate.** ⏳ **A recovery pull for `RC-6` is OWED and is not this pass's to perform.**

⭐ **The standing date-mismatch instruction was therefore never triggered by any `RC` entry** — there is no `RC` upload date that postdates its finding. It was tested against `BP-Sac` instead; see §5.

### 4.3 Byte-range retro-registration tables

*(Full per-finding tables, with anchor phrases and timestamps, are written into `St_Francis_EMC_Distinctives.md` as a dated retro-registration block, on the `260835-7` `GV`/`a202` precedent. Reproduced here in full.)*

#### `File 47` / `RC-1` — `GatewayToCatholicismResponse-transcript.txt`, 51,968 B, 634 sentences

| Finding | Byte range | Time | Anchor | Status |
|---|---|---|---|---|
| `RC1-1` | @43,091–43,116 · @7,870–7,892 · @2,694–2,723 | 46:54 · 9:04 · 2:55 | *"as a member of the ACNA, and I'm a deacon within the Diocese uh uh of the South"* / *"My Archbishop is my bishop, Archbishop Foley Beach."* | ⚠️ core verified; 7 composite clauses NOT in this file — see §6 flag 12 |
| `RC1-2` | @7,048–7,102 (+@7,762–7,856, @7,103–7,300) | 8:15 | *"Apostolic succession is not tied to one particular see."* | ✅ |
| `RC1-3` (episcopacy) | @46,014–46,133 | 50:10 | *"It's part of the **plenae esse**, I would say, part of the fullness of the church"* | ⚠️ **material** — see §6 flag 1 |
| `RC1-3` (real presence) | @8,654–8,677 · @28,081–28,240 · @17,702–17,764 · @19,366–19,483 | 9:59 · 31:01 · 20:04 · 22:06 | *"real objective presence"*; *"much stronger on the Eucharist… even than the Westminster Confession"* | ⚠️ *"Catholic"* not *"more catholic"* |
| `RC1-4` | @45,778–45,860 · @28,081–28,124 · @27,436–27,502 | 49:41 · 31:01 · 30:25 | *"baptism regenerates, and that's in our formularies. That is explicitly in our formularies."* | ✅ |
| `RC1-5` | @20,780–20,828 · @21,786–21,843 · @20,556–20,592 · @21,700–21,790 · @22,226–22,284 · @22,347–22,368 · @16,071–16,095 · @16,404–16,458 | 23:40–25:19, 18:12–18:43 | *"I want to say we're Reformed Catholic"*; *"we are actually fully Catholic and we are also Protestant"* | ✅ (one clause rides on `RC7-11`/`RC5-5`) |
| `RC1-6` | @24,642–24,655 · @45,488–45,693 · @25,031–25,075 · @23,416–23,478 · @48,237–48,253 · @48,523–48,539 · @46,433–46,562 · @47,662–47,704 | 27:31–52:37 | *"we cannot be the hallway"*; *"there's this big room called the Catholic room"* | ⚠️ ×2 — see §6 flags 4, 5 |
| `RC1-7` ★★ GATING | @42,887–42,966 · @43,154–43,201 · @43,514–43,555 · @43,208–43,267 · @43,722–43,771 | 46:39–47:43 | *"the United States never adopted the 39 Articles as a required standard of faith"* | ✅ **strongest-verified in the batch** |
| `RC1-8` | @51,283–51,332 · @51,651–51,760 · @50,886–50,941 · @51,433–51,597 | 55:19–56:12 | *"they themselves, first of all, said that they're not infallible. And second of all said, you can change these things."* | ✅ |
| `RC1-9` | @18,505–18,553 · @19,000–19,051 | 20:56 · 21:37 | *"Calvin was not opposed to iconography inherently"*; *"If my presbytery knew what my position on icons was…"* | ✅ hearsay hedge accurate — must not be relaxed |
| `RC1-10` ★ | — | — | *"disagrees with certain Homilies"* | ⛔ **NOT FOUND** — see §6 flag 8 |
| `RC1-11` | @34,931–34,968 · @44,304–44,416 · @36,505–36,539 · @39,750–39,797 | 38:12–43:31 | *"they are not bad in and of themselves"*; *"we are actually fighting against Puritanism"* | ⚠️ trivial |
| `RC1-12` | @33,092–33,123 | 36:19 | *"It's also in the East, but okay."* | ✅ — a four-word aside, not a developed rebuttal |
| `RC1-13` | @26,378–26,443 | 29:24 | *"it was actually illegally inserted into the Book of Common Prayer"* | ✅ dual-ASR confirmed |
| `RC1-14` | @49,812–49,835 · @49,958–49,986 · **@50,414–50,468** · @50,674–50,719 (passage @49,600–50,760) | 53:59–55:08 | *"this is more Catholic-minded than elements of the 1662"*; *"I prefer the 28, but I will also use this one. I use both."* | ⚠️⚠️ **possible wrong-prayer-book attribution — see §6 flag 2** |
| `RC1-15` | @16,799–16,853 · @16,936–16,960 · @20,227–20,281 | 19:05–23:08 | *"Salvation by grace alone, justification by faith alone"*; *"The Church of England never accepted the Synod of Dort"* | ⚠️ *"recoverings"*; read-aloud issue — §6 flag 6 |

#### `File 48` / `RC-2` — `PapacyDebateThoughts-Edmonds-transcript.txt`, 8,393 B, 96 sentences

| Finding | Byte range | Time | Anchor | Status |
|---|---|---|---|---|
| `RC2-1` | @38–63 · @379–400 | 0:02 · 0:20 | *"I am getting ready to move from uh Pennsylvania to Tennessee"*; *"at the end of summer, I will be heading to California"* | ⚠️ two sub-clauses NOT found — §6 flags 15, 16 |
| `RC2-2` ⭐ | **@1,363–1,403** (error) · **@1,499–1,544** (correction); context @1,205–1,617, mechanism @1,617–2,090, damage @2,282–2,530 | 1:24 · 1:47 | *"I said that the heresy was Monophysitism… However, actually, the heresy is Nestorianism, which is Christ Being 2 persons."* | ✅ **the specifically-requested check: L768's self-correction claim is VERIFIED** |

#### `File 49` / `RC-3` — `TeachingTheMass-transcript.txt`, 83,380 B, 1,156 sentences

| Finding | Byte range | Time | Anchor | Status |
|---|---|---|---|---|
| `RC3-1` | 742–820 (+477–573) | 0:54 | *"Instruction on Holy Communion according to the 1928 U.S. Book of Common Prayer."* | ✅ |
| `RC3-2` | — | — | — | ⛔ **ID DOES NOT EXIST** — numbering hole at 2 |
| `RC3-3`/`RC3-7` (biography) | 5,585–5,664 · 6,340–6,880 · 7,115–7,195 · 7,342–7,363 · 47,523–47,564 · 26,513–26,555 · 25,670–25,698 · 26,095–26,135 · 23,136–23,203 · 28,365–28,375 · 21,590–21,700 | 7:37–54:07 | *"I grew up in a very, actually, fundamentalist Baptist church"*; *"Father Ray, my priest"*; *"I was a Benedictine oblate for a few years"* | ⚠️ partial; 7 L429 elements absent — §6 flag 13 |
| `RC3-3`/`RC3-7` (ordination) | **73,198–73,273** | 1:22:53 | *"As a priest, I was newly ordained in 2020."* | ⛔⛔ **CONTRADICTED — §6 flag A1** |
| `RC3-4` | 8,643–8,702 · 8,704–8,889 (rationale 7,200–8,700) | 11:02 · 11:27 | *"that kind of makes it the Father James Show if that happens"* | ⚠️ `ad orientem`/`versus populum` = 0 occurrences |
| `RC3-5` | 9,476–9,531 · 9,788–9,884 · 10,039–10,204 · 11,055–11,151 · 11,369–11,442 | 12:27–13:57 | *"Prior to 1549, we have what is known as the Sarum Rite."* | ✅ |
| `RC3-6` | 17,864–18,061 · 22,615–22,746 · 18,402–18,499 · 19,436–19,554 · 19,728–19,863 · 20,027–20,217 | 21:20–26:35 | *"The alb is the… white robes that we see in Revelation. We're putting on the righteousness of Christ."* | ⚠️ **Rev 7:14 absent — load-bearing, §6 flag 3** |
| `RC3-8` ★★ | **29,468–29,619** (objection 29,336–29,467; illustration 29,620–29,944) | 34:17 | *"a symbol doesn't work well if it's not there. It's got to be there to work."* | ⚠️ verbatim; **Rev 5:8 framing is the corpus's — the text quoted is Ps 141:2, unnamed. §6 flag 9** |
| `RC3-9` ★★ | **30,678–30,817** · 30,114–30,253 · 30,259–30,493 · 30,494–30,677 · 30,818–30,915 | 35:02–35:48 | *"I need a strong argument to tell me no, we shouldn't use incense."*; *"That is never negated."* | ✅ **highest-confidence item in the batch** |
| `RC3-10` | 28,539–28,677 · 28,235–28,311 · 28,735–29,059 · 29,060–29,335 | 32:54–33:31 | *"the final nail in the coffin… was Malachi 1:11"* | ✅ verbatim |
| `RC3-11` | 29,945–30,050 | 34:48 | *"So incense is a symbol. There's nothing magical about it… Symbols are powerful."* | ✅ verbatim |
| `RC3-12` | 27,583–27,887 (framing 27,196–27,517) | 32:13 | *"There's a reason we have icons… We are not brains on sticks."* | ✅ verbatim |
| `RC3-13` | 34,438–34,562 · 34,081–34,139 · 34,410–34,436 | 39:39–40:06 | *"we're reverencing the reality of Christ being present amongst us"* | ✅ (object not named as tabernacle — caveat correct) |
| `RC3-14` | 40,746–41,150 · 41,700–41,779 (+44,970–45,274) | 46:54–51:2x | *"You'll notice **Ember Saturdays**…"*; *"Lent, which is our penitential season"* | ⚠️ *"Ember Saturdays"* not *"ember days"* |
| `RC3-15` | 44,369–44,476 | 50:50 | *"these creeds are accurate because they can be proven most assuredly by Scripture"* | ⚠️ *"Article 8"* is the corpus's identification; `article` = 0 |
| `RC3-16` | 50,438–50,733 · 50,734–50,819 · 50,220–50,438 | 57:41–57:59 | *"the spear goes through the side of our Lord. Water and blood come out."* | ⚠️ John 19:34 is the corpus's citation; `19:34` = 0 |
| `RC3-17` | 51,162–51,324 · 66,006–66,113 · 66,154–66,270 · 66,375–66,542 · 66,543–66,970 · 66,810–67,470 | 58:25, 1:14:39–1:15:39 | *"we don't believe in what's called transubstantiation, but we agree with the Lutherans"* | ⚠️ **"between Luther and Calvin" appears NOWHERE — §6 flag 10** |
| `RC3-18` ★★ | **60,537–60,642** · 60,420–60,536 · 61,196–61,368 | 1:09:04 | *"So I genuflect, or if my knees are really bad that day, I'll do a solemn bow, and then I will lift it up."* | ✅ **elevation prong un-gated** |
| `RC3-19` | 51,538–51,655 · 51,656–52,000 · 51,325–51,537 | 58:51 | *"unless I'm holding one of the elements, these— my thumbs and my forefingers— do not separate"* | ⚠️ `lavabo` = 0 |
| `RC3-20` | — | — | *"prays the 1928 commemoration of the departed"* | ⛔ **NOT FOUND — the most consequential negative. §6 flag A2** |
| `RC3-21` ★★ | **53,224–53,456** · 53,457–54,052 · 54,053–54,154 · 54,295–54,434 · 54,986–55,057 · 55,058–55,251 · 55,252–55,289 | 1:00:46–1:02:58 | *"That's not the belief of any historic church, by the way."*; *"it's the official declaration of God."* | ⚠️ ×3 minor |
| `RC3-22` ★★ | 62,088–62,155 · **62,636–62,750** · 63,012–63,197 · 62,751–63,011 · **58,760–58,835 / 58,919–59,272** · 59,273–59,420 | 1:07:03–1:11:33 | *"not to pay for our sins, but to give ourselves to God"* | ⚠️⚠️ **ATTRIBUTION — two quoted phrases are Massey Shepherd's. §6 flag 7** |
| `RC3-23` ★★ | 64,348–64,504 | 1:13:12 | *"at the very end, I lift up the elements. We say, O Father Almighty, world without end, amen."* | ⚠️ `doxology` = 0 |
| `RC3-24` | 67,496–67,569 · 67,637–67,681 · 67,686–67,861 · 67,862–68,120 | 1:16:18–1:16:31 | *"His body, blood, soul, and divinity are present."*; *"Christ is not what's called locally present."* | ⚠️ `Trent` = 0 |
| `RC3-25` | 72,502–72,650 | 1:22:10 | *"We believe in what's called concomitance… to receive one is to receive both."* | ✅ verbatim |
| `RC3-26` ★★ | **73,925–74,121** · 74,122–74,290 · 72,712–73,135 · 73,136–73,478 | 1:22:2x–1:23:41 | *"So we always, always offer both. There's never going to be a time when I'm the priest here where I will only offer The body…"* | ⚠️ emphatic; `both kinds` = 0, `withhold` = 0 |
| `RC3-27` ★★ | **74,355–74,468** · 74,469–74,766 | 1:24:23 | *"Any leftover is either reverently consumed or it is put in the tabernacle pew."* | ✅ **reservation prong un-gated**; *"tabernacle pew"* is an ASR artefact, the corpus's `[in]` repair is correct |
| `RC3-28` | 74,767–74,903 · 75,827–75,892 | 1:25:07 · 1:26:17 | *"we will even do what are called the ablutions"* | ⚠️ substantive — §6 flag 11 |
| `RC3-29` | 76,340–76,405 · 76,571–76,660 · 77,555–77,830 · 77,862–78,046 · 78,491–78,587 | 1:26:52–1:29:08 | *"During Lent and during Advent, you will not say the Alleluia part."* | ⚠️ Gloria rule stated for *"penitential season"* generally |

⭐ **`RC-3` DATING INDEPENDENTLY CONFIRMED, AND THE ASR QUIRK REGISTERED.** The Charlie Kirk reference the corpus used to narrow `RC-3` to ~Sept 2025 **is** in the file, at **45,104–45,172 · 0:51:28** — but rendered ***"Charlie Park"*** in the AssemblyAI pass **and identically in the independent YouTube captions**. `Kirk` = **0 occurrences in both renderings.** Substantively unmistakable (paired with *"the young woman and the train"*, given as the reason a bidding prayer was added). Independent corroboration at **42,042–42,149 · 0:48:16**: *"was it the 13th or 14th? 14th. This upcoming Sunday is St. Matthew's"* → week of 14–21 Sept 2025, against an upload of 2025-09-22. **The corpus's dating is right; the name does not grep.**

#### `File 50` / `RC-4` — `Apocrypha-transcript.txt`, 25,645 B, 263 sentences · **all 7 findings VERIFIED, 0 discrepancies, 0 contradictions**

| Finding | Byte range | Time | Anchor | Status |
|---|---|---|---|---|
| `RC4-1/3/4/6/7` (deuterocanon preference) | 162–209 | 0:11 | *"a better term for it would be the Deutero-canon"* | ✅ ⚠️ qualified at 1,133–1,177: *"I'm going to use those terms interchangeably"* |
| `RC4-1/3/4/6/7` (Article 6) | **9,734–9,774** (+9,133–9,172) | 10:35 | *"we're not saying that it's not canonical"* | ✅ **exact**; ⛔ the WCF 1.3 comparison is `[Analysis]` — `Westminster` = 0 |
| `RC4-1/3/4/6/7` (Homilies) | 12,569–14,563 | 13:37–16:30 | *"An Homily of Alms Deeds"*; *"the same lesson doth the Holy Ghost also teach"* | ✅ |
| `RC4-1/3/4/6/7` (via media) | 14,994–15,257 | 16:47–17:06 | *"I grew up on Chick tracts"* … *"exactly the same as the rest of Scripture"* | ✅ both poles exact |
| `RC4-1/3/4/6/7` (Jerome, Gregory) | 15,484–15,517 | 17:19 | *"Jerome, for instance… Gregory the Great, who was a pope"* | ✅ |
| `RC4-1/3/4/6/7` (2 Esdras dating) | 17,774–17,846 · 20,480–20,523 | 20:14 · 23:50 | *"the first 2 chapters of 2 Esdras is very clearly after the time of Jesus"* | ✅ (corpus holds ~1/8 of the argument) |
| `RC4-2` | **4,101–4,166** (+2,434–3,086, 3,643–3,672) | 4:34 | *"When it comes to the Deutero-Canon, we're not sure. So we're just going to say, here ends the reading."* | ✅ ⚠️ **speaker slip at 3,674–3,822 reads INVERTED — §6 flag 14** |
| `RC4-5` (a) IC prooftext | **11,172–11,218** | 12:10 | *"full of grace could also be translated as highly favored one"* | ✅ exact; ⚠️ *"Luke 1:28"* is the corpus's supplied citation, never spoken |
| `RC4-5` (b) Maccabees/purgatory | **8,936–8,986** (+8,552–8,594) | 9:46 | *"Does not mean that purgatory or purgation is wrong."* | ✅ ⭐ **discharges L2914's own tag-integrity flag — §6 flag 20** |

#### `File 51` / `RC-5` — `BadArgumentsRomanCatholicism-transcript.txt`, 23,834 B, 233 sentences

| Finding | Byte range | Time | Anchor | Status |
|---|---|---|---|---|
| `RC5-1` (Mt 18:18 keys→all) | **2,959–3,024** | 3:06 | *"Matthew 18:18, Jesus indicates that he has given the keys to all of the apostles"* | ✅ |
| `RC5-1` (primacy granted) | **3,740–3,881** | 3:54–4:06 | *"He is the leader of the apostles. I would not deny that"* | ✅ ⚠️ *"leader"*, not *"head"*; `first among equals` = 0 in this file |
| `RC5-1` (three denials) | 2,604–2,650 | 2:53 | *"This says nothing about universal jurisdiction… papal supremacy… papal infallibility."* | ✅ |
| `RC5-1` (Eph 2:20) | **4,592–4,664** | 5:02 | *"There's no mention or singling out of Saint Peter within this foundation"* | ✅ |
| `RC5-1` (rock = confession) | — | — | `confession`/`confess` = **0** in transcript AND YouTube captions | ⛔ **NOT IN `RC-5`** — carried by `RC7-4`, verified there at 28:10 |
| `RC5-1` (patristic consensus list) | — | — | `Chrysostom` 0, `Jerome` 0, `patristic` 0, `consensus` 0 | ⛔ **NOT IN `RC-5`** — carried by `RC7-4`, verified there at 27:39 |
| `RC5-1` (keys = discipline/appellate) | — | — | `discipline` 0, `appellate` 0, `appeal` 0 | ⛔ **NOT IN `RC-5`** — carried by `RC7-5`, verified there at 46:12 |
| `RC5-2` | **8,265–8,663** | 8:49–9:32 | *"Master's Seminary… Saint Augustine, Origen, Tertullian, um Cyprian of Carthage, Cyril of Alexandria"*; *"Master's Seminary is John MacArthur's seminary."* | ✅ all five names exact, in his order; ⚠️ over-reach — §6 flag 17 |
| `RC5-3` | **10,055–10,152** | 11:10 | *"I'm submitted to Scripture. I'm submitted to my bishop. submitted to the church and her teachings."* | ⚠️ **THE CORPUS IS RIGHT AND THE NEW TRANSCRIPT DRIFTED — §6 flag 18** |
| `RC5-4` | **10,180–13,600** | 11:15–15:10 | the 33,000-denominations debunk, all three prongs | ✅ present at length; the description's NCRegister link is the article he promises at ~13,300 |
| `RC5-5` | **14,472–14,542** | 16:00 | *"The Protestant reformers never saw themselves as starting a new church."* | ✅ exact |
| `RC5-6` ★★ | **15,799–15,938** | 17:34–17:47 | *"they need to show that as biblical and as historical"* / *"We don't get to presuppose that all of that is true and then I have to prove it wrong."* | ✅ **verbatim, dual-ASR identical.** He frames it himself at 15,288–15,333 as *"a presupposition that sort of lingers behind the arguments"* |
| `RC5-7` | **21,604–21,655** · **21,789–21,850** | 23:53 · 24:05 | *"you can retcon history to make it fit your theology"*; *"if your argument is, well, it could still be true technically… you're gonna have to give me something stronger than that"* | ✅ both strings verbatim, dual-ASR identical |

#### `File 52` / `RC-7` — see §3.4. **All 12 findings ✅ VERIFIED and speaker-confirmed as `C` = Rev. James.**

---

## 5. TASK 3 — `SacramentValidity` vs the `BP` SACRAMENT-VALIDITY FINDINGS

> ## VERDICT: **(a) SAME SOURCE.** `File 54` **is** the video the `BP-Sac` findings were minted from.

⛔⛔ **AND THE BRIEF'S PREMISE FOR THIS TASK IS FALSE. IT IS FLAGGED, NOT QUIETLY USED.**

The brief describes *"a large date gap"* and invokes the standing instruction, which governs *"where an upload date **postdates** the finding."* **The upload date does not postdate the finding — it predates it by eight months.**

- The `BP` batch was applied at **`260619`–`260620` = 2026-06-19/20** (`St_Francis_EMC_Distinctives.md` changelog L7083).
- The video was uploaded **2025-10-17**.

**The standing instruction's trigger condition is not met. It was therefore not applied, and the reason is recorded rather than the instruction being stretched to fit.**

⚠️ **The secondary premise — that the `BP` batch is deacon-era — is also not what the corpus says.** L1286 dates only the *icons* video (`BP-Icons`) to ~2020, and Cross-Batch item 8 at L2842 already records the batch as internally split. Against `SRC_Channel_Inventory.md` the five `BP` videos run **2020-04-02 → 2025-10-17**:

| Sub-tag | Video | ID | Upload |
|---|---|---|---|
| `BP-Angl` | Five Reasons I Became Anglican | `hJ1HA4kRv3M` | 2020-04-02 |
| `BP-Icons` | Are Icons Idolatrous? | `UmIAkdRtzhw` | 2020-07-03 |
| `BP-Switch` | Advice for Switching Traditions | `imipCdI7B9s` | 2021-01-13 |
| `BP-RPW` | Responding to Matthew Everhard on the RPW | `SPIMaZUVeJw` | 2025-08-07 (File 3) |
| **`BP-Sac`** | **What Makes a Sacrament Valid?** | **`p-jeXC7sokY`** | **2025-10-17** |

**`BP-Sac` is a second current-era item in a batch whose "2020" label has been over-generalised — not a repost of deacon-era material.**

### 5.1 The evidence for SAME SOURCE — content match, not topic match, as instructed

**26 of 26 quoted clauses across all eight `BP-Sac` findings are present as EXACT byte strings in `File 54`:**

`BP-11` @749, @783 · `BP-12` @1,528/1,547, @1,667, @1,964 · `BP-13` @1,135, @1,187, @1,331 · `BP-14` @3,277, @3,389, @2,676, @2,746, @2,475 · `BP-15` @7,706 · `BP-16` @8,229, @8,201 · `BP-17` @4,075, @4,147, @4,343, @4,738 · `BP-18` @7,271.

**Zero misses.** The only divergences are cosmetic normalisations a finding-writer would make (*"4"* → *"four"*, disfluency dropped). The independent YouTube captions render the four-fold list **without** the disfluency — *"the proper minister, the proper matter, the proper form, and the proper intent"* — matching `BP-12`'s clean quote exactly.

⭐ **And the match is STRUCTURAL, which is what settles it against a re-teaching.** `BP-15`'s distinctive *analytical* observation — that he is maximally permissive about who may validly baptize but **conspicuously withholds** the intent prong for the Eucharist — is a description of **this script's shape** (@2,122–3,434 permissive; @7,494–7,893 the withholding, *"central to the debate between Anglicans and Roman Catholics on whether or not Anglicans have valid holy orders"*). That does not survive independent re-recording as a coincidence. `BP-16`'s self-styling and the `barelyprotestant@gmail.com` address are this video's outro verbatim.

⭐ **Corroborating:** `SRC_Channel_Inventory.md` inventories all 368 videos across `EXT-2`/`EXT-3` from a ~2026-08-25 pull. **Exactly one** carries this title. There is no earlier sacrament-validity video for the batch to have used.

### 5.2 ⚠️⚠️ WHAT THIS BREAKS — FLAGGED, NOT FIXED

- ⛔⛔ **`POD-1` (L6824) and `POD-12` (L6834) date `BP-13` and `BP-15` to "(2020)". On this evidence that is wrong by five years, and it is load-bearing.** `POD-12` argues that 2019 podcast material *"supplies from 2019 … the premise `BP-15` (2020) only implied"* — a **one-year** developmental gap. If `BP-15` is 2025-10-17 the actual gap is **six years**, and the POD→BP developmental reading needs re-derivation. `POD-1`'s *"this is the same doctrine a year earlier"* is affected identically. ⛔ **Nothing edited.**
- ⚠️ **`SRC_Channel_Inventory.md` marks `p-jeXC7sokY` `INCLUDE` (a not-yet-ingested candidate), decided `260835-10`.** It is in fact already mined as `BP-11`…`BP-18`. A future intake acting on that `INCLUDE` would re-mine eight existing findings. **The miss is explicable — the `BP` batch is pre-manifest, carries no File number and no recorded video ID — and the cell is corrected by this pass** (§7).
- ⚠️ **One loose end, recorded rather than explained away.** At @7,856 he says he *"is writing a script for a video on"* the Anglican-orders/Eucharistic-intent question. File 32 (*Are Holy Orders Within Anglicanism Valid?*, `uSHi3Fqgerg`) is **2025-08-21, two months EARLIER**, and no orders-validity video after 2025-10-17 appears in the inventory through 2026-08-25. Weak counter-evidence about the *recording* date (as against the upload date). **It does not touch the SAME-SOURCE verdict**, which rests on the 26/26 quote match and the single-title inventory result.
- ⚠️ **The original `BP`-batch input transcript is gone.** A sweep of `~/EMC/original transcripts/` found no `BP-Sac` source file (the `BP-RPW` source survives). A byte-for-byte comparison against the batch's actual input is impossible; the identification rests on the evidence above.

---

## 6. TASK 4 — `2019BCP-MorningPrayer` vs `a202` RECORDING 4

> ## VERDICT: **(b) OVERLAPPING BUT DISTINCT TREATMENT.**

⭐ **They are definitively two different videos** — `xySXFYRQ9tI` (2020-03-28) vs `ulrD_RdI6Q0` (2023-01-29) — established from the `-meta.json` and the manifest, not inferred. The question was whether the *material* is the same. It is not.

### 6.1 The quantitative test

Both texts normalised and shingled. Source A = 5,239 words; Source B (`a202.txt` @184,863–211,169, 26,307 B, read directly and matching the manifest registration exactly) = 5,349 words.

| Shingle | Shared | Jaccard |
|---|---|---|
| 8-gram | 15 | 0.00142 |
| 10-gram | 8 | 0.00076 |
| 12-gram | 6 | 0.00057 |
| 15-gram | 3 | 0.00028 |

⭐⭐ **Every shared shingle at n ≥ 10 is one fixed liturgical text — the Gloria Patri.** *"as it was in the beginning is now and ever shall be world without end amen."* **There is not one shared 10-word run of his own prose between the two recordings.**

⚠️ Caveat recorded honestly: Source A is a clean `universal-3-5-pro` transcript, Source B is raw unpunctuated older ASR, so true overlap is somewhat higher than 0.0006. Not remotely high enough for (a).

### 6.2 The decisive axis — they walk two physically different books

- **Source A (2020)** walks the **modern-language "red" 2019 BCP** while personally using the 1928: *"my personal favorite is actually the 1928… **this is the prayer book that I use**… However, for one that has modern language in it, **which this is**…"* (@2,448–2,760). Confirmed at @22,011: on the modern Lord's Prayer, *"I have personal problems with the way this one is worded."*
- **Source B (2023)** walks the **Traditional Language Edition**, having switched: *"2019 traditional language book of common prayer **traditional language Edition**"* (@184,974); *"essentially the same as the regular **red** prayer book"* (@185,071); *"only last year did I switch over to the 2019"* (@185,324).

**Pagination confirms different books:** lectionary at **p. 736** (A, @8,533) vs **p. 738** (B, @185,593); collects *"in the 600s"* (A) vs **pp. 598–640** (B, @203,999).

### 6.3 Different worked example, and different orders

| | Source A | Source B |
|---|---|---|
| Date worked | **28 March 2020** (@4,136, @5,154); *"this is during the coronavirus"* (@3,995) | **28 January 2023** (@185,943) |
| Season | 4th Sunday in Lent | 3rd Sunday of Epiphany; *"Lent is coming up February 22nd"* (@193,882) |
| First lesson | **Exodus 35** | **Genesis 27** |
| Second lesson | **Matthew 27:27-56** | **John 14:15-end** |
| Psalm | **Ps 69:1-18** | **Ps 132-135** |

⭐⭐ **And the speaker's own orders differ, on tape** — a hard discriminator ruling out any re-upload reading. Source A @13,921, on the absolution: *"**If you are a deacon as I am**, or if you are a layperson, you are… going to remain kneeling."* Source B @191,913: *"so a priest even Alone by himself… **would still read this**… so that's the one that I do when I'm by myself."* **Deacon in 2020, priest in 2023** — consistent with L363's *"priesting falls between roughly 2021 and 2023."*

### 6.4 Scope — each covers substantial material the other entirely lacks

**Only in Source A:** ~6 minutes of prayer-book history (1534 break with Rome; the **Sarum Rite** @981; **Cranmer** @914; 1549 @672; 1552; 1662 as *"the standard prayer book for all of Anglicanism"* @1,933 — **none of these words occur in B**); a full **Holy Days / calendar section** @5,363–8,533, including the three-tier calendar (*"Red-letter holy days… the closest thing we have to required holy days"* @5,675), the explicit refusal to canonise (*"we don't want to start creating, canonizing people as saints when the church is divided like it is today"*, St Charles the Martyr excepted, @6,436), and optional commemorations incl. **MLK Jr.** and **Bishop Tikhon** @7,280–7,336 — **B has no calendar section at all**; antiphonal psalmody by sides of the nave @18,391; the Prayer for Mission traced to **1979** @23,785.

**Only in Source B:** a **1928-vs-2019 Venite comparison** @193,614; an actual **plainsong demonstration** — he chants Ps 132 @195,467 (*"chant"* absent from A); **antiphons** with a personal aside @192,727; **Malachi 1:11** as an Epiphany opening sentence and *"one of my favorite verses in the Old Testament"* @208,618 (⭐ a §13/incense-adjacent datum); the Great Litany aside @206,349; the *Benedictus es Domine* traced to *"the deutero canonical parts of Daniel"* @199,996; the **KJV-with-deuterocanon** shown on camera @200,926; **facing liturgical East at the Creed** @202,470; a third-grade-student anecdote and *"I've been doing this for… over 10 years now"* @210,100/@210,419.

**What genuinely overlaps** is a shared *syllabus*, wholly re-expressed: same office order, prep-first method, MP at p. 11, rubrics-in-italics, boldface = the people's parts, officiant need not be ordained, confession long/short, *O Lord, open our lips*, Venite, psalms whole-verse or by asterisk, Gloria Patri, lesson→canticle×2, *Te Deum* except in Lent, Benedictus, Apostles' Creed, Lord's Prayer traditional preferred, suffrages, collects, Prayer for Mission, General Thanksgiving, St John Chrysostom, the Grace. Both prefer the **30-day Psalter**. Both give the *"here endeth the reading"* vs *"the word of the Lord"* convention for deuterocanonical lessons (A @19,460–19,514 naming Tobit and Sirach; B @198,442).

### 6.5 ⭐⭐ A REGISTERED OPEN ITEM IS DISCHARGED AS A BY-PRODUCT — `GV-55` IS LOCATED

`St_Francis_EMC_Distinctives.md` **L6995** and **L7026** record `GV-55` as **"⛔ UNLOCATED WITH CONFIDENCE"**, with the failed search terms stated: *"'eastward' and 'king james'/'kjv' both return 0 hits anywhere in the file."*

⭐ **All three of `GV-55`'s elements ARE in `a202` recording 4:**

| Element | `a202.txt` offset | Text |
|---|---|---|
| Eastward at the Creed | **@202,470** | *"it's proper to be all facing the same direction standing at the Apostles Creed **Facing East or liturgical East** for the church"* |
| KJV-with-deuterocanon | **@200,926** (`King James` @200,936) | *"this is a **King James Bible with the deuterocaine and the Apocalypse** I love it I show it to my mom all the time"* |
| Lent | **@193,882** (+ the Te Deum rubric @199,700–200,300) | *"what in Lent is coming up February 22nd"* |

⭐ **Why the earlier search missed it, stated so it is not re-derived:** the ASR never renders *"eastward"* — it renders *"Facing East"* / *"liturgical East"* (`liturgical East` = exactly one hit in the file, @202,470). And *"King James"* occurs in **title case only**; a case-sensitive grep for `king james` returns 0, **exactly as L7026 truthfully reports.** ⛔ **Both prior search terms were sound and both were unlucky. L7026's verdict is not called wrong; it is superseded in practice.**

⚠️ **`GV-54`'s registered offset @185,228 (L7022) vs this pass's independent grep @185,229** — a one-byte difference, almost certainly 0- vs 1-indexing. **Flagged, not corrected.**

⭐ **And `File 55` adds a dated pre-switch attestation the corpus did not have:** Source A @2,448, in his own voice on **2020-03-28**, *"my personal favorite is actually the 1928… this is the prayer book that I use"* — a first-person fix on the pre-switch state, sitting between `GV-30` and `RC1-14`.

⚠️ **It also complicates Known Gap 9 in the corpus's own preferred direction, and is reported, not resolved:** in the very same March 2020 video in which he says the 1928 is the book he uses, **he is teaching Morning Prayer out of the red 2019.** That is another instance of **concurrent use by choice** — the pattern already flagged at L1756 (`LS-13`/`POD-3`/`POD-13`). **A further argument against reading 1928→2019 as a clean linear switch. Known Gap 9 NOT resolved.**

⛔ **`File 55` neither corroborates nor unsettles `GV-55`'s two load-bearing halves, and that silence is itself a finding:** Source A contains **no** eastward/liturgical-east instruction (its four `East` hits are *"Eastern Orthodox"* and *"Easter season"*) and **no** KJV show-and-tell (its single `King James` @2,758 is *"less King James type language"*, describing the modern 2019's register — the opposite point). **`GV-55` remains a recording-4-only datum.**

---

## 7. ⛔⛔⛔ FLAGGED FOR JD — NOT RESOLVED, NOT CORRECTED

**Every item below was found by this pass and deliberately left standing. The corpus text is unaltered in every case, per the never-alter rule and the `GV-4` precedent.**

### A. Contradiction (bucket d) — one

**A1. ⛔⛔ `RC3-3`/`RC3-7` ORDINATION DATE.** `File 49` @**73,198–73,273** · 1:22:53: *"This is a big thing during COVID **As a priest, I was newly ordained in 2020.**"* The corpus at L429 assigns *"newly ordained 2020"* to the **deacon** era and L363 puts *"priesting between roughly 2021 and 2023."* Corroborated at 28,235–28,311 tying the California cure to *"when I first was ordained."* **A reconciliation exists (transitional diaconate then priesting inside 2020) but is untested.** ⛔ **This is the `GV-4` shape and is handled the same way: flagged, not corrected.** Note it interacts with §6.3's tape evidence that he is a **deacon** on 2020-03-28 and a **priest** by 2023-01-29 — which does **not** settle it, since a 2020 priesting after March is consistent with both.

### B. NOT FOUND — two, with search terms stated

**A2. ⛔ `RC3-20` — *"prays the 1928 commemoration of the departed"* — NOT FOUND. The most consequential negative of the pass.** Searched in `File 49`: `depart` 0 · `deceased` 0 · `commemorat` 0 · `requiem` 0 · `repose` 0 · `all souls` 0 · `died in` 0 · `soul of` 0 · `faithful departed` 0 · `purgatory` 0 · `church militant` 0 · `cloud of witnesses` 0 · `funeral` 0 · `burial` 0 · `dead` 2 (both irrelevant). Cross-checked in the independent YouTube captions: `depart` 0, `deceased` 0, `commemorat` 0. **The one place it would sit — the Prayer for the Whole State of Christ's Church — IS reached, at 52,150–52,600 · 0:59:39, but he names it and moves to page 75 without reading it or mentioning the departed.** ⚠️ **Silence is not evidence he does not; but Known Gap 10's guard (L158, L216, L2915, L2917, L2953, L7049, and `SRC_Manifest.md` L1354) currently rests on `RC3-20` as an affirmative datum that this file does not supply.** ⚠️ A second sign the tag may be mis-prefixed: the odd `RC3-20` cross-reference at L3397/`IP-81` is about **baptismal validity**.

**A3. ⛔ `RC1-10` — *"disagrees with certain Homilies"* — NOT FOUND.** `Homil`/`homil` = **0 hits** in `File 47` (51,968 B read end-to-end, three passes), 0 in its 248,875-byte YouTube captions, 0 in both `File 48` renderings, **and 0 in `File 49`.** Nearest passage @47,662–47,897 concerns *elements of Anglicanism claiming unique theology*, not the Homilies. ⚠️ **QC-b and Q2 currently rest on an unlocated finding.** If it exists it is in `RC-6` — for which no transcript exists (§4.2).

**A4. ⛔ `RC3-2` — the ID does not exist anywhere in the corpus.** `RC3` numbering has a hole at 2. Recorded so a later pass finds a decision rather than an apparent gap.

### C. Attribution problems — two, both load-bearing

**A5. ⛔⛔ `RC3-22` — TWO QUOTED PHRASES ARE MASSEY SHEPHERD'S, NOT REV. JAMES'S.** L1022 tags *"represent"* and *"the occasion of its continuing benefits"* as `[Stated, RC3-22]`. `File 49` @**58,760–58,835** · 1:07:03: *"I'm just going to quote this from **Massey**, who is a Brilliant liturgist. **I have some disagreements with him**…"* — the quoted phrases follow at @**58,919–59,272** · 1:07:19. **They are Massey H. Shepherd's, read aloud and endorsed.** The corpus also drops *"and innumerable"* and *"to his Church"* from inside its quotation marks. ✅ **The non-propitiatory half (*"not to pay for our sins, but to give ourselves to God"*, @62,636–62,750) IS his own and is unaffected — Q4a's reweight survives.** ⏳ Needs a read-aloud note on the `BLOG-3` pattern.

**A6. ⚠️ `RC1-15` — *"a reformation martyr"* is HIM READING TURNER'S ARTICLE ALOUD.** `File 47` @16,936–16,960. The name *"Cranmer"* does not occur in the sentence — the corpus supplies it. His own act is the **non-objection** that follows: *"There's um not really much here that I would necessarily argue with."* **The corpus's *"calls Cranmer 'a reformation martyr'"* overstates.** ⏳ Needs a read-aloud note of the `POD-3`/`BLOG-49` class.

### D. Wording and citation discrepancies — corpus wording vs transcript wording

**1. ⚠️⚠️ `RC1-3` — MATERIAL, and it may collapse a development sequence.** Corpus: *"part of the church's 'essence … fullness' (transcript garbled at the key word but esse-leaning)."* `File 47` @46,014–46,133: **not garbled** — *"It's part of the **plenae esse**, I would say, part of the fullness of the church."* Word confidences `plenae` 0.707, `esse` 0.936; the independent YouTube rendering hears *"plan a si."* ⛔ **If it is *plene esse*, `RC1-3` COINCIDES WITH `LS-10` (2022) rather than preceding it, collapsing the `RC1-3` → `LS-10` → `IP-10` sequence at L1180 / L1194 / L4821 / L5474.** ⏳ **EAR-VERIFICATION OWED: `KsLqJIPrpCg` at ≈00:50:13.**

**2. ⚠️⚠️ `RC1-14` — POSSIBLE MIS-ATTRIBUTION TO THE WRONG PRAYER BOOK. NOT RESOLVED.** The corpus attaches *"more Catholic minded than elements of the 1662"* (@50,414–50,468) **to the 1928**. The unbroken *"this one"* deictic chain across @49,600–50,760 points at the **2019**: nearest antecedent is *"The diocese's official prayer book is the 2019"*; permission language follows (*"allowed to… my archbishop lets me"*); Turner's article attacks the ACNA 2019, never the 1928; and eight sentences later *"I prefer the 28, but I will also use **this one**"* makes *"this one"* explicitly **not** the 28. ⛔ **Deixis is gestural — he is holding books — so audio alone cannot close it.** Material for Known Gap 9 and for `GV-30`/`GV-54`/`POD-3`/`BLOG-154`. ⏳ **EAR-VERIFICATION OWED: `KsLqJIPrpCg` at ≈00:54:47.**

**3. ⚠️ `RC3-6` — the Rev 7:14 citation is the corpus's, not his.** L1090 reads *"alb and surplice = Christ's righteousness, **Rev 7:14**."* `File 49` @17,864–18,061: *"the white robes that we see in **Revelation**"* — no chapter or verse. `7:14` = 0, `tribulation` = 0. Only two *"Revelation"* hits in the file; the other (@56,695) is *"there's one in Revelation, I can't remember the exact reference."* ⛔ **The `RC3-6` → `RV-24` → `RV-45` "prooftext moves within the same book" observation (L1121 / L2546 / L2583) is comparing a SPECIFIED 2026 verse against an UNSPECIFIED 2025 book-level reference.**

**4. ⚠️ `RC1-6` over-reach — *"Anglicanism is a full 'room'"* is not his phrase.** `File 47` @46,433–46,562: *"there's this big room called **the Catholic room**… My goal is to be as much in that Catholic room as possible."* Substance supported; the noun phrase is not his.

**5. ⚠️ `RC1-6` Fisher quotation is abridged.** Corpus: *"no peculiar confession of its own … the Catholic faith of the ancient Church."* Transcript @23,416–23,478: *"no peculiar **thought, practice, creed, or** confession of its own. It has only the Catholic faith of the **ancient Catholic Church**, as preserved in the Catholic creeds…"*

**6. ⚠️ `RC1-15`** — corpus *"recoveries"*; transcript @16,799–16,853 *"**recoverings**"* (his coinage, confirmed in both ASRs).

**7. ⚠️ `RC1-11`** — corpus *"not bad in themselves"*; transcript @34,931 *"not bad **in and of** themselves."* Corpus omits two clauses at @44,304: *"because we don't want to be Puritan"* and *"so it makes sense to actually be more Catholic-minded."*

**8. ⚠️ `RC1-3` Calvin** — corpus *"more catholic"*; transcript @17,702 *"Calvin's Institutes is actually really, in many ways, **Catholic**, far more—"* (the comparative is carried by *"far more"*).

**9. ⚠️ `RC3-8` — the Rev 5:8 framing is the corpus's.** Rev 5:8 is **never cited**; the scripture actually quoted at @29,620–29,944 is **Psalm 141:2**, unnamed. `bowl` / `vial` / `golden` / `prayers of the saints` all = 0. ⛔ **The finding's substance — *"a symbol doesn't work well if it's not there"* @29,468–29,619 — is verbatim and stands.**

**10. ⚠️ `RC3-17` — *"between Luther and Calvin" appears NOWHERE in `File 49`.*** `between` occurs exactly once (@50,552, the mixed-chalice sentence). His own framing is *"That first half… more Lutheran… That second half… more Calvinist."* Corpus also elides *"what's called"* from *"we don't believe in **what's called** transubstantiation."*

**11. ⚠️ `RC3-28` substantive.** Corpus glosses the ablutions' purpose as *"to lose no consecrated particle"*; `particle` = 0, `crumb` = 0. **His stated rationale** (@74,767–74,903; @75,827–75,892) is the strength of the presence doctrine plus washing the fingers that held the Sacrament and consuming the ablution water.

**12. ⚠️ `RC1-1` composite-attribution flag.** L429 is a five-source composite (`RC1-1, RC3-3, RC6-4, RC2-1, RC3-7`), so **no clause can be attributed to `RC1-1` from the document alone.** Clauses NOT in `File 47` or `File 48`: *"Calvinist stage"* (`Calvinist` 0), *"period visiting Eastern Orthodoxy"* (3 `Orthodox` hits, all about *recommending* EO), *"Father Ray"* (0), Benedictine Oblate (0/0), KJV/Coverdale (0/0), Morning-Prayer-before-Communion, clergy-attire maximalism (`cassock`/`clerical`/`collar`/`vestment`/`attire` all 0). *"fundamentalist Baptist"* is PARTIAL (`File 47` gives *Baptist* only, @11,212–11,235).

**13. ⚠️ `RC3-3`/`RC3-7` elements absent from `File 49`:** *"Calvinist stage"* 0 · *"Pennsylvania"* 0 · *"Tennessee"* 0 · *"ACNA"* 0 · *"Foley Beach"* 0 · *"Diocese of the South"* 0 · *"EMC"* 0. Those parts of L429 must rest on `RC1-1`/`RC6-4`/`RC2-1` — and `RC6-4` has no substrate (§4.2).

**14. ⚠️⚠️ `RC4-2` — A SPEAKER SLIP THAT READS AS AN INVERSION, AND IT IS HIS, NOT THE ASR'S.** `File 50` @3,674–3,822 · 4:05 transcribes as: *"if we read a **non**-apocryphal book, or **non**-deuterocanonical… they're just going to say, uh here ends the reading"* — the opposite of the finding. **Cross-checked against the independent YouTube captions: rendered identically.** ⭐ **Two independent renderings agree, so this is Rev. James's own tongue-slip, not a transcription artefact — and he self-corrects 150 bytes later at @4,101–4,166: *"When it comes to the Deutero-Canon, we're not sure. So we're just going to say, here ends the reading."*** ⛔ **The corpus reading is the correct one. Logged so that a future reader hitting @3,674 does not conclude the corpus inverted him.**

**15/16. ⚠️ `RC2-1` — two sub-clauses NOT found.** *"first cure, San Francisco Bay Area"*: `San Francisco` 0, `Bay Area` 0 in **both** `File 48` and `File 47`; he names only *"California"* (@379–400). *"newly ordained 2020"* is **not stated** in `File 48` — that video (2020-06-04) shows him still a **deacon** preparing to move. **The 2020 dating is a sound inference from upload dates, not a transcript statement.** ⚠️ Contrast flag A1, where `File 49` states 2020 for *priestly* ordination.

**17. ⚠️ `RC5-2` over-reach.** *"Rejects memorialism as a misreading of the fathers"* is exactly right. *"…**and sources his own patristic real-presence reading**"* is **not warranted by `File 51`**: `real presence` 0, `transubstantiation` 0, `memorial` 0. His claim is purely **negative** (*"none of those believed in a mere symbolic-only position"*) plus a **methodological** prescription (@8,899–8,969: *"get as close to the source as you can and try to read the whole source"*). He states no positive eucharistic doctrine in that video.

**18. ⭐ `RC5-3` — THE CORPUS IS RIGHT AND THE NEW TRANSCRIPT IS THE ONE THAT DRIFTED. DO NOT "CORRECT" THE CORPUS HERE.** `File 51` @10,055–10,152 (AssemblyAI): *"I'm submitted to Scripture. I'm submitted to my bishop. **submitted to the church and her teachings**."* — the third *"I'm"* is **dropped**. Corpus (L588/L1777/L4565): all three present. **YouTube's independent 2021-era captions: all three present.** ⭐⭐ **This matters specifically because L4565 builds an argument on the triple frame — *"an enumeration in a repeated grammatical frame — 'submitted to' three times"* — and declines to read a rank off it. That reasoning is CONFIRMED, not undermined: the threefold repetition is real and dual-attested.** ⛔ Cite @10,055–10,152 **with the dropped-`I'm` noted and the YouTube rendering as the corroborating second witness.**

**19. ⚠️ Legend error at L392.** It states the `RC3` range as *"RC3-1..~27"*; the actual range is **`RC3-1`…`RC3-29`** (`RC3-29` exists at L1724) **with a hole at `RC3-2`**. ⛔ **Also: no per-ID ledger exists for the `RC` batch anywhere** (checked `St_Francis_EMC_Distinctives.md`, `PROJECT_STATE.md`, `SRC_Manifest.md`, `RJ_Final_Question_List.md`, `RJ_Incense_Analysis.md`) — `RC` IDs appear only as tags on compound narrative bullets, so sub-claim → ID mapping is by claim-cluster, not by registry. **This is a structural gap the `RC` batch shares with `BP` and it limits what any verification pass can assert about which sub-claim a given ID "really" names.**

**20. ⭐ `RC4-5` — L2914's OWN TAG-INTEGRITY FLAG IS ANSWERED.** L2914 warns that *"the patch material cites 'RC4-5' for both this Maccabees/purgatory point and the separate Luke 1:28 / Immaculate Conception doubt … these may be two distinct statements miscoded under one ledger ID … Flag for verification against the original transcript."* ✅ **Verified: both statements are real, both are in `File 50`, ~2,180 bytes / ~2.5 minutes apart** (Maccabees @8,936–8,986 / 9:46; Luke 1:28 @11,172–11,218 / 12:10). **So the shared tag is NOT a cross-source miscoding — it is one ledger ID covering two distinct statements from one source, exactly as the flag's more benign branch supposed.** ⛔ **Which statement `RC4-5` "really" is has NOT been resolved; both are now byte-located, so either can be cited directly.**

**21. Minor, recorded without comment:** `RC1-7` numeral vs spelled-out *"39 Articles"* · `RC1-3` real presence doubled formula · `RC3-4` `ad orientem`/`versus populum` = 0 · `RC3-14` *"Ember Saturdays"* · `RC3-15` *"Article 8"* is the corpus's identification, `article` = 0 · `RC3-16` John 19:34 is the corpus's citation · `RC3-19` `lavabo` = 0 · `RC3-21` *"That's not the belief of any historic church"* / *"God **does** work through hierarchy"* / *"a sacramental words"* ASR stumble · `RC3-23` `doxology` = 0 · `RC3-24` `Trent` = 0 · `RC3-26` `both kinds` = 0, `withhold` = 0 · `RC3-29` Gloria rule stated for *"penitential season"* generally · `RC2-2` he corrects **which heresy the Three Chapters were condemned for**, not the controversy · `RC1-12` the chasuble/ritualized-donning material at L1091 is `[Analysis]`, not covered by `[Stated, RC1-12]` · `RC1-5`'s *"Reformers never saw themselves as starting a new church"* rides on `RC7-11`/`RC5-5`, not on `File 47`.

### E. Caution flags carried forward

- **`RC1-9` hearsay layering must not be relaxed.** Sproul-on-Calvin is *"I've seen it on video"* (one remove); Sproul-on-himself is friend-of-a-friend (two removes). The corpus's *"secondhand, hearsay, hedge"* is exactly right.
- **`RC1-13`** — he expressly declines to argue the Black Rubric (*"I won't get into that now"*). A bare assertion; relevant to how much weight it bears against `IP-38`/`BLOG-5`.
- **`RC3-12` / `RC3-27` caveats CONFIRMED.** Icon *veneration* is nowhere in `File 49` (`venerat` = 0) — **Q17 correctly stays open.** No adoration of the reserved sacrament is described (`monstrance` 0, `exposition` 0) — **QC-d caveat confirmed.**
- ⚠️ **Unattributed-voice hazard, `File 47` @51,515–51,597 · 56:02: *"ecumenical councils are not infallible."*** Sits inside a reductio against Rome; **whose position it states is genuinely ambiguous.** Recorded as ambiguous, not adopted. Relevant to §3 / Q5 conciliar selectivity.
- ⚠️ **SENSITIVE, `File 47` @10,700–13,900 · ≈12:10–15:40 — the Truro case**, including non-sexual abuse allegations against a **named third party**, plus megachurch-dynamics analysis. ⛔ **Flagged NOT for deployment; logged only so it is not later "discovered" unlogged.**

### F. Substantive material held by NO existing finding

⛔⛔ **NOTHING MINTED. Listed with byte offsets so a later pass can act on JD's ruling.**

**`File 47` / `RC-1`:**
- ⭐⭐ **@40,264–40,303 · 43:59 — THE EARLIEST INCENSE DATUM IN THE CORPUS, AND IT RUNS AGAINST THE PRACTICE.** *"Well, maybe not smell because incense was not, but—"* — he **concedes** incense was not part of pre-20th-c. Anglican practice and does not contest it. `incense` = **1 occurrence in all of `File 47`.** ⛔ **Bears directly on §13, `IP-98`…`IP-105`, `DQ-19`/`DQ-24`(b), and `Incense_Conversational_Outline.md` Step 2 — which this pass did not touch.** ⏳ **Route to whoever holds §13.**
- ⭐ @49,377–49,453 — *"I don't mean Romanism as a slur… I'm talking about the unique parts of Roman Catholicism."*
- ⭐ @46,489–46,562 — Rome as *"one foot in, one foot out"* of the Catholic room.
- @36,218–36,264 — epiclesis sourced to the Scottish Episcopal Prayer Book.
- @25,773–25,900 — public, courteous disagreement with his own canon **by name** (Canon Greg Goble).
- ⭐ @10,084–10,120 (+@1,700, @17,400, @14,500, @49,460) — the epistemic standard, five instances in one video: *"There's no evidence being given here. It's just being an assertion."*
- @15,430–15,458 — *"pre-Protestant"* qualifier · @2,941–2,965 — *"Byzantine Papal Catholic"* coined · @9,000–9,900 — Ordinariate→SSPX trajectory + parable-of-the-sower reading of conversion churn · @7,892–7,935 — succession line traced to St Andrew, hedged *"I think"* · @27,900–28,240 — four-item *"what makes one Catholic"* list, baptism and Eucharist as *"the chief sacraments"* · @50,099–50,143 — Facebook Daily Office streams, deacon-era.

**`File 48` / `RC-2`:**
- ⭐⭐ @2,870–4,600 — **A SECOND self-correction (Theodoret), plus an admission he did not check his own patristic list**: @3,641–3,671 · 4:19 *"I got this sort of list from someone… It could have been James White… so I got that list, and I didn't check all of them out."* **Stronger than the Nestorianism half the corpus holds; reinforces L1777.**
- @3,137–3,174 — his own Mt 16:18 position stated plainly · @4,099–4,135 — Augustine's change of mind, taught by him · @4,262–4,286 — Tertullian excluded on a sainthood criterion · @4,993–5,024 — Assyrian Church of the East hedge.
- ⭐ @5,656–5,713 / @5,268–5,300 — **cross-examination named as the load-bearing debate format** (he wanted 30 min, got 15). **Directly relevant to structuring any in-person exchange.**
- ⭐ @6,896–6,955 — a stated **charity rule for post-debate commentary**.

**`File 49` / `RC-3`:**
- 🎯 **@56,387–56,444 · 1:04:16 — Sursum Corda as *"where heaven and earth meet together"*** (+@56,000–56,290: *"every single liturgy, without exception, throughout all of Church history… has what is called the Sursum Corda"*). ⛔ **Heaven-earth-participation language is already present in 2025, which materially complicates Cross-Batch item 8 at L2836 reading it as a 2026 reweight (`IP-1`/`IP-3`) away from `RC3-10`'s Malachi lead.** Does not overturn the thesis — Malachi is still the stated decisive argument for incense here.
- 🎯 **@55,760–55,871 · 1:03:36 — a second, stronger no-own-power absolution disavowal, quoted nowhere in the corpus:** *"I'm not forgiving you in my own power. I'm pointing to Scripture, and I'm pointing to God."* A near-verbatim **2025** antecedent of `IP-34` and `POD-2`.
- 🎯 **@16,648–16,707 (amice = *"the helmet of salvation"*) and @16,872–17,053 (cassock = our sinfulness).** `RC3-6` lists alb/surplice/stole/maniple/chasuble but **not amice or cassock**. ⛔ **Matters for `RV-24`, whose "black cassock under the white alb" pairing is treated as the 2026 form of `RC3-6` — the cassock half is already here in 2025, unlogged.**
- 🎯 @15,462–15,532 — **clerical collar credited to the Church of Scotland** — the same *"it isn't actually Roman"* move as the chasuble rebuttal, from a Presbyterian source. Useful for Q8a.
- 🎯 **@57,722–57,836 / @58,028–58,151 / @58,577–58,648 — an explicit anti-innovation rule in his own voice, 2025:** *"We don't want to innovate. We don't want to go beyond what Scripture does."*; *"We want to follow the Tradition of the Church as grounded in Scripture."* ⚠️ **RPW-adjacent normative-principle language that sits interestingly AGAINST `RC3-9`'s burden direction. Bears on §13 / `IP-2` / `DQ-4` / `DQ-19`. Recorded both ways, adjudicated neither.**
- 🎯 @73,198–73,478 — **directly and independently corroborates `IP-79`'s "the cup never withheld, even during COVID"**, same COVID test case, a year earlier.
- @62,570–62,635 — the only named exception to the joined-fingers rule · @44,198–44,289 — *"if you cannot confess this you are not what's called an orthodox Christian"* · @27,583 — incense and icons in the **same enumeration** (relevant to `BLOG-60` at L5877).
- Lower priority: Nicene Creed as boundary @44,198 · *"altar or table, either works out fine"* @48,861 · intinction discouraged @70,743–71,700 · reception on the tongue preferred not required @69,229 · Prayer of Humble Access @63,724 · no deacon at the parish @75,113 · bow at the name of Jesus (Phil 2:10) @34,881 · processional cross vs pagan processions @36,400–36,700 · Ten Commandments + law/gospel @38,082–38,900 · one-year lectionary @13,197 / @42,540 · *"Liturgy = work of the people,"* Acts 13:2 @8,995 / @12,650 · Aslan *"not safe, but good"* @32,394 · homily deliberately ~15 min + critique of evangelical *"fluff"* @46,000–47,120 · posture rules @78,760–80,800 · Prayer of St. Francis as closing @82,168.

**`File 50` / `RC-4`:**
- ⭐ **@22,270–22,800 — A RETENTION-PRESUMPTION STATEMENT IN THE DEACON ERA, IN CONSENSUS-TRADITION TERMS:** *"we want to throw away as little as possible when it comes to the tradition, the consensus tradition of the Church."* ⛔ **Directly germane to Open Q 15 / QC-f at L2870-2871 and to `LS-23`'s consensus rule. Not held. Flagged as significant; NOT characterised as resolving anything.**
- @18,367–22,400 — the full 2 Esdras 7:28-29 messianic prooftext **presented at strength then dismantled by himself** (~4 kB; the corpus holds one clause) · @16,600–17,570 — Geneva Bible / 2 Esdras 1:30 ↔ Mt 23:37-38 parallel · @6,100–6,400 — *"We can't do that as Anglicans"* on Article 6 · @10,584–10,650 — a **Matthew 16 over-weighting argument eight months EARLIER than `RC-5`'s** · @5,353–5,642 — **dated 2020-05-22 jurisdiction/status data**: *"my province, the Anglican Church in North America"*, the 2019 is *"the one that I was ordained in"*, and *"once I get ordained, God willing… to the priesthood"* (⛔ **deacon, not yet priested, as of 2020-05-22 — bears on flag A1**) · @4,458–4,498 — the *"word of the Lord"* / *"here ends the reading"* distinction is a **modern accretion**, *"I don't think it's in the '28"* · @4,828–4,905 — deuterocanon used *"as part of the worship itself"*, broader than `RC4-2` · @25,161–25,400 — Apocrypha printed in Protestant Bibles until the 1800s, removed *"because it was cheaper"* · @24,000–24,750 — a **finer-than-binary credibility gradation within the deuterocanon**.

**`File 51` / `RC-5`:**
- ⭐⭐ **@12,799–12,932 · 14:19 · 2021-01-24 — *"the REC, uh what I am… Reformed Episcopal Church"*. ⛔⛔ THIS IS A `CL-9` DATUM.** The corpus records `CL-9` as *"does NOT move — tenth consecutive intake, `Reformed Episcopal` 0·0 · `REC` as an acronym 0·0 · `ACNA` 0·0"* (L70, L112, L190), and L429 currently reads *"Deacon-era jurisdiction was ACNA, Diocese of the South."* **RC-5 says, in his own voice, that in January 2021 he was REC.** REC/ACNA full communion makes the two compatible rather than contradictory, **but the corpus holds no tag for it.** ⛔ **NOT minted, NOT reconciled, NOT entered anywhere. The single highest-value un-held datum found by this pass.**
- ⭐ @5,374–9,000 — **the whole quote-mining methodology section**, of which only the Master's Seminary illustration is held: the definition and that *"both Protestants and Roman Catholics and Eastern Orthodox do"* it; the **Gregory Nazianzen** worked example (a Father calling a "pope" infallible who turns out to mean the **Bishop of Alexandria**, @6,158–6,800); **Pope Leo praising Emperor Leo** as infallible with the reductio *"are we supposed to believe in… empirical Infallibility?"* (@7,039–7,200); the **hyperbolic-language principle** (@7,396–7,900); and the sourcing rule (@8,899–8,969). **A stated patristic-hermeneutics rule, largely unheld.**
- @15,996–16,800 — **the conciliar counter-evidence independently in `RC-5`** (*"they try to pull rank, the papal legates"*, and the historiographical test *"did they see themselves as doing this sort of usurpation…? I don't think they did"*). The corpus holds this at L695 under `RC7-6`/`RC7-7`/`RC7-12` only. **`File 51` is an independent, earlier, SOLO attestation of the same argument.**
- ⭐⭐ **@15,691–15,745 — *"Not even an ecumenical council can override the papacy"*, dated 2021-01-24 — THIRTEEN DAYS EARLIER THAN `LS-14`** (2021-02-06), which the corpus itself notes came *"from a two-voice undiarized file in which three attributions were overturned."* **`File 51` is solo, single-speaker, zero attribution risk.** Not held by any finding.
- ⭐ @~20,780–20,900 — **the generalisation-defeater sentence, the cleanest statement of the `RC5-7` rule in the file, and the corpus does not hold it:** *"what we're looking for is not a way to reconcile the things out. We're looking for what the evidence seems to indicate."* ⛔ **Bears directly on the incense "it isn't negated" lever L697 names, and on the L2870/L2871 dual reading of Open Q 15 — because it is a rule against reconcilability-as-warrant IN GENERAL, not only about the papacy.**
- @13,660–15,290 — the character-attack **asymmetry** argument (*"we're not saying that there is a Luther office"*) · @17,228–17,600 / @22,750–22,900 — the retcon analogy **credited to Dr. Jordan Cooper**, twice · @21,000–21,600 — **self-reported prior Baptist identity applied self-critically**, naming *The Trail of Blood* — *"we did this as Baptists"* · @22,216–22,400 — the Trent Horn / Jerry Walls exchange · @23,203–23,400 — his closing concession, *"there are better arguments… and I'll take those more seriously."*

### G. Items owed

1. ⏳ **A recovery pull for `RC-6`** (*"Is Mary the Mother of God?"*, 2023). Its findings still have no substrate.
2. ⏳ **Ear-verify `KsLqJIPrpCg` at ≈00:50:13** — *plene esse* / *plenae esse* / bare *esse*? Decides whether `RC1-3` coincides with `LS-10` or precedes it.
3. ⏳ **Ear-verify `KsLqJIPrpCg` at ≈00:54:47** — which book is he holding? Decides `RC1-14`'s referent; touches Known Gap 9.
4. ⏳ **JD's ruling on flag A1** (the 2020 priestly-ordination contradiction).
5. ⏳ **JD's ruling on §2.2** — whether the seven-file warrant narrows to six, or stands with the `File 49` exception noted.
6. ⏳ **A read-aloud attribution note for `RC3-22`** (Massey Shepherd) and **`RC1-15`** (Turner), on the `BLOG-3` / `POD-3` pattern.
7. ⏳ **`RC3-20`'s warrant line** needs a status flag — decided by whoever owns §5 / Known Gap 10.
8. ⏳ **Correct L392's `RC3` range** (`RC3-1..~27` → `RC3-1..RC3-29`, hole at 2).
9. ⏳ **Re-derive the `POD`→`BP` developmental reading** given `BP-Sac` = 2025-10-17 (§5.2).
10. ⏳ **Route `File 47` @40,264–40,303 (the 2020 incense concession) to §13.**
11. ✅ **`BLOG-11`'s provenance flag (L1106) can be ADVANCED:** the recovered `-meta.json` confirms `RC-1` = `KsLqJIPrpCg`, uploaded **2020-04-30** — **the same date as the W1 blogspot post** the HTTP 429 blocked. ⛔ **That is a DATE MATCH, not a script identification.** Strengthen the flag; do **not** convert to a merge without comparing the post's text to `RC1-11`/`RC1-13` at @34,931 / @26,378.

---

## 8. WHAT WAS TOUCHED

**Tracked files edited (4):** `SRC_Manifest.md` · `St_Francis_EMC_Distinctives.md` · `SRC_Channel_Inventory.md` · `PROJECT_STATE.md`. **New (2):** this artifact and its raw-session companion under `passes/`.

⛔ **`Incense_Conversational_Outline.md` and `RJ_Incense_Analysis.md` NOT TOUCHED.**
⛔ **Nothing drafted, altered or posted to Rev. James.**
⛔ **`validate_project.py` NOT modified.** `RJ_Final_Question_List.md`, `RJ_Open_Questions_and_Divergences.md`, `On_Incense_and_the_Altar.md`, `ORCHESTRATION.md`, `SRC_Coverage_Register.md` NOT touched.
⛔ **No existing finding altered, renumbered, re-pointed or corrected. No byte offset in any existing entry altered** (including `GV-54`'s @185,228, whose one-byte discrepancy is flagged, not fixed).
⛔ **`DQ-9` unmoved · `DQ-24` untouched · no Discord state touched.**
⛔ **Nothing committed.**

---

## 9. CLOSING GATE

### 9.1 Validator AFTER, against baseline

| | BEFORE | AFTER |
|---|---|---|
| Summary line | `82 ok · 9 warnings · 0 errors` | **`82 ok · 9 warnings · 0 errors`** |
| Firing codes | the nine listed at §0.1 | **the same nine, identical text, in the same order** |

✅ **NO CHANGE. No warning introduced, none cleared, no error introduced.** `[C3]` is satisfied for all four edited files because each carries a `Last updated: 260835-11` stamp **and** a matching `PROJECT_STATE.md` §4 registry row, both updated in the same pass.

### 9.2 `git --no-optional-locks status --short` — every line

```
 M PROJECT_STATE.md
 M SRC_Channel_Inventory.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
?? passes/260835-11_rc-bp-retro-verification_close-out.md
?? passes/260835-11_rc-bp-retro-verification_diff.patch
```

**HEAD unchanged: `07031e718559f522d6c5fc6c731174eb5ce9280d`.**

### 9.3 Diff accounting — all 16 deletions attributed

`--stat`: **4 files changed, 323 insertions(+), 16 deletions(-)**. **Every one of the 16 deleted lines is a line this pass deliberately modified. There is no unattributable hunk, and no file outside the four is modified.**

| Count | What | Where |
|---|---|---|
| 4 | `**Last updated:**` stamp lines | `PROJECT_STATE.md`, `SRC_Manifest.md`, `SRC_Channel_Inventory.md`, `St_Francis_EMC_Distinctives.md` |
| 4 | `PROJECT_STATE.md` §4 registry rows | the same four files' rows |
| 8 | `SRC_Channel_Inventory.md` decision-cell rows | `KsLqJIPrpCg`, `sO-_EJbq_oQ`, `Nxx1QEhvIB0`, `s2-jIFFBiJg`, `wvpJL0DzBto`, `auiLAv8BYpk`, `p-jeXC7sokY`, `xySXFYRQ9tI` |

⭐ **Every one of the 12 replaced prose cells retains its prior text verbatim after a *"Previously:"* marker.** Nothing was overwritten; the three `PROJECT_STATE.md` §4 rows with descriptive prose likewise keep their `260835-10`/`260835-7` text after *"Previously:"*. The fourth (`PROJECT_STATE.md`'s own row) carries no prose and is a bare stamp bump.

### 9.4 What to stage

**Stage all six:**

```
git add PROJECT_STATE.md \
        SRC_Manifest.md \
        St_Francis_EMC_Distinctives.md \
        SRC_Channel_Inventory.md \
        passes/260835-11_rc-bp-retro-verification_close-out.md \
        passes/260835-11_rc-bp-retro-verification_diff.patch
```

⛔⛔ **NOTHING WAS COMMITTED, AND NOTHING WAS STAGED. The four tracked modifications and the two new `passes/` artifacts are left in the working tree for JD.**

### 9.5 Where the full record lives

- **This file** — the complete pass report.
- **`passes/260835-11_rc-bp-retro-verification_diff.patch`** — the full unified diff (457 lines, 158,219 bytes), written out because it far exceeds what chat can carry.
