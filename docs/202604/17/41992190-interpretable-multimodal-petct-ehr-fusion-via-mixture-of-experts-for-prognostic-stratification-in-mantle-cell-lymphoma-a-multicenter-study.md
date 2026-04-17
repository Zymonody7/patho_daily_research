---
title: "Interpretable multimodal PET/CT-EHR fusion via mixture-of-experts for prognostic stratification in mantle cell lymphoma: a multicenter study."
title_zh: 基于混合专家模型的可解释多模态 PET/CT-EHR 融合用于套细胞淋巴瘤的预后分层：一项多中心研究
authors: "Chong Jiang, Zitong Zhang, Zekun Jiang, Chongyang Ding, Yue Teng, Limin Gao, Ming Jiang, Linhao Qu, Rong Tian"
date: 2026-04-16
pdf: "https://pubmed.ncbi.nlm.nih.gov/41992190/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 整合影像和电子健康档案数据的多模态深度学习
tldr: 针对套细胞淋巴瘤（MCL）生物学异质性强、传统预后工具准确性不足的问题，本研究开发了一种基于混合专家模型（MoE）的多模态融合框架。该框架通过注意力门控机制，深度整合了患者基线PET/CT影像视觉特征、影像组学特征以及电子健康记录（EHR）的文本表征。实验结果显示，该模型在预测无进展生存期和总生存期方面显著优于传统临床指标，并能通过注意力图谱提供病理相关的可解释性，为MCL的精准风险分层提供了非侵入性工具。
selection_source: fresh_fetch
motivation: 旨在解决套细胞淋巴瘤预后评估中因生物学异质性导致现有工具预测效能受限的临床难题。
method: 提出一种混合专家（MoE）融合网络，利用注意力门控机制协同视觉编码器、影像组学提取器和医学语言模型，实现PET/CT影像与EHR数据的深度表征融合。
result: 多模态特征（R-signatures）在预测复发和死亡风险上表现出极高的区分度（AUC最高达0.893），且在多中心验证中显著超越了常规临床预后指数。
conclusion: 该研究证明了多模态深度学习融合框架能显著提升淋巴瘤预后预测的精度，并具备良好的临床转化潜力与生物学解释性。
---

## 摘要
背景：套细胞淋巴瘤（MCL）是一种罕见的、具有生物学异质性的 B 细胞恶性肿瘤，其预后差异极大。现有的预后评估工具尚不理想。我们开发了一个可解释的深度学习框架，整合了基线 [18F]FDG PET/CT 和电子健康记录（EHR）数据，用于个体化风险分层。方法：在这项多中心研究中，分析了 187 名初治 MCL 患者。采用混合专家（MoE）融合网络整合了来自 PET/CT 和 EHR 数据的多模态表征。通过基于注意力的门控机制，将包含视觉编码器、影像组学提取器和医学语言模型的专家模块进行集成，构建了用于预测无进展生存期（PFS）和总生存期（OS）的多模态影像组学特征（R-signatures）。对 R-signatures 进行了验证，并将其与临床及代谢因素共同纳入多参数模型。通过注意力可视化、专家级贡献度和病理相关性评估了深度学习模型的可解释性。结果：R-signatures 能够稳健地识别复发（训练集 AUC = 0.893，验证集 0.755）和死亡（AUC 分别为 0.804 和 0.844），并能独立预测不良预后（PFS：HR = 27.70，P < 0.001；OS：HR = 6.86，P = 0.001）。整合了 R-signatures 与总病灶糖酵解、β2-微球蛋白、白细胞计数（WBC）和 Ki-67 的多参数模型表现优于传统指标（C 指数：PFS 训练集 0.892，验证集 0.781；OS 训练集 0.877，验证集 0.862）。随时间变化的 ROC 分析一致显示 AUC 接近或超过 0.800。校准曲线和决策曲线分析证实了良好的吻合度和卓越的临床净获益。注意力图将高权重区域定位在肿瘤高代谢区域，且母细胞型和多形性变异型的 R-signature 值高于经典组织学类型（P = 0.028 和 P = 0.010）。结论：这种可解释的 PET/CT-EHR 融合框架显著提高了 MCL 的预后预测精度，为风险适应性管理提供了一种无创且具有临床转化价值的工具。

## Abstract
BACKGROUND: Mantle cell lymphoma (MCL) is a rare, biologically heterogeneous B-cell malignancy with highly variable outcomes. Existing prognostic tools are suboptimal. We developed an interpretable deep learning framework integrating baseline [18F]FDG PET/CT and electronic health record (EHR) data for individualized risk stratification. METHODS: In this multicenter study, 187 treatment-naïve MCL patients were analyzed. A mixture-of-experts (MoE) fusion network integrated multimodal representations from PET/CT and EHR data. Expert modules comprising vision encoders, radiomics extractors, and a medical language model were integrated through an attention-based gating mechanism to construct multimodal radiomic signatures (R-signatures) predictive of progression-free survival (PFS) and overall survival (OS). R-signatures were validated and incorporated with clinical and metabolic factors into multiparametric models. Deep learning model interpretability was evaluated using attention visualization, expert-level contributions and pathologic correlation. RESULTS: R-signatures robustly discriminated relapse (AUC = 0.893 training, 0.755 validation) and death (AUC = 0.804 and 0.844), and independently predicted adverse outcomes (PFS: HR = 27.70, P < 0.001; OS: HR = 6.86, P = 0.001). Multiparametric models integrating R-signatures with total lesion glycolysis, β2-microglobulin, WBC, and Ki-67 outperformed conventional indices (C-indices: PFS 0.892 training, 0.781 validation; OS 0.877 training, 0.862 validation). Time-dependent ROC analyses consistently showed AUCs approaching or exceeding 0.800. Calibration and decision curve analyses confirmed excellent agreement and superior clinical net benefit. Attention maps localized high-weighted regions to hypermetabolic tumor areas, with higher R-signature values in blastoid and pleomorphic variants versus classical histology (P = 0.028 and P = 0.010). CONCLUSIONS: This interpretable PET/CT-EHR fusion framework substantially improves prognostic precision in MCL, providing a noninvasive, clinically translatable tool for risk-adapted management.