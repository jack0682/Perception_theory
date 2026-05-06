"""
exp02b: Smooth-Adjacency NEB — T-ST-5b Regime B
Claim: Under depth-weighted edges w_ij = exp(-λ_z * |z_i - z_j|²),
barrier ΔE_stereo > ΔE_flat, increasing with Δz and λ_z.
Status target: Cat C → Cat B if monotone increase confirmed.
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import csv
import scipy.sparse as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from stereo_scc.fields import make_grid_2d, gaussian_field, normalize_field, laplacian_from_adj
from stereo_scc.topology import persistent_component_count

ROWS, COLS = 20, 20
ALPHA, BETA = 1.0, 4.0
RHO_PERS = 0.05
N_STEPS_RELAX = 2000
STEP_RELAX = 5e-4
N_IMAGES = 16
N_NEB_STEPS = 600
STEP_NEB = 0.002
K_SPRING = 1.0

RESULT_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "exp02b_smooth_neb")
os.makedirs(RESULT_DIR, exist_ok=True)

n = ROWS * COLS


# ── energy and gradient ────────────────────────────────────────────────────────

def gl_energy(u, L):
    W = (u ** 2) * ((1 - u) ** 2)
    return float(ALPHA * u @ L @ u + BETA * W.sum())


def gl_gradient(u, L):
    dW = 2 * u * (1 - u) * (1 - 2 * u)
    return 2 * ALPHA * (L @ u) + BETA * dW


def project_simplex_tangent(g, u):
    return g - g.mean()


def find_minimum(u_init, L, n_steps=N_STEPS_RELAX, step=STEP_RELAX):
    u = u_init.copy()
    m = u.sum()
    for _ in range(n_steps):
        g = gl_gradient(u, L)
        g_proj = project_simplex_tangent(g, u)
        u = u - step * g_proj
        u = np.clip(u, 0.0, 1.0)
        u = u * (m / u.sum())
    return u


# ── adjacency builders ─────────────────────────────────────────────────────────

def build_smooth_adj(rows, cols, depth_map, lambda_z):
    """4-neighbour sparse adjacency with smooth depth weighting."""
    n = rows * cols
    rows_idx, cols_idx, data = [], [], []
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr2, nc2 = r + dr, c + dc
                if 0 <= nr2 < rows and 0 <= nc2 < cols:
                    nidx = nr2 * cols + nc2
                    dz = abs(depth_map[idx] - depth_map[nidx])
                    w = float(np.exp(-lambda_z * dz ** 2))
                    rows_idx.append(idx)
                    cols_idx.append(nidx)
                    data.append(w)
    return sp.csr_matrix((data, (rows_idx, cols_idx)), shape=(n, n))


def build_flat_adj(rows, cols):
    adj, _ = make_grid_2d(rows, cols)
    return sp.csr_matrix(adj) if not sp.issparse(adj) else adj


# ── NEB / string method ────────────────────────────────────────────────────────

def neb_barrier(u_start, u_end, L, n_images=N_IMAGES, n_steps=N_NEB_STEPS,
                step=STEP_NEB, k_spring=K_SPRING):
    """String-method NEB on a connected graph."""
    images = [u_start + (u_end - u_start) * i / (n_images - 1) for i in range(n_images)]
    images = [np.clip(img, 0.0, 1.0) for img in images]
    m = u_start.sum()

    for _ in range(n_steps):
        energies = [gl_energy(img, L) for img in images]
        new_images = [images[0]]
        for i in range(1, n_images - 1):
            g = gl_gradient(images[i], L)
            tang = images[i + 1] - images[i - 1]
            tang_norm = np.linalg.norm(tang)
            if tang_norm < 1e-12:
                tang_norm = 1.0
            tang = tang / tang_norm
            g_perp = g - np.dot(g, tang) * tang
            spring = k_spring * (
                np.linalg.norm(images[i + 1] - images[i])
                - np.linalg.norm(images[i] - images[i - 1])
            ) * tang
            update = g_perp - spring
            update = project_simplex_tangent(update, images[i])
            new_img = images[i] - step * update
            new_img = np.clip(new_img, 0.0, 1.0)
            new_img = new_img * (m / new_img.sum())
            new_images.append(new_img)
        new_images.append(images[-1])
        images = new_images

    energies = [gl_energy(img, L) for img in images]
    e_start = energies[0]
    barrier = max(energies) - e_start
    return max(0.0, barrier), energies


# ── hard-bimodal initialisation ────────────────────────────────────────────────

def make_hard_bimodal(rows, cols, half_width=4):
    """Two rectangular blocks of 0.9 separated by 0s."""
    u = np.zeros(rows * cols)
    center_r = rows // 2
    col_mid = cols // 2
    for r in range(center_r - half_width, center_r + half_width):
        for c in range(col_mid // 2 - half_width, col_mid // 2 + half_width):
            if 0 <= r < rows and 0 <= c < cols:
                u[r * cols + c] = 0.9
        for c in range(col_mid + col_mid // 2 - half_width, col_mid + col_mid // 2 + half_width):
            if 0 <= r < rows and 0 <= c < cols:
                u[r * cols + c] = 0.9
    return u


def make_merged_init(rows, cols):
    """Single central Gaussian blob for K=1 target."""
    u = gaussian_field(rows * cols, [(rows // 2, cols // 2)], sigma=3.5, height=0.8,
                       grid_shape=(rows, cols))
    return np.clip(u, 0.0, 1.0)


# ── main sweep ─────────────────────────────────────────────────────────────────

def main():
    delta_z_vals = [0.25, 0.5, 1.0, 2.0]
    lambda_z_vals = [0.5, 1.0, 2.0, 4.0, 8.0]

    # flat reference
    adj_flat = build_flat_adj(ROWS, COLS)
    L_flat = laplacian_from_adj(adj_flat)
    u_flat_init = make_hard_bimodal(ROWS, COLS)
    m = u_flat_init.sum()
    u_flat_relax = find_minimum(u_flat_init, L_flat)
    k_flat = persistent_component_count(adj_flat, u_flat_relax, rho_pers=RHO_PERS)
    if k_flat == 1:
        u_merged_ref = u_flat_relax.copy()
        barrier_flat = 0.0
    else:
        u_merged_ref = find_minimum(make_merged_init(ROWS, COLS) * (m / make_merged_init(ROWS, COLS).sum()),
                                    L_flat)
        b, _ = neb_barrier(u_flat_relax, u_merged_ref, L_flat)
        barrier_flat = b

    print(f"  Flat reference: K={k_flat}, barrier={barrier_flat:.4f}")

    rows_csv = []
    for dz in delta_z_vals:
        for lz in lambda_z_vals:
            product = lz * dz ** 2
            w_bridge = np.exp(-product)

            # Build depth map: left half z=1.0, right half z=1.0+dz
            depth_map = np.ones(n)
            for idx in range(n):
                c = idx % COLS
                if c >= COLS // 2:
                    depth_map[idx] = 1.0 + dz

            adj_smooth = build_smooth_adj(ROWS, COLS, depth_map, lz)
            L_smooth = laplacian_from_adj(adj_smooth)

            u_init = make_hard_bimodal(ROWS, COLS)
            u_relax = find_minimum(u_init, L_smooth)
            k_act = persistent_component_count(adj_smooth, u_relax, rho_pers=RHO_PERS)

            if k_act <= 1:
                barrier = 0.0
                note = "K=1: no K=2 min"
            else:
                # K=2 stable: find K=1 reference under smooth adj
                u_m_init = make_merged_init(ROWS, COLS)
                u_m_init = u_m_init * (m / u_m_init.sum())
                u_merged = find_minimum(u_m_init, L_smooth)
                k_merged = persistent_component_count(adj_smooth, u_merged, rho_pers=RHO_PERS)
                if k_merged >= 2:
                    # Couldn't find K=1 — use very long relaxation from noise
                    u_noise = np.random.default_rng(99).uniform(0.01, 0.1, n)
                    u_noise = u_noise * (m / u_noise.sum())
                    u_merged = find_minimum(u_noise, L_smooth, n_steps=4000)
                    k_merged = persistent_component_count(adj_smooth, u_merged, rho_pers=RHO_PERS)

                if k_merged >= 2:
                    barrier = float("nan")
                    note = f"K=2 stable; K=1 ref not found (k_merged={k_merged})"
                else:
                    b, epath = neb_barrier(u_relax, u_merged, L_smooth)
                    barrier = b
                    note = f"NEB: {len(epath)} images"

            ratio = (barrier / barrier_flat) if (barrier_flat > 1e-10 and not np.isnan(barrier)) else float("nan")

            rows_csv.append({
                "delta_z": dz, "lambda_z": lz, "product": round(product, 4),
                "w_bridge": round(w_bridge, 6), "K_act": k_act,
                "barrier_smooth": round(barrier, 6) if not np.isnan(barrier) else "nan",
                "barrier_flat": round(barrier_flat, 6),
                "ratio_smooth_flat": round(ratio, 4) if not np.isnan(ratio) else "nan",
                "notes": note
            })
            print(f"  dz={dz:.2f} lz={lz:.1f} product={product:.2f} w={w_bridge:.4f} "
                  f"K={k_act} barrier={barrier:.4f} ratio={'nan' if np.isnan(ratio) else f'{ratio:.3f}'}")

    # Save CSV: barrier vs depth (fixed λ_z=4.0)
    lz_fixed = 4.0
    depth_rows = [r for r in rows_csv if r["lambda_z"] == lz_fixed]
    with open(os.path.join(RESULT_DIR, "barrier_vs_depth_smooth_NEB.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=depth_rows[0].keys())
        w.writeheader()
        w.writerows(depth_rows)

    # Save CSV: barrier vs lambda (fixed Δz=1.0)
    dz_fixed = 1.0
    lambda_rows = [r for r in rows_csv if r["delta_z"] == dz_fixed]
    with open(os.path.join(RESULT_DIR, "barrier_vs_lambda_smooth_NEB.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=lambda_rows[0].keys())
        w.writeheader()
        w.writerows(lambda_rows)

    # Full grid CSV
    with open(os.path.join(RESULT_DIR, "barrier_grid_smooth_NEB.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows_csv[0].keys())
        w.writeheader()
        w.writerows(rows_csv)

    # Plot: barrier vs Δz for each λ_z
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    ax = axes[0]
    for lz in lambda_z_vals:
        sub = [r for r in rows_csv if r["lambda_z"] == lz]
        xs = [r["delta_z"] for r in sub]
        ys = [float(r["barrier_smooth"]) if r["barrier_smooth"] != "nan" else np.nan for r in sub]
        ax.plot(xs, ys, marker="o", label=f"λ_z={lz}")
    ax.axhline(barrier_flat, color="k", linestyle="--", label="flat")
    ax.set_xlabel("Δz (depth separation)")
    ax.set_ylabel("Merger barrier ΔE")
    ax.set_title("Smooth NEB: barrier vs depth separation")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    for dz in delta_z_vals:
        sub = [r for r in rows_csv if r["delta_z"] == dz]
        xs = [r["lambda_z"] for r in sub]
        ys = [float(r["barrier_smooth"]) if r["barrier_smooth"] != "nan" else np.nan for r in sub]
        ax.plot(xs, ys, marker="s", label=f"Δz={dz}")
    ax.axhline(barrier_flat, color="k", linestyle="--", label="flat")
    ax.set_xlabel("λ_z (depth weight)")
    ax.set_ylabel("Merger barrier ΔE")
    ax.set_title("Smooth NEB: barrier vs λ_z")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(RESULT_DIR, "barrier_vs_depth_lambda_smooth.png"), dpi=100)
    plt.close()

    # Determine result
    valid_barriers = [(r["delta_z"], r["lambda_z"], float(r["barrier_smooth"]))
                      for r in rows_csv if r["barrier_smooth"] not in ("nan", 0.0)
                      and isinstance(r["barrier_smooth"], float) and float(r["barrier_smooth"]) > 1e-6]
    k2_count = sum(1 for r in rows_csv if r["K_act"] >= 2)
    max_barrier = max((v[2] for v in valid_barriers), default=0.0)

    # Monotone check for λ_z sweep at Δz=1.0
    lz_barriers = [(r["lambda_z"], float(r["barrier_smooth"]))
                   for r in lambda_rows if r["barrier_smooth"] not in ("nan",) and r["K_act"] >= 2]
    lz_barriers.sort()
    monotone_lz = all(b2 >= b1 for (_, b1), (_, b2) in zip(lz_barriers, lz_barriers[1:])) if len(lz_barriers) >= 2 else None

    # Monotone check for Δz sweep at λ_z=4.0
    dz_barriers = [(r["delta_z"], float(r["barrier_smooth"]))
                   for r in depth_rows if r["barrier_smooth"] not in ("nan",) and r["K_act"] >= 2]
    dz_barriers.sort()
    monotone_dz = all(b2 >= b1 for (_, b1), (_, b2) in zip(dz_barriers, dz_barriers[1:])) if len(dz_barriers) >= 2 else None

    status = "SUPPORTED" if (k2_count > 0 and max_barrier > 0 and
                              (monotone_lz or monotone_dz)) else "PARTIAL"
    if k2_count == 0:
        status = "NOT_SUPPORTED (no K=2 minima found)"

    # Write summary
    with open(os.path.join(RESULT_DIR, "exp02b_smooth_neb_summary.md"), "w") as f:
        f.write("# exp02b-Smooth-NEB: T-ST-5b Regime B Summary\n\n")
        f.write("## Setup\n\n")
        f.write(f"- Grid: {ROWS}x{COLS}, alpha={ALPHA}, beta={BETA}, rho_pers={RHO_PERS}\n")
        f.write(f"- Smooth adjacency: w_ij = w_2d * exp(-λ_z * |z_i - z_j|²)\n")
        f.write(f"- Δz sweep: {delta_z_vals}\n")
        f.write(f"- λ_z sweep: {lambda_z_vals}\n\n")
        f.write("## Flat reference\n\n")
        f.write(f"K_flat={k_flat}, barrier_flat={barrier_flat:.4f}\n\n")
        f.write("## Results grid\n\n")
        f.write("| Δz | λ_z | product | w_bridge | K_act | barrier | ratio |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        for r in rows_csv:
            f.write(f"| {r['delta_z']} | {r['lambda_z']} | {r['product']} | "
                    f"{r['w_bridge']} | {r['K_act']} | {r['barrier_smooth']} | "
                    f"{r['ratio_smooth_flat']} |\n")
        f.write(f"\n## Summary\n\n")
        f.write(f"- K=2 stable configurations: {k2_count}/{len(rows_csv)}\n")
        f.write(f"- Max barrier (smooth): {max_barrier:.4f}\n")
        f.write(f"- Barrier flat: {barrier_flat:.4f}\n")
        f.write(f"- Monotone in λ_z (Δz=1.0): {monotone_lz}\n")
        f.write(f"- Monotone in Δz (λ_z=4.0): {monotone_dz}\n\n")
        f.write(f"## T-ST-5b Claim Status: **{status}**\n\n")
        f.write("Cat B promotion requires: monotone barrier increase in BOTH Δz and λ_z sweeps,\n")
        f.write("and max_barrier > barrier_flat in the K=2-stable regime.\n")

    print(f"\n[exp02b] k2_count={k2_count}, max_barrier={max_barrier:.4f}, "
          f"monotone_lz={monotone_lz}, monotone_dz={monotone_dz} => {status}")


if __name__ == "__main__":
    np.random.seed(42)
    main()
