"""
exp02c: Smooth-Adjacency Barrier — Beta Sweep and Full Comparison
Claim (T-ST-5b): Under smooth depth-weighted adjacency, merger barrier
  ΔE_smooth > ΔE_flat, increasing in Δz and λ_z.
Exp02b showed null-barrier at β=4 (GL toy energy too weak to create K=2 minima).
This experiment sweeps β ∈ {4, 10, 20, 50} to find the regime where smooth
adjacency creates genuine K=2 local minima and measurable barriers.
Also compares flat / smooth / hard adjacency for each (β, Δz, λ_z).
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import csv
import scipy.sparse as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from stereo_scc.fields import make_grid_2d, gaussian_field, laplacian_from_adj
from stereo_scc.topology import persistent_component_count

ROWS, COLS = 20, 20
ALPHA = 1.0
BETA_VALS = [4.0, 10.0, 20.0, 50.0]
RHO_PERS = 0.05
N_STEPS_RELAX = 3000
STEP_RELAX = 3e-4
N_IMAGES = 16
N_NEB_STEPS = 800
STEP_NEB = 0.002
K_SPRING = 1.0

RESULT_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "exp02c_smooth_full")
os.makedirs(RESULT_DIR, exist_ok=True)

n = ROWS * COLS
rng = np.random.default_rng(42)


# ── energy and gradient ────────────────────────────────────────────────────────

def gl_energy(u, L, alpha=ALPHA, beta=4.0):
    W = (u ** 2) * ((1.0 - u) ** 2)
    return float(alpha * u @ (L @ u) + beta * W.sum())


def gl_gradient(u, L, alpha=ALPHA, beta=4.0):
    dW = 2.0 * u * (1.0 - u) * (1.0 - 2.0 * u)
    return 2.0 * alpha * np.asarray(L @ u).ravel() + beta * dW


def project_mass(u, M):
    u = np.clip(u, 0.0, 1.0)
    return u * (M / u.sum())


def find_minimum(u_init, L, beta=4.0, n_steps=N_STEPS_RELAX, step=STEP_RELAX):
    u = u_init.copy()
    M = u.sum()
    for _ in range(n_steps):
        g = gl_gradient(u, L, beta=beta)
        g_proj = g - g.mean()
        u = np.clip(u - step * g_proj, 0.0, 1.0)
        u = project_mass(u, M)
    return u


# ── adjacency builders ─────────────────────────────────────────────────────────

def build_flat_adj(rows, cols):
    adj, _ = make_grid_2d(rows, cols)
    return adj if sp.issparse(adj) else sp.csr_matrix(adj)


def build_smooth_adj(rows, cols, depth_map, lambda_z):
    nn = rows * cols
    ri, ci, data = [], [], []
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr2, nc2 = r + dr, c + dc
                if 0 <= nr2 < rows and 0 <= nc2 < cols:
                    nidx = nr2 * cols + nc2
                    dz = abs(depth_map[idx] - depth_map[nidx])
                    w = float(np.exp(-lambda_z * dz ** 2))
                    ri.append(idx); ci.append(nidx); data.append(w)
    return sp.csr_matrix((data, (ri, ci)), shape=(nn, nn))


def build_hard_adj(rows, cols, depth_map, delta_z):
    nn = rows * cols
    ri, ci, data = [], [], []
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr2, nc2 = r + dr, c + dc
                if 0 <= nr2 < rows and 0 <= nc2 < cols:
                    nidx = nr2 * cols + nc2
                    if abs(depth_map[idx] - depth_map[nidx]) < delta_z:
                        ri.append(idx); ci.append(nidx); data.append(1.0)
    return sp.csr_matrix((data, (ri, ci)), shape=(nn, nn))


# ── initialisation helpers ─────────────────────────────────────────────────────

def make_bimodal_init(rows, cols, half_width=4):
    u = np.zeros(rows * cols)
    cr = rows // 2
    cmid = cols // 2
    for r in range(cr - half_width, cr + half_width):
        for c in range(cmid // 2 - half_width, cmid // 2 + half_width):
            if 0 <= r < rows and 0 <= c < cols:
                u[r * cols + c] = 0.9
        for c in range(cmid + cmid // 2 - half_width, cmid + cmid // 2 + half_width):
            if 0 <= r < rows and 0 <= c < cols:
                u[r * cols + c] = 0.9
    return u


def make_merged_init(rows, cols, M):
    u = gaussian_field(rows * cols, [(rows // 2, cols // 2)],
                       sigma=4.0, height=0.8, grid_shape=(rows, cols))
    u = np.clip(u, 0.0, 1.0)
    return project_mass(u, M)


# ── NEB ────────────────────────────────────────────────────────────────────────

def neb_barrier(u_start, u_end, L, beta=4.0,
                n_images=N_IMAGES, n_steps=N_NEB_STEPS,
                step=STEP_NEB, k_spring=K_SPRING):
    M = u_start.sum()
    images = [u_start + (u_end - u_start) * i / (n_images - 1)
              for i in range(n_images)]
    images = [np.clip(img, 0.0, 1.0) for img in images]

    for _ in range(n_steps):
        new_images = [images[0]]
        for i in range(1, n_images - 1):
            g = gl_gradient(images[i], L, beta=beta)
            tang = images[i + 1] - images[i - 1]
            norm_t = np.linalg.norm(tang)
            tang = tang / max(norm_t, 1e-12)
            g_perp = g - np.dot(g, tang) * tang
            spring = k_spring * (
                np.linalg.norm(images[i + 1] - images[i])
                - np.linalg.norm(images[i] - images[i - 1])
            ) * tang
            update = g_perp - spring
            update = update - update.mean()
            new_img = np.clip(images[i] - step * update, 0.0, 1.0)
            new_img = project_mass(new_img, M)
            new_images.append(new_img)
        new_images.append(images[-1])
        images = new_images

    energies = [gl_energy(img, L, beta=beta) for img in images]
    barrier = max(0.0, max(energies) - energies[0])
    return barrier, energies


def find_k1_reference(adj, L, M, beta, u_bimodal=None):
    """Try multiple inits to find a K=1 minimum."""
    candidates = [
        make_merged_init(ROWS, COLS, M),
        project_mass(np.ones(n) * 0.5 + rng.uniform(-0.02, 0.02, n), M),
        project_mass(rng.uniform(0.01, 0.1, n), M),
    ]
    for u_init in candidates:
        u = find_minimum(u_init, L, beta=beta, n_steps=4000)
        k = persistent_component_count(adj, u, rho_pers=RHO_PERS)
        if k <= 1:
            return u, k
    return None, None


# ── one (β, Δz, λ_z) trial ────────────────────────────────────────────────────

def run_trial(adj, L, adj_name, beta, delta_z, lambda_z, M):
    u_bimodal = make_bimodal_init(ROWS, COLS)
    u_bimodal = project_mass(u_bimodal, M)
    u_relax = find_minimum(u_bimodal, L, beta=beta)
    k_act = persistent_component_count(adj, u_relax, rho_pers=RHO_PERS)

    if k_act <= 1:
        return dict(adj=adj_name, beta=beta, delta_z=delta_z, lambda_z=lambda_z,
                    K_act=k_act, barrier=0.0, note="K=1 after relax; no K=2 minimum")

    u_k1, k1 = find_k1_reference(adj, L, M, beta)
    if u_k1 is None:
        return dict(adj=adj_name, beta=beta, delta_z=delta_z, lambda_z=lambda_z,
                    K_act=k_act, barrier=float("nan"), note="K=1 ref not found")

    barrier, _ = neb_barrier(u_relax, u_k1, L, beta=beta)
    return dict(adj=adj_name, beta=beta, delta_z=delta_z, lambda_z=lambda_z,
                K_act=k_act, barrier=round(barrier, 6),
                note=f"NEB K={k_act}->1")


# ── main ───────────────────────────────────────────────────────────────────────

def main():
    delta_z_vals = [0.25, 0.5, 1.0, 2.0]
    lambda_z_vals = [1.0, 2.0, 4.0, 8.0]

    adj_flat = build_flat_adj(ROWS, COLS)
    u_bimodal_proto = make_bimodal_init(ROWS, COLS)
    M = u_bimodal_proto.sum()

    all_rows = []

    for beta in BETA_VALS:
        print(f"\n=== beta={beta} ===")

        # flat reference
        L_flat = laplacian_from_adj(adj_flat)
        flat_row = run_trial(adj_flat, L_flat, "flat", beta, 0.0, 0.0, M)
        all_rows.append(flat_row)
        print(f"  flat: K={flat_row['K_act']} barrier={flat_row['barrier']:.4f}")

        for dz in delta_z_vals:
            depth_map = np.ones(n)
            for idx in range(n):
                if (idx % COLS) >= COLS // 2:
                    depth_map[idx] = 1.0 + dz

            # hard adjacency at this Δz
            adj_hard = build_hard_adj(ROWS, COLS, depth_map, dz)
            L_hard = laplacian_from_adj(adj_hard)
            hard_row = run_trial(adj_hard, L_hard, "hard", beta, dz, float("nan"), M)
            hard_row["lambda_z"] = "inf"
            all_rows.append(hard_row)
            print(f"  hard dz={dz:.2f}: K={hard_row['K_act']} barrier={hard_row['barrier']}")

            for lz in lambda_z_vals:
                adj_smooth = build_smooth_adj(ROWS, COLS, depth_map, lz)
                L_smooth = laplacian_from_adj(adj_smooth)
                row = run_trial(adj_smooth, L_smooth, "smooth", beta, dz, lz, M)
                all_rows.append(row)
                print(f"  smooth dz={dz:.2f} lz={lz:.1f}: K={row['K_act']} "
                      f"barrier={row['barrier']:.4f} {row['note']}")

    # ── CSV output ─────────────────────────────────────────────────────────────

    fieldnames = ["adj", "beta", "delta_z", "lambda_z", "K_act", "barrier", "note"]
    with open(os.path.join(RESULT_DIR, "exp02c_full_grid.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(all_rows)

    # ── plots ──────────────────────────────────────────────────────────────────

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.ravel()

    for i_beta, beta in enumerate(BETA_VALS):
        ax = axes[i_beta]
        beta_rows = [r for r in all_rows if r["beta"] == beta and r["adj"] == "smooth"]

        for lz in lambda_z_vals:
            sub = [r for r in beta_rows if r["lambda_z"] == lz]
            sub.sort(key=lambda r: float(r["delta_z"]))
            xs = [float(r["delta_z"]) for r in sub]
            ys = [float(r["barrier"]) if not isinstance(r["barrier"], str)
                  and not (isinstance(r["barrier"], float) and np.isnan(r["barrier"]))
                  else np.nan for r in sub]
            ax.plot(xs, ys, marker="o", label=f"smooth λ_z={lz}")

        # flat and hard baselines
        flat_b = next((r["barrier"] for r in all_rows if r["beta"] == beta
                       and r["adj"] == "flat"), None)
        if flat_b is not None:
            ax.axhline(float(flat_b), color="k", linestyle="--", linewidth=1.5, label="flat")

        for dz in delta_z_vals:
            hard_b = next((r["barrier"] for r in all_rows if r["beta"] == beta
                           and r["adj"] == "hard" and float(r["delta_z"]) == dz), None)
            if hard_b is not None and not isinstance(hard_b, float):
                pass
            elif hard_b is not None:
                ax.axvline(dz, color="gray", linestyle=":", alpha=0.5)

        ax.set_title(f"β={beta}: smooth barrier vs Δz")
        ax.set_xlabel("Δz (depth separation)")
        ax.set_ylabel("Merger barrier ΔE")
        ax.legend(fontsize=7)
        ax.grid(True, alpha=0.3)

    plt.suptitle("T-ST-5b: Smooth-adjacency barrier — β sweep", fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(RESULT_DIR, "exp02c_barrier_beta_sweep.png"), dpi=100)
    plt.close()

    # ── per-β barrier-vs-λ_z plot (at Δz=1.0) ─────────────────────────────────

    fig2, ax2 = plt.subplots(figsize=(8, 5))
    for beta in BETA_VALS:
        sub = [r for r in all_rows
               if r["beta"] == beta and r["adj"] == "smooth"
               and float(r["delta_z"]) == 1.0
               and isinstance(r["lambda_z"], float)]
        sub.sort(key=lambda r: float(r["lambda_z"]))
        xs = [float(r["lambda_z"]) for r in sub]
        ys = [float(r["barrier"]) if not np.isnan(float(r["barrier"])) else np.nan for r in sub]
        ax2.plot(xs, ys, marker="s", label=f"β={beta}")
    ax2.set_xlabel("λ_z (depth weight sharpness)")
    ax2.set_ylabel("Merger barrier ΔE (Δz=1.0)")
    ax2.set_title("T-ST-5b: Barrier vs λ_z for each β (smooth adjacency, Δz=1.0)")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(RESULT_DIR, "exp02c_barrier_vs_lz_by_beta.png"), dpi=100)
    plt.close()

    # ── summary report ─────────────────────────────────────────────────────────

    summary_lines = ["# exp02c: Smooth-Barrier Full-Energy Summary\n",
                     "## T-ST-5b Claim: ΔE_smooth > ΔE_flat, increasing in Δz and λ_z\n\n",
                     "## Per-β summary\n\n"]

    for beta in BETA_VALS:
        beta_smooth = [r for r in all_rows if r["beta"] == beta and r["adj"] == "smooth"
                       and isinstance(r["lambda_z"], float)]
        flat_b = next((r["barrier"] for r in all_rows if r["beta"] == beta
                       and r["adj"] == "flat"), float("nan"))
        k2_count = sum(1 for r in beta_smooth if r["K_act"] >= 2)
        barriers = [float(r["barrier"]) for r in beta_smooth
                    if isinstance(r["barrier"], float) and not np.isnan(r["barrier"])]
        max_b = max(barriers, default=0.0)
        above_flat = sum(1 for b in barriers if b > float(flat_b) + 1e-6) if not np.isnan(float(flat_b)) else 0

        # Monotone check at Δz=1.0 over λ_z
        lz_sub = [(float(r["lambda_z"]), float(r["barrier"])) for r in beta_smooth
                  if float(r["delta_z"]) == 1.0 and r["K_act"] >= 2
                  and isinstance(r["barrier"], float) and not np.isnan(r["barrier"])]
        lz_sub.sort()
        mono_lz = (all(b2 >= b1 for (_, b1), (_, b2) in zip(lz_sub, lz_sub[1:]))
                   if len(lz_sub) >= 2 else None)

        # Monotone check at λ_z=4.0 over Δz
        dz_sub = [(float(r["delta_z"]), float(r["barrier"])) for r in beta_smooth
                  if r["lambda_z"] == 4.0 and r["K_act"] >= 2
                  and isinstance(r["barrier"], float) and not np.isnan(r["barrier"])]
        dz_sub.sort()
        mono_dz = (all(b2 >= b1 for (_, b1), (_, b2) in zip(dz_sub, dz_sub[1:]))
                   if len(dz_sub) >= 2 else None)

        status = "SUPPORTED" if (k2_count > 0 and max_b > float(flat_b) + 1e-6
                                  and mono_lz and mono_dz) else \
                 "PARTIAL" if (k2_count > 0 and max_b > 0) else \
                 "NOT_SUPPORTED (no K=2 minima)"

        summary_lines.append(f"### β={beta}\n")
        summary_lines.append(f"- flat baseline barrier: {flat_b:.4f}\n")
        summary_lines.append(f"- K=2 stable configs: {k2_count}/{len(beta_smooth)}\n")
        summary_lines.append(f"- Max smooth barrier: {max_b:.4f}\n")
        summary_lines.append(f"- Configs above flat: {above_flat}/{len(barriers)}\n")
        summary_lines.append(f"- Monotone in λ_z (Δz=1.0): {mono_lz}\n")
        summary_lines.append(f"- Monotone in Δz (λ_z=4.0): {mono_dz}\n")
        summary_lines.append(f"- **Status: {status}**\n\n")

    summary_lines.append("## T-ST-5b Promotion Criteria\n\n")
    summary_lines.append("Cat C → Cat B requires:\n")
    summary_lines.append("1. K=2 genuine local minima under smooth adjacency (K_act=2 with positive NEB barrier)\n")
    summary_lines.append("2. Barrier monotone increasing in Δz (fixed λ_z) and in λ_z (fixed Δz)\n")
    summary_lines.append("3. max barrier > flat baseline barrier\n")
    summary_lines.append("4. Result holds for at least one (β, Δz, λ_z) regime\n\n")
    summary_lines.append("Note: T-ST-5b is a *regime* claim — it need not hold for all β,\n")
    summary_lines.append("only for sufficiently strong phase separation (large β) and depth separation.\n")

    with open(os.path.join(RESULT_DIR, "exp02c_summary.md"), "w") as f:
        f.writelines(summary_lines)

    print("\n[exp02c] Done. Results in:", RESULT_DIR)
    print("CSV: exp02c_full_grid.csv | Summary: exp02c_summary.md")


if __name__ == "__main__":
    main()
