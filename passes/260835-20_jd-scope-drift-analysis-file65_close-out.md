# 260835-20 — JD's scope-drift / self-correction `[Analysis]` on `File 65`, recorded at the Analysis layer

**Delegated pass. Real repo pass. Analysis-layer entry minted. Nothing committed.**

---

## 1. Gate

| Item | Result |
|---|---|
| `git rev-parse HEAD` | **`3e0f1322eb4e097f4a4efb46b5ba20b695b960ec`** — matches briefed `3e0f132` exactly; branch `main` |
| `git status --short` before first edit | ⭐ **EMPTY**, captured directly and not reconstructed |
| Validator BEFORE | **`82 ok · 9 warnings · 0 errors`** |
| `PROJECT_STATE.md`'s own stamp at gate | **`260835-19`** |
| Next-free pass stamp | **`260835-20`** — re-derived fresh by grep, not carried from the brief |
| Next-free `LS` | **`LS-130`** — verified free, ⛔ **deliberately NOT consumed.** Next free remains `LS-130` |
| `File` number | none consumed, none needed |

### All nine firing codes at gate (verbatim)

```
WARN [C1]  src/SRC_Discord_RPW.md: 2 relative timestamp(s) outside message headers
WARN [C3]  Calvin_Luther_and_Anglican_Formularies_on_Iconography.md: no parseable 'Last updated' stamp; registry says '260832-2'
WARN [C3]  tools/transcribe_yt.py: no parseable 'Last updated' stamp; registry says '260833-7'
WARN [C4]  St_Francis_EMC_Distinctives.md: 2 passage(s) describe an ANSWERED question as pending
WARN [C5]  RJ_Final_Question_List.md: 17 volatile-state assertions
WARN [C5]  RJ_Incense_Analysis.md: 9 volatile-state assertions
WARN [C5]  St_Francis_EMC_Distinctives.md: 7 volatile-state assertions
WARN [C10] §15's newest LS citation is 9 findings behind the ledger (LS-120 vs LS-129)
WARN [C11] outline last checked against IP-97 (260833-5); the IP ledger now runs to IP-108. 11 finding(s) unreviewed
```

⭐⭐ **`[C10]`'s expectation CONFIRMED, not assumed.** The brief predicted the `LS` gap would have widened to **9** per `260835-19`. **It has** — `LS-120` vs ledger head `LS-129`. It read *"eight"* at every gate from `260835-15` through `260835-19`; `260835-19`'s minting of `LS-129` is what moved it. **The other eight codes are unchanged from the `260835-19` gate.**

### Stamp derivation (fresh, by grep)

Repo-wide content grep for `26[0-9]{4}-[0-9]+` tops out at **`260835-19`**, which is a **REAL consumed stamp**: committed artifacts `passes/260835-19_ls129-normative-self-identification-ear-verified{.diff,_close-out.md}` exist, and it is `PROJECT_STATE.md`'s own header stamp. `grep -rn "260835-20"` → **zero matches repo-wide.** `grep -rn "260836-"` → only quoted shell-command lines and absence-assertions inside earlier close-outs; **no live stamp.** → **This pass is `260835-20`.**

### `LS` derivation (fresh, independent)

Highest registered is **`LS-129`**. Every repo-wide `LS-130` occurrence was read in context — all are next-free registry assertions (`St_Francis_EMC_Distinctives.md` L16/L3011/L7387, `passes/260835-19_*`, `PROJECT_STATE.md` L5). The validator's `[C2]` arm independently reported **`LS-1..129` unbroken** at gate. **`LS-130` is free — and is NOT spent by this pass** (see §5).

---

## 2. Read first, as instructed

`LS-129`'s full entry (`St_Francis_EMC_Distinctives.md` §13) and its `260835-19` dated note were read before any edit, together with `RJ_Incense_Analysis.md` §12.2, `CLAUDE.md`'s three-layer rule, and the `File 65` registration row in `SRC_Manifest.md`. This pass sits beside `LS-129` — same source, same video, adjacent timestamp range — and does not duplicate, alter or re-point it.

---

## 3. ⭐⭐⭐ Placement — verified, not assumed. §12.2 was **declined on reasoning**

The brief asked whether the entry belonged as a dated note at `RJ_Incense_Analysis.md` §12.2 *"or elsewhere per existing convention — verify rather than assume."*

**Answer: elsewhere.** The substantive material is at **`St_Francis_EMC_Distinctives.md` §13**, with a **pointer-only** note left at §12.2.

**Why §12.2 is the wrong home.** Its deferred lever is a question about his **POSITION** — *"does he hold the RPW in any standard sense?"* This pass's material is about how he **CHARACTERIZES OTHERS' POSITIONS**, i.e. rhetorical **method**. Different propositions. ⛔ Filing method material inside a deferred position-lever would have invited exactly the trigger-firing the brief forbids.

**Why §13 is the right home — positive evidence, not residual.**

1. §13 already carries `[Analysis]` **"He refutes the *populist* RPW, not the confessional one"** — the same observation, **without the mechanism.** This entry supplies the mechanism and a dated instance.
2. §13 carries **`BP-52`'s `[Analysis — pattern note]`**, an **OPEN standing-pattern flag**: *"characterizing an opposing position via an unattributed 'what you're saying is' inference… **Worth tracking as a standing pattern across the corpus, not a one-off.**"* This entry answers that open flag.
3. §13 is where the `260835-19` `LS-129` note and the whole Everhard `BP-50…BP-60` block already live — JD's own second instance.
4. The owner-attributed-analysis convention is established there: `BP-54`'s **`[Analysis — the equivocation, JD-identified]`**.

**What was still added at §12.2** — a pointer-only dated note, because one genuinely new §12.2-relevant datum exists: in 2020 he does not merely *use a different label* (which is all `260835-19`'s §12.2 note claims); **he rejects the regulative principle explicitly and by name.** That sharpens `260835-19`'s note without altering one word of it. ⛔ **The trigger is still NOT fired** — see §6.

---

## 4. Verification of every quotation

⭐ **`File 65`'s registered `sha256` `a7dfa485321815dc74882480c720cc513182c0f88c6e68b0cd97406759c1e18c`, 24,156 B — recomputed from disk this pass and MATCHES `SRC_Manifest.md`.**

⭐ **Every byte range and timestamp below was computed programmatically this pass** against `CoronavirusEasterClaim-transcript.txt` / `-sentences.json` — **not copied from the brief and not from `260835-19`.** Each range was round-tripped (`raw[b0:b1].decode() == sentence text`) and every one verified exact.

⭐⭐ **Second-rendering corroboration** (`CoronavirusEasterClaim-youtube.srt`), independent of AssemblyAI: `"one of the problems I have with reformed"` ✅ · `"that is representative of reformed"` ✅ · `"said this at the beginning so apologies"` ✅ · `"different grades of reformed theology"` ✅ · `"the vast majority"` ✅ · `"Presbyterianism"` ✅.

| # | `s` | bytes | t (s) | timestamp | content |
|---|---|---|---|---|---|
| A1 | s90 | @8472-8684 | 620.4-632.8 | [10:20]-[10:32] | scoping marker at the outset *(already in `LS-129`)* |
| A2 | s101-102 | @9772-10168 | 709.5-732.7 | [11:49]-[12:12] | incense/instruments, hedged *"Most"* *(already in `LS-129`)* |
| **A3** | **s140** | **@12819-12944** | **927.7-937.0** | **[15:27]-[15:37]** | **unqualified generalization #1** |
| **A4** | **s145** | **@13479-13681** | **980.5-992.5** | **[16:20]-[16:32]** | *"…not a scriptural position"*; clause at **[16:27]-[16:32]** |
| **A5** | **s162** | **@15011-15069** | **1090.3-1092.7** | **[18:10]-[18:12]** | **unqualified generalization #2 — NOT IN THE BRIEF** |
| **A6** | **s163-164** | **@15070-15186** | **1096.3-1100.8** | **[18:16]-[18:20]** | *"I should have probably said this at the beginning…"* |
| **A7** | **s165-167** | **@15187-15474** | **1102.0-1118.6** | **[18:21]-[18:38]** | *"different grades of Reformed theology"* |
| **A8** | **s168** | **@15475-15619** | **1119.5-1130.8** | **[18:39]-[18:50]** | *"the vast majority of Reformed people would not agree"* |
| **A9** | **s171** | **@15726-15905** | **1138.0-1148.9** | **[18:58]-[19:08]** | *"please don't hear me say that this is… representative"* |
| **A10** | **s172-173** | **@15906-16033** | **1149.6-1157.5** | **[19:09]-[19:17]** | the Puritans sentences |
| **A11** | **s174** | **@16034-16065** | **1158.2-1159.8** | **[19:18]-[19:19]** | *"So I just want to clarify that."* |
| **A12** | **s210** | **@19380-19651** | **1388.5-1405.0** | **[23:08]-[23:24]** | *"the vast majority of Presbyterians today— I love Presbyterians"* |
| **A13** | **s212-213** | **@19665-19771** | **1407.5-1415.8** | **[23:27]-[23:35]** | *"…an extreme form of Presbyterianism."* |
| **A14** | **s215** | **@19893-20025** | **1422.9-1431.6** | **[23:42]-[23:51]** | *"not a condemnation of Presbyterians in general"* |

### ⚠️⚠️ Five divergences between the brief and the artifact — reported, not reconciled

**(1) ⛔⛔ MATERIAL — the brief's `18:57`–`19:17` quotation REVERSES SOURCE ORDER.** It presents *"if you are not reformed yourself… representative of reformed theology in general today… I should have probably said this at the beginning so apologies to my reformed friends"* as one quotation whose ellipsis implies the apology **follows.** It **precedes** it: apology **A6 [18:16]-[18:20]**, *"representative"* sentence **A9 [18:58]-[19:08]** — **38 seconds later.** Both sentences are genuine, both are his, and the self-correction is real. ⛔ **But the composite must never be deployed in the brief's form** — an ellipsis that inverts source order is precisely what hands the other party a legitimate grievance. Recorded as two separate quotations in true order.

**(2) ⛔⛔ MATERIAL — *"He goes on in this stretch to characterize no-instruments and no-incense-in-worship"* is FALSE as to sequence.** That is **A2, [11:49]-[12:12]** — **three and a half minutes BEFORE** the `[15:27]` generalization, not after it — and it is already registered in `LS-129`.

**(3) ⚠️ Minor timing.** `15:27`–`15:36` → sentence spans **[15:27]-[15:37]** *(the brief is right about the words; `15:36` is the onset of the final word, "scriptural")*. `16:28` → the clause runs **[16:27]-[16:32]**. `23:30`–`23:34` → **[23:32]-[23:35]**.

**(4) ⭐ The brief is RIGHT and the primary ASR is WRONG on wording.** The brief's *"is that it it has"* matches the YouTube rendering verbatim; AssemblyAI drops one *"it"* (*"is that It has"*). **JD's ear and the second rendering agree against the primary ASR.** The brief's wording is authoritative and is what the entry records.

**(5) ⚠️** The fringe characterization already carries its own hedge **in his own words** — *"**Most** of the regulative principle followers will not allow"* — so it is not framed as universal even where it stands.

### ⚠️⚠️⚠️ The counter-datum, recorded prominently

A scoping marker is present **at the outset.** At **A1, [10:20]-[10:32]** — the first time he introduces the regulative principle at all, five minutes before A3 — he **already** says *"this is obviously very much a conservative, I would say fundamentalist type of Presbyterian."*

⛔⛔ **So *"he opens with an unqualified generalization"* is NOT sustainable as stated against this file.**

⚠️ **The counter-datum's own limit is recorded too:** A1 scopes **the article's author** (who holds the RPW), whereas A3/A5 generalize about **Reformed theology as such** (*"positions that are clearly not scriptural"*). Arguably different propositions.

⭐⭐ **The narrowest form surviving every datum**, recorded on the entry's face: *within `[15:27]`-`[18:12]` he twice generalizes about Reformed theology without qualification, having scoped the target correctly at `[10:20]`; from `[18:16]` he re-scopes at length and names his own sequencing as backwards.* ⛔ **Whether that still supports JD's *"rhetorical strategy"* reading is JD's judgment and is LEFT OPEN.**

### ⭐⭐ Two findings the brief did not have, both favouring the observation

- **A SECOND unqualified generalization at A5, [18:10]-[18:12]** — *"And this is another problem I have with Reformed theology"* — six seconds before the correction block opens.
- **The self-correction is a sustained ~63-second block (A6→A11, [18:16]-[19:19]), resumed at A12→A14 ([23:08]-[23:51])** — not the single sentence the brief has.

### ⭐⭐ Corpus corroboration JD did not cite — mechanisms kept **distinct**

- **`BP-52`'s open standing-pattern flag** (Everhard video — JD's own second instance) is **answered but not conflated.** `BP-50`/`BP-52` **fabricate** the opponent's position (*"what you're saying is"*); `File 65` **mis-scopes** a real position's constituency. Family resemblance is not identity.
- **§13's existing `[Analysis]`** *"He refutes the populist RPW, not the confessional one"* — same observation, no mechanism.
- ⚠️⚠️ **`DQ-3` is a COUNTER-EXAMPLE as much as a corroboration and is recorded as such.** There (Discord, 2026-07-09) he names the scope **himself and up front** — *"the most extreme I can think of"* — which is the **opposite** of the `File 65` sequencing. ⛔ **NOT counted as a fourth instance of JD's pattern.**

---

## 5. ⛔⛔ Numbering — no ledger number consumed, and the reasoning is on the entry's face

`LS-130` was verified free and **deliberately not spent.** The `LS` series is a `[Stated]` source-tag series for findings about **what Rev. James said**; this entry is `[Analysis]` — **JD's own reasoning.** Minting an `LS` for it would place JD's argument inside a ledger of Rev. James's statements, which is **exactly the conflation the three-layer system exists to prevent** (`CLAUDE.md`: *"These layers are never conflated"*).

⭐ **Precedent followed, not invented:** `RJ_Incense_Analysis.md` §12.2's *"JD's observation"*, `BP-52`'s `[Analysis — pattern note]`, and `BP-54`'s `[Analysis — the equivocation, JD-identified]` all carry owner-attributed analysis **with no number of their own.**

**Next free values, all unchanged:** `LS-130`, `DQ-25`, `IP-109`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EXT-4`, `W47`, `File 72`.

---

## 6. ⛔⛔⛔ Limits honoured

| Limit | Status |
|---|---|
| `DQ-9` | ⛔ **NOT moved, not touched.** §C is confined to a dated juxtaposition |
| Label-vs-level (left open by `260835-19`) | ⛔ **NOT resolved.** Nothing selects between `260835-18`'s readings (a) and (c) |
| §12.2's explicit trigger | ⛔ **NOT fired.** It requires *his usage of the term* shown **non-standard in his own words**; **rejecting** a principle is not a non-standard use of it |
| JD's analysis | ✅ Recorded **as JD's**, attributed explicitly, adopted by nobody |
| The self-correction | ✅ **Retained**, with a standing bar on any future use that omits it |
| JD's hypothesis (§D) | ✅ Recorded **as unestablished**; no evidence offered or gathered for it |
| `Incense_Conversational_Outline.md` | ⛔ **NOT touched** |
| Anything toward Rev. James | ⛔ **Nothing drafted, altered or posted** |
| Existing findings | ⛔ **None altered, renumbered or re-pointed;** every addition is a dated note beside the original |
| `SRC_Manifest.md` | ⛔ **NOT touched** — no source ingested, no hash changed, no ear-verification class extended |

---

## 7. Validator AFTER, and files touched

**`82 ok · 9 warnings · 0 errors`** — **identical to baseline; no regression.** All nine codes unchanged, same counts. Full output: `passes/260835-20_validator-after.txt`.

- `[C3]` `PROJECT_STATE.md` **`260835-20`** ✅ · `St_Francis_EMC_Distinctives.md` **`260835-20`** ✅ · `RJ_Incense_Analysis.md` **`260835-20`** ✅ — all agree with registry.
- `[C2]` **`LS-1..129` unbroken** — confirming `LS-130` was not consumed.

**Three tracked files touched**, plus three new `passes/` artifacts:

| File | Change |
|---|---|
| `St_Francis_EMC_Distinctives.md` | New dated Analysis-layer entry at §13 (§A quotation table, §B JD's `[Analysis]`, §C dated observation, §D JD's hypothesis, three hard limits, numbering note); stamp → `260835-20`; two changelog entries (`v-260835-20`, `v5.1`) |
| `RJ_Incense_Analysis.md` | One pointer-only dated note at §12.2; stamp → `260835-20`; one changelog entry |
| `PROJECT_STATE.md` | `260835-20` gate note + pass note; stamp → `260835-20`; three registry rows updated (its own, distinctives, incense analysis) |

---

## 8. ⚠️ One honest process note

At gate I ran `git status --short` **without** `--no-optional-locks`, contrary to the project's standing convention from the `260835-3` FUSE-mount diagnosis. On this FUSE mount that leaves a **benign 0-byte `.git/index.lock`**, which is present now. ⛔ **No `rm` was attempted and none should be** — per `260835-3` the artifact is benign, and all subsequent git reads (`--no-optional-locks status`, `rev-parse`, `diff`) succeeded normally. Reported rather than quietly cleaned.

---

## 9. Git state — ⛔ nothing committed

```
$ git --no-optional-locks status --short
 M PROJECT_STATE.md
 M RJ_Incense_Analysis.md
 M St_Francis_EMC_Distinctives.md

$ git --no-optional-locks diff --stat
 PROJECT_STATE.md               | 30 +++++++++++++---
 RJ_Incense_Analysis.md         | 14 +++++++-
 St_Francis_EMC_Distinctives.md | 77 +++++++++++++++++++++++++++++++++++++++++-
 3 files changed, 115 insertions(+), 6 deletions(-)
```

**HEAD unchanged at `3e0f1322eb4e097f4a4efb46b5ba20b695b960ec`.**

### What to stage

```
git add PROJECT_STATE.md \
        RJ_Incense_Analysis.md \
        St_Francis_EMC_Distinctives.md \
        passes/260835-20_jd-scope-drift-analysis-file65.diff \
        passes/260835-20_jd-scope-drift-analysis-file65_close-out.md \
        passes/260835-20_validator-after.txt
```

Suggested commit message: `260835-20: JD's scope-drift/self-correction Analysis on File 65 (§13); §12.2 pointer; no ledger number consumed`

⛔ **COMMITTED NOTHING.** Staging and commit are JD's.
