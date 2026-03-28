---
title: High-Resolution Colony Images of Clinically Isolated Bacteria for Automated Detection and Deep Learning.
title_zh: 用于自动检测和深度学习的临床分离细菌高分辨率菌落图像
authors: "Jia Du, Chun Yang, Miao Sun, Qi Sun, Miao Wang, Xufeng Ji, Kaifei Wang, Jiancheng Xu"
date: 2026-03-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/41896581/"
tags: ["query:pathoai"]
score: 9.0
evidence: 用于自动检测和深度学习的大规模菌落图像数据集
tldr: 针对微生物菌落人工分析效率低、主观偏差大以及现有AI数据集规模小且不规范的问题，本研究发布了一个包含19种临床常见细菌、151个菌株的大规模高分辨率标准化数据集。该数据集通过严格的受控环境采集，包含超过11.8万个标注菌落实例，捕捉了丰富的种内表型多样性。这一成果为开发高泛化性的自动化菌落检测与分类深度学习模型提供了坚实的数据基础，推动了临床微生物检测的标准化与智能化。
selection_source: fresh_fetch
motivation: 传统人工判读菌落效率低下且易受主观偏见影响，而现有AI数据集因规模小、多样性差且采集标准不一，难以满足临床自动化检测的需求。
method: 在受控光照和统一角度下，按照严格协议采集并标注了涵盖19种细菌、151个菌株的高分辨率图像，并进行了数据增强处理。
result: "构建了一个包含118,442个菌落实例的大规模开源数据集，每个物种均包含50张图像以充分展示种内表型差异。"
conclusion: 该标准化数据集为训练和评估临床细菌自动化检测模型提供了高质量基准，有助于实现微生物检测的高效化、标准化和可追溯化。
---

## 摘要
固体培养基上的菌落观察与分析是微生物研究的关键步骤。然而，传统的人工判读方法在处理大规模样本时效率低下，且易受主观偏见影响，难以满足高效、标准化和可追溯检测的需求。尽管人工智能和计算机视觉为自动化菌落分析提供了新机遇，但现有数据集通常规模较小、采集不一致且缺乏足够的菌株多样性，限制了模型的泛化能力。在此，我们公开了一个大型、规范化的菌落图像数据集，涵盖了来自不同来源的 19 种细菌和 151 个菌株，每种细菌包含 50 张图像以捕捉种内表型多样性。图像是在封闭背景、稳定光照和统一拍摄角度下，遵循严格协议采集的，随后经过系统标注和增强以提高可用性。该数据集总共包含 118,442 个菌落实例，为训练、评估和应用自动化检测的 AI 模型提供了坚实基础。

## Abstract
The observation and analysis of colonies on solid media are key steps in microbiological research. However, traditional manual interpretation methods are inefficient when handling large-scale samples and are prone to subjective bias, making it difficult to meet the demands for efficient, standardized, and traceable detection. Although AI and computer vision offer new opportunities for automated colony analysis, existing datasets are often small, inconsistently collected, and lack sufficient strain diversity, limiting model generalization. Here, we publicly release a large, normalized colony image dataset covering 19 bacterial species and 151 strains from diverse sources, with 50 images per species to capture within-species phenotypic diversity. Images were collected on a closed background under stable lighting and uniform shooting angles following strict protocols, then systematically annotated and augmented to improve usability. In total, the dataset contains 118,442 colony instances, providing a robust foundation for training, evaluating, and applying AI models for automated detection.