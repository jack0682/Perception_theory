"""NQ-172: NQ-168 (04-25) vs NQ-170 (04-26) reproducibility test.

Both at L=20, ζ=1.0, β=1.0, c=0.5, pure E_bd, n_restarts=1.
Difference: seed function only.
  - NQ-168 uses: np.random.seed(seed * 37 + 7)
  - NQ-170 uses: np.random.seed(seed * 41 + 11)

NQ-168 reported (5 seeds): Mode 1 ≈ near-zero, max_overlap > 98% (Goldstone)
NQ-170 reported (3 seeds): Mode 1 ≈ numerical zero, max_overlap = 0.000 (NOT Goldstone)

This script runs BOTH setups for seeds {0, 1, 2}, dumps:
  - minimizer u as numpy array (.npy)
  - F (local maxima count)
  - Hessian lowest 6 eigenpairs
  - translation overlap for each mode
  - ASCII heatmap visualization (no matplotlib needed)
  - side-by-side comparison report

Run: cd CODE && python3 scripts/nq172_reproducibility_test.py
Outputs:
  - scripts/results/nq172_reproducibility.json
  - scripts/results/nq172_u_<setup>_seed<n>.npy (6 files)
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
                rows.append(idx); cols.append(nidx)
    return GraphState(sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n)))


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
    g = u.reshape(L, L)
    du_x = (np.roll(g, -1, axis=0) - g).flatten()
    du_y = (np.roll(g, -1, axis=1) - g).flatten()
    du_x /= (np.linalg.norm(du_x) + 1e-14)
    du_y /= (np.linalg.norm(du_y) + 1e-14)
    return du_x, du_y


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


def find_F1_minimizer(L, beta, c, seed, seed_func):
    """seed_func: function from int to int — seed transformation."""
    graph = build_torus_graph(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=15000,
    )
    xi_0 = np.sqrt(1.0 / beta)
    r0 = np.sqrt(c * L * L / np.pi)
    np.random.seed(seed_func(seed))
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
        return {
            'u': res.u, 'F': count_local_maxima_torus(res.u, L),
            'energy': float(res.energy), 'converged': bool(res.converged),
            'graph': graph, 'params': params, 'seed': seed,
            'init_cx': float(cx), 'init_cy': float(cy),
            'init_seed_value': int(seed_func(seed)),
        }
    except Exception as e:
        return {'error': str(e), 'seed': seed}


def ascii_heatmap(u, L, width=40):
    """ASCII heatmap of u reshape(L,L)."""
    g = u.reshape(L, L)
    chars = " .:-=+*#%@"
    lo, hi = float(g.min()), float(g.max())
    rng = max(hi - lo, 1e-12)
    lines = []
    lines.append(f"  range: [{lo:.4f}, {hi:.4f}], mean={float(g.mean()):.4f}, std={float(g.std()):.4f}")
    lines.append("  " + "-" * (L * 2 + 2))
    for i in range(L):
        row = "  |"
        for j in range(L):
            t = (g[i, j] - lo) / rng
            idx = min(len(chars) - 1, int(t * (len(chars) - 1)))
            row += chars[idx] * 2
        row += "|"
        lines.append(row)
    lines.append("  " + "-" * (L * 2 + 2))
    return "\n".join(lines)


def analyze_minimizer(result, L, label):
    u = result['u']
    graph = result['graph']
    params = result['params']
    du_x, du_y = translation_modes(u, L)
    eigvals, eigvecs = compute_hessian_lowest(u, graph, params, n_modes=6)
    overlaps = []
    for k in range(eigvecs.shape[1]):
        v = eigvecs[:, k]
        ov_x = float(abs(np.dot(v, du_x)))
        ov_y = float(abs(np.dot(v, du_y)))
        overlaps.append({
            'mode': k, 'eigenvalue': float(eigvals[k]),
            'overlap_x': ov_x, 'overlap_y': ov_y,
            'max_overlap': float(max(ov_x, ov_y)),
        })
    g = u.reshape(L, L)
    return {
        'label': label,
        'seed': result['seed'],
        'init_seed_value': result['init_seed_value'],
        'init_cx': result['init_cx'], 'init_cy': result['init_cy'],
        'F': result['F'], 'energy': result['energy'],
        'converged': result['converged'],
        'u_min': float(g.min()), 'u_max': float(g.max()),
        'u_mean': float(g.mean()), 'u_std': float(g.std()),
        'u_range': float(g.max() - g.min()),
        'mode_overlaps': overlaps,
        'heatmap': ascii_heatmap(u, L),
    }


def main():
    print("=" * 80)
    print("NQ-172: Reproducibility test of NQ-168 (04-25) vs NQ-170 (04-26)")
    print("=" * 80)
    print("Setup: L=20, ζ=1.0 (β=1.0), c=0.5, pure E_bd, n_restarts=1")
    print("Seeds: 0, 1, 2")
    print()

    L = 20; beta = 1.0; c = 0.5; n_seeds = 3
    out_dir = os.path.join(os.path.dirname(__file__), 'results')
    os.makedirs(out_dir, exist_ok=True)

    setups = {
        'NQ168_setup': lambda s: s * 37 + 7,
        'NQ170_setup': lambda s: s * 41 + 11,
    }

    report = {
        'L': L, 'beta': beta, 'c': c, 'zeta': 1.0,
        'protocol': 'L=20, β=1.0, ζ=1.0, c=0.5, pure E_bd',
        'setups': {},
    }

    for setup_name, seed_func in setups.items():
        print(f"\n{'=' * 80}")
        print(f"  SETUP: {setup_name}")
        print(f"{'=' * 80}")
        setup_results = []
        for seed in range(n_seeds):
            t0 = time.time()
            print(f"\n--- {setup_name} seed={seed} (init_seed = {seed_func(seed)}) ---")
            res = find_F1_minimizer(L, beta, c, seed, seed_func)
            if 'error' in res:
                print(f"  FAILED: {res['error']}")
                continue
            rec = analyze_minimizer(res, L, f"{setup_name}_seed{seed}")
            dt = time.time() - t0
            print(f"  cx={rec['init_cx']:.2f}, cy={rec['init_cy']:.2f}")
            print(f"  F = {rec['F']} (local maxima)")
            print(f"  Energy = {rec['energy']:.4f}, converged = {rec['converged']}")
            print(f"  u: min={rec['u_min']:.4f}, max={rec['u_max']:.4f}, "
                  f"mean={rec['u_mean']:.4f}, std={rec['u_std']:.4f}, range={rec['u_range']:.4f}")
            print(f"  Lowest 6 Hessian eigenpairs:")
            for ov in rec['mode_overlaps']:
                print(f"    mode {ov['mode']}: λ = {ov['eigenvalue']:+.4e},  "
                      f"overlap_x = {ov['overlap_x']:.4f},  "
                      f"overlap_y = {ov['overlap_y']:.4f},  "
                      f"max = {ov['max_overlap']:.4f}")
            print(f"  Heatmap of u (L×L = 20×20):")
            print(rec['heatmap'])
            print(f"  ({dt:.1f}s)")
            # save numpy
            npy_path = os.path.join(out_dir, f"nq172_u_{setup_name}_seed{seed}.npy")
            np.save(npy_path, res['u'])
            print(f"  → u saved to {npy_path}")
            setup_results.append(rec)
        report['setups'][setup_name] = setup_results

    # Side-by-side comparison
    print(f"\n{'=' * 80}")
    print("  SIDE-BY-SIDE COMPARISON")
    print(f"{'=' * 80}")
    print(f"\n  {'metric':<25} | {'NQ168_setup (s=0)':<25} | {'NQ170_setup (s=0)':<25}")
    print(f"  {'-'*25}-+-{'-'*25}-+-{'-'*25}")
    nq168_s0 = next((r for r in report['setups'].get('NQ168_setup', []) if r['seed'] == 0), None)
    nq170_s0 = next((r for r in report['setups'].get('NQ170_setup', []) if r['seed'] == 0), None)
    if nq168_s0 and nq170_s0:
        rows = [
            ('F (local maxima)', nq168_s0['F'], nq170_s0['F']),
            ('energy', f"{nq168_s0['energy']:.4f}", f"{nq170_s0['energy']:.4f}"),
            ('converged', nq168_s0['converged'], nq170_s0['converged']),
            ('u min', f"{nq168_s0['u_min']:.4f}", f"{nq170_s0['u_min']:.4f}"),
            ('u max', f"{nq168_s0['u_max']:.4f}", f"{nq170_s0['u_max']:.4f}"),
            ('u std', f"{nq168_s0['u_std']:.4f}", f"{nq170_s0['u_std']:.4f}"),
            ('u range', f"{nq168_s0['u_range']:.4f}", f"{nq170_s0['u_range']:.4f}"),
            ('init cx', f"{nq168_s0['init_cx']:.2f}", f"{nq170_s0['init_cx']:.2f}"),
            ('init cy', f"{nq168_s0['init_cy']:.2f}", f"{nq170_s0['init_cy']:.2f}"),
        ]
        for k in range(6):
            o168 = nq168_s0['mode_overlaps'][k]
            o170 = nq170_s0['mode_overlaps'][k]
            rows.append((f"mode {k} eigenvalue",
                        f"{o168['eigenvalue']:+.3e}", f"{o170['eigenvalue']:+.3e}"))
            rows.append((f"mode {k} max_overlap",
                        f"{o168['max_overlap']:.4f}", f"{o170['max_overlap']:.4f}"))
        for label, a, b in rows:
            print(f"  {str(label):<25} | {str(a):<25} | {str(b):<25}")
    print()

    # Diagnostic verdict
    print(f"\n{'=' * 80}")
    print("  DIAGNOSTIC VERDICT")
    print(f"{'=' * 80}")
    if nq168_s0 and nq170_s0:
        nq168_disk = nq168_s0['u_range'] > 0.5 and nq168_s0['F'] >= 1
        nq170_disk = nq170_s0['u_range'] > 0.5 and nq170_s0['F'] >= 1
        nq168_gold = nq168_s0['mode_overlaps'][1]['max_overlap'] > 0.5
        nq170_gold = nq170_s0['mode_overlaps'][1]['max_overlap'] > 0.5
        print(f"  NQ168_setup seed=0: disk-shaped={nq168_disk}, Mode-1 Goldstone={nq168_gold}")
        print(f"  NQ170_setup seed=0: disk-shaped={nq170_disk}, Mode-1 Goldstone={nq170_gold}")
        if nq168_disk and nq168_gold and (not nq170_disk or not nq170_gold):
            print(f"\n  → NQ168 reproducible. NQ170 protocol fails (different basin or collapsed minimizer).")
            print(f"    V5b super-lattice branch likely valid but IC-sensitive.")
        elif nq170_disk and not nq170_gold and nq168_disk and not nq168_gold:
            print(f"\n  → BOTH setups produce non-Goldstone result.")
            print(f"    V5b super-lattice branch FALSIFIED — NQ-168 (04-25) was likely an artifact.")
        elif nq168_disk and nq168_gold and nq170_disk and nq170_gold:
            print(f"\n  → BOTH setups reproduce Goldstone. NQ-170 prior result was an analysis artifact.")
        else:
            print(f"\n  → Mixed/ambiguous. Inspect heatmaps above for direct interpretation.")
        report['verdict'] = {
            'nq168_disk_shaped': nq168_disk, 'nq168_mode1_goldstone': nq168_gold,
            'nq170_disk_shaped': nq170_disk, 'nq170_mode1_goldstone': nq170_gold,
        }

    json_path = os.path.join(out_dir, 'nq172_reproducibility.json')
    with open(json_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\n=== JSON report saved: {json_path} ===")
    print(f"=== Numpy u files saved: {out_dir}/nq172_u_*.npy (6 files) ===")


if __name__ == "__main__":
    main()
