---
title: "OptiSyn: an interpretable, multi-omics-driven graph convolutional network framework for synergy-oriented drug combination design in disease treatment."
title_zh: OptiSyn：一种用于疾病治疗中协同导向药物组合设计的可解释、多组学驱动图卷积网络框架
authors: "Yinli Shi, Jun Liu, Guoduan Zeng, Yuedan Wang, Shuang Guan, Muzhi Li, Sicun Wang, Yanan Yu, Weibin Yang, Zhong Wang"
date: 2026-03-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/41877167/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 多组学驱动的图卷积网络用于药物组合设计
tldr: 针对中药复方配伍机制复杂、难以量化设计的问题，本研究开发了OptiSyn框架，通过整合多组学数据识别强直性脊柱炎的关键基因，并利用可解释的多层图卷积网络融合分子对接与临床经验，预测最优药物组合。该模型成功筛选出ASD-A复方，经实验验证能有效调节免疫反应并平衡IL17/Foxp3轴，为中医药现代化和精准联合用药提供了数据驱动的新路径。
selection_source: fresh_fetch
motivation: 旨在利用人工智能和多组学技术，解决传统中药复方配伍中机制不明、缺乏定量设计手段的挑战。
method: 构建了一个融合网络拓扑、分子对接、临床用药知识及化合物相似性的可解释多层图卷积网络模型。
result: 成功识别出8个强直性脊柱炎关键基因，并筛选出能显著降低炎症因子、调节免疫细胞比例的ASD-A中药复方。
conclusion: 该研究证明了AI驱动的药物设计能够与中医“君臣佐使”理论相结合，为复杂疾病的联合治疗提供了科学依据。
---

## 摘要
背景：生物信息学和大规模计算建模已成为现代生物医学科学的重要研究领域，助力药物发现和治疗优化。利用系统生物学和人工智能（AI）技术整合多维数据，为中药（TCM）方剂的现代化和机制阐明提供了一个独特且强大的技术框架。方法：利用多组学数据集、差异基因表达分析、加权基因共表达网络分析、单细胞转录组分析、孟德尔随机化和网络模块划分，鉴定了强直性脊柱炎（AS）相关的关键核心基因。为了预测最佳药物组合和协同的君臣佐使治疗作用，利用网络拓扑特征、分子对接数据、临床用药经验知识和化合物聚类相似性，构建了一个可解释的多层图卷积网络模型。结果：以AS为代表性疾病模型，发现了8个AS相关的核心基因。该模型优先筛选出一种可能的中药方剂ASD-A，由没药、骨碎补、枸杞子、淫羊藿、牛膝、高良姜、连翘和黄芪组成。消融实验强调了多源信息整合在方剂筛选和定制化干预方法创建中的关键作用，而模型性能评估显示出强大的预测潜力。功能富集分析发现，鉴定的核心基因与免疫反应和T细胞介导的免疫过程紧密相关。体内外实验证实，ASD-A显著降低了促炎细胞因子（如IL-6和TNF-α，P < 0.05），调节了CD80和CD86细胞亚群的比例，并调节了KRAS、SMAD2和MAPK14等重要基因的表达（P < 0.05）。此外，在激活的Jurkat细胞中，ASD-A显著降低了IL17荧光，同时增加了Foxp3荧光（P < 0.05），表明其重新平衡了IL17/Foxp3轴。方剂分解分析进一步阐明了主要和辅助成分在控制核心基因活性中的作用。结论：所提出的AI驱动方剂设计方法为AS的联合治疗策略提供了新见解，同时也符合中药理论的“君臣佐使”原则。本研究展示了将现代生物信息学和AI技术与传统医学相结合的巨大潜力，有助于实现高效且具有机制依据的疾病治疗。

## Abstract
BACKGROUND: Bioinformatics and large-scale computational modelling have emerged as essential research fields in modern biomedical science, enabling drug discovery and therapeutic optimisation. A unique and potent technical framework for the modernisation and mechanistic clarification of traditional Chinese medicine (TCM) formulations is provided by the integration of multidimensional data using systems biology and artificial intelligence (AI) techniques. METHODS: Ankylosing spondylitis-associated key hub genes were identified using multi-omics datasets, differential gene expression analysis, weighted gene co-expression network analysis, single-cell transcriptomic analysis, Mendelian randomization, and network module partitioning. In order to predict the optimal drug combinations and synergistic principal-auxiliary therapeutic roles, an interpretable, multi-layer graph convolutional network model was built using network topology features, molecular docking data, empirical clinical medication knowledge, and compound clustering similarity. RESULTS: Eight AS-associated hub genes were found using AS as a representative disease model. A possible TCM formula, ASD-A, comprising Myrrha, Drynariae Rhizoma, Lycii Fructus, Epimedii Folium, Achyranthis Bidentatae Radix, Alpiniae Officinarum Rhizoma, Forsythiae Fructus, Astragali Radix, was prioritised by the proposed model. While ablation studies highlighted the crucial role of multi-source information integration in compound formula screening and the creation of customised intervention methods, model performance evaluation showed strong predictive potential. The identified hub genes were found to be tightly linked to immunological responses and T-cell-mediated immune processes, according to functional enrichment analyses. Experiments conducted both in vivo and in vitro confirmed that ASD-A significantly reduced pro-inflammatory cytokines like IL-6 and TNF-α (P < 0.05), modulated the proportions of CD80 and CD86 cell subsets, and regulated the expression of important genes like KRAS, SMAD2, and MAPK14 (P < 0.05). Furthermore, in activated Jurkat cells, ASD-A significantly decreased IL17 fluorescence while increasing Foxp3 fluorescence (P < 0.05), indicating a rebalancing of the IL17/Foxp3 axis. The roles of major and auxiliary components in controlling hub gene activity were further clarified by formula decomposition analysis of ASD-A. CONCLUSION: The suggested AI-driven formula design approach provides new insights into combinatorial therapy approaches for AS while also conforming to the TCM theory of Jun-Chen-Zuo-Shi principle. The significant potential of combining contemporary bioinformatics and AI techniques with traditional medicine is demonstrated by this study, which could facilitate efficient and mechanistically informed disease therapy.

---

## 论文详细总结（自动生成）

这篇论文介绍了一个名为 **OptiSyn** 的计算框架，旨在利用人工智能（AI）和多组学数据来优化中药复方（多种药物组合）的设计。

### 1. 解决的问题与研究意义
*   **核心问题**：传统中药复方（TCM Formula）的配伍（哪些药配在一起）往往依赖经验，缺乏现代科学的定量解释。同时，面对强直性脊柱炎（AS）等复杂疾病，如何从成千上万种药物组合中找到具有“协同效应”（1+1>2）的最优组合是一个巨大的搜索难题。
*   **研究意义**：它尝试用 AI 填补“传统医学理论”与“现代分子生物学”之间的鸿沟，将中医的“君臣佐使”配伍原则转化为可计算、可解释的图神经网络模型。

### 2. “白话版”概述
想象你要组建一支特种部队（中药复方）去攻克一个顽固的堡垒（疾病）。首先，你通过大数据分析找到堡垒最脆弱的几个大门（核心基因）。然后，你用一个智能算法（OptiSyn）在士兵库里挑选最合适的队员，不仅看每个士兵的单兵作战能力（分子对接），还要看他们之间配合是否默契（临床经验和化学相似性）。最后，算法不仅给了你名单，还告诉你谁是队长（君药）、谁是副官（臣药）。

### 3. 方法部分
*   **核心思想**：将药物、基因、疾病之间的复杂关系建模为一个“异质图”，利用图卷积网络（GCN）学习这些节点之间的深层互动。
*   **模型结构**：
    *   **多组学筛选**：利用 WGCNA（加权基因共表达网络分析，找成群起作用的基因）、单细胞测序和孟德尔随机化（一种利用遗传变异寻找因果关系的统计方法）锁定 8 个强直性脊柱炎的关键核心基因。
    *   **多层 GCN 框架**：输入层整合了四类信息：
        1.  **网络拓扑**：基因与基因之间的相互作用。
        2.  **分子对接**：模拟药物分子与目标蛋白结合的紧密程度。
        3.  **临床知识**：历史上已有的有效用药经验。
        4.  **化合物相似性**：结构相似的药物可能有相似功能。
*   **关键设计取舍**：模型放弃了纯粹的“黑盒”预测，而是引入了**可解释性设计**，通过分析 GCN 的权重来对应中医的“君臣佐使”角色，使预测结果能被医生理解。

### 4. 实验部分
*   **数据与任务**：以强直性脊柱炎（AS）为模型，从多组学数据库中提取数据，预测并设计名为 **ASD-A** 的新复方（包含没药、黄芪等 8 味药）。
*   **Baseline 与评价**：进行了消融实验（Ablation Study），证明如果去掉“临床经验”或“分子对接”中的任何一环，模型的预测准确度都会显著下降。
*   **主要结果**：
    *   **生物验证**：在细胞和动物实验中，ASD-A 显著降低了炎症因子（IL-6, TNF-α）。
    *   **免疫调节**：实验证明该药方能重新平衡 T 细胞免疫（调节 IL17/Foxp3 轴），这是治疗自身免疫疾病的关键。

### 5. 资源与算力
*   **文中未充分披露**具体的 GPU 型号或训练时长，但考虑到 GCN 模型和分子对接的规模，通常需要中等规模的计算集群或高性能工作站。

### 6. 真正可信的贡献
*   **证据最强的结论**：ASD-A 复方对 IL17/Foxp3 轴的调节作用得到了体内外实验的双重验证，这证明了模型筛选出的药物组合确实具有生物学活性。
*   **理论贡献**：成功将“君臣佐使”这一抽象的中医概念映射到了图神经网络的节点重要性评分上。

### 7. 局限与风险
*   **外推风险**：目前仅在强直性脊柱炎（AS）上进行了验证，模型是否适用于癌症或其他复杂疾病尚不确定。
*   **成分复杂性**：中药每味药含有成百上千种成分，模型在处理“草药-成分-靶点”的多对多映射时可能做了简化处理。
*   **数据偏差**：临床经验数据可能存在幸存者偏差或记录不全的问题。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事药物组合发现（Drug Combination）、网络药理学、以及希望将传统医学知识图谱化的 AI 研究者。
*   **后续可跟进的问题**：如何处理中药成分在人体内代谢后的动态变化（PK/PD），并将其整合进图神经网络的动态边权重中？

（完）
