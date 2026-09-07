# Ritual Canon Examples, and Ritualism in the REC Split

**STAMP: 260835-62.** ASSIGNED BY BRIEF, NOT DERIVED. No stamp registry was
read and no stamp was derived, per instruction.

**Mode:** READ-ONLY against `~/EMC/theology`. All output written to
`~/EMC/staging-62`. Nothing created, edited, moved or deleted in the repository;
no git write command run; no git lock taken. Read-only git commands used
`--no-optional-locks`.

**Repo HEAD at start and at finish:** `82a4fe0e07854996a4343096045bebfef6f90da7`
("260835-60: post-1900 authorization of liturgical incense"). Matches the
`82a4fe0` given in the HANDOFF. Working tree clean at start.

---

## §0. Two divergences between the brief and the repo, recorded before anything else

Per the standing rule that a recorded convention in the repo overrides an
instruction in the brief, and the instruction not to trust figures stated in the
brief:

**(0.1) `Ritual_Canon_1874_To_1904.md` does not exist and never has.** The brief's
READ FIRST list names it "(in the repo root)". It is absent from the working
tree, absent from `git ls-files`, and absent from the entire commit history
(`git log --all --diff-filter=A --name-only` for `Ritual_Canon`: no matches). The
nearest actual file is `Ritualist_Case_For_Incense_and_the_1899_Opinion.md`,
which is a different document on a different subject. **This pass proceeded on
the three `src/` files, which do exist and were read in full.** If a document by
that name exists outside the repo, this pass did not see it, and any assumption
the brief was carrying from it has not been checked here.

**(0.2) The White & Dykman passage is captured, but the brief mis-quotes it by
one word.** The brief renders it "the very existence of the Church". The captured
text reads **"had threatened almost the very existence of the Church"**. The
word *almost* is in the original and is doing real work. Located at
`src/SRC_PRIMARY_1904-2018_TEC_Ritual-Canon-Repeal_and_BOS-Incense-Form.txt`,
EXCERPT 2.3, where it is already correctly labelled **PRIMARY-ADJACENT** and
sourced to White & Dykman vol. 1 (1954) p. 411 under the running head "CANON 21",
sub-heading "CONVENTION OF 1904". The brief's characterization of it as an
annotator's language written eighty years later is confirmed by the repo's own
capture note.

---

## §1. ITEM 1 — The four examples as passed by the Deputies

### VERDICT: **VERIFIED**, with two corrections to the brief's figures.

The American church, in a formal recorded vote of one House, adopted a clause
which declared the use of incense to be an instance of a ceremony "setting forth
or symbolizing erroneous or doubtful doctrines". The examples were not attached
on a looser footing. They were attached to the doctrinal test itself, and the
leading opponent of the canon understood them that way on the floor and said so.

### 1(a) The full text of the clause as passed

From the Journal, House of Deputies, resolution of the Committee on Canons as
reported 23 October and adopted 27 October 1874 (repo capture extract A, printed
pp. 108-109; identically re-printed as received by the Bishops in Message No. 43,
extract E, printed pp. 320-321):

> § II [1.] If any Bishop have reason to believe, or if complaint be made
> to him in writing by two or more of his Presbyters, that ceremonies or
> practices during the celebration of the Holy Communion, not ordained or
> authorized in the Book of Common Prayer, **and setting forth or symbolizing
> erroneous or doubtful doctrines**, have been introduced into a parish wnthin
> his jurisdiction (**and, as examples, the following are declared to be
> considered as such:**
>
> a. The use of Incense.
>
> h. The placing, or carrying, or retaining a Crucifix in any part of the place
> of public worship.
>
> c. The Elevation of the Elements in the Holy Communion in such manner
> as to expose them to the view of people as objects toward which adoration is
> to, be made.
>
> d. Any act of adoration of or toward the Elements in the Holy Communion
> such as bowings, prostrations, genuflections, and all such like acts not
> author- ized or allowed by the Rubrics of the Book of Common Prayer), it shall
> be the duty of such Bishop to summon the Standing Committee as his Couneil of
> Advice, and wdth them to investigate the matter.

(OCR as read in the repo capture; "wnthin", "wdth", "Couneil", and the "h." for
"b." are the OCR's, not mine.)

### 1(b) Where the examples sat structurally — the load-bearing question

**Incense was named as an instance of the conjunctive doctrinal test, not on a
looser footing.**

The grammar settles it. The antecedent of "such" in "declared to be considered
as such" is the whole preceding description: ceremonies or practices which are
(i) not ordained or authorized in the Book of Common Prayer **and** (ii) setting
forth or symbolizing erroneous or doubtful doctrines. The parenthesis opens
immediately after that description and before the apodosis ("it shall be the duty
of such Bishop"). There is no intervening antecedent for "such" to attach to.

This is not merely my reading of the grammar. **De Koven read it the same way on
the floor, and staked his speech on it** (`SRC_PRIMARY_1874_DeKoven_...`, speech
of 26 October 1874):

> That is, it does not simply forbid the use of incense—I wish that were all.
> What it does is to say that the use of incense symbolizes erroneous or doubtful
> doctrines, which is a dreadful thing to commit this House to. For this House to
> forbid the use of incense is a very proper thing, perhaps; but for this House
> to say that the use of incense symbolizes false doctrines, is for this House to
> put itself in utter and total opposition to the Holy Scriptures...

And **De Koven confirmed the same reading retrospectively on 31 October**, after
the examples had been struck, in his remarks printed in the same pamphlet:

> In the next place, there are two specifications left out, which said that the
> use of incense and the use of the crucifix symbolized false doctrine.

So the structural claim is not an inference this project is imposing. It is how
the canon's most conspicuous opponent characterized it, twice, on the record,
both before and after the vote.

⭐ **Note for the live exchange, flagged and not developed here.** De Koven's
26 October argument is, in substance, RJ's argument: that to forbid incense on
prudential grounds is permissible ("a very proper thing, perhaps") but to declare
it symbolic of false doctrine sets the Church "in utter and total opposition to
the Holy Scriptures", the Scriptures then adduced being Psalm 141, Malachi 1:11,
Numbers 16, and Leviticus 16. **Per the standing rule that his own example
outranks the project's version of it** — this is a case where the argument
already exists in a named Anglican's words, in an American General Convention, in
1874. What the record then shows is that the House of Deputies heard that
argument and adopted the clause anyway, the next day, and that De Koven himself
voted Nay. Whether and how to deploy that is a question for JD, not for this
pass. It is recorded, not drafted.

### 1(c) The exact vote, the date, and the Journal page

Journal, House of Deputies, 18th Day, **Tuesday 27 October 1874**, printed
pp. 143-145 (repo capture extract D). Vote by Dioceses and Orders, called for by
the Deputation from Tennessee:

| Order | Dioceses represented | Ayes | Nays | Divided |
|---|---|---|---|---|
| Clergy | 41 | **38** | **2** | 1 |
| Laity | 39 | **35** | **3** | 1 |

"The resolution reported by the Committee was therefore adopted." (printed p. 145)

Negative, clerical: Albany; Michigan (Brown, Worthington Nay; Gillespie Aye).
Negative, lay: Albany; New York (Livingston, Davies Nay; Ruggles Aye); Vermont.
Divided: Indiana (clerical); New Jersey (lay).

Wisconsin clerical entry, printed p. 144: "The Rev. Dr. Adams, and the Rev.
Messrs. Half and Ten Broeck. — Aye. **The Rev. Dr. DeKoven. — Nay.**"

**⚠ CORRECTION 1 TO THE BRIEF.** The brief says "the Deputies passed incense as
an example 38-2." Two things are wrong with that shorthand:

1. **38-2 is the CLERICAL vote only.** The lay vote was 35-3. Citing "38-2"
   without saying "of the clergy, by dioceses" misstates the record.
2. **There was no vote on incense.** The vote was on the Committee's entire
   resolution, which contained the doctrinal test, all four examples, and the
   whole enforcement machinery of subsections [2] and [3]. No deputy ever voted
   on incense as a separable proposition. The most that can be said — and it is
   still a great deal — is that the House adopted a resolution which named
   incense first among the examples, having heard De Koven argue the previous day
   that this was precisely what the clause did.

**⚠ CORRECTION 2 TO THE BRIEF.** The brief says the vote came "the morning after
DeKoven's speech." The speech was 26 October and the vote 27 October, so "the
next day" is right. **"The morning" is not established.** The Journal does not
record the hour. Do not deploy "the morning after" without a source for it.

Aycrigg (1880) gives the lay figure as 34, not 35. **The Journal governs.**
Aycrigg's vote figures are internally inconsistent (he prints 28 clerical at p.
156 against 38 at p. 74) and should not be used.

### 1(d) The Bishops' striking of the examples

House of Bishops, 20th Day, **Thursday 29 October 1874**, printed pp. 333-335
(repo capture extract F). On the motion of the **Bishop of North Carolina**:

> Resolved That § II. of the Canon on Ritual be amended by striking out the words
> beginning with " And as examples," and ending with " Book of Common Prayer."
>
> Which was adopted.

Communicated to the Deputies as **Message No. 63, 29 October 1874**, printed p.
171 (extract G), item 2: "To strike out in the same Subsection [1] all those
words inclosed within parentheses, beginning with the words 'and as examples,'
and ending with the words 'Book of Common Prayer.'"

**No reason is recorded, and no committee report accompanies the striking.** The
motion is a bare striking motion carried on the floor. The Journal records that
the Bishops' Committee on Canons had reported a resolution which was under
discussion (extract F opening line), but the striking was a floor amendment to
that resolution, not a committee recommendation, and the Journal gives no
rationale for it. Nothing else in the Bishops' proceedings that day supplies one:
the surrounding amendments are the Bishop of Albany's drafting changes, the
Bishop of Western New York's re-ordering of the doctrinal test, the Bishop of
Maryland's non-concurrence substitute (**not adopted**), and the Missionary
Bishop of Montana's motion to drop "or doubtful" (**not adopted**).

This is independently corroborated from the hostile side. Aycrigg (1880), an
REC-approved chronicle, printed p. 156:

> This proves that the Ritualists controlled the General Convention in some way
> that **can only be surmised, since the House of Bishops acts in secret**. ...
> But **the official report** shows these simple facts.

And the Ritualist correspondent in the New York Tribune, 14 November 1874, gives
the mechanics — "The latter struck their pen through. . . .the two. . .
.concerning crucifixes and incense" — and no reason either.

**⚠ CORRECTION 3, TO AYCRIGG AND TO ANY ACCOUNT DERIVED FROM HIM.** Aycrigg says
repeatedly that the Bishops struck *two* examples, incense and the crucifix. That
is wrong as a description of what the Bishops did. **They struck all four**, by
striking the entire parenthesis. The elevation and adoration clauses reappear in
the enacted canon only because the **Committee of Conference reinserted them**,
in altered wording and under a weaker formula — "(such as" rather than "and, as
examples, the following are declared to be considered as such:" — on 31 October
(extract H, printed p. 183). The brief has this right and Aycrigg has it wrong.
Recorded so the error is not inherited from the secondary literature.

The enacted canon contains **no occurrence of the word "incense"** (repo capture
extract J, which accounts for all five occurrences in the whole 1874 OCR).

### 1(e) Deputies other than De Koven connecting incense to the doctrinal test

**Within the Journal: none, and none is possible.** The Journal records motions,
messages and votes, not debate. This is stated in the repo capture's own header
and is confirmed by the fact that the only incense occurrences in the entire
Journal OCR are in the successive drafts of the canon plus one unrelated
missionary report.

**Outside the Journal: yes — and this pass located the record that supplies it.**

The contemporary verbatim stenographic report of the debate exists: **"Debates of
the House of Deputies in the General Convention ... 1874", reported for The
Churchman, Hartford: M. H. Mallory & Co.** — IA item `debatesofhouseof00epis_0`.
This volume was not previously in the project's possession and supplies what the
Journal omits. Captured in this staging folder.

**Mr. ANDREWS, of Ohio** (lay deputy), 27 October 1874 — the day of the vote —
independently verified in this pass by exact-phrase query:

> Suppose that this Conven- tion, expressly or impliedly, were to give voice to
> the opinion that incense' in the a(Sninistration of the Holy Communion is
> admissible, and on Christmas next, throughout all the length and breadth of
> this land ... sm-pliced boys enter these chancels and wave the censer, what do
> you suppose the effect in this Chm'ch would be ? ... I do not know what it
> would be here in New York ; I cannot tell : but throughout thi^ whole
> continent west of this city, if that one thing was authorized and it was un-
> derstood that this Church had committed itseK deliberately to it, I know well
> that it would break up this Church, and this Convention would never sit again.

**Rev. Dr. HALL, of Long Island**, 27 October 1874, also independently verified:

> Outside of this building it is perfectly well understood w'hat the Canon means.
> It means either the downfall or the victory of Ritualism.

**How much weight Andrews will bear — read this before deploying him.** Andrews's
statement is a **conditional**, and doubly hedged. He does not say incense as
then practised was breaking up the Church. He says it would break up **if** the
Convention "expressly or impliedly" declared incense admissible **and** that
authorization were acted on nationally — and he expressly excepts New York from
his prediction. Nobody proposed such an authorization and the Convention moved
the other way. Aycrigg's widely-circulating version silently drops both the
geographical qualifier and half the conditional, converting a hedged hypothetical
into something close to a flat prediction. **Quote the Debates text, not
Aycrigg's.**

So on 1(e) specifically: Andrews connects incense to the *effect on the Church*
and objects to "indirect teaching by symbols and not words"; he is not a second
witness to the *doctrinal-symbolism* reading in the way De Koven is. De Koven
remains the clearest and most explicit voice on that precise point.

---

## §2. ITEM 2 — Provenance of the "very existence of the Church" passage

### VERDICT: **UNMATCHED.**

No contemporary source, 1871-1880, characterizes the American ritual controversy
in a register comparable to White & Dykman's. The characterization is White &
Dykman's own.

**What the passage can be cited for:** that a mid-twentieth-century official
annotator of the Constitution and Canons understood the 1871 and 1874 ritual
fight to have been the gravest crisis of the period, and recorded that the canon
was repealed in 1904 without a voice raised in its defence — the repeal fact
being separately supported by the 1904 Journal capture already in the repo.
**What it cannot be cited for:** that anyone at the time said so, or that the
Church's existence was in fact at stake. It is an annotator's retrospective
judgment written eighty years after the events, and the contemporary record runs
against it.

### The search record

Corpora swept in full, by regex over complete OCR text (not by the IA
`inside.php` endpoint alone, which was demonstrated in this pass to under-report
— it returned zero hits for `imperil` in the 1874 Journal where the OCR has two):

| Source | IA identifier |
|---|---|
| Journal of the General Convention, 1874 | `journalofproceed1874phil` |
| Journal of the General Convention, 1871 | `journalofproceed1871epis` |
| Debates of the House of Deputies, 1874 | `debatesofhouseof00epis_0` |
| Debates of the House of Deputies, 1871 | `debateshousedep00churgoog` |
| Pastoral Letter of the House of Bishops, 1871 | `pastoralletterto00epis_0` |
| Pastoral Letter of the House of Bishops, 1874 | anglicanhistory.org (from *The Church Journal*, 19 Nov 1874) |
| Pastoral Letter of the House of Bishops, 1877 | anglicanhistory.org |
| Aycrigg, *Memoirs of the REC*, 1880 | `memoirsofreforme00aycr` |
| American Church Review, vols. 24, 26, 27, 30/1 | `sim_church-review_*` |

**1874 Journal — zero occurrences of:** "existence of the Church", "existence of
this Church", disruption, disrupt*, rupture, asunder, "break up", "broken up",
"divide this Church", "destroy this Church", "rend the Church", calamity,
convulsion, catastrophe, crisis, secession, revolt, anarchy, shipwreck,
imperiled, jeopard, hazard, survival, "preserve the Church", "save the Church",
disorganiz*, agitation, excitement, fatal, gravest, momentous, "integrity of the
Church", "life of the Church", "Reformed Episcopal".
Non-zero but examined and irrelevant to ritual: peril 7, imperil 2, danger 10,
destroy 1, overthrow 1, "very existence" 1 (the Church Building Society),
dissolution 27 (**all** "dissolution of the pastoral connection"), dismember 4
and threaten 3 (**all** the provincial-system debate).

**1871 Journal — zero occurrences of:** "existence of the Church", disruption,
rupture, asunder, "break up", dismember, imperil, convulsion, catastrophe,
secession, agitation, momentous, "peace and unity".
Non-zero and irrelevant: crisis 4 (Irish disestablishment ×2, the Vatican
Council, a Commission report), calamity 18 (**all** the Chicago fire), peril 3,
"very existence" 1 (the infant Church in Africa).

**1871 Pastoral Letter — zero occurrences of:** existence, crisis, calamity,
convulsion, threaten, destroy, break, divide, asunder, disrupt, rend, ruin,
overthrow, dissol*, separat*, secession.

**Not located:** the pamphlet "Church Freedom" (16 pp., REC, 38 Bible House, New
York), which reprints the Tribune "Ritualist" letter of 14 Nov 1874. Not on the
Internet Archive; `title:"church freedom"` returns six unrelated items.
**Not runnable:** a whole-archive phrase sweep. Both `ia-fts.archive.org` and the
`services/search/beta/scrape.json` endpoints are closed to programmatic access.

### Why the negative is strong rather than merely empty

Four findings, in ascending order of force:

**(i) The Bishops never said it, in the one document that would count.** The 1871
Pastoral Letter is the document the 1874 House of Bishops expressly adopted as
"its own action" on ritual. Its ritual section puts the peril on *the souls of
men*: "if a teacher suggests this error, by act or posture, he places himself in
antagonism to the doctrine of this Church, and the teaching of GOD'S Word, and
puts in peril the souls of men." Ritualism is "mainly a question of taste,
temperament, and constitution, until it becomes the expression of doctrine" —
verified in this pass by exact-phrase query. The word *existence* does not occur
in the document.

**(ii) The 1874 and 1877 Pastoral Letters do not raise ritual at all.** Reported,
not independently verified in this pass — flagged in the capture file as
requiring verification. If confirmed, the Bishops' pastoral at the close of the
very Convention W&D describe passes over the subject in silence.

**(iii) The register was available and in use in 1874 — against provinces.** Mr.
Ruggles of New York, on the provincial system: "the proposition can lead to
nothing but disruption, dismemberment and total ruin"; "the ruin of this Church
would be a greater calamity to mankind than the r[u]in of the Union itself." The
Committee on Amendments to the Constitution, Journal 1874 pp. 150-151: "Such a
system would dismember this Church". These men reached for the strongest language
they had, days after the ritual debate, on a different question. Their restraint
on ritual was a choice, not a limit of vocabulary. *(Reported; not independently
verified — recorded as LEADS in the Debates capture.)*

**(iv) Where the register does appear on ritual, it is in the mouths of men
reporting it in order to disown it.** The 1871 Committee on the State of the
Church: "we cannot but rejoice in the fact that in this great Triennial General
Council the strife has been not, **as so many predicted**, to destroy our goodly
heritage and devour one another". Dr. Sullivan of Illinois: "**we are told** that
... in the end it would split and break up the Church." The Chairman of the
Committee on Canons: "the public, **who suppose** we are goin[g] to be split into
ten thousand pieces by these subjects; but I do not believe we shall lose a hair
b[y] them." De Koven: "I have never heard that it was going to make a crisis in
the Church."

That last group is the most useful thing in this section. It establishes that the
"this will break up the Church" register **was circulating** in 1871-1874, among
the public and in the press, and that the men inside the Convention repeatedly
named it in order to reject it. White & Dykman's sentence preserves the register
of the outside prediction and reports it as the fact of the matter.

### The three nearest contemporary approaches, ranked

1. **American Church Review, "The Illinois Case," vol. 27 (1875), pp. 236-237.**
   PRIMARY. "And the result is pretty sure to be at no distant day, a break up of
   the General Convention. **This might be borne, for the General Convention is
   not the Church**, which had its being long before it was heard of, and may as
   much outlast it." — the closest approach, and it refuses the last step
   explicitly, drawing exactly the distinction W&D collapse.
2. **Mr. Andrews of Ohio**, 27 Oct 1874. PRIMARY, verified. A doubly-hedged
   conditional; see §1(e).
3. **Bishop H. W. Lee**, Iowa Convention 26 May 1874, via the Hartford Churchman.
   SECONDARY at two removes. "would eat out its very vitals as a Reformed and
   Primitive Church, and sap its foundations as an Apostolic body" — destruction
   of *character*, not of existence.

### Verification caveat on §2

The corpus sweep in this section was carried out by a delegated search agent and
is reported here largely on that basis. Three load-bearing items were
independently re-verified by me in this pass: the 1871 Pastoral Letter's "question
of taste" formula, the Andrews speech, and the Hall speech. **The remainder of the
negative record — in particular the reported contents of the 1874 and 1877
Pastoral Letters, and the Ruggles/Fulton/Sullivan/Huntington passages — has not
been independently confirmed and is flagged as such in the capture files.** The
UNMATCHED verdict rests principally on the verified 1871 Pastoral Letter finding
and on the two Journals' zero-hit records, which are the strongest legs.

---

## §3. ITEM 3 — Ritualism and incense in the Reformed Episcopal split

### VERDICT: **PARTIAL.**

- **Ritualism IS named as a cause** — explicitly, in the withdrawal letter's own
  numbered reasons. **VERIFIED.**
- **Incense is NOT named anywhere** in the founding documents. **FALSIFIED**, as
  to incense.
- **The proximate occasion is more complicated than the popular account**, and
  the founding documents do not say what that account says. **PARTIAL.**

### 3(a) Is ritualism named as a cause, and in what terms?

**Yes.** Three loci, all in documents rather than in narrative. The first was
independently re-verified in this pass by exact-phrase query.

Withdrawal letter, reason "First" (10 November 1873):

> you well know how heavy has been the trial of having to exercise my office in
> certain churches in the dio cese of Kentucky, **where the services are
> conducted so as to symbolize and to teach the people doctrines subversive of
> the ' truth as it is in Jesus,'** ... I have been most painfully impressed by
> the conviction that 1 was sanctioning and indorsing by my presence and official
> acts **the dangerous errors symbolized by the services customary in Ritualistic
> churches.**

Withdrawal letter, reason "2":

> The only true remedy, in my judgment, is the judicious yet thorough revision of
> the Prayer Book, eliminating from it all that gives countenance, directly or
> indirectly, to **the whole system of Sacerdotalism and Ritualism**.

Reply to Dr. Tozer, New York Tribune, 13 October 1873:

> When the Episcopal Church of England and the United States has been able to
> clear herself ... of **the deadly evil of Ritualism, whose last development is
> the revival of the Confessional**...

**But note precisely what Cummins means by it.** The content he attaches to
"Ritualism" throughout is **doctrinal symbolism** — services "conducted so as to
symbolize and to teach ... doctrines subversive", "the dangerous errors
symbolized by the services" — plus the Confessional. He objects to ceremonial
only as a *carrier of sacerdotal doctrine*. He never itemises the ceremonial acts.

And the other founding documents are even more doctrinal than the letter:
- **The Call** (13 November 1873) does not use the word "Ritualism" at all. It
  names "the errors of Sacerdo talism", Baptismal regeneration, "the Real
  presence ... in the elements", and "a Sacrifice offered by a priest".
- **The Declaration of Principles** (2 December 1873) does not use it either. Its
  Article IV rejects five propositions — one-polity exclusivism, sacerdotal
  priesthood, the Table as altar of oblation, presence in the elements, and
  baptismal regeneration — every one of them framed as a **doctrine**, not as a
  practice.

### 3(b) Is incense named anywhere? — **No. Plainly, no.**

Searched exhaustively and separately in four bodies of text:

**1. The Cummins Memoir (1878), complete OCR, 1,066,765 characters.** Searched
for `incens`, `cense`, `censer`, `thurib`, `ceremoni`, `vestment`.
- `incens` — **two** occurrences in the whole volume: printed p. 85, "covered
  with the sweet incense of the Saviour's intercession" (a devotional metaphor
  quoting Bickersteth on prayer), and printed p. 543, "indifferent or incensed
  laymen" (the adjective). **Neither falls inside any founding document.**
- `censer`, `thurible` — **zero** occurrences in the volume.
- `ceremoni-` — **zero** occurrences anywhere in the span covering the withdrawal
  letter, the Call, the Council proceedings and the Tozer reply (printed
  pp. 412-441).

**2. The REC Constitution and Canons (1878), complete OCR, 83,425 characters.**
- `incense`, `censer`, `thurible`, `ceremonial`, `ceremony`, `ceremonies` —
  **zero** occurrences.
- The only ceremonial-adjacent provision in the entire document is Constitution
  **Article IX**, side-noted "Ritualism Prohibited":
  > Nothing calculated to teach — **either directly or symbolically** — that the
  > Christian Ministry pos¬ sesses a Sacerdotal character, or that the Lord's
  > Supper is a Sacrifice, shall ever be allowed in the worship of this Church ;
  > nor shall any Com¬ munion Table be constructed in the form of an altar.
  A doctrinal test with **no enumerated examples**. The only physical object
  named in the whole Constitution is the Communion Table.

**3. Annie Darling Price's REC history (1902).** Every incense hit in the volume
is either (i) a quotation from *Protestant Episcopal* ritual-controversy
documents she reprints as background, (ii) a 1900 press account of the Fond du
Lac consecration, or (iii) rhetorical ("her principles are as sweet incense").
**None is from an REC founding document.**

**4. ⭐ Cummins's own 1876 itemisation of ritualist abuses** — the strongest
single negative, because it is the one place he descends from generalities to a
list. Speaking two and a half years after the founding, of Maryland:
> six Ritualistic churches established within the limits of a single city, with
> **altars and candles and strange vestments**, with **idolatrous prostration
> before material things**, with **auricular confession** constantly practised
> without rebuke, with **prayers for the dead** openly offered, and **the mass
> celebrated at funerals**, and with even the error painted upon the windows...

Altars, candles, vestments, prostration, confession, prayers for the dead, the
mass at funerals, painted legends. **No incense. No censers.** When Cummins
finally names names, incense is not among them.

### 3(c) The proximate occasion as the documents themselves state it

**The withdrawal letter gives three reasons in its own numbering, and the
Evangelical Alliance communion is the third and last of them**, introduced as
"One other reason for my present action remains to be given."

Reason **First** is Ritualism in his own diocese, framed as a standing cumulative
burden. Reason **2** is despair of remedy through Church authority — "I have lost
all hope that this system of error ... can be, or will be eradicated by any action
of the authorities of the Church, legislative or executive" — carrying the
constructive programme (return to the 1785 Prayer Book) which the Call and the
Declaration then execute. Reason **3** is the Alliance communion.

And note what Cummins says reason 3 actually *is*. It is not "I did this and it
was right", nor "I was attacked for it". It is that the consequences proved his
position untenable:

> The results of that participation have been such as to prove to my mind that
> such a step cannot be taken by one occupying the position I now hold without
> sadly disturbing the peace and harmony of ' this Church, ' and without impairing
> my influence for good over a large portion of the same Church.
>
> As I cannot surrender the right and privilege thus to meet my fellow-Christians
> of other churches around the table of our dear Lord, I must take my place where
> I can do so without alienating those of my own household of faith.

**Corroboration from the other two founding documents:** the Call never mentions
the Evangelical Alliance, Dr. Hall, or intercommunion. Neither does the
Declaration of Principles; its only trace of the intercommunion issue is Article
IV's first rejected doctrine, that the Church of Christ exists in only one form of
polity. Intercommunion returns in Cummins's presidential address, but as
**programme** ("we shall rejoice to meet them and their flocks ... around the
Lord's table"), not as grievance.

**⚠ The popular account tracks the biographer, not the documents.** The Memoir's
*narrative* frames the withdrawal as precipitated by the abuse Cummins suffered
after the communion service — "The storm of bitterness had not spent itself when
the great and momentous question arose in Bishop Cummins's mind, whether he could
longer remain in a church where he had been so harshly judged". Cummins's letter
never mentions the abuse, the attacks, or Tozer at all. The two layers are kept
separate and labelled throughout the capture file.

So the honest answer to the brief's question: on the documents' own terms, the
Alliance communion is the **precipitating occasion and the demonstration** — the
event that proved what reasons 1 and 2 had already made him fear — not the ground
of the withdrawal. The popular account is not simply wrong; it is a
foregrounding of the third reason at the expense of the first two.

### 3(d) The defensible formulation

The sentence *"it was among the issues behind the Reformed Episcopal split in
1873"* **must be narrowed before deployment.** Say instead, and only:

> **Ritualism was among the stated causes of the Reformed Episcopal secession of
> 1873 — Cummins's letter of withdrawal names "the dangerous errors symbolized by
> the services customary in Ritualistic churches" and "the whole system of
> Sacerdotalism and Ritualism." But the founding documents nowhere mention
> incense. What they object to is ceremonial that teaches sacerdotal doctrine —
> and where the REC does legislate, in Article IX of its Constitution, it
> prohibits by doctrinal test ("either directly or symbolically") and attaches no
> list of examples at all.**

**What must NOT be said:** that incense was among the issues behind the REC
split; that the REC condemned incense; or that the REC named incense as
symbolizing false doctrine. None of the three is supported, and the first is
positively contradicted by Cummins's own 1876 list.

**The genuinely interesting result, flagged and not developed.** The REC — the
body that left over ritualism — wrote a symbolic-doctrinal test into its
Constitution and named **no** ceremonies under it. The PEC House of Deputies
wrote an equivalent test and named **four**, incense first, and its House of
Bishops struck the list. Whether that contrast is worth anything in the live
exchange is JD's call. It is recorded here, not argued.

---

## §4. Owed work and unresolved gaps

Recorded so they are not lost, in rough order of how much they matter.

1. **The REC Book of Common Prayer of 1874** (IA `bookofcommonpray00refo`, open,
   642 images) **was not searched.** Its rubrics are where a ceremonial
   prohibition would most naturally sit. **This is the most significant gap in
   ITEM 3** and the finding at 3(b) should carry that qualification until it is
   closed.
2. **The 1874 first edition of the REC Constitution and Canons** (IA
   `constitutioncano00refo`) was not collated. Until it is, nothing can be
   claimed about when Article IX entered the Constitution or in what words. The
   1878 text is all this pass has.
3. **The Journal of the First General Council** (Philadelphia, 1873; HathiTrust
   full view, vol. id `wu.89077056000`) was not consulted. The Council
   proceedings here come from the 1878 Memoir instead. HathiTrust's page-text
   endpoints are session-gated and were not reachable programmatically.
4. **The 1874 and 1877 Pastoral Letters** were reported but not independently
   verified. Both bear on §2 and are flagged in the capture file.
5. **The Ruggles, Fulton, Sullivan, Huntington and McCrady passages** in the 1874
   Debates were reported but not independently verified. Recorded as LEADS with
   locations; **do not quote outward until verified.**
6. **Printed page numbers in the 1874 Debates** were not read off the running
   heads in this pass. The IA leaf numbers are recorded; the printed pages (225,
   244) are as reported and marked UNVERIFIED.
7. **The pamphlet "Church Freedom"** (REC, 38 Bible House, New York) was not
   located. It reprints the Tribune "Ritualist" letter of 14 November 1874.
8. **No byte offsets were logged** for any file written by this pass, and none of
   these captures has been registered in `SRC_Manifest.md` — correctly, since
   this pass is forbidden to write to the repo. Registration is owed at intake.

---

## §5. Files written by this pass

All in `~/EMC/staging-62`, top level, named to the repo's `SRC_` convention so
that intake is a plain file move.

| File | What it is |
|---|---|
| `Ritual_Canon_Examples_And_REC_Split.md` | This findings file. |
| `SRC_PRIMARY_1873_Cummins_REC-Founding-Documents.txt` | Withdrawal letter, the Call, Journal of the First General Council, Declaration of Principles, Tozer reply; plus the incense negative and the DOCUMENT/NARRATIVE divergence note. |
| `SRC_PRIMARY_1874_Debates-House-of-Deputies_Ritual-Canon-Speeches.txt` | Andrews of Ohio and Hall of Long Island, verbatim and verified, from the contemporary stenographic report; plus six unverified leads. |
| `SRC_PRIMARY_1871_House-of-Bishops_Pastoral-Letter-Ritual-Section.txt` | The ritual section of the letter the 1874 Bishops adopted as their own action, with its negative search record. |
| `SRC_PRIMARY_1878_ReformedEpiscopalChurch_Constitution-Canons-Ceremonial.txt` | Declaration of Principles as printed 1878, Constitution Article IX, and the exhaustive ceremonial-vocabulary search record. |
| `SRC_SECONDARY_1880_Aycrigg_REC-Memoirs_1874-Convention-Entries.txt` | Labelled SECONDARY. Aycrigg on the striking, the Tribune "Ritualist" letter, Bishop Lee; plus the correction to Aycrigg's two-vs-four error and the supersession notice. |

**END.**
