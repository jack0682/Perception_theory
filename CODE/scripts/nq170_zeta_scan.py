"""NQ-170: ζ-scan to quantify Theorem 1 V5b sub/super-lattice crossover boundary.

Tests V5b prediction:
  - ζ ≤ 0.2 (sub-lattice): max translation overlap < 0.5, no Goldstone, orbital only
  - ζ ≥ 0.5 (super-lattice): max translation overlap > 0.9, Goldstone present
  - ζ ∈ [0.3, 0.4] (crossover): smooth transition

Protocol:
  1. ζ ∈ {0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0} × N=3 random seeds × L=20 torus
  2. β = 1/ζ² (so ξ_0 = sqrt(α/β) = ζ; with α=1, lattice spacing a=1, gives ζ = ξ_0/a)
  3. Find F=1 minimizer of pure E_bd
  4. Compute Hessian lowest 4 eigenpairs + translation overlap projections
  5. Quantify max(overlap_x, overlap_y) for Mode 1 vs ζ
  6. Identify crossover ζ_* (e.g., where max_overlap crosses 0.5)

Run: cd CODE && python3 scripts/nq170_zeta_scan.py
Output: scripts/results/nq170_zeta_scan.json
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
    data_arr = np.ones(len(rows))
    W = sp.csr_matrix((data_arr, (rows, cols)), shape=(n, n))
    return GraphState(W)


def count_local_maxima_torus(u, L):
    g = u.reshape(L, L)
    F = 0
    for i in range(L):
        for j in range(L):
            v = g[i, j]
            is_max = all(g[(i + di) % L, (j + dj) % L] < v
                         for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)])
            if is_max:
                F += 1
    return F


def translation_modes(u, L):
    """Normalized δu_x, δu_y (translation Goldstone basis)."""
    g = u.reshape(L, L)
    du_x = (np.roll(g, -1, axis=0) - g).flatten()
    du_y = (np.roll(g, -1, axis=1) - g).flatten()
    du_x /= (np.linalg.norm(du_x) + 1e-14)
    du_y /= (np.linalg.norm(du_y) + 1e-14)
    return du_x, du_y


def compute_hessian_lowest(u_star, graph, params, n_modes=4, eps=1e-4):
    """Finite-difference Hessian projected onto tangent space, lowest n_modes."""
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
    eigvals, eigvecs = np.linalg.eigh(H_proj)
    idx = np.argsort(eigvals)
    return eigvals[idx[:n_modes]], eigvecs[:, idx[:n_modes]]


def find_F1_minimizer(L, beta, c, seed):
    """Find F=1 torus-disk minimizer from random IC, pure E_bd."""
    graph = build_torus_graph(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=15000,
    )
    xi_0 = np.sqrt(1.0 / beta)
    r0 = np.sqrt(c * L * L / np.pi)
    np.random.seed(seed * 41 + 11)
    cx = np.random.uniform(0.5, L - 0.5)
    cy = np.random.uniform(0.5, L - 0.5)
    i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
    dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
    r = np.sqrt(dx**2 + dy**2).flatten()
    ic_width = max(xi_0, 0.2)
    u_init = 0.5 * (1.0 - np.tanh((r - r0) / ic_width))
    u_init = np.clip(u_init + np.random.normal(0, 0.02, size=L*L), 0.01, 0.99)
    try:
        res = find_formation(graph, params, normalize=False, verbose=False, u_init=u_init)
        if not res.converged:
            return None
        F = count_local_maxima_torus(res.u, L)
        return {'u': res.u, 'F': F, 'energy': float(res.energy),
                'graph': graph, 'params': params, 'seed': seed}
    except Exception as e:
        return {'error': str(e)}


def analyze_one(result, L, zeta):
    """Compute spectral data + translation overlap for the lowest non-tangent mode."""
    u = result['u']
    graph = result['graph']
    params = result['params']
    du_x, du_y = translation_modes(u, L)
    try:
        eigvals, eigvecs = compute_hessian_lowest(u, graph, params, n_modes=4)
    except Exception as e:
        return {'error': str(e)}

    # Mode 0: tangent (near-zero); Mode 1: lowest physical mode
    overlaps = []
    for k in range(eigvecs.shape[1]):
        v = eigvecs[:, k]
        ov_x = float(abs(np.dot(v, du_x)))
        ov_y = float(abs(np.dot(v, du_y)))
        overlaps.append({'mode': k, 'eigenvalue': float(eigvals[k]),
                         'overlap_x': ov_x, 'overlap_y': ov_y,
                         'max_overlap': float(max(ov_x, ov_y))})
    # Mode 1 (lowest physical) — V5b prediction target
    mode1 = overlaps[1]
    return {
        'zeta': zeta,
        'L': L,
        'seed': result['seed'],
        'F': result['F'],
        'energy': result['energy'],
        'mode1_eigenvalue': mode1['eigenvalue'],
        'mode1_overlap_x': mode1['overlap_x'],
        'mode1_overlap_y': mode1['overlap_y'],
        'mode1_max_overlap': mode1['max_overlap'],
        'all_overlaps': overlaps,
    }


def main():
    print("=" * 70)
    print("NQ-170: ζ-scan for Theorem 1 V5b crossover quantification")
    print("=" * 70)

    L = 20
    c = 0.5
    N_seeds = 3
    zetas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0]

    report = {
        'L': L,
        'c': c,
        'N_seeds': N_seeds,
        'zetas': zetas,
        'protocol': 'pure E_bd (lambda_cl=0, lambda_sep=0); F=1 torus disk; H_bd lowest 4 modes; translation overlap',
        'results': [],
    }

    for zeta in zetas:
        beta = 1.0 / (zeta ** 2)  # xi_0 = sqrt(1/beta) = zeta
        print(f"\n--- ζ = {zeta} (β = {beta:.3f}) ---")
        for seed in range(N_seeds):
            t0 = time.time()
            res = find_F1_minimizer(L, beta, c, seed)
            if res is None or 'error' in res:
                print(f"  seed={seed}: FAILED ({res})")
                continue
            if res['F'] != 1:
                print(f"  seed={seed}: F={res['F']} (not F=1, skip)")
                continue
            rec = analyze_one(res, L, zeta)
            if 'error' in rec:
                print(f"  seed={seed}: analysis error ({rec['error']})")
                continue
            dt = time.time() - t0
            print(f"  seed={seed}: λ_1={rec['mode1_eigenvalue']:.4e}, "
                  f"max_overlap={rec['mode1_max_overlap']:.3f} "
                  f"(ov_x={rec['mode1_overlap_x']:.3f}, ov_y={rec['mode1_overlap_y']:.3f}) "
                  f"({dt:.1f}s)")
            report['results'].append(rec)

    # Aggregate by ζ
    print("\n=== ζ vs Mode 1 max overlap (V5b crossover) ===")
    by_zeta = {}
    for r in report['results']:
        z = r['zeta']
        by_zeta.setdefault(z, []).append(r['mode1_max_overlap'])

    aggregate = {}
    for z in sorted(by_zeta.keys()):
        vals = by_zeta[z]
        aggregate[z] = {
            'n': len(vals),
            'mean_max_overlap': float(np.mean(vals)),
            'min_max_overlap': float(min(vals)),
            'max_max_overlap': float(max(vals)),
            'std_max_overlap': float(np.std(vals)),
        }
        print(f"  ζ={z}: n={len(vals)}, mean_max_overlap={np.mean(vals):.3f} "
              f"(range [{min(vals):.3f}, {max(vals):.3f}])")
    report['aggregate_by_zeta'] = aggregate

    # Identify crossover ζ_* where mean_max_overlap crosses 0.5
    print("\n=== Crossover ζ_* identification ===")
    sorted_z = sorted(by_zeta.keys())
    z_below = [z for z in sorted_z if aggregate[z]['mean_max_overlap'] < 0.5]
    z_above = [z for z in sorted_z if aggregate[z]['mean_max_overlap'] >= 0.5]
    if z_below and z_above:
        z_low = max(z_below)
        z_high = min(z_above)
        # Linear interpolation
        ov_low = aggregate[z_low]['mean_max_overlap']
        ov_high = aggregate[z_high]['mean_max_overlap']
        if ov_high > ov_low:
            zeta_star = z_low + (0.5 - ov_low) * (z_high - z_low) / (ov_high - ov_low)
            print(f"  ζ_* (overlap=0.5 crossing): ≈ {zeta_star:.3f}")
            print(f"  bracketed by: ζ={z_low} (overlap={ov_low:.3f}) and ζ={z_high} (overlap={ov_high:.3f})")
            report['crossover_zeta_star'] = float(zeta_star)
            report['crossover_bracket'] = [float(z_low), float(z_high)]
        else:
            print(f"  Non-monotone — V5b crossover hypothesis FALSIFIED?")
            report['crossover_zeta_star'] = None
            report['crossover_falsified'] = True
    else:
        print(f"  ζ-range insufficient — no crossing observed in [{sorted_z[0]}, {sorted_z[-1]}]")
        report['crossover_zeta_star'] = None
        report['crossover_unbracketed'] = True

    # V5b prediction check
    print("\n=== V5b prediction check ===")
    print(f"  Sub-lattice (ζ ≤ 0.2): expect max_overlap < 0.5")
    sub_check = [aggregate[z]['mean_max_overlap'] for z in sorted_z if z <= 0.2]
    print(f"    Observed: {[f'{v:.3f}' for v in sub_check]} → "
          f"{'PASS' if all(v < 0.5 for v in sub_check) else 'FAIL'}")
    print(f"  Super-lattice (ζ ≥ 0.5): expect max_overlap > 0.9")
    super_check = [aggregate[z]['mean_max_overlap'] for z in sorted_z if z >= 0.5]
    print(f"    Observed: {[f'{v:.3f}' for v in super_check]} → "
          f"{'PASS' if all(v > 0.9 for v in super_check) else 'FAIL'}")
    report['v5b_sub_lattice_pass'] = bool(all(v < 0.5 for v in sub_check)) if sub_check else None
    report['v5b_super_lattice_pass'] = bool(all(v > 0.9 for v in super_check)) if super_check else None

    # Save
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'nq170_zeta_scan.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\n=== RESULTS SAVED: {out_path} ===")


if __name__ == "__main__":
    main()
