---
title: Rapid detection of NDM-producing carbapenem-resistant Escherichia coli using MALDI-TOF MS combined with machine learning techniques.
title_zh: 基于 MALDI-TOF MS 结合机器学习技术快速检测产 NDM 型碳青霉烯耐药大肠埃希菌
authors: "Rongrong Dong, Yifei Wang, Lei Song, Jiayin Wang, Chun Yang, Xufeng Ji, Qi Zhou, Hao Wang, Xinhua Guo, Jiancheng Xu"
date: 2026-04-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/41619912/"
tags: ["query:pathoai"]
score: 9.0
evidence: 机器学习用于碳青霉烯耐药大肠杆菌检测
tldr: 针对产 NDM 酶的耐药大肠埃希菌（CREC）检测慢、传播快的问题，本研究结合 MALDI-TOF 质谱技术与机器学习算法，通过引入新型复合基质提升蛋白质图谱分辨率。利用随机森林模型实现了对 NDM 阳性菌株的高精度识别（AUC 达 0.993），并锁定了 4 个关键特征峰，为临床快速诊断耐药菌提供了高效、准确的技术手段。
selection_source: fresh_fetch
motivation: 产 NDM 酶的耐药大肠埃希菌对公共卫生威胁巨大，临床急需一种比传统 PCR 更快速、可靠的自动化检测手段。
method: 采集临床菌株并利用复合基质改进质谱分析，通过对比九种机器学习算法筛选出最优的随机森林模型来识别耐药特征峰。
result: 随机森林模型在识别 NDM 菌株上表现优异（AUC 0.993），并成功鉴定出 4 个与 NDM 基因表达直接相关的特异性离子峰。
conclusion: 质谱技术结合机器学习与复合基质改进，能够实现对产 NDM 耐药菌的快速精准鉴定，显著提升了医院感染控制的效率。
---

## 摘要
背景：产新德里金属 β-内酰胺酶（NDM）的碳青霉烯耐药大肠埃希菌（CREC）对全球公共卫生构成重大威胁。及时检测 CREC 对于有效的患者管理和遏制耐药性传播至关重要。目的：本研究旨在利用基质辅助激光解吸电离飞行时间质谱（MALDI-TOF MS）结合机器学习（ML）技术，建立一种快速且可靠的产 NDM 型 CREC 检测方法。方法：收集 2018 年 8 月至 2022 年 12 月期间吉林大学第一医院临床实验室的大肠埃希菌临床分离株。采用聚合酶链反应（PCR）检测分离株中的 23 种常见耐药基因。利用 MALDI-TOF MS 分析蛋白质图谱，并使用由 (E)-丙基 α-氰基-4-羟基肉桂酸酯（CHCA-C3）和 α-氰基-4-羟基肉桂酸（CHCA）组成的协同基质。通过对九种机器学习算法的对比分析，确定了最优算法并用于寻找 NDM 特异性离子峰。此外，将 NDM 基因克隆到标准大肠埃希菌株 ATCC 25922 中，以验证这些特异性峰的可靠性。结果：共 154 株大肠埃希菌被分为三组：45 株 CREC 菌株、58 株产超广谱 β-内酰胺酶（ESBL）菌株以及 51 株非 CREC 且非产 ESBL 菌株。PCR 扩增鉴定出 12 种耐药基因。建立的基于随机森林算法的机器学习模型表现出优异的判别能力，AUC 达到 0.993，AP 达到 0.997。使用协同基质鉴定了四个 NDM 特异性峰（m/z 5132、m/z 5209、m/z 6350 和 m/z 6371）。相比之下，传统的 CHCA 基质未发现特异性峰。此外，在重组大肠埃希菌株 ATCC 25922-PZY01/NDM 的 MALDI-TOF MS 图谱中检测到了 m/z 5132 和 m/z 5209 的特异性峰，这与 NDM 基因的表达直接相关。结论：通过协同基质方法，将 MALDI-TOF MS 与机器学习技术相结合，实现了对产 NDM 型 CREC 的快速、精准鉴定。这一进展显著增强了临床管理和医院感染控制的有效性。

## Abstract
BACKGROUND: Carbapenem-resistant Escherichia coli (CREC) producing New Delhi metallo-beta-lactamase (NDM) poses a substantial threat to global public health. Prompt detection of CREC is essential for effective patient management and to curb the spread of resistance. OBJECTIVE: This study aims to establish a rapid and reliable detection method for NDM-producing CREC using matrix-assisted laser desorption ionization time-of-flight mass spectrometry (MALDI-TOF MS) in conjunction with machine learning (ML) techniques. METHODS: Clinical isolates of E. coli were collected from the First Hospital of Jilin University's clinical laboratory from August 2018 to December 2022. Polymerase chain reaction was employed to detect 23 prevalent resistance genes in the isolates. Protein profiles were analysed by MALDI-TOF MS with a cooperative matrix consisting of (E)-propyl α-cyano-4-hydroxylcinnamylate (CHCA-C3) and α-cyano-4-hydroxycinnamic acid (CHCA). By comparative analysis of nine ML algorithms, the optimal algorithm was identified and used to find the NDM-specific ion peaks. Furthermore, the NDM gene was cloned into the standard E. coli strain ATCC 25922 to verify the reliability of these specific peaks. RESULTS: A total of 154 E. coli strains were categorized into three groups: 45 CREC strains, 58 extended-spectrum beta-lactamase-producing strains, and 51 non-CREC, non-extended-spectrum beta-lactamase strains. Polymerase chain reaction amplification identified 12 resistance genes. The established ML model with random forest algorithm exhibits excellent discriminative ability, achieving an AUC of 0.993 and an AP of 0.997. Four specific peaks (m/z 5132, m/z 5209, m/z 6350, and m/z 6371) of NDM were identified using the cooperative matrix. In contrast, the traditional CHCA matrix revealed no specific peaks. Furthermore, the specific peaks at m/z 5132 and m/z 5209 were detected in the MALDI-TOF MS spectra of the recombinant E. coli strain ATCC 25922-PZY01/NDM, which directly correlated with the expression of the NDM gene. CONCLUSIONS: The integration of MALDI-TOF MS with ML techniques, facilitated by the cooperative matrix approach, has enabled the swift and precise identification of NDM-producing CREC. This advancement significantly enhances the effectiveness of clinical management and the control of hospital-acquired infections.