# MAE scientific packet

Source: Kaiming He et al., Masked Autoencoders Are Scalable Vision Learners, arXiv:2111.06377v3, Section 3 Approach. https://arxiv.org/html/2111.06377v3#S3

Scope: pre-training only. Partition an image into non-overlapping patches; randomly retain some. Embed retained patches with positions and encode only those. Mask tokens are absent from the encoder. Decoder input combines encoded visible patches with shared learned mask tokens, restores spatial order and adds decoder positional embeddings. A lightweight decoder predicts patch pixels. Compare predictions with original pixels using MSE only at masked positions. The original image is a supervision target, not a source of hidden pixels for the encoder. Downstream recognition, benchmarks and normalized-pixel variants are omitted.

Toy counts, not model resolution: 4x4 = 16 positions, numbered row-major 1..16. Visible positions: 1, 6, 11, 12. Twelve positions masked (75%). Exactly four visible patch representations reach the encoder. Four encoded visible representations plus twelve mask tokens form the decoder's sixteen positions. Restore positions consistently, then predict sixteen patch outputs; twelve participate in loss. Shared mask-token values can differ in position after adding positional embeddings. Encoder and decoder positional embeddings need not be identical.

The image, mask sample and reconstruction are schematic. Do not imply real model inference, measured reconstruction quality, perfect recovery or benchmark performance. Optional loss notation: mean over masked positions of squared pixel reconstruction error. The decoder is smaller than the encoder by design; do not invent a numeric size or speedup.
