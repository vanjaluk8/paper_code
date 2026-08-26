---
citation: Babakniya et al. "SLoRA: Federated Parameter-Efficient Fine-Tuning of Language Models." ArXiv, 2023.
tags:
  - federated-PEFT
  - SLoRA
thesis-sections: §6.2, §6.3
tier: 1
paper-key: slora
---

## Meta
- **Full citation:** S. Babakniya et al., "SLoRA: Federated Parameter-Efficient Fine-Tuning of Language Models," arXiv preprint arXiv:2308.06522, 2023.
- **Venue:** ArXiv 2023
- **Tags:** `federated-PEFT` `SLoRA`
- **Thesis sections:** §6.2, §6.3

## Key Findings
1. Proposes SLoRA — a framework combining sparse and low-rank adaptation for FL.
2. Clients can train LoRA with different ranks according to their resource budgets.
3. Server aggregates by truncation and padding to unify sparse matrices.

## Methodology
- **Approach:** Sparse low-rank model — each client trains LoRA with different sparsity and rank structure. Server aggregates by handling sparse updates.
- **Base model:** RoBERTa, Llama (small).
- **Aggregation:** FedAvg with sparsity awareness — pruning small singular values and re-padding.

## Results / Metrics
- Up to 2x faster convergence.
- Reduces communication by 50% compared to dense FedLoRA.

## Limitations / Gaps
- Complexity of sparsity processing.

## Federation / Peer-to-Peer Approach
- Centralized aggregation

## Relevance to Thesis
- Very relevant: sparsity in LoRA could help in P2P exchange, where only meaningful LoRA components are transmitted. In a P2P marketplace, peers could share sparse (compressed) adapters.
- Suggests that adapters can be pruned per peer, useful for reputation-weighted communication.

## Limitations / Gaps (continued)
- Centralized processing.
- Additional server overhead due to sparse handling.