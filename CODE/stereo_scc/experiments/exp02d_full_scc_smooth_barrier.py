#!/usr/bin/env python3
"""
exp02d: Full SCC Energy Barrier for T-ST-5b (T-ST-5b promotion evidence)

T-ST-5b claim: Under smooth depth-weighted adjacency (§3.10), the merger
barrier ΔE_smooth > ΔE_flat, monotone increasing in depth separation Δz
and depth weight sharpness λ_z.

exp02c finding (GL-only energy): flat and smooth adjacency give approximately
equal NEB barriers at β=20 (≈ 0.41 for both). GL energy insufficient for
T-ST-5b. This experiment tests whether E_cl (closure) and/or E_sep (separation)
from the full SCC energy create a genuine structural barrier under smooth
adjacency not present for flat adjacency.

Energy variants compared:
  gl_only  : E_bd only    (w_cl=0, w_sep=0, w_bd=1) — exp02c replication
  bd_cl    : E_bd + E_cl  (w_cl=1, w_sep=0, w_bd=1)
  bd_sep   : E_bd + E_sep (w_cl=0, w_sep=1, w_bd=1)
  full_scc : E_bd + E_cl + E_sep (w_cl=1, w_sep=1, w_bd=1)

Adjacency variants:
  flat   : uniform weight 1.0 (GraphState.grid_2d)
  smooth : Gaussian decay exp(-λ_z · dz²) in depth difference

NEB method: single-field space (exp60 design).
  u_A = clip(u1 + u2, 0, 1) projected to m_total  (K=2 combined)
  u_B = find_formation(g, p_merged)               (K=1 minimizer)
  Path: linear interpolation → NEB iterations with climbing image.

Grid: 12×12 (n=144) — balanced between SCC quality and runtime.
"""
import sys, os, json, csv, time
import numpy as np
import scipy.sparse as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.multi import find_k_formations
from scc.energy import EnergyComputer

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ROWS, COLS = 12, 12
BETA = 20.0
VOLUME_FRACTION = 0.3
LAMBDA_REP = 10.0

DELTA_Z_VALS = [0.5, 1.0, 2.0]
LAMBDA_Z_VALS = [2.0, 4.0]

ENERGY_VARIANTS = [
    ("gl_only",  dict(w_cl=0.0, w_sep=0.0, w_bd=1.0)),
    ("bd_cl",    dict(w_cl=1.0, w_sep=0.0, w_bd=1.0)),
    ("bd_sep",   dict(w_cl=0.0, w_sep=1.0, w_bd=1.0)),
    ("full_scc", dict(w_cl=1.0, w_sep=1.0, w_bd=1.0)),
]

NEB_N_IMAGES = 12
NEB_MAX_ITER = 600
NEB_TOL = 5e-3
NEB_K_SPRING = 1.0
NEB_DT = 0.004

K2_N_RESTARTS = 2
K2_MAX_ITER = 2000
K1_MAX_ITER = 3000
K1_N_RESTARTS = 3

RESULT_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "exp02d_full_scc")
os.makedirs(RESULT_DIR, exist_ok=True)

n = ROWS * COLS

# ---------------------------------------------------------------------------
# Adjacency builders
# ---------------------------------------------------------------------------

def build_flat_adj(rows: int, cols: int) -> GraphState:
    return GraphState.grid_2d(rows, cols)


def build_smooth_adj(rows: int, cols: int, depth_map: np.ndarray, lambda_z: float) -> GraphState:
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
    W = sp.csr_matrix((data, (ri, ci)), shape=(nn, nn))
    return GraphState(W)


def make_depth_map(rows: int, cols: int, delta_z: float) -> np.ndarray:
    """Left half: depth 1.0, right half: depth 1.0 + delta_z."""
    depth = np.ones(rows * cols)
    for idx in range(rows * cols):
        if (idx % cols) >= cols // 2:
            depth[idx] = 1.0 + delta_z
    return depth


def make_params(beta: float, vf: float, **weight_kwargs) -> ParameterRegistry:
    return ParameterRegistry(
        beta_bd=beta,
        volume_fraction=vf,
        max_iter=K2_MAX_ITER,
        n_restarts=K2_N_RESTARTS,
        eps_grad=5e-3,
        **weight_kwargs,
    )

# ---------------------------------------------------------------------------
# NEB (adapted from exp60: single-field space)
# ---------------------------------------------------------------------------

def _neb_tangent_ew(images: list, energies: np.ndarray, i: int) -> np.ndarray:
    tau_plus = images[i + 1] - images[i]
    tau_minus = images[i] - images[i - 1]
    dE_plus = abs(energies[i + 1] - energies[i])
    dE_minus = abs(energies[i - 1] - energies[i])
    dE_max = max(dE_plus, dE_minus)
    dE_min = min(dE_plus, dE_minus)
    if energies[i + 1] > energies[i - 1]:
        tau = dE_max * tau_plus + dE_min * tau_minus
    elif energies[i + 1] < energies[i - 1]:
        tau = dE_min * tau_plus + dE_max * tau_minus
    else:
        tau = tau_plus + tau_minus
    norm = np.linalg.norm(tau)
    return tau / max(norm, 1e-14)


def neb_barrier_scc(
    ec: EnergyComputer,
    m_total: float,
    u_A: np.ndarray,
    u_B: np.ndarray,
    n_images: int = NEB_N_IMAGES,
    k_spring: float = NEB_K_SPRING,
    max_iter: int = NEB_MAX_ITER,
    tol: float = NEB_TOL,
    dt: float = NEB_DT,
    verbose: bool = False,
) -> dict:
    """Climbing-image NEB in single-field space from u_A (K=2 combined) to u_B (K=1)."""
    total_images = n_images + 2
    images = []
    for i in range(total_images):
        alpha = i / (total_images - 1)
        img = (1.0 - alpha) * u_A + alpha * u_B
        img = project_volume(np.clip(img, 0.0, 1.0), m_total)
        images.append(img.copy())

    # Linear interpolation barrier (for reference)
    li_energies = np.array([ec.energy(img)[0] for img in images])
    E_endpoints = max(ec.energy(u_A)[0], ec.energy(u_B)[0])
    barrier_li = float(np.max(li_energies) - E_endpoints)

    enable_climbing = max_iter // 4
    converged = False
    history = []
    max_force_clamp = 5.0

    for iteration in range(max_iter):
        energies = np.array([ec.energy(img)[0] for img in images])
        gradients = [np.zeros(n) if (i == 0 or i == total_images - 1)
                     else ec.gradient_projected(images[i])
                     for i in range(total_images)]

        interior_E = energies[1:-1]
        climbing_idx = int(np.argmax(interior_E)) + 1
        use_climbing = (iteration >= enable_climbing)

        forces = []
        for i in range(1, total_images - 1):
            tau = _neb_tangent_ew(images, energies, i)
            grad_i = gradients[i]
            if i == climbing_idx and use_climbing:
                f = -grad_i + 2.0 * np.dot(grad_i, tau) * tau
            else:
                grad_perp = grad_i - np.dot(grad_i, tau) * tau
                d_plus = np.linalg.norm(images[i + 1] - images[i])
                d_minus = np.linalg.norm(images[i] - images[i - 1])
                f_spring = k_spring * (d_plus - d_minus)
                f = -grad_perp + f_spring * tau
            f_norm = np.linalg.norm(f)
            if f_norm > max_force_clamp * np.sqrt(n):
                f = f * (max_force_clamp * np.sqrt(n) / f_norm)
            forces.append(f)

        rms_force = float(np.sqrt(np.mean([np.sum(fv**2) for fv in forces])))
        max_force_val = float(max(np.linalg.norm(fv) / np.sqrt(n) for fv in forces))
        history.append({
            'iter': iteration,
            'rms_force': rms_force,
            'max_force': max_force_val,
            'barrier': float(energies[climbing_idx] - E_endpoints),
        })

        if verbose and iteration % 100 == 0:
            print(f"    NEB iter {iteration}: max_f={max_force_val:.4f}  "
                  f"barrier={energies[climbing_idx] - E_endpoints:.5f}"
                  f"{' [CI]' if use_climbing else ''}")

        if max_force_val < tol:
            converged = True
            break

        for idx, i in enumerate(range(1, total_images - 1)):
            images[i] = project_volume(np.clip(images[i] + dt * forces[idx], 0.0, 1.0), m_total)

    final_energies = np.array([ec.energy(img)[0] for img in images])
    saddle_idx = int(np.argmax(final_energies[1:-1])) + 1
    barrier_neb = float(np.max(final_energies[1:-1]) - E_endpoints)

    return {
        'barrier_li': barrier_li,
        'barrier_neb': barrier_neb,
        'E_A': float(ec.energy(u_A)[0]),
        'E_B': float(ec.energy(u_B)[0]),
        'saddle_E': float(final_energies[saddle_idx]),
        'saddle_idx': saddle_idx,
        'converged': converged,
        'n_iter': len(history),
        'final_max_force': float(history[-1]['max_force']) if history else float('inf'),
        'energy_path_neb': final_energies.tolist(),
    }


# ---------------------------------------------------------------------------
# Per-trial runner
# ---------------------------------------------------------------------------

def run_trial(
    g: GraphState,
    p: ParameterRegistry,
    adj_name: str,
    variant_name: str,
    delta_z: float,
    lambda_z: float,
    verbose: bool = False,
) -> dict:
    """Run one (adjacency, energy_variant, delta_z, lambda_z) trial."""
    base_record = dict(
        adj=adj_name, variant=variant_name,
        delta_z=delta_z, lambda_z=lambda_z,
        beta=BETA,
    )
    t0 = time.time()

    # Step 1: Find K=2 endpoint
    if verbose:
        print(f"    [{adj_name}/{variant_name}] Finding K=2 endpoint...")
    try:
        k2_results = find_k_formations(
            g, p, K=2,
            lambda_rep=LAMBDA_REP,
            lambda_bar=100.0,
            n_restarts=K2_N_RESTARTS,
            max_iter=K2_MAX_ITER,
        )
    except Exception as exc:
        return {**base_record, 'K_act': 0, 'barrier_neb': float('nan'),
                'barrier_li': float('nan'), 'note': f'k2_fail: {exc}',
                'elapsed_s': time.time() - t0}

    if len(k2_results) < 2:
        return {**base_record, 'K_act': len(k2_results), 'barrier_neb': 0.0,
                'barrier_li': 0.0, 'note': 'K=2 not found (only 1 formation)',
                'elapsed_s': time.time() - t0}

    u1, u2 = k2_results[0].u, k2_results[1].u
    m1, m2 = float(np.sum(u1)), float(np.sum(u2))
    m_total = m1 + m2

    u_A = project_volume(np.clip(u1 + u2, 0.0, 1.0), m_total)

    # Step 2: Find K=1 endpoint
    if verbose:
        print(f"    [{adj_name}/{variant_name}] Finding K=1 endpoint...")
    vf_merged = max(0.22, min(0.78, m_total / n))
    p_k1 = ParameterRegistry(
        beta_bd=p.beta_bd,
        volume_fraction=vf_merged,
        max_iter=K1_MAX_ITER,
        n_restarts=K1_N_RESTARTS,
        eps_grad=5e-3,
        w_cl=p.w_cl, w_sep=p.w_sep, w_bd=p.w_bd,
    )
    try:
        k1_result = find_formation(g, p_k1)
    except Exception as exc:
        return {**base_record, 'K_act': 2, 'barrier_neb': float('nan'),
                'barrier_li': float('nan'), 'note': f'k1_fail: {exc}',
                'elapsed_s': time.time() - t0}

    u_B = project_volume(k1_result.u, m_total)

    # Step 3: NEB
    if verbose:
        print(f"    [{adj_name}/{variant_name}] Running NEB...")
    ec = EnergyComputer(g, p)
    neb_result = neb_barrier_scc(ec, m_total, u_A, u_B, verbose=verbose)

    # Per-term energy at K=2 combined and K=1
    _, terms_A = ec.energy(u_A)
    _, terms_B = ec.energy(u_B)

    elapsed = time.time() - t0
    return {
        **base_record,
        'K_act': 2,
        'barrier_neb': round(neb_result['barrier_neb'], 6),
        'barrier_li': round(neb_result['barrier_li'], 6),
        'E_A': round(neb_result['E_A'], 6),
        'E_B': round(neb_result['E_B'], 6),
        'saddle_E': round(neb_result['saddle_E'], 6),
        'E_A_bd': round(terms_A.get('E_bd', 0.0), 6),
        'E_A_cl': round(terms_A.get('E_cl', 0.0), 6),
        'E_A_sep': round(terms_A.get('E_sep', 0.0), 6),
        'converged': neb_result['converged'],
        'n_iter': neb_result['n_iter'],
        'final_max_force': round(neb_result['final_max_force'], 5),
        'note': 'NEB K=2->1',
        'elapsed_s': round(elapsed, 1),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("  exp02d: Full SCC Energy Barrier (T-ST-5b)")
    print(f"  Grid: {ROWS}x{COLS}  β={BETA}  vol_frac={VOLUME_FRACTION}")
    print("=" * 70)

    all_rows = []

    for variant_name, weight_kwargs in ENERGY_VARIANTS:
        print(f"\n{'='*60}")
        print(f"  Energy variant: {variant_name}  "
              f"(w_cl={weight_kwargs['w_cl']}, w_sep={weight_kwargs['w_sep']}, "
              f"w_bd={weight_kwargs['w_bd']})")
        print(f"{'='*60}")

        p = make_params(BETA, VOLUME_FRACTION, **weight_kwargs)

        # --- Flat adjacency (baseline) ---
        print(f"\n  [flat/{variant_name}]")
        g_flat = build_flat_adj(ROWS, COLS)
        flat_row = run_trial(g_flat, p, "flat", variant_name, 0.0, 0.0, verbose=True)
        all_rows.append(flat_row)
        print(f"  flat: K={flat_row['K_act']}  "
              f"barrier_neb={flat_row['barrier_neb']}  "
              f"converged={flat_row.get('converged', '?')}  "
              f"t={flat_row['elapsed_s']}s")

        # --- Smooth adjacency sweep ---
        for delta_z in DELTA_Z_VALS:
            depth_map = make_depth_map(ROWS, COLS, delta_z)
            for lambda_z in LAMBDA_Z_VALS:
                g_smooth = build_smooth_adj(ROWS, COLS, depth_map, lambda_z)
                print(f"\n  [smooth Δz={delta_z:.1f} λ_z={lambda_z:.1f} / {variant_name}]")
                row = run_trial(g_smooth, p, "smooth", variant_name,
                                delta_z, lambda_z, verbose=True)
                all_rows.append(row)
                print(f"  K={row['K_act']}  "
                      f"barrier_neb={row['barrier_neb']}  "
                      f"barrier_li={row['barrier_li']}  "
                      f"converged={row.get('converged', '?')}  "
                      f"t={row['elapsed_s']}s")

    # --- CSV output ---
    fieldnames = [
        'adj', 'variant', 'delta_z', 'lambda_z', 'beta',
        'K_act', 'barrier_neb', 'barrier_li', 'E_A', 'E_B', 'saddle_E',
        'E_A_bd', 'E_A_cl', 'E_A_sep',
        'converged', 'n_iter', 'final_max_force', 'note', 'elapsed_s',
    ]
    csv_path = os.path.join(RESULT_DIR, "exp02d_full_scc.csv")
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        w.writeheader()
        w.writerows(all_rows)
    print(f"\nCSV: {csv_path}")

    # --- Summary report ---
    _write_summary(all_rows)

    # --- Plots ---
    _write_plots(all_rows)

    print(f"\n[exp02d] Done. Results in: {RESULT_DIR}")


def _write_summary(all_rows: list):
    lines = [
        "# exp02d: Full SCC Smooth Barrier Summary\n\n",
        "**T-ST-5b claim**: ΔE_smooth > ΔE_flat, monotone in Δz and λ_z.\n\n",
        f"Grid: {ROWS}×{COLS}  β={BETA}  vol_frac={VOLUME_FRACTION}\n\n",
        "## Per-variant results\n\n",
    ]

    for variant_name, _ in ENERGY_VARIANTS:
        v_rows = [r for r in all_rows if r['variant'] == variant_name]
        flat_row = next((r for r in v_rows if r['adj'] == 'flat'), None)
        smooth_rows = [r for r in v_rows if r['adj'] == 'smooth' and r['K_act'] >= 2]

        flat_barrier = float(flat_row['barrier_neb']) if flat_row and not _isnan(flat_row['barrier_neb']) else float('nan')
        smooth_barriers = [float(r['barrier_neb']) for r in smooth_rows
                           if not _isnan(r['barrier_neb'])]
        max_smooth = max(smooth_barriers, default=float('nan'))
        above_flat = sum(1 for b in smooth_barriers if b > flat_barrier + 1e-5)

        # Monotone check at λ_z=4.0 over Δz
        dz_sub = sorted(
            [(float(r['delta_z']), float(r['barrier_neb'])) for r in smooth_rows
             if float(r['lambda_z']) == 4.0 and not _isnan(r['barrier_neb'])],
            key=lambda x: x[0],
        )
        mono_dz = (all(b2 >= b1 for (_, b1), (_, b2) in zip(dz_sub, dz_sub[1:]))
                   if len(dz_sub) >= 2 else None)

        # Monotone check at Δz=1.0 over λ_z
        lz_sub = sorted(
            [(float(r['lambda_z']), float(r['barrier_neb'])) for r in smooth_rows
             if float(r['delta_z']) == 1.0 and not _isnan(r['barrier_neb'])],
            key=lambda x: x[0],
        )
        mono_lz = (all(b2 >= b1 for (_, b1), (_, b2) in zip(lz_sub, lz_sub[1:]))
                   if len(lz_sub) >= 2 else None)

        if len(smooth_barriers) > 0 and max_smooth > flat_barrier + 1e-5 and mono_dz and mono_lz:
            status = "SUPPORTED"
        elif len(smooth_barriers) > 0 and max_smooth > flat_barrier + 1e-5:
            status = "PARTIAL (barrier above flat, monotonicity not confirmed)"
        elif len(smooth_barriers) > 0:
            status = "NOT_SUPPORTED (smooth barrier not above flat)"
        else:
            status = "INCONCLUSIVE (no K=2 minima found)"

        lines += [
            f"### {variant_name}\n",
            f"- Flat barrier: {flat_barrier:.5f}\n",
            f"- Max smooth barrier: {max_smooth:.5f}\n",
            f"- K=2 configs with barrier > flat: {above_flat}/{len(smooth_barriers)}\n",
            f"- Monotone in Δz (λ_z=4.0): {mono_dz}\n",
            f"- Monotone in λ_z (Δz=1.0): {mono_lz}\n",
            f"- **T-ST-5b status: {status}**\n\n",
        ]

    lines += [
        "## T-ST-5b Cat C → Cat B promotion criteria\n\n",
        "1. K=2 genuine local minima under smooth adjacency (positive NEB barrier)\n",
        "2. max smooth barrier > flat barrier (smooth creates additional barrier)\n",
        "3. Barrier monotone in Δz (depth separation) and λ_z (weight sharpness)\n",
        "4. Holds for at least one energy variant with E_cl active\n\n",
        "## Key question\n\n",
        "Does adding E_cl (closure energy) to GL-only (E_bd) create a smooth-adjacency\n",
        "barrier? Compare gl_only vs bd_cl results above.\n",
    ]

    summary_path = os.path.join(RESULT_DIR, "exp02d_summary.md")
    with open(summary_path, 'w') as f:
        f.writelines(lines)
    print(f"Summary: {summary_path}")


def _write_plots(all_rows: list):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.ravel()

    for ax_idx, (variant_name, _) in enumerate(ENERGY_VARIANTS):
        ax = axes[ax_idx]
        v_rows = [r for r in all_rows if r['variant'] == variant_name]

        flat_row = next((r for r in v_rows if r['adj'] == 'flat'), None)
        if flat_row and not _isnan(flat_row['barrier_neb']):
            ax.axhline(float(flat_row['barrier_neb']), color='k',
                       linestyle='--', linewidth=1.5, label='flat')

        for lambda_z in LAMBDA_Z_VALS:
            sub = [r for r in v_rows
                   if r['adj'] == 'smooth' and float(r['lambda_z']) == lambda_z
                   and not _isnan(r['barrier_neb'])]
            sub.sort(key=lambda r: float(r['delta_z']))
            xs = [float(r['delta_z']) for r in sub]
            ys = [float(r['barrier_neb']) for r in sub]
            if xs:
                ax.plot(xs, ys, marker='o', label=f'smooth λ_z={lambda_z}')

        ax.set_title(f"{variant_name}: barrier vs Δz  (β={BETA})")
        ax.set_xlabel("Δz (depth separation)")
        ax.set_ylabel("NEB barrier ΔE")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    plt.suptitle(f"exp02d: Full SCC Barrier vs Depth Separation  (β={BETA}, {ROWS}×{COLS})",
                 fontsize=12)
    plt.tight_layout()
    plot_path = os.path.join(RESULT_DIR, "exp02d_barrier_vs_dz.png")
    plt.savefig(plot_path, dpi=100)
    plt.close()
    print(f"Plot: {plot_path}")

    # Variant comparison at Δz=1.0
    fig2, ax2 = plt.subplots(figsize=(9, 5))
    x_positions = np.arange(len(ENERGY_VARIANTS))
    width = 0.25
    lambda_z_colors = {2.0: 'steelblue', 4.0: 'darkorange'}

    for j, lambda_z in enumerate(LAMBDA_Z_VALS):
        barriers = []
        for variant_name, _ in ENERGY_VARIANTS:
            v_rows = [r for r in all_rows if r['variant'] == variant_name]
            row = next((r for r in v_rows if r['adj'] == 'smooth'
                        and float(r['delta_z']) == 1.0 and float(r['lambda_z']) == lambda_z), None)
            b = float(row['barrier_neb']) if (row and not _isnan(row['barrier_neb'])) else 0.0
            barriers.append(b)
        ax2.bar(x_positions + j * width - width / 2, barriers, width=width,
                label=f'smooth λ_z={lambda_z}', color=lambda_z_colors.get(lambda_z))

    # Flat baselines
    flat_barriers = []
    for variant_name, _ in ENERGY_VARIANTS:
        row = next((r for r in all_rows if r['variant'] == variant_name and r['adj'] == 'flat'), None)
        flat_barriers.append(float(row['barrier_neb']) if (row and not _isnan(row['barrier_neb'])) else 0.0)
    ax2.plot(x_positions, flat_barriers, 'ks--', linewidth=1.5, label='flat baseline', zorder=5)

    ax2.set_xticks(x_positions)
    ax2.set_xticklabels([v for v, _ in ENERGY_VARIANTS])
    ax2.set_ylabel("NEB barrier ΔE")
    ax2.set_title(f"exp02d: Barrier by energy variant at Δz=1.0  (β={BETA})")
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plot2_path = os.path.join(RESULT_DIR, "exp02d_barrier_by_variant.png")
    plt.savefig(plot2_path, dpi=100)
    plt.close()
    print(f"Plot: {plot2_path}")


def _isnan(x) -> bool:
    try:
        return np.isnan(float(x))
    except (TypeError, ValueError):
        return True


if __name__ == '__main__':
    main()
