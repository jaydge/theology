# 260835-12 — Diarization verification: the `A101-2026-07-26` room primary plus seven Batch 9 recordings

**Pass type:** attribution establishment and artifact registration. ⛔⛔ **NOT AN INTAKE. NO FINDING MINTED. NO NUMBER OF ANY PREFIX CONSUMED EXCEPT `File`.**

---

## ⏳ EAR-CHECK QUEUE — READ THIS FIRST, FIVE ITEMS

Listed at the top per the brief, on the `PapacyDebate` ear-check table model. Each names the artifact, the timestamp, and **what listening to it would resolve**. ⛔ None is a blanket queue; each is a specific decision that content alone could not make.

| # | Artifact | Timestamp | What one listen resolves |
|---|---|---|---|
| **E1** | `hDRmWM5Nkgw` (Anglican 101, Session 1: Our History, 2021-06-15) | **00:32–01:49** (the teaching voice's first sustained stretch) | ⛔⛔ **BLOCKING. Is the teaching voice Rev. James at all?** No self-identification, no direct address by name, no biography unique to him anywhere in 54 minutes. **This channel is PROVEN to host another man's teaching** (the two Fr. Ray videos below), so channel ownership is not a warrant. Until this is answered the file cannot be mined. Compare against any known-his recording. |
| **E2** | `IGNmKMXhL1Q` (Morning Prayer, 5th Sunday in Lent, 2020-03-29) | **SPK_B 14:45–18:18** (the homily) against **SPK_A 00:02–01:01** (the office) | **Are these two men, or one man split by register?** The two labels alternate with perfect regularity, and label `B` carries *both* the congregational response (*"Thanks be to God"*) *and* the officiant's own versicle (*"The Lord be with you"*) — which no single role does. Either the diarizer split one voice at the reading/preaching register change, or there are two officiants. Content cannot decide it. |
| **E3** | `A101-20260726` room capture | **107:25–107:48** (turn 374) | A brief cross-talk exchange (*"Huh? Oh, it's the, uh, Saint Francis or the — Oh, there are plenty of those."*) is **merged into the teacher's label**. Not load-bearing — no finding rests there — but it fixes the exact impurity boundary of label `A` and would tell us whether other rapid-crosstalk merges are likely. |
| **E4** | `A101-20260726` room capture | **50:04–54:07** (turns 171→176) | Confirms **speaker `B` = the second priest, "Father Bryan."** The identification is already locked at three content anchors (below) and I regard it as established; this is a cheap confirmation of a hazard that will govern all future use of this file. |
| **E5** | `A101-20260726` room capture | **123:26–124:01** (turns 471–478) | ⭐ **Which label is JD?** Speaker `C` is, on strong inference, JD — he leaves the Discord questions, does the deep dives, stays after class. JD would know in one second. This matters because the corpus rule is *"JD's questions are never findings about Rev. James"*, and knowing `C` = JD converts that rule from a content judgment into a label rule. |

⚠️ **E1 and E2 are the only two that BLOCK work.** E3, E4 and E5 are confirmations and conveniences.

---

## Gate

| Item | Value |
|---|---|
| HEAD | `98660cab503358084425e482cee5d75a75ce80be`, branch `main` |
| `git --no-optional-locks status --short` before first edit | **EMPTY** — captured directly, not reconstructed |
| Validator BEFORE | **`82 ok · 9 warnings · 0 errors`** |
| `PROJECT_STATE.md` stamp at gate | **`260835-11`** |
| This pass | **`260835-12`** |
| Next-free File at gate | **`File 56`** |

**Nine firing codes, individually:** `[C1]` `src/SRC_Discord_RPW.md` 2 relative timestamps outside message headers · `[C3]` `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` no parseable stamp · `[C3]` `tools/transcribe_yt.py` no parseable stamp · `[C4]` `St_Francis_EMC_Distinctives.md` 2 stale answered-question passages · `[C5]` `RJ_Final_Question_List.md` 17 volatile-state assertions · `[C5]` `RJ_Incense_Analysis.md` 9 · `[C5]` `St_Francis_EMC_Distinctives.md` 7 · `[C10]` §15 eight findings behind the `LS` ledger head · `[C11]` outline eleven `IP` findings unreviewed. **Identical to the `260835-10` and `260835-11` gates; none of this pass's business.**

**Stamp derivation.** `grep -rhoE '\b26[0-9]{4}-[0-9]+\b'` across the repo returns apparent `260835-12` hits at `PROJECT_STATE.md:5,27,31`; `passes/260835-8_…_close-out.md:20,262`; `passes/260835-9_…_close-out.md:3`; `passes/260835-9_…_raw-session-output.md:22`; `passes/260835-10_…_close-out.md:11`; `passes/260835-11_…_close-out.md:35,38`. **Every one was opened and read. All are prose inside earlier close-outs asserting their own absence.** Highest REAL stamp is `260835-11` — it has artifacts in `passes/` and is `PROJECT_STATE.md`'s own stamp. **This pass is `260835-12`.**

**`File` number re-derived fresh.** Highest REGISTERED is `File 55`; every `File 56` occurrence repo-wide is a next-free assertion (`PROJECT_STATE.md:7`, `SRC_Manifest.md:3,3423`, `St_Francis_EMC_Distinctives.md:2931`). **`File 56` was free.**

**FUSE lock.** The `260835-3` diagnosis was **applied, not re-derived** — every git read used `git --no-optional-locks`; no lock created, none removed, no `rm` attempted.

---

## ⛔⛔ THE HEADLINE: THREE OF THE SEVEN RECORDINGS WOULD HAVE POISONED THE CORPUS, AND TWO OF THEM ARE NOT HIS AT ALL

Stated first because it is the whole value of the pass.

1. ⛔⛔⛔ **`8nRhmD4w-Wg` and `9Fezj9WMh3A` — THE TEACHING VOICE IS FR. RAY, NOT REV. JAMES. NOT ONE WORD OF EITHER FILE'S 74 MINUTES OF TEACHING IS HIS.**
2. ⛔⛔⛔ **`DavM_5hcN0w` — SPEAKER `B` IS PASTOR MIKE WINGER, PLAYED FROM WINGER'S OWN VIDEO. 11.4 minutes / 2,296 words of a Calvary Chapel anti-paedobaptist argument sits inside a file whose author is refuting it.**
3. ⛔⛔ **`GeWfXTAjFDo` — "1 speaker" IS WRONG. It is a live class whose participant turns are entirely swallowed into the single label.**

⭐ And two of the brief's own working hypotheses are **falsified**, reported rather than complied with (§7 below).

---

## Task 0 — `A101-2026-07-26` room primary

### ⛔⛔ First, a correction to the brief's framing, and it changes what can be claimed

The brief calls this *"the missing `[R]` primary that sixteen existing findings depend on."* **It is not that file.** `SRC_Manifest.md` L517 registers the `[R]` primary as `A101-20260726-JD-recording-with-q-and-a.md` — **57,305 bytes, `96a9c5a9…`**, held outside the repo, found missing on disk by `SRC_Disk_Reconcile_report.md` (2026-08-25) and re-confirmed missing at `260835-9`.

The new artifact is **a fresh AssemblyAI diarized ASR of the same underlying room audio** (`Audio_07_26_2026_19_15_11.mp3`, `8a74a5a0…`, 126,120,854 bytes) — **100,141 bytes, `087a8314…`**, generated `2026-08-27T16:27:12Z`. Different bytes, different hash, different rendering.

⭐ **So the SUBSTRATE is recovered; the specific registered `[R]` markdown is still absent.** That is a real and large gain — the sixteen findings now have a locatable room-side source again, and for the first time a *diarized* one, which the missing file never was. ⛔ **But `SRC_Manifest.md`'s `96a9c5a9` row is NOT satisfied by this file and is NOT overwritten.** A third rendering is registered beside it. ⏳ **Recovery of the original `96a9c5a9` markdown remains OWED.**

### Speaker structure — five labels, 131m 23s (7,883 s), 1,533 sentences, 489 turns

| Label | Turns | Words | Minutes | Identification |
|---|---|---|---|---|
| **A** | 212 | 14,058 | 88.4 | **The teaching priest — Rev. James** (established below) |
| **B** | 88 | 1,622 | 14.0 | ⛔⛔ **A SECOND PRIEST — "Father Bryan"** |
| **C** | 113 | 1,679 | 7.7 | Well-read questioner; leaves the Discord questions — **on strong inference, JD** (E5) |
| **D** | 34 | 471 | 2.7 | Older man, low voice; the genetic-code/original-sin interlocutor |
| **E** | 42 | 495 | 3.3 | Questioner-inquirer; possibly the "Chrissy" addressed at 107:25 |

⚠️ `B`'s 14.0 minutes is inflated by silence — turn 479 (124:25–126:56) is 151 seconds of near-total mumble in the post-class ambient stretch. His **substantive** speech is roughly 6 minutes across four turns. ⛔ **This is exactly why speaking duration was not used as an identification heuristic** — the brief's warning, and the `File 52` inversion, both hold here.

### ✅ FIVE SPEAKERS IS CORRECT — THIS IS NOT THE `6Z68nITG1Is` FRAGMENTATION PATTERN

Each label carries a **stable, distinct, non-overlapping persona**, and they interact with one another as distinct persons:

- **B** — clerical register throughout; speaks of *"the rubrics to Communion"*, *"when my presiding [bishop]"*, the priest's faculties in the first person, church history as *"sort of my wheelhouse"*.
- **C** — layman's well-read questioning: *"You seem pretty well-read on church history. Can apostolic succession be proven like a pedigree…"*; deep dives on Dutch supra/infralapsarian history.
- **D** — one hobby-horse, pressed repeatedly: sin transmitted through genetic code; and a flat objection, *"I take issue with your statement, we desire to sin."* Announces his own voice quality: *"It's a little bit difficult to hear you. I'm sorry. My voice is low anyway."*
- **E** — newcomer-inquirer register: crucifix vs empty cross, whose faith is enacted in infant baptism, *"are you ever available to just go into more conversation about specific questions that we have?"*

⭐ **Fragmentation would produce labels that swap mid-topic with no interactional logic. These do the opposite.** Verdict: **five real participants.**

### ⭐ `A` = Rev. James — established, and stated at exactly the strength the evidence supports

⛔⛔ **THE NAME "JAMES" DOES NOT OCCUR ANYWHERE IN THIS TRANSCRIPT, AND NOBODY ADDRESSES `A` BY NAME.** So this is **NOT** established by self-identification or direct address, and it is not claimed to be. It is established by **role, biography, and elimination**:

1. **`A` is a priest, in his own words** — 44:37, *"As a priest, I am not allowed to deny and reject somebody who has repented."*
2. **`A` is the preacher of that morning** — 16:42, *"We preached about justification this morning."* (2026-07-26 was a Sunday; the class ran 19:15.)
3. **`A` ≠ Father Bryan**, the only other priest in the room — `A` addresses him at 50:04 (*"Father Brian, I'm told you have some sins to confess"*) and speaker `C` distinguishes them at 108:01 (*"I forget if it was Brian or you"*).
4. ⭐⭐ **`A` tells Rev. James's own distinctive biography in the first person** — 75:05, *"I left the Baptist world… I was realizing I have to basically anathematize all of church history."* This is the exit narrative the corpus independently attributes to him and which `IP-35` already logs.
5. **`A` is the man who answers the project's Discord questions** — 123:31, *"there's one that you left on the Discord. I don't think I've gotten to it. I'll get to them when I can."*
6. **The content matches the registered `A101-2026-07-26` row exactly** — Articles IX–XVI, Article XVII announced and not taught, and the post-session Black-Rubric / sacrifice-of-the-Mass discussion.

⭐ **Anchor 4 is the strongest single one**, and combined with anchor 3 (elimination of the only other clergyman present) I regard the identification as **established for registration purposes**. ⏳ A name-level confirmation is nonetheless cheap and is queued as **E4/E5**.

### ⛔⛔ THE LOAD-BEARING HAZARD: A SECOND PRIEST IS IN THE ROOM AND SPEAKING DOCTRINE

**Speaker `B` = "Father Bryan"**, locked at **three independent anchors**:

1. ⭐⭐ **`A` back-references `B`'s content by name.** `B` at **63:02–65:56**: *"a priest cannot pronounce absolution on repentance… the priest cannot withhold absolution from a penitent."* `A` at **69:12**: *"**and as Father Bryan was saying**, we don't get to say, oh, you're repentant? Too bad, I'm still binding you to your sin."* The back-reference matches `B`'s turn precisely.
2. ⭐ **`C` triangulates it.** `B` at 63:02 says *"if you look at **the rubrics to Communion**, I forget what page I was on."* `C` at **108:01**: *"when he referred to **the rubric**, I forget if it was **Brian or you**."*
3. **`A` addresses Father Brian as present in the room** at 50:04, and `B`'s sustained clerical first-person register begins 2½ minutes later at 52:53.

⛔⛔ **THE CORPUS CURRENTLY UNDERSTATES THIS.** `St_Francis_EMC_Distinctives.md` L3050 reads: *"Clergy references (**"Father Brian"**) are **context only**."* **That was true of the undiarized captures and is now false of the room audio: Father Bryan is not a reference, he is a participant, and his ~6 minutes of substantive speech is doctrinal exposition on confession, absolution, the priest's faculties, and episcopal consecration — the very stretches `IP-31`…`IP-36` cover.** ⛔ **The line is NOT edited. A dated note is added beside it.**

### ✅ AND THE AUDIT CLEARS — ALL SIXTEEN FINDINGS SURVIVE, STATED PLAINLY BECAUSE A CLEAN RESULT IS A REAL FINDING

Every locatable load-bearing verbatim from `IP-24`…`IP-39` was matched against the new diarized rendering and its speaker read off. ⭐ **Every single one lands on speaker `A`. Not one lands on Father Bryan, and not one lands on any attendee.**

| Finding | Verbatim probed | Turn / time | Speaker |
|---|---|---|---|
| `IP-31` | *"look at what I wrote here"*, *"standard is perfection"* | 113 · 35:14 | **A** |
| `IP-31` | *"spiritual bank of heaven"* | 116 · 36:16 | **A** |
| `IP-31` | *"damned for the glory"* | 124 · 38:42 | **A** |
| `IP-32` | *"committed actual sins"*, *"blessed virgin"*, *"our formularies"* | 139 · 42:02 | **A** |
| `IP-33` | *"none must"*, *"refreshed"*, *"deacon can[’t hear]"* | 175 · 50:45 | **A** |
| `IP-33` | *"regain your justification"* | 67 · 21:42 | **A** |
| `IP-33` | *"back to your baptism"* | 166 · 48:32 | **A** |
| `IP-34` | *"forgiving any sins"*, *"in my own power"* | 218 · 68:27 | **A** |
| `IP-34` | *"establish rite[s] … ceremonies"* | 220 · 69:12 | **A** |
| `IP-35` | *"necessary result"* | 202 · 59:33 | **A** |
| `IP-35` | *"Ignatius"* | 226 · 74:18 | **A** |
| `IP-35` | *"ordained by other ministers"*, *"Donat[ism]"* | 228 · 75:05 | **A** |
| `IP-36` | Lord's-Day / Saturday stretch | 208 · 60:56 | **A** |

⭐⭐ **`IP-32` gains coverage it did not have.** It was logged *"`[S]`-SOURCED ONLY; `[R]` does not cover Article XV."* **This rendering covers Article XV in full at turn 139 (42:02–42:52), speaker `A`** — the Immaculate Conception material now has room-side substrate for the first time. ⛔ **The finding is NOT edited; the coverage upgrade is reported.**

⭐ **The corpus's existing attendee assignments are independently CONFIRMED**, one by one, against the diarization: the genetic-code comment → `D`; *"I take issue with your statement, we desire to sin"* → `D`; the final-justification questions → `C`; the treasury-of-merit questions → `C`; the crucifix question → `E`. **L3050's speaker discipline was right.**

⚠️ **One reverse-direction impurity found and reported, not fixed:** turn **374 (107:25–107:44)** merges a short cross-talk exchange into label `A`. Chit-chat about supra/infralapsarianism; **no finding rests there.** Queued as **E3**.

⚠️ **One incidental ASR divergence, non-load-bearing:** `IP-35` records the Clement/Didache counter as *"deferred to the ordinal session"*; this rendering has *"when we get into the question of the prayer book and **the Lord's Prayer**."* Flagged for the quirk register; nothing rests on it.

---

## Tasks 1–5 — six flagged videos

### ⛔⛔⛔ `8nRhmD4w-Wg` and `9Fezj9WMh3A` (Fr. Ray) — NOT REV. JAMES. NOT MINABLE FOR HIS POSITIONS.

The brief anticipated that *"Rev. James [may be] present only as host or introducer."* **The finding is stronger than that: he is not identifiable in either file at all.**

**Speaker `A` is Fr. Ray**, and he is speaking for the entire teaching duration (39.3 min and 34.7 min). Anchors, from the recordings' own content:

- `FrRay-Eucharist` **21:41**, speaker `B`: ***"Thank you, Fr. Ray."*** *(byte 22,545)*
- `FrRay-OtherSacraments`: ***"when the bishop laid hands on me and prayed, make … Ray a priest in the Church, I became a priest in the Church, and I will die a priest in the Church"*** *(byte 18,229)*
- `FrRay-Eucharist`: *"this is your time with Jesus, **this is not your time with Ray**"* · *"it's **Ray's** magical act"* · *"the bishop calls me. **Fr. Ray?**"* · *"he goes, hey, what are you doing next week, **Ray**?"* · *"the musician said to me, you know, **Ray**…"*
- `A` narrates **his own conversion and ordination** in the first person, as Ray, at length in both files.

⭐⭐ **Independent structural confirmation from the inventory dates: 2017-07-06 and 2017-07-14.** Rev. James was **a deacon in 2020** (`File 55` @13,921, *"a deacon as I am"*, 2020-03-28). **A man narrating his own priesting in 2017 cannot be him.** Two independent lines, agreeing.

**Speaker `B` in both files is a COLLAPSED ATTENDEE LABEL** — 1.9 min / 323 words over 42 turns, and 0.8 min / 142 words over 31 turns; average 7.7 and 4.6 words per turn. Short interjections and questions from a live parish class, merged into one label. Decisive: `B` at 11:03 says ***"Father, I have a question."*** ⛔ **This is the `File 49` (`TeachingTheMass`) shape: single-label-not-single-voice.**

⛔⛔ **CONSEQUENCE: if Rev. James is present as host, he is inside the collapsed `B` label and is UNRECOVERABLE from content.** Neither file may be mined for his positions, and neither may be used as a speaker warrant. ⭐ **Registered anyway**, on the `File 53` precedent — the registration IS the record of the exclusion, and prevents a future pass re-pulling them as his.

⭐⭐ **A GENERALISABLE RULE FALLS OUT AND IS WORTH MORE THAN THE INSTANCE: `EXT-2` IS HIS CHANNEL BUT IS NOT A SPEAKER WARRANT.** His channel demonstrably hosts other men's teaching, uploaded under his account. ⏳ **Owed as an `ORCHESTRATION.md` §8 amendment; NOT written by this pass.**

### ⛔⛔⛔ `DavM_5hcN0w` (Response to Pastor Mike Winger on Infant Baptism, 2020-07-19) — SPEAKER `B` IS MIKE WINGER

⭐⭐⭐ **AND SPEAKER `A` SELF-IDENTIFIES BY NAME, THE ONLY FILE IN THIS PASS THAT DOES:** byte **0** and byte **79,605** — ***"I am Brother James, and this is the first sort of official YouTube … video for the Barely Protestant … YouTube channel."*** He opens and closes with it. **`A` = Rev. James, established by direct self-identification.**

**Speaker `B` (30 turns, 2,296 words, 11.4 minutes) is Pastor Mike Winger, heard via clips played from Winger's own video.** Three independent anchors:

1. ⭐⭐ **78:57, `B`: *"**Barely Protestant says**, where does scripture say women can receive communion…? Also, would you be willing to have a brotherly debate on it? **No, I'm sorry** … I've had 3 or 4 debate offers in the last week."*** — `B` is **reading out and declining** a question submitted by Rev. James's own channel. `B` is answering him, not being him.
2. **71:35, `B`: *"a brief word on church history. **This is part 5, part 5**, and then we're gonna go to **your guys' questions**."*** — `B` is running the structure of *his own* video and addressing *his own* audience.
3. **58:10, `B`: *"Maybe someone who knows this line of reasoning better than I do could **put that in the comments** and enlighten us."***

⭐ **Reciprocal confirmation:** `A` says at the top, *"I was actually part of the livestream when it first happened, **and I asked a question** which we will get to in a bit"* — and `B` at 78:57 reads out exactly that question. **The two halves lock.**

⛔⛔ **THIS IS A LIVE `GV-50` HAZARD OF THE FIRST ORDER.** A flat read of this transcript attributes 11.4 minutes of Baptist anti-paedobaptist argument to an Anglican priest who is refuting it — including *"I start to go, I'm confused by this"* and *"it starts to get a little weird to me"* about the covenant-community argument **that Rev. James holds**. ⛔ **Registered with a hard NON-QUOTABLE marker on label `B`.**

### ⚠️ `IGNmKMXhL1Q` (Morning Prayer, 5th Sunday in Lent, 2020-03-29) — UNRESOLVED, EAR-CHECK E2

Two labels: `A` 19.2 min (the office), `B` 5.3 min — **and `B` preaches the homily** at 14:45–18:18 and 18:26–19:08.

⛔ **I cannot determine from content whether this is two men or one man split by register.** The reason is specific and worth recording: **label `B` carries the congregational response (*"Thanks be to God"*, 06:36 and 09:14) AND the officiant's own versicle (*"The Lord be with you"*, 20:09) AND the homily.** No single liturgical role does all three. Either the diarizer split one voice at the office/preaching register change, or roles are shared in a way the audio would make obvious instantly. **The labels alternate with perfect regularity (19 turns each), which is itself weak evidence for a split-of-one.**

⭐ **Two positive by-products, both real:**
- ✅ **The `260835-10` triage decision is VINDICATED.** That pass `INCLUDE`d this row specifically because the title reads *"(with a Homily)"*, treating the homily as a teaching component against the new `EXCLUDE-office` category. **The homily is real and substantial — 3.5 minutes of genuine preaching** (*"We live in a fallen world… a serious disease plaguing the entire world, stores closed, businesses folded"*). The judgment call was right.
- ⭐ **Independent dating corroboration.** The homily's COVID content fixes it to Lent 2020, and the 5th Sunday in Lent 2020 is **2020-03-29**, matching the inventory date exactly and sitting **one day after** `File 55`'s *"a deacon as I am"* (2020-03-28).

⚠️⚠️ **A CHECK AGAINST `File 55` WAS ATTEMPTED AND DOES NOT SETTLE E2 — REPORTED AS A FAILED TEST, NOT QUIETLY DROPPED.** `File 55` (`2019BCP-MorningPrayer`, `xySXFYRQ9tI`, **2020-03-28**, the very next day) looked like a decisive comparator: same office, same book, registered `['A']` and **inside JD's ear-verification warrant as single-speaker.** ⛔ **It is not comparable, because it is not the same kind of act.** Reading it directly: `File 55` is an **instructional walkthrough about HOW to say Morning Prayer**, not a celebration of it — *"they're going to say, the word of the Lord, and **we respond**, thanks be to God"* · *"the officiant will turn and say, the Lord be with you. **And with thy spirit. Is the response.**"* · *"Then the officiant says, let us bless the Lord. **Response:** thanks be to God."* **One man narrating both parts — which is exactly why it is single-speaker, and why JD's ear heard one voice.** `IGNmKMXhL1Q` is an actual office with a homily. **The comparison proves nothing about `File 60` and E2 stands.**

⭐ **Two things it DOES yield.** (a) ⭐⭐ **A by-product about `File 55` itself: it is registered *"⛔ NONE — REGISTERED BUT UNMINED"*, and it is a substantive teaching video on liturgical practice — a better mining candidate than its row suggests.** ⏳ Flagged, not mined. (b) **[Stated-Analysis]** He was **a deacon on 2020-03-28** and teaching this office; a deacon officiating Morning Prayer alone the next day would read the responses himself and preach — which **leans toward** `File 60` being one voice split by register. ⛔ **An inference, labelled as one; it does not discharge E2.**

⛔ **Not minable pending E2.**

### ⛔ `hDRmWM5Nkgw` (Anglican 101, Session 1: Our History, 2021-06-15) — ATTRIBUTION NOT ESTABLISHED, EAR-CHECK E1

Same shape as the Fr. Ray files: `A` = teacher (54.1 min), `B` = **collapsed attendee label** (0.9 min / 142 words over 36 turns; short answers — *"Protestant."*, *"It's Anglican."*, *"Albino."* — plus two real questions). ⛔ **So "2 speakers" here does not mean a two-voice recording; it means one teacher plus one merged attendee label.**

⚠️ **First: this is NOT a duplicate of any registered session.** Dated **2021-06-15**, it belongs to an **earlier run** of Anglican 101, distinct from the 2026 run (`A101-2026-06-14` … `08-23`). No collision.

⛔⛔ **The teaching voice cannot be identified from content.** No self-identification, no direct address by name, no biographical anchor unique to Rev. James in 54 minutes.

⭐ **What the evidence DOES support, labelled as inference and not as identification:** the voice is **strongly consistent** with him — *"I was looking at Eastern Orthodoxy before I became Anglican"* (a convert biography compatible with `IP-35`'s Baptist exit); a closely matching idiolect (the *"some will say X, some will say not-X"* triadic construction, the self-interrupting asides); and the **identical class-opening ritual** (*"The Lord be with you / And with thy spirit / Let us pray"* + a collect) that `6Z68nITG1Is` and `GeWfXTAjFDo` both use. **[Stated-Analysis]**

⛔⛔ **BUT INFERENCE IS NOT A WARRANT, AND THIS PASS HAS JUST PROVEN WHY: the same channel hosts Fr. Ray's classes.** The class-opening ritual is a practice any Anglican priest shares. **Registered with attribution OPEN; nothing mined.**

### ⛔⛔ `6Z68nITG1Is` (Anglican Class, Session V: Articles of Religion, 2026-08-10) — THE BRIEF'S HYPOTHESIS IS FALSIFIED

⭐⭐⭐ **SPEAKER `A` IS ESTABLISHED BY DIRECT ADDRESS, BY NAME** — the only such anchor in the six videos: at **03:15**, speaker `E` says ***"Sorry, Father James is trying to start"*** *(byte 293)*, immediately before `A` resumes at 03:18. **`A` = Rev. James.**

⛔⛔ **AND THE SIX-WAY SPLIT IS NOT OVER-FRAGMENTATION. IT IS SIX REAL PEOPLE.** The brief instructed me to *"treat the six-way split as likely over-fragmented, not as six real distinct speakers."* **The content does not support that and I am reporting rather than complying.**

| Label | Min | Who, from the recording's own content |
|---|---|---|
| **A** | 76.9 | **Rev. James** — named at 03:15 |
| **B** | 2.2 | ⭐⭐ **The genetic-code interlocutor** — *"every generation has added to our genetic material. That it's code"*; the 8-o'clock-alarm/two-eggs habit analogy applied to predestination |
| **C** | 1.7 | ⭐ **An ONLINE participant** — *"**I've never been to your church building**, so I don't know if you have any crucifixes"* |
| **D** | 4.0 | ⚠️⚠️ **A SECOND LEARNED TEACHING VOICE** — delivers a considered Anglican position on invocation of the saints at length (*"The Reformation problem with the invocation of the saints is not… The problem [is]"*), recommends a book, speaks of *"our dealing with the Reformation"* |
| **E** | 6.4 | Questioner-explainer — the ride-home analogy for invocation; a ceremony/retrieval point |
| **F** | 2.8 | ⭐ **A ROMAN CATHOLIC participant** — *"Those are the main points **from my tradition** towards purgatory being a thing… So why is it that the Anglican tradition outright r[ejects]"* |

⭐⭐⭐ **Three of the six are corroborated by in-recording events, not just by persona:**
- **`F`** is the *"Vatican agent"* `A` jokes about at **04:07** (*"You should let them know that a Vatican agent is here"*).
- **`C`**'s never-visited status is stated in his own words — a livestreamed class with remote questioners, which is *why* the speaker count is high.
- ⭐⭐ **`B` IS THE SAME MAN AS SPEAKER `D` IN THE `A101-20260726` ROOM RECORDING** — the identical genetic-code-and-original-sin hobby-horse, in the same register, in both. **A cross-recording persona match, independently derived.**

⛔⛔ **AND THE BRIEF'S STATED GROUND FOR THE SUSPICION IS FALSE AS DESCRIBED.** The brief says *"the room twin of that same session already has a documented calibration failure (word-level splice check failed its own calibration)."* What is actually documented, at `St_Francis_EMC_Distinctives.md` **L206**, concerns `A101-2026-08-09`'s room capture and reads: *"`B` is still not a synonym for Rev. James: label `B` also carries the purgatory questioner (887, 892), a question put TO the teacher (937), and **both halves of the calibration merge (1394)**"*, with guard 2 being *"the falsified splice detector."*

⭐⭐ **That is a MERGE — too FEW labels, one label carrying several people — which is the OPPOSITE defect from over-fragmentation.** Reasoning from it to a suspicion of over-splitting runs the inference backwards. **Both the direct content evidence and the correctly-read precedent point the same way: the six labels are six people.**

⛔⛔ **A SECOND PROBLEM WITH THE BRIEF'S PREMISE: "the room twin of this same session" IS NOT ESTABLISHED.** `SRC_Manifest.md` L520, the `A101-2026-08-09` stream row, says in terms: ***"⏳ POSSIBLE FUTURE CAPTURE — FLAGGED ONLY. NOT PULLED, AND ITS EXISTENCE IS NOT ESTABLISHED… Do not read this row as a known source."*** And the inventory dates `6Z68nITG1Is` to **2026-08-10**, not 08-09.

**What the content shows:** Session V covers predestination and original sin, then images and the second commandment, purgatory, and invocation of the saints — i.e. **Articles XVII–XXII**, with Article XXII (*"Of Purgatory"*, which treats purgatory, images and invocation of saints together) accounting for the whole back half. `A101-2026-08-09` is registered as Article XVII **plus Lent, the church calendar, fasting, communion admission and the rosary**, running 4h 20m against this file's 97.6 min. **Overlap at Article XVII; divergence after it.**

⛔⛔ **I am NOT asserting these are the same event, and NOT asserting they are different.** Per the `260833-3` standard — *same event ESTABLISHED, not assumed* — and per the manifest's own explicit warning on that row, **no dual-capture row is created.** ⏳ **OWED: settle it by comparing this transcript against the `A101-2026-08-09` room capture directly.** (That capture is not present in readable form under `in person classes/20260809/`, which holds only pass artifacts — so the comparison needs the capture pulled first.) ⛔ **Until it is settled, mining this file risks re-mining `IP-45`…`IP-68` — the `260835-4` error exactly.**

⚠️⚠️ **AND SPEAKER `D` IS A FATHER-BRYAN-CLASS HAZARD, REGISTERED AS SUCH:** 4.0 minutes of substantive doctrinal exposition by a second authoritative voice inside a class otherwise attributed to Rev. James.

⭐ Incidental datable anchor for whoever settles the twin question: at 00:18 `A` says *"I'm off through the 24th, so I can't even relax on my **paternity leave**."*

---

## Task 6 — `GeWfXTAjFDo` (Revelation Class, Session XVII, 2026-08-17)

⛔⛔ **THE BRIEF'S CAUTION IS VINDICATED, AND THE RESULT IS STRONGER THAN "UNCONFIRMED-SOLO": IT IS POSITIVELY NOT SOLO.**

The file is **one single turn** — 4,872 words, 31.2 minutes, one label. **Participant voices are demonstrably inside it:**

- ⭐⭐ ***"Does that make sense? **Can you expound on that a little bit more?** All right, um, so right now— I'm sorry, not between now…"*** — **a participant's request, swallowed into the teacher's label.** A teacher does not ask himself to expound and then apologise.
- ***"the Lord be with you. **And with thy spirit.**"*** — the congregational response, inside the label.
- ***"any questions before we move on to letter C? All right, so this is number 2. **Yeah.**"***
- ***"Are there any final questions before we close off? **No.** All right, thank you all very much."***

⛔ **This is the `File 49` / `TeachingTheMass` pattern exactly: single-LABEL, not single-VOICE.** It must not be used as a speaker warrant, and any future quotation from it must be register-checked sentence by sentence.

✅ **`A` = Rev. James**, established by **role self-identification**, on the same standard `260818-3` used for `A101-2026-08-09` segment 2: *"postmillennialism, **the belief that we have here at the church, at St. Francis**"*, and he sets the parish's adult-formation direction — *"it's going to help me know what… I'll look at that and take that into account of what we'll be going into next for adult formation."*

---

## §7 — Mining: what was done, and why NOTHING was minted

The brief authorises targeted mining *"where attribution is settled."* Attribution is settled for four of eight artifacts. **No finding was minted from any of them, and each refusal has its own reason:**

| Artifact | Attribution | Why nothing minted |
|---|---|---|
| `A101-20260726` room | ✅ settled | ⛔ **Already mined** as `IP-24`…`IP-39` at `260809-1`. Re-mining is the `260835-4` error. This is a substrate recovery and verification pass, the `260835-11` model. |
| `8nRhmD4w-Wg`, `9Fezj9WMh3A` | ✅ settled — **NOT HIS** | Nothing of his to mine. |
| `DavM_5hcN0w` | ✅ settled | See below — **material located, not minted.** |
| `6Z68nITG1Is` | ✅ settled (speaker) | ⛔ Session identity vs `A101-2026-08-09` unresolved; mining risks re-mining `IP-45`…`IP-68`. |
| `GeWfXTAjFDo` | ✅ settled (speaker) | ⛔ Confirmed collapsed-label file; and `RV` de-duplication could **not** be established to the `260835-4` standard (see below). |
| `hDRmWM5Nkgw`, `IGNmKMXhL1Q` | ⛔ **NOT settled** | The brief forbids mining before attribution resolves. |

**De-duplication probe, run on the `260835-4` method (source-file names AND the changelog, not titles alone).** All seven video IDs and their transcript basenames were grepped repo-wide: **none appears in `St_Francis_EMC_Distinctives.md` or `SRC_Manifest.md`** — only in `SRC_Channel_Inventory.md` and in triage close-outs (`260835-10`, `batch9-selection_260826`). ⚠️ **This is reported as a probe result, NOT as a clean de-duplication.** `260835-4`'s lesson was that a probe can return a true negative on the wrong index; the `RV` batch's internal locator scheme was not reconstructed this pass, so **`GeWfXTAjFDo`'s independence from `RV-1`…`RV-63` is UNVERIFIED, not verified.**

### ⭐⭐ Targeted mining of `DavM_5hcN0w` — one real datum, LOCATED AND NOT MINTED

**Term scan against the standing questions, speaker `A` only** (labels separated first, so Winger's words could not contaminate the count): `regulative` **0** · `warrant` **0** · `approved example` **0** · `necessary inference` **0** · `element` **0** · `circumstance` **0** · `incense` **0** · `altar` **0** · `sacrifice` **0** · `real presence` **0** · `eucharist` **0** · `burden` **0** · `ceremon` **0** · `adiaphora` **0** · `indifferent` **0** · `normative` **1** ⚠️ *(false positive — "infant baptism as a normative practice in the 2nd century"; historical frequency, not RPW vocabulary)*.

⭐ **So `DQ-24`, `OQ20`/`OQ21`, element/circumstance, and eucharistic presence and sacrifice draw a complete blank. Reported as a clean negative.**

⭐⭐⭐ **BUT THE BURDEN-OF-PROOF MATERIAL IS PRESENT, AND IT IS THE MOST VALUABLE THING IN THE SEVEN FILES.** Speaker `A`, 2020-07-19:

> *"nowhere does Scripture say infants can no longer be marked as part of the family of God. We do not see that in Scripture. So the point is that that practice was **never abrogated**"* — bytes **48,583** and **48,708**

> *"Why does he think that that has changed today? ***He has to demonstrate that it has changed.***"* — byte **53,308**

⭐⭐ **This is the SAME RULE as the `260835-4` recording-5 burden rule** (*"if that restriction is going to be added it needs to be demonstrated within Scripture"*, stated four times, 2020) **and as `DQ-19`'s 2026 statement — here on a THIRD, independent occasion, on a different topic (infant baptism, not baptismal repentance), in the same year.** The attestation is broader than the corpus records.

⛔⛔ **AND THE SAME TWO-WAY CAVEAT `260835-4` RECORDED APPLIES AND IS RECORDED AGAIN: the rule is stated here about a practice with EXPLICIT COVENANTAL WARRANT (circumcision → baptism, the Abrahamic covenant). Whether incense qualifies is the contested question itself. It cuts both ways and is recorded both ways. NOT logged as supporting the incense lever.**

⛔ **NOT MINTED.** Whether this is a new finding or a corroboration of the `260835-4` datum and `DQ-19` is a numbering judgment sitting on an area JD has already flagged as unresolved — the `260835-4` precedent is to locate and hand over, not to mint into it. **Byte ranges are registered so a minting decision costs nothing.**

---

## §8 — Registrations: `File 56` … `File 63`

⭐ **A distinction this pass relies on and states openly: REGISTRATION IS NOT A SPEAKER WARRANT.** Two artifacts (`File 61`, `File 60`) are registered with attribution **OPEN**. The alternative — leaving pulled artifacts unregistered until attribution resolves — recreates the exact `RC`-batch problem `260835-11` spent a whole pass repairing (material with no File number, no hash, no locatable source). The `File 49` precedent already separates the two: registered, hashed, locatable, **and explicitly not usable as a speaker warrant.**

| File | Artifact | Bytes | sha256 | Attribution | Minable? |
|---|---|---|---|---|---|
| **56** | `A101-20260726-transcript.txt` (room, diarized re-render) | 100,141 | `087a8314…` | ✅ `A` = Rev. James · ⛔ `B` = **Father Bryan, 2nd priest** | ⛔ already mined `IP-24`…`IP-39` |
| **57** | `Response-Winger-InfantBaptism-transcript.txt` | 79,964 | `64894db9…` | ✅ `A` = Rev. James (**self-ID**) · ⛔⛔ `B` = **MIKE WINGER, NON-QUOTABLE** | ⚠️ `A` only; material located §7 |
| **58** | `FrRay-Eucharist-transcript.txt` | 43,490 | `dccb76a6…` | ⛔⛔ `A` = **FR. RAY** · `B` = collapsed attendees | ⛔⛔ **NOT HIS** |
| **59** | `FrRay-OtherSacraments-transcript.txt` | 37,148 | `f0285ba5…` | ⛔⛔ `A` = **FR. RAY** · `B` = collapsed attendees | ⛔⛔ **NOT HIS** |
| **60** | `MorningPrayer-5thSundayLent-transcript.txt` | 18,369 | `78cdf0e2…` | ⚠️ **OPEN — one voice or two? (E2)** | ⛔ pending E2 |
| **61** | `A101-Session1-OurHistory-transcript.txt` | 48,948 | `909fd89e…` | ⛔ **OPEN — teaching voice unidentified (E1)** | ⛔ pending E1 |
| **62** | `Anglican-SessionV-ArticlesOfReligion-transcript.txt` | 88,110 | `34a578c4…` | ✅ `A` = Rev. James (**named, 03:15**) · ⚠️ `D` = 2nd teaching voice · 6 real speakers | ⛔ session identity open |
| **63** | `Revelation-SessionXVII-MillennialReign1-transcript.txt` | 26,381 | `aa243a3f…` | ✅ `A` = Rev. James (role self-ID) · ⛔ **collapsed-label, NOT solo** | ⛔ `RV` de-dup unverified |

**Next free File is now `File 64`.**

⛔⛔ **NO OTHER NUMBER CONSUMED. Next free values re-derived and unchanged: `DQ-25`, `IP-109`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EXT-4`, `W47`.**

---

## §9 — What was NOT touched

⛔ **`Incense_Conversational_Outline.md` and `RJ_Incense_Analysis.md` NOT touched.** ⛔ **Nothing drafted, altered or posted to Rev. James.** ⛔ **No existing finding altered, renumbered, re-pointed or corrected** — including `St_Francis_EMC_Distinctives.md` **L3050**'s *"Clergy references… are context only"*, which this pass shows to be superseded by the room audio and which is **flagged beside, not edited**. ⛔ **No byte offset in any existing entry altered.** ⛔ **`SRC_Manifest.md` L517's `96a9c5a9` `[R]` row NOT overwritten.** ⛔ `DQ-9` unmoved · `DQ-24` untouched · no Discord state touched. ⛔ **`validate_project.py`, `RJ_Final_Question_List.md`, `RJ_Open_Questions_and_Divergences.md`, `On_Incense_and_the_Altar.md`, `ORCHESTRATION.md`, `SRC_Coverage_Register.md` NOT touched.**

## §10 — Owed

⏳ **E1 and E2** (blocking) · ⏳ **E3, E4, E5** (confirmations) · ⏳ Recovery of the original `96a9c5a9` `[R]` markdown · ⏳ Settle whether `6Z68nITG1Is` is the `[S]` twin of `A101-2026-08-09` (requires pulling that room capture) · ⏳ JD's ruling on the `DavM_5hcN0w` burden-rule datum: new finding or corroboration · ⏳ **`ORCHESTRATION.md` §8 amendment: `EXT-2` channel ownership is NOT a speaker warrant** — the Fr. Ray result · ⏳ Reconstruct the `RV` locator scheme to de-duplicate `File 63` properly.

*(§5 rule 11 — this note makes no claim about its own commit state.)*
