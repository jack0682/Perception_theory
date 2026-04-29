"""NQ-198g: β-dependence of C in μ ≈ C(β, ξ_0) · |∂S|/n (V5b-F free-BC).

Day 3 EOD spawn (`07_*` §7).

Test β scan at fixed L=20, c=0.10 to determine C(β) functional form.

Setup:
  - L=20 (NQ-198a anchor), c=0.10, free-BC.
  - β ∈ {2, 3, 4, 6, 8}; ξ_0 = 1/√β ∈ {0.707, 0.577, 0.5, 0.408, 0.354}.
  - 3 seeds each.

Predictions:
  - Phase 3 form: C(β) ∝ β/ξ_0 = β^{3/2} → C(β=2)/C(β=4)=2^{-3/2}*4^{3/2}/2^{3/2}=??
    Actually μ = A_R3b·β·|∂S|/ξ_0 with A_R3b const → C = A_R3b·β·n/ξ_0 dim-wise.
    Hmm Phase 3 wasn't in the form C(β)·|∂S|/n. Replot.
  - Day 3 §4: μ ≈ 2α = 2 const → C(β) = 2n/|∂S| → not const since |∂S|, n fixed.
  - Empirical NQ-198a fit: μ ≈ 13·|∂S|/n at β=4. Hypothesis: μ ∝ β → C(β) ≈ π·β.
    → C(β=2)≈6.28, C(β=4)≈12.57, C(β=8)≈25.13.

Run: cd CODE && python3 scripts/nq198g_beta_scan.py
Expected runtime: ~3-5 min (5 β values × 3 seeds × L=20).
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import grad_bd

# Reuse setup from NQ-198a
from scripts.nq198a_V5bTprime_mass_dependence import (
    build_free_bc_2d, count_local_maxima_free_bc, translation_modes_free_bc,
    compute_hessian_lowest, estimate_cluster_perimeter, find_F1_minimizer,
    analyze_minimizer
)


def main():
    L = 20
    c = 0.10
    betas = [2.0, 3.0, 4.0, 6.0, 8.0]
    seeds = list(range(3))

    results = {
        'meta': {
            'L': L, 'c': c, 'graph_type': '2D_free_BC',
            'betas': betas, 'seeds_per_beta': len(seeds),
            'started_at': time.strftime('%Y-%m-%dT%H:%M:%S'),
        },
        'per_beta': [],
    }

    print(f"NQ-198g β-scan at L={L}, c={c}, free-BC", flush=True)
    print(f"=" * 60, flush=True)
    print(f"5 β values × 3 seeds = 15 attempts", flush=True)

    t_global = time.time()
    for beta in betas:
        xi_0 = 1.0 / np.sqrt(beta)
        per_beta = {'beta': beta, 'xi_0': float(xi_0), 'attempts': []}
        print(f"\n[β={beta}] ξ_0={xi_0:.3f}, ζ={xi_0:.3f}:", flush=True)

        for seed in seeds:
            t_s = time.time()
            try:
                res = find_F1_minimizer(L, beta, c, seed, max_iter=15000)
                if res is None:
                    print(f"  seed={seed}: no minimizer", flush=True)
                    per_beta['attempts'].append({'seed': seed, 'status': 'no_minimizer'})
                    continue
                t_opt = time.time() - t_s
                analysis = analyze_minimizer(res, L, beta)
                analysis['seed'] = seed
                analysis['time_optimizer_s'] = round(t_opt, 1)
                per_beta['attempts'].append(analysis)
                mu_str = f"{analysis['mu_Goldstone']:.3f}" if analysis['mu_Goldstone'] is not None else "n/a"
                # Compute C = mu * n / |∂S|
                n = L * L
                perim = analysis['cluster_perimeter']
                C_emp = analysis['mu_Goldstone'] * n / max(perim, 1) if analysis['mu_Goldstone'] is not None and perim > 0 else None
                C_str = f"{C_emp:.2f}" if C_emp else "n/a"
                print(f"  seed={seed}: μ={mu_str}, |∂S|={perim}, u_max={analysis['u_max']:.3f}, "
                      f"C={C_str}, t={t_opt:.0f}s", flush=True)
            except Exception as e:
                print(f"  seed={seed}: EXCEPTION {type(e).__name__}: {e}", flush=True)
                per_beta['attempts'].append({'seed': seed, 'status': 'exception', 'error': str(e)})

        good = [a for a in per_beta['attempts']
                if a.get('mu_Goldstone') is not None and a.get('cluster_perimeter', 0) > 0]
        if good:
            mus = [a['mu_Goldstone'] for a in good]
            perims = [a['cluster_perimeter'] for a in good]
            n = L * L
            Cs = [mus[i] * n / perims[i] for i in range(len(good))]
            per_beta['summary'] = {
                'n_good': len(good), 'mu_mean': float(np.mean(mus)),
                'perim_mean': float(np.mean(perims)),
                'C_mean': float(np.mean(Cs)), 'C_std': float(np.std(Cs)) if len(Cs) > 1 else 0.0,
            }
            s = per_beta['summary']
            print(f"  → β={beta}: μ={s['mu_mean']:.3f}, |∂S|={s['perim_mean']:.0f}, "
                  f"C={s['C_mean']:.2f}±{s['C_std']:.2f}", flush=True)
        else:
            per_beta['summary'] = {'n_good': 0}
            print(f"  → β={beta}: NO VALID DATA", flush=True)
        results['per_beta'].append(per_beta)

    # Cross-β analysis
    print(flush=True)
    print(f"=" * 60, flush=True)
    print(f"CROSS-β COMPARISON", flush=True)
    print(f"{'β':>4} {'ξ_0':>6} {'μ':>8} {'|∂S|':>5} {'C_emp':>7} "
          f"{'C/β':>7} {'C/β^1.5':>9} {'π·β':>7}", flush=True)
    for s in results['per_beta']:
        beta = s['beta']; xi_0 = s['xi_0']
        sm = s.get('summary', {})
        if sm.get('n_good', 0) > 0:
            C = sm['C_mean']; mu = sm['mu_mean']; perim = sm['perim_mean']
            print(f"{beta:>4.1f} {xi_0:>6.3f} {mu:>8.3f} {perim:>5.0f} {C:>7.2f} "
                  f"{C/beta:>7.3f} {C/(beta**1.5):>9.3f} {np.pi*beta:>7.2f}", flush=True)

    elapsed = time.time() - t_global
    results['meta']['elapsed_s'] = round(elapsed, 1)
    results['meta']['finished_at'] = time.strftime('%Y-%m-%dT%H:%M:%S')

    out_path = os.path.join(os.path.dirname(__file__), 'results', 'nq198g_beta_scan.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        for s in results['per_beta']:
            for a in s['attempts']:
                a.pop('graph', None); a.pop('params', None); a.pop('n', None)
                a.pop('u', None)
                if 'mode_records' in a:
                    a['mode_records'] = [{k: v for k, v in m.items() if not isinstance(v, np.ndarray)}
                                         for m in a['mode_records']]
        json.dump(results, f, indent=2, default=str)
    print(flush=True)
    print(f"Saved: {out_path}", flush=True)
    print(f"Elapsed: {elapsed/60:.1f} min", flush=True)


if __name__ == '__main__':
    main()
