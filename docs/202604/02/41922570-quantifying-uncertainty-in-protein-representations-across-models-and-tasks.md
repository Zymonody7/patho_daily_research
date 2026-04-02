---
title: Quantifying uncertainty in protein representations across models and tasks.
title_zh: 量化跨模型和任务的蛋白质表示不确定性
authors: "R Prabakaran, Yana Bromberg"
date: 2026-04-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/41922570/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 蛋白质语言模型和生物分子嵌入的评估
tldr: 蛋白质语言模型生成的嵌入向量应用广泛，但其表示的可靠性缺乏量化评估。本研究提出一种模型无关的评分框架，通过计算蛋白质在潜空间近邻中非生物“合成”序列的比例来衡量不确定性。实验证明，该方法能有效识别无法捕捉生物特征的低质量嵌入，通过在下游任务前进行筛选，显著提升了生物特性预测的可靠性。
selection_source: fresh_fetch
motivation: 现有的蛋白质嵌入向量缺乏对其表示生物信息准确性的评估手段，导致下游任务可能基于不可靠的特征进行推断。
method: 提出一种通过计算蛋白质在潜空间近邻中“合成序列”占比来量化嵌入不确定性的评分框架。
result: 发现低质量的嵌入向量在向量属性上与随机序列无法区分，而该框架能有效识别并剔除这些不可靠的表示。
conclusion: 该研究为蛋白质语言模型的可靠性评估提供了首个量化标准，建议在科学领域的语言模型应用中推广此类嵌入质量筛查。
---

## 摘要
生物分子嵌入作为序列和结构的有效表示，能够实现相似性搜索、结构和功能预测以及生物物理性质评估等任务。然而，在不评估嵌入准确表示生物分子能力的情况下依赖它们是一个关键缺陷——这类似于在手术中使用手术刀而不验证其锋利程度。在此，我们提出了一种评估蛋白质语言模型编码生物学意义信息能力的方法。对于每种蛋白质，表示不确定性被评分为其在潜空间最近邻中非生物“合成”序列所占的比例。我们的分析表明，低质量的嵌入通常无法捕捉到有意义的生物学特征，表现出的向量属性与随机生成的序列无法区分。据我们所知，我们的模型无关评分框架是第一个量化蛋白质序列嵌入可靠性的框架。它支持在下游应用和推理之前进行嵌入筛选，从而显著提高其可靠性。我们建议，在科学领域的其他语言模型应用中也应进行嵌入评估。

## Abstract
Biomolecular embeddings serve as efficient representations of sequence and structure, enabling tasks such as similarity searches, structure and function prediction and estimation of biophysical properties. However, relying on embeddings without assessing their ability to accurately represent biomolecules is a critical flaw-akin to using a scalpel in surgery without verifying its sharpness. Here we propose a means to evaluate the capacity of protein language models to encode biologically meaningful information. For each protein, representation uncertainty is scored as the fraction of non-biological 'synthetic' sequences among its nearest neighbors in latent space. Our analysis reveals that low-quality embeddings often fail to capture meaningful biology, displaying vector properties indistinguishable from those of randomly generated sequences. Our model-agnostic scoring framework is, to our knowledge, the first to quantify protein sequence embedding reliability. It enables embedding screening prior to downstream applications and inferences, significantly improving their reliability. We propose that embedding evaluation should be undertaken for other uses of language models in science as well.