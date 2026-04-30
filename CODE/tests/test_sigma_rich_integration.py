"""Integration tests for σ_rich through the find_formation pipeline.

End-to-end check that compute_sigma_rich is well-defined on the actual
output of the SCC optimizer (single- and multi-formation), per
THEORY/working/MF/sigma_rich_augmentation.md §6.3.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import pytest

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.multi import find_k_formations
from scc.sigma_rich import SigmaRich, compute_sigma_rich


def grid_positions(rows: int, cols: int) -> np.ndarray:
    return np.array(
        [[r, c] for r in range(rows) for c in range(cols)],
        dtype=np.float64,
    )


def make_grid_with_positions(rows: int, cols: int) -> GraphState:
    g = GraphState.grid_2d(rows, cols)
    g.positions = grid_positions(rows, cols)
    return g


@pytest.fixture
def integration_params() -> ParameterRegistry:
    return ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=10.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.5,
    )


# ===========================================================================
# Single-formation pipeline
# ===========================================================================

class TestSingleFormationPipeline:

    def test_sigma_rich_on_find_formation_output(self, integration_params):
        """find_formation → compute_sigma_rich runs and returns valid shapes."""
        g = make_grid_with_positions(8, 8)
        result = find_formation(g, integration_params, verbose=False)
        # Inject Hessian eigenpairs to skip the FD Hessian (kept fast).
        eigvals = np.array([0.05, 0.4, 1.2, 3.0])
        eigvecs = np.eye(g.n)[:, :4]
        sr = compute_sigma_rich(
            result.u, g, integration_params,
            hessian_eigenpairs=(eigvals, eigvecs),
        )
        assert isinstance(sr, SigmaRich)
        assert sr.centroids.shape == (1, 2)
        assert sr.orientations.shape == (1, 2, 2)
        assert sr.wigner_data.shape == (1, 1, 2, 2)
        assert np.all(np.isfinite(sr.centroids))
        assert np.all(np.isfinite(sr.orientations))
        assert np.all(np.isfinite(sr.wigner_data))

    def test_centroid_inside_grid(self, integration_params):
        """Optimized formation centroid sits inside the grid bounding box."""
        rows, cols = 10, 10
        g = make_grid_with_positions(rows, cols)
        result = find_formation(g, integration_params, verbose=False)
        eigvals = np.array([0.1, 0.5, 1.0])
        eigvecs = np.eye(g.n)[:, :3]
        sr = compute_sigma_rich(
            result.u, g, integration_params,
            hessian_eigenpairs=(eigvals, eigvecs),
        )
        c = sr.centroids[0]
        assert 0.0 <= c[0] <= rows - 1
        assert 0.0 <= c[1] <= cols - 1

    def test_orientation_psd(self, integration_params):
        """Inertia tensor is positive-semidefinite for a real formation."""
        g = make_grid_with_positions(8, 8)
        result = find_formation(g, integration_params, verbose=False)
        eigvals = np.array([0.1, 0.5, 1.0])
        eigvecs = np.eye(g.n)[:, :3]
        sr = compute_sigma_rich(
            result.u, g, integration_params,
            hessian_eigenpairs=(eigvals, eigvecs),
        )
        evals = np.linalg.eigvalsh(sr.orientations[0])
        assert np.all(evals >= -1e-9), f"non-PSD orientation: {evals}"


# ===========================================================================
# Multi-formation pipeline
# ===========================================================================

class TestMultiFormationPipeline:

    def test_sigma_rich_on_k_formations(self, integration_params):
        """find_k_formations → compute_sigma_rich on stacked K-field state."""
        g = make_grid_with_positions(10, 10)
        K = 2
        results = find_k_formations(
            g, integration_params, K=K,
            max_iter=300, n_restarts=1,
        )
        u_field = np.stack([r.u for r in results])
        eigvals = np.array([0.05, 0.4, 1.2, 3.0])
        eigvecs = np.eye(g.n)[:, :4]
        sr = compute_sigma_rich(
            u_field, g, integration_params,
            hessian_eigenpairs=(eigvals, eigvecs),
        )
        assert sr.centroids.shape == (K, 2)
        assert sr.orientations.shape == (K, 2, 2)
        assert sr.wigner_data.shape == (K, K, 2, 2)
        assert np.all(np.isfinite(sr.centroids))
        # K=2 distinct formations → centroids should be separated.
        sep = np.linalg.norm(sr.centroids[0] - sr.centroids[1])
        assert sep > 0.5, f"K=2 centroids collapsed: sep={sep:.3f}"

    def test_wigner_block_symmetry(self, integration_params):
        """W[j,k] is symmetric in (j,k) at the matrix level (real Schur form)."""
        g = make_grid_with_positions(8, 8)
        results = find_k_formations(
            g, integration_params, K=2, max_iter=200, n_restarts=1,
        )
        u_field = np.stack([r.u for r in results])
        eigvals = np.array([0.1, 0.5, 1.0])
        eigvecs = np.eye(g.n)[:, :3]
        sr = compute_sigma_rich(
            u_field, g, integration_params,
            hessian_eigenpairs=(eigvals, eigvecs),
        )
        # Off-diagonal blocks should match by construction (symmetric mix).
        np.testing.assert_allclose(
            sr.wigner_data[0, 1], sr.wigner_data[1, 0], atol=1e-9,
        )
