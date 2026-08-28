# ORCHESTRATION — how work gets done on this project

**Last updated: 260835-24** (date-stamped, format yymmdd-iteration) ⭐⭐⭐ **260835-24 — ONE NEW §8 STANDING INSTRUCTION: THE OFFICE RULE. CHANNEL IS NOT THE AXIS; ORIGINAL TEACHING CONTENT IS, AND THE RULE APPLIES UNIFORMLY TO BOTH CHANNELS.** ⛔⛔ **It replaces the incoherent channel-scoped handling flagged as owing a ruling at `260835-23`** — offices `EXCLUDE`d on `EXT-3` per an earlier JD instruction, `INCLUDE`d on `EXT-2`, with seven more `EXT-2` office rows added on that precedent. **Three cases: pure office with no original teaching → `DECLINED-office`; office containing a homily, sermon or other original teaching → `INCLUDE`; title and description do not settle it → `UNCERTAIN`, never a guess either way.** ⭐⭐⭐ **The governing case is `IGNmKMXhL1Q` (`File 60`), a Morning Prayer WITH a homily — a blanket office exclusion would have lost it — and the hard part is that this uploader records Sunday Morning Prayer both with and without a homily and does not reliably flag which in the title, so title silence is not evidence of absence.** ⛔⛔⛔ **The rule's other half: a READ-ALOUD ATTRIBUTION LAYER IS REQUIRED for any office row that is `INCLUDE`d — the liturgical text is not his own words even when the homily is (`File 60`/`File 68`/`File 69` precedent, `File 69` being read-aloud 100% and carrying first-person eucharistic-presence language that is the Prayer Book's and not his).** *Previous header summary retained:* ⭐⭐⭐ **260835-22 — TWO NEW §8 STANDING INSTRUCTIONS, both long-owed and both previously homeless. (1) CHANNEL OWNERSHIP IS NOT A SPEAKER WARRANT** — owed since `260835-14`, whose Fr. Ray result established it (two "Fr. Ray Teaching About…" videos on Rev. James's own `EXT-2` channel are entirely another priest's teaching, predating his diaconate); `260835-18` supplied the mechanism (Fr. Ray was his own rector) but expressly did not write the amendment. **Speaker identity must be established from content in every case**, with the non-warrants enumerated (ownership, title, uploader, diarization label, speaking duration, folder location, registration itself). **(2) PROGRESS REPORTING FOR DELEGATED SESSIONS** — a brief status line roughly every ten minutes or at each major task boundary, naming task, progress and blockers. ⚠️ **`260835-21` grepped the repo and found this convention written down NOWHERE, despite every delegated prompt carrying it.** ⛔ **Status lines are instrumentation, never deliverables, and never abbreviate the close-out.** *Previous header summary retained:* ⭐ **260835-15 — new §8 standing instruction: the SINGLE-LABEL, NOT CONFIRMED SINGLE-VOICE speaker-warrant class. See §8 for the rule and its two known instances.**

> **What this file is.** The durable *working conventions* — how a batch
> gets from a YouTube URL to a committed finding, and which mistakes keep
> recurring. ⛔ **It holds NO volatile state.** Next-free numbers, open
> questions, gate status, and current owed items live in
> `PROJECT_STATE.md`, which is read first, always. Evidence and
> attribution rules live in `PROJECT_STATE.md` §5 and are not duplicated
> here.
>
> **Read order for any new thread:** `PROJECT_STATE.md` → this file →
> whatever the task names.

---

## 1. The core pattern: delegate, then verify independently

**One git repository is the single source of truth.** Nothing important
lives only in a chat thread.

**The orchestration thread does not edit the repo**, except for small,
fully self-verified fixes — a handful of lines, checked against the real
file, validator run, diff reverse-apply-tested. Anything larger is
delegated.

**Substantive work is delegated** to a Cowork task ("On your computer"
mode) or Claude Code, via a detailed written prompt with explicit
gate-checks.

⭐⭐⭐ **Every returned diff is independently verified before JD commits.**
Orchestration clones the repo fresh, applies the diff to that clean
clone, runs the validator, and spot-checks the load-bearing claims
against the actual corpus text. ⛔ **This is not optional and has caught
real errors repeatedly** — stale baselines, phantom numbering, a
misattributed quote, a silently duplicated source, a hash computed before
the file's own changelog entry was added.

**JD commits and pushes from his own terminal**, never from inside the
working-thread tool. Final human gate; stays a hard boundary.

⚠️⚠️ **One thread touching this repo at a time.** ⛔ **Parallel threads
editing the same files have caused real collisions** — a `DQ` posted in
one thread and never captured by another, a diff test-applying clean in
orchestration's own sandbox while a stale clone masked that it had
already landed via a different path. If a second thread must run, tell
orchestration explicitly before it starts, not after.

---

## 2. Paths

Everything under `~/EMC/`:

| Path | What |
|---|---|
| `~/EMC/theology` | the git repo |
| `~/EMC/original transcripts/video transcripts/` | livestream/video sources, in `batchN/` subfolders |
| `~/EMC/original transcripts/in person classes/` | A101 and other live-class sources, in date folders |
| `~/EMC/blog_archives/` | blog corpus |
| `~/EMC/downloads/` | patch/diff files handed to JD |
| `~/EMC/theology/passes/` | ⭐ pass artifacts, committed — see §4 |

⛔ **Not `/Users/jd/Downloads`** (the macOS one) and not Dropbox — the
repo was moved out of Dropbox at `260828-2` because its sync daemon
contended with `.git/`. Attach `~/EMC` to a Cowork task and both the repo
and the archive are covered.

---

## 3. The batch workflow, end to end

1. **JD transcribes.** `transcribe` (§6) turns a YouTube URL into the
   project's standard six-file set.
2. **Orchestration writes the intake prompt** — naming the exact HEAD to
   gate on, the exact validator baseline, the sources, what to read the
   material against by finding number, and the deliverables.
3. **The working thread runs intake and reconcile together**, applies
   edits directly, re-runs the validator, and **stops before committing**.
4. **It writes two artifacts** into `passes/` (§4) and commits nothing.
5. **Orchestration verifies** against a fresh clone (§1).
6. **JD applies, validates, commits, pushes** from his own terminal.

⛔ **Never two intakes before a reconcile.** Each batch lands fully —
applied, verified, committed — before the next begins.

**Any new file created for the project — a research document, an
analysis, anything — is created inside a working session with actual
repo access (Cowork or Claude Code), not drafted in an ordinary chat and
handed over afterward.** ⚠️ **A file assembled in a plain chat thread has
no repo, no git, nothing to commit — "commit this" in that context is not
actionable, and the file ends up untracked and undiscussed until someone
notices it later.** If research produces something worth keeping,
generate it (or move it) inside a session that can actually register it,
and tell orchestration before it lands, not after.

---

## 4. ⭐ Pass artifacts live in the repo, not in chat attachments

**Every delegated pass writes two files into `passes/`:**

```
passes/<stamp>_<short-name>.diff
passes/<stamp>_<short-name>_close-out.md
```

e.g. `passes/260831-1_batch5.diff`.

⭐⭐ **They are committed alongside the change they describe**, in the same
commit. That makes the reasoning behind every pass permanently
recoverable from git history, and it means **orchestration reads them
from a fresh clone rather than needing them uploaded** — which is the
point: chat attachments are a finite resource and this workflow no longer
spends them per batch.

**The close-out is a real document, not a receipt.** It records what was
found, what was declined and why, what was checked and came back empty,
and anything the pass could not resolve. ⛔ **A pass that reports only
success is under-reporting.**

⚠️ **The diff in `passes/` is the diff as applied.** Since JD applies it
before committing, the committed diff file describes the very commit it
travels in — self-referential but accurate, and far more useful than
having it live outside the repo.

⚠️ **A file can land in `passes/` without being registered in
`PROJECT_STATE.md`'s file table** if it's reference material rather than
a pass artifact proper (e.g. process documentation JD drops in for
orchestration's own benefit). ⛔ **That's fine and doesn't need forcing
into the registration discipline** — only source transcripts, findings
corpora, and documents a future pass might cite need a registry row.

---

## 5. Hand-off format

Every hand-off from orchestration to JD ends with a block naming:

- **📥 any file to download first** — stated in bold at the TOP of the
  message, not the bottom. ⚠️ **JD has repeatedly run commands before
  noticing a file needed downloading; this is a real, recurring cost.**
- **venue** — Cowork desktop "On your computer", or Claude Code
- **approval setting**
- **what to attach** — normally just `~/EMC`
- **what to expect back**

**Commit blocks are given verbatim, ready to paste**, and always include
`rm -f .git/index.lock` before `git add` (§7).

---

## 6. Transcription pipeline

**`~/bin/transcribe`** → wrapper → `~/bin/transcribe_yt.py`, running in
the venv at `~/.venvs/transcribe`.

```
transcribe --url "<youtube url>" --name <Basename> --speakers <n> \
  --prompt "<one plain sentence describing the recording>" \
  --outdir "~/EMC/original transcripts/video transcripts/batchN"
```

**Produces six files per video:** `-sentences.json` (⭐ PRIMARY,
diarized), `-timestamps.json` (word-level, navigation only),
`-transcript.srt`, `-transcript.txt`, `-youtube.srt` (⭐⭐ YouTube's own
captions — an INDEPENDENT second rendering), and `-meta.json`.

⭐⭐⭐ **`-meta.json` is the source of record for registration** — title,
video id, url, channel, ISO upload date, `was_live`, duration, the exact
AssemblyAI config, the key-terms list used, and sha256 of every output.
⛔ **Do not re-derive by hand what it supplies. Do verify its recorded
hashes against the files.**

**Key terms** are read automatically from `asr_keyterms_A101.md`. ⚠️
**Watch for `key terms loaded: N` in the output** — Batches P1-P3 ran
without it, which is a real difference in capture quality and is recorded
in their registrations.

**Cookies** come from a file at `$YTDLP_COOKIES` (exported once with a
browser extension; valid for months). ⛔ **Reading a running browser's
cookie store directly yields a partial set and silently changes which
formats YouTube offers** — that failure cost a debugging cycle.

**Running several at once:** `~/bin/run_batch4.sh` is the template —
background jobs staggered ~8s apart, each logging to `batchN/logs/`.
⚠️ **Scripts run under `/bin/sh`, which does not read `~/.zshrc`** — call
`"$HOME/bin/transcribe"` by full path inside a script, never bare.

⏳ **Known issue, do not re-fix blindly:** the upload progress bar still
reports 100% immediately. Two attempts (capped reads; faster refresh)
did not resolve it. **Next attempt should investigate what
requests/urllib3 actually does with the reader object rather than
refining the current approach.**

---

## 7. Recurring failure modes — each has bitten at least once

**Stale git locks.** `.git/index.lock` or `.git/HEAD.lock` left behind by
a sandboxed tool that can create files but not always unlink them.
⛔ **A working thread must report a lock and stop, never delete one.**
JD clears it. Every commit block includes `rm -f .git/index.lock`
pre-emptively.

**Self-referential registry rows.** Bumping a file's own `Last updated:`
stamp while forgetting its row in `PROJECT_STATE.md` §4 — C3 catches it.
⚠️ **`PROJECT_STATE.md` and `SRC_Manifest.md` each have a row for
themselves.**

**Hashes computed too early.** Hashing a file *before* adding its own
changelog entry makes the recorded hash stale the moment the entry lands.
⛔ **Hash last, after every edit to that file is complete.**

**Attribution by adjacency.** Turn-tracing and topical fit are weaker
evidence than a speaker label or a doctrinal impossibility. **`LS-39` was
misattributed exactly this way** — a guest's clause read as his — and was
only caught by a later cross-check. ⛔ **Where diarization exists, it
governs.**

**Diarization establishes whose VOICE, not whose WORDS.** Chat questions,
quoted opponents, and read-aloud documents all carry the speaker's own
label. ⛔ **Response and review videos are the high-risk class: by
construction he characterizes positions that are not his.**

**Count-matching is not content-matching.** Two renderings both showing a
term N times does not mean they agree — `regulative` was 5·5 with two
sites differing.

**Term scans need speaker splits.** `element ×25` looked like `DQ-9`
movement; all 25 were false positives traced individually.

**Duplicate sources arrive disguised as new.** `a304`, `a303`, and the
`-youtube.en-orig.srt` files were all near- or byte-identical re-supplies.
⛔ **Duplicate-check by content before minting any tag.**

**Briefs can be wrong.** A prompt's stated premise has been falsified by
the repo more than once. ⛔ **The repo wins; flag the discrepancy, do not
silently reconcile it.**

**A local sandbox's `git apply --check` can fail while the same patch
lands cleanly on JD's actual machine.** ⚠️ **If orchestration's own clone
was made even slightly stale, a `--check` failure there is not
authoritative — re-clone fresh and re-check before assuming a real
conflict.** This produced a false "possible collision" scare once already.

**A working thread offering to "commit this" in a plain chat, without
repo access, cannot actually do so** — the file ends up untracked,
undiscussed, and discovered later. See §3's note on where new files get
created.

---

## 8. Standing instructions

⭐⭐⭐ **Any mention of incense or icons, in any source, however tangential,
is flagged as high priority** and reported explicitly in every close-out
— including when the result is a confirmed zero.

⛔ **Nothing is ever drafted, altered, or posted to Rev. James by a
delegated pass.** Discord access is manual, always: JD copies the full
thread himself and pastes it for comparison. ⛔ **Full-thread recapture,
never an append** (`260801-3`) — because he has edited a message after
posting before, and only a full comparison catches that.

**Corrections are dated notes beside the original, never silent
rewrites** — the never-alter rule, project-wide.

⭐⭐ **Every intake or retro-registration pass updates the coverage
registries for whatever it covers, in the same pass — BOTH of them**
(added `260834-7`):

1. **`SRC_Coverage_Register.md`** — the coverage state for the material
   the pass touched: what was retrieved, what was judged, what was
   deliberately declined and why, and what remains unreviewed.
2. **`SRC_Channel_Inventory.md`** — the decision cell for each video the
   pass covered, set to **`INGESTED`** and carrying **the File number and
   the finding range**, so the inventory never drifts behind the corpus.

⚠️⚠️ **`SRC_Coverage_Register.md` DOES NOT EXIST YET AND IS NOT CREATED BY
THE PASS THAT WROTE THIS INSTRUCTION.** It is forthcoming: a later pass
will build it as the single place recording coverage for **every source
universe this project draws on** — both YouTube channels (`EXT-2`
`@barelyprotestant5365` and `EXT-3` `@StFrancisAnglicanSpartanburg`), the
`BLOG` written corpus, the `POD` podcast corpus, the Discord threads, the
in-person class recordings, and the pre-manifest `aNNN` transcript files.
⛔ **A reader who meets this convention before the file exists is not
looking at an error and should not go hunting for it** — until that pass
runs, clause 1 is owed rather than actionable, and clause 2 stands on its
own and is enforceable now.

⭐ **Why both and not one.** They answer different questions.
`SRC_Channel_Inventory.md` is video-keyed and channel-scoped: it says
what happened to *this video*. The coverage register is universe-scoped:
it says what is left. A pass that updates only the inventory leaves every
non-YouTube universe — and every *unretrieved* item — invisible.

⭐⭐⭐ **NEW (260835-15) — SINGLE-LABEL, NOT CONFIRMED SINGLE-VOICE: a
weaker speaker-warrant class, for use going forward wherever this pattern
recurs.** Automatic diarization returning exactly one label
(`speakers_detected: ['A']` or equivalent) is **not by itself** a
confirmed single-voice recording — the software under-detects real
speaker count, and any live-class, Q&A, or audience-address format can
have every participant turn collapsed into the teacher's own label.
⛔ **Before a single-label file is used as a speaker warrant, check its
own content for participant-address markers**: a name spoken to, an
answer that doesn't fit the teacher's own voice, a call-response
liturgical exchange, a closing address to someone else. **None found →
the file stands as SINGLE-VOICE, CONFIRMED, the strongest tier. Attendee
turns found inside the one label → the file drops to SINGLE-LABEL, NOT
CONFIRMED SINGLE-VOICE**, usable only where the specific cited byte range
has been individually checked against the located attendee-turn list and
does not intersect it — never as a blanket warrant for the file as a
whole. ⭐ **Two independent instances already on file, found separately
and only now named as one class: `File 49`/`TeachingTheMass`** (attendee
turns including the file's own final line, *"Thanks, Frank."* —
`SRC_Manifest.md`, `260835-11`) **and `File 63`/`GeWfXTAjFDo`**
(participant turns swallowed into label `A`, `260835-12`). Both are
excluded from any blanket single-speaker warrant; `File 49`'s six-file
warrant narrowing is recorded at `SRC_Manifest.md` beside the warrant
itself.

⭐⭐⭐ **NEW (260835-22) — CHANNEL OWNERSHIP IS NOT A SPEAKER WARRANT.
SPEAKER IDENTITY MUST BE ESTABLISHED FROM CONTENT, IN EVERY CASE, WITHOUT
EXCEPTION.** Owed since `260835-14`, whose evidence established it;
`260835-18` supplied its mechanism but expressly did not write it. Written
here now.

⛔⛔⛔ **That a recording sits on a channel belonging to, named for, or
operated by a person does NOT establish that the person is the one
speaking on it** — not for `EXT-2` (`@barelyprotestant5365`), not for
`EXT-3` (`@StFrancisAnglicanSpartanburg`), and not for any channel, feed,
blog, or archive this project draws on. **Ownership is a fact about who
published; it is not a fact about who talked.**

⭐ **The instance that forced the rule.** Two videos titled *"Fr. Ray
Teaching About…"* (`8nRhmD4w-Wg`, `9Fezj9WMh3A`), sitting on Rev. James's
own `EXT-2` channel, are **entirely another priest's teaching** — Fr.
Ray's, narrating his own ordination in the first person, uploaded 2017,
**predating Rev. James's 2020 diaconate**. Registered as `File 58`/`File
59` at `260835-12` and given a formal `EXCLUDED — confirmed not Rev.
James` disposition at `260835-18`. ⚠️ **The title said so plainly and the
channel still nearly carried them into the corpus as his** — which is the
whole lesson: had they been mined on ownership, findings in another
priest's voice would have entered the corpus under Rev. James's name, and
the corpus has no mechanism that would have caught it downstream.
⭐ **The mechanism, found later (`260835-18`) and worth keeping because it
generalises:** Fr. Ray was Rev. James's own first priest and mentor
(`St_Francis_EMC_Distinctives.md` L430). **A channel hosts a mentor's,
a colleague's, a guest's, or a played-back third party's material as a
matter of course, and nothing about that is anomalous** — so a
same-channel recording in someone else's voice is a NORMAL case to be
expected, not a freak one to be treated as unlikely.

✅ **WHAT DOES ESTABLISH SPEAKER IDENTITY — from the recording's OWN
CONTENT, and nothing else:** self-identification; direct address by name;
role self-identification; first-person biography unique to the person;
or elimination against a located, content-derived speaker set.
⛔ **WHAT NEVER ESTABLISHES IT:** channel ownership · the title · the
uploader · the diarization label (the `260835-7` label-flip hazard) ·
speaking duration (the `File 52` inversion) · the file's folder location ·
or the fact of registration itself — **registration is not a speaker
warrant** (`File 60`/`File 61`, `260835-12`).

⛔ **A recording whose speaker cannot be established from its own content
is registered with ATTRIBUTION OPEN and is NOT MINED for anyone's
positions until it is resolved.** Open attribution is a normal, stable,
reportable state — ⛔ **it is never closed by defaulting to the channel
owner**, and a pass that cannot resolve it says so and stops rather than
assuming. *(Live instance: ear-check `E1`, `hDRmWM5Nkgw`, blocking on
exactly this question.)*

⭐⭐⭐ **NEW (260835-24) — THE OFFICE RULE: CHANNEL IS NOT THE AXIS,
ORIGINAL TEACHING CONTENT IS. APPLIES UNIFORMLY TO BOTH CHANNELS.**

⛔⛔ **This replaces the channel-scoped handling that stood until now,
which was incoherent and known to be:** office recordings were
`EXCLUDE-office` on `EXT-3` per an earlier JD instruction, `INCLUDE`d on
`EXT-2`, and `260835-23` added seven more `EXT-2` office rows on that
precedent while flagging the asymmetry as owing a ruling. **The ruling is
that the axis was wrong, not that one channel's answer was.**

**THE RULE, in three cases:**

1. **A pure office recording with no original teaching → `DECLINED-office`.**
2. **An office containing a homily, sermon, or other original teaching → `INCLUDE`.**
3. ⭐ **Where the title and description do not settle which it is →
   `UNCERTAIN`. Do NOT guess either way.** An `UNCERTAIN` row stays on the
   board; a decline is silent and permanent.

⭐⭐⭐ **THE GOVERNING CASE, AND WHY A BLANKET OFFICE EXCLUSION IS WRONG:
`IGNmKMXhL1Q` (`File 60`) — *"Morning Prayer, 5th Sunday in Lent…
(with a Homily)."*** The office around it is read-aloud liturgy; **the
homily is his own words.** ⛔ **A blanket office exclusion would have lost
it.** ⚠️ **And note what makes the case hard rather than easy: this
uploader records Sunday Morning Prayer both WITH and WITHOUT a homily and
does not reliably flag which in the title — so title silence is NOT
evidence of absence, which is exactly what case 3 exists to handle.**

⛔⛔⛔ **THE READ-ALOUD ATTRIBUTION LAYER IS REQUIRED FOR ANY OFFICE ROW
THAT IS `INCLUDE`D — THIS IS NOT OPTIONAL AND IT IS THE OTHER HALF OF THE
RULE.** An office that earns `INCLUDE` earns it **for its homily**, not
for its liturgy. **The liturgical text is not his own words even when the
homily is.** Before any such recording is mined, the read-aloud spans must
be separated from the original-teaching spans, and nothing inside a
read-aloud span may be attributed to him.

⭐ **The precedent is established and load-bearing, not hypothetical:**
`File 60` (`IGNmKMXhL1Q`, registered ATTRIBUTION OPEN) · `File 68`
(`xcNz2wdI2P8`, Stations of the Cross) · `File 69` (`M7iSL5mznTk`, A
Liturgy for Spiritual Communion — **`260835-18` recorded it READ-ALOUD
100%, ZERO own-voice content, and flagged it as a `GV-50`-class trap: it
contains first-person *"I believe that Thou art truly present in the Holy
Sacrament"* and *"Body and Blood are being offered to the Father"* —
⛔ THE PRAYER BOOK'S WORDS, NOT HIS — sitting exactly on the
eucharistic-presence and eucharistic-sacrifice questions**). ⚠️ **That is
the whole danger in one example: the read-aloud layer of an office lands
precisely on the corpus's live questions, in the first person, and reads
as testimony if the layer is not separated first.**

⚠️ **A decline under this rule is cheap and should be recognised as such.**
Most of what an office row is worth evidentially — which book he used,
which feast he kept, on what date, at what length — is legible from the
inventory row's own title and metadata and needs no pull at all.
⛔ **What a decline costs is only the homily, which is why case 3 exists.**

⛔ **Any `DECLINED-office` verdict is conditional in one respect, and each
cell says so: if content later shows a homily, the decline does not hold.**

⭐⭐ **NEW (260835-22) — PROGRESS REPORTING: A DELEGATED SESSION EMITS A
BRIEF STATUS LINE ROUGHLY EVERY TEN MINUTES OR AT EACH MAJOR TASK
BOUNDARY, WHICHEVER COMES FIRST.** ⚠️ **This convention has been carried
in the text of every delegated prompt for some time, but `260835-21`
grepped the repo and found it written down NOWHERE. It was a convention
with no home. This is its home.**

**Each status line states three things and nothing more:**

1. **which task** — the item number or task name currently in hand;
2. **rough progress** — what is done, what is in flight;
3. **whether anything is blocking** — and if so, what, named plainly.

⭐ **Keep them short. One or two sentences.** They exist so the
orchestrator can tell a long-running pass from a stalled one, and can
intervene early when a pass is heading somewhere wrong — **the whole
value is in arriving DURING the work, not after it.**

⛔⛔ **STATUS LINES ARE INSTRUMENTATION, NOT DELIVERABLES. THEY NEVER
REPLACE, ABBREVIATE, SUBSTITUTE FOR, OR EXCUSE ANY PART OF THE FULL
CLOSE-OUT.** A pass that reported diligently throughout still owes its
complete close-out — every gate value, every firing code, the full
accounting, the diff, and the pass artifact in `passes/` (§4). ⛔ **"I
already said that in a status update" is not a reason to leave anything
out of the close-out**, which must stand alone and be readable by someone
who never saw a single status line. **Nothing is ever established by a
status line**: they are progress signals, and they carry no findings, no
verifications, and no decisions.

---

## 9. Thread lifecycle — how JD manages long conversations

**Separate from this project's own git-based delegate-and-verify loop, JD
runs a memory-stored, cross-thread system for managing the cost and
staleness of long chat conversations generally.** Not part of this
project's data discipline, but worth knowing about, since orchestration
threads are exactly the kind of long-running conversation this system
exists to handle.

**The full specification lives at
`passes/ff-rff-ffd-system-documentation-v2.md`; this section summarizes
it.**

**The problem it solves:** a chat thread resends its full history every
turn, an interface has no native fork or compaction, and a long thread
eventually buries active work under stale context.

**Three memory-stored commands, `FF` / `RFF` / `FFD`:**
- **`FF`**, run in a heavy or pivoting thread, produces a dense,
  copy-pasteable handoff block ending in a unique **fork tag** (e.g.
  `FORKTAG-CS-p4k9m2`) generated in that thread's own text.
- **JD pastes the block as the first message of a fresh thread** and
  continues there at far lower per-turn cost.
- **`RFF`**, run in the new thread, retrieves anything the handoff didn't
  carry — either directly via `conversation_search` (the fork tag exists
  in exactly the source and forked threads, so it identifies the source
  precisely rather than by fuzzy keyword match) or by generating a
  retrieval prompt for JD to relay manually.
- **`FFD`**, run in the *source* thread, produces incremental delta
  passes if that thread keeps accumulating information after the first
  handoff — so a second fork later isn't working from a stale snapshot.

⚠️ **v1 (this description) is live and in use. A v2 (doc-backed state) is
specified but untested** as of `260832-2` — this project's own
`ORCHESTRATION.md`/`PROJECT_STATE.md` pair is, in effect, one instance of
exactly that doc-backed-state pattern already.

**Relevance to this repo specifically:** if a hand-off into a *fresh*
orchestration thread ever uses `FF`/`RFF` rather than the simple "read
`PROJECT_STATE.md` then this file" pointer already established, the new
thread should expect a fork-tag-bearing block as its first message and
can treat it the same way — confirm the tag survived the paste verbatim,
then proceed. ⛔ **Neither replaces the other:** `FF`/`RFF`/`FFD` manage
*conversation* continuity; `PROJECT_STATE.md` and this file manage
*project* continuity. A fresh thread benefits from both if both are
available, but the project state is authoritative if they ever disagree.
