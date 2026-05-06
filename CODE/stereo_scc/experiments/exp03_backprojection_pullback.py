"""exp03: Backprojection + pullback round-trip (Claim C).

Claim C: The partial map b_t (backproject) + pullback u_L^pix = u_t(b_t(x))
correctly reconstructs the 3D cohesion field at valid pixels and assigns NaN
at pixels without depth estimates.

Saves: results/exp03/{roundtrip_error.csv, field_3d.png, field_pullback.png, summary.md}
"""
from __future__ import annotations

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import numpy as np
import csv

from stereo_scc.stereo_geometry import (
    depth_from_disparity,
    backproject_pixels,
    pullback_field_to_pixels,
)
from stereo_scc.visualization import save_field_image

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "exp03")


def run():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    rng = np.random.default_rng(1)

    H, W = 16, 16
    n_pixels = H * W

    # Camera intrinsics (simple pinhole)
    f = 500.0  # focal length in pixels
    cx, cy = W / 2.0, H / 2.0
    K_cam = np.array([[f, 0, cx],
                      [0, f, cy],
                      [0, 0, 1.0]])

    # Disparity field: valid in center, invalid (zero) at borders
    disparity = np.zeros((H, W), dtype=np.float64)
    disparity[3:13, 3:13] = 5.0 + rng.uniform(-0.5, 0.5, (10, 10))
    # Disparity=0 at borders -> depth=inf -> invalid

    depth = depth_from_disparity(disparity, focal_length=f, baseline=0.12)

    # Pixel coordinates (u=col, v=row) for all pixels
    rows_idx, cols_idx = np.meshgrid(np.arange(H), np.arange(W), indexing="ij")
    pixels_uv = np.stack([cols_idx.ravel(), rows_idx.ravel()], axis=1).astype(np.float64)

    confidence = np.where(disparity.ravel() > 0, 1.0, 0.0)

    points_3d, valid_mask = backproject_pixels(
        pixels_uv, depth.ravel(), K_cam,
        confidence=confidence, min_confidence=0.5,
    )

    n_valid = valid_mask.sum()
    n_invalid = (~valid_mask).sum()

    # Assign a synthetic 3D cohesion field based on proximity to 3D centroid
    centroid = points_3d.mean(axis=0)
    dists = np.linalg.norm(points_3d - centroid, axis=1)
    u_3d = np.exp(-dists / dists.max())

    # Pull back to pixel space
    valid_indices = np.where(valid_mask)[0]
    u_pix = pullback_field_to_pixels(u_3d, valid_indices, n_pixels)

    # Verify: valid pixels have finite values, invalid pixels have NaN
    n_valid_finite = np.isfinite(u_pix[valid_indices]).sum()
    n_invalid_nan = np.isnan(u_pix[~valid_mask]).sum()

    # Round-trip error at valid pixels: u_pix[valid_indices] should equal u_3d
    roundtrip_error = np.abs(u_pix[valid_indices] - u_3d).max()

    # Save CSV
    csv_path = os.path.join(RESULTS_DIR, "roundtrip_error.csv")
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["metric", "value"])
        writer.writerow(["n_pixels", n_pixels])
        writer.writerow(["n_valid_backprojected", n_valid])
        writer.writerow(["n_invalid_pixels", n_invalid])
        writer.writerow(["n_valid_finite_after_pullback", n_valid_finite])
        writer.writerow(["n_invalid_nan_after_pullback", n_invalid_nan])
        writer.writerow(["max_roundtrip_error", f"{roundtrip_error:.2e}"])

    # Save field images
    u_pix_display = np.where(np.isfinite(u_pix), u_pix, 0.0)
    save_field_image(
        u_pix_display, (H, W),
        filename=os.path.join(RESULTS_DIR, "field_pullback.png"),
        title="exp03: Pulled-back cohesion field u_L^pix",
        vmin=0.0, vmax=1.0,
    )

    valid_field_img = valid_mask.astype(np.float64)
    save_field_image(
        valid_field_img, (H, W),
        filename=os.path.join(RESULTS_DIR, "valid_mask.png"),
        title="exp03: Valid pixel mask (b_t domain)",
        vmin=0.0, vmax=1.0,
    )

    # Claim C checks
    correct_valid = (n_valid_finite == n_valid)
    correct_invalid = (n_invalid_nan == n_invalid)
    roundtrip_ok = (roundtrip_error < 1e-10)
    claim_c = correct_valid and correct_invalid and roundtrip_ok
    status = "SUPPORTED" if claim_c else "NOT SUPPORTED"

    summary = f"""# exp03: Backprojection + Pullback Round-Trip (Claim C)

## Setup

- Image size: {H}x{W} = {n_pixels} pixels
- Valid disparity region: rows 3-12, cols 3-12 (center patch)
- Camera: f={f}, baseline=0.12m

## Results

| Metric | Value |
|---|---|
| Valid pixels backprojected | {n_valid} |
| Invalid pixels (NaN depth) | {n_invalid} |
| Valid pixels with finite u_pix | {n_valid_finite} |
| Invalid pixels with NaN u_pix | {n_invalid_nan} |
| Max round-trip error | {roundtrip_error:.2e} |

## Claim C

b_t pullback correctly maps u_3d to pixel space (identity at valid pixels,
NaN at invalid pixels).

Status: **{status}**

Notes:
- correct_valid={correct_valid}, correct_invalid={correct_invalid}
- roundtrip_error={roundtrip_error:.2e} (expected < 1e-10)
"""
    with open(os.path.join(RESULTS_DIR, "summary.md"), "w") as f:
        f.write(summary)

    print(f"[exp03] valid={n_valid}, invalid={n_invalid}, "
          f"roundtrip_err={roundtrip_error:.2e} => {status}")


if __name__ == "__main__":
    run()
