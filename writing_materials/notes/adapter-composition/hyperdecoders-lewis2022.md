## Meta
- **Citation:** Lewis, P. et al. (2022). Hyperdecoders: Instance-specific Decoders for Multi-task NLP.
- **Venue:** (Pre-print, arXiv:2203.08304)
- **Tags:** `adapter-composition` `multi-task` `instance-specific`
- **Thesis sections:** §4.3 (hyperdecoders as adapter composition)

## Key Findings
1. Hyperdecoder generates instance-specific decoder parameters (weights and biases) for each sample at inference time, conditioned on input embeddings.
2. A hyperencoder processes task-specific adapters to generate parameters for the output layer.
3. This is a multi-task decoder architecture with adaptive computation that adapts to each sample.
4. Outperforms previous multi-task methods on 29 diverse NLP tasks.

## Composition Method
- For each example, the shared encoder computes embeddings. The hyperdecoder takes these embeddings and generates per-instance decoder parameters.
- Task adapters are independently trained; the hyperdecoder acts as a fusion mechanism.
- Conceptually similar to mixing independent adapters: each task contributes its adapter output but they are combined via the hyperdecoder at the output layer.

## Relevance to Thesis
- Hyperdecoder-based composition is a fusion mechanism of multiple task-specific adapters.
- Relevant to the P2P vision where many task adapters must be combined for a given query from a client -- the hyperdecoder weights adapters dynamically per instance.

## Limitations / Gaps
- The hyperdecoder is trained specific to a fixed set of tasks -- adding new tasks may require retraining it.
- Focused on the decoder head, not on compositional adapter fusion across layers, which is more general.
- Does not address decentralized routing or dynamic composition of adapters at inference.