---
title: "EMCFsys: A scalable ecosystem for high-throughput nanoscale ultrastructure analysis across biological kingdoms"
title_zh: EMCFsys：一个用于跨生物界高通量纳米级超微结构分析的可扩展生态系统
authors: "Feng X, Yu Z, Guo J, Mengze D, Liu F, Xu S, Zhang G, Xie L, Han B, Chen Z, Deng G, Rui C, He Y."
date: 2026-03-19
pdf: "https://doi.org/10.21203/rs.3.rs-8942783/v1"
tags: ["query:bioinfo"]
score: 9.0
evidence: 跨界细胞生物学和细胞器分类的基础模型
tldr: 针对体积电子显微镜（vEM）成像慢、标注难的瓶颈，本文推出了EMCFsys生态系统。该系统包含涵盖14种模态的400万张电镜图像数据集，以及用于16倍加速成像的修复模型EMCellFiner和支持少样本分割的基座模型EMCellFound。通过集成Napari插件，研究者能以极低标注成本实现跨物种、跨细胞的高通量3D超微结构重建，显著降低了大规模生物成像的研究门槛。
selection_source: fresh_fetch
motivation: 解决体积电子显微镜在进行大规模生物组织成像时面临的采集周期长、人工标注工作量巨大以及跨物种通用性差的问题。
method: 构建了一个包含400万张图像的多模态数据集，并开发了用于图像超分辨率修复的EMCellFiner模型和支持零样本/少样本学习的细胞基座模型EMCellFound。
result: "实现了16倍的成像速度提升，并能在仅使用0.01%标注数据的情况下，完成内质网等复杂细胞器的精确3D重建。"
conclusion: EMCFsys通过整合高性能模型与无代码插件，为跨物种、高通量的纳米级细胞超微结构分析提供了一个高效且通用的标准化平台。
---

## 摘要
体电子显微镜 (vEM) 提供了细胞超微结构的纳米级三维可视化，但大体积成像和分析仍受限于漫长的采集时间和繁重的标注处理。在此，我们提出了电子显微镜细胞基础生态系统 (EMCFsys)，该系统包含：一个由 4,002,802 张高质量电子显微照片组成的精选数据集，涵盖 14 种模态和主要生物界；一个基础图像修复模型 (EMCellFiner)，通过对低分辨率或低驻留时间扫描进行高保真超分辨率处理，使采集速度提高 16 倍；以及一个基础模型 (EMCellFound)，支持零样本到少样本的细胞器分类、二维分割和精确的三维重建。这促进了高精度的三维超微结构重建，即使是像内质网这样的多片段细胞器，也只需使用低至 0.01% 的标注数据。该生态系统集成在一个零代码的 Napari 插件中，无需编程专业知识即可实现自动化的、高通量的纳米级分析。通过大幅减少成像时间、标注负担和计算障碍，EMCF 为跨细胞类型和物种的大规模 vEM 研究建立了一个高效、通用的平台。

## Abstract
<title>Abstract</title>  <p>Volume electron microscopy (vEM) provides nanoscale 3D visualization of cellular ultrastructure, but large-volume imaging and analysis remain limited by long acquisition times and annotation-intensive processing. Here we present the Electron Microscopy Cell Foundation ecosystem (EMCFsys), comprising a curated dataset of 4,002,802 high-quality electron micrographs spanning 14 modalities and major biological kingdoms, a foundation image restoration model (EMCellFiner) that enables 16-fold faster acquisition through high-fidelity super-resolution from low-resolution or low-dwell-time scans, and a foundation model (EMCellFound) that supports zero- to few-shot organelle classification, 2D segmentation, and precise 3D reconstruction. This facilitates high-precision 3D ultrastructure reconstruction, even for multi-piece organelles like the endoplasmic reticulum by using as little as 0.01% labeled data. Integrated into a zero-code Napari plugin, the ecosystem enables automated, high-throughput nanoscale analysis without programming expertise. By substantially reducing imaging time, annotation burden, and computational barriers, EMCF establishes an efficient, generalizable platform for large-scale vEM studies across cell types and species.</p>