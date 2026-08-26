## Meta
- **Citation:** (2023). Prototype-based HyperAdapter for Sample-Efficient Multi-task Learning.
- **Venue:** Pre-print (arXiv:2310.11670)
- **Tags:** `adapter-composition` `hypernet` `multi-task`
- **Thesis sections:** §4.3, §7.2 (prototype/embedding composition)

## Key Findings
1. Prototype-based HyperAdapter proposes a hypernetwork that generates task-specific adapter weights from a small set of prototype examples (few-shot), enabling sample-efficient adaptation for new tasks.
2. The hypernetwork takes task prototypes (a few labeled examples from the task) and produces the adapter parameters, reducing the need for full fine-tuning or per-task training.
3. Compared to standard multi-task adapters and AdapterFusion, this approach improves GLUE performance while requiring fewer training samples per task.
4. Composition across tasks is implicit: the hypernetwork uses prototype embeddings, enabling zero-shot adaptation to new tasks via prototype similarity search.

## Composition Method
- The hypernetwork takes few prototype embeddings from a given task and synthesizes the adapter weights for that task.
- At inference time for a new batch of examples, it can pick the most similar prototype and generate appropriate adapter weights.
- This enables a form of instance-level adaptive composition.

## Relevance to Thesis
- Prototype-based generation is relevant for generating adapter parameters for many novel tasks in a P2P setting (cold-start or few-shot).
- Similar to hypernetwork-based composition: a central registry of prototype embeddings could be searched for each input.
- Relevant to §7.2 which covers compositional multi-task adapter interaction.

## Limitations / Gaps
- Hypernetwork still needs a training stage across many tasks, which may require a centralized authority.
- Does not discuss how to route queries to the appropriate adapter or how to fuse multiple adapters simultaneously.