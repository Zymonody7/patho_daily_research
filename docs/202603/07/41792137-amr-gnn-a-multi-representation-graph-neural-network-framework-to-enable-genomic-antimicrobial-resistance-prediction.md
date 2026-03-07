---
title: "AMR-GNN: a multi-representation graph neural network framework to enable genomic antimicrobial resistance prediction."
title_zh: AMR-GNN：一种用于基因组抗生素耐药性预测的多表示图神经网络框架
authors: "Nguyen HA, Peleg AY, Wisniewski JA, Wang X, Wang Z, Blakeway LV, Badoordeen GZ, Theegala R, Doan NQ, Parker MH, Green AG, Song J, Dowe DL, Macesic N., Hoai-An Nguyen, Anton Y Peleg, Jessica A Wisniewski, Xiaoyu Wang, Zhikang Wang, Luke V Blakeway, Gnei Z Badoordeen, Ravali Theegala, Nhu Quynh Doan, Matthew H Parker, Anna G Green, Jiangning Song, David L Dowe, Nenad Macesic"
date: 2026-03-06
pdf: "https://pubmed.ncbi.nlm.nih.gov/41792137/"
tags: ["query:pathoai"]
score: 10.0
evidence: 用于基因组抗生素耐药性预测的图神经网络
tldr: 针对全基因组测序数据维度高且缺乏标准化表示导致抗生素耐药性（AMR）预测困难的问题，本文提出了 AMR-GNN 框架。该框架利用图神经网络整合多种基因组表示，在铜绿假单胞菌及多种临床病原体数据集上验证了其有效性。研究不仅显著提升了预测精度，还通过识别关键生物标志物增强了模型的可解释性，并有效缓解了克隆关系对预测结果的干扰，为精准医疗提供了有力支持。
selection_source: fresh_fetch
motivation: 全基因组测序数据的高维度和缺乏标准化表示是准确预测细菌抗生素耐药性表型的主要障碍。
method: 开发了一个集成多种基因组表示的图神经网络框架，通过图深度学习技术从序列数据中提取复杂的耐药特征。
result: 在多种临床重要病原体的大规模数据集上，该框架展现了优异的预测性能，并能有效识别出具有生物学意义的耐药标志物。
conclusion: AMR-GNN 证明了多表示图学习在基因组预测任务中的通用性和解释力，为耐药性机制研究和临床诊断提供了新工具。
---

## 摘要
全基因组测序（WGS）数据是理解抗生素耐药性（AMR）机制的宝贵资源。然而，WGS 数据具有高维性，且缺乏标准化的基因组表示，这是 AMR 表型预测的主要障碍。为了充分挖掘这些高分辨率数据，我们提出了 AMR-GNN，这是一个基于图深度学习的框架，它将多种基因组表示与图神经网络（GNN）相结合，从而实现基于基因组序列数据的 AMR 表型预测。我们使用铜绿假单胞菌（Pseudomonas aeruginosa）对 AMR-GNN 进行了测试，这是一种具有临床相关性的革兰氏阴性细菌病原体，以其复杂的 AMR 机制而闻名。我们将 AMR-GNN 作为一个概念验证框架，旨在通过数据驱动的机器学习（ML）方法解决 AMR 表型预测中的几个关键问题，包括利用多种基因组表示来提升性能、减轻克隆关系的影响以及识别具有信息量的生物标志物以提供可解释性。在涵盖革兰氏阴性和革兰氏阳性病原体的最大公开数据集上进行的后续验证，突显了 AMR-GNN 在检测多种临床相关病原体-药物组合的 AMR 方面的广泛适用性。

## Abstract
Whole-genome sequencing (WGS) data are an invaluable resource for understanding antimicrobial resistance (AMR) mechanisms. However, WGS data are high-dimensional and the lack of standardized genomic representations is a key barrier to AMR phenotype prediction. To fully explore these high-resolution data, we propose AMR-GNN, a graph deep learning-based framework that integrates multiple genomic representations with graph neural networks (GNN) to enable AMR phenotype prediction from genomic sequence data. We test AMR-GNN with Pseudomonas aeruginosa, a clinically relevant Gram-negative bacterial pathogen known for its complex AMR mechanisms. We present AMR-GNN as a proof-of-concept framework designed to address several key problems in AMR phenotype prediction with data-driven machine learning (ML) approaches, including using multiple genomic representations to enhance performance, to mitigate the influence of clonal relationships and to identify informative biomarkers to provide explainability. Follow-up validation on the largest publicly available dataset spanning both Gram-negative and Gram-positive pathogens highlights AMR-GNN's broad applicability in detecting AMR in diverse and clinically relevant pathogen-drug combinations.