#!/usr/bin/env python3
"""Experiment 38: Energy barrier height between K=2 and K=1 minima.

Quantifies the kinetic stability of multi-formation configurations by
computing the energy barrier along interpolation paths from the K=2
state to the K=1 (merged) state.

Method:
  1. Find K=2 formations (with repulsion) and K=1 merged formation.
  2. Combine K=2 fields into a single field u_K2 = clip(u1+u2, 0, 1).
  3. Linear interpolation: u(α) = (1-α)*u_K2 + α*u_K1, α ∈ [0,1].
  4. At each α: project to Σ_{m_total}, compute E_self(u(α)).
  5. Barrier = max_α E(α) - max(E(0), E(1)).

Configs:
  A) 15×15 grid, β ∈ {20, 30, 50, 100}
  B) Dumbbell (8×8 clusters), bridge_width ∈ {1, 4}, β=50
  C) Refined path (few gradient steps at each α) for 15×15 β=50
"""
import sys, os, json, time
import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.multi import find_k_formations
from scc.energy import EnergyComputer


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_params(beta=50.0, vol_frac=0.3):
    return ParameterRegistry(
        beta_bd=beta,
        volume_fraction=vol_frac,
        max_iter=5000,
        n_restarts=3,
        eps_grad=1e-3,
    )


def make_dumbbell(cluster_size=8, bridge_width=1):
    """Two cluster_size×cluster_size grids connected by bridge_width edges."""
    cs = cluster_size
    rows, cols = cs, 2 * cs
    n = rows * cols
    row_idx, col_idx = [], []

    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            if c + 1 < cols:
                if c == cs - 1:
                    mid = cs // 2
                    half_bw = bridge_width // 2
                    lo = max(0, mid - half_bw)
                    hi = min(cs, mid - half_bw + bridge_width)
                    if lo <= r < hi:
                        row_idx.extend([idx, idx + 1])
                        col_idx.extend([idx + 1, idx])
                else:
                    row_idx.extend([idx, idx + 1])
                    col_idx.extend([idx + 1, idx])
            if r + 1 < rows:
                idx2 = (r + 1) * cols + c
                row_idx.extend([idx, idx2])
                col_idx.extend([idx2, idx])

    data = np.ones(len(row_idx))
    W = sp.csr_matrix((data, (row_idx, col_idx)), shape=(n, n))
    return GraphState(W)


def energy_path_linear(u_start, u_end, m_total, graph, params, n_steps=51):
    """Compute energy along linear interpolation from u_start to u_end.

    Returns (alphas, energies, energy_terms_list).
    """
    ec = EnergyComputer(graph, params)
    alphas = np.linspace(0.0, 1.0, n_steps)
    energies = []
    terms_list = []

    for alpha in alphas:
        u_interp = (1.0 - alpha) * u_start + alpha * u_end
        u_interp = project_volume(np.clip(u_interp, 0.0, 1.0), m_total)
        E, terms = ec.energy(u_interp)
        energies.append(E)
        terms_list.append(terms)

    return alphas, np.array(energies), terms_list


def energy_path_refined(u_start, u_end, m_total, graph, params,
                        n_steps=51, n_grad_steps=10, lr=0.01):
    """Energy path with a few gradient descent steps at each interpolation point.

    This gives a lower energy path closer to the minimum energy path (MEP).
    """
    ec = EnergyComputer(graph, params)
    alphas = np.linspace(0.0, 1.0, n_steps)
    energies = []
    terms_list = []

    for alpha in alphas:
        u = (1.0 - alpha) * u_start + alpha * u_end
        u = np.clip(u, 0.0, 1.0)
        u = project_volume(u, m_total)

        # A few projected gradient descent steps to relax
        for _ in range(n_grad_steps):
            g = ec.gradient_projected(u)
            u = u - lr * g
            u = np.clip(u, 0.0, 1.0)
            u = project_volume(u, m_total)

        E, terms = ec.energy(u)
        energies.append(E)
        terms_list.append(terms)

    return alphas, np.array(energies), terms_list


def compute_barrier(energies):
    """Barrier = max(E) - max(E[0], E[-1]). Returns (barrier, alpha_max_idx)."""
    E_max = np.max(energies)
    E_endpoints = max(energies[0], energies[-1])
    barrier = E_max - E_endpoints
    alpha_max_idx = int(np.argmax(energies))
    return float(barrier), alpha_max_idx


def find_k2_and_k1(graph, params, lambda_rep=10.0):
    """Find K=2 formations and merged K=1 formation. Returns (k2_results, k1_result, m_total)."""
    # K=2
    k2 = find_k_formations(
        graph, params, K=2,
        lambda_rep=lambda_rep, lambda_bar=100.0,
        n_restarts=3, max_iter=3000,
    )
    u1, u2 = k2[0].u, k2[1].u
    m_total = float(np.sum(u1) + np.sum(u2))
    n = graph.n

    # Merged K=1
    u_merged_init = np.clip(u1 + u2, 0.0, 1.0)
    u_merged_init = project_volume(u_merged_init, m_total)

    vf = m_total / n
    vf = max(0.22, min(0.78, vf))
    params_merged = ParameterRegistry(
        beta_bd=params.beta_bd,
        volume_fraction=vf,
        max_iter=5000,
        n_restarts=1,
        eps_grad=1e-3,
    )
    k1 = find_formation(graph, params_merged)

    # Re-project K=1 to same total volume
    u_k1 = project_volume(k1.u, m_total)

    return k2, k1, u_k1, m_total


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def run_config(graph, params, label, lambda_rep=10.0, do_refined=False):
    """Run barrier computation for one configuration."""
    print(f"\n{'='*70}")
    print(f"  {label}")
    print(f"{'='*70}")

    t0 = time.time()
    k2, k1, u_k1, m_total = find_k2_and_k1(graph, params, lambda_rep)
    u1, u2 = k2[0].u, k2[1].u
    u_k2 = np.clip(u1 + u2, 0.0, 1.0)
    u_k2 = project_volume(u_k2, m_total)

    # Energy at endpoints
    ec = EnergyComputer(graph, params)
    E_K2, terms_K2 = ec.energy(u_k2)
    E_K1, terms_K1 = ec.energy(u_k1)

    E_K2_self = k2[0].energy + k2[1].energy

    print(f"  K=2 self-energy (sum):  {E_K2_self:.6f}")
    print(f"  K=2 combined field E:   {E_K2:.6f}")
    print(f"  K=1 merged E:           {E_K1:.6f}")
    print(f"  m_total = {m_total:.2f}")

    # Linear interpolation
    alphas, energies, terms_list = energy_path_linear(
        u_k2, u_k1, m_total, graph, params, n_steps=51
    )
    barrier_lin, alpha_max_idx = compute_barrier(energies)
    alpha_max = alphas[alpha_max_idx]

    print(f"  Linear barrier:         {barrier_lin:.6f}")
    print(f"  Barrier at α =          {alpha_max:.3f}")

    result = {
        'label': label,
        'E_K2_self': float(E_K2_self),
        'E_K2_combined': float(E_K2),
        'E_K1': float(E_K1),
        'barrier_linear': float(barrier_lin),
        'alpha_max_linear': float(alpha_max),
        'alphas': alphas.tolist(),
        'energies_linear': energies.tolist(),
    }

    # Refined path
    if do_refined:
        print("  Computing refined path (gradient relaxation)...")
        alphas_r, energies_r, terms_r = energy_path_refined(
            u_k2, u_k1, m_total, graph, params,
            n_steps=51, n_grad_steps=15, lr=0.005
        )
        barrier_ref, alpha_max_ref_idx = compute_barrier(energies_r)
        alpha_max_ref = alphas_r[alpha_max_ref_idx]
        print(f"  Refined barrier:        {barrier_ref:.6f}")
        print(f"  Refined barrier at α =  {alpha_max_ref:.3f}")

        result['barrier_refined'] = float(barrier_ref)
        result['alpha_max_refined'] = float(alpha_max_ref)
        result['energies_refined'] = energies_r.tolist()

    elapsed = time.time() - t0
    result['elapsed'] = elapsed
    print(f"  Elapsed: {elapsed:.1f}s")
    return result


def main():
    print("=" * 70)
    print("  EXP38: Energy Barrier Height (K=2 → K=1)")
    print("=" * 70)

    all_results = []

    # --- Config A: 15×15 grid, varying β ---
    print("\n\n### CONFIG A: 15×15 grid, β sweep ###")
    grid_15 = GraphState.grid_2d(15, 15)
    betas = [20, 30, 50, 100]

    for beta in betas:
        params = make_params(beta=beta)
        label = f"Grid 15x15, β={beta}"
        do_ref = (beta == 50)  # refined path only for β=50
        result = run_config(grid_15, params, label, lambda_rep=10.0,
                            do_refined=do_ref)
        result['config'] = 'grid_15x15'
        result['beta'] = beta
        all_results.append(result)

    # --- Config B: Dumbbell, varying bridge width ---
    print("\n\n### CONFIG B: Dumbbell (8×8 clusters), β=50 ###")
    for bw in [1, 4]:
        graph = make_dumbbell(cluster_size=8, bridge_width=bw)
        params = make_params(beta=50.0)
        label = f"Dumbbell 8x8, bridge={bw}, β=50"
        result = run_config(graph, params, label, lambda_rep=10.0,
                            do_refined=False)
        result['config'] = f'dumbbell_bw{bw}'
        result['beta'] = 50
        result['bridge_width'] = bw
        all_results.append(result)

    # --- Summary table ---
    print("\n\n" + "=" * 90)
    print("  SUMMARY TABLE")
    print("=" * 90)
    header = f"{'Config':<35} {'E_K2':>10} {'E_K1':>10} {'Barrier':>10} {'Refined':>10} {'α_max':>8}"
    print(header)
    print("-" * 90)
    for r in all_results:
        ref = r.get('barrier_refined', None)
        ref_str = f"{ref:.6f}" if ref is not None else "—"
        print(f"{r['label']:<35} {r['E_K2_combined']:>10.4f} {r['E_K1']:>10.4f} "
              f"{r['barrier_linear']:>10.6f} {ref_str:>10} {r['alpha_max_linear']:>8.3f}")

    # --- Barrier scaling with β ---
    grid_results = [r for r in all_results if r['config'] == 'grid_15x15']
    if len(grid_results) > 1:
        print("\n\n### BARRIER SCALING WITH β ###")
        betas_arr = np.array([r['beta'] for r in grid_results])
        barriers_arr = np.array([r['barrier_linear'] for r in grid_results])
        # Log-log slope
        if np.all(barriers_arr > 0) and len(betas_arr) > 1:
            log_b = np.log(betas_arr)
            log_bar = np.log(barriers_arr)
            slope = np.polyfit(log_b, log_bar, 1)[0]
            print(f"  Log-log slope (barrier ~ β^γ): γ = {slope:.3f}")
            for b, bar in zip(betas_arr, barriers_arr):
                print(f"  β={b:>5.0f}  barrier={bar:.6f}")

    # --- Save JSON ---
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'results', 'exp38_barrier_height.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    # Convert for JSON serialization
    save_results = []
    for r in all_results:
        sr = {k: v for k, v in r.items()}
        save_results.append(sr)

    with open(out_path, 'w') as f:
        json.dump(save_results, f, indent=2)
    print(f"\nResults saved to {out_path}")
    print("DONE.")


if __name__ == '__main__':
    main()
