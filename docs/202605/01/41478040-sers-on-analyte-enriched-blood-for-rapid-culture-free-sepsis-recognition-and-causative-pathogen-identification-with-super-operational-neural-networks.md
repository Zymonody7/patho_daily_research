---
title: "SERS on analyte-enriched blood for rapid, culture-free sepsis recognition and causative pathogen identification with super operational neural networks."
title_zh: 基于富集待测物血液的 SERS 技术，利用超运算神经网络实现快速、免培养的脓毒症识别及致病病原体鉴定
authors: "Manal Hassan, Md Sakib Bin Islam, Sakib Mahmud, Mahmoud Elgamal, Md Shaheenur Islam Sumon, Ali Ait Hssain, Emad Ibrahim, Amit Kumar, Yiping Zhao, Saad Bin Abul Kashem, Mehmet Burcin Unlu, Gozde Durmus, Muhammad E H Chowdhury, Susu M Zughaier"
date: 2026-05-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/41478040/"
tags: ["query:pathoai"]
score: 9.0
evidence: 用于血液中致病病原体识别的深度学习
tldr: "针对败血症诊断依赖培养、耗时长且灵敏度低的问题，本研究提出一种结合表面增强拉曼光谱（SERS）与超运算神经网络（SuperRamanNet）的深度学习工作流。该方法直接从富集分析物的血液中提取光谱特征，在包含653例样本的数据集上实现了99.67%的败血症识别准确率和98.84%的病原体分类准确率。这种无需培养、便携且高精度的方案为临床快速分诊和早期精准用药提供了重要技术支撑。"
selection_source: fresh_fetch
motivation: 传统的败血症诊断高度依赖耗时的细菌培养，难以满足临床对早期干预和快速识别病原体的迫切需求。
method: 采用表面增强拉曼光谱技术获取血液样本特征，并利用轻量化的超运算神经网络（SuperRamanNet）进行一维光谱信号的分类与识别。
result: "系统在内部交叉验证中达到了近乎完美的准确率，并在独立外部验证集上保持了98.28%的病原体分型精度，展现出极强的泛化能力。"
conclusion: 该研究证明了SERS结合先进深度学习模型在无需培养的情况下实现临床级败血症诊断的可行性，具有显著的即时检测应用潜力。
---

## 摘要
脓毒症仍是导致发病率和死亡率上升的主要原因，然而常规诊断方法速度慢、依赖培养，且往往缺乏早期干预所需的灵敏度或特异性。先前的研究很少在血培养样本或独立外部队列中展示出临床级的性能。我们通过表面增强拉曼光谱与深度学习工作流（SERS-DL）填补了这些空白，该工作流直接从富集了目标待测物的血液中进行脓毒症病例识别和致病病原体鉴定。我们构建了一个主要数据集，包含从卡塔尔一家三级医院收集的 653 份富集待测物血液样本中获取的 SERS 光谱，以及一个由 70 份独立样本组成的外部盲测队列。在对 SERS 光谱进行严格预处理和类别加权增强后，我们训练了 SuperRamanNet，这是一种基于超运算神经网络（super operational neural networks）的轻量级一维分类器。在五折样本包含交叉验证中，该系统在二分类脓毒症识别中达到了 99.67% 的准确率，在六类病原体鉴定中达到了 98.84% 的准确率。在外部队列中，病原体分型的准确率保持在 98.28% 的高水平，表明其具有强大的泛化能力。对比基准测试和消融研究证实了其相对于卷积和运算基准模型的持续提升，并量化了数据增强和架构选择的影响。残留的混淆主要集中在对照组与大肠杆菌（Escherichia coli）之间，以及某些革兰氏阴性类别之间，这强调了在血液样本采集过程中改进原始类别平衡的必要性。总体而言，这种快速、免培养且便携的 SERS-DL 流水线能够直接从血液中提供接近临床级的脓毒症检测和病原体鉴定准确率。其紧凑的模型和简化的工作流支持即时检测（POCT）转化，具有加速分诊、指导早期治疗并减轻全球脓毒症负担的潜力。

## Abstract
Sepsis remains a leading cause of morbidity and mortality, yet routine diagnostics are slow, culture-dependent, and often lack the sensitivity or specificity required for early intervention. Prior studies rarely demonstrate clinical-grade performance on blood culture samples or in independent external cohorts. We address these gaps with a surface-enhanced Raman spectroscopy and deep learning workflow (SERS-DL) that performs sepsis instance recognition and causative pathogen identification directly from target-analyte enriched blood. We assembled a primary dataset of SERS spectra acquired from 653 analyte-enriched blood samples collected at a tertiary hospital in Qatar and an external blind cohort of 70 independent samples. After rigorous preprocessing and class-weighted augmentation of SERS spectra, we trained SuperRamanNet, a lightweight one-dimensional classifier based on super operational neural networks. In five-fold, sample-contained cross-validation, the system achieved 99.67 % accuracy for binary sepsis recognition and 98.84 % accuracy for six-class pathogen identification. On the external cohort, performance remained high at 98.28 % for pathogen typing, indicating robust generalizability. Comparative benchmarks and ablation studies confirmed consistent gains over convolutional and operational baselines and quantified the impact of augmentation and architectural choices. Residual confusions were concentrated between control and Escherichia coli and among certain Gram-negative classes, underscoring the need for improved raw class balance during blood sample collection. Overall, this rapid, culture-free, and portable SERS-DL pipeline delivers near clinical-grade accuracy for sepsis detection and pathogen identification directly from blood. The compact model and streamlined workflow support point-of-care translation, with potential to accelerate triage, guide early therapy, and reduce the global sepsis burden.

---

## 论文详细总结（自动生成）

这篇论文介绍了一种结合**表面增强拉曼光谱（SERS）**与**超运算神经网络（SuperRamanNet）**的新技术，旨在解决脓毒症（败血症）诊断中“等不起”和“查不准”的核心痛点。

### 1. 解决的问题与研究价值
*   **核心问题**：脓毒症是由于感染引起的全身炎症反应，致死率极高。目前的金标准是“血培养”，即把血液里的细菌养大再鉴定，这通常需要 24-72 小时。在等待期间，医生只能凭经验用药，容易导致治疗延误或抗生素滥用。
*   **研究价值**：该研究实现了**免培养（Culture-free）**的快速诊断。通过激光照射血液样本获取化学指纹，并用 AI 自动识别，将诊断时间从“天”缩短到“分钟”级别，且准确率达到了临床级水平。

### 2. 白话版概述
想象一下，细菌在血液里会留下独特的“气味”或“指纹”。传统的办法是把细菌抓出来养一堆，看它们长成什么样（血培养）；而这篇论文的方法是直接用一种特殊的激光放大器（SERS）去捕捉这些微弱的指纹信号，然后交给一个非常聪明的“超级大脑”（SuperRamanNet）去辨认。这个大脑不仅能看出你有没有得败血症，还能直接告诉你具体是哪种细菌在作怪，整个过程不需要等待细菌生长。

### 3. 方法部分
*   **核心思想**：利用 SERS 技术极大地增强血液中生物分子的拉曼散射信号，获取反映病原体代谢和细胞壁特征的一维光谱数据，再通过非线性建模能力极强的神经网络进行分类。
*   **模型结构（SuperRamanNet）**：
    *   **超运算神经网络（SuperONNs）**：不同于传统 CNN 使用固定的线性卷积（$y = wx + b$），SuperONNs 的每个神经元可以从一组非线性算子库（如泰勒多项式、正弦函数等）中自动学习并组合出最适合的映射函数。
    *   **轻量化设计**：采用一维（1D）架构，参数量远少于传统深度模型，适合集成到便携式设备中。
*   **关键设计取舍**：
    *   **富集处理**：在检测前对血液中的待测物进行富集，以提高信噪比。
    *   **类别加权增强**：针对不同细菌样本量不平衡的问题，在训练时对少数类进行了数据增强和权重补偿。

### 4. 实验部分
*   **数据**：来自卡塔尔一家医院的 653 份临床血液样本（主数据集）+ 70 份独立外部盲测样本。
*   **任务**：
    1.  **二分类**：识别是否患有脓毒症（对照组 vs 感染组）。
    2.  **六分类**：鉴定具体病原体（包括大肠杆菌、金黄色葡萄球菌、肺炎克雷伯菌等常见致病菌）。
*   **Baseline**：传统的卷积神经网络（CNN）和标准运算神经网络（ONN）。
*   **主要结果**：
    *   **内部验证**：脓毒症识别准确率 99.67%，病原体鉴定准确率 98.84%。
    *   **外部验证**：在完全未见过的外部数据集上，病原体分型准确率仍保持在 **98.28%**，证明了极强的泛化能力。

### 5. 资源与算力
*   **文中未充分披露**具体的硬件配置（如 GPU 型号）和训练时长。但考虑到模型是轻量化的一维网络且样本量在数百量级，通常单张消费级显卡或高性能 CPU 即可在短时间内完成训练。

### 6. 真正可信的贡献
*   **外部验证的稳健性**：很多 AI+医疗的研究在自家数据集上表现完美，一换环境就崩。该研究通过了 70 例独立外部队列的盲测，这是其结论最具说服力的地方。
*   **非线性算子的优势**：证明了在处理复杂的生物光谱信号时，SuperONN 这种能够自适应调整激活函数的架构比传统 CNN 捕捉特征更精准。

### 7. 局限与风险
*   **样本多样性不足**：虽然有外部验证，但样本主要来自单一地区的医院，不同人种、不同地区的菌株变异是否会影响光谱特征仍需验证。
*   **混合感染难题**：实验主要针对单一病原体感染。临床上偶尔会出现多种细菌混合感染，模型在这种情况下的表现尚未探讨。
*   **前处理依赖**：虽然免去了培养，但“富集待测物”的过程仍需要一定的实验室操作，尚未达到完全的“滴血即检”。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事医疗诊断 AI、生物光谱分析、以及对非线性神经网络架构（ONN/SuperONN）感兴趣的研究者。
*   **后续可跟进的问题**：能否利用该模型进一步预测细菌的**耐药性（AST）**？如果能直接从光谱中读出细菌怕哪种药，那将是该领域的终极突破。

（完）
