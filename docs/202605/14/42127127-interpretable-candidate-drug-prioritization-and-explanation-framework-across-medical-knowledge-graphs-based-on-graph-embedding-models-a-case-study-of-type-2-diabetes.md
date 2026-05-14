---
title: "Interpretable candidate drug prioritization and explanation framework across-medical knowledge graphs based on graph embedding models: A case study of type 2 diabetes."
authors: "Zekun Zhou, Shuo Yang"
date: 2026-01-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/42127127/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 用于药物优先级排序的图嵌入模型
tldr: 一种基于医疗知识图谱和图嵌入的可解释药物候选物优先级排序框架。
selection_source: fresh_fetch
motivation: 用于药物优先级排序的图嵌入模型。
method: 方法与实现细节请参考摘要与正文。
result: 结果与对比结论请参考摘要与正文。
conclusion: 总体而言，该工作在所述任务上展示了有效性，并提供了可复用的思路或工具。
---

## Abstract
OBJECTIVE: Addressing the challenges in elucidating the mechanisms of complex diseases such as Type 2 Diabetes Mellitus (T2DM), this study aims to construct a domain-specific cross-medicine knowledge graph (CMKG) and develop a unified path scoring framework that couples graph embeddings with rule-based reasoning, enabling high-precision, interpretable prioritization and explanation of potential drug candidates. METHODS: First, multi-source biomedical data from Hetionet, SymMap, TCMBank, STRING, and TTD were integrated. Using Jaccard and overlap-based fusion strategies, entity alignment and relation consolidation were performed to construct a deep CMKG bridged by genes. Second, four graph embedding models (TransE, DistMult, ComplEx, and RotatE) were introduced for link prediction and evaluated using MRR and Hits@K. Finally, to overcome the interpretability limitations of black-box predictions, AnyBURL rule learning was combined with depth-first search (DFS). We innovatively introduced an Ingredient Specificity Index (ISI) and a hybrid path confidence calibration mechanism, constructing a unified path scoring system incorporating length decay, node/relation weights, and experimental evidence bonuses to screen the most critical mechanistic paths. RESULTS: The constructed CMKG contains 15 entity types (245,235 entities) and 52 relation types (7,155,373 triples), covering 709 core T2DM genes. Link prediction stability tests across multiple random seeds showed that the ComplEx model consistently performed best in handling complex multi-mapping relations (MRR = 0.213 ± 0.004, Hits@10 = 0.418 ± 0.003). Consequently, the fully converged ComplEx model (Peak Hits@10 = 0.48) was utilized for comprehensive prediction. Retaining the top 100 predictions, Abelmoschus manihot and Topiramate ranked highest among TCM herbs and modern medicine compounds, respectively. Path analysis based on the scoring system revealed deep multi-target mechanisms, including insulin signaling sensitization, inflammatory regulation, and chromatin/cell-cycle intervention. CONCLUSION: The proposed gene-bridged graph embedding and unified path scoring framework successfully translates probabilistic predictions into biologically traceable semantic explanations. Rigorous ablation and parameter sensitivity experiments confirm that the framework achieves a robust balance between knowledge coverage and explanatory specificity, providing a transparent, robust, and scalable methodological foundation for candidate drug prioritization in complex diseases.