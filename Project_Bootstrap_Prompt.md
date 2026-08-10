# Project Bootstrap Prompt

**Last updated: 260816-1**

**Purpose:** Reusable instructions for starting or continuing a structured,
long-term research/dialogue project with canonical document tracking. Paste
this at the start of a new project, or reference it when a session needs a
reminder of the conventions already in force.

---

## Source handling

- Raw, unedited source material (transcripts, chat exports, external texts)
  uses the `SRC_` filename prefix. Canonical analysis/synthesis documents do
  not use this prefix.
- Full transcripts stay OUT of Claude Project knowledge. They live in a
  stable local folder, unmodified from their original uploaded form, and are
  attached to a chat message only for the session that needs them. Do not
  split a multi-item transcript file into smaller files, re-download,
  re-encode, or normalize line endings — any of these changes invalidates
  previously-logged byte offsets.
- A `SRC_Manifest.md` lives in project knowledge: for each transcript file,
  it records the sha256 hash and the byte range covering each distinct
  item (video, session, etc.) within that file.
- Before trusting any previously-logged byte offset, verify the source
  file's current hash against `SRC_Manifest.md`.
- Before deploying any verbatim quote in outward-facing material, stop and
  request the actual source file rather than relying on a ledger's
  paraphrased summary of what was said. Ledger summaries are for
  navigation, not for quotation.
- Byte-offset extraction on long-line transcript files uses `grep -ob` and
  `dd`, not plain `grep`, which is unreliable on very long lines.
- Verbatim quotes are verified by byte-offset before being logged or
  deployed. Never attribute a paraphrase as a direct quote.

### ⭐⭐ A TRIMMED OR REPLACED ORIGINAL IS RECORDED, AND THE SURVIVOR IS MARKED NOT-THE-ORIGINAL (adopted 260816-1)

**The rule.** When an as-recorded original is trimmed, re-encoded, split or
replaced, **two things happen together and neither is optional**: the event
is recorded in `SRC_Manifest.md` (what existed, what was done to it, what
was deleted), **and the surviving file is marked in the manifest as NOT the
as-recorded original**, with the reason. ⛔ **This holds even — especially —
when the survivor has inherited the original's filename.**

⚠️⚠️ **THE REASONING, RECORDED BECAUSE THE RULE IS USELESS WITHOUT IT.**
A filename is a **provenance claim**. `Audio_08_09_2026_19_35_15.mp3` asserts
"this is what the recorder wrote at 19:35:15 on 2026-08-09." When the
untrimmed file is deleted and the trimmed file takes its name, **that
assertion silently becomes false, and nothing in the file, its hash, or its
timestamps records that it changed.** ⛔ **A hash check cannot catch this:
the hash faithfully describes the file that is there, and says nothing about
whether that file is the one the name claims.** This is the **`W17`
stamp-defect shape** — a stamp that certifies something the artefact no
longer is — and it is the same class as the `BLOG-71` footer defect, where
text inside the body hash dated nothing because the hash verified the fetch
and not the authorship.

⭐ **Why the record and the marking are BOTH required.** The record alone
lives in a changelog that a future pass may not read; the marking alone says
the file is not the original but not what happened to it. **Together they
survive the pass that wrote them**, which is the only durable test.

⛔ **Do not reconstruct the deleted original, and do not estimate what was
removed** unless the trim's own parameters were recorded at the time. An
estimate is precisely the error the `BLOG-13` furniture rule exists to
correct.

### ⭐⭐ DUAL INDEPENDENT ASR RENDERINGS OF ONE CAPTURE — THE VERIFICATION PROTOCOL (adopted 260816-1; second registered use)

*First use: the 06-28 stream's `[SW]`/`[SY]` pair (`260812-1`). Registered
here as a standing convention on its second use.*

Where one capture is transcribed by **two independent ASR systems**:

- ✅ **Where the renderings AGREE, wording carries PROVISIONAL confidence** —
  confirmed against transcription error, and that only.
- ⚠️ **Where they DIVERGE, the passage enters a VERIFICATION QUEUE**
  resolved by ear against the audio.
- ⛔⛔ **NEITHER TRANSCRIPT IS AUTHORITATIVE ON WORDING ALONE.**
- ⛔ **Diarization is a NAVIGATION LAYER ONLY. It is NEVER attribution of
  record.**

⭐⭐ **WHERE THE AUDIO SURVIVES, VERIFICATION GOES TO THE AUDIO, NOT TO THE
SECOND TRANSCRIPT.** Two machines reading one recording can only ever
adjudicate one machine reading against another. **The recording itself is a
stronger warrant than any number of renderings of it** — the `260810-1`
pattern that discharged `IP-37`/`IP-38`/`IP-39`.

⚠️ **AND THE AGREEMENT OF TWO RENDERINGS IS SILENT ABOUT ANYTHING THE
CAPTURE ITSELF MISSED.** Both derive from one recording; neither can catch
what the microphone did not get. **An `[R]`/`[S]` pair has two independent
*recordings* and can catch omission; a dual-ASR pair cannot, and must never
be read as equivalent to one.**

⛔ **A tuned key-terms list built from observed manglings is TOOLING and
belongs in the repo, not in a chat thread** — and ⛔ **it is not a correction
map.** It changes what the recogniser hears on the *next* run; it never
licenses rewriting a mangled form already captured. **Observed manglings are
logged in the quirk register and left standing in the transcript.**

## Discord / live dialogue logs

- Verbatim activity logs (one file per topic thread) are kept in project
  knowledge as raw record only: timestamp, author, verbatim text, and
  permalink if available. No analysis, no source tags, no commentary
  inside these files.
- The capture method is a **manual full-thread copy/paste from the Discord
  client**, which is then formatted into Markdown. No export tool is or has
  ever been used. Any claim in a changelog that a capture came from
  DiscordChatExporter is false and superseded (see `SRC_Manifest.md`
  260801-3).
- **Capture the WHOLE thread on every new reply. Never append a single
  message.** A full recapture makes `git diff` the edit detector: only the
  new message should appear, and anything else that moves is an edit.
- **Discord messages are mutable.** Any diff touching an already-captured
  message is an edit, and is logged as a dated correction with the superseded
  text named. It is never absorbed silently, and the historical entry is
  never rewritten.
- Copy/paste has tested limits, and they are worked around by hand, not
  assumed away: it does **not** carry the `(edited)` marker, so an edit
  visible in the client is invisible in the archive and must be noted
  manually at capture time; it renders same-day timestamps bare, which are
  resolved against the capture date and flagged as resolved-by-report rather
  than captured. It **does** preserve paragraph breaks.
- Never re-type or reformat a message from a summarised or partial paste.
  Archive text comes from the raw capture only.

## Document modes

- **APPEND MODE:** patches only; no live docs are touched. New findings are
  queued in a running patch-block artifact for later reconciliation.
- **RECONCILE MODE:** live docs are attached and edited directly, using
  anchor-based `str_replace` against unique anchors — never line-number
  insertion, since documents shift between sessions.
- A control/orchestration thread (if used) handles state tracking and
  prompt generation only. Transcript or source intake never happens there.
- When updating Claude Project knowledge, always delete-and-replace the
  file rather than uploading a duplicate, to avoid duplicate-file
  collisions.

## Attribution discipline

- Maintain a three-layer attribution system in all analysis documents:
  **Stated** (verbatim, byte-offset verified), **Stated-Analysis** (a
  labeled inference from something stated), and **Analysis** (the
  project's own argument, not attributed to the source). These layers must
  never be conflated in output or in what gets relayed back to the source
  person.
- Watch for rhetorical or reductio content being misread as declarative
  statements. If a source's strongest-sounding line is actually a question
  posed within their own argument, flag it explicitly as such and do not
  quote it back as though it were an assertion.
- Never impute a rule, position, or reasoning to someone that they have not
  stated, even when it seems like a natural completion of what they said.
  If their reasoning is ambiguous between two readings, ask which they mean
  rather than picking one and asking them to ratify it.

## Numbering and versioning

- Source-tag numbering (e.g. IP, DQ, GV, RC, BP, EXT, and other batch-
  specific prefixes) is cumulative and unbroken across all intake batches,
  never restarted per-document.
- Question-list-style documents use integer version increments (v12 → v13).
- Ledger/findings documents use date-based versioning: `yymmdd-[iteration]`.
- Every canonical document carries a permanent, prepended changelog. Once
  written, changelog entries are historical record and are never altered,
  only added to.

## Strategic/dialogue discipline (where applicable)

- One committal question per turn in any live dialogue; hold rebuttals and
  downstream arguments until the prior answer is on record.
- Lock a general principle or rule before applying it to the specific case
  it was really aimed at. Don't name the target case until the rule is
  already committed to.
- Prefer questions that ask what work a stated distinction is doing, over
  questions that assert a rule and ask for ratification — the latter risks
  looking like a misreading if the person's actual reasoning differs.
- Maintain a retired/do-not-deploy register for arguments that have been
  answered satisfactorily and should not be reused.
- Keep tone collaborative and non-adversarial by design, not just by
  accident, when the relationship with the source person matters as much`
  as the argument.

## Voice and drafting

- The project owner drafts in their own voice; Claude checks and tightens
  rather than ghostwriting wholesale.
- Minimize em-dashes/en-dashes in fresh conversational output; prefer
  commas, parentheses, periods, restructured sentences, or an occasional
  semicolon. Heavy dash use reads as AI-generated and should be avoided.
- Dash-policing (and similar style passes) is skipped during complex
  document reconciliation work; a single cleanup pass happens afterward
  if needed, rather than mid-task.

---

*This file is itself a canonical document: update it via delete-and-replace
in Project knowledge, and via normal commit in the GitHub repo, when new
recurring conventions emerge that should apply project-wide.*

## Changelog

- **260816-1 (2026-08-16):** Two conventions added to Source handling, both from the `A101-2026-08-09` intake. **(1) A trimmed or replaced original is recorded and the survivor is marked not-the-original** — adopted after that session's as-recorded file was truncated by stream copy, the untrimmed original deleted, and the trimmed file left carrying the original's name; the reasoning is recorded with the rule because a filename is a provenance claim and no hash check can detect that it has become false (the `W17` stamp-defect shape). **(2) The dual-independent-ASR verification protocol**, registered as a standing convention on its second use (first: the 06-28 `[SW]`/`[SY]` pair, `260812-1`) — agreement gives provisional confidence against transcription error only, divergence enters an ear-verification queue, neither transcript is authoritative on wording alone, and diarization is navigation only and never attribution of record. Records that where the audio survives verification goes to the audio rather than to a second rendering (the `260810-1` pattern), that two renderings of one capture are silent about what the capture itself missed, and that a tuned key-terms list is repo tooling and **not** a correction map.
- **260801-3 (2026-08-01):** Added the Discord capture-method rules to the Discord/live-dialogue section, after a divergence between the archive and the live client was traced and resolved. Records that captures are manual full-thread copy/paste and never came from an export tool, retracting a false provenance claim carried in `src/SRC_Discord_RPW.md` and `SRC_Manifest.md`; requires full-thread recapture on every reply so that `git diff` surfaces edits; requires dated corrections for edited messages; records the tested limits of copy/paste (no `(edited)` marker, bare same-day timestamps, paragraph breaks preserved); and forbids re-typing archive text from a summarised paste.
- **260727-1 (2026-07-27):** Added this file's first `**Last updated:**` stamp (it carried no version marker before this pass). Registered in `PROJECT_STATE.md` §4 at the same value.