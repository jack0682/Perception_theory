"""Field construction: soft cohesion fields on graphs and 3D point clouds.

F_0(P) = {u: P -> [0,1]}  (base field space, no mass constraint)
F_M(P) = {u in F_0: sum u_i * mu_i = M}  (mass-constrained)

See: stereo_scc_canonical_memo_v1.1.md §D2, §D3
"""
from __future__ import annotations

import numpy as np
import scipy.sparse as sp


def make_grid_2d(rows: int, cols: int, weight: float = 1.0) -> tuple[sp.csr_matrix, tuple[int, int]]:
    """4-connected 2D grid adjacency matrix.

    Returns:
        adj: sparse (n, n) symmetric adjacency
        shape: (rows, cols)
    """
    n = rows * cols
    row_idx, col_idx = [], []
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            if c + 1 < cols:
                row_idx.extend([idx, idx + 1])
                col_idx.extend([idx + 1, idx])
            if r + 1 < rows:
                row_idx.extend([idx, idx + cols])
                col_idx.extend([idx + cols, idx])
    data = np.full(len(row_idx), weight, dtype=np.float64)
    adj = sp.csr_matrix((data, (row_idx, col_idx)), shape=(n, n))
    return adj, (rows, cols)


def make_depth_separated_grid(
    rows: int,
    cols: int,
    depth_map: np.ndarray,
    delta_z: float = 0.5,
) -> tuple[sp.csr_matrix, tuple[int, int]]:
    """2D grid with depth-filtered adjacency (Canonical Memo v1.1 §D1).

    Edges between adjacent pixels are removed if |z(x) - z(y)| >= delta_z.
    This implements the depth-aware adjacency G_t^P that prevents closure
    support from bridging across depth discontinuities.

    Args:
        rows, cols: Grid dimensions
        depth_map: Depth values, shape (rows*cols,) or (rows, cols)
        delta_z: Depth discontinuity threshold

    Returns:
        adj: sparse (n, n) depth-filtered adjacency
        shape: (rows, cols)
    """
    depth = np.asarray(depth_map, dtype=np.float64).ravel()
    assert len(depth) == rows * cols

    n = rows * cols
    row_idx, col_idx, data = [], [], []
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            # horizontal neighbor
            if c + 1 < cols:
                jdx = idx + 1
                if abs(depth[idx] - depth[jdx]) < delta_z:
                    row_idx.extend([idx, jdx])
                    col_idx.extend([jdx, idx])
                    data.extend([1.0, 1.0])
            # vertical neighbor
            if r + 1 < rows:
                jdx = idx + cols
                if abs(depth[idx] - depth[jdx]) < delta_z:
                    row_idx.extend([idx, jdx])
                    col_idx.extend([jdx, idx])
                    data.extend([1.0, 1.0])

    adj = sp.csr_matrix((data, (row_idx, col_idx)), shape=(n, n))
    return adj, (rows, cols)


def gaussian_field(
    n: int,
    centers: list,
    sigma: float,
    height: float = 0.9,
    grid_shape: tuple[int, int] | None = None,
) -> np.ndarray:
    """Soft cohesion field as sum of Gaussians centered at given nodes.

    Produces u in F_0 (values in [0,1]) before mass normalization.

    Args:
        n: Number of nodes
        centers: Flat node indices (int) or (row, col) tuples when grid_shape given
        sigma: Width parameter (in pixel units for 2D, node-index units for 1D)
        height: Peak value (< 1.0 to stay strictly interior to [0,1])
        grid_shape: (rows, cols) — if given, centers are treated as (row, col) tuples
                    and distances computed in 2D Euclidean space

    Returns:
        u: array of shape (n,)
    """
    u = np.zeros(n, dtype=np.float64)
    if grid_shape is not None:
        rows, cols = grid_shape
        r_idx, c_idx = np.divmod(np.arange(n), cols)
        for center in centers:
            cr, cc = center
            dist2 = (r_idx - cr) ** 2 + (c_idx - cc) ** 2
            u += height * np.exp(-0.5 * dist2 / sigma ** 2)
    else:
        for c in centers:
            distances = np.abs(np.arange(n) - c).astype(float)
            u += height * np.exp(-0.5 * (distances / sigma) ** 2)
    return np.clip(u, 0.0, 1.0)


def normalize_field(u: np.ndarray, M: float) -> np.ndarray:
    """Project u onto the mass-constrained simplex face F_M.

    Scales u so that sum(u) = M while keeping values in [0,1].
    Uses multiplicative scaling (valid when sum(u) > 0).

    Args:
        u: Input field, shape (n,)
        M: Target mass

    Returns:
        u_norm: Scaled field with sum = M, values in [0,1]
    """
    total = u.sum()
    if total < 1e-12:
        raise ValueError("Cannot normalize zero field")
    scale = M / total
    u_norm = u * scale
    if u_norm.max() > 1.0:
        u_norm = u_norm / u_norm.max() * 0.999
        u_norm = u_norm * (M / u_norm.sum())
    return np.clip(u_norm, 0.0, 1.0)


def laplacian_from_adj(adj: sp.spmatrix) -> sp.csr_matrix:
    """Combinatorial Laplacian L = D - A."""
    degree = np.asarray(adj.sum(axis=1)).ravel()
    D = sp.diags(degree, format="csr")
    return (D - adj).astype(np.float64)
