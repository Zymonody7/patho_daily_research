---
title: Machine learning-based prediction of BV-relevant probiotic functional potential in vaginal-derived Lactobacillus crispatus strains.
title_zh: 基于机器学习的阴道来源卷曲乳杆菌菌株中 BV 相关益生功能潜力的预测
authors: "Keyu Quan, Weichi Liu, Hao Jin, Weiwei Hu, Qinggele Borjihan, Qiuhua Bao, Yongfu Chen"
date: 2026-03-17
pdf: "https://pubmed.ncbi.nlm.nih.gov/41845201/"
tags: ["query:pathoai"]
score: 9.0
evidence: 机器学习预测阴道微生物群中益生菌的功能潜力
tldr: 针对阴道益生菌筛选成本高、效率低的问题，本研究通过对639株卷曲乳杆菌进行体外功能实验并建立加权评分体系，结合k-mer基因组特征和多阶段特征选择策略，开发了机器学习预测工具VLCPredictor。该工具能高效评估菌株在维持阴道微生态平衡及防治妇科感染方面的功能潜力，为女性生殖健康益生菌的精准开发提供了高效的计算框架。
selection_source: fresh_fetch
motivation: 传统的阴道益生菌筛选依赖高成本、高强度的体外实验，且现有益生菌产品大多针对肠道疾病而非女性生殖健康。
method: 利用k-mer基因组特征结合多阶段特征选择策略，训练多种机器学习算法构建了名为VLCPredictor的菌株功能潜力预测流水线。
result: 通过对639株卷曲乳杆菌的体外实验数据进行加权评分，成功筛选出3株最优菌株，并验证了模型在预测菌株益生功能上的准确性。
conclusion: 该研究证明了基于基因组数据的机器学习模型可以有效加速阴道益生菌的开发，为维持女性生殖系统微生态平衡提供了技术支持。
---

## 摘要
阴道微生物群在维持女性生殖健康和稳态中发挥着关键作用。然而，目前大多数可用的乳杆菌分离株主要是为预防和治疗肠道疾病而开发的，而针对女性生殖健康的菌株特异性研究仍然有限。传统的培养和筛选策略通常伴随着高昂的成本和大量的劳动力需求。机器学习能够快速分析大规模组学数据，促进候选益生菌的高效识别。本研究使用三种选择性培养基从健康女性的阴道分泌物中分离出总共 639 株卷曲乳杆菌（Lactobacillus crispatus）。基于系统发育树分析，选择了 67 株代表性菌株进行体外实验，包括生长能力、酸化能力（pH 降低）、乳酸产量、过氧化氢产量和抗菌活性。随后根据这些结果建立了一个加权评分系统，从而鉴定了三株具有最佳综合性能的卷曲乳杆菌菌株。最后，通过整合菌株基于 k-mer 的基因组特征，采用多阶段特征选择策略并结合多种机器学习算法，开发了一个预测流程 VLCPredictor。该流程能够对阴道来源卷曲乳杆菌菌株的功能潜力进行评分。我们的研究为卷曲乳杆菌在女性生殖道健康中的开发和应用提供了一个高效的框架，对维持女性生殖系统的微生物平衡以及预防和治疗妇科感染性疾病具有重要意义。

## Abstract
The vaginal microbiota plays a pivotal role in maintaining female reproductive health and homeostasis. However, most currently available Lactobacillus isolates have been developed for the prevention and treatment of intestinal diseases, whereas strain-specific investigations targeting female reproductive health remain limited. Conventional cultivation and screening strategies are often associated with high costs and substantial labor requirements. Machine learning enables rapid analysis of large-scale omics data, facilitating efficient identification of candidate probiotics. A total of 639 Lactobacillus crispatus isolates were recovered from vaginal secretions of healthy women using three selective media. Based on phylogenetic tree analysis, 67 representative strains were selected for in vitro assays including growth capacity, acidification capacity (pH reduction), lactic acid production, hydrogen peroxide production, and antimicrobial activity. A weighted scoring system was subsequently established based on these results, leading to the identification of three Lactobacillus crispatus strains with optimal overall performance. Finally, by integrating k-mer-based genomic features of the strains, a multi-stage feature selection strategy was employed in combination with multiple machine learning algorithms to develop a predictive pipeline, VLCPredictor. This pipeline is capable of scoring the functional potential of vaginal-derived Lactobacillus crispatus strains. Our study provides an efficient framework for the development and application of Lactobacillus crispatus in female reproductive tract health. It may support significant implications for maintaining microbial equilibrium in the female reproductive system, as well as for the prevention and treatment of gynecological infectious diseases.