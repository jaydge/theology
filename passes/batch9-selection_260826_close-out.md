# Batch 9 Selection — Read-and-Report Pass (2026-08-26)

**Not a registered project pass.** No corpus file was edited (per the brief's explicit scope limit), so this artifact carries no `26xxxx-n` project stamp and is not entered in `PROJECT_STATE.md`'s pass ledger. It is reference material only — see `passes/README.md`'s own carve-out for non-registering artifacts. File name is date-stamped by real calendar date, not the project's internal counter.

---

## 1. Gate

- `git rev-parse HEAD`: `83bf85bfc716bddd8bd83c4c753bd3be525872d2` — matches the briefed `83bf85b`. ✅
- `git --no-optional-locks status --short`: **EMPTY** before this pass and unchanged throughout (confirmed again at close, §9 below).
- `python3 validate_project.py`: **82 ok · 9 warnings · 0 errors.** All nine firing codes (unchanged from the corpus's own last-recorded run, so listed rather than re-derived): `[C1]` `src/SRC_Discord_RPW.md` — 2 relative timestamps outside message headers; `[C3]` `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` — no parseable stamp; `[C3]` `tools/transcribe_yt.py` — no parseable stamp; `[C4]` `St_Francis_EMC_Distinctives.md` — 2 stale answered-question passages; `[C5]` `RJ_Final_Question_List.md` — 17 volatile-state assertions; `[C5]` `RJ_Incense_Analysis.md` — 9; `[C5]` `St_Francis_EMC_Distinctives.md` — 7; `[C10]` §15 eight findings behind the `LS` ledger head; `[C11]` outline eleven `IP` findings unreviewed. None of the nine concern anything this pass touched.
- `PROJECT_STATE.md`'s own stamp: **260835-10** (its "Last updated" line, top of file).

## 2. Candidate pool — the "96 flagged" claim, independently checked

Per the brief's own warning not to trust that claim, I grepped the repo fresh (`Tier 1`, `Tier 2`, `Tier-1`, `Tier-2`, `96 flagged`, case-insensitive, all `.md`). **No such pass and no such count exist anywhere in the repo.** The only "Tier 1" hits are unrelated doctrinal content in `St_Francis_EMC_Distinctives.md` (a quoted "Tier 1: Catholic doctrine…" line about assurance). This matches — and I confirmed independently rather than took on faith — the corpus's own `260835-10` pass note, which records the identical check and the identical null result. **No comparison against "96" is offered below because there is nothing to compare against.**

**Actual candidate pool: the 57 `INCLUDE` verdicts from `260835-10`** (`SRC_Channel_Inventory.md`, current stamp), read in full — 44 from `EXT-2` (`@barelyprotestant5365`, his own channel) and 13 from `EXT-3` (`@StFrancisAnglicanSpartanburg`, the parish channel). I did not re-open the 9 `UNCERTAIN` or 8 `EXCLUDE-*` rows from that pass; they are out of scope for a download batch by their own verdict.

## 3. Task 1 — Dedupe against covered material

The `260835-10` close-out states every one of its 74 target rows was blank before verdicting, which rules out the row itself already carrying an `INGESTED` decision cell. That is **not** the same check as *content*-level duplication against material registered under a different File whose video-ID match was never written into the inventory — which is exactly the gap the brief's Task 5 flagged around File 4. I checked for that directly, cross-referencing `SRC_Manifest.md`'s own File-registration tables (titles, dates, byte ranges, session labels) against all 57 `INCLUDE` titles/dates, not just File 4's.

**Result: 11 of the 13 `EXT-3` candidates are duplicates or near-duplicates of already-registered, already-mined material. Only 2 of 13 are clean.** The `EXT-2` set (44 candidates) came back clean — see §3.4.

### 3.1 The File-4 case itself — 3 confirmed duplicates

`SRC_Manifest.md`'s File 4 registration (`a302-Revelation-June-July-2026.md`) gives **exact per-session byte ranges and titles** for Sessions IX, X and XI, fully mined (`RV-1…RV-23`, "contiguous, no gaps"). Matching those titles/dates against the channel inventory:

| Video ID | Title | Verdict |
|---|---|---|
| `nOSaF0BWS2Y` | Session IX: the Beast and the Bottomless Pit | **DROP** — File 4, Session IX (bytes 125–29,423), fully mined |
| `ADQnOyBaSRk` | Session X: the Woman, the Child, and the Dragon | **DROP** — File 4, Session X (bytes 29,512–60,374), fully mined |
| `M71-SrYEoEQ` | Session XI: the Two Beasts and the Mark | **DROP** — File 4, Session XI (bytes 60,455–94,822), fully mined. `SRC_Manifest.md` names this video ID **explicitly** as the duplicate of a304's re-supply of this exact range: *"Disposition: ⛔ DUPLICATE. Do not register, do not ingest, do not tag."* |

### 3.2 Beyond File 4 — the same problem recurs at Files 11 and 12

The channel's own session numbering ("Session XV," "Session XVI") doesn't match Files 11/12's internal numbering ("Session XIV," "Session XV"), which is exactly why `260835-10` (and the Step-5b tally before it) left the video-match blank rather than force it. Blank video-match is not the same as blank *content* coverage — checking File 11/12's registered content against the channel titles closes that gap:

| Video ID | Title | Verdict |
|---|---|---|
| `nGfY6_P5m5o` | Session XV (channel numbering): The Whore and the Beast (Ch 17-18) | **DROP** — content-matches File 11 (`a306`), fully mined `RV-33…RV-43` |
| `lJo0WgP37rs` | Session XVI (channel numbering): The Marriage Supper of the Lamb (Ch 19) | **PARTIAL — do not treat as a clean fresh pull.** Content-matches File 12 (`a307`), mined as `RV-44…RV-52`. But `St_Francis_EMC_Distinctives.md` records File 12 as a **truncated capture** — *"the capture truncates mid-clause and JD's own viewing of the video confirms it cuts off before the session's natural end… NOTHING IN RV-44…RV-52 COVERS 'THE WHOLE OF WHAT HE SAID ABOUT REVELATION 19.'"* A re-pull of this video would not be fresh territory, but it could close a **known, named gap** (the missing tail of Session XVI/Session XV-per-File-12) if that's a priority JD wants addressed. Flagged as an option, not included in the main ranked list below. |

### 3.3 The Anglican Class (Articles of Religion) series — 5 more confirmed, 1 already-possessed-but-unread, 1 genuinely open

All 7 `EXT-3` "Anglican Class, Session I–VII" candidates are livestream titles for **2026 Articles-of-Religion classes**. I checked these against the `A101` in-person session registry (a different registry section from the Revelation-class one) rather than assuming no connection, because the topic, weekly cadence, and upload-lag pattern all matched. Five resolved by direct content/title cross-check:

| Video ID | Title | Class date match | Verdict |
|---|---|---|---|
| `pHqKPBpQR7c` | Session I: Introduction | `A101-2026-06-14-P1` | **Already downloaded & registered** (260807-1), but only swept for one finding (`IP-12`); the manifest itself says whether it holds more was "NOT established." This is a *"go read what you already have"* task, not a fresh download — excluded from the ranked list below, flagged separately. |
| `zXxQwz9s0Ps` | Session II: History | `A101-2026-06-28` | **DROP** — this is literally `A101-20260628-official-video.md`, already ingested, `IP-40…IP-44` |
| `5amf7UHdeLI` | Session III: Articles I-VIII | `A101-2026-07-19` | **DROP** — confirmed by `SRC_Manifest.md`'s own text, `IP-13…IP-23` |
| `hxkQxBSCpNc` | Session IV: Articles IX-XVI | `A101-2026-07-26` | **DROP** — confirmed (content matches Articles XIII-XVI etc.), `IP-24…IP-39` |
| `VjK_jbfao-k` | Session VI: Articles of Religion | `A101-2026-08-16` | **DROP** — already ingested 260829-3, `IP-70…IP-83` |
| `2jHkSh1ieTo` | Session VII: Articles of Religion | `A101-2026-08-23` | **DROP** — the registered filename is literally `Anglican-SessionVII-ArticlesOfReligion-sentences.json`; already ingested 260833-3, `IP-84…IP-97`, and is the *sole* witness for Articles XXXVI-XXXIX |
| `6Z68nITG1Is` | Session V: Articles of Religion | `A101-2026-08-09` | **GENUINELY OPEN.** The manifest's own session table flags this exact stream row as *"POSSIBLE FUTURE CAPTURE — FLAGGED ONLY. NOT PULLED, and its existence is not established… do not read this row as a known source."* It has since been uploaded and is in this candidate pool. The room capture (`[R]`) for 08-09 is fully mined (`IP-45…IP-68`, 25 findings) but **every finding from that session carries an open, undischarged ear-verification flag** and the room file is itself "trimmed-but-name-inherited" (not the as-recorded original). Pulling this stream would give the corpus a second, independent rendering — the same method that discharged ear-verification flags at 07-19 and 07-26 — and is real, useful, not-yet-existing work. **Kept in the ranked list.** |

Net: of 13 `EXT-3` `INCLUDE` candidates, **11 are already covered** (9 clean drops, 1 partial-coverage special case, 1 already-possessed-but-unread), and **2 are genuinely open** (`GeWfXTAjFDo`, never registered anywhere; `6Z68nITG1Is`, flagged-but-never-pulled).

### 3.4 The `EXT-2` set (44 candidates) — checked, clean

Files 1-26 predate video IDs entirely (in-person audio never uploaded, per `SRC_Channel_Inventory.md`'s own Step-5b tally) so they cannot silently duplicate a channel video. Files 27-46 are matched by exact video-ID equality, and the inventory table is one row per video ID — any of my 44 candidates that already had a File match would show `INGESTED`, not `INCLUDE`, by construction. I additionally checked the three multi-speaker debate titles in this set against each other and against the corpus's known duplicate-event pairs (`x0hfBI6w6f0`/`MLCh-d15F_o`, the Apostolicae Curae debate; `7_egBtP9H1I`, the Holy-Orders-within-Anglicanism debate) — `auiLAv8BYpk` ("Debate on the Papacy: Scripture and the Seven Ecumenical Councils," 2020-06-02) is a different topic and a different date from both; no collision found. **No drops from this set.**

## 4. Task 2 — Ranking against the standing questions

Weighted per JD's standing instruction: Eucharist/eucharistic reasoning ranked above other categories, since it feeds the incense funnel (showbread, Oblation, type/antitype). Ranked against `DQ-24` (the five-level ordering and what counts as received), `OQ20`/`OQ21`, the element/circumstance distinction, burden-of-proof material, eucharistic presence/sacrifice, formulary/authority questions, and assurance/soteriology.

Reference point pulled from the corpus itself: `DQ-24` is the live five-level authority ordering (Scripture → Tradition → jurisdiction/gathered Bishops → Bishop Ordinary → Rector) plus the sharpest-yet burden rule ("the onus is upon the innovator who insists"), anchored at §13/§9 Eucharist-Sacrifice and cross-referenced to `OQ20`/`OQ21`. Material that bears on *what determines whether a ceremonial practice continues*, on *sacramental validity/form*, or on *eucharistic presence and sacrifice* ranks highest; material that's Anglican-identity/Rome-positioning but doesn't touch those levers ranks lower; short reaction clips and pure-history content rank lowest regardless of subject match.

## 5. Task 3 — Prerequisite flags (no assumed solo)

Flagged with a stated basis in every case, per the standing caution (`GV-50`, `GV-51`, `a105`).

- **Confirmed multi-voice by title:** `auiLAv8BYpk` ("Deacon James **and** Noah Edmonds"), `MLvweRO41bo` ("A Talk **with** Austin from Gospel Simplicity"), `gDcmyvbuA1Y` (close-out's own reasoning calls it "an interview").
- **Confirmed multi-voice by corpus registration:** `6Z68nITG1Is` — this is the stream twin of `A101-2026-08-09`, which the manifest states outright is *"Multi-voice; diarization is navigation only; the word-level splice check FAILED its own calibration."*
- **Named-other-teacher, speaker not established — treat as guest content until diarized, on the Kennedy/`GV-2-6` precedent:** `8nRhmD4w-Wg` and `9Fezj9WMh3A` ("**Fr. Ray** Teaching About…") — the title names a different clergyman as the teacher. Nothing here establishes whether Rev. James's own voice appears at all (intro/host) or not. Do not attribute any content from these to Rev. James without diarization or an equivalent warrant.
- **Solo-dominant with real Q&A, sparse/unreliable diarization — apply the File-4/10/11/12 rule, not the solo assumption:** `GeWfXTAjFDo` (Revelation Class). The established pattern for this whole class series is `>>` markers "sparse and unreliable... long stretches of RJ's teaching carry no marker at all, and several parishioner questions are marked only on the reply" — any transcription pass must attribute by content-in-context, not by marker, exactly as prior sessions in this series required.
- **Solo, no stated basis found for multi-voice (titles/format checked, nothing found):** `Nxx1QEhvIB0`, `p-jeXC7sokY`, `9SMGzwSsMSI`, `hDRmWM5Nkgw`, `UmIAkdRtzhw`, `s2-jIFFBiJg`, `xcNz2wdI2P8`, `M7iSL5mznTk`, `DavM_5hcN0w`, `wvpJL0DzBto`, `KsLqJIPrpCg`, `sO-_EJbq_oQ`, `imipCdI7B9s`, `gA-ELOCiwC8`, `xySXFYRQ9tI`. These are apologetics/teaching-format titles matching the channel's large solo-video pattern, with no guest named and no debate/interview framing — but "no stated basis found" is not the same claim as "confirmed solo," and each should get the same content-attribution caution on first listen that any new source gets.
- **Solo primary with liturgical call-and-response possible:** `IGNmKMXhL1Q` (Morning Prayer with a Homily) — he is the officiant; congregational responses may be present in the audio but this is not a guest-speaker scenario.

## 6. Task 4 — The ranked batch (22 videos)

All durations from `channel_videos.tsv` via `SRC_Channel_Inventory.md`. Channel: `EXT-2` = his own channel (`@barelyprotestant5365`); `EXT-3` = the parish channel.

### Tier 1 — Eucharist / incense-funnel core (highest priority)

| Video ID | Title | Uploaded | Duration | Channel | Rationale | Prerequisite |
|---|---|---|---|---|---|---|
| `Nxx1QEhvIB0` | Teaching the Mass | 2025-09-22 | 94:45 | EXT-2 | Direct, extended (95-min) Eucharist/Mass teaching — the single most on-point title in the whole pool for eucharistic presence/sacrifice and the incense funnel | Solo, no basis found for multi-voice |
| `p-jeXC7sokY` | What Makes a Sacrament Valid? | 2025-10-17 | 11:29 | EXT-2 | Sacramental validity/form goes directly to the element/circumstance distinction underlying `DQ-24`'s ceremonial-continuation question | Solo, no basis found |
| `9SMGzwSsMSI` | Anglican 101 Session 2: Our Confessional Standards | 2021-07-05 | 38:45 | EXT-2 | "Confessional standards" is exactly `DQ-24`'s Scripture/Tradition/jurisdiction ordering territory — formulary/authority core material | Solo, no basis found |
| `auiLAv8BYpk` | Debate on the Papacy: Scripture and the Seven Ecumenical Councils (Deacon James and Noah Edmonds) | 2020-06-02 | 76:07 | EXT-2 | Long-form debate; burden-of-proof and authority reasoning tend to surface explicitly in debate format, on-point for the formulary/authority and burden-of-proof standing questions | **Multi-voice, confirmed by title** |

### Tier 2 — Formulary/authority + ceremonial-warrant (incense-funnel adjacent)

| Video ID | Title | Uploaded | Duration | Channel | Rationale | Prerequisite |
|---|---|---|---|---|---|---|
| `UmIAkdRtzhw` | Are Icons Idolatrous? | 2020-07-03 | 14:35 | EXT-2 | Ceremonial/image-warrant reasoning — same family of argument as the incense funnel (what worship practices are warranted and how) | Solo, no basis found |
| `s2-jIFFBiJg` | What About the Apocrypha? (Anglican Perspectives) | 2020-05-22 | 29:50 | EXT-2 | Canon/formulary question, directly Anglican-confessional-identity | Solo, no basis found |
| `xcNz2wdI2P8` | Stations of the Cross (St. Augustine's Prayer Book) | 2020-03-27 | 25:43 | EXT-2 | Ceremonial devotional practice — element/circumstance and ceremonial-warrant adjacent | Solo, no basis found (liturgical reading) |
| `MLvweRO41bo` | A Talk with Austin from Gospel Simplicity | 2021-03-03 | 42:35 | EXT-2 | Cross-tradition (RC/Anglican/EO) liturgical discussion in his own voice — comparative formulary/authority value | **Multi-voice, confirmed by title** |
| `DavM_5hcN0w` | Response to Pastor Mike Winger's Video Against Infant Baptism | 2020-07-19 | 88:29 | EXT-2 | Long-form sacramental theology; "what counts as received" burden-of-proof reasoning shows up regularly in this format elsewhere in the corpus | Solo, no basis found (response-video format) |

### Tier 3 — Eucharist-adjacent guest teaching (comparative value, caution flagged)

| Video ID | Title | Uploaded | Duration | Channel | Rationale | Prerequisite |
|---|---|---|---|---|---|---|
| `8nRhmD4w-Wg` | Fr. Ray Teaching About the Eucharist | 2017-07-06 | 42:04 | EXT-2 | On-topic by title, but the named teacher is not Rev. James — comparative/background value only until attribution is established | **Named other teacher — do not attribute to Rev. James without diarization** |
| `9Fezj9WMh3A` | Fr. Ray Teaching About the Other Sacraments | 2017-07-14 | 35:48 | EXT-2 | Same as above, broader sacramental scope | **Named other teacher — same flag** |
| `M7iSL5mznTk` | A Liturgy for Spiritual Communion (Traditional) | 2020-03-20 | 3:14 | EXT-2 | Eucharist-adjacent liturgical text, short but on-topic | Solo, no basis found |

### Tier 4 — Authority/Rome-positioning, moderate depth

| Video ID | Title | Uploaded | Duration | Channel | Rationale | Prerequisite |
|---|---|---|---|---|---|---|
| `wvpJL0DzBto` | Bad Arguments for Roman Catholicism | 2021-01-24 | 26:06 | EXT-2 | Rome-positioning/authority | Solo, no basis found |
| `KsLqJIPrpCg` | Response to "Why is Anglicanism a Gateway to (Roman) Catholicism?" | 2020-04-30 | 56:29 | EXT-2 | Long-form Rome/authority positioning | Solo, no basis found |
| `sO-_EJbq_oQ` | Thoughts on the Papacy Debate with Noah Edmonds | 2020-06-04 | 9:53 | EXT-2 | His own follow-up reflection on the `auiLAv8BYpk` debate above — distinct content, not a duplicate of it | Solo, no basis found |
| `imipCdI7B9s` | Advice for Switching Traditions/Denominations | 2021-01-13 | 17:49 | EXT-2 | Confessional-identity advice | Solo, no basis found |
| `gA-ELOCiwC8` | Fundamentalist Claims Coronavirus is Because We Celebrate Easter? | 2020-04-09 | 28:52 | EXT-2 | Defense of a liturgical-calendar practice — element/circumstance adjacent | Solo, no basis found |

### Tier 5 — Worship/liturgy practice (lower doctrinal density, real coverage value)

| Video ID | Title | Uploaded | Duration | Channel | Rationale | Prerequisite |
|---|---|---|---|---|---|---|
| `IGNmKMXhL1Q` | Morning Prayer, 5th Sunday in Lent (with a Homily) | 2020-03-29 | 25:56 | EXT-2 | Office + homily (teaching component); worship/liturgy | Solo primary; liturgical responses possible |
| `xySXFYRQ9tI` | How to Use the Book of Common Prayer for Morning Prayer | 2020-03-28 | 29:13 | EXT-2 | Practical formulary use, lower argumentative density | Solo, no basis found |
| `hDRmWM5Nkgw` | Anglican 101, Session 1: Our History | 2021-06-15 | 55:43 | EXT-2 | Background/context for the confessional-standards material in Tier 1 | Solo, no basis found |

### Tier 6 — Fresh/unregistered territory outside the Eucharist weighting

| Video ID | Title | Uploaded | Duration | Channel | Rationale | Prerequisite |
|---|---|---|---|---|---|---|
| `GeWfXTAjFDo` | Revelation Class, Session XVII: The Millennial Reign, Pt 1 (Ch 20) | 2026-08-17 | 31:22 | EXT-3 | Genuinely unregistered — no File covers Session XVII; the only clean "fresh Revelation" candidate in the pool | Solo-dominant with parishioner Q&A; sparse/unreliable diarization per the established File 4/10/11/12 pattern |
| `6Z68nITG1Is` | Anglican Class, Session V: Articles of Religion | 2026-08-10 | 97:38 | EXT-3 | Not-yet-pulled stream twin of `A101-2026-08-09`; would supply a second independent rendering to help discharge that session's 25 open ear-verification flags | **Multi-voice, confirmed by corpus's own registration of the parent session** |

## 7. Task 5 — File-4-shaped gap, explicit answer

Yes, and it is larger than File 4 alone. §3.1-3.3 above cover it in full: **File 4 itself accounts for 3 of the 13 `EXT-3` candidates** (Sessions IX, X, XI — all duplicates), and the *same shape of gap* — a video whose content is already transcribed and mined under a registered File, but whose video-ID match was never written into `SRC_Channel_Inventory.md` because the session numbering conflicts — recurs **twice more**: Files 11/12 (2 candidates) and the whole `A101` Articles-of-Religion series (6 of 7 candidates). None of these are flagged as `INGESTED` in the inventory, so a pass that trusted the inventory's decision column alone would have downloaded 9 already-fully-mined videos and one already-registered-but-unread one as if they were fresh. Only `GeWfXTAjFDo` and `6Z68nITG1Is` are genuinely outside any registered File's territory.

## 8. Decision-cell update — not done, flagged for JD's call

The brief asked me to flag rather than act if the list were clean enough to write directly as `SRC_Channel_Inventory.md` decision-cell updates (e.g. "queued for Batch 9"). **I'm not doing that unilaterally, and I don't think a plain "queued" tag would be accurate here even if I had approval to write it** — 11 of the 13 `EXT-3` `INCLUDE` rows are not just "not this batch," they're topically-correct-but-duplicate, which is a different fact than the inventory currently records for them (they still read plain `INCLUDE`, no duplicate note). If you want, I can prepare a **separate, explicitly-scoped follow-up pass** that adds dated notes beside those 11 rows recording the File/session they duplicate (never overwriting the `INCLUDE` verdict itself, per the never-alter convention) — that seems like the more useful and more accurate action than a blanket "queued for Batch 9" tag on the clean rows. Say the word and I'll scope it properly rather than doing it inline here.

## 9. Close

- `git --no-optional-locks status --short` after writing this artifact: only this new untracked file under `passes/`. No tracked file touched.
- Validator: **does not need re-running.** Nothing in the corpus changed.
