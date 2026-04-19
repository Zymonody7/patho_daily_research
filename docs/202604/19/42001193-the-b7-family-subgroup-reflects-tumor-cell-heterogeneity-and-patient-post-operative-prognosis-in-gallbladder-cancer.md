---
title: The B7 family subgroup reflects tumor cell heterogeneity and patient post-operative prognosis in gallbladder cancer.
title_zh: B7家族亚群反映了胆囊癌的肿瘤细胞异质性及患者术后预后
authors: "Chuhan Ma, Huixin Hu, Yang Li, Chongli Zhong, YunHao Dong, Zhanhao Chang, Shuo Xu, Yuyang Zhang, Hangqi Hu, Chao Lv, Yu Tian"
date: 2026-04-18
pdf: "https://pubmed.ncbi.nlm.nih.gov/42001193/"
tags: ["query:seqai"]
score: 7.0
evidence: 单细胞RNA测序分析肿瘤细胞异质性
tldr: 针对胆囊癌（GBC）术后预后评估不准及肿瘤异质性不明的问题，研究通过单细胞测序分析了B7家族分子（CD276、VTCN1、HHLA2）在不同上皮亚群中的表达特征。发现HHLA2通过RAC1/CDC42-PAK1-Cofilin通路促进肿瘤上皮-间充质转化（EMT）。基于这些分子标志物结合临床特征构建的GBM机器学习模型，显著提升了术后风险分层能力，为胆囊癌精准治疗提供了新靶点和预测工具。
selection_source: fresh_fetch
motivation: 旨在通过单细胞分辨率探究B7家族免疫检查点分子在胆囊癌细胞异质性中的作用，并优化患者术后风险分层。
method: 利用单细胞转录组测序定义肿瘤亚群，通过分子生物学实验验证HHLA2信号通路，并对比多种机器学习算法构建生存预测模型。
result: 发现CD276和VTCN1与细胞增殖相关，而HHLA2通过激活RAC1/CDC42-PAK1-Cofilin通路驱动肿瘤迁移与EMT，且集成这些指标的GBM模型预测效果最优。
conclusion: B7家族分子不仅揭示了胆囊癌的功能亚群差异，还可作为关键生物标志物提升术后预后评估的准确性。
---

## 摘要
目的：旨在通过在单细胞分辨率下研究B7家族免疫检查点分子CD276 (B7-H3)、VTCN1 (B7-H4)和HHLA2 (B7-H7)的表达及其下游信号转导，阐明胆囊癌（GBC）细胞的生物学异质性，并优化术后风险分层。方法：利用来自7例原发肿瘤的单细胞RNA测序（scRNA-seq）数据，通过非负矩阵分解（NMF）描绘了五个上皮亚群。通过慢病毒干预、药理学抑制和皮下异种移植实验，验证了HHLA2与RAC1/CDC42-PAK1-Cofilin信号通路之间的功能关联。共纳入188例接受手术治疗的GBC患者进行生存建模。基于五个变量（CD276、VTCN1、HHLA2表达，肿瘤大小及分化程度）训练了七种机器学习生存算法，并通过C指数（C-index）、ROC-AUC和校准曲线进行了比较。结果：CD276+和VTCN1+上皮细胞表现出促增殖特征，而HHLA2+细胞则表现出高水平的上皮-间质转化（EMT）和迁移特征。HHLA2过表达导致RAC1/CDC42-PAK1-Cofilin信号活性增加，在体外增强了细胞增殖、侵袭和EMT，并在体内加速了肿瘤生长。这些效应可被RAC1、CDC42或PAK1抑制剂以及CFL1敲降所逆转。NMF将肿瘤上皮细胞分为五个功能各异的亚群。整合了三种B7分子表达、肿瘤大小和分化程度的梯度提升机（GBM）模型在训练集和验证集上均实现了卓越的区分度和准确的校准。结论：B7家族的表达描绘了生物学特征各异的GBC亚群；HHLA2通过RAC1/CDC42-PAK1-Cofilin信号通路促进EMT。纳入CD276、VTCN1和HHLA2表达以及肿瘤大小和分化程度的GBM模型展现了增强术后风险分层的潜力，为生物标志物开发和靶向治疗干预提供了具有前景的候选对象。

## Abstract
PURPOSE: To elucidate the biological heterogeneity of gallbladder cancer (GBC) cells and refine post-operative risk stratification by investigating the expression and downstream signaling of the B7-family immune checkpoint molecules CD276 (B7-H3), VTCN1 (B7-H4), and HHLA2 (B7-H7) at single-cell resolution. METHODS: Single-cell RNA sequencing (scRNA-seq) data from seven primary tumors delineated five epithelial subgroups via non-negative matrix factorization (NMF). The functional association between HHLA2 and RAC1/CDC42-PAK1-Cofilin signaling was validated by lentiviral manipulation, pharmacologic inhibition, and subcutaneous xenografts. A total of 188 surgically treated GBC patients were enrolled for survival modeling. Seven machine-learning survival algorithms were trained on five variables (CD276, VTCN1, HHLA2 expression, tumor size, and differentiation) and compared by C-index, ROC-AUC, and calibration curves. RESULTS: CD276 + and VTCN1 + epithelial cells displayed pro-proliferative profiles, whereas HHLA2 + cells exhibited high EMT and migration signatures. HHLA2 overexpression led to increased RAC1/CDC42-PAK1-Cofilin signaling activity, enhanced proliferation, invasion, and EMT in vitro, and accelerated tumor growth in vivo. These effects were reversed by RAC1, CDC42, or PAK1 inhibitors, as well as by CFL1 knockdown. NMF classified tumor epithelial cells into five functionally distinct subgroups. A gradient-boosting machine (GBM) model integrating expression of the three B7 molecules with tumor size and differentiation achieved superior discrimination and accurate calibration on both the training and validation sets. CONCLUSION: B7-family expression delineates biologically distinct GBC subpopulations; HHLA2 promotes EMT via RAC1/CDC42-PAK1-Cofilin signaling. The GBM model incorporating CD276, VTCN1, and HHLA2 expression with tumor size and differentiation demonstrates potential for enhanced post-operative risk stratification, offering promising candidates for biomarker development and targeted therapeutic interventions.