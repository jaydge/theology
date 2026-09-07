# The Register of the 1874 Dissent, and the Pamphlet Divergence

**STAMP: 260835-64.** ASSIGNED BY BRIEF, NOT DERIVED. No stamp registry was
read and no stamp was derived, per instruction.

**Mode:** READ-ONLY against `~/EMC/theology`. All output written to
`~/EMC/staging-64`. Nothing created, edited, moved or deleted in the repository;
no git write command run; no git lock taken. Read-only git commands used
`--no-optional-locks`.

**Repo HEAD at start and at finish:** `89960773f2e9bb8cccc7e80bb904cdc6f4f3607c`
("260835-62: the 1874 incense example and the REC split"). Working tree clean at
start and at finish.

**Files written this pass, both in `~/EMC/staging-64`:**

| File | What it is |
|---|---|
| `SRC_PRIMARY_1874_Debates-House-of-Deputies_DeKoven-Andrews-Beers-Ritual-Canon-Vote.txt` | Verbatim capture: De Koven's 26 Oct speech and 31 Oct remarks as the stenographer reported them, Andrews's reply on Scripture, Beers's speech, and the 27 Oct roll call and RECAPITULATION |
| `Ritual_Canon_1874_Dissent_Register_And_Pamphlet.md` | This report |

---

## §0. Two divergences between the brief and the record, recorded before anything else

Per the standing rule that a recorded convention in the repo overrides an
instruction in the brief, and the instruction to re-derive every figure:

**(0.1) `Ritual_Canon_1874_Reinstated_Examples.md` does not exist.** The brief's
READ FIRST list names it "(repo root, if copied in; otherwise note its absence
and proceed)". It is absent from the working tree and returns zero hits on a
recursive grep of the repo for the string `Reinstated_Examples`. Noted; this pass
proceeded on `Ritual_Canon_Examples_And_REC_Split.md`, the two `src/` primaries,
`src/SRC_PRIMARY_1874_GeneralConvention_Journal_Canon-20-Title-I_Ritual-Canon-Sequence.txt`
and `Incense_Reply_Source_Checks.md`, all of which do exist and were read.

**(0.2) ⛔ THE BRIEF'S SECOND CHARACTERIZATION OF `260835-63` IS NOT BORNE OUT.**
The brief states that "the pamphlet omits De Koven's stated reason for his 31
Oct Nay, which was constitutional rather than a protest against the surviving
specifications." **The pamphlet does not omit it. The pamphlet contains it, at
greater length than the Debates do, and adds to it a clause the stenographer did
not record.** The pamphlet's closing paragraph (`…ProjectCanterbury.txt`
L1314-1339) states the constitutional objection in full and ends "if I do not
vote for this, it will be simply on the ground that I have been trained by
Virginia to respect the Constitution" — the same sentence the Debates end on.
The *first* half of the brief's characterization **is** borne out and is
confirmed below: the Debates name incense and the crucifix where the pamphlet
names only the crucifix. See §3.

**(0.3) Method note, bearing on everything below.** `260835-62` obtained its
extracts through the Internet Archive `inside.php` full-text-search endpoint.
**That endpoint under-reports on this item and was not relied on here.** A query
for `blasphemy` against `debatesofhouseof00epis_0` returns `{"matches": []}`,
while the item's complete OCR contains one occurrence (§1.1). This pass loaded
the complete OCR derivative (3,541,143 characters) and searched it whole. The
brief's warning about `BookReaderGetTextWrapper`'s page offset did not arise:
no page-level fetch was needed.

---

## §1. ITEM 1 — How far the dissent actually went

### VERDICT

**The strongest characterization on record is De Koven's, and it is not
blasphemy.** It is that for the House to say that the use of incense symbolizes
false doctrine "is for this House to put itself in **utter and total opposition
to the Holy Scriptures**", and that committing the House to that proposition is
"**a dreadful thing**". His strongest intensifier anywhere in the argument is
"and this is something **more awful**", used of the Aaron/censer type, not of his
opponents.

**What that amounts to, stated precisely.** It is a charge of *contradiction of
Scripture*, levelled at a **proposed legislative act of the House**, in the
subjunctive, before the vote. It is not a sin-word, not an accusation against
persons, and not a charge that anyone had blasphemed. Nobody in the 1874 ritual
debate said that holding incense theologically objectionable is blasphemy,
impiety, sacrilege or profanation — **not De Koven, not anyone.** The vocabulary
is absent from the debate entirely. That is a **NEGATIVE FINDING WITH A FULL
SEARCH RECORD**, not an unsearched gap.

**⚠ For deployment.** The register available to a defender of incense in an
American General Convention, in 1874, in front of the very House about to name
incense as a symbol of erroneous doctrine, was *"in utter and total opposition
to the Holy Scriptures."* It was not *blasphemy*. If the project wants a named
Anglican precedent for the strongest form of the objection, this is it, and it
stops where it stops.

### 1(a) Blasphemy and its cognates — the search record

Searched over the complete OCR of the Debates volume, in two normalized views
(whitespace-collapsed, and de-hyphenated), case-insensitively, as substrings so
that every inflection is caught.

**Within the ritual-canon debate (26-27 October 1874, the 17th and 18th Days,
`__D` 1321392-1709018 — the whole of it, from Fulton's opening for the Committee
on Canons to the roll call):**

| Term (substring) | Occurrences |
|---|---|
| `blasphem-` | **0** |
| `impious` / `impiet-` | **0** |
| `sacrileg-` | **0** |
| `profan-` | **0** |
| `idolatr-` | **0** |
| `desecrat-` / `damnab-` / `unrighteous` / `monstrous` / `outrage` / `infamous` | **0** |
| `heresy` | 2 |
| `heretic-` | 1 |
| `abominat-` | 1 |
| `superstition` | 1 |
| `renegade` | 1 |

**Across the whole volume (all 3,541,143 characters, every day of the session):**

| Term | Total | Where, and in whose mouth |
|---|---|---|
| `blasphem-` | **1** | `__D` 1975112, 20th Day (29 Oct), the **Prayer-Book revision** debate, of Rome: "Rome was bound, of logical necessity, to land in the **blasphemous decree of 1870**" — i.e. papal infallibility. Not the ritual canon, not incense, and directed at Rome. |
| `sacrileg-` | **1** | `__D` 2295433, 21st Day (30 Oct), **Rev. Dr. LEEDS of Maryland**, describing the ritualist position in order to reject it: the denial of the impulse to adore "is, **by those who feel it**, held to be sacrilege… Now, sir, I deny the legitimacy of the conclusion". Reported speech, immediately disowned. |
| `impious` / `impiet-` | **0** | — |
| `idolatr-` | **1** | `__D` 2942266, in a pastoral passage on covetousness ("covetousness, which is idolatry"). No connection to ceremonial. |
| `profan-` | 6 | none in the ritual debate |

⛔ **So: the word "blasphemy" appears once in a volume of 3.5 million characters,
on a different day, in a different debate, about the Vatican Council. The one
occurrence of "sacrilege" is a characterization of the ritualists' own view,
quoted by an opponent in order to deny it. Neither is available to either side
of this question.**

### 1(b) The full range of terms used by opponents of the clause

Every one of these is verbatim from the Debates and attributed to the speaker
the stenographer names.

**REV. DR. DE KOVEN, of Wisconsin** (26 Oct, printed pp. 201-205) — the doctrinal
objection, and the only one:

| Term | Of what |
|---|---|
| "an utter piece of nonsense" | the incense specification |
| "a **dreadful thing** to commit this House to" | the proposition that incense symbolizes erroneous doctrine |
| "to put itself in **utter and total opposition to the Holy Scriptures**" | what the House would be doing by adopting it |
| "and this is something **more awful**" | *(of the Aaron/censer type, not of his opponents)* |
| "the beginning of **endless confusion**" | the substitution of "doubtful" for "strange" |
| "**the Reverend Paul Pry** into a canonical institution" | the two-Presbyter complaint mechanism |
| "something which the gentlemanly heart of our Church will **utterly and totally condemn**" | the same |

**REV. DR. BEERS, of Albany** (27 Oct, printed pp. 229-234) — the fullest speech
against the specifications after De Koven's, and **not doctrinal**:

| Term | Of what |
|---|---|
| "those **obnoxious** specifications" | the four examples |
| "would be simply **ridiculous** to enact" | the same |
| "it will **not be wise** for this General Convention to legislate on Ritual at all" | the whole canon |
| "I have **waited in vain for any evidence**… that there is any such state of things existing as calls for this legislation" | the factual premise |

**MR. SHATTUCK, of Massachusetts** (lay; 26 and 27 Oct) — pastoral, not doctrinal.
He introduces himself as "perhaps the only Lay Ritualist in this House", and his
case is that Ritualism reaches people nothing else reaches. He voted Nay.

**REV. DR. LEWIN, of Maryland** (27 Oct) — opposed the Committee's canon, but
**from the other side**: "I am opposed to the Canon as proposed by the Committee
on Canons… **I am also for specific legislation**." His objection to a rival
proposal was constitutional: "this Canon is entirely contrary to the spirit if
not the letter of the Constitution."

**REV. MR. BOLTON, of Pennsylvania** (27 Oct) — opposed the canon as too weak and
moved a substitute adding private confession, prayers to the Virgin Mary,
prayers for the dead, and vestments. His figure for the Committee's approach:
they "had something that they felt very venomous in their hand, and they
concluded that the best way to deal with it was to take hold of it by one of its
extremities."

### 1(c) Did anyone say the majority position was contrary to Scripture as doctrine?

**YES — one man, once: De Koven.** `contrary to Scripture` returns zero in the
debate; the assertion is made in the words quoted above and in no others. The
only two other Scripture-facing utterances in the ritual debate run the *other*
way:

- **REV. DR. FULTON of Alabama** (Committee on Canons), reading the ordination
  vow: "Are you ready with all faithful diligence to banish and drive away from
  the Church all erroneous and strange doctrine **contrary to God's Word**?"
- **MR. WHITTLE of Georgia** (lay), reading Article XXIV: "It is a thing plainly
  **repugnant to the Word of God**, and the custom of the Primitive Church, to
  have public prayer in the Church… in a tongue not understanded of the people"
  — deployed *against* ceremonial teaching.

### 1(d) Did anyone defend the clause on doctrinal grounds, and in what terms?

**YES, and this is the finding of §1 that the project did not have.**

**⭐⭐ MR. ANDREWS, of Ohio (lay), 27 October, printed p. 225 — the direct answer
to De Koven.** He opens: "I propose to confine myself entirely to the **legal**
aspects of this case, and **not to the theological**." He then answers De Koven's
Scripture argument by *refusing to make the counter-argument*:

> "he quotes the literal language of the Scripture as part of his argument. I
> might quote the literal language of the Scripture as part of my argument, if I
> did not deem it unworthy of this occasion to attempt to influence this body by
> it. **I might say that Jehovah Himself said, under certain circumstances, that
> incense was an abomination to Him; but I would not deem that appropriate to
> this argument at all.** What is the meaning of incense in connection with the
> administration of the Lord's Supper? That is the point."

⛔⛔ **READ THIS BEFORE DEPLOYING IT, IN EITHER DIRECTION.** This is a
**praeteritio**. Andrews raises the Scripture counter and twice expressly
declines to make it. He is **not** asserting that Scripture calls incense an
abomination. Quoting him as though he were would be exactly the misreading the
project's attribution rules exist to prevent. What he *does* assert is the
doctrinal-symbolism point:

> "this **symbolizing** of doubtful doctrine, this **insinuating** of doubtful
> doctrine to men, women, and children who are not in the habit of discussing
> these matters, that tends to make a lodgment and that you cannot answer, is
> what we aim at. If a man wishes to preach doubtful doctrine in this Church,
> let him do it; but let him do it openly **by word of mouth and not by symbols**."

⛔ The allusion behind "an abomination to Him" is **not named in the Debates**.
Isaiah 1:13 is the obvious candidate. This pass does not supply it and it must
not be supplied in outward material without a source.

**Other defences, all short of a doctrinal case for the incense specification
specifically:**

- **REV. DR. RUDDER of Pennsylvania**: ritualism is "**this new heresy** in the
  Church"; leaving it alone will "damage the Church and bar its progress."
- **REV. DR. LEWIN of Maryland**: the acts named "have been before the courts,
  and have been specifically **declared to be unlawful**" — an appeal to
  adjudication, not to doctrine.
- **REV. DR. HALL of Long Island**: "Outside of this building it is perfectly
  well understood what the Canon means. It means either the **downfall or the
  victory of Ritualism**." *(Already in the repo at 260835-62 §1; re-verified.)*
- **REV. DR. BEERS of Albany** — who **voted Nay** — nonetheless: "the man who
  will venture now to reintroduce the emblems of the symbols of those **mediaeval
  superstitions**… is a **renegade to the Church of the Reformation**." This is
  the strongest anti-ritualist language in the debate and it comes from a man in
  the minority *against* the canon.

⛔⛔ **NOBODY DEFENDED THE INCENSE SPECIFICATION BY ARGUING FROM SCRIPTURE.** The
one man who could have, and who saw the opening, declined it on the floor and
said why.

---

## §2. ITEM 2 — The isolation of the dissenting view

### VERDICT

**In numbers, not adjectives: the doctrinal objection was one man.**

- **One** of the seventeen deputies who made a substantial speech in the ritual
  debate opposed the clause on doctrinal grounds — De Koven.
- **Two** dioceses out of forty-one cast a clerical Nay, and **neither was his**;
  his own deputation outvoted him 3-1.
- **Zero** protests, minority reports or dissenting entries accompany the
  adoption, in the Journal or in the Debates.
- The doctrinal objection was heard on 26 October at length and **the House
  adopted the clause the next day**.

### 2(a) The vote of 27 October 1874

⭐ **Established this pass from TWO independent printed sources for the first
time.** The Journal (repo capture, printed pp. 143-145) and the Debates
(`__D` 1705645, printed p. 248) print the same recapitulation.

| Order | Dioceses represented | Ayes | Nays | Divided |
|---|---|---|---|---|
| Clergy | 41 | **38** | **2** | 1 |
| Laity | 39 | **35** | **3** | 1 |

Called for by the Deputation from **Tennessee**; the Debates add that **Kentucky
also asked** and was told Tennessee had asked first (`__D` 1699751). The Debates
OCR prints the clerical aye figure as "88", an OCR error for 38, corrected here
only because the Journal independently prints 38 and the roll immediately above
names exactly two dissenting clerical dioceses. **The lay figure 35 is confirmed
against Aycrigg's 34; the Journal and the Debates agree and Aycrigg is wrong.**

**⛔ THE VOTE WAS ON THE WHOLE RESOLUTION, NOT ON THE EXAMPLES AND NOT ON
INCENSE.** This confirms `260835-62`'s CORRECTION 1 and is re-derived here
independently: the Debates record a single question ("The question recurring on
the resolution reported by the Committee on Canons") and a single roll. No
deputy ever voted on incense as a separable proposition.

**⭐⭐ NEW — THE INDIVIDUAL ROLL, WHICH CHANGES WHAT "38-2" MEANS.** The Debates
print the roll deputy by deputy. Counted by this pass:

- **26 individual deputies voted Nay** — 16 clerical, 10 lay.
- Only **two dioceses** cast a clerical Nay: **Albany** (all four clergy) and
  **Michigan** (2 of 3).
- **De Koven's own diocese voted AYE.** Wisconsin's clerical entry: "Rev. Dr.
  Adams, Rev. Mr. Half, and Rev. Mr. Ten Broeck, aye. **Rev. Dr. De Koven, nay.**"

⛔ **38-2 and 35-3 are counts of DIOCESES. 16 and 10 are counts of MEN. Both are
true, of different things, and neither may be quoted for the other.** Full roll
in the companion capture file, §4c.

### 2(b) Floor opponents by ground

The ritual debate (26-27 Oct) contains **seventeen** speakers who made a
substantial speech (a turn of more than 4,000 characters), enumerated from the
stenographic report:

| Speaker | Position | Ground |
|---|---|---|
| **DE KOVEN** (Wisconsin, cl.) | **Against the specifications** | ⭐ **DOCTRINAL** — the clause asserts something contrary to Scripture — *plus* constitutional and procedural |
| **BEERS** (Albany, cl.) | Against the whole canon | **Prudential / evidentiary** — no case made out; specifications "ridiculous to enact" |
| **SHATTUCK** (Massachusetts, lay) | Against | **Pastoral** — Ritualism reaches people nothing else reaches |
| **LEWIN** (Maryland, cl.) | Against *this* canon | **Wanted stronger and more specific legislation**; constitutional objection to a rival draft |
| **BOLTON** (Pennsylvania, cl.) | Against as too weak | Moved a **wider** substitute (confession, prayers for the dead, vestments) |
| FULTON (Alabama, cl.) | For — Committee on Canons | Ordination vow; the Church must act |
| BURGWIN (Pittsburgh, lay) | For — closed for the Committee | Constitutional and drafting |
| ANDREWS (Ohio, lay) | For | **Legal, expressly not theological** — but argues the symbolism point |
| RUDDER (Pennsylvania, cl.) | For | "this new heresy" |
| WHITTLE (Georgia, lay) | For | Article XXIV; symbols teach |
| NORTON (Virginia, cl.) | For | Answers the constitutional objection |
| SMITH (South Carolina, lay) | For | Defends the principle against amendments |
| HALL (Long Island, cl.) | For | "downfall or the victory of Ritualism" |
| CLARK (New Jersey, cl.) | For | The fact of Ritualism and the remedy |
| THOMPSON (Tennessee, lay) | For | Offered a resolution |
| HAZLEHURST (Pennsylvania, lay) | For | On behalf of the laity |
| STEVENSON (Kentucky, lay) | — | Called for the vote by orders |

**⭐ So: five substantial speeches opposed the Committee's canon, and only ONE of
the five opposed it because the doctrinal declaration was false. Two of the other
four opposed it because it did not go far enough.** A Nay vote in this chamber is
not evidence of sympathy with incense — Beers voted Nay and called reintroducing
mediaeval ceremonial the act of "a renegade to the Church of the Reformation."

### 2(c) Protest, minority report, dissenting entry

**NONE. NEGATIVE FINDING WITH A SEARCH RECORD.**

- Debates, 18th Day and the surrounding span (`__D` 1475776-1720000): `\bprotest\b`
  and its inflections **0**; `minority report` **0**; `minority` **0**;
  `dissent` **0**; `leave to record` **0**; `enter upon the Journal` **0**.
  *(A naive substring search for `protest` returns 27 — every one is
  "Protestant". Word-boundary matching was used.)*
- Journal (repo capture): grep for `protest`, `dissent`, `minority` across the
  whole file returns **nothing**. The Journal goes straight from the roll to
  "The resolution reported by the Committee was therefore adopted."

**The dissent was a speech and a vote. It left no other trace.**

⭐ **Corroborating datum for the argument's afterlife, on the record from the
same volume:** De Koven himself said, in the same speech, "if our debates go down
to posterity, as I trust they may, the fact that I have pointed this out to this
House, being duly recorded and duly read, will add a point and pungency to the
fact, if you pass it without disproving what I have to say." *(Debates, printed
p. 205.)* **The House passed it without disproving it.** ⚠ `[Analysis]` — the
inference from that is the project's own and is not attributed to anyone in 1874.

---

## §3. ITEM 3 — The pamphlet divergence

### VERDICT

**⛔⛔ NO. The Project Canterbury pamphlet is NOT safe to cite as the source of
record for De Koven's words. The stenographic *Debates of the House of Deputies*
(IA `debatesofhouseof00epis_0`) is, and should be designated so.**

The pamphlet is not a forgery and not a paraphrase — the two texts agree
sentence for sentence across the whole of the 26 October speech, and this pass
demonstrated that mechanically in both directions (§3.4). **But the pamphlet is a
revised text; it says so, in part; and it is revised at the two points that bear
on this project's question and nowhere else of comparable weight.**

### 3(a) The divergence table

Verbatim from both sides. Pamphlet = `src/SRC_PRIMARY_1874_DeKoven_Canon-On-Ritual-Speech_ProjectCanterbury.txt`.
Debates = the companion capture file in this folder. OCR as read.

#### The 26 October speech

| # | Debates (stenographic) | Pamphlet (printed) | Weight |
|---|---|---|---|
| 1 | "the use of incense symbolizes **erroneous and strange** doctrines" | "the use of incense symbolizes **erroneous or doubtful** doctrines" | ⚠⚠ **MATERIAL.** The pamphlet makes De Koven's paraphrase match the canon's actual wording, which he had quoted correctly two sentences earlier and objected to at length. The Debates preserve an inconsistency; the pamphlet resolves it. |
| 2 | "**and that ascending incense symbolized** the atoning sacrifice and the everlasting mediation." *(declarative)* | "**and what did the ascending incense symbolize but** the atoning Sacrifice and the everlasting Mediation?" *(rhetorical question)* | ⚠⚠ **MATERIAL under this project's own attribution rules**, which exist to stop rhetorical content being read as declarative. Here the printed text converts a declarative into a question. |
| 3 | "I never was in any church in connection with the Protestant Episcopal Church **in which** incense was used" | "…**at a time when** incense was used" | Minor |
| 4 | "a commission formed in that **broad-hearted** spirit" | "a commission formed in this **generous** spirit" | Minor |
| 5 | "Certainly if **they have** Presbyters to do it" | "Certainly if **we are to have** Presbyters to do it" | Minor |
| 6 | "the change **in** the old-fashioned words" | "the change **of** the old-fashioned words" | Trivial |
| 7 | "Cut out **your** crucifix from **your** stained windows, put **them** out of your prayer-books" | "Cut out **the** crucifix from **the** stained windows, put **it** out of your prayer-books" | Trivial |
| 8 | "The kindred drops will **seek** their own" | "The kindred drops will **claim** their own" | Trivial *(a hymn quotation)* |
| 9 | "and so I **will not propose it to this House: I will only propose that it be referred** for their consideration to the Committee on Canons" | "At the end of my speech, therefore, I **propose to offer my amendment**, and also this substitute…" | ⚠ Recasts his procedural intention |
| 10 | Three separate turns on 26 Oct, separated by other speakers and by interventions | Printed as one continuous address | ⚠⚠ **STRUCTURAL.** See below. |

#### The 31 October remarks

| # | Debates (stenographic) | Pamphlet (printed) | Weight |
|---|---|---|---|
| 11 | "it said that the use of **the crucifix and the use of incense** was unlawful during the celebration of the Holy Communion" | "It said that the use of **the crucifix** was unlawful during the celebration of the Holy Communion." | ⛔⛔ **THE CENTRAL EXCISION. Incense is deleted.** |
| 12 | "it could have been inferred by cunning people that the use of **the crucifix and the use of incense were** allowable in other services" | "…that the use of **the crucifix was** allowable in other services" | ⛔⛔ **Same excision, second occurrence.** |
| 13 | "Therefore I think it is a very wise process to cast out **those two things**." | "Therefore, I think **it might be conceived to be** a wise process to cast out **this particular specification**." | ⛔⛔ Two changes at once: **plural to singular** (incense drops out again) and **assertion to hedge**. |
| 14 | "I can understand how the House of Bishops **might have made this amendment**" | "…**might have omitted what was said about the crucifix**" | ⛔ Narrows the subject to the crucifix a third time |
| 15 | **"Rev. Mr. BOLTON, of Pennsylvania. That is just the trouble."** | *absent* | ⚠⚠ An **interruption from the floor**, and a hostile one, removed |
| 16 | **"Rev. Dr. ADAMS, of Wisconsin. Does the Roman Catholic Church remove the crucifix?"** and De Koven's reply, "I do not know anything about the Roman Catholic Church. I leave that to my brother from Wisconsin. [Laughter.]" | *absent* | ⚠⚠ A second exchange, with a colleague from his own deputation, removed |
| 17 | "the symbolic representation is **out!**" **[Laughter.]** | "the symbolic representation is **taken away**." *(no laughter)* | ⚠ Stage direction removed |
| 18 | "nothing in this Canon **possibly** authorizes" | "nothing in this Canon authorizes" | ⚠ Hedge removed *(direction opposite to #13)* |
| 19 | "the reverend **gentleman** from Pennsylvania" *(sing.; Bolton had just interrupted)* | "the reverend **gentlemen** from Pennsylvania" *(pl.)* | Follows from #15 |
| 20 | "I would not of my own will vote for **these two hard things if I had my own choice**" | "I would not of my own will vote for **these particular specifications**" | ⚠ |
| 21 | "**I can vote for this Canon entirely** as expressing the present mind of the Church" | "**I might vote for this Canon** as expressing the present mind of the Church" | ⚠⚠ **MATERIAL.** Weakens a statement of intent into a possibility. |
| 22 | "yet if this Church think it best to limit it to kneeling, I am **perfectly** satisfied" | "…I am satisfied" | Minor |
| 23 | "whether there shall be a little more **liberty** in ceremonial, then the Constitution is very elastic" | "…a little more **restriction** in ceremonial…" | ⚠⚠ **MATERIAL AND UNRESOLVED.** The two readings are opposites. The pamphlet's "restriction" is the one that fits the argument. This pass records the divergence and **does not adjudicate it**; it may be a stenographic slip, an OCR error, or an author's correction. |
| 24 | *absent* | The whole "gradation in the acts" passage — "It may, indeed, be said…", the numbered list *Bowings / Genuflections / Kneeling / Prostrations*, and "if this interpretation be not allowed, it will puzzle lawyer or theologian…" | ⭐⭐ **ADDITION — and the pamphlet admits it.** See 3(b). |
| 25 | *absent* | "**much more even to seem to declare what is or what is not doctrine by Canon is utterly unconstitutional**" | ⛔⛔ **ADDITION, AND IT IS NOT ADMITTED.** This is the sharpest single statement of the constitutional objection in the pamphlet, and it is not in the stenographic record. |
| 26 | "the amendment… **confines the Canon to the celebration of the Holy Communion**" | "…confines the Canon, **which the proposed Amendment of the House of Bishops did not do**, to the celebration…" | ⚠ Explanatory clause added |

⭐⭐ **#24 SETTLES AN OPEN QUESTION IN THE REPO.** `Incense_Reply_Source_Checks.md`
(L264-275) records, as `[Stated-Analysis]` and expressly as inference rather than
fact, that "the gradation-of-postures paragraph ('It may, indeed, be said …',
L1285-1313) **reads as written prose and is the likeliest candidate**" for the
paragraph the pamphlet says was inserted. **The Debates confirm it.** That
passage, and only that passage, is absent from the stenographic report of the 31
October remarks. **The inference is now VERIFIED and can be relabelled `[Stated]`
as to the fact of absence** — with the caveat that the pamphlet does not itself
identify which paragraph it means, so the identification rests on the Debates,
not on the pamphlet's own words.

### 3(b) The pamphlet's publication history

| Question | Answer | Status |
|---|---|---|
| Title | *The Canon on Ritual, and the Holy Eucharist; a Speech delivered in the General Convention, October 26th, 1874, by the Rev. James De Koven, D.D., Warden of Racine College* | **ESTABLISHED** from the title page as transcribed |
| Publisher | New York: T. Whittaker, 2 Bible House | **ESTABLISHED** |
| Date of publication | Not printed on the title page; the pamphlet carries no date | **NOT ESTABLISHED.** 1874 or shortly after is the obvious inference; it is not stated |
| Who prepared it | **Not stated anywhere in the pamphlet.** No editor, no preface, no publisher's note, no "reported by" | **NOT ESTABLISHED** |
| From what copy | **Not stated.** No source is named — not the stenographer, not *The Churchman*, not the author's manuscript | **NOT ESTABLISHED** |
| Does it say it is revised? | **PARTLY, AND ONLY ONCE.** Before the 31 October remarks it prints: *"The following remarks were made after the presentation of the Amended Canon, October 31st. **A paragraph, in substance spoken at a later time, has been inserted.**"* | **ESTABLISHED, VERBATIM** |
| Does it say the 26 Oct speech is revised? | **NO. It makes no statement of any kind about the text of the 26 October speech**, which it presents as "a Speech delivered in the General Convention, October 26th, 1874" | **ESTABLISHED as a negative** |
| Does it disclose that the "speech" is three turns? | **NO** | **ESTABLISHED as a negative** |
| Does it disclose the excisions at #11-#14, or the addition at #25? | **NO** | **ESTABLISHED as a negative** |

⚠ **UNMATCHED.** Who prepared the pamphlet, when, and from what copy is not
established by anything this pass read. It was not pursued beyond the pamphlet's
own four corners, because the pamphlet's own four corners settle the question the
brief actually asks. Recorded as owed if the provenance is ever needed.

### 3(c) Do the divergences run in a consistent direction?

**Yes, and it is stateable without any claim about motive, which this pass does
not make and which the record does not support.**

**The pattern is: the 26 October speech is left substantially intact; the 31
October remarks are systematically narrowed to the crucifix.**

1. **The 26 October speech is not cut.** A two-directional mechanical check
   (§3.4) found **no passage of the Debates version absent from the pamphlet**
   and **no passage of the pamphlet version absent from the Debates**, across
   126 and 304 sampled units respectively. Whatever else the pamphlet is, it is
   not an abridgement of the 26 October speech.
2. **Every excision in the 31 October remarks removes incense.** Four separate
   places (#11, #12, #13, #14). In each, a text that named *the crucifix and
   incense* becomes a text naming *the crucifix* alone. **The pamphlet does not
   remove the crucifix anywhere.**
3. **The floor is removed.** Both interjections and both stage directions go
   (#15, #16, #17). What was an exchange becomes an address.
4. **Statements of voting intent are softened; the constitutional objection is
   sharpened.** #21 weakens "I can vote for this Canon entirely" to "I might
   vote"; #13 weakens "it is a very wise process" to "it might be conceived to
   be a wise process"; #25 adds the strongest constitutional sentence in the
   pamphlet, which the stenographer did not record.
5. **Where the printed text and the stenographic text differ on doctrine, the
   printed text is the more internally consistent** (#1, #23).

⛔ **THIS PASS REPORTS THE PATTERN AND DOES NOT CHARACTERIZE MOTIVE.** Every
divergence above is consistent with an author preparing his own remarks for print
— tidying a quotation he had misspoken, cutting interruptions, adding a point he
wished he had made. It is equally consistent with other accounts. **Nothing in
the record identifies who made the changes.** The pamphlet names no editor.

⚠⚠ **BUT THE CONSEQUENCE FOR THIS PROJECT IS INDEPENDENT OF MOTIVE.** The
project has been citing, as De Koven's words on 31 October 1874, a text from
which incense has been removed at every point where he named it. **The
stenographic record shows he named incense four times in remarks the pamphlet
prints as being about the crucifix.** That is a strengthening of the project's
case on the facts and a weakening of its sourcing, simultaneously.

### 3(d) The method, and its limits — stated so a later pass can audit it

Two mechanical checks were run, in both directions, over
whitespace-and-punctuation-stripped lowercase text:

1. **Pamphlet → Debates.** The pamphlet's 26 Oct speech and 31 Oct remarks were
   split into 308 sentence-units of >60 letters. Each was probed against the
   Debates by three 12-character subsequences. **8 units scored zero hits, 11
   scored one.** Zero-scoring units, individually inspected: **2** are the canon
   text the pamphlet reprints as a preface and which the Debates never quote in
   full (probe indices 3, 4); **6 are real divergences** — probe 93 = item #7,
   probes 296-298 = item #24 (the gradation passage), probe 299 = item #21,
   probe 306 = item #25. Of the 11 one-hit units, one more (probe 293) is a
   further sentence of the #24 gradation passage and one (probe 88) is item #2;
   the rest are OCR noise, individually inspected.
2. **Debates → Pamphlet.** De Koven's three 26 Oct turns and his 31 Oct remarks
   were split into 250 units by the same rule and probed against the pamphlet.
   **Four flagged, all wording substitutions** (#3, #7, #21 and one OCR artifact
   in the Charles II passage). **No whole passage of the Debates is missing from
   the pamphlet.**

⛔ **THE LIMIT, STATED PLAINLY.** This method detects **omissions and additions**.
It does **not** detect **substitutions inside a sentence** — which is exactly what
items #1, #11, #12, #13, #14 and #23 are. Those were found by **reading the two
texts against each other** across the incense-bearing passages and the whole of
the 31 October remarks. **A sentence-by-sentence substitution audit of the
non-incense two-thirds of the 26 October speech was NOT run.** More minor
substitutions of the #4/#5/#6 class certainly exist there. **This table is
complete for the 31 October remarks and for the incense and doctrinal-test
passages of 26 October; it is not claimed to be complete for the rest.**

---

## §4. ITEM 4 — Source-of-record designation

### VERDICT

**Four capture headers and registry cells designate the pamphlet as source of
record for De Koven's speech text. All four are now wrong, and one is wrong on a
point of fact that this pass falsified. The corrections are recorded below as
owed. NOTHING WAS EDITED.**

### 4(a) The designations, quoted

**⛔ LOCUS 1 — `src/SRC_PRIMARY_1874_DeKoven_Canon-On-Ritual-Speech_ProjectCanterbury.txt`,
capture header, lines 23-27.** *(This is the designation the brief flags.)*

> SOURCE OF RECORD: this pamphlet is the source of record for the SPEECH text.
>   The Journal of the General Convention of 1874 (captured separately as
>   SRC_PRIMARY_1874_GeneralConvention_Journal_Canon-20-Title-I_Ritual-Canon-Sequence.txt)
>   is the source of record for the ENACTED canon and for motions, messages and
>   votes; it does not record debate.

**⛔ LOCUS 2 — `SRC_Manifest.md`, the registry row for that file (line 4474).**

> ⛔⛔ **THE FILE IS THE SOURCE OF RECORD FOR THE SPEECH TEXT ONLY — the 1874
> Journal, registered below, is the source of record for the enacted canon,
> motions, messages and votes.** ⚠ **Item (4) carries the pamphlet's own caveat
> that "A paragraph, in substance spoken at a later time, has been inserted"**

**⛔⛔ LOCUS 3 — `Incense_Reply_Source_Checks.md`, lines 264-270.** *(The most
serious of the four: it makes a factual claim that is now false.)*

> **The pamphlet is the only source of record for both texts**, and it carries
> its own caveat that one paragraph of the 31 Oct. remarks was "in substance
> spoken at a later time" and inserted — the pamphlet does not say which
> paragraph.

**⛔ LOCUS 4 — `Incense_Reply_Source_Checks.md`, line 361.**

> Source of record: the T. Whittaker pamphlet (Project Canterbury
> transcription); the Journal does not print speeches.

**Two further mentions, weaker but affected:**

- `src/SRC_PRIMARY_1874_GeneralConvention_Journal_...txt`, header line 26-27:
  "DeKoven's speeches are in the separately captured pamphlet
  `SRC_PRIMARY_1874_DeKoven_Canon-On-Ritual-Speech_ProjectCanterbury.txt`."
  **Now incomplete rather than wrong.**
- `passes/260835-57_incense-reply-source-checks_close-out.md`, line 51: "the
  pamphlet is sole source of record for both". **Same falsification as Locus 3,
  but this is a pass close-out and is historical record — under the never-alter
  rule it should NOT be touched at all.**

### 4(b) What the corrected designation should be

**The pamphlet's status changes from *source of record* to *a printed and
partially revised text of the same speech, useful for its readable transcription
and for its own admission of insertion, and NOT authoritative on wording.***

### 4(c) ⭐ THE EXACT WORDING A LATER PASS SHOULD APPLY

Three appends. **None alters an existing sentence** — each is a dated note placed
after the text it corrects, per never-alter.

**FOR LOCUS 1** — append immediately after the existing SOURCE OF RECORD block in
the capture header:

> ⛔⛔ **SUPERSEDED IN PART, 260835-64. THIS PAMPHLET IS NO LONGER THE SOURCE OF
> RECORD FOR THE SPEECH TEXT.** The contemporary verbatim stenographic report —
> *Debates of the House of Deputies … 1874*, reported for The Churchman
> (Hartford: M. H. Mallory & Co.), IA item `debatesofhouseof00epis_0` — is the
> source of record for what De Koven said on 26 and 31 October 1874. **This
> pamphlet is a printed and partially revised text and is not authoritative on
> wording.** Its divergences from the stenographic report are tabulated at
> `Ritual_Canon_1874_Dissent_Register_And_Pamphlet.md` §3(a), and are of three
> kinds: (i) in the 31 October remarks, **incense is removed at all four points
> where the stenographer records De Koven naming it**, leaving a text about the
> crucifix alone; (ii) two floor interjections and their replies are removed;
> (iii) at least one clause is **added** that the stenographer did not record
> ("much more even to seem to declare what is or what is not doctrine by Canon
> is utterly unconstitutional") beyond the one insertion the pamphlet itself
> admits. ⭐ **The paragraph the pamphlet admits was "in substance spoken at a
> later time" is now identified: it is the gradation-of-postures passage ("It
> may, indeed, be said …"), which is the only passage of the 31 October remarks
> absent from the stenographic report.** ⚠ **The pamphlet remains a legitimate
> convenience text and remains citable as evidence of what was PRINTED under De
> Koven's name; it is not citable for what was SAID.** Prior text left standing
> per the never-alter rule.

**FOR LOCUS 2** — append to the `SRC_Manifest.md` registry cell:

> ⛔⛔ **260835-64 — SOURCE-OF-RECORD DESIGNATION WITHDRAWN.** This file is **not**
> the source of record for the speech text. The stenographic *Debates of the
> House of Deputies … 1874* (IA `debatesofhouseof00epis_0`) is. See the capture
> header's 260835-64 note and
> `Ritual_Canon_1874_Dissent_Register_And_Pamphlet.md` §3. ⭐ **The paragraph
> flagged in this cell as "in substance spoken at a later time" is identified:
> the gradation-of-postures passage.** Prior cell text left standing per the
> never-alter rule.

**FOR LOCUS 3** — append immediately after the "only source of record" sentence:

> ⛔⛔ **FALSIFIED 260835-64. "The pamphlet is the only source of record for both
> texts" IS NO LONGER TRUE AND WAS NEVER TRUE — a contemporary verbatim
> stenographic report of both existed throughout.** *Debates of the House of
> Deputies … 1874*, reported for The Churchman, IA `debatesofhouseof00epis_0`,
> prints the 26 October speech at printed pp. 201-205 and the 31 October remarks
> at printed pp. 338-339. ⛔ **It is the source of record for both, and it
> differs from the pamphlet at the points that matter to this document** —
> above all, the 31 October remarks name **incense and the crucifix** where the
> pamphlet names only the crucifix. ⭐ **The `[Stated-Analysis]` identification
> of the gradation-of-postures paragraph as the inserted one is CONFIRMED by the
> stenographic report and may be relabelled `[Stated]` as to the fact of its
> absence from the floor record.** ⚠ **Every verbatim quotation in this document
> that is sourced to the pamphlet must be re-verified against the Debates before
> outward deployment.** Prior text left standing per the never-alter rule.

**FOR LOCUS 4** — append:

> ⛔ **CORRECTED 260835-64: source of record is the stenographic *Debates of the
> House of Deputies … 1874*, not the pamphlet. The Journal indeed does not print
> speeches; the Debates volume does.** Prior text left standing.

⛔ **`passes/260835-57_…_close-out.md` line 51 — DO NOT TOUCH.** It is a pass
close-out and therefore historical record. Its error is corrected by the Locus 3
note, which is in the live document the close-out describes.

---

## §5. Owed work and unresolved gaps

In rough order of how much they matter.

1. ⛔⛔ **Every verbatim De Koven quotation now standing in the repo derives from
   the pamphlet and needs re-verification against the Debates.** At least
   `Incense_Reply_Source_Checks.md`, `Ritual_Canon_Examples_And_REC_Split.md`
   §1(b), `RJ_Incense_Analysis.md` and `Incense_Conversational_Outline.md`
   should be swept. **Not swept this pass.** In particular,
   `Ritual_Canon_Examples_And_REC_Split.md` §1(b) quotes "erroneous or doubtful
   doctrines, which is a dreadful thing" from the pamphlet; the Debates read
   "erroneous and strange".
2. ⚠⚠ **The "liberty" / "restriction" divergence (#23) is unresolved** and one of
   the two readings is wrong. It could be settled by reading the page image at
   printed p. 339 of the Debates rather than the OCR. **Not attempted.**
3. ⚠ **A sentence-level substitution audit of the non-incense two-thirds of the
   26 October speech has not been run** (§3(d)).
4. ⚠ **Printed page numbers throughout are OCR-inline tokens, not read off the
   running heads of the page images** — the same UNVERIFIED status `260835-62`
   recorded for its own. De Koven 26 Oct: pp. 201-205, the incense argument on
   p. 203. Andrews: p. 225. Beers: pp. 229-234. The roll and recapitulation:
   pp. 247-249. De Koven 31 Oct: pp. 338-339.
5. ⚠ **The pamphlet's provenance** — who prepared it, when, from what copy — is
   UNMATCHED (§3(b)) and was not pursued outside the pamphlet itself.
6. ⚠ **The five other speeches opposing or qualifying the canon were classified
   from their opening and closing statements of position, not from a full
   reading of each.** Beers's 37,761-character speech was read in four samples,
   not entire. The classification in §2(b) is defensible but is not a
   line-by-line warrant.
7. ⚠ **`260835-62` §3 LEADS 2, 3, 4, 5 and 6 remain unverified.** LEAD 1 (Fulton)
   is partly confirmed (companion capture §6).
8. ⚠ **Aycrigg** was not consulted this pass beyond what the repo already
   records. He remains SECONDARY and known wrong on the striking.
9. ⚠ **The 31 October concurrence vote** (clergy 38-2-1; laity, 31 dioceses,
   28-1-2) is taken from the repo's Journal capture and was **not** independently
   re-derived from the Debates this pass.

---

## §6. What a later pass should NOT conclude from this one

- ⛔ **Do not read Andrews's "abomination" sentence as an assertion.** It is a
  praeteritio. He says twice that he will not make the argument. §1(d).
- ⛔ **Do not read a Nay vote as sympathy with incense.** Beers of Albany voted
  Nay and called reintroducing mediaeval ceremonial the act of "a renegade to
  the Church of the Reformation". §2(b).
- ⛔ **Do not say "38-2" without saying "of the clergy, by dioceses".** Twenty-six
  individual deputies voted Nay. §2(a).
- ⛔ **Do not say the House rejected De Koven's argument.** It adopted the clause
  without answering the Scripture argument — which is a different and, for this
  project, a stronger fact. Whether to deploy it is JD's call; it is recorded
  here, not drafted.
- ⛔ **Do not characterize the pamphlet's editing as suppression.** The record
  identifies no editor and states no motive. §3(c).
