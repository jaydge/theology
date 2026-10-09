# 260835-73 close-out: Incense outline memory card

**Pass:** 260835-73. **Date:** 2026-10-09. **Mode:** RECONCILE (one new document plus registry entries). **Passes never commit:** nothing was added or committed.

## 1. Gate outputs (verbatim)

`git -C ~/EMC/theology rev-parse HEAD`:
```
a5d8cc9d3c6e13d05eb5e437480bc000beca6b7e
```
`git -C ~/EMC/theology status --short` (before the first edit):
```
(empty: no output)
```
HEAD commit: `a5d8cc9 260835-72: Followup-thread intake (DQ-29..37), reserve register, status reconcile`.

**Prerequisite check (260835-72 applied and committed): PASS.** `Incense_Conversational_Outline.md` carries `**Last updated: 260835-72**`, a `260835-72` changelog entry (line 724 at gate time), and the `260835-72` dated block under the Deployment map with its sixteen-item reserve register (`(b) Reserve register (new, 260835-72)`, line 691 at gate time).

**Stamp check:** `260835-73` returned zero hits across tracked `*.md`/`*.py` and in `git log --all`, so it was free. **Starting stamps of the files touched:** `PROJECT_STATE.md` was at `260835-72` in both its document stamp and its §4 cell, so they agreed. `Incense_Outline_Memory_Card.md` is new.

**Read in full before writing:** `Incense_Conversational_Outline.md` (all 783 lines: steps, dated notes, the Deployment map, the `260835-72` overlay and reserve register, the changelog); `PROJECT_STATE.md` §0 to §4; `RJ_Final_Question_List.md` v23 live-status block and the item 1e dated note. Also checked: `DQ-16` to `DQ-19`, `DQ-29` to `DQ-37` and the `JD-RECORD` block in `St_Francis_EMC_Distinctives.md`; `IP-3`, `IP-114` and the `BP-38`/`RC3-8` entries; `Orthodox_Bridge_Rebuttal_Assessment.md` §3.4 and §7.3; and `Malachi_1_11_Lexical_Analysis.md` for the Hophal cue. `src/SRC_Discord_Followup-raw.txt` hashes to `48bb0a586b7d69d3f053a840f0d7fb59d3f5b5fe15f5cb41e66bafd300d0d528`, which matches the manifest. Every Followup-thread quotation on the card was grep-confirmed verbatim against the raw, and every RPW-thread quotation against `src/SRC_Discord_RPW.md`; one was corrected from "The RPW" to "the RPW" to match the source's lowercase. `BP-38`, `RC3-8`, `IP-3` and `IP-114` are video or in-person findings and are quoted from the ledger only; the card labels them as such and marks `IP-114` NOT quotable.

## 2. Files touched, with anchors

1. **`Incense_Outline_Memory_Card.md`** (NEW, repo root, untracked; 22,822 B; sha256 `2d5b6885400a014cbe574f0f5ed707d5a99577a28fbc1ed1ef33e48d174a8fc3`). It contains the purpose header, the stamp `260835-73`, the derivation pointer (outline @ `260835-72`), the prepended changelog, Layer A, standing guards, Layer B, Layer C (Mermaid) and Layer D. The spoken core was inserted by script, copied byte-for-byte from the outline's `## The two-minute spoken core` line, not retyped. A copy is at `~/EMC/staging-73/Incense_Outline_Memory_Card.md`.
2. **`PROJECT_STATE.md`**, three anchored edits:
   - The line `**Last updated: 260835-72** (created 260724-3)…` became `**Last updated: 260835-73**…`, and a one-line `260835-73` changelog entry was inserted directly beneath it, above the `260835-72` GATE block.
   - In the §4 row for `PROJECT_STATE.md`, the version cell `260835-72` became `260835-73`, and a short `260835-73` note was prepended to the description cell. The prior cell text is retained verbatim after *(Prior cell text retained:)*.
   - A new §4 row, `Incense_Outline_Memory_Card.md` | `260835-73` | class + derivation pointer | JD only, was inserted immediately after the `Incense_Conversational_Outline.md` row.

**Not touched:** `Incense_Conversational_Outline.md` and every other document.

**⚠️ One deliberate deviation from the brief's wording, flagged for JD.** The brief says to add a new registry row and "do not alter other rows." I also bumped `PROJECT_STATE.md`'s own stamp and its own §4 row to `260835-73`, keeping the prior text. The reason is that `CLAUDE.md`'s close-out checklist item 3 requires a touched file's stamp and registry cell to move together, and validator C3 errors if they disagree. No other document's row was altered. **If JD prefers the literal reading, the alternative is to revert the two stamp/cell edits and keep only the new row and the changelog line; C3 stays green either way.**

## 3. Brief items corrected against the record (the record won)

1. **5b cue.** The brief proposed "Zacharias outside, people praying." Luke 1:9-10, as the outline uses it, has the people praying outside and Zacharias offering inside. The cue on the card is "People outside, Zacharias inside."
2. **Cyril "print check pending".** This is stale. JD verified the reading against the page on 2026-10-09, and it is captured and Tier 1 per the outline's `260835-72` Step 5c note and reserve item 10. The card carries the remaining live guard instead: the v.12 line "their incense fragrant" must be read with the spiritual-incense gloss that precedes it.
3. **"He has stated no sorting rule".** This is superseded. On 2026-10-08 he stated "fulfillment widens" (`DQ-37`(b)), per the outline's Step 6 `260835-72` note. The card's guard says that his only stated sorting rule is "fulfillment widens" and that the three-pattern sort is `[Analysis]`.
4. **"Instituted means required" (Step 2 cue).** It was not used. The phrase never occurs in the capture (grep 0, recorded at `260835-72`), so a cue built on it would point at nothing in the record. The Step 2 cue is his own "Expected but not required" (`IP-12`), with JD's 10/8 WCF line as the anchor.
5. **"Nobody keeps Leviticus 2".** It was replaced by the modal-split form. "Nobody keeps" has the same shape as the retired "nobody performs" clause (`260835-3`: true as intended, answerable as heard). The Step 4 cue is "One Hophal, two subjects," which comes from `Malachi_1_11_Lexical_Analysis.md` and not from the outline itself; that provenance is noted here so it is not mistaken for outline text.
6. **"His Discord line has moved three times (… 8/25 reception …)".** This is kept, with a precision added. The 8/25 to 8/28 reception material (`DQ-24`(b), `DQ-25`, `DQ-26`) was stated generally and was never applied to incense by name, so the card says exactly that.

## 4. Validator runs (full, verbatim)

### 4a. Baseline (before any edit)

```
========================================================================
PROJECT INTEGRITY VALIDATION   root: /sessions/rcw-0184vrr2bp786r7j4i1iljtt/mnt/EMC/theology
========================================================================
  ok    [C0] PROJECT_STATE.md: resolved at registered path
  ok    [C0] ORCHESTRATION.md: resolved at registered path
  ok    [C0] passes/README.md: resolved at registered path
  ok    [C0] St_Francis_EMC_Distinctives.md: resolved at registered path
  ok    [C0] RJ_Final_Question_List.md: resolved at registered path
  ok    [C0] RJ_Open_Questions_and_Divergences.md: resolved at registered path
  ok    [C0] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: resolved at registered path
  ok    [C0] Protestant_Commentary_Survey_Malachi_1_11.md: resolved at registered path
  ok    [C0] Patristic_Citations_Incense_Verification.md: resolved at registered path
  ok    [C0] Tertullian_Incense_Passages.md: resolved at registered path
  ok    [C0] Brattston_Article_Assessment.md: resolved at registered path
  ok    [C0] Frere_Appendix_A_Translated.md: resolved at registered path
  ok    [C0] Orthodox_Bridge_Rebuttal_Assessment.md: resolved at registered path
  ok    [C0] Malachi_1_11_Lexical_Analysis.md: resolved at registered path
  ok    [C0] Ceremonial_Meaning_Source_Checks.md: resolved at registered path
  ok    [C0] Incense_Reply_Source_Checks.md: resolved at registered path
  ok    [C0] American_Episcopal_Reception_1899_Opinion.md: resolved at registered path
  ok    [C0] Ritualist_Case_For_Incense_and_the_1899_Opinion.md: resolved at registered path
  ok    [C0] RJ_Incense_Analysis.md: resolved at registered path
  ok    [C0] On_Incense_and_the_Altar.md: resolved at registered path
  ok    [C0] Incense_Conversational_Outline.md: resolved at registered path
  ok    [C0] SRC_Manifest.md: resolved at registered path
  ok    [C0] SRC_Channel_Inventory.md: resolved at registered path
  ok    [C0] SRC_Coverage_Register.md: resolved at registered path
  ok    [C0] asr_keyterms_A101.md: resolved at registered path
  ok    [C0] src/SRC_Discord_RPW.md: resolved at registered path
  ok    [C0] src/SRC_Discord_Assurance.md: resolved at registered path
  ok    [C0] src/SRC_Discord_Assurance-raw.txt: resolved at registered path
  ok    [C0] src/SRC_Discord_39ArticlesFormularies.md: resolved at registered path
  ok    [C0] src/SRC_Discord_SevenSacraments.md: resolved at registered path
  ok    [C0] src/SRC_Discord_BaptismConfirmation.md: resolved at registered path
  ok    [C0] README.md: resolved at registered path
  ok    [C0] Project_Bootstrap_Prompt.md: resolved at registered path
  ok    [C0] tools/transcribe_yt.py: resolved at registered path
  ok    [C0] validate_project.py: resolved at registered path
  ok    [C0] CLAUDE.md: resolved at registered path
  ok    [C1] src/SRC_Discord_39ArticlesFormularies.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_Assurance.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_BaptismConfirmation.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_SevenSacraments.md: no unresolved relative timestamps
  ok    [C2] DQ-1..37 unbroken, no duplicates
  ok    [C2] IP-1..125 unbroken, no duplicates
  ok    [C2] RV-1..63 unbroken, no duplicates
  ok    [C2] LS-1..141 unbroken, no duplicates
  ok    [C2] BLOG-1..158 unbroken, no duplicates
  ok    [C2] POD-1..16 unbroken, no duplicates
  ok    [C3] PROJECT_STATE.md: version agrees with registry (260835-72)
  ok    [C3] ORCHESTRATION.md: version agrees with registry (260835-37)
  ok    [C3] passes/README.md: version agrees with registry (260832-3)
  ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260835-72)
  ok    [C3] RJ_Final_Question_List.md: version agrees with registry (260835-72 (v23))
  ok    [C3] RJ_Open_Questions_and_Divergences.md: version agrees with registry (260833-2)
  ok    [C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: version agrees with registry (260832-2)
  ok    [C3] Protestant_Commentary_Survey_Malachi_1_11.md: version agrees with registry (260835-45)
  ok    [C3] Patristic_Citations_Incense_Verification.md: version agrees with registry (260835-47)
  ok    [C3] Tertullian_Incense_Passages.md: version agrees with registry (260835-48)
  ok    [C3] Brattston_Article_Assessment.md: version agrees with registry (260835-49)
  ok    [C3] Frere_Appendix_A_Translated.md: version agrees with registry (260835-50)
  ok    [C3] Orthodox_Bridge_Rebuttal_Assessment.md: version agrees with registry (260835-51)
  ok    [C3] Malachi_1_11_Lexical_Analysis.md: version agrees with registry (260835-52)
  ok    [C3] Ceremonial_Meaning_Source_Checks.md: version agrees with registry (260835-56)
  ok    [C3] Incense_Reply_Source_Checks.md: version agrees with registry (260835-65)
  ok    [C3] American_Episcopal_Reception_1899_Opinion.md: version agrees with registry (260835-55)
  ok    [C3] Ritualist_Case_For_Incense_and_the_1899_Opinion.md: version agrees with registry (260835-39)
  ok    [C3] RJ_Incense_Analysis.md: version agrees with registry (260835-65)
  ok    [C3] On_Incense_and_the_Altar.md: version agrees with registry (260833-2)
  ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260835-72)
  ok    [C3] SRC_Manifest.md: version agrees with registry (260835-72)
  ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260835-72)
  ok    [C3] SRC_Coverage_Register.md: version agrees with registry (260835-72)
  ok    [C3] asr_keyterms_A101.md: version agrees with registry (260830-2)
  ok    [C3] README.md: version agrees with registry (260835-8)
  ok    [C3] Project_Bootstrap_Prompt.md: version agrees with registry (260816-1)
  ok    [C3] tools/transcribe_yt.py: version agrees with registry (260833-7)
  ok    [C3] validate_project.py: version agrees with registry (260835-39)
  ok    [C3] CLAUDE.md: version agrees with registry (260835-72)
  ok    [C4] RJ_Final_Question_List.md: no unmarked stale-status passages for answered questions
  ok    [C4] RJ_Incense_Analysis.md: no unmarked stale-status passages for answered questions
  ok    [C5] total volatile-state assertions outside PROJECT_STATE: 34
  ok    [C6] src/SRC_Discord_39ArticlesFormularies.md: hash matches manifest
  ok    [C6] src/SRC_Discord_Assurance.md: hash matches manifest
  ok    [C6] src/SRC_Discord_BaptismConfirmation.md: hash matches manifest
  ok    [C6] src/SRC_Discord_RPW.md: hash matches manifest
  ok    [C6] src/SRC_Discord_SevenSacraments.md: hash matches manifest
  ok    [C7] On_Incense_and_the_Altar.md: relay-clean firewall intact (class suspended; no cleanup owed)
  ok    [C7] Incense_Conversational_Outline.md: relay-clean firewall intact (class suspended; no cleanup owed)
  ok    [C8] all 4 QA-* citations resolve in the question list
  ok    [C8] all 7 VP- label(s) defined in the distinctives; 7 cited, none dangling
  ok    [C9] item 7: carries a retirement marker, consistent with the register
  ok    [C9] item 20: carries a retirement marker, consistent with the register
  ok    [C9] item 14: carries a retirement marker, consistent with the register
  ok    [C9] item 9: carries a retirement marker, consistent with the register
  ok    [C10] every finding flagged as common ground is credited in §15
  ok    [C10] §15 is within 1 finding(s) of the RV ledger head (RV-63)
  ok    [C10] §15 is within 0 finding(s) of the BLOG ledger head (BLOG-158)
  ok    [C10] §15 is within 0 finding(s) of the POD ledger head (POD-16)
  ok    [C11] RV current in the outline pointer (RV-63 @ 260830-1, ledger at RV-63)
  ok    [C12] session registry parsed: 77 capture row(s) across 66 session(s)
  ok    [C12] 27 standalone recording row(s) parsed and correctly EXCLUDED from the session count (manifest rule: a standalone recording gets no session row)
  ok    [C12] no capture is stuck in SECONDARY -- SWEEP PENDING
  ok    [C12] retrofit rule present: bare pre-260725 offsets resolve to their session's PRIMARY capture
  ok    [C12] no session row is awaiting completion
  ok    [C12] no finding is under the wording-critical quoting freeze
  WARN  [C1] src/SRC_Discord_RPW.md: 4 relative timestamp(s) outside message headers ('Yesterday at …'). Not caught by the header rule; check whether they are quoted text or unresolved captures.
  WARN  [C4] St_Francis_EMC_Distinctives.md: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby. Review manually.
  WARN  [C5] RJ_Final_Question_List.md: 17 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] RJ_Incense_Analysis.md: 9 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] St_Francis_EMC_Distinctives.md: 7 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C10] §15's newest DQ citation is 9 findings behind the ledger (DQ-28 vs DQ-37). Sweep the interval for creditable material.
  WARN  [C10] §15's newest IP citation is 7 findings behind the ledger (IP-118 vs IP-125). Sweep the interval for creditable material.
  WARN  [C10] §15's newest LS citation is 21 findings behind the ledger (LS-120 vs LS-141). Sweep the interval for creditable material.
  WARN  [C11] outline last checked against DQ-26 (260835-31); the DQ ledger now runs to DQ-37. 11 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.
  WARN  [C11] outline last checked against IP-108 (260835-32); the IP ledger now runs to IP-125. 17 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.
------------------------------------------------------------------------
COVERAGE SUMMARY — files examined per check
------------------------------------------------------------------------
  check  files  name                                         status
  C0        36  registry resolution                          OK
         └─ PROJECT_STATE.md
         └─ ORCHESTRATION.md
         └─ passes/README.md
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Tertullian_Incense_Passages.md
         └─ Brattston_Article_Assessment.md
         └─ Frere_Appendix_A_Translated.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Incense_Reply_Source_Checks.md
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ RJ_Incense_Analysis.md
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
         └─ SRC_Manifest.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Coverage_Register.md
         └─ asr_keyterms_A101.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_Assurance-raw.txt
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_SevenSacraments.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ README.md
         └─ Project_Bootstrap_Prompt.md
         └─ tools/transcribe_yt.py
         └─ validate_project.py
         └─ CLAUDE.md
  C1         5  relative timestamps in archives              OK
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_SevenSacraments.md
  C2         1  source-tag numbering                         OK
         └─ St_Francis_EMC_Distinctives.md
  C3        30  version stamps vs registry                   OK
         └─ PROJECT_STATE.md
         └─ ORCHESTRATION.md
         └─ passes/README.md
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Tertullian_Incense_Passages.md
         └─ Brattston_Article_Assessment.md
         └─ Frere_Appendix_A_Translated.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Incense_Reply_Source_Checks.md
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ RJ_Incense_Analysis.md
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
         └─ SRC_Manifest.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Coverage_Register.md
         └─ asr_keyterms_A101.md
         └─ README.md
         └─ Project_Bootstrap_Prompt.md
         └─ tools/transcribe_yt.py
         └─ validate_project.py
         └─ CLAUDE.md
  C4         3  stale answered-question status               OK
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Incense_Analysis.md
  C5        24  volatile-state duplication                   OK
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Brattston_Article_Assessment.md
         └─ CLAUDE.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Frere_Appendix_A_Translated.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Reply_Source_Checks.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ ORCHESTRATION.md
         └─ On_Incense_and_the_Altar.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Project_Bootstrap_Prompt.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ README.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Incense_Analysis.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ St_Francis_EMC_Distinctives.md
         └─ Tertullian_Incense_Passages.md
         └─ asr_keyterms_A101.md
         └─ passes/README.md
  C6         5  archive hash integrity                       OK
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_SevenSacraments.md
  C7         2  relay-clean firewall (WARN-only, suspended)  OK
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
  C8        33  dangling question-ID cross-references        OK
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Brattston_Article_Assessment.md
         └─ CLAUDE.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Frere_Appendix_A_Translated.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Reply_Source_Checks.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ ORCHESTRATION.md
         └─ On_Incense_and_the_Altar.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ PROJECT_STATE.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Project_Bootstrap_Prompt.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ README.md
         └─ RJ_Incense_Analysis.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Coverage_Register.md
         └─ SRC_Manifest.md
         └─ Tertullian_Incense_Passages.md
         └─ asr_keyterms_A101.md
         └─ passes/README.md
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_SevenSacraments.md
  C9         1  do-not-deploy consistency                    OK
         └─ RJ_Final_Question_List.md
  C10        1  section 15 staleness                         OK
         └─ St_Francis_EMC_Distinctives.md
  C11        2  outline-vs-findings drift                    OK
         └─ Incense_Conversational_Outline.md
         └─ St_Francis_EMC_Distinctives.md
  C12        2  session-registry integrity / dual capture    OK
         └─ SRC_Manifest.md
         └─ St_Francis_EMC_Distinctives.md
------------------------------------------------------------------------
103 ok · 10 warnings · 0 errors
Read the coverage summary before trusting the error count.
```

### 4b. After this pass

```
========================================================================
PROJECT INTEGRITY VALIDATION   root: /sessions/rcw-0184vrr2bp786r7j4i1iljtt/mnt/EMC/theology
========================================================================
  ok    [C0] PROJECT_STATE.md: resolved at registered path
  ok    [C0] ORCHESTRATION.md: resolved at registered path
  ok    [C0] passes/README.md: resolved at registered path
  ok    [C0] St_Francis_EMC_Distinctives.md: resolved at registered path
  ok    [C0] RJ_Final_Question_List.md: resolved at registered path
  ok    [C0] RJ_Open_Questions_and_Divergences.md: resolved at registered path
  ok    [C0] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: resolved at registered path
  ok    [C0] Protestant_Commentary_Survey_Malachi_1_11.md: resolved at registered path
  ok    [C0] Patristic_Citations_Incense_Verification.md: resolved at registered path
  ok    [C0] Tertullian_Incense_Passages.md: resolved at registered path
  ok    [C0] Brattston_Article_Assessment.md: resolved at registered path
  ok    [C0] Frere_Appendix_A_Translated.md: resolved at registered path
  ok    [C0] Orthodox_Bridge_Rebuttal_Assessment.md: resolved at registered path
  ok    [C0] Malachi_1_11_Lexical_Analysis.md: resolved at registered path
  ok    [C0] Ceremonial_Meaning_Source_Checks.md: resolved at registered path
  ok    [C0] Incense_Reply_Source_Checks.md: resolved at registered path
  ok    [C0] American_Episcopal_Reception_1899_Opinion.md: resolved at registered path
  ok    [C0] Ritualist_Case_For_Incense_and_the_1899_Opinion.md: resolved at registered path
  ok    [C0] RJ_Incense_Analysis.md: resolved at registered path
  ok    [C0] On_Incense_and_the_Altar.md: resolved at registered path
  ok    [C0] Incense_Conversational_Outline.md: resolved at registered path
  ok    [C0] Incense_Outline_Memory_Card.md: resolved at registered path
  ok    [C0] SRC_Manifest.md: resolved at registered path
  ok    [C0] SRC_Channel_Inventory.md: resolved at registered path
  ok    [C0] SRC_Coverage_Register.md: resolved at registered path
  ok    [C0] asr_keyterms_A101.md: resolved at registered path
  ok    [C0] src/SRC_Discord_RPW.md: resolved at registered path
  ok    [C0] src/SRC_Discord_Assurance.md: resolved at registered path
  ok    [C0] src/SRC_Discord_Assurance-raw.txt: resolved at registered path
  ok    [C0] src/SRC_Discord_39ArticlesFormularies.md: resolved at registered path
  ok    [C0] src/SRC_Discord_SevenSacraments.md: resolved at registered path
  ok    [C0] src/SRC_Discord_BaptismConfirmation.md: resolved at registered path
  ok    [C0] README.md: resolved at registered path
  ok    [C0] Project_Bootstrap_Prompt.md: resolved at registered path
  ok    [C0] tools/transcribe_yt.py: resolved at registered path
  ok    [C0] validate_project.py: resolved at registered path
  ok    [C0] CLAUDE.md: resolved at registered path
  ok    [C1] src/SRC_Discord_39ArticlesFormularies.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_Assurance.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_BaptismConfirmation.md: no unresolved relative timestamps
  ok    [C1] src/SRC_Discord_SevenSacraments.md: no unresolved relative timestamps
  ok    [C2] DQ-1..37 unbroken, no duplicates
  ok    [C2] IP-1..125 unbroken, no duplicates
  ok    [C2] RV-1..63 unbroken, no duplicates
  ok    [C2] LS-1..141 unbroken, no duplicates
  ok    [C2] BLOG-1..158 unbroken, no duplicates
  ok    [C2] POD-1..16 unbroken, no duplicates
  ok    [C3] PROJECT_STATE.md: version agrees with registry (260835-73)
  ok    [C3] ORCHESTRATION.md: version agrees with registry (260835-37)
  ok    [C3] passes/README.md: version agrees with registry (260832-3)
  ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260835-72)
  ok    [C3] RJ_Final_Question_List.md: version agrees with registry (260835-72 (v23))
  ok    [C3] RJ_Open_Questions_and_Divergences.md: version agrees with registry (260833-2)
  ok    [C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: version agrees with registry (260832-2)
  ok    [C3] Protestant_Commentary_Survey_Malachi_1_11.md: version agrees with registry (260835-45)
  ok    [C3] Patristic_Citations_Incense_Verification.md: version agrees with registry (260835-47)
  ok    [C3] Tertullian_Incense_Passages.md: version agrees with registry (260835-48)
  ok    [C3] Brattston_Article_Assessment.md: version agrees with registry (260835-49)
  ok    [C3] Frere_Appendix_A_Translated.md: version agrees with registry (260835-50)
  ok    [C3] Orthodox_Bridge_Rebuttal_Assessment.md: version agrees with registry (260835-51)
  ok    [C3] Malachi_1_11_Lexical_Analysis.md: version agrees with registry (260835-52)
  ok    [C3] Ceremonial_Meaning_Source_Checks.md: version agrees with registry (260835-56)
  ok    [C3] Incense_Reply_Source_Checks.md: version agrees with registry (260835-65)
  ok    [C3] American_Episcopal_Reception_1899_Opinion.md: version agrees with registry (260835-55)
  ok    [C3] Ritualist_Case_For_Incense_and_the_1899_Opinion.md: version agrees with registry (260835-39)
  ok    [C3] RJ_Incense_Analysis.md: version agrees with registry (260835-65)
  ok    [C3] On_Incense_and_the_Altar.md: version agrees with registry (260833-2)
  ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260835-72)
  ok    [C3] Incense_Outline_Memory_Card.md: version agrees with registry (260835-73)
  ok    [C3] SRC_Manifest.md: version agrees with registry (260835-72)
  ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260835-72)
  ok    [C3] SRC_Coverage_Register.md: version agrees with registry (260835-72)
  ok    [C3] asr_keyterms_A101.md: version agrees with registry (260830-2)
  ok    [C3] README.md: version agrees with registry (260835-8)
  ok    [C3] Project_Bootstrap_Prompt.md: version agrees with registry (260816-1)
  ok    [C3] tools/transcribe_yt.py: version agrees with registry (260833-7)
  ok    [C3] validate_project.py: version agrees with registry (260835-39)
  ok    [C3] CLAUDE.md: version agrees with registry (260835-72)
  ok    [C4] RJ_Final_Question_List.md: no unmarked stale-status passages for answered questions
  ok    [C4] RJ_Incense_Analysis.md: no unmarked stale-status passages for answered questions
  ok    [C5] total volatile-state assertions outside PROJECT_STATE: 34
  ok    [C6] src/SRC_Discord_39ArticlesFormularies.md: hash matches manifest
  ok    [C6] src/SRC_Discord_Assurance.md: hash matches manifest
  ok    [C6] src/SRC_Discord_BaptismConfirmation.md: hash matches manifest
  ok    [C6] src/SRC_Discord_RPW.md: hash matches manifest
  ok    [C6] src/SRC_Discord_SevenSacraments.md: hash matches manifest
  ok    [C7] On_Incense_and_the_Altar.md: relay-clean firewall intact (class suspended; no cleanup owed)
  ok    [C7] Incense_Conversational_Outline.md: relay-clean firewall intact (class suspended; no cleanup owed)
  ok    [C8] all 4 QA-* citations resolve in the question list
  ok    [C8] all 7 VP- label(s) defined in the distinctives; 7 cited, none dangling
  ok    [C9] item 7: carries a retirement marker, consistent with the register
  ok    [C9] item 20: carries a retirement marker, consistent with the register
  ok    [C9] item 14: carries a retirement marker, consistent with the register
  ok    [C9] item 9: carries a retirement marker, consistent with the register
  ok    [C10] every finding flagged as common ground is credited in §15
  ok    [C10] §15 is within 1 finding(s) of the RV ledger head (RV-63)
  ok    [C10] §15 is within 0 finding(s) of the BLOG ledger head (BLOG-158)
  ok    [C10] §15 is within 0 finding(s) of the POD ledger head (POD-16)
  ok    [C11] RV current in the outline pointer (RV-63 @ 260830-1, ledger at RV-63)
  ok    [C12] session registry parsed: 77 capture row(s) across 66 session(s)
  ok    [C12] 27 standalone recording row(s) parsed and correctly EXCLUDED from the session count (manifest rule: a standalone recording gets no session row)
  ok    [C12] no capture is stuck in SECONDARY -- SWEEP PENDING
  ok    [C12] retrofit rule present: bare pre-260725 offsets resolve to their session's PRIMARY capture
  ok    [C12] no session row is awaiting completion
  ok    [C12] no finding is under the wording-critical quoting freeze
  WARN  [C1] src/SRC_Discord_RPW.md: 4 relative timestamp(s) outside message headers ('Yesterday at …'). Not caught by the header rule; check whether they are quoted text or unresolved captures.
  WARN  [C4] St_Francis_EMC_Distinctives.md: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby. Review manually.
  WARN  [C5] RJ_Final_Question_List.md: 17 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] RJ_Incense_Analysis.md: 9 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] St_Francis_EMC_Distinctives.md: 7 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C10] §15's newest DQ citation is 9 findings behind the ledger (DQ-28 vs DQ-37). Sweep the interval for creditable material.
  WARN  [C10] §15's newest IP citation is 7 findings behind the ledger (IP-118 vs IP-125). Sweep the interval for creditable material.
  WARN  [C10] §15's newest LS citation is 21 findings behind the ledger (LS-120 vs LS-141). Sweep the interval for creditable material.
  WARN  [C11] outline last checked against DQ-26 (260835-31); the DQ ledger now runs to DQ-37. 11 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.
  WARN  [C11] outline last checked against IP-108 (260835-32); the IP ledger now runs to IP-125. 17 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.
------------------------------------------------------------------------
COVERAGE SUMMARY — files examined per check
------------------------------------------------------------------------
  check  files  name                                         status
  C0        37  registry resolution                          OK
         └─ PROJECT_STATE.md
         └─ ORCHESTRATION.md
         └─ passes/README.md
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Tertullian_Incense_Passages.md
         └─ Brattston_Article_Assessment.md
         └─ Frere_Appendix_A_Translated.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Incense_Reply_Source_Checks.md
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ RJ_Incense_Analysis.md
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Outline_Memory_Card.md
         └─ SRC_Manifest.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Coverage_Register.md
         └─ asr_keyterms_A101.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_Assurance-raw.txt
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_SevenSacraments.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ README.md
         └─ Project_Bootstrap_Prompt.md
         └─ tools/transcribe_yt.py
         └─ validate_project.py
         └─ CLAUDE.md
  C1         5  relative timestamps in archives              OK
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_SevenSacraments.md
  C2         1  source-tag numbering                         OK
         └─ St_Francis_EMC_Distinctives.md
  C3        31  version stamps vs registry                   OK
         └─ PROJECT_STATE.md
         └─ ORCHESTRATION.md
         └─ passes/README.md
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Tertullian_Incense_Passages.md
         └─ Brattston_Article_Assessment.md
         └─ Frere_Appendix_A_Translated.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Incense_Reply_Source_Checks.md
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ RJ_Incense_Analysis.md
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Outline_Memory_Card.md
         └─ SRC_Manifest.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Coverage_Register.md
         └─ asr_keyterms_A101.md
         └─ README.md
         └─ Project_Bootstrap_Prompt.md
         └─ tools/transcribe_yt.py
         └─ validate_project.py
         └─ CLAUDE.md
  C4         3  stale answered-question status               OK
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Incense_Analysis.md
  C5        25  volatile-state duplication                   OK
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Brattston_Article_Assessment.md
         └─ CLAUDE.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Frere_Appendix_A_Translated.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Outline_Memory_Card.md
         └─ Incense_Reply_Source_Checks.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ ORCHESTRATION.md
         └─ On_Incense_and_the_Altar.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Project_Bootstrap_Prompt.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ README.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Incense_Analysis.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ St_Francis_EMC_Distinctives.md
         └─ Tertullian_Incense_Passages.md
         └─ asr_keyterms_A101.md
         └─ passes/README.md
  C6         5  archive hash integrity                       OK
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_SevenSacraments.md
  C7         2  relay-clean firewall (WARN-only, suspended)  OK
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
  C8        34  dangling question-ID cross-references        OK
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ American_Episcopal_Reception_1899_Opinion.md
         └─ Brattston_Article_Assessment.md
         └─ CLAUDE.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Ceremonial_Meaning_Source_Checks.md
         └─ Frere_Appendix_A_Translated.md
         └─ Incense_Conversational_Outline.md
         └─ Incense_Outline_Memory_Card.md
         └─ Incense_Reply_Source_Checks.md
         └─ Malachi_1_11_Lexical_Analysis.md
         └─ ORCHESTRATION.md
         └─ On_Incense_and_the_Altar.md
         └─ Orthodox_Bridge_Rebuttal_Assessment.md
         └─ PROJECT_STATE.md
         └─ Patristic_Citations_Incense_Verification.md
         └─ Project_Bootstrap_Prompt.md
         └─ Protestant_Commentary_Survey_Malachi_1_11.md
         └─ README.md
         └─ RJ_Incense_Analysis.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Ritualist_Case_For_Incense_and_the_1899_Opinion.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Coverage_Register.md
         └─ SRC_Manifest.md
         └─ Tertullian_Incense_Passages.md
         └─ asr_keyterms_A101.md
         └─ passes/README.md
         └─ src/SRC_Discord_39ArticlesFormularies.md
         └─ src/SRC_Discord_Assurance.md
         └─ src/SRC_Discord_BaptismConfirmation.md
         └─ src/SRC_Discord_RPW.md
         └─ src/SRC_Discord_SevenSacraments.md
  C9         1  do-not-deploy consistency                    OK
         └─ RJ_Final_Question_List.md
  C10        1  section 15 staleness                         OK
         └─ St_Francis_EMC_Distinctives.md
  C11        2  outline-vs-findings drift                    OK
         └─ Incense_Conversational_Outline.md
         └─ St_Francis_EMC_Distinctives.md
  C12        2  session-registry integrity / dual capture    OK
         └─ SRC_Manifest.md
         └─ St_Francis_EMC_Distinctives.md
------------------------------------------------------------------------
105 ok · 10 warnings · 0 errors
Read the coverage summary before trusting the error count.
```

### 4c. Check codes, each with its full title, and the change from baseline

- **C0, registry resolution:** OK. Files examined went from 36 to **37** (+`Incense_Outline_Memory_Card.md`), and a new `ok` line reads "resolved at registered path."
- **C1, relative timestamps in archives:** OK. 5 files, no change. The same WARN on `src/SRC_Discord_RPW.md` (4 relative timestamps) is pre-existing.
- **C2, source-tag numbering:** OK. 1 file, no change.
- **C3, version stamps vs registry:** OK. Files examined went from 30 to **31**. `PROJECT_STATE.md` now agrees at `260835-73`, and a new `ok` line for the card agrees at `260835-73`.
- **C4, stale answered-question status:** OK. 3 files, no change. The WARN on `St_Francis_EMC_Distinctives.md` is pre-existing.
- **C5, volatile-state duplication:** OK. Files examined went from 24 to **25** (the card). The card contributes **0** volatile-state assertions by design: it has no "STATUS:" lines, and the total is unchanged at 34. The three WARNs are pre-existing.
- **C6, archive hash integrity:** OK. 5 files, no change.
- **C7, relay-clean firewall (WARN-only, suspended):** OK. 2 files, no change. The card is not in C7's scope, and its INTERNAL class says it is not relay-clean.
- **C8, dangling question-ID cross-references:** OK. Files examined went from 33 to **34** (the card). The card cites no labels of the kinds C8 checks.
- **C9, do-not-deploy consistency:** OK. 1 file, no change.
- **C10, section 15 staleness:** OK. 1 file, no change. The three WARNs (`DQ`, `IP`, `LS` lags) are pre-existing.
- **C11, outline-vs-findings drift:** OK. 2 files, no change. Both WARNs (11 `DQ`, 17 `IP` unreviewed) are pre-existing and accurate. This pass does not review the outline and moves no `CHECKED-AGAINST` value.
- **C12, session-registry integrity / dual capture:** OK. 2 files, no change.

**Summary:** the baseline was `103 ok · 10 warnings · 0 errors`, and the after run is `105 ok · 10 warnings · 0 errors`. The +2 `ok` lines are the card's C0 and C3 lines. The warning set is identical line for line. Nothing was suppressed, and the validator asked for nothing beyond the registry row.

⚠️ **Gap, recorded and not fixed:** no validator check compares the card against the outline, so the card can go stale silently. The §4 row and the card's derivation pointer both say to re-derive the card whenever the outline's stamp moves.

## 5. Rendering result

`which mmdc` returned nothing (exit 1), so **mermaid-cli is not installed.** Per the brief, nothing was installed and no PNG or SVG was produced. The Mermaid source is in the card at Layer C, where GitHub and VS Code render it. ⚠️ **The chart has not been machine-validated**, because no renderer was available and installing one was out of scope. It was written to conservative syntax (quoted labels, no semicolons or dashes in labels, subgraph IDs without spaces), and it has 33 nodes: 15 steps, 12 decision diamonds, 3 outcome nodes and 3 question nodes.

## 6. Not done, and why

- **The PNG and SVG render** were not produced because `mmdc` is absent and installs are barred.
- **A print test** of Layer A's one-page fit was not run. Layer A is about 805 words in an 18-row table (17 steps plus the core), which is estimated to fit one page at a normal print size. To keep it on one page, the guards that must travel visibly were moved to a "Standing guards" strip directly after Layer A, and every row's State cell still carries its own SPENT, RESERVE or DO NOT DEPLOY marking.
- **The spoken core** was not reworded, because it is JD's text. One discrepancy is flagged beneath it, not edited: its closing "the incense is the prayers of the saints" differs from reserve item 12's grammar ("the bowls full of incense are the prayers"). The 60-second compression uses the item-12 grammar.
- **The `IP-101` pedagogy warrant** is still met by no step. It is carried on the card as "the one hole," and no answering step was drafted (`260726-1` rule).
- **The reserve Heb 9 question** is given in register form only. It was not drafted as posted text, because it is queued behind the two open questions.
- **Nothing was posted. No commit and no `git add`.**

## 7. Diff and copies

- `~/EMC/staging-73/260835-73.diff` holds the full `git diff` (the `PROJECT_STATE.md` changes; 114,588 B, because the edited §4 cell is one very long line).
- `~/EMC/staging-73/Incense_Outline_Memory_Card.md` is a copy of the new untracked card, since `git diff` does not show it.
- `~/EMC/staging-73/validator_baseline.txt` and `validator_after.txt` are the raw validator outputs.

`git status --short` after the pass:
```
 M PROJECT_STATE.md
?? Incense_Outline_Memory_Card.md
```
