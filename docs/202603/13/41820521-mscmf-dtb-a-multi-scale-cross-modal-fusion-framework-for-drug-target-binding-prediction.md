---
title: "MSCMF-DTB: a multi-scale cross-modal fusion framework for drug-target binding prediction."
title_zh: MSCMF-DTB：一种用于药物-靶点结合预测的多尺度跨模态融合框架
authors: "Juan Huang, Yuxue Pan, Qu Chen"
date: 2026-03-12
pdf: "https://pubmed.ncbi.nlm.nih.gov/41820521/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于药物-靶点结合的深度学习和BERT嵌入
tldr: 药物-靶点结合预测是药物研发的关键，但现有模型难以同时兼顾分子拓扑、化学子结构及蛋白质序列特征。MSCMF-DTB框架通过DenseGCN提取药物图特征，结合指纹信息，并利用多尺度CNN处理蛋白质BERT嵌入，最后通过交叉注意力与张量网络融合多模态特征。实验证明该模型在DrugBank等多个数据集上性能领先，并能识别关键结合位点，具备实际虚拟筛选潜力。
selection_source: fresh_fetch
motivation: 旨在解决现有模型在预测药物-靶点结合时，无法有效整合分子拓扑结构、化学片段特征与蛋白质序列上下文依赖关系的问题。
method: 采用DenseGCN与分子指纹双通道提取药物特征，结合TAPE-BERT与多尺度CNN处理蛋白质序列，并通过交叉注意力机制与张量网络实现高阶特征融合。
result: "在DrugBank数据集上将AUC和召回率分别提升了3.2%和6.1%，并在KIBA等回归任务中表现稳定，同时通过注意力机制验证了预测结果的生物学可解释性。"
conclusion: 该框架在分类与回归任务中均展现出卓越的泛化能力，能有效识别实验验证的抑制剂，为药物重定向和虚拟筛选提供了可靠的计算工具。
---

## 摘要
预测药物-靶点结合仍然是计算药物发现中的核心挑战，特别是由于模型需要共同捕捉分子拓扑结构、化学子结构以及蛋白质序列依赖性。我们提出了 MSCMF-DTB，这是一个支持药物-靶点相互作用（DTI）分类和药物-靶点亲和力（DTA）回归的端到端深度学习框架。在药物方面，使用 RDKit 生成的分子图通过 DenseGCN 模块进行编码，同时一个并行的指纹通道捕捉片段级和组成特征。在蛋白质方面，来自 TAPE-BERT 的上下文嵌入通过多尺度一维卷积神经网络（1D CNN）处理，以提取局部序列模式。跨模态的药物-蛋白质关系使用交叉注意力机制结合张量网络进行建模，以实现高阶特征交互。融合后的表示被输入到多层感知机（MLP）中进行最终预测。广泛的实验表明，MSCMF-DTB 在小规模和大规模数据集（用于 DTI 的 Human、C. elegans、GPCR、BioSNAP 和 DrugBank，以及用于 DTA 的 DAVIS 和 KIBA）上均取得了具有竞争力且一致的性能。值得注意的是，在用于 DTI 预测的大规模 DrugBank 数据集上，与次优模型（DrugBAN）相比，MSCMF-DTB 的 AUC 和召回率（Recall）分别提高了 3.2% 和 6.1%。对于 DTA 预测，该模型在大型且异构的 KIBA 数据集上实现了稳定的性能，均方误差（MSE）为 0.146，一致性指数（Concordance Index）为 0.886，rm² 为 0.765。基于注意力的可解释性进一步表明，该模型学习到了具有生物学意义的相互作用区域。最后，冷启动案例研究表明，MSCMF-DTB 成功识别了经实验验证的 AKT1 抑制剂，说明了其在虚拟筛选和药物重定向中的实际应用价值。

## Abstract
Predicting drug-target binding remains a central challenge in computational drug discovery, particularly due to the need for models that jointly capture molecular topology, chemical substructures, and protein sequence dependencies. We propose MSCMF-DTB, an end-to-end deep learning framework supporting both drug-target interaction (DTI) classification and drug-target affinity (DTA) regression. On the drug side, molecular graphs generated with RDKit are encoded using a DenseGCN module, while a parallel fingerprint channel captures fragment-level and compositional features. On the protein side, contextualized embeddings from TAPE-BERT are processed through a multi-scale 1D CNN to extract local sequence patterns. Cross-modal drug-protein relationships are modeled using cross-attention mechanism coupled with a tensor network for higher-order feature interaction. The fused representations are fed into an MLP for final prediction. Extensive experiments demonstrate that MSCMF-DTB achieves competitive and consistent performance across small- and large-scale datasets (Human, C. elegans, GPCR, BioSNAP, and DrugBank for DTI, and DAVIS and KIBA for DTA). Notably, on the large-scale DrugBank dataset for DTI prediction, MSCMF-DTB improved AUC and Recall by up to 3.2% and 6.1%, respectively, compared with the second-best model (DrugBAN). For DTA prediction, the model achieved stable performance on the large and heterogeneous KIBA dataset, with an MSE of 0.146, a Concordance Index of 0.886, and an rm² of 0.765. Attention-based interpretability further shows that the model learns biologically meaningful interaction regions. Finally, a cold-start case study indicates that MSCMF-DTB successfully identifies experimentally validated inhibitors to AKT1, illustrating its practical utility in virtual screening and drug repurposing.