# Diffusion Policy Stage 2 canary acceptance

Date: 2026-10-04, Asia/Shanghai. Final status: ACCEPTED for the local 178 mm contract canary. A / B / C / D are all PASS. This is a same-Codex manual review of the final rendered SVG and preserved method text, supported by structural checks and actual edit probes. No independent reviewer, printed proof, journal approval or native design-editor import test was performed.

The accepted source is figure.svg in this directory. The number-edit probe intentionally changes Ta to 3 to demonstrate editability; that probe is scientifically invalid and is not an accepted figure. Initial rendering defects and probe outputs remain under review/ and edit-probe/ as evidence.

|Gate|Status|Evidence and boundary|
|---|---|---|
|A Scientific correctness|PASS|Final topology, horizon counts, diffusion direction and caption were checked anew against local Sections 2.3 / 3.1 / 3.2; detailed audit below. Limited to the inference overview, not the full paper Figure 2.|
|B Visual economy|PASS at 178 mm|Actual final 300 dpi and nominal 96 ppi physical-size previews inspected. Long explanations moved to caption, global poster title removed, repeated predictor boxes consolidated into one expanded step. No clipping or text/arrow overlap observed in the final render.|
|C Editability|PASS|53 native text elements, 28 text spans, 95 vector shapes counted, 0 images; independent text, number, arrow and timeline edits each produced localized changes after rendering. Counts include definitions and markers and do not enumerate independent scientific components.|
|D Composition preservation|PASS|Actual Stage 1 PNG compared with final render. Observation/conditioning, parallel backbone inset, wide action-trajectory ribbon, colored eight-action timeline, robot scenes and feedback route are retained. Curves, scenes and neural-network glyphs remain visual representations; the result does not reduce to boxes and arrows. No pixel-fidelity claim.|

Final status follows the specified rule: ACCEPTED requires all four PASS; REVISE requires A PASS with fixable B/C/D failures; A FAIL gives NOT_ACCEPTED. Missing evidence stays PENDING. The 85 mm stress limitation does not fail the 178 mm gate.

## A: scientific audit of the final output

|Item|Actual final representation|Result|
|---|---|---|
|To = 2|Two observation groups at t − 1 and t; observation bracket and editable To = 2 label|PASS|
|Observation conditioning|Observation → RGB encoder → image features → c_t; q_t/state vector also enters c_t|PASS|
|One encoding per query|Once per query label; c_t retained on blue bus across diffusion; next query forms a new condition|PASS|
|Gaussian action initialization|A_t^K contains schematic noisy action channels; its ribbon leads through omitted steps to A_t^k|PASS|
|Denoiser inputs|edge-current-denoiser enters the shared predictor; edge-fixed-condition-denoiser enters from blue bus; εθ(c_t, A_t^k, k) names all three inputs|PASS|
|Scheduled update inputs|Current A_t^k bypasses the predictor via edge-current-update; predicted noise enters via edge-noise-prediction-update|PASS|
|Direction|Expanded update is k → k − 1, output arrow enters A_t^(k−1), and subsequent ribbon ends at A_t^0; K → 0 repetition label agrees|PASS|
|No incomplete exact update|Scheduled operator only, with coefficients explicitly outside caption scope|PASS|
|k versus t versus τ|Diffusion index k, robot/environment time t and action-position τ are distinct in figure/caption|PASS|
|Tp = 8|Eight action groups: t through t + 7; joint prediction bracket spans all eight|PASS|
|Ta = 4|First four action groups emphasized and covered by orange bracket; orange route from that bracket enters environment|PASS|
|Four remaining actions|Pale second half labeled Replan before execution; caption states it is superseded by replanning|PASS|
|Clean prediction to execution panel|edge-final-timeline connects A_t^0 to the predicted timeline, with arrow visible above panel backgrounds|PASS|
|Environment feedback|Environment → new observations has a visible arrowhead; source of returning blue route is the new-observation scene and its sole arrowhead enters the observation input|PASS|
|Next-query history|Next query at t + 4 is explicit. Caption states that the latest history is used; the one lower-right scene represents acquisition, not a new horizon of one|PASS|
|Alternative backbones|Two parallel inset cells marked either backbone; no serial edge or implied CNN → Transformer route|PASS|
|No observation diffusion / future-image generation|Only action curves are denoised. Robot scenes belong to acquired observations/environment, with explicit caption caveat|PASS|
|Scope and empirical claims|Horizon values, curves, channels and robot scenes declared illustrative. No performance numbers or experimental parameter claims. Training and complete network internals omitted explicitly|PASS|

## B: physical rendering and readability

SVG root: width="178mm", height="117mm", viewBox="0 0 1780 1170". One SVG unit is 0.1 mm in the primary layout. The SVG was composed with these physical metrics; it is not a rescaled 1536 × 1024 raster.

|Quantity|178 mm target|85 mm stress scaling|
|---|---|---|
|300 dpi preview|2102 × 1382 px|1004 × 660 px|
|Physical width implied by pixel rounding|177.969 mm at 300 dpi|85.005 mm at 300 dpi|
|PNG pHYs DPI readback|299.9994 dpi|299.9994 dpi|
|Normal labels|7.37 pt|3.52 pt|
|Mathematical base text|8.50 pt|4.06 pt|
|Subscripts and superscripts|5.95 pt|2.84 pt|
|Main relation stroke|0.32 mm|0.153 mm|
|Feedback stroke|0.24 mm|0.115 mm|
|Critical arrowhead extent|1.10 mm|0.525 mm|

Both previews are rendered from the same file and composition. Integer pixel rounding and PNG's integer pixels-per-metre encoding cause the tiny physical-width/DPI differences above; SVG physical width remains exactly 178 mm. Additional review/physical-178mm-at-96ppi.png and physical-85mm-at-96ppi.png are nominal screen equivalents, not a calibrated monitor or printed proof. Physical acceptance is grounded in SVG millimetres, font/line metrics, DPI and inspected renders rather than the chat image's display size.

At 178 mm, horizon brackets, key arrowheads, action counts and mathematical indices are distinguishable; labels do not collide with routes after correction. At 85 mm, the three regions, partial-execution distinction and closed loop remain identifiable, but sub/superscripts, τ labels, timeline times and the expanded noise-predictor formula are too small for comfortable reading. The stress result is LIMITED, not single-column readiness. No alternate layout was created to improve this stress check.

Caption migration is itemized in review/caption-migration.md. No measured percentage reduction is claimed. The final figure has short entity/operator/relation labels, while explanatory sentences and scientific caveats reside in caption.md.

Reproduction uses the existing CairoSVG 2.9.1 / Pillow 11.3.0 environment, without installing packages. For each width, set output_width = round(width_mm / 25.4 × 300), render figure.svg with cairosvg.svg2png(dpi=300, output_width=output_width), then save the PNG with Pillow dpi=(300, 300). Height follows the same source aspect ratio. This is file rendering, not a new drawing implementation.

## C: actual independent edit probes

Each probe starts from a fresh copy of the accepted SVG. Only its named edit is applied; the accepted source is unchanged.

|Probe|Actual edit|Changed pixels at 178 mm / 300 dpi|
|---|---|---|
|Text|RGB → Image|1387|
|Number|Ta label 4 → 3, deliberately invalid test copy|276|
|Arrow|Reroute only environment → observations path|764|
|Timeline vector|Reduce only action-0 glyph width, 86 → 65 SVG units|2462|

Actual source copies, rendered copies and localized difference bounds are recorded in editability-check.json and edit-probe/. The renderer initially rejected a probe XML declaration using the nonstandard encoding spelling utf8; probe copies were rewritten with encoding="utf-8" and all four rerenders passed. The failure did not alter the accepted source.

The figure uses editable shared SVG symbols for scene/action glyph geometry; separate use instances allow per-instance movement/scaling, while the symbol definitions expose their shapes. This is standard SVG structure, not a new component engine. Native Illustrator/Inkscape import, font substitution across operating systems and printed readability remain untested.

## D: comparison and preservation

The reconstruction preserves the original four-region arrangement, color roles, visual reading order and observation → diffusion → execution feedback narrative. Detailed explanatory captions and the large title were removed. The original shaded robot illustrations were replaced by native vector scenes with an articulated gripper, tabletop and colored cubes; their schematic role is preserved without a pixel-matching claim. Four colored action channels remain in noisy-to-clean curves and action glyphs. The parallel CNN slab and Transformer token motifs remain recognizable.

The original PNG and original case records were only read. Source paths and SHA-256 values are recorded in editability-check.json. No Stage 1 code, image generation, archive content, historical evaluation or framework was changed for this canary. All canary artifacts and edit/render evidence are under outputs/diffusion-policy-stage2/.
