## Meta
- **Citation:** Predictive-LoRA: A Proactive and Fragmentation-Aware Serverless LoRA Serving System
- **Venue:** arXiv 2025
- **Tags:** `adapter-serving` `lora` `serverless` `prediction`
- **Thesis sections:** §5.x

## Key Findings
1. Predictive-LoRA proposes a proactive approach to LoRA serving in serverless settings — predict which adapters will be needed and pre-load them to avoid cold starts.
2. Introduces fragmentation-aware caching that accounts for GPU memory fragmentation and pre-emptively moves adapters between GPU tiers.
3. Uses a forecasting model to predict future adapter requests based on request patterns.
4. Cold start latency is reduced by caching adapters even across container re-initializations.
5. Demonstrates up to 50% tail latency reduction compared to reactive caching strategies.

## Relevance to Thesis
- Important for a future P2P marketplace: adapter pre-fetching and caching can mitigate P2P transfer latency in marketplace.
- Predictive caching — anticipating which adapters will be needed based on past patterns — is similar to predicting "which peers will fetch which adapters".
- The fragmentation-aware caching (tiered storage) is analogous to "which adapters to pre-fetch from which peers".

## Limitations / Gaps
- The "prediction" is over time but within a single serverless cluster.
- Not addressing adapter discovery — the forecasting model assumes a fixed or a priori known set of adapters.
- Does not address P2P transfer latencies over internet-scale distances.
- Lacks evaluation of prediction accuracy over real internet-deployed workloads.