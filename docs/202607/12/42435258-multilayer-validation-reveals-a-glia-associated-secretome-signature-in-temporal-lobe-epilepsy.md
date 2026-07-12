---
title: Multilayer Validation Reveals a Glia-Associated Secretome Signature in Temporal Lobe Epilepsy.
title_zh: 多层验证揭示颞叶癫痫中与胶质细胞相关的分泌组特征
authors: "Yang Dai, Zesheng Li, Quanlei Liu, Xiaotong Fan, Chunhao Shen, Yumin Luo, Yongzhi Shan, Guoguang Zhao"
date: 2026-07-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/42435258/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 多组学和单细胞RNA测序用于生物标志物发现
tldr: 针对颞叶癫痫（TLE）缺乏临床生物标志物的问题，研究结合小鼠模型单细胞测序与人类转录组数据，筛选出与胶质细胞激活相关的分泌蛋白。通过对患者脑脊液（CSF）进行ELISA验证和机器学习建模，确定了CXCL10、TTR等6种关键蛋白标志物。这些标志物不仅能有效区分TLE患者，还与发作频率相关，为癫痫的临床诊断和病理研究提供了新靶点。
selection_source: fresh_fetch
motivation: 旨在寻找能够反映癫痫病理变化且在临床脑脊液中稳定可测的生物标志物，以解决目前癫痫分子诊断手段匮乏的问题。
method: 整合小鼠单细胞测序、公共转录组数据及人类脑脊液样本，利用ELISA定量验证候选蛋白，并结合机器学习模型评估其诊断效能。
result: 发现CXCL10、APOE等5种蛋白在TLE患者脑脊液中显著升高，而TTR显著降低，其中CXCL10水平与术前癫痫发作频率呈正相关。
conclusion: 证实了小胶质细胞激活及胶质相关分泌组特征与颞叶癫痫进展密切相关，为未来转化医学研究提供了具有潜力的生物标志物组合。
---

## 摘要
尽管多组学研究日益揭示了与癫痫相关的分子改变，但临床上可获取、可稳定检测且具有生物学相关性的脑脊液（CSF）生物标志物仍然匮乏。本研究旨在鉴定与癫痫相关分子改变相关的可测量生物标志物。通过红藻氨酸（KA）诱导的小鼠模型、单细胞 RNA 测序以及公共转录组数据集，鉴定了与炎症、胶质细胞激活和代谢失调相关的分泌蛋白编码基因。候选生物标志物在小鼠和人类数据集中得到了验证，并使用酶联免疫吸附测定法（ELISA）在颞叶癫痫（TLE）患者和非癫痫对照组的脑脊液中进行了定量。构建了机器学习模型以评估诊断性能，并利用 SHAP 分析进行可解释性研究。六种蛋白质（C-X-C 基序趋化因子配体 10 [CXCL10]、转甲状腺素蛋白 [TTR]、载脂蛋白 E [APOE]、载脂蛋白 D [APOD]、半乳糖凝集素-3 结合蛋白 [LGALS3BP] 和溶菌酶 [LYZ]）在人类脑脊液中表现出表达失调。在 TLE 患者中，脑脊液中 CXCL10、APOE、APOD、LGALS3BP 和 LYZ 的水平显著升高，而 TTR 水平显著降低（均 p < 0.001）。机器学习模型展示了良好的分类性能，其中 TTR 和 CXCL10 是主要的贡献特征。脑脊液 CXCL10 水平与术前癫痫发作频率呈正相关（Spearman's ρ = 0.698, p < 0.0001）。来自动物模型和临床脑脊液样本的多层证据表明，小胶质细胞激活和胶质细胞相关的分子改变与 TLE 的进展有关，相关的分泌蛋白可能为未来的转化研究提供候选生物标志物。

## Abstract
Although multi-omics studies have increasingly revealed molecular alterations associated with epilepsy, clinically accessible cerebrospinal fluid (CSF) biomarkers that are stably detectable and biologically relevant remain scarce. This study aimed to identify measurable biomarkers associated with epilepsy-related molecular alterations. Kainic acid (KA)-induced mouse model, single-cell RNA sequencing, and public transcriptomic datasets identified secreted protein-coding genes associated with inflammation, glial activation, and metabolic dysregulation. Candidate biomarkers were validated across mouse and human datasets and quantified in CSF of patients with temporal lobe epilepsy (TLE) and non-epileptic controls using enzyme-linked immunosorbent assays. Machine learning models were built to evaluate diagnostic performance and interpretability using SHAP analysis. Six proteins (C-X-C motif chemokine ligand 10 [CXCL10], transthyretin [TTR], apolipoprotein E [APOE], apolipoprotein D [APOD], galectin-3-binding protein [LGALS3BP], and lysozyme [LYZ]) were dysregulated in human CSF. CSF levels of CXCL10, APOE, APOD, LGALS3BP, and LYZ were significantly elevated in TLE, whereas TTR was markedly reduced (all p < 0.001). Machine learning models demonstrated promising classification performance, with TTR and CXCL10 emerging as major contributing features. CSF CXCL10 levels positively correlated with preoperative seizure frequency (Spearman's ρ = 0.698, p < 0.0001). Multilevel evidence from animal models and clinical CSF samples indicates that microglial activation and glia-related molecular alterations are associated with TLE progression, and related secreted proteins may provide candidate biomarkers for future translational investigation.