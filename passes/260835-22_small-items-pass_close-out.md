# 260835-22 — Small-items pass: five queued items (close-out)

**Date:** 2026-08-28 · **Type:** small-items, apply · **Result:** all five items applied; nothing minted; nothing committed.

---

## Gate

| Item | Value |
|---|---|
| Briefed HEAD | `6d0f881` |
| Actual HEAD | `6d0f881979920a838243b40ebad2dc281378835a` — ✅ **exact match** |
| Branch | `main` |
| `git --no-optional-locks status --short` before first edit | ✅ **EMPTY**, captured directly, not reconstructed |
| Git read discipline | every read used `git --no-optional-locks` per the `260835-3` FUSE-lock diagnosis; no lock created, none removed, no `rm` attempted |
| `PROJECT_STATE.md` stamp at gate | **`260835-21`** |
| Next-free pass stamp | **`260835-22`** — derived fresh (below) |
| Validator BEFORE | **`82 ok · 9 warnings · 0 errors`** |
| Validator AFTER | **`82 ok · 9 warnings · 0 errors`** — identical, see the item-3 accounting |

### Validator BEFORE — all nine firing codes, verbatim

1. `WARN [C1] src/SRC_Discord_RPW.md: 2 relative timestamp(s) outside message headers ('Yesterday at …').`
2. `WARN [C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: no parseable 'Last updated' stamp; registry says '260832-2'`
3. `WARN [C3] tools/transcribe_yt.py: no parseable 'Last updated' stamp; registry says '260833-7'`
4. `WARN [C4] St_Francis_EMC_Distinctives.md: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby.`
5. `WARN [C5] RJ_Final_Question_List.md: 17 volatile-state assertions.`
6. `WARN [C5] RJ_Incense_Analysis.md: 9 volatile-state assertions.`
7. `WARN [C5] St_Francis_EMC_Distinctives.md: 7 volatile-state assertions.`
8. `WARN [C10] §15's newest LS citation is 9 findings behind the ledger (LS-120 vs LS-129).`
9. `WARN [C11] outline last checked against IP-97 (260833-5); the IP ledger now runs to IP-108. 11 finding(s) unreviewed.`

⛔ **None of the nine is this pass's business, and none moved.** Full run preserved at `passes/260835-22_validator-after.txt`.

### Stamp derivation

Repo-wide grep for `260835-[0-9]{1,3}` across all tracked `*.md` and `*.py`, sorted numerically: the run is unbroken to **`260835-21`**, which is `PROJECT_STATE.md`'s own stamp and a real consumed stamp. **`260835-22` returned zero matches repo-wide. This pass is `260835-22`.**

⚠️ **A derivation hazard is recorded for later passes, and it is the subject of item 4:** `260835-12` and `260835-14` are **both real and both consumed** — `260835-12` by the `CLAUDE.md`/Bootstrap divergence audit, `260835-14` by the diarization-verification pass whose internal prose still says `260835-12`. A naive content-grep can be misled in both directions here.

---

## Item 1 — `A101-2026-07-26`'s `[R]` primary row is closed ✅

### Hash verification (performed before the gap was treated as closed)

The brief supplied the expected values; this pass verified them independently against the file on disk rather than accepting them.

```
path   : original transcripts/in person classes/20260726/A101-20260726-JD-recording-with-q-and-a.md
bytes  : 57,305                                    ✅ matches registered
raw sha256      : 96a9c5a9cac91232c2d1c0971af6fbdc7afb265f99bd737873e082c99b3e038e
body.strip()    : 96a9c5a9cac91232c2d1c0971af6fbdc7afb265f99bd737873e082c99b3e038e   ✅ EXACT match
text.strip()utf8: 96a9c5a9cac91232c2d1c0971af6fbdc7afb265f99bd737873e082c99b3e038e
```

⭐ **All three digests are identical** — the file carries no leading or trailing whitespace, so `SRC_Manifest.md`'s registered `sha256(body.strip())` value is also its raw-bytes digest. **The recovery is byte-exact, not merely equivalent.**

### The `260835-12` note

⛔ **NOT deleted and NOT rewritten.** The note reading *"THE SUBSTRATE IS RECOVERED, BUT THIS FILE IS STILL MISSING AND THIS ROW IS NOT SATISFIED"* stands verbatim in `SRC_Manifest.md`'s `[R]` cell. **It was accurate when written.** A new dated `260835-22` note was added *beside* it recording the recovery, the verified hash, the current path, and that the row is satisfied. The parallel note in `St_Francis_EMC_Distinctives.md` was treated the same way.

⚠️ **Location class unchanged:** the file is still held **outside the repo**, in JD's archive, per the standing rule for `[R]` captures. Recovery changed its availability, not its location class.

### `File 56` reconciliation

⛔ **`File 56` is NOT deregistered and its row was not edited.** Both notes state that the two **coexist and are not interchangeable**:

| Question | File of record |
|---|---|
| Who is speaking · diarization · speaker mapping | **`File 56`** (the diarized third rendering) |
| Wording · byte offsets · hash-verified quotation | **the recovered `[R]` primary** |

`File 56` remains the **sole** substrate for the speaker `A`/`B` mapping, the Father Bryan second-priest discovery across `IP-31`…`IP-36`, the independently confirmed attendee assignments, and `IP-32`'s Article XV room-side coverage. ⛔ **The recovered `[R]` primary is undiarized and can answer none of those.** The reconciliation is stated as a routing rule so a later pass does not treat the recovery as superseding `File 56`.

### Spot-check of `IP-24`…`IP-39` — sample, not exhaustive, per brief

The sixteen were verified against `File 56` at `260835-14` and were **not** redone. Instead, **27 logged `[R]` byte-offset anchors** drawn from **11 of the 16 findings** were re-resolved against the recovered file:

| Finding | Anchors | Result |
|---|---|---|
| `IP-24` | 2 | ✅ both exact |
| `IP-25` | 1 | ✅ exact |
| `IP-26` | 3 | ✅ all exact |
| `IP-27` | 2 | ✅ both exact |
| `IP-28` | 3 | ✅ all exact |
| `IP-29` | 2 | ✅ both exact |
| `IP-30` | 2 | ✅ both exact |
| `IP-37` | 4 | ✅ all exact |
| `IP-38` | 4 | ✅ all exact |
| `IP-39` | 4 | ✅ all exact |
| **Total** | **27** | ✅ **27 at delta `+0`; 0 NOT FOUND; 0 offset-divergent** |

*(`IP-31`…`IP-36` were deliberately not sampled: they are wholly or largely `[S]`-sourced and `[R]` is fragmentary there by the row's own record, so `[R]` offsets are sparse and a null result would carry no information.)*

✅ **No wording divergence at any checked point. `260835-14`'s verification therefore STANDS, unamended.**

⚠️ **Reported honestly rather than oversold.** The hash match **already entails byte-identity**, so the offset check is **confirmatory, not independent evidence of file integrity**. What it *does* establish independently is that the offsets recorded in `IP-24`…`IP-39` were logged **against this file** and not against some other rendering — which is the load-bearing question, and it is answered yes.

---

## Item 2 — `ORCHESTRATION.md`: channel ownership is not a speaker warrant ✅

### The search came first

The brief flagged that neither JD nor the orchestrator was certain whether this had already been applied — possibly folded into `260835-15`'s new warrant class. **It had not been.**

- `ORCHESTRATION.md` §8 read in full: contains the `260835-15` **SINGLE-LABEL, NOT CONFIRMED SINGLE-VOICE** class and no ownership rule.
- ⭐ **The two answer different questions.** `260835-15`'s class governs *how many voices a single diarization label conceals*. This amendment governs *whose voice it is at all*. Neither subsumes the other.
- ✅ **Decisive:** `passes/260835-18_batch9-remainder-registration-and-mining_close-out.md` L263 — *"`ORCHESTRATION.md` §8 amendment: `EXT-2` channel ownership is NOT a speaker warrant — still owed from `260835-14`; this pass supplies its mechanism (Fr. Ray was his own rector) but does not write the amendment."*

**Genuinely absent. Written.**

### What was written

Added to §8, stamped `260835-22`:

- ⛔ **Ownership is a fact about who published; it is not a fact about who talked** — for `EXT-2`, `EXT-3`, or any channel, feed, blog or archive.
- The instance that forced it: `8nRhmD4w-Wg` / `9Fezj9WMh3A`, two *"Fr. Ray Teaching About…"* videos on Rev. James's own channel, **entirely another priest's teaching**, predating his 2020 diaconate; `File 58`/`File 59`, formally `EXCLUDED — confirmed not Rev. James`.
- ⭐ The mechanism, kept because it **generalises**: Fr. Ray was his own first priest and mentor. **A channel hosting a mentor's, colleague's, guest's or played-back third party's material is a NORMAL case to expect, not a freak one.**
- ✅ **Admissible grounds enumerated:** self-identification · direct address by name · role self-identification · unique first-person biography · elimination against a content-derived speaker set.
- ⛔ **Non-warrants enumerated:** channel ownership · title · uploader · diarization label (`260835-7` label-flip) · speaking duration (`File 52` inversion) · folder location · registration itself.
- ⛔ Unresolvable → **ATTRIBUTION OPEN, not mined**, and *"never closed by defaulting to the channel owner."*

---

## Item 3 — `[C3]` stamp-truncation fixed ✅ — and it surfaced one hidden drift

### The defect

```python
rtok = re.search(r'\d{6}-\d', rv)     # six digits, dash, exactly ONE digit
dtok = re.search(r'\d{6}-\d', dv)
```

Every iteration number past 9 was **truncated to its first digit before comparison**. `260835-16` and `260835-18` both reduced to `260835-1` and compared **equal**, so `[C3]` printed *"version agrees with registry"* over live drift.

⛔⛔ **This is the same defect SHAPE as the `260725-1` glob defect already documented in the file's own header: a check that ran, reported "ok," and was not comparing what it claimed to compare. Silent false passes are worse than noisy failures.**

### The fix

```python
rtok = re.search(r'\b\d{6}-\d+\b', rv)
dtok = re.search(r'\b\d{6}-\d+\b', dv)
```

`\d+` takes the whole iteration number; `\b` on both ends stops a stamp matching inside a longer digit run. A full inline comment block was added at the check and a dated entry at the file header, per convention.

### Behaviour verified against cases

| registry | document | old | new | |
|---|---|---|---|---|
| `260835-16` | `260835-18` | `ok` | **`DRIFT`** | real drift, was hidden |
| `260835-2` | `260835-21` | `ok` | **`DRIFT`** | was hidden |
| `260812-1` | `260812-11` | `ok` | **`DRIFT`** | was hidden |
| `260835-21` | `260835-21` | `ok` | `ok` | agrees |
| `260835-9` | `260835-9` | `ok` | `ok` | agrees, single-digit |
| `v22 (260835-16)` | `260835-16 (v22)` | `ok` | `ok` | agrees, decorated cell |

✅ **No false positives introduced; three previously-invisible drift shapes now caught.**

### Drift surfaced by the fix — one instance, corrected

⭐ **`SRC_Channel_Inventory.md` — §4 registry cell `260835-16`, document stamped `260835-18`.** Both truncated to `260835-1`; `[C3]` had been passing it silently.

**Which side is right was checked, not guessed:**

- `passes/260835-18_…_close-out.md` L252: *"Touched four tracked files: `PROJECT_STATE.md`, `SRC_Manifest.md`, `SRC_Channel_Inventory.md`, `St_Francis_EMC_Distinctives.md`."*
- `PROJECT_STATE.md`'s own `260835-18` pass note names the same four.
- The document's own header carries a substantive `260835-18` summary (the Batch 9 remainder close-out).

✅ **The document's `260835-18` stamp is correct; the registry cell was simply never updated in that pass.** The **cell** was corrected to `260835-18` with a dated `260835-22` note explaining the correction and why `[C3]` had missed it. ⛔ **The document's stamp was not touched.**

⛔ **Nothing else surfaced, and nothing ambiguous was guessed at.** The brief's own cited instances (`PROJECT_STATE.md` and `SRC_Manifest.md` at `260835-16` vs `260835-18`) had already been resolved by later passes — both now stamp `260835-21` — and are recorded here as historical, not live.

### Accounting for the validator count

| | ok | warn | err |
|---|---|---|---|
| BEFORE | 82 | 9 | 0 |
| AFTER | 82 | 9 | 0 |

**The count is unchanged, and that is the correct outcome rather than evidence the fix did nothing.** The fix made exactly one hidden drift visible; that drift was **corrected inside the same pass**, so it never had the chance to fire. Had it been left, `[C3]` would now show **1 error**. The nine warning codes are byte-identical to baseline.

---

## Item 4 — `PROJECT_STATE.md`'s `260835-12` / `260835-14` mislabel ✅

The gate and pass-note blocks describing the diarization-verification work are labelled **`260835-12`**; that work was **committed as `260835-14`** after its artifacts were renamed, the original `260835-12` having been consumed in flight by the `CLAUDE.md`/Bootstrap divergence audit. The collision was self-reported at the time (`260835-13`'s commit message), but the internal prose was never relabelled.

⛔ **Corrected as a dated note, NOT by find-and-replace.** The note was placed **immediately above** the two mislabelled blocks so a reader meets the correction before the error. The mislabelled prose is left exactly as written.

The note records: what happened and why; that the authoritative record is `260835-14` on two independent witnesses (committed artifact filenames + commit message); that `passes/260835-14_…_close-out.md` carries the same defect on its own first line and is likewise left standing; that **this is a labelling defect only** — no finding, verification, `File` registration, speaker mapping or byte offset is in question; that cross-references elsewhere citing this work as `260835-12` are correspondingly mislabelled and are **not** being hunted down and rewritten; and the derivation consequence — **both `260835-12` and `260835-14` are real and consumed.**

*(First flagged as an anomaly at `260835-15`, which correctly declined to repair it as out of scope.)*

---

## Item 5 — the progress-reporting standing instruction now exists ✅

### Placement was checked, not assumed

`ORCHESTRATION.md` **§8 "Standing instructions"** is the repo's own home for standing instructions to delegated sessions — it already holds the incense/icon priority rule, the never-post-to-Rev.-James rule, the never-alter rule, the dual-registry update rule, and the `260835-15` warrant class. §5 is hand-off *format* (what a hand-off block names) and §4 is pass artifacts; neither is the right home. **§8 it is.**

### Absence re-confirmed

`260835-21` found no such instruction. Re-checked here across all tracked `*.md`: every hit for status/progress language is unrelated findings-corpus prose (*"Status update (RC intake)"* and similar in `St_Francis_EMC_Distinctives.md` / `RJ_Final_Question_List.md`). ⚠️ **A convention carried in every delegated prompt, written down nowhere.**

### What was written

A delegated session emits a brief status line **roughly every ten minutes or at each major task boundary, whichever comes first**, stating exactly three things: **which task · rough progress · whether anything is blocking.** One or two sentences. Their value is *arriving during the work, not after it.*

⛔⛔ **The guard the brief specified, written in full:** status lines are **instrumentation, not deliverables**. They never replace, abbreviate, substitute for or excuse any part of the full close-out; *"I already said that in a status update"* is not a reason to omit anything; the close-out must stand alone and be readable by someone who saw no status line; **nothing is ever established by a status line** — no findings, no verifications, no decisions.

---

## Hard limits — all honoured

- ⛔ **`Incense_Conversational_Outline.md` — NOT touched** (not even read this pass).
- ⛔ **`RJ_Incense_Analysis.md` §4.6/§4.8/§4.10 — NOT touched.** That file was not modified at all.
- ⛔ **Nothing drafted, altered or posted to Rev. James.**
- ⛔ **`DQ-9` not moved and not touched.**
- ⛔ **Nothing minted** — no finding, and no `IP`, `LS`, `RV`, `DQ`, `BLOG`, `POD`, `VP`, `GV`, `RC`, `BP`, `EXT`, `W` or `File` number. Next-free values unchanged.
- ⛔ **No existing finding altered, renumbered, re-pointed or corrected; no byte offset in any entry altered.**
- ⛔ **`File 56` not deregistered; its row not edited.**
- ⛔ **No find-and-replace performed anywhere in this pass.** Every correction is a dated note beside the original.
- ⛔ **No Discord state touched. Nothing committed.**

---

## Files touched — five tracked files plus artifacts

| File | Change | Stamp |
|---|---|---|
| `SRC_Manifest.md` | `[R]` cell dated note (recovery, hash, `File 56` coexistence, spot-check); header summary | `260835-21` → **`260835-22`** |
| `St_Francis_EMC_Distinctives.md` | dated note at the `A101-2026-07-26` block; changelog entry | `260835-20` → **`260835-22`** |
| `ORCHESTRATION.md` | §8 ×2 new standing instructions (items 2 and 5); header summary | `260835-15` → **`260835-22`** |
| `validate_project.py` | `[C3]` regex fix + inline comment block + header defect note | `260812-1` → **`260835-22`** |
| `PROJECT_STATE.md` | item-4 dated note; gate + pass note; `SRC_Channel_Inventory.md` cell correction; five §4 registry cells | `260835-21` → **`260835-22`** |

New artifacts: `passes/260835-22_small-items-pass_close-out.md` (this file) · `passes/260835-22_small-items-pass.diff` · `passes/260835-22_validator-after.txt`.

---

## `git status --short` at close — nothing committed

```
 M ORCHESTRATION.md
 M PROJECT_STATE.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
 M validate_project.py
?? passes/260835-22_small-items-pass.diff
?? passes/260835-22_small-items-pass_close-out.md
?? passes/260835-22_validator-after.txt
```

**Stage all eight** — the five modified tracked files and the three new `passes/` artifacts. ⛔ **This pass committed nothing**, per instruction.

---

## Owed / carried forward — not this pass's business, recorded so it is not lost

- ⏳ Ear-checks **E1** (`hDRmWM5Nkgw`, blocking — the live instance of the item-2 rule) and **E2**… **E5**; E2 was discharged from content at `260835-18`.
- ⏳ `[C3]` still WARNs on two files with no parseable stamp: `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` and `tools/transcribe_yt.py`. **Now that `[C3]` compares stamps correctly, giving these two real stamps would bring them under a check that actually works.** Cheap, and not attempted here.
- ⏳ `[C10]` §15 nine `LS` findings behind the ledger head; `[C11]` eleven `IP` findings unreviewed against the outline.
- ⏳ Cross-references elsewhere in the corpus citing the diarization pass as `260835-12` remain mislabelled by inheritance (item 4's note covers them; they are not being rewritten).
