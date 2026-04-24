"""Dual-regime Phase B: ζ = ξ_0/a scan — test Dual-Regime Spectrum Theorem.

Predictions (from 23_dual_regime_formalization.md):
  ζ < 1: λ_0 = O(β), genuine orbital, ratio λ_0/λ_1 ≈ 1
  ζ > 1: λ_0 << λ_1, Goldstone-like
  ζ = 1: sharp transition

Scan: L=16, c=0.5, α=1, varying β such that ζ = √(α/β) ∈ {0.18, 0.3, 0.5, 0.8, 1.0, 1.3, 1.8, 2.4}.

Both torus and free-BC center-aligned.

Run: cd CODE && python3 scripts/dual_regime_zeta_scan.py
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import grad_bd


def build_torus_graph(L):
    n = L * L
    rows, cols = [], []
    for i in range(L):
        for j in range(L):
            idx = i * L + j
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = (i + di) % L, (j + dj) % L
                nidx = ni * L + nj
                rows.append(idx)
                cols.append(nidx)
    data = np.ones(len(rows))
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W)


def count_local_maxima_periodic(u, L, periodic):
    g = u.reshape(L, L)
    F = 0
    for i in range(L):
        for j in range(L):
            v = g[i, j]
            ok = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if periodic:
                    ni, nj = (i + di) % L, (j + dj) % L
                else:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= L or nj < 0 or nj >= L:
                        continue
                if g[ni, nj] >= v:
                    ok = False
                    break
            if ok:
                F += 1
    return F


def compute_hessian_pure_bd(u_star, graph, params, n_modes=8, eps=1e-4):
    n = graph.n
    g0 = grad_bd(u_star, graph, params)
    H = np.zeros((n, n))
    for i in range(n):
        u_p = u_star.copy()
        u_p[i] += eps
        g_p = grad_bd(u_p, graph, params)
        H[:, i] = (g_p - g0) / eps
    H = (H + H.T) / 2.0
    one = np.ones(n)
    P = np.eye(n) - np.outer(one, one) / n
    H_proj = P @ H @ P
    eigvals = np.linalg.eigvalsh(H_proj)
    eigvals.sort()
    return eigvals[:n_modes + 1]


def find_F1_disk(L, beta, graph_type, c=0.5, n_tries=15):
    if graph_type == 'torus':
        graph = build_torus_graph(L)
        periodic = True
    else:
        graph = GraphState.grid_2d(L, L)
        periodic = False

    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=2, max_iter=8000,
    )

    xi_0 = np.sqrt(1.0 / beta)
    r0 = np.sqrt(c * L * L / np.pi)
    # Adaptive IC width: in super-lattice, use xi_0; in sub-lattice, use 1
    ic_width = max(xi_0, 0.5)

    best = None
    for seed in range(n_tries):
        np.random.seed(seed * 13 + 7)
        if graph_type == 'torus':
            cx = np.random.uniform(0, L)
            cy = np.random.uniform(0, L)
            i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
            dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
            dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
            r = np.sqrt(dx**2 + dy**2).flatten()
        else:
            i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
            r = np.sqrt((i_idx - L/2)**2 + (j_idx - L/2)**2).flatten()
        u_init = 0.5 * (1.0 - np.tanh((r - r0) / ic_width))
        u_init = np.clip(u_init + np.random.normal(0, 0.02, size=L*L), 0.01, 0.99)
        try:
            res = find_formation(graph, params, normalize=False, verbose=False, u_init=u_init)
            if res.converged:
                F = count_local_maxima_periodic(res.u, L, periodic)
                if F == 1 and (best is None or res.energy < best[1]):
                    best = (res.u, res.energy, graph, params, periodic)
        except Exception:
            pass
    return best


def main():
    L = 16
    c = 0.5
    alpha = 1.0

    # Zeta values to scan
    # zeta = sqrt(alpha/beta), so beta = alpha / zeta^2
    zetas_target = [0.18, 0.3, 0.5, 0.8, 1.0, 1.3, 1.8, 2.4]
    beta_list = [alpha / z**2 for z in zetas_target]

    # Check β > β_crit for L=16 Fiedler
    # lambda_2 for free-BC 16x16 ≈ 2(1-cos(π/15)) ≈ 0.0438
    # beta_crit ≈ 4*alpha*lambda_2 / |W''(c)| = 4*0.0438 ≈ 0.175
    beta_crit = 0.175
    valid_idx = [i for i, b in enumerate(beta_list) if b > beta_crit * 1.2]
    zetas = [zetas_target[i] for i in valid_idx]
    betas = [beta_list[i] for i in valid_idx]
    print(f"=== Dual-Regime ζ scan (L={L}, α={alpha}, c={c}) ===")
    print(f"β_crit ≈ {beta_crit}")
    print(f"Valid ζ values: {zetas}")
    print(f"Corresponding β values: {[f'{b:.3f}' for b in betas]}")

    results_torus = []
    results_free = []
    t0_all = time.time()

    for graph_type, results in [('torus', results_torus), ('free_bc', results_free)]:
        print(f"\n\n{'='*60}")
        print(f"Graph type: {graph_type}")
        print('='*60)
        for zeta, beta in zip(zetas, betas):
            print(f"\n--- ζ={zeta:.2f}, β={beta:.3f} ---")
            xi_0 = np.sqrt(alpha / beta)
            r0 = np.sqrt(c * L * L / np.pi)
            t0 = time.time()
            found = find_F1_disk(L, beta, graph_type, c=c, n_tries=10)
            if found is None:
                print(f"  No F=1 disk found.")
                continue
            u_disk, energy, graph, params, periodic = found
            F = count_local_maxima_periodic(u_disk, L, periodic)

            print(f"  F={F}, energy={energy:.4f}, ξ_0={xi_0:.3f}, r_0/ξ_0={r0/xi_0:.2f}")

            eigs = compute_hessian_pure_bd(u_disk, graph, params, n_modes=6, eps=1e-4)
            eigs_str = [f'{e:.4g}' for e in eigs[:6]]
            print(f"  Eigenvalues [0:6]: {eigs_str}")

            lam_t = eigs[0]
            lam_0 = eigs[1]
            lam_1 = eigs[2]
            lam_2 = eigs[3]

            ratio_01 = lam_0 / lam_1 if lam_1 > 1e-10 else None
            ratio_02 = lam_0 / lam_2 if lam_2 > 1e-10 else None

            print(f"  λ_tangent={lam_t:.2e}, λ_0={lam_0:.4f}, λ_1={lam_1:.4f}, λ_2={lam_2:.4f}")
            r01_str = f"{ratio_01:.3f}" if ratio_01 is not None else "NA"
            r02_str = f"{ratio_02:.3f}" if ratio_02 is not None else "NA"
            print(f"  λ_0/λ_1={r01_str}, λ_0/λ_2={r02_str}")
            print(f"  λ_0/β={lam_0/beta:.3f}")

            runtime = time.time() - t0
            print(f"  Runtime: {runtime:.1f}s")

            results.append({
                'zeta': zeta, 'beta': beta,
                'xi_0': float(xi_0), 'r_0': float(r0),
                'F': int(F), 'energy': float(energy),
                'eigs': [float(e) for e in eigs.tolist()],
                'lam_tangent': float(lam_t),
                'lam_0': float(lam_0), 'lam_1': float(lam_1), 'lam_2': float(lam_2),
                'ratio_01': float(ratio_01) if ratio_01 else None,
                'ratio_02': float(ratio_02) if ratio_02 else None,
                'lam0_over_beta': float(lam_0 / beta),
                'runtime_sec': runtime,
            })

    # Save
    out = os.path.join(os.path.dirname(__file__), 'results', 'dual_regime_zeta_scan.json')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump({
            'L': L, 'c': c, 'alpha': alpha,
            'zetas': zetas, 'betas': betas,
            'results_torus': results_torus,
            'results_free_bc': results_free,
        }, f, indent=2)
    print(f"\nTotal runtime: {time.time() - t0_all:.1f}s")
    print(f"Saved: {out}")

    # Summary table
    print("\n" + "="*70)
    print("DUAL-REGIME SCAN SUMMARY")
    print("="*70)
    for graph_type, results in [('torus', results_torus), ('free_bc', results_free)]:
        print(f"\n--- {graph_type} ---")
        print(f"{'ζ':>6} {'β':>8} {'λ_0':>10} {'λ_0/λ_2':>10} {'λ_0/β':>10} {'regime':>12}")
        for r in results:
            ratio = r.get('ratio_02')
            lam0_over_beta = r['lam0_over_beta']
            if ratio is None:
                regime = 'NA'
            elif ratio < 0.1 and lam0_over_beta < 0.1:
                regime = 'SUPER (G)'
            elif ratio > 0.5 and lam0_over_beta > 0.3:
                regime = 'SUB (orbit)'
            else:
                regime = 'CROSSOVER'
            ratio_str = f"{ratio:.3f}" if ratio is not None else "NA"
            print(f"{r['zeta']:>6.2f} {r['beta']:>8.3f} {r['lam_0']:>10.4f} {ratio_str:>10} {lam0_over_beta:>10.4f} {regime:>12}")


if __name__ == "__main__":
    main()
