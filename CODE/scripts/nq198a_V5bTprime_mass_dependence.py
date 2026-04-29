"""NQ-198a: V5b-T' / V5b-F PN-barrier Goldstone mass-dependence test.

Day 3 deepening pass spawn (`THEORY/logs/daily/2026-04-29/05_*` §7).

Question: Does the V5b-T'/V5b-F Goldstone-like Hessian eigenvalue depend on
cluster mass m?
  - Phase 3 heuristic predicts μ ∝ |∂S| ∝ √m.
  - Day 3 §4 derivation (`05_*`) predicts μ ≈ 2α = 2βξ_0² (mass-independent).

Setup:
  - 2D free BC graphs (V5b-F regime; mechanism parallels V5b-T' on torus).
  - β = 4, ξ_0 = 0.5, ζ = 0.5 (R3b corner-saturated regime).
  - 4 mass values: m ∈ {20, 40, 80, 160}.
  - L matched to keep c ≈ 0.10:
      m=20  → L=14, c=0.102
      m=40  → L=20, c=0.100  (NQ-173 setup; sanity-check anchor)
      m=80  → L=28, c=0.102
      m=160 → L=40, c=0.100
  - Seeds: N=3 per (m, L). Total 12 attempts.

Per-minimizer measurements:
  - Hessian lowest 6 non-tangent eigvals.
  - Lowest non-tangent eigvec → Goldstone-like (max translation overlap, full-space).
  - Eigval of best-Goldstone mode = μ_Gold^lifted candidate.
  - Cluster perimeter |∂S| from saturated-site count.

Output: scripts/results/nq198a_V5bTprime_mass.json

Expected runtime: ~20-30 min on standard CPU.

Predictions:
  Phase 3:    μ(m=20)/μ(m=40) ≈ √(0.5) ≈ 0.71
              μ(m=80)/μ(m=40) ≈ √(2.0) ≈ 1.41
              μ(m=160)/μ(m=40) ≈ √(4.0) = 2.0
  Day 3 §4:   μ(m) ≈ const ≈ 2 across all m.

Decision: NQ-198a result drives D-5 V5b-T' canonical text:
  - If mass-independent confirmed → D-5-A1 revised text (`05_*` §5.3).
  - If √m scaling confirmed → D-5-A1 original Phase 3 form retained.
  - If neither → spawn NQ-198a-followup.

Run: cd CODE && python3 scripts/nq198a_V5bTprime_mass_dependence.py
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import grad_bd


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
    return GraphState(sp.csr_matrix(
        (np.ones(len(rows)), (rows, cols)), shape=(n, n))), n


def count_local_maxima_free_bc(u, L):
    g = u.reshape(L, L)
    F = 0
    for i in range(L):
        for j in range(L):
            v = g[i, j]
            ok = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < L and 0 <= nj < L:
                    if g[ni, nj] >= v:
                        ok = False; break
            if ok: F += 1
    return F


def translation_modes_free_bc(u, L):
    g = u.reshape(L, L)
    du_x = np.zeros((L, L)); du_x[:-1, :] = g[1:, :] - g[:-1, :]
    du_y = np.zeros((L, L)); du_y[:, :-1] = g[:, 1:] - g[:, :-1]
    out = []
    for name, m in [('x', du_x.flatten()), ('y', du_y.flatten())]:
        norm = np.linalg.norm(m)
        out.append((name, m / norm if norm > 1e-14 else m))
    return out


def compute_hessian_lowest(u_star, graph, params, n_modes=6, eps=1e-4):
    n = graph.n if hasattr(graph, 'n') else u_star.shape[0]
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


def estimate_cluster_perimeter(u, L, sat_threshold=0.9):
    """Count edges where u jumps across sat_threshold — proxy for |∂S|."""
    g = u.reshape(L, L)
    sat = (g >= sat_threshold).astype(int)
    perim = 0
    for i in range(L):
        for j in range(L):
            if sat[i, j] == 1:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < L and 0 <= nj < L:
                        if sat[ni, nj] == 0: perim += 1
                    else:
                        perim += 1  # boundary edge counts
    return perim


def find_F1_minimizer(L, beta, c, seed, max_iter=15000):
    graph, n = build_free_bc_2d(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=max_iter,
    )
    # NQ-191 P2 patch: pass via find_formation kwarg (Phase 4 F17)
    xi_0 = np.sqrt(1.0 / beta)
    r0 = np.sqrt(c * L * L / np.pi)
    # Sharp IC: square cluster of m sites pre-saturated to 0.99 (forces corner-sat basin).
    # Multi-IC: vary cluster placement + smoothness; sharp ICs first to bias toward corner-sat.
    ic_configs = [
        ('sharp_corner_BL',  'square', 0.99, 0.01, (1, 1)),
        ('sharp_corner_TR',  'square', 0.99, 0.01, (-1, -1)),  # anchor=top-right
        ('sharp_corner_TL',  'square', 0.99, 0.01, (1, -1)),
        ('sharp_corner_BR',  'square', 0.99, 0.01, (-1, 1)),
        ('sharp_center',     'square', 0.99, 0.01, None),
        ('soft_center',      'tanh',   None, None, None),
    ]

    attempts = []
    for ic_id, (label, kind, hi, lo, anchor) in enumerate(ic_configs):
        np.random.seed(seed * 53 + 13 + ic_id * 1000)
        if kind == 'square':
            # Build square cluster of side ~ sqrt(m) sites
            side = int(np.ceil(np.sqrt(c * L * L)))
            if anchor is not None:
                ax_raw, ay_raw = anchor
                # Negative anchors mean from top/right
                ax = ax_raw if ax_raw >= 0 else (L - side + ax_raw)
                ay = ay_raw if ay_raw >= 0 else (L - side + ay_raw)
            else:
                ax = max(1, (L - side) // 2 + np.random.randint(-1, 2))
                ay = max(1, (L - side) // 2 + np.random.randint(-1, 2))
            ax = max(0, min(ax, L - side)); ay = max(0, min(ay, L - side))
            u_init = np.full(n, lo)
            for ii in range(ax, ax + side):
                for jj in range(ay, ay + side):
                    if 0 <= ii < L and 0 <= jj < L:
                        u_init[ii * L + jj] = hi
            # Adjust to exact volume m
            cur_sum = np.sum(u_init)
            target = c * n
            adj = (target - cur_sum) / n
            u_init = np.clip(u_init + adj, 0.01, 0.99)
        else:  # tanh
            cx = np.random.uniform(0.5, L - 0.5)
            cy = np.random.uniform(0.5, L - 0.5)
            i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
            dx = np.abs(i_idx - cx); dy = np.abs(j_idx - cy)
            r = np.sqrt(dx**2 + dy**2).flatten()
            u_init = 0.5 * (1.0 - np.tanh((r - r0) / max(xi_0, 0.2)))
        u_init = np.clip(u_init + np.random.normal(0, 0.01, size=n), 0.01, 0.99)

        try:
            res = find_formation(graph, params, normalize=False, verbose=False,
                                 u_init=u_init, allow_outside_spinodal=True)
            # Accept near-stationary states (NQ-173 monkey-patch logic)
            if not res.converged and len(res.energy_history) > 10:
                tail = res.energy_history[-max(10, len(res.energy_history) // 10):]
                rel_change = abs(tail[-1] - tail[0]) / max(abs(tail[0]), 1e-12)
                if rel_change < 1e-3: res.converged = True
            if not res.converged: continue
            F = count_local_maxima_free_bc(res.u, L)
            u_max = float(np.max(res.u))
            attempts.append({'F': F, 'energy': float(res.energy), 'u': res.u,
                             'ic_id': ic_id, 'u_max': u_max,
                             'corner_sat': u_max >= 0.95})
        except Exception as e:
            print(f"  attempt seed={seed} ic={ic_id}: {type(e).__name__}: {e}", flush=True)
            continue

    if not attempts: return None
    # Prefer corner-saturated (u_max >= 0.95) attempts; among those, lowest energy.
    cs = [a for a in attempts if a['corner_sat']]
    if cs:
        best = min(cs, key=lambda a: a['energy'])
        best['F1_found'] = (best['F'] == 1)
    else:
        # No corner-saturation: fall back, but flag.
        best = min(attempts, key=lambda a: a['energy'])
        best['F1_found'] = False
    best['graph'] = graph; best['params'] = params; best['n'] = n
    return best


def analyze_minimizer(result, L, beta):
    """Extract Goldstone eigval + cluster perimeter."""
    u = result['u']; graph = result['graph']; params = result['params']; n = result['n']
    trans_modes = translation_modes_free_bc(u, L)
    tangent = np.ones(n) / np.sqrt(n)

    eigvals, eigvecs = compute_hessian_lowest(u, graph, params, n_modes=8)

    best_idx = -1; best_overlap = -1.0
    mode_records = []
    for k in range(eigvecs.shape[1]):
        v = eigvecs[:, k]
        ov_t = float(abs(np.dot(v, tangent)))
        if ov_t > 0.5:  # skip volume tangent
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

    perim = estimate_cluster_perimeter(u, L)
    return {
        'mu_Goldstone': float(eigvals[best_idx]) if best_idx >= 0 else None,
        'best_overlap': best_overlap if best_idx >= 0 else 0.0,
        'best_idx': best_idx,
        'cluster_perimeter': perim,
        'mode_records': mode_records,
        'F': count_local_maxima_free_bc(u, L),
        'F1_found': result['F1_found'],
        'energy': result['energy'],
        'u_max': float(np.max(u)),
        'u_min': float(np.min(u)),
        'fraction_saturated': float(np.mean(u >= 0.9)),
    }


def main():
    # Two parallel mass-dep sweeps:
    # (a) Fixed L=20, vary c (and hence m): tests μ vs m at fixed L (NQ-173 anchor included).
    # (b) Fixed c≈0.10, vary L (and hence m): tests μ vs m at fixed c.
    # Setups labeled (m, L, sweep_id):
    setups = [
        # Sweep (a): fixed L=20, varied c
        (40, 20, 'a_L20_c10', 0.10),
        (80, 20, 'a_L20_c20', 0.20),
        (120, 20, 'a_L20_c30', 0.30),
        (160, 20, 'a_L20_c40', 0.40),
        # Sweep (b): fixed c~0.10, varied L
        (80, 28, 'b_c10_L28', 80/784.0),
        (160, 40, 'b_c10_L40', 160/1600.0),
        # Out-of-V5b-T' regime control: m=20 small-cluster at L=14 c=0.10
        (20, 14, 'c_L14_c10', 20/196.0),
    ]
    beta = 4.0
    seeds = list(range(3))

    results = {
        'meta': {
            'beta': beta, 'xi_0': float(np.sqrt(1.0 / beta)), 'zeta': 0.5,
            'setups': [{'m': m, 'L': L, 'sweep_id': sid, 'c': c}
                       for m, L, sid, c in setups],
            'seeds_per_setup': len(seeds),
            'total_attempts': len(setups) * len(seeds),
            'predictions': {
                'Phase_3_heuristic': 'mu propto sqrt(m); mu(20)/mu(40)=0.71, mu(80)/mu(40)=1.41, mu(160)/mu(40)=2.0',
                'Day_3_section_4': 'mu approx 2*alpha = 2*beta*xi_0^2 = 2*4*0.25 = 2 (constant across m)',
            },
            'started_at': time.strftime('%Y-%m-%dT%H:%M:%S'),
        },
        'per_setup': [],
    }

    print(f"NQ-198a V5b-T'/V5b-F Goldstone mass-dependence", flush=True)
    print(f"=" * 60, flush=True)
    print(f"beta={beta}, xi_0=0.5, zeta=0.5 (R3b corner-saturated)", flush=True)
    print(f"{len(setups)} setups (m, L, sweep_id, c):", flush=True)
    for m, L, sid, c in setups:
        print(f"  m={m:3d}, L={L:2d}, sweep={sid}, c={c:.4f}", flush=True)
    print(f"Seeds per setup: {len(seeds)}; total {len(setups)*len(seeds)} attempts", flush=True)
    print(flush=True)

    t_global = time.time()
    for setup_idx, (m, L, sid, c) in enumerate(setups):
        n = L * L
        # Iterations scale with n; bigger L needs more
        max_iter = max(15000, 3 * n)
        per_setup = {'m': m, 'L': L, 'sweep_id': sid, 'c': c, 'attempts': []}
        print(f"[{setup_idx+1}/{len(setups)}] m={m}, L={L}, sweep={sid}, c={c:.4f} (max_iter={max_iter}):", flush=True)

        for seed in seeds:
            t_s = time.time()
            try:
                res = find_F1_minimizer(L, beta, c, seed, max_iter=max_iter)
                if res is None:
                    print(f"  seed={seed}: no minimizer found", flush=True)
                    per_setup['attempts'].append({'seed': seed, 'status': 'no_minimizer'})
                    continue
                t_opt = time.time() - t_s
                t_h = time.time()
                analysis = analyze_minimizer(res, L, beta)
                t_hess = time.time() - t_h
                analysis['seed'] = seed
                analysis['time_optimizer_s'] = round(t_opt, 1)
                analysis['time_hessian_s'] = round(t_hess, 1)
                per_setup['attempts'].append(analysis)
                mu_str = f"{analysis['mu_Goldstone']:.3f}" if analysis['mu_Goldstone'] is not None else "n/a"
                print(f"  seed={seed}: F={analysis['F']}, μ_G={mu_str}, "
                      f"|∂S|={analysis['cluster_perimeter']}, "
                      f"u_max={analysis['u_max']:.3f}, "
                      f"opt={t_opt:.0f}s, hess={t_hess:.0f}s", flush=True)
            except Exception as e:
                print(f"  seed={seed}: EXCEPTION {type(e).__name__}: {e}", flush=True)
                per_setup['attempts'].append({'seed': seed, 'status': 'exception',
                                              'error': str(e)})

        # Per-setup summary
        good = [a for a in per_setup['attempts'] if a.get('mu_Goldstone') is not None]
        if good:
            mus = [a['mu_Goldstone'] for a in good]
            perims = [a['cluster_perimeter'] for a in good]
            ovs = [a['best_overlap'] for a in good]
            per_setup['summary'] = {
                'n_good': len(good), 'mu_mean': float(np.mean(mus)),
                'mu_std': float(np.std(mus)) if len(mus) > 1 else 0.0,
                'mu_min': float(np.min(mus)), 'mu_max': float(np.max(mus)),
                'perim_mean': float(np.mean(perims)),
                'overlap_mean': float(np.mean(ovs)),
            }
            s = per_setup['summary']
            print(f"  → m={m}: μ_G mean={s['mu_mean']:.3f}±{s['mu_std']:.3f}, "
                  f"|∂S| mean={s['perim_mean']:.1f}, "
                  f"overlap mean={s['overlap_mean']:.2f}", flush=True)
        else:
            per_setup['summary'] = {'n_good': 0}
            print(f"  → m={m}: NO GOOD ATTEMPTS", flush=True)
        results['per_setup'].append(per_setup)
        print(flush=True)

    # Cross-setup comparison
    summaries = [(s['m'], s['summary']) for s in results['per_setup']
                 if s.get('summary', {}).get('n_good', 0) > 0]
    print(f"=" * 60, flush=True)
    print(f"CROSS-SETUP COMPARISON", flush=True)
    print(f"{'m':>4} {'L':>3} {'c':>6} {'n':>2} {'μ_mean':>8} {'μ_std':>7} "
          f"{'|∂S|_mean':>10} {'ov_mean':>8}", flush=True)
    for s in results['per_setup']:
        m, L, c = s['m'], s['L'], s['c']
        sm = s.get('summary', {})
        if sm.get('n_good', 0) > 0:
            print(f"{m:>4} {L:>3} {c:>6.3f} {sm['n_good']:>2} "
                  f"{sm['mu_mean']:>8.3f} {sm['mu_std']:>7.3f} "
                  f"{sm['perim_mean']:>10.1f} {sm['overlap_mean']:>8.2f}", flush=True)
        else:
            print(f"{m:>4} {L:>3} {c:>6.3f}  0    n/a     n/a       n/a      n/a", flush=True)

    # Test predictions
    if len(summaries) >= 2:
        print(flush=True)
        print(f"PREDICTION TEST", flush=True)
        # Reference: m=40 if available, else first
        ref_idx = next((i for i, (m, _) in enumerate(summaries) if m == 40), 0)
        ref_m, ref_s = summaries[ref_idx]
        ref_mu = ref_s['mu_mean']
        print(f"Reference: m={ref_m}, μ_ref={ref_mu:.3f}", flush=True)
        print(f"{'m':>4} {'μ_meas':>8} {'μ_meas/μ_ref':>14} "
              f"{'Phase3_pred':>13} {'Day3_§4_pred':>14}", flush=True)
        for m, s in summaries:
            ratio_meas = s['mu_mean'] / ref_mu if ref_mu > 1e-9 else 0
            ratio_phase3 = np.sqrt(m / ref_m)
            ratio_day3 = 1.0  # constant
            print(f"{m:>4} {s['mu_mean']:>8.3f} {ratio_meas:>14.3f} "
                  f"{ratio_phase3:>13.3f} {ratio_day3:>14.3f}", flush=True)

    elapsed = time.time() - t_global
    results['meta']['elapsed_s'] = round(elapsed, 1)
    results['meta']['finished_at'] = time.strftime('%Y-%m-%dT%H:%M:%S')

    out_path = os.path.join(os.path.dirname(__file__), 'results', 'nq198a_V5bTprime_mass.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        # Strip non-serializable objects
        for setup in results['per_setup']:
            for a in setup['attempts']:
                a.pop('graph', None); a.pop('params', None); a.pop('n', None)
                a.pop('u', None)
                if 'mode_records' in a:
                    for mr in a['mode_records']:
                        for k in list(mr.keys()):
                            if isinstance(mr[k], np.ndarray):
                                mr[k] = mr[k].tolist()
        json.dump(results, f, indent=2, default=str)
    print(flush=True)
    print(f"Saved: {out_path}", flush=True)
    print(f"Elapsed: {elapsed/60:.1f} min", flush=True)


if __name__ == '__main__':
    main()
