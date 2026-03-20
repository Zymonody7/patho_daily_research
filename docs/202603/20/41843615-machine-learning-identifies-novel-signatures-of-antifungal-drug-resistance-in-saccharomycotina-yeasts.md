---
title: Machine learning identifies novel signatures of antifungal drug resistance in Saccharomycotina yeasts.
title_zh: 机器学习识别出酵母亚门真菌中抗真菌药物抗性的新特征
authors: "Marie-Claire Harrison, David C Rinker, Abigail L LaBella, Dana A Opulente, John F Wolters, Xiaofan Zhou, Xing-Xing Shen, Marizeth Groenewald, Chris Todd Hittinger, Antonis Rokas"
date: 2026-03-17
pdf: "https://pubmed.ncbi.nlm.nih.gov/41843615/"
tags: ["query:pathoai"]
score: 9.0
evidence: 基于基因组数据训练随机森林算法进行抗真菌耐药性预测
tldr: 针对真菌耐药性在跨物种演化中缺乏广谱解释的问题，本研究利用近乎所有已知酵母亚门物种的基因组与表型数据，采用随机森林算法预测了对八种抗真菌药物的耐药性。研究发现氟康唑耐药性的预测准确率最高，并识别出与临床菌株完全不同的关键氨基酸位点。这些天然变异位点在能量上更稳定，揭示了自然界中广泛存在的耐药机制，为理解真菌耐药演化提供了新视角。
selection_source: fresh_fetch
motivation: 探究临床已知的真菌耐药基因突变是否能解释整个酵母亚门在自然界中的广谱耐药性。
method: 收集了近乎所有已知酵母物种的基因组和表型数据，利用随机森林模型基于蛋白质功能注释和关键蛋白序列进行耐药性分类预测。
result: 机器学习成功预测了多种药物的耐药性，并发现决定自然界耐药性的关键蛋白位点与临床常见位点并不重合，且在结构上更具稳定性。
conclusion: 研究非临床环境下的自然耐药性能够揭示被临床研究忽视的演化机制，从而更全面地理解真菌耐药性的起源与演变。
---

## 摘要
抗真菌药物抗性是真菌感染管理中的一个主要挑战。已知许多基因组变化会导致特定病原体临床分离株产生获得性耐药性，但这些变化是否能广泛解释整个谱系的天然抗性尚不清楚。我们利用了来自酵母亚门（Saccharomycotina）几乎所有已知物种的自然采样菌株的基因组、生态和表型性状数据，研究了对八种抗真菌药物抗性的演化。药物抗性的系统发育分布因药物而异；氟康唑抗性广泛存在，而 5-氟胞嘧啶抗性则很少见，脂霉目（Lipomycetales）除外。在基因组数据上训练的随机森林算法预测耐药酵母的准确率为 54-75%。氟康唑抗性的预测准确率始终最高（75.2%）。此外，基于酵母亚门全基因组范围内 InterPro 蛋白质注释的存在与数量变异训练的模型（75.2%），与基于已知参与氟康唑抗性的蛋白质 Erg11 的氨基酸序列比对数据训练的模型（74.3-74.9%），在氟康唑抗性预测准确率上表现相似。有趣的是，用于预测整个酵母亚门氟康唑抗性的主要 Erg11 残基，与先前在白念珠菌（Candida albicans）临床分离株中发现的与抗性相关的残基并不重叠，在空间上也不接近，且保守性较低。对白念珠菌 Erg11 蛋白的计算机模拟深度突变扫描显示，临床抗性病例中涉及的氨基酸变异几乎普遍具有去稳定作用，而我们最具信息量的残基中的变异在能量上更趋于中性，这解释了为什么后者在自然种群中比前者更常见。重要的是，先前对白念珠菌 Erg11 的实验分析表明，尽管我们最具信息量的残基中的氨基酸变异从未直接涉及临床病例，但它们可以直接导致抗性。我们的结果表明，对临床上从未遇到过的酵母物种的天然抗性研究，将有助于更全面地理解抗真菌药物抗性。

## Abstract
Antifungal drug resistance is a major challenge in fungal infection management. Numerous genomic changes are known to contribute to acquired drug resistance in clinical isolates of specific pathogens, but whether they broadly explain natural resistance across entire lineages is unknown. We leveraged genomic, ecological, and phenotypic trait data from naturally sampled strains from nearly all known species in subphylum Saccharomycotina to examine the evolution of resistance to eight antifungal drugs. The phylogenetic distribution of drug resistance varied by drug; fluconazole resistance was widespread, while 5-fluorocytosine resistance was rare, except in Lipomycetales. A random forest algorithm trained on genomic data predicted drug-resistant yeasts with 54-75% accuracy. Fluconazole resistance was consistently predicted with the highest accuracy (75.2%). Furthermore, fluconazole resistance prediction accuracy was similar between models trained on genome-wide variation in the presence and number of InterPro protein annotations across Saccharomycotina (75.2%) and those trained on amino acid sequence alignment data of Erg11, a protein known to be involved in fluconazole resistance (74.3-74.9%). Interestingly, the top Erg11 residues for predicting fluconazole resistance across Saccharomycotina do not overlap with, are not spatially close to, and are less conserved than those previously linked to resistance in clinical isolates of Candida albicans. In silico deep mutational scanning of the C. albicans Erg11 protein reveals that amino acid variants implicated in clinical cases of resistance are almost universally destabilizing while variants in our most informative residues are energetically more neutral, explaining why the latter are much more common than the former in natural populations. Importantly, previous experimental analyses of C. albicans Erg11 have shown that amino acid variation in our most informative residues, despite having never been directly implicated in clinical cases, can directly contribute to resistance. Our results suggest that studies of natural resistance in yeast species never encountered in the clinic will yield a fuller understanding of antifungal drug resistance.