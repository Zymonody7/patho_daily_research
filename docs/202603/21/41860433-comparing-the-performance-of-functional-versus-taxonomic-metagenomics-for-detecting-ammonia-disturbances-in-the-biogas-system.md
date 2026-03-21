---
title: Comparing the performance of functional versus taxonomic metagenomics for detecting ammonia disturbances in the biogas system.
title_zh: 比较功能宏基因组学与分类宏基因组学在检测沼气系统氨扰动中的性能
authors: "Dries Boers, Olivier Chapleur, Anders F Andersson, Anna Schnürer"
date: 2026-03-20
pdf: "https://pubmed.ncbi.nlm.nih.gov/41860433/"
tags: ["query:pathoai"]
score: 6.0
evidence: 用于干扰检测的宏基因组分类和功能分析
tldr: 沼气生产常受高浓度氨干扰，及早发现干扰至关重要。本研究通过对三个独立实验室反应器的宏基因组数据进行功能和分类学标注，利用正则化回归模型对比了两者在检测氨干扰方面的表现。结果显示，在单一研究内部，分类学数据表现更优；但在跨研究应用时，功能模型展现出更好的泛化潜力。这表明功能宏基因组在跨场景监测中具有一定优势，但并未全面超越分类学方法。
selection_source: fresh_fetch
motivation: 旨在探究在沼气生产系统中，利用宏基因组的功能特征是否比分类学特征更能有效地预警和检测氨浓度干扰。
method: 收集三个独立实验的宏基因组序列，分别进行基因功能和物种分类标注，并利用正则化回归模型拟合氨浓度与干扰状态。
result: 在单一实验内部，物种分类数据的检测性能与功能数据相当甚至更优，但在跨实验的模型迁移测试中，功能模型表现出相对较好的泛化能力。
conclusion: 研究结果仅有限地支持了功能宏基因组优于分类学的假设，暗示在构建通用的生物监测模型时需综合考虑两类特征。
---

## 摘要
沼气是一种具有巨大潜力的可再生能源，但其生产经常受到工艺扰动的阻碍，其中高氨浓度是一个常见原因。尽早发现此类扰动是理想的；宏基因组数据具有改善此类检测的潜力。本研究比较了宏基因组数据的功能和分类方面，并假设功能数据在检测氨扰动方面表现更好。该假设通过对来自三项独立研究的样本进行宏基因组测序得到了验证，这些研究在氨扰动期间对实验室规模的反应器进行了跟踪。所得序列用于预测基因，并进行了功能和分类注释。利用正则化回归将这些特征的读取计数（read counts）与反应器样本的扰动状态和氨浓度进行拟合，这使得即使在样本量有限的情况下也能过滤掉无关特征。在研究内部，分类数据在检测氨扰动和拟合氨浓度方面具有相似或更好的表现。然而，当将训练好的模型应用于其他研究时，虽然整体表现较差，但功能模型比分类模型表现更好的情况更为常见。总之，我们关于功能宏基因组学优于分类宏基因组学的假设仅得到了有限的支持。

## Abstract
Biogas is a renewable energy source with great potential, but its production is frequently hindered by process disturbances, of which a high ammonia concentration is one common cause. It is desirable that such disturbances are found as early as possible; metagenomics data has the potential to improve this detection. This study compares functional and taxonomic aspects of metagenomics data, hypothesising that functional data will perform better for detecting ammonia disturbances. The hypothesis was tested by metagenomic sequencing of samples from three independent studies, which followed lab-scale reactors during ammonia disturbances. The resulting sequences were used to predict genes, which were functionally and taxonomically annotated. The read counts of these features were fitted to disturbance states and ammonia concentrations of reactor samples using regularised regression, which allowed filtering out irrelevant features even with limited sample sizes. Within studies, taxonomic data had similar or better performance in detecting ammonia disturbances and in fitting ammonia concentrations. When applying trained models to other studies however, while performance was generally poor, functional models more often performed better compared to taxonomic models than the other way around. All in all, our hypothesis that functional metagenomics would outperform taxonomic metagenomics only found limited support.