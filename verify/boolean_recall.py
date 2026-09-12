#!/usr/bin/env python3
"""
WP-12 / Major #10 -- Boolean recall of the final 123-record corpus.

The review's single highest-value suggested fix: of the 123 final included
records, how many are returned by at least one of the 20 Scopus/WoS Boolean
queries in Appendix C? This is the manual cross-validation search reported in
Appendix D.4 -- 172 Scopus records + 125 WoS records, run against the live
database interfaces on 2026-05-11.

Match rule (DOI first, then normalised title, per the task instructions):
  1. Normalise DOI: lowercase, strip whitespace, strip a leading
     "https://doi.org/" if present.
  2. Normalise title: lowercase, strip whitespace, collapse internal
     whitespace, strip trailing punctuation, drop all non-alphanumeric
     characters (so hyphenation/colon/curly-quote differences between Scopus,
     WoS and the reading-list export don't cause false negatives).
  3. A final-corpus record is "recalled" if its DOI matches a Boolean-export
     row's DOI, OR (when no DOI match is found) its normalised title matches
     a Boolean-export row's normalised title.

This script does not write manuscript prose -- only the numbers and the
per-record table, per instruction.

Usage: python3 verify/boolean_recall.py
Outputs: verify/boolean_recall.md (the deliverable), plus prints a summary.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FINAL_LIST = ROOT / "snowball_output" / "13_final_reading_list_2026-05-12.csv"
SCOPUS_EXPORT = ROOT / "snowball_output" / "11_MANUAL_SCOPUS_export_1105.csv"
WOS_EXPORT = ROOT / "snowball_output" / "11_MANUAL_WOS_export_1105.txt"
OUT_MD = ROOT / "verify" / "boolean_recall.md"


def norm_doi(doi):
    if not doi:
        return ""
    d = doi.strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    d = re.sub(r"^doi:\s*", "", d)
    return d


def norm_title(title):
    if not title:
        return ""
    t = title.strip().lower()
    t = re.sub(r"[^a-z0-9]+", "", t)  # drop all punctuation/whitespace
    return t


def load_final_records():
    with open(FINAL_LIST, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 123
    out = []
    for r in rows:
        out.append({
            "paper_key": r["paper_key"],
            "title": r["title"],
            "doi": r.get("doi", ""),
            "arxiv_id": r.get("arxiv_id", ""),
            "doi_norm": norm_doi(r.get("doi", "")),
            "title_norm": norm_title(r["title"]),
        })
    return out


def load_scopus_export():
    with open(SCOPUS_EXPORT, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        out.append({
            "title": r.get("Title", ""),
            "doi": r.get("DOI", ""),
            "doi_norm": norm_doi(r.get("DOI", "")),
            "title_norm": norm_title(r.get("Title", "")),
        })
    return out


def load_wos_export():
    with open(WOS_EXPORT, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    out = []
    for r in rows:
        out.append({
            "title": r.get("TI", ""),
            "doi": r.get("DI", ""),
            "doi_norm": norm_doi(r.get("DI", "")),
            "title_norm": norm_title(r.get("TI", "")),
        })
    return out


def main():
    final = load_final_records()
    scopus = load_scopus_export()
    wos = load_wos_export()

    scopus_doi = {r["doi_norm"] for r in scopus if r["doi_norm"]}
    scopus_title = {r["title_norm"] for r in scopus if r["title_norm"]}
    wos_doi = {r["doi_norm"] for r in wos if r["doi_norm"]}
    wos_title = {r["title_norm"] for r in wos if r["title_norm"]}

    results = []
    for r in final:
        matched_scopus_doi = bool(r["doi_norm"]) and r["doi_norm"] in scopus_doi
        matched_wos_doi = bool(r["doi_norm"]) and r["doi_norm"] in wos_doi
        matched_scopus_title = bool(r["title_norm"]) and r["title_norm"] in scopus_title
        matched_wos_title = bool(r["title_norm"]) and r["title_norm"] in wos_title

        if matched_scopus_doi or matched_wos_doi:
            match_type = "DOI"
        elif matched_scopus_title or matched_wos_title:
            match_type = "title"
        else:
            match_type = None

        recalled = match_type is not None
        which = []
        if matched_scopus_doi or matched_scopus_title:
            which.append("Scopus")
        if matched_wos_doi or matched_wos_title:
            which.append("WoS")

        results.append({
            **r,
            "recalled": recalled,
            "match_type": match_type,
            "matched_in": "+".join(which) if which else "-",
        })

    n_recalled = sum(1 for r in results if r["recalled"])
    pct = 100 * n_recalled / len(results)
    not_recalled = [r for r in results if not r["recalled"]]

    print(f"Final corpus: {len(results)} records")
    print(f"Recalled by at least one Boolean query: {n_recalled} ({pct:.1f}%)")
    print(f"Not recalled: {len(not_recalled)}")
    by_type = {}
    for r in results:
        if r["recalled"]:
            by_type[r["match_type"]] = by_type.get(r["match_type"], 0) + 1
    print(f"  matched by DOI: {by_type.get('DOI', 0)}")
    print(f"  matched by title only: {by_type.get('title', 0)}")

    # Write the markdown deliverable.
    lines = []
    lines.append("# Boolean Recall of the Final 123-Record Corpus")
    lines.append("")
    lines.append("WP-12 / Major #10. Computed by `verify/boolean_recall.py` from:")
    lines.append("- `snowball_output/13_final_reading_list_2026-05-12.csv` (123 final records)")
    lines.append("- `snowball_output/11_MANUAL_SCOPUS_export_1105.csv` (172 records, Appendix C's 10 Scopus queries, run 2026-05-11)")
    lines.append("- `snowball_output/11_MANUAL_WOS_export_1105.txt` (125 records, Appendix C's 10 WoS queries, run 2026-05-11)")
    lines.append("")
    lines.append("Match rule: DOI match first (normalised, case-insensitive, "
                  "`doi.org/` prefix stripped); falling back to normalised-title "
                  "match (lowercased, punctuation/whitespace stripped) only when "
                  "no DOI match is found.")
    lines.append("")
    lines.append("## Headline result")
    lines.append("")
    lines.append(f"**{n_recalled} of {len(results)} final records ({pct:.1f}%)** are returned by "
                  "at least one of the 20 Scopus/WoS Boolean queries.")
    lines.append("")
    lines.append(f"- Matched by DOI: {by_type.get('DOI', 0)}")
    lines.append(f"- Matched by title only (no DOI match): {by_type.get('title', 0)}")
    lines.append(f"- Not matched by either export: {len(not_recalled)}")
    lines.append("")
    lines.append("## Records NOT returned by any Boolean query")
    lines.append("")
    lines.append("| paper_key | title | doi | arxiv_id |")
    lines.append("|---|---|---|---|")
    for r in not_recalled:
        title = r["title"].replace("|", "\\|")
        lines.append(f"| {r['paper_key']} | {title} | {r['doi']} | {r['arxiv_id']} |")
    lines.append("")
    lines.append("## Full per-record table")
    lines.append("")
    lines.append("| paper_key | title | recalled | match type | matched in |")
    lines.append("|---|---|---|---|---|")
    for r in results:
        title = r["title"].replace("|", "\\|")
        lines.append(f"| {r['paper_key']} | {title} | {'Yes' if r['recalled'] else 'No'} "
                      f"| {r['match_type'] or '-'} | {r['matched_in']} |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nWrote {OUT_MD}")


if __name__ == "__main__":
    main()
