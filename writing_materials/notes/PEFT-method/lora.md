## Meta
- **Citation:** Hu, E., et al. (2022). LoRA: Low-Rank Adaptation of Large Language Models. *ICLR*.
- **Venue:** ICLR
- **Tags:** LoRA, PEFT, Fine-tuning, Low-Rank, LLMs
- **Thesis sections:** §4.2 LoRA, §4.6.1 Adapter Weight Composition and Fusion

## Key Findings
1. Fine-tune by adding low-rank decomposition (A, B) to query/value layers of pre-trained transformer; A and B are hyperfine small weight matrices such that W' = W + BA.
2. Only rank r (typically 1-16) matrices A and B added per layer; r = 4 for Q values can match full fine-tune (r equivalent to adapt size ~1%).
3. No inference latency change when merging the trained weights: LoRA update added to W for serve, freeze base weights.
4. LoRA is rank required to match fine-tune quality NLL curves — Full W is near-optimal.
5. Best configuration: adapt attention weights only (Q and V projection combination).
6. Multi-task solutions: train multiple LoRA wr/Wr for different tasks and choose at inference time without memory cost.
7. Can train concatenated LoRA for multi-task — pick task-specific during inference.
8. LoRA is orthogonal to no other classes of PEFT — adapters, prefix, prompt tuning, low-rank adaptation vary.

## Relevance to Thesis
- LoRA is the most widely adopted PEFT method for LLMs. The paper's demonstration of "task-specific adapters selected at inference time" directly maps to the adapter marketplace.
- No added inference latency when switching between task adapters: key requirement for multi-tenancy of P2P.
- Multi-task LoRA concept (training separate LoRAs, picking best at inference) directly mirrors per-task adapter marketplace.

## Limitations / Gaps
- Sample dimension of pre-trained model rank remains small but SVD of gradient vs fine-tune update shows it is low-rank constrained to specific layers.
- Performance sweet spot r = 4 — but rank must be tuned for specific task/dataset.
- No support for inter-task LoRA specialization: each one separate — do not model shared knowledge between them.
- Cannot model full update to LoRA fine-tune: some tasks cannot be modeled with low-rank structure.