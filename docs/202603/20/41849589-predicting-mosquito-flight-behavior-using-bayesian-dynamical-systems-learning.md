---
title: Predicting mosquito flight behavior using Bayesian dynamical systems learning.
title_zh: 利用贝叶斯动力系统学习预测蚊子飞行行为
authors: "Christopher Zuo, Chenyi Fei, Alexander E Cohen, Soohwan Kim, Ring T Cardé, Jörn Dunkel, David L Hu"
date: 2026-03-20
pdf: "https://pubmed.ncbi.nlm.nih.gov/41849589/"
tags: ["query:pathoai"]
score: 6.0
evidence: 贝叶斯学习用于疾病媒介监测
tldr: 针对蚊媒疾病防控中对蚊子寻宿主行为缺乏定量理解的问题，研究者结合三维红外追踪技术与贝叶斯动力系统推理，利用超过2000万个飞行轨迹数据点，构建了一个描述埃及伊蚊在视觉和二氧化碳诱导下飞行行为的生物物理模型。该模型能准确预测蚊子对人类目标的反应，为优化蚊虫捕获和防控策略提供了定量基础。
selection_source: fresh_fetch
motivation: 为了解决目前对视觉和感官信号如何引导蚊子寻找目标的定量理解不足，从而提升蚊虫捕获和监测的效率。
method: 结合三维红外追踪技术获取海量埃及伊蚊飞行轨迹，并利用贝叶斯动力系统推理方法学习其背后的生物物理动力学模型。
result: 该模型基于超过2000万个数据点训练，能够精确预测蚊子在二氧化碳和视觉诱导下对人类目标的飞行响应行为。
conclusion: 研究建立的定量行为模型为优化蚊虫捕获装置设计和制定疾病防控策略提供了科学的计算基础。
---

## 摘要
蚊媒疾病每年在全球导致数十万人死亡。破译蚊子的寻宿行为对于通过蚊子捕获和监测来预防疾病传播至关重要。尽管最近取得了实质性进展，但我们仍然缺乏对视觉和其他感官线索如何引导蚊子寻找目标的全面定量理解。在此，我们将埃及伊蚊（Aedes aegypti）的三维红外追踪与贝叶斯动力系统推理相结合，学习了一个蚊子寻宿行为的定量生物物理模型。该模型基于超过 2000 万个数据点进行训练，每个数据点对应于在视觉和二氧化碳线索存在下记录的蚊子自由飞行轨迹中的瞬时位置和速度，能够准确预测蚊子对人类目标的反应。我们的研究结果为优化蚊子捕获和控制策略提供了定量基础，这是减轻蚊媒疾病影响的关键一步。

## Abstract
Mosquito-borne diseases cause several hundred thousand deaths worldwide every year. Deciphering mosquito host-seeking behavior is essential to prevent disease transmission through mosquito capture and surveillance. Despite recent substantial progress, we still lack a comprehensive quantitative understanding of how visual and other sensory cues guide mosquitoes to their targets. Here, we combined three-dimensional infrared tracking of Aedes aegypti mosquitoes with Bayesian dynamical systems inference to learn a quantitative biophysical model of mosquito host-seeking behavior. Trained on more than 20 million data points, each corresponding to an instantaneous position and velocity in mosquito free-flight trajectories recorded in the presence of visual and carbon dioxide cues, the model accurately predicts how mosquitoes respond to human targets. Our results provide a quantitative foundation for optimizing mosquito capture and control strategies, a key step toward mitigating the impact of mosquito-borne diseases.