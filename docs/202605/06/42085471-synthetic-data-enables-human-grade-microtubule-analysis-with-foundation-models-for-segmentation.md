---
title: Synthetic data enables human-grade microtubule analysis with foundation models for segmentation.
title_zh: 合成数据利用分割基础模型实现人类水平的微管分析
authors: "Mario Koddenbrock, Justus Westerhoff, Dominik Fachet, Simone Reber, Felix A Gers, Erik Rodner"
date: 2026-05-05
pdf: "https://pubmed.ncbi.nlm.nih.gov/42085471/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 用于微管分割的基础模型
tldr: 微管分割对研究细胞功能至关重要，但长期受限于人工标注的高成本和数据集匮乏。本研究通过模拟真实干涉反射显微图像，构建了无需人工标注的合成数据集 SynthMT。实验证明，利用仅 10 张合成图像进行超参数优化后，SAM3Text 模型在真实数据上达到了接近甚至超越人类的分割精度，为生物医学丝状结构的自动化分析提供了高效方案。
selection_source: fresh_fetch
motivation: 针对微管结构分析中人工标注耗时耗力且缺乏大规模标注数据集的现状，寻求一种无需人工干预的自动化分割评估与优化方法。
method: 开发了一种新型图像生成管线，通过模拟真实干涉反射显微镜下的微管特征生成 SynthMT 合成数据集，并以此指导分割基础模型的超参数优化。
result: 实验表明，经过少量合成数据优化的 SAM3Text 模型在处理未见过的真实微管图像时，其分割准确率达到了人类专家级别甚至更高。
conclusion: 研究证实了结合合成数据与基础模型可以有效解决复杂生物图像的自动化分析难题，并公开了数据集和评估框架以促进后续研究。
---

## 摘要
研究微管 (MTs) 及其力学特性对于理解细胞内运输、细胞分裂和药物作用至关重要。尽管其重要性不言而喻，专家仍需花费大量时间手动分割这些丝状结构。由于缺乏大规模标注数据集，目前无法系统地评估最先进方法在此任务中的适用性。我们通过引入合成数据集 SynthMT 填补了这一空白，该数据集是通过在体外重组微管的真实干扰反射显微镜 (IRM) 帧上调整一种新型图像生成流水线而产生的，无需人工标注。在我们的基准测试中，我们在零样本和基于超参数优化 (HPO) 的少样本设置下评估了九种全自动微管分析方法。在这两种设置下，经典算法和当前的基础模型在人类视觉上认为简单的体外微管 IRM 图像上，仍难以达到生物学下游分析所需的准确度。然而，最近推出的 SAM3 模型是一个显著的例外。仅在十张随机 SynthMT 图像上进行 HPO 后，其文本提示版本 SAM3Text 在未见的真实数据上实现了近乎完美、甚至在某些情况下超越人类的表现。这表明，当方法配置得到合成数据的有效引导时，全自动微管分割已变得可行。为了推动进展，我们公开了该数据集、生成流水线和评估框架。

## Abstract
Studying microtubules (MTs) and their mechanical properties is central to understanding intracellular transport, cell division, and drug action. While important, experts still need to spend many hours manually segmenting these filamentous structures. The suitability of state-of-the-art methods for this task cannot be systematically assessed, as large-scale labeled datasets are missing. We address this gap by introducing the synthetic dataset SynthMT, produced by tuning a novel image generation pipeline on real-world interference reflection microscopy (IRM) frames of in vitro reconstituted MTs without requiring human annotations. In our benchmark, we evaluate nine fully automated methods for MT analysis in both zero- and Hyperparameter Optimization (HPO)-based few-shot settings. Across both settings, classical algorithms and current foundation models still struggle to achieve the accuracy required for biological downstream analysis on in vitro MT IRM images that humans perceive as visually simple. However, a notable exception is the recently introduced SAM3 model. After HPO on only ten random SynthMT images, its text-prompted version SAM3Text achieves near-perfect and in some cases super-human performance on unseen, real data. This indicates that fully automated MT segmentation has become feasible when method configuration is effectively guided by synthetic data. To enable progress, we publicly release the dataset, the generation pipeline, and the evaluation framework.