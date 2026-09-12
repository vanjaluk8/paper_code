#!/usr/bin/env python3
"""
Blocking 5 -- generate the appraisal scoring template (baseline adequacy,
threats-to-validity reporting, peer-review status) over the union of the 17
concept-matrix systems and the 33 Table 7 systems.

Parses both system lists directly from the LaTeX source rather than
hand-transcribing them, to avoid the kind of miscount a manual list is prone
to (verified: 33 distinct systems total, the 17 concept-matrix systems all a
strict subset of the 33 Table 7 systems).

Usage: python3 verify/blocking5_generate_appraisal_template.py
"""
import re
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def parse_cited_systems(text, label_start, stop_at_second_midrule=False):
    start = text.index(label_start)
    body_start = text.index("\\midrule", start)
    if stop_at_second_midrule:
        body_end = text.index("\\midrule", body_start + 1)
    else:
        body_end = text.index("\\end{tabular}", body_start)
    body = text[body_start:body_end]
    systems = {}
    for line in body.splitlines():
        line = line.strip()
        m = re.match(r"^(.*?)~?\\cite\{([^}]+)\}", line)
        if m and "&" in line:
            name = re.sub(r"\\v\{([A-Za-z])\}", r"\1", m.group(1)).strip()
            key = m.group(2).split(",")[0].strip()
            systems[key] = name
    return systems


def main():
    methodology_tex = (ROOT / "sections" / "03_methodology.tex").read_text(encoding="utf-8")
    table7 = parse_cited_systems(methodology_tex, "\\label{tab:datasets}")
    assert len(table7) == 33, f"expected 33 Table 7 systems, got {len(table7)}"

    synthesis_tex = (ROOT / "sections" / "09_synthesis_gap.tex").read_text(encoding="utf-8")
    matrix17 = parse_cited_systems(synthesis_tex, "\\label{tab:concept_matrix}",
                                    stop_at_second_midrule=True)
    assert len(matrix17) == 17, f"expected 17 concept-matrix systems, got {len(matrix17)}"
    assert set(matrix17) <= set(table7), "concept-matrix systems must be a subset of Table 7"

    all_keys = set(table7) | set(matrix17)
    out_path = ROOT / "verify" / "blocking5_appraisal_scoring_template.csv"
    fieldnames = ["system", "bib_key", "in_concept_matrix_17", "in_table7_33",
                  "baseline_adequacy", "threats_to_validity_reporting",
                  "peer_reviewed_status", "notes"]
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for key in sorted(all_keys):
            name = table7.get(key) or matrix17.get(key)
            w.writerow({
                "system": name, "bib_key": key,
                "in_concept_matrix_17": "Y" if key in matrix17 else "N",
                "in_table7_33": "Y" if key in table7 else "N",
                "baseline_adequacy": "", "threats_to_validity_reporting": "",
                "peer_reviewed_status": "", "notes": "",
            })
    print(f"Wrote {out_path}: {len(all_keys)} distinct systems "
          f"({len(matrix17)} in concept matrix, all subset of {len(table7)} in Table 7)")


if __name__ == "__main__":
    main()
