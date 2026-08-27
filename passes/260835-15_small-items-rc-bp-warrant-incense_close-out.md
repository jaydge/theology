# 260835-15 — Small-items pass: RC/BP corrections, warrant scoping, GV-12, incense-section flag

**Pass type:** dated-note corrections and flags only. ⛔⛔ **NOTHING MINTED. NO EXISTING FINDING TEXT ALTERED. NO SOURCE RE-MINED.**

---

## Gate

| Item | Value |
|---|---|
| HEAD at start | `68bf1d8917a5760d2dc393365aaa0f9844f570e7`, branch `main` |
| `git --no-optional-locks status --short` before first edit | **EMPTY** — captured directly |
| Validator BEFORE | **`82 ok · 9 warnings · 0 errors`** |
| `PROJECT_STATE.md` stamp at gate | **`260835-12`** (own header/pass-note text) |
| Next-free pass stamp | **`260835-15`** — see anomaly note below |
| Validator AFTER | **`82 ok · 9 warnings · 0 errors`** — identical codes, no regression |

**Stamp-derivation anomaly, flagged not fixed.** `PROJECT_STATE.md`'s own header and its `260835-12`-labelled pass note both describe the diarization-verification pass's content, but the actual committed artifacts for that work are filed as `260835-14` (`passes/260835-14_diarization-verification-a101-room-and-batch9_*`, and the HEAD commit's own message: `260835-14: diarization verification…`). This is a **pre-existing, already self-reported collision** — `260835-13`'s own commit message says *"stamp collision with the in-flight diarization pass's `260835-12` filenames flagged for that pass's commit."* The internal pass-note text was never retroactively relabelled when the commit was renumbered. A naive repo-wide content-grep for the stamp pattern tops out at `260835-13` (every higher apparent hit is a next-free assertion); the committed filenames and git log carry a real `260835-14`. Taking the more authoritative source (committed filenames/commit messages over uncorrected internal prose), the highest real stamp is `260835-14` and **this pass is `260835-15`**. Not this pass's business to repair — flagged in the new `PROJECT_STATE.md` gate block.

---

## Item 1 — RC3-20 (§ St_Francis_EMC_Distinctives.md)

`RC3-20` ("prays the 1928 commemoration of the departed") was already reported `NOT FOUND` by `260835-11`/Flag B1 (18 search terms, 0 hits, both `File 49` renderings). This pass:

1. Added a dated note at Flag B1 confirming the status flag it left "owed" is now applied.
2. Added a dated note at the **Known Gap 10** entry itself (§3, item 10), formally marking `RC3-20` **UNVERIFIED — not located at source**, not deleted, and flagging that Known Gap 10's guard — which cites `RC3-20` as a settled affirmative datum preventing *"we don't do prayers for the dead"* from being flattened onto him — rests on this unverified citation.
3. **Distinguished carefully:** the guard's *practical conclusion* (that sentence is the objector's, not his) is **independently safe** — `260821-1`'s direct audio verification confirmed it by diarization label, not by coherence with `RC3-20`. What's flagged is only the *original coherence-based reasoning* that also cited `RC3-20`.

No number consumed. No finding altered.

## Item 2 — Ordination-date contradiction (mislabeled "RC1-10" in the brief)

**Label flag:** the brief's tag `RC1-10` is wrong. `RC1-10` is exclusively the Homilies-disagreement finding (Flag B2, unrelated). The actual ordination-date contradiction is tagged `RC3-3`/`RC3-7` (Flag A1). Flagged rather than silently substituted, then investigated as A1 per the substance of the request.

**Cross-referenced against the corpus's own `CL-9` chain** (built independently across BLOG/LS/POD intakes, not just the RC section's own looser L363 timeline): `POD-4` (deacon ordination planned 2019-11-10), `BLOG-15` (Deacon by 2019-12-21), `LS-118` (2020-03-08, still deacon, expects priesting May 2020), `File 55` (2020-03-28, "a deacon as I am"), `File 50`/`RC-4` (2020-05-22, still not a priest), `GV-49`/`GV-50` (2020, expecting priesting that summer), `LS-31` (2021-05-22, ACNA→REC move), File 15 (2021-08-05, priest under Sutton).

**Candidate resolution offered, not adopted:** every 2020 source has him still a deacon through May, and `GV-49`/`GV-50` already expect priesting that summer — consistent with `RC3-3`/`RC3-7`'s own 2025 claim ("newly ordained [priest] in 2020"), reading `L429`'s "deacon-era" heading as a period label rather than a literal rank-at-that-moment claim.

**Genuine ambiguity flagged, not resolved:** `L363`/`CL-9`'s "priesting 2021-2023" bracket is built from indirect signals (self-styling "Father" by 2023; first attestation as priest *under Sutton in the REC*, which could postdate an earlier ACNA ordination given the move is characterised elsewhere as "jurisdictional-geographic"). Two live readings recorded; neither adopted, per instruction not to resolve unilaterally.

## Item 3 — RC3-22 / RC1-15 attribution layer

Both already had `260835-11` flags (C1, C2) marking a read-aloud attribution problem, with a note "OWED." This pass applied the three-layer split at each finding's own location, following the corpus's existing `BLOG-3`/`POD-3` read-aloud convention:

- **`RC3-22`** (§9): "represent" / "the occasion of its continuing benefits" reassigned `[Stated — MASSEY SHEPHERD'S WORDS, read aloud by RJ...]`; his own non-propitiatory phrases remain `[Stated, RC3-22]` and Q4a's reweight is unaffected.
- **`RC1-15`** (§5/§7): "a reformation martyr" reassigned `[Stated — TURNER'S ARTICLE, read aloud by RJ...]`, with his own non-objection recharacterized as `[Stated-Analysis]` (an inference of rough agreement, not a direct assertion). His own sola fide / anti-Dort statements remain `[Stated, RC1-15]`.

Both original tags left untouched (never-alter); both `260835-11` "OWED" flags marked applied.

## Item 4 — GV-12

Read `260835-5`'s and `260835-6`'s search logs first (both tried `ryle`/`Ryle`/`bishop ryle`/`low church wing`, both against `a201.txt` and `a202.txt`, both 0 useful hits). Per the `GV-55` precedent (found via "liturgical East" rather than "eastward"), tried the claimed content's *other* terms instead: `succession`, `catholicity`. Found in `a201.txt` recording 2 (same recording as `GV-10`/`GV-11`) at **@41,431-41,708**:

> *"this is not a sort of like hardcore uh **rile bishop rile** uh reformed position of this so it is more sympathetic towards things like **episode succession** and the **catholicity** — emphasizing the catholicity of anglicanism..."*

The ASR renders "Ryle" as "rile" (doubled: "rile bishop rile") and "episcopal" as "episode" — neither prior search term could have found it. Dated note added beside the existing table row and the `260835-6`/`260835-7` "unresolved" paragraph, on the exact `GV-55` pattern (verdict not edited, superseded in practice).

## Item 5 — Warrant scope ⭐

**Ruling delivered:** the single-speaker human-verification warrant (`SRC_Manifest.md`) narrows to **six files** — `File 47`, `48`, `50`, `51`, `54`, `55`. `File 49`/`TeachingTheMass` is excluded, on its own attendee-turn evidence (`260835-11`, including the file's own final line, *"Thanks, Frank."*).

**New warrant class established** at `ORCHESTRATION.md` §8: **SINGLE-LABEL, NOT CONFIRMED SINGLE-VOICE** — for any file where automatic diarization returns one label but internal content (participant address, call-response, closing address to someone else) suggests uncaptured additional speakers. Usable only where the specific cited range has been checked against a located attendee-turn list and doesn't intersect it; never as a blanket warrant. Named instances: `File 49` (this pass) and `File 63`/`GeWfXTAjFDo` (already flagged the same way at `260835-12`, now given the formal class name). Flagged explicitly for use "wherever this pattern recurs," per instruction.

Neither the warrant's own original text nor any `RC3` finding was altered — dated rulings added beside both.

## Item 6 — RJ_Incense_Analysis.md §4.6/§4.8/§4.10

Each section gets a dated note at its top: **falsified-pending-revision.** The note states (1) the "unknown, and diagnostic" premise their lead lever rests on (§7) is falsified by `260835-1`/`IP-98` (Malachi 1:11's "pure offering" = Christ, a third fork); (2) the reformulated seam proposed at `260835-2` (`Incense_Conversational_Outline.md` Step 4) has not survived its own counter-objection ("not offering him afresh" denies re-immolation, not enactment — so both clauses may be equally enacted and the seam's asymmetry may not exist); (3) revision is deferred to a separate, scoped pass. **Flag only — no rewrite attempted**, per instruction. This discharges the "reported elsewhere, left standing" status carried since `260835-1`/`260835-2`/`260835-3`, all three of which explicitly declined to touch these sections.

`Incense_Conversational_Outline.md` was **read only** (to quote the Step 4 counter-objection verbatim) — **not touched**, per instruction and per its own standing protection.

One validator side-effect caught and fixed before close: the file's "blank lines" are conventionally `\n \n` (a lone space), not `\n\n`; my first draft of the three notes introduced true `\n\n` breaks that shifted a C4 windowing heuristic elsewhere in the document, producing two false-positive WARNs. Fixed by matching the file's own blank-line convention; validator returned to baseline.

---

## What was NOT touched

`Incense_Conversational_Outline.md`, `RJ_Final_Question_List.md`, `RJ_Open_Questions_and_Divergences.md`, `On_Incense_and_the_Altar.md`, `SRC_Coverage_Register.md`, `SRC_Channel_Inventory.md`, `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md`, `validate_project.py`, `CLAUDE.md`, `Project_Bootstrap_Prompt.md`, `README.md`, all `src/` archives. **Nothing drafted, altered, or posted to Rev. James.**

## Files touched (5, plus this pass's own two `passes/` artifacts)

`PROJECT_STATE.md`, `St_Francis_EMC_Distinctives.md`, `SRC_Manifest.md`, `ORCHESTRATION.md`, `RJ_Incense_Analysis.md` — each version-bumped to `260835-15` in both its own header and the `PROJECT_STATE.md` §4 registry row, keeping C3 clean.

## Validator

**BEFORE:** `82 ok · 9 warnings · 0 errors`. **AFTER:** `82 ok · 9 warnings · 0 errors` — identical 9 codes, no regression, no improvement claimed beyond what the items themselves state.

## git status after edits, before this artifact was written

```
 M ORCHESTRATION.md
 M PROJECT_STATE.md
 M RJ_Incense_Analysis.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
```

Diff at `passes/260835-15_small-items-rc-bp-warrant-incense.diff` (233 lines). **Nothing committed by this pass** — commit is JD's own action.
