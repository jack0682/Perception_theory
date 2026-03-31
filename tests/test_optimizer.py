"""Tests for scc.optimizer — formation finding and projected gradient descent."""

import numpy as np
import pytest

from scc.graph import GraphState
from scc.optimizer import find_formation, FormationResult, project_volume
from scc.energy import EnergyComputer
from scc.diagnostics import DiagnosticVector
from tests.conftest import make_params


# =============================================================================
# BASIC SMOKE TEST
# =============================================================================


class TestFindFormationBasic:

    def test_find_formation_returns_result(self, grid_5x5, default_params):
        """Basic smoke test — returns FormationResult with all fields."""
        result = find_formation(grid_5x5, default_params)
        assert isinstance(result, FormationResult)
        assert isinstance(result.u, np.ndarray)
        assert isinstance(result.energy, float)
        assert isinstance(result.energy_terms, dict)
        assert isinstance(result.diagnostics, DiagnosticVector)
        assert isinstance(result.converged, bool)
        assert isinstance(result.n_iter, int)
        assert isinstance(result.energy_history, list)
        assert isinstance(result.grad_norm_history, list)

    def test_find_formation_on_sigma_m(self, grid_5x5, default_params):
        """Result u satisfies sum(u) ≈ m, 0 ≤ u ≤ 1."""
        result = find_formation(grid_5x5, default_params)
        u = result.u
        n = grid_5x5.n
        c = default_params.volume_fraction
        m = c * n

        assert np.all(u >= -1e-10), "u has negative entries"
        assert np.all(u <= 1.0 + 1e-10), "u exceeds 1"
        np.testing.assert_allclose(np.sum(u), m, atol=1e-6,
            err_msg="Volume constraint violated")

    def test_find_formation_energy_decreases(self, grid_5x5, default_params):
        """Final energy ≤ initial uniform field energy."""
        result = find_formation(grid_5x5, default_params)

        # Compute energy of uniform field at volume fraction c
        ec = EnergyComputer(grid_5x5, default_params)
        u_uniform = np.full(grid_5x5.n, default_params.volume_fraction)
        E_uniform, _ = ec.energy(u_uniform)

        assert result.energy <= E_uniform + 1e-8, (
            f"Final energy {result.energy:.6f} > uniform energy {E_uniform:.6f}")

    def test_find_formation_convergence(self, grid_5x5):
        """Result converged flag is True on easy case (small grid)."""
        params = make_params()
        result = find_formation(grid_5x5, params)
        assert result.converged, (
            f"Failed to converge on 5x5 grid after {result.n_iter} iterations")

    def test_find_formation_diagnostics(self, grid_10x10, default_params):
        """Diagnostics vector has 4 components in [0,1]."""
        result = find_formation(grid_10x10, default_params)
        diag = result.diagnostics
        vec = diag.vector

        assert vec.shape == (4,), f"Expected 4 components, got {vec.shape}"
        assert np.all(vec >= -1e-10), f"Diagnostic component < 0: {vec}"
        assert np.all(vec <= 1.0 + 1e-10), f"Diagnostic component > 1: {vec}"


# =============================================================================
# DETERMINISM AND REPRODUCIBILITY
# =============================================================================


class TestFindFormationDeterminism:

    def test_find_formation_deterministic(self, grid_10x10, default_params):
        """Same parameters → same energy and field-value distribution.

        Multi-start may converge to spatially mirrored/rotated minima,
        so we compare energies and sorted field values rather than
        element-wise field equality.
        """
        r1 = find_formation(grid_10x10, default_params)
        r2 = find_formation(grid_10x10, default_params)

        np.testing.assert_allclose(r1.energy, r2.energy, atol=1e-6,
            err_msg="Same inputs produced different energies")
        np.testing.assert_allclose(
            np.sort(r1.u), np.sort(r2.u), atol=0.01,
            err_msg="Same inputs produced different field-value distributions")


# =============================================================================
# u_init MODE
# =============================================================================


class TestFindFormationUInit:

    def test_find_formation_u_init(self, grid_10x10, default_params):
        """When u_init provided, skips multi-start; result near u_init basin."""
        n = grid_10x10.n
        # Create a localized initial field (left half high, right half low)
        u_init = np.zeros(n)
        size = 10
        for i in range(size):
            for j in range(size):
                u_init[i * size + j] = 0.9 if j < size // 2 else 0.1

        result = find_formation(grid_10x10, default_params, u_init=u_init)

        # The optimized field should still have higher mass on the left
        left_mass = sum(result.u[i * size + j] for i in range(size) for j in range(size // 2))
        right_mass = sum(result.u[i * size + j] for i in range(size) for j in range(size // 2, size))
        assert left_mass > right_mass, "u_init basin not preserved"

    def test_find_formation_u_init_preserves_volume(self, grid_10x10, default_params):
        """u_init mode still satisfies volume constraint."""
        n = grid_10x10.n
        rng = np.random.RandomState(123)
        u_init = rng.uniform(0.2, 0.8, n)

        result = find_formation(grid_10x10, default_params, u_init=u_init)
        m = default_params.volume_fraction * n

        assert np.all(result.u >= -1e-10)
        assert np.all(result.u <= 1.0 + 1e-10)
        np.testing.assert_allclose(np.sum(result.u), m, atol=1e-6,
            err_msg="Volume constraint violated in u_init mode")


# =============================================================================
# VOLUME FRACTION VARIATION
# =============================================================================


class TestFindFormationVolume:

    @pytest.mark.parametrize("vf", [0.3, 0.5, 0.7])
    def test_find_formation_different_volumes(self, grid_10x10, vf):
        """Different volume_fraction → different mass."""
        params = make_params(volume_fraction=vf)
        result = find_formation(grid_10x10, params)
        m_expected = vf * grid_10x10.n

        np.testing.assert_allclose(np.sum(result.u), m_expected, atol=1e-6,
            err_msg=f"Volume constraint violated for vf={vf}")


# =============================================================================
# PHASE TRANSITION
# =============================================================================


class TestPhaseTransition:

    def test_find_formation_phase_transition(self, grid_10x10):
        """Above critical β, field should be non-trivial (not uniform)."""
        # High β drives double-well separation → non-uniform field
        params = make_params(beta_bd=50.0, alpha_bd=0.1)
        result = find_formation(grid_10x10, params)

        # Non-trivial means u is not approximately constant
        u_std = np.std(result.u)
        assert u_std > 0.01, (
            f"Field is nearly uniform (std={u_std:.6f}) despite high β")


# =============================================================================
# FormationResult STRUCTURE
# =============================================================================


class TestFormationResultFields:

    def test_formation_result_fields(self, grid_5x5):
        """FormationResult has u, energy, diagnostics, converged."""
        params = make_params()
        result = find_formation(grid_5x5, params)

        assert hasattr(result, 'u')
        assert hasattr(result, 'energy')
        assert hasattr(result, 'diagnostics')
        assert hasattr(result, 'converged')
        assert hasattr(result, 'energy_terms')
        assert hasattr(result, 'n_iter')
        assert hasattr(result, 'energy_history')
        assert hasattr(result, 'grad_norm_history')

        # energy_terms should contain the three components
        assert 'E_cl' in result.energy_terms
        assert 'E_sep' in result.energy_terms
        assert 'E_bd' in result.energy_terms

        # History lists should be non-empty
        assert len(result.energy_history) > 0
        assert len(result.grad_norm_history) > 0


# =============================================================================
# EDGE CASES
# =============================================================================


class TestFindFormationEdgeCases:

    def test_find_formation_small_grid(self):
        """Works on 3x3 grid (edge case)."""
        grid = GraphState.grid_2d(3, 3)
        params = make_params()
        result = find_formation(grid, params)

        assert isinstance(result, FormationResult)
        n = grid.n
        m = params.volume_fraction * n
        np.testing.assert_allclose(np.sum(result.u), m, atol=1e-6)
        assert np.all(result.u >= -1e-10)
        assert np.all(result.u <= 1.0 + 1e-10)


# =============================================================================
# PROJECT_VOLUME UNIT TESTS
# =============================================================================


class TestProjectVolume:

    def test_preserves_feasibility(self, rng):
        """Projection lands in [0,1]^n with sum = m."""
        n = 25
        u = rng.standard_normal(n) * 2  # wild values
        m = 10.0
        v = project_volume(u, m)

        assert np.all(v >= -1e-12)
        assert np.all(v <= 1.0 + 1e-12)
        np.testing.assert_allclose(np.sum(v), m, atol=1e-10)

    def test_already_feasible(self):
        """If u is already feasible, projection is (near) identity."""
        u = np.array([0.4, 0.6, 0.5, 0.5])
        m = 2.0  # sum(u) = 2.0
        v = project_volume(u, m)
        np.testing.assert_allclose(v, u, atol=1e-10)

    def test_empty(self):
        """Empty array edge case."""
        v = project_volume(np.array([]), 0.0)
        assert len(v) == 0
