# 上游实测与最小组合范围

历史记录：本文记录 2026-10-02 的完整 PaperVizAgent 组合和当日阻塞。2026-10-03 用户已要求由 Codex 替代文本编排，当前入口见 `README.md`、依赖解剖与实测见 `CODEX-NATIVE-REPORT.md`。本文中的 Google 配置要求不再是当前 Stage 1 的前提。

2026-10-02。先检查并运行上游，再确定兼容修改；本报告记录实际文件和运行结果。新原型位于 `FigureCompose`，与 legacy LocalFigure 是同级目录。旧架构开发已停止。

## 固定源码与独立环境

|项目|源码 commit|环境|
|---|---|---|
|[google-research/papervizagent](https://github.com/google-research/papervizagent)|`e088a8fff74cc363b6897c0843631fff76484908`|独立 `.venv`，Python 3.12.11，按原 requirements 安装 73 个包|
|[ResearAI/AutoFigure-Edit](https://github.com/ResearAI/AutoFigure-Edit)|`16f3749e9d512bdf7b7b55c162307bc289750b7a`|独立 `.venv`，Python 3.12.11，按原 requirements 安装 70 个包|

实际依赖版本分别存于 `audit/papervizagent-installed.txt` 和 `audit/autofigure-edit-installed.txt`。不能合并环境：本次 PaperVizAgent 安装了 openai 3.23.0、google-genai 2.27.0、Pillow 12.3.0，而 AutoFigure-Edit 的原 requirements 将其分别限制为 <2、<2、<12。

## 可以原样复用的能力

|环节|实际上游入口与行为|组合方式|
|---|---|---|
|自动参考选择|`RetrieverAgent.process(..., retrieval_setting='auto')`；读取原生 `ref.json`，diagram 候选最多取前 200 个，LLM 选择十个 reference ID|原样使用；现有主样本为 180 张，全部在候选范围内|
|参考驱动规划|`PlannerAgent.process` 加载选中的 caption、content 和实际图片，生成详细图像描述|保留原 Planner；仅修复参考图片载荷的字段不一致|
|视觉风格|原 Stylist 读取仓库自带的 `neurips2025_diagram_style_guide.md`|原样使用；没有新建 style grammar 或生成新的风格规则|
|图像生成与迭代|`PaperVizProcessor.process_single_query`，`exp_mode='demo_full'`：Retriever → Planner → Stylist → Visualizer → Critic 迭代|原样调用；最多三轮，关闭其 benchmark evaluation|
|导入已生成图片|AutoFigure-Edit CLI `--input_figure_path` 或 `method_to_svg(input_figure_path=...)`|原样使用；跳过 AutoFigure-Edit 自身的生图步骤|
|SVG 重建|原 SAM3 检测、box 合并、RMBG 裁剪、LLM SVG 模板、语法检查、可选优化及图标替换|原样使用；没有自建分割、布局或 SVG renderer|
|编辑|AutoFigure-Edit 自带 Web / svg-edit|原样使用；最终产物应有可编辑文字/向量，图片图标可以保留为图片对象|

PaperVizAgent 的自动检索本身基于 candidate 的文本内容，不直接对全部图片做视觉 embedding 排序；Planner 随后实际接收选中的图片。保留这一机制，没有另建检索模型或向量数据库。

## 实际输入与输出

PaperVizAgent 的单次输入为上游原生 dict：`content` 是科学上下文，`visual_intent` 是自然语言图像要求。可选的 `additional_info.rounded_ratio` 控制纵横比，`max_critic_rounds` 控制原有 Critic 轮数。它不要求用户提供模板、图谱、坐标或端口。

其参考记录需要四个已有字段：`id`、`content`、`visual_intent`、`path_to_gt_image`。现有 DiagramBank 的 title/abstract 映射到 content，caption 映射到 visual_intent，PNG 复制到原有 images 目录。参考 content 明确注明是 source abstract，不冒充完整 Methods。原图号、论文链接、rights 和 SHA-256 保存在附带的 source 清单。

PaperVizAgent 输出上游 dict，包含自动选择的 reference ID、规划/风格/批评文本、各阶段的 base64 JPEG、`eval_image_field` 指向的最终图。`run.py` 保存整个原生结果，并将最终图片保存成 PNG 供后一步导入。这是文件格式衔接，没有重绘或新图像生成逻辑。

AutoFigure-Edit 的 imported-figure 输入是 raster 文件路径。它输出 `figure.png`、`samed.png`、`boxlib.json`、图标 crops、`template.svg`、可选 `optimized_template.svg` 和 `final.svg`。其 CLI 将 method 文本与导入图片设为互斥输入；重建阶段主要依据已生成的图片。本原型不改动这个接口。

## 确认需要的极小修改

仅修改 PaperVizAgent 的三个文件，共 10 行新增、3 行删除。完整差异保存为 `audit/papervizagent-compat.patch`。

|问题|实际证据|修复|
|---|---|---|
|Windows 没有 `time.tzset()`|原始 `ExpConfig` 初始化直接抛 AttributeError；见 `papervizagent-pristine-config.log`|用 `hasattr` 包住该调用，Windows 沿用系统时区|
|Google API-key 回退未捕获 ADC 缺失异常|未改源码时连 `main.py --help` 都因 DefaultCredentialsError 退出；见 `papervizagent-pristine-help.log`|补捕获 DefaultCredentialsError，并提前初始化后续所需的 project/location|
|Planner 图片字段与 Gemini converter 不一致|原 Planner 发送 `image_base64`，converter 只读取 `source`；原格式转换得到 0 个 image part|让 Planner 按已有 converter 的 source 格式发送图片及实际 MIME；修正后得到 1 个 image part|

除此之外，定制仅为一次数据字段转换和 `run.py` 的两阶段调用、文件保存、凭据缺失提示。它使用两个原生环境和两个原生 pipeline；没有新 agents、schemas、templates、layout、routing、resolver、renderer 或 evaluation framework。AutoFigure-Edit 的 tracked 源码没有修改。

## 模型与 API 的真实要求

PaperVizAgent 当前这些文本 stages 都直接调用 Gemini helper，需要 Google API key 或配置正确的 Vertex ADC。仅填写任意其他服务的文本 key 不会自动切换这些 stages。图像 Visualizer 原有代码支持 Gemini image models，也支持带 `gpt-image` 名称的 OpenAI 图像路线；后者另外需要 OpenAI key。模型名来自其原生 YAML defaults 或运行参数。

AutoFigure-Edit 的 SVG 重建已有 Gemini、OpenAI Responses、OpenRouter、Bianxie 和 custom compatible 路由。最小组合可以两步共用同一 Google key；若选择其他 SVG 服务，使用其已有 provider 参数。仓库默认模型名称只是上游配置，当前账号是否可调用、具体质量与费用尚未实测。

SAM3 可以走原有 local / Roboflow / fal 路线。此机未安装 sam3 包、未有已配置的 Roboflow/fal key；安装的 PyTorch 是 2.14.1+cpu，CUDA 返回 False。API 路线不要求重新安装本地 SAM3。检测到图标后，原有第三步需要获授权的 `briaai/RMBG-2.0` 权重或 HF token；本机未有 token/cache，原生访问检查明确拒绝。没有图标时上游会走其已有纯 SVG 分支，不需要 RMBG，但不能人为伪装检测结果来绕过依赖。

AutoFigure-Edit 在纯 SVG 重建失败时还有整张 raster 包入 SVG 的 fallback。这个 fallback 不满足用户的 editable-SVG 验收；wrapper 会报错，不将它当成完成结果。

## Windows 实测结果与未完成项

- 两个独立环境都安装成功。
- PaperVizAgent 原始 CLI/config 分别暴露了上述 credential/tzset 问题；小修复后 CLI help 和配置初始化成功。
- Planner 图片载荷丢失已验证并修复；180 张实际 PNG 已进入原有 reference pool。
- AutoFigure-Edit 原始 CLI help 成功，原始 imported-figure 流程已运行至 step 1，成功将仓库示例导入为 figure.png。
- 原始 AutoFigure-Edit SVG-to-PNG helper 对一个文字/曲线技术 probe 成功，无需补新的 Windows renderer。
- 两个原生 Web 服务已作为本地隐藏进程启动并做健康检查，结果见 `audit/service_health.json`；检查结束会停止本次启动的进程。
- 自然语言 π0 acceptance 请求已准备并实际尝试；PaperVizAgent 因缺少可用 Google 凭据停止，日志为 `audit/acceptance-attempt.log`。

**尚未生成新的 acceptance raster，也没有最终 editable SVG。** Help、健康检查、示例导入和技术 probe 都不是目标图的验收。publication quality、科学标签准确性、生成图与重建 SVG 的实际视觉一致性，必须在模型凭据齐备后用真实输出判断。

## 验收案例

选用真实 π0 VLA 架构，输入仅为 `examples/request.txt` 的自然语言指令和 `examples/context.md` 的论文上下文。上下文重新核对了论文 Section IV / Appendices B/D，没有从旧 semantic graph 或图形 JSON 获取事实。

验收需要看到 PaperVizAgent 自动选择参考、完成真正图像生成，再由 AutoFigure-Edit imported-stage-1 流程输出可编辑 SVG。最后实际查看两张成图，判断它是否达到普通论文架构图的视觉水平，并核对输入、两类参数、flow 推理和动作输出。当前待模型服务与 SAM/RMBG 依赖配置，不能声称验收通过。
