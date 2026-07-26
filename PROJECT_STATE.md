# PROJECT_STATE — the single source of truth for VOLATILE state

**Last updated: 260725-4** (created 260724-3). Read this file first, before any other project document.

> **260725-4 pass note.** Applied patch batches **260725-3** (sessions-ingested registry, capture codes, dual-capture procedure → `SRC_Manifest.md`) and **260725-2 REISSUE** (Revelation class corpus, findings **RV-1 … RV-23** → `St_Francis_EMC_Distinctives.md`). Changes in this file are confined to **§1** (one monitored-source row), **§3** (three common-ground entries added to the do-not-deploy register), **§4** (four version bumps) and **§5** (next-free numbers, new prefix rule). **No gate moved, no channel state changed, no question was answered or retired by this pass.** DQ-15 remains outstanding and DQ-9 remains the standing obstacle.
>
> **⚠️ TWO ITEMS AWAIT JD AND ARE SURFACED BY THE VALIDATOR ON EVERY RUN.** (1) **Two Anglican 101 sessions are registered but undated** (`A101-2026-TBD-01`, `A101-2026-TBD-02` in `SRC_Manifest.md`). **Until a date lands, no `IP` finding may be logged from them** — a finding cannot be dated from a session whose date is unknown. (2) **`IP-12` is under a wording-critical quoting freeze**: the finding is usable, quoting it at him is not, until `"regular principle"` is checked against his own audio.

<!-- PURPOSE HEADER -->

**AUDIENCE:** JD and Claude. Not Rev. James, not third parties.
**CLASS:** BACKSTAGE.
**FUNCTION:** The **only** authoritative record of anything that changes: whose turn it is, what has been asked, what has been answered, which gates are open, which levers are retired, what version each document is at, and what the next free source-tag number is.
**HANDLING:** ⚠️ **This file is short by design. Keep it short.** It holds *state*, never *argument*. Reasoning, evidence and analysis live in the corpus documents; if a line here needs a paragraph of justification, the paragraph belongs in the corpus and this file gets a pointer.

<!-- END PURPOSE HEADER -->

---

## ⚠️ THE RULE THIS FILE EXISTS TO ENFORCE

**Volatile state is authoritative HERE and nowhere else.**

Other documents may *discuss* state, and much of that discussion is valuable (routing, analysis, craft notes). But when a corpus document and this file disagree about **whether something was asked, whether it was answered, whose turn it is, or what version a file is at, THIS FILE WINS** and the corpus document is stale and must be corrected.

**Why this exists.** In July 2026 the status of one question (DQ-5) was restated in **five** places across three documents, each hand-maintained. One went stale, subsequent passes read the stale copy and re-affirmed it, and **a question that had been answered on 07-10 was carried as "awaiting reply" until 07-24** — holding the project's central funnel closed for two weeks behind a gate that was already open. The same mechanism carried question-list item 20 as "unposted" through three versions after it had been asked and answered. **Neither failure was caused by having many files. Both were caused by having many copies of one fact.**

**The discipline:** at the top of every reconcile pass, **update this file first**. Corpus edits follow from it, never the reverse.

---

## 0. HANDLING POLICY — CURRENT

**⚠️ POLICY CHANGE, 260725-1: ALL DOCUMENTS ARE INTERNAL ONLY. EXTERNAL SHARING IS SUSPENDED UNTIL FURTHER NOTICE.**

| Item | State |
|---|---|
| External sharing (to RJ, to the Discord intermediary, to any third party, including the pastor reviewer) | ⛔ **SUSPENDED** |
| Metadata, markup, annotation, purpose headers, changelogs | ✅ **PERMITTED IN EVERY FILE**, including `On_Incense_and_the_Altar.md` |
| `On_Incense_and_the_Altar.md` handling class | **INTERNAL** · relay-clean **SUSPENDED (RECOVERABLE)** |
| `Incense_Conversational_Outline.md` handling class | **INTERNAL** · relay-clean **SUSPENDED (RECOVERABLE)** *(⚠️ inferred, not explicitly directed — see note)* |
| Validator check **C7** (relay-clean firewall) | **WARN**, downgraded from ERROR |

**⚠️ THE DISCIPLINE IS DOWNGRADED, NOT DELETED.** Relay-clean is a *recoverable* state, not a retired one. C7 still runs and still reports; it no longer fails the build. The firewall rule itself — *nothing from `RJ_Incense_Analysis.md` ever enters a relay-clean document, including changelogs* — remains on the books and remains the standard those files must be returned to before any future external release. **To restore:** flip both CLASS lines back to RELAY-CLEAN, strip any backstage vocabulary C7 has accumulated in the interim, and change C7 back to `err(...)` in `validate_project.py`. Nothing about this pass makes that harder.

**⚠️ Note on `Incense_Conversational_Outline.md`.** The policy named `On_Incense_and_the_Altar.md` explicitly. The outline was *also* classed RELAY-CLEAN (shareable), to a pastor reviewer rather than to RJ, so "all documents are now internal only" reaches it too. It has been reclassed on the same terms. **Flagged because it was an inference, not a direction** — reverse it if the reviewer channel was meant to stay open.

**What has NOT changed.** The backstage/relay-clean *separation of content* still governs what is written where; only the sharing permission and the enforcement severity changed. `RJ_Incense_Analysis.md` remains the most sensitive file in the corpus regardless of who may see it.

---

## 1. CHANNEL STATE — whose turn is it

*The single most error-prone fact in the project. Check here before drafting anything.*

| Channel | State | Last message | By | Next action | Do not bump before |
|---|---|---|---|---|---|
| **Discord — Regulative Principle** ⭐ *priority channel* | ⏳ **AWAITING RJ** | 2026-07-23, 12:07 PM | JD | Wait. **Add nothing.** (DQ-15 posted) | **2026-07-30** |
| **Discord — 39 Articles / Formularies** | ✅ Closed by JD | 2026-07-21, 10:15 AM | JD | None. One item unanswered but **downgraded, do not bump** | n/a |
| **Discord — Seven sacraments vs. Art. 25** | ✅ Closed by JD | 2026-07-21, 10:16 AM | JD | None | n/a |
| **Discord — Baptism & Confirmation** | ✅ Closed | 2026-07-04, 12:36 PM | LilleyPartyofFive | None. **JD is not a participant** | n/a |
| **Anglican 101 — in person** | 🔄 Active, ongoing | (per session) | — | Attend; generates IP findings; **costs no Discord turn** | n/a |

### Monitored sources — no turn state, no action owed

*⚠️ **These are not channels.** They produce findings; they do not have a turn, cannot be bumped, and cost nothing to leave alone. Listed so an active recurring source is not invisible to the registry. (Added 260725-4 per batch 260725-2 §0.5; reverse if a source row is unwanted here.)*

| Source | State | Latest ingested | Findings | Note |
|---|---|---|---|---|
| **Revelation class — stream only** | 🔄 Active, ongoing | Session XI (uploaded 2026-06-30) | `RV` series | JD does **not** attend. Sessions I-VIII not ingested. Session rows in `SRC_Manifest.md` |

**⚠️ Standing constraint:** *one committal question per turn, per channel.* Rebuttals are held until the prior answer is on record.

**⚠️ Cross-channel note (learned 260724):** RJ replies in **batches across threads**, not per-thread. Two open questions in his queue means the second gets the shorter answer. **While DQ-15 is outstanding, do not open a new Discord thread.** Reassess if no reply by ~2026-07-30.

---

## 2. GATES

### ⚠️⚠️ THE STANDING OBSTACLE — DQ-9, AND IT IS UNDERNEATH EVERYTHING

> **Read this before planning any incense move. It is not a gate and it is not a question in a queue; it is a structural problem in the project's whole approach, and it has no owner yet.**
>
> **What he said (DQ-9, 2026-07-11).** *"The RPW is about principles and not individual acts."* His complaint is against those who use the RPW "for individual practices, demanding those EXACT practices be found in Scripture, rather than principles that are drawn from the witness of Scripture." His stated principle: *"that imagery and symbolism are to reflect the Biblical witness."*
>
> **Why it is the obstacle.** DQ-4's three warrant sources — command, approved example, necessary inference — are all **act-level**. DQ-9 substitutes **principle-level** warrant without formally retracting DQ-4. **Under DQ-9 incense passes trivially**, and so does most of the Western ceremonial tradition.
>
> **⚠️ THE SCOPE OF THE PROBLEM, STATED PLAINLY (260725-1 audit finding).** This is not one unanswered question among several. **Every prepared incense question presupposes act-level warrant** — question-list items 1, 1b, 1c, 1d, 1e and 21 all ask where *the act* is warranted. **`Incense_Conversational_Outline.md` presupposes it at Steps 3, 5, 5b and 6.** `RJ_Incense_Analysis.md` presupposes it throughout. **If DQ-9 is left unengaged, the funnel dissolves at the last step regardless of how well every prior step went**, because he can grant every finding and still answer "the principle is satisfied."
>
> **⚠️ What does NOT exist yet.** **No document in the corpus argues act-level warrant over principle-level warrant.** The outline has no step for it (drift report, 260725-1, item 2). The question list has no item for it. That argument is unwritten, it is JD's to write, and **it is the highest-value unwritten thing in the project.**
>
> **The material is already logged and waiting:** **DQ-10** (asked directly and in the friendliest terms for one thing the imagery principle excludes, it produced none — the single case offered is excluded by a separate rule about the object of worship, so the principle licenses and filters nothing) and **DQ-4** (the act-level sources he affirmed, which DQ-9 loosens without retracting).
>
> ⚠️ **Do not treat this as fixed by the DQ-15 answer, whatever it says.** DQ-15 asks about **genre** — whether vision, prophecy and recorded practice transfer alike. That is the transfer question. **DQ-9 is the level question, and it sits under the transfer question**: even a favourable genre answer leaves principle-level warrant intact and incense passing on it. **Sequence the level question after DQ-15 lands. Do not let a good answer on DQ-15 read as the funnel closing.**


| Gate | State | Closed by | Date |
|---|---|---|---|
| **Definitional gate** — does he require positive warrant for acts of worship? | ✅ **CLOSED** ("Correct") | DQ-4 | 2026-07-10 |
| **Funnel gate** — filter on record in his own words before incense enters | ✅ **SATISFIED, both strands** | DQ-7 (Revelation) + DQ-8/DQ-9 (OT carryover) | 2026-07-11 |

**⚠️ Consequence:** the Bucket A incense material is **unlocked**. The lock-before-port sequence is discharged. Remaining obstacle is **DQ-9**, not the gate.

---

## 3. QUESTION STATE

### Posted, awaiting reply
| ID | Question | Posted | Channel |
|---|---|---|---|
| **DQ-15** ⭐ | Grounding question in genre form: does the DQ-7 transfer rule work the same for a heavenly vision, a prophecy, and a recorded NT-church practice? | 2026-07-23 | RPW |
| — | Self-contradictions closure (locks the DQ-1 enumeration) | 2026-07-14 | Formularies · ⚠️ **DOWNGRADED, do not bump** |

### Drafted and queued (NOT posted)
| ID | Question | Status |
|---|---|---|
| **DQ-10 follow-up** | "Is there anything the imagery principle rules out on its own?" | ⏸ **QUEUED behind DQ-15.** Not competing. |
| **Q-Inc-5 / item 1e** | Priesthood-mediation question | Filed, not posted |
| **Q-Inc-0, QC-f, QC-a, …** | Bucket A incense set | Gate satisfied; sequencing not yet set |

### Answered / retired this cycle
| ID | Result |
|---|---|
| **DQ-5** ★ crux | ✅ Answered 2026-07-10 (see DQ-8/DQ-9) |
| **Item 20** — Art. 25 grace | ✅ Answered 2026-07-20 → **RETIRED** |
| **DQ-7** verification flags (×2) | ✅ Discharged 260724-1 |
| **QC-a** — which Article's title vs. content | ✅ Resolved → Article 29 (GV-43) |

### ⛔ DO-NOT-DEPLOY REGISTER
*Retired levers and common ground. Do not reopen without a recorded reason.*

**⚠️ Entries that correspond to a question-list item carry an explicit `[→ item N]` pointer.** Check **C9** reads these pointers and verifies the named item carries a retirement marker. **An entry without a pointer is not checked** — add one whenever a register entry maps to an item.

- **Article 25 / seven sacraments** — he answered formulary-faithfully (DQ-2, DQ-11) `[→ item 7]` `[→ item 20]`
- **Lent** — formulary-faithful `[→ item 14]`
- **Baptismal regeneration** — the formulary position; he is faithful to it (GV-38) `[→ item 9]`
- **Invocation — THE LEVER ONLY.** His formulation ("in directing our prayers to God, ask Him that He have the Saints in Heaven pray for us") is Article 22-compatible; **common ground, not a lever** (DQ-7, DQ-7a). ⚠️ **The retirement covers the lever, not the subject. Question-list item 15 is LIVE and has been DEPLOYED** — JD is clarifying what RJ means by it, and that work is in progress. **No `[→ item N]` pointer, deliberately:** C9 must not demand a retirement marker on live work. *(Distinction recorded 260725-1, after C9 flagged item 15 and the obvious reading was the wrong one.)*
- **Broad principle "fulfilled symbols cease"** — ⚠️ **do not run**; use only the narrow form (Levitical-priesthood-attached symbols cease absent NT reinstitution)
- **1 Cor 10:1-2 parity point** (DQ-9) — category confusion; low value; do not spend a turn
- **"The Romans would agree with us"** aside (DQ-11) — factually doubtful, **JD's knowledge only, never deployed**
- **DQ-6 Laud quotation** — provenance UNVERIFIED; never attribute to RJ
- **DQ-14** third-party comment — never attribute to RJ
- **Councils recognize truth, they do not constitute it (RV-15)** — formulary-faithful and inconsistent with a magisterial view; the receptionist account is the Anglican and the Reformed one both. **Common ground, not a lever.** *(Useful as a datum for the Article VI two-tier thread — authority to recognize is not authority to require — but that is a supporting premise, not a charge.)*
- **Word and sacrament in Article 28 compatible language (RV-9)** — "receive both word and sacrament … the body and blood of Christ" is language the Articles themselves use. **Common ground, not a lever.** Says nothing about sacrifice; the Mass-as-sacrifice gap is untouched by it
- **"2 + 2 = 4 regardless of who says it" — he rejects reactive theology by name (RV-14).** ⚠️ **Never deploy as a gotcha.** It is a methodological commitment JD shares and **it is HIS OWN STATED STANDARD**, which makes it available later as a *shared premise* and worthless as a charge

*⚠️ **The three RV entries above deliberately carry NO `[→ item N]` pointer.** They map to no question-list item because no lever was ever built on them; per the note above, an entry without a pointer is not checked by C9, and that is correct here rather than an omission. (Added 260725-4, currency-audit item 6.)*

---

## 4. DOCUMENT REGISTRY

**⚠️ PATHS ARE PART OF THE REGISTRY.** Every registered file is listed by its **exact repo-relative path**, not by a bare filename. `validate_project.py` derives its expected file set from this table; a bare filename here becomes a check that silently matches nothing. *(See §7 — this is exactly how C1 and C6 ran zero times while reporting a clean pass.)*

| Path | Version | Class | Audience |
|---|---|---|---|
| `PROJECT_STATE.md` | 260725-4 | Backstage | JD + Claude |
| `St_Francis_EMC_Distinctives.md` | 260725-4 | Backstage — findings corpus | JD only |
| `RJ_Final_Question_List.md` | v17 (260725-1) | Backstage — question bank | JD only |
| `RJ_Incense_Analysis.md` | 260725-1 | ⚠️ **BACKSTAGE — DO NOT SHARE** | JD only |
| `On_Incense_and_the_Altar.md` | 260725-1 | **INTERNAL** · relay-clean **SUSPENDED (recoverable)** | JD only |
| `Incense_Conversational_Outline.md` | 260725-4 | **INTERNAL** · relay-clean **SUSPENDED (recoverable)** | JD only |
| `SRC_Manifest.md` | 260725-4 | Source registry | JD + Claude |
| `src/SRC_Discord_RPW.md` | 260724-1 | Raw archive — never edited except date resolution | — |
| `src/SRC_Discord_39ArticlesFormularies.md` | 260724-3 | Raw archive — never edited except date resolution | — |
| `src/SRC_Discord_SevenSacraments.md` | 260724-3 | Raw archive — never edited except date resolution | — |
| `src/SRC_Discord_BaptismConfirmation.md` | 260722-1 | Raw archive — never edited except date resolution | — |
| `README.md` | ⚠️ **STALE — see below** | Repo front page | JD + Claude |
| `Project_Bootstrap_Prompt.md` | (unstamped) | Conventions | JD + Claude |

### Repo layout — record it, do not assume it

```
<repo root>/
├── PROJECT_STATE.md              ← read first
├── St_Francis_EMC_Distinctives.md
├── RJ_Final_Question_List.md
├── RJ_Incense_Analysis.md
├── On_Incense_and_the_Altar.md
├── Incense_Conversational_Outline.md
├── SRC_Manifest.md
├── README.md
├── Project_Bootstrap_Prompt.md
├── validate_project.py
└── src/                          ← ⚠️ THE ARCHIVES ARE NOT FLAT
    ├── SRC_Discord_RPW.md
    ├── SRC_Discord_39ArticlesFormularies.md
    ├── SRC_Discord_SevenSacraments.md
    └── SRC_Discord_BaptismConfirmation.md
```

**⚠️ NO TOOL MAY ASSUME A FLAT TREE.** The `src/` placement of the archives is the actual layout and has been since before the July 2026 failure. Any check that globs the working directory for `SRC_Discord_*.md` will match nothing and report success. Derive from this registry; search recursively on a path miss; error on unresolvable.

**Repo status.** Private, internal-use-only git repository. A **pre-commit hook runs `validate_project.py`**, so a check that silently skips is worse than one that fails loudly: it makes every commit look verified.

⚠️ **Two paths above are unconfirmed** (`SRC_Manifest.md` and `README.md` at repo root). They are the natural reading of "archives live under `/src/`, not flat," but JD stated the layout only for the archives. The validator's recursive fallback resolves either way and warns when a registered path had to be found elsewhere. **Correct the table if the fallback fires.**

**⚠️ `README.md` IS STALE AND IS NOW REGISTERED SO IT STOPS BEING INVISIBLE.** It carries "Current baselines: Distinctives at `260621-1`, Question List at `260621-1 (v11)`, both incense documents at `260621-1`" — thirteen versions and a month out of date — and it still advertises `On_Incense_and_the_Altar.md` as "Relay-clean (shareable)," which the 260725-1 policy change contradicts. It was never in the registry, so no check ever looked at it. **This is the same defect class as the C1/C6 silent skip: a file outside the registry is a file outside every guarantee.** Fixing the README content is deferred; registering it is not.

⚠️ **Backstage/relay-clean content separation still governs**, per §0. Nothing from `RJ_Incense_Analysis.md` enters a relay-clean-class document, including changelogs, even while the class is suspended.

---

## 5. NUMBERING REGISTRY

**Next free number by prefix:** `DQ-16` · `IP-13` · **`RV-24`** · **`LS-1` (RESERVED, unused)** · `QA` is a question-list label series, not a finding series (see rule 5) · (GV, BP, RC, EXT, Rev closed batches)

**Rules:**
1. Numbering is **cumulative and unbroken** within each prefix. Never reuse, never renumber a live tag.
2. ⚠️ **Amendment entries take the PARENT's number with a letter suffix** — an entry that corrects, verifies or discharges a flag on `DQ-7` is **`DQ-7a`**, not the next sequential number. *(Added 260724-3 after an amendment to DQ-7 was mis-numbered DQ-11a by position; corrected.)*
3. Only genuine **sources** get tags. External reviewers, critiques and commentary are logged `[Analysis]` with no tag.
4. `DQ` now spans **four threads**; the thread is identified in the finding body and in `SRC_Manifest.md`, not by the prefix.
5. ⚠️ **`QA-*` tags are question-list labels, not source tags.** They name a sharpening *within* a question item (`QA-Euc` → item 4, `QA-Art31` → item 4a, `QA-Art25` → item 7, `QA-Art34` → item 8a). They are cited from the distinctives, so **a `QA-` tag must exist in `RJ_Final_Question_List.md` before it is cited anywhere else.** Three of the four were cited into a void from v11 to v16; check **C8** now guards this.
6. ⚠️ **One tag, one finding.** A tag serving two findings forks its own citation trail and every downstream cross-reference becomes ambiguous. If a finding needs its own identity, it takes **the next free number**, not a letter suffix — suffixes are reserved for amendments to a parent (rule 2). *(Added 260725-1 on resolving the IP-4 collision, which sat unresolved for three months because re-tagging touches three documents.)*
7. ⚠️ **PREFIX SCOPE — what sorts is WHAT THE RECORDING IS, not how it was delivered.** *(Added 260725-4 with batch 260725-2, before the 200-plus video archive arrives and a bad scheme becomes expensive.)*

   | Prefix | Scope |
   |---|---|
   | `IP` | Anglican 101 sessions JD attends in person, 2026 onward. **Delivery-independent:** if one of these later arrives as a YouTube-derived transcript, it is still `IP` |
   | `RV` | The Revelation class series (2026 run, sessions IX onward). *The 2025 run is the closed `Rev` batch; do not extend it* |
   | `LS` | Everything else on the channel: standalone videos, topical streams, interviews, response videos. **This is the 200-plus bucket** |

   Two supporting conventions. **A new prefix is minted only for a sustained, self-numbering teaching series**; one-off videos go to `LS` regardless of topic. And **`BP`, the Everhard response video, is a closed batch that would today be `LS` — leave it alone; do not retro-renumber a closed series.**

   ⚠️ **THE DUPLICATION HAZARD THIS CREATES, AND THE HASH CHECK IS BLIND TO IT.** Because the Anglican 101 classes are also streamed, **the same session can enter the corpus twice**: once as JD's room recording, once as a YouTube-derived transcript in a future batch. Those are two files with two hashes, and a hash check passes both. **The ingestion test is the sessions-ingested registry in `SRC_Manifest.md`, keyed on session — not the hash.** Without it, one batch out of the 200 can silently re-log IP-1 through IP-12 under fresh tags, which is the IP-4 collision arriving by a different door.

---

## 6. INTAKE CHECKLIST — run every time

1. **Note the handover date.** Relative timestamps ("Yesterday", "Today") are relative to **the date JD supplies the paste**, not to the intake session.
2. **Resolve every relative timestamp to an absolute date, in the `SRC_Discord_*.md` file itself**, before logging anything.
3. **Update `PROJECT_STATE.md` FIRST** — channel state, question state, gates.
4. Log findings in the corpus, each dated from its **message timestamp**.
5. Patch the question list and topical analyses.
6. **Run `validate_project.py`.** Fix everything it reports.
7. Update version stamps and changelogs.

---

## 7. KNOWN DEFECTS — deferred, not forgotten

| Defect | Status |
|---|---|
| **IP-4 tag collision** — one tag doing double duty (five-sacraments finding *and* §13 incense finding) | ✅ **RESOLVED 260725-1.** IP-4 retained for the sacraments finding; the §13 incense finding promoted to **IP-12**, with a ledger entry added and live cross-references updated across the distinctives, the incense analysis, the question list, and `SRC_Manifest.md`. Historical changelog entries left as written, per the never-alter rule |
| **Validator silent-skip (C1, C6)** — glob-restricted checks matched nothing and reported a clean pass | ✅ **RESOLVED 260725-1.** Checks now derive from the §4 registry, resolve recursively, error on unresolvable, and a coverage assertion fails the run if any check contributes zero results. See §8 item 1 |
| **Dangling question IDs** `QA-Art25`, `QA-Art31`, `QA-Euc` | ✅ **RESOLVED 260725-1** → items 7, 4a, 4 respectively. New check **C8** guards the class |
| **`README.md` never registered, baselines stale at 260621-1 / v11** | ⚠️ **PARTIALLY RESOLVED 260725-1.** Now registered (§4) so checks can see it. **Content still stale — deferred** |
| **TM-8.6** — Pope Benedict XVI quotation | UNVERIFIED; broader apologetics workstream |
| **DQ-6** — Laud quotation | Provenance UNVERIFIED |
| **`St_Francis_EMC_Distinctives.md` is ~372 KB of prose** | Retrieval is slow and grep-dependent. ⚠️ **The JSONL re-encode proposal is RETIRED (260725-1) — JD is satisfied with the prose format.** The size is accepted as a working condition, not a defect awaiting a fix. Mitigation is anchor discipline and the validator, not conversion |

---

## 8. RECURRING CURRENCY AUDIT — the checklist

> **⛔ RETIRED 260725-1: the distinctives JSONL re-encode.** The former §8 staged a machine-readable conversion of `St_Francis_EMC_Distinctives.md`. **JD is satisfied with the prose format; the proposal is retired, not deferred.** Do not re-propose it. Its one durable warning is preserved elsewhere and still binds: *never flatten the three-layer attribution system, and never drop the do-not-deploy guards.* That warning now applies to any tooling that touches the corpus, not to a conversion that is not happening.

**Why this replaced it.** The re-encode was a solution to slow retrieval. The failures this project has actually sustained were **currency failures, not retrieval failures**: a stale status carried nine days (DQ-5), a stale item carried three versions (item 20), two validator checks running zero times while reporting clean, three question IDs cited into a void, one tag doing double duty for three months, a §15 that had not moved since the RC batch, and a README a month out of date. Every one of those is a thing that was true once and quietly stopped being true. **This checklist is the instrument for that class.**

**Cadence:** every reconcile pass, and any standalone pass tagged CURRENCY AUDIT. **Run in order.** Items 1-3 are mechanical; 4-8 need judgment and cannot be delegated to the validator.

### 1. Tooling first — did the checks actually run?
- [ ] Run `python3 validate_project.py` (add a root path if not run from the repo root).
- [ ] **Read the COVERAGE SUMMARY before reading the results.** A check reporting **0 files seen is a failure**, regardless of the error count. The run exits non-zero on zero-coverage precisely so this cannot be skimmed past.
- [ ] Confirm every registered path in §4 resolved **exactly**. A `[C0] resolved by search` warning means the registry is wrong; fix the registry, not the file.
- [ ] Remember the pre-commit hook: a silent skip makes every commit since the defect look verified. **Distrust a clean pass you did not read the coverage line of.**

### 2. Stamps and registry
- [ ] Every document's `**Last updated:**` stamp matches its §4 registry row (C3).
- [ ] Every file in the repo is *in* §4. **An unregistered file is outside every guarantee** — that is how the README drifted a month.
- [ ] Stamps stay machine-parseable. `PROJECT_STATE.md` and `SRC_Manifest.md` were versioned in **prose only** until 260725-1 and were therefore uncheckable by C3; both now carry a standard `**Last updated:**` line. **Do not revert either to a prose-only version note.**

### 3. Cross-reference integrity
- [ ] Question IDs cited in the distinctives all resolve in the question list (C8).
- [ ] No do-not-deploy item is still marked deployable in the question list (C9).
- [ ] Source tags: numbering unbroken, no duplicates, no tag doing double duty (C2). **A tag serving two findings is a citation trail that silently forks.**
- [ ] **Sessions, not hashes** (C12, added 260725-4). Every session row in `SRC_Manifest.md` marked `SECONDARY — SWEEP PENDING` has a recorded sweep; every byte offset cited after 260725 carries a capture code. **A registered-but-unreconciled second capture is the two-copies-of-one-fact condition this file exists to prevent, and it must not sit quietly across commits.**

### 4. ⚠️ THE BALANCE CHECK — is §15 keeping pace?
- [ ] Count DQ/IP findings added since the last pass. Count §15 additions since the last pass. **If tensions grew and §15 did not, the source-of-truth document is drifting adversarial** (C10 flags this mechanically; the judgment is yours).
- [ ] Sweep the pass's new findings for anything marked *common ground*, *credit it*, *formulary-faithful*, *do not deploy*, or *no lever here* — and confirm each was actually folded into §15, not merely noted in an analysis block. **Noted is not logged.** Every §15 addition made on 260725-1 had been sitting in an analysis note, some for two weeks.
- [ ] Ask directly: *would RJ recognise himself in §15?* If §15 reads thinner than the tensions sections, the corpus is no longer a record of a man; it is a brief against him.

### 5. Volatile state
- [ ] Channel state, gates, and question state in §1-§3 updated **before** any corpus edit.
- [ ] No corpus document asserts a status that contradicts this file (C4).
- [ ] Every relative timestamp in every `src/SRC_Discord_*.md` resolved to an absolute date **in the archive file itself** (C1). **This is the July 2026 bug.**
- [ ] Archive hashes match `SRC_Manifest.md` (C6).

### 6. Retired levers
- [ ] Anything answered formulary-faithfully this pass added to the §3 do-not-deploy register.
- [ ] Nothing on the register has quietly reactivated in the question list.

### 7. Derived and dependent documents
- [ ] Documents carrying a derivation pointer re-checked against their source (currently: `Incense_Conversational_Outline.md` ← `RJ_Incense_Analysis.md` + the distinctives). **Report drift; do not rewrite JD's reasoning without asking** (C11).
- [ ] Handling classes in §0 still match the CLASS line in each file's purpose header.

### 8. Close the pass
- [ ] Changelogs prepended, never altered.
- [ ] Version stamps bumped in both the document and the §4 registry.
- [ ] Re-run the validator. **Read the coverage summary again.**

**⚠️ Do not run a currency audit in the same session as a live intake.** Intake creates the state this checklist audits; auditing it in the same breath audits your own unfinished work.
