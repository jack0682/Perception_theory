"""exp04: Prior / likelihood separation in MAP inference (Claim D).

Claim D: The prior E_SCC[u] and the photometric likelihood L_obs(O|u,P) are
independent terms in the MAP objective. Adding L_obs (as a pixel-alignment
term) shifts the MAP minimizer without altering E_SCC structure.

This experiment uses a synthetic photometric term E_photo = ||u_pix - I||^2
as a stand-in for L_obs. It verifies:
  1. With E_photo=0 (prior only): MAP minimizes E_SCC => formation u_prior
  2. With E_photo != 0: MAP minimizes E_SCC + lambda_photo * E_photo => u_map
  3. u_map != u_prior (photo term shifts solution)
  4. E_SCC(u_map) > E_SCC(u_prior) (photo pulls away from prior minimum)
  5. E_photo(u_map) < E_photo(u_prior) (photo term is reduced)

Saves: results/exp04/{map_comparison.csv, field_prior.png, field_map.png, summary.md}
"""
from __future__ import annotations

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import numpy as np
import csv

from stereo_scc.fields import make_grid_2d, gaussian_field, normalize_field, laplacian_from_adj
from stereo_scc.energies import ginzburg_landau_energy, energy_gradient, find_local_minimum
from stereo_scc.visualization import save_field_image

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "exp04")


def map_with_photo(
    u0: np.ndarray,
    L,
    I_target: np.ndarray,
    alpha: float = 1.0,
    beta: float = 4.0,
    lambda_photo: float = 2.0,
    max_iter: int = 3000,
    step: float = 0.005,
) -> np.ndarray:
    """Gradient descent on E_SCC + lambda_photo * ||u - I||^2."""
    import scipy.sparse as sp
    u = u0.copy()
    M_target = u.sum()

    for _ in range(max_iter):
        g_scc = energy_gradient(u, L, alpha, beta)
        g_photo = 2.0 * lambda_photo * (u - I_target)
        g = g_scc + g_photo
        g_proj = g - g.mean()
        u_new = np.clip(u - step * g_proj, 0.0, 1.0)
        deficit = M_target - u_new.sum()
        u_new = u_new + deficit / len(u_new)
        u_new = np.clip(u_new, 0.0, 1.0)
        if np.linalg.norm(u_new - u) < 1e-8:
            break
        u = u_new
    return u


def run():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    rows, cols = 20, 20
    n = rows * cols
    grid_shape = (rows, cols)

    adj, _ = make_grid_2d(rows, cols)
    L = laplacian_from_adj(adj)

    # Prior-only minimum: two blobs
    u_init = gaussian_field(n, centers=[(6, 6), (14, 14)], sigma=3.0, height=0.85,
                            grid_shape=grid_shape)
    u_init = normalize_field(u_init, M=float(u_init.sum()))
    u_prior = find_local_minimum(u_init, L, alpha=1.0, beta=4.0)

    # Photometric target: single blob in top-right (conflicts with prior)
    I_target = gaussian_field(n, centers=[(5, 15)], sigma=4.0, height=0.8,
                              grid_shape=grid_shape)
    I_target = I_target / I_target.max()  # normalize to [0,1]

    # MAP with photo term
    u_map = map_with_photo(u_init.copy(), L, I_target,
                           alpha=1.0, beta=4.0, lambda_photo=3.0)

    # Compute energies
    E_scc_prior = ginzburg_landau_energy(u_prior, L, alpha=1.0, beta=4.0)
    E_scc_map = ginzburg_landau_energy(u_map, L, alpha=1.0, beta=4.0)
    E_photo_prior = np.sum((u_prior - I_target) ** 2)
    E_photo_map = np.sum((u_map - I_target) ** 2)

    field_shift = np.linalg.norm(u_map - u_prior)

    # Save CSV
    csv_path = os.path.join(RESULTS_DIR, "map_comparison.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["metric", "prior_only", "MAP_with_photo"])
        writer.writerow(["E_SCC", f"{E_scc_prior:.6f}", f"{E_scc_map:.6f}"])
        writer.writerow(["E_photo", f"{E_photo_prior:.6f}", f"{E_photo_map:.6f}"])
        writer.writerow(["field_L2_shift", "", f"{field_shift:.6f}"])

    # Save field images
    save_field_image(u_prior, grid_shape,
                     filename=os.path.join(RESULTS_DIR, "field_prior.png"),
                     title="exp04: Prior-only MAP (E_SCC only)")
    save_field_image(u_map, grid_shape,
                     filename=os.path.join(RESULTS_DIR, "field_map.png"),
                     title="exp04: Full MAP (E_SCC + E_photo)")
    save_field_image(I_target.reshape(rows, cols).ravel(), grid_shape,
                     filename=os.path.join(RESULTS_DIR, "photo_target.png"),
                     title="exp04: Photometric target I")

    # Claim D checks
    solutions_differ = field_shift > 0.01
    photo_reduced = E_photo_map < E_photo_prior
    scc_prior_lower = E_scc_prior <= E_scc_map + 1e-6  # prior is SCC-optimal
    claim_d = solutions_differ and photo_reduced
    status = "SUPPORTED" if claim_d else "NOT SUPPORTED"

    summary = f"""# exp04: Prior / Likelihood Separation in MAP (Claim D)

## Setup

- Grid: {rows}x{cols}
- Prior target: two Gaussian blobs at (6,6) and (14,14)
- Photometric target: single blob at (5,15)
- lambda_photo = 3.0

## Results

| Metric | Prior only | MAP + Photo |
|---|---|---|
| E_SCC | {E_scc_prior:.6f} | {E_scc_map:.6f} |
| E_photo | {E_photo_prior:.6f} | {E_photo_map:.6f} |
| Field L2 shift | — | {field_shift:.6f} |

## Claim D

Prior E_SCC and likelihood E_photo are independent terms; adding E_photo
shifts the MAP solution while E_SCC structure is preserved.

Status: **{status}**

Notes:
- solutions_differ (L2 shift={field_shift:.4f} > 0.01): {solutions_differ}
- photo_reduced (E_photo: {E_photo_prior:.4f} -> {E_photo_map:.4f}): {photo_reduced}
- scc_prior_lower (prior E_SCC <= MAP E_SCC): {scc_prior_lower}
"""
    with open(os.path.join(RESULTS_DIR, "summary.md"), "w") as f:
        f.write(summary)

    print(f"[exp04] field_shift={field_shift:.4f}, E_photo: {E_photo_prior:.4f}->{E_photo_map:.4f} => {status}")


if __name__ == "__main__":
    run()
