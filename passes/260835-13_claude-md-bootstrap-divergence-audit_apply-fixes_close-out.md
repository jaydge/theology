# 260835-13 — Apply proposed fixes from the `260835-12` CLAUDE.md/Bootstrap divergence audit (close-out)

**Mode:** RECONCILE, narrowly scoped to the items named in the delegating brief.
**Scope:** `CLAUDE.md` and `Project_Bootstrap_Prompt.md` only. `PROJECT_STATE.md` §4
registry, `ORCHESTRATION.md`, and every other tracked file were left untouched.
**Committed:** nothing. Per the brief, commit is JD's.

---

## Gate

| Item | Value |
|---|---|
| `git rev-parse HEAD` (start of pass) | `530d987fed5e3a9510cfdb837f40df7f70acc36d` |
| Branch | `main` |
| `git --no-optional-locks status --short` (before first edit) | **NOT empty** — see below |
| Validator baseline | **82 ok · 9 warnings · 0 errors**, exit 0 |
| `PROJECT_STATE.md`'s own "Last updated" stamp | `260835-12` |
| Highest real `26xxxx-N` found repo-wide | `260835-12` — **but already double-consumed, see anomaly below** |
| This pass's stamp | **`260835-13`** |

### ⚠️ Pre-existing dirty tree at gate — not caused by, or touched by, this pass

`git status --short` at gate was **not** clean:

```
 M PROJECT_STATE.md
 M SRC_Channel_Inventory.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
?? passes/260835-12_diarization-verification-a101-room-and-batch9.diff
?? passes/260835-12_diarization-verification-a101-room-and-batch9_close-out.md
```

This is the uncommitted working tree of an **already-in-progress, unrelated pass**
(`260835-12`, "diarization-verification-a101-room-and-batch9") — its own close-out file
confirms it touched exactly these four tracked files plus its own `passes/` artifacts, and
nothing else. None of these four files were touched by this pass; three of them
(`St_Francis_EMC_Distinctives.md` plus the two named-off-limits files) are also explicitly
out of scope per the brief. Flagged rather than silently absorbed, since "before this pass's
first edit" needed an honest baseline and the tree was not actually clean when this pass
started.

### ⚠️ Pass-stamp collision, pre-existing — flagged, not fixed

A repo-wide grep for `26[0-9]{4}-[0-9]+` shows `260835-12` used **twice**: once by the
audit this pass is applying (`530d987`, already committed to `HEAD`), and once by the
uncommitted diarization pass's own `PROJECT_STATE.md` gate note and `passes/` filenames
(above). One of the two was minted in error — most likely the diarization pass reused the
audit's stamp instead of incrementing to `260835-13`. Not this pass's business to resolve
(it did not create the collision and the diarization pass's files are untouched here), but
it does mean the grep-for-highest-stamp method returns an ambiguous answer at the moment,
and **this pass claims the next real integer, `260835-13`**, to avoid deepening the
collision to a triple.

### Validator baseline — full warning set (9, all pre-existing, none this pass's business)

Identical to the `260835-12` audit's own recorded baseline:

1. `WARN [C1] src/SRC_Discord_RPW.md` — 2 relative timestamps outside message headers.
2. `WARN [C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` — no parseable stamp; registry says `260832-2`.
3. `WARN [C3] tools/transcribe_yt.py` — no parseable stamp; registry says `260833-7`.
4. `WARN [C4] St_Francis_EMC_Distinctives.md` — 2 stale answered-question passages.
5. `WARN [C5] RJ_Final_Question_List.md` — 17 volatile-state assertions.
6. `WARN [C5] RJ_Incense_Analysis.md` — 9 volatile-state assertions.
7. `WARN [C5] St_Francis_EMC_Distinctives.md` — 7 volatile-state assertions.
8. `WARN [C10]` — §15's newest `LS` citation 8 findings behind the ledger.
9. `WARN [C11]` — outline last checked against `IP-97`; ledger now `IP-108`, 11 unreviewed.

---

## Verify-before-write: audit claims re-checked against current file content

Both `CLAUDE.md` and `Project_Bootstrap_Prompt.md` were read in full before any edit. Every
claim the audit made about their content (exact wording, line-level location of the
Anglican 101 bullet, the `SRC_Manifest.md` description, the Numbering-and-versioning
bullets, the prefix list) matched current file content exactly — **no drift since
`260835-12` ran.** All items below were applied as verified; none needed to be skipped.

---

## Items applied

**Item 1 — transcript git-exclusion (`Project_Bootstrap_Prompt.md`).** Confirmed L17 still
read "stay OUT of Claude Project knowledge" only. Replaced with the audit's drafted text,
adding "OUT of **git** and out of Claude Project knowledge," matching `CLAUDE.md`'s
wording. Covered by this pass's single `Project_Bootstrap_Prompt.md` changelog entry
(`260835-13`).

**Item 3 — the two missing `260816-1` conventions (`CLAUDE.md`), the most serious item in
the audit.** Confirmed neither convention (trimmed-original marking; dual-ASR verification
protocol) appears anywhere in `CLAUDE.md`. Inserted both, condensed to `CLAUDE.md`'s house
style, immediately after the Anglican 101 capture-policy bullet in §Source handling,
preserving every normative clause the audit named: record-and-mark together; audio over a
second transcript; diarization as navigation only, never attribution of record; key-terms
lists as tooling, not a correction map. `CLAUDE.md` carries no changelog (confirmed correct
per audit item 9 — see below), so per the never-alter discipline a dated inline note was
placed at the point of insertion instead: `(adopted 260816-1; ported in ... 260835-13, per
the 260835-12 audit)`, in the same parenthetical-date style `CLAUDE.md` already uses for its
`260726-1` standing rules.

**Item 5 — `SRC_Manifest.md`'s location (`Project_Bootstrap_Prompt.md` + `CLAUDE.md`).**
Confirmed `Project_Bootstrap_Prompt.md` L23 still claimed the file "lives in project
knowledge." Generalized to "is the source registry," matching `CLAUDE.md`'s framing (which
itself was confirmed to make no location claim at all — silence, not error). Rather than add
a second, separate clause to `CLAUDE.md` asserting the git-tracked-at-repo-root fact (which
would have meant a second insertion point and a second dated note for a one-line fact),
this was folded into the wording change on the `Project_Bootstrap_Prompt.md` side, since
that is where the actual false claim lived; `CLAUDE.md`'s existing silence was already
correct and needed no addition of its own beyond what item 6 supplies.

**Item 6 — sessions-ingested-table concept (`Project_Bootstrap_Prompt.md`).** Confirmed
absent from `Project_Bootstrap_Prompt.md`'s `SRC_Manifest.md` description. Added in the
same edit as item 5, with its rationale verbatim from `CLAUDE.md`: "a hash check catches
re-uploads of the same file, not a second capture of the same event."

**Item 7 — the three `260726-1` rules: not promoted.** ⛔ Per JD's ruling in the brief, no
file edit was made. Recorded here, explicitly, that promotion was considered (the audit
raised it as Divergence 7) and declined, so a future audit does not re-raise it as
unresolved. Also recorded in `Project_Bootstrap_Prompt.md`'s new changelog entry, so the
decision is visible from either file.

**Item 8 — changelog-correction clarification (`Project_Bootstrap_Prompt.md`).** Confirmed
the corollary sentence ("if a past entry turns out to be wrong, correct it in a new entry
that says so") was absent from Numbering and versioning. Appended verbatim from `CLAUDE.md`.

**Item 10 — `RV` prefix (`Project_Bootstrap_Prompt.md`).** Confirmed the illustrative prefix
list omitted `RV`. Added, matching `CLAUDE.md`'s list.

**Item 4 — Discord cross-reference (`CLAUDE.md`).** Confirmed `CLAUDE.md` carried no
Discord-capture-method content. Added one bullet at the end of §Source handling pointing to
`ORCHESTRATION.md` §8 and `Project_Bootstrap_Prompt.md` §Discord / live dialogue logs, dated
inline in the same style as items 3's insertions.

## Items requiring no action — confirmed, not left implicit

- **Item 2** ("unmodified from their original uploaded form" — present only in
  `Project_Bootstrap_Prompt.md`): reviewed. `Project_Bootstrap_Prompt.md` already carries
  this wording (confirmed at L18 of the pre-edit file, now folded into the item-1 edit
  unchanged); `CLAUDE.md`'s silence here is covered by its adjacent
  never-split/re-encode/normalize clause. Audit's own read: literal precedence resolves
  correctly on its own here. No action needed, and none taken.
- **Item 9** (`CLAUDE.md` carries no changelog of its own): reviewed. `CLAUDE.md`'s own
  header explicitly frames `Project_Bootstrap_Prompt.md` as "the canonical, versioned,
  changelogged document," which is a stated (if implicit) carve-out. No action needed. This
  is also why items 3 and 4's insertions used inline dated notes rather than a new
  changelog section — adding a changelog mechanism to `CLAUDE.md` was never asked for and
  would have gone beyond the brief.
- **Item 11** (`under src/` qualifier, `CLAUDE.md`-only): reviewed. Correct specialization
  for a git-repo-specific working copy versus a reusable template; not a divergence. No
  action needed.
- **Item 12** (four `CLAUDE.md` sections with no `Project_Bootstrap_Prompt.md`
  counterpart): reviewed. All four are git-repo/Claude-Code-operational or project-identity
  content that `Project_Bootstrap_Prompt.md`, as a generic reusable template, has no
  obligation to carry. No competing claim exists on any of the four topics. No action
  needed.

---

## Deliberately NOT done, and why (flagged for JD, not decided unilaterally)

- **Neither file's own "Last updated" header stamp was bumped**, and **`PROJECT_STATE.md`
  §4's registry cells for `CLAUDE.md` and `Project_Bootstrap_Prompt.md` were not touched.**
  This repo's own convention (`CLAUDE.md`'s "Close-out checklist for every RECONCILE pass,"
  step 3) is to bump a touched document's stamp and its registry cell together in the same
  pass. This brief's item list never asked for that, and `PROJECT_STATE.md` is currently
  mid-edit by the unrelated, uncommitted `260835-12` diarization pass (see the dirty-tree
  flag above) — layering a second, unrelated registry edit onto that file while it sits
  uncommitted seemed like exactly the kind of scope creep the brief's precision was trying
  to avoid. **Consequence, confirmed by the after-run below: this keeps validator check C3
  green** (no new stamp-vs-registry mismatch), which would not have been true had the
  headers been bumped without a matching registry update. **A stamp/registry reconciliation
  for these two cells is owed as follow-up**, ideally once the pending diarization pass is
  committed or otherwise resolved, so the two edits to `PROJECT_STATE.md` don't collide.
- **`PROJECT_STATE.md`'s own gate-note mechanism (the `> ✅ GATE (...)` block style) was not
  used for this pass's record.** This pass's gate lives here, in this close-out, per the
  brief's own gate instructions, not in `PROJECT_STATE.md`.

---

## Validator: after vs. baseline

**After: 82 ok · 9 warnings · 0 errors, exit 0. Identical to baseline, cell for cell** — the
same nine warning codes listed above, none new, none resolved. Expected: no check that
guards `CLAUDE.md` or `Project_Bootstrap_Prompt.md` content changed status, since neither
file's stamp moved and neither warning set touches the sections edited.

---

## Files changed by this pass

```
 M CLAUDE.md
 M Project_Bootstrap_Prompt.md
```

Full diff: 109 lines, both files, reproduced in the session's final report (short enough to
paste directly; also stands as the record here).

## `git status --short` after this pass, full listing

```
 M CLAUDE.md
 M PROJECT_STATE.md
 M Project_Bootstrap_Prompt.md
 M SRC_Channel_Inventory.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
?? passes/260835-12_diarization-verification-a101-room-and-batch9.diff
?? passes/260835-12_diarization-verification-a101-room-and-batch9_close-out.md
?? passes/260835-13_claude-md-bootstrap-divergence-audit_apply-fixes_close-out.md
```

**This pass's own contribution to that list:** `CLAUDE.md`, `Project_Bootstrap_Prompt.md`
(both modified), and this close-out file (new, untracked). **Everything else in the list
predates this pass and was not touched by it** — see the dirty-tree flag above.

**What JD would stage, if committing this pass alone:** `CLAUDE.md`,
`Project_Bootstrap_Prompt.md`, and
`passes/260835-13_claude-md-bootstrap-divergence-audit_apply-fixes_close-out.md` — leaving
the four pre-existing modified files and the two `260835-12` diarization-pass artifacts for
that other pass's own commit, so the two passes don't get squashed into one mixed-vintage
commit (the exact failure mode `CLAUDE.md`'s own emission-discipline section exists to
prevent).

⛔ **Nothing staged, nothing committed**, per the brief.
