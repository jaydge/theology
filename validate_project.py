#!/usr/bin/env python3
"""
validate_project.py — mechanical cross-file integrity checks.

Run after every reconcile pass, before updating changelogs.
Catches the exact class of failure that produced the 260724-1 correction:
stale duplicated state, unresolved relative timestamps, numbering breaks,
and version drift between PROJECT_STATE.md and the corpus.

Usage:  python3 validate_project.py
Exit:   0 = clean, 1 = errors found
"""
import re, sys, glob, hashlib, os

ERR, WARN, OK = [], [], []
def err(m):  ERR.append(m)
def warn(m): WARN.append(m)
def ok(m):   OK.append(m)

def read(p):
    return open(p, encoding='utf-8').read() if os.path.exists(p) else None

STATE = read('PROJECT_STATE.md')
if STATE is None:
    print("FATAL: PROJECT_STATE.md not found. It is the source of truth; nothing else can be checked without it.")
    sys.exit(1)

# ---------------------------------------------------------------- CHECK 1
# Relative timestamps must never survive intake in a raw archive.
# This is the bug that cost two weeks in July 2026.
for f in sorted(glob.glob('SRC_Discord_*.md')):
    hits = re.findall(r'^###\s+(Yesterday|Today)\s+at\s+.*$', read(f), re.M)
    if hits:
        err(f"[C1] {f}: {len(hits)} UNRESOLVED relative timestamp(s). "
            f"Resolve to absolute dates against the handover date BEFORE logging anything from this file.")
    else:
        ok(f"[C1] {f}: no unresolved relative timestamps")

# ---------------------------------------------------------------- CHECK 2
# Source-tag numbering: unbroken, no duplicates. Suffixed amendments (DQ-7a)
# are legal and must attach to an EXISTING parent number.
corpus = read('St_Francis_EMC_Distinctives.md') or ''
for prefix in ['DQ', 'IP']:
    tags = re.findall(rf'^\*\*{prefix}-(\d+)([a-z]?)\.\*\*', corpus, re.M)
    if not tags:
        continue
    plain = sorted({int(n) for n, s in tags if not s})
    dupes = [n for n in plain if [x for x, s in tags if not s].count(str(n)) > 1]
    if dupes:
        err(f"[C2] {prefix}: duplicate finding number(s) {dupes}")
    gaps = [n for n in range(1, max(plain) + 1) if n not in plain]
    # A number present in the document but not in ledger format is a formatting
    # inconsistency, not a numbering break.
    hard = [n for n in gaps if not re.search(rf'\b{prefix}-{n}\b', corpus)]
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
            err(f"[C2] {prefix}-{n}{s} is an amendment with no parent {prefix}-{n}. "
                f"Amendments take the PARENT's number (see PROJECT_STATE §5 rule 2).")

# ---------------------------------------------------------------- CHECK 3
# Version stamps in each document must match the PROJECT_STATE registry.
def registry_version(fname):
    m = re.search(rf'\|\s*`{re.escape(fname)}`\s*\|\s*([^|]+?)\s*\|', STATE)
    return m.group(1).strip() if m else None

def doc_version(path):
    s = read(path)
    if s is None: return None
    m = re.search(r'\*\*Last updated:\s*([^*]+?)\*\*', s)
    return m.group(1).strip() if m else None

for f in ['St_Francis_EMC_Distinctives.md', 'RJ_Final_Question_List.md',
          'RJ_Incense_Analysis.md', 'On_Incense_and_the_Altar.md',
          'Incense_Conversational_Outline.md']:
    rv, dv = registry_version(f), doc_version(f)
    if rv is None:
        warn(f"[C3] {f}: not listed in PROJECT_STATE document registry")
    elif dv is None:
        warn(f"[C3] {f}: no parseable 'Last updated' stamp; registry says {rv}")
    elif rv.split()[0].strip('()') not in dv and dv.split()[0] not in rv:
        err(f"[C3] {f}: VERSION DRIFT — registry says '{rv}', document says '{dv}'")
    else:
        ok(f"[C3] {f}: version agrees with registry ({dv})")

# ---------------------------------------------------------------- CHECK 4
# Any question PROJECT_STATE marks answered/retired must not be described
# as awaiting/unposted anywhere in the corpus without a supersede marker.
ANSWERED = re.findall(r'\*\*(DQ-\d+[a-z]?)\*\*[^|]*\|\s*✅', STATE)
STALE_PAT = re.compile(r'(awaiting reply|still awaiting|unposted|outstanding)', re.I)
SUPERSEDE_PAT = re.compile(r'(SUPERSEDED|CORRECTED|retained for trail|do NOT bump|DOWNGRADED|RETIRED|moot|⛔|was wrong|FALSE)', re.I)

for f in ['St_Francis_EMC_Distinctives.md', 'RJ_Final_Question_List.md', 'RJ_Incense_Analysis.md']:
    s = read(f)
    if not s: continue
    bad = 0
    for qid in set(ANSWERED):
        for m in re.finditer(re.escape(qid), s):
            window = s[max(0, m.start() - 400): m.end() + 400]
            if STALE_PAT.search(window) and not SUPERSEDE_PAT.search(window):
                bad += 1
    if bad:
        warn(f"[C4] {f}: {bad} passage(s) describe an ANSWERED question as pending "
             f"with no supersede marker nearby. Review manually.")
    else:
        ok(f"[C4] {f}: no unmarked stale-status passages for answered questions")

# ---------------------------------------------------------------- CHECK 5
# Volatile-state duplication pressure. Informational: the more places
# restate live state, the higher the chance of the July 2026 failure.
tot = 0
for f in sorted(glob.glob('*.md')):
    if f in ('PROJECT_STATE.md',) or f.startswith('SRC_'):
        continue
    s = read(f) or ''
    n = len(re.findall(r'awaiting reply|LIVE STATUS|STATUS:', s, re.I))
    tot += n
    if n > 6:
        warn(f"[C5] {f}: {n} volatile-state assertions. Consider replacing with a pointer to PROJECT_STATE.")
ok(f"[C5] total volatile-state assertions outside PROJECT_STATE: {tot}")

# ---------------------------------------------------------------- CHECK 6
# SRC file hashes must match SRC_Manifest.md.
man = read('SRC_Manifest.md') or ''
for f in sorted(glob.glob('SRC_Discord_*.md')):
    h = hashlib.sha256(open(f, 'rb').read()).hexdigest()
    if f"`{f}`" not in man:
        err(f"[C6] {f}: not registered in SRC_Manifest.md")
    elif h in man:
        ok(f"[C6] {f}: hash matches manifest")
    else:
        err(f"[C6] {f}: HASH MISMATCH — file changed since manifest was written. "
            f"Update manifest to {h[:16]}…")

# ---------------------------------------------------------------- CHECK 7
# Relay-clean firewall: the shareable document must not contain
# backstage vocabulary.
relay = read('On_Incense_and_the_Altar.md')
if relay:
    # Scan the BODY only: the purpose header and changelog legitimately *describe*
    # the firewall and would otherwise self-trip. Word boundaries prevent
    # "lever" matching inside "leverage".
    body = relay
    for cut in ['<!-- END PURPOSE HEADER -->', '## Changelog']:
        if cut in body:
            body = body.split(cut)[1] if cut.endswith('-->') else body.split(cut)[0]
    terms = [r'\blevers?\b', r'\bBucket [ABCD]\b', r'\bdo-not-deploy\b',
             r'\bfunnel\b', r'\bgotcha\b', r'\bbackstage\b',
             r'\bcrux question\b']
    leaks = [t for t in terms if re.search(t, body, re.I)]
    # Case-SENSITIVE: the handling-class marker, not the ordinary phrase
    # ("what Lutherans do not share…" is not a leak).
    if re.search(r'\bDO NOT SHARE\b', body):
        leaks.append('DO NOT SHARE')
    if leaks:
        err(f"[C7] On_Incense_and_the_Altar.md: BACKSTAGE VOCABULARY LEAK -> {leaks}. "
            f"This document is shareable with RJ.")
    else:
        ok("[C7] On_Incense_and_the_Altar.md: relay-clean firewall intact")

# ---------------------------------------------------------------- report
print("=" * 68)
print("PROJECT INTEGRITY VALIDATION")
print("=" * 68)
for m in OK:   print("  ok   ", m)
for m in WARN: print("  WARN ", m)
for m in ERR:  print("  ERROR", m)
print("-" * 68)
print(f"{len(OK)} ok · {len(WARN)} warnings · {len(ERR)} errors")
sys.exit(1 if ERR else 0)
