---
title: A Surface-Enhanced Raman Scattering-Digital Microfluidics Biosensing Platform Integrated with a 1D-Convolutional Neural Network for Noninvasive Detection of Inflammation Markers.
title_zh: 一种集成一维卷积神经网络的表面增强拉曼散射-数字微流控生物传感平台，用于炎症标志物的无创检测
authors: "Siyue Xiong, Peitao Dong, Chengxuan Wang, Xun Li, Dingbang Xiao, Xuezhong Wu"
date: 2026-03-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/41733640/"
tags: ["query:pathoai"]
score: 7.0
evidence: 用于炎症标志物检测的一维卷积神经网络
tldr: 针对早期败血症诊断中汗液炎症标志物检测难的问题，该研究开发了一种集成表面增强拉曼散射（SERS）与数字微流控（DMF）的自动化传感平台。通过构建磁性夹心免疫复合物并结合1D卷积神经网络（1D-CNN）进行光谱数据处理，实现了对C反应蛋白（CRP）的高灵敏度定量分析。该系统在20分钟内完成检测，检出限达0.77 pg/mL，为非侵入式、自动化的临床早期筛查提供了高效的技术方案。
selection_source: fresh_fetch
motivation: 旨在解决早期败血症诊断中，汗液等非侵入性样本内炎症标志物浓度极低且难以快速、自动化检测的挑战。
method: 结合了数字微流控的液滴精准操控能力与SERS的高灵敏度，并利用1D卷积神经网络对拉曼光谱进行特征提取与定量回归分析。
result: 平台实现了0.77 pg/mL的超低检出限，且1D-CNN模型在CRP定量任务中达到了0.994的决定系数，显著优于传统分析方法。
conclusion: 该研究证明了SERS-DMF技术与深度学习结合在非侵入式医疗诊断中的潜力，为开发全自动、高精度的便携式生物传感设备奠定了基础。
---

## 摘要
脓毒症早期诊断中多种炎症标志物（IMs）的无创检测具有挑战性。为此，本文创新性地开发了一种基于表面增强拉曼散射（SERS）和数字微流控（DMF）的集成传感平台。该平台可对汗液中的炎症标志物C反应蛋白（CRP）进行高灵敏度和自动化的分析。它采用功能化的Au@Fe3O4作为磁性捕获核心，并利用拉曼报告分子修饰的SERS标签形成“AuMNPs/IMs/SERS标签”夹心免疫复合物。结合DMF芯片在液滴操控方面的固有精度，这两种技术的协同作用实现了汗液样本中痕量分析物的自动化、高效富集和原位检测。研究发现，SERS-DMF平台可在20分钟内高效检测CRP，检出限达0.77 pg/mL，远低于临床阈值。该平台与金标准ELISA的一致性证明了其高可靠性。此外，一维卷积神经网络模型的建立显著提升了CRP定量分析的准确性和鲁棒性。在测试集中，CRP的决定系数为0.994，均方根误差为0.135。基于线性假设，该技术显著优于传统分析方法。本研究整合了SERS-DMF技术在早期脓毒症无创、快速筛查中的应用，凭借超低样本消耗和全过程自动化等优势，为开发炎症标志物诊断设备奠定了创新的技术基础。

## Abstract
The noninvasive detection of multiple inflammatory markers (IMs) for early sepsis diagnosis is challenging. Therefore, herein, we innovatively developed an integrated sensing platform based on surface-enhanced Raman scattering (SERS) and digital microfluidics (DMF). The platform allows highly sensitive and automated analysis of the inflammatory marker C-reactive protein (CRP) in sweat. It uses functionalized Au@Fe3O4 as a magnetic capture core and Raman-reported molecule-modified SERS tags to form a "AuMNPs/IMs/SERS tag" sandwich immunocomplex. Combined with the inherent precision of the DMF chip in droplet manipulation, the synergy between these two technologies achieves automated, high-efficiency enrichment and in situ detection of trace analytes in sweat samples. We observed that the SERS-DMF platform can efficiently detect CRP within 20 min, achieving a detection limit of 0.77 pg/mL. These values are substantially below clinical thresholds. Consistent with the gold-standard ELISA, our platform demonstrates high reliability. Moreover, the establishment of a one-dimensional convolutional neural network model considerably improved the accuracy and robustness for quantitatively analyzing the CRP. In the test set, the coefficient of determination for the CRP was 0.994, with a root mean square error of 0.135. Based on linear assumptions, our technology significantly outperforms traditional analytical methods. This study integrates the application of SERS-DMF technology for the noninvasive, rapid screening of early-stage sepsis. Using advantages such as ultralow sample consumption and complete process automation provides an innovative technical foundation for developing diagnostic devices for IMs.