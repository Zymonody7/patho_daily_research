---
title: Efficient detection and typing of phage-plasmids.
title_zh: 噬菌体质粒的高效检测与分型
authors: "Karina Ilchenko, Remy A Bonnin, Eduardo P C Rocha, Eugen Pfeifer"
date: 2026-03-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/41660861/"
tags: ["query:seqai"]
score: 8.0
evidence: 基因组中噬菌体质粒检测与分型的计算方法
tldr: 噬菌体-质粒（P-Ps）兼具噬菌体和质粒的特征，导致现有工具难以将其与普通移动遗传元件区分。为此，研究者开发了 tyPPing 工具，通过分析保守蛋白质的频率和组合特征，实现了对 P-Ps 的高效识别与分类。实验证明该工具在灵敏度和可扩展性上优于现有方法，能准确识别携带抗药性或毒力因子的 P-Ps，为研究细菌进化和临床致病机理提供了可靠的生物信息学基础。
selection_source: fresh_fetch
motivation: 由于噬菌体-质粒同时具备两类遗传元件的特征，现有工具常将其误判，阻碍了对这类重要进化驱动因子的研究。
method: 开发了 tyPPing 识别工具，通过搜索特定的保守蛋白质频率和组合模式，将噬菌体-质粒从普通质粒和噬菌体中分离并分类。
result: 在多项数据库测试中，该工具展现出优于同类软件的灵敏度与扩展性，并成功在不完整的基因组草图中识别出具有功能的元件。
conclusion: 该研究为系统化鉴定和编目复杂的移动遗传元件提供了可靠基础，对理解抗生素耐药性传播具有重要意义。
---

## 摘要
噬菌体质粒（Phage-plasmids, P-Ps）是在溶源期以质粒形式复制的温和噬菌体。尽管它们具有高度多样性，但它们携带与噬菌体和质粒相似的基因。这导致了基因交换以及杂合或缺陷元件的形成，从而限制了对 P-Ps 的准确检测。为应对这一挑战，我们开发了 tyPPing，这是一种易于使用的方法，能够高效且高精度地检测和分型 P-Ps。它通过搜索特定的频率和保守蛋白集，将 P-Ps 与质粒和噬菌体区分开来。tyPPing 的优势在于其精确的预测能力以及对 P-Ps 进行系统分型的能力，包括分配置信度。我们在多个数据库和一组不完整（草图）基因组上测试了 tyPPing。虽然预测结果依赖于组装质量，但我们检测到了高质量的 P-Ps，并通过实验证明了它们的功能性。与其他分类方法相比，tyPPing 旨在检测不同的 P-P 类型，并在灵敏度和可扩展性方面超越了其他工具。P-Ps 具有高度多样性，使得系统地识别新类型成为一项艰巨的任务。然而，通过将 tyPPing 与其他工具相结合，我们为应对这一挑战奠定了宝贵的基础。tyPPing 及其他方法的使用说明已记录在我们的 GitHub 仓库中：github.com/EpfeiferNutri/Phage-plasmids/。重要性：移动遗传元件（如噬菌体和质粒）具有多样性，并通过水平基因转移驱动细菌进化。许多噬菌体质粒携带抗生素抗性基因或毒力因子，它们兼具噬菌体和质粒的特性，并拥有温和噬菌体和质粒的生命周期。这使得准确分类变得困难，因为目前的计算工具通常将它们归类为其中之一。我们通过开发 tyPPing 解决了这个问题，这是一种全新的高精度方法，用于系统地识别、分离和编目噬菌体质粒。我们证明了 tyPPing 具有高度准确性和广泛的兼容性。它为未来所有涉及噬菌体和质粒的研究提供了可靠的基础，涵盖从农业环境到临床环境中的致病菌株。

## Abstract
UNLABELLED: Phage-plasmids (P-Ps) are temperate phages that replicate as plasmids during lysogeny. Despite their high diversity, they carry genes similar to phages and plasmids. This leads to gene exchanges and to the formation of hybrid or defective elements, which limits accurate detection of P-Ps. To address this challenge, we developed tyPPing, an easy-to-use method that efficiently detects and types P-Ps with high accuracy. It searches for distinct frequencies and sets of conserved proteins to separate P-Ps from plasmids and phages. tyPPing's strength comes from both its precise predictions and its ability to systematically type P-Ps, including the assignment of confidence levels. We tested tyPPing on several databases and a collection of incomplete (draft) genomes. While predictions rely on the quality of assemblies, we detected high-quality P-Ps and experimentally proved them to be functional. Compared to other classification methods, tyPPing is designed to detect distinct P-P types and surpasses other tools in terms of sensitivity and scalability. P-Ps are highly diverse, making the systematic identification of new types a difficult task. By combining tyPPing with other tools, however, we show a valuable foundation for addressing this challenge. How to use tyPPing and other approaches is documented in our GitHub repository: github.com/EpfeiferNutri/Phage-plasmids/. IMPORTANCE: Mobile genetic elements, such as phages and plasmids, are diverse and drive bacterial evolution through horizontal gene transfer. Phage-plasmids, of which many carry antibiotic resistance genes or virulence factors, are both phages and plasmids and have life cycles of temperate phages and plasmids. This makes accurate classification difficult as current computational tools typically classify them as one or the other. We addressed this problem by developing tyPPing, a new and highly precise method, to systematically identify, separate, and catalog phage-plasmids. We demonstrated that tyPPing is highly accurate and broadly compatible. It provides a reliable foundation for all future studies involving phages and plasmids, ranging from agriculture environments to pathogenic strains of clinical settings.