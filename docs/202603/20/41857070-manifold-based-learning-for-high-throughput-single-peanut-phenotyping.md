---
title: Manifold-based learning for high-throughput single-peanut phenotyping.
title_zh: 基于流形学习的高通量单粒花生表型分析
authors: "Weng Kung Peng, Xiaomin Lin, Peishan Deng, Jianwen Jiang, Chunling Ding, Shijin Yuan"
date: 2026-03-19
pdf: "https://pubmed.ncbi.nlm.nih.gov/41857070/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 流形学习用于表型的大规模几何建模
tldr: 花生育种受限于复杂的基因型与表型交互作用，缺乏高效的量化手段。该研究开发了一套高通量表型分析框架，利用数码显微镜或手机成像结合流形学习技术，捕捉花生果实的几何形态特征。通过对中国各地6500多颗花生果实的分析，成功识别出具有地理特征的形态标记并实现了品种的精准鉴别，为构建预测表型性状的几何大模型及加速精准农业奠定了基础。
selection_source: fresh_fetch
motivation: 针对花生基因型与表型之间受环境影响且难以量化分析的问题，亟需一种高效、低成本的大规模表型提取工具。
method: 采用数字显微成像或手机拍摄获取图像，并集成流形学习算法对花生果实的几何空间分布进行降维分析与可视化。
result: 基于中国境内6500余份样本，该方法准确识别了不同产地的形态差异，并实现了对花生品种的高精度自动分类。
conclusion: 该研究建立的可扩展几何分析流程，为开发能够预测作物性状的几何大模型提供了技术支撑，有助于提升花生育种的智能化水平。
---

## 摘要
花生（Arachis hypogaea L.）是一种因高含油量而备受重视的主要豆类作物，其表现出受环境影响塑造的复杂基因型-表型相互作用，但这些关系目前仍不为人所熟知。我们提出了一种高通量表型分析框架，该框架利用数字显微镜或智能手机成像技术捕捉花生荚果的几何形状，并结合流形学习进行大规模分析和可视化。通过对从中国各地收集的 6500 多个荚果进行研究，我们识别出了具有地理特征的形态特征，并实现了准确的品种鉴别。这种可扩展的方法为能够预测表型特征并加速精准农业发展的“大几何模型”（Large Geometric Model）奠定了基础。我们的流程为花生育种和可持续作物改良提供了一种变革性工具。

## Abstract
Peanut (Arachis hypogaea L.), a major legume crop valued for its high oil content, displays complex genotypic-phenotypic interactions shaped by environmental influences, yet these relationships remain poorly understood. We present a high-throughput phenotyping framework that captures the geometry of peanut pods using digital microscopy or smartphone imaging integrated with manifold-learning for large-scale analysis and visualization. Using over 6500 pods collected across China, we identify a geographically distinct morphological signature and demonstrate accurate cultivar discrimination. This scalable approach establishes the foundation for a Large Geometric Model capable of predicting phenotypic traits and accelerating precision agriculture. Our pipeline offers a transformative tool for peanut breeding and sustainable crop improvement.