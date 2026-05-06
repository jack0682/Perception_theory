"""Stereo geometry: backprojection, pullback, depth-filtered adjacency.

Implements the observation layer from Canonical Memo v1.1 §D8, §D9:
  b_t: X_L^valid -> P_t  (backprojection, partial map)
  u_L^pix(x) = u_t(b_t(x))  (pullback to pixels)

See: stereo_scc_canonical_memo_v1.1.md §D8, §D9
"""
from __future__ import annotations

import numpy as np


def depth_from_disparity(
    disparity: np.ndarray,
    focal_length: float,
    baseline: float,
) -> np.ndarray:
    """Stereo depth formula: z = f_cam * b / delta.

    Args:
        disparity: Disparity field, shape (H, W) or (n,). Zero/negative = invalid.
        focal_length: Camera focal length in pixels
        baseline: Stereo baseline in meters

    Returns:
        depth: Depth in meters (same shape; inf where disparity <= 0)
    """
    disp = np.asarray(disparity, dtype=np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        depth = np.where(disp > 0, focal_length * baseline / disp, np.inf)
    return depth


def backproject_pixels(
    pixels_uv: np.ndarray,
    depth: np.ndarray,
    K_cam: np.ndarray,
    confidence: np.ndarray | None = None,
    min_confidence: float = 0.1,
) -> tuple[np.ndarray, np.ndarray]:
    """Backproject valid pixels to 3D point cloud (partial map b_t).

    Implements b_t(x_L) = z(x_L) * K_cam^{-1} * [u_L, v_L, 1]^T
    (Canonical Memo v1.1 §D9). Partiality: undefined for low-confidence pixels.

    Args:
        pixels_uv: Pixel coordinates, shape (n, 2) as (u, v) = (col, row)
        depth: Depth values, shape (n,)
        K_cam: 3x3 camera intrinsic matrix
        confidence: Optional disparity confidence, shape (n,). If None, all valid.
        min_confidence: Minimum confidence to include a pixel

    Returns:
        points_3d: 3D points, shape (m, 3) for valid pixels only
        valid_mask: Boolean mask shape (n,) indicating which pixels were backprojected
    """
    n = len(pixels_uv)
    if confidence is None:
        confidence = np.ones(n, dtype=np.float64)

    valid = (confidence >= min_confidence) & np.isfinite(depth) & (depth > 0)
    uv_valid = pixels_uv[valid]
    z_valid = depth[valid]

    K_inv = np.linalg.inv(K_cam)
    ones = np.ones((valid.sum(), 1), dtype=np.float64)
    uv1 = np.hstack([uv_valid, ones])  # (m, 3)
    rays = (K_inv @ uv1.T).T  # (m, 3)
    points_3d = rays * z_valid[:, None]  # scale by depth

    return points_3d, valid


def pullback_field_to_pixels(
    u_3d: np.ndarray,
    point_indices: np.ndarray,
    n_pixels: int,
) -> np.ndarray:
    """Pull back 3D cohesion field to pixel space.

    Computes u_L^pix(x) = u_t(b_t(x)) for valid pixels.
    For invalid pixels (not in domain of b_t), assigns NaN.

    Args:
        u_3d: Cohesion field on point cloud, shape (m,) for m valid points
        point_indices: Original pixel indices for each point, shape (m,)
        n_pixels: Total number of pixels

    Returns:
        u_pix: Pixel-space cohesion field, shape (n_pixels,); NaN at invalid pixels
    """
    u_pix = np.full(n_pixels, np.nan, dtype=np.float64)
    u_pix[point_indices] = u_3d
    return u_pix


def depth_filtered_adjacency_3d(
    points_3d: np.ndarray,
    k_neighbors: int = 6,
    max_dist_3d: float = 0.1,
    depth_weight: float = 5.0,
) -> "sp.csr_matrix":
    """Build depth-aware adjacency for 3D point cloud.

    Edge weight w(i,j) = exp(-d_3d^2 / sigma^2) * depth_penalty(i,j)
    where depth_penalty suppresses edges across depth discontinuities.

    Implements E_t^3D from Canonical Memo v1.1 §D1.

    Args:
        points_3d: 3D points, shape (m, 3)
        k_neighbors: Number of nearest neighbors to consider
        max_dist_3d: Maximum 3D distance for an edge
        depth_weight: Weight applied to depth difference in edge weighting

    Returns:
        adj: Sparse (m, m) adjacency matrix
    """
    import scipy.sparse as sp

    m = len(points_3d)
    from scipy.spatial import cKDTree

    tree = cKDTree(points_3d)
    distances, indices = tree.query(points_3d, k=k_neighbors + 1)

    row_idx, col_idx, data = [], [], []
    for i in range(m):
        for j_local in range(1, k_neighbors + 1):
            j = indices[i, j_local]
            d_3d = distances[i, j_local]
            if d_3d > max_dist_3d:
                continue
            depth_diff = abs(points_3d[i, 2] - points_3d[j, 2])
            w = np.exp(-d_3d**2 / (max_dist_3d / 2) ** 2) * np.exp(
                -depth_weight * depth_diff
            )
            if w > 1e-6:
                row_idx.append(i)
                col_idx.append(j)
                data.append(w)

    adj = sp.csr_matrix((data, (row_idx, col_idx)), shape=(m, m))
    adj = (adj + adj.T) / 2.0  # symmetrize
    return adj
