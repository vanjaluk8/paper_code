## Meta
- **Citation:** Aghajanyan, A., Zettlemoyer, L., & Gupta, S. (2021). Low Rank Adaptation Enables Efficient Domain Transfer In Billion Parameter Language Models. *LoRA Paper Predecessor*.
- **Venue:** ICML 2021
- **Tags:** PEFT, Low-Rank Adaptation, Domain Transfer, Billion Parameter LMs
- **Thesis sections:** §4.2 LoRA, §4.3 Low-Rank Methods

## Key Findings
1. Proposes low-rank updates to pre-trained transformers: fine-tune only a low-rank decomposition (rank-r matrices).
2. Directly enables domain transfer for billion-parameter LMs (T5, GPT-like) across many NLP tasks.
3. Shows that pretrained features are so expressive that the domain-specific "task-specific" update required is low rank.
4. Reduces trainable parameter count to 0.01% of full fine-tune.
5. Connects LoRA adaptation directly to the insight that the gradient update lies in a low-rank space — existing pre-trained weights are near-optimal already.

## Relevance to Thesis
- Confirms that low-rank adaptation works for billion-parameter LLMs.
- Establishes the theoretical foundation for adapter-based systems — small parameter changes suffice.
- Positive evidence for cheap adapter storage and fast transfer across users — adapters are lightweight, shareable.

## Limitations / Gaps
- Does not study the characteristics of the space of adapters themselves.
- Gives upper bound of rank < 5 indicates rank 1 likely sufficient.
- No analysis of mixing/subtraction operations of adapters across domains.