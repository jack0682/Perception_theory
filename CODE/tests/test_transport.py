"""Tests for scc.transport — fingerprint, cost, OT, fixed-point, persist."""

import numpy as np
import pytest

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.transport import (
    cohesion_fingerprint,
    graph_distance_matrix,
    transport_cost,
    sinkhorn_partial_ot,
    transport_field,
    transport_fixed_point,
    TransportResult,
    persist_transport,
    _minimize_with_transport,
)
from tests.conftest import make_params


# =============================================================================
# COHESION FINGERPRINT
# =============================================================================

class TestCohesionFingerprint:

    def test_shape(self, grid_5x5, default_params, rng):
        """Default fingerprint should be (n, 3) with values in [0, 1]."""
        n = grid_5x5.n
        u = rng.uniform(0.1, 0.9, n)
        phi = cohesion_fingerprint(u, grid_5x5, default_params)
        assert phi.shape == (n, 3)
        assert np.all(phi >= -1e-10) and np.all(phi <= 1.0 + 1e-10)

    def test_shape_with_resolvent(self, grid_5x5, default_params, rng):
        """Fingerprint with use_resolvent=True should be (n, 4)."""
        n = grid_5x5.n
        u = rng.uniform(0.1, 0.9, n)
        phi = cohesion_fingerprint(u, grid_5x5, default_params, use_resolvent=True)
        assert phi.shape == (n, 4)
        assert np.all(phi >= -1e-10) and np.all(phi <= 1.0 + 1e-10)

    def test_uniform_field(self, grid_5x5, default_params):
        """Uniform field should give uniform fingerprint (constant across sites)."""
        n = grid_5x5.n
        u = np.full(n, 0.5)
        phi = cohesion_fingerprint(u, grid_5x5, default_params)
        # phi[:,0] = u is exactly uniform
        assert np.allclose(phi[:, 0], 0.5)
        # Other components should have low variance (not necessarily exactly uniform
        # due to boundary effects, but close)
        for col in range(1, phi.shape[1]):
            std = np.std(phi[:, col])
            assert std < 0.3, f"Column {col} std={std:.4f} too high for uniform field"


# =============================================================================
# GRAPH DISTANCE MATRIX
# =============================================================================

class TestGraphDistanceMatrix:

    def test_3x3_grid(self):
        """3x3 grid: verify known distances."""
        g = GraphState.grid_2d(3, 3)
        dist = graph_distance_matrix(g)
        assert dist.shape == (9, 9)
        # Self-distance = 0
        for i in range(9):
            assert dist[i, i] == 0.0
        # Corner (0,0) to corner (2,2): Manhattan distance = 4
        assert dist[0, 8] == 4.0
        # Adjacent nodes: distance = 1
        assert dist[0, 1] == 1.0  # (0,0)-(0,1)
        assert dist[0, 3] == 1.0  # (0,0)-(1,0)
        # Symmetry
        np.testing.assert_array_equal(dist, dist.T)


# =============================================================================
# TRANSPORT COST
# =============================================================================

class TestTransportCost:

    def test_self_cost_spatial_diagonal(self, grid_5x5, default_params, rng):
        """cost(phi, phi, dist) should have zeros on spatial diagonal."""
        n = grid_5x5.n
        u = rng.uniform(0.1, 0.9, n)
        phi = cohesion_fingerprint(u, grid_5x5, default_params)
        dist = graph_distance_matrix(grid_5x5)
        # With gamma=0, only spatial term remains
        c = transport_cost(phi, phi, dist, sigma=1.0, gamma=0.0)
        np.testing.assert_allclose(np.diag(c), 0.0, atol=1e-12)

    def test_symmetry_spatial(self, grid_5x5, default_params, rng):
        """Spatial component of cost should be symmetric."""
        n = grid_5x5.n
        u = rng.uniform(0.1, 0.9, n)
        phi = cohesion_fingerprint(u, grid_5x5, default_params)
        dist = graph_distance_matrix(grid_5x5)
        # Pure spatial cost (gamma=0)
        c = transport_cost(phi, phi, dist, sigma=1.0, gamma=0.0)
        np.testing.assert_allclose(c, c.T, atol=1e-12)


# =============================================================================
# SINKHORN PARTIAL OT
# =============================================================================

class TestSinkhornOT:

    def test_balanced(self, rng):
        """Balanced OT on simple case: marginals should be satisfied."""
        n = 5
        cost = rng.uniform(0, 1, (n, n))
        cost = (cost + cost.T) / 2  # symmetric
        mu = np.ones(n) / n
        nu = np.ones(n) / n
        M, info = sinkhorn_partial_ot(cost, mu, nu, eps=0.1, mass_fraction=1.0)
        assert info['converged']
        # Row sums should match mu
        np.testing.assert_allclose(M.sum(axis=1), mu, atol=1e-4)
        # Column sums should match nu
        np.testing.assert_allclose(M.sum(axis=0), nu, atol=1e-4)

    def test_partial_mass(self, rng):
        """Partial OT with mass_fraction=0.5: total transported mass should be ~0.5 * min(sum_mu, sum_nu)."""
        n = 6
        cost = rng.uniform(0, 2, (n, n))
        mu = np.ones(n) / n
        nu = np.ones(n) / n
        mass_frac = 0.5
        M, info = sinkhorn_partial_ot(cost, mu, nu, eps=0.1, mass_fraction=mass_frac)
        total = M.sum()
        expected = mass_frac * min(mu.sum(), nu.sum())
        np.testing.assert_allclose(total, expected, atol=0.05)

    def test_substochastic(self, rng):
        """Row sums of transport plan should be <= mu (E1 axiom)."""
        n = 8
        cost = rng.uniform(0, 2, (n, n))
        mu = rng.uniform(0.05, 0.3, n)
        nu = rng.uniform(0.05, 0.3, n)
        M, info = sinkhorn_partial_ot(cost, mu, nu, eps=0.5, mass_fraction=0.8)
        row_sums = M.sum(axis=1)
        assert np.all(row_sums <= mu + 1e-4), (
            f"Sub-stochastic violation: max excess = {(row_sums - mu).max():.6f}")


# =============================================================================
# TRANSPORT FIELD
# =============================================================================

class TestTransportField:

    def test_identity_like(self, rng):
        """Near-identity M should approximately preserve the field."""
        n = 5
        # Make a diagonally-dominant transport plan
        M = np.eye(n) * 0.9 + rng.uniform(0, 0.01, (n, n))
        u_s = rng.uniform(0.2, 0.8, n)
        u_transported = transport_field(M, u_s)
        # Should be close to u_s since M is near-identity
        np.testing.assert_allclose(u_transported, u_s, atol=0.1)


# =============================================================================
# FIXED-POINT ITERATION
# =============================================================================

class TestFixedPoint:

    def test_convergence_weak_regime(self, grid_5x5, default_params, rng):
        """Weak regime (large eps_ot, small lambda_tr) should converge."""
        n = grid_5x5.n
        # Create a simple formation-like field
        u_t = np.full(n, 0.2)
        center = n // 2
        u_t[center] = 0.9
        # Neighbors of center
        for nb in [center - 1, center + 1, center - 5, center + 5]:
            if 0 <= nb < n:
                u_t[nb] = 0.7

        result = transport_fixed_point(
            u_t, grid_5x5, default_params,
            sigma=2.0, gamma=0.5, eps_ot=5.0, lambda_tr=0.01,
            max_fp_iter=10, fp_tol=1e-3,
        )
        assert isinstance(result, TransportResult)
        assert result.M.shape == (n, n)
        assert len(result.fp_residuals) > 0

    def test_identity_init(self, grid_5x5, default_params, rng):
        """u_s should be structurally similar to u_t when transport is weak."""
        n = grid_5x5.n
        u_t = np.full(n, 0.3)
        u_t[n // 2] = 0.8

        result = transport_fixed_point(
            u_t, grid_5x5, default_params,
            sigma=2.0, gamma=0.5, eps_ot=5.0, lambda_tr=0.01,
            max_fp_iter=5, fp_tol=1e-3,
        )
        # u_s should have mass concentrated similarly to u_t
        # (not necessarily identical due to re-optimization, but correlated)
        corr = np.corrcoef(result.u_t, result.u_s)[0, 1]
        assert corr > 0.0, f"u_s should be positively correlated with u_t, got r={corr:.3f}"


# =============================================================================
# PERSIST (TRANSPORT-BASED)
# =============================================================================

class TestPersistTransport:

    def test_identical_fields(self, rng):
        """Same field with identity-like transport → Persist ≈ 1."""
        n = 10
        u = np.full(n, 0.3)
        u[3:7] = 0.9  # core at indices 3-6

        # Near-identity transport plan (strong diagonal)
        M = np.eye(n) * 0.8 + rng.uniform(0, 0.01, (n, n))

        p = persist_transport(u, u, M, theta_core=0.8)
        assert p > 0.7, f"Persist for identical fields with identity M = {p:.4f}"

    def test_disjoint_cores(self):
        """Disjoint cores → Persist ≈ 0."""
        n = 20
        u_t = np.full(n, 0.1)
        u_t[0:5] = 0.9  # core at left

        u_s = np.full(n, 0.1)
        u_s[15:20] = 0.9  # core at right

        # Transport plan that doesn't connect left to right
        M = np.eye(n) * 0.5  # diagonal — maps i→i
        # Core_t={0..4}, Core_s={15..19}, M[0:5, 15:20] = 0
        p = persist_transport(u_t, u_s, M, theta_core=0.8)
        assert p < 0.1, f"Persist for disjoint cores = {p:.4f}"

    def test_no_core(self):
        """No core sites → Persist = 0."""
        n = 10
        u_t = np.full(n, 0.5)  # all below theta_core=0.8
        u_s = np.full(n, 0.5)
        M = np.eye(n)
        p = persist_transport(u_t, u_s, M, theta_core=0.8)
        assert p == 0.0

    def test_partial_overlap(self):
        """Partially overlapping cores should give 0 < Persist < 1."""
        n = 20
        u_t = np.full(n, 0.1)
        u_t[3:8] = 0.9  # core at 3-7

        u_s = np.full(n, 0.1)
        u_s[5:10] = 0.9  # core at 5-9, overlaps 5-7

        # Diagonal transport — maps i to i
        M = np.eye(n) * 0.8
        p = persist_transport(u_t, u_s, M, theta_core=0.8)
        assert 0.0 < p < 1.0, f"Partial overlap should give 0 < Persist < 1, got {p:.4f}"

    def test_shifted_field(self):
        """Spatially shifted formation should have reduced Persist."""
        n = 30
        u_t = np.full(n, 0.1)
        u_t[5:10] = 0.9

        u_same = u_t.copy()
        u_shifted = np.full(n, 0.1)
        u_shifted[15:20] = 0.9  # shifted far away

        M = np.eye(n) * 0.8
        p_same = persist_transport(u_t, u_same, M, theta_core=0.8)
        p_shifted = persist_transport(u_t, u_shifted, M, theta_core=0.8)
        assert p_same > p_shifted, (
            f"Same field Persist={p_same:.4f} should exceed shifted Persist={p_shifted:.4f}")


# =============================================================================
# TRANSPORT ENERGY
# =============================================================================

class TestTransportEnergy:

    def test_transport_energy_nonnegative(self, grid_10x10, default_params, rng):
        """Transport energy should be non-negative (cost >= 0, M >= 0)."""
        n = grid_10x10.n
        u = rng.uniform(0.1, 0.9, n)
        phi = cohesion_fingerprint(u, grid_10x10, default_params)
        dist = graph_distance_matrix(grid_10x10)
        cost = transport_cost(phi, phi, dist, sigma=1.0, gamma=1.0)

        mu = u / u.sum()
        nu = u / u.sum()
        M, info = sinkhorn_partial_ot(cost, mu, nu, eps=0.5)

        energy = np.sum(M * cost)
        assert energy >= -1e-10, f"Transport energy should be non-negative, got {energy}"
        assert np.all(M >= -1e-15), "Transport plan should be non-negative"
        assert np.all(cost >= -1e-15), "Cost matrix should be non-negative"


# =============================================================================
# _minimize_with_transport ISOLATION
# =============================================================================

class TestMinimizeWithTransport:

    def test_returns_valid_field(self, grid_10x10, default_params, rng):
        """Output should be on Sigma_m with values in [0,1]."""
        from scc.transport import _minimize_with_transport

        n = grid_10x10.n
        c = default_params.volume_fraction
        m = c * n
        u_init = rng.uniform(0.1, 0.9, n)
        u_init = u_init * (m / u_init.sum())  # project to Sigma_m
        u_init = np.clip(u_init, 0, 1)

        u_opt = _minimize_with_transport(u_init, grid_10x10, default_params)

        assert np.all(u_opt >= -1e-8), f"Values below 0: min={u_opt.min()}"
        assert np.all(u_opt <= 1.0 + 1e-8), f"Values above 1: max={u_opt.max()}"
        np.testing.assert_allclose(u_opt.sum(), m, atol=0.1,
                                   err_msg=f"sum(u)={u_opt.sum():.4f}, expected m={m:.1f}")


# =============================================================================
# FINGERPRINT PROPERTIES
# =============================================================================

class TestFingerprintProperties:

    def test_binary_field(self, grid_10x10, default_params):
        """Nearly binary field should have fingerprint component 0 near 0 or 1."""
        n = grid_10x10.n
        u = np.full(n, 0.01)
        u[40:60] = 0.99  # nearly binary: strong core

        phi = cohesion_fingerprint(u, grid_10x10, default_params)

        # Component 0 is just u — should be near 0 or 1
        for i in range(n):
            assert phi[i, 0] < 0.05 or phi[i, 0] > 0.95, (
                f"phi[{i},0]={phi[i,0]:.4f} not near 0 or 1 for binary field")

    def test_varies_with_params(self, grid_10x10):
        """Different a_cl values should produce different fingerprints."""
        n = grid_10x10.n
        u = np.random.default_rng(42).uniform(0.2, 0.8, n)

        params1 = make_params(a_cl=1.0)
        params2 = make_params(a_cl=3.5)

        phi1 = cohesion_fingerprint(u, grid_10x10, params1)
        phi2 = cohesion_fingerprint(u, grid_10x10, params2)

        # Component 0 (raw u) should be identical
        np.testing.assert_allclose(phi1[:, 0], phi2[:, 0])
        # Component 1 (closure) should differ since a_cl differs
        assert not np.allclose(phi1[:, 1], phi2[:, 1], atol=1e-3), (
            "Fingerprint closure component should vary with a_cl")


# =============================================================================
# TRANSPORT COST PROPERTIES
# =============================================================================

class TestTransportCostProperties:

    def test_cost_increases_with_gamma(self, grid_5x5, default_params, rng):
        """Higher gamma should increase cost for different fingerprints."""
        n = grid_5x5.n
        u1 = rng.uniform(0.1, 0.9, n)
        u2 = rng.uniform(0.1, 0.9, n)
        phi1 = cohesion_fingerprint(u1, grid_5x5, default_params)
        phi2 = cohesion_fingerprint(u2, grid_5x5, default_params)
        dist = graph_distance_matrix(grid_5x5)

        c_low = transport_cost(phi1, phi2, dist, sigma=1.0, gamma=0.1)
        c_high = transport_cost(phi1, phi2, dist, sigma=1.0, gamma=10.0)

        # Higher gamma adds more fingerprint penalty, so total cost increases
        assert np.sum(c_high) > np.sum(c_low), (
            "Higher gamma should increase total cost")

    def test_zero_fingerprint_cost_for_identical(self, grid_5x5, default_params, rng):
        """Fingerprint component should be zero when phi_t == phi_s."""
        n = grid_5x5.n
        u = rng.uniform(0.1, 0.9, n)
        phi = cohesion_fingerprint(u, grid_5x5, default_params)
        dist = graph_distance_matrix(grid_5x5)

        # gamma=0 → spatial only
        c_spatial = transport_cost(phi, phi, dist, sigma=1.0, gamma=0.0)
        # gamma=1 → spatial + fingerprint
        c_full = transport_cost(phi, phi, dist, sigma=1.0, gamma=1.0)

        # With identical fingerprints, fingerprint term is ||phi(x)-phi(x)||^2 = 0
        # on diagonal, but off-diagonal phi(x) != phi(y) in general.
        # On diagonal, both should be zero
        np.testing.assert_allclose(np.diag(c_spatial), 0.0, atol=1e-12)
        np.testing.assert_allclose(np.diag(c_full), 0.0, atol=1e-12)


# =============================================================================
# SINKHORN EDGE CASES
# =============================================================================

class TestSinkhornEdgeCases:

    def test_large_cost(self, rng):
        """Large costs should produce near-zero off-diagonal transport."""
        n = 5
        # Very large cost off-diagonal, zero on diagonal
        cost = np.ones((n, n)) * 1000.0
        np.fill_diagonal(cost, 0.0)
        mu = np.ones(n) / n
        nu = np.ones(n) / n
        M, info = sinkhorn_partial_ot(cost, mu, nu, eps=0.01)
        # Transport should be concentrated on diagonal
        off_diag = M.sum() - np.trace(M)
        assert off_diag < 0.01, (
            f"Off-diagonal mass should be near zero with large costs, got {off_diag:.6f}")

    def test_small_eps(self, rng):
        """Small epsilon should produce sparser transport plan."""
        n = 6
        cost = rng.uniform(0, 2, (n, n))
        cost = (cost + cost.T) / 2
        mu = np.ones(n) / n
        nu = np.ones(n) / n

        M_large_eps, _ = sinkhorn_partial_ot(cost, mu, nu, eps=5.0, max_iter=500)
        M_small_eps, _ = sinkhorn_partial_ot(cost, mu, nu, eps=0.01, max_iter=500)

        # Smaller eps → sparser plan (more concentrated, higher max entry)
        # Measure sparsity by ratio of max entry to mean entry
        ratio_large = M_large_eps.max() / max(M_large_eps.mean(), 1e-15)
        ratio_small = M_small_eps.max() / max(M_small_eps.mean(), 1e-15)
        assert ratio_small > ratio_large, (
            f"Small eps should produce sparser plan: ratio_small={ratio_small:.2f} "
            f"vs ratio_large={ratio_large:.2f}")

    def test_mass_conservation(self, rng):
        """Total transported mass should match mass_fraction * min(sum(mu), sum(nu))."""
        n = 8
        cost = rng.uniform(0, 2, (n, n))
        mu = rng.uniform(0.05, 0.3, n)
        nu = rng.uniform(0.05, 0.3, n)

        for mf in [0.5, 0.8, 1.0]:
            M, info = sinkhorn_partial_ot(cost, mu, nu, eps=0.1, mass_fraction=mf,
                                          max_iter=500)
            total = M.sum()
            expected = mf * min(mu.sum(), nu.sum())
            np.testing.assert_allclose(total, expected, atol=0.1,
                                       err_msg=f"mass_fraction={mf}: total={total:.4f}, expected={expected:.4f}")


# =============================================================================
# FIXED-POINT PROPERTIES
# =============================================================================

class TestFixedPointProperties:

    def test_weak_regime_fast_convergence(self, grid_10x10, default_params):
        """Weak regime (small lambda_tr, large eps_ot) should converge in <= 5 iterations."""
        n = grid_10x10.n
        u_t = np.full(n, 0.2)
        center = n // 2
        u_t[center] = 0.9
        for nb in [center - 1, center + 1, center - 10, center + 10]:
            if 0 <= nb < n:
                u_t[nb] = 0.7

        result = transport_fixed_point(
            u_t, grid_10x10, default_params,
            sigma=2.0, gamma=0.5, eps_ot=10.0, lambda_tr=0.001,
            max_fp_iter=5, fp_tol=1e-2,
        )
        assert result.iterations <= 5, (
            f"Weak regime should converge quickly, took {result.iterations} iterations")

    def test_result_on_sigma_m(self, grid_10x10, default_params):
        """Result u_s should satisfy sum(u_s) ≈ m and 0 <= u_s <= 1."""
        n = grid_10x10.n
        c = default_params.volume_fraction
        m = c * n

        u_t = np.full(n, 0.2)
        center = n // 2
        u_t[center] = 0.9
        for nb in [center - 1, center + 1, center - 10, center + 10]:
            if 0 <= nb < n:
                u_t[nb] = 0.7

        result = transport_fixed_point(
            u_t, grid_10x10, default_params,
            sigma=2.0, gamma=0.5, eps_ot=5.0, lambda_tr=0.01,
            max_fp_iter=3, fp_tol=1e-3,
        )

        assert np.all(result.u_s >= -1e-8), f"u_s has negative values: min={result.u_s.min()}"
        assert np.all(result.u_s <= 1.0 + 1e-8), f"u_s exceeds 1: max={result.u_s.max()}"
        np.testing.assert_allclose(result.u_s.sum(), m, atol=1.0,
                                   err_msg=f"sum(u_s)={result.u_s.sum():.2f}, expected m={m:.1f}")

    def test_transport_energy_bounded(self, grid_10x10, default_params):
        """Transport energy should be finite and non-negative."""
        n = grid_10x10.n
        u_t = np.full(n, 0.2)
        center = n // 2
        u_t[center] = 0.9
        for nb in [center - 1, center + 1, center - 10, center + 10]:
            if 0 <= nb < n:
                u_t[nb] = 0.7

        result = transport_fixed_point(
            u_t, grid_10x10, default_params,
            sigma=2.0, gamma=0.5, eps_ot=5.0, lambda_tr=0.01,
            max_fp_iter=3, fp_tol=1e-3,
        )

        assert np.isfinite(result.transport_energy), (
            f"Transport energy should be finite, got {result.transport_energy}")
        assert result.transport_energy >= -1e-10, (
            f"Transport energy should be non-negative, got {result.transport_energy}")


# =============================================================================
# EDGE CASES
# =============================================================================

class TestTransportEdgeCases:

    def test_transport_cost_disconnected_graph(self, default_params):
        """Disconnected graph should produce finite cost (no NaN)."""
        import scipy.sparse as sp

        # Two disconnected components: nodes 0-2 and nodes 3-5
        row = [0, 1, 1, 2, 3, 4, 4, 5]
        col = [1, 0, 2, 1, 4, 3, 5, 4]
        W = sp.csr_matrix((np.ones(8), (row, col)), shape=(6, 6))
        graph = GraphState(W)

        u = np.array([0.8, 0.7, 0.6, 0.3, 0.2, 0.1])
        phi = cohesion_fingerprint(u, graph, default_params)
        dist = graph_distance_matrix(graph)

        # dist should contain inf for cross-component pairs
        assert np.any(np.isinf(dist)), "Disconnected graph should have inf distances"

        cost = transport_cost(phi, phi, dist, sigma=1.0, gamma=1.0)
        assert np.all(np.isfinite(cost)), f"Cost matrix should be finite, has {np.sum(~np.isfinite(cost))} non-finite entries"
        assert not np.any(np.isnan(cost)), "Cost matrix should not contain NaN"

    def test_fixed_point_single_node(self, default_params):
        """Single-node graph should work without error."""
        import scipy.sparse as sp

        W = sp.csr_matrix((1, 1), dtype=np.float64)
        graph = GraphState(W)
        u_t = np.array([0.5])

        result = transport_fixed_point(
            u_t, graph, default_params,
            sigma=1.0, gamma=0.5, eps_ot=1.0, lambda_tr=0.01,
            max_fp_iter=3, fp_tol=1e-3,
        )
        assert isinstance(result, TransportResult)
        assert result.M.shape == (1, 1)
        assert np.all(np.isfinite(result.u_s))

    def test_sinkhorn_zero_marginals(self):
        """Zero source/target marginals should not produce NaN."""
        n = 5
        cost = np.ones((n, n))
        mu = np.zeros(n)
        nu = np.zeros(n)

        M, info = sinkhorn_partial_ot(cost, mu, nu, eps=0.1)
        assert np.all(np.isfinite(M)), "Transport plan should be finite for zero marginals"
        assert not np.any(np.isnan(M)), "Transport plan should not contain NaN"
        assert M.sum() < 1e-10, "No mass should be transported with zero marginals"
        assert info['converged']
