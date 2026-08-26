---
citation: "Adaptive Parameter-Efficient Federated Fine-Tuning on Heterogeneous Devices." IEEE TMC, 2025.
tags:
  - federated-PEFT
  - adaptive
thesis-sections: §6.1, §6.2
tier: 1
paper-key: adaptive-peft-hetero
---

## Meta
- **Full citation:** "Adaptive Parameter-Efficient Federated Fine-Tuning on Heterogeneous Devices," IEEE Trans. Mobile Computing, 2025.
- **Venue:** IEEE TMC 2025
- **Tags:** `federated-PEFT` `adaptive` `heterogeneous-devices`
- **Thesis sections:** §6.1, §6.2

## Key Findings
1. Clients can use different PEFT modules (adapters, prefix tuning, LoRA) based on local resource budgets.
2. An adaptive selection mechanism matches PEFT methods to device capabilities.
3. Reduces non-IID challenges by allowing more expressive adapters for higher capacity clients.

## Methodology
- **Approach:** Clients choose among adapters, LoRA, prefix tuning according to local resource constraints.
- **Base model:** BERT-family (glue tasks)
- **Selection rule:** Client computes resource availability, selects PEFT type accordingly.
- **Aggregation:** Adapters from all clients are aggregated into a global set by the server.

## Results / Metrics
- 2-3% accuracy improvement over single PEFT type across heterogeneous clients.
- Memory usage varies by up to 4x among client types.

## Limitations / Gaps
- Centralized aggregator required.
- Does not scale to larger LLMs (experiments on BERT only).
- No privacy or security analysis.

## Federation / Peer-to-Peer Approach
- Centralized FL with adaptive per-client PEFT.

## Relevance to Thesis
- Supports the concept that clients can be heterogeneous with respect to which adapters they train.
- Informs the type of protocol needed for matching adapters to client capabilities in P2P.

## Limitations / Gaps (continued)
- No decentralized mechanism.
- Only classification tasks considered.
- No constraint on differential privacy or Byzantine resilience.