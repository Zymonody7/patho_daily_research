---
title: Multimodal interpretable deep learning for transcriptome-informed precision oncology and drug mechanism analysis.
title_zh: 用于转录组指导的精准肿瘤学和药物机制分析的多模态可解释深度学习
authors: "Ning Qu, Xiaochu Tong, Zhaokun Wang, Panpan Shao, Lehan Zhang, Xiaoya Zhang, Yuxin Xing, Jin Liu, Yitian Wang, Sulin Zhang, Mingyue Zheng, Xutong Li"
date: 2026-05-13
pdf: "https://pubmed.ncbi.nlm.nih.gov/42129298/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 用于多组学整合和药物敏感性的多模态深度学习
tldr: 针对精准肿瘤学中药物反应预测难、机制解释性差的问题，本文提出了 BioGDR 框架。该框架通过整合基于结构的预测生物特征（如差异基因表达和激酶抑制谱），利用通路感知的图神经网络和药物引导注意力机制，实现了无需实验测量即可预测药物敏感性。实验证明其在化合物筛选和临床队列预测中优于现有方法，并成功验证了新型抑制剂的作用机制，为药物研发到临床应用提供了可解释的桥梁。
selection_source: fresh_fetch
motivation: 现有的精准医疗方法在解释复杂细胞信号和跨异质环境预测药物反应方面存在困难，且往往依赖昂贵的实验测量。
method: 开发了名为 BioGDR 的多模态深度学习框架，利用图神经网络建模生物通路，并结合药物引导的注意力机制来整合预测的转录组和激酶抑制特征。
result: 该模型在早期药物筛选和异质细胞系敏感性预测任务中表现优于现有方法，并在临床患者数据和新型 ALDH1B1 抑制剂的实验验证中展现了良好的泛化能力。
conclusion: BioGDR 通过整合多模态生物信息和可解释性分析，为连接临床前药物开发与临床精准用药提供了一个稳健的计算框架。
---

## 摘要
精准肿瘤学在解释复杂的细胞信号和预测异质性癌症环境中的药物反应方面面临着严峻挑战。在此，我们提出了 BioGDR，这是一个多模态可解释深度学习框架，它整合了基于结构的预测生物学特征（包括差异基因表达和激酶抑制谱），从而消除了对实验测量的需求。通过利用通路信息的图神经网络对肿瘤转录组状态进行建模，并采用药物引导的注意力策略，BioGDR 能够深入洞察化合物和细胞背景下的药物敏感性机制。全面评估表明，BioGDR 在与早期药物发现相关的化合物筛选以及预测精准肿瘤学特征的异质细胞状态下的细胞系敏感性方面优于现有方法，而对临床患者队列的分析进一步证实了其实用价值和泛化能力。对一种新型 ALDH1B1 抑制剂的实验验证证实了其识别敏感细胞群并揭示潜在机制的能力。这项工作建立了一个稳健的、具有生物学信息的框架，桥接了临床前药物开发和临床应用，通过综合的多模态学习和可解释的机制分析推动了精准肿瘤学的发展。

## Abstract
Precision oncology faces critical challenges in interpreting complex cellular signals and predicting drug responses across heterogeneous cancer environments. Here, we present BioGDR, a multimodal interpretable deep learning framework that integrates structure-based predicted biological features, including differential gene expression and kinase inhibition profiles, eliminating the need for experimental measurements. By modeling tumor transcriptomic states through pathway-informed graph neural networks and employing a drug-guided attention strategy, BioGDR enables mechanistic insights into drug sensitivity across compound and cellular contexts. Comprehensive evaluations demonstrate that BioGDR outperforms existing methods in compound screening relevant to early-stage drug discovery and in predicting cell line sensitivity across heterogeneous cellular states characteristic of precision oncology, while analyses on clinical patient cohorts further confirm its practical utility and generalization capability. Experimental validation with a novel ALDH1B1 inhibitor confirms its ability to identify sensitive cell populations and reveal underlying mechanisms. This work establishes a robust, biologically informed framework that bridges preclinical drug development and clinical applications, advancing precision oncology through integrative, multimodal learning and interpretable mechanism analysis.