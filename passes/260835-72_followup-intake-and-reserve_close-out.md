# PASS 260835-72 — Followup-thread intake, reserve register, and status reconcile — CLOSE-OUT

**Stamp `260835-72`, ASSIGNED BY BRIEF, NOT DERIVED.** Run 2026-10-09, fresh Cowork desktop thread, "On your computer" mode, folder `~/EMC` attached. Model: this session reports `claude-fable-5-1` (the brief asked for Opus; the serving model may differ from the configured identifier and is recorded here rather than assumed).

**Nothing committed. Nothing `git add`ed. Nothing posted to Rev. James. The raw file `src/SRC_Discord_Followup-raw.txt` was not touched (sha256 unchanged before and after: `48bb0a586b7d69d3f053a840f0d7fb59d3f5b5fe15f5cb41e66bafd300d0d528`).**

Return items per the HANDOFF: (a) the complete `git diff` is at `~/EMC/staging-72/260835-72.diff` (628 lines) and is pasted back in the thread; (b) this file is the complete raw close-out.

---

## 0. Gate checks

### 0.1 Repo state (verbatim)

```
$ git -C ~/EMC/theology rev-parse HEAD
38016602760b004a47fb678e30a931e03d26c4f2
$ git -C ~/EMC/theology status --short
(empty — no output, exit 0)
```

Recent log: `3801660 Adding Cyril primary source` · `f69fbd4 JD reply 10 9` · `d410db3 rj 10 8 reply` · `0cb2d3a rj 10 7 reply` · `67b5508 RJ latest`. **HEAD is a descendant of the expected `d410db3`** (two commits later). Working tree clean. **No `.git/*.lock` present; the lock-hygiene rule was not needed.**

### 0.2 Validator baseline (full output below, §7.1): `104 ok · 9 warnings · 0 errors`

Every check code with its full title name: `C0 - registry resolution` · `C1 - relative timestamps in archives` · `C2 - source-tag numbering` · `C3 - version stamps vs registry` · `C4 - stale answered-question status` · `C5 - volatile-state duplication` · `C6 - archive hash integrity` · `C7 - relay-clean firewall (WARN-only, suspended)` · `C8 - dangling question-ID cross-references` · `C9 - do-not-deploy consistency` · `C10 - section 15 staleness` · `C11 - outline-vs-findings drift` · `C12 - session-registry integrity / dual capture`.

Baseline warnings (9): `C1 - relative timestamps in archives` ×1 (RPW.md, 4 relative timestamps outside headers) · `C4 - stale answered-question status` ×1 (distinctives, 2 passages) · `C5 - volatile-state duplication` ×3 (question list 17; RJ_Incense_Analysis 9; distinctives 7) · `C10 - section 15 staleness` ×2 (IP 7 behind; LS 21 behind) · `C11 - outline-vs-findings drift` ×2 (DQ: 2 unreviewed; IP: 17 unreviewed).

⚠️ `~/EMC/staging-72/validator_before.txt` (17,653 B, 19:05, before this thread opened) already existed in the folder; left in place, not used. This pass's own baseline is `260835-72_validator_baseline.txt`.

---

## 1. Task 0 — Orphaned pass outputs (report only; nothing applied)

### `~/EMC/staging-69/` (6 entries, all 2026-09-08)
| File | Size | mtime | Repo comparison |
|---|---|---|---|
| `Church_Of_Ireland_Incense_Prohibition.md` | 31,059 | 2026-09-08 04:17 | **IDENTICAL** to `theology/Church_Of_Ireland_Incense_Prohibition.md` (committed `0883e4f` "260835-69: the Church of Ireland prohibition on incense") |
| `SRC_PRIMARY_1800-1869_UnionWithIreland-Act-Art-5_and_Irish-Church-Act-1869_ss1-2-19-20-21.txt` | 11,421 | 04:14 | IDENTICAL to `theology/src/…` |
| `SRC_PRIMARY_1878_ChurchOfIreland_BCP-Volume_Constitutions-and-Canons-Ecclesiastical_Canons-33-40-48_pdf-pp495-504.txt` | 23,886 | 04:06 | IDENTICAL to `theology/src/…` |
| `SRC_PRIMARY_2026_ChurchOfIreland_Constitution-Chapter-IX_Canons-2-5-12-13-38-43_Current-Text.txt` | 13,477 | 04:13 | IDENTICAL to `theology/src/…` |
| `SRC_SECONDARY_2022_Ford_Church-of-Ireland-Ritual-Canons-1871-1974_ChurchHistory.txt` | 15,064 | 04:15 | IDENTICAL to `theology/src/…` |

No close-out, report, `.diff` or `.patch` file present. **So `260835-69`'s outputs ARE in the repo (committed by JD at `0883e4f`) but the registry stops at `260835-68`: `Church_Of_Ireland_Incense_Prohibition.md` has no `PROJECT_STATE.md` §4 row and the four `src/` captures have no `SRC_Manifest.md` row. Registration debt, reported; not discharged by this pass (out of brief).**

First 20 lines of `Church_Of_Ireland_Incense_Prohibition.md` (the report file):
```
# The Church of Ireland prohibition on incense

**PASS 260835-69. STAMP ASSIGNED, NOT DERIVED.**
**READ-ONLY PASS. Nothing in `~/EMC/theology` was created, edited, moved or deleted.
No git write command was run. No file was committed.**
**All output is in `~/EMC/staging-69` at top level.**

---

## HEADLINE

**The prohibition exists, and it is not in the Prayer Book.** It is **Canon 38,
"Of Incense," of the Constitutions and Canons Ecclesiastical of the Church of
Ireland**, agreed by the General Synod (the volume's heading says "at General
Synods held in Dublin in the years of our Lord 1871 and 1877"), **printed as an
appendix inside the 1878 Prayer Book volume but not listed in that volume's own
"Contents of this Book"** — and it stands today, word for word unchanged, as
**Canon 40, "Use of incense forbidden," of Chapter IX of the Church of Ireland
Constitution.**
```

### `~/EMC/staging-70/` (8 entries, all 2026-09-08)
| File | Size | mtime | Repo comparison |
|---|---|---|---|
| `Orthodox_Malachi_1_11_And_Incense_Warrant.md` | 28,189 | 06:25 | **NOT IN REPO** |
| `SRC_PRIMARY_0743_John-of-Damascus_Exposition-Orthodox-Faith-IV-13_Malachi-1-11_NPNF2-09-Salmond.txt` | 1,993 | 06:11 | NOT IN REPO |
| `SRC_PRIMARY_0787_Second-Council-of-Nicaea_Definition_Incense-and-Lights_NPNF2-14-Percival.txt` | 3,371 | 06:22 | NOT IN REPO |
| `SRC_PRIMARY_1899_Sokolof_Manual-Orthodox-Church-Divine-Services_Incense-And-Censer.txt` | 2,831 | 06:22 | NOT IN REPO |
| `SRC_PRIMARY_2004_Theodore-of-Mopsuestia_Commentary-Twelve-Prophets_Malachi-1-11_FOTC108-Hill.txt` | 3,873 | 06:11 | NOT IN REPO |
| `SRC_PRIMARY_2008_Orthodox-Study-Bible_Notes-Mal-1-11_Ps-140-141_Sirach-39-14_Lev-2_Num-17.txt` | 5,013 | 06:22 | NOT IN REPO |
| `SRC_PRIMARY_2012_Cyril-of-Alexandria_Commentary-Twelve-Prophets-vol3_Malachi-1-11_FOTC124-Hill.txt` | 4,217 | 06:10 | NOT IN REPO — ⚠️ **an earlier Cyril capture from the same translation; NOT the file registered this pass (`SRC_PRIMARY_0430_…`, 11,674 B). JD should decide whether this one is superseded by the page-verified capture or kept beside it.** |
| `SRC_SECONDARY_2026_Orthodox-Popular-Apologetics_Incense-Warrant_Peck-OrthodoxAnswers-StMichael.txt` | 5,617 | 06:23 | NOT IN REPO |

No close-out, `.diff` or `.patch` present. First 20 lines of `Orthodox_Malachi_1_11_And_Incense_Warrant.md`:
```
# Eastern Orthodox reading of Malachi 1:11, and the Orthodox warrant for liturgical incense

**Stamp: 260835-70.** ⛔ **ASSIGNED BY BRIEF, NOT DERIVED.** No stamp was derived
and the stamp registry was not read to confirm it, per the brief's instruction.

⛔⛔ **READ-ONLY PASS. `~/EMC/theology` WAS NOT WRITTEN TO.** No file in the
repository was created, edited, moved, renamed or deleted; no git command of any
kind was run, read or write. All output is in `~/EMC/staging-70`. Nothing was
copied into the repository and nothing was committed.

⛔ **NOTHING MINTED.** No `IP`, `DQ`, `GV`, `RC`, `BP`, `RV`, `EXT` or any other
ledger number consumed. No existing document altered.

⛔⛔⛔ **NOTHING WAS TRANSLATED BY THIS PASS.** Every English rendering below is
an existing published translation, named with its translator. Where no published
English translation could be reached, the entry is **UNMATCHED** and says so.

**Attribution layers:** `[Stated]` = verbatim from a capture file;
`[Stated-Analysis]` = labelled inference from something stated;
`[Analysis]` = this project's own argument.
```

### `~/EMC/staging-71/`: **does not exist.** No other `staging-NN` with `NN > 68` besides `staging-72` (this pass; held `validator_before.txt` at open).

### `git apply --check`: **not run — no `.diff`/`.patch` exists in either folder.**

### `~/EMC/theology/handout/`: **does not exist.** `RPW_Primer_Questions.md`: **not found anywhere under `~/EMC`** (`find ~/EMC -name RPW_Primer_Questions.md` → no result).

---

## 2. Source read, orientation, and dating

- Orientation confirmed on the first post before reading: `JD Smith` / `OP` / ` — 9/5/26, 9:55 AM`, then JD's text; every later post read header-then-text. Rev. James's headers are single-line (`Athanasius325 / Fr James — <time>`); JD's are three-line.
- 29 headers: JD 15, Rev. James 14. Header counts are a lower bound on messages (the client merges consecutive same-poster messages).
- Dating re-derived from git: 9/5–10/7 headers render as full dates; the 10/7 header was bare at `0cb2d3a` (10/7), `Yesterday at 1:43 PM` at `d410db3` (10/8), `10/7/26, 1:43 PM` at `f69fbd4`; the 10/8 headers were bare at `d410db3` and `Yesterday at` at `f69fbd4` → 2026-10-08; bare `3:08 PM`/`3:23 PM` → 2026-10-09 (recapture committed 15:32:09 ET that day).
- ⚠️ **Brief deviation recorded:** the committed diff `d410db3`→`f69fbd4` shows NO whitespace change inside the 2:18 PM body (only the end-of-file newline). The brief's "(edited) marker / single added blank line" is recorded in `SRC_Manifest.md` as JD's report, not as reproducible from git.

---

## 3. Findings minted — `DQ-29`…`DQ-37` (next free `DQ-38`), plus `JD-RECORD` (no number)

Ledger "next free" note confirmed as `DQ-29` before minting (`St_Francis_EMC_Distinctives.md` L14; `PROJECT_STATE.md` §5; `DQ-28-P` note). No discrepancy.

| # | Date / message | Headline | Key byte offsets (0-based, end-exclusive, whole file) |
|---|---|---|---|
| DQ-29 | 9/5 3:01, 3:10, 6:34, 6:50 PM | 1000's-of-years frame; DeKoven and Canon 20 Title I; the two-argument frame; DeKoven on Mal 1:11; 1899 "far, far from a complete rejection" | @2,308–2,470 · @2,686–2,757 · @2,974–3,094 · @4,007–4,057 · @4,805–4,898 · @5,125–5,153 · @5,300–5,569 · @5,788–5,859 · @5,894–5,959 · @5,962–6,064 · @6,067–6,124 · @6,127–6,217 · @6,282–6,421 · @7,515–7,684 |
| DQ-30 | 9/11 9:50 PM | His RPW definition; principles as fundamental truths; vestments; "Regulative Examples of Worship" | @22,521–22,656 · @22,764–22,912 · @22,943–23,043 · @23,067–23,190 · @23,192–23,268 · @23,392–23,763 · @23,766–24,018 |
| DQ-31 | 9/11 10:13 PM | Hanukkah trilemma; synagogue argument reaches incense "in principle" | @24,378–24,501 · @24,686–25,034 · @25,224–25,369 |
| DQ-32 | 9/11 6:51 PM; 9/12 2:14 AM | Lower-tier allowances; hierarchy all "Yes"; UECNA/Robinson (hearsay, guarded) | @20,881–21,062 · @21,494–21,696 · @21,961–22,055 · @22,135–22,322 · @25,536–25,650 · @25,876–25,907 · @25,908–25,987 · @25,988–26,145 · @26,146–26,257 · @26,258–26,295 · @26,298–26,548 |
| DQ-33 | 9/18 2:23 PM | 1500-years weighting; "you hold the burden in demonstrating it is, in point of fact, sinful" | @41,819–41,915 · @42,300–42,388 · @42,389–42,502 · @42,503–42,677 · @42,680–42,931 (his own 9/28 re-quote at @61,676–61,927) |
| DQ-34 | 9/28 5:20, 5:32 PM | Two misreading corrections; "allows for a (proper, logically consistent) Regulative Principle" | @60,128–60,268 · @60,291–60,413 · @60,638–60,901 · @61,446–61,599 · @61,985–62,016 · @62,211–62,292 · @62,295–62,380 |
| DQ-35 | 10/4 12:42 AM | The clarification: proof that JD's interpretation of the RPW is biblical | @63,185–63,463 · @63,466–63,676 |
| DQ-36 | 10/7 1:43 PM | "Your application of the RPW is inconsistent with Scripture"; two passages; non-Aaronic offerers | @68,601–68,712 · @68,755–68,871 · @68,941–69,062 · @69,080–69,425 |
| DQ-37 | 10/8 2:18 PM | The fulfillment dilemma; restrictions fall, rite widens; circumcision and showbread; "prophecy of incense and a Grain Sacrifice"; "strong case to deny the literal meaning"; `[Analysis]` pattern-(ii)-not-(iii) note | @76,855–76,957 · @76,978–77,227 · @77,231–77,528 · @77,530–77,659 · @77,660–77,840 · @77,841–78,048 · @78,049–78,242 |
| JD-RECORD | 9/8, 9/17, 9/27, 9/28, 10/4, 10/8, 10/9 | JD's own positions, byte-verified, no number consumed | see §3.1 |

### 3.1 Full offset tables (output of `offsets.py`; `FATAL … 2 matches` lines are the known duplicates — `q33a`/`q33b` re-quoted by Rev. James on 9/28 (resolved by position, both occurrences recorded above) and `jd0905` re-quoted by him on 9/5 (not cited))

```
q29a	@2,308–2,470	162B
q29b	@2,686–2,757	71B
q29c	@2,974–3,094	120B
q29d	@4,007–4,057	50B
q29e	@4,805–4,898	93B
q29f	@5,300–5,569	269B
q29g	@5,788–5,859	71B
q29h1	@5,894–5,959	65B
q29h2	@5,962–6,064	102B
q29h3	@6,067–6,124	57B
q29h4	@6,127–6,217	90B
q29i	@6,282–6,421	139B
q29j	@7,515–7,684	169B
q29k	@5,125–5,153	28B
q30a	@23,067–23,190	123B
q30b	@23,192–23,268	76B
q30c	@23,392–23,763	371B
q30d	@23,766–24,018	252B
q30e	@22,521–22,656	135B
q30f	@22,764–22,912	148B
q30g	@22,943–23,043	100B
q31a	@24,686–25,034	348B
q31b	@25,224–25,369	145B
q31c	@24,378–24,501	123B
q32a	@21,494–21,696	202B
q32b	@22,135–22,322	187B
q32c	@25,536–25,650	114B
q32d	@21,961–22,055	94B
q32e1	@25,876–25,907	31B
q32e2	@25,908–25,987	79B
q32e3	@25,988–26,145	157B
q32e4	@26,146–26,257	111B
q32e5	@26,258–26,295	37B
q32f	@26,298–26,548	250B
q32g	@20,881–21,062	181B
FATAL q33a: 2 matches
FATAL q33b: 2 matches
q33c	@41,819–41,915	96B
q33d	@42,300–42,388	88B
q33e	@42,503–42,677	174B
q34a	@60,128–60,268	140B
q34b	@60,291–60,413	122B
q34c	@60,638–60,901	263B
q34d	@61,985–62,016	31B
q34e	@62,211–62,292	81B
q34f	@62,295–62,380	85B
q34g	@61,446–61,599	153B
q35a	@63,185–63,463	278B
q35b	@63,466–63,676	210B
q36a	@68,601–68,712	111B
q36b	@68,755–68,871	116B
q36c	@68,941–69,062	121B
q36d	@69,080–69,425	345B
q37a	@76,855–76,957	102B
q37b	@76,978–77,227	249B
q37c	@77,231–77,528	297B
q37d	@77,660–77,840	180B
q37e	@77,841–78,048	207B
q37f	@78,049–78,242	193B
q37g	@77,530–77,659	129B
hash-check-size 83190 bad 2

```
```
FATAL jd0905: 2 matches
jd0908fathers	@15,971–16,120	149B
jd0908cyril	@17,911–18,078	167B
jd0908lev10	@18,500–18,585	85B
jd0908warrant	@17,586–17,707	121B
jd0908q1	@19,543–19,744	201B
jd0908q2	@20,239–20,314	75B
jd0917sentence	@32,040–32,145	105B
jd0917acts	@41,168–41,254	86B
jd0917element	@36,620–36,716	96B
jd0917follow	@40,607–40,686	79B
jd0927burden	@45,097–45,186	89B
jd0927normative	@45,366–45,486	120B
jd0927q1	@55,236–55,391	155B
jd0927q2	@59,440–59,576	136B
jd0927optional	@55,999–56,097	98B
jd0927prescribed	@56,999–57,085	86B
jd0928sorry	@62,417–62,482	65B
jd1004notsame	@63,782–63,843	61B
jd1004prohibited	@67,535–67,638	103B
jd1004heb	@67,310–67,533	223B
jd1004stands	@67,734–67,879	145B
jd1004change	@67,968–68,066	98B
jd1008heb712	@70,566–70,787	221B
jd1008prophets	@71,610–71,907	297B
jd1008minchah	@72,358–72,573	215B
jd1008cyril	@72,575–72,759	184B
jd1008angel	@73,227–73,356	129B
jd1008v5	@73,684–73,789	105B
jd1008rev83	@74,035–74,149	114B
jd1008luke	@74,414–74,687	273B
jd1008wcf	@76,007–76,221	214B
jd1008q	@76,426–76,556	130B
jd1009yes	@78,271–78,360	89B
jd1009circ	@78,870–79,113	243B
jd1009bread	@79,277–79,361	84B
jd1009sign	@79,363–79,449	86B
jd1009arkveil	@79,721–79,941	220B
jd1009rev1119	@80,000–80,216	216B
jd1009rule	@80,371–80,492	121B
jd1009heb	@80,572–80,769	197B
jd1009lev2	@80,900–81,088	188B
jd1009rev58	@81,209–81,358	149B
jd1009irenaeus	@81,460–81,638	178B
jd1009cyril	@81,639–81,867	228B
jd1009luke	@81,937–82,157	220B
jd1009fulfil	@82,312–82,389	77B
jd1009q	@82,666–82,824	158B
jd1009notallegory	@81,133–81,208	75B
hash-check-size 83190 bad 1

```

### 3.2 Brief claims checked against the capture (grep, whole file)
| Brief claim | Result |
|---|---|
| Acts 15 / Gal 5:2 "cut from the 10/9 reply for length" (reserve item 6) | **FALSE — deployed 10/9** in one sentence, @78,870–79,113. Corrected in the outline's reserve register. |
| "instituted worship is required worship" deployed 10/9 (Step 2) | **NOT IN CAPTURE (0 hits).** Not recorded as deployed; nearest form is the 10/8 WCF paragraph @76,007–76,221. Noted at the outline Step 2 note and the JD-RECORD. |
| Perowne's symmetry canon "deployed 10/9" (reserve item 5) | **NOT IN CAPTURE (0 hits for "Perowne", "bread and wine").** Recorded as available, not deployed. |
| 10/9 reply is "three messages" | Capture shows TWO headers (3:08 PM, 3:23 PM); the 3:08 block has an internal message break. Recorded as header counts. |
| Mal 3:3-4, Isa 19, Jer 33 unspent | Confirmed (0, 0, 0). |
| Rev 11:19, Christ our Passover (once), Lev 24:7, Cyril, Irenaeus deployed as stated | Confirmed. |

---

## 4. Files touched, with the anchors used (all edits via `~/EMC/staging-72/edits/apply.py`: uniqueness pre-check on every anchor before any write; three small follow-up fixes used an inline `assert count==1`)

**`St_Francis_EMC_Distinctives.md`** — (1) insert `DQ-29`…`DQ-37` + `JD-RECORD` before anchor `---\n\n## Revelation Class Findings, 2026 (RV ledger)\n`; (2) changelog prepend at `## Changelog\n\n- **260835-68 (2026-09-07):**`; (3) stamp line prefix `**Last updated: 260835-68** (date-stamped, format yymmdd-iteration) ` → `260835-72` with the prior note retained. Follow-up fix: `DQ-29`(d) "exhaustive" wording replaced (anchor the sentence itself).

**`SRC_Manifest.md`** — (1) dated current-state note inserted between `the words are the Archbishops'.**` and the `SRC_Discord_39ArticlesFormularies.md` field table; (2) dated note after the `DQ-Thread-Followup` alias row (anchor: the row's tail `… until \`src/SRC_Discord_Followup.md\` is built** |\n`); (3) Cyril section inserted before `---\n\n# Dual-Capture Reconciliation Procedure (added 260725-4, batch 260725-3)`; (4) stamp line.

**`SRC_Coverage_Register.md`** — (1) §6 dated update inserted before `\n\n**Standing capture limitation, stated once here rather than per-thread:**`; (2) changelog `v1.6` prepended at `## Changelog\n\n- **v1.5 — 260835-58.**`; (3) stamp line.

**`SRC_Channel_Inventory.md`** — (1) third non-application dated note inserted before `> ⭐⭐ **DATED NOTE, 260835-42 (2026-08-31)`; (2) stamp line. (Brief asked for a row; `260835-58` precedent followed — a Discord thread has no video ID; the row went to the coverage register.)

**`PROJECT_STATE.md`** (17 edits) — stamp L3; GATE (260835-72) block before `> ✅ **GATE (260835-58) — REGISTRY-MAINTENANCE PASS.`; §1 Followup row before `| **Discord — 39 Articles / Formularies** | ✅ Closed by JD |`; §1 cell-correction note before `\n### Monitored sources — no turn state, no action owed`; §2 dated note before the gate table (`| Gate | State | Closed by | Date |…| **Definitional gate**`); §3 two OPEN rows before `| — | **ASSURANCE: NOTHING POSTED-AWAITING.**`; §3 ANSWERED-BY-JD row before `| **DQ-19** ⭐⭐⭐ | ✅ **Answered 2026-08-21`; do-not-deploy two entries before `---\n\n## 4. DOCUMENT REGISTRY`; §4 rows bumped by anchor `| \`<file>\` | <old stamp> | ` for PROJECT_STATE.md, St_Francis_EMC_Distinctives.md, Incense_Conversational_Outline.md, SRC_Manifest.md, SRC_Channel_Inventory.md, SRC_Coverage_Register.md, CLAUDE.md, and the full `RJ_Final_Question_List.md` row; §5 `**Next free number by prefix:** **\`DQ-29\`** ` → `DQ-38` with prior text retained. Follow-up fix: the Rev 8:3 do-not-deploy gloss trimmed to the brief's stated reason.

**`Incense_Conversational_Outline.md`** (7 edits) — dated block after `⛔⛔ **NOTHING IN THIS SECTION IS A PLAN, … writes no part of his next turn.**\n`; Step 3(c) note before `> ⛔⛔⛔ **UPDATE (260835-31) — THE FORK IS NOT EXHAUSTIVE AGAINST HIM…`; Step 6 note before `\n### Step 7\\. The heaven's liturgy objection\n`; Step 2 note before `\n### Step 2b\\. The principle-level warrant objection\n`; Step 5c note before `\n### Step 5d\\. The overlap period (AD 30-70)\n`; changelog prepend at `## Changelog\n\n- **260835-65 (2026-09-07):**`; stamp line. `CHECKED-AGAINST` NOT moved.

**`RJ_Final_Question_List.md`** (4 edits) — v23 dated block replacing/preceding `### ★★ ✅ ANSWERED — DQ-15, the grounding question in genre form`; item 1e note before `---  \n \n### 1a. Which Homilies do you take exception to? …`; stamp `**Last updated: 260835-16 (v22)** …` → `260835-72 (v23)`; changelog prepend at `# CHANGELOG (permanent — never deleted)  \n\n260835-16 (v22):`. Follow-up fix: one inference ("pre-empted") reworded at the 1e note.

**`CLAUDE.md`** (2 edits) — one bullet after `- Verbatim quotes are byte-offset verified before being logged or deployed.`; stamp `**Last updated: 260728-2**` → `260835-72`.

Not touched: `src/SRC_Discord_Followup-raw.txt`, `src/SRC_PRIMARY_0430_…` (registered only), `validate_project.py`, `RJ_Incense_Analysis.md`, everything else.

```
 CLAUDE.md                         |   6 +-
 Incense_Conversational_Outline.md |  55 ++++++++++++-
 PROJECT_STATE.md                  |  39 ++++++---
 RJ_Final_Question_List.md         |  24 +++++-
 SRC_Channel_Inventory.md          |   4 +-
 SRC_Coverage_Register.md          |  12 ++-
 SRC_Manifest.md                   |  37 ++++++++-
 St_Francis_EMC_Distinctives.md    | 168 +++++++++++++++++++++++++++++++++++++-
 8 files changed, 326 insertions(+), 19 deletions(-)
```

---

## 5. Judgment calls and deviations (read these)

1. **Minting from the raw.** `SRC_Manifest.md` (`260835-58`) said no `DQ` may be minted until an archive of record exists; the brief directed byte-verified minting from the raw. The brief was followed; the supersession is recorded as a dated note and the archive (`src/SRC_Discord_Followup.md`) is logged as OWED. `C1`/`C6` still cannot see this thread.
2. **Channel inventory**: no row (schema mismatch), per the `260835-58` ruling; dated non-application note instead; row in the coverage register.
3. **Question list**: the Followup questions were never items in this file, so they are recorded in a dated block in the live-status section rather than as new numbered items; "instituted new covenant form" is not a verbatim item and was marked superseded at its nearest forms (item 1e).
4. **Priority channel**: the RPW row's DO NOT POST is recorded as superseded (dated note), not edited; the new Followup row itself carries DO NOT POST for a different reason (two of JD's questions open).
5. **Attribution**: every `[Stated]` is Rev. James verbatim; JD's words live in the `JD-RECORD`, `PROJECT_STATE.md` §3 rows and outline notes, always named as JD's; the pattern-(ii)/(iii) mismatch is labelled `[Analysis]` everywhere it appears.
6. **Validator movement** (§7.3): `C10 - section 15 staleness` DQ arm ok→WARN (gap 0→9), not swept (do-not-sweep-to-suppress); `C11 - outline-vs-findings drift` DQ count 2→11, review deferred on the `260835-27` ruling.

## 6. Not done / owed
- `src/SRC_Discord_Followup.md` archive of record (owed since `260835-58`; now more urgent since nine findings cite the raw).
- Registration of `260835-69`'s committed outputs (`Church_Of_Ireland_Incense_Prohibition.md` §4 row; four `src/` manifest rows) and a decision on `staging-70`'s eight uncommitted files (incl. the older Cyril capture).
- `C11` outline review against `DQ-27`…`DQ-37` (deferred by ruling). §15 sweep for `DQ-29`…`DQ-37` (judgment call, not run).
- Eusebius DE 1.10 unread (reserve item 9). Perowne and Simeon wording unverified against editions (items 5, 7).

---

## 7. Validator runs, quoted in full

### 7.1 BEFORE (baseline)
```
========================================================================
PROJECT INTEGRITY VALIDATION   root: /sessions/rcw-01rda833wofmcpjygrficj23/mnt/EMC/theology
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
  ok    [C2] DQ-1..28 unbroken, no duplicates
  ok    [C2] IP-1..125 unbroken, no duplicates
  ok    [C2] RV-1..63 unbroken, no duplicates
  ok    [C2] LS-1..141 unbroken, no duplicates
  ok    [C2] BLOG-1..158 unbroken, no duplicates
  ok    [C2] POD-1..16 unbroken, no duplicates
  ok    [C3] PROJECT_STATE.md: version agrees with registry (260835-68)
  ok    [C3] ORCHESTRATION.md: version agrees with registry (260835-37)
  ok    [C3] passes/README.md: version agrees with registry (260832-3)
  ok    [C3] St_Francis_EMC_Distinctives.md: version agrees with registry (260835-68)
  ok    [C3] RJ_Final_Question_List.md: version agrees with registry (260835-16 (v22))
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
  ok    [C3] Incense_Conversational_Outline.md: version agrees with registry (260835-65)
  ok    [C3] SRC_Manifest.md: version agrees with registry (260835-68)
  ok    [C3] SRC_Channel_Inventory.md: version agrees with registry (260835-58)
  ok    [C3] SRC_Coverage_Register.md: version agrees with registry (260835-58)
  ok    [C3] asr_keyterms_A101.md: version agrees with registry (260830-2)
  ok    [C3] README.md: version agrees with registry (260835-8)
  ok    [C3] Project_Bootstrap_Prompt.md: version agrees with registry (260816-1)
  ok    [C3] tools/transcribe_yt.py: version agrees with registry (260833-7)
  ok    [C3] validate_project.py: version agrees with registry (260835-39)
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
  ok    [C10] §15 is within 0 finding(s) of the DQ ledger head (DQ-28)
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
  WARN  [C10] §15's newest IP citation is 7 findings behind the ledger (IP-118 vs IP-125). Sweep the interval for creditable material.
  WARN  [C10] §15's newest LS citation is 21 findings behind the ledger (LS-120 vs LS-141). Sweep the interval for creditable material.
  WARN  [C11] outline last checked against DQ-26 (260835-31); the DQ ledger now runs to DQ-28. 2 finding(s) unreviewed against the outline's logical flow. REPORT drift; do not rewrite JD's reasoning without asking.
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
104 ok · 9 warnings · 0 errors
Read the coverage summary before trusting the error count.

```

### 7.2 AFTER
```
========================================================================
PROJECT INTEGRITY VALIDATION   root: /sessions/rcw-01rda833wofmcpjygrficj23/mnt/EMC/theology
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

### 7.3 Every change from the baseline, explained
- `C2 - source-tag numbering`: `DQ-1..28` → `DQ-1..37` unbroken (nine mints).
- `C3 - version stamps vs registry`: nine files report `260835-72` (`RJ_Final_Question_List.md` as `260835-72 (v23)`); all agree with the §4 registry. During the pass, `C3` ERRORs appeared transiently on files stamped before their registry rows were bumped and cleared once both sides matched.
- `C10 - section 15 staleness`: the DQ arm moved from `ok … within 0` to `WARN … 9 findings behind (DQ-28 vs DQ-37)` — expected (threshold `> 4`); §15 deliberately NOT swept. `ok` count 104→103, warnings 9→10.
- `C11 - outline-vs-findings drift`: DQ arm count 2→11 (same WARN line, new figures). `CHECKED-AGAINST` not moved.
- All other lines identical, including `C5` counts (17 / 9 / 7 — no new volatile-state phrases introduced), `C4`, `C9`, `C12` (77 capture rows / 66 sessions unchanged — the new manifest tables did not pollute the session registry).
- Summary: `104 ok · 9 warnings · 0 errors` → `103 ok · 10 warnings · 0 errors`.
