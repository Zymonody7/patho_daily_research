---
title: A Bayesian modelling framework for estimating tick-borne pathogen transmission dynamics at the host-tick interface.
title_zh: 一种用于评估宿主-蜱界面蜱传病原体传播动力学的贝叶斯建模框架
authors: "Kim Y, Faivre B, Boulinier T, Sineau C, Galon C, Moutailler S, Bournez L, Métras R., Younjung Kim, Bruno Faivre, Thierry Boulinier, Célia Sineau, Clémence Galon, Sara Moutailler, Laure Bournez, Raphaëlle Métras"
date: 2026-04-03
pdf: "https://pubmed.ncbi.nlm.nih.gov/41931472/"
tags: ["query:pathoai"]
score: 8.0
evidence: 用于病原体传播动力学的贝叶斯建模
tldr: 蜱传病原体传播涉及宿主到蜱、蜱间共食及预感染等多种复杂路径，难以量化。本研究开发了一个贝叶斯建模框架，通过整合宿主与蜱的野外采样数据，估算不同路径的传播概率及影响因素。在法国鸟类与蜱的实测数据中，该模型证实了“共食传播”在多种病原体扩散中的关键作用，并发现吸血饱满度显著影响传播效率，为精准防控蜱传疾病提供了量化工具。
selection_source: fresh_fetch
motivation: 蜱传病原体存在宿主传播、蜱间共食传播及垂直传播等多种交织路径，传统方法难以准确区分并量化各路径对疾病扩散的贡献。
method: 构建了一个贝叶斯统计建模框架，利用宿主及其体表蜱虫的感染状态数据，联合估计不同传播路径的概率以及物种、发育阶段等协变量的影响。
result: 模拟实验验证了模型参数恢复的准确性，且在法国野外数据中发现，包含“共食传播”路径的模型对伯氏疏螺旋体和嗜吞噬细胞无形体的拟合效果显著优于传统模型。
conclusion: 该框架为利用生态野外监测数据解析蜱传病原体传播动力学提供了标准化工具，强调了记录蜱虫在宿主体表空间分布对提升预测精度的重要性。
---

## 摘要
理解宿主-蜱界面蜱传病原体的传播动力学面临挑战，因为蜱的感染存在多种途径，包括：(i) 宿主到蜱的传播，(ii) 蜱到蜱（共同取食）的传播，以及 (iii) 通过垂直传播或先前取食产生的预存感染。评估控制这些途径的参数对于识别主要传播驱动因素，并进而确定关键防控点至关重要。在本研究中，我们开发了一个贝叶斯建模框架，通过利用采集宿主及其寄生蜱的野外调查数据，对宿主-蜱界面的传播进行联合建模，从而估算描述每种传播途径概率的关键参数，并评估包括鸟类物种、蜱的发育阶段和饱血程度在内的相关因素。首先，通过将模型拟合到模拟的宿主-蜱感染数据，我们证明了该框架恢复这些数据背后参数值的能力。当获得更多关于个体蜱之间共同取食概率变异性的信息时，模型性能显著提高，这突显了检测所有采集到的蜱并记录它们在宿主上相互空间分布的价值。其次，我们将模型拟合到 2023 年在法国东北部鸟类-蜱界面采集的野外数据，重点关注伽氏蜱螺旋体（Borrelia garinii）、瓦莱蜱螺旋体（B. valaisiana）和嗜吞噬细胞无形体（Anaplasma phagocytophilum）作为案例病原体。对于所研究的所有三种病原体，包含共同取食传播的模型对数据的解释力显著优于不包含该途径的模型。饱血程度与嗜吞噬细胞无形体在鸟类到蜱的传播概率呈显著正相关。最后，估算的参数（如鸟类感染嗜吞噬细胞无形体的概率，以及取食前蜱感染螺旋体或无形体的概率）与未用于模型拟合的外部数据集的数值具有可比性。我们的框架为未来基于在宿主-蜱界面采集的流行病学和生态学野外数据来理解蜱传病原体传播动力学提供了宝贵的基础。

## Abstract
Understanding the transmission dynamics of tick-borne pathogens at the host-tick interface is challenged by the presence of multiple pathways for tick infection, including (i) host-to-tick transmission, (ii) tick-to-tick (cofeeding) transmission, and (iii) pre-existing infection through vertical transmission or prior feeding. Assessing parameters governing these pathways is critical for identifying the main transmission drivers and, consequently, key prevention and control points. Here, we developed a Bayesian modelling framework that estimates key parameters describing the probability of each transmission pathway and assesses associated factors, including bird species, tick life stage and engorgement level, by jointly modelling transmission at the host-tick interface using data collected in field studies that sample hosts and their ticks. First, by fitting the model to simulated host-tick infection data, we demonstrated the framework's ability to recover the parameter values underlying these data. Model performance improved significantly when more information was available on variability in cofeeding probability among individual ticks, highlighting the value of testing all collected ticks and recording their spatial distribution on the host in relation to each other. Second, we fitted the model to field data collected at the bird-tick interface in Northeast France in 2023, focusing on Borrelia garinii, B. valaisiana, and Anaplasma phagocytophilum as case pathogens. For all three pathogens studied, models including cofeeding transmission explained the data significantly better than models that did not. Engorgement level was significantly and positively associated with the probability of bird-to-tick transmission for A. phagocytophilum. Finally, the estimated parameters, such as the probability of A. phagocytophilum infection in birds and the probability of Borrelia or Anaplasma infection in ticks before feeding, were comparable to values from an external dataset, not used for model fitting. Our framework provides a valuable foundation for future research to understand tick-borne pathogen transmission dynamics based on epidemiological and ecological field data collected at the host-tick interface.