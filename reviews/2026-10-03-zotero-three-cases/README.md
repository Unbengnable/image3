# Zotero 三案例审阅包

[完整报告](REPORT.md) · [比较页](comparison.html) · [导出说明](EXPORT-NOTES.md) · [逐文件清单](EXPORT-MANIFEST.json)

直接在浏览器打开 comparison.html，可同时看原图和生成图，并切换初稿/第一修订/最后一稿。每例 1 次生成与 2 次编辑，共 9 次内置 imagegen 调用。所有图片是 PNG，本轮没有 SVG。

|案例|结果|
|---|---|
|[FAST](fast/evaluation.json)|数值一致性未通过；上方展开列少一个零。|
|[Diffusion Policy](diffusion-policy/evaluation.json)|核心机制范围已复核；网络内部细节覆盖有限。|
|[DreamerV3](dreamerv3/evaluation.json)|prior 输入与在线反馈未通过完整关系检查。|

最后一稿 figure.png 表示修订预算结束后的结果，不等于通过验收。目标论文图像在九次调用结束后才查看。生成与评价都是同一 Codex，不是独立盲评；投稿尺寸没有验收。
