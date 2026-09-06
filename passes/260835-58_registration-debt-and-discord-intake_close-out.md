# 260835-58 — Registration debt and Discord intake

**Date:** 2026-09-06 · **Class:** registry maintenance · **Ledger numbers consumed: NONE**

⛔⛔ **Nothing in this pass is a finding about Rev. James.** No `DQ`, `IP`, `LS`, `RV`, `Rev`, `BLOG`, `POD`, `VP`, `GV`, `RC`, `BP`, `EXT`, `W`, `File` or `DELTA` number was consumed, and none was minted. No research was done. Not one analytical conclusion in any file was altered.

---

## 1. Gate

| Item | Value |
|---|---|
| HEAD | `cb833ea`, branch `main`, *"latest new discord channel raw txt for input"* — **the brief's HEAD confirmed** |
| `git status --short` | **EMPTY** before the first edit |
| Validator baseline | **98 ok · 11 warnings · 0 errors**, `C0` **34** files, `C6` **5** — the brief's figure confirmed by re-running, not trusted |
| Stamp | **260835-58**, derived by grep after reading the `260835-12`/`260835-14` hazard note first, as the brief required. Both re-confirmed REAL and CONSUMED, neither treated as free. Distinct-stamp sweep over tracked `*.md`/`*.py`/`*.txt`, numerically sorted: unbroken run `260835-1 … 260835-57`, no gaps. `260835-58`, `260835-59` and `260836-1` each returned hits; **all were opened and read in context and all are `260835-57`'s own forward absence-assertion** (*"`260835-58`, `260835-59`, `260836-1` return ZERO"*) at `Incense_Reply_Source_Checks.md` L39 and `passes/260835-57_…_close-out.md` L24 — **content hits, not consumptions, the exact shape the hazard note warns about.** `260835-99` re-confirmed NOT a stamp. `260835-60` and `260836-2` return ZERO. `git log --all` and `passes/` both top out at `260835-57` |
| Mode | RECONCILE. Stamps reported against §4 registry cells before editing; no drift found |

---

## 2. ⛔⛔ Two of the brief's own instructions were falsified at gate and withdrawn by JD before any edit

These were put to JD as blocking questions and answered before a single file was written. Both are recorded here **because the brief asked that a later pass not re-raise them as debt.**

### 2a. §4 rows for the twenty-five capture files — the brief's Item 1 contradicts the project's own recorded convention

Two independent findings forced the question.

**(i) No external primary text has ever carried a `PROJECT_STATE.md` §4 row.** Not the Westall book, not either prayer book, not the page-images PDF, not the folio JSON, not Brattston. The `260835-34`/`260835-35` ruling that created the class says so in terms: *"Rows here are identified by path and hash only."*

**(ii) The exemption is explicit for exactly this file shape.** `SRC_Manifest.md` records that `src/SRC_Discord_RPW-raw.txt` is *"deliberately NOT given a `PROJECT_STATE.md` §4 row — it is a stamp-less capture file; the exemption is recorded there … a decision, not an oversight."*

**And the mechanism behind that decision was confirmed by reading `validate_project.py`, not assumed.** `C3` skips only basenames beginning `SRC_Discord_`. Twenty-four `SRC_PRIMARY_`/`SRC_SECONDARY_` §4 rows would therefore each raise *"no parseable 'Last updated' stamp"* — **warnings 11 → about 33** — and the only way to silence them would be to write stamp lines **into never-alter capture files**, changing the very hashes this pass was registering.

> **JD's ruling:** *"manifest only, hold §4. The recorded convention governs, not the brief."*

### 2b. The brief's expected direction is wrong and is withdrawn by its author

The brief expected *"C0 and C6 examining more files."* Neither can move under the ruling above. `C0`'s file set **is** the §4 table. `C6` hashes only `SRC_Discord_*.md` archives resolved from §4, and the new capture is a raw `.txt` with **no archive of record** — `C6` could grow only by building `src/SRC_Discord_Followup.md`, which is intake work carrying content judgment.

> **JD's ruling:** do not build the archive; record it as owed. **Corrected expectation: `C0` stays 34, `C6` stays 5, warnings drop by two from Item 4.**

**Both held exactly.**

---

## 3. Item 1 — twenty-four captures registered

**File list derived by diffing, not trusted.** `git show --stat 2ed1c2a` → nineteen `src/` files; `f850609` → five. Twenty-four, plus the new Discord raw = the brief's twenty-five exactly. An independent check confirmed **these twenty-five and no others** are tracked in git yet absent from `SRC_Manifest.md`.

Registered as a **dated table appended to `EXTERNAL PRIMARY TEXTS`**, unnumbered on the `260835-35` class-wide ruling. A separate table rather than rows inserted into the existing one, because that table is followed by five dated notes and inserting into its middle would place `260835-58` material above prose written before it existed. **The two tables are one register and must be read together.**

- Bytes, lines and whole-file `sha256` **computed this pass from the files on disk**, plain `sha256sum`, no stripping.
- Every `Work` and `Provenance` cell **transcribed from the capture file's own `CAPTURE HEADER` block and from nowhere else.**
- ⚠️ Each row notes that the byte and line counts **include the capture header**, which is not part of the source — so an offset into any of these files is an offset into header-plus-source.

### Unstated fields — recorded as unknown, per the brief

A dedicated block after the table lists every field the headers do not state. **Nothing was supplied from general knowledge of the work, however obvious.**

| Field missing | Rows affected |
|---|---|
| No copyright statement | 9 |
| Publisher and/or place not stated | 5 |
| Year not stated | 5 (Church Association Tract 259 alone accounts for 3) |
| URL not resolvable from the header | 3 (Gihr prints a URL *template*; Fortescue an item id only; the GIRM file's `romanliturgy.org` Latin) |
| Transcription's own retrieval date | 2 (both Project Canterbury pages) |
| Per-entry retrieval dates | 1 (the Byzantine variants collation) |
| Translator not named | 1 (Gihr 1902) |

⛔ **This pass verified none of these texts against their sources.** The capture judgments belong to `260835-56` and `260835-57` and are unreviewed here.

---

## 4. Item 2 — the sixth Discord thread, and the 1899 quotation check

`src/SRC_Discord_Followup-raw.txt` — thread **"Followup questions"**, opened by JD after the classes wrapped, carrying his opening post and **four consecutive Rev. James replies**: five numbered responses, the two-argument frame, the De Koven/Malachi side note, and his quotation of the 1899 Opinion.

Registered in `SRC_Manifest.md` (`Discord Thread Archives`), `SRC_Coverage_Register.md` §6, and given a canonical alias **marked as resolving to no archive**.

⛔⛔ **It is the corpus's first Discord thread with no archive of record.** `src/SRC_Discord_Followup.md` does not exist. The thread is invisible to `C1` and `C6`, is not mined, and **nothing in it may be cited.**

⏳⏳ **Owed intake work, and the pass that takes it inherits a stated weakness.** The raw carries no `CAPTURED …` line and **all five headers are bare times with no date anywhere in the file** (`9:55 AM`, `3:01 PM`, `3:10 PM`, `6:34 PM`, `6:50 PM`). The `260833-6` capture-line method cannot run. Dates must come from the **weaker commit-timestamp-plus-elimination warrant** used at `260835-26`/`-28`/`-41`, bounded above by `cb833ea` — and that warrant class must be recorded on every date it produces.

⛔ **`SRC_Channel_Inventory.md` was checked and deliberately given no row.** It is a YouTube video inventory keyed on video ID; a search of it for "discord" returns **zero** hits, and no Discord thread has ever had a row there. Creating one would have invented a category. A `260835-58` dated note records the non-application, on the same principle as that file's own `260835-42` note.

### The 1899 Opinion quotation — checked, three divergences, all editorial

Compared against `src/SRC_PRIMARY_1899_Archbishops_Lambeth-Opinion-Incense-Lights.txt` after NFKC normalisation, quote folding, whitespace collapsing, and removal of Project Canterbury's `[n/m]` page markers. **A raw byte comparison was not run** and would report Discord rendering artifacts as differences.

✅ **Three of five stretches identical**, including the load-bearing one he actually deploys — the *"In conclusion, we are far from saying…"* conclusion, **906 characters, exact.**

| # | Side | Divergence |
|---|---|---|
| 1 | His | Comma inserted after *"intended"* — *"…the symbolism is intended, to teach, to the symbolism itself."* Primary has no comma; primary is the grammatical reading. Sense unchanged |
| 2 | His | Quotation marks dropped around *"understanded by the people"*. Nothing else in the sentence differs |
| 3 | ⛔ **NOT his** | Primary reads *"in emitting [sic: \"omitting\"] incense"*; his reads *"in emitting incense"*. **Both texts read "emitting."** The difference is Project Canterbury's own editorial gloss — transcription apparatus, **not a divergence in the Archbishops' text**, and must never be reported as one |

⏳ Divergence 3 does mean the printed 1899 Macmillan reading at that point is **unverified by this project** — the repo holds no page image of the 1899 printing. Recorded as owed, not resolved.

⛔ **Neither text normalised to the other.** The raw is untouched; the `260835-56` capture is untouched. The dated note in the manifest is the only record of the comparison.

⚠️ One structural observation recorded and not acted on: he presents the *"Further, it must be remembered…"* block **without quotation marks**, split across messages with his own `(continued)` markers. A later pass must not read those markers as his words, nor the unmarked block as his own prose.

---

## 5. Item 3 — the `CAPTURED …` line debt: five, verified, unrepairable

Every commit touching a raw Discord artifact was listed and **its first line read directly out of git**, rather than taken on the brief's say-so.

| Commit | When | Pass | First line |
|---|---|---|---|
| `cb833ea` | — | this thread's capture | ⛔ **none** (`Followup questions`) |
| `b65c4b61` | 2026-09-01 03:37 ET | `260835-46` | ⛔ **none** — the state at `HEAD` |
| `b9d17f3` | 2026-08-30 09:22 ET | `260835-41` | ⛔ **none** |
| `4c96038` | 2026-08-28 22:52 ET | `260835-28` | ⛔ **none** |
| `baa2f09` | 2026-08-28 17:04 ET | `260835-26` | ⛔ **none — deleted here** |
| `2427eba` | 2026-08-28 08:21 ET | — | ✅ `CAPTURED 2026-08-28, 8:21 AM ET…` |
| `dba65d3` | 2026-08-25 15:51 ET | — | ✅ `CAPTURED 2026-08-25, 3:12 PM ET…` |
| `4367a70` | 2026-08-24 19:39 ET | — | ✅ `CAPTURED 2026-08-24, 7:38 PM ET…` |

⭐ **The regression begins exactly at `260835-26`**, as the manifest records.

⛔⛔ **No line was added to any file**, on three independent grounds, each sufficient alone:

1. The capture date is a fact about when JD copied from the Discord client and is recorded **nowhere in the repo** — only the commit timestamp bounds it above. Writing one would **fabricate a date**, which the brief expressly forbids.
2. A raw capture artifact is **never edited** and is superseded only by a later capture.
3. Four of the five are **historical git states not on disk** and cannot be edited at all.

⏳⏳ **The debt stands at five and remains owed to JD. It is closeable only prospectively — by the next capture carrying the line.**

`SRC_Coverage_Register.md` §6 also gains the **`260835-46` extension, back-registered**: it never reached that file, whose last §6 entry was `260835-41` while its stamp read `260835-42`. ⚠️ Written from `SRC_Manifest.md`'s own cells and from git; **the comparison was not re-run and this pass does not vouch for it independently.**

---

## 6. Item 4 — stamps

Both standing `C3` warnings closed **without touching either file's content.**

| File | Stamp written | Why not `260835-58` |
|---|---|---|
| `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` | `260832-2` | The registry's own value. Content vintage did not change; a bump would assert a revision that did not happen |
| `tools/transcribe_yt.py` | `260833-7` | Same. No code, default, flag or behaviour altered; the script was not run |

Each carries a one-paragraph note recording that the stamp line was **added at `260835-58` as a format repair**, that nothing else was altered, and that the §4 registry cell is unchanged. **Both §4 cells therefore stand at their existing values and `C3` now compares them green.**

Stamps bumped to `260835-58`, with §4 cells bumped in the same pass: `PROJECT_STATE.md`, `SRC_Manifest.md`, `SRC_Channel_Inventory.md`, `SRC_Coverage_Register.md`.

---

## 7. ⏳ Found and not fixed

- ⛔⛔ **`Ceremonial_Meaning_Source_Checks.md` and `Incense_Reply_Source_Checks.md` are registered NOWHERE** — not in `PROJECT_STATE.md` §4, not in `SRC_Manifest.md`. They are the **first and second external-research documents in the `260835-44`…`260835-53` series never given a registry row**. Registering an analysis document is a §4 `Class`/`Audience` judgment that is JD's, not this pass's. **Recorded as owed, at the manifest and in the gate note. Not fixed.**
- ⚠️ **The two raw Discord artifacts are treated inconsistently:** `src/SRC_Discord_Assurance-raw.txt` has a §4 row; `src/SRC_Discord_RPW-raw.txt` deliberately has none. Recorded; neither altered.
- ⏳ The 1899 Macmillan printed reading at *"emitting/omitting"* is unverified by this project (no page image in the repo).
- ⏳ `src/SRC_Discord_Followup.md` — the archive — is owed, with the weaker dating warrant it inherits stated above.

---

## 8. Validator

| | Before | After |
|---|---|---|
| **Coverage — `C0` registry resolution** | 34 files | **34** |
| **Coverage — `C6` archive hash integrity** | 5 files | **5** |
| `C3` version stamps vs registry | 28 | 28 |
| **ok** | 98 | **100** |
| **warnings** | 11 | **9** |
| **errors** | 0 | **0** |

**Exactly JD's corrected expectation.** The two warnings that cleared are the two `C3` items in Item 4; the `ok` count rose by the same two, which now pass instead of warning. Every remaining warning is one that predates this pass and none is in its scope: `C1` ×1, `C4` ×1, `C5` ×3, `C10` ×2, `C11` ×2. **Errors did not move off zero at any point.**

---

## 9. Commit sequence

Per the brief: this pass artifact and its `.diff` are committed **alone**. **The corpus commit is held for JD's review.**

Files changed and awaiting that review: `PROJECT_STATE.md`, `SRC_Manifest.md`, `SRC_Channel_Inventory.md`, `SRC_Coverage_Register.md`, `Calvin_Luther_and_Anglican_Formularies_on_Iconography.md`, `tools/transcribe_yt.py`.

⚠️ **Emission-discipline note.** `CLAUDE.md` requires the full registered set to be committed together in one commit. This pass's brief overrides that with an explicit two-stage sequence, and the artifact commit deliberately contains **no corpus file**. The six above are complete and consistent in the working tree; **none is partially written.**
