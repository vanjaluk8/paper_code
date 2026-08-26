# Federated PEFT Notes

This directory contains structured notes from the federated-PEFT PDFs located at:
`writing/slr_methodology_paper/writing_materials/pdfs/federated-PEFT/`

## Papers (22 total)

| # | Paper Key | Full Title | Venue | Notes |
|---|-----------|------------|-------|-------|
| 1 | `fedlora-wireless` | Federated Low-Rank Adaptation for Large Models Fine-Tuning Over Wireless Networks | GLOBECOM 2024 | Done |
| 2 | `dp-fedlora` | DP-FedLoRA: Privacy-Enhanced Federated Fine-Tuning for On-Device LLMs | ICDM 2025 | Done |
| 3 | `fedmcp` | FedMCP: Parameter-Efficient FL with Model-Contrastive Personalization | ICPADS 2024 | Done |
| 4 | `fed-adapter-quant` | Federated Adaptive Fine-Tuning with Heterogeneous Quantization and LoRA | INFOCOM 2025 | Done |
| 5 | `adaptive-peft-heterogeneous` | Adaptive PEFT on Heterogeneous Devices | TMC 2025 | Done |
| 6 | `hetero-tasks-clients-neurips` | Federated Fine-Tuning under Heterogeneous Tasks and Client Resources | NeurIPS 2024 Wkshp | Done |
| 7 | `aggregating-lora` | Aggregating Low Rank Adapters in Federated Fine-Tuning | IEEE FLTA 2024 | Done |
| 8 | `fedpetuning` | FedPETuning: When FL Meets PEFT | ACL 2023 Findings | Done |
| 9 | `hetero-lora-on-device` | Heterogeneous LoRA for On-Device Foundation Models | EMNLP 2024 | Done |
| 10 | `fedex-lora` | FedEx-LoRA: Exact Aggregation for Federated and Efficient Fine-Tuning | ACL 2025 | Done |
| 11 | `towards-federated-lora` | Towards FL Low-Rank Adaptation with Heterogeneous Data | NAACL 2025 | Done |
| 12 | `slora` | SLoRA: Federated PEFT of Language Models | ArXiv 2023 | Done |
| 13 | `improving-lora-privacy` | Improving LoRA in Privacy-preserving FL | ArXiv 2024 | Done |
| 14 | `federa` | FeDeRA: Efficient Fine-tuning of Language Models in FL | ArXiv 2024 | Done |
| 15 | `splitlora` | SplitLoRA: A Split PEFT Framework | ArXiv 2024 | Done |
| 16 | `flora` | FLoRA: Federated Fine-Tuning Large Language Models with Heterogeneous Resources | ArXiv 2024 | Done |
| 17 | `selective-aggregation` | Selective Aggregation for LoRA in FL | ArXiv 2024 | Done |
| 18 | `robust-efficient-lora` | Towards Robust and Efficient FL LoRA with Heterogeneous Clients | ArXiv 2024 | Done |
| 19 | `fedalt` | FedALT: Federated Fine-Tuning through Adaptive Local Training | ArXiv 2025 | Done |
| 20 | `fed-tuning` | Beyond Fine-Tuning: Efficient Fed-Tuning for Mobile/Web Users | ACM 2023 | **UNREAD** — PDF rendering not possible |
| 21 | `fedadapter-mobile` | FedAdapter: Efficient FL for MobileNLP | ACM 2023 | **UNREAD** — PDF rendering not possible |
| 22 | `fedbiot` | FedBiOT: LLM Local Fine-tuning in FL without Full Model | ACM 2024 | **UNREAD** — PDF rendering not possible |

## Notes on Notes Status

- Notes 1–19 are FULL and based on READ content of each PDF. The notes contain: meta, key findings, methodology, federation approach, relevance to the thesis, and limitations/gaps.
- Notes 20–22 are **UNREAD** — these three PDFs could not be rendered on this machine (missing `poppler-utils`/`pdftoppm`). They must be re-processed on a machine with PDF rendering capability.

## Literature Review Gaps Highlighted by Notes

### Well-covered topics:
- **FedPETuning (FedPETuning 2023):** Adapter aggregation is viable — forms the foundational work.
- **DP-FedLoRA (DP-fedlora):** How to add differential privacy guarantees to federated LoRA.
- **Federated adaptive finetuning (quantization-based):** How heterogeneous base model quantization doesn't break adapter-only exchanges.
- **FedMCP (FedMCP):** Model-contrastive personalization with adapters.
- **FeDeRA, FLoRA, SLoRA, FedEx-LoRA:** Various aggregation strategies.
- **Selective/Robust aggregation (robust-efficient-lora):** Byzantine resilience for adapter exchange.
- **Wireless federated LoRA (fedlora-wireless):** Wireless practical feasibility.

### Under-explored from thesis perspective:
- **P2P exchange protocol** — no paper proposes a fully decentralized routing/gossip protocol for adapters.
- **No P2P marketplace**: existing works use FL server as central hub.
- **Privacy** is considered only with DP mechanism that assumes central aggregator, not P2P.
- **Security** of adapter sharing is only addressed in robust-aggregation paper (trimmed mean) — but still through server.
- **Federated** and **P2P** are seen as separate fields in current literature.

### Priority gaps for thesis:
1. No work addresses fully decentralized adapter exchange without a central server.
2. No peer scoring/reputation system for selecting quality adapters from unverified sources.
3. No latency/bandwidth evaluation for P2P adapter dissemination.
4. All works test on classification tasks, no generative task results.