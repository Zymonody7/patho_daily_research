---
title: Integrated microneedle patch and machine learning in time-resolved fluorescent immunochromatography test strip for accurate and rapid detection of Staphylococcus aureus enterotoxin B in salmon.
title_zh: 集成微针贴片与机器学习的时间分辨荧光免疫层析试纸条，用于准确、快速检测三文鱼中的金黄色葡萄球菌肠毒素B
authors: "Hui Jiang, Hui Du, Donglei Jiang, Xinmei Liu, Haijing Wu, Mengjing Huang, Rui Sun, Xiaojie Sun, Siqi Zeng, Yanmin Ju, Jun Yang"
date: 2026-05-16
pdf: "https://pubmed.ncbi.nlm.nih.gov/41806717/"
tags: ["query:pathoai"]
score: 8.0
evidence: 机器学习用于金黄色葡萄球菌肠毒素的快速检测
tldr: 针对三文鱼中金黄色葡萄球菌肠毒素B（SEB）检测效率低的问题，该研究集成水凝胶微针贴片（HMNP）、时间分辨荧光免疫层析（TRFITS）与机器学习算法。通过微针快速提取样本液，结合TRFITS显色，并利用YOLOv11模型进行浓度预测。该方案在32分钟内实现了高精度定量检测，检出限降至2 ng/mL，为食品安全现场快速检测提供了新思路。
selection_source: fresh_fetch
motivation: 旨在解决传统食品致病菌毒素检测耗时长、操作复杂且难以在现场进行精确定量分析的挑战。
method: 采用甲基丙烯酰化明胶制备微针贴片提取样本，并结合时间分辨荧光免疫层析技术与YOLOv11深度学习模型进行图像识别与浓度预测。
result: "系统在32分钟内完成检测，YOLOv11模型预测准确率达91.3%，并将检测下限从4.63 ng/mL优化至2 ng/mL。"
conclusion: 这种集成微针采样与机器学习辅助分析的检测平台，显著提升了食品安全监测的灵敏度与便捷性。
---

## 摘要
金黄色葡萄球菌肠毒素B (SEB) 是引起食源性疾病的主要原因。在本研究中，我们开发了一种结合水凝胶微针贴片 (HMNP) 和机器学习 (ML) 的时间分辨荧光免疫层析试纸条 (TRFITS)，用于快速检测三文鱼中的 SEB。所开发的 HMNP 由甲基丙烯酰化明胶制成，可在 6 分钟内自动提取 37 mg 组织间液。随后，我们对三文鱼样本进行了 TRFITS 分析以检测 SEB，并利用 ML 算法预测其浓度。该方法实现了 32 分钟内对 SEB 的高效采样和准确定量，检出限 (LOD) 为 4.63 ng/mL。此外，应用于三文鱼的 ML 辅助 TRFITS 表明，YOLOv11 模型实现了 91.3% 的预测准确率和更低的 LOD (2 ng/mL)。这些研究结果突出了一种现场检测 SEB 的新方法，对食品安全监测和即时诊断应用具有重要意义。

## Abstract
Staphylococcus aureus enterotoxin B (SEB) is a leading cause of foodborne illness. In this study, we developed a time-resolved fluorescent immunochromatography test strip (TRFITS) combined with a hydrogel microneedle patch (HMNP) and machine learning (ML) for the rapid detection of SEB in salmon. The developed HMNP, fabricated from methacrylated gelatin, can automatically extract 37 mg of interstitial fluid within 6 min. We then conducted TRFITS analysis on salmon samples to detect SEB and ML algorithms so as to predict its concentration. This method enabled efficient sampling and accurate quantification of SEB within 32 min, with a limit of detection (LOD) of 4.63 ng/mL. In addition, ML-assisted TRFITS applied to salmon demonstrated that the YOLOv11 model achieved a prediction accuracy of 91.3% and a lower LOD of 2 ng/mL. These findings highlight a novel approach toward on-site SEB detection with significant implications for food safety monitoring and point-of-care diagnostic applications.