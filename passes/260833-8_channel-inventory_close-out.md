# 260833-8 — `SRC_Channel_Inventory.md` created: channel video inventory and decision backfill, no source registered

**Pass artifacts:** `passes/260833-8_channel-inventory.diff` (as applied — `git diff` for tracked files plus a `git diff --no-index /dev/null SRC_Channel_Inventory.md` block for the new untracked file, since this pass was instructed not to run `git add`) · this file.
**Gate:** HEAD `e0919c199f8efce27663d7ff0211d8b6456d0629` (*"260833-7: transcribe_yt.py moved into version control (tools/); auth-probe self-rewrite defect fixed; no intake, no finding minted"*), confirmed by `git rev-parse HEAD` before any edit; matches the brief exactly.
**Validator BEFORE:** `79 ok · 7 warnings · 0 errors` — confirmed to be the actual baseline (matches the brief's stated expectation exactly). The seven: C1 (`src/SRC_Discord_RPW.md`, 1 relative timestamp), C3 ×2 (`Calvin_Luther_and_Anglican_Formularies_on_Iconography.md` and `tools/transcribe_yt.py`, unparseable stamps), C4 (`St_Francis_EMC_Distinctives.md`, 2 answered-as-pending), C5 ×2 (`RJ_Final_Question_List.md` 17 / `RJ_Incense_Analysis.md` 9 volatile-state assertions), C11 (outline 4 findings behind the DQ ledger head).
**Validator AFTER:** `81 ok · 7 warnings · 0 errors` — the identical seven warnings, zero errors; the `ok` count rose from 79 to 81 (the new file's own C3/C0 checks passing clean). Mid-pass a transient `2 errors` state occurred (`[C3] VERSION DRIFT` on both `PROJECT_STATE.md` and `SRC_Manifest.md`) after their top `Last updated` stamps were bumped to `260833-8` before their own §4/self-registry cells were updated to match — the same near-miss class the `260833-2` and `260833-7` close-outs record; fixed by updating both registry cells in the same pass, confirmed clean by the final AFTER run.
**Stamp reasoning:** `grep -rhoE '2[0-9]{5}-[0-9]+' --include=*.md .` across the whole repo found the highest existing stamp to be `260833-7` (the gate commit itself). `passes/` filenames follow `<stamp>_<slug>.diff` with the iteration number incrementing within the same day-bucket (`260832-...` ran 1-5, `260833-...` has run 1-7 so far) — no evidence of a day-bucket-increment rule when the bucket isn't exhausted, so `260833-8` was chosen as the next iteration on the same bucket. `grep -rn "260833-8"` returned zero hits before this pass's first edit.
**No finding minted. No `File`, `LS`, `IP`, `RV`, `DQ`, `VP`, `DELTA` or `W` number consumed.** Nothing committed, staged, or pushed — `git add`/`git commit` are left for JD, per instruction. (Note: a `git add -A` was attempted mid-pass to capture a diff via the usual staged-diff method; it failed outright with a pre-existing `.git/index.lock` from outside this pass's own git usage, so nothing was actually staged. The diff artifact was captured instead via plain `git diff` for tracked files and `git diff --no-index` for the new untracked file, neither of which touches the index.)

---

## 0. This pass's actual scope

This is a **decision-recording pass, not an intake pass.** It creates `SRC_Channel_Inventory.md`, a companion registry to `SRC_Manifest.md`, cataloguing all 368 videos across the `@barelyprotestant5365` (`EXT-2`, 306 videos) and `@StFrancisAnglicanSpartanburg` (`EXT-3`, 62 videos) YouTube channels, pulled via `/Users/jd/EMC/channel_videos.tsv` and `/Users/jd/EMC/channel_metadata.jsonl` (both held outside the repo, on the existing `PROJECT_STATE.md` §0 footing already used for `BLOG`/`POD`/`A101` stream sources). No new source was read for content, no transcript was fetched, and no finding of any kind was minted.

## 1. Source-data verification (Step 3)

- `channel_videos.tsv`: 369 lines total (1 header + **368 data rows**, confirmed via `wc -l` and a `csv.DictReader` row count). Columns: `video_id, duration_seconds, upload_date, title, channel_code, channel_handle, source_tab`. The TSV's own `upload_date` column is `NA` for all 368 rows (not populated at scrape time).
- `channel_metadata.jsonl`: located at `/Users/jd/EMC/channel_metadata.jsonl` (185,624 bytes) — **364 records**, confirmed by `wc -l`. A second file, `channel_metadata_test.jsonl` (44 bytes, one dummy `{"video_id": "test", ...}` record), was found alongside it and is **not** the metadata file — excluded from this pass.
- **Set-difference, computed programmatically** (Python, sets of `video_id` from each file): 368 TSV IDs minus 364 JSONL IDs = **exactly 4**: `Wt7HI5SJahk`, `mfty5D0PAF0`, `b6hTPg50R9Q`, `7HKFlfqG1jY` — an exact match against the brief's expected list. The reverse difference (JSONL IDs not in TSV) is empty — every JSONL record has a corresponding TSV row.

## 2. Exact-ID matches — Files 27-34 (Step 5a)

`SRC_Manifest.md` was searched (`grep -n "\*\*File 2[7-9]\*\*\|\*\*File 3[0-4]\*\*"`) for each of the eight video IDs already recorded in that file's own Files 27-34 provenance tables (`A2JI_p52Tyo`, `5sfXxCPx05M`, `q7XR5CJrzM4`, `3h7MIO4srEs`, `rH3unprZ0iE`, `uSHi3Fqgerg`, `Vfq5b5btlVw`, `BXqUAK9Mxg0`). All eight were found, matched strictly by ID equality against the TSV, and the finding ranges recorded — `LS-100`…`LS-110` (Files 27-29, batch `260831-1`) and `LS-111`…`LS-120` (Files 30-34, batch `260831-3`) — were pulled directly from that file's own batch pass-notes, not invented. No range was split further per individual File because `SRC_Manifest.md` itself does not record a finer per-file breakdown within a batch.

## 3. Inexact title matches — Files 1-26 (Step 5b)

Each File's working title (or, where only a guest surname was recorded — Files 20-22, 24 — the surname) was searched against all 368 TSV titles. Every candidate that survived was cross-checked a second, independent way: the JSONL `upload_date` was compared against the recording-date evidence `SRC_Manifest.md` had already established for that File from internal content cues, entirely independent of the title search.

**Result: 19 of 26 matched, corroborated by both title and independent date agreement** (within 0-2 days, consistent with a UTC-vs-local-time offset already visible across every checked pair) — Files 3, 5, 6, 7, 10, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26. Two of these (Files 22 and 24, both guest River Devereux) initially returned 4 title candidates each; the date cross-check resolved both to a single exact-date match (File 22 → `jEBzUZ1cZLI`, upload `2021-08-18`, exact match to the manifest's own internally-corroborated date; File 24 → `edFjnm7mYfM`, upload `2021-05-08`, inside the manifest's stated `late 2020–2021-05-22` window and the only "Eucharist"-titled candidate, matching the File's own working filename `Eucharist-sentences.json`).

**Marked `INGESTED (inexact title match)`, never plain `INGESTED`,** per instruction — every one of these 19 decision cells says so explicitly.

**2 left ambiguous** — Files 11 and 12 (`a306`/Session XIV, `a307`/Session XV per each File's own internal numbering). The channel's own title-numbering has no "Session XIV" entry at all, and its "Session XV" title carries the content the manifest attributes to File 11 (Revelation 17-18), while its "Session XVI" title carries the content attributed to File 12 (Revelation 19, the marriage supper of the Lamb). This is a genuine, pre-existing off-by-one between the corpus's internal session count and the channel's own title-numbering — `SRC_Manifest.md` itself records repeated instability in this series' session numbers (Session XII missing from the channel; three distinct header-length "lessons" already logged for adjacent Files). Rather than force a match on content alone against a File's own stated number, both were left **blank** and the conflict recorded in `SRC_Channel_Inventory.md`'s own §5b section.

**5 had zero candidates** — Files 1 and 2 (in-person audio recordings of a class, confirmed never uploaded to either channel — no comparable title exists), File 4 (one file spanning three Revelation sessions, IX-XI, with no 1:1 video), Files 8 and 9 (one nine-block transcript pair spanning eight sessions with a mid-session split, likewise not reducible to a single video per file).

## 4. Category declines (Step 5c)

The remaining 339 videos (368 minus the 27 exact/inexact matches from Steps 2-3) were reviewed against the ten known decline categories from the prior ~120-video triage (gaming, UFO, politics/culture-war, scandal/personality, non-Christian apologetics, hell/annihilationism, dispensationalism, channel admin, unrelated book/film review, guest-conference sessions). Titles (and, where a JSONL record existed, the first ~300 characters of description) were reviewed under an explicit conservative instruction: only decline where the category is unambiguous, leave blank whenever a video could plausibly be Anglican/Christian-doctrine content of the kind this project wants preserved for future judgment.

**Result: 56 declined, 285 left blank.** Breakdown by category:

| Category | Count |
|---|---|
| channel-admin | 11 |
| politics | 10 |
| gaming | 9 |
| guest-conference | 8 |
| scandal | 5 |
| ufo | 4 |
| hell-annihilationism | 3 |
| dispensationalism | 3 |
| non-christian-apologetics | 2 |
| book-film-review | 1 |
| **Total** | **56** |

Every decline is dated `2026-08-25` (this pass's date). Explicitly and deliberately left blank rather than force-classified: every "Revelation Class"/"Anglican 101"/"Ante-Nicene Fathers" session title (the already-tracked class series), Perseus Conference *announcement/promo* videos (only the actual recorded conference-session talks were declined as `guest-conference`), personal-update videos with substantive content beyond channel logistics (e.g. health/diagnosis videos), and book reviews of theologically-themed (non-entertainment) works.

Two of the four no-metadata-gap video IDs (`mfty5D0PAF0`, `b6hTPg50R9Q`) were declined as `gaming` on title alone (no JSONL description exists for either) — both titles are unambiguous ("Livestream Gaming: Sea of Stars", "Impromptu Gaming Stream"). The other two gap IDs (`Wt7HI5SJahk`, `7HKFlfqG1jY`) were left blank — no comparably unambiguous title signal was found for either.

## 5. Upload-date scope-difference analysis

Computed directly: of the 306 `EXT-2` rows, 302 have a JSONL record (i.e. a real upload date); of those 302, only **4** postdate 2026-07-25 (`-4r_jF7YRpU` 2026-08-04, `wXH9IM-FWTs` 2026-08-25, `1URyNWfhjz8` 2026-08-13, `EzZypB5cBBM` 2026-07-31). Also computed: 224 of the 306 `EXT-2` rows carry `source_tab = streams` and 82 carry `source_tab = videos`. This is recorded in `SRC_Channel_Inventory.md` as **well-supported but not certain** evidence that the count difference between this pull (306) and the prior 2026-07-25 triage (219, per the brief) is a tab-scope difference (the older triage most likely covered only the `/videos` tab) rather than 87 videos of genuinely new content — not certain because the older triage's exact tab scope was never directly confirmed in any surviving record.

## 6. Registration (Step 7)

- **`SRC_Channel_Inventory.md`** created at repo root, following `SRC_Manifest.md`'s own header/stamp/table conventions (pipe tables, `**Last updated:**` line, dated pass-note-style prose sections). Stamped `260833-8`.
- **`SRC_Manifest.md`** — added a companion-registry pointer note immediately under its own `Last updated` line, and a full `260833-8` pass-note entry (in the file's existing reverse-chronological convention) summarizing this pass. Its own `Last updated` stamp moved `260833-6` → `260833-8`. ⛔ No existing File block, hash, byte offset or finding text was touched.
- **`PROJECT_STATE.md`** — added a `260833-8` pass note at the top (before the `260833-7` note, same reverse-chronological convention), added a new §4 registry row for `SRC_Channel_Inventory.md`, and updated the existing `SRC_Manifest.md` and `PROJECT_STATE.md` (self) registry-row version cells to `260833-8` to keep C3's version-drift check clean.

## 7. Constraint confirmations

- No File, finding, `LS`, `IP`, `RV`, `DQ`, `VP`, `DELTA` or `W` number was minted, renumbered, or altered anywhere.
- No existing hash, byte offset, or finding text in `SRC_Manifest.md` or `St_Francis_EMC_Distinctives.md` was touched.
- Nothing was posted, drafted, or altered toward Rev. James; no gate moved; no channel state changed.
- Nothing committed, staged, or pushed by this pass.

## 8. What is left for JD

`git status --short` (see the chat close-out for the literal, complete output) shows `M PROJECT_STATE.md`, `M SRC_Manifest.md`, `?? SRC_Channel_Inventory.md`, and `?? .scratch_inv/` (this pass's own working-data scratch directory — TSV/JSONL intermediate files used to build the inventory table; **not intended to be committed**, and could not be removed from this pass's own sandboxed mount — flagged for JD to delete manually, e.g. `rm -rf .scratch_inv/`, before or instead of staging anything else). To commit the actual registry change:

```
git add PROJECT_STATE.md SRC_Manifest.md SRC_Channel_Inventory.md passes/260833-8_channel-inventory.diff passes/260833-8_channel-inventory_close-out.md
git commit -m "260833-8: SRC_Channel_Inventory.md created — 368-video channel inventory, decision backfill, no source registered"
```

`.scratch_inv/` should NOT be staged.
