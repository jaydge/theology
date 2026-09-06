# The Homilies on incense

**Stamp: 260835-59.** ASSIGNED, NOT DERIVED — the brief assigned this stamp and
forbade deriving one, because two other passes were running concurrently. The
stamp registry was not read and no registry cell has been written.

**Mode: neither APPEND nor RECONCILE.** This pass ran against a READ-ONLY
repository (`~/EMC/theology`, HEAD `cb833ea` at the time the brief was written)
and wrote everything to a separate staging folder (`~/EMC/staging-59`). Nothing
in the repository was created, edited, moved, renamed or deleted; no writing git
command was run; the only git-adjacent operation was reading files. JD will
handle any move into `src/` and any commit himself.

**Occasion.** The 1899 Archbishops' Opinion says the Church has never spoken of
incense as an evil thing, and then concedes:

> "There are some expressions in the Homilies which have that character. But the
> Homilies are hortatory rather than imperative, and have never been taken as
> having high authority on points of doctrine or of ritual."

*(Verbatim from `src/SRC_PRIMARY_1899_Archbishops_Lambeth-Opinion-Incense-Lights.txt`,
lines 191-194.)*

RJ has asked in substance where the Church of England agrees with JD's position.
The Archbishops point at the Homilies and then rank them low. This pass
establishes what the Homilies actually say and how much weight they can bear.

**Files written by this pass, all in `~/EMC/staging-59`:**

| File | Contains |
|---|---|
| `Homilies_On_Incense.md` | this file — the findings, §1-§5 |
| `SRC_PRIMARY_1859_Griffiths_Books-of-Homilies-Incense-and-Censing-Passages.txt` | all 15 passages as extracted from the scholarly edition, plus the search method and its failure modes |
| `SRC_SECONDARY_2014_ReformedAnglicanFellowship_Peril-of-Idolatry-Incense-Passages.txt` | the second witness (JD's candidate source), the two material differences, and the record of a truncated-fetch false negative |
| `SRC_PRIMARY_1571_Articles-of-Religion_Article-35-Of-the-Homilies-and-Later-Forms.txt` | Article 35 in four witnesses, Article 34, the BCP rubrics, and Canons 46/49/80/85 of 1604 |

---

## §1 — Locate every passage

### Edition chosen, and why

**John Griffiths, ed., *The Two Books of Homilies Appointed to be Read in
Churches* (Oxford: at the University Press, 1859).** It is the standard
scholarly edition: it prints both Books complete, collates the sixteenth-century
printings in footnotes, supplies the Latin and Greek of the patristic and
classical quotations the homilies translate, and carries an index and a glossary
of archaic words. Working copy: the Internet Archive OCR text layer of the Google
scan, item `twobookshomilie00grifgoog`, retrieved 2026-09-06.

JD's supplied candidate — the Reformed Anglican Fellowship blog post of
2014-10-23 — was treated as a lead, per the brief, and is captured as a **second
witness only**. Three reasons it cannot be the edition of record:

1. **It carries one homily.** "Against Peril of Idolatry", all three Parts,
   complete. It therefore cannot reach the two occurrences in Book I, and it
   cannot support the negative finding about the other thirty-one homilies.
2. **It names no edition, no editor and no copy-text**, and gives no collation.
3. **It has at least one reading that the scholarly edition rejects** — see
   §1.4.

### 1.1 The whole-corpus search, and the two ways it can go wrong

Both Books were searched — not only the Peril of Idolatry — for *incense,
censing, censer, cense, perfume, odours, frankincense, sweet savour, savour,
thurib-, sensing*, and OCR-tolerant variants of each.

⛔ **TWO FAILURE MODES WERE HIT AND ARE RECORDED SO THE FIGURES CAN BE TRUSTED.**

- **A naive search of the Griffiths OCR undercounts.** It misses `iucense-sbipa`
  (OCR of "incense-ships", p. 258) and it misses `one crumb of in-\ncense`
  (hyphenated across a line break, p. 266). The text had to be de-hyphenated and
  re-searched with OCR-tolerant patterns before the count settled. Anyone
  re-deriving these figures by plain grep on that file will get a lower number
  and it will be wrong.
- **A truncated fetch of the second witness produced a clean false negative.** An
  ordinary HTTP fetch of the Reformed Anglican page returned 119,439 characters,
  cut off mid-sentence in the early Third Part, and a search of that capture
  returned **zero** occurrences of "incense". Reported as it stood, that would
  have been a falsified premise: that JD's candidate source never mentions
  incense. It mentions it thirteen times. The page had to be loaded whole and
  searched in the DOM.

Both are recorded in the capture headers.

### 1.2 The count

**Fifteen relevant occurrences, in exactly two homilies. Both are the THIRD PART
of their homily. Every other homily in both Books yields nothing.**

| # | Homily | Part | Griffiths page | Word, as it stands |
|---|---|---|---|---|
| 1 | Bk I, Hom. IV, *Of Good Works annexed unto Faith* | Third | 54, l. 29 *(glossary)* | "decking and **censing** them" |
| 2 | Bk I, Hom. IV, *Of Good Works* | Third | 58, l. 25 *(glossary)* | "kneeling, kissing, and **censing** of them" |
| 3 | Bk II, Hom. II, *Against Peril of Idolatry* | Third | c. 232 | "burn **incense**, offer up gold to images" |
| 4 | " | Third | c. 232 | "burning of **incense** and such other, wherewith God in the temple was honoured" |
| 5 | " | Third | c. 232 | "one crumb of **incense** before an image or idol" |
| 6 | " | Third | c. 232 | "burning of **incense** and candles" |
| 7 | " | Third | c. 234 | "burn **incense** before them" |
| 8 | " | Third | 258, l. 7 *(index)* | "candlesticks, **incense-ships**, platters" — in a quotation of **Jerome** |
| 9 | " | Third | c. 264 | "spices and **odours**" — in a quotation of **Lactantius** |
| 10 | " | Third | c. 265 | "ointments, **incense**, and odours" — in a quotation of **Seneca** |
| 11 | " | Third | c. 266 | "offer up **odours and incense** unto them" |
| 12 | " | Third | c. 266 | "one crumb of **incense** before an image" |
| 13 | " | Third | c. 267 | "burn **incense** ... to their books" |
| 14 | " | Third | 270, l. 8 *(glossary)* | "in **censing** of them" |
| 15 | " | Third | c. 271 | "burning of **incense**, offering up of gifts unto images and idols" |

Page numbers marked *(glossary)* or *(index)* come from Griffiths' own finding
aids and are authoritative. The rest are derived by scanning back to the nearest
running-head page marker in the OCR and are given as approximate. One conflict
is recorded: at passage 1 the OCR page marker reads 64 and the glossary reads 54;
the glossary is preferred.

### 1.3 What returned nothing, reported either way

- **`frankincense`: 0** in the body of either Book. It occurs only inside
  Griffiths' own editorial footnote to p. 258.
- **`sweet savour`: 0.** The sacrificial phrase of Leviticus and Ephesians does
  not occur. All eleven `savour` hits are figurative — "savour of death unto
  death", "sweet savouriness", "savouring and tasting not of the flesh but of the
  Spirit".
- **`censer`: 0** in the homily text; footnote only.
- **`perfume`: 1**, and it is not incense — "howsoever thou perfumest thyself" in
  *Against Excess of Apparel*, rebuking bodily vanity.
- **`incensed` (= provoked to anger): 1**, in *Against Wilful Rebellion*.
  Homonym.
- **Parts One and Two of the Homily against Peril of Idolatry: 0.** All thirteen
  are in the Third Part.
- **Every homily on worship as such — *Of the Right Use of the Church*, *Of
  repairing and keeping clean of Churches*, *Of Prayer*, *Of the Place and Time
  of Prayer*, *That Common Prayers and Sacraments ought to be ministered in a
  known Tongue*, *Of the worthy receiving of the Sacrament*: 0.** ⭐ This is not a
  small negative. The Homilies contain a sustained treatment of what belongs in
  a church and what belongs in worship, and incense is not mentioned in any of
  it.

### 1.4 Where the two witnesses differ

**Difference 1, and it changes the sense.** At Griffiths p. 258, inside the
quotation of Jerome's letter to Nepotian:

- **Griffiths:** "the table, candlesticks, **incense-ships**, platters, cups,
  mortars, and other things all of gold"
- **Reformed Anglican page:** "the table, candlesticks, **incense, ships**,
  platters, cups, mortars, and other things all of gold"

Griffiths reads a single compound noun — the incense-boats of the Temple
furniture, rendering Jerome's *thuribula*. The web text splits it into
"incense" and a meaningless "ships". ⚠ **On the web text's reading, incense
appears free-standing in a list of things "allowed of the Lord" under the old
covenant; on the scholarly reading it does not appear as a substance at all.**
Griffiths' own footnote goes further and says the sixteenth-century translator
got even the vessel wrong: *thuribulum* means a censer, not an incense-ship.
Anyone building on a free-standing "incense" here is building on the weaker
witness, against the scholarly edition, against that edition's express note, and
against the Latin.

**Difference 2, immaterial but a search trap.** Griffiths "in **censing** of
them"; the web text "in **sensing** of them". A search of that page for
"censing" returns nothing.

Otherwise the two witnesses agree on the whole inventory. Where the Griffiths
OCR is corrupt at a load-bearing clause, the web text supplies the same reading,
and the clause is secure.

> **VERDICT §1: VERIFIED.** Fifteen relevant occurrences exist, in two homilies —
> Book I Homily IV *Of Good Works annexed unto Faith* (Third Part, 2) and Book II
> Homily II *Against Peril of Idolatry* (Third Part, 13). Zero elsewhere in either
> Book; zero in Parts One and Two of the Peril of Idolatry; zero in every homily
> that treats worship, prayer, the sacrament, or the fabric of the church. No
> occurrence of *frankincense*, *sweet savour*, or *censer* in the homily text.

---

## §2 — What is actually condemned

This is the section the pass turns on.

### 2a. Is incense condemned as such, or in a particular use?

**In a particular use, in all fifteen. Not once as such.**

There is no sentence in either Book whose subject is incense and whose predicate
condemns it. In every one of the fifteen, incense or censing is an act performed
**upon or before an image or idol**, and the sentence's grammatical object is the
image. The recurring formula is "*of them*", "*before them*", "*unto them*",
"*before an image or idol*", "*unto images and idols*".

### 2b. Which use?

Four distinct settings, and they are not evenly weighted:

- **Old Testament idolatry (passage 1).** Israel censing the images of Baal,
  Moloch, Chamos, Baalpeor, Astaroth, Bel, the Brazen Serpent.
- **Pagan Greco-Roman idol-cultus (passages 9, 10, and the frame of 3-7).**
  Reported at second hand, out of Lactantius and Seneca, and used as the
  heathen's own testimony against image-worship.
- **Roman and late-medieval English image-cultus (passages 2, 3-7, 11-15).** The
  bulk of them. Pilgrimage, candles, wax limbs, kneeling, kissing, censing —
  the whole apparatus of the shrine.
- **Jewish ceremonial as superseded (passage 8 only).** The single occurrence in
  that category, inside a quotation of Jerome, and on the scholarly reading the
  word there is a vessel, not the substance.

⭐ **One setting is worth marking because it is the strongest thing in the file
for the other side.** Passages 11-12 are the homily in its own voice, and the
actors it names are Christian clergy: *"it is not enough thus to deck idols, but
at the last come in the Priests themselves, likewise decked with gold and
pearl... and then rising up again, offer up odours and incense unto them."* This
is the one place in either Book where the censing described is done by Christian
ministers in a Christian church. **It is still censing of images.**

⛔ **AND ONE PASSAGE CUTS THE OTHER WAY HARDER THAN ANYTHING IN THE FILE CUTS
AGAINST INCENSE.** Passage 4:

> "And in the second of Paralipomenon, the twenty-ninth chapter, all the outward
> rites and ceremonies, **as burning of incense and such other, wherewith God in
> the temple was honoured**, is called *Cultus*, to say worshipping; which is
> forbidden straitly by God's word to be given to images."

*(Reformed Anglican witness; Griffiths agrees, its OCR of this clause being
partly mangled but concordant.)*

The homily's premise here is that **burning incense is an act by which God was
honoured** — worship, *Cultus*. Its conclusion is that such worship must not be
given to images. **The argument needs incense to be a real honour paid to God in
order to work.** The fault the homily locates is in the recipient.

### 2c. Does the passage distinguish the substance from the ceremony?

**No — and the absence is itself the finding. PARTIAL.**

Nowhere in either Book is there a sentence distinguishing the material (incense)
from the act (censing), or asking whether the material is lawful apart from the
act. The homilies never reach that question, because incense is never the topic.
The distinction the homilies do draw is a **different one from the project's
working patristic distinction**, and this must be said plainly:

- **The project's working position on the fathers:** incense offered *as
  sacrifice* is condemned; incense as such is not. The distinction is by **mode**.
- **What the Homilies actually draw:** incense offered *to an image* is
  condemned; incense as an honour to God in the Temple is presupposed lawful
  (passage 4). The distinction is by **recipient**.

These are not the same distinction. ⚠ **Do not treat the Homilies as a second
witness to the patristic distinction. They are a witness to a different one.**
That the Homilies' distinction happens to be, if anything, *more* permissive than
the fathers' is a separate matter and is not a reason to conflate them.

### 2d. Named in its own right, or only inside a list?

**Inside a list, in fourteen of fifteen.** The standing company is: candles,
gold, silver, ships, crutches, chains, wax legs and arms and whole bodies,
kneeling, capping, kissing, pilgrimage. The syntax is uniformly serial.

The nearest thing to a standalone mention is passage 4 — and there incense is
named as a thing **wherewith God was honoured**.

Passage 13 must be flagged for a different reason: **it is a rhetorical question
inside a reductio**, not a declarative. *"Do men kneel before their books, light
candles at noon time, burn incense, offer up gold and silver, and other gifts to
their books?"* The homily is arguing that images cannot be the books of the
laity, because nobody treats books this way. ⚠ Quoted flat, it reads as a
condemnation of burning incense. It is not one. Per project rule, rhetorical
content is not to be redeployed as assertion.

### 2e. The one ambiguity, kept live and unresolved

Passage 15, the closing exhortation, will bear two readings and this pass does
not choose between them.

> "...he will be honoured and worshipped, not in, nor by images or idols, which
> he hath most straitly forbidden, neither in kneeling, lighting of candles,
> burning of incense, offering up of gifts unto images and idols, to believe
> that we shall please him, for all these be abomination before God."

- **Reading A (object-governed).** "unto images and idols" governs the whole
  series; and "to believe that we shall please him" qualifies it further. What is
  called abomination is the series *as directed to images, in the belief that so
  directing it pleases God*. On this reading passage 15 says nothing whatever
  about incense offered to God.
- **Reading B (series-final).** "unto images and idols" attaches only to the last
  member, "offering up of gifts". "Neither in" parallels "not in" and excludes
  kneeling, candles and incense as modes of honouring God at all. On this reading
  the homily does condemn burning incense as a way of worshipping God.

Reading A is the more natural on the syntax and is the one the parallel
constructions at passages 14 and 3-7 support, every one of which is
object-governed. Reading B is not idle: "neither in" does echo "not in", and the
list at passage 14 is introduced by "True religion... standeth not in", which is
about what religion consists in rather than about images alone. **Both readings
stay live.** If this is ever put to RJ, it goes as a question about which reading
the sentence takes, not as an assertion that it takes one.

> **VERDICT §2: VERIFIED, with one reservation and one correction.**
> **(a) VERIFIED** — incense is condemned in a particular use, never as such.
> **(b) VERIFIED** — the use is incense offered to images and idols, in four
> settings, of which contemporary image-cultus is the dominant one; Jewish
> ceremonial-as-superseded accounts for one occurrence only, and there the word
> is a vessel.
> **(c) PARTIAL** — no substance/ceremony distinction is drawn anywhere. ⛔ AND
> THE CORRECTION: the Homilies do **not** make the fathers' distinction. Theirs
> is by recipient, not by mode. They are not a second witness to the patristic
> point and must not be cited as one.
> **(d) VERIFIED** — incense is named inside a list in fourteen of fifteen; the
> fifteenth names it as an honour paid to God.
> **The consequence for the occasion of this pass, stated plainly: the Homilies
> do not contain a condemnation of incense as such, and the Archbishops' phrase
> "some expressions in the Homilies which have that character" concedes more than
> the text requires.** On the strongest reading available to the other side, what
> the Homilies condemn is censing images. The one sentence that could be read
> more broadly (passage 15) is recorded above with both readings live.

---

## §3 — Relation to *Of Ceremonies*

Pass 260835-57 established that "Of Ceremonies, why some be abolished, and some
retained" supplies a category between *evil in itself* and *merely imprudent* —
ceremonies indifferent in themselves, abolished because **"the abuses could not
well be taken away, the thing remaining still."** That finding is not re-derived
here.

### 3a. The Homily runs the *Of Ceremonies* argument — against images

⭐⭐ **The Homily against Peril of Idolatry does not merely sit near the "things
indifferent" category. It engages it by name, states the opposing use of it, and
rules images out of it by exactly the inseparable-abuse reasoning that "Of
Ceremonies" uses.**

It states the opponent's position (Griffiths p. 221):

> "...and that therefore we may have images, so we worship them not, for that
> they be **things indifferent, which may be abused, or well used**"

And then rules against it (Griffiths pp. 223-224):

> "...idolatry is to images, specially in temples and churches, **an inseparable
> accident** (as they term it); so that images in churches and idolatry go always
> both together, and that therefore the one cannot be avoided except the other...
> Whereupon it followeth, that our images in churches have been, be, and ever
> will be none other but abominable idols, and be therefore **no things
> indifferent**."

*(Griffiths, corroborated by the second witness. Griffiths' index carries the
entry "images in churches not things indifferent".)*

Set that beside "Of Ceremonies": *"the most weighty cause of the abolishment of
certain Ceremonies was, That they were so far abused... that the abuses could not
well be taken away, the thing remaining still."* **Same move.** The Homily is
running the formulary's own argument, at greater strength — "Of Ceremonies"
abolishes for inseparable abuse while leaving the thing indifferent; the Homily
goes further and denies that images were ever indifferent at all.

### 3b. And it withholds that move from incense

⭐ **This is the finding of the section.** The Homily has a fully-built machine
for saying "this thing is not indifferent, because its abuse is inseparable from
it". It runs that machine on images. **It never runs it on incense.** Incense
never appears as a candidate ceremony to be assessed; it appears only as one act
in the list of things done to images. There is no sentence anywhere in either
Book that asks whether incense is indifferent, whether its abuse is separable, or
whether it should be retained or abolished.

### 3c. So: inside, outside, or in tension?

- **On Reading A of passage 15 (§2e), the Homilies' language sits INSIDE the *Of
  Ceremonies* category, and below it.** Nothing in the Homilies calls incense
  evil in itself; nothing in them even assesses incense as a ceremony. What they
  condemn is a use, and the recipient is the fault. That is fully compatible with
  incense being a ceremony indifferent in itself — and the Homilies do not even
  take the further step "Of Ceremonies" takes of abolishing it for abuse, because
  they never consider it.
- **On Reading B, there is a genuine TENSION** — not with "Of Ceremonies"
  directly, but between two formulary-level texts. "Of Ceremonies" says abolished
  ceremonies were abused, not evil, and that retained ones "may be altered and
  changed, and therefore are not to be esteemed equal with God's Law." Reading B
  would have a homily commended by Article 35 calling one such ceremony
  "abomination before God" irrespective of its object. That is a stronger word
  than "Of Ceremonies" ever uses of any ceremony.

**Recorded neutrally, as the brief requires:** the tension, if it exists, is
generated by Reading B, and Reading B is the minority reading of one sentence.
It is not generated by the other fourteen occurrences, none of which strains
against "Of Ceremonies" at all.

> **VERDICT §3: PARTIAL.** On the dominant reading the Homilies' incense language
> sits **inside** the *Of Ceremonies* category and does not even reach the
> abolished-for-abuse tier, because the Homilies never assess incense as a
> ceremony at all. On the minority reading of a single sentence there is a real
> tension between two formulary texts, and it is recorded rather than resolved.
> ⭐ The substantive finding of this section is independent of that ambiguity:
> **the Homily against Peril of Idolatry builds and deploys the exact
> inseparable-abuse argument that "Of Ceremonies" uses, deploys it against
> images, and withholds it from incense.**

---

## §4 — The authority question

### 4a. Article 35, exact wording

Four witnesses were compared and are captured in full in
`SRC_PRIMARY_1571_Articles-of-Religion_Article-35-Of-the-Homilies-and-Later-Forms.txt`.

**The 1571 English text and the Church of England's current official text agree
word for word:**

> "The second Book of Homilies, the several titles whereof we have joined under
> this Article, doth contain a godly and wholesome Doctrine, and necessary for
> these times, as doth the former Book of Homilies, which were set forth in the
> time of Edward the Sixth; and therefore we judge them to be read in Churches by
> the Ministers, diligently and distinctly, that they may be understanded of the
> people."

Followed by the list of the twenty-one titles, of which **no. 2 is "Against peril
of Idolatry"**.

⚠⚠ **A DIVERGENCE IN THE REPOSITORY'S OWN 1662 FILE, FLAGGED FOR JD.**
`src/the-book-of-common-prayer-1662.pdf` (a modern typeset transcription by
Charles Wohlers, not a facsimile — the same file the 260835-57 capture header
already describes) reads **"in *the* Churches"** and **"understanded *by* the
people"**, against all three other witnesses. Neither changes the sense; both
break a verbatim quotation. ⛔ **Do not deploy a verbatim Article 35 from that
PDF.** This pass is read-only and has changed nothing.

**Does the Article speak to doctrine, to ritual, or to both?** It speaks to
**doctrine**, and only to doctrine: "doth contain a godly and wholesome
**Doctrine**, and necessary for these times". The word *ritual* does not appear,
nor any equivalent. What the Article adds beyond the commendation is not a
doctrinal ranking but an **order**: "we judge them to be read in Churches by the
Ministers, diligently and distinctly."

### 4b. Rubrics and canons directing the Homilies to be read

- **The 1662 Communion office, standing rubric before the Offertory:** *"Then
  shall follow the Sermon, **or one of the Homilies** already set forth, or
  hereafter to be set forth, by Authority."* The Homilies stand in the body of
  the eucharistic rite as the appointed alternative to the sermon.
- **The following 1662 rubric** treats the two as interchangeable: *"after the
  Sermon or Homily ended"*.
- **State Service, 5 November:** *"After the Creed, if there be no Sermon, shall
  be read one of the six homilies against Rebellion."*
- **State Service, 30 January:** *"After the Nicene Creed, shall be read, instead
  of the Sermon for that Day, the first and second parts of the Homily against
  Disobedience and wilful Rebellion... or the Minister... shall preach a Sermon of
  his own composing upon the same argument."*
- **Canon 46 (1604):** where there is no sermon, the minister *"shall read some
  one of the Homilies prescribed or to be prescribed by authority."*
- **Canon 49 (1604):** an unlicensed minister *"shall only study to read plainly
  and aptly (without glossing or adding) the Homilies."*
- **Canon 80 (1604):** every parish must be furnished with *"the Books of
  Homilies allowed by authority"*, at the parish's charge, alongside the Bible
  and the Prayer Book.
- ⭐⭐ **Canon 85 (1604):** churchwardens shall keep the church *"in such an
  orderly and decent sort, without dust or any thing that may be either noisome
  or unseemly, as best becometh the House of God, **and is prescribed in an
  Homily to that effect**."* A canon making the ordering of the church building
  conform to what a homily prescribes.

### 4c. The American church

**Article 35 was retained, text intact and title-list intact**, in the Articles
"established by the Bishops, the Clergy, and the Laity of the Protestant
Episcopal Church in the United States of America, in Convention, on the twelfth
day of September, in the Year of our Lord, 1801", and it stands so in the 1928
book. The 1801 revision then added, in brackets in the text:

> "[This Article is received in this Church, so far as it declares the Book of
> Homilies to be an explication of Christian doctrine, and instructive in piety
> and morals. But all references to the constitution and laws of England are
> considered as inapplicable to the circumstances of this Church; which also
> suspends the order for the reading of said Homilies in churches, until a
> revision of them may be conveniently made, for the clearing of them, as well
> from obsolete words and phrases, as from the local references.]"

Two moves, and they should not be run together:

1. **A reception limit on what the Article declares** — received so far as it
   declares the Homilies "an explication of Christian doctrine, and instructive
   in piety and morals".
2. **A suspension of the duty to read them**, expressly temporary ("until a
   revision of them may be conveniently made"), and expressly for reasons of
   language and locality ("obsolete words and phrases... local references"), not
   of content.

⚠ Note what the American clause does **not** do. It does not lower the Homilies'
authority; it fixes what the Article is received as declaring, and it suspends a
practical order for stated non-doctrinal reasons. And it says nothing at all
about ritual or ceremonial in either direction.

### 4d. Is the Archbishops' ranking a fair reading of Article 35?

The sentence at issue has two halves, and they do not fare alike.

**The case that the ranking is fair:**

- Article 35's operative verb is commendatory — the Homilies "contain" godly
  doctrine "necessary for these times". A time-indexed commendation of teaching
  is not an enactment.
- The Article legislates one thing only: that they be read aloud. Canons 46 and
  49 confirm exactly that character — a homily is what stands in for a sermon
  where there is no preacher, and the unlicensed reader must deliver it "without
  glossing or adding". That is homiletic matter, not a code.
- **The Homilies are hortatory in form**, and demonstrably so: §2d found the
  strongest-sounding incense sentence in the corpus to be a rhetorical question
  inside a reductio.
- **The American church itself did what the Archbishops describe** — it received
  the Article as declaring the Homilies an explication of doctrine and
  instructive in piety and morals, and suspended their reading.
- On **ritual** specifically, Article 35 says nothing whatever. A text silent on
  ritual is a thin basis for high authority on ritual.

**The case that the ranking is contestable:**

- ⭐⭐ **The "doctrine" half runs into Article XI.** Article XI, *Of the
  Justification of Man*, ends: *"Wherefore, that we are justified by faith only
  is a most wholesome doctrine, and very full of comfort; **as more largely is
  expressed in the Homily of Justification**."* An Article of Religion refers a
  point of doctrine out to a homily for its fuller expression. It is hard to
  square that with "have never been taken as having high authority on points of
  doctrine". The Archbishops wrote *doctrine or of ritual*, and the doctrine
  half has a direct counter-instance inside the Articles themselves. ⭐⭐ **And
  the American church kept that counter-instance.** Article XI in the 1801
  Articles, as printed in the 1928 book, retains the clause word for word: *"as
  more largely is expressed in the Homily of Justification."* So the same
  revision that added the limiting bracket to Article 35 left standing an
  Article that refers a doctrine out to a homily.
- ⭐ **The "ritual" half has a counter-instance too, in Canon 85**, which makes
  churchwardens' duty about the ordering of the church conform to what "is
  prescribed in an Homily to that effect". That is a homily operating
  prescriptively, by canon, on a question of ceremonial order.
- **Article 35 is one of the subscribed formularies**, and its language is "we
  judge them to be read" — a judgement of the Church, not a recommendation.
- The State Services do not permit a homily as an option; on those days they
  **command** a named homily where there is no sermon, and require a substituted
  sermon to be on the homily's own argument.
- "Hortatory rather than imperative" describes the Homilies' **rhetorical form**.
  Whether a text's form is hortatory and whether the Church has invested it with
  authority are two different questions, and the Archbishops' sentence moves from
  the first to the second without an argument.

**Not argued for here.** Both cases are set out; neither is adopted.

> **VERDICT §4: PARTIAL — the Archbishops' ranking is CONTESTABLE, and it is
> weaker on doctrine than on ritual.**
> **(a)** Article 35's 1571 and current official wording are identical; it speaks
> expressly to **doctrine** and not at all to ritual, and it issues one order —
> that the Homilies be read. ⚠ The repository's 1662 PDF diverges from every
> other witness at two points and must not be quoted verbatim.
> **(b)** The Homilies are directed to be read by the 1662 Communion rubric, by
> two State Service rubrics that command a named homily, and by Canons 46, 49
> and 80; Canon 85 makes a homily prescriptive on a point of church order.
> **(c)** The American church **retained** Article 35 entire in 1801, adding a
> bracketed clause that receives it as declaring the Homilies an explication of
> doctrine and instructive in piety and morals, and that suspends the order to
> read them pending revision for obsolete language and local references. The
> clause is silent on ritual.
> **(d)** The "ritual" half of the Archbishops' sentence is defensible on
> Article 35's silence, and is met by Canon 85. **The "doctrine" half is met
> head-on by Article XI**, which sends a point of doctrine out to the Homily of
> Justification for its fuller expression.

---

## §5 — Prior use of this argument

**Question:** has anyone in the period used the Homilies *against incense* — in
the 1899 proceedings, in the 1866-1874 American material already in `src/`, or in
the English ritual controversy?

### 5a. What was searched

Every `.txt` in `~/EMC/theology/src` was searched, case-insensitively, for
`Homilies`, `Homily`, `Article XXXV`, `Article 35`, `Peril of Idolatry`,
`Idolatry`, `idolatr`. The Westall PDF was searched twice: once via the
repository's existing extraction `SRC_PRIMARY_1899_Westall_Case_For_Incense.txt`
(329,971 characters), and once via a fresh `pdftotext -layout` of
`SRC_PRIMARY_1899_Westall_Case_For_Incense-bwb_C0-AUU-939.pdf` (525,535
characters — the difference is layout whitespace; both extractions begin and end
at the same text, so no pages are missing from the repository copy).

### 5b. What was found

| Source in `src/` | Result |
|---|---|
| `SRC_PRIMARY_1899_Westall_Case_For_Incense*` (both extractions, and the PDF) | **Zero.** No occurrence of "Homilies", "Book of Homilies", "Article XXXV", or "Peril of Idolatry". The only `Homil-` strings are patristic citation abbreviations — "Origen, *Homil. in lib. Judic.* iii. 2" and "St. Basil, *Homilia in Gordium Martyrem*, § 2". The single `idolatr` hit is about the Seventh Œcumenical Council and the Incarnation, not about the Books of Homilies. ⛔ **Westall does not address the Homilies at all, and therefore does not answer the Archbishops' concession.** |
| `SRC_PRIMARY_1899_Archbishops_Lambeth-Opinion-Incense-Lights.txt` | The concession itself, and nothing more. The Archbishops name the Homilies, characterise them, rank them, and move on. They cite no homily, no passage, and no page. |
| `SRC_PRIMARY_1906_RoyalCommission_Ecclesiastical-Discipline-Incense.txt` | Quotes the Archbishops' sentence back verbatim, as a quotation. No independent use, no citation of any homily. |
| `SRC_PRIMARY_1874_DeKoven_Canon-On-Ritual-Speech_ProjectCanterbury.txt` | Cites the Homilies four times — but on the **Eucharist**, arguing from the advertisement annexed to the first Book about "the due receiving of his blessed Body and Blood under the form of bread and wine". Nothing about incense. |
| 1866-1874 American material — `1868_GeneralConvention_Journal_Five-Bishops-Appointment`, `1871_GeneralConvention_Journal_Five-Bishops-Ritual-Report`, `1874_GeneralConvention_Journal_Canon-20-Title-I` | **Zero.** |
| English ritual controversy — `1868_ArchesCourt_Martin-v-Mackonochie-Incense`, `1868_PrivyCouncil_Martin-v-Mackonochie-Incense-Obiter`, `1868_RoyalCommission_Ritual_Second-Report-Lights-Incense`, `1870_ArchesCourt_Elphinstone-v-Purchas-Incense`, `1895_Roberts_ECU-History` | **Zero.** |
| `SRC_PRIMARY_2003_Brattston_Incense_in_Ante-Nicene_Christianity.txt` | Mentions homilies, but patristic ones. Out of period and off the question. |

### 5c. What this means, stated carefully

The Homilies-against-incense argument **does not appear in any source the
repository holds**. The Archbishops raise the Homilies unprompted, in order to
dismiss them, and nobody in the sources — not the ritualist advocate whose whole
book is the case for incense, not the Royal Commission that quotes the Opinion,
not the American ritual proceedings, not the English case law — takes the point
up in either direction.

⚠ **The limit of this finding, so it is not overstated.** The corpus searched is
the repository's `src/`, not the whole of the 1899 proceedings or the whole
ritual-controversy literature. The correct claim is: *within the sources this
project holds, the argument is unused.* Whether it was used in material the
project has not gathered is not established here. Establishing it would need the
Lambeth hearing papers and the ritualist pamphlet literature, neither of which is
in `src/`.

> **VERDICT §5: UNMATCHED, with a search record.** No use of the Homilies against
> incense was found in any source in `src/`. Westall — checked specifically, per
> the brief, in both the repository extraction and a fresh extraction of the PDF —
> **does not address the Books of Homilies anywhere**, and so does not answer
> them. The 1906 Royal Commission reproduces the Archbishops' concession as a
> quotation without adding to it. DeKoven cites the Homilies on the Eucharist, not
> on incense. The 1866-1874 American material and the English ritual-controversy
> sources yield nothing. The finding is bounded by the corpus searched.

---

## Deployment notes

1. ⛔ **Nothing in this file is quotation-ready for outward-facing use.** Per
   project rule, a verbatim quote must come from the actual source file, and the
   scholarly edition here was worked from an OCR text layer with known
   corruption. Before any Homilies quotation is deployed, a clean copy of a named
   edition must be obtained for that purpose. The extracts in the capture files
   are for analysis and navigation.
2. ⛔ **Do not deploy a verbatim Article 35 from `src/the-book-of-common-prayer-1662.pdf`** —
   see §4a.
3. ⚠ **Passage 13 is a rhetorical question inside a reductio** (§2d). It is the
   passage most likely to be quoted flat as a condemnation of burning incense. It
   is not one.
4. ⚠ **Do not cite the Homilies as a second witness to the patristic
   sacrifice/honour distinction** (§2c). They draw a different distinction.
5. ⚠ **Passage 15 bears two readings and neither has been chosen** (§2e). If it
   goes to RJ it goes as a question about which reading the sentence takes.
6. ⚠ **A live datum in the repository bears on deployment and should be read
   before this material is used with RJ.** `St_Francis_EMC_Distinctives.md`
   records that RJ has stated disagreement with "certain Homilies", and records a
   further statement bearing specifically on the anti-image Homily. That record
   is not restated or re-attributed here; the entry and its own attribution
   layers are in that file and should be read there. It matters because the
   Homily against Peril of Idolatry is the one homily this pass is about.

## Owed work, not done by this pass

- The Griffiths text was worked from an OCR layer. A clean text of a named
  edition is owed before quotation.
- The 1571-vs-1662 comparison at §4a rests, on the 1571 side, on an unattributed
  transcription that agrees with the Church of England's current official text.
  It is not a collation against a sixteenth-century printing.
- §5's negative is bounded by `src/`. The Lambeth hearing papers and the
  ritualist pamphlet literature have not been searched.
- Whether the Archbishops had a specific passage in mind when they wrote "some
  expressions in the Homilies which have that character" is not established. They
  cite none. On the evidence of §1 and §2 the candidates are passages 13 and 15,
  and neither will carry the weight without the reading recorded at §2e.
