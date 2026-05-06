"""Energy functionals for stereo-SCC framework.

Implements the Ginzburg-Landau / Allen-Cahn energy on graphs:
  E[u; P] = alpha * u^T L u + beta * sum_x W(u(x))
where W(u) = u^2(1-u)^2 is the double-well potential.

This is the simplified single-field version of E_SCC for toy experiments.
The full E_SCC = lambda_cl E_cl + lambda_sep E_sep + lambda_bd E_bd + lambda_tr E_tr
is in scc/energy.py. Use this module for stereo barrier calculations only.

See: stereo_scc_canonical_memo_v1.1.md §T3, §T5
"""
from __future__ import annotations

import numpy as np
import scipy.sparse as sp
import scipy.optimize as opt


def double_well(u: np.ndarray) -> np.ndarray:
    """W(u) = u^2 (1-u)^2."""
    return u ** 2 * (1.0 - u) ** 2


def double_well_deriv(u: np.ndarray) -> np.ndarray:
    """W'(u) = 2u(1-u)(1-2u)."""
    return 2.0 * u * (1.0 - u) * (1.0 - 2.0 * u)


def ginzburg_landau_energy(
    u: np.ndarray,
    L: sp.spmatrix,
    alpha: float = 1.0,
    beta: float = 4.0,
) -> float:
    """Ginzburg-Landau energy: E[u] = alpha * u^T L u + beta * sum W(u).

    This is the toy single-field energy combining boundary smoothness
    and phase separation. In full SCC this corresponds to E_bd + E_sep.

    Args:
        u: Field values, shape (n,)
        L: Graph Laplacian, sparse (n, n)
        alpha: Smoothness coefficient (boundary weight)
        beta: Double-well coefficient (phase separation weight)

    Returns:
        energy: Scalar energy value
    """
    Lu = np.asarray(L @ u).ravel()
    smoothness = alpha * float(u @ Lu)
    well = beta * double_well(u).sum()
    return smoothness + well


def energy_gradient(
    u: np.ndarray,
    L: sp.spmatrix,
    alpha: float = 1.0,
    beta: float = 4.0,
) -> np.ndarray:
    """Gradient of Ginzburg-Landau energy w.r.t. u.

    grad E = 2*alpha*L*u + beta*W'(u)

    Note: for E_bd = 2*alpha*u^T L u (ordered pair convention),
    gradient = 4*alpha*L*u. Here we use the simpler u^T L u form.

    Args:
        u: Field values, shape (n,)
        L: Graph Laplacian
        alpha, beta: Energy coefficients

    Returns:
        grad: Gradient array, shape (n,)
    """
    Lu = np.asarray(L @ u).ravel()
    return 2.0 * alpha * Lu + beta * double_well_deriv(u)


def find_local_minimum(
    u0: np.ndarray,
    L: sp.spmatrix,
    alpha: float = 1.0,
    beta: float = 4.0,
    M: float | None = None,
    max_iter: int = 2000,
    step: float = 0.01,
) -> np.ndarray:
    """Projected gradient descent on the mass simplex.

    Minimizes ginzburg_landau_energy starting from u0 subject to
    sum(u) = M (if provided) and u in [0, 1]^n.

    Args:
        u0: Initial field, shape (n,)
        L: Laplacian
        alpha, beta: Energy parameters
        M: Target mass (if None, unconstrained)
        max_iter: Maximum iterations
        step: Gradient step size

    Returns:
        u_min: Local minimum (or best found)
    """
    u = u0.copy()
    M_target = u.sum() if M is None else M

    for _ in range(max_iter):
        g = energy_gradient(u, L, alpha, beta)
        # Project gradient onto mass-constraint hyperplane
        g_proj = g - g.mean()
        u_new = np.clip(u - step * g_proj, 0.0, 1.0)
        # Re-enforce mass constraint
        deficit = M_target - u_new.sum()
        u_new = u_new + deficit / len(u_new)
        u_new = np.clip(u_new, 0.0, 1.0)
        if np.linalg.norm(u_new - u) < 1e-8:
            break
        u = u_new
    return u


def merger_barrier_estimate(
    u_K: np.ndarray,
    L: sp.spmatrix,
    alpha: float = 1.0,
    beta: float = 4.0,
    n_interpolate: int = 50,
) -> float:
    """Estimate merger barrier by linear interpolation through field space.

    Approximates the barrier Delta_E = max_{t in [0,1]} E[u(t)] - E[u_K]
    along the straight-line path u(t) = (1-t)*u_K + t*u_merged,
    where u_merged is the uniform mass-normalized field (one formation).

    This is a toy barrier estimate; the true saddle-point barrier requires
    a proper minimum energy path (NEB/string method).

    Args:
        u_K: K-formation field (local minimum), shape (n,)
        L: Graph Laplacian
        alpha, beta: Energy coefficients
        n_interpolate: Number of interpolation steps

    Returns:
        barrier: Max energy along path minus starting energy
    """
    M = u_K.sum()
    u_uniform = np.full(len(u_K), M / len(u_K))

    E_start = ginzburg_landau_energy(u_K, L, alpha, beta)
    energies = []
    for t in np.linspace(0, 1, n_interpolate):
        u_t = (1.0 - t) * u_K + t * u_uniform
        energies.append(ginzburg_landau_energy(u_t, L, alpha, beta))

    return max(energies) - E_start


def stereo_barrier_comparison(
    adj_no_depth: sp.spmatrix,
    adj_with_depth: sp.spmatrix,
    u_K: np.ndarray,
    alpha: float = 1.0,
    beta: float = 4.0,
) -> dict[str, float]:
    """Compare merger barriers with and without depth-filtered adjacency.

    Demonstrates Claim T5 (Canonical Memo v1.1): stereo geometry raises
    merger barriers by removing depth-discontinuity edges.

    Args:
        adj_no_depth: Adjacency without depth filtering (flat 2D)
        adj_with_depth: Depth-filtered adjacency (stereo P-conditioned)
        u_K: K-formation field to use as starting point
        alpha, beta: Energy parameters

    Returns:
        dict with 'barrier_flat', 'barrier_stereo', 'ratio'
    """
    from stereo_scc.fields import laplacian_from_adj

    L_flat = laplacian_from_adj(adj_no_depth)
    L_stereo = laplacian_from_adj(adj_with_depth)

    barrier_flat = merger_barrier_estimate(u_K, L_flat, alpha, beta)
    barrier_stereo = merger_barrier_estimate(u_K, L_stereo, alpha, beta)

    ratio = barrier_stereo / max(barrier_flat, 1e-12)
    return {
        "barrier_flat": barrier_flat,
        "barrier_stereo": barrier_stereo,
        "ratio": ratio,
    }
