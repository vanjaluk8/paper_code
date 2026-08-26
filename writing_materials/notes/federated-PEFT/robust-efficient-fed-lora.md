---
citation: "Towards Robust and Efficient Federated Low-Rank Adaptation with Heterogeneous Clients." ArXiv, 2024.
tags:
  - federated-PEFT
  - robust
thesis-sections: §6.2, §6.3
tier: 2
paper-key: robust-efficient-lora
---

## Meta
- **Full citation:** "Towards Robust and Efficient Federated Low-Rank Adaptation with Heterogeneous Clients," arXiv preprint arXiv:2410.22815, 2024.
- **Venue:** ArXiv 2024
- **Tags:** `federated-PEFT` `robust` `heterogeneous`
- **Thesis sections:** §6.2, §6.3

## Key Findings
1. Proposes robust aggregation for LoRA in FL when some clients are noisy or Byzantine.
2. Employs median-based (trimmed mean) aggregation of LoRA — robustness.

## Methodology
- **Approach:** Subspace aggregation of LoRA matrix entries with robust statistics (median, trimmed mean) to tolerate Byzantine fault.

## Results / Metrics
- Graceful degradation under up to 30% Byzantine clients.

## Limitations / Gaps
- Only IID data evaluated — requiring no change.
- Assumes homogeneous LoRA ranks across clients.

## Federation / Peer-to-Peer Approach
- Centralized robust aggregation.

## Relevance to Thesis
- Directly applicable to P2P if robust aggregation is done by each peer when integrating adapters from other peers.
- Robust statistics could be critical in P2P marketplace where malicious / dishonest peers might share corrupted adapters.

## Limitations / Gaps (continued)
- Only robust aggregation at central point — not gossip-based.