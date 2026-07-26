# SRC_Manifest — Transcript Source Manifest

**Last updated: 260725-4** (date-stamped, format yymmdd-iteration)

*Generated 2026-07-22; extended 2026-07-24 (260724-1), capture-method and dating rule corrected 260724-3; archive paths recorded and IP-4/IP-12 references corrected 260725-1. **260725-4: File 4 (Revelation class corpus) registered from batch 260725-2; the sessions-ingested registry, capture codes and dual-capture reconciliation procedure added from batch 260725-3; boundary-detection method amended to record that two intake formats are now in play; **placeholder rows added for the unregistered Anglican 101 sessions JD confirmed he has attended since 06-14, dates pending.***

* Covers the ASR transcript files uploaded for verbatim verification (Files 1-3), the Revelation class corpus (File 4), and the four archived Discord thread captures (added 260724-1). Append-mode intake; no canonical documents touched by this file.*

## Boundary-detection method (checked before relying on any result)

Searched both files for every plausible marker a multi-video export might use: all-caps title lines, blank-line/double-newline separators, form-feed characters, timestamp patterns (`H:MM`), and transition phrases ("welcome," "episode," "part N," "session N," etc.).

**Result: none found.** Both files:
- contain zero blank lines and zero double-newlines (checked programmatically),
- contain no timestamp markers,
- contain no all-caps header lines,
- contain no recognizable intro/transition phrasing marking a new recording.

Each file is one continuous stream of single-sentence lines (Whisper-style ASR output) with no internal segmentation markers of any kind.

**Conclusion:** each file is treated as a single video/recording spanning its entire byte range. This matches the filename convention (`Audio_MM_DD_YYYY_HH_MM_SS_mp3.txt`), which timestamps one recording's start time per file, not a batch of videos. The two files here are ~65 minutes apart on the same date and appear to be two sequential recordings from the same evening (first in-person Anglican 101 class + Q&A session), not multiple distinct videos bundled into one file.

If this assumption is wrong for a future upload (i.e., a file really does bundle multiple videos with a different export format), flag it — this detection method won't catch boundaries that don't use any of the marker types checked above.

### ⚠️ AMENDMENT 260725-4 — TWO INTAKE FORMATS ARE NOW IN PLAY. DO NOT APPLY THE SINGLE-VIDEO ASSUMPTION BY DEFAULT.

The section above was written when every uploaded source was raw single-stream ASR. **File 4 (`a302-Revelation-June-July-2026.md`) is the flagged case that section asked to be told about.** It is not raw ASR: it is structured markdown with `##` session titles and `###` date lines, carrying **three videos, cleanly delimited**.

| Format | Recognition | Boundary rule |
|---|---|---|
| **Raw ASR** (Files 1-3) | Single-sentence lines, zero blank lines, no headers, filename of the form `Audio_MM_DD_YYYY_HH_MM_SS_mp3.txt` | One file = one recording. Byte range is the whole file |
| **Structured markdown** (File 4 onward) | `##` / `###` header lines, long-line ASR bodies | **Boundaries are explicit. Read them; do not infer.** Record per-video byte ranges |

**The rule:** check for `##` / `###` headers *first*, on every new upload. Only fall back to the marker sweep above when there are none.

## File 1

| Field | Value |
|---|---|
| Filename | `Audio_06_14_2026_19_21_22_mp3.txt` |
| SHA-256 | `51a0a42375c6fff0f5df6bc219717a0388e5bfd8ddc646f2fe23c45cc69085e6` |
| Size | 49,562 bytes |
| Lines | 874 |
| Video count detected | 1 |
| Byte range | 0–49,562 (entire file) |
| Content | First in-person Anglican 101 class + Q&A. Contains the Malachi 1:11 incense passage (source of **IP-12**, promoted from IP-4 on 260725-1). |

## File 2

| Field | Value |
|---|---|
| Filename | `Audio_06_14_2026_20_26_39_mp3.txt` |
| SHA-256 | `0b5a50b3a7a6a373e658154ec47babf51ce303fd73918df8d90e3998e0b4d440` |
| Size | 41,452 bytes |
| Lines | 866 |
| Video count detected | 1 |
| Byte range | 0–41,452 (entire file) |
| Content | Continuation Q&A (sacraments, church history reading list, church-shopping discussion). Two "incense" mentions (offsets 9914, 10339) but not the BP-39 material — see File 3 below. |

## On merging Files 1 and 2

**Recommend keeping them as separate files, unmerged.** Byte offsets already logged in the canonical docs (e.g. `IP-12`, formerly `IP-4`, at 12441–13335) were computed against these exact files; merging into one new file would shift every offset after the merge point and invalidate the existing citations without adding anything — the two are already cleanly identifiable as one evening's session in two parts. If clearer labeling is wanted without touching the files themselves (renaming an uploaded file isn't possible from this end, and re-uploading under a new name would just create a third artifact with the same content), the cleanest fix is a **canonical alias**, tracked here rather than on disk:

| Canonical alias | Actual filename | Role |
|---|---|---|
| IP-Session-2026-06-14 · Part 1 | `Audio_06_14_2026_19_21_22_mp3.txt` | First in-person Anglican 101 class + Q&A (contains IP-12/Malachi passage; IP-12 was IP-4 before 260725-1) |
| IP-Session-2026-06-14 · Part 2 | `Audio_06_14_2026_20_26_39_mp3.txt` | Continuation Q&A, same evening |

Any future reference to "the first in-person session" can cite "Part 1 / Part 2" and this table resolves it to the real filename and hash — offsets stay exactly as already logged, nothing to recompute.

## File 3 — BP-39 source (added 2026-07-22)

| Field | Value |
|---|---|
| Filename | `Responding_to_Matthew_Everhard_on_the_Regulative_Principle_mp3.txt` |
| SHA-256 | `d3fc2406b9f26f6a69e282eb13460df196230b36d96ff67ce9335fbf342960e5` |
| Size | 69,507 bytes |
| Lines | 940 |
| Video count detected | 1 |
| Byte range | 0–69,507 (entire file) |
| Content | RJ's response video to Matthew Everhard on the regulative principle — the "BP/Everhard video" referenced elsewhere in the canon. Confirmed single continuous transcript, same no-marker format as Files 1–2 (checked for headers, blank lines, form feeds, timestamps — none found). Opening line ("today we're going to do a video on the question of the regulative principle") matches the filename and confirms single-video scope. Contains the BP-39 material — see patch block for verified verbatims.

## File 4 — Revelation class corpus (added 2026-07-25, batch 260725-2)

| Field | Value |
|---|---|
| Filename | `a302-Revelation-June-July-2026.md` |
| SHA-256 | `f8571cae84e4aad0fec5d42222483b2d2bab0e5574838d7f51be8ec1c82cba44` |
| Size | 94,822 bytes |
| Lines | 14 (structured markdown; long-line ASR bodies) |
| Video count detected | **3** (explicit `##` / `###` headers; **first file in the corpus with real internal boundaries** — see the 260725-4 amendment to the boundary-detection section above) |
| Hash checked against manifest | ✅ No collision. Not previously ingested |
| Capture | `[S]` — Rev. James's channel audio |
| Findings sourced | **RV-1 … RV-23** (contiguous, no gaps) |

### Per-video byte ranges

| Session | Title (as written) | YouTube upload date | Recording date | Header bytes | Transcript body bytes |
|---|---|---|---|---|---|
| **IX** | Revelation Class, Session IX: the Beast and the Bottomless Pit (Chapter 11) | 2026-06-21 | **2026-06-21** | 28-123 | **125-29,423** |
| **X** | Revelation Class, Session X: the Woman, the Child, and the Dragon | 2026-06-30 | ⚠️ not established | 29,425-29,510 | **29,512-60,374** |
| **XI** | Revelation Class, Session XI: the Two Beasts and the Mark | 2026-06-30 | ⚠️ not established | 60,376-60,453 | **60,455-94,822** |

⚠️ **The header dates are YouTube UPLOAD dates, not recording dates**, and are preserved as written because they are the lookup key for finding the source video. Session IX's recording date is well supported (the class is Sunday morning; the most recent Sunday on or before the 06-21 upload is 06-21 itself; the content self-confirms with "the handout you have includes the first uh what we did last Sunday"). **Sessions X and XI are stamped *uploaded 2026-06-30, recording date not established*** — both follow Session IX and precede the 06-30 upload, and the only Sunday in that window is 06-28, which two sequential sessions cannot share. One glance at the channel's video list closes it; nothing in the corpus depends on it.

**All byte offsets for RV findings are absolute against the whole file,** not against a per-session split. Every quote was located by uniqueness check against all 94,822 bytes; no quote occurs more than once, so no offset is ambiguous.

### Canonical aliases — Revelation corpus

| Canonical alias | Byte range | Role |
|---|---|---|
| RV-Session-IX | 125-29,423 | Revelation 11, second half |
| RV-Session-X | 29,512-60,374 | Revelation 12 |
| RV-Session-XI | 60,455-94,822 | Revelation 13 |

### ASR quirks — File 4, preserved as transcribed

Recorded so later greps do not fail silently and so nobody "corrects" a quote in place. Precedent: `"regular principle"` at IP-12. ⚠️ **Quirks are properties of a CAPTURE, not of a session** — see the dual-capture procedure below.

- **"predtoist"** for *preterist*, throughout Session XI
- **"hyper predatorism"** for *hyper-preterism* (XI 72864)
- **"nosticism" / "innosticism" / "protonostic"** for *Gnosticism* etc., throughout XI; the leading g is dropped repeatedly
- **"Simon"** for *simony* (XI, Simon Magus passage)
- **"Gamatria"** for *gematria* (XI); he flags his own uncertainty aloud
- **"playma"** for *pleroma*; **"aestheticism"** for *asceticism* (XI)
- **"kleth"** for *killeth*, **"leadth"** for *leadeth* (XI, KJV reading)
- **"{slash}"** as a literal token at X 39990, where he said "Israel slash the church"
- **"his session at the Father"** for *session* / *intercession* at the Father's right hand (IX); he self-corrects aloud in the same sentence

### ⚠️ Speaker-attribution warning — File 4

The `>>` diarization markers are **sparse and unreliable**: 4 in Session IX, 22 in Session X, 41 in Session XI, against 95 KB of text. Long stretches of RJ's teaching carry no marker at all, and several parishioner questions are marked only on the reply. **Do not treat an unmarked span as attributed.** Every RV quote was read in context and attributed by content, not by marker. Parishioner speech is logged as such and given no tag, per §5 numbering rule 3.

---

# Discord Thread Archives (added 2026-07-24)

*Four verbatim Discord thread captures (DiscordChatExporter). Unlike Files 1-3 above, these are **not** ASR transcripts: they are structured markdown with speaker headers and message timestamps, so findings are cited by **message timestamp**, not byte offset. They are the archival source for the entire **DQ** finding series (DQ-1 … DQ-15).*

## ⚠️ CAPTURE METHOD AND DATING RULE (corrected 260724-3)

**Capture method.** These archives are **copy/paste from the Discord client**, not tool exports. That is why recent messages arrive as **relative timestamps** ("Yesterday at 11:42 AM", "Today at 9:04 AM") instead of absolute dates: Discord renders them relative to *the moment of viewing*.

**⚠️ THE RULE, and it is not optional.** A relative timestamp in a pasted thread is relative to **the date JD supplies the paste**, not to the intake session, not to the export date, and not to any date written in the file.

**Standing procedure for every Discord intake:**
1. **Note the handover date** (the date JD provides the paste). That is the anchor.
2. **Resolve every relative timestamp to an absolute date against that anchor before logging anything.** "Yesterday" = handover date minus one. "Today" = handover date.
3. **Write the resolved absolute dates into the `SRC_Discord_*.md` file itself**, replacing the relative forms, so the archive is self-dating and the anchor never has to be reconstructed later.
4. **Then** log findings, dating each from the resolved message timestamp.

**Why this rule exists.** Three consecutive passes (260715-1, 260722-1, 260723-1) dated findings from the *intake session* rather than the message. **DQ-5 was carried as "awaiting reply" for nine days after it had been answered**, and the funnel was held closed for two weeks behind a gate that was already open. DQ-7 was logged a day late by the same mechanism. **Resolving dates at intake, in the archive file, is what prevents a recurrence** — a relative timestamp left unresolved is a live error waiting for the next pass to inherit.

| Field | Value |
|---|---|
| Filename | `SRC_Discord_RPW.md` |
| SHA-256 | `66f5f17f5db1956f9fa3a581e1f91a4579f3862def7524a3c976e5c1919907be` |
| Size | 18,381 bytes |
| Lines | 206 |
| Thread | "Regulative Principle" (opened by JD, 2026-06-18) |
| Coverage | 2026-06-18 → 2026-07-23 |
| Export history | 260722-1 initial (relative timestamps unresolved); **260724-1 re-export**, extends through 07-23 and resolves the three "Yesterday" timestamps to 07-21 |
| Findings sourced | **DQ-3, DQ-4, DQ-5, DQ-7, DQ-8, DQ-9, DQ-10, DQ-7a, DQ-14, DQ-15** — the priority channel and the source of the entire incense funnel |

| Field | Value |
|---|---|
| Filename | `SRC_Discord_39ArticlesFormularies.md` |
| SHA-256 | `c28363cd4e9c33e49d06aab47cea2adbfd0f5e56ca72798afba987f2d41ffc9b` |
| Size | 12,717 bytes |
| Lines | 172 |
| Thread | "39 articles, Anglican formularies, and exceptions to them" (opened by JD, 2026-06-16) |
| Coverage | 2026-06-16 → 2026-07-21 |
| Export history | 260722-1 initial; **260724-3 relative timestamps resolved to 07-21** |
| Findings sourced | **DQ-1, DQ-6, DQ-12.** Also contains the third-party (M1B3AU) material and JD's uncorrected-by-design reply |

| Field | Value |
|---|---|
| Filename | `SRC_Discord_SevenSacraments.md` |
| SHA-256 | `45251fbdfa286da08e13e8389eda43212a36f5654abf646881a2d3d3f769171f` |
| Size | 7,279 bytes |
| Lines | 74 |
| Thread | "Seven sacraments vs. Article 25" (opened by JD, 2026-06-17) |
| Coverage | 2026-06-17 → 2026-07-21 |
| Export history | 260722-1 initial; **260724-3 relative timestamps resolved to 07-21** |
| Findings sourced | **DQ-2, DQ-11.** Closes question-list item 20 |

| Field | Value |
|---|---|
| Filename | `SRC_Discord_BaptismConfirmation.md` |
| SHA-256 | `3d36452d4deaea516ed6a442630cc0ea4e6036bfa380ac1cf947ade406bb1301` |
| Size | 5,999 bytes |
| Lines | 103 |
| Thread | "Baptism & Confirmation" (opened by **LilleyPartyofFive**, 2026-06-28 — **JD is not a participant**) |
| Coverage | 2026-06-28 → 2026-07-04 |
| Export history | 260722-1 initial |
| Findings sourced | **DQ-13.** ⚠️ Thread-etiquette note attached at DQ-13: anything raised from this thread elsewhere should be sourced to RJ's teaching generally, not framed as picking up another parishioner's thread |

## Canonical aliases — Discord threads

| Canonical alias | Actual filename | Role |
|---|---|---|
| DQ-Thread-RPW | `SRC_Discord_RPW.md` | Priority channel; the incense funnel |
| DQ-Thread-Formularies | `SRC_Discord_39ArticlesFormularies.md` | Article VI / self-contradictions |
| DQ-Thread-Sacraments | `SRC_Discord_SevenSacraments.md` | Article 25 / the Five |
| DQ-Thread-Baptism | `SRC_Discord_BaptismConfirmation.md` | Baptism & Confirmation (JD absent) |

---

# Sessions Ingested (added 260725-4, batch 260725-3)

## ⚠️ THE SESSION IS THE CITATION UNIT. THE CAPTURE IS A SUBSTRATE.

A finding tag names a **session**, never a file. `IP-12` is a thing Rev. James said on 2026-06-14; it is not a thing that lives at byte 12441 of a particular mp3 transcript. **Tags never move when a capture is replaced.** Only coordinates move, and coordinates are not identity.

This table exists because the hash check cannot do this job. The file tables above check whether a **file** has been ingested. They cannot tell whether an **event** has been ingested, and the same event reaches this project through two doors: JD's room recorder, and Rev. James's YouTube upload of the same class. Those are two files, two hashes, and one session. **A hash check passes both and duplicates every finding.**

**Ingestion test, run before every intake:** does a row already exist for this *session*? Not: does this hash already appear?

### Capture codes

| Code | Meaning |
|---|---|
| **`[R]`** | **Room.** JD's own recorder, in the building. Distant mic, higher ASR error rate |
| **`[S]`** | **Stream.** Rev. James's channel audio. Close mic, lower error rate. **Authoritative for wording where it exists** |
| **`[?]`** | Provenance not recorded. Should not occur going forward |

> ### ⚠️ RETROFIT RULE — this is the whole retrofit
>
> **Any byte offset recorded before 260725 without a capture code refers to the capture marked PRIMARY for its session in the table below.**
>
> **Do not edit existing findings to add codes.** Add codes going forward. Everything already cited stays valid and stays findable.

### ⭐ ANGLICAN 101 — the series JD attends in person

*Findings prefix `IP`. These are the sessions where JD is in the room and can ask follow-ups. **Every one of these has, or will have, a stream twin on the channel.***

| Session ID | Date | Covered | JD present | Capture | Role | File | SHA-256 (first 8) | Bytes | Findings | Wording-critical? |
|---|---|---|---|---|---|---|---|---|---|---|
| `A101-2026-06-14-P1` | 2026-06-14 | First class + Q&A; Malachi 1:11 incense passage | ✅ **YES** | `[R]` | **PRIMARY** | `Audio_06_14_2026_19_21_22_mp3.txt` | `51a0a423` | 49,562 | **IP-12** (promoted from IP-4, 260725-1) | ⚠️ **YES — see note 1** |
| ″ | ″ | ″ | ″ | `[S]` | ⬜ **NOT YET INGESTED** | *(on channel, not yet pulled)* | — | — | — | — |
| `A101-2026-06-14-P2` | 2026-06-14 | Continuation Q&A: sacraments, reading list, church-shopping | ✅ **YES** | `[R]` | **PRIMARY** | `Audio_06_14_2026_20_26_39_mp3.txt` | `0b5a50b3` | 41,452 | *(two incense mentions, not BP-39 material)* | — |
| ″ | ″ | ″ | ″ | `[S]` | ⬜ **NOT YET INGESTED** | *(on channel, not yet pulled)* | — | — | — | — |
| `A101-2026-TBD-01` | ⚠️ **DATE TBD** | ⚠️ unknown — JD to supply | ✅ **YES** | `[?]` | ⬜ **NO AUDIO INGESTED** | *(none)* | — | — | *(none yet)* | — |
| ″ | ″ | ″ | ″ | `[S]` | ⬜ **NOT YET INGESTED** | *(presumed on channel, not yet pulled)* | — | — | — | — |
| `A101-2026-TBD-02` | ⚠️ **DATE TBD** — *may not exist; JD reports "1-2" further sessions* | ⚠️ unknown — JD to supply | ✅ **YES** *(if held)* | `[?]` | ⬜ **NO AUDIO INGESTED** | *(none)* | — | — | *(none yet)* | — |
| ″ | ″ | ″ | ″ | `[S]` | ⬜ **NOT YET INGESTED** | *(presumed on channel, not yet pulled)* | — | — | — | — |

**Note 1 — `A101-2026-06-14-P1` is the single highest-priority recapture in the corpus.** It carries `IP-12`, whose logged ASR quirk is `"regular principle"` for *regulative principle*. That is a distant-mic artifact with high confidence; his capture will very likely read "regulative principle." `IP-12` is the §13 incense finding and it sits inside the funnel. **Pull the stream capture for this session first.**

**⚠️ Note 2 — GAP CONFIRMED AND NOW VISIBLE. ⚠️ AWAITING JD FOR THE DATES (raised and confirmed 260725-4; rows added, NOT completed).**

Raised at 260725-4 as a suspected gap and **confirmed by JD in the same pass: he attended the 06-14 session (rows above) plus a further ONE OR TWO Anglican 101 sessions since, dates not yet supplied.** Placeholder rows `A101-2026-TBD-01` and `A101-2026-TBD-02` are now in the table.

**This is the whole point of the row, so it is worth being blunt about what the placeholders do and do not do:**

- They make the gap **visible**. Before this pass the corpus contained no evidence that these sessions existed at all. **An empty row is a visible gap; an absent row is an invisible one**, and an invisible gap is the defect class this project keeps paying for.
- They **do not** claim the sessions were captured. Capture is `[?]` and the role is **NO AUDIO INGESTED**. A session that happened is a session that exists, **even if nothing was recorded**.
- `A101-2026-TBD-02` is marked **may not exist**, because "1-2" is what is known. **Do not silently delete it if it turns out there was only one session** — mark it *did not occur* and leave it, so the question is never re-asked.

**⚠️ WHAT JD NEEDS TO SUPPLY BEFORE THESE ROWS CAN BE COMPLETED:**

1. **The date of each session** (this is the blocker; the Session ID is derived from it and cannot be minted without it).
2. **What each session covered.** The Anglican 101 series was working through the Thirty-Nine Articles, so approximately which Articles.
3. **Whether room audio exists** for either. If it does, it is an `[R]` capture and the ingestion pipeline applies as normal.
4. **Whether the stream twin is on the channel.** Every in-person session is expected to have one, and per note 1 the `[S]` capture is authoritative for wording.

⚠️ **Until the dates land, no `IP` finding may be logged from these sessions.** Next free is `IP-13` (`PROJECT_STATE.md` §5); a finding cannot be dated from a session whose date is unknown, and **dating a finding from the intake session rather than the source is the exact mechanism that cost this project two weeks in July 2026.**

### REVELATION CLASS — series JD does not attend

*Findings prefix `RV`. Stream-only, so no dual-capture problem arises. Session numbers are Rev. James's own. Source file: **File 4** above.*

| Session ID | Uploaded | Recorded | Covered | JD present | Capture | Role | File | Byte range | Findings |
|---|---|---|---|---|---|---|---|---|---|
| `RV-S09` | 2026-06-21 | 2026-06-21 | Revelation 11, second half | — no | `[S]` | **PRIMARY** | `a302-Revelation-June-July-2026.md` | 125-29,423 | **RV-1 … RV-10** |
| `RV-S10` | 2026-06-30 | ⚠️ not established | Revelation 12 | — no | `[S]` | **PRIMARY** | ″ | 29,512-60,374 | **RV-11 … RV-19** |
| `RV-S11` | 2026-06-30 | ⚠️ not established | Revelation 13 | — no | `[S]` | **PRIMARY** | ″ | 60,455-94,822 | **RV-20 … RV-23** |
| ⬜ | | | *Sessions I-VIII precede the corpus and are not ingested* | — no | | | | | |

**Note 3.** Sessions I through VIII exist and are presumably on the channel. They are not ingested and are not findings-bearing. Rows are omitted rather than left blank because nothing in the corpus cites them; add rows if and when they are pulled. *(The 2025 Revelation class logged under the `Rev` prefix in `St_Francis_EMC_Distinctives.md` §18 is a different, earlier run of the class and is not covered by these rows.)*

### STANDALONE RECORDINGS — not part of any series

*Findings prefix `LS` going forward. These stay in the file tables above and get no session rows, because a one-off video is its own session and the hash check is sufficient for it.*

| Recording | Capture | File | SHA-256 (first 8) | Findings |
|---|---|---|---|---|
| Response to Matthew Everhard on the regulative principle | `[S]` | `Responding_to_Matthew_Everhard_on_the_Regulative_Principle_mp3.txt` | `d3fc2406` | **BP-39** and the BP batch |

⚠️ **`BP` is a closed batch that would today be `LS`. Leave it. Do not retro-renumber a closed series.**

---

# Dual-Capture Reconciliation Procedure (added 260725-4, batch 260725-3)

*Run when a stream capture arrives for a session already ingested from room audio.*

⚠️ **Do not run this in the same session as a live intake.** Same reason the currency audit carries that warning: it audits state, and intake creates state.

**Step 1. Register, do not promote.** Add the `[S]` capture as a row under the existing session. Role: `SECONDARY — SWEEP PENDING`. **Leave `[R]` as PRIMARY.** The room capture stays authoritative until the sweep is finished, because until then it is the only capture the corpus's coordinates actually resolve against.

**Step 2. Sweep every finding citing that session.** For each verbatim quote, search the `[S]` capture. Four outcomes, each logged:

| Outcome | Meaning | Action |
|---|---|---|
| ✅ **CONFIRMED** | Found, byte-identical | Record `[S]` offsets alongside `[R]`. No amendment |
| ⚠️ **AMENDED** | Found, wording differs | **This is the payload of the whole exercise.** Record both strings verbatim. Then judge separately whether the corrected wording changes the finding's force, and say so explicitly |
| ⛔ **NOT FOUND** | Quote absent in any form | **Highest severity.** Either the finding rests on a mishearing, or the captures differ in scope. Resolve before promoting. **A finding in this state must not be deployed** |
| ⬜ **OUT OF SCOPE** | The `[S]` capture does not cover that stretch (stream started late, dropped) | Not an error. Record it, and keep `[R]` as the citation substrate for that finding specifically |

**Step 3. Log amendments as amendments, not as new findings.** Per §5 numbering rule 2, a correction to `IP-12` is **`IP-12a`**, taking the parent's number with a letter suffix. It is not the next free number. An amendment that silently became a sibling is exactly the mis-numbering that produced the `DQ-11a` correction on 260724-3.

**Step 4. Promote, and keep the old capture.** Only after the sweep completes: `[S]` becomes PRIMARY, `[R]` becomes `SUPERSEDED`. **Do not delete the room capture and do not unregister it.** Changelog entries cite it, changelogs are never altered, and a superseded capture that has been unregistered turns every historical citation into a dead pointer.

**Step 5. Move the ASR quirks.** Quirks are properties of a **capture**, not of a session. When `[S]` becomes PRIMARY, the quirk register for that session is rebuilt against the new capture and the old list is retained under the `[R]` row rather than deleted. `"regular principle"` is a fact about JD's microphone, not about what Rev. James said.

**Step 6. Clear the wording-critical flag.** Any finding marked WORDING-CRITICAL that came back CONFIRMED or AMENDED is now quotable. Findings still NOT FOUND stay frozen for quoting.

## ⚠️ WORDING-CRITICAL — the standing do-not-quote-yet rule

Most findings survive a transcription error fine, because the substance does not turn on the exact phrase. A few do not: `DQ-4`'s **"Correct"** closed the definitional gate on one word.

**A finding whose force depends on Rev. James's exact phrasing, sourced from a room `[R]` capture, must not be deployed as a verbatim quote until it is confirmed against his audio.** This is not a freeze on the finding; it is a freeze on quoting it at him. Given the quote-precision rule and the friendship stakes, being wrong about a word attributed to him in writing is the one error in this project that is expensive socially as well as evidentially.

**Currently flagged:** `IP-12` (`A101-2026-06-14-P1`). ⚠️ **The `RV` batch is `[S]`-sourced and is therefore not subject to this rule** — File 4 is already his channel audio.
