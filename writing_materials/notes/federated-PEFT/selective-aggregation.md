---
citation: "Selective Aggregation for Low-Rank Adaptation in Federated Learning." ArXiv, 2024.
tags:
  - federated-PEFT
  - selective-aggregation
thesis-sections: §6.3
tier: 2
paper-key: selective-aggregation
---

## Meta
- **Full citation:** "Selective Aggregation for Low-Rank Adaptation in Federated Learning," arXiv preprint arXiv:2410.01463, 2024.
- **Venue:** ArXiv 2024
- **Tags:** `federated-PEFT` `selective-aggregation` `LoRA`
- **Thesis sections:** §6.3

## Key Findings
1. Proposes selective adapter aggregation — not all clients contribute but only top-X selected based on relevance, data importance.
2. Reduces communication.

## Methodology
- **Approach:** Measure similarity of adapter update (cosine similarity) between client update and overall update direction. Select or mask clients.
- **Base model:** RoBERTa.

## Results / Metrics
- 30% communication reduction without sacrificing accuracy.
- Faster convergence.

## Limitations / Gaps
- Only for text classification.
- Device energy not measured.

## Federation / Peer-to-Peer Approach
- Centralized server.

## Relevance to Thesis
- Important for P2P: selective sharing of adapters (by relevance) could be key in P2P — peers could skip low-value adapter exchanges.

## Limitations / Gaps
- Not directly applicable to P2P without modification.