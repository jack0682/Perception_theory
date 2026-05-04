"""
TEMPORARY DRAFT - gamma-path-prover (W6 D1 dispatch, 2026-05-04)
================================================================

Purpose
-------
Compute the Sigma_m-projected Hessian of E_bd at (a) the uniform u = c*1 and
(b) the post-pitchfork minimizer u*_eps on the L=4 D_4 free-BC grid,
under each of the three Hessian conventions:

  I.  Centered     : H_c = grad^2 E(u) - mu(u) * I
  II. Lagrange-P   : H_L = P_T grad^2 E(u) P_T,   P_T = I - (1/n) 11^T
  III. Reduced     : H_r = B^T grad^2 E(u) B,     B = ortho basis of T_u Sigma_m

Then extract mu_0, mu_1 (the two smallest eigenvalues on the n-1 dim tangent
subspace) under each convention, and compute the implied effective ratio
A_2/A_1 via canonical formula:
        mu_0 = 4 |W''(c)| eps           => effective coefficient k_0
        mu_1 = (A_2/A_1) |W''(c)| eps   => effective ratio = mu_1/k_0 * 4
                                          = 4 * (mu_1 / mu_0_canonical)

We instead report the dimensionless coefficients
        c_0 := mu_0 / (eps |W''(c)|),   c_1 := mu_1 / (eps |W''(c)|),
and the ratio c_1/c_0.

If the canonical normal-form derivation (R22 sec 3.3) holds verbatim:
    c_0 = 4   c_1 = 4   c_1/c_0 = 1   implied A_2/A_1 = 4 (degenerate)
NQ-187 numerical observation:
    c_0 ~ 1   c_1 ~ 2   c_1/c_0 = 2   implied A_2/A_1 = 4*(c_1/4)/(c_0/4)*...
                                                       = 8 (per Wave 3 reasoning)

System: E_bd(u) = 2 alpha u^T L u + beta sum_i W(u_i)
        W(u) = u^2(1-u)^2,   W''(c=1/2) = -1
        beta_crit = 4 alpha lambda_2 / |W''(c)|
        beta = beta_crit + eps,  alpha = 1, c = 0.5

Hessian (full ambient): H = 4 alpha L_G + beta diag(W''(u_i))
Note: this is the SAME analytic Hessian used by the NQ-187 script
      (test_sigma_theorem4_scaling.py:hessian_bd_analytic).

Output: tabulated mu_0, mu_1, ratio, implied A_2/A_1 per convention.
"""
from __future__ import annotations

import os
import sys
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

# scc package via sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import double_well_second_deriv
from scc.optimizer import find_formation


def hessian_full(u: np.ndarray, graph: GraphState, alpha: float, beta: float) -> np.ndarray:
    """Ambient (n x n) Hessian of E_bd at u: H = 4 alpha L_G + beta diag(W''(u))."""
    n = u.shape[0]
    L = graph.L.toarray() if sp.issparse(graph.L) else np.asarray(graph.L)
    W_pp = 2.0 * (1.0 - 6.0 * u + 6.0 * u * u)  # W''(u_i) elementwise
    return 4.0 * alpha * L + beta * np.diag(W_pp)


def lagrange_multiplier(u: np.ndarray, graph: GraphState, alpha: float, beta: float) -> float:
    """The Lagrange multiplier mu(u) for the volume constraint sum u_i = m,
    defined by KKT stationarity:
            grad E(u) = mu(u) * 1
    With grad E(u) = 4 alpha L u + beta * 2 u (1-u)(1-2u),
    the projected stationarity gives mu(u) = (1/n) 1^T grad E(u).
    """
    Lu_obj = graph.L @ u
    Lu = np.asarray(Lu_obj).ravel()
    Wp = 2.0 * u * (1.0 - u) * (1.0 - 2.0 * u)
    grad = 4.0 * alpha * Lu + beta * Wp
    return float(np.mean(grad))


def hessian_centered(u, graph, alpha, beta):
    """Convention I: H_c = grad^2 E(u) - mu(u) * I."""
    H = hessian_full(u, graph, alpha, beta)
    mu = lagrange_multiplier(u, graph, alpha, beta)
    return H - mu * np.eye(H.shape[0])


def hessian_lagrange_projected(u, graph, alpha, beta):
    """Convention II: H_L = P_T H P_T, P_T = I - (1/n) 11^T."""
    H = hessian_full(u, graph, alpha, beta)
    n = H.shape[0]
    one = np.ones(n)
    P = np.eye(n) - np.outer(one, one) / n
    return P @ H @ P


def hessian_reduced(u, graph, alpha, beta):
    """Convention III: H_r = B^T H B, B = orthonormal basis of T_u Sigma_m.

    T_u Sigma_m = {v : 1^T v = 0} is the (n-1)-dim subspace orthogonal to 1.
    Build B from QR of any matrix whose columns span this subspace.
    Equivalent (up to choice of basis) to the nontrivial spectrum of H_L.
    """
    H = hessian_full(u, graph, alpha, beta)
    n = H.shape[0]
    # Construct orthonormal basis of T = (1)^perp
    # via QR on (I - 11^T/n), keeping the n-1 nonzero columns
    one = np.ones((n, 1))
    P = np.eye(n) - one @ one.T / n
    Q, _ = np.linalg.qr(P)
    # Q has columns spanning T plus one zero column at the end; pick n-1 vecs
    # whose images under P are nonzero; cleanest: use eigvecs of P with
    # eigenvalue 1 (drop the eigenvalue-0 constant direction)
    w, V = np.linalg.eigh(P)
    # Keep eigenvectors with eigenvalue close to 1
    keep = np.abs(w - 1.0) < 1e-6
    B = V[:, keep]
    assert B.shape[1] == n - 1, f"basis has {B.shape[1]} cols, expected {n-1}"
    return B.T @ H @ B


# ---------------------------------------------------------------------------
# Eigenvalue extraction on T_u Sigma_m
# ---------------------------------------------------------------------------

def bottom_two_on_tangent(H_conv: np.ndarray, conv_name: str) -> tuple[float, float]:
    """Return the two smallest eigenvalues on T_u Sigma_m.

    For Conventions I and II, the operator acts on R^n; the constant direction
    1 may carry a non-physical eigenvalue. Strategy:
      - Compute all eigenvalues of H_conv as a dense symmetric matrix.
      - Identify and DROP the eigenvector closest to the constant 1/sqrt(n).
      - Return the two smallest remaining.
    For Convention III, H_r is already (n-1) x (n-1) on T; just return bottom-2.
    """
    H = (H_conv + H_conv.T) / 2.0
    w, V = np.linalg.eigh(H)
    n = H.shape[0]
    if conv_name == 'reduced':
        idx = np.argsort(w)
        return float(w[idx[0]]), float(w[idx[1]])
    # Identify the eigenvector closest to 1/sqrt(n)
    ones = np.ones(n) / np.sqrt(n)
    overlaps = np.abs(V.T @ ones)
    const_idx = int(np.argmax(overlaps))
    # Mask it out
    mask = np.ones(n, dtype=bool)
    mask[const_idx] = False
    w_phys = w[mask]
    idx = np.argsort(w_phys)
    return float(w_phys[idx[0]]), float(w_phys[idx[1]])


# ---------------------------------------------------------------------------
# Main: run on L=4 D_4 free-BC grid
# ---------------------------------------------------------------------------

def make_uniform(n: int, c: float = 0.5) -> np.ndarray:
    return np.full(n, c)


def find_post_pitchfork_minimizer(graph: GraphState, alpha: float, beta: float, c: float = 0.5,
                                   amp: float = 0.30, seed: int = 0):
    """Run the same find_formation as the NQ-187 script to land on u*_eps."""
    n = graph.n
    v2 = graph.fiedler_vector()
    v2 = v2 - np.mean(v2)
    if abs(v2.min()) > abs(v2.max()):
        v2 = -v2
    mxv = np.max(np.abs(v2))
    if mxv > 1e-12:
        v2 = v2 / mxv
    rng = np.random.default_rng(seed)
    noise = 1e-6 * rng.standard_normal(n)
    noise -= noise.mean()
    u_init = np.full(n, c) + amp * v2 + noise
    u_init = np.clip(u_init, 1e-6, 1.0 - 1e-6)

    params = ParameterRegistry(
        alpha_bd=alpha, beta_bd=beta, volume_fraction=c,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=50000,
        eps_grad=1e-10, eps_field=1e-12, eps_energy=1e-15,
        eps_init=0.01, dt_init=0.01,
    )
    res = find_formation(graph, params, normalize=False, verbose=False,
                         u_init=u_init, allow_outside_spinodal=False)
    return res.u, params


def report_one(label, u, graph, alpha, beta, eps, Wpp_abs):
    """Compute & print mu_0, mu_1 under each convention at u."""
    print(f"\n=== {label} (eps = {eps:g}) ===")
    print(f"  L_G fiedler = {graph.fiedler:.6f}")
    print(f"  beta = {beta:.6f}")
    print(f"  Lagrange mu(u) = {lagrange_multiplier(u, graph, alpha, beta):.6e}")

    rows = []
    for conv_name, builder in [('centered', hessian_centered),
                                ('lagrange', hessian_lagrange_projected),
                                ('reduced', hessian_reduced)]:
        Hc = builder(u, graph, alpha, beta)
        m0, m1 = bottom_two_on_tangent(Hc, conv_name)
        c0 = m0 / (eps * Wpp_abs) if eps > 0 else float('nan')
        c1 = m1 / (eps * Wpp_abs) if eps > 0 else float('nan')
        ratio = m1 / m0 if abs(m0) > 1e-12 else float('nan')
        # Implied A_2/A_1 under canonical formula mu_0 = 4|W''(c)|eps,
        # mu_1 = (A_2/A_1) |W''(c)| eps
        # If we BELIEVE mu_0 = 4|W''(c)|eps (so c_0 should equal 4):
        #   implied A_2/A_1 = c_1
        # If we instead use the OBSERVED c_0 to define normalization:
        #   implied A_2/A_1 = 4 * c_1/c_0
        implied_canonical = c1                # interpret c_1 directly
        implied_observed  = 4.0 * c1 / c0 if abs(c0) > 1e-9 else float('nan')
        rows.append((conv_name, m0, m1, ratio, c0, c1, implied_canonical, implied_observed))
        print(f"  [{conv_name:>8s}] mu0 = {m0:+.6e}  mu1 = {m1:+.6e}"
              f"  c0 = {c0:+.4f}  c1 = {c1:+.4f}  c1/c0 = {ratio:+.4f}"
              f"  A2/A1[canon] = {implied_canonical:+.4f}"
              f"  A2/A1[obs] = {implied_observed:+.4f}")
    return rows


def main():
    L = 4
    alpha = 1.0
    c = 0.5
    Wpp = double_well_second_deriv(c)        # = -1
    Wpp_abs = abs(Wpp)

    graph = GraphState.grid_2d(L, L)
    n = graph.n
    lam2 = graph.fiedler
    beta_crit = 4.0 * alpha * lam2 / Wpp_abs

    print("="*78)
    print(f"L={L} D_4 free-BC grid (n={n}); alpha={alpha}, c={c}")
    print(f"|W''(c)| = {Wpp_abs}")
    print(f"lambda_2 (Fiedler) = {lam2:.6f}")
    print(f"beta_crit = 4 alpha lambda_2 / |W''(c)| = {beta_crit:.6f}")
    print("="*78)

    # ---- Run at multiple eps values, compute u*_eps via find_formation ----
    epsilons = [0.001, 0.01, 0.1]
    all_results = {'uniform': {}, 'post_pitchfork': {}}

    # Uniform reference (eps in label only, eigenvalues independent of eps for uniform u=c1
    # except via beta=beta_crit+eps -- which DOES enter H = 4aL + beta diag(W''(u)))
    for eps in epsilons:
        beta = beta_crit + eps
        u_unif = make_uniform(n, c)
        rows = report_one(f"u = c*1 (uniform)", u_unif, graph, alpha, beta, eps, Wpp_abs)
        all_results['uniform'][eps] = rows

    # Post-pitchfork
    for eps in epsilons:
        beta = beta_crit + eps
        u_star, _ = find_post_pitchfork_minimizer(graph, alpha, beta, c=c)
        rows = report_one(f"u = u*_eps (post-pitchfork minimizer)",
                           u_star, graph, alpha, beta, eps, Wpp_abs)
        all_results['post_pitchfork'][eps] = rows
        print(f"  ||u* - c1||_inf = {np.max(np.abs(u_star - c)):.4e}")

    # ----- Summary table at smallest eps -----
    eps_small = epsilons[0]
    print("\n" + "="*78)
    print(f"SUMMARY TABLE (at smallest eps = {eps_small})")
    print("="*78)
    print(f"\n--- AT u = c*1 (uniform, BEFORE pitchfork-broken state) ---")
    print(f"{'Convention':>10s} | {'mu_0':>14s} | {'mu_1':>14s} | {'mu_1/mu_0':>10s} |"
          f" {'c_0':>8s} | {'c_1':>8s} | {'A2/A1[canon]':>12s} | {'A2/A1[obs]':>12s}")
    for r in all_results['uniform'][eps_small]:
        print(f"{r[0]:>10s} | {r[1]:+.6e} | {r[2]:+.6e} | {r[3]:+10.4f} |"
              f" {r[4]:+8.4f} | {r[5]:+8.4f} | {r[6]:+12.4f} | {r[7]:+12.4f}")

    print(f"\n--- AT u = u*_eps (post-pitchfork minimizer) ---")
    print(f"{'Convention':>10s} | {'mu_0':>14s} | {'mu_1':>14s} | {'mu_1/mu_0':>10s} |"
          f" {'c_0':>8s} | {'c_1':>8s} | {'A2/A1[canon]':>12s} | {'A2/A1[obs]':>12s}")
    for r in all_results['post_pitchfork'][eps_small]:
        print(f"{r[0]:>10s} | {r[1]:+.6e} | {r[2]:+.6e} | {r[3]:+10.4f} |"
              f" {r[4]:+8.4f} | {r[5]:+8.4f} | {r[6]:+12.4f} | {r[7]:+12.4f}")

    # Cross-check: scale c_0 with eps to see leading order
    print(f"\n--- SCALING with eps (post-pitchfork, lagrange convention) ---")
    print(f"{'eps':>8s} | {'mu_0':>14s} | {'mu_1':>14s} | {'mu_1/eps':>10s} | {'mu_1/mu_0':>10s}")
    for eps in epsilons:
        r = all_results['post_pitchfork'][eps]
        # row [1] is lagrange
        lag = r[1]
        print(f"{eps:>8.4g} | {lag[1]:+.6e} | {lag[2]:+.6e} | {lag[2]/eps:+10.4f} | {lag[3]:+10.4f}")

    print("\n--- SCALING with eps (post-pitchfork, centered convention) ---")
    print(f"{'eps':>8s} | {'mu_0':>14s} | {'mu_1':>14s} | {'mu_1/eps':>10s} | {'mu_1/mu_0':>10s}")
    for eps in epsilons:
        r = all_results['post_pitchfork'][eps]
        cen = r[0]
        print(f"{eps:>8.4g} | {cen[1]:+.6e} | {cen[2]:+.6e} | {cen[2]/eps:+10.4f} | {cen[3]:+10.4f}")


def cross_check_nq187_penalty(graph, u, alpha, beta, rho_factor=1e3):
    """Replicate the EXACT eigenvalue extraction NQ-187 does (rank-1 penalty)."""
    n = graph.n
    H = hessian_full(u, graph, alpha, beta)
    one = np.ones(n)
    rho = rho_factor * max(1.0, abs(beta))
    H_pen = H + (rho / n) * np.outer(one, one)
    w = np.linalg.eigvalsh(H_pen)
    w = np.sort(w)
    physical = w[w < 0.5 * rho]
    return physical[0], physical[1]


def secondary_check():
    """Verify equivalence holds at L=8 (non-trivial size) and check NQ-187 matches."""
    print("\n\n" + "#"*78)
    print("# SECONDARY CHECK: L=8 D_4 grid + NQ-187 penalty replication")
    print("#"*78)
    L = 8
    alpha = 1.0
    c = 0.5
    Wpp_abs = abs(double_well_second_deriv(c))
    graph = GraphState.grid_2d(L, L)
    n = graph.n
    lam2 = graph.fiedler
    beta_crit = 4.0 * alpha * lam2 / Wpp_abs
    print(f"L={L}, n={n}, lambda_2={lam2:.6f}, beta_crit={beta_crit:.6f}")

    eps = 0.01
    beta = beta_crit + eps
    u_star, _ = find_post_pitchfork_minimizer(graph, alpha, beta, c=c)
    print(f"\nAt u*_eps (eps={eps}):")
    print(f"  ||u*-c1||_inf = {np.max(np.abs(u_star - c)):.4e}")
    print(f"  Lagrange mu(u*) = {lagrange_multiplier(u_star, graph, alpha, beta):.4e}")

    rows = []
    for conv_name, builder in [('centered', hessian_centered),
                                ('lagrange', hessian_lagrange_projected),
                                ('reduced', hessian_reduced)]:
        Hc = builder(u_star, graph, alpha, beta)
        m0, m1 = bottom_two_on_tangent(Hc, conv_name)
        rows.append((conv_name, m0, m1))
        print(f"  [{conv_name:>8s}] mu0 = {m0:+.6e}  mu1 = {m1:+.6e}  ratio = {m1/m0:.4f}")

    # NQ-187 penalty replication
    m0n, m1n = cross_check_nq187_penalty(graph, u_star, alpha, beta)
    print(f"  [NQ-187 pen] mu0 = {m0n:+.6e}  mu1 = {m1n:+.6e}  ratio = {m1n/m0n:.4f}")

    # ALSO verify equivalence numerically: max |mu_i^conv - mu_i^lagrange|
    print("\nMax pairwise eigenvalue discrepancy across conventions (should be ~1e-12):")
    base = rows[1]  # lagrange
    for r in rows:
        d0 = abs(r[1] - base[1])
        d1 = abs(r[2] - base[2])
        print(f"  [{r[0]:>8s}] |Δμ_0| = {d0:.2e}  |Δμ_1| = {d1:.2e}")


def algebraic_proof_note():
    """Print explanation of why all three conventions coincide on T_u Sigma_m."""
    print("\n\n" + "#"*78)
    print("# ALGEBRAIC NOTE — why all three conventions coincide on T_u Sigma_m")
    print("#"*78)
    print("""
Let H = grad^2 E(u) (full ambient n x n Hessian).
Let mu(u) = the Lagrange multiplier (a scalar).

  Conv I (Centered):     H_c = H - mu(u) * I.
  Conv II (Lagrange-P):  H_L = P_T H P_T,  P_T = I - (1/n) 1 1^T.
  Conv III (Reduced):    H_r = B^T H B,    B = ortho basis of T = (1)^perp.

For any v in T_u Sigma_m (i.e. 1^T v = 0):
  (H_c v) . v = v^T H v - mu * ||v||^2
  (H_L v) . v = v^T P_T H P_T v = v^T H v        (since P_T v = v on T)
  (H_r v) . v = (B v')^T H (B v') = v^T H v      (with v = B v')

So Conv II and Conv III give IDENTICAL eigenvalues on T (they are restrictions
of H to T). Conv I differs from Conv II by a UNIFORM SHIFT of -mu(u) on every
eigenvalue (including the constant-direction eigenvalue).

Hence:
  mu_k(I) = mu_k(II) - mu(u)   for all eigenvalues on T.

For Conv I to equal Conv II eigenvalue-by-eigenvalue, we need mu(u) = 0.

KEY OBSERVATION: at the SCC double-well with c = 1/2, the Hessian
H = 4 alpha L_G + beta diag(W''(u_i)) and the gradient
grad E(u) = 4 alpha L_G u + beta * 2 u (1-u)(1-2u).

At ANY critical point of E ON Sigma_m, KKT gives grad E = mu(u) * 1, so
mu(u) = (1/n) 1^T grad E.

  - At u = c * 1 (uniform with c = 1/2):  W'(c) = 2c(1-c)(1-2c) = 0,
    and L_G * 1 = 0, so grad E = 0. Hence mu(u) = 0 trivially.

  - At u = u*_eps (post-pitchfork min on Sigma_m):  by KKT, grad E = mu(u) * 1.
    Now 1^T grad E = 4 alpha (1^T L_G u) + beta * 2 sum_i u_i(1-u_i)(1-2u_i)
                   = 0  + beta * 2 sum_i u_i(1-u_i)(1-2u_i).
    The double-well derivative W'(u) = 2 u(1-u)(1-2u) is ANTISYMMETRIC about
    u = 1/2:   W'(1 - u) = -W'(u).
    The bifurcated minimizer u*_eps = c1 + a_eps * phi_(1,0) has u_i and 1-u_i
    pairing up across the (anti)symmetric structure of phi_(1,0) (cos(pi(i+1/2)/L)
    has paired +/- values about its mean), so sum W'(u_i) = 0. Hence mu(u*_eps) = 0.

==> mu(u) = 0 IDENTICALLY for both u = c1 and u = u*_eps at c = 1/2.
==> Conv I = Conv II = Conv III on T_u Sigma_m for THIS theorem's setting.

==> The gamma-path "Sigma_m-Hessian convention" hypothesis CANNOT EXPLAIN the
    factor-of-4 discrepancy between R22's continuum claim (A_2/A_1 = 4) and
    NQ-187's measured ratio (~2 from mu_1/mu_0 = 2 at L<=16).
    The discrepancy is NOT a convention artifact.
""")


if __name__ == '__main__':
    main()
    secondary_check()
    algebraic_proof_note()
