# CLAUDE.md

**Last updated: 260728-2**

> ⚠️ **REGISTERED IN `PROJECT_STATE.md` §4 ON 260728-2 (CL-5).** Until then this
> file was tracked in git but appeared **zero times** in the registry, which put
> the one file that instructs an agent outside every guarantee the registry
> provides. This stamp exists so **validator check C3 guards it** instead of
> skipping it silently. ⛔ **Registration is not reconciliation:** nobody has yet
> audited this file against `Project_Bootstrap_Prompt.md` for divergence. That
> audit is owed work.

> **This is a working copy for Claude Code.** `Project_Bootstrap_Prompt.md`
> is the canonical, versioned, changelogged document. If this file and that
> one ever diverge, `Project_Bootstrap_Prompt.md` wins — update this file to
> match, not the reverse. `PROJECT_STATE.md` is the single source of truth
> for volatile state (whose turn it is, what's asked/answered, gates,
> document versions). **Read `PROJECT_STATE.md` first, every session.**

## What this repo is

A structured, long-term theological research and dialogue project on the
public teaching of Rev. James Gadomski ("Rev. James" or "RJ," **never**
"Fr. James"), rector of St. Francis Anglican Church (Episcopal Missionary
Church), plus a parallel Protestant apologetics workstream. Priority
framework: **Bucket A** (internal Anglican tensions, where RJ diverges from
his own named formulary, the 1662 BCP) outweighs **Bucket B** (cross-
tradition Reformed vs. Anglican disagreement).

## Before doing anything

1. Read `PROJECT_STATE.md` in full.
2. State which mode this session is: **APPEND** or **RECONCILE** (see below).
3. If RECONCILE: report the "Last updated" stamp of every file you're about
   to touch, and diff it against `PROJECT_STATE.md` §4's registry cell for
   that file. **If they disagree, stop and say so before editing anything.**
   This is not optional — it is how the July 2026 mixed-vintage-tree
   incident is caught before it repeats.
4. Run `python3 validate_project.py` and read the coverage summary, not just
   the error count. A check that examined zero files is not a passing check.

## Source handling

- Raw, unedited source material (transcripts, chat exports, external texts)
  uses the `SRC_` filename prefix, under `src/`. Canonical analysis/synthesis
  documents do not use this prefix.
- Full audio/video transcripts stay OUT of git and out of project knowledge.
  They are attached to a chat message only for the session that needs them.
  **Never** split a multi-item transcript file, re-download, re-encode, or
  normalize line endings — any of these invalidates previously-logged byte
  offsets.
- `SRC_Manifest.md` is the source registry: sha256 hash and byte range per
  item for every transcript file, plus the **sessions-ingested** table
  (session + date + coverage), which is the identity layer the hash check
  cannot provide — a hash check catches re-uploads of the same file, not a
  second capture of the same event.
- Before trusting a previously-logged byte offset, verify the source file's
  current hash against `SRC_Manifest.md`.
- Before deploying any verbatim quote in outward-facing material, stop and
  request the actual source file. Never quote from a ledger's paraphrased
  summary — ledgers are for navigation, not for quotation.
- Byte-offset extraction on long-line transcript files: use `grep -ob` and
  `dd`, not plain `grep`, which is unreliable on very long lines.
- Verbatim quotes are byte-offset verified before being logged or deployed.
  Never attribute a paraphrase as a direct quote.
- **Anglican 101 capture policy (set 260726-1):** JD's room recording `[R]`
  is PRIMARY **permanently, by policy** for this series — it captures
  post-session informal Q&A the official stream upload `[S]` does not.
  `[S]` never promotes for this series; a stream capture arriving for an
  already-ingested session runs a **comparison pass**, producing a
  divergence-report patch, not a promotion. Audio verification is required
  for both captures regardless of which is primary. See `SRC_Manifest.md`
  §Note 2a for the full procedure and its two branches.
- **Trimmed/replaced originals: record and mark together, not just replace
  (adopted 260816-1; ported in from `Project_Bootstrap_Prompt.md` §Source
  handling 260835-13, per the `260835-12` audit — the most serious gap it
  found).** When an as-recorded original is trimmed, re-encoded, split, or
  replaced, record the event in `SRC_Manifest.md` **and** mark the
  surviving file as NOT the as-recorded original — even, especially, when
  it inherited the original's filename. A filename is a provenance claim a
  hash check cannot verify; the record and the marking are both required,
  or the rule fails.
- **Dual independent ASR of one capture — verification protocol (adopted
  260816-1; ported in 260835-13, same audit).** Where two ASR systems
  transcribe one capture, agreement gives only PROVISIONAL confidence
  against transcription error; divergence goes to a verification queue
  resolved **by ear against the audio**, never against the second
  transcript. Neither transcript is authoritative on wording alone.
  Diarization is a navigation layer only, never attribution of record. A
  tuned key-terms list is repo tooling that improves future runs — it is
  **not** a correction map for text already captured.
- **Discord capture method and copy/paste limits (added 260835-13, per the
  `260835-12` audit):** see `ORCHESTRATION.md` §8 and
  `Project_Bootstrap_Prompt.md` §Discord / live dialogue logs.

## Document modes

- **APPEND MODE:** patches only; live docs are never touched. New findings
  go into a running patch-block artifact for later reconciliation.
- **RECONCILE MODE:** live docs are edited directly, using anchor-based
  string replacement against unique anchors — **never** line-number
  insertion, since documents shift between sessions.
- A control/orchestration thread (if one exists in the chat interface)
  handles state tracking and prompt generation only. Transcript or source
  intake never happens there.
- When updating Claude.ai Project knowledge, always delete-and-replace
  rather than uploading a duplicate.

## ⚠️ Emission discipline — read this before every RECONCILE pass

This is the rule that exists because of a real incident: an interrupted
pass emitted its output in two batches, and a partial download across that
boundary produced a working tree with a stale `PROJECT_STATE.md` sitting
beside documents whose stamps had already been bumped. No single check
could diagnose it, because the stale file was the one doing the checking.

- **At the end of any pass that touches the repo, commit the entire
  registered set together, in one commit.** Never cherry-pick which files
  to write just because only some of them changed content — a registry
  bump with no matching document change is still a real change.
- **If a pass is interrupted before it finishes** (tool-use limit, timeout,
  anything that would split the work), say so explicitly, name every file
  still owed, and do **not** commit a partial set. Re-run the pass whole
  rather than resuming mid-stream.
- Since Claude Code edits the working tree directly and commits from there,
  this failure mode should be structurally harder to hit than it was in the
  browser workflow — there is no download step to be interrupted across.
  Don't assume that immunity; verify `git status` is clean and every
  touched file's stamp agrees with its registry cell before committing.

## Attribution discipline

- Maintain the three-layer attribution system in all analysis documents:
  **Stated** (verbatim, byte-offset verified), **Stated-Analysis** (a
  labeled inference from something stated), and **Analysis** (the project's
  own argument, not attributed to RJ). These layers are never conflated in
  output or in anything relayed back to him.
- Watch for rhetorical or reductio content being misread as declarative.
  If RJ's strongest-sounding line is actually a question inside his own
  argument, flag it as such — never quote it back as an assertion.
- Never impute a rule, position, or reasoning to RJ that he hasn't stated,
  even when it seems like a natural completion of what he said. If his
  reasoning is genuinely ambiguous between two readings, **keep both
  readings live and ask which he means** — don't pick one and ask him to
  ratify it.
- **⭐ Standing rule (260726-1): his own example outranks the project's
  version of it.** Whenever new source material shows RJ has already used
  an argument in his own words, recast the project's version of that
  argument as his, in every document where it appears. His own example
  cannot be dismissed as an outside framework; the project's paraphrase of
  the same argument can.
- **⭐ Standing permission (260726-1):** update documents without asking
  first where RJ's position is clear on the record. Ambiguous readings
  still come back as questions — this permission covers documentation, not
  posting anything to him.

## Numbering and versioning

- Source-tag numbering (`IP`, `DQ`, `GV`, `RC`, `BP`, `RV`, `EXT`, and other
  batch-specific prefixes) is cumulative and unbroken across all intake
  batches — never restarted per document. Current heads are in
  `PROJECT_STATE.md` §5.
- Question-list-style documents use integer version increments (`v17` →
  `v18`). Ledger/findings documents use date-based versioning:
  `yymmdd-[iteration]`.
- Every canonical document carries a permanent, prepended changelog. Once
  written, changelog entries are historical record and are **never**
  altered, only added to. If a past entry turns out to be wrong, correct it
  in a **new** entry that says so — don't rewrite history.

## Strategic/dialogue discipline

- **One committal question per turn** in any live dialogue (Discord); hold
  rebuttals and downstream arguments until the prior answer is on record.
- Lock a general principle before applying it to the specific case it's
  really aimed at (the funnel approach). Don't name the target case until
  the rule is already committed to.
- Prefer questions that ask what work a stated distinction is doing, over
  questions that assert a rule and ask for ratification.
- Maintain the retired/do-not-deploy register for arguments already
  answered satisfactorily.
- **⚠️ Posture note (260726-1):** JD is now willing to tip his hand on
  argument direction where it moves the discussion faster. This relaxes
  concealment of direction only — lock-before-port still governs order of
  operations, and hybrid pre-emption (naming and dismantling an anticipated
  escape) still never enters posted text.
- Keep tone collaborative and non-adversarial by design, not by accident.
- **⚠️ Check `PROJECT_STATE.md` §2 before drafting or posting anything to
  RJ.** If a question is outstanding and unanswered, no new question goes
  to him until it's answered — check the live-status gates.

## Voice and drafting

- JD drafts in his own voice; Claude checks and tightens rather than
  ghostwriting wholesale.
- Minimize em-dashes/en-dashes in fresh conversational output — prefer
  commas, parentheses, periods, restructured sentences, or an occasional
  semicolon. Heavy dash use reads as AI-generated and should be avoided.
- Dash-policing is skipped during complex document reconciliation work; a
  single cleanup pass happens afterward if needed, not mid-task.
- RJ is always **"Rev. James"** or **"RJ,"** never "Fr. James."

## Close-out checklist for every RECONCILE pass

1. Report starting stamps and diagnose any drift before editing (see above).
2. Apply edits via anchor-based string replacement.
3. Bump the document stamp **and** the `PROJECT_STATE.md` §4 registry cell
   together, in the same pass, for every file touched.
4. Prepend one changelog entry per document per pass — never two, never
   altered after the fact.
5. Run `python3 validate_project.py`. Report the **coverage summary**
   (files examined per check) before the error count — a clean run over
   the wrong file set is not a clean run.
6. Confirm `git status` shows every registered file that changed, commit
   the full set together, and push.
7. If this was an interrupted pass: do not commit. Say what's owed instead.
