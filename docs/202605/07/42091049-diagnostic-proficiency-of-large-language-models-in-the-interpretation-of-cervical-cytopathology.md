---
title: Diagnostic Proficiency of Large Language Models in the Interpretation of Cervical Cytopathology.
title_zh: 大语言模型在宫颈细胞病理学解读中的诊断能力
authors: "Iason Psilopatis, Kleio Vrettou"
date: 2026-05-06
pdf: "https://pubmed.ncbi.nlm.nih.gov/42091049/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 评估大语言模型在细胞病理学诊断解释中的能力
tldr: "针对大语言模型在宫颈细胞病变诊断中的可靠性问题，本研究评估了 Gemini、Claude 和 Copilot 在处理 30 例标准化 PAP 涂片案例时的表现。结果显示，虽然模型在识别正常细胞方面表现尚可（约 90% 准确率），但在识别感染性病原体和恶性肿瘤方面存在严重缺陷，甚至将浸润癌误诊为良性。这表明当前多模态大模型尚不能胜任临床诊断，仅可作为辅助教学工具。"
selection_source: fresh_fetch
motivation: 评估当前主流多模态大语言模型在宫颈细胞病理学（PAP 涂片）诊断中的准确性与临床应用潜力。
method: 采用零样本提示词（Zero-shot prompt），让 Gemini、Claude 和 Copilot 对来自数字图谱的 30 例代表性宫颈细胞案例进行分类诊断。
result: 模型在识别正常形态时表现较好，但在区分感染、异型增生及恶性肿瘤时准确率大幅下降，且存在严重的漏诊和误诊现象。
conclusion: 当前大语言模型无法独立进行宫颈癌筛查诊断，应定位为受人工监管的教育辅助工具而非自主诊断工具。
---

## 摘要
本研究旨在评估成熟的多模态大语言模型（LLMs）——特别是 Gemini、Claude 和 Copilot——在解读宫颈细胞病理学（巴氏涂片）方面的诊断能力。这项诊断准确性研究使用了来自《子宫颈细胞病理学数字图谱》（Cytopathology of the Uterine Cervix-Digital Atlas）的 30 个代表性病例作为金标准。研究采用标准化的零样本（zero-shot）提示词对模型进行测试，以区分正常细胞、良性改变（感染）和宫颈细胞异常。结果显示，各模型表现出显著的差异性。虽然 Gemini 和 Copilot 在识别正常生理形态方面表现出较高的熟练度（90%），但在感染性病原体和异型增生/肿瘤性病变方面的表现则急剧下降。值得注意的是，所有模型都将几例浸润性癌误分类为良性或低级别病变。Claude 表现出较高的“诊断升级”率，经常将正常细胞误认为存在异常。由于显著的过度诊断率以及未能检测出浸润性癌，目前的大语言模型尚不足以对宫颈异型增生和恶性肿瘤进行明确诊断。它们应被视为新兴的教育辅助工具，而非自主诊断工具，且需要严格的人工监督。

## Abstract
To evaluate the diagnostic proficiency of well-established multimodal Large Language Models (LLMs)-specifically Gemini, Claude, and Copilot-in interpreting cervical cytopathology (PAP smears). This diagnostic accuracy study used 30 representative cases from the "Cytopathology of the Uterine Cervix-Digital Atlas," which represented the gold standard. The models were tested using a standardized, zero-shot prompt to distinguish between normal cells, benign modifications (infections), and cervical cell abnormalities. The models demonstrated significant variability. While Gemini and Copilot showed high proficiency (90%) in identifying normal physiological morphology, performance declined sharply for infectious pathogens and dysplastic/neoplastic lesions. Notably, all models misclassified several invasive carcinomas as benign or low-grade lesions. Claude exhibited a high rate of "diagnostic escalation," frequently misidentifying normal cells as having abnormalities. Current LLMs are inadequate for the definitive diagnosis of cervical dysplasia and malignancy due to significant rates of overdiagnosis and failure to detect invasive carcinomas. They should be viewed as emerging educational aids rather than autonomous diagnostic tools, requiring rigorous human oversight.