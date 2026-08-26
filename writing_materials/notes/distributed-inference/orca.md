## Meta
- **Citation:** Choi, Y., et al. (2021). Orca: A Distributed Serving System for Transformer-Based Generative Models. *SOSP*.
- **Venue:** SOSP
- **Tags:** Distributed Serving, Generation Model Serving, LLM Inference, Throughput
- **Thesis sections:** §3.2 Distributed Serving, §3.3.2 Scheduling

## Key Findings
1. Orca: high-throughput distributed serving system for transformer generations.
2. Fine-grained, iteration-level scheduling: schedules output token generation, not batch — eliminates padding waste and improves throughput 15-25x over non-distributed approaches for single model tasks.
3. Selective batching: Fine-grained scheduling chooses which generation sequences to serve next.
4. GPU/IO optimization: merges memory allocation per sequences for KV-cache, optimizes kernel at C-U-D-A level.
5. Up to 20x improvement for single model serving.

## Relevance to Thesis
- Ground-work for LLM serving systems (continuous batching foundation).
- Scheduler concept relevant if P2P adapter architecture decides to switch between adapters within a stream of requests.

## Limitations / Gaps
- Distributed 2-GPU cluster reference; single model (BART), not adapter multiple.
- Generator task, not classifier.
- Scheduler-level only; cannot change adapter per request.