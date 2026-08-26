# 260835-1 — TARGETED MINING OF FILES 41 AND 43 AGAINST THE LIVE QUESTIONS (PASS B1)

**Last updated: 260835-1.** ⛔⛔ **ELEVEN FINDINGS MINTED AS SECTION BULLETS WITH BYTE-RANGE CITATIONS · NO `LS`, `IP`, `RV`, `BLOG`, `POD`, `DQ`, `VP`, `DELTA`, `EXT`, `W` OR `File` NUMBER CONSUMED · 32 CANDIDATE DATA REJECTED AS ALREADY HELD.**

> ⭐ **The `git diff` is 219 lines / 114,899 bytes and is too large for chat; it is written to `passes/260835-1_files-41-43-targeted-mining_pass-b1.diff`, as the brief directs.** The complete raw session output is at `passes/260835-1_files-41-43-targeted-mining_pass-b1_raw-session-output.md`. This close-out carries the gate, the reasoning, the verification, the rejections and the decisions. *(§5 rule 11 — this note makes no claim about its own commit state.)*

---

## ✅ GATE

| Check | Expected | Observed | Result |
|---|---|---|---|
| `git rev-parse HEAD` | `4801284` | `48012843bc3aee71b64d86323e2c38ed5c3ac24e` | ✅ **MATCH** |
| Branch | — | `main` | — |
| `git status --short` before first write | — | *(empty, exit 0)* | ✅ **CLEAN** |
| `.git/*.lock` at gate | ⚠️ briefed as recurring for **five** consecutive passes | ⭐⭐ **ABSENT** — `ls -la .git/*.lock` → `No such file or directory` | ✅ **no lock** |
| `.git/*.lock` at close-out | — | ⚠️⚠️ **PRESENT** — appeared at the FINAL `git status`/`git diff`, after a mid-pass check had found it absent | ⚠️ **RECURRED. REPORTED, NOT WORKED AROUND.** |
| `validate_project.py` BEFORE | derive | **`80 ok · 9 warnings · 0 errors`** | ✅ recorded |
| `PROJECT_STATE.md` stamp at gate | report | **`260834-9`** (created `260724-3`) | ✅ reported |
| Next-free pass stamp | derive by repo-wide grep | **`260835-1`** ⚠️ *(with a reported ambiguity — §0.3)* | ✅ **DERIVED, VERIFIED FREE, AMBIGUITY REPORTED** |
| Next-free `IP` | re-derive fresh | **`IP-98`** — ⛔ **NOT consumed** | ✅ re-derived |
| Source hashes | verify, do not copy | ✅ both **recomputed from the files and matching** | ✅ verified |

### 0.1 Every firing code, recorded individually (9 warnings, 0 errors)

1. **`WARN [C1]`** `src/SRC_Discord_RPW.md`: 2 relative timestamp(s) outside message headers (`'Yesterday at …'`). Not caught by the header rule; check whether they are quoted text or unresolved captures.
2. **`WARN [C3]`** `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md`: no parseable `'Last updated'` stamp; registry says `'260832-2'`.
3. **`WARN [C3]`** `tools/transcribe_yt.py`: no parseable `'Last updated'` stamp; registry says `'260833-7'`.
4. **`WARN [C4]`** `St_Francis_EMC_Distinctives.md`: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby. Review manually.
5. **`WARN [C5]`** `RJ_Final_Question_List.md`: 17 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
6. **`WARN [C5]`** `RJ_Incense_Analysis.md`: 9 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
7. **`WARN [C5]`** `St_Francis_EMC_Distinctives.md`: 7 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
8. **`WARN [C10]`** §15's newest LS citation is 8 findings behind the ledger (`LS-120` vs `LS-128`). Sweep the interval for creditable material.
9. **`WARN [C11]`** outline last checked against `DQ-19` (`260833-1`); the DQ ledger now runs to `DQ-24`. 5 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.

**Identical set and order to `260834-6`, `-7`, `-8` and `-9`'s BEFORE runs.**

### 0.2 ⚠️⚠️ THE `.git` LOCK — IT RECURRED, AND THIS SECTION CORRECTS ITS OWN EARLIER READING RATHER THAN PUBLISHING IT

⛔⛔ **A CORRECTION TO THIS PASS'S OWN MID-PASS OBSERVATION, MADE BEFORE PUBLICATION AND RECORDED RATHER THAN SILENTLY FIXED — THE IDENTICAL SHAPE `260834-7` REPORTED.** Midway through, this pass had observed the lock absent at a post-edit `git status --short` and had drafted this section as *"absent at both ends, the first time in the sequence."* **The FINAL `git status --short` produced the lock.** The mid-pass observation was true and incomplete; the finding is the full sequence.

| Moment | Command | Result |
|---|---|---|
| **Gate** | `ls -la .git/*.lock` | ⭐ `ls: cannot access '.git/*.lock': No such file or directory` — ⛔ **no lock** |
| **Gate** | `git status --short` | clean, exit 0, ⛔ **no unlink warning, no lock created** |
| **Mid-pass** *(after all three files were edited)* | `git status --short`, `git rev-parse HEAD`, `git diff --stat` | three entries, exit 0, ⛔ **no unlink warning**; `ls -la .git/*.lock` → **still absent** |
| **Close-out** | `git diff > passes/…​.diff` then `git status --short` | output normal and complete, then ⚠️ `warning: unable to unlink '/…/theology/.git/index.lock': Operation not permitted` |
| **Close-out** | `ls -la .git/*.lock` | ⚠️ **`-rw------- … 0 Aug 26 2026 .git/index.lock`** — zero-byte lock present |

⚠️⚠️ **SO THE `260834-6`/`260834-7` PATTERN IS REPRODUCED A FOURTH TIME: absent at gate, present at close-out, same `Operation not permitted` on unlink, same zero-byte file.**

⭐⭐ **AND THE OBSERVATION THIS PASS CAN ADD, OFFERED AS OBSERVATION AND NOT AS DIAGNOSIS.** ⛔ **This pass ran NO index-writing porcelain at all — no `git add`, no `git commit`, no `git stash`.** Only `git rev-parse`, `git status`, `git show HEAD:<path>`, `git diff --stat` and `git diff`. ⚠️⚠️ **That means `260834-9`'s narrowing — *"the lock appeared at the moment of an INDEX-WRITING command (`git stash push`), not at a read-only `git status`"* — is NOT sufficient as stated, because no such command was run here.** ⭐ **What distinguishes the two `git status` invocations within THIS pass is the same thing `260834-7` named as a candidate and declined to conclude from: the tree was clean at the first and dirty at the second.** ⛔⛔ **A likelier mechanism is available and is offered as a hypothesis only: `git status` and `git diff` REFRESH the index when cached stat data is stale — which is precisely what a dirty tree causes — and an index refresh is an index WRITE. On that reading `260834-9`'s narrowing survives and merely needs widening from "index-writing porcelain" to "any operation that refreshes the index."** ⛔ **NOT ADOPTED. It is a hypothesis that fits four observations and has not been tested, and testing it would mean deliberately provoking the condition, which is not this pass's business.**

⛔⛔ **NO WORKAROUND WAS APPLIED.** The lock was **not** force-removed, its permissions were **not** changed, `.git` was not touched by any other means, and **no git operation was retried against it.** Read-only plumbing was unaffected throughout: `git rev-parse HEAD` returned `48012843bc3aee71b64d86323e2c38ed5c3ac24e` after the lock appeared, unchanged, and the closing `git status --short` produced correct and complete output at exit 0 **with the lock in place**. ⚠️⚠️ **THE CONSEQUENCE FOR WHOEVER STAGES THIS PASS: `git add`/`git commit` may fail on `.git/index.lock`. ⛔ DO NOT FORCE-REMOVE IT. The fix belongs to whoever owns the filesystem permissions on `.git/`, not to a pass.**

### 0.3 ⚠️⚠️ STAMP DERIVATION — AND THE ONE AMBIGUITY IN IT IS REPORTED, NOT SILENTLY RESOLVED

`grep -rhoE '\b26[0-9]{4}-[0-9]+\b'` across every `.md`, `.py`, `.txt`, `.diff` and `.patch` in the repo returns a highest stamp of **`260834-9`**. `260835` returns **six** hits and **every one is prose inside `260834-5`/`-6`/`-7`/`-9`'s own artifacts and `PROJECT_STATE.md` asserting that `260835` is free** — none is a stamp in use, and each was read in context before being dismissed.

⛔⛔ **THE AMBIGUITY, STATED PLAINLY BECAUSE A LATER PASS WILL MEET IT AGAIN.** `260834` is the **first day-group in the project's history to reach `-9`**, and **there is no precedent in either direction**:

| Evidence | Value |
|---|---|
| Highest iteration ever reached in any group | **`-9`** (this group; next highest `-8` at `260833`) |
| `grep -rhoE '\b26[0-9]{4}-1[0-9]\b'` — has a **two-digit iteration** ever been used? | ⛔ **ZERO hits. Never.** |
| Iterations at which prior groups terminated | `-1`, `-2`, `-3`, `-4`, `-5`, `-8` — ⛔ **no fixed cap** |
| Is the `yymmdd` field a real date? | ⛔ **No.** `PROJECT_STATE.md`'s own `260823-1` gate note: *"the stamp series is a **monotonic pass counter** in `yymmdd-n` form that **has outrun the wall-clock date**"* — and `260834` spans two calendar days (`2026-08-25` and `2026-08-26` in `git log`), so the group boundary is not calendar-driven either |

⭐ **`260835-1` WAS CHOSEN, AND THE GROUND IS RECORDED:** advancing the monotonic counter continues the established series, whereas `260834-10` would introduce a two-digit iteration that has never been used and that **sorts wrongly** in `passes/` (`260834-10` would file between `260834-1` and `260834-2`). ⚠️⚠️ **`260834-10` IS THE LIVE ALTERNATIVE, IT IS GREP-VERIFIED EQUALLY FREE, AND IT IS NAMED HERE SO THE CHOICE IS VISIBLE AND CHEAPLY REVERSIBLE** — three stamp strings and two filenames — **rather than buried in a stamp nobody re-examines.** ⏳ **A one-line convention in `ORCHESTRATION.md` fixing the roll-over rule is OWED and deliberately not written by this pass; a convention edit is not this pass's brief.**

### 0.4 Next-free `IP`, re-derived fresh and NOT consumed

⭐ **Re-derived from the repo, not copied from any prior document.** `grep -rhoE '\bIP-[0-9]{1,4}\b'` across every `.md` returns a maximum token of `IP-98`; **every `IP-98` occurrence repo-wide was read in context and every one is a next-free registry assertion** (`260833-4`'s close-out, `260834-5`/`-6`/`-7`/`-9`'s close-outs, `PROJECT_STATE.md`, `St_Francis_EMC_Distinctives.md`'s `260834-5` changelog entry). The highest `IP-n` attached to an actual finding is **`IP-97`**, and validator `C2` independently reports `IP-1..97 unbroken, no duplicates`. ⛔⛔ **`IP-98` IS FREE AND THIS PASS DID NOT CONSUME IT — see §5 on why, and on the prefix question that is reserved to JD.**

### 0.5 Sources verified against the files, not against the registration

| File | Source | Registered raw `sha256` (`260834-9`) | **Recomputed this pass** | Bytes | Result |
|---|---|---|---|---|---|
| **41** | `a101-2.md` | `3123ee648c84587fda1398ffd5fa2b2c8a236313fd2cf605dbe2bf773a696703` | ⭐ **identical** | 263,995 ✅ | ✅ **MATCH** |
| **43** | `a105.md` | `555640c60bc5695781d25917c2ed17ca7e5cfaba61e223e378b98b0b80529fc9` | ⭐ **identical** | 188,770 ✅ | ✅ **MATCH** |

⭐ **The RAW convention was used, as `260834-9` registered it as the value of record. The `260834-9` File 44/45 hash trap was not walked into — no strip-convention value was computed, compared or relied on.**

---

# 1. ⭐⭐⭐ THE HEADLINE — AN ANSWER THE PROJECT HAS BEEN TREATING AS UNKNOWN HAS BEEN ON RECORD SINCE 2024, IN A FILE THE PROJECT ALREADY MINED

**`RJ_Incense_Analysis.md` §4.6 is the "pure offering" parallel-clause lever — upgraded, in its own words, "from reserve to a lead internal lever." It rests on a premise. The premise is that his reading of Malachi 1:11's second clause is unknown.** Its §4.10 reserve entry instructs: *"Deploy only if he leans back on Malachi: **ask what the 'pure offering' is**, and let the Trent/Mass consequence or the spiritualizing-consistency consequence do the work."* Its closing uncertainty list states it outright:

> *"Whether, pressed on the Malachi 'pure offering,' he will move toward a sacrificial reading (→ Trent proximity) or retreat to spiritual (→ concedes the incense) — **unknown**, and diagnostic of how far his Romeward drift actually runs."*

⭐⭐⭐ **IT IS NOT UNKNOWN. HE ANSWERS IT TWICE, IN 2024, UNPROMPTED, IN THE SAME SIX-WEEK CLASS THE CORPUS MINED FOR THE REGULATIVE-PRINCIPLE MATERIAL — 8 KB AWAY FROM IT IN THE SAME RECORDING.**

**`AW-I`, File 41 `@18,335`–`@18,760`** — reading Mal 1:11 in full (he calls it *"one of my favorite verses in the whole Bible… I have this verse on my contact cards"*):

> ***"by the way, that pure offering is Jesus, because there is only one pure offering — Jesus himself. He is the pure offering. He is offered to us for the forgiveness of sins. He daily intercedes for us in heaven because of the work that he has done on the cross."***

**`AW-IV`, File 41 `@113,900`–`@114,200`** — a week later, same series, same verse, with the guard attached:

> *"we see Malachi 1:11 prophesying that the Gentiles will be the ones who are worshiping God using incense and offering a sacrifice, **a pure sacrifice, which is Christ himself — we're not offering him afresh, we're offering… ourselves united to Christ.**"*

**`Recon-Euch`, File 41 `@195,097`–`@195,300`, 2025** — reading the verse aloud a year later, he renders the second clause himself:

> *"and a pure, **or a grain**, sacrifice."*

⭐ **That last is not incidental: it is `RJ_Incense_Analysis.md` §4.8's *minchah* fork, in his own mouth. He knows the word is the grain offering — and in `File 43` class 7 he teaches the grain offering as fulfilled in Christ the bread of life and enacted in Holy Communion (§3.A below).**

## 1.1 ⛔⛔ IT IS A **THIRD** FORK, AND THE LEVER'S AXIS IS THE WRONG ONE

| Fork §4.6/§4.10 anticipates | What it would cost him | Does he take it? |
|---|---|---|
| **Sacrificial-literal** — a literal offering on an altar | → Trent proximity (Session 22, ch. 1) | ⛔ **NO.** He pre-empts it in the same breath: *"we're not offering him **afresh**"* |
| **Spiritualizing** — the offering is prayer/thanksgiving (Heb 13:15) | → concedes the incense on the same reading | ⛔ **NO.** He never reads the offering as prayer |
| ⭐⭐⭐ **CHRISTOLOGICAL** — the pure offering **is Christ**, received and re-offered in us | ⛔ **neither consequence lands** | ✅ **THIS ONE, TWICE** |

⚠️⚠️ **AND IT IS THE SAME MOVE HE MAKES EVERYWHERE ELSE.** The showbread (`DQ-20`): the type is fulfilled and the antitype is **enacted**. The grain offering (§3.A): the type is fulfilled and the antitype is **enacted**. Mal 1:11's *"pure offering"*: the type is fulfilled in Christ and the antitype is **enacted** in the Oblation, *"ourselves united to Christ."* ⛔⛔ **So §4.6's framing — *"he cannot literalize the incense and spiritualize the offering in one clause"* — describes an axis he is not on, and the lever as drafted would meet an answer it does not anticipate.**

## 1.2 ⭐⭐ WHAT THE LEVER BECOMES — RECORDED AS THE SHAPE OF THE SEAM, ⛔ NOT DRAFTED, NOT DEPLOYED, NOT POSTED

Within **one verse** and **one parallelism** he treats the two clauses **oppositely with respect to physical enactment**:

- On the ***offering*** clause: fulfilment in Christ **DISCHARGES** the physical act. *"We're not offering him afresh."*
- On the ***incense*** clause: the symbol **REQUIRES** the physical act. *"A symbol doesn't work well if it's not there. It's got to be there to work."* (`Recon-Euch` `@195,711`, already on record at §13.)

⭐ **That is sharper and more accurate than the lever on file, and it needs no imported Reformed premise either.** ⛔⛔⛔ **`RJ_Incense_Analysis.md` §4.6, §4.8 AND §4.10 WERE NOT EDITED. Their "unknown" premise is REPORTED AS FALSIFIED and left standing, per the never-alter rule — the correction is written into `St_Francis_EMC_Distinctives.md` §13 and here, beside them, not over them.** ⏳ **Rewriting §4.6 is OWED and is a separate pass's job; so is deciding whether the reformulated seam is worth putting to him at all.**

---

# 2. THE LIVE QUESTIONS, ANSWERED OR MOVED — ONE ROW PER QUESTION THE BRIEF NAMED

| Live question | What this pass found | Status |
|---|---|---|
| **`DQ-24`'s five-level ordering; what makes a practice received** | ⭐⭐ The only place in the corpus where he says what a tradition is **for**: *"a ritual of passing down of a **tradition** that helps maintain **stability within the society**"* (File 43 `@155,540`). ⚠️ **LIMIT: it is an alphabet analogy, and he does not apply the word to ecclesial Tradition in it.** | ⏳ **`DQ-24` UNTOUCHED. `OQ21` sharpened, not answered.** |
| **`OQ21` — church-wide vs jurisdictional reception** | ⛔ **Nothing.** Neither file distinguishes practices received church-wide from practices received jurisdictionally. `Bishop Ordinary` · `sect or jurisdiction` · `gathered Bishops` · `established customs` all **0** across both files. | ⛔ **HONEST ZERO. `OQ21` does not move.** |
| **Element / circumstance** | ⭐⭐⭐ A **THIRD non-instance**, and the first of a new kind — see §2.1. | ⛔ **NOT resolved. Logged as an absence.** |
| **His warrant for incense** | ⭐⭐ A dated **conversion narrative** with Mal 1:11 named **by him** as *"the final nail in the coffin"*; the three-legged warrant stated as a unit; ⭐⭐⭐ and §1's *"pure offering"* answer. ⭐ Plus a **third, untracked warrant type** — ritual act as divine pedagogy (§2.2). | ⭐⭐ **SUBSTANTIALLY ADVANCED.** |
| **Heaven-earth participation** | ⭐⭐ A **second and earlier ground**: the **Incarnation**, at the Sursum Corda, 2024 — not the heavenly *pattern* the 2025 Revelation class supplies. **A ground the fulfilment rule cannot reach.** | ⭐⭐ **ADVANCED.** |
| **Showbread and type/antitype** | ⭐⭐⭐ He **taught the showbread himself**, twelve loaves and all — **including the incense on top of the bread**. See §3.B; it qualifies a clause of `DQ-20`'s `[Analysis]`. | ⭐⭐⭐ **CORRECTION OF RECORD.** |

## 2.1 ⭐⭐⭐ THE ELEMENT/CIRCUMSTANCE QUESTION — A THIRD NON-INSTANCE, AND THE FIRST IN WHICH HE **BUILDS** THE ARGUMENT THE DISTINCTION WOULD DEFEAT

**[Stated, `Recon-Euch` · File 41 `@196,456`–`@196,900`, 2025.]** He concedes the gap himself, unprompted:

> *"Now, there's no explicit mention of incense in sort of like the book of Acts, for instance, as part of the worship of the church. **But there are no explicit mentions of things like women receiving holy communion in the New Testament church. Does that mean therefore women should not receive holy communion?**"*

And then the burden rule, applied to incense by name (`@196,878`–`@197,090`):

> *"When we see scripture in the Old Testament and scripture in the perfect worship of God in heaven, incense is in both. **I need a strong argument.** And then of course the prophecy in Malachi — **I need a strong argument to tell me no, we shouldn't use incense.** So I try to be careful not to do too much incense, but I think it's an important part of our worship. That's my little tantrum entire. I apologize, but I'm in charge."*

⭐⭐ **THE BURDEN RULE IS HERE A YEAR BEFORE `DQ-19`/`DQ-24`(b).** `DQ-24`(b) is logged as *"the burden rule's cleanest statement yet"* (*"the onus is upon the innovator"*, 2026-08-25). **This is the same rule in negative-direction phrasing, applied to the concrete case, in 2025.** ⛔ **`DQ-24`(b) IS NOT AMENDED, RE-DATED OR MERGED. Logged as an EARLIER INSTANCE, which is what it is.**

⛔⛔⛔ **WHY THE REDUCTIO MATTERS AND WHAT IT IS NOT.** `260834-5` established that he has been **handed** the element/circumstance distinction twice and taken it up neither time (`BP-48`(b)'s *tu quoque*, no criterion supplied; `A101-2026-08-09` seg 3's *adiaphora* framing, answered on the concrete case instead). ⚠️⚠️ **This third instance is different in kind: nobody puts the distinction to him, and he constructs — unprompted — the one argument it most cleanly defeats.** A critic holding WCF 1.6 answers in one sentence: *who* receives a commanded element is a **circumstance** of that element; adding incense introduces a **new ceremony**; the parallel does not run.

⛔⛔ **AND THE THREE THINGS THIS IS EXPRESSLY NOT LOGGED AS.** **(a)** Not an **error** — the reductio is a live and common argument and it is not obviously wrong. **(b)** Not **ignorance** — `LS-47` (2020) establishes he commands the RPW/normative vocabulary and deploys it accurately. **(c)** Not **evasion** — nobody raised it. ⭐ **It is logged as what it is: the corpus's first instance of him ARGUING INSIDE the gap the distinction marks, rather than declining to engage it when offered.** ⛔ **`DQ-9` does not move. Nothing is drafted toward him on it.**

## 2.2 ⭐⭐⭐ A **THIRD** POSITIVE WARRANT FOR CEREMONIAL THAT §13 DOES NOT TRACK — AND IT IS IMMUNE TO BOTH STANDING OBJECTIONS

`ritual act` is grep-verified **0** across `St_Francis_EMC_Distinctives.md`, `RJ_Incense_Analysis.md`, `On_Incense_and_the_Altar.md`, `RJ_Final_Question_List.md` and `Incense_Conversational_Outline.md`. It occurs **8 times** in `a105.md`.

**[Stated, File 43 `@63,994`–`@65,240`, his class 6]:**

> *"You're noticing that the vast majority — and almost exclusively, not quite exclusively but almost exclusively — the way things are being taught to the people of God are **ritual act**: various placements, various actions that are happening, various objects — **not merely a list of 'well, this is what you believe' and just sort of passing it on merely by word.**"*

He guards it (*"don't misunderstand, the word is incredibly important — in fact we're receiving this information from the word"*), gives the mechanism (*"the word itself is giving us examples of ritual act that **reinforce** these beliefs"*), and illustrates it with a child's teeth (*"you do acts… you show the child how to brush his or her teeth. **This is what God is doing to his people.**"*). ⭐⭐⭐ **Then the application, in one clause at `@65,195`: *"So ritual act is very important. **We obviously think that that's true here too, right?**"***

**[Stated, File 43 `@154,693`–`@155,600`, his class 7]** — restated with a different analogy: the alphabet song, learned by everyone in the same tune and the same order though *"there's nothing inherent that says you have to have A, B, C, D"*; ***"we've ritualized the teaching"***; and ***"that's a ritual of passing down of a tradition that helps maintain stability within the society."***

⭐⭐⭐ **WHY THIS IS A THIRD WARRANT AND NOT A RESTATEMENT OF EITHER TRACKED ONE.**

| Warrant | §13 tracks it as | Standing objection |
|---|---|---|
| (i) OT / apocalyptic ceremonial | Exod 30, Mal 1:11, Rev 8 | ⚠️ his own fulfilment rule (the 🎯 lever) |
| (ii) Heaven-earth participation | `Rev-9/10/11`, *"our worship is reflecting their worship"* | ⚠️ the apocalyptic-genre objection |
| ⭐⭐⭐ **(iii) Ritual act as divine pedagogy** | ⛔ **NOT TRACKED AT ALL** | ⛔⛔ **NEITHER OBJECTION REACHES IT** |

⛔⛔ **(iii) is a claim about God's *pedagogical method*, not about any particular Old Testament rite — so the fulfilment rule has nothing to fulfil — and it makes no appeal to Revelation's imagery — so the genre objection has nothing to bite on.** ⚠️⚠️ **Any future form of `OQ8` aimed only at (i) and (ii) leaves (iii) standing, and this is recorded so that is a choice rather than an oversight.**

⚠️ **THE `OQ21` BEARING, WITH ITS LIMIT NAMED RATHER THAN OVERSOLD.** `260834-5` found *Tradition* has never been a discrete ranked item, and that where he treats it by name (`A101-VI`) he gives it an **explanatory** office. ⭐ **The class-7 clause gives it a third office: TRANSMISSIVE AND STABILIZING.** ⛔⛔ **BUT THE SENTENCE IS ABOUT THE ALPHABET.** It is a secular analogy offered to explain why God taught Israel by ritual; he does not apply the word to ecclesial Tradition in it. ⛔ **NOT logged as a definition of Tradition, NOT as an answer to `OQ21`, and `DQ-24`(a) level (2) is untouched.**

## 2.3 ⭐⭐⭐ THE FULFILMENT RULE CARRIES A QUALIFIER, AND §13's STRONGEST INTERNAL LEVER WAS RECORDED WITHOUT IT

`uniquely Old Testament` and `uniquely OT` are grep-verified **0** across all five project documents. The corpus's 🎯 lever quotes the conclusion of this sentence and not its restriction. **[Stated, File 43 `@75,677`–`@75,960`, his class 6]:**

> *"So when we go to the ritual acts that are established here that don't carry on over here, right, and we say, well no, we need to go back to these Old Testament practices **that are uniquely Old Testament**, right — that's when we get into issues of implicitly, liturgically, ceremonially saying that this has not yet happened."*

⚠️⚠️ **THIS CUTS TWO WAYS AND BOTH ARE STATED.** ⛔ **It does NOT weaken the lever and is NOT logged as doing so.** But it supplies, in his own words, **the criterion the lever must clear** — and on his own account incense is *not* uniquely Old Testament: Malachi 1:11 prophesies it **for the Gentile church** and Revelation 8 has it in **heaven**, which are exactly the two texts he leans on. ⭐ **So the fulfilment rule and the incense defence are, on his own qualifier, consistent — and the project should have known that before pressing.** ⚠️ **Equally: it is a criterion he states and never applies to a contested case, which is the same shape as the fulfilment-scope question JD has asked twice and received an instance for both times (`DQ-20`).** ⛔ **`OQ8` is SHARPENED and NOT MOVED; nothing is drafted toward him.**

---

# 3. FILE 43 — WHAT THE PRIORITY READS PRODUCED

## 3.A ⭐⭐⭐ THE SIX LEVITICAL OFFERINGS RUN IN REVERSE ONTO THE 1928 LITURGY'S OWN ORDER

**[Stated, File 43 `@141,115`–`@163,900`, his class 7.]** He takes Leviticus chapter by chapter — **burnt · grain ("meat") · peace · sin · guilt · ordination** — showing each *"pointing to the Cross"*. Then, of a section he says he added days before the class *"because I thought it was really powerful"*:

> ***"What if we were to go backwards with this? They're looking forward — and if we mirror that and look backwards, let's see what happens."***

| Levitical offering | Where it lands in the liturgy, in his own words |
|---|---|
| **Ordination** | *"the priest presides over the celebration of Holy Communion… Christ himself is ordained, is consecrated, chosen to be the one — Christ our high priest"* |
| **Guilt** (sin against God) | the Decalogue's **first table** — *"they're all laws about God"* |
| **Sin** (sin against neighbour) | the **second table** / the Summary of the Law — *"there has to be a reconciliation with God [first]… then… with humanity"* |
| **Peace** | ***"the Absolution… and then we have those comfortable words — that's one of my favourite parts of the liturgy"*** |
| **Grain** | the Sursum Corda, the prayer of consecration, *"the bread and the wine"* — tied to **Melchizedek's** bread-and-wine (`@160,615`) |
| **Burnt** | the **Oblation** — *"the offering of our entire selves to God, because what does Christ do? He offers his entire self to us"* |

⭐ **His own summary: *"we are seeing the liturgy play out"*; *"we are walking backwards through this"* (`@161,507`); and of the whole construction — *"this is God telling his story to us, saying: in a thousand years from now this is all going to make perfect sense, so just have faith in me"* (`@164,985`).**

⭐⭐ **AND THE UNIQUENESS CLAIM, HEDGED BY HIM AND RECORDED WITH THE HEDGE.** Reading the Oblation from page 81 with his hands on the altar: *"as far as I know, the Anglican liturgy is **the only one** that has an explicit reference of this offering of our entire selves to God in the Holy Communion itself… **I could be wrong**, but I've heard other Anglicans say this as well"* (`@163,615`–`@163,900`). ⚠️ **The same claim in weaker form at `AW-V` File 41 `@125,100`–`@125,350`: *"very unique in ours as well."*** ⛔ **The claim's TRUTH is not assessed and NO accuracy flag is raised — §19 is not touched. It is his stated belief about his own rite, twice.**

⭐⭐⭐ **[Analysis] WHY IT MATTERS.** `peace offering` · `guilt offering` · `ordination offering` · `six offerings` · `reverse order` all **0** across the corpus; `burnt offering` occurs once and not from this source. **This is the STRUCTURAL counterpart of `DQ-20`/`DQ-24`(d)'s showbread answer.** There, one non-atoning sanctuary component is fulfilled **and its antitype is still enacted**. **Here the same move is applied not to one component but to the WHOLE ORDO: the entire Levitical sequence is fulfilled, and its fulfilment is performed, in order, every Sunday.**

⛔⛔ **AND THE THREE-PATTERN OBSERVATION, LABELLED `[Analysis]` AND EXPRESSLY NOT ATTRIBUTED TO HIM.** The corpus now holds three distinct patterns in his own teaching: **(i)** fulfilled → **CEASES** (the sin offerings, `DQ-19`); **(ii)** fulfilled → **ENACTED IN THE ANTITYPE** (showbread → Eucharist, `DQ-20`; the whole ordo, here); **(iii)** prophesied → **RETAINED AS ITSELF** (incense, Mal 1:11). ⛔⛔⛔ **HE HAS NEVER STATED THIS AS A RULE. It is not attributed to him, it is not the answer to the question JD has asked twice, and it is NOT drafted toward him.** ⭐ **It is recorded because JD asked for the criterion and keeps receiving instances — and three instances with three different shapes is itself the datum.**

## 3.B ⭐⭐⭐ THE SHOWBREAD WAS NOT "A COMPONENT SUPPLIED TO HIM BY THE QUESTION"

**[Stated, File 43 `@60,050`–`@63,141`, his class 6.]** The table of *"the bread of the presence"*: **twelve loaves**, *"made in preparation for the Sabbath… so likely they were made on Friday"*, *"dedicated to God"*. His own connection:

> ***"So what day does Christ die? Friday… and what ritual act does Christ associate with his death, on the night in which he was betrayed? Holy Communion, the Lord's Supper"*** — *"so we see this bread being connected, Christ himself being the bread of life… where we are eating bread and drinking wine and thus being united to Christ in his death."*

And at `@62,221`: ***"the priests are the ones who will ceremonially eat this showbread."***

⛔⛔⛔ **AND THE CLAUSE THAT MATTERS MOST, AT `@62,844`:**

> ***"they put incense on top of the bread, which is a very interesting thing to do"***

— followed immediately (`@62,968`) by his standing rule: *"remember, whenever you see incense in the Old Testament or in the New Testament, you associate it with the prayers of the saints of God."*

### The cross-reference, and it is a correction of record

`DQ-20`'s `[Analysis]` records that his showbread answer *"was therefore not drawn from what he had just taught"* and that he supplied it *"on a component supplied to him by the question."*

| Claim | Verdict |
|---|---|
| *"not drawn from what he had just taught"* (the 2026-08-23 class) | ⭐ **TRUE AND STANDS.** `IP-90` verified `showbread` **0·0** across both captures. Nothing here touches it. |
| *"on a component supplied to him by the question"* | ⛔⛔ **QUALIFIED.** The showbread, the twelve loaves, the priests' reverent eating and the Eucharistic reading are all his own classroom teaching, years earlier. |

⭐⭐ **`DQ-20`(c)'s elaboration — *"The priests were to reverently eat the Bread, and by that ritual they were Communing with God"* — is `File 43 @62,221` restated.** ⛔⛔⛔ **AND SO IS THE FRANKINCENSE: JD's own message 31 narrowed the question using exactly this detail — *"twelve loaves set out on the table each Sabbath with **frankincense** offered with them as Leviticus 24 prescribes"* (`src/SRC_Discord_RPW.md:325`, 2026-08-25) — and Rev. James had taught the incense-on-the-showbread himself, a year earlier.**

⭐ **The component was not supplied to him. It was RETURNED to him.**

⛔⛔ **WHAT THIS CHANGES AND WHAT IT DOES NOT.** `DQ-20`(b)/(c) unaltered, un-re-dated, un-merged. `260833-3`'s observation-only disposition on the class/Discord type difference **unchanged**. `DQ-20` itself **NOT EDITED** — a dated note is added beside it and its own wording stands, per the never-alter rule. ⭐ **What changes is only the inference about NOVELTY: the showbread reading is not a fresh construction produced under questioning but a position he has taught — which makes it MORE settled, not less.**

⭐⭐ **A SECOND FRANKINCENSE DATUM, FROM HIS CLASS 7 (`@144,858`):** the grain offering is *"a voluntary one, made of **fine flour, oil and frankincense**."* ⚠️⚠️ **`RJ_Incense_Analysis.md` §4.13 carries Leviticus 2:1-2's frankincense as the PROJECT'S OWN research — *"also checked this pass: Leviticus 2:1-2 against the corpus's Exodus 30 material"* — with no record that he teaches it. He does.** ⛔ **REPORTED, NOT CORRECTED.**

## 3.C ⚠️ READ, DO NOT GREP — HONOURED, AND THE BATTERY REPORTED **ALONGSIDE** THE READ

⛔ **Every datum in §3 was obtained by READING the byte ranges in full, not by a term battery.** The battery is reported here because the brief requires it and because its result is itself the finding:

| Term | `a105.md` (188,770 B) | Truth |
|---|---|---|
| `antitype` | ⛔ **0** | ⛔ the material is present in bulk |
| `typolog-` | ⛔ **0** | ⛔ same |
| `prefigure` | ⛔ **0** | ⛔ same |
| `showbread` | 1 (`@62,243`) | ⚠️ plus `bread of the presence` ×3 (`@61,086`, `@61,293`, `@63,141`) — **a bare `showbread` grep under-reports by 3** |

⭐⭐ **A TERM SCAN OF THIS FILE FOR TYPE/ANTITYPE VOCABULARY RETURNS A FALSE ABSENCE, exactly as `260834-9`'s hand-off warned. He does the reasoning without any of its technical vocabulary — which is the identical shape `IP-90` independently recorded for the 2026-08-23 class.**

⭐ **WHAT THE READ DID CORROBORATE, offered as a check on `260834-6`'s battery rather than a replacement for it: all ten `incense` occurrences in `a105.md` were located and read in context — SEVEN in class 6 (`@62,853`, `@62,968`, `@63,227`, `@63,278`, `@63,340`, `@63,570`, `@63,598`) and THREE in class 7 (`@144,882`, `@147,942`, `@151,008`) — reproducing `260834-6`'s 7-and-3 counts exactly.**

## 3.D THE DEPTH SWEEP — RECORDINGS 1, 2 AND 5, ALL READ IN FULL

| Rec | His class | Bytes | `260834-7` class | Result |
|---|---|---|---|---|
| **1** | class 2 | `40`–`20,504` | ⚠️ Partially covered | ⛔ **NIL RETURN against the live questions, and it is reported as one.** `incense` **0** · `showbread` **0** · `tabernacle` **0**; no ceremonial-warrant and no fulfilment-rule material. Content (creatio ex nihilo, Gen 1:26, the imago Dei mandate, the family as first institution) **already held**. |
| **2** | class 3 | `20,505`–`52,549` | ⚠️ Partially covered | ⭐ **ONE datum** — Cain (§3.E). Everything else (baptism/apostasy, grafting, the thrown-ring image, the flood-as-baptism, the protoevangelium) **already held**. |
| **5** | class 4 | `105,803`–`139,614` | ⚠️ Partially covered | ⭐ **TWO worked types §17's method bullet does not name** (§3.F). Christus Victor, dispensationalism, Galatians 3 and Melchizedek all **already held**. |

⭐ **Reporting recording 1 as a nil return is deliberate.** A depth sweep that reports only its hits under-reports; the next pass needs to know this range was read and yielded nothing, so it is not read again.

## 3.E ⭐⭐ WRONG WORSHIP KILLS — AND THE FIRST WRONG OFFERING IN SCRIPTURE DRAWS NO PUNISHMENT

**[Stated, `AW-I` · File 41 `@19,541`–`@20,150`]:** *"If you look at how in the Old Testament he takes **great precision and care to command how his worship is done**… and **there are people who actually did do worship incorrectly and were judged and even killed for that**. So we need to take our worship seriously."* ⭐ He gives the stakes a mechanism: worship *"off in a significant way"* is *"orienting us **away** from God"*, on a wrong-motorway-exit analogy that compounds with time.

⛔⛔ **[Stated, File 43 `@38,700`–`@39,000`, his class 3]**, of Cain's rejected offering: ***"now, I want you to know something: in the passage God does not punish Cain for giving the wrong offering. There's no curse laid upon him, there's nothing like that that is done."*** The curse follows the **murder**.

⛔⛔ **NOT A CONTRADICTION AND EXPRESSLY NOT LOGGED AS ONE** — different cases (the Nadab-and-Abihu class vs. Cain), both readings ordinary. ⭐ **They are logged together because they are the corpus's only two statements on the CONSEQUENCE of wrongly-ordered worship and they run in opposite directions**, which is worth having in hand before any exchange leaning on how much is at stake in getting worship right. ⚠️ **A third sits between them: [Stated, File 43 `@150,998`] — his own example of the sin the GUILT offering covers is *"the using of the incorrect incense."*** ⛔ Recorded; no conclusion drawn in either direction.

## 3.F ⭐ TWO WORKED TYPES §17's METHOD BULLET DOES NOT NAME

**(i) The Binding of Isaac** **[Stated, File 43 `@132,803`–`@137,100`]** — five parallels given one by one: the father willing to sacrifice the son (Gen 22:2 / John 3:16); **Moriah** as the site of Jerusalem against Golgotha *"just outside"*; the wood on the son's back against Christ carrying the cross; the son's willing submission (he argues Isaac was an adult, *"as old as 37"*, not a child); the ram as substitute (Gen 22:13 / John 1:29 / 1 Pet 1:18-19); with *"God will provide himself a lamb"* as the hinge. ⚠️ He adds a Christological guard unprompted — the son submits *"according to his **human** will"*, because *"God has one divine will, God does not have three wills."* ⭐ `Binding of Isaac` **0** · `Aqedah` **0** · `Moriah` **0**.

**(ii) Babel undone at Pentecost** **[Stated, File 43 `@105,803`–`@107,700`]** — Acts 2 as *"the undoing in a sense of the Tower of Babel"*, distinguished sharply from *"what is understood as quote speaking in tongues today"*, which he calls *"almost the exact opposite."* ⭐ §17's method bullet names *"the rewinding of fall/flood/**Babel**"* but not the mechanism; `Tower of Babel` **0**.

⛔ **Neither is a new position.** Both are ordinary instances of the christotelic method §17 already records, and they are logged as **completing the type list**, not as changing it.

---

# 4. FILE 41 — THE REMAINING PRIORITY READS

## 4.A ⭐⭐ HEAVEN AND EARTH UNITED, GROUNDED ON THE **INCARNATION**, 2024

**[Stated, `AW-V` · File 41 `@130,384`–`@132,100`.]** Of the Sursum Corda: *"universal, and it goes back as far as we can see liturgically… in just about every liturgy in Holy Communion."* Then:

> ***"Heaven and Earth are united — that's the reality of the Incarnation, right. God becomes man, God enters into creation, so Heaven and Earth are brought together."***

He closes with the Sanctus, *"an Anthem… that points to the uh **saric** hymn heard by the prophet in Isaiah… and it's also repeated in Revelation 4 — I think it's Isaiah 6"* ⚠️ **quoted exactly as the ASR renders it: *"saric"* is an ASR corruption of *seraphic*; the corrected word is NOT written into the quotation, and `seraphic` is therefore **0** in the source as well as in the corpus.**

⭐⭐ **[Analysis] THE GROUND IS DIFFERENT AND THE DIFFERENCE IS THE POINT.** §13's escape-hatch note records the heaven-earth warrant from the 2025 Revelation class as ***earthly worship patterns itself on heavenly worship*** — a **pattern** claim, which that note itself observes is vulnerable to the apocalyptic-genre objection. ⭐⭐ **Here the same union is grounded on the INCARNATION — a union already accomplished in history — and that ground is immune to the fulfilment rule in the way the pattern ground is not, because the Incarnation is precisely what he says the Old Testament types pointed forward to.** ⛔⛔ **NOT logged as a change of mind and NOT as a replacement.** ⚠️ `heaven and earth are united` **0** · `seraphic` **0** across the corpus — ⛔ **and `seraphic` is 0 in the SOURCE too: the ASR renders the word *"saric"*, so the corrected spelling is deliberately not written into the quotation.**

## 4.B ⭐⭐ THE INCENSE PRACTICE HAS A DATED CONVERSION NARRATIVE

**[Stated, `Recon-Euch` · File 41 `@194,413`–`@194,930`, 2025]:**

> *"I love incense. I think it's an important part of worship. **I was, when I first was ordained, I was not so insistent upon incense as I am today** — to the gratitude of some of my first [parishioners] back in **California**. But as I was studying scripture, and as I was… looking into questions and theology of worship and all sorts of stuff, **I started getting convicted**, and sort of **the final nail in the coffin**, where I was like 'okay, we have to use incense, even if it's just a little bit,' **was Malachi 1:11.**"*

⭐ **AND THE WARRANT AS A THREE-LEGGED UNIT** (`@196,342`–`@197,025`): OT incense ***"that is never negated"*** · incense in ***"the worship, the perfect worship of heaven"*** · ***"the prophecy in Malachi."*** **[Analysis]** ⭐⭐ **The corpus has had the three legs; it has never had his own account of their ORDER OF FORCE.** He names Malachi 1:11 as **decisive** and the other two as standing background — the reverse of the weighting `260621-1` recorded when it corrected the *"Malachi demoted"* framing. ⭐ **It also dates the hardening of the practice to AFTER his first cure**, in his own characterisation rather than by inference. ⛔ **The parishioners are not identified and the California parish is not named further; nothing about third parties is carried.**

## 4.C ⭐⭐ §0 STANDING INSTRUCTION — AN `icons` HIT, AND §12's GAP IS REAFFIRMED ON NEW EVIDENCE

**[Stated, `Recon-Euch` · File 41 `@193,847`–`@194,060`, 2025]:** ***"There's a reason we do incense. There's a reason we have icons. There's a reason we have singing. There's a reason we have all these different actions — standing up, sitting down, kneeling… We are not brains on sticks."***

⭐⭐ **He then gives the reason for INCENSE at length (§4.B) and gives NO reason for icons at all — the sentence promises one and the class never returns to it.** §12's existing bullet records that `Icons` appears **three times, all in passing**, always inside the five-senses list, and that his theology of their devotional use is **not** established. ⛔⛔ **This is a FOURTH occurrence, from a different year, a different source and a fuller register, and it is the same shape. §12's gap is REAFFIRMED on new evidence rather than merely restated — and the bullet's *"three times"* count is left UNEDITED, with the fourth recorded as a dated note beside it.**

⭐ **`AW-I` `@17,500`-`@17,950` supplies a fifth, and it is the source of §12's own quoted list: *"sight — we see icons, we see scripture… the vestments, the altar… and then smell — the incense, even though some people don't like it."***

## 4.D ⭐ TWO DIFFERENT RATIONALES FOR FACING THE SAME DIRECTION

**[Stated, `AW-I` · File 41 `@28,900`–`@29,450`]:** *"even something as weird as the direction I'm facing — the whole reason I'm mostly facing the same way you all are is that **I am not the center of attention** here for the liturgy. I'm just the one in front line. We are all worshiping together in the same direction because we are all worshiping the same God."*

**[Stated, File 43 `@57,684`, his class 6]**, arising from the Tabernacle's **Eastern Gate**: *"we historically, the church has faced east when worshiping, right — **so we are looking for the expectation of Christ to come.**"*

⛔ **NOT logged as inconsistent** — a practice may carry more than one reason and he says so himself (*"a lot of liturgy is the pragmatics of it being turned into theological reasons"*, `Recon-Euch`, already on record). ⚠️ **But the second is an OT-derived rationale for a retained practice, produced inside the very session that argues against reviving uniquely-OT practice** — the shape §13 exists to watch. ⚠️ `facing east` · `faced east` · `direction I'm facing` all **0**; `ad orientem` occurs 26 times but never from these two sources.

---

# 5. ⛔⛔⛔ THE REJECTIONS — 32 CANDIDATE DATA REJECTED AS ALREADY HELD

**This is the number the brief asked for, and the check that produced it was run BEFORE any bullet was written.** Every pre-manifest citation line in `St_Francis_EMC_Distinctives.md` carrying `AW-`, `COT-`, `Ember`, `Recon-Euch` or `Lent vid` was extracted (94 lines) and read in full; each candidate datum from the reads was matched against it.

| # | Candidate | Already held at | Source |
|---|---|---|---|
| 1 | Regulative vs normative principle; the whole consistency argument | L1438 `[Stated, AW-I, Recon-Euch]` | AW-I |
| 2 | Incense/vestments/hymns/instruments as RPW counter-examples | L1438 | AW-I |
| 3 | Jesus at Hanukkah; synagogue worship unprescribed | L1438 | AW-I |
| 4 | *"A symbol doesn't work well if it's not there"* | L1438 · `RC3-8` | AW-I / Recon-Euch |
| 5 | Worship as duty before benefit | L1412 | AW-I |
| 6 | Whole-person worship, five senses, *"brains on sticks"* | L1413 | AW-I |
| 7 | Veneration of heroes, distinguished from worship; no dulia/latria | L1251 | AW-I |
| 8 | Perkins's four senses of Eucharistic sacrifice | L1008 | AW-I / AW-V |
| 9 | No re-sacrifice; the medieval side-altar private masses | L1007 | AW-I / AW-V |
| 10 | Entertainment-worship critique, Jesus Movement, church-shopping | L1413 · `RV-26` | AW-I |
| 11 | The *"it's not about us"* worship-leader anecdote | L1413 · `RV-26` | AW-I |
| 12 | *"Reformed Catholic"* self-identity, William Perkins | L421 | AW-I |
| 13 | Councils 1-6 invoked positively | L675 | AW-IV |
| 14 | Reverencing the altar; Ark analogy; Jeremy Taylor | L1070 | AW-IV |
| 15 | Bowing at the name of Jesus | L1254 | AW-IV |
| 16 | The Communion structure, Liturgy of the Word and Sacrament | L1669 | AW-IV / AW-V |
| 17 | Real substantial presence; bread and wine remain | L932 | AW-V |
| 18 | Two acceptable views; the Lutheran lean; Cranmer's movement | L933 | AW-V |
| 19 | Transubstantiation rejected (Art. 28) | L935 · `IP-74` | AW-V |
| 20 | Will not celebrate a private Mass | L1009 · L1716 | AW-V |
| 21 | Both kinds; never withholding the cup | L1715 · `IP-79` | AW-V |
| 22 | The epiclesis defended; the J. I. Packer anecdote | L1669 | AW-V |
| 23 | Elevation, bells, genuflection, reservation, ablutions, mixing | L1069 | Recon-Euch |
| 24 | Vestments and the maniple; the practical-plus-symbolic rationale | L1071 | Recon-Euch |
| 25 | *"A lot of liturgy is the pragmatics… turned into theological reasons"* | L1072 | Recon-Euch |
| 26 | *Creatio ex nihilo*; Genesis 1:26 as a Trinitarian hint | L2273 `[Stated, COT-1]` | File 43 rec 1 |
| 27 | Baptism objectively grafts; apostasy; the thrown-ring image | L871 `[Stated, COT-2]` | File 43 rec 2 |
| 28 | The type list: protoevangelium, flood-as-baptism, Passover, bronze serpent, Melchizedek, Moses, Joshua, David | L2271 `[Stated, COT-1 through COT-7]` | File 43, all |
| 29 | Christus Victor *"competitive with"* penal substitution | L784 `[Stated, COT-4]` | File 43 rec 5 |
| 30 | Dispensationalism *"heretical"*; Galatians 3; one people of God | L786 · L2272 | File 43 rec 5 |
| 31 | The *"priest friend"* / *"paganized"* datum | L2276 | File 43 rec 3 |
| 32 | ⭐⭐ **The showbread → Holy Communion CONCLUSION** | L2275 `[Stated, COT-3, COT-5, COT-6, COT-7]` | File 43 rec 3 |

⛔⛔ **REJECTION 32 IS THE ONE WORTH DWELLING ON, BECAUSE IT IS EXACTLY THE FAILURE THIS SEQUENCE WAS DESIGNED TO AVOID.** L2275 already records *"the showbread… read as foreshadowing Holy Communion."* ⭐ **A pass that read `File 43` recording 3 and minted "the showbread foreshadows Holy Communion" would have written the corpus's 141st citation of a datum it already held.** ⛔ **It was rejected.** ⭐⭐ **What was minted instead is what L2275 does NOT hold: the twelve loaves, the Friday reasoning, the priests' ceremonial eating, and — the item that matters — the incense on top of the bread.**

⚠️ **Three further data were read, judged genuinely new, and DECLINED as off-scope rather than minted:** the descent into Hades and the preaching to the spirits in prison (File 43 rec 2 `@45,705`, his stated position, *"well supported within the church history"*); the complementarian/egalitarian treatment (rec 1 `@13,640`); and the Pauline authorship of Hebrews with the pre-AD-70 dating argument (rec 3 `@73,550`). ⛔ **None bears on any live question, and minting on relevance alone would inflate §17 without serving anything. Recorded here so a later pass finds them rather than re-deriving them.**

---

# 6. ⛔ WHAT WAS MINTED, AND UNDER WHAT — THE PREFIX QUESTION IS RESERVED TO JD

**Eleven findings, all as SECTION BULLETS with byte-range citations.** ⭐ **That is the form this document has always carried `File 41`/`File 43` material in** — L1438, L1441, L2271-2276 are all bullets with `**[Stated, AW-I]**`-style citations, not numbered ledger entries — **now upgraded with the byte ranges `260834-9` made available for the first time.**

| Section | Items |
|---|---|
| **§13** | 8 — Malachi's *"pure offering"* = Christ; the silence-of-Acts reductio + the 2025 burden rule; the *"uniquely Old Testament"* qualifier; ritual act as divine pedagogy; the incense conversion narrative; the Incarnation-grounded heaven-earth union; the killed-for-wrong-worship / Cain-not-punished pair; the two ad-orientem rationales |
| **§17** | 3 — the six offerings mirrored onto the liturgy; the showbread teaching with the incense clause and the Leviticus 2 frankincense; the Aqedah and Babel-at-Pentecost types |
| **§12** | dated note — the fourth `icons` occurrence; gap REAFFIRMED, not closed |
| **`DQ-20`** | dated note — one clause of its `[Analysis]` qualified; ⛔ its own wording UNEDITED |

⛔⛔ **NO `LS`, `IP`, `RV`, `BLOG`, `POD`, `DQ`, `VP`, `DELTA`, `EXT`, `W` OR `File` NUMBER CONSUMED. Next-free values re-derived from the repo and unchanged: `DQ-25`, `IP-98`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EXT-4`, `W47`, `File 47`.**

⚠️⚠️ **AND THE DECISION BEHIND THAT, STATED SO IT CAN BE OVERTURNED CHEAPLY.** The `aNNN` class sources have **no numbered ledger** — `AW-` and `COT-` are *session ids*, not finding numbers. Giving them one, and choosing its prefix, is a convention decision with corpus-wide consequences (`C2`'s unbroken-range check, `C10`'s ledger-head arithmetic, and every downstream document's citation form all key off it). ⛔ **`260833-3` set the precedent that a prefix ruling belongs to JD and not to a pass, and it is followed here.** ⏳ **OWED AND FLAGGED, NOT ACTED ON.** ⭐ **If JD rules a prefix, these eleven convert to numbered entries mechanically — every one already carries its byte range, its attribution basis and its `[Stated]`/`[Analysis]` label.**

---

# 7. ✅ VALIDATOR AFTER, AND THE FULL BEFORE/AFTER DIFF

```
80 ok · 9 warnings · 0 errors
```

⭐ **IDENTICAL HEADLINE TO THE BEFORE RUN — same count, same nine codes, in the same order.** ⛔⛔ **THE BEFORE CAPTURE WAS PRODUCED WITHOUT ANY INDEX-WRITING GIT COMMAND**, on the `260834-9` method: the working tree was copied to a scratch directory (excluding `.git`) and the three touched files restored with `git show HEAD:<path>`, which is read-only. **No `git stash` was attempted.**

**Exactly three substantive lines differ, and every one is an `ok` line reporting a value this pass deliberately changed:**

```
38c38
<   ok    [C3] PROJECT_STATE.md: version agrees with registry (260834-9)
---
>   ok    [C3] PROJECT_STATE.md: version agrees with registry (260835-1)
41c41
<   ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260834-5)
---
>   ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260835-1)
48c48
<   ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260834-9)
---
>   ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260835-1)
```

*(A fourth diff line, `2c2`, is the header's `root:` path and is an artifact of the scratch-copy method, not a change to the repo.)*

⭐ **`ok` before and `ok` after on all three. No warning appeared, none disappeared, no error was introduced in the final state.**

## 7.1 ⚠️⚠️ AN ERROR **WAS** INTRODUCED MID-PASS AND FIXED — REPORTED, NOT HIDDEN

**A `C8` ERROR fired on the first AFTER run, taking the validator to `79 ok · 9 warnings · 1 errors`:**

```
ERROR [C8] DANGLING VP- LABELS cited but never DEFINED in St_Francis_EMC_Distinctives.md:
{'VP-8': ['PROJECT_STATE.md']}
```

**Cause, diagnosed at source rather than guessed:** `C8`'s `VP-` arm skips a `VP-N` token when its line matches `NEXT_FREE_MARK = re.compile(r'next free', re.I)` — a **space**, not a hyphen. The `260834-9` pass note survives this check only because the *same line* happens to contain the unrelated string *"NEXT FREE FILE NUMBER IS NOW `File 47`"*. This pass's note listed `VP-8` in a next-free enumeration written **hyphenated throughout**, so nothing on the line matched, and `VP-8` was scored as a **citation** of a pair that does not exist.

**Fix:** the enumeration was rephrased to *"the **next free** value for every prefix…"*. ⛔ **`validate_project.py` was NOT modified, and no `VP-` pair was created to satisfy the check.** ⚠️⚠️ **The underlying fragility is REPORTED, not fixed: `C8`'s skip depends on an unhyphenated spelling that this project's own prose uses inconsistently, and `260834-9` passes it by coincidence rather than by construction.** ⏳ **Widening the pattern to `next[- ]free` is a one-character-class change to the validator; it is OWED and deliberately not made — `validate_project.py` is registry-tracked at `260812-1` and editing it is not this pass's brief.**

## 7.2 ⚠️⚠️ THE BRIEF EXPECTED `C11` TO MOVE FURTHER OUT OF DATE. **IT DID NOT.**

The brief states: *"expect `C11` to move further out of date, which is correct."* ⛔ **`C11` is byte-for-byte unchanged** — still *"outline last checked against `DQ-19`… the DQ ledger now runs to `DQ-24`. 5 finding(s) unreviewed."*

⭐ **The reason is structural and is reported rather than reconciled: `C11`'s drift arithmetic keys off the `DQ`, `IP` and `RV` LEDGER HEADS, and this pass consumed no ledger number** (§6). **Eleven findings entered the corpus and the outline's drift counter cannot see any of them.** ⚠️⚠️ **THAT IS ITSELF A DEFECT WORTH RECORDING: `C11` measures outline staleness against numbered ledgers only, so the entire `AW-`/`COT-`/`A101-`/`ANF-`/`Misc-2025` half of the corpus is invisible to it. The `Incense_Conversational_Outline.md` review is now MORE out of date than before this pass and the validator says otherwise.** ⛔ **REPORTED, NOT FIXED. `Incense_Conversational_Outline.md` was NOT touched, as the brief requires, and the C11 review remains a separate pass — which should read §13's `260835-1` block before it runs.**

---

# 8. `git status --short`, IN FULL

```
 M PROJECT_STATE.md
 M SRC_Channel_Inventory.md
 M St_Francis_EMC_Distinctives.md
?? passes/260835-1_files-41-43-targeted-mining_pass-b1.diff
?? passes/260835-1_files-41-43-targeted-mining_pass-b1_close-out.md
?? passes/260835-1_files-41-43-targeted-mining_pass-b1_raw-session-output.md
warning: unable to unlink '/…/EMC/theology/.git/index.lock': Operation not permitted
```

⛔ **Complete and unabridged — six status entries plus the warning git emitted after them, nothing elided.** ⚠️⚠️ **The seventh line is NOT a status entry: it is the `.git/index.lock` condition firing (see §0.2). The command's exit code was 0 and its status output is correct and complete.** `ls -la .git/*.lock` immediately after returns `-rw------- … 0 Aug 26 2026 .git/index.lock`.

⚠️ **An earlier, mid-pass `git status --short` — taken after all three tracked files were edited but before the `passes/` artifacts were written — returned the three `M` lines alone, at exit 0, with NO unlink warning and NO lock on disk. Both captures are recorded; they are not reconciled.**

⛔ **`git rev-parse HEAD` after all writes still returns `48012843bc3aee71b64d86323e2c38ed5c3ac24e` — HEAD did not move and NOTHING WAS COMMITTED BY THIS PASS.**

## What to stage

**All five, in one commit:**

```
git add PROJECT_STATE.md \
        St_Francis_EMC_Distinctives.md \
        SRC_Channel_Inventory.md \
        passes/260835-1_files-41-43-targeted-mining_pass-b1.diff \
        passes/260835-1_files-41-43-targeted-mining_pass-b1_close-out.md \
        passes/260835-1_files-41-43-targeted-mining_pass-b1_raw-session-output.md
```

Suggested message: `260835-1: Files 41/43 targeted mining (Pass B1) — Malachi's "pure offering" answered as Christ in 2024, falsifying RJ_Incense_Analysis §4.6's unknown premise; ritual-act-as-pedagogy as a third ceremonial warrant; the "uniquely Old Testament" qualifier; the six Levitical offerings mirrored onto the 1928 ordo; showbread shown to be his own teaching, incense and all; 32 data rejected as already held; no ledger number consumed`

⚠️ **The `.diff` was generated BEFORE this close-out existed, so it contains the three tracked-file changes and not itself or this file. That is the same shape every prior pass's `.diff` has.**

---

# 9. WHAT THIS PASS DID NOT DO, STATED EXPLICITLY

⛔ **No `LS`, `IP`, `RV`, `DQ`, `BLOG`, `POD`, `VP`, `DELTA`, `EXT`, `W` or `File` number consumed.** `IP-98` was re-derived fresh and left free.

⛔ **No existing tag renumbered, re-pointed, corrected or merged.** `AW-`, `COT-`, `Ember`, `Recon-Euch`, `Lent vid`, `A101-`, `ANF-`, `Misc-2025` all stand exactly as written.

⛔⛔ **`COT-n` was NOT used as a locator anywhere in this pass, and no `COT-n` → byte-range mapping was written.** It remains the registered unresolved defect `260834-7` §4.4 established and `260834-9` registered. ⏳ Still owed.

⛔⛔ **No source text was attributed to Rev. James on a basis that was not recorded.** Every `File 43` datum carries an **EXTERNAL** attribution basis (`a105.md`: 0 name strings in 188,770 bytes, `>>` = 0). The `File 41` recording-9 material is recorded as sitting **outside all 38 unlabelled `>>` turns**, with the marker offsets (`@198,611`/`@198,618`) given so the claim is checkable rather than asserted. ⛔ **Nothing from any `>>` turn was attributed to him.**

⛔ **No boundary reading adopted.** The `a101-2` `151,803` boundary keeps both readings live. `AW-VI` was not read this pass and is untouched.

⛔ **No error corrected in any downstream document.** Reported and left standing: `RJ_Incense_Analysis.md` §4.6/§4.8/§4.10's falsified *"unknown"* premise; §4.13's Leviticus 2 frankincense recorded as project research rather than his teaching; `C8`'s hyphen fragility; `C11`'s blindness to un-numbered findings.

⛔ **`DQ-9` not moved. `IP-84` neither confirmed nor extended. `OQ8` SHARPENED and NOT MOVED. `OQ20`, `OQ21`, `DQ-24` untouched. The element/circumstance question logged with a third non-instance and NOT resolved.** No gate, no channel state, no `VP-` pair, no `DELTA`, no register entry, no hash or byte offset altered in any registry.

⛔⛔ **`Incense_Conversational_Outline.md` NOT TOUCHED** — the C11 review is a separate pass and this one does not pre-empt it. ⛔ **`RJ_Incense_Analysis.md`, `On_Incense_and_the_Altar.md`, `RJ_Final_Question_List.md`, `RJ_Open_Questions_and_Divergences.md`, `SRC_Manifest.md`, `ORCHESTRATION.md`, `validate_project.py` NOT TOUCHED.**

⛔ **Nothing drafted, altered, or posted to Rev. James.**

⛔ **`SRC_Coverage_Register.md` NOT created** — clause 1 of `ORCHESTRATION.md` §8's standing instruction remains owed and not actionable, exactly as `260834-7` and `260834-9` recorded.

**Touched three tracked files** (`St_Francis_EMC_Distinctives.md`, `SRC_Channel_Inventory.md`, `PROJECT_STATE.md`) **plus three new `passes/` artifacts.**

---

# 10. HAND-OFF

| Priority | Item | Why |
|---|---|---|
| **1** | ⭐⭐⭐ **Rewrite `RJ_Incense_Analysis.md` §4.6/§4.8/§4.10** | Its lead internal lever rests on a premise this pass falsified. **The reformulated seam is set out at §1.2 and is sharper than the one on file.** ⛔ Not this pass's to write. |
| **2** | ⭐⭐ **The C11 outline review** | Now MORE out of date than the validator can see (§7.2). **It should read §13's `260835-1` block first** — three of the eight items bear directly on the outline's incense argument. |
| **3** | ⭐⭐ **The `aNNN` prefix ruling** | Reserved to JD. Eleven findings are ready to convert mechanically if a prefix is given (§6). |
| **4** | ⭐ **`OQ8`'s next form** | Must now clear the *"uniquely Old Testament"* qualifier (§2.3) **and** reach warrant (iii), ritual act as divine pedagogy (§2.2), which neither standing objection touches. |
| **5** | **First mining of Files 45 and 46** | 388,321 B, 26.5 % of the scope set, still unmined. `a202` gated behind diarization. Unchanged from `260834-9`'s hand-off. |
| **6** | **`ORCHESTRATION.md`: fix the stamp roll-over rule** | `260834` reached `-9` and there is no convention for what follows (§0.3). One line. |
| **7** | **`validate_project.py`: `next[- ]free`** | `C8`'s skip is hyphen-fragile and `260834-9` passes it by coincidence (§7.1). One character class. |

⭐⭐ **AND ONE THING THIS PASS WANTS ON THE RECORD FOR WHOEVER MINES FILES 40 AND 42.** ⛔ **The single most valuable item found here — the Malachi *"pure offering"* gloss — sits 8 KB from a passage the corpus mined years ago, in a recording classified `Covered` with 7 of 10 deciles occupied and 16 live citations.** ⚠️⚠️ **`Covered` means *cited*, not *exhausted*. `260834-7` said so explicitly (its classification rests on "the material a citation describes lies in this range", never on "the range has been read"), and this pass is the empirical demonstration. **Do not read a `Covered` classification as a reason to skip a range.**
