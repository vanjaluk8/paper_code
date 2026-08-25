# Decentralised Adapter-Based LLM Inference: A Systematic Literature Review

> **Full title:** *Decentralised Adapter-Based LLM Inference: A Systematic Literature Review — Mapping the Research Gap at the Intersection of PEFT, P2P Systems, and Multi-Task Serving*
>
> **Author:** Vanja Luk  
> **Institution:** University of Rijeka, Faculty of Informatics and Digital Technologies  
> **Programme:** Doctoral Study Programme in Informatics  
> **Course:** Scientific Research Methodology  
> **Supervisor:** Prof. Sanda Martinčić-Ipšić  
> **Date:** May 2026

***

## Overview

This repository contains the full LaTeX source of a systematic literature review (SLR) written as a doctoral-level research methodology coursework. The review investigates whether a **peer-to-peer (P2P) adapter-based inference** paradigm is theoretically grounded and practically motivated: can lightweight, task-specific adapters be discovered, retrieved, composed, and served across autonomous nodes — each hosting a shared frozen backbone — without any central coordinator?

Following **PRISMA 2020**, **Wohlin (2014) snowballing**, and **Xiao & Watson (2019)**, the review surveys **123 papers** across five thematic clusters. The central finding is that no existing system simultaneously addresses all seven critical dimensions of a fully decentralised adapter serving framework, leaving a structured and empirically unexplored research direction.

***

## Research Question

> *Can lightweight, task-specific adapters be discovered, retrieved, composed, and served across autonomous nodes — each hosting a shared frozen backbone — without any central coordinator?*

The review establishes that the answer is **not yet addressed** by existing literature. The combination of frozen backbone, adapter-level P2P exchange, decentralised discovery, multi-task fusion, and absence of a central coordinator constitutes a coherent but unexplored research direction.

***

## Repository Structure

```
fidit_slr/
├── main.tex                        # Root LaTeX document (entry point)
├── bibliography.bib                # BibTeX bibliography (~123 references)
├── figures/                        # Figures directory (PDFs, SVGs)
│   └── fig_gap_quadrant.pdf        # Four-quadrant gap taxonomy figure
└── sections/                       # Modular LaTeX section files
    ├── 00_abstract.tex             # Abstract and keywords
    ├── 01_introduction.tex         # Introduction and research question
    ├── 02_background.tex           # Background and conceptual framework
    ├── 03_methodology.tex          # SLR methodology (PRISMA, snowballing)
    ├── 04_peft.tex                 # PEFT and adapter techniques (G0–G1)
    ├── 05_adapter_composition.tex  # Adapter composition and fusion (G2)
    ├── 06_inference_systems.tex    # LLM inference serving systems (G4)
    ├── 07_moe_routing.tex          # Mixture-of-Experts and routing (G5)
    ├── 08_p2p_federated.tex        # P2P and federated learning (G3, G6)
    ├── 09_synthesis_gap.tex        # Synthesis, concept matrix, gap analysis
    ├── 10_poc.tex                  # Proof-of-concept design (NL-to-SQL) <- not used for SLR
    ├── 11_conclusion.tex           # Conclusions and limitations
    └── 12_appendix.tex             # Appendix (search strings, PRISMA flow, etc.)
```

***

## Document Sections

| # | File | Content |
|---|------|---------|
| 0 | `00_abstract.tex` | Abstract + keywords |
| 1 | `01_introduction.tex` | Motivation, research question, scope |
| 2 | `02_background.tex` | Transformer adapters, PEFT taxonomy, P2P foundations |
| 3 | `03_methodology.tex` | PRISMA 2020 protocol, Wohlin snowballing, inclusion/exclusion criteria, corpus assembly |
| 4 | `04_peft.tex` | Houlsby adapters, LoRA, QLoRA, prefix tuning, sparse adapters |
| 5 | `05_adapter_composition.tex` | AdapterFusion, LoraHub, LoraRetriever, multi-task composition |
| 6 | `06_inference_systems.tex` | S-LoRA, Punica, CaraServe, Petals, multi-tenant serving |
| 7 | `07_moe_routing.tex` | Switch Transformers, Adapter-X, MoE Expert Choice, sparse routing |
| 8 | `08_p2p_federated.tex` | FedPETuning, DP-FedLoRA, FLoRA, Petals, Šajina MT-EF, gossip protocols |
| 9 | `09_synthesis_gap.tex` | **Core contribution** — 7-dimension concept matrix, four-quadrant gap map |
| 10 | `10_poc.tex` | PoC: three modular adapters for NL-to-SQL on MIMIC-III / TREQS  <- not used for SLR |
| 11 | `11_conclusion.tex` | Summary of findings, limitations, future directions |
| 12 | `12_appendix.tex` | Search strings, PRISMA flow diagram, snowballing trace, full corpus |

***

## Methodology

The review follows three complementary protocols:

- **PRISMA 2020** — Transparent reporting of systematic reviews; inclusion/exclusion criteria applied to database search results.
- **Wohlin (2014) snowballing** — Forward and backward citation chaining to expand corpus coverage beyond database queries.
- **Xiao & Watson (2019)** — Guidance on qualitative synthesis and gap identification in IS/CS literature reviews.

**Databases searched:** ACL Anthology, arXiv, Semantic Scholar, IEEE Xplore, ACM DL  
**Final corpus:** 123 papers (2017–2026)  
**Thematic clusters:** PEFT, Adapter Composition, Inference Systems, MoE Routing, P2P & Federated Learning

***

## Key Contribution: Seven-Dimension Concept Matrix

The synthesis chapter (`09_synthesis_gap.tex`) introduces an analytical framework comparing 17 major systems against **seven binary design dimensions**:

| Dimension | Description |
|-----------|-------------|
| **Frozen backbone** | Shared base model parameters are never modified |
| **Adapter exchange** | Adapters can be shared/transferred between nodes |
| **P2P topology** | No central server; peers communicate directly |
| **Discovery** | Capability-level adapter lookup without a registry |
| **Multi-task fusion** | Multiple adapters composed at inference time |
| **Privacy/DP** | Differential privacy or isolation guarantees |
| **No central coordinator** | Fully decentralised orchestration |

No reviewed system satisfies all seven dimensions simultaneously. The gap analysis classifies open problems into **four quadrants**: Conceptual, Algorithmic, Systems, and Empirical.

***

## Identified Research Gaps

### Conceptual Gap
No existing work frames adapters as **autonomous, transferable knowledge units** with identity, provenance, and capability description in a P2P context. This gap is the prerequisite for all algorithmic and systems work.

### Algorithmic Gaps
1. **Adapter discovery protocol** — No protocol for locating task-relevant adapters across a P2P network without a central registry (DHT-based capability-level lookup is unexplored).
2. **Capability embeddings** — No method derives compact, data-free representations of adapter functionality from weights alone.
3. **Behavioural fingerprints** — No probe-set method provides functional adapter descriptors robust to distribution shift.

### Systems Gaps
1. **P2P adapter exchange architecture** — No reviewed architecture addresses adapter exchange across autonomous nodes.
2. **Gossip-based metadata dissemination** — No gossip protocol studied for adapter metadata propagation under realistic peer churn.

### Empirical Gaps
1. **Reuse quality bounds** — No formal bounds on adapter reuse degradation as a function of distribution distance and adapter rank.
2. **Decentralised fusion** — AdapterFusion's centralised training step is incompatible with P2P; probe-based alternatives are unstudied.

***

## Proof-of-Concept Design

Section `10_poc.tex` outlines a PoC for the thesis's immediate scope (D1-sql):

- **Task:** Natural language to SQL generation on clinical/medical data
- **Dataset:** MIMIC-III / TREQS NLQ–SQL pairs
- **Base model:** Single frozen transformer (T5 or BERT-class)
- **Adapters:**
  - Adapter A1 — Clinical entity extraction
  - Adapter A2 — Schema mapping
  - Adapter A3 — NL-to-SQL generation
- **Evaluation metrics:** Execution accuracy, query consistency, inference cost

This PoC intentionally defers P2P orchestration, privacy, and production-level distribution to future work.

***

## Related Work Groups

The review organises the literature into six groups (used throughout the document):

| Group | Theme | Representative Works |
|-------|-------|---------------------|
| **G0** | Foundational PEFT | Houlsby (2019), Hu/LoRA (2021), Pfeiffer/AdapterHub (2020), Šajina P2P (2021/2024), Borzunov/Petals (2023), Sheng/S-LoRA (2024) |
| **G1** | Advanced PEFT | HyperFormer, QLoRA, Prefix Tuning, Sparse Adapters, BitFit |
| **G2** | Multi-task composition | AdapterFusion, LoraHub, LoraRetriever, Multi-Query Transformer |
| **G3** | P2P / Distributed | Chaudhari (2024), Gupta FL P2P (2023), DFaaS, EdgeServe |
| **G4** | Inference systems | S-LoRA, Petals, dynamic LoRA loading, CaraServe |
| **G5** | Routing / MoE | Switch Transformers (Fedus 2022), Adapter-X (Li 2024), Expert Choice (Zhou 2022) |
| **G6** | Federated / Privacy | FedAvg, FedProx, pFedMMA, FLamby, FedPETuning, DP-FedLoRA |

***

## How to Build

**Requirements:** A full TeX distribution (TeX Live 2023+ or MiKTeX), `latexmk`, `bibtex`/`natbib`, and the `svg` package (requires `Inkscape` in PATH for SVG figures).

```bash
# Clone the repository
git clone https://github.com/vanjaluk8/fidit_slr.git
cd fidit_slr

# Compile (recommended: latexmk for full bibliography resolution)
latexmk -pdf main.tex

# Or manually:
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

The compiled PDF will be output as `main.pdf`.

***

## LaTeX Package Dependencies

| Package | Purpose |
|---------|---------|
| `geometry` | Page layout (A4, 2.5 cm margins) |
| `natbib` | Bibliography (`square, sort, comma, numbers`) with `plainnat` style |
| `hyperref` | Clickable cross-references and hyperlinks |
| `booktabs`, `longtable`, `tabularx`, `multirow` | Tables |
| `graphicx`, `svg` | Figures (PDF/SVG) |
| `subcaption` | Sub-figures |
| `amsmath`, `amssymb` | Mathematical notation |
| `listings` | Code snippets (Bash) |
| `appendix` | Appendix environment |
| `setspace` | 1.5× line spacing |
| `xcolor` | Colour definitions |

***

## Citation

If you reference this work, please cite it as:

```bibtex
@techreport{Luk2026SLR,
  author      = {Luk, Vanja},
  title       = {Decentralised Adapter-Based {LLM} Inference: A Systematic Literature Review},
  institution = {University of Rijeka, Faculty of Informatics and Digital Technologies},
  year        = {2026},
  month       = {May},
  note        = {Doctoral Study Programme in Informatics, Scientific Research Methodology}
}
```

***

## Thesis Context

This SLR constitutes the literature review component of a doctoral thesis on **Decentralised Adapter-Based LLM Systems**. The thesis proposes a peer-to-peer adapter inference framework wherein:

- A single frozen transformer backbone is loaded into RAM on each peer node.
- Lightweight task-specific adapters (LoRA/bottleneck) are stored on distributed nodes.
- Missing adapters are fetched via P2P protocols (DHT, gossip, capability embeddings).
- Adapter fusion (AdapterFusion-style) and Mixture-of-Adapters (MoA) are supported without retraining the base.
- The system targets constrained hardware with low-latency, memory-efficient multi-task inference.

***

## License

This repository contains academic research materials. All rights reserved by the author unless otherwise stated. For reuse or citation, please contact the author or refer to the University of Rijeka's doctoral thesis regulations.
