# 260835-19 — `LS-129` minted: the 2020 normative-principle self-identification, ear-verified

**Pass type:** minting, from an already-registered source, on an ear-verification warrant. ⛔ **`File 65` was registered at `260835-18`; this pass registers no source and consumes no `File` number.** ⭐ **One number consumed: `LS-129`.**

---

## ⛔⛔ READ THIS FIRST — ONE PREMISE IN THE BRIEF DOES NOT HOLD, AND TWO SMALLER DIVERGENCES ARE REPORTED RATHER THAN RECONCILED

1. ⛔⛔⛔ **THERE IS NO "CORRECTION OF RECORD" IN `260835-18` ABOUT `File 65`'s IDENTITY, AND NONE WAS EVER NEEDED.** The brief instructs: *read `260835-18`'s "correction of record that `File 65` is `gA-ELOCiwC8` … not the earlier-cited title."* **No such correction exists.** `grep -rn -iE "CORRECTION OF RECORD|mis-cited|earlier-cited"` returns three unrelated hits (the `DQ-20` showbread correction ×2, and a `BLOG-142` miscited-verse finding). **`File 65` is `gA-ELOCiwC8` / *"Fundamentalist Claims Coronavirus is Because We Celebrate Easter? A Charitable Response"* consistently in every file that names it** — `SRC_Manifest.md` L3567, `SRC_Channel_Inventory.md` L121, `passes/260835-10`, `passes/batch9-selection_260826`, and `260835-18`'s own §8 registration table. ⭐ **Every pre-`260835-18` `File 65` mention is a next-free-number assertion inside `260835-16`/`260835-17` prose — that is exactly what `260835-18`'s own gate says it verified — not a differently-titled registration.** **Nothing was corrected because nothing was wrong.** The brief's other read-first instruction (the three-reading hedge) is real, was read in full, and is discharged below.
2. ⚠️ **TIMESTAMP RANGE.** The brief cites the self-identification at **10:12-10:17**. Against `CoronavirusEasterClaim-sentences.json` the sentence runs **t=612.6-619.6 = [10:12]-[10:19]**. ⭐ **The start matches exactly; the tail runs ~2.6 s past the cited end.** ⛔ **No conflict** — the cited range sits inside the sentence and identifies it unambiguously — **and the ASR's timing is NOT treated as authoritative against the ear.** `LS-129` carries the full sentence range and the divergence is recorded in `SRC_Manifest.md`, not silently resolved.
3. ⚠️ **VERBATIM.** JD's ear gives *"what **it is** known as"* and *"which I don't hold to **but you know** for general sake"*; the ASR gives *"what is known as"* and drops the *"you know."* ⭐ **The ear governs.** `LS-129` quotes the ASR-supported wording where the difference is immaterial to the finding, and the divergence is recorded at the manifest rather than resolved silently in either direction.

⭐⭐ **Everything else in the brief verified against the artifacts exactly, including the harder claims:** the external-stance critique does run continuously **through [13:19]** (the closing sentence ends at t=799.6 = 13:19.6); *"very subjective"* is there twice; the chapter-and-verse and scroll-versus-book objections are there; and instruments and incense are named as things *"most would not allow"* under a framework attributed to *"a conservative, I would say fundamentalist type of Presbyterian."*

---

## Gate

| Item | Value |
|---|---|
| HEAD | `99c268ed19b30d443114da73932e01e42a607a4e` — matches the briefed `99c268e`; branch `main` |
| `git --no-optional-locks status --short` before first edit | ⭐ **EMPTY** — captured directly, not reconstructed |
| Validator BEFORE | **`82 ok · 9 warnings · 0 errors`** |
| Validator AFTER | **`82 ok · 9 warnings · 0 errors`** — no regression; see the one expected text change below |
| `PROJECT_STATE.md` stamp at gate | **`260835-18`** |
| This pass | **`260835-19`** |
| Next-free `LS` at gate | **`LS-129`** — free, ⭐ **CONSUMED.** Next free is now **`LS-130`** |
| Next-free `File` | **`File 72`** — ⛔ **not consumed, none needed** |

**Nine firing codes, individually, BEFORE:** `[C1]` `src/SRC_Discord_RPW.md` 2 relative timestamps outside message headers · `[C3]` `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` no parseable stamp · `[C3]` `tools/transcribe_yt.py` no parseable stamp · `[C4]` `St_Francis_EMC_Distinctives.md` 2 stale answered-question passages · `[C5]` `RJ_Final_Question_List.md` 17 volatile-state assertions · `[C5]` `RJ_Incense_Analysis.md` 9 · `[C5]` `St_Francis_EMC_Distinctives.md` 7 · `[C10]` §15's newest `LS` citation 8 findings behind the ledger (`LS-120` vs `LS-128`) · `[C11]` outline 11 `IP` findings unreviewed. **Unchanged from the `260835-15`/`260835-16`/`260835-18` gates.**

**AFTER — same nine codes, same counts, and ⭐ EXACTLY ONE TEXT CHANGE, WHICH IS AN ARITHMETIC CONSEQUENCE OF THE MINT AND IS REPORTED RATHER THAN GLOSSED:** `[C10]` now reads ***"§15's newest LS citation is 9 findings behind the ledger (LS-120 vs LS-129)"*** where it read *"8 … vs LS-128"*. ⛔ **Same warning, same file, one further behind, because `LS-129` exists and §15 was NOT swept this pass.** ⚠️ **This was foreseen and is stated in advance rather than concealed: minting an `LS` without sweeping §15 necessarily widens that gap by one. §15 sweeping is a judgment call about creditable material and was not in this brief's scope.** ⛔ **The `[C10]` gap was ALREADY firing at gate and is not this pass's to close.**

⭐ **`[C2]` moved as it should: `LS-1..128 unbroken` at gate → `LS-1..129 unbroken, no duplicates` after.**

**FUSE lock.** The `260835-3` diagnosis was **applied, not re-derived** — every git read used `git --no-optional-locks`; no lock created, none removed, no `rm` attempted.

### Stamp and number derivation, fresh and by grep

**Pass stamp.** Repo-wide content grep for `26[0-9]{4}-[0-9]+` tops out at **`260835-18`**, which is a **REAL consumed stamp** — committed artifact `passes/260835-18_batch9-remainder-registration-and-mining_close-out.md`, and it is `PROJECT_STATE.md`'s own header stamp. `grep -rn "260835-19"` returned **zero matches repo-wide**; `grep -rn "260836-"` returned only quoted shell-command lines inside `passes/260835-9_*` prose and two close-out sentences asserting `260836-*` absent — **no live `260836` stamp.** **This pass is `260835-19`.**

**`LS` re-derived independently, not carried from the brief.** Highest registered is `LS-128`. **Every `LS-129` occurrence repo-wide was located and read in context** — 19 files, and every one is a next-free registry assertion of the form *"next-free values … `LS-129`"*, including `260835-18`'s own two. ⭐ **Independently corroborated by the validator's `[C2]` arm, which reported `LS-1..128` unbroken at gate.** **`LS-129` was free and is consumed.**

**Substrate verified, not assumed.** `CoronavirusEasterClaim-transcript.txt` re-hashed from disk this pass: `sha256 a7dfa485321815dc74882480c720cc513182c0f88c6e68b0cd97406759c1e18c`, **24,156 bytes** — **matches `SRC_Manifest.md`'s `File 65` row exactly.** Every byte range in `LS-129` was computed programmatically against that artifact, not copied from any prior document.

---

## ⭐⭐⭐ TASK 1 — `LS-129` MINTED, AND THE WARRANT QUESTION ANSWERED FROM THE CORPUS'S OWN CONVENTIONS

### The datum

**`File 65`** (`gA-ELOCiwC8`, **2020-04-09**), s89, @8351-8471, t=612.6-619.6, **[10:12]-[10:19]**:

> *"So Lutherans and Anglicans — you know, Anglican here — we hold to what is known as the normative principle of worship."*

Followed by the external placement of the regulative principle (s90, [10:20]-[10:32]), both definitions (s91-92, [10:33]-[10:49]), and a continuous external critique through **[13:19]**.

### The warrant class — determined, not invented

⛔⛔ **THE BRIEF'S OWN FRAMING IS CORRECTED RATHER THAN ADOPTED, AND THIS IS THE PASS'S ONE REAL METHOD JUDGMENT.** The brief asks whether this is *"a distinct class, or the strongest tier of an existing one"* on the ground that it is *"a stronger warrant than the six-file/single-file classes already on record."*

⚠️⚠️ **Those two classes are not on the same axis.** The **six-file** warrant (`260835-15`, `SRC_Manifest.md` L3447) and the **single-file** warrant (`260835-16`) are **SPEAKER-ATTRIBUTION** warrants — they answer *who is talking.* This datum's warrant answers *what was said.* ⛔ **Ranking a content warrant above a speaker warrant is a category error, and `LS-129` says so on its face rather than making the comparison the brief invited.**

⭐⭐⭐ **On the content axis the corpus already has a hierarchy, and this fits its top tier rather than opening a new one.** `SRC_Manifest.md` L98 describes JD's direct audio verification as **the `260810-1` class**, *"the strongest the project has."* `260835-3` extended that class from a **local audio artifact** to the **primary video** with three verifications. **This is that class.** ⛔ **Not a new class, and not asserted as one.**

⭐ **One refinement is recorded rather than claimed as a class:** `260835-3` heard **three isolated clauses**; this hearing covers a **continuous ~5-minute stretch with its surrounding context** ([08:44]-[13:19]). **That is not a nicety — it is the only reason the presence/absence-of-disclaimer contrast below is evidentially available at all.** ⭐⭐ **Logged as the class's strongest instance to date, and the first in which the hearing CHANGED the reading rather than confirming it.**

---

## ⭐⭐⭐ TASK 2 — THE THREE-READING HEDGE SUPERSEDED, IN ONE RESPECT ONLY, BY DATED NOTE

⛔⛔ **NEVER-ALTER HONOURED IN FULL. `260835-18`'s two dated notes (`St_Francis_EMC_Distinctives.md` §13 and at `LS-47`) stand word for word. Nothing was edited, trimmed, reordered or deleted.** Two new dated `260835-19` notes sit beside them.

### What is retired, and on what evidence

⛔ **Reading (b) — *"no change at all; the 2020 line is descriptive in the `LS-47` sense"* — IS RETIRED.**

⭐⭐⭐ **AND IT IS RETIRED BY `260835-18`'s OWN COUNTER-EVIDENCE, TURNED AROUND.** That pass led with the transubstantiation line as the strongest thing against the datum:

> s74, @7160-7344, t=524.7-540.0, **[08:44]-[09:00]** — *"So for instance, the superstition of the Middle Ages is we hold to the understanding of real presence or transubstantiation, **which I don't hold to**, but for general sake, real presence."*

`260835-18` read this as showing *"'we hold' in his mouth is NOT reliably a first-person subscription."* ⭐⭐ **Heard in context, it shows the reverse.** That sentence carries an **explicit parenthetical disclaimer**. The normative-principle sentence **ninety seconds later carries none** — and carries the **opposite** marker, the self-locating *"you know, Anglican here."* ⛔⛔ **The disclaimer is evidence of a habit, and the habit's absence is therefore informative rather than neutral. He marks reported speech when that is what it is.**

⭐ **Independent corroboration from a second direction:** he then spends three minutes describing the regulative principle from outside it — *"very subjective"* (twice), *"an odd position"*, *"problematic"*, *"It requires the interpreter to make a lot of assumptions"* — attributing it to *"a conservative, I would say fundamentalist type of Presbyterian."* **A man reporting a position he holds does not do that.**

### What is NOT retired

⚠️⚠️ **Readings (a) (a genuine 2020→2026 development) and (c) (stable substance under shifting labels) BOTH REMAIN LIVE. NEITHER IS SELECTED.** ⛔ **The retirement of (b) does not select between them and nothing in `LS-129` or the notes may be cited as if it did.**

### Byte-range correction, made as a note and not as an edit

⚠️ `260835-18` cites **@7232-7290**, **@8388-8439** and **@8661-8732**. None delimits the sentence it is attached to. Computed programmatically against the registered artifact this pass, the correct ranges are **@7160-7344**, **@8351-8471** and **@8685-8903**. ⛔ **The originals are NOT edited; the correction is a dated note, and `LS-129` carries the corrected ranges and is authoritative for citation.**

---

## ⛔⛔⛔ TASK 3 — `DQ-9`: RECORDED AND DATED, NOT RESOLVED, NOT CHARACTERISED

**ESTABLISHED:**
- On **2020-04-09** he self-identified, **unqualifiedly and in his own voice**, with the **normative** principle, and described the **regulative** principle from outside it (`LS-129`).
- On the **2026** record he self-identifies with the **regulative** principle and **expressly rejects** the normative label as *"too loosey-goosey"* (`IP-2`, `BP-35`).
- **The two statements are six years apart and they do not agree.**

⛔⛔⛔ **NOT ESTABLISHED — and the list is exhaustive on purpose:** **why** they differ · **which (if either)** reflects sustained practice rather than a label used loosely in a given video · whether this is a **development**, a **vocabulary shift over stable substance**, or an **inconsistency** · which of readings (a) and (c) survives.

⛔⛔ **`DQ-9` IS NOT MOVED.** `DQ-9` is the **level** question — act-level versus principle-level warrant. **A change of LABEL is not by itself a change of LEVEL**, and this pass does not treat it as one.

⚠️⚠️ **A GUARD WRITTEN FOR THE NEXT PASS, NOT FOR THIS ONE.** The tempting move — reading the 2020 normative self-identification as an admission that the 2026 regulative claim is insincere, loose, or non-standard — **is not available on this evidence**, and it is exactly the arguing-backwards `RJ_Incense_Analysis.md` §12.2 was written to forbid. **The guard is stated at the `DQ-9` block, at `LS-129`, and at §12.2.**

⏳⏳ **FLAGGED FOR A DEDICATED PASS OR JD's OWN JUDGMENT.** Recorded at `PROJECT_STATE.md`'s standing `DQ-9` obstacle block as a new dated `260835-19` note, with the dating precise on both sides. ⛔ **The act-level-over-principle-level argument remains unwritten and JD's to write.**

---

## ⭐⭐ TASK 4 — THE INCENSE CLAUSE, CROSS-REFERENCED, NO CONCLUSION DRAWN

**s101-104, @9772-10168, t=709.5-732.7, [11:49]-[12:12]:**

> *"Most of the regulative principle followers will not allow for instruments used in worship, **nor will they allow for incense used in worship**, nor robes or things like that… at least definitely **incense and instruments**. Those are 2 things that they would not allow. **Most would not allow.**"*

⭐⭐⭐ **This is the corpus's first datum in which REV. JAMES HIMSELF states the incense/RPW incompatibility** — and he states it as an **outside characterization** of a framework he is at that moment positioning himself as **not operating under**, having self-identified as normative ninety seconds earlier. He then answers it from **Psalm 150** and, at [12:29]-[12:38], *"And incense is all throughout the Old Testament and is in the New Testament too. It's in the Book of Revelation."*

**Cross-referenced to `RJ_Incense_Analysis.md` §12.2** — the *"does he hold the RPW in any standard sense?"* deferred lever — **because JD's own stated reasoning for that lever is precisely the incense/RPW incompatibility, and here Rev. James makes the same observation himself.**

⛔⛔⛔ **AND §12.2's EXPLICIT TRIGGER IS *NOT* DECLARED FIRED. The note says why, so that no later pass fires it on this entry by mistake:** the trigger requires **his usage of the term** to be shown **non-standard, in his own words.** What `LS-129` shows is that **in 2020 he used a DIFFERENT term.** ⚠️ **A different label six years earlier is a different proposition from a non-standard use of the present label.** ⛔ **The deferral stands unchanged and undeployed. No lever promoted, no argument text written or revised anywhere in that file.**

⏳ **Interpretive work left to the `RJ_Incense_Analysis.md` rewrite when it resumes.** This note exists so the material is waiting for it rather than re-derived from scratch.

---

## ⚠️ ONE PRE-EXISTING VALIDATOR DEFECT FOUND, REPORTED AND NOT FIXED

⛔⛔ **`[C3]` CANNOT DISTINGUISH `-1` FROM `-16`, `-18` OR `-19`.** `validate_project.py` L372-374 compares registry and document stamps through `re.search(r'\d{6}-\d', …)` — **one digit after the dash.** `260835-16` and `260835-18` both reduce to `260835-1` and compare **equal**.

⭐ **This is not hypothetical: at gate, the §4 registry cells for `PROJECT_STATE.md` and `SRC_Manifest.md` both read `260835-16` while both documents were stamped `260835-18`, and `[C3]` reported *"version agrees with registry"* for both.** ⛔⛔ **Real version drift was invisible to the check whose entire job is catching version drift.**

⛔ **NOT FIXED THIS PASS.** `validate_project.py` is registered at `260812-1` and is not this brief's business; a validator change would also invalidate the before/after comparison this pass rests on. ⭐ **Both stale cells were corrected as part of this pass's own registry updates, so the specific instance is gone — but the defect that hid it is not, and it will hide the next one.** ⏳ **Owed: a one-character fix (`\d{6}-\d+`) in a scoped pass, run against a clean tree so the resulting `[C3]` errors can be triaged deliberately.**

---

## §5 — Files touched, and what moved in each

| File | What changed |
|---|---|
| `St_Francis_EMC_Distinctives.md` | ⭐ **`LS-129` minted** (new ledger block after `LS-128`) · **two `260835-19` dated notes** superseding `260835-18`'s hedge at §13 and at `LS-47` · header stamp `260835-18`→`260835-19` + new summary paragraph · `v-260835-19` in the mid-file changelog · **`v5.0`** in the permanent CHANGELOG |
| `PROJECT_STATE.md` | **`260835-19` gate note + pass note** · **new dated note at the standing `DQ-9` obstacle block** · §5 next-free `LS-129`→**`LS-130`** (prior text retained) · §4 registry cells updated for all four touched files (⭐ two of which were **stale at gate** — see the validator defect above) |
| `SRC_Manifest.md` | **New ear-verification block** (verification #4, `File 65`, [08:44]-[13:19]) with the warrant class stated and the brief's six-file/single-file comparison corrected · the two timing/verbatim divergences recorded · **dated note extending the `File 65` registration** (row not edited) · header stamp + summary |
| `RJ_Incense_Analysis.md` | **One dated cross-reference note at §12.2** — flag and pointer only, ⛔ trigger NOT fired · changelog entry · header stamp |

⛔⛔ **NOT TOUCHED, EXPLICITLY:** `Incense_Conversational_Outline.md` · `RJ_Final_Question_List.md` · `SRC_Channel_Inventory.md` · `SRC_Coverage_Register.md` · `ORCHESTRATION.md` · `validate_project.py` · any source transcript or archive · **anything drafted, altered or posted toward Rev. James.**

---

## §6 — Nothing else moved

⛔⛔ **NO OTHER NUMBER OF ANY PREFIX CONSUMED. Next-free values re-derived and unchanged: `DQ-25`, `IP-109`, `RV-64`, `BLOG-159`, `POD-17`, `VP-8`, `EXT-4`, `W47`, `File 72`.** ⭐ **`LS` moved and only `LS`: `LS-129`→ next free `LS-130`.**

⛔ **No existing finding altered, renumbered or re-pointed.** ⛔ **No source ingested, registered or re-hashed** (`File 65`'s hash was **recomputed and compared**, not changed). ⛔ **No byte offset in any existing entry altered — three were corrected BY NOTE.** ⛔ **§15 NOT swept** (and the `[C10]` consequence is stated above). ⛔ **`OQ8` untouched · the Article 34 row untouched · `CL-9` untouched · Known Gaps untouched · no `VP-` pair or number · no `DELTA` · no register entry · no gate moved · no Discord state touched.**

---

## §7 — Owed

- ⏳⏳ **JD's or a dedicated pass's ruling on the 2020-normative / 2026-regulative tension.** ⛔ **This is the largest open item the pass creates and it is deliberately left open.** Everything needed to rule is now recorded and dated on both sides.
- ⏳ **The `[C3]` one-digit stamp-comparison fix**, in a scoped pass against a clean tree.
- ⏳ **`§15` sweep for the `LS-120`→`LS-129` interval** — now nine behind. Pre-existing, widened by one, not this brief's scope.
- ⏳ **`RJ_Incense_Analysis.md` rewrite** — `LS-129`'s incense clause is waiting for it at §12.2.

*(§5 rule 11 — this close-out makes no claim about its own commit state.)*

---

## §8 — Staging

**`git --no-optional-locks status --short` after the work, every line:**

```
 M PROJECT_STATE.md
 M RJ_Incense_Analysis.md
 M SRC_Manifest.md
 M St_Francis_EMC_Distinctives.md
?? passes/260835-19_ls129-normative-self-identification-ear-verified.diff
?? passes/260835-19_ls129-normative-self-identification-ear-verified_close-out.md
?? passes/260835-19_validator-after.txt
```

**Recommended staging — all seven paths, nothing withheld:** the four modified governed documents and the three new `passes/` artifacts.

⛔⛔ **NOTHING WAS COMMITTED. NOTHING WAS STAGED.** The tree is left exactly as described above for JD's review.
