---
title: "A low-cost \"plant-scanner\" platform for automated detection of Ustilago maydis infection in maize using deep learning."
title_zh: 一种用于利用深度学习自动检测玉米中玉米黑粉菌感染的低成本“植物扫描仪”平台
authors: "Marvin Christ, Seyed Amir Hossein Tabatabaei, Niklas Ostwald, Oskar Seifert, Itzel Rubio Elizalde, Paul Klemm, Clemens Thölken, Marcus Lechner, Nasim Faridnia, Gert Bange, Keywan Sohrabi"
date: 2026-07-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/42436216/"
tags: ["query:pathoai"]
score: 7.0
evidence: 深度学习用于植物真菌感染的自动检测
tldr: 针对玉米黑粉菌感染缺乏自动化量化工具的问题，本研究开发了一套低成本的旋转摄像头扫描平台，通过采集多角度视频并结合深度学习进行分析。研究对比了传统机器学习与YOLO11模型，结果显示基于YOLO11的方法在检测感染症状上表现卓越，AUC达到0.99-1.00。该方案为植物病理学提供了一个开源、可复现且无偏见的自动化评分工具，具有极高的实用价值。
selection_source: fresh_fetch
motivation: 旨在解决实验室环境下人工识别玉米黑粉菌感染症状效率低、主观性强且缺乏自动化定量分析手段的挑战。
method: 开发了一套配备旋转摄像头和定制照明的硬件平台，并分别采用手工特征结合传统分类器以及预训练的YOLO11深度学习模型进行对比实验。
result: 实验表明YOLO11模型在检测和分类感染症状方面表现近乎完美，其AUC值高达0.99-1.00，远超传统机器学习方法的0.90。
conclusion: 该低成本、开源的自动化扫描平台为植物病害的精准检测提供了高效方案，其模块化设计使其易于推广至其他植物病理学研究领域。
---

## 摘要
玉米黑粉菌（Ustilago maydis）是一种活体营养型真菌，可引起玉米黑粉病，导致植物地上部分形成肿瘤。尽管玉米黑粉菌已成为植物-真菌相互作用研究的模型，但目前尚无工具能够在实验室条件下自动量化感染症状以进行深度学习分析。为解决这一问题，我们开发了一种旋转摄像系统，可在定制的光照和快门设置下捕捉植物视频。这些视频被用于训练机器学习模型，以区分健康植株和受感染植株。本文提出了两种检测方法。在第一种方法中，通过采用简单的掩码技术并结合利用手工特征的经典机器学习分类器，该模型取得了合理的性能，其中一个分类器的受试者工作特征曲线（ROC）下面积（AUC）最高达到0.90，表现出较高的灵敏度和特异性。第二种方法利用预训练的 YOLO11 模型进行目标检测和进一步分类。基于 YOLO11 的方法优于传统方法，实现了近乎完美的验证准确率（AUC：0.99-1.00），证明了其在实时、可扩展应用中的优越性。我们的工具集具有成本效益高、可定制且采用开放式积木设计的扫描平台，为无偏见的疾病症状检测和评分提供了宝贵的概念验证资源，在其他植物病理学研究中具有潜在应用价值。这一点使得其他研究实验室能够轻松复制和调整，从而使该平台在特定应用之外具有鲁棒性、可扩展性和实用性。

## Abstract
Ustilago maydis is a biotrophic fungus that causes smut disease in maize, leading to tumor formation on aerial parts of the plant. While U. maydis has been a model for plant-fungal interaction studies, no tool has existed to automatically quantify infection symptoms under laboratory conditions for deep learning analysis. To address this, we developed a rotating camera system that captures videos of plants under customized lighting and shutter settings. These videos were used to train machine learning models to distinguish between healthy and infected plants. Two detection approaches have been presented. In the first approach, by employing a naive masking technique and combining classical machine learning classifiers utilizing handcrafted features, the model achieved a reasonable performance, with an Area Under the Curve (AUC) of maximum 0.90 on the Receiver Operating Characteristic in one of the classifiers, showing relatively high sensitivity and specificity. The second approach utilizes pre-trained YOLO11 model for object detection and further classification. The YOLO11-based approach outperforms traditional methods, achieving near-perfect validation accuracy (AUC: 0.99-1.00), demonstrating its superiority for real-time, scalable applications. Our toolset, featuring a cost-efficient and customizable scanning platform with open building-blocks design, provides a valuable resource as a proof-of-concept for unbiased disease symptom detection and scoring, with potential applications in other plant pathology studies. This point enables easy replication and adaptation by other research laboratories which makes the platform robust, scalable and practical beyond our specific application.