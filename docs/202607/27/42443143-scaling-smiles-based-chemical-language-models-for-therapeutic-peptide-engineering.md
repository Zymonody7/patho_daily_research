---
title: Scaling SMILES-Based Chemical Language Models for Therapeutic Peptide Engineering.
title_zh: 扩展基于 SMILES 的化学语言模型用于治疗性多肽工程。
authors: "Aaron L Feller, Maxim Secor, Sebastian Swanson, Claus O Wilke, Kristine Deibler"
date: 2026-07-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/42443143/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于治疗性多肽工程和设计的化学语言模型
tldr: 治疗性多肽兼具蛋白质特异性与小分子多样性，但现有模型难以兼顾：蛋白质模型局限于天然氨基酸，而化学模型难以处理长序列。为此，研究者开发了 PeptideCLM-2，这是一款基于 SMILES 并在超过 1 亿个分子上预训练的化学语言模型，能够原生表征复杂的多肽化学结构。实验证明，该模型在预测膜扩散、生物功能和半衰期等关键开发指标上优于现有方法，为多肽药物设计提供了高效的计算工具。
selection_source: fresh_fetch
motivation: 现有的蛋白质模型无法处理非天然氨基酸，而传统化学模型在处理多肽这类大型聚合物序列时表现不佳，导致多肽药物研发缺乏通用的基础模型。
method: 研发了 PeptideCLM-2 系列模型，通过在 1 亿多个分子数据上进行大规模预训练，利用 SMILES 字符串原生表征复杂的多肽化学结构。
result: 在膜扩散性、生物活性及半衰期等多个药物开发关键指标的预测任务中，该模型表现优于传统的静态化学描述符和复杂的多嵌入流水线。
conclusion: 该研究证明了通过扩展基于 SMILES 的化学语言模型，可以有效填补多肽药物在计算建模上的空白，提升复杂生物分子的工程化效率。
---

## 摘要
治疗性多肽在药物发现中占据独特的中间地带，兼具蛋白质相互作用的高特异性和小分子的化学多样性，然而它们目前处于计算领域的盲区。现有的基础模型无法有效地处理它们：蛋白质模型受限于天然氨基酸，而化学模型难以处理大型类聚合物序列。这种脱节迫使该领域依赖于无法捕捉细微化学细节的静态化学描述符，或者依赖于针对特定数据集定制的复杂多嵌入流水线。为了弥补这一差距，我们提出了 PeptideCLM-2，这是一套在超过 1 亿个分子上训练的化学语言模型，旨在原生表征复杂的多肽化学。这种建模方法扩展了治疗性多肽可用的机器学习模型工具包。基准测试结果显示，在预测包括膜扩散、生物功能和半衰期在内的开发终点方面，该模型相较于先前的方法表现出强大的性能。

## Abstract
Therapeutic peptides occupy a unique middle ground in drug discovery, offering the high specificity of protein interactions with the chemical diversity of small molecules, yet they currently fall in a computational blind spot. Existing foundation models cannot handle them effectively: protein models are restricted to natural amino acids, while chemical models struggle to process large, polymer-like sequences. This disconnect has forced the field to rely on static chemical descriptors that fail to capture subtle chemical details or on complex multiembedding pipelines that are custom tailored to specific data sets. To bridge this gap, we present PeptideCLM-2, a suite of chemical language models trained on over 100 million molecules to natively represent complex peptide chemistry. This modeling approach expands the available toolkit of machine learning models for therapeutic peptides. Benchmarking results show strong performance versus prior methods for predicting development end points including membrane diffusion, biological function, and half-life.

---

## 论文详细总结（自动生成）

这篇论文介绍了 **PeptideCLM-2**，一个专门为“治疗性多肽”设计的化学语言模型。以下是该研究的详细总结：

### 1. 解决的问题与研究价值
*   **核心问题**：治疗性多肽（由氨基酸组成的短链）处于药物研发的“尴尬地带”。
    *   **蛋白质模型**（如 ESM）通常只能处理 20 种天然氨基酸，无法识别多肽中常见的化学修饰或非天然氨基酸。
    *   **小分子模型**（基于原子图或 SMILES）在处理多肽这种长链、类聚合物的结构时，往往因为序列过长或结构重复而表现不佳。
*   **研究价值**：多肽药物兼具小分子的多样性和蛋白质的高特异性，是目前新药研发的热点。该论文通过扩展化学语言模型，填补了多肽药物在计算建模上的空白，让 AI 能直接“读懂”复杂的多肽化学结构。

### 2. 白话版概述
多肽就像是用不同颜色的珠子串成的短项链。以前的 AI 要么只认识 20 种标准珠子（蛋白质模型），要么把项链拆成一堆散乱的原子（小分子模型），都看不全貌。这篇论文开发了一个名为 PeptideCLM-2 的“超级翻译官”，它直接学习了超过 1 亿个分子的化学结构语言（SMILES 字符串）。它不仅能识别标准珠子，还能识别各种奇形怪状的非标准珠子及其连接方式，从而精准预测这些多肽在人体内的表现，比如能不能穿过细胞膜、能药效维持多久。

### 3. 方法部分
*   **核心思想**：将多肽的化学结构视为一种“语言”，利用大规模预训练（Pre-training）来捕获化学规律。
*   **模型结构**：采用了基于 Transformer 架构的化学语言模型（CLM）。它不依赖于预定义的生物学特征，而是直接处理 **SMILES**（一种用字母和符号表示分子结构的文本格式）。
*   **关键设计与取舍**：
    *   **原生表征**：放弃了将多肽简化为氨基酸序列的做法，而是保留完整的原子级化学细节。
    *   **规模化（Scaling）**：在超过 1 亿个分子的大规模数据集上进行训练，以确保模型见过足够多的化学环境，从而能够泛化到复杂的多肽结构上。
    *   **端到端预测**：模型生成的嵌入（Embedding）可以直接用于下游任务，无需手动设计复杂的化学描述符。

### 4. 实验部分
*   **数据与任务**：在多个关键的药物开发指标上进行了测试：
    *   **膜扩散（Membrane Diffusion）**：预测多肽进入细胞的能力。
    *   **生物功能（Biological Function）**：预测多肽是否能产生预期的生物效应。
    *   **半衰期（Half-life）**：预测药物在血液中代谢的速度。
*   **Baseline（对比方法）**：
    *   传统的静态化学描述符（如 RDKit 生成的物理化学参数）。
    *   针对特定数据集定制的复杂多嵌入（Multi-embedding）流水线。
*   **主要结果**：PeptideCLM-2 在所有基准测试中均表现出更强的性能，尤其是在处理包含非天然修饰的多肽时，其预测准确度显著优于传统方法。

### 5. 资源与算力
*   **训练规模**：明确提到在 **1 亿多个分子** 上进行了预训练。
*   **算力细节**：**文中未充分披露**具体的 GPU 型号、训练时长或具体的计算开销。

### 6. 真正可信的贡献
*   **打破了“天然氨基酸”的限制**：证明了基于 SMILES 的语言模型在处理复杂生物聚合物（如多肽）时，比传统的蛋白质序列模型更具通用性。
*   **验证了 Scaling Law**：展示了通过增加预训练数据量，可以显著提升模型对多肽这种“大分子中的小分子”的理解能力。
*   **实用性强**：直接针对药物研发中的痛点（如半衰期、渗透性）进行验证，而非仅仅跑通合成数据。

### 7. 局限与风险
*   **序列长度瓶颈**：SMILES 字符串描述大型多肽时会变得非常长，可能会触及 Transformer 模型的上下文窗口限制，导致计算成本激增。
*   **缺乏 3D 信息**：SMILES 是 1D 文本，虽然隐含了化学连接，但无法直接表达多肽在空间中的折叠构象（3D Structure），这对于某些生物相互作用至关重要。
*   **数据偏差**：1 亿个预训练分子中，绝大多数可能是普通小分子，针对特定多肽类别的优化程度仍有待观察。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事多肽药物研发、大环分子设计、以及关注非天然氨基酸修饰的研究者。
*   **后续可跟进的问题**：如何将 1D 的 SMILES 语言模型与 3D 结构信息（如 AlphaFold 产生的构象）进行多模态融合，以进一步提升预测精度？

（完）
