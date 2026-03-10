---
title: DNA-Logic Trimodal Biofuel Cell Platform for AI-Assisted Dual Pathogen Detection.
title_zh: 用于人工智能辅助双重病原体检测的 DNA 逻辑三模态生物燃料电池平台
authors: "Wen T, Jin C, Chen H, Wu Q, Wang K, Feng D, Wang H, Huang KJ, Diao K, Tan X., Tao Wen, Chenchen Jin, Haiyan Chen, Qingnian Wu, Kaili Wang, Defen Feng, Haibo Wang, Ke-Jing Huang, Kaisheng Diao, Xuecai Tan"
date: 2026-03-09
pdf: "https://pubmed.ncbi.nlm.nih.gov/41802090/"
tags: ["query:pathoai"]
score: 9.0
evidence: 利用DNA逻辑电路进行AI辅助的双重病原体检测
tldr: 针对甘蔗黑穗病和梢腐病检测依赖实验室、耗时长的问题，该研究开发了一种基于DNA逻辑门控的三模态自供电生物传感平台。该平台集成电化学、比色和光热信号，通过DNA逻辑电路实现双病原体并行检测，并利用随机森林回归模型进行AI辅助数据处理。实验证明其检测限达亚飞摩尔级，且在田间样本测试中表现出与qPCR高度一致的准确性，为智慧农业提供了低成本、便携的现场筛查方案。
selection_source: fresh_fetch
motivation: 传统的qPCR检测技术难以满足甘蔗病害现场快速筛查的需求，亟需一种便携、多模态且无需外部电源的检测系统。
method: 构建了一个由DNA逻辑电路驱动的自供电平台，通过目标DNA触发酶释放或纳米酶活化，产生电、色、热三种信号，并结合随机森林算法进行多维度数据融合分析。
result: 该系统对两种病原体的检测限分别低至3.7 × 10^-16 M和2.3 × 10^-16 M，且机器学习模型的预测准确率（R2）最高可达1.000。
conclusion: 该研究证明了DNA逻辑电路与多模态传感及AI算法结合的可行性，为复杂环境下的多病原体现场快速检测提供了通用策略。
---

## 摘要
开发了一种 DNA 逻辑门控、三模态、自供电的生物传感平台，用于快速、同步和现场检测两种主要的甘蔗病原体：甘蔗黑粉菌（smut）和甘蔗梢腐病菌（pokkah boeng）。传统的诊断技术（如 qPCR）被认为耗时、依赖实验室且不适合现场部署。为了克服这些局限性，所提出的设备将电化学、比色和光热信号读取集成到一个便携式系统中，由酶生物燃料电池供电，并通过智能手机界面进行操作。传感机制由特定目标的 DNA 逻辑电路协调。在存在黑粉菌 DNA 的情况下，葡萄糖氧化酶被释放，在基于亚甲基蓝的电解质中产生电化学电流和颜色变化。对于梢腐病菌，AuCo 纳米酶被激活，催化 TMB 氧化产生蓝色，并在近红外（NIR）激光照射下产生独特的光热响应。两条路径正交触发，互不干扰。多模态信号使用机器学习辅助的随机森林回归模型进行处理。黑粉菌检测模型在学习率为 0.024、训练数据分配为 63% 的情况下，R2 值达到 0.982；而梢腐病菌检测模型在学习率为 0.001、训练数据分配为 90% 的情况下，达到了完美的准确度（R2 = 1.000）。该平台表现出高灵敏度，黑粉菌的检测限低至 3.7 × 10-16 M，梢腐病菌的检测限低至 2.3 × 10-16 M，并具有优异的重复性和稳定性。使用从受感染甘蔗植株采集的田间样本进行的验证显示，与标准 qPCR 检测高度一致。该系统为疾病早期预警提供了一种强大、低成本且用户友好的工具，代表了智慧农业框架下多重病原体筛选的通用策略。

## Abstract
A DNA-logic-gated, trimodal, self-powered biosensing platform is developed for the rapid, simultaneous, and on-site detection of two major sugarcane pathogens, Sporisorium scitamineum (smut) and Fusarium sacchari (pokkah boeng). Conventional diagnostic techniques such as qPCR are considered time-consuming, laboratory-dependent, and unsuitable for field deployment. To overcome these limitations, the proposed device integrates electrochemical, colorimetric, and photothermal signal readouts into a single portable system, powered by an enzymatic biofuel cell and operated via a smartphone interface. The sensing mechanism is orchestrated by target-specific DNA logic circuits. In the presence of smut DNA, glucose oxidase is released, generating an electrochemical current and a color shift in a methylene blue-based electrolyte. For pokkah boeng, an AuCo nanozyme is activated, catalyzing the oxidation of TMB to yield a blue color and a distinct photothermal response under NIR laser irradiation. Both pathways are triggered orthogonally without cross-interference. Multimodal signals are processed using a machine learning-assisted random forest regression model. The smut detection model achieves an R2 value of 0.982 with a learning rate of 0.024 and 63% training data allocation, while the pokkah boeng model attains perfect accuracy (R2 = 1.000) at a learning rate of 0.001 and a 90% training split. The platform demonstrates high sensitivity, with detection limits as low as 3.7 × 10-16 M for smut and 2.3 × 10-16 M for pokkah boeng, along with excellent repeatability and stability. Validation using field samples collected from infected sugarcane plants shows high consistency with standard qPCR assays. The system provides a powerful, low-cost, and user-friendly tool for early disease warning and represents a universal strategy for multiplex pathogen screening in smart agriculture frameworks.