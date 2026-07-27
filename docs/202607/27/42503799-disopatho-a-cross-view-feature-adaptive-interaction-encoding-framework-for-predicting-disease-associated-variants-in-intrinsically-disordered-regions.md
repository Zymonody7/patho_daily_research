---
title: "DisoPatho: A Cross-View Feature-Adaptive Interaction Encoding Framework for Predicting Disease-Associated Variants in Intrinsically Disordered Regions."
title_zh: DisoPatho：一种用于预测内在无序区域中疾病相关变异的跨视图特征自适应交互编码框架
authors: "Xiaohua Wang, Shaojie Zhang, Hongmei Jiang, Xiao Liang, Wenjun Xue, Hu Hou, Guizhao Liang"
date: 2026-07-26
pdf: "https://pubmed.ncbi.nlm.nih.gov/42503799/"
tags: ["query:seqai"]
score: 8.0
evidence: 深度学习预测疾病相关变异
tldr: "针对内在无序区（IDR）因缺乏稳定结构和高序列变异性导致致病变异预测困难的问题，本研究提出了DisoPatho深度学习框架。该框架采用以突变位点为中心的架构，通过跨视图自适应交互机制，融合了IDR特有的能量表征与蛋白质语言模型（xTrimoPGLM、ESM）的嵌入特征。实验表明，DisoPatho在多个数据集上显著优于现有方法，在系统发育约束较弱的挑战性测试集中，其MCC比AlphaMissense提升了50.2%，为无序蛋白区域的疾病诊断提供了更精准的工具。"
selection_source: fresh_fetch
motivation: 传统的蛋白质变异预测工具依赖稳定的三维结构或多序列比对，难以准确识别缺乏固定结构且高度变异的内在无序区（IDR）中的致病突变。
method: 提出了一种以突变位点为锚点的深度学习框架，利用跨视图交互机制协同整合IDR特有的能量特征与预训练蛋白质语言模型的语义嵌入。
result: 在多个基准数据集上取得了领先的预测性能，特别是在系统发育信号微弱的独立测试集中，其预测精度和覆盖范围均大幅超过AlphaMissense等主流模型。
conclusion: 该研究证明了结合物理化学能量表征与大规模语言模型特征在处理高度灵活蛋白质区域时的优越性，为理解无序区变异的致病机理提供了新视角。
---

## 摘要
准确预测内在无序区域（IDRs）内的变异对于推进疾病诊断和生物医学解释至关重要。然而，IDRs 本身缺乏稳定的结构构象且具有高度的序列变异性，这使得现有的预测器难以在这些区域实现稳健的性能。在此，我们介绍了 DisoPatho，这是一个专门为预测 IDRs 中疾病相关变异而设计的深度学习框架。DisoPatho 采用了一种新型的以突变为中心的架构，利用变异位点作为特征构建和交互的锚点。其核心创新在于一种跨视图自适应特征交互机制，该机制协同整合了 IDR 特异性能量表示与蛋白质语言模型（包括 xTrimoPGLM 和 Evolutionary Scale Modeling）的嵌入。这种策略能够在不需要显式结构描述符、多序列比对或手工设计的保守性评分的情况下，全面捕捉进化约束和理化模式。因此，DisoPatho 表现出更强的判别能力，能更好地适应 IDRs 的高度灵活性。对多个 IDR 数据集的综合评估表明，DisoPatho 显著优于现有方法。在五折交叉验证中，它在两个数据集上分别实现了 0.899 和 0.840 的平均 AUC，以及 0.862 和 0.860 的 ACC。值得注意的是，在一个系统发育约束提供有限判别信号的高度混淆独立测试集中，DisoPatho 在各自可预测变异上的 MCC 较 AlphaMissense 提升了 50.2%，同时实现了更广泛的预测覆盖范围。对预测结果的深入分析进一步证实了该框架在 IDR 特异性场景下的有效性和稳定性。DisoPatho 的代码、数据集和预测结果已发布于 https://github.com/IBHFLab/DisoPatho 供学术使用。

## Abstract
Accurate prediction of variants within intrinsically disordered regions (IDRs) is crucial for advancing disease diagnosis and biomedical interpretation. However, the intrinsic lack of stable structural conformations and the high sequence variability of IDRs make it challenging for existing predictors to achieve robust performance in these regions. Here, we introduce DisoPatho, a deep learning framework specifically tailored for predicting disease-associated variants in IDRs. DisoPatho features a novel mutation-centric architecture that utilizes the variant site as an anchor for feature construction and interaction. The core innovation lies in a cross-view adaptive-feature interaction mechanism, which synergistically integrates IDR-specific energy representations with embeddings from protein language models, including xTrimoPGLM and Evolutionary Scale Modeling. This strategy enables the comprehensive capture of evolutionary constraints and physicochemical patterns without requiring explicit structural descriptors, multiple-sequence alignments, or hand-crafted conservation scores. Consequently, DisoPatho exhibits enhanced discriminative power better adapted to the highly flexible nature of IDRs. Comprehensive evaluations across multiple IDR data sets demonstrate that DisoPatho substantially outperforms existing methods. In 5-fold cross-validation, it achieves average AUCs of 0.899 and 0.840, with ACCs of 0.862 and 0.860 on two data sets. Notably, on a highly confounded independent test set where phylogenetic constraints offer limited discriminative signals, DisoPatho yields a 50.2% relative improvement in MCC over AlphaMissense on their respective predictable variants, while achieving broader prediction coverage. In-depth analyses of the prediction results further confirm the effectiveness and stability of the framework in IDR-specific scenarios. The code, data sets, and predictions for DisoPatho are available for academic use at https://github.com/IBHFLab/DisoPatho.

---

## 论文详细总结（自动生成）

### DisoPatho：针对蛋白质“无序区”致病变异预测的深度学习框架

#### 1. 解决的问题与研究意义
*   **核心问题**：预测蛋白质中**内在无序区域（IDRs）**上的基因变异是否会导致疾病。
*   **背景知识**：传统的蛋白质像是有固定形状的“零件”（如锁和钥匙），但 IDRs 像是“乱绳”，没有稳定的三维结构，且进化速度极快。
*   **研究意义**：现有的主流预测工具（如 AlphaMissense）高度依赖稳定的空间结构或进化保守性（即看这个位置在不同物种间是否变动）。由于 IDRs 既没结构又不保守，传统工具在这些区域表现很差。IDRs 与癌症、神经退行性疾病密切相关，因此开发专门针对这些“混乱区域”的工具至关重要。

#### 2. 白话版概述
蛋白质里有一类区域像面条一样甩来甩去，没有固定形状，这就是 IDRs。当这些“面条”上的氨基酸发生突变时，现有的 AI 往往因为看不出它的形状而“抓瞎”。这篇论文做了一个专门针对“面条区”的 AI 助手 DisoPatho。它不看形状，而是通过分析氨基酸的“物理化学能量”和“蛋白质语言模型”提供的语义信息，精准识别出哪些突变会引发疾病。

#### 3. 方法部分
*   **核心思想**：采用**以突变为中心（Mutation-centric）**的架构。它不试图理解整个蛋白质的长程结构，而是将突变位点作为“锚点”，观察其局部的特征变化。
*   **模型结构**：
    *   **跨视图特征融合**：模型从两个视角观察突变。
        *   **视角 A（能量表征）**：提取 IDR 特有的物理化学能量特征（反映氨基酸之间的相互作用力）。
        *   **视角 B（语言模型嵌入）**：利用预训练的蛋白质语言模型（xTrimoPGLM 和 ESM），像处理文本语义一样理解氨基酸序列的上下文。
    *   **自适应交互机制**：通过一种特殊的编码器，让这两个视角的特征进行“对话”和互补，自动学习哪些特征对判断致病性更重要。
*   **关键设计取舍**：**放弃了 MSA（多序列比对）和显式结构描述符**。这样做的好处是模型推理极快，且不依赖于那些在无序区本就不可靠的进化信息或预测出来的假结构。

#### 4. 实验部分
*   **数据与任务**：在多个专门收集 IDR 变异的数据集上进行二分类任务（致病 vs. 中性）。
*   **Baseline（对比方法）**：对比了 AlphaMissense（DeepMind 出品）、ESM-1v、EVE 等顶级模型。
*   **评价指标**：AUC（曲线下面积）、ACC（准确率）、MCC（马修斯相关系数）。
*   **主要结果**：
    *   在 5 折交叉验证中，AUC 达到 0.840 - 0.899。
    *   **最强证据**：在一个极具挑战性的独立测试集（该集合中进化信号非常微弱，传统工具极易误判）中，DisoPatho 的 MCC 比 AlphaMissense 提升了 **50.2%**，且预测覆盖范围更广。

#### 5. 资源与算力
*   **文中未充分披露**具体的训练时长、GPU 型号或总算力消耗。但提到代码和模型已开源，且由于不依赖 MSA，其推理过程对算力的需求通常低于基于演化信息的模型。

#### 6. 真正可信的贡献
*   **填补了 IDR 预测的空白**：证明了在缺乏稳定结构的情况下，结合“物理化学能量”与“大规模语言模型”是处理高度灵活生物区域的有效路径。
*   **摆脱了对进化的依赖**：在进化约束较弱（即变异很快、参考序列少）的区域，该模型依然稳健，这对于研究新兴突变或罕见序列非常有价值。

#### 7. 局限与风险
*   **数据偏差风险**：IDR 的实验标注数据远少于折叠蛋白，模型可能在某些极端的无序类型上存在过拟合。
*   **黑盒解释性**：虽然引入了能量特征，但深度学习模型内部如何权衡“能量”与“语义”的逻辑仍不够直观，难以直接指导生物化学实验。
*   **真实应用障碍**：临床医生可能更倾向于使用有多年背书的保守性评分，DisoPatho 作为一个新工具，需要更多临床案例的验证。

#### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事蛋白质功能预测、变异效应分析、以及关注“非结构化”生物序列建模的研究者。
*   **后续可跟进的问题**：能否将这种“能量+语言模型”的思路推广到其他缺乏结构的生物大分子（如非编码 RNA 或蛋白质的柔性接头区）？

（完）
