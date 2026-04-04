---
title: A diagnostic model based on pulmonary microbiota and host gene expression to distinguish colonization from pneumonia.
title_zh: 一种基于肺部微生物群和宿主基因表达的诊断模型，用于区分定植与肺炎
authors: "Zhangfan Fu, Yuhan Sun, Haijun Yao, Qihui Liu, Qiran Zhang, Jin Hu, Yang Zhou, Ning Jiang, Jingwen Ai, Jialin Jin, Wenhong Zhang"
date: 2026-04-03
pdf: "https://pubmed.ncbi.nlm.nih.gov/41933095/"
tags: ["query:pathoai"]
score: 9.0
evidence: 结合肺部微生物群和宿主基因表达的诊断模型
tldr: 针对临床上难以区分下呼吸道微生物定植与肺炎感染导致抗生素滥用的问题，本研究通过对神经外科ICU患者的深部痰液进行宏基因组（mNGS）和转录组测序，分析了肺部菌群特征与宿主免疫反应。研究发现感染组存在明显的菌群失调，而定植组则表现出上皮屏障维护相关的通路激活。最终构建了一个包含7个基因特征的多组学诊断模型，在验证集中达到0.875的AUC，为精准区分定植与感染提供了新工具。
selection_source: fresh_fetch
motivation: 临床上难以准确区分肺部微生物是单纯定植还是引起了肺炎，这常导致抗生素的过度使用和诊疗决策困难。
method: 结合宏基因组测序分析肺部菌群多样性，并利用转录组测序分析宿主免疫基因表达，构建基于7个关键基因的多组学诊断模型。
result: 发现感染组菌群多样性降低且致病菌活跃，而定植组激活了维持上皮屏障的信号通路，模型在验证集上实现了0.875的分类准确度。
conclusion: 整合肺部微生态与宿主转录组特征能有效识别真正的肺炎感染，为优化抗生素使用和精准诊断提供了分子生物学依据。
---

## 摘要
肺炎仍是全球死亡的主要原因之一。传统的诊断方法往往无法区分下呼吸道的微生物定植与真实感染，这增加了临床决策的难度，并导致了抗生素的过度使用。迫切需要改进诊断策略。在这项前瞻性单中心研究中，研究人员收集了华山医院神经外科重症监护室（ICU）收治的呼吸道定植患者（n = 17）和感染性肺炎患者（n = 27）的深部痰液样本。通过宏基因组二代测序（mNGS）和宏转录组分析，对肺部微生物群和宿主免疫反应进行了表征。随后整合这些特征构建了一个诊断模型。微生物群落分析显示，感染组的 alpha 多样性降低，且代谢活跃的致病分类群富集，这与允许入侵的失调状态一致。相比之下，定植组表现出更平衡的微生物生态系统。转录组分析在两组之间识别出 2232 个差异表达的宿主基因。定植组表现出 Wnt、MAPK、趋化因子和局灶粘附通路的显著激活，这些通路在功能上与上皮屏障维持和早期免疫稳态有关。一个包含七个基因特征（ANKRD52、ZC3HAV1L、SERPINE3、CDPF1、ZNF720、TAGLN3 和 LRRC15）的多组学诊断模型实现了对定植与感染的区分（训练集 AUC = 0.951；验证集 AUC = 0.875）。通过联合分析肺部微生物组和宿主转录组，本研究深入探讨了区分定植与感染的宿主-微生物相互作用，并提出了一个具有潜在临床意义的预测模型。

## Abstract
Pneumonia remains a leading cause of global mortality. Conventional diagnostic approaches frequently fail to distinguish microbial colonization from true infection in the lower respiratory tract, complicating clinical decision-making and contributing to antibiotic overuse. Improved diagnostic strategies are urgently needed. In this prospective, single-center study, deep sputum specimens were collected from patients with respiratory colonization (n = 17) and infectious pneumonia (n = 27) admitted to the neurosurgical ICU of Huashan Hospital. Metagenomic next-generation sequencing (mNGS) and metatranscriptomic profiling were performed to characterize both the pulmonary microbiota and the host immune response. These features were subsequently integrated to construct a diagnostic model. Microbial community profiling revealed reduced alpha diversity and enrichment of metabolically active pathogenic taxa in the infection group, consistent with a dysbiotic state permissive to invasion. In contrast, the colonization group demonstrated a more balanced microbial ecosystem. Transcriptomic analyses identified 2232 differentially expressed host genes between the two groups. The colonization group showed marked activation of the Wnt, MAPK, chemokine, and focal adhesion pathways, which are functionally implicated in epithelial barrier maintenance and early immune homeostasis. A multi-omics diagnostic model incorporating seven gene features (ANKRD52, ZC3HAV1L, SERPINE3, CDPF1, ZNF720, TAGLN3, and LRRC15) achieved a discrimination between colonization and infection (AUC = 0.951 in the training cohort; 0.875 in the validation set). By jointly analyzing the pulmonary microbiome and host transcriptome, this study provides insight into host-microbe interactions distinguishing colonization from infection and presents a predictive model with potential clinical relevance.