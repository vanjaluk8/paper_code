## Meta
- **Citation:** Zhang, Y., et al. (2025). HMI: Hierarchical Knowledge Management for Efficient Multi-Task Adapter Inference. *arXiv:2504.17449*.
- **Venue:** Preprint
- **Tags:** Hierarchical Multi-Task Adapter Inference, PEFT, Adapter Routing, Cache
- **Thesis sections:** §4.6 Adapter Composition, §5.4 Hierarchical Task Selection

## Key Findings
1. HMI: system-level method for managing adapter modules using retrieval of modular adapters by activating only the required adapters per input query.
2. Hierarchical adapter selection — coarse → fine class taxonomy: given a query, first find top relevant adapter categories (via embedding match), then the best specific adapter within that category.
3. Evaluated with 1000 adapter modules (corresponding to 1000 tasks) and a shared frozen backbone (T5-Large).
4. Designed for multi-task adapter serving: the adapter per task is stored independently and selected/deselected per example.
5. Achieves near-oracle accuracy with memory reduction if selecting only 5 adapters at inference vs deploying all 1000 with full model retraining.
6. Router: cross-encoder that predicts best adapter given query embeddings.

## Relevance to Thesis
- **Crucial link**: first work that connects all three elements: adapters, multi-task selection, and system efficiency for realistic multi-task inference.
- Hierarchical routing directly comparable to adapter marketplace routing: adapter type (LoRA vs adapter vs prompt), adapter function (sentiment or generation) → coarse selection -> fine selection.
- System statically allocates peer adapter modules to adapters retrieved from the market.
- Storage-retrieval mechanism transfers to distributed P2P adapter search with hierarchical approach.

## Limitations / Gaps
- Controlled lab evaluation: all adapters stored on a single server (not P2P).
- Router trained separately with meta-embedding — limited generalizability for new adapter creations not in training set.
- Only T-5 Large evaluated — largest model, 820M parameters. Necessity/capacity for larger sizes is unclear.
- Builds on pre-LLM research from specific benchmark (SuperNI, GPTASKCURP) making large multi-task settings.