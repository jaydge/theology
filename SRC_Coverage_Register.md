# SRC_Coverage_Register — has this been looked at, and by whom, with what result?

**Last updated: 260835-9** (created 260835-9, discharging the `260834-7` standing instruction in `ORCHESTRATION.md` §8, which named this file as forthcoming)

> **What this file is, and is not.** This is a coverage index, one section per source universe, answering one question per universe: *has this been looked at, and by whom, with what result?* It does **not** duplicate `SRC_Manifest.md`'s hashes, byte offsets or per-file registration detail, and it does **not** restate finding text — both stay single-sourced where they already live (`SRC_Manifest.md` for registration, `St_Francis_EMC_Distinctives.md` for findings). Where a coverage state is itself uncertain, that uncertainty is stated as the finding, not resolved by this pass. ⛔ **No coverage classification below was re-derived** — each is cited to the pass that established it. Where this pass found a *later* pass had already corrected or superseded an earlier claim, the later, current state is reported and both are cited, on the project's own dated-note convention.
>
> **New in this file, not carried from elsewhere:** the §8 verification layer — a fresh, this-pass check that every registered `File` number's source still exists on disk and still hashes to its registered value.

---

## 1. EXT-2 (`@barelyprotestant5365`) — `/streams`

**224** of the channel's 306 `EXT-2` rows carry `source_tab = streams` (`SRC_Channel_Inventory.md:18`, counted at registration pass `260833-8`). A prior, external triage from **2026-07-25** is on record as covering **219** entries (`per the brief`, `passes/260833-8_channel-inventory_close-out.md:64`).

`SRC_Channel_Inventory.md`'s own registration-time inference (`:18`) read this as a **scope difference**, but guessed the old triage's scope wrong — it named the `/videos` tab. That guess is **falsified**, not merely superseded: `SRC_Disk_Reconcile_report.md` (run 2026-08-25, outside this repo at `~/EMC/`, gate HEAD `6b01d399`) located the actual source file behind the 219 figure — `livestream-videos-list.txt` (21,137 B, mtime 2026-07-25 00:45 EDT, 219 entries) — and read it directly: **all 218 complete entries read `Streamed N ago`; zero read `Uploaded`.** That is the `/streams` (Live) tab, not `/videos`. §7 Q4 of that report states it plainly: *"The inventory's SPECIFIC INFERENCE — that the old triage covered `/videos` only — is FALSIFIED. It covered `/streams` only."*

**Delta, on the corrected reading: 224 − 219 = 5** — five new livestreams in the month between the two pulls, an ordinary cadence for a channel whose newest indexed entry is "3 weeks ago." This is the likely-new-content figure for `/streams`, per `SRC_Disk_Reconcile_report.md` §7 Q4, itself confirming `SRC_Channel_Inventory.md:18`'s headline (scope difference, not 87 videos of new content) while correcting its named tab.

⚠️ **Two caveats travel with this number, stated rather than dropped.** (1) `livestream-videos-list.txt`'s 219th entry is truncated mid-title — the scrape may have been cut short, so 219 is a **floor**, and the 224−219=5 figure inherits that floor. (2) The index carries **no video IDs**, so it cannot be joined to `channel_videos.tsv` by ID, only by title/duration — a weaker key.

## 2. EXT-2 (`@barelyprotestant5365`) — `/videos`

**82** of the 306 `EXT-2` rows carry `source_tab = videos` (`SRC_Channel_Inventory.md:18`, `260833-8`). Per the corrected reading in §1 above, this is not a residual scope question — it is resolved: `livestream-videos-list.txt` is a Live-tab export and **the `/videos` tab does not appear in it at all.** `SRC_Disk_Reconcile_report.md` §7 Q4 states the consequence plainly: *"the 2026-07-25 triage never saw the `/videos` tab… 82 `EXT-2` `/videos`-tab videos were outside the triage's field of view entirely — not declined, not judged, not seen."*

**These 82 are flagged as awaiting a first triage sweep** (JD's working-list label: **batch 8** — not yet a repo pass; no such pass exists on disk as of this register).

## 3. EXT-3 (`@StFrancisAnglicanSpartanburg`, the parish channel)

**62** videos total (`SRC_Channel_Inventory.md`, header count). No pass has run a systematic triage sweep dedicated to this channel as such; its coverage to date is entirely a byproduct of other registrations landing on channel videos it happens to hold.

Cross-referencing the decision cells directly (not re-deriving them) against the three registrations named — Files 8-9 and 10-12 (the Revelation series) and File 41 (the Anglican Worship series):

| | Count | Basis |
|---|---:|---|
| EXT-3 rows carrying a decision from Files 8-9 / 10-12 / 41 specifically | **20** | 19 `INGESTED`, 1 `CANDIDATE MATCH, EVIDENCED BUT NOT ESTABLISHED` (`C2tCMfq-_hI`) |
| EXT-3 rows carrying *any* decision (the 20 above, plus decisions from other registrations — Files 40/42/43/44 and declines) | **47** | counted directly against the table |
| EXT-3 rows with **no decision cell of any kind** | **15** | six Revelation-class 2026 sessions not yet reached by any registration (Sessions IX-XI, XV-XVII), seven "Anglican Class" 2026 stream sessions (Articles of Religion I-VII), two Morning Prayer stream captures |

47 + 15 = 62. **So: of the 62, 20 carry a decision specifically traceable to the Revelation/Anglican-Worship registrations this section was asked to cross-reference; 47 of the 62 carry a decision from some registration; 15 remain genuinely blank.**

## 4. BLOG — closed at `260804-1`

**Closed.** `PROJECT_STATE.md:862` (pass `260804-1`, "BLOG Batch 5"): *"THE TALLY: 39 blogspot posts, all accounted for (30 previously registered + 1 fully read + 3 skimmed + 5 declined)"* — i.e. 30 registered, 1 fully read (`W32`), 3 skimmed for provenance only (`W33`-`W35`), 5 deliberately declined with reasons on record in `SRC_Manifest.md`. (The academia.edu paper, `W6`, is registered under `BLOG` by Ruling B but is not one of the 39.)

Two items travel alongside the closure, kept distinct from each other and from "open batches":

- **`BLOG-126` live-page confirmation** — logged as owed at `260804-1` (`PROJECT_STATE.md:868`), but **subsequently confirmed and cleared at `260813-1`** (`PROJECT_STATE.md:808`, Task C: *"✅ CONFIRMED, AND THE OUTWARD-USE FLAG IS CLEARED"*). ⭐ **Reported here as CLOSED, correcting the premise that it is still outstanding** — the confirmation discharges attribution only (Known Gap 2 itself is not filled; the caveat's substance is unchanged), but the live-page check itself is done.
- **Four announced-but-unlocated articles** — genuinely still open, and are **leads for a future live-blog search, not unread archive posts**: `BLOG-88`'s Part 2, `BLOG-96`'s Early Church instalment, `BLOG-111`'s Apostolic Succession follow-up, and the Parts 3/4 of the annihilationism series announced in `W34` (`PROJECT_STATE.md:862`, `260804-1`; hedged by him in the announcement and possibly never written).

## 5. POD — `W36`-`W43`

**8 files, all hash-verified.** First registered at `260806-1` (`SRC_Manifest.md`, *"FIRST-TIME REGISTRATION FOR ALL EIGHT — the `W19` warrant class, internal consistency only"* — i.e. the original registration hash was computed once from the files, with nothing prior to check it against). Independently **re-verified against the files on disk** at the external disk-reconcile pass (`SRC_Disk_Reconcile_report.md`, 2026-08-25, §2): *"All eight verified by `sha256(body.strip())`, computed this pass. 8/8 MATCH, zero mismatches."* Byte counts also matched exactly, 8/8. No pass between then and this one has touched these eight files (grep-confirmed: no `W36`…`W43` occurrence in any `passes/26083x-y` close-out after `260806-1`).

## 6. Discord archives — 5 threads

**Five** verbatim Discord thread captures (`SRC_Manifest.md:344`; `RPW`, `Assurance`, `39ArticlesFormularies`, `SevenSacraments`, `BaptismConfirmation`), all hash-verified by `validate_project.py` C6 as of this pass (5/5 OK — see §8 below).

**Standing capture limitation, stated once here rather than per-thread:** every capture of every `src/SRC_Discord_*.md` file is a **manual full-thread copy/paste** from the Discord client, later formatted to Markdown (`SRC_Manifest.md:134`) — Discord access is never automated, per the standing instruction in `ORCHESTRATION.md` §8. Capture-line dating (an explicit `CAPTURED <date>, <time> ET` line per archive) anchors each recapture. `260834-4` registered a fourth capture-method limitation, load-bearing for anything argumentatively sensitive: *"COPY/PASTE PRESERVES PARAGRAPH BREAKS BUT DOES NOT PRESERVE MARKDOWN EMPHASIS — DISCORD'S COPY/PASTE STRIPS ITALIC AND BOLD MARKUP SILENTLY… where emphasis is argumentatively load-bearing, a screenshot taken alongside the paste is the reliable capture method"* (`SRC_Manifest.md:136`; full record at `passes/260834-4_dq24-italics-discharge_discord-emphasis-rule_close-out.md`). This — plus the separately-registered rule that copy/paste never carries an `(edited)` marker (`260801-3`) — applies equally to every thread and is not re-stated five times.

## 7. In-person room recordings — A101 sessions

Every `A101` session with a room capture is dual-captured (`[R]` room + `[S]` stream), **except one**: `A101-2026-06-28`, which is stream-only (`[SW]`/`[SY]`, dual-ASR of the one broadcast) and carries no room capture and never will. `SRC_Manifest.md:526` (ruling `260812-1`): *"`A101-2026-06-28` HAS NO ROOM CAPTURE AND NEVER WILL — CONFIRMED ABSENT, NOT 'NOT YET CAPTURED'… JD searched his recorder app and his files: he did not record the room on 2026-06-28… do not read the absence of one as an un-ingested capture: there is nothing to ingest."* Room-audio search for that session is **closed, per JD's own ruling** — stream capture is accepted as sufficient for it.

All other room-attended sessions on record (2026-06-14 Parts 1-2, 07-19, 07-26, 08-09, 08-16, 08-23) carry `[R]` as PRIMARY, several cross-verified sentence-by-sentence against a companion `[S]` capture (Branch A discipline, `ORCHESTRATION.md`/`SRC_Manifest.md` Note 2a). **One exception inside this set, flagged by §8 below:** the `[R]` primary registered for `A101-2026-07-26` (`A101-20260726-JD-recording-with-q-and-a.md`, carrying `IP-24`…`IP-39`) is not findable on disk — see §8.

## 8. Verification layer — file existence and hash, every registered `File`

**This is new work by this pass, not a restatement of an earlier verification.** For every `File` number registered in `SRC_Manifest.md` (Files 1-46), this pass located the source on disk under `~/EMC/original transcripts/` and computed its SHA-256 fresh, comparing against the manifest's registered value (raw-bytes convention, the value of record per `SRC_Manifest.md`'s own stated rule for Files 40-46, and the sole convention recorded for Files 1-39).

**Result: 46 of 46 — PRESENT AND HASH-VERIFIED. Zero mismatches. Zero absences.** This is stated plainly because a clean result is a real finding, not because it was expected:

| Class | Files | Method |
|---|---|---|
| Plain-text/markdown primary | 1-19, 23, 25, 26, 40-46 | Direct `sha256` of the file, this pass, against `SRC_Manifest.md`'s registered raw hash |
| Born-diarized JSON primary, hash inline in `SRC_Manifest.md` | 20-22, 24, 27-34 | Direct `sha256` of the `sentences.json`, this pass, against the inline registered hash |
| Born-diarized JSON primary, hash held in the source's own `-meta.json` | 35-39 | Direct `sha256` of the `sentences.json`, this pass, against the `outputs` block of its own `-meta.json` (the File 27-34 convention; File 35's hash also happens to be inline and matches) |

Files 1-39 were also independently checked by the external `SRC_Disk_Reconcile_report.md` on 2026-08-25 (gate HEAD `6b01d399`, predating Files 40-46's registration): 38 registered sources, all ✅. **This pass's fresh check agrees with that report everywhere it overlaps, and closes the one gap that report could not: Files 40-46 were registered the day after it ran and had never been checked against disk until now.**

⛔⛔ **One related absence, outside the `File`-number set but material to this layer and not to be lost inside a clean 46/46 headline.** The `[R]` primary for `A101-2026-07-26` — `A101-20260726-JD-recording-with-q-and-a.md`, registered as carrying `IP-24`…`IP-39` (sixteen findings, including three room-only: `IP-37`, `IP-38`, `IP-39`) — **does not exist anywhere under `~/EMC/original transcripts/`.** First identified by `SRC_Disk_Reconcile_report.md` (2026-08-25): *"It is a registry row with no reachable file — the inverse of every other finding in this report."* **Re-confirmed absent by this pass** (fresh recursive search, 2026-08-26). This source is `⛔ ABSENT`: every finding resting on it is unverifiable against its own primary and is flagged as such here; `St_Francis_EMC_Distinctives.md` is not altered by this pass, per the task's own scope limit. ⏳ **Locate it or record it as lost — the coordinates for sixteen findings resolve against it and nothing else does.**

**No `⛔⛔ present-but-hash-mismatch` case was found anywhere in this sweep.** Had one existed, it would be flagged ahead of the absence above — a silent divergence between registered and current material is a worse state than a known absence, because it is not visible without exactly this kind of check.

## 9. Discord archives, POD and A101 stream sources — held outside the repo

Not a separate coverage state, but the standing scope boundary that governs §5-§7 and §12's Files: everything catalogued above as "held outside the repo" lives at `~/EMC/original transcripts/` (occasionally, for older registrations, at a superseded `~/EMC-Anglican/` or `~/EMC-Anglican2/` path, left standing per the never-alter rule — the current path of record is `~/EMC/original transcripts/`, confirmed reachable by this pass for every file it checked). These are deliberately **outside `validate_project.py` C6's scope**, which is scoped to `src/SRC_Discord_*.md` (`260813-1` diagnosis, reaffirmed at every subsequent registration touching this boundary) — not a coverage gap, a documented boundary.

## 10. The pre-manifest `aNNN` files — Files 40-46

This section is built from the actual pass chain (`260834-9` → `260835-1` → `260835-4` → `260835-5` → `260835-6` → `260835-7`), not summarized loosely.

**Registration-only, no targeted mining, by any pass:**

- **File 40** (`a101-1.txt`, Anglican 101 2024 series, `A101-I…VIII`) — registered `260834-9` with coverage "3 Covered · 5 Partially covered" against its own legend; §11 of that pass: *"Depth sweep owed on 5 of 8."* No later pass mined it.
- **File 42** (`a103.md`, Ante-Nicene/Nicene Fathers 2025, `ANF-1..9`) — registered with nine recordings against a legend that says eight; `260834-9` §11: *"Recordings 4, 5, 7 firewalled. Depth sweep owed on 1 and 2."* Not mined since.
- **File 44** (`a106.md`, misc topical, `Misc-2025`) — registered as three recordings, not the banner's six; `260834-9` §11: *"Lowest yield."* Not mined since.

**Needed targeted mining and got it, via `260835-1`:**

- **File 41** (`a101-2.md`, Anglican Worship series) and **File 43** (`a105.md`, Christ in the OT). `260835-1` minted eleven findings as section bullets with byte-range citations (`St_Francis_EMC_Distinctives.md` §13/§17), covering the Malachi 1:11 answer, the silence-of-Acts reductio and 2025 burden rule, the "uniquely Old Testament" qualifier, the incense conversion narrative, the six Levitical offerings mapped onto the 1928 liturgy, and the showbread correction to `DQ-20`, among others.
- **File 43's depth sweep, specifically** — recordings 1, 2 and 5, all read in full (`260835-1` §3.D): rec 1 (class 2) NIL RETURN against the live questions, content already held; rec 2 (class 3) one datum (Cain), everything else already held; rec 5 (class 4) two worked types not already named, with the rest (Christus Victor, dispensationalism, Galatians 3, Melchizedek) already held. **This depth sweep is COMPLETE, not work remaining** — File 43's `COT-n` indexing itself is separately flagged as an unresolved locator problem (`260834-9` §4, carried from `260834-7`), which is a different, still-open issue from the depth sweep.

**Wrongly flagged "wholly unmined," required retro-registration instead:**

- **File 45** (`a201.txt`) — `SRC_Manifest.md`'s own table (line 3339) still reads *"NONE — WHOLLY UNMINED"* as an unaltered marker, per the never-alter rule, with a dated note beside it. The marker is **false**: `260835-4` established that `a201.txt` (with `a202.txt`) is the source of the `GV` batch, mined in full at `260621-1` as `GV-1`…`GV-55` (`St_Francis_EMC_Distinctives.md` L6971, read directly at HEAD). `260835-4` also found four existing findings misattributed to Rev. James that are actually his debate interlocutor Fr Matt Kennedy's (`GV-2`, `GV-3`, `GV-4`'s second half, `GV-6`'s Lordship-Salvation clause); corrected by dated note (never silently rewritten) at `260835-5`, which also retro-registered byte ranges for 34 of 54 in-scope `GV` findings and minted one new finding (`GV-56`, the burden rule) from non-duplicative material `260835-4` located but did not log as a finding.
- **File 46** (`a202.txt`) — same false "WHOLLY UNMINED" marker (line 3340), same never-altered-with-a-note treatment. `260835-6` (read-and-report) established the marker false for all four of its recordings; `260835-7` retro-registered byte offsets for the remainder of the `GV` range and corrected two further misattributions (`GV-50`, entirely the Minton-debate moderator's introduction of Rev. James, not his own words; `GV-51`, split — the matter-validity half his, the "EO have valid orders" half his opponent Noah Edmonds answering James's own cross-examination question).

**Genuinely unresolved findings — not guessed at, search terms on record:** `GV-12` and `GV-55`. `SRC_Manifest.md` (registered `260835-7`): *"'ryle' (lowercase) returns exactly 1 hit… not `GV-12`'s claimed content… no verbatim self-positioning sentence was found"*; *"'lent' returns 10 hits… not a usable single anchor; 'deuterocanon' returns exactly 1 hit… no confident location exists"* for `GV-55`. Same language appears in `St_Francis_EMC_Distinctives.md` L7024-7026.

**Partial-coverage recordings, explicitly distinct from "unmined" — work remaining:**

| Recording | Depth | Basis |
|---|---|---|
| `a202`/File 46, rec 1 (Apostolicae Curae debate) | **~46%** | a contiguous middle stretch is mined; the first ~24,000 B (rules/intros) and last ~27,000 B (closing rebuttal, Q&A) are not (`260835-7`) |
| `a202`/File 46, rec 2 (Minton debate) | **partial, non-contiguous** | less than its raw citation count suggests once the `GV-50`/`GV-51` corrections are subtracted (`260835-7`) |
| `a202`/File 46, rec 3 (Monarch of England) | **partial by strict citation span** (~2,450 of 9,067 B directly quoted, though topically continuous) | `260835-7` |
| `a202`/File 46, rec 4 (How to Use the 2019 BCP) | **~4%** | one confirmed single-sentence citation near the opening; over 96% carries no located citation (`GV-55`, tentative/unconfirmed, sits here) | `260835-7` |

`SRC_Manifest.md`'s own line for File 46 (post-`260835-7`): *"NOT MINED THIS PASS. A future mining pass… should treat this as a depth-sweep-with-gaps job… not a first mining of virgin material."*

**Standing hazard, `File 46`/`a202.txt`, registered `260835-7` and not to be re-derived:** the diarization label `B` is Rev. James in recording 1 and his opponent Noah Edmonds in recording 2 — the mapping inverts inside the same file, and is the mechanism behind `GV-50`/`GV-51`.

**Rejected re-supply, not a source:** `a301-Classical-Theism.md`. `SRC_Manifest.md` (recorded `260834-9`): it is a re-supply of File 44 recording 2's exact byte range (99.92% `difflib.quick_ratio`, identical `>>` counts), *"IS NOT A SOURCE. IT IS NOT REGISTERED AS A FILE, IT GETS NO SESSION ROW, NO STANDALONE ROW AND NO FINDING TAG… Disposition | ⛔ REJECTED RE-SUPPLY. Do not register, do not ingest, do not tag."* Its hash differs from File 44's (a hash-keyed intake would pass it), so the rejection rests on content comparison, not a hash check; its one distinguishing feature (`### Jun 6, 2026` header) is preserved in `SRC_Manifest.md` as the sole internal witness that File 44 recording 2's `Misc-2025` banner year is false.

## 11. Permanent limits — stated as permanent, not pending

**Files 1-26 predate the `-meta.json` procedure and carry no video IDs.** `SRC_Channel_Inventory.md` Step 5b tallies all 26 against channel video candidates: **19 of 26 matched** (title + independent date corroboration: Files 3, 5, 6, 7, 10, 13-26 less the two below); **2 of 26 ambiguous** and left blank rather than force-matched (File 11, whose own "Session XIV" numbering conflicts with the channel's own numbering; File 12, same conflict at "Session XV" — the corpus's session numbers are not reliably self-consistent, per the manifest's repeated warning); **5 of 26 have zero candidates** (Files 1-2, in-person audio never uploaded; File 4, spanning three sessions; Files 8-9, a nine-block transcript across eight sessions). 19+2+5 = 26. **These are stated as permanently uncertain where no further evidence exists — not as open matching work.**

**Four videos carry no metadata record**, and are the one item in this section flagged for re-check rather than treated as permanently inaccessible. `SRC_Channel_Inventory.md`: *"4 of the 368 TSV video IDs have no `channel_metadata.jsonl` record — `Wt7HI5SJahk`, `mfty5D0PAF0`, `b6hTPg50R9Q` (all three members-only at pull time) and `7HKFlfqG1jY` (a not-yet-started livestream at pull time)… This is flagged for a future re-check, not assumed permanently inaccessible — a members-only video can become public, and a not-yet-started livestream will eventually air and acquire metadata."*

---

## Changelog

- **v1.0 — 260835-9.** File created, discharging the `260834-7` standing instruction. Sections 1-11 built from the cited passes without re-deriving any coverage classification; §8 (verification layer) is fresh work by this pass: 46/46 registered `File` numbers checked against disk, present and hash-matched, zero mismatches, zero absences; one related, non-`File`-numbered absence (the `A101-2026-07-26` `[R]` primary) re-confirmed still missing. Registered in `PROJECT_STATE.md` §4.
