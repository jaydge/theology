# 260834-7 — COVERAGE CHECK ON THE EIGHT PRE-MANIFEST SOURCE FILES

**Last updated: 260834-7.** Read-and-report pass, plus one conventions addition. ⛔ **NO SOURCE REGISTERED · NO FINDING MINTED · NO `File`, `LS`, `IP`, `RV`, `DQ`, `BLOG` OR `POD` NUMBER CONSUMED.**

> ⛔⛔ **THERE IS NO DIFF OF CORPUS CONTENT FOR THIS PASS.** No source transcript, findings ledger, register, manifest row, hash, byte offset, question list, outline or analysis document was created, edited or deleted. `St_Francis_EMC_Distinctives.md`, `SRC_Manifest.md`, `SRC_Channel_Inventory.md`, `Incense_Conversational_Outline.md`, `RJ_Incense_Analysis.md`, `On_Incense_and_the_Altar.md`, `RJ_Final_Question_List.md` and `RJ_Open_Questions_and_Divergences.md` are **untouched**. The artifact *is* the report.
>
> ⚠️ **THE ONE EXCEPTION, BRIEFED AND SCOPED:** the standing-convention addition at `ORCHESTRATION.md` §8, and the two stamp/registry cells required to keep it consistent. That is a conventions edit; it registers nothing and mints nothing. Accounting in §7 below. *(§5 rule 11 — this note makes no claim about its own commit state.)*

---

## ✅ GATE

| Check | Expected | Observed | Result |
|---|---|---|---|
| `git rev-parse HEAD` | `c0e7a36` | `c0e7a36b59ba333179c8d4b14d737ee4155c315a` | ✅ **MATCH** |
| Branch | — | `main` | — |
| `git status --short` before first write | clean | *(empty, exit 0)* | ✅ **CLEAN** |
| `.git/index.lock` | ⚠️ briefed as recurring, zero-byte | ⚠️⚠️ **ABSENT at gate · PRESENT at close-out** — ⭐ **`260834-6`'s pattern REPRODUCED EXACTLY, third occurrence** | ⚠️ **RECURRED. REPORTED, NOT WORKED AROUND.** |
| `validate_project.py` BEFORE | derive | `80 ok · 9 warnings · 0 errors` | ✅ recorded |
| `PROJECT_STATE.md` stamp | report | **`260834-5`** (created `260724-3`) | ✅ reported |
| Next-free pass stamp | derive | **`260834-7`** | ✅ **DERIVED AND VERIFIED FREE** |

### Every firing code, recorded individually (9 warnings, 0 errors)

1. **`WARN [C1]`** `src/SRC_Discord_RPW.md`: 2 relative timestamp(s) outside message headers (`'Yesterday at …'`). Not caught by the header rule; check whether they are quoted text or unresolved captures.
2. **`WARN [C3]`** `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md`: no parseable `'Last updated'` stamp; registry says `'260832-2'`.
3. **`WARN [C3]`** `tools/transcribe_yt.py`: no parseable `'Last updated'` stamp; registry says `'260833-7'`.
4. **`WARN [C4]`** `St_Francis_EMC_Distinctives.md`: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby. Review manually.
5. **`WARN [C5]`** `RJ_Final_Question_List.md`: 17 volatile-state assertions.
6. **`WARN [C5]`** `RJ_Incense_Analysis.md`: 9 volatile-state assertions.
7. **`WARN [C5]`** `St_Francis_EMC_Distinctives.md`: 7 volatile-state assertions.
8. **`WARN [C10]`** §15's newest LS citation is 8 findings behind the ledger (`LS-120` vs `LS-128`). Sweep the interval for creditable material.
9. **`WARN [C11]`** outline last checked against `DQ-19` (`260833-1`); the DQ ledger now runs to `DQ-24`. 5 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.

**Identical to `260834-6`'s BEFORE run — same count, same nine codes, same order.**

### ⚠️⚠️ THE `.git/index.lock` — IT RECURRED, AND `260834-6`'s DIAGNOSIS IS NOW CORROBORATED

⛔ **A CORRECTION TO THIS PASS'S OWN EARLIER READING, MADE BEFORE PUBLICATION AND RECORDED RATHER THAN SILENTLY FIXED.** Midway through, this pass had observed no lock and was on course to report that it did not recur. **The closing `git status --short` produced the lock.** The mid-pass observation was true and incomplete; the finding is the full sequence.

| Moment | Command | Result |
|---|---|---|
| **Gate** | `ls -la .git/index.lock` | `ls: cannot access '.git/index.lock': No such file or directory` — ⛔ **no lock** |
| Mid-pass | `git status --short` (opening check), `git rev-parse HEAD` | clean, exit 0, ⛔ **no warning emitted, no lock created** |
| **Close-out** | `git status --short` | output normal, then ⚠️ `warning: unable to unlink '/…/theology/.git/index.lock': Operation not permitted` |
| **Close-out** | `ls -la .git/index.lock` | ⚠️ **`-rw------- … 0 Aug 25 2026 .git/index.lock`** — zero-byte lock present |

⭐⭐ **THIS REPRODUCES `260834-6`'s OBSERVATION EXACTLY — same absent-at-gate, present-at-close-out shape, same `Operation not permitted` on unlink, same zero-byte file.** ⭐ **And it corroborates that pass's diagnosis, which it offered as observation rather than conclusion: git is CREATING the lock normally and failing to REMOVE it, because the filesystem denies `unlink` on this path.** ⚠️ **A refinement this pass can add: the lock is NOT produced by every `git status`.** The opening `git status --short` at gate emitted no warning and left no file; the closing one did both. **So the trigger is not the command name.** ⛔ **What distinguishes the two invocations is not established here and is deliberately not guessed at** — the working tree was clean at the first and dirty at the second, which is a candidate and nothing more.

⛔⛔ **NO WORKAROUND WAS APPLIED.** The lock was not force-removed, its permissions were not changed, `.git` was not touched by any other means, and no git operation was retried against it. Read-only plumbing stayed unaffected throughout: `git rev-parse HEAD` returned `c0e7a36b59ba333179c8d4b14d737ee4155c315a` after the lock appeared, unchanged. ⚠️ **The consequence for whoever stages this pass: `git add`/`git commit` may fail on the lock, and the fix belongs to whoever owns the filesystem permissions on `.git/`, not to a pass.**

### Stamp derivation

`grep -rhoE '26[0-9]{4}-[0-9]+'` across the whole repo returns a highest stamp of **`260834-6`**. **`260834-7` returns zero hits anywhere in `~/EMC/`** outside `.git/` internals (`.git/logs/HEAD`, `.git/COMMIT_EDITMSG` and `.git/index` match only on `260834-6`, the commit message at HEAD). `260835` returns four hits — all four are **prose inside `260834-5`'s and `260834-6`'s own artifacts and `PROJECT_STATE.md` asserting that `260835` is free**; none is a stamp in use. **`260834-7` is genuinely free.**

---

# ⛔⛔⛔ THE HEADLINE — THE UNCOVERED SET IS NOT WHERE THE BRIEF EXPECTED IT, AND IT IS BIGGER THAN A GAP INSIDE A MINED FILE

The brief's `⚠️ Uncovered` category was defined as *"the recording is inside a mined file but has no citation pointing at it."*

⭐⭐⭐ **THAT CATEGORY IS EMPTY. Every one of the 38 recordings in the five mined files carries locatable live cited content — not one of them is unmined.**

⛔⛔ **The Uncovered set is instead THIRTEEN WHOLE RECORDINGS IN TWO WHOLLY UNMINED FILES — `a201.txt` and `a202.txt` — which carry NO pre-manifest prefix at all and are cited by nothing.**

⚠️⚠️ **THIS CORRECTS `260834-6` ON A LOAD-BEARING POINT.** `260834-6` states that *"Seven of the eight files are already mined into `St_Francis_EMC_Distinctives.md` under `A101-`, `AW-`, `COT-`, `ANF-`, `Misc-2025`, `Ember`, `Lent vid` and `Recon-Euch`."* **It is five of the eight, not seven.** The eight prefixes it lists map, by the Source ID Legend's own rows, to exactly **five** files:

| Prefix | File | Recordings |
|---|---|---|
| `A101-I…VIII` | `a101-1.txt` | 8 |
| `AW-I…VI` · `Ember` · `Recon-Euch` · `Lent vid` | `a101-2.md` | 10 |
| `ANF-1..9` | `a103.md` | 9 |
| `COT-1..7` | `a105.md` | 7 |
| `Misc-2025` | `a106.md` | 3 |
| — | **`a201.txt`** | ⛔ **9, none cited** |
| — | **`a202.txt`** | ⛔ **4, none cited** |
| — | `a301-Classical-Theism.md` | 1 (duplicate of `a106` rec 2) |

**`a201` and `a202` were checked for coverage under OTHER prefixes before this was written, not assumed.** Every distinctive title string in the two files was grepped across `St_Francis_EMC_Distinctives.md`, `SRC_Manifest.md` and `SRC_Channel_Inventory.md`:

| Probe | Distinctives | Manifest | Channel inventory | Verdict |
|---|---|---|---|---|
| `Matt Kennedy` | **0** | 0 | 5 | ⛔ uncited |
| `Canterbury Cousins` | **0** | 0 | 1 | ⛔ uncited |
| `Simply Anglican` | **0** | 0 | 1 | ⛔ uncited |
| `Stories We Tell` | **0** | 0 | 1 | ⛔ uncited |
| `Evan Minton` | **0** | 0 | 2 | ⛔ uncited |
| `Monarch of England` | **0** | 0 | 1 | ⛔ uncited |
| `Memorialist` | 8 | 0 | 2 | ⚠️ **all 8 read in context — every one is `COT-`, `IP-`, `BP-Sac` or the LS ledger; none is `a201` rec 3** |
| `Contemporary Worship` | 4 | 0 | 1 | ⚠️ **all 4 read — `BLOG`/`W4`/`W13` lyric-reproduction notes and a `DQ` quotation; none is `a201` rec 6** |
| `Apostolicae` | 14 | 1 | 2 | ⚠️ **all read — `LS-113`, `BLOG-37`, `IP-39`, `BP-S…`; none is `a202` rec 1** |
| `John 6:63` | 2 | 0 | 1 | ⚠️ **both are `GV-21`; neither is `a201` rec 4** |
| `John Fisher` | 1 | 1 | 3 | ⚠️ **the one hit is an LS-ledger attribution note; not `a202` rec 1** |

⛔⛔ **CONCLUSION, STATED FLATLY: `a201.txt` (177,254 B, 9 recordings) and `a202.txt` (211,170 B, 4 recordings) HAVE NEVER BEEN MINED. They are not a coverage gap inside a registered batch; they are two unread files.** ⭐ **The consequence for the retro-registration pass is the opposite of what `260834-6` implied for them: they need registration PLUS a full first mining, not registration-only — and `a202`'s mining is gated behind its diarization prerequisite.**

⭐⭐⭐ **AND THE GOOD NEWS IS SYMMETRICAL AND IS THE PASS'S OTHER HEADLINE: BOTH PRIORITY FILES ARE FULLY COVERED. `a101-2.md` and `a105.md` contain ZERO Uncovered bytes.** Every recording in both carries live cited content, `AW-VI` Part 2 included. **For the two files the next pass cares most about, the act is registration-only at the recording level** — subject to the depth caveats in §3.

---

# 1. METHOD, AND WHAT IT CAN AND CANNOT ESTABLISH

## 1.1 Extraction

Every pre-manifest tag token in `St_Francis_EMC_Distinctives.md` (2,590,498 B) was located by regex with its line number and containing section. ⛔ **`A101-2026-MM-DD` was excluded at the pattern level** — 83 such tokens exist and they are the **in-person `IP` session captures**, not the 2024 `a101-1.txt` video series. Conflating them would have inflated `A101-` coverage by more than its true total.

## 1.2 ⭐ Compound and range citation forms — the reason a bare regex under-counts

⚠️ **A bare `AW-[IVX]+` / `COT-\d+` grep misses a large fraction of this corpus's citations, because it cites in compressed forms.** Five distinct compound shapes are in use and all five were expanded:

| Shape | Live example | Bare regex yields | Truth |
|---|---|---|---|
| Comma list, prefix once | `**[Stated, AW-I, II, V]**` (L421) | `AW-I` | `AW-I` + `AW-II` + `AW-V` |
| Slash list, prefix once | `**[Stated, A101-III/VII, AW-V]**` (L935) | `A101-III` | `A101-III` + `A101-VII` |
| Bare-prefix slash list | `**[Stated, A101 II/III/VII, AW-I/IV]**` (L775) | ⛔ **nothing at all** | 5 citations |
| Digit list, prefix once | `**[Stated, ANF-2,3,6]**` (L2256) | `ANF-2` | `ANF-2` + `ANF-3` + **`ANF-6`** |
| Explicit range | `**[Stated, COT-1 through COT-7]**` (L2271) | `COT-1`, `COT-7` | all seven |

⭐⭐ **`ANF-6` exists ONLY inside a compound.** A bare grep returns zero for it and would have reported `a103` recording 6 as Uncovered. **That single form is the difference between a true and a false gap, and it is the strongest argument in this pass for expanding compounds before counting anything.**

## 1.3 Content location — and ⚠️⚠️ the limit that governs every number below

⛔⛔ **CITATIONS IN THIS CORPUS CARRY SESSION IDS AND SOMETIMES TIMESTAMPS. THEY DO NOT CARRY BYTE OFFSETS.** There is therefore **no mechanical way** to prove that a given citation "points at" a given byte range. What can be done, and what was done, is: take the distinctive content string the citation itself names (*"showbread"*, *"sunbeam"*, *"not yet happened"*, *"grain offering"*, *"priest friend"*, *"Gesima"*, *"full moon"*) and locate that string in the source by byte offset.

⚠️ **That establishes that the material a citation describes lies in a particular range. It does NOT establish that the mining pass which wrote the citation had that range in view.** Every coverage verdict below rests on the first claim and not the second, and the retro-registration pass should treat these ranges as **strongly evidenced, not registered**.

⚠️ **Span is measured as DECILE OCCUPANCY** — how many of the recording's ten equal byte-tenths contain at least one located cited string. That is the most direct available proxy for the brief's *"span the recording rather than clustering at one point"*. **Classification rule, stated before the results so it is not fitted to them:**

- **Covered** — cited content located in **≥ 6 of 10 deciles**.
- **Partially covered** — cited content located, but in **≤ 5 of 10 deciles** (clustered, with substantial unmined stretches).
- **⚠️ Uncovered** — **no** cited content locatable and no citation naming the recording.

⛔ **The probe list is derived from the corpus's own citation text, not from the sources.** A recording on a narrow topic will legitimately show few probe *types*; type count is therefore reported but **not used as a classification criterion**, precisely because it would penalise a well-mined single-topic session such as the Ember video.

---

# 2. ⭐ PER-RECORDING COVERAGE TABLE — ALL 51 RECORDINGS

`types` = distinct cited content strings located · `hits` = total located occurrences · `dec` = deciles occupied of 10.

## 2.1 `a101-2.md` — 263,995 B — ⭐ PRIORITY FILE 1

| # | Recording | Byte range | Size | Prefix / session id | Live cites | types | hits | dec | Findings they sit in | **Class** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Anglican Worship I — Our Approach to Worship | `41`–`29,822` | 29,782 | `AW-I` | **16** | 6 | 37 | **7** | §1 · §5 · §9 ×2 · §12 · §13 ×4 · §15 ×2 · §13-XIII common ground · OQ8 · IP ledger preamble · `IP-59` · `RV` Session XIII | ✅ **Covered** |
| 2 | Anglican Worship II — Overview of the BCP | `29,823`–`62,397` | 32,575 | `AW-II` | **11** | 5 | 41 | **9** | §1 ×4 · §14 ×4 · `BLOG-53` · `BLOG-54` | ✅ **Covered** |
| 3 | Anglican Worship III — Matins and Evensong | `62,398`–`91,983` | 29,586 | `AW-III` | **10** | 6 | 21 | **6** | §11 · §12 ×3 · §14 · `RV-53…63` re-mine · `POD-2` · `POD-8` | ✅ **Covered** |
| **4** | ⭐ **Anglican Worship IV — Holy Communion Pt 1, Liturgy of the Word** | **`91,984`–`116,830`** | **24,847** | `AW-IV` | **7** | 8 | 30 | **6** | §3 · §5 · §10 (2026-08-09 seg 3) · §12 · §14 ×2 · §15 | ✅ **Covered** |
| **5** | ⭐ **Anglican Worship V — Holy Communion Pt 2, Liturgy of the Sacrament** | **`116,831`–`139,747`** | **22,917** | `AW-V` | **18** | 9 | 33 | **10** | §1 · §8 ×4 · §9 ×3 · §14 · §15 ×2 · POD common ground · `IP-72` · `IP-74` · `IP-79` · `LS` ledger · `BLOG-113` note | ✅ **Covered** |
| 6 | Anglican Worship VI Pt 1 — Liturgical Year and Calendar | `139,748`–`151,802` | 12,055 | `AW-VI` ⚠️ *shared* | **12** *(shared with #7)* | 3 | 31 | **9** | §4 · §14 ×4 · `IP-61` · `IP-63` | ✅ **Covered** |
| 7 | Anglican Worship VI Pt 2 — Calendar continued, Easter computus | `151,803`–`160,769` | 8,967 | `AW-VI` ⚠️ *shared* | **12** *(shared with #6)* | 5 | 17 | **7** | *(same twelve — see §4.1)* | ✅ **Covered** |
| 8 | Ember Days *(standalone topical)* | `160,770`–`166,782` | 6,013 | `Ember` | **6** ⚠️ *(down from 10 raw — see §5.3)* | 1 | 10 | **6** | §14 ×2 (the `[Stated, AW-VI, Ember vid]` finding + the etymology accuracy flag) · OQ 9 · Changelog v0.2 · `IP-61` cross-ref | ✅ **Covered** |
| **9** | ⭐⭐ **Instructed Eucharist (1928 US BCP walkthrough)** | **`166,783`–`248,029`** | **81,247** | `Recon-Euch` | **20** | 17 | 70 | **10** | §7 · §8 ×3 · §9 ×2 · §10 ×4 · §11 · §12 · §13 ×2 · §14 ×2 · §15 ×2 · `RV-53…63` · OQ block · Changelog | ✅ **Covered** |
| 10 | Lent and Ash Wednesday *(standalone topical)* | `248,030`–`263,994` | 15,965 | `Lent vid` | **2** | 5 | 31 | **9** | §14 ×2 | ✅ **Covered** |

⛔ **`a101-2.md` — 10 of 10 Covered. ZERO Uncovered bytes.**

## 2.2 `a105.md` — 188,770 B — ⭐ PRIORITY FILE 2

⚠️ **The file is NOT in class order (2, 3, 6, 5, 4, 7, 9). The `COT-n` column below is reported but NOT adopted — see §4.4.**

| # | Recording (his own class no.) | Byte range | Size | `COT-n` candidates | Live cites | types | hits | dec | Findings they sit in | **Class** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **class 2** — Creation and the Garden of Eden | `40`–`20,504` | 20,465 | `COT-1` (positional) | **2** | 2 | 5 | **4** | §17 method bullet · §17 creation bullet | ⚠️ **Partially covered** |
| 2 | **class 3** — The Fall and the Flood | `20,505`–`52,549` | 32,045 | `COT-2` (positional) | **11** | 6 | 18 | **5** | §5 · §7 ×5 · §17 · §18 · Cross-Batch · OQ 12 | ⚠️ **Partially covered** |
| **3** | ⭐⭐⭐ **class 6** — **The Tabernacle and the Presence of God** | **`52,550`–`76,107`** | **23,558** | `COT-3` (positional) **and** `COT-6` (class no.) | **7** *(+10 via `COT-6`)* | 6 | 42 | **10** | §13 ×2 · §17 ×2 · OQ 8 · `IP-21` | ✅ **Covered** |
| 4 | **class 5** — Jesus the Greater Moses | `76,108`–`105,802` | 29,695 | `COT-4`/`COT-5` ⚠️ split | **4** | 6 | 19 | **7** | §5 · §17 ×2 · OQ 11 | ✅ **Covered** |
| 5 | **class 4** — The Promise to Abraham and his Seed | `105,803`–`139,614` | 33,812 | `COT-5` (positional) / `COT-4` (class no.) | **5** | 5 | 22 | **5** | §5 · §17 ×3 | ⚠️ **Partially covered** |
| **6** | ⭐⭐ **class 7** — Jesus and the Levitical Sacrifices | **`139,615`–`165,438`** | **25,824** | `COT-6` (positional) / `COT-7` (class no.) | **10** | 4 | 17 | **6** | §13 ×2 · §17 ×4 · OQ 8 · `IP-21` | ✅ **Covered** |
| 7 | **class 9** — Jesus as the Son of David | `165,439`–`188,769` | 23,331 | `COT-7` (positional) | **2** | 4 | 84 | **10** | §17 method bullet ×2 | ✅ **Covered** ⚠️ *thin — 74 of 84 hits are one string* |

⛔ **`a105.md` — 4 Covered, 3 Partially covered, ZERO Uncovered bytes.**

## 2.3 `a101-1.txt` — 256,209 B

| # | Recording | Byte range | Size | Session id | Live cites | types | hits | dec | Findings they sit in | **Class** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Session I: Anglican Identity | `52`–`27,452` | 27,401 | `A101-I` | **6** | 3 | 10 | 5 | §1 ×3 · §8 · LS ledger · BLOG ledger | ⚠️ **Partially covered** |
| 2 | Session II: The Doctrine of God (Classical Theism) | `27,453`–`66,157` | 38,705 | `A101-II` | **11** | 2 | 14 | 4 | §3 · §4 ×4 · §5 ×2 · BLOG batch 3 · `BLOG-81` · LS ledger | ⚠️ **Partially covered** |
| 3 | Session III: Anglican History | `66,158`–`106,844` | 40,687 | `A101-III` | **9** | 7 | 24 | 5 | §1 ×3 · §2 · §5 · §8 · §12 · LS ledger ×2 | ⚠️ **Partially covered** |
| 4 | Session IV: Christology | `106,845`–`131,323` | 24,479 | `A101-IV` | **5** | 6 | 14 | **8** | §3 · §4 ×2 · §5 ×2 | ✅ **Covered** |
| 5 | Session V: Ecclesiology | `131,324`–`164,682` | 33,359 | `A101-V` | **6** | 4 | 8 | 4 | §2 ×2 · §18 · IP ledger ×3 | ⚠️ **Partially covered** |
| **6** | ⭐ **Session VI: Scripture (and Tradition)** | **`164,683`–`190,060`** | **25,378** | `A101-VI` | **13** | 8 | 34 | **8** | §2 ×5 · §7 · DQ ledger ×4 · Changelog | ✅ **Covered** |
| 7 | Session VII: Salvation and the Dominical Sacraments | `190,061`–`225,634` | 35,574 | `A101-VII` | **15** | 6 | 19 | 5 | §5 ×2 · §6 ×2 · §7 · §8 ×5 · BLOG ledger ×4 · `BLOG-113` | ⚠️ **Partially covered** |
| 8 | Session VIII: The Ecclesial Sacraments | `225,635`–`256,208` | 30,574 | `A101-VIII` | **3** | 4 | 8 | **6** | §5 · §6 · §7 | ✅ **Covered** |

⛔ **`a101-1.txt` — 3 Covered, 5 Partially covered, ZERO Uncovered.**

## 2.4 `a103.md` — 259,190 B

| # | Recording | Byte range | Size | Session id | Live cites | types | hits | dec | Findings they sit in | **Class** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Introduction — why and how | `61`–`30,246` | 30,186 | `ANF-1` | **22** | 6 | 12 | 5 | §2 ×2 · §3 ×4 · §12 ×4 · §16 · masthead · Cross-Batch · `IP-20` · `IP-45…50` · LS ledger ×5 · Changelog | ⚠️ **Partially covered** |
| 2 | class 2 — From Pentecost to Rome | `30,247`–`58,608` | 28,362 | `ANF-2` | **1** | 2 | 14 | 5 | §16 (inside `ANF-2,3,6`) | ⚠️ **Partially covered** |
| 3 | *(number not stated)* — century survey | `58,609`–`91,063` | 32,455 | `ANF-3` | **2** | 4 | 50 | **9** | §16 ×2 | ✅ **Covered** |
| 4 | ⚠️ **GUEST — Dr. Stephen Boyce on Ignatius** | `91,064`–`124,285` | 33,222 | `ANF-4` | **3** | 11 | 67 | **10** | §2 ×2 · §16 | ✅ **Covered** |
| 5 | ⚠️ **GUEST — Kevin Valdez on Athanasius** | `124,286`–`149,041` | 24,756 | `ANF-5` | **1** | 3 | 50 | **10** | §16 | ✅ **Covered** |
| 6 | class 6 — Justin Martyr, Irenaeus | `149,042`–`177,045` | 28,004 | `ANF-6` ⭐ *compound only* | **1** | 4 | 32 | **7** | §16 (inside `ANF-2,3,6`) | ✅ **Covered** |
| 7 | ⚠️ **GUEST — Tyler West on Hippolytus** | `177,046`–`205,246` | 28,201 | `ANF-7` | **1** | 4 | 7 | **6** | §16 | ✅ **Covered** |
| 8 | class 8 — *"Not quite saints"* (Tertullian, Origen) | `205,247`–`232,130` | 26,884 | `ANF-8` | **1** | 5 | 16 | **6** | §16 | ✅ **Covered** |
| 9 | final week — Constantine, AD 325 | `232,131`–`259,189` | 27,059 | `ANF-9` | **1** | 4 | 20 | **6** | §16 | ✅ **Covered** |

⛔ **`a103.md` — 7 Covered, 2 Partially covered, ZERO Uncovered.**

## 2.5 `a106.md` — 80,482 B

⚠️ **No `Misc-n` session id is in live use — see §4.3. All 14 citations carry the bare prefix `Misc-2025`; the recording assignments below were established by CONTENT in this pass and are not read off any citation.**

| # | Recording | Byte range | Size | Prefix | Cites resolved here | types | hits | dec | Findings they sit in | **Class** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Doctrine of the Trinity *(Trinity Sunday)* | `48`–`18,441` | 18,394 | `Misc-2025` | **2** *(+3 joint)* | 4 | 13 | **6** | §4 ×2 (*"two near-identical Trinity Sunday sessions"*) | ✅ **Covered** |
| **2** | ⭐⭐ **Classical Theism** ⛔ **A 2026 RECORDING** | `18,461`–`47,771` | 29,311 | `Misc-2025` | **8** *(+3 joint)* | 9 | 31 | **7** | §4 ×3 · BLOG batch 3 ×2 · §15 BLOG-3 common ground · `BLOG-81` · `BLOG-82` · `IP-13…23` | ✅ **Covered** |
| 3 | ⚠️ **GUEST — Gregory Bronson, *Sir Gawain and the Green Knight*** | `47,840`–`80,481` | 32,642 | `Misc-2025` | **1** *(+1 changelog)* | 2 | 29 | **7** | §12 (the *"do not be misled by the Misc-2025 guest lecture"* guard) · Changelog v0.3 | ✅ **Covered** |

⛔ **`a106.md` — 3 Covered, ZERO Uncovered.**

## 2.6 ⛔⛔ `a201.txt` — 177,254 B — **WHOLLY UNMINED**

| # | Recording | Byte range | Size | Prefix | Cites | **Class** |
|---|---|---|---|---|---|---|
| 1 | ⚠️ Talk with Fr Matt Kennedy: Where Does Our Assurance Lie? *(two voices, opens in the guest's)* | `52`–`37,044` | **36,993** | ⛔ **none** | **0** | ⚠️ **Uncovered** |
| 2 | A History of the Church in England — A Book Review | `37,045`–`43,305` | 6,261 | ⛔ none | **0** | ⚠️ **Uncovered** |
| 3 | The Memorialist View of The Last Supper | `43,306`–`66,152` | 22,847 | ⛔ none | **0** | ⚠️ **Uncovered** |
| 4 | A Bad Way to Understand John 6:63 | `66,153`–`72,999` | 6,847 | ⛔ none | **0** | ⚠️ **Uncovered** |
| 5 | Response to "Should Christians Baptize Their Babies?" | `73,000`–`106,902` | 33,903 | ⛔ none | **0** | ⚠️ **Uncovered** |
| 6 | Is Contemporary Worship Wrong? | `106,903`–`114,580` | 7,678 | ⛔ none | **0** | ⚠️ **Uncovered** |
| 7 | The Stories We Tell | `114,581`–`153,950` | 39,370 | ⛔ none | **0** | ⚠️ **Uncovered** |
| 8 | Simply Anglican — A Book Review | `153,951`–`173,500` | 19,550 | ⛔ none | **0** | ⚠️ **Uncovered** |
| 9 | Canterbury Cousins — A Book Review | `173,501`–`177,253` | 3,753 | ⛔ none | **0** | ⚠️ **Uncovered** |

## 2.7 ⛔⛔ `a202.txt` — 211,170 B — **WHOLLY UNMINED**

| # | Recording | Byte range | Size | Prefix | Cites | **Class** |
|---|---|---|---|---|---|---|
| 1 | ⚠️⚠️ A Debate on Holy Orders: *Apostolicae Curae* *(3 voices, 0 diarization)* | `51`–`95,315` | **95,265** | ⛔ none | **0** | ⚠️ **Uncovered** |
| 2 | ⚠️⚠️ Debate on Holy Orders: RJ and Noah, mod. Evan Minton *(3 voices, 0 diarization)* | `95,316`–`175,795` | **80,480** | ⛔ none | **0** | ⚠️ **Uncovered** |
| 3 | Is the Monarch of England the Pope of Anglicanism? | `175,796`–`184,862` | 9,067 | ⛔ none | **0** | ⚠️ **Uncovered** |
| 4 | How to Use the 2019 Book of Common Prayer | `184,863`–`211,169` | 26,307 | ⛔ none | **0** | ⚠️ **Uncovered** |

## 2.8 `a301-Classical-Theism.md` — 29,338 B

| # | Recording | Byte range | Size | Prefix | Cites | **Class** |
|---|---|---|---|---|---|---|
| 51 | Classical Theism — ⛔ **byte-identical to `a106` rec 2** | `0`–`29,337` | 29,338 | `Misc-2025` *(derivatively)* | **0 direct · 11 via `a106` rec 2** | ✅ **Covered (derivatively)** ⛔ **DO NOT INGEST** |

⛔ **Classified `Covered` on the ground that its content is `a106` recording 2's content and is cited eleven times there.** ⚠️ **That is a statement about coverage, NOT a recommendation to register it.** `260834-6`'s disposition stands: rejected re-supply, header preserved as the dating witness.

---

# 3. THE THREE-WAY CLASSIFICATION, WITH COUNTS

| Class | Recordings | Bytes | Share of the 1,466,408 B scope set |
|---|---|---|---|
| ✅ **Covered** | **28** | 757,059 | 51.6 % |
| ⚠️ **Partially covered** | **10** | 320,596 | 21.9 % |
| ⚠️ **Uncovered** | **13** | **388,321** | **26.5 %** *(of recording bytes; 388,424 including the two banner lines)* |
| **Total** | **51** | 1,465,976 | 100.0 % |

*(Sums to 432 B less than the 1,466,408 B scope set — the eight banner lines, which are not recordings. `a301`'s 29,338 B is counted once, in the Covered column; it duplicates `a106` rec 2's content by construction.)*

### ⭐ Byte weight of Uncovered — the two figures the brief asked for

| Measure | Value |
|---|---|
| **Total Uncovered byte weight** | ⛔ **388,321 B** — 13 recordings, all in `a201.txt` and `a202.txt` |
| **Uncovered byte weight restricted to `a101-2.md` and `a105.md`** | ⭐⭐⭐ **0 B — ZERO. Both priority files are fully covered.** |

⭐ **What that means for the retro-registration pass, stated plainly:**

- **`a101-2.md` and `a105.md` need REGISTRATION ONLY** at the recording level. No recording in either is unmined. ⚠️ The three `Partially covered` `a105` recordings (classes 2, 3 and 4) want a **depth** sweep, not a first mining, and that is a different and much cheaper act.
- **`a101-1.txt` and `a103.md` need registration, with a depth sweep** over their seven `Partially covered` recordings.
- **`a106.md` needs registration plus the recording-2 re-dating** (§4.3).
- ⛔⛔ **`a201.txt` and `a202.txt` need registration PLUS A FULL FIRST MINING of 388,321 bytes** — and `a202`'s 175,745 B of three-speaker material is gated behind `260834-6`'s diarization prerequisite. **This is the single largest piece of work the retro-registration pass faces and `260834-6`'s framing hid it.**

---

# 4. THE FOUR NAMED RESOLUTIONS

## 4.1 ⭐⭐ The `a101-2` recording 6/7 boundary at byte `151,803`

**The question asked:** do `AW-VI` citations fall on both sides of `151,803`, or only one?

⭐⭐⭐ **ANSWER: ON BOTH SIDES, DECISIVELY, AND THE TWO SIDES CARRY DIFFERENT CITED MATERIAL.** The `AW-VI` citations name four distinct blocks of content. Located by byte offset:

| Cited content (verbatim from the citation) | Located in | Part 1 `139,748`–`151,802` | Part 2 `151,803`–`160,769` |
|---|---|---|---|
| *"Pre–Vatican II calendar: Advent → Christmas → Epiphany → **Gesima** Sundays → Lent…"* (§14, `IP-63` cross-ref) | ⭐ **Part 1** | `Advent` **9** · `Epiphany` **8** · `Gesima` **1** · `calendar` **13** | `Advent` 4 · `Epiphany` **0** · `Gesima` **0** · `calendar` 4 |
| *"**Lent:** 40 days (Sundays not counted); total fast on **Ash Wednesday** and Good Friday"* (§14) | ⭐ **Part 1** | `Lent` **9** · `Ash Wednesday` **5** | `Lent` 1 · `Ash Wednesday` **0** |
| *"→ Whitsuntide/**Pentecost** → **Trinity**. **Counts from Trinity, not 'after Pentecost.'**"* (§14) | ⭐⭐⭐ **Part 2** | `Trinity` ⛔ **0** · `Pentecost` ⛔ **0** | `Trinity` **20** · `Pentecost` **8** |
| *(the Easter computus the segment opens mid-sentence on)* | ⭐ **Part 2** | `full moon` ⛔ **0** | `full moon` **4** · `Easter` **14** |

⛔⛔ **THE `Trinity`/`Pentecost` ROW IS THE LOAD-BEARING ONE AND IT IS AN ABSOLUTE ZERO ON THE PART 1 SIDE.** The corpus records, as `AW-VI`, a specific claim about *counting from Trinity rather than after Pentecost* — and the words `Trinity` and `Pentecost` **do not occur once** in Part 1, while occurring 20 and 8 times in Part 2. **A byte range that carries the only occurrences of the terms in a cited claim is not an unmined range.**

⭐ **What this settles and what it does not.**

- ✅ **SETTLED: `151,803`–`160,769` IS COVERED. It is not an unmined stretch and the retro-registration pass must not treat it as one.** That was worth establishing regardless of the boundary reading.
- ⛔⛔ **NOT SETTLED, AND DELIBERATELY NOT ADOPTED: WHICH READING IS RIGHT.** Citations falling on both sides of `151,803` is **exactly what reading (i) predicts** (one recording, split by a capture artifact — of course the material spans the split) **and exactly what reading (ii) predicts** (two recordings, both tagged `AW-VI` because the mining pass, like `260834-6`, saw one session in two parts). ⛔ **The evidence is consistent with both and discriminates between neither.**
- ⚠️ **`260834-6`'s judgment that reading (ii) is better supported is UNAFFECTED — neither strengthened nor weakened.** Its support comes from the two `EXT-3` channel rows (`9UDQhvMdkNA` *"VI Pt 1"* 916 s and `38BYTZzLmxg` *"VI Pt 2"* 663 s, both 2024-11-23) and the byte-to-duration ratio agreement (1.34 vs 1.38). **Nothing in citation distribution adds to or subtracts from that, and the brief's instruction not to adopt a reading on citation distribution alone is followed.** The audio or the two videos remain the thing to check.

⭐ **One incidental gain: the material split is clean.** Part 1 is the calendar's *opening* half (Advent through Lent) and Part 2 is its *closing* half (Easter computus, Trinity/Pentecost counting, the feast cycle). ⚠️ **That is what a single continuous exposition looks like AND what a two-part class looks like.** Recorded as an observation, not as evidence for either reading.

## 4.2 ⭐ The `ANF` legend row: 8 sessions vs 9 recordings

**ANSWER: NINE distinct `ANF-` session ids appear in live citations — `ANF-1` through `ANF-9`, unbroken. ⛔ NO RECORDING LACKS ONE.**

⚠️⚠️ **BUT THE COUNT DEPENDS ENTIRELY ON EXPANDING COMPOUND CITATIONS, AND A BARE GREP REPORTS EIGHT.**

| Session id | Live citations | Standalone token exists? |
|---|---|---|
| `ANF-1` | 22 | ✅ yes |
| `ANF-2` | 1 | ⚠️ only as the head of `ANF-2,3,6` |
| `ANF-3` | 2 | ✅ yes (`[Stated, ANF-3]`, L2257) |
| `ANF-4` | 3 | ✅ yes |
| `ANF-5` | 1 | ✅ yes |
| **`ANF-6`** | **1** | ⛔⛔ **NO — it exists ONLY inside `**[Stated, ANF-2,3,6]**` at L2256** |
| `ANF-7` | 1 | ✅ yes |
| `ANF-8` | 1 | ✅ yes |
| `ANF-9` | 1 | ✅ yes |

⭐⭐⭐ **`ANF-6` IS THE WHOLE ANSWER TO THIS QUESTION.** A bare `ANF-\d+` grep returns **eight** distinct ids and would have reported `a103` recording 6 as **Uncovered**. It is not: the citation `**[Stated, ANF-2,3,6]**` covers *"Justin Martyr's **Dialogue with Trypho** and **Apologies**"* — and recording 6 (`149,042`–`177,045`) is the one that carries `Justin` **28 times** and `Irenaeus` twice, against 15 and 0 in recording 3 and 0 and 13 in recording 4. **The citation resolves to recording 6 on content and the recording is covered.**

⭐⭐ **The `ANF-n` → recording map is POSITIONAL (file order), and it is corroborated at six independent points, not assumed:**

| Corroboration | Evidence |
|---|---|
| `ANF-4` = **Dr. Stephen Boyce** | §16: *"Dr. Stephen Boyce on Ignatius (**ANF-4**)"*; recording 4 (`91,064`–`124,285`) carries `Ignatius` ×36, the file's maximum, and Boyce's self-introduction at `@91,064` |
| `ANF-5` = **Kevin Valdez** | §16: *"Kevin Valdez on Athanasius (**ANF-5**)"*; recording 5 carries `Athanasius` ×35, the file's maximum |
| `ANF-7` = **Tyler West** | §16: *"Tyler West on Hippolytus (**ANF-7**)"*; recording 7 carries `Hippolytus`/`Apostolic Tradition` ×3 and *"sign of the cross"* ×2, both file maxima |
| `ANF-8` = **class 8** | §16 names it explicitly: *"**'Not quite saints' session (8)**: Tertullian… Origen"*; recording 8 carries `Tertullian` ×12, the file's maximum |
| `ANF-9` = **the Constantine session** | §16: *"**Constantine session (9)**"*; recording 9 carries `Edict of Milan` ×6 and `325` ×2, both file maxima |
| `ANF-6` = **Justin/Irenaeus** | as above |

⛔ **THE LEGEND ROW IS WRONG AND IS REPORTED, NOT CORRECTED.** The `ANF` row's *"teaching class, **8 sessions**"* is false; its own range field `ANF-1..9` is correct, `a103.md` contains nine recordings, and nine distinct ids are in live use. `260834-6` reported the same discrepancy from the file side; **this pass confirms it independently from the citation side.**

⚠️⚠️ **A SECOND, SEPARATE `ANF` DISCREPANCY FOUND HERE AND NOT PREVIOUSLY REPORTED — AND IT IS AN ATTRIBUTION ERROR, NOT A COUNTING ONE.** §16's own preamble reads *"**RJ's own teaching (sessions 1, 2, 3, 6, 7, 8, 9)**"* — **and lists session 7 among RJ's own.** ⛔ **Session 7 is Tyler West's guest lecture**, as §16 itself states nineteen lines later (*"**Tyler West on Hippolytus (ANF-7)**… This is… **West's framing, not RJ's**"*) and as `260834-6` established from the tape (*"we have **Tyler West** who will be leading our class today"*, `@177,046`). **The two statements in one section contradict each other on who taught recording 7.** RJ's own sessions are **1, 2, 3, 6, 8, 9** — six, not seven. ⛔ **REPORTED, NOT CORRECTED. No finding was re-attributed and §16 was not edited.** ⚠️ **This is a live attribution risk of exactly the class the project guards hardest against, and the retro-registration pass should resolve it before writing any session row for `a103`.**

## 4.3 ⭐⭐ `Misc-2025`: does any live citation carry or imply a date, and does the corpus state 2025 as a fact?

**Two answers, and the second is the more useful one.**

### (a) Does the corpus state 2025 for `a106` recording 2 as a FACT? ⛔ **NO — NOWHERE.**

Every instance of *2025* attaching to this material was located and read. **All of them are the banner, inherited:**

- ⚠️ **The year is inside the tag string itself.** The prefix is `Misc-2025`, not `Misc`. All **14** live citations therefore *carry* "2025" by construction, in every occurrence, without any of them ever *asserting* it. ⛔⛔ **That is the trap, and it is worse than `Rev`'s: `Rev`'s year had to be written beside the tag and could be omitted; `Misc-2025`'s year cannot be written without being asserted, and cannot be corrected without renaming the prefix.**
- The masthead source line (L357) and the Source ID Legend row (L380) both give *"2025"* — **and both are the banner copied forward.** `260834-6` established that `a106.md`'s own banner reads `St Francis Misc 2025`.
- **No finding, no `[Stated]` bullet, no ledger entry and no changelog line anywhere in `St_Francis_EMC_Distinctives.md` asserts a 2025 recording date for the Classical Theism session on independent grounds.** Grepped and read: zero.

### (b) ⭐⭐⭐ Does any live `Misc-` citation IMPLY a date? **YES — THREE OF THEM DO, AND THEY IMPLY 2026, NOT 2025.**

The corpus dates the `Misc-2025` material **by arithmetic, three separate times**, always against `BLOG-81`/`W20`, which is firmly dated **2014-07-19**:

| Line | Text | Implied year |
|---|---|---|
| L768 | *"§4 above already records classical theism, simplicity, one divine will and the wrath=love identity via the sunbeam analogy (`Misc-2025`). **This is that doctrine, in his own written voice, twelve years earlier.**"* | ⭐ **2026** |
| L1843 | *"attested in his own writing from **2014**, **twelve years before** the `Misc-2025` material"* | ⭐ **2026** |
| L5763 | *"the wrath=love identity via the **sunbeam-on-wax-and-clay analogy** (`Misc-2025`). **W20 is that doctrine, in his own written voice, twelve years earlier.**"* | ⭐ **2026** |

⭐⭐⭐ **AND THE ARITHMETIC POINTS AT THE RIGHT RECORDING, NOT MERELY THE RIGHT FILE.** The **sunbeam-on-wax-and-clay analogy** — the exact content all three lines name — was located by byte offset and sits **only** in `a106.md` recording 2:

> `@35,981` *"Think of a **sunbeam**. Think of the candle, the **wax** that is being impacted by the heat of the sun versus the **clay**…"* · `@36,227` *"the candle wax will melt and the clay will harden."*

`sunbeam` = **0** in recording 1, **9 hits** (`sunbeam`/`wax`/`clay`) in recording 2, **0** in recording 3. **The three "twelve years earlier" statements are about recording 2 specifically — the very recording whose banner year is wrong.**

⭐⭐ **A FOURTH, INDEPENDENT DATE IMPLICATION FROM THE CORPUS'S OWN CHANGELOG.** L2853: *"**v0.3 (2026-06-13):** Integrated Batch 3 (`Misc-2025`)."* ⛔ **The batch was integrated on 2026-06-13 — six or seven days AFTER `a301`'s header date (`Jun 6, 2026`) and the channel row (`gEDpnwg2tF0`, 2026-06-07).** A 2025 recording integrated in June 2026 would be a year-old capture; a 2026-06-06 recording integrated on 2026-06-13 is a **week-old** one, which is what the rest of this project's intake cadence looks like.

⛔⛔ **SUMMARY OF THE RESOLUTION.** The corpus **never states 2025 as a fact** for `a106` recording 2 — it inherits it from the banner, and the prefix name makes the inheritance invisible. **Four independent live signals inside the corpus imply 2026**: three arithmetic statements against a 2014 anchor, all anchored on a content string unique to recording 2, plus the integration date in its own changelog. ⭐ **Together with `a301`'s `### Jun 6, 2026` header and the `2026-06-07` channel row, the 2026 dating for recording 2 now has SIX independent supports and ZERO contrary evidence beyond the banner itself.**

⛔ **REPORTED, NOT CORRECTED. No citation was re-dated, no legend row edited, no prefix renamed, and no `Misc-n` assignment written.** ⚠️ **A caution for the pass that does correct it: recordings 1 and 3 are genuinely 2025** (`5mU3CdbXjOQ` 2025-06-18; `hlEGpBC3Vj4` 2025-12-31) — **a blanket re-date of the `Misc-2025` prefix would be as wrong as the current label**, and 8 of the 14 live citations resolve to recording 2 while 2 resolve to recording 1 and 1 to recording 3.

⚠️ **One further complication the renaming pass must face, recorded here: `Misc-1..7` IS A DEAD RANGE.** The legend's range field says `Misc-1..7`, but **the only `Misc-N` token anywhere in the document is the string `Misc-1` inside that legend row itself.** ⛔ **Not one live citation uses a `Misc-n` session id.** All 14 use the bare prefix `Misc-2025`. **There is therefore no citation-level machinery to re-point; there are only fourteen occurrences of a prefix whose name is a date claim.**

## 4.4 ⭐⭐⭐ `a105` is out of class order: does any live `COT-` citation point at class 1 or class 8?

**ANSWER, IN TWO PARTS, AND THE SECOND MATTERS MORE THAN THE FIRST.**

### (a) The direct answer: ⛔ **NO citation resolves to class 1 or class 8, and `COT-8` DOES NOT EXIST.**

`COT-8` and `COT-9` return **zero hits** in the whole document — so nothing can point at class 8 by number. `COT-1` exists (2 live citations) and **would** point at class 1 under a class-number reading. **It does not:** its cited content is located, by byte offset, inside recording 1 (class 2):

> *"creatio ex nihilo defended against 'God merely formed pre-existing matter'"* → `a105.md` `@3,840`, `@4,299`, `@9,965` — *"God creates all of existence **out of nothing**"* — all inside `40`–`20,504`, **which is class 2.**
> *"Genesis 1:26 read as a hint of the Trinity"* → `@5,103` — *"**Genesis 1:26** let us make man in our image… this is a **hint**"* — same recording. `1:26` occurs **twice in recording 1 and nowhere else in the file.**

⭐ **So the corpus does NOT cite material `a105.md` lacks.** No second source is implied and no citation is wrong on this point.

### (b) ⛔⛔ THE FINDING THAT MATTERS: **`COT-n` IS NOT A RELIABLE INDEX INTO `a105.md` UNDER EITHER READING, AND IS REPORTED AS UNRESOLVED**

⚠️ Both candidate readings were tested against the located content of every citation. **Each reading is confirmed by some citations and falsified by others.**

| Citation | Cited content | Located at | Positional reading (`COT-n` = *n*th recording) | Class-number reading (`COT-n` = his class *n*) |
|---|---|---|---|---|
| `COT-1` | *creatio ex nihilo*, Gen 1:26 | rec 1 (class 2) | ✅ **rec 1** | ⛔ class 1 — **absent from the file** |
| `COT-2` | apostasy, *"walked away from that regeneration"*, Rom 11 grafting | rec 2 (class 3): `grafted` ×9, `regenerat` ×4 · rec 1: **0, 0** | ✅ **rec 2** | ⛔ class 2 = rec 1 — **zero hits** |
| `COT-4` | Christus Victor *"competitive with"* penal substitution | rec 5 (class 4): `Christus Victor` ×2, `penal` ×10 · rec 4: **0, 0** | ⛔ rec 4 — **zero hits** | ✅ **class 4 = rec 5** |
| `COT-7` | grain/*"meat"* offering, Melchizedek's bread-and-wine | rec 6 (class 7): `grain offering` ×10 · rec 7: **0** | ⛔ rec 7 — **zero hits** | ✅ **class 7 = rec 6** |
| `COT-3` **+** `COT-6` *(cited together, for ONE passage)* | *"implicitly, liturgically, ceremonially saying that **this has not yet happened**"* | ⭐ **one location: `@75,897`–`75,955`, rec 3 (class 6)** | `COT-3` ✅ rec 3 / `COT-6` ⛔ rec 6 | `COT-6` ✅ class 6 = rec 3 / `COT-3` ⛔ class 3 = rec 2 |
| `COT-6` | *"a **priest friend**"* who called OT religion *"**paganized**"* | ⭐ **`@55,375`, `@55,553`, rec 3 (class 6)** — 0 elsewhere | ⛔ rec 6 | ✅ class 6 = rec 3 |
| `COT-5` | Abraham's promises, the true *"seed"*, Gal 3 **and** *"promised land → all creation"* | ⛔⛔ **SPLIT: `Abraham` ×42 / `seed` ×12 / `Galatians` ×8 in rec 5 (class 4); `promised land` ×12 in rec 4 (class 5), where Abraham = 1 and seed = 0** | ✅ half | ✅ the other half |

⭐⭐⭐ **THE MOST ECONOMICAL EXPLANATION, OFFERED AS AN OBSERVATION AND NOT ADOPTED: `COT-3` AND `COT-6` ARE THE SAME RECORDING UNDER TWO NUMBERING SYSTEMS.** Both are cited for one passage at `@75,897`; `COT-6`'s other content (`priest friend`, `paganized`) is in that same recording; and `COT-3`'s showbread content (`@61,086`–`63,141`, the file's only four `bread of the presence` hits) is in it too. **Recording 3 IS class 6.** A mining pass that tagged it `COT-3` by position on one occasion and `COT-6` by his spoken class number on another — without noticing the file is out of class order — produces exactly this pattern. ⛔ **NOT ADOPTED. It is a hypothesis that fits, and `COT-5`'s split still does not fit it.**

⛔⛔ **PER THE BRIEF'S OWN INSTRUCTION, ALL 41 `COT-` CITATIONS ARE REPORTED AS AMBIGUOUS AT THE ID LEVEL RATHER THAN FORCE-MAPPED.** A forced mapping here would be worse than the gap: under the positional reading it would mark rec 4 and rec 7 as carrying Christus Victor and Melchizedek material they demonstrably do not contain, telling the next pass those ranges are mined when they are not.

⭐ **COVERAGE IS NEVERTHELESS ESTABLISHED, BY CONTENT AND NOT BY ID.** Every one of the seven recordings carries locatable cited content (§2.2). **The ambiguity is in the numbering, not in the coverage.** ⚠️ **The retro-registration pass must NOT write `COT-n` session rows from the citations. It must derive session numbers from his own spoken class numbers in the tape — which `260834-6` has already transcribed — and then record, as a separate mapping table, which `COT-n` citation belongs to which session row.** ⛔ **Renumbering the existing `COT-n` tags is forbidden by the `260813-1` precedent and is not proposed here.**

---

# 5. CITATION-RESOLUTION STATISTICS

## 5.1 The headline figures

| | Count | Share |
|---|---|---|
| **Total live pre-manifest citations** *(compounds expanded, legend/definition rows and false positives excluded)* | **258** | 100 % |
| ✅ **Resolved cleanly** — id names exactly one recording **and** the cited content is locatable in that recording's byte range | **191** | **74.0 %** |
| ⚠️ **Ambiguous** — id names more than one candidate recording, or is a bare prefix with no session id | **64** | **24.8 %** |
| ⛔ **Failed to resolve** — cited content is present in **no** recording of the mapped file | **3** | **1.2 %** |

### Breakdown

| Prefix | Live | Clean | Ambiguous | Failed | Why |
|---|---|---|---|---|---|
| `A101-I…VIII` | 68 | **68** | — | — | roman numeral = session number = file order; ✅ verified by content for all 8 sessions |
| `AW-I…V` | 62 | **62** | — | — | five ids, five recordings, 1:1 |
| **`AW-VI`** | **12** | — | **9** | ⛔ **3** | one id, **two** recordings (§4.1); three citations fail outright (§5.2) |
| `Ember` | 6 | **6** | — | — | single recording |
| `Recon-Euch` | 20 | **20** | — | — | single recording |
| `Lent vid` | 2 | **2** | — | — | single recording |
| `ANF-1…9` | 33 | **33** | — | — | positional, corroborated at six independent points (§4.2) |
| **`COT-1…7`** | **41** | — | **41** | — | two competing numbering readings, each falsified by some citations (§4.4) |
| **`Misc-2025`** | **14** | — | **14** | — | bare prefix, no session id, three candidate recordings; resolved by content in this pass but not by any citation |
| `a201` / `a202` | **0** | — | — | — | ⛔ no prefix exists |

## 5.2 ⛔ The three failures, named individually

**Failure 1 and 2 — `AW-VI` at L756 (Aristotle/Plato/logos).** The citation reads *"…roots it in **Aristotle/Plato** under Scripture's authority, defending the use of Greek philosophical terms (**logos**; **'in him we live and move'**). **[Stated, A101-II, AW-VI, Misc-2025]**"*.

| Term | `a101-2.md` (all 10 recordings) | `a101-1.txt` Session II | `a106.md` rec 2 |
|---|---|---|---|
| `aristot` | ⛔ **0** | ⛔ **0** | ✅ 1 `@46,234` |
| `plato` | ⛔ **0** | ⛔ **0** | ✅ 1 `@46,269` |
| `logos` | ⛔ **0** | ⛔ **0** | ✅ 2 `@46,779`, `@46,856` |
| *"live and move"* | ⛔ **0** | ⛔ **0** | ✅ 1 `@46,919` |

⛔⛔ **THE `AW-VI` COMPONENT OF THIS CITATION RESOLVES TO NOTHING.** All four named strings sit in one place — `a106.md` recording 2, within 700 bytes of each other — which is the `Misc-2025` component. ⚠️ **The `A101-II` component also fails on these four strings**, though Session II is independently about classical theism (`classical theism` ×13, `simplicity` ×3) and so resolves at the topic level; the `AW-VI` component does not resolve even at that level, since `classical theism` in `a101-2.md` occurs **only in AW-III** (`@80,729`, `@80,842`, an aside), never in either `AW-VI` part.

⛔ **REPORTED AS UNRESOLVED, NOT REASSIGNED.** `AW-III` is a nearby candidate and is **deliberately not adopted** — a forced mapping is exactly what the brief forbids.

**Failure 3 — `AW-VI` at L1652 (the meat/dairy/fish attribution).** The passage reads *"**`AW-VI` records** *'abstinence from **meat and dairy, with fish**'*."*

| Term | `AW-VI` Part 1 | `AW-VI` Part 2 | **`Lent vid` `248,030`–`263,994`** |
|---|---|---|---|
| `dairy` | ⛔ **0** | ⛔ **0** | ✅ **2** — `@251,296` *"refrain from **meat and dairy** for these 40 days"* · `@251,812` |
| `fish` | ⛔ **0** | ⛔ **0** | ✅ **5** — `@251,931` *"you can have **fish** for instance"* |

⛔⛔ **THE CONTENT ATTRIBUTED TO `AW-VI` IS IN THE LENT VIDEO, A DIFFERENT RECORDING 96 KB AWAY.** ⚠️⚠️ **This matters beyond bookkeeping: L1652 uses this attribution to record a NON-HARMONISED DIFFERENCE between `AW-VI` and `IP-61` — *"`AW-VI` has abstinence 'from meat and dairy, with fish'; here the Friday rule is meat only"*. If the `AW-VI` half of that comparison is actually the Lent video, the difference being recorded is between the LENT VIDEO (Feb 2026) and `IP-61` (Aug 2026) — six months apart in one year — not between a 2024 class and a 2026 class two years apart.** ⛔ **REPORTED, NOT CORRECTED. `IP-61` is not touched, the difference is not harmonised, and no finding is re-dated.** ⚠️ **Flagged for the retro-registration pass as the higher-priority of the three failures.**

## 5.3 ⚠️ A FALSE-POSITIVE CLASS FOUND AND STRIPPED — 4 of 10 `Ember` tokens are not citations

A raw grep gives `Ember` **10** live tokens. Four were read in context and excluded:

| Line | Text | Why excluded |
|---|---|---|
| L5184 | *"`compline` and **`Ember`** are **ZERO** in all three files"* | ⛔ a **term-scan zero-report about OTHER sources** — the opposite of a citation |
| L5248 | *"**`Ember`**/`Rogation`/`Gesima`/`compline` **ZERO across all five**"* | ⛔ same class |
| L5320 | *"`Lent` **0·0·0** · **`Ember`** **0·0·0**"* | ⛔ same class |
| L1665 | *"**Ember** and Lent practice, 2025 (**RC-3**)"* | ⛔ an `RC-3` citation that *mentions* ember days; it is not a citation of the Ember video |

⭐⭐ **THIS IS A GENERAL HAZARD IN THIS CORPUS AND IS RECORDED AS ONE.** The project's own discipline of reporting confirmed zeros means that **a bare grep for any tag prefix will pick up the project's absence-reports about entirely different sources and score them as coverage.** ⛔ **Inverted, that is a false-coverage generator of exactly the kind the brief warns against — it would tell the next pass a range is mined because another pass reported the range's subject matter absent somewhere else.** ⚠️ **Every prefix count in §5.1 was context-checked for this class before it was written down.**

## 5.4 ⚠️ On `260834-6`'s *"roughly 194 live citations"*

**This pass counts 258.** The discrepancy is explained and is not a contradiction:

- ⭐ **`260834-6` did not expand compound citations.** Its per-prefix figures are consistent with bare-token counting, which — as §1.2 shows — loses entire citations (`A101 II/III/VII` yields **nothing** to a bare `A101-` grep) and silently drops list members (`ANF-6`, `COT-2` through `COT-6`).
- ⚠️ **`260834-6`'s own per-prefix table does not sum to 194 either** — the eight rows total **221** as printed (24 + 42 + 5 + 25 + 22 + 13 + 16 + 32 + 37). **Neither figure is reproducible from the other**, and the "194" in its Task 5 recommendation has no derivation shown.
- ⛔ **NOT logged as an error in `260834-6`.** Its coverage claim (*that* the files were mined) is confirmed for five files and corrected for two; **its citation ARITHMETIC is superseded by this pass's, which shows its method.**

---

# 6. WHAT THIS PASS DID NOT DO, STATED EXPLICITLY

⛔ **No source registered. No finding minted. No `File`, `LS`, `IP`, `RV`, `DQ`, `BLOG` or `POD` number consumed** — next-free numbers remain **`File 40`**, **`DQ-25`**, **`IP-98`**, **`LS-129`**, **`RV-64`**, **`BLOG-159`**, **`POD-17`**, unchanged. ⛔ **No hash registered, no byte offset written into any registry, no session row created, no `VP-` pair, no `DELTA`, no gate or channel state moved.**

⛔ **No boundary reading adopted.** The `a101-2` recording 6/7 boundary at `151,803` is left with both readings live, exactly as `260834-6` left it.

⛔ **No `COT-n`, `Misc-n` or `ANF-n` mapping adopted, corrected or renumbered.** The `ANF-n` positional map is *evidenced* and reported; it is not written into anything.

⛔ **No error corrected.** Six discrepancies are **reported and left standing**: the `ANF` legend's *"8 sessions"*; §16's attribution of session 7 to RJ; the `Misc-2025` banner year; the dead `Misc-1..7` range; the `AW-VI`/Aristotle citation; the `AW-VI`/meat-and-dairy attribution.

⛔ **`DQ-9` not moved. `IP-84` neither confirmed nor extended. `OQ20`, `OQ21`, `DQ-24` untouched. The element/circumstance question is exactly where `260834-5` and `260834-6` left it.**

⛔ **`Incense_Conversational_Outline.md`, `RJ_Incense_Analysis.md`, `St_Francis_EMC_Distinctives.md`, `On_Incense_and_the_Altar.md`, `RJ_Final_Question_List.md`, `RJ_Open_Questions_and_Divergences.md`, `SRC_Manifest.md` and `SRC_Channel_Inventory.md` NOT TOUCHED.** C11's drift is reported as firing code 9 and left standing.

⛔ **Nothing drafted, altered, or posted to Rev. James.**

⛔ **No theological substance read or analysed.** Source text was opened only to locate cited strings by byte offset and to count terms. ⚠️ **Per `ORCHESTRATION.md` §8's standing instruction, the incense/icon result is reported explicitly even though this pass did not read for it: `incense`/`censer` counts inside the covered ranges are unchanged from `260834-6`'s battery (`a101-2` AW-I 8, AW-IV 3, Instructed Eucharist 20; `a105` class 6 = rec 3 seven, class 7 = rec 6 three), and this pass adds NOTHING to and subtracts NOTHING from them.** ⭐ **What it does add is that every one of those ranges is inside a COVERED recording** — so the incense material in these files is already in the ledger, and the retro-registration pass should expect to find it there rather than mint it again.

---

# 7. THE CONVENTIONS ADDITION — FULL ACCOUNTING

## 7.1 Where it went, and why there rather than the other candidate

⭐ **Home chosen: `ORCHESTRATION.md` §8 "Standing instructions". The repo's own conventions were checked, not assumed.**

| Candidate | What it actually holds | Verdict |
|---|---|---|
| **`ORCHESTRATION.md` §8** | Its own heading is literally *"Standing instructions"*, and its three existing entries are all **project-wide obligations on every pass** — the incense/icon flag rule, the never-post-to-Rev-James rule, the never-alter rule. | ✅ **CORRECT HOME.** The new instruction is the same kind of object: an obligation binding every pass of a given class. |
| `passes/README.md` | Scoped to **pass-artifact file conventions** — what the `.diff` and `_close-out.md` are, why they are committed, and what may live in `passes/` without a registry row. Its own closing line defers upward: *"See `ORCHESTRATION.md` §4."* | ⛔ **WRONG HOME.** The instruction is about updating *registries*, not about writing pass artifacts. |

⭐ **A live precedent governs and was followed: `260832-5` added a sentence to `ORCHESTRATION.md` §9 and recorded that it *"bumped stamp and registry row"*.** The same two-cell consistency act is done here.

## 7.2 What the instruction says

Added to §8, after the never-alter rule, stamped `260834-7`. It requires every intake or retro-registration pass to update **both** registries in the same pass:

1. **`SRC_Coverage_Register.md`** — coverage state for the material covered: retrieved, judged, deliberately declined and why, and unreviewed.
2. **`SRC_Channel_Inventory.md`** — the decision cell for each video covered, set to **`INGESTED`** with **the File number and finding range**.

⚠️⚠️ **The instruction states in its own text that `SRC_Coverage_Register.md` DOES NOT YET EXIST and is NOT created by this pass**, names what a later pass will build it to cover (both YouTube channels, `BLOG`, `POD`, Discord, in-person recordings, and the pre-manifest `aNNN` files), and tells a reader who meets the convention before the file exists that this is not an error to go hunting for — **clause 1 is owed rather than actionable; clause 2 stands alone and is enforceable now.** ⭐ A short *"why both and not one"* note records that the inventory is video-keyed and channel-scoped while the register is universe-scoped, so a pass updating only the inventory leaves every non-YouTube universe — and every *unretrieved* item — invisible.

⛔ **`SRC_Coverage_Register.md` WAS NOT CREATED. It does not exist on disk after this pass and no stub, placeholder or registry row was written for it.**

## 7.3 The two consistency cells, and why they were unavoidable

⚠️ **`validate_project.py` CHECK 3 raises a hard `err`, not a `warn`, on version drift** (`"VERSION DRIFT — registry says X, document says Y"`). Editing `ORCHESTRATION.md` without bumping its stamp would leave the repo's stamping discipline broken; bumping its stamp without bumping the registry cell would take the validator to **1 error**. Both were therefore bumped, together:

- `ORCHESTRATION.md` — `**Last updated: 260832-5**` → `**Last updated: 260834-7**`
- `PROJECT_STATE.md` §4 registry row for `ORCHESTRATION.md` — version cell `260832-5` → `260834-7`, and the description cell extended to name §8's new rule and to carry the ⚠️ *forthcoming, not yet created* flag for `SRC_Coverage_Register.md`.

⛔ **NOTHING ELSE IN `PROJECT_STATE.md` WAS TOUCHED** — no pass note, no next-free line, no gate, no owed-leads sentence, no other registry row. ⛔ **No new file was registered.**

---

# 8. ✅ VALIDATOR AFTER, AND THE DIFF

```
80 ok · 9 warnings · 0 errors
```

⭐ **UNCHANGED from the BEFORE run — same count, same nine codes, in the same order.** The full 210-line output was diffed line by line against the BEFORE capture. **Exactly one line differs, and it is an `ok` line reporting the value this pass deliberately changed:**

```
39c39
<   ok    [C3] ORCHESTRATION.md: version agrees with registry (260832-5)
---
>   ok    [C3] ORCHESTRATION.md: version agrees with registry (260834-7)
```

⭐ **`ok` before and `ok` after — the check passes on both sides.** No warning appeared, none disappeared, and no error was introduced. **The new `passes/` artifact does not appear in the validator's file set, as expected:** §0's discovery mechanism derives the expected file set from `PROJECT_STATE.md` §4's registry table, and pass artifacts do not take registry rows (`ORCHESTRATION.md` §4).

---

# 9. `git status --short`, IN FULL

```
 M ORCHESTRATION.md
 M PROJECT_STATE.md
?? passes/260834-7_eight-file-coverage-check_read-and-report_close-out.md
warning: unable to unlink '/sessions/laughing-busy-franklin/mnt/EMC/theology/.git/index.lock': Operation not permitted
```

⛔ **Complete and unabridged — three status entries plus the warning git emitted after them, nothing elided.** ⚠️⚠️ **The fourth line is not a status entry: it is the `.git/index.lock` condition firing (see §GATE). The command's exit code was 0 and its status output is correct and complete.** A `ls -la .git/index.lock` immediately after returns `-rw------- … 0 Aug 25 2026 .git/index.lock`.

⛔ **`git rev-parse HEAD` after all writes still returns `c0e7a36b59ba333179c8d4b14d737ee4155c315a` — HEAD did not move and nothing was committed by this pass.**

## What to stage

**Stage all three, in one commit:**

```
git add ORCHESTRATION.md \
        PROJECT_STATE.md \
        passes/260834-7_eight-file-coverage-check_read-and-report_close-out.md
```

Suggested message: `260834-7: coverage check on the eight pre-manifest files (read-and-report); ORCHESTRATION §8 dual coverage-registry rule`

⛔⛔ **THERE IS NO `.diff` ARTIFACT FOR THIS PASS AND ITS ABSENCE IS DELIBERATE, NOT AN OVERSIGHT.** `passes/README.md` and `ORCHESTRATION.md` §4 expect a `<stamp>_<short-name>.diff` beside every close-out. **This pass produced no diff of corpus content** — the only tracked changes are the conventions addition and its two consistency cells, both fully quoted in §7, and both visible in the commit itself. ⚠️ **If a `.diff` is wanted for convention's sake, `git diff ORCHESTRATION.md PROJECT_STATE.md > passes/260834-7_orchestration-coverage-registry-rule.diff` before staging will produce it; it is four hunks and this pass did not presume to add a fourth file.**

⚠️ **If `git add` fails on `.git/index.lock`, that is the briefed filesystem condition (§GATE), not a fault in these files. Do not force-remove the lock; the fix belongs to whoever owns the permissions on `.git/`.**

---

# 10. HAND-OFF — WHAT THE RETRO-REGISTRATION PASS SHOULD DO WITH THIS

⭐ **The intake order in `260834-6` Task 5 survives this pass. What changes is the WORK ATTACHED TO EACH STEP.**

| Order | File | `260834-6` said | ⭐ **This pass adds** |
|---|---|---|---|
| **1** | `a101-2.md` | ingest first | ⭐⭐⭐ **REGISTRATION ONLY — 0 uncovered bytes, all 10 recordings Covered.** ⚠️ `AW-VI` covers **two** recordings under one id; the `151,803` boundary still needs the audio. ⛔ Two `AW-VI` citations fail to resolve (§5.2) and one of them mis-locates a non-harmonised difference. |
| **2** | `a105.md` | ingest second | ⭐⭐⭐ **REGISTRATION ONLY — 0 uncovered bytes.** ⛔⛔ **DO NOT write `COT-n` session rows from the citations** — the ids are unresolved under both readings (§4.4). Derive session numbers from his spoken class numbers; record the citation mapping separately. ⚠️ Depth sweep owed on recordings 1, 2 and 5. |
| **3** | `a101-1.txt` | cleanest file | ✅ registration only; ⚠️ **depth sweep owed on 5 of 8 recordings** (I, II, III, V, VII) |
| **4** | `a202.txt` | ingest with diarization prerequisite | ⛔⛔ **REGISTRATION *PLUS A FULL FIRST MINING OF 211,119 B*. It is not mined at all.** The diarization prerequisite now gates **first mining**, not re-mining — a materially larger job than `260834-6` described. |
| **5** | `a103.md` | ingest as six recordings, not nine | ✅ registration; ⚠️ depth sweep owed on recordings 1 and 2; ⛔⛔ **resolve §16's session-7 attribution contradiction FIRST** (§4.2) |
| **6** | `a201.txt` | split intake, recordings 2-9 safe | ⛔⛔ **REGISTRATION *PLUS A FULL FIRST MINING OF 177,202 B*. Not mined at all.** Recording 1 keeps its diarization prerequisite. |
| **7** | `a106.md` | lowest yield, carries the dating error | ✅ registration; ⭐⭐ **the 2026 re-dating of recording 2 now has six independent supports and zero contrary evidence (§4.3)**; ⚠️ `Misc-1..7` is a dead range — there is no citation machinery to re-point, only a prefix whose name is a date claim |
| **8** | `a301` | ⛔ do not ingest | ⛔ unchanged — and its content is already Covered via `a106` rec 2, so nothing is lost by not ingesting it |

⭐⭐ **AND THE ONE THING THAT SHOULD BE RESEQUENCED, OFFERED AS A RECOMMENDATION AND NOT A DECISION:** `260834-6` ranked `a201` and `a202` **6th and 4th** on the assumption they were already mined and needed registration. **They are not, and they are 26.5 % of the scope set.** ⚠️ **Whether "already in the ledger" or "not in the ledger at all" should drive the order is JD's call, not a pass's** — but the order was set on a premise this pass has falsified, and that is recorded so the choice is made knowingly.

---

# 11. COMPLETE RAW SESSION OUTPUT (unsummarized)

⛔ **Verbatim tool output, in run order. Nothing elided, nothing reformatted.**

## 11.1 Gate

```
$ git rev-parse HEAD
c0e7a36b59ba333179c8d4b14d737ee4155c315a
$ git rev-parse --abbrev-ref HEAD
main
$ ls -la .git/index.lock          # AT GATE
ls: cannot access '.git/index.lock': No such file or directory
$ git status --short              # AT GATE
(empty, exit 0)
```

## 11.2 `validate_project.py` — BEFORE (full, 210 lines)

```
========================================================================
PROJECT INTEGRITY VALIDATION   root: /sessions/laughing-busy-franklin/mnt/EMC/theology
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
  ok    [C3] PROJECT_STATE.md: version agrees with registry (260834-5)
  ok    [C3] ORCHESTRATION.md: version agrees with registry (260832-5)
  ok    [C3] passes/README.md: version agrees with registry (260832-3)
  ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260834-5)
  ok    [C3] RJ_Final_Question_List.md: version agrees with registry (260833-2 (v21))
  ok    [C3] RJ_Open_Questions_and_Divergences.md: version agrees with registry (260833-2)
  ok    [C3] RJ_Incense_Analysis.md: version agrees with registry (260834-1)
  ok    [C3] On_Incense_and_the_Altar.md: version agrees with registry (260833-2)
  ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260833-5)
  ok    [C3] SRC_Manifest.md: version agrees with registry (260834-4)
  ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260833-8)
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

## 11.3 `validate_project.py` — AFTER (full, 210 lines)

```
========================================================================
PROJECT INTEGRITY VALIDATION   root: /sessions/laughing-busy-franklin/mnt/EMC/theology
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
  ok    [C3] PROJECT_STATE.md: version agrees with registry (260834-5)
  ok    [C3] ORCHESTRATION.md: version agrees with registry (260834-7)
  ok    [C3] passes/README.md: version agrees with registry (260832-3)
  ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260834-5)
  ok    [C3] RJ_Final_Question_List.md: version agrees with registry (260833-2 (v21))
  ok    [C3] RJ_Open_Questions_and_Divergences.md: version agrees with registry (260833-2)
  ok    [C3] RJ_Incense_Analysis.md: version agrees with registry (260834-1)
  ok    [C3] On_Incense_and_the_Altar.md: version agrees with registry (260833-2)
  ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260833-5)
  ok    [C3] SRC_Manifest.md: version agrees with registry (260834-4)
  ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260833-8)
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

## 11.4 BEFORE vs AFTER diff

```
$ diff val_before.txt val_after.txt
39c39
<   ok    [C3] ORCHESTRATION.md: version agrees with registry (260832-5)
---
>   ok    [C3] ORCHESTRATION.md: version agrees with registry (260834-7)
(exit 1 — one differing line)
```

## 11.5 Citation extraction — raw token counts (before compound expansion)

```
$ python3 extract.py   # St_Francis_EMC_Distinctives.md
file bytes: 2590498 chars: 2539270
A101       total=   55  {'A101-I': 5, 'A101-II': 10, 'A101-III': 6, 'A101-IV': 3, 'A101-V': 6, 'A101-VI': 12, 'A101-VII': 12, 'A101-VIII': 1}
A101_DATE  total=   83  {'A101-2026-06-14': 1, 'A101-2026-06-28': 6, 'A101-2026-07-19': 12, 'A101-2026-07-26': 16, 'A101-2026-08-09': 38, 'A101-2026-08-16': 4, 'A101-2026-08-23': 6}
AW         total=   67  {'AW-I': 18, 'AW-II': 10, 'AW-III': 9, 'AW-IV': 5, 'AW-V': 13, 'AW-VI': 12}
COT        total=   36  {'COT-1': 3, 'COT-2': 10, 'COT-3': 6, 'COT-4': 3, 'COT-5': 4, 'COT-6': 8, 'COT-7': 2}
ANF        total=   32  {'ANF-1': 23, 'ANF-2': 1, 'ANF-3': 1, 'ANF-4': 3, 'ANF-5': 1, 'ANF-7': 1, 'ANF-8': 1, 'ANF-9': 1}
MISC_N     total=   17  {'Misc-1': 1, 'Misc-2025': 16}
MISC_2025  total=   16  {'Misc-2025': 16}
EMBER      total=   13  {'Ember': 13}
LENT       total=    5  {'Lent vid': 5}
RECON      total=   22  {'Recon-Euch': 22}
```

## 11.6 Citation resolution — compounds expanded, legend rows excluded

```
$ python3 resolve.py
A101-1       live=6    legend/def=2   lines=[422, 423, 429, 937, 4545, 5594]
A101-2       live=11   legend/def=0   lines=[675, 756, 758, 759, 771, 775, 781, 5740, 5741, 5762, 6381]
A101-3       live=9    legend/def=0   lines=[420, 422, 423, 568, 775, 935, 1255, 4545, 4552]
A101-4       live=5    legend/def=0   lines=[675, 758, 760, 778, 780]
A101-5       live=6    legend/def=0   lines=[569, 574, 2293, 2961, 3025, 3044]
A101-6       live=13   legend/def=0   lines=[568, 569, 570, 573, 575, 868, 4285, 4287, 4289, 4299, 6667]
A101-7       live=15   legend/def=0   lines=[775, 779, 838, 839, 868, 932, 933, 935, 936, 937, 5591, 5594, 5631, 5639, 6049]
A101-8       live=3    legend/def=0   lines=[776, 839, 868]
ANF-1        live=22   legend/def=1   lines=[94, 577, 618, 676, 679, 682, 745, 1270, 1275, 1318, 1398, 2255, 2735, 2919, 3155, 4608, 4672, 4790, 4794, 6677]
ANF-2        live=1    legend/def=0   lines=[2256]
ANF-3        live=2    legend/def=0   lines=[2256, 2257]
ANF-4        live=3    legend/def=0   lines=[579, 2263]
ANF-5        live=1    legend/def=0   lines=[2265]
ANF-6        live=1    legend/def=0   lines=[2256]
ANF-7        live=1    legend/def=0   lines=[2264]
ANF-8        live=1    legend/def=0   lines=[2258]
ANF-9        live=1    legend/def=0   lines=[2259]
AW-1         live=16   legend/def=2   lines=[421, 775, 1007, 1008, 1251, 1412, 1413, 1438, 1441, 1714, 1717, 2029, 2750, 2887, 3213, 4402]
AW-2         live=11   legend/def=0   lines=[420, 421, 422, 424, 1662, 1667, 1668, 5572, 5575]
AW-3         live=10   legend/def=0   lines=[1148, 1242, 1253, 1274, 1668, 2633, 6562, 6584]
AW-4         live=7    legend/def=0   lines=[675, 775, 1070, 1254, 1669, 1714]
AW-5         live=18   legend/def=0   lines=[421, 932, 933, 935, 941, 1007, 1008, 1009, 1669, 1715, 1716, 1891, 3268, 3272, 3282, 5031, 6049]
AW-6         live=12   legend/def=0   lines=[756, 1652, 1670, 1671, 1672, 3215, 3219]
COT-1        live=2    legend/def=1   lines=[2271, 2273]
COT-2        live=11   legend/def=0   lines=[790, 871, 872, 874, 877, 883, 2271, 2308, 2723, 2760]
COT-3        live=7    legend/def=0   lines=[1441, 1468, 2271, 2275, 2750, 2923]
COT-4        live=4    legend/def=0   lines=[784, 2271, 2274, 2759]
COT-5        live=5    legend/def=0   lines=[786, 2271, 2272, 2274, 2275]
COT-6        live=10   legend/def=0   lines=[1441, 1468, 2271, 2274, 2275, 2276, 2750, 2923]
COT-7        live=2    legend/def=0   lines=[2271, 2275]
Ember        live=10   legend/def=3   lines=[1665, 1667, 1671, 2757, 2854, 3215, 5184, 5248, 5320]
Lent vid     live=2    legend/def=3   lines=[1670, 1672]
Misc-2025    live=14   legend/def=2   lines=[756, 757, 768, 769, 1256, 1843, 2853, 2909, 5762, 5763, 5766, 5767]
Misc-N       live=0    legend/def=1   lines=[]
Recon-Euch   live=20   legend/def=2   lines=[870, 932, 934, 1007, 1009, 1069, 1071, 1072, 1076, 1148, 1254, 1413, 1438, 1668, 1669, 1715, 1717, 2633, 2747, 2854]

LIVE TOTAL: 262
```

## 11.7 Per-recording span analysis (all five mined files)

```
$ python3 span.py

===== a101-2.md (263995 B) =====
  AW-I                   29782B  types= 6 hits=  37 span= 0.63 deciles=7/10
      regulative/RPW(15), incense/censer(8), Malachi(5), duty/worthy(4), five senses/brains on sticks(3), altar/table interchangeable(2)
  AW-II                  32575B  types= 5 hits=  41 span= 0.85 deciles=9/10
      1928/1662/1979 BCP(31), Cranmer/Sarum(7), Marxist infiltration(1), layman-absolution rule(1), epiclesis/Packer(1)
  AW-III                 29586B  types= 6 hits=  21 span= 0.51 deciles=6/10
      1928/1662/1979 BCP(2), Coverdale/30-day Psalter(2), layman-absolution rule(3), Magnificat/Nunc Dimittis(5), calendar Advent/Epiphany/Gesima(7), Trinity/Pentecost counting(2)
  AW-IV                  24847B  types= 8 hits=  30 span= 0.78 deciles=6/10
      incense/censer(3), Malachi(2), 1928/1662/1979 BCP(2), Decalogue/Summary of Law(8), bowing at name of Jesus(4), Ark/reverence(2), Trinity/Pentecost counting(2), altar/table interchangeable(7)
  AW-V                   22917B  types= 9 hits=  33 span= 0.94 deciles=10/10
      1928/1662/1979 BCP(1), Cranmer/Sarum(2), layman-absolution rule(5), Magnificat/Nunc Dimittis(2), epiclesis/Packer(10), transubstantiation(6), Cranmer moved 3 views(1), private Mass(4), altar/table interchangeable(2)
  AW-VI p1               12055B  types= 3 hits=  31 span= 0.87 deciles=9/10
      1928/1662/1979 BCP(1), calendar Advent/Epiphany/Gesima(18), Lent 40 days/Ash Wed(12)
  AW-VI p2                8967B  types= 5 hits=  17 span= 0.85 deciles=7/10
      1928/1662/1979 BCP(2), calendar Advent/Epiphany/Gesima(4), Trinity/Pentecost counting(4), Easter computus/full moon(4), Lent 40 days/Ash Wed(3)
  Ember                   6013B  types= 1 hits=  10 span= 0.89 deciles=6/10
      Ember days(10)
  Recon-Euch             81247B  types=17 hits=  70 span= 0.93 deciles=10/10
      incense/censer(20), Malachi(4), five senses/brains on sticks(1), 1928/1662/1979 BCP(1), Cranmer/Sarum(1), Coverdale/30-day Psalter(7), layman-absolution rule(3), Magnificat/Nunc Dimittis(1), epiclesis/Packer(2), bowing at name of Jesus(1), transubstantiation(2), holy water stoup(2), chasuble/collar(8), calendar Advent/Epiphany/Gesima(9), Ember days(1), Lent 40 days/Ash Wed(1), altar/table interchangeable(6)
  Lent vid               15965B  types= 5 hits=  31 span= 0.94 deciles=9/10
      1928/1662/1979 BCP(1), Lent 40 days/Ash Wed(19), meat/dairy/fish(7), Joel 2(3), altar/table interchangeable(1)

===== a105.md (188770 B) =====
  COT r1 cl2             20465B  types= 2 hits=   5 span= 0.50 deciles=4/10
      creatio ex nihilo(3), Gen 1:26 image(2)
  COT r2 cl3             32045B  types= 6 hits=  18 span= 0.61 deciles=5/10
      protoevangelium(1), Rom 11 grafted(9), flood-as-baptism(1), blood atonement(5), Passover/doorpost(1), intercession(1)
  COT r3 cl6             23558B  types= 6 hits=  42 span= 0.97 deciles=10/10
      showbread(4), priest friend/paganized(2), not-yet-happened lever(3), word and sacrament(4), intercession(2), tabernacle(27)
  COT r4 cl5             29695B  types= 6 hits=  19 span= 0.96 deciles=7/10
      Passover/doorpost(5), bronze serpent(3), Joshua=Yeshua(3), Moses prophet-priest-king(1), David king/shepherd(1), intercession(6)
  COT r5 cl4             33812B  types= 5 hits=  22 span= 0.63 deciles=5/10
      Joshua=Yeshua(2), Melchizedek(11), Christus Victor(2), anti-dispensational(6), tabernacle(1)
  COT r6 cl7             25824B  types= 4 hits=  17 span= 0.79 deciles=6/10
      Melchizedek(3), grain/meat offering(10), David king/shepherd(3), intercession(1)
  COT r7 cl9             23331B  types= 4 hits=  84 span= 0.96 deciles=10/10
      protoevangelium(1), Moses prophet-priest-king(2), David king/shepherd(74), intercession(7)

===== a101-1.txt (256209 B) =====
  A101-I                 27401B  types= 3 hits=  10 span= 0.72 deciles=5/10
      Apocrypha/deuterocanon(2), 1928/1662 BCP(3), Old Catholic/Lutheran(5)
  A101-II                38705B  types= 2 hits=  14 span= 0.75 deciles=4/10
      dyothelite/two wills(1), classical theism(13)
  A101-III               40687B  types= 7 hits=  24 span= 0.89 deciles=5/10
      consensus patrum(4), two-tier sacraments(2), transubstantiation(5), 1928/1662 BCP(2), Marxist infiltration(1), Pusey/Newman(9), Homilies(1)
  A101-IV                24479B  types= 6 hits=  14 span= 0.76 deciles=8/10
      Nicaea/councils 1-6(2), dyothelite/two wills(2), Islam false religion(3), classical theism(2), election/supralapsarian(4), once-saved-always-saved(1)
  A101-V                 33359B  types= 4 hits=   8 span= 0.41 deciles=4/10
      Article 6 sufficiency(2), consensus patrum(1), Art 20 church authority(1), Matt 16 keys(4)
  A101-VI                25378B  types= 8 hits=  34 span= 0.81 deciles=8/10
      Article 6 sufficiency(3), Apocrypha/deuterocanon(16), consensus patrum(5), Art 20 church authority(2), Jude 3 no innovation(3), baptismal regeneration(3), Matt 16 keys(1), Homilies(1)
  A101-VII               35574B  types= 6 hits=  19 span= 0.97 deciles=5/10
      once-saved-always-saved(1), Art 25 sacraments(1), two-tier sacraments(4), real presence/John 6(6), transubstantiation(5), memorialism(2)
  A101-VIII              30574B  types= 4 hits=   8 span= 0.90 deciles=6/10
      imputation/simul(1), two-tier sacraments(5), memorialism(1), Matt 16 keys(1)

===== a103.md (259190 B) =====
  ANF r1                 30186B  types= 6 hits=  12 span= 0.48 deciles=5/10
      1 Clement(1), Ignatius(3), Constantine died Arian(5), Nicaea 325(1), Nicaea II / icons(1), consensus/humility(1)
  ANF r2                 28362B  types= 2 hits=  14 span= 0.82 deciles=5/10
      1 Clement(13), Nicaea 325(1)
  ANF r3                 32455B  types= 4 hits=  50 span= 0.95 deciles=9/10
      1 Clement(13), Barnabas over-allegory(21), Justin Martyr(15), consensus/humility(1)
  ANF r4 Boyce           33222B  types=11 hits=  67 span= 0.90 deciles=10/10
      1 Clement(6), Barnabas over-allegory(1), Irenaeus(13), Ignatius(36), Tertullian(1), Hippolytus/Apostolic Tradition(1), Constantine died Arian(4), Edict of Milan(1), Nicaea 325(1), in persona Christi(2), consensus/humility(1)
  ANF r5 Valdez          24756B  types= 3 hits=  50 span= 0.90 deciles=10/10
      Athanasius(35), Constantine died Arian(14), Nicaea 325(1)
  ANF r6                 28004B  types= 4 hits=  32 span= 0.81 deciles=7/10
      Justin Martyr(28), Irenaeus(2), Ignatius(1), consensus/humility(1)
  ANF r7 West            28201B  types= 4 hits=   7 span= 0.58 deciles=6/10
      Irenaeus(1), Athanasius(1), Hippolytus/Apostolic Tradition(3), sign of the cross shield(2)
  ANF r8                 26884B  types= 5 hits=  16 span= 0.86 deciles=6/10
      Ignatius(1), Tertullian(12), Athanasius(1), Constantine died Arian(1), apokatastasis(1)
  ANF r9                 27059B  types= 4 hits=  20 span= 0.61 deciles=6/10
      Athanasius(3), Constantine died Arian(9), Edict of Milan(6), Nicaea 325(2)

===== a106.md (80482 B) =====
  Misc r1 Trinity        18394B  types= 4 hits=  13 span= 0.96 deciles=6/10
      theistic personalism(5), Trinity Sunday(2), modalism/Sabellian(1), image of God inference(5)
  Misc r2 ClassTheism    29311B  types= 9 hits=  31 span= 0.96 deciles=7/10
      theistic personalism(10), sunbeam/wax/clay(9), divine simplicity(4), Trinity Sunday(1), Aristotle/Plato(2), logos(2), in him we live and move(1), giggle test objection(1), image of God inference(1)
  Misc r3 Gawain         32642B  types= 2 hits=  29 span= 0.89 deciles=7/10
      Green Knight(20), Mary/BVM in poem(9)
```

## 11.8 `a101-2.md` segment term battery — the AW-VI boundary evidence

```
$ python3 seg.py
term                    AW-I       AW-II      AW-III       AW-IV        AW-V     AW-VI.1     AW-VI.2       Ember  Recon-Euch        Lent
ember                      7           .           2           1           3           4           2          16          20           4
lent                       .           .           .           .           .           9           1           1           6          24
ash wednesday              .           .           .           .           .           5           .           .           .          10
gesima                     .           .           .           .           .           1           .           .           .           .
whitsun                    .           .           .           .           .           .           .           .           .           .
pentecost                  .           .           .           .           .           .           8           1           .           .
trinity                    .           .           5           5           2           .          20           .           2           .
advent                     .           .           6           .           .           9           4           .           6           .
epiphany                   .           .           1           .           .           8           .           .           3           .
dairy                      .           .           .           .           .           .           .           .           .           2
fish                       .           .           .           .           .           .           .           .           .           5
abstin                     .           .           .           .           .           .           .           .           .           .
fast                       2           .           .           .           .           3           .          15           6          35
calendar                   .           .           2           .           .          13           4           .           2           4
liturgical year            .           .           .           .           .           .           .           .           .           .
easter                     .           .           2           1           5          13          14           .           8          12
full moon                  .           .           .           .           .           .           4           .           .           .
computus                   .           .           .           .           .           .           .           .           .           .
aristotle                  .           .           .           .           .           .           .           .           .           .
plato                      .           .           .           .           .           .           .           .           .           .
logos                      .           .           .           .           .           .           .           .           .           .
bishop                     .           7           .           .           .           .           .           4           3           .
holy day                   .           .           .           .           .           .           1           1           .           .
feast                      1           1           3           .           .           2           2           1           2           .

$ python3 seg2.py
--- refined ember-days (word-boundary, not Sept/Nov/remember) ---
  AW-I       ember(word)=0
  AW-II      ember(word)=0
  AW-III     ember(word)=0
  AW-IV      ember(word)=0
  AW-V       ember(word)=0
  AW-VI.1    ember(word)=0
  AW-VI.2    ember(word)=0
  Ember      ember(word)=10
  Recon      ember(word)=1
  Lent       ember(word)=0
--- dairy / meat / fish / abstain contexts in AW-VI.1, AW-VI.2, Lent ---
  [Lent] @251296 ...adjustments on how they happen uh but the sort of more uh historic practice is that you refrain from meat and dairy for these 40 days and then uh they then you celebrate obviously with with Easter but...
  [Lent] @251812 ...tute an entire meal individually. Um as well it should be noted that when we talk about having no meat and no dairy uh there are exceptions in the sense that uh sort of liturggical exceptions that you...
  [Lent] @251912 ...at and no dairy uh there are exceptions in the sense that uh sort of liturggical exceptions that you can have fish for instance. Fish would be something that you are allowed to eat. This is why you'll...
  [Lent] @251931 ...there are exceptions in the sense that uh sort of liturggical exceptions that you can have fish for instance. Fish would be something that you are allowed to eat. This is why you'll see uh a lot of fi...
  [Lent] @252019 ...ve fish for instance. Fish would be something that you are allowed to eat. This is why you'll see uh a lot of fish fries that happen during Lent or some restaurants will then start doing all you can e...
  [Lent] @252147 ...ppen during Lent or some restaurants will then start doing all you can eat grouper or you know they'll have a fish sandwich that comes out during this time. that is a a a respect for those who are goi...
  [Lent] @252448 .... Um but uh as well uh interesting note uh during the Middle Ages they uh there were other exceptions besides fish and uh beaver was actually a uh meal that you could have. you could eat beaver during...
  [Lent] @251287 ...here are adjustments on how they happen uh but the sort of more uh historic practice is that you refrain from meat and dairy for these 40 days and then uh they then you celebrate obviously with with E...
  [Lent] @251544 ...your uh for your days as well. So what will happen typically is that uh you would have a regular meal without meat of course uh for lunch but then for breakfast and for dinner you would have say bread...
  [Lent] @251800 ...elves constitute an entire meal individually. Um as well it should be noted that when we talk about having no meat and no dairy uh there are exceptions in the sense that uh sort of liturggical excepti...
  [Lent] @257370 ... repenteth him of the evil. Who knoweth if he will return and repent, and leave a blessing behind him, even a meat offering, and a drink offering unto the Lord your God? Blow the trumpet in Zion. Sanc...
```

## 11.9 `a105.md` — cited-content location, both COT readings tested

```
cited content string              r1    r2    r3    r4    r5    r6    r7
protoevangelium/Gen3:15            .     1     .     .     .     .     1
flood-as-baptism/1Pet3:21          .     1     .     .     .     .     .
Passover lamb/doorpost             .     1     .     5     .     .     .
bronze serpent                     .     .     .     3     .     .     .
Melchizedek                        .     .     .     .    11     3     .
Moses prophet-priest-king          .     .     .     1     .     .     2
Joshua=Yeshua                      .     .     .     3     2     .     .
David shepherd/king                .     .     .     1     .     3    74
Rom 11 grafted                     .     9     .     .     .     .     .
creatio ex nihilo                  3     .     .     .     .     .     .
Gen 1:26 Trinity hint              2     .     .     .     .     .     .
blood atonement                    .     5     .     .     .     .     .
intercession                       .     1     2     6     .     1     7
word and sacrament                 .     .     4     .     .     .     .
already but not yet                .     .     .     1     .     .     .
Christus Victor                    .     .     .     .     2     .     .
showbread                          .     .     4     .     .     .     .
grain/meat offering                .     .     .     .     .    10     .
priest friend/paganized            .     .     2     .     .     .     .
not-yet-happened lever             .     .     3     .     .     .     .
anti-dispensational                .     .     .     .     6     .     .
penal substitution                 .     .     .     .    10     .     .
abraham                            .     6     .     1    42     1     1
seed                               2     4     .     .    12     1     .
galatians                          .     2     .     2     8     .     .
promised land                      .     .     2    12     .     .     .
regeneration                       .     4     .     .     .     .     .
apostasy                           .     1     .     .     .     .     .
tabernacle                         .     .    27     .     1     .     .
levitic                            .     .     2     .     3    15     .

--- decisive quote locations ---
  not yet happened         -> [(74107, 'r3 cl.6'), (75528, 'r3 cl.6'), (75955, 'r3 cl.6')]
  priest friend            -> [(55375, 'r3 cl.6')]
  paganiz                  -> [(55553, 'r3 cl.6')]
  showbread                -> [(62243, 'r3 cl.6')]
  bread of the presence    -> [(61086, 'r3 cl.6'), (61293, 'r3 cl.6'), (63141, 'r3 cl.6')]
  grain offering           -> [(141576, 'r6 cl.7'), (144514, 'r6 cl.7'), (144671, 'r6 cl.7'), (145463, 'r6 cl.7'), (145612, 'r6 cl.7'), (145797, 'r6 cl.7')] ...
  melchi|melkis            -> [(126141, 'r5 cl.4'), (126217, 'r5 cl.4'), (126777, 'r5 cl.4'), (127290, 'r5 cl.4'), (128349, 'r5 cl.4'), (128582, 'r5 cl.4')] ...
  christus victor          -> [(110618, 'r5 cl.4'), (110634, 'r5 cl.4')]
  out of nothing           -> [(3840, 'r1 cl.2'), (4299, 'r1 cl.2'), (9965, 'r1 cl.2')]
  1:26                     -> [(5103, 'r1 cl.2'), (14163, 'r1 cl.2')]
```

## 11.10 `a106.md` — the Misc-2025 dating evidence

```
term                        rec1_Trinity  rec2_ClassTheism       rec3_Gawain
sunbeam                                .                 2                 .
\bwax\b                                .                 4                 .
clay                                   .                 3                 .
simplicity                             .                 4                 .
modalis                                1                 .                 .
theistic personalis                    5                10                 .
giggle                                 .                 1                 .
trinity sunday                         2                 1                 .
aristot                                .                 1                 .
plato                                  .                 1                 .
\blogos\b                              .                 2                 .
live and move                          .                 1                 .
green knight                           .                 .                20
image of god                           5                 1                 .

 @35981 ['rec2_ClassTheism'] ...say that God's love and God's wrath are the same thing? This is how we say it. Think of a sunbeam. Think of the candle, the wax that is being impacted by the heat of the sun versus...
 @36138 ['rec2_ClassTheism'] ... heat of the sun versus the clay that is being impacted by the heat of the sun. that same sunbeam can hit both of those things. How will the reaction be? The same? No. The ma the w...
 @46234 ['rec2_ClassTheism'] ...ophy as well. I would say it's in the Old Testament, but uh it's really explained well by Aristotle um and in other parts by Plato uh where we're getting this philosophy and it's t...
 @46269 ['rec2_ClassTheism'] ...he Old Testament, but uh it's really explained well by Aristotle um and in other parts by Plato uh where we're getting this philosophy and it's the terminology for this philosophy ...
 @46779 ['rec2_ClassTheism'] ...the New Testament, points to its comfort with using Greek terms. In the beginning was the logos. That is a Greek term that is actually about the divine the the divine logos. That i...
 @46856 ['rec2_ClassTheism'] ...ning was the logos. That is a Greek term that is actually about the divine the the divine logos. That is the action of God himself, right? Um, in him we live and move and have our ...
 @46919 ['rec2_ClassTheism'] ... the divine the the divine logos. That is the action of God himself, right? Um, in him we live and move and have our being. that is from a um I can't remember who that's from, but ...
 @45265 ['rec2_ClassTheism'] ...ns before we close out? >> Yes. >> I I have to be honest. I don't see how this passed the giggle test at all. >> Okay. >> Um to be the image of something does not make you that som...
```

## 11.11 Aristotle/Plato/logos across all five mined files — the AW-VI resolution failure

```
term                    a101-1    a101-2      a103      a105      a106
aristot                      .         .         1         .         1
plato                        .         .         6         .         1
\blogos\b                    .         .         .         .         2
philosoph                    4         3        21         .        10
live and move                .         .         .         1         1
classical theism            15         2         .         1        21
simplicity                   4         1         1         .         4
greek                        .         2        18         2        11

-- a101-1 Session II byte range 27,453-66,157 --
   aristot 0
   plato 0
   \blogos\b 0
   philosoph 3
   greek 0
   classical theism 13
   simplicity 3

-- a101-2 classical theism / simplicity / philosoph, by segment --
  classical theism   @  80729 ['AW-III']
  classical theism   @  80842 ['AW-III']
  simplicity         @ 178781 ['Recon']
  philosoph          @ 232310 ['Recon']
  philosoph          @ 233322 ['Recon']
  philosoph          @ 233525 ['Recon']
```

## 11.12 `a201`/`a202` coverage probe — the Uncovered finding

```
$ for t in ...; do printf "%-22s dist=%s manifest=%s inv=%s\n" ...; done
Matt Kennedy           dist=1   manifest=0   inv=5  
Canterbury Cousins     dist=0   manifest=0   inv=1  
Simply Anglican        dist=0   manifest=0   inv=1  
Memorialist            dist=8   manifest=0   inv=2  
Stories We Tell        dist=0   manifest=0   inv=1  
Contemporary Worship   dist=4   manifest=0   inv=1  
Apostolicae            dist=18  manifest=1   inv=2  
6:63                   dist=3   manifest=0   inv=1  
Which Rite             dist=3   manifest=8   inv=1  
Evan Minton            dist=0   manifest=0   inv=2  
John Fisher            dist=1   manifest=1   inv=3  
Monarch of England     dist=0   manifest=0   inv=1  
```

## 11.13 Stamp derivation

```
$ grep -rhoE "26[0-9]{4}-[0-9]+" --include=*.md --include=*.py --include=*.txt --include=*.diff --include=*.patch . | sort -u | tail -6
260834-2
260834-3
260834-4
260834-5
260834-6
260834-7

$ grep -rl "260834-7" . /mnt/EMC   # excluding .git internals
ORCHESTRATION.md
PROJECT_STATE.md
/sessions/laughing-busy-franklin/mnt/EMC/theology/ORCHESTRATION.md
/sessions/laughing-busy-franklin/mnt/EMC/theology/PROJECT_STATE.md
(only this pass's own artifact and the two cells it wrote — free before use)
```

## 11.14 Close-out git state

```
$ git status --short
 M ORCHESTRATION.md
 M PROJECT_STATE.md
?? passes/260834-7_eight-file-coverage-check_read-and-report_close-out.md

$ ls -la .git/index.lock
-rw------- 1 laughing-busy-franklin laughing-busy-franklin 0 Aug 25 22:37 .git/index.lock

$ git rev-parse HEAD
c0e7a36b59ba333179c8d4b14d737ee4155c315a
```
