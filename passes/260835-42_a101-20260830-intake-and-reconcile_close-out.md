# 260835-42 — `A101-2026-08-30` INTAKE AND RECONCILE

**The in-person prayer-book class registered as `File 85` and mined: `IP-109`…`IP-125`, seventeen findings, unbroken.**

⭐⭐⭐ **HEADLINE: JD's report holds, and by a wide margin. `[58:02]`→`[157:03]` — roughly 100 minutes and ~240 occurrences of the term — is the largest single body of incense material anywhere in this corpus.**

⛔⛔⛔ **SECOND HEADLINE, AND THE BRIEF'S WARNING WAS CORRECT: the `speakers_detected: ['A','B']` result is a MERGE, not a count, and it is rejected from the recording's own content on five independent markers.**

---

## 1. Gate

| Item | Value |
|---|---|
| **HEAD at gate** | `ce511846eb4d4909e61274849656eb60c4c95dbc`, branch `main` |
| **HEAD verified how** | ⭐ The brief named no expected HEAD. Verified against where `260835-41` left the repo on **three agreeing checks**: `PROJECT_STATE.md`'s own stamp read `260835-41`; `ls passes/` topped out at `260835-41`; `git log -1` **is** the `260835-41` commit (*"260835-41: DQ-27 minted…"*, 2026-08-30 12:18:50 -0400) |
| **`git --no-optional-locks status --short` before first edit** | ⭐ **EMPTY.** Captured directly, not reconstructed. Every git read in this pass used `git --no-optional-locks`, per the `260835-3` FUSE-lock diagnosis |
| **`PROJECT_STATE.md` stamp at gate** | **`260835-41`** |
| **Validator BEFORE** | **`84 ok · 9 warnings · 0 errors`** |
| **Next-free pass stamp** | **`260835-42`** — derived fresh by grep, hazard note read first |
| **Next-free `IP` at gate** | **`IP-109`** — re-derived fresh. ⭐ **CONSUMED, `IP-109`…`IP-125`** |
| **Next-free `File` at gate** | **`File 85`** — re-derived fresh. ⭐ **CONSUMED** |

### Validator BEFORE — every firing code, in full

| Code | Where | What fired |
|---|---|---|
| `C1` ×1 | `src/SRC_Discord_RPW.md` | 2 relative timestamps outside message headers (*"Yesterday at …"*); not caught by the header rule |
| `C3` ×2 | `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` · `tools/transcribe_yt.py` | No parseable `Last updated` stamp; registry says `260832-2` / `260833-7` |
| `C4` ×1 | `St_Francis_EMC_Distinctives.md` | 2 passages describe an ANSWERED question as pending with no supersede marker nearby |
| `C5` ×3 | `RJ_Final_Question_List.md` (17) · `RJ_Incense_Analysis.md` (9) · `St_Francis_EMC_Distinctives.md` (7) | Volatile-state assertions; consider pointing to `PROJECT_STATE` |
| `C10` ×1 | §15 | Newest LS citation 21 findings behind the ledger (`LS-120` vs `LS-141`) |
| `C11` ×1 | `Incense_Conversational_Outline.md` | Outline last checked against `DQ-26` (`260835-31`); the DQ ledger now runs to `DQ-27`; 1 finding unreviewed |

⭐ Codes `C2`, `C6`, `C7`, `C8`, `C9`, `C12` all returned **OK**.

### Stamp derivation — fresh by grep, hazard note read FIRST

⭐⭐ **The `260835-12`/`260835-14` hazard note was read before the sweep, as the brief required.** Both re-confirmed **REAL and CONSUMED** (commits `530d987`, `68bf1d8`); neither in play at this end of the range.

**Derivation actually run:** a distinct-stamp sweep over tracked `*.md`/`*.py`/`*.txt` (`git ls-files` piped to `grep -hoE '\b26[0-9]{4}-[0-9]+\b'`) returns an unbroken run **`260835-1 … 260835-41`**, no gaps. `ls passes/`, numerically sorted, tops out at `260835-41`. `git log --all` tops out at the `260835-41` commit.

⚠️ **`260835-42` returned exactly ONE repo-wide hit, and it was opened and read in context rather than treated as a consumption.** It is the `260835-41` gate note's own forward assertion in `PROJECT_STATE.md` L7 — *"`260835-41` returned ZERO matches repo-wide … `260835-42` and above return zero"* — carried into `passes/260835-41_….diff` as the same line. **Checked, not assumed.**

⚠️ **`260835-99` re-checked in context and re-confirmed NOT a stamp** — the upper endpoint of an absence-assertion range inside earlier close-out prose. ✅ **`260835-43` and above return zero.**

### `IP-109` and `File 85` re-derived free before consumption

⛔ **Not assumed from the registry.** Every `IP-109` occurrence repo-wide was read in context: every one is a next-free assertion or a close-out's re-derivation (`260835-3`, `260835-14`, `260835-18`, `260835-19`, `260835-20`, `260835-26`, `260835-28`, `260835-4`), **none a minted entry.** `IP-110` and above: zero.

Same for `File 85`: every occurrence is a next-free assertion (`SRC_Manifest.md` L19/L2117, `passes/260835-38`, `passes/260835-39`). `File 86` and above: zero.

---

## 2. The source

| | |
|---|---|
| **Session** | `A101-2026-08-30` — the in-person prayer-book class |
| **Class date** | **2026-08-30**. ⭐ Transcript generated **2026-08-31** (`generated_utc: 2026-08-31T17:30:13Z`) — **recorded separately per the established convention and NOT used as the source date** |
| **Duration** | 9,976 s = **2:46:16** (the brief said 166m 16s — ✅ exact) |
| **Artifacts** | **Five** (the brief said five — ✅): `-sentences.json`, `-timestamps.json`, `-transcript.srt`, `-transcript.txt`, `-meta.json`, plus the source audio `output.mp3` |
| **Input mode** | `local_audio`. `source_url: null` · `youtube_captions: null` — ✅ **the brief's "no YouTube captions (local recording)" confirmed from the meta file, not assumed** |
| **Sentences** | 2,561 · **925 turns** · `A` 6,702 s / `B` 2,394 s of word-time |

✅ **ARTIFACT INTEGRITY — 5/5 EXACT, ZERO DIVERGENCE.** All four `outputs` entries verified fresh against disk on both `bytes` and `sha256`, **and** the `source_audio_file` digest (`output.mp3`, 79,800,546 B, `2a609356…`).

⚠️ **A trap in the meta file, recorded so no later pass falls into it: `-meta.json` carries TWO different audio digests.** `source_audio_file.sha256` = `2a609356…` (79,800,546 B, the source) and `audio.sha256` = `00571531…` (81,447,888 B, 64k/16 kHz mono — the **downsampled working copy sent to the ASR**). ⛔ **Neither is the hash of any transcript.** The registered `-transcript.txt` raw-bytes digest is `826d4527…`, per the registration convention.

---

## 3. ⛔⛔⛔ Speaker identity — the two-label count is falsified

**The brief instructed this pass not to accept the two-speaker count. It was right to.**

⭐⭐ **A new warrant class is named for reuse: `TWO-LABEL, NOT CONFIRMED TWO-VOICE`** — the `260835-15` single-label class extended one notch. Same mechanism (diarization under-detects in a live-class format), same remedy (check the file's own content for participant-address markers before treating a label as a person).

### The five markers — each independently sufficient, all byte-verified

| # | Marker | Sentence · speaker · time · byte range |
|---|---|---|
| 1 | ⭐⭐⭐ *"I, I have— **you both** have a good sense, but this is okay."* — **two addressees plus the speaker is three people, from his own mouth** | `s2469` · `A` · `[162:12]` · `@5,361,304–5,361,362` |
| 2 | ⭐⭐⭐ *"…well, no, it is an entirely— **by the way, y'all keep talking**— vision-wise…"* — **a side conversation the diarization does not separate** | `s2035` · `A` · `[137:10]` · `@4,494,761–4,494,927` |
| 3 | ⭐⭐ *"Yeah, we already— we already— I mean, **he agrees** with that."* — a third party in the room, third person; **not JD (he is answering JD) and not himself** | `s993` · `A` · `[78:44]` · `@2,465,562–2,465,624` |
| 4 | ⭐⭐⭐ *"Yeah, I think we'll take **Luke's** suggestion."* — the suggestion referred to is itself carried on label `B`; **either Luke's turn is inside `B`, or `B` credits a speaker the transcript never separates. Both readings defeat two-voice** | `s1545` · `B` · `[111:43]` · `@3,570,893–3,570,936` |
| 5 | ⭐⭐ Two further vocatives: *"**Chrissy**, she's got all kinds of literary niches"* (`s2506`, `B`, `[163:42]`); *"Well, **Matt**, Genesis is given as—"* (`s2403`, `B`, `[158:03]`, conf. **0.838**); *"…I thought I brought it with me, **Mike**"* (`s228`, `A`, `[17:54]`, conf. **0.531**) | as listed |

⚠️⚠️ **`Mike` at 0.531 is WEAK and is NOT relied on** — it is as likely *"man."* **It is recorded anyway, because suppressing a marker to keep a tidy count is the exact error this class of check exists to prevent.** `Matt` at 0.838 is stronger but also not load-bearing: **markers 1–4 carry the finding without either.**

### ⛔⛔ The sharper hazard: the merging is *within* turns

| Instance | Time | What it shows |
|---|---|---|
| `B` turn opens *"Are you concerned that people will stop praying?"* then answers it | `[90:51]` | The teacher's question inside the questioner's label |
| `B` turn contains *"Oh, so you mean since the Reformation?"* | `[62:30]` | Same |
| `B` turn contains *"oh, is that me? I don't know. **No, it's not me.** I don't know whose that is"* | `[141:11]` | **Two voices inside one turn on any reading** |
| `A` turn ends *"Are you using me as a reference?"* | `[145:03]` | Not the teacher's |

⛔⛔⛔ **THE OPERATIVE RULE, RECORDED AND BINDING: IN THIS FILE A TURN-LEVEL SPEAKER LABEL IS NOT A WARRANT. ONLY AN INDIVIDUALLY-CHECKED SENTENCE IS.** ✅ **Every one of the seventeen findings cites at sentence granularity; every cited sentence was byte-extracted from `-sentences.json`, confirmed unique in that file, and had its speaker read off one sentence at a time. Not one is inherited from a turn label.**

### ✅ What *does* establish the two principals

**`B` = JD — DIRECT ADDRESS BY NAME.** `s1178`, speaker `A`, `[88:22]`, `@2,788,563–2,788,726`: *"…rose before God from the hand of the **JD, do you object to the grain offering also, or just the incense?**"* ⚠️ **The sentence is itself a merge artifact** — his read-aloud of Revelation 8:4 runs into the question without a boundary — **but the vocative is unambiguous and `B` answers it in the next turn.** ⭐ Corroborated: `B` cites *"the 1899 article from the Archbishops of England"* and *"it's not my own research"* (the project's own `Ritualist_Case…` material); says *"I'm regulative"*; argues the reception case the `DQ` series records JD pressing; supplies personal biography (*"that's actually what we did at our wedding"*, *"my reformed grandfather"*, *"I went to a seminary"*).

**`A` = Rev. James — role self-identification + first-person biography matching the registered corpus.** Opens with the collect (`s0`); teaches throughout; *"the way that we do it at St. Francis"* (`s113`); *"I'm the one who's ordained to consecrate"* (`s138`); *"I'm literally not allowed canonically to celebrate communion by myself"* (`s1715`, `[121:39]`, `@3,913,209–3,913,280`); exercises rector-level authority over incense in the first person. ⭐⭐ **Independently corroborated against biography already held from other sources:** *"That is a description of at least the **Baptist** liturgy that I grew up in"* (`s31`, `@63,499–63,571`); *"Yeah, I grew up anti-Calvinist **IFB**"* (`s2527`, `@5,432,009–5,432,044`); *"My mother is a **King James Onlyist**, kind of"* (`s516`, `@1,296,260–1,296,303`) — matching `BP-20`/`BP-26`/`BLOG-78`/`BLOG-116`/`GV-31`.

⚠️ **NEW biography this source carries and the corpus does NOT corroborate, registered as new rather than as confirmation:** Cuban mother; *"Philly Polish and Italian"* paternal side; schooling in **Rutherford County**; a **615** (Nashville) area code. ⛔ **None used as a warrant.**

⛔⛔ **The warrant is bounded and says so: `A` and `B` are established as PRESENT AND SPEAKING, not as the sole occupants of their labels.** The five markers prove the opposite.

### ⛔⛔ Four `ATTRIBUTION OPEN` windows — flagged for JD's ear, nothing minted from any

| # | Window | What is open | Why it matters |
|---|---|---|---|
| **E10** | `[141:05]`–`[141:30]` | *"oh, is that me? … No, it's not me."* inside one `B` turn — **who are the two voices?** | Clearest within-turn two-voice instance; fixes the room's size directly |
| **E11** | `[111:35]`–`[112:15]` | The departure sequence — *"I appreciate you staying after"*, *"Luke's suggestion"*, *"I'm gonna stay in a while"*. **Who left, who stayed, is Luke a speaker or only a referent?** | ⭐⭐ **Highest value of the four.** Determines whether `[112:15]`–`[157:03]` — carrying `IP-115`, `IP-116`, `IP-120`, `IP-121` — is a clean two-person conversation |
| **E12** | `[93:24]`–`[95:12]` | ⚠️⚠️ `s1267` *"If I pray morning and evening prayer, I'll do it, um um—."* against `s1293` *"I don't practice that personally."* **Both `A`, 1m41s apart, same question (incense at home with prayer)** | ⛔⛔ **NOTHING MINTED FROM EITHER.** Mislabelling, truncation mid-qualification, or self-correction — **the corpus must not choose.** It is exactly the datum the allowed-vs-demanded question would most want, which is why it is left open rather than taken |
| **E13** | `[17:54]` · `[158:03]` | *"Mike"* (0.531) and *"Matt"* (0.838) — real names or ASR artifacts? | Would raise the established floor from three to four or five |

---

## 4. ⛔⛔ Two new defect classes

### (i) The `-transcript.txt` is NOT the concatenation of `-sentences.json`

Reconstructing the `.txt` by joining all 2,561 sentence texts with single spaces yields **166,716 bytes against the file's actual 166,597**, and **2,392 of the 2,561 sentences are not locatable verbatim in the `.txt` at all.** The cause: the `.txt` preserves AssemblyAI's raw `text` field; `-sentences.json` **re-capitalises at its own segmentation boundaries** (*"I'm just the first. **in** line"* against *"**In** line"*).

⛔⛔ **CONSEQUENCE: a byte offset into `-transcript.txt` CANNOT be converted to a sentence index by arithmetic, and a quotation verified against the `.txt` carries NO speaker label.** ✅ **`-sentences.json` is therefore PRIMARY and every citation is offset against it.** ⚠️ **Worked instance: `s1267` is present in `-sentences.json` and absent verbatim from `-transcript.txt`.**

⭐ **This was caught rather than assumed:** the first verification run produced sentence indices by cumulative arithmetic and mapped *"Well, Matt…"* to speaker `A`. **The correct speaker is `B`.** The arithmetic was discarded and every citation re-derived by direct match. ⛔ **Had the drift not been caught, at least one attribution in this pass would have been wrong.**

### (ii) ASR keyterm-prompt contamination

⛔⛔ The `-meta.json` `assemblyai_config.prompt` reads: *"In-person class session with **Rev. James Gadomski** as primary speaker, JD as primary questioner (especially on incense), and other participants."*

At `[61:12]`, speaker `B` produces the single word ***"Gadomski."*** (conf. **0.849**) — immediately after `A` says *"But people like— oh, I can't remember his name— James— Bishop James—"* about a **nineteenth-century Episcopal bishop**, and immediately before `A` says *"I can't remember his last name."*

⚠️⚠️ **The surname is in the ASR prompt and is almost certainly prompt-induced, not spoken.** ⛔⛔⛔ **REGISTERED AS A HAZARD, NOT ADJUDICATED** — a participant joking is also possible. **Either way the string `Gadomski` in this file is NOT a self-identification and must never be read as one.**

⭐⭐ **THE GENERAL RULE, RECORDED BECAUSE IT TRAVELS: a keyterm/prompt-biased ASR can manufacture exactly the name string a speaker-attribution check is looking for. Any future pass that finds a name in a transcript MUST check it against that source's own `assemblyai_config` prompt and `keyterms_prompt` before treating it as evidence.** ⚠️ Checked here: the 61 keyterms (from `asr_keyterms_A101.md`) are theological vocabulary and contain no personal names — **the contamination vector is the free-text `prompt` field alone.**

---

## 5. ✅ Father Bryan — confirmed absent

⭐ The brief required a positive check. **He is not in this session.**

**Search terms run, against both `-sentences.json` and `-transcript.txt`:** `Brian` **0** · `Bryan` **0** · `Father B` **0** · `Fr. B` / `Fr B` **0** · `Reverend` **0** · `Deacon` **0** · `Padre` **0** · `Curate` **0** · `Rector` **1** (and it is `B` naming the abstract office, not addressing anyone).

⭐⭐ **AND THE CHECK WAS NOT LEFT AT GREP, per `260835-1`'s zero-returns-while-present lesson.** A **register** sweep of the full 166 minutes was run for a second clerical first-person voice — the marker that caught him at `File 56` (*"a priest cannot pronounce absolution on repentance"*). **There is exactly one clerical first-person register in this file and it is `A`'s.** Label `B`'s register is lay throughout — wedding, grandfather, seminary-as-student, *"our church"*, *"I grew up Reformed."*

✅ **Absent on two independent tests, name and register.** ⛔ **Recorded as a fact about THIS session and expressly not generalised** — `File 56` has him present and speaking at 2026-07-26 and that stands.

---

## 6. The mining — against the frames the brief named

⭐ **Dating fact, recorded and not built on: `DQ-27` was minted from a Discord message posted 2026-08-29, 11:28 PM. This class was recorded 2026-08-30.** ⛔ **The corpus does not claim the class continues the thread, that either party had the other in mind, or that anything here was prompted by anything there.**

| Frame the brief named | Result |
|---|---|
| **`DQ-24`'s five-level ordering** | ✅ **PRESENT** — `IP-113`. He invokes it as *"that uh **5 or 6 order that I gave**, which was the Scriptures first"* (`s763`). ⚠️ **The referent of *"that I gave"* is NOT established and NOT guessed.** ⚠️ **The *"5 or 6"* is his and is recorded exactly; no sixth level is inferred** |
| **`DQ-25`/`DQ-26`/`DQ-27` reception criterion, applied to incense** | ✅ **PRESENT** — `IP-117` (reception + innovation antonym against a live proposal; ⭐ `Restorationist` is **new to the corpus**, 0 prior occurrences), `IP-112` (level (2) in two weaker spoken forms), and ⭐⭐⭐ **`IP-111`, the first-three-centuries concession** |
| **Allowed-vs-demanded (levels 1–3 permit but do not require; the Rector establishes it as normative)** | ✅✅ **PRESENT AND THE FULLEST STATEMENT IN THE CORPUS** — `IP-118`, both halves, thirteen minutes apart in one conversation. `IP-109` puts incense *below* the threshold needing episcopal approval at all |
| **Malachi 1:11 in any form** | ✅✅ **PRESENT IN BULK** — `IP-119` (read aloud in full **twice**, from two different translations, with the three-stage argument and ⭐ *"Will means command"*, **0 prior corpus occurrences**) |
| **⚠️ Cross-reference `IP-98`** | ✅ **DONE AND DELIBERATELY NOT ADJUDICATED** — `IP-114`. He identifies the grain/pure offering as **the Eucharist**, *"literally done today"*; `IP-98` has him identifying the same verse's *"pure offering"* as **Christ**; `DQ-27`(a) invokes the verse's **incense** clause as prophecy. ⛔⛔ **Three readings recorded side by side. The available reconciliation is NAMED so it is not silently assumed, and NOT ADOPTED on his behalf** |
| **Element / circumstance** | ⚠️ **PRESENT, AND ENTIRELY THE OBJECTOR'S** — `circumstance` `A` 1 / `B` 5. ⭐⭐ **This replicates `IP-56`'s measured split exactly** (*"the element/circumstance distinction is entirely the objector's"*). `A` answers in the principle register instead — `IP-116` |
| **The burden rule** | ✅✅ **PRESENT, AND IN A NEW DIRECTION** — `IP-115`. *"A command to discontinue principles of worship is needed to discontinue principles of worship"*, plus *"I need a positive argument, not it's unnecessary"* and *"I need something stronger than it's unnecessary."* ⚠️⚠️ **Now stands in the corpus alongside `DQ-24`(b)'s opposite allocation; recorded as two rules with different objects and ⛔ NOT adjudicated** |
| **Eucharistic sacrifice** | ✅ **PRESENT** — `IP-113` (Malachi ties incense to the Eucharist), `IP-114`, `IP-121` (⭐ Melchizedek supplies the priesthood-order premise `DQ-24`(d) and `IP-114` both need and neither states), `IP-120` (⭐⭐⭐ his own parish's incense ceremonial, first person, with its placement at the prayers for the state of Christ's Church) |

### ⚠️ Absences reported as findings, with the search terms listed

| Term / concept | Count | Note |
|---|---|---|
| `Brian` / `Bryan` / `Father B` / `Reverend` / `Deacon` / `Padre` / `Curate` | **all 0** | §5 above — plus a register check, not grep alone |
| `warrant` | **0 / 0** | ⭐ Extends `IP-56`'s *"ZERO are his"* — here **not even the objector** uses it |
| `thurible` | **0** | `censer` ×3 present; he uses the scriptural term, not the ceremonial one |
| `eucharistic sacrifice` (as a phrase) | **0** | ⚠️ The **concept** is present in bulk (`IP-113`, `IP-114`, `IP-121`); ⛔ **this is exactly the `260835-1` shape — key terms return zero while the material is present. The finding rests on the read, not the grep** |
| `propitiat-` · `sacrifice of the mass` · `Trent` · `Article XXXI` | **0** | The eucharistic-sacrifice discussion here is **typological (Malachi / Melchizedek / showbread)**, not formulary-controversial |
| `liturgical dance` | **0** | `DQ-24`(c)/`DQ-25`(b)'s paradigm case of innovation does **not** recur; `IP-117` supplies *Restorationism* in that slot instead |
| `adiaphora` | **1** | And it is **JD's**, not his |
| `Te Deum` | **1** | And it is `A`'s, on exclusive psalmody — ⛔ **not** the `DQ-26` church-wide-reception example, and not treated as one |
| `burden` | **0** | ⚠️ The **rule** is stated repeatedly (`IP-115`) without the word — a second `260835-1`-shape instance in the same source |

⭐⭐ **Method note, because the brief required it: this pass READ the transcript end to end — all 925 turns — rather than relying on greps. Two of the three most consequential findings (`IP-111`'s concession, `IP-118`'s *"If I were Pope"*) sit under no distinctive search term and would not have surfaced from a term scan.**

---

## 7. What was written

| File | What changed |
|---|---|
| `SRC_Manifest.md` | Header stamp → `260835-42` (prior text retained); changelog entry; **three new rows** in the `A101` sessions table (session · secondary artifacts · flagged-only stream); a **substrate-divergence** blockquote; an **artifact-integrity** blockquote; the full **`File 85`** registration block (registration table · two-label rejection with five markers · what establishes the principals · `E10`–`E13` · ASR prompt contamination · Father Bryan absence) |
| `St_Francis_EMC_Distinctives.md` | Header stamp → `260835-42` (prior retained); changelog entry; the **`IP-109`…`IP-125`** ledger block with its warrant note and its closing *what this block does not do* |
| `PROJECT_STATE.md` | Header stamp → `260835-42`; **gate + pass note**; dated note spending `IP-109`…`IP-125` and `File 85`; next-free-by-prefix update (`IP-126`, `File 86`; all others re-derived unchanged); **five registry stamp rows** bumped, prior cell text retained |
| `SRC_Channel_Inventory.md` | Header stamp → `260835-42` (prior retained); **dated note recording a NON-APPLICATION** — the source is a room capture with no video ID, so clause 2 has no target and the `260835-37` video-ID reconcile has no key; the duplicate check that *was* runnable, run and clean; a future row flagged if `EXT-3` uploads a twin |
| `SRC_Coverage_Register.md` | Header stamp → `260835-42` (prior retained); `v1.4` changelog entry; **§7 dated note** — eighth attended session, first with no `[S]` twin known, expressly distinguished from `A101-2026-06-28`'s ruling; attribution state recorded as coverage state |
| `passes/260835-42_…_close-out.md` | This file |

⛔ **`Incense_Conversational_Outline.md` and `RJ_Incense_Analysis.md` were NOT opened for editing.** ⛔ **Nothing was drafted, altered or posted to Rev. James.**

---

## 8. Validator AFTER, against baseline

| | BEFORE | AFTER | Δ |
|---|---|---|---|
| ok | 84 | **82** | **−2** |
| warnings | 9 | **11** | **+2** |
| **errors** | **0** | **0** | ⭐ **0 — unchanged** |

### The two new warnings, named and explained rather than reported as noise

Both are **`IP` arms of checks that already fired on other prefixes**, and both are the **expected, correct consequence of minting seventeen `IP` findings.** ⛔ **Neither is a defect introduced by this pass's edits; each is the validator doing its job.**

| New | Text | Why it fired |
|---|---|---|
| `C10` | *"§15's newest **IP** citation is 17 findings behind the ledger (`IP-108` vs `IP-125`)."* | §15 cites up to `IP-108`; the ledger now runs to `IP-125`. ⏳ **The interval is owed a sweep for creditable material. NOT run by this pass** — §15 is a curated section and sweeping it is its own job. *(Note the `LS` arm of `C10` was already firing at gate and is unchanged: `LS-120` vs `LS-141`.)* |
| `C11` | *"outline last checked against `IP-108` (`260835-32`); the IP ledger now runs to `IP-125`. **17** finding(s) unreviewed against the outline's logical flow."* | ⭐⭐ **REPORTED AS DRIFT, WHICH IS WHAT `C11` ASKS FOR — and the check's own instruction is obeyed: *"REPORT drift; do not rewrite JD's reasoning without asking."*** ⛔⛔ **`Incense_Conversational_Outline.md` was NOT opened for editing, per the brief.** ⏳ **Seventeen findings now await review against the outline; several bear on it directly — `IP-111` on the level-(2) history claim, `IP-118` on the *"expected but not required"* gap the outline's Step 3 is built around, `IP-114` on the Malachi grain-offering reading, `IP-115` on the burden rule's direction.** ⚠️ **This is a real and substantial queue, and it is stated at full size rather than minimised.** *(The `DQ` arm of `C11` was already firing at gate and is unchanged.)* |

⛔ **The seven warnings present at gate are all still present, all unchanged, and none was introduced or repaired by this pass.**

### ⚠️ One error was introduced by this pass and repaired before close, and the fact is recorded rather than hidden

The first post-edit run returned **`81 ok · 11 warnings · 1 errors`**. The error was `C8`: `DANGLING VP- LABELS cited but never DEFINED` — **caused by this pass's own next-free-by-prefix line in `PROJECT_STATE.md`, which spelled out a `VP-N` token while listing values that had NOT moved.** `C8` treats any such token in `PROJECT_STATE.md` as a citation and requires a matching vintage-pair block in the distinctives.

✅ **Repaired at source, not suppressed:** the line now states the `VP` next-free **without writing the label out**, and says in the text exactly why. ⛔ **No `VP` block was invented to satisfy the checker, and no `VP` number moved.** ⭐ **Recorded here because a pass that introduces and fixes an error owes the report as much as one that does not.**

---

## 9. ⛔⛔⛔ What this pass deliberately did not do

- ⛔ **`DQ-24`, `DQ-25`, `DQ-26`, `DQ-27` NOT amended, superseded or re-scoped.** Every cross-reference is recorded at the `IP` finding that makes it and at none of theirs.
- ⛔ **`IP-98` NOT moved, NOT re-read, NOT reconciled with `IP-114`.**
- ⛔ **`IP-56` NOT promoted; its ear-verification flag NOT discharged.** `IP-116` corroborates it and says so, and says just as plainly that corroboration is not verification.
- ⛔ **`LS-141` NOT touched.** ⛔ **`DQ-9` NOT moved.** ⛔ **`LS-23`/`LS-24` NOT merged.**
- ⛔ **`OQ20` and `OQ21` NOT moved.** `IP-110` bears on `OQ21`'s application-to-incense gap; **the gap is left exactly where `DQ-27`(f) put it.**
- ⛔ **The `DQ-27`(b) *"used all throughout Church History"* ambiguity NOT resolved,** despite `IP-111` and `IP-112` bearing directly on it.
- ⛔ **The `DQ-27`(b) test against `Ritualist_Case_For_Incense_and_the_1899_Opinion.md` NOT run** — `DQ-27`(b) declined it and this pass declines it too.
- ⛔ **`[95:37]` *"Then I would be on the side of you must burn incense"* recorded and NOT minted as a position** — it is a conditional inside a hypothetical, and quoting it as his view would misrepresent it.
- ⛔ **Nothing minted from `E10`–`E13`,** including `E12`'s apparent self-contradiction.
- ⛔ **C11's outline drift NOT cleared;** it is reported and left for its own pass.
- ⛔ **No `LS`, `DQ`, `RV`, `BLOG`, `POD`, `VP`, `GV`, `RC`, `BP`, `EXT`, `W` or `DELTA` number consumed.** `IP` and `File` only.
- ⛔ **NOTHING COMMITTED.** JD pushes `passes/` first, then corpus edits separately.
