# 260835-16 — `RC-6` REGISTRATION AND RETRO-VERIFICATION

**Pass stamp:** `260835-16` · **Date:** 2026-08-27 · **Type:** registration + retro-verification + date correction. Corrects and registers.

---

## 0. GATE

| Item | Value |
|---|---|
| `git rev-parse HEAD` (start) | `ed7e76ad5e710f64a0b652d25bbabc7943905a57` · branch `main` |
| `git --no-optional-locks status --short` before first edit | **NOT EMPTY** — one untracked file, `passes/260835-17_rc6-gate-halt_read-and-report_close-out.md`. Per instruction, this pass **stopped and reported** rather than editing around it. |
| What that file was | A read-and-report close-out from an earlier, duplicate run of this same delegated task. It found an uncommitted, incomplete `260835-16` pass already in the working tree (three modified files, containing a real defect — a false claim that AssemblyAI and YouTube's captions agree on `RC6-2`'s disputed word, when they diverge) and correctly halted rather than building on it, laying out three options for JD (complete in place / revert and redo whole / stash). |
| Resolution | JD confirmed the revert (`git checkout -- SRC_Channel_Inventory.md SRC_Manifest.md St_Francis_EMC_Distinctives.md`) was his own instruction, given the defect and the halt report's own "re-run whole" precedent. `260835-16` is retired as a label for that discarded work; JD ruled the stamp is genuinely free to reuse since nothing real exists under it. The halt report itself is left untouched, per never-alter — it is a legitimate record of real work, not an error. |
| Independent re-verification of that resolution (not taken on trust) | `grep -rn "260835-16" --include='*.md' .` (excluding the halt report's own prose) returned **zero matches**. `git --no-optional-locks diff --stat HEAD -- SRC_Manifest.md SRC_Channel_Inventory.md St_Francis_EMC_Distinctives.md PROJECT_STATE.md RJ_Final_Question_List.md` returned **empty**. Only then was `260835-16` treated as free. |
| Validator BEFORE | **`82 ok · 9 warnings · 0 errors`** — the standing 9, none new. |
| `PROJECT_STATE.md`'s own stamp at gate | `260835-15` |
| Next-free pass stamp | `260835-16` — re-derived fresh by grep, confirmed genuinely free (above), not carried from any number cited in the brief |
| Next-free `File` number | `File 64` — re-derived fresh by grep against live content (`grep -rhoE 'File 6[0-9]'`); `File 65` appears only inside the halt report's own prose describing the reverted work |

---

## 1. TASK 1 — REGISTRATION. `File 64`

⭐ **Hash, byte count and source-video metadata computed fresh this pass**, independently, with `hashlib.sha256` / raw byte count over `IsMaryTheMotherOfGod-transcript.txt`, cross-checked against (not copied from) `-meta.json`.

| File | Filename | SHA-256 (raw bytes) | Bytes | Video ID | Title | Upload | Dur (s) | Speakers | Batch |
|---|---|---|---|---|---|---|---|---|---|
| **File 64** | `IsMaryTheMotherOfGod-transcript.txt` | `28e68c81bf97de4c0bb3e6e36c7eb29cac707ff29b588ac9a73adf7da09eec22` | 4,666 | `jTNqBnhO8A8` | Is Mary the Mother of God? | **2022-07-30** | 362 | `['A']` (66/66 sentences) | **`RC-6`** |

Identity: `jTNqBnhO8A8` confirmed by exact unique title match across all 368 `SRC_Channel_Inventory.md` rows, independently reconfirmed against live YouTube metadata (per the brief; not re-derived, per instruction — though `-meta.json`'s title, video ID, duration and upload date all independently corroborate it anyway, at no extra cost).

**Provenance:** channel *Barely Protestant (Fr James)*, `UCWrx0o3G0laSrpOMuApxTMg` — same as `File 47`-`File 55`. ASR: AssemblyAI `universal-3-5-pro`/`universal-2`, `en`, `disfluencies: true`, `speaker_labels: true`, 61 keyterms from `asr_keyterms_A101.md`. Audio via `yt-dlp 2026.08.19`, 64k/16kHz/mono; audio SHA-256 `d139bee3eec43b5d98bea9797742d544b969f5f0111bc8f4d49cbe3d53ba03c3` (2,957,585 B — a distinct object from the transcript hash). Carries a `-youtube.srt` independent second rendering. Transcript held OUTSIDE the repo, at `~/EMC/original transcripts/video transcripts/batch10/`.

### 1.1 Human-verification warrant — scoped, and kept separate from the six-file class

JD manually verified by ear, having watched the full 6:02, that `File 64` is single-speaker, Rev. James only. AssemblyAI auto-detect independently returned `speakers_detected: ['A']` for all 66 sentences (confirmed independently: a Python read of `-sentences.json` shows a single unique speaker value across all 66 entries).

**Deliberately NOT folded into the `260835-11`/`260835-15` six-file warrant class**, for three reasons: (1) that warrant is a closed, dated ruling naming a specific set of files (`File 47`, `48`, `50`, `51`, `54`, `55`); `File 64` was not among them. (2) `260835-11`'s own scope limit explicitly excludes *"any future recovery pull"* — this is exactly that. (3) Per `ORCHESTRATION.md` §8, a single label is not by itself a single-voice warrant; `File 64`'s own content was checked independently for participant-address markers (no name spoken to, no answer in another voice, no call-response, self-addressed closing) and passes on that separate ground too. `File 64` is single-voice, confirmed, on three independent legs.

---

## 2. TASK 2 — DATE CORRECTION: `RC-6` IS 2022-07-30, NOT 2023

The corpus's "2023" dating of `RC-6` was a legacy guess from a vanished chat-thread paste, never checked against real data — the same error shape as `POD-1`/`POD-12`'s date error on `BP-13`/`BP-15` (`260835-11` §5.2).

**Confirmed three independent ways:** `-meta.json` (`upload_date_raw 20220730`, `release_date 20220730`); `SRC_Channel_Inventory.md`'s own pre-existing channel-metadata-scrape row for this video (already `2022-07-30`, unrelated to this pull); and live YouTube page metadata read at the identity step (`uploadDate 2022-07-30T10:51:02-07:00`, `duration PT6M2S` = 362s, matching exactly).

**Corrected as dated notes, none as silent rewrites, at:**
- `St_Francis_EMC_Distinctives.md` — L363 (main dating paragraph, full correction), the L391 summary table row, L429 (biography composite — downstream effect on the *"self-styles Father James by 2023"* attestation flagged), L1280 (Marian-restraint bullet — date + wording, see §3 below), L1368 (Assumption-absence bullet), the L7067 source-map table row, and the L7071-adjacent "still has no substrate" note (superseded, not deleted).
- `SRC_Manifest.md` — the `RC-6 HAS NO SUBSTRATE` section (superseded by the new `File 64` block, old text untouched) plus the top-line changelog.
- `PROJECT_STATE.md` — new top-of-file GATE/PASS NOTE block (the file's own append-log convention; the stale `260835-11` block at L33-35 is left exactly as written, per never-alter).
- `RJ_Final_Question_List.md` — **searched, and the "2023" figure does NOT occur there in connection with `RC-6`.** The brief's premise that the error "propagated" to this file is not confirmed by the file's actual content. Recorded rather than silently acted on; a light dated note was still added at the file's Q16/item-16 entry for context (date + `RC6-2` wording), since that entry cites `RC6-1`/`RC6-2` directly, even though there was no date error there to fix.

**Downstream effect, flagged not resolved:** `St_Francis_EMC_Distinctives.md` L429 and L7212 both use "self-styles Father James by 2023" as a lagging indicator bounding the priesting-date bracket at "roughly 2021 and 2023." With the correct date (2022-07-30), that attestation moves a year earlier. Whether this narrows the bracket is not this pass's to decide, and is noted rather than adjudicated.

---

## 3. TASK 3 — RETRO-VERIFICATION, `RC6-1`…`RC6-4`

Method: locate each finding's anchor phrase by exact-string search over the raw bytes of `File 64`, verify the byte range against the actual file length (4,666 B), cross-check against the independent `-youtube.srt` rendering.

| Finding | Byte range | Anchor | Status |
|---|---|---|---|
| `RC6-1` (Theotokos) | 1,794–1,863 | *"In giving birth to Jesus, she gave birth to God, because Jesus is God"* | ✅ VERIFIED, exact |
| `RC6-1`/`RC6-3` (Nestorian) | 2,320–2,340 | *"the Nestorian heresy"* | ✅ VERIFIED — corrects a stale @2,324-2,340 (off by 4) |
| `RC6-3` (Arian) | 3,519–3,535 | *"We're not Arians"* | ✅ VERIFIED, exact |
| `RC6-4` (opening) | 0–17 | *"I am Father James"* | ✅ VERIFIED, exact |
| `RC6-4` (closing) | 4,579–4,666 (= EOF) | *"Again, this is Father James, and please keep me in prayer as I travel. Blessings. Amen."* | ✅ VERIFIED — corrects a stale @5,347-5,382 (**beyond EOF, could not have existed**), and also corrects the earlier halted pass's own re-derivation of @4,586 (itself 7 bytes off) |
| `RC6-2` (elevation clause) | 1,241–1,298 | *"That elevate the Blessed Virgin higher than she should be"* | ✅ VERIFIED — corrects a stale @1,246-1,298 (off by 5) |
| `RC6-2` (disputed word) | 1,101–1,184 (word @1,117-1,129) | *"as some sort of divinization of um the Blessed Virgin Mary. This is not what it is."* | ✅✅ RESOLVED, see §4 |

⭐ **Every offset above was independently checked by this pass with both `grep -aobiF` and a Python `bytes.find()`, cross-confirming each other**, rather than trusted from the brief or from the earlier halted pass's own report — which is why the two small drifts and the one earlier pass's own re-derivation error were caught.

**Zero-checks, both renderings:**
- Silence (per corpus claim): `immaculate` 0 · `assumption` 0 · `perpetual virgin` 0 · `invocation` 0 · `invoke` 0 · `rosary` 0 · `dulia` 0 · `intercession` 0 · `saints` 0. **Corpus's silence claim confirmed exactly.**
- Incense/icon (per standing instruction, reported though nil): `incense` 0 · `icon` 0 · `image` 0 · `altar` 0 · `thurible` 0 · `censer` 0.
- Bonus closure: `RC1-10`'s Homilies-disagreement search (`260835-11` Flag B2, *"if it exists it is in RC-6"*) was re-run against `File 64` now that it exists — `Homil`/`homil` = 0 there too, both renderings. `RC1-10` remains NOT FOUND anywhere in the corpus; the one remaining place it could have been hiding is now closed. Dated note added at the flag.

**ASR quirks registered** (same class as `Theotokos`→"fel cocos" already known, and `File 49`'s Charlie Kirk→"Charlie Park"):
- YouTube captions render *Theotokos* as *"fel cocos"*.
- YouTube captions render *"the Nestorian heresy"* as *"the story in heresy"* (`nestorian` = 0 in that rendering).

---

## 4. `RC6-2` — RESOLVED ON JD'S EAR-CHECK, WITH AN ATTRIBUTION CORRECTION

AssemblyAI and YouTube's captions disagreed on one word at 1:27-1:41: AssemblyAI "divinization," YouTube "demonization." Per the dual-ASR protocol, this was not resolved by preferring either transcript — this pass stopped and asked. **JD listened and confirmed: the word is "divinization."** YouTube's "demonization" is a caption garble, in an already heavily-garbled stretch of that rendering (`Theotokos` → "fel cocos" two sentences earlier in the same captions; `Nestorian` → "story in" later in the file) — noted as context, not as the basis for resolving it before JD's answer arrived.

⚠️ **The attribution needed correcting too, not just the word, and JD flagged this himself.** Re-reading the full clause: *"a lot of people will misunderstand this term… as some sort of divinization of um the Blessed Virgin Mary. **This is not what it is.**"* Rev. James is **naming and rejecting a misreading** other people fall into — not stating his own affirmed description of Mary. He then separately grants, in the next sentence, that *"people haven't used it in ways that elevate the Blessed Virgin higher than she should be"* — a genuinely his-own qualification, distinct from the rejected "divinization" framing. The corpus's existing L1280 bullet conflates the two into one "fences it against… veneration" statement.

**And the corpus's own word choice needed checking too, per the brief's separate instruction:** `venerat` = **0 occurrences in both the AssemblyAI transcript and the independent YouTube captions.** "Veneration" is a corpus paraphrase, not a transcript word, in either rendering. Per the `GV-4` precedent, this is flagged rather than resolved by quietly substituting "divinization" for "veneration" in the corpus's language — both the original wording and this correction are on record; nothing is silently swapped. The dated note at `St_Francis_EMC_Distinctives.md` L1280 carries the full correction.

---

## 5. `SRC_Channel_Inventory.md` DECISION CELL

`jTNqBnhO8A8`'s decision cell updated: `INCLUDE` → `INGESTED (source registered) — File 64`. Old text preserved via `*Previously:*` chain, per convention. File's own top stamp bumped `260835-12` → `260835-16`.

---

## 6. WHAT WAS DECLINED / NOT TOUCHED

- `Incense_Conversational_Outline.md` and `RJ_Incense_Analysis.md` — not touched.
- Nothing drafted, altered, or posted to Rev. James.
- No `RC` number minted. No finding text altered, renumbered, or re-pointed anywhere. `File` numbers are the only numbers this pass consumed (`File 64`; next free is now `File 65`).
- The stale `260835-11` block in `PROJECT_STATE.md` (L33-35) and the original `RC-6 HAS NO SUBSTRATE` / "STILL HAS NO SUBSTRATE" text in `SRC_Manifest.md` and `St_Francis_EMC_Distinctives.md` were **not edited in place** — each is superseded by a new block placed beside it, per the never-alter rule.
- The leftover `passes/260835-17_rc6-gate-halt_read-and-report_close-out.md` from the earlier duplicate run was **left exactly as it is**, per JD's explicit instruction — it is a legitimate record, not an error, and this pass's own artifacts supersede its open questions by resolving them, not by erasing the record that they existed.

---

## 7. VALIDATOR, AFTER

`python3 validate_project.py` → **82 ok · 9 warnings · 0 errors** — identical to the BEFORE reading; the 9 warnings are the same standing set (C1 RPW timestamps, two C3 unstamped files, C4 two stale-pending passages, three C5 volatile-state files, C10 §15 lag, C11 outline drift). ⚠️ **One transient error was caught and fixed during this pass, not left in the final state:** bumping `RJ_Final_Question_List.md`'s own stamp without updating `PROJECT_STATE.md`'s §4 Document Registry cell for it produced a `[C3] VERSION DRIFT` error on the first re-run; the registry cell was corrected (and the registry cells for the other four touched files were bumped to match at the same time, since they had the same latent exposure), and the re-run came back clean.

---

## 8. FILES CHANGED

`PROJECT_STATE.md`, `RJ_Final_Question_List.md`, `SRC_Channel_Inventory.md`, `SRC_Manifest.md`, `St_Francis_EMC_Distinctives.md` — 5 files, 85 insertions / 15 deletions (`git diff --stat`). Full diff at `passes/260835-16_rc6-registration-and-retro-verification.diff` (132 KB, too large for chat). Nothing staged, nothing committed — per instruction.
