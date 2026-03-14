---
title: A Machine learning pipeline to investigate tissue ingrowth in cerebral aneurysms using preclinical animal models.
title_zh: 一种利用临床前动物模型研究脑动脉瘤组织向内生长的机器学习流水线
authors: "Fatemeh Afsari, Ishaq Ansari, Melanie E Martinez, Lillian Atchison, Sayat Mimar, Koji Hosaka, Brian Hoh, Pinaki Sarder"
date: 2026-03-13
pdf: "https://pubmed.ncbi.nlm.nih.gov/41826635/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 基于Unet++的机器学习流水线用于临床前模型的定量评估
tldr: "针对脑动脉瘤栓塞治疗后组织长入评估主观且耗时的问题，本研究开发了基于 Unet++ 卷积神经网络的机器学习流水线。该方法在小鼠颈动脉瘤模型的高分辨率组织学图像上实现了高精度的囊腔分割与组织检测，Dice 系数均超过 94%。该工具不仅提高了评估的客观性与一致性，还通过图形界面降低了使用门槛，为临床前动脉瘤愈合机制研究提供了标准化量化手段。"
selection_source: fresh_fetch
motivation: 临床前模型中脑动脉瘤组织长入的定量评估目前依赖人工，存在主观性强、效率低且缺乏统一标准的问题。
method: 构建了一个基于 Unet++ 架构的深度学习流水线，结合图像增强、归一化预处理及阈值后处理技术，对组织学图像进行自动化分割。
result: "模型在囊腔分割和组织检测任务中分别达到了 94.58% 和 95.23% 的 Dice 系数，且在盲测中表现出优于专家的一致性。"
conclusion: 该自动化工具为评估动脉瘤生物学稳定性提供了客观指标，有助于加速治疗策略的筛选及愈合机制的标准化研究。
---

## 摘要
脑动脉瘤是一种危及生命的疾病，其特征是脑血管中形成囊状凸起，可能破裂并导致严重并发症。一种治疗方法是将柔软、灵活的金属丝（弹簧圈）插入动脉瘤内，以促进凝血和封闭。介质通常用于模拟囊内的组织向内生长，以稳定愈合并防止复发。然而，临床前模型中组织向内生长的定量评估仍然费时费力、具有主观性且缺乏标准化，限制了比较治疗策略和愈合机制的能力。我们开发了一种基于 Unet++ 卷积神经网络 (CNN) 的稳健机器学习 (ML) 流水线，专门针对临床前颈动脉瘤小鼠模型中的组织向内生长进行分割和定量优化。该模型在 64 张高分辨率组织学图像上进行了训练和验证，采用了 10 折交叉验证。图像预处理包括调整大小、归一化和增强，而后期处理则对 CNN 生成的热图应用了阈值技术。我们的方法在囊腔分割和组织向内生长检测方面分别实现了 94.58% 和 95.23% 的 Dice 系数，AUC 分别为 99.24% 和 96.78%。模型的预测结果与地面真值（ground truth）表现出高度一致性（[Formula: see text]），支持其在评估生物稳定性及辅助临床决策方面的潜力。在针对专家标注的盲测评估中，我们的 AI 模型在所有评分者中达到了最高的一致性（Cohen's κ），证明了其提供一致且专家级组织向内生长评估的潜力。开发了一个用户友好的图形界面，使非技术用户能够进行分割并定量组织向内生长。通过提供客观、可重复的瘤内愈合指标，该方法支持了临床前动脉瘤模型中治疗效果的机制研究，并为促进愈合干预措施的标准化评估奠定了基础。

## Abstract
Cerebral aneurysm is a life-threatening condition characterized by the formation of a saccular bulge in brain blood vessels, which can rupture and lead to severe complications. One treatment involves inserting a soft, flexible wire (coil) into the aneurysm to promote clotting and sealing. Mediators are often used to simulate tissue ingrowth within the sac to stabilize healing and prevent recurrence. However, quantitative assessment of tissue ingrowth in preclinical models remains labor-intensive, subjective, and poorly standardized, limiting the ability to compare therapeutic strategies and healing mechanisms. We developed a robust machine learning (ML) pipeline based on a Unet + + convolutional neural network (CNN), optimized for segmenting and quantifying tissue ingrowth in a preclinical carotid aneurysm mouse model. The model was trained and validated on 64 high-resolution histological images using 10-fold cross-validation. Image preprocessing included resizing, normalization, and augmentation, while post-processing applied thresholding techniques to CNN-generated heatmaps. Our method achieved Dice coefficients of 94.58% for sac segmentation and 95.23% for tissue ingrowth detection, with AUCs of 99.24% and 96.78%, respectively. The model's predictions showed strong agreement with ground truth ([Formula: see text]), supporting its potential for assessing biological stability and informing clinical decisions. In a blinded evaluation against expert annotations, our AI model achieved the highest agreement (Cohen's κ) among all raters, demonstrating its potential to provide consistent and expert-level tissue ingrowth assessments. A user-friendly graphical interface was developed, to enable non-technical users to perform segmentation and quantify tissue ingrowth. By providing objective, reproducible metrics of intra-aneurysmal healing, this approach supports mechanistic studies of therapeutic efficacy in preclinical aneurysm models and establishes a foundation for standardized evaluation of pro-healing interventions.