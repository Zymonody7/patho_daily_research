---
title: Evolutionary structure constrains genomic prediction accuracy more than model complexity in mango (Mangifera indica L.).
title_zh: 在芒果（Mangifera indica L.）中，进化结构对基因组预测准确性的限制超过了模型复杂度
authors: "Ganesan Alagarasan, Abdulqader Jighly, Vanika Garg, Oluwaseun Akinlade, Natalie Dillon, Asjad Ali, Penghao Wang, Christopher I Cazzonelli, Ravi V Mural, Diego Jarquin, Peter Prentis, Rajeev K Varshney"
date: 2026-05-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/42108796/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 评估机器学习和图注意力网络在基因组预测中的应用
tldr: 针对芒果基因组预测中模型复杂度与预测准确率关系不明的问题，本研究对比了线性模型、机器学习及图注意力网络等多种算法。结果发现，不同模型的准确率趋于一致，复杂模型并未带来显著提升。研究进一步揭示，预测准确率主要受性状的进化结构（系统发育信号）制约，而非模型复杂度。这一发现强调了在育种预测中应更关注生物学背景而非盲目追求算法复杂化。
selection_source: fresh_fetch
motivation: 探究在芒果基因组预测任务中，增加模型复杂度或使用集成学习是否能显著优于传统的线性预测方法，并解释不同性状间预测准确率差异的原因。
method: 在芒果的五个性状上系统评估了线性混合模型、贝叶斯变量选择、核方法、机器学习算法、图注意力网络及堆叠集成模型，并利用全基因组标记构建进化树来量化系统发育信号。
result: 各种模型的预测表现趋同，机器学习和复杂集成模型并无系统性优势，且发现性状的系统发育信号强度与预测准确率之间存在强正相关（r ≈ 0.71）。
conclusion: 芒果基因组预测的准确性主要由性状的进化结构和遗传架构决定，而非模型复杂度，因此对齐性状的进化基础比采用复杂模型更为有效。
---

## 摘要
在基因组预测中，目前尚不清楚日益复杂的模型或集成模型是否比已建立的线性方法更能提高预测效果，以及为什么不同性状之间的预测准确性存在差异。本研究在芒果（Mangifera indica L.）中评估了一系列全面的基因组预测模型，包括线性混合模型、贝叶斯变量选择、核方法、机器学习算法、图注意力网络和堆叠集成模型。在五个性状中，线性、贝叶斯、核方法和集成模型的预测准确性趋于一致，堆叠集成仅带来了边际收益，而机器学习方法没有表现出系统性优势。集成消融和权重分析表明，预测信号主要由加性和平滑核成分主导，而更复杂的学习器对性能的贡献很小或甚至产生负面影响。为了解释这些与性状相关的可预测性模式，我们利用基于全基因组标记的树量化了系统发育信号。所有性状均表现出显著的系统发育信号，其强度差异很大，且与预测准确性强相关（r ≈ 0.71）。具有强系统发育结构的性状获得了最高的预测准确性，而信号较弱的性状无论选择何种模型，其预测难度始终较大。综上所述，这些结果证实，在芒果中，基因组预测准确性更多地取决于进化结构和性状架构，而非不断增加的模型复杂度。因此，将预测策略与性状变异的进化基础相结合，可能比采用日益复杂的模型更为有效。

## Abstract
In genomic prediction, it remains unclear whether increasingly complex or ensemble models improve prediction over established linear approaches, and why prediction accuracy varies among traits. Here, we evaluated a comprehensive suite of genomic prediction models, including linear mixed models, Bayesian variable selection, kernel methods, machine learning algorithms, graph attention networks, and stacked ensembles, in mango (Mangifera indica L.). Across five traits, prediction accuracy converged across linear, Bayesian, kernel, and ensemble models, with only marginal gains derived from stacking and no systematic advantage of machine learning approaches. Ensemble ablation and weight analyses revealed that predictive signal was dominated by additive and smooth kernel components, while more complex learners contributed little or negatively upon performance. To explain these trait-dependent patterns in predictability, we quantified the phylogenetic signal using genome-wide marker-based trees. All traits showed a significant phylogenetic signal, with the magnitude varying widely and strongly associated with prediction accuracy (r ≈ 0.71). Traits with strong phylogenetic structure achieved the highest prediction accuracies, whereas traits with a weaker signal were consistently harder to predict, regardless of model choice. Together, these results confirm that, in mango, genomic prediction accuracy is determined more by evolutionary structure and trait architecture rather than increasing model complexity. Aligning prediction strategies with the evolutionary basis of trait variation may therefore be more effective than adopting increasingly complex models.