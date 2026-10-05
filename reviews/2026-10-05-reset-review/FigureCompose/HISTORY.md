# 科研绘图工作历史

整理日期：2026-10-04。依据实际本地报告、产物、上传记录及相关聊天的公开消息片段重建。日期按用户时区 Asia/Shanghai；本记录不声称覆盖全部聊天或账户历史。

## 2026-10-02：LocalFigure 原型、数据接入与冻结

早期工作形成框架、PoC、0.3 和 π0 vertical slice，链路包含 semantic graph、plan、ELK/resolver/routing 和 SVG/PPTX。它验证了案例级科学关系、确定性重建与原生编辑对象，未证明通用自然语言绘图或投稿视觉质量。

π0 slice 的 closeout 保留两种相机变体、两种 profile、外部数据接入与 A/B/C 对照。53 项检查、174 文件冻结清单是当轮证据。85 mm 图高 236.52 mm、长绕线、端口泛化与范围识别问题进入 backlog；用户要求停止继续扩展。旧项目随后迁入 LocalFigure，迁移记录原样保存。

视觉增量轮下载 180 张 DiagramBank 图，17 张细读，建立八条 design grammar，接入 MathJax 和局部照片；595 项检查与20项自然语言入口检查记录为通过。仍仅覆盖受限 π0 adapter，主布局没有充分吸收视觉观察。素材和数学排版改善不等于构图与投稿能力完成。

证据：[旧交接](../archive/2026-10-04/LocalFigure/HANDOFF.md)、[π0 closeout](../archive/2026-10-04/LocalFigure/outputs/localfigure-pi-slice/CLOSEOUT.md)、[视觉轮记录](../archive/2026-10-04/LocalFigure/outputs/localfigure-visual/README.md)。

## 2026-10-02：停止旧架构，建立 FigureCompose

用户明确将 LocalFigure 归为 legacy，停止开发及保留性重构，只复用有价值的素材。新目录最初组合完整 PaperVizAgent 与 AutoFigure-Edit。

上游固定源码、独立环境和三处 Windows/载荷兼容修改得到实测；完整路线未得到真实目标成图，受 Gemini/ADC、SAM/RMBG/SVG 服务依赖限制。当时 Google blocker 是历史实现状态，不能套用到当前产品。

证据：[UPSTREAM-REPORT.md](UPSTREAM-REPORT.md)、audit/ 中原始帮助、兼容、服务和访问日志。上游源码与环境仍保留原位。

## 2026-10-02 至 10-03：成熟工具和替代路线验证

工具盘点与 Canva、diagrams.net、FigJam 试用留下原生成图、导出和编辑记录。导出能力、调用工具可用性与论文视觉质量分开判断；这些试验不是当前主路线的必需依赖。

方法研究验证 draw.io CLI、数学、可编辑 XML 往返、PDF 提图和 CLIP/FAISS 检索的局限。draw.io 的 foreignObject/fallback 与通用 SVG 字符级编辑能力不同，portable-labels 数学破坏的失败也保留。

FigurePilot 随后独立执行 π0、MemoryVLA、DreamerV3 原生 .drawio author 和局部编辑。三例完成，MemoryVLA 视觉最好；另两例容量、密度和留白仍需改善。它验证 agent + 原生编辑格式的案例能力，没有生成通用布局器，也没有替代 FigureCompose 的最新路线。该路线与后来的 PNG 案例具有不同输入与验收，DreamerV3 两路线的结果不能混合。

证据：[工具审计](../archive/2026-10-04/LocalFigure/SCIENTIFIC-FIGURE-TOOL-AUDIT.md)、[方法研究](../archive/2026-10-04/FigureMethodResearch-2026-10-03/REPORT.md)、[FigurePilot RESULTS](../archive/2026-10-04/FigurePilot/RESULTS.md)。

## 2026-10-03：Codex 成为主控，完成 π0

用户取代完整 Gemini 编排：Codex 承担科学理解、选参考、构图、prompt、critique，内置 imagegen 生成 PNG。主路径避免导入模型初始化模块，不要求 Google 凭据或独立 API key。

π0 一次生成、两轮科学修订后得到真实 PNG；Codex 辅助重建 SVG，复用 AutoFigure-Edit 本地 helper，核心文字与矢量可编辑，保留三个独立 scene crops。完整 SAM/RMBG/API 路线未运行成功，未伪造检测输出。参考 DB232/DB223 图像字节实际送入生图；参考构图独立性与投稿质量未完整验收。

证据：[CODEX-NATIVE-REPORT.md](CODEX-NATIVE-REPORT.md)、[π0 验收](outputs/codex-pi0/acceptance.md)、audit/ 中离线检查和编辑 probe。已有第一轮失败 probe 保留。

## 2026-10-03：冻结 Stage 1，完成 attention 第二案例

用户明确将两个上游降为可选资产/工具来源，要求冻结 Stage 1，Stage 2 使用极薄文件约定，并只做一个不同图类的第二案例。选定 scaled dot-product self-attention。

单次 imagegen 生成，Codex 查看 PNG 后全矢量重建；默认 finalize 在禁止导入模型 SDK 与 autofigure2 时成功。190 text、0 image，文字与矢量分别编辑并重渲染；旧 π0 核心哈希保持。参考图只提炼文字原则，没有图像条件。最小跨图类迁移得到证据；真实投稿尺寸和原生编辑软件测试仍未完成。

证据：[STAGE1-FREEZE.md](STAGE1-FREEZE.md)、[STAGE2-CONTRACT.md](STAGE2-CONTRACT.md)、[attention 验收](outputs/codex-attention/acceptance.md)。

## 2026-10-03：Zotero 三案例与公开审阅包

用户授权选几篇未用于当前完成案例的论文，从方法文字生图并与原图比较。FAST、Diffusion Policy、DreamerV3 各一次生成、两轮修订，总计九次调用。目标原图在生成之后查看，原文提取含图注的可能性已披露；生成与初评同一 Codex，非独立盲评。

Diffusion Policy 在限定核心机制范围内通过，FAST 精确序列缺项，DreamerV3 关系仍错。全部只完成 Stage 1 PNG，没有新的 SVG。图形表征丰富，但教学 prose、面板色块和反馈视觉权重较大，原图一般更紧凑。

用户授权上传 image3 审阅仓库，main 提交为 2b668ef0159373771afe1a15a73041b27f7eb564；记录60文件校验和约13.9 MiB ZIP。公开包去掉本机路径，原始本地 source 不改写。ZIP SHA-256 为 1eae2906f20dd016ee0b8b24ed1ad03e56f13491944b3bc43dd5607ebb468393。本次整理依据本地上传记录与保留的 Git checkout，没有重新联网核验。

证据：[三案例报告](outputs/zotero-three-cases/REPORT.md)、[比较页](outputs/zotero-three-cases/comparison.html)、[上传记录](outputs/zotero-three-cases/github-upload.json)。发布 checkout 在归档 FigureCompose-review-publish/image3；远端是历史审阅快照，不自动代表本次整理后的最新状态。

## 2026-10-04：独立路线图与尺寸要求

用户提交日期署为 2026-10-03 的独立审阅报告，要求读完理解后实际操作。路线图判断 Stage 1 视觉表征已可行，硬数值和拓扑可靠性仍不足；停止重复探索新框架和无限 image edit。

近期顺序收敛为：论文图优先 prompt、caption migration、普通文本 semantic lock、Diffusion Policy Stage 2 canary、真实物理尺寸和四门验收；通过后再处理 FAST、DreamerV3。Stage 2 目标是科学可编辑性与构图保留，避免全图 tracing 和框箭头退化。

用户确认178 mm主目标、85 mm仅压力测试；必须按物理字号/线宽重新排版，不仅等比例缩 PNG。上一聊天在资料阅读和尺寸确认后中断，没有 canary 成品。

证据：[路线图原件](docs/sources/stage1-independent-review-2026-10-03.original.txt)、[尺寸确认](docs/sources/diffusion-policy-width-confirmation-2026-10-04.md)、[公开消息摘录](docs/sources/conversation-excerpts-2026-10-04.json)。

## 2026-10-04：本次本地交接与清理

按用户要求建立 PROGRESS.md 统一进度、本文历史记录和本地原始指令副本。LocalFigure 旧实现、FigurePilot、方法研究、发布副本和根级 Python cache 移入日期归档，不删除证据。FigureCompose 源码、参考库、隔离环境、案例和审计保持位置。

归档保留文件 SHA-256、前后核对、旧文档快照和显式恢复脚本。冻结基线内容不改写；历史文档中的旧绝对路径保留，目录迁移由映射清单解释。当前入口文档指向统一进度，后续不再从旧报告推断开发优先级。

本次没有实施 Diffusion Policy SVG、生成新图、修完整上游、重新发布审阅包，也未把失败案例标为通过。最新下一步和验收状态以 [PROGRESS.md](PROGRESS.md) 为准。
