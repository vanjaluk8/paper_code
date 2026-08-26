## Meta
- **Citation:** S-LoRA: Serving Thousands of Concurrent LoRA Adapters (Chen et al., 2023)
- **Venue:** arXiv 2023 / MLSys 2025
- **Tags:** `adapter-serving` `lora` `scheduling` `memory-management`
- **Thesis sections:** §5.x

## Key Findings
1. S-LoRA scales to thousands of LoRA adapters on a single machine or cluster using Unified Paging — a unified memory pool across GPU and CPU memory.
2. Dynamically loads/unloads LoRA adapter weights between GPU and CPU memory to support far more adapters than fit in GPU memory.
3. Introduces a stateless scheduler that schedules requests based on adapter popularity and memory constraints.
4. Achieves near-zero switching overhead for adapters from CPU to GPU memory.
5. handshakePrevents OOM by prefetching adapters from CPU to GPU memory in the background.

## Relevance to Thesis
- Highly relevant as it addresses the key constraint of previous serving systems (Punica): limited number of GPU-resident adapters.
- S-LoRA introduces tiered memory (GPU-CPU) for adapters which is similar to the tiered memory concept needed in a P2P system, except the second tier is remote RAM rather than CPU RAM.
- The unified paging concept generalizes to P2P: adapters could be fetched from local/peer memory.
- S-LoRA's caches (adapter weights in CPU RAM) parallel a peer-to-peer cache of remote adapters.

## Limitations / Gaps
- All adapters are in the same physical machine's GPU+CPU memory — not distributed across independent peers.
- CPU<->GPU memory bandwidth (~32 GB/s) is far higher than network bandwidth (~1-10 GB/s), so S-LoRA's loading model doesn't translate directly to P2P.
- Assumes all adapters are available locally (on disk or CPU memory) — no network discovery or retrieval cost modeled.
- Does not address adapter provenance, trust, or versioning across different nodes.