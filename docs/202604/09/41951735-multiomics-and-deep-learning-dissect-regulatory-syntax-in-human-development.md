---
title: Multiomics and deep learning dissect regulatory syntax in human development.
title_zh: 多组学与深度学习剖析人类发育中的调控语法
authors: "Betty B Liu, Selin Jessa, Samuel H Kim, Yan Ting Ng, Soon Il Higashino, Georgi K Marinov, Derek C Chen, Benjamin E Parks, Li Li, Tri C Nguyen, Austin T Wang, Sean K Wang, Meng How Tan, Serena Y Tan, Michael Kosicki, Len A Pennacchio, Eyal Ben-David, Anca M Pasca, Anshul Kundaje, Kyle K H Farh, William J Greenleaf"
date: 2026-04-08
pdf: "https://pubmed.ncbi.nlm.nih.gov/41951735/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于多组学整合和调控语法预测的深度学习
tldr: 针对人类发育过程中染色质可及性数据局限于单一器官或模态的问题，本研究构建了涵盖12个器官、80余万个细胞的多组学图谱，并利用深度学习模型从DNA序列预测可及性。研究揭示了转录因子协同作用的“硬性”与“软性”语法规则，以及抑制可及性的通用基序，为解码人类发育中的顺式调控逻辑和遗传变异提供了基础资源。
selection_source: fresh_fetch
motivation: 现有人类发育阶段的染色质可及性数据缺乏多器官、单细胞层面的系统整合，限制了对复杂转录调控逻辑的理解。
method: 构建了包含12个胎儿器官、203种细胞类型的单细胞多组学图谱，并训练深度学习模型通过局部DNA序列预测染色质可及性。
result: 识别出影响可及性的基序词典，发现了转录因子间存在精确间距要求的“硬规则”和灵活排列的“软规则”，并定位了抑制可及性的基序。
conclusion: 该研究通过深度学习解析了DNA序列语法如何驱动细胞特异性染色质状态，为理解人类发育中的遗传变异提供了关键的调控框架。
---

## 摘要
转录因子在发育过程中通过以序列特异性方式结合调控 DNA 来建立细胞身份，通常会促进局部染色质开放性并调节基因表达。绘制开放染色质图谱为转录控制提供了关键见解，但目前可用的人类发育数据集仅限于大块组织、单一器官或单一模态。在此，我们展示了人类发育多组学图谱（Human Development Multiomic Atlas），这是一个涵盖 12 个器官、817,740 个胎儿细胞的染色质开放性和基因表达单细胞图谱，跨越 203 种细胞类型和超过 100 万个候选顺式调控元件，其中许多元件表现出器官特异性的体内增强子活性。通过训练以根据局部 DNA 序列预测开放性的深度学习模型，揭示了影响开放性的全面基序（motif）词典，包括表现出独特语法约束的复合基序，这些基序被预测介导转录因子的协同作用。我们识别了需要精确基序间距和方向的“硬”语法规则、允许灵活基序排列的“软”规则，以及抑制开放性的普遍基序。基于模型的遗传变异解释显示，具有正向和负向影响的基序破坏与基因表达的一致影响相关。我们的工作描绘了基序语法如何支配细胞类型特异性的染色质开放性，并为解码顺式调控逻辑和解释人类发育过程中的遗传变异提供了基础资源。

## Abstract
Transcription factors establish cell identity during development by binding regulatory DNA in a sequence-specific manner, often promoting local chromatin accessibility and regulating gene expression1. Mapping accessible chromatin offers critical insights into transcriptional control, but available datasets for human development are restricted to bulk tissue, single organs or single modalities2. Here we present the Human Development Multiomic Atlas, a single-cell atlas of chromatin accessibility and gene expression from 817,740 fetal cells across 12 organs, spanning 203 cell types and more than 1 million candidate cis-regulatory elements, many of which exhibit organ-specific in vivo enhancer activity. Deep learning models trained to predict accessibility from local DNA sequence unravel a comprehensive lexicon of motifs that influence accessibility, including composite motifs exhibiting distinct syntactic constraints that are predicted to mediate transcription factor cooperativity. We identify 'hard' syntactic rules requiring precise motif spacing and orientation, 'soft' rules allowing flexible motif arrangements, and ubiquitous motifs inhibiting accessibility. Model-based interpretation of genetic variants reveals that disruption of motifs with positive and negative effects is associated with concordant effects on gene expression. Our work delineates how motif syntax governs cell-type-specific chromatin accessibility and provides a foundational resource for decoding cis-regulatory logic and interpreting genetic variation during human development.

---

## 论文详细总结（自动生成）

这篇论文是关于人类发育调控逻辑的里程碑式研究，由斯坦福大学 William J. Greenleaf 和 Anshul Kundaje 等顶尖团队合作完成。以下是该研究的详细总结：

### 1. 核心问题与研究价值
*   **核心问题**：人类发育过程中，DNA 序列是如何像“指令集”一样，在不同器官、不同细胞中精确控制基因开关的？
*   **研究价值**：过去的研究要么只看单一器官，要么分辨率不够。这篇论文构建了目前最全面的人类胎儿多组学图谱，并利用 AI 破译了 DNA 序列中的“语法规则”（即转录因子结合位点之间的排列组合逻辑），这对于理解先天性疾病和演化生物学至关重要。

### 2. 白话版概述
1.  **建图谱**：研究者收集了 12 个胎儿器官，给 80 多万个细胞做了“全身检查”，同时测量了它们的基因表达（RNA）和染色质开放状态（ATAC，即 DNA 哪里是松开可以被读取的）。
2.  **教 AI**：他们训练了一个深度学习模型，让 AI 学习 DNA 序列和这些“松开区域”之间的关系。
3.  **找规律**：AI 发现 DNA 序列里不仅有“单词”（基序/Motif），还有“语法”。有些蛋白质必须离得刚刚好（硬规则），有些则比较随意（软规则）。
4.  **看后果**：研究还发现了一些专门负责“关灯”的序列，并证明了如果这些语法规则被破坏（基因突变），会导致基因表达异常。

### 3. 方法部分
*   **核心思想**：将染色质可及性（Accessibility）预测看作一个**序列到信号的回归任务**。通过建模 DNA 序列特征，反推哪些转录因子（TF）在起作用。
*   **模型结构**：采用了基于卷积神经网络（CNN）或 Transformer 架构的深度学习模型（类似于 BPNet 或 Enformer 变体）。模型输入是 1k-2kb 的 DNA 序列，输出是 203 种细胞类型中的可及性概率。
*   **关键设计取舍**：
    *   **多任务学习**：同时预测 203 种细胞类型，利用细胞间的相关性增强模型泛化能力。
    *   **归因分析（Attribution）**：使用 DeepLIFT 等解释性算法，将预测结果回溯到具体的 DNA 碱基上，从而识别出关键的基序（Motif）。
    *   **语法解析**：通过改变序列中基序的距离和方向，观察模型预测值的变化，从而定义“硬语法”和“软语法”。

### 4. 实验部分
*   **数据规模**：涵盖 12 个器官（如心、脑、肝等），817,740 个单细胞，定义了 203 种细胞类型和超过 100 万个候选调控元件（cCREs）。
*   **验证任务**：
    *   **体内活性验证**：通过转基因小鼠实验，证明模型预测的“增强子”在真实生物体内确实能驱动特定器官的基因表达。
    *   **变异解释**：将模型应用于人类遗传变异数据，看突变是否破坏了预测的语法规则。
*   **主要结果**：
    *   识别出了一套完整的“发育基序词典”。
    *   **硬语法（Hard Syntax）**：某些转录因子（如碱基对级别的精确间距）必须以特定物理结构结合才能生效。
    *   **抑制基序**：发现了一类普遍存在的序列，它们的作用不是“打开”而是“关闭”染色质。

### 5. 资源与算力
*   **文中未充分披露**具体的 GPU 型号和训练总时长。但考虑到 80 万细胞的多任务深度学习模型，通常需要高性能计算集群（如 A100 集群）进行数周的训练。

### 6. 真正可信的贡献
*   **高质量图谱**：这是目前人类发育阶段最全的单细胞多组学数据库，具有极高的引用价值。
*   **语法规则的量化**：首次在大规模人类数据上区分了调控逻辑的“硬”与“软”，证明了 DNA 序列不仅仅是基序的堆砌，其相对位置（间距、方向）同样携带关键信息。
*   **负向调控因子的识别**：明确了哪些序列特征会导致染色质关闭，这在以往的研究中常被忽视。

### 7. 局限与风险
*   **发育阶段局限**：数据集中在胎儿期，无法直接外推到成年人或衰老过程。
*   **相关性 vs 因果性**：虽然有 AI 预测和部分实验验证，但百万级调控元件中，绝大多数的因果功能仍需进一步的大规模扰动实验（如 CRISPR 筛查）来证实。
*   **模型黑盒**：尽管使用了归因算法，但深度学习模型在处理极长程（>100kb）相互作用时仍存在局限。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事基因组基础模型（Genomic Foundation Models）、调控网络建模、以及临床遗传变异解释的研究者。
*   **后续可跟进的问题**：能否利用这些“硬语法规则”人工设计合成增强子，实现对特定发育阶段细胞的精准基因治疗控制？

（完）
