## Meta
- **Citation:** Fedus, W., Zoph, B., & Shazeer, N. (2022). Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity. *JMLR*.
- **Venue:** JMLR 2022
- **Tags:** Switch Transformers, MoE, Routing, Sparsity, Scaling

## Key Findings
1. Switch Transformers replace dense feedforward layers with sparse MoE — each token selects 1 expert in top-1 routing.
2. Simplifies Top-2 and sparse routing: only one expert per token, same network parameters and activated parameters.
3. Expert capacity buffer: a configurable factor allocates how many tokens per batch can be processed per expert.
4. With a capacity factor >1, routing load is balanced across all available experts.
5. Balanced loss: used to ensure even load across experts.

## Relevance to Thesis (Specifically Mentioned Thesis Gap: §7.1 MoE Routing)
- MoE routing is the foundation for routing gating methods in the thesis.
- Routing to experts can be extended to routing adapters from peers.
- Top-1/top-k routing is the pre-requisite for the thesis §7 M on adapter routing.

## Key Metrics / Results
- 7x pretraining speedup vs. dense baseline.
- 1 expert capacity factor enables stable training.
- 1B to 1T parameter models experiments.

## Limitations / Gaps
- Not designed for adapters — only for dense MoE layers.
- Expert capacity factor is manual and task-dependent.
- Only trained MoE for raw pre-training — not differentially private.

## Relevance to Thesis Sections
- §7.1 MoE Routing Methods