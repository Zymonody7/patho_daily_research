---
title: Fingerprinting Fluorescent
title_zh: 荧光指纹识别
authors: "Wenxing Li, Liang Wu, Chenbin Liu, Wen Chen, Yazhou Wu, Shuchang Xu, Jie Deng, Danyu Tian, Jian Wan, Song Hu, Dongsheng Mao, Xiaoli Zhu"
date: 2026-03-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/41810482/"
tags: ["query:pathoai"]
score: 6.0
evidence: DNA自组装驱动的多重病原菌检测策略
tldr: 针对传统荧光原位杂交（FISH）技术在病原菌检测中多重检测能力受限的问题，该研究提出了一种基于DNA自组装驱动的指纹荧光原位杂交（FinFISH）策略。通过FAM、Cy3和Cy5三种荧光团的组合编码，为不同病原菌生成独特的荧光指纹，突破了成像通道数量对检测通量的限制。实验证明该方法在模拟及临床样本中均能准确识别病原菌并提供半定量信息，为临床诊断和空间微生物组学研究提供了高效工具。
selection_source: fresh_fetch
motivation: 传统FISH技术受限于荧光通道数量，难以在单次实验中同时检测多种病原菌，限制了其在高通量临床诊断中的应用。
method: 利用DNA自组装技术将三种基础荧光分子进行组合标记，为每种呼吸道病原菌构建独特的“荧光指纹”，并配合多通道反应芯片实现并行处理。
result: 该系统在模拟痰液、尿液及临床样本中成功实现了多种病原菌的准确识别，并能对混合感染进行半定量分析。
conclusion: FinFISH策略有效解决了成像系统的通量瓶颈，结合AI分析有望显著提升临床病原菌诊断和空间微生物分析的效率。
---

## 摘要
荧光原位杂交（FISH）是一种用于病原菌检测的高特异性技术，无需培养，并能同时提供病原菌丰度、形态和空间定位信息。然而，传统 FISH 有限的灵敏度和较差的多重检测能力阻碍了其更广泛的应用。在此，我们提出了一种由 DNA 自组装驱动的指纹荧光原位杂交（FinFISH）策略，用于多重病原菌检测。以呼吸道病原体为代表模型，FinFISH 采用三种不同的荧光团进行组合标记，为每个物种生成可识别的荧光指纹。在本研究中，选择 FAM、Cy3 和 Cy5 作为荧光报告基团，因为它们是多色成像和组合编码中成熟的荧光团组合，在标准荧光显微镜条件下光谱重叠极小。该策略实现的病原体检测远超荧光通道数量的限制，有效克服了传统成像系统的通量瓶颈，同时为进一步扩展提供了高度的可扩展性。此外，一种具有多通道反应腔的定制封闭芯片改善了并行样本处理并简化了实验操作。实验结果表明，FinFISH 不仅在模拟痰液和尿液样本中的病原菌识别方面表现良好，而且证明适用于临床样本。此外，FinFISH 还为混合感染提供了额外的半定量见解。随着未来扩展探针设计和人工智能（AI）辅助分析的整合，FinFISH 有潜力推进临床病原菌诊断、微生物共定位研究以及肿瘤内细菌的空间分析。

## Abstract
Fluorescence in situ hybridization (FISH) is a highly specific technique for pathogenic bacteria detection that requires no culturing and provides simultaneous information on pathogenic bacteria abundance, morphology, and spatial localization. However, the limited sensitivity and poor multiplexing capacity of conventional FISH have hindered its broader application. Herein, we proposed a fingerprinting FISH (FinFISH) strategy driven by DNA self-assembly for multiplexed pathogenic bacteria detection. Using respiratory pathogens as representative models, FinFISH employs three distinct fluorophores in combinatorial labeling to generate identifiable fluorescent fingerprints for each species. In this work, FAM, Cy3, and Cy5 were selected as the fluorescent reporters because they represent well-established fluorophore combinations for multicolor imaging and combinatorial encoding, with minimal spectral overlap under standard fluorescence microscopy conditions. This strategy enables pathogen detection far beyond the limitations imposed by fluorescence channel numbers, effectively overcoming the throughput bottleneck of conventional imaging systems while offering high scalability for further expansion. Additionally, a custom-designed enclosed chip featuring multichannel reaction chambers improves parallel sample processing and simplifies experimental operation. Experimental results demonstrated that FinFISH not only performed well in identifying pathogenic bacteria within simulated sputum and urine samples but also proved applicable to clinical samples. Moreover, FinFISH provides additional semiquantitative insights into mixed infections. With future integration of expanded probe design and artificial intelligence (AI)-assisted analysis, FinFISH has the potential to advance clinical pathogenic bacteria diagnostics, microbial colocalization studies, and spatial analysis of intratumoral bacteria.