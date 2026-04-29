"""NQ-198f: V5b-T' torus mass-dep test.

Day 3 EOD spawn (`THEORY/logs/daily/2026-04-29/07_*` §7 + `10_*` §3.1).

CRITICAL question: Does V5b-T' (corner-saturated cluster on translation-invariant
graph = torus) show the same μ ∝ |∂S|/n scaling as V5b-F (free-BC, NQ-198a)?

  - If μ ∝ |∂S|/n on torus too → V5b family **unified scaling** (finite-size
    collective effect across BC types).
  - If μ ≈ const on torus → `05_*` §4 derivation correct for V5b-T'; V5b-T' and
    V5b-F have **different scalings** (continuum-Goldstone vs finite-size).

Setup mirrors NQ-198a but with periodic BC graph (T²_L torus):
  - β=4, ξ_0=0.5 (R3b corner-saturated regime).
  - 4 mass values m ∈ {40, 80, 120, 160}; L matched to keep c=0.10.
    But torus IS translation-invariant; corner-saturation = cluster of u=1
    sites of mass m, anchored anywhere.
  - For consistency with NQ-198a, also do fixed-L sweep:
      Sweep (a): L=20, vary c (m): m ∈ {40, 80, 120, 160}, c ∈ {0.10, 0.20, 0.30, 0.40}
      Sweep (b): c≈0.10, vary L: m=40 L=20, m=80 L=28, m=160 L=40

Output: scripts/results/nq198f_V5bTprime_torus.json

Run: cd CODE && python3 scripts/nq198f_V5bTprime_torus.py
Expected runtime: ~3-5 min (similar to NQ-198a).
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import grad_bd


def build_torus_2d(L):
    """2D torus: each site has 4 neighbors with periodic BC."""
    n = L * L
    rows, cols = [], []
    for i in range(L):
        for j in range(L):
            idx = i * L + j
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni = (i + di) % L
                nj = (j + dj) % L
                rows.append(idx); cols.append(ni * L + nj)
    return GraphState(sp.csr_matrix(
        (np.ones(len(rows)), (rows, cols)), shape=(n, n))), n


def count_local_maxima_torus(u, L):
    g = u.reshape(L, L)
    F = 0
    for i in range(L):
        for j in range(L):
            v = g[i, j]
            ok = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni = (i + di) % L
                nj = (j + dj) % L
                if g[ni, nj] >= v: ok = False; break
            if ok: F += 1
    return F


def translation_modes_torus(u, L):
    """Periodic BC translation modes (forward differences with wrap)."""
    g = u.reshape(L, L)
    du_x = np.zeros((L, L))
    for i in range(L):
        ip = (i + 1) % L
        du_x[i, :] = g[ip, :] - g[i, :]
    du_y = np.zeros((L, L))
    for j in range(L):
        jp = (j + 1) % L
        du_y[:, j] = g[:, jp] - g[:, j]
    out = []
    for name, m in [('x', du_x.flatten()), ('y', du_y.flatten())]:
        norm = np.linalg.norm(m)
        out.append((name, m / norm if norm > 1e-14 else m))
    return out


def compute_hessian_lowest(u_star, graph, params, n_modes=8, eps=1e-4):
    n = u_star.shape[0]
    g0 = grad_bd(u_star, graph, params)
    H = np.zeros((n, n))
    for i in range(n):
        u_p = u_star.copy(); u_p[i] += eps
        g_p = grad_bd(u_p, graph, params)
        H[:, i] = (g_p - g0) / eps
    H = (H + H.T) / 2.0
    one = np.ones(n)
    P = np.eye(n) - np.outer(one, one) / n
    H_proj = P @ H @ P
    eigvals, eigvecs = np.linalg.eigh(H_proj)
    idx = np.argsort(eigvals)
    return eigvals[idx[:n_modes]], eigvecs[:, idx[:n_modes]]


def estimate_cluster_perimeter_torus(u, L, sat_threshold=0.9):
    """Count torus edges (periodic) where u jumps across sat_threshold."""
    g = u.reshape(L, L)
    sat = (g >= sat_threshold).astype(int)
    perim = 0
    for i in range(L):
        for j in range(L):
            if sat[i, j] == 1:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni = (i + di) % L
                    nj = (j + dj) % L
                    if sat[ni, nj] == 0: perim += 1
    return perim


def find_corner_sat_minimizer_torus(L, beta, c, seed, max_iter=15000):
    graph, n = build_torus_2d(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=max_iter,
    )
    side = int(np.ceil(np.sqrt(c * L * L)))

    # Multi-IC: square cluster anchored at different positions on torus.
    # On torus, all positions are equivalent (translation-invariant), but
    # cluster orientation/size variations help find the saturated minimum.
    ic_configs = [
        ('square_origin', (0, 0)),
        ('square_off_3_3', (3 % L, 3 % L)),
        ('square_off_5_2', (5 % L, 2 % L)),
        ('square_centered', ((L - side) // 2, (L - side) // 2)),
        ('square_diag', ((L // 4) % L, (L // 4) % L)),
        ('square_random_seed', None),  # Random position, seed-controlled
    ]

    attempts = []
    for ic_id, (label, anchor) in enumerate(ic_configs):
        np.random.seed(seed * 53 + 13 + ic_id * 1000)
        if anchor is None:
            ax = np.random.randint(0, L)
            ay = np.random.randint(0, L)
        else:
            ax, ay = anchor
        u_init = np.full(n, 0.01)
        for ii in range(side):
            for jj in range(side):
                idx_i = (ax + ii) % L
                idx_j = (ay + jj) % L
                u_init[idx_i * L + idx_j] = 0.99
        # Normalize to volume m
        cur_sum = np.sum(u_init)
        target = c * n
        adj = (target - cur_sum) / n
        u_init = np.clip(u_init + adj, 0.01, 0.99)
        u_init = np.clip(u_init + np.random.normal(0, 0.01, size=n), 0.01, 0.99)

        try:
            res = find_formation(graph, params, normalize=False, verbose=False,
                                 u_init=u_init, allow_outside_spinodal=True)
            if not res.converged and len(res.energy_history) > 10:
                tail = res.energy_history[-max(10, len(res.energy_history) // 10):]
                rel_change = abs(tail[-1] - tail[0]) / max(abs(tail[0]), 1e-12)
                if rel_change < 1e-3: res.converged = True
            if not res.converged: continue
            F = count_local_maxima_torus(res.u, L)
            u_max = float(np.max(res.u))
            attempts.append({'F': F, 'energy': float(res.energy), 'u': res.u,
                             'ic_id': ic_id, 'u_max': u_max, 'corner_sat': u_max >= 0.95})
        except Exception as e:
            print(f"  attempt seed={seed} ic={ic_id}: {type(e).__name__}: {e}", flush=True)
            continue

    if not attempts: return None
    cs = [a for a in attempts if a['corner_sat']]
    if cs:
        best = min(cs, key=lambda a: a['energy'])
        best['F1_found'] = (best['F'] == 1)
    else:
        best = min(attempts, key=lambda a: a['energy'])
        best['F1_found'] = False
    best['graph'] = graph; best['params'] = params; best['n'] = n
    return best


def analyze_minimizer_torus(result, L, beta):
    u = result['u']; graph = result['graph']; params = result['params']; n = result['n']
    trans_modes = translation_modes_torus(u, L)
    tangent = np.ones(n) / np.sqrt(n)

    eigvals, eigvecs = compute_hessian_lowest(u, graph, params, n_modes=8)

    best_idx = -1; best_overlap = -1.0
    mode_records = []
    for k in range(eigvecs.shape[1]):
        v = eigvecs[:, k]
        ov_t = float(abs(np.dot(v, tangent)))
        if ov_t > 0.5:
            mode_records.append({'mode_idx': k, 'eigval': float(eigvals[k]),
                                 'ov_tangent': ov_t, 'is_tangent': True}); continue
        overlaps = {name: float(abs(np.dot(v, m))) for name, m in trans_modes}
        max_ov = max(overlaps.values())
        mode_records.append({'mode_idx': k, 'eigval': float(eigvals[k]),
                             'ov_tangent': ov_t, 'overlap_x': overlaps['x'],
                             'overlap_y': overlaps['y'], 'max_overlap': max_ov,
                             'is_tangent': False})
        if max_ov > best_overlap:
            best_overlap = max_ov; best_idx = k

    perim = estimate_cluster_perimeter_torus(u, L)
    return {
        'mu_Goldstone': float(eigvals[best_idx]) if best_idx >= 0 else None,
        'best_overlap': best_overlap if best_idx >= 0 else 0.0,
        'best_idx': best_idx,
        'cluster_perimeter': perim,
        'mode_records': mode_records,
        'F': count_local_maxima_torus(u, L),
        'F1_found': result['F1_found'],
        'energy': result['energy'],
        'u_max': float(np.max(u)),
        'u_min': float(np.min(u)),
        'fraction_saturated': float(np.mean(u >= 0.9)),
    }


def main():
    setups = [
        # Sweep (a): fixed L=20, varied c
        (40, 20, 'a_L20_c10', 0.10),
        (80, 20, 'a_L20_c20', 0.20),
        (120, 20, 'a_L20_c30', 0.30),
        (160, 20, 'a_L20_c40', 0.40),
        # Sweep (b): fixed c≈0.10, varied L
        (80, 28, 'b_c10_L28', 80/784.0),
        (160, 40, 'b_c10_L40', 160/1600.0),
    ]
    beta = 4.0
    seeds = list(range(3))

    results = {
        'meta': {
            'beta': beta, 'xi_0': float(np.sqrt(1.0 / beta)), 'zeta': 0.5,
            'graph_type': '2D_torus_periodic_BC',
            'setups': [{'m': m, 'L': L, 'sweep_id': sid, 'c': c} for m, L, sid, c in setups],
            'seeds_per_setup': len(seeds),
            'total_attempts': len(setups) * len(seeds),
            'predictions': {
                'NQ-198a_V5bF_empirical': 'mu = 13.2 * |dS|/n; if torus same -> V5b family unified',
                '05_section4_derivation': 'mu ~ 2 alpha = 2 (constant); if torus matches -> regime separation',
            },
            'started_at': time.strftime('%Y-%m-%dT%H:%M:%S'),
        },
        'per_setup': [],
    }

    print("NQ-198f V5b-T' torus mass-dep test", flush=True)
    print("=" * 60, flush=True)
    print(f"beta={beta}, xi_0=0.5, zeta=0.5; 2D torus periodic BC", flush=True)
    print(f"{len(setups)} setups; {len(seeds)} seeds each = {len(setups)*len(seeds)} attempts", flush=True)
    for m, L, sid, c in setups:
        print(f"  m={m:3d}, L={L:2d}, sweep={sid}, c={c:.4f}", flush=True)
    print(flush=True)

    t_global = time.time()
    for setup_idx, (m, L, sid, c) in enumerate(setups):
        n = L * L
        max_iter = max(15000, 3 * n)
        per_setup = {'m': m, 'L': L, 'sweep_id': sid, 'c': c, 'attempts': []}
        print(f"[{setup_idx+1}/{len(setups)}] m={m}, L={L}, sweep={sid}, c={c:.4f}:", flush=True)

        for seed in seeds:
            t_s = time.time()
            try:
                res = find_corner_sat_minimizer_torus(L, beta, c, seed, max_iter=max_iter)
                if res is None:
                    print(f"  seed={seed}: no minimizer", flush=True)
                    per_setup['attempts'].append({'seed': seed, 'status': 'no_minimizer'})
                    continue
                t_opt = time.time() - t_s
                t_h = time.time()
                analysis = analyze_minimizer_torus(res, L, beta)
                t_hess = time.time() - t_h
                analysis['seed'] = seed
                analysis['time_optimizer_s'] = round(t_opt, 1)
                analysis['time_hessian_s'] = round(t_hess, 1)
                per_setup['attempts'].append(analysis)
                mu_str = f"{analysis['mu_Goldstone']:.3f}" if analysis['mu_Goldstone'] is not None else "n/a"
                print(f"  seed={seed}: F={analysis['F']}, μ_G={mu_str}, "
                      f"|∂S|={analysis['cluster_perimeter']}, u_max={analysis['u_max']:.3f}, "
                      f"opt={t_opt:.0f}s, hess={t_hess:.0f}s", flush=True)
            except Exception as e:
                print(f"  seed={seed}: EXCEPTION {type(e).__name__}: {e}", flush=True)
                per_setup['attempts'].append({'seed': seed, 'status': 'exception', 'error': str(e)})

        good = [a for a in per_setup['attempts'] if a.get('mu_Goldstone') is not None]
        if good:
            mus = [a['mu_Goldstone'] for a in good]
            perims = [a['cluster_perimeter'] for a in good]
            ovs = [a['best_overlap'] for a in good]
            per_setup['summary'] = {
                'n_good': len(good), 'mu_mean': float(np.mean(mus)),
                'mu_std': float(np.std(mus)) if len(mus) > 1 else 0.0,
                'perim_mean': float(np.mean(perims)),
                'overlap_mean': float(np.mean(ovs)),
            }
            s = per_setup['summary']
            print(f"  → m={m}: μ_G mean={s['mu_mean']:.3f}±{s['mu_std']:.3f}, "
                  f"|∂S| mean={s['perim_mean']:.1f}, overlap mean={s['overlap_mean']:.2f}", flush=True)
        else:
            per_setup['summary'] = {'n_good': 0}
            print(f"  → m={m}: NO GOOD ATTEMPTS", flush=True)
        results['per_setup'].append(per_setup)
        print(flush=True)

    print("=" * 60, flush=True)
    print("CROSS-SETUP COMPARISON (TORUS)", flush=True)
    print(f"{'m':>4} {'L':>3} {'c':>6} {'n':>2} {'μ_mean':>8} {'μ_std':>7} "
          f"{'|∂S|':>6} {'μ·n/|∂S|':>10} {'2α(=2)':>7}", flush=True)
    for s in results['per_setup']:
        m, L, c = s['m'], s['L'], s['c']
        sm = s.get('summary', {})
        if sm.get('n_good', 0) > 0:
            mu = sm['mu_mean']; perim = sm['perim_mean']; n = L * L
            ratio = mu * n / max(perim, 1)
            print(f"{m:>4} {L:>3} {c:>6.3f} {sm['n_good']:>2} "
                  f"{mu:>8.3f} {sm['mu_std']:>7.3f} {perim:>6.1f} "
                  f"{ratio:>10.2f} {2.0:>7.1f}", flush=True)

    elapsed = time.time() - t_global
    results['meta']['elapsed_s'] = round(elapsed, 1)
    results['meta']['finished_at'] = time.strftime('%Y-%m-%dT%H:%M:%S')

    out_path = os.path.join(os.path.dirname(__file__), 'results', 'nq198f_V5bTprime_torus.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        for setup in results['per_setup']:
            for a in setup['attempts']:
                a.pop('graph', None); a.pop('params', None); a.pop('n', None)
                a.pop('u', None)
        json.dump(results, f, indent=2, default=str)
    print(flush=True)
    print(f"Saved: {out_path}", flush=True)
    print(f"Elapsed: {elapsed/60:.1f} min", flush=True)


if __name__ == '__main__':
    main()
