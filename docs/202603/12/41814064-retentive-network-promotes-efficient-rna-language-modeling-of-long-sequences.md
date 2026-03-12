---
title: Retentive Network promotes efficient RNA language modeling of long sequences.
title_zh: Retentive Network 促进了长序列的高效 RNA 语言建模
authors: "Yi Shen, Guangshuo Cao, Yueming Hu, Shilong Zhang, Jianghong Wu, Dijun Chen, Ming Chen"
date: 2026-03-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/41814064/"
tags: ["query:bioinfo"]
score: 10.0
evidence: 使用保留网络进行长序列RNA语言建模
tldr: 针对Transformer模型在处理长RNA序列时面临的O(n²)计算复杂度瓶颈，本研究提出了基于Retentive Network的RNA语言模型RNAret。该模型利用保留机制实现了线性复杂度的并行训练与低开销推理，并在2980万条RNA序列上完成了自监督预训练。实验结果显示，RNAret在RNA相互作用预测、二级结构预测及mRNA/lncRNA分类等任务中均优于现有模型，为长序列RNA的功能研究提供了高效的特征提取工具。
selection_source: fresh_fetch
motivation: Transformer架构的平方级计算复杂度限制了其在处理长链RNA序列时的效率和扩展性。
method: 开发了基于Retentive Network架构的RNAret模型，通过保留机制实现线性复杂度的长序列建模与并行化训练。
result: 在包含2980万条序列的大规模预训练后，模型在RNA相互作用、二级结构预测及分类等多个下游任务中取得了领先性能。
conclusion: RNAret证明了RetNet架构在RNA领域替代Transformer的潜力，能够更高效地提取长序列生物特征并推动RNA生物学研究。
---

## 摘要
RNA 序列的潜在特征对于理解其功能至关重要。因此，基于 Transformer 的核苷酸语言模型受到了广泛关注；然而，Transformer 的 O(n²) 复杂度限制了其处理长序列的能力。在这项工作中，我们提出了 RNAret，这是一种基于 Retentive Network 的 RNA 语言模型，它通过保留机制实现了训练并行化、低计算开销和长序列处理，且复杂度为 O(n)。我们在 2980 万条 RNA 序列上，使用自监督掩码语言建模方法对 RNAret 进行了预训练。实验证明了 RNAret 作为 RNA 语言模型的优势，在包括 RNA-RNA 相互作用预测、RNA 二级结构预测以及 mRNA/lncRNA 分类在内的一系列任务中均取得了优异的性能。RNAret 在提取 RNA 序列潜在特征和推进我们对 RNA 生物学的理解方面展现出巨大的潜力。

## Abstract
The latent features of RNA sequences are crucial for our understanding of their functions. Thus, Transformer-based nucleotide language models have received widespread attention; however, the O(n²) complexity of Transformer limits their ability to process long sequences. In this work, we propose RNAret, an RNA language model based on Retention Network, which achieves training parallelism, low computational overhead, and long-sequence processing through a retention mechanism, with O(n) complexity. We pretrain RNAret using a self-supervised masked language modeling approach on 29.8 million RNA sequences. Experiments demonstrate the merit of RNAret as an RNA language model, achieving superior performance on a range of tasks, including RNA-RNA interaction prediction, RNA secondary structure prediction, and mRNA/lncRNA classification. RNAret shows strong potential for extracting latent features from RNA sequences and advancing our understanding of RNA biology.