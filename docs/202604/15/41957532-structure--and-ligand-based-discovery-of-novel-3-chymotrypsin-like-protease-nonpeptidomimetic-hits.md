---
title: Structure- and Ligand-Based Discovery of Novel 3-Chymotrypsin-Like Protease Nonpeptidomimetic Hits.
title_zh: 基于结构和配体的新型3-胰凝乳蛋白酶样蛋白酶非拟肽类命中化合物的发现
authors: "Sabrina Silva-Mendonça, Donald Seanego, Christopher Jurisch, Melina Mottin, Flávia Nader Motta, Beatriz S A Rodrigues, Gilberto S M Junior, Alexandra Maria Dos Santos Carvalho, Fábio Muniz de Oliveira, Sunniva Sigurdardóttir, Per Sunnerhagen, Izabela Marques Dourado Bastos, Richard Gessner, Kelly Chibale, Carolina Horta Andrade"
date: 2026-04-14
pdf: "https://pubmed.ncbi.nlm.nih.gov/41957532/"
tags: ["query:pathoai"]
score: 9.0
evidence: 机器学习用于新冠病毒3CL蛋白酶抑制剂发现
tldr: 针对新冠病毒3CL蛋白酶（3CLpro）易受变异株影响的问题，本研究结合基于配体（形状匹配、机器学习）与基于结构（集成对接）的计算方法，从H3D和ChemBridge数据库中筛选非肽类抑制剂。通过实验验证，成功发现6个活性分子，其中LabMol-499表现最佳（IC50为13.71 µM），且证实其为非竞争性可逆抑制剂，为开发新型抗病毒药物提供了先导化合物。
selection_source: fresh_fetch
motivation: 现有的新冠药物面临病毒变异挑战，需要寻找作用机制不同的新型非肽类3CL蛋白酶抑制剂。
method: 结合了形状匹配、集成对接以及基于随机森林算法与ECFP4分子指纹的机器学习模型，对大规模化合物库进行虚拟筛选。
result: 成功鉴定出6个具有抑制活性的新化合物，其中LabMol-499的IC50值为13.71 µM，且表现出非竞争性可逆抑制特征。
conclusion: 该研究证明了多策略计算筛选在发现新型蛋白酶抑制剂中的有效性，并为后续的药物先导化合物优化奠定了基础。
---

## 摘要
SARS-CoV-2 3-胰凝乳蛋白酶样（3CLpro）蛋白酶是开发 COVID-19 治疗药物的关键靶点。虽然恩斯特韦（ensitrelvir）和奈玛特韦（nirmatrelvir）是已获批的治疗药物，但为了应对变异株和其他相关病毒的出现，持续研发新型抗病毒药物仍是必要的。本研究采用基于结构和配体的计算机辅助方法来鉴定新型 3CLpro 非拟肽类抑制剂。利用来自 COVID Moonshot、NCATS

## Abstract
The SARS-CoV-2 3-chymotrypsin-like (3CLpro) protease is a key target for the development of COVID-19 therapeutics. While ensitrelvir and nirmatrelvir are approved drugs for treatment, the continuous research and development for new antiviral drugs is necessary to combat the emergence of variants and other related viruses. This study employed structure- and ligand-based computer-assisted approaches to identify new 3CLpro nonpeptidomimetic inhibitors. Using data from COVID Moonshot, NCATS, and the literature, computational methods such as shape-based, ensemble docking, and machine learning (ML) techniques were developed, achieving robust validation metrics: AUC = 87%, EF = 7, BEDROC = 60% for shape-based; AUC = 87%, EF = 7.03, BEDROC = 62% for ensemble docking, and ACC = 81%, MCC = 62% for ML models, combing Random forest + ECFP4 fingerprint. These models were utilized in virtual screening (VS) campaigns using the H3D and ChemBridge libraries, from which six promising hits with IC50 values ≤80 µM were identified, including LabMol-499 with an IC50 of 13.71 µM and a Ki of 21.74 µM. Moreover, we found that LabMol-499 acts as a noncompetitive, reversible inhibitor of 3CLpro. These findings provide a foundation for hit-to-lead optimization of new nonpeptidomimetic 3CLpro inhibitors.

---

## 论文详细总结（自动生成）

这篇论文展示了如何结合传统的分子模拟与现代机器学习技术，从海量化学库中筛选出能够抑制新冠病毒（SARS-CoV-2）复制的关键蛋白酶抑制剂。

### 1. 解决的问题与研究意义
*   **核心问题**：寻找新型的**3CLpro（3-胰凝乳蛋白酶样蛋白酶）**抑制剂。3CLpro 是新冠病毒复制的核心“加工厂”，切断它病毒就无法增殖。
*   **研究意义**：虽然已有奈玛特韦（辉瑞 Paxlovid 成分）等药物，但病毒在不断变异，且现有药物多为“拟肽类”（结构像蛋白质片段），容易被体内酶降解。这篇论文的目标是寻找**非拟肽类**（结构不像蛋白质）的小分子，这类分子通常更稳定、药代动力学性质更好。

### 2. 白话版概述
研究团队像玩“层层滤网”游戏一样，把超过 120 万个化合物放进一个三层漏斗：
1.  **第一层（形状比对）**：看分子长得像不像已知的有效药物。
2.  **第二层（物理模拟）**：把分子丢进病毒蛋白的 3D 模型里，看能不能“卡”得严丝合缝（考虑了蛋白的动态抖动）。
3.  **第三层（AI 预测）**：用训练好的随机森林模型预测这个分子是否有活性。
最后，他们从剩下的几十个“种子选手”中通过实验室实验抓到了 6 个有效的分子，其中最强的叫 **LabMol-499**。

### 3. 方法部分：核心思想与关键设计
该研究采用了**共识虚拟筛选（Consensus Virtual Screening）**策略，将三种不同维度的计算方法串联：

*   **基于配体的形状匹配（Shape-based）**：
    *   **核心**：以一个已知的强效抑制剂为模板，计算库中分子的 3D 形状和化学特征重叠度。
    *   **取舍**：作为第一步，计算速度快，能迅速排除掉 99% 形状完全不符的分子。
*   **集成对接（Ensemble Docking）**：
    *   **核心**：蛋白质不是僵硬的，而是会“呼吸”抖动的。研究者选择了 5 种不同的蛋白构象（PDB 结构），让分子分别去试。
    *   **设计**：采用了从粗到精（HTVS -> SP -> XP）的对接精度，平衡了计算成本和准确性。
*   **机器学习模型（ML/QSAR）**：
    *   **模型结构**：**随机森林（Random Forest）** + **ECFP4 分子指纹**（一种将分子结构转化为 0/1 向量的编码方式）。
    *   **可解释性**：引入了 **SHAP 值分析**，揭示了模型认为哪些化学基团（如吡啶、嘧啶环）对活性贡献最大，这为后续化学家修改分子提供了指南。

### 4. 实验部分：数据与结果
*   **数据集**：整合了来自 COVID Moonshot、NCATS 和公开文献的数千个已知活性/无活性分子数据。
*   **评价指标**：
    *   **计算端**：AUC（曲线下面积）达到 0.87，MCC（马修斯相关系数）为 0.62，显示了极高的分类可靠性。
    *   **实验端**：使用 FRET 酶促实验（一种通过荧光变化检测蛋白酶是否被抑制的方法）进行验证。
*   **主要结果**：
    *   成功鉴定出 6 个命中化合物（Hits），IC50（抑制 50% 病毒蛋白活性所需的浓度）在 13.71 µM 到 80 µM 之间。
    *   **LabMol-499** 表现最好，且实验证明它是一种**非竞争性、可逆**抑制剂。这意味着它可能不是死磕蛋白的活性中心，而是通过结合其他部位让蛋白“瘫痪”。

### 5. 资源与算力
*   **文中未充分披露**具体的硬件配置（如 GPU/CPU 核数）或总计算耗时。文中提到了使用商业软件 Schrödinger Suite 和开源工具（RDKit, Scikit-learn）。

### 6. 真正可信的贡献
*   **多算法共识的有效性**：证明了将“物理模拟（对接）”与“统计学习（ML）”结合，比单一方法更能降低假阳性率。
*   **LabMol-499 的机制验证**：不仅预测了活性，还通过实验测定了抑制常数（Ki）和可逆性，证据链完整，是一个非常扎实的先导化合物起点。

### 7. 局限与风险
*   **活性强度尚在微摩尔级**：IC50 为 13.71 µM，虽然是很好的“命中”，但离真正的药物（通常需要纳摩尔级，nM）还有 100-1000 倍的差距。
*   **水溶性挑战**：预测显示 LabMol-499 的脂溶性（LogP）较高，水溶性较差，这在后续成药时可能导致吸收问题。
*   **外推风险**：模型基于现有已知骨架训练，对于完全新颖的化学空间可能存在预测盲区。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事药物虚拟筛选、蛋白质-配体相互作用建模、以及关注 AI 模型可解释性（SHAP）的研究者。
*   **后续可跟进的问题**：如何利用生成式 AI（Generative AI）以 LabMol-499 为骨架进行定向进化，在保持非拟肽特征的同时，将其活性从 µM 提升到 nM 级别？

（完）
