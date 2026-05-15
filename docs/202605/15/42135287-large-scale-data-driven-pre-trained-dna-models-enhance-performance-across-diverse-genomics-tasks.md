---
title: Large-scale data-driven pre-trained DNA models enhance performance across diverse genomics tasks.
title_zh: 大规模数据驱动的预训练 DNA 模型提升了多种基因组学任务的性能
authors: "Sun C, He Z, Zhang S, Xu K, Sun Y, Wang Y, Hu P, Bo X, Liao M, Li H, Chen H., Canzhuang Sun, Zhijie He, Shifei Zhang, Kang Xu, Yu Sun, Yuyang Wang, Pengzhen Hu, Xiaochen Bo, Mingzhi Liao, Hao Li, Hebing Chen"
date: 2026-05-14
pdf: "https://pubmed.ncbi.nlm.nih.gov/42135287/"
tags: ["query:bioinfo"]
score: 10.0
evidence: 监督多任务DNA基础模型
tldr: "针对基因组深度学习模型任务单一、难以跨场景扩展的问题，研究者开发了 SUCCEED 预训练 DNA 基础模型。该模型在 6,389 个 ENCODE 功能基因组轨道上进行监督式多任务预训练，结合卷积与 Transformer 架构捕捉局部基序和长程依赖。实验证明，SUCCEED 在表观基因组预测、信号去噪及 3D 染色质接触预测等任务中表现优异，超越了纯自监督模型，为复杂生物背景下的基因组建模提供了统一且可迁移的框架。"
selection_source: fresh_fetch
motivation: 现有的基因组深度学习模型大多针对特定任务且需重复训练，缺乏在不同生物学背景下的通用性和可扩展性。
method: 提出 SUCCEED 模型，通过在数千个功能基因组数据集上进行监督式多任务预训练，并融合卷积层与 Transformer 架构来提取 DNA 序列的调控特征。
result: 该模型在预测细胞特异性表观特征和 3D 染色质接触等任务上达到或超过了 Enformer 等顶尖模型的水平，且显著优于仅基于序列的自监督模型。
conclusion: SUCCEED 证明了大规模监督式预训练能有效提升 DNA 基础模型的可迁移性，为基因组调控研究提供了一个高效的统一建模工具。
---

## 摘要
基于序列的深度学习推动了基因组解释的发展，但大多数模型仍针对特定任务且依赖重新训练，限制了其在不同生物学背景下的可扩展性。在此，我们提出了 SUCCEED，这是一个在 6,389 个 ENCODE 功能基因组学轨道上进行预训练的有监督多任务 DNA 基础模型，旨在学习可迁移的调控表征。通过将卷积层与 Transformer 架构相结合，SUCCEED 能够捕捉局部序列基序和长程调控依赖关系，在基准任务中实现了与 Enformer 相当或更优的性能。通过迁移学习，它能够预测细胞类型特异性的表观基因组图谱，对稀疏的染色质开放性信号进行去噪，并在不输入 CTCF 的情况下预测跨数据规模和细胞类型的三维染色质接触。在多种基因组学任务中，SUCCEED 的表现与 Sei 等有监督基础模型相当，并优于仅在 DNA 序列上训练的自监督模型。总之，SUCCEED 是一个可迁移且可扩展的基础模型，为复杂生物学背景下的基因组尺度调控建模提供了一个统一的框架。

## Abstract
Sequence-based deep learning has advanced genome interpretation, yet most models remain task-specific and rely on retraining, limiting scalability across biological contexts. Here we present SUCCEED, a supervised multi-task DNA foundation model pretrained on 6,389 ENCODE functional genomics tracks to learn transferable regulatory representations. By integrating convolutional layers with a Transformer architecture, SUCCEED captures both local sequence motifs and long-range regulatory dependencies, achieving performance comparable to or exceeding Enformer across benchmark tasks. Through transfer learning, it predicts cell-type-specific epigenomic profiles, denoises sparse chromatin accessibility signals, and predicts three-dimensional chromatin contacts without CTCF input across data scales and cell types. Across diverse genomics tasks, SUCCEED performs comparably to supervised foundation models such as Sei and outperforms self-supervised models trained solely on DNA sequence. Overall, SUCCEED is a transferable and scalable foundation model that provides a unified framework for genome-scale regulatory modeling in complex biological contexts.