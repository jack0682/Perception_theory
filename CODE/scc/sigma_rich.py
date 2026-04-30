"""σ_rich augmentation for K-jump deterministic inheritance (OP-0008 Path B).

Implements the rich σ-tuple per
``THEORY/working/MF/sigma_rich_augmentation.md``::

    σ_rich = (σ_standard, centroids, orientations, wigner_data)

All four components are derived diagnostics of the primitive ``u_t`` field
(CN10 contrastive). σ_rich does not introduce new energy terms (CN5 4-energy
independence preserved). The Hessian-derived blocks (σ_standard, wigner_data)
operate on the existing :class:`scc.energy.EnergyComputer` API.

Status: working-only Cat B sketch (W5 Day 4, 2026-04-30). Irrep labels in
σ_standard are multiplicity placeholders pending Aut(G)_{u*} character data.
"""
from __future__ import annotations

from collections import namedtuple
from typing import Optional, Tuple

import numpy as np

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer


SigmaRich = namedtuple(
    "SigmaRich",
    ["sigma_standard", "centroids", "orientations", "wigner_data"],
)


# ---------------------------------------------------------------------------
# Position helpers
# ---------------------------------------------------------------------------

def _resolve_positions(graph_state: GraphState,
                       positions: Optional[np.ndarray]) -> np.ndarray:
    """Resolve node positions from explicit kwarg or GraphState attribute."""
    if positions is not None:
        return np.asarray(positions, dtype=np.float64)
    pos = getattr(graph_state, "positions", None)
    if pos is not None:
        return np.asarray(pos, dtype=np.float64)
    raise ValueError(
        "compute_sigma_rich requires node positions. Pass positions=<(n,d) "
        "array> or set graph_state.positions."
    )


def _normalize_field(u: np.ndarray) -> np.ndarray:
    """Coerce single-formation (n,) input to (1, n) K-field shape."""
    u = np.asarray(u, dtype=np.float64)
    if u.ndim == 1:
        return u[np.newaxis, :]
    if u.ndim == 2:
        return u
    raise ValueError(f"u_field must have shape (n,) or (K, n); got {u.shape}")


# ---------------------------------------------------------------------------
# Centroid + orientation tensor (per-formation spatial moments — §2.3.1, §2.3.2)
# ---------------------------------------------------------------------------

def compute_centroids(u_field: np.ndarray,
                      positions: np.ndarray,
                      eps: float = 1e-12) -> np.ndarray:
    """Per-formation u-weighted centroid c_j = Σ_x u^j(x) x / Σ_x u^j(x).

    Returns ``(K, d)``.
    """
    u = _normalize_field(u_field)
    masses = u.sum(axis=1, keepdims=True)
    masses = np.where(masses < eps, eps, masses)
    return (u @ positions) / masses


def compute_orientations(u_field: np.ndarray,
                         positions: np.ndarray,
                         centroids: Optional[np.ndarray] = None) -> np.ndarray:
    """Per-formation inertia tensor ``M_j = Σ_x u^j(x)(x-c_j)(x-c_j)^T``.

    Returns ``(K, d, d)``. Eigen-decomposition is left to the caller; the
    public ``compute_sigma_rich`` returns an eigenvalue-sorted version.
    """
    u = _normalize_field(u_field)
    if centroids is None:
        centroids = compute_centroids(u, positions)
    K = u.shape[0]
    d = positions.shape[1]
    M = np.empty((K, d, d), dtype=np.float64)
    for j in range(K):
        x_centered = positions - centroids[j]
        M[j] = np.einsum("i,ia,ib->ab", u[j], x_centered, x_centered)
    return M


# ---------------------------------------------------------------------------
# Hessian computation (full FD; tractable for moderate n)
# ---------------------------------------------------------------------------

def _build_hessian(u: np.ndarray,
                   graph_state: GraphState,
                   params: ParameterRegistry,
                   h: float = 1e-5) -> np.ndarray:
    """Symmetric finite-difference Hessian of total energy at ``u``."""
    ec = EnergyComputer(graph_state, params)
    n = u.shape[0]
    H = np.zeros((n, n), dtype=np.float64)
    g0 = ec.gradient(u)
    for i in range(n):
        u_p = u.copy()
        u_p[i] += h
        H[:, i] = (ec.gradient(u_p) - g0) / h
    return 0.5 * (H + H.T)


def _hessian_eigenpairs(u_field: np.ndarray,
                        graph_state: GraphState,
                        params: ParameterRegistry,
                        n_pairs: Optional[int] = None
                        ) -> Tuple[np.ndarray, np.ndarray]:
    """Compute Hessian eigenpairs at the (mean) field configuration."""
    u = _normalize_field(u_field)
    u_mean = u.mean(axis=0)
    H = _build_hessian(u_mean, graph_state, params)
    eigvals, eigvecs = np.linalg.eigh(H)
    if n_pairs is not None:
        eigvals = eigvals[:n_pairs]
        eigvecs = eigvecs[:, :n_pairs]
    return eigvals, eigvecs


# ---------------------------------------------------------------------------
# σ_standard — Hessian eigenvalue / multiplicity triples (§2.2)
# ---------------------------------------------------------------------------

def _sigma_standard(eigvals: np.ndarray, tol: float = 1e-6) -> tuple:
    """Group eigenvalues into degenerate clusters → (n_k, irrep_label, λ_k).

    Without explicit Aut(G)_{u*} character data, irrep labels default to a
    multiplicity tag ``mult-{n_k}`` (Cat B placeholder, §2.4 W2 forward gap).
    """
    eigvals = np.asarray(eigvals, dtype=np.float64)
    if eigvals.size == 0:
        return tuple()
    sorted_vals = np.sort(eigvals)
    out = []
    cluster_start = sorted_vals[0]
    cluster_size = 1
    for v in sorted_vals[1:]:
        if abs(v - cluster_start) < tol:
            cluster_size += 1
        else:
            out.append((cluster_size, f"mult-{cluster_size}",
                        float(cluster_start)))
            cluster_start = v
            cluster_size = 1
    out.append((cluster_size, f"mult-{cluster_size}", float(cluster_start)))
    return tuple(out)


# ---------------------------------------------------------------------------
# Wigner-von Neumann avoided-crossing 2×2 effective Hamiltonians (§2.3.3)
# ---------------------------------------------------------------------------

def _wigner_data(eigvals: np.ndarray,
                 eigvecs: np.ndarray,
                 u_field: np.ndarray,
                 near_deg_tol: float = 1e-3) -> np.ndarray:
    """Pairwise (K, K, 2, 2) Wigner-vN avoided-crossing 2×2 matrices.

    For each formation pair (j, k) the diagonal entries are the two lowest
    Hessian eigenvalues (the candidate Goldstone-pair). The off-diagonal
    captures cross-formation mixing on the Goldstone subspace via Schur
    projection of the formation densities ``u^j``, ``u^k``.

    Reed-Simon IV §XIII.5 (Wigner-von Neumann): for codim-2 generic
    crossings, non-degenerate eigenvalues yield diagonal 2×2 blocks within
    a single formation (j == k, no level repulsion). Cross-formation pairs
    (j != k) carry mixing proportional to projection overlap.
    """
    u = _normalize_field(u_field)
    K = u.shape[0]
    W = np.zeros((K, K, 2, 2), dtype=np.float64)
    if eigvals.size == 0:
        return W

    lam0 = float(eigvals[0])
    lam1 = float(eigvals[1]) if eigvals.size > 1 else 0.0
    is_degenerate = abs(lam1 - lam0) < near_deg_tol

    if eigvecs.ndim == 2 and eigvecs.shape[1] >= 2:
        vecs2 = eigvecs[:, :2]
    else:
        vecs2 = None

    for j in range(K):
        for k in range(K):
            W[j, k, 0, 0] = lam0
            W[j, k, 1, 1] = lam1
            # Off-diagonal mixing: only nonzero for (a) degenerate Goldstone
            # pair, or (b) cross-formation pair with shared Goldstone support.
            if vecs2 is not None and (is_degenerate or j != k):
                u_j = u[j]
                u_k = u[k]
                nj = np.linalg.norm(u_j) + 1e-12
                nk = np.linalg.norm(u_k) + 1e-12
                pj = vecs2.T @ (u_j / nj)
                pk = vecs2.T @ (u_k / nk)
                mix = 0.5 * float(pj[0] * pk[1] + pj[1] * pk[0])
                W[j, k, 0, 1] = mix
                W[j, k, 1, 0] = mix
    return W


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def compute_sigma_rich(
    u_field: np.ndarray,
    graph_state: GraphState,
    params: ParameterRegistry,
    hessian_eigenpairs: Optional[Tuple[np.ndarray, np.ndarray]] = None,
    positions: Optional[np.ndarray] = None,
    n_eig: int = 6,
) -> SigmaRich:
    """Compute σ_rich = (σ_standard, centroids, orientations, wigner_data).

    See ``THEORY/working/MF/sigma_rich_augmentation.md`` §2 for the full
    mathematical specification.

    Args:
        u_field: shape ``(n,)`` for single-formation or ``(K, n)`` for
            K-field multi-formation input.
        graph_state: :class:`GraphState`.
        params: :class:`ParameterRegistry`.
        hessian_eigenpairs: optional precomputed
            ``(eigenvalues, eigenvectors)``. If None, computed via
            full finite-difference Hessian + ``np.linalg.eigh``.
        positions: ``(n, d)`` node positions. If None, falls back to
            ``getattr(graph_state, 'positions', None)``.
        n_eig: number of Hessian eigenpairs to compute when
            ``hessian_eigenpairs`` is None.

    Returns:
        :class:`SigmaRich` namedtuple.
    """
    pos = _resolve_positions(graph_state, positions)

    centroids = compute_centroids(u_field, pos)
    raw_orient = compute_orientations(u_field, pos, centroids=centroids)

    # Eigenvalue-sorted (descending) reconstruction of the orientation tensor.
    orientations = np.empty_like(raw_orient)
    for j in range(raw_orient.shape[0]):
        eigvals_j, eigvecs_j = np.linalg.eigh(raw_orient[j])
        order = np.argsort(eigvals_j)[::-1]
        Q = eigvecs_j[:, order]
        D = np.diag(eigvals_j[order])
        orientations[j] = Q @ D @ Q.T

    if hessian_eigenpairs is None:
        eigvals, eigvecs = _hessian_eigenpairs(
            u_field, graph_state, params, n_pairs=n_eig
        )
    else:
        eigvals, eigvecs = hessian_eigenpairs
        eigvals = np.asarray(eigvals, dtype=np.float64)
        eigvecs = np.asarray(eigvecs, dtype=np.float64)

    sigma_standard = _sigma_standard(eigvals)
    wigner_data = _wigner_data(eigvals, eigvecs, u_field)

    return SigmaRich(
        sigma_standard=sigma_standard,
        centroids=centroids,
        orientations=orientations,
        wigner_data=wigner_data,
    )
