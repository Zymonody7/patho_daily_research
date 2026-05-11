---
title: Spatiotemporal evolution of a pine wilt disease model integrating infectious disease transmission and predator-prey interactions.
title_zh: 融合传染病传播与捕食者-猎物相互作用的松材线虫病模型的时空演化
authors: "Shuai Zhang, Peng Wu, Shengqiang Liu"
date: 2026-05-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/42113284/"
tags: ["query:pathoai"]
score: 6.0
evidence: 传染病传播与时空演化建模
tldr: 针对松材线虫病建模中忽视流行病传播与捕食关系耦合的问题，本文构建了一个整合捕食者-猎物动力学与疾病传播机制的时空演化模型。通过在辽宁省地理地图上的数值模拟，验证了模型与实际观测的一致性，并揭示了引入捕食者对疫情的显著抑制作用。研究通过最优控制理论分析了生物防治与人工干预的成本效益，为林业病害管理提供了科学的决策依据。
selection_source: fresh_fetch
motivation: 现有的松材线虫病模型通常将流行病传播与生态系统中的捕食关系割裂开来，无法准确描述生物防治下的时空动态。
method: 建立了一个耦合捕食者-猎物相互作用与疾病传播机制的偏微分方程模型，并利用COMSOL在辽宁省地理尺度上进行数值模拟。
result: 模拟结果在无捕食者时与实际疫情数据吻合，而引入捕食者后能有效抑制疾病扩散，并确定了不同成本下的最优控制策略。
conclusion: 生物防治在生态效益上具有优先性，但在实际管理中需根据捕食者引入成本与决策者支付意愿，在生物防治与人工干预间进行权衡。
---

## 摘要
以往关于松材线虫病（pine wilt disease）的模型研究大多局限于独立的流行病模型或捕食者-猎物模型，忽视了生态系统中这两种机制之间的耦合。本研究开发了一个耦合模型，将捕食者-猎物相互作用与松材线虫病的传播机制相结合，从而能够更准确地表征生物防治与疾病传播的时空动态。理论分析主要确立了在给定阈值条件下，几个关键子系统是持久的，并进一步证明了全系统稳态的存在性。利用 COMSOL Multiphysics 进行的数值模拟成功再现了中国辽宁省二维地理地图上松材线虫病的时空演化过程。在没有捕食者的情况下，模拟结果与实际观测数据一致；而引入捕食者后，疾病得到了有效抑制。基于抛物型系统的最优控制理论和数值模拟结果，本研究进一步系统分析了松材线虫病管理的最优策略选择：(1) 当已引入捕食者时，补充人为控制的额外收益可能有限；(2) 如果目标仅为生态效益，应优先考虑通过引入捕食者进行生物防治；(3) 根据成本效益分析和决策者的支付意愿，当引入捕食者的成本低于某一阈值时，首选生物防治；否则，人为控制在经济上更具合理性。

## Abstract
Previous modeling studies on pine wilt disease have largely been confined to either standalone epidemic models or predator-prey models, overlooking the coupling between these two mechanisms within the ecosystem. A coupled model is developed that integrates predator-prey interactions with the transmission mechanism of pine wilt disease, thereby enabling a more accurate representation of the spatiotemporal dynamics of biological control and disease transmission. The theoretical analysis primarily establishes that, under given threshold conditions, several key subsystems are persistent, and further proves the existence of steady states for the full system. Numerical simulations, implemented using COMSOL Multiphysics, successfully reproduced the spatiotemporal evolution of pine wilt disease on a two-dimensional geographical map of Liaoning Province, China. In the absence of predators, the simulated results are consistent with actual observational data, whereas the disease is effectively suppressed when predators are introduced. Based on the optimal control theory for parabolic systems and the results of numerical simulations, this study further systematically analyzes optimal strategy selection for pine wilt disease management: (1) When predators have been introduced, the additional benefit of supplementary human control may be limited; (2) If the goal is ecological effectiveness alone, biological control by predator introduction should be prioritized; (3) According to cost-effectiveness analysis and the decision-maker's willingness-to-pay, biological control is preferred when the cost of predator introduction is below a threshold; otherwise, human control is more economically justified.