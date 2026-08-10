# ASR Key-Terms List — Anglican 101 (`A101`)

**Last updated: 260816-1** (created 260816-1; date-stamped, format yymmdd-iteration)

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
Council of Hieria
Second Council of Nicaea
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

- **260816-1 (2026-08-16):** File created with the `A101` intake of the
  2026-08-09 session. Eleven mangled forms verified by grep against
  `SRC_WHISPER_20260809.txt` before entry; ten confirmed as stated in the
  intake brief; **one corrected — the brief's `hyperdulia → "Hyria"` is
  the Council of Hieria (754), established from the surrounding date and
  the Second Nicaea reference, and Rendering B drops the name entirely.**
  Terms entered on expected-coverage grounds are segregated from terms
  entered on an observed mangling, and the absences are recorded as
  absences.
