---
title: Adaptive diagnostic reasoning framework for pathology with multimodal large language models.
title_zh: 基于多模态大语言模型的病理学自适应诊断推理框架
authors: "Yunqi Hong, Kuei-Chun Kao, Liam Edwards, Nein-Tzu Liu, Chung-Yen Huang, Alex Oliveira-Kowaleski, Cho-Jui Hsieh, Neil Y C Lin"
date: 2026-03-07
pdf: "https://pubmed.ncbi.nlm.nih.gov/41794962/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 多模态大语言模型用于病理诊断推理
tldr: "针对病理诊断中AI模型透明度不足、难以审计的问题，该研究提出了一种基于多模态大语言模型（MLLM）的自适应诊断推理框架。通过两阶段自学习过程，模型能从少量标注数据中提取诊断标准并生成与专家共识一致的循证推理描述。实验证明，该框架在乳腺癌和前列腺癌诊断中准确率超过90%，能有效识别复杂亚型，为临床提供可审计、高可信度的AI辅助诊断方案。"
selection_source: fresh_fetch
motivation: 现有的病理AI系统多为不透明的“黑盒”，缺乏可解释的推理过程，导致临床应用受限。
method: 利用多模态大模型在不更新权重的情况下，通过两阶段自学习从少量样本中提取诊断标准，并结合病理专家反馈生成结构化推理。
result: "该框架在区分正常组织与浸润性癌方面达到90%以上准确率，并能自主识别核异型性等关键组织学特征以区分复杂癌症亚型。"
conclusion: 该研究通过将视觉理解与逻辑推理结合，实现了从黑盒分类器向可审计、循证式医疗AI系统的转变。
---

## 摘要
背景：人工智能提升了病理筛查的效率，但由于大多数系统作为不透明的黑盒运行，其临床应用仍然受限。我们旨在通过建立一个能够生成透明且与证据挂钩的推理框架来解决这种不透明性，从而支持诊断审计。方法：我们提出了一个框架，使现成的多模态大语言模型从被动的模式识别转向主动的诊断推理。通过使用乳腺癌和前列腺癌数据集中的少量标记子集，我们采用两阶段自学习过程来推导诊断标准，且无需更新模型权重。我们整合了资深病理学家的专家反馈，以确保生成的描述符合既定的医学标准。结果：研究表明，我们的框架在区分正常组织与浸润性癌方面达到了 90% 以上的准确率，同时生成了可供审计的依据。除了二元分类，该模型还能通过自主识别包括核不规则性和结构破坏在内的标志性组织学特征，有效区分导管原位癌等复杂亚型。这些计算机生成的描述与专家评估高度吻合。我们的方法相比传统基准模型实现了显著的性能提升，并能有效适应不同的组织类型和独立的基座模型。结论：通过将视觉理解与推理相结合，我们的框架为构建临床可信的人工智能提供了一种有前景的方法。该框架有助于弥合不透明分类器与可审计系统之间的鸿沟，为医疗工作流中基于证据的解释提供了一条可行路径。

## Abstract
BACKGROUND: Artificial intelligence enhances pathology screening efficiency, yet clinical adoption remains limited because most systems operate as opaque black boxes. We aim to resolve this opacity by establishing a framework that generates transparent, evidence-linked reasoning to support diagnostic auditing. METHODS: We present a framework that shifts off-the-shelf multimodal large language models from passive pattern recognition to active diagnostic reasoning. Using small labeled subsets from breast and prostate cancer datasets, we employ a two-phase self-learning process to derive diagnostic criteria without updating model weights. We integrate expert feedback from board-certified pathologists to ensure the generated descriptions align with established medical standards. RESULTS: Here we show that our framework produces audit-ready rationales while achieving over 90% accuracy in distinguishing normal tissue from invasive carcinoma. Beyond binary classification, the model effectively differentiates complex subtypes like ductal carcinoma in situ by autonomously identifying hallmark histological features, including nuclear irregularities and structural disruption. These computer-generated descriptions closely match expert assessments. Our approach delivers substantial performance gains over conventional baselines and adapts effectively across diverse tissue types and independent foundation models. CONCLUSIONS: By uniting visual understanding with reasoning, our framework provides a promising approach for clinically trustworthy artificial intelligence. This framework helps bridge the gap between opaque classifiers and auditable systems, suggesting a viable path toward evidence-linked interpretation in medical workflows.