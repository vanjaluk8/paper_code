## Meta
- **Citation:** Fu, Y., et al. (2024). ServerlessLLM: Low-Latency Serverless Inference for Large Language Models. *OSDI*.
- **Venue:** OSDI
- **Tags:** Serverless Inference, Cold Start, GPU Memory, LLM Serving
- **Thesis sections:** §3.3 Serverless Inference, §5.3 Cold Start

## Key Findings
1. ServerlessLLM: serverless framework for LLM inference with focus on "cold start" latency reduction.
2. Multi-tier storage: GPU → CPU RAM → SSD for model artifacts: models loaded across P2P memory hierarchy.
3. Model load time reduced (5-10x) compared to downloading model for each request — key for low-latency inference.
4. Parallel model loading: activate multiple load streams across available memory.
5. Support for multi-tenant across tenants.

## Relevance to Thesis
- Serverless loading of model artifacts: "cold start" for adapter distribution — essential for P2P adapter marketplace requesting specific adapters from different peers, with latency constraints.
- Tiered storage peak: GPU RAM for "active" adapters, CPU RAM for "hot" adapters, SSD for "cold" adapters.
- Supports heterogeneous adapters: no single model shape across tenants.

## Limitations / Gaps
- Designed for small model shapes per tenant — not changed per request.
- No adapter/layer dynamic switching.
- No latency bounds on multi-number load across P2P adapters.