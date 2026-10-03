# Zotero 三篇新论文：文字生图与论文原图对照

2026-10-03。完成 FAST、Diffusion Policy、DreamerV3 三个新案例。它们未出现在当前项目已有 π0/attention 完成案例中；这不等于审计了用户全部历史对话或使用记录。

本轮只评估 Stage 1 的 PNG 生成和修订。每例一次生成、两次针对性编辑，共九次内置 imagegen 调用。没有运行 Stage 2、产出新的 SVG，不能据此宣称新的可编辑重建泛化通过。Stage 1 架构和 run.py 未修改，没有模型服务、Google 凭据或新增专用绘图脚本。

## 结果

|案例|两轮修订后的科学判断|视觉与原图比较|
|---|---|---|
|FAST|未通过数值一致性。正确说明 DCT、量化、低频优先展开、BPE 和近似解码；上方展开列仍少一个零。|色彩和解释层次清楚，但重复展示与长文字使图比原图臃肿。原图更清楚展示 BPE 合并。|
|Diffusion Policy|在“条件动作扩散与滚动执行”限定范围内，主要关系通过目视复核。|闭环和 horizon 更容易讲解；原图网络结构更完整，生成图省略 causal mask、逐层 FiLM 等细节。|
|DreamerV3|未通过完整关系检查。actor 方向已修正，但 prior 条件线和在线反馈仍有问题。|模型学习、想象学习和交互三区分明；原图的时间展开和路径更简洁可靠。|

不把三个案例合成一个主观总分。科学错误可使案例不通过，不能被漂亮配色抵消；也不以“比论文原图好看”替代检查科学内容。

## 取样、来源和对照方法

三个案例分别覆盖动作序列压缩、条件扩散及滚动控制、RSSM 与想象学习。为图类差异有意选样，不是随机样本，不适合计算总体成功率。没有选择此前的 π0 或 Attention Is All You Need。

|案例|Zotero 条目 / 附件 key|实际 PDF 版本|方法文字|对照原图|
|---|---|---|---|---|
|FAST|FS8G6Q34 / 7W4YFC8Q|2501.09747v1，2025-01-16|Section V-A/V-B，Algorithm 1，PDF 4–5 页|Figure 4，PDF 第 5 页|
|Diffusion Policy|ILNUZULC / KQXJ6KL3|2303.04137v5，2024-03-14，扩展版|Sections 2.3、3.1、3.2，PDF 2–4 页|Figure 2，PDF 第 3 页|
|DreamerV3|RWS3QYN9 / AKLG5XL5|2301.04104v2，2024-04-17|World model / Critic / Actor learning，PDF 3–6 页|Figure 3，PDF 第 3 页|

Zotero 元数据里的年份不总等于附件版本；本轮判断以实际 PDF 为准。FAST 元数据缺作者，PDF 署名为 Karl Pertsch、Kyle Stachowicz 等；Diffusion Policy 为 Cheng Chi 等；DreamerV3 为 Danijar Hafner、Jurgis Pasukonis、Jimmy Ba、Timothy Lillicrap。完整条目和原始附件路径保留在本地；审阅包的 source.json 使用公开论文版本链接，并保留 PDF SHA-256 与附件 key。只读论文库，没有改写 Zotero 条目或附件。

先提取方法正文并写出科学 brief，再在既有 180 图参考库选图、查看参考，提炼成文字视觉原则，随后生成和修订。分别选 DB179、DB005、DB241；仅使用颜色、表征区分、迭代和时间链等视觉原则，没有复制相关上游方法。目标论文的图像在全部九次调用结束后才渲染并查看；没有作为 imagegen 输入，也没有从它们裁素材。方法全文提取文件含图注，Codex 读方法时可能见到图注，不能称为完全盲测；图注没有写入实际生图 prompt。基础模型是否在预训练中见过这些论文无法判断，不据此保证绝对原创。

生成和评价都是当前 Codex 完成，非独立评审；后验原图对照只是人工检查，不是基准评测框架。每例的图形事实、顺序、条件路径、数字一致性、额外假设、信息遗漏和阅读负担分别记录于 evaluation.json。

## FAST

方法目标是把每个动作维度的时间序列做 DCT，scale + round 得到量化整数，按频率列优先、跨动作维度展开，再经 BPE 压缩为可变长 token。量化有损，BPE 相对量化整数序列无损。生成图还根据正文补充了解码、反归一化和近似重建。

第一稿主矩阵出现第三维，而解码序列未包含对应系数。第一次编辑统一为二维四频率后，上方展开列只显示三个零，DCT 轴还重复了 3。第二次编辑修正轴，仍未补齐上方展开列。矩阵和中间 inset/下方逆 BPE 都对应 [12, 9, 4, -2, 0, 0, 0, 0]，上方却缺项。这个数字错误足以阻止验收，不能用其它正确部分掩盖。

对照 Figure 4：两图采用方法顺序所必需的“连续信号→频域→量化→展开→token”语义，不代表照搬原图。原图用五步、频率 basis 和 BPE 分组合并表达压缩，布局紧凑；生成图独立采用长编码行、展开教学 inset、近似解码行，解释更详，但重复多、BPE 合并细节更弱。示意曲线未由所示系数计算，图脚已声明 illustrative，不可拿它们当真实 DCT 数值验证。

## Diffusion Policy

第一稿已表达观测只编码一次、固定条件、动作高斯噪声、迭代去噪、三种 horizon 和只执行部分预测动作，但反馈接到了动作序列，而且自行添加了缺少完整调度系数的更新公式；动作 timeline 又使用了未来机器人场景，易与未来图像预测混淆。

第一次编辑移除公式，改为动作向量 timeline，把反馈接回观测，但观测源端还留有逆向箭头。第二次编辑去掉该箭头，并增加向左回流方向。最后图在主机制范围内没有看到上述科学错误：k 与 t 区分，To=2/Tp=8/Ta=4 明确为示意，执行 t 到 t+3 后用新观测开始下一次 policy query，观测不扩散。CNN+FiLM 与 Transformer+cross-attention 被标记为替代方案。

对照 Figure 2：原图同时展现一般策略和两类 denoiser 内部结构，特别是 FiLM 的 a*x+b、k embedding、causal attention mask。生成图更强调从条件到去噪再到执行的讲解，省略这些内部约束，不能作为 Figure 2 的完整替代。最终机器人到新观测的短蓝线缺明显箭头头部，靠相邻“Observe again and replan”文字理解，是剩余视觉瑕疵；共享 denoiser 下方的紫色路线也不够干净。实际机器人图片是生成的示意插图，并非实验帧。

## DreamerV3

第一稿的主要错误包括：actor 的动作箭头反向、奖励/continuation 进入 critic 而非 returns、prior 样本与 posterior 合流到训练 state；使用正态 bell curve 表示本应 categorical 的状态；在线反馈来自 replay。第一次编辑将 categorical 和训练 state 改好，但仍保留部分错误，并把在线 state 标签改成 (h_t,x_t)。

第二次编辑修正 actor→action→RSSM 和 state=(h,z)，并让 critic 接收 state、reward/continue 各自接 returns，想象中不再有未来 encoder。仍有两项重要残留：左图 prior 虽写 p(z|h) 却没有 h_t 输入线；底部“new observation”路线实际从 replay buffer 出发，仍错误暗示在线 inference 从存储端取输入。另外 shared critic 只清楚接 terminal state，不能读出每个时刻的 value；起始 replay-inferred 状态与第一想象 state 的关系缺少清楚连接。正文机制覆盖因此仍为部分完成。

对照 Figure 3：原图直接并排展开 world-model learning 和 actor-critic learning，只有真实阶段以及想象起始有编码器，离散状态和 recurrent 状态贯穿时间。生成图新增预测头、returns 和交互解释，但未完整重建原图左侧三步 observation/posterior 时间展开，并带来更多连线错误。原图在科学关系和表达经济性上更强；生成图的 panel 层次好看不能抵消错误。

## 阅读尺度和交付边界

已实际查看每张初稿、两次编辑和原图裁片。屏幕大图总体无明显文字裁切，文字与线条较清晰，但三张都以大量说明填满 1536×1024。尚未进行指定期刊栏宽、灰度打印、字体尺寸或读者理解实验；不能宣称投稿级。比较页的尺寸滑块只是屏幕缩放，不是印刷验收。

审阅包每例目录包含 request.txt、context.md、selected-references.json、generation-prompt.txt、image-edit-1.txt、image-edit-2.txt、draft-1.png、draft-2.png、figure.png、original-figure.png、evaluation.json、source.json。完整论文、原文全文提取、整页渲染和 Zotero 完整条目仍保留在本地；公开来源链接见各例 source.json。figure.png 表示预算结束后的最后一稿，不表示该案例通过。原图裁片只来自本地 PDF 渲染，不作生成素材。

[打开并排比较页](comparison.html)，可切换初稿/第一修订/最后一稿、缩放或查看原尺寸。原始 PNG 与记录也可独立查看。旧 π0/attention 文件哈希与本轮开始前一致。

本轮结论：自然语言方法文字能跨三类方法产出有解释价值的候选图；限定两轮修订预算下，只有 Diffusion Policy 的核心机制达到可用解释图范围，FAST 的数值和 Dreamer 的关系仍阻止科学验收。工程重点应是 Codex 对真实产物逐项 critique，以及在需要精确数字/连线时用后续矢量编辑做确定性修复。本轮没有执行这种 Stage 2 修复，不把它当成已解决。

