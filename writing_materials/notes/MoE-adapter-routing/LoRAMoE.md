## Meta
- **Citation:** Chen et al. (2024) LoRAMoE: Alleviating World Knowledge Forgetting in Large Language Models via MoE
- **Venue:** ACL 2024
- **Tags:** `MoE-routing` `world-knowledge` `LoRA` `forgetting`
- **Thesis sections:** §7.x (MoE routing)

## Key Findings
1. LoRAMoE addresses world knowledge forgetting in LLMs by freezing the backbone and routing to domain-specific LoRA experts.
2. The system uses a "Mixture-of-Experts" setup where each LoRA captures different domain knowledge, and the router selects experts based on input context.
3. LoRAMoE outperforms standard adapting on world knowledge benchmarks without catastrophic forgetting.

## Routing / Gating Mechanism
- Uses a sparse MoE gating mechanism: a router network computes scores over LoRA experts, selecting top-k.
- Router is trained jointly with LoRA modules; gradients flow only through selected experts.
- For token-level routing, each token may select a different subset of LoRA experts.

## Relevance to Thesis
- Directly relevant as a PEFT + MoE approach that combines multiple adapters wwith input-dependent routing.
- Shows how to maintain diverse expertise without retraining the entire model.

## Limitations / Gaps
- Centralised router remains a single point of coordination.
- Top-k routing can lead to expert imbalance and reduced capacity utilisation.