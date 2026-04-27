---
title: "DrugGPS: Attention-guided multimodal fusion for intelligent exploration of drug-target and drug-disease interactions."
title_zh: DrugGPS：用于药物-靶点和药物-疾病相互作用智能探索的注意力引导多模态融合
authors: "Huifeng Yao, Xinyi Yang, Yu Wang, Chenxiao Wang, Yiming Sun, Yunya Jiang, Li Liang, Qing Zhang, Haichun Liu, Hongmei Li, Xian Wei, Yadong Chen, Mengyi Lu, Yanmin Zhang"
date: 2026-04-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/42037091/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 药物-靶点和药物-疾病相互作用的多模态融合
tldr: 药物研发中准确预测药物-靶点（DTI）和药物-疾病（DDI）相互作用至关重要，但单一模态数据难以捕捉复杂的生化关系。DrugGPS 框架通过注意力机制融合了药物结构、序列、生物网络及相似性图谱等多模态数据，并引入 MeSH 疾病特征。实验证明该模型在预测精度和效率上优于现有方法，并成功识别出 MR 受体的活性化合物，为药物重定向提供了高效工具。
selection_source: fresh_fetch
motivation: 传统的单模态预测方法难以全面刻画药物、靶点与疾病之间复杂的生化和药理联系，限制了预测的准确性与泛化能力。
method: 提出 DrugGPS 框架，利用注意力机制融合药物分子结构、蛋白质序列、生物关联网络及相似性图谱，并整合 MeSH 疾病特征进行统一建模。
result: 在多个公开数据集上超越了现有最先进模型，并通过案例研究成功筛选出 4 个经实验验证的盐皮质激素受体活性化合物。
conclusion: 该研究证明了多模态融合策略在提升 DTI 和 DDI 预测性能方面的有效性，为加速药物发现和老药新用提供了智能化支持。
---

## 摘要
背景与目的：准确预测药物-靶点相互作用（DTIs）和药物-疾病相互作用（DDIs）对于加速药物研发过程至关重要。然而，传统的单模态方法难以捕捉药物与靶点之间复杂的生化和药理关系，从而限制了模型的准确性和泛化能力。因此，开发能够提升预测性能的创新方法至关重要。实验方法：为了克服这些局限性，我们推出了 DrugGPS，这是一种新型的多模态预测框架。DrugGPS 整合了异构生物数据，采用由注意力机制引导的多通道特征融合策略，实现高精度的 DTI 和 DDI 预测。主要结果：DrugGPS 整合了结构和序列表示、生物关系网络以及基于相似性的图，以学习丰富的特征嵌入。它采用基于注意力的融合模块来提取和整合跨通道信息，增强了其表征复杂化学-生物相互作用的能力。此外，该框架还纳入了源自 MeSH 的疾病特征，以统一药物-靶点-疾病关联的建模，从而为治疗机制提供更深入的见解。针对盐皮质激素受体（MR）的案例研究验证了该模型的实用性，识别出四种经过实验验证的活性化合物。开发了一个交互式可视化平台，用于探索预测的 DTI 和 DDI 相互作用。在公共数据集上的广泛实验表明，DrugGPS 在准确性、鲁棒性和计算效率方面优于现有最先进的方法，展示了其在智能药物研发和老药新用方面的潜力。结论与意义：这些发现表明 DrugGPS 具有提高 DTI 和 DDI 相互作用预测以用于老药新用的潜力，以及在加速药物开发和发现方面的潜力。

## Abstract
BACKGROUND AND PURPOSE: Accurate prediction of drug-target interactions (DTIs) and drug-disease interactions (DDIs) are critical for accelerating the drug discovery process. However, conventional unimodal approaches struggle to capture the complex biochemical and pharmacological relationships between drugs and targets, thereby limiting model accuracy and generalisability. Hence, it is essential to develop innovative approaches that can enhance predictive performance. EXPERIMENTAL APPROACH: To overcome these limitations, we introduce DrugGPS as a novel multimodal predictive framework. DrugGPS integrates heterogeneous biological data, using a multi-channel feature fusion strategy guided by attention mechanisms for highly accurate DTI and DDI prediction. KEY RESULTS: DrugGPS integrates structural and sequential representations, biological relational networks and similarity-based graphs to learn enriched feature embeddings. It adopts an attention-based fusion module to distil and integrate cross-channel information, strengthening its ability to characterise complex chemical-biological interactions. Additionally, the framework incorporates MeSH-derived disease features to unify the modelling of drug-target-disease associations, thus providing deeper insights into therapeutic mechanisms. A case study on the mineralocorticoid receptor (MR) verifies its utility with the model by identifying four experimentally validated active compounds. An interactive visualisation platform was developed to explore predicted DTI and DDI interactions. Extensive experiments on public datasets show that DrugGPS outperforms state-of-the-art methods in accuracy, robustness and computational efficiency, demonstrating its potential for intelligent drug discovery and repositioning. CONCLUSION AND IMPLICATIONS: These findings indicate the potential of DrugGPS to improve DTI and DDI interaction predictions for drug repositioning, and its potential in accelerating drug development and discovery.

---

## 论文详细总结（自动生成）

这篇论文介绍了一个名为 **DrugGPS** 的深度学习框架，旨在通过整合多种生物信息数据，更准确地预测药物与蛋白质靶点（DTI）以及药物与疾病（DDI）之间的相互作用。

### 1. 解决的问题与研究意义
在药物研发中，预测“哪个药能对付哪个蛋白质”或“哪个药能治哪种病”是核心问题。
*   **痛点**：传统的 AI 模型通常只看单一数据（比如只看药物的化学结构，或只看蛋白质的氨基酸序列）。但这就像只看锁的形状而不看钥匙的材质，信息不全导致预测不准，且难以解释复杂的生化反应。
*   **意义**：DrugGPS 通过“多模态融合”技术，把药物结构、蛋白质序列、生物关联网络等多种信息揉在一起，提高了预测精度。这对于“老药新用”（寻找现有药物的新用途）和加速新药筛选具有直接的临床和商业价值。

### 2. 白话版概述
想象你要判断一个新厨师（药物）能不能做好一道复杂的名菜（靶点/疾病）。
*   以前的方法可能只看厨师的简历（化学结构）。
*   **DrugGPS** 不仅看简历，还看他的拿手菜视频（蛋白质序列）、他的社交圈（生物网络，看他认识哪些厉害的厨师）、以及菜谱的分类标签（MeSH 疾病特征）。
*   它利用一种“注意力机制”来当裁判，自动判断在面对这道菜时，简历、视频和社交圈哪个信息更重要，最后给出一个精准的匹配得分。

### 3. 方法部分
*   **核心思想**：多模态特征对齐与融合。模型认为单一维度的特征是不完整的，必须通过跨通道的信息互补来捕捉深层关联。
*   **模型结构**：
    *   **特征提取层**：分别处理药物（SMILES 字符串和分子图）、靶点（氨基酸序列）和疾病（MeSH 描述符）。
    *   **图学习模块**：利用图神经网络（GNN）处理药物-药物、蛋白质-蛋白质的相互作用网络，捕捉“邻居”信息。
    *   **注意力引导融合（Attention-guided Fusion）**：这是核心设计。它不是简单地把特征拼接，而是通过注意力权重，让模型学习在不同场景下哪些模态的数据更具决定性。
    *   **统一建模**：将 DTI 和 DDI 放在同一个框架下处理，引入 MeSH（医学主题词表，一种标准化的生物医学词典）来增强疾病特征的语义表达。
*   **关键取舍**：放弃了单一的大模型，选择了多通道并行结构，以平衡计算效率和特征的丰富度。

### 4. 实验部分
*   **数据与任务**：在多个公开的 DTI 和 DDI 基准数据集上进行测试。
*   **Baseline（对比方法）**：对比了当前最先进的（SOTA）深度学习模型，如基于图卷积或 Transformer 的预测模型。
*   **评价指标**：主要使用 AUC（曲线下面积）、AUPRC（精准率-召回率曲线面积）和准确率。
*   **主要结果**：
    *   DrugGPS 在各项指标上均优于现有模型。
    *   **湿实验验证（最强证据）**：针对盐皮质激素受体（MR，一种与高血压相关的蛋白质），模型筛选出了 4 个活性化合物，并经过了真实的实验室生化实验验证，证明预测确实有效。

### 5. 资源与算力
*   **文中未充分披露**具体的 GPU 型号、训练时长或显存占用等硬件细节。

### 6. 论文的可信贡献
*   **多模态整合能力**：成功证明了将 MeSH 疾病特征与分子结构结合能显著提升预测效果。
*   **闭环验证**：不仅有计算机模拟（In silico），还有真实的生化实验验证，这在 AI 药研论文中属于“金标准”证据。
*   **可视化工具**：开发了交互式平台，让非 AI 背景的生物学家也能直观查看预测结果。

### 7. 局限与风险
*   **数据偏差**：公开数据集往往存在“正样本”过多的问题，模型在处理完全未知的“孤儿靶点”（研究极少的蛋白质）时可能表现下降。
*   **解释性挑战**：虽然使用了注意力机制，但要具体解释“为什么这个分子能结合这个蛋白”的底层物理化学机制，模型仍显不足。
*   **冷启动问题**：对于没有任何已知相互作用记录的新分子，多模态中的“网络特征”会失效，此时模型性能高度依赖结构模态。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事药物虚拟筛选、蛋白质组学、以及图机器学习的研究者。
*   **后续可跟进的问题**：如何利用大语言模型（LLM）生成的知识图谱来进一步增强 MeSH 这种静态特征的动态语义表达？

（完）
