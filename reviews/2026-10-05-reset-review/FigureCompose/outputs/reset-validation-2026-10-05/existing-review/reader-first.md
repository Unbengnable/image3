# Reader-first observation

Recorded: 2026-10-05 12:57:00 UTC (20:57:00 Asia/Shanghai). Inputs opened before this note: only `input/figure.png` and `input/caption.md`. No source SVG, project progress, protocol, scientific source or earlier acceptance was read. This is a staged procedural blind within shared storage and the same model family, not a human or independently trained-model review.

## Reconstructed mechanism

Two recent RGB frames, at t − 1 and t, go through an RGB encoder once per policy query. The resulting features join a proprioception vector q_t in a fixed condition c_t. A full length-eight action sequence starts as Gaussian noise. At each diffusion step k, the same noise predictor takes the noisy action sequence, the fixed condition and k. A scheduled update transforms the action sequence to k − 1; this repeats to produce A_t^0. The predictor may use either a temporal CNN with FiLM or a Transformer with cross-attention. The final eight predicted actions are displayed at robot times t through t + 7. The first four are executed, the last four are superseded when new observations trigger replanning at t + 4. The orange execution route goes to the environment, and a blue observation loop returns to the conditioning panel.

## Ambiguities and missing context

- q_t is visible as a symbol; the caption, rather than the diagram itself, identifies it as proprioception. Whether it contains a history or only current state is not clear.
- The alternating blue/green tiles in c_t plausibly depict combined observations and state, but their counts have no explicit semantics.
- The denoiser alternatives sit beside conditioning rather than beside the predictor box, making their relation to that box depend on reading the caption.
- The curves look smoother as denoising proceeds. This is an effective illustrative convention but does not independently establish that diffusion imposes action smoothness; the caption marks them illustrative.
- The output-to-action-strip purple route reaches the pale right-hand region first, which can briefly suggest that only the unexecuted region receives the output. The Tp bracket and caption resolve this as one whole predicted sequence.
- The execution arrow starts above the strip around its middle rather than visibly branching from its first-four region. The bracket and orange border carry most of the selection meaning.
- Training, schedule arithmetic, action units, exact architecture and warm start are absent. The caption explicitly scopes most of these out. This is sufficient for an inference overview, but not an algorithm specification.

## Paper-use, design and readability judgments

The three stacked panels establish a readable narrative: condition, denoise, execute/requery. Color separates conditioning, diffusion and execution; the action channels consistently recur in the curve plots and action groups. Panel titles are prominent, and time indices help keep robot time distinct from diffusion time. The caption prevents the illustrative horizons and scenes from being mistaken for experiment evidence.

The design is usable for a broad overview at the supplied large image size. Its many labels and long return path demand close reading, and the spatial placement of the two backbone alternatives leaves an association gap. I would not infer publication readiness from this image alone. Small-column readability, source fidelity, font handling and genuine semantic editability need separate checks. The caption is relatively long but carries essential scope qualifications.

## Calls and effort to this point

One orchestration call opened the image and read the caption, then obtained a timestamp. No image generation, network calls or native editor interactions occurred. API monetary cost is not exposed by these tools; it cannot be stated as zero. The judgment above precedes source and prior-self-assessment exposure.
