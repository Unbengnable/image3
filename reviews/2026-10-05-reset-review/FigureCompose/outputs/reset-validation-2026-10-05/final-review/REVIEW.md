# Paired MAE review of frozen candidates

Review started 2026-10-05 13:09:55 UTC (21:09:55 Asia/Shanghai). Final evidence/cost inspection: 13:15:43 UTC. Reporting and final verification follow. X is the direct-vector arm; Y is the imagegen-then-reconstruction arm. Reader-first was recorded before that mapping, scientific packet or native sources were opened.

Both final candidates convey the MAE pre-training mechanism and pass the delivered CairoSVG source-scope science check. Both also fail an actual Inkscape visual compatibility check: selected patch crops overflow and overlap the encoder-input area. Experimental decision is **REVISE for X and REVISE for Y**. The original raster generated PNG is separately **NOT_ACCEPTED for science**; later SVG repairs do not change that Stage 1 result. These are dimension-specific findings, without a composite score or a claim of publication quality. Historical Diffusion Policy acceptance remains untouched.

## Separate main findings

|Dimension|X: direct vector|Y: raster then reconstructed SVG|
|---|---|---|
|Science, delivered CairoSVG view|PASS|PASS|
|Meaningful visual substance|PASS: identifiable landscape crops, sparse encoding, restored token positions and spatial loss outlines|PASS: recognizable sailboat, removed-image view, sparse crops and target/prediction loss grids|
|Design economy and route clarity|PASS with minor ambiguity: compact forward row, lower target branch; loss subset depends on orange-outline convention|PARTIAL: strong spatial explanation but repeated image/target/indices and two-direction reading add load|
|Physical source typography and supplied render integrity|PASS for specified millimetres, DPI and no observed collisions in CairoSVG preview; 5.10 pt subscripts remain a risk|PASS for specified millimetres, DPI and no observed collisions in CairoSVG preview; 6.05 pt indices remain a risk|
|178 mm human print readability|NOT_TESTED; screen reader judgment PARTIAL because subscripts are small|NOT_TESTED; screen reader judgment PARTIAL because dense indices are small|
|Native semantic editability, tested 75%→50%|PASS: retained IDs, crops, encoder/latent counts, decoder slots, loss outlines and caption change consistently|PASS: blanking geometry, retained crops, latent/mask bank counts, restored slots, prediction/target loss outlines and caption change consistently|
|Editable scene illustration internals|PASS: native vectors and local symbols|PARTIAL by intentional hybrid design: two scene illustrations are raster; scientific text/geometry native|
|Inkscape CLI parse and plain-SVG save|PASS|PASS|
|Inkscape visual export compatibility|FAIL: crop symbols display overlapping full landscapes|FAIL: crop scene uses display overlapping full sailboat images|
|Interactive native editing / Illustrator compatibility|NOT_TESTED|NOT_TESTED|
|Observed copying audit|PASS for no observed copied asset/layout from inspected references/target; not proof of originality|PASS for no observed copied asset/layout from inspected references/target; not proof of originality|

The REVISE decision follows source-scope science PASS with a concrete delivered-use compatibility failure. Missing human readability evidence remains pending. This does not impose an 85 mm redesign or revise either frozen main.

## Scientific evidence and spatial patterns

Authority: preserved original [Section 3](https://arxiv.org/html/2111.06377v3#S3) text plus the frozen common packet. The packet defines a toy 4 by 4 grid, not model resolution. Original Section 3 states that the encoder only handles visible tokens without masks; encoded visible tokens and shared mask vectors form the full decoder sequence, restored by unshuffling, with decoder positions; MSE applies only to masked image pixels.

Both main sources show visible IDs **1, 6, 11, 12** at correct row-major spatial locations. Four identifiable patch crops enter the encoder; four native latent tokens leave it. Twelve mask tokens/slots join after encoding. Sixteen slots are restored and sixteen patch predictions shown. The masked loss domain is exactly **2, 3, 4, 5, 7, 8, 9, 10, 13, 14, 15, 16**, excluding the four visible positions. Original pixels supply a target branch separate from the inference path. No explicit wrong hidden-pixel or mask-token edge enters the encoder.

X's image crop symbol viewBoxes agree with the source scene positions. Its decoder-grid translations and loss-outline geometry match the data IDs; counts are not just labels. Y's source exposes independent native blanking rectangles, outlines, latent and mask rectangles, labels and arrows; the two embedded scene assets carry illustration content rather than the whole diagram. Data kinds and visual positions agree across masked, visible, latent, restored, prediction and target views. Both use a lightweight decoder and distinguish encoder/decoder positions without claiming identical embeddings. Captions scope away downstream recognition, benchmarks and normalized targets, and identify illustration rather than measured inference.

X expresses the sparse-encoder insight using selection crops and a restored latent grid. Y makes removed pixels explicit and spatially juxtaposes target and prediction. Neither is an empty grid-and-box failure. X's compact omission of a full masked-image stage preserves the required selection relation. Y's duplicated target is explanatory but increases visual load. Exact Transformer internals and shuffle implementation are omitted consistently with the overview scope.

## PNG science versus subsequent SVG repair

Y's original `arm-raster/generation-01.png` was inspected independently before its author critique/cost records. It depicts four visible encoder inputs but only **three** output latent blocks, conflicting with its own four-latent annotation. The loss-target illustration hides masked original pixels behind gray cells, failing to show the actual pixel targets used for supervised reconstruction. The restoration annotation is placed after decoder output rather than an explicit pre-decoder restored sequence. These are scientific defects in the generated diagram, even though its scene imagery and sparse patches are useful. Stage 1 science: **FAIL / NOT_ACCEPTED**.

Y's final SVG repairs latent count, restored pre-decoder spatial slots, positional placement and a full original-pixel target. Its final source-scope science PASS therefore measures successful Codex reconstruction/correction, not imagegen scientific reliability. X has no generated PNG stage; its native source and CairoSVG delivered view are the main artifact.

## Actual semantic edits

Both separate 50% copies retain **1, 3, 6, 8, 9, 11, 12, 14**, leaving masked/loss IDs **2, 4, 5, 7, 10, 13, 15, 16**. Eight crops reach the encoder, eight latents emerge, eight post-encoder masks fill the complement, sixteen positions/predictions remain, and loss labels/outlines/captions change to eight. Scene assets and principal main routes remain unchanged. The main hashes rechecked during review agree with frozen author records.

X preserves native scene/crop geometry and extends its latent column; Y fits eight crop glyphs in the same area by narrowing them, which distorts their displayed aspect ratio but preserves crop identity and selection semantics. Both edit renders are inspected and coherent in CairoSVG. This is evidence of semantic editing in native text and scientific geometry. It is not proof of interactive editor usability; neither edit copy was repaired from reviewer feedback.

## Physical typography and native renderer failure

X is **178 by 82 mm**, 2102 by 968 px, 299.9994 dpi. Body is about **7.65 pt**, headings **8.50 pt**, IDs/small labels **6.52 pt** and latent subscripts **5.10 pt**. Y is **178 by 99.68 mm**, 2102 by 1177 px, 299.9994 dpi. Body is about **7.06 pt**, headings **8.07 pt**, IDs/token labels **6.05 pt**. These source/DPI values establish size, not comfort on an uncalibrated screen or paper proof. X main has 51 native text elements and zero image elements; Y 114 native texts and two local scene images. Object counts supplement, rather than replace, semantic evidence.

Installed Inkscape **1.4.4** parsed copies of both originals, saved plain SVG and exported each saved copy. The selected image crop content overflowed its intended frames, producing several large overlapping full scenes over the sparse-patch/encoder-input area. A second direct export from each original copy reproduced the same PNG bytes as its saved roundtrip export; it is not just a save mutation. Native text strings and image counts survive. This demonstrates that successful CLI status and element preservation do not establish native visual compatibility. Evidence is under `native-editor/`, including direct/roundtrip PNGs, saved SVGs and `check.json`.

The actionable future repair is to make patch viewport clipping explicit in a form supported by the intended native editor, then rerender both original and saved native copies. This is a diagnosis to verify, not a tested implementation. No source repair was made here. The failed native view would not be suitable for paper use despite the coherent CairoSVG preview.

## Post-freeze originality and exposure audit

At **13:13:25 UTC**, after reader-first, source audit and edit checks, the reviewer viewed DB005, DB082 and the official [MAE Figure 1](https://arxiv.org/html/2111.06377v3/arch.png) in one batch. The target image was downloaded from that exact URL into `target-MAE-figure1.png`; the first web open was at 13:13:06 UTC. No target/reference image was sent to authors, and no reviewer findings were sent to authors for revisions. The coordinator reports caption exposure during packet preparation and a target URL open after freeze; its actual later target-pixel download is separate from the authors' exposure.

DB005 uses three shaded horizontal stages, horse→zebra images, repeated noise/DDIM steps, a computed mask and a correction loop. Neither candidate copies those assets, step labels, shaded three-stage arrangement, noisy-image repetition or unusual correction motif. Y's two-direction flow is broadly similar to many folded pipelines, but its sparse-image/token/loss logic, scene and placement differ; that alone is not evidence of copying.

DB082 uses three rounded color regions, a temporal axis, repeated human-motion images, per-time base models and nested per-joint temporal Transformers. Neither candidate imports its human imagery, time-axis repetition, colored region grouping or nested Transformer composition. Local crop/token use is a shared scientific illustration convention, not a distinctive copied asset.

The MAE target uses a flamingo image, a single masked-input grid, a tall visible patch column, tall encoder, several long token columns, smaller decoder, a salmon-colored output column and right-side target. X shares the mandatory encoder→restored tokens→decoder order and qualitative encoder/decoder size asymmetry, but replaces the flamingo, long columns and target placement with landscape crops, a two-dimensional restored grid, explicit loss locations and a lower original-pixel branch. Y uses a sailboat, separate original/masked views, a two-tier route, two-dimensional restored grid, explicit mask bank and target/prediction loss panels. No observed reference asset reuse or nonessential layout replication was found. This is not proof of originality: model-training memory and unobserved exposure cannot be excluded.

## Costs and provenance, read last

Author notes, operation records and cost/provenance files were read at **13:15:43 UTC**, after independent image/source/edit/native/reference findings. Their reported imagegen errors agree with the reviewer's independent PNG observations. Author self-checks are not adopted as acceptance.

|Measured quantity|X / V|Y / R|
|---|---|---|
|Measured start definition|12:57:54 UTC after brief scope read|12:58:55.352 UTC design registration; first machine observation 12:58:06.668 UTC|
|Main freeze|13:06:17 UTC|13:05:31.76 UTC|
|Author end|13:10:23.545 UTC|13:09:26.346 UTC|
|Reported elapsed|749.545 s / 12.49 min from initial clock|630.994 s / 10.52 min from design registration; about 679.678 s / 11.33 min from first machine observation|
|Imagegen generation/edit calls|0 / 0|1 / 0; generation took about 54 s|
|Successful CairoSVG renders, including semantic copy|4|3|
|Consolidated main content/layout revisions|1|1|
|Syntax/render-only repair|1 glyph repair; one failed inline edit command preceded it|0|
|Separate semantic edits|1|1|
|New packages / external paid model API calls|0 / 0|0 / 0|
|Tokens, active thinking time, subscription monetary cost|Unavailable|Unavailable|

Clock boundaries differ, and neither measures active compute. The single paired case does not establish one route as generally faster, cheaper or better. Y contributes richer image content but required scientific repair; X reaches a compact explanatory representation without imagegen, but both share a native crop compatibility defect. The paired outcome supports testing either route further with cross-renderer checks, not a causal route preference.

Reviewer operations before report writing: 11 functions.exec orchestration calls; twelve image views (two neutral mains, two semantic copies, three references/target, two native roundtrips, original generated PNG and two direct-native confirmations); six successful Inkscape exports, no figure repairs; one web open plus one exact target-image download; no imagegen calls or package installations. Reviewer token/monetary costs are unavailable. Final report writing/check calls are additional.

## Limits and preservation

This is one project-fresh case, two fresh same-model author contexts and one same-model reviewer. Shared storage was a procedural boundary, not OS isolation. Authors received a prepared paraphrased packet, so automatic extraction from an underspecified request was not tested. Human reader recovery, calibrated print proof, journal suitability and interactive editing are NOT_TESTED. This reviewer did not inspect all intermediate drafts; main/effect evidence and author operations are distinguished accordingly.

All reviewer writes are confined to `final-review/`. Frozen mains, semantic copies and historical acceptance were not overwritten. Reports use ordinary paragraphs/tables without manual alignment whitespace. No DOCX was generated, so DOCX page QA is not applicable.
