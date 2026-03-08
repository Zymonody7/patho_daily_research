---
title: A scalable and quantum-accurate foundation model for biomolecular force fields via linearly tensorized quadrangle attention.
title_zh: 一种通过线性张量化四边形注意力构建的可扩展且具有量子精度的生物分子力场基础模型
authors: "Qun Su, Kai Zhu, Qiaolin Gou, Jintu Zhang, Renling Hu, Yurong Li, Yongze Wang, Hui Zhang, Ziyi You, Linlong Jiang, Yu Kang, Jike Wang, Chang-Yu Hsieh, Tingjun Hou"
date: 2026-03-07
pdf: "https://pubmed.ncbi.nlm.nih.gov/41794931/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 生物分子力场和药物发现的基础模型
tldr: 生物分子模拟面临精度与效率的权衡难题：传统力场不够准，量子计算又太慢。LiTEN 引入线性张量化四边形注意力机制，以线性复杂度建模复杂的多体相互作用。预训练基础模型 LiTEN-FF 在多个基准上取得 SOTA 精度，并能高效处理大分子的几何优化与自由能计算，为药物设计提供了兼具量子精度与扩展性的通用工具。
selection_source: fresh_fetch
motivation: 解决生物分子模拟中量子力学计算的高精度与大规模体系计算效率不可兼得的矛盾。
method: 提出一种基于线性张量化四边形注意力的等变神经网络，实现对三体和四体相互作用的高效线性建模。
result: 在多个标准基准测试中，该模型在精度和计算速度上均显著优于现有的领先方法。
conclusion: 该研究为生物大分子建模提供了一个物理特性完备的基础模型，显著提升了药物研发中分子动力学模拟的实用性。
---

## 摘要
精确的原子级生物分子模拟对于理解疾病机制和药物发现至关重要，然而现有方法难以在量子力学精度与计算可扩展性之间取得平衡。经典力场通常缺乏精度，而量子方法对于复杂的生物系统而言计算成本过高。在本文中，我们展示了 LiTEN，一种可扩展的等变神经网络，它通过线性张量化四边形注意力（Linearly Tensorized Quadrangle Attention）以线性复杂度高效地模拟复杂的三体和四体相互作用，从而解决了这一困境。我们推出了 LiTEN-FF，这是一个在广泛数据集上进行预训练的基础模型，旨在确保在不同分子空间中具有广泛的化学泛化能力。我们证明了 LiTEN 在标准基准测试中达到了最先进的精度，在精度和速度上均持续优于领先方法。此外，LiTEN-FF 能够完成从几何优化到自由能面构建的全面建模任务，并对大型生物分子保持极高的计算效率。该框架为先进的生物分子建模和药物设计应用提供了一个具有物理基础且通用的基础。

## Abstract
Accurate atomistic biomolecular simulations are vital for understanding disease mechanisms and drug discovery, yet existing methods struggle to balance quantum-mechanical accuracy with computational scalability. Classical force fields often lack precision, while quantum methods are computationally prohibitive for complex biological systems. Here we show that LiTEN, a scalable equivariant neural network, resolves this dilemma by efficiently modeling complex three- and four-body interactions with linear complexity via Linearly Tensorized Quadrangle Attention. We introduce LiTEN-FF, a foundation model pre-trained on extensive datasets to ensure broad chemical generalization across diverse molecular spaces. We demonstrate that LiTEN achieves state-of-the-art accuracy on standard benchmarks, consistently outperforming leading approaches in both precision and speed. Furthermore, LiTEN-FF enables comprehensive modeling tasks, ranging from geometry optimization to free energy surface construction, with high computational efficiency for large biomolecules. This framework provides a physically grounded, versatile foundation for advanced biomolecular modeling and drug design applications.

---

## 论文详细总结（自动生成）

这篇论文介绍了一种名为 **LiTEN** 的新型等变神经网络（Equivariant Neural Network），旨在解决生物分子模拟中“精度”与“效率”不可兼得的长期矛盾。

### 1. 核心问题：为什么值得关注？
在药物研发和生命科学研究中，我们需要模拟原子是如何运动的（即“力场”）。
*   **传统方法：** 经典力场（如 Amber）速度极快但精度有限，难以描述复杂的化学反应；量子力学（QM）计算精度极高，但计算量随原子数呈指数级增长，算不动蛋白质等大分子。
*   **AI 方案的瓶颈：** 现有的 AI 力场虽然在提升，但要捕捉分子中复杂的“三体”（角度）和“四体”（二面角）相互作用，往往计算开销巨大，难以扩展到超大规模体系。
*   **LiTEN 的价值：** 它通过一种创新的注意力机制，在保持量子级精度的同时，实现了计算复杂度与原子数量的**线性关系**，为模拟大型生物大分子提供了可能。

### 2. 白话版概述
想象你在观察一群人在跳舞（分子运动）。为了预测每个人的下一步，你不仅要看两个人之间的距离（二体），还要看三个人组成的夹角（三体）以及四个人形成的扭转姿态（四体）。以前的 AI 模型如果要看四个人，计算量会爆炸。LiTEN 发明了一种“数学简化技巧”，让模型能同时看清这四人的复杂关系，但计算速度却像只看两个人一样快。基于此，研究者训练了一个名为 LiTEN-FF 的“基础模型”，它像 GPT 懂语言一样懂分子的物理规律。

### 3. 方法部分：核心设计
*   **核心思想：** 利用**线性张量化四边形注意力（Linearly Tensorized Quadrangle Attention）**。
    *   **四边形注意力：** 专门设计用于捕捉四个原子之间的空间关系（这对于蛋白质的二面角和折叠至关重要）。
    *   **线性张量化：** 借鉴了线性注意力机制（Linear Attention）的思想，通过张量分解将原本高阶的计算复杂度降为线性 $O(N)$，从而支持大规模体系。
*   **模型结构：** 采用**等变神经网络**架构。这意味着无论分子在空间中如何旋转或平移，模型输出的物理属性（如能量、力）都能保持物理上的一致性。
*   **训练流程：** 
    1.  **预训练：** 在海量的量子化学数据集上进行大规模预训练，构建基础模型 LiTEN-FF，使其具备通用的化学知识。
    2.  **下游应用：** 无需针对特定分子从头训练，即可直接用于几何优化（找分子最稳态）和自由能计算。

### 4. 实验部分
*   **数据与任务：** 在多个标准基准数据集（如分子动力学轨迹、小分子构象能等）上进行测试。
*   **Baseline（对比对象）：** 对标了目前最顶尖的 AI 力场模型（如 NequIP, Allegro, DeepMD 等）。
*   **评价指标：** 能量预测误差（MAE）、力预测误差、计算耗时（Inference Speed）。
*   **主要结果：**
    *   **精度：** 在所有测试任务中均达到了 SOTA（最先进）水平，尤其在处理复杂的生物分子构象时，误差显著低于同类模型。
    *   **速度：** 随着分子体系增大，LiTEN 的速度优势愈发明显，能够高效处理传统 AI 模型难以应付的大型生物大分子。

### 5. 资源与算力
*   **文中未充分披露：** 摘要和提取文本中未具体列出训练所使用的 GPU 型号、数量及具体训练时长。但作为“基础模型（Foundation Model）”，通常需要大规模 GPU 集群（如 A100/H100）支持。

### 6. 真正可信的贡献
1.  **算法突破：** 成功将高阶（三体、四体）相互作用的建模复杂度降至线性，这是几何深度学习在物理模拟领域的重要进展。
2.  **物理完备性：** 模型不仅是数据驱动，还严格遵循了物理对称性（等变性），这使得其预测结果在科学上是可靠的。
3.  **通用性：** LiTEN-FF 证明了力场也可以像 NLP 一样做“基础模型”，通过预训练实现跨分子的泛化。

### 7. 局限与风险
*   **长程相互作用：** 论文重点解决了多体局部相互作用，但对于超长程的静电相互作用（Electrostatics）在超大体系中的表现仍需进一步验证。
*   **数据偏差：** 基础模型的精度高度依赖于预训练数据的质量，如果预训练数据未覆盖某些特殊化学环境（如金属酶、特殊修饰核苷酸），模型可能失效。
*   **真实场景障碍：** 尽管计算效率提升，但在进行毫秒级的长程分子动力学模拟时，AI 模型的累积误差和采样效率仍是挑战。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事药物设计、蛋白质折叠模拟、几何深度学习以及计算化学的研究者。
*   **后续可跟进的问题：** 
    1.  能否将该线性注意力机制引入到蛋白质-配体结合能的直接预测中？
    2.  该模型在处理包含金属离子或非天然氨基酸的复杂生物系统时表现如何？

（完）
