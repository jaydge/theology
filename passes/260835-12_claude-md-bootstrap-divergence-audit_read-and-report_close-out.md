# 260835-12 — `CLAUDE.md` / `Project_Bootstrap_Prompt.md` divergence audit (close-out)

**Mode:** READ-AND-REPORT. No live document was edited. Every resolution below is a
proposal only, per the brief ("propose, don't apply").
**Scope:** `CLAUDE.md` and `Project_Bootstrap_Prompt.md`, section by section, plus the
`PROJECT_STATE.md` §4 registry cells for both.
**Committed:** nothing. **No `.diff` accompanies this pass** — nothing on disk changed,
so there is no diff to ship. This follows the same convention as the other
read-and-report passes in this series (`260834-6`, `260834-7`, `260835-6`), which shipped
a close-out only.

---

## Gate

| Item | Value |
|---|---|
| `git rev-parse HEAD` | `98660cab503358084425e482cee5d75a75ce80be` |
| Branch | `main` |
| `git status --short` | empty (clean tree) at gate |
| Validator baseline | **82 ok · 9 warnings · 0 errors**, exit 0 — identical cell-for-cell to the `260835-11` gate (see below) |
| `CLAUDE.md` own stamp (L3) | `260728-2` |
| `PROJECT_STATE.md` §4 registry cell for `CLAUDE.md` (L1271) | `260728-2` |
| `CLAUDE.md` stamp cross-check | ✅ **AGREE.** No drift. |
| `Project_Bootstrap_Prompt.md` own stamp (L3) | `260816-1` |
| `PROJECT_STATE.md` §4 registry cell for `Project_Bootstrap_Prompt.md` (L1268) | `260816-1` |
| `Project_Bootstrap_Prompt.md` stamp cross-check | ✅ **AGREE.** No drift. |
| Highest existing `26xxxx-N` in repo | `260835-11` (confirmed both by `PROJECT_STATE.md`'s own "Last updated" line and by the HEAD commit message) |
| Next-free pass stamp | **`260835-12`** — every apparent `260835-12` hit on a repo-wide grep is prose inside earlier close-outs (`260835-8`, `260835-9`, `260835-11`) describing searches for their own absence, the same false-positive shape those passes already diagnosed. No real `260835-12` exists. |

### ⚠️ Known, pre-existing, benign artifact — not this pass's business

A zero-byte `.git/index.lock` is a recurring permissions artifact of the sandboxed FUSE
mount (diagnosed at `260835-3`, re-confirmed benign at `260835-9` and `260835-11`). This
pass used `git --no-optional-locks` for every git read, created no lock, removed no lock,
and made no commit — nothing here depends on git write access. Flagged only because
`CLAUDE.md`'s own emission-discipline section (see Divergence 12 below) is exactly the
rule this artifact tests, so it seemed worth confirming this pass didn't trip it.

### Baseline warnings (all 9, unchanged from the `260835-11` gate — reproduced for the record, not touched by this pass)

1. `WARN [C1] src/SRC_Discord_RPW.md` — 2 relative timestamps outside message headers.
2. `WARN [C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` — no parseable stamp; registry says `260832-2`.
3. `WARN [C3] tools/transcribe_yt.py` — no parseable stamp; registry says `260833-7`.
4. `WARN [C4] St_Francis_EMC_Distinctives.md` — 2 stale answered-question passages.
5. `WARN [C5] RJ_Final_Question_List.md` — 17 volatile-state assertions.
6. `WARN [C5] RJ_Incense_Analysis.md` — 9 volatile-state assertions.
7. `WARN [C5] St_Francis_EMC_Distinctives.md` — 7 volatile-state assertions.
8. `WARN [C10]` — §15's newest `LS` citation is 8 findings behind the ledger.
9. `WARN [C11]` — outline last checked against `IP-97`; ledger now runs to `IP-108`, 11 unreviewed.

---

## Framing: this audit was already owed, and was already partially started

`CLAUDE.md` L9–11 flags its own registration as incomplete work: *"Registration is not
reconciliation: nobody has yet audited this file against `Project_Bootstrap_Prompt.md` for
divergence. That audit is owed work."* The `260835-8` pass, while checking a narrower
question (whether it was safe to delete two project-knowledge copies), incidentally found
two real divergences and explicitly declined to run the full audit, recording them "only
so they are not lost." This pass is that audit, run in full. Both `260835-8` findings are
confirmed below (Divergences 1 and 2) and integrated into a complete list.

**Headline finding, stated up front because it reframes the whole audit:** the "canonical
wins" rule (`CLAUDE.md` L13–18: *"If this file and that one ever diverge,
`Project_Bootstrap_Prompt.md` wins"*) assumes `Project_Bootstrap_Prompt.md` is the more
current document. **On several of the divergences below, it is not.**
`Project_Bootstrap_Prompt.md` was last substantively edited `260816-1`, and several of its
"Source handling" claims describe a **Claude-Project-knowledge-centric** working model
(`SRC_Manifest.md` "lives in project knowledge," transcripts excluded from "Claude Project
knowledge" only) that predates, or was never reconciled against, the **git-repo-centric**
model this project actually runs today (`ORCHESTRATION.md` §1: *"One git repository is the
single source of truth"*; `SRC_Manifest.md` is in fact a tracked, registered, hash-guarded
repo file, not a project-knowledge artifact). `CLAUDE.md`, as the newer-in-substance
working copy that Claude Code actually loads, has in places drifted **ahead** of
`Project_Bootstrap_Prompt.md`, not behind it. A literal "the canonical file wins" reading
would, in those places, silently revert the project to a stale and in one case factually
false claim about its own architecture.

---

## Full divergence list

Numbered for reference. Severity tags: 🔴 **critical** (safety/integrity rule missing or
reversed), 🟠 **major** (real content gap, mitigated elsewhere or lower-stakes), 🟡
**moderate**, ⚪ **minor/cosmetic**, 🔵 **structural** (section present in one file only,
not a contradiction).

### 1. 🔴 Transcript git-exclusion silently dropped in `Project_Bootstrap_Prompt.md`

*(This is `260835-8`'s first found divergence — confirmed, and given full authority analysis here.)*

- **`CLAUDE.md` L47:** *"Full audio/video transcripts stay **OUT of git and out of
  project knowledge**."*
- **`Project_Bootstrap_Prompt.md` L17:** *"Full transcripts stay **OUT of Claude Project
  knowledge**."* — silent on git entirely.

**Which file is right, checked against actual practice:** `ORCHESTRATION.md` §2's path
table places transcripts at `~/EMC/original transcripts/…`, explicitly **outside**
`~/EMC/theology` (the git repo). Current practice matches `CLAUDE.md`'s stricter text.

**Authority: `CLAUDE.md` is correct; `Project_Bootstrap_Prompt.md` is incomplete and should
be brought up to match it** — the one case in this audit where the "working copy" is
righter than the declared "canonical" file. Under the literal precedence rule as written,
`Project_Bootstrap_Prompt.md` wins, and its silence would license treating
git-inclusion of a transcript as merely a project-knowledge problem, not a git one. No
incident has occurred from this yet, but the gap is live.

**Proposed resolution:** amend `Project_Bootstrap_Prompt.md` L17 to read *"Full transcripts
stay OUT of git and out of Claude Project knowledge"* (matching `CLAUDE.md`'s wording),
with a changelog entry noting the correction and citing this audit. Draft text:

> - Full transcripts stay OUT of git and out of Claude Project knowledge. They live in a
>   stable local folder, unmodified from their original uploaded form, and are attached to
>   a chat message only for the session that needs them. Do not split a multi-item
>   transcript file into smaller files, re-download, re-encode, or normalize line endings —
>   any of these changes invalidates previously-logged byte offsets.

---

### 2. ⚪ "unmodified from original uploaded form" — present only in `Project_Bootstrap_Prompt.md`

*(`260835-8`'s second found divergence — confirmed.)*

- **`Project_Bootstrap_Prompt.md` L17–18:** *"They live in a stable local folder,
  **unmodified from their original uploaded form**…"*
- **`CLAUDE.md` L47–51:** no equivalent phrase; the substance is covered by the adjacent
  never-split/re-encode/normalize clause, but the word **unmodified** never appears.

**Authority: `Project_Bootstrap_Prompt.md` is correct and slightly more explicit here** —
this is the one divergence in this audit where the literal precedence rule resolves
correctly on its own. No safety gap: the operative content (don't split/re-encode/
normalize) is present in both files.

**Proposed resolution:** low priority. If `CLAUDE.md`'s source-handling section is revised
for Divergence 3 anyway (below), fold in *"unmodified from their original uploaded form"*
at the same time.

---

### 3. 🔴 Two entire adopted data-integrity conventions (`260816-1`) are absent from `CLAUDE.md` — and absent everywhere else in the repo too

`Project_Bootstrap_Prompt.md` §Source handling carries two ⭐⭐-marked standing conventions,
both dated `260816-1` in its own changelog:

- **"A trimmed or replaced original is recorded, and the survivor is marked
  not-the-original"** (L37–67) — when an as-recorded source file is trimmed, re-encoded,
  split, or replaced, the event must be logged in `SRC_Manifest.md` **and** the surviving
  file must be marked as **not** the as-recorded original, even if it inherited the
  original's filename. Reasoning given: a filename is a provenance claim a hash check
  cannot verify (the `W17` stamp-defect shape).
- **"Dual independent ASR renderings of one capture — the verification protocol"**
  (L69–100) — where two ASR systems transcribe one capture: agreement gives only
  provisional confidence, divergence goes to a verification queue resolved **by ear against
  the audio** (never against the second transcript), neither transcript is authoritative on
  wording alone, and diarization is a navigation layer only, never attribution of record.

**Neither block appears in `CLAUDE.md`.** I grepped `PROJECT_STATE.md` and
`ORCHESTRATION.md` for both ("trimmed or replaced," "not-the-original," "DUAL
INDEPENDENT," "dual-ASR," "`W17`") and found **zero genuine matches** — the one apparent
hit in `PROJECT_STATE.md` is an unrelated phrase ("retained word for word and are not
deleted, trimmed or replaced," about `IP` bullet preservation, not source files).

**Why this is the most serious item in the audit.** `CLAUDE.md`'s own header calls it
*"a working copy for Claude Code"* and `PROJECT_STATE.md` §4 (L1271) annotates its registry
row *"Claude (read first by Claude Code)."* `CLAUDE.md`'s own last stamp is `260728-2` —
**before** `260816-1`, when these two conventions were adopted. A Claude Code session that
loads `CLAUDE.md` as its automatic context has no way to learn either rule exists unless it
separately reads `Project_Bootstrap_Prompt.md`, which nothing in `CLAUDE.md` itself
instructs it to do (`CLAUDE.md`'s "Before doing anything" checklist names only
`PROJECT_STATE.md` and the validator). Both conventions are directly load-bearing for the
project's central verbatim-quote discipline — exactly the kind of rule a session should not
be able to miss.

**Authority: `Project_Bootstrap_Prompt.md` is authoritative and correct here; `CLAUDE.md` is
simply stale** and needs both blocks added, in full or by close paraphrase.

**Proposed resolution:** insert both `Project_Bootstrap_Prompt.md` blocks (L37–100)
into `CLAUDE.md` §Source handling, immediately after the existing Anglican 101 capture
policy bullet (after L73), condensed slightly to match `CLAUDE.md`'s tighter house style but
preserving every normative clause (record + mark together; audio over second transcript;
diarization is navigation only; key-terms lists are tooling, not a correction map). A full
draft insertion is available on request; not written out in full here to keep this
close-out from duplicating ~65 lines verbatim when the source text already exists at a
named, stable location.

---

### 4. 🟠 Discord / live-dialogue-logs capture-method section has no `CLAUDE.md` counterpart

`Project_Bootstrap_Prompt.md` §Discord / live dialogue logs (L102–127) specifies: verbatim
activity logs kept as raw record only (no analysis inline); capture is a **manual
full-thread copy/paste**, never an export tool, and any changelog claim that
`DiscordChatExporter` was used is retracted as false; **full-thread recapture on every
reply, never an append**, so `git diff` surfaces edits; Discord messages are mutable, so any
diff touching an already-captured message is a dated correction, never a silent absorb; and
the specific tested limits of copy/paste (no `(edited)` marker, bare same-day timestamps
resolved by report, paragraph breaks preserved).

**`CLAUDE.md` has none of this.** Its only Discord mention is the unrelated one-committal-
question-per-turn dialogue rule (L152).

**Partially mitigated, not fully:** `ORCHESTRATION.md` §8 restates the core of it —
*"Discord access is manual, always: JD copies the full thread himself… Full-thread
recapture, never an append… Corrections are dated notes beside the original, never silent
rewrites"* — and the stated project read order is `PROJECT_STATE.md` → `ORCHESTRATION.md` →
task, so a session following that order does encounter the substance. But `CLAUDE.md`
itself, read alone, carries none of it, and the specific copy/paste failure modes
(missing `(edited)` marker, bare timestamps) exist **only** in
`Project_Bootstrap_Prompt.md` — not even `ORCHESTRATION.md` has those.

**Authority: `Project_Bootstrap_Prompt.md` is authoritative.** Recommend `CLAUDE.md` add at
minimum a cross-reference rather than staying silent.

**Proposed resolution:** add one bullet to `CLAUDE.md` §Source handling or a new short
"Discord capture" subsection: *"Discord capture method and copy/paste limits: see
`ORCHESTRATION.md` §8 and `Project_Bootstrap_Prompt.md` §Discord / live dialogue logs."*

---

### 5. 🟡 `SRC_Manifest.md`'s storage location is stated, and stale, in `Project_Bootstrap_Prompt.md`

- **`Project_Bootstrap_Prompt.md` L23:** *"A `SRC_Manifest.md` **lives in project
  knowledge**: for each transcript file, it records the sha256 hash and the byte range…"*
- **`CLAUDE.md` L52–56:** makes no location claim at all — calls it "the source registry"
  and describes its contents, without saying where it lives.

**Checked against actual practice:** `SRC_Manifest.md` is a git-tracked file at repo root
(895 KB on disk), registered in `PROJECT_STATE.md` §4, and guarded by validator checks `C0`
(path resolution), `C3` (stamp-vs-registry), and `C6` (hash-vs-manifest) — all `ok` in this
pass's baseline. It is not a project-knowledge artifact in current practice.

**Why this is worse than a simple omission:** unlike Divergences 1, 3, and 4 — where
`Project_Bootstrap_Prompt.md` is silent and `CLAUDE.md` fills the gap — here
`Project_Bootstrap_Prompt.md` makes an **affirmative claim that is false** under the
project's current architecture. A literal "canonical wins" reading doesn't just lose a
rule, it asserts something wrong about where the single most load-bearing registry file in
the project actually is.

**Authority: neither file states the current truth outright** (`CLAUDE.md`'s silence is
merely incomplete; `Project_Bootstrap_Prompt.md`'s claim is actively wrong). Recommend
`CLAUDE.md` gets an explicit, correct statement rather than leaving it implicit.

**Proposed resolution:** amend `Project_Bootstrap_Prompt.md` L23 to drop the location claim
or generalize it (*"A `SRC_Manifest.md` is the source registry: for each transcript
file…"*, matching `CLAUDE.md`'s framing), and add one clause to `CLAUDE.md` stating plainly
that in this repo `SRC_Manifest.md` is a git-tracked file at repo root, not a
project-knowledge artifact.

---

### 6. 🟡 `SRC_Manifest.md`'s "sessions-ingested table" / identity-layer concept exists only in `CLAUDE.md`

`CLAUDE.md` L53–56 describes a second registry component beyond hash+byte-range — a
sessions-ingested table (session + date + coverage) — and explains why it's needed: *"a
hash check catches re-uploads of the same file, not a second capture of the same event."*
`Project_Bootstrap_Prompt.md`'s description of `SRC_Manifest.md` (L23–25) covers only the
hash/byte-range component; the re-upload-vs-recapture distinction and the sessions-ingested
table do not appear there at all.

**Authority: `CLAUDE.md` is ahead here** — this looks like a genuine methodological
refinement developed after `Project_Bootstrap_Prompt.md`'s manifest description was
written, and it is not project-specific (the re-upload/re-capture distinction applies to
any project using this template with recorded sessions). Per `Project_Bootstrap_Prompt.md`'s
own footer (*"update it… when new recurring conventions emerge that should apply
project-wide"*), this is a candidate for promotion that appears to have been missed.

**Proposed resolution:** add the sessions-ingested-table concept and its rationale to
`Project_Bootstrap_Prompt.md`'s `SRC_Manifest.md` description.

---

### 7. 🟡 Three dated standing-rule blocks live only in `CLAUDE.md`, apparently un-promoted despite `Project_Bootstrap_Prompt.md`'s own promotion policy

All three are dated `260726-1` — before `CLAUDE.md`'s own last stamp (`260728-2`), and well
before `Project_Bootstrap_Prompt.md`'s last edit (`260816-1`), meaning
`Project_Bootstrap_Prompt.md` had a later opportunity to absorb them and did not:

- **Attribution discipline, `CLAUDE.md` L125–130:** *"⭐ Standing rule (260726-1): his own
  example outranks the project's version of it"* — when new source material shows the
  subject has already used an argument in their own words, the project's paraphrase of that
  argument is recast as theirs, everywhere it appears.
- **Attribution discipline, `CLAUDE.md` L131–134:** *"⭐ Standing permission (260726-1)":*
  documents may be updated without asking first where the subject's position is clear on the
  record; ambiguous readings still come back as questions.
- **Strategic/dialogue discipline, `CLAUDE.md` L161–165:** *"⚠️ Posture note (260726-1)":*
  the project owner is now willing to tip his hand on argument direction where it moves
  discussion faster — concealment of direction only, lock-before-port still governs
  sequencing, and hybrid pre-emption still never enters posted text.

**None of these contradicts `Project_Bootstrap_Prompt.md`** — it states no competing rule
on any of the three, so this is not a "weaker rule wins" risk in the way Divergences 1, 3,
4, and 5 are. It's a **process-compliance gap**: `Project_Bootstrap_Prompt.md`'s own footer
(L199–201) commits to absorbing "new recurring conventions… that should apply
project-wide," and the first two of these three read as generalizable dialogue-methodology
rules, not RJ-specific facts (the "his own example outranks" rule and the "tip his hand"
posture note don't name Rev. James or St. Francis anywhere in their text).

**Authority: ambiguous by design** — this is JD's call on whether these were meant to stay
CLAUDE.md-local operational notes or were simply never promoted. Flagging rather than
resolving.

**Proposed resolution (offered, not applied):** promote the first two (attribution
standing rule + permission) into `Project_Bootstrap_Prompt.md` §Attribution discipline
verbatim; promote the posture note into §Strategic/dialogue discipline, generalizing "his
own" language exactly as `CLAUDE.md` already generalizes it in Attribution discipline's
prose. If JD judges any of the three to be genuinely project-specific rather than
generalizable, no action is needed — but that judgment hasn't been made explicit anywhere
in either file, and this audit is the first time the gap has been surfaced.

---

### 8. ⚪ Changelog-correction clarification exists only in `CLAUDE.md`

`CLAUDE.md` L147–148 amplifies the shared "changelog entries are historical record and
never altered, only added to" rule (present in both files, near-identically worded) with a
clarification neither file's other copy has: *"If a past entry turns out to be wrong,
correct it in a **new** entry that says so — don't rewrite history."*
`Project_Bootstrap_Prompt.md` L166–168 states the base rule but not this corollary.

**Authority: `CLAUDE.md` is ahead; generalizable, no RJ-specific content.** Same promotion
pattern as Divergence 7.

**Proposed resolution:** add the same clarifying sentence to
`Project_Bootstrap_Prompt.md`'s Numbering and versioning section.

---

### 9. ⚪ `CLAUDE.md` carries no changelog of its own — self-resolving, not a live risk

Every other canonical document in the registry carries a changelog, including
`Project_Bootstrap_Prompt.md` itself (L203–207). `CLAUDE.md` has none, despite stating the
shared rule that *"every canonical document carries a permanent, prepended changelog"*
(L145) and despite tracking dated standing rules internally (the three `260726-1` items in
Divergence 7) with no changelog entry marking when they were added.

**This resolves itself on a close reading, not a live gap:** `CLAUDE.md`'s own header
(L14) calls `Project_Bootstrap_Prompt.md` *"the canonical, **versioned, changelogged**
document,"* implicitly distinguishing itself as the non-canonical, non-changelogged working
copy. So the shared "every canonical document…" rule, read together with that header
framing, doesn't actually obligate `CLAUDE.md` to carry one.

**Flagged anyway because the exemption is implicit, not stated as an explicit carve-out
next to the rule itself** — a future editor applying the changelog rule literally to
`CLAUDE.md` (a file that is, after all, versioned and registry-guarded) could reasonably
expect one. No resolution needed unless JD wants the exemption made explicit.

---

### 10. ⚪ Numbering-prefix example list is stale in `Project_Bootstrap_Prompt.md`

`CLAUDE.md` L138: *"(`IP`, `DQ`, `GV`, `RC`, `BP`, `RV`, `EXT`, and other batch-specific
prefixes)"*. `Project_Bootstrap_Prompt.md` L161–162: *"(e.g. IP, DQ, GV, RC, BP, EXT, and
other batch-specific prefixes)"* — omits `RV`. `RV` is a real, active,
validator-tracked prefix (`RV-1..63`, `C2`-guarded, confirmed `ok` in this pass's baseline).

**No rule is actually violated** — both lists are illustrative ("and other batch-specific
prefixes"), not exhaustive, so this is cosmetic drift, not a functional gap.

**Proposed resolution:** add `RV` to `Project_Bootstrap_Prompt.md`'s list for consistency,
next time that file is touched for another reason. Not worth a standalone pass.

---

### 11. 🔵 `under src/` directory qualifier — `CLAUDE.md`-only, and correctly so

`CLAUDE.md` L44–46 states the `SRC_` prefix rule applies "under `src/`";
`Project_Bootstrap_Prompt.md` L14–16 states the same prefix rule with no directory,
appropriately, since it is a reusable template not tied to any one repo's folder layout.
**Not a divergence** — correct specialization, no resolution needed.

---

### 12. 🔵 Four `CLAUDE.md` sections have no `Project_Bootstrap_Prompt.md` counterpart

- **"Before doing anything"** (L30–40) — the gate/stamp-cross-check procedure this very
  audit's Gate table follows.
- **"⚠️ Emission discipline"** (L88–108) — the atomic-commit rule written after the real
  mixed-vintage-tree incident.
- **"Close-out checklist for every RECONCILE pass"** (L182–196).
- **"What this repo is"** (L20–28) and the Anglican 101 capture policy bullet (L66–73) —
  pure project-identity/project-specific content.

**Not treated as contradictions.** `Project_Bootstrap_Prompt.md`'s own stated purpose is a
generic, reusable template ("paste this at the start of a new project") that assumes
neither git nor Claude Code specifically; these four are git-repo/Claude-Code-operational
content `Project_Bootstrap_Prompt.md` has no obligation to carry. Listed here only because
the brief asked for every divergence, structural or substantive, and these are the
remaining places the two files' section lists don't line up. No authority conflict exists
— `Project_Bootstrap_Prompt.md` makes no competing claim on any of the four topics.

---

## Summary table

| # | Topic | Severity | Which file is authoritative | Naive-precedence risk? |
|---|---|---|---|---|
| 1 | Transcript git-exclusion | 🔴 critical | `CLAUDE.md` (Bootstrap incomplete) | **Yes** — Bootstrap wins, drops git rule |
| 2 | "unmodified…uploaded form" wording | ⚪ minor | `Project_Bootstrap_Prompt.md` | No — precedence resolves correctly |
| 3 | Trimmed-original marking + dual-ASR protocol entirely missing from `CLAUDE.md` | 🔴 critical | `Project_Bootstrap_Prompt.md` | **Yes** — CC's auto-loaded file has neither rule |
| 4 | Discord capture-method section missing from `CLAUDE.md` | 🟠 major | `Project_Bootstrap_Prompt.md` | Partial — mitigated by `ORCHESTRATION.md` §8 |
| 5 | `SRC_Manifest.md` "lives in project knowledge" — stale claim | 🟡 moderate | Neither states current truth; Bootstrap affirmatively wrong | **Yes** — Bootstrap asserts a false architecture |
| 6 | Sessions-ingested-table concept missing from Bootstrap | 🟡 moderate | `CLAUDE.md` | No — omission, not contradiction |
| 7 | Three `260726-1` standing-rule blocks un-promoted | 🟡 moderate | Ambiguous (JD's call) | No — no competing Bootstrap rule |
| 8 | Changelog-correction clarification missing from Bootstrap | ⚪ minor | `CLAUDE.md` | No |
| 9 | `CLAUDE.md` has no changelog | ⚪ minor | Self-resolved by `CLAUDE.md`'s own header | No |
| 10 | `RV` missing from Bootstrap's prefix example list | ⚪ trivial | `CLAUDE.md` | No — illustrative list, not exhaustive |
| 11 | `under src/` qualifier | 🔵 structural | Both correct for their scope | No |
| 12 | Four sections unique to `CLAUDE.md` | 🔵 structural | Both correct for their scope | No |

**Four items (1, 3, 4, 5) carry real naive-precedence risk** — the literal "canonical wins"
rule would, on those four, pick the weaker, missing, or stale rule. All four point the same
direction: `Project_Bootstrap_Prompt.md` needs to absorb content `CLAUDE.md` already has
correct (1, 5) or that only `Project_Bootstrap_Prompt.md` itself has but `CLAUDE.md` never
received (3, 4) — i.e., **this is not a case of one file being generally more reliable than
the other; both directions of drift are present**, which is exactly what an audit rather
than a spot-check was needed to surface.

---

## What was declined, and what came back empty

Per `passes/README.md`: *"A close-out that reports only successes is under-reporting."*

- ⛔ **Declined:** editing `CLAUDE.md` or `Project_Bootstrap_Prompt.md`. Every resolution
  above is a draft/proposal only, per the brief.
- ⛔ **Declined:** resolving Divergence 7 (the three `260726-1` standing-rule blocks) one
  way or the other — genuinely JD's call, not inferable from either file's own text.
- ⛔ **Declined:** writing out the full ~65-line insertion text for Divergence 3 verbatim in
  this close-out, since the source text already exists intact at a named, stable location
  (`Project_Bootstrap_Prompt.md` L37–100) and reproducing it here would just create a third
  copy to go stale. Available on request if JD wants a ready-to-paste block.
- ⛔ **Declined:** touching `PROJECT_STATE.md` beyond reading its §4 registry cells for the
  gate table. No registry cell needed a bump — neither file's stamp changed.
- ⛔ **Declined:** committing. Nothing was staged; `git status` is unchanged from gate.
- 🔍 **Came back empty:** a search for any divergence where `CLAUDE.md` states a rule that
  actively **contradicts** (rather than omits or extends) `Project_Bootstrap_Prompt.md`.
  Every difference found is either an omission, a stale claim, or an addition — none is a
  head-on contradiction of stated substance. The two files disagree by silence and drift,
  not by asserting opposite rules.
- 🔍 **Came back empty:** grep for the two `260816-1` conventions (trimmed-original marking,
  dual-ASR protocol) anywhere in `PROJECT_STATE.md` or `ORCHESTRATION.md`. Confirmed absent
  project-wide outside `Project_Bootstrap_Prompt.md` itself — this is what makes Divergence
  3 critical rather than merely duplicated-elsewhere.

---

## Validator: after vs. baseline

**After: 82 ok · 9 warnings · 0 errors, exit 0. Identical to baseline, cell for cell.** No
check changed status — expected, since no live file was edited this pass.

---

## Files changed

None. `git status --short` is empty both before and after this pass, aside from this
close-out file itself landing untracked in `passes/`.

```
?? passes/260835-12_claude-md-bootstrap-divergence-audit_read-and-report_close-out.md
```

⛔ **Nothing staged, nothing committed.** `git add` and `git commit` are JD's, per standing
convention, whenever he decides which (if any) of the proposed resolutions to act on.
