> [!nav] Linked: [[MOC_experiments_validation]] · [[THEORY_INDEX]]

# exp02: Stereo Merger Barrier (Claim T5 / Claim B)

## Setup

- Grid: 20x20 (n=400)
- Depth discontinuity: left half z=1.0, right half z=3.0
- K=2 field: two Gaussian blobs separated by depth boundary
- alpha=1.0, beta=4.0

## Results

| Condition | Merger barrier | K_act |
|---|---|---|
| Flat 2D | 2.965868 | 1 |
| Stereo (depth-filtered) | 2.973775 | 2 |
| Ratio (stereo/flat) | 1.0027 | — |

## Claim B

Depth-filtered adjacency raises the merger barrier relative to flat 2D.

Status: **SUPPORTED**

Notes:
- barrier_stereo=2.973775 vs barrier_flat=2.965868
- ratio=1.0027 (>1 means stereo stabilizes; <1 means anomaly)
- This is a toy linear-interpolation barrier (not true saddle-point NEB)
