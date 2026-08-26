---
citation: "FedEx-LoRA: Exact Aggregation for Federated and Efficient Fine-Tuning." ACL 2025.
tags:
  - federated-PEFT
  - exact-aggregation
thesis-sections: §6.2, §6.3
tier: 1
paper-key: fedex-lora
---

## Meta
- **Full citation:** "FedEx-LoRA: Exact Aggregation for Federated and Efficient Fine-Tuning," in Proc. ACL 2025.
- **Venue:** ACL 2025
- **Tags:** `federated-PEFT` `exact-aggregation` `LoRA`
- **Thesis sections:** §6.2, §6.3

## Key Findings
1. LoRA updates are quasi-linear and thus FedAvg of LoRA updates implicitly approximates a global optimum — FedEx-LoRA proposes an exact aggregation method via KKT conditions.
2. Proposes Exact Aggregation that eliminates the need for individual optimization in FL.
3. The approach solves a single global optimization problem on the LoRA manifold at the server side.
4. Achieves significant accuracy gains in IID and non-IID settings compared to standard FedAvg on adapters.

## Methodology
- **Approach:** FL with LoRA — server receives LoRA matrices and solves weighted ERM over the LoRA subspace directly.
- **Base model:** GPT-2 / Llama, evaluated on NLU.
- **Aggregation:** Exact aggregation via solving KKT optimality conditions for low-rank updates.

## Results / Metrics
- Outperforms naive FedAvg of LoRA updates.
- Better convergence speed.

## Limitations / Gaps
- Central server required to compute exact aggregation.
- Computational overhead of optimization at server.

## Federation / Peer-to-Peer Approach
- Centralized. But the concept of "exact aggregation" could inform peer-to-peer gossip-based optimization.

## Relevance to Thesis
- Important to reference — optimal aggregation strategy for adapters.
- In P2P, each node could apply exact aggregation based on neighbor updates.
- Could inform how to weight adapter contributions in a decentralized gradient averaging protocol.

## Limitations / Gaps (continued)
- Does not address Byzantine attacks or P2P communication.
- Large overhead for resource-limited clients if the server became a bottleneck.