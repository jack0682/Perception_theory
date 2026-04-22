#!/usr/bin/env python3
"""
exp_profile_fit.py — NQ-32: SCC full minimizer profile vs tanh ansatz.

Origin: logs/daily/2026-04-22/ (SF-S1 session), G5 deliverable.
Theory: working/SF/profile_deviation.md §4 (3 candidate profiles).

Goal
----
Measure radial profile u*(r) of find_formation output at varied (alpha, beta),
fit three candidates:
  (C1) Pure tanh:       u(r) = 0.5 * (1 - tanh((r - r0) / xi))
  (C2) Perturbed tanh:  u(r) = 0.5 * (1 - tanh((r - r0) / xi)) + eps * g(r)
                        where g(r) = sech^2((r - r0) / xi) ("tanh-width perturbation")
  (C3) Generalized soliton:
                        u(r) = 0.5 * (1 - tanh((r - r0) / xi)^p)  (shape exponent p)

Extract effective xi_fitted per fit, compare to theoretical xi_theory = sqrt(alpha/beta).

Round 18 observation at (alpha=2, beta=80, xi_theory=0.158):
  - measured ratio_edge = 0.875, ansatz predicted 0.546 (+60%)
  - measured ratio_site = 0.323, ansatz predicted 0.386 (-16%)
  The profile deviation correlates with Prop 1.3b cl_sep Hessian structure
  (working/SF/mode_count.md §2.3: 1641 negative eigenvalues at canonical defaults).

Method
------
1. For each (alpha, beta) with xi_theory in asymptotic regime [0.10, 0.30]:
   a. Run find_formation with K_soft <= 0.55 filter (sharp K=1).
   b. Extract formation center (center-of-mass of {x: u[x] >= 0.5}).
   c. Bin sites by distance r from center; compute binned mean u(r).
   d. Fit three candidate profiles via scipy.optimize.least_squares.
   e. Record xi_fitted, fit R^2, residuals per profile.
2. Scan (alpha, beta) grid.
3. Report effective xi_fitted / xi_theory vs parameters.
4. Identify which profile (C1 / C2 / C3) fits best at each point.

Expected runtime: 15-30 min on 48x48 grid, 9 (alpha, beta) pairs, n_inits=24.

Usage
-----
  cd CODE && python3 experiments/exp_profile_fit.py [--grid-size 48] [--n-inits 24]

Execution: USER LOCAL ONLY (per G5 plan: script only).
"""
import sys
import os
import json
import argparse
import time
import threading
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation

try:
    from scc.k_soft import k_soft
    HAS_KSOFT = True
except ImportError:
    HAS_KSOFT = False


# ---------------------------------------------------------------------------
# Candidate profiles
# ---------------------------------------------------------------------------

def profile_tanh(r, xi, r0, u_max=1.0, u_min=0.0):
    """Pure tanh soliton: u(r) = u_min + (u_max - u_min) * 0.5 * (1 - tanh((r - r0)/xi))."""
    return u_min + (u_max - u_min) * 0.5 * (1.0 - np.tanh((r - r0) / max(xi, 1e-8)))


def profile_perturbed_tanh(r, xi, r0, eps, u_max=1.0, u_min=0.0):
    """Tanh + sech^2 perturbation (modulates width at interface)."""
    arg = (r - r0) / max(xi, 1e-8)
    base = 0.5 * (1.0 - np.tanh(arg))
    perturb = eps * (1.0 / np.cosh(arg)) ** 2
    return u_min + (u_max - u_min) * (base + perturb)


def profile_generalized(r, xi, r0, p, u_max=1.0, u_min=0.0):
    """Shape-exponent soliton: tanh((r - r0)/xi)^p in signed sense.

    For p = 1: reduces to pure tanh.
    For p != 1: asymmetric in growth rate around r0.
    """
    arg = (r - r0) / max(xi, 1e-8)
    t = np.tanh(arg)
    # signed power: preserves sign of t
    sign = np.sign(t)
    mag = np.abs(t) ** max(p, 0.01)
    signed = sign * mag
    return u_min + (u_max - u_min) * 0.5 * (1.0 - signed)


# ---------------------------------------------------------------------------
# Radial profile extraction
# ---------------------------------------------------------------------------

def extract_radial_profile(u, grid_size, n_bins=None):
    """Extract u(r) by binning sites by distance from formation center.

    Formation center: center-of-mass of {x: u[x] >= 0.5} (if empty, use grid midpoint).
    """
    L = grid_size
    xs, ys = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    u_grid = u.reshape(L, L)

    mask = u_grid >= 0.5
    if mask.sum() > 0:
        cx = float(np.sum(xs * mask) / mask.sum())
        cy = float(np.sum(ys * mask) / mask.sum())
    else:
        cx, cy = (L - 1) / 2.0, (L - 1) / 2.0

    r = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2).flatten()
    uvals = u_grid.flatten()

    r_max = float(r.max())
    if n_bins is None:
        n_bins = max(20, int(r_max) + 1)

    bin_edges = np.linspace(0, r_max + 1e-3, n_bins + 1)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    bin_mean = np.full(n_bins, np.nan)
    bin_count = np.zeros(n_bins, dtype=int)

    for i in range(n_bins):
        sel = (r >= bin_edges[i]) & (r < bin_edges[i + 1])
        if sel.sum() > 0:
            bin_mean[i] = float(uvals[sel].mean())
            bin_count[i] = int(sel.sum())

    valid = ~np.isnan(bin_mean)
    return bin_centers[valid], bin_mean[valid], bin_count[valid], (cx, cy)


# ---------------------------------------------------------------------------
# Fits
# ---------------------------------------------------------------------------

def fit_profile(r_data, u_data, profile_name, xi_init, r0_init):
    """Nonlinear least-squares fit of one candidate profile."""
    from scipy.optimize import least_squares

    if profile_name == 'tanh':
        def residuals(params):
            xi, r0 = params
            return profile_tanh(r_data, xi, r0) - u_data
        x0 = [xi_init, r0_init]
        bounds = ([1e-3, 0.0], [50.0, 1000.0])
    elif profile_name == 'perturbed':
        def residuals(params):
            xi, r0, eps = params
            return profile_perturbed_tanh(r_data, xi, r0, eps) - u_data
        x0 = [xi_init, r0_init, 0.0]
        bounds = ([1e-3, 0.0, -2.0], [50.0, 1000.0, 2.0])
    elif profile_name == 'generalized':
        def residuals(params):
            xi, r0, p = params
            return profile_generalized(r_data, xi, r0, p) - u_data
        x0 = [xi_init, r0_init, 1.0]
        bounds = ([1e-3, 0.0, 0.1], [50.0, 1000.0, 5.0])
    else:
        raise ValueError(f"unknown profile: {profile_name}")

    try:
        result = least_squares(residuals, x0, bounds=bounds, method='trf')
    except Exception as exc:
        return {'success': False, 'error': str(exc)}

    resid = residuals(result.x)
    ss_res = float(np.sum(resid ** 2))
    ss_tot = float(np.sum((u_data - u_data.mean()) ** 2))
    r_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan

    entry = {
        'success': bool(result.success),
        'xi_fitted': float(result.x[0]),
        'r0_fitted': float(result.x[1]),
        'r_squared': float(r_squared),
        'rms_residual': float(np.sqrt(ss_res / len(r_data))),
    }
    if profile_name == 'perturbed':
        entry['eps'] = float(result.x[2])
    if profile_name == 'generalized':
        entry['p'] = float(result.x[2])
    return entry


# ---------------------------------------------------------------------------
# Measurement wrapper
# ---------------------------------------------------------------------------

def measure_at_config(alpha, beta, grid_size=48, c=0.3, n_inits=24, k_soft_max=0.55):
    """Run find_formation at config, extract profile, fit 3 candidates.

    Uses Round 18 exp_alpha_scan_v3 convention:
      - ParameterRegistry(beta_bd=beta, w_bd=alpha, w_cl=1.0, w_sep=1.0,
                          max_iter=5000, n_restarts=n_inits,
                          dt_init=0.01, eps_init=0.01)
      - find_formation() called ONCE; internal multi-start uses n_restarts seeds
        (seed=0 is Fiedler-initialized, others are random with eps_init).
    """
    graph = GraphState.grid_2d(grid_size, grid_size)
    params = ParameterRegistry(
        beta_bd=beta, volume_fraction=c,
        w_cl=1.0, w_sep=1.0, w_bd=alpha,
        max_iter=5000, n_restarts=n_inits,
        dt_init=0.01, eps_init=0.01,
    )

    xi_theory = float(np.sqrt(alpha / beta))

    # Heartbeat thread: emit progress every 8s during long find_formation call.
    _hb_stop = threading.Event()
    _hb_start = time.time()
    def _heartbeat():
        while not _hb_stop.wait(8.0):
            elapsed = time.time() - _hb_start
            print(f"      ... find_formation running α={alpha} β={beta} (elapsed {elapsed:.0f}s)", flush=True)
    _hb_thread = threading.Thread(target=_heartbeat, daemon=True)
    _hb_thread.start()

    try:
        result = find_formation(graph, params, verbose=False)
    except Exception as exc:
        return {
            'alpha': alpha, 'beta': beta, 'xi_theory': xi_theory,
            'n_inits': n_inits, 'k_soft_max': k_soft_max,
            'found': False, 'reason': f'find_formation failed: {exc}',
        }
    finally:
        _hb_stop.set()

    u_out = result.u
    if HAS_KSOFT:
        best_k_soft = float(k_soft(u_out, grid_size=grid_size))
    else:
        best_k_soft = np.inf
    best_energy = float(result.energy)

    if best_k_soft > k_soft_max:
        return {
            'alpha': alpha, 'beta': beta, 'xi_theory': xi_theory,
            'n_inits': n_inits, 'k_soft_max': k_soft_max,
            'found': False, 'reason': f'K_soft={best_k_soft:.3f} > {k_soft_max}',
            'k_soft_observed': best_k_soft, 'energy': best_energy,
        }

    best_u = u_out

    r_data, u_data, counts, center = extract_radial_profile(best_u, grid_size)

    fits = {}
    for pname in ('tanh', 'perturbed', 'generalized'):
        fits[pname] = fit_profile(r_data, u_data, pname, xi_init=xi_theory, r0_init=grid_size/6.0)

    # Extract xi_fitted / xi_theory
    xi_ratios = {pname: (fits[pname]['xi_fitted'] / xi_theory) if fits[pname].get('success') else np.nan
                 for pname in fits}

    # Pick best fit by R^2
    best_profile = max(fits, key=lambda p: fits[p].get('r_squared', -np.inf))

    return {
        'alpha': alpha, 'beta': beta, 'xi_theory': xi_theory,
        'grid_size': grid_size, 'n_inits': n_inits, 'k_soft_max': k_soft_max,
        'found': True, 'k_soft': best_k_soft, 'energy': best_energy,
        'center': list(center),
        'r_data': r_data.tolist(), 'u_data': u_data.tolist(), 'bin_counts': counts.tolist(),
        'fits': fits,
        'xi_ratios': xi_ratios,
        'best_profile': best_profile,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def _worker(task):
    """Worker for multiprocessing parallel execution.

    Limits BLAS thread count per worker to avoid CPU over-subscription.
    """
    idx, n_total, alpha, beta, kwargs = task
    # Cap BLAS threads per worker to prevent contention when configs run in parallel
    os.environ.setdefault('OMP_NUM_THREADS', '2')
    os.environ.setdefault('OPENBLAS_NUM_THREADS', '2')
    os.environ.setdefault('MKL_NUM_THREADS', '2')
    os.environ.setdefault('VECLIB_MAXIMUM_THREADS', '2')

    xi_th = float(np.sqrt(alpha / beta))
    print(f"  [{idx+1}/{n_total}] START alpha={alpha}, beta={beta}, xi_theory={xi_th:.3f}", flush=True)
    t_i = time.time()
    res = measure_at_config(alpha, beta, **kwargs)
    elapsed = time.time() - t_i
    res['elapsed_sec'] = elapsed

    if res['found']:
        print(f"  [{idx+1}/{n_total}] DONE α={alpha} β={beta}: K_soft={res['k_soft']:.3f}, "
              f"best={res['best_profile']}, xi_ratio(tanh)={res['xi_ratios']['tanh']:.3f}, "
              f"xi_ratio(gen)={res['xi_ratios']['generalized']:.3f} ({elapsed:.1f}s)", flush=True)
    else:
        print(f"  [{idx+1}/{n_total}] SKIP α={alpha} β={beta}: {res.get('reason')} ({elapsed:.1f}s)", flush=True)
    return idx, res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--grid-size', type=int, default=48)
    ap.add_argument('--n-inits', type=int, default=24)
    ap.add_argument('--c', type=float, default=0.3)
    ap.add_argument('--k-soft-max', type=float, default=0.55)
    ap.add_argument('--out', default='results/exp_profile_fit.json')
    ap.add_argument('--workers', type=int, default=1,
                    help='Parallel workers (1=serial, 4-6 recommended on M1 8-core)')
    args = ap.parse_args()

    # (alpha, beta) grid chosen to span xi_theory in [0.10, 0.30]
    # xi_theory = sqrt(alpha/beta); need asymptotic regime (xi << r_0) on grid.
    configs = [
          (5.0, 5.0), (10.0, 10.0), (20.0, 20.0),
          (10.0, 2.5), (20.0, 5.0), (40.0, 10.0),
          (10.0, 1.0), (20.0, 2.5), (40.0, 5.0),
    ]

    print(f"[exp_profile_fit] grid={args.grid_size} n_inits={args.n_inits} c={args.c} workers={args.workers}")
    print(f"[exp_profile_fit] scanning {len(configs)} (alpha, beta) configs...")

    t0 = time.time()
    kwargs = {
        'grid_size': args.grid_size,
        'c': args.c,
        'n_inits': args.n_inits,
        'k_soft_max': args.k_soft_max,
    }
    tasks = [(i, len(configs), a, b, kwargs) for i, (a, b) in enumerate(configs)]

    if args.workers <= 1:
        # Serial path (original behavior)
        results = [None] * len(configs)
        for task in tasks:
            idx, res = _worker(task)
            results[idx] = res
    else:
        # Parallel path via multiprocessing.Pool
        import multiprocessing as mp
        ctx = mp.get_context('spawn')  # 'spawn' required on macOS
        results = [None] * len(configs)
        with ctx.Pool(processes=args.workers) as pool:
            for idx, res in pool.imap_unordered(_worker, tasks):
                results[idx] = res

    total_elapsed = time.time() - t0
    out = {
        'session': '2026-04-22_SF-S1_G5',
        'purpose': 'NQ-32: SCC profile vs tanh ansatz',
        'configs': [{'alpha': a, 'beta': b} for a, b in configs],
        'grid_size': args.grid_size,
        'n_inits': args.n_inits,
        'c': args.c,
        'k_soft_max': args.k_soft_max,
        'results': results,
        'total_elapsed_sec': total_elapsed,
        'n_configs': len(configs),
        'n_found': sum(1 for r in results if r['found']),
    }

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)

    print(f"\n[exp_profile_fit] done in {total_elapsed:.1f}s. Wrote {out_path}")
    print(f"[exp_profile_fit] {out['n_found']}/{out['n_configs']} configs passed K_soft filter.")


if __name__ == '__main__':
    main()
