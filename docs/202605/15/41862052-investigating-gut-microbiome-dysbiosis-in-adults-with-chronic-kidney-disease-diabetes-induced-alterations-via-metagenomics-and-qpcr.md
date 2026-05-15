---
title: "Investigating gut microbiome dysbiosis in adults with chronic kidney disease: Diabetes-induced alterations via metagenomics and qPCR."
title_zh: 调查慢性肾脏病成年患者的肠道微生物群失调：通过宏基因组学和qPCR研究糖尿病引起的改变
authors: "Saranya Gunasekaran Rajalakshmi, Ramesh Babu K, Pragasam Viswanathan"
date: 2026-05-15
pdf: "https://pubmed.ncbi.nlm.nih.gov/41862052/"
tags: ["query:seqai"]
score: 7.0
evidence: 用于肠道微生物失调的16S rRNA宏基因组方法和基于网络的方法
tldr: 糖尿病是导致慢性肾脏病（CKD）的主因，但肠道菌群在其中的演变规律尚不明确。本研究通过16S rRNA测序、qRT-PCR及机器学习方法（如随机森林、WGCNA），对比了健康人、单纯糖尿病及糖尿病肾病患者的菌群差异。结果发现，随病情加重，有益菌（如青春双歧杆菌）显著减少，而致病相关菌（如均匀拟杆菌）增加。该研究揭示了菌群失调随疾病进展的动态变化，为CKD的早期干预提供了微生物标志物参考。
selection_source: fresh_fetch
motivation: 旨在探究从单纯糖尿病发展到慢性肾脏病过程中，肠道微生物群落如何发生失调及其与临床指标的关联。
method: 采用16S rRNA扩增子测序结合qRT-PCR验证，并利用随机森林、加权基因共表达网络分析（WGCNA）和倾向评分匹配等多种计算手段整合临床数据。
result: 识别出与肾功能指标（eGFR和血肌酐）显著相关的关键菌属，发现随疾病进展，保护性菌群如青春双歧杆菌比例下降，而促病菌群如均匀拟杆菌显著上升。
conclusion: 肠道菌群失调始于糖尿病阶段并在并发肾脏病时进一步加剧，这种渐进式的微生物失衡反映了代谢性疾病恶化的病理过程。
---

## 摘要
背景：2型糖尿病（T2D）是糖尿病肾病的主要诱因，而糖尿病肾病是慢性肾脏病（CKD）的首要原因。本研究采用16S rRNA宏基因组学方法，结合qRT-PCR验证和临床数据整合，调查了健康个体以及患有或不患有CKD的糖尿病患者的肠道微生物失调和组成变化，旨在识别与疾病进展显著相关的关键属。方法：利用16S rRNA扩增子测序分析了22名个体的粪便样本，以评估肠道微生物群组成。采用差异丰度分析、LEfSe和基于网络的方法来识别关键分类群。通过qRT-PCR验证了显著特征。使用包括Pearson相关性、WGCNA、随机森林和倾向评分匹配在内的综合方法，将微生物特征与临床标志物联系起来。使用PICRUSt2预测了微生物通路的通路功能富集。关键发现：共鉴定出1409个扩增子序列变体（ASVs）。Bray-Curtis相异度显示患病受试者与健康受试者之间存在显著的微生物多样性差异（p < 0.031）。与估算肾小球滤过率（eGFR）和血清肌酐（sCr）相关的关键分类群包括单形拟杆菌（Bacteroidetes uniformis，LFC +9）、瘤胃球菌属（Ruminococcus，LFC +8.1）和嗜琥珀酸透析杆菌（Dialister succinatiphilus，LFC +6.7），这些菌群与疾病进展和代谢调节有关。相比之下，保护性分类群如青春双歧杆菌（Bifidobacterium adolescentis，LFC -9.5）、普拉梭菌（Faecalibacterium prausnitzii，LFC -6.39）、柯林斯氏菌属（Collinsella）和埃氏巨型球菌（Megasphaera elsdenii）有所减少。Pearson相关性、WGCNA、倾向评分匹配和随机森林分类的整合揭示了与临床协变量相关的微生物特征。意义：我们的研究结果表明，肠道微生物群的转变始于不伴有CKD的糖尿病患者，但在伴有CKD的糖尿病患者中变得更加显著，有益菌比例较低，反映了随疾病进展而逐渐加剧的微生物失衡。

## Abstract
BACKGROUND: Type 2 diabetes (T2D) is a major contributor to diabetic nephropathy, the leading cause of chronic kidney disease (CKD). This study investigated gut microbial dysbiosis and composition shift among healthy individuals and diabetic patients with or without CKD using a 16S rRNA metagenomic approach, validated by qRT-PCR and clinical data integration to identify the significant key genera associated with disease progression. METHODS: Stool samples from 22 individuals were analysed using 16S rRNA amplicon sequencing to assess gut microbiota composition. Differential abundance analysis, LEfSe, and network-based methods were employed to identify key taxa. Significant features were validated by qRT-PCR. Integrated approaches, including Pearson correlation, WGCNA, random forest, and propensity score matching, were used to associate microbial features with clinical markers. Functional enrichment of microbial pathways was predicted using PICRUSt2. KEY FINDINGS: A total of 1409 amplicon sequence variants (ASVs) were identified. Bray-Curtis dissimilarity showed significant microbial diversity differences between disease and healthy subjects (p < 0.031). Key taxa associated with eGFR and serum creatinine (sCr) included Bacteroidetes uniformis (LFC +9), Ruminococcus (LFC +8.1), and Dialister succinatiphilus (LFC +6.7), linked to disease progression and metabolic regulation. In contrast, protective taxa such as Bifidobacterium adolescentis (LFC -9.5), Faecalibacterium prausnitzii (LFC -6.39), Collinsella, and Megasphaera elsdenii were reduced. Integration of Pearson correlation, WGCNA, propensity score matching, and random forest classification revealed microbial features associated with clinical covariates. SIGNIFICANCE: Our findings show the gut microbiome shifts begin in diabetics without CKD conditions but become more pronounced in diabetics with CKD, with a lower ratio of beneficial bacteria, reflecting a gradual microbial imbalance along disease progression.