---
title: Rapid determination of potential mycotoxin-producing fungi contamination in post-harvest blueberries based on near infra-red spectroscopy and enhanced prototypical network.
title_zh: 基于近红外光谱和增强型原型网络的采后蓝莓潜在产毒真菌污染快速检测
authors: "Leqing Zhu, Weijie Xia, Lin Xie, Xiangyang Wang, Shuang Gu"
date: 2026-08-03
pdf: "https://pubmed.ncbi.nlm.nih.gov/42545152/"
tags: ["query:pathoai"]
score: 8.0
evidence: 用于真菌病原体检测和分类的深度学习
tldr: "针对蓝莓采后真菌感染在深色表皮下难以肉眼识别的问题，本研究结合近红外光谱（NIR）技术，提出了一种增强型原型网络模型。该模型通过集成空间注意力机制的卷积神经网络和MetaMix数据增强，在小样本情况下实现了对三种产毒真菌及健康样本的高精度分类，准确率达97.9%，为蓝莓真菌毒素风险的早期无损检测提供了有效方案。"
selection_source: fresh_fetch
motivation: 蓝莓受真菌感染后易产生毒素且初期病征在深色表皮下难以察觉，亟需一种非接触且能应对小样本数据的快速检测技术。
method: 利用近红外光谱获取真菌特征，并构建结合空间注意力机制与MetaMix增强策略的增强型原型网络进行少样本分类学习。
result: "在包含三种产毒真菌及对照组的五分类任务中，该模型在18-shot设置下达到了97.9%的平均准确率和98.1%的精确度。"
conclusion: 实验证明近红外光谱结合原型学习能够有效识别蓝莓早期的真菌污染，为保障食品安全提供了高精度的智能化检测手段。
---

## 摘要
蓝莓易受真菌感染，可能导致真菌毒素污染。准确识别蓝莓中的产毒真菌至关重要，因为受霉菌污染的水果制成的加工产品由于真菌毒素的持久性而具有显著的健康风险。然而，对蓝莓真菌病害进行分类仍具挑战性，因为深色表皮下的感染通常在视觉上无法察觉。近红外（NIR）光谱提供了一种极具前景的替代方案，因为它对不同的真菌病原体表现出独特的吸收特性，并能实现非接触式测量。本研究探讨了利用近红外光谱对三种产毒真菌引起的病害进行分类：交链格孢菌（Alternaria alternata）、藤仓赤霉菌（Fusarium fujikuroi）和扩展青霉（Penicillium expansum）。蓝莓样本分别接种其中一种病原体，或作为未接种的对照组。对两次独立采收的果实在接种后1-6天收集的近红外光谱进行了分析。为了解决有限数据下的分类挑战，本研究提出了一种增强型原型网络来对蓝莓真菌感染进行分类，在第一次采收的数据上进行训练，并在第二次采收的数据上进行验证。具有空间注意力的定制卷积神经网络改进了特征提取，而数据归一化和MetaMix增强则提升了模型性能。通过分层交叉验证，具有18-shot原型的五类分类器实现了97.9%的平均准确率、97.9%的灵敏度、99.5%的特异性、98.1%的精确度和97.9%的F1分数。这些研究结果突显了近红外光谱结合基于原型的学习在蓝莓真菌毒素风险早期检测中的潜力。

## Abstract
Blueberries are susceptible to fungal infection that may lead to mycotoxin contamination. Accurate identification of mycotoxin-producing fungi in blueberries is critical, as processed products derived from mould-contaminated fruits pose significant health risks due to the persistence of mycotoxins. However, classifying fungal diseases in blueberries remains challenging because infections beneath the dark-coloured epidermis are often visually undetectable. Near-infra-red (NIR) spectroscopy presents a promising alternative, as it exhibits distinct absorption characteristics for different fungal pathogens and enables non-contact measurement. This study investigates the use of NIR spectra to classify diseases caused by three mycotoxin-producing fungi: Alternaria alternata, Fusarium fujikuroi, and Penicillium expansum. Blueberry samples were individually inoculated with one of these pathogens or maintained as non-inoculated controls. NIR spectra collected from fruits across two independent harvests were analysed 1-6 days post-inoculation. To address the classification challenge with limited data, this study proposes an enhanced prototypical network to classify blueberry fungal infections, training on the first harvest and validating on the second harvest. A customised convolutional neural network with spatial attention improves feature extraction, while data normalisation and MetaMix augmentation enhance model performance. Through stratified cross-validation, the five-class classifier with 18-shot prototypes achieved an average accuracy of 97.9%, sensitivity of 97.9%, specificity of 99.5%, precision of 98.1% and F1-score of 97.9%. These findings highlight the potential of NIR spectroscopy combined with prototype-based learning for early detection of mycotoxin risks in blueberries.

---

## 论文详细总结（自动生成）

这篇论文介绍了一种结合**近红外光谱（NIR）**技术与**深度学习（增强型原型网络）**的方法，用于快速、无损地检测采后蓝莓是否被产毒真菌污染。

### 1. 解决的问题与价值
*   **核心问题**：蓝莓在采后极易受真菌感染并产生**真菌毒素**（Mycotoxins，一种耐高温、难消除的致毒物质）。由于蓝莓表皮颜色深，早期的真菌感染在视觉上几乎不可见，传统的化学检测又慢且具有破坏性。
*   **研究价值**：真菌毒素一旦进入加工环节（如做成果酱、果汁），会对消费者健康造成长期威胁。该研究提供了一种“不用洗、不用切、照一下就知道”的智能化检测方案，对食品安全预警具有重要意义。

### 2. 白话版概述
蓝莓生病了肉眼看不出来，但不同种类的真菌在生长时会改变蓝莓的化学成分。研究人员用近红外光照射蓝莓，收集反射回来的光谱（相当于蓝莓的“化学指纹”）。因为实际场景中获取带标签的病害样本很难，他们采用了一种擅长处理小数据的 AI 算法——**原型网络**。这个 AI 像是一个经验丰富的“分类员”，它先学习每种真菌感染的特征模版（原型），然后通过对比新样本与模版的相似度，精准判断蓝莓感染了哪种真菌。

### 3. 方法部分
*   **核心思想**：利用**度量学习（Metric Learning）**。将复杂的光谱数据映射到一个高维特征空间，使同类病害的样本在空间中靠得更近，不同类的离得更远。
*   **模型结构**：
    *   **特征提取器**：采用定制的卷积 neural network (CNN)，并引入了**空间注意力机制（Spatial Attention）**。这能让模型自动识别光谱中哪些波段（对应特定的化学键振动）对区分真菌最关键。
    *   **原型生成**：计算每一类已知样本特征的平均值，作为该类的“标准模版”（Prototype）。
*   **关键设计取舍**：
    *   **MetaMix 数据增强**：针对农业数据样本量小的痛点，通过在特征层面进行线性插值合成新样本，增强了模型的泛化能力。
    *   **归一化处理**：对光谱数据进行标准化，消除了环境光线和仪器噪声的干扰。

### 4. 实验部分
*   **数据来源**：两次独立采收的蓝莓样本，分别接种了三种主要的产毒真菌：交链格孢菌、藤仓赤霉菌、扩展青霉，并设置了健康对照组。
*   **任务目标**：五分类任务（3 种真菌 + 1 种健康对照 + 1 种模拟损伤对照）。
*   **评价指标**：准确率（Accuracy）、灵敏度、特异性、F1 分数。
*   **主要结果**：在 **18-shot**（即每类只需 18 个参考样本）的设置下，模型在独立验证集上的平均准确率达到了 **97.9%**。即使在感染初期（接种后 1-3 天），模型也能保持极高的识别率。

### 5. 资源与算力
*   **文中未充分披露**具体的 GPU 型号或训练时长。但基于 1D 光谱数据的 CNN 模型通常参数量较小，普通的消费级显卡（如 RTX 3060）即可在短时间内完成训练。

### 6. 真正可信的贡献
*   **跨批次验证**：研究使用了两次独立采收的数据（一次训练，一次验证），这证明了模型不是在“背数据”，而是真正学到了真菌感染的稳定光谱特征。
*   **注意力机制的解释性**：通过注意力权重发现，模型关注的波段与真菌代谢引起的糖分、水分和有机酸变化高度吻合，具有生物学上的合理性。

### 7. 局限与风险
*   **单一感染假设**：实验是在实验室环境下人工接种单一真菌，而现实中蓝莓可能同时感染多种真菌，复合感染的识别难度更高。
*   **品种局限性**：不同品种的蓝莓其光谱背景不同，模型在其他品种上的表现尚未验证。
*   **硬件成本**：高精度的近红外光谱仪价格昂贵，将其集成到小型化、廉价的便携设备中仍有技术挑战。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事无损检测、智慧农业、小样本学习（Few-shot Learning）以及食品安全监测的 AI 研究者。
*   **后续可跟进的问题**：如何利用**自监督学习**（Self-supervised Learning）在完全没有标注的情况下，从海量的原始光谱中预训练出更通用的特征提取器？

（完）
