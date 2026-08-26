## Meta
- **Citation:** Huang, C. et al. (2023). LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition. *arXiv:2307.13269*.
- **Venue:** Pre-print / Workshop
- **Tags:** LoraHub, LoRA Composition, Cross-Task Generalization, Adapter Routing, Adapter Composition

## Key Findings (from PDF reading — "LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition")
1. LoraHub introduces a cross-task generalization method by dynamically composing LoRA modules: given a few examples from a held-out task, it composes pre-trained LoRA adapters without additional training.
2. Zero-shot transfer: combine LoRA modules trained on different tasks to predict a new unseen task.
3. Two main steps: (a) retrieval — identify relevant pre-existing LoRA adapters via few-shot prompts; (b) composition — weighted averaging of retrieved adapters' weights for new task classification.
4. Achieves performance comparable to full few-shot fine-tuning on unseen tasks.

## Relevance to Thesis (Specifically Mentioned Thesis Gap: §7 Modular MoE + Routing, §4 Adapter Composition)
- Directly relevant to adapter composition: LoraHub selects and composes LoRA adapters dynamically without training.
- Demonstrates task-language ability of combining adapters: a marketplace of various LoRA modules for different tasks can be created.
- Closest prior work to this thesis aim: "plug-and-play" adapter composition for multi-task inference without centralised orchestrator.

## Key Metrics / Results
- Comparable to full-few-shot fine-tuning on BBH/BFL benchmark metrics.
- 73.1% accuracy on BIG-Bench (for select tasks) vs. in-context few-shot ~72%.
- Adapter dynamic composes of averaging weights.

## Limitations / Gaps
- Composition via naive weighted averaging — no routing or gating mechanism.
- Evaluation on classification only — not generative NL tasks studied.
- Does not scale to many tasks: assumes a pool of trained LoRAs for the composition.
- No adaptation to client hardware: requires whole network composition.
- No p2p system integration.

## Relevance to Thesis Sections
- §7.2 Adapter routing for multi-task inference
- §4.5 Adapter composition and merging