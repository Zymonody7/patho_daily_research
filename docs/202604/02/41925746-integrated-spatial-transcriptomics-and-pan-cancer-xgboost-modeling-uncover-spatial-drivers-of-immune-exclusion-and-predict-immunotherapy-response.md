---
title: Integrated spatial transcriptomics and pan-cancer XGBoost modeling uncover spatial drivers of immune exclusion and predict immunotherapy response.
title_zh: 整合空间转录组学与泛癌 XGBoost 建模揭示免疫排斥的空间驱动因素并预测免疫治疗反应
authors: "Hongying Zhao, Wangyang Liu, Haotian Xu, Lu Wang, Zushun Chen, Yanwu Sun, Li Wang"
date: 2026-04-02
pdf: "https://pubmed.ncbi.nlm.nih.gov/41925746/"
tags: ["query:seqai"]
score: 9.0
evidence: 整合空间转录组学和 XGBoost 模型用于癌症研究
tldr: 针对免疫治疗中肿瘤微环境空间复杂性难以刻画的问题，本研究整合27种癌症的多组学数据与空间转录组技术，识别出驱动免疫排斥的关键调控轴（如SNHG6-BIRC5），并结合CRISPR筛选和药理基因组学验证了其功能。在此基础上，构建了基于14个特征的泛癌XGBoost预测模型，在免疫治疗响应预测中达到0.771的AUC，优于传统标志物，为精准免疫治疗提供了空间维度的见解和预测工具。
selection_source: fresh_fetch
motivation: 旨在揭示肿瘤免疫微环境中非编码RNA调控网络如何通过空间定位驱动免疫排斥，并提升免疫治疗响应的预测精度。
method: 整合多组学分析、空间转录组定位、CRISPR功能筛选以及基于14个关键特征的XGBoost机器学习建模。
result: 发现SNHG6-BIRC5轴是肺腺癌免疫冷表型的关键驱动因素，且开发的泛癌预测模型在区分免疫治疗响应者方面表现优于PD-L1。
conclusion: 研究证明了空间转录组结合机器学习能有效识别免疫排斥的驱动因子，并为癌症精准医疗提供了可靠的生物标志物和在线预测工具。
---

## 摘要
免疫治疗彻底改变了癌症治疗，但表征肿瘤免疫微环境的空间复杂性仍是一项挑战。在本研究中，我们建立了一个整合了 27 种癌症类型多组学分析的综合计算框架，以解码免疫相关的非编码 RNA 调控网络。超越传统的批量分析，我们利用空间转录组学来剖析这些调节因子的空间定位。我们确定了 SNHG6-BIRC5 轴是肺腺癌“免疫冷”表型的关键驱动因素。我们提供了视觉证据，证明该轴定位于肿瘤巢，并与 T 细胞浸润呈负相关，从而阐明了空间免疫排斥的机制。为了验证这些发现的临床相关性，全基因组规模的 CRISPR-Cas9 筛选数据证实了这些靶点对癌细胞生存的功能必要性。此外，药物基因组学分析显示，该轴的高表达与长春花碱等化疗药物的敏感性相关，这为免疫排斥型肿瘤患者提供了一种潜在的分层策略。为了将临床效用扩展到免疫治疗预测，我们开发了一个包含 14 个高性能调节特征的泛癌 XGBoost 机器学习模型。该模型在区分免疫治疗响应者与非响应者方面表现稳健，AUC 达到 0.771，优于 PD-L1 等传统标志物。总之，本研究强调了免疫排斥和化疗敏感性的空间决定因素，并提出了一种用于精准免疫治疗分层的通用机器学习工具。开发的在线资源可免费使用，以促进整个社区的生物标志物发现。

## Abstract
Immunotherapy has revolutionized cancer treatment, yet characterizing the spatial complexity of the tumor immune microenvironment remains a challenge. In this study, we established a comprehensive computational framework integrating multi-omics profiling across 27 cancer types to decode immune-related non-coding RNA regulatory networks. Moving beyond traditional bulk analysis, we utilized spatial transcriptomics to dissect the spatial localization of these regulators. We identified the SNHG6-BIRC5 axis as a critical driver of the "immune-cold" phenotype in lung adenocarcinoma. We provide visual evidence that this axis localizes to tumor nests and negatively correlates with T- cell infiltration, elucidating a mechanism of spatial immune exclusion. Validating the clinical relevance of these findings, genome-scale CRISPR-Cas9 screening data confirmed the functional essentiality of these targets for cancer cell survival. Furthermore, pharmacogenomic analysis revealed that high expression of this axis correlates with sensitivity to chemotherapy agents like Vinblastine, suggesting a potential stratification strategy for patients with immune-excluded tumors. To expand the clinical utility to immunotherapy prediction, we developed a pan-cancer XGBoost machine learning model incorporating 14 high-performance regulatory features. This model achieved robust performance in distinguishing immunotherapy responders from non-responders with an AUC of 0.771, outperforming traditional markers such as PD-L1. Collectively, this study highlights spatial determinants of immune exclusion and chemotherapy sensitivity- and presents a generalized machine- learning tool for precision immunotherapy stratification. The developed online resource is freely available to facilitate community-wide biomarker discovery.