# Codex 主导的科研绘图：依赖解剖与最小改造

2026-10-04：本文保留两轮实测原记录；其中历史“下一步”不再决定执行顺序。最新进度与已确认的 Diffusion Policy 178 mm canary 见 [PROGRESS.md](PROGRESS.md)，历史路线见 [HISTORY.md](HISTORY.md)。当前 canary 尚未实现。

最新状态更新：用户已确认 Stage 1 架构冻结，Stage 2 默认采用 Codex 辅助矢量重建；PaperVizAgent 与 AutoFigure-Edit 均为资产/工具来源。第二个不同图类案例已实际完成，见本文末尾“第二案例泛化验收”。下面的 π0 和完整 AutoFigure-Edit 依赖记录保留为第一轮实测，不代表当前还要修完整上游。

2026-10-03。用户目标是尽可能依靠 Codex、本地程序、成熟开源工具和现有插件/MCP。此前完整运行 PaperVizAgent 的做法被本轮要求取代。主链路的推理由当前 Codex 对话完成，生图使用已安装 imagegen 技能的内置工具。Google 凭据不是当前 Stage 1 的依赖。

## PaperVizAgent 模型依赖地图

以下基于本地固定源码 `e088a8fff74cc363b6897c0843631fff76484908`，包含此前记录的三个兼容修复；没有继续修改上游。

|功能|当前上游调用与位置|输入|输出|本轮替代方式|
|---|---|---|---|---|
|导入和客户端初始化|`utils/generation_utils.py:29–92` 导入 Google SDK；模块顶层 `google.auth.default()` → Vertex 客户端，失败才回退 Google key；还初始化 Anthropic Vertex/OpenAI|配置 YAML、环境变量、ADC|全局客户端|主入口不导入该模块；没有初始化任何模型客户端|
|参考选择|`agents/retriever_agent.py:162` 直接 `call_gemini_with_retry_async`|content、visual_intent、diagram 原生 ref.json 前 200 条文本|十个 reference ID|Codex 读取 180 条原生记录，筛选并查看图像，选择 1–3 张|
|科学理解和规划/prompt|`agents/planner_agent.py:107` 直接 Gemini；此前已修复参考图 source 字段|上下文、要求、选中图的文本和实际图像|详细 diagram description|Codex 理解上下文、确定信息和构图，写生图 prompt|
|风格|`agents/stylist_agent.py:78` 直接 Gemini|规划描述、上游风格指南|修订图像描述|Codex 使用参考的视觉规律和必要上游文本指导|
|生图|`agents/visualizer_agent.py:164–179` Gemini 或原生 OpenAI Images helper|描述、模型配置、纵横比|base64 JPEG|内置 image generation 工具；没有复用带客户端初始化副作用的 adapter|
|批评和改写|`agents/critic_agent.py:116` 直接 Gemini|原始上下文、规划、实际生成 JPEG|critique 和修订描述|Codex 查看实际 PNG，对科学连线、文字和视觉进行反馈|
|迭代编排|`utils/paperviz_processor.py` 导入所有 agents 和 eval_toolkits；`_run_critic_iterations` 再调用 Critic/Visualizer|data dict、当前图片、轮数|最终图字段与完整过程 dict|当前 Codex agent loop 决定修改和再次调用生图工具|
|可选 polish|`agents/polish_agent.py:80,166` 直接 Gemini|原图、风格指南、建议|建议/润色图片|不接入主链路；必要修改由 Codex 和内置工具完成|
|vanilla 分支|`agents/vanilla_agent.py:137–152` Gemini 或 OpenAI image helper|上下文和视觉要求|图片|不接入；主链路要求参考选择|
|benchmark evaluation|`utils/eval_toolkits.py` 导入 Google types/generation_utils，按模型名调用服务|参考图与生成图|分数和评语|不引入评估框架；本轮只检查一个真实案例|

配置面：`configs/model_config.template.yaml` 包含 defaults.model_name/image_model_name、google_cloud.project_id/location、api_keys.google_api_key/openai_api_key/anthropic_api_key 和 Anthropic region/project。generation_utils 读取 GOOGLE_CLOUD_PROJECT、GOOGLE_CLOUD_LOCATION、GOOGLE_API_KEY、OPENAI_API_KEY、ANTHROPIC_PROJECT_ID/REGION。只有改变 image_model_name，无法替换 Retriever/Planner/Stylist/Critic 中的直接 Gemini 调用。

## 工具层与模型层的边界

可直接离线使用：180 张 PNG、原生 `ref.json` 四字段、`reference_sources.json` 来源/rights/哈希，以及 `utils/image_utils.py` 中仅依赖 Pillow 的 PNG base64 → JPEG base64 转换。数据读取使用 Python 标准库即可。

适合阅读但无需抽成新包：上游 prompt 文本、风格指南、参考示例构造方式、图像检查规则。`RetrieverAgent` 内的 JSON 读取/结果解析代码和模型调用放在同一模块，导入就会连带初始化模型工具；本轮没有为了几行 JSON 读取继续拆框架。`ExpConfig` 虽不调用模型，但绑定实验目录、上游模型 defaults 和时区副作用；主链路不需要它。

不应作为纯工具导入：generation_utils、所有 model agents、paperviz_processor、eval_toolkits。即使 do_eval=False，processor 模块依然导入评估工具。通过避免这些导入，主路径可以在阻止 Google/OpenAI/Anthropic SDK 导入的情况下读取参考库和准备文件。

保留两个原有独立环境。`run.py` 只负责输入、原生参考记录读取、产物导入、可编辑结构检查和调用 AutoFigure-Edit。旧 wrapper 保存在 `audit/run-google-legacy.py` 供追溯，不是当前入口。没有新的模型服务、agent 框架、向量库、布局引擎、模板语言或 renderer。

## Codex 最小实验

使用已有 `examples/request.txt` 和 `examples/context.md` 的真实 π0 模型/推理任务。参考由 Codex 根据文本和图像选定：DB232 的简洁 VLA 组织方式；DB223 的多模态 token strip 和科学配色。DB223 的 memory bank、门控和 diffusion 模块不进入目标图。DB021 也经过查看，其流场科学图不适合本次紧凑架构构图，未送入生图工具。

科学 authority 是用户提供的 context 和重新打开的 [π0 原文](https://arxiv.org/html/2410.24164v1)，不是参考图。保持图像/文本在预训练 backbone 一侧、状态/动作在 action-expert 参数一侧，以及观测条件、连续 action chunk 和 Euler 推理方向。阶段一实际调用及图像检查记录随产物保留。

## Stage 2 的真实依赖

AutoFigure-Edit 的 imported-figure 支持跳过生图，但不会跳过 SAM3、需要时的 RMBG 和 SVG 模型调用。本机环境只有无关服务的 key，不把它们用于本项目。其全量重建模型服务和 SAM API 尚未配置，本地 SAM3 包也不可用。RMBG 权重的访问限制延续此前报告；本轮没有申请访问、下载权重或配置凭据。

`run.py --stage svg` 默认 openai_response，Google 只作为显式可选上游 provider 存在。缺少服务时会明确报 Stage 2 未就绪，而非要求为了 Stage 1 配置 Google。`--stage finalize` 是独立的 Codex 辅助重建路线：Codex 从实际 PNG 编写本案例 SVG，复用 AutoFigure-Edit 的 `validate_svg_syntax`、`replace_icons_in_svg` 和 `svg_to_png` 本地函数。局部裁片由 Codex 查看图像后确定范围，保留原背景，未使用 SAM/RMBG。兼容上游的参数名 `nobg_path` 不表示做了去背景，裁片记录已明确 `background_removed: false`。该路线不会伪造 SAM 检测或声称运行了完整上游管线。

所有 SVG 都必须含实际可编辑文字和矢量；整张 raster 包入 SVG、或再添加几个假文字/图形，不算通过。代码的结构检查只是筛查，不能替代实际查看渲染和核对科学内容。Illustrator/Inkscape 可编辑性需要实际导入确认；不能把 SVG 结构存在等同于已测试 PowerPoint 的文字编辑支持。

## 实际验收记录

Stage 1 实际完成：一个内置生图调用和两个针对科学连线/嵌入表达的编辑调用，生成三个 2078 × 757 PNG。前两稿分别存在状态连入 backbone、噪声动作接入状态端等问题；Codex 目视发现后修正。再次查看原文附录 B 时确认 action/time MLP 的抽象表达比加法 junction 准确，因此第三稿采用同一个 MLP 接收 noisy actions 和 flow time，输出连接至 noisy action tokens。第三稿作为 `outputs/codex-pi0/figure.png` 保存。实际 prompt 见同目录 `image-generation-call.txt`、`image-edit-1.txt`、`image-edit-2.txt`，扩展规划 brief 为 `image-prompt.txt`。

SVG 辅助重建实际完成：Codex 对照第三稿写入一次性 `reconstruction.svg`。核心文字、模型区域、token/matrix glyph 和连接保持为 SVG text/shape/use；三个相机/机器人场景裁片经原有 replace_icons_in_svg 函数组装为独立 image。全图 raster 没有嵌入。初版 Cairo 渲染暴露 tspan baseline-shift 和 text-anchor 的数学排版问题；本案例改用明确定位的可编辑数学字符，并修正速度公式裁切和状态连线与标签的接触。第三版渲染经过查看，交付为 `figure.svg` 和 `svg-preview.png`。矩阵纹理经过简化，字体与 PNG 略有差异；没有声称像素级一致。

可编辑结构：107 个 text、30 个 path、25 个 rect、1 个 line、34 个 use 和3 个 image（包含 defs 中的形状定义计数，不等同于 90 个独立组件）。裁片覆盖约 5.5% 画布面积。实际将副本中的 “Action expert” 改为 “Edit probe”，将区域 fill 改为绿色，使用同一上游 renderer 重渲染；变化范围位于 action-expert 区域，交付原件保持不变。见 `audit/codex-svg-edit-probe.json` 与 `codex-svg-edit-probe-v2.svg/png`。首次 probe 的 XML encoding alias 导致 Cairo 解析失败，改为规范 `utf-8` 后通过；失败文件留作审计，不是交付物。

离线工具检查：禁止 Google/OpenAI/Anthropic SDK 导入后，180 条记录/实际图片读取、输入准备、已有 image_utils 转换均成功；纯 raster SVG 和 raster 加 dummy 文字/图形均被拒绝，独立局部图片加文字矢量被接受。证据为 `audit/codex-native-checks.json`。这些检查只验证工具行为，不认证视觉质量。

完整上游重建尝试：`run.py --stage svg --raster outputs/codex-pi0-draft2/figure.png --out outputs/codex-pi0-full-afe` 以非零状态停止，明确指出 openai_response SVG model service 和 SAM3 Roboflow service 未配置。没有初始化/请求模型服务，没有把失败的全量路线记作通过。已有本地 SAM3/RMBG 限制也未被解决。

本轮证明了没有 Google 凭据也可完成 Codex 主导的 Stage 1，并产出具有实际文字/矢量编辑价值的辅助重建 SVG。PNG 和 SVG 是论文候选图；科学信息已对照上下文/原文检查，但正常论文印刷尺寸下的可读性与最终投稿视觉标准仍需判断。本轮没有完整 AutoFigure-Edit 自动重建、跨案例泛化或原生设计软件编辑验收。下一步应围绕这一张实际候选图改进或确定 Stage 2 的服务/本地依赖，不恢复 Google 作为默认 Stage 1 blocker。

## 第二案例泛化验收

按用户最新要求，只选 scaled dot-product Transformer self-attention 作为第二例，未做 Dreamer/U-Net 多案例并行，也未新增绘图脚本。最新产品定义为 Codex-native scientific figure generation + Codex-assisted vector reconstruction，输入/输出文件约定见 STAGE2-CONTRACT.md；Stage 1 的职责和数据流冻结，见 STAGE1-FREEZE.md。

原始输入保存为 examples/attention/request.txt/context.md，主科学来源为重新打开核对的 [Attention Is All You Need Section 3.2.1](https://arxiv.org/html/1706.03762v7)。本例是单个无 mask 的 head，展示投影、scores、row-wise softmax、attention map 和 values 的加权组合。四位置权重 [0.10, 0.20, 0.60, 0.10] 是明确标记的 illustrative example，不是实测 attention。

Codex 在现有 180 图的原生库中浏览 metadata，查看 DB111、DB244、DB103，选取前两张后提炼运算标注、score/value 路径分离和矩阵层次的视觉原则。没有把参考图字节传入工具，避免整张原始架构图约束目标构图。imagegen 实际单次生成 1536 × 1024 PNG，经查看后科学公式和连线无需再次生成；source prompt 与选图方式记录在 outputs/codex-attention/generation-prompt.txt 和 reference-use.md。

Codex 随后对照 PNG 与原始上下文写入一次性 reconstruction.svg。相同 run.py finalize 入口保存/检查/渲染，得到核心三文件 figure.svg、svg-preview.png 和 editability-check.json。190 text、25 path、50 rect、3 line、1 circle、6 use、0 image（包括 defs/marker，不能等同于同数量独立组件）。这是全矢量输出，没有图像包裹，也未使用上一例机器人裁片逻辑。

通用 Stage 2 功能仅增加输入文件检查、调用已安装 CairoSVG/Pillow、保存结构结果和实际文字/有色矢量编辑 probe。没有图类条件、模型调用、统一布局或 renderer 算法。自动工具只标记结构与 probe 结果，科学/视觉保持 pending 直到 Codex 查看实际 PNG/预览。最终查看修正了标题/公式间距，并补记该范围内的复核结论。

在现有渲染环境中，禁止导入 google、openai、anthropic 和 autofigure2，默认 finalize 仍成功；见 audit/attention-stage2-independent.json。第一次直接在 PaperVizAgent 环境调用 finalize 缺少 CairoSVG，未通过；改用正常 CLI 选择的既有环境后成功。渲染环境物理位于 AutoFigure-Edit/.venv，这不是模型/Agent 依赖。本轮没有安装新包、修 SAM/RMBG 或配置 key。

文字与矢量分别在独立副本中编辑和重渲染，实际差异区域分别位于顶部公式和输入 token：text bbox [467,31,830,73]，vector bbox [59,344,126,398]。交付原件不变。core editability-check.json 记录了完整证据、实际所用工具和未进行的原生编辑器/投稿尺寸验收。

π0 最终 figure.png、figure.svg、svg-preview.png 的 SHA-256 和原 provenance 一致，audit/second-case-freeze-check.json 记录全部为 true。主控与 Stage 1 的 prepare/reference 代码未改变，离线 SDK 禁止导入检查仍通过。第二案例运行逻辑没有专用绘图脚本或新框架；本案例 SVG、prompt/context 和审计文件是普通交付素材。

当前可支持的结论：同一 Codex 主导链路已从含局部 raster 的 π0 架构图迁移到全矢量 attention 矩阵图，完成第二图类最小泛化验收。尚未证明任意复杂图的稳定自动化、印刷栏宽与最终投稿级视觉，也没有原生 Illustrator/Inkscape/PowerPoint 编辑测试。完整 AutoFigure-Edit 自动流程不再是下一轮必要目标。
