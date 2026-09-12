#!/usr/bin/env python3
"""Merge the author's Keep/Skip eligibility decisions (major19_eligibility_raw_decisions.json,
made interactively against the 65 abstract-screened Major-19 top-up survivors) with
major19_topup_screened.csv and major19_eligibility_suggestions.csv (Claude's per-item
I4/topical-fit read) into one eligibility-decision table.

id = sha1(title)[:12], the same key the review artifact used, so decisions join back
onto titles unambiguously without re-typing them.
"""
import csv
import hashlib
import json

SCREENED = "verify/major19_topup_screened.csv"
SUGGESTIONS = "verify/major19_eligibility_suggestions.csv"
DECISIONS = "verify/major19_eligibility_raw_decisions.json"
OUT = "verify/major19_eligibility_decisions.csv"


def slug(title):
    return hashlib.sha1(title.encode("utf-8")).hexdigest()[:12]


def main():
    suggestions = {}
    with open(SUGGESTIONS, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            suggestions[row["title"]] = (row["suggestion"], row["suggestion_reason"])

    decisions = json.load(open(DECISIONS))["items"]

    rows = []
    with open(SCREENED, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["screening_decision"] != "KEEP":
                continue
            title = row["title"]
            key = slug(title)
            if key not in decisions:
                raise SystemExit(f"no author decision recorded for: {title}")
            suggestion, reason = suggestions.get(title, ("", ""))
            rows.append({
                "title": title,
                "year": row["year"],
                "sources": row["sources"],
                "venue_or_id": row["venue_or_id"],
                "claude_suggestion": suggestion,
                "claude_suggestion_reason": reason,
                "author_decision": decisions[key],
            })

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    kept = [r for r in rows if r["author_decision"] == "keep"]
    skipped = [r for r in rows if r["author_decision"] == "skip"]
    print(f"{len(rows)} candidates decided: {len(kept)} keep, {len(skipped)} skip")
    print()
    print("KEEP:")
    for r in kept:
        print(f"  - {r['title']}  [{r['sources']}]")


if __name__ == "__main__":
    main()
