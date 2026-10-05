# E1: Diffusion Policy delivered-figure review

Evidence window: first reader timestamp 2026-10-05 12:57:00 UTC; final evidence timestamp 13:02:22 UTC (20:57:00–21:02:22 Asia/Shanghai), 5 minutes 22 seconds between recorded evidence times. Reporting and final verification follow that window. Active thinking time and subscription monetary cost are unavailable.

This bounded review adds a successful semantic edit and native CLI roundtrip to the local evidence. It also finds specific design ambiguities. It does not replace the prior historical acceptance or establish publication quality.

## Separate findings

|Dimension|Finding|Evidence and limit|
|---|---|---|
|Science|PASS within preserved-source inference scope|Mechanism recovered from delivered PNG/caption first; source Sections 2.3/3.1/3.2 agree with fixed observation conditioning, action denoising, scheduled update, alternative backbones and receding horizon. No hard error found. Illustrative horizons are not reported settings. Exact q_t semantics are underspecified.|
|Design / visual economy|PARTIAL|Three-panel narrative, colors and explicit time labels help. A_t^0 arrow enters the pale tail, the orange execute route originates on the upper bracket, and alternative-backbone motifs are detached from the predictor. These make correct associations depend on caption and close reading.|
|Readability at 178 mm|PARTIAL|300 dpi renders have no observed clipping or text/arrow overlap. Body is about 7.37 pt; sub/superscripts about 5.95 pt. These are plausible small figure labels, but calibrated display, print and human readability remain NOT_TESTED. The supplied large image cannot establish print comfort.|
|Editability|PASS for tested semantic change|Ta=4→3 consistently changes native group metadata/opacity, selected/deferred region geometry, bracket, execution source, next-query label, SVG accessible description/comment and caption. To=2 and Tp=8 stay unchanged. 53 native text elements and zero embedded images remain.|
|Native-editor compatibility|PASS for CLI parser/save/export only|Installed Inkscape 1.4.4 opens a copy, saves plain SVG and exports PNG; 53 native texts and eight action IDs/flags survive. Rendering inspected. Interactive editing and Illustrator import are NOT_TESTED.|
|Delivered PNG to source reconstruction consistency|PASS|Fresh source render matches the supplied delivered visual structure. No attempt at pixel equality or asset-provenance proof.|
|Historical Stage 1 composition preservation, prior gate D|NOT_TESTED|No Stage 1 original PNG or reference image was opened in this experiment. The prior self-evaluation remains a historical claim.|

No aggregate score is assigned. For this experiment, delivered-use checks remain PARTIAL/PENDING because the design issues and physical human readability are unresolved. The historic local ACCEPTED/A-B-C-D-PASS record is preserved.

## Concrete semantic edit

Files: `edit/figure.svg`, `edit/caption.md`, `edit/preview-178mm.png`, `edit/check.json`. Render is 2102 by 1382 px with Pillow 300 dpi metadata, representing approximately 177.97 mm width after pixel rounding. SVG physical width remains 178 mm.

The selected region narrows from x=80…511 to x=80…403. The deferred region expands from x=533…964 to x=425…964. Action t+3 moves to the start of the pale region; action groups 0–2 remain opaque, 3–7 pale. The execution bracket ends at x=403, and the execute route starts at x=241.5, the selected-region midpoint. Ta becomes 3 and the next query t+3; the eight predicted actions still span t through t+7. The caption explicitly retains illustrative scope. All three panels retain the supplied composition. No scientific or layout correction was required after the initial edit render.

Source SHA-256 before edit and after native input copying: `ea4b45ded38650397cdf9477805a1e0f59b2fba69c068249c00848a1ccd669f6`. Edited SVG SHA-256: `7f14b4d82fb697dda6e99421d2e0f98e7e0013248cc648b666eb405a5f6003d5`. The semantic test is on a separate copy and does not repair or overwrite the accepted source.

## Native editor evidence

Files: `native-editor/input-copy.svg`, `native-editor/roundtrip.svg`, `native-editor/roundtrip-178mm.png`, `native-editor/check.json`.

Discovery: Get-Command did not expose Inkscape on PATH. Program Files inspection found `LOCAL_PROGRAMS/Inkscape/bin/inkscape.exe`; the coordinator also identified the console `inkscape.com`. The installed console reports version 1.4.4. It imported the original COPY, saved plain SVG and exported the saved result as a 2102 by 1382 PNG. The inspected render retains scenes, plots, indices, arrows and action partitions without observed missing objects or obvious collisions. It changes some font rendering details slightly, which reinforces the need to inspect exports across tools.

An initial PowerShell argument construction passed output paths as positional inputs, producing missing-file warnings and no exports despite exit code zero. One syntax-only correction used explicit argument strings and file-existence checks. Both exports then succeeded. This was an invocation repair, not a figure revision. No GUI was launched, and no interactive edit was performed.

## Actionable follow-up

1. Route the final clean prediction to a visibly whole-sequence anchor or the Tp bracket, avoiding entry into only the pale tail.
2. Make the execution selection relation visibly originate inside or at the selected first-Ta region; keep that association explicit after horizon edits.
3. Add a lightweight association between the alternative-backbone inset and the shared predictor, or move the inset nearer its parent operator.
4. Obtain a 178 mm printed or calibrated human check for subscript readability before treating the figure as ready for a paper. This is a pending evidence gap, not a request to redesign at 85 mm.

These are findings for a later authorized revision. They have not been applied to the protected historical figure or used to add an improvement iteration to this experiment.

## Exposure, operations and costs

- Reader-first saw only `input/figure.png` and `input/caption.md`; its note was saved before instructions/source/prior details. The project AGENTS subsequently exposed the broad historic PASS line; detailed acceptance was read last, after actual edit and native tests.
- Source files opened: project AGENTS.md; this experiment PROTOCOL.md; original canary figure.svg; preserved Diffusion method-source-pages.txt; detailed acceptance.md last. Directory metadata was inspected to find acceptance and Inkscape. The semantic lock, previous edit probes, target-paper image, reference images, MAE scientific packet and new-arm outputs were not opened.
- This is same-model procedural reviewer separation in shared filesystem storage. It is not an OS sandbox, a human study or independently trained-model replication.
- Image generation calls: 0. Network/source-fetch calls: 0. Paid model API calls: 0. Package installations: 0. GUI/native mouse interactions: 0.
- CairoSVG render invocations: 2 successful (original copy and semantic copy). Inkscape export invocations: 4 total, 2 unsuccessful due to initial argument syntax and 2 successful after one syntax-only repair. Native version/help calls: 2. Figure scientific/visual revisions: 0 after initial semantic edit; syntax-only repairs of native invocation: 1.
- Operational tool ledger before reporting: 13 functions.exec calls wrapping 27 nested tool calls, including four image views (input, original CairoSVG render, semantic render and native render), file reads/writes, commands and timestamps. Report-writing and final-verification calls are outside that operational subtotal.
- Token usage and subscription price are not provided by the tools. Do not interpret absent cost telemetry or zero imagegen calls as zero overall cost.

Formatting check: reports use ordinary paragraphs and Markdown tables/lists, with no tab/space alignment. The edited caption retains original scientific statements except the authorized execution-horizon change and corrected relative source path; it removes trailing blank lines. No original file was overwritten.
