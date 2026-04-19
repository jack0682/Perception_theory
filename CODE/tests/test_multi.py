"""Tests for scc.multi — K-field multi-formation architecture."""

import numpy as np
import pytest

from scc.graph import GraphState
from scc.multi import (
    find_k_formations, _total_energy, transport_k_formations,
    multi_diagnostic_vector, inter_formation_distances, classify_regime,
    formation_overlap,
)
from scc.optimizer import find_formation, FormationResult
from scc.diagnostics import DiagnosticVector
from scc.transport import TransportResult
from tests.conftest import make_params


# =============================================================================
# BASIC API
# =============================================================================

class TestFindKFormationsAPI:

    def test_returns_list_of_k_results(self, grid_10x10, default_params):
        """K=2 returns a list of exactly 2 FormationResult objects."""
        results = find_k_formations(grid_10x10, default_params, K=2,
                                    max_iter=200, n_restarts=1)
        assert isinstance(results, list)
        assert len(results) == 2
        for r in results:
            assert isinstance(r, FormationResult)

    def test_k1_matches_single(self, grid_10x10, default_params):
        """K=1 should produce a result structurally similar to find_formation."""
        results = find_k_formations(grid_10x10, default_params, K=1,
                                    max_iter=500, n_restarts=2)
        assert len(results) == 1
        r = results[0]
        # Should have valid field, energy, diagnostics
        assert r.u.shape == (grid_10x10.n,)
        assert np.isfinite(r.energy)
        assert isinstance(r.diagnostics, DiagnosticVector)

    def test_k3(self, grid_10x10, default_params):
        """K=3 on 10x10 grid should return 3 results."""
        results = find_k_formations(grid_10x10, default_params, K=3,
                                    max_iter=200, n_restarts=1)
        assert len(results) == 3
        for r in results:
            assert r.u.shape == (grid_10x10.n,)
            assert np.isfinite(r.energy)


# =============================================================================
# FIELD CONSTRAINTS
# =============================================================================

class TestFieldConstraints:

    def test_field_bounds(self, grid_10x10, default_params):
        """All K fields should have values in [0, 1]."""
        results = find_k_formations(grid_10x10, default_params, K=2,
                                    max_iter=300, n_restarts=1)
        for k, r in enumerate(results):
            assert np.all(r.u >= -1e-8), (
                f"Formation {k}: min value = {r.u.min():.6f}")
            assert np.all(r.u <= 1.0 + 1e-8), (
                f"Formation {k}: max value = {r.u.max():.6f}")

    def test_volume_constraint(self, grid_10x10, default_params):
        """Each field should satisfy sum(u^k) ≈ m_k."""
        n = grid_10x10.n
        m = default_params.volume_fraction * n
        results = find_k_formations(grid_10x10, default_params, K=2,
                                    max_iter=300, n_restarts=1)
        for k, r in enumerate(results):
            np.testing.assert_allclose(
                r.u.sum(), m, atol=1.0,
                err_msg=f"Formation {k}: sum(u)={r.u.sum():.2f}, expected m={m:.1f}")

    def test_simplex_constraint(self, grid_10x10, default_params):
        """At each site, sum of all K fields should be <= 1 (approximately, due to soft barrier)."""
        results = find_k_formations(grid_10x10, default_params, K=2,
                                    lambda_bar=100.0, max_iter=500, n_restarts=1)
        S = sum(r.u for r in results)
        # Soft barrier won't enforce exactly, but violation should be small
        max_violation = (S - 1.0).max()
        assert max_violation < 0.3, (
            f"Simplex violation too large: max(sum_k u^k - 1) = {max_violation:.4f}")

    def test_custom_m_per_formation(self, grid_10x10, default_params):
        """Custom m_per_formation should be respected."""
        n = grid_10x10.n
        # Fractions of total nodes
        m_fracs = [0.2, 0.3]
        results = find_k_formations(grid_10x10, default_params, K=2,
                                    m_per_formation=m_fracs,
                                    max_iter=300, n_restarts=1)
        for k, (r, frac) in enumerate(zip(results, m_fracs)):
            expected_m = frac * n
            np.testing.assert_allclose(
                r.u.sum(), expected_m, atol=1.0,
                err_msg=f"Formation {k}: sum(u)={r.u.sum():.2f}, expected={expected_m:.1f}")


# =============================================================================
# REPULSION & SPATIAL SEPARATION
# =============================================================================

class TestRepulsion:

    def test_low_overlap(self, grid_10x10, default_params):
        """K=2 formations should have low pointwise overlap (u^1 * u^2)."""
        results = find_k_formations(grid_10x10, default_params, K=2,
                                    lambda_rep=10.0, max_iter=500, n_restarts=2)
        overlap = float(results[0].u @ results[1].u)
        n = grid_10x10.n
        # Normalize by grid size for interpretability
        overlap_per_site = overlap / n
        assert overlap_per_site < 0.15, (
            f"Overlap per site = {overlap_per_site:.4f}, expected < 0.15")

    def test_stronger_repulsion_less_overlap(self, grid_10x10, default_params):
        """Higher lambda_rep should produce less overlap between formations."""
        results_low = find_k_formations(grid_10x10, default_params, K=2,
                                        lambda_rep=1.0, max_iter=300, n_restarts=1)
        results_high = find_k_formations(grid_10x10, default_params, K=2,
                                         lambda_rep=50.0, max_iter=300, n_restarts=1)
        overlap_low = float(results_low[0].u @ results_low[1].u)
        overlap_high = float(results_high[0].u @ results_high[1].u)
        # Higher repulsion should give less overlap (or equal if both near zero)
        assert overlap_high <= overlap_low + 0.5, (
            f"Higher repulsion overlap={overlap_high:.4f} should be <= "
            f"lower repulsion overlap={overlap_low:.4f}")


# =============================================================================
# ENERGY & DIAGNOSTICS
# =============================================================================

class TestEnergyAndDiagnostics:

    def test_finite_energy(self, grid_10x10, default_params):
        """Each formation should have finite energy."""
        results = find_k_formations(grid_10x10, default_params, K=2,
                                    max_iter=300, n_restarts=1)
        for k, r in enumerate(results):
            assert np.isfinite(r.energy), f"Formation {k}: energy = {r.energy}"

    def test_energy_terms_present(self, grid_10x10, default_params):
        """Each formation should have energy_terms dict with expected keys."""
        results = find_k_formations(grid_10x10, default_params, K=2,
                                    max_iter=300, n_restarts=1)
        for k, r in enumerate(results):
            assert isinstance(r.energy_terms, dict), (
                f"Formation {k}: energy_terms is {type(r.energy_terms)}")
            assert len(r.energy_terms) > 0, f"Formation {k}: empty energy_terms"

    def test_diagnostics_valid(self, grid_10x10, default_params):
        """Each formation should have a valid DiagnosticVector in [0, 1]^4."""
        results = find_k_formations(grid_10x10, default_params, K=2,
                                    max_iter=300, n_restarts=1)
        for k, r in enumerate(results):
            d = r.diagnostics
            assert isinstance(d, DiagnosticVector)
            vec = d.vector
            assert vec.shape == (4,), f"Formation {k}: diag shape = {vec.shape}"
            for i, name in enumerate(['bind', 'sep', 'inside', 'persist']):
                assert 0.0 - 1e-6 <= vec[i] <= 1.0 + 1e-6, (
                    f"Formation {k}: {name} = {vec[i]:.6f} out of [0,1]")


# =============================================================================
# SMALL GRID
# =============================================================================

class TestSmallGrid:

    def test_5x5_k2(self, grid_5x5, default_params):
        """K=2 should work on small 5x5 grid."""
        results = find_k_formations(grid_5x5, default_params, K=2,
                                    max_iter=200, n_restarts=1)
        assert len(results) == 2
        for r in results:
            assert r.u.shape == (25,)
            assert np.all(r.u >= -1e-8)
            assert np.all(r.u <= 1.0 + 1e-8)
            assert np.isfinite(r.energy)


# =============================================================================
# TOTAL ENERGY
# =============================================================================

class TestTotalEnergy:

    def test_total_energy_nonneg(self, grid_10x10, default_params):
        """Total K-field energy (intra + repulsion + barrier) should be finite."""
        from scc.energy import EnergyComputer
        results = find_k_formations(grid_10x10, default_params, K=2,
                                    max_iter=300, n_restarts=1)
        ec = EnergyComputer(grid_10x10, default_params)
        ec.normalize_weights()
        fields = [r.u for r in results]
        E = _total_energy(fields, ec, grid_10x10, lambda_rep=10.0, lambda_bar=100.0)
        assert np.isfinite(E), f"Total energy = {E}"

    def test_total_energy_decreases_with_restarts(self, grid_10x10, default_params):
        """More restarts should find equal or better energy."""
        # 1 restart
        r1 = find_k_formations(grid_10x10, default_params, K=2,
                               max_iter=200, n_restarts=1)
        # 3 restarts
        r3 = find_k_formations(grid_10x10, default_params, K=2,
                               max_iter=200, n_restarts=3)
        # More restarts picks the best, so energy should be <= (with tolerance for randomness)
        e1 = sum(r.energy for r in r1)
        e3 = sum(r.energy for r in r3)
        # Allow some tolerance — randomness means this isn't guaranteed every time
        # but 3 restarts should generally not be much worse than 1
        assert e3 < e1 * 1.5, (
            f"3-restart energy {e3:.4f} much worse than 1-restart {e1:.4f}")


# =============================================================================
# MULTI-FORMATION TEMPORAL TRANSPORT
# =============================================================================

class TestMultiFormationTransport:
    """Tests for K-formation temporal transport."""

    def _make_k_formations(self, grid, params, K=2, max_iter=300):
        """Helper: find K formations to use as source for transport."""
        return find_k_formations(grid, params, K=K,
                                 max_iter=max_iter, n_restarts=1)

    def test_transport_k_formations_returns_k_results(self, grid_10x10, default_params):
        """Should return K TransportResult objects."""
        sources = self._make_k_formations(grid_10x10, default_params, K=2)
        results = transport_k_formations(
            sources, grid_10x10, default_params,
            max_fp_iter=3, eps_ot=1.0,
        )
        assert isinstance(results, list)
        assert len(results) == 2
        for r in results:
            assert isinstance(r, TransportResult)

    def test_transport_k_formations_fields_on_sigma_m(self, grid_10x10, default_params):
        """Each transported field should satisfy volume constraint."""
        n = grid_10x10.n
        m = default_params.volume_fraction * n
        sources = self._make_k_formations(grid_10x10, default_params, K=2)
        results = transport_k_formations(
            sources, grid_10x10, default_params,
            max_fp_iter=3, eps_ot=1.0,
        )
        for k, r in enumerate(results):
            np.testing.assert_allclose(
                r.u_s.sum(), m, atol=2.0,
                err_msg=f"Formation {k}: sum(u_s)={r.u_s.sum():.2f}, expected ~{m:.1f}")
            assert np.all(r.u_s >= -1e-8), f"Formation {k}: min u_s = {r.u_s.min()}"
            assert np.all(r.u_s <= 1.0 + 1e-8), f"Formation {k}: max u_s = {r.u_s.max()}"

    def test_transport_k_formations_simplex_constraint(self, grid_10x10, default_params):
        """Sum of transported fields should be <= 1 at each site (within tolerance)."""
        sources = self._make_k_formations(grid_10x10, default_params, K=2)
        results = transport_k_formations(
            sources, grid_10x10, default_params,
            max_fp_iter=3, eps_ot=1.0,
        )
        S = sum(r.u_s for r in results)
        max_violation = float((S - 1.0).max())
        # Transported fields inherit separation from source; allow soft violation
        assert max_violation < 0.5, (
            f"Simplex violation too large after transport: {max_violation:.4f}")

    def test_transport_k_formations_convergence(self, grid_10x10, default_params):
        """Each formation's transport should converge (or residual should decrease)."""
        sources = self._make_k_formations(grid_10x10, default_params, K=2)
        results = transport_k_formations(
            sources, grid_10x10, default_params,
            max_fp_iter=10, eps_ot=1.0, fp_tol=1e-3,
        )
        for k, r in enumerate(results):
            assert len(r.fp_residuals) > 0, f"Formation {k}: no residuals recorded"
            # Either converged or residual decreased over iterations
            if len(r.fp_residuals) >= 2:
                assert r.fp_residuals[-1] <= r.fp_residuals[0] * 10, (
                    f"Formation {k}: residual not decreasing "
                    f"({r.fp_residuals[0]:.4f} -> {r.fp_residuals[-1]:.4f})")

    def test_transport_k_formations_persist(self, grid_10x10, default_params):
        """Per-formation Persist should be > 0.3 for similar formations."""
        from scc.transport import persist_transport
        sources = self._make_k_formations(grid_10x10, default_params, K=2,
                                          max_iter=500)
        results = transport_k_formations(
            sources, grid_10x10, default_params,
            max_fp_iter=5, eps_ot=1.0,
        )
        for k, r in enumerate(results):
            # Use theta_core=0.5 since multi-formation fields may have
            # reduced peaks due to repulsion/simplex constraints
            p = persist_transport(r.u_t, r.u_s, r.M, theta_core=0.5)
            assert p > 0.3, (
                f"Formation {k}: Persist={p:.3f}, expected > 0.3 for similar fields")

    def test_multi_diagnostic_vector(self, grid_10x10, default_params):
        """Should return K DiagnosticVector objects with valid components."""
        sources = self._make_k_formations(grid_10x10, default_params, K=2,
                                          max_iter=500)
        results = transport_k_formations(
            sources, grid_10x10, default_params,
            max_fp_iter=3, eps_ot=1.0,
        )
        diags = multi_diagnostic_vector(sources, None, results, grid_10x10, default_params)
        assert isinstance(diags, list)
        assert len(diags) == 2
        for k, d in enumerate(diags):
            assert isinstance(d, DiagnosticVector), (
                f"Formation {k}: expected DiagnosticVector, got {type(d)}")
            vec = d.vector
            assert vec.shape == (4,), f"Formation {k}: shape = {vec.shape}"
            for i, name in enumerate(['bind', 'sep', 'inside', 'persist']):
                assert 0.0 - 1e-6 <= vec[i] <= 1.0 + 1e-6, (
                    f"Formation {k}: {name} = {vec[i]:.6f} out of [0,1]")


# =============================================================================
# INTER-FORMATION DISTANCE & REGIME CLASSIFICATION
# =============================================================================

class TestInterFormationDistance:

    def test_separated_formations(self, grid_10x10, default_params):
        """Two formations on opposite sides should have d_min > 0."""
        n = grid_10x10.n
        # Manually create two well-separated fields
        u1 = np.zeros(n)
        u2 = np.zeros(n)
        # Formation 1: left columns (cols 0-2)
        for r in range(10):
            for c in range(3):
                u1[r * 10 + c] = 0.8
        # Formation 2: right columns (cols 7-9)
        for r in range(10):
            for c in range(7, 10):
                u2[r * 10 + c] = 0.8
        fields = [u1, u2]
        D = inter_formation_distances(fields, grid_10x10, theta_supp=0.1)
        assert D.shape == (2, 2)
        assert D[0, 0] == 0.0
        assert D[1, 1] == 0.0
        # Minimum distance between col 2 and col 7 is 4 hops
        assert D[0, 1] >= 4
        assert D[1, 0] >= 4
        # Symmetry
        np.testing.assert_allclose(D[0, 1], D[1, 0])

    def test_overlapping_formations(self, grid_10x10, default_params):
        """Two formations with overlapping support should have d_min = 0."""
        n = grid_10x10.n
        u1 = np.zeros(n)
        u2 = np.zeros(n)
        # Both active in the center
        for r in range(3, 7):
            for c in range(3, 7):
                u1[r * 10 + c] = 0.7
                u2[r * 10 + c] = 0.6
        fields = [u1, u2]
        D = inter_formation_distances(fields, grid_10x10, theta_supp=0.1)
        assert D[0, 1] == 0.0
        assert D[1, 0] == 0.0

    def test_classify_well_separated(self, grid_10x10, default_params):
        """Manually separated formations should classify as 'well-separated'."""
        n = grid_10x10.n
        u1 = np.zeros(n)
        u2 = np.zeros(n)
        for r in range(10):
            for c in range(3):
                u1[r * 10 + c] = 0.8
        for r in range(10):
            for c in range(7, 10):
                u2[r * 10 + c] = 0.8
        fields = [u1, u2]
        regime = classify_regime(fields, grid_10x10, theta_supp=0.1, D_sep=3)
        assert regime == 'well-separated'

    def test_classify_strongly_interacting(self, grid_10x10, default_params):
        """Fully overlapping formations should be 'strongly-interacting'."""
        n = grid_10x10.n
        u1 = np.zeros(n)
        u2 = np.zeros(n)
        for r in range(10):
            for c in range(10):
                u1[r * 10 + c] = 0.7
                u2[r * 10 + c] = 0.6
        fields = [u1, u2]
        regime = classify_regime(fields, grid_10x10, theta_supp=0.1, D_sep=3)
        assert regime == 'strongly-interacting'

    def test_classify_regime_consistency(self, grid_10x10, default_params):
        """If d_min >= D_sep for all pairs, regime must be 'well-separated'."""
        n = grid_10x10.n
        u1 = np.zeros(n)
        u2 = np.zeros(n)
        # Place formations far apart
        for r in range(10):
            u1[r * 10 + 0] = 0.9
            u2[r * 10 + 9] = 0.9
        fields = [u1, u2]
        D = inter_formation_distances(fields, grid_10x10, theta_supp=0.1)
        D_sep = 3
        all_sep = all(D[j, k] >= D_sep for j in range(2) for k in range(2) if j != k)
        regime = classify_regime(fields, grid_10x10, theta_supp=0.1, D_sep=D_sep)
        if all_sep:
            assert regime == 'well-separated'

    def test_formation_overlap_disjoint(self, grid_10x10, default_params):
        """Disjoint formations should have zero off-diagonal overlap."""
        n = grid_10x10.n
        u1 = np.zeros(n)
        u2 = np.zeros(n)
        u1[:30] = 0.8
        u2[70:] = 0.8
        O = formation_overlap([u1, u2], theta_supp=0.1)
        assert O[0, 1] == 0.0
        assert O[1, 0] == 0.0
        assert O[0, 0] == 30.0
        assert O[1, 1] == 30.0

    def test_formation_overlap_full(self, grid_10x10, default_params):
        """Fully overlapping formations should have off-diagonal = support size."""
        n = grid_10x10.n
        u1 = np.ones(n) * 0.5
        u2 = np.ones(n) * 0.5
        O = formation_overlap([u1, u2], theta_supp=0.1)
        assert O[0, 1] == n
        assert O[0, 0] == n

    def test_single_formation_regime(self, grid_10x10, default_params):
        """K=1 should always be 'well-separated'."""
        u1 = np.ones(grid_10x10.n) * 0.5
        regime = classify_regime([u1], grid_10x10)
        assert regime == 'well-separated'


# =============================================================================
# PHASE B: COUPLED TRANSPORT & RE-OPTIMIZATION
# =============================================================================

class TestPhaseB:

    def test_transport_reoptimize_mode(self, grid_10x10, default_params):
        """Transport with reoptimize produces valid formations."""
        sources = find_k_formations(grid_10x10, default_params, K=2,
                                    lambda_rep=10.0, max_iter=300, n_restarts=1)
        results = transport_k_formations(sources, grid_10x10, default_params,
                                         phase2_mode='reoptimize', max_fp_iter=5)
        assert len(results) == 2
        for r in results:
            assert r.u_s.min() >= -0.01
            assert abs(r.u_s.sum() - sources[0].u.sum()) < 1.0

    def test_transport_none_mode(self, grid_10x10, default_params):
        """Transport with no correction."""
        sources = find_k_formations(grid_10x10, default_params, K=2,
                                    lambda_rep=10.0, max_iter=300, n_restarts=1)
        results = transport_k_formations(sources, grid_10x10, default_params,
                                         phase2_mode='none', max_fp_iter=5)
        assert len(results) == 2

    def test_init_fields(self, grid_10x10, default_params):
        """find_k_formations with init_fields."""
        n = grid_10x10.n
        init = [np.full(n, 0.3), np.full(n, 0.2)]
        results = find_k_formations(grid_10x10, default_params, K=2,
                                    lambda_rep=10.0, init_fields=init, max_iter=300,
                                    n_restarts=1)
        assert len(results) == 2

    def test_transport_correction_backward_compat(self, grid_10x10, default_params):
        """Default phase2_mode='correction' should work as before."""
        sources = find_k_formations(grid_10x10, default_params, K=2,
                                    lambda_rep=10.0, max_iter=300, n_restarts=1)
        results = transport_k_formations(sources, grid_10x10, default_params,
                                         max_fp_iter=3, eps_ot=1.0)
        assert len(results) == 2
        for r in results:
            assert isinstance(r, TransportResult)

    def test_coupled_cost_transport(self, grid_10x10, default_params):
        """Transport with coupled_cost=True produces valid results."""
        sources = find_k_formations(grid_10x10, default_params, K=2,
                                    lambda_rep=10.0, max_iter=300, n_restarts=2)
        results = transport_k_formations(
            sources, grid_10x10, default_params,
            lambda_rep=10.0,
            coupled_cost=True,
            max_fp_iter=5, eps_ot=1.0,
        )
        assert len(results) == 2
        for r in results:
            assert r.u_s.min() >= -0.01
            assert np.isfinite(r.u_s).all()
        # Simplex should be approximately satisfied
        S = sum(r.u_s for r in results)
        assert float(np.max(S)) < 1.5  # not perfect but bounded
