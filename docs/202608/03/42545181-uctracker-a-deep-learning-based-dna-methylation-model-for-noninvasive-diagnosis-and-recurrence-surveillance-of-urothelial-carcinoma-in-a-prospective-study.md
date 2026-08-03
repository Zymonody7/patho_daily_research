---
title: "UCtracker: A Deep Learning-Based DNA Methylation Model for Noninvasive Diagnosis and Recurrence Surveillance of Urothelial Carcinoma in a Prospective Study."
title_zh: UCtracker：一项前瞻性研究中基于深度学习的 DNA 甲基化模型，用于尿路上皮癌的无创诊断和复发监测。
authors: "Shengwei Xiong, Gaojie Li, Yucai Wu, Yuan Liang, Heng Guo, Yu Zhang, Gengyan Xiong, Long Tian, Xin Zhang, Ye Tian, Zhengguo Ji, Bin Guo, Yue Shi, Jian Fan, Zhihua Li, Yanqing Gong, Shiming He, Xuesong Li, Weimin Ci, Liqun Zhou"
date: 2026-08-03
pdf: "https://pubmed.ncbi.nlm.nih.gov/42545181/"
tags: ["query:seqai"]
score: 7.0
evidence: 用于DNA甲基化和癌症监测的深度学习模型
tldr: "针对尿路上皮癌（UC）无创诊断和术后监测的难题，研究者开发了基于尿液DNA甲基化的深度学习模型UCtracker。该模型利用CNN-BiLSTM架构处理2000个关键的低甲基化差异区域，在多中心验证中实现了超过90%的灵敏度和特异性，且在极低测序深度下表现稳定。在术后随访中，它能提前多达250天预警复发，为UC的精准管理提供了高性价比的无创工具。"
selection_source: fresh_fetch
motivation: 现有的尿路上皮癌诊断和术后监测手段缺乏足够的灵敏度且具有侵入性，急需一种高准确率的无创检测方案。
method: 提取尿液DNA中2000个关键的低甲基化差异区域，并结合CNN-BiLSTM深度学习架构构建分类模型。
result: "模型在独立验证集上达到90.6%的灵敏度，优于传统FISH检测，并能提前约8个月发现术后复发迹象。"
conclusion: UCtracker证明了深度学习结合表观遗传学特征在癌症无创筛查和长期监测中的巨大潜力，具有极高的临床应用价值。
---

## 摘要
尿路上皮癌 (UC) 的无创诊断和纵向监测在临床上仍具有挑战性。本研究开发并前瞻性验证了 UCtracker，这是一种基于尿液 DNA 甲基化的深度学习模型，用于 UC 检测和术后复发监测。通过对 UC 组织、配对的癌旁正常组织和非肿瘤尿液样本进行高深度全基因组亚硫酸氢盐测序，鉴定了 UC 特异性差异甲基化区域 (DMRs)。UCtracker 采用前 2000 个低甲基化 DMRs，并结合卷积神经网络-双向长短期记忆 (CNN-BiLSTM) 架构构建而成。在内部验证队列 (n = 165) 中，UCtracker 的灵敏度达到 94.6%，特异性达到 94.4%；在独立多中心队列 (n = 55) 中亦保持高性能，灵敏度为 90.6%，特异性为 91.3%。对于 T1 期肿瘤、高级别肿瘤和膀胱 UC，UCtracker 的灵敏度高于 UroVysion 荧光原位杂交技术。子抽样分析表明，即使在极低测序深度下，该模型也表现出稳定的诊断性能。在术后监测中，对 48 名 UC 患者的 131 份样本进行纵向尿液分析，检测到了 94.1% 的复发事件，并比临床确诊提前多达 250 天识别出复发。这些研究结果表明，UCtracker 是一种高准确度且具有成本效益的尿液检测工具，可用于 UC 诊断、术后监测和个体化患者管理。

## Abstract
Noninvasive diagnosis and longitudinal surveillance of urothelial carcinoma (UC) remain clinically challenging. Here, we developed and prospectively validate UCtracker, a urine DNA methylation-based deep learning model for UC detection and postoperative recurrence monitoring. UC-specific differentially methylated regions (DMRs) were identified by high-depth whole-genome bisulfite sequencing of UC tissues, paired adjacent normal tissues, and non-tumor urine samples. UCtracker was constructed using the top 2000 hypomethylated DMRs and a convolutional neural network-bidirectional long short-term memory architecture. In an internal validation cohort (n = 165), UCtracker achieved a sensitivity of 94.6% and a specificity of 94.4%, and maintained high performance in an independent multicenter cohort (n = 55), with a sensitivity of 90.6% and a specificity of 91.3%. UCtracker showed higher sensitivity than UroVysion fluorescence in situ hybridization for T1 tumors, high-grade tumors, and bladder UC. Subsampling analyses demonstrated stable diagnostic performance even at ultralow sequencing depths. In postoperative surveillance, longitudinal urine profiling of 131 samples from 48 UC patients detected 94.1% of recurrence events and identified recurrence up to 250 days before clinical confirmation. These findings support UCtracker as a highly accurate and cost-effective urine-based tool for UC diagnosis, postoperative surveillance, and personalized patient management.