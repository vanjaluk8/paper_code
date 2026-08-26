## Meta
- **Citation:** Jeong, E., et al. (2021). FedED: Federated Learning via Ensemble Distillation for Medical NLP. *EMNLP*.
- **Venue:** EMNLP
- **Tags:** Federated Learning, Knowledge Distillation, NLP, Medical Data
- **Thesis sections:** §6.2 Decentralized FL, §5.6 Model Sharing

## Key Findings
1. FedED: Federated Ensemble Distillation — each client trains model locally, uploads the logit distribution (not model weights) to a central server; server ensemble-distills logits into a refined global model.
2. Logits are generated from the server-side teacher model, reducing communication: logits are significantly smaller (100-800 floats per sample) than full gradient or weight updates.
3. Prevents gradient leakage by only sharing logit scores, not gradients.

## Relevance to Thesis
- Logit-based knowledge distillation replaces full model sharing — directly complementary to using adapters for model sharing.
- Knowledge distillation from student models (adapter outputs) aggregated through consensus could implement activity-based routing: the "best" adapter is the best student model.
- Communication-savvy: logit transfer can serve as adapter distribution.

## Limitations / Gaps
- Central aggregator server present not fully decentralized — but logit-based approach is modular.
- Evaluated only on medical NLP tasks (ICD coding from clinical notes) — limited applicability.
- Communication efficiency trade: combines centralized logit ensemble with NLP task — not full model parameter exchange.