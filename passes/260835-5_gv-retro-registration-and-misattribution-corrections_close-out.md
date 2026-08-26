# 260835-5 — GV Batch Retro-Registration and Four Misattribution Corrections — CLOSE-OUT

**HEADLINE: DEPENDENT ENTIRELY ON `260835-4`. NOTHING RE-DERIVED. Byte ranges retro-registered for 34 of 54 in-scope `GV` findings; four misattributions corrected in place by dated note; one finding minted (`GV-56`); `a202.txt` NOT opened.**

---

## 0. GATE

| Check | Briefed | Observed | Verdict |
|---|---|---|---|
| `git rev-parse HEAD` | `a0cc4f3` | `a0cc4f3837ba0335a386b14f450c3faa7d9f56ca` | ✅ exact |
| `git --no-optional-locks status --short` before first edit | must capture | EMPTY, exit 0 | ✅ captured directly |
| `validate_project.py` BEFORE | report | `80 ok · 9 warnings · 0 errors` | ✅ |
| `PROJECT_STATE.md`'s own stamp at gate | report | `260835-4` | ✅ |
| Next-free pass stamp | derive | `260835-5` (repo-wide grep, highest existing `260835-4`) | ✅ |

⚠️ **The `.git` lock diagnosed at `260835-3` (FUSE mount denies `unlink` on `index.lock`) is understood and was not re-diagnosed.** Every git read this pass used `git --no-optional-locks`. No lock was created, none removed, no `rm` attempted.

Prerequisite read in full before any other action: `passes/260835-4_file-45-first-mining_pass-b2_close-out.md`. Nothing in it was re-derived — its byte offsets, speaker identifications, and dedup table were applied directly, then independently corroborated where this pass re-grepped the same passages (see §2 below).

---

## 1. What this pass is and is not

⛔⛔ **This pass mints nothing new against the general prohibition in its own brief EXCEPT the one exception the brief itself carved out (Task 4) — one number, `GV-56`, consumed.** It consumes no `LS` number. It does not touch `a202.txt`. It retro-registers locators onto findings that already exist (`GV-1`…`GV-55`) and corrects four of them, per the brief.

## 2. Task 1 — retro-registration

**Method:** every byte offset in the new registration table (`St_Francis_EMC_Distinctives.md`, new section "`GV` batch — `a201.txt` byte-range retro-registration," placed immediately before the CHANGELOG) was independently re-derived this pass by exact-string `grep -bo` against `a201.txt` (177,254 bytes, `sha256` `09a24f92…`, per `SRC_Manifest.md` File 45) — not copied from `260835-4`. Where this pass's own grep landed on the same passage `260835-4` had already cited, that is noted as corroboration (e.g. `GV-2` @31,131 exact match; `GV-4` second half @7,830 exact match; `GV-15` @45,577 vs. `260835-4`'s @45,306, same sentence).

**Placement decision, stated and defended:** five findings already carried an internal `a201 Ln/Vn` label (`GV-9, GV-30, GV-32, GV-33, GV-34, GV-36, GV-37` — note `GV-9` did not previously carry the label but sits beside `GV-32` which did) and got their byte offset added inline, beside the existing tag, matching the file's own established convention for that class of citation. For the remaining located findings, a dedicated table was used rather than ~30 scattered inline edits across dense, heavily cross-referenced prose — judged the lower-risk path for a purely additive registration task, and consistent with `SRC_Manifest.md`'s own tabular convention for File 45's per-recording ranges. This deviation from strict "inline everywhere" is disclosed, not silent.

**Result: 34 of 54 in-scope findings (`GV-1..55`, less `a202`-sourced `GV-43`) got a specific byte range or range-plus-recording.** 9 are marked **UNLOCATED**, with the exact search terms tried stated in the table, rather than guessed: `GV-12` ("Bishop Ryle"), `GV-44` ("lens by which we should interpret"), `GV-45` (Article 31 / "none other satisfaction"), `GV-47` (Saepius Officio), `GV-49`/`GV-50` (seminary-paper set-piece), `GV-52`/`GV-53` (royal supremacy / civil magistrate). 2 more (`GV-46`, `GV-51`) are recording-inferred (grouped with `GV-36` under the same `a201 L17/V8` label) but byte-unlocated — their distinctive phrases ("cookies and milk," "Parker," "black rubric," "Book of Concord") do not grep in `a201.txt` at all. `GV-31` is recording-located (rec 7) but deliberately left without a byte offset or quote, on the standing privacy guard `260835-4` §4.5 applied to the same recording. `GV-54` is confirmed `a202`-sourced and out of scope. `GV-43` was excluded from the start (already `a202`-labeled).

⚠️ **UNLOCATED is not a claim about `a202.txt`.** `a202.txt` was not opened this pass. UNLOCATED means only that this pass's search of `a201.txt` did not find the phrase there with confidence — it may be in `a202`, may use different ASR phrasing than the corpus's paraphrase, or may simply not be independently re-locatable by this method. No range was manufactured to close a gap.

**Two new locations surfaced beyond `260835-4`'s own table, both independently grepped and both in-scope:** `GV-39` (absolution among the means of grace) at `a201 @160,109`, recording 8; `GV-40` (women's ordination, deferring to the book's author) at `a201 @157,059`, recording 8 — the search also turned up a false candidate at `@119,862` (ordinary use of the word "women" in recording 7) which was checked in context and rejected.

## 3. Task 2 — four misattributions corrected

Each correction is a dated sub-bullet inserted immediately beside its finding's original text. **No original sentence was altered, deleted, or moved.** Per the standing never-alter rule (`ORCHESTRATION.md` §8), corrections are dated notes beside the original.

1. **`GV-4`, second half — done first, as the worst.** *"But he also holds 'regeneration has to precede Faith'"* (`a201 @7,830`, diarization 8:50/9:02, Speaker A) is Fr Matt Kennedy's — RJ's interlocutor's own contrary position, not a tension in Rev. James's view. **The correction states plainly that the "terminus-not-trigger refinement" has no subject**: there was never a second position in Rev. James's own voice to refine against the first, so the entire analytical move is withdrawn along with its premise, not merely flagged as uncertain. `GV-4`'s first half stands, confirmed, and is now read as a single unqualified affirmation.

2. **`GV-3`, entire — Augustinian receptionism is Fr Matt Kennedy's** (`a201 @10,397-10,805`, diarization 11:50/11:55, Speaker A). The correction states explicitly that this removes an apparent inconsistency with `GV-15` (corporeal "physically united" real presence) that was never real, since `GV-15` was never actually in tension with anything Rev. James himself said — the receptionist half of that apparent tension belonged to Kennedy throughout.

3. **`GV-6`, the Lordship-Salvation/cheap-grace clause — Kennedy's** (`a201 @25,978-26,081`, diarization 29:45/29:51, Speaker A). The main half (apostasy of the genuinely regenerate; faithlessness distinguished from apostasy, 2 Tim 2:13) stands, confirmed correctly Rev. James's by the same diarization and independently re-verified this pass.

4. **`GV-2` — "I consider myself High church" is Fr Matt Kennedy's**, spoken as one sentence with the question "how would you describe yourself?" directed at Rev. James (`a201 @31,131`, diarization 35:50, Speaker A). The correction states both facts together: the citation as written is wrong, **and** the underlying claim survives independently — `GV-10` has Rev. James saying substantially the same thing solo, in recording 2, at `a201 @42,688`.

## 4. Task 3 — confirmed, not re-litigated

`GV-1`, `GV-5`, `GV-6`'s main half, and `GV-9` were re-checked by this pass's own independent grep against `a201.txt` (not merely re-asserted from `260835-4`) and are reported as confirmed correct in the new registration table — no change made, reported rather than left silent, per the brief.

## 5. Task 4 — the two unheld items

Both were checked against the existing `GV` findings before assuming either disposition, per the brief's instruction.

- **Acts 2:37-39 exegesis (recording 5): treated as a sub-point addition to `GV-26`, not a new number.** `GV-26` already holds the "gives you that faith and repentance" clause (`a201 @85,089`); it did not hold the surrounding Acts 2:37-39 exegesis, the "both are put together" rule, or the "faith is a gift … repentance is a gift" generalisation. Because the core clause already has a tag, and the additional material is squarely an extension of the same passage rather than a distinct claim, it was added as a dated sub-point (on the corpus's own `VP-5` (i)-(iv) precedent for incremental additions without renumbering), explicitly logged as the 2020 antecedent of the 2026 Discord assurance-thread statement on the same text.
- **The burden rule (recording 5, stated four times): minted as `GV-56`.** `260835-4`'s own dedup pass established this is held by no existing `GV` finding at all — not even partially — so there is no existing tag to extend without distorting it. `260835-4`'s caveat is carried forward verbatim as part of the finding: **expressly not logged as supporting the incense lever**, since the rule presupposes an established prior practice, which is the contested question for incense itself.

`GV` legend range updated `GV-1..55` → `GV-1..56`.

## 6. What this pass did not do

- `a202.txt` / File 46 NOT opened, read, or registered — next pass's first task, per the brief.
- No draft, alteration, or post to Rev. James.
- `Incense_Conversational_Outline.md` and `RJ_Incense_Analysis.md` NOT touched.
- `SRC_Manifest.md` and `SRC_Channel_Inventory.md` NOT touched — their File-45/File-46 `UNMINED` dated notes from `260835-4` already stand and this pass's scope is finding-level citation, not source-level registration.
- No `GV` finding renumbered, retired, or merged — the four corrected findings keep their numbers; corrections are additive notes only.
- No `LS`, `IP`, `RV`, `DQ`, `BLOG`, `POD`, `VP`, `DELTA`, `EXT`, `W`, or `File` number consumed.

## 7. Validator

**BEFORE:** `80 ok · 9 warnings · 0 errors` (codes: `C1`, `C3`×2, `C4`, `C5`×3, `C10`, `C11` — identical set to `260835-4`'s own baseline).

**Interim (after the two content edits, before the `PROJECT_STATE.md` registry stamp update):** `79 ok · 9 warnings · 1 error` — `[C3] St_Francis_EMC_Distinctives.md: VERSION DRIFT — registry says '260835-3', document says '260835-5'`. This fired because the top-of-file stamp was bumped before `PROJECT_STATE.md`'s version registry (§4 table) was updated to match — an ordinary two-step stamp update, not a defect in either file.

**AFTER (final):** `80 ok · 9 warnings · 0 errors` — identical to baseline, same nine codes. `PROJECT_STATE.md`'s registry row for `St_Francis_EMC_Distinctives.md` updated `260835-3` → `260835-5` with a summary note, following the established convention every prior pass touching this file has used (append-only "Previously:" chain, nothing prior altered).

## 8. `git status --short`, in full

```
 M PROJECT_STATE.md
 M St_Francis_EMC_Distinctives.md
?? passes/260835-5_gv-retro-registration-and-misattribution-corrections.diff
?? passes/260835-5_gv-retro-registration-and-misattribution-corrections_close-out.md
?? passes/260835-5_gv-retro-registration-and-misattribution-corrections_raw-session-output.md
```

**Suggested staging: all five, one commit.**

```
git add PROJECT_STATE.md \
        St_Francis_EMC_Distinctives.md \
        passes/260835-5_gv-retro-registration-and-misattribution-corrections.diff \
        passes/260835-5_gv-retro-registration-and-misattribution-corrections_close-out.md \
        passes/260835-5_gv-retro-registration-and-misattribution-corrections_raw-session-output.md
```

**Suggested message:** `260835-5: GV batch retro-registration (34/54 findings byte-located, 9 honestly unlocated) + four misattribution corrections (GV-2/3/4/6, Kennedy's words carried as Rev. James's) + GV-56 minted (burden rule) + GV-26 sub-point (Acts 2:37-39 antecedent); a202.txt not opened`

⛔ **NOTHING WAS COMMITTED**, per the brief. `git rev-parse HEAD` after all writes still returns `a0cc4f3837ba0335a386b14f450c3faa7d9f56ca`.

## 9. Full diff

See `passes/260835-5_gv-retro-registration-and-misattribution-corrections.diff` (also pasted in the session reply) — 192 lines, two files.
