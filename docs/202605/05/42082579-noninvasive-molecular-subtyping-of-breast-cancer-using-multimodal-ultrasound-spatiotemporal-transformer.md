---
title: Noninvasive molecular subtyping of breast cancer using multimodal ultrasound spatiotemporal transformer.
title_zh: 利用多模态超声时空 Transformer 进行乳腺癌非侵入性分子分型
authors: "Tao Chen, Qinghua Niu, Zichen An, Chenhui Wang, Zhihao Chen, Lianfang Du, Chao Jia, Chunxiao Li, Jiying Gu, Ting Sun, Yuxiang Wang, Fan Li, Hongming Shan"
date: 2026-05-04
pdf: "https://pubmed.ncbi.nlm.nih.gov/42082579/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 利用超声和血流动力学的多模态 Transformer 进行癌症分型
tldr: 乳腺癌分子分型对制定治疗方案至关重要，但目前依赖有创活检，且常规超声缺乏反映肿瘤生物学特征的动态信息。本研究开发了MUST-Sub模型，利用时空Transformer架构融合静态B超形态与造影超声血流动力学特征，在多中心验证中实现了最高0.94的分类AUC。该方法不仅在性能上优于单模态模型，还提取出与肿瘤增殖指数相关的可解释生物标志物，为无创术前分型提供了新工具。
selection_source: fresh_fetch
motivation: 针对目前乳腺癌分子分型依赖有创活检且常规超声难以捕捉肿瘤动态生物学特征的问题，探索无创的影像学替代方案。
method: 提出一种名为MUST-Sub的时空Transformer模型，通过整合配对的B超形态特征与对比增强超声的血流动力学模式进行多模态学习。
result: 该模型在内部及多中心外部验证集上对乳腺癌分型的平均AUC达到0.90至0.94，且其生成的影像标志物与肿瘤大小及Ki-67增殖指数显著相关。
conclusion: 结合时空建模的多模态超声技术能够有效识别乳腺癌分子亚型，可作为临床术前无创评估肿瘤生物学特性的辅助手段。
---

## 摘要
分子分型对于指导乳腺癌的全身治疗至关重要，但目前需要进行侵入性活检。传统的 B 型超声提供了丰富的解剖信息，但缺乏捕捉肿瘤全面生物学特征所需的功能动力学信息。在此，我们提出了首个多模态超声时空 Transformer 模型 MUST-Sub，该模型整合了配对的 B 型超声形态特征与超声造影（CEUS）血流动力学模式，用于对 Luminal 型、HER2 阳性型和三阴性亚型进行分类。MUST-Sub 在回顾性开发队列上进行训练，并在内部、前瞻性和多中心外部队列上进行了验证，其宏平均受试者工作特征曲线下面积（AUC）分别达到 0.94、0.90 和 0.92，Luminal 型与非 Luminal 型分类的 AUC 分别为 0.92、0.88 和 0.91，优于仅基于 B 型超声的深度学习基准模型。MUST-Sub 还生成了源自时空注意力的可解释定量生物标志物：形态相关生物标志物与肿瘤大小呈负相关（Spearman ρ = [-0.34, -0.23]；均 p < 0.05），而血流动力学相关生物标志物与肿瘤大小（ρ = [0.24, 0.32]；均 p < 0.05）及 Ki-67 增殖指数（ρ = [0.21, 0.24]；均 p < 0.05）呈正相关。这些结果表明，结合时空建模的多模态超声可作为一种极具前景的辅助方法，用于乳腺癌活检前的非侵入性分子表型分析。

## Abstract
Molecular subtyping is essential for guiding systemic therapy in breast cancer but currently requires invasive biopsy. Conventional B-mode ultrasound offers rich anatomical information, yet lacks the functional dynamics needed to capture the comprehensive biology of tumors. Here, we present the first multimodal ultrasound spatiotemporal transformer, MUST-Sub, which integrates paired B-mode morphological features with contrast-enhanced ultrasound (CEUS) hemodynamic patterns to classify Luminal, HER2-enriched, and triple-negative subtypes. Training on a retrospective development cohort, and validated on internal, prospective, and multicenter external cohorts, MUST-Sub achieved macro-average areas under the receiver operating characteristic curve (AUCs) of 0.94, 0.90, and 0.92, respectively, and Luminal versus non-Luminal AUCs of 0.92, 0.88, and 0.91, outperforming B-mode-only deep learning baselines. MUST-Sub also produced interpretable quantitative biomarkers derived from spatiotemporal attention: the morphology-associated biomarker showed inverse correlations with tumor size (Spearman ρ = [- 0.34, - 0.23]; all p < . 05), while the hemodynamics-associated biomarker correlated positively with tumor size (ρ = [0.24, 0.32]; all p < . 05) and Ki-67 proliferation index (ρ = [0.21, 0.24]; all p < . 05). These results suggest that multimodal ultrasound with spatiotemporal modeling can serve as a promising adjunctive approach for non-invasive pre-biopsy molecular phenotyping of breast cancer.