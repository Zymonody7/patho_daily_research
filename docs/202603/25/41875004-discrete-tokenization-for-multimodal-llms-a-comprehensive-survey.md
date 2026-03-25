---
title: "Discrete Tokenization for Multimodal LLMs: A Comprehensive Survey."
title_zh: 多模态大语言模型的离散分词：全面综述
authors: "Jindong Li, Yali Fu, Jiahong Liu, Linxiao Cao, Wei Ji, Menglin Yang, Irwin King, Ming-Hsuan Yang"
date: 2026-03-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/41875004/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 多模态大语言模型的离散标记化与语言处理
tldr: 多模态大模型在处理图像、音频等连续信号时，需将其转化为离散 Token 以适配语言模型架构。本文系统综述了以矢量量化（VQ）为核心的离散分词技术，通过对 8 种代表性 VQ 变体进行分类，深入探讨了其在模型对齐、推理和生成中的作用。该综述梳理了从传统应用到现代多模态大模型的演进路径，并总结了码本崩溃等核心挑战，为构建高效通用的多模态系统提供了关键参考。
selection_source: fresh_fetch
motivation: 旨在解决大语言模型难以直接处理连续多模态数据的问题，通过离散化技术实现异构模态与文本空间的统一表示。
method: 构建了首个针对大模型的离散分词分类体系，系统分析了 8 种矢量量化变体的算法原理、训练机制及其在多模态流水线中的集成方式。
result: 揭示了不同量化策略对模型对齐和生成性能的影响，并识别出码本崩溃、梯度估计不稳定及模态特定编码限制等关键技术挑战。
conclusion: 离散分词是实现通用多模态智能的基础，未来研究将向动态任务自适应量化、统一分词框架及生物启发式码本学习方向发展。
---

## 摘要
大语言模型（LLMs）的飞速发展增强了对有效机制的需求，即将连续的多模态数据转换为适用于基于语言处理的离散表示。离散分词（Discrete tokenization）以矢量量化（VQ）为核心方法，兼具计算效率和与 LLM 架构的兼容性。尽管其重要性日益增加，但目前仍缺乏一篇在基于 LLM 的系统背景下系统性考察 VQ 技术的全面综述。本研究填补了这一空白，首次提出了针对 LLM 设计的离散分词方法的结构化分类和分析。我们对跨越经典和现代范式的 8 种代表性 VQ 变体进行了分类，并分析了它们的算法原理、训练动态以及与 LLM 流水线集成的挑战。除了算法层面的研究外，我们还从不含 LLM 的经典应用、基于 LLM 的单模态系统以及基于 LLM 的多模态系统三个方面讨论了现有研究，重点阐述了量化策略如何影响对齐、推理和生成性能。此外，我们识别了关键挑战，包括码本崩溃（codebook collapse）、不稳定的梯度估计以及特定模态的编码约束。最后，我们讨论了新兴的研究方向，如动态和任务自适应量化、统一分词框架以及受生物启发的码本学习。本综述弥合了传统矢量量化与现代 LLM 应用之间的鸿沟，为开发高效且泛化能力强的多模态系统提供了基础参考。持续更新版本可在以下地址获取：https://github.com/jindongli-Ai/LLM-Discrete-Tokenization-Survey。

## Abstract
The rapid advancement of large language models (LLMs) has intensified the need for effective mechanisms to transform continuous multimodal data into discrete representations suitable for language-based processing. Discrete tokenization, with vector quantization (VQ) as a central approach, offers both computational efficiency and compatibility with LLM architectures. Despite its growing importance, there is a lack of a comprehensive survey that systematically examines VQ techniques in the context of LLM-based systems. This work fills this gap by presenting the first structured taxonomy and analysis of discrete tokenization methods designed for LLMs. We categorize 8 representative VQ variants that span classical and modern paradigms and analyze their algorithmic principles, training dynamics, and integration challenges with LLM pipelines. Beyond algorithm-level investigation, we discuss existing research in terms of classical applications without LLMs, LLM-based single-modality systems, and LLM-based multimodal systems, highlighting how quantization strategies influence alignment, reasoning, and generation performance. In addition, we identify key challenges including codebook collapse, unstable gradient estimation, and modality-specific encoding constraints. Finally, we discuss emerging research directions such as dynamic and task-adaptive quantization, unified tokenization frameworks, and biologically inspired codebook learning. This survey bridges the gap between traditional vector quantization and modern LLM applications, serving as a foundational reference for the development of efficient and generalizable multimodal systems. A continuously updated version is available at: https://github.com/jindongli-Ai/LLM-Discrete-Tokenization-Survey.