---
title: "RGPA-GCN: Graph convolutional networks for rice gene-phenotype association prediction."
title_zh: RGPA-GCN：用于水稻基因-表型关联预测的图卷积网络。
authors: "J Luo, X Wang, X Li, Q Zhou, Y Xiang, Z Yue, Y Gao"
date: 2026-03-22
pdf: "https://pubmed.ncbi.nlm.nih.gov/41865388/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 用于基因-表型关联预测的图卷积网络
tldr: 水稻基因与表型关联（GPA）的实验鉴定耗时耗力，计算预测成为重要辅助手段。本研究提出RGPA-GCN模型，将GPA预测建模为图节点分类任务，利用k-近邻算法构建融合基因功能与表型语义相似性的拓扑图，并通过图卷积网络进行信息聚合。实验证明该方法在5折交叉验证中优于多种经典及前沿模型，能有效预测未知关联及新基因/表型，为提升水稻产量与抗逆性提供了高效的计算工具。
selection_source: fresh_fetch
motivation: 传统的生物实验鉴定水稻基因与表型关联成本极高，亟需高效的计算方法来筛选潜在关联以加速育种进程。
method: 该方法将预测任务转化为图节点分类问题，通过k-NN构建包含基因功能和表型语义信息的拓扑图，并利用图卷积网络实现特征聚合。
result: 在5折交叉验证中，该模型性能显著优于6种传统机器学习算法和3种现有最先进模型，且具备预测全新基因或表型的能力。
conclusion: RGPA-GCN通过整合多源相似性信息和图学习技术，为水稻基因功能研究和精准育种提供了一个准确且鲁棒的预测框架。
---

## 摘要
水稻作为人类重要的食物来源发挥着关键作用。识别基因-表型关联（GPAs）可以显著增强水稻对环境压力的耐受性及其整体产量。然而，发现 GPAs 的实验过程不仅耗费大量资源，而且非常耗时。GPAs 的计算筛选已成为补充和加速生物实验的重要工具。在本研究中，我们将 GPAs 预测建模为节点分类任务，并提出了 RGPA-GCN，这是一种利用图卷积网络的创新计算方法。RGPA-GCN 通过应用 k-最近邻（k-nearest neighbor）方法构建拓扑图，以实现有效的信息聚合。该图中的节点融合了基因功能相似性和表型语义相似性，从而提高了预测的准确性。值得注意的是，RGPA-GCN 方法展示了其预测未知 GPAs 以及此前未见过的基因或表型的能力。通过 5 折交叉验证，RGPA-GCN 表现出优异的性能，优于六种经典机器学习方法和三种最先进的模型。此外，针对采样器的消融研究以及涉及五种不同表型的案例研究取得了理想的结果，进一步证明了该方法的有效性。

## Abstract
Rice plays a pivotal role as a vital food source for human consumption. Identifying gene-phenotype associations (GPAs) can significantly enhance the tolerance of rice to environmental stress and its overall yield. Nevertheless, the experimental process of discovering GPAs is not only consume a lot of resources but also time-consuming. The computational screening for GPAs has emerged as an essential tool to complement and expedite biological experiments. In this study, we tackle the prediction of GPAs by framing it as a node classification task, and introduce RGPA-GCN, an innovative computational approach leveraging graph convolutional networks. RGPA-GCN constructs a topology graph through the application of the k-nearest neighbor method for effective information aggregation. The nodes within this graph encapsulate both gene functional similarity and phenotype semantic similarity, enhancing the accuracy of our predictions. Notably, the RGPA-GCN approach demonstrates its ability to predict both unknown GPAs and previously unseen genes or phenotypes. Leveraging 5-fold cross-validation, RGPA-GCN exhibits commendable performance, outperforming six classical machine learning methods, and three state-of-the-art models. Additionally, the ablation studies on the sampler and the case studies involving five different phenotypes yields promising results, underscoring the effectiveness of this approach.