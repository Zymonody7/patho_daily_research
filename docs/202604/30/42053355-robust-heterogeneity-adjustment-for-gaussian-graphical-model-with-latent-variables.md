---
title: Robust Heterogeneity Adjustment for Gaussian Graphical Model With Latent Variables.
title_zh: 具有潜变量的高斯图模型的稳健异质性调整
authors: "Li L, Li R, Ma S, Zhang Q."
date: 2026-05-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/42053355/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 用于编码多变量生物数据中条件依赖关系的图形模型
tldr: 针对生物多元数据中因未观测子群体（如肿瘤亚型）和离群点导致的图模型估计失真问题，该研究提出了一种结合混合模型的鲁棒潜变量高斯图模型。该方法在剔除潜变量干扰的同时，能同步实现网络结构估计、离群点检测及子群体识别。实验证明，该方法在存在高比例噪声和异质性时仍能保持估计的可靠性，为复杂生物网络分析提供了稳健的工具。
selection_source: fresh_fetch
motivation: 传统潜变量高斯图模型在处理具有未观测子群体异质性和技术伪影离群点的数据时，容易产生错误的条件依赖结构估计。
method: 通过将混合模型集成到潜变量高斯图框架中，构建了一个能够同时处理数据异质性、识别样本归属并剔除离群点干扰的鲁棒估计框架。
result: 实验表明该方法在高度异质和多噪声的环境下，依然能准确恢复剔除潜变量影响后的网络结构，并成功应用于乳腺癌数据的亚型分析。
conclusion: 该研究为存在复杂异质性和异常值的多元数据提供了一种通用的图模型推断方案，增强了生物网络分析的准确性与鲁棒性。
---

## 摘要
图模型是编码多变量生物数据中条件依赖结构的基础工具，而潜变量高斯图模型在存在未观测混杂变量的情况下，对于捕捉复杂的依赖关系起着关键作用。然而，实际应用中常面临两个关键挑战：源自未观测子群体（如肿瘤亚型、细胞簇或患者分层）的系统性异质性，以及离群值（如技术伪影或罕见的表型变异），这两者都可能显著扭曲潜在的网络结构。为解决这些问题，我们通过集成混合模型扩展了潜变量高斯图模型，提出了一种针对数据异质性定制的稳健框架。所提方法可以同时实现网络结构估计（在移除潜变量的共享效应后）、离群值检测以及子群体成员身份识别。本文开发了一种有效的计算算法。广泛的实验评估表明，所提方法在存在异质性的情况下能提供可靠的图估计，即使在存在显著比例离群值的情况下也能保持稳健性。对乳腺癌数据集的异质性分析进一步说明了该方法的实际适用性及其合理的生物学意义。

## Abstract
Graphical models serve as fundamental tools for encoding conditional dependence structures in multivariate biological data, with latent variable Gaussian graphical models playing a pivotal role in capturing complex dependencies in the presence of unobserved confounding variables. However, practical implementations often face two critical challenges: systematic heterogeneity arising from unobserved subpopulations (e.g., tumor subtypes, cell clusters, or patient stratifications) and outliers (e.g., technical artifacts or rare phenotypic variations), both of which can substantially distort the underlying network structure. To address these issues, we extend the latent variable Gaussian graphical model by integrating a mixture model, proposing a robust framework tailored for data heterogeneity. The proposed method can simultaneously achieve network structure estimation (after removing shared effects from latent variables), outlier detection, and subgroup membership identification. An effective computational algorithm is developed. Extensive experimental evaluations demonstrate that the proposed method offers a reliable graphical estimate in the presence of heterogeneity, maintaining robustness even against a significant proportion of outliers. The heterogeneity analysis of a breast cancer dataset further illustrates the practical applicability of the proposed approach and its sound biological implications.