## Meta
- **Citation:** Mahabadi, R. K., Henderson, J., & Ruder, S. (2021). HyperFormer: Multi-task Fine-tuning via Shared Hypernetwork. *ACL* / *arXiv:2104.13628*.
- **Venue:** ACL / arXiv 2021
- **Tags:** HyperFormer, Hypernetwork, Multi-task, Adapter, PEFT

## Key Findings
1. HyperFormer generates adapter weights via a shared hypernetwork across tasks, enabling knowledge sharing between tasks.
2. Hypernetwork reduces per-task total parameters vs. independent adapters.
3. HyperFormer is designed for Multi-task Fine-tuning: a lightweight hypernetwork produces adapter weights for all tasks, conditioned on task embedding.
4. This is a form of "modular composition": adapter weights are generated, not trained per task.

## Relevance to Thesis (Specifically Mentioned Thesis Gap: §4.5 Adapter Composition)
- PDF NOT FOUND: this paper was not in the PDF collection.
- Context from existing notes: HyperFormer's hypernetwork approach is a key method for controlled adapter generation. 
- Relevant for thesis §3.4 Advanced PEFT since it demonstrates "weight generation" for adapters via hypernetwork, which can be extended to decentralized adapter composition.

## How to Write for Thesis
- Include HyperFormer as an advanced PEFT method in §3.4 under weight-generated PEFT or hypernetwork-controlled adapter generation.
- Contrast with AdapterFusion approach in §4 where adapters are trained and then combined.
- NOTE: Read the actual paper from the conference proceedings since no PDF is in the collection.

## Relevance to Thesis Sections
- §3.4 Advanced PEFT (HyperFormer)