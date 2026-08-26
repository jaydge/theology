# 260835-7 — `a202.txt` Retro-Registration and `GV-50`/`GV-51` Corrections — CLOSE-OUT

**HEADLINE: DEPENDENT ENTIRELY ON `260835-6`. NOTHING RE-DERIVED WITHOUT INDEPENDENT CHECK. 11 `GV` findings byte-located in `a202.txt` (2 already-known, 9 newly located, one of them at two sites); two misattributions corrected in place by dated note; one standing hazard registered permanently; coverage state recorded. `GV-12`/`GV-55` remain genuinely unresolved. No `GV` number consumed. Nothing committed.**

---

## 0. GATE

| Check | Value | Verdict |
|---|---|---|
| `git rev-parse HEAD` | `856f9a5fbcab1a0f6cc20ca8e622282c616ea09b` | ✅ matches briefed `856f9a5` exactly |
| `git --no-optional-locks status --short` before first edit | EMPTY, exit 0 | ✅ captured directly, not reconstructed |
| `validate_project.py` BEFORE | `80 ok · 9 warnings · 0 errors` | ✅ — identical code set to `260835-6`'s own baseline |
| `PROJECT_STATE.md`'s own top-of-file stamp at gate | `260835-4` | ✅ reported as-is — this is the file's OWN pre-existing one-behind-its-table inconsistency `260835-6` already flagged and did not touch; not caused or corrected by this pass either |
| Next-free pass stamp | `260835-7` | ✅ derived by repo-wide `grep -rhoE '\b26[0-9]{4}-[0-9]+\b'`; highest existing anywhere was `260835-6` (the read-and-report pass); `260835-7` returned zero hits before this pass began writing |

Every git read this pass used `git --no-optional-locks` (the FUSE-mount lock behavior diagnosed at `260835-3`, understood and not re-diagnosed). No lock created, none removed, no `rm` attempted.

**Prerequisite read in full before any other action, per the brief:** `passes/260835-6_a202-coverage-classification_read-and-report_close-out.md`. Nothing in it was re-derived on trust — every byte offset this pass registers was independently re-searched against `a202.txt` itself, and both `GV-50`/`GV-51` speaker attributions were independently re-checked directly against the AssemblyAI diarization sentence files, not carried from `260835-6`'s summary.

---

## 1. What this pass is and is not

Retro-registers locators onto existing findings (`GV-43…GV-54`, the `a202`-sourced subset) and corrects two of them, the same shape as `260835-5`. **Mints nothing, consumes no `GV` number** — every next-free ledger value reported unchanged at the end. Does not mine any new `a202.txt` content beyond what was already located; the uncovered remainder is explicitly left for a separate mining pass, per the brief.

⚠️ **One discrepancy in the brief, reported rather than silently reconciled:** the brief's own parenthetical names eleven finding numbers (`GV-43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54`) but calls them "the nine offsets." Eleven findings were registered; `GV-49` and `GV-51` each carry two distinct offset sites within `a202.txt` (rec 1 + rec 2 for `GV-49`; two speaker-split clauses for `GV-51`), so depending on what "an offset" is taken to mean the true count is either 11 (findings) or 13 (distinct byte sites) — neither is 9. All eleven named findings were registered regardless of the count language.

---

## 2. Task 1 — retro-registration, independently re-derived

**Method:** `a202.txt` (211,170 bytes) hash-verified fresh this pass — `sha256 5fdcafeb0ff6a2fd3424387e2250e212fa614ee84e329431b4609394a86be8a2`, exact match to `SRC_Manifest.md`'s registered File 46 hash and byte count. Every anchor phrase was searched directly against this file's own bytes with Python (`str.find`, all occurrences enumerated, not just the first), independently of `260835-6`'s cited offsets. New section added to `St_Francis_EMC_Distinctives.md`, immediately after the existing `a201.txt` retro-registration table and before the CHANGELOG, following that table's exact format and the placement convention it set.

**Result, corroboration vs. refinement:**
- `GV-43`, `GV-44`, `GV-47`, `GV-52`, `GV-53`, `GV-54` — independently re-derived offsets **match `260835-6` exactly.**
- `GV-45` — range matches exactly; this pass additionally found a related-but-distinct occurrence of "none other satisfaction" earlier in the same recording (@66,705, spoken by the *opponent* reading Article 31's text, not by Rev. James) and flagged it as **not** part of `GV-45`'s registered content, so a later pass does not conflate the two.
- `GV-46` — recording corrected to rec 1 (matching `260835-6`, overturning the old "recording 8 (inferred)" guess); the "black rubric" anchor refined to an exact offset (`260835-6` gave "~41,180-ish"; this pass's exact-string search puts it at @41,159).
- `GV-49` — both sites (`a202` rec 1 @23,798-34,772; rec 2 @97,299-106,908) independently re-derived; the rec-1 start refined slightly (@23,798 vs. `260835-6`'s @~23,851, same sentence — "the year 1896 pope leo the 13th issued a papal bull"). The rec-2 self-identification sentence ("I will be reading my first argument from a paper I did last year in seminary") was independently **sentence-verified** against the diarization as Speaker C, established as Rev. James by a direct floor-handoff in the same recording, not assumed.
- `GV-50`, `GV-51` — offsets match `260835-6` exactly; **speaker attribution independently re-derived from scratch** (§3 below), not carried from `260835-6`'s diarization summary.
- `GV-12`, `GV-55` — independently re-searched, both remain genuinely UNLOCATED, exact search terms and hit-counts stated in the new table (`GV-12`: "ryle" 1 hit but content mismatch, "Ryle"/"bishop ryle" 0; `GV-55`: "lent" 10 hits — not a usable anchor — "deuterocanon" 1 tentative hit, "eastward"/"king james"/"kjv" all 0).

---

## 3. Task 2 & 3 — the two corrections, and how the standing hazard was independently re-verified

⛔⛔⛔ **THE HAZARD WAS NOT TAKEN ON TRUST. This pass opened the raw AssemblyAI diarization sentence files itself** (`redownloads/HolyOrders-Debate-ApostolicaeCurae-sentences.json` and `…-Minton-sentences.json`, both `speaker_labels: true`) and re-derived each recording's own speaker mapping independently, from each recording's own self-identification and floor-handoff sentences — never by carrying recording 1's label mapping into recording 2.

**Recording 1** (*Apostolicae Curae* debate) — established fresh: `A` = Noah Edmonds, self-identified *"My name is Noah Edmonds… I'm going to be moderating this debate"* (moderator only, not a debater in this one); `B` = Rev. James (second opening statement, per the moderator's own stated running order — *"opening statements from John… followed by James's"*), whose opening statement (@23,798) begins the same papal-bull argument confirmed elsewhere as his; `C` = John Fisher 2.0, self-identified *"as Catholics we want Anglicans to acknowledge…"*, thanking *"James Barely Protestant"* by name in the first opening statement.

**Recording 2** (Minton debate) — established fresh, independently of recording 1: `A` = Evan Minton, self-identified sentence 1, *"I'm Evan Minton of Cerebral Faith Ministries."* `B` = Noah Edmonds — self-names at the debate's own opening (sentence 5) and later argues a stricter Roman-Catholic-leaning sacramental-validity position (sentences 609-611) consistent with the video's own description of him. `C` = Rev. James — handed the floor by name at sentence 19 (*"So, James, I'm going to give you the floor"*), and the very next speaker (sentence 20) begins his opening statement, self-identifying at sentence 25 with the seminary-paper line that independently confirms `GV-49`.

**`B` = Rev. James in recording 1; `B` = Noah Edmonds, his opponent, in recording 2. The label inverts.** This is now registered as a standing hazard in `SRC_Manifest.md` (Speaker-attribution section, File 46 entry) with a short cross-reference pointer added at the per-recording rows above it, so a future pass reads the warning before opening either debate row, not after repeating the mistake.

**Task 2 — `GV-50` corrected.** Sentence 8 in recording 2, *"Deacon James also runs the Barely Protestant Facebook page along with several other liturgical and sacramental Protestants,"* is Speaker A (Evan Minton), part of his unbroken third-person introduction of both debaters (sentences 6-9 all speaker A, none first-person). Corrected by dated note beside the finding's own text (`St_Francis_EMC_Distinctives.md`, "Ordination timeline" bullet) — the sentence is preserved byte-for-byte above the note, per the never-alter rule. The underlying fact (he did run that page) is not withdrawn; only the citation of the sentence as his own statement is.

**Task 3 — `GV-51` split.** The "cookies and milk" matter-validity clause (sentence 607, @166,617) is Speaker C — confirmed Rev. James, correctly his. The "EO have valid orders" clause (sentence 285, @130,178) is Speaker B — confirmed Noah Edmonds, answering Speaker C's own cross-examination question at sentence 284 (*"would you say that the Eastern Orthodox… do not have valid orders?"*). Corrected by dated note beside the finding's own text (`St_Francis_EMC_Distinctives.md`, "Eucharistic taxonomy" bullet): the matter-validity half stands as his; the EO-valid-orders half is withdrawn from his attribution and recorded as Noah's answer, solicited by James's own question but not thereby his position.

---

## 4. Task 4 — standing hazard registered permanently

Added to `SRC_Manifest.md` in two places: (a) a full subsection under "Speaker-attribution note — Files 40-46," File 46 entry, stating both recordings' independently-derived speaker maps side by side and naming the inversion explicitly; (b) a short dated pointer immediately beside the two `a202` debate rows in the per-recording table above it, so it is the first thing read before either row is opened. `PROJECT_STATE.md`'s §4 registry row for `SRC_Manifest.md` updated to summarize this, per the established "*Previously:*" chain convention — no prior note edited or removed.

## 5. Task 5 — coverage state recorded, not mined

Per-recording coverage table added to `SRC_Manifest.md` immediately after the `a202` per-recording rows: rec 1 ≈46%, rec 2 partial and non-contiguous (with the two now-corrected findings' effect on the apparent count noted), rec 3 partial by strict citation span but topically continuous throughout, rec 4 ≈4%. Explicitly states this is a depth-sweep-with-gaps job for a future pass, not virgin material, and that any such pass's own brief must carry the label-flip hazard forward. **The uncovered remainder was NOT mined this pass.**

---

## 6. What this pass did not do

- No `a202.txt` content mined beyond the eleven findings' own located passages.
- `Incense_Conversational_Outline.md` and `RJ_Incense_Analysis.md` NOT opened.
- Nothing drafted, altered, or posted to Rev. James.
- No `GV` finding renumbered, retired, or merged; the two corrected findings keep their numbers — corrections are additive dated notes only.
- No `LS`, `IP`, `RV`, `DQ`, `BLOG`, `POD`, `VP`, `DELTA`, `EXT`, `W`, or `File` number consumed. `GV` next-free unchanged at `GV-57`.
- `GV-12` and `GV-55` NOT resolved — reported UNLOCATED with search terms stated, not guessed.
- Nothing committed.

## 7. Validator

**BEFORE:** `80 ok · 9 warnings · 0 errors` — codes `C1`, `C3`×2, `C4`, `C5`×3, `C10`, `C11` (identical set to `260835-6`'s own baseline).

**AFTER (final, both file-stamp and registry-row updates made together to avoid the transient version-drift error `260835-5` reported):** `80 ok · 9 warnings · 0 errors` — identical to baseline, same nine codes. `[C3]` confirms both touched files individually: `St_Francis_EMC_Distinctives.md: version agrees with registry (260835-7)`; `SRC_Manifest.md: version agrees with registry (260835-7)`.

## 8. `git status --short`, in full

```
 M PROJECT_STATE.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
```

Plus this pass's own new artifacts (untracked): `passes/260835-7_a202-retro-registration-and-gv50-gv51-corrections.diff`, `passes/260835-7_a202-retro-registration-and-gv50-gv51-corrections_close-out.md`.

**Suggested staging: all five, one commit — not run, per the brief.**

```
git add PROJECT_STATE.md \
        SRC_Manifest.md \
        St_Francis_EMC_Distinctives.md \
        passes/260835-7_a202-retro-registration-and-gv50-gv51-corrections.diff \
        passes/260835-7_a202-retro-registration-and-gv50-gv51-corrections_close-out.md
```

**Suggested message:** `260835-7: a202.txt retro-registration (11/13 GV-43..54 sites byte-located, GV-12/GV-55 honestly unlocated) + GV-50/GV-51 misattribution corrections (Minton's introduction, Noah's cross-exam answer) + standing label-flip hazard registered (SRC_Manifest.md, File 46) + a202 coverage state recorded, not mined`

⛔ **NOTHING WAS COMMITTED.** `git rev-parse HEAD` after all writes still returns `856f9a5fbcab1a0f6cc20ca8e622282c616ea09b`.

## 9. Diff

`passes/260835-7_a202-retro-registration-and-gv50-gv51-corrections.diff` — 144 lines, three files (`PROJECT_STATE.md`, `SRC_Manifest.md`, `St_Francis_EMC_Distinctives.md`).
