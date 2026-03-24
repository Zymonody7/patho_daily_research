---
title: On the utility of Deep Learning for model classification and parameter estimation on complex diversification scenarios.
title_zh: 论深度学习在复杂多样化情景下的模型分类与参数估计中的效用
authors: "Pablo Gutiérrez de la Peña, Guillermo Iglesias, Edgar Talavera, Andrea Sánchez Meseguer, Isabel Sanmartín"
date: 2026-03-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/41874436/"
tags: ["query:pathoai"]
score: 8.0
evidence: 深度学习用于系统发育树的模型分类和参数估计
tldr: "针对系统发育树分析中传统似然法难以处理复杂演化模型的问题，本研究评估了卷积神经网络（CNN）在物种多样化模型分类和参数估计中的表现。通过对六种复杂演化场景（如大规模灭绝、多样性依赖等）进行大规模模拟，并利用CDV向量化技术处理树结构数据，结果显示CNN在模型分类准确率（80-93%）和参数回归精度上均优于传统极大似然估计（MLE），为宏观演化研究提供了一种高效的深度学习替代方案。"
selection_source: fresh_fetch
motivation: 传统的似然法在处理高复杂度的随机演化模型时存在计算瓶颈，限制了对复杂物种多样化动态的研究。
method: 利用卷积神经网络（CNN）对经过CDV向量化处理的系统发育树数据进行训练，执行六种演化场景的分类任务及相关参数的回归估计。
result: "CNN在模型分类上的准确率达到80-93%，显著高于极大似然估计的70-74%，且在参数估计的平均误差上也表现更优。"
conclusion: 深度学习方法在处理复杂演化模型时比传统统计方法更具优势，未来可进一步扩展至谱系异质性等更复杂的生物地理模型。
---

## 摘要
应用于定年系统发育树的出生-死亡模型是研究过去多样化动态的有用工具。这些随机模型中的参数通常使用基于似然的方法进行推断；然而，对于中高复杂度的模型，这些方法可能会出现计算可处理性问题。深度学习是一种在保持计算可处理性的同时增加模型复杂性的方法。这些技术最近已在序列采样系统发育（系统发育动力学）和性状依赖的出生-死亡模型（宏观进化）背景下得到了探索。在本文中，我们探讨了卷积神经网络（CNN）在六种恒定速率和随时间变化的谱系同质多样化情景下，解决仅含现存物种系统发育树的分类（模型选择）和回归（参数估计）任务的能力，这些情景包括：恒定出生-死亡、高灭绝、大规模灭绝、多样性依赖的多样化，以及分段恒定情景“停滞与辐射”和“兴起与衰落”。我们在每种多样化情景下模拟了 10,000 棵系统发育树，并使用 CDV 向量化程序对其进行编码以捕获支系长度信息。编码后的树被用于训练一组 CNN 模型，这些模型旨在匹配桉树、针叶树和鲸目动物的三种经验系统发育树，这些发育树此前曾用于基准测试多样化模型，且在现存末端节点数量上有所不同。此外，我们针对同一组情景比较了 CNN 与极大似然估计（MLE）的性能。我们发现 CNN 的分类准确率达到了 80-93%，而 MLE 的准确率为 70-74%。对 CNN 分类而言，最困难的情景是高灭绝和大规模灭绝。对于回归任务，MLE 的平均绝对误差略高于深度学习。两种方法在估计比率参数（如大规模灭绝存活率和相对灭绝率）时都存在困难。最后，我们将 CNN 模型应用于最佳拟合多样化情景下三种经验系统发育树的参数估计。这使我们能够讨论不足之处和未来的改进方向，例如引入速率可变、谱系异质的模型。

## Abstract
Birth-Death models applied to dated phylogenies are useful tools to study past diversification dynamics. Parameters in these stochastic models are typically inferred using likelihood-based methods; however, these approaches can exhibit computational tractability issues for models of moderate to high complexity. One approach to increase model complexity while remaining computationally tractable is Deep Learning. These techniques have recently been explored in the context of serially-sampled phylogenies (phylodynamics) and trait-dependent birth-death models (macroevolution). Here, we explore the power of Convolutional Neural Networks (CNNs) to solve classification (model selection) and regression (parameter estimation) tasks for extant-only phylogenies under six constant-rate and time-varying, lineage-homogeneous diversification scenarios: Constant Birth-Death, High Extinction, Mass Extinction, Diversity-Dependent Diversification, and the piecewise-constant scenarios Stasis-and-Radiate and Waxing-and-Waning. We simulated 10,000 phylogenetic trees under each diversification scenario, which were encoded using the CDV vectorization procedure to capture branch length information. The encoded trees were used to train a set of CNNs models designed to match three empirical phylogenies of eucalypts, conifers, and cetaceans, which have previously been used for benchmarking diversification models and differ in the number of extant tips. Additionally, we compared CNN performance with Maximum Likelihood Estimation (MLE) for the same set of scenarios. We found that CNNs exhibited classification accuracy levels of 80-93%, whereas MLE achieved levels of 70-74%. The most difficult scenarios for CNN classification were High Extinction and Mass-Extinction. For regression tasks, mean average errors were slightly higher for MLE compared with DL. Both approaches had difficulty estimating ratio parameters such as mass-extinction survival and relative extinction. Finally, we applied our CNN models for parameter estimation on the three empirical phylogenies under the best-fit diversification scenario. This allows us to discuss shortcomings and future avenues for improvement, such as the inclusion of rate-variable, lineage-heterogeneous models.