---
title: Quantitative Analysis of Multiple Serum Tumor Biomarkers by an Interpretable Stacked Ensemble Model.
title_zh: 基于可解释堆叠集成模型的多种血清肿瘤生物标志物定量分析
authors: "Boyu Wu, Jiawei Chen, Yanheng Huang, Pan Li, Qingmei Deng, Ronglu Dong, Liangbao Yang"
date: 2026-04-20
pdf: "https://pubmed.ncbi.nlm.nih.gov/42010926/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 用于生物标志物检测的可解释堆叠集成模型
tldr: "针对血清肿瘤标志物在表面增强拉曼光谱（SERS）检测中面临的光谱复杂和基质干扰问题，本研究提出了一种可解释堆叠集成模型（ISEM）。该模型结合了LASSO特征选择与集成学习算法，实现了对12种血清肿瘤标志物的高精度定量分析（R2 > 0.9），并通过SHAP解释性分析揭示了分子结构与光谱特征的关联，为癌症早期筛查提供了可靠且透明的数字化工具。"
selection_source: fresh_fetch
motivation: 现有的SERS生物标志物定量分析受限于光谱重叠和基质干扰，且缺乏模型的可解释性与泛化能力。
method: 提出了一种集成LASSO特征选择、堆叠集成学习（Stacked Ensemble）和SHAP解释性分析的计算框架。
result: 成功实现了12种血清肿瘤标志物的定量预测，所有指标的决定系数（R2）均超过0.9，并揭示了糖基化等因素对预测的影响。
conclusion: 该研究建立了一个兼具高精度与透明度的生物标志物定量分析框架，显著提升了SERS技术在复杂生物样本检测中的应用潜力。
---

## 摘要
表面增强拉曼光谱 (SERS) 在生物分子检测中具有极高的灵敏度和特异性，特别是在分析血清肿瘤生物标志物方面。然而，其应用受到光谱复杂性和基质干扰的限制。尽管机器学习 (ML) 在 SERS 数据分析中展现出应用前景，但现有的生物标志物检测定量模型仍缺乏泛化性和可解释性。为应对这些挑战，我们开发了一种可解释堆叠集成模型 (ISEM)，该模型集成了特征选择、集成学习和可解释人工智能 (XAI)，用于定量分析 12 种血清肿瘤生物标志物。为确保定量分析的可靠性，我们利用均匀且可重复的金 (Au) 纳米颗粒基底对获取的 SERS 数据进行了验证。采用预处理和最小绝对收缩与选择算子 (LASSO) 特征选择，为准确定量奠定了基础。随后，对 12 种血清肿瘤生物标志物进行了定量，结果表明 ISEM 具有优异的性能，所有标志物的预测准确度 R² 值均超过 0.9。至关重要的是，基于定量结果，我们利用 Shapley 加性解释 (SHAP) 提供了结构-光谱相关性的分子级可解释性，揭示了糖基化反应、基质干扰和光谱重叠如何影响预测准确性。此外，通过泛化性验证，证实了 ISEM 在未知样本中定量多种生物标志物的能力。本研究为复杂生物基质中的生物标志物定量分析建立了一个集成驱动的可解释框架，展示了在癌症早期诊断和筛查方面的巨大潜力。

## Abstract
Surface-enhanced Raman spectroscopy (SERS) offers exceptional sensitivity and specificity for biomolecular detection, particularly in analyzing serum tumor biomarkers. However, its application is hindered by spectral complexity and matrix interference. Although machine learning (ML) has shown promise in SERS data analysis, existing quantitative models for biomarker detection lack generalizability and interpretability. To address these challenges, we developed an interpretable stacked ensemble model (ISEM) that integrates feature selection, ensemble learning, and explainable artificial intelligence (XAI) for quantifying 12 serum tumor biomarkers. To ensure reliable quantitative analysis, we validated the acquired SERS data using uniform and reproducible Au nanoparticle substrates. Preprocessing, least absolute shrinkage, and selection operator (LASSO) feature selection were employed to establish a foundation for accurate quantification. Subsequently, 12 serum tumor biomarkers were quantified, demonstrating the superior performance of ISEM, which achieved a high predictive accuracy, with R2 values exceeding 0.9 for all biomarkers. Crucially, based on the quantitative results, we provided molecular-level interpretability for structure-spectrum correlations using Shapley additive explanations (SHAP), revealing how glycosylation reactions, matrix interference, and spectral overlap influence prediction accuracy. Furthermore, the capability of ISEM to quantify multiple biomarkers in unseen samples was confirmed through validation of its generalizability. Our study establishes an ensemble-driven, interpretable framework for quantitative biomarker analysis in a complex biological matrix, demonstrating significant potential for early cancer diagnosis and screening.