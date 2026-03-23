---
title: TabPFN Opens New Avenues for Small-Data Tabular Learning in Drug Discovery.
title_zh: TabPFN 为药物研发中的小样本表格学习开辟了新途径
authors: "Woruo Chen, Yao Tian, Nian Liao, Youchao Deng, Dejun Jiang, Dongsheng Cao"
date: 2026-03-23
pdf: "https://pubmed.ncbi.nlm.nih.gov/41867095/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 用于药物发现的基于Transformer的表格基础模型
tldr: 早期药物研发常面临数据稀缺和分布偏移的挑战，导致传统的梯度提升树模型（如 XGBoost）鲁棒性受限。本研究将基于 Transformer 的表格基础模型 TabPFN 应用于分子数据建模，发现其在回归任务、小样本场景及分布外（OOD）评估中表现出比传统模型更稳定且显著的优势。通过特征消融和嵌入分析，证实了该模型具有更优的归纳偏置，为药物发现中的小数据预测提供了高效且稳健的新途径。
selection_source: fresh_fetch
motivation: 解决早期药物研发中因样本量极小和数据分布偏移导致的预测模型可靠性不足及传统模型鲁棒性差的问题。
method: 采用无需任务特定重训练的表格基础模型 TabPFN，在分子和量子化学数据集上对比其与 XGBoost 的分类与回归性能。
result: TabPFN 在回归任务和中小型数据集上显著优于传统树模型，且在分布外数据测试中表现出更平滑的结构-性质关系和更强的泛化能力。
conclusion: TabPFN 作为一种数据高效的表格学习工具，为药物发现领域的小数据和分布外预测挑战提供了强有力的替代方案。
---

## 摘要
早期药物研发常受限于数据稀缺和分布外（OOD）偏移，这限制了预测模型的可靠性。尽管深度学习在分子和生物数据的表示学习方面取得了进展，但表格建模仍然不可或缺，特别是在小样本和 OOD 场景下。十多年来，梯度提升决策树（GBDT），如 XGBoost，一直是主流选择，但在这些条件下其鲁棒性有限。TabPFN 是最近推出的一种基于 Transformer 的表格基础模型，无需针对特定任务进行重新训练即可在小数据集上实现准确预测。将 TabPFN 应用于各种分子数据集，我们发现 TabPFN 在分类任务中与 XGBoost 表现相当，但在回归任务中表现出明显且稳定的优势，尤其是在中小规模数据集和 OOD 评估中增益最为显著。特征和数据消融（10-90%）进一步突显了其鲁棒性，因为与树集成模型相比，其性能下降平缓且敏感性极低。在量子任务中，TabPFN 在 QM7 上表现出具有竞争力的准确性，但在较大的 QM8 数据集上受到挑战，此时树集成模型重新占据优势。除了指标之外，嵌入分析表明 TabPFN 具有更平滑的结构-性质关系和增强的类别可分性，反映了有益的归纳偏置而非过拟合。总之，这些发现表明 TabPFN 为药物研发中的表格学习提供了一种鲁棒且高效的数据替代方案，为应对小样本和 OOD 挑战下的预测建模提供了新思路。

## Abstract
Early-stage drug discovery often suffers from data scarcity and out-of-distribution (OOD) shifts, which constrain the reliability of predictive models. While deep learning has advanced representation learning from molecular and biological data, tabular modeling remains indispensable, particularly in small-sample and OOD scenarios. For more than a decade, gradient-boosted decision trees (GBDTs), such as XGBoost, have been the dominant choice, yet their robustness is limited under such conditions. TabPFN, a recently introduced transformer-based tabular foundation model, enables accurate predictions on small data sets without task-specific retraining. Applying TabPFN to a variety of molecular data sets, we find that TabPFN performs on par with XGBoost in classification but demonstrates clear and stable advantages in regression, with its strongest gains on small and medium data sets and under OOD evaluations. Feature and data ablations (10-90%) further highlight its robustness, as performance degrades gracefully and exhibits minimal sensitivity compared with tree ensembles. On quantum tasks, TabPFN shows competitive accuracy on QM7 but is challenged by the larger QM8 data set, where tree ensembles regain strength. Beyond metrics, embedding analyses indicate smoother structure-property relationships of TabPFN and enhanced class separability, reflecting beneficial inductive biases rather than overfitting. Collectively, these findings demonstrate that TabPFN offers a robust and data-efficient alternative for tabular learning in drug discovery, shedding new light on predictive modeling under small-data and OOD challenges.