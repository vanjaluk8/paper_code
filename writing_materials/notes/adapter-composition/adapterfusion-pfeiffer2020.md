## Meta
- **Citation:** Pfeiffer, J., et al. (2020). AdapterFusion: Non-Destructive Task Composition for Transfer Learning.
- **Venue:** EMNLP 2020 (originally arXiv:2005.00247)
- **Tags:** `adapter-composition` `task-composition` `non-destructive`
- **Thesis sections:** §4.2 (composition of task-specific adapters), §3 (transfer learning)

## Key Findings
1. Proposes **AdapterFusion** as a two-stage approach: (1) train task-specific adapters in isolation (single-task), (2) compose them using a fusion layer that learns to combine independently trained adapters.
2. Fusion layer is a lightweight attention mechanism that weights each task adapter's contribution to the layer output.
3. The composition is parameter-efficient (0.54% additional parameters per new task instead of full fine-tuning).
4. Adapters are non-destructive -- previously trained adapters remain unchanged when new tasks are added.
5. Enables compositional zero-shot transfer: old tasks can be adapted to new ones via existing adapters.

## Composition Method
- At each layer, pre-trained task adapters are all activated. A fusion attention module learns to weight them per layer, enabling flexible combination.
- Task adapters are trained independently (each task gets its own adapter weights).
- Composition is handled by the fusion mechanism: weighted sum of adapter outputs per layer.
- Key difference from MAD-X: the fusion is learned across task adapters, not just sequentially stacking them.

## Relevance to Thesis
- **Highly relevant to adapter composition in a P2P setting: modular, non-destructive, and independent training of adapters aligns perfectly with a decentralized P2P marketplace.**
- The fusion mechanism is the model for how adapters can be combined without destructive interference (no catastrophic forgetting).
- This is the closest precursor work to the adapter composition component of the thesis.

## Limitations / Gaps
- Fusion module is trained after task adapter training -- requires sharing training data for the fusion stage.
- Does not address cold-start composition of novel adapters not seen during training.
- Assumes a central fusion training step -- not fully decentralized.