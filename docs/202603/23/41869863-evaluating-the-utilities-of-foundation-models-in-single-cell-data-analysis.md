---
title: Evaluating the Utilities of Foundation Models in Single-Cell Data Analysis.
title_zh: 评估基础模型在单细胞数据分析中的效用
authors: "Tianyu Liu, Kexing Li, Yuge Wang, Hongyu Li, Hongyu Zhao"
date: 2026-03-23
pdf: "https://pubmed.ncbi.nlm.nih.gov/41869863/"
tags: ["query:seqai"]
score: 10.0
evidence: 评估单细胞测序数据分析的基础模型
tldr: 随着大模型在生物医学领域的兴起，单细胞基础模型（FMs）层出不穷，但其真实效能尚不明确。本研究通过 scEval 框架对 scGPT、Geneformer 等 10 个主流模型在 8 类下游任务中进行了全面评估。结果显示，虽然部分模型表现优异，但在特定任务上仍难以超越传统专用算法。该研究为单细胞大模型的预训练与微调提供了实践指南，并开源了评测工具以推动领域发展。
selection_source: fresh_fetch
motivation: 旨在系统性评估单细胞领域涌现的大模型在实际科研任务中的表现，并探讨其相对于传统专用方法的优势与局限。
method: 提出 scEval 评测框架，对比了 10 种单细胞基础模型在细胞类型注释、批次效应校正等 8 个核心任务上的性能、稳定性和超参数敏感度。
result: 发现 scGPT、Geneformer 和 CellFM 综合表现领先，但在多个任务中，基础模型的表现并未能稳定超越针对特定任务优化的传统算法。
conclusion: 单细胞大模型虽具潜力但仍面临挑战，研究者应根据具体任务选择模型，并参考本研究提供的指南优化预训练与微调流程。
---

## 摘要
基础模型（FMs）在工业和科学领域都取得了显著进展。在本文中，我们通过针对单细胞数据相关的八个下游任务进行全面实验，评估了基础模型在单细胞测序数据分析中的性能。综合考虑十个单细胞基础模型的模型性能和用户易用性，表现最好的模型包括 scGPT、Geneformer 和 CellFM。然而，通过将这些基础模型与特定任务方法进行比较，我们发现单细胞基础模型在所有任务中并不总是优于特定任务方法，这挑战了开发单细胞分析基础模型的必要性。此外，我们基于提出的 scEval 框架，评估了超参数、初始设置和稳定性对训练单细胞基础模型的影响，并提供了预训练和微调指南，以增强单细胞基础模型的性能。我们的工作总结了单细胞基础模型的现状，指出了其局限性和未来发展方向，并提供了一个免费可用的评估流程，用于基准测试新模型并促进方法开发。

## Abstract
Foundation Models (FMs) have made significant strides in both industrial and scientific domains. In this paper, we evaluate the performance of FMs for single-cell sequencing data analysis through comprehensive experiments across eight downstream tasks pertinent to single-cell data. Overall, the top FMs include scGPT, Geneformer, and CellFM by considering model performances and user accessibility among ten single-cell FMs. However, by comparing these FMs with task-specific methods, we found that single-cell FMs may not consistently excel than task-specific methods in all tasks, which challenges the necessity of developing foundation models for single-cell analysis. In addition, we evaluated the effects of hyperparameters, initial settings, and stability for training single-cell FMs based on a proposed scEval framework, and provide guidelines for pre-training and fine-tuning to enhance the performances of single-cell FMs. Our work summarizes the current state of single-cell FMs, points to their constraints and avenues for future development, and offers a freely available evaluation pipeline to benchmark new models and improve method development.