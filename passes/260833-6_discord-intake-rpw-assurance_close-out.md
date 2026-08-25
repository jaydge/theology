# 260833-6 — Discord double intake: RPW recapture + the Assurance thread archived

**Pass artifacts**

- `passes/260833-6_discord-intake-rpw-assurance.diff`
- `passes/260833-6_discord-intake-rpw-assurance_close-out.md` (this file)

**Validator**

| | |
|---|---|
| Before | **75 ok · 5 warnings · 0 errors** |
| After | **78 ok · 6 warnings · 0 errors** |

The five standing warnings are unchanged and were confirmed individually at the gate: C1 relative timestamp in `src/SRC_Discord_RPW.md`; C3 `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` stamp; C4 two answered-as-pending passages; C5 ×2 volatile-state assertions. **The sixth warning is C11 and it is expected — see §11.**

**Gate.** HEAD `11c32e3f9b1b902a023f0d50b1d1090938e68049` (*"260833-5: C11 outline review…"*), working tree clean, both raw sources committed at HEAD. Stamp `260833-6` grep-verified free (highest consumed was `260833-5`).

**DQ range consumed: `DQ-20` … `DQ-23`. Next free: `DQ-24`.**

---

## 1. TASK 1 — the RPW full-thread recapture, reported explicitly

**Result: messages 1-23 CLEAN — byte-identical to the raw in both heading and body. Message 24 carried ONE divergence.**

All 24 previously-archived messages were compared against `src/SRC_Discord_RPW-raw.txt` **word for word, programmatically**, not by eye.

### The one divergence, and its cause is ADJUDICATED — which is new

Message 24 (Rev. James, 8/21/26, 2:17 PM) ended `…He accepts it.` in the archive where the raw reads `…He accepts it. ` — **a single trailing space, dropped at end-of-message.**

`260833-1` hit an analogous case on message 23 and had to leave the cause open ("either JD edited the post, or that capture's handling introduced the comma; both readings stand and neither is chosen"). **This pass could do better, because a second and independent detector existed for the first time in the project's history.**

**RAW-vs-RAW.** `git diff be2587f HEAD -- src/SRC_Discord_RPW-raw.txt` — comparing the artifact `260833-1` worked from against the artifact this pass worked from — returns:

- the added `CAPTURED` line, and
- pure appends,
- **and nothing else. Zero changes to any already-captured message body across the entire thread history.**

The prior raw at `be2587f` **also carries the trailing space**. Therefore the byte was dropped by **this project's own append handling at `260833-1`**, not by Rev. James. It is a defect in our file of the same class as `260818-2`'s Defect 1 and `260801-3`'s paragraph flattenings.

**Disposition: restored in the body, with a dated correction note in the archive changelog. `260833-1`'s entry is NOT altered — it stands as written per the never-alter rule, and the new entry is the correction.** Offsets into message 24's body no longer hold; offsets against messages 1-23 are untouched.

**Conclusion on edits: Rev. James has edited nothing in this thread, ever, so far as two independent captures can show. JD has edited nothing in this thread.** (He *has* edited a message in the *other* thread — §3.)

### Append

Six messages, all resolved to **2026-08-24**:

| # | Time | Author | Content |
|---|---|---|---|
| 25 | 8:50 AM | JD Smith (OP) | The Hebrews-scope question |
| 26 | 11:27 AM | Athanasius325 / Fr James | *"There are no sin offerings apart from Christ…"* |
| 27 | 12:13 PM | JD Smith (OP) | The showbread clarification |
| 28 | 12:22 PM | **M1B3AU** | ⛔ **Third-party post — see §4** |
| 29 | 1:03 PM | Athanasius325 / Fr James | *"The Eucharist is the fulfillment of the Showbread…"* |
| 30 | 7:37 PM | Athanasius325 / Fr James | The Shewbread elaboration |

Coverage extended to **2026-06-18 → 2026-08-24**. Hash, size, lines and coverage updated in `SRC_Manifest.md`; `PROJECT_STATE.md` §4 row bumped to `260833-6`. **Hash computed LAST, after the changelog entry was written.** C6 passes.

### Verification of the archives themselves

Both archives were re-parsed after all edits and every message body compared byte-for-byte against its raw: **RPW 30/30 bodies byte-exact; Assurance 6/6 bodies byte-exact.** The only heading that does not match its raw modulo the U+202F convention is message 19 — see §5.

---

## 2. The capture-date line — the convention that did the work

⭐ **This is the quiet structural win of the pass and it should be carried forward deliberately.**

Both raws now open with `CAPTURED <date>, <time> ET, by JD, from the Discord client.` Discord renders bare time (no date) for same-day messages, which has been this project's weakest dating link since `260722-1` and has caused at least three recorded errors.

**Ten bare timestamps were resolved this pass — six in RPW, four in Assurance — every one against the file's own capture line, on the face of the artifact.** That is strictly stronger than the `260801-2`/`260810-1` class, where resolution rested on JD's separately-reported recollection.

**Corroborated rather than assumed:** in each thread the last message precedes its capture by one minute (RPW 7:37 PM / 7:38 PM; Assurance 7:27 PM / 7:28 PM), and no bare stamp in either file falls after its capture time.

⚠️ **Messages carrying full dates in the raw were NOT "resolved" and were not touched** — twenty-four in RPW, two in Assurance.

---

## 3. TASK 2 — the new Assurance archive

`src/SRC_Discord_Assurance.md` created; format follows `src/SRC_Discord_RPW.md` exactly. Coverage **2026-08-19 → 2026-08-24**, six messages. Registered in `SRC_Manifest.md` with its own `| Field | Value |` block, an alias row (`DQ-Thread-Assurance`), a raw-artifact block for `src/SRC_Discord_Assurance-raw.txt`, and two new `PROJECT_STATE.md` §4 registry rows.

### The bare-header attribution reasoning

⛔ **This was a formatting question, not an attribution question, and the reasoning is recorded so it stays that way.**

The client renders headers in **two shapes** in this thread:

- **Three lines** — handle, then a bare `OP` badge line, then a leading-space `` — 7:27 PM``
- **One line** — `JD Smith — 12:02 PM`

**The shape marks the OP badge and nothing else.** In *this* thread the OP is **Athanasius325 / Fr James**, so every three-line header is his; in `src/SRC_Discord_RPW.md` the OP is JD and every three-line header is JD's. The two files therefore look inverted, and that inversion is entirely explained by who opened which thread. **Attribution is unambiguous at every message in both files.**

**Both shapes fold into the single existing heading form `### <date>, <time> — <handle> (OP)`, which preserves the badge as the `(OP)` suffix** — the form `SRC_Discord_RPW.md` has used since `260722-1`. The archive is therefore shape-independent: **a re-render in the other shape produces no diff.** Both shapes are recorded in the archive's changelog and in the manifest block, so a future recapture cannot read a rendering difference as an edit.

### The JD-edit record

⛔⛔ **JD edited his own 12:02 PM message after posting. This is the first time the never-alter rule has been applied to JD's own text in this corpus, and it applies in full.**

- **The archive records the message AS IT NOW STANDS.**
- **A dated note at the message** records that it was edited, quotes what was removed, and records the circumstances.
- **What was removed:** a closing paragraph characterising Rev. James's position — *"It seems there is very little emphasis on faith or inward evidence of grace when it's expressed like this, almost as though it isn't required, despite there being way more verses in the NT about being saved by faith than there are about being saved through baptism"*.
- **The circumstances, which are what make it innocuous:** the removal was **JD's own deliberate revision**, made **before Rev. James replied**. Rev. James answered the message in the form archived, so the archived text is the text he answered — exactly the `260801-3` message-19 disposition, applied to the same author rather than to a different one.
- ⛔ **`(edited)` marker: CHECKED, ZERO occurrences in either raw file.** Per the standing clipboard-capture limitation (`260801-3`) an absent marker confirms nothing. **This edit is on record because JD reported it at capture time — which is precisely the hand-noting that limitation requires, and it worked.**
- ⚠️ The removed paragraph is **not** restored, **not** treated as JD's posted position, and **not** treated as having been before Rev. James. It is quoted once, in the note, so the record is recoverable.

### U+202F

All six Assurance headers carry U+202F before AM/PM, as do all thirty RPW headers. **The `260833-1` whole-class ruling was APPLIED rather than a fresh ruling being made:** header-only Discord artifact (zero U+202F in any message body), normalised to the plain-space heading convention on capture, and **recorded in the new archive** so the normalisation is never re-litigated. ⛔ It was not silently normalised and it was not silently left — either would become a phantom diff on every future recapture.

---

## 4. TASK 3 — the M1B3AU disposition (`DQ-23`)

⛔⛔ **The long 12:22 PM post is `M1B3AU`'s. NOTHING IN IT IS ATTRIBUTABLE TO REV. JAMES AT ANY TIER** — not stated, not endorsed, not context. Logged `[EXT / third-party, Discord — not RJ]`, the `DQ-6`/`DQ-14` handling class, with `DQ-14`'s rule restated at the finding: *"A rector's silence on a layman's post is not endorsement."*

⚠️ **The attribution risk here is unusually high and is named at the finding:** Rev. James replies **41 minutes later in the same thread**. His reply answers JD's 12:13 PM showbread question and engages nothing in this post.

### The central claim, and the zero — the useful part

He attributes to a clergyman at the 2026-08-23 class the framing that the 39 Articles exist *"to unite Christianity around a minimum standard of what is to be believed."*

⛔⛔ **`260833-3` checked both captures of that class and found the framing taught BY NOBODY.** `minimum`/`minimal` **0·0** · `standard` **0·0** · `Westminster` **0·0** · `WCF` **0·0** · `LBCF` **0·0** · `1689` **0·0** · `streams` **0·0** · `big tent` **0·0** · `latitude` **0·0** · `comprehensive` **0·0** · `boundary` **0·0**. The zero survives its own robustness checks (the `[S]`-sole stretch was read in full; the nearest thing in either capture is label `C`'s Article XXXIII remark, logged as neither man's).

**Recorded, not re-derived.** Consequences restated unchanged: **not a Rev. James datum · not a Rev. Brian datum · ⛔ does NOT corroborate `GV-37` and must never be logged as doing so.**

⭐⭐ **This pass adds the likeliest explanation and does not choose it over the two `260833-3` left open:** the framing is **`M1B3AU`'s own**, posted in nearly identical terms on **2026-07-10** in `src/SRC_Discord_39ArticlesFormularies.md` — same three-confession contrast, same "minimum standard" phrase, six weeks before the class he now attributes it to. He may be hearing his own settled framing back. ⛔ Recorded as an observation about the source of the framing, **not** as a charge of fabrication.

### The substantive Eucharistic content

⛔⛔ **His own position and nobody else's.** The paschal-lamb argument and the repeated *"partaking of his divine nature"* formula are logged as `M1B3AU`'s.

⚠️⚠️ **The collision risk is specific and is named at the finding:** this post argues eating-the-sacrificial-victim from the Passover lamb, which is materially close to `IP-39`/`IP-89`/`LS-112`'s Bramhall material **and sits in the same thread on the same day as Rev. James's own showbread answer.** ⛔ **The proximity is coincidence of thread and date, not agreement of authorship.** It must not contaminate `DQ-20`, `IP-39`, `IP-89` or `LS-112`, and must not be cited as corroboration of any of them. `2 Peter 1:4` applied to eucharistic reception is not a formulation the corpus holds from Rev. James in any era.

### The DQ-6 precedent

⚠️ **Followed.** JD left the inaccuracies uncorrected in-thread, by design, as at `DQ-6` (*"thread energy preserved for the RJ funnel"*). Deliberate, not an oversight: the thread was one turn from the showbread answer, and a correction addressed to a third party would have spent that turn on someone who is not the funnel. ⛔ Nothing drafted toward him.

---

## 5. The message-19 U+202F anomaly — reported again, moved again by nobody

`src/SRC_Discord_RPW.md` message 19's heading (`7/23/26, 12:07 PM`) still carries U+202F where the other twenty-nine headings carry a plain space. **It is the one heading in the file that was never normalised.**

**It surfaced this pass as a heading diff in the automated comparison — which is exactly the phantom-diff behaviour the standing ruling predicts.**

⛔ **Left unmoved, deliberately.** `260818-2` recorded it and declined to act; `260833-1` re-recorded it and declined again, expressly leaving it for JD's ruling. **This pass makes the same call for the same reason: it was not in the brief, and a raw archive is not the place to act unasked.** `PROJECT_STATE.md` §7's open item stands unchanged. It is recorded in the archive changelog so a future recapture reads it as known residue rather than as an edit.

---

## 6. TASK 4 — the one-exchange-or-two determination

### RPW: **ONE exchange, one number (`DQ-20`)**

The material could be read as two (question → answer, question → answer). It is logged as one, on three grounds:

1. **JD's 12:13 PM message opens *"Sorry, I meant…"*.** On its face it is a **restatement of the same question**, prompted by Rev. James's stated non-comprehension (*"I'm not sure what you mean by how far it reaches"*), not a new committal question. Treating it as a second posted question would also put JD in breach of `PROJECT_STATE` §1's standing constraint of *one committal question per turn, per channel* — **which he did not breach.**
2. **The `DQ-4`/`DQ-8`/`DQ-9`/`DQ-10`/`DQ-19` shape** puts a posted question and its reply-chain in one entry, and **`DQ-10` already holds a two-message reply chain** (07-11 and 07-21). A clarification turn inside one exchange is less than that, not more.
3. **The `DQ-16`/`DQ-17` split route was considered and DECLINED on its own stated conditions** — that split required a question-side entry already finalised as a question-only body **and** numbers explicitly reserved before the reply arrived. **Neither condition holds here.**

⭐ `DQ-20` was the reserved next-free number *for a newly posted question*, and JD's 8:50 AM message is exactly that — so the number is consumed as intended, not stranded.

### Assurance: **TWO exchanges, two numbers (`DQ-21`, `DQ-22`)**

**The difference from the RPW case is principled, not arbitrary.** JD's 12:02 PM message is a **new committal question**: Rev. James had answered fully at 11:54 AM, JD accepted the answer and pressed a distinct point, and Rev. James understood and answered it directly. That is two exchanges under the same shape. ⚠️ JD's 12:02 PM contains two *questions* but is **one turn**, so both are sub-findings of the single `DQ-22` entry rather than split further.

### M1B3AU: **its own number (`DQ-23`)**

Follows `DQ-6` and `DQ-14`, both of which gave third-party posts their own numbers under the `[EXT]` tag.

---

## 7. Findings minted

### `DQ-20` — RPW, the fulfilment-scope exchange ★★★

Four `[Stated]` sub-findings plus analysis blocks.

- **(a) The sin-offering answer.** *"There are no sin offerings apart from Christ. Christ is the One Sacrifice to Atone for sins."* With `DQ-19`(d)'s *"Christ has fulfilled the sin offering sacrifices"*, the Hebrews ground twice in eleven days in his own typed words — `IP-39`/`IP-91`'s ground in a second register. ⚠️ **Logged with the fact that it does not answer what was asked** (scope vs sufficiency), ⛔ **as a non-overlap and NOT as evasion — he said outright he did not follow the question.**
- **(b) ⭐⭐⭐ The showbread answer.** *"The Eucharist is the fulfillment of the Showbread, known as the Bread of the Presence."* He answers the worked instance affirmatively: **a non-atoning component IS inside the fulfilment.**
- **(c) ⭐⭐⭐ The elaboration**, unprompted, 6½ hours later, and the fuller of the two — three distinct moves: the priests' reverent eating **was itself communion with God**; the Bread was always *"in the Presence of God"* (**Exodus 25:30**); the Shewbread **was offered to God as the Eucharist is offered to God**, with worshippers *"united to the Eucharist"*, citing **the Oblation and the arrangement/wording of the 1662 BCP**.
- **(d) Scripture and formulary cited in the same sentence** as parallel warrants — `IP-13`'s method in live dialogue.

**Analysis blocks:**

- ⭐⭐⭐ **Type/antitype applied to a non-atoning sanctuary component, in his own voice, twice, with increasing detail.** ⚠️⚠️ **And it is a THIRD thing, not either of the two the corpus tracks:** `IP-3` sorts old-covenant material into *abrogated* (bloody) and *surviving* (bloodless); the showbread answer sorts it into neither — **the type is superseded AND its antitype is enacted.** ⛔⛔ **The Step 5c bloodless-examples guard is NOT cleared and must not be reported as cleared** — that argument is the project's `[Analysis]` and its guard reads *"he has stated no such rule."* **He still has stated no such rule.** What changed is narrower: on **one** bloodless component, given to him by name, he agrees the fulfilment reaches. ⛔ Not generalised by him; not extended by this entry.
- ⭐⭐ **The 1662 Oblation as a formulary-grounded move.** `Oblation` is well attested (61 occurrences, 15 files) but **every substantive deployment is the 1928** (`LS-66`, `RC3-22`, `GV-45`). ⭐⭐ **The 1662-plus-Oblation pairing has appeared in this corpus ONLY as the project's own unanswered question — Known Gap 9 / OQ5 — and never as a citation of his. This is his first.** And he reaches for the **1662 he names as his standard** (`GV-37`, `POD-7`, `IP-41`) rather than the **1928 his parish uses** (`LS-69`, `RC1-14`), on the exact point where OQ5 asks why. ⛔ Logged as a datum bearing on OQ5, **not** as an answer to it. ⚠️ Note he cites the Oblation **and *"the arrangement/wording"*** — the *order* of the rite; `LS-77` is the only prior instance of him reasoning from the BCP's arrangement.
- ⭐ **The 2026-08-23 showbread zero, cross-referenced — and it is why this answer is evidence of something.** `IP-90` records `showbread`/`shewbread`/`bread of the presence`/`table of showbread` **0·0** across both captures, with the whole type/antitype vocabulary absent alongside. **He supplied this reading the day after teaching a session in which the word never occurs.** ⛔ `260833-3`'s observation-only disposition is **unchanged**; what this pass adds is that the Discord side is now captured and attributable, which it was not when that disposition was made.
- ⚠️ **The pattern, as an observation only.** JD asked for the general rule **twice** and received an **instance** both times, elaborated rather than generalised. ⛔⛔ **NOT evasion, NOT a charge.** Innocent readings are available and one is positively supported: he said he did not follow the first question; the elaboration is unprompted and generous; and `DQ-17` already records him declining to give a rule in terms on an adjacent question, so **answering by instance is his established manner rather than a response to this question.** ⚠️ Recorded because it is now the **third consecutive occasion** (`DQ-17`, `DQ-19`, `DQ-20`) on which a request for a general criterion returned a worked example — a fact about the shape of the exchange, ⛔ **not evidence about his position.**

### `DQ-21` — Assurance, the ground ★★★

- **(a)** *"I have assurance because of the Promises of God given in Baptism. I know that Christ died for me, because I know that Christ died for all."*
- **(b) ⭐⭐ The Westminster disclaimer, volunteered and unprompted:** *"Yes, it doesn't necessarily flow from the WCF."* He was not asked whether *his* account was Westminster's — JD had said only that the Hopkins test was not. **He extends the concession to his own answer before giving it.** Bears on `OQ18`: here he marks the boundary himself, against a standard he does not hold. ⛔ Does not settle `OQ18`.
- **(c) ⭐⭐⭐ Universal atonement in his own voice, load-bearing for assurance — a corpus first on both counts.** The second clause is the inference carrying the personal application (*"…**because** I know that Christ died for all"*). **Corpus check run and reported: `died for all` · `universal atonement` · `unlimited atonement` — ZERO in every `.md` before this pass.** `limited atonement` returns one hit and it is not his position-taking (`LS-85`); `particular redemption` appears only in the project's own Known Gap 4 list; every `Arminian` hit concerns **foreknowledge, never extent**, including `IP-37`'s *"I do not identify as an Arminian."* **Known Gap 4 has been recorded as narrowing-and-not-filling at least three times.** ⭐⭐⭐ **This fills it — and does so incidentally, deployed as an already-settled premise in service of something else, which is the strongest form such a datum can take.** ⛔ **NOT logged as an Arminian self-identification; `IP-37` forbids the inference and the label is not applied to him.**

**Known Gap 5 — shifted, stayed, or broadened? Answer: STAYED, NARROWED IN LOCUS, BROADENED IN WARRANT.**

- ⭐ **STAYED.** The governing contrast — **objective promise against inward state** — is unchanged across eleven years (`BLOG-63` 2015, `POD-6` 2019, `GV-5`, `BP-29`), and `IP-76`'s anti-introspective motive (avoiding the later-Puritan *"constant second-guessing"*) is the same motive visible here.
- ⭐ **NARROWED IN LOCUS.** `BP-29`/`GV-5` ground it in **baptism**; `BLOG-63`/`POD-6` in **baptism plus the priest's weekly absolution**. **The current statement names baptism only.**
- ⛔⛔ **THE PRIEST'S-ABSOLUTION ELEMENT IS ABSENT, AND IT IS REPORTED AS AN ABSENCE AND NOTHING MORE.** Not a change of mind, not a retraction, not a development, not evidence that he has moved. **He was asked one question and gave a two-sentence answer; a short answer omitting an element is not a withdrawal of it, and the corpus contains no statement withdrawing it.**
- ⭐ **BROADENED IN WARRANT.** None of `BLOG-63`, `POD-6`, `GV-5` or `BP-29` supplies a reason why the promise applies **to him in particular**. (c) now supplies one. **That is the part of Gap 5 that was genuinely missing.**
- ⏳ **Gap 5 moves from *"current-voice side genuinely absent"* to *"first current-voice datum acquired."* NOT closed.**

⛔ **`VP-` pair considered and DECLINED**, with the reasoning recorded: a `BLOG-63`/`DQ-21` pair is same-direction, not opposing, and the only difference is an **absence**. **Minting a pair on an absence would convert "he did not mention it" into "he changed his mind."**

### `DQ-22` — Assurance, the limits ★★

- **(a) ⭐⭐ The apostate answer:** *"No, because the Promises are not for those who reject Christ."* ⭐ **The missing term D10 has wanted:** the ground is not bare baptism — it is the promise, and the promise has a **stated scope condition**. Fits `IP-76`'s narrow definition of apostasy (*"a willful, stubborn, deliberate rejection of the faith"*, expressly not *"struggling with sin"*) without strain. ⛔ Not a full account — he does not say how one distinguishes oneself from the apostate **prospectively**, and was not asked in that form.
- **(b) ⭐⭐ Faith and repentance as constituents *of* the promise:** *"Faith and Repentance are part of the Promise given in Baptism, as Acts 2:38-39 show."* **The precision is the finding.** The ordinary Reformed construction makes faith the **instrument by which** the promise is received; **he puts faith and repentance INSIDE the promise, as part of what is given** — which is why the preceding clause is *"we are not saved by our works"*: on his construction faith cannot be a work because it is not the recipient's contribution at all. Coheres with `IP-76`'s *"regeneration also causes faith"* (via `IP-28`). ⚠️ `IP-28` already records Acts 2:38-39 read as the norm for baptismal justification; **this adds what the passage does in his account of the promise's CONTENT**, which `IP-28` does not carry. ⛔⛔ **FEDERAL VISION GUARD APPLIED AND RESTATED: `Federal Vision` is 0 in both new sources; the framing is Acts, Augustine and the baptismal promise; the label is the project's, not his. THIS MUST NOT BE REPORTED AS A FEDERAL VISION POSITION.** `OQ12` neither advanced nor retired.
- **(c) ⭐ The honest disclaimer:** *"I have no idea what happens with the second half of that."* ✅ **Filed in §15 — see §8.**

⚠️ **What he did NOT answer, recorded so it is not lost:** JD's second case had two halves; **he declines the second (never-evangelised) and does not separately address the first (baptized but never believed)** — which is the more pressing of the two for D10 and is not niche at all. ⛔ Recorded as an open item, **not** as evasion: (b) arguably answers it by implication, **but that is the project's inference and he did not draw it.** ⏳ A candidate for a future turn; ⛔ not drafted here.

### `DQ-23` — the M1B3AU post `[EXT — not RJ]`

See §4.

---

## 8. §15 — swept in the same pass, three filed, five declined

**Filed:**

1. ⭐⭐ **The candour disclaimer (`DQ-22`(c)).** **Filed, and the reasoning is recorded because §15 filings must be argued.** It is shared ground in the strict `BLOG-16` sense, not merely a likeable trait: **the Reformed answer to the fate of the never-evangelised is also a refusal to pronounce.** It also belongs to §15's established **intellectual-honesty** class — he was under no pressure and the speculative answers available were cheap. ⛔ **What is credited is the refusal to speculate, not any substantive position.**
2. ⭐ **The Hebrews ground for the sin offerings (`DQ-20`(a))** — the existing `DQ-18`/`DQ-19` item **confirmed rather than duplicated**; it did not weaken on restatement.
3. ⭐ **Assurance rested on an objective promise rather than an inward state (`DQ-21`(a))** — ⚠️ **filed NARROWLY and the narrowness is the point.** What is shared is the **anti-introspective instinct** (WCF 18 grounds assurance first in the divine promises). ⛔ **The LOCUS is NOT filed** — that the promise is given in baptism, and that baptism is its sole named ground, is precisely where a Reformed reader differs; **the `POD-6` decline governs and is unchanged.** Filing it whole would flatter the section, which `BLOG-16` forbids.

**Declined, with reasons:**

1. *"Yes, it doesn't necessarily flow from the WCF"* (`DQ-21`(b)) — creditable **candour**, but it is an acknowledgement of **divergence**, and filing a divergence-acknowledgement in the common-ground register is the `BLOG-16` error. Noted at the finding instead.
2. **Universal atonement** (`DQ-21`(c)) — a genuine cross-tradition difference of the `BLOG-16` Arminianism class; its interest here is evidentiary, not irenic, and filing it would risk reading as approval of a position the project has not examined.
3. **Faith and repentance as constituents of the promise** (`DQ-22`(b)) — the sharpest divergence in the pass; not common ground on any reading.
4. *"The Promises are not for those who reject Christ"* (`DQ-22`(a)) — a limit a Reformed reader would welcome, **but it sits inside the live D10/`BP-29` question and filing it would decide that question by filing** (`BLOG-98` precedent).
5. **The showbread identification** (`DQ-20`(b)/(c)) — the pass's headline and impressive as exegesis, **but it is the substance of an open enquiry, not agreed ground; crediting it would prejudge Step 5c.**

---

## 9. Batteries — every result, including the zeros

### §0 STANDING INSTRUCTION — incense and icons

**RPW messages 25-30**, every hit traced to a speaker:

| Term | Count | Speakers |
|---|---|---|
| `incense` | **1** | ⭐ **JD ONLY** — *"Malachi I'll want to come back to as well, since the incense there sits alongside a grain offering"* (deferring the topic) |
| `sacrifice` | 8 | JD 3 · **Rev. James 1** · M1B3AU 4 |
| `oblation` | 1 | **Rev. James** — the 1662 citation |
| `thurible` · `censer` · `censing` · `thurifer` · `frankincense` · `icon` · `iconograph-` · `image` · `altar` · `candle` · `vestment` · `smoke` · `ceremon-` | **0** | — |

**Assurance thread: every probe 0 — a confirmed zero, reported as required.**

⛔ **Rev. James named incense ZERO times this pass.** `DQ-19`'s incense opening is **not repeated and not withdrawn — it is untouched, because JD deferred it by his own choice.**

### `DQ-9`'s battery — trace every hit to a speaker

**RPW messages 25-30 and the whole Assurance thread**, same result on both:

`regulative` **0** · `normative` **0** · `RPW` **0** · `warrant` **0** · `approved example` **0** · `necessary inference` **0** · `authoriz-`/`authoris-` **0** · `element` **0** · `circumstance` **0** · `licen-` **0** · `adiaphora` **0** · `repugnant` **0** · `prescrib-` **0** · `good and necessary` **0** · `principle` **0** · `individual act` **0**.

⚠️ **A total lexical zero on the level question — and `260833-3`'s warning applies in reverse.** The usual trap is a count that matches without the content. **Here the CONTENT is squarely `DQ-9`-adjacent** (a fulfilment criterion is exactly the kind of thing that must be pitched at act level or principle level) **while the TERMS are wholly absent.** ⛔⛔ **Neither settles the level question. `DQ-9` IS REPORTED AND NOT MOVED. Absences do not compound into a position.**

### `OQ18` — whose voice

**Two data added; the item is NOT advanced.** (1) `DQ-21`(b)'s unprompted *"it doesn't necessarily flow from the WCF"* — boundary-marking against a standard he does not hold, the one case where the whose-voice question does not arise. (2) The `we` count, speaker-traced: **Assurance `we` ×8, seven of them his**, all soteriological (*"we are not saved by our works"*); **RPW msgs 25-30 `we` ×7, NONE his** (JD 1, M1B3AU 6); `what we have received` **0** across both. ⚠️ **His characteristic *"what we've received"* register is absent from his new RPW messages entirely.** ⛔⛔ **The systematic pass is still NOT RUN and Note 2k's 45 flagged claims are unresolved.**

### `OQ19` — checked, empty, and NOT advanced

⛔⛔ **An honest zero, reported as required.** Nothing in either source bears on the provenance of the permission-by-depiction rule. The one adjacent thing — `DQ-20`(c)'s citation of the 1662 *"arrangement/wording"* — is a **formulary**-grounded move and points, if anything, away from the hypothesis's concern; **it is one instance on a different question and is not evidence about `DQ-16`'s rule.** ⛔ **The hypothesis remains a hypothesis: not verified, not advanced, not cited as a finding, not put to him.**

### `OQ20` — *"what we have received"* and the date floor

**Lexical, speaker-traced: `what we have received` 0 · `received` 0 · `consensus` 0 · `tradition` 0 · `ancient` 0 · `apostolic` 0 · `early Church` 0** across both new sources. ⛔ **An honest zero — he does not use the phrase or any neighbour anywhere in the new material.**

⭐⭐ **But `DQ-20`(c) bears on it substantively, which the lexical scan would have missed.** Asked what governs the fulfilment, he warrants from **Exodus 25:30 and the 1662 BCP** — **from Scripture plus a named, dated formulary, not from *"what we have received"* at all.** ⚠️ If his warrants in practice run to **text rather than custom**, the *"received"* of the burden rule may be doing less work than the item's sharpest reading supposes, and the 1662 citation would supply an **implicit floor (a book, with a date)** rather than an open-ended one. ⛔⛔ **One instance, not an answer.** He was not asked what *"received"* means and did not define it; the item does not move, the three candidate readings are not chosen among, and the sharpest form is not softened. ⏳ Recorded so a future pass can test whether the text-over-custom pattern holds.

---

## 10. What was declined, and why

- **Normalising message 19's U+202F** — out of brief; `260818-2` and `260833-1` both declined and left it for JD (§5).
- **A `VP-` pair on `BLOG-63`/`DQ-21`** — same-direction, and the difference is an absence (§7).
- **`DEEP HISTORY` on `DQ-20`** — current-era live dialogue; no opposing vintage.
- **Five §15 candidates** (§8).
- **Advancing `OQ19`** — hypothesis only, per the brief and the item's own guard.
- **Moving `DQ-9`** — reported, not moved.
- **Clearing `C11`** (§11).
- **Any question, draft, or reply toward Rev. James** — ⛔ **nothing posted, drafted, or altered. Both threads are live and awaiting JD's replies; the wording is his.**

---

## 11. C11 status after the pass — **FIRES, EXPECTED, NOT CLEARED**

```
WARN [C11] outline last checked against DQ-19 (260833-1); the DQ ledger now runs
           to DQ-23. 4 finding(s) unreviewed against the outline's logical flow.
           REPORT drift; do not rewrite JD's reasoning without asking.
```

⚠️⚠️ **This is expected and correct, exactly as the brief predicted.** The outline was reviewed at `260833-5` to `IP-97`/`DQ-19`; four new DQ findings now stand unreviewed.

⛔⛔ **`Incense_Conversational_Outline.md` IS NOT TOUCHED BY THIS PASS.** The drift is **reported**, per the check's own instruction. Clearing it by editing the outline is a separate review pass, with JD's involvement.

⭐ **For that pass: `DQ-20` is the one that most needs the review.** Its showbread material bears directly on **Step 5c's bloodless-examples argument** — which cites Hebrews 9:2-4's inclusion of *the table and bread of the Presence* among the furniture Christ's entry fulfilled. ⛔ **But the standing guard *"he has stated no such rule"* is NOT cleared by `DQ-20` and must not be reported as cleared.** He agrees the fulfilment reaches **one** bloodless component; he states no general rule, and the outline must not be written as though he did.

---

## 12. Unresolved / carried forward

1. ⏳ **Message 19's U+202F** — still awaiting JD's ruling; third pass to record it.
2. ⏳ **C11 drift** — four findings unreviewed against the outline; separate pass, with JD.
3. ⏳ **Known Gap 5 is moved, not closed** — open: whether absolution remains part of his account; how the believer distinguishes himself **prospectively** from the apostate; and the **baptized-but-never-believing** half of JD's question, which he did not address.
4. ⏳ **OQ5 / Known Gap 9** — `DQ-20`(c) supplies a datum (he cites the 1662's Oblation) but no reason for the 1928/1662 choice.
5. ⏳ **OQ18's systematic pass** — still not run; two more data points added.
6. ⏳ **OQ20** — undefined term; one suggestive instance, no answer.
7. ⏳ **`DQ-9`** — unmoved, and the highest-value unwritten thing in the project remains unwritten.
8. ⚠️ **Two channels are simultaneously on JD's turn** — the cross-channel single-threading constraint is now a live constraint, not a theoretical one. **Which thread gets the next question is JD's sequencing call and is not a documentation task.**
9. ⚠️ **Two items JD flagged in-thread and deferred by his own choice are owed BY HIM** in the RPW thread: the Joshua 7 reading and Malachi 1:11's grain offering.
10. ⚠️ **`SRC_Manifest.md`'s Discord-archives header parenthetical** (*"DiscordChatExporter"*) is false and was retracted at `260801-3`; it is now flagged in place with the retraction rather than edited, per the never-alter rule.

---

## 13. Files touched

| File | Change |
|---|---|
| `src/SRC_Discord_RPW.md` | Message-24 dated correction; six messages appended; changelog entry |
| `src/SRC_Discord_Assurance.md` | ⭐ **NEW** — six messages, changelog, header-shape note, JD-edit dated note |
| `St_Francis_EMC_Distinctives.md` | `DQ-20`…`DQ-23`; §15 block; Known Gap 5 update; `OQ18`/`OQ19`/`OQ20` dated notes; stamp + changelog |
| `SRC_Manifest.md` | RPW row (hash/size/lines/coverage/export/findings); RPW raw block; two new blocks; alias row; header note; stamp + changelog |
| `PROJECT_STATE.md` | Stamp; §1 two rows + dated note; §3; §4 two new rows + cells + tree; §5 next-free + rule 4; pass note; registry versions |
| ⛔ `Incense_Conversational_Outline.md` | **NOT TOUCHED** |

**Diff verified by reverse-apply (`git apply --check --reverse`): clean.**

⛔ **Nothing committed. No `git add`, `git commit`, or `git push` was run.**
