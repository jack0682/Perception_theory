"""Transport kernel computation for SCC temporal theory.

Implements entropy-regularized partial optimal transport via Sinkhorn
iteration in log-domain. The transport plan M_{t->s} satisfies the
sub-stochastic constraint (E1 axiom: row sums <= 1), allowing partial
dissipation of cohesion mass.

References: Canonical Spec §8.5, paper1 §6.
"""
from __future__ import annotations

import numpy as np
import scipy.sparse.csgraph as csgraph
from dataclasses import dataclass
from typing import List, Optional
from scipy.special import logsumexp

from scc.graph import GraphState
from scc.operators import closure, distinction, resolvent_diagonal
from scc.params import ParameterRegistry

_EPS = 1e-12  # numerical stability floor


# ---------------------------------------------------------------------------
# Entropic partial optimal transport (Sinkhorn, log-domain)
# ---------------------------------------------------------------------------

def sinkhorn_partial_ot(
    cost: np.ndarray,
    mu: np.ndarray,
    nu: np.ndarray,
    eps: float,
    mass_fraction: float = 1.0,
    max_iter: int = 100,
    tol: float = 1e-6,
) -> tuple[np.ndarray, dict]:
    """Entropy-regularized partial optimal transport via log-domain Sinkhorn.

    Computes a transport plan M*(x,y) = a(x) K(x,y) b(y) where
    K(x,y) = exp(-c(x,y)/eps), using dustbin rows/columns to absorb
    unmatched mass when mass_fraction < 1.

    Parameters
    ----------
    cost : (n, m) cost matrix c(x,y).
    mu : (n,) source marginal (cohesion field u_t).
    nu : (m,) target marginal (cohesion field u_s).
    eps : entropic regularization parameter eps_OT > 0.
    mass_fraction : fraction of total mass to transport (1.0 = balanced).
    max_iter : maximum Sinkhorn iterations.
    tol : convergence tolerance on marginal violation.

    Returns
    -------
    M : (n, m) transport plan satisfying sub-stochastic constraints.
    info : dict with 'iterations', 'converged', 'marginal_error'.

    References
    ----------
    Canonical Spec §8.5, paper1 §6.
    """
    cost = np.asarray(cost, dtype=np.float64)
    mu = np.asarray(mu, dtype=np.float64).ravel()
    nu = np.asarray(nu, dtype=np.float64).ravel()

    if np.any(np.isnan(cost)) or np.any(np.isnan(mu)) or np.any(np.isnan(nu)):
        raise ValueError("Input contains NaN")

    n, m = cost.shape
    assert mu.shape == (n,) and nu.shape == (m,)
    assert eps > 0, "Regularization eps must be positive"
    assert 0 < mass_fraction <= 1.0

    sum_mu = mu.sum()
    sum_nu = nu.sum()
    total_mass = mass_fraction * min(sum_mu, sum_nu)

    # Handle degenerate cases
    if total_mass < _EPS or sum_mu < _EPS or sum_nu < _EPS:
        return np.zeros((n, m)), {
            'iterations': 0, 'converged': True, 'marginal_error': 0.0
        }

    # Determine whether dustbin is needed.
    # Dustbin absorbs unmatched mass so that the real block is sub-stochastic.
    # When mass_fraction=1.0 and marginals have equal total mass, no dustbin
    # is needed (standard balanced Sinkhorn already gives row_sums = mu).
    source_slack = sum_mu - total_mass  # mass source can discard
    target_slack = sum_nu - total_mass  # mass target doesn't need to receive
    use_dustbin = (source_slack > _EPS) or (target_slack > _EPS)

    if use_dustbin:
        # Extended cost matrix with dustbin row/column (cost 0).
        cost_ext = np.zeros((n + 1, m + 1), dtype=np.float64)
        cost_ext[:n, :m] = cost

        # Dustbin target absorbs source slack, dustbin source absorbs target slack.
        mu_ext = np.empty(n + 1)
        mu_ext[:n] = mu
        mu_ext[n] = max(target_slack, _EPS)

        nu_ext = np.empty(m + 1)
        nu_ext[:m] = nu
        nu_ext[m] = max(source_slack, _EPS)

        log_K = -cost_ext / eps
        ne, me = n + 1, m + 1
    else:
        log_K = -cost / eps
        mu_ext = mu
        nu_ext = nu
        ne, me = n, m

    # Initialize log scaling vectors
    log_a = np.zeros(ne)
    log_b = np.zeros(me)

    log_mu = np.log(mu_ext + _EPS)
    log_nu = np.log(nu_ext + _EPS)

    converged = False
    marginal_error = np.inf
    iterations = 0

    for it in range(max_iter):
        log_a = log_mu - logsumexp(log_K + log_b[np.newaxis, :], axis=1)
        log_b = log_nu - logsumexp(log_K.T + log_a[np.newaxis, :], axis=1)

        iterations = it + 1

        # Check convergence every 5 iterations
        if iterations % 5 == 0 or it == max_iter - 1:
            log_M_full = log_a[:, np.newaxis] + log_K + log_b[np.newaxis, :]
            log_M_full = np.clip(log_M_full, -500, 500)
            M_full = np.exp(log_M_full)

            row_err = np.abs(M_full.sum(axis=1) - mu_ext).sum()
            col_err = np.abs(M_full.sum(axis=0) - nu_ext).sum()
            marginal_error = row_err + col_err

            if marginal_error < tol:
                converged = True
                break

    # Extract the real (non-dustbin) block of the plan.
    # Do NOT rescale: the extended Sinkhorn already targets the correct
    # total mass, and uniform rescaling would violate sub-stochasticity.
    log_M = log_a[:n, np.newaxis] + log_K[:n, :m] + log_b[np.newaxis, :m]
    log_M = np.clip(log_M, -500, 500)
    M = np.exp(log_M)

    # Clip tiny negatives from numerical noise
    np.clip(M, 0.0, None, out=M)

    info = {
        'iterations': iterations,
        'converged': converged,
        'marginal_error': float(marginal_error),
    }
    return M, info


# ---------------------------------------------------------------------------
# Transport field application
# ---------------------------------------------------------------------------

def transport_field(M: np.ndarray, u_s: np.ndarray) -> np.ndarray:
    """Apply transport plan to transport a cohesion field.

    Computes the transported field at source sites by normalizing
    the plan-weighted target field by the row mass.

    Parameters
    ----------
    M : (n, m) transport plan from sinkhorn_partial_ot.
    u_s : (m,) cohesion field at target time s.

    Returns
    -------
    u_transported : (n,) transported field values at source sites.
        u_transported(x) = sum_y M(x,y) u_s(y) / max(sum_y M(x,y), eps_safe)

    References
    ----------
    Canonical Spec §8.5.
    """
    M = np.asarray(M, dtype=np.float64)
    u_s = np.asarray(u_s, dtype=np.float64).ravel()

    numerator = M @ u_s
    row_sums = M.sum(axis=1)
    return numerator / np.maximum(row_sums, _EPS)


# ---------------------------------------------------------------------------
# Cohesion fingerprint and transport cost matrix
# ---------------------------------------------------------------------------

def cohesion_fingerprint(
    u: np.ndarray, graph: GraphState, params: ParameterRegistry
) -> np.ndarray:
    """Compute the cohesion fingerprint φ(x) ∈ [0,1]^4 at each site.

    φ(x) = (u(x), Cl(u)(x), D(x; 1-u), C(x,x))

    Components:
        φ₀ = u(x)        — raw cohesion value
        φ₁ = Cl(u)(x)    — self-completion (closure operator)
        φ₂ = D(x; 1-u)   — self-contrast (distinction operator)
        φ₃ = C(x,x)      — self-integration (resolvent diagonal, normalized)

    Parameters
    ----------
    u : np.ndarray, shape (n,)
        Cohesion field values in [0, 1].
    graph : GraphState
        Graph structure with adjacency and derived quantities.
    params : ParameterRegistry
        Operator parameters.

    Returns
    -------
    np.ndarray, shape (n, 4)
        Fingerprint vectors for all sites.

    References
    ----------
    Canonical Spec v2.0 §10 (temporal transport).
    """
    if np.any(np.isnan(u)):
        raise ValueError("Input field contains NaN")

    n = graph.n
    phi = np.empty((n, 4))

    phi[:, 0] = u
    phi[:, 1] = closure(u, graph, params)
    phi[:, 2] = distinction(u, graph, params)

    # Resolvent diagonal C(x,x) >= 1 (Neumann series starts at I).
    # Interaction-only normalization: (C(x,x) - 1) / C(x,x) maps [1, ∞) → [0, 1).
    # The identity contribution (1) is subtracted so only the co-belonging
    # interaction term remains, preserving relative differences: core sites
    # with high co-belonging have C(x,x) >> 1 → φ₃ ≈ 1, while exterior
    # sites with C(x,x) ≈ 1 → φ₃ ≈ 0. This gives meaningful discrimination
    # for the transport cost, unlike 1/C(x,x) which saturates near 1.0.
    c_diag = resolvent_diagonal(u, graph, params)
    phi[:, 3] = np.clip((c_diag - 1.0) / np.maximum(c_diag, _EPS), 0.0, 1.0)

    return phi


def graph_distance_matrix(graph: GraphState) -> np.ndarray:
    """Compute shortest-path distances between all pairs of sites.

    Uses BFS on the unweighted adjacency structure (treats all edges
    as unit weight).

    Parameters
    ----------
    graph : GraphState
        Graph structure with sparse adjacency matrix.

    Returns
    -------
    np.ndarray, shape (n, n)
        Pairwise shortest-path distances. Unreachable pairs (disconnected
        components) get np.inf. Callers should handle inf before squaring
        to avoid overflow; see transport_cost() which replaces inf with 1e6.
    """
    adj_binary = (graph.W > 0).astype(np.float64)
    dist = csgraph.shortest_path(adj_binary, method="D", directed=False)
    return dist


def transport_cost(
    phi_t: np.ndarray,
    phi_s: np.ndarray,
    dist_matrix: np.ndarray,
    sigma: float = 1.0,
    gamma: float = 1.0,
    other_fields_s: Optional[List[np.ndarray]] = None,
    lambda_rep: float = 0.0,
) -> np.ndarray:
    """Compute the self-referential transport cost matrix.

    c(x, y) = d_G(x, y)² / (2σ²) + γ · ‖φ_t(x) - φ_s(y)‖²
            + λ_rep · Σ_j u^j_s(y)   (repulsion term, if other_fields_s given)

    The cost combines spatial distance (graph geodesic) with fingerprint
    dissimilarity, making transport sensitive to the cohesion structure
    at both source and target. The optional repulsion term penalizes
    transporting mass to sites occupied by other formations.

    Parameters
    ----------
    phi_t : np.ndarray, shape (n, 4)
        Cohesion fingerprint at time t (source).
    phi_s : np.ndarray, shape (n, 4)
        Cohesion fingerprint at time s (target).
    dist_matrix : np.ndarray, shape (n, n)
        Pairwise graph distances.
    sigma : float
        Spatial tolerance parameter (default 1.0).
    gamma : float
        Fingerprint weight parameter (default 1.0).
    other_fields_s : list of np.ndarray, optional
        Other formations' fields at target time. When provided with
        lambda_rep > 0, adds repulsion cost at target sites.
    lambda_rep : float
        Repulsion weight for other-formation avoidance (default 0.0).

    Returns
    -------
    np.ndarray, shape (n, n)
        Transport cost matrix c(x, y).

    References
    ----------
    Canonical Spec v2.0 §10 (temporal transport).
    """
    if sigma <= 0:
        raise ValueError("sigma must be positive")

    # Spatial term: d_G(x,y)^2 / (2 * sigma^2)
    # Replace inf distances (disconnected components) with large finite value
    # to avoid inf**2 overflow warnings. exp(-1e6/eps) ≈ 0 in Sinkhorn anyway.
    dist_finite = np.where(np.isinf(dist_matrix), 1e6, dist_matrix)
    spatial = dist_finite ** 2 / (2.0 * sigma ** 2)

    # Fingerprint dissimilarity: gamma * ||phi_t(x) - phi_s(y)||^2
    diff = phi_t[:, np.newaxis, :] - phi_s[np.newaxis, :, :]
    fingerprint = gamma * np.sum(diff ** 2, axis=2)

    cost = spatial + fingerprint

    # Repulsion: penalize target sites occupied by other formations.
    # Scale by gamma (fingerprint weight) to keep repulsion cost comparable
    # to the fingerprint term, not the raw energy lambda_rep which can dominate.
    if other_fields_s is not None and lambda_rep > 0:
        n_s = phi_s.shape[0]
        rep_cost = np.zeros(n_s)
        for other_u in other_fields_s:
            rep_cost += other_u
        # Use gamma-scaled repulsion: gamma * lambda_rep_normalized * Σ u^j
        # where lambda_rep_normalized ensures the repulsion cost is O(1) like
        # the fingerprint term when other fields are ~1 at a site.
        rep_scale = gamma * min(lambda_rep, 1.0)
        cost += rep_scale * rep_cost[np.newaxis, :]

    return cost


# ---------------------------------------------------------------------------
# Self-referential fixed-point iteration
# ---------------------------------------------------------------------------

@dataclass
class TransportResult:
    """Result of the transport fixed-point iteration."""
    u_s: np.ndarray          # field at time s
    u_t: np.ndarray          # field at time t (source)
    M: np.ndarray            # transport plan
    converged: bool
    iterations: int
    fp_residuals: list       # per-iteration ||u_s_new - u_s||/||u_s||
    transport_energy: float  # lambda_tr * sum(M * cost)


def _minimize_with_transport(
    u_init: np.ndarray,
    graph: GraphState,
    params: ParameterRegistry,
) -> np.ndarray:
    """Find static energy minimizer using a transported field as initial guess.

    In the weak regime, transport influence enters through the initial guess
    u_init (warm-start from transported field), not as an additional energy
    term in the inner static optimization. The outer fixed-point loop
    (transport_fixed_point) handles the transport coupling iteratively.
    For strong regime, lambda_tr would need to be added as a penalty term
    in the static energy — this is deferred.

    Parameters
    ----------
    u_init : (n,) transported field to use as initialization.
    graph : GraphState
    params : ParameterRegistry

    Returns
    -------
    u_opt : (n,) optimized cohesion field.
    """
    from scc.optimizer import find_formation

    result = find_formation(graph, params, u_init=u_init)
    return result.u


def persist_transport(u_t: np.ndarray, u_s: np.ndarray, M: np.ndarray, theta_core: float = 0.8) -> float:
    """Core-to-core inheritance persistence via transport kernel.

    Measures how much of the cohesive core at time t is inherited
    by the core at time s through the transport plan M.

    Per Canonical Spec §7.1:
    Persist = Σ_{x∈Core_t} Σ_{y∈Core_s} M(x,y) · u_s(y) / ρ_persist

    where Core_t = {x : u_t(x) >= theta_core} and
    ρ_persist = Σ_{x∈Core_t} u_t(x) (normalization).

    Parameters
    ----------
    u_t : (n,) cohesion field at time t (source).
    u_s : (m,) cohesion field at time s (target).
    M : (n, m) transport plan from sinkhorn_partial_ot.
    theta_core : threshold for core membership (default 0.8).

    Returns
    -------
    float in [0, 1]. Persist = 1 means full core inheritance, 0 means none.
    """
    u_t = np.asarray(u_t, dtype=np.float64).ravel()
    u_s = np.asarray(u_s, dtype=np.float64).ravel()
    M = np.asarray(M, dtype=np.float64)

    core_t = u_t >= theta_core
    core_s = u_s >= theta_core

    if not np.any(core_t) or not np.any(core_s):
        return 0.0

    # Core-to-core transported mass
    M_core = M[np.ix_(core_t, core_s)]
    inherited = np.sum(M_core * u_s[core_s][np.newaxis, :])

    # Normalization: total core mass at time t
    rho = np.sum(u_t[core_t])

    return float(np.clip(inherited / max(rho, _EPS), 0.0, 1.0))


def transport_fixed_point(
    u_t: np.ndarray,
    graph: GraphState,
    params: ParameterRegistry,
    sigma: float = 1.0,
    gamma: float = 1.0,
    eps_ot: float = 1.0,
    lambda_tr: float = 0.1,
    max_fp_iter: int = 20,
    fp_tol: float = 1e-4,
    other_fields_s: Optional[List[np.ndarray]] = None,
    lambda_rep_transport: float = 0.0,
) -> TransportResult:
    """Self-referential fixed-point iteration for transport kernel.

    Alternates between computing the transport plan (given current fields)
    and re-optimizing the target field (given the transport bias), until
    mutual consistency is reached.

    In the weak regime (small lambda_tr, large eps_ot), the map Φ is a
    contraction and convergence is guaranteed.

    Parameters
    ----------
    u_t : (n,) cohesion field at time t (source formation).
    graph : GraphState (same spatial structure for both times).
    params : ParameterRegistry.
    sigma : spatial tolerance for transport cost.
    gamma : fingerprint weight for transport cost.
    eps_ot : entropic regularization for OT.
    lambda_tr : transport energy weight.
    max_fp_iter : maximum fixed-point iterations.
    fp_tol : convergence tolerance on relative u_s change.

    Returns
    -------
    TransportResult with converged field, transport plan, and diagnostics.

    References
    ----------
    Canonical Spec v2.0 §10, T-Persist.
    """
    u_t = np.asarray(u_t, dtype=np.float64).ravel()
    if np.any(np.isnan(u_t)):
        raise ValueError("Input field contains NaN")
    n = graph.n

    # Initialize u_s = u_t (identity initialization)
    u_s = u_t.copy()

    # Precompute invariants
    dist_matrix = graph_distance_matrix(graph)
    phi_t = cohesion_fingerprint(u_t, graph, params)

    fp_residuals = []
    M = np.zeros((n, n))
    cost = np.zeros((n, n))
    converged = False
    iterations = 0

    for k in range(1, max_fp_iter + 1):
        iterations = k

        # Step a: target fingerprint
        phi_s = cohesion_fingerprint(u_s, graph, params)

        # Step b: transport cost (with optional repulsion from other formations)
        cost = transport_cost(phi_t, phi_s, dist_matrix, sigma, gamma,
                              other_fields_s=other_fields_s,
                              lambda_rep=lambda_rep_transport)

        # Step c: optimal transport plan
        M, _info = sinkhorn_partial_ot(cost, u_t, u_s, eps_ot)

        # Step d: transported field
        u_transported = transport_field(M, u_s)

        # Step f: re-optimize with transport as warm start
        u_s_new = _minimize_with_transport(u_transported, graph, params)

        # Step g: convergence check
        norm_u_s = np.linalg.norm(u_s)
        residual = np.linalg.norm(u_s_new - u_s) / max(norm_u_s, _EPS)
        fp_residuals.append(float(residual))

        u_s = u_s_new

        if residual < fp_tol:
            converged = True
            break

    # Final transport energy
    transport_energy = float(lambda_tr * np.sum(M * cost))

    return TransportResult(
        u_s=u_s,
        u_t=u_t,
        M=M,
        converged=converged,
        iterations=iterations,
        fp_residuals=fp_residuals,
        transport_energy=transport_energy,
    )
