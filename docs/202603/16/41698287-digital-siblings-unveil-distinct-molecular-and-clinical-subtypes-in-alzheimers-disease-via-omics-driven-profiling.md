---
title: "Digital siblings unveil distinct molecular and clinical subtypes in Alzheimer's disease via omics-driven profiling."
title_zh: 数字同胞通过组学驱动的分析揭示阿尔茨海默病中截然不同的分子和临床亚型
authors: "Bethany Bengs, Russell H Swerdlow, Jefferey Burns, Chad Slawson, Global Neurodegeneration Proteomics Consortium (GNPC), Matthew McCoy, Mihaela E Sardiu"
date: 2026-03-15
pdf: "https://pubmed.ncbi.nlm.nih.gov/41698287/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 流形学习用于多组学整合和患者分层
tldr: 阿尔茨海默病（AD）具有高度的生物学和临床异质性，导致精准诊疗困难。本研究利用流形学习技术融合了438名患者的蛋白质组学、人口统计学和临床数据，构建了“数字同胞”框架，通过识别潜在空间中相似的患者群体，成功划分出具有独特分子机制和临床特征的亚型。该方法揭示了与年龄、饮酒等相关的通路富集，为AD的精准分型和未来动态预测模型奠定了基础。
selection_source: fresh_fetch
motivation: 针对阿尔茨海默病因高度异质性导致的预后和个性化治疗难题，需要一种能刻画患者相似性并识别亚型分子特征的数据驱动方法。
method: 采用流形学习技术融合蛋白质组学与临床多维数据，在学习到的潜在空间中识别“数字同胞”（特征相近的患者），并进行聚类分层和蛋白质网络分析。
result: 成功识别出具有显著差异的分子和临床亚型，并发现了与年龄、酒精摄入及共病相关的特定生物通路富集和关键蛋白质相互作用。
conclusion: “数字同胞”框架为阿尔茨海默病的精准分型提供了新视角，有助于深化对疾病异质性机制的理解，并为开发个性化预测模型提供了支撑。
---

## 摘要
阿尔茨海默病 (AD) 是一种多因素神经退行性疾病，具有广泛的生物学和临床异质性，这使得预后和个性化治疗策略变得复杂。因此，表征患者相似性和亚型特异性分子特征的数据驱动方法对于推进 AD 的精准医学至关重要。我们应用流形学习技术融合了 438 名 AD 患者的蛋白质组学、人口统计学和临床数据，从而能够在学习到的潜空间内识别“数字同胞”——即具有密切相关分子和临床特征的患者。该框架实现了稳健的患者亚组聚类和分层，揭示了与年龄、饮酒和共病等临床特征相关的独特通路富集。此外，对这些亚组内关键蛋白质相互作用的结构和网络分析，为可能驱动疾病异质性的分子机制提供了见解。虽然这种方法主要基于综合分子模式对患者进行聚类，但它为开发纳入纵向进展和干预结果的预测模型奠定了关键基础。总之，我们的结果强调了基于“数字同胞”的分层在完善患者亚组表征方面的潜力，并为未来 AD 的动态建模奠定了基础。

## Abstract
Alzheimer's Disease (AD) is a multifactorial neurodegenerative disorder marked by extensive biological and clinical heterogeneity, complicating prognosis and personalized treatment strategies. Because of this, data-driven methods that characterize patient similarity and subgroup-specific molecular signatures are essential for advancing precision medicine in AD. We applied manifold learning techniques to fuse proteomic, demographic, and clinical data from 438 AD patients, enabling the identification of "digital siblings"-patients with closely related molecular and clinical profiles within a learned latent space. This framework enabled robust clustering and stratification of patient subgroups, revealing distinct pathway enrichments associated with clinical traits such as age, alcohol use, and comorbidities. Moreover, structural and network analyses of key protein interactions within these subgroups provided insights into the molecular mechanisms potentially driving disease heterogeneity. While this approach primarily clustered patients based on comprehensive molecular patterns, it lays critical groundwork for developing predictive models that incorporate longitudinal progression and intervention outcomes. Overall, our results underscore the potential of "digital sibling"-based stratification to refine patient subgroup characterization and serve as a foundation for future dynamic modeling in AD.