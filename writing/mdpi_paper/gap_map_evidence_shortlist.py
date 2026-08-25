#!/usr/bin/env python3
"""
gap_map_evidence_shortlist.py

Purpose: generate a per-row shortlist of candidate papers to cite as evidence
in tab:gap_map (sections/09_synthesis_gap.tex), replacing the current
G-group-level evidence with 2-3 specific paper citations per row.

SAFETY CONTRACT (do not weaken these):
  - This script is READ-ONLY against every pipeline/manuscript file.
  - It NEVER writes to bibliography.bib, any sections/*.tex file, or any
    PRISMA numbers/validation file.
  - Its only output is OUTPUT_MD below -- a suggestions file for manual
    review. Nothing it produces should be pasted into the manuscript
    without you personally checking the paper first.
  - It asserts the final-corpus row count before doing anything else. If
    that assertion fails, it stops. This is the guard against silently
    generating suggestions from the wrong pipeline stage (464 / 552 / 224
    instead of the true final 123).

USAGE:
  1. Edit the CONFIG block below so the paths match your actual repo layout.
  2. Run: python3 gap_map_evidence_shortlist.py
  3. Read gap_map_evidence_shortlist.md. Pick 2-3 papers per row yourself.
  4. Manually edit tab:gap_map's Evidence column in
     sections/09_synthesis_gap.tex -- this script will not do that for you.
"""

import csv
import sys
from pathlib import Path

# =============================================================================
# CONFIG -- adjust these paths to your actual repository layout before running
# =============================================================================

FINAL_READING_LIST = "/Users/vanja/git/papers_code/writing/slr_methodology_paper/writing_materials/13_final_reading_list_2026-05-12.csv"   # the authoritative 123
EXTRACTION_FILE = "/Users/vanja/git/papers_code/writing/mdpi_paper/11_data_extraction_2026-05-12.csv"          # 224-row extraction table
# Optional fallback source for G-group tags if the final list doesn't carry one.
# Try these in order; first one found and readable wins.
GROUP_SOURCE_CANDIDATES = [
    "/Users/vanja/git/papers_code/writing/slr_methodology_paper/writing_materials/13_final_reading_list_2026-05-12.csv",
    "S6_enriched_reading_pool.csv",
    "S1_prevalidated_corpus.csv",
]

EXPECTED_FINAL_COUNT = 123
EXPECTED_DISTINCT_COUNT = 120  # per your known dedup pairs (LoRA, Houlsby, CaraServe/Toppings)

OUTPUT_MD = "gap_map_evidence_shortlist.md"
TOP_N_PER_ROW = 5  # how many candidates to list per gap-map row

# =============================================================================
# Gap-map rows, taken verbatim from tab:gap_map in sections/09_synthesis_gap.tex
# (quadrant, short id, groups cited as evidence, gap description, keyword hints)
# =============================================================================

GAP_ROWS = [
    dict(
        quadrant="Conceptual",
        row_id="C1",
        groups=["G0", "G1", "G2", "G3", "G4", "G5", "G6"],
        description="No work frames adapters as autonomous, transferable knowledge "
                     "units with identity, provenance, and capability in a P2P context",
        keywords=["adapter", "identity", "provenance", "capability", "knowledge unit"],
    ),
    dict(
        quadrant="Algorithmic",
        row_id="A1",
        groups=["G3", "G4"],
        description="No protocol identified for locating task-relevant adapters "
                     "across a P2P network without a central registry",
        keywords=["discovery", "registry", "lookup", "DHT", "index"],
    ),
    dict(
        quadrant="Algorithmic",
        row_id="A2",
        groups=["G2", "G5"],
        description="No reviewed method derives a compact, data-free representation "
                     "of adapter functional capability from weights alone",
        keywords=["weight-space", "representation", "capability", "similarity", "embedding"],
    ),
    dict(
        quadrant="Algorithmic",
        row_id="A3",
        groups=["G2", "G4"],
        description="No reviewed method provides a functional, behaviour-based "
                     "adapter descriptor robust to distribution shift",
        keywords=["probe", "behaviour", "functional descriptor", "distribution shift"],
    ),
    dict(
        quadrant="Systems",
        row_id="S1",
        groups=["G3", "G4"],
        description="No P2P architecture proposed for adapter exchange without "
                     "central infrastructure",
        keywords=["P2P", "architecture", "decentralised", "no central", "exchange"],
    ),
    dict(
        quadrant="Systems",
        row_id="S2",
        groups=["G3", "G6"],
        description="No gossip-based protocol identified for adapter metadata "
                     "dissemination across a dynamic peer population",
        keywords=["gossip", "metadata", "dissemination", "churn", "peer population"],
    ),
    dict(
        quadrant="Empirical",
        row_id="E1",
        groups=["G3", "G6"],
        description="No theoretical bounds derived for adapter reuse quality as a "
                     "function of distribution distance between peers",
        keywords=["distribution distance", "reuse quality", "bound", "non-IID"],
    ),
    dict(
        quadrant="Empirical",
        row_id="E2",
        groups=["G2", "G5"],
        description="All reviewed composition methods require centralised training "
                     "data for the fusion step, incompatible with P2P operation",
        keywords=["fusion", "centralised training data", "composition", "AdapterFusion"],
    ),
]

# =============================================================================
# Helpers
# =============================================================================

def fail(msg):
    print(f"\nABORTING: {msg}", file=sys.stderr)
    sys.exit(1)


def load_csv(path):
    p = Path(path)
    if not p.exists():
        fail(f"File not found: {path}. Fix the CONFIG block before rerunning.")
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def find_group_column(rows):
    """Look for a plausible G-group column among common naming variants."""
    if not rows:
        return None
    candidates = ["seed_group", "group", "prevalidated_group", "corpus_group", "G_group"]
    for cand in candidates:
        if cand in rows[0]:
            return cand
    return None


# =============================================================================
# Main
# =============================================================================

def main():
    print("Loading final reading list:", FINAL_READING_LIST)
    final_rows = load_csv(FINAL_READING_LIST)

    # --- SAFETY CHECK: this is the guard against loading the wrong pipeline stage ---
    if len(final_rows) != EXPECTED_FINAL_COUNT:
        fail(
            f"Final reading list has {len(final_rows)} rows, expected "
            f"{EXPECTED_FINAL_COUNT}. This does NOT look like the authoritative "
            f"final corpus -- check FINAL_READING_LIST in CONFIG before proceeding. "
            f"Refusing to generate suggestions from a possibly-wrong file."
        )
    if "paper_key" not in final_rows[0]:
        fail("Final reading list has no 'paper_key' column -- check the file/schema.")

    distinct_titles = len({(r.get("title") or "").strip().lower() for r in final_rows})
    print(f"OK: {len(final_rows)} rows loaded (expected {EXPECTED_FINAL_COUNT}).")
    print(f"    Distinct titles: {distinct_titles} (expected {EXPECTED_DISTINCT_COUNT}) "
          f"-- {'OK' if distinct_titles == EXPECTED_DISTINCT_COUNT else 'MISMATCH, verify manually'}")

    final_keys = {r["paper_key"] for r in final_rows}

    # --- Locate G-group tags ---
    group_col = None
    group_source_rows = None
    for candidate_path in GROUP_SOURCE_CANDIDATES:
        try:
            rows = load_csv(candidate_path)
        except SystemExit:
            continue
        col = find_group_column(rows)
        if col:
            group_col = col
            group_source_rows = rows
            print(f"Found group column '{col}' in {candidate_path}")
            break

    group_by_key = {}
    if group_col and group_source_rows:
        for r in group_source_rows:
            k = r.get("paper_key")
            if k:
                group_by_key[k] = (r.get(group_col) or "").strip()
    else:
        print(
            "WARNING: no seed_group-style column found in any candidate file. "
            "Falling back to keyword-only matching (less precise -- review "
            "candidates more carefully before using them)."
        )

    # --- Load extraction data for tier / citation_count / key_finding / sections ---
    print("Loading extraction file:", EXTRACTION_FILE)
    extraction_rows = load_csv(EXTRACTION_FILE)
    extraction_by_key = {r["paper_key"]: r for r in extraction_rows if r.get("paper_key") in final_keys}
    print(f"Matched {len(extraction_by_key)} of {len(final_keys)} final-corpus papers "
          f"in the extraction file.")
    if len(extraction_by_key) < len(final_keys) * 0.8:
        print(
            "WARNING: fewer than 80% of final-corpus papers matched in the extraction "
            "file. Some candidates below may be missing metadata -- do not assume the "
            "shortlist is complete."
        )

    # --- Build candidate pool: only papers actually in the final 123 ---
    pool = []
    for key in final_keys:
        erow = extraction_by_key.get(key, {})
        pool.append({
            "paper_key": key,
            "title": erow.get("title", ""),
            "tier": erow.get("tier", ""),
            "citation_count": _safe_int(erow.get("citation_count")),
            "thesis_sections": erow.get("thesis_sections", ""),
            "distribution_mechanism": (erow.get("distribution_mechanism") or "").lower(),
            "peft_technique": (erow.get("peft_technique") or "").lower(),
            "key_finding": erow.get("key_finding", ""),
            "notes_raw": (erow.get("notes_raw") or "").lower(),
            "group": group_by_key.get(key, ""),
        })

    # --- Score and shortlist per gap-map row ---
    out_lines = [
        "# Gap-map evidence shortlist (candidates only -- verify before using)\n",
        f"Generated from {FINAL_READING_LIST} ({len(final_rows)} rows) and "
        f"{EXTRACTION_FILE}. Read-only output -- nothing here has been written "
        f"into the manuscript.\n",
    ]
    if not group_col:
        out_lines.append(
            "> **No G-group column found** -- rankings below are keyword-only "
            "and less reliable. Cross-check against tab:groups in "
            "03_methodology.tex manually.\n"
        )

    for row in GAP_ROWS:
        scored = []
        for p in pool:
            score = 0
            reasons = []
            if group_col and p["group"]:
                group_hits = [g for g in row["groups"] if g in p["group"]]
                if group_hits:
                    score += 10 * len(group_hits)
                    reasons.append(f"group match: {group_hits}")
            haystack = " ".join([
                p["distribution_mechanism"], p["peft_technique"],
                p["notes_raw"], p["key_finding"].lower(),
            ])
            kw_hits = [kw for kw in row["keywords"] if kw.lower() in haystack]
            if kw_hits:
                score += len(kw_hits)
                reasons.append(f"keyword match: {kw_hits}")
            if p["tier"] == "1":
                score += 2
            score += min(p["citation_count"] or 0, 500) / 100.0  # mild citation tiebreak

            if score > 0:
                scored.append((score, p, reasons))

        scored.sort(key=lambda x: x[0], reverse=True)
        top = scored[:TOP_N_PER_ROW]

        out_lines.append(f"\n## {row['quadrant']} — {row['row_id']}: {row['description']}\n")
        out_lines.append(f"Current evidence (group-level): {', '.join(row['groups'])}\n")
        if not top:
            out_lines.append("No candidates scored above zero -- review manually.\n")
            continue
        for score, p, reasons in top:
            out_lines.append(
                f"- **{p['paper_key']}** (tier {p['tier'] or '?'}, "
                f"{p['citation_count'] or 0} citations, group={p['group'] or '?'}) "
                f"-- score {score:.1f} [{'; '.join(reasons)}]\n"
                f"  - {p['title']}\n"
                f"  - key_finding: {p['key_finding'] or '(none recorded)'}\n"
            )

    Path(OUTPUT_MD).write_text("".join(out_lines), encoding="utf-8")
    print(f"\nWrote {OUTPUT_MD} -- review it and pick 2-3 papers per row yourself.")
    print("Nothing has been changed in any manuscript or bibliography file.")


def _safe_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return 0


if __name__ == "__main__":
    main()
