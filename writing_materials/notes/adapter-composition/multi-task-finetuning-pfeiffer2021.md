## Meta
- **Citation:** Pfeiffer, J., Kamath, A., Ruckle, A., Gurevych, I., & Ruder, S. (2021). Parameter-efficient Multi-task Fine-tuning for Transformers.
- **Venue:** ACL 2021
- **Tags:** `adapter-composition` `multi-task` `PEFT`
- **Thesis sections:** §4.2 (multi-task adapter fine-tuning)

## Key Findings
1. Introduces adapters as modular trainable components for multi-task learning -- share across related tasks via hidden state sharing in the shared Transformer.
2. Adapters from multiple tasks are trained simultaneously, with each task having its own classifier head and set of adapters, but the backbone Transformer remains shared and frozen.
3. Achieves multi-task performance comparable to full multi-task fine-tuning at significantly reduced parameter overhead (3.6% of BERT parameters).
4. Shows that adapter-based multi-task learning avoids catastrophic forgetting and preserves per-task performance better than full fine-tuning.

## Composition Method
- Each task gets its own set of adapter parameters, but all tasks share the same frozen Transformer backbone.
- At each layer, hidden representations pass through the adapter for that task.
- No composition across different adapters (stacking, gating, or averaging) -- it is per-task adapter isolation during training.
- The shared backbone enforces implicit parameter sharing across tasks.

## Relevance to Thesis
- Demonstrates that adapters can support multiple tasks without interference -- a key premise of P2P multi-adapter systems.
- The frozen backbone idea is foundational for a P2P model where a single base model serves multiple users/tasks.
- Relevant to §4.2 on multi-task adapter training.

## Limitations / Gaps
- Does not consider composition of independently trained adapters (only jointly trained adapters). No mechanism for merging adapters post-hoc.
- No routing or selection of adapters -- limited to all tasks simultaneously.
- Not applicable to decentralized settings where adapters come from different sources.