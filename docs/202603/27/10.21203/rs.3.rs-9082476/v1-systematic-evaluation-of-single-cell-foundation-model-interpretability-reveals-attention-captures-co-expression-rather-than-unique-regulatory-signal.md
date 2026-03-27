---
title: Systematic evaluation of single-cell foundation model interpretability reveals attention captures co-expression rather than unique regulatory signal
title_zh: 对单细胞基础模型可解释性的系统评估揭示了注意力机制捕捉的是共表达而非独特的调控信号
authors: Kendiukhov I.
date: 2026-03-26
pdf: "https://doi.org/10.21203/rs.3.rs-9082476/v1"
tags: ["query:bioinfo"]
score: 9.0
evidence: 单细胞基础模型在基因调控网络推理中的评估
tldr: 单细胞大模型常被认为其注意力机制能揭示基因调控关系，但这一假设缺乏严谨验证。本研究通过对4种细胞系和2种扰动方式进行系统性评估，发现注意力权重主要捕捉的是基因共表达等统计关联，而非因果调控信号。实验表明，简单的基因级基准模型在预测扰动效果上优于复杂的注意力边得分，且消融实验证实注意力头对预测并无实质贡献。研究提出了CSSI工具以优化异质群体中的边提取，为单细胞大模型的可解释性建立了质量控制标准。
selection_source: fresh_fetch
motivation: 探究单细胞大模型中的注意力权重是否真正捕捉到了因果基因调控信号，而非仅仅反映数据中的统计相关性。
method: 构建了包含37项分析的系统性评估框架，在多种细胞类型和CRISPR扰动数据下，对比了注意力得分与简单基因级基准模型的预测效能。
result: 实验证明注意力机制在预测基因扰动效果时表现逊于简单的基准模型，且消融注意力头并不会导致模型性能下降，说明其并未捕捉到独特的因果信号。
conclusion: 注意力权重不应被直接解释为因果调控证据，研究提出的CSSI工具为从异质细胞群体中更准确地恢复基因关联提供了新方案。
---

## 摘要
背景：scGPT 和 Geneformer 等单细胞基础模型正日益广泛地应用于基因调控网络（GRN）推断，其中源自注意力的边得分（edge scores）通常被解释为调控关系的代理指标。然而，注意力模式是否捕捉到了因果调控关系，而非仅仅是表达数据中已存在的统计关联，尚未经过系统性验证。这一研究空白至关重要，因为 NLP 可解释性文献已证实注意力权重并不能可靠地指示特征重要性，但这一结论在生物学基础模型中尚未得到严格评估。结果：我们提出了一个系统性评估框架，包含 37 项分析、153 项统计检验、4 种细胞类型（K562、RPE1、T 细胞、iPSC 神经元）和 2 种扰动模态（CRISPRi、CRISPRa）。注意力模式编码了特定层的生物学结构——早期层为蛋白质-蛋白质相互作用，后期层为转录调控——但这种结构对于扰动预测并无增量价值：平凡的基因级基准模型表现优于注意力边和相关性边（AUROC 0.81–0.88 对比 0.70），成对边得分在基因级特征之外没有提供任何预测贡献（ΔAUROC = -0.0004 至 -0.002；559,720 次观察），且对调控头的因果消融在三个独立的干预通道中均未导致性能下降。注意力与相关性之间的关系具有上下文依赖性（在 K562 中相当，在 CRISPRa 中较差，在 RPE1 中较好），但基因级特征的主导地位是普遍存在的。细胞状态分层可解释性（CSSI）解决了注意力机制特有的缩放失效问题，使 GRN 恢复效果提升了高达 1.85 倍。结论：单细胞基础模型中的注意力模式编码了结构化的生物信息，但并非通常认为的因果调控信号。该评估框架为该领域建立了可复用的质量控制标准，而 CSSI 为从异质群体中改进边恢复提供了一个可立即部署的工具。

## Abstract
<title>Abstract</title>  <p>  <bold>Background</bold>  : Single-cell foundation models such as scGPT and Geneformer are increasingly used for gene regulatory network (GRN) inference, with attention-derived edge scores routinely interpreted as regulatory proxies. However, whether attention patterns capture causal regulatory relationships—rather than statistical associations already present in expression data—has not been systematically tested. This gap is critical because the NLP interpretability literature has established that attention weights do not reliably indicate feature importance, yet this finding has not been rigorously evaluated in biological foundation models.  <bold>Results</bold>  : We present a systematic evaluation framework comprising thirty-seven analyses, 153 statistical tests, four cell types (K562, RPE1, T cells, iPSC neurons), and two perturbation modalities (CRISPRi, CRISPRa). Attention patterns encode layer-specific biological structure—protein–protein interactions in early layers, transcriptional regulation in late layers—but this structure provides no incremental value for perturbation prediction: trivial gene-level baselines outperform both attention and correlation edges (AUROC 0.81–0.88 versus 0.70), pairwise edge scores add zero predictive contribution beyond gene-level features (∆AUROC = −0.0004 to −0.002; 559,720 observations), and causal ablation of regulatory heads produces no degradation across three independent intervention channels. The attention–correlation relationship is context-dependent (equal in K562, worse in CRISPRa, better in RPE1), but gene-level dominance is universal. Cell-State Stratified Interpretability (CSSI) addresses an attention-specific scaling failure, improving GRN recovery up to 1.85×.  <bold>Conclusions</bold>  : Attention patterns in single-cell foundation models encode structured biological information but not the causal regulatory signal they are commonly interpreted as capturing. The evaluation framework establishes reusable quality-control standards for the field, and CSSI provides an immediately deployable tool for improved edge recovery from heterogeneous populations.  </p>

---

## 论文详细总结（自动生成）

这篇论文对当前单细胞基础模型（scFMs）的一个核心假设提出了有力质疑。以下是该研究的结构化总结：

### 1. 核心问题：注意力机制真的懂“基因调控”吗？
在单细胞 AI 领域，scGPT 和 Geneformer 等大模型被广泛用于推断**基因调控网络（GRN）**（即基因 A 如何控制基因 B）。研究者通常认为，模型内部的**注意力权重（Attention Weights）**代表了基因间的调控强度。
**这篇论文的价值在于：** 它首次系统性地验证了这一假设。如果注意力权重只是捕捉了简单的统计相关性（共表达），而非因果调控关系，那么目前许多基于 AI 发现的“新调控机制”可能只是空中楼阁。

### 2. 白话版概述
*   **现状：** 很多人觉得单细胞大模型像 LLM 一样神奇，它“关注”某个基因，就代表这个基因很重要。
*   **发现：** 作者通过大量实验证明，这些模型的注意力机制其实只是在看哪些基因经常“成对出现”（相关性），并没有真正理解谁控制谁（因果性）。
*   **结论：** 在预测基因被破坏（扰动）后的变化时，用最简单的统计学方法甚至比用复杂的 AI 注意力得分更准。
*   **工具：** 作者提供了一个叫 CSSI 的新方法，能稍微修正注意力机制在不同细胞状态下的偏差。

### 3. 方法部分
*   **核心思想：** 采用“因果干预”的思路。如果注意力权重真的代表调控，那么：
    1. 它应该能预测 CRISPR 实验（一种基因剪刀技术，用于关闭或激活特定基因）的结果。
    2. 删掉那些所谓的“调控注意力头”，模型的预测能力应该会崩塌。
*   **评估框架：** 构建了包含 37 项分析和 153 项统计检验的基准测试。
*   **关键对比：** 将注意力得分与“基因级基准”（只看基因本身的特征，不看成对关系）以及“相关性基准”（简单的皮尔逊相关系数）进行 PK。
*   **设计取舍：** 作者没有重新训练模型，而是直接对已发布的顶级模型（scGPT, Geneformer）进行“解剖”（Mechanistic Interpretability）。

### 4. 实验部分
*   **数据与任务：** 使用了 4 种细胞系（如 T 细胞、神经元）和两种 CRISPR 扰动数据（CRISPRi 抑制，CRISPRa 激活）。任务是预测：当基因 A 被扰动时，基因 B 是否会改变。
*   **评价指标：** AUROC（曲线下面积，越接近 1 越准）。
*   **主要结果：**
    *   **注意力表现平平：** 注意力得分的 AUROC 仅为 0.70 左右。
    *   **简单方法完胜：** 仅基于基因自身属性的简单基准模型，AUROC 达到了 0.81–0.88。
    *   **消融实验：** 强行关闭模型中被认为负责调控的注意力头，模型的预测性能**完全没有下降**。这证明模型在做预测时，根本没用到这些所谓的“调控信号”。

### 5. 资源与算力
*   **文中未充分披露：** 论文主要侧重于对预训练模型的推理和评估，未详细列出执行这 153 项统计检验的具体 GPU 小时数，但提到使用了标准的生物信息学计算环境。

### 6. 真正可信的贡献
*   **破除迷信：** 证据最强的一点是证明了**注意力权重 $\neq$ 调控强度**。通过大规模消融实验，有力地反驳了“注意力机制能自动涌现因果发现能力”的观点。
*   **CSSI 工具：** 提出了“细胞状态分层可解释性”（CSSI），解决了注意力权重在不同细胞群体间无法直接比较的缩放问题，将调控网络的恢复准确度提升了 1.85 倍。

### 7. 局限与风险
*   **模型局限：** 实验主要针对 scGPT 和 Geneformer，虽然它们是主流，但未来更先进的架构（如基于状态空间模型的 Mamba）是否也存在此问题尚待验证。
*   **零样本 vs 微调：** 研究主要评估了预训练模型的零样本（Zero-shot）能力。如果针对特定任务进行深度微调，注意力机制是否能产生真正的调控信号仍有讨论空间。
*   **数据偏差：** CRISPR 实验本身存在噪声，可能影响了对“真理”的判定。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 正在开发单细胞大模型、或试图利用 AI 寻找药物靶点的研究者。
*   **后续可跟进的问题：** 既然现有的注意力机制无法捕捉因果，我们是否应该在模型架构中显式引入“因果图约束”，而不是指望它从海量共表达数据中自动“悟”出因果？

（完）
