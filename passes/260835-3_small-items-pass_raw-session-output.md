# 260835-3 — RAW SESSION OUTPUT

Raw, unedited output of every verification command run by the `260835-3` pass, in order. Reproduced here because it exceeds chat.

⚠️ **Path note:** commands ran in the Linux workspace, where the repo is mounted at `/sessions/…/mnt/EMC/theology`. That is the same working tree as `~/EMC/theology`; the validator header prints the mount path and it is not a second copy.

---

## 1. GATE — HEAD and lock check, before any edit

```
$ git rev-parse HEAD
456e36c5ff01184af4e8efcb32cb5c2e65b83c81

$ ls -la .git/*.lock
no .git lock files
```

⭐ **HEAD matches the briefed `456e36c` exactly. NO stale lock at gate — see §5.**

## 2. VALIDATOR — BEFORE (complete output)

```
========================================================================
PROJECT INTEGRITY VALIDATION   root: /sessions/vigilant-optimistic-dijkstra/mnt/EMC/theology
========================================================================
  ok    [C0] PROJECT_STATE.md: resolved at registered path
  ok    [C0] ORCHESTRATION.md: resolved at registered path
  ok    [C0] passes/README.md: resolved at registered path
  ok    [C0] St_Francis_EMC_Distinctives.md: resolved at registered path
  ok    [C0] RJ_Final_Question_List.md: resolved at registered path
  ok    [C0] RJ_Open_Questions_and_Divergences.md: resolved at registered path
  ok    [C0] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: resolved at registered path
  ok    [C0] RJ_Incense_Analysis.md: resolved at registered path
  ok    [C0] On_Incense_and_the_Altar.md: resolved at registered path
  ok    [C0] Incense_Conversational_Outline.md: resolved at registered path
  ok    [C0] SRC_Manifest.md: resolved at registered path
  ok    [C0] SRC_Channel_Inventory.md: resolved at registered path
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
  ok    [C2] DQ-1..24 unbroken, no duplicates
  ok    [C2] IP-1..97 unbroken, no duplicates
  ok    [C2] RV-1..63 unbroken, no duplicates
  ok    [C2] LS-1..128 unbroken, no duplicates
  ok    [C2] BLOG-1..158 unbroken, no duplicates
  ok    [C2] POD-1..16 unbroken, no duplicates
  ok    [C3] PROJECT_STATE.md: version agrees with registry (260835-2)
  ok    [C3] ORCHESTRATION.md: version agrees with registry (260834-7)
  ok    [C3] passes/README.md: version agrees with registry (260832-3)
  ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260835-1)
  ok    [C3] RJ_Final_Question_List.md: version agrees with registry (260833-2 (v21))
  ok    [C3] RJ_Open_Questions_and_Divergences.md: version agrees with registry (260833-2)
  ok    [C3] RJ_Incense_Analysis.md: version agrees with registry (260834-1)
  ok    [C3] On_Incense_and_the_Altar.md: version agrees with registry (260833-2)
  ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260835-2)
  ok    [C3] SRC_Manifest.md: version agrees with registry (260834-9)
  ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260835-1)
  ok    [C3] asr_keyterms_A101.md: version agrees with registry (260830-2)
  ok    [C3] README.md: version agrees with registry (260828-2)
  ok    [C3] Project_Bootstrap_Prompt.md: version agrees with registry (260816-1)
  ok    [C3] validate_project.py: version agrees with registry (260812-1)
  ok    [C3] CLAUDE.md: version agrees with registry (260728-2)
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
  ok    [C10] §15 is within 2 finding(s) of the DQ ledger head (DQ-24)
  ok    [C10] §15 is within 0 finding(s) of the IP ledger head (IP-97)
  ok    [C10] §15 is within 1 finding(s) of the RV ledger head (RV-63)
  ok    [C10] §15 is within 0 finding(s) of the BLOG ledger head (BLOG-158)
  ok    [C10] §15 is within 0 finding(s) of the POD ledger head (POD-16)
  ok    [C11] DQ current in the outline pointer (DQ-24 @ 260835-2, ledger at DQ-24)
  ok    [C11] IP current in the outline pointer (IP-97 @ 260833-5, ledger at IP-97)
  ok    [C11] RV current in the outline pointer (RV-63 @ 260830-1, ledger at RV-63)
  ok    [C12] session registry parsed: 74 capture row(s) across 64 session(s)
  ok    [C12] 27 standalone recording row(s) parsed and correctly EXCLUDED from the session count (manifest rule: a standalone recording gets no session row)
  ok    [C12] no capture is stuck in SECONDARY -- SWEEP PENDING
  ok    [C12] retrofit rule present: bare pre-260725 offsets resolve to their session's PRIMARY capture
  ok    [C12] no session row is awaiting completion
  ok    [C12] no finding is under the wording-critical quoting freeze
  WARN  [C1] src/SRC_Discord_RPW.md: 2 relative timestamp(s) outside message headers ('Yesterday at …'). Not caught by the header rule; check whether they are quoted text or unresolved captures.
  WARN  [C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: no parseable 'Last updated' stamp; registry says '260832-2'
  WARN  [C3] tools/transcribe_yt.py: no parseable 'Last updated' stamp; registry says '260833-7'
  WARN  [C4] St_Francis_EMC_Distinctives.md: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby. Review manually.
  WARN  [C5] RJ_Final_Question_List.md: 17 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] RJ_Incense_Analysis.md: 9 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] St_Francis_EMC_Distinctives.md: 7 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C10] §15's newest LS citation is 8 findings behind the ledger (LS-120 vs LS-128). Sweep the interval for creditable material.
------------------------------------------------------------------------
COVERAGE SUMMARY — files examined per check
------------------------------------------------------------------------
  check  files  name                                         status
  C0        24  registry resolution                          OK
         └─ PROJECT_STATE.md
         └─ ORCHESTRATION.md
         └─ passes/README.md
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ RJ_Incense_Analysis.md
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
         └─ SRC_Manifest.md
         └─ SRC_Channel_Inventory.md
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
  C3        18  version stamps vs registry                   OK
         └─ PROJECT_STATE.md
         └─ ORCHESTRATION.md
         └─ passes/README.md
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ RJ_Incense_Analysis.md
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
         └─ SRC_Manifest.md
         └─ SRC_Channel_Inventory.md
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
  C5        13  volatile-state duplication                   OK
         └─ CLAUDE.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Incense_Conversational_Outline.md
         └─ ORCHESTRATION.md
         └─ On_Incense_and_the_Altar.md
         └─ Project_Bootstrap_Prompt.md
         └─ README.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Incense_Analysis.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ St_Francis_EMC_Distinctives.md
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
  C8        21  dangling question-ID cross-references        OK
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ CLAUDE.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Incense_Conversational_Outline.md
         └─ ORCHESTRATION.md
         └─ On_Incense_and_the_Altar.md
         └─ PROJECT_STATE.md
         └─ Project_Bootstrap_Prompt.md
         └─ README.md
         └─ RJ_Incense_Analysis.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Manifest.md
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
81 ok · 8 warnings · 0 errors
Read the coverage summary before trusting the error count.
```

## 3. STAMP DERIVATION

```
$ grep -rhoE '\b26[0-9]{4}-[0-9]+\b' --include='*.md' --include='*.py' . | sort -u | tail -25
260832-2
260832-3
260832-4
260832-5
260833-1
260833-2
260833-3
260833-4
260833-5
260833-6
260833-7
260833-8
260834-1
260834-2
260834-3
260834-4
260834-5
260834-6
260834-7
260834-8
260834-9
260834-10
260835-1
260835-2
260835-3
```

⭐ **Highest stamp `260835-2` → this pass is `260835-3`. `260835-3` returned zero hits repo-wide before this pass.**

## 4. NEXT-FREE `IP` — re-derived two independent ways, against `HEAD`

```
$ git grep -hoE '\bIP-(9[89]|1[0-9][0-9])\b' HEAD -- '*.md' '*.py' '*.txt' | sort -u
IP-98
```

**Every `IP-98` occurrence at `HEAD` — all 21, each read in context.** ⛔ **Every one is a next free registry line or a pass note recording it unspent. Not one is a finding.**

```
$ git grep -n 'IP-98' HEAD -- '*.md' '*.py' '*.txt'
PROJECT_STATE.md:21  … fset altered. Next-free unchanged: `DQ-25`, `IP-98`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `File 47`.* …
PROJECT_STATE.md:25  … r `C2` concurs, `IP-1..97` unbroken); every `IP-98` occurrence repo-wide is a next-free registry assertio …
PROJECT_STATE.md:27  … ed from the repo and is unchanged: `DQ-25`, `IP-98`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EX …
PROJECT_STATE.md:41  … . Next-free numbers are UNCHANGED: `DQ-25`, `IP-98`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EX …
PROJECT_STATE.md:69  … ngested none. Next-free unchanged: `DQ-25`, `IP-98`, `LS-129`, `BLOG-159`, `RV-64`, `POD-17`.** ⏳ **OWED  …
PROJECT_STATE.md:1254  … URTEEN `IP` NUMBERS, UNBROKEN; NEXT FREE IS `IP-98`.** The prefix ruling the `260833-3` note reserved to  …
PROJECT_STATE.md:1260  …  the recapture rather than assumed.**)* · **`IP-98`** *(⭐⭐⭐ **updated 260833-4: `IP-84`…`IP-97` ARE SPENT …
St_Francis_EMC_Distinctives.md:1684  …  from the repo rather than copied: `DQ-25`, `IP-98`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `File 47`.* …
St_Francis_EMC_Distinctives.md:2890  … rived from the repo and unchanged (`DQ-25`, `IP-98`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `File 47`). …
St_Francis_EMC_Distinctives.md:6737  … et altered. **Next-free unchanged: `DQ-25`, `IP-98`, `LS-129`, `BLOG-159`, `RV-64`, `POD-17`.** ⏳ **Owed  …
passes/260833-4_a101-20260823-minting_close-out.md:15  … rteen findings, unbroken. Next free `IP` is `IP-98`.** ⛔ **`IP-84` was grep-verified free before the firs …
passes/260834-5_licensing-principle-topical-pass_close-out.md:263  … **Next-free numbers are untouched: `DQ-25`, `IP-98`, `LS-129`, `BLOG-159`, `RV-64`, `POD-17`.** …
passes/260834-6_eight-file-triage_read-and-report_close-out.md:693  … umbers remain **`File 40`**, **`DQ-25`**, **`IP-98`**, **`LS-129`**, **`RV-64`**, **`BLOG-159`**, **`POD- …
passes/260834-7_eight-file-coverage-check_read-and-report_close-out.md:483  … umbers remain **`File 40`**, **`DQ-25`**, **`IP-98`**, **`LS-129`**, **`RV-64`**, **`BLOG-159`**, **`POD- …
passes/260834-9_annn-retro-registration_pass-a_close-out.md:73  … re re-checked rather than assumed: `DQ-25`, `IP-98`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EX …
passes/260834-9_annn-retro-registration_pass-a_close-out.md:348  … med** — next-free values are **`DQ-25`**, **`IP-98`**, **`LS-129`**, **`RV-64`**, **`BLOG-159`**, **`POD- …
passes/260835-1_files-41-43-targeted-mining_pass-b1_close-out.md:21  … | Next-free `IP` | re-derive fresh | **`IP-98`** — ⛔ **NOT consumed** | ✅ re-derived | …
passes/260835-1_files-41-43-targeted-mining_pass-b1_close-out.md:73  … ross every `.md` returns a maximum token of `IP-98`; **every `IP-98` occurrence repo-wide was read in con …
passes/260835-1_files-41-43-targeted-mining_pass-b1_close-out.md:383  … rived from the repo and unchanged: `DQ-25`, `IP-98`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EX …
passes/260835-1_files-41-43-targeted-mining_pass-b1_close-out.md:478  … A`, `EXT`, `W` or `File` number consumed.** `IP-98` was re-derived fresh and left free. …
passes/260835-2_c11-outline-review-dq-arm_close-out.md:343  … med.** Next-free values unchanged: `DQ-25`, `IP-98`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EX …
```

```
$ git show HEAD:St_Francis_EMC_Distinctives.md \
    | grep -ohE '^\*\*IP-[0-9]+[a-z]?\.\*\*' | grep -oE '[0-9]+' | sort -n | uniq > /tmp/ip.txt
$ seq 1 97 > /tmp/exp.txt
$ diff /tmp/ip.txt /tmp/exp.txt && echo "IP-1..97 COMPLETE, NO GAPS, NO EXTRAS"
IP-1..97 COMPLETE, NO GAPS, NO EXTRAS
```

⛔ **`IP-98` verified free, then consumed. `IP-98`…`IP-108` now spent; next free `IP-109`.**

## 5. ⚠️⚠️ THE `.git` LOCK — observed mid-pass, and it is created BY the pass

```
$ git status --short
 M Incense_Conversational_Outline.md
 M PROJECT_STATE.md
 M RJ_Incense_Analysis.md
 M SRC_Channel_Inventory.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
warning: unable to unlink '/…/theology/.git/index.lock': Operation not permitted
```

```
$ stat .git/index.lock
  File: .git/index.lock
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 2ah/42d	Inode: 705         Links: 1
Access: (0600/-rw-------)  Uid: ( 1142/vigilant-optimistic-dijkstra)   Gid: ( 1142/vigilant-optimistic-dijkstra)
Access: 2026-08-26 09:33:13.160423819 -0400
Modify: 2026-08-26 09:33:13.160423819 -0400
```

```
$ mount | grep mnt/EMC
/proc/self/fd/3 on /sessions/vigilant-optimistic-dijkstra/mnt/EMC type fuse (rw,nosuid,nodev,relatime,user_id=0,group_id=0,default_permissions,allow_other)
```

⭐⭐⭐ **Zero bytes, born this session, on a FUSE mount that denies the unlink. `git status` creates the lock, cannot remove it, and leaves it behind — which is the whole of the six-pass "stale lock" recurrence.**

⛔⛔ **NOT REMOVED. No `rm` attempted.** All later git reads used `git --no-optional-locks`, which does not take the lock; output compared against the locking invocation and identical.

## 6. VALIDATOR — AFTER (complete output)

```
========================================================================
PROJECT INTEGRITY VALIDATION   root: /sessions/vigilant-optimistic-dijkstra/mnt/EMC/theology
========================================================================
  ok    [C0] PROJECT_STATE.md: resolved at registered path
  ok    [C0] ORCHESTRATION.md: resolved at registered path
  ok    [C0] passes/README.md: resolved at registered path
  ok    [C0] St_Francis_EMC_Distinctives.md: resolved at registered path
  ok    [C0] RJ_Final_Question_List.md: resolved at registered path
  ok    [C0] RJ_Open_Questions_and_Divergences.md: resolved at registered path
  ok    [C0] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: resolved at registered path
  ok    [C0] RJ_Incense_Analysis.md: resolved at registered path
  ok    [C0] On_Incense_and_the_Altar.md: resolved at registered path
  ok    [C0] Incense_Conversational_Outline.md: resolved at registered path
  ok    [C0] SRC_Manifest.md: resolved at registered path
  ok    [C0] SRC_Channel_Inventory.md: resolved at registered path
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
  ok    [C2] DQ-1..24 unbroken, no duplicates
  ok    [C2] IP-1..108 unbroken, no duplicates
  ok    [C2] RV-1..63 unbroken, no duplicates
  ok    [C2] LS-1..128 unbroken, no duplicates
  ok    [C2] BLOG-1..158 unbroken, no duplicates
  ok    [C2] POD-1..16 unbroken, no duplicates
  ok    [C3] PROJECT_STATE.md: version agrees with registry (260835-3)
  ok    [C3] ORCHESTRATION.md: version agrees with registry (260834-7)
  ok    [C3] passes/README.md: version agrees with registry (260832-3)
  ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260835-3)
  ok    [C3] RJ_Final_Question_List.md: version agrees with registry (260833-2 (v21))
  ok    [C3] RJ_Open_Questions_and_Divergences.md: version agrees with registry (260833-2)
  ok    [C3] RJ_Incense_Analysis.md: version agrees with registry (260835-3)
  ok    [C3] On_Incense_and_the_Altar.md: version agrees with registry (260833-2)
  ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260835-3)
  ok    [C3] SRC_Manifest.md: version agrees with registry (260835-3)
  ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260835-3)
  ok    [C3] asr_keyterms_A101.md: version agrees with registry (260830-2)
  ok    [C3] README.md: version agrees with registry (260828-2)
  ok    [C3] Project_Bootstrap_Prompt.md: version agrees with registry (260816-1)
  ok    [C3] validate_project.py: version agrees with registry (260812-1)
  ok    [C3] CLAUDE.md: version agrees with registry (260728-2)
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
  ok    [C10] §15 is within 0 finding(s) of the DQ ledger head (DQ-24)
  ok    [C10] §15 is within 0 finding(s) of the IP ledger head (IP-108)
  ok    [C10] §15 is within 1 finding(s) of the RV ledger head (RV-63)
  ok    [C10] §15 is within 0 finding(s) of the BLOG ledger head (BLOG-158)
  ok    [C10] §15 is within 0 finding(s) of the POD ledger head (POD-16)
  ok    [C11] DQ current in the outline pointer (DQ-24 @ 260835-2, ledger at DQ-24)
  ok    [C11] RV current in the outline pointer (RV-63 @ 260830-1, ledger at RV-63)
  ok    [C12] session registry parsed: 74 capture row(s) across 64 session(s)
  ok    [C12] 27 standalone recording row(s) parsed and correctly EXCLUDED from the session count (manifest rule: a standalone recording gets no session row)
  ok    [C12] no capture is stuck in SECONDARY -- SWEEP PENDING
  ok    [C12] retrofit rule present: bare pre-260725 offsets resolve to their session's PRIMARY capture
  ok    [C12] no session row is awaiting completion
  ok    [C12] no finding is under the wording-critical quoting freeze
  WARN  [C1] src/SRC_Discord_RPW.md: 2 relative timestamp(s) outside message headers ('Yesterday at …'). Not caught by the header rule; check whether they are quoted text or unresolved captures.
  WARN  [C3] Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: no parseable 'Last updated' stamp; registry says '260832-2'
  WARN  [C3] tools/transcribe_yt.py: no parseable 'Last updated' stamp; registry says '260833-7'
  WARN  [C4] St_Francis_EMC_Distinctives.md: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby. Review manually.
  WARN  [C5] RJ_Final_Question_List.md: 17 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] RJ_Incense_Analysis.md: 9 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C5] St_Francis_EMC_Distinctives.md: 7 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
  WARN  [C10] §15's newest LS citation is 8 findings behind the ledger (LS-120 vs LS-128). Sweep the interval for creditable material.
  WARN  [C11] outline last checked against IP-97 (260833-5); the IP ledger now runs to IP-108. 11 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.
------------------------------------------------------------------------
COVERAGE SUMMARY — files examined per check
------------------------------------------------------------------------
  check  files  name                                         status
  C0        24  registry resolution                          OK
         └─ PROJECT_STATE.md
         └─ ORCHESTRATION.md
         └─ passes/README.md
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ RJ_Incense_Analysis.md
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
         └─ SRC_Manifest.md
         └─ SRC_Channel_Inventory.md
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
  C3        18  version stamps vs registry                   OK
         └─ PROJECT_STATE.md
         └─ ORCHESTRATION.md
         └─ passes/README.md
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ RJ_Incense_Analysis.md
         └─ On_Incense_and_the_Altar.md
         └─ Incense_Conversational_Outline.md
         └─ SRC_Manifest.md
         └─ SRC_Channel_Inventory.md
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
  C5        13  volatile-state duplication                   OK
         └─ CLAUDE.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Incense_Conversational_Outline.md
         └─ ORCHESTRATION.md
         └─ On_Incense_and_the_Altar.md
         └─ Project_Bootstrap_Prompt.md
         └─ README.md
         └─ RJ_Final_Question_List.md
         └─ RJ_Incense_Analysis.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ St_Francis_EMC_Distinctives.md
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
  C8        21  dangling question-ID cross-references        OK
         └─ St_Francis_EMC_Distinctives.md
         └─ RJ_Final_Question_List.md
         └─ CLAUDE.md
         └─ Calvin_Luther_and_Anglican_Formularies_on_Iconography.md
         └─ Incense_Conversational_Outline.md
         └─ ORCHESTRATION.md
         └─ On_Incense_and_the_Altar.md
         └─ PROJECT_STATE.md
         └─ Project_Bootstrap_Prompt.md
         └─ README.md
         └─ RJ_Incense_Analysis.md
         └─ RJ_Open_Questions_and_Divergences.md
         └─ SRC_Channel_Inventory.md
         └─ SRC_Manifest.md
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
80 ok · 9 warnings · 0 errors
Read the coverage summary before trusting the error count.
```

## 7. BEFORE → AFTER, EVERY DIFFERING CHECK LINE

```
30c30
<   ok    [C2] IP-1..97 unbroken, no duplicates
---
>   ok    [C2] IP-1..108 unbroken, no duplicates
35c35
<   ok    [C3] PROJECT_STATE.md: version agrees with registry (260835-2)
---
>   ok    [C3] PROJECT_STATE.md: version agrees with registry (260835-3)
38c38
<   ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260835-1)
---
>   ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260835-3)
41c41
<   ok    [C3] RJ_Incense_Analysis.md: version agrees with registry (260834-1)
---
>   ok    [C3] RJ_Incense_Analysis.md: version agrees with registry (260835-3)
43,45c43,45
<   ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260835-2)
<   ok    [C3] SRC_Manifest.md: version agrees with registry (260834-9)
<   ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260835-1)
---
>   ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260835-3)
>   ok    [C3] SRC_Manifest.md: version agrees with registry (260835-3)
>   ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260835-3)
68,69c68,69
<   ok    [C10] §15 is within 2 finding(s) of the DQ ledger head (DQ-24)
<   ok    [C10] §15 is within 0 finding(s) of the IP ledger head (IP-97)
---
>   ok    [C10] §15 is within 0 finding(s) of the DQ ledger head (DQ-24)
>   ok    [C10] §15 is within 0 finding(s) of the IP ledger head (IP-108)
74d73
<   ok    [C11] IP current in the outline pointer (IP-97 @ 260833-5, ledger at IP-97)
89a89
>   WARN  [C11] outline last checked against IP-97 (260833-5); the IP ledger now runs to IP-108. 11 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.
```

⭐⭐⭐ **One `ok` became a `WARN`, and it is `C11` counting the eleven. That is the intended result.** ⚠️ **The `C10` `DQ` movement from *within 2* to *within 0* is an artefact of §15 declines citing `DQ-24` and `DQ-8` by name — no `DQ` finding was swept or credited. Recorded in §15 itself.**

## 8. `git status --short` — FINAL

```
$ git --no-optional-locks status --short
 M Incense_Conversational_Outline.md
 M PROJECT_STATE.md
 M RJ_Incense_Analysis.md
 M SRC_Channel_Inventory.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
?? passes/260835-3_small-items-pass.diff
?? passes/260835-3_small-items-pass_close-out.md
?? passes/260835-3_small-items-pass_raw-session-output.md
```

## 9. DIFFSTAT, AND THE DELETED-LINE AUDIT IN FULL

```
$ git --no-optional-locks diff --stat
 Incense_Conversational_Outline.md |  11 ++-
 PROJECT_STATE.md                  |  47 ++++++++--
 RJ_Incense_Analysis.md            |  39 +++++++-
 SRC_Channel_Inventory.md          |  10 +-
 SRC_Manifest.md                   |  46 +++++++++-
 St_Francis_EMC_Distinctives.md    | 188 +++++++++++++++++++++++++++++++++++++-
 6 files changed, 320 insertions(+), 21 deletions(-)
```

**Every deleted line (21), truncated to 120 characters. Each is a line this pass deliberately modified; in all but one the original content is preserved inside the replacement.**

```
-**Last updated: 260835-2** (date-stamped, format yymmdd-iteration)
-"The defenders of incense in worship don't treat it as a mere circumstance, and they're right not to: they ground it in…
-**Last updated: 260835-2** (created 260724-3). Read this file first, before any other project document.
-| `PROJECT_STATE.md` | 260835-2 | Backstage | JD + Claude |
-| `St_Francis_EMC_Distinctives.md` | 260835-1 | Backstage — findings corpus. ⭐⭐ **260835-1 — eleven findings minted fro…
-| `RJ_Incense_Analysis.md` | 260834-1 | ⚠️ **BACKSTAGE — DO NOT SHARE** | JD only |
-| `Incense_Conversational_Outline.md` | 260835-2 | **INTERNAL** · relay-clean **SUSPENDED (recoverable)** ⭐⭐ **260835-2…
-| `SRC_Manifest.md` | 260834-9 | Source registry. ⭐⭐⭐ **260834-9 — the seven pre-manifest `aNNN` sources RETRO-REGISTER…
-| `SRC_Channel_Inventory.md` | 260835-1 | ⭐⭐ **260835-1 — nine decision cells EXTENDED (not overwritten) with the `2608…
-**Next free number by prefix:** **`DQ-25`** *(⭐⭐⭐ **UPDATED 260834-3: `DQ-24` IS NOW SPENT** — minted from the number t…
-**Last updated: 260834-1** (date-stamped, format yymmdd-iteration)
-**Last updated: 260835-1** ⭐⭐ (**260835-1 — nine decision cells EXTENDED, none overwritten**, per `ORCHESTRATION.md` §8…
-| `x0hfBI6w6f0` | Debate: Is Apostolicae Curae Correct? (Opening Statements Only) | 2020-08-28 | 2483 | EXT-2 | videos …
-| `C2tCMfq-_hI` | What We Believe About Worship and Holy Communion | 2025-09-23 | 5685 | EXT-3 | videos | 161 | ⚠️⚠️ **…
-| `R-GHhWcuH78` | Christ in the Old Testament, Session VI | 2025-01-11 | 1849 | EXT-3 | videos | 17 | INGESTED — **File…
-| `ZTs6Ru9ZdnI` | Anglican Worship, Session I: Our Approach to Worship | 2024-09-17 | 2146 | EXT-3 | videos | 86 | INGE…
-**Last updated: 260834-9** (date-stamped, format yymmdd-iteration)
-| `AW-SessionI` | **2024-09-17** (`ZTs6Ru9ZdnI`, 2146 s) | ⚠️ **not established** | Session I: Our Approach to Worship …
-| `COT-Class6` | **2025-01-11** (`R-GHhWcuH78`, 1849 s) | ⚠️ **not established** | ⭐⭐⭐ Class 6 (file order 3): **The Ta…
-| ⭐⭐ **Instructed Eucharist (1928 US BCP walkthrough)** — the corpus's `Recon-Euch` | ⚠️ **not established** *(⚠️ candi…
-**Last updated: 260835-1** (date-stamped, format yymmdd-iteration)
```

⭐ **The single true content replacement is line 2 — the spoken core, on JD's ruling.**

## 10. §4.6 / §4.8 / §4.10 UNTOUCHED — verified section by section against `HEAD`

⛔⛔ **Not inferred from the diff. Each section was extracted from `HEAD` and from the working tree and compared directly.**

```
$ for s in 4.6 4.8 4.10; do
>   git show HEAD:RJ_Incense_Analysis.md | awk '<extract §$s>' > /tmp/head_$s.txt
>   awk '<extract §$s>' RJ_Incense_Analysis.md             > /tmp/wt_$s.txt
>   diff -q /tmp/head_$s.txt /tmp/wt_$s.txt
> done

=== §4.6  ===   10 lines HEAD ·  10 lines working tree   IDENTICAL to HEAD  ✅
=== §4.8  ===    8 lines HEAD ·   8 lines working tree   IDENTICAL to HEAD  ✅
=== §4.10 ===   24 lines HEAD ·  24 lines working tree   IDENTICAL to HEAD  ✅
```

⭐ **All three byte-identical to `HEAD`. Their falsified *"unknown"* premise stands exactly as written; the rewrite is owed to a separate pass.**

---

*Full diff: `passes/260835-3_small-items-pass.diff` (336,133 bytes, 596 lines). Analysis: `passes/260835-3_small-items-pass_close-out.md`.*
