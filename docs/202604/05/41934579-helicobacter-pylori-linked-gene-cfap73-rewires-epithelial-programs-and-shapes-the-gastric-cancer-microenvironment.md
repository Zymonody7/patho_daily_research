---
title: Helicobacter pylori-linked gene CFAP73 rewires epithelial programs and shapes the gastric cancer microenvironment.
title_zh: 幽门螺杆菌相关基因 CFAP73 重塑上皮程序并塑造胃癌微环境
authors: "Haiwen Li, Ran Wei, Yuhan Liu, Jiaju Wang, Xinyi Wang, Li Chen, Bangjie Chen, Yong Yao"
date: 2026-04-04
pdf: "https://pubmed.ncbi.nlm.nih.gov/41934579/"
tags: ["query:pathoai"]
score: 7.0
evidence: 利用随机森林模型研究幽门螺杆菌感染对胃癌微环境的影响
tldr: 幽门螺杆菌（HP）感染是胃癌的主要诱因，但其诱导上皮细胞恶变的具体机制尚不明确。本研究通过整合多组学数据和空间转录组学，发现纤毛相关蛋白CFAP73是受HP感染抑制的关键抑癌基因。CFAP73的缺失会激活EMT和增殖通路，并重塑肿瘤微环境，使其向免疫抑制状态转变。该研究揭示了CFAP73作为连接HP感染与胃癌进展的生物标志物，为评估预后和化疗敏感性提供了新视角。
selection_source: fresh_fetch
motivation: 旨在阐明幽门螺杆菌感染如何通过干扰特定的上皮细胞程序，驱动胃粘膜向恶性肿瘤转化的分子机制。
method: 结合趋势检验、随机森林建模、单细胞测序及空间转录组技术，在多个独立队列中筛选并验证与HP感染及胃癌预后相关的关键基因。
result: 鉴定出CFAP73为核心抑癌因子，其表达随HP感染降低，且高表达与良好的生存预后、顺铂化疗敏感性及抗肿瘤免疫微环境显著相关。
conclusion: CFAP73是HP驱动胃癌发生的关键分子开关，其失活不仅促进上皮细胞恶性重编程，还通过调控成纤维细胞和T细胞状态构建促癌微环境。
---

## 摘要
背景：幽门螺杆菌（HP）感染是胃癌最强的环境驱动因素，但在感染过程中逐渐被破坏并与恶性转化相关的上皮程序仍不清楚。方法：利用 Jonckheere-Terpstra 检验在 HP 感染数据集（GSE60662、GSE60427）中鉴定趋势相关基因，并将其与 TCGA-STAD 中的生存相关基因取交集。整合随机森林建模、多个独立验证队列、功能分析、单细胞 RNA 测序（GSE249874）、配体-受体推断以及空间转录组学，以定义 CFAP73 的生物学作用及其对微环境的影响。结果：CFAP73 被鉴定为在 HP 感染期间逐渐下调的最显著的肿瘤保护基因，且能强力预测良好的生存预后和顺铂获益。CFAP73 的表达标志着一种抑癌性上皮状态，其特征为增殖减少、上皮-间质转化（EMT）受抑制以及 p53 和凋亡通路的激活。单细胞分析显示 CFAP73 主要存在于非恶性上皮细胞中，HP 感染会导致其缺失。CFAP73+ 上皮细胞表现出 LCN2 表达增加和致癌信号减弱。在微环境方面，CFAP73 高表达肿瘤富集了效应 T 细胞和 Th17 T 细胞，并显示出耗竭性 T 细胞、调节性 T 细胞（Tregs）以及促肿瘤相关成纤维细胞（CAF）状态（iCAF、apCAF）的减少。配体-受体建模显示，CFAP73+ 上皮细胞接收到来自 CAF 的 WNT、TGFβ 和 PDGF 信号较弱，但与 T 细胞的细胞毒性相互作用较强。空间转录组学证实，CFAP73+ 上皮区域与增殖活跃、缺氧及免疫检查点活跃的微环境（niches）在空间上是分离的。结论：CFAP73 是一种此前未被认识的、在 HP 感染早期即被抑制的上皮抑癌因子。CFAP73 的缺失可能促进了上皮细胞的恶性重编程，并将成纤维细胞和 T 细胞状态重塑为免疫抑制性的促肿瘤微环境。CFAP73 是连接 HP 驱动的黏膜损伤与胃癌发生、进展及治疗反应的有潜力的生物标志物。

## Abstract
BACKGROUND: Helicobacter pylori (HP) infection is the strongest environmental driver of gastric cancer, yet the epithelial programs that are progressively disrupted during infection and are associated with malignant transformation remain unclear. METHODS: Trend-associated genes across HP-infection datasets (GSE60662, GSE60427) were identified using the Jonckheere-Terpstra test and intersected with survival-associated genes in TCGA-STAD. Random-forest modeling, multiple independent validation cohorts, functional analyses, single-cell RNA-seq (GSE249874), ligand-receptor inference, and spatial transcriptomics were integrated to define the biological role and microenvironmental impact of CFAP73. RESULTS: CFAP73 emerged as the top tumor-protective gene progressively downregulated during HP infection and strongly predictive of favorable survival and cisplatin benefit. CFAP73 expression marked a tumor-suppressive epithelial state characterized by reduced proliferation, EMT inhibition, and activation of p53 and apoptotic pathways. Single-cell analysis showed CFAP73 predominantly in non-malignant epithelial cells, with HP infection driving its loss. CFAP73 + epithelial cells displayed increased LCN2 expression and attenuated oncogenic signaling. Microenvironmentally, CFAP73_high tumors were enriched for effector and Th17 T cells and showed reduced exhausted T cells, Tregs, and pro-tumorigenic CAF states (iCAF, apCAF). Ligand-receptor modeling revealed that CFAP73 + epithelial cells received weaker WNT, TGFβ, and PDGF signals from CAFs but stronger cytotoxic interactions from T cells. Spatial transcriptomics confirmed spatial segregation of CFAP73 + epithelial regions from proliferative, hypoxic, immune-checkpoint-active niches. CONCLUSIONS: CFAP73 is a previously unrecognized epithelial tumor suppressor suppressed early during HP infection. Loss of CFAP73 may contribute to epithelial malignant reprogramming and reshapes fibroblast and T-cell states toward an immunosuppressive, pro-tumor microenvironment. CFAP73 represents a promising biomarker linking HP-driven mucosal injury to gastric cancer initiation, progression, and therapeutic response.