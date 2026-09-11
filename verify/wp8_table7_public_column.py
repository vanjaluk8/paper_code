#!/usr/bin/env python3
"""
WP-8 / P1-4 + C-8 -- Table 7 "Public" column tally, and the Pillar-4 denominator.

Recomputes both directly from sections/03_methodology.tex's Table 7
(\\label{tab:datasets}) body, rather than trusting the caption or prose.

Usage: python3 verify/wp8_table7_public_column.py
"""
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
METHOD_TEX = ROOT / "sections" / "03_methodology.tex"


def extract_table_body(text):
    start = text.index("\\label{tab:datasets}")
    # Table body runs from the first \midrule after the label to \end{tabular}
    body_start = text.index("\\midrule", start)
    body_end = text.index("\\end{tabular}", body_start)
    return text[body_start:body_end]


def main():
    text = METHOD_TEX.read_text(encoding="utf-8")
    body = extract_table_body(text)

    rows = []
    pillar = None
    for line in body.splitlines():
        line = line.strip()
        m_pillar = re.match(r"\\multicolumn\{6\}\{l\}\{\\textbf\{(Pillar \d[^}]*)\}\}", line)
        if m_pillar:
            pillar = m_pillar.group(1)
            continue
        m_row = re.search(r"&\s*(Yes|Partial|No|Unknown)\s*\\\\", line)
        if m_row:
            rows.append((pillar, m_row.group(1)))

    print(f"Total data rows parsed: {len(rows)} (expect 33)")
    assert len(rows) == 33

    tally = Counter(v for _, v in rows)
    print("Public column tally (from table body, not caption/prose):")
    for k in ["Yes", "Partial", "No", "Unknown"]:
        print(f"  {k}: {tally[k]}")
    print(f"  SUM: {sum(tally.values())}")

    expected = {"Yes": 26, "Partial": 1, "No": 2, "Unknown": 4}
    if tally == Counter(expected):
        print("-> Matches Sec 3.4.1's reported 26/1/2/4. OK.")
    else:
        print(f"-> MISMATCH vs Sec 3.4.1's reported 26/1/2/4: got {dict(tally)}")

    print()
    pillar4_rows = [(p, v) for p, v in rows if p and p.startswith("Pillar 4")]
    print(f"Pillar 4 (P2P and Federated Learning) rows: {len(pillar4_rows)}")
    p4_tally = Counter(v for _, v in pillar4_rows)
    print(f"  tally: {dict(p4_tally)}")
    print(f"  -> denominator for the 'federated or P2P fine-tuning methods' "
          f"claim in Sec 3.4.1 is {len(pillar4_rows)}, not 3.")


if __name__ == "__main__":
    main()
