# Incense Reply — Source Checks

**Last updated: 260835-65** (created 260835-57; date-stamped, format yymmdd-iteration) ⛔⛔ **260835-65 — THIS DOCUMENT'S SOURCE-OF-RECORD DESIGNATION FOR DE KOVEN IS WITHDRAWN AT TWO LOCI (§3 and §5), BY DATED NOTE, ON `260835-64`'s FINDING AND IN `260835-64`'s DRAFTED WORDING.** ⛔ **THE PAMPHLET IS NOT THE SOURCE OF RECORD FOR EITHER TEXT. The stenographic *Debates of the House of Deputies … 1874* is, and the two differ at the points this document turns on.** ⚠️⚠️ **CONSEQUENCE THAT TRAVELS WITH EVERY QUOTATION BELOW: every verbatim De Koven quotation in this file is pamphlet-sourced and must be re-verified against the Debates before outward deployment. That re-verification was NOT run by this pass and is owed.** ⛔ **No original sentence altered, no verdict changed, no finding added or revised, nothing minted.** ⭐ **REGISTERED in `PROJECT_STATE.md` §4 by this pass (JD's ruling; previously carried as owed at `260835-58`).**

---

## What this document is

Five discrete source checks, run as one pass, each ending in an explicit verdict in
one of these forms: **VERIFIED**, **FALSIFIED**, **PARTIAL**, **UNMATCHED**. Occasion:
RJ's Discord reply advancing a two-option frame (prudential objection to incense is
permissible; objection in principle on theological grounds is blasphemy of Scripture),
citing DeKoven's 1874 speech and Canon 20, Title I.

⛔⛔⛔ **HARD RULE OBSERVED THROUGHOUT: nothing was translated by this pass.** Every
English rendering of Justin and Irenaeus below is the published Ante-Nicene Fathers
translation, quoted verbatim from the capture file, with translator and edition
recorded.

⭐ **All material relied on was CAPTURED to `src/`, not merely cited** — five new
capture files, listed at §6. **No existing corpus file was modified by this pass.**
Every figure in the brief was re-derived (the brief's HEAD figure was stale; see §0).

**Attribution layers used below:** `[Stated]` = verbatim from the capture file;
`[Stated-Analysis]` = labelled inference from something stated; `[Analysis]` = this
project's own argument.

---

## §0. Gate

| Item | Value |
|---|---|
| Briefed HEAD | `2e38b41` |
| HEAD at session start | `76f6cd1` (260835-56 pass artifacts) — **brief's figure was stale** |
| HEAD at write-up | `2ed1c2a` (260835-56 corpus commit: "source checks file and 19 captures") — committed by JD mid-pass |
| `git --no-optional-locks status --short` at write-up | five `??` entries, all this pass's captures; nothing else |
| Validator BEFORE and at write-up | `98 ok · 11 warnings · 0 errors`, coverage `C0 34 · C1 5 · C2 1 · C3 28 · C4 3 · C5 22 · C6 5 · C7 2 · C8 31 · C9 1 · C10 1 · C11 2 · C12 2` — matches the briefed baseline; ⚠️ **C0 examines 34 files and C6 hashes 5: neither sees the 260835-56 captures nor this pass's. See §7.** |
| Stamp | **260835-57**, derived by grep after reading the 260835-12/14 hazard note: distinct-stamp sweep over tracked `*.md/*.py/*.txt` runs unbroken `260835-1 … 260835-56`; `260835-57` returned exactly TWO hits, both opened and both absence-assertions ("`260835-57` and above return ZERO") in `Ceremonial_Meaning_Source_Checks.md` L57 and `passes/260835-56_…_close-out.md` L48 — content hits, not consumptions; `260835-58`, `260835-59`, `260836-1` return ZERO; `260835-99` re-confirmed NOT a stamp. |
| Web access | Confirmed working (New Advent, Project Canterbury, archive.org all fetched). Sandbox shell has NO network; captures went via the fetch tool and the built-in browser pane (Claude in Chrome was offline). |

---

## §1. Justin Martyr on Malachi 1:11

**Capture:** `src/SRC_PRIMARY_0155_Justin_Martyr_Malachi-1-11_Dialogue-28-41-116-117_1Apology-10-13_ANF1.txt`
(Dods & Reith, ANF 1, 1885, via New Advent) and
`src/SRC_PRIMARY_0180_Irenaeus_Against-Heresies_IV-17-5-6_Malachi-Incense-Prayers_ANF1.txt`
(Roberts & Rambaut, ANF 1, 1885, via New Advent).

### 1a. Where Malachi 1:10-12 occurs in the Dialogue

All nine New Advent pages of the Dialogue were fetched and searched for "rising of the
sun", "Malachi 1" and "incense". Hits: **chs. 28, 41, 116-117** (the same four sites
Westall, *Case for Incense* 1899 p. 48 n. 2, lists from Warren). Ch. 22 hits "rising of
the sun" only inside Psalm 49. Ch. 78's "incense" is the Magi's gift. No other site.
The brief's "41 is a probable second site" — ✅ confirmed; and **28 is a third**, which
the brief did not list.

### 1b. Does Justin name incense, and does he deny that God receives it?

| Site | Names incense? | What Justin says |
|---|---|---|
| Dial. 28 | ❌ Not in his quotation of Malachi ("in every place a sacrifice is offered unto My name, even a pure sacrifice") | Uses the verse against circumcision-as-sign; adds "God rejoices in his gifts and offerings" of the Gentile who keeps the decrees. No comment on incense. |
| Dial. 41 | ✅ **In the quotation only**: "in every place incense is offered to My name, and a pure offering" | `[Stated]` "He then speaks of those Gentiles, namely us, who in every place offer sacrifices to Him, i.e., the bread of the Eucharist, and also the cup of the Eucharist". **Incense is quoted and then passed over in silence** — neither affirmed nor denied. |
| Dial. 116 | ❌ | "in every place among the Gentiles sacrifices are presented to Him well-pleasing and pure. Now God receives sacrifices from no one, except through His priests." |
| Dial. 117 | ❌ **Incense does not appear in the chapter at all**; his quotation there omits the incense clause ("my name is glorified among the Gentiles (He says); but you profane it") | `[Stated]` "Now, that prayers and giving of thanks, when offered by worthy men, are the only perfect and well-pleasing sacrifices to God, I also admit. For such alone Christians have undertaken to offer, and in the remembrance effected by their solid and liquid food, whereby the suffering of the Son of God which He endured is brought to mind". |
| 1 Apol. 10 | ❌ | "God does not need the material offerings which men can give". |
| 1 Apol. 13 | ✅ **In his own voice** | `[Stated]` "declaring, as we have been taught, that He has no need of streams of blood and libations and incense; whom we praise to the utmost of our power by the exercise of prayer and thanksgiving". |

`[Stated-Analysis]` Justin's word in every place is **need** (1 Apol. 10, 13; Dial. 22 "not
… because they are needful to Him") — not "receive". The one place he uses "receives"
(Dial. 116) is a positive statement about priestly mediation, not a denial. **He nowhere
says God does not *receive* incense.** The nearest thing is 1 Apol. 13's "no need of …
incense", which is a different claim and is made in the Apology, not the Dialogue.

### 1c. What does he identify the pure offering as?

`[Stated]` Dial. 41: "the bread of the Eucharist, and also the cup of the Eucharist".
Dial. 117: "the sacrifices which we offer through this name … i.e., in the Eucharist of
the bread and the cup", which he then glosses as "prayers and giving of thanks … in the
remembrance effected by their solid and liquid food". `[Stated-Analysis]` The offering is
the Eucharistic bread and cup, understood as the vehicle of prayer and thanksgiving. The
brief's "prayers and thanksgivings" is half of what he says; the Eucharistic half is the
half RJ will cite (RJ_Incense_Analysis.md §4.13(i) already has RJ reading these two
chapters on video).

### 1d. 1 Apology 13 — does it make the same move?

No. It makes a **different and stronger** move: God has no need of incense (named), and
Christians honour Him by prayer and thanksgiving and by *not* consuming by fire what He
made for sustenance. It does not cite Malachi. It is the only place Justin names incense
in his own voice, and it is a non-need argument about worship in general, not an
exegesis of the "pure offering".

### ⭐ Verdict on the working premise: **PARTIAL**

- "Justin is the fountainhead of the patristic eucharistic reading" — **not verifiable
  from this pass**; he is the earliest writer captured who reads the *minchah* as the
  Eucharist (Irenaeus follows c. 180). "Fountainhead" is a claim about priority that
  would need the Didache and dating arguments; not attempted. Treat as plausible,
  unverified.
- "explicitly denies that God receives incense or material offerings" — **FALSIFIED as
  to the Dialogue chapters on Malachi.** Incense is never discussed in 28, 41, 116 or
  117; in 41 he quotes the incense clause and says nothing about it. The denial of *need*
  for incense is in 1 Apol. 13, a different work, and is "need", not "receive".
- "identifying the Malachi pure offering with prayers and thanksgivings" — **VERIFIED
  with a rider**: he identifies it with the Eucharistic bread and cup AND with prayers and
  thanksgivings, in the same breath (117), and the Eucharistic identification is the
  primary one (41).

⛔ **Deployment caution.** Quoting Dial. 117's "prayers and giving of thanks … are the only
perfect and well-pleasing sacrifices" without "in the remembrance effected by their solid
and liquid food" hands RJ a legitimate grievance in thirty seconds. Both halves or
neither.

### 1e. Second question — has any writer used Justin's reading against the ceremonial argument?

Searched: the two Justin captures; Irenaeus AH IV.17 (fetched and captured); the repo's
`Protestant_Commentary_Survey_Malachi_1_11.md`, `Patristic_Citations_Incense_Verification.md`,
`Tertullian_Incense_Passages.md`, `RJ_Incense_Analysis.md`; the Westall 1899 and
Brattston 2003 captures in `src/`; the Lambeth Opinion 1899 capture (zero hits on
Justin/Malachi/Irenaeus).

Findings, in date order:

1. **Irenaeus, AH IV.17.6 (c. 180)** — the earliest writer to gloss the *incense* of
   Mal 1:11 rather than pass over it: `[Stated]` "Now John, in the Apocalypse, declares
   that the 'incense' is 'the prayers of the saints.'" ⚠️ **Not an argument against a
   ceremonial practice** (there was none to argue against); it is the reading, not the
   deployment. Captured because it is the patristic root of the incense-as-prayer
   reading that later Protestant commentators attribute to "Irenaeus, Tertullian and
   Augustine" (Trapp 1660, Tier 2 in the Survey) and that Barnes 1870 reproduces.
2. **Trapp, c. 1660** (Survey §2 entry 4, Tier 2) — yokes Mal 1:11, Ps 141:2, Rev 5:8,
   Rev 8:3-4 and reads all four figuratively, attributing the reading to the Fathers.
   Does not name Justin.
3. **Perowne, Cambridge Bible 1890** (Survey entry 17, Tier 2) — ✅ **the one located
   instance that deploys Justin's own qualification against the Eucharistic *minchah*
   reading and, through it, against the incense inference**: argues it was "too hastily
   assumed" that the early writers put the Eucharistic interpretation on the *minchah*,
   reading Justin from his statement that prayers and thanksgivings are the only perfect
   sacrifices. Tier 2 only; not re-verified this pass.
4. **Brattston 2003** (`src/`, Tier 3 assessed in `Brattston_Article_Assessment.md`)
   asserts the ante-Nicene writers "took pains to demonstrate that [incense] was not part
   of the Christian cultus" and cites Irenaeus and Eusebius (Dem. Ev.) for incense =
   prayer. Eusebius not fetched this pass.

**Verdict on the second question: PARTIAL.** No patristic writer uses Justin against a
ceremonial argument. Perowne (1890) does, at Tier 2. Irenaeus supplies the patristic
incense-as-prayer gloss that the later Protestant deployment rests on.

---

## §2. Canon 20, Title I, as enacted

**Capture:** `src/SRC_PRIMARY_1874_GeneralConvention_Journal_Canon-20-Title-I_Ritual-Canon-Sequence.txt`
— Journal of the General Convention of 1874 (Hartford, 1875), archive.org
`journalofproceed1874phil`, extracts A–J with printed page numbers; and the pamphlet's
"THE CANON AS FINALLY PASSED" in the DeKoven capture (§3), which agrees verbatim in
substance.

### 2a. Operative wording as enacted (Journal pp. 183-185; extract H; Digest renumbers Canon 20 → Canon 22)

`[Stated]` "§ II. [1.] If any Bishop have reason to believe, or if complaint be made to
him in writing by two or more of his Presbyters, that within his jurisdiction ceremonies
or practices not ordained or authorized in the Book of Common Prayer, and setting forth
or symbolizing erroneous or doubtful doctrines, have been introduced by any Minister
during the celebration of the Holy Communion (such as a. The Elevation of the
Elements … as objects toward which adoration is to be made; b. Any act of adoration of
or toward the Elements in the Holy Communion, such as bowings, prostrations, or
genuflections; and c. All other like acts not authorized or allowed by the Rubrics of the
Book of Common Prayer); It shall be the duty of such Bishop to summon the Standing
Committee as his Council of Advice, and with them to investigate the matter." (OCR
readings normalised only in this quotation; the capture keeps the OCR as read.)

### 2b. Conduct-based or symbolic?

**Conjunctive and symbolic.** Two facts must both be found: (i) not ordained or
authorized in the BCP, **and** (ii) "setting forth or symbolizing erroneous or doubtful
doctrines". This was the Committee of Conference's deliberate restoration: the House of
Bishops on 29 Oct. had made the test **disjunctive** (Bishop of Western New York's
amendment, adopted: "which set forth or symbolize erroneous or doubtful doctrines, **or**
ceremonies or practices not ordained or authorized"; Journal p. 334, extract F; Message
63, extract G), and the Deputies refused to concur (30 Oct., p. 178). DeKoven on 31 Oct.
named exactly this: the conference text "requires two facts to be proved … First, That
they symbolize erroneous or doubtful doctrines; and, Second, That they are not
authorized or ordained in the Book of Common Prayer" (DeKoven capture L1218-1225).
✅ **260835-55's "symbolic" is CONFIRMED, and sharpened: the test is symbolic-AND-
unauthorised, and the symbolic limb was fought for and won against the Bishops' attempt
to make unauthorised-alone sufficient.**

The three examples are introduced by "such as" and are illustrative, not an exhaustive
list; (c) "All other like acts" is tied to acts of adoration toward the Elements
(260835-54's grammatical observation stands).

### 2c. The struck clause

The Journal preserves it three times (extracts A, B/C variants, E). As passed by the
Deputies 27 Oct. and sent to the Bishops (Message 43, p. 320): `[Stated]` "(and, as
examples, the following are declared to be considered as such: a. The use of incense.
b. The placing, or carrying, or retaining a Crucifix in any part of the place of public
worship. c. The Elevation of the Elements … d. Any act of adoration of or toward the
Elements … and all such like acts not authorized or allowed by the Rubrics of the Book of
Common Prayer)". Struck **in its entirety** — all four examples — by the House of
Bishops on the motion of the **Bishop of North Carolina**, 29 Oct. (p. 333: "striking out
the words beginning with 'And as examples,' and ending with 'Book of Common Prayer.'
Which was adopted."). The Committee of Conference then restored examples (c) and (d) in
revised form as (a)–(c) and did not restore incense or the crucifix.

### 2d. Does the enacted canon authorise, permit or name incense?

**No.** The word "incense" occurs five times in the whole 2.2-million-character OCR
(extract J): four in draft/substitute texts and messages, one in Bishop Whipple's
missions report ("the incense of earnest prayer"). Zero in the enacted section, in the
Bishops' Message 78, or in the Digest. Nothing in it authorises or permits incense;
DeKoven said so from the floor (§3).

### 2e. RJ's sequence claim — "a proposed incense ban within it was removed after DeKoven's speech"

Chronologically true; causally unproven and, on the record, the House that heard the
speech did the opposite:

| Date | Body | Action | Source |
|---|---|---|---|
| 23 Oct | Deputies' Committee on Canons | Reports canon with incense as example (a) | p. 108, ext. A |
| 26 Oct | Deputies | Blanchard substitute (flat prohibition list, "1. The use of incense"); **DeKoven's amendment "Leave out all within the parentheses"; DeKoven's speech** | pp. 135-136, ext. B; pamphlet |
| 27 Oct | Deputies | Substitutes and amendments tabled; **canon adopted WITH incense as (a)**, clergy 38-2-1, laity 35-3-1; **DeKoven votes Nay** | pp. 142-145, ext. D |
| 29 Oct | Bishops | Strike all four examples (Bp. of North Carolina); test made disjunctive (Bp. of W. New York); passed | pp. 333-335, ext. F; Msg 63 |
| 30 Oct | Deputies | Non-concur; Committee of Conference (Lewin's motion to concur with the Bishops lost) | p. 178, ext. G |
| 31 Oct | Conference → Bishops (Msg 78) → Deputies | Conjunctive test restored; examples (a)-(c) as enacted; Deputies concur clergy 38-2-1, laity 28-1-2; **DeKoven votes Nay again** | pp. 183-188, ext. H |

`[Analysis]` The incense example was removed by the House of Bishops, which struck all
four examples at once and left no reason on the record; the Deputies, who heard the
speech, passed the incense example the next morning by 38 dioceses to 2. RJ's
"removed after DeKoven's speech" is accurate as sequence and unsupported as cause. The
Bishop of Maryland's failed substitute (p. 334) gives the only recorded Bishops'
rationale in the vicinity, and it is "deficiency of time" and "detail rather than
principle", not incense.

### ⭐ Verdict on §2: **VERIFIED** (enacted text, symbolic-conjunctive test, struck clause, no incense) — with RJ's causal framing **PARTIAL**.

**Argumentative stake, recorded not argued:** the enacted test presupposes that
ceremonies acquire significations that can be adjudicated by a Bishop and Standing
Committee; the Bishops tried to remove that presupposition and the Deputies put it back.

---

## §3. DeKoven's "nothing in this Canon authorizes" line

**Capture:** `src/SRC_PRIMARY_1874_DeKoven_Canon-On-Ritual-Speech_ProjectCanterbury.txt`
(the T. Whittaker pamphlet, via Project Canterbury; copy verified against the fetched
original by seven string counts — incense 24, Ritualist 9, symboliz- 37, Malachi 1,
Laughter 6, Eucharistic 18, Presbyter 15 — all matching).

- **Same speech or separate exchange?** **Separate.** The pamphlet prints the 26 Oct.
  speech (L104-1157, ending "I now offer the amendments"), then "THE CANON AS FINALLY
  PASSED" (L1161), then: `[Stated]` "The following remarks were made after the
  presentation of the Amended Canon, October 31st. A paragraph, in substance spoken at a
  later time, has been inserted" (L1211-1213). The "nothing in this Canon authorizes"
  line is at L1228-1234 of the 31 Oct. remarks.
- **Interval:** **five days** (26 → 31 Oct.). ⚠️ 260835-54 §3 wrote "six days later";
  re-derived here as five. Not corrected there (never-alter); recorded here as a dated
  note, 260835-57.
- **Occasion and source of record for each:** 26 Oct. — debate in the House of Deputies
  on the Committee on Canons' report, 17th day (Journal p. 135 records DeKoven's
  amendment offered that day; the Journal does not record speeches). 31 Oct. — after
  Message 78 and the conference report were before the Deputies, 22nd day (Journal
  pp. 183-188 record the concurrence vote, DeKoven Nay; again no speeches). **The pamphlet
  is the only source of record for both texts**, and it carries its own caveat that one
  paragraph of the 31 Oct. remarks was "in substance spoken at a later time" and
  inserted — the pamphlet does not say which paragraph. `[Stated-Analysis]` The
  gradation-of-postures paragraph ("It may, indeed, be said …", L1285-1313) reads as
  written prose and is the likeliest candidate; this is inference, not stated.

  > ⛔⛔ **FALSIFIED 260835-64. "The pamphlet is the only source of record for both texts" IS NO LONGER TRUE AND WAS NEVER TRUE — a contemporary verbatim stenographic report of both existed throughout.** *Debates of the House of Deputies … 1874*, reported for The Churchman, IA `debatesofhouseof00epis_0`, prints the 26 October speech at printed pp. 201-205 and the 31 October remarks at printed pp. 338-339. ⛔ **It is the source of record for both, and it differs from the pamphlet at the points that matter to this document** — above all, the 31 October remarks name **incense and the crucifix** where the pamphlet names only the crucifix. ⭐ **The `[Stated-Analysis]` identification of the gradation-of-postures paragraph as the inserted one is CONFIRMED by the stenographic report and may be relabelled `[Stated]` as to the fact of its absence from the floor record.** ⚠️ **Every verbatim quotation in this document that is sourced to the pamphlet must be re-verified against the Debates before outward deployment.** Prior text left standing per the never-alter rule.
  >
  > *Wording drafted at `260835-64` §4(c) (LOCUS 3) and applied here verbatim by `260835-65`; the applying pass composed none of it.* ⭐ **The stenographic capture is in the repo at `src/SRC_PRIMARY_1874_Debates-House-of-Deputies_DeKoven-Andrews-Beers-Ritual-Canon-Vote.txt` (added by `260835-64`; registered in `SRC_Manifest.md` by `260835-65`).**
- **Order:** speech first, floor line second, in the same legislative episode and the same
  chamber. Both attributable to DeKoven.
- `[Stated]` 31 Oct.: "there are two specifications left out, which said that the use of
  incense and the use of the crucifix symbolized false doctrine. … nothing in this Canon
  authorizes the use of incense or the use of the crucifix. It leaves that just where it
  was before. If it was lawful before, it is lawful now; if it was unlawful before, it is
  still unlawful."
- ⚠️ 260835-54's quotation matches the capture verbatim.

### ⭐ Verdict on §3: **VERIFIED** — both statements are DeKoven's, five days apart, speech (26 Oct.) before floor line (31 Oct.), same debate, under one citation trail; with the pamphlet's inserted-paragraph caveat recorded against the 31 Oct. text.

---

## §4. Of Ceremonies — exact wording

**Capture:** `src/SRC_PRIMARY_1662_BCP_Of-Ceremonies-Why-Some-Be-Abolished_pdf-pp6-8.txt`
— full text of "Of Ceremonies, why some be abolished, and some retained", extracted
by pdftotext from `src/the-book-of-common-prayer-1662.pdf` with each column cropped
separately (the file is landscape 792×612; gutter confirmed by `-bbox`). **Extraction
succeeded; page images were not needed.** Known defects left uncorrected and documented
in the capture header: the "ct" ligature is dropped ("praice", "rejeed", "addied",
"reſpe", "perfe"), long-s retained, drop-capitals scrambled. Location: PDF p. 6 right
column (begins) → p. 7 both columns → p. 8 left column (ends; "condemn no other
Nations" at p. 8, confirming 260835-53).

### 4a. Ceremonies indifferent in themselves, abolished for abuse or changed signification

- PDF p. 6 (capture L61-64): `[Stated]` "ſome at the firﬅ were of godly intent and
  purpoſe deviſed, and yet at length turned to vanity and ſuperﬅition: Some entered into
  the Church by undiſcreet devotion, and ſuch a zeal as was without knowledge; and for
  becauſe they were winked at in the beginning, they grew daily to more and more abuſes,
  which not only for their unprofitableneſs, but alſo becauſe they have much blinded the
  people, and obſcured the glory of God, are worthy to be cut away, and clean reje[ct]ed".
- PDF p. 7 (L77-79): `[Stated]` "the keeping or omitting of a Ceremony, in itſelf
  conſidered, is but a ſmall thing; yet the wilful and contemptuous tranſgreſſion and
  breaking of a common Order and Diſcipline is no ſmall offence before God".
- PDF p. 7 (L121-127): `[Stated]` "the moﬅ weighty cauſe of the aboliſhment of certain
  Ceremonies was, That they were ſo far abuſed, partly by the ſuperﬅitious blindneſs of
  the rude and unlearned, and partly by the unſatiable avarice of ſuch as ſought more
  their own lucre, than the glory of God, that the abuſes could not well be taken away,
  the thing remaining ﬅill."

### 4b. Abolition for abuse distinguished from condemnation as evil in itself

- The abolished ceremonies are "of godly intent and purpoſe deviſed" (p. 6) and "taken
  away which were moﬅ abuſed, and did burden men's conſciences without any cauſe"
  (p. 7, L144-146); the retained ones "are retained for a Diſcipline and Order, which
  (upon juﬅ Cauſes) may be altered and changed, and therefore are not to be eﬅeemed
  equal with God's Law" (L147-149).
- PDF p. 8 (L155-163): `[Stated]` "in theſe our doings we condemn no other Nations, nor
  preſcribe any thing but to our own people only: For we think it convenient that every
  Country ſhould uſe ſuch Ceremonies as they ſhall think beﬅ … and that they ſhould put
  away other things, which from time to time they perceive to be moﬅ abuſed, as in men's
  Ordinances it often chanceth diverſely in divers Countries."
- Also relevant (p. 7, L110-121): Christ's Gospel "is not a Ceremonial Law … being
  content only with thoſe Ceremonies which do ſerve to a decent Order and godly
  Diſcipline, and ſuch as be apt to ﬅir up the dull mind of man … by ſome notable and
  ſpecial ſignification, whereby he might be edified" — the formulary's own statement
  that retained ceremonies carry signification.

### ⭐ Verdict on §4: **VERIFIED** — the 1662 formulary supplies a category between "intrinsically evil" and "merely imprudent": a ceremony **in itself indifferent** ("in itſelf conſidered … but a ſmall thing"; "of godly intent … deviſed"), **abolished because so far abused that "the abuſes could not well be taken away, the thing remaining ﬅill"**, while expressly declining to condemn its use elsewhere ("we condemn no other Nations"). That is neither a judgment that the thing is evil in itself nor a merely prudential preference; it is a judgment about the thing's acquired abuse and signification in a given place and time.

`[Analysis]` The same document also says retained ceremonies are chosen for their
"ſpecial ſignification" — i.e. the formulary's own ceremonial theory is that ceremonies
signify, which is the presupposition §2's canon shares.

---

## §5. DeKoven on Malachi 1:11

**Capture:** DeKoven speech capture (§3), L369-397; Journal capture (§2).

### 5a. Exact wording and location

`[Stated]` (26 Oct. speech, L377-390, immediately following the Psalm 141 passage at
L365-374): "Then again, I heard it read in St. Thomas' Church yesterday morning at the
beginning of the services, 'From the rising of the sun even unto the going down of the
same, my name shall be great among the Gentiles, and in every place incense shall be
offered unto my name, and a pure offering; for my name shall be great among the heathen,
saith the Lord of Hosts.' I am not going to enter into the question whether that was a
prophecy of something that was literally to take place. Some people say it was, but I am
afraid they are Ritualists. My only question is as to its symbolical meaning. The prophet
Malachi holds that incense symbolizes the pure offering,—I suppose the Eucharistic
offering; and for the sake of this argument I am willing for the moment to concede that
that offering is nothing but an offering of prayer and thanksgiving; though I do not
think so."

Source of record: the T. Whittaker pamphlet (Project Canterbury transcription); the
Journal does not print speeches. RJ's excerpt cites Psalm 141; the Malachi passage is the
**next paragraph of the same speech**, not elsewhere in the debate.

> ⛔ **CORRECTED 260835-64: source of record is the stenographic *Debates of the House of Deputies … 1874*, not the pamphlet. The Journal indeed does not print speeches; the Debates volume does.** Prior text left standing.
>
> *Wording drafted at `260835-64` §4(c) (LOCUS 4) and applied here verbatim by `260835-65`.*

**Verdict on (a): VERIFIED.**

### 5b. Reports others using it, uses it himself, or both?

**Both, and differently — the two must not be collapsed:**

- **Reports others:** `[Stated]` "Some people say it was [a prophecy of something that was
  literally to take place], but I am afraid they are Ritualists." `[Stated-Analysis]` The
  "it" is a *literal* fulfilment reading of the incense clause; in context (a speech
  against declaring incense symbolic of false doctrine) this is others using Mal 1:11 for
  literal incense — but DeKoven does not say "in defense of incense" in so many words.
  RJ's "indicates that people are using that passage in defense of incense" is a fair
  paraphrase, one inferential step beyond the words.
- **Uses it himself:** yes, but for a **symbolic** argument only, expressly declining the
  literal reading ("I am not going to enter into the question … My only question is as to
  its symbolical meaning"), and reading the pure offering as "I suppose the Eucharistic
  offering". He does not deploy Mal 1:11 as a warrant for the practice; he deploys it to
  show incense cannot be said to symbolise false doctrine.

**Verdict on (b): VERIFIED — both; report and use are distinct and the use is not the use
reported.**

### 5c. Whom does he identify?

No one by name. `[Stated]` "Some people … I am afraid they are Ritualists." — a class,
with self-distancing irony from the House's self-described "only clerical Ritualist"
(L284-285).

**Verdict on (c): VERIFIED as to wording; UNMATCHED as to any individual.**

### 5d. Is Hopkins named anywhere in the debate?

Searched: the whole DeKoven pamphlet (0 hits on "Hopkins"); the whole 1874 Journal OCR
(the Journal's "DeKoven" hits were all enumerated; "Hopkins" was not separately swept
across the 2.2M-character OCR, and the Journal records no speeches in any case). Debate
reports in *The Churchman* / *The Church Journal* for Oct.–Nov. 1874 were **not**
searched (not reachable this pass).

**Verdict on (d): UNMATCHED — not named in the speech, the 31 Oct. remarks, or any
captured Journal extract; periodical reports unsearched.**

### 📌 Bearing on the 260835-55 verdict — dated note, 260835-57

260835-55 concluded that Hopkins's use of Mal 1:11 as a scriptural warrant for incense
was "an isolated instance rather than a current", and recorded as its strongest counter
that the search had been for engagement with Hopkins rather than for repetition. **This
item narrows that verdict.** DeKoven, on the floor of General Convention eight years
after Hopkins's book, testifies that "some people" hold the literal-fulfilment reading of
Mal 1:11 and identifies them as Ritualists. That is a second contemporary witness that
the reading was **in circulation** in American ritualist opinion, not confined to
Hopkins's page. It does **not** show a written current (no second author is named), and
DeKoven himself declines the reading. Corrected scope: **not "isolated" — held by an
unnamed group DeKoven expected the House to recognise; still no second author located.**
260835-55's verdict text is not edited (never-alter).

### ⭐ Verdict on §5: **(a) VERIFIED · (b) VERIFIED, both, distinct · (c) VERIFIED wording / UNMATCHED individual · (d) UNMATCHED.**

---

## §6. Captures created by this pass (all untracked at write-up; none registered)

| File | Source | Bears on |
|---|---|---|
| `src/SRC_PRIMARY_0155_Justin_Martyr_Malachi-1-11_Dialogue-28-41-116-117_1Apology-10-13_ANF1.txt` | New Advent, ANF 1 (Dods & Reith) | §1 |
| `src/SRC_PRIMARY_0180_Irenaeus_Against-Heresies_IV-17-5-6_Malachi-Incense-Prayers_ANF1.txt` | New Advent, ANF 1 (Roberts & Rambaut) | §1e — **not in the brief**; pulled because the second question (later use of the Malachi-incense reading) led straight to the one Father who glosses the incense clause, and the Protestant commentators in the Survey cite him for it |
| `src/SRC_PRIMARY_1874_DeKoven_Canon-On-Ritual-Speech_ProjectCanterbury.txt` | Project Canterbury | §3, §5 |
| `src/SRC_PRIMARY_1874_GeneralConvention_Journal_Canon-20-Title-I_Ritual-Canon-Sequence.txt` | archive.org `journalofproceed1874phil` | §2, §3, §5 |
| `src/SRC_PRIMARY_1662_BCP_Of-Ceremonies-Why-Some-Be-Abolished_pdf-pp6-8.txt` | repo PDF, pdftotext | §4 |

---

## §7. Registration debt — flagged, not repaired

⛔ **Neither pass 260835-56's nineteen captures (committed at `2ed1c2a`) nor pass
260835-57's five captures are registered in `SRC_Manifest.md` or in `PROJECT_STATE.md`
§4.** The validator therefore does not see them: C0 examines 34 files and C6 hashes 5,
figures unchanged across both passes. Both stamps are named here so the debt is
traceable: **260835-56 and 260835-57.** Not repaired in this pass (out of scope; JD
decides per `ORCHESTRATION.md` §7).

---

## Changelog

- **260835-65 (2026-09-07):** ⛔⛔ **TWO DATED NOTES, BOTH WITHDRAWING THIS DOCUMENT'S SOURCE-OF-RECORD DESIGNATION FOR DE KOVEN'S TEXTS; NO ORIGINAL SENTENCE ALTERED AND NO VERDICT CHANGED.** **§3** — the sentence *"The pamphlet is the only source of record for both texts"* is **FALSIFIED**: a contemporary verbatim stenographic report of both existed throughout (*Debates of the House of Deputies … 1874*, IA `debatesofhouseof00epis_0`), and it names **incense and the crucifix** in the 31 October remarks where the pamphlet names only the crucifix. **§5** — the *"Source of record: the T. Whittaker pamphlet"* line is likewise corrected. ⭐ **BOTH NOTES USE `260835-64`'s OWN DRAFTED WORDING VERBATIM (its §4(c), LOCUS 3 and LOCUS 4); this pass composed none of the correction text and only recorded that it applied it.** ⭐⭐ **ONE GAIN FOR THIS DOCUMENT: its `[Stated-Analysis]` identification of the gradation-of-postures paragraph as the pamphlet's admitted insertion is CONFIRMED by the stenographic report and may be relabelled `[Stated]` as to the fact of that paragraph's absence from the floor record — the note says so and the relabelling itself is NOT performed here.** ⚠️⚠️ **OWED, AND NOT DISCHARGED HERE: every verbatim De Koven quotation in this file is pamphlet-sourced and needs re-verification against the Debates before outward deployment.** ⛔ **`passes/260835-57_incense-reply-source-checks_close-out.md` line 51 carries the same falsified claim and was DELIBERATELY NOT TOUCHED — it is a pass close-out and therefore historical record, per `260835-64`'s own instruction and the never-alter rule.** ⭐ **This file was also REGISTERED in `PROJECT_STATE.md` §4 this pass, on JD's ruling, in the same class and treatment as the `260835-44`…`260835-53` external-research series.** ⛔ **Nothing minted, no analytical conclusion added, revised or extended, nothing drafted or posted.**

- **260835-57** — created. Five checks, five captures, verdicts: §1 PARTIAL; §2 VERIFIED
  (RJ's causal framing PARTIAL); §3 VERIFIED; §4 VERIFIED; §5 (a)(b) VERIFIED, (c)
  wording VERIFIED / individual UNMATCHED, (d) UNMATCHED. Dated notes: 260835-54's "six
  days" re-derived as five; 260835-55's "isolated instance" narrowed by DeKoven's
  testimony. No existing file modified.
