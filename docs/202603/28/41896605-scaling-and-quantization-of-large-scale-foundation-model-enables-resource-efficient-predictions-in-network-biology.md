---
title: Scaling and quantization of large-scale foundation model enables resource-efficient predictions in network biology.
title_zh: 大规模基础模型的扩展与量化实现了网络生物学中资源高效的预测。
authors: "Han Chen, Madhavan S Venkatesh, Javier Gόmez Ortega, Siddharth V Mahesh, Tarak N Nandi, Ravi K Madduri, Karin Pelka, Christina V Theodoris"
date: 2026-03-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/41896605/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于网络生物学和单细胞转录组的基础模型
tldr: "针对网络生物学基础模型随数据规模增大导致计算资源消耗剧增的问题，本研究构建了包含1.04亿个人类单细胞转录组的大规模数据集，并训练了不同规模的模型以确立缩放法则。通过引入模型量化技术，在保持生物学知识表达能力的同时，将微调时间缩短至15%，内存占用降至34%，实现了在资源受限环境下高效进行单细胞下游任务预测。"
selection_source: fresh_fetch
motivation: 随着预训练数据和模型规模的扩大，网络生物学基础模型在微调和推理过程中的计算资源需求变得难以负担。
method: 汇集1.04亿个单细胞转录组数据进行大规模预训练，并利用模型量化技术压缩模型参数以降低计算开销。
result: 量化后的模型在零样本学习和微调任务中保持了与全精度模型相当的性能，且显著降低了训练时间和内存消耗。
conclusion: 模型量化是实现资源高效型生物基础模型微调与推理的有效途径，能在不损失生物学洞察力的前提下提升模型可用性。
---

## 摘要
网络生物学基础模型在大规模生物数据上进行预训练，通过迁移学习在多种下游任务中实现上下文感知预测。然而，随着可用预训练数据的扩展，模型规模的增加也提高了下游应用中微调和推理所需的计算资源。在本研究中，我们首先构建了一个包含来自广泛组织和疾病的约1.04亿个人类单细胞转录组的语料库，并预训练了规模逐渐增大的模型，定义了转录掩码学习的缩放法则。随后，我们证明了模型量化保留了全精度模型的上下文基因和细胞嵌入空间，在零样本和微调应用中达到了相当的性能，而在相同批次大小下进行微调时，仅需全精度模型15%的时间和34%的内存。总的来说，模型量化是一种在保留生物学知识的同时实现资源高效微调和推理的有效方法。

## Abstract
Foundation models for network biology are pretrained on large-scale biological data to enable context-aware predictions in a diverse array of downstream tasks through transfer learning. However, increasing model sizes with the expansion of available pretraining data also increases the computational resources required for fine-tuning and inference in downstream applications. Here we first assemble a corpus comprising ~104 million human single-cell transcriptomes from a broad range of tissues and diseases and pretrain successively larger models, defining the scaling laws for transcriptional masked learning. We then demonstrate that model quantization preserves the contextual gene and cell embedding space of the full-precision model, matching performance in zero-shot and fine-tuning applications while requiring only 15% of the time and 34% of the memory as the full model for fine-tuning with the same batch size. Overall, model quantization represents an effective method for resource-efficient fine-tuning and inference while preserving biological knowledge.