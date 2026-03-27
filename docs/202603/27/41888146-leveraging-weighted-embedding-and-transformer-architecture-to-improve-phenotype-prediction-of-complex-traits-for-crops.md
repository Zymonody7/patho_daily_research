---
title: Leveraging weighted embedding and Transformer architecture to improve phenotype prediction of complex traits for crops.
title_zh: 利用加权嵌入和 Transformer 架构改进农作物复杂性状的表型预测
authors: "Jing Li, Linfeng Yu, Mengfan Li, Rui Han, Yecheng Li, Abdulwahab Saliu Shaibu, Kwadwo Gyapong Agyenim-Boateng, Zhaoyi Hao, Yitian Liu, Bin Li, Shengrui Zhang, Liang Li, Lijuan Qiu, Junming Sun"
date: 2026-03-26
pdf: "https://pubmed.ncbi.nlm.nih.gov/41888146/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 用于基因组序列表示的Transformer架构
tldr: 针对作物复杂性状预测中海量基因组数据与生物学解释性难以平衡的问题，本研究开发了 GP-WAITER 深度学习框架。该框架通过将 GWAS 衍生的 SNP 权重融入 CNN 与 Transformer 的混合架构，利用加权嵌入和自注意力机制捕捉超长基因序列的远程依赖关系。实验表明，该模型在预测准确率和计算效率上显著优于现有 SOTA 模型，并能精准定位关键遗传变异，为精准育种提供了高效且具解释性的工具。
selection_source: fresh_fetch
motivation: 现有的统计模型在处理大规模基因组数据时，难以在预测精度与生物学功能解释之间达成平衡。
method: 提出 GP-WAITER 框架，结合了卷积神经网络、Transformer 架构以及基于全基因组关联分析（GWAS）的加权嵌入机制。
result: "在六个数据集上，该模型相比七种主流模型实现了最高 77.5% 的准确率提升和约 2 倍的计算效率增长。"
conclusion: 该框架通过融合先验生物知识与深度学习架构，实现了对作物复杂性状的高效预测与关键变异位点的透明化解析。
---

## 摘要
理解基因组变异与表型之间的关系是揭示复杂性状背后遗传结构的基础。然而，现有的统计模型难以在处理海量基因组数据集与保持生物学可解释性之间取得平衡。在此，我们介绍了 GP-WAITER，这是一个将基于全基因组关联分析（GWAS）的单核苷酸多态性（SNP）权重整合到混合卷积神经网络和 Transformer 架构中的深度学习框架。通过利用加权嵌入机制和多头自注意力机制，GP-WAITER 能够有效捕捉超长基因组序列中的远程依赖关系。该模型在六个数据集上始终优于七种最先进的基因组预测模型，预测准确度最高提升了 77.5%，均方误差降低了 78%，计算效率提高了 1.8 至 2.4 倍。此外，GP-WAITER 通过精准定位驱动特定性状的关键遗传变异，提供了生物学透明度。这一可扩展且可解释的框架为精准育种和性状相关变异的功能解释提供了强有力的工具。

## Abstract
Understanding the relationship between genomic variation and phenotype is fundamental to deciphering the genetic architecture underlying complex traits. Yet, existing statistical models struggle to balance massive genomic datasets with biological interpretability. Here, we introduce GP-WAITER, a deep learning framework integrating GWAS-derived SNP weights into a hybrid convolutional neural network and Transformer architecture. By utilizing a weighted embedding mechanism and multi-head self-attention, GP-WAITER effectively captures long-range dependencies across ultra-long genomic sequences. The model consistently outperforms seven state-of-the-art genomic prediction models across six datasets, achieving up to a 77.5% improvement in prediction accuracy, a 78% reduction in mean squared error, and a 1.8-2.4fold increase in computational efficiency. Furthermore, GP-WAITER offers biological transparency by pinpointing key genetic variants driving specific traits. This scalable, interpretable framework provides a powerful tool for precision breeding and the functional interpretation of trait-associated variants.