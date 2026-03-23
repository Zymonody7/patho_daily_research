---
title: "Topology-Aware Generation and Activity-Based Filtering: A Computational-Experimental Framework for Data-Scarce Quaternary Ammonium Compound Discovery."
title_zh: 拓扑感知生成与基于活性的过滤：一种用于数据稀缺季铵化合物发现的计算-实验框架
authors: "Shiva Ghaemi, Amanda Consylman, Bo Pan, Alice Wu, Ashley Petersen, Gabe Chang, Diana McDonough, Mark Forman, Elise L Bezold, William M Wuest, Amarda Shehu, Liang Zhao, Kevin P C Minbiole"
date: 2026-03-23
pdf: "https://pubmed.ncbi.nlm.nih.gov/41785100/"
tags: ["query:pathoai"]
score: 9.0
evidence: 利用变分自编码器进行AI引导的新型抗菌消毒剂开发
tldr: 针对季铵盐类（QACs）抗菌化合物在数据稀缺情况下难以发现新结构的问题，本研究对比了两种基于拓扑感知变分自编码器（VAE）的生成工作流。通过引入活性预测模型进行预筛选，显著提升了生成分子的质量和合成价值。实验验证了11种新型QACs对四种病原体具有高效抗菌活性，证明了该框架在小样本化学空间探索中的有效性。
selection_source: fresh_fetch
motivation: 细菌耐药性增强使得开发新型季铵盐类抗菌药迫在眉睫，但该领域结构-活性数据稀缺，限制了传统AI生成模型的应用。
method: 采用拓扑感知变分自编码器生成候选结构，并对比了“专家直接评估”与“模型预测活性后再行专家评估”两种筛选策略。
result: "引入活性过滤后，具有合成价值的候选分子比例从9%提升至38%，且实验验证了11个对病原体具有1-32 μM低抑制浓度的活性分子。"
conclusion: 拓扑感知生成结合计算预筛选，能够有效克服数据稀缺挑战，在有限的专家评估成本下实现高质量化学实体的系统性发现。
---

## 摘要
季铵化合物 (QACs) 是广泛使用的抗菌消毒剂，其效力正受到日益严重的细菌耐药性的威胁。人工智能引导的新型 QACs 开发受到历史上稀疏的结构-活性数据以及生成具有生物活性的新型化学实体方法的限制。本文介绍了一项关于两种计算工作流的对比实验研究，旨在加速数据受限条件下的 QACs 发现。两种工作流均采用拓扑感知变分自编码器来生成新型候选化合物。在工作流 1 中，生成的 QAC 结构在固定的时间限制内，通过系统应用化学领域决策标准直接进行专家评估。在工作流 2 中，生成的候选化合物首先使用经过训练以预测抗菌活性的预测模型进行计算过滤，仅将预计对至少一种菌株具有高活性的分子提交专家评估。这种预测性过滤使得在相同的时间限制内能够评估更大、更高质量的候选化合物库。对两种工作流产生的化合物集进行的对比评估显示，候选化合物质量有了实质性提高：被认为值得合成的化合物比例从 9% 增加到 38%，而无效输出从 21% 减少到 0%。对两种工作流中选出的 29 种化合物进行实验表征，获得了 11 种新型 QACs，其实验验证的针对四种细菌病原体的最小抑菌浓度为 1-32 μM。这些结果表明，拓扑感知生成与计算预过滤相结合，能够在尊重专家评估时间实际限制的同时，系统地探索数据稀缺的化学空间。

## Abstract
Quaternary ammonium compounds (QACs) are widely used antimicrobial disinfectants whose efficacy is threatened by increased bacterial resistance. Artificial intelligence-guided development of novel QACs is constrained by historically sparse structure-activity data and methods to generate novel chemical entities with bioactivity. This paper presents a comparative experimental study of two computational workflows designed to accelerate QAC discovery under data-limited conditions. Both workflows employ a topology-aware variational autoencoder to generate novel candidates. In Workflow 1, generated QAC structures were directly subjected to expert evaluation within a fixed time constraint through the systematic application of chemistry-domain decision criteria. In Workflow 2, generated candidates were first computationally filtered using predictive models trained to anticipate antimicrobial activity, advancing only molecules projected to be highly active against at least one bacterial strain for expert evaluation. This predictive filtering enabled the assessment of a larger, higher-quality candidate pool within the same time constraint. Comparative assessment of the compound sets resulting from the two workflows revealed substantial improvements in candidate quality: compounds deemed synthesis-worthy increased from 9% to 38%, while invalid outputs decreased from 21% to 0%. Experimental characterization of 29 selected compounds across both workflows yielded 11 novel QACs with experimentally validated minimum inhibitory concentrations of 1-32 μM against four bacterial pathogens. These results demonstrate that topology-aware generation coupled with computational prefiltering enables systematic navigation of data-scarce chemical spaces while respecting practical constraints on expert evaluation time.