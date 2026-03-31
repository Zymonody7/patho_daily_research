---
title: "ECOD: Classification of domains in AFDB Swiss-Prot structure predictions."
title_zh: ECOD：AFDB Swiss-Prot 结构预测中的结构域分类
authors: "R Dustin Schaeffer, Jing Zhang, Qian Cong, Nick V Grishin"
date: 2026-03-30
pdf: "https://pubmed.ncbi.nlm.nih.gov/41911251/"
tags: ["query:bioinfo"]
score: 8.0
evidence: AlphaFold结构预测中的结构域分类
tldr: 随着 AlphaFold 预测结构的爆发式增长，如何系统性地对海量结构进行演化分类成为挑战。本研究利用 DPAM 流水线对 Swiss-Prot 数据库中超过 54 万个蛋白质预测结构进行了 ECOD 结构域分类，成功识别出逾 103 万个结构域。该工作不仅扩展了 ECOD 的覆盖范围，还发现了 10 万个序列比对无法识别的新结构域，为理解蛋白质功能演化提供了高置信度的结构基础。
selection_source: fresh_fetch
motivation: 旨在将 AlphaFold 预测的海量蛋白质结构纳入演化分类体系，以解决传统序列比对在识别远源同源结构域时的局限性。
method: 采用 DPAM 自动化流水线对 UniProtKB/Swiss-Prot 集合中的 54.2 万个蛋白质模型进行结构域分割与 ECOD 拓扑分类。
result: 成功分类了超过 103 万个结构域，涵盖 3493 种拓扑结构，并识别出 10 万个现有 Pfam 数据库未涵盖的结构域。
conclusion: 该研究通过整合 Swiss-Prot 预测结构，显著提升了 AlphaFold 模型的解释力，并为大规模功能导向的蛋白质分类奠定了基础。
---

## 摘要
高精度蛋白质结构预测算法的发展导致了结构数据的爆炸式增长，改变了我们对不同生物体中蛋白质结构与功能关系的理解。诸如蛋白质结构域进化分类（ECOD）之类的结构域分类系统已将这些计算预测与实验结构相结合，为研究界创建了全面的资源。AlphaFold 蛋白质结构数据库（AFDB）发挥着独特的作用，提供了数百万个预测结构，ECOD 已对人类蛋白质、小型病原体和参考蛋白质组进行了系统分类。在本文中，我们将这一分类框架扩展到 UniProtKB/Swiss-Prot 数据集，应用 AlphaFold 模型结构域解析器（DPAM）流水线对超过 542,000 个 Swiss-Prot 蛋白质结构预测中的结构域进行分类，产生了超过 1,032,000 个已分类的结构域。这些结构域涵盖了 3,493 种 ECOD 拓扑结构，并显示出极高的分配置信度（平均 DPAM 概率：0.992），具有广泛的分类学和功能多样性。值得注意的是，超过 100,000 个结构域缺乏现有的 Pfam 映射，这反映了基于结构的分类具有更高的灵敏度，并识别出了尚未被基于序列的图谱捕获的结构域组。这些结果显著扩大了 ECOD 在功能和分类学多样化蛋白质空间中的覆盖范围，将高置信度的结构预测锚定在进化框架中。通过整合 Swiss-Prot 预测，我们增强了 AlphaFold 模型的使用价值和可解释性，并为未来大规模、基于功能的结构域分类奠定了基础。

## Abstract
The development of highly accurate protein structure prediction algorithms has led to an explosion of structural data, transforming our understanding of protein structure-function relationships across diverse organisms. Domain classifications such as the Evolutionary Classification of Protein Domains (ECOD) have incorporated these computational predictions alongside experimental structures to create comprehensive resources for the research community. The AlphaFold Protein Structure Database (AFDB) plays a unique role, providing millions of predicted structures that ECOD has systematically classified for human proteins, small pathogens, and reference proteomes. Here, we extend this classification framework to the UniProtKB/Swiss-Prot dataset, applying the Domain Parser for AlphaFold Models (DPAM) pipeline to classify domains from over 542,000 Swiss-Prot protein structure predictions, resulting in more than 1,032,000 classified domains. These domains span 3,493 ECOD topologies and display high assignment confidence (mean DPAM probability: 0.992), with extensive taxonomic and functional diversity. Notably, over 100,000 domains lack existing Pfam mappings, reflecting the extended sensitivity of structure-based classification and identifying domain groups not yet captured by sequence-based profiles. These results significantly expand ECOD's coverage into a functionally and taxonomically diverse protein space, anchoring high-confidence structure predictions in an evolutionary framework. By integrating Swiss-Prot predictions, we enhance the utility and interpretability of AlphaFold models and establish a foundation for future large-scale, functionally informed domain classifications.