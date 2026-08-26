## Meta
- **Citation:** (2024). LoraRetriever: Input-Aware LoRA Retrieval and Composition for Large Language Models.
- **Venue:** Pre-print (arXiv:2402.09997)
- **Tags:** `adapter-composition` `routing` `loRA`
- **Thesis sections:** §7.2 (adapter routing), §5 (PEFT composition)

## Key Findings
1. LoraRetriever retrieves and composes multiple LoRA adapters dynamically based on the input prompt.
2. Architecture: stored candidate LoRA modules with descriptions → retrieval via a shared embedding ↔ description matcher → weighted composition based on attention across the retrieved LoRAs.
3. On compositional task-oriented QA and domain-specific adaptation, it matches/exceeds the best single-adapter performance by retrieving relevant domain/task adapters for each input.
4. Enables zero-shot composition for new combination tasks.

## Composition Method
- LoRA adapter library is indexed via task/domain descriptions mapped to adapters.
- For a given input sequence: embed the input, use it to retrieve the top-k most relevant adapters from the library, and combine them by weighted linear interpolation proportional to their relevance scores (attention scores via LoRA).
- Composition uses a Layer-wise LoRA Composition module that computes mixing weights for each task adapter per layer, thus dynamically supporting multi-task composition at inference time.
- This is the first work to treat composition as *retrieval-based dynamic adapter routing*. This is extremely relevant to P2P systems where adapters must be retrieved from many possible sources.

## Relevance to Thesis
- **Highly relevant**: a direct precursor to our work on P2P adapter marketplace and adapter routing.
- Introduces retrieval-based composition, analogous to a DHT-based retrieval system.
- LoraRetriever's ability to retrieve top-k adapters based on input relevance is closely related to a P2P discovery and composition mechanism.

## Limitations / Gaps
- LoraRetriever selects adapters from a fixed library trained for known tasks; no discovery/registration of adapters.
- Indexing occurs in a centralized registry and does not natively decentralize.
- Relies on descriptions -- while novel, the retrieval task is a simple embedding search and assumes a comprehensive set of descriptions for all tasks.
- No fault-tolerance considered.