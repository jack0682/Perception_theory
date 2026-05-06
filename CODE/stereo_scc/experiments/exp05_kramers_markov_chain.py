"""exp05: K_act Markov chain and stationary distribution (Claim E).

Claim E: The K_act Markov jump process (Kramers rates, Gillespie sim) has a
well-defined stationary distribution. At low T_star (N-1 asymmetry) the chain
concentrates near K=1 (merger-dominant). At high T_star it spreads over K.

Saves: results/exp05/{stationary_dist.csv, markov_trajectory_*.png,
        free_energy_*.png, summary.md}
"""
from __future__ import annotations

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import numpy as np
import csv

from stereo_scc.kramers import (
    build_rate_matrix,
    simulate_markov_chain,
    stationary_distribution,
    free_energy_from_barriers,
)
from stereo_scc.visualization import save_markov_trajectory, save_free_energy_curve

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "exp05")

K_MAX = 5  # states K = 0..5


def make_barriers(K_max: int, E0_down: float = 0.5, E0_up: float = 1.5) -> tuple:
    """Asymmetric barriers: up >> down (N-1 merger dominance)."""
    barriers_down = np.full(K_max, E0_down)
    barriers_up = np.full(K_max, E0_up)
    return barriers_down, barriers_up


def run():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    barriers_down, barriers_up = make_barriers(K_MAX)

    T_star_values = [0.2, 0.5, 1.0, 2.0]
    rows_csv = [["T_star"] + [f"pi_K={k}" for k in range(K_MAX + 1)] + ["K_mode"]]

    for T_star in T_star_values:
        Q = build_rate_matrix(barriers_down, barriers_up, T_star)
        pi = stationary_distribution(Q)
        K_mode = int(np.argmax(pi))
        rows_csv.append([f"{T_star:.2f}"] + [f"{p:.4f}" for p in pi] + [str(K_mode)])

        # Simulate trajectory
        rng = np.random.default_rng(42)
        times, states = simulate_markov_chain(Q, K_init=K_MAX, t_max=200.0, rng=rng)
        save_markov_trajectory(
            times, states,
            filename=os.path.join(RESULTS_DIR, f"markov_traj_T{T_star:.1f}.png"),
            K_max=K_MAX,
            title=f"exp05: K_act(t) trajectory — T*={T_star}",
        )

        # Free energy
        F_rel = free_energy_from_barriers(barriers_down, barriers_up, T_star)
        K_values = np.arange(K_MAX + 1)
        save_free_energy_curve(
            K_values, F_rel,
            filename=os.path.join(RESULTS_DIR, f"free_energy_T{T_star:.1f}.png"),
            T_star=T_star,
            title="exp05: Effective free energy F(K)",
        )

    # Save CSV
    csv_path = os.path.join(RESULTS_DIR, "stationary_dist.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows_csv)

    # Claim E: at low T_star, pi concentrates at low K (K=1 or K=0)
    Q_low = build_rate_matrix(barriers_down, barriers_up, T_star=0.2)
    pi_low = stationary_distribution(Q_low)
    low_T_concentrates = pi_low[:2].sum() > 0.7  # most mass at K=0 or K=1

    Q_high = build_rate_matrix(barriers_down, barriers_up, T_star=2.0)
    pi_high = stationary_distribution(Q_high)
    high_T_spreads = pi_high.max() < 0.5  # no single dominant state

    claim_e = low_T_concentrates and high_T_spreads
    status = "SUPPORTED" if claim_e else "NOT SUPPORTED"

    # Detailed stationary distributions for summary
    dist_lines = []
    for T_star in T_star_values:
        Q = build_rate_matrix(barriers_down, barriers_up, T_star)
        pi = stationary_distribution(Q)
        K_mode = int(np.argmax(pi))
        dist_lines.append(f"| T*={T_star:.2f} | {' | '.join(f'{p:.3f}' for p in pi)} | K_mode={K_mode} |")

    summary = f"""# exp05: K_act Markov Chain Stationary Distribution (Claim E)

## Setup

- K_max = {K_MAX}
- barriers_down = {barriers_down[0]:.2f} (uniform; K->K-1 merger)
- barriers_up = {barriers_up[0]:.2f} (uniform; K->K+1 birth)
- Asymmetry: E_up >> E_down => merger-dominant at low T*
- Gillespie simulation, t_max=200, K_init={K_MAX}

## Stationary Distributions pi(K)

| T* | {' | '.join(f'K={k}' for k in range(K_MAX+1))} | K_mode |
|---|{'---|' * (K_MAX+2)}
{chr(10).join(dist_lines)}

## Claim E

At low T* (N-1 asymmetry), K_act concentrates at low K (merger-dominant).
At high T*, distribution spreads over K values.

Status: **{status}**

Notes:
- low_T_concentrates (pi_low[K<=1] > 0.7): {low_T_concentrates}
  pi_low = [{', '.join(f'{p:.3f}' for p in pi_low)}]
- high_T_spreads (pi_high.max < 0.5): {high_T_spreads}
  pi_high = [{', '.join(f'{p:.3f}' for p in pi_high)}]

P-F flag: T_star undefined until P-F-A1 Langevin on F_M(P) is formalized.
"""
    with open(os.path.join(RESULTS_DIR, "summary.md"), "w") as f:
        f.write(summary)

    print(f"[exp05] low_T concentrates={low_T_concentrates}, high_T spreads={high_T_spreads} => {status}")


if __name__ == "__main__":
    run()
