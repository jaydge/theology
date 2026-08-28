# 260835-25 — JD's five small-item rulings from `260835-24` §7 (close-out)

**Pass stamp:** `260835-25` · **Date:** 2026-08-28 · **Scope:** apply five rulings; build the Revelation video-to-transcript mapping; flag one rule for JD.

⛔⛔⛔ **NOTHING MINTED AND NO NUMBER OF ANY KIND CONSUMED** — no `DQ`, `IP`, `LS`, `RV`, `Rev`, `BLOG`, `POD`, `VP`, `GV`, `RC`, `BP`, `EXT`, `W` or `File`. Nothing downloaded or transcribed. `Incense_Conversational_Outline.md` and `RJ_Incense_Analysis.md` **not touched**. Nothing drafted, altered or posted to Rev. James. **Nothing committed** — `passes/` goes up first for review, corpus edits separately.

---

## 1. Gate

| item | value |
|---|---|
| HEAD at gate | `60b11f0c90ccd4ec046e39f82194580e1de74355`, branch `main` |
| `git --no-optional-locks status --short` before first edit | **EMPTY** — captured directly, not reconstructed |
| git reads | all via `git --no-optional-locks` per the `260835-3` FUSE-lock diagnosis; no lock created, none removed, no `rm` attempted |
| Validator BEFORE | **`82 ok · 9 warnings · 0 errors`** |
| `PROJECT_STATE.md` own stamp at gate | **`260835-24`** |
| Next-free pass stamp | **`260835-25`** — derived fresh by grep, see §1.2 |

### 1.1 All nine firing codes at gate, verbatim

1. `[C1]` `src/SRC_Discord_RPW.md`: 2 relative timestamp(s) outside message headers (`'Yesterday at …'`).
2. `[C3]` `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md`: no parseable `Last updated` stamp; registry says `260832-2`.
3. `[C3]` `tools/transcribe_yt.py`: no parseable `Last updated` stamp; registry says `260833-7`.
4. `[C4]` `St_Francis_EMC_Distinctives.md`: 2 passage(s) describe an ANSWERED question as pending with no supersede marker.
5. `[C5]` `RJ_Final_Question_List.md`: 17 volatile-state assertions.
6. `[C5]` `RJ_Incense_Analysis.md`: 9 volatile-state assertions.
7. `[C5]` `St_Francis_EMC_Distinctives.md`: 7 volatile-state assertions.
8. `[C10]` §15's newest `LS` citation is 9 findings behind the ledger (`LS-120` vs `LS-129`).
9. `[C11]` outline last checked against `IP-97` (`260833-5`); the `IP` ledger runs to `IP-108`; 11 findings unreviewed.

⛔ **Unchanged from the `260835-24` gate. None of it is this pass's business and none of it was touched.**

### 1.2 Stamp derivation — hazard note read FIRST, as the brief required

The `260835-12`/`260835-14` hazard note (recorded at `PROJECT_STATE.md` `260835-22`, restated in the `260835-23` and `260835-24` close-outs) warns that a naive content-grep misleads **in both directions** there:

- `260835-12` reads as *available* to a grep because earlier close-outs contain prose asserting its absence — **but it is REAL and CONSUMED** (the `CLAUDE.md`/Bootstrap divergence audit, commit `530d987`).
- `260835-14` exists **only** as committed filenames and a commit message — its own internal prose still says `260835-12` — **and it too is REAL and CONSUMED** (the diarization-verification pass).

⛔ **Neither is in play at this end of the range and neither was treated as free.**

Derivation actually used:

- repo-wide content grep for `26[0-9]{4}-[0-9]+` across `*.md`/`*.py`/`*.txt` tops out at **`260835-24`**;
- corroborated by **three independent authoritative witnesses** — `PROJECT_STATE.md`'s own header stamp at gate, the committed artifacts `passes/260835-24_three-rulings{.diff,_close-out.md}`, and commit `60b11f0`'s own message;
- `grep -rn "260835-25"` → **zero matches repo-wide**; `ls passes/ | grep -c 260835-25` → **0**; `git log --all | grep -c "260835-25"` → **0**; `grep -rn "260836-"` → only quoted shell lines and absence-assertions inside earlier close-outs.

**Highest REAL stamp is `260835-24`. This pass is `260835-25`.**

### 1.3 State figures — re-derived independently, not taken from the brief

⛔ The brief supplied no state figures and expressly forbade using any. Verdicts were parsed off each row's **operative (newest) verdict** — the text before the first *"Previously:"* — with `REGISTERED —` treated as `INGESTED`.

⚠️ **Six rows were hand-adjudicated rather than parsed, and this is worth recording because a first-keyword parse gets all six wrong:**

- Four `260835-24` returns whose *banner* reads **"JD'S RULING ON THE FOUR FLAGGED `EXCLUDE` ROWS"** but whose verdict is `INCLUDE` — `Ns2jU8injPw`, `17M5hMvDRm4`, `EqgNkZK7iJM`, `bQXMP1cLRa0`. A parse keyed on first keyword scores them `EXCLUDE`.
- Two Fr. Ray rows whose cells open **"REGISTERED AS `File 58`/`File 59`"** but whose verdict is `DECLINED — NOT REV. JAMES` — `8nRhmD4w-Wg`, `9Fezj9WMh3A`. A first-keyword parse scores them `INGESTED`.

Each of the six was read in full before assignment.

⭐ **The corrected baseline reproduces `260835-24`'s own post-state exactly — 108 / 203 / 36 / 6 / 13 / 2 / 0 = 368.** That is an independent agreement, not an adoption. **No brief premise was falsified this pass** (the brief asserted none to falsify).

---

## 2. Item 1 — `File 69` stays registered as-is ✅

**Ruling applied.** Recorded as a dated note in **both** places a re-raise could originate:

1. `SRC_Channel_Inventory.md`, the `M7iSL5mznTk` decision cell — where the office rule is applied to rows;
2. `SRC_Manifest.md`, the `File 69` block — the registry of record.

⚠️⚠️ **The tension is stated plainly rather than glossed.** Under the office rule written into `ORCHESTRATION.md` §8 at `260835-24`, this recording is **case 1 exactly** — a pure office with no original teaching — and **would have been `DECLINED-office` at triage.** `260835-18` records it as **read-aloud end to end, 100%, zero own-voice content.** It was ingested under the prior handling, before that rule existed, **and JD's ruling is that it stays.**

⛔ **The ruling is about the artifact, not the rule.** It does not weaken the office rule, does not create a precedent for ingesting further pure offices, and does not license reopening any `DECLINED-office` row. A registered artifact is not re-litigated because the triage standard later moved under it.

⭐ **Two positive reasons for retention, both from the file's own evidence rather than asserted:**

- the `260835-18` **practice** datum — he publicly led an Act of Spiritual Communion in the traditional rite in March 2020, a fact about what he *did*, which survives the read-aloud rule intact;
- the `GV-50`-class **trap warning** itself, which the office rule cites as load-bearing precedent. ⛔ Deregistration would delete the warning along with the artifact.

⛔ Registration status, `File` number, hash, byte count, speaker warrant and the `PRACTICE ONLY` restriction are all unchanged.

---

## 3. Item 2 — the at-Mass premise on `17M5hMvDRm4` and `bQXMP1cLRa0` ✅

**Ruling applied.** Both rows **stay `INCLUDE` — T4** and **stay in the pull list.** The *at Mass* premise **stays unverified and is not to be chased before pull** — JD's ruling is that it does not bear on the decision either way.

⭐⭐⭐ **The substance of the ruling is the narrowed ground, and it is written into both cells in JD's own terms:** the rapping itself is **not** what interests him. The rows are included for **whether Rev. James says anything theologically substantive in reacting to it.** The incident is the occasion; **his commentary is the object.**

⛔ **A consequence is written in so a later pass does not misread it:** a pull returning only reaction — amusement, disapproval, no theological content — is a **nil return, correctly reported.** It does not falsify the ground, because the ground was never that the clip contains an incident of a particular kind.

⚠️ `260835-24`'s ceremonial-propriety reading is **retained below the new note as one shape the commentary might take** — explicitly **not** as the ground of inclusion, and **not** as something to go looking to confirm. Ear-check at pull only if the at-Mass question turns out to bear on what he actually says.

⭐ `bQXMP1cLRa0`'s pull-order note is retained and is now doubly relevant: at 3,527 views it is the most-watched of the four returned rows by a wide margin, so whatever theological commentary it carries has had the widest reach.

---

## 4. Item 3 — the Revelation mapping ⭐ (the large item)

### 4.1 The renumbering is confirmed **from inside the repo**, not taken on report

JD reports that Rev. James renamed and renumbered sessions after posting, and that his own markdown files — copied from the live titles about a month ago — no longer match the current channel numbering. **That is confirmed here without relying on the report, because the evidence was already on disk.** Each transcript's own first line is a copy-paste of the live title as it stood at download.

| transcript file's OWN first line (captured ~2026-07) | `SRC_Channel_Inventory.md` title NOW | video ID | chapter |
|---|---|---|---|
| *Revelation Class, Session **XI**: The Two Beasts and the Mark (Ch 13)* | Session **XI** — same | `M71-SrYEoEQ` | 13 |
| *Revelation Class, Session **XIII**: The Last Plagues and the Song of Moses (Chapter 15)* | Session **XIII** — same | `7yiQQdH_sEI` | 15 |
| *Revelation Class, Session **XIV**: The Whore and the Beast (Ch 17-18)* | ⚠️ Session **XV** | `nGfY6_P5m5o` | 17-18 |
| *Revelation Class, Session **XV**: The Marriage Supper of the Lamb (Chapter 19)* | ⚠️ Session **XVI** | `lJo0WgP37rs` | 19 |

⭐⭐⭐ **The shift is +1, it begins at the ch-17-18 session, and everything else in both titles matches exactly — subtitle, chapter parenthesis, upload date.** Two consecutive sessions moving by the same offset is a **systematic channel-side renumbering**, not a transcription slip.

⛔⛔ **Consequence, and the reason the note exists: `RV-S14` is what the channel now calls Session XV, and `RV-S15` is what it now calls Session XVI.** A pass reading a row ID as a channel session number is off by one from the ch-17-18 session onward.

⛔ **Row IDs are NOT renamed**, nor are the *"Session XIII/XIV/XV only"* descriptions in the `File 10`/`File 11`/`File 12` blocks — they are cited identifiers and renaming them is the renumbering §5 rule 1 forbids. **Read them as opaque labels with no channel meaning**, exactly as `Rev2025-S*`'s *2025* is already read as a legacy string with no date content.

### 4.2 The mapping — all 16 rows resolve, zero unresolved

| video ID | chapter(s) | session row | source file | status |
|---|---|---|---|---|
| `Ac3oAM2trBc` | intro | `Rev2025-S1` | `a104.md` / **File 8** | already `INGESTED` |
| `QqQHIrI7-6M` | 1-3 | `Rev2025-S2` | ″ | already `INGESTED` |
| `FxbVzG0on5I` | 4 | `Rev2025-S3` | ″ | already `INGESTED` |
| `RG4AP5vSKrY` + `DACpGVyqqNE` | 5-6 | `Rev2025-S4` | **Files 8+9** | already `INGESTED` (one row, two videos) |
| `_8axw8Hog60` | 7 | `Rev2025-S5` | `a104-2.md` / **File 9** | already `INGESTED` |
| `ZbTi1klNlw8` | 8 | `Rev2025-S6` | ″ | already `INGESTED` ⭐⭐⭐ **`Rev-9`, the altar/censer passage** |
| `B7YgZ-o2WU0` | 9 | `Rev2025-S7` | ″ | already `INGESTED` |
| `6JRvrk-t3e0` | 10 | `Rev2025-S8` | ″ | already `INGESTED` |
| `nOSaF0BWS2Y` | **11** | `RV-S09` | `a302…` / **File 4** @125-29,423 | ⭐ **ESTABLISHED THIS PASS** |
| `ADQnOyBaSRk` | **12** | `RV-S10` | ″ @29,512-60,374 | ⭐ **ESTABLISHED THIS PASS** |
| `M71-SrYEoEQ` | **13** | `RV-S11` | ″ @60,455-94,822 | ⭐⭐ **ESTABLISHED, byte-exactly** |
| ⛔ *(none — no video, no transcript)* | **14** | ⛔ **NONE** | ⛔ **NONE** | ⚠️⚠️ **UNCOVERED; the channel's missing Session XII** |
| `7yiQQdH_sEI` | 15 | `RV-S13` | `a305…` / **File 10** | already `INGESTED` |
| ⛔ *(none — no video, no transcript)* | **16** | ⛔ **NONE** | ⛔ **NONE** | ⚠️⚠️ **UNCOVERED; the channel's missing Session XIV** |
| `nGfY6_P5m5o` | **17-18** | `RV-S14` | `a306…` / **File 11** @85-26,838 | ⭐ **ESTABLISHED THIS PASS** |
| `lJo0WgP37rs` | **19** | `RV-S15` | `a307…` / **File 12** @95-21,575 | ⭐ **ESTABLISHED** ⚠️ **PARTIAL** |
| `GeWfXTAjFDo` | **20** | ⚠️ *(no `RV-S` row)* | **File 63** | **REGISTERED** at `260835-12`, ⛔ **UNMINED — no `RV` findings exist for ch 20** |

**Five rows moved `INCLUDE` → `INGESTED`.** ⛔ **Zero Revelation rows remain unresolved.**

### 4.3 How each pairing was established — and what was NOT available

⚠️⚠️ **JD's suggested caption-grep route was tested and is honestly reported as unavailable rather than faked.** Only **one** of the sixteen videos (`GeWfXTAjFDo`) has captions on disk — `original transcripts/video transcripts/redownloads/` holds `…-youtube.srt` for it alone — and the brief forbade downloading. **The other fifteen have no captions and no metadata JSON in the repo.**

The equivalent empirical test was therefore run against material already held. **Four independent, agreeing checks per row:**

1. **The transcripts' own internal title-and-date headers.** `a302` carries `##`/`###` headers naming *Session IX: the Beast and the Bottomless Pit (Chapter 11)* / *Jun 21, 2026*, *Session X: the Woman, the Child, and the Dragon* / *Jun 30, 2026*, and *Session XI: the Two Beasts and the Mark* — each matching a channel row's title, and the first two its upload date, exactly, and each sitting immediately before the registered byte range. `a306` and `a307` carry the live titles in §4.1.
2. **The chapter each block actually expounds**, read from the text — every one agrees with its row.
3. **Byte-density against video runtime** — 12.5-14.7 B/s across all six newly-checked sessions, so each transcript accounts for the **whole** video, not part of one.
4. **One-to-one uniqueness in both directions** — each chapter is covered by exactly one transcript and exactly one video.

### 4.4 ⭐⭐⭐ The strongest single piece of evidence — byte-exact

`a304-Revelation-class-11.md` (34,462 B, byte-identical to `a304-Revelation-August-2026.md`) is a **standalone re-download of the ch-13 session**:

- its first line is `M71-SrYEoEQ`'s **full current title verbatim, including the chapter parenthesis**;
- its second is `## Aug 2, 2026` — **that row's upload date**;
- **its body is exactly 34,367 B after a 95-byte header — byte-for-byte the length of `RV-S11`'s registered range 60,455-94,822**;
- both open *"Let's do that. >> All right. The Lord be with you"* and both close *"…Nero using 616 … We'll see you at communion in a second."*

⛔ **`a304` is a redundant re-download of material already inside `File 4`** — the same shape as the `a403`/`a404`/`a406` set confirmed at `260822-2`. **It is not a new source, takes no `File` number, and nothing is owed for it.**

### 4.5 ⚠️⚠️ Two defects found in the manifest's *Uploaded* column — reported, **not corrected**

Dated-noted at the `RV-S*` table; **the cells are left standing** per the never-alter rule. A later pass may correct them on that note's warrant.

1. ⛔⛔ **`RV-S11` reads `2026-06-30`. That is wrong; the true value is `2026-08-02`.** Diagnosed rather than guessed: `a302`'s internal `### Jun 30, 2026` line for Session XI **duplicates Session X's date line verbatim**, and the manifest took it at face value. Three independent witnesses give 2026-08-02 — the inventory row, `a304`'s own header, and the five-week teaching gap the June date would otherwise collapse.
2. ⚠️ **`RV-S13` reads `2026-08-02`. The true value is `2026-08-03`** — `a305`'s own header reads *## Aug 3, 2026* and the channel row reads 2026-08-03. ⭐ The wrong value is exactly `RV-S11`'s *true* value, consistent with a one-row-down copy at registration.

### 4.6 ⚠️⚠️⚠️ One inherited claim corrected — it would have cost a wasted pull

`260835-24` recorded that `RV-S15` is truncated and that *"the video would complete it."* ⛔ **It would not.**

`lJo0WgP37rs` runs **1,547 s = 25:47**, and JD's own viewing at `260823-1` reports the **video itself** cuts off at about 25 minutes mid-sentence. The transcript's density is **13.9 B/s, mid-band for this series** — i.e. **the capture already accounts for the full video.**

⭐⭐⭐ **The truncation is in the recording, not in the capture.** Re-pulling this video recovers nothing. `RV-S15` stays PARTIAL permanently unless a Part 2 is posted, and the `260823-1` prohibition stands: **no absence may be claimed for Revelation 19 after the break.**

### 4.7 ⏳ Naming convention — **proposed, not applied**

Session numbers have now failed **twice** as an index (the `Rev`/`RV` *2025* mislabel; this renumbering), and chapter coverage has settled both.

**Proposal:** annotate — never rename — every `RV-S*` and `Rev2025-S*` row and every Revelation `File` block with its **chapter coverage** as the primary human-readable identifier, e.g. `RV-S14` shown as ***`RV-S14` (Rev 17-18)***, so a reader keys on the chapter while the row ID stays the stable citation token.

⛔⛔ **Not a renumbering and not a rename:** every existing ID keeps its exact string, every citation elsewhere keeps resolving, §5 rule 1 is untouched. ⭐ Cheap — the coverage column already holds the chapter for every row; the change is presentational.

⚠️ **Argument against, recorded so JD rules on a fair statement:** chapters are not one-to-one with sessions either (`Rev2025-S4` is chapters 5-6 across two videos; `RV-S14` is 17-18), so the annotation is a **better** index, not a perfect one.

⛔ **NOT APPLIED. Awaiting JD.**

---

## 5. Item 4 — Revelation 14 and 16 ✅ (brief search, noted, closed)

Every Revelation transcript on disk was searched for chapter-14 and chapter-16 markers **with ASR-quirk tolerance, which mattered** — this corpus renders *bowls* as **"bowels"**, alongside the standing `censer`→`sensor` and `Sursum`→`cersum` traps registered at `260826-2`.

**Both chapters appear only as cross-references. Neither is expounded anywhere:**

- **Revelation 14** — four times in `a104-2.md` (`Rev2025-S5`, on the 144,000 and *first fruits*) and once in `a307` (the winepress, *"echoing Isaiah 63 and then back to Revelation 14"*).
- **Revelation 16** — only **prospectively**: `a305`'s own closing calls Revelation 15 *"this lurggical prologue to the bold [bowl] judgments of chapter 16"*, and `a302` looks ahead to *"the final bowls of wrath."*

⛔ **A forward reference to a chapter is not coverage of it.**

⭐ **Corroborated from the other side, which is what makes the answer solid rather than an absence-of-evidence claim:** the channel has **no video** for either chapter, and the two missing session numbers line up exactly — **Session XII** (absent, confirmed three times over at `260822-2`) sits where **chapter 14** belongs, and **Session XIV** (the gap created by the renumbering in §4.1) sits where **chapter 16** belongs. **The gap is visible from the transcript side and the channel side independently.**

⚠️ **Recorded as apparently skipped. Rev. James has been irregular with uploads.** ⛔ No cause is inferred, no absence is treated as significant, **item CLOSED, no broader investigation opened.**

⛔ Rev. 16's bowls are bowls of **wrath**, not incense (`260835-24`), so neither gap touches the incense funnel.

---

## 6. Item 5 — the five `UNCERTAIN` office rows ✅, and the rule flagged ⚠️⚠️⚠️

### 6.1 What was applied

All five keep **`UNCERTAIN`** and are **pull-marked anyway**: `FaWyhA4iB3U`, `VvkxFsykeyc`, `H1H9CO8mF8c`, `ZkVlWb852NY`, `AawVFH69H0E`.

⛔ **The two things are separated in every cell and must stay separated:** `UNCERTAIN` records **what is not known** (whether a homily is present); the pull mark records **what is to be done** (open it anyway). Resolving the first is **not** a precondition of the second, and **a later pass must not read the pull mark as having settled the status.**

⚠️⚠️ **The read-aloud attribution layer is required and expressly not waived.** Under JD's own reasoning it matters **more**, not less — the commentary being sought sits **interleaved** with the liturgical text.

⚠️ **Expected yield is recorded as LOW in advance**, so a thin batch is not read afterwards as a failure.

⭐ **Pull order is written into the cells rather than left to a later pass:**

- `FaWyhA4iB3U` **first** — 59m, the longest office row in the inventory, and its title does not even name which office it is: the highest-information pull of the five.
- `VvkxFsykeyc` and `H1H9CO8mF8c` **both together or neither** — one pull settles both the commentary question and the unexplained 8m 14s asymmetry `260835-24` recorded. ⛔ Half a pull answers neither.

### 6.2 ⚠️⚠️⚠️ The office rule is FLAGGED — **not rewritten**. This is the item most worth JD's attention.

The `260835-24` rule at `ORCHESTRATION.md` §8 declines pure offices **on the assumption that they carry no original teaching.**

⭐⭐⭐ **JD's reasoning is that commentary around the liturgy is original teaching even with no homily** — announcements, framing, explanation of what is being done and why, asides between the parts of the rite. **This does not soften the rule at the edges; it contradicts its central premise.** If he is right, **case 1 declines rows that do contain his own words.**

⛔ **What this pass did:** placed a flag beside the rule recording that its premise is before JD, so no pass applies it unaware. ⛔ **What this pass did not do:** touch the six `DECLINED-office` rows, alter the rule's text, or soften it in practice. **Until JD rules, the rule as written governs.**

**Reported for his ruling, as the brief asked:**

**(a) Should the six `DECLINED-office` rows be revisited? — YES, on this reasoning.** They were declined on **exactly** the premise now in question. The class was created four days ago, nothing downstream depends on it, and no finding cites any of the six — so revisiting is cheap and reversible.

⚠️ **One of the six would stay declined regardless, and saying so keeps the recommendation honest:** `8gb4BXlfLO4` is a **31-second** Easter Vigil fragment — too short to contain commentary of any kind — and it carries a **second, stronger, independent ground**: its description names another parish and another priest (Fr Chance Perdue, Grace Anglican, Edgeworth PA), which is the Fr. Ray precedent and the §8 channel-ownership rule. **Revisiting the class would return five rows, not six.**

**(b) What a softened rule would say:**

> **Pull offices rather than declining them. Expect low yield, and record it as low in advance so a thin return is not read as a failure. Keep the read-aloud attribution layer non-optional — under this reasoning it matters more, not less, because the commentary sought sits interleaved with the liturgical text.**

⚠️ **The counter-argument is recorded with it, because it is real:** `File 69` is **100% read-aloud with zero own-voice content**. At least one pure office in this corpus **demonstrably contains no commentary at all.** A softened rule must **expect nil returns** rather than treat them as misses — which is also the shape §3's ruling takes on the rapping rows, and the two should be read together.

---

## 7. Method — no find-and-replace anywhere

⛔⛔ **All 19 edits across four files were unique-anchor replacements behind a hard uniqueness pre-check that runs BEFORE the file is opened for writing and aborts the whole run if any anchor does not match exactly once.**

| file | edits | pre-check |
|---|---|---|
| `SRC_Channel_Inventory.md` | 13 decision cells | 13/13 unique, first run |
| `SRC_Channel_Inventory.md` | header stamp | 1/1 |
| `SRC_Manifest.md` | 2 dated notes + header | 3/3 |
| `ORCHESTRATION.md` | §8 flag | 1/1 |
| `ORCHESTRATION.md` | header stamp | 1/1 |
| `PROJECT_STATE.md` | 4 registry rows + header/gate | 5/5 |

⚠️ **Two aborts occurred earlier and are reported rather than hidden** — both in the *authoring* of the edit script, before any file was opened: a `TypeError` on a mismatched function signature, and a `SyntaxError` after an apostrophe-normalisation step broke the script's own string literals. **Neither reached the pre-check and neither wrote anything.** The pre-check itself passed on the first run for every file.

⭐ **Every reclassified cell EXTENDS rather than overwrites**; the prior verdict is retained verbatim after *"Previously:"* and marked **superseded on evidence / on the ground / not superseded at all**, never on error. ⛔ **No row's video ID, title, date, duration, channel, tab or view count touched.**

---

## 8. What was checked and came back empty, and what could not be resolved

⛔ **Reported per `passes/README.md` — a close-out that reports only successes is under-reporting.**

- **Captions for 15 of the 16 Revelation videos: absent.** Only `GeWfXTAjFDo` has `.srt`/`.json` on disk. JD's suggested caption-grep pairing could not be run as described; the substitute is stated in §4.3 rather than the method being silently swapped.
- **Revelation 14 and 16 exposition: confirmed zero** across every Revelation transcript, with quirk-tolerant patterns. A reported absence, not a gap.
- **`RV-S12`: does not exist** in the manifest and no row is created for it. The `RV-S` sequence runs S09, S10, S11, **S13**, S14, S15 — a gap that predates the renumbering and matches the channel's own missing Session XII.
- **Chapter 20 (`GeWfXTAjFDo` / `File 63`): registered but UNMINED.** No `RV-S` row and no `RV` findings exist for it. ⛔ Not changed — it is already `REGISTERED`, so the brief's "leave `INCLUDE` unless positively established" does not reach it, and minting is out of scope. **Flagged as the one Revelation row with real residual work.**
- **`RV-S15` residual pull value: retracted** (§4.6). `260835-24` named it "the one Revelation row with real residual pull value." **That is now false.** The residual value has moved to `File 63`/chapter 20 above.
- **`SRC_Coverage_Register.md`: not updated.** ⚠️ `ORCHESTRATION.md` §8 requires every intake or retro-registration pass to update **both** registries. This pass retro-registers five rows and therefore arguably owes a coverage-register update. ⛔ **It was deliberately not made:** the brief scoped this pass to five named items and forbade broader work, and the register's Revelation section would need re-deriving in full rather than patched. **Recorded as OWED, not overlooked** — so a later pass finds a decision rather than an omission.
- **`§8 incense/icons` standing instruction: CONFIRMED ZERO.** Nothing in this pass's material touched incense or icons. `Rev-9` and `Rev-10` were referenced only as already-discharged cross-references; ⛔ the `260835-24` finding that the Revelation block carries **no incense urgency** is unchanged and was not revisited.

---

## 9. Verdict totals and files touched

**BEFORE → AFTER:** `INGESTED`/`REGISTERED` **108 → 113** · `INCLUDE` **203 → 198** · `DECLINED` **36 → 36** · `DECLINED-office` **6 → 6** · `UNCERTAIN` **13 → 13** · `EXCLUDE-*` **2 → 2** · blank **0 → 0** · **total 368**.

⛔ **Touched four tracked files:** `PROJECT_STATE.md`, `SRC_Channel_Inventory.md`, `SRC_Manifest.md`, `ORCHESTRATION.md` — plus new `passes/` artifacts.

⛔ **NOT touched:** `Incense_Conversational_Outline.md` · `RJ_Incense_Analysis.md` · `SRC_Coverage_Register.md` · `St_Francis_EMC_Distinctives.md` · `RJ_Final_Question_List.md` · `RJ_Open_Questions_and_Divergences.md` · `On_Incense_and_the_Altar.md` · `CLAUDE.md` · `validate_project.py` · all of `src/`.

⛔ **`DQ-9` not moved · `DQ-24` not moved · no Discord state touched.**

**Validator AFTER: `82 ok · 9 warnings · 0 errors`** — identical to baseline, same nine codes, listed in `passes/260835-25_validator-after.txt`.

*(§5 rule 11 — this document makes no claim about its own commit state.)*
