---
title: Enzyme-constrained genome-scale model of Yarrowia lipolytica predicts growth-phase specific metabolic engineering targets.
title_zh: 解脂耶罗维亚酵母的酶约束全基因组尺度模型预测生长阶段特异性的代谢工程靶点
authors: "Juliano Sabedotti De Biaggi, Young-Kyoung Park, Eduard J Kerkhoven, Rodrigo Ledesma-Amaro, Petri-Jaan Lahtvee"
date: 2026-03-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/41876849/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 深度学习用于基因组规模代谢模型中的酶约束
tldr: 针对解脂耶氏酵母在工业生物制造中代谢预测精度不足的问题，本研究构建了受酶约束的全基因组代谢模型 eciYali5-GEM。通过整合深度学习预测的酶参数与不同生长阶段的蛋白质组学数据，该模型克服了传统模型无法捕捉代谢动态变化的局限。结果显示，模型能精准识别脂质和类胡萝卜素合成在特定生长阶段的代谢工程靶点，并提出了基于诱导型启动子的优化策略，为提升微生物工厂产量提供了高效的理性设计工具。
selection_source: fresh_fetch
motivation: 传统的全基因组代谢模型因缺乏酶促反应速率约束，难以准确预测解脂耶氏酵母在不同生长阶段的代谢工程靶点。
method: 结合深度学习预测的酶参数与多阶段蛋白质组学数据，构建并校准了受酶约束的代谢模型 eciYali5-GEM。
result: 模型成功预测了脂质和类胡萝卜素生产中具有生长阶段特异性的代谢靶点，包括已验证的基因和待实验的新靶点。
conclusion: 酶约束模型显著提升了代谢预测的准确性，为解脂耶氏酵母的精准代谢工程改造提供了重要的计算工具和理论指导。
---

## 摘要
产油酵母解脂耶罗维亚酵母（Yarrowia lipolytica）作为一种工业生物技术平台正变得日益重要，并得到了多种可用代谢工程工具的支持。全基因组尺度模型（GEMs）与该酵母的迭代改良密切相关，而酶活性约束（ecGEMs）增强了这些模型的预测能力。尽管最新的 ecGEM 重建工具利用深度学习来扩大这些约束的覆盖范围，但该方法尚未应用于解脂耶罗维亚酵母模型。本文描述了解脂耶罗维亚酵母 ecGEM（eciYali5-GEM）的重建，及其在预测该酵母中分别用于增强脂质和类胡萝卜素产量的代谢工程靶点方面的应用。为此，我们利用从两种工程菌株（分别生产脂质和类胡萝卜素）及其亲本菌株的不同生长阶段收集的生理通量和质谱蛋白质组学数据，对一个人工构建的解脂耶罗维亚酵母模型进行了约束。我们发现，酶约束能够预测生长阶段特异性的代谢工程靶点，而普通 GEMs 并不具备这一特征。结合这些靶点与其他基于 ecGEM 的见解，我们提出了两种进一步代谢工程的策略，包括使用诱导型启动子对靶点（如用于类胡萝卜素生产的八氢番茄红素脱氢酶）进行精确的生长阶段特异性表达。这些靶点包括先前已在别处验证过的基因，以及等待实验验证的新基因。该模型已公开，可被不同的代谢工程工作类似地调整和使用，使其成为将解脂耶罗维亚酵母开发为微生物细胞工厂的通用工具。关键点：• eciYali5-GEM 的重建使用了计算机模拟和体外蛋白质组学数据。• 酶约束丰富了解脂耶罗维亚酵母 ecGEM 的预测。• eciYali5-GEM 改进了代谢工程的理性设计。

## Abstract
The oleaginous yeast Yarrowia lipolytica has been gaining increasing importance as an industrial biotech platform, supported by several available metabolic engineering tools. Genome-scale models (GEMs) are relevant to the iterative improvement of this yeast, and their predictive ability is enhanced by enzymatic activity constraints (ecGEMs). Although the newest tools for ecGEM reconstruction use deep learning to expand the coverage of these constraints, this approach has not yet been applied to Y. lipolytica models. This paper describes the reconstruction of an ecGEM of Y. lipolytica (eciYali5-GEM) and its application in predicting metabolic engineering targets for enhanced lipid and carotenoid production, respectively, in this yeast. To achieve this, we constrained a manually curated Y. lipolytica model with physiological flux and mass-spectrometry proteomics data collected from distinct growth phases of two engineered strains (producing lipids and carotenoids, respectively) and their parental strain. We found that the enzymatic constraints enable the prediction of growth-phase-specific metabolic engineering targets, a feature not displayed by regular GEMs. Combining these targets with other ecGEM-based insights, we propose two strategies for further metabolic engineering, including the use of inducible promoters for precise, growth-phase-specific expression of targets such as phytoene dehydrogenase for carotenoid production. These targets included genes previously validated elsewhere, as well as novel genes awaiting experimental validation. This model, which is publicly available, can be similarly adapted and used by different metabolic engineering efforts, making it a versatile tool for the development of Y. lipolytica as a microbial cell factory. KEY POINTS: • eciYali5-GEM reconstruction used in silico and in vitro proteomics data. • Enzyme constraints enriched Y. lipolytica ecGEM predictions. • eciYali5-GEM improves metabolic engineering rational design.