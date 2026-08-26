# 260835-4 — `File 45` (`a201.txt`) "FIRST MINING", Pass B2 — CLOSE-OUT

**⛔⛔⛔ HEADLINE: THE BRIEF'S PREMISE IS FALSE. `File 45` HAS BEEN MINED SINCE `260621-1`. NOTHING WAS MINTED, AND THE REASON IS EVIDENCE, NOT CAUTION.**

---

## 0. GATE

| Check | Briefed | Observed | Verdict |
|---|---|---|---|
| `git rev-parse HEAD` | `9882dc3` | `9882dc3d23fc5a97fed55a26b91afd3886ec2ccc` | ✅ exact |
| Branch | — | `main` | ✅ |
| Working tree before first edit | must capture | `git --no-optional-locks status --short` → **EMPTY**, exit 0 | ✅ **captured directly** |
| `PROJECT_STATE.md` stamp at gate | report | **`260835-3`** (created `260724-3`) | ✅ |
| Next-free pass stamp | derive | **`260835-4`** | ✅ |
| Next-free `LS` | re-derive fresh | **`LS-129`** | ✅ free — ⛔ **NOT consumed** |

### 0.1 ⭐⭐ The clean-tree capture that `260835-3` could not make

`260835-3` recorded, against itself, that *"`git status --short` before the first edit was NOT captured, and that is stated rather than glossed,"* and reconstructed its clean-tree claim instead. **This pass captured it directly, before any write, and it was empty with exit 0. The gap is discharged.**

### 0.2 ⭐ The `.git` lock — applied, not re-derived, and not re-encountered

`260835-3` established the mechanism: the repo sits on a FUSE mount that denies `unlink`, so an ordinary `git status` takes `index.lock` and cannot remove it, manufacturing its own stale lock. **This pass applied that finding rather than rediscovering it: every git read used `git --no-optional-locks`, which does not take the lock.**

⛔ **No lock was created by this pass. None was removed. No `rm` was attempted. No permissions were changed.** The `--no-optional-locks` invocation is disclosed here as a read-only workaround, **not** as a fix.

### 0.3 Stamp derivation

`grep -rhoE '\b26[0-9]{4}-[0-9]+\b'` across the repo (excluding `.git`): highest existing stamp is **`260835-3`**. `grep -rn '260835-4'` returns **zero hits**. ⭐ `260834-10` exists in the repo as a *discussed alternative* only (the `260835-1` §0.3 ambiguity note), never as a stamp in use; this pass follows the `260835-1`/`-2`/`-3` precedent of advancing the day-group field.

### 0.4 `LS` re-derived fresh, not copied

- `validate_project.py` `C2`: **`LS-1..128` unbroken, no duplicates.**
- Independent enumeration of every `LS-n` in the repo: max **129**.
- **Every `LS-129` occurrence repo-wide was read in context**: 19 files, and each is a *next-free registry assertion* (`"next-free values … `LS-129`"`), not a live ledger entry.
- **Verdict: `LS-129` was free.** ⛔⛔ **It was NOT consumed. Next free remains `LS-129`.**

### 0.5 ✅ VALIDATOR — BASELINE

```
80 ok · 9 warnings · 0 errors
```

**All nine firing codes, individually, in order:**

| # | Code | Warning |
|---|---|---|
| 1 | `C1` | `src/SRC_Discord_RPW.md`: 2 relative timestamp(s) outside message headers (`'Yesterday at …'`) |
| 2 | `C3` | `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md`: no parseable 'Last updated' stamp; registry says `260832-2` |
| 3 | `C3` | `tools/transcribe_yt.py`: no parseable 'Last updated' stamp; registry says `260833-7` |
| 4 | `C4` | `St_Francis_EMC_Distinctives.md`: 2 passage(s) describe an ANSWERED question as pending with no supersede marker |
| 5 | `C5` | `RJ_Final_Question_List.md`: 17 volatile-state assertions |
| 6 | `C5` | `RJ_Incense_Analysis.md`: 9 volatile-state assertions |
| 7 | `C5` | `St_Francis_EMC_Distinctives.md`: 7 volatile-state assertions |
| 8 | `C10` | §15's newest `LS` citation is 8 findings behind the ledger (`LS-120` vs `LS-128`) |
| 9 | `C11` | outline last checked against `IP-97` (`260833-5`); the `IP` ledger now runs to `IP-108`. 11 finding(s) unreviewed |

⚠️ **This is an 80/9 baseline. `260835-3`'s own gate note records `81 ok · 8 warnings`; the difference is `C3`'s stamp check on `Calvin_Luther_…` and `tools/transcribe_yt.py` moving between `ok` and `WARN` as stamps change. Reported, not investigated — it is not this pass's brief.**

---

## 1. ⛔⛔⛔ THE STOP CONDITION

### 1.1 The evidence, quoted verbatim

`St_Francis_EMC_Distinctives.md` **L6971**, changelog entry `v1.4`, read directly at `HEAD`:

> `v1.4 - 260621-1: **Reconciled the GV batch (General Videos, Videos 1-13; findings GV-1 .. GV-55)** against live state, from the append-mode unified patch queue (Unified_Patch_Queue_GV_260621). Source files a201.txt (Videos 1-9) and a202.txt (Videos 10-13); GV numbering unbroken across both.`

**`a201.txt` is `File 45`. `a201.txt` is the `GV` batch's source. `File 45` was mined on 260621-1 — roughly three months before `260834-9` retro-registered it as never mined.**

### 1.2 What this falsifies

| Claim | Where | Status |
|---|---|---|
| *"`File 45` … ⛔ **NONE — WHOLLY UNMINED**"* | `SRC_Manifest.md` L3310 | ⛔ **FALSE** |
| *"⛔ **NONE — REGISTERED BUT UNMINED**"* ×9 | `SRC_Manifest.md` L2622-2630 | ⛔ **FALSE** ×9 |
| *"`a201.txt` … and `a202.txt` … have **NEVER been mined**"* | `SRC_Manifest.md` L2638 | ⛔ **FALSE** |
| *"they carry no pre-manifest prefix **and are cited by nothing**"* | `SRC_Manifest.md` L2638 | ⚠️ **half false** — see 1.4 |
| *"⛔⛔ **FIRST MINING of 177,202 B**"* | `260834-9` close-out L381 | ⛔ **FALSE** |
| *"`FINDING RANGE PENDING PASS B`"* ×9 | `SRC_Channel_Inventory.md` | ⛔ **FALSE** |
| The brief's *"registered but never mined… No prefix, cited by nothing"* | this pass's brief | ⛔ **FALSE** |

### 1.3 ⛔⛔ Why minting would have been the worst available outcome

`260834-6`'s own close-out named this hazard in terms: the duplicate risk for these files is **"not a duplicate SOURCE; it is a duplicate FINDING minted under a second prefix."**

**Minting `LS-129`… over `a201.txt` would have created a second, parallel set of tags for roughly thirty findings that already exist as `GV-n`** — with different wording, different byte ranges, and no cross-reference, in a corpus whose whole value is that a claim can be traced to one place. ⛔ **The brief instructed a first mining. The evidence forbade it. The evidence won.**

### 1.4 ⭐⭐ Why `260834-7`'s title-probe was not negligent — and the method defect that is worth more than the instance

`260834-7` probed `Matt Kennedy`, `Canterbury Cousins`, `Simply Anglican`, `Stories We Tell`, `Evan Minton`, `Monarch of England` across three documents and got **zero**. That result is **correct**. It is also **uninformative**, because:

⛔⛔ **`GV` FINDINGS NEVER CITE TITLES.** Fifty of the fifty-five carry no source locator at all beyond `[Stated, GV-n]`. The five that do carry an internal scheme — `a201 L13/V6`, `a201 L15/V7`, `a201 L17/V8`, `a202 L2/V10`, `a202 L8/V13` — which no title probe can see.

⭐ **The clause *"cited by nothing"* is withdrawn. The clause *"no pre-manifest prefix"* STANDS** — there is no `a201`-specific prefix; the findings live under `GV`, whose legend row (L389) names only *"General Videos batch (Videos 1-13)"* and enumerates nothing.

⚠️ **Note the contrast the legend table itself supplies: the `RC` row two lines below DOES enumerate its seven videos by title. The `GV` row is the un-enumerated one.**

⏳ **OWED, NOT WRITTEN: an `ORCHESTRATION.md` §8 amendment — a "cited by nothing" verdict must probe SOURCE-FILE NAMES and the findings corpus's CHANGELOG, not only titles.** This pass did not touch `ORCHESTRATION.md`.

---

## 2. ⭐⭐ THE `V`-NUMBER DECODER — RECOVERED, CONFIRMED, AND RECORDED AS AN INFERENCE

**Scheme:** the source files use banner/body line pairs, so video *n* opens at line `2n+1`. `a201.txt` has 22 lines / 10 `==` markers / 9 recordings; `a202.txt` has 8 lines / 4 recordings.

| Label | Decodes to | Confirming content | Located by this pass |
|---|---|---|---|
| `a201 L13/V6` (`GV-30`) | `a201` **recording 6** | *"Book of Common Prayer in 1928 with incense ad orientem"* | ⭐ **`@113,903`, read off the tape by this pass** |
| `a201 L17/V8` (`GV-37`) | `a201` **recording 8** | 1662 *"the most official version … all prayer books are supposed to conform theologically to"* | **`@163,999`** |
| `a201 L17/V8` (`GV-36`) | `a201` **recording 8** | *"I would hold much more towards Luther's position"* | **`@157,799`** |
| `a201 L15/V7` (`GV-31`/`32`/`33`/`34`) | `a201` **recording 7** | biographical material; *"the diocese of mid-america"* | corroborated by `SRC_Manifest.md` L3383's `@114,931`, inside rec 7 |
| `a202 L8/V13` (`GV-54`) | `a202` **recording 4** | *"Liturgical edition switched 1928 → ACNA 2019"* vs. that recording's title | ⛔ not opened |

**⇒ `a201` Videos 1-9 = recordings 1-9 in manifest row order; `a202` Videos 10-13 = recordings 1-4.**

⛔⛔ **THE DECODER IS AN INFERENCE FROM FIVE SURVIVING LABELS AND IS RECORDED AS ONE.** `Unified_Patch_Queue_GV_260621` occurs **exactly once in the entire repo — inside L6971 itself** — and does not exist on disk; `passes/` reaches back only to `260832`. **The `GV` batch's per-video provenance was never written down and cannot now be reconstructed, only inferred.**

⏳ **Retro-registering byte ranges for the 50 unlocated `GV` findings is OWED. NOT done here.**

---

## 3. ⭐⭐⭐ THE PASS'S REAL PRODUCT — RECORDING 1 DIARIZED, AND FOUR MISATTRIBUTIONS FOUND

### 3.1 The artifacts, located as instructed

`~/EMC/original transcripts/video transcripts/redownloads/Kennedy-Assurance-{meta,sentences,timestamps}.json`, `-transcript.srt/.txt`, `-youtube.srt`.

`-meta.json` confirms: `source_url` `https://www.youtube.com/watch?v=xk2zB2LEcF8` · `upload_date` **2023-11-24** · `duration_seconds` **2536** · channel **"Barely Protestant (Fr James)"** · `speech_models` **`universal-3-5-pro`** · **`speaker_labels: true`**.

**399 sentences, word-level speaker labels, two speakers (A = 233, B = 166), reduced to 98 turns and read in full.**

### 3.2 ⭐⭐ Both speakers established from the tape's own content, then confirmed by the diarization

**This is deliberately not circular — the identifications do not rest on the machine labels.**

| Evidence | Turn | Establishes |
|---|---|---|
| *"I'm with **Father James Gadd, who's a friend of mine**"* | T0 (A), 0:03 | **A is not Rev. James** |
| *"I don't want to put words in your mouth, **Father James**"* | T2 (A), addressed across | **A is not Rev. James** |
| *"how would you **describe yourself?**"* → *"I would say I'm comfortable with Anglo-Catholic"* | T76 (A) → T77 (B) | **B is the one being asked** |
| *"What is your— it's **Barely Protestant**?"* → *"**Barely Protestant.**"* | T90 (A) → T91 (B), 41:04 | **B owns the channel = Rev. James** |
| Video title *"Talk with **Fr Matt Kennedy**"*; A names *"Stand Firm"*, *"Preventing Grace Podcast, the one I do with my wife"* | T0 (A) | **A = Fr Matt Kennedy** |

⛔ **Neither speaker is EAR-verified. Both are established from tape content plus machine diarization. That is stronger than the undiarized state and weaker than an ear check, and it is recorded at that strength.**

### 3.3 ⛔⛔⛔ FOUR MISATTRIBUTIONS — KENNEDY'S WORDS CARRIED AS REV. JAMES'S

**Every one located twice: by byte range in `a201.txt` (the registered source) and by timestamp + speaker in the diarization.**

#### (a) ⛔⛔ `GV-2` — *"I consider myself High church"* is **Fr Matt Kennedy's**

- **`a201.txt @31,131`** · diarization **35:50, Speaker A**
- Full sentence: *"**I consider myself high church**, but more— **how would you describe yourself?** Lutheran Anglican?"*
- ⭐⭐ **The self-label and the question put to Rev. James are ONE SENTENCE.** Rev. James's actual answer, three seconds later: *"I would say I'm comfortable with Anglo-Catholic"* (**35:53, Speaker B**, `@31,405` region).
- ⭐ **The string `consider myself High church` occurs EXACTLY ONCE in all 177,254 bytes of `a201.txt`.**
- **Corpus location:** `St_Francis_EMC_Distinctives.md` **L439**, the GV self-identification cluster, tagged `[Stated, GV-2, GV-10, GV-11, GV-12, GV-25]`.

⭐⭐ **THE CLAIM SURVIVES THE QUOTATION, AND THIS MUST BE SAID AS LOUDLY AS THE ERROR.** Recording 2 `@42,688` has him, **solo**, saying *"an anglican such as myself **a high church anglican an anglo catholic** even a sort of more caroline divine reformed anglican uh someone who might call himself a reformed catholic"* — which is **`GV-10`, correctly attributed**. **Rev. James does describe himself as high church. He simply never said the sentence `GV-2` quotes.**

#### (b) ⛔⛔⛔ `GV-3` — the Augustinian-receptionism datum is **Kennedy's, entire, both halves**

- **`a201.txt @10,416`-`@11,100`** · diarization **11:50 and 11:55, Speaker A**
- *"this goes back to **Augustine, in my view**. Augustine, I think, even said that all the sacraments … are **received by faith**, so that … the reason communion is effective in the soul of a believer is because he is **taking hold of Christ by faith through the bread and the wine**, and I would say the same thing is true with baptism."*
- **Corpus location:** L949 — *"**Augustinian receptionism on both sacraments (GV-3).** Communion is effective because the believer 'is taken hold of of Christ by faith through' the elements; 'same … with baptism.'"* **[Stated, GV-3]**

⭐⭐⭐ **AND THE CONSEQUENCE IS A GAIN, NOT A LOSS.** `GV-3` is cited in §8 as *"Augustinian benefit-by-faith"* **alongside** `GV-15`'s *"real presence sacramental union … physically united to the bread and the wine."* Those two sit awkwardly together — a receptionist datum beside a corporeal one. **Removing Kennedy's sentence removes an apparent internal inconsistency in Rev. James's eucharistic position that was never his.**

#### (c) ⛔⛔⛔ `GV-4`'s second half — *"regeneration has to precede Faith"* — is **Kennedy's**

- **`a201.txt @7,830`** · diarization **8:50 and 9:02, Speaker A**
- *"**Actually, I do believe regeneration has to precede faith**, but I don't … make a necessary link between spiritual regeneration and baptism. So, that **regeneration could take place anytime** in a person's life."*
- **Corpus location:** L887 — *"Regeneration is 'definitely received' by valid baptism (GV-4); **but he also holds** 'regeneration has to precede Faith' and is not necessarily tied to baptism's *moment* ('could take place anytime')"*, presented as the **"terminus-not-trigger refinement" (`GV-4`, `GV-26`)**.

⛔⛔⛔ **THIS IS THE MOST CONSEQUENTIAL OF THE FOUR. The *"but he also holds"* clause is HIS INTERLOCUTOR'S CONTRARY POSITION. THERE IS NO TENSION, AND THEREFORE NOTHING TO REFINE — the entire analytical move rests on two men's words stitched into one.**

✅ **`GV-4`'s FIRST half is correctly his:** *"by the time someone is validly baptized, which is Trinitarian baptism … that person has **definitely received regeneration**"* (`@2,552`, **2:44, Speaker B**). ⭐ **And at 8:16 he states the OPPOSITE of Kennedy expressly, in his own voice: *"it seems like you're saying that it's faith that precedes regeneration, whereas **I'm putting regeneration preceding faith**."***

#### (d) ⛔⛔ `GV-6`'s *"rejects both Lordship Salvation and cheap grace"* is **Kennedy's**

- **`a201.txt @25,978`-`@26,081`** · diarization **29:45 / 29:51, Speaker A**
- *"**I'm not a lordship salvation guy**, um, at all. **I'm not a cheap grace guy either**, but I'm not a lordship salvation guy."*
- **Corpus location:** L794.

✅ **`GV-6`'s MAIN half IS correctly his** — apostasy of the genuinely regenerate, and faithlessness (2 Tim 2:13) distinguished from apostasy: *"if we are faithless, he remains faithful, for he cannot deny himself … it's a denial of Christ that kicks me out of the Kingdom"* (`@19,363`, **22:11/22:25, Speaker B**), reinforced at **28:16-28:57, Speaker B**.

### 3.4 ✅ WHAT THE AUDIT CLEARS — and it clears more than it convicts

| Finding | Quotation | Location | Verdict |
|---|---|---|---|
| **`GV-1`** | *"I reject the Roman understanding of justification, definitely"* | `@31,405` · **36:06, B** | ✅ **correct** |
| **`GV-5`** | *"a promise given … to me, rather than a … psychological state within myself"* | **2:09, B** | ✅ **correct** |
| **`GV-6`** (main) | 2 Tim 2:13; faithlessness ≠ apostasy | `@19,363` · **22:11, B** | ✅ **correct** |
| **`GV-9`** | *"the Catechism of 1571 or whichever"*; *"the faith of the family, of the parents … take hold for that child"* | `@4,966` / `@5,069` · **5:33 / 5:43, B** | ✅ **correct** |
| **`GV-7`** | *"Barely Protestant"* nickname; *"I'm historically Protestant"* | **41:04 / 41:20, B** | ✅ **correct** |

⚠️ **`GV-22` — a correction that makes it SAFER, not weaker.** Its *"I'm not even Catholic"* and the ~75%-agreement figure are **not in recording 1 at all**. They are **recording 4, `@67,653`, SOLO** — *"on Roman Catholicism which obviously I'm not even Catholic"* and *"about 75% of the critiques he gave against Rome I agreed with fully."* **A solo recording carries no attribution risk.**

⚠️⚠️ **THE RESIDUAL RISK IS NOT ZERO AND IS STATED PLAINLY: the `260834-6` close-out independently flagged `a201 @11,342` (*"it does take the burden and weight … focusing on the objective promises"*) and `@11,489` (*"takes the burden off of the subjective person"*) as Kennedy's. This pass's diarization CONFIRMS both (T26/T28, Speaker A). Any `GV` finding drawing on the assurance register of recording 1 needs the same check applied finding by finding — and 50 of 55 carry no locator to check against.**

### 3.5 ⚠️⚠️ A DATING DEFECT FALLS OUT OF THE SAME DISCOVERY

- **L389**, the `GV` legend, dates the batch **"2024-era"**.
- **L487**: *"The nearest self-description in his own voice is **not** `LS-9` (2022) but **GV-10 / GV-2 (2024-era)**"*.
- **L466**: the label is *"attested 2019 → 2020 → 2022 (`LS-9`) → **2024 (`GV-10`)** → masthead (`EXT-2`)"*.

⛔⛔ **Eight of the nine `a201` recordings are 2020-2022; the ninth is 2023-11-24. Recording 2, which carries `GV-10`, is 2021-02-19. There is no 2024 node. The L487 correction INVERTS: `GV-10` is OLDER than `LS-9`, not newer.** ⏳ **`VP-5`'s DELTA reasoning at L490 depends on it. ⛔ NOT touched.**

---

## 4. THE MINING WAS DONE ANYWAY — REPORTED AS *MATERIAL PRESENT*, NOT AS FINDINGS

⭐ **A de-duplication verdict from a pass that has not read the source is worthless, so all nine recordings were read.** Recording 1 via the 98-turn diarized transcript; recordings **3, 4, 5, 6 read directly** in this session; recordings **2, 7, 8, 9** via delegated full reads with verbatim-quotation-and-byte-offset requirements.

⛔⛔ **NOTHING BELOW IS A FINDING. NO NUMBER IS CONSUMED. Each item is tagged with the `GV` finding that already holds it, where one does.**

### 4.1 Already held — the de-duplication result

| Material | Recording | Already held as |
|---|---|---|
| *"real presence sacramental union … physically united to the bread and the wine"* (`@45,306`) | 3 | **`GV-15`** |
| Multiplication-by-miracle; *extra Calvinisticum* rejected (`@62,806`-`@64,306`) | 3 | **`GV-16`** |
| Anamnesis as mystical union with the Passover night (`@58,306`-`@59,306`) | 3 | **`GV-17`** |
| The *"1500 years"* patristic-consensus rule; Ignatius d. 107 (`@54,806`-`@56,306`) | 3 | **`GV-18`** |
| Belgic / Westminster / LBCF used against memorialism (`@44,306`) | 3 | **`GV-19`** |
| Essence-realist *"I am the door"* exegesis (`@48,306`-`@50,806`) | 3 | **`GV-20`** |
| John 6:63 *"flesh"* = one's own power; symbolic reading *"blasphemous"* (`@70,153`-`@72,653`) | 4 | **`GV-21`** |
| Baptism *"an actual effectual sign as it says in the thirty-nine articles"* (`@103,500`) | 5 | **`GV-23`** |
| *"baptism actually gives you that faith and repentance"* (`@85,000`) | 5 | **`GV-26`** ⚠️ see 4.2 |
| Circumcision/baptism continuity, Col 2:11-12, *"a widening not a replacing"* (`@91,500`-`@94,000`) | 5 | **`GV-27`** |
| Instruments/contemporary songs *"not in and of themselves a problem"* (`@106,903`) | 6 | **`GV-28`** |
| Man-centred worship *"is idolatry"*; high-church vestments equally liable (`@108,903`-`@109,903`) | 6 | **`GV-29`** |
| *"Book of Common Prayer in 1928 with incense ad orientem"* (`@113,903`) | 6 | **`GV-30`** |
| Celtic-vs-Roman even-handedness; Whitby (`@38,045`-`@40,667`) | 2 | **`GV-14`** |
| *"high church anglican, an anglo catholic, even … caroline divine"* (`@42,688`) | 2 | **`GV-10`** |
| Zwingli/transubstantiation *"not allowed"*; *"much more towards Luther's position"* (`@157,799`) | 8 | **`GV-36`** |
| 1662 *"all prayer books are supposed to conform theologically to"* (`@163,999`) | 8 | **`GV-37`** |
| Article 27 + 1662 rite; *"an Anglican thing … explicitly in our formularies"* (`@159,155`-`@172,497`) | 8 | **`GV-38`** |
| Anglicans do not deny eucharistic sacrifice; *"abundantly not the case"* (`@174,702`) | 9 | **`GV-41`** |
| *"we don't try to improve upon the blueprints"* (`@132,581`) | 7 | **`GV-35`** |
| 1928 + ACNA catechisms (`@121,581`); *"diocese of mid-america"* (`@132,081`) | 7 | **`GV-32`**, **`GV-34`** |

### 4.2 ⭐⭐ Two items genuinely NOT held — the strongest candidates if JD rules that minting proceeds

**(a) ⭐⭐⭐ THE `Acts 2:37-39` ANTECEDENT — recording 5, `@84,500`-`@85,500` and `@97,000`-`@99,000`.**

> *"just because there is an order does not mean that it necessarily has to go that way and in fact **if you are Augustinian like I would be I would consider myself sort of a semi Augustinian you understand that baptism actually gives you that faith and repentance** because baptism is regenerative as talks about in first Peter so the fact is that **baptism itself gives you that repentance and is actually the actual act of repentance**"* — `@84,900`-`@85,200`

> *"so far we have looked at **acts 2:38 and you know 37 38 39** and there's there's nothing there all it says is **repent and be baptized** and he assumes that that means you have to first repent … **no both are put together**"* — `@97,346`-`@97,600`

> *"baptism is the gift that you receive from the church from Christ through the church … **just like faith is a gift just like repentance is a gift** these are all gifts from God"* — `@98,900`-`@99,000`

⭐⭐⭐ **THIS IS THE 2020 ANTECEDENT OF THE DISCORD STATEMENT THE BRIEF NAMES — that faith and repentance are part of the promise given in baptism, `Acts 2:38-39` — on the SAME TEXT, six years earlier, with the same structural move: repentance and faith are not prerequisites brought TO baptism but gifts given IN it.**

⚠️ **`GV-26` holds the *"gives you that faith and repentance"* clause. It does NOT hold the Acts 2:37-39 exegesis, the *"both are put together"* rule, or the *"faith is a gift … repentance is a gift"* generalisation.** ⭐ **Known Gap 5's current-voice side was recorded as empty for a decade; this is 2020 material inside that decade bearing directly on the CONSTITUENT STRUCTURE of the baptismal promise.**

**(b) ⭐⭐ THE BURDEN RULE — recording 5, stated four times.**

| Location | Wording |
|---|---|
| `@86,000` | *"**you need to establish that within Scripture itself and we don't see that established**"* |
| `@94,500` | *"if you're going to make that **monumental shift** of this understanding **that needs to be demonstrated in Scripture** … it needs to be clear it needs to be **more than just implications** if you interpret it a certain way"* |
| `@96,500` | *"the position is not well we have to assume believers baptism and then try to find reasons … **if that restriction is going to be added it needs to be demonstrated within Scripture**"* |
| `@106,500` | *"**if we're going to switch those presuppositions we have to explain why from Scripture itself**"* |

⭐⭐ **The rule's SHAPE: the onus lies on whoever asserts a CHANGE or a RESTRICTION to a received practice — a continuity presumption. That is `DQ-24`(b)'s shape (*"The onus is upon the innovator who insists that we must have these particular practices done"*) running in the opposite direction, six years earlier.**

⛔⛔⛔ **AND IT IS EXPRESSLY NOT LOGGED AS SUPPORTING THE INCENSE LEVER. It is stated about a practice carrying an explicit covenantal sign (circumcision → baptism, Col 2:11-12), and the *"monumental shift"* framing PRESUPPOSES an established prior practice among the people of God. Whether incense qualifies is the contested question itself. Using this to argue that objectors to incense bear the burden would be exactly the move `260834-6` warns against — and it would be answered by his own *"uniquely Old Testament"* qualifier (`260835-1`). ⛔ It cuts both ways and is recorded both ways.**

⚠️ **Note against `260834-6`'s ABSENCE 4:** that pass recorded `burden of proof` as **zero** in `a201` and both `burden` hits as Kennedy's. **Both statements are literally true and both are confirmed here. The burden RULE is nonetheless present in recording 5 — stated four times without ever using the word *"burden."*** ⭐ **A textbook instance of the brief's own warning: `260835-1` established that `antitype`/`typolog-` return zero in `a105` while the material is present in bulk. The same failure mode, in a different file, caught by reading.**

### 4.3 ⭐⭐ Other material present, reported for the record

- ⭐⭐ **`DQ-9` / `OQ21` — recording 6 `@113,403`-`@113,903`, and it is the most quotable and most abusable line in the file.** *"you can have a contemporary sort of style worship **if that is the the tradition of your denomination** I'm not telling you to do it like an Anglican service using the Book of Common Prayer in 1928 with incense ad orientem all that sort of stuff you know **you follow the tradition that your denomination is a part of**."* ⚠️⚠️ **This is a rule about NOT IMPOSING his tradition's forms on OTHER denominations. It is NOT a concession that incense needs no warrant WITHIN Anglicanism, and it must not be deployed as one.** ⭐ It does bear on `OQ21`: the reception unit he names here is **the denomination**, not the whole church.
- ⭐ **Recording 6 `@111,403` carries a retrospection qualifier of exactly the shape `260835-1` found:** after describing the catechumen dismissal he says *"I'm again I'm not saying that that's the standard we should have today."*
- ⭐ **Even-handedness datum, recording 6 `@109,403`:** the entertainment/idolatry charge is levelled at **his own party** — *"this is a problem I would say with you know even with the high church tradition … we're carrying more about the vestments."*
- ⭐ **The Passover example, recording 3 `@58,806` — 2020.** `IP-90`'s note tracks it across roughly six weeks in 2026. **It is present six years earlier.** ⏳ A continuity check across the whole corpus is OWED and not done.
- ⚠️ **Corpus-lexical correction: `ritual act` occurs in recording 3 `@46,806`** (*"in taking this ritual act you are remembering"*). `260835-1` recorded `ritual act` as **0** in the corpus. ⛔⛔ **BUT HERE IT DESCRIBES THE MEMORIALIST POSITION HE IS CRITIQUING, NOT HIS OWN — it is NOT a third instance of the divine-pedagogy warrant.** Reported so the zero is not re-asserted and so the hit is not miscounted as support.
- ⭐ **Confirmation as a sacrament, recording 5 `@100,500`-`@102,000`:** *"we have this thing called confirmation … it's one of the sacraments"*, *"confirmation is important I would say it's essential."* Held as **`GV-24`**.
- ⚠️ **Provenance calibration, and it is not in the corpus:** recordings 3, 4 and 5 are **PRE-ORDINATION**. Recording 4 `@66,653`: *"I'm hoping to have **ordination** to come by soon hopefully sometime in July."* Recording 3 `@43,306`: *"I'm not wearing the collar."* ⛔ **`GV-1`/`GV-22` are labelled *"deacon-era"* at L792; recording 1 is 2023-11-24, when he was a priest, and recording 4 is pre-ordination. The label is wrong in both directions and is reported, not corrected.**

### 4.4 ⛔ HONEST ZEROES — reported with the terms searched

| Question | Result |
|---|---|
| **Element / circumstance distinction** | ⛔⛔ **ZERO across all nine recordings.** Searched `element`, `circumstance`, `indifferent`, `adiaphora`, `warrant`, `regulative`. Recording 6's *"contemporary **elements**"* (`@106,903`) is the ordinary sense — it denotes **instruments**, which the technical distinction classes as *circumstances*. ⚠️ **A lexical collision, not an adoption of the term.** Recording 7's several `element` hits are all ordinary-sense. ⛔ **Recording 8's *"normative means vs. God working outside the sacraments"* is a DIFFERENT AXIS and must not be conflated with it.** |
| **Priest's absolution as a ground of assurance (`BLOG-63`)** | ⛔⛔ **ZERO in recording 1** — `absolution` and `confession` return **0** in bytes 52-37,044, and `Eucharist` returns **0**. ⭐⭐ **In a 42-minute conversation whose entire subject is where assurance lies, he names BAPTISM ONLY.** ⚠️⚠️ **This EXTENDS `DQ-21`'s "narrowed in locus" observation back to 2023 — but it is an ABSENCE and is recorded as nothing more. It is not a retraction, not a change of mind, and the corpus holds no statement withdrawing the element.** ⚠️ Recording 8 `@159,916` does list absolution among the normative means — so the absence is specific to the assurance discussion, not general. |
| **Church-wide vs jurisdictional reception (`OQ21`)** | ⚠️ **Thin but non-zero.** Two data points, pulling opposite ways: recording 8 `@163,999` (1662 as trans-jurisdictional norm) and recording 6 `@113,403` (*"the tradition that your denomination is a part of"*). ⛔ **Neither is framed as province-vs-whole-church, and neither should be presented as answering `OQ21`.** |
| **`Matt Kennedy` in the findings corpus** | ✅ **Confirmed zero**, as briefed — ⛔⛔ **and the brief's inference from it (*"nothing here is already held"*) is FALSE. The name's absence is exactly what a batch that cites no titles and no guests would produce.** |
| **Recording 7 theology** | ⚠️ **Largely a nil return for this project.** A conference talk on Christian literature. **Narrative** as divine pedagogy is argued at length (`@121,081`), but ⛔ **no claim that RITUAL teaches** — the divine-pedagogy warrant (`260835-1`) is NOT corroborated here, and substituting narrative-pedagogy for ritual-pedagogy would be a category error. |

### 4.5 ⛔⛔ PRIVACY GUARD — APPLIED, AND ITS APPLICATION RECORDED

**Recording 7** was read under the standing guard by a delegate instructed that **personal history is not a finding** and that the strongest way to apply the guard is not to go looking. **Byte ranges passed over without description:** `115,081`-`116,581`, part of `116,581`-`117,081`, part of `119,081`-`120,081`, `130,581`-`132,081`, parts of `135,581`-`137,081`, `152,581`-`153,581`. ⛔ **No childhood or family material is recorded, characterised, summarised or alluded to anywhere in this artifact.** Two theological propositions from the `135,581`-`137,081` stretch were extracted **with their settings stripped**.

⛔ **The same guard was applied beyond recording 7, where the brief did not require it but the material did:** **recording 1 T31** contains extended accounts of two named-adjacent private individuals' moral and personal collapse, and **T49/T75** his own upbringing and baptisms. ⛔⛔ **None of it is carried.** ⭐ **One fact is recorded at the weakest useful layer because he makes it load-bearing himself — he grounds his position partly in his own formation (*"maybe this is back to my background growing up"*, T3) — and that is recorded as a fact ABOUT HIS REASONING with no biographical content attached.** ⛔ **Recording 9 `@176,790` names a family member's religious affiliation; flagged by the delegate, not carried.** ⛔ **Recording 4's apologist is deliberately unnamed BY HIM (`@71,153`, *"I'm not giving the name"*) and is not named here.**

---

## 5. ⚠️⚠️ THE `[Stated]` / `[Stated-Analysis]` / `[Analysis]` LAYERS ON THIS PASS'S OWN CLAIMS

| Claim | Layer |
|---|---|
| L6971 says `a201.txt` is a `GV` source file | **[Stated]** — read verbatim at `HEAD` |
| Speaker A = Kennedy, B = Rev. James | **[Stated]** — from the tape's own content, confirmed by diarization; ⛔ **not ear-verified** |
| `GV-2`/`3`/`4b`/`6b` carry Kennedy's words | **[Stated]** — byte range + timestamp + speaker label, each verified individually |
| The `V`*n* → line `2n+1` decoder | **[Stated-Analysis]** — inference from five labels, confirmed at three anchors |
| `File 46`/`a202.txt` is likewise already mined | **[Stated-Analysis]** — ⛔ **the file was NOT opened**; inferred from L6971's own sentence and two `a202`-labelled `GV` findings |
| Removing `GV-3` removes an apparent inconsistency in his eucharistic position | **[Analysis]** — this pass's argument, ⛔ **not attributed to him** |
| Recording 5's burden rule has `DQ-24`(b)'s shape | **[Analysis]** — ⛔ **he has never connected them; the bridge is this project's** |
| The `GV` batch's "2024-era" dating is wrong | **[Stated-Analysis]** — the upload dates are `[Stated]`; that `GV-10` comes from recording 2 is inference |

---

## 6. ✅ VALIDATOR AFTER

*(See §8 for the run. Recorded there so the before/after diff sits beside the `git status`.)*

---

## 7. ⛔⛔ WHAT THIS PASS DID NOT DO

- ⛔⛔⛔ **NO NUMBER CONSUMED, OF ANY PREFIX.** Next-free re-derived and unchanged: **`DQ-25`, `IP-109`, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EXT-4`, `W47`, `File 47`.**
- ⛔⛔⛔ **`St_Francis_EMC_Distinctives.md` NOT TOUCHED.** All four misattributions, the dating defect, the *"deacon-era"* label and the `GV` provenance gap **stand exactly as written**. ⭐ **The corrections are JD's: they require deciding whether to amend `GV-2`/`3`/`4`/`6` in place, to supersede them, or to re-source them — a numbering and never-alter question that belongs to him.**
- ⛔ **No `GV` finding renumbered, re-pointed, merged, retired or corrected.**
- ⛔ **No `SRC_Manifest.md` row overwritten** — the false `UNMINED` markers stand with a dated note beside them.
- ⛔ **No `SRC_Channel_Inventory.md` decision cell edited** — reasons at §3 of that file's stamp note; in short, filling them requires adopting the decoder as fact.
- ⛔ **`SRC_Coverage_Register.md` NOT created** (still does not exist; still owed from `260834-7`).
- ⛔ **`ORCHESTRATION.md` NOT touched** — the §8 probe-method amendment is owed.
- ⛔ **`validate_project.py` NOT modified.** The two registered defects (`C11` blindness to un-numbered findings, `C8`'s hyphen fragility) are untouched. ⚠️ **`C11` is blind to this pass by construction — an attribution audit that mints nothing is invisible to it.**
- ⛔ **`Incense_Conversational_Outline.md` NOT touched. `RJ_Incense_Analysis.md` §4.6/§4.8/§4.10 NOT touched.**
- ⛔ **`DQ-9` unmoved · `DQ-24` unamended · `OQ8`, `OQ19`, `OQ20`, `OQ21` untouched · no Discord state touched · no `VP-` pair, no `DELTA`, no gate, no register entry.**
- ⛔ **No source ingested, re-hashed or re-registered. No byte offset in any existing entry altered.**
- ⛔ **`a202.txt` / `File 46` NOT OPENED.**
- ⛔⛔ **Nothing drafted, altered or posted to Rev. James.**

---

## 8. ⛔⛔⛔ THE THREE RULINGS THIS PASS RESERVES TO JD

1. **The `GV` re-attribution.** Four findings carry an interlocutor's words. Amend in place, supersede, or re-source? ⚠️ **`GV-4` is the urgent one — its analytical point does not survive the correction.**
2. **Whether `a201`/`a202` should be re-mined at all under a corrected scheme.** ⭐ **The case FOR: the `GV` batch has no byte ranges, no dates, no diarization, and 50 of 55 findings have no locator. The case AGAINST: ~30 findings already exist and duplicating them is the specific harm the manifest was built to prevent.** ⭐ **A third option, which this pass recommends without adopting: retro-register byte ranges onto the EXISTING `GV` findings using the decoder, minting nothing — the `260834-9` shape, applied to findings instead of sources.**
3. **Whether Pass B3 (`File 46`) proceeds.** ⛔⛔ **On this evidence it should NOT proceed on its current brief.**

---

## 9. `git status --short`, IN FULL

*(See the session output — reproduced there verbatim and unabridged.)*

**Suggested staging: all six, one commit.**

```
git add PROJECT_STATE.md \
        SRC_Manifest.md \
        SRC_Channel_Inventory.md \
        passes/260835-4_file-45-first-mining_pass-b2.diff \
        passes/260835-4_file-45-first-mining_pass-b2_close-out.md \
        passes/260835-4_file-45-first-mining_pass-b2_raw-session-output.md
```

Suggested message: `260835-4: File 45 is NOT unmined — it is the GV batch's source (L6971); recording 1 diarized, four GV misattributions found and reported; nothing minted`

⚠️ **If `git add` fails on `.git/index.lock`, that is the briefed filesystem condition. DO NOT force-remove the lock.**

⛔ **NOTHING WAS COMMITTED. `git rev-parse HEAD` after all writes still returns `9882dc3d23fc5a97fed55a26b91afd3886ec2ccc`.**
