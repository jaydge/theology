# 260834-9 — COMPLETE RAW SESSION OUTPUT (unsummarized)

⛔ Verbatim tool output, in run order. Nothing elided, nothing reformatted. Paths appear as the sandbox mount saw them.

⚠️ **Sections 1 and 2 are transcribed from the GATE-TIME runs.** Re-running them now would return different results — `git status` is no longer clean and `260834-9` now returns hits, because this pass wrote it. **That is the point of recording them at gate, and it is stated rather than left to be inferred.** Sections 3 onward are captured output.

## 1. Gate
```
$ git rev-parse HEAD
d536711471c0eed96cd67072f33a1a8c321ca15c
$ git status --short          # AT GATE
(empty, exit 0)
$ ls -la .git/*.lock          # AT GATE
no lock files
$ git rev-parse --abbrev-ref HEAD
main
```

## 2. Stamp derivation
```
$ grep -rn '260834-9' .   ; echo '(end)'
(end)
$ grep -rn '260835-' .    ; echo '(end)'
(end)
$ grep -rhoE "26[0-9]{4}-[0-9]+" --include="*.md" --include="*.py" --include="*.diff" . | sort -u | tail -3
260834-6
260834-7
260834-8
```

## 3. validate_project.py — BEFORE (full)
```
========================================================================
PROJECT INTEGRITY VALIDATION   root: <REPO>
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
  ok    [C3] PROJECT_STATE.md: version agrees with registry (260834-8)
  ok    [C3] ORCHESTRATION.md: version agrees with registry (260834-7)
  ok    [C3] passes/README.md: version agrees with registry (260832-3)
  ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260834-5)
  ok    [C3] RJ_Final_Question_List.md: version agrees with registry (260833-2 (v21))
  ok    [C3] RJ_Open_Questions_and_Divergences.md: version agrees with registry (260833-2)
  ok    [C3] RJ_Incense_Analysis.md: version agrees with registry (260834-1)
  ok    [C3] On_Incense_and_the_Altar.md: version agrees with registry (260833-2)
  ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260833-5)
  ok    [C3] SRC_Manifest.md: version agrees with registry (260834-8)
  ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260834-8)
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
  ok    [C11] IP current in the outline pointer (IP-97 @ 260833-5, ledger at IP-97)
  ok    [C11] RV current in the outline pointer (RV-63 @ 260830-1, ledger at RV-63)
  ok    [C12] session registry parsed: 43 capture row(s) across 33 session(s)
  ok    [C12] 8 standalone recording row(s) parsed and correctly EXCLUDED from the session count (manifest rule: a standalone recording gets no session row)
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
  WARN  [C11] outline last checked against DQ-19 (260833-1); the DQ ledger now runs to DQ-24. 5 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.
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

## 4. Source hashes, byte counts, line counts, delimiter counts (computed this pass)
```
file                                 bytes  lines   ==   >>    stripB
a101-1.txt                          256209     17    9    0    256208
   raw sha256   : 11ebced26d71d6beee81ab1f81dfcbc60d9bd4c17e7566a0220f29858781c0c1
   strip sha256 : a37b29335a00e2eff25e690cab05217b5cf90d97ab3cba957beafc63e098f9a3
a101-2.md                           263995     20   11   39    263994
   raw sha256   : 3123ee648c84587fda1398ffd5fa2b2c8a236313fd2cf605dbe2bf773a696703
   strip sha256 : 1f93d159708520c86628c6b37f47726ac195d2c9e17af4581ad1e285e665e632
a103.md                             259190     19    9   19    259189
   raw sha256   : a46887b1ad065f3accf3dd5cdc5b5ff5fb03bedd0347a508e8734a4021378cd5
   strip sha256 : 0774d0c24e40d97dfbd4d7bbd395f931ae3010525b725828f913a0b1787f928a
a105.md                             188770     15    7    0    188769
   raw sha256   : 555640c60bc5695781d25917c2ed17ca7e5cfaba61e223e378b98b0b80529fc9
   strip sha256 : 491090b53b8cc8a874425e9160c897625942cc0732f11fc884cf54b886daf411
a106.md                              80482     10    6   75     80482
   raw sha256   : aade40a2231481c9de7cd5e843400f13994de60c24109cb497d2652f35a3eabd
   strip sha256 : aade40a2231481c9de7cd5e843400f13994de60c24109cb497d2652f35a3eabd
a201.txt                            177254     22   10    0    177250
   raw sha256   : 09a24f927df0eb39ee2704f351e2a1e97bbc30178e6dc9b214ffdaf24a9c07c8
   strip sha256 : 77f1fcbc7717db61e9a784d82fa65c126933712b08a220c63eff42c84c2d4683
a202.txt                            211170      8    5    0    211169
   raw sha256   : 5fdcafeb0ff6a2fd3424387e2250e212fa614ee84e329431b4609394a86be8a2
   strip sha256 : c413de80bd68478d60a71aef4854eecf8a8a8e780532705972751db9c6befa58
a301-Classical-Theism.md             29338      5    0   33     29338
   raw sha256   : 3551973355aa3518ca877f1d3e9de56ade8e560025d3fa19c3712b8e7bd56585
   strip sha256 : 3551973355aa3518ca877f1d3e9de56ade8e560025d3fa19c3712b8e7bd56585
```

## 5. `^==` offsets — verification of 260834-6 byte ranges (not re-derivation)
```
a101-1.txt 256209 [0, 52, 27453, 66158, 106845, 131324, 164683, 190061, 225635]
a101-2.md 263995 [0, 41, 29823, 62398, 91984, 116831, 139748, 151803, 160770, 166783, 248030]
a103.md 259190 [61, 30247, 58609, 91064, 124286, 149042, 177046, 205247, 232131]
a105.md 188770 [40, 20505, 52550, 76108, 105803, 139615, 165439]
a106.md 80482 [22, 48, 18442, 18461, 47772, 47840]
a201.txt 177254 [0, 52, 37045, 43306, 66153, 73000, 106903, 114581, 153951, 173501]
a202.txt 211170 [0, 51, 95316, 175796, 184863]
```

## 6. Byte-offset probes run this pass
```
a101-2.md @160772: 'Father James here the recor of St Francis Anglican Church in Spartenburg South Carolina I uh this video will b'
a101-2.md @248031: '=Father James here, the director of St. Francis Anglican Church in Spartanberg, South Carolina. And our video '
a101-2.md @166568: "Father James if you liked this video please subscribe this is our Church's YouTube channel I would love for yo"
a101-2.md @263429: ' Father James. You can look, uh, my email is framesgdomsky, g- a d o mskigmail.com. And, uh, if you are in the'
a201.txt @114931: 'father james godomski although my first name is actually adam i had to have that written down for some reason '
a201.txt @35926: "barely Protestant barely Protestant that's a nickname I got from an Eastern Orthodox friend of mine when I was"
a103.md @92374: "Father James. All right, good to see everybody this morning. I hope you're going to enjoy the discussion. If y"
a103.md @96388: "Father James has already introduced some of them to you. You're going to be looking at the end of the first ce"
a103.md @115000: 'Father James knows I struggled. So I dropped number four, combined it into five. So you could technically put '
a103.md @124994: 'father James for giving me the great opportunity to teach this lecture on the great senius. um just um absolut'
a101-1.txt @50101: 'Father James why are you now saying that Jesus says not my will but thine there are two Wills there who who wh'
a106.md @48231: "I'm Gregory Bronson. Um, brother James asked me to come and uh do a talk on my uh area of special specializati"
a101-2 'constructed Eucharist' offsets: [167269]
a101-2 'instructed Eucharist' offsets: []
a105 b'showbread': [62243]
a105 b'shewbread': []
a105 b'bread of the presence': [61086, 61293, 63141]
a106 'sunbeam': [35981, 36138]
```

## 7. a105 recording openings — his own spoken class numbers, re-verified
```
=== rec 1 [40-20504] ===
==it makes fancy noises too all right the Lord be with you with th spirit let us pray Almighty and everlasting God who does govern all things in Heaven and Earth mercifully hear the supplications of thy people and grant us thy peace all the days of our life through Jesus Christ Our Lord amen that collect is the second Sunday after Epiphany I chose it because the theme uh well the focus on this uh class is going to be creation as well as the Garden of Eden uh so God governs both Heaven and Earth all right so class t

=== rec 2 [20505-52549] ===
==right the Lord be with you with th spirit let us pray oh gracious father we humbly beseech thee for thine Holy Catholic Church that thou wouldst be pleased to fill it with all truth in all peace where it is corrupt purify it where it is in error direct it where in anything it is a Miss reform it where it is right establish it where it is in want provide for it where it is divided reunited for the sake of him who died and rose again and ever Liv to make intercession for us Jesus Christ thy son our Lord amen amen a

=== rec 3 [52550-76107] ===
==the Lord be with you sp let us pray almighty God who showest to them that are in error the light of thy truth to the intent that they may return into the way of righteousness Grant unto all those who are admitted into the fellowship of Christ's religion that they may avoid those things that are contrary to their profession and follow all such things as are agreeable to the same through our Lord Jesus Christ amen all right so today we have the sixth class uh last time we met we were doing uh Moses and now we're mo

=== rec 4 [76108-105802] ===
==the Lord be with you let us pray Lord we beseech thee to keep thine household the church in continual godliness that through thy protection it may be free from all adversities and devoutly given to serve thee in Good Works to the glory of thy name through Jesus Christ Our Lord amen this morning we have class five for Christ in the Old Testament this one is titled Jesus the greater Moses now I think this is important because often times I gave this introduction this is I I don't do this very often uh but you'll se

=== rec 5 [105803-139614] ===
==all right the Lord be with you with our spirit let us pray oh Lord we beseech thee mercifully to receive the prayers of thy people who call upon thee and Grant that they may both perceive and know what things they ought to do and also may have Grace and power Faithfully to fulfill the same through Jesus Christ Our Lord amen all right this is class four now we are speaking about uh moving on to the promise of Abraham a promise to Abraham and his seed before that though I want to get into a little sort of seemingly

=== rec 6 [139615-165438] ===
==the Lord be with you and with th spirit let us pray enlarge thy kingdom oh God and deliver the world from the Dominion and tyranny of Satan hasten the time which thy Spirit hath foretold when all nations whom thou has made shall worship thee and glorify thy name bless the good Endeavors of those who strive to propagate the truth and prepare the hearts of all men to receive it to the honor of thine holy name amen all right we are on session 7 now of Christ in the Old Testament we are going to be looking at the lev

=== rec 7 [165439-188769] ===
==really this is what I'm most excited for chalkboard I love chalkboards the Lord be with you with th spirit let us pray keep we beseech thee Oh Lord thy church with thy Perpetual mercy and because the Frailty of Man Without thee cannot but fall keep us ever by thy help from All Things hurtful and lead us to All Things profitable to our Salvation through Jesus Christ Our Lord amen that's the 15th Sunday after Trinity and I should probably have this right here all right so this is class n we're we're almost done go 

```

## 8. a103 recording-3 class-number probe (the correction to 260834-6)
```
Amen. This is class three. We are going over um this will be a two-part uh sort of series within this class uh defending the faith. Uh another word for that is called apologetics. This is part one for defending the faith as indicated by the title. We are going to go over two different works. One is known as the epistle of Barnabas and the other one is known as Justin Martyr's uh dialogue with trifo. All right. Uh so we'll there's a connection to these uh and I I'll go ahead and explain why we have these two in particular. So the Christian defense of the faith is going to come against sort of two broadly speaking sort of approaches. A defense of Christianity against uh Judaism and then a a de
```

## 9. validate_project.py — AFTER (full)
```
========================================================================
PROJECT INTEGRITY VALIDATION   root: <REPO>
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
  ok    [C3] PROJECT_STATE.md: version agrees with registry (260834-9)
  ok    [C3] ORCHESTRATION.md: version agrees with registry (260834-7)
  ok    [C3] passes/README.md: version agrees with registry (260832-3)
  ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260834-5)
  ok    [C3] RJ_Final_Question_List.md: version agrees with registry (260833-2 (v21))
  ok    [C3] RJ_Open_Questions_and_Divergences.md: version agrees with registry (260833-2)
  ok    [C3] RJ_Incense_Analysis.md: version agrees with registry (260834-1)
  ok    [C3] On_Incense_and_the_Altar.md: version agrees with registry (260833-2)
  ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260833-5)
  ok    [C3] SRC_Manifest.md: version agrees with registry (260834-9)
  ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260834-9)
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
  WARN  [C11] outline last checked against DQ-19 (260833-1); the DQ ledger now runs to DQ-24. 5 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.
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

## 10. BEFORE vs AFTER diff (paths normalised to <REPO> on both sides)
```
38c38
<   ok    [C3] PROJECT_STATE.md: version agrees with registry (260834-8)
---
>   ok    [C3] PROJECT_STATE.md: version agrees with registry (260834-9)
47,48c47,48
<   ok    [C3] SRC_Manifest.md: version agrees with registry (260834-8)
<   ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260834-8)
---
>   ok    [C3] SRC_Manifest.md: version agrees with registry (260834-9)
>   ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260834-9)
78,79c78,79
<   ok    [C12] session registry parsed: 43 capture row(s) across 33 session(s)
<   ok    [C12] 8 standalone recording row(s) parsed and correctly EXCLUDED from the session count (manifest rule: a standalone recording gets no session row)
---
>   ok    [C12] session registry parsed: 74 capture row(s) across 64 session(s)
>   ok    [C12] 27 standalone recording row(s) parsed and correctly EXCLUDED from the session count (manifest rule: a standalone recording gets no session row)
```

⭐ Exactly five lines differ. All five are `ok` before and `ok` after.

## 11. Close-out git state
```
$ git status --short
 M PROJECT_STATE.md
 M SRC_Channel_Inventory.md
 M SRC_Manifest.md
?? passes/260834-9_annn-retro-registration_pass-a.diff
?? passes/260834-9_annn-retro-registration_pass-a_close-out.md
?? passes/260834-9_annn-retro-registration_pass-a_raw-session-output.md
$ echo exit=$?
exit=0
$ git rev-parse HEAD
d536711471c0eed96cd67072f33a1a8c321ca15c
$ ls -la .git/*.lock
-rw------- 1 zealous-sharp-noether zealous-sharp-noether 0 Aug 26 01:00 .git/index.lock
$ git stash list
(empty — the one attempted `git stash push` created NO stash and was NOT retried)
```

## 12. C12 session-registry delta, re-derived with a replica of the validator parser
```
BEFORE:  parsed 43   sessions 33   standalone 8
AFTER:   parsed 74   sessions 64   standalone 27
DELTA:   +31 rows   +31 sessions   +19 standalone   (exactly the rows written)

New session-row ids (31, all unique, no collision with any existing row):
  A101video-SI SII SIII SIV SV SVI SVII SVIII
  AW-SessionI II III IV V VI-Pt1 VI-Pt2
  ANF-Class1 2 3 4 5 6 7 8 9
  COT-Class2 Class3 Class4 Class5 Class6 Class7 Class9
```
