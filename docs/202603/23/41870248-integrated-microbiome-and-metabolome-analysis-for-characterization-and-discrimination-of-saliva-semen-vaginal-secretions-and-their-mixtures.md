---
title: "Integrated Microbiome and Metabolome Analysis for Characterization and Discrimination of Saliva, Semen, Vaginal Secretions, and Their Mixtures."
title_zh: 整合微生物组与代谢组分析用于唾液、精液、阴道分泌物及其混合物的表征与鉴别
authors: "Yu Deng, Xiaoyuan Zhen, Ruocheng Xia, Ruxin Zhu, Gongying Zhang, Pengyu Chen, Jianghua Lai, Ruiyang Tao"
date: 2026-03-23
pdf: "https://pubmed.ncbi.nlm.nih.gov/41870248/"
tags: ["query:seqai"]
score: 7.0
evidence: 用于体液识别的16S rRNA测序和微生物特征分析
tldr: "法医学中准确识别体液来源及遗留时间具有挑战性。本研究通过整合全长16S rRNA测序与非靶向代谢组学技术，分析了唾液、精液、阴道分泌物及其混合物在不同暴露时间下的特征。结果显示，多组学数据的融合显著提升了分类性能，随机森林模型在体液识别任务中达到了100%的准确率，为复杂法医样本的精准鉴定提供了新思路。"
selection_source: fresh_fetch
motivation: 针对法医学中单一组学难以准确区分混合体液及判定遗留时间的问题，探索微生物与代谢物联合分析的潜力。
method: 采集唾液、精液、阴道分泌物及其混合样本，利用16S rRNA测序和UHPLC-QTOF/MS技术获取微生物与代谢谱，并构建随机森林分类模型。
result: "发现各体液具有独特的微生物-代谢物关联网络，且多组学融合模型的识别准确率从单组学的约80%提升至100%。"
conclusion: 整合微生物组与代谢组数据能有效克服复杂样本的鉴定难题，显著提高法医体液识别的准确性与可靠性。
---

## 摘要
体液鉴定 (BFID) 和遗留时间 (TsD) 推断在法医学实践中具有重要价值，但也具有挑战性。先前的研究表明，整合微生物和代谢组谱图可提供互补的生物学见解。因此，本研究对新鲜唾液 (SA)、精液 (SE)、阴道分泌物 (VF) 及其混合物 (SA-VF 和 SE-VF) 进行了非靶向代谢组学分析和全长 16S rRNA 测序，并在室内暴露 15 天和 30 天后进行了额外的微生物分析。结果显示，单一体液样本表现出特定的优势细菌类群，而两种混合样本则包含来自两种组成体液的可检测细菌特征。非靶向 UHPLC-QTOF/MS 分析揭示了每种体液独特的代谢特征，这些特征在类固醇和胆汁酸代谢等生物相关通路中富集。此外，我们初步鉴定了特征代谢物，包括 α-茄碱、抗念珠菌素和巨霉素 C1，其中一些是罕见的微生物抗生素。由于非靶向方法的探索性质及其相关限制，这些结果可作为识别潜在候选物的临时参考。代谢组和微生物组数据的整合揭示了强烈的代谢物-微生物相关性，突显了每种体液类型特有的受微生物影响的代谢网络。分别使用差异微生物和代谢物作为输入特征，随机森林模型实现的 BFID 准确率分别为 80% 和 83.1%；然而，整合这两组特征后，准确率提高到了 100%。相比之下，基于微生物的 TsD 预测在单一体液样本中表现良好，但在混合样本中效果有所下降。总之，我们的研究强调了微生物组与代谢组数据整合在 BFID 中强大的预测潜力和提高的预测准确性。

## Abstract
Body fluid identification (BFID) and estimation of time since deposition (TsD) are valuable yet challenging in forensic practice. Previous studies have demonstrated that integrating microbial and metabolomic profiles provides complementary biological insights. Therefore, this study performed untargeted metabolomic profiling and full-length 16S rRNA sequencing on fresh saliva (SA), semen (SE), vaginal secretions (VF), and their mixtures (SA-VF and SE-VF), with additional microbial analysis after 15 and 30 days of indoor exposure. Results showed the single-fluid samples exhibited specific dominant bacterial taxa, whereas the two mixture samples contained detectable bacterial signatures from both constituent fluids. Untargeted UHPLC-QTOF/MS analysis revealed unique metabolic signatures for each body fluid, enriched in biologically relevant pathways like steroid and bile acid metabolism. Moreover, we putatively identified characteristic metabolites, including α-solanine, candicidin, and megalomicin C1, some of which are rare microbial antibiotics. Owing to the exploratory nature and associated constraints of nontargeted approaches, these results serve as a provisional reference for identifying potential candidates. Integration of metabolomic and microbiome data uncovered strong metabolite-microbe correlations, highlighting microbially influenced metabolic networks unique to each body fluid type. Using differential microbes and metabolites individually as input features, the random forest model achieved BFID accuracies of 80 and 83.1%, respectively; however, integrating both sets of features increased accuracy to 100%. In contrast, microbial-based TsD prediction performed well for single-fluid samples but showed reduced effectiveness for mixed samples. Overall, our research highlights the powerful predictive potential and improved predictive accuracy of the integration of microbiome and metabolome data in BFID.