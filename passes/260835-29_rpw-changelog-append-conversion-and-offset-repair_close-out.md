# 260835-29 — `src/SRC_Discord_RPW.md`'s changelog converted prepended → appended, and every logged offset into it repaired

## 1. Gate — every value derived, not assumed

✅ **GATE.** HEAD `ce55b00d33807a51a650f9f07f06a8ea45d76df6` — matches the briefed `ce55b00` exactly; branch `main`. `git --no-optional-locks status --short` returned **EMPTY** before this pass's first edit, captured directly and not reconstructed; every git read used `git --no-optional-locks`.

**Validator BEFORE:** `81 ok · 10 warnings · 0 errors`, all ten codes reproduced verbatim: `[C1]` `src/SRC_Discord_RPW.md` 2 relative timestamps outside message headers; `[C3]` `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` no parseable stamp; `[C3]` `tools/transcribe_yt.py` no parseable stamp; `[C4]` `St_Francis_EMC_Distinctives.md` 2 stale answered-question passages; `[C5]` `RJ_Final_Question_List.md` 17 volatile-state assertions; `[C5]` `RJ_Incense_Analysis.md` 9; `[C5]` `St_Francis_EMC_Distinctives.md` 7; `[C10]` §15's newest `LS` citation 9 behind the ledger head (`LS-120` vs `LS-129`); `[C11]` `DQ` arm — outline last checked against `DQ-24`, ledger at `DQ-26`, 2 unreviewed; `[C11]` `IP` arm — outline last checked against `IP-97`, ledger at `IP-108`, 11 unreviewed. `PROJECT_STATE.md`'s own stamp at gate: `260835-28`.

**Stamp derivation — hazard note read first.** `passes/260835-28_..._close-out.md` §7 was read in full before anything else, as required, and its findings were treated as established rather than re-derived. The `260835-12`/`260835-14` hazard note (recorded `260835-22`) was also read first: it warns that a naive content-grep misleads in both directions on this range — `260835-12` reads as available inside prose asserting its absence but is REAL and CONSUMED (commit `530d987`); `260835-14` exists only as committed filenames and a commit message but is likewise REAL and CONSUMED (commit `68bf1d8`). Both treated as consumed.

**Derivation used:** a distinct-stamp sweep over tracked `*.md`/`*.py`/`*.txt` returns an unbroken run `260835-1 … 260835-28` with no gaps; `ls passes/` independently tops out at `260835-28`; `git log --all` tops out at commit `ce55b00` ("260835-28: ..."). The one apparent higher hit, `260835-99`, was read in context and confirmed to be the upper endpoint of an absence-assertion range inside earlier close-out prose, not a real stamp. `260835-29` returns zero matches repo-wide, zero in `passes/`, zero in `git log --all`. **This pass is `260835-29`.**

## 2. The problem, as `260835-28` §7 established it (not re-derived)

`src/SRC_Discord_RPW.md` carried a **prepended** changelog while every citation into it is an **absolute byte offset from byte 0**. Every changelog entry therefore silently displaced every previously-logged body offset. `260835-28` found: `DQ-25`'s five ranges displaced `+6,466` by that pass's own entry (corrected values recorded in a dated note, originals untouched); `DQ-24`'s four ranges already broken at `HEAD`, landing roughly `+14,100` bytes off in unrelated text, with two tangled causes (structural displacement, and independent imprecision at the minting commit `24a0a50` itself — only (c) matched its quote start exactly; (a) off by −52, (b) by −53, (d) by +253).

**JD's ruling:** convert the archive's changelog to append. Chosen over an anchor-relative offset scheme because appending removes the failure mode structurally, whereas an anchor-relative convention would depend on every future pass remembering it and a silent violation would reproduce the hazard.

## 3. Task 1 — the changelog relocated, verbatim, in order

The `## Changelog` header and every entry (unaltered, unreworded, unrenumbered, unreordered) moved from immediately after the file's title to immediately after the full message body, at EOF. This is a **pure rearrangement**: the same 43,676-byte changelog block plus the 6-byte separator run that used to sit between the changelog and the `**Thread:**` header now sits between the body and the relocated changelog instead.

**Verified, not assumed:**
- Total file length: **81,551 bytes before and after** — unchanged.
- Line count: **434 before and after** — unchanged.
- SHA-256: `38fb5727424d8dac47007df89a620b0132bd33835a0401d6b2a6236c63fae2c2` → `3be72b043830b196a3ba0fd74edf34cd8b32867c5e9e4f41e8349e38c2b8955f`.
- Uniform shift for every offset that pointed into the body/Thread-header region: **`-43,682` bytes**, derived as (old `**Thread:**` marker position) − (title length), and cross-checked as (relocated changelog length 43,676) + (separator run 6) = 43,682.

## 4. Task 2 — every citation into this file found, recomputed and verified

Searched the whole findings corpus (`St_Francis_EMC_Distinctives.md`, `RJ_Incense_Analysis.md`, `RJ_Final_Question_List.md`, `SRC_Manifest.md`) for byte-offset citations pointing into `src/SRC_Discord_RPW.md`. **Only `DQ-24`, `DQ-25` and `DQ-26` carry byte-offset citations into this file** — `DQ-1`…`DQ-23` and every finding sourced from the other four `SRC_Discord_*.md` archives cite by message timestamp, not byte offset.

**`DQ-25` — a gap found in `260835-28`'s own correction, not assumed complete.** That pass's shift note covered only the reply's five ranges (a)-(c). Checked directly: the entry's own two intro citations (JD's posted questions, the entry's opening two `[byte @…]` marks) were **not** covered, even though they sit in the same entry, the same file, and are displaced by the identical mechanism. Confirmed broken at `HEAD` before this pass's move, confirmed to resolve correctly at the same `+6,466` displacement `260835-28` found for (a)-(c) — proving the same cause — and now carried forward through this pass's `-43,682` relocation shift and recorded as a dated note alongside the five ranges `260835-28` already corrected.

**`DQ-26`'s nine citations** were minted fresh at `HEAD` `ce55b00` and needed no pre-move correction (no later changelog entry had yet displaced them) — only this pass's own relocation shift.

All twenty citations (4 for `DQ-24`, 7 for `DQ-25`, 9 for `DQ-26`) were recomputed and verified by **direct byte extraction against the file on disk, post-relocation**, exact match start-to-end (not a prefix check). Full post-move values are recorded as dated notes beside each entry in `St_Francis_EMC_Distinctives.md`. No original offset was rewritten anywhere — every correction is a dated note beside the original, per never-alter.

## 5. Task 3 — `DQ-24`'s two tangled causes, recorded separately

Re-verified independently (not merely quoted from `260835-28`): checked out `src/SRC_Discord_RPW.md` at its minting commit `24a0a50` and located each of the four quotes directly. Confirmed exactly what `260835-28` §7 reported: **(c)** matched its quote's start exactly (diff 0); **(a)** was off by −52; **(b)** was off by −53; **(d)** was off by +253 (landing entirely in JD's preceding question, not RJ's reply).

Because a shift correction applied to an already-wrong offset stays wrong, `DQ-24`'s four ranges were **not** repaired by the uniform `-43,682` shift. Instead each was recomputed by locating its exact quoted text in the current `HEAD` file (verified unique, single occurrence each) and then carrying that HEAD-correct value through the relocation shift. Both causes — structural displacement (now moot, since no future changelog entry can displace anything again) and minting-time imprecision (independent of relocation, fixed only by re-deriving from the quote) — are recorded separately in the dated note, per the brief's explicit instruction not to conflate them.

**`DQ-24` corrected, post-relocation:** (a) `@28,812–29,132` · (b) `@27,895–28,139` · (c) `@28,294–28,809` · (d) `@27,617–27,892`. A secondary inline position-check inside (b) (the "must"-italics verification, already discharged by `260834-4`'s screenshot) shared its value with (b)'s old upper bound and is noted to move identically, to `@28,139`.

## 6. Task 4 — the convention written into the repo

`SRC_Manifest.md`'s `src/SRC_Discord_RPW.md` row gains a new `Changelog position` field: **APPENDED, NOT PREPENDED**, stated as a binding handling rule (not a one-time note), with the reason (offset stability) and the consequence of violating it (every offset logged against the file would be silently invalidated again) spelled out. `PROJECT_STATE.md` §7's defect row is not deleted — a dated `RESOLVED 260835-29` note is added beside it, per never-alter.

**Other archives checked, per the brief's explicit instruction not to assume the check is unnecessary:** all four other `SRC_Discord_*.md` files (`Assurance`, `39ArticlesFormularies`, `BaptismConfirmation`, `SevenSacraments`) also carry a **prepended** changelog — same shape. Searched the whole corpus for byte-offset citations into any of the four: **none exist.** Every finding sourced from those threads (and `DQ-1`…`DQ-23` from this one) cites by message timestamp. **Reported, not fixed, per the brief:** the same structural hazard is latent in those four files but has no live victim today, since nothing points an absolute byte offset into any of them.

## 7. Task 5 — verification sample

Six citations sampled across all three findings, re-extracted from the file on disk post-relocation (SHA-256 `3be72b04…`) and confirmed to resolve exactly to their quoted text:

| Finding | Post-move range | Resolves |
|---|---|---|
| `DQ-24`(a) | `@28,812–29,132` | ✅ "In direct answer to what you're really looking for…5) The Rector" |
| `DQ-24`(d) | `@27,617–27,892` | ✅ "The continuation of the practices that we have received…" |
| `DQ-25` intro 1 | `@30,030–30,252` | ✅ "I wasn't asking for an exact timeframe…" |
| `DQ-25`(c) | `@31,131–31,332` | ✅ "So the introduction of liturgical dancing…" |
| `DQ-26`(a) | `@36,356–36,399` | ✅ "It involves both transmission and duration." |
| `DQ-26`(e)/(f) | `@36,912–37,058` | ✅ "Something like the Te Deum Laudamus…" |

All twenty citations (not just this sample) were verified the same way before being recorded; none failed to resolve.

## 8. Standing-instruction compliance

⛔ Nothing drafted, altered, or posted to Rev. James. ⛔ JD's raw artifact (`src/SRC_Discord_RPW-raw.txt`) not touched. ⛔ `Incense_Conversational_Outline.md` and `RJ_Incense_Analysis.md` not touched. ⛔ No finding minted, no ledger number of any kind consumed. ⛔ No message body byte in `src/SRC_Discord_RPW.md` altered — only the changelog block's position changed.

## 9. Numbers consumed

**NONE.** No `DQ`, `IP`, `LS`, `RV`, `Rev`, `BLOG`, `POD`, `VP`, `GV`, `RC`, `BP`, `EXT`, `W`, `DELTA` or `File`. This is a structural repair pass.

## 10. Validator AFTER — reported against baseline

`81 ok · 10 warnings · 0 errors` — **identical to the BEFORE baseline** except three `[C3]` lines now read `260835-29` instead of `260835-28` (the expected registry-version bump for the three files this pass touched: `PROJECT_STATE.md`, `SRC_Manifest.md`, `St_Francis_EMC_Distinctives.md`). Confirmed by full diff of validator output, not by error count alone. An intermediate run (after the archive move but before the registry version bumps) surfaced 2 `[C3]` VERSION DRIFT errors as expected — resolved by bumping the two registry cells and `St_Francis_EMC_Distinctives.md`'s own stamp line, then re-confirmed clean.

## 11. Files changed — and what to stage

- `src/SRC_Discord_RPW.md` — changelog relocated prepended → appended; no message body byte altered; size/line-count unchanged; hash changed.
- `SRC_Manifest.md` — new `Changelog position` binding-rule row; SHA-256/Export-history dated notes; `Last updated` stamp bumped.
- `St_Francis_EMC_Distinctives.md` — dated offset-repair notes beside `DQ-24`, `DQ-25`, `DQ-26`; `Last updated` stamp bumped; no finding text altered.
- `PROJECT_STATE.md` — new GATE(260835-29) block; §7 defect row marked RESOLVED by dated note; §4 registry version cells bumped for `PROJECT_STATE.md`, `SRC_Manifest.md`, `St_Francis_EMC_Distinctives.md`.
- `passes/260835-29_rpw-changelog-append-conversion-and-offset-repair_close-out.md` — this artifact (new).

**Per JD's standing instruction: commit nothing this pass.** JD pushes `passes/` first, then the corpus edits separately. `git status --short` at close:

```
 M PROJECT_STATE.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
 M src/SRC_Discord_RPW.md
?? passes/260835-29_rpw-changelog-append-conversion-and-offset-repair_close-out.md
```

Recommended staging, when JD is ready: stage `passes/260835-29_...close-out.md` first and push/commit it alone, then stage the four corpus files (`src/SRC_Discord_RPW.md`, `SRC_Manifest.md`, `St_Francis_EMC_Distinctives.md`, `PROJECT_STATE.md`) as a second, separate commit — per the brief's explicit sequencing.

## 12. What was declined, checked-and-empty, or left unresolved

- No finding minted, no `DQ` consumed, no ledger number of any kind touched.
- `DQ-24`'s quoted text was not altered — only its offsets were stale, and only its offsets are corrected.
- The other four `SRC_Discord_*.md` archives' prepended-changelog shape is reported, not converted — out of scope for this pass, per the brief.
- The "must"-italics inline position-check inside `DQ-24`(b) is noted to move but is not independently re-verified beyond confirming it shared (b)'s old boundary value — it was already discharged as a finding by `260834-4` and carries no live argumentative weight.
