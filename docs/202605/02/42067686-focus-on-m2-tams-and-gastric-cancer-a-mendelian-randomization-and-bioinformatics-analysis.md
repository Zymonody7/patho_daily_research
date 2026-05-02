---
title: "Focus on M2-TAMs and gastric cancer: a Mendelian randomization and bioinformatics analysis."
title_zh: 聚焦 M2 型肿瘤相关巨噬细胞与胃癌：孟德尔随机化与生物信息学分析
authors: "GuangTao Min, Hao Tang, GuangNing Min, YuMin Li"
date: 2026-05-02
pdf: "https://pubmed.ncbi.nlm.nih.gov/42067686/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 用于多组学整合和生物标志物发现的生物信息学算法
tldr: 针对胃癌免疫治疗响应率低且预后评估难的问题，本研究结合孟德尔随机化（MR）与生物信息学方法，识别出与胃癌显著相关的M2型肿瘤相关巨噬细胞（TAM）特征。通过WGCNA和Lasso-Cox回归筛选出SEC61G、BGN和STC1三个核心预后基因并构建风险模型。结果显示，该模型能有效预测患者生存期及免疫治疗敏感性，为胃癌的精准医疗和个性化用药提供了新的生物标志物与治疗靶点。
selection_source: fresh_fetch
motivation: 旨在通过识别与M2型肿瘤相关巨噬细胞相关的关键基因，解决胃癌预后预测不准及免疫治疗效果有限的临床难题。
method: 整合孟德尔随机化分析、WGCNA基因共表达网络及Lasso-Cox回归算法，筛选并验证了与胃癌预后密切相关的免疫细胞亚型及基因模块。
result: 成功构建了由SEC61G、BGN和STC1组成的风险评分模型，发现高风险组患者对免疫治疗响应较差，但对维利帕尼等特定药物更敏感。
conclusion: 该研究建立的TAM驱动型预后模型为胃癌患者的生存预测、免疫疗效评估及个体化靶向治疗提供了科学依据。
---

## 摘要
胃癌（GC）是一种具有高度侵袭性和异质性的恶性肿瘤，尽管近期取得了进展，但在免疫治疗方面仍面临挑战。本研究旨在识别新型生物标志物并构建预后模型，以改善预后预测和治疗策略。孟德尔随机化（MR）分析利用 FinnGen 和 GWAS 队列识别了与胃癌相关的免疫细胞亚型。应用 CIBERSORT 和 WGCNA 算法定义了 M2 型肿瘤相关巨噬细胞（TAM）相关的基因模块。通过 Lasso-Cox 回归筛选关键预后基因以建立风险模型，并使用 GEO 数据集进行了验证。通过 GSEA 和免疫浸润分析评估了生物学功能差异、肿瘤微环境异质性和治疗敏感性。使用 TCGA、HPA 和蛋白质印迹法（Western blot）进行了蛋白质水平的验证。MR 分析揭示了 26 种与胃癌相关的免疫细胞亚型。WGCNA 识别了 20 个基因模块，并优先考虑了与 M2 型 TAM 相关性最强的模块。开发了包含 SEC61G、BGN 和 STC1 的预后特征，将患者分为具有不同生存结局的不同风险组（1/3/5 年生存率，均 P < 0.05）。高风险患者表现出钙信号通路的富集、免疫治疗反应性降低，以及对维利帕尼（veriparib）和帕博西尼（palbociclib）的敏感性增加。在胃癌组织中验证了关键基因的蛋白质过表达。这一整合的生物信息学-MR 框架建立了胃癌的 TAM 驱动预后模型，展示了其在生存预测、免疫治疗疗效评估和个性化治疗靶向方面的临床应用价值。研究结果为推进胃癌的精准免疫治疗提供了可操作的见解。

## Abstract
Gastric cancer (GC), a highly aggressive and heterogeneous malignancy, remains challenging in immunotherapy despite recent advancements. This study aims to identify novel biomarkers and construct a prognostic model to improve outcome prediction and therapeutic strategies. Mendelian randomization (MR) analysis identified immune cell subtypes linked to GC using FinnGen and GWAS cohorts. CIBERSORT and WGCNA algorithms were applied to define M2 tumor-associated macrophage (TAM)-related gene modules. Key prognostic genes were selected via Lasso-Cox regression to establish a risk model, validated using GEO datasets. Biological function disparities, tumor microenvironment heterogeneity, and therapeutic sensitivities were assessed via GSEA and immune infiltration analysis. Protein-level validation was performed using TCGA, HPA, and Western blot. MR analysis revealed 26 immune cell subtypes associated with GC. WGCNA identified 20 gene modules, with the most M2 TAM-correlated module prioritized. A prognostic signature incorporating SEC61G, BGN, and STC1 was developed, stratifying patients into distinct risk groups with divergent survival outcomes (1-/3-/5-year, all P < 0.05). High-risk patients exhibited enriched calcium signaling pathways, reduced immunotherapy responsiveness, and increased sensitivity to veriparib and palbociclib. Protein overexpression of key genes was validated in GC tissues. This integrated bioinformatics-MR framework establishes a TAM-driven prognostic model for GC, demonstrating clinical utility in survival prediction, immunotherapy efficacy evaluation, and personalized therapeutic targeting. The findings provide actionable insights for advancing precision immunotherapy in GC.

---

## 论文详细总结（自动生成）

这篇论文通过整合遗传学因果推断和多组学数据分析，深入探讨了**M2型肿瘤相关巨噬细胞（M2-TAMs）**在胃癌中的作用。以下是详细的结构化总结：

### 1. 解决的问题与研究价值
*   **核心问题**：胃癌（GC）极具侵袭性且个体差异大，现有的免疫治疗对很多患者无效。临床上迫切需要能准确预测患者生存期（预后）并指导用药的生物标志物。
*   **研究价值**：研究聚焦于**M2型巨噬细胞**（一种在肿瘤微环境中“助纣为虐”、抑制免疫反应并促进肿瘤生长的免疫细胞）。通过证明这种细胞与胃癌的因果关系并筛选核心基因，为精准医疗提供了科学依据。

### 2. 白话版概述
肿瘤不仅有癌细胞，周围还围着一群被“洗脑”的免疫细胞（如M2型巨噬细胞），它们保护肿瘤不被免疫系统攻击。这篇论文先用遗传学方法证明了这些“叛变”的免疫细胞确实会导致胃癌恶化，然后利用算法从成千上万个基因中揪出了3个最关键的“帮凶”基因（SEC61G, BGN, STC1）。基于这三个基因，研究者做了一个评分系统：分数越高，患者预后越差，且对常规免疫治疗不敏感，但可能对某些特定化疗药更有效。

### 3. 方法部分
*   **核心思想**：**因果推断 + 基因共表达网络分析**。
*   **推理流程**：
    1.  **孟德尔随机化 (MR)**：利用人类基因组中的随机变异（SNP）作为“天然实验”，排除环境干扰，确认哪些免疫细胞亚型与胃癌有真正的因果联系。
    2.  **CIBERSORT 算法**：通过分析肿瘤组织的转录组数据，反推其中各种免疫细胞（如M2型巨噬细胞）的占比。
    3.  **WGCNA (加权基因共表达网络分析)**：将成千上万个基因按表达模式聚类成不同的“模块”，找出与M2型巨噬细胞数量最相关的基因模块。
    4.  **Lasso-Cox 回归**：一种机器学习筛选算法，从相关模块中剔除冗余信息，最终选定3个对生存预测贡献最大的核心基因。
*   **关键设计取舍**：研究没有只停留在相关性分析上，而是先用 MR 确定了因果性，这大大增强了结论的生物学可信度。

### 4. 实验部分
*   **数据来源**：FinnGen 数据库、GWAS 汇总数据、TCGA（癌症基因组图谱）以及 GEO 验证数据集。
*   **评价指标**：生存曲线（Kaplan-Meier）、受试者工作特征曲线（ROC）下的面积（AUC，用于评估预测准确性）、P值。
*   **主要结果**：
    *   识别出 26 种与胃癌相关的免疫亚型。
    *   构建了基于 **SEC61G、BGN 和 STC1** 的 3 基因风险模型。
    *   该模型在预测 1 年、3 年、5 年生存率方面表现优异（P < 0.05）。
    *   **药物发现**：高风险组患者对维利帕尼（Veriparib）和帕博西尼（Palbociclib）表现出更高的敏感性。

### 5. 资源与算力
*   **文中未充分披露**。论文主要基于公开数据库进行生物信息学分析，通常涉及 R 语言环境及相关统计学包，未提及高性能计算集群或大规模 GPU 训练需求。

### 6. 真正可信的贡献
*   **因果证据最强**：通过孟德尔随机化明确了免疫细胞与胃癌的因果链条，而非简单的“伴随现象”。
*   **模型简洁实用**：仅用 3 个基因就构建了具有显著预测能力的模型，相比动辄几十个基因的模型，更具临床转化潜力。
*   **多维度验证**：结论不仅在多个公开数据集（TCGA, GEO）中成立，还通过了 HPA 数据库的蛋白水平验证和实验室 Western Blot 实验验证。

### 7. 局限与风险
*   **数据偏差**：MR 分析主要基于欧洲人群（FinnGen），结论在东亚等胃癌高发地区的适用性需进一步验证。
*   **实验深度不足**：虽然做了 Western Blot 验证蛋白表达，但缺乏功能性实验（如敲除这三个基因看肿瘤是否停止生长）来证明其分子机制。
*   **真实应用障碍**：从生物信息学模型到临床常规检测（如 PCR 试剂盒）仍有很长的标准化和审批流程。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事多组学整合、因果推理、以及肿瘤免疫微环境建模的 AI 研究者。
*   **后续可跟进的问题**：能否利用深度学习（如 Graph Neural Networks）更好地模拟 WGCNA 发现的基因共表达网络，从而识别出更隐蔽的非线性调控靶点？

（完）
