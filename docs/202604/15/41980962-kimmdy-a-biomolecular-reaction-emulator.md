---
title: "KIMMDY: a biomolecular reaction emulator."
title_zh: KIMMDY：一种生物分子反应模拟器
authors: "Eric Hartmann, Jannik Buhr, Kai Riedmiller, Evgeni Ulanov, Boris N Schüpp, Denis Kiesewetter, Daniel Sucerquia, Camilo Aponte-Santamaría, Frauke Gräter"
date: 2026-04-14
pdf: "https://pubmed.ncbi.nlm.nih.gov/41980962/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 用于预测生物分子反应速率的图神经网络
tldr: 针对生物分子反应模拟中计算成本高、难以处理长时间尺度及复杂级联反应的问题，本文开发了名为 KIMMDY 的反应仿真器。该工具结合动力学蒙特卡洛算法与图神经网络，能够在大规模构象系综中预测反应速率并模拟竞争性反应。实验证明 KIMMDY 在蛋白质和 DNA 的自由基反应、亲核取代等场景下表现优异，为理解复杂生化过程提供了高效的计算手段。
selection_source: fresh_fetch
motivation: 传统的分子动力学模拟在处理涉及秒级长时间尺度和复杂竞争路径的生物化学反应时面临巨大的计算挑战。
method: 利用动力学蒙特卡洛框架结合图神经网络预测反应速率，在动态构象系综中模拟连续且竞争的生化反应过程。
result: 在蛋白质和 DNA 的自由基反应、亲核取代及光二聚化等多种应用场景中，该方法成功复现了实验数据并展示了处理大规模系统的能力。
conclusion: KIMMDY 填补了微观模拟与宏观生化动力学之间的空白，为理解复杂生物系统中的反应级联和指导湿实验提供了新工具。
---

## 摘要
分子模拟已成为生物研究中不可或缺的手段。尽管其准确性不断提高，但直接模拟生化反应（所有生命过程的核心）在计算上仍然具有挑战性。在此，我们提出了一种生物分子反应模拟器 KIMMDY，它利用动力学蒙特卡洛（kinetic Monte Carlo）方法对构象系综中的反应进行建模。我们的方法能够处理具有连续、竞争反应的动态大规模系统，甚至可以处理秒级或更慢时间尺度的反应。它利用图神经网络进行大规模反应速率预测，同时也能够使用更简单的基于物理或启发式的模型。我们通过实验数据验证了该方法，并通过一系列应用展示了其强大功能和通用性，包括自由基反应、亲核取代和光二聚化。示例系统涵盖了蛋白质和 DNA。KIMMDY 有助于理解复杂系统中的生化反应级联，帮助重新解释实验数据，并能为未来的湿实验提供启发。

## Abstract
Molecular simulations have become indispensable in biological research. Their accuracy continues to improve, but directly modelling biochemical reactions - central to all life processes - remains computationally challenging. Here, we present a biomolecular reaction emulator that models reactions across conformational ensembles using kinetic Monte Carlo. Our method, KIMMDY, is capable of handling dynamic, large-scale systems with successive, competing reactions, even on the second timescale or slower. It leverages graph neural networks for large-scale prediction of reaction rates, while also being capable of using simpler physics-based or heuristic models. We validate our approach against experimental data and showcase its power and versatility through a series of applications, including radical reactions, nucleophilic substitutions, and photodimerization. Example systems span proteins and DNA. KIMMDY aids the understanding of biochemical reaction cascades in complex systems, helps to re-interpret experimental data, and can inspire future wet-lab experiments.