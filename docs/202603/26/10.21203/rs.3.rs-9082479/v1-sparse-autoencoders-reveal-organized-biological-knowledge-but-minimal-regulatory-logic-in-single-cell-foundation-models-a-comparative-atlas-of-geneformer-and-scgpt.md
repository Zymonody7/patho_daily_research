---
title: "Sparse autoencoders reveal organized biological knowledge but minimal regulatory logic in single-cell foundation models: a comparative atlas of Geneformer and scGPT"
title_zh: 稀疏自编码器揭示了单细胞基础模型中组织的生物学知识，但调控逻辑极少：Geneformer 与 scGPT 的比较图谱
authors: Kendiukhov I.
date: 2026-03-25
pdf: "https://doi.org/10.21203/rs.3.rs-9082479/v1"
tags: ["query:bioinfo"]
score: 9.0
evidence: 使用稀疏自编码器评估单细胞基础模型 Geneformer 和 scGPT
tldr: 单细胞大模型（如Geneformer和scGPT）是否真正理解基因调控逻辑尚不明确。本研究利用稀疏自编码器（SAE）对这两个模型的内部激活进行了解构，构建了包含超过10万个特征的解释性图谱。研究发现，模型虽然成功学习了复杂的生物学知识（如通路、蛋白质相互作用和层级结构），但在应对CRISPRi扰动实验时表现出极弱的因果调控逻辑。这一结果揭示了当前单细胞模型在模拟基因调控网络方面的局限性，并为模型改进提供了方向。
selection_source: fresh_fetch
motivation: 旨在探究单细胞大模型内部表征的是真实的基因因果调控逻辑，还是仅仅捕捉了统计学上的基因共表达关系。
method: 通过在Geneformer和scGPT的各层残差流上训练TopK稀疏自编码器，将稠密的神经元激活分解为数万个可解释的稀疏特征。
result: "研究构建了包含10.7万个特征的图谱，证实模型虽能高度组织化地表征生物通路和功能模块，但在CRISPRi扰动测试中仅有约6%的转录因子展现出特异性的因果调控响应。"
conclusion: 单细胞大模型已内化了丰富的生物学知识，但在捕捉深层因果调控逻辑方面仍存在显著局限，模型表征能力是当前理解复杂调控机制的主要瓶颈。
---

## 摘要
背景：Geneformer 和 scGPT 等单细胞基础模型编码了丰富的生物学信息，但这些信息是否包含因果调控逻辑而非仅仅是统计共表达仍不清楚。稀疏自编码器（SAEs）可以通过将密集激活分解为可解释的特征来解决神经网络中的叠加（superposition）问题，但尚未系统地应用于生物学基础模型。结果：我们在 Geneformer V2-316M（18 层，d=1,152）和 scGPT 全人类模型（12 层，d=512）所有层的残差流激活上训练了 TopK SAEs，分别生成了包含 82,525 和 24,527 个特征的图谱。两个图谱均证实了大规模叠加现象的存在，其中 99.8% 的特征在奇异值分解（SVD）中是不可见的。系统表征揭示了丰富的生物学组织结构：29–59% 的特征可注释到 Gene Ontology、KEGG、Reactome、STRING 或 TRRUST，其 U 型层分布反映了层次化抽象。特征组织成共激活模块（Geneformer 中有 141 个，scGPT 中有 76 个），表现出因果特异性（中位数为 2.36 倍），并形成了跨层信息高速公路（63–99.8%）。在针对全基因组规模的 CRISPRi 扰动数据进行测试时，48 个转录因子中仅有 3 个（6.2%）表现出针对特定调控靶点的特征响应。多组织对照仅带来微小改善（10.4%，48 个转录因子中的 5 个），这表明模型表征是瓶颈所在。结论：这些模型已经内化了有组织的生物学知识，包括通路成员身份、蛋白质相互作用、功能模块和层次化抽象，但它们编码的因果调控逻辑极少。我们将这两个特征图谱作为交互式网络平台发布，支持对两种领先单细胞基础模型 30 层中超过 107,000 个特征的探索。

## Abstract
<title>Abstract</title>  <p>Background: Single-cell foundation models such as Geneformer and scGPT encode rich biological information, but whether this includes causal regulatory logic rather than statistical co-expression remains unclear. Sparse autoencoders (SAEs) can resolve superposition in neural networks by decomposing dense activations into interpretable features, yet they have not been systematically applied to biological foundation models. <h4>Results:</h4> We trained TopK SAEs on residual stream activations from all layers of Geneformer V2-316M (18 layers, d=1,152) and scGPT whole-human (12 layers, d=512), producing atlases of 82,525 and 24,527 features, respectively. Both atlases confirm massive superposition, with 99.8% of features invisible to SVD. Systematic characterization reveals rich biological organization: 29–59% of features annotate to Gene Ontology, KEGG, Reactome, STRING, or TRRUST, with U-shaped layer profiles reflecting hierarchical abstraction. Features organize into co-activation modules (141 in Geneformer, 76 in scGPT), exhibit causal specificity (median 2.36×), and form cross-layer information highways (63–99.8%). When tested against genome-scale CRISPRi perturbation data, only 3 of 48 transcription factors (6.2%) show regulatory-target-specific feature responses. A multi-tissue control yields marginal improvement (10.4%, 5 of 48 TFs), establishing model representations as the bottleneck. <h4>Conclusions:</h4> These models have internalized organized biological knowledge, including pathway membership, protein interactions, functional modules, and hierarchical abstraction, yet they encode minimal causal regulatory logic. We release both feature atlases as interactive web platforms enabling exploration of more than 107,000 features across 30 layers of two leading single-cell foundation models.</p>

---

## 论文详细总结（自动生成）

这篇论文利用大语言模型（LLM）领域前沿的可解释性工具——**稀疏自编码器（SAE）**，对目前最流行的两个单细胞基础模型（Geneformer 和 scGPT）进行了“开颅手术”。

### 1. 解决的问题与核心价值
**问题：** 现在的单细胞大模型（scFMs）虽然在很多任务上表现不错，但它们到底学到了什么？它们是像人类专家一样理解了基因之间的**因果调控逻辑**（例如：基因 A 表达增加会导致基因 B 减少），还是仅仅记住了哪些基因经常一起出现的**统计相关性**？

**价值：** 这是首次系统性地将 SAE 应用于生物学基础模型。研究揭示了一个残酷的现实：虽然模型内部高度组织化地存储了海量的生物学知识（如代谢通路、蛋白相互作用），但在面对真实的基因编辑（CRISPRi）扰动实验时，它们几乎无法预测出正确的调控反应。这为“大模型是否真的懂生物”提供了量化的科学证据。

---

### 2. 白话版概述
想象单细胞模型是一个读过几百万份细胞“简历”的 AI。
*   **它很聪明：** 它知道哪些基因是“同事”（在同一个通路里），哪些基因是“邻居”（在同一个细胞器里）。
*   **它很糊涂：** 如果你问它“如果我把老板（转录因子）开除了，哪些员工（下游基因）会罢工？”，它基本答不上来。
*   **结论：** 现在的模型更像是一本内容丰富的“生物百科全书”，而不是一个能模拟生命运行的“实验室”。

---

### 3. 方法部分：SAE 拆解技术
*   **核心思想：** 神经网络的神经元存在“叠加（Superposition）”现象，即一个神经元可能同时代表多个生物学概念。**稀疏自编码器（SAE）** 的作用是将这些挤在一起的信号“解压”成数万个独立的、具有明确生物学意义的“特征（Features）”。
*   **模型结构：** 针对 Geneformer（18层）和 scGPT（12层）的每一层**残差流（Residual Stream）**训练了 TopK SAE。
    *   **残差流：** 可以理解为 Transformer 模型中信息传输的主干道。
    *   **TopK 机制：** 强制模型在解释某次激活时，只能使用极少数（K个）特征，从而保证了特征的稀疏性和可解释性。
*   **关键设计：** 研究者构建了一个包含 10.7 万个特征的图谱，并利用 Gene Ontology（基因功能注释）、KEGG（通路）等数据库对这些特征进行自动标注。

---

### 4. 实验部分
*   **数据与任务：**
    1.  **特征标注：** 检查 SAE 提取的特征是否对应已知的生物学模块。
    2.  **CRISPRi 扰动测试：** 使用真实的基因干扰实验数据，观察当某个转录因子（TF）被抑制时，模型内部对应的特征是否会发生符合逻辑的变化。
*   **主要结果：**
    *   **知识组织：** 29%–59% 的特征能精准对应到已知的生物通路或蛋白相互作用网络。模型在深层展现出更高阶的抽象（如细胞类型特异性）。
    *   **调控逻辑匮乏：** 在 48 个转录因子的扰动测试中，**仅有 3 个（6.2%）** 表现出特异性的因果响应。即使换用多组织数据训练，提升也微乎其微。
    *   **叠加现象严重：** 99.8% 的生物学特征在传统的线性降维（如 SVD）中是不可见的，必须依靠 SAE 这种非线性方法才能挖掘出来。

---

### 5. 资源与算力
*   **训练资源：** 文中未充分披露具体的 GPU 型号和训练总时长，但提到针对 Geneformer 和 scGPT 的所有层分别训练了 SAE，这通常涉及大规模的推理激活值存储和二阶优化计算。
*   **产出：** 发布了一个包含 10.7 万个特征的交互式在线图谱，供研究者查询。

---

### 6. 真正可信的贡献
1.  **工具迁移：** 证明了 SAE 是分析生物基础模型内部表征的强有力工具，比传统的注意力图（Attention Map）更具解释力。
2.  **层次化发现：** 证实了模型内部存在从“基础基因功能”到“复杂细胞模块”的层次化抽象结构。
3.  **幻觉揭示：** 强有力地证明了当前模型在**因果推断**上的短板，打破了“模型规模越大就越懂调控”的迷思。

---

### 7. 局限与风险
*   **数据偏差：** 训练基础模型的数据多为稳态数据，缺乏扰动状态的数据，这可能是模型不懂“因果”的根本原因。
*   **SAE 局限：** SAE 虽然能提取特征，但无法修复模型本身的缺陷。如果模型底层就没学到调控逻辑，SAE 只能观察到“无逻辑”的结果。
*   **评估指标：** CRISPRi 实验本身存在噪声，可能导致对模型能力的低估。

---

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事单细胞基础模型开发、基因调控网络（GRN）建模、以及关注 AI 模型可解释性的研究者。
*   **后续可跟进的问题：** 如何在预训练阶段引入“因果约束”或“扰动数据”，而不仅仅是让模型做基因表达量的填空题？

（完）
