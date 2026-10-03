# Stage 1 架构冻结

2026-10-03 用户确认：Stage 1 已基本证明可行，当前主要工程问题转到 Stage 2 和第二案例泛化。

冻结的是职责与链路：自然语言及可选上下文 → 当前 Codex 理解和规划 → 读取参考库、选择并查看参考 → 内置 imagegen 工具 → 实际 PNG → 科学与视觉检查。Codex 保持主控。PaperVizAgent 的 Gemini agents 不进入主链路；本地程序只做资产和文件工具。

本次不改 Retriever/Planner/Stylist/Critic、不新造 planner/graph/layout engine、不配置 Google 服务。参考使用方式和每张图的构图可根据任务调整，这不构成新增编排架构。第二案例采用文字提炼参考的方式，记录其来源与实际使用方式。

π0 的 request/context、最终 PNG/SVG/preview 和现有审计均保留；其 SHA-256 见 `outputs/codex-pi0/provenance.json`，第二案例结束再核对。架构冻结不表示第一稿已达到投稿级、已通过独立构图验收或已验证真实印刷栏宽。
