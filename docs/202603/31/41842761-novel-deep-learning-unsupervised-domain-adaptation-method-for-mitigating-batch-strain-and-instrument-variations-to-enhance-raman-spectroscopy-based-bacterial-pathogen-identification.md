---
title: "Novel Deep-Learning Unsupervised Domain Adaptation Method for Mitigating Batch, Strain, and Instrument Variations to Enhance Raman Spectroscopy-Based Bacterial Pathogen Identification."
title_zh: 一种用于减轻批次、菌株和仪器差异以增强基于拉曼光谱的细菌病原体鉴定的新型深度学习无监督领域自适应方法
authors: "Zhe Zhang, Yiwen Xu, Siyu Meng, Zhouhao Lei, Huan Zeng, Qiang Zhao, Liliang Wang, Huijie Hu, Jiyong Yang, Yizhi Song"
date: 2026-03-31
pdf: "https://pubmed.ncbi.nlm.nih.gov/41842761/"
tags: ["query:pathoai"]
score: 9.0
evidence: 用于细菌病原体识别的深度学习
tldr: "拉曼光谱结合深度学习可快速识别病原体，但受仪器、批次和菌株差异导致的域偏移影响，模型泛化性较差。本研究提出RSCDM模型，通过两个分类器的输出差异动态识别偏离源域的目标样本，并利用对抗学习进行特征对齐。实验显示，该方法将跨仪器和菌株的识别准确率从约80%提升至95%以上，微调后可达99.3%，将鉴定时间从数天缩短至分钟级，显著增强了临床诊断的鲁棒性。"
selection_source: fresh_fetch
motivation: 针对拉曼光谱在实际应用中因仪器差异、实验批次和菌株多样性导致的模型识别准确率下降问题。
method: 提出一种名为RSCDM的无监督域适应框架，利用双分类器的预测差异来度量样本分布差距，并通过对抗训练实现跨域特征对齐。
result: "在多种细菌识别任务中，该方法将准确率从81.6%提升至95.4%，并在跨仪器临床样本测试中通过微调达到了99.3%的极高精度。"
conclusion: 该研究通过解决光谱数据的域偏移挑战，实现了分钟级的快速病原体鉴定，为单细胞拉曼光谱技术的临床转化提供了技术支撑。
---

## 摘要
抗生素耐药性威胁的日益加剧，要求进行快速且准确的病原体鉴定。虽然拉曼光谱结合深度学习支持快速检测，但由于仪器异质性、批次变异性和菌株多样性引起的领域偏移，模型的鲁棒性仍然受到影响。为解决这一问题，我们提出了拉曼光谱分类差异模型（RSCDM），这是一种新型领域自适应框架，通过特定任务分类器之间的输出差异，动态识别远离源域特征分布的目标样本。该模型通过对抗性地对齐不同领域的特征来弥合光谱变异性。与依赖固定领域假设的传统方法不同，RSCDM 利用分类器输出差异来自适应地检测分布外样本，从而实现任务驱动的领域对齐。实验结果表明，使用商用光谱仪时，RSCDM 将跨批次和菌株的七种细菌的分类准确率从 81.6% 提高到 95.4%；对于使用自制光谱仪获取的六种临床分离株（未包含在训练中），准确率从 77.5% 提高到 91.3%。在商用和自制光谱仪获取的标准菌株光谱上对预训练模型进行微调，进一步将临床分离株的鉴定准确率提升至 99.3%，验证了其对仪器多样性的鲁棒性。总之，这些发现解决了光谱领域自适应中的关键挑战，并支持将单细胞拉曼光谱转化为临床相关应用。结果表明，我们的方法提高了对批次、菌株和仪器变异性的鲁棒性，并在高细菌负荷条件下将鉴定时间从几天缩短至几分钟。

## Abstract
The escalating threat of antibiotic resistance demands a rapid and accurate pathogen identification. While Raman spectroscopy combined with deep learning supports fast detection, model robustness remains compromised by domain shifts arising from instrument heterogeneity, batch variability, and strain diversity. To address this, we propose the Raman Spectral Classification Discrepancy Model (RSCDM), a novel domain adaptation framework that dynamically identifies target samples far from the source domain feature distribution via output discrepancies between task-specific classifiers. It adversarially aligns features of different domains to bridge the spectral variability. Unlike traditional methods relying on fixed-domain assumptions, RSCDM leverages classifier output differences to adaptively detect out-of-distribution samples, enabling task-driven domain alignment. Experimental results demonstrate that RSCDM enhances classification accuracy for seven bacterial species across batches and strains from 81.6% to 95.4% using a commercial spectrometer and from 77.5% to 91.3% for six clinical isolates (excluded from training) obtained with a home-built spectrometer. Fine-tuning the pretrained model on reference strains' spectra acquired by both commercial and home-built spectrometers further boosts the identification accuracy of clinical isolates to 99.3%, validating robustness to instrument diversity. Together, these findings address critical challenges in spectral domain adaptation and support translation of single-cell Raman spectroscopy into clinically relevant settings. The results demonstrate that our method improved robustness to batch/strain/instrument variability and reduced identification time from days to minutes under the high-bacterial-load conditions.