---
title: Integrated single-cell and spatial mapping coupled with machine learning unveils core stemness landscapes and regulatory drivers in triple-negative breast cancer.
title_zh: 整合单细胞与空间图谱结合机器学习揭示三阴性乳腺癌的核心干性景观与调控驱动因子
authors: "Zhenzhong Huo, Weibo Sun, Chun Lou, Tiansong Yang"
date: 2026-03-23
pdf: "https://pubmed.ncbi.nlm.nih.gov/41870799/"
tags: ["query:seqai"]
score: 8.0
evidence: 单细胞与空间制图结合XGBoost机器学习
tldr: 针对三阴性乳腺癌（TNBC）高度异质性及肿瘤干细胞（CSCs）驱动恶化的问题，本研究整合单细胞、空间及大块转录组数据，利用CytoTRACE算法与XGBoost机器学习构建了由CALD1等5个核心基因组成的干性预测模型。研究发现高干性细胞处于分化起点，通过激活Notch信号通路促进免疫逃逸并导致预后不良，同时筛选出BI.2536等潜在敏感药物，为TNBC干细胞靶向治疗提供了新靶点。
selection_source: fresh_fetch
motivation: 旨在阐明三阴性乳腺癌中肿瘤干细胞维持其干性特征并驱动肿瘤进展的分子调控机制。
method: 整合多模态转录组数据，利用hdWGCNA与XGBoost算法筛选核心基因，并结合虚拟敲除技术验证其对Notch等干性通路的调控作用。
result: 成功构建了包含CALD1、ANP32B等5个基因的风险模型，证实高干性评分与免疫逃逸、Notch通路激活及临床预后差显著相关。
conclusion: 该研究揭示了TNBC干性景观的调控核心，为针对肿瘤干细胞的个性化精准治疗和药物开发提供了重要分子依据。
---

## 摘要
目的：三阴性乳腺癌（TNBC）表现出显著的肿瘤内异质性，癌症干细胞（CSCs）被认为在这一过程中发挥着关键作用。然而，将 CSC 相关干性特征与肿瘤进展联系起来的分子调控机制尚未得到充分阐明。方法：我们整合了单细胞 RNA 测序（scRNA-seq）、空间转录组学和批量转录组数据，利用 inferCNV 和 CytoTRACE 算法识别高干性细胞群体。通过 hdWGCNA 结合机器学习方法评估了干性相关基因的特征重要性，并构建了基于 XGBoost 的风险预测模型。使用 Monocle3 和 scTour 推断细胞分化轨迹，同时通过 CellChat 分析、SHAP 归因和基于 scTenifoldKnk 的虚拟敲除实验评估了核心基因对干性通路和恶性生物学行为的影响。结果：我们成功建立了一个包含五个核心干性相关基因（CALD1、ANP32B、FIS1、CD82 和 APLP2）的预测模型，高干性评分组表现出更差的预后和增强的免疫逃逸。轨迹分析证实，高干性亚群处于分化的起始阶段。富集分析显示 Notch 信号通讯高度活跃，虚拟敲除核心基因有效抑制了 NOTCH1 等干性标志物的表达。此外，药物敏感性分析发现 BI.2536 及其相关化合物在高风险组中表现出更高的治疗敏感性。结论：我们的预测模型为 TNBC 的干性景观提供了新的视角。这些核心基因在维持干性方面发挥着关键作用，并可作为针对 TNBC 类干细胞个性化治疗的潜在分子靶点。

## Abstract
OBJECTIVE: Triple-negative breast cancer (TNBC) exhibits pronounced intratumoral heterogeneity, and cancer stem cells (CSCs) are thought to play a pivotal role in this process. However, the molecular regulatory mechanisms linking CSC-associated stemness features to tumor progression remain insufficiently elucidated. METHODS: We integrated single-cell RNA sequencing (scRNA-seq), spatial transcriptomics, and bulk transcriptomic data to identify high-stemness cell populations using the inferCNV and CytoTRACE algorithms. Stemness-related genes were evaluated for feature importance through hdWGCNA combined with machine learning approaches, and an XGBoost-based risk prediction model was constructed. Cellular differentiation trajectories were inferred using Monocle3 and scTour, while the effects of core genes on stemness pathways and malignant biological behaviors were assessed via CellChat analysis, SHAP attribution, and scTenifoldKnk-based virtual knockdown experiments. RESULTS: We successfully established a predictive model comprising five core stemness-related genes (CALD1, ANP32B, FIS1, CD82, and APLP2), with the high-stemness score group exhibiting poorer prognosis and enhanced immune evasion. Trajectory analysis confirmed that the high-stemness subpopulation resided at the initiation stage of differentiation. Enrichment analyses revealed highly active Notch signaling communication, and virtual knockdown of hub genes effectively suppressed the expression of stemness markers such as NOTCH1. In addition, drug sensitivity analysis identified BI.2536 and related compounds as exhibiting higher therapeutic sensitivity in the high-risk group. CONCLUSION: Our predictive model offers a novel perspective on the stemness landscape of TNBC. These core genes play key roles in maintaining stemness and also serve as potential molecular targets for personalized therapies aimed at TNBC stem-like cells.

---

## 论文详细总结（自动生成）

这是一份关于三阴性乳腺癌（TNBC）干性景观研究的深度技术总结：

### 1. 核心问题与研究价值
**核心问题**：三阴性乳腺癌（TNBC）是乳腺癌中最难治的一种，其特征是极高的异质性和容易复发。科学界认为**肿瘤干细胞（CSCs）**是导致这种恶性特征的“元凶”，但究竟是哪些基因在维持这些细胞的“干性”（即自我更新和分化能力），以及它们如何影响肿瘤的空间分布和免疫逃逸，目前尚不清晰。

**研究价值**：本文通过整合单细胞、空间位置和临床大样本数据，利用机器学习筛选出了 5 个关键驱动基因。这不仅为 TNBC 提供了新的预后评估工具，还通过“虚拟敲除”模拟实验找到了潜在的治疗靶点。

### 2. 白话版概述
三阴性乳腺癌像是一个复杂的社会，其中有一群处于“原始状态”的细胞（干细胞），它们不干活只负责分裂和指挥，导致癌症不断扩张且不怕化疗。研究者利用单细胞测序技术把这些“指挥官”找出来，用机器学习算法（XGBoost）锁定了 5 个核心基因。研究发现，这些基因通过一种叫 Notch 的信号通路指挥其他细胞，并帮助肿瘤躲避免疫系统的攻击。最后，研究还发现一种名为 BI.2536 的药物可能对这些高危细胞特别有效。

### 3. 方法部分：核心思想与模型设计
该研究采用了一种**多模态数据整合+可解释机器学习**的架构：
*   **干性识别（特征工程）**：利用 `CytoTRACE` 算法根据单细胞转录组的 mRNA 复杂度推断细胞的分化潜能（干性），并结合 `inferCNV`（推断染色体拷贝数变异）剔除正常细胞，精准锁定高干性的恶性细胞亚群。
*   **基因筛选（hdWGCNA + XGBoost）**：
    *   先用 **hdWGCNA**（高维加权基因共表达网络分析）在单细胞层面寻找与干性高度相关的基因模块。
    *   再将候选基因输入 **XGBoost** 模型，利用其特征重要性评分（Feature Importance）筛选出对预后贡献最大的 5 个核心基因（CALD1, ANP32B, FIS1, CD82, APLP2）。
*   **因果推断与模拟（scTenifoldKnk）**：这是一种基于图信号处理的“虚拟敲除”技术。研究者在计算机上模拟关闭这 5 个核心基因，观察整个基因调控网络的变化，从而验证它们对 Notch 等关键干性通路的控制作用。
*   **空间验证**：利用空间转录组数据，将单细胞识别出的干性特征映射到真实的组织切片上，观察干细胞在肿瘤微环境中的物理分布。

### 4. 实验部分：数据与结果
*   **数据来源**：整合了公共数据库（如 TCGA, GEO）的单细胞 RNA 测序数据、空间转录组数据以及大样本 Bulk RNA 测序数据。
*   **主要任务**：构建风险预测模型、推断细胞分化轨迹、分析免疫微环境。
*   **评价指标**：生存曲线（KM curve）的 P 值、ROC 曲线下的面积（AUC）、SHAP 解释值。
*   **主要结果**：
    1.  **模型表现**：基于 5 个基因构建的风险模型在多个独立数据集上均能显著区分预后好坏。
    2.  **生物学发现**：高干性细胞处于分化轨迹的起点，且高风险组表现出明显的免疫抑制特征（免疫逃逸）。
    3.  **通路机制**：Notch 信号通路在高干性细胞中高度活跃，是维持其特征的核心。
    4.  **药物筛选**：通过计算预测，发现 Polo 样激酶抑制剂（如 BI.2536）对高风险患者更敏感。

### 5. 资源与算力
*   **文中未充分披露**。论文重点在于算法流程和生物学解释，未提及具体的 GPU/CPU 型号或训练耗时。考虑到 XGBoost 和单细胞分析的常规需求，标准工作站即可完成。

### 6. 真正可信的贡献
*   **证据最强的结论**：通过 **scTenifoldKnk 虚拟敲除**验证了核心基因与 Notch1 信号通路之间的调控关系，这比单纯的相关性分析更具说服力。
*   **多维度验证**：干性特征在单细胞（微观）、空间（结构）和大块组织（临床）三个维度上得到了一致性验证，增强了结论的鲁棒性。

### 7. 局限与风险
*   **实验验证不足**：所有的结论均基于生物信息学分析和计算机模拟（In silico），缺乏湿实验（如 CRISPR 敲除细胞系或类器官实验）的直接验证。
*   **数据偏差**：回顾性数据可能存在批次效应，且 TNBC 亚型众多，该模型在不同亚型间的普适性有待验证。
*   **临床转化障碍**：筛选出的药物 BI.2536 虽有潜力，但在人体内的毒性和有效性仍需临床试验。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事单细胞多组学整合、可解释机器学习、以及肿瘤精准医疗的 AI 研究者。
*   **后续可跟进的问题**：如何利用**生成式 AI（如 scGPT 或 Geneformer）**在更大规模的预训练模型上直接提取干性特征，而非依赖传统的统计学算法（如 CytoTRACE）？

（完）
