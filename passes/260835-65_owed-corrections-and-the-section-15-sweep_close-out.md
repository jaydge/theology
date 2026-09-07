# 260835-65 — Owed corrections and the §15 sweep

**STAMP: 260835-65.** ASSIGNED BY BRIEF, NOT DERIVED. No stamp registry was read
and no stamp was derived, per instruction.

**Mode:** RECONCILE. **This pass wrote to the repository.** Six registered
documents edited; no capture file touched; no file created except the two pass
artifacts in `passes/`.

**Repo HEAD at start:** `9ddd00d` ("260835-64: the 1874 dissent register and the
pamphlet divergence"). Working tree **clean at start**. All git reads used
`--no-optional-locks`; **no lock failure occurred**.

**Validator, re-derived at HEAD `9ddd00d` rather than assumed:**

| | ok | warnings | errors |
|---|---|---|---|
| **Before** | 100 | 9 | **0** |
| **After** | 104 | 9 | **0** |

⛔ **Errors stayed at zero throughout. The pass did not need to stop.**

---

## §0. Divergences from the brief, recorded before anything else

Per the standing rule that a recorded convention in the repo overrides an
instruction in the brief, and the instruction to say so plainly where a
premise is wrong.

**(0.1) ⛔ "PROJECT_STATE.md section 15" DOES NOT EXIST.** The brief's READ
FIRST list and its ITEM 3 both name it. `PROJECT_STATE.md` runs **§0 through
§8** and has no §15. **§15 is `St_Francis_EMC_Distinctives.md` §15, "Where He's
Sound (common ground — credit it)"** — which is what `validate_project.py`'s
`[C10]` actually reads (`DIST`, not `STATE`). The sweep was performed there.
`PROJECT_STATE.md` §8 item 4 is the *checklist* for that sweep, which is
probably the source of the confusion.

**(0.2) ⚠️ "Three appends" IS FOUR.** `260835-64` §4(c) opens *"Three appends"*
and then drafts wording for **LOCUS 1, LOCUS 2, LOCUS 3 and LOCUS 4**. The
brief's count of four is right and `260835-64`'s own word "Three" is wrong.
**Four wordings were treated as drafted.**

**(0.3) ⚠️ "C0 unchanged" IS NOT ACHIEVABLE ALONGSIDE ITEM 4(a).** The brief's
expected direction says *"C0 and C6 unchanged, per the manifest-only
convention."* That holds for ITEM 4(b) and **C6 is unchanged at 5 files**. But
ITEM 4(a) directs two documents into `PROJECT_STATE.md` §4, and C0 derives its
file set from §4, so **C0 necessarily moves 34 → 36**. C3 moves 28 → 30, C5
22 → 24 and C8 31 → 33 for the same reason. **Coverage rising because two files
entered the registry is the intended effect of ITEM 4(a), not drift.**

**(0.4) ⛔⛔ THE BRIEF'S ITEM 1(a) WAS NOT EXECUTED AS WRITTEN — see §1 below.
This is the one substantive non-compliance in the pass and it is escalated to
JD rather than decided here.**

**(0.5) ✅ The brief's `[C10]` figure was correct.** Re-derived by grep before
touching anything: `DQ` head 28, §15 credited 24, **gap exactly 4**, and the
threshold is `> 4`, so the next `DQ` mint would indeed have tripped it.

---

## §1. ITEM 1 — the four source-of-record designations

### 1(a) LOCUS 1 — ⛔⛔ NOT APPLIED. The decision, its grounds, and what is owed.

`260835-64` drafted a note to be appended **inside the capture header** of
`src/SRC_PRIMARY_1874_DeKoven_Canon-On-Ritual-Speech_ProjectCanterbury.txt`,
immediately after its `SOURCE OF RECORD` block. **It was not applied. The
capture file is byte-identical to its state at HEAD `9ddd00d`** — re-verified
this pass: `8de40ae1…`, 75,806 bytes, 1,340 lines, matching its registry row.

**Three grounds, each re-derived rather than assumed:**

1. ⛔⛔ **Seven line offsets are logged into that file across the corpus, all
   below the header.** `L104-1157`, `L1161`, `L1211-1213`, `L1218-1225`,
   `L1228-1234` (all in `Incense_Reply_Source_Checks.md`), and `L1285-1313`,
   `L1314-1339` (in `Ritual_Canon_1874_Dissent_Register_And_Pamphlet.md`; the
   first of these is also cited in `Incense_Reply_Source_Checks.md`). The
   drafted note is roughly twenty lines. **An in-header insertion shifts every
   one of them.** `CLAUDE.md` §Source handling forbids operations that
   invalidate previously-logged byte offsets, and `SRC_Manifest.md`'s own
   `EXTERNAL PRIMARY TEXTS` header block states that an offset into these files
   is an offset into header-plus-source.
2. ⛔ **`SRC_PRIMARY_` captures are write-once by established practice.**
   `git log` per file across all of `src/`: **no `SRC_PRIMARY_` capture has ever
   been modified after its adding commit.** The only `src/` files with more than
   one commit are `SRC_Discord_RPW-raw.txt` and `SRC_Discord_Assurance-raw.txt`,
   which are extended by recapture under an explicit convention.
3. ⚠️ **The hash guard would have been defeated rather than served.**
   `CLAUDE.md` requires verifying a file's current hash against `SRC_Manifest.md`
   before trusting a logged offset. Editing the file and updating the manifest's
   hash makes that check *pass* over seven now-wrong offsets.

**What was done instead.** The full withdrawal is recorded in the registry cell
that governs use of the capture (LOCUS 2, applied — see below), together with a
`260835-65` note stating that the header note is absent **by decision**, giving
all three grounds, so a later reader of the cell finds a decision rather than an
oversight.

⏳⏳ **OWED, AND IT IS JD'S CALL, NOT A PASS'S:** whether to disturb the capture
file to place the note in its header. **If yes, the same pass owes dated notes
against all seven logged offsets recording the line shift, plus new
bytes/lines/sha256 in the manifest row.** `260835-65` declined to make that
trade on its own judgment.

### 1(b) LOCUS 2 — ✅ APPLIED, verbatim.

`SRC_Manifest.md`, the `EXTERNAL PRIMARY TEXTS` row for the pamphlet. **Located
by reading, not by trusting the row number — and the brief's row number was
right: line 4474.** `260835-64`'s drafted LOCUS 2 wording appended verbatim,
followed by the `260835-65` note described in 1(a).

### 1(c) LOCUS 3 — ✅ APPLIED, verbatim.

`Incense_Reply_Source_Checks.md` §3. **Verified by reading: the brief describes
it exactly.** The sentence *"The pamphlet is the only source of record for both
texts"* stands at the end of the "Occasion and source of record for each" bullet
(the brief's "lines 264-270" resolves to the bullet spanning **L264-273**).
`260835-64`'s FALSIFIED wording appended verbatim as an indented block inside
that bullet, with one added line recording that the wording is `260835-64`'s and
the application is `260835-65`'s.

### 1(d) LOCUS 4 — ✅ APPLIED, verbatim.

Same file, §5. **The brief's "line 361" resolves exactly:** *"Source of record:
the T. Whittaker pamphlet (Project Canterbury transcription); the Journal does
not print speeches."* `260835-64`'s CORRECTED wording appended verbatim as a
blockquote immediately after the paragraph.

### 1(e) What was deliberately NOT touched

⛔ **`passes/260835-57_incense-reply-source-checks_close-out.md` line 51** —
carries the same falsified "sole source of record" claim. **Untouched, per
`260835-64`'s own instruction and the never-alter rule: it is a pass close-out
and therefore historical record.** Its error is corrected by the LOCUS 3 note in
the live document it describes.

⚠️ **`src/SRC_PRIMARY_1874_GeneralConvention_Journal_…txt` header lines 26-27**
— `260835-64` classed this as "now incomplete rather than wrong". **Not touched**,
for the same offset and write-once reasons as LOCUS 1, and because no wording was
drafted for it. **Recorded as owed, and it is minor.**

---

## §2. ITEM 2 — the two 1974 Measure corrections

✅ **Both claims verified verbatim in place before annotating, and the statutory
exception verified against the capture rather than against `260835-60`'s report
of it.**

**The claims, as they actually read:**

- `RJ_Incense_Analysis.md` §8, AFTERMATH block, Phase 2 bullet: *"**Phase 2, THE
  LEGAL GROUND DISSOLVES (1974).** The **Worship and Doctrine Measure 1974**
  repealed the **Act of Uniformity 1662**, the statutory foundation of the
  Victorian case law."*
- `Incense_Conversational_Outline.md`, the historical-corroboration step: *"The
  1899 Opinion has no legal force today: the Worship and Doctrine Measure 1974
  repealed the Act of Uniformity 1662, dissolving the enforcement regime…"*

**The Schedule 2 exception, read directly from
`src/SRC_PRIMARY_1964-1974_ChurchAssembly-GeneralSynod_Measures_Vestures-AlternativeServices-WorshipAndDoctrine.txt`,
"SCHEDULE 2, *Acts and Measures Repealed*, REPRODUCED IN FULL", the
`14 Cha. 2. c. 4.` row:**

> The Act of Uniformity 1662. | **The whole Act except sections 10 and 15.** |
> In section 10, the words "nor shall presume to consecrate and administer the
> holy sacrament of the Lords Supper".

⭐ **A detail neither the brief nor `260835-60` carried, and it is in the
capture:** the repeal is not simply "all but ss.10 and 15" — **section 10 is
itself partially repealed**, as to one quoted clause. Both notes state it.

**Both notes state the correct position affirmatively**, per the brief, because
these two files feed JD's conversational preparation. Both say plainly that the
original claim is **substantially right and imprecisely stated, and is not
withdrawn**: the statutory frame the Victorian case law and the 1899 Opinion
reasoned within is gone, and the exception does not touch ceremonial. What is
disqualified is the unqualified word *"repealed"* in outward-facing material.

⛔⛔ **WHAT SECTIONS 10 AND 15 CONTAIN IS NOT STATED IN EITHER NOTE AND WAS NOT
SUPPLIED FROM GENERAL KNOWLEDGE.** The capture records the extent of repeal, not
the text of the surviving sections. Recorded as a limit, in both notes.

*(Discharges `260835-60`'s own owed-work item 8, which that pass recorded as
"For a reconcile pass" and could not act on because it ran read-only.)*

---

## §3. ITEM 3 — the §15 sweep

**Gap re-derived by grep, before and after, from the same expressions
`validate_project.py` uses (`^\*\*PFX-N.\*\*` for the ledger head, `\bPFX-N\b`
within the §15 body for what §15 cites):**

| Series | Head | §15 before | Gap before | §15 after | Gap after |
|---|---|---|---|---|---|
| **DQ** | 28 | 24 | **4** | 28 | **0** |
| IP | 125 | 108 | 17 (WARN) | 118 | 7 (WARN) |
| RV | 63 | 62 | 1 | 62 | 1 |
| LS | 141 | 120 | 21 (WARN) | 120 | 21 (WARN) |
| BLOG | 158 | 158 | 0 | 158 | 0 |
| POD | 16 | 16 | 0 | 16 | 0 |

✅ **The brief's figure of 4 was correct.**

**How it was performed.** Previous sweeps were read first. The established shape,
from `260833-1` onward, is a `### <source> common ground (added <stamp>)`
sub-section carrying credits as bullets and an explicit **"N DECLINES, WITH
REASONS"** block on the `BLOG-16` precedent. That shape was followed and **not
reinvented**. One departure is stated in the new section's own heading: every
§15 sub-section since `260833-1` says *"swept in the SAME pass that logged the
findings"* and **this one cannot**, so it says so rather than borrowing the form.

**Result: FIVE CREDITS, EIGHT DECLINES, ONE SCOPE EXCLUSION.**

Credits: `DQ-25`(a)/(b) the definition of *"received"* given plainly and
deflated; `DQ-26`(a) the criterion amended by its own author; `DQ-26`(c) `OQ21`
answered in the concessive direction; `DQ-28`(b) clerical discretion
subordinated to Scripture, his own example and his own penalty; ⭐⭐
`DQ-28`(c)/(d) incense permitted-and-not-required, his own *"Correct."*

⛔⛔ **The most important decline is the pair of coverage facts (`DQ-27`(f),
`DQ-28`(f)).** Both entries record, twice and carefully, that the
church-wide/jurisdictional axis question stands asked twice and answered zero
times, and both record it **NOT as evasion and NOT as a charge**. A non-answer is
not soundness and cannot be filed as one; equally it is not a tension. It stays
where those entries put it.

⚠️ **`DQ-23` is a scope exclusion, not a decline:** a third-party Discord post
by `M1B3AU`, tagged `[EXT / third-party, Discord — not RJ]`. Recorded so its
absence reads as a decision.

### ⛔⛔⛔ A hazard hit and reverted inside this pass — the most useful thing in it

**The first draft of the section's C10 metrics caveat named both other ledger
heads in the sentence explaining that the lags were not swept.** Because `[C10]`
arm (b) measures what §15 **cites**, not what §15 **credits**, that sentence
alone drove the `IP` lag from 17 to 0 and the `LS` lag from 21 to 0 —
**silently deleting two live warnings without a single finding being swept.**
Caught by re-deriving the gaps immediately after writing, and reverted.

⚠️ **The batch 6 and batch 7 notes had warned that naming declined items inflates
the metric. This is the first recorded instance where it would have SUPPRESSED A
WARNING rather than merely flattered a number.** The final text states the
figures without writing the tags, and says explicitly why the tags are absent so
a later pass does not "tidy" them back in.

⚠️⚠️ **A RESIDUAL EFFECT IS REPORTED RATHER THAN HIDDEN: the `IP` lag `[C10]`
reports still moves 17 → 7**, because `IP-118` is legitimately cited as a
condition travelling with the `DQ-28`(c)/(d) credit. ⛔ **Not one `IP` finding
was swept, credited or declined.** The warning still fires; the number is now
misleading and the section says so in terms.

⛔ **NOTHING WAS MINTED. Next free `DQ` is `DQ-29`, re-derived and untaken** —
the queued mint is the following pass's, not this one's.

---

## §4. ITEM 4 — the registry items

### 4(a) ✅ Both source-check documents registered in `PROJECT_STATE.md` §4

Registered per JD's ruling **in the same class and treatment as the
`260835-44`…`260835-53` external-research series**: `Class` opening
**"Backstage — EXTERNAL RESEARCH…"**, `Audience` **"JD only"**, placed
immediately after `Malachi_1_11_Lexical_Analysis.md`, the last row of that
series.

⚠️ **One deliberate departure from the series' shape, and it is forced by C3.**
Every row in that series carries a `Version` equal to the stamp at which the
document was both created and registered. **Here registration lags creation**,
and C3 compares the registry `Version` against the file's own `**Last updated:**`
stamp. So:

- `Ceremonial_Meaning_Source_Checks.md` → **`Version` 260835-56**, its own
  existing stamp. ⛔ **The file itself was NOT edited by this pass.**
- `Incense_Reply_Source_Checks.md` → **`Version` 260835-65**, because this pass
  did edit it (ITEM 1, LOCUS 3 and 4) and bumped its stamp accordingly.

Both `Class` cells record "CREATED *x*, REGISTERED `260835-65`" so the lag is
legible.

⏳ **Noted, not decided:** `Ceremonial_Meaning_Source_Checks.md` carries **no
changelog section**. Whether a source-check document owes one is a convention
question and is left to JD.

### 4(b) ✅ Seventeen captures registered in `SRC_Manifest.md` — MANIFEST ONLY

⭐ **The file list was DERIVED, not taken from the brief:** every file in `src/`
was tested by basename against `SRC_Manifest.md`, and each unregistered file was
attributed to its adding commit with `git log --diff-filter=A`. **Seventeen came
back unregistered and all seventeen attribute to the five named passes** —
`260835-59` ×3, `260835-60` ×6, `260835-61` ×2, `260835-62` ×5, `260835-64` ×1.
**The brief's premise was exactly right.** After this pass, **zero files in
`src/` are unregistered.**

Bytes, lines and sha256 computed by this pass from disk (plain whole-file
`sha256sum`, no stripping). Every `Work` and `Provenance` cell transcribed from
the capture file's own header. An **UNSTATED FIELDS** block lists what the
headers do not state — copyright status (**all seventeen**), publishers and
places, years, editors and translators, underlying-transcription retrieval
dates, and the two `1874_Debates` captures' unverified printed page numbers.
⛔ **Nothing supplied from general knowledge.**

⛔ **MANIFEST ONLY, per the `260835-58` convention JD confirmed: no
`PROJECT_STATE.md` §4 rows were added for these stamp-less capture files, and no
`File`/`W` number was consumed.** **C6 is unchanged at 5 files**, as the brief
predicted.

⛔⛔ **THE SAME LIMIT `260835-58` STATED IS RESTATED AND HOLDS: this pass verified
none of these texts against their sources.** A row certifies that a file exists
on disk with that digest and that its own header says what the row says. It
certifies nothing about the capture's fidelity to the work.

### 4(c) ⏳ A second registration debt, NAMED AND NOT DISCHARGED

The same five passes also committed **five analysis documents to the repo root**
with **no §4 row**: `Homilies_On_Incense.md`,
`Post_1900_Authorization_Of_Incense.md`, `Ritual_Canon_1874_To_1904.md`,
`Ritual_Canon_Examples_And_REC_Split.md` and
`Ritual_Canon_1874_Dissent_Register_And_Pamphlet.md`. **Outside this pass's
brief; the same `Class`/`Audience` judgment that JD reserved for the other two.**
⚠️ **Recorded in the manifest so the count is known: the §4 registration debt
stands at FIVE after this pass, down from seven.**

---

## §5. ITEM 5 — the diarization warning

✅ Recorded as a dated note in `SRC_Manifest.md`, **Note 2e**, placed immediately
after the protocol bullet that reads *"Diarization is a NAVIGATION LAYER ONLY.
It is NOT attribution of record"* — which is the only place in the corpus where
that file's diarization is relied on as a protocol, and directly above HAZARD 1,
which registered the artifact's failure to locate turn boundaries.

The note records: the file, the timestamp `02:23:15`, speaker `B`, that the
sentence is JD's own and confirmed by JD's ear against the audio, and that the
error falls at a turn boundary where one speaker trails off mid-sentence and the
next begins mid-thought. **The general lesson is stated for transfer: labels on
this file are not warrants at turn boundaries, and anything mined near a speaker
change owes an ear-check.** It is written in the shape the repo already uses for
attribution warnings (`DATED NOTE, <stamp> (<date>) —`, cf. the `260835-18` and
`260835-30` notes).

⛔ **Recorded as consistent with, and not a revision of, HAZARD 1:** that finding
was that the timing data *cannot* locate splices (0 ms at the known
questioner→reply boundary). This is a confirmed instance of the misattribution
that failure permits.

⛔ **Nothing was mined from that file this pass and no other timestamp in it was
checked.** ⚠️ **No claim is made that `02:23:15` is the only such error, and the
absence of others is expressly not a finding.**

---

## §6. Emission discipline, and what remains uncommitted

⚠️ **THIS PASS WAS NOT INTERRUPTED. All six corpus files are written and the
working tree is in its final intended state.**

⛔⛔ **Per the brief's COMMIT SEQUENCE, this commit contains the two `passes/`
artifacts ALONE.** The six corpus files are **deliberately left staged-out and
uncommitted for JD's review**. This is a knowing, instructed departure from
`CLAUDE.md`'s emission-discipline rule that a pass commits the entire registered
set together in one commit — **the brief overrides it explicitly, and the reason
the rule exists (a partial set landing without anyone knowing) does not apply
here, because the split is deliberate, announced, and the whole remainder is one
`git commit -a` away.**

**Owed to JD, in one commit, after review:**

```
Incense_Conversational_Outline.md
Incense_Reply_Source_Checks.md
PROJECT_STATE.md
RJ_Incense_Analysis.md
SRC_Manifest.md
St_Francis_EMC_Distinctives.md
```

✅ **Every touched file's stamp and its §4 registry cell were bumped together in
this pass, and C3 passes over all thirty registered stamped files.** Each edited
document received **exactly one** changelog entry (`St_Francis_EMC_Distinctives.md`,
`RJ_Incense_Analysis.md`, `Incense_Conversational_Outline.md`,
`Incense_Reply_Source_Checks.md`); `SRC_Manifest.md` and `PROJECT_STATE.md` carry
prepended header pass-notes, which is those two files' own convention.

---

## §7. Owed work, in rough order of how much it matters

1. ⛔⛔ **LOCUS 1 — JD's decision.** Whether to place `260835-64`'s drafted note
   inside the pamphlet capture's header at the cost of shifting seven logged
   line offsets, and if so, to annotate all seven and re-hash the manifest row in
   the same pass. §1(a).
2. ⛔⛔ **Every verbatim De Koven quotation in the repo is pamphlet-sourced and
   needs re-verification against the Debates.** `260835-64` §5 item 1 named at
   least `Incense_Reply_Source_Checks.md`,
   `Ritual_Canon_Examples_And_REC_Split.md` §1(b), `RJ_Incense_Analysis.md` and
   `Incense_Conversational_Outline.md`. **Not swept by `260835-64` and not swept
   here** — this pass was a debt-discharge pass and re-verification is research.
3. ⏳ **Five root analysis documents still unregistered in §4.** §4(c).
4. ⚠️ **The `IP` (7 reported / 17 real) and `LS` (21) §15 lags are unswept.**
   Both still WARN. Outside this brief.
5. ⚠️ **`[C11]` still reports drift on both arms** — the outline is checked
   against `DQ-26` and `IP-108` while the ledgers run to `DQ-28` and `IP-125`.
   ⛔ **No pointer was moved by this pass; moving one without doing the review
   would be the falsification the check exists to prevent.**
6. ⚠️ **The 1874 Journal capture's header** is "now incomplete rather than
   wrong" on the same point as LOCUS 1. §1(e). Minor.
7. ⚠️ **`Ceremonial_Meaning_Source_Checks.md` has no changelog.** Convention
   question for JD. §4(a).
8. ⚠️ **`CLAUDE.md` has still never been audited against
   `Project_Bootstrap_Prompt.md` for divergence** — `CLAUDE.md`'s own header has
   carried that as owed since `260728-2`. Not this pass's brief; restated because
   it is the file that instructs every agent.

---

## §8. What a later pass should NOT conclude from this one

- ⛔ **Do not read the manifest's seventeen new rows as verification of those
  captures.** They record digests and transcribed headers. §4(b).
- ⛔ **Do not read the `IP` lag's fall from 17 to 7 as progress.** No `IP`
  finding was swept. §3.
- ⛔ **Do not read the absent LOCUS 1 header note as an oversight.** It is a
  recorded decision with three grounds, escalated to JD. §1(a).
- ⛔ **Do not read `DQ-28`(c)/(d)'s §15 credit as RJ holding incense
  indifferent.** It is his account of what levels (1)–(3) demand. `IP-118`(b)
  stands unaltered and `DQ-28`(e) records the two as compatible-on-their-face
  and expressly not adjudicated.
- ⛔ **Do not deploy *"Correct."* detached from JD's 4:01 PM sentence.** The
  §15 credit carries that condition and it is not severable.
- ⛔ **Do not treat "the 1974 Measure repealed the Act of Uniformity 1662" as
  now safe with the exception appended.** What sections 10 and 15 contain was
  not established and must be obtained before anything is built on them.
