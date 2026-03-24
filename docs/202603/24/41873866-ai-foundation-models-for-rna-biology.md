---
title: AI foundation models for RNA biology.
title_zh: RNA生物学中的AI基础模型
authors: "Haopeng Yu, Yiliang Ding"
date: 2026-03-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/41873866/"
tags: ["query:bioinfo"]
score: 10.0
evidence: 用于 RNA 生物学的 AI 基础模型
tldr: RNA生物学正经历AI大模型带来的变革。针对RNA序列、结构与功能之间复杂的映射难题，研究者利用数百万跨物种RNA数据进行自监督预训练，构建出具备通用表征能力的基座模型。通过微调，这些模型能精准预测功能规则，并结合可解释AI技术挖掘顺式作用元件等生物学基元，为解码生命调控规律提供了强有力的计算工具。
selection_source: fresh_fetch
motivation: 传统的实验方法难以高效解析海量RNA序列中蕴含的复杂结构与功能调控规律。
method: 综述了利用数百万跨物种RNA序列进行自监督预训练，并结合特定架构创新与微调策略构建基座模型的方法。
result: 总结了模型在预测RNA功能、识别结构基元及顺式调控元件等任务中的表现，并强调了可解释性AI在发现新生物学规律中的作用。
conclusion: RNA基座模型正通过整合多模态数据，从黑盒预测器演变为揭示生命遗传信息调控机制的核心发现工具。
---

## 摘要
RNA生物学正经历着由AI基础模型驱动的变革性革命。这些模型通过在涵盖不同物种、数百万个RNA分子的海量多样化数据集上进行训练，学习RNA序列、结构与功能之间复杂的相互关系。通过对这些序列进行自监督学习，这些模型获得了对RNA的可泛化理解，随后可针对各种下游任务进行微调，从而实现对嵌入在RNA序列中的功能规则的解码。在本综述中，我们提供了RNA基础模型的全面指南。结合RNA生物学的具体实例，我们从基础模型的概念出发，回顾了预训练数据集、架构创新、自监督策略以及微调方法的重要性，这些方法使得通用的RNA表征能够转化为特定任务的模型。至关重要的是，我们强调了可解释人工智能（XAI）方法如何将这些模型从黑盒预测器转变为有价值的发现工具，从而揭示候选的顺式作用调节元件和结构基序。随着RNA基础模型的不断进步以及更多多模态生物数据的整合，它们旨在揭示编码在RNA中的更多调控规则和功能。

## Abstract
RNA biology is undergoing a transformative revolution driven by AI foundation models. These models learn the intricate relationships between RNA sequence, structure, and function by training on vast, diverse datasets spanning millions of RNA molecules across various species. Through self-supervised learning on these sequences, these models acquire a generalizable understanding of RNA, which can then be fine-tuned for various downstream tasks, thereby enabling the decoding of functional rules embedded in RNA sequences. In this review, we provide a comprehensive guide to RNA foundation models. Using concrete examples of RNA biology, we begin with the concept of foundation models and review the importance of pre-training datasets, architectural innovations, self-supervised strategies, and fine-tuning approaches that allow general RNA representations to be translated into task-specific models. Crucially, we highlight how explainable AI (XAI) methods transform these models from black-box predictors into valuable discovery tools that reveal candidate cis-regulatory elements and structural motifs. As RNA foundation models keep advancing and integrating more multimodal biological data, they aim to uncover additional regulatory rules and functions encoded in RNA.