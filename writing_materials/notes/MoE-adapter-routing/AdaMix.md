## Meta
- **Citation:** Wang et al. (2023) AdaMix: Mixture-of-Adaptations for Parameter-efficient Model Tuning
- **Venue:** ArXiv preprint (October 2022)
- **Tags:** `MoE-routing` `PEFT` `mixture-of-experts` `multi-task`
- **Thesis sections:** §7.x (MoE routing)

## Key Findings
1. AdaMix proposes a mixture-of-adaptations approach that learns to combine/route between multiple PEFT modules (adapters + LoRA) via a learned gating mechanism.
2. The method trains multiple PEFT "experts" and a sparse gating network that selects top-k experts per input token.  
3. Achieves performance comparable to full fine-tuning on GLUE and SuperGLUE with fewer parameters than dense MoE variants.

## Routing / Gating Mechanism
- A learned gating network computes probabilities over PEFT experts (adapter modules or LoRA modules).
- Only the top-k experts are activated per token (sparse gating), reducing inference cost.
- Gating is input-dependent: different tokens may route to different expert modules.

## Relevance to Thesis
- Demonstrates that learned gating of multiple PEFT modules is effective for multi-task adaptation without full fine-tuning.
- Directly relevant to the question of how to combine adapter modules selectively in a multi-task setting.

## Limitations / Gaps
- Still uses a centralised gating network (learned router) that requires co-location of all PEFT modules.
- Gating overhead may not be negligible for on-device deployment.