---
title: "MultiPert: An adversarial alignment and dual attention framework for single-cell multi-omics perturbation prediction."
title_zh: MultiPert：一种用于单细胞多组学扰动预测的对抗对齐与双重注意力框架
authors: "Mengyuan Zhao, Xinyue Tang, Jiawei Li, Cheng Liang, Jijun Tang, Fei Guo"
date: 2026-03-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/41811907/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于单细胞多组学扰动预测的深度学习框架
tldr: 准确预测细胞对扰动的反应对理解生物调控至关重要，但现有方法多局限于单模态转录组数据。MultiPert 是一种针对单细胞多组学设计的深度学习框架，通过模态特定编码器、双重注意力机制和对抗训练，实现了基因表达与蛋白质丰度的协同预测。在人类 THP-1 和肾脏数据集上的实验证明，该模型在预测精度和稳定性上优于现有方法，并能有效泛化至未知扰动，为揭示免疫调控机制和药物研发提供了强有力的工具。
selection_source: fresh_fetch
motivation: 现有的单细胞扰动预测方法大多仅处理转录组数据，难以捕捉多组学之间复杂的跨层分子效应。
method: 该框架结合了模态特定的预训练编码器、用于整合扰动信息的双重注意力机制，以及用于跨模态对齐的对抗训练技术。
result: 在多项基准测试中，MultiPert 对基因和蛋白质响应的预测准确度均超过了现有最先进方法，并成功识别出免疫相关的调控通路。
conclusion: MultiPert 扩展了多组学层面的扰动建模能力，为深入研究发病机制和加速药物筛选奠定了稳健的方法学基础。
---

## 摘要
准确预测扰动响应在系统生物学研究中至关重要，因为它在表征细胞身份和阐明生物通路的调节机制方面发挥着关键作用。现有的扰动响应预测方法主要局限于单模态转录组数据，限制了其捕捉跨层分子效应的能力。在此，我们提出了 MultiPert，这是一个专门为预测单细胞多组学数据中的扰动响应而设计的深度学习框架。MultiPert 采用具有专门预训练的模态特定编码器，通过双重注意力机制整合扰动，并通过对抗训练实现跨模态对齐。在人类 THP-1 和肾脏多组学数据集上的基准测试表明，MultiPert 能够可靠地预测受扰动的基因表达和蛋白质丰度谱，与现有最先进策略相比，实现了更高的准确性和稳定性。MultiPert 可以泛化到未见过的扰动，并基于受扰动的蛋白质组预测揭示免疫检查点分子的调节机制。此外，受扰动转录组预测的富集分析揭示了免疫相关通路。通过提供一个集成且可解释的框架，MultiPert 扩展了多组学层面的扰动建模范围，从而为发病机制和药物发现的全面研究提供了坚实的方法学基础。

## Abstract
Precise prediction of perturbation responses is essential in systems biology research, as it plays a pivotal role in characterizing cellular identities and elucidating the regulatory mechanisms of biological pathways. Existing perturbation-responses prediction approaches are predominantly confined to single-modality transcriptomic data, limiting their capacity to capture cross-layer molecular effects. Here, we present MultiPert, a deep learning framework specifically designed for predicting perturbation responses in single-cell multi-omics data. MultiPert employs modality-specific encoders with dedicated pretraining, integrates perturbation through a dual-attention mechanism, and achieves cross-modal alignment via adversarial training. Benchmarking on human THP-1 and kidney multi-omics datasets demonstrates that MultiPert reliably predicts both perturbed gene expression and protein abundance profiles, achieving superior accuracy and stability compared to state-of-the-art strategies. MultiPert generalizes to unseen perturbations and uncovers regulatory mechanisms of immune checkpoint molecules based on perturbed proteomic predictions. In addition, enrichment analyzes of perturbed transcriptomic predictions reveal immune-related pathways. By providing an integrated and interpretable framework, MultiPert expands the scope of perturbation modeling at the multi-omics level, thereby offering a robust methodological foundation for comprehensive research into pathogenesis and drug discovery.