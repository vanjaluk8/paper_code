# Supplementary Material S4 — Search Prompts, Database Queries, and Search Execution Log

**Manuscript:** *Decentralised Adapter-Based LLM Inference: A Systematic Literature
Review—Mapping the Research Gap at the Intersection of PEFT, P2P Systems, and
Multi-Task Serving*

This file reproduces the content that was Appendices B, C, and D of an earlier
draft (Undermind search prompts, manual database queries, and the full search
execution log). It was moved out of the main manuscript to Supplementary
Material to reduce page count and verbatim-text surface, per peer review.
Appendix A (Detailed Corpus Construction Pipeline) remains in the main
manuscript's appendix. Section references below (e.g. "the manuscript's
§3.1") refer to the main manuscript, not to this file.

---

## B. Undermind Group Search Prompts

The following six prompts were submitted verbatim to Undermind (undermind.ai) to
retrieve candidate papers for Groups G1–G6 of the pre-validated corpus described
in the manuscript's §3.1 (Search Strategy and Corpus). Undermind was used
exclusively for candidate *retrieval*; all inclusion and exclusion decisions were
made by the author through manual assessment of each returned record. The
prompts are reproduced here in their entirety for transparency and
reproducibility.

### B.1 — Group 1: Advanced Adapter Architectures & PEFT Methods

> I am researching parameter-efficient fine-tuning (PEFT) methods for large
> language models, building on the foundational work of Houlsby et al. (2019)
> on bottleneck adapters and Hu et al. (2022) on LoRA (Low-Rank Adaptation). I
> am looking for papers that extend, improve, or propose alternatives to these
> methods, including but not limited to: QLoRA (quantized LoRA), DoRA, IA³,
> prefix tuning, prompt tuning, BitFit, sparse adapters, hypernetwork-based
> adapters (HyperFormer), adapter pruning, rank-adaptive LoRA, VeRA, and methods
> that combine adapters with quantization or knowledge distillation. I am
> specifically interested in works that analyze the expressiveness, rank
> selection, or composability of low-rank and bottleneck adapter modules in
> transformer architectures (encoder-only, decoder-only, and encoder-decoder).
> Please retrieve the most cited and most recent SOTA papers in this space,
> including survey papers beyond Han et al. (2024, TMLR).

### B.2 — Group 2: Multi-Task Learning & Adapter Composition

> I am researching multi-task learning with adapter modules and task
> composition techniques for transformer-based language models, building on
> AdapterFusion (Pfeiffer et al., 2021, EACL) and AdapterHub (Pfeiffer et al.,
> 2020, EMNLP). I want to find papers on: non-destructive composition of
> multiple task-specific adapters, adapter stacking and fusion strategies,
> hypernetwork-based multi-task adapter generation (e.g., HyperFormer,
> HyperFormer++), multi-task adapter routing, knowledge transfer between
> adapters, continual learning with adapters, task arithmetic and model merging
> (e.g., TIES-merging, DARE), and zero-shot or few-shot generalization via
> adapter composition. I am also interested in works comparing centralized
> multi-task fine-tuning with modular adapter-based multi-task approaches.
> Please retrieve the most relevant and highly cited SOTA papers, including
> recent 2023–2025 works.

### B.3 — Group 3: P2P Networks & Decentralised Systems for ML

> I am researching peer-to-peer (P2P) and decentralized distributed systems
> applied to machine learning and deep learning, building on: Petals
> (Borzunov et al., 2022/2023, ACL/NeurIPS) for collaborative LLM inference,
> Šajina et al. (2024, Future Generation Computer Systems) on multi-task P2P
> learning with encoder-only transformers, and Šajina (2021 *[sic; the
> thesis's actual defence year is 2025, per its title page — the prompt text
> is reproduced verbatim as originally submitted to Undermind and is not
> corrected here]*, University of Rijeka doctoral thesis) on peer-to-peer deep
> learning. I am looking for papers on: decentralized model training and
> inference over P2P overlays, gossip-based and DHT-based protocols for model
> or parameter sharing, capability-aware peer discovery in ML networks,
> decentralized federated learning without a central server, split inference
> across heterogeneous edge nodes, bandwidth-aware and latency-aware
> distributed inference, and decentralized model marketplaces. Please also
> include foundational P2P systems papers (Chord, Kademlia, BitTorrent) that
> are relevant to designing distributed ML systems. Retrieve the most relevant
> SOTA papers from 2018–2025.

### B.4 — Group 4: Efficient Inference & Multi-Adapter Serving

> I am researching efficient inference systems for large language models with
> a focus on serving multiple adapters (LoRA or bottleneck) simultaneously
> over a single frozen base model, building on S-LoRA (Sheng et al., 2024,
> MLSys) and Petals (Borzunov et al., 2023). I want to find papers on:
> multi-tenant LLM serving with adapter multiplexing, dynamic adapter loading
> and swapping at inference time, memory-efficient batching strategies for
> adapter inference (e.g., unified paging, continuous batching), KV cache
> management under adapter heterogeneity, model serving on constrained
> hardware (edge devices, commodity GPUs), speculative decoding with
> adapters, pipeline parallelism for adapter-augmented models, and systems
> like vLLM, Punica, AlpaServe, FlexGen, and EdgeServe. I am also interested
> in work on adapter caching, prefetching strategies, and latency-accuracy
> tradeoffs in multi-adapter inference. Please retrieve the most relevant and
> most cited SOTA papers from 2020–2025, prioritizing MLSys, OSDI, EuroSys,
> SOSP, and NSDI venues.

### B.5 — Group 5: Routing & Mixture-of-Experts

> I am researching routing mechanisms and Mixture-of-Experts (MoE)
> architectures applied to transformer models, with a focus on their
> connection to adapter-based and modular multi-task learning. My starting
> point includes AdapterFusion (Pfeiffer et al., 2021) and S-LoRA (Sheng et
> al., 2024). I want to find papers on: sparse MoE routing in transformers
> (Switch Transformer, GShard, GLaM, Mixtral), expert choice routing and load
> balancing strategies (Zhou et al., 2022), soft routing and differentiable
> gating mechanisms, Mixture-of-Adapters (MoA) and MoE applied specifically to
> PEFT/LoRA modules (e.g., MoLoRA, MixLoRA, Adapter-X by Li et al. 2024),
> task-conditioned adapter routing, learned routing without task identity, and
> routing in decentralized or federated settings. I am also interested in
> theoretical analyses of routing stability, collapse, and capacity. Please
> retrieve the most relevant SOTA papers from 2020–2025, including both NLP
> and systems-focused works.

### B.6 — Group 6: Federated Learning & Privacy-Preserving Adaptation

> I am researching federated learning with a focus on privacy-preserving
> fine-tuning and adapter-based personalization for transformer models. I am
> looking for papers that connect to the proposed research on decentralized
> adapter systems. Starting from the general federated learning literature
> (FedAvg by McMahan et al., 2017; FedProx by Li et al., 2020), I want papers
> on: federated fine-tuning of large language models using LoRA or adapter
> modules (e.g., FedPEFT, FedAdapter), personalized federated learning with
> heterogeneous local models (pFedMMA, per-FedAvg), non-IID data
> distributions and their effect on adapter convergence, differential privacy
> in federated adapter training, cross-silo vs. cross-device federated
> learning for NLP, medical and clinical federated learning benchmarks
> (FLamby, MIMIC), communication-efficient federated learning with sparse or
> compressed updates, and split learning with adapter modules. Please
> retrieve the most relevant and most cited SOTA papers from 2017–2025,
> prioritizing works that explicitly address heterogeneous data or privacy
> constraints in adapter or PEFT contexts.

---

## C. Manual Database Search Queries

Scopus (Elsevier) and Web of Science (Clarivate) were queried manually as part
of the snowballing and enrichment stages described in the manuscript's
Appendix A. Ten advanced search queries were executed on each platform; all
twenty are reproduced verbatim below. In Scopus, results were filtered to
journal articles and conference proceedings (`SRCTYPE("j" OR "p")`) with a
`PUBYEAR > y` bound; the WoS queries are Topic-field (`TS=`) searches with an
analogous `PY >= y` bound (the two platforms' year operators differ by one
boundary year). The WoS Starter API was subsequently used in a *post-hoc
enrichment role* only — to append WoS accession numbers and citation counts to
already-retrieved records — and was not a source of new candidates. All raw
result sets from both platforms are archived alongside the `slr_engine`
repository (`exports/scopus/` and `exports/wos/`); access is detailed in the
manuscript's Data Availability statement.

### C.1 Scopus Advanced Search Queries

**Q1 — Core Adapter-Based NLP.**
```
TITLE-ABS-KEY(("adapter" OR "adapters" OR "LoRA" OR "low-rank")
AND ("parameter-efficient" OR "PEFT" OR "parameter efficient")
AND ("NLP" OR "natural language processing" OR "transformer"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2018
```

**Q2 — Multi-Task Learning with Transformers.**
```
TITLE-ABS-KEY((("adapter*" OR "LoRA" OR "parameter-efficient fine-tuning")
AND ("multi-task" OR "multitask" OR "multi-adapter")
AND ("inference" OR "serving" OR "deployment" OR "edge")))
AND SRCTYPE(j OR p)
AND PUBYEAR > 2020
AND NOT TITLE-ABS-KEY(("medical" OR "healthcare" OR "clinical"
    OR "sentiment" OR "recommendation"))
```

**Q3 — Peer-to-Peer & Distributed NLP.**
```
TITLE-ABS-KEY(("peer-to-peer" OR "P2P" OR "decentralized" OR "federated")
AND ("learning" OR "training" OR "inference")
AND ("NLP" OR "natural language" OR "machine learning" OR "deep learning"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2017
```

**Q4 — Adapter Fusion & Dynamic Routing.**
```
TITLE-ABS-KEY(("adapter" OR "adapters")
AND ("fusion" OR "routing" OR "dynamic" OR "mixture-of-experts"
    OR "MoE" OR "gating"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2020
```

**Q5 — Parameter-Efficient Multi-Task Transformers.**
```
TITLE-ABS-KEY(("parameter-efficient" OR "PEFT" OR "efficient adaptation")
AND ("multi-task" OR "multitask")
AND ("transformer" OR "pre-trained models"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2019
```

**Q6 — Modular Inference & Task Switching.**
```
TITLE-ABS-KEY(("modular" OR "modularity")
AND ("inference" OR "inference time")
AND ("adapter" OR "task-specific" OR "lightweight modules"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2018
```

**Q7 — Agent-Based Collaborative Learning.**
```
TITLE-ABS-KEY(("agent" OR "agents" OR "node" OR "nodes")
AND ("collaborative" OR "collaboration" OR "decentralized")
AND ("deep learning" OR "neural network" OR "model training"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2017
```

**Q8 — NL-to-SQL with Adapters.**
```
TITLE-ABS-KEY(("NL-to-SQL" OR "semantic parsing"
    OR "natural language to SQL")
AND ("adapter" OR "fine-tun*" OR "parameter-efficient" OR "efficient"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2019
```

**Q9 — Sequence Labelling & Token Classification with PEFT.**
```
TITLE-ABS-KEY(("token classification" OR "NER"
    OR "named entity recognition" OR "sequence labeling")
AND ("adapter" OR "LoRA" OR "parameter-efficient" OR "PEFT"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2019
```

**Q10 — Frozen Base Model Paradigm.**
```
TITLE-ABS-KEY(("frozen" OR "freeze" OR "frozen base")
AND ("adapter" OR "efficient" OR "modular")
AND ("transfer learning" OR "fine-tun*"))
AND SRCTYPE("j" OR "p")
AND PUBYEAR > 2018
```

### C.2 Web of Science Advanced Search Queries

**Q1 — Core Adapter-Based NLP.**
```
TS=(("adapter" OR "adapters" OR "LoRA" OR "low-rank")
AND ("parameter-efficient" OR "PEFT" OR "parameter efficient")
AND ("NLP" OR "natural language processing" OR "transformer"))
AND PY >= 2018
```

**Q2 — Multi-Task Adapter Inference.**
```
TS=((("adapter*" OR "LoRA" OR "PEFT")
AND ("multi-task" OR "multitask")
AND ("inference" OR "serving" OR "edge" OR "distributed")))
AND PY >= 2021
AND NOT TS=(("medical" OR "healthcare" OR "sentiment"))
```

**Q3 — Peer-to-Peer Distributed Learning.**
```
TS=(("peer-to-peer" OR "P2P" OR "decentralized" OR "federated")
AND ("learning" OR "training" OR "inference")
AND ("NLP" OR "natural language" OR "machine learning"
    OR "neural network"))
AND PY >= 2017
```

**Q4 — Adapter Fusion & Routing Mechanisms.**
```
TS=(("adapter" OR "adapters")
AND ("fusion" OR "dynamic routing" OR "mixture-of-experts"
    OR "MoE" OR "gating"))
AND PY >= 2020
```

**Q5 — Modular Deep Learning.**
```
TS=(("modular" OR "modularity")
AND ("neural" OR "transformer" OR "deep learning")
AND ("inference" OR "task-specific" OR "lightweight"))
AND PY >= 2018
```

**Q6 — Agent-Based Collaborative ML.**
```
TS=(("agent" OR "agents" OR "distributed node*")
AND ("collaborative" OR "collaboration" OR "decentralized"
    OR "gossip")
AND ("deep learning" OR "machine learning"))
AND PY >= 2017
```

**Q7 — Memory-Efficient Multi-Task NLP.**
```
TS=(("multi-task" OR "multitask")
AND ("memory-efficient" OR "memory efficient"
    OR "parameter-efficient" OR "computational efficient")
AND ("NLP" OR "natural language" OR "transformer"))
AND PY >= 2018
```

**Q8 — Transfer Learning with Task Adaptation.**
```
TS=(("transfer learning" OR "fine-tun*")
AND ("adapter" OR "parameter-efficient" OR "LoRA")
AND ("NLP" OR "text" OR "language"))
AND PY >= 2019
```

**Q9 — Sequence Task Learning.**
```
TS=(("token classification" OR "NER" OR "named entity"
    OR "sequence labeling")
AND ("adapter" OR "fine-tun*" OR "efficient" OR "modular"))
AND PY >= 2019
```

**Q10 — Distributed Inference.**
```
TS=(("distributed" OR "decentralized")
AND ("inference" OR "inference time")
AND ("efficient" OR "modular" OR "lightweight"))
AND PY >= 2018
```

### C.3 Related-Reviews Search (2026-09-10)

A single dedicated query was run on each of Web of Science and Scopus on
2026-09-10 to locate competing secondary studies of overlapping scope (the
manuscript's §3.1, Table 4); ScienceDirect was not searched separately as it
indexes the same Elsevier content surfaced by Scopus. WoS returned 50 records,
Scopus 19; six competing surveys were retained after screening.

**Web of Science.**
```
TS=(("survey" OR "systematic review" OR "literature review"
     OR "overview" OR "taxonomy" OR "SLR")
AND ("parameter-efficient fine-tuning" OR "PEFT"
     OR "adapter" OR "adapters" OR "LoRA"
     OR "prompt tuning" OR "prefix tuning")
AND ("federated" OR "decentralized" OR "decentralised"
     OR "peer-to-peer" OR "P2P" OR "distributed"
     OR "multi-task serving" OR "modular"
     OR "mixture-of-experts" OR "mixture of experts"))
AND PY=2021-2026
```

**Scopus.**
```
TITLE-ABS-KEY(("survey" OR "systematic review"
     OR "literature review" OR "SLR")
AND ("parameter-efficient" OR "PEFT" OR "LoRA"
     OR "adapter" OR "prompt tuning")
AND ("federated" OR "decentralized" OR "peer-to-peer"
     OR "distributed" OR "modular" OR "mixture-of-experts"))
AND DOCTYPE(re) AND PUBYEAR > 2020
```

### C.4 Disconfirming (Adversarial) Search (2026-09-10)

To test the gap claim of the manuscript's §9 against sources outside the
peer-reviewed corpus, a structured disconfirming search was run on
2026-09-10 following the grey-literature / multivocal-review guidelines of
Garousi et al. (2019). Eight queries were issued across arXiv (abstract and
full-text fields), GitHub (repositories and code), and general web search,
with no peer-review, venue, or document-type filter:

1. decentralized LoRA adapter marketplace exchange peer-to-peer LLM
2. "adapter" OR "LoRA" peer-to-peer discovery routing "without a central" server capability
3. github decentralized LoRA adapter sharing network gossip DHT language model
4. Bittensor subnet LoRA adapter fine-tuning marketplace incentive
5. peer-to-peer adapter exchange frozen backbone adapter discovery composition decentralized inference
6. "Platformless AI" decentralized model adapter serving
7. decentralized adapter repository hub retrieval composition multiple LoRA peers no coordinator
8. gossip protocol OR DHT adapter capability discovery LLM peer nodes serving

**Screening rule.** A hit was recorded as a candidate disconfirming artefact
if it described a system, protocol, or running project (peer-reviewed,
preprint, blog, or code repository) combining (i) task-specific adapters or
LoRA as the unit of exchange with (ii) a peer-to-peer or server-free
topology; for each, it was further noted whether it provides adapter-level
*discovery* (locating a capability without a central registry) and
*composition*.

**Result.** No located artefact satisfied all four properties (table below);
each candidate covers a single facet. The two industry projects named in the
manuscript's §10.3 (Bittensor, Platformless AI) were re-confirmed as
non-matching: both operate at whole-model granularity with a central
artefact store (a model hub or on-chain metadata), and neither publishes an
adapter-level discovery or composition protocol. The gap claim of the
manuscript's §9 therefore stands on a documented rather than informal basis.

**Table C.4.1 — Disconfirming-search results grouped by category (2026-09-10).**
Unit = adapters/LoRA are the exchanged object; P2P = coordinator-free
topology; Disc. = registry-free capability discovery; Comp. = multi-adapter
composition. ✓ = yes; ○ = partial; blank = no. No row satisfies all four.

| Category | What it is | Unit | P2P | Disc. | Comp. |
|---|---|:-:|:-:|:-:|:-:|
| Decentralised whole-model serving | P2P serving of whole models or KV-cache, not adapters | | ✓ | ○ | |
| Decentralised market for fine-tuned models | Incentivised training market; artefacts hosted centrally | | ○ | | |
| Decentralised co-training of one shared adapter | Gossip-averaged updates to a *single* adapter | ○ | ✓ | | |
| Centralised adapter retrieval + composition | Retrieve-then-merge from a central pool / registry | ✓ | | ○ | ✓ |
| Registry-based adapter hubs | Centralised multi-tenant registries | ✓ | | ○ | ✓ |
| DHT capability discovery for agents | DHT keys map capability paths; for agents/services, not adapters | | ✓ | ✓ | |

*Representative artefacts:* whole-model serving — Platformless AI, PlanetServe
(arXiv:2504.20101), P2P prefix-cache serving (arXiv:2606.17059);
model-training market — Bittensor finetuning-subnet, arXiv:2506.07940;
co-training one adapter — Dec-LoRA (Ghiasvand et al.), arXiv:2511.18291,
arXiv:2606.22878; retrieval + composition — LoraRetriever (Zhao et al.),
arXiv:2605.01429, arXiv:2602.21222; adapter hubs — AdapterHub (Pfeiffer et
al.), HuggingFace adapters; DHT for agents — arXiv:2601.14567.

### C.5 Post-Review Top-Up Search (2026-09-12)

In response to peer review, a supplementary search checked for literature
published after the primary search's cutoff (the manuscript's §3.1). It
reused the same twenty Scopus/WoS queries of §§C.1–C.2 above verbatim, with
only the year bound advanced to admit the gap window (Scopus:
`PUBYEAR > 2025`; WoS: `PY >= 2026`), plus six new thematic queries run
against arXiv for the same window (2026-05-13 to 2026-09-12) — arXiv's query
syntax is not compatible with Scopus/WoS's Boolean strings, and served as the
only source directly reachable from the environment that ran this stage.

**arXiv queries (all `abs:` field searches).**

1. (adapter OR LoRA OR "low-rank adaptation") AND ("parameter-efficient" OR PEFT) AND (NLP OR "language model" OR transformer)
2. (adapter OR LoRA OR "parameter-efficient fine-tuning") AND ("multi-task" OR multitask OR "multi-adapter") AND (inference OR serving OR deployment)
3. ("peer-to-peer" OR P2P OR decentralized OR decentralised OR federated) AND (learning OR training OR inference) AND ("language model" OR NLP OR "deep learning")
4. (adapter OR adapters) AND (fusion OR routing OR "mixture-of-experts" OR MoE OR gating)
5. (modular OR modularity) AND (inference) AND (adapter OR "task-specific" OR "lightweight modules")
6. ("frozen" AND (backbone OR "base model")) AND (adapter OR "parameter-efficient")

**Screening and results.** Scopus returned 9,516 raw records (8,724 unique
after dedup by EID/DOI/title), WoS 5,316 raw (4,983 unique after dedup by UT
accession number), and arXiv 481 raw. The same title-level PEFT+scope filter
used at the manuscript's Layer 2 (Appendix A.4) reduced these to 40, 43, and
27 new candidates respectively (one Scopus hit and zero WoS/arXiv hits
duplicated the existing 123-record corpus). Cross-source consolidation gave
93 distinct candidates, 17 of them found independently by both Scopus and
WoS. An abstract-level screen at the same depth as Layer 2's own
topical-relevance read retained 65; all 28 drops shared one pattern — a
title matching the keyword filter but an application domain outside the
review's three themes (medical imaging, industrial/IoT, vision-only,
telecom, bioinformatics, robotics). Author eligibility review of the 65
against the manuscript's Table A2 criteria (I4 applied strictly:
peer-reviewed venue required, since no citation-count check was performed on
the arXiv-only survivors) retained four: DyMerge-LoRA, AdaFuse, TailorLLM,
and DeCAF, cited in the manuscript's Inference Systems, MoE Routing, and
P2P/Federated sections respectively (§3.1). None of the four was put through
Wohlin snowballing, quality appraisal, or discovery-route classification;
they are discussed narratively only and excluded from the 123-record corpus
and every statistic derived from it. Full per-candidate records (all 93,
with screening rationale, eligibility decision, and the author's Keep/Skip
call) are archived in `verify/major19_eligibility_decisions.csv` in the
repository (Data Availability statement).

---

## D. Search Execution Log

This appendix provides a chronological account of every search activity
performed during corpus construction, together with record counts at each
stage (table below). The purpose is to allow full reproduction or audit of
the PRISMA flow by the reader or supervisor. The audited final deliverables
referenced below are version-controlled in the `mdpi_paper_slr` repository
(the curated corpus and per-record pipeline artefacts); see the manuscript's
Data Availability statement for further repository access. The final three
rows (2026-09-12) record a post-review top-up search rather than a stage of
the original PRISMA flow: they are logged here for audit completeness but
their four retained citations are not added to the 123-record corpus, and
the manuscript's PRISMA diagram is unchanged (§3.1).

### D.1 — Search Timeline

**Table D.1.1 — Chronological search log with input and output record counts.**

| Date | Activity | In | Out |
|---|---|---|---|
| 2026-04-14 | Undermind AI-assisted deep search, six group queries G1–G6 (prompts verbatim in §B above); author screened each exported list against the manuscript's §3.2 criteria | 6 queries¹ | 377 exported (ranked lists) |
| 2026-04-14 | Cross-group deduplication of the six G1–G6 exports (priority G0 > G1 > ⋯ > G6); joined with 9 G0 seeds | 377 + 9 | 352 pre-validated (343 from G1–G6) |
| 2026-04-17 | Pre-validated corpus metadata correction (venue names, citation counts; no records added or removed) | 352 | 352 |
| 2026-04-21 | Semantic Scholar API snowball on G0 seeds (backward + forward) | 7 seeds | 1,150 raw |
| 2026-04-21 | Within-snowball deduplication (DOI + SS paper ID) | 1,150 | 972 |
| 2026-04-21 | Title screening (Layer 1: year; Layer 2: keyword; Layer 3: LLM triage) | 972 | 162 INCL, 791 EXCL, 19 UNCERT |
| 2026-04-21 | Merge snowball INCLUDE with 352-paper pre-validated corpus (G0–G6); cross-deduplication | 514 | 502 |
| ≈2026-04-22 | Semantic Scholar / OpenAlex enrichment + topical-relevance filter | 502 | 464 kept; 32 deprioritised; 6 excluded |
| ≈2026-04-28 | Abstract-level review, pass 1 (on the 464 corpus; AI-assisted, human decision) | 464 | 202 KEEP, 169 DEFER, 93 SKIP |
| 2026-04-28/05-02 | Abstract review passes completed across the extended pool (464 + 88 forward snowball records) | 552 | 214 KEEP, 173 DEFER, 165 SKIP |
| 2026-05-02 | Full-text review queue compiled from KEEP and borderline-DEFER records | KEEP/DEFER subset | 387 queued |
| 2026-05-02 | Preliminary data extraction | 387 | 190 extracted |
| 2026-05-08 | Forward citation snowball: Scopus (citing G0) | 106 raw | 74 title-screened in |
| 2026-05-08 | Forward citation snowball: Web of Science (citing G0) | 20 raw | 14 title-screened in |
| 2026-05-08 | Forward snowball records added to abstract review (G_SNOW_F group) | 88 added | 12 KEEP; 4 DEFER; 72 SKIP |
| 2026-05-11 | DOI-based venue validation: Scopus (`M3_scopus_venue`) | 172 DOIs | 172 matched |
| 2026-05-11 | DOI-based venue validation: Web of Science (`M4_wos_venue`) | 125 DOIs | 125 matched |
| 2026-05-12 | Data-extraction top-up with manual Scopus/WoS additions | 190 | 224 extracted (34 top-up) |
| 2026-05-12 | Full-text reading, quality assessment, and final curation (final reading list is the authoritative evidence base) | — | 123 final |
| 2026-09-10 | Related-reviews search: WoS + Scopus, one query each (§C.3 above); screening for competing secondary studies | 50 (WoS) + 19 (Scopus) | 6 competing surveys retained |
| 2026-09-10 | Disconfirming (adversarial) search: 8 queries across arXiv, GitHub, and web, no venue filter (§C.4 above) | 8 queries | 0 matching artefacts; near-misses catalogued |
| 2026-09-12 | Post-review top-up search: 20 reused Scopus/WoS queries (year bound advanced) + 6 new arXiv queries; cross-source dedup and title-level filter (§C.5 above) | 9,516 (Scopus) + 5,316 (WoS) + 481 (arXiv) raw | 93 distinct new candidates after dedup and filtering |
| 2026-09-12 | Top-up abstract-level screen (same depth as manuscript Appendix A.4) | 93 | 65 KEEP, 28 DROP (off-domain) |
| 2026-09-12 | Top-up author eligibility review against the manuscript's Table A2 (I4 applied strictly) | 65 | 4 retained (DyMerge-LoRA, AdaFuse, TailorLLM, DeCAF); *not* added to the 123-record corpus |

¹ Undermind returns a relevance-ranked candidate list, not an exhaustive hit
count; the size of the candidate pool it evaluated per query before the
author's manual selection was not separately retained. The G1–G6 route is
therefore logged from its exported ranked lists (manuscript §10.3).

### D.2 — Automated Citation Snowballing

Citation snowballing was executed programmatically on 2026-04-21 via the
Semantic Scholar Academic Graph API, supplemented by Scopus and ACL
Anthology engines, following a single-wave adaptation of the procedure of
Wohlin (2014) (one forward/backward wave, not iterated to saturation). The
G0 corpus comprises nine seed papers; seven of these were submitted for both
backward (reference list) and forward (citing papers) retrieval via the
Semantic Scholar API. The remaining two seeds were excluded from this
automated pass for documented reasons: the doctoral thesis of Šajina
(University of Rijeka repository object infri:1394) is documented in the
institutional repository rather than an API-indexed DOI, so its record was
incorporated through the pre-validated G0–G6 corpus rather than automated
retrieval; Šajina et al. (2024) was evaluated but excluded because its
forward citations yielded no new usable candidates and its backward
citations substantially overlapped with papers already retrieved through
the other seven seeds. Raw API responses yielded 1,150 candidate records;
after deduplication by DOI and Semantic Scholar paper identifier, 972
unique records entered title screening. Screening decisions are logged in
`log_screening_2026-04-21.json`; per-seed retrieval counts are in
`log_retrieval_2026-04-21.json`.

### D.3 — Forward Citation Snowballing (Scopus and WoS)

On 2026-05-08, a supplementary forward snowball was conducted by manually
querying the Scopus and Web of Science interfaces for papers citing any of
the G0 seed papers. This step retrieved 106 records from Scopus
(`MANUAL_FORWARD_SCOPUS_0805.csv`) and 20 records from WoS
(`M1_forward_wos_2026-05-08.txt`). After manual title screening, 88 records
(74 Scopus + 14 WoS) passed the relevance threshold and were appended to
the abstract review pool under the source group `G_SNOW_F`. These 88
records bypassed the automated enrichment filter and entered the review
directly. Of the 88, 12 were assigned KEEP, 4 were assigned DEFER, and 72
were SKIP at abstract review; the 4 DEFER records were resolved to SKIP in
the final consolidation. None of the 88 `G_SNOW_F` records survived to the
final 123-record list: although the 12 KEEP records entered the full-text
queue (8 reaching data extraction), all were excluded at the eligibility
stage, so the forward branch contributes 0 records to the final list.

### D.4 — Manual Database Cross-Validation

To verify completeness, the ten WoS and ten Scopus advanced queries
documented in §C above were also executed manually against the live
database interfaces. Scopus returned 172 records
(`11_MANUAL_SCOPUS_export_1105.csv`); Web of Science returned 125 records
(`11_MANUAL_WOS_export_1105.txt`).

Cross-referencing the 125 WoS records against the existing merged corpus
revealed that all candidates were already present via the Semantic Scholar
and Scopus retrieval pipeline; zero new candidates were identified from the
WoS manual search. This outcome is consistent with the known indexing
overlap between WoS and Scopus for the PEFT, NLP systems, and distributed
ML literature: Scopus coverage is broader for conference proceedings from
ACL, NeurIPS, ICML, and MLSys venues, which dominate this review's citation
landscape. The WoS manual search therefore served as a coverage cross-check
rather than a source of new records, confirming that the Scopus-dominated
retrieval pipeline achieved comprehensive coverage of the target
literature.

### D.5 — DOI-Based Venue Verification

The batch submitted for venue verification consists of the same 172 Scopus
and 125 WoS records retrieved during the manual cross-validation search
(§D.4 above); this step re-submits those record DOIs to obtain authoritative
venue and citation metadata, rather than drawing a new, independent sample.

Following full-text reading, the DOIs of candidate papers were submitted in
batch to Scopus and WoS to retrieve authoritative venue, publication year,
and citation-count metadata. The Scopus batch returned 172 records
(`M3_scopus_venue_validation_2026-05-11.csv`); the WoS batch returned 125
records (`M4_wos_venue_validation_2026-05-11.txt`). These files served
exclusively as metadata enrichment sources: they appended WoS accession
numbers and confirmed Scopus EIDs to records already in the reading pool,
and were not used to introduce new candidates.

### D.6 — Manual PDF and Venue Check

A subset of candidate papers had been initially downloaded from the arXiv
preprint server. As a final quality step, each arXiv download was manually
checked against Google Scholar, Semantic Scholar, and the ACL Anthology to
determine whether a peer-reviewed published version existed. Where a
published venue was identified and the PDF was publicly accessible, the
preprint was replaced with the official published version and the venue
metadata was updated accordingly. After this step, 18 papers in the final
123-paper reading list retained an arXiv source (`source = ARXIV` in
`13_final_reading_list_2026-05-12.csv`), either because no published version
was found or because the accepted manuscript was not separately accessible.
(This "18" figure reports the *retrieval source*; a separate, narrower
count of 11 records cited in the manuscript's §10.3 reports *venue
status* — records whose current indexed venue remains arXiv and for which
no peer-reviewed published version was identified at any retrieval stage;
see also the manuscript's Appendix A.3 and §10.3 for the related 11-record
venue-status count.) A further 4 records have no source annotation,
reflecting papers added from curated references whose primary retrieval
provenance was not logged in the pipeline output files.

### D.7 — Post-Review Top-Up Search Detail

Full query strings, screening rule, and per-stage counts for the 2026-09-12
post-review top-up search are given in §C.5 above; the corresponding rows
of the D.1 table summarise the same activity. Unlike D.1–D.6, this stage
post-dates the 123-record corpus's final curation (2026-05-12) and its four
retained citations are not part of that corpus: they were not put through
Wohlin snowballing, DOI-based venue validation, or quality appraisal, and
no pipeline CSV/JSON file was modified. The per-candidate audit trail for
all 93 screened records is `verify/major19_eligibility_decisions.csv` in
the repository (Data Availability statement), not the version-controlled
pipeline files referenced in D.1–D.6.
