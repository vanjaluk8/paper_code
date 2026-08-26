## Meta
- **Citation:** Punica: Multi-Tenant LoRA Serving (Chen et al., 2023)
- **Venue:** arXiv 2023 / MLSys 2024
- **Tags:** `adapter-serving` `lora` `multi-tenant` `cuda`
- **Thesis sections:** §5.x

## Key Findings
1. Proposes Punica, a multi-tenant LoRA serving system that enables batching of inference requests with different adapters.
2. Introduces a CUDA kernel (CAttn) that efficiently concatenates different LoRA adapters into a single inference batch.
3. Decouples LoRA computation from the base model, allowing per-request LoRA selection without mixing the base model weights.
4. Achieves near-linear throughput scaling with number of tenants (up to 32 adapters batched together).
5. Positions LoRA as a key enabler of multi-tenant serving — fusible adapter weights for concurrent inference.

## Relevance to Thesis
- Punica is a foundational work for multi-tenant LoRA serving. It shows that LoRA adapters can be simultaneously served for different tenants with minimal overhead.
- Important for the thesis's centralized serving component: Punica shows how to batch adapters on a single server.
- The core limitation for a P2P context: Punica assumes all weights (both base model and adapters) are on the same GPU — unrealistic for P2P.
- The batching technique (concatenating LoRA weights in CUDA kernels) is nevertheless relevant background for understanding how a P2P system might aggregate adapters after retrieving them from peers.

## Limitations / Gaps
- Fully centralized: all adapters must be on the same GPU memory. No adapter transfer mechanism.
- Assumes homogeneous GPU hardware (A100).
- Adapters are pre-loaded before inference — no support for on-demand adapter loading.
- No snappy scheduling algorithm — only batching + CUDA kernel optimization.
- Later works (S-LoRA, CaraServe) supersede Punica in serving efficiency, but Punica established the multi-tenant direction.