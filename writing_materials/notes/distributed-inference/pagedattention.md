## Meta
- **Citation:** Kwon, W., et al. (2023). Efficient Memory Management for Large Language Model Serving with PagedAttention. *SOSP*.
- **Venue:** SOSP
- **Tags:** LLM Serving, Memory Management, Attention, Batch Serving
- **Thesis sections:** §3.1 LLM Inference Serving, §3.3 Memory/Resource Management

## Key Findings
1. KV-cache memory management using paged/block-based allocation — similar to virtual memory paging in OS.
2. Key-value blocks allocated in non-contiguous physical pages, eliminating fragmentation.
3. 2-4x improvement in serving throughput for LLMs through efficient memory reuse.
4. Standard implementation in vLLM serving system.
5. Efficient memory sharing across multiple generation sequences.

## Relevance to Thesis
- PagedAttention enables memory-efficient serving when multiple adapters cause multiple independent KV-caches.
- Directly applicable to multi-task adapter model with multiple active adapters requiring separate KV-caches.
- Could be adapted to P2P scenario where different peers contribute KV-cache blocks via virtualized memory.

## Limitations / Gaps
- Focuses solely on single-node memory management — no network distribution.
- Assumes all layers on same GPU — not designed for P2P partitioned models.
- Requires customized memory management per hardware setting.