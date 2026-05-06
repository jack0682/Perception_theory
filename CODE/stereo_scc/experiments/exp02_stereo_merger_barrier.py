"""exp02: Stereo geometry raises merger barriers (Claim T5).

Claim B: Depth-filtered adjacency (stereo) produces a higher merger barrier
than flat 2D adjacency (monocular), for a K=2 formation with a depth
discontinuity between the two blobs.

Saves: results/exp02/{barriers.csv, barrier_comparison.png, summary.md}
"""
from __future__ import annotations

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import numpy as np
import csv

from stereo_scc.fields import make_grid_2d, make_depth_separated_grid, gaussian_field, normalize_field, laplacian_from_adj
from stereo_scc.energies import stereo_barrier_comparison, find_local_minimum
from stereo_scc.topology import persistent_component_count
from stereo_scc.visualization import save_barrier_comparison, save_field_image

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "exp02")


def run():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    rows, cols = 20, 20
    n = rows * cols
    grid_shape = (rows, cols)

    # Flat adjacency (no depth awareness)
    adj_flat, _ = make_grid_2d(rows, cols, weight=1.0)

    # Depth map: left blob at depth 1.0, right blob at depth 3.0 (large discontinuity)
    depth_map = np.ones((rows, cols), dtype=np.float64)
    depth_map[:, cols // 2:] = 3.0  # right half = far depth

    # Stereo (depth-filtered) adjacency
    adj_stereo, _ = make_depth_separated_grid(rows, cols, depth_map=depth_map, delta_z=0.5)

    # Blobs placed adjacent to the boundary (col=10) so the cross-boundary
    # gradient is large; removing those edges has a measurable effect on energy
    u_init = gaussian_field(n, centers=[(10, 7), (10, 13)], sigma=2.0, height=0.85,
                            grid_shape=grid_shape)
    u_init = normalize_field(u_init, M=float(u_init.sum()))

    # Relax to local minimum under flat Laplacian
    L_flat = laplacian_from_adj(adj_flat)
    u_K = find_local_minimum(u_init, L_flat, alpha=1.0, beta=4.0)

    # Compare barriers
    result = stereo_barrier_comparison(adj_flat, adj_stereo, u_K, alpha=1.0, beta=4.0)
    barrier_flat = result["barrier_flat"]
    barrier_stereo = result["barrier_stereo"]
    ratio = result["ratio"]

    # Check K_act under each adjacency
    K_flat = persistent_component_count(adj_flat, u_K, rho_pers=0.05)
    K_stereo = persistent_component_count(adj_stereo, u_K, rho_pers=0.05)

    # Save CSV
    csv_path = os.path.join(RESULTS_DIR, "barriers.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["condition", "barrier", "K_act"])
        writer.writerow(["flat_2d", f"{barrier_flat:.6f}", K_flat])
        writer.writerow(["stereo_depth_filtered", f"{barrier_stereo:.6f}", K_stereo])
        writer.writerow(["ratio_stereo_flat", f"{ratio:.4f}", ""])

    # Save bar chart
    save_barrier_comparison(
        labels=["Flat 2D", "Stereo (depth-filtered)"],
        barriers=[barrier_flat, barrier_stereo],
        filename=os.path.join(RESULTS_DIR, "barrier_comparison.png"),
        title="exp02: Merger barrier — flat vs stereo",
    )

    # Save field image
    save_field_image(
        u_K, grid_shape,
        filename=os.path.join(RESULTS_DIR, "field_u_K.png"),
        title="exp02: K=2 cohesion field (relaxed under flat L)",
    )

    # Claim B: stereo barrier > flat barrier
    claim_b = barrier_stereo > barrier_flat
    status = "SUPPORTED" if claim_b else "NOT SUPPORTED"

    summary = f"""# exp02: Stereo Merger Barrier (Claim T5 / Claim B)

## Setup

- Grid: {rows}x{cols} (n={n})
- Depth discontinuity: left half z=1.0, right half z=3.0
- K=2 field: two Gaussian blobs separated by depth boundary
- alpha=1.0, beta=4.0

## Results

| Condition | Merger barrier | K_act |
|---|---|---|
| Flat 2D | {barrier_flat:.6f} | {K_flat} |
| Stereo (depth-filtered) | {barrier_stereo:.6f} | {K_stereo} |
| Ratio (stereo/flat) | {ratio:.4f} | — |

## Claim B

Depth-filtered adjacency raises the merger barrier relative to flat 2D.

Status: **{status}**

Notes:
- barrier_stereo={barrier_stereo:.6f} vs barrier_flat={barrier_flat:.6f}
- ratio={ratio:.4f} (>1 means stereo stabilizes; <1 means anomaly)
- This is a toy linear-interpolation barrier (not true saddle-point NEB)
"""
    with open(os.path.join(RESULTS_DIR, "summary.md"), "w") as f:
        f.write(summary)

    print(f"[exp02] barrier_flat={barrier_flat:.4f}, barrier_stereo={barrier_stereo:.4f}, "
          f"ratio={ratio:.3f} => {status}")


if __name__ == "__main__":
    run()
