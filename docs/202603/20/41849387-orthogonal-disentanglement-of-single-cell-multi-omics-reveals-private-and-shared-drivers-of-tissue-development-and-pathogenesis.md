---
title: Orthogonal disentanglement of single-cell multi-omics reveals private and shared drivers of tissue development and pathogenesis.
title_zh: 单细胞多组学的正交解耦揭示了组织发育和发病机制的私有和共享驱动因素
authors: "Yi Fan, Yanchi Su, Gaoyang Hao, Fuzhou Wang, Xingjian Chen, Ka-Chun Wong, Xiangtao Li"
date: 2026-03-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/41849387/"
tags: ["query:bioinfo"]
score: 10.0
evidence: 用于解耦单细胞多组学数据的深度学习框架
tldr: 单细胞多组学数据因基因调控异步性存在模态特有（私有）与跨模态（共享）信号，难以精准解析。本研究提出OmiDos深度学习框架，通过领域适配和正交解耦技术分离这两类信号。该方法在聚类和批次校正任务中表现优异，并成功识别出小鼠腭部发育及髓母细胞瘤中的关键远端增强子，为理解组织发育与发病机制提供了更精细的生物学视角。
selection_source: fresh_fetch
motivation: 旨在解决单细胞多组学数据中由于基因调控异步性导致的模态特有信号与共享信号混杂、难以精确刻画生物动态的问题。
method: 提出名为OmiDos的深度学习框架，利用私有-共享成分分析、对抗学习和最大均值差异正则化，实现多组学潜在变量的正交解耦。
result: 在多平台数据集上实现了领先的聚类准确度和批次效应校正效果，并精准定位了调控上皮细胞分化及肿瘤进展的关键远端增强子。
conclusion: 通过对多组学信号进行正交解耦，能够更精细地揭示组织发育和疾病演变中的私有与共享驱动因素。
---

## 摘要
表征正常组织功能和疾病进展背后的基因表达和调控动态需要对单细胞多组学数据进行综合分析。然而，基因调控的异步性和单细胞多组学数据的快照特性产生了每个组学层特有的私有信号以及反映跨模态协调的共享信号。在此，我们提出了基于领域自适应的组学分离建模（OmiDos），这是一个灵活的、无需标注的深度学习框架，它通过私有-共享成分分析来解耦多组学数据中的组学特异性潜变量和组学间共享潜变量。其模块化架构能够无缝扩展，以整合对抗学习来处理非配对数据的不对齐问题，并重构其组件以利用最大均值差异正则化，从而最大限度地减少对生物变异性的干扰。通过这种解耦，OmiDos 能够在更精细的生物学粒度上估计基因表达和调控动态，并为各种下游分析提供支持。我们在跨越不同平台和组织类型的数据集上证明了 OmiDos 在聚类准确性、批次效应校正和不对齐解决方面的卓越性能。在小鼠次生腭发育中，OmiDos 精确识别了一个细胞类型特异性的非连锁远端增强子，阐明了其在调节上皮细胞分化和迁移中的关键作用。将 OmiDos 应用于髓母细胞瘤揭示了驱动 Neurod1 远端增强子区域部分闭合的潜在功能缺失，可能促成了髓母细胞瘤从正常状态向肿瘤状态的演变。

## Abstract
Characterizing gene expression and regulatory dynamics underlying both normal tissue function and disease progression requires an integrative analysis of single-cell multi-omics data. However, the asynchrony of gene regulation and the snapshot of single-cell multi-omics data give rise to private signals unique to each omics layer and shared signals reflecting cross-modality coordination. Here, we present Omics Separation Modeling using Domain Adaptation (OmiDos), a flexible annotation-free deep learning framework that disentangles omic-specific and interomic shared latent variables in multi-omics data with private-shared component analysis. Its modular architecture enables seamless extension to incorporate adversarial learning for unpaired data misalignment and to restructure its components to leverage the maximum mean discrepancy regularization, thereby minimizing interference with biological variability. Through this disentanglement, OmiDos enables the estimation of gene expression and regulatory dynamics at finer biological granularity and empowers various downstream analyses. We demonstrated the superior performance of OmiDos in terms of clustering accuracy, batch-effect correction, and misalignment resolution across datasets spanning diverse platforms and tissue types. In mouse secondary palate development, OmiDos precisely identified a cell type-specific unlinked distal enhancer, elucidating its essential role in the regulation of epithelial cell differentiation and migration. The application of OmiDos to medulloblastoma revealed a potential role deficiency in driving partial closure of the distal enhancer region of Neurod1 may contribute to the progression of medulloblastoma from normal to tumor states.