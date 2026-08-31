#!/usr/bin/env python3
"""
Phase 1 ground-truth verification for the PRISMA funnel.
Recomputes every funnel stage directly from pipeline data files.
No number is read from the .tex manuscript.
"""
import csv, json, os, sys
from collections import Counter, defaultdict

# Data root — the slr_engine repo's frozen output snapshot. Overridable via the
# SLR_OUTPUT env var; defaults to the flattened layout (slr_engine/snowballing/...).
import os as _os
SO = _os.environ.get(
    "SLR_OUTPUT",
    _os.path.join(_os.path.dirname(__file__), "..", "..", "slr_engine",
                  "snowballing", "snowball_output"),
)
SO = _os.path.abspath(SO)

def load_csv(name):
    p = os.path.join(SO, name)
    with open(p) as f:
        return list(csv.DictReader(f))

def load_json(name):
    p = os.path.join(SO, name)
    return json.load(open(p))

print("="*78)
print("PRISMA FUNNEL GROUND TRUTH (recomputed from pipeline data files)")
print("="*78)

# ---------------- Stage 1: raw candidates -> dedup -> title-screening pool ----
audit = load_json("log_screening_2026-04-21.json")
print("\n[Stage 1] Raw candidates & dedup (from log_screening_2026-04-21.json)")
print("  top-level keys:", list(audit.keys())[:20])

# The audit log structure - inspect
def walk(d, prefix="", depth=0):
    if depth>2: return
    if isinstance(d, dict):
        for k,v in d.items():
            if isinstance(v,(dict,list)):
                print("  "*depth + str(k) + " ("+type(v).__name__+")")
                walk(v,prefix,depth+1)
            else:
                print("  "*depth + f"{k} = {v}")
    elif isinstance(d,list):
        print("  "*depth + f"[list len {len(d)}]")

# just print relevant counts
print("  audit contains 'total' keys:", {k:audit[k] for k in audit if 'total' in k.lower() or 'count' in k.lower()})

# ---------------- Stage 2: title screening counts ---------------------------
# From audit json if present; else note.
if 'results' in audit:
    res = audit['results']
    print("\n[Stage 2] Title screening (results from audit log)")
    if isinstance(res, dict):
        print("  result keys:", list(res.keys())[:20])
    elif isinstance(res, list):
        dec = Counter(r.get('decision') or r.get('inclusion') for r in res)
        print("  decision counts:", dict(dec))
elif 'decisions' in audit:
    res = audit['decisions']
    print("\n[Stage 2] Title screening decisions (audit['decisions'])")
    if isinstance(res, dict):
        # dict of {decision_label: count}, e.g. INCLUDE=162 REVIEW=19 EXCLUDE=791
        print("  decision counts:", dict(res))
    elif isinstance(res, list):
        dec = Counter(r.get('decision') or r.get('inclusion') for r in res)
        print("  decision counts:", dict(dec))

# ---------------- Merge step: 162 INCLUDE + 352 prevalidated -> 502 ---------
rows = load_csv("pipeline_unified.csv")
def sel(pred): return [r for r in rows if pred(r)]

s5 = sel(lambda r: r["in_title_screened_S5"]=="1")
n_s5 = len(s5)
prevalidated = sel(lambda r: r["source_engine"] in ("undermind","seed"))
n_pre = len(prevalidated)
snowball_s5 = sel(lambda r: r["in_title_screened_S5"]=="1" and r["source_engine"] in ("ss","scopus","wos"))

print("\n[Stage merge] pipeline_unified.csv")
print(f"  in_title_screened_S5 = 1        : {n_s5}")
print(f"  pre-validated (undermind+seed)  : {n_pre}  ({sum(1 for r in s5 if r['source_engine'] in ('undermind','seed'))} of these in S5)")
print(f"  snowball-engine rows in S5      : {len(snowball_s5)}  (ss {sum(1 for r in snowball_s5 if r['source_engine']=='ss')}, "
      f"scopus {sum(1 for r in snowball_s5 if r['source_engine']=='scopus')}, wos {sum(1 for r in snowball_s5 if r['source_engine']=='wos')})")

# ---------------- Stage: enrichment / relevance filter ----------------------
s6 = sel(lambda r: r["in_enriched_S6"]=="1")
print("\n[Stage enrich] in_enriched_S6 = 1:", len(s6))

# ---------------- Stage: abstract review (552) ------------------------------
s7 = sel(lambda r: r["in_abstract_review_S7b"]=="1")
print("\n[Stage abstract] in_abstract_review_S7b = 1:", len(s7))
print("  abstract_decision:", dict(Counter(r["abstract_decision"] for r in s7)))
n_keep = sum(1 for r in s7 if r["abstract_decision"]=="KEEP")
n_skip = sum(1 for r in s7 if r["abstract_decision"]=="SKIP")
n_abstract_blank = sum(1 for r in s7 if r["abstract_decision"]=="")
print(f"  KEEP={n_keep} SKIP={n_skip} blank={n_abstract_blank}  (sum={n_keep+n_skip+n_abstract_blank})")

# ---------------- Stage: full-text queue (387?) -----------------------------
q9 = sel(lambda r: r["in_fulltext_queue_Q9"]=="1")
print("\n[Stage fulltext queue] in_fulltext_queue_Q9 = 1:", len(q9))
print("  abstract_decision in queue:", dict(Counter(r["abstract_decision"] for r in q9)))
print("  fulltext_decision in queue:", dict(Counter(r["fulltext_decision"] for r in q9)))

# ---------------- Stage: extraction (224?) ---------------------------------
ex = sel(lambda r: r["in_extraction_E11"]=="1")
print("\n[Stage extraction] in_extraction_E11 = 1:", len(ex))
print("  abstract_decision:", dict(Counter(r["abstract_decision"] for r in ex)))
print("  fulltext_decision:", dict(Counter(r["fulltext_decision"] for r in ex)))

# ---------------- Stage: final list (123 / 120) -----------------------------
fin = sel(lambda r: r["in_final_list_123"]=="1")
print("\n[Stage final] in_final_list_123 = 1:", len(fin))
print("  tier:", dict(Counter(r["tier"] for r in fin)))
print("  abstract_decision (all KEEP?):", dict(Counter(r["abstract_decision"] for r in fin)))
# distinct papers: by final_paper_key
keys = [r["final_paper_key"] or r["title"].strip().lower() for r in fin]
print("  distinct final_paper_key:", len(set(keys)))
# what about duplicates
dups = [k for k,c in Counter(keys).items() if c>1]
print("  duplicate keys:", len(dups), [(k, Counter(keys)[k]) for k in dups])

# ---------------- Cross-file checks -----------------------------------------
print("\n[Cross-file] file row counts")
for name in ["S7b_abstract_reviewed_final.csv","09_fulltext_review_queue_2026-05-02.csv",
             "11_data_extraction_2026-05-12.csv","13_final_reading_list_2026-05-12.csv"]:
    print(f"  {name}: {len(load_csv(name))} rows")

# RIS KEEP export
try:
    ris = open(os.path.join(SO,"08_zotero_ready_2026-05-02.ris")).read()
    n_ris = ris.count("\nTY  - ")
    print("  08_zotero_ready_2026-05-02.ris: entries =", n_ris)
except Exception as e:
    print("  RIS read error:", e)
