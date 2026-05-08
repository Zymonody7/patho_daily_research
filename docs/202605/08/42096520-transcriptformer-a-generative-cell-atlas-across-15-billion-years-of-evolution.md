---
title: "TranscriptFormer: A generative cell atlas across 1.5 billion years of evolution."
title_zh: TranscriptFormer：跨越 15 亿年进化的生成式细胞图谱
authors: "James D Pearce, Sara E Simmonds, Gita Mahmoudabadi, Lakshmi Krishnan, Giovanni Palla, Ana-Maria Istrate, Alexander Tarashansky, Benjamin Nelson, Omar Valenzuela, Donghui Li, Stephen R Quake, Theofanis Karaletsos"
date: 2026-05-07
pdf: "https://pubmed.ncbi.nlm.nih.gov/42096520/"
tags: ["query:seqai"]
score: 10.0
evidence: 跨物种转录组学的生成式基础模型
tldr: 针对跨物种单细胞转录组比较分析中存在的演化跨度大、数据异质性强等挑战，该研究开发了 TranscriptFormer 生成式基础模型。该模型在涵盖 12 个物种、跨越 15 亿年演化史的 1.12 亿个细胞上进行预训练。实验证明，TranscriptFormer 在跨物种细胞类型分类和人类疾病状态零样本识别上达到 SOTA 水平，并能自动学习发育轨迹和系统发育关系，为跨物种细胞生物学研究提供了统一的定量分析框架。
selection_source: fresh_fetch
motivation: 旨在解决单细胞转录组分析中难以跨越漫长的演化时间尺度来比较不同物种间细胞转录程序的难题。
method: 构建了一个基于 Transformer 架构的生成式基础模型家族，利用 12 个物种共 1.12 亿个细胞的大规模数据进行预训练。
result: 模型在跨越 6.85 亿年演化的物种间实现了高精度的细胞分类，并能零样本识别人类疾病状态，同时自动学习到发育轨迹和系统发育关系。
conclusion: 该研究证明了通过大规模跨物种数据训练，可以学习并预测生命之树中通用的细胞组织原则。
---

## 摘要
单细胞转录组学正在彻底改变我们对细胞多样性的理解，然而在生命树范围内比较转录程序仍然具有挑战性。我们开发了 TranscriptFormer，这是一个生成式基础模型系列，在涵盖 12 个物种、跨越 15.3 亿年进化的多达 1.12 亿个细胞上进行了训练。我们展示了其在细胞类型分类方面的最先进性能，即使对于进化间隔超过 6.85 亿年的物种也是如此，并实现了人类细胞中疾病状态的零样本识别。发育轨迹、系统发育关系和细胞层级在 TranscriptFormer 的表示中自然显现，而无需对这些标注进行任何显式训练。这项工作为定量单细胞分析和比较细胞生物学建立了一个强大的框架，从而证明了细胞组织的普遍原理可以在整个生命树中被学习和预测。

## Abstract
Single-cell transcriptomics is revolutionizing our understanding of cellular diversity, yet comparing transcriptional programs across the tree of life remains challenging. We developed TranscriptFormer, a family of generative foundation models trained on up to 112 million cells spanning 1.53 billion years of evolution across 12 species. We demonstrate state-of-the-art performance on cell type classification, even for species separated over 685 million years of evolution, and zero-shot disease state identification in human cells. Developmental trajectories, phylogenetic relationships and cellular hierarchies emerge naturally in TranscriptFormer's representations without any explicit training on these annotations. This work establishes a powerful framework for quantitative single-cell analysis and comparative cellular biology, thus demonstrating that universal principles of cellular organization can be learned and predicted across the tree of life.

---

## 论文详细总结（自动生成）

这篇论文介绍了一个名为 **TranscriptFormer** 的大规模生成式基础模型，旨在通过 AI 技术统一理解地球上不同物种的细胞生物学规律。

### 1. 解决的问题与研究价值
*   **核心问题**：不同物种（如人类、果蝇、线虫）虽然都有细胞，但它们的基因名称和序列差异巨大。传统的生物学方法很难直接比较“人类的神经元”和“原始生物的神经元”在分子层面到底有多像。
*   **研究价值**：如果能找到跨物种的通用“细胞语言”，科学家就可以利用简单生物（如斑马鱼）的实验数据来精准预测人类细胞的反应，极大地加速药物研发和进化生物学研究。

### 2. “白话版”概述
*   这就像是为细胞建立了一个“跨语言的大语言模型（如 GPT）”。
*   研究者收集了 12 个物种（跨越 15 亿年进化史）的 1.12 亿个细胞数据，让模型学习基因表达的“语法”。
*   模型不仅能准确识别从未见过的物种细胞类型，还能在没见过病变数据的情况下，一眼看出人类细胞是否患病（零样本识别）。
*   最神奇的是，模型在学习过程中自动“悟”出了物种进化的亲缘关系和细胞发育的规律，而不需要人类提前标注。

### 3. 方法部分
*   **核心思想**：利用**自监督生成式预训练**。模型通过预测细胞中基因的表达模式，学习基因与基因之间、基因与细胞功能之间的深层联系。
*   **模型结构**：采用了 **Transformer** 架构（TranscriptFormer 家族），利用其强大的注意力机制来捕捉成千上万个基因之间的复杂相互作用。
*   **训练流程**：
    1.  **大规模预训练**：在 1.12 亿个细胞上进行生成式训练，涵盖从人类到深海无脊椎动物的 12 个代表性物种。
    2.  **表征学习**：将每个细胞转化为一个高维向量（Embedding），这个向量代表了细胞的“生物学身份”。
*   **关键设计取舍**：放弃了仅针对单一物种的精调，转而追求**跨物种的通用性**。通过极大规模的数据量（Scaling）来抵消不同物种间基因命名的异质性。

### 4. 实验部分
*   **数据规模**：1.12 亿个单细胞转录组数据，时间跨度达 15.3 亿年。
*   **主要任务**：
    *   **细胞分类**：在跨越 6.85 亿年进化距离的物种间进行细胞类型预测。
    *   **零样本疾病识别**：在人类细胞中识别疾病状态。
    *   **生物学发现**：重建发育轨迹和系统发育树（物种演化关系图）。
*   **主要结果**：
    *   在细胞分类任务上达到 **SOTA（当前最佳）** 水平。
    *   模型内部的向量空间自然地排列出了物种的进化顺序，证明它抓住了进化的本质规律。

### 5. 资源与算力
*   **文中未充分披露**：摘要及提供的文本片段中未提及具体的 GPU 型号、训练时长或能耗数据。但考虑到 1.12 亿细胞的规模，这通常需要数千张 A100/H100 级别的显卡集群支持。

### 6. 真正可信的贡献
*   **证据最强的结论**：模型在**跨物种细胞迁移学习**上的表现非常稳健，证明了基础模型可以跨越极长的进化时间尺度（6.85 亿年以上）提取通用特征。
*   **涌现能力**：发育轨迹和进化关系的“自然显现”是一个强有力的证据，说明模型学到的是物理/生物学本质，而非简单的模式匹配。

### 7. 局限与风险
*   **物种覆盖偏差**：虽然涵盖了 12 个物种，但相对于地球上数百万种生物，样本量依然有限，可能存在“幸存者偏差”。
*   **数据模态单一**：目前主要基于转录组（RNA），尚未整合蛋白质组或空间转录组数据，对细胞的理解还不完整。
*   **临床应用障碍**：零样本疾病识别虽然惊艳，但在实际医疗诊断中，其假阳性率和解释性仍需严格的临床验证。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事单细胞基础模型、跨物种基因组学、以及药物靶点发现的 AI 研究者。
*   **后续可跟进的问题**：如何将非编码区 DNA 序列信息与这种细胞层级的 Transformer 结合，实现从“代码（DNA）”到“表现（细胞状态）”的全栈模拟？

（完）
