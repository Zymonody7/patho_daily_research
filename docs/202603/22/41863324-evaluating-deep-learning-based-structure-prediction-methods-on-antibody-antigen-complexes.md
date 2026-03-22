---
title: Evaluating Deep Learning Based Structure Prediction Methods on Antibody-Antigen Complexes.
title_zh: 评估基于深度学习的抗体-抗原复合物结构预测方法
authors: "Samuel Fromm, Marko Ludaic, Arne Elofsson"
date: 2026-03-21
pdf: "https://pubmed.ncbi.nlm.nih.gov/41863324/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 评估宿主-病原体蛋白复合物的深度学习预测
tldr: 针对抗体-抗原复合物预测中缺乏共进化信号的难题，本研究评估了 AlphaFold2、AlphaFold3、Boltz-1 和 Chai-1 等深度学习模型。研究发现，增加采样次数能以对数线性方式提升预测成功率，但模型自带的评分机制难以准确识别最优结构。AlphaFold3 表现最优，但其性能高度依赖于训练集中存在的结构相似性，揭示了当前模型在处理全新抗体结构时的局限性。
selection_source: fresh_fetch
motivation: 传统的蛋白质结构预测模型依赖共进化信息，但在缺乏此类信号的抗体-抗原相互作用预测中表现不佳。
method: 在全新的抗体-抗原复合物数据集上，对比评估了 AlphaFold3、AlphaFold2 及其变体（如增加采样量）以及 Boltz-1 和 Chai-1 的预测性能。
result: 增加采样显著提升了找到正确模型的概率，但模型内部质量评估指标往往无法从大量候选结构中筛选出真正的最优解。
conclusion: AlphaFold3 虽然在综合表现上领先，但其预测能力部分源于对训练集结构的记忆，在面对缺乏结构相似性的目标时性能会大幅下降。
---

## 摘要
动机：AlphaFold2 显著提高了蛋白质复合物结构的预测水平。然而，对于缺乏共进化信号的相互作用（如宿主-病原体和抗体-抗原相互作用），其准确性较低。为了解决这一局限性，目前已开发出两种策略：大规模采样，以及如 AlphaFold3 中引入的将 evoformer 替换为不依赖共进化的 pairformer，从而使网络能够进行更多的结构推理。结果：在本研究中，我们在未见过的抗体-抗原复合物上对结构预测方法进行了基准测试。我们发现，增加采样量能以大致呈对数线性的方式提高生成正确蛋白质模型的几率。然而，AlphaFold 的内部质量评估通常无法识别每个目标的最佳预测结构，导致排名第一的蛋白质模型与最佳模型相比，性能出现显著下降。对于所有方法而言，识别最佳模型仍然是一个重大挑战。我们还表明，AlphaFold3 的表现优于 AlphaFold2、Boltz-1 和 Chai-1。此外，对于与训练集缺乏结构相似性的复合物，AlphaFold3 的性能显著下降，这表明它在一定程度上学会了检测远源结构相似性。可用性与实现：所有代码均可在 github.com/samuelfromm/abag-benchmark-set/ 获取，所有数据均可在 DOI: 10.5281/zenodo.17978681 获取。后者仓库也包含代码。补充信息：补充信息可在网上查阅。

## Abstract
MOTIVATION: AlphaFold2 significantly improved the prediction of protein complex structures. However, its accuracy is lower for interactions without coevolutionary signals, such as host-pathogen and antibody-antigen interactions. Two strategies have been developed to address this limitation: massive sampling and replacing the evoformer with the pairformer, which does not rely on coevolution, as introduced in AlphaFold3, thereby enabling more structural reasoning by the network. RESULTS: : In this study, we benchmark structure prediction methods on unseen antibody-antigen complexes. We found that increased sampling improves the chances of generating a correct protein model, roughly in a log-linear manner. However, the internal quality estimates by AlphaFold often cannot identify the best predicted structures for each target, resulting in a significant loss of performance for the top-ranked protein model compared with the best model. For all methods, a significant challenge remains the identification of the best model. We also show that AlphaFold3 outperforms AlphaFold2, Boltz-1, and Chai-1. Furthermore, AlphaFold3 performance declines significantly for complexes that lack structural similarity to the training set, indicating that it has to some extent learned to detect remote structural similarities. AVAILABILITY AND IMPLEMENTATION: All code is available from github.com/samuelfromm/abag-benchmark-set/and all data from DOI : 10.5281/zenodo.17978681.The latter repository also contains the code. SUPPLEMENTARY INFORMATION: Supplementary information is available online.