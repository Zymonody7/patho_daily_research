---
title: "HNRM: hyperedge neighborhood-based representation for predicting N6-methyladenosine-related regulatory pathways."
authors: "Dongdong Jiang, Yan Li, Liang Yu"
date: 2026-04-29
pdf: "https://pubmed.ncbi.nlm.nih.gov/42050531/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 用于调控通路和疾病关联的超图神经网络
tldr: HNRM 利用超图神经网络预测 m6A 位点、疾病和药物之间的高阶关联。
selection_source: fresh_fetch
motivation: 用于调控通路和疾病关联的超图神经网络。
method: 方法与实现细节请参考摘要与正文。
result: 结果与对比结论请参考摘要与正文。
conclusion: 总体而言，该工作在所述任务上展示了有效性，并提供了可复用的思路或工具。
---

## Abstract
BACKGROUND: N6-methyladenosine (m6A), the most predominant post-transcriptional RNA modification, regulates splicing, translation, and decay processes. Its dysregulation is implicated in cancers, metabolic disorders, and neurological diseases. Despite accumulating evidence highlighting m6A as a key player in human pathologies, no previous computational framework has investigated the high-order associations among m6A sites, diseases, and drugs within a unified model. RESULTS: Here, we introduce HNRM, a data-driven approach designed to model hyperedges across these entities. We frame this problem as a high-order link-prediction task on a hypergraph. We employ a hypergraph neural network based on hyperedge neighborhoods to learn embedding representations of both hyperedges and nodes. CONCLUSIONS: The performance of HNRM is evaluated on a newly collected and processed m6A dataset, as well as on five additional datasets from other domains, demonstrating its superior effectiveness. Ablation studies and Gene Ontology enrichment analysis further validate its capability in identifying potential associations.