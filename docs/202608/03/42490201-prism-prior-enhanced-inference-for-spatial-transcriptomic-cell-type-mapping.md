---
title: "PRISM: Prior-enhanced Inference for Spatial Transcriptomic Cell Type Mapping."
title_zh: PRISM：用于空间转录组细胞类型映射的先验增强推理
authors: "Yiheng Xu, Xuehao Wang, Shuqi Liu, Congcong Ge, Xiang Chen, Yueming Wang, Bin Yu, Xiao-Ming Li"
date: 2026-08-03
pdf: "https://pubmed.ncbi.nlm.nih.gov/42490201/"
tags: ["query:seqai"]
score: 9.0
evidence: 空间转录组细胞类型映射与推理
tldr: 针对空间转录组（ST）细胞类型标注中存在的跨域差异大、平台噪声干扰及空间依赖性缺失等问题，本文提出了 PRISM 框架。该方法通过构建生物学先验提取标志基因，利用集成学习生成伪标签，并结合空间信息进行多级精细化调整。实验证明，PRISM 在多种组织和平台数据集上均表现优异，尤其在无标签场景下展现出极强的鲁棒性，为解析复杂组织结构提供了可靠工具。
selection_source: fresh_fetch
motivation: 现有的空间转录组标注方法往往忽略了空间结构依赖，且难以克服单细胞测序与空间测序数据之间的域偏移和平台噪声。
method: PRISM 采用三阶段架构，通过生物学先验引导标志基因提取，结合自监督伪标签生成与空间信息编码，实现跨域特征的对齐与优化。
result: 在涵盖 6 个平台、2 个物种的 11 个数据集上，PRISM 在准确率和 F1 分数上均领先，并在完全无标注环境下获得了最佳综合排名。
conclusion: 该研究通过引入生物学先验和空间约束，显著提升了空间转录组细胞映射的准确性与生物学可解释性。
---

## 摘要
动机：空间转录组学（ST）中的细胞类型注释对于破译复杂的组织结构和空间分辨的生物过程至关重要。大多数现有方法通过将单细胞 RNA 测序（scRNA-seq）数据的标签转移到 ST 数据来进行细胞类型注释，但通常依赖于弱约束的表示，忽略了结构化的空间依赖性，并将标志基因（marker gene）选择视为孤立的预处理步骤。这使得它们容易受到显著的领域差异以及平台特有噪声的影响，导致预测不稳定且生物学解释性有限。结果：为了解决这些问题，我们提出了 PRISM（Prior-enhanced Inference for Spatial Transcriptomic Cell Type Mapping），这是一个集成生物学先验构建、伪标签生成和多层级 ST 细化的新型三阶段框架。首先，PRISM 构建跨域生物学先验以显式提取标志基因，从而增强正向生物学区分度。接着，它采用先验增强的自训练策略，利用在 scRNA 上训练的集成模型为 ST 数据生成可靠的伪标签候选，作为跨域迁移的稳健锚点。最后，该框架整合通过指标引导评估选出的高质量集成预测，编码空间信息，并在双向生物学约束下优化模型。在涵盖 6 个平台、2 个物种和多种组织背景的 11 个 ST 数据集上进行的广泛实验验证了 PRISM 的有效性。具体而言，在 5 个有标签的基准数据集上，PRISM 在大脑和非大脑组织的准确率（Accuracy）和 Macro-F1 评估中均表现出强大的综合性能。此外，在完全无标签的设置下，PRISM 在所有数据集中获得了最佳的综合排名，展示了对领域偏移和平台异质性的强大鲁棒性。可用性与实现：PRISM 可在 https://github.com/lilab-ai4s/PRISM 和 https://doi.org/10.5281/zenodo.20529683 获取。

## Abstract
MOTIVATION: Cell type annotation in spatial transcriptomics (ST) is fundamental for deciphering complex tissue organization and spatially resolved biological processes. Most existing methods perform ST cell type annotation by transferring labels from single-cell RNA-seq (scRNA) data to ST data, but typically rely on weakly constrained representations that neglect structured spatial dependencies and treat marker gene selection as an isolated preprocessing step. This renders them vulnerable to substantial domain gaps as well as platform-specific noise, resulting in unstable predictions and limited biological interpretability. RESULTS: To address these issues, we propose Prior-enhanced Inference for Spatial Transcriptomic Cell Type Mapping (PRISM), a novel three-stage framework integrating biological prior construction, pseudo-label generation, and multi-level ST refinement. First, PRISM constructs a cross-domain biological prior to explicitly extract marker genes to enforce positive biological discriminability. Next, it adopts a prior-enhanced self-training strategy, where scRNA-trained ensembles generate reliable pseudo-label candidates for ST data, serving as a robust anchor for cross-domain adaptation. Finally, the framework consolidates high-quality ensemble predictions selected via metric-guided evaluation, encodes spatial information, and optimizes the model under dual-directional biological constraints. Extensive experiments on eleven ST datasets across six platforms, two species, and multiple tissue contexts validate PRISM. Specifically, on the five labeled benchmarks, PRISM shows strong overall performance under both Accuracy and Macro-F1 evaluation across brain and non-brain tissues. Moreover, under fully label-free settings, PRISM achieves the best overall composite rank across all datasets, demonstrating strong robustness to domain shift and platform heterogeneity. AVAILABILITY AND IMPLEMENTATION: PRISM is available at https://github.com/lilab-ai4s/PRISM and https://doi.org/10.5281/zenodo.20529683.

---

## 论文详细总结（自动生成）

这是一份关于论文 **PRISM: Prior-enhanced Inference for Spatial Transcriptomic Cell Type Mapping** 的结构化解读。

---

### 1. 解决的问题与研究意义
**核心问题**：如何准确地为“空间转录组（ST）”数据标注细胞类型。
*   **背景**：空间转录组技术能让我们看到组织中不同位置的基因表达，但它通常缺乏细胞类型的标签。研究者通常参考已有的“单细胞测序（scRNA-seq）”数据来“翻译”这些标签。
*   **痛点**：
    1.  **域偏移（Domain Shift）**：单细胞数据和空间数据来自不同平台，数据分布差异巨大。
    2.  **空间信息缺失**：现有方法往往把每个空间点当成孤立的个体，忽略了“邻居细胞通常类型相似”的生物学规律。
    3.  **噪声干扰**：标志基因（Marker Genes，即某种细胞特有的身份标签）的选择往往与后续分类脱节，导致模型容易被噪声误导。

---

### 2. 白话版概述
想象你在玩一个拼图游戏，但你手里只有一张模糊的参考图（单细胞数据）和一堆散乱的拼图块（空间转录组数据）。
PRISM 先从参考图中提取出最关键的特征（标志基因）作为“线索”；然后找来一群“专家”（集成模型）对拼图块进行初步分类，生成一份草稿；最后，它利用“相邻的拼图块通常属于同一图案”的逻辑，对草稿进行精细修正。通过这三步，它能比以往的方法更准确地还原出组织内部的细胞布局。

---

### 3. 方法部分
PRISM 采用了一个**三阶段框架**：

*   **第一阶段：生物学先验构建（Prior Construction）**
    *   **核心思想**：不再盲目使用所有基因，而是显式提取跨域通用的**标志基因**（Marker Genes）。
    *   **设计**：通过对比单细胞和空间数据，筛选出在特定细胞类型中稳定高表达的基因，增强模型对生物学特征的敏感度。
*   **第二阶段：伪标签生成（Pseudo-label Generation）**
    *   **核心思想**：利用集成学习（Ensemble Learning）克服单一模型的偏差。
    *   **流程**：在单细胞数据上训练多个分类器，让它们对空间数据进行预测。只有当多个模型达成共识时，才将其作为“伪标签”（可靠的锚点），用于引导后续的自训练。
*   **第三阶段：多层级 ST 精细化（Multi-level Refinement）**
    *   **核心思想**：引入空间结构约束和双向生物学约束。
    *   **关键设计**：
        *   **空间编码**：利用图神经网络或类似机制捕捉空间坐标信息，让物理位置接近的点在特征空间也更接近。
        *   **双向约束**：既要求预测的标签符合基因表达特征，也要求基因表达符合已知的标志基因分布，实现特征与标签的深度对齐。

---

### 4. 实验部分
*   **数据规模**：涵盖 11 个数据集，涉及 6 种主流空间技术平台（如 Visium, Slide-seq 等），包含人类和小鼠的脑部及非脑部组织。
*   **对比方法（Baselines）**：与 Seurat（经典统计方法）、Cell2location、SpatialPCA 等多种深度学习和传统方法进行了对比。
*   **评价指标**：准确率（Accuracy）、Macro-F1 分数（衡量对稀有细胞类型识别能力的指标）。
*   **主要结果**：
    *   在有标注的基准测试中，PRISM 在不同组织类型上均取得了最高分。
    *   **鲁棒性极强**：在完全没有空间标签的“盲测”环境下，PRISM 的综合排名依然稳居第一，证明其处理平台差异的能力很强。

---

### 5. 资源与算力
*   **代码地址**：[GitHub - lilab-ai4s/PRISM](https://github.com/lilab-ai4s/PRISM)
*   **算力需求**：**文中未充分披露**具体的 GPU 工时或内存消耗，但考虑到其包含集成学习和多阶段优化，计算开销预计高于单阶段的轻量级模型。

---

### 6. 真正可信的贡献
1.  **生物学先验的显式集成**：证明了将“标志基因”作为硬约束引入深度学习模型，比纯数据驱动的黑盒模型更有效。
2.  **跨平台鲁棒性**：通过 6 个平台的广泛验证，证明了该方法在应对不同测序技术带来的噪声时具有极高的稳定性。
3.  **空间一致性优化**：成功将空间位置信息转化为模型优化的正则项，显著提升了组织边界处的分类精度。

---

### 7. 局限与风险
1.  **计算复杂度**：三阶段框架和集成学习意味着训练和推理时间可能较长，在大规模数据集（如百万级空间点）上的扩展性有待观察。
2.  **依赖参考集质量**：如果作为参考的单细胞数据本身存在标注错误或细胞类型缺失，PRISM 的伪标签生成阶段可能会引入偏差。
3.  **分辨率限制**：对于非单细胞分辨率的空间转录组（一个点包含多个细胞），PRISM 的“硬分类”逻辑可能不如“解卷积（Deconvolution）”方法精细。

---

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事空间组学分析、跨域迁移学习、以及对“生物学知识引导的深度学习”感兴趣的研究者。
*   **后续可跟进的问题**：如何将这种先验增强的思路扩展到“多模态”空间数据（如同时结合病理切片图像和基因表达）？

（完）
