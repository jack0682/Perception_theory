"""NQ-174: ζ_*(graph-class) precise dependence.

W4-04-26 NQ-170c bracketed:
  ζ_*(2D torus) ∈ [0.2, 0.5]  (sub at 0.2, super at 0.5)
  ζ_*(1D cycle) < 0.2          (super at 0.2 already with overlap 0.76)

This script narrows the brackets:

  - 2D torus L=20: ζ ∈ {0.25, 0.30, 0.35, 0.40, 0.45} × N=5 seeds  (25 minimizers)
  - 1D cycle L=40: ζ ∈ {0.05, 0.10, 0.15} × N=5 seeds              (15 minimizers)

Total: 40 minimizer attempts.

Per-minimizer measurement (V5b-T criterion):
  - Mode-agnostic Goldstone overlap of lowest 6 non-tangent eigenmodes.
  - Crossover ζ_* identified as smallest ζ where max_overlap > 0.9 (V5b-T super-lattice).

Mode-agnostic detection (per W4-04-26 NQ-172 lesson + W5 pre_brainstorm §8.4):
  Iterate over all 6 lowest non-tangent eigenmodes; record max overlap.
  Do NOT hardcode `mode_overlaps[1]` or any specific mode index.

Multi-IC strategy (per NQ-170c reuse):
  3 IC widths per (ζ, seed): xi_0, xi_0/2, xi_0*2.

Run: cd CODE && python3 scripts/nq174_zeta_star_precise.py
Output: scripts/results/nq174_zeta_star.json

Expected runtime: ~15-25 min for 40 minimizers (similar scaling to NQ-170c).

Day 1 EOD: script ready. Day 2 morning execution.
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import grad_bd


# === Graph constructors (reused from NQ-170c) ===

def build_torus_2d(L):
    n = L * L
    rows, cols = [], []
    for i in range(L):
        for j in range(L):
            idx = i * L + j
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = (i + di) % L, (j + dj) % L
                rows.append(idx); cols.append(ni * L + nj)
    return GraphState(sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))), n


def build_cycle_1d(L):
    n = L
    rows, cols = [], []
    for i in range(L):
        for di in [-1, 1]:
            rows.append(i); cols.append((i + di) % L)
    return GraphState(sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))), n


# === F count ===

def count_local_maxima(u, graph_class, L):
    if graph_class == '2D_torus':
        g = u.reshape(L, L)
        F = 0
        for i in range(L):
            for j in range(L):
                v = g[i, j]
                if all(g[(i + di) % L, (j + dj) % L] < v
                       for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                    F += 1
        return F
    elif graph_class == '1D_cycle':
        F = 0
        for i in range(L):
            v = u[i]
            if u[(i - 1) % L] < v and u[(i + 1) % L] < v:
                F += 1
        return F


# === Translation modes ===

def translation_modes(u, graph_class, L):
    if graph_class == '2D_torus':
        g = u.reshape(L, L)
        du_x = (np.roll(g, -1, axis=0) - g).flatten()
        du_y = (np.roll(g, -1, axis=1) - g).flatten()
        modes = [('x', du_x), ('y', du_y)]
    elif graph_class == '1D_cycle':
        du_x = np.roll(u, -1) - u
        modes = [('x', du_x)]
    out = []
    for name, m in modes:
        norm = np.linalg.norm(m)
        out.append((name, m / norm if norm > 1e-14 else m))
    return out


# === Hessian ===

def compute_hessian_lowest(u_star, graph, params, n_modes=6, eps=1e-4):
    n = graph.n if hasattr(graph, 'n') else u_star.shape[0]
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


# === Find F=1 minimizer ===

def find_F1_minimizer(graph_class, L, beta, c, seed):
    if graph_class == '2D_torus':
        graph, n = build_torus_2d(L)
    elif graph_class == '1D_cycle':
        graph, n = build_cycle_1d(L)

    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=15000,
    )
    xi_0 = np.sqrt(1.0 / beta)

    if graph_class == '2D_torus':
        r0 = np.sqrt(c * L * L / np.pi)
    else:  # 1D_cycle
        r0 = c * L / 2.0

    ic_widths = [max(xi_0, 0.2), xi_0 * 0.5, xi_0 * 2.0]

    attempts = []
    for ic_id in range(3):
        np.random.seed(seed * 53 + 13 + ic_id * 1000)
        if graph_class == '2D_torus':
            cx = np.random.uniform(0.5, L - 0.5)
            cy = np.random.uniform(0.5, L - 0.5)
            i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
            dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
            dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
            r = np.sqrt(dx**2 + dy**2).flatten()
        else:  # 1D_cycle
            cx = np.random.uniform(0.5, L - 0.5)
            i_idx = np.arange(L)
            r = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))

        u_init = 0.5 * (1.0 - np.tanh((r - r0) / ic_widths[ic_id]))
        u_init = np.clip(u_init + np.random.normal(0, 0.02, size=n), 0.01, 0.99)

        try:
            res = find_formation(graph, params, normalize=False, verbose=False, u_init=u_init)
            if not res.converged:
                continue
            F = count_local_maxima(res.u, graph_class, L)
            attempts.append({'F': F, 'energy': float(res.energy), 'u': res.u, 'ic_id': ic_id})
        except Exception:
            continue

    if not attempts:
        return None
    f1 = [a for a in attempts if a['F'] == 1]
    best = min(f1, key=lambda a: a['energy']) if f1 else min(attempts, key=lambda a: (a['F'], a['energy']))
    best['F1_found'] = bool(f1)
    best['graph'] = graph
    best['params'] = params
    best['n'] = n
    return best


# === Mode-agnostic Goldstone overlap ===

def analyze_minimizer(result, graph_class, L, zeta):
    u = result['u']
    graph = result['graph']
    params = result['params']
    n = result['n']

    trans_modes = translation_modes(u, graph_class, L)
    tangent = np.ones(n) / np.sqrt(n)

    eigvals, eigvecs = compute_hessian_lowest(u, graph, params, n_modes=6)

    best_overlap = -1.0
    best_mode = -1
    best_eigval = float('nan')
    best_overlaps = {}

    for k in range(eigvecs.shape[1]):
        v = eigvecs[:, k]
        ov_t = float(abs(np.dot(v, tangent)))
        if ov_t > 0.5:
            continue  # skip volume tangent
        overlaps = {f'ov_{name}': float(abs(np.dot(v, m))) for name, m in trans_modes}
        max_ov = max(overlaps.values())
        if max_ov > best_overlap:
            best_overlap = max_ov
            best_mode = k
            best_eigval = float(eigvals[k])
            best_overlaps = overlaps

    return {
        'F1_found': result['F1_found'],
        'energy': float(result['energy']),
        'best_mode_idx': best_mode,
        'best_eigval': best_eigval,
        'best_overlap': best_overlap,
        'best_overlaps_per_axis': best_overlaps,
    }


# === Crossover detection ===

def find_zeta_star(per_zeta_data, threshold=0.9):
    """Find smallest ζ where mean overlap (across seeds) > threshold."""
    sorted_zetas = sorted(per_zeta_data.keys())
    for zeta in sorted_zetas:
        overlaps = [r['best_overlap'] for r in per_zeta_data[zeta]
                    if r is not None and 'best_overlap' in r and r['best_overlap'] > 0]
        if overlaps:
            mean_ov = np.mean(overlaps)
            if mean_ov > threshold:
                return zeta, float(mean_ov)
    return None, None


# === Main sweep ===

def main():
    c = 0.10  # volume fraction
    n_seeds = 5
    sweeps = [
        ('2D_torus', 20, [0.25, 0.30, 0.35, 0.40, 0.45]),
        ('1D_cycle', 40, [0.05, 0.10, 0.15]),
    ]

    all_results = {}
    t0 = time.time()

    for graph_class, L, zetas in sweeps:
        print(f"\n=== Graph class: {graph_class} L={L} ===")
        per_zeta = {}
        for zeta in zetas:
            beta = 1.0 / zeta**2
            results_for_zeta = []
            for seed in range(n_seeds):
                print(f"[{graph_class} ζ={zeta} seed={seed}] β={beta:.3f}")
                res = find_F1_minimizer(graph_class, L, beta, c, seed)
                if res is None:
                    results_for_zeta.append(None)
                    continue
                analysis = analyze_minimizer(res, graph_class, L, zeta)
                analysis['seed'] = seed
                results_for_zeta.append(analysis)
                print(f"  F1={analysis['F1_found']} mode={analysis['best_mode_idx']} "
                      f"λ={analysis['best_eigval']:.3e} max_ov={analysis['best_overlap']:.3f}")
            per_zeta[zeta] = results_for_zeta

        # Find ζ_*
        zeta_star, mean_at = find_zeta_star(per_zeta, threshold=0.9)
        print(f"  ζ_*({graph_class}) ≈ {zeta_star} (first ζ with mean overlap > 0.9, mean = {mean_at})")

        all_results[graph_class] = {
            'L': L,
            'zetas_swept': zetas,
            'per_zeta': {str(z): per_zeta[z] for z in per_zeta},
            'zeta_star_threshold_0.9': zeta_star,
            'mean_overlap_at_star': mean_at,
        }

    elapsed = time.time() - t0
    print(f"\nTotal elapsed: {elapsed:.1f}s")

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'nq174_zeta_star.json')
    with open(out_path, 'w') as f:
        json.dump({
            'meta': {
                'c': c, 'n_seeds': n_seeds,
                'sweeps_description': '2D torus L=20 + 1D cycle L=40, mode-agnostic detection',
                'crossover_threshold': 0.9,
                'elapsed_s': elapsed,
                'mode_agnostic': True,
                'no_mode_index_hardcode': True,
                'description': 'ζ_*(graph-class) precise dependence (NQ-174)',
            },
            'results': all_results,
        }, f, indent=2, default=lambda o: float(o) if hasattr(o, 'item') else str(o))
    print(f"\nWrote {out_path}")


if __name__ == '__main__':
    main()
