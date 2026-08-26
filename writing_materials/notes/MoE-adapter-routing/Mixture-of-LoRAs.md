## Meta
- **Citation:** Chen et al. (2024) Mixture-of-LoRAs: An Efficient Multitask Tuning Method
- **Venue:** ArXiv preprint (March 2024)
- **Tags:** `MoE-routing` `LoRA` `multitask`
- **Thesis sections:** §7.x (MoE routing)

## Key Findings
1. Proposes Mixture-of-LoRAs (MoE-LoRA) as a method for multi-task tuning that uses a shared base model with multiple LoRA modules and a soft router.
2. The router adaptively selects LoRA weights based on task ID, allowing a single model to serve multiple fine-tuned tasks simultaneously.
3. Achieves comparable or better performance than per-task fine-tuned models without needing per-task copies of the full model.

## Routing / Gating Mechanism
- A learned gating network computes task-expert alignment; each task selects its own set of LoRA experts.
- Routing is still token-level inside the MoE layer in some configurations.
- The router is lightweight and adds minimal latency.

## Relevance to Thesis
- Directly relevant to selecting adapters/routers for different tasks in a P2P multi-adapter system.
- Could inspire task-aware routing across peers.

## Limitations / Gaps
- Assumes discrete tasks wwith task IDs — does not handle open-ended, streaming tasks without predefined IDs.
- Centralised learning of both expert weights and router.