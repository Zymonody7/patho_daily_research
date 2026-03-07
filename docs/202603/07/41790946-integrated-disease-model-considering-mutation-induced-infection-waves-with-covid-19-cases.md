---
title: Integrated disease model considering mutation-induced infection waves with COVID-19 cases.
title_zh: 考虑突变诱发感染波及 COVID-19 病例的综合疾病模型
authors: "Seungho Baek, Haneol Cho, SangChul Lee, Myeongsu Yoo, Donghyok Kwon, KyuHwan Lee, Yeonju Kim, Chansoo Kim"
date: 2026-01-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/41790946/"
tags: ["query:pathoai"]
score: 7.0
evidence: 针对新冠病毒变异诱发感染波的综合疾病模型
tldr: 针对传统SIR模型难以捕捉新冠病毒多变异株引发的多波疫情动态的问题，该研究提出一种集成建模方法，通过叠加代表不同主导变异株的S型逻辑回归曲线来模拟累计感染人数。利用PELT算法确定变异株更替的数学切分点，并在14个国家的数据上验证了该模型。结果表明，这种多变异株集成框架比单毒株模型预测精度显著提高，为应对病毒变异提供了动态更新的流行病学预测方案。
selection_source: fresh_fetch
motivation: 传统流行病学模型在面对病毒频繁变异导致的多轮感染高峰时，难以准确描述复杂的疫情演变动态。
method: "通过叠加多个代表不同主导变异株的逻辑回归曲线，并结合PELT算法在变异株占比约50%的关键点进行模型重校准。"
result: 在对美国、英国等14个国家及全球数据的实证评估中，该集成模型在MAPE和RMSE等指标上均优于传统的单毒株预测方法。
conclusion: 研究证实了根据新变异株出现动态更新模型参数的必要性，为未来应对多变异病原体引发的流行病提供了数学理论支撑和预测框架。
---

## 摘要
COVID-19 是一场前所未有的全球大流行，引发了连续的感染波，给公共卫生和流行病学研究带来了独特的挑战。传统的易感者-感染者-康复者（SIR）模型往往难以捕捉这些复杂的动态，特别是考虑到该病毒已经产生了多种亚变体。为了应对这些挑战，我们采用了一种经验建模方法，将来自 Our World in Data（每日确诊 COVID-19 病例）和 GISAID（变体流行率）的真实世界数据整合到一个新提出的综合模型中。具体而言，我们对多条 S 型（逻辑回归）曲线进行求和，每条曲线代表一个特定主导变体的累计感染人数，并在新变体出现时重新校准模型。通过纳入变体特异性参数，我们的框架以动态、数据驱动的方式有效地捕捉了 COVID-19 的生物学和流行病学特征。最重要的是，我们采用了剪枝精确线性时间（PELT）算法，为何时可以合法地对独立变体模型进行求和提供了严谨的数学依据：具体而言，即当变体主导率达到约 50% 时。这确立了在特定主导条件下可以将独立的逻辑模型进行加性组合的理论基础。我们使用平均绝对百分比误差（MAPE）、均方根误差（RMSE）和平均绝对误差（MAE）来评估我们的模型。基于来自 14 个国家（包括韩国、美国和英国）以及全球汇总数据，我们的实证结果证实，与单毒株方法相比，整合主导变体能显著提高准确性。我们还提供了通过逻辑函数近似 SIR 动态的理论动机，并讨论了如何改进该综合框架以增强预测性能。通过这种方式，我们展示了针对新出现的变体迭代更新流行病学模型的可行性和优势，从而为当前和未来的大流行管理提供具有操作性的见解。

## Abstract
COVID-19, an unprecedented global pandemic, has caused successive waves that pose unique challenges to public health and epidemiological research. Traditional Susceptible-Infected-Recovered (SIR) models often struggle to capture these complex dynamics, especially given that the virus has spawned multiple sub-variants. To tackle these challenges, we adopt an empirical modeling approach by integrating real-world data from Our World in Data (daily confirmed COVID-19 cases) and GISAID (variant prevalence) into a newly proposed integrated model. Specifically, we sum multiple sigmoidal (logistic) curves, each representing the cumulative infections of a distinct dominant variant, and recalibrate the model whenever a new variant emerges. By incorporating variant-specific parameters, our framework effectively captures the biological and epidemiological characteristics of COVID-19 in a dynamic, data-driven manner. Most importantly, we employ the Pruned Exact Linear Time (PELT) algorithm to provide rigorous mathematical justification for when separate variant models can be legitimately summed: specifically, when variant dominance reaches approximately 50%. This establishes the theoretical foundation that separate logistic models can be additively combined under specific dominance conditions. We evaluate our model using Mean Absolute Percentage Error (MAPE), Root Mean Square Error (RMSE), and Mean Absolute Error (MAE). Our empirical findings confirm that integrating dominant variants is associated with markedly improved accuracy compared to a single-strain approach, based on data from fourteen countries (including South Korea, the United States, and the United Kingdom) and global aggregates. We also provide theoretical motivation for approximating SIR dynamics via logistic functions and discuss how this integrated framework can be refined to enhance predictive performance. In doing so, we demonstrate the feasibility and advantages of iteratively updating epidemiological models in response to emerging variants, thereby offering actionable insights for ongoing and future pandemic management.