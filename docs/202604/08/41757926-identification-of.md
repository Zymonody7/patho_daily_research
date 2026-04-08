---
title: Identification of
title_zh: 曲霉属的鉴定
authors: "Meng Tan, Zhe Guo, Yanyi Wang, Xinyi Xu, Wei Cao, Zhaoyang Liu, Chuanhao Jiang"
date: 2026-04-08
pdf: "https://pubmed.ncbi.nlm.nih.gov/41757926/"
tags: ["query:pathoai"]
score: 7.0
evidence: 深度学习用于图像中的真菌病原体识别
tldr: "针对临床微生物实验室中曲霉菌因形态相似导致难以快速准确鉴定的问题，本研究开发了基于深度学习的 FungalNet 模型。该模型结合 ResNet-50 架构与 Focal Loss 算法，利用 11,689 张高分辨率显微图像进行训练，并引入了结合交叉验证与专家审核的质量控制流程。实验结果显示，FungalNet 在组别和物种水平的鉴定准确率分别达到 98.45% 和 97.85%，为临床真菌鉴定提供了一种高效、低成本的自动化方案。"
selection_source: fresh_fetch
motivation: 传统的显微形态学方法难以区分亲缘关系接近且形态相似的曲霉菌物种，限制了临床诊断和抗真菌治疗的及时性。
method: 提出 FungalNet 模型，通过集成 ResNet-50 骨干网络与 Focal Loss 损失函数，并配合五折交叉验证的质量控制手段，对 12 种临床曲霉菌的显微图像进行特征提取与分类。
result: "FungalNet 在曲霉菌组别和物种级别的分类准确率分别达到 98.45% 和 97.85%，性能显著优于 GoogLeNet 和 Xception 等主流深度学习模型。"
conclusion: 基于深度学习的图像分析技术能够实现曲霉菌的快速精准鉴定，具备集成到临床常规诊断流程中以提升真菌鉴定效率的潜力。
---

## 摘要
临床微生物实验室中曲霉属（Aspergillus）物种的快速准确鉴定对于曲霉病的诊断和抗真菌治疗至关重要。然而，由于形态学上的相似性，传统方法在区分系统发育相关的物种方面仍面临挑战。本研究提出了 FungalNet，这是一种集成了 ResNet-50 架构和 Focal Loss 算法的深度学习模型，专门设计用于增强曲霉属鉴定的特征提取。研究从 100 倍油镜下的乳酚棉蓝染色载玻片制剂中获取了总计 12,000 张高分辨率图像，其中 311 张图像通过结合五折交叉验证和专家人工审查的新型质量控制方法被剔除。使用剩余的 11,689 张合格图像评估了四种深度学习模型（FungalNet 和三种现有模型）在鉴定曲霉属物种和组（sections）方面的性能。FungalNet 表现出卓越的分类性能，在组水平和物种水平上的总体准确率分别达到 98.45% 和 97.85%。这些结果表明，FungalNet 在快速准确鉴定曲霉属物种方面具有显著的应用前景。随着进一步的优化和多中心验证，该工具可能被整合到常规诊断工作流程中，以提高临床环境下真菌鉴定的效率和可靠性。重要性：本研究将显微形态鉴定与深度学习相结合，以解决准确鉴定曲霉属物种的挑战。研究纳入了属于 8 个不同组的 12 种临床分离曲霉属物种。从 100 倍油镜下乳酚棉蓝染色的透明胶带法载玻片制剂中收集了 11,689 张合格图像，并使用 FungalNet（本研究提出的模型）以及三种现有模型（GoogLeNet、ResNet-50 和 Xception）进行了分析。结果显示，FungalNet 在曲霉属鉴定中表现出优异的性能，在组水平（98.45%）和物种水平（97.85%）均达到了最高的分类准确率。鉴于其周转时间快且具有成本效益，这种基于人工智能的图像分析方法在临床微生物实验室快速准确鉴定曲霉属物种方面展现出巨大的潜力。

## Abstract
Rapid and accurate identification of Aspergillus species in clinical microbiology laboratories is crucial for aspergillosis diagnosis and antifungal therapy. However, traditional methods still face challenges in distinguishing phylogenetically related species due to their morphological similarities. This study presents FungalNet, a deep learning model integrating ResNet-50 architecture with Focal Loss algorithm, specifically designed to enhance feature extraction for Aspergillus identification. A total of 12,000 high-resolution images were obtained from lactophenol cotton blue-stained slide preparations under a 100× oil immersion objective, among which 311 images were excluded through a novel quality control approach combining fivefold cross-validation and expert manual review. The performance of four deep learning models (FungalNet and three established models) for identifying Aspergillus species and sections was evaluated using the remaining 11,689 qualified images. FungalNet demonstrated superior classification performance, achieving overall accuracies of 98.45% and 97.85% at the section and species levels, respectively. These results indicate that FungalNet shows significant promise for rapid and accurate identification of Aspergillus species. With further optimization and multicenter validation, this tool could potentially be integrated into routine diagnostic workflows to enhance the efficiency and reliability of fungal identification in clinical settings.IMPORTANCEThis study integrates microscopic morphology identification with deep learning to address the challenge of accurate Aspergillus species identification. Twelve clinically isolated Aspergillus species belonging to eight different sections were included. From touch-tape slide preparations with lactophenol cotton blue staining under a 100× oil immersion objective, 11,689 qualified images were collected and analyzed using FungalNet (our proposed model) along with three established models (GoogLeNet, ResNet-50, and Xception). The results showed that FungalNet demonstrated superior performance in Aspergillus identification, achieving the highest classification accuracy at both section (98.45%) and species (97.85%) levels. Given its rapid turnaround time and cost-effectiveness, this AI-based image analysis approach shows promising potential for the rapid and accurate identification of Aspergillus species in clinical microbiology laboratories.