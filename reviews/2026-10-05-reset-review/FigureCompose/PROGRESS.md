# FigureCompose 统一进度与交接

更新：2026-10-05（Asia/Shanghai）。本文件是当前进度和执行顺序的唯一更新入口；历史报告保留当时结论，不能据旧报告恢复已停止路线。操作边界仍受 AGENTS.md 约束。

当前执行状态：2026-10-05 用户在全局 reset review 后明确授权的有限实验已完成：Diffusion Policy 独立子代理复审、项目新案例 MAE 的固定预算验证、同一 brief 的 imagegen→editable SVG 与直接 editable SVG 对照。两名 fresh-context 作者与一名独立审阅子代理完成工作，规则见 [PROTOCOL](outputs/reset-validation-2026-10-05/PROTOCOL.md)，结果见 [RESULTS](outputs/reset-validation-2026-10-05/RESULTS.md)。本批次结束，没有根据审阅结果追加修图或启动生产开发。

本次新证据：Diffusion Policy 成品在限定来源范围的科学复审通过，Ta=4→3 副本修改与 Inkscape CLI 视觉导出通过，但设计关联和纸面可读性仍为 PARTIAL/PENDING，未复验旧 gate D。MAE 两条路线的最终 CairoSVG 预览科学关系与 75%→50% 语义副本通过，均有有效空间图像表达；原始 imagegen PNG 科学 FAIL。两个 MAE SVG 在 Inkscape 直接导出和另存导出均出现裁片溢出，实验交付状态均为 REVISE，不进入 accepted artifacts。冻结后原图审计未发现参考素材或非必要布局照搬，不等于绝对原创证明；本次仍为同模型、单案例、准备好科学输入包的测试。细项见 [独立 paired review](outputs/reset-validation-2026-10-05/final-review/REVIEW.md)。

保全检查：此前 163 个输出文件零变更、零缺失；共同输入哈希未变。没有安装依赖、新增绘图脚本、修改生产代码或 Stage 1/2 contract。当前新候选的兼容性修复、更多案例和人类纸面验证均尚未执行，不据下方历史执行表顺手启动其他任务。

此前暂停记录继续保留。已有 accepted artifacts 不改，用户对 canary 的核验仍未记录，不将旧 ACCEPTED 当作用户确认；FAST / DreamerV3 精修、生产约定和框架开发不在本次恢复范围。原暂停留档入口：[本次工作与暂停记录](outputs/diffusion-policy-stage2/review/pause-2026-10-05.md)；文件校验清单：[pause-manifest](outputs/diffusion-policy-stage2/review/pause-manifest-2026-10-05.json)。当前用户授权优先于 AGENTS.md 开头保留的旧暂停说明。

## 当前产品与阶段

自然语言科研绘图要求及可选科学上下文 → Codex 理解、自动选参考、独立构图和 prompt → 内置 imagegen 生成真实 PNG → 查看与有限修订 → Codex 对照 PNG 和原始上下文重建可编辑 SVG → 成熟 XML/SVG 工具检查和渲染 → 科学与视觉验收。

Stage 1 架构已验证并冻结。prompt 与图内信息量可以调整，默认向论文 method figure 收敛。PaperVizAgent 是参考资产与文本指导来源；AutoFigure-Edit 是可选工具箱。Google 凭据、完整 Gemini 编排、SAM/RMBG 服务均不是默认主链路前提。

π0 与 attention 是 Stage 2 prototype evidence / pre-canary：证明曾完成可编辑 SVG 的最小闭环，不证明当前 Stage 2 contract 已通过。Diffusion Policy 是 Current Stage 2 contract canary，已首次联合验证 178 mm 真实尺寸、caption migration、semantic lock 与四门验收，本地结果为 ACCEPTED（A/B/C/D 全 PASS）。验收由同一 Codex 制作和复核，不是独立审阅或投稿认证；85 mm 完整细节阅读受限。精确文字、数值、计数、矩阵、时间线与关键关系由可编辑元素实现，并逐项核对。SVG 结构检查只能筛查，不能保证科学正确。局部 illustration 可为 raster，整张 PNG 包入 SVG 不通过。

run.py 是文件、结构检查和现成渲染工具的薄入口，不会从普通 Python 进程调用当前 Codex 推理或内置 imagegen；prepare、raster 不是生图步骤。

## 已完成与未通过

|案例或阶段|真实完成内容|状态及边界|本地证据|
|---|---|---|---|
|π0|生成及两次修订；PNG、SVG、预览；107 text 与三个局部图片；实际编辑 probe|Stage 2 prototype evidence / pre-canary；单图最小闭环完成；独立构图、原生编辑器和投稿尺寸未完整验收|[acceptance](outputs/codex-pi0/acceptance.md)|
|Transformer attention|单次生成；全矢量 SVG；190 text、0 image；文字和矢量独立编辑 probe|Stage 2 prototype evidence / pre-canary；第二图类最小迁移完成；投稿验收未完成，不证明当前 contract 通过|[acceptance](outputs/codex-attention/acceptance.md)|
|FAST|Stage 1 初稿与两次修订、论文原图对照|数值一致性未通过：顶部展开列仍缺一个零；没有 Stage 2|[evaluation](outputs/zotero-three-cases/fast/evaluation.json)|
|Diffusion Policy Stage 1|初稿与两次修订、原图对照|历史 PNG 测试：核心机制通过目视复核，不是原 Figure 2 的完整替代；本行不包含后续 Stage 2|[evaluation](outputs/zotero-three-cases/diffusion-policy/evaluation.json)|
|Diffusion Policy Stage 2|178 × 117 mm 全矢量 SVG、两尺寸 300 dpi 预览、caption、semantic lock、四类实际编辑 probe 与逐项科学/视觉复核|Current Stage 2 contract canary：本地 ACCEPTED，A/B/C/D 全 PASS；85 mm 细节阅读受限；同一 Codex 审阅，原生设计软件导入、独立复审与纸面打样未执行|[acceptance](outputs/diffusion-policy-stage2/acceptance.md)|
|DreamerV3|Stage 1 初稿与两次修订、原图对照|科学关系未通过：prior 条件线、在线观测反馈及 critic 时间覆盖仍有问题；没有 Stage 2|[evaluation](outputs/zotero-three-cases/dreamerv3/evaluation.json)|
|三案例审阅包|九张生成稿、三张原图裁片、prompt、来源、评估和 ZIP 已上传|上传记录：main，提交 2b668ef0159373771afe1a15a73041b27f7eb564，60 文件；本轮未重新上传或在线复核|[github-upload.json](outputs/zotero-three-cases/github-upload.json)|

元素计数包含 defs/marker，不等于同数量的独立科学组件。三案例为有意选样，生成与初评由同一 Codex 完成；目标原图在生成修订之后查看，但方法提取可能含图注，不称为完全盲测，也不计算总体成功率。figure.png 是最后一稿文件名，不能据此认定通过。

现有完整案例保持原字节；失败、草稿、prompt、source、provenance、原文提取和审计均保留。三案例详细判断见 [REPORT](outputs/zotero-three-cases/REPORT.md)。

## 最近一次工作停在哪里

目录整理时，Diffusion Policy Stage 2 尚未产出。用户随后要求消除四处约定歧义，并限定本轮完成该 canary。2026-10-04 已在 outputs/diffusion-policy-stage2/ 完成真实重建、caption migration、semantic lock、178/85 mm 同源渲染和四门本地验收；当前停在这张成品，没有顺手启动 FAST 或 DreamerV3。

2026-10-05 已记录本次产物、验收方式、限制和完整文件哈希，随后按用户要求暂停等待核验。本次留档只核对已有文件和记录，不重做科学或视觉验收，不改成品内容。恢复时先读取本文件及 pause-2026-10-05.md，再按用户核验意见决定修订或后续工作。

本次成图不改 Stage 1、不写归档、不新增绘图脚本或框架；仅交接说明消歧与状态回写在交付目录之外。科学检查从最终 SVG 的节点、边、数值和计数重新开始，没有继承 PNG 的通过标记。验收方式与未验证项见成品 acceptance.md。

## 唯一近期执行顺序

|优先级|任务|目前状态|完成条件|
|---|---|---|---|
|P0|冻结 Stage 1 主链路；减少教学 poster 风格和图内 prose|架构冻结已完成；新 prompt policy 尚未实际验证|论文图优先，不新增 planner/layout 框架|
|P0|Diffusion Policy：Current Stage 2 contract canary|产物已完成；本地 ACCEPTED，四门全 PASS；现暂停等待用户核验|成品与证据均在 outputs/diffusion-policy-stage2；85 mm 限制另记；用户核验不等同于本地自评|
|P1|FAST 数值/矩阵/计数精修|尚未启动；暂停期间不推进，等待用户核验及恢复指令|完整八项展开序列一致、精确元素可编辑|
|P1|DreamerV3 关系精修|尚未启动；暂停期间不推进，顺序仍在 FAST 之后|prior、actor/action、RSSM、真实在线反馈及 value/returns 关系逐项通过|
|P1|据三案例证据收敛 Stage 2 contract|等待上述验证|保留薄文件约定，不引入 DSL 或科学绘图引擎|
|P2|更多图类或领域、自动化与检索扩展|未启动|只有上述验收完成后再考虑|

### Diffusion Policy 已确认要求

主目标是 178 mm 双栏宽。SVG 的字体、线宽、箭头和间距按真实物理尺寸设置，不能仅将现有 1536×1024 PNG 等比例映射为 178 mm。

SVG 根元素必须为 width="178mm"，高度由构图决定，viewBox 与版面匹配。178 mm PNG 预览固定按 300 dpi 渲染（宽度 round(178 / 25.4 × 300) = 2102 px），记录实际像素尺寸并写入 300 dpi 元数据；物理尺寸检查按此比例认定，不能凭屏幕显示大小判断。

85 mm 仅作 readability stress test：同一 SVG 固定按 300 dpi 缩放渲染（宽度 round(85 / 25.4 × 300) = 1004 px），不改变布局、文字或内容。检查最小字体、箭头头部、horizon bracket、时间线和关键标签的可辨认性。记录限制即可，不要求完整保留细节，不为压力测试重新设计整图或大幅压缩内容。主验收仍是 178 mm。

保留观测/条件、动作迭代去噪和滚动执行的视觉结构。压缩图内 prose，解释、范围和 illustrative caveat 移入 caption；原科学含义和示意边界仍须明确。40–60% prose 减少来自审阅建议，是参考范围，不是已经测得的改善。

最小 lock list 使用普通文本：To=2、Tp=8、Ta=4 是示意；观测到 condition、condition 到 denoiser、action noise 到 denoiser、执行到 environment、新观测到下一次 policy query；区分扩散索引 k 与机器人时间 t，固定去噪方向。8 个预测动作与 4 个执行动作必须一致，反馈不能接成未来图像预测。CNN+FiLM 与 Transformer+cross-attention 是并列替代方案，不能串联。

重建文字、数字、timeline、bracket 和关键箭头，允许独立局部 illustration。保留颜色层次、panel 和有意义的视觉表征，不能退回只剩框箭头，也不追求全图 tracing 或像素一致。

本 canary 使用唯一文件名，不使用 reconstruction.svg、template.svg 或 svg-preview.png 别名：

```text
outputs/diffusion-policy-stage2/
  figure.svg
  preview-178mm.png
  preview-85mm.png
  editability-check.json
  semantic-lock.txt
  caption.md
  acceptance.md
```

figure.svg 同时是可编辑源文件与最终 SVG；预览均由它渲染。必要的 probe 与核对证据也只保存在此目录。原 Stage 1 输入只读引用，原 PNG 保持不变。这些是普通案例文件，不是新 schema。目录与七个交付文件现已实际创建，首轮失败渲染和四类独立编辑 probe 也已保留。

### 四门验收

|门|检查内容|当前 canary 状态|
|---|---|---|
|A 科学正确性|数值、计数、关系、方向、端点与示意含义逐项核对，任一硬错误不接受|PASS：最终图逐项核对；范围为 inference overview|
|B 视觉精简|无大段 prose 和重复解释；核心机制视觉权重合理；178 mm 可读|PASS at 178 mm；85 mm 细节阅读受限，未另行排版|
|C 可编辑性|真实 text、精确数值/公式、关键箭头和时间线可编辑，并做独立编辑 probe|PASS：53 text、0 image；文字/数值/箭头/时间线四类 probe 均有实际重渲染差异|
|D 构图保留|保留视觉层次、panel 结构与表征，不以结构检查代替实际 PNG/SVG 对照|PASS：已实际对照原 PNG 和最终 SVG 渲染；非像素级复刻|

如需独立复审，遵循用户已授权的路线图安排并从真实成品出发。没有成品或实际复审时，不标记完成。

最终状态规则：ACCEPTED = A/B/C/D 全部 PASS；REVISE = A PASS，但 B/C/D 有可修复失败；NOT_ACCEPTED = A FAIL。未执行、待检查或缺少证据时保持 PENDING，不能推断 PASS；B/C/D 的未解决失败不能汇总为 ACCEPTED。不使用总分掩盖科学硬错误。

本例主 SVG 为 178 × 117 mm；300 dpi 主预览 2102 × 1382 px，压力预览 1004 × 660 px。常规标签 7.37 pt、数学正文 8.50 pt、上下标 5.95 pt；85 mm 缩放后常规标签约 3.52 pt，不能视为单栏可用。所有渲染和编辑证据见 [editability-check.json](outputs/diffusion-policy-stage2/editability-check.json)，逐条判断见 [acceptance.md](outputs/diffusion-policy-stage2/acceptance.md)。未做独立审阅、原生设计编辑器导入或纸面打样，不扩展为任意图类稳定自动化结论。

## 工作区与本地恢复

活跃代码：run.py；当前说明：README.md、AGENTS.md、STAGE1-FREEZE.md、STAGE2-CONTRACT.md。本文件记录最新进度，[HISTORY.md](HISTORY.md) 记录演变。

保留 papervizagent/ 的原生 180 图参考库、来源和既有隔离环境；保留 AutoFigure-Edit/ 的源码及 .venv。默认渲染复用后者中的 CairoSVG/Pillow，该物理位置不意味着执行其模型 pipeline。上游环境相互隔离，不合并、不安装新包。

LocalFigure 旧实现、FigurePilot、方法调研和发布用 Git 副本进入 [日期归档](../archive/2026-10-04/README.md)，内部相对关系保持。归档的历史绝对路径和 provenance 原样保留，不再作为活跃入口；具体映射见归档清单。FigurePilot 与研究目录仍相邻，原 CLI 相对定位得以保留。含绝对路径的旧脚本不承诺迁移后直接可运行。

## 不依赖聊天的原始要求与证据

[独立审阅原件](docs/sources/stage1-independent-review-2026-10-03.original.txt) 是用户提供的路线图原文，字节保留，其“实际查看”等陈述来自原审阅者，本轮不冒充重新进行视觉复审。

[178/85 mm 用户确认原文](docs/sources/diffusion-policy-width-confirmation-2026-10-04.md) 保存最新尺寸要求。[相关历史消息摘录](docs/sources/conversation-excerpts-2026-10-04.json) 保存检索到的用户与助手公开消息，仅是相关近期片段，不是全账户历史导出，不含推理或工具载荷。当前交接读本文件即可，摘录用于追溯。

目录整理阶段的验证范围是归档字节完整性、冻结文件、活跃资源与链接可定位、现有 CLI 的只读结构检查；当时没有重做旧视觉验收，没有新生图或新 SVG，没有投稿级质量认证。其后新增的 canary 工作单独记录在上文和成品验收文件中，不回改这些历史案例报告。

本次整理已完成：25,598 个文件、2,720,984,800 字节（约 2.53 GiB）移入日期归档；迁移前后 SHA-256 全部一致。353 个保留的案例/审计/参考/代码文件核对通过，174 个冻结文件仍与原清单一致。180 条参考及图片、既有渲染环境、两个现有 SVG 的只读 CLI 检查、76 个当前文档本地链接均通过。发布 checkout 保持干净，commit 与 ZIP 哈希匹配上传记录；原审阅路线图字节和用户尺寸要求内容均保留。

最终核对见 [integrity-check.json](../archive/2026-10-04/records/integrity-check.json) 和 [validation.json](../archive/2026-10-04/records/validation.json)。归档节省的是活跃目录的混杂，不释放磁盘空间。原始源文、历史截图说明、provenance 与旧绝对路径是必须保留的格式/位置例外；本轮新写 Markdown 的多余空白与不可见字符检查通过，未涉及 DOCX 渲染。首次链接检查发生在核对报告写出前，临时报缺失的两个报告链接，已生成并复查通过；初次结果保留在归档 records/validation-initial.json。
