# Major #19 — Ready-to-run Scopus and WoS top-up queries

Same 20 Boolean queries as Appendix C (`sections/12_appendix.tex`, §C.1–C.2),
**verbatim except for the year bound**, so any new hits are attributable to
the passage of time, not a change in search strategy. Core query logic is
unchanged from the original searches your corpus is built on.

## Why the year filter alone isn't enough — read this before running

Scopus's `PUBYEAR` and WoS's `PY` are **year-granularity only** — there's no
raw-query field for "May 2026 onward" that I can verify works without live
access to test it. Simply changing `PUBYEAR > 2018` to `PUBYEAR > 2025` gives
you all of 2026, which **re-includes January–May 2026** — records your
original search already covered.

**Two ways to close that gap, pick one:**

1. **Safe, guaranteed to work (recommended):** run each query below as-is,
   then apply the platform's own UI date-range refiner — Scopus: "Refine
   results" → "Date range" or "Load date"; WoS: "Refine results" →
   "Timespan" → custom range — set to **2026-05-13 through today**. This
   works regardless of which raw-query date field your subscription
   supports.
2. **Faster if it works for you:** Scopus supports a `LOAD-DATE` field in
   some subscription tiers (`AND LOAD-DATE AFT 20260512`) that filters by
   when Scopus indexed the record rather than its stated cover date — more
   robust against papers whose cover year lags their actual appearance. I
   haven't been able to verify this field is available on your specific
   Scopus access, so try it, and fall back to option 1 if it errors.

De-duplicate whatever you export against the existing 123-record corpus
before screening — `verify/boolean_recall.py`'s matching logic (DOI first,
then normalised title) can be pointed at your new export files directly.

---

## Scopus (C.1) — 10 queries, year bound updated to 2025 (= "2026 onward")

**Q1 — Core Adapter-Based NLP.**
```
TITLE-ABS-KEY(("adapter" OR "adapters" OR "LoRA" OR "low-rank")
AND ("parameter-efficient" OR "PEFT" OR "parameter efficient")
AND ("NLP" OR "natural language processing" OR "transformer"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2025
```

**Q2 — Multi-Task Learning with Transformers.**
```
TITLE-ABS-KEY((("adapter*" OR "LoRA" OR "parameter-efficient fine-tuning")
AND ("multi-task" OR "multitask" OR "multi-adapter")
AND ("inference" OR "serving" OR "deployment" OR "edge")))
AND SRCTYPE(j OR p)
AND PUBYEAR > 2025
AND NOT TITLE-ABS-KEY(("medical" OR "healthcare" OR "clinical"
    OR "sentiment" OR "recommendation"))
```

**Q3 — Peer-to-Peer & Distributed NLP.**
```
TITLE-ABS-KEY(("peer-to-peer" OR "P2P" OR "decentralized" OR "federated")
AND ("learning" OR "training" OR "inference")
AND ("NLP" OR "natural language" OR "machine learning" OR "deep learning"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2025
```

**Q4 — Adapter Fusion & Dynamic Routing.**
```
TITLE-ABS-KEY(("adapter" OR "adapters")
AND ("fusion" OR "routing" OR "dynamic" OR "mixture-of-experts"
    OR "MoE" OR "gating"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2025
```

**Q5 — Parameter-Efficient Multi-Task Transformers.**
```
TITLE-ABS-KEY(("parameter-efficient" OR "PEFT" OR "efficient adaptation")
AND ("multi-task" OR "multitask")
AND ("transformer" OR "pre-trained models"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2025
```

**Q6 — Modular Inference & Task Switching.**
```
TITLE-ABS-KEY(("modular" OR "modularity")
AND ("inference" OR "inference time")
AND ("adapter" OR "task-specific" OR "lightweight modules"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2025
```

**Q7 — Agent-Based Collaborative Learning.**
```
TITLE-ABS-KEY(("agent" OR "agents" OR "node" OR "nodes")
AND ("collaborative" OR "collaboration" OR "decentralized")
AND ("deep learning" OR "neural network" OR "model training"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2025
```

**Q8 — NL-to-SQL with Adapters.**
```
TITLE-ABS-KEY(("NL-to-SQL" OR "semantic parsing"
    OR "natural language to SQL")
AND ("adapter" OR "fine-tun*" OR "parameter-efficient" OR "efficient"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2025
```

**Q9 — Sequence Labelling & Token Classification with PEFT.**
```
TITLE-ABS-KEY(("token classification" OR "NER"
    OR "named entity recognition" OR "sequence labeling")
AND ("adapter" OR "LoRA" OR "parameter-efficient" OR "PEFT"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2025
```

**Q10 — Frozen Base Model Paradigm.**
```
TITLE-ABS-KEY(("frozen" OR "freeze" OR "frozen base")
AND ("adapter" OR "efficient" OR "modular")
AND ("transfer learning" OR "fine-tun*"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2025
```

---

## Web of Science (C.2) — 10 queries, year bound updated to 2026

**Q1 — Core Adapter-Based NLP.**
```
TS=(("adapter" OR "adapters" OR "LoRA" OR "low-rank")
AND ("parameter-efficient" OR "PEFT" OR "parameter efficient")
AND ("NLP" OR "natural language processing" OR "transformer"))
AND PY >= 2026
```

**Q2 — Multi-Task Adapter Inference.**
```
TS=((("adapter*" OR "LoRA" OR "PEFT")
AND ("multi-task" OR "multitask")
AND ("inference" OR "serving" OR "edge" OR "distributed")))
AND PY >= 2026
AND NOT TS=(("medical" OR "healthcare" OR "sentiment"))
```

**Q3 — Peer-to-Peer Distributed Learning.**
```
TS=(("peer-to-peer" OR "P2P" OR "decentralized" OR "federated")
AND ("learning" OR "training" OR "inference")
AND ("NLP" OR "natural language" OR "machine learning"
    OR "neural network"))
AND PY >= 2026
```

**Q4 — Adapter Fusion & Routing Mechanisms.**
```
TS=(("adapter" OR "adapters")
AND ("fusion" OR "dynamic routing" OR "mixture-of-experts"
    OR "MoE" OR "gating"))
AND PY >= 2026
```

**Q5 — Modular Deep Learning.**
```
TS=(("modular" OR "modularity")
AND ("neural" OR "transformer" OR "deep learning")
AND ("inference" OR "task-specific" OR "lightweight"))
AND PY >= 2026
```

**Q6 — Agent-Based Collaborative ML.**
```
TS=(("agent" OR "agents" OR "distributed node*")
AND ("collaborative" OR "collaboration" OR "decentralized"
    OR "gossip")
AND ("deep learning" OR "machine learning"))
AND PY >= 2026
```

**Q7 — Memory-Efficient Multi-Task NLP.**
```
TS=(("multi-task" OR "multitask")
AND ("memory-efficient" OR "memory efficient"
    OR "parameter-efficient" OR "computational efficient")
AND ("NLP" OR "natural language" OR "transformer"))
AND PY >= 2026
```

**Q8 — Transfer Learning with Task Adaptation.**
```
TS=(("transfer learning" OR "fine-tun*")
AND ("adapter" OR "parameter-efficient" OR "LoRA")
AND ("NLP" OR "text" OR "language"))
AND PY >= 2026
```

**Q9 — Sequence Task Learning.**
```
TS=(("token classification" OR "NER" OR "named entity"
    OR "sequence labeling")
AND ("adapter" OR "fine-tun*" OR "efficient" OR "modular"))
AND PY >= 2026
```

**Q10 — Distributed Inference.**
```
TS=(("distributed" OR "decentralized")
AND ("inference" OR "inference time")
AND ("efficient" OR "modular" OR "lightweight"))
AND PY >= 2026
```

---

## After running these

1. Export all hits from both platforms (CSV for Scopus, tab-delimited for
   WoS — same format as the original `11_MANUAL_SCOPUS_export_1105.csv` /
   `11_MANUAL_WOS_export_1105.txt`).
2. De-duplicate against the 123-record corpus (DOI first, then normalised
   title — `verify/boolean_recall.py` does exactly this, just point its
   `SCOPUS_EXPORT`/`WOS_EXPORT` constants at your new files).
3. Screen genuinely new candidates against the criteria in Table A2
   (`sections/12_appendix.tex`, Appendix A.3).
4. For anything that passes screening, check whether it bears on any of the
   eight open gaps in §9.4 — that judgement is yours, not something to
   infer from a hit count.

A parallel, much looser arXiv-only signal (no Scopus/WoS access available in
this environment) already turned up 27 shortlisted candidates, including a
cluster of 9 on federated/decentralized LoRA specifically — see
`verify/major19_topup_arxiv_candidates.csv`. That's not a substitute for the
above, but it's a reason to expect the Scopus/WoS pass will find something
too, not come back empty.
