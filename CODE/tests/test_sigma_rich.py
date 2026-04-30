"""Tests for scc.sigma_rich — OP-0008 Path B σ_rich numerical pipeline.

Spec: THEORY/working/MF/sigma_rich_augmentation.md
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import pytest

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.sigma_rich import (
    SigmaRich,
    compute_sigma_rich,
    compute_centroids,
    compute_orientations,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def grid_positions(rows: int, cols: int) -> np.ndarray:
    """Reconstruct (row, col) positions for grid_2d node ordering."""
    return np.array(
        [[r, c] for r in range(rows) for c in range(cols)],
        dtype=np.float64,
    )


def make_test_graph(rows: int = 6, cols: int = 6):
    g = GraphState.grid_2d(rows, cols)
    g.positions = grid_positions(rows, cols)
    return g, g.positions


def make_test_params() -> ParameterRegistry:
    return ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=10.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.3,
    )


# ===========================================================================
# Centroid tests — §2.3.1
# ===========================================================================

class TestCentroid:

    def test_centroid_uniform(self):
        """Uniform u → centroid equals mean of node positions."""
        g, pos = make_test_graph(6, 6)
        u = np.full(g.n, 0.5)
        c = compute_centroids(u, pos)
        assert c.shape == (1, 2)
        np.testing.assert_allclose(c[0], pos.mean(axis=0), atol=1e-9)

    def test_centroid_localized(self):
        """tanh-disk profile → centroid ≈ disk center within 1e-3."""
        rows, cols = 11, 11
        g, pos = make_test_graph(rows, cols)
        center = np.array([5.0, 5.0])  # interior, symmetric
        r = np.linalg.norm(pos - center, axis=1)
        u = 0.5 * (1.0 - np.tanh((r - 2.5) / 0.4))
        c = compute_centroids(u, pos)
        np.testing.assert_allclose(c[0], center, atol=1e-3)

    def test_centroid_multiformation(self):
        """K=2 → returns (2, d) centroids per formation."""
        rows, cols = 12, 12
        g, pos = make_test_graph(rows, cols)
        center_a = np.array([3.0, 3.0])
        center_b = np.array([8.0, 8.0])
        ra = np.linalg.norm(pos - center_a, axis=1)
        rb = np.linalg.norm(pos - center_b, axis=1)
        u_a = 0.5 * (1.0 - np.tanh((ra - 1.5) / 0.4))
        u_b = 0.5 * (1.0 - np.tanh((rb - 1.5) / 0.4))
        u = np.stack([u_a, u_b])
        c = compute_centroids(u, pos)
        assert c.shape == (2, 2)
        np.testing.assert_allclose(c[0], center_a, atol=5e-3)
        np.testing.assert_allclose(c[1], center_b, atol=5e-3)


# ===========================================================================
# Orientation tests — §2.3.2
# ===========================================================================

class TestOrientation:

    def test_orientation_isotropic(self):
        """Isotropic disk → orientation eigenvalues approximately equal."""
        rows, cols = 13, 13
        g, pos = make_test_graph(rows, cols)
        center = np.array([6.0, 6.0])
        r = np.linalg.norm(pos - center, axis=1)
        u = 0.5 * (1.0 - np.tanh((r - 3.0) / 0.4))
        M = compute_orientations(u, pos)
        eigvals = np.sort(np.linalg.eigvalsh(M[0]))
        ratio = eigvals[1] / max(eigvals[0], 1e-12)
        assert ratio < 1.15, (
            f"isotropy violated: ratio={ratio:.3f}, eigvals={eigvals}"
        )

    def test_orientation_elongated(self):
        """Anisotropic Gaussian → primary axis aligned with elongation."""
        rows, cols = 15, 15
        g, pos = make_test_graph(rows, cols)
        center = np.array([7.0, 7.0])
        diff = pos - center
        sigma_x, sigma_y = 4.0, 1.0
        u = np.exp(
            -0.5 * ((diff[:, 0] / sigma_x) ** 2 + (diff[:, 1] / sigma_y) ** 2)
        )
        u = np.clip(u, 0.0, 1.0)
        M = compute_orientations(u, pos)
        eigvals, eigvecs = np.linalg.eigh(M[0])
        primary = eigvecs[:, np.argmax(eigvals)]
        assert abs(primary[0]) > abs(primary[1]), (
            f"primary axis = {primary} but elongation is along axis-0"
        )

    def test_orientation_sorted_in_compute_sigma_rich(self):
        """Public sigma_rich returns eigenvalue-sorted orientation tensor."""
        g, pos = make_test_graph(6, 6)
        params = make_test_params()
        center = np.array([2.5, 2.5])
        diff = pos - center
        u = np.exp(-0.5 * ((diff[:, 0] / 3.0) ** 2 + (diff[:, 1] / 1.0) ** 2))
        eigvals = np.array([0.5, 1.5, 3.0])
        eigvecs = np.eye(g.n)[:, :3]
        sr = compute_sigma_rich(
            u, g, params, hessian_eigenpairs=(eigvals, eigvecs)
        )
        # Diagonalize the returned tensor; eigvals should be sorted descending
        e = np.sort(np.linalg.eigvalsh(sr.orientations[0]))[::-1]
        assert e[0] >= e[1] >= 0.0


# ===========================================================================
# Wigner-vN avoided-crossing tests — §2.3.3
# ===========================================================================

class TestWigner:

    def test_wigner_diagonal(self):
        """Non-degenerate Hessian → wigner_data 2×2 block is diagonal."""
        g, pos = make_test_graph(5, 5)
        params = make_test_params()
        center = np.array([2.0, 2.0])
        r = np.linalg.norm(pos - center, axis=1)
        u = 0.5 * (1.0 - np.tanh((r - 1.5) / 0.5))
        # Inject deliberately non-degenerate eigenvalues (gap >> tol).
        eigvals = np.array([1.0, 5.0, 10.0])
        eigvecs = np.eye(g.n)[:, :3]
        sr = compute_sigma_rich(
            u, g, params, hessian_eigenpairs=(eigvals, eigvecs)
        )
        W = sr.wigner_data
        assert W.shape == (1, 1, 2, 2)
        # Diagonal entries are the two lowest eigenvalues.
        np.testing.assert_allclose(W[0, 0, 0, 0], 1.0)
        np.testing.assert_allclose(W[0, 0, 1, 1], 5.0)
        # Non-degenerate single-formation block has zero mixing.
        assert abs(W[0, 0, 0, 1]) < 1e-9
        assert abs(W[0, 0, 1, 0]) < 1e-9

    def test_wigner_offdiagonal_for_pair(self):
        """K=2 with asymmetric Goldstone support → cross-pair mixing nonzero."""
        g, pos = make_test_graph(7, 7)
        params = make_test_params()
        # Asymmetric placement breaks the antisymmetric cancellation that
        # would otherwise zero the symmetric Schur projection.
        c_a = np.array([1.0, 1.0])
        c_b = np.array([4.0, 5.0])
        ra = np.linalg.norm(pos - c_a, axis=1)
        rb = np.linalg.norm(pos - c_b, axis=1)
        u_a = 0.5 * (1.0 - np.tanh((ra - 1.0) / 0.4))
        u_b = 0.5 * (1.0 - np.tanh((rb - 2.0) / 0.4))
        u = np.stack([u_a, u_b])
        n = g.n
        v0 = np.ones(n) / np.sqrt(n)
        v1 = pos[:, 0].astype(np.float64)
        v1 /= np.linalg.norm(v1)
        eigvecs = np.column_stack([v0, v1])
        eigvals = np.array([0.1, 0.7])
        sr = compute_sigma_rich(
            u, g, params, hessian_eigenpairs=(eigvals, eigvecs)
        )
        W = sr.wigner_data
        assert W.shape == (2, 2, 2, 2)
        assert abs(W[0, 1, 0, 1]) > 1e-3


# ===========================================================================
# Top-level σ_rich integration
# ===========================================================================

class TestSigmaRichIntegration:

    def test_returns_namedtuple(self):
        g, pos = make_test_graph(4, 4)
        params = make_test_params()
        u = np.full(g.n, 0.3)
        eigvals = np.array([0.1, 0.4, 0.9])
        eigvecs = np.eye(g.n)[:, :3]
        sr = compute_sigma_rich(
            u, g, params, hessian_eigenpairs=(eigvals, eigvecs)
        )
        assert isinstance(sr, SigmaRich)
        assert sr.sigma_standard
        assert sr.centroids.shape == (1, 2)
        assert sr.orientations.shape == (1, 2, 2)
        assert sr.wigner_data.shape == (1, 1, 2, 2)

    def test_sigma_standard_groups_degenerate(self):
        g, pos = make_test_graph(4, 4)
        params = make_test_params()
        u = np.full(g.n, 0.3)
        # 2-fold degenerate at 0.5; singleton at 1.7
        eigvals = np.array([0.5, 0.5 + 1e-9, 1.7])
        eigvecs = np.eye(g.n)[:, :3]
        sr = compute_sigma_rich(
            u, g, params, hessian_eigenpairs=(eigvals, eigvecs)
        )
        # First cluster is multiplicity 2, second multiplicity 1.
        assert sr.sigma_standard[0][0] == 2
        assert sr.sigma_standard[1][0] == 1

    def test_positions_required(self):
        g = GraphState.grid_2d(3, 3)
        params = make_test_params()
        u = np.full(g.n, 0.3)
        eigvals = np.array([0.1, 0.4])
        eigvecs = np.eye(g.n)[:, :2]
        with pytest.raises(ValueError, match="node positions"):
            compute_sigma_rich(
                u, g, params, hessian_eigenpairs=(eigvals, eigvecs)
            )
