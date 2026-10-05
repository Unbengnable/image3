# MAE source and semantic check before reference exposure

Reader-first was saved before mapping and source inspection. Route map: X is arm-vector; Y is arm-raster. Shared packet and preserved original Section 3 were read at 2026-10-05 13:11:10 UTC. Native main SVGs and edit SVGs, rendered edit PNGs and edit captions were then inspected before any reference or target figure image.

## Scientific audit

Original Section 3 supports random removal of image patches, encoding only visible tokens with encoder positions, post-encoder shared mask-token insertion and unshuffling, decoder positions, a lightweight decoder, patch-pixel prediction and masked-only MSE. The packet fixes the illustrative 16-slot example. Both mains show visible IDs {1,6,11,12}, exactly four encoder inputs/latents, twelve post-encoder mask slots and sixteen restored/predicted positions. Their loss-marked IDs are the complement {2,3,4,5,7,8,9,10,13,14,15,16}. No hidden image pixels or mask tokens have an edge into the encoder. The original-image branch terminates at loss/target, not inference.

X source uses crop symbols with the correct row-major viewBoxes and native landscape geometry. Its decoder slot translations and twelve loss-outline positions match the IDs. Y source uses two local embedded scene illustrations and editable scene uses, blanking rectangles, per-position outlines, token rectangles, native labels and routes. Its visible/removed/latent/restored/prediction/target IDs agree. A full-grid image is not used to carry the diagram's text or scientific geometry. Each caption appropriately limits reconstructions and toy counts; neither makes measured accuracy or resolution claims.

The original text describes prediction of masked patches and masked-only loss. The packet explicitly asks sixteen patch outputs; this is consistent with the source's full decoder token sequence and patch projection, provided visible outputs are excluded from loss, as both figures do. Both abstract Transformer block structure and exact shuffle implementation; the restoration positions preserve their operative semantics. No hard source contradiction was found within stated pre-training scope.

## Separate 50% semantic edits

Both edit copies retain visible IDs {1,3,6,8,9,11,12,14}, eight encoder patch inputs/latents, eight masks and sixteen restored/output slots. Loss-marked complement is {2,4,5,7,10,13,15,16}. Native data attributes and visual spatial positions agree. Captions and 50% / 8-visible / 8-mask / 8-loss labels agree. Source-scene assets, overall main routes and compositions remain the same. The rendered copies have no observed clipping or mistaken loss region. Y uses narrower visible crop frames to fit eight; they distort crop aspect in display, which is a visual limitation, but do not change source IDs or permit hidden encoder pixels. X uses eight separate native crop symbols and a longer latent column.

## Physical and editable structure

X: 178 by 82 mm, viewBox 1780 by 820. Body 27 units = 7.65 pt; small text 23 = 6.52 pt; headers 30 = 8.50 pt. Latent subscripts explicitly use 18 = 5.10 pt. Native texts: 51 main / 63 edit. Embedded images: zero. Shared scene and crop symbols are editable vector geometry, not raster text.

Y: 178 by 99.68 mm, viewBox 1000 by 560. Body 14 units = 7.06 pt; small/index/token text 12 = 6.05 pt; headers 16 = 8.07 pt. Native texts: 114 main / 122 edit. Embedded images: two scene crops, with diagram geometry/text native. Embedded scene illustration internals remain raster; scientific partitions and routes are editable. Main PNGs were supplied at 300 dpi; final metadata and native import/export are pending reviewer checks.

Science finding before reference/provenance exposure: PASS for both delivered CairoSVG main SVG views and separate semantic copies. Visual substance: PASS for both at overview level; the landscape/sailboat content, selection crops and spatial loss markers carry method information. Design economy differs by representation rather than constituting a box-only failure. Human physical readability and originality remained pending at this point.

## Later native cross-renderer finding

At 13:14:03 UTC the Inkscape 1.4.4 CLI plain-SVG saves and exports had completed and were inspected. BOTH candidates failed visual compatibility: selected-patch scene uses overflow their crop viewports and render large overlapping full scenes across the encoder-input area. At 13:15:19 UTC direct PNG export of the original copies reproduced the same defect byte-for-byte as the roundtrip PNG for each arm, isolating it from a save-only change. Texts and scene-image counts remain intact, but object counts cannot rescue the broken visual mechanism. Native crop clipping/viewport behavior needs a future repair and cross-renderer recheck. No repair was attempted in this frozen batch. Interactive editing remains NOT_TESTED.

Original supplied main previews have 299.9994 dpi readback: X 2102 by 968 px; Y 2102 by 1177 px. Both semantic-copy previews match their main dimensions/DPI. The native failure is recorded separately from source-scope science in the delivered CairoSVG view.
