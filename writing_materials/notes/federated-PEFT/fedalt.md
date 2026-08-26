---
citation: "FedALT: Federated Fine-Tuning through Adaptive Local Training." ArXiv, 2025.
tags:
  - federated-PEFT
  - adaptive-training
thesis-sections: §6.2
tier: 2
paper-key: fedalt
---

## Meta
- **Full citation:** "FedALT: Federated Fine-Tuning through Adaptive Local Training," arXiv preprint arXiv:2503.11880, 2025.
- **Venue:** ArXiv 2025
- **Tags:** `federated-PEFT` `adaptive-training`
- **Thesis sections:** §6.2

## Key Findings
1. Proposes adaptive local training — clients dynamically choose between training adapters (global) or personalizing (local) based on gradient diversity.
2. Adaptive training schedule changes depending on convergence.

## Methodology
- **Approach:** Per-step gradient diversity metric: client alternates between training LoRA or training without LoRA for extra client-specific feature.

## Results / Metrics
- Accuracy increase from personalized knowledge.

## Limitations / Gaps
- Central server.
- Overhead of gradient diversity calculation.

## Federation / Peer-to-Peer Approach
- Centralized.

## Relevance to Thesis
- Important to exploring per-personalisation in P2P: each peer independently decides whether to specialize or contribute to the global knowledge.
- In a P2P marketplace, each peer could decide when to share adapters.

## Limitations / Gaps (continued)
- No robustness or privacy. Heterogeneous model quantisation not addressed.