---
title: Evaluating the learnability of single-cell large language models on multiple tasks
title_zh: 评估单细胞大语言模型在多项任务上的可学习性
authors: "Yan Y, Wang X, Song D."
date: 2026-03-12
pdf: "https://doi.org/10.21203/rs.3.rs-8919408/v1"
tags: ["query:bioinfo"]
score: 9.0
evidence: 评估单细胞大语言模型
tldr: 单细胞基础模型（scFMs）是否遵循“规模法则”尚不明确。本研究系统评估了 Geneformer 和 scGPT 在细胞类型标注和扰动预测任务上的表现。结果发现，大规模预训练对标注任务有效，但在扰动预测中收益有限，且增大模型规模并不总能提升性能。研究揭示了现有模型在捕捉复杂生物相互作用方面的局限，强调了引入生物学先验知识的重要性。
selection_source: fresh_fetch
motivation: 验证单细胞基础模型在不同生物学任务中是否真正遵循“模型越大、数据越多、效果越好”的规模法则。
method: 通过在细胞类型标注和扰动预测任务上对比 Geneformer 与 scGPT，并分析其在真实与合成数据上的表现差异来进行系统评估。
result: 预训练显著提升了细胞标注准确率，但在扰动预测中表现平平，且模型往往只捕捉到了简单的统计特征而非深层生物逻辑。
conclusion: 盲目追求模型规模并非单细胞领域的万灵药，未来应转向开发融合深层生物学先验和特定任务架构的模型。
---

## 摘要
<title>摘要</title>  <p>单细胞基础模型（scFMs）的兴起引发了人们对其统一多种生物学任务潜力的关注。然而，它们的实际效用以及缩放法则（scaling laws，即性能随模型和数据规模增加而提升的假设）的有效性仍缺乏深入研究。在本文中，我们系统地评估了两种具有代表性的 scFMs——Geneformer 和 scGPT，涵盖了扰动预测和细胞类型注释任务。我们的研究结果表明，大规模预训练的收益具有强烈的任务依赖性，在细胞类型注释方面具有显著优势，但在扰动预测方面的提升有限。此外，我们的结果表明，增加模型规模并不能保证性能的提升，甚至可能产生负面影响，这挑战了“越大越好”的范式。通过比较模型在不同复杂程度的真实数据与合成数据上的表现，我们的分析表明，对于扰动预测，所测试的 scFMs 捕获的仅仅是简单的汇总统计数据，可能难以学习复杂的生物相互作用。这些结果强调了有必要超越单纯的规模缩放，转向开发整合更深层生物学知识的模型。我们建议，重新关注特定任务的架构和具有生物学启发意义的先验知识，对于释放基础模型在单细胞生物学中的真正潜力至关重要。</p>

## Abstract
<title>Abstract</title>  <p>The rise of single-cell foundation models (scFMs) has sparked interest in their potential to unify diverse biological tasks. However, their practical utility and the validity of scaling laws—the assumption that performance improves with model and data size—remain under-examined. Here, we systematically evaluate two representative scFMs, Geneformer and scGPT, across perturbation prediction and cell type annotation tasks. Our findings suggest that the benefits of large-scale pretraining are strongly task-dependent, conferring substantial advantages in cell type annotation but limited gains in perturbation prediction. Furthermore, our results indicate that increasing model size does not guarantee improved performance and can even be detrimental, challenging the ``bigger is better'' paradigm. By comparing model performance on real versus synthetic data with different levels of complexity, our analysis suggests that for perturbation prediction, the tested scFMs capture little more than simple summary statistics and may struggle to learn complex biological interactions. These results highlight the need to move beyond scaling and toward developing models that integrate deeper biological knowledge. We suggest that a renewed focus on task-specific architectures and biologically-informed priors may be critical for unlocking the true potential of foundation models in single-cell biology.</p>