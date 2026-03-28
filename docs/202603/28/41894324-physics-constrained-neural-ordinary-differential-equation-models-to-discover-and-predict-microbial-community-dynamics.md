---
title: Physics-constrained neural ordinary differential equation models to discover and predict microbial community dynamics.
title_zh: 物理约束的神经常微分方程模型用于发现和预测微生物群落动态
authors: "Thompson J, Connors BM, Zavala VM, Venturelli OS., Jaron Thompson, Bryce M Connors, Victor M Zavala, Ophelia S Venturelli"
date: 2026-03-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/41894324/"
tags: ["query:pathoai"]
score: 9.0
evidence: 物理约束的机器学习用于微生物群落动态
tldr: 微生物群落的动态受代谢物竞争和互补驱动，但传统机理模型过于僵化，而纯机器学习模型又缺乏可解释性且易过拟合。本研究提出了“神经物种中介者（NSM）”模型，将描述代谢物动态的机理方程与神经网络相结合，构建物理约束的神经常微分方程。实验证明，NSM 在体外数据集上的预测性能优于单一模型，并能揭示潜在的生物相互作用，为理解和控制微生物群落提供了兼具灵活性与可解释性的新工具。
selection_source: fresh_fetch
motivation: 现有的微生物群落模型在捕捉复杂的代谢物介导相互作用时，面临机理模型假设过于僵化与机器学习模型缺乏可解释性且数据需求量大的双重挑战。
method: 提出了一种名为 NSM 的物理约束机器学习模型，通过在神经常微分方程框架中嵌入神经网络，来学习和模拟微生物与代谢物之间的动态交互。
result: 在体外实验数据集上的测试结果显示，NSM 的预测准确度超过了纯机理模型和纯机器学习模型，并能提供关于生物直接相互作用的深刻见解。
conclusion: 将神经网络有机嵌入到微生物群落的机理模型中，能够显著提升模型对复杂生物系统动态的预测能力和生物学解释力。
---

## 摘要
微生物群落在塑造生态系统功能方面发挥着至关重要的作用，而预测性建模框架对于理解、控制和利用其特性至关重要。代谢物的竞争和交叉喂养驱动着微生物组的动态和功能。现有的捕捉微生物群落中代谢物介导相互作用的机理模型由于僵化的假设而灵活性有限。虽然机器学习模型提供了灵活性，但它们需要大型数据集，难以解释，并且可能会对实验噪声产生过拟合。为了克服这些局限性，我们开发了一种物理约束的机器学习模型，称之为神经物种中介器（NSM），它将代谢物动态的机理模型与机器学习组件相结合。NSM 在体外实验数据集上的表现优于机理或机器学习组件，并提供了对直接生物相互作用的见解。总之，与单独的机理或机器学习组件相比，将神经网络精心嵌入到微生物群落动态的机理模型中，提高了预测性能和可解释性。

## Abstract
Microbial communities play essential roles in shaping ecosystem functions and predictive modeling frameworks are crucial for understanding, controlling, and harnessing their properties. Competition and cross-feeding of metabolites drives microbiome dynamics and functions. Existing mechanistic models that capture metabolite-mediated interactions in microbial communities have limited flexibility due to rigid assumptions. While machine learning models provide flexibility, they require large datasets, are challenging to interpret, and can overfit to experimental noise. To overcome these limitations, we develop a physics-constrained machine learning model, which we call the neural species mediator (NSM), that combines a mechanistic model of metabolite dynamics with a machine learning component. The NSM outperforms mechanistic or machine learning components on in vitro experimental datasets and provides insights into direct biological interactions. In summary, carefully embedding a neural network into a mechanistic model of microbial community dynamics improves prediction performance and interpretability compared to its constituent mechanistic or machine learning components.