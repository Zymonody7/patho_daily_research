---
title: A foundation model for nucleotide sequences.
title_zh: 一种核苷酸序列的基础模型
authors: "Xilin Shen, Jia Xin Li, Meng Yang, Lei Shi, Kexin Chen, Xiangchun Li"
date: 2026-03-19
pdf: "https://pubmed.ncbi.nlm.nih.gov/41854075/"
tags: ["query:bioinfo"]
score: 10.0
evidence: 核苷酸序列及其注释的基础模型
tldr: 现有的基因组大模型多侧重于核苷酸序列本身，忽视了丰富的注释信息，限制了模型在跨物种和多生物场景下的泛化能力。为此，研究者推出了 OmniNA，这是一个在 9170 万条序列及其关联注释（共 1.07 万亿碱基）上训练的自监督生成式基础模型。通过联合学习序列语法与注释语义，OmniNA 在序列检测、物种分类等 23 个基准测试中达到 SOTA 或领先水平，并能有效揭示突变对 DNA/RNA 处理的影响，为基因组学研究提供了强大的预训练工具。
selection_source: fresh_fetch
motivation: 现有的基因组模型往往只关注核苷酸序列，未能充分利用序列相关的文本注释信息，导致模型对生物学语义的理解不足。
method: 提出 OmniNA 模型，通过自监督学习框架将 1.07 万亿碱基的核苷酸序列与其对应的 1.97 亿词量注释进行联合训练，实现序列与语义的互补表征。
result: 该模型在包括序列检测、物种分类在内的 23 项下游任务中表现优异，并能通过自然语言范式进行微调，准确预测基因突变对生物过程的影响。
conclusion: OmniNA 证明了整合注释信息的感知学习能显著提升核酸基础模型的泛化性，为基因组学和转录组学研究提供了通用的表征工具。
---

## 摘要
基础模型在多种下游任务中展现了卓越的性能。然而，在基因组学和转录组学中，核苷酸序列与其丰富注释的整合仍未得到充分探索，这可能限制了模型在不同物种和生物学背景下的泛化能力。在此，我们介绍了 OmniNA（全适用核酸基础模型），这是一个自监督生成式基础模型，在涵盖多种物种的 9170 万条核苷酸序列及其相关注释上进行了训练，总计包含 10762 亿个碱基和 1.97 亿个单词。与大多数仅关注功能基因组元件识别的现有方法不同，OmniNA 同时从序列和注释中学习，利用它们的互补性来增强语义理解和表示学习。我们证明了 OmniNA 能够捕捉序列语法和注释语义，从而促进在核苷酸级任务中的稳健迁移。OmniNA 可以在自然语言范式下进行微调，并在包括序列检测和物种分类在内的 23 个基准测试中达到了最先进或具有竞争力的性能。其学习到的表示还有助于揭示突变对 DNA 和 RNA 处理的影响。我们公开发布该模型，作为基因组学和转录组学研究的社区资源。OmniNA 通过整合注释感知学习，代表了推进基础建模迈出的一步，为基因组学和转录组学研究提供了一个强大的工具。

## Abstract
Foundation models have demonstrated exceptional performance across diverse downstream tasks. However, in genomics and transcriptomics, the integration of nucleotide sequences with their rich annotations remains underexplored, potentially limiting model generalizability across species and biological contexts. Here, we introduce OmniNA (Omni-applicable foundation model for nucleic acid), a self-supervised generative foundation model trained on 91.7 million nucleotide sequences and their associated annotations, totaling 1076.2 billion bases and 197 million words spanning diverse species. Unlike most existing approaches that focus solely on functional genomic element recognition, OmniNA jointly learns from both sequences and annotations, leveraging their complementarity to enhance semantic understanding and representation learning. We demonstrate that OmniNA captures sequence grammar and annotation semantics, facilitating robust transfer across nucleotide-level tasks. OmniNA can be fine-tuned under natural language paradigms and achieves state-of-the-art or competitive performance in 23 benchmarks, including sequence detection and species classification. Its learned representations also help reveal mutation effects on DNA and RNA processing. We release the model publicly as a community resource for genomics and transcriptomics research. OmniNA represents a step toward advancing foundational modeling by integrating annotation-aware learning, offering a powerful tool for genomics and transcriptomics research.