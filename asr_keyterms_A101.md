# ASR Key-Terms List — Anglican 101 (`A101`)

**Last updated: 260830-2** (created 260816-1; date-stamped, format yymmdd-iteration)

**Purpose.** A tuned key-terms list for the AssemblyAI `universal-3-5-pro`
transcription of Anglican 101 sessions. It is passed to the ASR as a
prompt-time term list so that the vocabulary this class actually uses is
recognised rather than approximated.

⛔ **THIS IS REUSABLE TOOLING, NOT VOLATILE STATE.** It is registered in
`PROJECT_STATE.md` §4 and lives in the repo for the same reason
`validate_project.py` does: it is re-run on every future session, and a
term list that lives in a chat thread has to be rebuilt from memory by
whoever transcribes next. **Rebuilding it from memory is how a term drops
out silently.**

---

## ⛔⛔ WHAT THIS FILE IS NOT

⛔ **It is NOT a correction map, and it must never be applied as one.**
Feeding these terms to the recogniser changes what the recogniser *hears*
on the next run. It does **not** license rewriting a mangled form in an
already-captured transcript. **Every mangled form observed in a capture is
logged in that capture's quirk register in `SRC_Manifest.md` and left
standing in the transcript**, per the never-alter rule.

⚠️ **The distinction is load-bearing.** A silent correction destroys the
evidence that the capture was unreliable at that point — which is exactly
the evidence a later verification pass needs.

---

## ⭐⭐⭐ HOW TO USE THIS — THE PROMPT, READY TO PASTE

**AssemblyAI:** paste the block below into the `word_boost` / **Custom
Vocabulary** field (or `word_boost` array if using the API). Set boost
level to **high**. ⚠️ **This is a vocabulary hint list, not an
instruction — AssemblyAI does not take prose direction, so do not paste
the surrounding explanation, only the terms.**

**Local Whisper (or any engine taking an `initial_prompt`):** paste the
prose form below instead. Whisper's `initial_prompt` biases toward the
style and vocabulary of whatever text it's given, so a natural sentence
works better there than a bare list.

### Prose form, for Whisper's `initial_prompt`

```
A lecture on Anglican theology and liturgy, discussing the Book of
Common Prayer, the Thirty-nine Articles, and the Elizabethan Settlement.
Topics include the Eucharist, Ante-Communion, the Deacon's Mass,
transubstantiation, memorialism, and the regulative principle of
worship. The speaker references the Council of Trent, the Council of
Hieria, the Second Council of Nicaea, Quartodeciman practice, and the
Gesima seasons — Septuagesima, Sexagesima, Quinquagesima — as well as
Pascha and Trinitytide. Liturgical objects are named: the aumbry, the
pyx, the monstrance, the tabernacle, and the ablutions. Theological
vocabulary includes adiaphora, koinonia, latria, dulia, hyperdulia,
propitiatory, lapsarian, sola scriptura, and good and necessary
consequence. Authors and figures include Cranmer, Bramhall, Zwingli,
and the Summa Theologiae. Scripture and canon discussion covers the
Apocrypha, the deuterocanonical books, Tobit, the Wisdom of Solomon,
Maccabees, and the Didache.
```

⚠️ **Whisper's `initial_prompt` is capped at 224 tokens** — the block
above is sized to fit. ⛔ **Do not append the full list to it; it will
be silently truncated and the terms at the end will be lost.**

### ⛔ Standing reminder

**Use this on every AssemblyAI or Whisper run for this corpus.** It was
not used on the `P1`, `P2`, or `P3` batches — a known gap, cheap to
mitigate after the fact by cross-checking against YouTube's own captions
rather than re-transcribing.

---

## The list

```
Book of Common Prayer
Ante-Communion
Council of Trent
Tridentine
Summa Theologiae
paedocommunion
purgatory
Quartodeciman
Septuagesima
Sexagesima
Quinquagesima
Pascha
Gesima
Trinitytide
ablution
Council of Hieria
Second Council of Nicaea
second commandment
Church Triumphant
Church Militant
Theotokos
cloud of witnesses
Eucharist
Ante-Communion
Deacon's Mass
aumbry
pyx
monstrance
ablutions
tabernacle
transubstantiation
memorialism
local presence
koinonia
adiaphora
regulative principle
good and necessary consequence
Zwingli
Maccabees
Tobit
Wisdom of Solomon
Didache
latria
dulia
hyperdulia
Apocrypha
deuterocanonical
sola scriptura
Thirty-nine Articles
Article XVII
Article XX
Article XXII
regulative principle
Sursum Corda
Magisterium
Anglo-Catholic
Elizabethan Settlement
Black Rubric
Bramhall
Cranmer
genuflect
propitiatory
lapsarian
```

---

## Provenance — how each term was chosen

Terms were derived from **mangled forms observed in the local whisperfile
rendering (`SRC_WHISPER_20260809.txt`, Rendering A)** of the 2026-08-09
session, then checked against the AssemblyAI rendering (Rendering B) to
establish whether the term was already recognised.

⭐ **Every mangling below was verified by grep against the actual file
before being entered here.** None is carried from report.

| True form | Whisper form (Rendering A) | Rendering A | Rendering B | Note |
|---|---|---|---|---|
| Book of Common Prayer | *"Book of Congress"* | 2 | 0 | B correct |
| Council of Trent | *"the Council of Tribes"* | 1 | 0 | B correct |
| Tridentine | *"Tribantine"* | 1 | 0 | B correct |
| Summa Theologiae | *"the Southa Theology"* | 1 | 0 | B correct |
| paedocommunion | *"Cato community"* | 1 | 0 | B correct |
| Ante-Communion | *"an Anticonunion"* | 1 | 0 | B correct |
| purgatory | *"Hercules"* | 1 | 0 | B correct |
| Quartodeciman | *"Quartodestimate"* | 1 | 0 | B correct |
| Septuagesima | *"Septagesima"* | 1 | 0 | B correct |
| Pascha | *"Pasco"* | 1 | 0 | B correct |
| **Council of Hieria** | *"Hyria"* | 2 | **0 — DROPPED** | ⛔ **see the correction below** |

---

## ⛔⛔ ONE CORRECTION TO THE INTAKE BRIEF'S QUIRK TABLE — `Hyria` IS **NOT** HYPERDULIA

⚠️ **The `260816-1` intake brief listed the mangling as `hyperdulia →
"Hyria"`. That attribution is WRONG, and it was caught before the term
list was built rather than after.**

**What the surrounding context actually establishes.** Rendering A carries
the name twice as *"Hyria"*, followed within two sentences by the bare date
*"754"* and by *"goes against the second Nicene Council."*

**A council, dated 754, prior to the Seventh Council, and standing against
Second Nicaea, is the Council of HIERIA** — the iconoclast synod of 754,
which Second Nicaea (787) overturned. ⛔ **It is not the Latin devotional
grade *hyperdulia*, which is a different word for a different thing and is
not what is being discussed at that point.**

⛔⛔ **WHY THIS MATTERED ENOUGH TO CHECK.** Had the brief's attribution been
carried into this file unverified, the term list would have taught the
recogniser to render a **historical council** as a **devotional category**.
That is worse than the original mangling: *"Hyria"* is visibly broken and
invites a check, whereas *"hyperdulia"* is a real word that would read as
correct and would never be questioned. ⭐ **A plausible wrong term is more
dangerous than an implausible one.**

⚠️ **AND RENDERING B IS WORSE HERE THAN RENDERING A, WHICH IS THE REVERSE OF
THE USUAL DIRECTION.** Rendering B **drops the council name entirely** —
only the bare date *"754"* survives, with the name absent in any form.
⛔ **A pass grepping Rendering B alone for this council would report it
absent when it is spoken.** This is the `Lateran` → *"lad ladan"* shape
(`260813-1`) arriving from the opposite side: not a mangling to chase, but
a **deletion** with nothing left to grep.

⭐ **Both `Council of Hieria` and `Second Council of Nicaea` are therefore
in the list above**, and `hyperdulia` is in it **on its own merits** (see
the absence note below), not as a rendering of *"Hyria"*.

---

## ⚠️⚠️ CORRECTION 260818-3 — RENDERING B DOES **NOT** DROP THE NAME. IT RENDERS IT *"Hyrea"*

⛔ **Dated note beside the original. The two sections above stand exactly as
`260816-1` wrote them, per the never-alter rule — including the table row that
reads `0 — DROPPED`. They were an honest report of a grep that was actually
run; the defect is in what the grep was pointed at, not in the reporting.**

⛔⛔ **THE FACT.** Rendering B (`SRC_AAI_20260809_sentences.json`) carries the
council's name **TWICE**, as ***"Hyrea"***, at **sentences 1851 and 1852**
(t = 8061.9 s and 8062.4 s, **2:14:22**). Grep-verified this pass in three
Rendering-B artifacts independently — the sentences JSON, the `.srt`, and the
word-level timestamps file. **Rendering A carries it twice as *"Hyria."***
`Hieria` returns **0 in both**.

⭐ **So the true state is: BOTH renderings mangle the name to a near-homophone,
NEITHER drops it, and NEITHER gets it right.** The claim above that
*"Rendering B is worse here than Rendering A"* is therefore also withdrawn:
they are equally wrong, in the same way, by one letter.

⚠️⚠️ **WHY THE ORIGINAL GREP MISSED IT — AND THIS IS THE PART THAT GENERALISES.**
The `260816-1` pass searched Rendering B for **`Hyria`** (Rendering A's mangled
form) and for **`Hieria`** (the true form). It did **not** search for
**Rendering B's own mangled form**, because that form was not yet known.

⛔⛔ **THAT IS PRECISELY THE `Lateran` → *"lad ladan"* LESSON (`260813-1`) THAT
THE SAME PASS CITED BY NAME — APPLIED TO ONE RENDERING AND NOT THE OTHER.**
An absence chased through "both renderings and the known mangled forms" is only
as good as the list of known forms, and **each rendering generates its own.**

⭐ **THE RULE ADOPTED FROM IT, WHICH IS THE REASON THIS NOTE IS HERE AND NOT
ONLY IN A PASS NOTE:** when two renderings mangle a term **differently**, an
absence in either is **not reportable** until the term has been located in the
rendering that HAS it, and the other rendering's local form has been read off
**the corresponding timestamp window**. ⛔ **Never grep the second rendering for
the first one's mistake.**

⚠️ **A SECOND INSTANCE OF THE SAME SHAPE, FOUND IN THE SAME SEGMENT AND FROM
THE OPPOSITE SIDE:** Rendering B writes ***"2nd Commandment"*** (×10) where
Rendering A writes ***"second commandment"*** (×11). ⛔ **A grep for
`2nd commandment` against Rendering A returns ZERO for a term spoken eleven
times.** It is not a mangling at all — it is a *transcription convention* — and
it will bite a term scan just as hard.

✅ **WHAT STANDS UNDISTURBED.** The identification of the council itself (754,
prior to the Seventh, standing against Second Nicaea = **Hieria**) is confirmed
by this pass from the same surrounding context; the `hyperdulia` misattribution
in the `260816-1` intake brief was correctly caught; and **both terms stay in
the list above on their existing grounds.**

⭐ **ONE TERM ADDED TO THE LIST THIS PASS** on the strength of the convention
trap: `second commandment`, so the recogniser produces one stable form.

---

## ⚠️ SEGMENT-2 MANGLINGS OBSERVED (added 260818-3, sentences 887-1977)

⛔ **Logged so the next capture gets them; ⛔ NOT a licence to rewrite anything
already captured.** All grep-verified.

| True form | Rendering A | Rendering B | Note |
|---|---|---|---|
| **Council of Hieria** | *"Hyria"* ×2 | ***"Hyrea"* ×2** | ⛔⛔ **corrects the table above** |
| purgatory | *"Hercules"* ×1 | correct | ⭐ located: **s887**, the first sentence of segment 2 |
| venial | *"menial"* | correct | |
| saints | *"students"* ×1 | correct | |
| Anglican | *"ancient"* ×1 | correct | ⛔ **material** — changes the question asked |
| Hebrews 12:1 | *"perhaps 12-1"* | correct | |
| cloud of witnesses | *"a lot of witnesses"* | correct | |
| Church Triumphant | *"church triumvirate"* | correct | |
| Church Militant | *"church middle-ist"* | correct | |
| directly | *"joyously"* ×1 | correct | ⛔ **material** |
| toll booth | *"told me"* ×1 | correct | ⛔ **material** |
| Trent Horn | *"Trent Warren"* | correct | ⚠️ a person, **not** the Council of Trent |
| patron saint | *"patriot-zine"* | correct | |
| *Letters to Malcolm, Chiefly on Prayer* | *"Malcolm Sheeley"* | correct | subtitle mangled into a surname |
| **BCP Preface** (Sursum Corda → Sanctus) | ✅ **correct** | ⛔ **garbled** | ⭐ **A is the better witness here** |
| ⭐⭐⭐ **James 5:16 — *"a righteous **man** availeth much"*** *(added 260821-1)* | ✅ correct at **s1041**; *"righteous **man**"* at s1043 | ✅ correct at **s1041**; ⛔⛔ ***"righteous **DEAD**"* at s1043** | ⛔⛔⛔ **SEE THE DEFECT-CLASS NOTE BELOW — THE SHARPEST INSTANCE IN THIS FILE** |

### ⛔⛔⛔ A SIXTH DEFECT SHAPE, ADDED 260821-1 — A MANGLING THAT INSERTS AN ENTIRE DOCTRINE

⛔⛔ **THIS IS THE `Eucharist` → *"the universe"* FAMILY — A WRONG READING IN ORDINARY, GRAMMATICAL, PLAUSIBLE ENGLISH THAT NOTHING ANNOUNCES — AND IT IS THE MOST DANGEROUS INSTANCE THE PROJECT HAS MET.**

✅ **JD's direct audio verification, 260821-1:** ***"the prayers of a righteous man availeth much, right?"*** ⭐⭐ **THAT IS JAMES 5:16 (KJV)** — the KJV reads *"The effectual fervent prayer of a righteous man availeth much"*, and ***"availeth"* is the KJV's own marker, carried by no modern version.** ⛔ **It is a SCRIPTURE CITATION, attributed to Scripture per `PROJECT_STATE.md` §5 rule 9.4's public-domain-text exemption, and NOT counted as his own prose.**

⛔⛔ **WHY THIS IS WORSE THAN *"the universe"* OR *"abortion"*, AND THE COMPARISON IS THE POINT:**

| Instance | Why it is catchable | Why this one is not |
|---|---|---|
| `Eucharist` → *"the universe"* | **Plainly wrong** to any reader who knows the subject | — |
| `worship` → *"abortion"* | **Visibly off-topic** — the subject changes | — |
| ⛔⛔ **`righteous man` → *"righteous DEAD"*** | — | ⛔⛔ **DOCTRINALLY COHERENT AND CONTEXTUALLY APT.** The surrounding stretch really is about the sanctified in heaven, so the wrong reading *fits* — and it **inserts an entire doctrine (the intercession of the dead) into what is actually a proof text** |

⚠️⚠️ **THE GENERAL RULE ADOPTED, SO A FUTURE PASS INHERITS IT RATHER THAN REDISCOVERING IT: a plausible wrong reading that inserts real theological content is more dangerous than an implausible one, and the danger scales with HOW WELL the wrong reading fits its context. A mangle that reads like something he might plausibly have said is the one that gets deployed.** ⛔ **A term list cannot fix this shape — both words are real English and both are in-domain. Only the ear can.**

⛔⛔ **AND A DISCREPANCY IS RECORDED RATHER THAN SMOOTHED: ear-queue item 10 named s1043; JD's returned verbatim is word-for-word s1041, a different sentence about six seconds earlier. *"Availeth much"* occurs at s1041 in BOTH renderings and at s1043 in NEITHER. ⛔ Both readings of what that means are live, neither is chosen, and s1043 remains unquoted in either form.** **Full handling at `St_Francis_EMC_Distinctives.md` `IP-47a`.**

⚠️ **TERMS ADDED TO THE LIST ABOVE FROM THIS SEGMENT:** `Church Triumphant` ·
`Church Militant` · `Theotokos` · `cloud of witnesses` · `second commandment`.
⛔ **`Trent Horn` is deliberately NOT added** — a proper name of a living third
party is not a theological term, and adding it would bias the recogniser toward
a person over the Council on a session where both are discussed.


---

## ⚠️⚠️ SEGMENT-3 MANGLINGS (added 260819-1, sentences 1978-2563) — ⛔⛔ AND THE WORST ONE IN THE FILE

⛔ **Logged so the next capture gets them; ⛔ NOT a licence to rewrite anything already captured.** All grep-verified.

### ⛔⛔ THE HEADLINE — `Eucharist` BECOMES *"the universe"*, AND IT IS WORSE THAN `Hyrea`

**`Eucharist` returns 18 in Rendering B and 12 in Rendering A. FIVE of the six missing occurrences are rendered *"the universe."***

| Rendering B | Rendering A |
|---|---|
| *"Christ is present in the Eucharist"* (s2007) | *"Christ is present in **the universe**"* |
| *"the presence of Christ in the Eucharist"* (s2345) | *"the presence of christ in **the universe**"* |
| *"denies the local presence"* (s2372) | *"denies the local presence of Christ in **the universe**"* |
| *"that's not the purpose of the Eucharist"* (s2420) | *"that's not the purpose of **the universe**"* |
| *"the purpose of the Eucharist is to eat"* (s2421) | *"the purpose of **the universe** is to eat"* |

⛔⛔ **WHY THIS IS THE MOST DANGEROUS ENTRY IN THIS FILE.** *"Hyrea"* and *"Hyria"* are **visibly broken** — a reader meets them and knows something is wrong. ***"The universe"* is ordinary, grammatical English.** A pass grepping Rendering A for `Eucharist` gets **12**, has no reason to suspect a shortfall, and loses two load-bearing sentences. ⭐ **A plausible wrong word is more dangerous than an implausible one — the `hyperdulia` principle, arriving in the ORDINARY-VOCABULARY direction rather than the technical-term one.**

### The rest of the segment-3 register

| True form | Rendering A | Rendering B | Note |
|---|---|---|---|
| **Eucharist** | ⛔⛔ ***"the universe"* ×5** | correct ×18 | ⛔⛔ **see above** |
| **Ante-Communion** | ⛔ ***"an Anticonunion"*** | ✅ correct | ⛔⛔ **A grep of A for `Ante-Communion` returns ZERO for a term that is there** ✅⭐ **EAR-CONFIRMED 260821-1 — JD's direct audio verification: spoken CLEARLY as *"Ante-Communion"*, in the fuller clause *"a service called an Ante-Communion or a Deacon's Mass"* (`IP-54a`). ⛔ THIS ROW IS NOT REMOVED AND MUST NOT BE — the mangling is real and is exactly why the term did not grep. ⭐ What changed is the STATUS of the true form: ear-confirmed AGAINST the mangling, the strongest state a quirk row can reach** |
| **adiaphora** | ⛔ ***"a diaport"*** | ✅ correct | ⛔ reads as two ordinary words |
| **Maccabees** | ⛔ ***"The Bacchus"*** | ✅ correct | ⛔ **a plausible proper noun; nothing announces the error** |
| **Tobit** | ⛔ ***"tokens"*** | ✅ correct | ⛔ ordinary English |
| **Zwingli** | ⛔⛔ **DROPPED** — *"Do you agree with this being me?"* | ⛔ ***"Swingley"*** | ⛔⛔ **`Zwingli` is 0·0 while the name is spoken. NEITHER rendering carries it** |
| **Anglican** | ⛔ ***"the interposition"* ×2** | ✅ correct | ⚠️ **a REPEAT offender in A with a DIFFERENT form each time** — segment 2 recorded *"ancient"* |
| **aumbry** | *"an omri"*; later ***"an omelette"*** | *"an omri"*; later *"an ombrage"* | ⚠️⚠️ **BOTH mangle; at the first occurrence IDENTICALLY** |
| **pyx** | *"a pix"*; later ***"a pig"*** | *"a pix"*; later ✅ *"a pyx"* | ⚠️⚠️ **same** |
| **divinity** | ⛔ *"body, blood, soul, and **body**"* | ✅ *"…and divinity"* | ⛔ material |
| **regulative principle** | ⛔ *"the **regular** principle"* ×1 | ✅ correct | ⛔ **material — `DQ-9`-adjacent** |
| **sacrament** | ⛔ *"the sacrum"* | ✅ correct | |
| **Scripture** | ⛔ *"description"* ×1 | ✅ correct | ⛔ material |
| **Roman Mass** | ⛔ *"the Roman **baths**"* | ✅ correct | ⛔ material |
| **Article XXVIII clause** | ⛔ *"ordain your exact course… in a door or a hotel"* | ✅ *"…the sacrament of the Eucharist to be carried about"* | ⛔ **A garbles badly; B is the better witness** |
| ***"a mere memorial"* clause** (s2396) | ⭐ **CARRIES IT** | ⛔ **LOSES IT** | ⭐⭐ **A is the better witness here — the third such instance in two segments** |

### ⚠️⚠️ AND THE PROTOCOL GETS A BOUND — TWO RENDERINGS CAN AGREE AND BOTH BE WRONG

At sentences **2014-2015 both renderings independently produce *"an omri"* and *"a pix"*** for what are almost certainly **aumbry** and **pyx**. ⛔⛔ **The dual-ASR protocol says agreement gives provisional confidence against transcription error. HERE THE TWO AGREE AND ARE BOTH WRONG.** ⭐ **Agreement between two engines is evidence they made the SAME INFERENCE from the same audio, not evidence the inference was right — and on a low-frequency technical term, the same inference is exactly what one should expect.** ⛔ **This bounds the protocol; it does not overturn it.**

---

## ⛔⛔ A FOURTH DEFECT SHAPE, ADDED 260819-1 — AND IT IS NOT A MANGLING AT ALL

⚠️⚠️ **Recorded because it produced FOUR false absences inside the `260819-1` pass itself, and was caught only by re-running every check against the joined text.**

⛔⛔ **`SRC_WHISPER_20260809.txt` (Rendering A) IS HARD-WRAPPED at short line lengths.** **A line-oriented grep — which is what every `grep` invocation in this project is by default — returns ZERO for any phrase that straddles a line break, no matter how plainly the phrase is present.**

**Demonstrated:** *"the tabernacle is the word that was used"*, *"worship Christ is through the eating"*, *"what's not allowed is transubstantiation"* and *"use the Apocrypha to teach morals and history"* **all returned NOT FOUND on a line-oriented search and are ALL present**, split across two or three lines each.

⭐⭐ **THE GENERAL RULE, AND IT IS NOW A FAMILY OF THREE.** An absence in a rendering is **not reportable** until it has been chased through:

1. ⭐ **that rendering's own MANGLED FORMS** — the `Hyrea` lesson (`260818-3`);
2. ⭐ **that rendering's own TRANSCRIPTION CONVENTIONS** — the *"2nd Commandment"* / *"second commandment"* trap (`260818-3`);
3. ⭐⭐ **that rendering's own LINE STRUCTURE** — this entry (`260819-1`).

⛔⛔ **ALL THREE ARE PROPERTIES OF THE FILE, NOT OF THE SESSION, AND ALL THREE CONVERT A PRESENT TERM INTO A REPORTED ABSENCE.** ⛔ **A key-terms list fixes only the first. The second and third are search discipline and no term list can help with them, which is why they are recorded here rather than added to the list above.**

---

## ⚠️⚠️ SEGMENT-4 MANGLINGS (added 260820-1, sentences 2564-3855) — ⛔⛔ AND A DEFECT CLASS A TERM LIST CANNOT FIX

⭐⭐ **THE HEADLINE IS NOT A MANGLING AND IT IS THE ONE A FUTURE TERM SCAN
MOST NEEDS: EQUAL COUNTS ARE NOT AGREEMENT.** `regulative` returns **five in
Rendering B and five in Rendering A** across this segment, and **two of the
ten sites are not shared** — Rendering A **loses** s2609 (*"where it crosses
regulative"* → *"where it crosses right with it"*) and **carries** s2687
(*"Your definition, regulative, has to be in the Bible itself"*), which
Rendering B renders *"Your question actually has to be in the Bible itself."*
⛔⛔ **A pass that ran the count and stopped would have reported perfect
dual-ASR agreement on the segment's most `DQ-9`-relevant term.** ⭐ **Rule:
agreement is a property of SITES, not of totals, and has to be checked site
by site whenever a count is load-bearing. A key-terms list does not help
with this at all.**

| True form | Rendering A | Rendering B | Note |
|---|---|---|---|
| **Sexagesima** | ⛔⛔ *"the sex of the Gethsemane"* | ✅ | ⛔ A plausible-sounding religious phrase in place of a calendar term |
| **Quinquagesima** | *"Quintagesima"* | ✅ | |
| **Septuagesima** | *"Septagesima"* | ✅ | ✅ confirms the existing register row against its actual occurrence |
| **Quartodeciman** | *"Quartodestimate"* | ✅ | ✅ confirms the existing register row |
| **Pascha** | *"Pasco"* | ✅ | ✅ confirms the existing register row |
| **Advent** | ⛔⛔ **DROPPED** (s3204) | ✅ | ⛔ text loss, not a mangle |
| **worship** (s3700) | ⛔⛔ *"abortion"* | ✅ | ⛔⛔ ordinary English, wholly different subject, nothing flags it |
| **elements** (s2889) | ⛔ *"elbows"* | ✅ | |
| **refraining** (s2577) | *"a regrading for meat"* | ✅ | |
| **s3765** | ⛔⛔ *"all forms of vaccine are valid"* | ⛔ *"all 40s are bad"* | ⛔⛔ **BOTH garbled; A's is fluent English about a different subject** |
| **s3233 — the evaluative word** | *"true"* | *"good"* | ⛔⛔ **NOT A MANGLE — A GENUINE DIVERGENCE at the word carrying a finding's whole force. Quoted in neither form** |
| **s3656** | *"from the perspective of the **pulpit**"* | *"…of the **world**"* | ⛔ material; not quoted |
| **s3648** | *"answer the comment of that"* | *"answer to God for that"* | ⛔ A garbles |
| **s3692 — a public figure's name** | ⛔⛔ **rendered as THE INITIALS OF A PERSON IN THE ROOM** | names the figure | ⛔⛔⛔ **SEE BELOW** |

### ⛔⛔⛔ A FIFTH DEFECT SHAPE, ADDED 260820-1 — A MANGLING THAT MANUFACTURES AN ATTRIBUTION

⚠️⚠️ **Every shape recorded in this file so far corrupts a WORD. This one
corrupts an ATTRIBUTION.** At **s3692** Rendering B names a public figure and
**Rendering A renders that name as the initials of a person present in the
room.** ⛔⛔ **In a corpus whose central discipline is not attributing
anything to the wrong person, an ASR error that invents an apparent reference
to an attendee is a distinct and more dangerous class than any mangled
technical term.**

⛔ **The rule adopted from it: a proper name appearing in one rendering and
not the other is never, on its own, evidence that the person was referred
to — and least of all when the name resolves to someone present in the
room.** ⚠️ **A key-terms list CANNOT fix this: the correct output here is a
public figure's name, which no list of Anglican vocabulary would ever
contain, and the wrong output is a short, high-frequency token the
recogniser will always find plausible.** ⭐ **It is recorded here anyway,
because this file is where a future transcriber looks, and the mitigation is
procedural rather than lexical: read the corresponding window in the other
rendering before treating any name as spoken.**

---

## ⚠️ TERMS ENTERED ON EXPECTED-COVERAGE GROUNDS, NOT ON AN OBSERVED MANGLING

⛔ **Recorded separately so a later pass does not read the whole list as
evidence that every term in it was spoken.**

`latria` · `dulia` · `hyperdulia` · `deuterocanonical` · `Sexagesima` ·
`Quinquagesima` · `Article XXII`

**`latria` and `dulia` grep to ZERO in BOTH renderings of the 2026-08-09
session**, and `hyperdulia` to zero in both once the *"Hyria"*
misattribution is removed. ⛔ **That absence is recorded as an absence and
nothing is built on it** — it does not establish that the distinction was
not taught in other words, and it does not establish that it was. They are
listed here **so that a future session which does use them is captured
correctly**, which is the whole point of a prospective term list.

---

## Changelog

- **260821-1 (2026-08-11):** ⭐⭐⭐ **EXTENDED at the `A101-2026-08-09` EAR-VERIFICATION ROUND 1 — and this is the first entry in this file written from the AUDIO rather than from a rendering comparison.** ⛔ **A SIXTH DEFECT SHAPE RECORDED: a mangling that INSERTS AN ENTIRE DOCTRINE.** *"The prayers of a righteous **man** availeth much"* (s1041) is **JAMES 5:16 (KJV)** — a proof text — and Rendering B's *"the prayers of the righteous **DEAD**"* at s1043 does not get one word wrong, **it inserts the intercession of the dead into a Scripture citation.** ⛔⛔ **Same family as `Eucharist` → *"the universe"* and `worship` → *"abortion"*, but WORSE than either, because the wrong reading is DOCTRINALLY COHERENT AND CONTEXTUALLY APT rather than plainly wrong or visibly off-topic.** ⚠️ **General rule adopted: the danger of a plausible-English mangle scales with how WELL the wrong reading fits — and ⛔ a term list cannot fix this shape, since both words are real English and both are in-domain. Only the ear can.** ⛔ **A discrepancy is recorded rather than smoothed: queue item 10 named s1043, JD's verbatim is s1041, and *"availeth much"* is at s1041 in BOTH renderings and s1043 in NEITHER; both readings live, neither chosen, s1043 unquoted.** ✅ **And one existing row is UPGRADED rather than removed: `Ante-Communion` is ear-confirmed as spoken clearly against Rendering A's *"an Anticonunion"* — ⛔ the mangled-form row is KEPT, because it remains the reason the term did not grep.** **Full handling at `St_Francis_EMC_Distinctives.md` `IP-47a` and `IP-54a`.**

- **260820-1 (2026-08-11):** ⚠️⚠️ **EXTENDED at the `A101-2026-08-09` SEGMENT-4 intake (sentences 2564-3855), the session's last.** ⭐⭐ **THE HEADLINE IS NOT A MANGLING: `regulative` returns FIVE in both renderings AND TWO OF THE TEN SITES ARE NOT SHARED — Rendering A loses s2609 and carries s2687, which Rendering B loses. EQUAL COUNTS ARE NOT AGREEMENT; agreement is a property of SITES.** ⛔⛔ **AND A FIFTH DEFECT SHAPE IS ADDED, THE FIRST THAT A TERM LIST CANNOT MITIGATE: at s3692 Rendering A renders a PUBLIC FIGURE'S NAME AS THE INITIALS OF A PERSON IN THE ROOM — a mangling that manufactures an ATTRIBUTION rather than corrupting a word.** ⚠️ **Fourteen segment-4 manglings tabled**, including ⛔⛔ `Sexagesima` → *"the sex of the Gethsemane"*, `worship` → *"abortion"* (s3700), `elements` → *"elbows"*, `Advent` DROPPED, and ⛔⛔ **a genuine load-bearing divergence at s3233 — *"good"* (B) vs *"true"* (A) — quoted in neither form.** ✅ **Three long-standing register rows (`Quartodeciman`, `Septuagesima`, `Pascha`) are CONFIRMED against their actual occurrences for the first time; they had been carried from the `260816-1` brief unverified.** ⛔ **Nothing already captured is rewritten and no prior wording is altered.** ⭐ **Six terms added to the list** (`Gesima`, `Sexagesima` promoted from expected-coverage to observed, `Didache` confirmed, `Quinquagesima` promoted, `Trinitytide`, `ablution`). ⭐⭐⭐ **This closes the `A101-2026-08-09` ingest: all four segments have now contributed to this file.**
- **260819-1 (2026-08-19):** ⚠️⚠️ **EXTENDED at the `A101-2026-08-09` SEGMENT-3 intake (sentences 1978-2563).** ⛔⛔ **THE HEADLINE, AND IT IS THE WORST ENTRY IN THIS FILE: Rendering A renders `Eucharist` — the segment's central term — as *"the universe"* FIVE TIMES** (`Eucharist` 18 in B, 12 in A). ⭐ **Unlike *"Hyrea"*, which is visibly broken, *"the universe"* is ordinary grammatical English: a pass grepping Rendering A gets 12, has no reason to suspect a shortfall, and loses two load-bearing sentences. A plausible wrong word is more dangerous than an implausible one — the `hyperdulia` principle arriving in the ordinary-vocabulary direction.** **Fifteen further segment-3 manglings added in their own table**, including ⛔ **`Ante-Communion` → *"an Anticonunion"*** (so a grep of A for the term returns zero — and it was the intake brief's own named target), `adiaphora` → *"a diaport"*, `Maccabees` → *"The Bacchus"*, `Tobit` → *"tokens"*, and ⛔⛔ **`Zwingli` 0·0 while the name is spoken** (B mangles it to *"Swingley"*, A drops it entirely). ⚠️⚠️ **A BOUND ON THE DUAL-ASR PROTOCOL RECORDED: at s2014-2015 both renderings independently produce *"an omri"* and *"a pix"* for aumbry and pyx — they AGREE and are BOTH WRONG. Agreement is evidence two engines made the same inference, not that the inference was right.** ⭐⭐ **AND A FOURTH DEFECT SHAPE ADDED THAT IS NOT A MANGLING AT ALL: Rendering A is HARD-WRAPPED, so a line-oriented grep returns ZERO for any phrase straddling a line break — it produced FOUR false absences inside the pass itself before being caught.** ⭐ **The general rule is now a family of three: an absence is not reportable until chased through a rendering's own mangled forms, its own transcription conventions, AND its own line structure — all three are properties of the FILE, not the session, and a key-terms list fixes only the first.** ⭐ **Twenty terms added to the list** (`Eucharist`, `Ante-Communion`, `Deacon's Mass`, `aumbry`, `pyx`, `monstrance`, `ablutions`, `tabernacle`, `transubstantiation`, `memorialism`, `local presence`, `koinonia`, `adiaphora`, `regulative principle`, `good and necessary consequence`, `Zwingli`, `Maccabees`, `Tobit`, `Wisdom of Solomon`, `Didache`). ⛔ **Nothing already captured is rewritten and no prior wording is altered.**
- **260818-3 (2026-08-18):** ⚠️⚠️ **CORRECTED at the `A101-2026-08-09`
  segment-2 intake: the `260816-1` claim that Rendering B DROPS the Council of
  Hieria's name is FALSE.** Rendering B carries it twice as ***"Hyrea"***
  (sentences 1851-1852), grep-verified in three Rendering-B artifacts;
  Rendering A carries it twice as *"Hyria."* **Neither drops it and neither
  gets it right**, so the *"Rendering B is worse here"* claim is withdrawn too.
  ⛔ **The original wording and the `0 — DROPPED` table row STAND per the
  never-alter rule; a dated correction section is added beside them.** ⭐ **The
  generalisable rule adopted: when two renderings mangle a term differently, an
  absence in either is not reportable until the term is located in the rendering
  that has it and the other's local form is read off the corresponding timestamp
  window — never grep the second rendering for the first one's mistake.** ⚠️ **A
  second instance of the same shape recorded from the opposite side:** Rendering
  B writes *"2nd Commandment"* ×10 where Rendering A writes *"second
  commandment"* ×11, so a grep for `2nd commandment` against A returns zero for
  a term spoken eleven times. **Fifteen segment-2 manglings added in their own
  table; five terms added to the list** (`second commandment`, `Church
  Triumphant`, `Church Militant`, `Theotokos`, `cloud of witnesses`), and
  **`Trent Horn` deliberately NOT added** with the reason recorded.
- **260816-1 (2026-08-16):** File created with the `A101` intake of the
  2026-08-09 session. Eleven mangled forms verified by grep against
  `SRC_WHISPER_20260809.txt` before entry; ten confirmed as stated in the
  intake brief; **one corrected — the brief's `hyperdulia → "Hyria"` is
  the Council of Hieria (754), established from the surrounding date and
  the Second Nicaea reference, and Rendering B drops the name entirely.**
  Terms entered on expected-coverage grounds are segregated from terms
  entered on an observed mangling, and the absences are recorded as
  absences.
