---
title: Demography-dependent variability in the human tumor mycobiome.
title_zh: 人类肿瘤真菌组中依赖于人口统计学特征的变异性
authors: "Dan Coster, Thomy Margalit, Ronen Ben-Ami, Ben Boursi, Ron Shamir"
date: 2026-03-26
pdf: "https://pubmed.ncbi.nlm.nih.gov/41885500/"
tags: ["query:seqai"]
score: 6.0
evidence: 肿瘤真菌组数据处理与批次校正
tldr: 肿瘤真菌组具有重要的预后价值，但患者人口统计学特征对其组成的影响尚不明确。本研究针对现有数据处理可能产生的假阳性问题，对TCGA中5000多份肿瘤样本进行了重新分析，采用了14种数据转换与批次校正组合，并利用倾向评分调整混杂因素。研究发现了24种与年龄、性别、BMI特别是种族显著相关的真菌物种，揭示了肿瘤微环境的复杂性，为精准肿瘤学中的个性化诊断和治疗提供了新视角。
selection_source: fresh_fetch
motivation: 探究患者的年龄、性别、BMI及种族等人口统计学因素如何影响肿瘤内真菌组的构成，并解决现有研究中数据处理方法可能导致的假阳性信号问题。
method: 通过对TCGA数据库中13种癌症类型的5000多个样本进行重分析，对比了14种数据转换与批次校正组合，并结合倾向评分匹配来消除组织学类型和肿瘤分期的干扰。
result: 识别出24种在不同人口统计特征下丰度存在显著差异的真菌物种，其中20种差异与种族密切相关。
conclusion: 肿瘤真菌组受患者人口统计学因素（尤其是种族）的显著影响，在进行相关生物信息学分析时必须采用稳健的数据归一化技术以确保结果的可靠性。
---

## 摘要
最近的研究表明，肿瘤真菌组（mycobiome）在癌症患者中可能具有预后和诊断意义。我们旨在利用这些研究的数据，更好地了解患者特征（年龄、性别、体重指数 [BMI] 和种族）如何影响肿瘤真菌组的组成。鉴于近期对肿瘤微生物组数据处理程序的批评，我们首先对数据进行了测试，并得出结论：所使用的批次校正和转换可能会产生错误信号。相反，我们针对 13 种癌症类型的 224 种真菌物种的数据，探索了 14 种数据转换和批次校正方法的组合。利用倾向评分来调整潜在的混杂因素，如组织学类型和肿瘤分期。为了尽量减少错误结果，我们仅将在所有 14 种组合归一化后的数据中，在特定癌症类型的某个人口统计学因素下显示出显著丰度差异的真菌物种鉴定为阳性结果。我们观察到 24 种肿瘤内真菌物种的丰度在某些人口统计学特征下存在显著差异。其中共有 20 项差异存在于特定癌症的种族之间。研究结果表明，真菌组、癌症类型和患者人口统计学特征之间存在复杂的相互作用。我们的研究强调，为了理解真菌组在癌症发生和治疗反应中的作用，有必要考虑种族因素。该研究还强调了数据处理技术的重要性。重要性：本研究分析了瘤内真菌组依赖于人口统计学特征的变异性，为不同癌症类型和患者人口统计学特征下的真菌丰度提供了新的见解。通过分析来自癌症基因组图谱（The Cancer Genome Atlas）的 5,000 多个肿瘤样本，该研究鉴定了 24 种真菌物种，其丰度变化与种族、年龄、性别和体重指数等人口统计学因素显著相关。这些发现强调了肿瘤微环境的复杂性，以及在癌症研究中考虑人口统计学多样性的重要性。该研究强调了使用稳健的数据归一化和批次校正技术以避免伪相关，从而确保真菌组分析可靠性的必要性。这项工作突出了真菌组作为精准肿瘤学的新前沿，并为未来考虑人口统计学因素对肿瘤生物学影响的个性化癌症诊断和治疗铺平了道路。

## Abstract
UNLABELLED: Recent studies have shown that the tumor mycobiome may have prognostic and diagnostic significance in cancer patients. We aimed to gain a better understanding of how patient characteristics (age, sex, body mass index [BMI], and race) influence the composition of the tumor mycobiome, using the data of these studies. We first tested the data in view of recent critiques of tumor microbiome data processing procedures and concluded that the batch correction and transformation used on it may produce false signals. Instead, we explored 14 combinations of data transformation and batch correction methods on data of 224 fungal species across 13 cancer types. Propensity scores were utilized to adjust for potential confounders such as histological type and tumor stage. To minimize false outcomes, we identified as positive results only those fungi species that showed significant difference in abundance across a demographic factor within a particular cancer type, using data normalized according to all 14 combinations. We observed significant differences in 24 fungal species abundance within tumors for certain demographic characteristics. A total of 20 of these differences were among races in specific cancers. The findings indicate that there are intricate interactions between the mycobiome, cancer type, and patient demographics. Our study highlights the need to account for race in order to understand the role of the mycobiome in cancer development and treatment response. The study also underscores the importance of data processing techniques. IMPORTANCE: This study analyzes the demographic-dependent variability of the intratumor mycobiome, providing a novel understanding of fungal abundance across different cancer types and patient demographics. By analyzing over 5,000 tumor samples from The Cancer Genome Atlas, the research identified 24 fungal species with significant abundance variations linked to demographic factors such as race, age, sex, and body mass index. These findings underscore the complexity of the tumor microenvironment and the importance of accounting for demographic diversity in cancer research. The study emphasizes the necessity of using robust data normalization and batch correction techniques to avoid spurious associations in order to ensure the reliability of mycobiome analysis. This work highlights the mycobiome as a new frontier in precision oncology and paves the way for future personalized cancer diagnostics and treatments that account for the influence of demographic factors on tumor biology.