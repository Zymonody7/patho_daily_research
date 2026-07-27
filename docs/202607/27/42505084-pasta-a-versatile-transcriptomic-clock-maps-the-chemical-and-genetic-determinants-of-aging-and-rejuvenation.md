---
title: "Pasta, a Versatile Transcriptomic Clock, Maps the Chemical and Genetic Determinants of Aging and Rejuvenation."
title_zh: Pasta：一种通用的转录组时钟，揭示了衰老与回春的化学和遗传决定因素
authors: "Jérôme Salignon, Maria Tsiokou, Patricia Marqués, Enriqueta Rodríguez-Diaz, Hazel Ang, Federico Pietrocola, Christian G Riedel"
date: 2026-07-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/42505084/"
tags: ["query:seqai"]
score: 7.0
evidence: 利用RNA-Seq数据的转录组衰老时钟
tldr: 针对转录组衰老时钟受限于平台和组织特异性的问题，研究者开发了名为 Pasta 的通用型人类衰老时钟。该工具采用“年龄偏移”学习框架，能跨组织、跨平台准确预测生物年龄。通过对三百万个转录组样本的大规模筛选，Pasta 揭示了线粒体翻译和 mRNA 剪接在衰老与回春中的关键作用，并实验验证了相关调控药物，为抗衰老研究提供了高效的数字化工具。
selection_source: fresh_fetch
motivation: 现有的转录组衰老预测工具往往依赖特定检测平台或组织类型，难以在多样化的生物医学数据中实现通用化应用。
method: 开发了一种基于“年龄偏移”学习框架的 Pasta 模型，使其能够兼容大体转录组、单细胞测序和微阵列等多种异构数据源。
result: 模型在大规模筛选中发现线粒体翻译和 mRNA 剪接分别是驱动衰老与回春的关键因素，并验证了 pralatrexate 等药物的调控效果。
conclusion: Pasta 证明了其作为大规模筛选衰老干预手段的有效性，为识别抗衰老药物和理解衰老生物学机制提供了通用的计算框架。
---

## 摘要
随着年龄相关疾病负担的日益加重，理解和调节衰老过程已成为当务之急。转录组衰老时钟 (TACs) 可以追踪生物学年龄，但仍受限于平台依赖性、组织特异性或有限的可访问性。为解决这一问题，我们开发了 Pasta，这是一种稳健且广泛适用的人类 TAC，基于一种新型的“年龄偏移” (age-shift) 学习框架构建。Pasta 准确预测了包括大块 (bulk) 和单细胞 RNA-Seq 以及微阵列数据在内的多种组织和数据类型的相对年龄。其预测结果与衰老和干细胞样细胞状态一致，并依赖于富集在 p53 和 DNA 损伤反应通路中的模型系数。Pasta 的年龄评分与几种癌症类型的肿瘤分级和患者生存率相关，表明其具有潜在的临床相关性。应用于 Connectivity Map L1000 数据集中的 300 多万个转录组，Pasta 识别出了已知的和先前未被认识的衰老调节化合物及遗传扰动，强调了线粒体翻译和 mRNA 剪接分别是细胞衰老和回春倾向的关键决定因素。实验验证证实，普拉曲沙 (pralatrexate) 是人类细胞中强效的衰老诱导剂，而荜茇宁 (piperlongumine) 则是回春剂。总之，这些发现确立了 Pasta 作为衰老研究和药物发现中一种通用且易于获取的工具。

## Abstract
With the growing burden of age-related diseases, understanding and modulating the aging process has become a priority. Transcriptomic aging clocks (TACs) can track biological age but remain limited by platform dependence, tissue specificity, or restricted accessibility. To address this, we developed Pasta, a robust and broadly applicable human TAC, built using a novel 'age-shift' learning framework. Pasta accurately predicted relative age across diverse tissues and data types, including bulk and single-cell RNA-Seq as well as microarray data. Its predictions aligned with senescent and stem-like cellular states and relied on model coefficients enriched for p53 and DNA damage response pathways. Pasta's age scores correlated with tumor grade and patient survival in several cancer types, indicating potential clinical relevance. Applied to over three million transcriptomes from the Connectivity Map L1000 dataset, Pasta identified both established and previously unrecognized age-modulatory compounds and genetic perturbations, highlighting mitochondrial translation and mRNA splicing as key determinants of cellular propensity for aging and rejuvenation, respectively. Experimental validation confirmed pralatrexate as a potent senescence inducer and piperlongumine as a rejuvenating agent in human cells. Together, these findings establish Pasta as a versatile and accessible tool for aging research and therapeutic discovery.