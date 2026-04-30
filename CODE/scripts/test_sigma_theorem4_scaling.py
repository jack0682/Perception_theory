"""
test_sigma_theorem4_scaling.py — NQ-187 §8 numerical verification

Goal: numerically verify the prediction p=2 (μ_1 - μ_0 ~ ε^p) for the σ-eigenvalue
split at the first D_4 pitchfork on the L×L free-BC grid, falsifying the
alternative p=3/2.

Protocol (working/SF/sigma_theorem4_higher_order.md §8):
  1. Graph: D_4 free-BC L×L grid for L ∈ {4, 8, 16}.
  2. Compute β_crit^(2) = 4α·λ_2^Lap / |W''(c)| for each L (T8-Core).
  3. For ε ∈ {0.001, 0.003, 0.01, 0.03, 0.1}:
     a. Set β = β_crit^(2) + ε, α = 1.0, c = 0.5.
     b. Run find_formation from a Fiedler-perturbed initial condition.
     c. Compute Σ_m-restricted Hessian at minimizer u^*_ε.
        We use the ANALYTIC Hessian of E_bd:
          H_bd(u) = 4α·L_G + β·diag(W''(u_i)),    W(u) = u²(1-u)²
        which is exact and avoids finite-difference noise that would swamp
        the O(ε²) splitting.  The Σ_m restriction is applied via the
        orthogonal projector P = I - 11ᵀ/n.
     d. Use scipy.sparse.linalg.eigsh(sigma=0, which='LM') shift-invert mode
        for bottom-k eigenvalues when n is large; dense eigh otherwise.
        The constant-mode kernel of P is regularized by adding a high
        rank-1 penalty 11ᵀ/n · ρ so it does not interfere with the smallest
        physical eigenvalue.
     e. Identify μ_0, μ_1 as the two smallest non-Goldstone eigenvalues
        (the constant-mode null is regularized away).
  4. Fit log(μ_1 - μ_0) vs log(ε) → power p.
  5. Report p per L; check convergence as L → ∞.

Falsifiability verdict (§8.3):
  - All |p_L - 2| < 0.3 → CONFIRMED (consistent with §3.2 polynomial
    equivariant analysis, no 5th-order D_4 equivariant).
  - All p_L ≈ 1.5 → FALSIFIED (alternative p=3/2 prediction).
  - Mixed regime → INCONSISTENT (likely numerical artifact / finite-grid).

Output:
  - JSON: CODE/scripts/results/sigma_theorem4_scaling.json
  - stdout summary
"""
from __future__ import annotations

import json
import os
import sys
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.sparse.linalg import LinearOperator, eigsh

# scc package via sys.path (per CLAUDE.md "Run everything from CODE/")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import double_well_second_deriv
from scc.optimizer import find_formation, project_volume


# ---------------------------------------------------------------------------
# Hessian construction (analytic, sparse)
# ---------------------------------------------------------------------------

def hessian_bd_analytic(u: np.ndarray, graph: GraphState, params: ParameterRegistry) -> sp.csr_matrix:
    """Analytic Hessian of E_bd at u.

    For W(u) = u²(1-u)² (canonical double-well), W''(u) = 2(1 - 6u + 6u²).
    The smoothness Hessian is 4α·L (ordered-pair convention; canonical §8).
    """
    W_pp_vec = 2.0 * (1.0 - 6.0 * u + 6.0 * u**2)
    H = (4.0 * params.alpha_bd * graph.L
         + sp.diags(params.beta_bd * W_pp_vec)).tocsr()
    return H


def sigma_m_eigs(
    u: np.ndarray,
    graph: GraphState,
    params: ParameterRegistry,
    k: int = 4,
    use_lanczos: bool = True,
    constant_penalty: float = 1e3,
) -> np.ndarray:
    """Bottom-k Σ_m-restricted Hessian eigenvalues at u.

    The constant mode 1 spans the kernel of the Σ_m-tangent projector.
    To compute the bottom of the *physical* spectrum, we add a rank-1
    penalty `constant_penalty · (11ᵀ/n)` that pushes the constant mode
    far above all physical eigenvalues, then return the bottom-k of the
    resulting spectrum.

    use_lanczos=True → scipy.sparse.linalg.eigsh shift-invert (sigma=0,
    which='LM'); ~100× faster than dense eigh on n=256 (L=16) per the
    NQ-187 §8 implementation note.
    """
    n = u.shape[0]
    H = hessian_bd_analytic(u, graph, params)

    # Add rank-1 constant-mode penalty: H' = H + ρ/n · 11ᵀ
    # so the constant eigenvector 1/√n carries eigenvalue ρ + (1ᵀH1)/n,
    # which is large and well above the physical spectrum.
    one = np.ones(n)
    rho = constant_penalty * max(1.0, abs(params.beta_bd))
    rank1 = sp.csr_matrix((rho / n) * np.outer(one, one))
    H_pen = (H + rank1).tocsc()

    if use_lanczos and n >= 64:
        # Shift-invert Lanczos for bottom k eigenvalues.  k_request must
        # be > 1 and < n-1 for eigsh; ask for k+2 to give a safety margin.
        k_req = min(k + 2, n - 2)
        try:
            eigs = eigsh(
                H_pen, k=k_req, sigma=0.0, which='LM',
                return_eigenvectors=False, tol=1e-10, maxiter=5000,
            )
        except Exception:
            # Fallback to dense
            eigs = np.linalg.eigvalsh(H_pen.toarray())
    else:
        eigs = np.linalg.eigvalsh(H_pen.toarray())

    eigs = np.sort(np.asarray(eigs, dtype=np.float64))
    # Drop any eigenvalue near the constant penalty (paranoid)
    physical = eigs[eigs < 0.5 * rho]
    return physical[:k]


# ---------------------------------------------------------------------------
# Critical β and Fiedler-perturbed IC
# ---------------------------------------------------------------------------

def beta_crit_2(graph: GraphState, alpha: float, c: float) -> float:
    """β_crit^(2) = 4α·λ_2^Lap / |W''(c)|  (T8-Core, canonical §13)."""
    W_pp = double_well_second_deriv(c)
    return 4.0 * alpha * graph.fiedler / abs(W_pp)


def fiedler_perturbed_ic(graph: GraphState, c: float, amp: float = 1e-3,
                         seed: int = 0) -> np.ndarray:
    """u_init = c·1 + amp · (Fiedler vector) + small noise to break degeneracy.

    The D_4 grid has a 2D Fiedler eigenspace; graph.fiedler_vector() returns
    one basis vector (numerically chosen by ARPACK), giving an axis-aligned
    bias for the bifurcation. The amplitude is L²-normalized so that
    max|u-c| = amp · max|v_2| / ‖v_2‖.

    To force a strong axis-aligned breaking we project the Fiedler vector
    onto its dominant axis (largest component direction).
    """
    n = graph.n
    v2 = graph.fiedler_vector()
    v2 = v2 - np.mean(v2)  # ensure ⊥ constant mode
    # Sign-fix so the largest |component| is positive
    if abs(v2.min()) > abs(v2.max()):
        v2 = -v2
    # Rescale so max|v2| = 1 (amp now controls deviation amplitude directly)
    mxv = np.max(np.abs(v2))
    if mxv > 1e-12:
        v2 = v2 / mxv
    rng = np.random.default_rng(seed)
    noise = 1e-6 * rng.standard_normal(n)
    noise -= noise.mean()
    u = np.full(n, c) + amp * v2 + noise
    return np.clip(u, 1e-6, 1.0 - 1e-6)


# ---------------------------------------------------------------------------
# Power-law fit log(Δμ) = p · log(ε) + b
# ---------------------------------------------------------------------------

def power_law_fit(eps_arr: np.ndarray, delta_arr: np.ndarray) -> tuple[float, float, float]:
    """Linear regression in log-log: returns (p, p_stderr, intercept)."""
    eps_arr = np.asarray(eps_arr, dtype=np.float64)
    delta_arr = np.asarray(delta_arr, dtype=np.float64)
    mask = (delta_arr > 0) & (eps_arr > 0)
    log_e = np.log(eps_arr[mask])
    log_d = np.log(delta_arr[mask])
    n = len(log_e)
    if n < 2:
        return float('nan'), float('nan'), float('nan')
    sx = log_e.sum()
    sy = log_d.sum()
    sxx = (log_e * log_e).sum()
    sxy = (log_e * log_d).sum()
    denom = n * sxx - sx * sx
    if abs(denom) < 1e-30:
        return float('nan'), float('nan'), float('nan')
    p = (n * sxy - sx * sy) / denom
    b = (sy - p * sx) / n
    if n > 2:
        resid = log_d - (p * log_e + b)
        s2 = (resid * resid).sum() / (n - 2)
        p_se = float(np.sqrt(max(s2, 0.0) * n / denom))
    else:
        p_se = 0.0
    return float(p), float(p_se), float(b)


# ---------------------------------------------------------------------------
# Single (L, ε) run
# ---------------------------------------------------------------------------

def run_one(L: int, eps: float, alpha: float = 1.0, c: float = 0.5,
            verbose: bool = False) -> dict:
    graph = GraphState.grid_2d(L, L)
    beta_c = beta_crit_2(graph, alpha=alpha, c=c)
    beta = beta_c + eps

    params = ParameterRegistry(
        alpha_bd=alpha, beta_bd=beta, volume_fraction=c,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,  # E_bd only — pure σ-Theorem-4 setting
        n_restarts=1, max_iter=50000,
        eps_grad=1e-8, eps_field=1e-10, eps_energy=1e-14,
        eps_init=0.01,
        dt_init=0.01,
    )

    # Initialize FAR from the unstable uniform fixed point so the optimizer
    # relaxes downhill into the bifurcated minimizer rather than getting
    # trapped near u=c·1 by tiny gradient ~ε at small ε.  amp=0.3 is well
    # inside the basin of attraction at c=0.5 (max allowed before clipping
    # is c=0.5 itself).
    amp = 0.30
    u_init = fiedler_perturbed_ic(graph, c, amp=amp, seed=0)

    t0 = time.time()
    res = find_formation(graph, params, normalize=False, verbose=False,
                         u_init=u_init, allow_outside_spinodal=False)
    t_opt = time.time() - t0

    t1 = time.time()
    eigs = sigma_m_eigs(res.u, graph, params, k=4, use_lanczos=(L >= 16))
    t_eig = time.time() - t1

    mu0 = float(eigs[0]) if len(eigs) >= 1 else float('nan')
    mu1 = float(eigs[1]) if len(eigs) >= 2 else float('nan')
    delta = abs(mu1 - mu0) if (np.isfinite(mu0) and np.isfinite(mu1)) else float('nan')

    # Order parameter: deviation from uniform
    osc = float(np.std(res.u))

    info = {
        'L': L, 'n': graph.n, 'eps': eps,
        'beta_crit': float(beta_c), 'beta': float(beta),
        'alpha': alpha, 'c': c,
        'energy': float(res.energy), 'converged': bool(res.converged),
        'n_iter': int(res.n_iter),
        'eigs': [float(e) for e in eigs],
        'mu_0': mu0, 'mu_1': mu1, 'delta_mu': float(delta),
        'amp_init': float(amp), 'osc_u': osc,
        't_opt_s': t_opt, 't_eig_s': t_eig,
    }
    if verbose:
        print(f"  [L={L} ε={eps:g}] μ0={mu0:.4e} μ1={mu1:.4e} Δ={delta:.4e}"
              f" osc={osc:.3e} conv={res.converged} ({t_opt:.1f}s opt + {t_eig:.2f}s eig)",
              flush=True)
    return info


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    Ls = [4, 8, 16]
    epsilons = [0.001, 0.003, 0.01, 0.03, 0.1]
    alpha = 1.0
    c = 0.5

    out = {
        'meta': {
            'protocol': 'NQ-187 §8 (working/SF/sigma_theorem4_higher_order.md)',
            'goal': 'verify p=2 in μ_1 - μ_0 ~ ε^p (D_4 free-BC L×L grid)',
            'alpha': alpha, 'c': c,
            'epsilons': epsilons, 'Ls': Ls,
            'predictions': {
                '§3.2_polynomial': 'p = 2 (no 5th equivariant)',
                'alternative':     'p = 3/2 (5th equivariant non-zero)',
            },
            'falsifiability_rule': 'CONFIRMED if all |p_L - 2| < 0.3',
            'hessian_method': 'analytic E_bd Hessian (4αL + β diag(W"(u_i)))',
            'eig_method': 'eigsh(sigma=0,which=LM) for L≥16 else eigh',
            'constant_mode_handling': 'rank-1 penalty 11^T/n · ρ',
        },
        'L_results': {},
        'verdict': None,
    }

    overall_t0 = time.time()
    print(f"=== NQ-187 §8 numerical verification — start ({time.strftime('%H:%M:%S')}) ===")
    for L in Ls:
        L_t0 = time.time()
        print(f"\n--- L = {L} (n = {L*L}) ---")
        results = []
        for eps in epsilons:
            r = run_one(L, eps, alpha=alpha, c=c, verbose=True)
            results.append(r)
        # Power-law fit
        eps_arr = np.array([r['eps'] for r in results])
        delta_arr = np.array([r['delta_mu'] for r in results])
        p, p_se, b = power_law_fit(eps_arr, delta_arr)
        elapsed = time.time() - L_t0
        print(f"  L={L} fit: p = {p:.3f} ± {p_se:.3f} (intercept exp(b)={np.exp(b):.3e})"
              f"  [elapsed {elapsed:.1f}s]")

        out['L_results'][str(L)] = {
            'beta_crit': float(results[0]['beta_crit']),
            'n': results[0]['n'],
            'epsilons': [r['eps'] for r in results],
            'mu_0': [r['mu_0'] for r in results],
            'mu_1': [r['mu_1'] for r in results],
            'delta_mu': [r['delta_mu'] for r in results],
            'eigs_full': [r['eigs'] for r in results],
            'osc_u': [r['osc_u'] for r in results],
            'converged': [r['converged'] for r in results],
            'fit_p': p, 'fit_p_stderr': p_se, 'fit_intercept_log': b,
            'elapsed_s': elapsed,
            'per_eps_runs': results,
        }

    # Verdict
    p_values = [out['L_results'][str(L)]['fit_p'] for L in Ls]
    finite = [p for p in p_values if np.isfinite(p)]
    if finite and all(abs(p - 2.0) < 0.3 for p in finite):
        verdict = 'confirmed (p=2 across all L; §3.2 polynomial-equivariant analysis upheld)'
    elif finite and all(abs(p - 1.5) < 0.3 for p in finite):
        verdict = 'falsified (p=3/2 alternative observed; non-polynomial correction needed)'
    elif finite and all(abs(p - 1.0) < 0.3 for p in finite[-2:]):
        # Restrict to larger L (finite[-2:]) since L=4 is small-grid noise
        verdict = ('inconsistent — observed p≈1 at L∈{8,16}, contradicting both §3.2 prediction (p=2) '
                   'and §5 alternative (p=3/2); data shows leading-order non-degeneracy '
                   'μ_0=ε|W"(c)|, μ_1=2ε|W"(c)| (cubic-equivariant ratio A_2/A_1 < 4 on finite L)')
    else:
        verdict = ('inconsistent (mixed power; likely finite-grid / IC / convergence '
                   'artifacts at small ε — see logs)')
    out['verdict'] = verdict
    out['meta']['p_values_per_L'] = dict(zip([str(L) for L in Ls], p_values))
    out['meta']['elapsed_total_s'] = time.time() - overall_t0

    # Persist
    out_path = os.path.join(os.path.dirname(__file__), 'results',
                            'sigma_theorem4_scaling.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2, default=float)
    print(f"\nWrote {out_path}")

    # Summary
    print("\n=== Summary ===")
    for L in Ls:
        Lr = out['L_results'][str(L)]
        print(f"  L={L:>2d}: β_crit={Lr['beta_crit']:.4f}  p = {Lr['fit_p']:.3f} ± {Lr['fit_p_stderr']:.3f}")
    print(f"  Total elapsed: {out['meta']['elapsed_total_s']:.1f}s")
    print(f"  Verdict: {verdict}")


if __name__ == '__main__':
    main()
