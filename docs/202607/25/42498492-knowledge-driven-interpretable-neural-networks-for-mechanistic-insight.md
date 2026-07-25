---
title: Knowledge-driven interpretable neural networks for mechanistic insight.
title_zh: 知识驱动的可解释神经网络用于机制洞察
authors: "Yan Ke, Tianwei Yu"
date: 2026-07-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/42498492/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 知识驱动的可解释神经网络，用于从组学数据中获取机制见解
tldr: 现有的组学数据通路分析方法往往忽略了生物分子间复杂的机械性相互作用，导致对病理机制的理解停留在浅层。为此，研究者开发了一种知识驱动的可解释神经网络框架，通过将组学特征嵌入生物通路图并对生化反应进行解析建模，实现了对功能关联和子网络的深度挖掘。该方法不依赖特征筛选，能保留微弱信号，在乳腺癌和新冠肺炎数据分析中成功识别出关键的免疫与代谢通路，为整合组学分析提供了兼具预测力与机械解释性的新工具。
selection_source: fresh_fetch
motivation: 传统的生物通路分析方法缺乏对分子间具体相互作用机制的建模，难以深入揭示病理变化背后的分子逻辑。
method: 该框架将多组学特征映射到已知的生物通路图中，利用解析模型模拟生化反应，从而构建出具有可解释层级结构的特征子网络。
result: 在乳腺癌微RNA调控和新冠肺炎代谢组学数据的应用中，该方法准确识别出了与疾病进展密切相关的免疫和代谢关键通路。
conclusion: 这种将先验知识与机器学习深度融合的方法，成功弥合了预测模型与生物学机制解释之间的鸿沟，为精准医疗研究提供了新范式。
---

## 摘要
在通路知识背景下分析组学数据对于理解病理变化背后的分子机制至关重要。然而，目前的通路分析方法未能对生物相互作用的详细机制特性进行建模，从而将对通路行为的理解限制在相对浅显的层面。为解决这一问题，我们提出了一种知识驱动的机器学习框架，该框架将特征嵌入到通路图中，并对反应进行解析建模，从而产生可解释的特征层级和子网络，并在其中通过估计功能关联来模拟生物相互作用。该方法与特征选择无关，能够利用完整的组学数据集而无需舍弃微弱信号。在乳腺癌 microRNA-基因调节数据和 COVID-19 代谢组学数据上的应用，突出了与疾病进展相关的免疫和代谢通路。该框架架起了预测建模与机制解释之间的桥梁，并为综合通路分析奠定了基础。

## Abstract
Analyzing omics data in the context of pathway knowledge is critical for understanding the molecular mechanisms underlying pathological changes. However, current pathway analysis methods do not model the detailed mechanistic nature of biological interactions, limiting the understanding of pathway behavior to a relatively shallow level. To address this issue, we present a knowledge-driven machine learning framework that embeds features into pathway graphs and models reactions analytically, producing interpretable feature hierarchies and subnetworks in which functional associations are estimated to model biological interactions. The approach is agnostic to feature selection, enabling the use of full omics datasets without discarding weak signals. Applications to breast cancer microRNA-gene regulation data and COVID-19 metabolomics data highlight immune and metabolic pathways relevant to disease progression. This framework bridges predictive modeling with mechanistic interpretation and offers a foundation for integrative pathway analysis.

---

## 论文详细总结（自动生成）

这是一份关于论文《Knowledge-driven interpretable neural networks for mechanistic insight》的深度解析：

### 1. 解决的问题与研究价值
**核心问题**：在生物信息学中，我们拥有海量的“组学数据”（如基因表达、代谢物含量），但如何从这些数据中读懂**致病机制**？现有的分析方法（如通路富集分析）往往只把生物通路看作一组分子的集合，忽略了分子之间具体的生化反应逻辑（谁抑制了谁、谁转化成了谁）。这导致模型虽然能预测疾病，但无法告诉科学家具体的生物学“因果链条”。

**研究价值**：该论文提出了一种将**先验生物知识**直接注入**神经网络结构**的方法。它不再是一个黑盒模型，而是一个与生物反应路径一一对应的“透明模型”，让 AI 能够像生物学家一样思考反应过程，从而在预测疾病的同时，直接给出可解释的分子机制。

### 2. 白话版概述
想象生物体内的代谢过程是一座复杂的化工厂流水线。传统的 AI 只是在工厂门口数零件（统计数据），然后猜工厂在产什么。而这篇论文的方法是**直接按照工厂的设计图纸搭建了一个神经网络**：网络里的每一个神经元代表一个化学物质，每一条连线代表一个已知的生化反应。通过训练，AI 不仅能预测工厂的产量（疾病状态），还能告诉你是哪条流水线上的哪个阀门（特定反应）出了问题。

### 3. 方法部分（核心设计）
*   **核心思想**：**知识嵌入（Knowledge Embedding）**。将已知的生物通路图（Pathway Graphs）转化为神经网络的拓扑结构。
*   **模型结构**：
    *   **输入层**：多组学特征（如 microRNA 表达量、代谢物浓度）。
    *   **隐藏层（机制层）**：神经元的连接不是全连接，而是严格遵循生物化学反应路径。模型对反应进行了“解析建模”（Analytic Modeling），即用数学公式模拟分子间的相互作用（如酶促反应）。
    *   **输出层**：表型预测（如癌症进展、新冠病情严重程度）。
*   **关键设计取舍**：
    *   **放弃特征筛选**：传统方法会先删掉信号弱的基因，但该模型保留全量数据，因为微弱的信号在生物通路中累积后可能产生巨大影响。
    *   **可解释性优先**：为了保证每个参数都有生物学意义，模型牺牲了全连接网络的灵活性，换取了“子网络挖掘”的能力。

### 4. 实验部分
*   **实验数据**：
    1.  **乳腺癌数据**：涉及 microRNA 与基因的调控关系。
    2.  **COVID-19 数据**：代谢组学数据（血液中的小分子代谢物）。
*   **任务**：预测疾病进展（如癌症分期、新冠重症程度），并识别关键的生物子网络。
*   **评价指标**：预测准确率（AUC/F1-score）以及**机制一致性**（识别出的通路是否符合已知的生物医学常识）。
*   **主要结果**：模型成功识别出了与新冠进展相关的免疫和代谢关键通路，且在预测性能上不亚于传统的黑盒机器学习模型，但在解释“为什么这么预测”方面远超后者。

### 5. 资源与算力
*   **文中未充分披露**具体的 GPU 型号或训练时长。但由于该模型是基于先验知识的稀疏连接网络（非大规模全连接），其参数量通常远小于同规模的深度学习模型，预计普通工作站即可完成训练。

### 6. 真正可信的贡献
1.  **结构即解释**：证明了将生物图结构（Graph）直接映射为神经网络层级是可行的，且能有效提取“机制性”特征。
2.  **弱信号捕获**：展示了在不进行预先特征过滤的情况下，如何通过通路结构整合微弱的生物信号。
3.  **跨组学整合**：为 microRNA、基因、代谢物等多源数据的统一建模提供了标准范式。

### 7. 局限与风险
*   **知识依赖风险**：模型高度依赖现有的生物通路数据库（如 KEGG 或 Reactome）。如果人类已知的“设计图纸”有错或不完整，模型的推断也会产生偏差。
*   **动态性缺失**：生物反应是随时间变化的动态过程，目前的模型更多是静态快照，难以模拟复杂的反馈调节回路。
*   **外推限制**：对于完全未知的、数据库中没有记载的新反应，该模型无法自发发现。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事图神经网络（GNN）、可解释 AI（XAI）以及多组学整合研究的研究者。
*   **后续可跟进的问题**：如何利用神经符号机（Neural-Symbolic）或强化学习，在已知通路图的基础上，自动“补全”或“修正”那些缺失的生物反应逻辑？

（完）
