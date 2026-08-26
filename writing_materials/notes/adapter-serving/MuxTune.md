## Meta
- **Citation:** MuxTune: Efficient Multi-Task LLM Fine-Tuning in Multi-Tenant, Heterogeneous Environments (2026)
- **Venue:** arXiv 2026
- **Tags:** `adapter-serving` `lora` `finetuning` `multi-tenant`
- **Thesis sections:** §5.x

## Key Findings
1. MuxTune proposes a shared/programmable LoRA fine-tuning system that mixes training, serving, and adapters for multitask scenarios.
2. Introduces a novel CUDA kernel that fuses fine-tuning and inference for LoRA adapter serving.
3. Achieves up to 2.3x throughput improvement during mixed training/serving workloads.
4. Introduces the idea of "composable adapters" — adapting to tasks through adapter composition.
5. Supports a multi-tenant environment where each tenant fine-tunes their own adapter while benefiting from other tenants' adapters indirectly.

## Relevance to Thesis
- Relevant for the idea of composing adapters from different tenants — relates to the "marketplace" dimension where adapters could be shared/composed in a multi-tenant setting.
- The composable nature of MuxTune's adapters suggests that a future marketplace could support adapter merging/composition by AI models using multiple adapters.
- Shows that fine-tuning multiple adapters simultaneously on one cluster is possible.

## Limitations / Gaps
- All adapters pre-loaded within single cluster — no discovery needed.
- Adapter composition is assumed among known, registered adapters.
- Does not address version tracking, trust, or P2P retrieval.
- Focused on training rather than the discovery/marketplace aspect.