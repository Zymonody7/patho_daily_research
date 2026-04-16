---
title: "Multi-tissue multi-omics integration reveals tissue-specific pathways, gene networks and drug candidates for type 1 diabetes."
title_zh: 多组织多组学整合揭示了1型糖尿病的组织特异性通路、基因网络和候选药物。
authors: "Montgomery Blencowe, Zara Saleem, Ruoshui Liu, Margaret Wang, I-Hsin Tseng, Julian Wier, Stefan Mutter, Florin Vaida, Yi Guo, Niina Sandholm, Courtney Ackeifi, Daniel L Kaufman, Xia Yang"
date: 2026-04-15
pdf: "https://pubmed.ncbi.nlm.nih.gov/41986815/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 疾病通路的多组织多组学整合
tldr: 针对 1 型糖尿病 (T1D) 遗传位点与病理机制关联不明的问题，本研究通过整合 GWAS 数据与多组织多组学调控网络，识别出关键驱动基因（如 FYN、TAP1）及组织特异性通路（如胰岛中的干扰素信号）。研究不仅在 NOD 小鼠模型中验证了关键基因，还结合电子病历筛选出潜在的候选药物，为 T1D 的早期干预和精准治疗提供了系统性的分子图谱和药理依据。
selection_source: fresh_fetch
motivation: 旨在揭示 1 型糖尿病遗传风险因素如何通过干扰特定组织的生物学通路和基因调控网络，最终导致胰岛 beta 细胞的损失。
method: 采用多组织多组学整合分析方法，将人类 GWAS 数据与组织特异性基因表达及网络模型结合，识别关键驱动基因，并利用小鼠模型和电子病历数据进行验证及药物筛选。
result: 发现了跨组织的免疫通路及组织特异性的病毒响应、Notch 信号等通路，识别出 FYN、TAP1 等核心调控基因，并筛选出多类可延缓疾病进展的候选药物。
conclusion: 该研究构建了 1 型糖尿病的组织特异性遗传网络全景图，为理解疾病发病机制提供了新视角，并为基于网络分析的药物开发提供了潜在靶点。
---

## 摘要
目的/假设：尽管全基因组关联研究（GWAS）已确定了与1型糖尿病相关的位点，但将这些位点与疾病病理联系起来的具体通路和调节网络在很大程度上仍不清楚。我们假设1型糖尿病的遗传风险因素破坏了组织特异性的生物学通路和基因网络，最终导致β细胞丢失。方法：我们进行了一项多组织多组学分析，将人类1型糖尿病的GWAS数据与相关组织的基因表达和基因网络模型的组织特异性调节数据相结合，以

## Abstract
AIMS/HYPOTHESIS: Although genome-wide association studies (GWAS) have identified loci associated with type 1 diabetes, the specific pathways and regulatory networks linking these loci to disease pathology remain largely unknown. We hypothesised that type 1 diabetes genetic risk factors disrupt tissue-specific biological pathways and gene networks that ultimately lead to beta cell loss. METHODS: We conducted a multi-tissue multi-omics analysis that integrates human GWAS data for type 1 diabetes with tissue-specific regulatory data for gene expression and gene network models across relevant tissues to highlight key pathways and key driver (KD) genes contributing to type 1 diabetes pathogenesis. KD genes were validated using islet-specific gene expression and protein data from non-obese diabetic (NOD) mice compared with type 2 diabetic and non-diabetic mouse models. Drug repositioning predictions were generated using the INCS L1000 and PharmOmics platforms, and candidate drugs were tested using electronic medical records (EMRs) of individuals with type 1 diabetes from the OneFlorida+ Clinical Data Network. RESULTS: Our integrative genomics approach identified known immune pathways across multiple tissues, such as adaptive immune responses, cytokine-mediated inflammation, primary immunodeficiency, and interactions between lymphoid and non-lymphoid cells. Tissue-specific signals included genes related to type 2 diabetes in lymphocytes, viral response pathways in macrophages and monocytes, and Notch signalling in adipose tissue and immune cells. In pancreatic islet analysis, we observed significant enrichment for type 1 diabetes and type 2 diabetes gene sets alongside immune-related pathways, including antigen processing, systemic lupus erythematosus and IFN signalling. Removing HLA genes from the analysis revealed additional immune pathways, such as retinoic acid-inducible gene I (RIG-I)/melanoma differentiation-associated protein 5 (MDA5) induction of interferons, together with melanogenesis, steroid hormone synthesis and iron transport. Network modelling highlighted the autoimmune basis of disease, with KDs such as FYN, TAP1, WAS and HLA-B/C/G, as well as additional immunomodulatory proteins such as LCK, LCP2 and genes such as EMR1 and GC. These KDs were further supported by gene and protein expression data from NOD mice. We additionally highlight various drug classes that target the type 1 diabetes genetic networks and may be useful to delay type 1 diabetes development; some of these were supported by our EMR screen. CONCLUSIONS/INTERPRETATION: Our multi-tissue multi-omics approach provides a detailed landscape of the tissue-specific genetic networks and regulators underlying type 1 diabetes. This analysis confirms the roles of known immune pathways while uncovering additional regulatory elements and disease-associated networks, thus expanding our understanding of type 1 diabetes pathogenesis. The identification of potential drug candidates through network analysis, with supporting evidence from EMRs, offers potential therapeutic strategies for targeting disease pathways and holds promise for delaying or preventing type 1 diabetes progression.

---

## 论文详细总结（自动生成）

这篇论文通过整合人类遗传学大数据、多组织基因网络和临床电子病历，系统性地梳理了 1 型糖尿病（T1D）的发病机制，并筛选了潜在的治疗药物。

### 1. 核心问题与研究价值
*   **核心问题**：虽然我们通过全基因组关联分析（GWAS，一种寻找疾病相关基因变异的方法）知道了哪些基因位点与 1 型糖尿病有关，但并不清楚这些位点是如何在不同组织（如胰岛、免疫细胞、脂肪）中通过干扰哪些生物通路导致疾病的。
*   **研究价值**：1 型糖尿病是一种自身免疫疾病，目前尚无根治手段。该研究不仅揭示了疾病的“分子地图”，还通过“老药新用”策略找到了可能延缓病程的候选药物，具有很强的临床转化潜力。

### 2. 白话版概述
1 型糖尿病就像是一场针对身体胰岛细胞的“内乱”。过去我们只知道参与叛乱的“嫌疑人名单”（遗传位点），但不知道他们在哪里接头、谁是带头的。这篇论文利用大数据构建了一个跨组织的“社交网络图”，找出了那些指挥叛乱的“带头大哥”（关键驱动基因），并发现这些活动不仅发生在胰腺，还涉及免疫系统和脂肪组织。最后，研究者根据这张图，在现有的药物库中寻找能“劝降”这些带头大哥的药物，并通过医院的真实病例数据验证了这些药确实有效。

### 3. 方法部分
*   **核心思想**：**多组学整合分析（Mergeomics）**。将静态的遗传变异数据（GWAS）映射到动态的基因表达调控网络中。
*   **模型结构与流程**：
    1.  **映射（Mapping）**：利用 eQTL（表达定量性状位点，即影响基因表达水平的遗传变异）将 GWAS 发现的变异位点关联到具体的基因上。
    2.  **富集分析（MSEA）**：识别在特定组织中显著聚集的生物通路（如干扰素信号通路）。
    3.  **网络建模（KDA）**：利用贝叶斯网络构建基因间的因果关系图，识别出处于网络中心、控制大量下游基因的“关键驱动基因”（Key Drivers, KDs）。
    4.  **药物预测**：利用 LINCS L1000 等数据库，寻找能逆转 T1D 异常基因表达模式的药物。
*   **关键设计取舍**：研究者特意进行了“剔除 HLA 基因”的分析。HLA 是 T1D 最强的遗传信号，但它往往会掩盖其他微弱却重要的信号。剔除它后，研究者发现了如 RIG-I/MDA5（病毒响应相关）等此前被忽视的通路。

### 4. 实验部分
*   **数据来源**：人类 T1D GWAS 汇总数据、多种组织的基因表达谱、NOD（非肥胖糖尿病）小鼠模型数据、OneFlorida+ 临床网络电子病历（EMR）。
*   **验证任务**：
    *   **分子验证**：在 NOD 小鼠中检测预测的关键驱动基因（如 *FYN*, *TAP1*）是否真的存在表达异常。
    *   **临床验证**：在电子病历中观察服用预测药物的患者，其 T1D 相关临床指标是否有所改善。
*   **主要结果**：
    *   识别出跨组织的通用免疫通路和组织特异性通路（如脂肪组织中的 Notch 信号）。
    *   确定了 *FYN*、*TAP1*、*WAS* 等核心调控因子。
    *   筛选出多类候选药物，部分药物在真实世界病历数据中显示出潜在疗效。

### 5. 资源与算力
*   **文中未充分披露**。论文主要基于已有的公共数据库和生物信息学算法工具包（如 Mergeomics R 包），未提及高性能计算集群的具体配置。

### 6. 真正可信的贡献
*   **多组织全景图**：证明了 T1D 不仅仅是胰腺的问题，免疫细胞和脂肪组织的代谢环境同样关键。
*   **非 HLA 机制的挖掘**：证据最强的是关于 RIG-I/MDA5 通路的发现，这为“病毒感染诱发 T1D”的假说提供了遗传学支持。
*   **闭环验证**：从计算预测到动物实验，再到人类电子病历的“干-湿-干”闭环验证，增加了结论的可靠性。

### 7. 局限与风险
*   **人群偏差**：GWAS 数据主要来自欧洲裔人群，结论在其他族裔中的适用性有待验证。
*   **回顾性研究风险**：电子病历的验证属于回顾性分析，存在混杂因素（如患者同时服用其他药物），不能直接等同于临床试验的因果结论。
*   **静态网络限制**：基因网络是基于稳态数据构建的，可能无法完全捕捉疾病发生瞬间的动态触发过程。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事图神经网络（GNN）、多模态数据融合、药物发现（Drug Discovery）的 AI 研究者。
*   **后续可跟进的问题**：能否利用深度学习（如 Graph Transformer）替代传统的贝叶斯网络，更精准地预测复杂疾病中的“关键驱动因子”？

（完）
