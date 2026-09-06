# Ceremonial Meaning — Source Checks

**Last updated: 260835-56** (created 260835-56; date-stamped, format yymmdd-iteration)

---

## What this document is

Four discrete source checks, run as one pass, each ending in an explicit verdict
in one of these forms: **VERIFIED**, **FALSIFIED**, **PARTIAL**, **UNMATCHED**.

⛔⛔⛔ **HARD RULE OBSERVED THROUGHOUT: no Greek, Latin or Church Slavonic was
translated by this pass — not a full text, not a phrase, not to fill a gap.**
Every English rendering below is an existing published translation, quoted
verbatim from its own source, with translator, edition and location recorded.

⭐ **All source material relied on for §§1–3 was CAPTURED to `src/`, not merely
cited**, per `CLAUDE.md` §Source handling and the brief's constraint that this
material is intended for outward deployment. Nineteen new capture files; list at
§5.

⛔ **No existing corpus file was modified by this pass.** §4's read is against a
file already in `src/`. See §6 for the registration debt this leaves open.

---

## §0. Gate

| Item | Value |
|---|---|
| Briefed HEAD | `2e38b41` |
| Actual HEAD | `2e38b41a5352c4a686908b5ffb537e2e2f36ab3c` — ✅ **matches exactly**; branch `main` |
| `git --no-optional-locks status --short` before first write | ✅ **EMPTY**, captured directly |
| Briefed validator baseline | `98 ok / 11 warnings / 0 errors` |
| Validator re-derived on the clean tree | ✅ **`98 ok · 11 warnings · 0 errors` — the brief's figure is CORRECT** |
| `PROJECT_STATE.md` stamp at gate | `260835-55` |

Every git read used `git --no-optional-locks`.

### Stamp derivation — hazard note read FIRST, and the hazard fired

⭐⭐ **The `260835-12`/`260835-14` hazard note was read before anything was
derived.** It warns that content-grep misleads in both directions: a pass note
internally labelled `260835-12` describes work whose committed artifacts are
`260835-14`, so content-grep under-counts; **and a predecessor's forward
absence-assertion produces a content hit that is NOT a consumption.**

⚠️⚠️ **The second half of the hazard fired on this pass, exactly as warned.** A
naive sweep returns `260835-56` as an apparent hit. **All three occurrences are
`260835-55`'s own forward absence-assertion** — the sentence *"`260835-56` and
above return ZERO repo-wide"* — in `PROJECT_STATE.md` L11 and in `260835-55`'s
own `.diff` and close-out. ✅ **A content hit, not a consumption. Opened and read
in context, not assumed.**

**Derivation.** Distinct-stamp sweep over tracked `*.md`/`*.py`/`*.txt`,
numerically sorted, returns an unbroken run `260835-1 … 260835-55`, no gaps.
✅ `260835-57` and above return ZERO repo-wide. ✅ `260836-` … `260839-` return
ZERO. ✅ `git log --all` tops out at `260835-55` (`2e38b41`); `passes/`,
numerically sorted, tops out at `260835-55`. ⚠️ `260835-99` re-checked in context
and re-confirmed **NOT a stamp** — the upper endpoint of an absence-assertion
range inside earlier close-out prose. **This pass is `260835-56`.**

⛔ **NOTHING MINTED AND NO LEDGER NUMBER CONSUMED** — no `IP`, `LS`, `DQ`, `RV`,
`Rev`, `BLOG`, `POD`, `VP`, `GV`, `RC`, `BP`, `EXT`, `W`, `File` or `DELTA`. The
brief specified none, and none was.

---

## §1. Censing prayer texts — the load-bearing item

**The claim under test.** That incense acquired its Christian ceremonial meaning
alongside eucharistic sacrifice, and that **in both Roman and Eastern use the
censing is accompanied by prayers treating the incense as an offering God
receives.**

### 1a. The Byzantine prayer of the incense — the highest-value output

⭐⭐⭐ **The Byzantine text DOES ask God to receive the incense at a heavenly
altar, and here it is exactly.** Isabel Florence Hapgood, tr., *Service Book of
the Holy Orthodox-Catholic Apostolic (Greco-Russian) Church*, Boston/New York:
Houghton, Mifflin and Company, **1906, p. 75** — public domain; read from the
Cornell page image, not from OCR alone:

> **"Unto thee, O Christ our God, do we offer incense for an odour of spiritual
> fragrance : which do thou accept upon thy most heavenly Altar, and pour forth
> upon us in return the grace of thine all-holy Spirit."**

⭐ **WORDING-CRITICAL. Frozen from reuse until re-verified against the printed
page.** The load-bearing clause is **"which do thou accept upon thy most heavenly
Altar"**. The mark after "fragrance" is a spaced colon in the 1906 printing;
"Altar" is capitalised and "heavenly" is not.

**Where it is said.** At the Proskomide (Office of Oblation) of the Liturgy of St
John Chrysostom, after the particles are gathered on the diskos and immediately
before the covering of the Gifts. The deacon puts incense in the censer and says
*"Bless, Master, the censer"*; the priest says this prayer; the censer is then
used at once. **The prayer and the censing are not merely adjacent — the prayer
is the blessing of the censer that is about to be swung.**

**Revised edition.** Hapgood, rev. ed., New York: Association Press, **1922,
p. 74** — one substantive change only, **"O Christ our God" → "O Christ-God"**.

**Bishop's form**, Hapgood 1906, **p. 88**, said before the Gospel:

> "We offer unto thee the censer, O Christ our God, for the savour of a sweet
> spiritual odour; which do thou accept upon thy most heavenly Altar, requiting
> us with the grace of thy Holy Spirit."

**Published-translation variants located** (the altar clause and the verb of
reception in each):

| Rendering | Altar clause | Verb | Rights |
|---|---|---|---|
| Covel 1722, p. 17 | "thy **Altar above the Heavens**" | received (ptcp) | PD |
| Neale 1859, p. 169 | "Thy **heavenly altar**" | receive (imper.) | PD |
| Robertson 1894, p. 217 | "thy **heavenly Altar**" | accepting (ptcp) | PD |
| **Hapgood 1906 p. 75 / 1922 p. 74** | "thy **most heavenly Altar**" | accept (imper.) | PD |
| Patrinacos 1984, p. 205 | "Thy **heavenly altar**" | receive | © |
| St Tikhon's 1984/2010, pp. 22–23 | "Thy **heavenly altar**" | Receive | © |
| Lash / Thyateira | "your **altar above the heavens**" | Accept | © |
| AGES / GOA (Dedes) | "Your **altar which is above the heavens**" | accept | © |
| ROCOR E. Amer. Diocese | "Thy **most heavenly altar**" | accepting (ptcp) | © |
| Melkite / Abp Raya | "Your **altar in heaven**" | receive | © |

⭐ **Every one of the ten located renderings, from 1722 to the present, has (i)
"offer" governing *incense* as its direct object and (ii) a petition that God
accept or receive that incense at a heavenly altar. No variant weakens either
element.**

Two further public-domain renderings in full:

> **Neale 1859, p. 169:** "We offer to Thee incense, O CHRIST our GOD, for a
> savour of a spiritual perfume: receive it unto Thy heavenly altar, and send
> down in its stead the grace of Thy most HOLY SPIRIT."
>
> **Robertson 1894, p. 217:** "Incense we offer to thee, O Christ our God, for an
> odour of a spiritual sweet smell: which accepting at thy heavenly Altar, in
> return send down on us the grace of thine All-holy Spirit."

⚠️⚠️ **A CONFLATION TRAP, LOGGED BEFORE IT IS FALLEN INTO.** The words
*noetic / supersensual / super-celestial* do **not** occur in this prayer in any
located rendering. They belong to the **neighbouring post-consecration litany**
("upon his holy, and most heavenly, and supersensual Altar" — Hapgood 1906,
p. 111), which is about the **consecrated Gifts, not incense, and is not
accompanied by a censing.** ⛔ **Anyone citing a "noetic altar" for the censer
prayer has merged two texts.**

Related Byzantine texts that ask reception at a heavenly altar but concern the
oblation rather than the incense: Hapgood 1906 p. 76 (deacon holding the censer,
"bless also this oblation, and accept it on thy most heavenly Altar") and St
Basil's prayer of oblation, p. 98.

### 1b. The Roman offertory censing prayers

**Pre-1962 / 1962 form — four spoken prayers.** Nicholas Gihr, *The Holy
Sacrifice of the Mass: Dogmatically, Liturgically and Ascetically Explained*, tr.
from the 6th German ed., Freiburg im Breisgau / St. Louis: B. Herder, **1902**
(public domain; Latin and English in facing columns):

1. **Blessing of the incense, p. 535** — "By the intercession of blessed Michael
   the Archangel, standing at the right hand of the Altar of Incense, and of all
   His elect, may the Lord vouchsafe to bless✠ this incense, and **receive it as
   an odor of sweetness**. Through Christ our Lord. Amen."
2. **Censing the oblata, p. 536** — "May this incense which Thou hast blessed, O
   Lord, ascend to Thee, and may Thy mercy descend upon us."
3. **Censing the altar (Ps 140:2–4), pp. 537–538** — "Let my prayer, O Lord, be
   directed as incense in Thy sight: and the lifting up of my hands as the
   evening sacrifice…"
4. **Returning the thurible, p. 540** — "May the Lord enkindle within us the fire
   of His love and the flame of eternal charity. Amen."

Second public-domain witness with different wording: F. C. Husenbeth (ed.), *The
Missal for the Use of the Laity*, 1853, Ordinary of the Mass at the Offertory,
pp. 12–13 — e.g. no. 2 reads "May this incense blessed by thee, ascend to thee, O
Lord, and may thy mercy descend upon us."

The general blessing formula, **Gihr, p. 376**: "Be thou blessed by Him in whose
honor thou wilt be consumed. Amen." Fortescue, *The Ceremonies of the Roman Rite
Described*, London: Burns Oates and Washbourne, 1920, pp. 25 and 121, confirms
this is the invariable way incense is blessed, the offertory formula being the
sole exception.

⭐⭐ **CURRENT FORM: THERE ARE NO WORDS AT ALL.** GIRM **§277** (2011 ICEL): *"The
Priest, having put incense into the thurible, **blesses it with the Sign of the
Cross, without saying anything**."* (IGMR 2002 §144: *"benedicit nihil dicens"*.)
Order of Mass **n. 27** (2011 ICEL) is a bare rubric — "If appropriate, he also
incenses the offerings, the cross, and the altar" — with no text; the Missal
prints spoken texts at nn. 23–26 and 28 and **no incense formula among them.**
A full-text search of the entire Latin *Ordo Missae* 2002 for *Incensum /
Dirigatur / Accendat / Michael / Per intercessionem* returns **zero**.

⭐ **GIRM §75 supplies an interpretation, not a prayer**: the censing is done "so
as to signify the Church's offering and prayer rising like incense in the sight
of God." ⚠️ **That is a rubrical gloss in the weak/symbolic register — the
incense *signifies* the Church's offering; it is not itself offered.**

### 1c. Texts naming an altar in heaven, or asking God to receive the incense

- ⭐ ***Per intercessionem*** is **the only Roman censing prayer that asks God to
  receive the incense** ("in odorem suavitatis accipere"). ⚠️⚠️ **It names a
  heavenly altar — the *altaris incensi* of Rev 8:3 — but does NOT ask God to
  receive the incense AT that altar. The altar is where Michael stands. This
  distinction is load-bearing and must not be blurred.**
- ***Supplices te rogamus*** (Roman Canon, retained in EP I), 2011 ICEL: "command
  that these gifts be borne by the hands of your holy Angel **to your altar on
  high**"; Gihr 1902 (PD): "to Thine Altar on high". ⛔ **It does NOT accompany a
  censing** — not in the current form (GIRM §276's five incense moments are
  exhaustive and this is not one) and not in the 1962 form — **and it concerns
  the eucharistic gifts, not incense.**

### ⭐ Verdict on §1: **PARTIAL**

**The offering language is present in BOTH traditions historically, but not
equally, not in the same strength, and NOT AT ALL in the current Roman rite.**

- **Byzantine — offering language proper, in the strongest available form, and
  currently in force.** The verb is *offer*; the direct object is *the incense
  itself*; God is asked to *accept that incense*; the place of reception is named
  as *a heavenly altar*; and there is an explicit reciprocity — "send down upon
  us **in return** the grace of thine all-holy Spirit". ⭐ **This is not
  incense-as-symbol-of-prayer. The prayer is not mentioned.**
- **Roman, 1962 form — offering language proper is present but WEAKER, and mixed
  with three weaker registers.** *Per intercessionem* asks reception of the
  incense, but third-person and mediated through Michael's intercession, and
  without the heavenly altar as the place of reception. *Incensum istud* asserts
  ascent without requesting acceptance. ⚠️ ***Dirigatur* is the weak form
  outright** — what is asked to be directed is *my prayer*, incense being only the
  simile. *Accendat* is not offering at all. *Ab illo benedicaris* is a mere
  honorific.
- ⛔⛔ **Roman, current form — NEITHER.** No offering language, no honorific,
  nothing, because there are no words, and the rubric positively directs silence
  at the point where the old blessing formula stood.

⛔⛔⛔ **HOW THE CLAIM MUST BE NARROWED BEFORE DEPLOYMENT.** *"Both rites ask God
to receive the incense at a heavenly altar"* is **FALSE**: it holds for Byzantium
and fails for Rome twice over — the older Roman rite asks reception but never at
the heavenly altar it names, and the current Roman rite asks nothing. The
defensible form is the weaker one: *"the Byzantine rite, and the Roman rite in its
pre-1970 form, both accompany the censing with prayers treating the incense as a
thing offered to God and received by him."* ⚠️ **The asymmetry between the two
Roman forms is total, not gradual, and an informed Roman Catholic interlocutor
will know that the current Missal says nothing.**

⭐ **AND A COUNTERWEIGHT ALREADY IN THE REPO THAT MUST TRAVEL WITH THIS ITEM.**
The 1899 ritualist submission's own expert on the theology of incense, H. R.
Percival, states the contrary proposition flatly at printed p. 90 of
`src/SRC_PRIMARY_1899_Westall_Case_For_Incense.txt`: *"It is a complete mistake to
suppose that the burning of Incense necessarily is an act of Divine worship, or
has any necessary connection with sacrifice."* ⛔ **And W. J. Birkbeck's Appendix
B, the submission's dedicated treatment of Eastern use, quotes NO censing prayer
at all** — it describes the eight censings and quotes only *"O heavenly King."*
⚠️ **The ritualists' own 1899 brief did not deploy the Byzantine incense prayer.
That silence is worth knowing before the prayer is deployed now.**

---

## §2. Purchas and Mackonochie

**The working belief under test** (from the orchestration thread, unverified):
that neither judgment turned on incense — Mackonochie (1868) being about
elevation, kneeling, the mixed chalice and altar lights, and Purchas (1871) about
eastward position, vestments and wafer bread.

### ⛔⛔⛔ The working belief is WRONG, and wrong in both halves. Stated plainly, as the brief required.

**Incense was a pleaded article in both prosecutions, and in both it was decided
against the priest by Sir Robert Phillimore in the Court of Arches.** The correct
distinction is not *which case was about incense* but **which court**.

### 2a. *Martin v. Mackonochie*

- **Arches:** Sir Robert Phillimore, Dean of the Arches, judgment **28 March
  1868**, **(1868) L.R. 2 A. & E. 116**; incense at **pp. 211–215**.
- **Privy Council:** Lord Chancellor Cairns, **23 December 1868**, **(1868) L.R. 2
  P.C. 365**; lights at pp. 386–392.

**The four heads of charge**, from the official Butterworths edition of the
judgment (1868), printed p. 8:

> "(1.) The elevation of the Blessed Sacrament of the Lord's Supper, accompanied
> in Mr. Mackonochie's case by kneeling 'or excessive kneeling' at times not
> prescribed by the Rubrics.
> **(2.) The use of incense during the celebration of the Eucharist.**
> (3.) The mixing of water with wine at the time of the administration of the
> Lord's Supper.
> (4.) The use of lighted candles upon the Holy Table."

⭐ **Incense: charged — YES. Decided and monished at the Arches — YES. Before the
Privy Council — NOT AT ALL.**

Phillimore's holding, quoted verbatim in Church Association Tract 259, pp. 6–7,
from L.R. 2 A. & E. 211–215:

> "**It certainly was in use in the Church of England in the time of King Edward
> VI.'s First Prayer Book.** … On the other hand, the use of it during the
> celebration of the Eucharist is not directly ordered in any Prayer Book, Canon,
> injunction, formulary, or visitation article of the Church of England since the
> Reformation… To bring in incense at the beginning or during the celebration,
> and remove it at the close of the celebration of the Eucharist, appears to me a
> distinct ceremony, additional and not even indirectly incident to the
> ceremonies ordered by the Book of Common Prayer. **Although therefore it be an
> ancient, innocent, and pleasing custom, I am constrained to pronounce that the
> use of it by Mr. Mackonochie, in the manner specified in both charges, is
> illegal and must be discontinued.**"

⚠️⚠️ **THE 1899 SUBMISSION'S QUOTATION IS ACCURATE BUT DECAPITATED, AND THIS
MATTERS MORE THAN THE WORKING BELIEF DID.** Re-derived by this pass directly from
the page image of `src/SRC_PRIMARY_1899_Westall_Case_For_Incense-bwb_C0-AUU-939.pdf`,
**leaf 45 = printed p. 33**:

> "Sir R. Phillimore, in Martin *v.* Mackonochie (L. R. 2 Ad. and Ecc., at
> p. 215), says of incense, 'It certainly was in use in the Church of England in
> the time of King Edward the Sixth's First Prayer Book.'"

⛔ **The sentence Westall quotes is a finding of historical fact made *en route to
a holding of illegality*, and the holding is not quoted.** Deploying the concession
without the disposition is a misquotation by omission.

⚠️ **Why incense never went up on appeal.** Phillimore decided against
Mackonochie on two counts (incense, mixed chalice) and in his favour on three
(elevation, kneeling, lights). **It was the Church Association that appealed, on
the three it had lost.** Incense was therefore never before the Judicial
Committee.

### 2b. The "inert use" crux — resolved, and it runs against the ritualists

At **leaf 30 = printed p. 18** (re-derived this pass from the page image; the OCR
in `src/SRC_PRIMARY_1899_Westall_Case_For_Incense.txt` corrupts the key word to
"imert"), Westall's Statement reads:

> "Sir Robert Phillimore categorically affirms¹ that Incense was used under the
> First Prayer Book, and if he affirms that only its "*inert use* is *now* legal"
> it is to be observed (1) that the point was not made before him that the censer
> was an ornament within the Ornaments Rubric…"
>
> ¹ "See Martin *v.* Mackonochie. 2. Law Reports (Adm. and Eccl.), p. 15 anno,
> 1868." *(so printed; "p. 15" is presumably a misprint for 215 — recorded as
> printed, not corrected)*

⭐⭐ **The word is "inert", italicised and in quotation marks, and Westall
attributes it to Phillimore. On the capture, the language is Cairns's, in the
Privy Council**, L.R. 2 P.C. at 386–392 (Church Association Tract 259, pp. 4–6):

> "There is a clear and obvious distinction between **the presence in the church
> of things inert and unused**, and the active use of the same things as a part of
> the administration of a sacrament or of a ceremony. **Incense**, water, a
> banner, a torch, a candle and candlestick may be parts of the furniture or
> ornaments of a church: but **the censing of persons and things**, or, as was
> said by the Dean of Arches, the bringing in incense at the beginning or during
> the celebration, and removing it at the close of the celebration of the
> Eucharist… these acts give a life and meaning to what is otherwise inexpressive:
> and the act must be justified, if at all, as part of a ceremonial law."

⛔ **So the inert/ceremonial distinction the 1899 pamphlet leans on is real, but it
comes from an ADVERSE dictum that names incense on the unlawful side — not from a
permission.** ⚠️ **And Westall's own sentence concedes as much: it is a plea to
*distinguish* an adverse authority, not a citation of a favourable one.**

⚠️ **BOUNDED HONESTLY: the attribution to Cairns rather than Phillimore rests on
Tract 259's arrangement of the extracts, not on a reading of L.R. 2 A. & E.
itself, which this pass could not obtain (see UNMATCHED below). Whether Phillimore
also used the word at pp. 211–215 is OPEN.**

### 2c. The Purchas litigation — two cases, two names, two courts

- **Arches: *Elphinstone v. Purchas***, articles exhibited 27 November 1869,
  judgment **3 February 1870**, **(1870) L.R. 3 A. & E. 66**; incense/censing at
  pp. 99–101.
- **Privy Council: *Hebbert* (heretofore *Elphinstone*) *v. Purchas***, **23
  February 1871**, **(1871) L.R. 3 P.C. 605**. Elphinstone died; Hebbert was
  substituted.

**Incense at the Arches — charged and monished, in three forms:** censing persons
and things during Holy Communion and other Divine Service; censing the crucifix on
the holy table; and a thurifer "carrying an incense-vessel containing incense,
swinging the same" in procession, with Purchas himself censed before commencing
the Communion Service. Phillimore: these articles "are substantially proved…
illegal, on the principle of the decision in *Martin v. Mackonochie*."

⛔ **Incense at the Privy Council in 1871 — NOT AT ALL.** The appeal concerned
vestments, the eastward position, wafer bread and the mixed chalice, because those
were the points Phillimore had allowed. ⚠️ **So the received summary in the
working belief is right about the 1871 appeal and wrong to treat the appeal as
"the Purchas case".**

### 2d. Was there an English case before 1899 that DID turn on incense?

⭐⭐ **The Crown's own answer**, *Report of the Royal Commission on Ecclesiastical
Discipline*, 1906, ch. IV §(9):

> "**It has been held in the Court of Arches that the ceremonial use of incense is
> illegal. The question has never been before the Judicial Committee.**"

Also: ***Sumner v. Wix*** (Arches 1870, Phillimore) held incense burned in the
interval between Morning Prayer and Holy Communion illegal as "subsidiary and
preparatory to the celebration". ⛔ Later *Mackonochie* rounds (1870, 1874/5,
1878, 1882): no incense. ⛔ *Read v. Bishop of Lincoln* (1889–92): no incense —
six articles only, none of them incense. ⚠️ **The 1899 Archbishops' Opinion cites
no incense case law at all**; its only case citation is Benson's Lincoln judgment,
and that only for processional lights.

### ⭐ Verdict on §2: **FALSIFIED** (as to the working belief)

**Both cases CAN be cited on incense, but only in these precise terms:**

1. ***Martin v. Mackonochie* (1868) L.R. 2 A. & E. 116, at 211–215 (Arches,
   Phillimore)** — **the leading English authority holding the ceremonial use of
   incense during Holy Communion unlawful.** May also be cited for the concession
   that incense "certainly was in use… in the time of King Edward VI.'s First
   Prayer Book" — ⛔ **provided the adverse disposition is stated in the same
   breath.**
2. ***Martin v. Mackonochie* (1868) L.R. 2 P.C. 365, at 386–392 (JCPC, Cairns)** —
   **obiter only**, and the obiter puts censing on the unlawful side.
3. ***Elphinstone v. Purchas* (1870) L.R. 3 A. & E. 66, at 99–101 (Arches,
   Phillimore)** — monition against censing persons and things, censing the
   crucifix, and the thurifer in procession.
4. ⛔⛔ ***Hebbert v. Purchas* (1871) L.R. 3 P.C. 605 CANNOT be cited on incense at
   all.** Anyone citing "Purchas" for an incense proposition must cite the 1870
   Arches case under its own name.
5. ⛔ **No pre-1899 Privy Council authority on incense exists.** "The Privy Council
   held incense illegal" is wrong.

---

## §3. The "1868 bishops' ritualism report"

**Question:** is an 1868 report a distinct real document, or a garbling of the
Declaration of Bishops of 5 October 1866? ⭐ **Searched before concluding, as the
brief required — and the answer is neither of the two the brief anticipated.**

### 3a. ⛔⛔⛔ There are TWO real candidates, and the phrase mislabels both

### 3b. The American candidate is REAL but is NOT 1868 — it is 1871

`src/SRC_PRIMARY_1868_Five_Bishops_Report_On_Ritualism.txt` (captured this pass
from Project Canterbury) is the **Report on Ritualism by the Committee of Five
Bishops**. ✅ **"(1) The use of Incense" is item (1), the FIRST of eleven
recommended prohibitions — CONFIRMED VERBATIM this pass from the captured text,
not taken from the prior pass's report.** Signatories as printed: **ALFRED LEE, J.
WILLIAMS, T.M. CLARK, W. H. ODENHEIMER, J. B. KERFOOT.**

⛔⛔ **But Project Canterbury's own bibliographic line reads "No place: no
publisher, no date, c. 1868", and the "c. 1868" is a CONJECTURE, and it is WRONG.**
The document's own text says the Committee was "appointed by the House of Bishops,
at the General Convention of 1868… and to report to **the next** General
Convention", and then recommends "action by the **present** General Convention."
The Journals settle it on both ends:

- *Journal of the General Convention 1868*, House of Bishops p. 273, Twentieth
  Day, **29 October 1868** — the Presiding Bishop appoints the committee, naming
  the Bishops of Delaware, Connecticut, New Jersey, Rhode Island and Pittsburgh:
  **Lee, Williams, Odenheimer, Clark, Kerfoot.**
- *Journal of the General Convention 1871*, House of Bishops p. 263, Second Day,
  **Baltimore, Thursday 5 October 1871** — "The Bishop of Delaware presented the
  report of the Special Committee of the Five Bishops appointed at the last
  General Convention… Vide Appendix IX." **Appendix IX, pp. 598–601**, titled
  "Report of the Special Committee appointed by the House of Bishops, 1868, on
  Ritual Uniformity", is word for word the Project Canterbury pamphlet.

⭐⭐ **This CORRECTS `American_Episcopal_Reception_1899_Opinion.md` §9.2(a) and the
repo's "eight-year pattern" at §9.2, both of which date this document to 1868 on
the orchestration thread's read.** ⛔ **It also removes one of the three beats in
that pattern: the correct sequence is 1866 / 1871 / 1874, not 1866 / 1868 / 1874.**
⚠️ **The pattern is not destroyed — three attempts to name incense in eight years
becomes three attempts in eight years still — but a pass that cites "1868" for this
document is citing Project Canterbury's conjectural URL slug, not the record.**
⛔ **Not applied to that file. This pass modifies no corpus file; see §6.**

### 3c. The English candidate IS 1868, and its whole subject is incense and lights

**Second Report of the Commissioners Appointed to Inquire into the Rubrics,
Orders, and Directions for Regulating the Course and Conduct of Public Worship…**
London: Eyre & Spottiswoode for HMSO, 1868. **[C. 4016]**, HC (1867-8) xxxviii.
Letters Patent 3 June 1867 to twenty-nine Commissioners; **the Second Report is
dated 30 April 1868**, attested "W. F. KEMP, Secretary, Jerusalem Chamber,
Westminster." Chairman at that date: **Charles Thomas Longley, Archbishop of
Canterbury.** The four reports were 19 August 1867 (vestments), **30 April 1868
(candles and incense)**, 12 January 1870 (lessons), 31 August 1870 (Prayer Book).

**The recommendation, verbatim, paragraph 7:**

> "7. Under these circumstances, and in conformity with the principles which
> guided us in our First Report, we are of opinion that it is expedient to
> restrain in the public services of the Church all variations from established
> usage in respect of Lighted Candles and of Incense."

And the finding of fact at paragraph 6:

> "6. The use of Incense in the public services of the Church during the present
> century is very recent, and the instances of its introduction are very rare; and
> so far as we have any evidence before us, it is at variance with the Church's
> usage for 300 years."

⚠️⚠️ **A CIRCULATING MISQUOTATION IDENTIFIED AND ITS SOURCE NAMED.** The wording
that circulates — "restrain all variations from established usage **in respect
to** the use of lighted candles and incense in the public services of the Church"
— **is not the Report's**. It is **G. Bayfield Roberts, *The History of the English
Church Union 1859–1894* (London: Church Printing, 1895)**, which puts it in
quotation marks while reordering the clause, writing "in respect to" for "in
respect of", inserting "the use of", and de-capitalising. ⛔ **Cite paragraph 7,
not Roberts.** Captured as `SRC_SECONDARY_1895_Roberts_…` and deliberately flagged
SECONDARY.

⭐ **It is NOT a bishops' report in any fair sense.** Six of twenty-nine members
were prelates (Canterbury, Armagh, London, St David's, Oxford, Gloucester &
Bristol); the rest were peers, MPs, judges, deans and laymen. ⚠️ **And it was
signed with heavy dissent** — 23 signatures; **Beauchamp, Phillimore, Beresford
Hope, Hubbard, Gregory and T. W. Perry withheld signature**; **Wilberforce (a
bishop) and Goodwin signed but dissented from the enforcement paragraphs 8–9**;
**Coleridge and Stanley signed reserving that incense and lights "have in
themselves, and in their origin, no doctrinal significance"** and should be
restrained only where they give offence.

⚠️ **AND A SILENCE WORTH RECORDING, RE-DERIVED BY GREP THIS PASS.** A
case-insensitive search of the complete `src/SRC_PRIMARY_1899_Westall_Case_For_Incense.txt`
returns **ZERO** hits for `royal commission`, `ritual commission` and `second
report`. ⛔ **The 1899 ritualist submission never mentions the one official English
inquiry whose dedicated subject was incense — a silence of the same shape as the
Advertisements silence already recorded at `Ritualist_Case_For_Incense_and_the_1899_Opinion.md`
§4b.**

### ⭐ Verdict on §3: **PARTIAL**

⛔ **The "garbling of the 1866 Declaration" hypothesis is FALSIFIED — a real,
distinct, dated 1868 document exists whose entire subject is incense and lights.**

⚠️ **But the label "the 1868 bishops' ritualism report" fits NEITHER candidate
cleanly, and a writer using it is almost certainly conflating them.** The American
one is a *bishops'* report and names incense first, **but it is 1871.** The
English one is genuinely **1868** and is about incense, **but it is a Royal
Commission's, not the bishops'.**

**Handling rule.** If the year 1868 is load-bearing → cite the **Royal Commission's
Second Report, 30 April 1868, paragraph 7, [C. 4016], HC (1867-8) xxxviii.** If the
*bishops* are load-bearing → cite the **Five Bishops' report, presented 5 October
1871, Appendix IX to the 1871 General Convention Journal, pp. 598–601.**
⛔ **Do not let one label do both jobs.**

⚠️ **UNMATCHED within this item:** the verbatim text of the 5 October 1866
Declaration of Bishops was not located this pass (searched: the 1868 Journal,
Project Canterbury, general web search), so whether *that* document names incense
rests on `260835-54`'s Coxe reading and is not re-verified here. ⚠️ Also
UNMATCHED: any catalogue imprint date for the separately printed American pamphlet
(HathiTrust Cloudflare-blocked, loc.gov empty, no WorldCat record surfaced).

---

## §4. Westall title page attribution

**Source:** `src/SRC_PRIMARY_1899_Westall_Case_For_Incense-bwb_C0-AUU-939.pdf`.
✅ **Offset `leaf = printed folio + 12` re-verified this pass, not assumed** —
leaf 153 carries printed folio 141 and leaf 183 carries 171, both matching the
Table of Contents. The title page is an unnumbered preliminary at **leaf 7**, read
as a page image.

**The title page, transcribed exactly as printed:**

> THE CASE FOR INCENSE
>
> SUBMITTED TO HIS GRACE
>
> THE ARCHBISHOP OF CANTERBURY
>
> ON BEHALF OF
>
> THE REV. H. WESTALL
>
> ON MONDAY, MAY 8, 1899
>
> TOGETHER WITH
>
> A LEGAL ARGUMENT
>
> AND
>
> THE APPENDICES OF THE EXPERTS
>
> LONGMANS, GREEN, AND CO.
> 39, PATERNOSTER ROW, LONDON,
> NEW YORK AND BOMBAY.
> 1899

### The findings, item by item as the brief asked

- **Author as printed: NONE.** ⛔⛔ **The title page names no author, no editor and
  no contributor. There is no "by" line of any kind.**
- **Westall's capacity: NOT author.** ⭐ **He is the person *on behalf of* whom the
  case is submitted** — "SUBMITTED TO HIS GRACE THE ARCHBISHOP OF CANTERBURY **ON
  BEHALF OF** THE REV. H. WESTALL". ⚠️ **He is the respondent whose practice was at
  issue, not the writer of the book.**
- **T. A. Lacey on the title page: ABSENT.** He does not appear.
- **Where Lacey does appear** (Table of Contents, leaf 9, read as a page image):
  **Appendix F, "The Use of the Censer after the Accustomed Manner. T. A. Lacey",
  printed p. 141**, and **Appendix J, "Incense Under the Prayer Book of 1549. T. A.
  Lacey", printed p. 171.** ✅ He also **signs Appendix F at its end** (leaf 159–160
  = printed pp. 147–148, OCR "TAU AUACEYe").
- ⭐ **Frere's separate attribution is confirmed and is not unique to him.** The
  Table of Contents attributes **every** appendix separately: A and H and E to W. H.
  Frere, B to W. J. Birkbeck, C.1 to H. R. Percival and C.2 to D. Stone, D to E.
  Geldart, F and J to T. A. Lacey, G to W. H. St. J. Hope. ⛔ **The book is a
  composite of separately-signed expert appendices under a collective title, with no
  named author or editor at all.**

### ⭐ Verdict on §4: **FALSIFIED**

⛔⛔ **The source under assessment attributes this work to "Westall and Lacey"
jointly. That is wrong twice over.** Westall is not an author but the clergyman on
whose behalf the case was submitted; Lacey is not a joint author but the signed
contributor of two of the nine appendices, F and J. ⚠️ **And the deeper point: the
title page attributes the work to nobody, so any "X and Y" attribution is an
inference someone has made from the Table of Contents — and if it is going to be
made, it would have to name Frere (three appendices) ahead of Lacey (two).**

⭐ **Recommended citation form:** *The Case for Incense Submitted to His Grace the
Archbishop of Canterbury on behalf of the Rev. H. Westall* (London: Longmans, Green
& Co., 1899), then the appendix and its signed author where a specific argument is
being cited.

---

## §5. Source captures made by this pass

All under `src/`, all untracked at time of writing, each carrying a header block
marked "CAPTURE HEADER — added by pass 260835-56, not part of the source" with
source URL, retrieval date and edition.

**§1 — censing prayers (10 files)**

| File | Carries |
|---|---|
| `SRC_PRIMARY_1906_Hapgood_Service_Book_Incense_Prayer.txt` | ⭐ the load-bearing Byzantine text, 1906 p. 75 and 1922 p. 74, from page images |
| `SRC_PRIMARY_1859_Neale_Liturgies_Prothesis_Incense_Prayer.txt` | Neale 1859 p. 169 |
| `SRC_PRIMARY_1894_Robertson_Divine_Liturgies_Incense_Prayer.txt` | Robertson 1894 p. 217 |
| `SRC_PRIMARY_1722_Covel_Present_Greek_Church_Incense_Prayer.txt` | earliest English located, 1722 p. 17 |
| `SRC_PRIMARY_2026_Modern_Byzantine_Incense_Prayer_Variants.txt` | modern © renderings, quoted at prayer length only |
| `SRC_PRIMARY_1902_Gihr_Holy_Sacrifice_Offertory_Incensations.txt` | the four 1962-form prayers, PD English |
| `SRC_PRIMARY_1853_Husenbeth_Missal_Laity_Offertory_Incensations.txt` | second PD witness, differing wording |
| `SRC_PRIMARY_1920_Fortescue_Ceremonies_Roman_Rite_Ab_Illo_Benedicaris.txt` | the general blessing formula and its rubric |
| `SRC_PRIMARY_2011_GIRM_Ordo_Missae_Offertory_Incensation.txt` | ⭐ GIRM §§75, 276–277 and Order of Mass n. 27 — the silence |

**§2 — case law (5 files)**

`SRC_PRIMARY_1868_ArchesCourt_Martin-v-Mackonochie-Incense.txt` ·
`SRC_PRIMARY_1868_PrivyCouncil_Martin-v-Mackonochie-Incense-Obiter.txt` ·
`SRC_PRIMARY_1870_ArchesCourt_Elphinstone-v-Purchas-Incense.txt` ·
`SRC_PRIMARY_1899_Archbishops_Lambeth-Opinion-Incense-Lights.txt` (full text) ·
`SRC_PRIMARY_1906_RoyalCommission_Ecclesiastical-Discipline-Incense.txt`

**§2/§4 — Westall passages (1 file)**

`SRC_PRIMARY_1899_Westall_Case-For-Incense-Mackonochie-Passages.txt`
⚠️ **Its page citations are superseded by this document.** It gives the
Phillimore quotation at printed p. 22; **the correct folio, re-derived this pass
from the page image at leaf 45, is p. 33.** The "inert" passage is at p. 18.

**§3 — the 1868 question (4 files)**

`SRC_PRIMARY_1868_Five_Bishops_Report_On_Ritualism.txt` (with an appended RESOLVED
block recording the 1871 date) ·
`SRC_PRIMARY_1868_RoyalCommission_Ritual_Second-Report-Lights-Incense.txt` ·
`SRC_PRIMARY_1871_GeneralConvention_Journal_Five-Bishops-Ritual-Report.txt` ·
`SRC_SECONDARY_1895_Roberts_ECU-History_Second-Report-Ritual-Commission.txt`
(**flagged SECONDARY deliberately** — it is captured as the *provenance of a
misquotation*, not as authority)

---

## §6. What this pass did NOT do, and what it leaves owed

⛔ **No existing corpus file was modified.** Per brief.

⚠️⚠️ **REGISTRATION DEBT, FLAGGED RATHER THAN FORCED — and it is the
`260835-52` close-out defect in a new place.** `CLAUDE.md` close-out rule 3
requires the `PROJECT_STATE.md` §4 registry cell to be bumped in the same pass for
every file touched, and §Source handling requires `SRC_Manifest.md` registration
for source captures. **This pass creates one canonical file and nineteen `src/`
captures and registers NONE of them, because the brief forbids modifying any
existing corpus file and reserves the corpus commit to JD.** ⛔ **This is a named
departure, reported rather than folded in. It is owed work, and the validator will
not catch it until the files are tracked.**

⚠️ **CORRECTIONS OWED TO OTHER FILES, IDENTIFIED BUT NOT APPLIED:**

1. `American_Episcopal_Reception_1899_Opinion.md` §9.2(a) and the "eight-year
   pattern" — the Five Bishops' report is **1871, not 1868** (§3b above).
2. `Ritualist_Case_For_Incense_and_the_1899_Opinion.md` §4a — its account of
   Mackonochie does not say that **incense was head (2) of four and was held
   illegal**; it reports only Phillimore's concession. §4b's "including incense"
   for Purchas is **confirmed** (§2c above).
3. The `260835-51` / `260835-47` line on whether the Fathers connect incense to
   sacrifice now has a counterweight from inside the 1899 brief itself — Percival
   at printed p. 90 (§1 verdict above).

⛔ **NOT SEARCHED / UNMATCHED, bounded honestly:**
- **L.R. 2 A. & E. 211–215 in the original Law Reports.** BaILII returns a bot
  challenge; the Internet Archive Law Reports scan has OCR for front matter only;
  both scans of the 1868 Butterworths pamphlet truncated at c. printed p. 30. **The
  holding is therefore carried by three independent and mutually hostile witnesses
  that agree verbatim (Church Association Tract 259; Westall 1899; a modern
  ecclesiastical-law blog quoting p. 215) — but NOT by the report itself.**
- ***Sumner v. Wix*** first page in 3 A. & E. — UNMATCHED.
- The 1911 *Encyclopædia Britannica* "Incense" article text — UNMATCHED, so not
  quoted.
- Tract 259's internal date discrepancy for the Privy Council judgment
  ("December 23rd" vs "December 28th", 1868, of the same judgment) — **UNRESOLVED**.
- Byzantine service books not reachable: Antiochian *Liturgikon* (1994), HTM
  printed books, Jordanville *Hieratikon*, Pittsburgh Metropolia clergy volumes
  (2007), UGCC *Anthology for Worship* (2004), Shann's *Euchology* (1891),
  Brightman (1896), Brett (1720), Bute (1866), King (1772).
- The 1962 *Missale Romanum* Latin was **not** verified against an altar missal
  scan — no searchable copy available; the Latin is carried by Gihr's facing
  column.
- GIRM: usccb.org and vatican.va both failed to serve §§276–277; the 2011 ICEL text
  is cross-checked against the 2002 Latin and the Vatican 2003 English. ⚠️ **Should
  be re-verified against USCCB if a USCCB citation string is ever needed.**

**Tooling notes for the next pass.** `web.archive.org` is hard-blocked (HTTP 403).
The Linux workspace shell has no outbound network (proxy 403) — all fetching must
go through the fetch tool. Archive.org `_djvu.txt` fetches truncate at roughly
80–110 kB, so whole books cannot be pulled that way; the working routes are the
search-inside endpoint and direct page-image fetches at
`archive.org/download/<id>/page/nNNN.jpg`. The fetch tool rejects URLs over roughly
300 characters.
