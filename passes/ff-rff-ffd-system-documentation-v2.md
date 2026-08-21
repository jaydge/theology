# FF / RFF / FFD Thread Fork and Retrieval System

**Version:** 2.0
**Date:** August 21, 2026
**Owner:** JD Smith
**Status:** v1 system is live and in use. v2 architecture (doc-backed state) is specified but untested.

**Purpose of this document:** Documentation of record for the three memory-stored prompt shortcuts that manage forking Claude chat threads, retrieving information across forks, and issuing delta handoffs. The verbatim prompt texts below are what is currently stored in Claude's memory. The rationale sections preserve design reasoning that was deliberately stripped out of the memory entries to reduce their per-conversation token overhead.

**This copy is being handed to a separate thread for beta testing of the v2 architecture.** See the Beta Test Brief immediately below.

---

## Beta Test Brief (for the receiving thread)

You are being handed this document to validate the v2 architecture described in the section "Planned evolution: doc-backed state." The v1 system already works and is in production use. Do not redesign it. Your job is to determine whether the v2 store mechanics actually function before JD invests in rewriting the memory prompts.

**Test in this order. Stop and report if any step fails.**

1. **Verify the write primitive.** Using the GitHub MCP connector, write a small test handoff document to a repository. Confirm it lands.
2. **Verify the read-back.** From a position of no prior context about that file, retrieve it by path and confirm the content is complete and legible.
3. **Verify in-place update.** This is the critical test. Read the file to obtain its blob SHA, then update it in place with modified content using that SHA. Confirm the update succeeded, the history shows two commits, and the diff is what you expect. This is the capability the entire v2 design depends on.
4. **Verify discoverability.** From a fresh context, locate the handoff document without being given its exact path, using only a naming convention and search. If this fails reliably, the convention needs to be more predictable or JD needs to supply a path each time.
5. **Test the failure modes.** What happens on a stale SHA (someone else updated the file between your read and your write)? What happens if the connector is unavailable mid-task? Both are realistic in JD's multi-thread workflow.

**Report back:** which steps passed, actual error text for anything that failed, and a recommendation on whether v2 is worth building. A clear negative is a useful result.

**Known constraint going in:** JD's CS course project already flagged GitHub MCP push reliability as unconfirmed, with manual local commit and push as the working fallback. If the connector proves unreliable for writes, note that the fallback (Claude generates the file content, JD commits it manually) still delivers most of the v2 benefit and should be evaluated as the realistic path rather than treated as a failure.

---

## System overview (v1, current)

Claude chat threads accumulate context cost: every attachment and message is resent and re-billed on every turn for the life of a thread, input over 200K tokens bills at 2x, and long threads bury active work under stale noise. Claude.ai chat has no native fork or user-invocable compaction. This system is a manual workaround:

1. **FF** in a heavy or pivoting source thread produces a dense, copy-pasteable handoff block.
2. JD pastes the block into a fresh thread and continues work there at a fraction of the per-turn cost.
3. **RFF** in the new thread reaches back for anything the handoff did not carry, either by Claude searching the source thread directly or by generating a retrieval prompt for JD to relay.
4. **FFD** in the source thread produces incremental delta passes when the source thread continues to accumulate information after the first handoff.

The **fork tag** (e.g. `FORKTAG-CS-p4k9m2`) is the spine of the v1 system: a unique string generated in the source thread's own text, carried verbatim into the forked thread, existing in exactly those two conversations, so `conversation_search` can positively identify the source thread later without relying on fuzzy keyword matching.

### Workflow (prose form)

Source thread gets heavy or pivots, run `FF`, copy the block (excluding the Context Snapshot), paste as first message of new thread, confirm the FORKTAG line survived the paste verbatim, work in the new thread. When a gap appears, run `RFF` (bare, or with a steer). Claude retrieves directly or hands back a retrieval prompt; if prompted, paste the prompt into the source thread and relay answers back. If the source thread keeps accruing new information, run `FFD` there for incremental passes.

---

## Prompt 1: FF (fork/handoff)

### Stored memory text (verbatim)

> "FF" prefix (also "FF:", "FF -"): generate a fork/handoff prompt for the current (source) thread as one copy-pasteable block. MANDATORY FIRST LINE of output: a literal fork tag, format FORKTAG-<short word/client hint>-<6 random alphanumerics> (e.g. FORKTAG-ADT-x7k2p9), on its own line before anything else. A prose description of provenance does not satisfy this; if the tag line is missing, the output is nonconforming and must be fixed in the same turn (verify before finishing). Directly under the tag: a few plain-language fallback keywords, and the thread's URL if recent_chats returns it (if not found or it returns an unrelated thread, say so; the tag is the retrieval method regardless). Bare FF = high-fidelity preservation of the ENTIRE thread: full substance of facts, decisions, attachments, terminology, open questions. Never prune on Claude's own judgment; save tokens via tighter phrasing, not omission. Mark corrected facts as superseded rather than dropping or restating them as current; omit only truly inconsequential resolved logistics. For anything uncertain, write "no record"/"uncertain" -- never plausibly reconstruct. Bare FF always produces the complete canonical structure even if prior handoff/delta outputs exist in the thread; prior handoffs never change FF's shape (deltas are FFD's job). Trailing text after FF: classify intent first -- (a) new-focus/topics-to-drop = pruning mode: weight toward JD's stated focus and omit only what he flagged or what it supersedes; (b) depth/extraction request = honor within full fidelity, no pruning; (c) delta request = apply FFD rules. If ambiguous, state the chosen interpretation at the top. Sections after the tag block: (1) thread purpose, one line; (2) established facts, confidence-flagged if disputed; (3) decisions JD explicitly made, distinct from Claude suggestions; (4) attachment contents transcribed in full substance (actual values/text, not "a screenshot of X"), sorted source material (docs JD would consult again in original form) vs working artifacts (screenshots, drafts); (5) recommended verbatim re-attachments: source-material files where summary risks loss (e.g. contract, spec) -- name file and why; (6) open questions, separate from facts; (7) thread-specific terminology/shorthand/client context; (8) current task and concrete next step; (9) RFF guidance: one line -- direct retrieval via tag search vs generated prompt back to JD (note if tag/URL retrieval already failed when tried); (10) gap-check line: what may not be fully captured; in pruning mode also list what was deliberately dropped per JD's scope vs possible genuine omissions. Generate without asking permission. AFTER the block, clearly separated, a "Context Snapshot" for JD only (never pasted forward): message count, attachment count by type, rough token estimate (~1.3-1.4 tokens/word). Caveat: floor not total (system prompt, tools, memory, image/PDF overhead invisible); if the thread appears longer than visible context, say so and label counts as floors over the visible portion, never corrections to JD's own counts. Not precise; don't use to explain usage-bar movements.

### Design rationale

- **Tag as mandatory first line.** In live testing (CS orchestration thread, August 2026), the tag requirement was violated twice despite being explicitly written into the instruction: once by the entire canonical structure being skipped in favor of a delta-shaped output, once by a narrative "provenance" section replacing the literal string. Positioning the tag as the unmissable first line, plus an end-of-output self-check, is the hardening that resulted. A rule buried as item 9 of 11 in a dense paragraph loses attention competition.
- **Anti-anchoring clause.** The delta-shaped failure happened because the thread's most recent similar exchange was a delta pass, and bare FF anchored on that pattern instead of the canonical template. The trigger word alone does not fully override recent conversational pattern; the instruction now says so explicitly.
- **High fidelity by default.** An earlier draft let Claude prune "no longer relevant" content on its own judgment. JD rejected this: bare FF must preserve everything at full fidelity, with pruning only on explicit instruction, because Claude's relevance judgment on an early, proactive fork is unreliable. Not enough has happened yet to distinguish noise from about-to-matter.
- **Intent classification for trailing text.** Real usage showed trailing text after FF can mean three different things: pruning/steering, a depth-extraction request (e.g. "give me the direct quotes and judgment calls from the Week 1 review"), or a delta request. Treating all trailing text as pruning would misread a depth request as "drop everything else."
- **"No record" over reconstruction.** Originated in JD's own handwritten handoff prompt for the CS project: a plausible reconstruction is worse than a flagged gap, because JD may act on it without re-verifying.
- **Source material vs working artifacts.** Also from JD's handwritten prompt: in an 85-attachment thread, the receiving thread needs to know which attachments are authoritative references worth consulting again (standards docs, CEDs, contracts) versus disposable working captures.
- **Context Snapshot as JD-only.** Message, attachment, and token counts help JD judge when a thread is heavy enough to fork, but are noise in the destination thread. The truncation-honesty rule (visible-context counts are floors, never corrections to JD's own counts) came from the CS thread correctly noticing it could only see 23 of a known 85 attachments because early content had aged out of its context window.

### Usage notes

- Strip the Context Snapshot before pasting the block into the new thread.
- After pasting, visually confirm the `FORKTAG-` line survived verbatim. It is the one component that cannot be silently wrong.
- FF run proactively (30 to 40 turns) loses less in compression than FF run as a rescue at 300 turns.
- FF can be run for topic-pivot reasons well below any token threshold. Token savings and context refocus are both valid triggers.

---

## Prompt 2: RFF (retrieve from fork)

### Stored memory text (verbatim)

> "RFF" prefix: run in a forked thread to retrieve gaps from its source thread. Each invocation = fresh re-evaluation of the ENTIRE current thread as it now stands, not a rerun of the FF handoff. Gaps = items from the FF gap-check line plus anything since surfaced that is incomplete, estimated, or under-specified vs what the source thread likely holds (including topics first mentioned after a prior RFF pass). Don't re-surface items a prior RFF already resolved. Trailing text after RFF = explicit steer: open the output by restating the steer as understood, retrieve that first with sharpened queries, in addition to (not instead of) the general gap scan. Bare RFF = general scan only. Locate the source thread: conversation_search on the fork tag from the FF handoff; before trusting a match, verify the exact tag literally appears in the retrieved content. Expect index lag: a failed tag search on a recent source thread is normal, not an error -- say so, fall back to the FF handoff's keywords/URL, or to a generated retrieval prompt. Per gap item: direct retrieval (read_conversation) only when confident of locating it; for anything vague or likely outside that thread's content, don't guess -- generate a targeted retrieval prompt instead. Mixing is fine (retrieve confident items, prompt for the rest). Generated retrieval prompts must: include the fork tag so the source thread knows which lineage is asking; instruct the source thread to answer "no record" rather than plausibly reconstruct; phrase items as specific questions/search terms, priority order, most valuable first. Direct-retrieval answers: always cite the source thread's link alongside, and present retrieved content ready to paste/act on, clearly separated from Claude's own confidence/sourcing commentary. Intended for long-running, information-dense source threads (extended negotiations, research orchestration) where one FF summary can't carry everything.

### Design rationale

- **Fresh re-evaluation per invocation.** JD's stated requirement: if a topic first arises mid-thread after the initial RFF pass, a later RFF must pick it up as a new gap. RFF is a re-derivation from the live transcript each time, not a tracked state machine. This is a known limitation, accepted.
- **Per-item confidence gating.** Direct retrieval on a vague reference risks a confident-sounding wrong answer, which is worse than no answer. Mixing modes within one pass (retrieve the specific, prompt for the vague) was chosen over all-or-nothing.
- **Index lag as expected behavior.** Empirically established in the design thread: a conversation does not appear in recent_chats or conversation_search while live, and lag persists across browser switches, device switches, and viewing other chats. First-attempt tag-search failure on a recently-forked source thread is the normal case, not a malfunction, and the instruction says so to prevent misdiagnosis.
- **Anti-hallucination guard in generated prompts.** The "no record over reconstruction" rule initially existed only in FF. The round-trip path (RFF generates prompt, JD pastes into source thread) lacked it, meaning the source thread could plausibly reconstruct answers. Now every generated retrieval prompt carries the guard.
- **Fork tag inside generated prompts.** So the source thread knows which handoff lineage is asking, and traceability is preserved across the round trip.

### Usage notes

- Steered form: `RFF <topic or question>`, e.g. `RFF the de17804 commit scope`. The steer is retrieved first; the general scan still runs.
- If RFF returns a generated prompt rather than answers, paste it into the source thread, collect answers, relay back. This is the expected path shortly after a fork.
- Share-button links do not work as retrieval identifiers. See Known Limitations.

---

## Prompt 3: FFD (delta handoff)

### Stored memory text (verbatim)

> "FFD" prefix (also "FF-delta"): delta handoff pass, run in a SOURCE thread where a prior FF/FFD handoff already exists. MANDATORY FIRST LINE, same rule as FF: the literal fork tag on its own line -- reuse the exact tag from any prior FF/FFD pass in this thread (never generate a second tag for one source thread); if none exists anywhere in the thread, generate one per FF format and flag it as this thread's first tag. Missing tag line = nonconforming output, fix in the same turn. Content: only what's new or was missed since the prior handoff -- newly surfaced risks/unknowns, facts verified or corrected since, decisions made since, new attachments, and status of previously open items (resolved / still open / now moot). Don't repeat covered material unless brief restatement is needed for the new information to make sense. State which prior passes this delta supplements (e.g. "supplements the initial FF and first delta") so the receiving thread knows reading order and supersession. Same fidelity rules as FF: bare FFD = full fidelity on new material, no unrequested pruning; pruning only via trailing steering text; separate verified facts from open/unconfirmed; "no record" over plausible reconstruction. End with an updated Context Snapshot (JD-only, never pasted forward), same content and floor-not-total caveats as FF's.

### Design rationale

- **Origin.** FFD was formalized after JD improvised a delta request in the CS orchestration thread ("you already provided a hand-off pass; now provide anything you may have missed") and the output, while good on substance, lacked a fork tag and an updated snapshot. The improvisation proved the pattern was needed; the gaps proved it needed a spec.
- **Single tag per source thread.** Multiple tags for one source thread would fragment RFF's search identity. FFD always reuses the existing tag.
- **Supersession pointer.** The CS thread accumulated an initial handoff, two deltas, and a consolidated canonical version. Without explicit "this supplements X and Y" statements, a receiving thread cannot know the reading order or which document supersedes which. This is the single strongest argument for the v2 architecture below.

### Usage notes

- Run FFD in the source thread, not the forked thread.
- Typical trigger: the source thread continued accumulating information after the first handoff was already pasted forward.

---

## Known limitations (empirically established, August 2026)

1. **Live-thread index lag.** A conversation is not retrievable via recent_chats or conversation_search while it is the active session. Lag persists across viewing other chats, switching browsers, and switching devices. The precise trigger and delay are unknown; assume a just-forked source thread is not yet searchable.
2. **Claude cannot self-locate.** No tool returns the live conversation's own URL, title, or ID from inside it. URL capture depends on recent_chats succeeding later, or JD supplying it.
3. **Share links are a different ID namespace.** A claude.ai/share/ UUID is a snapshot resource ID, not the conversation ID; read_conversation cannot use it. Confirmed by direct test. Do not use the Share button for retrieval purposes.
4. **Attachment aging.** In long threads, early attachments and content age out of the visible context window. A thread's self-count of its own attachments is a floor. FF and FFD snapshots must not present visible-context counts as corrections to JD's own counts.
5. **Compliance is probabilistic.** The system's correctness depends on an LLM following long prose instructions. Measured failure rate before hardening: two deviations in three FF runs (structure skipped; tag rendered as narrative). Hardening (mandatory first line, self-check, anti-anchoring clause) reduces but does not eliminate this. Verify the tag on every fork.
6. **Token estimates are floors.** System prompt, tool definitions, memory content, and image/PDF overhead are invisible from inside a conversation. Claude.ai's usage-bar metering, including whether prompt-cache discounts apply to it, is not publicly documented.

---

## Planned evolution: doc-backed state (v2 architecture)

### The core change

v1 stores canonical state in conversation transcripts, which are the most fragile store available: index lag, no self-reference, unusable share IDs, content aging out. v2 moves the handoff out of conversations entirely and into a durable file that any thread can read and any FFD pass can edit in place.

### What this removes

Not the handoff itself. FF still has to do the hard part, which is deciding what matters and writing it down faithfully. What it removes is the transport layer, which is where every observed failure in the v1 design cycle actually occurred.

- **Fork tag search.** No conversation_search, no index lag, no verifying a tag survived a paste. The file has a stable path.
- **Self-location.** Irrelevant. Nothing needs the thread's URL because the handoff no longer lives in a thread.
- **Manual steps.** No copy, no strip-the-snapshot, no paste, no verify.
- **Append-only delta chains.** The largest gain. In v1, FFD produces a second document supplementing the first, with supersession pointers so a reader knows which to trust. The CS thread accumulated four such passes. With an editable file, FFD edits in place: superseded facts get corrected, resolved open questions move to resolved. One canonical document instead of a stack requiring reading order.

### What this does not remove

- **Compliance risk.** Claude still has to write a good handoff. The most-violated rule (the tag) disappears, so this improves, but does not vanish.
- **RFF's residual case.** If something was never captured in the file, the source thread still has to be searched, with the same index lag. RFF's scope shrinks substantially but not to zero. The fork tag survives as a demoted fallback for exactly this case.
- **Token cost.** Reading the file into a new thread costs the same as pasting it; a tool result persists in context exactly like pasted text. The savings were always in abandoning the old thread, never in how the handoff traveled. v2 buys reliability and single-source-of-truth, not tokens.

### Bonus capability

Source-material attachments can live in the store alongside the handoff. The AP CED PDF sitting in the repo means a new thread reads it from there rather than JD re-attaching it. This partially solves the "recommended verbatim re-attachments" problem, which in v1 is pure manual labor.

### Store options

**GitHub (preferred).** `create_or_update_file` performs true in-place updates. Updating an existing file requires its blob SHA, which `get_file_contents` returns, so the round trip is read then write. Advantages over the alternatives: real version history with diffs (you can see exactly what each FFD pass changed), native Markdown, per-repo scoped MCP connector matching JD's minimum-scope credential preference, portable and not locked into a SaaS document format, and the pattern is already proven in the CS course project where the repo is the state store and threads are disposable workers around it. Known risk: GitHub MCP push reliability was flagged as unconfirmed in that same project, with manual local commit and push as the working fallback.

**ClickUp (viable alternative).** `clickup_update_document_page` supports content updates with replace, append, and prepend modes, merging server-side without needing to read the page first. This is a clean primitive for the living-document pattern and requires no SHA handling. Weaker version history than git, and content lives in a SaaS format rather than portable Markdown files.

**Google Drive (not recommended as primary).** Drive's `update_file` only modifies metadata (title, parent folder). There is no content-update tool available. Every FFD pass would create a new file version, reproducing the supersession-chain problem v2 exists to eliminate. Usable as a write-once archive for finished handoffs, not as a living document store.

### The canonicality rule (new, required)

Once state lives outside the thread, the file and the thread can disagree. Default rule: **the file is canonical for everything up to its last update; the live thread is canonical for anything since.** Without this stated explicitly in the rewritten prompts, a future thread will silently pick one and may pick wrong.

### Steps to implement

1. **Verify the primitive.** Confirm the full round trip works: create, read back, update in place, confirm history. See the Beta Test Brief above.
2. **Pilot on one project.** The CS course is the natural candidate: it is mid-fork and already has a canonical handoff written. Convert the existing document into the store rather than generating a new one.
3. **Settle conventions.** Where handoff files live (one central repo versus per-project), a naming convention predictable enough that a new thread can find the file by search without being given a path, and whether the document structure stays as today's FF sections or gets reshaped for in-place editing. Sections edited repeatedly, such as open questions, may warrant separate files.
4. **Define the canonicality rule** in the prompts, per above.
5. **Rewrite the three prompts.** FF becomes "write or update the handoff file, return the path or link." RFF becomes "read the file first, search the source thread only for what the file lacks." FFD becomes an in-place edit rather than a new output. The fork tag is demoted to a fallback identifier.
6. **Update this document to v3.**

### Access scope note

The v2 architecture puts GitHub or ClickUp tool access into threads that would otherwise not need it, including personal ones. Narrower alternative if that matters: scope the file-backed workflow to client and project work only, and retain the v1 paste-block version for personal threads. Flagged per JD's standing preference on permission scope.

---

## Related conventions

- Fork tag format: `FORKTAG-<short word/client hint>-<6 random alphanumerics>`. One tag per source thread, ever.
- The tag must exist as literal text in both the source thread (in the FF or FFD output) and the forked thread (in the pasted handoff), exactly two conversations.
- Context Snapshot is never pasted forward.
- House style applies to all outputs: no emojis, no em dashes, minimal horizontal rules.

---

## Changelog

- **v2.0 (2026-08-21):** Added Beta Test Brief for handoff to a testing thread. Added full "Planned evolution: doc-backed state" section covering what the architecture removes and does not remove, store option comparison with verified tool capabilities (GitHub in-place update confirmed via create_or_update_file with SHA; ClickUp confirmed via clickup_update_document_page; Google Drive confirmed as metadata-only and therefore unsuitable as primary), the new canonicality rule, implementation steps, and an access-scope note. Corrected the v1 architectural note, which had pointed at Google Drive as the upgrade target before tool capabilities were verified. No changes to the three memory prompt texts, which remain as applied on 2026-08-17.
- **v1.0 (2026-08-17):** Initial documentation. Captured the compressed memory entries as applied on that date, following the design and hardening cycle in the originating thread (peak-usage analysis, token economics, fork system design, live CS-thread testing, hardening, compression).
