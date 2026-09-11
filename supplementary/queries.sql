# SCOPUS ADVANCED SEARCH QUERIES
# Query 1: Core Adapter-Based NLP

TITLE-ABS-KEY(("adapter" OR "adapters" OR "LoRA" OR "low-rank") 
AND 
("parameter-efficient" OR "PEFT" OR "parameter efficient") 
AND 
("NLP" OR "natural language processing" OR "transformer"))
AND 
SRCTYPE("j" OR "p")
AND 
PUBYEAR > 2018


Query 2: Multi-Task Learning with Transformers

TITLE-ABS-KEY((("adapter*" OR "LoRA" OR "parameter-efficient fine-tuning")
AND
("multi-task" OR "multitask" OR "multi-adapter")
AND
("inference" OR "serving" OR "deployment" OR "edge")))
AND SRCTYPE(j OR p)
AND PUBYEAR > 2020
AND NOT TITLE-ABS-KEY(("medical" OR "healthcare" OR "clinical" OR "sentiment" OR "recommendation"))



Query 3: Peer-to-Peer & Distributed NLP
TITLE-ABS-KEY(("peer-to-peer" OR "P2P" OR "decentralized" OR "federated")
AND
("learning" OR "training" OR "inference")
AND
("NLP" OR "natural language" OR "machine learning" OR "deep learning"))
AND
SRCTYPE("j" OR "p")
AND
PUBYEAR > 2017


Query 4: Adapter Fusion & Dynamic Routing
TITLE-ABS-KEY(("adapter" OR "adapters") 
AND 
("fusion" OR "routing" OR "dynamic" OR "mixture-of-experts" OR "MoE" OR "gating"))
AND 
SRCTYPE("j" OR "p")
AND 
PUBYEAR > 2020

Query 5: Parameter-Efficient Multi-Task Transformers
TITLE-ABS-KEY(("parameter-efficient" OR "PEFT" OR "efficient adaptation") 
AND 
("multi-task" OR "multitask") 
AND 
("transformer" OR "pre-trained models"))
AND 
SRCTYPE("j" OR "p")
AND 
PUBYEAR > 2019

Query 6: Modular Inference & Task Switching
TITLE-ABS-KEY(("modular" OR "modularity") 
AND 
("inference" OR "inference time") 
AND 
("adapter" OR "task-specific" OR "lightweight modules"))
AND 
SRCTYPE("j" OR "p")
AND 
PUBYEAR > 2018


Query 7: Agent-Based Collaborative Learning
TITLE-ABS-KEY(("agent" OR "agents" OR "node" OR "nodes") 
AND 
("collaborative" OR "collaboration" OR "decentralized") 
AND 
("deep learning" OR "neural network" OR "model training"))
AND 
SRCTYPE("j" OR "p")
AND 
PUBYEAR > 2017

Query 8: NL-to-SQL with Adapters (Domain-Specific)
TITLE-ABS-KEY(("NL-to-SQL" OR "semantic parsing" OR "natural language to SQL") 
AND 
("adapter" OR "fine-tun*" OR "parameter-efficient" OR "efficient"))
AND 
SRCTYPE("j" OR "p")
AND 
PUBYEAR > 2019

Query 9: Sequence Labeling & Token Classification with PEFT
TITLE-ABS-KEY(("token classification" OR "NER" OR "named entity recognition" OR "sequence labeling") 
AND 
("adapter" OR "LoRA" OR "parameter-efficient" OR "PEFT"))
AND 
SRCTYPE("j" OR "p")
AND 
PUBYEAR > 2019

Query 10: Frozen Base Model Paradigm
TITLE-ABS-KEY(("frozen" OR "freeze" OR "frozen base") 
AND 
("adapter" OR "efficient" OR "modular") 
AND 
("transfer learning" OR "fine-tun*"))
AND 
SRCTYPE("j" OR "p")
AND 
PUBYEAR > 2018


WEB OF SCIENCE (WoS) ADVANCED SEARCH QUERIES
Query 1: Core Adapter-Based NLP (WoS)
TS=(("adapter" OR "adapters" OR "LoRA" OR "low-rank") 
AND 
("parameter-efficient" OR "PEFT" OR "parameter efficient") 
AND 
("NLP" OR "natural language processing" OR "transformer"))
AND PY >= 2018



TS=((("adapter*" OR "LoRA" OR "PEFT")
AND
("multi-task" OR "multitask")
AND
("inference" OR "serving" OR "edge" OR "distributed")))
AND PY >= 2021
AND NOT TS=(("medical" OR "healthcare" OR "sentiment"))




Query 3: Peer-to-Peer Distributed Learning (WoS)
TS=(("peer-to-peer" OR "P2P" OR "decentralized" OR "federated") 
AND 
("learning" OR "training" OR "inference") 
AND 
("NLP" OR "natural language" OR "machine learning" OR "neural network"))
AND PY >= 2017

Query 4: Adapter Fusion & Routing Mechanisms (WoS)
TS=(("adapter" OR "adapters") 
AND 
("fusion" OR "dynamic routing" OR "mixture-of-experts" OR "MoE" OR "gating"))
AND PY >= 2020

Query 5: Modular Deep Learning (WoS)
TS=(("modular" OR "modularity") 
AND 
("neural" OR "transformer" OR "deep learning") 
AND 
("inference" OR "task-specific" OR "lightweight"))
AND PY >= 2018

Query 6: Agent-Based Collaborative ML (WoS)
TS=(("agent" OR "agents" OR "distributed node*") 
AND 
("collaborative" OR "collaboration" OR "decentralized" OR "gossip") 
AND 
("deep learning" OR "machine learning"))
AND PY >= 2017

Query 7: Memory-Efficient Multi-Task NLP (WoS)
TS=(("multi-task" OR "multitask") 
AND 
("memory-efficient" OR "memory efficient" OR "parameter-efficient" OR "computational efficient") 
AND 
("NLP" OR "natural language" OR "transformer"))
AND PY >= 2018

Query 8: Transfer Learning with Task Adaptation (WoS)
TS=(("transfer learning" OR "fine-tun*") 
AND 
("adapter" OR "parameter-efficient" OR "LoRA") 
AND 
("NLP" OR "text" OR "language"))
AND PY >= 2019

Query 9: Sequence Task Learning (WoS)
TS=(("token classification" OR "NER" OR "named entity" OR "sequence labeling") 
AND 
("adapter" OR "fine-tun*" OR "efficient" OR "modular"))
AND PY >= 2019

Query 10: Distributed Inference (WoS)
TS=(("distributed" OR "decentralized") 
AND 
("inference" OR "inference time") 
AND 
("efficient" OR "modular" OR "lightweight"))
AND PY >= 2018
