# FigureCompose

2026-10-04 统一交接：最新状态、Diffusion Policy 178 mm Stage 2 canary 和执行顺序以 [PROGRESS.md](PROGRESS.md) 为准；路线演变见 [HISTORY.md](HISTORY.md)。本页保留运行说明，旧实现与完成阶段实验见 [日期归档](../archive/2026-10-04/README.md)。Diffusion Policy 当前 canary 已本地四门通过，见 [acceptance](outputs/diffusion-policy-stage2/acceptance.md)；FAST / DreamerV3 尚无 Stage 2 成品。

当前产品定义：**Codex-native scientific figure generation + Codex-assisted vector reconstruction**。

用户只输入自然语言，可附方法段、科学上下文、数据或参考图。Codex 在当前对话中理解任务、自动选参考、独立构图、编写生图 prompt、查看并修订实际图片，再对照 PNG 和原始上下文重建 SVG。本地代码只负责文件、检查和调用现成工具。

`自然语言/上下文 → Codex + reference bank → 内置生图工具 → figure.png → Codex 辅助矢量重建 → figure.svg`

## 已完成的两类 prototype / pre-canary 案例

|案例|实际结果|重建工具与限制|
|---|---|---|
|[π0 架构图](outputs/codex-pi0/acceptance.md)|真实生图及两轮科学修正；可编辑 SVG 保留三个独立场景裁片|复用 AutoFigure-Edit 本地工具；未跑完整 SAM/RMBG/API；独立构图与最终投稿标准未通过完整验收|
|[Transformer attention 矩阵机制图](outputs/codex-attention/acceptance.md)|真实生图；全矢量 SVG，无 raster；文字和矢量分开修改并重渲染验证|通用 run.py + stdlib XML/CairoSVG/Pillow，禁止导入模型 SDK 和 autofigure2 仍成功；没有新增专用绘图脚本|

第二案例的实际输出为 `outputs/codex-attention/figure.png`、`figure.svg`、`svg-preview.png`、`editability-check.json`。参考图经 Codex 查看后提炼为文字原则，没有把整图作为图像条件传入。参考使用记录为 `reference-use.md`，实际 prompt 为 `generation-prompt.txt`。

两例仅为 Stage 2 prototype evidence / pre-canary。当前 Diffusion Policy 是 Current Stage 2 contract canary，178 mm 真实尺寸、caption migration、semantic lock 与四门验收须联合通过。当前 canary 文件名与尺寸渲染规则见 [STAGE2-CONTRACT.md](STAGE2-CONTRACT.md)；不使用 `reconstruction.svg` / `figure.svg` 双名，也不沿用历史预览别名。

这支持从一个案例向另一类科研图迁移的最小结论。实际出版尺寸可读性、最终投稿视觉标准和原生设计软件编辑仍分别需要验证。两类案例成功不代表任意方法图都能稳定全自动重建。

## 冻结的 Stage 1

后续用户授权的三个 Zotero 文字生图测试见 [三案例报告](outputs/zotero-three-cases/REPORT.md) 和 [原图/各稿对照页](outputs/zotero-three-cases/comparison.html)。每例一次生成和两轮编辑；Diffusion Policy 在限定核心机制范围内完成复核，FAST 数值一致性和 DreamerV3 关系仍未通过。本批次仅测试 PNG，没有执行 Stage 2，不纳入上表的完整可编辑案例。

职责和链路见 [STAGE1-FREEZE.md](STAGE1-FREEZE.md)。Codex 主控、reference bank 和内置 imagegen 保持原有边界，不改 PaperVizAgent 的 Gemini agents，不新造 planner、semantic graph 或 layout engine，不配置 Google 服务。

PaperVizAgent 保留为参考资产、文本指导和可复用本地工具来源。参考的选择与使用方式应适应每个任务：提炼层次、密度、配色和运算标注后独立构图，记录是否传入原图字节。不能把原始科学图默认作为构图底稿。科学 facts 来自用户内容和论文，而非视觉参考。

π0 已交付 PNG/SVG/preview 哈希在第二案例结束后再次核对一致，产物没有被修改。

## 默认 Stage 2

[STAGE2-CONTRACT.md](STAGE2-CONTRACT.md) 是极薄文件约定：输入为实际 figure.png、原始 request/context、generation-prompt.txt 和 selected-references.json；输出为 figure.svg、svg-preview.png、editability-check.json。Codex 自己决定一次性 SVG 如何重建，不要求用户提供模板或图谱。

默认工具是已安装的标准 XML/SVG 检查、CairoSVG 和 Pillow。AutoFigure-Edit 是可选工具箱，当前不把修通其完整流程作为工程优先级。独立图片组装可按需调用其 helper；完整 API/SAM/RMBG 路线保留为显式可选 stage，不是默认重建入口。

editability-check.json 同时保存真实元素结构和文字/矢量的两个独立编辑 probe。科学和视觉复核初始标为待检查，必须由 Codex 查看实际 PNG/渲染后补记。结构计数、XML 成功或像素发生变化都不能单独认证科学正确或发表质量。整图 raster 包进 SVG不算通过。

## 本地工具命令

run.py 是极薄文件工具。它不会从普通 Python 进程自动调用当前 Codex 的推理或内置生图工具。用户在对话里提供自然语言后，Codex 使用以下内部命令准备文件，并接续完成选参考、生图和重建。

```powershell
python -X utf8 run.py --request-file examples/attention/request.txt --context examples/attention/context.md --out outputs/new-case
```

Codex 可用 `--stage references` 查看原生库；`--query` 是字面筛选，不是语义排序。`--reference` 是 Codex 内部记录选图的参数，用户不必提供 reference ID。

内置工具生成后保存实际 PNG。`--stage raster` 只调用 Pillow 保存文件，不做生图或模型初始化：

```powershell
python -X utf8 run.py --stage raster --raster <实际生成图路径> --out outputs/new-case
```

Codex 从 PNG 和保存的上下文写出一次性 SVG 后，调用通用 Stage 2。内部 `--template` 表示已有 SVG 源文件，未引入模板系统；输入与输出目录可分开以保留修订：

```powershell
python -X utf8 run.py --stage finalize --template outputs/new-case/reconstruction.svg --inputs outputs/new-case --out outputs/new-case/revision1
python -X utf8 run.py --stage check --template outputs/new-case/revision1/figure.svg
```

默认重建不导入 autofigure2 或任何模型 SDK。本机使用已安装 CairoSVG/Pillow 的现有隔离环境；正常 CLI 在当前 Python 缺少 renderer 时选择既有环境，没有安装新依赖。该环境物理位于 AutoFigure-Edit/.venv，不表示执行了上游 Agent 或要求其服务凭据。

如任务需要独立裁片，可显式使用 `--icon-crops` 复用原上游组装 helper；裁片必须注明 Codex 选定、是否保留背景，不伪装 SAM 输出。`--stage svg` 保留完整上游 optional route，只有已有相应服务且任务需要时才使用，不作为下一步必修项。

## 开发边界与审计

只做了一个第二案例，没有 Dreamer/U-Net 扩展或模板库，没有模型服务框架、semantic graph、layout/routing/resolver、renderer 或评估框架。运行改动集中在 run.py 的通用 Stage 2 文件/检查功能。手写的案例 SVG 是交付源文件，不是专用绘图脚本。

最新指令在 AGENTS.md。依赖地图与两轮记录在 [CODEX-NATIVE-REPORT.md](CODEX-NATIVE-REPORT.md)，详细第二案例判断在 [acceptance.md](outputs/codex-attention/acceptance.md)。UPSTREAM-REPORT.md 是旧完整接入的历史记录；旧 Google blocker 不代表当前路线。LocalFigure 保持 legacy，未接入其引擎。
