## Meta
- **Citation:** An, J., et al. (2025). Evolution of Meta's Llama Models and Parameter-Efficient Fine-tuning. *Preprint*.
- **Venue:** Preprint
- **Tags:** Llama, PEFT, LoRA, Foundation Models
- **Thesis sections:** §2.2 Language Model landscape context, §7.2.1 PEFT methods overview

## Key Findings
1. Comprehensive summary of Llama model evolution (1, 2, 3, 3.1) and PEFT compatibility.
2. Key observation: as base model size increases, PEFT methods (especially LoRA) narrow performance gap with full fine-tuning.
3. For Llama-scale models, adapter modules (<0.1% of base parameters) suffice for most downstream tasks.
4. Evaluates standard PEFT on Llama: LoRA works best for commonsense reasoning tasks, prompt tuning for generation.
5. Multi-task inference scenario notes: separate LoRA weights can be loaded on-demand — minimal memory overhead.

## Relevance to Thesis
- Llama models are the de facto standard for PEFT research — paper provides baseline verification that LoRA adapters of rank 8-64 suffice for Llama-level tasks.
- Multi-task adapters loading instructions directly applicable to P2P adapter marketplace.
- The paper's conclusion that even "tiny" adapters work for Llama supports lightweight adapter transmission in P2P.

## Limitations / Gaps
- Only surveys adapter methods for HQ training, does not consider P2P or decentralized training.
- No adapter selection, routing, or retrieval techniques covered.
- No privacy, security, or incentive aspects surveyed.