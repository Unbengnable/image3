# Caption migration and reconstruction decisions

The original Stage 1 PNG was viewed before reconstruction. It remains in ../zotero-three-cases/diffusion-policy/figure.png; no new Stage 1 generation or edit was performed.

|Original information|Disposition|Final location|
|---|---|---|
|Large global title and three numbered region titles|Remove global title; shorten region titles|a / b / c panel headings|
|Observation horizon, prediction horizon, execute horizon and time labels|Keep exact values once each|Editable To / Tp / Ta brackets and timeline|
|Encode once per policy query|Keep a short label; explain query boundary|Once per query; caption paragraph 1|
|RGB observations are not diffused or future-predicted|Move the full explanation|Caption paragraph 2|
|Proprioceptive robot state, examples of joint angles and gripper state|Keep q_t and state-vector glyph; move examples/general explanation|Observation panel and caption paragraph 1|
|From images / from proprioception beside conditioning vector|Remove repeated labels; retain both input routes|Blue vector and two incoming arrows|
|Fixed conditioning across denoising|Keep short relation|Fixed conditioning c_t on the blue bus|
|Multiple Predict noise boxes and shared-parameter route|Show one shared predictor and an expanded scheduled step|Denoising panel; caption explains repetition|
|Gaussian action noise and K diffusion steps|Keep initialization label and K → 0 direction|Denoising panel|
|Scheduled DDPM / DDIM update with omitted coefficients|Keep operator; move scope and coefficient caveat|Scheduled update; caption paragraph 2|
|k distinct from environment time t|Keep short local labels; explain notation|Panels b/c and caption paragraph 2|
|CNN/FiLM and Transformer/cross-attention internal explanations|Keep parallel visual insets; move detailed interpretation|Backbone inset and caption paragraph 1|
|Execute first Ta actions / Execute only Ta actions|Remove repeated prose|Ta = 4 bracket and one Execute route|
|Not executed before replanning|Keep one short relation for the pale second half|Replan before execution; caption paragraph 2|
|Observe again and replan / long Next policy query route description|Keep unambiguous arrowheads; shorten label|Environment → observations; Next query: t + 4|
|Illustrative horizons and trajectories; not measured data|Move full caveat and retain it in SVG accessible description|Caption paragraph 2 and SVG desc|

No claim of a measured 40–60% prose reduction is made: the reference range was advisory, and prose versus entity-label token counts depend on classification. The actual SVG contains short entity/operator/relation labels, no long explanatory sentence. The caption restores the scope and caveats removed from the drawing.

Composition retained: observation/conditioning at upper left; parallel alternatives at upper right; a wide noisy-to-clean action ribbon in the middle; eight action glyphs, partial execution, robot scenes and a feedback loop below. Blue conditioning, purple actions and orange execution preserve the color roles. Background tints and the feedback stroke were reduced. Robot scenes, action curves, convolution slabs, transformer tokens and vector glyphs were rebuilt as editable native SVG geometry; no full-image raster or automatic tracing was used.

Initial render evidence is retained in initial/. It exposed CairoSVG's handling of centered text spans and a path hidden under the subsequently drawn execution panel. The final source uses explicit text-span positions and draws the output route after panel backgrounds. A later route adjustment avoids the τ label below the current action sequence. These were reconstruction defects, not changes to the Stage 1 scientific brief.
