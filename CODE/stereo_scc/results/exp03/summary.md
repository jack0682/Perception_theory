# exp03: Backprojection + Pullback Round-Trip (Claim C)

## Setup

- Image size: 16x16 = 256 pixels
- Valid disparity region: rows 3-12, cols 3-12 (center patch)
- Camera: f=500.0, baseline=0.12m

## Results

| Metric | Value |
|---|---|
| Valid pixels backprojected | 100 |
| Invalid pixels (NaN depth) | 156 |
| Valid pixels with finite u_pix | 100 |
| Invalid pixels with NaN u_pix | 156 |
| Max round-trip error | 0.00e+00 |

## Claim C

b_t pullback correctly maps u_3d to pixel space (identity at valid pixels,
NaN at invalid pixels).

Status: **SUPPORTED**

Notes:
- correct_valid=True, correct_invalid=True
- roundtrip_error=0.00e+00 (expected < 1e-10)
