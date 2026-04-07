"""Exp64: Decompose merge barrier by energy term (E_bd, E_cl, E_sep).

The existing barrier derivation (BARRIER-EXPONENT.md) analyzes only E_bd,
but exp38 measures total weighted energy. This experiment decomposes the
barrier to determine which terms contribute and at what scaling.

For each β: compute the per-term barrier along the LI path and fit scaling.
"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.multi import find_k_formations
from scc.energy import (EnergyComputer, energy_bd, energy_cl, energy_sep)


def decompose_barrier(grid_size=15, betas=[20, 30, 50, 100], vol_frac=0.3):
    graph = GraphState.grid_2d(grid_size, grid_size)
    n = graph.n
    n_steps = 51

    all_results = {}

    for beta in betas:
        print(f"\n{'='*50}")
        print(f"β = {beta}")
        params = ParameterRegistry(
            beta_bd=beta, volume_fraction=vol_frac,
            max_iter=5000, n_restarts=3, eps_grad=1e-3
        )

        # Find K=2 and K=1
        k2_results = find_k_formations(graph, params, K=2, n_restarts=5)
        u1_f = k2_results[0].u
        u2_f = k2_results[1].u
        u_k2 = np.clip(u1_f + u2_f, 0, 1)
        m_total = np.sum(u_k2)

        k1_result = find_formation(graph, params)
        u_k1 = k1_result.u
        # Rescale K=1 to same total mass
        u_k1 = project_volume(u_k1, m_total)

        # Energy computer WITHOUT normalization (raw weights w_cl=w_sep=w_bd=1)
        # This matches exp38 which does NOT call normalize_weights
        ec = EnergyComputer(graph, params)

        # Compute per-term energies along LI path
        alphas = np.linspace(0, 1, n_steps)
        E_total = []
        E_bd_list = []
        E_cl_list = []
        E_sep_list = []

        for alpha in alphas:
            u = (1 - alpha) * u_k2 + alpha * u_k1
            u = project_volume(np.clip(u, 0, 1), m_total)

            e_bd = energy_bd(u, graph, params)
            e_cl = energy_cl(u, graph, params)
            e_sep = energy_sep(u, graph, params)

            # Weighted energies (same as EnergyComputer)
            E_bd_list.append(ec.lambda_bd * e_bd)
            E_cl_list.append(ec.lambda_cl * e_cl)
            E_sep_list.append(ec.lambda_sep * e_sep)
            E_total.append(ec.lambda_bd * e_bd + ec.lambda_cl * e_cl + ec.lambda_sep * e_sep)

        E_total = np.array(E_total)
        E_bd_arr = np.array(E_bd_list)
        E_cl_arr = np.array(E_cl_list)
        E_sep_arr = np.array(E_sep_list)

        # Per-term barriers
        def barrier(E):
            return float(np.max(E) - max(E[0], E[-1]))

        b_total = barrier(E_total)
        b_bd = barrier(E_bd_arr)
        b_cl = barrier(E_cl_arr)
        b_sep = barrier(E_sep_arr)

        # Also compute: at α where total is max, what are per-term values?
        idx_max = np.argmax(E_total)
        alpha_max = alphas[idx_max]

        # Per-term contribution at barrier peak
        delta_bd = E_bd_arr[idx_max] - max(E_bd_arr[0], E_bd_arr[-1])
        delta_cl = E_cl_arr[idx_max] - max(E_cl_arr[0], E_cl_arr[-1])
        delta_sep = E_sep_arr[idx_max] - max(E_sep_arr[0], E_sep_arr[-1])

        print(f"  m_total = {m_total:.1f}")
        print(f"  λ_bd={ec.lambda_bd:.4f}, λ_cl={ec.lambda_cl:.4f}, λ_sep={ec.lambda_sep:.4f}")
        print(f"  Barrier (total): {b_total:.4f}")
        print(f"  Barrier (bd):    {b_bd:.4f}")
        print(f"  Barrier (cl):    {b_cl:.4f}")
        print(f"  Barrier (sep):   {b_sep:.4f}")
        print(f"  At peak (α={alpha_max:.2f}):")
        print(f"    ΔE_bd  = {delta_bd:+.4f}")
        print(f"    ΔE_cl  = {delta_cl:+.4f}")
        print(f"    ΔE_sep = {delta_sep:+.4f}")
        print(f"    Sum    = {delta_bd+delta_cl+delta_sep:.4f} (total={b_total:.4f})")

        # Reorganization region analysis
        diff = np.abs(u_k2 - u_k1)
        R_count = np.sum(diff > 0.5)  # nodes that flip significantly
        R_partial = np.sum((diff > 0.1) & (diff <= 0.5))

        print(f"  |R| (>0.5): {R_count}, |R_partial| (0.1-0.5): {R_partial}")

        all_results[str(beta)] = {
            'beta': beta,
            'barrier_total': b_total,
            'barrier_bd': b_bd,
            'barrier_cl': b_cl,
            'barrier_sep': b_sep,
            'delta_bd_at_peak': float(delta_bd),
            'delta_cl_at_peak': float(delta_cl),
            'delta_sep_at_peak': float(delta_sep),
            'alpha_max': float(alpha_max),
            'R_count': int(R_count),
            'R_partial': int(R_partial),
            'm_total': float(m_total),
        }

    # Scaling analysis
    print(f"\n{'='*60}")
    print("SCALING ANALYSIS")
    betas_arr = np.array(betas, dtype=float)
    for name in ['barrier_total', 'barrier_bd', 'barrier_cl', 'barrier_sep']:
        vals = np.array([all_results[str(b)][name] for b in betas])
        # Filter positive values for log fit
        mask = vals > 0
        if np.sum(mask) >= 2:
            log_b = np.log(betas_arr[mask])
            log_v = np.log(vals[mask])
            slope, intercept = np.polyfit(log_b, log_v, 1)
            C = np.exp(intercept)
            print(f"  {name:20s}: γ = {slope:.3f}, C = {C:.3f}, vals = {vals.round(3)}")
        else:
            print(f"  {name:20s}: insufficient positive data, vals = {vals.round(3)}")

    # Fraction of barrier from each term
    print(f"\n{'='*60}")
    print("BARRIER FRACTION BY TERM")
    print(f"{'β':>6} {'%E_bd':>8} {'%E_cl':>8} {'%E_sep':>8}")
    for b in betas:
        r = all_results[str(b)]
        total = r['barrier_total']
        if total > 0:
            print(f"{b:6.0f} {r['delta_bd_at_peak']/total*100:8.1f} {r['delta_cl_at_peak']/total*100:8.1f} {r['delta_sep_at_peak']/total*100:8.1f}")

    with open('/home/jack/ex/experiments/results/exp64_barrier_decomposition.json', 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved to experiments/results/exp64_barrier_decomposition.json")

    return all_results


if __name__ == '__main__':
    decompose_barrier()
