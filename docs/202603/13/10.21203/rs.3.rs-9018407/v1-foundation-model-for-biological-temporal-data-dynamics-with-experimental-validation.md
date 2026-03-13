---
title: Foundation Model for Biological Temporal Data Dynamics with Experimental Validation
title_zh: 具有实验验证的生物时间数据动力学基础模型
authors: "Duan X, Periwal V."
date: 2026-03-12
pdf: "https://doi.org/10.21203/rs.3.rs-9018407/v1"
tags: ["query:bioinfo"]
score: 8.0
evidence: 生物时间数据动力学基础模型
tldr: 针对生物和生理时间序列数据存在的高维噪声、观测不全及异质性挑战，本文提出一种结合掩码变分自编码器（VAE）与潜空间神经常微分方程（Neural ODE）的通用动力学骨干模型。该模型在脑电图（EEG）、空气质量和果蝇基因表达等异质数据集上，实现了优于传统基准的预测性能，并支持反事实分析与机制蒸馏。研究证明了共享的潜空间动力学架构能有效统一跨领域的预测、适配及可解释性分析任务。
selection_source: fresh_fetch
motivation: 生物生理时间序列数据通常具有高维噪声和时空异质性，导致难以构建既能稳定积分又支持干预分析的连续时间模型。
method: 提出一种可复用的潜空间动力学骨干网络，通过掩码感知 VAE 耦合潜空间神经常微分方程（Neural ODE），实现从观测到潜空间的动力学建模与解码。
result: 在 EEG 预测、空气质量干预模拟及果蝇基因调控机制蒸馏等任务中，该模型均表现出优异的预测精度、数据效率以及对复杂生物过程的解释能力。
conclusion: 共享的潜空间动力学骨干模型能够作为一种“基础模型”，统一处理异质生物时间序列的预测、反事实推理及机制发现。
---

## 摘要
<title>摘要</title> <p>高维生物及生理相关时间序列通常具有噪声、部分观测以及在受试者、空间和时间上的异质性，这使得学习既能稳定积分又对干预分析有用的连续时间模型变得困难。我们提出了一种可重用的潜变量动力学骨干网络，它将掩码感知的变分自编码器与潜变量神经常微分方程相结合，并通过解码后的展开（rollouts）或解码器推前（pushforward）将学习到的动力学返回到观测空间。在这项工作中，我们在动力学意义上使用“基础模型”一词：即一个用于跨数据集和下游任务进行时间建模的共享可迁移骨干网络。我们在三个数据集上评估了该框架：64通道脑电图（EEG）运动与想象、带有气象和日历控制的 AirQualityUCI 多变量环境时间序列，以及配准后的黑腹果蝇囊胚基因表达图谱。在脑电图和空气质量数据中，相同的骨干网络相对于经典基准模型改进了开环预测，并支持受控的反事实展开。在脑电图中，它还实现了高效利用数据的受试者自适应。在空气质量数据中，它支持对外部驱动因素进行可解释的计算机模拟（in silico）干预筛选。在果蝇图谱中，该黑盒骨干网络监督一个稀疏可编辑的 Hill 型机制学生模型，从而产生候选调控结构、方程级扰动假设以及用于机制分析的可解释人工智能工作流。这些结果表明，共享的潜变量动力学骨干网络可以统一异质生物时间序列背景下的预测、自适应、反事实分析、可解释人工智能和机制蒸馏。</p>

## Abstract
<title>Abstract</title>  <p>High-dimensional biological and physiology-adjacent time series are often noisy, partially observed, and heterogeneous across subjects, space, and time, making it difficult to learn continuous-time models that are both stable to integrate and useful for intervention analysis. We propose a reusable latent-dynamics backbone that couples a mask-aware variational autoencoder with a latent neural ordinary differential equation, and returns the learned dynamics to observation space through decoded rollouts or decoder pushforward. In this work, we use the term foundation model in a dynamical sense: a shared transferable backbone for temporal modeling across datasets and downstream tasks. We evaluate the framework on three datasets: 64-channel electroencephalography motor movement and imagery, the AirQualityUCI multi-variate environmental time series with meteorological and calendar controls, and a registered Drosophila blastoderm gene-expression atlas. Across electroencephalography and air quality, the same backbone improves open-loop forecasting relative to classical baselines and supports controlled counterfactual rollouts. In electroencephalography, it also enables data-efficient subject adaptation. In air quality, it supports interpretable in silico intervention screening over exogenous drivers. In the Drosophila atlas, the black-box backbone supervises a sparse editable Hill-type mechanistic student model, yielding candidate regulatory structure, equation-level perturbation hypotheses, and an interpretable artificial-intelligence workflow for mechanistic analysis. These results show that a shared latent-dynamics backbone can unify forecasting, adaptation, counterfactual analysis, interpretable AI, and mechanistic distillation across heterogeneous biological time-series settings.</p>