---
citation: FedMCP: Parameter-Efficient Federated Learning with Model-Contrastive Personalization." IEEE ICPADS, 2024.
tags:
  - federated-PEFT
  - model-contrastive
thesis-sections: §6.1, §6.3
tier: 1
paper-key: fedmcp
---

## Meta
- **Full citation:** FedMCP: Parameter-Efficient Federated Learning with Model-Contrastive Personalization. In Proc. IEEE ICPADS, 2024.
- **Venue:** IEEE ICPADS 2024
- **Tags:** `federated-PEFT` `model-contrastive` `personalization`
- **Thesis sections:** §6.1, §6.3

## Key Findings
1. Proposes FedMCP — combining parameter-efficient adaptation (adapter layers) with model-contrastive learning in federated settings.
2. Contrastive loss ensures each client learns task-distinctive adapters while sharing shared knowledge.
3. Achieves personalized (non-IID) performance improvements on text classification.

## Methodology
- **Approach:** Each client trains adapter layers shared in a server aggregation + contrastive loss on local data and proxies.
- **Base model:** BERT-style transformer with adapter modules.
- **Contrastive objective:** InfoNCE loss applied over client local representations to encourage task-specific personalization.
- **Aggregation of adapters:** FedAvg at the adapter level — shared across clients.

## Results / Metrics
- Outperforms full-model FedAvg in non-IID scenarios with communication efficiency.
- Personalization improved by 5-10% over global FedAdapter on non-IID splits.

## Limitations / Gaps
- Only classification tasks evaluated (text classification).
- Central server required for adapter averaging — not P2P.
- Contrastive component adds computational overhead per client.

## Federation / Peer-to-Peer Approach
- Centralized FL with adapter-level aggregation.
- Introduces model-contrastive learning for better task separation across clients.

## Relevance to Thesis
- Directly in scope — combines PEFT + personalization via adapter layers in federation.
- Strong analogy to P2P if adapter knowledge could be exchanged without central server.
- Demonstrates that adapters can capture task- and client-specific nuances.

## Limitations / Gaps (continued)
- No decentralized aggregation protocol.
- Mismatch between global-lossened shared adapter and heterogeneous client objectives not fully addressed.
- No evaluation on generative LLM tasks.