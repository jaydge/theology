# 260835-56 — Censing prayer capture and four verification checks

**Date:** 2026-09-05 · **Class:** external research and source capture · **Ledger numbers consumed: NONE**

⛔⛔ **Nothing in this pass is a finding about Rev. James.** No `DQ`, `IP`, `LS`, `RV`,
`Rev`, `BLOG`, `POD`, `VP`, `GV`, `RC`, `BP`, `EXT`, `W`, `File` or `DELTA` number was
consumed, and none was needed.

---

## 1. Gate

| Item | Value |
|---|---|
| Briefed HEAD | `2e38b41` |
| Actual HEAD | `2e38b41a5352c4a686908b5ffb537e2e2f36ab3c` — ✅ **matches exactly**; branch `main` |
| `git --no-optional-locks status --short` before first write | ✅ **EMPTY**, captured directly, not reconstructed |
| Briefed validator baseline | `98 ok / 11 warnings / 0 errors` |
| Validator BEFORE, re-derived on the clean tree | ✅ **`98 ok · 11 warnings · 0 errors` — the brief's figure is CORRECT** |
| Validator AFTER | **`98 ok · 11 warnings · 0 errors`** — unchanged |
| `PROJECT_STATE.md` stamp at gate | `260835-55` |

Every git read used `git --no-optional-locks`, per the `260835-3` FUSE-lock diagnosis.

⚠️ **The AFTER figure is unchanged BECAUSE the new files are untracked, not because
nothing was added.** Twenty new files exist in the working tree and the validator does
not examine them. **This is stated so the unchanged number is not mistaken for
evidence that the tree is complete.** See §5.

### Stamp derivation — hazard note read FIRST, and the hazard FIRED

⭐⭐ **The `260835-12`/`260835-14` hazard note was read before anything was derived, as
the brief required.** It warns in both directions: `260835-12` reads as available inside
prose asserting its own absence but is REAL and CONSUMED (commit `530d987`); `260835-14`
exists only as filenames and a commit message, REAL and CONSUMED (commit `68bf1d8`);
**and a predecessor's forward absence-assertion produces a content hit that is NOT a
consumption.** Both re-confirmed consumed; neither in play at this end of the range.

⚠️⚠️ **THE SECOND LIMB FIRED, AND THE BRIEF WAS RIGHT TO WARN AGAINST ASSUMING
SEQUENCE.** A naive content-grep returns `260835-56` as an apparent hit. **All three
occurrences are `260835-55`'s own forward absence-assertion** — the sentence
*"`260835-56` and above return ZERO repo-wide"* — appearing in `PROJECT_STATE.md` L11,
in `passes/260835-55_hopkins-vs-dekoven-malachi-1-11.diff` L262, and in that pass's
close-out L23. ✅ **Each was opened and read in context. A content hit, not a
consumption.**

**Derivation.** Distinct-stamp sweep over tracked `*.md`/`*.py`/`*.txt`, numerically
sorted, returns an unbroken run **`260835-1 … 260835-55`**, no gaps. ✅ `260835-57` and
above return **ZERO** repo-wide. ✅ `260836-` … `260839-` return **ZERO**. ✅
`git log --all` tops out at `260835-55` (`2e38b41`); `passes/`, numerically sorted, tops
out at `260835-55`. ⚠️ **`260835-99` re-checked in context and re-confirmed NOT a
stamp** — the upper endpoint of an absence-assertion range inside earlier close-out
prose. **This pass is `260835-56`.**

---

## 2. What was produced

**One new canonical file:** `Ceremonial_Meaning_Source_Checks.md` (~24 KB), four
sections, each carrying an explicit verdict line.

**Nineteen new `src/` captures**, each with a `CAPTURE HEADER` block giving source URL,
retrieval date and edition, marked as not part of the source. Full list at §5 of the
canonical file.

⛔ **No existing corpus file was modified.** The one apparent exception is not one:
`src/SRC_PRIMARY_1868_Five_Bishops_Report_On_Ritualism.txt` was **created by this pass**
and then had a `RESOLVED` block **appended** to its own capture header later in the same
pass. It is a new file, not an edit to an existing one, and the append is additive.

---

## 3. The four verdicts

| § | Item | Verdict |
|---|---|---|
| §1 | Censing prayer texts | **PARTIAL** |
| §2 | Purchas and Mackonochie | **FALSIFIED** (the working belief) |
| §3 | The "1868 bishops' ritualism report" | **PARTIAL** |
| §4 | Westall title page attribution | **FALSIFIED** |

### §1 — the load-bearing item, and the claim needs narrowing before deployment

⭐⭐⭐ **THE HIGHEST-VALUE OUTPUT WAS OBTAINED. The Byzantine text does ask God to
receive the incense at a heavenly altar, and it is quoted exactly**, from Hapgood 1906
p. 75 read off the page image rather than OCR: *"which do thou accept upon thy most
heavenly Altar."* All ten located published renderings, 1722 to the present, carry both
"offer incense" and a petition for reception at a heavenly altar. **No translation was
produced by this pass.**

⛔⛔ **But the claim as briefed is too strong and must not be deployed in its present
form.** *"In both Roman and Eastern use the censing is accompanied by prayers treating
the incense as an offering God receives"* is **true of the Byzantine rite, true of the
pre-1970 Roman rite in a weaker and mediated way, and FALSE of the current Roman rite,
which prescribes no words at all** — GIRM §277: *"blesses it with the Sign of the Cross,
without saying anything."* ⚠️ **And the Roman prayer that does ask reception,
*Per intercessionem*, names the heavenly altar only as where Michael stands, not as the
place of reception. That distinction is load-bearing and an informed interlocutor will
press it.**

⭐ **A counterweight found inside the repo's own primary source and recorded because it
runs against the argument:** Percival, the 1899 submission's own expert on the theology
of incense, at printed p. 90 — *"It is a complete mistake to suppose that the burning of
Incense necessarily is an act of Divine worship, or has any necessary connection with
sacrifice."* ⛔ **And Birkbeck's Appendix B, the submission's treatment of Eastern use,
quotes no censing prayer at all. The ritualists' own brief did not deploy the text this
pass has now sourced.**

### §2 — the working belief is wrong in both halves

⛔⛔ **Incense was a pleaded article in BOTH prosecutions and was decided against the
priest in BOTH, by Phillimore in the Court of Arches.** In *Martin v. Mackonochie* it
was **head (2) of four** and was held *"illegal and must be discontinued."* In
*Elphinstone v. Purchas* (Arches 1870) three incense articles drew a monition. ⭐ **The
real distinction is the court, not the case: every English incense holding before 1899
is an Arches holding, and the Judicial Committee never decided the point** — confirmed
by the Crown's own 1906 Royal Commission on Ecclesiastical Discipline: *"It has been held
in the Court of Arches that the ceremonial use of incense is illegal. The question has
never been before the Judicial Committee."*

⚠️ **A correction to a citation the project has been carrying.** The 1899 submission's
Phillimore quotation is at **printed p. 33** — re-derived this pass from the page image
at leaf 45, against the `leaf = folio + 12` offset re-verified independently. **The
capture file written earlier in this pass gives p. 22; that is wrong and is superseded
in writing.** The "inert use" passage is at **printed p. 18**, and the OCR corruption
"imert" in the existing `src/` text file is resolved to **"inert"** off the image.

⚠️ **And the "inert" language appears to be Cairns's in the Privy Council, not
Phillimore's, where it names incense on the UNLAWFUL side of the line — so the
distinction the 1899 pamphlet leans on comes from an adverse dictum, not a permission.**
⛔ **Bounded: this rests on Tract 259's arrangement, not on L.R. 2 A. & E. itself, which
could not be obtained. Left OPEN, not asserted.**

### §3 — the brief's own framing was too narrow, and neither expected answer is right

⛔ **"A garbling of the 1866 Declaration" is FALSIFIED — a real, dated 1868 document
exists whose entire subject is incense and lights:** the **Second Report of the Royal
Commission on Ritual, 30 April 1868, [C. 4016]**, paragraph 7. ⚠️ **But it is a Royal
Commission's report, not the bishops' — six prelates of twenty-nine members, and one of
the six dissented from its enforcement paragraphs.**

⛔⛔ **AND A CORRECTION THAT RUNS AGAINST THE REPO'S EXISTING §9.2(a): the American
"1868" report is 1871.** The Five Bishops were appointed 29 October 1868 and reported to
the House of Bishops at Baltimore on **5 October 1871**, printed as Appendix IX,
pp. 598–601, of the 1871 Journal. **Project Canterbury's "c. 1868" is a conjecture and
it is wrong**, and `American_Episcopal_Reception_1899_Opinion.md` §9.2(a) inherited it.
⚠️ **The "1866 / 1868 / 1874 eight-year pattern" recorded at `260835-54` should read
1866 / 1871 / 1874. The pattern survives; the middle date does not.** ⛔ **Not applied
— see §5.**

⚠️ **A circulating misquotation was identified and its source named.** The wording
*"restrain all variations from established usage in respect to the use of lighted
candles and incense…"* is **not** the Report's; it is Roberts's *History of the English
Church Union* (1895), reordering and re-wording the clause inside quotation marks. The
Roberts page is captured and **deliberately flagged `SRC_SECONDARY_`**, as the
provenance of an error rather than as authority.

⭐ **A silence recorded, re-derived by grep this pass:** `royal commission`,
`ritual commission` and `second report` each return **0** hits case-insensitively across
the complete `src/SRC_PRIMARY_1899_Westall_Case_For_Incense.txt`. ⛔ **The 1899 ritualist
submission never mentions the one official English inquiry devoted to incense — the same
shape as the Advertisements silence at `Ritualist_Case_For_Incense_and_the_1899_Opinion.md`
§4b.**

### §4 — the attribution is wrong twice over

Read locally off the page image at **leaf 7**; no web search was needed, as the brief
predicted. ⛔⛔ **The title page names NO author, NO editor and NO contributor.** Westall
is the clergyman **"ON BEHALF OF"** whom the case was submitted, not its author. **T. A.
Lacey does not appear on the title page.** He is named in the Table of Contents (leaf 9)
as author of **Appendix F** (p. 141) and **Appendix J** (p. 171), and signs Appendix F at
its end. ⭐ **Every one of the nine appendices is separately attributed; Frere has
three (A, E, H) to Lacey's two.** ⚠️ **So a "Westall and Lacey" attribution is an
inference from the contents page, and if it were to be made at all it would have to name
Frere ahead of Lacey.**

---

## 4. Discipline observed

- ⛔ **No Greek, Latin or Church Slavonic translated by this pass** — not a text, not a
  phrase, not to fill a gap. Every English rendering is an existing published translation
  with translator, edition and location recorded. Where none could be located the item is
  marked UNMATCHED with the searches recorded.
- ⭐ **Every source relied on for §§1–3 was captured to `src/`, not merely cited**, per
  the brief's constraint and `CLAUDE.md` §Source handling.
- ⭐ **Every figure asserted was re-derived by grep or off a page image rather than taken
  from the brief or from a subagent's report.** The brief's HEAD, its validator baseline,
  the `leaf = folio + 12` offset, the Westall folios, the zero-hit sweeps and the stamp
  were all re-derived. **Two subagent page citations were found wrong on re-derivation
  and are corrected in writing** (§2 above).
- ⚠️ **Public-domain editions were preferred throughout.** Modern copyrighted
  translations are cited and quoted only at the length of the single prayer, and marked
  as under copyright.

---

## 5. What this pass deliberately did NOT do, and what is owed

⛔ **No corpus file modified**, per brief. ⛔ **Nothing committed beyond `passes/`**,
per brief.

⚠️⚠️ **REGISTRATION DEBT — NAMED, NOT FOLDED IN, AND IT IS THE `260835-52` CLOSE-OUT
DEFECT IN A NEW PLACE.** `CLAUDE.md` close-out rule 3 requires the `PROJECT_STATE.md` §4
registry cell bumped in the same pass for every file touched, and §Source handling
requires `SRC_Manifest.md` registration for source captures. **This pass creates one
canonical file and nineteen captures and registers NONE of them, because the brief
forbids modifying any existing corpus file and reserves the corpus commit to JD.**
⛔ **Owed work. The validator will not catch it until the files are tracked, which is
precisely why the unchanged AFTER figure at §1 must not be read as an all-clear.**

⚠️ **CORRECTIONS IDENTIFIED BUT NOT APPLIED** (all recorded at §6 of the canonical file):

1. `American_Episcopal_Reception_1899_Opinion.md` §9.2(a) and the eight-year pattern —
   the Five Bishops' report is **1871, not 1868**.
2. `Ritualist_Case_For_Incense_and_the_1899_Opinion.md` §4a — its Mackonochie account
   reports Phillimore's concession without the holding that **incense was head (2) of
   four and was pronounced illegal**. §4b's "including incense" for Purchas is
   **confirmed**.
3. `src/SRC_PRIMARY_1899_Westall_Case-For-Incense-Mackonochie-Passages.txt` gives the
   Phillimore quotation at p. 22; the correct folio is **p. 33**. Superseded in writing
   in the canonical file rather than edited, per never-alter.

⛔ **UNMATCHED / not reachable, bounded honestly:** L.R. 2 A. & E. 211–215 in the
original Law Reports (BaILII bot-challenged; Archive.org Law Reports OCR is front matter
only; both Butterworths pamphlet scans truncated at c. p. 30) — **the holding is carried
by three independent and mutually hostile witnesses that agree verbatim, but not by the
report itself**; *Sumner v. Wix* first page; the 1911 *EB* "Incense" article text (so not
quoted); the verbatim 1866 Declaration of Bishops; any catalogue imprint date for the
American pamphlet; ten named Byzantine service books; the 1962 *Missale Romanum* Latin
against an altar missal. ⚠️ Tract 259's internal date discrepancy for the Privy Council
judgment ("December 23rd" vs "December 28th", 1868, same judgment) — **UNRESOLVED**.

**Tooling notes for the next pass.** `web.archive.org` is hard-blocked (403). The Linux
workspace shell has **no outbound network** (proxy 403) — all fetching must go through
the fetch tool. Archive.org `_djvu.txt` fetches truncate at roughly 80–110 kB; the
working routes are the search-inside endpoint and direct page images at
`archive.org/download/<id>/page/nNNN.jpg`. The fetch tool rejects URLs over roughly 300
characters. Several oversized fetches land in host-side files that are **not** visible to
the Linux shell, and some arrive as a single enormous line that defeats grep context
flags — read those with offset/limit instead.

---

## 6. Commit

Per the brief: pass artifacts in `passes/` **alone**. The canonical file and the
nineteen `src/` captures are left **uncommitted in the working tree for JD** to review,
register and commit.
