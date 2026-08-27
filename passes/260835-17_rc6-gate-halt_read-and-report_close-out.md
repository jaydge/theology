# 260835-17 — RC-6 registration pass HALTED AT GATE (read-and-report)

**Stamp: 260835-17** (derived fresh by grep over all `*.md`; `260835-16` is **already consumed in the working tree** — see §1)
**Date: 2026-08-27**
**Mode: read-and-report. NOTHING EDITED. NOTHING STAGED. NOTHING COMMITTED. NO NUMBER OF ANY KIND MINTED — no `File`, no finding, no `RC`, no `LS`/`IP`/`RV`/`DQ`/`GV`/`BP`/`EXT`/`W`.**

⛔⛔ **THIS IS NOT THE COMMISSIONED REGISTRATION PASS.** The commissioned pass was not performed. This document records why, and records the independent verification work that is useful to JD whichever way he rules.

---

## 1. ⛔⛔ THE GATE FAILED — AN UNCOMMITTED, INCOMPLETE `260835-16` PASS IS ALREADY IN THE WORKING TREE

`git status --short`, captured before any edit (and no edit was subsequently made):

```
 M SRC_Channel_Inventory.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
```

`git --no-optional-locks status --short --untracked-files=all` returns the same three lines and **no untracked files.**

⛔⛔ **Those three modifications are a substantially-executed version of the very pass this brief commissions, stamped `260835-16`, uncommitted, and INCOMPLETE.** It registers `File 64`, records JD's single-file ear warrant, corrects the 2023→2022-07-30 dating, and retro-verifies `RC6-1`…`RC6-4` with byte ranges — i.e. Tasks 1, 2 and 3 of this brief, already done by something that is not this session.

**`ORCHESTRATION.md` §1 is explicit:** *"One thread touching this repo at a time. Parallel threads editing the same files have caused real collisions."*

**`CLAUDE.md` §Emission discipline is explicit:** *"If a pass is interrupted before it finishes … say so explicitly, name every file still owed, and do not commit a partial set. **Re-run the pass whole rather than resuming mid-stream.**"*

⛔ **Re-running whole requires reverting the working tree, which would discard uncommitted work. That is JD's call, not a delegated pass's.** Proceeding on top of it would have produced either a duplicate registration or a silent merge of two passes — the exact `260832-5`-shape collision the project has already paid for twice today.

### 1.1 What the in-flight `260835-16` covers, and what it still owes

| Brief task | In-flight `260835-16` state |
|---|---|
| Task 1 — register as new File | ✅ `File 64` registered in `SRC_Manifest.md`, full row + provenance block |
| Task 1 — ear warrant, scoped to one file | ✅ recorded, with explicit three-point reasoning for **not** folding into the `260835-15` six-file group |
| Task 2 — date correction, `St_Francis_EMC_Distinctives.md` | ✅ dated notes at L363-364 **and** at the `RC-1…RC-7` table row |
| Task 2 — date correction, `SRC_Manifest.md` | ✅ dated note beside the `RC-6 HAS NO SUBSTRATE` heading |
| Task 2 — date correction, `PROJECT_STATE.md` | ⛔⛔ **NOT DONE. FILE NOT MODIFIED.** L35 still reads *"`RC-6` (…, 2023) IS NOT IN THE PULL AND STILL HAS NO SUBSTRATE"* |
| Task 2 — date correction, `RJ_Final_Question_List.md` | ⛔ **NOT DONE. FILE NOT MODIFIED.** |
| Task 3 — retro-verify `RC6-1`…`RC6-4` | ✅ all four, with byte ranges — but see §3 for three defects |
| `SRC_Channel_Inventory.md` decision cell | ✅ `INCLUDE` → `INGESTED (source registered) — File 64` |
| Pass artifacts in `passes/` | ⛔⛔ **NOT WRITTEN.** `passes/260835-16_rc6-recovery-and-retro-verification_close-out.md` **does not exist**, though `SRC_Channel_Inventory.md`'s new text cites it by name |
| `PROJECT_STATE.md` §4 registry cells / stamp | ⛔⛔ **NOT BUMPED.** `PROJECT_STATE.md` still stamped `260835-15` while three registered documents it governs are stamped `260835-16` |

⛔⛔ **THE LAST ROW IS THE SERIOUS ONE.** A stale `PROJECT_STATE.md` sitting beside documents whose stamps have already been bumped **is, verbatim, the failure mode `CLAUDE.md` §Emission discipline exists to prevent** — *"No single check could diagnose it, because the stale file was the one doing the checking."* The tree is currently in exactly that state.

### 1.2 ⛔ A FALSE CLAIM INSIDE THE UNCOMMITTED TEXT

`SRC_Channel_Inventory.md`'s new `jTNqBnhO8A8` cell asserts the dating error was *"corrected as a dated note in all three"* (naming `St_Francis_EMC_Distinctives.md`, `PROJECT_STATE.md`, `SRC_Manifest.md`). **`PROJECT_STATE.md` was never touched.** The claim is false as the tree stands. It would become true if the pass were completed; it is false if the pass is committed as-is.

---

## 2. GATE READINGS (all captured before any edit; no edit made)

- **`git --no-optional-locks rev-parse HEAD`** → `ed7e76ad5e710f64a0b652d25bbabc7943905a57`
- **`PROJECT_STATE.md` stamp** → `260835-15`
- **Next-free pass stamp, derived fresh by grep** (`grep -rhoE '26083[0-9]-[0-9]+' --include='*.md' .`) → **`260835-17`**. ⚠️ **NOT `260835-16` — that stamp is live in the uncommitted tree.** This is the third stamp collision today and the first one the fresh-grep instruction actually caught before it landed.
- **Next-free `File` number, derived fresh by grep** → ⚠️ **ambiguous by exactly the same cause.** `grep -rhoE 'File 6[0-9]'` returns `File 60`…`File 65`. `File 64` and `File 65` exist **only inside the uncommitted `260835-16` text** (64 = the new registration, 65 = its "next free" declaration). **Against committed `HEAD`, next-free is `File 64`. Against the working tree, next-free is `File 65`.** Which is correct depends entirely on JD's ruling in §5.
- **Validator, `python3 validate_project.py`** → **82 ok · 9 warnings · 0 errors.** Coverage summary read, not just the count: C1 6 files, C2 3, C3 24, C4 22, C5 2, C6 6, C7 2 (WARN-only, suspended), C8 22, C9 1, C10 1, C11 2, C12 2. No check examined zero files. **Firing codes: none — 0 errors.** The 9 warnings are the pre-existing standing set; **the validator does not catch the stale-`PROJECT_STATE.md` condition in §1.1, which is the point `CLAUDE.md` makes about it.**

---

## 3. INDEPENDENT VERIFICATION OF THE SOURCE AND OF THE IN-FLIGHT WORK

Done because it is useful to JD under either ruling, and because the in-flight text's load-bearing claims were never independently checked by anything.

### 3.1 ✅ Registration facts — ALL CONFIRMED

Computed fresh from `~/EMC/original transcripts/video transcripts/batch10/`, not copied from `-meta.json`, then cross-checked against it:

| Fact | Value | Agrees with in-flight text |
|---|---|---|
| `-transcript.txt` sha256 | `28e68c81bf97de4c0bb3e6e36c7eb29cac707ff29b588ac9a73adf7da09eec22` | ✅ |
| bytes | 4,666 | ✅ |
| sentences | 66 | ✅ |
| speaker labels | **66/66 = `A`**; `speakers_detected: ['A']` | ✅ |
| video id | `jTNqBnhO8A8` | ✅ |
| upload_date | **2022-07-30** (`upload_date_raw 20220730`, `release_date 20220730`) | ✅ |
| duration | 362 s | ✅ |
| channel | `Barely Protestant (Fr James)`, `UCWrx0o3G0laSrpOMuApxTMg` | ✅ |
| audio sha256 | `d139bee3eec43b5d98bea9797742d544b969f5f0111bc8f4d49cbe3d53ba03c3` — a distinct object from the transcript hash | ✅ |
| keyterms | `keyterms_count: 61`, sourced from `asr_keyterms_A101.md` | ✅ — the `key terms loaded: N` check `ORCHESTRATION.md` §6 warns about is satisfied |
| `was_live` | `False` / `not_live` | — |

⭐ **The 2022-07-30 date is confirmed by three mutually independent routes:** `-meta.json` (yt-dlp, this pull) · `SRC_Channel_Inventory.md`'s pre-existing row (the live channel-metadata scrape, which already carried `2022-07-30` before any of this) · and the live YouTube page metadata read at the identity step (`uploadDate 2022-07-30T10:51:02-07:00`, `duration PT6M2S` = 362 s). **The corpus's "2023" is wrong. That part of the brief is correct and is confirmed here independently of the in-flight edit.**

### 3.2 Byte ranges — verified individually with `grep -obiF`

| Finding | In-flight claim | Verified offset | Verdict |
|---|---|---|---|
| `RC6-1` Theotokos | @1,794-1,863 | **@1,794**, extracting exactly *"In giving birth to Jesus, she gave birth to God, because Jesus is God"* | ✅ **exact** |
| `RC6-1`/`RC6-3` Nestorian | @2,324-2,340 | *"the Nestorian heresy"* begins **@2,320** | ⚠️ off by 4 |
| `RC6-3` Arian | @3,519-3,535 | *"We're not Arians"* **@3,519** | ✅ **exact** |
| `RC6-2` elevation clause | @1,246-1,298 | *"That elevate the Blessed Virgin"* begins **@1,241** | ⚠️ off by 5 |
| `RC6-2` divinization | @1,104-1,129 | *"divinization"* **@1,117**; @1,104 is leading context | ✅ acceptable as a range |
| `RC6-4` opening self-styling | @0-17 | **@0** — *"I am Father James"* | ✅ **exact** |
| `RC6-4` closing self-styling | **@5,347-5,382** | ⛔⛔ **BEYOND EOF — THE FILE IS 4,666 BYTES.** The real closing is **@4,586**: *"Again, this is Father James, and please keep me in prayer as I travel. Blessings. Amen."* | ⛔ **HARD ERROR** |

⛔ **The `@5,347-5,382` citation cannot be verified because it cannot exist.** Under `CLAUDE.md`'s rule that a logged byte offset is verified before being trusted, that citation must not ship. The finding it supports is fine — the quote is real at @4,586 — but the locator is wrong.

### 3.3 ✅ Silence check — CONFIRMED, and it is the strongest result here

`St_Francis_EMC_Distinctives.md` L1280 claims RC-6 is *"Silent on the Immaculate Conception, Assumption, perpetual virginity, and invocation."* Checked against the raw bytes (single-line file, so a zero line-match is a true zero):

`immaculate` **0** · `assumption` **0** · `perpetual virgin` **0** · `invocation` **0** · `invoke` **0** · `rosary` **0** · `dulia` **0** · `intercession` **0** · `saints` **0**

✅ **The corpus's silence claim is exactly right.** This also holds `St_Francis_EMC_Distinctives.md` L1368's *"the corpus holds NOTHING current on the Assumption"* and keeps Open Questions item 4 open as written.

### 3.4 ⛔⛔ THE SECOND-WITNESS CLAIM IN THE IN-FLIGHT TEXT IS NOT SUPPORTED — THE TWO RENDERINGS DIVERGE AT THE LOAD-BEARING POINT

The uncommitted `SRC_Manifest.md` block asserts the `-youtube.srt` rendering *"matches the AssemblyAI wording at both points, with only disfluency-level differences … no substantive divergence between the two renderings."* **Checked directly. That is false at the point that matters most.**

| Point | AssemblyAI | YouTube captions | |
|---|---|---|---|
| `RC6-2` key word | *"as some sort of **divinization** of um the Blessed Virgin Mary"* | *"as some sort of **demonization** of the blessed virgin mary"* — `divinizat` = **0** in the YouTube rendering | ⛔ **DIVERGENT** |
| `RC6-2` elevation clause | *"That elevate the Blessed Virgin higher than she should be"* | *"that elevate the most virgin iron she should"* — garbled | ⛔ **DIVERGENT** |
| `RC6-1` Theotokos | *"In giving birth to Jesus, she gave birth to God, because Jesus is God"* | *"in giving birth to jesus she gave birth to god because jesus is god"* | ✅ **matches** |
| `RC6-3` Arian | *"We're not Arians"* | *"we're not arians"* | ✅ **matches** |
| `RC6-4` channel name | *"this is **Barely** Protestant on the road"* | *"this is **merely** protestant on the road"* | ⚠️ divergent, but **both names are attested for this channel** in the corpus (*"Barely / Merely Protestant"*, `St_Francis_EMC_Distinctives.md` L391) — likely not an error in either |

⛔⛔ **`CLAUDE.md` §Source handling, dual-ASR protocol, governs and is not satisfied:** *"agreement gives only PROVISIONAL confidence … divergence goes to a verification queue resolved **by ear against the audio**, never against the second transcript. Neither transcript is authoritative on wording alone."*

⏳ **EAR-CHECK OWED (call it E3), and `RC6-2`'s resolution depends on it.** Context (*"as some sort of ___ of the Blessed Virgin Mary. This is not what it is"*) makes **divinization** overwhelmingly the likelier spoken word and **demonization** the garble — but that is an inference from sense, and the protocol forbids settling it by preferring one transcript. **JD is the only one who can close this, in ~10 seconds, at 1:27-1:41.**

### 3.5 `RC6-2` — the corpus's "veneration" is NOT in the source. Flagged, not resolved.

`St_Francis_EMC_Distinctives.md` L1280 quotes RJ as fencing Theotokos against *"not … some sort of" veneration*. ⛔ **`venerat` = 0 occurrences in the AssemblyAI transcript AND 0 in the independent YouTube captions.** The word is not spoken in either rendering.

The in-flight text catches this and flags it correctly — that judgement is sound and I confirm it. ⚠️ **But its proposed replacement, "divinization," is precisely the word §3.4 shows to be single-source and unconfirmed.** So `RC6-2` is currently **less settled than the in-flight text presents it**: the corpus's word is wrong, and the replacement is not yet verified.

⛔ **Not resolved here, per the `GV-4` precedent. Both readings stay live.** The substance of the finding — that he fences the title against improper Marian elevation — is **not** in doubt; it is independently carried by the elevation clause, which both renderings attest in substance even where the YouTube one garbles it.

### 3.6 ⭐ ASR quirk worth registering — `Theotokos`

The YouTube captions render **Theotokos** as ***"fel cocos"***. Same shape as the already-registered `Lateran` → *"lad ladan"* and `Charlie Kirk` → *"Charlie Park"* quirks. ⚠️ **A future term-scan for `Theotokos` across YouTube-caption renderings will return false zeroes.** Worth a line in `SRC_Manifest.md` beside the other two quirks — **not added here, because this pass edits nothing.**

### 3.7 ⭐ Solo-speaker: confirmed, and the `260835-15` warrant-class check was actually run

Per `ORCHESTRATION.md` §8, a single label is **not by itself** a single-voice warrant; the file's own content must be checked for participant-address markers. **Run here:** no name spoken to, no answer in another voice, no call-response exchange, no closing address to another person. The closing is *"please keep me in prayer as I travel. Blessings. Amen."* — self-addressed to an audience, not to a participant. ✅ **`File 64` qualifies as SINGLE-VOICE, CONFIRMED — the strongest tier** — on three independent legs: JD's ear verification of the full 6:02, AssemblyAI's `['A']`, and this content check.

⭐ **The in-flight text's refusal to fold this into the `260835-15` six-file warrant is correct and its three-point reasoning is sound** — the six-file warrant is a closed dated ruling about a named set, `File 64` was not in the `260835-11` pull, and that warrant's own scope limit expressly excludes *"any future recovery pull."* **Whatever JD rules in §5, that reasoning should survive into whatever lands.**

---

## 4. INCENSE AND ICONS — STANDING INSTRUCTION, REPORTED AS A CONFIRMED ZERO

Per `ORCHESTRATION.md` §8, reported explicitly even when nil. Checked across `File 64`'s full 4,666 bytes: **`incense` 0 · `icon` 0 · `image` 0 · `altar` 0 · `thurible` 0 · `censer` 0.** ⛔ **Confirmed zero.** RC-6 is 6 minutes on the Theotokos title and contributes nothing to the incense or iconography funnels.

---

## 5. ⏳ WHAT IS OWED — JD'S RULING, THREE OPTIONS

⛔ **Nothing is staged. Nothing is committed. No file was edited by this session.**

**Option A — complete the in-flight `260835-16` rather than re-run it.** Keep the three modified files, then add: the `PROJECT_STATE.md` date correction and §4 registry bumps, the `RJ_Final_Question_List.md` date correction, the two `passes/260835-16_*` artifacts, the `@5,347-5,382` → `@4,586` locator fix, the two small offset drifts (§3.2), the §1.2 false "all three" claim, and the §3.4 second-witness retraction. ⚠️ **Contradicts `CLAUDE.md`'s "re-run whole rather than resuming mid-stream" — but that rule was written against a partial *download*, and here the partial state is fully visible and diffable, which is the condition the rule assumed absent.** Cheapest, and the in-flight work is mostly sound.

**Option B — revert and re-run whole at `260835-17`.** `git checkout -- SRC_Channel_Inventory.md SRC_Manifest.md St_Francis_EMC_Distinctives.md`, then re-run clean. ⛔⛔ **This DISCARDS the uncommitted `260835-16` work, which is not recoverable afterward.** Literal compliance with the emission-discipline rule. ⛔ **A delegated pass must not do this on its own judgement — it needs JD's explicit instruction naming these three files.**

**Option C — stash and decide later.** `git stash push -u -m "260835-16 in-flight RC-6 pass"`. Preserves the work, clears the tree, defers the ruling. Safest if the origin of the `260835-16` edits is unknown.

⚠️⚠️ **BEFORE ANY OF THE THREE: establish where the `260835-16` edits came from.** If another thread or Cowork task is still live against this repo, that must be stopped first, or the collision simply repeats — `ORCHESTRATION.md` §1. **This session did not create them and cannot account for them.**

⛔ **Also unresolved and not this pass's to settle:** the next-free `File` number is `File 64` against `HEAD` and `File 65` against the working tree (§2). **It resolves itself once JD rules, and not before.**

---

## 6. WHAT WAS CHECKED AND CAME BACK EMPTY, OR WAS DECLINED

- **Declined:** every edit in the brief — Tasks 1, 2, 3, the inventory cell, and the `passes/` pass artifact proper. Reason: §1.
- **Declined:** reverting, stashing, or otherwise clearing the working tree. Reason: discards uncommitted work; JD's call.
- **Declined:** re-deriving the identity of `jTNqBnhO8A8`, per the brief's instruction. ⭐ **Though noted: `-meta.json`'s title, video id, duration and upload date all independently corroborate it anyway, at no cost.**
- **Not touched, per the brief:** `Incense_Conversational_Outline.md`, `RJ_Incense_Analysis.md`. Confirmed unmodified in `git status`.
- **Nothing drafted, altered, or posted to Rev. James.** No question drafted. No gate moved. No channel state changed.
- **Came back empty:** the incense/icon sweep (§4) · `venerat` in both renderings (§3.5) · all nine Marian-silence terms (§3.3) · `passes/260835-16_*` (does not exist, though cited by name in the uncommitted inventory text).
- **Could not be resolved by any means available to a delegated pass:** ear-check E3 (§3.4). Requires JD and the audio.

---

## 7. VALIDATOR, AFTER

⛔ **Not re-run against a changed tree, because the tree is unchanged by this session.** The §2 reading — **82 ok · 9 warnings · 0 errors** — is both the before and the after. It is **not** a clean bill of health for the tree: it is a clean run over a tree that contains an incomplete pass the validator has no check for.
