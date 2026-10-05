# Arm R design decision

Recorded before first artifact creation. Active work begins 2026-10-05T12:57:45Z (approximate first task read); machine timestamp below is authoritative for registration.

Central message: sparse image evidence enters the encoder; spatial mask tokens enter only downstream; the loss is restricted spatially to masked image pixels.

Scope: MAE pre-training, toy 4 by 4 spatial patches. Four visible positions 1, 6, 11, 12; twelve removed. Omit downstream use, benchmarks and normalized-pixel variant.

Representation: a recognizable sailboat/island/water illustration with patch transformations. Retain independently cropped generated illustration only; reconstruct text, spatial masks, exact patch positions, token counts, blocks, arrows and loss domain as native SVG. A raster candidate is visual material, never scientific authority.

Layout: independently chosen connected two-band pathway. Intact and masked images occupy the upper left; sparse image evidence flows upper right to encoder. Decoder mechanism returns along lower band toward prediction and spatial loss. Original target has its own loss branch. Caption holds explanations and caveats.

Physical size: 178 mm main width; 300 dpi PNG 2102 pixels wide. SVG type targets around 7 to 9 pt at that size. No 85 mm deliverable is required here.

Reference exposure: only common/reference-principles.txt; no source pixels, old figure outputs, target figure or other arm inspected. Model prior knowledge cannot be quantified.

Budget: one generation, optional one own-image edit, one SVG draft plus at most one consolidated content revision and up to two syntax/render repairs; then semantic edit on separate copy.
