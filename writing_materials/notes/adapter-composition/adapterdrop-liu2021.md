## Meta
- **Citation:** Liu, L. et al. (2021). AdaplerDrop: On the Efficiency of Adapters in Transformers.
- **Venue:** EMNLP 2021 (main)
- **Tags:** `adapter-composition` `efficiency` `inference-optimization`
- **Thesis sections:** §4.3 (efficient inference with adapters)

## Key Findings
1. Analyzes the redundancy of adapters across layers -- shows that adapters at middle-to-high Transformer layers contribute less to task performance than early layers.
2. Introduces **AdapterDrop** -- selectively dropping adapters from certain layers (both during training and inference) to reduce computation.
3. Achieves up to 2x speedup with less than 1% performance drop by removing adapters from the middle layers during inference.
4. Dropping adapters during training acts as a regularizer, improving generalization on unseen tasks.
5. Key insight: not all layers equally benefit from adapters; the lower layers closest to input and top layers are the most critical for task performance.

## Composition Method
- Starts with adapters in every Transformer layer, then selectively removes them from certain layers.
- This is a pruning/sparsity approach rather than a composition method per se -- it focuses on efficiency of individual adapters rather than combining multiple adapters.

## Relevance to Thesis
- Relevant to the efficiency aspect of adapter composition: dropping adapters selectively can reduce overhead in a multi-adapter serving scenario.
- Implications for decentralized serving: lightweight adapters can be prioritized and only served from critical layers, reducing bandwidth requirements.

## Limitations / Gaps
- AdapterDrop is morphology-based (redundancy reduction) rather than a composition mechanism for merging adapters.
- Does not address how adapters from different tasks are combined or selected for inference.
- Evaluated on single-task adaptation, not multi-adapter composition scenarios.