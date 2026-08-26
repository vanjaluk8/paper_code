## Meta
- **Citation:** Hu, E., et al. (2023). Parameter-efficient fine-tuning of large-scale pre-trained models. *Nature Reviews*.
- **Venue:** Nature Reviews Methods Primers
- **Tags:** PEFT Review, LLM, Adapters, Transfer Learning
- **Thesis sections:** §4 PEFT methods

## Key Findings
1. High-level overview of PEFT methods structured by type: additive adapters, reparameterization (LoRA), prompting methods.
2. Provides guidelines for selecting PEFT method based on scale, resource, data size.
3. Notes the shift from adapters (additive) to low-rank adaptation (LoRA).
4. Under model deployment: uses PEFT to serve multiple tasks from single base.

## Relevance to Thesis
- Strong foundational overview of PEFT to set the context for decentralized adapter serving.
- Adapter selection guideline: memory-heavy tasks require narrow PEFT; larger tasks need small added parameters.
- The "multi-task serving from single base" concept maps directly to P2P adapter market.

## Limitations / Gaps
- Brief coverage of multi-task inference — summary table only.
- No system implementation details.
- Primarily a guidance paper, not a research contribution.