---
title: A geometric and probabilistic framework for mechanistic antifungal screening from colony morphology.
title_zh: 一种基于菌落形态的几何与概率框架，用于机制性抗真菌筛选。
authors: "Ezekiel Ahn, Insuck Baek, Seunghyun Lim, Amelia Lovelace, Masoud Kazem-Rostami, Helen Ngo, Richard D Ashby, Minhyeok Cha, Moon S Kim, Sunchung Park, Lyndel W Meinhardt"
date: 2026-08-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/42046385/"
tags: ["query:pathoai"]
score: 7.0
evidence: 用于抗真菌药物筛选的几何与概率框架
tldr: 针对传统杀菌剂筛选仅依赖生长抑制标量（如MIC）而忽略几何失效模式的问题，本文提出了一种基于菌落形态的几何概率框架。该框架通过计算效价坐标λ、极性坐标I及失效概率p，将常规菌落图像转化为可量化的机制描述语言。实验证明该方法能有效区分效价与极性相关的失效模式，为杀菌剂候选物的机制化筛选和优先级排序提供了新工具。
selection_source: fresh_fetch
motivation: 现有的杀菌剂筛选指标如EC50仅能反映生长抑制程度，无法提供与菌落几何形状相关的生长方向和极性失效信息。
method: 构建了λ-I-p几何概率框架，通过菌落面积存活率定义效价坐标λ，通过长宽比变化定义极性坐标I，并结合Clopper-Pearson置信区间估计失效概率。
result: 实验发现酰胺类候选物在抑制生长的同时显著诱导了极性破坏，且该框架在UV-C暴露梯度实验中展现出一致的剂量依赖性轨迹。
conclusion: 该框架将菌落图像转化为一种通用的筛选语言，实现了对杀菌剂作用强度、几何形变及失效频率的综合评估。
---

## 摘要
背景：杀真菌剂的发现仍严重依赖于标量筛选终点 [例如抑菌圈、半最大效应浓度 (EC50) 或最小抑菌浓度 (MIC)]，这些指标总结了生长抑制情况，但提供的几何相关失效模式信息有限，从而限制了早期筛选过程中的机制优先级排序。由于菌落形态编码了生长方向和极性，我们开发了一个几何与概率筛选框架，以区分可可和咖啡相关病原体中的效力与极性相关失效模式。结果：通过常规菌落图像，我们计算了固定剂量效力坐标 λ（面积存活率的负自然对数）和极性坐标 I（长宽比的自然对数倍数变化，处理组/对照组）。随后，我们在操作阈值 τ = 1.10 下估算了极性破坏事件概率 (p̂)，并给出了精确的 95% Clopper-Pearson 置信区间，同时在 τ = 1.10-1.20 范围内进行了灵敏度分析。在针对 9 个分离株和 4 种酚类支链酰胺/酸候选药物的单剂量初筛中，酰胺类药物一致聚集在 (+λ, +I) 象限，表明其作用方向相对于酸类类似物具有同时抑制生长和破坏极性的特征。最强的组合是经 PhSOAM 处理的 CGH5 (λ = 0.67)，该组合也显示出较高的形状破坏概率 (p̂ = 0.75; 95% CI 0.43-0.95)。基于椭圆的轴向重建将 I 与特定轴的收缩率联系起来，并与直接基于长度和宽度的比率高度一致。对独立的 UV-C 暴露时间梯度（0-30 分钟）的重新分析产生了连贯的剂量依赖性 λ(d) 和 I(d) 轨迹，并支持在约 10 分钟时进行事件级推断。结论：λ-I-p 语法将菌落图像转换为一种与仪器无关的筛选语言，描述了干预措施在测试条件下的作用强度 (λ)、是否与极性相关的几何变化有关 (I) 以及定义的失效模式发生的频率 (p̂)，从而支持候选杀真菌剂的机制筛选和优先级排序。2026 年发表。本文为美国政府作品，在美国属于公有领域。

## Abstract
BACKGROUND: Fungicide discovery still relies heavily on scalar screening endpoints [e.g. inhibition zones, median effective concentration (EC50) or minimum inhibitory concentration (MIC)] that summarize growth suppression but provide limited information about geometry-linked failure modes, constraining mechanistic prioritization during early screening. Because colony morphology encodes growth direction and polarity, we developed a geometric and probabilistic screening framework to separate potency from polarity-linked failure modes in cacao- and coffee-relevant pathogens. RESULTS: From routine colony images, we computed a fixed-dose potency coordinate, λ, as the negative natural log of the area survival ratio, and a polarity coordinate, I, as the natural log fold-change in length-to-width ratio (treated/control). We then estimated polarity-disruption event probability (p̂) with exact 95% Clopper-Pearson confidence bounds at an operational threshold of τ = 1.10, with sensitivity analysis across τ = 1.10-1.20. In a single-dose primary screen across nine isolates and four phenolic-branched amide/acid candidates, amides consistently clustered in the (+λ, +I) quadrant, indicating an action direction characterized by concurrent growth suppression and polarity disruption relative to the acid analogues. The strongest combination was CGH5 treated with PhSOAM (λ = 0.67), which also showed high shape-disruption probability (p̂ = 0.75; 95% CI 0.43-0.95). Ellipse-based axis reconstruction linked I to axis-specific contraction ratios and showed strong agreement with direct length- and width-based ratios. Re-analysis of an independent UV-C exposure-time gradient (0-30 min) produced coherent dose-dependent λ(d) and I(d) trajectories and supported event-level inference at ~10 min. CONCLUSION: The λ-I-p grammar converts colony images into an instrument-agnostic screening language describing how strongly an intervention acts at the tested condition (λ), whether it is associated with polarity-linked geometry change (I) and how often a defined failure mode occurs (p̂), thereby supporting mechanistic screening and prioritization of candidate fungicides. Published 2026. This article is a U.S. Government work and is in the public domain in the USA.