# PASS 260835-74 — Cleanup of owed items: close-out

**Stamp:** `260835-74` (assigned by brief, not derived). **Date:** 2026-10-09. **Run on:** JD's computer, in `~/EMC/theology` and `~/EMC/staging-74`.
**Commits:** none. **`git add`:** none. JD commits.
**Skills announced at the start of the pass:** `anchor-edits-and-large-files` (logged byte offsets in the Followup raw; the anchor-only edit rule) and `canonical-document-discipline` (stamped ledgers, §4 registry, the never-alter changelog rules).

---

## 1. Gate checks

### Gate 1 — HEAD and status (verbatim)

```
$ git -C ~/EMC/theology rev-parse HEAD
47a8a4b5bbd798ee19af9ae86af87259c86c1245
$ git -C ~/EMC/theology status --short
(empty: no output)
```

- `c0177c2` **is** an ancestor of HEAD (`git merge-base --is-ancestor c0177c2 HEAD` succeeded). HEAD is one commit past it: `47a8a4b` *"rj 10 9 reply"*, JD, 2026-10-09 17:32:17 -0400.
- `git status --short` was empty before the first edit, so the gate passed.

### Gate 2 — validator baseline

`105 ok · 10 warnings · 0 errors`, matching the brief exactly. The full output is in Appendix A. Every check code with its full title name:

`C0 - registry resolution` · `C1 - relative timestamps in archives` · `C2 - source-tag numbering` · `C3 - version stamps vs registry` · `C4 - stale answered-question status` · `C5 - volatile-state duplication` · `C6 - archive hash integrity` · `C7 - relay-clean firewall (WARN-only, suspended)` · `C8 - dangling question-ID cross-references` · `C9 - do-not-deploy consistency` · `C10 - section 15 staleness` · `C11 - outline-vs-findings drift` · `C12 - session-registry integrity / dual capture`.

The ten baseline warnings:
- `C1 - relative timestamps in archives`: RPW, 4 loose
- `C4 - stale answered-question status`: Distinctives, 2
- `C5 - volatile-state duplication`: Question List 17, RJ_Incense_Analysis 9, Distinctives 7
- `C10 - section 15 staleness`: DQ 9 behind, IP 7 behind, LS 21 behind
- `C11 - outline-vs-findings drift`: DQ 11 unreviewed, IP 17 unreviewed

### Gate observation, reported to JD at the start of the pass

`47a8a4b` changed `src/SRC_Discord_Followup-raw.txt` after `260835-72`. Its sha256 is now `63920d327fbe759d5679cc1f8292533a7cf8e89c73e6f3c1effa0cad86c89f58` (89,131 B, 788 lines by `wc -l`), not `48bb0a58…` (83,190 B, 754 lines). The commit did two things:

1. **JD's 10/9 3:23 PM post was edited in place.** The two captures are byte-identical for bytes 0–82,963 and diverge at byte 82,964. The sentence *"…because God doesn't institute worship yet not require it; and if it only permits incense…"* now reads *"…because any worship that God institutes, He also requires it to be performed; and as a result, if it only permits incense…"*.
2. **Three Rev. James posts were appended:** 10/9 at 4:49, 5:08 and 5:24 PM. The 5:24 PM post quotes JD's edited wording.

Every byte offset logged in `DQ-29`…`DQ-37` and the JD-RECORD block ends at or before 82,824. All of them therefore resolve to identical bytes in both captures.

---

## 2. Per-task results

### Task 1 — close-outs filed

- I copied `260835-72_followup-intake-and-reserve_close-out.md` (sha256 `df8a2620…`) and `260835-73_memory-card_close-out.md` (sha256 `c1eb49e9…`) into `passes/` unchanged. The sha256 values match source and copy.
- The `.diff` files were not copied, as the brief instructed.
- `passes/README.md` does not index close-outs, so no rows were added.

### Task 2 — Followup archive of record

**Format.** I read `src/SRC_Discord_RPW.md` for the format and the `SRC_Manifest.md` Discord section for the rules (capture method and dating rule; the U+202F whole-class ruling; header shapes; the appended-changelog rule from `260835-29`). I checked orientation on the first post (`JD Smith` / `OP` / ` — 9/5/26, 9:55 AM`, then the text) and read every post the same way.

**Build.** `src/SRC_Discord_Followup.md` was built by script (`work/parse_raw.py`, `work/build_archive.py`) from the raw bytes at `47a8a4b`:
- **64 messages under 32 client headers.** JD has 43 messages under 15 headers; Rev. James has 21 under 17.
- Each message has a `### date, time — speaker` heading. Under it is a line giving the `message N` number, the resolved absolute date-time, its header and part-of-header position, the raw byte range, and the dating warrant.
- **Message breaks.** A single newline joining two non-empty lines inside a header block is treated as a break when the earlier line ends a sentence. The exceptions are list markers, bullets, numbered items, and one determination.
  - The breaks are listed in Appendix F with their raw byte positions.
  - Corroboration: every resulting message is ≤ 2,000 characters (maximum 1,996), Discord's per-message limit. Twelve of the 32 header blocks exceed that limit, so they must contain more than one message.
  - The determination is **message 58** (Rev. James, 10/8, 2:18 PM), kept as one message. JD reported at `260835-72` an in-message whitespace edit after its first sentence. Discord trims trailing whitespace, so that edit can only have been inside a single message. Flagged for JD.
- **Date resolutions:**
  - 9/5–10/7: the client's own full dates.
  - JD 10/8 1:28 PM and Rev. James 10/8 2:18 PM: from the client's `Yesterday` form in a 10/9 capture, which agrees with `260835-72`.
  - All 10/9 headers: bare, resolved to 2026-10-09 by commit-timestamp-plus-elimination against `47a8a4b` (the weaker class, so labelled).
- **Normalisation:** header-only. U+202F becomes a space (all 32 in the raw are in headers), and JD's three-line OP header is folded.
- **Byte-faithfulness:** all 64 message texts were re-extracted from the written archive and compared byte-for-byte with their raw slices, and all matched.
- **Dated notes in the archive:**
  - message 61, JD's in-place edit (the archived text is the text Rev. James answered);
  - message 58, the determination above;
  - message 7, the attribution boundary for the 1899 Opinion text he posted unquoted.
- **The archive's own hash.** The header records the sha256 of the message region (`899e36bc…`), because a file cannot carry its own whole-file hash. The whole-file sha256 is in the manifest: `405a28f47f2729b9ff1130890a385b08222ce896d8a2d31dff71de3ea5da53aa`, 118,425 B, 1,203 lines.
- **C1 safety.** The archive contains no `Yesterday at <digit>` string, which `C1 - relative timestamps in archives` would flag. This was asserted in the build.

**Registration:**
- `SRC_Manifest.md`: a dated note beside the raw artifact's `260835-72` note (row not edited). It records the raw's move and states that `DQ-29`…`DQ-37` offsets stay against `48bb0a58…` and are not re-based. It includes the `DQ`-to-message map (Appendix G).
- The archive has its own section after that note. A dated note under the aliases table says `DQ-Thread-Followup` now resolves to it.
- A `PROJECT_STATE.md` §4 row was added. Without it, `C1` and `C6` would not see the file, because they derive their file set from §4.

**Validator after Task 2:** `108 ok · 10 warnings · 0 errors`. New ok lines:
- `C0 - registry resolution`: the archive resolves.
- `C1 - relative timestamps in archives`: no unresolved timestamps.
- `C6 - archive hash integrity`: hash matches the manifest.

No new warning from `C1` or `C6`.

### Task 3 — staging-69's committed outputs

- `git show --stat 0883e4f` added five files: `Church_Of_Ireland_Incense_Prohibition.md` and four `src/` captures (the stat output is in Appendix H).
- `Church_Of_Ireland_Incense_Prohibition.md` now has a §4 row. Its stamp, read from its own header (*"PASS 260835-69. STAMP ASSIGNED, NOT DERIVED."*), is `260835-69`. Its class is Backstage, EXTERNAL RESEARCH pass report.
  - ⚠️ The file has no `**Last updated:**` line. The version cell is therefore written as *"260835-69 (unstamped: …)"*, and `C3 - version stamps vs registry` warns *unstamped*, which is the validator's designed signal for this state.
  - Adding the line would be an edit to the document, so it is left as JD's call.
- The four captures are registered in `SRC_Manifest.md` (manifest only, per the `260835-58`/`65` convention: no §4 row, no ledger number), with sha256, bytes and lines. Work and provenance are taken from each file's own capture header.
- All five files are byte-identical to their staging-69 copies (`cmp`).
- **staging-69 contains no close-out or report file;** recorded.
- Not registered: `src/Book_of_Common_Prayer_(Church_of_Ireland,_1878).pdf`, committed separately at `7022633`. Owed (see §5).

### Task 4 — staging-70's files

- **Nine files, not eight. No close-out.** The full inventory (size, sha256, first 20 lines of each) is in Appendix C.
- **The Orthodox report** is placed at the root as `Orthodox_Malachi_1_11_And_Incense_Warrant.md`. Its own §7 file table gives that name ("this document"). It has a §4 row at its own stamp `260835-70`, unstamped in the sense above, so `C3` warns.
  - ⚠️ Its `[Stated]` label means "verbatim from a capture file", which conflicts with the project rule that `[Stated]` is for Rev. James's words only. This is recorded in its row; the document is not edited.
- **The older Cyril capture** (`SRC_PRIMARY_2012_Cyril-…`, 4,217 B, sha256 `923832c4…`) covers printed pp. 298–299 only. The `0430` file (pp. 295–299, JD-verified) contains every passage in it.
  - After joining hyphenated line-splits and collapsing whitespace, the only differences are: the older capture's own `[LEMMA]`/`[COMMENT]` labels; its abridgement of the Isaiah/Jeremiah proof texts; page-break apparatus and OCR artifacts in `0430` (footnotes 30–32, running heads, *"of fering"*, a stray `?`); and one apostrophe (`Christ’s` in `0430`, `Christ's` in the older capture).
  - **Wholly contained, so NOT added**, and recorded as superseded in the manifest. The `diff -u` (raw and reflowed) is in Appendix D.
- **The six other captures** were placed in `src/` under their own names (byte-identical to staging) and registered in the manifest with sha256. Copyright notes were carried from their headers (Theodore and the OSB are © and for internal use only; the OSB Mal 1:11 note is FROZEN pending a printed-copy check).
- **Nothing unclassifiable** was left unplaced.

### Task 5 — registry gap

- **GATE FINDING 3's two files** (`Ceremonial_Meaning_Source_Checks.md`, `Incense_Reply_Source_Checks.md`) **already had §4 rows**, registered at `260835-65` on JD's ruling. No duplicate rows were added. A dated note beside GATE FINDING 3 records that it is discharged and when.
- **Tracked-files versus §4 diff** (`git ls-files` against the §4 path column), root-level `.md` with no row:
  - **Registered at `260835-74`**, each with its stamp read from its own header and class read from its own description:
    - `Homilies_On_Incense.md` (`260835-59`)
    - `Post_1900_Authorization_Of_Incense.md` (`260835-60`)
    - `Ritual_Canon_1874_To_1904.md` (`260835-61`)
    - `Ritual_Canon_Examples_And_REC_Split.md` (`260835-62`)
    - `Ritual_Canon_1874_Dissent_Register_And_Pamphlet.md` (`260835-64`)
    - `REC_Prayer_Book_1874_Ceremonial.md` (`260835-66`)
  - **Plus** `Church_Of_Ireland_Incense_Prohibition.md` (Task 3) and the newly placed Orthodox report (Task 4).
  - **OWED:** `DQ_Mint_Draft_20260809_Reservation.md` (`260835-67`). Its class can't be read from the file: it is a withdrawn DRAFT that may belong in `passes/`.
  - **Non-`.md` tracked files without a row:** `.gitignore` (exempt by the `260728-2` decision) and `theology.code-workspace` (editor configuration; exemption owed to JD).
- **None of the eight newly registered reports has a `**Last updated:**` line.** Each version cell therefore says *unstamped*, and `C3 - version stamps vs registry` warns eight times. These warnings are real, and they are not suppressed.
- **Audience** cells are set to "JD only" by series precedent and marked for JD to confirm.

### Task 6 — `C11 - outline-vs-findings drift`

**Reading.** I read `DQ-27`…`DQ-37` (and `DQ-28-P`) in full, the whole of `Incense_Conversational_Outline.md`, and `IP-109`…`IP-125` in full.

**DQ arm.** One dated REVIEWED block was placed after the `260835-72` reserve register, in the `260835-31` format: per finding, per step, UNAFFECTED, CONFIRMS or CHANGES-WHAT-IS-AVAILABLE, with reasons.
- **The scope limit is recorded in the block.** Rev. James's 10/9 replies are archived but not minted, so they are not reviewed. A further `DQ` review is owed once `DQ-38` onward exist.
- **Five dated notes beside steps (6.3), each flagged for JD, no argument text changed:**
  1. **Spoken core.** `DQ-28`(d) answers the *"violating that verse"* clause, and `DQ-37` shows the core's dilemma isn't exhaustive.
  2. **Step 1.** The *"violation"* clause, against `DQ-28`(d).
  3. **Step 5,** at the circumcision illustration. `DQ-37`(c) describes circumcision as "made wider", and the note points to Step 6's paragraph.
  4. **Step 8,** at the `260833-1` update. Its "discussed, therefore strong" conclusion is exposed by `DQ-28`/`DQ-32`/`DQ-37`.
  5. **Step 9,** at the 1899 sentence. Its gloss meets his reading in `DQ-29`(f)/`DQ-34`(c).
- **One correction to the `260835-72` overlay,** by dated note inside the review block:
  - Step 2b was carried as unspent, but JD posted points 1–3 and the held-back fifth argument on 9/17, and the act-level texts on 10/4.
  - Step 2's three-category framework was also posted on 9/17.
  - Byte offsets for all of these are given in the block.
- **Two items found outside the review, reported only:** the Step 9 Church of Ireland attribution (a canon, not the BCP, per `260835-69`), and the spoken core's closing grammar against reserve item 12.
- **6.4.** After the block was written, `CHECKED-AGAINST` moved from `DQ-26 @ 260835-31` to `DQ-37 @ 260835-74`, with the prior value kept in the pointer's history.

**IP arm (6.5), done.** The context allowed it, so I reviewed all seventeen (`File 85`, all under open ear flags) in a second REVIEWED block directly after the DQ block. Nothing in it is quotable at him.
- **Four further dated notes:**
  1. **Spoken core:** `IP-114`, *"literally done today"*.
  2. **Step 3(b)(1):** `IP-119`, *"Will means command"*, and `IP-114`, necessary consequence.
  3. **Step 5,** at the narrow principle: `IP-115`, `IP-121` and `IP-119`.
  4. **Step 5b,** at question 4: `IP-120` and `IP-115`.
- **This pass's own Step 8 note was extended before commit** with `IP-119` as the same-day spoken counterweight. The evidence supports a split between written and spoken statements, not between discussion and catechesis.
- `IP-118`'s `s1301` sentence (speaker unconfirmed) was **not used**.
- After the block was written, `CHECKED-AGAINST` moved from `IP-108 @ 260835-32` to `IP-125 @ 260835-74`, with the prior value kept.
- **Total dated notes beside steps: nine.** No step's argument text was rewritten.

### Task 7 — `C10 - section 15 staleness`, `DQ` arm

I read §15 and the `260835-65` sweep convention. A new sweep section for `DQ-29`…`DQ-37` was placed after it.

**Eight credits:**
1. The prudential objection allowed (`DQ-29`(d)).
2. His exact transcription of the 1899 conclusion (`DQ-29`(f)).
3. His own definition, offered when he asked for JD's (`DQ-30`, the giving and not the content).
4. Level (1) marked "my position", and his bishop's non-use volunteered (`DQ-32`(b)).
5. An accurate correction that JD accepted (`DQ-34`(a)).
6. Agreement that demanding a prohibiting verse is the normative principle's demand (`DQ-35`(a)).
7. Scripture as the agreed ground of decision (`DQ-33`/`DQ-35`/`DQ-36`).
8. Fulfillment and the set-aside Aaronic priesthood as common frame (`DQ-37`(a)/(b)).

**Everything else declined with a reason.** The unanswered questions were declined as coverage facts, under the guard that a non-answer is not soundness.

The `IP` and `LS` ledger heads are deliberately not named, per the `260835-65` caveat. The `DQ` arm of `C10` now reads `within 0 findings (DQ-37)`. The IP arm (7) and LS arm (21) still warn, unchanged.

### Task 8 — memory card

- **One dated note below the Layer A table;** the table is not edited. It says Step 2 is **SPENT 10/9** as well as 10/8.
- **Byte verification:**
  - The brief's wording *"If Malachi 1:11 institutes incense for the church in any sense, then it's required, because God doesn't institute worship yet not require it"* occurs **once in the `48bb0a58…` capture, at [byte @82,872–83,012]**. Its cue clause is at 82,964–83,012.
  - ⚠️ It occurs **zero times in the current `63920d32…` capture**, because JD later edited it. The current sentence (*"…because any worship that God institutes, He also requires it to be performed"*) is at **[byte @82,872–83,032]**.
  - Rev. James quotes the edited form at **[byte @87,696–87,856]**.
- **Both wordings are recorded as available Step 2 cues in JD's own words.** The choice is left to JD.
- The note also records that the point now has a reply in the thread (archive message 64, not minted), and that Step 2's framework was already posted on 9/17.
- **Stamp and row.** The card's stamp moved to `260835-74`, with a changelog entry prepended and its §4 row bumped. Because the outline's stamp moved (Task 6), a one-line dated note beside the derivation pointer says the card was not re-derived and is stale by its own rule. The pointer itself is unmoved at `260835-72`.

### Task 9 — `PROJECT_STATE.md` reconcile

At the head of `PROJECT_STATE.md` I added one changelog line and one GATE block, in the existing style. The block lists every owed item as **DONE at `260835-74`** (with its task number) or **STILL OWED** (with its reason). The four items the brief named are listed as still owed:
- Eusebius *DE* 1.10.
- The Perowne and Simeon wordings.
- The public paper's prep: `handout/` does not exist, and `RPW_Primer_Questions.md` was not found anywhere under `~/EMC`. I searched by name; its only mention is in the `260835-72` close-out.
- JD's decision on the core's closing line against item 12's grammar.

### Task 10 — validate, changelog, close-out

- **Validator after all edits:** `119 ok · 15 warnings · 0 errors`. It is in full in Appendix B, and the movement is explained in §4 below.
- **Changelog entries prepended and stamps bumped,** each with its §4 row bumped, where the prior cell text is retained:
  - `St_Francis_EMC_Distinctives.md`
  - `Incense_Conversational_Outline.md`
  - `SRC_Manifest.md`, where the stamp line and a `**260835-74:**` paragraph sit at the head, per that file's own pattern
  - `Incense_Outline_Memory_Card.md`
  - `PROJECT_STATE.md`
- **New files** were not given changelogs: they are byte copies of other passes' work, or a new archive with its own appended changelog.
- **Written to `~/EMC/staging-74/`:** `260835-74.diff` (the full `git diff`), `260835-74_status.txt` (`git status --short`), and `new/`, which holds every untracked file, path-preserved and checked with `cmp`. Working scripts and intermediate files are in `work/`.
- `work/outline_pre_t6.bak` is a working copy of the outline taken before Task 6. It is not a deliverable.

---

## 3. Files touched, and the anchors used

All edits used Python anchor-text replacement with a `count != 1` fatal pre-check before any write (`work/anchor.py`). No edit used a line number. Appendix E is the verbatim log of every anchor, 39 edits, each with its file, mode and anchor head.

| File | What changed |
|---|---|
| `src/SRC_Discord_Followup.md` | **NEW.** The archive of record. |
| `SRC_Manifest.md` | A raw-artifact `260835-74` note with the `DQ` map, and the archive section after it. A dated note under the aliases table. The `wc -l` correction to this pass's own note before commit. Two new external-capture sections before `# Dual-Capture Reconciliation Procedure`. The stamp line and a `260835-74` paragraph. |
| `PROJECT_STATE.md` | A §4 row for the archive. Eight §4 rows for reports. A discharge note beside GATE FINDING 3. Rows bumped for the Distinctives, outline, manifest, card and itself. The stamp, the changelog line and the GATE block at the head. |
| `Incense_Conversational_Outline.md` | The DQ and IP REVIEWED blocks, nine dated notes, `CHECKED-AGAINST` moved twice with history, the stamp line and a changelog entry. |
| `St_Francis_EMC_Distinctives.md` | The §15 sweep section before `## 16.`, the stamp line and a changelog entry. |
| `Incense_Outline_Memory_Card.md` | The stamp, a changelog entry, a stale note beside the pointer, and the Step 2 note below Layer A. |
| `passes/260835-72_…_close-out.md`, `passes/260835-73_…_close-out.md` | **NEW** (byte copies). |
| `Orthodox_Malachi_1_11_And_Incense_Warrant.md` | **NEW** (a byte copy from staging-70). |
| `src/SRC_PRIMARY_0743_…`, `_0787_…`, `_1899_Sokolof_…`, `_2004_Theodore_…`, `_2008_Orthodox-Study-Bible_…`, `src/SRC_SECONDARY_2026_…` | **NEW** (byte copies from staging-70). |

Nothing in `~/EMC/staging-69`, `staging-70`, `staging-72` or `staging-73` was modified.

---

## 4. Validator: what moved from the baseline, and why

**Baseline `105 ok · 10 warnings · 0 errors` → after `119 ok · 15 warnings · 0 errors`.**

**ok +14:**
- `C0 - registry resolution`: +9, the nine new §4 rows (37 → 46 files).
- `C1 - relative timestamps in archives`: +1, the Followup archive (5 → 6).
- `C6 - archive hash integrity`: +1, the Followup archive hash matches the manifest (5 → 6).
- `C10 - section 15 staleness`: +1, the `DQ` arm now reads *within 0 findings (DQ-37)* (Task 7).
- `C11 - outline-vs-findings drift`: +2, DQ current at `DQ-37 @ 260835-74` and IP current at `IP-125 @ 260835-74` (Task 6).
- 9 + 1 + 1 + 1 + 2 = 14.

**Warnings −3:**
- `C10 - section 15 staleness`, DQ arm, cleared because the sweep was done.
- `C11 - outline-vs-findings drift`, DQ and IP arms, cleared because the reviews were done.

**Warnings +8:**
- `C3 - version stamps vs registry` warns *"registry marks it unstamped"* on each of the eight newly registered reports, which carry no `**Last updated:**` line.
- 10 − 3 + 8 = 15.

**Expected movement that did not happen as the brief predicted:** "new `C0`/`C3` ok lines for new registry rows". `C0` gained nine ok lines. `C3` gained **no** ok lines: `C3` skips `SRC_Discord_*` archives by design, and the eight reports have no parseable stamp. That is reported, not engineered around.

**Coverage moves with no change in verdict:**
- `C3 - version stamps vs registry`: 31 → 39 files.
- `C5 - volatile-state duplication`: 25 → 33 files. The total stays at 34 assertions.
- `C8 - dangling question-ID cross-references`: 34 → 43 files.

**Unchanged:**
- `C2 - source-tag numbering`: DQ-1..37 and IP-1..125 still unbroken. Nothing was minted.
- `C4 - stale answered-question status`: Distinctives, 2.
- `C5 - volatile-state duplication`: the same three warnings.
- `C7 - relay-clean firewall (WARN-only, suspended)`: ok.
- `C9 - do-not-deploy consistency`: ok.
- `C12 - session-registry integrity / dual capture`: ok, still 77 capture rows across 66 sessions.
- The `C1` RPW loose warning.
- `C10` IP (7) and LS (21).

During the pass there was **one transient error, cleared before the final run:** `C3 - version stamps vs registry` VERSION DRIFT on the memory card between Task 8 (stamp bumped) and Task 10 (row bumped).

---

## 5. Not done / owed

1. **Intake of Rev. James's three 10/9 replies** (archive messages 62–64). They are not minted, and next free `DQ` is `DQ-38`. A further `C11 - outline-vs-findings drift` `DQ` review and a `C10 - section 15 staleness` sweep follow once they are minted. **Reason:** this is new capture outside the brief, and minting is content work.
2. **Eusebius *DE* 1.10** (reserve item 9): unread. Not this pass's to do.
3. **The Perowne and Simeon wordings** (reserve items 5 and 7): unverified against editions. Not this pass's to do.
4. **The public paper's prep.** `handout/` does not exist, and `RPW_Primer_Questions.md` was not found under `~/EMC`. Not this pass's to do.
5. **JD's decision on the spoken core's closing line versus reserve item 12's grammar.** It is JD's text.
6. **JD's review of archive message 58** (one message by determination) and of the single-newline break rule.
7. **JD's choice of Step 2 cue** (memory card): as first posted, or as edited.
8. **Memory card re-derivation.** It is stale by its own rule since the outline moved to `260835-74`.
9. **Nine dated-note flags in the outline:** the spoken core ×2, Step 1, Step 3(b)(1), Step 5 ×2, Step 5b, Step 8 and Step 9. All are JD's one-hunk calls.
10. **The Church of Ireland attribution correction** in outline Step 9 and `RJ_Incense_Analysis.md` §8 (a canon, not the BCP). It needs a fresh authorisation, per `0883e4f`.
11. **`DQ_Mint_Draft_20260809_Reservation.md`**: not registered, because its class can't be read from the file.
12. **`theology.code-workspace`**: exemption from §4 to be confirmed.
13. **`**Last updated:**` lines for the eight newly registered reports** (`C3 - version stamps vs registry` warns *unstamped*). Adding them is an edit to each document and is JD's call.
14. **"JD only" Audience** on those eight rows, to confirm.
15. **The Orthodox report's `[Stated]` convention conflict.** Recorded and not edited.
16. **Two `src/` files not in `SRC_Manifest.md`:** `src/Book_of_Common_Prayer_(Church_of_Ireland,_1878).pdf` (19,607,519 B, `7022633`) and `src/SRC_PRIMARY_1874_ReformedEpiscopalChurch_Book-of-Common-Prayer_Front-Matter-and-Ceremonial-Search.txt` (`260835-66`). **Reason:** outside the brief's "files that commit added".
17. **`C10 - section 15 staleness`, IP arm (`IP-119`…`IP-125`) and LS arm (`LS-121`…`LS-141`)**: not swept, and outside this brief.
18. **The `CAPTURED …` line debt.** The `47a8a4b` recapture carries none.
19. **The Orthodox report's own §6 owed work:** Theodoret; Germanus; the OSB note against print; the *FOTC* 124 year.

---

## Appendix A — validator BASELINE, in full (before any edit)

```
========================================================================
PROJECT INTEGRITY VALIDATION   root: /sessions/rcw-016draygadtjjsx7wygrckyn/mnt/EMC/theology
========================================================================
  ok    [C0] PROJECT_STATE.md: resolved at registered path
  ok    [C0] ORCHESTRATION.md: resolved at registered path
  ok    [C0] passes/README.md: resolved at registered path
  ok    [C0] St_Francis_EMC_Distinctives.md: resolved at registered path
  ok    [C0] RJ_Final_Question_List.md: resolved at registered path
  ok    [C0] RJ_Open_Questions_and_Divergences.md: resolved at registered path
  ok    [C0] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: resolved at registered path
  ok    [C0] Protestant_Commentary_Survey_Malachi_1_11.md: resolved at registered path
  ok    [C0] Patristic_Citations_Incense_Verification.md: resolved at registered path
  ok    [C0] Tertullian_Incense_Passages.md: resolved at registered path
  ok    [C0] Brattston_Article_Assessment.md: resolved at registered path
  ok    [C0] Frere_Appendix_A_Translated.md: resolved at registered path
  ok    [C0] Orthodox_Bridge_Rebuttal_Assessment.md: resolved at registered path
  ok    [C0] Malachi_1_11_Lexical_Analysis.md: resolved at registered path
  ok    [C0] Ceremonial_Meaning_Source_Checks.md: resolved at registered path
  ok    [C0] Incense_Reply_Source_Checks.md: resolved at registered path
  ok    [C0] American_Episcopal_Reception_1899_Opinion.md: resolved at registered path
  ok    [C0] Ritualist_Case_For_Incense_and_the_1899_Opinion.md: resolved at registered path
  ok    [C0] RJ_Incense_Analysis.md: resolved at registered path
  ok    [C0] On_Incense_and_the_Altar.md: resolved at registered path
  ok    [C0] Incense_Conversational_Outline.md: resolved at registered path
  ok    [C0] Incense_Outline_Memory_Card.md: resolved at registered path
  ok    [C0] SRC_Manifest.md: resolved at registered path
  ok    [C0] SRC_Channel_Inventory.md: resolved at registered path
  ok    [C0] SRC_Coverage_Register.md: resolved at registered path
  ok    [C0] asr_keyterms_A101.md: resolved at registered path
  ok    [C0] src/SRC_Discord_RPW.md: resolved at registered path
  ok    [C0] src/SRC_Discord_Assurance.md: resolved at registered path
  ok    [C0] src/SRC_Discord_Assurance-raw.txt: resolved at registered path
  ok    [C0] src/SRC_Discord_39ArticlesFormularies.md: resolved at registered path
  ok    [C0] src/SRC_Discord_SevenSacraments.md: resolved at registered path
  ok    [C0] src/SRC_Discord_BaptismConfirmation.md: resolved at registered path
  ok    [C0] README.md: resolved at registered path
  ok    [C0] Project_Bootstrap_Prompt.md: resolved at registered path
  ok    [C0] tools/transcribe_yt.py: resolved at registered path
  ok    [C0] validate_project.py: resolved at registered path
  ok    [C0] CLAUDE.md: resolved at registered path
  ok    [C1] src/SRC_Discord_39ArticlesFormularies.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_Assurance.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_BaptismConfirmation.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_SevenSacraments.md: no unresolved relative timestamps
  ok    [C2] DQ-1..37 unbroken, no duplicates
  ok    [C2] IP-1..125 unbroken, no duplicates
  ok    [C2] RV-1..63 unbroken, no duplicates
  ok    [C2] LS-1..141 unbroken, no duplicates
  ok    [C2] BLOG-1..158 unbroken, no duplicates
  ok    [C2] POD-1..16 unbroken, no duplicates
  ok    [C3] PROJECT_STATE.md: version agrees with registry (260835-73)
  ok    [C3] ORCHESTRATION.md: version agrees with registry (260835-37)
  ok    [C3] passes/README.md: version agrees with registry (260832-3)
  ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260835-72)
  ok    [C3] RJ_Final_Question_List.md: version agrees with registry (260835-72 (v23))
  ok    [C3] RJ_Open_Questions_and_Divergences.md: version agrees with registry (260833-2)
  ok    [C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: version agrees with registry (260832-2)
  ok    [C3] Protestant_Commentary_Survey_Malachi_1_11.md: version agrees with registry (260835-45)
  ok    [C3] Patristic_Citations_Incense_Verification.md: version agrees with registry (260835-47)
  ok    [C3] Tertullian_Incense_Passages.md: version agrees with registry (260835-48)
  ok    [C3] Brattston_Article_Assessment.md: version agrees with registry (260835-49)
  ok    [C3] Frere_Appendix_A_Translated.md: version agrees with registry (260835-50)
  ok    [C3] Orthodox_Bridge_Rebuttal_Assessment.md: version agrees with registry (260835-51)
  ok    [C3] Malachi_1_11_Lexical_Analysis.md: version agrees with registry (260835-52)
  ok    [C3] Ceremonial_Meaning_Source_Checks.md: version agrees with registry (260835-56)
  ok    [C3] Incense_Reply_Source_Checks.md: version agrees with registry (260835-65)
  ok    [C3] American_Episcopal_Reception_1899_Opinion.md: version agrees with registry (260835-55)
  ok    [C3] Ritualist_Case_For_Incense_and_the_1899_Opinion.md: version agrees with registry (260835-39)
  ok    [C3] RJ_Incense_Analysis.md: version agrees with registry (260835-65)
  ok    [C3] On_Incense_and_the_Altar.md: version agrees with registry (260833-2)
  ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260835-72)
  ok    [C3] Incense_Outline_Memory_Card.md: version agrees with registry (260835-73)
  ok    [C3] SRC_Manifest.md: version agrees with registry (260835-72)
  ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260835-72)
  ok    [C3] SRC_Coverage_Register.md: version agrees with registry (260835-72)
  ok    [C3] asr_keyterms_A101.md: version agrees with registry (260830-2)
  ok    [C3] README.md: version agrees with registry (260835-8)
  ok    [C3] Project_Bootstrap_Prompt.md: version agrees with registry (260816-1)
  ok    [C3] tools/transcribe_yt.py: version agrees with registry (260833-7)
  ok    [C3] validate_project.py: version agrees with registry (260835-39)
  ok    [C3] CLAUDE.md: version agrees with registry (260835-72)
  ok    [C4] RJ_Final_Question_List.md: no unmarked stale-status passages for answered questions
  ok    [C4] RJ_Incense_Analysis.md: no unmarked stale-status passages for answered questions
  ok    [C5] total volatile-state assertions outside PROJECT_STATE: 34
  ok    [C6] src/SRC_Discord_39ArticlesFormularies.md: hash matches manifest
  ok    [C6] src/SRC_Discord_Assurance.md: hash matches manifest
  ok    [C6] src/SRC_Discord_BaptismConfirmation.md: hash matches manifest
  ok    [C6] src/SRC_Discord_RPW.md: hash matches manifest
  ok    [C6] src/SRC_Discord_SevenSacraments.md: hash matches manifest
  ok    [C7] On_Incense_and_the_Altar.md: relay-clean firewall intact (class suspended; no cleanup owed)
  ok    [C7] Incense_Conversational_Outline.md: relay-clean firewall intact (class suspended; no cleanup owed)
  ok    [C8] all 4 QA-* citations resolve in the question list
  ok    [C8] all 7 VP- label(s) defined in the distinctives; 7 cited, none dangling
  ok    [C9] item 7: carries a retirement marker, consistent with the register
  ok    [C9] item 20: carries a retirement marker, consistent with the register
  ok    [C9] item 14: carries a retirement marker, consistent with the register
  ok    [C9] item 9: carries a retirement marker, consistent with the register
  ok    [C10] every finding flagged as common ground is credited in §15
  ok    [C10] §15 is within 1 finding(s) of the RV ledger head (RV-63)
  ok    [C10] §15 is within 0 finding(s) of the BLOG ledger head (BLOG-158)
  ok    [C10] §15 is within 0 finding(s) of the POD ledger head (POD-16)
  ok    [C11] RV current in the outline pointer (RV-63 @ 260830-1, ledger at RV-63)
  ok    [C12] session registry parsed: 77 capture row(s) across 66 session(s)
  ok    [C12] 27 standalone recording row(s) parsed and correctly EXCLUDED from the session count (manifest rule: a standalone recording gets no session row)
  ok    [C12] no capture is stuck in SECONDARY -- SWEEP PENDING
  ok    [C12] retrofit rule present: bare pre-260725 offsets resolve to their session's PRIMARY capture
  ok    [C12] no session row is awaiting completion
  ok    [C12] no finding is under the wording-critical quoting freeze
  WARN  [C1] src/SRC_Discord_RPW.md: 4 relative timestamp(s) outside message headers ('Yesterday at …'). Not caught by the header rule; check whether they are quoted text or unresolved captures.
  WARN  [C4] St_Francis_EMC_Distinctives.md: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby. Review manually.
  WARN  [C5] RJ_Final_Question_List.md: 17 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] RJ_Incense_Analysis.md: 9 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] St_Francis_EMC_Distinctives.md: 7 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C10] §15's newest DQ citation is 9 findings behind the ledger (DQ-28 vs DQ-37). Sweep the interval for creditable material.
  WARN  [C10] §15's newest IP citation is 7 findings behind the ledger (IP-118 vs IP-125). Sweep the interval for creditable material.
  WARN  [C10] §15's newest LS citation is 21 findings behind the ledger (LS-120 vs LS-141). Sweep the interval for creditable material.
  WARN  [C11] outline last checked against DQ-26 (260835-31); the DQ ledger now runs to DQ-37. 11 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.
  WARN  [C11] outline last checked against IP-108 (260835-32); the IP ledger now runs to IP-125. 17 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.
------------------------------------------------------------------------
COVERAGE SUMMARY — files examined per check
------------------------------------------------------------------------
  check  files  name                                         status
  C0        37  registry resolution                          OK
         └─ PROJECT_STATE.md
         └─ ORCHESTRATION.md
         └─ passes/README.md
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Tertullian_Incense_Passages.md
         └─ Brattston_Article_Assessment.md
         └─ Frere_Appendix_A_Translated.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Incense_Reply_Source_Checks.md
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ RJ_Incense_Analysis.md
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Outline_Memory_Card.md
         └─ SRC_Manifest.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Coverage_Register.md
         └─ asr_keyterms_A101.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_Assurance-raw.txt
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_SevenSacraments.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ README.md
         └─ Project_Bootstrap_Prompt.md
         └─ tools/transcribe_yt.py
         └─ validate_project.py
         └─ CLAUDE.md
  C1         5  relative timestamps in archives              OK
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_SevenSacraments.md
  C2         1  source-tag numbering                         OK
         └─ St_Francis_EMC_Distinctives.md
  C3        31  version stamps vs registry                   OK
         └─ PROJECT_STATE.md
         └─ ORCHESTRATION.md
         └─ passes/README.md
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Tertullian_Incense_Passages.md
         └─ Brattston_Article_Assessment.md
         └─ Frere_Appendix_A_Translated.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Incense_Reply_Source_Checks.md
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ RJ_Incense_Analysis.md
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Outline_Memory_Card.md
         └─ SRC_Manifest.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Coverage_Register.md
         └─ asr_keyterms_A101.md
         └─ README.md
         └─ Project_Bootstrap_Prompt.md
         └─ tools/transcribe_yt.py
         └─ validate_project.py
         └─ CLAUDE.md
  C4         3  stale answered-question status               OK
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Incense_Analysis.md
  C5        25  volatile-state duplication                   OK
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Brattston_Article_Assessment.md
         └─ CLAUDE.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Frere_Appendix_A_Translated.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Outline_Memory_Card.md
         └─ Incense_Reply_Source_Checks.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ ORCHESTRATION.md
         └─ On_Incense_and_the_Altar.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Project_Bootstrap_Prompt.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ README.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Incense_Analysis.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ St_Francis_EMC_Distinctives.md
         └─ Tertullian_Incense_Passages.md
         └─ asr_keyterms_A101.md
         └─ passes/README.md
  C6         5  archive hash integrity                       OK
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_SevenSacraments.md
  C7         2  relay-clean firewall (WARN-only, suspended)  OK
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
  C8        34  dangling question-ID cross-references        OK
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Brattston_Article_Assessment.md
         └─ CLAUDE.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Frere_Appendix_A_Translated.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Outline_Memory_Card.md
         └─ Incense_Reply_Source_Checks.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ ORCHESTRATION.md
         └─ On_Incense_and_the_Altar.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ PROJECT_STATE.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Project_Bootstrap_Prompt.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ README.md
         └─ RJ_Incense_Analysis.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Coverage_Register.md
         └─ SRC_Manifest.md
         └─ Tertullian_Incense_Passages.md
         └─ asr_keyterms_A101.md
         └─ passes/README.md
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_SevenSacraments.md
  C9         1  do-not-deploy consistency                    OK
         └─ RJ_Final_Question_List.md
  C10        1  section 15 staleness                         OK
         └─ St_Francis_EMC_Distinctives.md
  C11        2  outline-vs-findings drift                    OK
         └─ Incense_Conversational_Outline.md
         └─ St_Francis_EMC_Distinctives.md
  C12        2  session-registry integrity / dual capture    OK
         └─ SRC_Manifest.md
         └─ St_Francis_EMC_Distinctives.md
------------------------------------------------------------------------
105 ok · 10 warnings · 0 errors
Read the coverage summary before trusting the error count.
```

## Appendix B — validator AFTER, in full (after all edits)

```
========================================================================
PROJECT INTEGRITY VALIDATION   root: /sessions/rcw-016draygadtjjsx7wygrckyn/mnt/EMC/theology
========================================================================
  ok    [C0] PROJECT_STATE.md: resolved at registered path
  ok    [C0] ORCHESTRATION.md: resolved at registered path
  ok    [C0] passes/README.md: resolved at registered path
  ok    [C0] St_Francis_EMC_Distinctives.md: resolved at registered path
  ok    [C0] RJ_Final_Question_List.md: resolved at registered path
  ok    [C0] RJ_Open_Questions_and_Divergences.md: resolved at registered path
  ok    [C0] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: resolved at registered path
  ok    [C0] Protestant_Commentary_Survey_Malachi_1_11.md: resolved at registered path
  ok    [C0] Patristic_Citations_Incense_Verification.md: resolved at registered path
  ok    [C0] Tertullian_Incense_Passages.md: resolved at registered path
  ok    [C0] Brattston_Article_Assessment.md: resolved at registered path
  ok    [C0] Frere_Appendix_A_Translated.md: resolved at registered path
  ok    [C0] Orthodox_Bridge_Rebuttal_Assessment.md: resolved at registered path
  ok    [C0] Malachi_1_11_Lexical_Analysis.md: resolved at registered path
  ok    [C0] Ceremonial_Meaning_Source_Checks.md: resolved at registered path
  ok    [C0] Incense_Reply_Source_Checks.md: resolved at registered path
  ok    [C0] Church_Of_Ireland_Incense_Prohibition.md: resolved at registered path
  ok    [C0] Orthodox_Malachi_1_11_And_Incense_Warrant.md: resolved at registered path
  ok    [C0] Homilies_On_Incense.md: resolved at registered path
  ok    [C0] Post_1900_Authorization_Of_Incense.md: resolved at registered path
  ok    [C0] Ritual_Canon_1874_To_1904.md: resolved at registered path
  ok    [C0] Ritual_Canon_Examples_And_REC_Split.md: resolved at registered path
  ok    [C0] Ritual_Canon_1874_Dissent_Register_And_Pamphlet.md: resolved at registered path
  ok    [C0] REC_Prayer_Book_1874_Ceremonial.md: resolved at registered path
  ok    [C0] American_Episcopal_Reception_1899_Opinion.md: resolved at registered path
  ok    [C0] Ritualist_Case_For_Incense_and_the_1899_Opinion.md: resolved at registered path
  ok    [C0] RJ_Incense_Analysis.md: resolved at registered path
  ok    [C0] On_Incense_and_the_Altar.md: resolved at registered path
  ok    [C0] Incense_Conversational_Outline.md: resolved at registered path
  ok    [C0] Incense_Outline_Memory_Card.md: resolved at registered path
  ok    [C0] SRC_Manifest.md: resolved at registered path
  ok    [C0] SRC_Channel_Inventory.md: resolved at registered path
  ok    [C0] SRC_Coverage_Register.md: resolved at registered path
  ok    [C0] asr_keyterms_A101.md: resolved at registered path
  ok    [C0] src/SRC_Discord_RPW.md: resolved at registered path
  ok    [C0] src/SRC_Discord_Assurance.md: resolved at registered path
  ok    [C0] src/SRC_Discord_Assurance-raw.txt: resolved at registered path
  ok    [C0] src/SRC_Discord_Followup.md: resolved at registered path
  ok    [C0] src/SRC_Discord_39ArticlesFormularies.md: resolved at registered path
  ok    [C0] src/SRC_Discord_SevenSacraments.md: resolved at registered path
  ok    [C0] src/SRC_Discord_BaptismConfirmation.md: resolved at registered path
  ok    [C0] README.md: resolved at registered path
  ok    [C0] Project_Bootstrap_Prompt.md: resolved at registered path
  ok    [C0] tools/transcribe_yt.py: resolved at registered path
  ok    [C0] validate_project.py: resolved at registered path
  ok    [C0] CLAUDE.md: resolved at registered path
  ok    [C1] src/SRC_Discord_39ArticlesFormularies.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_Assurance.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_BaptismConfirmation.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_Followup.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_SevenSacraments.md: no unresolved relative timestamps
  ok    [C2] DQ-1..37 unbroken, no duplicates
  ok    [C2] IP-1..125 unbroken, no duplicates
  ok    [C2] RV-1..63 unbroken, no duplicates
  ok    [C2] LS-1..141 unbroken, no duplicates
  ok    [C2] BLOG-1..158 unbroken, no duplicates
  ok    [C2] POD-1..16 unbroken, no duplicates
  ok    [C3] PROJECT_STATE.md: version agrees with registry (260835-74)
  ok    [C3] ORCHESTRATION.md: version agrees with registry (260835-37)
  ok    [C3] passes/README.md: version agrees with registry (260832-3)
  ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260835-74)
  ok    [C3] RJ_Final_Question_List.md: version agrees with registry (260835-72 (v23))
  ok    [C3] RJ_Open_Questions_and_Divergences.md: version agrees with registry (260833-2)
  ok    [C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: version agrees with registry (260832-2)
  ok    [C3] Protestant_Commentary_Survey_Malachi_1_11.md: version agrees with registry (260835-45)
  ok    [C3] Patristic_Citations_Incense_Verification.md: version agrees with registry (260835-47)
  ok    [C3] Tertullian_Incense_Passages.md: version agrees with registry (260835-48)
  ok    [C3] Brattston_Article_Assessment.md: version agrees with registry (260835-49)
  ok    [C3] Frere_Appendix_A_Translated.md: version agrees with registry (260835-50)
  ok    [C3] Orthodox_Bridge_Rebuttal_Assessment.md: version agrees with registry (260835-51)
  ok    [C3] Malachi_1_11_Lexical_Analysis.md: version agrees with registry (260835-52)
  ok    [C3] Ceremonial_Meaning_Source_Checks.md: version agrees with registry (260835-56)
  ok    [C3] Incense_Reply_Source_Checks.md: version agrees with registry (260835-65)
  ok    [C3] American_Episcopal_Reception_1899_Opinion.md: version agrees with registry (260835-55)
  ok    [C3] Ritualist_Case_For_Incense_and_the_1899_Opinion.md: version agrees with registry (260835-39)
  ok    [C3] RJ_Incense_Analysis.md: version agrees with registry (260835-65)
  ok    [C3] On_Incense_and_the_Altar.md: version agrees with registry (260833-2)
  ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260835-74)
  ok    [C3] Incense_Outline_Memory_Card.md: version agrees with registry (260835-74)
  ok    [C3] SRC_Manifest.md: version agrees with registry (260835-74)
  ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260835-72)
  ok    [C3] SRC_Coverage_Register.md: version agrees with registry (260835-72)
  ok    [C3] asr_keyterms_A101.md: version agrees with registry (260830-2)
  ok    [C3] README.md: version agrees with registry (260835-8)
  ok    [C3] Project_Bootstrap_Prompt.md: version agrees with registry (260816-1)
  ok    [C3] tools/transcribe_yt.py: version agrees with registry (260833-7)
  ok    [C3] validate_project.py: version agrees with registry (260835-39)
  ok    [C3] CLAUDE.md: version agrees with registry (260835-72)
  ok    [C4] RJ_Final_Question_List.md: no unmarked stale-status passages for answered questions
  ok    [C4] RJ_Incense_Analysis.md: no unmarked stale-status passages for answered questions
  ok    [C5] total volatile-state assertions outside PROJECT_STATE: 34
  ok    [C6] src/SRC_Discord_39ArticlesFormularies.md: hash matches manifest
  ok    [C6] src/SRC_Discord_Assurance.md: hash matches manifest
  ok    [C6] src/SRC_Discord_BaptismConfirmation.md: hash matches manifest
  ok    [C6] src/SRC_Discord_Followup.md: hash matches manifest
  ok    [C6] src/SRC_Discord_RPW.md: hash matches manifest
  ok    [C6] src/SRC_Discord_SevenSacraments.md: hash matches manifest
  ok    [C7] On_Incense_and_the_Altar.md: relay-clean firewall intact (class suspended; no cleanup owed)
  ok    [C7] Incense_Conversational_Outline.md: relay-clean firewall intact (class suspended; no cleanup owed)
  ok    [C8] all 4 QA-* citations resolve in the question list
  ok    [C8] all 7 VP- label(s) defined in the distinctives; 7 cited, none dangling
  ok    [C9] item 7: carries a retirement marker, consistent with the register
  ok    [C9] item 20: carries a retirement marker, consistent with the register
  ok    [C9] item 14: carries a retirement marker, consistent with the register
  ok    [C9] item 9: carries a retirement marker, consistent with the register
  ok    [C10] every finding flagged as common ground is credited in §15
  ok    [C10] §15 is within 0 finding(s) of the DQ ledger head (DQ-37)
  ok    [C10] §15 is within 1 finding(s) of the RV ledger head (RV-63)
  ok    [C10] §15 is within 0 finding(s) of the BLOG ledger head (BLOG-158)
  ok    [C10] §15 is within 0 finding(s) of the POD ledger head (POD-16)
  ok    [C11] DQ current in the outline pointer (DQ-37 @ 260835-74, ledger at DQ-37)
  ok    [C11] IP current in the outline pointer (IP-125 @ 260835-74, ledger at IP-125)
  ok    [C11] RV current in the outline pointer (RV-63 @ 260830-1, ledger at RV-63)
  ok    [C12] session registry parsed: 77 capture row(s) across 66 session(s)
  ok    [C12] 27 standalone recording row(s) parsed and correctly EXCLUDED from the session count (manifest rule: a standalone recording gets no session row)
  ok    [C12] no capture is stuck in SECONDARY -- SWEEP PENDING
  ok    [C12] retrofit rule present: bare pre-260725 offsets resolve to their session's PRIMARY capture
  ok    [C12] no session row is awaiting completion
  ok    [C12] no finding is under the wording-critical quoting freeze
  WARN  [C1] src/SRC_Discord_RPW.md: 4 relative timestamp(s) outside message headers ('Yesterday at …'). Not caught by the header rule; check whether they are quoted text or unresolved captures.
  WARN  [C3] Church_Of_Ireland_Incense_Prohibition.md: registry marks it unstamped; no version to check. Add a '**Last updated:**' line so this file stops being invisible.
  WARN  [C3] Orthodox_Malachi_1_11_And_Incense_Warrant.md: registry marks it unstamped; no version to check. Add a '**Last updated:**' line so this file stops being invisible.
  WARN  [C3] Homilies_On_Incense.md: registry marks it unstamped; no version to check. Add a '**Last updated:**' line so this file stops being invisible.
  WARN  [C3] Post_1900_Authorization_Of_Incense.md: registry marks it unstamped; no version to check. Add a '**Last updated:**' line so this file stops being invisible.
  WARN  [C3] Ritual_Canon_1874_To_1904.md: registry marks it unstamped; no version to check. Add a '**Last updated:**' line so this file stops being invisible.
  WARN  [C3] Ritual_Canon_Examples_And_REC_Split.md: registry marks it unstamped; no version to check. Add a '**Last updated:**' line so this file stops being invisible.
  WARN  [C3] Ritual_Canon_1874_Dissent_Register_And_Pamphlet.md: registry marks it unstamped; no version to check. Add a '**Last updated:**' line so this file stops being invisible.
  WARN  [C3] REC_Prayer_Book_1874_Ceremonial.md: registry marks it unstamped; no version to check. Add a '**Last updated:**' line so this file stops being invisible.
  WARN  [C4] St_Francis_EMC_Distinctives.md: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby. Review manually.
  WARN  [C5] RJ_Final_Question_List.md: 17 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] RJ_Incense_Analysis.md: 9 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] St_Francis_EMC_Distinctives.md: 7 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C10] §15's newest IP citation is 7 findings behind the ledger (IP-118 vs IP-125). Sweep the interval for creditable material.
  WARN  [C10] §15's newest LS citation is 21 findings behind the ledger (LS-120 vs LS-141). Sweep the interval for creditable material.
------------------------------------------------------------------------
COVERAGE SUMMARY — files examined per check
------------------------------------------------------------------------
  check  files  name                                         status
  C0        46  registry resolution                          OK
         └─ PROJECT_STATE.md
         └─ ORCHESTRATION.md
         └─ passes/README.md
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Tertullian_Incense_Passages.md
         └─ Brattston_Article_Assessment.md
         └─ Frere_Appendix_A_Translated.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Incense_Reply_Source_Checks.md
         └─ Church_Of_Ireland_Incense_Prohibition.md
         └─ Orthodox_Malachi_1_11_And_Incense_Warrant.md
         └─ Homilies_On_Incense.md
         └─ Post_1900_Authorization_Of_Incense.md
         └─ Ritual_Canon_1874_To_1904.md
         └─ Ritual_Canon_Examples_And_REC_Split.md
         └─ Ritual_Canon_1874_Dissent_Register_And_Pamphlet.md
         └─ REC_Prayer_Book_1874_Ceremonial.md
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ RJ_Incense_Analysis.md
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Outline_Memory_Card.md
         └─ SRC_Manifest.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Coverage_Register.md
         └─ asr_keyterms_A101.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_Assurance-raw.txt
         └─ src/SRC_Discord_Followup.md
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_SevenSacraments.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ README.md
         └─ Project_Bootstrap_Prompt.md
         └─ tools/transcribe_yt.py
         └─ validate_project.py
         └─ CLAUDE.md
  C1         6  relative timestamps in archives              OK
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ src/SRC_Discord_Followup.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_SevenSacraments.md
  C2         1  source-tag numbering                         OK
         └─ St_Francis_EMC_Distinctives.md
  C3        39  version stamps vs registry                   OK
         └─ PROJECT_STATE.md
         └─ ORCHESTRATION.md
         └─ passes/README.md
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Tertullian_Incense_Passages.md
         └─ Brattston_Article_Assessment.md
         └─ Frere_Appendix_A_Translated.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Incense_Reply_Source_Checks.md
         └─ Church_Of_Ireland_Incense_Prohibition.md
         └─ Orthodox_Malachi_1_11_And_Incense_Warrant.md
         └─ Homilies_On_Incense.md
         └─ Post_1900_Authorization_Of_Incense.md
         └─ Ritual_Canon_1874_To_1904.md
         └─ Ritual_Canon_Examples_And_REC_Split.md
         └─ Ritual_Canon_1874_Dissent_Register_And_Pamphlet.md
         └─ REC_Prayer_Book_1874_Ceremonial.md
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ RJ_Incense_Analysis.md
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Outline_Memory_Card.md
         └─ SRC_Manifest.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Coverage_Register.md
         └─ asr_keyterms_A101.md
         └─ README.md
         └─ Project_Bootstrap_Prompt.md
         └─ tools/transcribe_yt.py
         └─ validate_project.py
         └─ CLAUDE.md
  C4         3  stale answered-question status               OK
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Incense_Analysis.md
  C5        33  volatile-state duplication                   OK
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Brattston_Article_Assessment.md
         └─ CLAUDE.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Church_Of_Ireland_Incense_Prohibition.md
         └─ Frere_Appendix_A_Translated.md
         └─ Homilies_On_Incense.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Outline_Memory_Card.md
         └─ Incense_Reply_Source_Checks.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ ORCHESTRATION.md
         └─ On_Incense_and_the_Altar.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Orthodox_Malachi_1_11_And_Incense_Warrant.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Post_1900_Authorization_Of_Incense.md
         └─ Project_Bootstrap_Prompt.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ README.md
         └─ REC_Prayer_Book_1874_Ceremonial.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Incense_Analysis.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Ritual_Canon_1874_Dissent_Register_And_Pamphlet.md
         └─ Ritual_Canon_1874_To_1904.md
         └─ Ritual_Canon_Examples_And_REC_Split.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ St_Francis_EMC_Distinctives.md
         └─ Tertullian_Incense_Passages.md
         └─ asr_keyterms_A101.md
         └─ passes/README.md
  C6         6  archive hash integrity                       OK
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ src/SRC_Discord_Followup.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_SevenSacraments.md
  C7         2  relay-clean firewall (WARN-only, suspended)  OK
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
  C8        43  dangling question-ID cross-references        OK
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Brattston_Article_Assessment.md
         └─ CLAUDE.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Church_Of_Ireland_Incense_Prohibition.md
         └─ Frere_Appendix_A_Translated.md
         └─ Homilies_On_Incense.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Outline_Memory_Card.md
         └─ Incense_Reply_Source_Checks.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ ORCHESTRATION.md
         └─ On_Incense_and_the_Altar.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Orthodox_Malachi_1_11_And_Incense_Warrant.md
         └─ PROJECT_STATE.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Post_1900_Authorization_Of_Incense.md
         └─ Project_Bootstrap_Prompt.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ README.md
         └─ REC_Prayer_Book_1874_Ceremonial.md
         └─ RJ_Incense_Analysis.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Ritual_Canon_1874_Dissent_Register_And_Pamphlet.md
         └─ Ritual_Canon_1874_To_1904.md
         └─ Ritual_Canon_Examples_And_REC_Split.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Coverage_Register.md
         └─ SRC_Manifest.md
         └─ Tertullian_Incense_Passages.md
         └─ asr_keyterms_A101.md
         └─ passes/README.md
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ src/SRC_Discord_Followup.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_SevenSacraments.md
  C9         1  do-not-deploy consistency                    OK
         └─ RJ_Final_Question_List.md
  C10        1  section 15 staleness                         OK
         └─ St_Francis_EMC_Distinctives.md
  C11        2  outline-vs-findings drift                    OK
         └─ Incense_Conversational_Outline.md
         └─ St_Francis_EMC_Distinctives.md
  C12        2  session-registry integrity / dual capture    OK
         └─ SRC_Manifest.md
         └─ St_Francis_EMC_Distinctives.md
------------------------------------------------------------------------
119 ok · 15 warnings · 0 errors
Read the coverage summary before trusting the error count.
```

## Appendix C — staging-70 inventory: every file with size, line count, sha256, and its first 20 lines (no close-out exists, so none is listed first)

```
=================== Orthodox_Malachi_1_11_And_Incense_Warrant.md
size 28189 B · lines 474 · sha256 83ec7a88a4b338388e86272a7caa8c20333b61ac557a4a41e1ffde958ed52321
repo copy: 
# Eastern Orthodox reading of Malachi 1:11, and the Orthodox warrant for liturgical incense

**Stamp: 260835-70.** ⛔ **ASSIGNED BY BRIEF, NOT DERIVED.** No stamp was derived
and the stamp registry was not read to confirm it, per the brief's instruction.

⛔⛔ **READ-ONLY PASS. `~/EMC/theology` WAS NOT WRITTEN TO.** No file in the
repository was created, edited, moved, renamed or deleted; no git command of any
kind was run, read or write. All output is in `~/EMC/staging-70`. Nothing was
copied into the repository and nothing was committed.

⛔ **NOTHING MINTED.** No `IP`, `DQ`, `GV`, `RC`, `BP`, `RV`, `EXT` or any other
ledger number consumed. No existing document altered.

⛔⛔⛔ **NOTHING WAS TRANSLATED BY THIS PASS.** Every English rendering below is
an existing published translation, named with its translator. Where no published
English translation could be reached, the entry is **UNMATCHED** and says so.

**Attribution layers:** `[Stated]` = verbatim from a capture file;
`[Stated-Analysis]` = labelled inference from something stated;
`[Analysis]` = this project's own argument.
=================== SRC_PRIMARY_0743_John-of-Damascus_Exposition-Orthodox-Faith-IV-13_Malachi-1-11_NPNF2-09-Salmond.txt
size 1993 B · lines 34 · sha256 6c3a31f6d7c383d13529b010c0d4e4d74b04d8c01ebf689ffca532f5bab544ef
repo copy: 
CAPTURE — 260835-70
SOURCE: St John of Damascus, An Exposition of the Orthodox Faith, Book IV,
        Chapter 13, "Concerning the holy and immaculate Mysteries of the Lord."
        English: S. D. F. Salmond, tr., Nicene and Post-Nicene Fathers,
        Second Series, Vol. 9 (1899). PUBLIC DOMAIN.
PROVENANCE: newadvent.org/fathers/33044.htm, read in-page 2026-09-08.
            Page innerText length 128,307 chars. Book IV runs Chapters 1-27.
            Scripture references shown inline are New Advent's editorial links.

--- BEGIN CAPTURE ---

With bread and wine Melchisedek, the priest of the most high God, received
Abraham on his return from the slaughter of the Gentiles. Genesis 14:18 That
table pre-imaged this mystical table, just as that priest was a type and image of
Christ, the true high-priest. Leviticus xiv For you are a priest for ever after
the order of Melchisedek. Of this bread the show-bread was an image. This surely
is that pure and bloodless sacrifice which the Lord through the prophet said is
offered to Him from the rising to the setting of the sun Malachi 1:11 .

--- END CAPTURE ---
=================== SRC_PRIMARY_0787_Second-Council-of-Nicaea_Definition_Incense-and-Lights_NPNF2-14-Percival.txt
size 3371 B · lines 55 · sha256 2c724bf11abc5e14f4225424527acc7ed0658649f4fef105ae0ca92ae5fbdb86
repo copy: 
CAPTURE — 260835-70
SOURCE: The Second Council of Nicaea (787), The Decree / Definition of the
        Holy Great and Ecumenical Synod, the Second of Nice.
        English: Henry R. Percival, ed., Nicene and Post-Nicene Fathers,
        Second Series, Vol. 14, "The Seven Ecumenical Councils" (1900).
        PUBLIC DOMAIN.
PROVENANCE: newadvent.org/fathers/3819.htm, read in-page 2026-09-08.
            Page innerText length 121,915 chars. "incense" occurs exactly
            TWICE on the page, at char 22,364 and char 69,111. Both captured.

--- BEGIN CAPTURE 1 (char 22,364) — from the epistle/profession material,
    the imperial-portrait analogy ---

For if the people go forth with lights and incense to meet the laurata and images
of the Emperors when they are sent to cities or rural districts, they honour
surely not the tablet covered over with wax, but the Emperor himself.

--- END CAPTURE 1 ---

--- BEGIN CAPTURE 2 (char 69,111) — THE DEFINITION ITSELF, the load-bearing text ---
=================== SRC_PRIMARY_1899_Sokolof_Manual-Orthodox-Church-Divine-Services_Incense-And-Censer.txt
size 2831 B · lines 46 · sha256 a5e52c7b94577aa8bf4798e74f863ff48f9d1cdff5e0d1618cf00fbe4dec0068
repo copy: 
CAPTURE — 260835-70
SOURCE: Arch-Priest D. Sokolof, A Manual of the Orthodox Church's Divine
        Services. Translated from the Russian. New York and Albany:
        Wynkoop Hallenbeck Crawford Co., Printers, 1899. PUBLIC DOMAIN.
        (Title page read directly from the OCR text.)
PROVENANCE: archive.org item `amanualoftheorth00sokouoft`,
            file `amanualoftheorth00sokouoft_djvu.txt`, retrieved 2026-09-08.
            Normalised length 403,627 chars; /censing|censer|incense/i returns
            36 hits. The doctrinal explanation is the section headed "Incense."
            (Marginal "22" is the printed page number in the captured span.)
WHY THIS SOURCE: it is the only ORTHODOX explanation of the censing that this
            pass could obtain in a public-domain English text. The standard
            modern Orthodox liturgical commentaries were located but are
            access-restricted — see the UNMATCHED register in the analysis file.

--- BEGIN CAPTURE ---

Incense. — Besides the lampads, candlesticks and candelabra, with their burning
candles and lamps, an important item of divine service is the burning and
swinging of incense (a fragrant tree-gum). This swinging is performed sometimes
=================== SRC_PRIMARY_2004_Theodore-of-Mopsuestia_Commentary-Twelve-Prophets_Malachi-1-11_FOTC108-Hill.txt
size 3873 B · lines 63 · sha256 21dfb2206151d06e01515179156ac0ee7b8c04226f69491eb93581546cb93ccf
repo copy: 
CAPTURE — 260835-70
SOURCE: Theodore of Mopsuestia, Commentary on the Twelve Prophets.
        The Fathers of the Church: A New Translation, VOLUME 108.
        Translated by Robert C. Hill. Catholic University of America Press.
        Copyright © 2004. ISBN 0-8132-0108-X (pbk.).
        All four data points read directly out of the volume's own front matter.
COPYRIGHT: © modern translation. NOT public domain. Internal verification only.
PROVENANCE: archive.org item `theodore-of-mopsuestia-commentary-on-the-twelve-prophets`,
            file `Theodore of Mopsuestia - Commentary on the Twelve Prophets_djvu.txt`,
            retrieved 2026-09-08 by in-page fetch from the archive.org origin.
            Raw length 1,044,226 chars.
            ⚠️ HYPHEN-SPLIT PRECAUTION APPLIED (per the 260835-66 finding): the
            text was normalised with /-\s*\n\s*/ removed before searching, and
            "incense" was searched as /in\s*-?\s*cense/i. On the normalised text
            (1,035,201 chars) the term returns exactly THREE hits in the whole
            volume: 213,550 / 249,662 / 976,219. Only the third is in Malachi.
            Running headers in the captured span: "404 THEODORE OF MOPSUESTIA"
            and "COMMENTARY ON MALACHI 2 405". Bracketed [608] is the edition's
            marginal column reference.
CAVEAT: OCR of a scan. Re-verify against print before outward quotation.
=================== SRC_PRIMARY_2008_Orthodox-Study-Bible_Notes-Mal-1-11_Ps-140-141_Sirach-39-14_Lev-2_Num-17.txt
size 5013 B · lines 89 · sha256 9439baf5431e85cac03db539019385fae09512f4b5fce63cedf8f15f6c4e3fe9
repo copy: 
CAPTURE — 260835-70
SOURCE: The Orthodox Study Bible (St. Athanasius Academy of Orthodox Theology /
        Thomas Nelson; OT from the Septuagint). Study notes, not the biblical text.
COPYRIGHT: © modern study apparatus. NOT public domain. Internal verification only.
PROVENANCE AND VERIFICATION — read this before quoting anything below:
  Two INDEPENDENT archive.org scans of the edition were OCR'd separately and
  both were searched:
    [A] item `the-orthodox-study-bible_202509`,
        file `The Orthodox Study Bible_djvu.txt` (normalised len 7,682,575)
    [B] item `the-orthodox-study-bible-2021-medium-quality-scan`,
        file `The Orthodox Study Bible 2021 [Medium Quality Scan]_djvu.txt`
  Both retrieved 2026-09-08. Hyphen-split normalisation applied before searching
  (per 260835-66). "incense" returns 224 hits across [A].
  The Malachi 1:11 note was located in BOTH and the two readings were diffed.
  They agree, except that [A]'s OCR corrupts two words that [B] renders cleanly:
        [A] "in every place OF church"   [B] "in every place or church"
        [A] "nearly evel service"        [B] "nearly every service"
  A third witness was obtained: page image leaf 1081 (= printed p. 1054) of [A],
  fetched via the BookReader image endpoint and read on screen. It is legible at
  the note and agrees with [B].
=================== SRC_PRIMARY_2012_Cyril-of-Alexandria_Commentary-Twelve-Prophets-vol3_Malachi-1-11_FOTC124-Hill.txt
size 4217 B · lines 70 · sha256 923832c4736576c4d13d569ca650b376cdeca31eb144818eade1fea8116f0c25
repo copy: 
CAPTURE — 260835-70
SOURCE: St Cyril of Alexandria, Commentary on the Twelve Prophets, Volume 3.
        The Fathers of the Church: A New Translation, VOLUME 124.
        Translated by Robert C. Hill. Catholic University of America Press.
        Title page verified by direct read of the OCR text (see PROVENANCE):
        "ST. CYRIL OF ALEXANDRIA / COMMENTARY ON THE TWELVE PROPHETS,
        VOLUME 3 ... Translated by Robert C. Hill ... THE FATHERS OF THE
        CHURCH A NEW TRANSLATION VOLUME 124". ISBN 978-0-8132-0115-3.
        ⚠️ The year 2012 in this filename is PROVISIONAL — it is the earliest
        20xx date in the front matter, not a verified copyright line. No
        "Copyright ©" string was recoverable from the OCR. Confirm before use.
COPYRIGHT: © modern translation. NOT public domain. Captured here for internal
           verification only. ⛔ Do NOT deploy verbatim outward without a
           rights check or substitution of a public-domain rendering.
PROVENANCE: archive.org item `cyril-of-alexandria-a-commentary-on-the-twelve-prophets`,
            file `cyril of alexandria - a commentary on the twelve prophets 3_djvu.txt`,
            retrieved 2026-09-08 by in-page fetch from the archive.org origin.
            Text length 804,092 chars. "MALACHI" first occurs at char 632,913;
            the lemma "rising of the sun" occurs EXACTLY ONCE in the volume,
            at char 666,873. Running page headers in the captured span read
=================== SRC_SECONDARY_2026_Orthodox-Popular-Apologetics_Incense-Warrant_Peck-OrthodoxAnswers-StMichael.txt
size 5617 B · lines 99 · sha256 2c00ad7a462a0697d9c2714907f41fffe38278f3816a2469af3da8272eeb3a32
repo copy: 
CAPTURE — 260835-70
⛔⛔ ALL THREE SOURCES BELOW ARE **SECONDARY**. They are parish pages and a
    priest's blog. They establish WHAT IS COMMONLY SAID in Orthodox popular
    apologetics. They are NOT authority, they bind nobody, and no verdict in
    the analysis document rests on them alone.
    All three were retrieved 2026-09-08 and read in-page (each is
    client-rendered; a plain fetch returns an empty shell).
    They are three of the five URLs already listed, UNVERIFIED, in
    `Protestant_Commentary_Survey_Malachi_1_11.md` Appendix §A6.

================================================================
1. Fr. John Peck, "Worship With Incense" — https://frjohnpeck.com/worship-with-incense/
   (Orthodox priest, personal site. Page innerText 7,110 chars.)
================================================================

[the scriptural list he gives]
Exodus 25,30,31,35,37,39,40 / Leviticus 4,16 / Numbers 4,7,16 / Deuteronomy 33 /
1 Samuel (1 Kingdoms/Reigns LXX) 2 / 1 Chronicles 6,9,23 / 2 Chronicles 2,13,26,29 /
Psalm 141 / Isaiah 60 / Jeremiah 17,41 / Malachi 1 / Luke 1 / Revelation 5,8

```

Dispositions: Orthodox_Malachi_1_11_And_Incense_Warrant.md → repo root + §4 row; SRC_PRIMARY_2012_Cyril-… → NOT ADDED (wholly contained in the 0430 file; superseded); the other six → src/ + SRC_Manifest.md rows.

## Appendix D — Cyril: diff -u of the overlapping text (0430 pp. 298-299 region vs staging-70 capture body), raw and reflowed

```diff
### diff -u (raw lines): 0430 printed pp. 298-299 region (lines 127-196) vs staging-70 capture body
--- cyril_0430_pp298-299_region.txt	2026-10-09 21:46:15.221719374 +0000
+++ cyril_staging70_capture_body.txt	2026-10-09 21:46:15.224202631 +0000
@@ -1,70 +1,33 @@
-Hence, from the rising of the sun to its setting, my name has been glo- 
-rified among the nations, and in every place incense is offered to my 
-name and a pure offering; because my name is great among the nations, 
-says the Lord almighty (v.11). He now clearly repudiates the offer- 
-
-
-30. Heb 12.16. 
-
-
-298 CYRIL OF ALEXANDRIA 
-
-
-ing of sacrifice according to the Law, and, as it were, abandons 
-his love for Jews, and regards the priesthood as unacceptable 
-and the shadow as inadmissible—animal sacrifice and incense, 
-I mean—this not being his original intention. He makes this 
-clear also in other prophets, as when he says in the statement 
-of Isaiah, “I am fed up with burnt offerings of rams; fat of sheep 
-and blood of bulls and goats I do not want, not even if you come 
-to appear before me. After all, who asked this from your hands? 
-Do not continue trampling on my court. (565) If you bring the 
-best of flour, it is a waste of time; incense is an abomination 
-to me.” And in Jeremiah, “Assemble your burnt offerings along 
-with your sacrifices and eat the meat, because I did not speak 
-to your fathers about burnt offerings and sacrifices on the day 
-I brought them up out of the land of Egypt.”*! The Law, you 
-see, was a prefiguring and foretelling of worship in spirit and 
-in truth, and “regulations for the body,” as the divinely inspired 
-Paul writes, *until the time comes to set things right." Now, the 
-time for reform would, in my view, be no other than the coming 
-of our Savior. The first covenant, on account of its not being 
-faultless, is said to have disappeared, being obsolete; a place was 
-sought for a new and second one, which would be proof against 
-any blame or fault. This, in fact, is said by the Son himself, who 
-bears the name also of Angel of Great Counsel—hence his say- 
-ing, “I do not speak of myself: the Father who sent me is the one 
-who gave me instructions as to what to speak and what to say.”*” 
-
-Accordingly, he clearly told those exercising priesthood ac- 
-cording to the Law that they are unacceptable to him or, rather, 
-I have no pleasure in them as they perform sacrifices in shadow and 
-type, and that he would not accept what was offered by them. He 
-predicts that his name will be great and famous among people ev- 
-erywhere throughout the earth under heaven, and that in every 
-place and nation pure and bloodless sacrifices will be offered to 
-his name, now that the ministers no longer diminish his honor 
-or pay him spiritual worship in indifferent fashion. Instead, with 
-enthusiasm, simplicity, and holiness they will be zealous in of 
-fering the pleasing odor of the spiritual incense—(566) namely, 
-
-
-31. Is 1.11—19; Jer 7.21. 
-32. Heb 9.10; Jn 4.23; Heb 8.7, 13; Is 9.6; Jn 12.49. 
-
-
-COMMENTARY ON MALACHI 1 299 
-
-
-faith, hope, love, and the ornaments of good works. This is obvi- 
-ously when Christ’s heavenly and life-giving sacrifice is institut- 
-ed, through which death is destroyed, and this corruptible flesh 
-from the earth puts on incorruptibility.? 
-
-You by contrast profane it in saying, The table of the Lord. is spoiled, 
-and the food on it is of no value (v.12). In this he also makes clear 
-to us that those called from the nations will be better and more 
-honest than those from Israel; their sacrifices will be pure, their 
-incense fragrant, and his name will be great from east to west, 
-whereas among you (he says) the altar is not held in the high 
-regard that befits God.
+
+[LEMMA, v.11]
+Hence, from the rising of the sun to its setting, my name has been glorified
+among the nations, and in every place incense is offered to my name and a pure
+offering; because my name is great among the nations, says the Lord almighty
+(v.11).
+
+[COMMENT — opening]
+He now clearly repudiates the offering of sacrifice according to the Law, and,
+as it were, abandons his love for Jews, and regards the priesthood as
+unacceptable and the shadow as inadmissible—animal sacrifice and incense, I
+mean—this not being his original intention.
+
+[COMMENT — Isaiah/Jeremiah proof texts abridged here; Cyril cites Is 1.11-19 and
+Jer 7.21, including Isaiah's "incense is an abomination to me."]
+
+[COMMENT — the positive prediction]
+He predicts that his name will be great and famous among people everywhere
+throughout the earth under heaven, and that in every place and nation pure and
+bloodless sacrifices will be offered to his name, now that the ministers no
+longer diminish his honor or pay him spiritual worship in indifferent fashion.
+Instead, with enthusiasm, simplicity, and holiness they will be zealous in
+offering the pleasing odor of the spiritual incense—(566) namely, faith, hope,
+love, and the ornaments of good works. This is obviously when Christ's heavenly
+and life-giving sacrifice is instituted, through which death is destroyed, and
+this corruptible flesh from the earth puts on incorruptibility.
+
+[COMMENT — at v.12]
+In this he also makes clear to us that those called from the nations will be
+better and more honest than those from Israel; their sacrifices will be pure,
+their incense fragrant, and his name will be great from east to west, whereas
+among you (he says) the altar is not held in the high regard that befits God.
+

### diff -u (reflowed: hyphen line-splits joined, whitespace collapsed, one sentence per line)
--- cyril_0430_reflowed.txt	2026-10-09 21:46:15.226539053 +0000
+++ cyril_staging70_reflowed.txt	2026-10-09 21:46:15.228442891 +0000
@@ -1,22 +1,11 @@
+[LEMMA, v.11]
 Hence, from the rising of the sun to its setting, my name has been glorified among the nations, and in every place incense is offered to my name and a pure offering; because my name is great among the nations, says the Lord almighty (v.11).
-He now clearly repudiates the offer30.
-Heb 12.16. 298 CYRIL OF ALEXANDRIA ing of sacrifice according to the Law, and, as it were, abandons his love for Jews, and regards the priesthood as unacceptable and the shadow as inadmissible—animal sacrifice and incense, I mean—this not being his original intention.
-He makes this clear also in other prophets, as when he says in the statement of Isaiah, “I am fed up with burnt offerings of rams; fat of sheep and blood of bulls and goats I do not want, not even if you come to appear before me.
-After all, who asked this from your hands?
-Do not continue trampling on my court.
-(565)
-If you bring the best of flour, it is a waste of time; incense is an abomination to me.”
-And in Jeremiah, “Assemble your burnt offerings along with your sacrifices and eat the meat, because I did not speak to your fathers about burnt offerings and sacrifices on the day I brought them up out of the land of Egypt.”*!
-The Law, you see, was a prefiguring and foretelling of worship in spirit and in truth, and “regulations for the body,” as the divinely inspired Paul writes, *until the time comes to set things right."
-Now, the time for reform would, in my view, be no other than the coming of our Savior.
-The first covenant, on account of its not being faultless, is said to have disappeared, being obsolete; a place was sought for a new and second one, which would be proof against any blame or fault.
-This, in fact, is said by the Son himself, who bears the name also of Angel of Great Counsel—hence his saying, “I do not speak of myself: the Father who sent me is the one who gave me instructions as to what to speak and what to say.”*”
-Accordingly, he clearly told those exercising priesthood according to the Law that they are unacceptable to him or, rather, I have no pleasure in them as they perform sacrifices in shadow and type, and that he would not accept what was offered by them.
+[COMMENT — opening]
+He now clearly repudiates the offering of sacrifice according to the Law, and, as it were, abandons his love for Jews, and regards the priesthood as unacceptable and the shadow as inadmissible—animal sacrifice and incense, I mean—this not being his original intention.
+[COMMENT — Isaiah/Jeremiah proof texts abridged here; Cyril cites Is 1.11-19 and Jer 7.21, including Isaiah's "incense is an abomination to me."]
+[COMMENT — the positive prediction]
 He predicts that his name will be great and famous among people everywhere throughout the earth under heaven, and that in every place and nation pure and bloodless sacrifices will be offered to his name, now that the ministers no longer diminish his honor or pay him spiritual worship in indifferent fashion.
-Instead, with enthusiasm, simplicity, and holiness they will be zealous in of fering the pleasing odor of the spiritual incense—(566) namely, 31.
-Is 1.11—19; Jer 7.21. 32.
-Heb 9.10; Jn 4.23; Heb 8.7, 13; Is 9.6; Jn 12.49.
-COMMENTARY ON MALACHI 1 299 faith, hope, love, and the ornaments of good works.
-This is obviously when Christ’s heavenly and life-giving sacrifice is instituted, through which death is destroyed, and this corruptible flesh from the earth puts on incorruptibility.?
-You by contrast profane it in saying, The table of the Lord. is spoiled, and the food on it is of no value (v.12).
+Instead, with enthusiasm, simplicity, and holiness they will be zealous in offering the pleasing odor of the spiritual incense—(566) namely, faith, hope, love, and the ornaments of good works.
+This is obviously when Christ's heavenly and life-giving sacrifice is instituted, through which death is destroyed, and this corruptible flesh from the earth puts on incorruptibility.
+[COMMENT — at v.12]
 In this he also makes clear to us that those called from the nations will be better and more honest than those from Israel; their sacrifices will be pure, their incense fragrant, and his name will be great from east to west, whereas among you (he says) the altar is not held in the high regard that befits God.
```

## Appendix E — every anchor used (file · mode · first 160 chars of anchor), in order of application

```
SRC_Manifest.md	after	'Confirmed on the first post before any reading, per the `CLAUDE.md` rule added this pass. |\n'
SRC_Manifest.md	after	"> ⭐ **DATED NOTE, 260835-72 (2026-10-09):** the `DQ-Thread-Followup` row above is superseded as to citability — `DQ-29`…`DQ-37` are minted from the raw on JD's "
SRC_Manifest.md	replace	'89,131 bytes, 787 lines.**'
PROJECT_STATE.md	after	'| `src/SRC_Discord_Assurance-raw.txt` | 260833-6 | ⭐ **NEW, REGISTERED 260833-6.** Byte-exact raw capture artifact (`CAPTURED 2026-08-24, 7:28 PM ET`) supportin'
SRC_Manifest.md	before	'\n---\n\n# Dual-Capture Reconciliation Procedure (added 260725-4'
SRC_Manifest.md	before	'\n---\n\n# Dual-Capture Reconciliation Procedure (added 260725-4'
PROJECT_STATE.md	after	"| `Incense_Reply_Source_Checks.md` | 260835-65 | ⭐⭐ **Backstage — EXTERNAL RESEARCH, CREATED `260835-57`, REGISTERED `260835-65` ON JD'S RULING: same class and "
PROJECT_STATE.md	after	'> ⏳⏳ **GATE FINDING 3 — REPORTED, NOT FIXED, AND OUTSIDE THIS BRIEF.** A diff of tracked files against the §4 table found **`Ceremonial_Meaning_Source_Checks.md'
Incense_Conversational_Outline.md	after	'`[C11]` will report 11 `DQ` findings unreviewed; that is accurate.\n'
Incense_Conversational_Outline.md	before	'\n---\n \n## The full outline'
Incense_Conversational_Outline.md	replace	'Starting from this claim is stronger than opening with a denial of something they may not have said. If their own case establishes incense as an act of worship '
Incense_Conversational_Outline.md	replace	'**An illustrative parallel: circumcision.** Faith existed before Christ, and faith continues; yet circumcision ceased. It ceased because it did not signify fait'
Incense_Conversational_Outline.md	replace	'**Update (260833-1) — a third register datum, and it carries the hard form.** In the Discord dialogue itself, asked what governs drawing OT material into worshi'
Incense_Conversational_Outline.md	replace	'English church worship was plain and essentially incense-free from the Edwardian Reformation (late 1540s) until the ritualist revival of the 1850s onward, a dev'
Incense_Conversational_Outline.md	replace	'CHECKED-AGAINST: DQ-26 @ 260835-31 · IP-108 @ 260835-32 · RV-63 @ 260830-1\n'
Incense_Conversational_Outline.md	replace	'⛔ So "discussed, therefore strong" no longer holds as stated.'
Incense_Conversational_Outline.md	after	'⛔ Not moved for `DQ-38` onward, which do not exist yet. See the `IP` block below for that arm.\n'
Incense_Conversational_Outline.md	before	'\n> ⚠️⚠️ **DATED NOTE, 260835-74 (2026-10-09) — TWO CLAUSES OF THE SPOKEN CORE ARE NOW ANSWERABLE'
Incense_Conversational_Outline.md	replace	'1. **Wrong vocabulary for a new institution.** The verse uses the technical Levitical cult terms of its hearers: muqtar (that which is burned), muggash (offered'
Incense_Conversational_Outline.md	replace	'> **Old Covenant symbols attached to the Levitical priesthood cease unless Christ or the apostles positively reinstitute them under the New Covenant.**\n'
Incense_Conversational_Outline.md	replace	"4. Then what is being offered, or symbolized, when incense is burned in a New Testament service? If it symbolizes the congregation's prayers, those prayers are "
Incense_Conversational_Outline.md	replace	'CHECKED-AGAINST: DQ-37 @ 260835-74 · IP-108 @ 260835-32 · RV-63 @ 260830-1\n'
St_Francis_EMC_Distinctives.md	before	'\n## 16. Ante-Nicene/Nicene Fathers Class'
Incense_Outline_Memory_Card.md	replace	'**Last updated: 260835-73** (date-stamped, format yymmdd-iteration)'
Incense_Outline_Memory_Card.md	replace	"Once the outline's stamp moves past `260835-72`, treat the card as stale until it is re-derived.\n"
Incense_Outline_Memory_Card.md	replace	'## Changelog\n\n- **260835-73 (2026-10-09):**'
Incense_Outline_Memory_Card.md	replace	'\n## Standing guards (these travel with every layer)'
St_Francis_EMC_Distinctives.md	replace	'**Last updated: 260835-72** (date-stamped, format yymmdd-iteration) '
St_Francis_EMC_Distinctives.md	after	'## Changelog\n\n'
PROJECT_STATE.md	replace	'| `St_Francis_EMC_Distinctives.md` | 260835-72 | '
Incense_Conversational_Outline.md	replace	'**Last updated: 260835-72** (date-stamped, format yymmdd-iteration) '
Incense_Conversational_Outline.md	after	'## Changelog\n\n'
PROJECT_STATE.md	replace	'| `Incense_Conversational_Outline.md` | 260835-72 | '
SRC_Manifest.md	replace	'**Last updated: 260835-72** (date-stamped, format yymmdd-iteration) '
SRC_Manifest.md	replace	'\n\n> ⛔⛔⛔ **DATED NOTE, 260835-4 — `File 45` AND `File 46` ARE NOT UNMINED'
PROJECT_STATE.md	replace	'| `SRC_Manifest.md` | 260835-72 | '
PROJECT_STATE.md	replace	'| `Incense_Outline_Memory_Card.md` | 260835-73 | '
PROJECT_STATE.md	replace	'**Last updated: 260835-73** (created 260724-3). Read this file first, before any other project document.\n'
PROJECT_STATE.md	replace	'| `PROJECT_STATE.md` | 260835-73 | '
```

## Appendix F — Followup archive: message-break determinations and message table

```
Message breaks inferred inside client header blocks (raw byte position of the separating newline), and joins kept inside one message:

H 3 Athanasi 9/5/26, 3:10 PM          BREAK @5,859: …'roposing a ban on it, but never actually did.' | 'I see two arguments being made: '
H 5 Athanasi 9/5/26, 6:50 PM          BREAK @7,684: …'eny that is to deny the Witness of Scripture.' | 'This is also an interesting set of paragraphs'
H 5 Athanasi 9/5/26, 6:50 PM          BREAK @9,189: …'(continued)' | 'Secondly, the Liturgical use of incense was s'
H 5 Athanasi 9/5/26, 6:50 PM          BREAK @10,585: …'(continued)' | 'And, thirdly and lastly, they had the less he'
H 6 JD Smith 9/8/26, 9:18 AM          KEPT  @11,271: …'@Athanasius325 / Fr James ' | 'Thanks for this, and I hope you had a nice lo'
H 6 JD Smith 9/8/26, 9:18 AM          BREAK @12,871: …' three reasons, and the ruling they produced.' | 'If the question is broader than England, the '
H 7 JD Smith 9/8/26, 9:26 AM          BREAK @15,382: …'incense, and vestments," then "we will obey."' | 'On Canon 20, which you mentioned as having ju'
H 7 JD Smith 9/8/26, 9:26 AM          BREAK @15,750: …'nd no canon on ritual has been enacted since.' | "Malachi 1:11 doesn't supply the warrant to bu"
H 8 JD Smith 9/8/26, 9:35 AM          BREAK @19,006: …"ulated incense.) Those aren't the same thing." | "I would also say that I'm going further than "
H13 Athanasi 9/12/26, 2:14 AM         KEPT  @25,907: …'1) Scripture: Yes (my position)' | '2) Tradition: Yes (the vast majority of Churc'
H13 Athanasi 9/12/26, 2:14 AM         KEPT  @25,987: …'ty of Church history has allowed for its use)' | '3) The established customs laid out by the ga'
H13 Athanasi 9/12/26, 2:14 AM         KEPT  @26,145: …'urisdiction (the Episcopal Missionary Church)' | '4) The Bishop Ordinary: Yes (Bishop Millsaps,'
H13 Athanasi 9/12/26, 2:14 AM         KEPT  @26,257: …' use incense, is fine with us using incense.)' | '5) The Rector: Yes (I am the Rector.) '
H14 JD Smith 9/17/26, 8:28 PM         BREAK @28,481: …"ither. It just doesn't permit it in worship. " | 'So, on the Regulative principle - I think it’'
H14 JD Smith 9/17/26, 8:28 PM         BREAK @29,821: …"at verse in the same passage I'll cite below." | "That's what the Reformed confessions codify. "
H14 JD Smith 9/17/26, 8:28 PM         BREAK @31,705: …'an, and both predate Westminster by 80 years.' | 'Calvin put it in 1544 as "the rule which dist'
H14 JD Smith 9/17/26, 8:28 PM         KEPT  @32,328: …'(1)' | 'Express command. "Preach the word" (2 Tim 4:2'
H14 JD Smith 9/17/26, 8:28 PM         KEPT  @32,382: …'(2) ' | "Approved example. Where Scripture doesn't com"
H14 JD Smith 9/17/26, 8:28 PM         KEPT  @32,988: …'(3) ' | 'Good and necessary consequence. Infant baptis'
H14 JD Smith 9/17/26, 8:28 PM         BREAK @33,645: …'ise is commanded, and a hymn is a form of it.' | 'I mention it because you opened the other thr'
H14 JD Smith 9/17/26, 8:28 PM         BREAK @35,571: …'ent is still the same act, only less audible.' | 'A “form” of worship is a way of performing th'
H14 JD Smith 9/17/26, 8:28 PM         BREAK @37,573: …'here God asked for it under the new covenant.' | 'One last thing on the principle itself.'
H14 JD Smith 9/17/26, 8:28 PM         BREAK @39,266: …'lone — a principle reaching a particular act.' | 'And when I asked what made Revelation 5:8 ins'
H14 JD Smith 9/17/26, 8:28 PM         BREAK @41,136: …'More on your examples in a following post. ' | '——————'
H14 JD Smith 9/17/26, 8:28 PM         KEPT  @41,281: …'It distinguishes between:' | '-Acts of worship (like prayer)'
H14 JD Smith 9/17/26, 8:28 PM         KEPT  @41,312: …'-Acts of worship (like prayer)' | '-Circumstances necessary to perform those act'
H14 JD Smith 9/17/26, 8:28 PM         KEPT  @41,415: …' (like time of day when the prayer is prayed)' | '-Things indifferent (not necessary to perform'
H16 JD Smith 9/27/26, 5:32 AM         BREAK @44,811: …", and that's what the last post aimed to do. " | "You've asked me instead to show a prohibition"
H16 JD Smith 9/27/26, 5:32 AM         BREAK @45,965: …'ns to use incense in the context of worship."' | 'To be fair to the normative principle, it isn'
H17 JD Smith 9/27/26, 5:41 AM         BREAK @48,582: …', and dare to intermingle their own with it?"' | 'He then raises the obvious objection against '
H17 JD Smith 9/27/26, 5:41 AM         BREAK @49,822: …" That's where these next messages are going. " | 'Here are the examples, as promised.'
H17 JD Smith 9/27/26, 5:41 AM         BREAK @51,511: …'s out of bounds when I make it about incense.' | 'Hanukkah'
H17 JD Smith 9/27/26, 5:41 AM         BREAK @52,802: …'us commemoration of something that had ended.' | "It's worth noting that the same objection aro"
H17 JD Smith 9/27/26, 5:41 AM         BREAK @53,732: …'0 says the restricted access has now changed.' | 'Each of those answers came down to the same d'
H18 JD Smith 9/27/26, 5:49 AM         BREAK @55,998: …"nd you've defended it as a Godward offering. " | 'Take the first. If incense is optional altoge'
H18 JD Smith 9/27/26, 5:49 AM         BREAK @57,252: …' comparison you drew with reading Scripture. ' | "And Malachi can't do the work of the second o"
H19 JD Smith 9/27/26, 6:09 AM         BREAK @59,577: …'t see how both can be held at the same time. ' | '-----'
H19 JD Smith 9/27/26, 6:09 AM         KEPT  @59,583: …'-----' | 'Again, take your time, and I hope you have a '
H24 JD Smith 10/4/26, 6:35 PM         BREAK @65,632: …'y offered fire "which he commanded them not."' | 'Jeremiah 7:31 does the same thing more plainl'
H24 JD Smith 10/4/26, 6:35 PM         BREAK @67,109: …"something I've added; it comes from the text." | 'The application to incense is on 9/8 and 9/27'
H26 JD Smith Yesterday at 1:28 PM     BREAK @71,152: …'ry consequence (the three tests of the RPW.) ' | '--'
H26 JD Smith Yesterday at 1:28 PM     KEPT  @71,155: …'--' | 'Malachi 1:11'
H26 JD Smith Yesterday at 1:28 PM     BREAK @73,146: …'but "in spirit and in truth" (John 4:21-23). ' | '--'
H26 JD Smith Yesterday at 1:28 PM     KEPT  @73,149: …'--' | 'Revelation 8:3-5'
H26 JD Smith Yesterday at 1:28 PM     BREAK @74,873: …'church offering it, or telling the church to.' | '--'
H26 JD Smith Yesterday at 1:28 PM     KEPT  @74,876: …'--' | "I also don't see that it's a necessary conseq"
H27 Athanasi Yesterday at 2:18 PM     KEPT  @76,957: …'nt of the Old Covenant worship, or is it not?' | 'The reason I ask is if New Covenant worship i'
H28 JD Smith 3:08 PM                  BREAK @79,584: …'reason, not because fulfillment spared them. ' | "That's the step I don't see supported. A rite"

Message table: n · header · part/parts · speaker · header time · raw [start, end)
 1 · H1 · 1/1 · JD Smith (OP) · 9/5/26, 9:55 AM · [54, 2,014)
 2 · H2 · 1/1 · Athanasius325 / Fr James · 9/5/26, 3:01 PM · [2,062, 4,058)
 3 · H3 · 1/2 · Athanasius325 / Fr James · 9/5/26, 3:10 PM · [4,106, 5,859)
 4 · H3 · 2/2 · Athanasius325 / Fr James · 9/5/26, 3:10 PM · [5,860, 6,218)
 5 · H4 · 1/1 · Athanasius325 / Fr James · 9/5/26, 6:34 PM · [6,266, 6,421)
 6 · H5 · 1/4 · Athanasius325 / Fr James · 9/5/26, 6:50 PM · [6,469, 7,684)
 7 · H5 · 2/4 · Athanasius325 / Fr James · 9/5/26, 6:50 PM · [7,685, 9,189)
 8 · H5 · 3/4 · Athanasius325 / Fr James · 9/5/26, 6:50 PM · [9,190, 10,585)
 9 · H5 · 4/4 · Athanasius325 / Fr James · 9/5/26, 6:50 PM · [10,586, 11,209)
10 · H6 · 1/2 · JD Smith (OP) · 9/8/26, 9:18 AM · [11,245, 12,871)
11 · H6 · 2/2 · JD Smith (OP) · 9/8/26, 9:18 AM · [12,872, 13,512)
12 · H7 · 1/3 · JD Smith (OP) · 9/8/26, 9:26 AM · [13,548, 15,382)
13 · H7 · 2/3 · JD Smith (OP) · 9/8/26, 9:26 AM · [15,383, 15,750)
14 · H7 · 3/3 · JD Smith (OP) · 9/8/26, 9:26 AM · [15,751, 17,054)
15 · H8 · 1/2 · JD Smith (OP) · 9/8/26, 9:35 AM · [17,090, 19,006)
16 · H8 · 2/2 · JD Smith (OP) · 9/8/26, 9:35 AM · [19,007, 19,413)
17 · H9 · 1/1 · JD Smith (OP) · 9/8/26, 9:44 AM · [19,449, 20,315)
18 · H10 · 1/1 · Athanasius325 / Fr James · 9/11/26, 6:51 PM · [20,364, 22,339)
19 · H11 · 1/1 · Athanasius325 / Fr James · 9/11/26, 9:50 PM · [22,388, 24,109)
20 · H12 · 1/1 · Athanasius325 / Fr James · 9/11/26, 10:13 PM · [24,159, 25,369)
21 · H13 · 1/1 · Athanasius325 / Fr James · 9/12/26, 2:14 AM · [25,418, 26,549)
22 · H14 · 1/9 · JD Smith (OP) · 9/17/26, 8:28 PM · [26,586, 28,481)
23 · H14 · 2/9 · JD Smith (OP) · 9/17/26, 8:28 PM · [28,482, 29,821)
24 · H14 · 3/9 · JD Smith (OP) · 9/17/26, 8:28 PM · [29,822, 31,705)
25 · H14 · 4/9 · JD Smith (OP) · 9/17/26, 8:28 PM · [31,706, 33,645)
26 · H14 · 5/9 · JD Smith (OP) · 9/17/26, 8:28 PM · [33,646, 35,571)
27 · H14 · 6/9 · JD Smith (OP) · 9/17/26, 8:28 PM · [35,572, 37,573)
28 · H14 · 7/9 · JD Smith (OP) · 9/17/26, 8:28 PM · [37,574, 39,266)
29 · H14 · 8/9 · JD Smith (OP) · 9/17/26, 8:28 PM · [39,267, 41,136)
30 · H14 · 9/9 · JD Smith (OP) · 9/17/26, 8:28 PM · [41,137, 41,689)
31 · H15 · 1/1 · Athanasius325 / Fr James · 9/18/26, 2:23 PM · [41,738, 43,080)
32 · H16 · 1/3 · JD Smith (OP) · 9/27/26, 5:32 AM · [43,117, 44,811)
33 · H16 · 2/3 · JD Smith (OP) · 9/27/26, 5:32 AM · [44,812, 45,965)
34 · H16 · 3/3 · JD Smith (OP) · 9/27/26, 5:32 AM · [45,966, 47,486)
35 · H17 · 1/6 · JD Smith (OP) · 9/27/26, 5:41 AM · [47,523, 48,582)
36 · H17 · 2/6 · JD Smith (OP) · 9/27/26, 5:41 AM · [48,583, 49,822)
37 · H17 · 3/6 · JD Smith (OP) · 9/27/26, 5:41 AM · [49,823, 51,511)
38 · H17 · 4/6 · JD Smith (OP) · 9/27/26, 5:41 AM · [51,512, 52,802)
39 · H17 · 5/6 · JD Smith (OP) · 9/27/26, 5:41 AM · [52,803, 53,732)
40 · H17 · 6/6 · JD Smith (OP) · 9/27/26, 5:41 AM · [53,733, 55,199)
41 · H18 · 1/3 · JD Smith (OP) · 9/27/26, 5:49 AM · [55,236, 55,998)
42 · H18 · 2/3 · JD Smith (OP) · 9/27/26, 5:49 AM · [55,999, 57,252)
43 · H18 · 3/3 · JD Smith (OP) · 9/27/26, 5:49 AM · [57,253, 58,748)
44 · H19 · 1/2 · JD Smith (OP) · 9/27/26, 6:09 AM · [58,785, 59,577)
45 · H19 · 2/2 · JD Smith (OP) · 9/27/26, 6:09 AM · [59,578, 59,662)
46 · H20 · 1/1 · Athanasius325 / Fr James · 9/28/26, 5:20 PM · [59,711, 61,599)
47 · H21 · 1/1 · Athanasius325 / Fr James · 9/28/26, 5:32 PM · [61,648, 62,380)
48 · H22 · 1/1 · JD Smith (OP) · 9/28/26, 7:41 PM · [62,417, 62,874)
49 · H23 · 1/1 · Athanasius325 / Fr James · 10/4/26, 12:42 AM · [62,924, 63,676)
50 · H24 · 1/3 · JD Smith (OP) · 10/4/26, 6:35 PM · [63,713, 65,632)
51 · H24 · 2/3 · JD Smith (OP) · 10/4/26, 6:35 PM · [65,633, 67,109)
52 · H24 · 3/3 · JD Smith (OP) · 10/4/26, 6:35 PM · [67,110, 68,552)
53 · H25 · 1/1 · Athanasius325 / Fr James · 10/7/26, 1:43 PM · [68,601, 69,425)
54 · H26 · 1/4 · JD Smith (OP) · Yesterday at 1:28 PM · [69,466, 71,152)
55 · H26 · 2/4 · JD Smith (OP) · Yesterday at 1:28 PM · [71,153, 73,146)
56 · H26 · 3/4 · JD Smith (OP) · Yesterday at 1:28 PM · [73,147, 74,873)
57 · H26 · 4/4 · JD Smith (OP) · Yesterday at 1:28 PM · [74,874, 76,802)
58 · H27 · 1/1 · Athanasius325 / Fr James · Yesterday at 2:18 PM · [76,855, 78,243)
59 · H28 · 1/2 · JD Smith (OP) · 3:08 PM · [78,271, 79,584)
60 · H28 · 2/2 · JD Smith (OP) · 3:08 PM · [79,585, 81,358)
61 · H29 · 1/1 · JD Smith (OP) · 3:23 PM · [81,386, 83,223)
62 · H30 · 1/1 · Athanasius325 / Fr James · 4:49 PM · [83,263, 85,215)
63 · H31 · 1/1 · Athanasius325 / Fr James · 5:08 PM · [85,255, 87,238)
64 · H32 · 1/1 · Athanasius325 / Fr James · 5:24 PM · [87,278, 89,131)
```

## Appendix G — DQ-29…DQ-37 byte ranges (raw, 48bb0a58… = 63920d32… for bytes < 82,964) mapped to archive messages

```
DQ-29:
   [byte @2,308–2,470] -> message 2 (Rev. James)
   [byte @2,686–2,757] -> message 2 (Rev. James)
   [byte @2,974–3,094] -> message 2 (Rev. James)
   [byte @4,007–4,057] -> message 2 (Rev. James)
   [byte @4,805–4,898] -> message 3 (Rev. James)
   [byte @5,125–5,153] -> message 3 (Rev. James)
   [byte @5,300–5,569] -> message 3 (Rev. James)
   [byte @5,788–5,859] -> message 3 (Rev. James)
   [byte @5,894–5,959] -> message 4 (Rev. James)
   [byte @5,962–6,064] -> message 4 (Rev. James)
   [byte @6,067–6,124] -> message 4 (Rev. James)
   [byte @6,127–6,217] -> message 4 (Rev. James)
   [byte @6,282–6,421] -> message 5 (Rev. James)
   [byte @7,515–7,684] -> message 6 (Rev. James)
DQ-30:
   [byte @22,521–22,656] -> message 19 (Rev. James)
   [byte @22,764–22,912] -> message 19 (Rev. James)
   [byte @22,943–23,043] -> message 19 (Rev. James)
   [byte @23,067–23,190] -> message 19 (Rev. James)
   [byte @23,192–23,268] -> message 19 (Rev. James)
   [byte @23,392–23,763] -> message 19 (Rev. James)
   [byte @23,766–24,018] -> message 19 (Rev. James)
DQ-31:
   [byte @24,378–24,501] -> message 20 (Rev. James)
   [byte @24,686–25,034] -> message 20 (Rev. James)
   [byte @25,224–25,369] -> message 20 (Rev. James)
DQ-32:
   [byte @21,494–21,696] -> message 18 (Rev. James)
   [byte @20,881–21,062] -> message 18 (Rev. James)
   [byte @21,961–22,055] -> message 18 (Rev. James)
   [byte @22,135–22,322] -> message 18 (Rev. James)
   [byte @25,876–25,907] -> message 21 (Rev. James)
   [byte @25,908–25,987] -> message 21 (Rev. James)
   [byte @25,988–26,145] -> message 21 (Rev. James)
   [byte @26,146–26,257] -> message 21 (Rev. James)
   [byte @26,258–26,295] -> message 21 (Rev. James)
   [byte @26,298–26,548] -> message 21 (Rev. James)
   [byte @25,536–25,650] -> message 21 (Rev. James)
DQ-33:
   [byte @41,819–41,915] -> message 31 (Rev. James)
   [byte @42,300–42,388] -> message 31 (Rev. James)
   [byte @42,389–42,502] -> message 31 (Rev. James)
   [byte @42,503–42,677] -> message 31 (Rev. James)
   [byte @42,680–42,931] -> message 31 (Rev. James)
   [byte @61,676–61,927] -> message 47 (Rev. James)
DQ-34:
   [byte @60,128–60,268] -> message 46 (Rev. James)
   [byte @60,291–60,413] -> message 46 (Rev. James)
   [byte @62,417–62,482] -> message 48 (JD)
   [byte @61,446–61,599] -> message 46 (Rev. James)
   [byte @60,638–60,901] -> message 46 (Rev. James)
   [byte @61,985–62,016] -> message 47 (Rev. James)
   [byte @62,211–62,292] -> message 47 (Rev. James)
   [byte @62,295–62,380] -> message 47 (Rev. James)
DQ-35:
   [byte @63,185–63,463] -> message 49 (Rev. James)
   [byte @63,466–63,676] -> message 49 (Rev. James)
   [byte @63,782–63,843] -> message 50 (JD)
DQ-36:
   [byte @68,601–68,712] -> message 53 (Rev. James)
   [byte @68,755–68,871] -> message 53 (Rev. James)
   [byte @68,941–69,062] -> message 53 (Rev. James)
   [byte @69,080–69,425] -> message 53 (Rev. James)
DQ-37:
   [byte @76,426–76,556] -> message 57 (JD)
   [byte @76,855–76,957] -> message 58 (Rev. James)
   [byte @76,978–77,227] -> message 58 (Rev. James)
   [byte @77,231–77,528] -> message 58 (Rev. James)
   [byte @77,530–77,659] -> message 58 (Rev. James)
   [byte @77,660–77,840] -> message 58 (Rev. James)
   [byte @77,841–78,048] -> message 58 (Rev. James)
   [byte @78,049–78,242] -> message 58 (Rev. James)
   [byte @82,666–82,824] -> message 61 (JD)
```

## Appendix H — git show --stat 0883e4f (Task 3)

```
commit 0883e4faadb06a32afbaf2111c6fa532c296d817
Author: JD Smith <jaydge@gmail.com>
Date:   Tue Sep 8 00:30:24 2026 -0400

    260835-69: the Church of Ireland prohibition on incense
    
    The prohibition exists and is NOT in the Prayer Book: it is Canon 38, Of Incense, of the Constitutions and Canons Ecclesiastical of the Church of Ireland (General Synods 1871 and 1877), printed as an appendix inside the 1878 Prayer Book volume but absent from that volume's own Contents. It stands today word for word unchanged as Canon 40 of Chapter IX of the Church of Ireland Constitution. RJ_Incense_Analysis.md section 8's claim is PARTIAL: substance right, attribution wrong; its quotation is unpunctuated and lower-cases public services, matching the modern Canon 40 rather than the 1878 printing, and renders therefor as therefore. So section 8 quoted the modern canon and labelled it a prayer book; correction owed under a fresh authorisation, since the 260835-35 authorisation was expressly limited to the Elphinstone bullet. Scope VERIFIED: absolute, no proviso, no episcopal dispensation, drawn wider than its neighbours (at any time, or other place), sitting mid-way through a seven-canon anti-ritualist sweep (34-40) that also banned crosses outright and candles; penalty at Canon 48, admonition or suspension up to three months, deprivation on a second offence; no prosecution for incense identified. Still stands VERIFIED and is the substantive find: every neighbour was relaxed (crosses 1964, processions and the sign of the cross 1974, candles 1984, wafer bread and vesture loosened) and incense alone was never touched, the last absolute survivor of the 1871 code. Jurisdiction PARTIAL: from 1 Jan 1871 the canons are the internal law of a voluntary association binding its own members as if mutually contracted, with no coercive jurisdiction and by construction incapable of binding the Church of England or TEC (Irish Church Act 1869 ss. 2, 19, 20, 21, verbatim); the Anglican Communion Office gives no date for provincial standing, UNMATCHED, and Article Fifth's original wording could not be obtained, repealed out by the Statute Law Revision Act 1953. Deployable form: an Anglican church, the moment it was free to legislate for its own worship, prohibited incense outright by canon with a stated penalty, and kept it unamended through three revisions that abandoned nearly everything beside it. NOT an Anglican prayer book, and NOT evidence about the Church of England. Owed: registration of the 1878 PDF in SRC_Manifest.md and PROJECT_STATE.md section 4, with size, page count and sha256 recorded in the report.

 Church_Of_Ireland_Incense_Prohibition.md           | 525 +++++++++++++++++++++
 ...-5_and_Irish-Church-Act-1869_ss1-2-19-20-21.txt | 200 ++++++++
 ...cclesiastical_Canons-33-40-48_pdf-pp495-504.txt | 476 +++++++++++++++++++
 ...pter-IX_Canons-2-5-12-13-38-43_Current-Text.txt | 244 ++++++++++
 ...eland-Ritual-Canons-1871-1974_ChurchHistory.txt | 263 +++++++++++
 5 files changed, 1708 insertions(+)
```

## Appendix I — git status --short at close (also in 260835-74_status.txt)

```
 M Incense_Conversational_Outline.md
 M Incense_Outline_Memory_Card.md
 M PROJECT_STATE.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
?? Orthodox_Malachi_1_11_And_Incense_Warrant.md
?? passes/260835-72_followup-intake-and-reserve_close-out.md
?? passes/260835-73_memory-card_close-out.md
?? src/SRC_Discord_Followup.md
?? src/SRC_PRIMARY_0743_John-of-Damascus_Exposition-Orthodox-Faith-IV-13_Malachi-1-11_NPNF2-09-Salmond.txt
?? src/SRC_PRIMARY_0787_Second-Council-of-Nicaea_Definition_Incense-and-Lights_NPNF2-14-Percival.txt
?? src/SRC_PRIMARY_1899_Sokolof_Manual-Orthodox-Church-Divine-Services_Incense-And-Censer.txt
?? src/SRC_PRIMARY_2004_Theodore-of-Mopsuestia_Commentary-Twelve-Prophets_Malachi-1-11_FOTC108-Hill.txt
?? src/SRC_PRIMARY_2008_Orthodox-Study-Bible_Notes-Mal-1-11_Ps-140-141_Sirach-39-14_Lev-2_Num-17.txt
?? src/SRC_SECONDARY_2026_Orthodox-Popular-Apologetics_Incense-Warrant_Peck-OrthodoxAnswers-StMichael.txt
```

*End of close-out. The full diff is 260835-74.diff in this folder; new (untracked) files are copied under new/.*
