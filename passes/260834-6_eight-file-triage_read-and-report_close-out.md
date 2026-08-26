# 260834-6 — TRIAGE OF THE EIGHT UNREGISTERED SOURCE FILES

**Last updated: 260834-6.** Read-and-report pass. ⛔ **NO SOURCE REGISTERED · NO FINDING MINTED · NO `File`, `LS`, `IP`, `RV`, `BLOG` OR `POD` NUMBER CONSUMED.**

> ⛔⛔ **THERE IS NO DIFF OF CORPUS CONTENT FOR THIS PASS.** This pass produced exactly one new file — this one. No registered source, ledger, register, manifest row, hash, byte offset, question list, outline or analysis document was created, edited or deleted. There is no companion `.diff` because there is nothing to diff. The artifact *is* the report. *(§5 rule 11 — this note makes no claim about its own commit state.)*

---

## ✅ GATE

| Check | Expected | Observed | Result |
|---|---|---|---|
| `git rev-parse HEAD` | `6b01d39` | `6b01d3992cb2cae8cc1b72813ff918c311199a65` | ✅ **MATCH** |
| `git status --short` before first write | clean | *(empty)* | ✅ **CLEAN** |
| `.git/index.lock` | ⚠️ briefed as present, zero-byte, unremovable | ⚠️⚠️ **ABSENT at gate, PRESENT at close-out** — see below | ⚠️ **CONFIRMED REAL AND REPRODUCIBLE. NOT WORKED AROUND.** |
| `validate_project.py` BEFORE | `80 ok · 9 warnings · 0 errors` | `80 ok · 9 warnings · 0 errors` | ✅ **MATCH** |
| `PROJECT_STATE.md` stamp | `260834-5` | `260834-5` (created `260724-3`) | ✅ **MATCH** |
| Next-free pass stamp | derive | **`260834-6`** | ✅ **DERIVED AND VERIFIED FREE** |

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

### ⚠️⚠️ THE `.git/index.lock` — REPORTED, NOT WORKED AROUND

The briefed lock behaved differently at the two ends of this pass, and both observations are recorded rather than reconciled:

- **At gate**, immediately after the opening `git status --short` (which returned clean), `ls -la .git/index.lock` returned `ls: cannot access '.git/index.lock': No such file or directory`. **No lock was present.**
- **At close-out**, the closing `git status --short` produced its output normally **and then emitted** `warning: unable to unlink '/…/theology/.git/index.lock': Operation not permitted`, leaving a **zero-byte `.git/index.lock`** on disk. A direct `rm -f` returns `rm: cannot remove '.git/index.lock': Operation not permitted`.

⭐ **Diagnosis, offered as observation not conclusion: git is CREATING the lock normally and failing to REMOVE it, because the filesystem denies unlink on this path.** That is a permissions condition on the mount, not a stale lock left by a crashed process — which is why it reappears rather than persisting. Read-only plumbing is unaffected: `git rev-parse HEAD` continued to return `6b01d3992cb2cae8cc1b72813ff918c311199a65` throughout.

⛔⛔ **NO WORKAROUND WAS APPLIED.** The lock was not force-removed, its permissions were not changed, `.git` was not touched by any other means, and no git operation was retried against it. ⚠️ **The consequence for whoever stages this pass: an index-writing operation (`git add`, `git commit`) may fail on the lock, and the fix belongs to whoever owns the filesystem permissions on `.git/`, not to a pass.**

**Stamp derivation.** `grep -rhoE '\b26[0-9]{4}-[0-9]+\b'` across the whole repo *and* across `~/EMC/` returns a highest stamp of **`260834-5`**. `260834-6` returns **zero hits anywhere in `~/EMC/`**. (`260835` returns three hits — all three are prose *inside* `260834-5`'s own artifacts and `PROJECT_STATE.md` asserting that `260835` is free; none is a stamp in use.) **`260834-6` is genuinely free.**

---

## ⛔⛔⛔ THE PASS'S LOAD-BEARING RESULT — THE BRIEF'S PREMISE IS HALF WRONG, AND IT IS THE HALF THAT DETERMINES WHAT THE NEXT PASS IS

The brief scopes these eight files as *"established as unregistered **and unread**."*

**Unregistered: CONFIRMED.** None of the eight appears in any `SRC_Manifest.md` table. The manifest names `a101-1.txt`, `a101-2.md`, `a103.md`, `a105.md`, `a201.txt` and `a202.txt` **only as duplicate-check candidate targets** (lines 2721, 2723, 2792-2794, 2893-2894) and carries **no registration statement for any of them either way**. `a106.md` and `a301-Classical-Theism.md` are not named at all.

**Unread: ⛔ FALSE. All eight files' contents have already been mined into `St_Francis_EMC_Distinctives.md` under pre-manifest tag prefixes.** The Source ID Legend (line 369) defines them explicitly:

| Legend row (verbatim) | Maps to | Live citations |
|---|---|---|
| `**A101-I…VIII**` \| Anglican 101 series \| RJ's teaching video series (8 parts) \| RJ \| 2024 \| by session (I-VIII) | **`a101-1.txt`, all 8 segments** | 24 |
| `**AW-I…VI**` \| Anglican Worship series \| RJ's teaching video series (6 parts) \| RJ \| 2024 \| by session (I-VI) | **`a101-2.md` segments 2-8** | `AW-I` 42; `AW-IV` 5; `AW-V`/`AW-VI` 25 |
| `**Recon-Euch**` \| "Reconstructed / Deconstructed Eucharist" \| single walkthrough video \| RJ \| — \| by timestamp | **`a101-2.md` segment 10** | 22 |
| `**Ember**` \| Ember-days video \| single topical video \| RJ \| — \| by timestamp | **`a101-2.md` segment 9** | 13 |
| `**Lent vid**` \| Lent video \| single topical video \| RJ \| **Feb 2026** \| by timestamp | **`a101-2.md` segment 11** | 5 |
| `**Misc-2025**` \| Miscellaneous topical sessions \| assorted videos/Q&A \| RJ **(+ Bronson guest)** \| 2025 \| Misc-1..7 | **`a106.md`, all 3 recordings** | 16 |
| `**ANF**` \| Ante-Nicene & Nicene Fathers class \| teaching class, **8 sessions** \| RJ **+ 3 named guests (Boyce, West, Valdez)** \| 2025 \| ANF-1..9 | **`a103.md`, all 9 recordings** | 32 |
| `**COT**` \| Christ in the Old Testament class \| teaching class, **7 sessions** \| RJ (all) \| 2025 \| COT-1..7 | **`a105.md`, all 7 recordings** | 37 |

Corroborated at the finding level, not merely the legend level: `IP-50` cross-refs `ANF-1`; `IP-60` cross-refs `AW-I`; `IP-61` and `IP-63` cross-ref `AW-VI`; `IP-72`, `IP-74` and `IP-79` each cross-ref `AW-V`. The Bronson guest named in the `Misc-2025` row is found at `a106.md` @48,439 (*"I'm Gregory Bronson… professor of English"*). The three ANF guests named in the `ANF` row are found at `a103.md` @91,064 (Dr. Steven Boyce), @124,286 (Kevin Valdez) and @177,046 (Tyler West).

⭐⭐⭐ **CONSEQUENCE — AND IT CHANGES THE NEXT PASS'S KIND, NOT ITS SIZE.** Seven of the eight files are **not an intake problem; they are a retro-registration problem** — the exact `Rev`/Files 8-9 situation that `260813-1` resolved: material already mined under a pre-manifest batch prefix, carrying live findings and live cross-references, but with **no File number, no hash, no byte offsets, and no session rows**. A pass that treats them as fresh sources will **re-mine material already in the ledger and mint duplicate findings under new prefixes.**

⚠️ **Two legend/file discrepancies found and reported, NOT corrected** (correcting the legend is not this pass's brief):

- **`ANF` says "8 sessions" but `a103.md` contains 9 recordings** — and the same row's own range field says `ANF-1..9`. The session count is wrong; the range is right.
- **`Misc-2025` says "2025" but one of `a106.md`'s three recordings is 2026.** See the dating trap below. ⛔ This is the `260822-2` `Rev`-mislabel shape arriving by a second door.

⛔ **NOT CLAIMED:** that the mining is *complete*, that every segment was mined to the same depth, or that any specific finding does or does not already exist for any specific byte range. Establishing per-segment mining coverage is a separate pass and was not run.

---

# TASK 1 — STRUCTURE

**Method.** Every `==`-initial line and every ATX heading was located by byte offset with `re.finditer(rb'(?m)^(==.*|#{1,6} .*)$')`; segment boundaries were then read from the offsets, and each segment's opening ~900 bytes read for self-identification. ⛔ **No delimiter convention was assumed.** Four *different* conventions were found across the eight files, and two of them do not carry titles at all.

**Total: 51 distinct recordings across the eight files** (52 delimiter-marked segments, of which one — `a301` — is wholly contained in another; see Task 2).

---

## ⭐ 1.1 `a101-2.md` — 263,995 bytes — **HIGHEST PRIORITY, REPORTED FIRST AND IN MOST DETAIL**

**Banner line, verbatim:**

```
==1 year ago - Anglican Worship series==
```

⚠️ **The banner is a RELATIVE date and dates nothing.** *"1 year ago"* is anchored to an unrecorded capture moment. Per the manifest's standing rule (*header dates are labels, not sources*), **it is not adopted.** Independent corroboration is available in `SRC_Channel_Inventory.md` (`EXT-3` rows, Anglican Worship 2024-09-17 → 2024-11-26) and is cited below as corroboration, **not adopted as the recording dates either** — the channel rows are *upload* dates.

**Delimiter convention actually used:** a single `==` at line start, immediately followed by transcript text on the same line. ⛔ **ONLY THE FIRST RECORDING CARRIES A TITLE.** Recordings 2-10 open `==` directly into the collect. Titles below are therefore **derived from each recording's own self-identifying sentence**, quoted verbatim, not read off a header.

**Number of distinct recordings: 10** (banner + 10 segments = 11 delimiter-marked blocks).

| # | Title | Basis | Stated date | Byte range | Size |
|---|---|---|---|---|---|
| — | *(banner)* | — | ⚠️ *"1 year ago"* — relative, not adopted | `0`–`40` | 41 B |
| 1 | **Anglican Worship, Session I: Our Approach to Worship** | ⭐ **explicit header** | none stated; *"the first of our six weeks"* | `41`–`29,822` | 29,782 B |
| 2 | **Anglican Worship, Session II — Overview of the Book of Common Prayer** | derived: *"our second week is uh going giving an overview of the book of common prayer"* | none stated | `29,823`–`62,397` | 32,575 B |
| 3 | **Anglican Worship, Session III — Matins and Evensong** | derived: *"we are doing class three of Anglican worship we're going over matens and even song"* | ⭐ none stated, but **internally datable**: prays *"the prayer for in time of Calamity on page 41… concerning [Hurri]cane Helen[e]"* for *"the upstate South Carolina area and North Carolina"* — Helene struck late Sept 2024 | `62,398`–`91,983` | 29,586 B |
| **4** | ⭐⭐⭐ **Anglican Worship, Session IV — Holy Communion Part One: the Liturgy of the Word** | derived, and he states both the number and the subtitle: *"we are on **part four** today for the Anglican worship class uh I actually decided uh to do this into two parts so you'll see the subtitle is **holy communion part one Liturgy of the word** and next week we will be going over the second half of Holy Communion which is the **Liturgy of the sacrament**"* | none stated | **`91,984`–`116,830`** | **24,847 B** |
| **5** | ⭐⭐⭐ **Anglican Worship, Session V — Holy Communion Part Two: the Liturgy of the Sacrament** | derived: *"we are in class five… we are on uh class 5 this is **holy communion part two** uh we separated t[hem]"* | none stated | **`116,831`–`139,747`** | **22,917 B** |
| 6 | **Anglican Worship, Session VI Part 1 — the Liturgical Year and Calendar** | derived, **including his own on-air correction of the handout**: *"this is actually **class six** it says class 5 but I forgot to update it to class six so just keep that in mind"* | none stated; opens with the **collect for the First Sunday in Advent**, *"we'll be starting the new [li]turgical year in a few weeks"* → recorded some weeks before Advent I 2024 (2024-12-01) | `139,748`–`151,802` | 12,055 B |
| 7 | **Anglican Worship, Session VI Part 2 — the Calendar continued (Easter computus and the feast cycle)** | ⛔ **derived only from continuity — opens mid-sentence**, *"==of the all the holy days and feast days and such begin depend is always the first Sunday after the full moon…"* | none stated | `151,803`–`160,769` | 8,967 B |
| 8 | **Ember Days** *(standalone topical video, not part of the six-week series)* | ⭐ **self-identified in the first clause**: *"Father James here the rec[t]or of St Francis Anglican Church in Spartenburg South Carolina I uh this video will be over **Ember days** what they are how we observe them and a bit of their history"* | none stated | `160,770`–`166,782` | 6,013 B |
| **9** | ⭐⭐⭐ **Instructed Eucharist (1928 US BCP walkthrough)** — the corpus's `Recon-Euch` | derived: *"Welcome to the first of many **constructed Eucharists**… there are two handouts. The first one says, 'How we worship instruction on holy communion according to the **1928 US book of common prayer**.'"* ⚠️ *"constructed"* is an **ASR mangling of "instructed"** — see the quirk note in Task 3 | none stated | **`166,783`–`248,029`** | **81,247 B** ⭐ *the largest single recording in all eight files* |
| 10 | **Lent and Ash Wednesday** *(standalone topical video)* | ⭐ **self-identified**: *"Father James here, the director of St. Francis Anglican Church in Spartanberg, South Carolina. And our video today will be about **Lent and Ash Wednesday**"* | ⭐⭐ **STATED IN HIS OWN VOICE, THE ONLY EXPLICIT RECORDING DATE IN THE ENTIRE FILE**: *"today, the recording of this video is uh **February 18th, 2026**, which is the first day of Lent, also known as Ash Wednesday, which is why I have the ashes upon my head"* | `248,030`–`263,994` | 15,965 B |

### ⭐⭐⭐ DIRECT ANSWER TO THE FLAGGING PASS'S QUESTION

**Anglican Worship IV and V — the two sessions a separate flagging pass identified as top-tier relevant — ARE BOTH PRESENT IN THIS FILE, IN FULL, AND ARE EXACTLY WHAT THAT PASS DESCRIBED.**

- **Anglican Worship IV — Holy Communion, Liturgy of the Word: bytes `91,984`–`116,830` (24,847 B).**
- **Anglican Worship V — Holy Communion, Liturgy of the Sacrament: bytes `116,831`–`139,747` (22,917 B).**

He names the two-part split himself, in Session IV, before delivering either half. The pairing is his, not an editor's.

### ⚠️ BOUNDARY UNCERTAINTY — ONE, AND IT IS REPORTED RATHER THAN DECIDED

**The recording-6 / recording-7 boundary at byte `151,803` is the only boundary in this file I will not call.** Recording 7 opens **mid-sentence** (*"of the all the holy days and feast days and such begin depend is always…"*) and continues recording 6's calendar material without a collect, a greeting or any restart marker. Two readings are live and **neither is chosen**:

- **(i) One recording, split by a capture artifact.** The mid-sentence opening is what a dropped/rejoined capture looks like; the delimiter would then be JD's mark for a file break, not a recording break.
- **(ii) Two recordings, being Session VI Part 1 and Part 2.** ⭐ **This reading has independent external corroboration**, which reading (i) does not: `SRC_Channel_Inventory.md` carries **two** `EXT-3` rows for Session VI and no other session — `9UDQhvMdkNA` *"VI Pt 1"* (916 s) and `38BYTZzLmxg` *"VI Pt 2"* (663 s), **both 2024-11-23**. The byte ratio 12,055 : 8,967 = **1.34** against the duration ratio 916 : 663 = **1.38**.

⛔ **The corroboration is strong and I still do not adopt it**, because it is a *channel upload* fact being used to settle an *internal* boundary, and because a mid-sentence open is equally consistent with Part 2 having been recorded as a continuation with the collect omitted. **Reading (ii) is the better-supported reading and the byte ranges above are written on it; the next pass should confirm against the audio or the two videos before any session row is written.** Either way the *content* boundary is at `151,803` and no material is lost or double-counted.

⛔ **Not claimed:** that recordings 1-7 are the six-week series *complete*. Six sessions across seven recordings is consistent, but "six weeks" is his stated plan, not a verified count.

---

## ⭐ 1.2 `a105.md` — 188,770 bytes — **Christ in the Old Testament**

**Banner line, verbatim** — ⛔ note it is **NOT** `==`-delimited; it is a bare first line:

```
St Francis Christ in the OT Class 2025
```

**Delimiter convention actually used:** bare-text banner line, then `==` at line start opening directly into transcript. ⛔ **NO recording carries a title.** All seven titles below are derived from his own self-identifying sentence.

**Number of distinct recordings: 7.**

⛔⛔ **THE FILE IS NOT IN CLASS ORDER, AND THE CLASS NUMBERS ARE NOT CONTIGUOUS.** File order is classes **2, 3, 6, 5, 4, 7, 9**. Classes **1 and 8 are absent**, and nothing past 9 is present. Reading position-in-file as session number is the whole error available here.

| # | Class no. (his own words) | Title / subject | Stated date | Byte range | Size |
|---|---|---|---|---|---|
| — | — | *(banner)* | ⚠️ *"2025"* — a label, not adopted | `0`–`39` | 40 B |
| 1 | **class 2** — *"class two session two in Christ in the Old Testament"* | Creation and the Garden of Eden | none; collect is *"the second Sunday after Epiphany"* | `40`–`20,504` | 20,465 B |
| 2 | **class 3** — *"this morning we are on class three of Christ in the Old Testament"* | The Fall and the Flood *(Abraham deferred on air)* | none | `20,505`–`52,549` | 32,045 B |
| **3** | ⭐⭐⭐ **class 6** — *"today we have the sixth class… last time we met we were doing uh Moses and now we're moving on into specifically the **Tabernacle and the presence of God**"* | **The Tabernacle and the Presence of God** | none | **`52,550`–`76,107`** | **23,558 B** |
| 4 | **class 5** — *"this morning we have class five for Christ in the Old Testament this one is titled **Jesus the greater Moses**"* | Jesus the Greater Moses | none | `76,108`–`105,802` | 29,695 B |
| 5 | **class 4** — *"this is class four now we are speaking about… the promise to Abraham"* | The Promise to Abraham and his Seed *(with a Tower of Babel excursus)* | none | `105,803`–`139,614` | 33,812 B |
| **6** | ⭐⭐⭐ **session 7** — *"we are on **session 7** now of Christ in the Old Testament we are going to be looking at the **levitical sacrifices** uh and **how they point to Christ**"* | **Jesus and the Levitical Sacrifices** | none | **`139,615`–`165,438`** | **25,824 B** |
| 7 | **class 9** — *"so class number nine **Jesus as the son of David**"* | Jesus as the Son of David | none; collect is *"the 15th Sunday after Trinity"* | `165,439`–`188,769` | 23,331 B |

### ⭐⭐⭐ DIRECT ANSWER — AND A CORRECTION TO THE BRIEF'S EXPECTATION

**YES — the session on Jesus and the Levitical sacrifices is present: `a105.md` bytes `139,615`–`165,438`.** He announces it in exactly those terms, and states the type/antitype purpose in the same breath (*"how they point to Christ"*).

⚠️⚠️ **BUT IT IS NOT THE SEGMENT THAT BEARS ON SHOWBREAD, AND THE BRIEF'S FRAMING WOULD SEND THE NEXT PASS TO THE WRONG BYTE RANGE.** The term battery (Task 3) is decisive:

| | class 6 — Tabernacle (`52,550`–`76,107`) | class 7 — Levitical Sacrifices (`139,615`–`165,438`) |
|---|---|---|
| `showbread` / `shewbread` / *bread of the presence* | ⭐⭐⭐ **4** | ⛔ **0** |
| `tabernacle` | ⭐⭐⭐ **27** | 0 |
| `incense` / `censer` | ⭐ **7** | 3 |
| `altar` | 5 | 5 |
| `Levitic-` | 2 | ⭐ **15** |
| `sacrific-` | 21 | 23 |

⭐ **The showbread material is in the TABERNACLE class (class 6), not the Levitical-sacrifices class (class 7).** All four `showbread` occurrences in all eight files sit inside `52,550`–`76,107`. **Both segments are needed** — class 6 for the showbread furniture and its incense, class 7 for the sacrificial type/antitype reasoning — but they are **two different recordings 63 KB apart**, and the brief names only one of them.

---

## 1.3 `a101-1.txt` — 256,209 bytes — **Anglican 101 (2024)**

**Banner line, verbatim:**

```
==Following video series from 2024, Anglican 101==
```

**Delimiter convention:** `==Title==` — ⭐ **the only file of the eight where every recording carries a closed, explicit `==…==` title**, followed on the same line by transcript.

**Number of distinct recordings: 8.** ⛔ **No recording states a date.** The banner's *"2024"* is a label and is not adopted; `SRC_Channel_Inventory.md` carries eight matching `EXT-3` rows, 2024-05-19 → 2024-07-13, as corroboration only.

| # | Title (verbatim from header) | Byte range | Size |
|---|---|---|---|
| — | *(banner)* | `0`–`51` | 52 B |
| 1 | `Anglican 101, Session I: Anglican Identity` | `52`–`27,452` | 27,401 B |
| 2 | `Anglican 101, Session II: The Doctrine of God (Classical Theism)` | `27,453`–`66,157` | 38,705 B |
| 3 | `Anglican 101, Session III: Anglican History` | `66,158`–`106,844` | 40,687 B |
| 4 | `Anglican 101, Session IV: Christology` | `106,845`–`131,323` | 24,479 B |
| 5 | `Anglican 101, Session V: Ecclesiology (Theology of the Church)` | `131,324`–`164,682` | 33,359 B |
| **6** | ⭐ `Anglican 101 Session VI: Scripture (and Tradition)` | **`164,683`–`190,060`** | 25,378 B |
| 7 | `Anglican 101 Session VII: Salvation and the Dominical Sacraments` | `190,061`–`225,634` | 35,574 B |
| 8 | `Anglican 101, Session VIII: The Ecclesial Sacraments` | `225,635`–`256,208` | 30,574 B |

⚠️ **Header inconsistency, reported not corrected:** sessions VI and VII omit the comma after *"Anglican 101"* that sessions I-V and VIII carry. A literal `Anglican 101,` grep misses two of eight.

---

## 1.4 `a103.md` — 259,190 bytes — **Ante-Nicene and Nicene Church Fathers (2025)**

**Banner line, verbatim** — again a **bare first line, not `==`-delimited**:

```
St Francis Ante-Nicene and Nicene Church Fathers Class 2025
```

**Delimiter convention:** bare banner, then untitled `==` opening directly into transcript. ⛔ **No recording carries a title and none states a date.**

**Number of distinct recordings: 9.** ⚠️ **The Source ID Legend says this class has 8 sessions. It has 9.**

| # | Class no. / subject (derived from his own words) | Teacher | Byte range | Size |
|---|---|---|---|---|
| 1 | *"the first class of the Antonyine and Nyine fathers"* — introduction, why and how | RJ | `61`–`30,246` | 30,186 B |
| 2 | *"the second week… class two **from Pentecost to Rome**"* | RJ | `30,247`–`58,608` | 28,362 B |
| 3 | *(number not stated in the opening; content continues the century survey)* ⚠️ | RJ | `58,609`–`91,063` | 32,455 B |
| 4 | *"We have a special guest with us today, **Dr. Steven Boyce**… a doctorate uh in canonicity and textual criticism"* | ⚠️ **GUEST — Dr. Steven Boyce** | `91,064`–`124,285` | 33,222 B |
| 5 | *"we have uh **Kevin Valdez** teaching on **St. Athanasius** today for adult formation"* | ⚠️ **GUEST — Kevin Valdez** | `124,286`–`149,041` | 24,756 B |
| 6 | *"**class number six**… defending the faith part two… **St. Justin Martyr's first and second apologies**… **St. Irenaeus's against heresies**"* | RJ | `149,042`–`177,045` | 28,004 B |
| 7 | *"we have **Tyler West** who will be leading our class today"* | ⚠️ **GUEST — Tyler West** | `177,046`–`205,246` | 28,201 B |
| 8 | *"today we are going over **class 8**… the title for this one… is **not quite saints**"* | RJ | `205,247`–`232,130` | 26,884 B |
| 9 | *"this is the **final week** for our anti[-Nic]ene class… focus upon what happens in the 4th century… **AD 325**"* | RJ | `232,131`–`259,189` | 27,059 B |

⚠️ **Boundary/numbering uncertainty, reported not resolved:** recording 3 does not state its class number, and recordings 4, 5 and 7 are introduced by guest name rather than by number. His own numbering (1, 2, ?, ?, ?, 6, ?, 8, final) is **consistent with** a straight 1-9 but does not by itself establish that recording 3 is class 3, or that the guest weeks are classes 4, 5 and 7. `SRC_Channel_Inventory.md`'s nine `EXT-3` rows (I…IX, 2025-05-04 → 2025-07-13, with IV = Dr Stephen Boyce, V = Kevin Valdes, VII = Tyler West) **do** line up 1:1 in that order — corroboration, cited, **not adopted**.

---

## 1.5 `a106.md` — 80,482 bytes — **St Francis Misc**

**Banner line, verbatim** — bare first line:

```
St Francis Misc 2025
```

**Delimiter convention — ⭐ A FOURTH CONVENTION, AND THE ONLY TWO-LINE ONE.** Each recording is opened by **two** consecutive `==` lines: `==<Title>` on its own line, then `==<transcript>` beginning the body. Counting `==` lines here gives **6**; counting *recordings* gives **3**. A delimiter-counting script that does not read the lines gets this file wrong by a factor of two.

**Number of distinct recordings: 3.**

| # | Title (verbatim from its own `==` line) | Body byte range | Size | Date |
|---|---|---|---|---|
| 1 | `==Doctrine of the Trinity` (title @`22`–`47`) | `48`–`18,441` | 18,394 B | none stated; *"who can tell me what today is other than Sunday? Trinity Sunday"* |
| 2 | `==Classical Theism` (title @`18,442`–`18,460`) | `18,461`–`47,771` | 29,311 B | ⛔⛔ none stated — **see the dating trap below** |
| 3 | `==Sir Gawain and the Green Knight - a study on its christian themes` (title @`47,772`–`47,839`) | `47,840`–`80,481` | 32,642 B | none stated; guest-taught |

### ⛔⛔ THE BANNER IS FALSE FOR AT LEAST ONE RECORDING — THE `Rev`-MISLABEL SHAPE, ARRIVING BY A SECOND DOOR

`a106.md`'s banner says **`Misc 2025`**, and the Source ID Legend's `Misc-2025` row copies that year. **Recording 2 is a 2026 recording.** It is byte-for-byte the same transcript as `a301-Classical-Theism.md` (Task 2), and `a301`'s own header states **`### Jun 6, 2026`**; `SRC_Channel_Inventory.md` carries `gEDpnwg2tF0` *"Classical Theism (for Trinity Sunday)"* at **2026-06-07**.

⭐ This is precisely the failure `260822-2` corrected for `Rev` — *"mislabelled 2025 at the intake before any dating discipline existed"* — and `260822-2`'s own warning that **14 of this document's `(2025)` citations are genuinely 2025 and sit on the `RC`/`RC3`/`RC4`/`ANF`/`COT` series** does **not** cover `Misc-2025`. ⛔ **Reported, not corrected. No `Misc-n` citation was inspected, moved or re-dated by this pass.** Which of `Misc-1..7` attach to recording 2 is unestablished, and establishing it is the retro-registration pass's job.

⛔ Recordings 1 and 3 are separately corroborated as 2025 by `SRC_Channel_Inventory.md` (`5mU3CdbXjOQ` *Doctrine of the Trinity* 2025-06-18; `hlEGpBC3Vj4` *Sir Gawain* 2025-12-31) — so the banner is right for two of three and wrong for one. **A blanket re-date would be as wrong as the current label.**

---

## 1.6 `a201.txt` — 177,254 bytes — **compilation, "batch AA"**

**Banner line, verbatim** (note the internal spaces, which a `==Title==` grep will miss):

```
== additional general videos from RJ - batch AA ==
```

**Delimiter convention:** `==Title (YYYY)==` — closed, titled, with a **JD-supplied parenthetical year**. ⚠️ **THE PARENTHETICAL YEARS ARE JD'S LABELS, NOT STATED DATES, AND SIX OF THE THIRTEEN ACROSS `a201`+`a202` ARE WRONG** (see the dating table at the end of Task 1). **No recording in this file states its own date.**

**Number of distinct recordings: 9.**

| # | Title (verbatim) | Byte range | Size | Voices |
|---|---|---|---|---|
| — | *(banner)* | `0`–`51` | 52 B | — |
| **1** | `Talk with Fr Matt Kennedy: Where Does Our Assurance Lie? (2024)` | `52`–`37,044` | 36,993 B | ⚠️⚠️ **TWO — and it OPENS IN THE GUEST'S VOICE** |
| 2 | `A History of the Church in England--A Book Review (2021)` | `37,045`–`43,305` | 6,261 B | solo |
| 3 | `The Memorialist View of The Last Supper: Arguments and Critiques (2020)` | `43,306`–`66,152` | 22,847 B | solo |
| 4 | `A Bad Way to Understand John 6:63 (2021)` | `66,153`–`72,999` | 6,847 B | solo |
| 5 | `Response to "Should Christians Baptize Their Babies?" (2020)` | `73,000`–`106,902` | 33,903 B | solo |
| 6 | `Is Contemporary Worship Wrong? (2020)` | `106,903`–`114,580` | 7,678 B | solo |
| 7 | `The Stories We Tell (2022) (includes RJ's childhood info)` — ⚠️ the parenthetical *"(includes RJ's childhood info)"* is **JD's editorial annotation, not part of the video title** | `114,581`–`153,950` | 39,370 B | solo |
| 8 | `Simply Anglican--A Book Review (2021)` | `153,951`–`173,500` | 19,550 B | solo |
| 9 | `Canterbury Cousins--A Book Review (2021)` | `173,501`–`177,253` | 3,753 B | solo |

⭐ **The "compilation of interviews and debates" framing in the brief overstates `a201`.** Interlocutor-signal density (`yeah` / `right?` / `mhm`) is 52 in recording 1 and 0-10 in every other; recordings 2-9 are **solo videos**. `a201`'s multi-voice risk is **confined to recording 1**.

---

## 1.7 `a202.txt` — 211,170 bytes — **compilation, "batch BB"**

**Banner line, verbatim:**

```
== additional general videos from RJ - batch BB ==
```

**Delimiter convention:** identical to `a201` — `==Title (YYYY)==` with a JD-supplied year.

**Number of distinct recordings: 4.**

| # | Title (verbatim) | Byte range | Size | Voices |
|---|---|---|---|---|
| — | *(banner)* | `0`–`50` | 51 B | — |
| **1** | `A Debate on Holy Orders: "Absolutely Null and Utterly Void"...Is Apostolicae Curae Correct? (2021)` | `51`–`95,315` | 95,265 B | ⚠️⚠️⚠️ **THREE — moderator + two debaters** |
| **2** | `Debate on Holy Orders within Anglicanism: Rev. James and Noah, Moderated by Evan Minton (2020)` | `95,316`–`175,795` | 80,480 B | ⚠️⚠️⚠️ **THREE — moderator + two debaters** |
| 3 | `Is the Monarch of England the Pope of Anglicanism? (2021)` | `175,796`–`184,862` | 9,067 B | solo |
| 4 | `How to Use the 2019 Book of Common Prayer (2023)` | `184,863`–`211,169` | 26,307 B | solo |

**Speaker roster established from the text itself** (not inferred):

- **Recording 1** — moderator: *"my name is **noah edmonds of the eccentric naturalist** and i'm going to be moderating this debate"*. Affirmative: *"**james godomski** [Gadomski]… a priest within the anglican tradition as well as a schoolteacher… graduated from trinity school for ministry with a master of divinity and runs the **barely protestant** youtube channel"*. Negative: *"**john fisher** a **john fisher 2.0** is the loyal apologist of the universal pontiff of rome… has a master of arts in religious studies and runs the youtube channel john fisher 2.0"*. ⛔ **He is a PRIEST here.**
- **Recording 2** — moderator: *"I'm **Evan Minton** of **cerebral faith** ministries"*. Debaters: *"**James Gaddafi** [Gadomski] and… **Noah Edmunds** [Edmonds]"*; *"The Reverend James… is a **deacon** within the Anglican tradition, he is in his **final semester of seminary** at Trinity School for Ministry and is **expected to receive ordination to the priesthood this summer**"*; *"**noah** is an **evolutionary biology** major, he runs **the eccentric naturalist**"*. ⛔ **He is a DEACON here.**

⭐⭐ **The two recordings settle the Noah Edmonds question between them: he is RJ's OPPONENT in recording 2 and the MODERATOR of recording 1.** Both roles are stated on the tape, in his own self-introduction in recording 1 and in Minton's introduction in recording 2, and the same identifier — *"the eccentric naturalist"* — attaches to him in both.

---

## 1.8 `a301-Classical-Theism.md` — 29,338 bytes

**Banner: ⛔ there is no `==` banner. This file uses ATX markdown headings — a fourth-and-a-half convention, and the only one of the eight with a structured header block:**

```
# Classical Theism
## Classical Theism (for Trinity Sunday)
### Jun 6, 2026
```

**Delimiter convention:** none internally — the file is a single body after the three-line header, using `>>` diarization markers throughout.

**Number of distinct recordings: 1** — and ⛔ **it is not a new one.** See Task 2.

**Stated date: ⭐ `Jun 6, 2026`** — the header's third line. This is the **only** dated header in the eight files and, per the manifest's own rule, is a **label** — but it is a label that **corroborates** an independent channel row (`gEDpnwg2tF0`, 2026-06-07) and **contradicts** `a106.md`'s `Misc 2025` banner for the same recording.

---

## ⚠️ DATING TABLE — JD'S PARENTHETICAL YEARS IN `a201`/`a202` vs `SRC_Channel_Inventory.md`

| File · # | Banner year | Channel row | Verdict |
|---|---|---|---|
| a201 · 1 Matt Kennedy | **(2024)** | `xk2zB2LEcF8` **2023-11-24** | ⛔ **MISMATCH** |
| a201 · 2 Hist. Church in England | (2021) | `Ym8DgpMjB5A` 2021-02-19 | ✅ consistent |
| a201 · 3 Memorialist View | (2020) | `30mExhHCw4w` 2020-06-18 | ✅ consistent |
| a201 · 4 John 6:63 | **(2021)** | `Y-xfYRjzMC8` **2020-06-26** | ⛔ **MISMATCH** |
| a201 · 5 Baptize Their Babies | (2020) | `pYO6mt0DZko` 2020-05-30 | ✅ consistent |
| a201 · 6 Contemporary Worship | (2020) | `zt5kpHQ2nkw` 2020-04-09 | ✅ consistent |
| a201 · 7 The Stories We Tell | (2022) | `FSHHIm-xIBM` 2022-02-17 | ✅ consistent |
| a201 · 8 Simply Anglican | **(2021)** | `CmnwsSDrc3o` **2020-10-21** | ⛔ **MISMATCH** |
| a201 · 9 Canterbury Cousins | **(2021)** | `qm_ur2izYBY` **2020-10-17** | ⛔ **MISMATCH** |
| a202 · 1 Apostolicae Curae debate | **(2021)** | `MLCh-d15F_o` **2020-08-29** | ⛔ **MISMATCH** — ⭐⭐ and see below |
| a202 · 2 Minton-moderated debate | (2020) | `7_egBtP9H1I` 2020-03-02 | ✅ consistent |
| a202 · 3 Monarch / Pope | **(2021)** | `M1E8Tfj4vnU` **2020-12-20** | ⛔ **MISMATCH** |
| a202 · 4 How to Use the 2019 BCP | (2023) | `ulrD_RdI6Q0` 2023-01-29 | ✅ consistent |

⛔⛔ **SIX OF THIRTEEN JD-SUPPLIED YEARS DISAGREE WITH THE CHANNEL, AND EVERY DISAGREEMENT RUNS THE SAME DIRECTION — THE BANNER IS LATER THAN THE UPLOAD.** ⭐ **Recommendation: treat every `a201`/`a202` parenthetical year as an unverified label and adopt none of them.** Neither year is adopted by this pass; both are recorded so the retro-registration pass resolves each against the video rather than against the container.

⭐⭐ **`a202` recording 1's mismatch is the load-bearing one and it is independently falsified from inside the tape**: in recording 1 the moderator introduces RJ as *"**a priest** within the anglican tradition"*, while recording 2 (2020-03-02) has him as a **deacon** *"expected to receive ordination to the priesthood this summer"*. A 2020-08-29 date for recording 1 places it **after** that summer priesting and is fully consistent; the banner's *"2021"* is consistent too, so **the tape narrows the window to "after mid-2020" without settling the year.** ⛔ The mismatch is real; the correction is not made here.

---

# TASK 2 — DUPLICATE CHECK, AT RECORDING LEVEL

**Method, and why it is three tests and not one.** `SRC_Manifest.md` records that two duplicate classes need opposite tests: *"`a304` was a re-supply of the same TRANSCRIPT and therefore ran 99.984% identical; `a303` is a re-supply of the same AUDIO under a DIFFERENT ASR ENGINE, and two engines over one recording share almost no long literal runs… a hash check passes both; a longest-run check catches the `a304` class and PASSES the `a303` class; only coverage-window and quirk-alignment comparison catches the `a303` class."* Accordingly every recording was checked on **(a)** title/date against the registry and the channel inventory, **(b)** longest-common-run where a candidate existed, and **(c)** duration/coverage-window where a same-audio re-supply was conceivable.

## ⛔⛔ RESULT 1 — ONE TRUE DUPLICATE, AND IT IS INSIDE THE SCOPE SET

**`a301-Classical-Theism.md` IS NOT AN INDEPENDENT SOURCE. IT IS `a106.md` BYTES `18,461`–`47,771`.**

| Test | Result |
|---|---|
| SHA-256, `a106` recording 2 body vs `a301` whole file | `14402def7e36c5f2…` vs `3551973355aa3518…` — ⛔ **DIFFERENT. A hash-keyed intake passes this file.** |
| Length | 29,329 B vs 29,338 B |
| Word count | 5,578 vs 5,575 |
| **Longest common run** | ⭐⭐⭐ **29,261 characters** — begins *">> The Lord be with you. >> Let's pray. Almighty God, we thank you so much for revealing to us uh the try new nature of you…"* |
| `difflib.quick_ratio` | **0.9992** |
| `>>` marker count | **33** vs **33** — identical |
| Head divergence | `a106` carries 45 B of extra lead-in (*"cast and can surface to fix you. That's good."*) that `a301` drops; `a301` carries the 3-line ATX header `a106` lacks |
| Tail | ⭐ **identical to the final character** — *"…So we don't get to say that Greek philosophy is just wrong because they had bad Greek religion. But yeah, um any other questions? All right. I thank you all very much."* |

⭐ **This is the `a304` class exactly — one transcript supplied twice, not one audio transcribed twice.** Identical `>>` counts and a 29,261-character literal run exclude the `a303` (two-engine) reading outright: two engines do not agree on 29,261 consecutive characters.

⛔⛔ **DISPOSITION RECOMMENDED — `a301-Classical-Theism.md` SHOULD NOT BE INGESTED, SHOULD RECEIVE NO `File` NUMBER, NO SESSION ROW AND NO FINDING TAG.** It is the same disposition `SRC_Manifest.md:287` gives `a304`. ⭐ **It is nevertheless not worthless: it is the DATING WITNESS for `a106` recording 2** (`### Jun 6, 2026`), which is the only reason the `Misc 2025` banner error above is visible at all. It should be recorded as a rejected re-supply *with that fact attached*, not merely deleted.

⛔ **NOT DONE HERE:** no rejection row was written to `SRC_Manifest.md`, no hash was registered, and no `a304`-style disposition note was added. That is a registration act and this pass registers nothing.

## ⭐⭐⭐ RESULT 2 — THE `a202` / FILE 33 QUESTION: **RESOLVED**

**The brief's flag:** *"`a202`'s first item is a 2021 Holy Orders debate whose moderator self-identifies as 'noah edmonds,' and File 33 (`ApostolicSuccession`, 2020-03-08) is his recap of his first formal debate against 'Noah.' Those may be the same event, different events, or one recapping the other."*

**Answer: it is NOT `a202` recording 1. It is `a202` recording 2 — and the relation is "one recaps the other," six days apart.** All three of the brief's options were live; the third is correct, and it attaches to the recording the brief did not name.

### The chain, each link independently evidenced

| Link | Evidence |
|---|---|
| File 33 is a **solo recap**, not a debate | `SRC_Manifest.md:2926`: *"**Rev. James, solo** (label `A`, 305 sentences) — ⛔⛔ **post-debate recap of his own first formal debate against a named opponent ("Noah"); Noah's arguments are characterized at length and are NEVER his.**"* Title: *Thoughts on the Apostolic Succession Debate*, `Vfq5b5btlVw`, **2020-03-08**, **33:30**. |
| File 33 self-dates to **deacon, final semester** | `SRC_Manifest.md:2979`: *"he states he is 'in seminary currently in my last semester' and 'still a deacon', expecting priesting 'in May of this year' (`LS-118`)"* |
| `a202` recording 2 **is that debate** | Its own moderator, on tape: *"I'm **Evan Minton** of cerebral faith ministries… tonight we're having a conversation between **James** [Gadomski] and **Noah Edmunds**… The Reverend James is a **deacon** within the Anglican tradition, he is in his **final semester of seminary** at Trinity School for Ministry and is **expected to receive ordination to the priesthood this summer**"* — ⭐⭐⭐ **the same three life-stage facts as File 33's self-dating, from an independent speaker.** |
| Title and date align | `SRC_Channel_Inventory.md:129`: `7_egBtP9H1I` \| *Debate on Holy Orders within Anglicanism: Rev. James and Noah, Moderated by Evan Minton* \| **2020-03-02** \| 5023 s \| 2457 views \| *(blank decision — **not INGESTED, not DECLINED**)*. **Six days before File 33's 2020-03-08 upload.** |
| It is his **first** formal debate | Consistent: `7_egBtP9H1I` (2020-03-02) precedes every other debate row on the channel — the Papacy debate vs Noah Edmonds is `auiLAv8BYpk`, 2020-06-02. |

### The `a303` lesson applied — a low longest-common-run does NOT clear it, so title/date/duration were brought alongside

| Test | `a202` recording 2 vs File 33 |
|---|---|
| Longest common run (case/punctuation-normalised) | **107 characters** — and ⭐ **it is a liturgical quotation**, *"…that our sinful bodies may be made clean by his body and our souls washed through his most precious blood…"* (Prayer of Humble Access), quoted independently in both. **Not shared transcript.** |
| `quick_ratio` | 0.5273 — character-frequency similarity of English prose, carrying no content claim |
| **Duration** | ⭐⭐⭐ **83:43 (5,023 s) vs 33:30 (2,010 s)** |
| Transcript length | 80,479 chars vs 28,812 chars — ratio 2.79 against the duration ratio 2.50 |
| Speaker count | **3** (Minton, RJ, Noah) vs **1** (RJ solo, label `A` only) |

⛔⛔ **THE `a303` CLASS IS EXCLUDED ON DURATION, NOT ON THE RUN LENGTH.** Two ASR engines over one audio produce the same duration and comparable word counts; a fifty-minute difference and a 1-vs-3 speaker count cannot be an engine artifact. **These are two different recordings of two different events. `a202` recording 2 is NOT a duplicate of File 33 and does not re-supply it.**

⭐⭐⭐ **AND THE RELATION IS THE VALUE, NOT THE PROBLEM.** File 33's own manifest guard says *"Noah's arguments are **characterized at length and are NEVER his**."* The corpus currently holds this debate **only through RJ's secondhand characterization of his opponent.** `a202` recording 2 supplies **Noah's actual words from the event being characterized** — which makes it the rarest thing in this corpus: a chance to check one registered source's characterization of an absent party against that party's own tape. **That is a strictly stronger reason to ingest it than mere novelty.**

### `a202` recording 1 — a different event entirely

Recording 1's opponent is **not** Noah Edmonds. On tape: *"combating him with the counter distinction… the negative that the holy orders with[in] anglicanism are not valid is going to be **john fisher**, a **john fisher 2.0**… the loyal apologist of the universal pontiff of rome"*; Noah Edmonds appears **only as moderator** (*"my name is noah edmonds of the eccentric naturalist and i'm going to be moderating this debate"*; and at close, *"i am no[ah] edmunds of the eccentric n[aturalist]"*). Channel row: `MLCh-d15F_o`, **2020-08-29**, 5,897 s, 1,364 views, blank decision. ⚠️ The channel also holds `x0hfBI6w6f0` *Debate: Is Apostolicae Curae Correct? (Opening Statements Only)*, 2020-08-28, 2,483 s — an **opening-statements-only partial of the same event**, which recording 1 subsumes; the next pass should not ingest both.

⭐ **The "noah edmonds" collision in the brief is a ROLE coincidence, not an identity error** — same man, opponent in March, moderator in August. Both roles are stated on tape.

## RESULT 3 — THE OTHER 48 RECORDINGS

**Registry check.** `SRC_Manifest.md` holds **39 File-numbered sources**, 5 Discord archives, 14 unnumbered A101 capture files and 46 `W`-numbered sources (**104 registered primary sources**; next free File number **40**). **Not one of the 51 recordings in these eight files matches any registered File by title, date, video ID or content.** Every corresponding video ID in `SRC_Channel_Inventory.md` carries a **blank decision** — neither `INGESTED` nor `DECLINED`.

**Nearest-neighbour checks run and cleared:**

| Recording | Nearest registered source | Cleared because |
|---|---|---|
| `a201` · 1 *Talk with Fr Matt Kennedy* | ⛔ none — the LS interview batch (Files 20-22, 28-29) holds Saller, Alander, Devereux, Findley, Truglia; **Kennedy is not among them** | different guest, different video ID |
| `a202` · 1 Apostolicae Curae debate | **File 32** *Are Holy Orders Within Anglicanism Valid? A Response Video* (`uSHi3Fqgerg`, 2025-08-21) | ⭐ **same topic, five years apart, different form** — File 32 is a solo response to *"5 Minute Catholic Apologetics"*; recording 1 is a moderated live debate vs John Fisher 2.0 |
| `a202` · 1 title string | **File 30** (`Heschmeyer`) renders Fr John J. Hughes's book as *"Absolutely Null and Utterly **Boyd**"* | ⚠️ **a shared TITLE STRING is not a shared recording.** Both quote the same 1896 bull and the same book; neither is the other |
| `a101-1` · 2 *Session II: The Doctrine of God (Classical Theism)* | `a106` · 2 / `a301` *Classical Theism* | ⭐ **checked and distinct** — `a101-1` recording 2 is 2024 Anglican 101 (38,705 B, no `>>` markers); `a106` recording 2 is 2026-06-06 Trinity Sunday (29,311 B, 33 `>>` markers). Two teachings on one topic, two years apart |
| `a105` · all 7 | Files 4, 8-12 (`a302`/`a104`/`a104-2`/`a305`/`a306`/`a307`, the Revelation corpus) | different series entirely; `a105` is Christ in the OT |
| all `a1xx` | `a303` (⛔ rejected re-supply) and `a304` (⛔ rejected re-supply) | neither overlaps this scope set |

⚠️⚠️ **THE CLEARANCE IS AGAINST `SRC_Manifest.md`, AND THAT IS NOT THE SAME AS "NEW."** Per the load-bearing result above, seven of eight files are already mined into `St_Francis_EMC_Distinctives.md` under `A101-`, `AW-`, `COT-`, `ANF-`, `Misc-2025`, `Ember`, `Lent vid` and `Recon-Euch`. **"Not in the manifest" ≠ "not already mined."** The duplicate risk for these files is **not a duplicate SOURCE; it is a duplicate FINDING minted under a second prefix.** That risk is real, is not cleared by anything in this pass, and is the single strongest reason the intake order in Task 5 is what it is.

---

# TASK 3 — TERM BATTERY AND PRIORITY RANKING

## 3.1 ASR quirks folded into the battery, and which registers they came from

`SRC_Manifest.md` carries **28 distinct quirk-register sections** (headings at lines 267, 532, 603/619, 811/831, 918/928, 1136, 1250, 1277, 1411, 1445, 1476, 1623, 1636, 1777/1786, 1906, 2096, 2183, 2383, 2412, 2486, 2550, 2633, 2710, 2775, 2900, 2985, 3076, 3232), plus `asr_keyterms_A101.md`. **Quirks folded into this battery, each named with its register:**

| Correct term | ASR rendering(s) folded in | Register |
|---|---|---|
| **Eucharist** | ⭐⭐⭐ *"the universe"* (×5), *"the Ubers"* | `260819-1` (§ *"THE PASS'S LOAD-BEARING ASR RESULT"*); `260809-1` `[R]` |
| **liturgical** | *"lurgical"* / *"a lurgical"* (File 16, ×29) **and** *"lurggical"* (Files 8, 10, 12, and the `IP-12` `[S]` register) | `260826-5`; `260813-1`; `260814-1`; `260823-1`; `260807-1` |
| **regulative (principle)** | ⭐ *"regular principle"* — the founding precedent at `IP-12` | `260807-1`; `260819-1` |
| **adiaphora** | *"a diaport"* — **plus** the plain-English paraphrase *"indifferen[t/ce]"*, added by this pass on expected-coverage grounds | `260819-1` |
| **element(s)** | ⛔ *"elbows"* (*"the consecrated elbows"*) | `260820-1` |
| **censer / incense** | ⭐⭐⭐ *"sensor"* / *"golden sensor"* | `260813-1` |
| **sola scriptura** | *"solar scripture"*, *"soul scripture"*, *"sole scripture"* | `260813-1`; `260827-2`; `260829-4` |
| **formularies** | *"the Anglican formulas"* (bare `formular` returns 0) | `260829-4` |
| **homilies** | *"homaly"* / *"homalies"* | `260809-1` `[S]` |
| **Book of Common Prayer** | *"Book of Congress"*, *"book of comma prayer"*, *"turbbook"/"turbook"* | `260816-1`; `260829-4`; `260812-1` |
| **Articles by bare number** | ⭐⭐ *"the authority of the church at number 20"*, *"the 29th article"* — an `Article 34`-shaped grep is **structurally blind** | `260829-4` |

⚠️ **Two quirks deliberately NOT folded, and why:** *"Hyria"/"Hyrea"* is **Council of Hieria**, ⛔ **not `hyperdulia`** — `asr_keyterms_A101.md` records the `260816-1` brief's attribution as expressly **WRONG**, corrected at `260818-3`; and *"the Ubers"* (Eucharist, `260809-1` `[R]`) is flagged in its own register as a **false-positive trap**, so its 0 count here is reported but carries no weight either way. Both were checked; neither fires in these eight files.

⚠️ **Three structural traps checked before any zero below was written**, per the `260819-1` *"family of three"*: **(1) mangled forms** — folded above; **(2) transcription conventions** — the *"2nd Commandment"*/*"second commandment"* trap; **(3) line structure** — ⭐ **none of these eight files is hard-wrapped.** Each is one very long line per segment, so the `SRC_WHISPER_20260809.txt` hard-wrap false-absence class **cannot** occur here. That is stated because it is the reason these zeros are trustworthy, not an assumption.

## 3.2 Whole-file battery

*(Counts are regex-family totals — clean spellings plus every folded quirk. `·` = zero.)*

| Term family | **a101-2** | a105 | a101-1 | a103 | a106 | a201 | a202 | a301 |
|---|---|---|---|---|---|---|---|---|
| `regulative` (+*regular principle*) | ⭐⭐⭐ **30** | 1 | · | · | · | · | · | · |
| `element` (+*elbows*) | 18 | 3 | 2 | 1 | 3 | 10 | 8 | · |
| `circumstance` / `circumstantial` | ⛔ **·** | ⛔ **·** | ⛔ **·** | 1 | 3 | ⛔ **·** | 2 | · |
| `adiaphora` (+*a diaport*, *indifferen-*) | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** |
| `incense` / `censer` (+*sensor*, *frankincense*, *thurible*) | ⭐⭐⭐ **31** | ⭐ **11** | · | 5 | · | 1 | · | · |
| `tradition` | ⭐ **46** | 3 | ⭐⭐ **49** | 28 | 14 | 29 | 32 | · |
| `received` / `receive` | 43 | 19 | 39 | 14 | 1 | 28 | ⭐ **60** | 1 |
| `consensus` | 3 | 1 | ⭐ **10** | 4 | · | · | 4 | · |
| `burden` | 1 | · | · | · | · | 2 | · | · |
| `warrant` | ⛔ **·** | ⛔ **·** | 2 | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** |
| **`Article 34` / `Article XXXIV`** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** |
| `showbread` / `shewbread` / *bread of the presence* | ⛔ **·** | ⭐⭐⭐ **4** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** |
| `Malachi` | ⭐⭐ **11** | ⛔ **·** | 1 | 1 | 2 | · | 1 | 2 |
| `Eucharist` (+*the universe*, *the Ubers*) | 19 | 6 | 12 | 22 | 1 | 26 | ⭐⭐ **119** | 1 |
| `liturgical` (+*lurgical*, *lurggical*) | ⭐ **44** | 10 | ⛔ **·** | 1 | 1 | 1 | 3 | · |
| `sola scriptura` (+*solar/soul scripture*) | · | · | 3 | · | · | · | 1 | · |
| `Article(s) <n>` / *of Religion* | · | · | 9 | 2 | · | 1 | ⭐ **30** | · |
| `formularies` (+*formulas*) | 1 | · | 4 | 1 | · | 4 | ⭐ **36** | · |
| `homilies` (+*homal-*) | 3 | · | 2 | · | 6 | · | 17 | 3 |
| `antitype` / `typology` / *a type of* | ⛔ **·** | ⛔ **·** | 1 | · | · | · | 1 | · |
| `Levitic-` | · | ⭐⭐ **32** | 2 | 2 | · | · | · | · |
| `tabernacle` | 1 | ⭐⭐ **28** | · | · | · | · | 1 | · |
| `sacrific-` | ⭐ **70** | ⭐⭐ **90** | 41 | 19 | · | 4 | ⭐ **79** | · |
| Book of Common Prayer / prayer book (+quirks) | ⭐⭐⭐ **129** | 2 | 27 | 2 | · | 9 | 50 | · |

## 3.3 ⭐ SEGMENT-LEVEL BATTERY FOR THE TWO PRIORITY FILES — *the part that makes the next pass possible*

### `a101-2.md`

| Term | AW-I `41`–`29,822` | AW-II `29,823`–`62,397` | AW-III `62,398`–`91,983` | **AW-IV `91,984`–`116,830`** | **AW-V `116,831`–`139,747`** | AW-VI·1 `139,748`–`151,802` | AW-VI·2 `151,803`–`160,769` | Ember `160,770`–`166,782` | **Instr.Euch `166,783`–`248,029`** | Lent `248,030`–`263,994` |
|---|---|---|---|---|---|---|---|---|---|---|
| `regulative` | ⭐⭐⭐ **15** | · | · | · | · | · | · | · | · | · |
| `incense`/`censer` | ⭐⭐ **8** | · | · | ⭐ **3** | · | · | · | · | ⭐⭐⭐ **20** | · |
| `Malachi` | ⭐⭐ **5** | · | · | ⭐ **2** | · | · | · | · | ⭐ **4** | · |
| `tradition` | · | ⭐⭐ **22** | 2 | 1 | ⭐ **8** | 7 | 1 | · | 3 | 2 |
| `received` | 7 | 1 | · | 2 | ⭐ **15** | 1 | · | · | ⭐⭐⭐ **42** | 1 |
| `consensus` | · | · | · | · | · | · | ⭐ **3** | · | · | · |
| `Eucharist` (+q) | 2 | 4 | · | · | ⭐ **10** | · | · | · | 3 | · |
| `element` | 1 | · | · | · | 2 | 3 | · | · | ⭐ **12** | · |
| `altar` | 2 | · | · | ⭐ **7** | 3 | · | · | · | ⭐ **6** | 1 |
| `sacrific-` | ⭐ **22** | 12 | 1 | 3 | ⭐⭐ **24** | · | · | · | 8 | · |
| `liturgical` (+q) | · | 3 | · | 1 | 2 | ⭐ **9** | · | · | 7 | 5 |
| `burden` | · | · | · | · | 1 | · | · | · | · | · |
| **`circumstance`** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** |

### `a105.md`

| Term | cl.2 `40`–`20,504` | cl.3 `20,505`–`52,549` | **cl.6 Tabernacle `52,550`–`76,107`** | cl.5 `76,108`–`105,802` | cl.4 `105,803`–`139,614` | **cl.7 Levitical `139,615`–`165,438`** | cl.9 `165,439`–`188,769` |
|---|---|---|---|---|---|---|---|
| **`showbread`** | · | · | ⭐⭐⭐ **4** | · | · | ⛔ **·** | · |
| `tabernacle` | · | · | ⭐⭐⭐ **27** | · | 1 | · | · |
| `incense` | · | · | ⭐⭐ **7** | · | · | ⭐ **3** | · |
| `Levitic-` | · | · | 2 | · | 3 | ⭐⭐ **15** | · |
| `altar` | · | · | ⭐ **5** | · | · | ⭐ **5** | 1 |
| `sacrific-` | 1 | 19 | ⭐ **21** | 2 | ⭐ **22** | ⭐ **23** | 2 |
| `received` | 1 | 3 | 1 | ⭐ **8** | ⭐ **8** | 4 | 1 |
| `liturgical` (+q) | · | · | 3 | · | · | 3 | · |
| `tradition` | · | 1 | 1 | · | · | 1 | · |
| `Malachi` · `regulative` · `circumstance` · `antitype` | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** | ⛔ **·** |

## 3.4 ⭐⭐⭐ THE ABSENCES, REPORTED AS FINDINGS

Each was chased through the mangled-form, convention and line-structure checks before being written down.

### ⛔⛔⛔ ABSENCE 1 — `circumstance` IS ZERO IN THE ENTIRE ANGLICAN WORSHIP SERIES, INCLUDING THE SEGMENT WITH FIFTEEN `regulative` HITS

**`circumstance` / `circumstantial` = 0 in all eleven segments of `a101-2.md`.** It is also 0 in `a101-1.txt` (all eight Anglican 101 sessions), 0 in `a105.md`, and 0 in `a201.txt`. It fires only in `a103` (×1), `a106` (×3) and `a202` (×2) — none of them worship-teaching contexts.

⭐⭐⭐ **This is the strongest single datum the pass produced for the element/circumstance question.** The corpus's existing position (`260834-5`) is that he *"has been handed the distinction twice and taken it up neither time"* — at `BP-48`(b) naming it only inside a *tu quoque*, and in `A101-2026-08-09` segment 3 answering the concrete case from Article XXVIII instead of engaging the framing. **This pass adds the third and cleanest kind of evidence: not a non-uptake under pressure, but a spontaneous, unprompted, six-week systematic exposition of Anglican worship — his own syllabus, his own handouts, his own pace — in which he uses `regulative` fifteen times and the word `circumstance` not once.**

⛔⛔ **THIS IS AN ABSENCE AND IS LOGGED AS ONE.** It is **not** rejection of the distinction, **not** tacit acceptance, **not** evasion, and **not** evidence he is unaware of it. `260834-5`'s ruling that *"A NON-UPTAKE IS AN ABSENCE"* governs, and this is weaker than a non-uptake, not stronger: nobody put the distinction to him here. ⛔ **`DQ-9` IS NOT MOVED BY THIS PASS.**

### ⛔⛔ ABSENCE 2 — `Article 34` / `Article XXXIV` IS A TRUE ZERO ACROSS ALL EIGHT FILES

Chased through **six** forms before being reported, because `260829-4` records that Articles are cited by **bare number** and an `Article 34`-shaped grep is *"STRUCTURALLY BLIND"*:

| Form searched | Hits, all eight files |
|---|---|
| `article\s*34` / `number\s*34` / `article thirty-four` | **0** |
| `34th` / `thirty-fourth` | **0** |
| *"rites and ceremonies"* (+ *"rights and ceremonies"*, the `IP-34` mangling) | **0** |
| *"particular or national church"* / *"national church hath"* / *"every particular church"* | **0** |
| *"traditions of the church"* | 1 in `a101-2`, 1 in `a103` — ⚠️ **inspected; neither is an Article XXXIV citation** |
| *"openly break"* / *"willingly and purposely"* | **0** |

⭐ **`IP-84` (Article XXXIV) receives NO corroboration and NO challenge from any of these eight files.** The Article he leans on for jurisdictional ceremonial authority is not quoted, cited, numbered or paraphrased anywhere in 1.47 MB of his own worship and identity teaching. ⛔ **Reported as an absence. `IP-84` is neither confirmed nor extended nor weakened by this pass.**

### ⛔⛔ ABSENCE 3 — `adiaphora` IS ZERO IN ALL EIGHT FILES, INCLUDING ITS PARAPHRASE

0 for `adiaphor-`, 0 for the `260819-1` mangling *"a diaport"*, **and 0 for the plain-English `indifferen-`** — the paraphrase a preacher would reach for if avoiding the Greek. Consistent with `260834-5`'s record that the term reaches him from **objectors** (`A101-2026-08-09` s2401-s2412) rather than from him.

### ⛔ ABSENCE 4 — `burden of proof` IS ZERO; ALL THREE `burden` HITS ARE THE ORDINARY SENSE

Every occurrence was read in context:

- `a101-2` @130,525 — *"often times we can be so **burdened by our sins** that we believe we are unforgivable"* (AW-V, the Comfortable Words)
- `a201` @11,342 — *"it does take the **burden and weight** um focusing on the object[ive] promises"* — ⚠️ **and this is Fr Matt Kennedy speaking, not RJ**
- `a201` @11,489 — *"takes the **burden off of** the subjective person"* — ⚠️ **also Kennedy**

⭐ **`260826-5`'s authority-rule / burden-of-proof distinction is untouched, and `260834-5`'s `burden of proof` = 0 across all 118 primary sources now extends to these eight unregistered files as well.** ⛔ Nothing here identifies the two rules.

### ⛔ ABSENCE 5 — `warrant` IS ESSENTIALLY ABSENT FROM HIS OWN VOCABULARY

`warrant` = 2 in `a101-1.txt`, **0 in the other seven files** — including the entire worship series. ⭐ Relevant to `DQ-9` as a **method datum**: the act-level/principle-level warrant question is posed in the project's vocabulary, not his. ⛔ Logged as an observation about vocabulary. **It is not evidence about his position and must not be read as any.**

### ⛔ ABSENCE 6 — `antitype` / `typology` IS ZERO IN `a105`, THE TYPE/ANTITYPE FILE

`a105.md` announces *"how they point to Christ"* and delivers 32 `Levitic-` and 90 `sacrific-` hits, with **0** for `antitype`, `typolog-` or *"types and shadows"*. ⭐ **He does the reasoning without the vocabulary** — which means **a term-keyed search of `a105` for type/antitype material will return a confident and entirely false zero.** ⚠️ **This is the most dangerous artifact the battery found**, and it is exactly the `260829-4` *"a non-zero count is more dangerous than a zero"* class inverted: here the clean spelling returns zero while the material is present in bulk. **The next pass must read `52,550`–`76,107` and `139,615`–`165,438` rather than grep them.**

### ⚠️ ONE NON-ABSENCE WORTH THE SAME WARNING — `Malachi` = 0 IN `a105`

`Malachi` fires **11 times in `a101-2`** (AW-I ×5, AW-IV ×2, Instructed Eucharist ×4) and **0 times in `a105`**. Malachi 1:11's *"in every place incense shall be offered unto my name, and a pure offering"* is the standard eucharistic-sacrifice and incense proof-text, and `260831-3` already records File 34's *"and a pure offering"* / *"in a pure offering"* rendering split. ⭐ **The Malachi material is in the WORSHIP series, not the Old Testament class** — the opposite of where a reader would look.

## 3.5 ⭐ PRIORITY RANKING AGAINST THE STANDING QUESTIONS

*(⭐⭐⭐ = bears directly and heavily · ⭐⭐ = bears directly · ⭐ = bears indirectly · — = nothing found)*

| File | `DQ-9` act/principle warrant | `DQ-24` five-level ordering | element/circumstance | `OQ20` "received" | `IP-84` Art. XXXIV | Eucharist & eucharistic reasoning | burden of proof | **Overall** |
|---|---|---|---|---|---|---|---|---|
| **`a101-2.md`** | ⭐⭐⭐ 15 `regulative` in AW-I + 31 `incense` | ⭐⭐ 46 `tradition`, 22 in AW-II | ⭐⭐⭐ **the zero, and it is the strongest zero in the pass** | ⭐⭐⭐ 43 `received`, **42 in the Instructed Eucharist alone** | ⛔ zero | ⭐⭐⭐ AW-IV+AW-V complete, 10 `Eucharist`/24 `sacrific-` in AW-V | ⛔ zero | ⭐⭐⭐ **1st** |
| **`a105.md`** | ⭐⭐ the OT-carryover strand `DQ-5`/`DQ-8` feeds into it | ⭐ 3 `tradition` | ⛔ zero | ⭐ 19 `received` | ⛔ zero | ⭐ 6 | ⛔ zero | ⭐⭐⭐ **2nd** — ⭐⭐⭐ **sole holder of `showbread`** |
| **`a202.txt`** | ⭐ | ⭐⭐ 32 `tradition`, 36 `formularies`, 30 Article-by-number | ⭐ 2 | ⭐⭐ 60 `received` (highest of the eight) | ⛔ zero | ⭐⭐⭐ 119 `Eucharist`, 79 `sacrific-` | ⛔ zero | ⭐⭐ **3rd** |
| **`a101-1.txt`** | ⭐ 2 `warrant` (the only ones) | ⭐⭐⭐ **49 `tradition` + 10 `consensus`; Session VI is literally *"Scripture (and Tradition)"*** | ⛔ zero | ⭐⭐ 39 `received` | ⛔ zero | ⭐ 12 | ⛔ zero | ⭐⭐ **4th** |
| **`a103.md`** | — | ⭐ 28 `tradition`, 4 `consensus` | ⭐ 1 | ⭐ 14 | ⛔ zero | ⭐⭐ 22 `Eucharist` | ⛔ zero | ⭐ **5th** |
| **`a201.txt`** | — | ⭐ 29 `tradition` | ⛔ zero | ⭐ 28 | ⛔ zero | ⭐⭐ 26 `Eucharist` (Memorialist + John 6:63) | ⛔ zero | ⭐ **6th** |
| **`a106.md`** | — | ⭐ 14 `tradition` | ⭐ 3 | ⛔ 1 | ⛔ zero | ⛔ 1 | ⛔ zero | **7th** |
| **`a301`** | — | — | — | — | — | — | — | ⛔ **8th — duplicate, do not ingest** |

---

# TASK 4 — ATTRIBUTION RISK, PER FILE

## ⛔⛔ FIRST: A CORRECTION TO THE BRIEF

**The brief states that `a301` is the only file carrying `>>` diarization markers. That is false.** Four files carry them; `a301` is not even the largest holder.

| File | `>>` count | Located in |
|---|---|---|
| `a106.md` | ⭐⭐ **75** | recording 2 (Classical Theism) ×33 · recording 3 (Sir Gawain) ×42 |
| `a101-2.md` | ⭐⭐ **39** | recording 9 (Instructed Eucharist) ×38 · recording 10 (Lent) ×1 |
| `a301-…md` | 33 | its single body — ⭐ **identical to `a106` recording 2's 33, corroborating the duplicate finding** |
| `a103.md` | 19 | recording 9 (final week) ×19 |
| `a101-1.txt` · `a105.md` · **`a201.txt`** · **`a202.txt`** | ⛔ **0** | — |

⛔⛔ **THE CONSEQUENCE INVERTS THE BRIEF'S RISK ASSESSMENT AT ITS MOST IMPORTANT POINT.** The brief expects `a201` and `a202` — the multi-voice compilations — to be the hard cases, and they are; but it also implies diarization is available where it is most needed. **It is available in exactly the files that need it least (solo teaching) and absent from exactly the two files that need it most (three-speaker debates).** ⭐ **`a101-2` recording 9 is the one happy case: the single most valuable segment in the pass is also the one large segment that carries diarization.**

## Per-file verdict

| File | Can Rev. James's voice be positively established from text alone? | Evidence and grounds |
|---|---|---|
| **`a101-2.md`** | ⭐⭐ **YES for 8 of 10 recordings; QUALIFIED for 2** | **Direct self-identification twice in his own voice**: *"**Father James here the rec[t]or of St Francis Anglican Church** in Spartenburg South Carolina"* (@160,772, Ember) and *"**Father James here, the director** of St. Francis Anglican Church in Spartanberg, South Carolina"* (@248,031, Lent); plus *"**I am Father James** if you liked this video please subscribe"* (@166,568) and *"**I'm Father James.** You can look, uh, my email is framesgdomsky…"* (@263,429). ⚠️ **Recordings 9 and 10 carry `>>` markers with NO speaker labels** — turn boundaries are visible, turn OWNERS are not. In recording 9 (Instructed Eucharist) the class asks questions; **the 38 `>>` boundaries mark where a non-RJ voice may begin and supply no way to tell which.** ⛔ **No quotation from a `>>`-delimited turn in recording 9 may be attributed to him without audio.** |
| **`a105.md`** | ⚠️⚠️ **NO — and this is the flag** | ⛔⛔ **ZERO name strings of any kind in 188,770 bytes.** No *"Father James"*, no *"Rev. James"*, no *"Gadomski"*, no *"barely protestant"*, no *"the rector"*, no self-introduction. The Source ID Legend asserts `COT` is *"RJ (all)"* — **that attribution does not come from this file.** ⭐ On the other hand `>>` = 0 and there is no handoff language anywhere, so there is **no positive evidence of a second teaching voice either**; the risk is not misattribution between two speakers but **an unestablished single speaker**. **FLAGGED: `a105`'s attribution rests entirely on external series/channel evidence and must be so recorded at registration.** |
| **`a101-1.txt`** | ⚠️ **WEAKLY — by second-person address only** | One name hit, and it is him **voicing a hypothetical questioner addressing him**: *"what's happening **Father James** why are you now saying that Jesus says not my will but thine"* (@50,101). That establishes the teacher is addressed as Father James; it is **not** a self-introduction. `>>` = 0, no guest handoffs, single continuous teaching voice in all eight sessions. **Acceptable, but it is inference from address, not identification.** |
| **`a103.md`** | ⭐ **YES for RJ's own 6 recordings; ⛔⛔ NO for 3 — AND THE BRIEF DOES NOT FLAG THIS FILE AT ALL** | RJ is named repeatedly **by the guests**, which establishes him as the host: *"Thank you, **Father James**"* (@92,374); *"**Father James** has already introduced some of them to you"* (@96,388); *"**Father James** knows I struggled"* (@115,000); *"first like to thank uh **father James** for giving me the great opportunity to teach this lecture"* (@124,994). ⛔⛔ **BUT THREE FULL RECORDINGS ARE TAUGHT BY SOMEONE ELSE** — recording 4 (`91,064`–`124,285`, **Dr. Steven Boyce**), recording 5 (`124,286`–`149,041`, **Kevin Valdez**), recording 7 (`177,046`–`205,246`, **Tyler West**) — **89,894 bytes, 34.7% of the file, in other men's voices**, with **no diarization** except recording 9's 19 markers. Each opens with RJ's collect and handoff and then **runs to the end of the segment in the guest's voice with no marked return.** ⚠️ **`a103` carries higher misattribution risk than `a201`, and the brief flags `a201` and not `a103`.** |
| **`a106.md`** | ⭐ **YES for recordings 1-2; ⛔ NO for recording 3** | Recording 3 (`47,840`–`80,481`, 32,642 B = **40.6% of the file**) is guest-taught and the guest names himself: *"**I'm Gregory Bronson**… **brother James** asked me to come and uh do a talk on my uh area of special specialization… I'm a professor of English at uh [Trevecca] University in Nashville"* (@48,439). ⭐ It carries 42 `>>` markers — turn boundaries but **no labels**. Recordings 1-2 are single-voice teaching; recording 2's 33 `>>` markers are congregational responses and Q&A. |
| **`a201.txt`** | ⭐ **YES — the strongest self-identification in all eight files — but ⛔⛔ RECORDING 1 OPENS IN THE GUEST'S VOICE** | ⭐⭐⭐ **@114,931: *"i am **father james godomski** although my first name is actually **adam** i had to have that written down for some reason"*** — full name, in his own voice, unprompted. Also @35,926: *"what is your[s] it's **barely Protestant**… that's a nickname I got from an Eastern Orthodox friend of mine when I was still Baptist"*. ⛔⛔ **THE TRAP IS AT THE TOP OF THE FILE: recording 1's first 500 bytes are FR MATT KENNEDY, not RJ** — *"welcome to whatever podcast this is… I'm with **Father James Gad**[omski] who's a friend of mine"* and *"I don't want to put words in your mouth Father James but let me just see if I can articulate the position that **you** were holding"*. **Anyone reading `a201.txt` from byte 52 reads a guest's words as RJ's.** With `>>` = 0 and 52 interlocutor signals across 36,993 bytes, **recording 1 cannot be speaker-separated from text alone.** ⭐ Recordings 2-9 are solo and safe. |
| **`a202.txt`** | ⚠️⚠️⚠️ **HOST/ROLE IDENTITY: YES, EXPLICITLY. TURN-LEVEL ATTRIBUTION: NO — AND THIS IS THE WORST FILE OF THE EIGHT** | Both debates **introduce every speaker by name, credential and side** (quoted in full at §1.7), so **who is in the room, on which side, is fully established from the tape** — better than any other file here. ⛔⛔ **AND `>>` = 0 ACROSS ALL 211,170 BYTES.** Two three-speaker moderated debates — 175,745 bytes, **83.2% of the file** — with **no diarization, no labels, no turn markers of any kind.** ⚠️ The formal debate structure (announced opening statements, rebuttals, timed segments) gives a **coarse** structural handle that `a201` recording 1 lacks, but **cross-examination and open Q&A stretches are unrecoverable from text alone.** ⛔⛔ **File 33's standing attribution guard — *"a position stated as belonging to… 'Noah'… is NEVER Rev. James's position, even inside his own sentence"* — applies here with full force and in a harder form: in a202 the two men are speaking alternately in one undifferentiated stream.** **FLAGGED: no quotation from `a202` recordings 1 or 2 may be attributed to Rev. James without diarized audio.** |
| **`a301-…md`** | ⭐ **N/A — duplicate** | 33 `>>` markers, no labels, no name strings. Its attribution is `a106` recording 2's attribution. |

## Files flagged where Rev. James's voice CANNOT be positively established

1. ⚠️⚠️⚠️ **`a202.txt` recordings 1 and 2** (175,745 B) — three speakers, zero diarization. **The highest-risk material in the pass.**
2. ⚠️⚠️ **`a201.txt` recording 1** (36,993 B) — two speakers, zero diarization, **opens in the guest's voice**.
3. ⚠️⚠️ **`a103.md` recordings 4, 5 and 7** (89,894 B) — three guest lecturers, no marked return. ⭐ **Not flagged in the brief.**
4. ⚠️ **`a106.md` recording 3** (32,642 B) — Gregory Bronson throughout.
5. ⚠️ **`a105.md`, entire file** (188,770 B) — no second voice detected, but **no positive establishment of the first**.
6. ⚠️ **`a101-2.md` recording 9's `>>` turns** (38 unlabelled boundaries inside the pass's single most valuable segment).

**Total material where turn-level attribution is not establishable from text alone: ≈ 335,000 bytes, 22.8% of the 1,466,408-byte scope set** — before counting `a105`'s unestablished-single-speaker case, which would take it past 35%.

---

# TASK 5 — RECOMMENDATION

## ⛔⛔ THE RECOMMENDATION THAT COMES BEFORE THE ORDER

**Do not run the next pass as an intake. Run it as a retro-registration.** Seven of eight files are already mined into `St_Francis_EMC_Distinctives.md` under `A101-`, `AW-`, `COT-`, `ANF-`, `Misc-2025`, `Ember`, `Lent vid` and `Recon-Euch`, carrying **194 live citations** between them and cross-referenced from at least seven `IP` findings. **A fresh-source intake will mint second findings for material the ledger already holds.** The governing precedent is `260813-1`'s handling of `Rev` and Files 8-9: material mined before the manifest existed, given File numbers, hashes, byte offsets and session rows **without re-mining and without renumbering the existing tags**.

⛔ **AND THE PREREQUISITE THAT COMES BEFORE THAT:** the existing per-segment mining coverage is **unknown**. This pass established *that* the files were mined, not *how completely*. **A coverage check — which byte ranges have live `AW-`/`COT-`/`ANF-`/`Misc-` citations and which have none — should be run first, and it is cheap.** Registering first and discovering coverage second is the expensive order.

## ⛔ FILES THAT SHOULD NOT BE INGESTED

**`a301-Classical-Theism.md` — DO NOT INGEST. NO `File` NUMBER, NO SESSION ROW, NO FINDING TAG.**

Its entire content is `a106.md` bytes `18,461`–`47,771`: a 29,261-character longest common run out of 29,329, `quick_ratio` 0.9992, identical `>>` counts, identical tail. This is the `a304` class — one transcript supplied twice — and `SRC_Manifest.md:287`'s disposition for `a304` is the right one here. ⚠️ **But record it as a REJECTED RE-SUPPLY WITH ITS HEADER PRESERVED, not as a deletion**: `a301`'s `### Jun 6, 2026` is the evidence that `a106`'s `Misc 2025` banner is false, and destroying the file destroys the only internal witness to that error.

**No other file should be withheld.** Notably **`a202` should NOT be withheld despite carrying the pass's worst attribution risk** — the right response to 83.2% undiarized three-speaker material is a **diarization prerequisite**, not exclusion. Excluding it would leave the corpus holding the March 2020 debate **only** through File 33's admitted secondhand characterization of an absent opponent.

## RECOMMENDED INTAKE ORDER

### **0 — COVERAGE CHECK (prerequisite, not an intake)**
Map every live `A101-`, `AW-`, `COT-`, `ANF-`, `Misc-`, `Ember`, `Lent vid` and `Recon-Euch` citation in `St_Francis_EMC_Distinctives.md` onto the byte ranges in Task 1. **Reason:** determines for every one of the 51 recordings whether the next act is registration-only or registration-plus-mining. **Nothing below is safe until this is done.** Cheap; no number consumed.

### **1 — `a101-2.md`** ⭐⭐⭐
**Reason:** it holds **AW-IV and AW-V complete and byte-bounded** (`91,984`–`116,830` and `116,831`–`139,747`) — the two sessions a separate flagging pass already ranked top-tier — plus **AW-I, the single richest segment in all eight files** (15 `regulative`, 8 `incense`, 5 `Malachi`, 22 `sacrific-`), plus the **Instructed Eucharist** (81,247 B; 20 `incense`, 42 `received`, 12 `element`, 4 `Malachi`) which is the largest incense concentration in the scope set and bears directly on `OQ20`. It carries the pass's **strongest reportable absence** (`circumstance` = 0 across all eleven segments), the **only explicit in-voice recording date** in the eight files, and — uniquely — **diarization on its most valuable long segment**. Attribution is clean for 8 of 10 recordings. ⚠️ **Two conditions:** confirm the recording-6/7 boundary at `151,803` before writing session rows; and treat recording 9's 38 unlabelled `>>` turns as unattributable pending audio.

### **2 — `a105.md`** ⭐⭐⭐
**Reason:** **sole holder of `showbread` in the entire scope set** (4 hits, all in class 6, `52,550`–`76,107`), which bears directly on the live showbread and type/antitype reasoning behind `DQ-24`'s frankincense narrowing; and **class 7** (`139,615`–`165,438`) is the Levitical-sacrifices session with 15 `Levitic-` and 23 `sacrific-`. **Ingest both segments — the brief names only one and it is the wrong one for showbread.** ⚠️ **Three conditions:** the file is **not in class order** (2, 3, 6, 5, 4, 7, 9) and classes 1 and 8 are missing; `antitype`/`typolog-` grep to **zero** despite the material being present in bulk, so **read, do not grep**; and the file contains **no internal speaker establishment whatsoever** — record the attribution basis as external.

### **3 — `a101-1.txt`** ⭐⭐
**Reason:** promoted above `a202` on **cost**, not on richness. It is the **cleanest file of the eight** — the only one where every recording carries an explicit `==Title==`, with **zero guests, zero `>>` markers and one continuous voice** — and **Session VI is literally *"Scripture (and Tradition)"*** (`164,683`–`190,060`), which is the most directly on-point material in the scope set for `DQ-24`'s unprecedented ranking of *Tradition* and for `OQ21`. Whole-file `tradition` = 49 and `consensus` = 10, both the highest of the eight. ⚠️ Note the header comma inconsistency at sessions VI and VII.

### **4 — `a202.txt`** ⭐⭐ — **ingest, with a hard prerequisite**
**Reason:** the highest eucharistic density in the scope set (119 `Eucharist`, 79 `sacrific-`, 36 `formularies`, 30 Articles-by-number, 60 `received`), and ⭐⭐⭐ **recording 2 is the primary record of the very debate File 33 recaps** — the one opportunity in this corpus to check a registered source's characterization of an absent opponent against that opponent's own words. ⛔⛔ **PREREQUISITE: DIARIZED AUDIO. Do not mint a single finding from recordings 1 or 2 from text alone.** Recording 3 (`175,796`–`184,862`) and recording 4 (`184,863`–`211,169`) are solo and may be taken independently and immediately. ⚠️ Do not adopt the banner years; recording 1's *"(2021)"* conflicts with the channel's 2020-08-29, and the tape narrows it only to *"after mid-2020"* via the priest/deacon distinction.

### **5 — `a103.md`** ⭐
**Reason:** solid patristics material (28 `tradition`, 22 `Eucharist`, 4 `consensus`) and a `>>`-bearing final session, but its live questions are indirect. ⛔ **Ingest as SIX recordings, not nine** — recordings 4, 5 and 7 (89,894 B, 34.7%) are guest lectures by Boyce, Valdez and West with no marked return, and must be firewalled at intake exactly as the LS interview files are. ⚠️ Report the legend's "8 sessions" vs the actual 9.

### **6 — `a201.txt`** ⭐
**Reason:** eight clean solo recordings (2-9) with modest per-question yield, plus one high-value two-voice interview. ⭐ **Split the intake**: recordings 2-9 are solo, safe and can go straight in; **recording 1 (Fr Matt Kennedy, `52`–`37,044`) needs the same diarization prerequisite as `a202`** and is the more dangerous of the two files to read naively, because it **opens in the guest's voice**. ⚠️ Four of nine banner years are wrong.

### **7 — `a106.md`**
**Reason:** lowest yield of the seven ingestible files (`received` = 1, `Eucharist` = 1, `regulative`/`incense`/`showbread`/`Malachi`-in-worship-sense all 0). ⭐ **But it must not be skipped, because it carries the pass's second dating error**: recording 2 is a **2026** recording under a **`Misc 2025`** banner, and the Source ID Legend has copied the wrong year. ⛔ Ingest as **three** recordings, not six (two-line delimiter convention), firewall recording 3 (Gregory Bronson, 40.6% of the file), and **re-date recording 2 to 2026-06-06/07 on `a301`'s header plus the channel row — without touching recordings 1 and 3, which are genuinely 2025.**

### **8 — `a301-Classical-Theism.md`** ⛔ **DO NOT INGEST** — see above.

## What this pass did NOT do, stated explicitly

⛔ **No source registered. No finding minted. No `File`, `LS`, `IP`, `RV`, `DQ`, `BLOG` or `POD` number consumed** — next-free numbers remain **`File 40`**, **`DQ-25`**, **`IP-98`**, **`LS-129`**, **`RV-64`**, **`BLOG-159`**, **`POD-17`**, unchanged. ⛔ **No hash registered, no byte offset written into any registry, no session row created, no `VP-` pair, no `DELTA`.** ⛔ **`DQ-9` not moved. `IP-84` neither confirmed nor extended. `OQ20`, `OQ21` and `DQ-24` untouched. The element/circumstance question is left exactly where `260834-5` left it, with one additional absence logged as an absence.** ⛔ **`Incense_Conversational_Outline.md` NOT touched** — C11's drift (outline at `DQ-19`, ledger at `DQ-24`, 5 findings unreviewed) is reported above as a firing code and left standing. ⛔ **`RJ_Incense_Analysis.md`, `On_Incense_and_the_Altar.md`, `RJ_Final_Question_List.md`, `RJ_Open_Questions_and_Divergences.md`, `SRC_Manifest.md`, `St_Francis_EMC_Distinctives.md`, `PROJECT_STATE.md` NOT touched.** ⛔ **Nothing drafted, altered, or posted to Rev. James.** ⛔ **The two legend errors and the six banner-date errors are REPORTED, NOT CORRECTED.** ⛔ **No theological substance was read or analysed beyond what ranking required; what he argues in these files is the next pass's job and is not characterised here.**

**Touched exactly one file: this one.**

---

## ✅ VALIDATOR AFTER

```
80 ok · 9 warnings · 0 errors
```

**UNCHANGED from the BEFORE run — same count, same nine codes, in the same order.** Expected and confirmed: this pass added one file to `passes/`, which the validator's §0 file-discovery mechanism derives from `PROJECT_STATE.md` §4's registry table and therefore does not enumerate.
