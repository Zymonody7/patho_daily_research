---
title: Interpretable Machine Learning to Decipher Myelodysplastic Syndrome-Associated Alterations of the Extracellular Matrix by Time-of-Flight Secondary Ion Mass Spectrometry.
title_zh: 利用飞行时间二次离子质谱和可解释机器学习解析骨髓增生异常综合征相关的细胞外基质改变
authors: "Ralf Zimmermann, Mirko Nitschke, Valentina Magno, Friedrich Stölzel, Manja Wobus"
date: 2026-04-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/41782272/"
tags: ["query:seqai"]
score: 7.0
evidence: 用于质谱分类的机器学习流水线
tldr: 骨髓增生异常综合征（MDS）会导致细胞外基质（ECM）发生病理改变，但传统手段难以高效识别其复杂变化。本研究开发了一套结合飞行时间二次离子质谱（ToF-SIMS）与机器学习的分析流程，利用贝叶斯优化的神经网络对患者与健康供体的ECM光谱进行分类，并引入SHAP解释工具揭示了关键的生化差异。该方法实现了无标记的病理检测，为MDS的临床诊断和药物研发提供了新的分子层面视角。
selection_source: fresh_fetch
motivation: 旨在通过分析间充质基质细胞分泌的细胞外基质，寻找与骨髓增生异常综合征相关的病理特征。
method: 采用飞行时间二次离子质谱获取高维光谱数据，并利用贝叶斯优化的神经网络进行分类，结合SHAP值解释模型决策背后的关键化学成分。
result: 成功区分了患者与健康人的细胞外基质样本，并识别出导致两者结构和组成差异的特征离子。
conclusion: 证明了可解释机器学习与质谱技术结合在无标记病理分析中的潜力，有助于开发新型疾病诊断和治疗策略。
---

## 摘要
机器学习（ML）加速了包括生物医学和临床研究在内的许多领域的发展。ML算法为高效分析多变量数据集提供了强大的选择。我们开发并验证了一个ML流程，通过飞行时间二次离子质谱（ToF-SIMS）检测骨髓增生异常综合征（MDS）相关的细胞外基质（ECM）病理改变。研究训练并应用了一个经贝叶斯优化的神经网络（NN），用于对来自MDS患者和健康对照供体的间充质基质细胞（MSCs）分泌的ECM的ToF-SIMS光谱进行分类。在主成分分析验证的基础上，解释工具SHapley Additive exPlanations（简称SHAP）被集成到分析流程中，以揭示ECM变体在组成和结构上的特征差异。我们的结果证明了ToF-SIMS-ML在无标记研究ECM致病性改变方面的潜力。该方法集成到基于细胞和类器官疾病模型的多尺度ECM分析中，可能有助于推动新型诊断和治疗策略的开发。

## Abstract
Machine learning (ML) accelerates progress in many areas, including biomedical and clinical research. ML algorithms provide powerful options for efficiently analyzing multivariate data sets. We developed and validated an ML pipeline to detect myelodysplastic syndrome (MDS)-associated pathological alterations of extracellular matrices (ECMs) by time-of-flight secondary ion mass spectrometry (ToF-SIMS). A Bayesian-optimized neural network (NN) was trained and applied to classify ToF-SIMS spectra of ECM secreted by mesenchymal stromal cells (MSCs) derived from MDS patients and healthy reference donors. Validated by principal component analysis, the explainer tool SHapley Additive exPlanations (known as SHAP) was integrated into the analysis pipeline to unravel characteristic compositional and structural differences of the ECM variants. Our results demonstrate the potential of ToF-SIMS-ML for the label-free investigation of pathogenic alterations of the ECM. Integrated into the multiscale ECM analysis of cell and organoid-based disease models, the introduced methodology may facilitate advances in the development of novel diagnostic and therapeutic strategies.