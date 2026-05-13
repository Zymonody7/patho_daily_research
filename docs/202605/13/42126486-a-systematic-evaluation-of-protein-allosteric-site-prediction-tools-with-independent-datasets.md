---
title: A systematic evaluation of protein allosteric site prediction tools with independent datasets.
title_zh: 基于独立数据集的蛋白质变构位点预测工具的系统评估
authors: "Yuanbao Ai, Haixiao Li, Xuemei Huang, Sen Liu"
date: 2026-05-13
pdf: "https://pubmed.ncbi.nlm.nih.gov/42126486/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 蛋白质位点预测计算工具的系统评估
tldr: 蛋白质变构调节对生物功能至关重要，但现有变构位点预测工具的性能差异尚不明确。本研究构建了包含结合态（holo）和非结合态（apo）蛋白质的独立测试集 CAPASP，对五种主流预测工具进行了多维度评估。结果显示，基于机器学习的 PASSer 和 APOP 在灵敏度和综合指标上表现最优，但所有工具在处理非结合态蛋白时性能均有所下降。该评估为研究者选择预测模型提供了参考，并指出了未来优化方向。
selection_source: fresh_fetch
motivation: 旨在解决现有蛋白质变构位点预测工具缺乏统一、独立的基准测试，导致研究者难以根据具体场景选择最优模型的问题。
method: 构建了 CAPASP-General 和 CAPASP-Unbound 两个独立数据集，从灵敏度、特异性、F1分数等五个维度对五种预测工具进行系统评估。
result: 实验发现基于蛋白质理化性质的机器学习模型 PASSer 和 APOP 在综合性能上领先，但在处理未结合配体的蛋白质结构时准确率明显降低。
conclusion: 机器学习模型在变构位点预测中具有显著优势，但未来仍需重点提升模型对蛋白质非结合态结构的泛化能力。
---

## 摘要
变构效应在蛋白质动力学中起着关键作用，对许多生物功能至关重要。在过去的十年中，研究者提出了多种预测变构位点的计算方法。然而，各方法的优缺点尚未得到充分了解。在本研究中，我们构建了两个未被所选计算方案使用的独立数据集：包含结合态（holo state）变构蛋白的 CAPASP-General 子集和包含游离态（apo state）变构蛋白的 CAPASP-Unbound 子集。随后，我们从灵敏度、特异性、F1 分数、MCC 值和排序能力五个维度系统评估了五种变构位点预测工具的准确性。结果表明，基于蛋白质理化性质的机器学习模型 PASSer 和 APOP 不仅在灵敏度预测方面取得了最高的成功率，而且在平均 F1 分数和 MCC 值方面也处于领先地位。然而，这些模型在 CAPASP-General 子集上的表现优于 CAPASP-Unbound 子集，这表明预测模型仍需进一步改进。这些发现有助于为不同的变构蛋白选择合适的预测模型，并深化我们对蛋白质功能和调节机制的理解。

## Abstract
Allostery plays a critical role in protein dynamics and is essential for many biological functions. Over the past decade, various computational approaches have been proposed for predicting allosteric sites. However, the strengths and weaknesses of each method are not well understood. In this study, we created two independent datasets that had not been used in selected computational protocols: a CAPASP-General subset comprising holo state allosteric proteins and a CAPASP-Unbound subset comprising apo state allosteric proteins. We then systematically evaluated the accuracy of five allosteric site prediction tools across five dimensions: sensitivity, specificity, F1-score, MCC value and ranking capability. The results indicated that the machine learning models PASSer and APOP, which are based on protein physicochemical properties, not only achieved the highest success rate in sensitivity prediction but also lead in average F1-score and MCC value. However, these models performed better with the CAPASP-General subset than with the CAPASP-Unbound subset, suggesting that the prediction models require further improvement. These findings could facilitate the selection of appropriate prediction models for different allosteric proteins and enhance our understanding of protein function and regulatory mechanisms.