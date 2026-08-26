## Meta
- **Citation:** Ming et al. (2024) MoELoRA: Contrastive Learning Guided Mixture of Experts on Parameter Efficient Fine-Tuning
- **Venue:** ArXiv preprint (February 2024)
- **Tags:** `MoE-routing` `LoRA` `contrastive-learning` `MoELoRA`
- **Thesis sections:** §7.x (MoE routing)

## Key Findings
1. MoELoRA integrates contrastive learning into MoE-LoRA training. Each LoRA expert is regularised to capture disentangled/contrastive features.
2. The router can then select experts based on contrastive signal strength, leading to better specialisation and task-specific routing.
3. Achieves improved few-shot performance compared to non-contrastive MoE-LoRA baselines.

## Routing / Gating Mechanism
- Standard top-k routing but the expert representing contrastive characteristics is computed as part of routing.
- Experts learn to specialise through contrastive loss that encourages orthogonal representations.
- Gating weights reflect semantic similarity between the input and the expert domain.

## Relevance to Thesis
- Provides insights into how expert specialisation can be induced through auxiliary training objectives.
- The contrastive design of expert representation may be applicable to P2P adapter quality estimation.

## Limitations / Gaps
- All experts are trained centrally, limiting applicability to fully decentralised scenarios.
- The contrastive approach adds an extra training objective; may not be trivial to implement in streaming settings.