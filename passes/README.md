# passes/ — committed pass artifacts

**Last updated: 260832-3** (date-stamped, format yymmdd-iteration)

Every delegated intake or reconcile pass writes two files here and they
are **committed alongside the change they describe**:

```
<stamp>_<short-name>.diff
<stamp>_<short-name>_close-out.md
```

**Why they live in the repo.** Two reasons, both practical:

1. **The reasoning behind every pass stays permanently recoverable** from
   git history, next to the change it produced — not stranded in a chat
   thread that will eventually be archived or hit a limit.
2. **Orchestration reads them from a fresh clone** rather than needing
   them uploaded as chat attachments. Attachments are finite; this
   workflow no longer spends them per batch.

⚠️ **The `.diff` is the diff as applied**, so a committed diff file
describes the very commit it travels in. Self-referential, but accurate.

⛔ **A close-out that reports only successes is under-reporting.** It
should record what was declined and why, what was checked and came back
empty, and anything the pass could not resolve.

⚠️ **Not everything in this folder is a pass artifact in the strict
sense.** Reference material JD drops in for orchestration's own benefit
(e.g. process documentation) can live here too without needing a
`PROJECT_STATE.md` registry row — see `ORCHESTRATION.md` §4.

See `ORCHESTRATION.md` §4.
