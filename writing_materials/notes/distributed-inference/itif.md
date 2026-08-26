## Meta
- **Citation:** Liu, L., et al. (2022). ITIF: Integrated Transformers Inference Framework for Multiple Tenants on GPU. *APSys*.
- **Venue:** APSys
- **Tags:** Multi-Tenant Inference, Transformer Serving, GPU Sharing, Resource Partitioning
- **Thesis sections:** §3.2 Distributed Serving, §3.3.2 Multi-Tenant GPU Management

## Key Findings
1. GPU-serving framework tailored for multi-tenant transformer inference: each tenant (user/task) uses a separate transformer model.
2. Memory sharing across tenants through sub-linear operator sharing.
3. GPU core factorization: partitions compute (columns) among tenants, tenant-specific attention blocks, shared FFN cores across tenants.
4. CPU execution of tuples scheduled when necessary tenant-specific workloads.
5. Up to 70% memory reduction across 8 tenants.

## Relevance to Thesis
- Multi-tenant serving of transformer models directly relates to P2P adapter marketplace: each incoming request is a "tenant" potentially needing a different adapter.
- GPU factorization can partition resources per adapter.

## Limitations / Gaps
- Tenants share architecture but not adapters — pre-existing PEFT adapters not considered.
- Single node only: no P2P interaction — the co-location is CPU-level, not networked.
- Designed for identical model (BERT) across tenants, not dissimilar models at the same time.