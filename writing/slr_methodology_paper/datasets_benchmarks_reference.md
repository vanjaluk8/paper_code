# Datasets and Benchmarks — Reference Table

Extracted from the writing materials notes for the 18+ representative systems in the concept matrix.

## Pillar 1: PEFT and Adapters

| Paper | Dataset | Task Type | Metric | Best Score | Public |
|---|---|---|---|---|---|
| Houlsby et al. (2019) | GLUE, SciTail | NLU classification | Accuracy | 93.0 (SciTail) | Yes |
| Hu et al. (2022) (LoRA) | GLUE | NLU classification | Accuracy | 89.7 (GLUE avg.) | Yes |
| Dettmers et al. (2023) (QLoRA) | Vicuna benchmark | instruction following | Elo rating | 99.3% of ChatGPT | Yes |
| Li & Liang (2021) (Prefix) | E2E, WebNLG, XSUM | NLG | ROUGE-L | 43.2 (XSUM) | Yes |
| Ben Zaken et al. (2022) (BitFit) | GLUE | NLU classification | Accuracy | ≈ BERT-base full FT | Yes |
| Poth et al. (2023) (Adapters lib.) | GLUE, SuperGLUE | NLU classification | Accuracy | matches single PEFT | Yes |

## Pillar 2: Adapter Composition

| Paper | Dataset | Task Type | Metric | Best Score | Public |
|---|---|---|---|---|---|
| Pfeiffer et al. (2020) (AdapterHub) | GLUE, XNLI | NLU + cross-lingual | Accuracy | multiple tasks | Yes |
| Pfeiffer et al. (2021) (AdapterFusion) | GLUE, SciTail, MRPC | NLU classification | Accuracy | 92.8 (SciTail) | Yes |
| Pfeiffer et al. (2020) (MAD-X) | GLUE (6 langs) | cross-lingual transfer | Accuracy | zero-shot transfer | Yes |
| Huang et al. (2023) (LoraHub) | BIG-Bench Hard | few-shot transfer | Accuracy | 34.7 avg per task (BBH) | Yes |
| Zhao et al. (2024) (LoraRetriever) | domain QA, MT-bench | multi-task QA | Accuracy / win-rate | matches best single | Yes |
| Ostapenko et al. (2024) | GLUE, SuperGLUE | NLU classification | Accuracy | --- | No |

## Pillar 3: Adapter-Aware Inference Serving

| Paper | Dataset | Task Type | Metric | Best Score | Public |
|---|---|---|---|---|---|
| Sheng et al. (2024) (S-LoRA) | synthetic | throughput | req/s | up to 4× throughput | No |
| Chen et al. (2023) (Punica) | synthetic serving | throughput | req/s | 12× higher throughput | No |
| Li et al. (2024) (CaraServe) | synthetic | throughput | req/s | 1.4× on average | No |
| Borzunov et al. (2023) (Petals) | multiple | instruction following | Accuracy | multiple | Yes |
| Šajina et al. (2024) (MT-EF) | Reddit, StackOverflow, CoNLL-2003, Few-NERD | MTP + NER | Test UA (User Accuracy) | +11.6% mean relative gain | Yes |

## Pillar 4: P2P and Federated Learning

| Paper | Dataset | Task Type | Metric | Best Score | Public |
|---|---|---|---|---|---|
| McMahan et al. (2017) (FedAvg) | CIFAR-10, Shakespeare | image/text classification | Accuracy | 10–100× comm. saving | Yes |
| Li et al. (2020) (FedProx) | FEMNIST, Sent140 | image/text classification | Accuracy | +1–5% vs FedAvg | Yes |
| Zhang et al. (2023) (FedPETuning) | GLUE | NLU classification | Accuracy | ≤5% loss vs central PEFT | Yes |
| Wang et al. (2024) (FLoRA) | GLUE (few-shot) | NLU classification | Accuracy | robust to rank hete. | Yes |
| Li et al. (2025) (DP-FedLoRA) | GLUE, clinical | text classification | Accuracy + (ε,δ) | ≤2% loss at ε=8 | Yes |
| Babakniya et al. (2023) (SLoRA) | GLUE, SuperGLUE | NLU classification | Accuracy | 2× faster convergence | Yes |
| Hegedus et al. (2019) (Gossip Learning) | synthetic | classification | Accuracy | ≈ FL quality (20–50% slower) | Yes |

## Pillar 5: MoE and Adapter Routing

| Paper | Dataset | Task Type | Metric | Best Score | Public |
|---|---|---|---|---|---|
| Fedus et al. (2022) (Switch Transformers) | C4 pre-training | language modelling | Perplexity, speedup | 4× speedup over T5-XXL | No |
| Zhou et al. (2022) (Expert Choice) | SuperGLUE, WMT | NLU + MT | Accuracy / BLEU | +2% average accuracy | No |
| Rajbhandari et al. (2022) (DeepSpeed-MoE) | GLUE, SuperGLUE | NLU classification | Accuracy | 4.5× speedup, <0.5% loss | No |
| Wang et al. (2023) (AdaMix) | GLUE, SuperGLUE | NLU classification | Accuracy | outperforms single PEFT | Yes |
| Li et al. (2024) (MixLoRA) | GLUE, domain-specific | NLU classification | Accuracy | --- | Yes |
| Zhang et al. (2024) (MiLoRA) | commonsense reasoning | reasoning + NLU | Accuracy | > single LoRA | Yes |
| Dou et al. (2024) (LoRAMoE) | world knowledge + instruct | multi-task generation | Accuracy, forgetting | alleviates forgetting | No |
| Liu et al. (2023) (MOELoRA) | medical + GLUE | NLU classification | Accuracy | > single LoRA | Yes |
| Ryabinin et al. (2020) (Crowdsourced MoE) | CIFAR-10/100, MNIST | image classification | Accuracy | up to 16 peers, 30% dropout | No |

## Clinical Gap

| Paper | Dataset | Task Type | Metric | Best Score | Public |
|---|---|---|---|---|---|
| MIMIC-III (federated PEFT) | MIMIC-III | clinical NLP | --- | --- | Yes |
| Proposed PoC (this thesis) | MIMIC-III NL-to-SQL | text-to-SQL | Execution accuracy | TBD | Yes |