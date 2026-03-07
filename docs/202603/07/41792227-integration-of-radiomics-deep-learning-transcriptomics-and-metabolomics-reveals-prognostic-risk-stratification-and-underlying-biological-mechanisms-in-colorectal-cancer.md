---
title: "Integration of radiomics, deep learning, transcriptomics, and metabolomics reveals prognostic risk stratification and underlying biological mechanisms in colorectal cancer."
title_zh: 整合影像组学、深度学习、转录组学和代谢组学揭示结直肠癌的预后风险分层及潜在生物学机制
authors: "Li Z, Cai R, Qin Y, Liao X, Wang E, Wu X, Zhao Y, Lu Z, Lin Y., Zhiheng Li, Rongzhi Cai, Yangyang Qin, Xiaoqing Liao, Enqi Wang, Xuanyu Wu, Yan Zhao, Zengxin Lu, Yan Lin"
date: 2026-03-06
pdf: "https://pubmed.ncbi.nlm.nih.gov/41792227/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 深度学习用于癌症多组学整合
tldr: 针对结直肠癌预后评估受肿瘤异质性干扰的问题，本研究通过分析1183名患者的CT影像，开发并优化了深度学习影像组学模型（DLRM）以实现风险分层。结合转录组学与代谢组学分析，研究揭示了高风险组与细胞外基质通路相关，而低风险组表现出更强的免疫浸润及丁酸代谢等保护性特征。该框架不仅提升了生存预测精度，还为理解结直肠癌的生物学机制提供了多组学证据。
selection_source: fresh_fetch
motivation: 结直肠癌的高异质性使得现有的临床预后评估方法难以精准预测患者的生存风险和治疗反应。
method: 利用来自四个中心的1183例CT影像数据，通过系统评估117种机器学习算法组合，构建并优化了深度学习影像组学模型（DLRM）。
result: 模型成功实现了患者的风险分层，并发现高风险肿瘤富集细胞外基质相关通路，而低风险肿瘤则表现出更高的CD8+ T细胞浸润及丁酸代谢等保护性特征。
conclusion: 该多组学集成框架为结直肠癌提供了稳健的风险分层工具，并揭示了与肿瘤进展相关的生物学过程及潜在的治疗靶点。
---

## 摘要
结直肠癌（CRC）是全球范围内第三大常见恶性肿瘤，也是癌症相关死亡的第二大原因，然而目前的预后分层受到肿瘤异质性的阻碍。在本研究中，我们利用来自四个中心的1183名患者的静脉期计算机断层扫描（CT）图像，通过对117种组合中的十种机器学习算法进行系统评估，开发并优化了一个深度学习影像组学模型（DLRM）。由此产生的风险分层将患者分为具有显著生存差异的高风险组和低风险组，且与临床因素的整合进一步提高了预测性能。整合转录组学和代谢组学分析显示，高风险肿瘤富集了与肿瘤进展相关的细胞外基质（ECM）相关通路，而低风险肿瘤则表现出免疫相关特征，包括较高的CD8⁺ T细胞浸润。两种组学一致地将丁酸代谢和氮代谢鉴定为保护性通路，并在一个独立的公共队列（n = 417）中得到了验证。这一整合分析框架提供了稳健的风险分层，并揭示了具有潜在治疗意义的生物学过程。

## Abstract
Colorectal cancer (CRC) is the third most common malignancy and the second leading cause of cancer-related death worldwide, yet current prognostic stratification is hindered by tumor heterogeneity. Here, we developed a deep learning radiomics model (DLRM), optimized through systematic evaluation of ten machine learning algorithms across 117 combinations, using venous-phase computed tomography (CT) images of 1183 patients from four centers. The resulting risk stratification stratified patients into high- and low-risk groups with distinct survival outcomes, and integration with clinical factors further improved prediction. Integrative transcriptomic and metabolomic analyses revealed that high-risk tumors were enriched for extracellular matrix (ECM)-related pathways associated with tumor progression, whereas low-risk tumors exhibited immune-related signatures, including higher CD8⁺ T-cell infiltration. Both omics consistently identified butanoate metabolism and nitrogen metabolism as protective pathways, validated in an independent public cohort (n = 417). This integrative analytic framework provides robust risk stratification and uncovers biological processes with potential therapeutic relevance.