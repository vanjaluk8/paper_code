## Meta
- **Citation:** Tian, Y., et al. (2022). FedNLP: Benchmarking Federated Learning Methods for Natural Language Processing. *Findings of NAACL*.
- **Venue:** NAACL Findings
- **Tags:** Federated Learning Benchmark, NLP, PEFT, NLU Generation, Sequence Labeling
- **Thesis sections:** §6.1 Federated Learning, §7.2 Benchmarking

## Key Findings
1. FedNLP is a comprehensive open-source benchmark for evaluating FL on text tasks: text classification, sequence labeling, sequence generation
2. Compares 12 FL methods (FedAvg, FedProx, FedOPT, FedBR and more) on 10 NLP datasets
3. Key insight: no single FL algorithm consistently beats the rest. FedAvg is best in text classification; comparisons matter on task type, data non-IID distribution
4. Communication overhead reduces by 10-100x on parameter sharing only with small local steps
5. FedNLP is on GitHub and uses HuggingFace tokenizer.

## Relevance to Thesis
- Shows that FL for NLP works with LoRA adapters: each adapter can be treated as a personalized per-task module — a local model trained on distributed data.
- The benchmark suite of methods (personalization, FedProx) can be adapted for P2P adapter exchange analysis.
- Illustrates that data imbalance issues in FL could occur in P2P settings.

## Limitations / Gaps
- Not P2P FL organization but centralized aggregator paradigm.
- Focuses on training aspects only, not system design or P2P communications.
- Training models fairly small (BERT, GPT-2) compared to instruction-tuned billion-parameter LLMs.