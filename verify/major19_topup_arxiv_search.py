#!/usr/bin/env python3
"""
Major #19 -- partial top-up search via arXiv (free, no Scopus/WoS access
available in this environment).

This is NOT a substitute for the review's actual request (re-running the 20
Scopus/WoS Boolean queries from Appendix C against the gap window) -- arXiv
covers preprints only, with a different (looser, OR-heavy abstract-keyword)
query syntax than Scopus/WoS's precise Boolean strings, and Scopus/WoS also
index peer-reviewed venues arXiv does not. This is a signal, not a
replacement: if it turns up nothing notable, that's weak evidence the real
gap is probably also small; if it turns up several strong candidates, that's
a sign the full Scopus/WoS pass (verify/major20_topup_search_queries.md) is
worth prioritising.

Date window: 2026-05-13 (day after the last search date, 2026-05-12) through
today. Six thematic queries approximating the intent of Appendix C's 20
Scopus/WoS queries, adapted to arXiv's abstract-keyword search syntax.

No screening or inclusion judgement is made here -- this only retrieves
candidates and checks which are already in the corpus. Usage:
    python3 verify/major19_topup_arxiv_search.py
"""
import csv
import re
import subprocess
import time
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATE_FROM = "202605130000"
DATE_TO = "202609122359"

QUERIES = {
    "Q1_core_adapter_peft": (
        'abs:(adapter OR LoRA OR "low-rank adaptation") '
        'AND abs:("parameter-efficient" OR PEFT) '
        'AND abs:(NLP OR "language model" OR transformer)'
    ),
    "Q2_multitask_multiadapter_serving": (
        'abs:(adapter OR LoRA OR "parameter-efficient fine-tuning") '
        'AND abs:("multi-task" OR multitask OR "multi-adapter") '
        'AND abs:(inference OR serving OR deployment)'
    ),
    "Q3_p2p_distributed_learning": (
        'abs:("peer-to-peer" OR P2P OR decentralized OR decentralised OR federated) '
        'AND abs:(learning OR training OR inference) '
        'AND abs:("language model" OR NLP OR "deep learning")'
    ),
    "Q4_adapter_fusion_routing": (
        'abs:(adapter OR adapters) '
        'AND abs:(fusion OR routing OR "mixture-of-experts" OR MoE OR gating)'
    ),
    "Q5_modular_inference_task_switching": (
        'abs:(modular OR modularity) '
        'AND abs:(inference) '
        'AND abs:(adapter OR "task-specific" OR "lightweight modules")'
    ),
    "Q6_frozen_backbone_adapter": (
        'abs:("frozen" AND (backbone OR "base model")) '
        'AND abs:(adapter OR "parameter-efficient")'
    ),
}

NS = {"atom": "http://www.w3.org/2005/Atom"}


def arxiv_query(search_query: str, max_results: int = 100) -> list[dict]:
    full_query = f"{search_query} AND submittedDate:[{DATE_FROM} TO {DATE_TO}]"
    cmd = [
        "curl", "-sL", "-G", "--max-time", "30",
        "https://export.arxiv.org/api/query",
        "--data-urlencode", f"search_query={full_query}",
        "--data-urlencode", "sortBy=relevance",
        "--data-urlencode", f"max_results={max_results}",
    ]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=40).stdout
    root = ET.fromstring(out)
    entries = []
    for entry in root.findall("atom:entry", NS):
        arxiv_id = entry.find("atom:id", NS).text.strip().split("/abs/")[-1]
        arxiv_id = re.sub(r"v\d+$", "", arxiv_id)
        title = entry.find("atom:title", NS).text.strip().replace("\n", " ")
        published = entry.find("atom:published", NS).text.strip()
        summary = entry.find("atom:summary", NS).text.strip().replace("\n", " ")
        entries.append({
            "arxiv_id": arxiv_id, "title": title,
            "published": published, "summary": summary[:300],
        })
    return entries


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (t or "").strip().lower())


PEFT_TERMS = r"\b(adapter|adapters|lora|peft|parameter-efficient|low-rank adaptation)\b"
SCOPE_TERMS = (r"\b(federated|decentrali[sz]ed|peer-to-peer|p2p|multi-task|multitask|"
               r"serving|inference|routing|mixture-of-experts|moe)\b")


def title_level_filter(title: str) -> bool:
    """Same precision level as the manuscript's own Layer-2 title screening:
    require PEFT/adapter terminology AND a scope term to co-occur in the
    TITLE (not just the abstract), to cut the loose OR-heavy abstract search
    down to something worth a human look."""
    t = title.lower()
    return bool(re.search(PEFT_TERMS, t)) and bool(re.search(SCOPE_TERMS, t))


def load_corpus_titles() -> set[str]:
    with open(ROOT / "snowball_output" / "13_final_reading_list_2026-05-12.csv",
              encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    return {norm_title(r["title"]) for r in rows}


def main():
    corpus_titles = load_corpus_titles()
    all_results: dict[str, dict] = {}
    per_query_counts = {}

    for label, q in QUERIES.items():
        print(f"Running {label}...")
        try:
            entries = arxiv_query(q)
        except Exception as e:
            print(f"  ERROR: {e}")
            entries = []
        per_query_counts[label] = len(entries)
        for e in entries:
            key = e["arxiv_id"]
            if key not in all_results:
                e["matched_queries"] = [label]
                all_results[key] = e
            else:
                all_results[key]["matched_queries"].append(label)
        time.sleep(3)  # arXiv API rate-limit courtesy

    print()
    print("Per-query candidate counts (within the date window):")
    for label, n in per_query_counts.items():
        print(f"  {label}: {n}")

    total_unique = len(all_results)
    print(f"\nTotal unique arXiv candidates across all 6 queries: {total_unique}")

    already_in_corpus = 0
    new_candidates = []
    for e in all_results.values():
        if norm_title(e["title"]) in corpus_titles:
            already_in_corpus += 1
        else:
            new_candidates.append(e)

    print(f"Already in the 123-record corpus (by title match): {already_in_corpus}")
    print(f"Genuinely new candidates (not in corpus, unscreened): {len(new_candidates)}")

    # Title-level keyword filter (same precision as the manuscript's own
    # Layer-2 title screening) to cut the loose abstract-search noise down
    # to a reviewable shortlist. This is mechanical keyword filtering, not
    # an eligibility/inclusion judgement -- no topical or quality assessment
    # is applied.
    shortlisted = [e for e in new_candidates if title_level_filter(e["title"])]
    print(f"Title-level PEFT+scope co-occurrence (reviewable shortlist): {len(shortlisted)}")

    out_path = ROOT / "verify" / "major19_topup_arxiv_candidates.csv"
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["arxiv_id", "title", "published",
                                           "matched_queries", "summary"])
        w.writeheader()
        for e in sorted(shortlisted, key=lambda x: x["published"], reverse=True):
            w.writerow({
                "arxiv_id": e["arxiv_id"], "title": e["title"],
                "published": e["published"],
                "matched_queries": ";".join(e["matched_queries"]),
                "summary": e["summary"],
            })
    print(f"\nWrote {len(shortlisted)} shortlisted candidates to {out_path}")
    print(f"({len(new_candidates)} total unscreened candidates before the title filter)")
    print("No eligibility/inclusion judgement applied -- shortlist only, for human screening.")


if __name__ == "__main__":
    main()
