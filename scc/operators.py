"""SCC operators: Closure (Cl_t), Distinction (D_t), Aggregation (P_t), Co-belonging (C_t).

All operator forms follow Canonical Spec v2.0 §9.
"""

from __future__ import annotations

import numpy as np
import scipy.sparse as sp

from scc.graph import GraphState
from scc.params import ParameterRegistry


# ---------------------------------------------------------------------------
# Numerically stable sigmoid
# ---------------------------------------------------------------------------

def sigmoid(x: np.ndarray) -> np.ndarray:
    """Logistic sigmoid with numerical stability."""
    return np.where(
        x >= 0,
        1.0 / (1.0 + np.exp(-x)),
        np.exp(x) / (1.0 + np.exp(x)),
    )


def sigmoid_deriv(s: np.ndarray) -> np.ndarray:
    """Derivative of sigmoid given sigmoid output s: s*(1-s)."""
    return s * (1.0 - s)


# ---------------------------------------------------------------------------
# Aggregation P_t  (Spec §9.1)
# ---------------------------------------------------------------------------

def aggregation(u: np.ndarray, graph: GraphState) -> np.ndarray:
    """(P_t u)(x) = sum_y N(x,y) u(y) / (sum_y N(x,y) + eps).

    Uses the precomputed row-normalized adjacency P.
    """
    return np.asarray(graph.P @ u).ravel()


# ---------------------------------------------------------------------------
# Closure Cl_t  (Spec §9.2)
# ---------------------------------------------------------------------------

def closure(
    u: np.ndarray, graph: GraphState, params: ParameterRegistry
) -> np.ndarray:
    """Cl_t(u)(x) = sigma(a_cl * ((1 - eta_cl)*u(x) + eta_cl*(P_t u)(x) - tau_cl)).

    Returns the closure-applied field.
    """
    Pu = aggregation(u, graph)
    z = params.a_cl * (
        (1.0 - params.eta_cl) * u + params.eta_cl * Pu - params.tau_cl
    )
    return sigmoid(z)


def closure_with_jacobian(
    u: np.ndarray, graph: GraphState, params: ParameterRegistry
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute Cl_t(u) and the quantities needed for the Jacobian.

    Returns (Cl_u, sigma_prime, z) where:
      - Cl_u: the closure output
      - sigma_prime: sigmoid derivative at the pre-activation
      - z: the pre-activation values

    The Jacobian J_Cl is:
      J_Cl = diag(sigma_prime * a_cl) @ ((1-eta)*I + eta*P)
    which is sparse and applied via mat-vec, never formed explicitly.
    """
    Pu = aggregation(u, graph)
    z = params.a_cl * (
        (1.0 - params.eta_cl) * u + params.eta_cl * Pu - params.tau_cl
    )
    Cl_u = sigmoid(z)
    sigma_prime = sigmoid_deriv(Cl_u)  # sigma'(z) = sigma(z)*(1-sigma(z))
    return Cl_u, sigma_prime, z


def closure_jacobian_transpose_vec(
    v: np.ndarray,
    sigma_prime: np.ndarray,
    graph: GraphState,
    params: ParameterRegistry,
) -> np.ndarray:
    """Compute J_Cl^T @ v without forming J_Cl.

    J_Cl = diag(sigma' * a_cl) @ ((1-eta)*I + eta*P)
    J_Cl^T = ((1-eta)*I + eta*P^T) @ diag(sigma' * a_cl)
    J_Cl^T @ v = ((1-eta)*I + eta*P^T) @ (sigma' * a_cl * v)
    """
    w = sigma_prime * params.a_cl * v
    result = (1.0 - params.eta_cl) * w + params.eta_cl * np.asarray(
        graph.P.T @ w
    ).ravel()
    return result


# ---------------------------------------------------------------------------
# Distinction D_t  (Spec §9.3)
# ---------------------------------------------------------------------------

def distinction(
    u: np.ndarray, graph: GraphState, params: ParameterRegistry
) -> np.ndarray:
    """D_t(x; 1-u) = sigma(a_D * (P_t(u)(x) - lambda_D * P_t(1-u)(x)) - tau_D).

    Per the P_1 trick: P_t(1-u) = P_1 - P_t(u).
    b_D = 0 enforced (analyticity requirement).
    """
    Pu = aggregation(u, graph)
    P1_minus_Pu = graph.P_1 - Pu  # P_t(1-u)
    z = params.a_D * (Pu - params.lambda_D * P1_minus_Pu) - params.tau_D
    return sigmoid(z)


def distinction_with_jacobian(
    u: np.ndarray, graph: GraphState, params: ParameterRegistry
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute D_t(u) and Jacobian ingredients.

    Returns (D_u, sigma_prime_D, z_D).

    The Jacobian J_D is:
      J_D = diag(sigma'_D * a_D * (1 + lambda_D)) @ P
    This follows because d/du [P_t(u) - lambda_D * P_t(1-u)]
      = P + lambda_D * P = (1 + lambda_D) * P
    """
    Pu = aggregation(u, graph)
    P1_minus_Pu = graph.P_1 - Pu
    z = params.a_D * (Pu - params.lambda_D * P1_minus_Pu) - params.tau_D
    D_u = sigmoid(z)
    sigma_prime_D = sigmoid_deriv(D_u)
    return D_u, sigma_prime_D, z


def distinction_jacobian_transpose_vec(
    v: np.ndarray,
    sigma_prime_D: np.ndarray,
    graph: GraphState,
    params: ParameterRegistry,
) -> np.ndarray:
    """Compute J_D^T @ v without forming J_D.

    J_D = diag(sigma'_D * a_D * (1+lambda_D)) @ P
    J_D^T = P^T @ diag(sigma'_D * a_D * (1+lambda_D))
    J_D^T @ v = P^T @ (sigma'_D * a_D * (1+lambda_D) * v)
    """
    w = sigma_prime_D * params.a_D * (1.0 + params.lambda_D) * v
    return np.asarray(graph.P.T @ w).ravel()


# ---------------------------------------------------------------------------
# Co-belonging C_t  (Spec §9.4) — Resolvent form, diagnostic only
# ---------------------------------------------------------------------------

def resolvent_diagonal(
    u: np.ndarray,
    graph: GraphState,
    params: ParameterRegistry,
) -> np.ndarray:
    """Compute the diagonal of C_t = (I - alpha_C * W_sym)^{-1}.

    Uses Neumann series truncation: C_t ≈ sum_{k=0}^{K} (alpha_C * W_sym)^k.
    Only the diagonal is tracked (cheap).

    Convergence requires alpha_C * rho(W_sym) < 1. If the series diverges
    (diagonal values exceed a safety threshold), iteration is truncated early.
    """
    W_sym = graph.cohesion_weighted_symmetric(u)
    n = graph.n
    alpha = params.alpha_C
    K = params.k_neumann

    # Track diagonal via stochastic probing or power iteration on diagonal
    # For exact diagonal: multiply successive powers and accumulate
    diag = np.ones(n)
    # v_k = (alpha * W_sym)^k @ e_i for all i simultaneously
    # We track the diagonal by computing (alpha*W_sym)^k row-by-row? Too expensive.
    # Instead: use the identity that diag(A^k) = sum_j A_{ij} * (A^{k-1})_{ji}
    # For sparse W_sym, cheapest: accumulate column-wise products.
    # Actually simplest correct approach: compute (alpha*W_sym)^k @ I columns
    # But that's O(n^2).
    # For practical use: Hutchinson trace estimator or Neumann on vectors.

    # Simple approach for moderate n: multiply power matrices
    aW = (alpha * W_sym).tocsr()
    power = sp.eye(n, format="csr")
    for k in range(1, K + 1):
        power = power @ aW
        diag += power.diagonal()
        # Divergence guard: if diagonal values explode, truncate early
        if np.max(np.abs(diag)) > 1e6:
            break

    return diag


def resolvent_full(
    u: np.ndarray,
    graph: GraphState,
    params: ParameterRegistry,
    method: str = "neumann",
) -> np.ndarray:
    """Compute full C_t matrix. Only for small n (diagnostic).

    Returns dense (n, n) array.
    """
    W_sym = graph.cohesion_weighted_symmetric(u)
    n = graph.n
    alpha = params.alpha_C

    if method == "exact":
        I = np.eye(n)
        return np.linalg.inv(I - alpha * W_sym.toarray())

    elif method == "neumann":
        K = params.k_neumann
        aW = alpha * W_sym
        result = sp.eye(n, format="csr")
        power = sp.eye(n, format="csr")
        for k in range(1, K + 1):
            power = power @ aW
            result = result + power
        return result.toarray()

    else:
        raise ValueError(f"Unknown method: {method}")


# ---------------------------------------------------------------------------
# Dict-param compatibility wrappers (for test harness)
# ---------------------------------------------------------------------------

def _make_graph_params(N_t: sp.spmatrix, params: dict):
    """Convert raw sparse matrix + dict to GraphState + ParameterRegistry."""
    graph = GraphState(N_t)
    p = ParameterRegistry(
        a_cl=params.get("a_cl", 3.5),
        eta_cl=params.get("eta_cl", 0.5),
        tau_cl=params.get("tau_cl", 0.5),
        a_D=params.get("a_D", 5.0),
        lambda_D=params.get("lambda_D", 1.0),
        tau_D=params.get("tau_D", 0.0),
        b_D=params.get("b_D", 0.0),
        alpha_C=params.get("alpha_C", 0.5),
        k_neumann=params.get("k_neumann", 10),
        alpha_bd=params.get("alpha_bd", 1.0),
        beta_bd=params.get("beta_bd", 10.0),
        volume_fraction=params.get("volume_fraction", 0.3),
        eps_agg=params.get("eps", 1e-10),
    )
    return graph, p


def aggregation_operator(f: np.ndarray, N_t: sp.spmatrix, eps: float = 1e-10) -> np.ndarray:
    """(P_t f)(x) = sum_y N(x,y) f(y) / (sum_y N(x,y) + eps)."""
    graph = GraphState(N_t)
    return aggregation(f, graph)


def closure_operator(u: np.ndarray, N_t: sp.spmatrix, params: dict) -> np.ndarray:
    """Cl_t(u) — dict-param interface."""
    graph, p = _make_graph_params(N_t, params)
    return closure(u, graph, p)


def distinction_operator(u: np.ndarray, N_t: sp.spmatrix, params: dict) -> np.ndarray:
    """D_t(x; 1-u) — dict-param interface."""
    graph, p = _make_graph_params(N_t, params)
    return distinction(u, graph, p)


def jacobian_closure(u: np.ndarray, N_t: sp.spmatrix, params: dict) -> np.ndarray:
    """Full n×n Jacobian of closure operator (dense). For testing only."""
    graph, p = _make_graph_params(N_t, params)
    _, sigma_prime, z = closure_with_jacobian(u, graph, p)
    n = len(u)
    # J_Cl = diag(sigma' * a_cl) @ ((1-eta)*I + eta*P)
    scale = sigma_prime * p.a_cl
    mix = (1.0 - p.eta_cl) * sp.eye(n) + p.eta_cl * graph.P
    J = sp.diags(scale) @ mix
    return J.toarray()


def jacobian_distinction(u: np.ndarray, N_t: sp.spmatrix, params: dict) -> np.ndarray:
    """Full n×n Jacobian of distinction operator (dense). For testing only."""
    graph, p = _make_graph_params(N_t, params)
    _, sigma_prime_D, z_D = distinction_with_jacobian(u, graph, p)
    n = len(u)
    # J_D = diag(sigma'_D * a_D * (1+lambda_D)) @ P
    scale = sigma_prime_D * p.a_D * (1.0 + p.lambda_D)
    J = sp.diags(scale) @ graph.P
    return J.toarray()
