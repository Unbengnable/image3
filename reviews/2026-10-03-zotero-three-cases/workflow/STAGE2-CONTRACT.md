# Stage 2：Codex 辅助矢量重建

产品定义：FigureCompose = Codex-native scientific figure generation + Codex-assisted vector reconstruction。

一个案例的输入为实际 `figure.png`、原始 `request.txt` 与可选 `context.md`、实际 `generation-prompt.txt`、`selected-references.json`。这些是已保存的普通文件，不要求用户编写模板、schema、图谱或坐标。参考图的使用方式同时记录。

Codex 查看 PNG，结合原始科学上下文与 prompt 重建一次性 SVG。可选择全部矢量，也可保留独立的局部 raster 插图。没有强制模板或统一 renderer；优先调用已安装的成熟 XML/SVG 检查和渲染工具。AutoFigure-Edit 的局部工具可按需复用，完整 SAM3/RMBG/API 管线属于可选路线，不是默认前提。

输出只有三个核心文件：`figure.svg`、`svg-preview.png`、`editability-check.json`。检查文件记录实际 text/vector/image 结构、所用工具、实际编辑 probe、视觉复核状态和未验证项。纯结构检查不得自动标记科学与视觉通过；Codex 必须查看实际渲染后补记判断。

文字、公式、关键图形和关系保持实际编辑价值；整张 PNG 包进 SVG 不算通过，包括添加 dummy 文字/矢量的包装。重建不得悄悄改变科学关系、丢失图注或把生成纹理当真实数据。像素级一致、正常论文栏宽可读性和原生设计软件导入是分别需要验证的事项。

`run.py --stage finalize` 只检查已存在的输入和 Codex 写出的 SVG，调用现成工具完成保存/渲染/结构记录。它不自动替 Codex 看图、构图或验证科学事实。无新的模型调用或绘图脚本。使用不同输出目录保存修订；保留已有产物。
