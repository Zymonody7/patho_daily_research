---
title: Contrastive multimodal deep learning for survival prediction in grade 2/3 gliomas.
title_zh: 对比多模态深度学习用于 2/3 级胶质瘤的生存预测
authors: "Peiying Hua, Chun-Chieh Lin, Travis Fenlon, Xiaoying Liu, Saeed Hassanpour"
date: 2026-04-15
pdf: "https://pubmed.ncbi.nlm.nih.gov/41987576/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 整合组织病理学和体细胞突变的多模态深度学习
tldr: 针对2/3级胶质瘤生存预测中因肿瘤异质性导致单模态数据预测不准的问题，该研究提出了一种对比多模态深度学习框架。该框架整合了病理全切片图像、体细胞突变和临床数据，通过三阶段训练流程对齐跨模态表征并优化生存分析目标。实验结果显示，该模型在TCGA数据集上达到0.91的C-index，显著优于单模态模型，并在外部验证集上表现稳健，为临床个性化治疗和风险分层提供了高效的自动化工具。
selection_source: fresh_fetch
motivation: 传统的2/3级胶质瘤生存预测依赖单一模态数据，难以捕捉肿瘤复杂的生物学异质性，导致预测准确度受限。
method: 提出一种三阶段训练的对比学习框架，通过对齐病理图像、基因突变和临床特征的表征空间，实现多源异构数据的深度融合与生存预测优化。
result: 该模型在内部验证中取得0.91的C-index，显著优于纯图像或纯临床基因模型，且对比学习显著提升了特征聚类质量和跨中心验证的泛化能力。
conclusion: 对比多模态学习能有效整合常规临床数据以提升胶质瘤预后评估精度，证明了跨模态表征对齐在辅助临床决策和患者风险分层中的应用潜力。
---

## 摘要
背景：由于肿瘤的生物学异质性以及当前依赖单模态数据的预后评估方法的局限性，2/3 级胶质瘤患者的准确生存预测仍具挑战性。方法：我们开发了一个整合了组织病理学全切片图像、体细胞突变和临床人口统计学数据的多模态深度学习框架。一个三阶段训练流水线将对比学习与生存特异性优化相结合，以对齐跨模态表示。该框架在来自 TCGA 的 498 名 2/3 级胶质瘤患者数据上进行了训练，并使用 5 折交叉验证和独立的达特茅斯-希区柯克医学中心 (DHMC) 队列 (n = 61) 进行了评估。结果：对比多模态模型实现了 0.91 的 C 指数 (95% CI: 0.84 至 0.96)，显著优于单模态模型（仅图像 = 0.76；仅非图像 = 0.87），并显示出优于非对比多模态模型 (C 指数 = 0.89) 的改进，尽管这一差异在统计学上并不显著。Kaplan-Meier 分析显示不同风险层级之间具有明显的生存差异 (log-rank P = 4.4 × 10^-5)。对比学习提高了表示聚类的质量，轮廓系数从 0.20 增加到 0.24 (P = 0.05)。在领域自适应后，对 DHMC 队列的外部评估实现了 0.87 的 C 指数 (95% CI: 0.77 至 0.95)。结论：对比多模态学习通过有效整合组织病理学、基因组学和临床数据，显著增强了 2/3 级胶质瘤的生存预测。这种无需标注的方法能够利用常规收集的数据进行早期风险分层，并有望为个性化治疗决策和临床试验分层提供参考。

## Abstract
BACKGROUND: Accurate survival prediction for grade 2/3 glioma patients remains challenging due to tumor biological heterogeneity and limitations of current prognostic methods that rely on single-modality data. METHODS: We developed a multimodal deep learning framework integrating histopathology whole-slide images, somatic mutations, and clinical-demographic data. A three-stage training pipeline combined contrastive learning with survival-specific optimization to align cross-modal representations. The framework was trained on 498 grade 2/3 glioma patients from TCGA and evaluated using 5-fold cross-validation and an independent Dartmouth-Hitchcock Medical Center (DHMC) cohort (n = 61). RESULTS: The contrastive multimodal model achieved a c-index of 0.91 (95% CI: 0.84 to 0.96), significantly outperforming the unimodal models (image-only = 0.76; non-image-only = 0.87) and showing an improvement over the non-contrastive multimodal model (c-index = 0.89), although this difference was not statistically significant. Kaplan-Meier analysis demonstrated clear survival separation across risk strata (log-rank P = 4.4 × 10-5). Contrastive learning improved representation clustering quality, with silhouette scores increasing from 0.20 to 0.24 (P = 0.05). External evaluation on the DHMC cohort achieved a c-index of 0.87 (95% CI: 0.77 to 0.95) after domain adaptation. CONCLUSION: Contrastive multimodal learning significantly enhances survival prediction in grade 2/3 gliomas by effectively integrating histopathology, genomics, and clinical data. This annotation-free approach enables early risk stratification using routinely collected data and shows promise for informing personalized treatment decisions and clinical trial stratification.