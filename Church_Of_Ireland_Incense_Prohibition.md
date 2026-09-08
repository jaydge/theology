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

**⭐ THE ORCHESTRATION PREDICTION IS SUBSTANTIALLY CORRECT AND §8 IS WRONG IN ITS
PARTICULARS.** The prediction expected the prohibition "to sit in the CANONS or
STATUTES of the Church of Ireland rather than in its Book of Common Prayer,
adopted in the anti-ritualist climate following disestablishment." That is
exactly right on all three counts — instrument, body, climate. The prediction's
one miss is geographical rather than substantive: the canons are **bound into**
the 1878 Prayer Book volume, so candidate (a) did yield the text as a local
read. **§8's characterisation — "The Church of Ireland BCP" and "An Anglican
prayer book prohibiting incense outright" — is FALSIFIED as stated.**

**⛔ A SECOND, SHARPER FINDING ABOUT §8's QUOTATION.** The wording quoted in §8
is unpunctuated and lower-cases "public services." The 1878 printing is
punctuated and capitalises "Public Services." The **current** Canon 40 is
unpunctuated and lower-case. **§8's quotation therefore came from the modern
Church of Ireland canon, not from any prayer book at all** — and was then
labelled "The Church of Ireland BCP." The substance survives intact; the
attribution does not. §8 also renders "therefor" as "therefore," which is a
different word.

---

## §1 — LOCATE THE INSTRUMENT

### VERDICT: **PARTIAL**

The prohibition is real, and the §8 wording is substantially accurate. The
attribution of it to a prayer book is wrong.

### What was found, and where

**Instrument:** Canon 38, "Of Incense," of the **Constitutions and Canons
Ecclesiastical** of the Church of Ireland.

**Adopting body and date, as printed at the head of the canons** (PDF p. 495 of
the repo file), verbatim:

> Agreed to and Decreed, by the Archbishops and Bishops, and the Representatives
> of the Clergy and Laity of the Church of Ireland, at General Synods held in
> Dublin in the years of our Lord 1871 and 1877.

**Exact wording as printed** (PDF p. 501, right column; drop-capital opening
resolved by 400 dpi image OCR, the two extractions agreeing on every word):

> **38. Of Incense.**
>
> NO incense or any substitution therefor, or imitation thereof, shall, at any
> time, be used in any church or chapel, or other place in which the Public
> Services of the Church are celebrated.

**Volume:** *The Book of Common Prayer … according to the use of The Church of
Ireland*, Dublin, "PUBLISHED BY AUTHORITY OF THE GENERAL SYNOD OF THE CHURCH OF
IRELAND, By the Association for Promoting Christian Knowledge," MDCCCLXXVIII.
Repo copy: `src/Book_of_Common_Prayer_(Church_of_Ireland,_1878).pdf`.

### ⭐ The structural point that decides the verdict

The canons **are bound into the 1878 volume** — after the Articles of Religion
and the Table of Kindred and Affinity, at PDF p. 495, running to p. 504, followed
by the "Additional Canons, 1877" and a reprint of the English Canon 30 of 1604 on
the sign of the cross.

But the volume's own **"CONTENTS OF THIS BOOK"** (PDF p. 11) runs 1 to 34 and
ends at *"34. Table of Kindred and Affinity within which none may marry
together."* **The Constitutions and Canons are not listed.** On the book's own
reckoning of what it contains, they are printed *with* the Prayer Book and are
not part *of* it. Canon 1 confirms the distinction from the other direction: it
speaks of "The Book of Common Prayer" as a thing the canons regulate the use of.

**Handling consequence.** "An Anglican prayer book prohibiting incense outright"
must not be said. What can be said, and is fully documented: **an Anglican
church prohibited incense outright, by canon, and printed that canon inside its
prayer book.** That is still a strong claim — arguably a cleaner one, since a
canon is a disciplinary enactment of a governing synod rather than a rubric, and
carries a stated penalty. But it is a different claim, and an informed
interlocutor who opens the 1878 book will find the contents page in about
fifteen seconds.

### The search that establishes the negative

Whole-volume search of the pdftotext extraction of all 514 pages (1,512,268
characters) for: `incens | cens[ei]r | censing | thurib | frankincens | perfum |
odour | odor | ceremon | ornament | vestment | vesture | cross | crosses | light
| lights`.

**Exactly four hits on the incense family in the entire book:**

| # | Location | Text | Character |
|---|---|---|---|
| 1 | Epistle for the Epiphany | "…frankincense, and myrrh" (Matt 2) | Scripture |
| 2 | The Psalter | "in thy sight as the incense" (Ps 141:2) | Scripture |
| 3 | PDF p. 501 | "38. Of Incense." | canon heading |
| 4 | PDF p. 501 | "NO incense or any substitution therefor…" | canon text |

**Per the 260835-66 caution, the negative was re-run against hyphen-split
fragments.** Method: (a) direct search for the fragment forms `in-` `incen-`
`cen-` `frankin-` `thuri-` `per-` `cere-` `orna-` at end of line — **zero hits
each**; (b) no soft hyphens or Unicode hyphen characters anywhere in the file
(0 occurrences of U+00AD, U+2010, U+2011); (c) the whole file was re-joined
programmatically (`-\s*\n\s*` removed, all whitespace collapsed) and re-searched
— **`incens` 4, `censer` 0, `censing` 0, `thurib` 0, `perfum` 0**. No additional
hit. *(260835-66's finding concerned the Internet Archive full-text index, which
this pass did not use; the analogous check was run against the local file
anyway.)*

**⚠️ THIS IS NOT A FAILED EXTRACTION.** The text layer returns Psalm 141:2 and
Matthew 2 correctly. The absence of incense from the rubrics, the Preface, and
the Articles of Religion is a **real absence**, not an artefact.

### Candidates (b) and (c)

Not live. Candidate (a) yielded the instrument on a local read, and the
instrument turned out to be a canon — so (b), "the canons or statutes adopted by
the General Synod following disestablishment, 1870 onward," is not an alternative
to (a) but a description of what (a) contains. No separate Declaration or
Resolution of the General Synod (candidate c) was sought once the canon was in
hand.

---

## §2 — SCOPE, AND WHAT ELSE IT PROHIBITS

### VERDICT: **VERIFIED**

### (a) What else the same instrument prohibits

**The incense clause sits in the middle of a long anti-ritualist list.** It is
one of a run of consecutive canons, 34 to 40, doing nothing else:

| Canon | Subject | What it does |
|---|---|---|
| 4 | Ecclesiastical vesture | Plain white surplice, bands, black scarf, hood. **"And no Minister shall wear any other Ecclesiastical vestment or ornament"** |
| 5 | Ordering of Divine Service | **"in no case when he is offering up Public Prayer shall his back be turned to the Congregation"** |
| 34 | The Communion Table | A movable table of wood, decent covering only |
| 35 | Lights | **No lighted lamps or candles** on the Table or anywhere in the church during services, except when needed for light |
| 36 | Crosses | **No cross at all**, "ornamental or otherwise," on the Table, on its covering, or on the wall or structure behind it |
| 37 | Administration of the Lord's Supper | No **elevation** of paten or cup beyond what is needed to take them in hand; no **mixed chalice**; no **wafer bread**; and "**all acts, words, ornaments, and ceremonies other than those that are prescribed by the Order in the Book of Common Prayer, are hereby declared to be unlawful, and are prohibited**" |
| **38** | **Incense** | **Absolute** |
| 39 | Processions | Unlawful to carry any **cross, banner, or picture** through any church or churchyard in any religious service or ceremonial; no procession as a rite or ceremony unless prescribed by the Bishop or the Rubrics |
| 40 | Ornaments of the Church | No change to structure, ornaments or monuments without incumbent, select vestry and bishop; appeal to the Diocesan Court and thence to the Court of the General Synod |

**⭐ JD NEEDS TO KNOW WHICH HE HAS, AND THIS IS THE ANSWER.** The incense clause
is **not a standalone judgement about incense**. It is one line in a seven-canon
sweep drafted, on the historian's account, to "rule out high-church practices" —
which is why it stands beside a canon banning crosses outright and a canon
banning candles. Deployed as though it were a considered theological verdict on
incense specifically, it will be answered by an informed Anglo-Catholic in one
move: *the same code banned the cross, and they took that back.*

Note also **Canon 37's sweeper clause**, which is arguably the more interesting
find: everything not prescribed by the Prayer Book order is declared unlawful at
Holy Communion. **That is a Church of Ireland canon enacting, in terms, something
very close to a regulative rule for the Communion service** — with one carved-out
exception, the customary reverence at the Holy Name in the Nicene Creed.

### (b) Absolute or conditioned?

**Absolute.** Canon 38 carries no proviso, no episcopal dispensation, no
exception. Compare its neighbours, which do carry conditions: Canon 35 excepts
candles "necessary for the purpose of giving light"; Canon 37 excepts the
customary reverence at the Holy Name; Canon 39 excepts processions "prescribed
by the Bishop, or by the Rubrics." **Canon 38 has none.** The drafting is
deliberate, and the phrase "or any substitution therefor, or imitation thereof"
closes the obvious evasions in advance.

### (c) All services or only some?

**Wider than services.** The canon reaches "any church or chapel, **or other
place** in which the Public Services of the Church are celebrated," and forbids
use "**at any time**." So it is not limited to the time of divine service, and
not limited to consecrated buildings. Contrast Canon 35, which bites only
"during the celebration of the Services or the Administration of the
Sacraments." **⭐ Incense is the most tightly drawn prohibition in the group.**

**⚠️ One limit worth noticing before deploying it.** The canon binds places where
the public services *are celebrated*. On its face it does not reach a private
house or a private oratory that is not such a place — which is the same gap the
Andrewes counterexample exploits in the English material (§8's pre-empt). Do not
claim it reaches private devotion; it does not say so.

### (d) Enforcement and penalty

**Canon 48, "The Authority of the General Synod established"** (PDF pp. 502-503):

> …if any person holding any Office within the same shall wilfully contemn,
> neglect, or violate any of the Canons or Laws thereof, and shall have been
> duly convicted, he shall for the first offence be admonished or suspended from
> his Office for a period not exceeding the term of three months, according to
> the nature or extent of such offence ; and for a second or subsequent offence
> he shall be admonished, suspended, or deprived of his Office, according to the
> extent and nature of the offence, and in each case with or without costs.

Route: Diocesan Court, with appeal to the Court of the General Synod (Canons 47
and 40).

**⚠️ The opening words of Canon 48 — "THE General Synod of the Church of Ireland,
lawfully" — are a reconstruction from a badly scrambled drop-capital extraction,
not a verified reading.** The penalty clause itself, from "assembled, being the
supreme authority…" onward, is verified by both extraction methods. Do not quote
the opening clause without re-reading PDF p. 502.

**Was it enforced against incense?** ⛔ **No prosecution for incense has been
identified.** Ford's article (SECONDARY), which surveys the ritual-canon
litigation from 1872 to 1941 in detail, names convictions for the cross (1892,
1928) and for bowing, the sign of the cross and stations of the cross (1937,
punished with six months' suspension and substantial costs) — and **names none
for incense**. Ford's own summary of the position by the end of the twentieth
century is that incense was "silently winked at."

---

## §3 — WHETHER IT STILL STANDS

### VERDICT: **VERIFIED** — it stands, unamended, and it is now conspicuous

### The current text

**Canon 40, Chapter IX of the Constitution of the Church of Ireland**, as
published by the Church of Ireland itself:

> **40. Use of incense forbidden**
>
> No incense or any substitution therefor or imitation thereof shall at any time
> be used in any church or chapel or other place in which the public services of
> the Church are celebrated.

**Word for word identical to 1878.** The only changes in a century and a half are
the removal of the commas, the lower-casing of "Public Services," and the canon
number (38 → 40).

### ⭐ WHAT MOVED AROUND IT — THIS IS THE FINDING

Every neighbour of the incense canon has been relaxed. The incense canon has not.

| 1878 | Now | Change |
|---|---|---|
| C. 36 — **no cross** on or behind the Table, "ornamental or otherwise" | C. 39 — **a cross MAY be placed** on or behind the Table, by faculty with incumbent and select vestry consent | **REVERSED** |
| C. 39 — **unlawful to carry any cross, banner, or picture** in procession; no processions as rite or ceremony | C. 41 — **processions permitted** at opening and close; **lawful to carry a cross**; lawful to carry a flag, banner or picture with the incumbent's consent | **REVERSED** |
| C. 35 — **no lighted lamps or candles** | **no counterpart canon** | **GONE** |
| C. 37 — no **wafer bread** (absolute) | C. 13(5) — wafer bread prohibited **except** in illness for intinction | **RELAXED** |
| C. 37 — no **mixed chalice** | **no counterpart** | **GONE** |
| C. 37 — no **elevation** | C. 13(4) — retained, plus a new ban on ringing bells | **RETAINED** |
| C. 5 — north side; back not turned | C. 13(3) — shall not stand with backs to the people when offering public prayer | **RETAINED in substance** |
| C. 4 — surplice, black scarf; no other vestment | C. 12 — cassock permitted; "**black scarf or a stole**"; no other vestment; **and a new clause 12(4) disclaiming any doctrinal significance in the apparel** | **RELAXED** |
| **C. 38 — no incense, absolute** | **C. 40 — no incense, absolute** | **UNCHANGED** |

**⭐ Incense is the last absolute survivor of the 1871 anti-ritualist code.** The
cross came back in 1964; processions and the sign of the cross in 1974; candles
in 1984 (all three dates from Ford, SECONDARY, and **not primary-verified by this
pass**). Incense alone was never touched.

### The dates, and how far they are sourced

- **1964** — the cross ban revised (Ford, p. 588-589 and abstract). SECONDARY.
- **1971-1974** — general revision of the canons by a committee chaired for its
  first two years by Bishop Richard Hanson; approved by General Synod 1974. Ford,
  p. 590. **On incense, Ford p. 591 verbatim: "Other prohibitions, however, on
  the use of incense, candles on the altar, and the elevation of the host, were
  retained."** SECONDARY.
- **May 1984** — candles ban removed (Ford, p. 591). SECONDARY.
- **Present** — Canon 40 as quoted above. **PRIMARY** (the Church's own
  publication of its own Constitution).

### ⚠️ THE PRAYER BOOK HALF OF THE QUESTION — UNMATCHED

The brief asks whether the provision survives "in the current law **and Prayer
Book**." The law half is verified. **The Prayer Book half is not established by
this pass**, for a reason that partly dissolves the question: the canons were
never part of the Prayer Book's own contents even in 1878, and today they live in
the Constitution, which is a separate document from the 2004 Book of Common
Prayer. **This pass did not examine the 1926 or 2004 Prayer Books.** No claim is
made about them either way.

### ⚠️ WHAT COULD NOT BE OBTAINED

The authoritative Constitution Chapter IX PDF at
`ireland.anglican.org/cmsfiles/pdf/Information/Constitution/09.pdf` — which
would normally carry amendment footnotes giving the enacting synod for each
clause — **could not be retrieved**: direct fetch returned an empty body, and the
browser attempt was stopped by a Cloudflare bot-verification interstitial. The
amendment dates above therefore rest on a secondary source. **Owed work.**

---

## §4 — JURISDICTIONAL STANDING

### VERDICT: **PARTIAL** — (a) and (c) verified from primary sources; (b) only half answered

### (a) The legal relation before 1871, and what the 1869 Act changed

**Before:** the Churches of England and Ireland were **one established church**,
united by Act of Parliament — Article Fifth of the Acts of Union of 1800. The
Irish Church Act 1869 describes what it was undoing in its own preamble,
verbatim: *"the union created by Act of Parliament between the Churches of
England and Ireland, as by law established."* Ford's characterisation of the
practical consequence (p. 580, SECONDARY): the Church of Ireland had "since the
Act of Union been bound by those [canons] of the Church of England."

**⛔ ARTICLE FIFTH'S OWN WORDING IS NOT IN HAND AND IS NOT SUPPLIED HERE.** On
legislation.gov.uk the revised text of Article Fifth prints only the Church of
Scotland clause; the words creating the united Church of England and Ireland are
marked **repealed by the Statute Law Revision Act 1953** and are not shown. The
parallel Great Britain Act of 1800 is available on that site as a scanned PDF
only. **Cite the 1869 Act, not Article Fifth, until Article Fifth has been read.**

**What the 1869 Act changed** — three sections, all verbatim from the "as
enacted" text:

**s. 2, the separation.**
> On and after the first day of January one thousand eight hundred and
> seventy-one the said union created by Act of Parliament between the Churches
> of England and Ireland shall be dissolved, and the said Church of Ireland,
> herein-after referred to as "the said Church," shall cease to be established
> by law.

**s. 19, the power that produced the canons.** Repeals every law and custom
preventing the bishops, clergy and laity from "holding assemblies, synods, or
conventions … for the purpose of making rules for the well-being and ordering of
the said Church," and from "framing constitutions and regulations for the general
management and good government of the said Church."

**⭐ s. 20, what kind of thing the canons then are.**
> The present ecclesiastical law of Ireland, and the present articles, doctrines,
> rites, rules, discipline, and ordinances of the said Church, with and subject
> to such (if any) modification or alteration as after the first day of January
> one thousand eight hundred and seventy-one may be duly made therein according
> to the constitution of the said Church for the time being, **shall be deemed to
> be binding on the members for the time being thereof in the same manner as if
> such members had mutually contracted and agreed to abide by and observe the
> same** … but nothing herein contained shall be construed to confer on any
> archbishop, bishop, or other ecclesiastical person **any coercive jurisdiction
> whatsoever**.

And the Act's own definition: *"'Jurisdiction' shall mean legal and coercive
power, and shall not extend to or include any power or authority which may be
exercised in a voluntary religious association, upon the footing of mutual
contract or agreement."*

**s. 21** abolished the Irish ecclesiastical courts and provided that "the
ecclesiastical law of Ireland, except in so far as relates to matrimonial causes
and matters, shall cease to exist as law."

**⭐ The consequence for how Canon 38/40 may be described.** From 1 January 1871
it is **the internal law of a voluntary religious association**, binding its own
members as if by mutual contract. It is not, and since 1871 has never been, state
law, and its makers were given no coercive jurisdiction. Calling it
"confessional-level," as §8 does, is a stretch in one direction and an
understatement in another: it is not a confession of faith, but it *is* an
enactment of the church's supreme legislative body carrying a stated penalty of
suspension or deprivation.

### (b) A distinct province of the Anglican Communion, and from when?

**Half verified.** The Anglican Communion Office lists the Church of Ireland as a
**member church**, with an Archbishop of Armagh (Primate of All Ireland and
Metropolitan), an Archbishop of Dublin & Glendalough, a Provincial Secretary, and
eleven dioceses. It is autonomous and self-governing. **PRIMARY-ish** (the
Communion's own secretariat).

**⛔ "FROM WHEN" IS UNMATCHED.** The ACO page gives no date of admission and no
founding instrument, and the Communion has none — it has no constitutive treaty.
The two datable facts in hand are the legal separation of 1 January 1871 (1869
Act s. 2) and the fact that the Lambeth Conferences begin in 1867 — **the latter
not verified by this pass and stated only as the place to look.**

**⚠️ TERMINOLOGY TRAP.** "Province" is used two ways and conflating them will
produce a false sentence. In Communion usage a member church is loosely called a
province (the ACO's own URL is `/province/ireland/`). *Internally* the Church of
Ireland has **two** ecclesiastical provinces, Armagh and Dublin.

### (c) Force in the Church of England or the American Episcopal Church?

### **NONE. EVER. AND THE NEGATIVE IS POSITIVELY GROUNDED.**

This is not an argument from absence. The 1869 Act's own terms establish it:
s. 19 authorises rules "for the well-being and ordering of **the said Church**";
s. 20 makes them binding "on the **members** for the time being thereof"; and the
Act's definition of jurisdiction expressly excludes anything exercised "in a
voluntary religious association, upon the footing of mutual contract." **A Church
of Ireland canon is by construction an instrument of internal association law.**
It has never bound a Church of England parish or a PECUSA/TEC parish, and could
not have, before or after 1871 — before, because there were no separate Church of
Ireland canons at all (the united church used the English ones); after, because
the Act that let the Church of Ireland make canons confined them to its own
members.

Ford adds, from the other direction and unprompted (SECONDARY, p. 591): the 1871
ritual canons were "a unique experiment in the Anglican communion," and on p. 589
records the argument used in the 1964 debate that "The Church of Ireland was
alone among the twenty churches in the Anglican communion" in banning the cross.

### ⭐ WHAT THE PROHIBITION CAN AND CANNOT BE CITED FOR

**CAN be cited for — and this is a real and defensible claim:**

> **An Anglican church, immediately on gaining the freedom to legislate for its
> own worship, prohibited incense outright, by canon, with a stated penalty of
> suspension or deprivation — and has kept that prohibition unamended for over a
> century and a half, through three revisions in which it relaxed or abandoned
> nearly everything standing beside it.**

That is the strongest honest form. Its force is not "an Anglican formulary
forbids incense." Its force is: **the "Anglican formularies exclude incense"
reading is not a Puritan import, because an Anglican church holding the same
formularies read them that way the moment it was free to say so** — and, unlike
the 1899 Lambeth Opinion, this one was never repealed, never overtaken, and
never even amended.

**CANNOT be cited for:**

- ⛔ **"An Anglican prayer book prohibits incense."** It is a canon, and the 1878
  volume's own contents page does not list the canons among the book's contents.
- ⛔ **Anything about what the Church of England held.** The Church of England
  never enacted this and never could have been bound by it. **This is the
  distinction the brief asked to be stated plainly, and it is the distinction
  §8's framing collapses.** The 1899 Lambeth Opinion is the Church of England
  evidence; the Church of Ireland canon is *a different Anglican church's*
  evidence. They corroborate each other; neither is the other.
- ⛔ **Anything about the American Episcopal Church**, which fought its own
  ritualism battle under the 1874 canon and never prohibited incense by name.
- ⛔ **"The Anglican tradition prohibits incense."** Ford's word for the ritual
  canons is *unique*, and that cuts both ways: it establishes that one Anglican
  church did prohibit incense outright, and in the same breath establishes that
  no other one did.

**⚠️ THE COUNTER JD SHOULD EXPECT, AND SHOULD PRE-EMPT RATHER THAN MEET.** An
informed Anglo-Catholic will say: *the same code banned the cross behind the
altar, which every Anglican church in the world permitted, and the Church of
Ireland itself repealed that in 1964. This is not the Anglican formularies
speaking; this is Victorian Irish Protestant party feeling, and they have been
walking it back ever since.* **That is a good answer and it is largely correct.**
The honest reply is the one the evidence supports: yes — and the incense clause
is the one they never walked back, in three separate revisions that touched
everything around it, including the ones that made them, in Ford's phrase, "the
laughing-stock of the Anglican communion." **The survival of Canon 40 through
1964, 1974 and 1984 is the finding, not the enactment of Canon 38 in 1871.**

---

## OWED WORK

1. **⭐ `src/Book_of_Common_Prayer_(Church_of_Ireland,_1878).pdf` is a new source
   in `src/` and is registered NEITHER in `SRC_Manifest.md` NOR in
   `PROJECT_STATE.md` §4.** Recorded here as owed, not done — this pass was
   read-only.
   - **file size:** 19,607,519 bytes
   - **page count:** 514 PDF pages
   - **sha256:** `f7af8e01b212142a526e50c71b5bcbfd7f33052c6fa9fd748cc9c6b75f6b9d75`
   - provenance: Google Books scan of a Bodleian copy (accession stamp visible
     on PDF p. 10); PDF Producer "Google Books PDF Converter (rel 3 12/12/14)".
     The Google Books id for the 1878 Church of Ireland BCP is `_cMUAAAAQAAJ`
     (per the Wohlers BCP bibliography at justus.anglican.org, SECONDARY).
2. **`RJ_Incense_Analysis.md` §8, the CONFESSIONAL-LEVEL PROHIBITION bullet,
   requires correction.** Three separate errors: the instrument (canon, not
   prayer book), the quotation's source (the modern canon, not the 1878 book),
   and "therefore" for "therefor." **Not edited by this pass.** Note that §8
   already carries a dated correction from 260835-35 under an authorisation
   expressly limited to the Elphinstone/Purchas bullet; a fresh authorisation is
   needed.
3. **The Constitution Chapter IX PDF** must be obtained to source the amendment
   dates (1964, 1974, 1984) from primary record. Cloudflare-blocked this pass.
4. **The 1871 vs 1877 question.** Ford dates the ritual canons entirely to
   April-May 1871 and never mentions 1877; the 1878 volume's heading says "1871
   and 1877" and prints a separate group headed "ADDITIONAL CANONS, 1877."
   Probable reconciliation: canons 1-48 are of 1871, the Additional Canons of
   1877. **Not confirmed.** The sources to settle it, from Ford's own note 37:
   *The Statutes Passed in the General Synod of the Church of Ireland 1871*
   (Dublin: Edward Purdon, 1874), 8-9, 18-19; and Bray, *The Anglican Canons*,
   lxviii, 838-856.
5. **Article Fifth of the Acts of Union 1800** — original wording not obtained;
   the united-church words are repealed out of the revised text and the as-enacted
   GB Act is a scanned PDF on legislation.gov.uk.
6. **Where clerical discipline for canon-breach now sits.** Current Canon 43 is
   headed "Penalty for wilful breach of any Canon" but on its face addresses only
   **lay** members. Chapter VIII (ecclesiastical tribunals) is the obvious place
   and was not examined. **Do not assert that clergy are now unpenalised.**
7. **The 1926 and 2004 Church of Ireland Prayer Books** were not examined.
8. **Canon 48's opening clause** ("THE General Synod of the Church of Ireland,
   lawfully") is a reconstruction from a scrambled extraction; re-read PDF p. 502
   right column, foot, before quoting it.
9. **1878 Canon 4's bracketed words** ("vesture", "Order") are reconstructions
   from the column crop and were not re-read from the page image.

---

## FILES WRITTEN (all in `~/EMC/staging-69`)

| File | Contents |
|---|---|
| `Church_Of_Ireland_Incense_Prohibition.md` | This report. §1-§4 with verdicts. |
| `SRC_PRIMARY_1878_ChurchOfIreland_BCP-Volume_Constitutions-and-Canons-Ecclesiastical_Canons-33-40-48_pdf-pp495-504.txt` | The 1878 volume: title page, adoption line, Canons 4, 35, 36, 37, **38**, 39, 40, 47, 48 verified by dual extraction; raw column crops retained; the full "Contents of this Book" list; the search record establishing the negative. |
| `SRC_PRIMARY_2026_ChurchOfIreland_Constitution-Chapter-IX_Canons-2-5-12-13-38-43_Current-Text.txt` | Current Canon 40 verbatim with a 1878/2026 word-comparison, plus the surrounding ceremonial canons as they now stand, plus the recorded absence of any candles canon. |
| `SRC_PRIMARY_1800-1869_UnionWithIreland-Act-Art-5_and_Irish-Church-Act-1869_ss1-2-19-20-21.txt` | Irish Church Act 1869 preamble and ss. 1, 2, 19, 20, 21 verbatim; the Article Fifth gap recorded honestly; Anglican Communion Office listing. |
| `SRC_SECONDARY_2022_Ford_Church-of-Ireland-Ritual-Canons-1871-1974_ChurchHistory.txt` | ⛔ SECONDARY. Ford, *Church History* 91/3 (2022): 575-595. Every incense passage; adoption context; amendment dates 1964/1974/1984; the enforcement record; the 1871-vs-1877 discrepancy flagged. |

---

**Sources**

- `src/Book_of_Common_Prayer_(Church_of_Ireland,_1878).pdf` (repo, read-only)
- [The Canons of the Church of Ireland](https://www.churchofireland.org/our-faith/the-canons)
- [Irish Church Act 1869, as enacted](https://www.legislation.gov.uk/ukpga/1869/42/enacted)
- [Act of Union (Ireland) 1800](https://www.legislation.gov.uk/aip/Geo3/40/38)
- [The Church of Ireland — Anglican Communion Office](https://www.anglicancommunion.org/province/ireland/)
- Alan Ford, ["The Cost of Democracy: The Church of Ireland and Its Ritual Canons, 1871–1974"](https://doi.org/10.1017/S000964072200213X), *Church History* 91, no. 3 (2022): 575–595 — **SECONDARY**
- [The Book of Common Prayer of the Church of Ireland](http://justus.anglican.org/resources/bcp/Ireland.htm) (Wohlers bibliography) — **SECONDARY**, used only for the Google Books identifier
