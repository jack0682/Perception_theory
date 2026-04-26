"""NQ-170b: ζ-scan with **mode-agnostic** Goldstone detection (fix of NQ-170).

NQ-170 (04-26 morning) had a method bug: it hardcoded "Mode 1" as the lowest
non-tangent mode, but NQ-172 (04-26 afternoon) revealed that when the tangent
mode (numerical ~0) and the near-zero Goldstone (~1e-7) are both at numerical
zero scale, the eigenvalue sorting can swap them — i.e., Goldstone may be at
mode 0 instead of mode 1. NQ-170's hardcoded mode_overlaps[1] then measures
the tangent (overlap=0) and falsely reports "no Goldstone".

Fix in this script:
  - Compute max(overlap_x, overlap_y) for ALL modes (k=0..n_modes-1)
  - Identify "tangent mode" via overlap with normalized 1-vector (constant)
  - "Goldstone candidate" = mode with maximum translation overlap
    among non-tangent modes
  - Report this mode-agnostic best Goldstone overlap

Same protocol as NQ-170:
  ζ ∈ {0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0} × N=3 seeds × L=20 torus, pure E_bd.

Run: cd CODE && python3 scripts/nq170b_zeta_scan_fixed.py
Output: scripts/results/nq170b_zeta_scan_fixed.json
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


def find_F1_minimizer(L, beta, c, seed, lambda_cl=0.0, lambda_sep=0.0):
    """Multi-attempt F=1 minimizer search (3 IC modes)."""
    graph = build_torus_graph(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=lambda_cl, w_sep=lambda_sep, w_bd=1.0,
        n_restarts=1, max_iter=15000,
    )
    xi_0 = np.sqrt(1.0 / beta)
    r0 = np.sqrt(c * L * L / np.pi)
    n = L * L

    # Try multiple ICs (random tanh, narrow tanh, eigmode-perturbed)
    attempts = []
    for ic_mode_id in range(3):
        np.random.seed(seed * 41 + 11 + ic_mode_id * 1000)
        cx = np.random.uniform(0.5, L - 0.5)
        cy = np.random.uniform(0.5, L - 0.5)
        i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
        dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
        dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
        r = np.sqrt(dx**2 + dy**2).flatten()
        if ic_mode_id == 0:
            ic_width = max(xi_0, 0.2)  # standard
        elif ic_mode_id == 1:
            ic_width = xi_0 * 0.5      # narrow (high-β regime)
        else:
            ic_width = xi_0 * 2.0      # wide
        u_init = 0.5 * (1.0 - np.tanh((r - r0) / ic_width))
        u_init = np.clip(u_init + np.random.normal(0, 0.02, size=n), 0.01, 0.99)
        try:
            res = find_formation(graph, params, normalize=False, verbose=False, u_init=u_init)
            if not res.converged:
                continue
            F = count_local_maxima_torus(res.u, L)
            attempts.append({
                'F': F, 'energy': float(res.energy), 'u': res.u,
                'ic_mode_id': ic_mode_id, 'cx': float(cx), 'cy': float(cy),
            })
        except Exception:
            continue

    if not attempts:
        return None
    # Pick F=1 with lowest energy if any; else pick lowest-F overall
    f1 = [a for a in attempts if a['F'] == 1]
    if f1:
        best = min(f1, key=lambda a: a['energy'])
        best['F1_found'] = True
    else:
        best = min(attempts, key=lambda a: (a['F'], a['energy']))
        best['F1_found'] = False
    best['graph'] = graph
    best['params'] = params
    best['seed'] = seed
    best['n_attempts'] = len(attempts)
    best['attempts_F'] = [a['F'] for a in attempts]
    return best


def analyze_mode_agnostic(result, L, zeta):
    """Mode-agnostic Goldstone detection.

    For each of n_modes (=6) lowest Hessian eigenmodes:
      - eigenvalue
      - overlap with δu_x, δu_y (translation directions)
      - overlap with normalized constant vector (tangent indicator)
      - max_overlap = max(overlap_x, overlap_y)

    Goldstone mode = mode with maximum translation overlap among modes
    where tangent_overlap is small (< 0.1).
    """
    u = result['u']
    graph = result['graph']
    params = result['params']
    n = graph.n

    du_x, du_y = translation_modes(u, L)
    tangent = np.ones(n) / np.sqrt(n)  # normalized constant

    try:
        eigvals, eigvecs = compute_hessian_lowest(u, graph, params, n_modes=6)
    except Exception as e:
        return {'error': str(e)}

    mode_data = []
    for k in range(eigvecs.shape[1]):
        v = eigvecs[:, k]
        ov_x = float(abs(np.dot(v, du_x)))
        ov_y = float(abs(np.dot(v, du_y)))
        ov_t = float(abs(np.dot(v, tangent)))
        mode_data.append({
            'mode': k,
            'eigenvalue': float(eigvals[k]),
            'overlap_x': ov_x,
            'overlap_y': ov_y,
            'overlap_tangent': ov_t,
            'max_translation_overlap': float(max(ov_x, ov_y)),
            'is_tangent': ov_t > 0.1,
        })

    # Find Goldstone mode: max translation overlap among non-tangent modes
    non_tangent = [m for m in mode_data if not m['is_tangent']]
    if non_tangent:
        goldstone = max(non_tangent, key=lambda m: m['max_translation_overlap'])
    else:
        goldstone = max(mode_data, key=lambda m: m['max_translation_overlap'])

    return {
        'zeta': zeta,
        'L': L,
        'seed': result['seed'],
        'F': result['F'],
        'F1_found': result.get('F1_found', False),
        'n_attempts': result.get('n_attempts', 1),
        'attempts_F': result.get('attempts_F', []),
        'energy': result['energy'],
        'u_min': float(u.min()),
        'u_max': float(u.max()),
        'u_std': float(u.std()),
        'mode_data': mode_data,
        'goldstone_mode_index': goldstone['mode'],
        'goldstone_eigenvalue': goldstone['eigenvalue'],
        'goldstone_max_overlap': goldstone['max_translation_overlap'],
        'goldstone_overlap_x': goldstone['overlap_x'],
        'goldstone_overlap_y': goldstone['overlap_y'],
    }


def main():
    print("=" * 70)
    print("NQ-170b: ζ-scan with mode-agnostic Goldstone detection (fix)")
    print("=" * 70)
    print("Fix: 'Goldstone mode' = max translation overlap across modes 0..5,")
    print("      excluding tangent (overlap with constant vector > 0.1).")
    print("Multi-IC: 3 IC widths per seed (standard, narrow, wide) — best F=1.")
    print()

    L = 20; c = 0.5; N_seeds = 3
    zetas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0]

    report = {
        'L': L, 'c': c, 'N_seeds': N_seeds, 'zetas': zetas,
        'protocol': 'mode-agnostic Goldstone detection; 3 IC widths per seed',
        'results': [],
    }

    for zeta in zetas:
        beta = 1.0 / (zeta ** 2)
        print(f"\n--- ζ = {zeta} (β = {beta:.3f}) ---")
        for seed in range(N_seeds):
            t0 = time.time()
            res = find_F1_minimizer(L, beta, c, seed)
            if res is None:
                print(f"  seed={seed}: ALL ATTEMPTS FAILED")
                continue
            rec = analyze_mode_agnostic(res, L, zeta)
            if 'error' in rec:
                print(f"  seed={seed}: analysis error ({rec['error']})")
                continue
            dt = time.time() - t0
            f1_marker = "✓" if rec['F1_found'] else "✗"
            print(f"  seed={seed}: F={rec['F']} {f1_marker} (attempts F={rec['attempts_F']}), "
                  f"Goldstone@mode{rec['goldstone_mode_index']} "
                  f"λ={rec['goldstone_eigenvalue']:+.3e}, "
                  f"max_overlap={rec['goldstone_max_overlap']:.4f} "
                  f"(ov_x={rec['goldstone_overlap_x']:.3f}, ov_y={rec['goldstone_overlap_y']:.3f}) "
                  f"({dt:.1f}s)")
            report['results'].append(rec)

    # Aggregate by ζ (only F=1 minimizers)
    print("\n=== ζ vs Goldstone max overlap (F=1 minimizers only) ===")
    by_zeta_f1 = {}
    by_zeta_all = {}
    for r in report['results']:
        z = r['zeta']
        by_zeta_all.setdefault(z, []).append(r['goldstone_max_overlap'])
        if r['F1_found']:
            by_zeta_f1.setdefault(z, []).append(r['goldstone_max_overlap'])

    aggregate = {}
    for z in sorted(by_zeta_all.keys()):
        all_vals = by_zeta_all[z]
        f1_vals = by_zeta_f1.get(z, [])
        agg = {
            'n_total': len(all_vals),
            'n_F1': len(f1_vals),
            'mean_overlap_all': float(np.mean(all_vals)),
            'mean_overlap_F1': float(np.mean(f1_vals)) if f1_vals else None,
        }
        aggregate[z] = agg
        f1_str = f"F1 mean={np.mean(f1_vals):.3f} (n={len(f1_vals)})" if f1_vals else "no F=1"
        print(f"  ζ={z}: all mean={np.mean(all_vals):.3f} (n={len(all_vals)}), {f1_str}")
    report['aggregate_by_zeta'] = aggregate

    # Crossover identification (using F=1 means where available)
    print("\n=== Crossover ζ_* identification (F=1 only) ===")
    sorted_z = sorted([z for z in aggregate if aggregate[z]['mean_overlap_F1'] is not None])
    z_below = [z for z in sorted_z if aggregate[z]['mean_overlap_F1'] < 0.5]
    z_above = [z for z in sorted_z if aggregate[z]['mean_overlap_F1'] >= 0.5]
    if z_below and z_above:
        z_low = max(z_below)
        z_high = min(z_above)
        ov_low = aggregate[z_low]['mean_overlap_F1']
        ov_high = aggregate[z_high]['mean_overlap_F1']
        if ov_high > ov_low:
            zeta_star = z_low + (0.5 - ov_low) * (z_high - z_low) / (ov_high - ov_low)
            print(f"  ζ_* (overlap=0.5 crossing): ≈ {zeta_star:.3f}")
            print(f"  bracketed by: ζ={z_low} (mean={ov_low:.3f}) and ζ={z_high} (mean={ov_high:.3f})")
            report['crossover_zeta_star'] = float(zeta_star)
            report['crossover_bracket'] = [float(z_low), float(z_high)]
    elif sorted_z and all(aggregate[z]['mean_overlap_F1'] > 0.9 for z in sorted_z):
        print(f"  All ζ values show mean overlap > 0.9 (Goldstone present everywhere with F=1)")
        report['crossover_zeta_star'] = None
    elif sorted_z and all(aggregate[z]['mean_overlap_F1'] < 0.5 for z in sorted_z):
        print(f"  All ζ values show mean overlap < 0.5 (no Goldstone)")
        report['crossover_zeta_star'] = None
    else:
        print(f"  Insufficient F=1 data for crossover bracketing")

    # V5b prediction check
    print("\n=== V5b prediction check (using F=1 minimizers) ===")
    sub_check = [aggregate[z]['mean_overlap_F1'] for z in sorted_z if z <= 0.2 and aggregate[z]['mean_overlap_F1'] is not None]
    print(f"  Sub-lattice (ζ ≤ 0.2): expect mean_overlap < 0.5")
    print(f"    Observed: {[f'{v:.3f}' for v in sub_check]} → "
          f"{'PASS' if all(v < 0.5 for v in sub_check) else 'FAIL' if sub_check else 'N/A (no F=1)'}")
    super_check = [aggregate[z]['mean_overlap_F1'] for z in sorted_z if z >= 0.5 and aggregate[z]['mean_overlap_F1'] is not None]
    print(f"  Super-lattice (ζ ≥ 0.5): expect mean_overlap > 0.9")
    print(f"    Observed: {[f'{v:.3f}' for v in super_check]} → "
          f"{'PASS' if all(v > 0.9 for v in super_check) else 'FAIL' if super_check else 'N/A (no F=1)'}")
    report['v5b_sub_lattice_pass'] = bool(all(v < 0.5 for v in sub_check)) if sub_check else None
    report['v5b_super_lattice_pass'] = bool(all(v > 0.9 for v in super_check)) if super_check else None

    out_path = os.path.join(os.path.dirname(__file__), 'results', 'nq170b_zeta_scan_fixed.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\n=== RESULTS SAVED: {out_path} ===")


if __name__ == "__main__":
    main()
