## Meta
- **Citation:** Xu, L., et al. (2025). Parameter-efficient fine-tuning in large language models: a survey. *Artificial Intelligence Review*.
- **Venue:** Artificial Intelligence Review
- **Tags:** PEFT Survey, LLM, Adapters, Prompt Tuning, LoRA
- **Thesis sections:** §4 PEFT methods

## Key Findings
1. Comprehensive survey of all major PEFT methods: LoRA, adapters, prompt tuning, prefix tuning, bias tuning, reparameterization methods.
2. Taxonomy of PEFT approaches across dimensions: resource efficiency, parameter count, task adaptation speed.
3. Cross-task adapter averaging, AdapterFusion, task arithmetic for multi-task inference.
4. Empirical evaluation across GLUE, SuperGLUE, etc.
5. Code release for PEFT implementations.

## Relevance to Thesis
- Directly relevant as a reference for all PEFT methods suitable for decentralization.
- Adapter averaging and fusion techniques (Section 6) directly applicable to routing in marketplace.
- Learning the PEFT landscape is foundation for understanding what can be shared in adapter marketplace.

## Limitations / Gaps
- No coverage of P2P or decentralized systems for PEFT deployment.
- Little guidance on network-level routing across adapters.
- Benchmarks limited to NLP benchmarks (GLUE, SuperGLUE) — no coverage of multi-task inference.