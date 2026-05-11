---
title: Characterization of telomere-related gene subtypes in lung adenocarcinoma and their implications for prognosis and treatment.
title_zh: 肺腺癌中端粒相关基因亚型的特征分析及其对预后和治疗的影响
authors: "Jingyi Gao, Yuansheng Zhao, Zhiying Cheng, Jiajun Yang, Linjun Jiang, Shuxue Xi, Shufang Shi, Geng Tian, Haiwen Zhao, Jialiang Yang, Jinyang Liu"
date: 2026-05-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/42113288/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 整合基因组学和转录组学，利用深度学习进行分子亚型分类
tldr: 针对肺腺癌中端粒相关基因（TRGs）作用机制不明的问题，本研究整合多组学数据与病理图像，通过聚类分析将患者分为两种分子亚型。结果显示，亚型1具有较好的免疫浸润和预后，而亚型2虽有高突变负荷却表现出免疫抑制特征；研究还开发了深度学习模型实现病理切片的亚型预测，为肺腺癌的精准分型和个性化治疗提供了重要参考。
selection_source: fresh_fetch
motivation: 探究端粒相关基因在肺腺癌发生发展及免疫逃逸中的具体作用，以解决目前临床上缺乏有效分子分型和预后预测手段的问题。
method: 整合基因组、转录组及病理图像数据，利用共识聚类确定分子亚型，并构建CLAM、TransMIL等深度学习模型从全切片图像中预测亚型。
result: 成功将肺腺癌分为预后良好且免疫响应积极的亚型1，以及表现出显著T细胞耗竭和免疫耐药特征的亚型2，并发现特定肠道微生物与亚型相关。
conclusion: 端粒相关基因的表达特征可作为肺腺癌分子分型和治疗指导的重要依据，为实现个性化诊疗奠定了基础。
---

## 摘要
背景：位于染色体末端的端粒调节细胞分裂并维持基因组稳定性。端粒相关基因（TRGs）在肿瘤发生和免疫逃逸中发挥着至关重要的作用，但其在肺腺癌（LUAD）中的作用机制尚未完全明确。方法：本研究整合了基因组学、转录组学和病理图像，分析了 LUAD 中 TRGs 的表达情况。通过单变量 Cox 回归鉴定了 278 个与预后相关的 TRGs。利用一致性聚类将 1086 名 LUAD 患者分为两个不同的分子亚型（Cluster 1 和 Cluster 2）。通过非负矩阵分解（NMF）和最近模板预测（NTP）验证了可靠性，并构建了深度学习模型（CLAM、TransMIL、CAMIL）以从全视野数字化切片（WSIs）中预测这些分子亚型。结果：研究发现 TRG 激活与 LUAD 的发生、进展和不良预后相关。基于 TRG 表达的分层识别出了具有不同临床结局的亚型。具体而言，Cluster 1 表现出更高的 KRAS 突变频率，伴有高微卫星不稳定性（MSI）、免疫浸润增加和免疫循环激活，且对免疫检查点阻断（ICB）治疗反应更好，患者预后更佳。相比之下，Cluster 2 的特征是高肿瘤突变负荷（TMB）和同源重组缺陷（HRD）。尽管这些基因组特征预期会增强肿瘤免疫原性，但 Cluster 2 表现出深刻的适应性免疫耐药，包括显著的 T 细胞耗竭（LAG3 和 TIGIT 升高）以及深刻的免疫抑制肿瘤微环境（TME）。微生物谱分析进一步显示，布劳特氏菌属（Blautia）、普拉梭菌属（Faecalibacterium）和明串珠菌属（Leuconostoc）在 Cluster 1 中显著富集。最后，我们开发了一个能够准确预测基于 TRG 亚型的深度学习模型，为该分类框架的潜在临床应用提供了初步支持。结论：本研究阐明了 TRGs 表达与 LUAD 生物学特征之间的关联，强调了它们在分子分型和治疗指导中的潜在临床意义，为 LUAD 的个体化诊疗策略奠定了基础。

## Abstract
BACKGROUND: Telomeres, located at chromosome ends, regulate cell division and maintain genomic stability. Telomere-related genes (TRGs) play essential roles in tumorigenesis and immune escape, but their mechanisms in lung adenocarcinoma (LUAD) are not fully understood. METHODS: This study integrated genomics, transcriptomics and pathological images to analyze TRGs expression in LUAD. Univariate Cox regression identified 278 TRGs linked to prognosis. Using consensus clustering, 1086 LUAD patients were classified into two distinct molecular subtypes (Cluster 1 and Cluster 2). Reliability was validated through non-negative matrix factorization (NMF) and nearest template prediction (NTP), and deep learning models (CLAM, TransMIL, CAMIL) were constructed to predict these molecular subtypes from whole-slide images (WSIs). RESULTS: Our study found that TRG activation is associated with the occurrence, progression, and poor prognosis of LUAD. TRG expression-based stratification identified subtypes with distinct clinical outcomes. Specifically, Cluster 1 showed a higher frequency of KRAS mutations, together with high microsatellite instability (MSI), increased immune infiltration, and activation of the immune cycle, along with a better response to immune checkpoint blockade (ICB) therapy and more favorable patient prognosis. In contrast, Cluster 2 was characterized by high tumor mutational burden (TMB) and homologous recombination deficiency (HRD). Although these genomic features would be expected to enhance tumor immunogenicity, Cluster 2 exhibited profound adaptive immune resistance, including marked T-cell exhaustion (elevated LAG3 and TIGIT) and a profoundly immunosuppressive tumor microenvironment (TME). Microbial profiling further revealed that the genera Blautia, Faecalibacterium, and Leuconostoc were significantly enriched in Cluster 1. Finally, we developed a deep learning model that accurately predicts TRG-based subtypes, providing preliminary support for the potential clinical utility of this classification framework. CONCLUSION: This study clarifies the association between TRGs expression and the biological characteristics of LUAD, highlighting their potential clinical significance in molecular typing and therapeutic guidance, and laying a foundation for personalized diagnosis and treatment strategies for LUAD.