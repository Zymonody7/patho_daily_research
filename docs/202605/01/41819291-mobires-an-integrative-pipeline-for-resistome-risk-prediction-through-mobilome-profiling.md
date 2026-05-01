---
title: "MobiRes: An integrative pipeline for resistome risk prediction through mobilome profiling."
title_zh: MobiRes：一种通过移动组分析进行耐药组风险预测的综合流程
authors: "Santhiya Kalimuthu, Ananthasubramanian Muthusamy"
date: 2026-05-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/41819291/"
tags: ["query:pathoai"]
score: 10.0
evidence: 用于从宏基因组数据集中预测耐药组风险的计算框架
tldr: 抗生素耐药性（AMR）通过环境传播构成全球威胁，但目前缺乏系统评估移动遗传元件（MGEs）风险的方法。MobiRes 框架通过整合宏基因组中的移动组和微生物组信息，利用随机森林模型预测耐药基因组风险。研究发现转座子是驱动耐药基因跨环境传播的核心因素，模型 AUC 达 0.82，为“全健康”视角的耐药性风险评估提供了可扩展的计算工具。
selection_source: fresh_fetch
motivation: 现有的抗生素耐药性研究多关注基因本身，缺乏对质粒、噬菌体和转座子等移动遗传元件在耐药基因传播中风险的系统性量化评估。
method: 开发了开源框架 MobiRes，通过整合宿主、移动性和生态因子，并结合随机森林模型与 SHAP 解释性分析，对多种环境宏基因组数据进行耐药风险预测。
result: 实验表明转座子是耐药基因传播的主要驱动力，且模型在区分不同环境的耐药风险上达到了 0.82 的 AUC 表现。
conclusion: 该研究证明了通过移动组画像预测耐药风险的可行性，强调了转座子在环境监测中的关键地位，为公共卫生安全提供了决策支持。
---

## 摘要
抗生素耐药性 (AMR) 构成了重大的全球健康挑战，环境是耐药决定因素的重要储存库和传播渠道。尽管抗生素耐药基因 (ARGs) 在环境背景下已得到广泛研究，但评估和优先排序与移动遗传元件 (MGEs)（如质粒、噬菌体、转座子和整合元件 (IEs)）相关风险的系统方法仍不明确。为了填补这一空白，我们提出了 MobiRes，这是一个开源计算框架，旨在通过整合移动组和微生物组的信息来预测耐药组风险。该流程使用广泛的公开宏基因组数据集进行了评估，涵盖了废水、家禽、土壤、沉积物和人类粪便样本等多种环境。为了验证该框架，应用了统计分析和机器学习模型来评估 MGEs 在驱动 ARG 传播中的作用。该流程识别出转座子是主要的 MGE 类别，同时捕获了质粒、噬菌体和 IE 相关 ARGs 的环境特异性变异。转座子相关 ARGs 表现出最一致的环境差异（ANOVA p = 0.0017；Kruskal-Wallis p = 0.018），而质粒和噬菌体相关 ARGs 表现出中度变化（p = 0.015-0.040），IE 相关 ARGs 在不同环境中保持相对稳定（p > 0.05）。随机森林 (RF) 模型的 AUC 达到 0.82，随后的特征重要性和 SHapley Additive exPlanations (SHAP) 分析表明，转座子丰度是驱动不同环境中 ARG 传播的主要因素。通过整合宿主、移动性和生态因素，MobiRes 为全面的 AMR 风险评估提供了一个可扩展且面向“全健康” (One Health) 的框架。该流程可在 https://github.com/santhiyakc17/MobiRes_Pipeline 公开获取。

## Abstract
Antimicrobial resistance (AMR) poses a significant global health challenge, with the environment serving as a crucial reservoir and conduit for resistance determinants. Although antibiotic resistance genes (ARGs) have been extensively studied in environmental contexts, systematic approaches for assessing and prioritizing the risks associated with mobile genetic elements (MGEs), such as plasmids, phages, transposons, and integrative elements (IEs), remain unclear. To address this gap, we present MobiRes, an open-source computational framework designed to predict resistome risk by integrating information from the mobilome and microbiome. The pipeline was evaluated using a wide range of publicly available metagenomic datasets spanning diverse environments, including wastewater, poultry, soil, sediments, and human fecal samples. To validate the framework, statistical analyses and machine learning models were applied to evaluate the role of MGEs in driving ARG dissemination. The pipeline identified transposons as the dominant MGE class while capturing environment-specific variation in plasmid, phage, and IE -associated ARGs. Transposon-associated ARGs showed the most consistent environmental differentiation (ANOVA p = 0.0017; Kruskal-Wallis p = 0.018), whereas plasmid and phage-associated ARGs varied moderately (p = 0.015-0.040) and IE-associated ARGs remained comparatively stable across environments (p > 0.05). The Random Forest (RF) model achieved an AUC of 0.82, and subsequent feature importance and SHapley Additive exPlanations (SHAP) analyses revealed that transposon abundance is the primary factor driving ARG dissemination across diverse environments. By integrating host, mobility, and ecological factors, MobiRes provides a scalable and One Health-oriented framework for comprehensive AMR risk assessment. This pipeline is publicly available at https://github.com/santhiyakc17/MobiRes_Pipeline.

---

## 论文详细总结（自动生成）

### MobiRes：通过移动组分析预测耐药组风险的综合流程

#### 1. 解决的问题与研究价值
抗生素耐药性（AMR）的威胁不仅在于耐药基因（ARGs）的存在，更在于这些基因的**流动性**。如果一个耐药基因被锁定在某种不致病的土壤细菌中，风险较低；但如果它位于**移动遗传元件（MGEs）**（如质粒、转座子）上，就极易跨物种传播给人类病原菌。

**研究价值：** 现有的研究大多只关注“有哪些耐药基因”，而缺乏系统评估“这些基因有多容易扩散”的工具。这篇论文开发了 **MobiRes** 框架，填补了从宏基因组数据中量化评估耐药传播风险的空白，为公共卫生预警提供了“全健康”（One Health）视角的计算工具。

---

#### 2. 白话版概述
*   耐药基因就像是细菌手中的“武器”，而移动遗传元件（MGEs）则是运送这些武器的“物流车”。
*   这项研究建立了一个名为 MobiRes 的“风险评估雷达”，专门扫描环境（如废水、农场、土壤）中的 DNA 数据。
*   它不仅看有多少“武器”，更看有多少“物流车”以及它们是什么型号（质粒、噬菌体、转座子等）。
*   通过 AI 模型，研究发现**转座子**（一种能在基因组内“跳跃”的 DNA 片段）是预测耐药性扩散风险最关键的指标。

---

#### 3. 方法部分
*   **核心思想：** 整合“宿主信息+移动性特征+生态环境因素”进行多维度风险建模。
*   **流程设计：**
    1.  **数据输入：** 宏基因组原始测序数据。
    2.  **特征提取：** 使用工具识别 ARGs（耐药基因）和四类主要的 MGEs：质粒（Plasmids）、噬菌体（Phages）、转座子（Transposons）和整合元件（IEs）。
    3.  **风险建模：** 采用**随机森林（Random Forest）**分类器。将不同环境的移动组特征作为输入，预测该环境的耐药风险等级。
    4.  **可解释性分析：** 引入 **SHAP（SHapley Additive exPlanations）** 算法，拆解模型决策过程，找出哪些 MGEs 对风险贡献最大。
*   **关键取舍：** 研究者没有追踪每一个具体的基因序列，而是将 MGEs 分类汇总，以提高模型在不同环境（如从废水到人类粪便）之间的泛化能力。

---

#### 4. 实验部分
*   **数据来源：** 涵盖废水、家禽养殖场、土壤、沉积物和人类粪便的公开宏基因组数据集。
*   **任务目标：** 区分不同环境下的耐药风险水平，并识别驱动传播的核心因子。
*   **评价指标：** 使用 AUC（曲线下面积）评估分类准确度，使用 ANOVA 和 Kruskal-Wallis 检验评估统计显著性。
*   **主要结果：**
    *   **模型表现：** 随机森林模型的 AUC 达到 **0.82**，表现出良好的预测能力。
    *   **核心发现：** 转座子（Transposons）在不同环境间的差异最显著（p=0.0017），且 SHAP 分析证实其是驱动耐药性传播的最主要特征。
    *   **环境差异：** 质粒和噬菌体相关耐药基因在特定环境中波动，而整合元件（IEs）则相对稳定。

---

#### 5. 资源与算力
*   **文中未充分披露。** 论文提到该流程是开源的（GitHub 已托管），但未详细列出训练模型所需的具体 GPU/CPU 型号或计算耗时。

---

#### 6. 论文的可信贡献
*   **量化了转座子的地位：** 过去研究常聚焦于质粒，本研究通过数据证明了转座子在环境耐药扩散中可能扮演着更基础、更关键的角色。
*   **端到端工具链：** 提供了从原始数据到风险评分的完整开源 Pipeline，降低了环境监测人员的使用门槛。
*   **跨场景验证：** 实验覆盖了从自然环境到人类社会的多种样本，增强了结论的普适性。

---

#### 7. 局限与风险
*   **数据库依赖：** 结果高度依赖于已知耐药基因和移动元件的数据库（如 CARD）。如果环境中存在未知的、新型的耐药机制，模型将无法识别。
*   **相关性非因果性：** 机器学习模型识别出的是“转座子丰度与风险的相关性”，并不能直接证明是转座子导致了某次具体的爆发。
*   **数据偏差：** 不同环境的测序深度和质量不一，可能对 MGEs 的检出率产生系统性偏差。

---

#### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事环境微生物组、传染病监测、以及生物信息学工具开发的 AI 研究者。
*   **后续可跟进的问题：** 是否可以利用**图神经网络（GNN）**来建模 contig（拼接片段）上 ARGs 与 MGEs 的物理邻近关系，从而比单纯的丰度统计更精准地预测“跳跃”发生的概率？

（完）
