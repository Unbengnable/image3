# Direct vector arm: design decision

Written before the first SVG, 2026-10-05 12:58 UTC. Central message: removing twelve of sixteen image patches makes the encoder sparse; the decoder restores the sixteen spatial positions using four encoded visible patches and twelve learned mask tokens, and masked pixels alone receive reconstruction loss.

Scope is MAE pre-training, with the frozen 4 × 4 toy example. The figure contains the image, visible patch IDs, encoder, encoded representations, restored decoder inputs, lightweight decoder, predicted image, masked loss locations and a separate target route. The caption explains positional embeddings, the shared mask token, toy resolution, random sampling, schematic reconstruction and omissions. No downstream task or measured model output appears.

The independently selected subject is a mountain lake with sun, shoreline and a pine tree. Native editable paths provide recognizable spatial content. Small crops explicitly carry the retained parts of that scene into the encoder. Blue blocks represent encoded visible patches; neutral blocks marked M represent auxiliary tokens. The decoder's input is a spatial grid, distinct from the sparse set. Orange outlines on predicted patches show the masked loss domain.

Independent layout: a single horizontal transformation chain across the upper part of the page, with a target-only supervision route below it. A compact spatial grid is used only where position matters. The large encoder and smaller decoder use different footprints without asserting a numeric capacity ratio. This layout was chosen from the method packet and abstract principles, with no reference image, old case figure, target paper image or other arm inspected.

Physical dimensions are 178 × 82 mm; SVG viewBox 0 0 1780 820. Main labels are 27–30 units (about 7.65–8.50 pt); small patch IDs are 23 units (about 6.52 pt). The 300 dpi preview is 2102 × 968 pixels, with PNG density metadata. Required semantic counts are 16 positions, visible IDs 1, 6, 11, 12, 12 masked, encoder 4, decoder 4 + 12, and masked loss 12.

This is a project-fresh case. No claim is made that the model has never encountered MAE or its published diagrams in training. Native editor import and reader acceptance are separate checks. Self-checks by the author do not count as acceptance.
