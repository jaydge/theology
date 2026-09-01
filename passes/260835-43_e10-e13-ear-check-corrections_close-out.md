# 260835-43 — E10–E13 ear-check resolution: dated corrections to 260835-42

**Pass stamp:** `260835-43` · **Date:** 2026-08-31 · **Venue:** Cowork, `~/EMC` attached
**Deliverables:** `passes/260835-43_e10-e13-ear-check-corrections.diff` + this close-out. ⛔ **NOTHING COMMITTED.**

---

## 1. Gate — every figure re-derived, none taken from the brief

| Check | Result |
|---|---|
| HEAD | `5743f1cd52af7233ce27d45153b5bd0ae17198d1` — *"handoff info"*, 2026-08-31T15:22:58-04:00. ✅ **Matches the HEAD the brief named, exactly.** Branch `main`. |
| `git --no-optional-locks status --short` | **EMPTY**, captured directly before the first edit, exit 0. No lock created, none removed, no `rm` attempted. |
| Validator BEFORE | **`82 ok · 11 warnings · 0 errors`** |
| `PROJECT_STATE.md` stamp at gate | `260835-42` |
| Pass stamp | **`260835-43`** |

⭐⭐ **THE BRIEF INSTRUCTED THAT ITS OWN FIGURES BE RE-DERIVED RATHER THAN TRUSTED, AND THEY WERE. `260835-42`'s AFTER figures ARE CONFIRMED — the brief's caution was warranted procedurally but the numbers held.**

**All eleven warning codes at gate:** `[C1]` `src/SRC_Discord_RPW.md` 2 relative timestamps outside message headers · `[C3]` `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` no parseable stamp · `[C3]` `tools/transcribe_yt.py` no parseable stamp · `[C4]` `St_Francis_EMC_Distinctives.md` 2 stale answered-question passages · `[C5]` `RJ_Final_Question_List.md` 17 volatile-state assertions · `[C5]` `RJ_Incense_Analysis.md` 9 · `[C5]` `St_Francis_EMC_Distinctives.md` 7 · `[C10]` §15 17 behind the `IP` head · `[C10]` §15 21 behind the `LS` head · `[C11]` outline 1 `DQ` unreviewed · `[C11]` outline 17 `IP` unreviewed.

⚠️ **THE BRIEF CITES `82 ok · 11 warnings · 0 errors` AND SO DOES THE GATE — but the count's SHAPE changed at `260835-42` and that is recorded here so it is not misread as drift: the standing figure was `9 warnings` from `260835-15` through `260835-41`. It became 11 because `260835-42`'s minting split `[C10]` and `[C11]` into per-ledger warnings (one `IP` + one `LS` for `C10`; one `DQ` + one `IP` for `C11`), not because two new defects appeared.** ⛔ **None of the eleven is this pass's business and none was touched.**

### Stamp derivation — hazard note read first, as required

`260835-12`/`260835-14` re-confirmed **REAL and CONSUMED** (commits `530d987`, `68bf1d8`); neither in play at this end of the range. A distinct-stamp sweep over tracked `*.md`/`*.py`/`*.txt` returns an unbroken run **`260835-1 … 260835-42`**, no gaps; `ls passes/` (version-sorted) tops out at `260835-42`; `git log --all` tops out at the `260835-42` commit `ac2167f`.

⚠️ **`260835-43` returns exactly THREE repo-wide hits. Every one was opened and read in context, and all three are `260835-42`'s own gate prose asserting its absence** (*"`260835-43` and above return zero"*) — in `PROJECT_STATE.md:7`, in `passes/260835-42_….diff:13`, and in `passes/260835-42_…_close-out.md:45`. **Checked, not assumed.**
⚠️ **`260835-99` re-checked in context and re-confirmed NOT a stamp** — the upper endpoint of an absence-assertion range in earlier close-out prose.
✅ **`260835-44` and above return ZERO. This pass is `260835-43`.**

### Substrate verification — done before any byte anchor was trusted

- `sha256(InPersonClass-20260830-sentences.json)` recomputed from disk = `808e209e4e75a3764ae29d9d73a1a4abbaacb6b1ef0dd8c7e0f1b8757d21624e` — **EXACT** match to the registered `File 85` row.
- Byte count **5,490,911** — **exact**.
- **5/5** of the `File 85` block's own logged byte anchors (`s2469`, `s2035`, `s993`, `s1545`, `s1178`) re-extracted at their recorded offsets; all five resolve to their quoted text at delta **`+0`**.

⛔ **No number of any prefix was consumed. Next free values re-derived and unchanged: `IP-126`, `File 86`, `LS-142`, `DQ-28`.**

---

## 2. Result per window

### ⛔ E10 — `[141:05]`–`[141:30]`: FALSIFIED, and the brief's premise about it is corrected

**JD's report:** the voice is **his own**; the subject is **an object someone was taking away** — not two people disputing identity. `s2120`–`s2123`, all label `B`, are therefore **one speaker, JD**, end to end.

⚠️⚠️ **THE BRIEF IS WRONG ON ONE POINT AND IT IS FLAGGED RATHER THAN SILENTLY RECONCILED (`ORCHESTRATION.md` §7).** The brief describes this as *"one of five independent markers for the two-label rejection."* ⛔ **It is not one of the five and never was.** The five markers are `s2469`/`s2465` · `s2035` · `s993` · `s1545` · the vocatives. This instance lives in the **separate within-turn-merging paragraph**, as one of **four** worked instances (`[90:51]`, `[62:30]`, `[141:11]`, `[145:03]`).

✅ **CONSEQUENCE — and it runs the brief's way, only more so.** The brief instructed that this not be read as weakening the broader rejection. Correct, **and by a wider margin than it supposed**: not one of the five markers is touched by JD's ear-check. ⭐⭐ **The rejection is in fact STRENGTHENED by this pass overall, because `E11` and `E12` together establish a NAMED third speaker actually present and actually speaking — precisely what markers 1-5 could only infer.**

⚠️ **WHAT IS GENUINELY WEAKENED, RECORDED HONESTLY RATHER THAN GLOSSED: the within-turn sub-claim's illustration set drops 4 → 3 and loses its strongest.** The block calls this instance *"two voices inside one turn on any reading"*; it now is not. The three survivors all rest on **register mismatch** — inference, not demonstration.
⛔⛔ **The BINDING rule — *a turn-level label is not a warrant in this file; only an individually-checked sentence is* — STANDS UNCHANGED**, because it rests as much on **label-level** merging, which `E12` now demonstrates positively with a named person.

### ✅ E11 — `[111:35]`–`[112:15]`: RESOLVED

**JD's report:** Luke was **present and speaking earlier, then left**. `s1544` *"I appreciate you staying after"*, `s1545` *"Luke's suggestion"*, `s1549` *"I'm gonna stay in a while"* are **all JD**, after his departure. **From `[112:15]` forward it is Rev. James and JD only.**

⭐ **Marker 4 resolves on its SECOND horn and SURVIVES.** It offered *"either Luke's turn is inside `B`, or `B` is crediting a speaker the transcript never separates."* JD selects the second — and `E12` independently proves Luke's own turns ARE in the file, inside label `A`.

⚠️ **The difficulty in one line:** `Luke` occurs as a **personal name exactly once** in 2,561 sentences (`s1545`) — **and it is someone else saying it**. The other four hits (`s1041`, `s1045`, `s1185`, `s2369`) are the Gospel. Luke never self-identifies, is never addressed by name, and is never separated by a label.

⛔⛔ **THE `E11` ROW'S OWN FINDING LIST IS WRONG, AND THE BRIEF'S IS RIGHT.** Re-derived independently this pass from the entries' own cited sentence IDs resolved against `-sentences.json`:

| Cell says | Actually cites | Verdict |
|---|---|---|
| `IP-117` | `[67:01]`, `[67:21]` | ⛔ 45 min before the range |
| `IP-121` | `s1615` `[116:00]` | ✅ correct |
| `IP-123` | `[9:06]`–`[11:51]` | ⛔ 100 min before the range |
| `IP-124` | `[19:08]`–`[28:49]` | ⛔ 84 min before the range |
| *(missing)* | **`IP-115`** `s1594` `[114:47]` | ✅ belongs |
| *(missing)* | **`IP-116`** `s1788` `[125:08]` | ✅ belongs |
| *(missing)* | **`IP-120`** `s1572` `[112:53]` | ✅ belongs |

**Corrected by dated note; the cell is not edited.**

⚠️ **The strengthening is PER-CITATION, not per-entry.** By cited sentence ID, `IP-120` and `IP-121` lie **wholly** inside the resolved stretch; `IP-115` also cites `s972` `[77:55]` and `s989` `[78:35]`, `IP-116` also cites `s1338` `[98:06]`. `E11` strengthens **four citations, not four entries.**

⛔⛔⛔ **LOAD-BEARING GUARD, RECORDED BECAUSE THIS IS EXACTLY WHERE A LATER PASS WILL OVER-READ: `E11` establishes the room's OCCUPANCY after `[112:15]`, NOT the RELIABILITY of its labels there.** Within-turn merging between the two principals remains fully live in that stretch — `s2403` at `[158:03]` is the standing counter-example, and it is inside it. **The sentence-granularity rule is not relaxed by this discharge.**

### ⛔⛔⛔ E12 — `[93:24]`–`[95:12]`: NOT A CONTRADICTION. A SPEAKER MISATTRIBUTION.

- ✅ **`s1267`** *"If I pray morning and evening prayer, I'll do it, um um—."* `[93:28]`–`[93:30]`, `@2,956,357–2,956,416` — **speaker is REV. JAMES, CONFIRMED.** *"I'll do it"* (burning incense) **confirmed accurate as transcribed; it survives the cutoff intact.**
  ⚠️⚠️ **The setting is EXPRESSLY UNCONFIRMED and recorded as JD's own stated guess, because he flagged it as such himself** — a liturgical-church context, possibly *"at home"*, offered as his interpretation, not as something he is certain he heard. ⛔ **Not promoted to a heard fact; nothing may be built on it.**
  ⏳ **Post-cutoff content after *"um um—"* REMAINS UNRECOVERED.**
- ⛔⛔⛔ **`s1293`** *"I don't practice that personally."* `[95:07]`–`[95:09]`, `@3,007,516–3,007,549`, **labelled `A`** — **NOT REV. JAMES. IT IS LUKE**, defending burning incense generally while stating he personally does not do it.

⭐⭐⭐ **THERE IS NO CONTRADICTION TO ADJUDICATE.** Two different people answering — Rev. James committing to the practice, Luke defending-but-not-practising — not one person saying two things 101 seconds apart. Of the `E12` row's three offered explanations, the **first** (*"one is mislabelled"*) is correct; the row is left standing.

⛔⛔ **REGISTERED AS AN INSTANCE OF THE EXISTING `TWO-LABEL, NOT CONFIRMED TWO-VOICE` CLASS — the class this file was given at `260835-42` — AND NOT AS A NEW CLASS, exactly as the brief directed.**
⭐⭐ **What IS new is its evidential status: this is that class's FIRST CONFIRMED, NAMED, EAR-VERIFIED instance anywhere in the corpus.** `File 49`, `File 63` and this file's own five markers all **inferred** a concealed speaker from content. This one has a name, a sentence, a byte range and a first-hand witness.

⏳⏳ **DOWNSTREAM: `[93:24]`–`[95:12]` is a MINIMUM THREE-SPEAKER WINDOW (Rev. James, JD, Luke).** Flagged for a future pass; ⛔ **this pass did not re-audit it and was scoped not to.**

✅✅ **BUT THE EXPOSURE IS MEASURED, SO THE FUTURE PASS INHERITS A NUMBER AND NOT A WORRY: ZERO of the 58 distinct sentence IDs cited across `IP-109`…`IP-125` falls inside the window.** Nearest before: `s1256` (`IP-112`, `[92:56]`), **28 s clear**. Nearest after: `s1338` (`IP-116`, `[98:06]`), **2m54s clear**. ⛔ **The misattribution has NO LIVE VICTIM among the seventeen minted findings.**

⚠️ **What is NOT clean, named so it is not mistaken for a clean result:** the `B`-labelled run immediately preceding — `s1289` *"So you would say then it's appropriate to burn incense physically with prayers?"* `[94:58]` through `s1292` `[95:06]` — reads as the other side of the exchange `s1293` answers, and its speaker (JD or Luke) is **not established**. Nor is `s1294` *"I can't find—."* `[95:10]`, label `A`, which may be Luke continuing or Rev. James resuming. **Neither resolved here.**

### ⛔⛔ E12-adjacent — `[95:37]`: the non-mint decision is REVERSED on its stated ground

`s1301`, **speaker `A`**, `[95:37]`–`[95:40]`, `@3,025,603–3,025,656`: *"Then I would be on the side of you must burn incense."*

**JD's report: stated FLATLY. Not hypothetical.** ⭐⭐⭐ **That removes the exact ground `260835-42` gave for declining it** — *"a CONDITIONAL, spoken inside a hypothetical."* If flat, it is a **position statement**, bearing directly on the allowed-versus-demanded question `IP-118`, `IP-12`, `DQ-19`(c) and `DQ-27` all turn on, and which is the live Discord thread.

⛔⛔⛔ **NOT MINTED HERE, deliberately — the phrasing-and-framing judgment was outside this brief.** ⏳⏳ **Flagged as a live candidate for the next content-minting pass, adjacent to the `E12` resolution.**
✅ **Companion dated note placed beside the original at `St_Francis_EMC_Distinctives.md`, `IP-118` `[Analysis]`; that text is not edited.**

⛔⛔⛔ **ONE PREREQUISITE THIS PASS RAISES AND CANNOT SETTLE, AND THE MINTING PASS MUST CLEAR IT FIRST: `s1301`'s SPEAKER IS NOT INDEPENDENTLY ESTABLISHED.** JD's report settles the **manner**, not the **speaker** — and label `A` is now known to contain **Luke** thirty seconds earlier at `s1293`. `s1301` sits **outside** the `[93:24]`–`[95:12]` window, but that boundary was drawn by the `E12` row, not by a voice check, and **adjacency is not a warrant** (`ORCHESTRATION.md` §7).

### ✅ E13 — `[17:54]` and `[158:03]`: resolved in OPPOSITE directions

- ✅ **`Mike` — REAL.** `s228`, speaker `A`, `[17:54]`–`[17:59]`, `@531,491–531,573`, conf **0.531**. An attendee who spoke; Rev. James was addressing him; **may have asked only one question the entire session**, which is why he leaves almost no lexical trace.
- ⛔⛔ **`Matt` — NOT REAL. A CONFIRMED ASR ERROR.** `s2403`, speaker `B`, `[158:03]`–`[158:23]`, `@5,217,540–5,217,817`, conf **0.838**. No one by that name present. ⛔ **A stronger and different disposition than the open/unconfirmed flag `260835-42` gave it — not left queued, not to be re-raised, closed as an error.**

⭐⭐⭐ **THE ASR'S CONFIDENCE ORDERING WAS EXACTLY BACKWARDS, AND THAT LESSON IS WORTH MORE THAN EITHER VOCATIVE.** The **0.531** vocative is real; the **0.838** vocative is fabricated. ⛔ **Word-level confidence is not evidence of a vocative's reality — here it ranked the true name BELOW the false one.** ⭐ **`260835-42`'s instinct was right for the wrong reason: it recorded `Mike` rather than suppressing it precisely because suppressing a marker to keep a tidy count is the error the check exists to prevent — and `Mike` is the one that was real.** ⚠️ **Distinct from the KEYTERM-PROMPT CONTAMINATION class also registered on this file: that one manufactures a name the prompt supplied; this one mis-ranks names the prompt did not.**

✅✅✅ **CONFIRMED ROOM-OCCUPANT FLOOR RISES THREE → FOUR, ALL NAMED: Rev. James, JD, Luke, Mike.** ⭐⭐ **This cashes out the block's own claim that *"at least two further participants speak and are collapsed into"* the two labels — those two are Luke (`E11`/`E12`) and Mike (`E13`), now established rather than inferred.**

⚠️ **Marker 5 is split and the rejection is unaffected, stated explicitly the way `260835-42` handled its own weak marker:** stronger half (`Matt`) falsified, weaker half (`Mike`) confirmed. ⛔ **`260835-42` expressly recorded marker 5 as non-load-bearing — *"markers 1-4 carry the finding without it"* — and expressly declined to rely on `Mike`.**

⏳⏳ **A THIRD NAME IN MARKER 5 IS NOT COVERED BY `E13` AS BRIEFED AND IS NOT CLOSED BY SILENCE: `Chrissy`** (`s2506`, speaker `B`, `[163:42]`–`[163:45]`, `@5,406,587–5,406,635`) — *"Chrissy, she's got all kinds of literary niches."* Grammatically ambiguous between a fronted vocative and a fronted third-person referent. **The floor of four is a floor, not a count.**

⚠️ **`s2403`'s own speaker is now MORE questionable, not less.** With the vocative gone it is a label-`B` sentence in **teaching register** at `[158:03]` — **inside** the stretch `E11` establishes as JD-and-Rev.-James-only. A within-turn merge candidate **between the two principals**, and the standing counter-example to reading `E11` as licence to trust labels after `[112:15]`. **Flag only; nothing rests on it.**

---

## 3. Divergences between the brief and the repo — reported, not silently reconciled

1. ⛔ **`E10` is not one of the five markers.** The brief says it is. It is one of four within-turn instances. **The repo wins.** (Substance unaffected — the brief's instruction runs the same way, only more strongly.)
2. ✅ **The brief's `E11` finding list is RIGHT and the repo's is WRONG.** Brief: `IP-115`/`IP-116`/`IP-120`/`IP-121`. Manifest cell: `IP-117`/`IP-121`/`IP-123`/`IP-124`. **Independently re-derived here, without reference to either, from the entries' own cited sentence IDs — the brief's list is confirmed exactly.** ⭐ **The rarer direction: this is the brief correcting the repo.**
3. ⚠️ **`s1293`'s timestamp.** The `E12` row gives `[95:09]`; the sentence's own `start` is `[95:07]` (its `end` is `[95:09]`). Recorded, row not edited.
4. ⚠️ **The brief's Deliverables list names only `SRC_Manifest.md`, but its own `E12`-adjacent item (a) requires correcting the `[95:37]` note — which lives in `St_Francis_EMC_Distinctives.md`, not the manifest.** Both were done; the wider file touch is flagged here rather than assumed.
5. ⚠️ **The brief's `82 ok · 11 warnings` figure is confirmed, but the count's shape changed at `260835-42`** (9 → 11 by `[C10]`/`[C11]` splitting per-ledger, not by new defects). Recorded so it is not later read as drift.

---

## 4. What changed — file by file

**`SRC_Manifest.md`** — header stamp `260835-42` → `260835-43` (prior text retained verbatim); new `260835-43` changelog entry above `260835-42`'s; **one consolidated dated correction note** after the `E10`–`E13` table covering all five items; **two short pointer notes** placed *beside* the originals they correct — one after the within-turn paragraph (`E10`), one after marker 5 (`E13`).

**`St_Francis_EMC_Distinctives.md`** — header stamp bumped (prior text retained); new changelog entry; **one dated note** after `IP-118`'s `[Analysis]` recording the `[95:37]` reversal, the non-mint's status, and the speaker prerequisite.

**`PROJECT_STATE.md`** — header stamp bumped; **`GATE (260835-43)` block + `PASS NOTE 260835-43`** inserted above `260835-42`'s; **three §4 registry rows** re-stamped to `260835-43` with prior cell text retained (`PROJECT_STATE.md`, `St_Francis_EMC_Distinctives.md`, `SRC_Manifest.md`) — the `260835-*` self-referential-registry-row failure mode (`ORCHESTRATION.md` §7) addressed deliberately, not incidentally.

---

## 5. Never-alter compliance — verified mechanically, not asserted

`git diff -U0` yields **131 insertions, 6 deletions**. **Every one of the six deleted lines was checked programmatically:**

- **5 of 6** are stamp lines and registry-row cells whose **entire prior text is carried forward verbatim** inside their replacement (*"Prior stamp text retained"* / *"Prior row text retained below"*) — verified by substring containment, not by eye.
- **1 of 6** is `PROJECT_STATE.md`'s own `**Last updated:**` line, a **pure `260835-42` → `260835-43` stamp bump with no summary text to retain** — the standing convention for that line, whose summary lives in the gate/pass note.

⛔ **No original text was altered, trimmed, reworded, deleted, renumbered or re-pointed. No finding, row, hash, byte range, offset or date cell was changed.**

---

## 6. Validator — full accounting

| | Result |
|---|---|
| **BEFORE** | `82 ok · 11 warnings · 0 errors` |
| **AFTER** | `82 ok · 11 warnings · 0 errors` |
| **AFTER, on a fresh clone of `5743f1c` with the diff applied** | `82 ok · 11 warnings · 0 errors` |

✅ **IDENTICAL, and not merely equal in total: all eleven codes are the same eleven, with the same counts, on the same files.** No regression, no new warning, no code cleared.
✅ **`[C3]` version-drift errors deliberately avoided:** all three files whose header stamps were bumped had their `PROJECT_STATE.md` §4 registry rows bumped in the same pass. `C3` raises an **error**, not a warning, on drift — this was checked in `validate_project.py` before the stamps were touched, not after.

**Diff verification:** `git apply --check` on a **fresh clone of the exact briefed HEAD** passes; the diff then **applies cleanly** and the applied clone validates identically. ⭐ Ten trailing-whitespace warnings from blockquote separators were found in the first cut and **normalised to the file's own `>` convention** before the final diff was written; the re-check is clean.

---

## 7. Incense and icons — the standing high-priority report

⭐⭐⭐ **This pass is entirely incense material and the result is emphatically not a zero.** The `E12` reattribution, the `[95:37]` reversal and the `E11` stretch all sit inside the ~100-minute incense disputation. **The single most consequential item for the incense question is `[95:37]`/`s1301`** — a candidate position statement on allowed-versus-demanded, previously discarded as a conditional. ⛔ **Icons: zero, and not looked for — outside this brief's scope.**

---

## 8. What this pass deliberately did NOT do

⛔ Nothing minted; `[95:37]` **flagged only**. · ⛔ `[93:24]`–`[95:12]` **not re-audited** beyond the two sentences named. · ⛔ Discord thread **not recaptured or mined** (JD's own manual pull). · ⛔ `RJ_Incense_Analysis.md` §4.6/§4.8/§4.10 **not touched** (deferred, standing instruction). · ⛔ `Incense_Conversational_Outline.md`, `RJ_Final_Question_List.md`, `ORCHESTRATION.md`, `SRC_Channel_Inventory.md`, `SRC_Coverage_Register.md`, `validate_project.py` **not touched**. · ⛔ **Nothing drafted, altered or posted to Rev. James.** · ⛔ **NOTHING COMMITTED.**

⚠️ **`ORCHESTRATION.md` §8's dual coverage-registry rule was considered and deliberately NOT triggered: this is a correction pass over an already-registered source, not an intake or retro-registration. No new coverage state exists to record, and `SRC_Channel_Inventory.md`'s video-ID reconciliation has no key to run on (`File 85` is a room capture — recorded INAPPLICABLE at `260835-42`, unchanged).**

⏳ **OWED, FLAGGED, NOT DONE:** dated notes at `IP-115`/`IP-116`/`IP-120`/`IP-121` recording `E11`'s **partial** discharge of their `⏳ OPEN EAR FLAG`s (in-range citations only). Outside this brief's enumerated deliverables; left for a follow-up rather than taken unasked.

⚠️ **REPORTED, NOT ACTED ON:** two artifacts outside the row's registered five-artifact set sit in `original transcripts/in person classes/20260830/` — `Audio_08_30_2026_19_23_13.mp3.json` (11,320,539 B) and `Audio_08_30_2026_19_23_13.mp3.txt` (169,109 B), both mtime **2026-08-31 18:03**, i.e. **after** `HEAD`'s `5743f1c` (15:22). Neither registered, hashed, nor used. **Flagged for JD.**

---

## 9. Queue status after this pass

| Window | Status |
|---|---|
| `E10` | ✅ **CLOSED** — falsified as a two-voice instance |
| `E11` | ✅ **CLOSED** — Luke present then departed; `[112:15]`+ is two-person |
| `E12` | ✅ **CLOSED — as a SPEAKER MISATTRIBUTION, not as a contradiction** |
| `E13` | ✅ **CLOSED** — `Mike` real, `Matt` a confirmed ASR error |
| `E6`, `E7` | ⛔ **UNCHANGED, STILL BLOCKING** (`File 83`/`File 84`) — not this pass's business |
| `E9` | ⏳ **UNCHANGED** |

### Residual open threads

1. ⛔ **`s1267`'s post-cutoff content** (after *"um um—"*) — **unrecovered**, and not recoverable from this rendering.
2. ⛔ **The *"at home"* setting** for `s1267` — **JD's stated guess only; never independently confirmed.** Whether it is ever confirmed is open.
3. ⏳ **Whether `[95:37]`/`s1301` gets minted** — for the next content-minting pass. ⛔ **Its speaker must be confirmed first.**
4. ⏳ **The `[93:24]`–`[95:12]` three-speaker window's remaining content**, including `s1289`–`s1292` and `s1294`.
5. ⏳ **`Chrissy`** (`s2506`) — not covered by `E13` as briefed.
6. ⏳ **`s2403`'s speaker** — a teaching-register sentence on label `B` inside the two-person stretch.
7. ⏳ **`IP-115`/`IP-116`/`IP-120`/`IP-121` entry-level ear-flag notes** — owed, see §8.

---

## 10. Hand-off

⛔ **Nothing committed. JD applies, validates, commits and pushes from his own terminal.**

```
cd ~/EMC/theology
rm -f .git/index.lock
git add -A
git commit -m "260835-43: E10-E13 ear-check resolution — s1293 reattributed from Rev. James to Luke (no contradiction to adjudicate, a speaker misattribution; TWO-LABEL NOT CONFIRMED TWO-VOICE gets its first confirmed, named, ear-verified instance); E10 falsified as a two-voice instance and the brief's five-marker premise corrected, the two-label rejection untouched and strengthened; E11 resolved (Luke present then departed, [112:15]+ is Rev. James and JD only) with the row's own finding list corrected to IP-115/116/120/121 and an explicit guard that this is occupancy not label reliability; E13 resolved in opposite directions, Mike (0.531) real and Matt (0.838) a confirmed ASR error, the ASR's confidence ordering exactly backwards, confirmed room floor three to four all named; [95:37] non-mint decision reversed on its stated ground and flagged for the next minting pass, not minted, speaker confirmation set as a prerequisite; zero of 58 cited sentence IDs falls inside the three-speaker window so no live victim among IP-109..IP-125; dated notes only, no finding row hash byte range or offset altered, no number consumed, validator 82 ok / 11 warnings / 0 errors unchanged"
git push
```
