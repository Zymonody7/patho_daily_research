---
title: "The BOS-Lig Data Set: Accurate Ligand Charges from a Consensus Approach for 66,810 Experimentally Synthesized Ligands."
title_zh: "BOS-Lig 数据集：基于共识方法确定的 66,810 种实验合成配体的准确电荷"
authors: "Roland G St Michel, Ryan J Jang, Aaron G Garrison, Ilia Kevlishvili, Heather J Kulik"
date: 2026-07-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/42438368/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 高通量筛选和配体性质预测
tldr: 针对过渡金属配合物高通量筛选中配体电荷及应用领域信息缺失的问题，本研究通过迭代电荷平衡工作流，从12.7万个单核配合物中提取并校准了6.6万个配体的准确电荷，构建了BOS-Lig数据集。该方法利用同配位配合物向异配位环境传播电荷信息，并结合主题模型将配体与反应性、光物理等功能领域关联，为数据驱动的配体设计提供了实验支撑的化学空间基础。
selection_source: fresh_fetch
motivation: 现有的晶体数据库中配体净电荷和功能应用信息往往缺失或不一致，限制了过渡金属配合物的计算筛选与设计。
method: 采用一种迭代电荷平衡算法，通过同配位配合物推导电荷并向异配位环境传播，同时利用主题模型从文献摘要中提取配体的功能分类。
result: "成功构建了包含66,810个配体准确电荷的BOS-Lig数据集，并为25,146个配体标注了涵盖反应性、氧化还原、生物和光物理化学的应用领域。"
conclusion: BOS-Lig数据集通过整合实验电荷属性与功能应用标签，为机器学习驱动的配体发现和金属配合物性能预测提供了高质量的基准数据。
---

## 摘要
理解配体性质对于过渡金属配合物的计算高通量筛选至关重要。然而，配体的净电荷等性质以及应用领域等其他信息在晶体学数据集中往往缺失或记录不一致。在此，我们从剑桥结构数据库（CSD）收录的 126,985 个单核过渡金属配合物中构建了一个配体数据集。通过结合配合物电荷、金属氧化态以及晶体学观测中的共识，我们利用迭代电荷平衡工作流，在识别出的 94,581 种独特配体结构中，为 66,810 种配体准确分配了净电荷，从而构建了波士顿开壳层配体（BOS-Lig）数据集。该工作流首先分配同配配合物中的配体电荷，然后在异配环境中迭代传播这些分配结果，从而在缺乏直接电荷信息的情况下也能推断出电荷。我们分析了八隅体规则等简单启发式方法失效的情况，并引入了纯度指标来识别电荷分配可能不正确的情形。每个配体还根据其金属配位原子以及是否存在多种变体（即半不稳定性）进行了分类。随后，我们将配合物与其相关的期刊摘要联系起来，并应用主题建模工作流将 25,146 种配体与涵盖反应性、氧化还原化学、生物化学和光物理化学的功能应用领域联系起来。总之，我们提供了一个基于实验的配体化学空间数据集，将电荷与功能应用联系起来，为计算筛选和数据驱动的配体设计奠定了基础。

## Abstract
Understanding ligand properties is essential for computational high-throughput screening of transition metal complexes. However, ligand properties such as net charge and other information such as their application area are often absent or inconsistently recorded in crystallographic data sets. Here, we construct a ligand data set from 126,985 mononuclear transition metal complexes curated from the Cambridge Structural Database. Using an iterative charge-balancing workflow that combines complex charges, metal oxidation states, and consensus across crystallographic observations, we confidently assign net charges to 66,810 ligands among 94,581 identified unique ligand structures to curate the Boston Open-Shell Ligand (BOS-Lig) data set. The workflow assigns ligand charges in homoleptic complexes first and then iteratively propagates these assignments across heteroleptic environments, allowing charges to be inferred even when direct charge information is unavailable. We analyze cases where simple heuristics such as the octet rule would have failed and introduce a purity metric to identify when our charge assignments may be incorrect. Each ligand is also classified in terms of its metal-coordinating atoms and whether there are multiple variants (i.e., hemilability). We then link complexes to their associated journal abstracts and apply a topic-modeling workflow to link 25,146 ligands with functional application areas spanning reactivity, redox chemistry, biological chemistry, and photophysical chemistry. Together, we provide an experimentally grounded data set of ligand chemical space that connects charge and functional application as a foundation for computational screening and data-driven ligand design.