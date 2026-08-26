# 260834-8 — REV/RV YEAR RE-VERIFICATION AND FILES 8-9 VIDEO PROVENANCE

**Last updated: 260834-8.** ⛔⛔ **NOT AN INTAKE. NO SOURCE RE-MINED, NO FINDING MINTED, NO `Rev`/`RV`/`File`/`LS`/`IP`/`DQ` NUMBER CONSUMED.** This pass verifies a dating claim before acting on it, finds the correction it was asked to make already made (`260822-2`), and registers the per-session video provenance for Files 8-9 that `260822-2` did not have.

---

## ✅⚠️ GATE

| Check | Expected | Observed | Result |
|---|---|---|---|
| `git rev-parse HEAD` | `c0e7a36` or later, checked for Rev/RV-touching commits | `c0e7a36b59ba333179c8d4b14d737ee4155c315a` | ✅ **MATCH.** Commit message: "260834-6: eight-file triage (read-and-report)... nothing registered, no number consumed" — does NOT touch `Rev`/`RV` dating. |
| `git status --short` at gate | — | **NOT CLEAN.** `M ORCHESTRATION.md`, `M PROJECT_STATE.md`, `?? passes/260834-7_eight-file-coverage-check_read-and-report_close-out.md` | ⚠️ **Pre-existing, not created by this pass.** These three belong to an apparent prior, uncommitted `260834-7` pass on a DIFFERENT subject — coverage-checking `a101-1.txt`, `a101-2.md`, `a103.md`, `a105.md`, `a106.md`, `a201.txt`, `a202.txt`, `a301-Classical-Theism.md`. Confirmed by reading its close-out in full and grepping it for `a104`/`File 8`/`File 9`/`Revelation`: the only hit is one unrelated citation of `260813-1` as a renumbering precedent. **It does not touch this pass's subject and was left untouched.** |
| `.git/index.lock` | ⚠️ briefed as recurring | **PRESENT at gate**, zero-byte, `-rw-------`, matching the shape `260834-6`/`260834-7` both diagnosed (git creates it normally, the filesystem denies `unlink`). | ⚠️ **REPORTED, NOT WORKED AROUND.** No git write operation (`add`/`commit`/`rm`) was attempted against it. It is still present at close-out, unchanged, confirmed by `ls -la .git/index.lock` after all edits. **Whoever stages this pass should expect `git add`/`git commit` may need the filesystem-permission fix this is not this pass's place to apply.** |
| `validate_project.py` BEFORE | derive | `80 ok · 9 warnings · 0 errors` — identical 9 codes to `260834-6`'s and `260834-7`'s own BEFORE runs | ✅ recorded |
| `PROJECT_STATE.md` stamp | report | **`260834-5`** (created `260724-3`) | ✅ reported |
| Next-free pass stamp | derive | **`260834-8`** — `grep -rEho '26[0-9]{4}-[0-9]+'` across all `.md` files gives a highest existing stamp of `260834-7` (uncommitted); `260834-8` returns zero hits anywhere. | ✅ **DERIVED AND VERIFIED FREE** |

### Every firing code, BEFORE (9 warnings, 0 errors) — identical set across all three most recent passes

1. `WARN [C1]` `src/SRC_Discord_RPW.md`: 2 relative timestamp(s) outside message headers.
2. `WARN [C3]` `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md`: no parseable `'Last updated'` stamp.
3. `WARN [C3]` `tools/transcribe_yt.py`: no parseable `'Last updated'` stamp.
4. `WARN [C4]` `St_Francis_EMC_Distinctives.md`: 2 passage(s) describe an ANSWERED question as pending.
5. `WARN [C5]` `RJ_Final_Question_List.md`: 17 volatile-state assertions.
6. `WARN [C5]` `RJ_Incense_Analysis.md`: 9 volatile-state assertions.
7. `WARN [C5]` `St_Francis_EMC_Distinctives.md`: 7 volatile-state assertions.
8. `WARN [C10]` §15's newest LS citation is 8 findings behind the ledger.
9. `WARN [C11]` outline last checked against `DQ-19`; ledger now runs to `DQ-24`.

**AFTER this pass's edits: `80 ok · 9 warnings · 0 errors` — identical. No new firing code introduced.** (One transient `ERROR [C3] PROJECT_STATE.md: VERSION DRIFT` appeared mid-pass when `SRC_Manifest.md`/`SRC_Channel_Inventory.md`'s registry-table version cells were bumped before `PROJECT_STATE.md`'s own registry row for itself; corrected in the same pass by bumping that row too, and the re-run confirms `0 errors`.)

---

## 1. THE CLAIM, VERIFIED BEFORE ACTING ON IT

The brief: the manifest registers Files 8-9 as "the 2025 Revelation run," retro-registered at `260813-1`; JD states the run is 2026; establish this from evidence rather than adopting it on assertion.

**Finding, stated first because it changes the shape of the whole pass: the correction was already made, at `260822-2` (git commit `e3dd43a`), roughly three weeks before this pass ran.** `SRC_Manifest.md`'s section header (`### REVELATION CLASS, 2025 RUN`), its canonical-aliases heading, and every one of the eight `Rev2025-S*` rows already carry a `260822-2` dated correction beside the original text, per the never-alter rule, following the exact pattern `260804-1` set as precedent (a dated note appended beside a wrong original rather than a silent edit). `St_Francis_EMC_Distinctives.md`'s §18 heading carries the same correction. **This pass's job therefore became independent verification of an already-made correction, not making a new one** — the brief's own conditional ("if and only if the 2026 dating is established, correct it") is satisfied by confirming the existing correction is sound, not by writing a second one beside it.

### 1.1 The sources' own internal dating

`a104.md` (98,944 bytes) is the ONLY file with a first-person year statement. Located by byte offset with `grep -bo`:

> **@21,053-21,073**, verbatim: *"So, I'm here in AD 2026. Almost all of Revelation is uh future for me."*

Context (bytes 20,800-21,400): he is defining **futurism** as one of four approaches to Revelation's timeline and naming the present year to occupy a futurist's vantage point — the next sentence is *"That's the approach."* Illustrative, not autobiographical in intent, but it is still the only spoken year in either file.

**Every other date-shaped string in both files, checked exhaustively:**

| String | Location(s) | Reading |
|---|---|---|
| `"2025"` | `a104.md` @28, `a104-2.md` @29 — ONLY these two, both inside JD's own title line (*"St Francis Revelation Class 2025 chunk 1/2 of 2"*) | JD's filename label, not Rev. James's speech. Identical trap shape to `Misc-2025`/`a106`, independently documented by `260834-7`: the year lives inside a label string and is never asserted as fact by anyone speaking. |
| `AD 60`, `AD 70`, `AD 132-135`, `AD 66-7`, `AD 69/70` (5 more `AD \d` hits) | Both files, all inside the exposition of Revelation's OWN historical dating (when the book was written, when the temple fell) | Content about the 1st century, not about when the class is happening. None points the other way. |
| `1948` | `a104.md` @30,013, inside a discussion of the state of Israel | Topical reference (eschatological significance of 1948 Israel), not a class-dating marker. |
| `right now` / `as of` / `currently` / `these days` (26 hits total) | Scattered, both files | Sampled: all are argumentative ("right now" = "at this point in the argument") or idiomatic ("voice as of many waters" — quoting Revelation 1:15) or truly generic ("as of now don't know"). None is a calendar reference. |

**No internal date marker points toward 2025.** The single spoken year is 2026.

### 1.2 `SRC_Channel_Inventory.md`'s `EXT-3` rows

The entire Revelation series on `@StFrancisAnglicanSpartanburg` runs Session I (2026-03-27) through Session XVII (2026-08-17). **Zero 2025 Revelation-titled videos exist anywhere in the 62-row `EXT-3` inventory.** The nearest 2025 content is unrelated topical material (`hlEGpBC3Vj4`, "Sir Gawain and the Green Knight," 2025-12-31) with a clean gap before Session I begins. This is an **absence**, and per the brief it is reported as a finding: the channel that hosts every session of this teaching series has no candidate for a 2025 Revelation run at all.

### 1.3 The "genuine 2025 run, re-taught in 2026" alternative — tested, not dismissed

This is the reading that would make the current registration correct, so it was tested on its own terms rather than waved off.

**Against it:**
- The channel enumeration is not a single pass's finding — `SRC_Manifest.md` records it independently confirmed **three times** (`260813-1`, `260814-1`, `260822-2`), by different methods, all agreeing: no 2025 Revelation content exists on `EXT-3`.
- Session III's own opening line, while JD is preparing that specific session: *"I was planning on trying to go over uh chapters four and five for this week. I looked, you know, I took my first look at Revelation 4."* **"Took my first look" is preparation language for material he has not yet taught** — not what a re-teacher of a prior 2025 series would say about chapter 4 while prepping session 3.
- Every one of the nine matched `EXT-3` video durations agrees with the corresponding byte range in Files 8-9 to within rounding, at a consistent 13.0-14.2 bytes/sec throughout both files (computed per session: S1 14.17, S2 13.11, S3 13.31, S4-combined 13.37, S5 13.64, S6 13.67, S7 13.02, S8 12.95 bytes/sec). **A genuinely separate 2025 recording, later re-taught with different pacing, different asides (the printing/paper-and-ink aside at the start of Session VII, the "another action-packed chapter" callback at Session VIII) and different chapter-per-session boundaries, would not be expected to match a single 2026 channel's durations this tightly across eight independent sessions.**
- Four of the eight sessions explicitly self-announce their own sequential number in speech (*"session two"* @32,189; *"this is session three... the heav[enly liturgy]"* @60,047; *"this is class session four, the lamb"* @83,102; *"session five"* @10,463; *"This is session six"* @40,911) — a pattern of live, sequential numbering, not the pattern of an already-taught series being revisited.

**For it:** nothing found. No independent 2025 Revelation content, no verbal marker of repetition ("as I said last year," "when I taught this before"), no structural anomaly consistent with two parallel series.

**Verdict: strongly rejected.** The evidence does not merely fail to support a genuine 2025 run — it actively contradicts one, on four independent lines (channel absence confirmed three ways, first-look preparation language, tight duration/byte correspondence across all eight sessions, live sequential self-numbering).

---

## 2. `260822-2` EXAMINED DIRECTLY

Commit `e3dd43a`, "260822-2: correct Rev/RV dating error (Rev is 2026, not 2025); retract 2-run comparison framing; supersede 260822-1; register Session XV." Touched `PROJECT_STATE.md`, `SRC_Manifest.md`, `St_Francis_EMC_Distinctives.md` (122 insertions, 29 deletions).

**What it corrected:** the Source ID Legend `Rev` row; the §18 heading in `St_Francis_EMC_Distinctives.md`; the §12 "2026 counterpart" independence claim (one silence sampled twice, not two independent silences); the "registered 2025 run stops at Revelation 10" explanation (rewritten as a hand-off, not a stop); the `RV-28`/`Rev-11` pairing candidate (withdrawn); `SRC_Manifest.md`'s Note 3 inversion (there are not two sets of eight sessions, there is one, already ingested); the manifest's section header, canonical-aliases heading, and all eight `Rev2025-S*` rows' year field (each annotated `YEAR = 2026, ESTABLISHED 260822-2`); and `PROJECT_STATE.md` §7's open anomaly row (closed in favour of the AD-2026 reading).

**Whether it examined this question:** yes, as its entire subject — this was not incidental to `260822-2`, it was the whole pass.

**Whether it lacked the video IDs that would have let it catch this:** **yes, precisely.** Its stated warrant is *"JD's own direct search of the `EXT-3` channel"* — sufficient to establish that one continuous 2026 series exists (Sessions I-XV, oldest upload 4 months old, newest 6 hours old, at the time) and to fix the YEAR. **It explicitly did not fix the DATE**: every `Rev2025-S*` row's `Uploaded` cell still read *"— not established"* after `260822-2`, and its own §7 anomaly-closure note says *"the exact DATES remain NOT ESTABLISHED, and this pass adopted none."* A channel search sufficient to browse titles and confirm a year is not the same operation as matching nine specific video IDs to nine specific byte ranges — and that gap is exactly why the `Uploaded` cells stayed blank through `260826-2` as well, up to this pass.

---

## 3. FILES 8-9's PER-SESSION VIDEO PROVENANCE — REGISTERED

All nine `EXT-3` video IDs verified against session content before being recorded (not adopted from title text alone):

| Block | Session | Video ID | Uploaded | Duration | Content verification |
|---|---|---|---|---|---|
| `a104` block 1 | I: How We Approach This Book | `Ac3oAM2trBc` | 2026-03-27 | 2244 s = 37:24 exact | Futurism/AD-2026 passage; three millennial views |
| `a104` block 2 | II: Chapters 1-3 | `QqQHIrI7-6M` | 2026-04-02 | 2079 s = 34:39 exact | Self-announced "session two" @32,189; seven churches |
| `a104` block 3 | III: The Heavenly Liturgy | `FxbVzG0on5I` | 2026-04-16 | 1766 s = 29:26 exact | Self-announced "session three, the heav[enly liturgy]" @60,047 |
| `a104` block 4 (Pt 1) | IV: Lamb and Seals, Pt 1 | `RG4AP5vSKrY` | 2026-05-07 | 1221 s = 20:21 | Self-announced "class session four, the lamb" @83,102 |
| `a104-2` block 1 (Pt 2) | IV: Lamb and Seals, Pt 2 | `DACpGVyqqNE` | 2026-05-07 | 734 s = 12:14 exact | Continues Session IV across the file boundary (see §4) |
| `a104-2` block 2 | V: 144,000 & Great Multitude | `_8axw8Hog60` | 2026-05-07 | 2246 s = 37:26 exact | Self-announced "session five" @10,463 |
| `a104-2` block 3 | VI: First Four Trumpets | `ZbTi1klNlw8` | 2026-05-10 | 1981 s = 33:01 exact | Self-announced "session six" @40,911; **Malachi 1:11 quoted verbatim @46,952** |
| `a104-2` block 4 | VII: Fifth & Sixth Trumpets | `B7YgZ-o2WU0` | 2026-05-19 | 2054 s = 34:14 exact | Dismissal/greeting boundary at S6/S7 and S7/S8 (genuine session breaks, confirming sequence) |
| `a104-2` block 5 | VIII: Mighty Angel and Little Scroll | `6JRvrk-t3e0` | 2026-05-26 | 2195 s = 36:35 exact | Chapter-progression continuity from Session VII; "another action-packed chapter" opening |

⚠️ **One discrepancy from the brief, reported rather than silently reconciled: the brief describes "ten videos" needing decision cells. Only NINE distinct video IDs resolve to Files 8-9's eight session blocks** — Session IV alone carries two (Pt 1 + Pt 2), and no tenth candidate exists anywhere in `SRC_Channel_Inventory.md`'s `EXT-3` rows that maps to this material.

**Two flagged beyond bookkeeping, per the brief:**
- **`ZbTi1klNlw8`** (Session VI) carries the Malachi 1:11 quotation and 10 `altar` hits in-range — this is `Rev-9`'s row, "the strongest internal lever in the corpus" per §15.
- **`FxbVzG0on5I`** (Session III) sources `Rev-3` and part of `Rev-11` — `Rev-11` belongs to the same §15 "strongest internal lever" cluster (`Rev-8`/`9`/`10`/`11`). No separate pass names this specific video ID elsewhere in the corpus (checked by grep — this is its only occurrence outside this pass's own edits), so "independently flagged top-tier" is read here as referring to the corpus's own §15 characterization of the material this video sources, not a second document naming the ID directly.

**Registered in `SRC_Manifest.md`:** as dated `260834-8` annotations beside each existing row's "not established" `Uploaded` cell (never overwriting), plus a new consolidated provenance table. **Registered in `SRC_Channel_Inventory.md`:** all nine decision cells filled `INGESTED`, cross-referencing File and finding numbers already in `SRC_Manifest.md` — no new number minted.

**What the corrected/verified dating means, stated explicitly as the brief asked:** these nine sessions move from roughly a year's apparent distance (as the surviving "2025" label implied) into the live 2026 window — March 27 through May 26, 2026 — which places them weeks before `IP-12` (the 2026-06-14 in-person class, the corpus's first in-person session of 2026) and squarely inside the same active teaching period as the rest of the tracked `RV` series, not a prior year's closed episode.

---

## 4. THE EIGHT-SESSIONS/NINE-RANGES STRUCTURE — TESTED, NOT ASSUMED

The proposed resolution: Session IV existing as two separate `EXT-3` uploads (Pt 1 `RG4AP5vSKrY` 1221 s, Pt 2 `DACpGVyqqNE` 734 s) explains why Files 8-9 hold nine `==` blocks across eight sessions.

**Tested directly rather than assumed.** The `a104.md`/`a104-2.md` FILE boundary — which is also where the manifest's existing "Part 1"/"Part 2" byte ranges are split, of necessity, since that's the only available split point in block-delimited data — was checked against the two independently-confirmed GENUINE session boundaries inside the same files:

| Boundary | Content at the cut | Signature |
|---|---|---|
| S1/S2 (`a104.md` @31,850) | *"...thank you all very much."* → *"The Lord be with you. >> With your spirit. >> Let us pray..."* | ✅ Dismissal + greeting — a real video boundary |
| S2/S3 (`a104.md` @59,103) | *"...thank you all very much."* → *"Lord be with you. >> Your spirit. >> Let us pray..."* | ✅ Dismissal + greeting — a real video boundary |
| **`a104.md`/`a104-2.md` file boundary** (inside Session IV) | *"...still being committed"* → *"to the old covenant as a way to be saved..."* | ⛔ **Mid-sentence. No dismissal, no greeting, no `==` marker independent of the file's own start.** |

**Conclusion: the file boundary does NOT carry the signature of a real video cut, and is not shown to coincide with the true Pt 1/Pt 2 upload boundary.** The better-supported reading is that JD's "chunk 1 of 2"/"chunk 2 of 2" file split is a mechanical division of the WHOLE eight-session transcript (file-size handling), independent of session or video structure, that happens to fall inside Session IV. **Both videos are confirmed to jointly source Session IV's content; neither is confirmed to align with the file boundary specifically** — the manifest's existing Part 1/Part 2 byte ranges remain the best available proxy (they do correctly partition all of Session IV's content between the two videos, jointly) but should not be read as verified against the real Pt 1/Pt 2 cut point. Per the brief's own warning, coincidence was not asserted without evidence — and the evidence available argues against it.

---

## 5. SESSIONS XII AND XIV — ABSENCE VS. RENUMBERING

Both already established in existing corpus content (`SRC_Manifest.md`, `SRC_Channel_Inventory.md`); confirmed by re-reading rather than re-derived:

- **Session XII is genuinely absent.** All Revelation videos on `EXT-3` were enumerated three independent times (`260813-1`, `260814-1`, `260822-2`); no title names "Session XII," Revelation 14, or Revelation 16. Recorded as an observation only — cause unknown, not reconstructed, not inferred to mean the session was never held.
- **Session XIV is NOT absent — it is a renumbering artifact.** `SRC_Channel_Inventory.md` (line 27) already records: File 11 (`a306`, the corpus's own "Session XIV," Revelation 17-18 content) matches the channel's title-numbered **"Session XV"** (`nGfY6_P5m5o`); File 12 (`a307`, the corpus's own "Session XV," Revelation 19 content) matches the channel's **"Session XVI"** (`lJo0WgP37rs`). This is consistent with JD's report that Rev. James renamed later sessions, shifting the channel's own displayed numbering by one from some point after the XII gap onward. Both files are left blank rather than force-matched in the inventory, per the manifest's own repeated caution that this corpus's session numbers are not reliably self-consistent — unaffected by this pass, since Files 11/12 are outside Files 8-9's scope.

---

## 6. ONE UNCORRECTED DEPENDENT CELL FOUND, FLAGGED, NOT EDITED

`RJ_Incense_Analysis.md` (a backstage prep document, not `Incense_Conversational_Outline.md`) still carries the pre-`260822-2` dating uncorrected in two places:

- Its own source line (line 21): *"...the 2025 Revelation class (Rev-9/10/11)..."*
- §1 body text (line 141): *"The 2025 Revelation class moves this warrant from IP-paraphrase to flat, repeated, first-person statement..."*

Neither carries a `260822-2`-style dated note. **This is genuinely a "dependent cell" of the kind the brief asked to have travel with the correction — but it sits outside this pass's explicitly named scope** (`SRC_Manifest.md` / `St_Francis_EMC_Distinctives.md` / `SRC_Channel_Inventory.md`), and touching a Rev.-James-adjacent backstage document unbidden was judged the riskier default against the brief's own "do not draft, alter, or post anything to Rev. James" boundary, even though this file is backstage rather than RJ-facing. **Flagged here rather than edited — an item for JD to rule on, on the `260804-1`/`260822-2` dated-note pattern, in a future pass scoped to include it.**

---

## 7. WHAT MOVED AND WHAT DID NOT

**Touched:** `SRC_Manifest.md` (nine dated `260834-8` annotations on the eight `Rev2025-S*` rows plus one combined-Session-IV annotation, one new provenance table, one new changelog entry, header stamp bump), `SRC_Channel_Inventory.md` (nine decision cells filled, header stamp bump), `PROJECT_STATE.md` (gate + pass note, two registry rows bumped — including its own, corrected after the validator caught the omission), plus this new `passes/` artifact.

**Not touched:** `St_Francis_EMC_Distinctives.md` (already correctly annotated at `260822-2`/`260826-2`; nothing here required a further note), `RJ_Incense_Analysis.md` (flagged, not edited — §6 above), `Incense_Conversational_Outline.md`, `RJ_Final_Question_List.md`, `RJ_Open_Questions_and_Divergences.md`, `On_Incense_and_the_Altar.md`, `ORCHESTRATION.md` and the pre-existing `260834-7` artifacts (not this pass's subject, left exactly as found).

**Nothing moved:** no `Rev`, `RV`, `File`, `LS`, `IP`, or `DQ` number consumed; no existing finding's content, quote, or byte offset altered; `Rev` stays closed; nothing drafted, altered, or posted to Rev. James; the `260822-2` correction was verified, not redone; `260834-7`'s uncommitted, unrelated work was left exactly as found.

*(§5 rule 11 — this note makes no claim about its own commit state.)*
