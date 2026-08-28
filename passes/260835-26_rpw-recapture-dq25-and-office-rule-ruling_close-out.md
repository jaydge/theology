# 260835-26 — The RPW recapture processed (`DQ-25` minted), and JD's office-rule ruling applied (close-out)

**Real repo pass.** Two parts, both applied. Nothing committed.

---

## Gate

| Item | Value |
|---|---|
| HEAD at gate | `4d0d91cf49ef42f9d99880ee3aa740cf112779f9` — **matches the briefed `4d0d91c` exactly**; branch `main` |
| `git --no-optional-locks status --short` before first edit | ⭐ **EMPTY** — captured directly, not reconstructed |
| Lock discipline | every git read used `git --no-optional-locks` per the `260835-3` FUSE diagnosis; no lock created, none removed, no `rm` attempted |
| Validator BEFORE | **`82 ok · 9 warnings · 0 errors`** (91 checks) |
| `PROJECT_STATE.md` stamp at gate | **`260835-25`** |
| This pass | **`260835-26`** |

### Every firing code at gate, reproduced rather than summarised

| Code | File | Message |
|---|---|---|
| `C1` | `src/SRC_Discord_RPW.md` | 2 relative timestamps outside message headers (`Yesterday at …`) |
| `C3` | `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` | no parseable `Last updated` stamp; registry says `260832-2` |
| `C3` | `tools/transcribe_yt.py` | no parseable `Last updated` stamp; registry says `260833-7` |
| `C4` | `St_Francis_EMC_Distinctives.md` | 2 passages describe an ANSWERED question as pending with no supersede marker |
| `C5` | `RJ_Final_Question_List.md` | 17 volatile-state assertions |
| `C5` | `RJ_Incense_Analysis.md` | 9 volatile-state assertions |
| `C5` | `St_Francis_EMC_Distinctives.md` | 7 volatile-state assertions |
| `C10` | — | §15's newest `LS` citation 9 findings behind the ledger (`LS-120` vs `LS-129`) |
| `C11` | — | outline last checked against `IP-97` (`260833-5`); `IP` ledger runs to `IP-108`; 11 unreviewed |

### Stamp derivation — hazard note read first, as the brief required

The `260835-12`/`260835-14` hazard note (recorded at `PROJECT_STATE.md` `260835-22`, restated in the `260835-23`, `260835-24` and `260835-25` close-outs) was read **before** deriving:

- `260835-12` reads as *available* to a naive grep because earlier close-outs contain prose asserting its absence — **but it is REAL and CONSUMED** (the `CLAUDE.md`/Bootstrap divergence audit, commit `530d987`).
- `260835-14` exists **only** as committed filenames and a commit message, its own internal prose still reading `260835-12` throughout — **and it too is REAL and CONSUMED** (the diarization-verification pass, commit `68bf1d8`).

Both treated as consumed. `grep -rhoE '\b26[0-9]{4}-[0-9]+\b'` across all `*.md` / `*.py` returns an unbroken run **`260835-1 … 260835-25`** with no gaps; **`260835-26`…`260835-99` and `260836-*` occur nowhere**. `passes/` on disk independently confirms no `260835-26` artifact exists.

✅ **`260835-26` is next free.**

---

## ⛔ One brief premise falsified, reported rather than complied with

The brief instructed: *"Resolve any relative timestamps against the capture line per the standing convention."*

**The recapture carries no capture line. It was deleted.**

```
git diff 2427eba baa2f09 -- src/SRC_Discord_RPW-raw.txt
@@ -1,5 +1,3 @@
-CAPTURED 2026-08-28, 8:21 AM ET, by JD, from the Discord client.
-
 Regulative Principle
```

This is the **first recapture since the `260833-6` convention was established to arrive without it** — and that convention exists precisely because Discord renders same-day timestamps bare. The instruction was not executable as written.

⏳ **FLAGGED FOR JD: restore the capture line on the next capture.** ⛔ **Not re-added by this pass** — the raw is JD's capture artifact and a session does not write into it.

**Registered as a fifth capture-method/artifact defect in `SRC_Manifest.md`**, distinguished from the existing four as a *regression* rather than an inherent limitation.

---

# Part A — the Discord recapture

## Diff against last-known-good: clean

⭐⭐⭐ **The edit detector is raw-vs-raw, per the `260833-6` precedent, and it is decisive.** `git diff 2427eba baa2f09` returns **the capture-line deletion and pure appends and nothing else** — zero changes to any already-captured message body across the whole thread history.

⭐⭐ **Independently re-confirmed programmatically:** all 34 previously-archived messages parsed out of both artifacts and compared body-for-body — **34/34 byte-identical.**

✅ **Nothing earlier changed. There was nothing to report before resolving.** Rev. James edited nothing; JD edited nothing.

## Timestamp resolution — by elimination, warrant class stated

Both new headers render bare (`8:55 AM`, `4:48 PM`). With no capture line, the standing method is unavailable. Both resolve to **`8/28/26`** on two independent, machine-witnessed bounds:

1. A bare render means same-day-as-capture (this file's own `260833-6` finding), and the capture necessarily precedes the commit at **2026-08-28 17:04:17 -0400**. → capture day is 8/28 or earlier.
2. The prior raw at `2427eba` was captured **2026-08-28 8:21 AM ET** and contains **no message after `8/26/26, 4:29 PM`**. An `8:55 AM` message on 8/27 or any earlier day would have appeared in it. It does not. → 8/27 and every earlier day excluded.

⭐ **8/28 is the only surviving value.** Corroborating bracket, run rather than assumed: `8:55 AM` falls 34 minutes after the prior capture (explaining its absence there), `4:48 PM` sixteen minutes before the commit.

⛔⛔ **WARRANT CLASS, STATED HONESTLY:** this is **commit-timestamp-plus-elimination**, not the capture-line method. It is machine-witnessed at both bounds and therefore **stronger** than the `260801-2`/`260810-1` JD-recollection class — but it is **NOT** the `260833-6` capture-line class and must not be cited as if it were.

## One-or-two-posts: settled by a witness, for the first time

The raw carries **ONE** rendered header (`8:55 AM`) over JD's material. Its final sentence follows after a **single newline with no header** — the exact structural signature `260833-1` met at message 24 and left open between a Shift+Enter continuation and a same-group follow-up post.

⭐ **JD reports in the brief that it was posted as two consecutive posts.** He is the author, which is the strongest available warrant for his own posting behaviour, and it resolves what the bytes cannot.

⛔ Archived as messages **35** and **36**, the single-newline boundary preserved byte-exactly as the post boundary, message 36's heading marked as sharing message 35's one rendered header. **The `260833-1` message-24 determination is NOT revisited** — that case had no witness and still has none.

## The append

| # | Author | Resolved | Content |
|---|---|---|---|
| 35 | JD Smith (OP) | `8/28/26, 8:55 AM` | Off Discord a couple of days; **disclaims the reading message 34 attributed to him** — *"I wasn't asking for an exact timeframe - just trying to understand what makes something count as 'received' in general, and how to tell if it applies to the whole church or just whichever jurisdictions choose to accept it."* |
| 36 | JD Smith (OP) | same header | Anchors to RJ's own words — *"Mainly I'm trying to follow the reasoning behind your statement, 'we don't do them because those practices aren't what we've received.'"* |
| 37 | Athanasius325 / Fr James | `8/28/26, 4:48 PM` | ⭐⭐⭐ **Substantive; answers the standing question.** |

**Unicode:** both new headers carry U+202F between time and AM/PM — verified **exactly 2 occurrences in the new region, ZERO in any of the three bodies** — consistent with the whole-class, header-only artifact this file has normalised at every prior capture. Normalised to plain space. The message-19 U+202F anomaly is unrelated and remains unmoved, still awaiting JD's ruling.

**`(edited)` marker:** none observed; per the standing clipboard-capture limitation this confirms nothing on its own. The raw-vs-raw byte diff is the detector, and this pass it came back clean.

**§8 incense/icons check:** ⛔ CONFIRMED ZERO in all three new posts.

## `DQ-25` — minted

`260835-21` established this exchange as a **new committal question** (not a continuation of `DQ-24`), left `DQ-25` free and unspent, and expressly named **both** precedents for when to mint — POSTED-AWAITING (the `DQ-18`/`DQ-19` shape, number consumed at posting) versus AT-COMPLETION — leaving the call to the downstream pass.

⭐ **The exchange is now complete:** question posted (msg 33) → clarifying counter-question (msg 34) → restatement and re-anchoring (msgs 35-36) → **substantive answer (msg 37)**. The at-completion condition is satisfied on its own terms, so the choice between the two precedents **did not need to be forced** — minting now satisfies both.

✅ **`DQ-25` re-verified genuinely free before consumption, not assumed:**

- validator `C2` reports `DQ-1..24` unbroken, no duplicates, at this pass's gate;
- every `DQ-25` occurrence repo-wide opened and read — every one is a next-free registry assertion or `260835-21`'s own determination note;
- `PROJECT_STATE.md` §3 independently names `DQ-25` next free;
- `DQ-26` occurs nowhere in the repo.

### The three `[Stated]` findings, with byte offsets

| | Quote | Offset |
|---|---|---|
| (a) | *"In saying something haven't been received, it hasn't been substantially practiced ever by our theological predecessors."* | `@67,816–67,935` |
| (a) | *"In the case of trying to emulate the exact practices involved directly with the Shewbread of the OT, I am unaware of anything that even remotely calls for such practices."* | `@67,936–68,106` |
| (b) | *"when we talk about receiving something all we mean by that is that we have literally received it from our theological predecessors: it is not something we have innovated on."* | `@68,173–68,346` |
| (c) | *"So the introduction of liturgical dancing, as some of the modern Roman Catholic, Lutheran, or Episcopal churches do, would be (at least in the West) innovative and thus not something that was received."* | `@68,347–68,548` |

⚠️⚠️ **OFFSET-UNIQUENESS DISCLOSURE, because this entry breaks the file's usual guarantee and says so in the ledger itself:** the (c) string occurs **twice** in `src/SRC_Discord_RPW.md` — once in the body (the offset given) and once inside `260835-26`'s own changelog entry, which quotes it verbatim. **Every other offset above was verified to occur exactly once.** The `DQ-25` entry records this explicitly so a lookup that does not anchor past the changelog is not silently misled.

⚠️ **Quoted exactly as archived, including *"something haven't been received"*** — a plain grammatical slip, not corrected.

## ⚠️ The two things the brief asked to be recorded precisely

Recorded **without interpretation**, as dated notes at `OQ20` and `OQ21`, and in the `DQ-25` entry itself.

### (1) He answered one half of the question and not the other

JD's message 35 asked **two** things:

- **(i)** what makes something count as *"received"* in general;
- **(ii)** how to tell whether it applies to the whole church or only to whichever jurisdictions choose to accept it.

**(a)/(b) answer (i).** ⛔⛔ **Nothing in the reply addresses (ii). The church-wide-versus-jurisdictional half is unanswered and remains open as `OQ21`** — now asked **twice** (messages 33 and 35) and answered **zero** times.

⛔ **Recorded as a fact about the reply's coverage. NOT as evasion, NOT as a charge, and NOT as evidence of anything about his position.**

### (2) *"at least in the West"* is a regional qualifier bearing on the unanswered half

(c)'s judgment that liturgical dancing is innovative is scoped **"(at least in the West)"** — the innovation verdict qualified by region rather than asserted church-wide. That is the same church-wide/jurisdictional axis `OQ21` tracks, surfacing **unprompted in the very reply that leaves `OQ21` unanswered**.

⛔⛔⛔ **THE OBSERVATION IS RECORDED AND NOTHING IS BUILT ON IT.** Not treated as an implicit answer to (ii); no inference drawn about what he would say church-wide; no argument constructed; no question drafted from it; nothing put to him.

## `OQ20` moves but does not close

⭐ The term is **defined for the first time in his own voice**, after three prior dated notes that each recorded only another undefined deployment.

⛔⛔ **The DATE-FLOOR half is untouched.** *"ever… by our theological predecessors"* names **a class of persons, not a date**; *"substantially practiced"* is **a breadth test whose threshold he does not specify**. The item's sharpest form is engaged, not resolved.

⚠️ Against its three candidate readings: *"our theological predecessors"* is closer to *received-by-his-own-tradition* than to the Vincentian *universal* — ⛔ **but *"our"* is not defined either, and the question that would settle it is exactly the one he did not answer. NO READING IS CHOSEN.**

⛔⛔ **`LS-23`/`LS-24` are NOT merged with the new definition.** The standing one-rule-or-two guard is carried forward unweakened; the lexical adjacency between *"substantially practiced ever by our theological predecessors"* and *"the consensus"* is **not** treated as identity.

---

# Part B — the office-rule ruling

## The premise that failed

`260835-24`'s case 1 declined a pure office **on the assumption that it carries no original teaching.** JD's ruling: **commentary around the liturgy is original teaching even where there is no homily** — announcements, framing, explanation of what is being done and why, asides between the parts of the rite.

⛔⛔ That does not narrow the old case 1 at its edges. **It falsifies its central assumption.**

## (1) Five rows returned to `INCLUDE`; one held

| Line | Video ID | Title | Result |
|---|---|---|---|
| 156 | `V-K-iLT9OH4` | Compline, From St. Augustine's Prayerbook | ✅ `INCLUDE` T3 |
| 264 | `x1NR-8xqt9c` | Matins: The Purification of St Mary the Virign (1928) | ✅ `INCLUDE` T3 |
| 266 | `93_uEJYu64Q` | Matins for the Feast Day of St Charles the Martyr (1928 BCP) | ✅ `INCLUDE` T3 |
| 371 | `io-OsOmFXhM` | Praying the Great Litany (2019 BCP) | ✅ `INCLUDE` T3 |
| 381 | `fXpoPWugyXI` | Tuesday Evening Prayer, 17th Sunday After Trinity, 1928 BCP | ✅ `INCLUDE` T3 |
| 111 | `8gb4BXlfLO4` | Easter Vigil From When I was in Seminary | ⛔ **HELD `DECLINED-office`** |

**Method:** each of the five is a **dated reclassification** whose new cell ends `*Previously:*` followed by **the entire prior cell verbatim**, per never-alter. ⛔ **No prior cell text was altered, and no find-and-replace was used anywhere.**

⛔⛔ **`8gb4BXlfLO4` held**, on grounds independent of the premise that moved: a **31-second fragment** (too short to carry commentary of any kind), and — the stronger ground — its description **names another parish and another priest** (*"Grace Anglican Church in Edgeworth, PA. The Rector at the time was Fr Chance Perdue"*), which the Fr. Ray precedent (`8nRhmD4w-Wg`/`9Fezj9WMh3A`) and §8's channel-ownership rule decide regardless. ⛔ **Its cell is not altered; a dated note sits beside it.**

⭐ **The `260835-24` cell's own foresight is what made this cheap** — it recorded two grounds explicitly *"so a future pass that overturns one does not reopen the row."* That is exactly what happened.

⭐ **The revisit returned FIVE rows, not six — exactly as `passes/260835-25_five-rulings_close-out.md` §6.2(a) predicted.** Re-derived directly against the inventory: the `DECLINED-office` class now holds **exactly one row**.

## (2) `ORCHESTRATION.md` §8 case 1 softened

**The amended case 1:** a pure office recording → **`INCLUDE`, and PULL IT.** Do not decline an office merely for being an office, and do not decline it on the silence of its title and description. Decline **only on an independent ground**, of which three are established:

- **FRAGMENT** — too short to carry commentary (`8gb4BXlfLO4`, 31s, the worked example);
- **NAMED OTHER SPEAKER** — another man's liturgy or voice (the Fr. Ray precedent, and the channel-ownership rule);
- **NO ORIGINAL CONTENT OF ANY KIND** — established **from content actually examined**, ⛔ never from metadata, never presumed.

⛔⛔ **Cases 2 and 3 are unchanged.** Both the original three-case text **and** the `260835-25` flag are **retained verbatim**, each marked superseded where it stands; the flag's now-false sentences (*"REMAINS IN FORCE EXACTLY AS WRITTEN"*, *"a pass meeting this flag should apply the rule as written"*) are **called out rather than edited**.

### ⚠️ `260835-25`'s counter-argument is carried into the amendment, not left behind

The brief was explicit that the softened rule must not read as claiming offices are high-yield. **The counter-argument is written into the operative text itself**, not only into the retained flag:

> `File 69` (`M7iSL5mznTk`) is **100% read-aloud with ZERO own-voice content** (`260835-18`) — at least one pure office in this corpus demonstrably contains **no commentary at all.** So a thin or empty return on an office pull is a **REAL AND EXPECTED OUTCOME**, not a miss and not a failed pass. A pass that records a nil return on an office row **has done the work correctly.**

⭐ **`INCLUDE` on an office row means PULL AND CHECK, not a prediction that content exists.** This sentence appears in the amended rule, in all five reclassified cells, and in the coverage register.

⛔⛔⛔ **The read-aloud attribution layer remains REQUIRED and is NOT waived — under JD's own reasoning it matters MORE, not less**, because the commentary sought sits **interleaved** with the liturgical text rather than in a separable homily block. `File 69` is retained as the standing warning: its read-aloud layer carries first-person *"I believe that Thou art truly present in the Holy Sacrament"* — the Prayer Book's words, not his — sitting exactly on the corpus's live eucharistic questions.

## (3) `SRC_Coverage_Register.md` — the `260835-25` debt discharged

Two dated notes; ⛔ **no existing figure, table or sentence rewritten.** Every figure **re-derived directly from `SRC_Channel_Inventory.md` this pass** — all 368 data rows parsed, 8 columns confirmed present on every row — and **not** carried from the brief, which supplied none.

⭐⭐⭐ **Headline: EXT-3 has no blank rows left.**

| | `260835-21` | **Now** |
|---|---:|---:|
| EXT-3 rows total | 62 | **62** |
| carrying a decision from Files 8-9 / 10-12 / 41 | 20 | **22** |
| carrying *any* decision | 47 | **62** |
| **no decision cell of any kind** | 15 | ⭐ **0** |

Current EXT-3 verdict distribution: **52 `INGESTED` · 6 `INCLUDE` · 2 `REGISTERED` · 2 `UNCERTAIN`**.

**The five Revelation rows that moved `INCLUDE` → `INGESTED` at `260835-25`**, named individually because the register's update was recorded as owed precisely for them:

| Video ID | Session as titled | Line |
|---|---|---:|
| `nOSaF0BWS2Y` | Session IX: the Beast and the Bottomless Pit | L389 |
| `ADQnOyBaSRk` | Session X: the Woman, the Child, and the Dragon | L388 |
| `M71-SrYEoEQ` | Session XI: The Two Beasts and the Mark | L387 |
| `nGfY6_P5m5o` | Session XV: The Whore and the Beast (Ch 17-18) | L385 |
| `lJo0WgP37rs` | Session XVI: The Marriage Supper of the Lamb | L384 |

⚠️⚠️ **Two limits carried forward rather than quietly dropped, because a fully-triaged channel is not a fully-mined one:**

1. **Revelation 14 and 16 are covered by NO video and NO transcript** (the channel's missing Sessions XII and XIV) — a **permanent corpus gap**, not a pending item.
2. **`RV-S15` cannot be completed by a re-pull — the video itself is truncated** (`260835-25` correcting `260835-24`).

Also carried: **`GeWfXTAjFDo` (`File 63`, ch 20) remains REGISTERED but UNMINED** — it counts toward the 62 as a decision cell, but it is not coverage of the chapter.

⚠️ **A numbering defect found and flagged, not retro-filled:** the file's stamp read `260835-21` but its changelog runs `v1.0 — 260835-9` and stops — **the `260835-21` update bumped the stamp without writing a changelog entry.** This pass's entry is therefore **`v1.1`, not `v1.2`**, with the gap recorded. ⛔ **This pass did not do the `260835-21` work and will not reconstruct its account of itself.**

## What Part B adds to the pull queue

**Ten office rows await a pull:** the five returned here, plus the five `UNCERTAIN` office rows pull-marked at `260835-25` (`FaWyhA4iB3U`, `VvkxFsykeyc`, `H1H9CO8mF8c`, `ZkVlWb852NY`, `AawVFH69H0E`). ⛔ **Expected yield recorded as LOW in advance on every one.** ⛔ **Nothing downloaded, nothing transcribed.**

---

## Validator AFTER, against baseline

| | Gate | After |
|---|---|---|
| ok | 82 | **81** |
| warnings | 9 | **10** |
| errors | 0 | ✅ **0** |
| **total checks** | **91** | **91** |

⭐ **The delta is exactly one check moving `ok` → `warn`, and it is expected, correct, and caused by this pass's own mint:**

> `WARN [C11] outline last checked against DQ-24 (260835-2); the DQ ledger now runs to DQ-25. 1 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.`

⛔ **This is the validator working as designed.** Minting `DQ-25` creates real, reportable drift against `Incense_Conversational_Outline.md`, which the brief **expressly forbade touching**. The warning is **reported, not suppressed**, and the outline was not opened. **The other nine codes are unchanged from gate, verbatim.**

### ⚠️ One error was introduced mid-pass and fixed; recorded rather than hidden

An intermediate run returned **`80 ok · 10 warnings · 1 errors`**:

> `ERROR [C8] DANGLING VP- LABELS cited but never DEFINED …: {'VP-8': ['PROJECT_STATE.md']}`

**Cause, diagnosed rather than guessed:** `C8`'s VP- arm excludes a mention when `NEXT_FREE_MARK = re.compile(r'next free', re.I)` matches **the same line**. This pass's new pass-note line wrote **"next-free values"** with a hyphen, which the pattern does not match, so a routine next-free *mention* of `VP-8` was scored as a *citation*. **Fixed by writing "next free" unhyphenated**, matching the form every prior `PROJECT_STATE.md` next-free line already uses. ⛔ **No validator code was changed and no `VP-` label was created or altered.**

⚠️ **Worth knowing for future passes:** the corpus's own house style favours the hyphenated *"next-free"*, but `C8` only recognises the unhyphenated form. **A next-free line naming a `VP-` number must be written "next free" or it trips a false `C8` error.** Recorded here rather than left to be rediscovered.

---

## Files touched

```
 M ORCHESTRATION.md          +77  -1
 M PROJECT_STATE.md          +44 -10
 M SRC_Channel_Inventory.md   +7  -7
 M SRC_Coverage_Register.md  +37  -1
 M SRC_Manifest.md            +7  -7
 M St_Francis_EMC_Distinctives.md +23 -1
 M src/SRC_Discord_RPW.md    +23  -0
```

| File | What changed |
|---|---|
| `src/SRC_Discord_RPW.md` | 3 posts appended (35-37); one changelog entry. **Pure append — no prior byte changed, so every offset logged against messages 1-34 still holds.** |
| `SRC_Manifest.md` | RPW row: SHA-256 `6bbcfbe2…` → `3c3acda5…`, size 58,506 → 68,549, lines 360 → 383, coverage → 2026-08-28, export history; fifth capture defect registered; stamp bumped. Prior values retained. |
| `St_Francis_EMC_Distinctives.md` | `DQ-25` minted; dated notes at `OQ20` and `OQ21`; stamp bumped. |
| `SRC_Channel_Inventory.md` | 5 cells reclassified `DECLINED-office` → `INCLUDE`; 1 dated note on `8gb4BXlfLO4`; stamp bumped. |
| `ORCHESTRATION.md` | §8 case 1 amended; original text and `260835-25` flag both retained verbatim and marked superseded; stamp bumped. |
| `SRC_Coverage_Register.md` | Dated notes at §2 and §3; `v1.1` changelog entry; stamp bumped. |
| `PROJECT_STATE.md` | Gate block; pass note; `DQ` next-free `DQ-25` → `DQ-26`; posted-awaiting row (was **stale**); four registry rows; stamp bumped. |

## ⛔ Deliberately not touched

`Incense_Conversational_Outline.md` · `RJ_Incense_Analysis.md` (both named off-limits by the brief) · `src/SRC_Discord_RPW-raw.txt` (JD's capture artifact — the missing capture line is **flagged, not repaired**) · `RJ_Final_Question_List.md` · `RJ_Open_Questions_and_Divergences.md` · `validate_project.py` · every other `SRC_Manifest.md` row.

## ⛔ Nothing minted but `DQ-25`

No `File`, `IP`, `LS`, `RV`, `BLOG`, `POD`, `VP`, `DELTA`, `EXT`, `W`, `GV`, `RC` or `BP` number consumed. Next free values re-derived, not copied: **`DQ-26`**, `IP-109`, `LS-130`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EXT-4`, `W47`, `File 72`.

`DQ-9` unmoved · `DQ-24` untouched · `IP-84` confirmed and not extended · no existing finding altered, renumbered or re-pointed · no byte offset in any existing entry altered · nothing downloaded or transcribed · **nothing drafted, altered, or posted to Rev. James.**

---

## Owed / carried forward

- ⏳ **Restore the `CAPTURED …` line to `src/SRC_Discord_RPW-raw.txt`** on the next capture — **JD's action**, not a session's.
- ⏳ **`OQ21` is the live unanswered item on the RPW thread** — asked twice, answered zero times. Both channel turns are JD's; the next posted question is a sequencing decision across two channels. ⛔ Nothing drafted.
- ⏳ **`OQ20`'s date-floor half** remains open; none of its three candidate readings chosen.
- ⏳ **C11 DQ-arm drift** (`DQ-25` unreviewed against the outline) — reported, and the outline deliberately not opened.
- ⏳ **Ten office rows queued for a pull**, expected yield LOW, read-aloud layer required.
- ⏳ **`SRC_Coverage_Register.md`'s missing `v1.1` entry for `260835-21`** — flagged, not retro-filled.
- ⏳ The pre-existing nine warnings are all unchanged from gate and none were addressed by this pass.

---

## Commit plan — nothing committed by this pass

`git --no-optional-locks status --short` after all edits:

```
 M ORCHESTRATION.md
 M PROJECT_STATE.md
 M SRC_Channel_Inventory.md
 M SRC_Coverage_Register.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
 M src/SRC_Discord_RPW.md
```

Plus untracked, once written: `passes/260835-26_rpw-recapture-dq25-and-office-rule-ruling_close-out.md` and `passes/260835-26_rpw-recapture-dq25-and-office-rule-ruling.diff`.

**Per the brief, in two commits:**

1. **`passes/` first** — stage the two new artifacts above only.
2. **The corpus edits separately** — stage the seven modified files listed above.
