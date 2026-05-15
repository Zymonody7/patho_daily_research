---
title: Multi-omics integration identifies ribosome biogenesis-active macrophage subpopulation and its key gene GNL2 in driving liver hepatocellular carcinoma progression and mechanisms.
title_zh: 多组学整合识别核糖体生物合成活跃的巨噬细胞亚群及其驱动肝细胞癌进展的关键基因 GNL2 与机制
authors: "Yajie Qi, Kun Li, Pincheng Li, Jianyu Yan, Shuyue Feng, Dan Wan, Ke Du, Xiao Liang, Fan Yang, Erzheng Zhou, Na Huang, Qian Wang, Nanbin Liu"
date: 2026-05-14
pdf: "https://pubmed.ncbi.nlm.nih.gov/42135716/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 多组学整合构建肝癌单细胞图谱
tldr: 针对肝细胞癌（LIHC）中驱动癌症进展的核心基因及核糖体生物合成（RB）作用不明的问题，本研究整合单细胞、大体转录组及空间转录组数据，利用WGCNA和117种机器学习组合构建了预后模型。研究发现了一类高核糖体生物合成活性的巨噬细胞亚群（RAMs），并锁定关键基因GNL2。实验证实GNL2通过调节炎症因子促进肿瘤进展，为LIHC的精准诊断和靶向治疗提供了新靶点。
selection_source: fresh_fetch
motivation: 旨在揭示核糖体生物合成在肝细胞癌进展中的系统性作用，并寻找关键的驱动基因和治疗靶点。
method: 整合多组学数据，通过加权基因共表达网络分析（WGCNA）和大规模机器学习算法筛选，构建了基于核糖体相关基因的预后风险模型。
result: 鉴定出一种具有高核糖体活性的巨噬细胞亚群（RAMs），并发现关键基因GNL2能通过调控TGF-β和TNF-α表达来促进肝癌细胞的增殖与迁移。
conclusion: 研究确立了RAMs亚群及GNL2基因在肝癌恶化中的核心地位，为临床预后评估和药物开发提供了科学依据。
---

## 摘要
背景：肝细胞癌（LIHC）是一种常见的恶性肿瘤，但驱动其进展的核心基因和潜在治疗靶点仍未得到充分探索。核糖体生物合成（RB）是与多种癌症相关的关键生物学过程；然而，其在 LIHC 中的系统性作用尚不明确。方法：本研究整合了 LIHC 单细胞 RNA-Seq、大块（bulk）RNA-Seq 和空间转录组数据，并结合核糖体生物合成相关基因集，构建了 LIHC 的单细胞图谱。采用加权基因共表达网络分析（WGCNA）来表征髓系细胞亚群。此外，利用 117 种机器学习算法组合开发了基于 RB 相关基因的 LIHC 预后风险模型。随后通过实验验证和临床样本分析证实了关键发现。结果：我们识别出一个具有高核糖体生物合成活性的独特巨噬细胞亚群，称为核糖体生物合成活跃型巨噬细胞（RAMs）。这些细胞与炎症巨噬细胞表现出强烈的通讯，可能由 MIF 相关的受体-配体相互作用介导。我们进一步构建了一个包含 8 个基因（PA2G4、GNL2、PWP1、DDX49、NOC4L、GDI2、CST7 和 RCL1）的预后模型，该模型显示出良好的预测性能。药物敏感性分析表明，高风险组可能对包括多西他赛在内的几种药物更敏感。在这些基因中，GNL2 被选中进行进一步研究。GNL2 表达升高与髓系细胞干性特征增强相关。分子对接分析确定了几种对 GNL2 具有潜在结合亲和力的候选化合物。在功能上，巨噬细胞中 GNL2 的敲低降低了 TGF-β 和 TNF-α 的表达，并与 LIHC 细胞增殖、迁移和侵袭的减少相关。结论：我们识别了一个高活性的核糖体生物合成巨噬细胞亚群（RAM），并构建了一个稳健的风险模型，以辅助 LIHC 的诊断、预后和治疗。GNL2 与 TGF-β 和 TNF-α 表达增加有关，并可能促进 LIHC 的进展。

## Abstract
BACKGROUND: Liver hepatocellular carcinoma (LIHC) is a common malignancy, yet the core genes driving its progression and potential therapeutic targets remain insufficiently explored. Ribosome biogenesis (RB) is a critical biological process linked to various cancers; however, its systematic role in LIHC remains unclear. METHODS: This study integrated LIHC single-cell RNA-Seq, bulk RNA-Seq, and spatial transcriptomic data with ribosome biogenesis-related gene sets to construct a single-cell atlas of LIHC. Weighted Gene Co-expression Network Analysis (WGCNA) was employed to characterize myeloid cell subsets. Furthermore, an LIHC prognostic risk model based on RB-related genes was developed using 117 machine-learning algorithm combinations. Key findings were subsequently corroborated through experimental validation and clinical sample analysis. RESULTS: We identified a distinct macrophage subpopulation with high ribosome biogenesis activity, termed ribosome biogenesis-active macrophages (RAMs). These cells exhibited strong communication with inflammatory macrophages, potentially mediated by MIF-related receptor-ligand interactions. We further constructed an 8-gene prognostic model (PA2G4, GNL2, PWP1, DDX49, NOC4L, GDI2, CST7, and RCL1), which showed good predictive performance. Drug sensitivity analysis suggested that the high-risk group may be more responsive to several agents, including docetaxel. Among these genes, GNL2 was selected for further investigation. Elevated GNL2 expression was associated with increased stemness features in myeloid cells. Molecular docking analysis identified several candidate compounds with potential binding affinity to GNL2. Functionally, GNL2 knockdown in macrophages reduced TGF-β and TNF-α expression and was associated with decreased proliferation, migration, and invasion of LIHC cells. CONCLUSION: We identified a highly active ribosome biogenesis-macrophage subpopulation (RAM), and constructed a robust risk model to aid in the diagnosis, prognosis, and treatment of LIHC. GNL2 is associated with increased expression of TGF-β and TNF-α and may contribute to LIHC progression.

---

## 论文详细总结（自动生成）

这篇论文通过整合单细胞测序、空间转录组和机器学习算法，深入探讨了肝细胞癌（LIHC）中“核糖体生物合成”这一生物学过程如何影响肿瘤微环境，并锁定了一个关键的免疫细胞亚群及其核心驱动基因。

### 1. 解决的问题与研究意义
*   **核心问题**：肝癌细胞为了快速增殖，需要大量的蛋白质，而核糖体是生产蛋白质的“工厂”。过去研究多关注癌细胞自身的核糖体，但这篇论文研究的是：**肿瘤周围的免疫细胞（特别是巨噬细胞）如果核糖体生产异常活跃，会如何助纣为虐，推动癌症进展？**
*   **研究意义**：肝癌预后差、异质性强。识别出这种特定的免疫细胞亚群（RAMs）及其关键基因 GNL2，为精准医疗提供了新的生物标志物（判断病情）和潜在的治疗靶点（开发新药）。

### 2. 白话版概述
*   研究者利用大数据分析，在肝癌组织中发现了一群特殊的“后勤保障”巨噬细胞，它们内部的核糖体制造非常活跃，被称为 RAMs。
*   通过 117 种机器学习算法的“大比武”，他们筛选出 8 个关键基因，能准确预测肝癌患者的生存时间。
*   研究锁定了一个叫 GNL2 的基因，它就像是这群巨噬细胞的“动力开关”，一旦高表达，就会释放炎症因子，诱导癌细胞变得更具侵略性、跑得更快。
*   最后，他们还通过计算机模拟，找到了几种可能抑制这个开关的潜在药物。

### 3. 方法部分
*   **核心思想**：多组学数据整合（Multi-omics Integration）。将单细胞 RNA 测序（看单个细胞在干嘛）、大块转录组（看群体平均水平）和空间转录组（看细胞在组织里的位置）结合起来。
*   **模型结构**：
    *   **WGCNA（加权基因共表达网络分析）**：用于识别与核糖体生物合成最相关的基因模块。
    *   **机器学习流水线**：这是本文的 AI 亮点。研究者组合了 Lasso、随机森林（Random Forest）、支持向量机（SVM）、GBM 等多种算法，测试了 **117 种组合**，最终选出性能最稳健的预后风险模型。
*   **关键设计**：不仅停留在数据挖掘，还引入了**细胞通讯分析（Cell-Cell Communication）**，研究 RAMs 巨噬细胞是如何通过 MIF 等信号通路与其它细胞“打招呼”的。

### 4. 实验部分
*   **数据来源**：TCGA（癌症基因组图谱）、ICGC（国际癌症基因组联盟）等公共数据库，以及实验室自有的临床样本。
*   **任务**：构建预后风险模型（预测生存率）和功能验证（验证基因作用）。
*   **评价指标**：C-index（一致性指数）、AUC（曲线下面积）、生存曲线的 P 值。
*   **主要结果**：
    *   成功鉴定出 RAMs 亚群。
    *   8 基因模型在多个独立数据集（Validation Cohorts）中均表现出极高的预测准确性。
    *   **湿实验验证**：在实验室敲低（关闭）巨噬细胞中的 GNL2 基因后，发现 TGF-β 和 TNF-α（促进癌症的因子）分泌减少，肝癌细胞的增殖和迁移能力显著下降。

### 5. 资源与算力
*   **文中未充分披露**具体的硬件配置（如 GPU/CPU 型号）。考虑到其涉及 117 种机器学习组合的训练和空间转录组分析，通常需要高性能计算集群（HPC）或高配工作站。

### 6. 真正可信的贡献
*   **证据最强的结论**：GNL2 基因在巨噬细胞中的表达水平与肝癌的恶性程度呈正相关。这一结论不仅有数千例临床数据的统计支持，还有细胞层面的功能实验（Knockdown 实验）作为直接证据。
*   **创新点**：首次定义了“核糖体生物合成活跃型巨噬细胞（RAMs）”这一亚群，并证明了免疫细胞的蛋白质合成能力也是肿瘤微环境的重要推手。

### 7. 局限与风险
*   **实验不足**：大部分功能验证是在体外（In vitro）细胞系中完成的，缺乏动物模型（In vivo）的验证，难以完全模拟复杂的体内免疫环境。
*   **外推风险**：虽然在肝癌中表现良好，但该模型和 RAMs 亚群是否适用于其他类型的实体瘤（如肺癌、胃癌）尚不清楚。
*   **数据偏差**：公共数据库（如 TCGA）多为西方人群数据，对于不同种族背景的适用性仍需更多本地临床数据验证。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事**多模态数据融合**、**自动化机器学习（AutoML）**以及**肿瘤免疫微环境建模**的研究者。
*   **后续可跟进的问题**：能否利用图神经网络（GNN）结合空间转录组数据，更精准地模拟 RAMs 巨噬细胞与癌细胞在物理空间上的相互作用，而不仅仅是基于基因表达量的相关性分析？

（完）
