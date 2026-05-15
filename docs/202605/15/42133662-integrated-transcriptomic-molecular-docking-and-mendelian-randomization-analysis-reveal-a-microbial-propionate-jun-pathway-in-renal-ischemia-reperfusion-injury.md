---
title: "Integrated transcriptomic, molecular docking, and mendelian randomization analysis reveal a microbial-propionate-JUN pathway in renal ischemia-reperfusion injury."
title_zh: 整合转录组学、分子对接和孟德尔随机化分析揭示了肾缺血再灌注损伤中的微生物-丙酸-JUN通路
authors: "Jun Li, Ruizhen Huang, Xing Wang, Yunfeng Zhang, Zuhuan Xu, Penglin Zhang, Honglin Hu"
date: 2026-12-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/42133662/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 整合转录组学和分子对接研究宿主-微生物相互作用
tldr: 针对肾缺血再灌注损伤（IRI）中肠道菌群作用机制不明的问题，本研究整合转录组分析、分子对接与孟德尔随机化（MR）因果推断，识别出JUN作为连接菌群代谢物与肾脏炎症信号的关键枢纽。研究发现Akkermansia muciniphila与Ruminococcus bromii通过共有代谢物丙酸盐作用于JUN蛋白，进而调控TNF/IL-17通路，揭示了“菌群-丙酸盐-JUN”这一潜在的肠肾调节轴，为肾损伤干预提供了分子层面的新见解。
selection_source: fresh_fetch
motivation: 旨在探究肠道菌群及其代谢物在肾缺血再灌注损伤（IRI）引发的炎症反应中的具体调控机制。
method: 结合转录组差异基因筛选、基于数据库的代谢物靶点预测、孟德尔随机化因果分析及分子动力学模拟，实现从宏观菌群到微观分子结合的多尺度关联建模。
result: 锁定JUN为介导炎症的关键枢纽基因，证实丙酸盐与JUN具有高亲和力结合能，并量化了特定菌群对肾损伤易感性的因果效应。
conclusion: 揭示了由特定肠道菌群、丙酸盐代谢物及JUN信号通路构成的肠肾调节轴，为理解肾脏炎症损伤提供了系统性的生物学解释。
---

## 摘要
肾缺血再灌注损伤 (IRI) 是急性肾损伤的主要原因，其特征是氧化应激、免疫细胞浸润和炎症信号激活。虽然肠道微生物群及其代谢物（尤其是短链脂肪酸）参与了全身免疫调节，但它们在肾 IRI 中的作用仍不清楚。在本研究中，我们整合了转录组分析、肠道来源代谢物靶点预测、分子对接和孟德尔随机化 (MR)，以探索肾 IRI 中潜在的微生物-代谢物-宿主调节机制。我们利用 gutMGene、Similarity Ensemble Approach 和 SwissTargetPrediction 数据库鉴定了 32 个肠道来源代谢物的靶基因。在两个肾 IRI 数据集（GSE126805 和 GSE90861）中，分别鉴定出 263 个和 641 个差异表达基因，核心基因主要富集在 TNF 和 IL-17 信号通路中。其中，JUN 被鉴定为连接肠道微生物群相关代谢物与肾脏炎症信号的关键核心。MR 分析显示，嗜黏蛋白阿克曼氏菌 (Akkermansia muciniphila) 与肾损伤易感性呈正相关 [p = 0.026, 比值比 (OR) = 1.219]，而布氏瘤胃球菌 (Ruminococcus bromii) 与肾损伤易感性呈负相关 (p = 0.011, OR = 0.740)。由于丙酸（而非丁酸）是与这两个菌属相关的共同代谢物，随后的分析重点关注了丙酸-JUN 的相互作用。分子对接和动力学模拟支持丙酸与 JUN 之间的强结合。总之，这些发现提示在肾 IRI 中存在一个涉及 A. muciniphila/R. bromii-丙酸-JUN-TNF/IL-17 信号通路的潜在肠-肾调节轴，为微生物相关的肾脏炎症损伤机制提供了新见解。

## Abstract
Renal ischemia-reperfusion injury (IRI) is a major cause of acute kidney injury and is characterized by oxidative stress, immune cell infiltration, and inflammatory signaling activation. Although gut microbiota and their metabolites, especially short-chain fatty acids, are involved in systemic immune regulation, their role in renal IRI remains unclear. Here, we integrated transcriptomic analysis, gut-derived metabolite target prediction, molecular docking, and Mendelian randomization (MR) to explore potential microbiota-metabolite-host regulatory mechanisms in renal IRI. We identified 32 target genes of gut-derived metabolites using the gutMGene, Similarity Ensemble Approach, and SwissTargetPrediction databases. In two renal IRI datasets (GSE126805 and GSE90861), 263 and 641 differentially expressed genes were identified, respectively, and hub genes were mainly enriched in the TNF and IL-17 signaling pathways. Among them, JUN was identified as a key hub linking gut microbiota-associated metabolites to renal inflammatory signaling. MR analysis showed that Akkermansia muciniphila was positively associated with kidney injury susceptibility [p = 0.026, odds ratio (OR) = 1.219], whereas Ruminococcus bromii was negatively associated with kidney injury susceptibility (p = 0.011, OR = 0.740). Because propionate, rather than butyrate, was the shared metabolite associated with both taxa, subsequent analyses focused on the propionate-JUN interaction. Molecular docking and dynamics supported strong binding between propionate and JUN. Overall, these findings suggest a potential gut-kidney regulatory axis involving A. muciniphila/R. bromii-propionate-JUN-TNF/IL-17 signaling in renal IRI, providing new insight into microbiota-associated mechanisms of renal inflammatory injury.