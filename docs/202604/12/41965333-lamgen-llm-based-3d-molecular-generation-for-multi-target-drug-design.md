---
title: "LaMGen: LLM-based 3D molecular generation for multi-target drug design."
title_zh: LaMGen：基于大语言模型的多靶点药物设计 3D 分子生成
authors: "Qun Su, Qiaolin Gou, Hui Zhang, Jike Wang, Huiyong Sun, Renling Hu, Rui Qin, Huanxiang Liu, Tingjun Hou, Yu Kang"
date: 2026-04-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/41965333/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 基于大语言模型的3D分子生成用于多靶点药物设计
tldr: 针对多靶点药物设计中现有方法缺乏生物背景且泛化性差的问题，LaMGen 提出了一种基于大语言模型（LLM）的 3D 分子生成框架。该框架利用包含 60 万量子精度构象和 70 万多靶点关联的 MTD2025 数据集，结合 ESM-C 蛋白质嵌入和旋转感知令牌，实现了高精度、低能耗的分子构象生成。实验表明，LaMGen 在生成速度（0.44s）和分子性质上优于扩散模型，能有效发现具有高结合亲和力的创新候选药物。
selection_source: fresh_fetch
motivation: 传统多靶点药物设计过度依赖配体相似性而忽视了复杂的蛋白质环境，导致模型在处理新靶点组合时泛化能力不足。
method: 构建了大规模多靶点数据集 MTD2025，并开发了集成蛋白质嵌入、旋转感知配体表示及三元耦合注意力机制的 LLM 架构。
result: 在独立基准测试中，该模型生成分子的速度比扩散模型快且质量更高，能够精准复现已知活性分子并发现结构新颖的高亲和力药物。
conclusion: LaMGen 证明了利用大语言模型处理复杂的 3D 多靶点药物设计任务的可行性，为高效开发复杂疾病药物提供了新工具。
---

## 摘要
多靶点药物在治疗复杂疾病方面具有巨大潜力，但现有方法主要依赖于基于配体的方法，缺乏足够的生物学背景，且通常局限于特定的靶点对，导致泛化能力有限。在此，我们介绍了 LaMGen，这是一个由大语言模型（LLM）驱动的通用多靶点药物设计框架。LaMGen 基于 MTD2025 数据集构建，该数据集包含超过 60 万个具有量子级精度的分子构象和 70 万个多靶点关联，能够直接生成具有量子级精度的能量有利构象。该框架集成了 ESM-C 蛋白质嵌入、旋转感知配体 token 以及 TriCoupleAttention 模块，用以捕捉多层级的靶点-配体相互作用。在独立基准测试中，LaMGen 在多项属性上优于基于扩散的模型，平均生成分子仅需 0.44 秒，同时保持了极高的构象合理性。回顾性分析表明，LaMGen 不仅能重现与已知活性药物相同的分子，还能持续产生具有保守核心支架和更优结合亲和力的结构新颖候选药物。

## Abstract
Multi-target drugs hold great promise for treating complex diseases, yet existing methodologies predominantly rely on ligand-based approaches, which lack sufficient biological context and are often confined to specific target pairs, resulting in limited generalizability. Here, we introduce LaMGen, a general-purpose multi-target drug design framework powered by large language models (LLMs). Built on MTD2025, a dataset comprising over 600,000 quantum-accurate molecular conformations and 700,000 multi-target associations, LaMGen directly yields energy-favorable conformations with quantum-level accuracy. The framework integrates ESM-C protein embeddings, rotation-aware ligand tokens, and a TriCoupleAttention module to capture multi-level target-ligand interactions. Across independent benchmarks, LaMGen outperforms diffusion-based model across multiple properties, generating molecules in an average of 0.44 s, while preserving high conformational plausibility. Retrospective analyses demonstrate that LaMGen not only can reproduce molecules identical to known actives, but also consistently produces structurally novel candidates with conserved core scaffolds and superior binding affinities.