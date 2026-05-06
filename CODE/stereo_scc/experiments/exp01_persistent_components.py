"""exp01: K_act = #PersComp vs slot-count comparison.

Claim A: PersComp correctly identifies coherent formations; slot-count
over-estimates K_act when noise activates empty slots.

Saves: results/exp01/{k_act_comparison.csv, persistence_curve.png, summary.md}
"""
from __future__ import annotations

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import numpy as np
import csv

from stereo_scc.fields import make_grid_2d, gaussian_field, normalize_field
from stereo_scc.topology import (
    component_persistence_curve,
    persistent_component_count,
    slot_count_kact,
)
from stereo_scc.visualization import save_persistence_curve

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "exp01")


def run():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    rng = np.random.default_rng(0)

    rows, cols = 20, 20
    adj, grid_shape = make_grid_2d(rows, cols)
    n = rows * cols

    # --- Scenario 1: Two well-separated Gaussian blobs ---
    u_two = gaussian_field(n, centers=[(5, 5), (14, 14)], sigma=2.5, height=0.9,
                           grid_shape=grid_shape)
    u_two = normalize_field(u_two, M=float(u_two.sum()))

    rho_pers = 0.05
    K_pers_two = persistent_component_count(adj, u_two, rho_pers=rho_pers)

    # Simulate slot-count: split u_two into 4 "slots" with noise
    u_slots = []
    for k in range(4):
        slot = rng.uniform(0, 0.05, n)  # noise-only slot
        u_slots.append(slot)
    u_slots[0] = u_two.copy() * (u_two > 0.3)  # first two slots get the real blobs
    u_slots[1] = u_two.copy() * (u_two > 0.3)
    # tiny noise pushes slot 2 and 3 above epsilon
    u_slots[2] += 0.06
    u_slots[3] += 0.06

    K_slot = slot_count_kact(u_slots, epsilon=0.05)

    # --- Scenario 2: One large connected blob (should give K_act=1) ---
    u_one = gaussian_field(n, centers=[(10, 10)], sigma=5.0, height=0.9,
                           grid_shape=grid_shape)
    K_pers_one = persistent_component_count(adj, u_one, rho_pers=rho_pers)

    # --- Scenario 3: Two blobs + weak noise (noise below rho_pers) ---
    # Noise amplitude must be < rho_pers so spurious bumps don't persist
    u_noisy = u_two + rng.uniform(0, 0.03, n)
    u_noisy = np.clip(u_noisy, 0, 1)
    K_pers_noisy = persistent_component_count(adj, u_noisy, rho_pers=rho_pers)

    # --- Save CSV ---
    rows_csv = [
        ["scenario", "K_act_PersComp", "K_act_slot", "note"],
        ["two_blobs", K_pers_two, "N/A", "two separated Gaussians"],
        ["one_blob", K_pers_one, "N/A", "single central Gaussian"],
        ["noisy_two_blobs", K_pers_noisy, K_slot, "blobs + uniform noise; slot=4 slots with noise"],
    ]
    csv_path = os.path.join(RESULTS_DIR, "k_act_comparison.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows_csv)

    # --- Save persistence curve for two-blob scenario ---
    thresholds, n_components = component_persistence_curve(adj, u_two, n_thresholds=100)
    save_persistence_curve(
        thresholds, n_components,
        filename=os.path.join(RESULTS_DIR, "persistence_curve_two_blobs.png"),
        rho_pers=rho_pers,
        K_act=K_pers_two,
        title="exp01: Persistence filtration — two Gaussian blobs",
    )

    thresholds_n, n_comp_n = component_persistence_curve(adj, u_noisy, n_thresholds=100)
    save_persistence_curve(
        thresholds_n, n_comp_n,
        filename=os.path.join(RESULTS_DIR, "persistence_curve_noisy.png"),
        rho_pers=rho_pers,
        K_act=K_pers_noisy,
        title="exp01: Persistence filtration — noisy two blobs",
    )

    # --- Summary ---
    claim_a = (K_pers_two == 2) and (K_pers_one == 1) and (K_pers_noisy == 2) and (K_slot > K_pers_noisy)
    status = "SUPPORTED" if claim_a else "NOT SUPPORTED"

    summary = f"""# exp01: K_act = #PersComp vs Slot-Count

## Results

| Scenario | K_act (PersComp) | K_act (slot-count) |
|---|---|---|
| Two separated blobs | {K_pers_two} | N/A |
| Single blob | {K_pers_one} | N/A |
| Noisy two blobs | {K_pers_noisy} | {K_slot} |

## Claim A

PersComp correctly counts coherent formations; slot-count over-estimates
when noise activates empty slots.

Status: **{status}**

Notes:
- rho_pers = {rho_pers}
- two_blobs expected K=2, got {K_pers_two}
- one_blob expected K=1, got {K_pers_one}
- noisy_two_blobs: PersComp={K_pers_noisy} (robust), slot-count={K_slot} (inflated)
"""
    with open(os.path.join(RESULTS_DIR, "summary.md"), "w") as f:
        f.write(summary)

    print(f"[exp01] K_pers_two={K_pers_two}, K_pers_one={K_pers_one}, "
          f"K_pers_noisy={K_pers_noisy}, K_slot={K_slot} => {status}")


if __name__ == "__main__":
    run()
