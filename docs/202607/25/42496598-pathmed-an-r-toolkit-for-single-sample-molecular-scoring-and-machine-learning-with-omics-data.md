---
title: "PathMED: An R toolkit for single-sample molecular scoring and machine learning with omics data."
title_zh: PathMED：一个用于组学数据单样本分子评分和机器学习的 R 工具包
authors: "Jordi Martorell-Marugán, Ivan Ellson, Raúl López-Domínguez, Pablo Pedro Jurado-Bascón, Juan Antonio Villatoro-García, Chang Wang, Frédéric Baribaud, Daniel Toro-Domínguez, Pedro Carmona-Sáez"
date: 2026-07-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/42496598/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 用于组学数据机器学习和分子评分的R工具包
tldr: 针对组学数据分析中分子评分方法分散且缺乏机器学习集成的问题，PathMED 提供了一个统一的 R 语言工具包。它整合了多种单样本评分算法，并配套了完整的机器学习模块，支持从转录组到蛋白质组的跨组学模型迁移。实验证明，该工具能有效预测乳腺癌治疗反应并解析疾病异质性，显著提升了组学研究的可解释性与模型泛化能力。
selection_source: fresh_fetch
motivation: 现有的分子评分工具缺乏统一框架，且难以直接与机器学习流程结合进行临床表型预测。
method: 开发了集成多种评分算法与机器学习模块的 R 包 PathMED，并引入基因集剖析步骤以处理通路层面的异质性。
result: 在乳腺癌等数据集上验证了该工具在跨组学预测、疗效评估及关键生物通路识别方面的有效性。
conclusion: PathMED 简化了从原始组学数据到生物学解释及临床预测的转化流程，是多组学研究的有力工具。
---

## 摘要
动机：分子评分是利用组学数据研究通路水平功能改变的一种流行方法。与直接使用组学数据相比，将分子评分用于单样本分子表征、表型预测或疾病分层等任务具有多项优势。分子评分提供了生物学可解释性，且在不同数据集之间具有更好的泛化性，从而促进了数据整合和机器学习应用。然而，目前有许多评分方法分布在不同的软件包中，且缺乏能够轻松将这些评分用于模型训练和预测的工具。结果：我们开发了 pathMED，这是一个 R/Bioconductor 软件包，它在一个简单的框架中统一了各种评分方法。此外，pathMED 还包含一个机器学习模块，用于训练和测试利用计算出的分子评分来预测临床结局的模型。我们通过三个使用公共组学数据的案例展示了其部分潜在应用。我们展示了在转录组评分上训练的机器学习模型在应用于蛋白质组评分以预测临床结局时的泛化能力。我们还演示了转录组评分在预测乳腺癌治疗反应以及识别与肿瘤生物学和治疗反应强相关的通路方面的应用。最后，我们展示了在分析流程中整合一种新型基因集剖析步骤对于在通路水平解决疾病异质性的益处。可用性：PathMED 可在 Bioconductor 仓库（https://bioconductor.org/packages/release/bioc/html/pathMED.html）免费获取。用于重现分析的代码已公开于 https://github.com/GENyO-BioInformatics/pathMED_article。补充信息：补充数据可在 Bioinformatics 在线版获取。

## Abstract
MOTIVATION: Molecular scoring is a popular approach for studying pathway-level functional alterations with omics data. Using molecular scores for tasks such as single-sample molecular characterisation, phenotype prediction or disease stratification has several advantages compared to using omics data directly. Molecular scores provide biological interpretability and are more generalisable across datasets, facilitating data integration and machine learning applications. However, numerous scoring methods are available through different software packages, and currently there is a lack of tools to easily use these scores for model training and prediction. RESULTS: We developed pathMED, an R/Bioconductor package that unifies various scoring methods in a simple framework. Furthermore, pathMED also contains a machine learning module to train and test models that use the calculated molecular scores to predict clinical outcomes. We demonstrate some of its potential applications in three use cases using public omics data. We showed the generalisability of machine learning models trained on transcriptomic scores in predicting clinical outcomes when deploying on proteomic scores. We also demonstrated the application of transcriptomics scores in predicting breast cancer treatment response and identifying pathways strongly associated to tumour biology and treatment response. Finally, we demonstrated the benefit of integrating a novel gene set dissection step into the analysis pipeline to resolve disease heterogeneity at the pathway level. AVAILABILITY: PathMED is freely available in the Bioconductor repository (https://bioconductor.org/packages/release/bioc/html/pathMED.html). Code to reproduce the analyses is publicly available at https://github.com/GENyO-BioInformatics/pathMED_article. SUPPLEMENTARY INFORMATION: Supplementary data are available at Bioinformatics online.

---

## 论文详细总结（自动生成）

这篇论文介绍了一个名为 **PathMED** 的 R 语言工具包，旨在解决生物组学数据（如基因表达、蛋白质水平）在机器学习建模中“维度高、噪声大、跨平台通用性差”的问题。

### 1. 解决的问题与核心价值
在 AI 医疗领域，直接使用数万个基因的表达量作为特征进行建模，往往会遇到**过拟合**和**可解释性差**的问题。此外，在转录组（RNA）上训练的模型很难直接用到蛋白质组上。
**PathMED 的价值在于：** 它将原始的分子数据转化为“通路评分（Pathway Scores）”。简单来说，就是不再看单个基因，而是看由一组基因组成的“生物功能小组”的活跃程度。这不仅降低了特征维度，还让模型结果能直接对应到生物学功能（如“免疫反应是否增强”），并显著提升了模型在不同类型数据间的泛化能力。

### 2. 白话版概述
想象你要通过一个人的购物清单（基因数据）来预测他的健康状况。清单上有几万种商品，直接分析太乱了。PathMED 的做法是先分类：把“慢跑鞋、护膝、运动饮料”归为“运动类”，给出一个活跃分。这样，几万个商品就变成了几百个“生活习惯评分”。接着，它内置了机器学习工具，利用这些评分来预测疾病。最厉害的是，即便换了一份不同格式的清单（比如从购物清单换成运动打卡记录），只要它们都指向“运动”这个概念，模型依然有效。

### 3. 方法部分
*   **核心思想：** 知识驱动的降维。利用已知的生物学通路数据库（如 MSigDB），将高维分子特征映射到低维的功能空间。
*   **模型结构：**
    1.  **评分模块（Scoring）：** 集成了多种主流算法（如 GSVA, ssGSEA, PLAGE），将“样本×基因”矩阵转换为“样本×通路”矩阵。
    2.  **机器学习模块（ML）：** 基于 R 语言的 `caret` 框架，支持随机森林、支持向量机等多种分类和回归模型。
    3.  **关键设计——基因集剖析（Gene Set Dissection）：** 这是该工具的特色。传统的通路分析会将所有基因混在一起算分，但 PathMED 可以将一个通路拆解为“上调基因子集”和“下调基因子集”，从而捕捉到更细微的生物学异质性。
*   **推理流程：** 输入原始组学数据 -> 选择评分算法 -> 计算单样本通路得分 -> 训练/调用 ML 模型 -> 输出预测结果（如药物反应、疾病分型）。

### 4. 实验部分
*   **数据与任务：** 使用了公开的乳腺癌转录组和蛋白质组数据。任务包括预测患者对化疗的反应，以及跨组学预测。
*   **主要结果：**
    *   **跨组学迁移：** 在转录组（RNA）数据上训练的模型，直接应用于蛋白质组数据时，表现出极强的鲁棒性。这证明了“通路水平”的特征比“分子水平”的特征更具通用性。
    *   **临床预测：** 在乳腺癌案例中，PathMED 准确识别出了与治疗反应相关的关键生物通路（如细胞周期、免疫检查点），预测准确率优于直接使用原始基因特征。
*   **评价指标：** AUC（曲线下面积）、准确率、灵敏度等。

### 5. 资源与算力
*   **文中未充分披露**具体的硬件配置。但作为一个 R 软件包，它主要运行在通用 CPU 环境下。由于通路评分和传统 ML 模型（非深度学习）计算量相对较小，通常在普通工作站或个人电脑上即可运行。

### 6. 核心贡献与证据
*   **统一框架：** 首次在一个 R 包中打通了“单样本评分 + 机器学习 + 结果解释”的全流程。
*   **跨组学验证：** 论文通过强有力的证据展示了：在 RNA 层面学到的生物学规律（通路评分），可以无缝迁移到蛋白质层面，这为多组学整合提供了新思路。
*   **提升可解释性：** 实验证明该工具能识别出具有临床意义的生物标志物，而不仅仅是一个黑盒预测器。

### 7. 局限与风险
*   **依赖先验知识：** 评分效果高度依赖于预定义的“基因集（Gene Sets）”。如果现有的生物学数据库不完整或有误，模型效果会受限。
*   **线性/传统 ML 局限：** 目前主要集成的是传统机器学习算法，对于超大规模数据（如单细胞测序）或需要复杂非线性建模的任务，可能不如深度学习模型。
*   **R 语言生态限制：** 对于习惯 Python/PyTorch 生态的 AI 研究者来说，存在一定的迁移成本。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事临床生物标志物开发、药物反应预测、以及希望提升组学模型可解释性的 AI 研究员。
*   **后续可跟进的问题：** 能否利用大语言模型（LLM）或图神经网络（GNN）来动态生成或优化这些“基因集”，从而摆脱对静态数据库的依赖？

（完）
