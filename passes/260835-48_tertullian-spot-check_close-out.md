# Close-out — `260835-48`: Tertullian spot-check

## Gate

- **HEAD confirmed:** `c33bd5b` ("260835-46: DQ-28 minted"), matching the brief's
  last-known value. **`260835-47`'s artifacts were NOT yet committed at gate** —
  `PROJECT_STATE.md` and `SRC_Manifest.md` carried its uncommitted edits, and
  `Patristic_Citations_Incense_Verification.md`, `passes/260835-47_patristic-
  verification.diff` and its close-out sat untracked. The brief anticipated either
  state ("may be committed by the time this runs"); reported as found, not assumed.
- **Validator baseline, fresh:** `86 ok · 11 warnings · 0 errors`, run before any
  edit this pass made. (Committed baseline at `c33bd5b` was `84 ok`; the 2-point gap
  is `260835-47`'s own still-uncommitted addition, not this pass's.)
- **Next-free pass stamp: `260835-48`**, derived by grep per the `260835-12`/
  `260835-14` stamp-derivation hazard (a predecessor pass's forward absence-
  assertion is a content hit, not a consumption — read before deriving). Repo-wide
  grep for `260835-48` returned exactly two hits, both `260835-46`/`260835-47`'s own
  forward absence-assertions ("`260835-48` and above return ZERO"), not
  consumptions. `git log --all` tops out at `260835-46` (`c33bd5b`); the passes/
  directory's numeric-sorted run is unbroken `260835-1…47`. **`260835-48` confirmed
  FREE and taken by this pass.**
- **Web access:** confirmed working before research began (test fetch of
  `newadvent.org/fathers/0304.htm` succeeded).
- **Ledger number consumed: NONE.** This is verification only, exactly as briefed.

## What was done

All five tasks in the brief were completed; see `Tertullian_Incense_Passages.md`
(new file, `src/`-adjacent, registered in `SRC_Manifest.md` §External Primary Texts
and in `PROJECT_STATE.md` §4) for the full analysis. Summary:

1. **`De Corona` 11** confirmed as the correct chapter for the soldier/incense line.
   Register independently re-derived (not merely copied from `260835-47`) as
   PRUDENTIAL, with the reasoning spelled out in the file's §2.
2. **`De Corona` 10** reported in full: Tertullian burns frankincense domestically
   himself, explicitly distinguished from idol-ceremony. Reported as counter-
   evidence, plainly, not softened.
3. **`Apology` 30** given the explicit verdict `260835-47` didn't record: SAFE TO
   DEPLOY WITH CAVEAT, theological register, contrast class is pagan state
   sacrifice, not Christian liturgical incense.
4. **`Apology` 42** confirmed as counter-evidence in the sentence immediately
   following the quotable-sounding opening clause; the funerary/cultic distinction
   is real but says nothing about a third category (Christian liturgical use).
5. **Three further works swept.** `De Idololatria` produced three hits (chs. 2, 9,
   11) — ch. 11 is, in this pass's judgment, the single most systematic Tertullian
   statement on this question found by either pass: one sentence forbidding the
   incense-seller's trade while explicitly permitting medicinal and funerary use.
   `Ad Scapulam` (5 chapters) and `De Oratione` (29 chapters) were read in full and
   returned **zero** occurrences of incense/frankincense — reported as negative
   findings per the brief's own instruction not to skip a passage because it cuts
   against the argument (in this case, cuts against there being more material to
   find at all).

## Sourcing

The four passages carried over from `260835-47`'s scope (*De Corona* 10 & 11,
*Apology* 30 & 42) were **double-attested** against New Advent and CCEL, word-for-
word identical on both, including CCEL's original ANF editorial footnotes (two of
which independently corroborate readings reached here). `tertullian.org`'s ANF
mirror was tried again on a different URL pattern (`anf/anf03/anf03-10.htm`) than
`260835-47` used and again returned an **empty body** — the same defect, a third
data point. CCEL served as the fallback second host, as `260835-47` established.

**The three new `De Idololatria` passages were NOT double-attested** — single-
sourced at New Advent only, for time. This is flagged in the deliverable file
itself (§0 and §5c) and is owed work before any outward deployment, on the same
standard `260835-47` set for its own Tertullian corrections.

## Declined / not done, and why

- **Did not double-attest `De Idololatria`.** Explained above; a real gap, not an
  oversight glossed over.
- **Did not sweep the rest of the Tertullian corpus** beyond the three works named
  in the brief (*De Idololatria*, *Ad Scapulam*, *De Oratione*). *De Spectaculis*,
  *Ad Nationes*, and everything else Tertullian wrote were not touched, and no claim
  is made about them.
- **Did not re-verify Barnabas, Justin, or Athenagoras** — explicitly out of scope
  per the brief.
- **Did not capture any source page to `src/`.** All primary texts were read live
  over the web. Nothing produced by this pass is hash-verifiable against a local
  copy; the `260835-44`/`260835-47` capture-before-outward-quotation flag is
  unchanged and still owed, and now additionally covers this file.
- **Did not touch `Patristic_Citations_Incense_Verification.md`, any corpus
  finding, Discord draft, or strategy document** — per the brief's explicit
  non-scope.

## An unbriefed fix this pass had to make

Adding the new document and bumping `SRC_Manifest.md`'s own top-of-file stamp to
`260835-48` put that stamp out of sync with `PROJECT_STATE.md` §4's registry cell
for `SRC_Manifest.md`, which still read `260835-47`. The validator's `[C3]` check
caught this immediately as `VERSION DRIFT` (one error, where the brief expected
zero). **This was not a pre-existing defect** — it is the direct, mechanical
consequence of this pass's own edit to `SRC_Manifest.md`'s stamp, and `CLAUDE.md`'s
own close-out checklist requires the document stamp and the registry cell to be
bumped together in the same pass. Fixed by updating that one registry cell (and
adding a `§4` registry row for the new `Tertullian_Incense_Passages.md` file itself,
matching the row `260835-47` created for its own document) — both changes are
included in this pass's diff and are within its stated scope (registering the new
document), not a scope expansion.

## Validator, before and after

| | ok | warnings | errors |
|---|---|---|---|
| Baseline (fresh, `260835-47` uncommitted, before this pass) | 86 | 11 | 0 |
| After this pass's edits, before the `[C3]` fix above | 85 | 11 | **1** |
| **Final** | **88** | **11** | **0** |

Matches the brief's expectation exactly: **ok +2** (one new passing `[C3]`, one new
passing `[C8]`, both `Tertullian_Incense_Passages.md`), **warning set unchanged**
(diffed line-for-line against the baseline, identical), **zero errors** at the
final state. The one error that appeared mid-pass was diagnosed and fixed, not
worked around; reported here rather than silently corrected and left unmentioned.

## Files touched

- **New:** `Tertullian_Incense_Passages.md` (22,726 B, 353 lines, `sha256` =
  `19f2b9444380f0f99bcf7914a3d0037d039c4d42c7699e3bd48360c141527863`).
- **Edited:** `SRC_Manifest.md` (new dated note under §External Primary Texts; new
  top-of-file changelog entry).
- **Edited:** `PROJECT_STATE.md` (new §4 registry row for the new document; the
  `SRC_Manifest.md` registry-cell fix described above).

The accompanying `.diff` isolates exactly these three files' changes **as made by
this pass alone** — `SRC_Manifest.md` and `PROJECT_STATE.md` both carried
`260835-47`'s own uncommitted edits before this pass started, so a plain `git diff`
against `HEAD` would have mixed the two passes' changes together under one stamp.
The diff was produced by reconstructing each file's pre-`260835-48` state (reversing
this pass's edits specifically, verified byte-exact by round-trip patching before
being trusted) and diffing against that, rather than against `HEAD`.

## Commit status

**Not committed.** Per brief: diff and close-out written to `passes/` only. The
"Artifacts first" / "Corpus edits after orchestration review" commit sequence in
the brief was read as sequencing guidance for whenever commits happen, not as an
instruction for this session to run `git commit`/`git push` itself — nothing in this
pass's own scope section authorized that, and "⛔ Does not commit" is stated
plainly under "What this pass does NOT do." `git status` at close is: three new/
modified files from this pass, layered on top of `260835-47`'s own still-uncommitted
state from before this pass began.
