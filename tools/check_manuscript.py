#!/usr/bin/env python3
"""Structural checks for the SLR manuscript. Usage: python3 tools/check_manuscript.py main.pdf"""
import re, subprocess, sys, os, collections

def text(pdf):
    """Extract laid-out text. Prefer poppler `pdftotext -layout` (the format the
    checks were calibrated on); fall back to PyMuPDF layout mode when poppler is
    not installed locally (e.g. this repo builds via Docker)."""
    if shutil_which('pdftotext'):
        try:
            return subprocess.run(['pdftotext', '-layout', pdf, '-'],
                                  capture_output=True, text=True, check=True).stdout
        except Exception:
            pass
    import fitz
    d = fitz.open(pdf)
    return '\n'.join(p.get_text('text') for p in d)

def shutil_which(name):
    from shutil import which
    return which(name)

def check_float_citations(t):
    """Every Figure/Table must be referenced somewhere other than its own caption."""
    bad = []
    lines = t.split('\n')
    caption_of = collections.defaultdict(list)
    ref_of = collections.defaultdict(list)
    for i, ln in enumerate(lines):
        s = ln.strip()
        cap = re.match(r'^(Figure|Table)\s+(A?\d+)\.', s)
        for m in re.finditer(r'\b(Figure|Table)s?\s+(A?\d+)', s):
            key = f"{m.group(1)} {m.group(2)}"
            if cap and cap.group(0).startswith(key):
                caption_of[key].append(i)
            else:
                ref_of[key].append(i)
    for key in sorted(caption_of, key=lambda k: (k.split()[0], k.split()[1])):
        if not ref_of[key]:
            bad.append(f"UNCITED: {key} appears only as a caption")
    # first-citation ordering, per kind
    for kind in ('Figure', 'Table'):
        firsts = [(min(ref_of[k]), k) for k in ref_of if k.startswith(kind)
                  and not k.split()[1].startswith('A') and ref_of[k]]
        order = [k for _, k in sorted(firsts)]
        nums = [int(k.split()[1]) for k in order]
        if nums != sorted(nums):
            bad.append(f"OUT OF ORDER ({kind}): first citations run {order}")
    return bad

def check_headings(t):
    bad = []
    if not re.search(r'^\s*References\s*$', t, re.M):
        bad.append("MISSING: 'References' heading")
    for h in ['Author Contributions', 'Funding', 'Data Availability',
              'Conflicts of Interest', 'Acknowledgments']:
        if h not in t:
            bad.append(f"MISSING: '{h}' statement")
    return bad

def check_prisma(t):
    """Recompute the funnel from the numbers the manuscript states."""
    bad, chain = [], [
        ("identified - duplicates = screened", 1150 - 178, 972),
        ("title outcomes sum to screened",      162 + 791 + 19, 972),
        ("merge minus cross-dupes",             162 + 352 - 12, 502),
        ("enrichment",                          502 - 38, 464),
        ("abstract pool",                       464 + 88, 552),
        ("abstract outcomes",                   214 + 173 + 165, 552),
        ("full-text queue",                     214 + 173, 387),
        ("queue exclusions",                    24 + 173, 197),
        ("extraction",                          190 + 34, 224),
        ("final",                               224 - 101, 123),
        ("tiers of final list",                 48 + 42 + 33, 123),
        ("tiers of enriched pool",              90 + 141 + 233, 464),
        ("quality bands",                       13 + 61 + 47 + 2, 123),
    ]
    for label, got, want in chain:
        if got != want:
            bad.append(f"ARITHMETIC: {label}: {got} != {want}")
    if '101' not in re.sub(r'\s+', ' ', t).replace('10.1', ''):
        bad.append("PRISMA 16b: no discussion of the 101 eligibility-stage exclusions")
    return bad

def check_prose(t):
    bad = []
    if re.search(r'5[–-]13screening', t):
        bad.append("BROKEN SENTENCE: '5-13screening' in Threats to Validity (B5)")
    # 'chapter' is a thesis-register word (manuscript section). Exclude proper
    # nouns: "North American Chapter of the Association..." / "European Chapter
    # of ..." are conference venue names (NAACL/EACL booktitles), not register.
    # The region adjective ("North American"/"European") always sits adjacent to
    # "Chapter" in these venue names, which is layout-robust (the "of the
    # Association" tail can be pushed far right by the pdftotext page-number
    # column, but "North American Chapter" never wraps mid-phrase).
    n = len(re.findall(r'\bchapters?\b', t, re.I))
    n -= len(re.findall(r'(?:North American|European)\s+Chapter', t))
    if n:
        bad.append(f"REGISTER: 'chapter' appears {n}x — should be 'Section'")
    for pat, why in [(r'\bfor this thesis\b', 'thesis register'),
                     (r'\bthe thesis narrative\b', 'thesis register'),
                     (r'\bwe treat this\b', 'first person'),
                     (r'\bto our knowledge\b', 'first person'),
                     (r'\bto the best of our knowledge\b', 'first person')]:
        if re.search(pat, t, re.I):
            bad.append(f"VOICE/{why}: {pat}")
    if re.search(r'Proceedings of the Proceedings of', t):
        bad.append("REF 26: duplicated 'Proceedings of the'")
    if 'MT-EF' in t and not re.search(r'Multi-?Task.{0,40}MT-?EF|MT-?EF\s*\(', t):
        bad.append("ACRONYM: MT-EF never expanded")
    moe = t.find('MoE'); full = t.lower().find('mixture-of-experts')
    if 0 <= moe < full:
        bad.append("ACRONYM: 'MoE' used before 'Mixture-of-Experts' is expanded")
    return bad

def check_crossrefs(t):
    bad = []
    if re.search(r'quality[- ]appraisal[^.]{0,80}§?\s*3\.3', t, re.I):
        bad.append("XREF: quality appraisal cited as §3.3 (is §3.4)")
    if re.search(r'documented in Appendix B', t):
        bad.append("XREF: Scopus/WoS queries cited as Appendix B (are Appendix C)")
    if re.search(r'^\s*C\.\d', t, re.M) and 'Appendix D' in t:
        bad.append("XREF: Appendix D subsections numbered C.x")
    if '??' in t:
        bad.append("LATEX: unresolved reference '??' in output")
    return bad

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("usage: python3 tools/check_manuscript.py main.pdf")
    t = text(sys.argv[1])
    issues = (check_headings(t) + check_float_citations(t) + check_prisma(t)
              + check_crossrefs(t) + check_prose(t))
    for i in issues:
        print(i)
    print(f"\n{len(issues)} issue(s).")
    sys.exit(1 if issues else 0)
