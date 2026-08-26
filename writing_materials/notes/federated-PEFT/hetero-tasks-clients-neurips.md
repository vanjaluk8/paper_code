---
citation: "Federated Fine-Tuning of Large Language Models under Heterogeneous Tasks and Client Resources." NeurIPS 2024 Workshop.
tags:
  - federated-PEFT
  - task-heterogeneity
thesis-sections: §6.1, §6.2, §6.3
tier: 1
paper-key: hetero-tasks-neurips
---

## Meta
- **Full citation:** "Federated Fine-Tuning of Large Language Models under Heterogeneous Tasks and Client Resources," in Proc. NeurIPS 2024 Workshop on Federated Learning.
- **Venue:** NeurIPS 2024 Workshop
- **Tags:** `federated-PEFT` `task-heterogeneity` `resource-heterogeneity`
- **Thesis sections:** §6.1, §6.2, §6.3

## Key Findings
1. Proposes FED-PEFT framework for federated PEFT LLM fine-tuning across heterogeneous tasks and clients.
2. Clients with diverse resource capabilities train different adapters or LoRA matrices.
3. Server-side knowledge distillation from aggregated adapters to improve precision.

## Methodology
- **Approach:** Server maintains LoRA parameters, clients fine-tune based on data and capabilities.
- **Base model:** LLAMA or similar LLM.
- **Heterogeneity:** Different batch sizes, adapter ranks, and tasks across clients.
- **Aggregation:** Weighted averaging with task-aware weighting (by number of samples).

## Results / Metrics
- Outperforms baseline FedAvg for heterogeneous scenario.
- Knowledge distillation adds overhead.
- Only evaluated with IID-broken scenario.

## Limitations / Gaps
- Limited to centralized FL model (server must aggregate).
- Knowledge distillation step expensive.
- No extension to P2P.

## Federation / Peer-to-Peer Approach
- Centralized server aggregation — the server orchestrates LoRA collection, aggregation, distribution.

## Relevance to Thesis
- Important reference for handling multiple tasks in FL via adapters.
- Highlights how knowledge distillation can be used to compress adapter knowledge — relevant if P2P nodes need to compress adapters for bandwidth.
- Task heterogeneity pattern is similar to our multi-task scenario in P2P adapter marketplace.

## Limitations / Gaps (continued)
- No differential privacy mechanism built-in.
- No Byzantine robustness.
- Limited to specific datasets (text classification).