---
title: "PTBD: a machine learning-based non-invasive diagnostic model for pulmonary tuberculosis using large-scale blood transcriptomes."
title_zh: PTBD：一种基于大规模血液转录组的机器学习非侵入性肺结核诊断模型
authors: "Changchun Wu, Xueqin Xie, Ziru Huang, Yuwei Zhou, Yushu Gou, Mengze Du, Hao Lin, Jian Huang"
date: 2026-03-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/41888771/"
tags: ["query:pathoai"]
score: 8.0
evidence: 利用血液转录组进行结核病诊断的机器学习
tldr: 肺结核（PTB）的快速准确诊断对控制疫情至关重要，但现有方法在灵敏度和实用性上存在局限。本研究开发了PTBD模型，通过整合最高得分对（TSP）算法与机器学习，分析了近三千例外周血转录组样本。该模型在区分PTB与肺炎、肺癌等复杂背景时表现优异，外部验证AUC达0.909，且在HIV感染、耐药等特殊人群中保持稳健，为临床早期筛查和预后评估提供了非侵入性的分子诊断工具。
selection_source: fresh_fetch
motivation: 针对现有肺结核诊断方法在复杂临床环境下灵敏度不足且难以兼顾多种并发症的问题，亟需一种稳健的非侵入性生物标志物检测手段。
method: 该研究利用2792份大规模外周血转录组数据，结合最高得分对（TSP）算法与机器学习技术，构建了基于基因对表达模式的诊断模型PTBD。
result: 模型在独立验证集中达到0.909的AUC，能有效区分肺结核与肺癌、肺炎等疾病，并满足世界卫生组织对特殊人群（如HIV感染者和儿童）的筛查标准。
conclusion: PTBD模型不仅实现了肺结核的高精度早期诊断，还通过识别五个关键基因对揭示了疾病进展的分子特征，具有极高的临床应用和预后预测价值。
---

## 摘要
背景：准确、快速的诊断对于通过及时干预和减少疾病传播来控制肺结核（PTB）至关重要。现有的肺结核诊断方法在灵敏度、特异性或实用性方面存在局限性。结果：在此，我们提出了一种基于非侵入性血液转录组的诊断模型，该模型将最高得分对（top-scoring pair）与机器学习相结合，为各类肺结核患者识别出新型且稳健的转录组生物标志物。利用 2,792 份外周血转录组样本，所提出的模型（PTBD）能有效区分肺结核与健康个体、潜伏性结核感染、肺炎、肺癌和肺结节，反映了其在真实临床环境中典型的复杂且异质的阴性样本背景下的稳健性，在测试集和独立外部验证集中分别实现了 0.869 和 0.909 的 AUC。其性能在不同地理区域、年龄组和特殊情况（包括卡介苗接种、HIV 感染、糖尿病和耐药性）下保持一致，满足了世界卫生组织（WHO）对社区分诊、儿童以及合并 HIV 感染的肺结核患者的诊断要求。此外，PTBD 还能实现肺外结核的诊断和治疗结果的预测，其特征评分可作为反映疾病进展和预后的分子生物标志物。结论：本研究为肺结核的早期诊断提供了一种广泛适用的工具，有助于及时干预并可能减轻全球肺结核负担。此外，PTBD 揭示了新型转录组生物标志物，以五个诊断基因对表达模式为代表，体现了肺结核的分子特征。

## Abstract
BACKGROUND: Accurate and rapid diagnosis is essential for controlling pulmonary tuberculosis (PTB) by enabling timely intervention and reducing disease transmission. Existing diagnostic methods for PTB are limited by sensitivity, specificity, or practicality. RESULTS: Here, we present a non-invasive blood transcriptome-based diagnostic model that integrates top-scoring pair with machine learning, identifying novel and robust transcriptomic biomarkers for diverse PTB patients. Using 2,792 peripheral blood transcriptome samples, the proposed model (PTBD) effectively distinguishes PTB from healthy individuals, latent tuberculosis infection, pneumonia, lung cancer, and pulmonary nodules, reflecting its robustness against the complex and heterogeneous negative sample background typical of real-world clinical settings, and achieving AUCs of 0.869 in the test set and 0.909 in an independent external validation set. Its performance is consistent across different geographic regions, age groups, and special conditions, including Bacillus Calmette-Guérin vaccination, HIV infection, diabetes, and drug resistance, meeting WHO requirements for community-based triage, children, and PTB with HIV infection. Furthermore, PTBD also enables diagnosis of extrapulmonary tuberculosis and prediction of treatment outcomes, with feature scores serving as molecular biomarkers reflecting disease progression and prognosis. CONCLUSIONS: This study provides a broadly applicable tool for early PTB diagnosis, facilitating timely intervention and potentially reducing global PTB burden. Moreover, PTBD uncovers novel transcriptomic biomarkers, represented by five diagnostic gene-pair expression patterns that embody the molecular hallmarks of PTB.