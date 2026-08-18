# St Francis EMC Research

**Last updated: 260828-2**

A structured theological research project on the public teaching of Rev. James Gadomski ("RJ"), rector of St. Francis Anglican Church (Episcopal Missionary Church) in Spartanburg, SC. The goal is to understand RJ's positions through his own teaching, identify genuine tensions with the Anglican formularies he holds (the Thirty-Nine Articles and 1662 BCP), and develop friendship-preserving questions for in-person and Discord-mediated conversation.

The priority framework weights **Bucket A** (internal Anglican tensions, where RJ diverges from his own formularies) over **Bucket B** (cross-tradition Reformed vs. Anglican disagreements). Attribution discipline is strict throughout: stated/verbatim claims, labeled inference, and my own argument are kept distinct, and unsourced motive speculation is avoided.

## Files

| File | Purpose | Share status |
|------|---------|--------------|
| `St_Francis_EMC_Distinctives.md` | Findings ledger. The source-of-truth record of RJ's positions, tagged by speaker and status and verified against transcripts. | Internal |
| `RJ_Final_Question_List.md` | Structured question bank. The analytical forms, organized by bucket, with cross-references and changelog. | Internal |
| `RJ_Open_Questions_and_Divergences.md` | Short review sheet. What is still unknown about RJ's views, and where he diverges from pre-Oxford classical Reformed Anglicanism. Summary index; derived from the ledgers, not a source. | Internal |
| `RJ_Incense_Analysis.md` | Leverage analysis and conversational sequencing for the incense cluster. Written backstage. | **DO NOT SHARE** |
| `On_Incense_and_the_Altar.md` | Relay document on incense and the regulative principle, in friendship-preserving register. | Internal (relay-clean suspended, recoverable) |
| `Incense_Conversational_Outline.md` | Conversational outline derived from the incense analysis, for peer/reviewer walkthrough. | Internal (relay-clean suspended, recoverable) |

**⚠️ Policy change: external sharing is currently SUSPENDED for all documents.** See `PROJECT_STATE.md` §0 for the current handling policy and the conditions for restoring relay-clean status. The two incense documents remain deliberately separated regardless of sharing status: `On_Incense_and_the_Altar.md` and `Incense_Conversational_Outline.md` are the relay-clean-class home for the friendly questions (no backstage leverage material, even in changelogs), while `RJ_Incense_Analysis.md` holds the strategy and must never be forwarded to RJ or through the Discord intermediary.

## Versioning

Two conventions are in use:

- **Distinctives and incense documents** use date-based stamps in `yymmdd-iteration` format (for example, `260621-1`).
- **The question list** uses integer increments (`v6`, `v7`, ...) alongside the date stamp.

Findings use `IP-n` numbering with a session-date stamp; source tags include IP (in-person), BP (Barely/Merely Protestant YouTube), RC (Roman Catholicism series), Rev (Revelation class), GV (General Videos), and EXT (external research). `QA-*` is a question-list LABEL series, not a source-tag series — it names a sharpening within a question-list item (see `PROJECT_STATE.md` §5, rule 5).

Current baselines for every document are tracked in `PROJECT_STATE.md` §4 (Document Registry), which is the single source of truth for version state. This file does not restate version numbers.

## Repo layout

Canonical documents live at the repo root. Raw source material (`SRC_` prefix) lives under `src/`, not flat:

```
<repo root>/
├── PROJECT_STATE.md
├── St_Francis_EMC_Distinctives.md
├── RJ_Final_Question_List.md
├── RJ_Open_Questions_and_Divergences.md
├── RJ_Incense_Analysis.md
├── On_Incense_and_the_Altar.md
├── Incense_Conversational_Outline.md
├── SRC_Manifest.md
└── src/
    └── SRC_Discord_*.md
```

## Workflow

A two-mode workflow keeps live documents stable. **Append mode** intake threads generate patch blocks for later reconciliation and never touch the live docs. **Reconcile mode** threads apply those patches against the live documents using anchor-based edits, after verifying baselines and confirming a mapping plan. GitHub commits and Project-knowledge updates are handled manually after each reconcile pass.

## Conventions

- RJ is always **"Rev. James"** or **"RJ,"** never "Fr. James."
- No em-dashes or en-dashes in written output. Use commas, parentheses, periods, or restructured sentences.

## Changelog

- **260828-2:** Added `RJ_Open_Questions_and_Divergences.md` to the files table and the repo-layout block, on the pass that created and registered it. No other change; version state still lives only in `PROJECT_STATE.md` §4.
- **260727-1 (2026-07-27):** Fixed stale content flagged since 260725-1: removed the duplicated baselines line (now points at `PROJECT_STATE.md` §4, the single source of truth for version state, rather than restating numbers here); corrected `On_Incense_and_the_Altar.md`'s share status from "Relay-clean (shareable)" to "Internal (relay-clean suspended, recoverable)" per the 260725-1 policy change, and added the same correction and a missing files-table row for `Incense_Conversational_Outline.md`; added the `QA-*` label-series note; added a repo-layout block showing `src/`. Added this file's first `**Last updated:**` stamp.
