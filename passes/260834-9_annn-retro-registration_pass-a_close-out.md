# 260834-9 — RETRO-REGISTRATION OF THE PRE-MANIFEST `aNNN` SOURCES (PASS A: REGISTRATION ONLY)

**Last updated: 260834-9.** ⛔⛔ **SEVEN SOURCES REGISTERED AS `File 40`…`File 46`. NO FINDING MINTED · NO `LS`, `IP`, `RV`, `BLOG`, `POD` OR `DQ` NUMBER CONSUMED.** `File` numbers are the only numbers this pass consumed.

> ⭐ **BOTH THE DIFF AND THE RAW SESSION OUTPUT ARE TOO LARGE FOR CHAT AND ARE WRITTEN TO `passes/`, AS THE BRIEF DIRECTS.** The complete `git diff` — 586 lines, 150,584 bytes across three files — is at **`passes/260834-9_annn-retro-registration_pass-a.diff`**. The complete raw session output, unsummarized — gate, stamp derivation, the full BEFORE and AFTER validator runs and their diff, every hash and byte/line/delimiter count, every `^==` offset, every byte-offset probe, the seven `a105` recording openings, the `a103` recording-3 class-number probe, and the close-out git state — is at **`passes/260834-9_annn-retro-registration_pass-a_raw-session-output.md`** (603 lines, 38,353 bytes). This close-out carries the gate, the reasoning, the verification and the decisions. *(§5 rule 11 — this note makes no claim about its own commit state.)*

---

## ✅ GATE

| Check | Expected | Observed | Result |
|---|---|---|---|
| `git rev-parse HEAD` | `d536711` | `d536711471c0eed96cd67072f33a1a8c321ca15c` | ✅ **MATCH** |
| Branch | — | `main` | — |
| `git status --short` before first write | — | *(empty, exit 0)* | ✅ **CLEAN** |
| `.git/*.lock` at gate | ⚠️ briefed as recurring across five consecutive passes | ⭐ **ABSENT** — `ls -la .git/*.lock` returned nothing | ✅ **no lock at gate** |
| `validate_project.py` BEFORE | derive | **`80 ok · 9 warnings · 0 errors`** | ✅ recorded |
| `PROJECT_STATE.md` stamp | report | **`260834-8`** (created `260724-3`) | ✅ reported |
| Next-free pass stamp | derive by repo-wide grep | **`260834-9`** | ✅ **DERIVED AND VERIFIED FREE** |

### Every firing code, recorded individually (9 warnings, 0 errors)

1. **`WARN [C1]`** `src/SRC_Discord_RPW.md`: 2 relative timestamp(s) outside message headers (`'Yesterday at …'`). Not caught by the header rule; check whether they are quoted text or unresolved captures.
2. **`WARN [C3]`** `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md`: no parseable `'Last updated'` stamp; registry says `'260832-2'`.
3. **`WARN [C3]`** `tools/transcribe_yt.py`: no parseable `'Last updated'` stamp; registry says `'260833-7'`.
4. **`WARN [C4]`** `St_Francis_EMC_Distinctives.md`: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby. Review manually.
5. **`WARN [C5]`** `RJ_Final_Question_List.md`: 17 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
6. **`WARN [C5]`** `RJ_Incense_Analysis.md`: 9 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
7. **`WARN [C5]`** `St_Francis_EMC_Distinctives.md`: 7 volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.
8. **`WARN [C10]`** §15's newest LS citation is 8 findings behind the ledger (`LS-120` vs `LS-128`). Sweep the interval for creditable material.
9. **`WARN [C11]`** outline last checked against `DQ-19` (`260833-1`); the DQ ledger now runs to `DQ-24`. 5 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.

**Identical set and order to `260834-6`, `260834-7` and `260834-8`'s BEFORE runs.**

### Stamp derivation

`grep -rhoE '26[0-9]{4}-[0-9]+'` across the whole repo returns a highest stamp of **`260834-8`**. **`260834-9` returns ZERO hits anywhere in the repo**, and `260835-` returns **zero** as well. **`260834-9` is genuinely free.**

### ⚠️⚠️ THE `.git` LOCK — REPORTED, NOT WORKED AROUND, AND IT RECURRED FOR A FOURTH CONSECUTIVE PASS

| Moment | Command | Result |
|---|---|---|
| **Gate** | `ls -la .git/*.lock` | ⭐ *(nothing)* — **no lock present** |
| **Gate** | `git status --short` | clean, exit 0, no warning emitted |
| **Mid-pass** | `git stash push -q -m tmpcheck` — attempted **once**, to produce a clean-tree validator BEFORE run | ⛔⛔ **FAILED SILENTLY.** No stash was created (`git stash list` empty afterwards), and the three modified files were confirmed intact by `git status --short` immediately after |
| **Mid-pass** | `ls -la .git/*.lock` | ⚠️ **`-rw------- … 0 Aug 26 01:00 .git/index.lock`** — zero-byte lock present |
| **Close-out** | `git status --short`, `git diff` | ✅ both ran normally, exit 0, correct output, **no unlink warning emitted this time** |

⛔⛔ **NO WORKAROUND WAS APPLIED.** The lock was **not** force-removed, its permissions were **not** changed, `.git` was not touched by any other means, and **the failed `git stash push` was NOT retried.** ⚠️ **Reported rather than worked around, exactly as the brief requires — and it changed this pass's method rather than being routed around:** the clean-tree validator BEFORE run was instead produced **without git**, by copying the working tree (minus `.git`) to a scratch directory and restoring the three pre-edit file states from copies taken before the first edit. **That reproduces the BEFORE output with no git write of any kind.**

⭐ **ONE OBSERVATION THAT REFINES `260834-6`/`260834-7`'s DIAGNOSIS, OFFERED AS OBSERVATION AND NOT CONCLUSION.** Those passes recorded *absent at gate, present at close-out* and could not identify the trigger, naming a dirty working tree as a candidate. **This pass narrows it slightly: the lock appeared at the moment of an INDEX-WRITING command (`git stash push`), not at a read-only `git status`.** Read-only plumbing was unaffected throughout — `git rev-parse HEAD` returned `d536711471c0eed96cd67072f33a1a8c321ca15c` before and after the lock appeared, and `git diff` and `git status` both ran correctly with the lock in place. ⛔ **This is a narrowing, not a diagnosis, and no conclusion is drawn.**

⚠️⚠️ **THE CONSEQUENCE FOR WHOEVER STAGES THIS PASS: `git add`/`git commit` may fail on `.git/index.lock`. Do NOT force-remove it. The fix belongs to whoever owns the filesystem permissions on `.git/`, not to a pass.**

---

## 1. WHAT THIS PASS DID — AND THE ONE THING IT REFUSED TO DO

**Seven sources retro-registered on the `260813-1` Files 8-9 precedent**, which was read directly and whose shape was matched: *material mined before the manifest existed gets File numbers, hashes, byte counts, byte ranges and session rows without re-mining and without renumbering any existing tag.*

| File | Source | Bytes | Recordings | Pre-manifest prefix | Coverage (`260834-7`) |
|---|---|---|---|---|---|
| **40** | `a101-1.txt` | 256,209 | 8 | `A101-I…VIII` | 3 Covered · 5 Partially covered |
| **41** | `a101-2.md` | 263,995 | 10 | `AW-I…VI` · `Ember` · `Recon-Euch` · `Lent vid` | ⭐ **10 of 10 Covered** |
| **42** | `a103.md` | 259,190 | ⭐ **9, not 8** | `ANF-1..9` | 7 Covered · 2 Partially covered |
| **43** | `a105.md` | 188,770 | 7 | `COT-1..7` ⚠️ **index unresolved** | 4 Covered · 3 Partially covered |
| **44** | `a106.md` | 80,482 | ⭐ **3, not 6** | `Misc-2025` | 3 Covered |
| **45** | `a201.txt` | 177,254 | 9 | ⛔ **none** | ⛔ **9 Uncovered** |
| **46** | `a202.txt` | 211,170 | 4 | ⛔ **none** | ⛔ **4 Uncovered** |

**Registered per file:** SHA-256 in **both documented conventions**, byte count, line count, `==` count, recording count, per-recording byte ranges, video provenance, attribution class. **Registered per recording:** **31 session rows** (Anglican 101 ×8, Anglican Worship ×7, Ante-Nicene ×9, Christ-in-the-OT ×7) and **19 standalone rows** (three `a101-2` topical videos, three `a106` sessions, thirteen `a201`/`a202` recordings).

⛔⛔⛔ **AND THE REFUSAL: THIS PASS MINTED NOTHING.** No finding. No `LS`, `IP`, `RV`, `BLOG`, `POD` or `DQ` number. **Next-free values are unchanged and were re-checked rather than assumed: `DQ-25`, `IP-98`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EXT-4`, `W47`.** ⭐ **Several things he says in these files are plainly finding-weight** — 15 `regulative` hits in one worship session, the only four `showbread` occurrences in the scope set, 20 `incense` hits in the Instructed Eucharist, Noah Edmonds's own words from the debate File 33 characterizes secondhand. ⛔ **None of it is recorded as a finding. That is Pass B's job and it is noted here and left alone.**

⛔ **`St_Francis_EMC_Distinctives.md` was NOT touched, and neither were `Incense_Conversational_Outline.md`, `RJ_Incense_Analysis.md` or `St_Francis_EMC_Distinctives.md`'s named companions.** ⛔ **Nothing drafted, altered, or posted to Rev. James.**

---

## 2. HASHES, BYTE COUNTS AND THE HASHING CONVENTION

⭐ **All values computed from the source files this pass, not copied from any prior document.** ⭐⭐ **Every byte count independently reproduces `260834-6`'s figure exactly** — which is what made it safe to *verify* that pass's byte ranges rather than re-derive them.

| File | Source | Raw `sha256` (full) | Raw bytes | `sha256(body.strip())` | Stripped bytes | Δ |
|---|---|---|---|---|---|---|
| 40 | `a101-1.txt` | `11ebced26d71d6beee81ab1f81dfcbc60d9bd4c17e7566a0220f29858781c0c1` | 256,209 | `a37b29335a00e2eff25e690cab05217b5cf90d97ab3cba957beafc63e098f9a3` | 256,208 | 1 |
| 41 | `a101-2.md` | `3123ee648c84587fda1398ffd5fa2b2c8a236313fd2cf605dbe2bf773a696703` | 263,995 | `1f93d159708520c86628c6b37f47726ac195d2c9e17af4581ad1e285e665e632` | 263,994 | 1 |
| 42 | `a103.md` | `a46887b1ad065f3accf3dd5cdc5b5ff5fb03bedd0347a508e8734a4021378cd5` | 259,190 | `0774d0c24e40d97dfbd4d7bbd395f931ae3010525b725828f913a0b1787f928a` | 259,189 | 1 |
| 43 | `a105.md` | `555640c60bc5695781d25917c2ed17ca7e5cfaba61e223e378b98b0b80529fc9` | 188,770 | `491090b53b8cc8a874425e9160c897625942cc0732f11fc884cf54b886daf411` | 188,769 | 1 |
| 44 | `a106.md` | `aade40a2231481c9de7cd5e843400f13994de60c24109cb497d2652f35a3eabd` | 80,482 | ⭐ `aade40a2231481c9de7cd5e843400f13994de60c24109cb497d2652f35a3eabd` | 80,482 | ⭐ **0** |
| 45 | `a201.txt` | `09a24f927df0eb39ee2704f351e2a1e97bbc30178e6dc9b214ffdaf24a9c07c8` | 177,254 | `77f1fcbc7717db61e9a784d82fa65c126933712b08a220c63eff42c84c2d4683` | 177,250 | ⚠️ **4** |
| 46 | `a202.txt` | `5fdcafeb0ff6a2fd3424387e2250e212fa614ee84e329431b4609394a86be8a2` | 211,170 | `c413de80bd68478d60a71aef4854eecf8a8a8e780532705972751db9c6befa58` | 211,169 | 1 |
| — | `a301-Classical-Theism.md` ⛔ **rejected** | `3551973355aa3518ca877f1d3e9de56ade8e560025d3fa19c3712b8e7bd56585` | 29,338 | ⭐ *identical* | 29,338 | ⭐ **0** |

⛔⛔ **WHICH CONVENTION APPLIES, RECORDED SO IT IS NOT GUESSED: THE RAW HASH IS THE VALUE OF RECORD FOR ALL SEVEN**, on the Files 8-9 precedent, because every byte range in this registration is absolute against the file **as delivered**. ⭐ **The strip values are recorded for cross-convention comparison only** — this manifest documents both, and **a raw check against a strip-convention row produces a false mismatch.**

⚠️⚠️ **FILE 44 IS THE TRAP AND IS FLAGGED FOR IT IN THE MANIFEST.** Its two values are **identical**, because `a106.md` carries no leading or trailing whitespace at all. **A pass that verifies File 44 under either convention and concludes the conventions agree in general will then apply that conclusion to File 45, whose values differ by four bytes.** ⚠️ **File 45's four-byte delta is the largest in the set and is trailing whitespace, not content.**

⭐ **`a301`'s raw hash is NEW and differs from File 44's** — so **a hash-keyed intake passes the duplicate file.** That is why the disposition below is a registry decision and not a hash check.

---

## 3. THE FIVE FINDINGS THAT HAD TO TRAVEL — AND HOW EACH WAS REGISTERED

### 3.1 ⛔⛔ The `a101-2` recording 6/7 boundary at byte `151,803` — REGISTERED AS A CONTENT BOUNDARY, BOTH READINGS LIVE

**Registered:** two session rows, `AW-SessionVI-Pt1` (`139,748`-`151,802`) and `AW-SessionVI-Pt2` (`151,803`-`160,769`). ⛔ **The CONTENT boundary is registered and is not in doubt — no material is lost or double-counted either way.** ⛔⛔ **What is NOT registered is whether it is a RECORDING boundary.**

- **(i) One recording, split by a capture artifact** — recording 7 opens mid-sentence with no collect, greeting or restart marker.
- **(ii) Two recordings, Session VI Pt 1 and Pt 2** — ⭐ **better supported**, on two `EXT-3` channel rows (`9UDQhvMdkNA` 916 s, `38BYTZzLmxg` 663 s, both 2024-11-23) and a byte ratio 1.34 against a duration ratio 1.38. ⛔ **DELIBERATELY NOT ADOPTED.**

⛔ **`260834-7` tested it and it did not discriminate:** `AW-VI` citations fall on **both** sides carrying **different** material, which is what **both** readings predict.

⚠️⚠️ **AND THE `260834-8` PRECEDENT IS RECORDED BESIDE THE ROWS, IN THE DIRECTION MOST LIKELY TO BE GOT WRONG.** For Files 8-9 the **file boundary turned out NOT to be the Pt 1/Pt 2 video cut** — it was a mid-sentence content cut carrying none of the dismissal-plus-greeting signature every confirmed session boundary in those files shows. ⛔ **So the existence of two Pt 1/Pt 2 videos here does NOT establish that this transcript's `==` boundary falls at the video cut, and the manifest says so explicitly.** ⏳ **The audio, or the two videos, remain the thing to check.**

⭐ **One thing this pass adds on its own evidence: UPLOAD ORDER IS NOT SESSION ORDER IN THIS SERIES.** Session V uploaded **2024-11-26**, three days **after** Session VI Pt 1 and Pt 2 (**2024-11-23**). **His spoken session numbers govern; the channel's dates do not.**

### 3.2 ⛔⛔ `a103.md` — NINE RECORDINGS REGISTERED AGAINST A LEGEND THAT SAYS EIGHT

**Registered:** nine session rows, `ANF-Class1`…`ANF-Class9`. ⛔ **The legend defect is REPORTED and NOT silently fixed** — the `ANF` legend row says *"teaching class, **8 sessions**"* while **its own range field says `ANF-1..9`.** **The range is right and the count is wrong**, confirmed from the file side (`260834-6`) and independently from the citation side (`260834-7`, nine distinct live ids). ⛔ **`St_Francis_EMC_Distinctives.md` was not edited; the defect is logged at `PROJECT_STATE.md` §7.**

⛔⛔⛔ **FIREWALL SET AT INTAKE — recordings 4, 5 and 7 (89,894 B, 34.7% of the file) are guest lectures by Dr. Stephen Boyce, Kevin Valdez and Tyler West with NO MARKED RETURN.** Each opens with Rev. James's collect and handoff and then runs to the end of its segment in the guest's voice, and the file carries no diarization outside recording 9's 19 `>>` markers. **NO QUOTATION FROM `91,064`-`124,285`, `124,286`-`149,041` OR `177,046`-`205,246` MAY BE ATTRIBUTED TO REV. JAMES** — the same firewall the `LS` interview files carry, applied at intake rather than after a correction.

⚠️⚠️ **A SECOND `ANF` DEFECT IS CARRIED FORWARD AND FLAGGED FOR RESOLUTION BEFORE ANY MINTING: §16 CONTRADICTS ITSELF OVER WHO TAUGHT SESSION 7.** Its preamble lists session 7 among *"RJ's own teaching"*; nineteen lines later the same section says *"West's framing, not RJ's."* **RJ's own sessions are 1, 2, 3, 6, 8, 9 — six, not seven.** ⛔ **Reported, not corrected.**

### 3.3 ⛔⛔ `a106.md` recording 2 — REGISTERED AS JUNE 2026; RECORDINGS 1 AND 3 AS GENUINELY 2025

**Six independent supports, zero contrary evidence beyond the container banner:**

1. `a301-Classical-Theism.md`'s own header, **`### Jun 6, 2026`** — preserved verbatim in the manifest.
2. `SRC_Channel_Inventory.md` row `gEDpnwg2tF0`, *"Classical Theism (for Trinity Sunday)"*, uploaded **2026-06-07**.
3-5. Three *"twelve years earlier"* arithmetic statements in the findings corpus (L768, L1843, L5763) against `BLOG-81`/`W20`, firmly dated **2014-07-19** → **2026** — ⭐ **and all three are anchored on the sunbeam-on-wax-and-clay analogy, which this pass re-located at `a106.md` @35,981 and which occurs in recording 2 and NOWHERE ELSE in the file.**
6. The corpus's own changelog: *"**v0.3 (2026-06-13):** Integrated Batch 3 (`Misc-2025`)"* — **six or seven days AFTER the header date and the channel row.**

⭐ **And `260834-7` found no live citation stating 2025 as a fact.** The year is **inside the tag string itself** — the prefix is `Misc-2025`, not `Misc` — so all 14 live citations *carry* 2025 by construction without any of them *asserting* it. ⛔⛔ **A worse trap than `Rev`'s: `Rev`'s year could be omitted; this one cannot be written without being asserted, or corrected without renaming the prefix.**

⛔⛔ **THE CORRECTION IS SCOPED TO RECORDING 2 ALONE.** Recording 1 is **genuinely 2025** — `5mU3CdbXjOQ`, 2025-06-18, and the tape asks *"who can tell me what today is other than Sunday? **Trinity Sunday**"*, with Trinity Sunday 2025 falling **2025-06-15**, three days before the upload. Recording 3 is **genuinely 2025** — `hlEGpBC3Vj4`, 2025-12-31. ⛔ **A blanket re-date would be as wrong as the current label.** ⛔ **The Source ID Legend's wrong year is REPORTED, not corrected** (logged at §7).

⚠️ **`Misc-1..7` is additionally a DEAD RANGE:** the only `Misc-N` token anywhere in the findings corpus is the string `Misc-1` inside the legend row itself. **No citation-level machinery exists to re-point.**

### 3.4 ⭐⭐ `a106.md` — THREE RECORDINGS, NOT SIX

**Registered as three standalone rows.** The file uses a **two-line `==` convention**: each recording opens with `==<Title>` on its own line, then `==<transcript>`. **Counting `==` lines gives 6; counting recordings gives 3.** ⭐ **Verified this pass by re-listing the `^==` offsets: `22, 48, 18442, 18461, 47772, 47840` — three title/body pairs.** ⛔ **A boundary-detection amendment recording this convention (and the other three in this set) was added to the manifest's boundary-detection section so it is not re-learned.**

⛔⛔ **FIREWALL: recording 3 (Gregory Bronson, `47,840`-`80,481`, 32,642 B = 40.6% of the file) is guest-taught throughout**, self-identified at **@48,231**.

### 3.5 ⛔⛔ `a201.txt` AND `a202.txt` — REGISTERED, AND EVERY RECORDING MARKED **REGISTERED BUT UNMINED**

**Thirteen standalone rows, each carrying the explicit marker `⛔ NONE — REGISTERED BUT UNMINED`**, and the channel decision cells reading **`FINDING RANGE PENDING PASS B`**. ⭐ **The marker is the point: it tells Pass B it is doing a FIRST MINING of 388,321 bytes — 26.5% of the scope set — not a depth sweep.**

**`260834-7` established this by title-probe across three documents:** `Matt Kennedy`, `Canterbury Cousins`, `Simply Anglican`, `Stories We Tell`, `Evan Minton` and `Monarch of England` all return **0** in the findings corpus; the apparent hits on `Memorialist`, `Contemporary Worship`, `Apostolicae`, `John 6:63` and `John Fisher` were each read in context and belong elsewhere.

⛔⛔⛔ **DIARIZATION PREREQUISITES RECORDED ON THE ROWS:** `a201` recording 1 (Fr Matt Kennedy, two voices, `>>` = 0, ⛔ **opens in the guest's voice**) and `a202` recordings 1-2 (three speakers each, `>>` = 0 across all 211,170 bytes, 175,745 B combined — **the highest-risk material in the scope set**).

---

## 4. THE `COT-n` DECISION — WHY NO READING WAS PICKED

⛔⛔ **`260834-7` established that `COT-n` is not a reliable index into `a105.md` under either the positional or the class-number reading. This pass registered that as an UNRESOLVED KNOWN DEFECT beside the rows and did NOT pick a reading.**

| Citation | Cited content located in | Positional reading | Class-number reading |
|---|---|---|---|
| `COT-1` | rec 1 (his class 2) | ✅ | ⛔ class 1 — **absent from the file** |
| `COT-2` | rec 2 (his class 3) | ✅ | ⛔ zero hits |
| `COT-4` | rec 5 (his class 4) | ⛔ zero hits | ✅ |
| `COT-7` | rec 6 (his class 7) | ⛔ zero hits | ✅ |
| `COT-3` **+** `COT-6` | ⭐ **ONE location, `@75,897`-`75,955`, rec 3** | one resolves, one does not | one resolves, one does not |
| `COT-6` | rec 3 (his class 6) | ⛔ | ✅ |
| `COT-5` | ⛔⛔ **SPLIT across rec 4 and rec 5** | half | the other half |

⛔ **A forced mapping would be worse than the gap.** Under the positional reading it would mark recordings 4 and 7 as carrying Christus Victor and Melchizedek material **they demonstrably do not contain**, telling a later pass those ranges are mined when they are not.

⭐⭐ **WHAT WAS REGISTERED INSTEAD: byte ranges as the authoritative locator, and session-row ids carrying HIS OWN SPOKEN CLASS NUMBERS** — `COT-Class2`, `COT-Class3`, `COT-Class6`, `COT-Class5`, `COT-Class4`, `COT-Class7`, `COT-Class9`, **in that file order**, each re-verified against the tape this pass:

- rec 1 @`40`: *"that collect is the second Sunday after Epiphany I chose it because the theme… **class two session two** in Christ in the Old Testament"*
- rec 2 @`20,505`: *"this morning we are on **class three** of Christ in the Old Testament"*
- rec 3 @`52,550`: *"today we have the **sixth class**… now we're moving on into specifically the **Tabernacle and the presence of God**"*
- rec 4 @`76,108`: *"this morning we have **class five**… this one is titled **Jesus the greater Moses**"*
- rec 5 @`105,803`: *"this is **class four** now we are speaking about… the promise to Abraham"*
- rec 6 @`139,615`: *"we are on **session 7** now… the **levitical sacrifices**… and how they point to Christ"*
- rec 7 @`165,439`: *"so **class number nine** — **Jesus as the son of David**"*

⛔ **No `COT-n` tag was renumbered or re-pointed** — rule 1 forbids it and `260813-1`'s precedent is explicit. ⏳ **A `COT-n` → byte-range mapping table is OWED and deliberately not written: writing it requires deciding the reading, which this pass may not do.**

⚠️⚠️ **THE SAME CAUTION IS REGISTERED FOR EVERY OTHER PRE-MANIFEST PREFIX.** The index is **VERIFIED** for `A101-I…VIII` (roman numeral = session number = file order, checked for all eight) and for `ANF-1..9` (positional, corroborated at six independent points). It is **NOT verified** for `COT-`. It **does not exist at all** for `Misc-2025`.

⚠️⚠️ **AND A SEPARATE `a105` FLAG TRAVELS WITH EVERY ROW: THE FILE ESTABLISHES NO SPEAKER AT ALL.** Zero name strings in 188,770 bytes; `>>` = 0. **The legend's `COT` = *"RJ (all)"* does not come from this file.** ⭐ There is equally no positive evidence of a second voice — the risk is an *unestablished single speaker*, not misattribution. **Recorded at registration, as `260834-6` required.**

---

## 5. VIDEO PROVENANCE — 51 RECORDINGS MAPPED, EVERY MATCH VERIFIED, TWO REPORTED AS NOT HOLDING

**Method: two independent tests per match, and content verification before writing.** (a) **Title/number/guest-name agreement** against `SRC_Channel_Inventory.md`; (b) **byte-rate consistency** — transcript bytes ÷ video duration, checked against the file's own spread rather than an absolute threshold. ⛔ **Where a match rested on only one leg, it is recorded as a candidate and not as established.**

| File | Series | Matches | Byte-rate range | Verdict |
|---|---|---|---|---|
| 40 | Anglican 101 2024 | 8 / 8, **verbatim title match on every one** | 12.6-15.0 B/s | ✅ **all hold** |
| 41 | Anglican Worship | 7 / 7 series + Ember + Lent, verbatim title match | 13.1-15.1 B/s | ✅ **all hold** |
| 41 | Instructed Eucharist | ⚠️ **1 candidate** (`C2tCMfq-_hI`) | 14.3 B/s | ⚠️ **EVIDENCED, NOT ESTABLISHED** |
| 42 | Ante-Nicene | 9 / 9, title numbers and guest names both matching | 13.7-15.4 B/s, ⚠️ **rec 7 at 17.0** | ✅ **all hold**; one rate outlier reported |
| 43 | Christ in the OT | 6 / 7 on explicit title numbers | 12.2-13.4 B/s | ⛔ **1 UNRESOLVED** (`PEGUfE6Y2LA`) |
| 44 | Miscellaneous | 3 / 3, titles match the file's own `==` title lines | 12.1-14.3 B/s | ✅ **all hold** |
| 45 | `a201` batch AA | 9 / 9 on verbatim titles | 13.0-14.6, ⚠️ **rec 7 at 11.2** | ✅ **all hold**; one rate outlier reported |
| 46 | `a202` batch BB | 4 / 4 on verbatim titles | 14.0-16.2 | ✅ **all hold**; ⭐ the two debates agree with each other at 16.0/16.2 |

### ⛔ THE TWO THAT DO NOT HOLD, REPORTED RATHER THAN FORCED

**(a) `PEGUfE6Y2LA` (*"Christ in the Old Testament"*, 2024-12-01, 1643 s) — UNRESOLVED, and the decision cell records the ambiguity rather than `INGESTED`.**

- **Reading (a): it is class 2**, matching File 43 recording 1 (`40`-`20,504`). Supported by **elimination** — it is the only unnumbered COT video on the channel and class 2 is the only `a105` class with no numbered channel row — and by **rate**, 20,465 B / 1,643 s = 12.5 B/s, inside the file's own 12.2-13.4 spread.
- **Reading (b): it is class 1**, which `a105.md` does not contain. ⭐ **An unnumbered title is exactly what a series OPENER gets**, and recording 1's own opening — *"class two session two… we're going to start at the very beginning"* — implies a class 1 that was an introduction rather than exposition.
- ⛔ **The rate test cannot separate them: a class-1 video would fall in the same range.** **Left unmarked, on the Files 11/12 precedent** (`260833-8` left those blank rather than force-matching against conflicting numbering). ⏳ **One look at the video closes it.**

**(b) `C2tCMfq-_hI` (*"What We Believe About Worship and Holy Communion"*, 2025-09-23, 5685 s) — CANDIDATE for File 41 recording 9, EVIDENCED BUT NOT ESTABLISHED.**

Three legs, **none a verbatim title match**: (i) it is the **only** `EXT-3` video long enough — every other non-`Anglican Class` row on that channel runs ≤ 3,011 s against this recording's 81,247 bytes; (ii) subject match — the recording reads its own handout aloud as *"How we worship: instruction on holy communion according to the 1928 US book of common prayer"*; (iii) rate 14.3 B/s, inside the file's own spread. ⚠️ **Leg (iii) is named as weak in the record: any video of adequate length passes it.**

⭐⭐ **AND IF IT HOLDS IT CARRIES A CONTAINER CONSEQUENCE, REGISTERED IN ITS OWN RIGHT: `a101-2.md` IS NOT A 2024 FILE.** Its banner reads *"1 year ago - Anglican Worship series"*; seven of ten recordings are the 2024 series, **but recording 9 is 2025-09-23 and recording 10 is 2026-02-18 in his own voice.** **The file spans roughly seventeen months and its banner describes only its first seven recordings** — the same shape as `a106`'s false banner, in a milder form.

### ⭐ ONE VIDEO EXPLICITLY RECORDED AS **NOT** TO BE INGESTED

`x0hfBI6w6f0` (*"Debate: Is Apostolicae Curae Correct? (Opening Statements Only)"*, 2020-08-28, 2,483 s) is an **opening-statements-only partial of the same event as `MLCh-d15F_o`**, which is registered as File 46 recording 1. ⛔ **Ingesting both would double-log one debate.** Its decision cell records the ruling so a later pass finds the decision rather than the video.

### ⚠️ TWO CORRECTIONS OF RECORD TO `260834-6`, BOTH ON EVIDENCE, NEITHER EDITED INTO THAT PASS'S OWN WORDING

1. ⭐⭐ **`a103.md` recording 3's class number IS stated.** `260834-6` reports it as *"(number not stated in the opening…)"*. The tape reads: *"**This is class three.** We are going over um this will be a two-part uh sort of series within this class uh **defending the faith**… This is **part one for defending the faith as indicated by the title.**"* ⭐ **This closes recording 3's numbering from the tape rather than from the channel, and independently confirms the channel row `yP3OdU7NBrA` *"Class III: Christians Defending the Faith, Part 1"*** — which recording 6 then completes (*"class number six… this is **defending the faith part two**"*).
2. **Offset calibration:** the Gregory Bronson self-introduction measures at **@48,231** with `grep -ob`, not `260834-6`'s **@48,439**. **The recomputed value is registered.**

⚠️ **A third, smaller observation is recorded rather than smoothed: `a103` recording 7 is a byte-rate outlier at 17.0 B/s against the file's 13.7-15.4 range.** Its title/guest match is exact (the channel names Tyler West and the tape names Tyler West), **but the rate anomaly is reported because rate consistency was one of the two tests this pass used to accept matches, and a reader should see where it did not hold.**

---

## 6. `a301-Classical-Theism.md` — REJECTED RE-SUPPLY, HEADER PRESERVED

⛔⛔ **NOT REGISTERED. NO `File` NUMBER, NO SESSION ROW, NO STANDALONE ROW, NO FINDING TAG.** Recorded in `SRC_Manifest.md` as a **rejected re-supply on the `a304` disposition pattern** (`SRC_Manifest.md:287`'s block, the second instance of the same shape).

**The evidence, carried from `260834-6` and not re-derived:** it is `a106.md` bytes `18,461`-`47,771` — a **29,261-character longest common run** out of 29,329, `difflib.quick_ratio` **0.9992**, **identical `>>` counts (33 vs 33)**, identical tail to the final character. ⛔ **The `a303` two-engine reading is excluded outright: two ASR engines do not agree on 29,261 consecutive characters.**

⭐⭐⭐ **ITS HEADER IS PRESERVED VERBATIM IN THE RECORD, AND THAT IS WHY IT IS RECORDED RATHER THAN DISMISSED:**

```
# Classical Theism
## Classical Theism (for Trinity Sunday)
### Jun 6, 2026
```

⛔ **`### Jun 6, 2026` is the ONLY internal witness that `a106.md`'s `St Francis Misc 2025` banner is false** — the only dated header in any of the eight files `260834-6` triaged. **A bare deletion would destroy the witness and leave the false banner unfalsifiable.**

---

## 7. `SRC_Channel_Inventory.md` — 51 DECISION CELLS FILLED, PER THE `260834-7` STANDING INSTRUCTION

`ORCHESTRATION.md` §8's standing instruction (added `260834-7`) requires every intake or retro-registration pass to update the channel inventory's decision cell for each video it covers, with the File number and finding range. **51 cells filled**, each recording the **File number, the session/standalone row, the byte range**, and — since nothing was minted — **explicitly** that the finding range is **PRE-EXISTING** (five mined files, naming the pre-manifest tag) or **PENDING PASS B** (`a201`/`a202`).

| Channel | Rows updated | Class |
|---|---|---|
| `EXT-3` | 8 | Anglican 101 2024 → File 40 |
| `EXT-3` | 10 | Anglican Worship + Ember + Lent + the Instructed Eucharist candidate → File 41 |
| `EXT-3` | 9 | Ante-Nicene → File 42 |
| `EXT-3` | 7 | Christ in the OT → File 43 *(⛔ one of them recording an UNRESOLVED match, not `INGESTED`)* |
| `EXT-3` | 3 | Miscellaneous → File 44 |
| `EXT-2` | 9 | `a201` → File 45, all **UNMINED** |
| `EXT-2` | 4 | `a202` → File 46, all **UNMINED** |
| `EXT-2` | 1 | `x0hfBI6w6f0` — ⛔ **NOT to be ingested** |

⛔ **Clause 1 of that standing instruction — `SRC_Coverage_Register.md` — remains OWED and NOT actionable: the file still does not exist on disk, exactly as `260834-7` recorded. ⛔ No stub, placeholder or registry row was created for it by this pass.**

---

## 8. ✅ VALIDATOR AFTER, AND THE FULL BEFORE/AFTER DIFF

```
80 ok · 9 warnings · 0 errors
```

⭐ **IDENTICAL HEADLINE TO THE BEFORE RUN — same count, same nine codes, in the same order.** The full output was diffed line by line against a BEFORE capture. ⛔⛔ **THE BEFORE CAPTURE WAS PRODUCED WITHOUT GIT** — the working tree was copied to a scratch directory (excluding `.git`) and the three pre-edit file states restored from copies taken before this pass's first edit — **because the one `git stash push` attempted for that purpose failed on the lock and was NOT retried.**

**Exactly five lines differ, and every one is an `ok` line reporting a value this pass deliberately changed:**

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

⭐ **`ok` before and `ok` after on all five. No warning appeared, none disappeared, no error was introduced.**

### ⭐⭐ C12's HEADLINE MOVED, AND THE FIGURES ARE PUBLISHED RATHER THAN LEFT TO BE DISCOVERED

**`43 → 74` capture rows across `33 → 64` sessions; `8 → 27` standalone rows. The delta is `+31 rows / +31 sessions / +19 standalone` — exactly the rows written, and checkable against §1 above.** ⚠️ **The `260826-4` precedent is followed deliberately: that pass built a version of the C12 pollution defect and caught it only by comparing the row count against `HEAD`, and its own lesson was that *an unpublished count is how this survived a full pass in the first place.***

⛔⛔ **AND THE `260826-4` DOCUMENTATION RULE WAS FOLLOWED RATHER THAN CITED: no supporting or comparison table added to `# Sessions Ingested` by this pass carries a capture code.** Every `[S]` written this pass sits in a genuine session row or a genuine standalone row; all evidence, reasoning and calibration material inside that section is prose or bullets. **The +31/+31/+19 delta is the proof — a single stray capture code in a prose table would have shown up as an extra row or an extra phantom session, and none did.**

⚠️ **The pre-existing C12 pollution (`Window test`, `Terminus`, `a303 vs [R]`, `[R] vs [S]`, `3-gram coverage by [R] vs by [S]`, `[SW] vs [SY] (Note 2d)`, `The six [S]-only OPENING markers`, `✅ CONFIRMED`-class rows) is UNTOUCHED and still counted — it remains the open defect `260826-4` registered at §7, and this pass neither fixed nor extended it.**

---

## 9. `git status --short`, IN FULL

```
 M PROJECT_STATE.md
 M SRC_Channel_Inventory.md
 M SRC_Manifest.md
?? passes/260834-9_annn-retro-registration_pass-a.diff
?? passes/260834-9_annn-retro-registration_pass-a_close-out.md
?? passes/260834-9_annn-retro-registration_pass-a_raw-session-output.md
```

⛔ **Complete and unabridged — six entries, nothing elided.** ⭐ **No `unable to unlink` warning was emitted by the closing `git status`, unlike `260834-6` and `260834-7`'s close-outs — but `.git/index.lock` IS present on disk** (`-rw------- … 0 Aug 26 01:00 .git/index.lock`), having appeared at the failed `git stash push` earlier in the pass. **Both facts are recorded; neither is reconciled.**

⛔ **`git rev-parse HEAD` after all writes still returns `d536711471c0eed96cd67072f33a1a8c321ca15c` — HEAD did not move and NOTHING WAS COMMITTED BY THIS PASS.**

### What to stage

**All six, in one commit:**

```
git add PROJECT_STATE.md \
        SRC_Manifest.md \
        SRC_Channel_Inventory.md \
        passes/260834-9_annn-retro-registration_pass-a.diff \
        passes/260834-9_annn-retro-registration_pass-a_close-out.md \
        passes/260834-9_annn-retro-registration_pass-a_raw-session-output.md
```

Suggested message: `260834-9: retro-register the pre-manifest aNNN sources as Files 40-46 (Pass A, registration only; nothing minted)`

⚠️⚠️ **IF `git add` FAILS ON `.git/index.lock`, THAT IS THE BRIEFED FILESYSTEM CONDITION AND NOT A FAULT IN THESE FILES. DO NOT FORCE-REMOVE THE LOCK.** The fix belongs to whoever owns the permissions on `.git/`.

⚠️ **The `.diff` was generated BEFORE this close-out existed**, so it contains the three tracked-file changes and not itself or this file. That is the same shape every prior pass's `.diff` has.

---

## 10. WHAT THIS PASS DID NOT DO, STATED EXPLICITLY

⛔ **No finding minted. No `LS`, `IP`, `RV`, `DQ`, `BLOG`, `POD`, `VP`, `DELTA`, `EXT` or `W` number consumed** — next-free values are **`DQ-25`**, **`IP-98`**, **`LS-129`**, **`RV-64`**, **`BLOG-159`**, **`POD-17`**, **`VP-8`**, **`EXT-4`**, **`W47`**, all unchanged. ⭐ **The only numbers consumed are `File 40`…`File 46`; next free is `File 47`.**

⛔ **No source re-mined and no source read for theological content.** Source text was opened only to verify structure, locate strings by byte offset, confirm class numbers spoken on the tape and check speaker establishment. ⛔ **What he argues in these files is not characterised anywhere in this pass.**

⛔ **No existing tag renumbered, re-pointed, corrected or merged.** `A101-`, `AW-`, `Ember`, `Recon-Euch`, `Lent vid`, `ANF-`, `COT-` and `Misc-2025` all stand exactly as written.

⛔ **No boundary reading adopted** — the `a101-2` `151,803` boundary keeps both readings live, as `260834-6` and `260834-7` left it.

⛔ **No error corrected in `St_Francis_EMC_Distinctives.md`.** Six defects are **reported and left standing**: the `ANF` legend's *"8 sessions"*; §16's session-7 attribution contradiction; the `Misc-2025` banner year; the dead `Misc-1..7` range; the `AW-VI`/Aristotle citation; the `AW-VI`/meat-and-dairy attribution.

⛔ **`DQ-9` not moved. `IP-84` neither confirmed nor extended. `OQ8`, `OQ20`, `OQ21` and `DQ-24` untouched. The element/circumstance question is exactly where `260834-5`, `260834-6` and `260834-7` left it.** ⛔ **No gate, no channel state, no `VP-` pair, no `DELTA`, no register entry.**

⛔ **`Incense_Conversational_Outline.md`, `RJ_Incense_Analysis.md`, `St_Francis_EMC_Distinctives.md`, `On_Incense_and_the_Altar.md`, `RJ_Final_Question_List.md` and `RJ_Open_Questions_and_Divergences.md` NOT TOUCHED.** C11's drift is reported as firing code 9 and left standing.

⛔ **Nothing drafted, altered, or posted to Rev. James.**

⛔ **`SRC_Coverage_Register.md` NOT created.**

⛔ **No git write attempted after the single failed `git stash push`, and that failure was not worked around.**

**Touched three tracked files** (`SRC_Manifest.md`, `SRC_Channel_Inventory.md`, `PROJECT_STATE.md`) **plus two new `passes/` artifacts.**

---

## 11. HAND-OFF TO PASS B

| Order | File | State after this pass | What Pass B faces |
|---|---|---|---|
| 1 | **File 41** `a101-2.md` | ✅ registered, 0 uncovered bytes | ⭐ **Minting only.** AW-IV and AW-V complete and byte-bounded; AW-I is the richest single segment (15 `regulative`); the Instructed Eucharist is the largest recording and the densest `incense` concentration. ⛔ Recording 9's 38 unlabelled `>>` turns are unattributable pending audio |
| 2 | **File 43** `a105.md` | ✅ registered, 0 uncovered bytes | ⭐⭐⭐ **The only `showbread` in the scope set, all four hits in `52,550`-`76,107`.** ⛔⛔ **READ, DO NOT GREP: `antitype`/`typolog-` return ZERO while the material is present in bulk.** ⚠️ Depth sweep owed on recordings 1, 2 and 5. ⛔ Speaker not established from the file |
| 3 | **File 40** `a101-1.txt` | ✅ registered | Cleanest file; Session VI (*"Scripture (and Tradition)"*) is the most on-point material for `DQ-24`/`OQ21`. Depth sweep owed on 5 of 8 |
| 4 | **File 46** `a202.txt` | ✅ registered, ⛔ **UNMINED** | ⛔⛔ **FIRST MINING of 211,119 B, gated behind diarized audio for 83.2% of it.** ⭐ Recording 2 is the primary record of the debate File 33 recaps secondhand |
| 5 | **File 42** `a103.md` | ✅ registered as NINE | ⛔⛔ **Resolve §16's session-7 attribution contradiction FIRST.** Recordings 4, 5, 7 firewalled. Depth sweep owed on 1 and 2 |
| 6 | **File 45** `a201.txt` | ✅ registered, ⛔ **UNMINED** | ⛔⛔ **FIRST MINING of 177,202 B.** Recordings 2-9 solo and safe; recording 1 gated behind diarization |
| 7 | **File 44** `a106.md` | ✅ registered as THREE, rec 2 dated 2026 | Lowest yield. ⚠️ The `Misc-2025` prefix rename is a separate decision — a prefix whose NAME is a date claim, with no `Misc-n` machinery to re-point |
| — | `a301` | ⛔ **rejected re-supply, header preserved** | Nothing owed |

⭐⭐ **AND ONE RESEQUENCING QUESTION IS LEFT OPEN FOR JD RATHER THAN DECIDED, EXACTLY AS `260834-7` LEFT IT.** `260834-6` ranked `a201` and `a202` 6th and 4th on the assumption they were already mined. **They are not, and they are 26.5% of the scope set.** Whether *"already in the ledger"* or *"not in the ledger at all"* should drive the order **is JD's call, not a pass's** — recorded so the choice is made knowingly.
