---
title: Prediction of antimicrobial minimum inhibitory concentration from bacterial genomes using a scalable and interpretable machine learning approach.
title_zh: 利用可扩展且可解释的机器学习方法从细菌基因组预测抗微生物药物最小抑菌浓度
authors: "Alessandro Gerada, Yinzheng Zhong, Nicholas Harper, Anoop Velluva, Nada Reza, Vineet Dubey, Alex Howard, Peter L Green, Steve Paterson, William Hope"
date: 2026-05-26
pdf: "https://pubmed.ncbi.nlm.nih.gov/42191912/"
tags: ["query:pathoai"]
score: 10.0
evidence: 利用机器学习从细菌基因组中预测抗生素耐药性
tldr: 一种高效且可解释的机器学习方法，无需先验知识即可从细菌基因组中预测抗生素最低抑菌浓度。
selection_source: fresh_fetch
motivation: 利用机器学习从细菌基因组中预测抗生素耐药性。
method: 方法与实现细节请参考摘要与正文。
result: 结果与对比结论请参考摘要与正文。
conclusion: 总体而言，该工作在所述任务上展示了有效性，并提供了可复用的思路或工具。
---

## 摘要
虽然机器学习模型可以从细菌全基因组测序（WGS）中预测抗微生物药物敏感性，但目前最先进的方法要么计算需求高，要么依赖于已知的遗传耐药决定因素。在这里，我们描述了一种高效的数据驱动方法，通过逐步扩展和细化预测性基因组片段来预测最小抑菌浓度（MIC），该方法不依赖于耐药决定因素的先验知识。所得模型具有高度的可解释性——捕获了已知的以及潜在的新型耐药决定因素。使用 762 株临床大肠杆菌菌株，71.6% 的预测结果与实测 MIC 的误差在正负一个稀释度以内。与基于注释的耐药决定因素（F1 = 0.82）或 k-mer 计数（F1 = 0.74）训练的替代模型相比，使用该算法训练的模型在外部数据上的泛化能力更好（F1 分数 = 0.85）。计算需求较低（内存占用 23.6GB，而 k-mer 模型为 38.8GB）。这些优势代表了从 WGS 预测抗微生物药物敏感性方面的重要进展，在临床诊断、药物开发和监测方面具有潜在的应用价值。

## Abstract
Although machine learning models can predict antimicrobial susceptibility from bacterial whole genome sequencing (WGS), state-of-the-art approaches are computationally demanding or dependent on knowledge of genetic resistance determinants. Here, we describe an efficient data-driven approach to predicting minimum inhibitory concentration (MIC) by progressively extending and refining predictive genome segments, independent of prior knowledge of resistance determinants. Resultant models had high interpretability - known and potentially novel resistance determinants were captured. Using 762 clinical E. coli strains, 71.6% of predictions were within one dilution of the measured MIC. Models trained with this algorithm generalised better onto external data (F1 score = 0.85) compared with alternative models trained on annotated resistance determinants (F1 = 0.82) or k-mer counts (F1 = 0.74). Computational demands were low (RAM usage 23.6GB vs 38.8GB for k-mer model). These advantages represent an important advance in predicting antimicrobial susceptibility from WGS, with potential applications for clinical diagnostics, drug development, and surveillance.