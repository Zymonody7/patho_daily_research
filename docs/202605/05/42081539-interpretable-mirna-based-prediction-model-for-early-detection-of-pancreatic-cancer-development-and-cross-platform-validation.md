---
title: "Interpretable miRNA-based prediction model for early detection of pancreatic cancer: Development and cross-platform validation."
title_zh: 基于 miRNA 的胰腺癌早期检测可解释预测模型：开发与跨平台验证
authors: "Yanfei Zhu, Linglin Zhu, Yumei Liu, Yongshuo Ji, Junqiu Zhu, Hong Zhao"
date: 2026-01-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/42081539/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 基于 miRNA 的可解释癌症检测诊断模型
tldr: 针对胰腺癌早期诊断困难且现有miRNA标志物缺乏跨平台验证的问题，本研究利用801个样本构建了一个基于20个miRNA特征的随机森林诊断模型。通过引入SHAP分析增强模型可解释性，该模型在训练集和多个独立外部验证集（涵盖RNA-seq和qRT-PCR平台）中均表现出稳定的诊断效能（AUC 0.78-0.87），为胰腺癌的早期筛查提供了一个具备跨平台鲁棒性和透明度的数字化方案。
selection_source: fresh_fetch
motivation: 旨在解决胰腺癌早期诊断标志物在不同检测平台间表现不一致以及预测模型缺乏临床可解释性的痛点。
method: 基于801例多中心样本数据，采用随机森林算法构建20-miRNA签名模型，并利用SHAP归因分析量化各生物标志物对诊断决策的贡献度。
result: 模型在训练集交叉验证中AUC达0.87，在独立外部验证集中AUC稳定在0.78至0.83之间，并成功识别出miR-6875-5p等关键致癌相关因子。
conclusion: 该研究通过结构化的跨平台验证证明了20-miRNA签名在胰腺癌早期诊断中的可靠性，为未来临床转化提供了可解释的建模框架。
---

## 摘要
背景：胰腺癌仍然是最致命的恶性肿瘤之一，这在很大程度上归因于诊断延迟。尽管微小 RNA (miRNA) 生物标志物展现出应用前景，但许多先前的研究缺乏跨平台验证和模型可解释性，限制了其临床适用性。方法：我们利用公开数据集开发并外部验证了一个基于 20-miRNA 特征的可解释诊断模型。共纳入 801 个样本，其中 767 个用于模型训练和验证。训练队列包括 GSE59856 和 GSE85589 (n = 216)，独立验证队列包括 TCGA-PAAD 和 GTEx 胰腺数据 (n = 585)，此外还进行了基于血清的验证 (GSE128508; n = 30)。特征选择和模型开发仅在训练队列中进行。应用了随机森林分类器，并使用 SHAP 分析评估了模型的可解释性。通过交叉验证和独立外部验证评估了诊断性能。结果：该模型在训练队列中实现了 0.87 (95% CI 0.82-0.92) 的交叉验证 AUC，灵敏度为 84.7%，特异性为 83.1%。在独立 RNA-seq 和 qRT-PCR 数据集的外部验证中，AUC 值在 0.78 到 0.83 之间。不同样本类型和平台的性能保持大致一致。SHAP 分析确定 miR-6875-5p、miR-196a-5p 和 miR-1246 是分类的主要贡献者。功能富集分析表明其参与了经典的癌症相关通路。结论：我们开发并外部验证了一个用于胰腺癌诊断的可解释 20-miRNA 特征，该特征在独立队列中表现出一致的性能。尽管基于回顾性数据集，但结构化的验证策略和可解释的建模框架为未来的前瞻性评估提供了透明的基础。

## Abstract
BACKGROUND: Pancreatic cancer remains one of the most lethal malignancies, largely due to delayed diagnosis. Although microRNA (miRNA) biomarkers show promise, many previous studies lack cross-platform validation and model interpretability, limiting clinical applicability. METHODS: We developed and externally validated an interpretable diagnostic model based on a 20-miRNA signature using publicly available datasets. A total of 801 samples were included, of which 767 were used for model training and validation. The training cohort comprised GSE59856 and GSE85589 (n = 216), and independent validation cohorts included TCGA-PAAD and GTEx pancreas (n = 585), with additional serum-based validation (GSE128508; n = 30). Feature selection and model development were conducted exclusively within the training cohort. A Random Forest classifier was applied, and model interpretability was assessed using SHAP analysis. Diagnostic performance was evaluated using cross-validation and independent external validation. RESULTS: The model achieved a cross-validation AUC of 0.87 (95% CI 0.82-0.92), with sensitivity of 84.7% and specificity of 83.1% in the training cohort. External validation across independent RNA-seq and qRT-PCR datasets demonstrated AUC values ranging from 0.78 to 0.83. Performance remained broadly consistent across sample types and platforms. SHAP analysis identified miR-6875-5p, miR-196a-5p, and miR-1246 among the principal contributors to classification. Functional enrichment analysis suggested involvement in canonical cancer-related pathways. CONCLUSIONS: We developed and externally validated an interpretable 20-miRNA signature for pancreatic cancer diagnosis with consistent performance across independent cohorts. Although based on retrospective datasets, the structured validation strategy and explainable modeling framework provide a transparent foundation for future prospective evaluation.