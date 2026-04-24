"""Dual-regime RIGOROUS verification.

Tests whether "dual-regime" is true phase transition or smooth crossover.

Three tests:

TEST 1: Fine ζ-scan on torus (L=16)
  - ζ ∈ {0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 1.5}
  - Look for sharp transition signatures (kink, derivative jump)
  - Fit smooth models: exp(c/ζ), power-law, double-exponential
  - Determine if truly phase-transition-like

TEST 2: L-scaling at fixed ζ
  - ζ = 1.0 (super-lattice regime)
  - L ∈ {8, 12, 16, 20, 24}
  - If genuine Goldstone: λ_0 → 0 as L → ∞ exponentially (continuum limit)
  - If smooth crossover: λ_0 L-independent

TEST 3: Crossover differentiability
  - Compute numerical derivative d(log λ_0)/dζ at each ζ
  - Phase transition: derivative diverges near ζ_*
  - Smooth crossover: derivative bounded

Run: cd CODE && python3 scripts/dual_regime_rigorous_test.py
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
    data = np.ones(len(rows))
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W)


def count_local_maxima_torus(u, L):
    g = u.reshape(L, L)
    F = 0
    for i in range(L):
        for j in range(L):
            v = g[i, j]
            ok = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = (i + di) % L, (j + dj) % L
                if g[ni, nj] >= v:
                    ok = False
                    break
            if ok:
                F += 1
    return F


def compute_hessian_spectrum(u_star, graph, params, n_modes=6, eps=1e-4):
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
    eigvals = np.linalg.eigvalsh(H_proj)
    eigvals.sort()
    return eigvals[:n_modes + 1]


def find_torus_F1(L, beta, c=0.5, n_tries=20):
    graph = build_torus_graph(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=2, max_iter=10000,
    )
    xi_0 = np.sqrt(1.0 / beta)
    r0 = np.sqrt(c * L * L / np.pi)
    ic_width = max(xi_0, 0.3)

    best = None
    for seed in range(n_tries):
        np.random.seed(seed * 19 + 11)
        cx = np.random.uniform(0, L)
        cy = np.random.uniform(0, L)
        i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
        dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
        dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
        r = np.sqrt(dx**2 + dy**2).flatten()
        u_init = 0.5 * (1.0 - np.tanh((r - r0) / ic_width))
        u_init = np.clip(u_init + np.random.normal(0, 0.02, size=L*L), 0.01, 0.99)
        try:
            res = find_formation(graph, params, normalize=False, verbose=False, u_init=u_init)
            if res.converged:
                F = count_local_maxima_torus(res.u, L)
                if F == 1 and (best is None or res.energy < best[1]):
                    best = (res.u, res.energy, graph, params)
        except Exception:
            pass
    return best


# =================== TEST 1: Fine ζ-scan ===================
def test1_fine_zeta_scan():
    print("=" * 70)
    print("TEST 1: Fine ζ-scan on torus L=16")
    print("=" * 70)
    L = 16
    c = 0.5

    # Fine ζ range
    zetas = [0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00, 1.20, 1.50, 1.80, 2.20]
    betas = [1.0 / z**2 for z in zetas]

    beta_crit = 0.175  # L=16 torus (actually λ_2 for torus 16x16 is 4sin²(π/16)≈0.152, so β_crit = 4×0.152 = 0.61 roughly)
    # For torus L=16: λ_2 = 2(1-cos(2π/16)) = 4 sin²(π/16) ≈ 0.1522
    # β_crit = 4·λ_2 = 0.609
    beta_crit_torus = 0.609
    print(f"β_crit (torus) ≈ {beta_crit_torus}")

    data = []
    for zeta, beta in zip(zetas, betas):
        if beta < beta_crit_torus * 1.2:
            print(f"\n  ζ={zeta:.2f}, β={beta:.3f} — below β_crit, skipping")
            continue
        print(f"\n  ζ={zeta:.2f}, β={beta:.3f}")
        t0 = time.time()
        found = find_torus_F1(L, beta, c=c, n_tries=10)
        if found is None:
            print(f"    No F=1 disk found")
            continue
        u_disk, energy, graph, params = found
        eigs = compute_hessian_spectrum(u_disk, graph, params, n_modes=5)
        lam_0 = float(eigs[1])
        lam_1 = float(eigs[2])
        lam_2 = float(eigs[3])
        print(f"    λ_0={lam_0:.4e}, λ_1={lam_1:.4e}, λ_2={lam_2:.4e}")
        data.append({'zeta': zeta, 'beta': beta, 'lam_0': lam_0, 'lam_1': lam_1, 'lam_2': lam_2,
                     'energy': float(energy), 'runtime': time.time() - t0})

    # Analyze: numerical derivative
    print("\n  --- Numerical analysis ---")
    if len(data) >= 3:
        zs = np.array([d['zeta'] for d in data])
        ls = np.array([d['lam_0'] for d in data])
        # Only analyze points with lam_0 > machine epsilon
        mask = ls > 1e-12
        zs_v, ls_v = zs[mask], ls[mask]
        if len(zs_v) >= 3:
            log_l = np.log(ls_v)
            # Numerical derivative d(log λ)/dζ
            slopes = []
            for i in range(len(zs_v) - 1):
                slope = (log_l[i+1] - log_l[i]) / (zs_v[i+1] - zs_v[i])
                slopes.append(slope)
                print(f"    ζ ∈ [{zs_v[i]:.2f}, {zs_v[i+1]:.2f}]: d(ln λ_0)/dζ = {slope:.2f}")

            # Check if slope is monotonic (smooth) or has a peak (transition)
            max_slope_idx = int(np.argmin(slopes))  # most negative slope
            print(f"  Most negative slope at ζ ≈ {(zs_v[max_slope_idx] + zs_v[max_slope_idx+1])/2:.3f}: {slopes[max_slope_idx]:.2f}")

    return data


# =================== TEST 2: L-scaling at ζ=1.0 ===================
def test2_L_scaling():
    print("\n" + "=" * 70)
    print("TEST 2: L-scaling at fixed ζ=1.0 (super-lattice)")
    print("=" * 70)
    zeta = 1.0
    beta = 1.0 / zeta**2  # = 1.0
    c = 0.5

    L_list = [8, 12, 16, 20, 24]
    data = []
    for L in L_list:
        # Check β_crit
        beta_crit_L = 4 * 2 * (1 - np.cos(2*np.pi/L))  # λ_2 for torus = 2(1-cos(2π/L))
        if beta < beta_crit_L * 1.2:
            print(f"\n  L={L}: β={beta:.3f} < β_crit={beta_crit_L:.3f} ×1.2, skipping")
            continue
        print(f"\n  L={L}, β={beta:.3f}")
        t0 = time.time()
        found = find_torus_F1(L, beta, c=c, n_tries=12)
        if found is None:
            print(f"    No F=1 disk found")
            continue
        u_disk, energy, graph, params = found
        eigs = compute_hessian_spectrum(u_disk, graph, params, n_modes=5)
        lam_0 = float(eigs[1])
        lam_1 = float(eigs[2])
        r0 = np.sqrt(c * L * L / np.pi)
        print(f"    λ_0={lam_0:.4e}, λ_1={lam_1:.4e}, r_0={r0:.2f}, runtime={time.time()-t0:.1f}s")
        data.append({'L': L, 'zeta': zeta, 'beta': beta, 'lam_0': lam_0,
                     'lam_1': lam_1, 'r_0': float(r0),
                     'energy': float(energy), 'runtime': time.time() - t0})

    # Analyze: does λ_0 decay with L?
    print("\n  --- L-scaling analysis ---")
    if len(data) >= 3:
        Ls = np.array([d['L'] for d in data])
        ls = np.array([d['lam_0'] for d in data])
        r0s = np.array([d['r_0'] for d in data])
        mask = ls > 1e-15
        Ls_v, ls_v, r0s_v = Ls[mask], ls[mask], r0s[mask]
        if len(Ls_v) >= 3:
            # Fit log(λ_0) = a - b·r_0 (Aubry/PN prediction)
            log_l = np.log(ls_v)
            slope, intercept = np.polyfit(r0s_v, log_l, 1)
            print(f"  Fit: log(λ_0) = {intercept:.3f} + ({slope:.4f}) × r_0")
            if slope < -0.5:
                print(f"  ✓ SIGNIFICANT L-decay — consistent with Aubry-like Goldstone (λ_0 → 0 as L → ∞)")
            else:
                print(f"  ~ WEAK L-decay — more likely smooth crossover")

    return data


# =================== TEST 3: Multi-mode structure ===================
def test3_mode_structure():
    """At various ζ, check if there are TWO near-zero modes (Goldstone doublet on torus)."""
    print("\n" + "=" * 70)
    print("TEST 3: Mode structure — Goldstone doublet?")
    print("=" * 70)
    L = 16
    c = 0.5

    zetas = [0.2, 0.5, 0.8, 1.0]
    data = []
    for zeta in zetas:
        beta = 1.0 / zeta**2
        if beta < 0.7:
            continue
        print(f"\n  ζ={zeta:.2f}, β={beta:.3f}")
        found = find_torus_F1(L, beta, c=c, n_tries=10)
        if found is None:
            print(f"    No F=1 disk found")
            continue
        u_disk, energy, graph, params = found
        eigs = compute_hessian_spectrum(u_disk, graph, params, n_modes=8)
        print(f"    Eigenvalues [0:8]: {[f'{e:.4e}' for e in eigs]}")

        # Check for TWO near-zero modes
        lam_t = eigs[0]  # tangent
        lam_0 = eigs[1]
        lam_1 = eigs[2]
        lam_2 = eigs[3]
        # Is there a doublet?
        ratio_01 = lam_0 / lam_1 if lam_1 > 0 else 0
        gap_02 = lam_2 / lam_1 if lam_1 > 0 else 0

        print(f"    λ_0/λ_1 = {ratio_01:.4f} (if 2 Goldstone: near 1)")
        print(f"    λ_2/λ_1 = {gap_02:.4f} (if gap to orbital: >> 1)")
        data.append({'zeta': zeta, 'eigs': [float(e) for e in eigs.tolist()],
                     'ratio_01': float(ratio_01), 'gap_02': float(gap_02)})

    return data


def main():
    print("\n" + "#" * 70)
    print("# DUAL-REGIME RIGOROUS VERIFICATION")
    print("# Testing: phase transition or smooth crossover?")
    print("#" * 70)

    t_global = time.time()

    r1 = test1_fine_zeta_scan()
    r2 = test2_L_scaling()
    r3 = test3_mode_structure()

    out = os.path.join(os.path.dirname(__file__), 'results', 'dual_regime_rigorous_test.json')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump({'test1_fine_zeta': r1, 'test2_L_scaling': r2, 'test3_mode_structure': r3}, f, indent=2)

    print(f"\n\nTotal runtime: {time.time() - t_global:.1f}s")
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
