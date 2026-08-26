## Meta
- **Citation:** Karimi Mahabadi, R. et al. (2022). HyperPELT: Unified Parameter-Efficient Language Model Tuning.
- **Venue:** (pre-print, updated 2022)
- **Tags:** `adapter-composition` `hypernetwork` `PEFT-unification`
- **Thesis sections:** §4.2 (unified PEFT), §8 (general discussion)

## Key Findings
1. HyperPELT unifies multiple PEFT methods (adapters, prefix tuning, LoRA) under a single hypernetwork that generates module-specific parameters.
2. The hypernetwork takes the task ID and PEFT component type as input and predicts the weight offsets for each method-specific module.
3. Performance matches or exceeds individually trained PEFT methods across GLUE and SuperGLUE tasks.
4. The hypernetwork approach reduces search/discovery costs -- the same trained hypernetwork can generate parameters for any PEFT variant.

## Composition Method
- A single hypernetwork (small MLP) maps a task embedding and a module type embedding to weight offsets for all layers.
- For each task, the generated parameters are plugged into the base model as if individually trained.
- No explicit composition across tasks -- the hypernetwork handles multiple PEFT types, not multiple task adapters.
- In effect, this provides a unified compute graph for generating any PEFT method's parameters from task descriptors.

## Relevance to Thesis
- The hypernetwork generation concept could theoretically scale to generating multiple task adapters on the fly; not directly applicable but conceptually similar to merging adapter parameters at scale.
- More relevant to the idea of a P2P registry that can synthesize adapters from descriptors.

## Limitations / Gaps
- Not a composition approach for merging adapters; it is a generative approach to parameter generation.
- Hypernetwork requires a meta-training phase across tasks, which may not be feasible in a decentralized setting.