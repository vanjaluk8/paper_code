## Meta
- **Citation:** (2022). Memory Efficient Continual Learning with Transformers (arXiv: 2203.04640v2)
- **Venue:** Pre-print (NeurIPS 2022?)
- **Tags:** `adapter-composition` `continual-learning` `PEFT`
- **Thesis sections:** §4.3 (continual PEFT), §6 (federated PEFT)

## Key Findings
1. Combines adapters with memory replay to address catastrophic forgetting in continual learning tasks.
2. Proposes a memory buffer of previous task data used to replay when training new tasks with adapters.
3. Adapters prevent interference across tasks by isolating task-specific parameters in the adapter modules instead of in base model weights.
4. Does not rely on task-ID at inference time unlike prior continual learning methods.
5. Outperforms prior experience replay methods.

## Composition Method
- Each task gets a separate set of adapters stored in memory.
- A shared encoder is frozen across tasks, so adapters learn orthogonal residual functions.
- No merging or mixing of adapters is performed; each task adapter operates independently on the shared frozen encoder.
- The approach focuses on avoiding forgetting by architectural isolation rather than fusion of modules.

## Relevance to Thesis
- Adapters inherently avoid forgetting by isolating per-task parameters; this validates the intuition behind using adapters in P2P systems where adapters can be pulled from registry and deployed without affecting other tasks.
- Provides indirect support for the modular, non-destructive nature of adapters in continual/decentralized settings.

## Limitations / Gaps
- Not a composition approach -- it avoids composition and relies on isolation of adapters per task.
- Does not consider scenarios where multiple adapters must be composed simultaneously (e.g., task combination).
- Memory buffer approach relies on sampling past data.