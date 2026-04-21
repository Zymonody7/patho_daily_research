---
title: Single-cell co-mapping reveals relationship between chromatin state and gene expression in early zebrafish development.
title_zh: 单细胞联合图谱揭示了斑马鱼早期发育过程中染色质状态与基因表达的关系
authors: "Vivek Bhardwaj, Alberto Griffa, Helena Viñas Gaza, Peter Zeller, Alexander van Oudenaarden"
date: 2026-04-21
pdf: "https://pubmed.ncbi.nlm.nih.gov/42011025/"
tags: ["query:seqai"]
score: 7.0
evidence: 单细胞中转录组和组蛋白修饰的多模态测量
tldr: 针对脊椎动物胚胎发育中染色质状态与基因表达耦合机制不明的问题，研究者开发了一种能同时检测单细胞全长转录组和组蛋白修饰的多模态测量方法，并应用于斑马鱼早期发育研究。研究发现，在胚层形成前两者处于解离状态，随后在原肠胚期逐渐耦合；通过机器学习模型识别了谱系特异性转录因子及其表观遗传调控模式。该研究揭示了细胞身份建立过程中转录与染色质层的动态交互逻辑。
selection_source: fresh_fetch
motivation: 由于缺乏在单细胞水平同时检测组蛋白修饰与基因表达的手段，科学界对脊椎动物胚胎发育中染色质景观如何构建并维持细胞身份的了解十分有限。
method: 开发了一种单细胞多模态测序技术，在斑马鱼早期发育过程中同步获取单个细胞的全长转录组和组蛋白修饰数据。
result: 发现染色质与转录状态在胚层形成前互不关联，随后通过抑制性染色质扩散和细胞特异性去甲基化实现发育基因的精准沉默与状态耦合。
conclusion: 通过可解释机器学习模型对转录因子进行分类，阐明了表观遗传调控与转录因子表达如何共同作用以确立脊椎动物的细胞谱系身份。
---

## 摘要
建立细胞类型特异性的染色质景观对于胚胎发育过程中细胞身份的维持至关重要。然而，由于缺乏在同一细胞中联合检测染色质修饰和基因表达的方法，我们对脊椎动物胚胎发育过程中这一景观如何建立的了解十分有限。在此，我们展示了斑马鱼早期胚胎发育过程中单细胞全长转录组和组蛋白修饰的多模态测量。我们发现，在胚层形成之前，细胞的染色质状态与转录状态是解耦的，并在原肠胚形成和体节发生过程中逐渐建立联系。发育基因的沉默是通过抑制性染色质的局部扩散以及细胞类型特异性的去甲基化实现的。通过在可解释的机器学习模型中结合转录因子（TF）表达和染色质状态，我们将转录因子分类为谱系特异性激活因子和抑制因子，并鉴定出一组受表观遗传调控的转录因子。总之，我们的数据解析了脊椎动物早期发育过程中染色质与转录之间的动态关系，并阐明了这两层调控如何相互作用以建立细胞身份。

## Abstract
Establishing a cell type-specific chromatin landscape is crucial for the maintenance of cell identity during embryonic development. However, our knowledge of how this landscape is set during vertebrate embryogenesis has been limited, due to the lack of methods to jointly detect chromatin modifications and gene expression in the same cell. Here we present a multimodal measurement of full-length transcriptome and histone modifications in individual cells during early embryonic development in zebrafish. We show that before the formation of germ layers, the chromatin and transcription states of cells are uncoupled and become progressively connected during gastrulation and somitogenesis. Silencing of developmental genes is achieved by local spreading of repressive chromatin together with cell type-specific demethylation. Combining transcription factor (TF) expression and chromatin states within an interpretable machine learning model, we classify TFs as lineage-specific activators and repressors and identify a subset of TFs that are epigenetically regulated. Altogether, our data resolves the dynamic relationship between chromatin and transcription during early vertebrate development and clarifies how these two layers interact to establish cell identity.