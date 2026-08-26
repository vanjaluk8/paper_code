## Meta
- **Citation:** Houlsby, N., et al. (2019). Parameter-Efficient Transfer Learning for NLP. *ICML*.
- **Venue:** ICML
- **Tags:** Adapters, Transfer Learning, NLP, Bottleneck Adapters
- **Thesis sections:** §4.1 Bottleneck Adapters, §4.5 Adapter Architecture

## Key Findings
1. Adapts 3-5% of parameters per new task through bottleneck adapter modules inserted in each transformer layer.
2. Averaging of adapters across tasks is work in progress to have a single architecture adapted for multi-task.
3. Adapter architecture: down-project-large linear -> non-linearity -> up-project.
4. Adapters within each transformer layer: first after attention, second after FFN (layer-norm + adapter).
5. Almost always converges to within 1% of full fine-tune.
6. The number of adapters scales with number of tasks — each task gets its own set (bottleneck and whatnot).

## Relevance to Thesis
- Foundational adapter paper: the architecture under test is the industry-standard.
- Sequential per-task training directly maps to "adapter marketplace" concept where each new task requires one new adapter (weight matrix), independent from others.
- Shows that adapters for individual tasks are cheap but cannot be effectively combined via simple addition — motivates the marketplace concept.

## Limitations / Gaps
- Only two architectures evaluated: T5-Base and BERT-Large — limited scope.
- New adapter must be trained sequentially for each task; no multi-task training.
- Adapter averaging across tasks does not maintain accuracy.
- Adapter merging/reuse across tasks is not addressed.