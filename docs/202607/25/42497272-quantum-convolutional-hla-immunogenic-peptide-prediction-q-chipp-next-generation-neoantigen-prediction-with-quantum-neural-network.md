---
title: "Quantum convolutional HLA immunogenic peptide prediction (Q-CHIPP): Next-generation neoantigen prediction with quantum neural network."
title_zh: 量子卷积 HLA 免疫原性肽预测 (Q-CHIPP)：基于量子神经网络的下一代新抗原预测
authors: "Ryan Peters, Kahn Rhrissorrakrai, Prerana Bangalore Parthasarathy, Vadim Ratner, Tanvi P Gujarati, Meltem Tolunay, Jie Shi, Jeffrey K Weber, Timothy A Chan, Laxmi Parida, Sara Capponi, Filippo Utro, Tyler J Alban"
date: 2026-07-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/42497272/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 用于免疫原性肽预测的量子神经网络
tldr: "01限制性肽段的免疫原性预测。结果显示，在样本量较少的情况下，该方法比经典模型准确率提升了6%，证明了量子机器学习在数据受限的生物医学系统中的应用潜力。"
selection_source: fresh_fetch
motivation: 针对癌症新抗原预测中经典模型难以处理小规模、高噪声生物数据且泛化性差的挑战，探索量子计算的优势。
method: 提出Q-CHIPP框架，采用量子卷积神经网络（QCNN）并集成Pauli旋转、动力学解耦等噪声抑制技术，在真实量子硬件上进行混合训练。
result: "在46量子比特硬件实验中，该模型在训练样本更少的情况下，比经典方法在MHC结合与免疫原性分类准确率上提升了6%。"
conclusion: 该研究展示了大规模量子卷积神经网络在生物医学建模中的可行性，为数据受限的生物系统提供了可扩展的量子增强研究基础。
---

## 摘要
量子计算的快速增长受到以空前速度执行复杂计算的承诺所驱动；然而，目前的用例受到量子硬件的限制，以及难以识别经典计算机无法轻易处理的问题。在这些限制下，包括药物发现、蛋白质折叠和精准医疗在内的生物学问题为理解当前量子硬件如何取得进展提供了机会。在免疫学中，癌症新抗原的准确预测仍然是一个主要挑战，受到小规模、高噪声数据集以及经典模型泛化能力不足的限制。在处理该问题时，我们探索了多种噪声抑制技术，包括泡利旋转（Pauli twirling）和动力学解耦（dynamical decoupling），并结合受控的基于 shot 的采样，以在真实硬件和热启动混合方法中稳定训练。通过这些方法，我们展示了量子卷积神经网络（QCNNs）在 MHC 结合和免疫原性预测中的应用，包括一项涉及 46 个量子比特的量子硬件实验，与经典方法相比，该实验在训练样本较少的情况下实现了分类准确率 6% 的提升。在这些模型的基础上，我们推出了量子卷积 HLA 免疫原性肽预测（Q-CHIPP），这是一个整合了 MHC 结合和 T 细胞识别的组合框架。它针对 HLA-A*02:01 限制性的 9 聚体肽，能够更准确地识别已知具有免疫原性的肽，从而改善了预测新抗原负荷的预后影响。总之，这些工作代表了 QCNNs 在生物医学建模中的大规模应用，突显了量子机器学习在数据受限的生物系统中的可行性和前景，并为量子增强的生物医学研究奠定了可扩展的基础。

## Abstract
The rapid growth of quantum computing is driven by promises of performing complex calculations with unprecedented speed; however, current use cases have been limited by quantum hardware and the difficulty of identifying problems that classical computers cannot easily address. Within these constraints, biological problems including drug discovery, protein folding, and precision medicine present an opportunity to understand how current quantum hardware can make advances. In immunology, accurate prediction of cancer neoantigens remains a major challenge, limited by small, noisy datasets and the inability of classical models to generalize. In approaching the problem, we explore multiple noise mitigation techniques, including Pauli twirling and dynamical decoupling, in conjunction with controlled shot-based sampling to stabilize training on real hardware and in a warm start hybrid approach. With these approaches, we demonstrate the use of Quantum Convolutional Neural Networks (QCNNs) for both MHC binding and immunogenicity prediction, including a quantum hardware experiment involving 46 qubits that achieved a 6% increase in classification accuracy with fewer training samples compared to classical approaches. Building on these models, we introduce Quantum Convolutional HLA Immunogenic Peptide Prediction (Q-CHIPP), a combinatorial framework integrating MHC binding and T-cell recognition. It targets HLA-A*02:01-restricted 9-mer peptides and, more accurately, identifies those peptides known to be immunogenic, improving the prognostic impact of predicted neoantigen load. Together, these represent a large-scale application of QCNNs in biomedical modeling, highlighting both the feasibility and promise of quantum machine learning for data-limited biological systems and establishing a scalable foundation for quantum-enhanced biomedical research.