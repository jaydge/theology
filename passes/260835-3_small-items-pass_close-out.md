# 260835-3 — THE SMALL-ITEMS PASS

**Nine items briefed. Nine items landed. Nothing deferred, nothing half-done.**

⭐⭐⭐ **THE HEADLINE IS ITEM 2, AND IT IS NOT THE ITEM THE BRIEF FLAGGED AS LARGEST BY ACCIDENT: `IP-98`…`IP-108` DISCHARGES A PREFIX RULING THAT HAS BEEN RESERVED TO JD SINCE `260833-3`, AND IN DOING SO MAKES ELEVEN FINDINGS VISIBLE TO `C11` FOR THE FIRST TIME.** Two consecutive passes recorded that the outline's drift counter could not see them. It can now.

⚠️ **AND THE PASS FOUND ONE THING NOBODY BRIEFED IT TO LOOK FOR, WHICH IS SECTION 0.2: THE `.git` LOCK IS NOT STALE AND NEVER WAS.** Six passes have reported "the stale lock recurred." It is not a leftover. **This repo's own `git status` manufactures it, every time, and cannot remove it.** The mechanism is established below.

---

## ✅ 0. GATE

| Check | Required | Found | Verdict |
|---|---|---|---|
| `git rev-parse HEAD` | `456e36c` | `456e36c5ff01184af4e8efcb32cb5c2e65b83c81` | ✅ **exact match**, branch `main` |
| Validator BEFORE | record summary + every firing code | `81 ok · 8 warnings · 0 errors` | ✅ all eight recorded at §0.1 |
| `PROJECT_STATE.md` stamp | report | **`260835-2`** | ✅ |
| Next-free pass stamp | derive by grep | **`260835-3`** | ✅ derivation at §0.3 |
| `.git/*.lock` | report, do not work around | ⛔ **NONE AT GATE** — and the reading changes | ⚠️ §0.2 |
| Next free `IP` | re-derive before consuming | **`IP-98`**, verified free two independent ways | ✅ §0.4 |

### 0.1 Every firing code, recorded individually (8 warnings, 0 errors)

```
WARN  [C1]  src/SRC_Discord_RPW.md: 2 relative timestamp(s) outside message headers ('Yesterday at …').
WARN  [C3]  Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: no parseable 'Last updated' stamp; registry says '260832-2'
WARN  [C3]  tools/transcribe_yt.py: no parseable 'Last updated' stamp; registry says '260833-7'
WARN  [C4]  St_Francis_EMC_Distinctives.md: 2 passage(s) describe an ANSWERED question as pending with no supersede marker nearby.
WARN  [C5]  RJ_Final_Question_List.md: 17 volatile-state assertions.
WARN  [C5]  RJ_Incense_Analysis.md: 9 volatile-state assertions.
WARN  [C5]  St_Francis_EMC_Distinctives.md: 7 volatile-state assertions.
WARN  [C10] §15's newest LS citation is 8 findings behind the ledger (LS-120 vs LS-128).
```

⛔ **All eight are pre-existing and none is this pass's subject. None was fixed, and none was made worse.** ⚠️ **The `C5` count for `RJ_Incense_Analysis.md` is unchanged at 9 despite this pass adding ~2,400 words to that file** — checked, not assumed.

### 0.2 ⚠️⚠️⚠️ THE `.git` LOCK — REPORTED, NOT WORKED AROUND, AND THE DIAGNOSIS OVERTURNS SIX PASSES' READING OF IT

**The brief says: stale `.git/*.lock` has recurred for six consecutive passes; report rather than work around.** ⭐⭐⭐ **Reported — and the finding is that it is not stale, not recurring, and not a leftover from anything.**

**What was observed, in order:**

1. **At gate, before any edit:** `ls -la .git/*.lock` → **nothing.** `.git/` clean. **There was no lock to inherit.**
2. `git rev-parse`, `git grep HEAD`, `git show HEAD:<path>` — all run during the pass, **all left `.git/` clean.**
3. **The pass's first `git status --short`** returned the six expected `M` lines **plus**:
   ```
   warning: unable to unlink '/…/theology/.git/index.lock': Operation not permitted
   ```
4. **After that command, and only after it:** a **zero-byte** `.git/index.lock`, mode `0600`, **birth 09:33:13 — this session.**

⭐⭐⭐ **THE MECHANISM, WHICH IS THE POINT OF THIS SECTION.** `git status` takes `index.lock` in order to refresh the index. The repo lives on a **FUSE mount** — `/proc/self/fd/3 on /…/mnt/EMC type fuse (rw,nosuid,nodev,relatime,user_id=0,group_id=0,default_permissions,allow_other)` — and that mount **denies the unlink**. Git creates the lock, does its work, tries to remove it, is refused, warns, and exits leaving the file behind.

⛔⛔ **SO EVERY ORDINARY `git status` IN THIS REPO MANUFACTURES ITS OWN "STALE" LOCK.** The lock a pass finds at gate is, on this reading, **the residue of the previous pass's own `git status`**, not evidence of an interrupted or crashed git operation. ⭐ **That explains the six-pass recurrence exactly, and explains why it recurs no matter what any pass does about it.**

⛔⛔⛔ **NOT REMOVED. NO `rm` ATTEMPTED. NOTHING REPAIRED.** The lock is present in the working tree as this pass ends and is left there deliberately.

⭐ **ONE READ-ONLY ACCOMMODATION, DISCLOSED RATHER THAN QUIETLY MADE:** every subsequent git read used **`git --no-optional-locks`**, which by design does not take the index lock. ⚠️ **This is stated as an invocation choice, NOT as a work-around: it removes nothing, repairs nothing, and changes no repo state. Output was compared against the locking invocation and is identical.**

⏳ **WHAT IS OWED, AND IT IS NOT THIS PASS'S TO DO:** if the diagnosis is right, the fix is at the mount, not in the repo, and the standing operational rule should become *"use `git --no-optional-locks` for reads in this repo"* rather than *"clear the stale lock."* ⛔ **Neither change is made here. `ORCHESTRATION.md` was NOT touched.**

⚠️⚠️ **ONE HONEST GAP IN THE GATE, STATED RATHER THAN GLOSSED.** `git status --short` **was not captured before the first edit** — the gate ran `rev-parse` and the lock check and went straight to work. **The clean-tree claim is therefore a RECONSTRUCTION, and it is labelled as one:** the final diff contains **20 deleted lines and every one is a line this pass deliberately modified**; no unattributable hunk exists; and **no file outside the six this pass touched is modified.** ⭐ **On that basis the tree was clean. It is inference from the diff, not observation, and a reader is entitled to know which.**

### 0.3 Stamp derivation

```
grep -rhoE '\b26[0-9]{4}-[0-9]+\b' --include='*.md' --include='*.py' . | sort -u
```
Highest stamp in the repo: **`260835-2`** (`PROJECT_STATE.md`, `Incense_Conversational_Outline.md`, and three `passes/` artifacts). ⭐ **Next free is `260835-3`.** ⛔ **No ambiguity this time** — unlike `260835-1`, whose derivation note recorded one; `260835-3` returns zero hits repo-wide before this pass.

### 0.4 Next-free `IP`, re-derived fresh — and this one was actually consumed

⭐⭐ **The brief requires `IP-98` to be re-derived as genuinely free BEFORE being consumed, and it was, two independent ways, both against `HEAD` rather than against the working tree.**

1. **Occurrence audit.** `git grep -hoE '\bIP-(9[89]|1[0-9][0-9])\b' HEAD` returns **exactly one token in the whole repo: `IP-98`** — nothing at `IP-99` or above exists anywhere. **All 21 occurrences of it were then read in context** — `PROJECT_STATE.md` ×7, `St_Francis_EMC_Distinctives.md` ×3, and eleven `passes/` close-out lines across `260833-4`, `260834-5`, `260834-6`, `260834-7`, `260834-9`, `260835-1` and `260835-2`. ⭐ **Every single one is a next free registry line or a pass note recording it unspent. Not one is a finding.** *(The full 21-line listing is at §4 of the raw-session-output artifact.)*
2. **Enumeration and diff.** `git show HEAD:St_Francis_EMC_Distinctives.md`, extract every `^\*\*IP-N\.\*\*`, sort-unique, diff against `seq 1 97` → **identical. `IP-1`…`IP-97` complete, no gaps, no extras.**

⛔ **`IP-98`…`IP-108` are now SPENT. Next free is `IP-109`.**

---

# 1. ⭐⭐⭐ ITEM 1 — THE SPOKEN CORE CLAUSE, JD's TEXT AND JD's RULING, APPLIED VERBATIM

**Applied exactly as given, one clause, in `Incense_Conversational_Outline.md`'s two-minute spoken core:**

> *"…with a grain offering in the same breath **that nobody performs**, is carrying the whole weight…"*
> → *"…with a grain offering in the same breath **which may be kept in the antitype but is certainly not kept literally**, is carrying the whole weight…"*

⛔⛔ **NOTHING ELSE IN THE PARAGRAPH CHANGED.** Not a word reordered, tightened, condensed or re-punctuated outside the replaced clause. ⭐ **The `HANDLING` header protects this paragraph from pre-emptive hybrid-dismantling and from pass-side rewording; both protections are intact, because the edit is JD's own.**

⭐⭐ **THE `260835-2` DATED NOTE STAYS AND THE NEW NOTE SITS BESIDE IT, AS THE BRIEF REQUIRES.** Nothing in the `260835-2` note is altered or marked superseded. It was right on the merits and right to decline to act, and it now reads as the record of why the change was owed.

**The new `260835-3` note records exactly the three things the brief specified:**

**(a) What the original clause meant, so it is not remembered as an error.** *"Nobody performs"* meant **nobody performs the TYPE — the burnt grain offering of Leviticus 2 itself**, and on that reading it was **true as intended and remains true**. ⚠️⚠️ **Its defect was never truth. It was that it is ANSWERABLE AS HEARD:** spoken to him, it invites the one-sentence reply `260835-2` anticipated — *on my account the grain offering IS performed, in the antitype, every Sunday* (`File 43 @141,115`–`@163,900`). **A clause true on its intended reading and defeated on its natural one is a defect in a paragraph whose entire function is to be spoken.**

**(b) What the replacement does.** It **anticipates his antitype answer without asserting it on his behalf**, and the modal split carries the load: ***may*** concedes the antitype reading as available to him and leaves it his to make; ***certainly*** holds the literal half, which is the half the argument actually needs. ⛔ **It does not attribute the antitype position to him, does not put the Sursum Corda mapping in his mouth in the spoken core, and does not dismantle the hybrid.**

**(c) ⛔⛔⛔ THE EVIDENTIAL LIMIT, RECORDED IN FULL — AND IT IS THE MOST IMPORTANT SENTENCE IN THIS SECTION.** **The corpus does NOT have him connecting Malachi's *minchah* to the Levitical grain offering he maps onto the 1928 ordo.** Two separate teachings exist:

- **(i)** he renders Mal 1:11's second clause *"a pure, **or a grain**, sacrifice"* — `File 41 @195,097`–`@195,300`, 2025, the Instructed Eucharist;
- **(ii)** he runs the six Levitical offerings backward onto the 1928 rite and lands the **grain** offering at the Sursum Corda, the consecration and *"the bread and the wine"*, tied to Melchizedek — `File 43 @141,115`–`@163,900`, class 7, 2025-01-15.

⛔⛔ **NOWHERE DOES HE JOIN THEM.** Different classes, different subjects, a year and a half of separation in the corpus's own dating, and no cross-reference in his own voice. ⚠️⚠️ **The bridge is the PROJECT'S INFERENCE across two teachings. It is a good inference. It is still an inference.** ⭐ **The hedged wording is deliberate and the note says so explicitly, with an instruction that a later pass must not tighten it on the ground that it reads weakly: *"may be kept" is not timidity; it is the strongest claim the evidence supports.*** ⏳ **The connection is recorded as a live question and a candidate to put to him directly — ⛔ NOT drafted, NOT deployed, NOT posted.**

⭐ **The same limit is written a second time into `IP-106`'s `[Analysis]`, deliberately, so that it cannot be lost if the outline note is ever stripped with the metadata block.**

---

# 2. ⭐⭐⭐ ITEM 2 — `IP-98`…`IP-108`. THE LARGEST ITEM, DONE CLEANLY, NOT HALF-DONE

**The brief's condition was explicit: if it cannot be done cleanly, do the rest and report it undone rather than half-doing it.** ⭐ **It was done cleanly. `C2` reports `IP-1..108 unbroken, no duplicates`, `C10` reports `§15 within 0 of the IP ledger head`, and the validator ends at 0 errors.**

## 2.1 What the conversion actually is, and what it is not

`260835-1` mined eleven findings and minted **every one as a section bullet, consuming no ledger number**, because the `aNNN` sources have no numbered ledger and choosing a prefix has corpus-wide consequences (`C2`'s unbroken-range check, `C10`'s arithmetic, and every downstream citation form key off it). ⛔ **It reserved the ruling to JD on the `260833-3` precedent.** ⭐⭐⭐ **JD ruled `IP`, and the ruling is coherent with the convention rather than an exception to it: `IP` is *in-person*; `File 41` (`a101-2.md`) and `File 43` (`a105.md`) are in-person class series; `IP-84`…`IP-97` were minted from `A101-2026-08-23` on exactly that basis.**

⛔⛔⛔ **THE `260835-1` §13 AND §17 BULLETS ARE RETAINED WORD FOR WORD. Not deleted, not trimmed, not replaced, not marked superseded.** ⭐ **The never-alter rule governs and the bullets are the record of how the material entered the corpus and of a pass correctly declining to consume a number it had not been given.** ⚠️ **The material is therefore in two places, deliberately — and each place has a dated `260835-3` note giving the bullet→number mapping, so a reader landing on either finds the other. The ledger entry is authoritative for tag, anchor, warrant class and cross-references; the bullet is authoritative for nothing and is superseded by nothing.**

⛔ **This is a NUMBERING pass over material already in the corpus. No re-reading of `File 41` or `File 43` was performed, no new candidate was admitted, and every quotation, byte range and `[Stated]`/`[Analysis]` label is `260835-1`'s own, unrewritten.**

## 2.2 The mapping, in full

| # | New tag | Finding | Source |
|---|---|---|---|
| §13-1 | **`IP-98`** | Malachi 1:11's *"pure offering"* is **Christ** — twice, 2024, unprompted; a **third fork** | `AW-I` `@18,335`-`@18,760`; `AW-IV` `@113,900`-`@114,200`; `Recon-Euch` `@195,097`-`@195,300` |
| §13-2 | **`IP-99`** | The silence-of-Acts reductio + the burden rule a year before `DQ-24`(b) | `Recon-Euch` `@196,456`-`@197,090` |
| §13-3 | **`IP-100`** | The fulfilment rule's qualifier — *"uniquely Old Testament"* | `File 43 @75,677`-`@75,960` |
| §13-4 | **`IP-101`** | Ritual act as divine pedagogy — a **third** positive warrant | `File 43 @63,994`-`@65,240`; `@154,693`-`@155,600` |
| §13-5 | **`IP-102`** | The incense conversion narrative; Malachi named as decisive | `Recon-Euch` `@194,413`-`@194,930`; `@196,342`-`@197,025` |
| §13-6 | **`IP-103`** | Heaven and earth united, grounded on the **Incarnation** | `AW-V` `@130,384`-`@132,100` |
| §13-7 | **`IP-104`** | Wrong worship kills / Cain unpunished — both stand, neither harmonised | `AW-I` `@19,541`-`@20,150`; `File 43 @38,700`-`@39,000` |
| §13-8 | **`IP-105`** | Two ad-orientem rationales, a year apart | `AW-I` `@28,900`-`@29,450`; `File 43 @57,684`-`@57,800` |
| §17-A | **`IP-106`** | The six Levitical offerings mirrored onto the 1928 ordo | `File 43 @141,115`-`@163,900` |
| §17-B | **`IP-107`** | The showbread taught in full — **incense on top of the bread** | `File 43 @60,050`-`@63,141`; `@62,844`; `@144,858` |
| §17-C | **`IP-108`** | The Aqedah and Babel-at-Pentecost types | `File 43 @132,803`-`@137,100`; `@105,803`-`@107,700` |

## 2.3 Three warrant classes, every entry naming its own

- ⭐⭐⭐ **(a) EAR-VERIFIED** — `IP-98`, and the load-bearing clause of `IP-107`. **The first `aNNN` material ever checked against audio rather than against a transcript.** ⛔ **Scoped narrowly and said so in each entry: `IP-98`'s class (a) covers the `AW-I` passage only, not its `AW-IV` or `Recon-Euch` quotations; `IP-107`'s covers one clause, not the entry.**
- ⭐⭐ **(b) `File 43` — EXTERNAL ATTRIBUTION WARRANT** (item 6). `IP-100`, `IP-101`, `IP-106`, `IP-107`, `IP-108`, and the `File 43` halves of `IP-104` and `IP-105`.
- ⚠️ **(c) `File 41` — single `[S]` capture, byte-verified, attribution from series context.** `IP-99`, `IP-102`, `IP-103`, and the `File 41` halves of `IP-104` and `IP-105`. ⛔⛔ **`IP-99` and `IP-102` come from recording 9 and each states in its own Verification line that its material sits OUTSIDE all 38 unlabelled `>>` turns (nearest markers `@198,611`/`@198,618`). The firewall is honoured and is NOT relaxed by this pass's video establishment.**

## 2.4 §15 swept in the same pass — one credit, ten declines

⭐ **The §8 item 4 discipline is honoured: the common-ground sweep ran in the same pass that minted the numbers, and `C10` guards it.**

**THE ONE CREDIT: `IP-107`'s standing interpretive rule** — *"whenever you see incense in the Old Testament or in the New Testament, you associate it with the prayers of the saints of God."* ⭐⭐ **Genuine common ground and the strongest instance in the incense material: the New Testament's own reading of the symbol, stated by him as a general rule, to his own class, with no controversy in view.** ⛔⛔ **Credited on its merits and EXPRESSLY NOT as a concession — he holds the prayers reading and the physical practice together and has never treated the first as displacing the second.**

**TEN DECLINES, each with its reason.** ⭐ **The two worth naming here:**

- ⛔⛔ **`IP-98` DECLINED** — the christological content would credit easily, **but it is the pivot of the project's most active open question and filing it as agreement would settle by bookkeeping what §4.6/§4.8/§4.10 exist to keep open.**
- ⛔⛔ **`IP-106` DECLINED, and this is the decline that matters most.** It is careful, substantial, unprompted teaching a Reformed reader would recognise much of. **It is also the corpus's strongest positive warrant for the shape of his service and the datum that falsified a clause of the spoken core.** ⛔ **Crediting the project's most formidable adverse finding as common ground would be a category error, and the bullet exists to say so rather than to pass over it in silence.**

## 2.5 ⚠️ A discrepancy the conversion surfaced — reported, not resolved

**Two documents cite different byte ranges for the same `IP-98` material.**

| Datum | `St_Francis_EMC_Distinctives.md` §13 bullet 1 | `PROJECT_STATE.md` L29 |
|---|---|---|
| Mal 1:11 = Christ, `AW-I` | `@18,335`–`@18,760` | `@18,041`–`@18,600` |
| Mal 1:11 = Christ, `AW-IV` | `@113,900`–`@114,200` | `@113,000`–`@113,560` |

⛔ **`IP-98` carries the distinctives values, and the choice is STATED rather than made silently:** the §13 bullet is the findings-corpus record, it carries the fuller quotation, and `SRC_Channel_Inventory.md`'s `ZTs6Ru9ZdnI` row independently agrees with it — **two of three sources concur.** ⛔⛔ **Neither range is edited; `PROJECT_STATE.md` L29 is left exactly as written.** ⭐ **The ranges overlap, so the likeliest explanation is that one pair brackets the reading and the other the gloss — ⚠️ but that is a GUESS and is labelled as one.** ⏳ **A read at both offsets settles it in a minute. Not performed — outside the brief. Registered in `PROJECT_STATE.md` §7.**

---

# 3. ⚠️⚠️ ITEM 3 — `IP-90`'s FACTUAL SLIP

**`IP-90`'s `[Analysis]` reads:** *"THIS IS THE SAME EXAMPLE, **THIRTEEN MONTHS LATER**, IN TAUGHT FORM AND CARRYING MORE WEIGHT."*

⛔ **Wrong. `DQ-8` is 2026-07-11; the session is 2026-08-23. The interval is roughly SIX WEEKS.**

⛔⛔ **DATED CORRECTION BESIDE THE ORIGINAL, PER THE NEVER-ALTER RULE. The paragraph is retained exactly as written.**

⭐⭐ **AND THE CORRECTION SHARPENS THE ENTRY RATHER THAN WEAKENING IT, WHICH IS WHY IT IS WORTH MAKING AND NOT JUST NOTING.** The claim is that this is the same example, later, in taught form, carrying more weight. **All of that is true at six weeks and is MORE striking at six weeks than at thirteen months:** an example given in answer to a question in July reappearing unprompted as the load-bearing argument of his own class in August is **a live, continuous position** — where thirteen months would have been a recurrence.

⛔ **Nothing else in `IP-90` is affected. Its quotations, byte offsets, verification lines, the `showbread` 0·0 term scan and the `260833-3` Discord disposition all stand. `DQ-8` is NOT re-dated, amended or re-pointed — it was `IP-90`'s prose that was wrong, not the ledger.**

⚠️ **Likely cause, recorded so the CLASS of error is visible and not just the instance:** the `260833-4` block was reconciling 2025 `LS` material against 2026 `IP` material throughout, and a year's interval appears to have been carried across from that comparison into a within-2026 one. ⏳ **No other date arithmetic in `IP-84`…`IP-97` was re-checked. A sweep is OWED, not performed.**

---

# 4. ⚠️⚠️ ITEM 4 — THE TWO STALE REVELATION REFERENCES

**Both corrected as dated notes beside the originals, in `RJ_Incense_Analysis.md`:**

1. **The source line at the head of the file** — *"…the 2025 Revelation class (Rev-9/10/11)…"*
2. **The §1 body paragraph** — *"The 2025 Revelation class moves this warrant from IP-paraphrase to flat, repeated, first-person statement…"*

⛔ **Both original sentences retained exactly as written.** ⭐ **Read as: the 2026 Revelation series. There is no 2025 run and no 2026 run; there is ONE series, Session I (2026-03-27) through Session XVII (2026-08-17), with `Rev` and `RV` as two BATCHES of it.**

⭐⭐ **PROVENANCE CARRIED WITH THE CORRECTION, because it is not this pass's finding:** corrected at **`260822-2`** (commit `e3dd43a`) and **independently re-verified at `260834-8`** on four lines — channel enumeration confirmed three times by different methods (zero 2025 Revelation-titled videos exist), the single spoken year in Files 8-9 being 2026, Session III's *"I took my first look at Revelation 4"* preparation language, and per-session duration/byte correspondence at 13.0-14.2 B/s across all nine matched videos. **The *"genuine 2025 run, re-taught in 2026"* alternative was tested and strongly rejected.**

⭐⭐ **THE SUBSTANTIVE EFFECT, WHICH LANDS HARDEST AT OCCURRENCE 2:** that paragraph's whole point is that the heaven-earth warrant moves from IP-paraphrase to **flat, repeated, first-person statement**. **Under the corrected dating that testimony is LIVE 2026 — months, not a year, before the present exchange.** ⛔ **The argument is STRONGER than it reads, and any pass tempted to discount the material on vintage should stop there.**

⛔ **`Rev-9`/`Rev-10`/`Rev-11` NOT renumbered, re-pointed or re-dated, per the `260822-2` non-retroactivity ruling. Only the prose year-label is corrected, and only by these notes.**

### ⚠️ A THIRD OCCURRENCE EXISTS AND IS DELIBERATELY LEFT STANDING

**The brief said two places. There are three.** The third is in that file's own **CHANGELOG**, in the `260621-1` entry: *"…now first-person sourced from the 2025 Revelation class (Rev-9/10/11)…"*

⛔⛔ **NOT CORRECTED, and the decision is recorded in the file itself so its survival is a decision rather than an oversight: a changelog entry is a historical record of what a past pass did and believed. Correcting it would falsify the record rather than repair it.** ⭐ **`260834-8` §6, which found and named the two live occurrences, did not name this one either — the two analyses agree independently.**

### ⛔⛔⛔ §4.6, §4.8 AND §4.10 — NOT TOUCHED

**Confirmed by inspection at the end of the pass: not one character of §4.6, §4.8 or §4.10 is in the diff.** Their falsified *"unknown"* premise stands unedited beside `IP-98`'s report of it — **the third consecutive pass to report it and decline to rewrite it.** ⏳ **The rewrite is owed to a separate, scoped pass.**

---

# 5. ⭐⭐⭐ ITEM 5 — THE EAR VERIFICATIONS

⭐⭐⭐ **THE FIRST TIME ANY `aNNN` MATERIAL HAS BEEN CHECKED AGAINST AUDIO RATHER THAN AGAINST A TRANSCRIPT.** The corpus's standing `⏳ OPEN EAR-VERIFICATION FLAG` exists precisely because ASR text has never been heard. **Three passages have now been heard.** Registered as a new block in `SRC_Manifest.md`.

| # | Video | Verified | Result |
|---|---|---|---|
| 1 | `C2tCMfq-_hI` (**File 41** rec 9) | transcript at ≈**33:03**; and who is speaking | ✅ **word for word** · ✅ **speaker = Rev. James** |
| 2 | `R-GHhWcuH78` (**File 43** rec 3) | *"they put incense on top of the bread"*, `@62,844` | ✅ **confirmed** |
| 3 | `ZTs6Ru9ZdnI` (**File 41** rec 1) | full Mal 1:11 reading + christological gloss, `@18,335`-`@18,760` | ✅ **verbatim**, ⚠️ + one structural datum |

## 5.1 ⭐⭐⭐ Verification 1 discharges `260834-9`'s open provenance question

**`260834-9` registered `C2tCMfq-_hI` as `File 41` recording 9's video on three legs, none a verbatim title match, and marked the row EVIDENCED BUT NOT ESTABLISHED — correctly, and it said leg (c) was weak.** ⭐⭐⭐ **It is now ESTABLISHED.** Audio at 33:03 matching the transcript verbatim is something no coincidence of length, subject or byte-rate can produce.

**Two separate claims were settled by one listen and are recorded separately, because they are separate:** **(i)** the **video↔recording match**; **(ii)** the **speaker at that point** is Rev. James, heard rather than inferred.

**Updated:** the `SRC_Manifest.md` standalone row's `Recorded` cell (EXTENDED, original text intact), the `Recon-Euch` three-leg note (dated note beside it, original intact), and the `SRC_Channel_Inventory.md` decision cell — **which now reads `INGESTED`, having been the one row `260835-1` deliberately kept as a candidate while minting from the recording.** ⭐ **`260835-1` was right to keep minting-from-the-recording and establishing-the-video apart; the second has now happened on its own evidence.**

⚠️ **ONE ARITHMETIC OBSERVATION, LABELLED AS THE PROJECT'S OWN INFERENCE AND NOT AS PART OF JD's REPORT.** At 14.3 B/s, 33:03 (1,983 s) into a recording beginning at byte 166,783 lands near **`@195,150`** — inside the `@193,700`-`@197,200` band `260835-1` mined four findings from. ⛔ **Recorded as CONSISTENT, not as establishing which passage was heard. JD's report specifies a timestamp and a speaker, not a byte offset, and no entry claims more than that.**

⛔⛔ **THREE LIMITS ON THE DISCHARGE, stated so it is not over-read:** **(1)** it does **not** clear recording 9's 38 unlabelled `>>` turns — confirming him at one point in a recording containing audience questions establishes nothing about the marked turns, and the firewall stands; **(2)** it does **not** establish a RECORDING date — 2025-09-23 remains an upload date; **(3)** it extends to **no other** unestablished match, `PEGUfE6Y2LA`/`COT-Class2` in particular.

## 5.2 ⚠️⚠️ Verification 3 — the *"by the way"* datum, recorded both ways

⭐⭐ **Heard on the tape, the sequence is: he reads Malachi 1:11 through, and THEN — prefaced by *"by the way"* — supplies the identification of the pure offering with Christ.**

⭐ **STATED PRECISELY, BECAUSE THE PRECISION MATTERS AND THE OBVIOUS WRITE-UP WOULD HAVE BEEN WRONG: the transcript ALREADY carried the words.** `260835-1` quotes *"by the way, that pure offering is Jesus…"*. **This is a CONFIRMATION, not a discovery**, and an early draft of the inventory note that called it *"a structural datum the transcript did not surface"* was corrected before it shipped. ⚠️ **It is worth registering all the same: a two-word discourse marker is exactly the class of token ASR fabricates, relocates or drops, and an inference about a speaker's rhetorical posture is a bad thing to rest on an unheard one. It is now heard.**

⛔⛔ **THE PREFACE MARKS THE GLOSS AS HIS OWN INTERPOLATION RATHER THAN AS EXPOSITION OF THE TEXT — AND IT CUTS BOTH WAYS. Recorded both ways, because a note recording only one would be misleading.**

- ⭐ **STRENGTHENS it as evidence of his own view.** *"By the way"* is what a man says volunteering something he holds, unprompted, outside the flow of what he set out to cover. **Not a reading he is reporting; a reading he is supplying.**
- ⛔⛔ **WEAKENS any claim that he EXEGETES the verse this way.** An aside is not an argument. **Nothing may be built on his having DERIVED the christological reading from the text, ranked it against the alternatives, or noticed that it constrains his own use of the verse's incense clause. He has said what the pure offering is. He has not said what follows.**
- ⏳ **Force left OPEN, on the `IP-69` pattern. A later pass may not close it by treating the aside as exposition.**

⏳ **The corpus's other open ear-verification flags are UNAFFECTED. Three passages heard is three passages, not a class discharge.**

---

# 6. ⭐⭐⭐ ITEM 6 — THE `a105` SPEAKER WARRANT, AND THE FIREWALL THAT TRAVELS WITH IT

**`260834-9` recorded that `a105.md` contains NO internal speaker establishment whatsoever: zero name strings in 188,770 bytes, `>>` = 0, no self-introduction — and observed, correctly, that the Source ID Legend's `COT` = *"RJ (all)"* does not come from that file.** ⭐ **It recorded that `a105`'s attribution rests entirely on external evidence. The external evidence had never been stated.**

⭐⭐⭐ **IT IS NOW STATED, BY JD. Three legs, all external to the file:** **(a)** the file is titled ***"St Francis Christ in the OT Class"***; **(b)** **JD attended**; **(c)** **Rev. James taught every session as sole speaker.**

⭐ **Leg (c) is load-bearing, and it is exactly the class of evidence a transcript with no name strings cannot supply and an attendee can.** ⭐⭐ **DISPOSITION: `a105` (File 43) is ESTABLISHED as Rev. James throughout, on an EXTERNAL ATTRIBUTION WARRANT, recorded so downstream findings NAME it rather than inherit it silently.**

⚠️ **RECORDED AS WHAT IT IS — an attendee's testimony, not an on-tape self-identification. Stronger than the bare Legend row; weaker than a recorded self-introduction.**

⛔ **The `260834-9` no-speaker-establishment flag is RETAINED UNALTERED. It remains an exactly correct description of what the FILE contains — the file still carries zero name strings and `>>` = 0. What changed is that the warrant it deferred to has been supplied rather than assumed.**

**Findings updated off the Legend alone and now naming the warrant:** `IP-100`, `IP-101`, `IP-106`, `IP-107`, `IP-108`, and the `File 43` halves of `IP-104` and `IP-105`. **The §17 `260835-1` section heading's caveat — *"Attribution basis EXTERNAL throughout (`a105.md` establishes no speaker)"* — is retained unaltered with a dated note recording that the external warrant is now supplied.**

## 6.1 ⛔⛔⛔ THE NON-GENERALIZATION FIREWALL — WRITTEN INTO THREE PLACES, NOT ONE

**The brief is emphatic that this warrant must not be generalised. It is recorded with all three counterexamples in `SRC_Manifest.md`, in the `IP` block preamble, and in the §17 dated note — three places, so stripping any one does not lose it.**

- ⛔⛔ **`a103` recordings 4, 5 and 7 — GUEST LECTURES (Dr. Stephen Boyce, Kevin Valdez, Tyler West), 89,894 B, 34.7 % of the file. THE FIREWALL STAYS UP, UNCHANGED.** ⭐ **Same series shape — his class, his collect, his handoff — and another man's voice for the body of the segment. This is precisely why an attendee's *"he taught every session"* cannot be lifted from one series to another.**
- ⛔⛔ **`a101-2` recording 9 — the 38 UNLABELLED `>>` TURNS stay UNATTRIBUTABLE.** The class asks questions through the single most valuable segment in the scope set. ⛔ **Nothing in the warrant touches this, and it was NOT relaxed by this pass's video establishment of the same recording — two different questions, answered separately.**
- ⛔⛔ **The 2026-08-23 class had an UNNAMED SECOND CLERGYMAN.** ⭐ **Presence of a second cleric is not a hypothetical here; it is a recorded fact about a session already mined. Presence in the room is not sole-speakership, and `a105`'s warrant asserts sole-speakership only for `a105`.**

⛔ **NOTHING IS RETROACTIVE TO ANY OTHER FILE. No other file's attribution status is changed, relaxed or re-opened.** ⚠️ **The manifest note says in terms that a later pass reaching for this warrant to settle an attribution question elsewhere is misusing it — written so the misuse is visible rather than plausible.**

---

# 7. ⛔⛔ ITEM 7 — TWO VALIDATOR DEFECTS REGISTERED, NEITHER FIXED

⛔⛔⛔ **`validate_project.py` WAS NOT MODIFIED. It is registry-tracked at `260812-1` and editing it was not this pass's brief.** Both are now rows in `PROJECT_STATE.md` §7.

## 7.1 `C11`'s arithmetic keys off ledger heads only

**Mechanism, at source:** `C11` compares the outline's `CHECKED-AGAINST` pointer against `ledger_head_c11()`, which counts only `^\*\*(DQ|IP|RV)-N\.\*\*` entries. **A finding minted in any other form — a section bullet, a dated note — moves the corpus and cannot move the counter.**

**The demonstrated instance:** `260835-1` added eleven findings as bullets; **`C11` was byte-for-byte unchanged and reported *"5 finding(s) unreviewed"* when the true figure was 16.** ⚠️⚠️ **The outline became MORE out of date and the validator said otherwise.**

⭐⭐⭐ **ITEM 2 RESOLVES THE INSTANCE, NOT THE DEFECT** — and the brief says so itself. **The next un-numbered finding will be invisible in exactly the same way.** ⛔⛔ **The structural scope is much wider than the instance: the entire `AW-`/`COT-`/`A101-`/`ANF-`/`Misc-2025` half of the corpus uses session ids rather than numbered ledgers and is invisible to `C11` by construction.**

⏳ **A fix is OWED and is NOT a one-liner. It requires a decision about what counts as a *finding* for drift purposes — a convention question that belongs to JD, not to a validator patch.**

## 7.2 `C8`'s skip pattern is `next free` with a space

**Mechanism, at source:** `C8`'s `VP-` arm skips a `VP-N` token when its line matches `NEXT_FREE_MARK = re.compile(r'next free', re.I)` — **a space, no character class.** A registry line written *"next-free"* matches nothing and the token is scored as a **citation** of a pair that does not exist.

**The demonstrated instance:** `260835-1` §7.1 hit exactly this and took the validator to **1 ERROR mid-pass** on a `VP-8` token inside a hyphenated enumeration. ⭐ **That pass rephrased its own prose and correctly declined either to edit the validator or to invent a `VP` pair to satisfy the check.**

⚠️⚠️⚠️ **AND THE PART THAT MAKES IT A DEFECT AND NOT A ONE-OFF: `260834-9`'s registry line PASSES BY COINCIDENCE.** The same line happens to contain the unrelated string *"NEXT FREE FILE NUMBER IS NOW `File 47`"*. **It is not passing by construction, and a future edit to that line could break it without touching anything that looks load-bearing.**

⏳ **The fix is a one-character-class change (`next[- ]free`). OWED, deliberately not made.** ⚠️ **This pass observed the constraint rather than testing it: every new `PROJECT_STATE.md` line carrying a prefix token spells it unhyphenated.**

---

# 8. ⚠️ ITEM 8 — `x0hfBI6w6f0`: THE RECOMMENDATION

⛔⛔ **THE COLUMN IS NOT RESTRUCTURED AND THE CELL'S VALUE IS NOT CHANGED. A recommendation note was added to the row and nothing else.**

**The question.** The row's decision cell records a **not-to-be-ingested ruling** — an opening-statements-only partial (2,483 s) of the same debate `MLCh-d15F_o` (5,897 s) carries in full and which is registered as `File 46` recording 1. **Should the column carry a distinct value rather than folding this into `DECLINED`?**

⭐⭐ **RECOMMENDATION: YES — a distinct value, `SUPERSEDED — <superseding row> — <date>`.**

**The reason, and it is a real distinction rather than a tidiness preference.** Every other `DECLINED` row in the inventory is declined **on its subject**: `DECLINED — gaming`, `— politics`, `— scandal`, `— channel-admin`, `— ufo`, `— hell-annihilationism`. **The vocabulary is a taxonomy of *why this content is out of scope*.** ⛔⛔ **`x0hfBI6w6f0` is not out of scope at all. Its subject is registered material the project actively wants, already ingested from the other row.** The only reason to leave it out is **redundancy against a fuller capture** — which is not a scope judgment, it is a deduplication judgment, and the two answer different questions.

**Three concrete costs of folding it into `DECLINED`:**

1. **It becomes invisible to a scope audit.** A later pass sweeping declines to ask *"did we wrongly exclude anything on subject?"* would have to read this cell's prose to discover it was never a subject decline at all.
2. **It hides a live dependency.** This row's status is **contingent on `MLCh-d15F_o` staying ingested.** If that registration were ever withdrawn or found defective, `x0hfBI6w6f0` becomes a candidate again. **`DECLINED` records no such link; `SUPERSEDED — MLCh-d15F_o` does.**
3. **The same shape will recur.** Partial re-uploads, trimmed versions and highlight cuts are ordinary on this channel, and the corpus already tracks at least one other duplicate-event pair.

**The counter-argument, recorded because it is not negligible:** ⚠️ **a new column value is a schema change across a 400-row table, and the existing prose cell already records everything a reader needs — `260834-9` wrote it precisely so *"a later pass finds the decision rather than the video."*** ⭐ **On that view the cost of a new value exceeds the cost of prose, and the honest answer is that this is a judgment about how much the inventory should be machine-readable versus human-readable.**

⏳ **The decision is JD's. A scoped pass is OWED. Nothing was restructured.**

---

# 9. ⭐⭐ ITEM 9 — `RJ_Incense_Analysis.md` §4.14, THE FRANKINCENSE EXCLUSION

**Added as §4.14, immediately before §5.**

⛔⛔⛔ **CLASSIFIED FIRST AND EXPLICITLY, BECAUSE THE CLASSIFICATION GOVERNS EVERYTHING IN IT: THIS IS THE PROJECT'S OWN SCRIPTURAL RESEARCH. It is not `[Stated]`, not `[Analysis]` of anything he has said, and NOT a finding about Rev. James. He has never been recorded addressing Lev 5:11 or Num 5:15.** ⭐ **It takes no finding number and consumes none — finding ledgers attach to source utterances, and this is a Bible reference.**

**The datum:** **Lev 5:11**, the poor man's sin offering of fine flour — ***"he shall put no oil upon it, neither shall he put any frankincense thereon; for it is a sin offering."*** **Num 5:15**, the jealousy offering of barley meal — ***"he shall pour no oil upon it, nor put frankincense thereon; for it is an offering of jealousy, an offering of memorial, bringing iniquity to remembrance."***

⭐⭐ **What makes it worth having is structural, not proof-textual.** The ordinary *minchah* of Lev 2:1-2 carries oil **and** frankincense as standard. **These two are the exceptions, and in BOTH the reason given is the offering's own character** — *"for it is a sin offering"*, *"for it is an offering of jealousy."* ⭐ **So frankincense in the Levitical system is withheld where the occasion is sin or suspicion: a MARKED absence, not an unremarked one.**

⭐ **IT ALSO CLOSES §4.13's OPEN DISCREPANCY, IN THE DIRECTION §4.13 ITSELF NAMED.** `260833-2` was handed a premise about *"an existing corpus note that frankincense is excluded from the sin offering (Lev 5:11) and the jealousy offering (Num 5:15)"*, **searched for it, could not find it, and reported the absence rather than silently supplying the datum.** ⭐⭐ **That was exactly right on both counts: the note did not exist, and the underlying scriptural fact is true.** §4.13's own closing sentence — *"or supply it fresh as a §4.14"* — is the instruction this section follows. ⛔ **§4.13 is NOT edited and its discrepancy report stands as written.**

⛔⛔ **THREE LIMITS CARRIED WITH THE DATUM so a later pass does not oversell it:**

1. ⛔ **It is *lebonah*, not *qetoret*** — frankincense as a single substance on a grain offering, not the Exodus 30 compound of which it is one of four ingredients. **An argument sliding from one to the other is equivocating on the word and would be caught.**
2. ⛔⛔ **It does not touch the abrogation question at all.** These verses regulate frankincense **inside** the Levitical system. **Not a lever, not a rebuttal, not in §5 or §6.**
3. ⚠️⚠️ **Its one real use is defensive and small** — against a universal *"incense simply means prayer"* rule, including as `IP-107` records him teaching it. ⛔⛔⛔ **AND EVEN THAT IS NOT DEPLOYED, NOT DRAFTED AS A QUESTION AND NOT SEQUENCED, with the reason stated: his rule is a homiletical generalisation about a symbol, not a claim about Levitical exception clauses, and answering a generalisation with an edge case reads as pedantry rather than as argument.** ⭐ **Recorded so the option is visible and its weakness is visible with it.**

---

# 10. ✅ VALIDATOR AFTER, AGAINST BASELINE

```
BEFORE:  81 ok · 8 warnings · 0 errors
AFTER:   80 ok · 9 warnings · 0 errors
```

⭐⭐⭐ **ZERO ERRORS. And the one-for-one movement is exactly the intended one: an `ok` became a `WARN` because this pass made a real drift visible.**

**Every differing line, in full — there are no others:**

```
30c30
<   ok    [C2] IP-1..97 unbroken, no duplicates
>   ok    [C2] IP-1..108 unbroken, no duplicates

35,45  [C3] six registry stamps: 260835-2/260835-1/260834-1/260835-2/260834-9/260835-1 → 260835-3 (all six)

68c68
<   ok    [C10] §15 is within 2 finding(s) of the DQ ledger head (DQ-24)
>   ok    [C10] §15 is within 0 finding(s) of the DQ ledger head (DQ-24)

69c69
<   ok    [C10] §15 is within 0 finding(s) of the IP ledger head (IP-97)
>   ok    [C10] §15 is within 0 finding(s) of the IP ledger head (IP-108)

74d73
<   ok    [C11] IP current in the outline pointer (IP-97 @ 260833-5, ledger at IP-97)

89a89
>   WARN  [C11] outline last checked against IP-97 (260833-5); the IP ledger now runs to
                IP-108. 11 finding(s) unreviewed against the outline's logical flow.
```

## 10.1 ⭐⭐⭐ `C11` NOW COUNTS THE ELEVEN — AND THAT IS A RESULT, NOT A REGRESSION

**The brief predicted it and it happened exactly.** `C11` moves from `ok` to `WARN` and reports **eleven `IP` findings unreviewed**. ⭐⭐⭐ **The drift was always there. Two passes recorded that the validator could not see it. It can now.**

⛔⛔ **THE OUTLINE'S `CHECKED-AGAINST` POINTER WAS NOT ADVANCED TO SUPPRESS THIS.** No IP-arm outline review was performed this pass, and claiming one would be false. ⏳ **The `C11` IP-arm review is OWED and is a separate pass** — one which should read `IP-98`, `IP-101` and `IP-106` first, since those three bear hardest on the argument.

## 10.2 ⚠️⚠️ ONE SIDE EFFECT THIS PASS CAUSED, REPORTED RATHER THAN ENJOYED

**`C10`'s `DQ` lag improved from *"within 2"* to *"within 0"* and NO `DQ` FINDING WAS SWEPT, CREDITED OR RE-EXAMINED.**

**Cause, diagnosed at source:** `C10` uses `maxnum(body15, prefix)` — **the highest tag MENTIONED anywhere in §15, credited or declined.** The new §15 declines cite `DQ-24`(b) and `DQ-8` by name, so the counter moved.

⛔⛔ **THE IMPROVED `DQ` FIGURE IS AN ARTEFACT OF A CROSS-REFERENCE AND MUST NOT BE READ AS §15 HAVING CAUGHT UP ON THE `DQ` LEDGER.** ⭐ **Recorded in §15 itself, beside the number, so a reader meets the caveat where they meet the figure.** ⚠️ **Same defect family as §7.1's `C11` item — a counter that measures mentions rather than decisions.** ⛔ **Not fixed; `validate_project.py` is not this pass's to edit.**

⭐ **The same reasoning is why §15's own `IP` lag note says in terms that *"within 0 of IP-108"* means one credit and ten declines, not eleven findings folded in.**

---

# 11. `git status --short`, IN FULL

```
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

⚠️ **Plus, on the LOCKING invocation only:** `warning: unable to unlink '.git/index.lock': Operation not permitted` — **see §0.2. The warning is a property of this repo's mount, not a property of this pass's state.**

**Line by line, with what it is:**

| Line | What changed |
|---|---|
| `M Incense_Conversational_Outline.md` | **Item 1** — the spoken-core clause (JD's text), the `260835-3` note beside the retained `260835-2` note, stamp bump, changelog entry. ⛔ **`CHECKED-AGAINST` untouched.** |
| `M PROJECT_STATE.md` | Gate + pass note, six registry stamp bumps, **three new §7 defect rows** (item 7 ×2 + the `IP-98` byte-range discrepancy), next-free `IP` → `IP-109` with a dated note beside the retained `260833-4` note. |
| `M RJ_Incense_Analysis.md` | **Items 4 and 9** — two dated year corrections beside retained originals; **new §4.14**; stamp bump; changelog entry. ⛔⛔ **§4.6/§4.8/§4.10 not in the diff.** |
| `M SRC_Channel_Inventory.md` | **Items 5 and 8** — four decision cells EXTENDED (`C2tCMfq-_hI` → `INGESTED`, `R-GHhWcuH78`, `ZTs6Ru9ZdnI`, `x0hfBI6w6f0` recommendation-note-only), header stamp bump. ⛔ **No cell overwritten; column not restructured.** |
| `M SRC_Manifest.md` | **Items 5 and 6** — the `a105` external attribution warrant + firewall, the `Recon-Euch` discharge note, a new ear-verification block, two session-row markers, one standalone-row cell extension, stamp + header pass note. |
| `M St_Francis_EMC_Distinctives.md` | **Items 2 and 3** — the `IP-98`…`IP-108` ledger block, the §15 common-ground block, the byte-range discrepancy sub-block, `IP-90`'s dated correction, bullet→number notes at §13 and §17, stamp + header note + changelog entry. |
| `?? passes/…diff` | The full diff as applied (336 KB — see §12). |
| `?? passes/…close-out.md` | This file. |
| `?? passes/…raw-session-output.md` | Raw command output. |

## What to stage

⭐ **Stage all nine paths, as one commit:**

```
git add Incense_Conversational_Outline.md PROJECT_STATE.md RJ_Incense_Analysis.md \
        SRC_Channel_Inventory.md SRC_Manifest.md St_Francis_EMC_Distinctives.md \
        passes/260835-3_small-items-pass.diff \
        passes/260835-3_small-items-pass_close-out.md \
        passes/260835-3_small-items-pass_raw-session-output.md
```

**Suggested message:** `260835-3: mint IP-98..IP-108; a105 speaker warrant; 3 ear verifications; spoken-core clause (JD's ruling); IP-90 + Rev-year corrections; §4.14; 2 validator defects registered`

⛔⛔ **NOTHING WAS COMMITTED AND NOTHING WAS STAGED.** ⚠️ **`git add` will take `index.lock`; on this mount it will warn on unlink and leave the file behind, exactly as §0.2 describes. That is expected and is not a failure of the commit.**

---

# 12. ⚠️ THE DIFF EXCEEDS CHAT AND IS WRITTEN TO `passes/`

**`git --no-optional-locks diff` is 596 lines and 336,133 bytes** (≈ 82× the size of this close-out's own prose) — the file's lines are single paragraphs of several kilobytes each, so line count badly understates size. ⛔ **It is written in full to `passes/260835-3_small-items-pass.diff` rather than pasted.**

**Diffstat:**

```
 Incense_Conversational_Outline.md |  11 ++-
 PROJECT_STATE.md                  |  47 ++++++++--
 RJ_Incense_Analysis.md            |  39 +++++++-
 SRC_Channel_Inventory.md          |  10 +-
 SRC_Manifest.md                   |  46 +++++++++-
 St_Francis_EMC_Distinctives.md    | 188 +++++++++++++++++++++++++++++++++++++-
 6 files changed, 320 insertions(+), 21 deletions(-)
```

⭐⭐ **ALL 21 DELETIONS AUDITED INDIVIDUALLY AND EVERY ONE IS A LINE THIS PASS DELIBERATELY MODIFIED** *(the full list, truncated to 120 characters each, is at §9 of the raw-session-output artifact)*: **six `Last updated:` stamp lines** · **six `§4` registry rows**, each extended in place with the original text retained inside the new cell as *"Previously:"* · **the `Next free number by prefix:` line** · **the `x0hfBI6w6f0` inventory cell** · **the `C2tCMfq-_hI`, `R-GHhWcuH78` and `ZTs6Ru9ZdnI` inventory cells** · **the two `SRC_Manifest.md` session rows and the `Recon-Euch` standalone row** · **and the spoken-core paragraph — the pass's one intentional replacement of standing prose, on JD's ruling.**

⛔ **No unattributable hunk exists. This is the evidence base for the reconstructed clean-tree claim at §0.2.** ⚠️ **Note that *deletion* here almost always means *line rewritten with its original content preserved inside it* — the only true content replacement in the whole diff is the eleven-word clause in the spoken core.**

---

# 13. WHAT THIS PASS DID NOT DO, STATED EXPLICITLY

- ⛔⛔⛔ **`RJ_Incense_Analysis.md` §4.6, §4.8 and §4.10 — NOT TOUCHED.** Verified against the diff. Their falsified *"unknown"* premise stands standing and its rewrite is owed to a separate pass.
- ⛔ **Nothing drafted, altered or posted to Rev. James.** No question drafted, no message composed, no Discord state touched.
- ⛔ **`validate_project.py` NOT modified.** Both defects registered, neither fixed.
- ⛔ **The `.git/index.lock` NOT removed.** No `rm` attempted. Reported with a mechanism.
- ⛔ **The `SRC_Channel_Inventory.md` decision column NOT restructured.** Recommendation only.
- ⛔ **The outline's `CHECKED-AGAINST` pointer NOT advanced.**
- ⛔ **`On_Incense_and_the_Altar.md`, `RJ_Final_Question_List.md`, `RJ_Open_Questions_and_Divergences.md`, `ORCHESTRATION.md`, `passes/README.md`, `CLAUDE.md`, `asr_keyterms_A101.md`, `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` and every `src/` file — NOT TOUCHED.**
- ⛔ **No `DQ`, `RV`, `LS`, `BLOG`, `POD`, `VP`, `DELTA`, `EXT`, `W` or `File` number consumed.** Next free by prefix, unchanged except `IP`: `DQ-25`, **`IP-109`**, `LS-129`, `RV-64`, `BLOG-159`, `POD-17`, `File 47`.
- ⛔ **No source ingested, no capture re-hashed, no byte range altered, no existing finding renumbered or re-pointed.** `DQ-9` unmoved · `DQ-20`'s wording unedited · `DQ-24`(b) not amended, re-dated or merged · `IP-90`'s text unaltered (correction beside it) · `OQ8`, `OQ19`, `OQ20`, `OQ21` untouched.
- ⛔ **The `260835-1` §13/§17 bullets NOT deleted, trimmed or replaced.**
- ⛔ **`COT-n` NOT used as a locator anywhere.** Byte ranges only; the index defect stays open.
- ⛔ **No attribution firewall relaxed anywhere.** `a103` 4/5/7, `a101-2` rec 9's `>>` turns, and `a202`/`a201`/`a106` all stand as registered.
- ⛔ **`Rev`/`RV` citation tokens NOT renumbered, re-pointed or re-dated.**
- ⛔ **Nothing committed. Nothing staged.**

---

# 14. HAND-OFF — WHAT IS OWED

| Owed | To whom | Why now |
|---|---|---|
| ⏳⏳⏳ **The `C11` IP-arm outline review** | a scoped pass | Eleven findings are now visibly unreviewed. **Read `IP-98`, `IP-101` and `IP-106` first** — they bear hardest on the argument, and `IP-101`'s warrant is one no step of the outline meets. |
| ⏳⏳⏳ **`RJ_Incense_Analysis.md` §4.6/§4.8/§4.10 rewrite** | a scoped pass | Third consecutive pass reporting a falsified premise and declining to rewrite it. `IP-98` now carries the falsification with a ledger number. |
| ⏳⏳ **The Malachi *minchah* ↔ Levitical grain offering connection** | **JD** | The project's inference, hedged deliberately. **A candidate to put to him directly.** Not drafted. |
| ⏳⏳ **`x0hfBI6w6f0` — `SUPERSEDED` column value** | **JD** | Recommendation and counter-argument both recorded at §8. Schema change; his call. |
| ⏳ **The two validator defects** | **JD** (7.1) / a pass (7.2) | 7.1 needs a convention decision about what counts as a finding; 7.2 is a one-character-class change. |
| ⏳ **The `IP-98` byte-range discrepancy** | any pass with `a101-2.md` open | A read at two offsets. One minute. |
| ⏳ **Date-arithmetic sweep of `IP-84`…`IP-97`** | a pass | `IP-90`'s slip was found by accident, not by a check. |
| ⏳ **The `.git` lock operational rule** | **JD** / `ORCHESTRATION.md` | If §0.2's diagnosis holds, the standing instruction should become *"use `git --no-optional-locks` for reads"*, and the fix is at the mount. **`ORCHESTRATION.md` not touched.** |

*(This note makes no claim about its own commit state.)*
