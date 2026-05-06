---
title: "From Trait-Structured Within-Host Dynamics to SIR Models: A Multiscale Framework With Re-Exposure."
title_zh: 从基于特征结构的宿主内动力学到 SIR 模型：一个包含再次暴露的多尺度框架
authors: "Cyrille Kenne, Pascal Zongo"
date: 2026-05-06
pdf: "https://pubmed.ncbi.nlm.nih.gov/42089926/"
tags: ["query:pathoai"]
score: 7.0
evidence: 感染建模的多尺度框架
tldr: 针对流行病学中宿主内免疫动态与群体传播模型脱节的问题，本文提出一种基于阈值的多尺度框架，将病原体载量和免疫反应的连续轨迹直接映射为S、I-、I+、R四种群体状态。通过推导具有性状结构的再暴露下一代算子，揭示了接种量和免疫特征对清除-持续转换的影响。该框架不仅能从免疫异质性推导流行指标，还发现了慢性感染导致R0<1时疫情仍持续的现象，为识别慢性病原库和制定防控策略提供了理论依据。
selection_source: fresh_fetch
motivation: 传统的流行病学模型往往忽略了宿主内部免疫动态与群体传播之间的直接机械联系，难以准确评估个体免疫差异对疫情演化的影响。
method: 建立包含病原体载量和非线性免疫激活的二元动力系统，通过直接投影宿主内轨迹定义群体状态，并推导了考虑局部与全局混合的再暴露下一代算子。
result: 模拟显示接种量和免疫性状决定了感染的清除或持续，并观察到S→I-→I+→R的演化级联，以及慢性感染状态引发的群体层面后向分叉现象。
conclusion: 该框架实现了从微观免疫测量到宏观流行指标的一致性推导，证明了慢性感染者在低传播率下维持疫情的关键作用。
---

## 摘要
我们提出了一个基于阈值的多尺度框架，将机械性的宿主内感染动力学与结构化的类 SIR 群体模型联系起来。从包含接种量（类 Allee）阈值和非线性免疫激活的病原体载量与免疫反应双变量系统出发，我们推导出了映射规则，将连续轨迹划分为四种状态：易感（S）、低免疫保护感染（I-）、高免疫保护感染（I+）和康复（R）。在这里，“感染”是指具有可检测病原体载量的个体。与以往的多尺度方法不同，我们的框架将两个尺度整合到一个单一系统中：群体仓室通过宿主内轨迹的直接投影产生，避免了临时性的连接函数。我们推导了针对特征结构化再次暴露（局部与全局混合）的下一代算子，以及全局混合下 R0 的显式表达式。模拟揭示了由接种量大小和免疫特征驱动的剧烈清除-持续转变，以及一种涌现的 S → I- → I+ → R 级联过程。在剧烈的阈值和激活条件下，慢性的宿主内平衡即使在 R0 < 1 时也能维持感染，从而在群体层面产生类似后向分叉的行为。该框架提供了一条从免疫异质性到流行病指标的一致路径，对于识别慢性宿主、解释剂量-反应数据以及直接从宿主内测量值估计控制阈值具有重要意义。

## Abstract
We present a threshold-based multiscale framework that links mechanistic within-host infection dynamics to a structured, SIR-like population model. Starting from a two-variable system for pathogen load and immune response that includes inoculum (Allee-like) thresholds and nonlinear immune activation, we derive mapping rules that classify continuous trajectories into four states: susceptible (S), infected with low immune protection ( I -  ), infected with high immune protection ( I +  ), and recovered (R). Here, "infected" refers to individuals with a detectable pathogen load. Unlike previous multiscale approaches, our framework integrates both scales into a single system: population compartments emerge by direct projection of within-host trajectories, avoiding ad hoc linking functions. We derive a next-generation operator for trait-structured re-exposure (local vs. global mixing) and an explicit expression for R 0  under global mixing. Simulations reveal sharp clearance-persistence transitions driven by inoculum size and immune trait, and an emergent S  →  I -  →  I +  →  R  cascade. Under sharp thresholds and activation, chronic within-host equilibria can sustain infection even when  R 0 < 1  , producing backward-bifurcation-like behavior at the population level. The framework provides a consistent route from immunological heterogeneity to epidemic indicators, with implications for identifying chronic reservoirs, interpreting dose-response data, and estimating control thresholds directly from within-host measurements.