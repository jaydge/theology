#!/usr/bin/env python3
"""
validate_project.py — mechanical cross-file integrity checks.

Run after every reconcile pass, before updating changelogs. Also wired as a
pre-commit hook in the private repo.

Catches the class of failure that produced the 260724-1 correction: stale
duplicated state, unresolved relative timestamps, numbering breaks, dangling
cross-references, and version drift between PROJECT_STATE.md and the corpus.

⚠️ THE DEFECT THIS VERSION FIXES (260725-1)
-------------------------------------------
C1 and C6 used to glob 'SRC_Discord_*.md' in the WORKING DIRECTORY. In the
actual repo those archives live under src/. The globs matched nothing, both
checks ran ZERO times, and the report printed "0 errors" — including the one
check that guards against the July 2026 relative-timestamp bug. A pre-commit
hook made every commit since then look verified.

Three structural changes prevent a recurrence:
  1. The expected file set is DERIVED FROM THE PROJECT_STATE.md §4 DOCUMENT
     REGISTRY (explicit paths), never from a directory glob.
  2. A registered file that is not at its registered path is SEARCHED FOR
     RECURSIVELY, and is an ERROR only if it is nowhere in the tree.
  3. A COVERAGE ASSERTION fails the run if any check contributes zero results.
     A skipped check must never look like a clean pass.

Usage:  python3 validate_project.py [ROOT]
        ROOT defaults to the directory containing this script.
Exit:   0 = clean, 1 = errors found (including zero-coverage)
"""
import re, sys, hashlib, os
from collections import OrderedDict

ERR, WARN, OK = [], [], []
def err(m):  ERR.append(m)
def warn(m): WARN.append(m)
def ok(m):   OK.append(m)

# ---------------------------------------------------------------- COVERAGE
# Every check records how many files it actually examined. A check that
# examines zero files is a FAILURE, not a pass. This is the assertion that
# would have caught the C1/C6 silent skip on the day it was introduced.
COVERAGE = OrderedDict()
CHECK_NAMES = {
    'C0': 'registry resolution',
    'C1': 'relative timestamps in archives',
    'C2': 'source-tag numbering',
    'C3': 'version stamps vs registry',
    'C4': 'stale answered-question status',
    'C5': 'volatile-state duplication',
    'C6': 'archive hash integrity',
    'C7': 'relay-clean firewall (WARN-only, suspended)',
    'C8': 'dangling question-ID cross-references',
    'C9': 'do-not-deploy consistency',
    'C10': 'section 15 staleness',
    'C11': 'outline-vs-findings drift',
}
# Checks that are allowed to see zero files without failing the run, and why.
COVERAGE_EXEMPT = {}

def seen(check, path):
    COVERAGE.setdefault(check, [])
    if path not in COVERAGE[check]:
        COVERAGE[check].append(path)

ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else \
       os.path.dirname(os.path.abspath(__file__)) or os.getcwd()

def read(p):
    try:
        with open(p, encoding='utf-8') as fh:
            return fh.read()
    except (OSError, UnicodeDecodeError):
        return None

STATE_PATH = os.path.join(ROOT, 'PROJECT_STATE.md')
STATE = read(STATE_PATH)
if STATE is None:
    print(f"FATAL: PROJECT_STATE.md not found under {ROOT}.")
    print("It is the source of truth and the source of the expected file set;")
    print("nothing else can be checked without it.")
    print("Pass a root path explicitly:  python3 validate_project.py /path/to/repo")
    sys.exit(1)

# ================================================================ CHECK 0
# Derive the expected file set from the PROJECT_STATE §4 registry, then
# RESOLVE each registered path against the real tree.
def registry_rows():
    """[(path, version_cell), ...] from the §4 DOCUMENT REGISTRY table."""
    m = re.search(r'^##\s*4\.\s*DOCUMENT REGISTRY(.*?)(?=^##\s|\Z)',
                  STATE, re.M | re.S)
    if not m:
        return []
    rows = []
    for line in m.group(1).splitlines():
        if not line.strip().startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 2:
            continue
        pm = re.match(r'^`([^`]+)`$', cells[0])
        if not pm:
            continue                      # header row, separator, or prose
        rows.append((pm.group(1), cells[1]))
    return rows

REGISTRY = registry_rows()
if not REGISTRY:
    err("[C0] Could not parse the §4 DOCUMENT REGISTRY table in PROJECT_STATE.md. "
        "Every check derives its file set from that table; without it this run "
        "is meaningless. Expected rows of the form: | `path/to/file.md` | version | ...")

def build_index(root):
    idx = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames
                       if d not in ('.git', 'node_modules', '__pycache__',
                                    '.venv', 'venv')]
        for fn in filenames:
            idx.setdefault(fn, []).append(os.path.join(dirpath, fn))
    return idx

INDEX = build_index(ROOT)

RESOLVED = {}     # registered path -> absolute path on disk
MISSING = []

for regpath, _ver in REGISTRY:
    seen('C0', regpath)
    exact = os.path.join(ROOT, regpath)
    if os.path.isfile(exact) and read(exact) is not None:
        RESOLVED[regpath] = exact
        ok(f"[C0] {regpath}: resolved at registered path")
        continue
    # Not where the registry says. Search the whole tree before failing.
    base = os.path.basename(regpath)
    hits = INDEX.get(base, [])
    if len(hits) == 1 and read(hits[0]) is not None:
        RESOLVED[regpath] = hits[0]
        rel = os.path.relpath(hits[0], ROOT)
        warn(f"[C0] {regpath}: NOT at its registered path; found at '{rel}' by "
             f"recursive search. The REGISTRY is wrong — fix PROJECT_STATE §4, "
             f"not the file.")
    elif len(hits) > 1:
        rels = [os.path.relpath(h, ROOT) for h in hits]
        err(f"[C0] {regpath}: AMBIGUOUS — {len(hits)} files named '{base}' in the "
            f"tree: {rels}. Cannot decide which is canonical. Disambiguate or "
            f"delete the duplicate.")
        MISSING.append(regpath)
    else:
        err(f"[C0] {regpath}: REGISTERED BUT MISSING OR UNREADABLE anywhere under "
            f"{ROOT}. Either the file was moved/deleted or the registry entry is "
            f"wrong. A registered file that cannot be read is an unchecked file.")
        MISSING.append(regpath)

def registered(pattern):
    """Resolved absolute paths whose registered path matches a regex."""
    return [(p, RESOLVED[p]) for p in RESOLVED if re.search(pattern, p)]

def get(regpath):
    return read(RESOLVED[regpath]) if regpath in RESOLVED else None

ARCHIVES = sorted(registered(r'SRC_Discord_[^/]*\.md$'))
CORPUS_NAMES = ['St_Francis_EMC_Distinctives.md', 'RJ_Final_Question_List.md',
                'RJ_Incense_Analysis.md', 'On_Incense_and_the_Altar.md',
                'Incense_Conversational_Outline.md']

def find_reg(basename):
    for p in RESOLVED:
        if os.path.basename(p) == basename:
            return p
    return None

DIST_KEY = find_reg('St_Francis_EMC_Distinctives.md')
QL_KEY   = find_reg('RJ_Final_Question_List.md')
OUT_KEY  = find_reg('Incense_Conversational_Outline.md')
MAN_KEY  = find_reg('SRC_Manifest.md')

DIST = get(DIST_KEY) or ''
QL   = get(QL_KEY) or ''

if not ARCHIVES:
    err("[C0] NO SRC_Discord_*.md ARCHIVES RESOLVED. This is the exact condition "
        "that made C1 and C6 run zero times while the report read '0 errors'. "
        "Register the archives in PROJECT_STATE §4 by explicit path.")

# ================================================================ CHECK 1
# Relative timestamps must never survive intake in a raw archive.
# This is the bug that cost two weeks in July 2026.
for regpath, abspath in ARCHIVES:
    s = read(abspath)
    if s is None:
        err(f"[C1] {regpath}: unreadable")
        continue
    seen('C1', regpath)
    hits = re.findall(r'^###\s+(Yesterday|Today)\s+at\s+.*$', s, re.M)
    loose = re.findall(r'\b(Yesterday|Today)\s+at\s+\d', s)
    if hits:
        err(f"[C1] {regpath}: {len(hits)} UNRESOLVED relative timestamp(s) in "
            f"message headers. Resolve to absolute dates against the handover "
            f"date, IN THIS FILE, before logging anything from it.")
    elif loose:
        warn(f"[C1] {regpath}: {len(loose)} relative timestamp(s) outside message "
             f"headers ('Yesterday at …'). Not caught by the header rule; check "
             f"whether they are quoted text or unresolved captures.")
    else:
        ok(f"[C1] {regpath}: no unresolved relative timestamps")

# ================================================================ CHECK 2
# Source-tag numbering: unbroken, no duplicates. Suffixed amendments (DQ-7a)
# are legal and must attach to an EXISTING parent number.
if DIST:
    seen('C2', DIST_KEY)
    for prefix in ['DQ', 'IP']:
        tags = re.findall(rf'^\*\*{prefix}-(\d+)([a-z]?)\.\*\*', DIST, re.M)
        if not tags:
            warn(f"[C2] {prefix}: no ledger-format entries found in "
                 f"{os.path.basename(DIST_KEY)}. Expected '**{prefix}-N.**'.")
            continue
        plain_list = [x for x, s in tags if not s]
        plain = sorted({int(n) for n in plain_list})
        dupes = sorted({int(n) for n in plain_list if plain_list.count(n) > 1})
        if dupes:
            err(f"[C2] {prefix}: duplicate finding number(s) {dupes}")
        gaps = [n for n in range(1, max(plain) + 1) if n not in plain]
        hard = [n for n in gaps if not re.search(rf'\b{prefix}-{n}\b', DIST)]
        soft = [n for n in gaps if n not in hard]
        if hard:
            err(f"[C2] {prefix}: numbering NOT unbroken; {hard} missing entirely")
        if soft:
            warn(f"[C2] {prefix}: {soft} exist in the document but not in ledger "
                 f"(**{prefix}-N.**) format. Cosmetic; safe to defer.")
        if not gaps:
            ok(f"[C2] {prefix}-1..{max(plain)} unbroken, no duplicates")
        for n, s in tags:
            if s and int(n) not in plain:
                err(f"[C2] {prefix}-{n}{s} is an amendment with no parent "
                    f"{prefix}-{n}. Amendments take the PARENT's number "
                    f"(PROJECT_STATE §5 rule 2).")

    # NOTE (260725-1): an automated "one tag, one finding" collision detector was
    # built here and REMOVED. It cannot distinguish a genuine collision (IP-4
    # heading a sacraments ledger entry while also tagging an incense finding)
    # from this corpus's normal and correct anchor style, where a section block
    # opens "[Stated + Analysis — IP-N (session ...)]" to point at its ledger
    # entry. It flagged IP-2, IP-3 and IP-5 as collisions when they were fine.
    # A check that cries wolf teaches people to ignore the validator, which costs
    # more than the collisions it would catch. The "one tag, one finding" rule
    # stays in PROJECT_STATE §5 rule 6 as a HUMAN discipline, enforced at review.

# ================================================================ CHECK 3
# Version stamps in each document must match the PROJECT_STATE registry.
def doc_version(s):
    m = re.search(r'\*\*Last updated:\s*([^*]+?)\*\*', s or '')
    return m.group(1).strip() if m else None

for regpath, ver_cell in REGISTRY:
    if regpath not in RESOLVED:
        continue
    if os.path.basename(regpath).startswith('SRC_Discord_'):
        continue                      # archives are versioned in the manifest
    seen('C3', regpath)
    s = read(RESOLVED[regpath])
    dv = doc_version(s)
    rv = ver_cell
    if re.search(r'unstamped|n/?a', rv, re.I):
        warn(f"[C3] {regpath}: registry marks it unstamped; no version to check. "
             f"Add a '**Last updated:**' line so this file stops being invisible.")
    elif re.search(r'STALE', rv, re.I):
        warn(f"[C3] {regpath}: registry flags this file STALE. Version comparison "
             f"skipped by design; the flag is the finding. Fix the content.")
    elif dv is None:
        warn(f"[C3] {regpath}: no parseable 'Last updated' stamp; registry says "
             f"'{rv}'")
    else:
        rtok = re.search(r'\d{6}-\d', rv)
        dtok = re.search(r'\d{6}-\d', dv)
        if rtok and dtok and rtok.group(0) == dtok.group(0):
            ok(f"[C3] {regpath}: version agrees with registry ({dv})")
        else:
            err(f"[C3] {regpath}: VERSION DRIFT — registry says '{rv}', document "
                f"says '{dv}'")

# ================================================================ CHECK 4
# Any question PROJECT_STATE marks answered/retired must not be described
# as awaiting/unposted anywhere in the corpus without a supersede marker.
ANSWERED = re.findall(r'\*\*(DQ-\d+[a-z]?)\*\*[^|]*\|\s*✅', STATE)
STALE_PAT = re.compile(r'(awaiting reply|still awaiting|unposted|outstanding)', re.I)
SUPERSEDE_PAT = re.compile(
    r'(SUPERSEDED|CORRECTED|retained for trail|do NOT bump|DOWNGRADED|RETIRED|'
    r'moot|⛔|was wrong|FALSE)', re.I)

for name in ['St_Francis_EMC_Distinctives.md', 'RJ_Final_Question_List.md',
             'RJ_Incense_Analysis.md']:
    k = find_reg(name)
    if not k:
        continue
    s = get(k)
    if not s:
        continue
    seen('C4', k)
    bad = 0
    for qid in set(ANSWERED):
        for m in re.finditer(re.escape(qid), s):
            window = s[max(0, m.start() - 400): m.end() + 400]
            if STALE_PAT.search(window) and not SUPERSEDE_PAT.search(window):
                bad += 1
    if bad:
        warn(f"[C4] {k}: {bad} passage(s) describe an ANSWERED question as pending "
             f"with no supersede marker nearby. Review manually.")
    else:
        ok(f"[C4] {k}: no unmarked stale-status passages for answered questions")

# ================================================================ CHECK 5
# Volatile-state duplication pressure. The more places restate live state,
# the higher the chance of the July 2026 failure.
tot = 0
for regpath in sorted(RESOLVED):
    base = os.path.basename(regpath)
    if base == 'PROJECT_STATE.md' or base.startswith('SRC_'):
        continue
    if not base.endswith('.md'):
        continue
    seen('C5', regpath)
    s = get(regpath) or ''
    n = len(re.findall(r'awaiting reply|LIVE STATUS|STATUS:', s, re.I))
    tot += n
    if n > 6:
        warn(f"[C5] {regpath}: {n} volatile-state assertions. Consider replacing "
             f"with a pointer to PROJECT_STATE.")
ok(f"[C5] total volatile-state assertions outside PROJECT_STATE: {tot}")

# ================================================================ CHECK 6
# Archive hashes must match SRC_Manifest.md.
man = get(MAN_KEY) or ''
if not man:
    err("[C6] SRC_Manifest.md did not resolve; archive hashes cannot be checked.")
for regpath, abspath in ARCHIVES:
    seen('C6', regpath)
    try:
        with open(abspath, 'rb') as fh:
            h = hashlib.sha256(fh.read()).hexdigest()
    except OSError:
        err(f"[C6] {regpath}: unreadable for hashing")
        continue
    base = os.path.basename(regpath)
    if f"`{base}`" not in man:
        err(f"[C6] {regpath}: not registered in SRC_Manifest.md")
    elif h in man:
        ok(f"[C6] {regpath}: hash matches manifest")
    else:
        err(f"[C6] {regpath}: HASH MISMATCH — file changed since the manifest was "
            f"written. Update manifest to {h[:16]}…")

# ================================================================ CHECK 7
# Relay-clean firewall.
# ⚠️ DOWNGRADED TO WARN 260725-1. All documents are INTERNAL ONLY and external
# sharing is SUSPENDED (PROJECT_STATE §0). The discipline is NOT deleted: the
# check still runs and still reports, so the cost of restoring relay-clean stays
# visible. TO RESTORE: change warn(...) back to err(...) here and flip the CLASS
# lines in the affected files.
RELAY_FILES = ['On_Incense_and_the_Altar.md', 'Incense_Conversational_Outline.md']
for name in RELAY_FILES:
    k = find_reg(name)
    if not k:
        continue
    relay = get(k)
    if not relay:
        continue
    seen('C7', k)
    body = relay
    # Scan the BODY only. The purpose header, the metadata block and the
    # changelog legitimately DESCRIBE the firewall (and are marked 'strip from
    # handout copies'), so they would otherwise self-trip.
    for cut in ['<!-- END PURPOSE HEADER -->', '<!-- END METADATA BLOCK -->',
                '## Changelog']:
        if cut in body:
            body = body.split(cut)[-1] if cut.endswith('-->') else body.split(cut)[0]
    terms = [r'\blevers?\b', r'\bBucket [ABCD]\b', r'\bdo-not-deploy\b',
             r'\bfunnel\b', r'\bgotcha\b', r'\bbackstage\b', r'\bcrux question\b']
    leaks = [t for t in terms if re.search(t, body, re.I)]
    if re.search(r'\bDO NOT SHARE\b', body):
        leaks.append('DO NOT SHARE')
    if leaks:
        warn(f"[C7] {k}: backstage vocabulary present -> {leaks}. Relay-clean is "
             f"SUSPENDED (recoverable), so this does not fail the run — but each "
             f"item here is cleanup owed before the file can be shared again.")
    else:
        ok(f"[C7] {k}: relay-clean firewall intact (class suspended; no cleanup owed)")

# ================================================================ CHECK 8
# Dangling cross-references: question IDs cited in the distinctives but
# absent from the question list. QA-* tags are question-list LABELS
# (PROJECT_STATE §5 rule 5) and must exist there before being cited.
if DIST and QL:
    seen('C8', DIST_KEY)
    seen('C8', QL_KEY)
    CHANGELOG_MARK = re.compile(r'^\s*(v?\d[\w.]*\s*[-–—]|\d{6}-\d)', re.M)
    cited = {}
    for m in re.finditer(r'\bQA-[A-Za-z][A-Za-z0-9]*\b', DIST):
        line_start = DIST.rfind('\n', 0, m.start()) + 1
        line_end = DIST.find('\n', m.end())
        line = DIST[line_start: line_end if line_end != -1 else len(DIST)]
        if CHANGELOG_MARK.match(line):
            continue                    # historical changelog: never altered
        cited.setdefault(m.group(0), 0)
        cited[m.group(0)] += 1
    dangling = sorted(t for t in cited if t not in QL)
    if dangling:
        err(f"[C8] DANGLING QUESTION IDs cited in "
            f"{os.path.basename(DIST_KEY)} but absent from "
            f"{os.path.basename(QL_KEY)}: {dangling}. "
            f"A citation that resolves to nothing is worse than no citation — it "
            f"reads as verified. Fix whichever file is wrong.")
    else:
        ok(f"[C8] all {len(cited)} QA-* citations resolve in the question list")
    # Reverse direction, informational.
    ql_tags = set(re.findall(r'\bQA-[A-Za-z][A-Za-z0-9]*\b', QL))
    orphans = sorted(ql_tags - set(cited))
    if orphans:
        warn(f"[C8] QA tag(s) defined in the question list but never cited from "
             f"the distinctives: {orphans}. Harmless, but check the tag is doing "
             f"work.")

# ================================================================ CHECK 9
# Do-not-deploy consistency: anything on the PROJECT_STATE register that
# still reads as deployable in the question list.
reg_m = re.search(r'DO-NOT-DEPLOY REGISTER(.*?)(?=^##\s)', STATE, re.M | re.S)
if reg_m and QL:
    seen('C9', QL_KEY)
    RETIRE_MARK = re.compile(
        r'(RETIRED|DO NOT DEPLOY|DO-NOT-DEPLOY|do not deploy|ASKED AND ANSWERED|'
        r'⛔|not a lever|common ground)', re.I)
    pointers = []
    for line in reg_m.group(1).splitlines():
        if not line.strip().startswith('-'):
            continue
        for item in re.findall(r'\[→ item (\d+[a-z]?)\]', line):
            label = re.sub(r'\s+', ' ', re.sub(r'[*`⚠️]', '', line)).strip(' -')
            pointers.append((item, label[:70]))
    if not pointers:
        warn("[C9] No '[→ item N]' pointers found in the do-not-deploy register. "
             "The check cannot verify entries it cannot map. Add pointers.")
    for item, label in pointers:
        m = re.search(rf'^###\s+{re.escape(item)}\.\s(.*?)(?=^###\s|\Z)',
                      QL, re.M | re.S)
        if not m:
            err(f"[C9] register entry '{label}' points to question-list item "
                f"{item}, which does not exist. Fix the pointer or the item.")
            continue
        section = m.group(0)
        head = section.split('\n')[0]
        if RETIRE_MARK.search(head) or RETIRE_MARK.search(section[:1200]):
            ok(f"[C9] item {item}: carries a retirement marker, consistent with "
               f"the register")
        else:
            warn(f"[C9] ⚠️ item {item} is on the DO-NOT-DEPLOY register "
                 f"('{label}') but reads as DEPLOYABLE in the question list — no "
                 f"retirement marker in its heading or opening. Either mark it or "
                 f"remove it from the register. Do not leave it ambiguous.")

# ================================================================ CHECK 10
# §15 staleness. Two independent signals:
#   (a) findings whose analysis says "credit it / §15" but which §15 never got;
#   (b) lag between the newest finding and the newest finding §15 cites.
if DIST:
    seen('C10', DIST_KEY)
    s15 = re.search(r'^##\s*15\.\s.*?(?=^##\s)', DIST, re.M | re.S)
    if not s15:
        err("[C10] §15 'Where He's Sound' not found in the distinctives. It is the "
            "corpus's only counterweight to the tensions sections; its absence is "
            "not a formatting issue.")
    else:
        body15 = s15.group(0)
        CREDIT = re.compile(r'(credit it|common ground|formulary-faithful|'
                            r'no lever here|Credit \(§15\)|see §15)', re.I)
        owed = []
        for m in re.finditer(r'^\*\*((?:DQ|IP)-\d+[a-z]?)\.\*\*', DIST, re.M):
            tag = m.group(1)
            # Bound the entry at the next ledger tag OR the next '## ' section
            # header, whichever comes first. Without the header bound the LAST
            # entry in a ledger bleeds into the following sections and inherits
            # their vocabulary — that bug made IP-11 look flagged when it wasn't.
            rest = DIST[m.end():]
            bounds = [x.start() for x in
                      [re.search(r'^\*\*(?:DQ|IP)-\d+[a-z]?\.\*\*', rest, re.M),
                       re.search(r'^##\s', rest, re.M)] if x]
            entry = DIST[m.start(): m.end() + (min(bounds) if bounds else 3000)]
            if CREDIT.search(entry) and tag not in body15:
                owed.append(tag)
        if owed:
            warn(f"[C10] ⚠️ §15 IS BEHIND. {len(owed)} finding(s) whose own "
                 f"analysis flags common ground are not credited in §15: "
                 f"{owed}. Noted in an analysis block is NOT logged in §15.")
        else:
            ok("[C10] every finding flagged as common ground is credited in §15")

        def maxnum(text, prefix):
            ns = [int(n) for n in re.findall(rf'\b{prefix}-(\d+)\b', text)]
            return max(ns) if ns else 0
        lag = maxnum(DIST, 'DQ') - maxnum(body15, 'DQ')
        if maxnum(body15, 'DQ') == 0:
            warn("[C10] ⚠️ §15 cites NO DQ findings at all, while the DQ ledger "
                 f"runs to DQ-{maxnum(DIST, 'DQ')}. The tensions sections have "
                 f"grown weekly and §15 has not moved. A source-of-truth document "
                 f"that only accumulates tensions is biased by construction.")
        elif lag > 4:
            warn(f"[C10] §15's newest DQ citation is {lag} findings behind the "
                 f"ledger. Sweep the interval for creditable material.")
        else:
            ok(f"[C10] §15 is within {lag} finding(s) of the DQ ledger head")

# ================================================================ CHECK 11
# Outline-vs-findings drift. The outline carries a derivation pointer naming
# its sources and the finding it was last checked against. If the ledger has
# moved past that point, the outline is unverified — REPORT, never rewrite.
if OUT_KEY and DIST:
    out = get(OUT_KEY) or ''
    seen('C11', OUT_KEY)
    seen('C11', DIST_KEY)
    dpat = re.search(r'DERIVATION[^\n]*?CHECKED-AGAINST:\s*((?:DQ|IP)-\d+[a-z]?)'
                     r'\s*@\s*(\d{6}-\d)', out)
    if not dpat:
        err("[C11] Incense_Conversational_Outline.md has no parseable derivation "
            "pointer. Expected a line containing: DERIVATION: … CHECKED-AGAINST: "
            "<finding> @ <yymmdd-n>. Without it, drift against the findings "
            "cannot be detected and the outline silently ages.")
    else:
        checked_tag, checked_stamp = dpat.group(1), dpat.group(2)
        cnum = int(re.search(r'\d+', checked_tag).group(0))
        dq_max = max([int(n) for n in re.findall(r'\bDQ-(\d+)\b', DIST)] or [0])
        if checked_tag.startswith('DQ') and dq_max > cnum:
            warn(f"[C11] outline last checked against {checked_tag} "
                 f"({checked_stamp}); the DQ ledger now runs to DQ-{dq_max}. "
                 f"{dq_max - cnum} finding(s) unreviewed against the outline's "
                 f"logical flow. REPORT drift; do not rewrite JD's reasoning "
                 f"without asking.")
        else:
            ok(f"[C11] outline derivation pointer current "
               f"({checked_tag} @ {checked_stamp})")
        for src in ['RJ_Incense_Analysis.md', 'St_Francis_EMC_Distinctives.md']:
            if src not in out:
                warn(f"[C11] outline derivation pointer does not name {src} as a "
                     f"source. Name every document it derives from.")

# ================================================================ COVERAGE
# THE ASSERTION. A check that examined zero files is a failure, full stop.
zero = []
for cid in CHECK_NAMES:
    if cid in COVERAGE_EXEMPT:
        continue
    if not COVERAGE.get(cid):
        zero.append(cid)
for cid in zero:
    err(f"[COVERAGE] {cid} ({CHECK_NAMES[cid]}) EXAMINED ZERO FILES. "
        f"A skipped check is not a passing check. This run cannot be trusted for "
        f"{cid}. Cause is almost always a registry path that no longer resolves — "
        f"read the [C0] lines above.")

# ---------------------------------------------------------------- report
print("=" * 72)
print(f"PROJECT INTEGRITY VALIDATION   root: {ROOT}")
print("=" * 72)
for m in OK:   print("  ok   ", m)
for m in WARN: print("  WARN ", m)
for m in ERR:  print("  ERROR", m)

print("-" * 72)
print("COVERAGE SUMMARY — files examined per check")
print("-" * 72)
print(f"  {'check':<6} {'files':>5}  {'name':<44} status")
for cid, name in CHECK_NAMES.items():
    files = COVERAGE.get(cid, [])
    status = "OK" if files else ("exempt" if cid in COVERAGE_EXEMPT
                                 else "⚠️  ZERO — RUN NOT TRUSTWORTHY")
    print(f"  {cid:<6} {len(files):>5}  {name:<44} {status}")
    for f in files:
        print(f"         └─ {f}")

print("-" * 72)
print(f"{len(OK)} ok · {len(WARN)} warnings · {len(ERR)} errors")
if zero:
    print(f"⚠️  {len(zero)} check(s) with ZERO coverage: {zero}")
print("Read the coverage summary before trusting the error count.")
sys.exit(1 if ERR else 0)
