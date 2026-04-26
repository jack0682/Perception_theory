"""NQ-170c: V5b graph-class extension + nodal count (final V5b verification).

Combines two W5 closing tasks:

1. **Graph-class extension** — verify V5b sub/super-lattice prediction on
   multiple graph classes (not just 2D torus):
   - 2D torus L=20 (baseline, already verified in NQ-170b)
   - 2D free BC L=20 (translation broken by boundary — V5b should NOT predict Goldstone)
   - 1D cycle L=40 (1D translation invariant — V5b should predict 1-fold Goldstone)

2. **Nodal count explicit** — for each F=1 minimizer, compute Courant nodal
   count n_k of the lowest 6 Hessian eigenvectors. This validates the
   σ-framework signature σ(u*) = (𝓕; {(n_k, [ρ_k], λ_k)}).

V5b graph-class predictions:
  - 2D torus super-lattice (ζ ≥ 0.5): 2D Goldstone doublet, max overlap > 0.9
  - 1D cycle super-lattice (ζ ≥ 0.5): 1D Goldstone, max overlap > 0.9
  - 2D free BC (any ζ): NO Goldstone (translation broken), max overlap should be small

Run: cd CODE && python3 scripts/nq170c_v5b_extension.py
Output: scripts/results/nq170c_v5b_extension.json
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import grad_bd


# === Graph constructors ===

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


def build_free_bc_2d(L):
    n = L * L
    rows, cols = [], []
    for i in range(L):
        for j in range(L):
            idx = i * L + j
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < L and 0 <= nj < L:
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
    elif graph_class == '2D_free_BC':
        g = u.reshape(L, L)
        F = 0
        for i in range(L):
            for j in range(L):
                v = g[i, j]
                neighbors = []
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < L and 0 <= nj < L:
                        neighbors.append(g[ni, nj])
                if all(nv < v for nv in neighbors):
                    F += 1
        return F
    elif graph_class == '1D_cycle':
        F = 0
        for i in range(L):
            v = u[i]
            if u[(i - 1) % L] < v and u[(i + 1) % L] < v:
                F += 1
        return F


# === Translation modes (graph-class specific) ===

def translation_modes(u, graph_class, L):
    if graph_class == '2D_torus':
        g = u.reshape(L, L)
        du_x = (np.roll(g, -1, axis=0) - g).flatten()
        du_y = (np.roll(g, -1, axis=1) - g).flatten()
        modes = [('x', du_x), ('y', du_y)]
    elif graph_class == '2D_free_BC':
        g = u.reshape(L, L)
        du_x = np.zeros((L, L))
        du_x[:-1, :] = g[1:, :] - g[:-1, :]
        du_y = np.zeros((L, L))
        du_y[:, :-1] = g[:, 1:] - g[:, :-1]
        modes = [('x', du_x.flatten()), ('y', du_y.flatten())]
    elif graph_class == '1D_cycle':
        du_x = np.roll(u, -1) - u
        modes = [('x', du_x)]
    out = []
    for name, m in modes:
        norm = np.linalg.norm(m)
        out.append((name, m / norm if norm > 1e-14 else m))
    return out


# === Hessian + Nodal Count ===

def compute_hessian_lowest(u_star, graph, params, n_modes=6, eps=1e-4):
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


def compute_nodal_count(eigvec, graph):
    """Courant nodal count: # connected components of {phi > 0} + {phi < 0}."""
    n = len(eigvec)
    eps = 1e-6 * float(np.max(np.abs(eigvec)) + 1e-14)
    W = graph.W if hasattr(graph, 'W') else graph
    if hasattr(W, 'tocsr'):
        Wc = W.tocsr()
    else:
        Wc = W
    indptr = Wc.indptr
    indices = Wc.indices

    def neighbors(i):
        return indices[indptr[i]:indptr[i + 1]]

    def count_components(mask):
        visited = np.zeros(n, dtype=bool)
        n_comp = 0
        for i in range(n):
            if mask[i] and not visited[i]:
                stack = [i]
                while stack:
                    j = stack.pop()
                    if visited[j]:
                        continue
                    visited[j] = True
                    for k in neighbors(j):
                        if mask[k] and not visited[k]:
                            stack.append(k)
                n_comp += 1
        return n_comp

    pos_mask = eigvec > eps
    neg_mask = eigvec < -eps
    return count_components(pos_mask) + count_components(neg_mask), \
           count_components(pos_mask), count_components(neg_mask)


# === Find F=1 minimizer (multi-IC) ===

def find_F1_minimizer(graph_class, L, beta, c, seed):
    if graph_class == '2D_torus':
        graph, n = build_torus_2d(L)
    elif graph_class == '2D_free_BC':
        graph, n = build_free_bc_2d(L)
    elif graph_class == '1D_cycle':
        graph, n = build_cycle_1d(L)

    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=15000,
    )
    xi_0 = np.sqrt(1.0 / beta)

    if graph_class.startswith('2D'):
        r0 = np.sqrt(c * L * L / np.pi)
        ic_widths = [max(xi_0, 0.2), xi_0 * 0.5, xi_0 * 2.0]
    else:  # 1D_cycle
        r0 = c * L / 2.0  # disk = arc of length c·L
        ic_widths = [max(xi_0, 0.2), xi_0 * 0.5, xi_0 * 2.0]

    attempts = []
    for ic_id in range(3):
        np.random.seed(seed * 53 + 13 + ic_id * 1000)
        if graph_class.startswith('2D'):
            cx = np.random.uniform(0.5, L - 0.5)
            cy = np.random.uniform(0.5, L - 0.5)
            i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
            if graph_class == '2D_torus':
                dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
                dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
            else:  # free BC
                dx = np.abs(i_idx - cx)
                dy = np.abs(j_idx - cy)
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
    best['attempts_F'] = [a['F'] for a in attempts]
    return best


# === Analyze with mode-agnostic Goldstone + nodal count ===

def analyze(result, graph_class, L, zeta):
    u = result['u']
    graph = result['graph']
    params = result['params']
    n = result['n']

    trans_modes = translation_modes(u, graph_class, L)
    tangent = np.ones(n) / np.sqrt(n)

    eigvals, eigvecs = compute_hessian_lowest(u, graph, params, n_modes=6)

    mode_data = []
    for k in range(eigvecs.shape[1]):
        v = eigvecs[:, k]
        overlaps = {f'overlap_{name}': float(abs(np.dot(v, m))) for name, m in trans_modes}
        max_trans_overlap = max(overlaps.values())
        ov_t = float(abs(np.dot(v, tangent)))
        # Nodal count
        n_total, n_pos, n_neg = compute_nodal_count(v, graph)
        mode_data.append({
            'mode': k,
            'eigenvalue': float(eigvals[k]),
            **overlaps,
            'overlap_tangent': ov_t,
            'max_translation_overlap': max_trans_overlap,
            'is_tangent': ov_t > 0.1,
            'nodal_count': int(n_total),
            'nodal_pos': int(n_pos),
            'nodal_neg': int(n_neg),
        })

    non_tangent = [m for m in mode_data if not m['is_tangent']]
    if non_tangent:
        goldstone = max(non_tangent, key=lambda m: m['max_translation_overlap'])
    else:
        goldstone = max(mode_data, key=lambda m: m['max_translation_overlap'])

    return {
        'graph_class': graph_class,
        'L': L,
        'zeta': zeta,
        'seed': result.get('seed'),
        'F': result['F'],
        'F1_found': result['F1_found'],
        'attempts_F': result['attempts_F'],
        'energy': result['energy'],
        'mode_data': mode_data,
        'goldstone_mode_index': goldstone['mode'],
        'goldstone_eigenvalue': goldstone['eigenvalue'],
        'goldstone_max_overlap': goldstone['max_translation_overlap'],
        'goldstone_nodal_count': goldstone['nodal_count'],
        # σ-signature: lowest 6 modes (n_k, λ_k)
        'sigma_signature': [(m['nodal_count'], m['eigenvalue']) for m in mode_data],
    }


def main():
    print("=" * 75)
    print("NQ-170c: V5b graph-class extension + nodal count (W5 closing)")
    print("=" * 75)
    print()

    c = 0.5
    N_seeds = 3
    configs = [
        # (graph_class, L, zeta_list, label)
        ('2D_torus', 20, [0.2, 0.5, 1.0], 'baseline (NQ-170b重)'),
        ('2D_free_BC', 20, [0.2, 0.5, 1.0], 'translation broken — V5b N/A'),
        ('1D_cycle', 40, [0.2, 0.5, 1.0], '1D translation — V5b 1D Goldstone'),
    ]

    report = {
        'protocol': 'V5b graph-class extension + Courant nodal count',
        'c': c,
        'N_seeds': N_seeds,
        'configs': [{'graph_class': cfg[0], 'L': cfg[1], 'zetas': cfg[2], 'label': cfg[3]} for cfg in configs],
        'results': [],
    }

    for graph_class, L, zetas, label in configs:
        print(f"\n{'#' * 75}")
        print(f"# Graph class: {graph_class}, L={L} ({label})")
        print(f"{'#' * 75}")
        for zeta in zetas:
            beta = 1.0 / (zeta ** 2)
            print(f"\n--- ζ = {zeta} (β = {beta:.3f}) ---")
            for seed in range(N_seeds):
                t0 = time.time()
                res = find_F1_minimizer(graph_class, L, beta, c, seed)
                if res is None:
                    print(f"  seed={seed}: ALL ATTEMPTS FAILED")
                    continue
                res['seed'] = seed
                rec = analyze(res, graph_class, L, zeta)
                dt = time.time() - t0
                f1 = "✓" if rec['F1_found'] else "✗"
                gold_n = rec['goldstone_nodal_count']
                print(f"  seed={seed}: F={rec['F']} {f1} (attempts={rec['attempts_F']}), "
                      f"Goldstone@mode{rec['goldstone_mode_index']} "
                      f"λ={rec['goldstone_eigenvalue']:+.3e}, "
                      f"max_overlap={rec['goldstone_max_overlap']:.4f}, "
                      f"nodal={gold_n} ({dt:.1f}s)")
                report['results'].append(rec)

    # Aggregate analysis
    print(f"\n{'=' * 75}")
    print("  AGGREGATE BY (graph_class, ζ) — F=1 minimizers only")
    print(f"{'=' * 75}\n")

    print(f"  {'graph_class':<14} | {'L':>3} | {'ζ':>4} | {'n':>3} | "
          f"{'mean overlap':>12} | {'V5b prediction':<25}")
    print("  " + "-" * 14 + "-+-" + "-" * 3 + "-+-" + "-" * 4 + "-+-" + "-" * 3
          + "-+-" + "-" * 12 + "-+-" + "-" * 25)
    aggregate = {}
    for graph_class, L, zetas, label in configs:
        for zeta in zetas:
            f1_results = [r for r in report['results']
                          if r['graph_class'] == graph_class and r['zeta'] == zeta and r['F1_found']]
            if not f1_results:
                continue
            overlaps = [r['goldstone_max_overlap'] for r in f1_results]
            mean_ov = float(np.mean(overlaps))

            if graph_class == '2D_torus':
                pred = "Goldstone iff ζ≥0.5" if zeta >= 0.5 else "no Goldstone"
                expected = "> 0.9" if zeta >= 0.5 else "< 0.5"
                pass_ = (mean_ov > 0.9) if zeta >= 0.5 else (mean_ov < 0.5)
            elif graph_class == '2D_free_BC':
                pred = "no Goldstone (boundary broken)"
                expected = "< 0.5"
                pass_ = mean_ov < 0.5
            elif graph_class == '1D_cycle':
                pred = "1D Goldstone iff ζ≥0.5" if zeta >= 0.5 else "no Goldstone"
                expected = "> 0.9" if zeta >= 0.5 else "< 0.5"
                pass_ = (mean_ov > 0.9) if zeta >= 0.5 else (mean_ov < 0.5)

            verdict = "PASS ✓" if pass_ else "FAIL ✗"
            print(f"  {graph_class:<14} | {L:>3} | {zeta:>4} | {len(f1_results):>3} | "
                  f"{mean_ov:>12.4f} | {pred} ({expected}) {verdict}")
            aggregate[f"{graph_class}_zeta{zeta}"] = {
                'graph_class': graph_class, 'L': L, 'zeta': zeta,
                'n': len(f1_results), 'mean_overlap': mean_ov,
                'prediction': pred, 'expected_range': expected, 'pass': bool(pass_),
            }
    report['aggregate'] = aggregate

    # σ-signature samples — print one example per (graph, ζ)
    print(f"\n{'=' * 75}")
    print("  σ-SIGNATURE SAMPLES (Courant nodal counts, lowest 6 modes)")
    print(f"{'=' * 75}\n")
    seen = set()
    for r in report['results']:
        key = (r['graph_class'], r['zeta'])
        if key in seen or not r['F1_found']:
            continue
        seen.add(key)
        sigs = [f"(n={s[0]}, λ={s[1]:+.3e})" for s in r['sigma_signature']]
        print(f"  {r['graph_class']:<14} ζ={r['zeta']:<4} seed={r['seed']}: F={r['F']}")
        for k, sig in enumerate(sigs):
            star = " ← Goldstone" if k == r['goldstone_mode_index'] else ""
            print(f"    mode {k}: {sig}{star}")

    out_path = os.path.join(os.path.dirname(__file__), 'results', 'nq170c_v5b_extension.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\n=== RESULTS SAVED: {out_path} ===")


if __name__ == "__main__":
    main()
