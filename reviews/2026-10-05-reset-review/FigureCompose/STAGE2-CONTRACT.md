# Stage 2：Codex 辅助矢量重建

2026-10-04 补充：当前执行状态与顺序见 [PROGRESS.md](PROGRESS.md)。重建同时参考已保存 critique，可使用普通文本的最小 lock list 固定计数、数值和关键关系；它不是新 schema。将长解释移入 caption，保留科学范围及示意声明。分别核对科学正确性、视觉精简、可编辑性和构图保留。真实出版尺寸需实际重排及查看，不能由元素计数代替。Diffusion Policy canary 采用用户确认的 178 mm 主目标与 85 mm 压力检查，已完成本地四门验收，见 [acceptance](outputs/diffusion-policy-stage2/acceptance.md)；该尺寸不是所有案例的强制默认，85 mm 结果不代表完整单栏可读。

产品定义：FigureCompose = Codex-native scientific figure generation + Codex-assisted vector reconstruction。

一个案例的输入为实际 `figure.png`、原始 `request.txt` 与可选 `context.md`、实际 `generation-prompt.txt`、`selected-references.json`。这些是已保存的普通文件，不要求用户编写模板、schema、图谱或坐标。参考图的使用方式同时记录。

Codex 查看 PNG，结合原始科学上下文与 prompt 重建一次性 SVG。可选择全部矢量，也可保留独立的局部 raster 插图。没有强制模板或统一 renderer；优先调用已安装的成熟 XML/SVG 检查和渲染工具。AutoFigure-Edit 的局部工具可按需复用，完整 SAM3/RMBG/API 管线属于可选路线，不是默认前提。

输出只有三个核心文件：`figure.svg`、`svg-preview.png`、`editability-check.json`。检查文件记录实际 text/vector/image 结构、所用工具、实际编辑 probe、视觉复核状态和未验证项。纯结构检查不得自动标记科学与视觉通过；Codex 必须查看实际渲染后补记判断。

上述名称保留历史 prototype 的薄约定。当前 Diffusion Policy contract canary 的唯一交付文件为 `figure.svg`、`preview-178mm.png`、`preview-85mm.png`、`editability-check.json`、`semantic-lock.txt`、`caption.md`、`acceptance.md`，全部位于 `outputs/diffusion-policy-stage2/`。`figure.svg` 是源文件和最终产物，不新增 `reconstruction.svg`、`template.svg` 或 `svg-preview.png` 别名；既有 `finalize` 命令的历史文件名不覆盖此 canary 约定，可直接复用现有检查和渲染工具，不修改主链路。

π0 / attention 仅为 Stage 2 prototype evidence / pre-canary。当前 canary 首次联合验证真实尺寸、caption migration、semantic lock 与四门验收：SVG 根元素 `width="178mm"`，高度随构图确定，`viewBox` 与版面匹配。两个 PNG 均按 300 dpi 渲染并记录 DPI 元数据；178 mm 为 2102 px 宽，85 mm 为 1004 px 宽。85 mm 使用同一 SVG 缩放渲染，不能重新排版。

最终状态为 `ACCEPTED`（A/B/C/D 全 PASS）、`REVISE`（A PASS，B/C/D 有可修复失败）或 `NOT_ACCEPTED`（A FAIL）。未执行或证据不足为 `PENDING`，不能视为通过。此规则分门记录，无加权总分。

文字、公式、关键图形和关系保持实际编辑价值；整张 PNG 包进 SVG 不算通过，包括添加 dummy 文字/矢量的包装。重建不得悄悄改变科学关系、丢失图注或把生成纹理当真实数据。像素级一致、正常论文栏宽可读性和原生设计软件导入是分别需要验证的事项。

`run.py --stage finalize` 只检查已存在的输入和 Codex 写出的 SVG，调用现成工具完成保存/渲染/结构记录。它不自动替 Codex 看图、构图或验证科学事实。无新的模型调用或绘图脚本。使用不同输出目录保存修订；保留已有产物。
