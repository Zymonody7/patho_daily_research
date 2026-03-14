---
title: Loop of N2-polarized neutrophils and exhausted CD8 + T cells induces immunotherapy resistance in NSCLC.
title_zh: N2极化中性粒细胞与耗竭性CD8+ T细胞之间的环路诱导非小细胞肺癌的免疫治疗耐药
authors: "Zhansheng Zou, Zhiyu Guo, Yuanhao Wei, Shaoxi Cai, Changhui Yu"
date: 2026-03-13
pdf: "https://pubmed.ncbi.nlm.nih.gov/41824204/"
tags: ["query:seqai"]
score: 7.0
evidence: 整合单细胞RNA测序数据集进行免疫微环境分析
tldr: 针对非小细胞肺癌中中性粒细胞导致免疫治疗耐药的机制不明问题，本研究通过整合大规模单细胞测序数据，揭示了N2型中性粒细胞与耗竭性CD8+ T细胞（Tex）之间通过ICAM1-整合素和CCL5-CCR1轴形成的促癌正反馈环路。基于此环路构建的深度学习模型和NTLS评分，能有效预测NSCLC及多种癌症的免疫治疗响应和预后，为克服耐药提供了新靶点和分层工具。
selection_source: fresh_fetch
motivation: 旨在阐明N2型中性粒细胞与耗竭性CD8+ T细胞在肺癌免疫微环境中的相互作用机制，并开发预测免疫治疗效果的临床模型。
method: 整合大规模单细胞转录组数据进行细胞通讯分析，并利用关键交互基因构建深度神经网络模型及预后评分系统（NTLS）。
result: 发现N2中性粒细胞通过ICAM1抑制T细胞NF-κB信号，而Tex细胞通过CCL5进一步激活中性粒细胞，形成维持免疫抑制环境的正反馈环路。
conclusion: 该研究定义的ICAM1-整合素和CCL5-CCR1交互轴是驱动免疫治疗耐药的关键机制，为癌症精准免疫治疗提供了稳健的预测工具。
---

## 摘要
虽然中性粒细胞是非小细胞肺癌（NSCLC）中主要的髓系成分，但N2极化中性粒细胞的具体免疫抑制功能及其与CD8⁺ T细胞的相互作用机制尚未得到完全阐明。此外，基于这些分子相互作用开发用于预后分层和免疫治疗反应预测的临床适用模型，仍是一项亟待解决的关键需求。我们整合了大规模单细胞RNA测序数据集以描绘肿瘤免疫微环境，并进行了通路富集和细胞间通讯分析。利用从这些相互作用中提取的关键分子特征构建了一个深度神经网络模型。该模型在大量（bulk）RNA测序队列上进行了训练和验证，用于预测免疫治疗反应。此外，我们开发了N2_Neu-CD8⁺ Tex环路评分（NTLS）用于预后评估，并评价了其在泛癌种中的适用性。我们的分析揭示了N2中性粒细胞与耗竭性CD8⁺ T细胞（Tex）之间存在一个此前未被表征的正反馈环路。中性粒细胞来源的ICAM1与CD8⁺ T细胞上的ITGAL/ITGB2结合，抑制其NF-κB信号通路并强化耗竭表型。以一种前馈方式，Tex来源的CCL5通过N2中性粒细胞上的CCR1发出信号，激活其NF-κB通路并进一步上调ICAM1的表达。这种ICAM1-整合素（Integrin）和CCL5-CCR1轴创建了一个自我维持的免疫抑制回路。基于该环路核心基因构建的深度学习模型准确预测了NSCLC和黑色素瘤的免疫治疗结果。衍生的NTLS评分被证明在预后分层方面有效，并在多个独立队列和癌症类型中得到了验证。本研究定义了一个由ICAM1-整合素和CCL5-CCR1相互作用驱动的致病性正反馈环路，N2中性粒细胞和Tex细胞通过该环路协同建立免疫抑制生态位，从而驱动免疫治疗耐药。我们基于这一分子回路开发的计算模型为患者分层提供了强大的工具，并具有显著的转化前景。

## Abstract
While neutrophils represent a prominent myeloid component in non-small cell lung cancer (NSCLC), the specific immunosuppressive functions of N2-polarized neutrophils and their mechanistic interactions with CD8⁺ T cells remain incompletely characterized. Furthermore, the development of clinically applicable models for prognostic stratification and immunotherapy response prediction, grounded in these molecular interactions, represents a critical unmet need. We integrated large-scale single-cell RNA sequencing datasets to delineate the tumor immune microenvironment, performing pathway enrichment and cell-cell communication analyses. Key molecular features derived from these interactions were employed to construct a deep neural network model. This model was trained and validated on bulk RNA sequencing cohorts to predict immunotherapy response. Additionally, we developed the N2_Neu-CD8⁺ Tex Loop Score (NTLS) for prognostic assessment and evaluated its pan-cancer applicability. Our analysis revealed a previously uncharacterized positive feedback loop between N2 neutrophils and exhausted CD8⁺ T cells (Tex). Neutrophil-derived ICAM1 engages with ITGAL/ITGB2 on CD8⁺ T cells, suppressing their NF-κB signaling and reinforcing the exhausted phenotype. In a feed-forward manner, Tex-derived CCL5 signals via CCR1 on N2 neutrophils, activating their NF-κB pathway and further upregulating ICAM1 expression. This ICAM1-Integrin and CCL5-CCR1 axis creates a self-sustaining immunosuppressive circuit. A deep learning model, built upon genes central to this loop, accurately predicted immunotherapy outcomes in NSCLC and melanoma. The derived NTLS score proved effective for prognostic stratification and was validated across multiple independent cohorts and cancer types. This study defines a pathogenic positive feedback loop, driven by ICAM1-Integrin and CCL5-CCR1 interactions, through which N2 neutrophils and Tex cells cooperatively establish an immunosuppressive niche that drives immunotherapy resistance. The computational models we developed, based on this molecular circuitry, offer robust tools for patient stratification and hold significant translational promise.