---
title: "Integrating scanning electron microscopy, explainable deep learning, and ITS sequencing for accurate identification in some species Geastrum."
authors: "Eda Kumru, Şehmus Altaş, Gülce Ediş, Fatih Ekinci, Koray Acici, Mehmet Serdar Güzel, Emre Keskin, Mustafa Sevindik, Ilgaz Akata"
date: 2026-05-13
pdf: "https://pubmed.ncbi.nlm.nih.gov/42129448/"
tags: ["query:pathoai"]
score: 7.0
evidence: 用于物种分类的深度学习和可解释人工智能
tldr: 将扫描电镜图像与深度学习和可解释AI结合，用于地星属物种的细粒度分类。
selection_source: fresh_fetch
motivation: 用于物种分类的深度学习和可解释人工智能。
method: 方法与实现细节请参考摘要与正文。
result: 结果与对比结论请参考摘要与正文。
conclusion: 总体而言，该工作在所述任务上展示了有效性，并提供了可复用的思路或工具。
---

## Abstract
The differentiation of species within the genus Geastrum remains a challenging task due to the strong morphological similarity among taxa and the limited discriminatory power of macroscopic characteristics alone. Although molecular approaches based on DNA extraction, PCR amplification, and ITS sequencing provide reliable taxonomic resolution, they are labor-intensive, destructive, and unsuitable for rapid or large-scale analyses. In this study, a comprehensive framework integrating scanning electron microscopy (SEM) based basidiospore imaging with modern deep learning and explainable artificial intelligence (XAI) techniques is proposed for fine-grained classification of Geastrum species. A curated dataset comprising 800 high-resolution SEM images from (Geastrum elegans, G. fimbriatum, G. quadrifidum, G. rufescens, and G. triplex) was evaluated using multiple convolutional and transformer-based architectures, including DenseNet121, EfficientNetB0, ConvNeXt-Tiny, and Swin-Tiny, as well as several ensemble configurations. Among all models, DenseNet121 achieved the highest single-model performance, reaching approximately 99.00% accuracy, precision, recall, F1-score, and specificity, with an MCC of 0.98 and an AUC approaching 1.00. Ensemble models, particularly DenseNet121-EfficientNetB0 and DenseNet121-ConvNeXt-Swin, consistently matched or slightly improved these results, demonstrating enhanced robustness and class separability. Explainable AI analyses based on LIME confirmed that model predictions are driven by biologically meaningful ultrastructural features, such as spore ornamentation patterns and surface textures, rather than spurious artifacts. Molecular phylogenetic analyses based on nrITS sequences independently supported the species boundaries inferred by the deep learning models. Overall, the results demonstrate that SEM-driven, explainable deep learning constitutes a powerful and objective complement to classical morphological and molecular approaches, offering a scalable pathway for accurate and reproducible species identification in taxonomically complex fungal groups.