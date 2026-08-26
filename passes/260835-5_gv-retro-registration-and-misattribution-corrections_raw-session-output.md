# 260835-5 — raw session output (commands and key results, in order)

## Gate

```
$ git --no-optional-locks rev-parse HEAD
a0cc4f3837ba0335a386b14f450c3faa7d9f56ca

$ git --no-optional-locks status --short
(empty, exit 0)

$ python3 validate_project.py   [BEFORE]
...
80 ok · 9 warnings · 0 errors
Firing codes: C1 (1), C3 (2), C4 (1), C5 (3), C10 (1), C11 (1) = 9

$ grep -rhoE '\b26[0-9]{4}-[0-9]+\b' --exclude-dir=.git . | sort -t- -k1,1n -k2,2n | uniq | tail -5
260835-1
260835-2
260835-3
260835-4
=> next-free pass stamp: 260835-5

$ head -30 PROJECT_STATE.md
**Last updated: 260835-4** (created 260724-3) ...
=> PROJECT_STATE.md's own stamp at gate: 260835-4

$ ls passes/ | sort   [confirms naming convention]
```

Prerequisite read in full: `passes/260835-4_file-45-first-mining_pass-b2_close-out.md` (369 lines) — read via the Read tool before any other action, per the brief.

## Locating a201.txt and the GV findings

```
$ find . -iname "a201*" -not -path "*/.git/*"   (in theology/) -> nothing
$ find . -iname "a201*"   (in EMC/)  -> ./original transcripts/video transcripts/a201.txt

$ wc -c a201.txt
177254 a201.txt

$ wc -l a201.txt
22 a201.txt

$ awk '{print NR": "length($0)" bytes, prefix="substr($0,1,20)}' a201.txt
1: 50 bytes   (header banner)
3: 36991 bytes  ===Talk with Fr Matt ...   (recording 1)
5: 6259 bytes   ===A History of the C...   (recording 2)
7: 22845 bytes  ===The Memorialist Vi...   (recording 3)
9: 6845 bytes   ===A Bad Way to Under...   (recording 4)
11: 33901 bytes ===Response to "Shoul...   (recording 5)
13: 7676 bytes  ===Is Contemporary Wo...   (recording 6)
15: 39368 bytes ===The Stories We Tel...   (recording 7)
17: 19548 bytes ===Simply Anglican--A...   (recording 8)
19: 3749 bytes  ===Canterbury Cousins...   (recording 9)
```

Recording byte ranges cross-checked against and matching `SRC_Manifest.md`'s File 45 registration exactly (rec 1 @52-37,044 … rec 9 @173,501-177,253).

## GV finding location — grep sweep against St_Francis_EMC_Distinctives.md

```
$ grep -n "GV-[0-9]" St_Francis_EMC_Distinctives.md | grep -oE "GV-[0-9]+" | sort -u | wc -l
55

$ for n in 1..55: grep -n first occurrence line for GV-$n
=> full line map recorded (GV-1 @L389/792 area ... GV-55 @L1729 ... GV-37/54/9/32/34 @L4064-4074 ... changelog L6971)
```

Read in full (via the Read tool, in ~30-100 line windows given file size): lines 380-499 (GV legend + self-ID cluster), 585-694 (hermeneutics/method), 780-894 (justification/assurance/apostasy/baptism GV block, including GV-1/2/3/4/5/6/9/22/23/24/26/27/38), 940-969 (eucharist block, GV-3/15/16/21/36/43/46/51), 6915-6975 (changelog head and the L6971 GV reconciliation entry).

## Byte-offset re-derivation against a201.txt — grep -boF batches

```
$ grep -boF "physically united to the bread and the wine" a201.txt
45577:physically united to the bread and the wine

$ grep -boiF "consider myself High church" a201.txt
31131:consider myself High church

$ grep -boF "definitely received regeneration" a201.txt
2657:definitely received regeneration

$ grep -boF "regeneration has to precede" a201.txt
7830:regeneration has to precede

$ grep -boF "he remains faithful" a201.txt
19373 / 19478

$ grep -boiF "lordship Salvation guy" a201.txt
25996 / 26080

$ grep -boF "kicks me out of the Kingdom" a201.txt
19653

$ grep -boF "promise given" a201.txt
2091

$ grep -boF "reject the Roman understanding" a201.txt
31394

$ grep -boF "not even Catholic" a201.txt
67702

$ grep -boiF "high church anglican an anglo catholic" a201.txt
42688

$ python3 -c "... print byte windows ..."
@10380-10900 => "this goes back to Augustin[e] in my view Augustin[e] I think even
said that all the SA ACS both well I would say both sacraments um are received
by faith ... he is taken hold of of Christ by faith through ... the bread and
the wine ... and I would say the same thing is true with with baptism ..."
=> GV-3 anchor: "this goes back to Augustin" @10397 ; "same thing is true with
   with baptism" @10765

@4950-5150 => "...if you look in the catechism of uh 1571 or or whichever that
one you see in the catechism that it's talking about how the faith of the
family the of the parents those who are in charge of the child take..."
=> GV-9 confirmed @4950-5150

$ grep -boiF "barely protestant" / "historically protestant" a201.txt
35926, 35944 / 36208   => GV-7

$ grep -boiF "grandparents" a201.txt
30063   => GV-8 (context)

$ grep -boiF "duffy" a201.txt
42317   => GV-13 (recording 2)
python3 context check confirms: "...even duffy's the stripping of the altars
although i think that one not a big fan of that one honestly..."

$ grep -boiF "devout" a201.txt
176811  => GV-42 (recording 9)
python3 context check confirms: "...my relative who is a devout roman catholic
might be getting this for christmas..."

$ grep -boiF "oxford movement" a201.txt
124259, 124327   => GV-33 (recording 7)

$ grep -boiF "abundantly not the case" a201.txt
174950   => GV-41 (recording 9)

$ grep -boiF "david" a201.txt
175832  => FALSE POSITIVE ("david ford," a person's name) — GV-52/53 NOT located
this way; royal supremacy / civil magistrate / confederacy / first among equals
all separately confirmed absent from a201.txt

$ grep -boiF "women" a201.txt
119862 (rec 7, false candidate — ordinary use, checked in context, rejected)
157059 (rec 8 — confirmed: "...he's for women's ordination he does talk about
that a bit and obviously i would defer...") => GV-40

$ grep -boiF "satisfaction" a201.txt
109238 — checked in context, FALSE POSITIVE (worship/entertainment discussion,
not Article 31 / eucharistic sacrifice) => GV-45 NOT located this way

$ grep -boiF "thoroughly reformed" a201.txt
41631   => GV-11 (recording 2)

$ grep -boiF "semi" a201.txt
85035 (recording 5, inside the Acts 2:37-39 passage) => GV-25
117341 (recording 7 — different context, not used)

$ grep -boiF "absolution" a201.txt
160109  => GV-39 (recording 8)

$ grep -boiF "mormon" a201.txt
37252, 43263  => both recording 2 => GV-48 (partial locate)

$ grep -boiF "trinity school" / "m.div" a201.txt
(no matches) => GV-49/GV-50 UNLOCATED

$ grep -boiF "cookies and milk" / "parker" / "black rubric" / "book of concord" a201.txt
(no matches) => GV-46 UNLOCATED (recording inferred only)

$ grep -boiF "eastern orthodox" / "valid orders" a201.txt
35994, 36064 (rec 2), 44571 (rec 3 boundary), 59258 (rec 3), 117061 (rec 7)
— none confidently matching the specific "EO have valid orders" claim
=> GV-51 UNLOCATED (recording inferred only)

$ grep -boiF "royal supremacy" / "civil magistrate" / "cannot establish doctrine"
  / "confederacy" / "first among equals" a201.txt
(no matches, any of them) => GV-52/GV-53 UNLOCATED

$ grep -boiF "article 31" / "multiplied masses" / "none other satisfaction" a201.txt
(no matches) => GV-45 UNLOCATED

$ grep -boiF "sacrificing priest" / "officio" a201.txt
(no matches) => GV-47 UNLOCATED

$ grep -boiF "ad orientem" / "deuterocanon" / "lent" a201.txt
ad orientem: 113995 (rec 6, GV-30's territory)
lent: 26175, 26227 (rec1), 29840 (rec1), 89189 (rec5), 112803 (rec6), 140831 (rec7)
=> GV-55 UNLOCATED WITH CONFIDENCE (six candidates, none chosen)

$ grep -boiF "ryle" a201.txt
(no matches) => GV-12 UNLOCATED

$ grep -boiF "lens by which we should interpret" a201.txt
(no matches) => GV-44 UNLOCATED

## Task 4 material — grep -boiF against a201.txt

$ grep -boiF "gives you that faith and repentance" a201.txt
85089

$ grep -boiF "acts 2:38" / "both are put together" / "faith is a gift" a201.txt
75388, 97346 / 97627 / 99106  (all recording 5)

$ grep -boiF "demonstrated in Scripture" / "demonstrated within Scripture"
  / "monumental shift" / "switch those presuppositions" a201.txt
94612 / 97248, 97291 / 94556 / 106684  (all recording 5)

$ grep -boiF "confirmation" a201.txt
100232, 100310, 100569, 100582, 100976, 101935, 101965, 102315  (all recording 5)
```

## Edits applied (St_Francis_EMC_Distinctives.md, then PROJECT_STATE.md)

1. Top-of-file stamp `260835-3` → `260835-5`.
2. Dated correction sub-bullet inserted beside GV-4 (terminus-not-trigger withdrawal).
3. Dated correction sub-bullet inserted beside GV-3 (entire finding, Kennedy's).
4. Dated correction sub-bullet inserted beside GV-6 (Lordship-Salvation clause only).
5. Dated correction sub-bullet inserted beside GV-2 (quoted sentence only; claim survives at GV-10).
6. Sub-point added to GV-26 (Acts 2:37-39 exegesis / Discord antecedent) — no new number.
7. New finding minted: GV-56 (burden rule, four citations, caveat carried forward).
8. GV source-legend row updated: range GV-1..55 → GV-1..56.
9. Inline byte offsets added beside the five already-labelled findings (GV-9, GV-30, GV-32, GV-33, GV-34, GV-36, GV-37) and inline notes added to the GV-36/46/51 grouped bullet distinguishing located (GV-36) from recording-inferred-but-unlocated (GV-46, GV-51).
10. New section "GV batch — a201.txt byte-range retro-registration (added 260835-5)" inserted immediately before the CHANGELOG header, containing the full locator table for all 55 in-scope-or-excluded findings plus GV-56.
11. New CHANGELOG entry v4.9 (260835-5) prepended above v4.8.
12. PROJECT_STATE.md §4 registry row for St_Francis_EMC_Distinctives.md updated 260835-3 → 260835-5 with summary note, prior note retained under "Previously:".

## Validator runs

```
[interim, after content edits, before PROJECT_STATE.md registry update]
79 ok · 9 warnings · 1 errors
ERROR [C3] St_Francis_EMC_Distinctives.md: VERSION DRIFT — registry says
  '260835-3', document says '260835-5'

[after PROJECT_STATE.md registry row updated]
80 ok · 9 warnings · 0 errors
(identical firing-code set to baseline: C1, C3x2, C4, C5x3, C10, C11)
```

## Final state

```
$ git --no-optional-locks status --short
 M PROJECT_STATE.md
 M St_Francis_EMC_Distinctives.md

$ git --no-optional-locks rev-parse HEAD
a0cc4f3837ba0335a386b14f450c3faa7d9f56ca   (unchanged — nothing committed)
```
