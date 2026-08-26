# 260835-8 — README reconcile and project-knowledge cleanup (close-out)

**Mode:** RECONCILE
**Scope:** repo `README.md` only (plus the mandatory `PROJECT_STATE.md` §4 registry cell).
**Committed:** nothing. Working tree left dirty for JD to stage and commit.

---

## Gate

| Item | Value |
|---|---|
| `git rev-parse HEAD` | `427409c04e748f6a443b3d4f1ac0d9a4edc2ae9e` |
| Branch | `main` |
| Validator baseline (before) | **80 ok · 9 warnings · 0 errors**, exit 0 |
| `README.md` own stamp | `260828-2` |
| `PROJECT_STATE.md` §4 registry cell for `README.md` (line 1236) | `260828-2` |
| Stamp cross-check | ✅ **AGREE.** No drift. Safe to edit. |
| Highest existing `26xxxx-N` in repo | `260835-7` |
| Next-free pass stamp | **`260835-8`** (verified: no `260835-8`…`260835-12` and no `260836-*` exists anywhere in `*.md` / `*.py`) |

### Baseline warnings (all 9, recorded so the after-run can be compared cell by cell)

1. `WARN [C1] src/SRC_Discord_RPW.md` — 2 relative timestamps outside message headers (`'Yesterday at …'`).
2. `WARN [C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` — no parseable `Last updated` stamp; registry says `260832-2`.
3. `WARN [C3] tools/transcribe_yt.py` — no parseable `Last updated` stamp; registry says `260833-7`.
4. `WARN [C4] St_Francis_EMC_Distinctives.md` — 2 passages describe an ANSWERED question as pending with no supersede marker.
5. `WARN [C5] RJ_Final_Question_List.md` — 17 volatile-state assertions.
6. `WARN [C5] RJ_Incense_Analysis.md` — 9 volatile-state assertions.
7. `WARN [C5] St_Francis_EMC_Distinctives.md` — 7 volatile-state assertions.
8. `WARN [C10]` — §15's newest `LS` citation is 8 findings behind the ledger (`LS-120` vs `LS-128`).
9. `WARN [C11]` — outline last checked against `IP-97` (`260833-5`); `IP` ledger now runs to `IP-108`; 11 findings unreviewed.

⛔ **None of these nine were touched by this pass.** They are pre-existing and remain open.

---

## Task 1 — em-dash convention softened ✅ DONE

**Editing method:** anchor-based replacement only, every anchor put through a hard
`count(anchor) != 1 → SystemExit` pre-check that aborts **before** the file is opened for
writing. No line-number edits. Four anchors, all verified unique:

```
  ok  anchor unique [README stamp]
  ok  anchor unique [README em-dash convention]
  ok  anchor unique [README changelog head]
  ok  anchor unique [PROJECT_STATE README registry cell]
```

**Superseded text (under `## Conventions`):**

> - No em-dashes or en-dashes in written output. Use commas, parentheses, periods, or restructured sentences.

**Replacement:**

> - Minimize em-dashes and en-dashes in fresh conversational output. Prefer commas, parentheses, periods, restructured sentences, or an occasional semicolon. The objection is to heavy, characteristically-AI dash use, not to the mark itself, so occasional intentional use is fine. Dash-policing is skipped during complex reconciliation work, with a single cleanup pass afterward if needed. The full statement lives in `CLAUDE.md` and `Project_Bootstrap_Prompt.md` under "Voice and drafting."

**Why this wording.** It is not invented for this pass. It tracks the standard already
carried, in near-identical words, in two registered repo files:

- `CLAUDE.md` §Voice and drafting (lines 175–179): *"Minimize em-dashes/en-dashes in fresh
  conversational output — prefer commas, parentheses, periods, restructured sentences, or an
  occasional semicolon. Heavy dash use reads as AI-generated and should be avoided. /
  Dash-policing is skipped during complex document reconciliation work; a single cleanup pass
  happens afterward if needed, not mid-task."*
- `Project_Bootstrap_Prompt.md` §Voice and drafting (lines 190–195): substantively the same.

So the README was the **only** one of the three still stating an absolute ban. This was a
one-file drift, not a project-wide policy change.

⭐ **Corroborating detail worth recording:** `README.md` already violated its own absolute ban
at line 29 (*"…not a source-tag series **—** it names a sharpening within a question-list
item…"*). The rule as written was already unenforced in the file that stated it, which is
independent evidence the ban was stale rather than merely unfashionable.

**Changelog.** One dated entry prepended in the README's own existing format
(`- **stamp:** …`, newest first), quoting the superseded wording verbatim inside the entry so
the prior text stays visible per the append-only convention. Nothing was rewritten without a
trace.

**Stamp bump.** `README.md` `260828-2` → **`260835-8`**, with the `PROJECT_STATE.md` §4
registry cell bumped in the same pass, per `CLAUDE.md` close-out checklist item 3.

⚠️ **One thing I did and am flagging rather than burying:** the registry-cell edit means this
pass touched `PROJECT_STATE.md`, which was not named in the brief. It is a mechanical
consequence of the stamp bump — without it, validator `C3` would have flipped from `ok` to a
failure. `PROJECT_STATE.md`'s **own** stamp was left at `260835-4` and no §0/pass-note block
was added, matching observed practice (the `260835-7` pass likewise edited registry cells
without bumping `PROJECT_STATE.md`'s own stamp). If JD wants a `PROJECT_STATE.md` pass note
for this pass, that is a separate small edit.

---

## Task 2 — Files-table "Share status" duplication ⛔ FLAGGED, NOT RESOLVED

**No edit was made.** This is a report and a proposal only, per the brief.

### What the duplication looks like

`README.md` §Files is a three-column table whose third column, **Share status**, carries a
live policy value on **every one of its six rows**:

| Row (file) | Share status value carried in the README |
|---|---|
| `St_Francis_EMC_Distinctives.md` | `Internal` |
| `RJ_Final_Question_List.md` | `Internal` |
| `RJ_Open_Questions_and_Divergences.md` | `Internal` |
| `RJ_Incense_Analysis.md` | `**DO NOT SHARE**` |
| `On_Incense_and_the_Altar.md` | `Internal (relay-clean suspended, recoverable)` |
| `Incense_Conversational_Outline.md` | `Internal (relay-clean suspended, recoverable)` |

Immediately beneath that table, in the very next paragraph, the README says:

> **⚠️ Policy change: external sharing is currently SUSPENDED for all documents.** See
> `PROJECT_STATE.md` §0 for the current handling policy and the conditions for restoring
> relay-clean status.

And `PROJECT_STATE.md` §0 (HANDLING POLICY — CURRENT, line 1015) does in fact own this,
down to the same per-file granularity — it carries its own table with rows for
`On_Incense_and_the_Altar.md` handling class and `Incense_Conversational_Outline.md`
handling class, plus the C7-severity state and the note that the outline's classification was
**inferred, not directed**.

### Why this is a structural defect and not a cosmetic one

Six live policy values sit in a document that, one line later, disclaims ownership of exactly
that fact. There is no mechanism keeping them in sync, and this is not hypothetical: the
README's own changelog records that this same column **has already gone stale once** —
entry `260727-1` reads *"corrected `On_Incense_and_the_Altar.md`'s share status from
'Relay-clean (shareable)' to 'Internal (relay-clean suspended, recoverable)' per the
260725-1 policy change."* The column drifted for two days after a policy change and had to be
chased. It is the exact failure the project's own single-owner rule exists to prevent, and
`README.md` is the repo front page, so it is the copy a newcomer reads first.

⚠️ Note also that the §0 owner carries a qualifier the README's column **structurally cannot**:
the outline's class is marked *"inferred, not explicitly directed — reverse it if the reviewer
changes."* A one-word cell in a table cannot express a provisional classification. The
duplicate is not merely redundant; it is lossier than the original.

### Proposed resolutions (JD's call — none applied)

**Option A — drop the column, cross-reference only (recommended).** Delete the
**Share status** column entirely; the table becomes `File | Purpose`. The paragraph beneath
already points at `PROJECT_STATE.md` §0, so nothing is lost. Cleanest fit with the
single-owner rule.
*Cost:* a reader must follow one link to learn any file's handling class.

**Option B — replace values with a uniform pointer.** Keep the column, but every cell reads
`See §0` (or `→ PROJECT_STATE.md §0`). Preserves the column's shape and signals that handling
class is a tracked property, without asserting any value.
*Cost:* a column of six identical cells is close to pure noise; Option A does the same job with
less.

**Option C — keep one genuine exception, pointer for the rest.** Cells read `See §0`, except
`RJ_Incense_Analysis.md`, which keeps `⛔ **DO NOT SHARE**`. The argument for the exception:
that value is not a policy *state* subject to the 260725-1 suspension, it is a permanent
content-firewall property (§0's *"What has NOT changed"* explicitly says the backstage
separation still governs regardless of sharing status), and it is the single highest-cost
mistake in the repo to make.
*Cost:* re-introduces one duplicated value, though of the least volatile one.

⭐ **My read, offered as a recommendation and not acted on:** **Option A**, with the paragraph
beneath the table strengthened to name `RJ_Incense_Analysis.md`'s never-forward status
explicitly in prose — which it *already does* (*"…must never be forwarded to RJ or through the
Discord intermediary"*). That gets Option C's safety without Option C's duplicate cell, and it
leaves §0 as the only place a handling class is stated.

⛔ **Not applied. Awaiting JD's decision.**

---

## Task 3 — source-handling rules: ✅ ALREADY IN THE REPO. NO DRAFT NEEDED.

**This is a found-already-covered result, not a proposal.** I searched rather than assumed,
and the brief's premise turned out to be incorrect in a way that matters for the
project-knowledge deletion decision.

### ⚠️⚠️ Correction to the briefing's premise

The brief states this content *"lives only in `docs/Project_Bootstrap_Prompt.md`, a
project-knowledge file."* **It does not.** `Project_Bootstrap_Prompt.md` exists **in the repo
root**, is tracked in git, is **registered in `PROJECT_STATE.md` §4 at `260816-1`**, and is
guarded by validator checks `C0` (registry resolution) and `C3` (stamp vs registry) — both
`ok` in the baseline run above. The project-knowledge copy is a **second copy of a repo file**,
which is precisely the "one copy of any document" hazard: two copies, one of which will go
stale with no signal telling you which.

A second, independent copy also exists in **`CLAUDE.md` §Source handling**, likewise registered
in §4 (`260728-2`) and C0/C3-guarded.

### Item-by-item coverage of the three named rules

| Rule named in the brief | `CLAUDE.md` §Source handling | `Project_Bootstrap_Prompt.md` §Source handling | Elsewhere |
|---|---|---|---|
| **`SRC_` prefix rationale** | ✅ L44–46: *"Raw, unedited source material (transcripts, chat exports, external texts) uses the `SRC_` filename prefix, under `src/`. Canonical analysis/synthesis documents do not use this prefix."* | ✅ L14–16, same wording minus `under src/` | Partially in `README.md` §Repo layout L35 (states the convention, not the rationale) |
| **Verify sha256 against `SRC_Manifest.md` before trusting a logged offset** | ✅ L57–58: *"Before trusting a previously-logged byte offset, verify the source file's current hash against `SRC_Manifest.md`."* Plus L52–56 defining the manifest as the source registry | ✅ L26–27, same rule; L23–25 defines the manifest | `SRC_Manifest.md` itself (72 `sha256` occurrences); `ORCHESTRATION.md` L172 |
| **Transcripts stay unmodified and out of any AI project-knowledge store** | ✅ L47–51: *"Full audio/video transcripts stay OUT of git and out of project knowledge… **Never** split a multi-item transcript file, re-download, re-encode, or normalize line endings — any of these invalidates previously-logged byte offsets."* | ✅ L17–22, same rule, adds *"They live in a stable local folder, **unmodified from their original uploaded form**"* | `PROJECT_STATE.md` §0 L1033 extends the same handling class to the BLOG batch, citing `Project_Bootstrap_Prompt.md` by name as the class's owner |

**Verdict: all three rules have a repo home, twice over. No new README section and no new file
is proposed, because none is needed.** Adding a third copy would make the duplication worse,
not better.

### ✅ Consequence for the project-knowledge deletion JD is holding

The blocking question behind Task 3 was: *is it safe to delete `docs/README.md` and
`docs/Project_Bootstrap_Prompt.md` from Claude project knowledge?*

**From a content-loss standpoint, yes.** Every rule in the brief's list survives the deletion
in at least two registered, validator-guarded repo files. Deleting the project-knowledge copies
removes duplicates, not originals, and moves the project *toward* the single-canonical-location
rule rather than away from it.

⛔ **Not done in this pass, as instructed.** Project knowledge is a separate write surface from
git and this pass touched only the repo. When JD does it, the delete-and-replace convention
(`CLAUDE.md` L85–86, `Project_Bootstrap_Prompt.md` L138–140) governs.

### ⚠️ Two open items surfaced by this search, neither resolved here

1. **The `CLAUDE.md` / `Project_Bootstrap_Prompt.md` divergence audit is still owed.**
   `CLAUDE.md`'s own header block (L9–11) says so in as many words: *"⛔ Registration is not
   reconciliation: nobody has yet audited this file against `Project_Bootstrap_Prompt.md` for
   divergence. That audit is owed work."* This pass did **not** perform that audit. It did
   incidentally observe two real divergences in the Source-handling sections, recorded here
   only so they are not lost:
   - `CLAUDE.md` L47 says transcripts stay out of **git and** project knowledge;
     `Project_Bootstrap_Prompt.md` L17 says only **Claude Project knowledge**. `CLAUDE.md` is
     the stricter of the two, but `Project_Bootstrap_Prompt.md` is declared canonical
     (`CLAUDE.md` L13–18), so on a literal reading the *weaker* text wins a conflict. Worth
     JD's attention.
   - `CLAUDE.md` omits *"stable local folder, unmodified from their original uploaded form."*
     The substance is covered by its never-split/re-encode/normalize clause, but the word
     **unmodified** appears only in `Project_Bootstrap_Prompt.md`.
2. **`README.md` §Repo layout states the `SRC_` prefix convention without its rationale**, and
   without pointing at the file that owns it. A one-clause cross-reference would close that,
   but it was **not added** — it is outside this pass's brief.

---

## What was declined, and what came back empty

Per `passes/README.md`: *"A close-out that reports only successes is under-reporting."*

- ⛔ **Declined:** resolving the Task 2 Share-status duplication. Explicitly reserved for JD.
- ⛔ **Declined:** deleting `docs/README.md` or `docs/Project_Bootstrap_Prompt.md` from project
  knowledge. Out of scope and a different write surface.
- ⛔ **Declined:** drafting anything to Rev. James; opening, reading or touching
  `Incense_Conversational_Outline.md` or `RJ_Incense_Analysis.md`. Neither file was read this
  pass.
- ⛔ **Declined:** committing. Working tree left dirty.
- ⛔ **Declined:** clearing any of the 9 baseline warnings, including the `C11` outline drift,
  which per the validator's own text is REPORT-only and must not be resolved by rewriting JD's
  reasoning.
- ⛔ **Declined:** performing the owed `CLAUDE.md` ↔ `Project_Bootstrap_Prompt.md` divergence
  audit. Found and reported, not executed.
- 🔍 **Came back empty:** the search for a *gap*. Task 3 was framed as "draft one if not
  [present]." The honest result is that the drafting half of the task had no work in it. I
  looked in all four files the brief named (`PROJECT_STATE.md`, `SRC_Manifest.md`,
  `ORCHESTRATION.md`, `README.md`) and then, because the first four were inconclusive, in
  `CLAUDE.md` and the repo-root `Project_Bootstrap_Prompt.md`, which is where it was.
- 🔍 **Came back empty:** the next-free-stamp collision check. No `260835-8` through
  `260835-12` and no `260836-*` exists anywhere in the tracked `*.md` / `*.py` files.

---

## Validator: after vs. baseline

**After: 80 ok · 9 warnings · 0 errors, exit 0. Identical to baseline, cell for cell.**
No check changed status, no new warning appeared, and no warning was silently cleared.
`C3 [README.md]` continues to read `ok` at the **new** value `260835-8`, which is the
positive confirmation that the stamp and the registry cell moved together.

---

## ⚠️⚠️ BLOCKER FOR JD — `.git/index.lock` IS PRESENT AND THIS SESSION CANNOT REMOVE IT

A zero-byte `.git/index.lock` appeared during this pass's first `git status --short` and is
**still there**. `git` reported it directly:

```
warning: unable to unlink '/…/theology/.git/index.lock': Operation not permitted
```

and an explicit removal attempt failed the same way:

```
rm: cannot remove '.git/index.lock': Operation not permitted
rm exit: 1
-rw------- 1 … 0 Aug 26 15:42 .git/index.lock
```

⭐ **This is the recurrence of a known, already-recorded defect, not a new one.** The
`260835-1` gate note in `PROJECT_STATE.md` (line 73) records the same shape: *"`.git/*.lock`
ABSENT AT GATE — and it RECURRED AT CLOSE-OUT."* It was absent at this pass's gate too, and
has recurred at close-out again. It appears to be a permissions artifact of the sandboxed
mount rather than a real concurrent-git lock.

⛔ **`git add` and `git commit` will fail until it is deleted**, and it must be deleted from
the host side (`rm -f .git/index.lock` in a normal terminal), because this session lacks the
permission. **No git state is corrupt** — `git diff`, `git status` and `git log` all read
correctly, `HEAD` is unmoved at `427409c`, and the working-tree changes are intact.

---

## Files changed (nothing staged, nothing committed)

```
 M PROJECT_STATE.md
 M README.md
?? passes/260835-8_readme-reconcile-and-project-knowledge-cleanup.diff
?? passes/260835-8_readme-reconcile-and-project-knowledge-cleanup_close-out.md
```

**Recommended staging: all four.** The two modified files are one atomic change (a stamp bump
without its registry cell is exactly the mixed-vintage-tree defect `CLAUDE.md` §Before doing
anything item 3 exists to catch), and the three `passes/` files are the pass record, which
per `passes/README.md` is committed alongside the change it describes.

⛔ **Nothing was staged and nothing was committed.** `git add` and `git commit` are JD's.
