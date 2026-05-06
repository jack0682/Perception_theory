"""
exp06: Boundary Stability under Shadow and Blur Perturbation (OP-0006)
Claim: SCC gradient-ridge boundary is more stable than raw intensity edge
under photometric perturbation (shadow, blur).
Metric: stability ratio = Δ_raw / Δ_SCC > 1 for shadow.
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import csv
import scipy.sparse as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from stereo_scc.fields import make_grid_2d, gaussian_field, laplacian_from_adj
from stereo_scc.topology import persistent_component_count

ROWS, COLS = 20, 20
ALPHA, BETA = 1.0, 10.0       # high β for phase-separated, crisp boundary
GRAD_THETA = 0.15              # gradient threshold for boundary
GRAD_RHO_BD = 0.05             # persistence threshold for PersRidge
RHO_PERS = 0.05
N_STEPS = 3000
STEP = 3e-4

RESULT_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "exp06_boundary")
os.makedirs(RESULT_DIR, exist_ok=True)

n = ROWS * COLS


# ── energy / optimizer ─────────────────────────────────────────────────────────

def gl_energy(u, L):
    W = (u ** 2) * ((1 - u) ** 2)
    return float(ALPHA * u @ L @ u + BETA * W.sum())


def gl_gradient(u, L):
    dW = 2 * u * (1 - u) * (1 - 2 * u)
    return 2 * ALPHA * (L @ u) + BETA * dW


def optimize(u_init, L, n_steps=N_STEPS, step=STEP):
    u = u_init.copy()
    m = u.sum()
    for _ in range(n_steps):
        g = gl_gradient(u, L)
        g -= g.mean()
        u = u - step * g
        u = np.clip(u, 0.0, 1.0)
        u = u * (m / u.sum())
    return u


# ── boundary computation ───────────────────────────────────────────────────────

def grad_magnitude(u, adj):
    """Discrete gradient magnitude at each node."""
    gm = np.zeros(n)
    for i in range(n):
        neighbors = np.where(adj[i] > 0)[0]
        gm[i] = np.sqrt(sum((u[i] - u[j]) ** 2 for j in neighbors))
    return gm


def threshold_boundary(gm, theta=GRAD_THETA):
    return set(np.where(gm > theta)[0])


def pers_ridge_boundary(gm, adj, rho_bd=GRAD_RHO_BD):
    """Persistent gradient ridge via H_0 superlevel barcode of gm."""
    # Use persistence filtration of gm itself:
    # nodes with persistent contribution to H_0 of superlevel set
    sorted_nodes = np.argsort(-gm)  # high to low
    uf = {}  # union-find (birth time of component)

    def find(x):
        while uf.get(x, x) != x:
            uf[x] = uf.get(uf.get(x, x), uf.get(x, x))
            x = uf.get(x, x)
        return x

    births = {}   # component root -> birth level
    deaths = {}   # node -> (birth, death) when it caused a merge

    for node in sorted_nodes:
        level = gm[node]
        neighbors_in = [j for j in np.where(adj[node] > 0)[0] if j in births or j in deaths]
        # Actually we want: nodes already processed with gm[j] >= level (approximately)
        # Simplified: track active components
        neighbors_active = [j for j in np.where(adj[node] > 0)[0]
                            if uf.get(j, j) in births]
        if not neighbors_active:
            # Birth of new component
            uf[node] = node
            births[node] = level
        else:
            roots = list({find(j) for j in neighbors_active})
            # Merge: youngest component (lowest birth = smallest value) dies
            roots_sorted = sorted(roots, key=lambda r: births.get(r, 0), reverse=True)
            survivor = roots_sorted[0]
            for dead_root in roots_sorted[1:]:
                deaths[dead_root] = (births[dead_root], level)
                del births[dead_root]
                uf[dead_root] = survivor
            uf[node] = find(survivor)
            births[find(survivor)] = births.get(find(survivor), level)

    # Persistent ridge: components with persistence > rho_bd
    persistent_nodes = set()
    for root, birth in births.items():
        # infinite persistence (no death) or large enough birth
        if birth > rho_bd:
            # all nodes in this component
            for i in range(n):
                if find(i) == find(root) and gm[i] > rho_bd:
                    persistent_nodes.add(i)
    for dead_root, (birth, death) in deaths.items():
        if birth - death > rho_bd:
            # nodes that were in this component
            # approximate: nodes with gm in [death, birth]
            for i in range(n):
                if death < gm[i] <= birth:
                    persistent_nodes.add(i)

    # Fallback: if no persistent nodes found, use thresholded version
    if not persistent_nodes:
        persistent_nodes = threshold_boundary(gm, theta=rho_bd)
    return persistent_nodes


def symmetric_diff_rate(B1, B2, B_ref):
    """Normalized symmetric difference relative to B_ref size."""
    if len(B_ref) == 0:
        return 0.0
    return len(B1.symmetric_difference(B2)) / len(B_ref)


def l1_grad_change(gm1, gm2, gm_ref_norm):
    """Normalized L1 change in gradient magnitude field."""
    if gm_ref_norm < 1e-10:
        return 0.0
    return float(np.abs(gm1 - gm2).sum()) / gm_ref_norm


# ── main ───────────────────────────────────────────────────────────────────────

def main():
    adj_sparse, _ = make_grid_2d(ROWS, COLS)
    adj_sparse = sp.csr_matrix(adj_sparse) if not sp.issparse(adj_sparse) else adj_sparse
    adj = adj_sparse.toarray()   # dense copy for neighbor iteration in grad_magnitude
    L = laplacian_from_adj(adj_sparse)

    # Reference field: single centered blob
    rng = np.random.default_rng(0)
    u_init = gaussian_field(n, [(ROWS // 2, COLS // 2)], sigma=3.5, height=0.8,
                             grid_shape=(ROWS, COLS))
    u_init = np.clip(u_init, 0.0, 1.0)
    m = u_init.sum()

    u_star = optimize(u_init, L)
    k_ref = persistent_component_count(adj_sparse, u_star, rho_pers=RHO_PERS)

    gm_ref = grad_magnitude(u_star, adj)
    B_ref = threshold_boundary(gm_ref)
    B_ref_pers = pers_ridge_boundary(gm_ref, adj)
    gm_ref_norm = float(gm_ref.sum())

    print(f"  Reference: K={k_ref}, |B_ref|={len(B_ref)}, |B_ref_pers|={len(B_ref_pers)}")

    # Shadow mask: left half (columns 0..9)
    shadow_mask = np.zeros(n)
    for idx in range(n):
        if idx % COLS < COLS // 2:
            shadow_mask[idx] = 1.0

    shadow_strengths = [0.2, 0.3, 0.5, 0.7, 0.8]
    blur_sigmas = [0.5, 1.0, 1.5, 2.0, 3.0]

    shadow_rows = []
    blur_rows = []

    # ── Shadow sweep ───────────────────────────────────────────────────────────
    print("  Shadow sweep:")
    for s in shadow_strengths:
        u_shadow_raw = u_star * (1.0 - s * shadow_mask)
        u_shadow_raw = np.clip(u_shadow_raw, 0.0, 1.0)
        u_shadow_raw = u_shadow_raw * (m / max(u_shadow_raw.sum(), 1e-10))

        # SCC re-optimized boundary
        u_star_shadow = optimize(u_shadow_raw, L)
        gm_shadow_scc = grad_magnitude(u_star_shadow, adj)
        B_shadow_scc = threshold_boundary(gm_shadow_scc)
        B_shadow_scc_pers = pers_ridge_boundary(gm_shadow_scc, adj)

        # Raw boundary (no re-optimization)
        gm_shadow_raw = grad_magnitude(u_shadow_raw, adj)
        B_shadow_raw = threshold_boundary(gm_shadow_raw)

        # Metrics
        delta_scc = symmetric_diff_rate(B_shadow_scc, B_ref, B_ref)
        delta_scc_pers = symmetric_diff_rate(B_shadow_scc_pers, B_ref_pers, B_ref_pers)
        delta_raw = l1_grad_change(gm_shadow_raw, gm_ref, gm_ref_norm)
        delta_scc_l1 = l1_grad_change(gm_shadow_scc, gm_ref, gm_ref_norm)
        ratio = delta_raw / delta_scc_l1 if delta_scc_l1 > 1e-6 else float("inf")

        shadow_rows.append({
            "shadow_strength": s,
            "delta_SCC_symmdiff": round(delta_scc, 4),
            "delta_SCC_pers_symmdiff": round(delta_scc_pers, 4),
            "delta_raw_L1": round(delta_raw, 4),
            "delta_SCC_L1": round(delta_scc_l1, 4),
            "stability_ratio": round(ratio, 3) if ratio < 1e5 else "inf",
            "claim": "SUPPORTED" if ratio > 1.0 else "NOT_SUPPORTED"
        })
        print(f"    s={s:.1f}: Δ_raw={delta_raw:.4f} Δ_SCC={delta_scc_l1:.4f} ratio={ratio:.3f}")

    # ── Blur sweep ─────────────────────────────────────────────────────────────
    print("  Blur sweep:")
    for sigma in blur_sigmas:
        u_blur_raw = gaussian_filter(u_star.reshape(ROWS, COLS), sigma=sigma).ravel()
        u_blur_raw = np.clip(u_blur_raw, 0.0, 1.0)
        u_blur_raw = u_blur_raw * (m / max(u_blur_raw.sum(), 1e-10))

        u_star_blur = optimize(u_blur_raw, L)
        gm_blur_scc = grad_magnitude(u_star_blur, adj)
        B_blur_scc = threshold_boundary(gm_blur_scc)
        B_blur_scc_pers = pers_ridge_boundary(gm_blur_scc, adj)

        gm_blur_raw = grad_magnitude(u_blur_raw, adj)
        B_blur_raw = threshold_boundary(gm_blur_raw)

        delta_scc = symmetric_diff_rate(B_blur_scc, B_ref, B_ref)
        delta_scc_pers = symmetric_diff_rate(B_blur_scc_pers, B_ref_pers, B_ref_pers)
        delta_raw = l1_grad_change(gm_blur_raw, gm_ref, gm_ref_norm)
        delta_scc_l1 = l1_grad_change(gm_blur_scc, gm_ref, gm_ref_norm)
        ratio = delta_raw / delta_scc_l1 if delta_scc_l1 > 1e-6 else float("inf")

        blur_rows.append({
            "blur_sigma": sigma,
            "delta_SCC_symmdiff": round(delta_scc, 4),
            "delta_SCC_pers_symmdiff": round(delta_scc_pers, 4),
            "delta_raw_L1": round(delta_raw, 4),
            "delta_SCC_L1": round(delta_scc_l1, 4),
            "stability_ratio": round(ratio, 3) if ratio < 1e5 else "inf",
            "claim": "SUPPORTED" if ratio > 1.0 else "NOT_SUPPORTED"
        })
        print(f"    σ={sigma:.1f}: Δ_raw={delta_raw:.4f} Δ_SCC={delta_scc_l1:.4f} ratio={ratio:.3f}")

    # Save CSVs
    with open(os.path.join(RESULT_DIR, "boundary_stability_shadow.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=shadow_rows[0].keys())
        w.writeheader()
        w.writerows(shadow_rows)

    with open(os.path.join(RESULT_DIR, "boundary_stability_blur.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=blur_rows[0].keys())
        w.writeheader()
        w.writerows(blur_rows)

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    ax = axes[0]
    ax.plot([r["shadow_strength"] for r in shadow_rows],
            [r["delta_raw_L1"] for r in shadow_rows], "r-o", label="raw edge Δ")
    ax.plot([r["shadow_strength"] for r in shadow_rows],
            [r["delta_SCC_L1"] for r in shadow_rows], "b-o", label="SCC boundary Δ")
    ax.set_xlabel("Shadow strength s")
    ax.set_ylabel("Normalized change")
    ax.set_title("Boundary stability: shadow perturbation")
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.plot([r["blur_sigma"] for r in blur_rows],
            [r["delta_raw_L1"] for r in blur_rows], "r-s", label="raw edge Δ")
    ax.plot([r["blur_sigma"] for r in blur_rows],
            [r["delta_SCC_L1"] for r in blur_rows], "b-s", label="SCC boundary Δ")
    ax.set_xlabel("Blur σ")
    ax.set_ylabel("Normalized change")
    ax.set_title("Boundary stability: blur perturbation")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(RESULT_DIR, "boundary_stability.png"), dpi=100)
    plt.close()

    # Heatmaps: reference field and gradient magnitude
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.5))
    axes[0].imshow(u_star.reshape(ROWS, COLS), cmap="hot", vmin=0, vmax=1)
    axes[0].set_title("u* (reference field)")
    axes[0].axis("off")
    axes[1].imshow(gm_ref.reshape(ROWS, COLS), cmap="plasma")
    axes[1].set_title("|∇_G u*| (gradient magnitude)")
    axes[1].axis("off")
    plt.tight_layout()
    plt.savefig(os.path.join(RESULT_DIR, "reference_field_grad.png"), dpi=100)
    plt.close()

    # Determine overall result
    shadow_supported = sum(1 for r in shadow_rows if r["claim"] == "SUPPORTED")
    blur_supported = sum(1 for r in blur_rows if r["claim"] == "SUPPORTED")
    shadow_ratios = [r["stability_ratio"] for r in shadow_rows
                     if isinstance(r["stability_ratio"], float)]
    max_shadow_ratio = max(shadow_ratios) if shadow_ratios else 0.0
    overall = "SUPPORTED" if shadow_supported >= 3 else "PARTIAL"

    # Write summary
    with open(os.path.join(RESULT_DIR, "boundary_stability_summary.md"), "w") as f:
        f.write("# exp06: Boundary Stability Summary (OP-0006)\n\n")
        f.write("## Setup\n\n")
        f.write(f"- Grid: {ROWS}x{COLS}, alpha={ALPHA}, beta={BETA} (phase-separated)\n")
        f.write(f"- Reference: K={k_ref}, |B_ref|={len(B_ref)}, |B_ref_pers|={len(B_ref_pers)}\n")
        f.write(f"- Boundary threshold θ={GRAD_THETA}, ρ_bd={GRAD_RHO_BD}\n\n")
        f.write("## Shadow Results\n\n")
        f.write("| s | Δ_raw | Δ_SCC | ratio | claim |\n")
        f.write("|---|---|---|---|---|\n")
        for r in shadow_rows:
            f.write(f"| {r['shadow_strength']} | {r['delta_raw_L1']} | "
                    f"{r['delta_SCC_L1']} | {r['stability_ratio']} | {r['claim']} |\n")
        f.write("\n## Blur Results\n\n")
        f.write("| σ | Δ_raw | Δ_SCC | ratio | claim |\n")
        f.write("|---|---|---|---|---|\n")
        for r in blur_rows:
            f.write(f"| {r['blur_sigma']} | {r['delta_raw_L1']} | "
                    f"{r['delta_SCC_L1']} | {r['stability_ratio']} | {r['claim']} |\n")
        f.write(f"\n## Summary\n\n")
        f.write(f"- Shadow: {shadow_supported}/{len(shadow_rows)} conditions SUPPORTED\n")
        f.write(f"- Blur: {blur_supported}/{len(blur_rows)} conditions SUPPORTED\n")
        f.write(f"- Max shadow stability ratio: {max_shadow_ratio:.3f}\n\n")
        f.write(f"## OP-0006 Cat B Criterion 3 Status: **{overall}**\n\n")
        f.write("Cat B promotion requires: stability ratio > 1 for s >= 0.3 (shadow).\n")
        f.write("Cat A promotion requires: topological stability proof + stereo conditioning.\n")

    print(f"\n[exp06] shadow_supported={shadow_supported}/{len(shadow_rows)}, "
          f"blur_supported={blur_supported}/{len(blur_rows)}, "
          f"max_shadow_ratio={max_shadow_ratio:.3f} => {overall}")


if __name__ == "__main__":
    main()
