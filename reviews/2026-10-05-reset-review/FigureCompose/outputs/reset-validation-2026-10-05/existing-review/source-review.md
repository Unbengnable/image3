# Source review

Source inspection recorded by 2026-10-05 12:58:27 UTC. Reader-first note was saved before project instructions or protocol were opened. Project `AGENTS.md` necessarily exposed its broad historical A/B/C/D PASS statement; detailed `acceptance.md`, the semantic lock and prior edit probes have not been opened at this stage. No target-paper image, reference image or new-arm output was inspected.

## Actual source evidence

Authority inspected: `outputs/zotero-three-cases/diffusion-policy/method-source-pages.txt`, preserved PDF pages 2–4, especially Sections 2.3, 3.1 and 3.2. This is local extracted paper text, including extraction imperfections and Figure 2 text/caption. I did not fetch or inspect the source PDF, so this review verifies consistency with the preserved method text, not extraction completeness or visual similarity to Figure 2.

- Section 2.3: latest To observations condition a Tp-action prediction; Ta actions execute before replanning. This directly supports the three distinct horizons and query advance by Ta.
- Section 2.3 and Equation 4: only actions are the denoising output; the observation conditions the predictor. The noisy sequence and predictor output both contribute to the update. The SVG supplies both edges. The scheduled-update box abstracts coefficients and stochastic terms without explicitly claiming a deterministic subtraction-only update.
- Page 2 and Section 3.2: observation features are extracted once rather than every denoising iteration; individual image times are encoded and concatenated. The shared encoder abstraction and fixed conditioning bus agree at overview level.
- Section 3.1: a temporal CNN with observation and k FiLM conditioning or a Transformer are alternative noise-prediction backbones. Page 3 Figure 2 caption supports observation cross-attention and causal action attention. The figure presents the alternatives correctly; the caption explicitly omits layer detail and causal masking.
- Source text does not establish To=2, Tp=8 or Ta=4 as experimental settings. The supplied caption explicitly marks them illustrative. It likewise avoids numerical performance claims.
- Proprioception q_t is more explicit in the figure/caption than in Sections 2.3/3.2 prose; preserved Figure 2 text includes robot pose. This gives contextual support, but the exact q_t content or history is not specified in this source packet and should not be inferred.

## Direct SVG observations

Inspected `outputs/diffusion-policy-stage2/figure.svg`. It is 178 mm by 117 mm, viewBox 1780 by 1170. Native text and vector elements carry the mechanism; scene, plot and action symbols are reused with `<use>`. No full-figure raster wrapping is present in the inspected source. Eight action groups have meaningful IDs, time metadata and executed-state attributes. The first four are opaque, the last four have an opacity group, with To=2, Tp=8, Ta=4 and next query t+4.

Body size 26 units corresponds to 2.6 mm / approximately 7.37 pt at 178 mm. Sub/superscripts are 21 units / approximately 5.95 pt; headings 31 units / approximately 8.79 pt. These are physical source metrics, not evidence of legibility on calibrated print. At 85 mm, body would shrink to approximately 3.52 pt. An 85 mm overview is consequently a severe readability stress, not an appropriate alternate delivery target for this information budget.

The two routing ambiguities in reader-first remain: final output enters the pale prediction tail; the execution route attaches to the upper bracket path rather than directly to a clearly selected group. Neither constitutes a demonstrated wrong dependency under the overall Tp bracket and caption. They reduce immediate visual clarity. The backbone panel names its function but has no connector to the noise-predictor box. Curves progressively become smooth; that convention must remain illustrative, especially since the source discusses Transformer reduction of CNN over-smoothing.

## Preliminary findings before detailed historical acceptance

Science: no hard source contradiction found within this stated inference scope. Design: narrative and color hierarchy are effective, with specific route and denoiser-association ambiguities. Readability: supplied PNG is readable at a large display size; print and edited rendering checks remain pending. Editability: native structures are present; a consistent semantic change has not yet been demonstrated. Native editor: command discovery did not find Inkscape on PATH; an installation directory exists and will be checked. These are reviewer observations and pending tests, not adopted historical PASS decisions.

## Historical self-evaluation comparison, read last

Detailed `outputs/diffusion-policy-stage2/acceptance.md` was read at 2026-10-05 13:02:22 UTC, after the source audit, semantic edit, CairoSVG renders and native Inkscape roundtrip were completed and inspected. Its earlier A/B/C/D PASS is prior same-Codex self-evaluation, not an independent measurement supplied by this review.

- A science: the earlier source-limited inference-scope conclusion survives this fresh check. This review recovered the mechanism before reading the detailed audit and found no hard contradiction in the preserved source. Exact q_t content remains underspecified.
- B visual economy: its reported source metrics agree with my independent calculation. The absence of clipping is supported by the new 2102 by 1382 renders. I do not adopt the broad design PASS unchanged: output-to-tail routing and detached backbone association justify PARTIAL for unassisted visual clarity. Calibrated print remains NOT_TESTED. Nominal large chat rendering alone does not settle it.
- C editability: the earlier number-only Ta=3 probe is expressly labeled scientifically invalid. My Ta=3 test propagates the change through partition geometry, group opacity and metadata, bracket, execute origin, next-query label, description/comment and caption. This adds semantic edit evidence beyond changing one numeric label. Native text and geometry remain present.
- D composition preservation: this review compared the supplied delivered PNG and a fresh render of its SVG, not the earlier Stage 1 PNG. Therefore the historic Stage 1 comparison remains NOT_TESTED here; it is not independently reaffirmed by matching two representations of the delivered artifact.
- Native editor: the earlier report explicitly left this untested. The new Inkscape 1.4.4 CLI plain-SVG roundtrip and PNG export completed, preserved 53 native text elements and eight action IDs/execution flags, and were visually inspected. This adds parser/save/export compatibility evidence. Interactive object selection, text editing, human usability and Illustrator compatibility remain NOT_TESTED.

The historical ACCEPTED status and files have not been changed. This experimental check provides separate findings without a composite score or a publication-quality claim.
