---
title: Integrative lipidomics profiles and explainable machine learning for species-specific identification of meat and bone meal.
title_zh: 综合脂质组学谱图与可解释机器学习用于肉骨粉的物种特异性鉴定
authors: "Bing Gao, Zhichao Yang, Jiabin Zheng, Haitao Yu, Xin Wang, Gangshan Wu, Hao Liang"
date: 2026-05-10
pdf: "https://pubmed.ncbi.nlm.nih.gov/41830763/"
tags: ["query:pathoai"]
score: 6.0
evidence: 用于物种识别的可解释机器学习以防止朊病毒传播
tldr: "为防止动物饲料中同物种循环利用引发的疯牛病等风险，本研究针对肉骨粉（MBM）物种鉴定难题，首次结合非靶向脂质组学与可解释机器学习技术。通过分析76份样本中的4180种脂质分子，筛选出46个关键生物标志物，并利用支持向量机实现了100%的分类准确率。该方法结合SHAP分析揭示了核心判别分子，为肉骨粉的精准溯源提供了科学依据。"
selection_source: fresh_fetch
motivation: 为了防止因动物饲料中同物种循环利用导致的疯牛病传播，需要一种精准的肉骨粉物种鉴定方法。
method: 采用非靶向脂质组学技术对4180种脂质进行分析，并结合支持向量机（SVM）算法与SHAP可解释性框架构建物种分类模型。
result: 0)等关键贡献分子。
conclusion: 脂质组学特征与可解释机器学习的结合，为肉骨粉的物种溯源和饲料安全监管提供了一套高效且透明的分析框架。
---

## 摘要
在许多司法管辖区，准确鉴定肉骨粉（MBM）的物种来源是一项监管要求，旨在防止动物饲料中的同物种循环（同类相食）。这种做法会促进牛海绵状脑病通过受朊病毒污染的饲料进行传播。本研究首次全面应用非靶向脂质组学方法，系统地表征了来自四个物种的76份MBM样本的脂质组成谱图。共鉴定出4180个脂质分子，分为43个脂质亚类。通过严格的评估标准（P < 0.05, VIP > 1.00, FC > 1.50 或 FC < 0.67），成功筛选出46个具有高度物种特异性的脂质生物标志物。利用这些差异脂质的丰度谱图，我们使用多种机器学习算法建立了优化的物种鉴定模型。支持向量机模型表现出卓越的性能，分类准确率达到100%。随后的SHapley加性解释（SHAP）分析显示，TG(44:0)、TG(49:0)和Cer(t41:1)这三个脂质分子对物种区分的贡献最为显著。所开发的分析框架结合了脂质组学谱图与可解释机器学习，为MBM的精确物种鉴定奠定了科学基础。

## Abstract
Accurate species identification of meat and bone meal (MBM) is a regulatory requirement in many jurisdictions to prevent intra-species recycling (cannibalism) in animal feed. It is a practice that facilitates transmission of bovine spongiform encephalopathy via prion-contaminated feed. This study represents the first comprehensive application of nontarget lipidomics method to systematically characterize the lipid composition profiles across 76 MBM samples from four species. A total of 4180 lipid molecules were identified, classified into 43 lipid subclasses. Through rigorous evaluation criteria (P < 0.05, VIP>1.00, FC>1.50 or FC<0.67), 46 highly species-specific lipid biomarkers were successfully screened. Leveraging the abundance profiles of these discriminative lipids, we established optimized species identification models using multiple machine learning algorithms. The support vector machine model demonstrated superior performance with 100% classification accuracy. Subsequent SHapley Additive exPlanations analysis revealed that three lipid molecules, TG(44:0), TG(49:0), and Cer(t41:1), contributed most significantly to species differentiation. The developed analytical framework, combining lipidomics profiles with explainable machine learning, establishes a scientific foundation for precise species identification in MBM.