---
title: Illuminating cell states by a comprehensive and interpretable single cell foundation model.
title_zh: 通过全面且可解释的单细胞基础模型阐明细胞状态
authors: "Wang J, Tan C, Gao Z, Shao S, Liu S, Li SZ."
date: 2026-03-16
pdf: "https://pubmed.ncbi.nlm.nih.gov/41839876/"
tags: ["query:seqai"]
score: 10.0
evidence: 用于数据表示和细胞状态识别的单细胞基础模型
tldr: 针对单细胞测序数据稀疏、异质性强且模型解释性差的问题，本文推出了CellVQ基础模型。该模型基于6800万细胞数据预训练，通过创新的单细胞离散化（SCD）模块将高维数据转化为可解释的“细胞代码”，并配合CellVQ-Graph工具整合多模态生物信息。实验证明其在多项下游任务中超越了现有基准，能有效揭示复杂的生物学现象，为细胞生物学研究提供了兼具通用性与透明度的AI工具。
selection_source: fresh_fetch
motivation: 现有的单细胞大模型在处理真实世界的稀疏异质数据时表现受限，且因缺乏可解释性而难以被生物学家直接用于科学发现。
method: 提出了包含5亿参数的CellVQ模型，利用SCD模块将细胞特征离散化为可分析的编码，并构建知识图谱插件以融合基因与细胞通讯等多模态数据。
result: 在所有评估的下游任务中均优于强基线模型，并利用其特有的离散编码成功解释了新发现的生物学规律。
conclusion: CellVQ通过离散化表示和多模态图谱技术，实现了单细胞数据的高效表征与深度解读，是细胞生物学领域极具应用潜力的基础模型。
---

## 摘要
单细胞测序的进展推动了具有强大数据表征能力的 AI 驱动基础模型的发展。然而，由于现实世界数据的稀疏性、异质性和较差的可解释性，它们的实际应用受到了限制。为了克服这些挑战，我们提出了 CellVQ。为了增强泛化能力，我们整合了一个包含 6800 万个细胞的大规模单细胞数据集，模型参数量达到 5 亿，并采用了具有挑战性的预训练任务。值得注意的是，我们引入了一个单细胞离散化（SCD）模块，该模块能够有效地表征细胞嵌入（cell embeddings），从而解决了数据异质性问题。为了提高可解释性，SCD 模块将高维且稀疏的单细胞数据转换为“细胞代码”（cell code），便于识别和分析。此外，我们还推出了 CellVQ-Graph，这是一个即插即用的工具，它将 CellVQ 的特征与多模态数据（基因、细胞通讯、注释）相结合，构建用于生物学发现的知识图谱。经过广泛评估，CellVQ 在所有下游任务中均优于强基线模型，并揭示了具有说服力解释的有趣生物学现象。CellVQ 旨在成为细胞生物学领域一个真正适用且通用的 AI 工具。

## Abstract
Advances in single-cell sequencing have enabled AI-driven foundation models with powerful data representation. However, their practical use is limited by real-world data sparsity, heterogeneity, and poor interpretability. To overcome these, we introduce CellVQ. To enhance generalizability, we incorporate a large-scale single-cell dataset comprising 68 million cells, model parameters totaling 500 million, and challenging pretraining tasks. Notably, we introduce a Single-Cell Discretization (SCD) module that effectively represents cell embeddings, addressing data heterogeneity. For improved interpretability, the SCD module transforms high-dimensional and sparse single-cell data into a "cell code," facilitating recognition and analysis. Additionally, we also present CellVQ-Graph, a plug-and-play tool that integrates CellVQ's features with multimodal data (genes, cell communication, annotations) to build a knowledge graph for biological discovery. Extensively evaluated, CellVQ outperforms strong baselines in all downstream tasks, and also uncovered intriguing biological phenomena with compelling explanations. CellVQ aspires to serve as a truly applicable and generalizable AI tool for the cell biology community.