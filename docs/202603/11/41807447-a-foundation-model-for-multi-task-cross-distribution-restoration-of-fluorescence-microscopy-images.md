---
title: A foundation model for multi-task cross-distribution restoration of fluorescence microscopy images.
title_zh: 一种用于荧光显微图像多任务跨分布修复的基础模型
authors: "Lu Q, Liu X, Feng Q, Zeng S, Cheng S., Qiqi Lu, Xiuli Liu, Qianjin Feng, Shaoqun Zeng, Shenghua Cheng"
date: 2026-03-10
pdf: "https://pubmed.ncbi.nlm.nih.gov/41807447/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 用于荧光显微镜图像修复的基础模型
tldr: 针对荧光显微成像中现有模型任务单一、泛化性差的问题，本文开发了 FluoResFM 基础模型。该模型通过引入文本先验信息，在统一框架下实现了去噪、解卷积和超分辨率等多任务处理。在涵盖20多种生物结构的异质数据集上训练后，FluoResFM 展现出卓越的跨分布泛化能力，仅需单样本微调即可适配新任务，显著提升了下游细胞分割的准确性。
selection_source: fresh_fetch
motivation: 传统的荧光显微图像修复模型通常只能处理特定任务，且难以应对不同生物结构或成像条件带来的数据分布变化。
method: 构建了一个名为 FluoResFM 的基础模型，利用文本先验引导模型在统一架构中学习去噪、解卷积和超分辨率等多种修复任务。
result: 该模型在多项任务上表现优于传统模型，且仅需极少量样本微调即可迁移至3D修复、各向同性重建等新场景。
conclusion: FluoResFM 证明了在大规模多任务数据集上预训练的基础模型能有效解决显微成像中的泛化难题，并能显著赋能下游生物图像分析任务。
---

## 摘要
深度学习在修复受噪声、模糊或欠采样退化的荧光显微图像方面展现了卓越的能力。然而，大多数现有模型是针对特定任务的，且在有限的、同质分布的数据上进行训练，这限制了它们的泛化能力和实用性。在此，我们提出了 FluoResFM，这是一个在统一模型中实现多任务和跨分布荧光显微图像修复的基础模型。FluoResFM 利用文本先验信息来适应特定的任务和数据分布。通过在涵盖三项任务（图像去噪、反卷积和超分辨率）以及 20 多种生物结构的数据集上进行训练，FluoResFM 在具有不同生物结构和成像条件的跨数据集上展示了卓越的修复性能和增强的泛化能力。通过仅使用单个样本进行微调，FluoResFM 可以进一步提高其在未见数据上的性能，达到与在数百个样本上训练的传统模型相当的结果，并能轻松适应其他任务，包括 3D 图像修复、表面投影、各向同性重建以及具有各种缩放因子的超分辨率。此外，利用 FluoResFM 修复的高质量图像，可以增强现有细胞/细胞器分割模型的性能。

## Abstract
Deep learning has demonstrated remarkable abilities in restoring fluorescence microscopy images degraded by noise, blur, or undersampling. However, most existing models are task-specific and trained on limited, homogeneously distributed data, which restricts their generalizability and practicality. Here, we present FluoResFM, a foundation model for multi-task and cross-distribution fluorescence microscopy image restoration in a unified model. FluoResFM leverages textual prior information to adapt to specific tasks and data distributions. Trained on datasets across three tasks (image denoising, deconvolution, and super-resolution) and over 20 biological structures, FluoResFM demonstrates superior restoration performance and enhanced generalization across datasets with varied biological structures and imaging conditions. Through fine-tuning with only a single sample, FluoResFM can further improve its performance on unseen data, achieving results comparable to conventional models trained on hundreds of samples, and be easily adapted to additional tasks, including 3D image restoration, surface projection, isotropic reconstruction, and super-resolution with various scale factors. Moreover, the performance of existing cell/organelle segmentation models can be enhanced using the high-quality images restored by FluoResFM.