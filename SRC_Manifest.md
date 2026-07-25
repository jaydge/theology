# SRC_Manifest — Transcript Source Manifest

**Last updated: 260725-1** (date-stamped, format yymmdd-iteration)

*Generated 2026-07-22; extended 2026-07-24 (260724-1), capture-method and dating rule corrected 260724-3; archive paths recorded and IP-4/IP-12 references corrected 260725-1.*

* Covers the ASR transcript files uploaded for verbatim verification (Files 1-3) and the four archived Discord thread captures (added 260724-1). Append-mode intake; no canonical documents touched by this file.*

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
