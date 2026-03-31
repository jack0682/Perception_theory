"""Tests for SCC operators: Cl_t monotonicity (A2), contraction (A3), sigmoid range.

Canonical Spec v2.0 axioms:
  A2 — Monotonicity: u <= v => Cl(u) <= Cl(v). UNCONDITIONAL.
  A3 — Contraction: geometric convergence with rate a_cl/4 when a_cl < 4.
  A4 — Continuity: Lipschitz with constant a_cl/4.
"""

import numpy as np
import pytest

from scc.operators import aggregation, closure, distinction
from scc.graph import GraphState
from scc.params import ParameterRegistry
from tests.conftest import make_params


# =============================================================================
# A2: MONOTONICITY (unconditional)
# =============================================================================

class TestA2Monotonicity:

    @pytest.mark.parametrize("a_cl", [1.0, 2.0, 3.0, 3.5, 3.9, 3.99])
    def test_random_field_pairs(self, grid_10x10, rng, a_cl):
        params = make_params(a_cl=a_cl)
        n = grid_10x10.n

        for _ in range(20):
            u = rng.uniform(0, 1, n)
            delta = rng.uniform(0, 0.3, n)
            v = np.clip(u + delta, 0, 1)

            cl_u = closure(u, grid_10x10, params)
            cl_v = closure(v, grid_10x10, params)

            np.testing.assert_array_less(
                cl_u - 1e-10, cl_v,
                err_msg=f"A2 VIOLATED at a_cl={a_cl}"
            )

    def test_extreme_fields(self, grid_10x10, default_params):
        n = grid_10x10.n
        cl_zero = closure(np.zeros(n), grid_10x10, default_params)
        cl_half = closure(np.full(n, 0.5), grid_10x10, default_params)
        np.testing.assert_array_less(cl_zero - 1e-10, cl_half)

        cl_low = closure(np.full(n, 0.01), grid_10x10, default_params)
        cl_high = closure(np.full(n, 0.99), grid_10x10, default_params)
        np.testing.assert_array_less(cl_low - 1e-10, cl_high)

    def test_single_site_increase(self, grid_10x10, default_params, rng):
        n = grid_10x10.n
        u = rng.uniform(0.2, 0.8, n)
        cl_u = closure(u, grid_10x10, default_params)

        for site in range(0, n, 10):
            v = u.copy()
            v[site] = min(u[site] + 0.1, 1.0)
            cl_v = closure(v, grid_10x10, default_params)
            np.testing.assert_array_less(
                cl_u - 1e-10, cl_v,
                err_msg=f"A2 VIOLATED at site {site}"
            )


# =============================================================================
# A3: CONTRACTION (a_cl < 4)
# =============================================================================

class TestA3Contraction:

    @pytest.mark.parametrize("a_cl", [1.0, 2.0, 3.0, 3.5, 3.9])
    def test_geometric_convergence(self, grid_10x10, rng, a_cl):
        params = make_params(a_cl=a_cl)
        n = grid_10x10.n
        u = rng.uniform(0, 1, n)
        assert a_cl / 4.0 < 1.0

        diffs = []
        prev = u.copy()
        for _ in range(50):
            cur = closure(prev, grid_10x10, params)
            diffs.append(np.linalg.norm(cur - prev))
            prev = cur

        # At a_cl=3.9, rate = 3.9/4 = 0.975, so need more iterations
        # After 50 steps: 0.975^50 ≈ 0.28, so use 1e-1 threshold
        threshold = 0.975 ** 50 if a_cl > 3.5 else 1e-3
        assert diffs[-1] < diffs[0] * max(threshold * 2, 1e-3), (
            f"A3 too slow at a_cl={a_cl}: {diffs[0]:.6f} → {diffs[-1]:.6f}")

    @pytest.mark.parametrize("a_cl", [1.0, 2.0, 3.0, 3.5, 3.9])
    def test_rate_bounded_by_acl_over_4(self, grid_10x10, rng, a_cl):
        params = make_params(a_cl=a_cl)
        n = grid_10x10.n
        lip = a_cl / 4.0
        u = rng.uniform(0.2, 0.8, n)

        prev = u.copy()
        cur = closure(prev, grid_10x10, params)
        d_prev = np.linalg.norm(cur - prev)

        for _ in range(20):
            nxt = closure(cur, grid_10x10, params)
            d_cur = np.linalg.norm(nxt - cur)
            if d_prev > 1e-12:
                ratio = d_cur / d_prev
                assert ratio < lip + 0.1, (
                    f"Contraction ratio {ratio:.4f} > a_cl/4={lip:.4f}+tol")
            d_prev = d_cur
            prev, cur = cur, nxt

    def test_unique_fixed_point(self, grid_10x10, rng):
        params = make_params(a_cl=3.0)
        n = grid_10x10.n

        fps = []
        for _ in range(5):
            u = rng.uniform(0, 1, n)
            for _ in range(200):
                u = closure(u, grid_10x10, params)
            fps.append(u)

        for fp in fps[1:]:
            np.testing.assert_allclose(fps[0], fp, atol=1e-4,
                err_msg="Fixed point uniqueness violated")

    @pytest.mark.parametrize("a_cl", [4.0, 5.0, 8.0])
    def test_no_guarantee_above_4(self, a_cl):
        assert a_cl / 4.0 >= 1.0


# =============================================================================
# SIGMOID RANGE
# =============================================================================

class TestClosureRange:

    def test_output_in_unit_interval(self, grid_10x10, default_params, rng):
        n = grid_10x10.n
        for _ in range(30):
            u = rng.uniform(0, 1, n)
            out = closure(u, grid_10x10, default_params)
            assert np.all(out >= 0), "Cl produced negative"
            assert np.all(out <= 1), "Cl produced > 1"

    def test_matches_sigmoid_formula(self, grid_10x10, default_params, rng):
        """Cl(u)(x) = σ(a_cl * ((1-η)*u(x) + η*P(u)(x) - τ))."""
        n = grid_10x10.n
        u = rng.uniform(0.2, 0.8, n)
        result = closure(u, grid_10x10, default_params)

        pu = aggregation(u, grid_10x10)
        p = default_params
        z = p.a_cl * ((1 - p.eta_cl) * u + p.eta_cl * pu - p.tau_cl)
        expected = 1.0 / (1.0 + np.exp(-z))

        np.testing.assert_allclose(result, expected, rtol=1e-12)


class TestDistinctionRange:

    def test_output_in_unit_interval(self, grid_10x10, default_params, rng):
        n = grid_10x10.n
        for _ in range(30):
            u = rng.uniform(0, 1, n)
            out = distinction(u, grid_10x10, default_params)
            assert np.all(out >= 0), "D produced negative"
            assert np.all(out <= 1), "D produced > 1"

    def test_interior_higher_than_exterior(self, grid_10x10, default_params, two_region_field):
        d = distinction(two_region_field, grid_10x10, default_params)
        size = 10
        int_d = np.mean([d[i * size + 1] for i in range(size)])
        ext_d = np.mean([d[i * size + 8] for i in range(size)])
        assert int_d > ext_d, f"Interior D ({int_d:.3f}) <= exterior D ({ext_d:.3f})"


class TestAggregation:

    def test_output_range(self, grid_10x10, rng):
        n = grid_10x10.n
        for _ in range(10):
            f = rng.uniform(0, 1, n)
            pf = aggregation(f, grid_10x10)
            assert np.all(pf >= -1e-10)
            assert np.all(pf <= 1 + 1e-10)

    def test_constant_preserved(self, grid_10x10):
        c = 0.6
        pf = aggregation(np.full(grid_10x10.n, c), grid_10x10)
        np.testing.assert_allclose(pf, c, atol=0.05)


# =============================================================================
# A4: CONTINUITY
# =============================================================================

class TestA4Continuity:

    def test_lipschitz(self, grid_10x10, default_params, rng):
        n = grid_10x10.n
        u = rng.uniform(0.2, 0.8, n)
        cl_u = closure(u, grid_10x10, default_params)

        for eps in [1e-2, 1e-4, 1e-6]:
            v = u + rng.uniform(-eps, eps, n)
            v = np.clip(v, 0, 1)
            cl_v = closure(v, grid_10x10, default_params)
            out_diff = np.linalg.norm(cl_v - cl_u)
            in_diff = np.linalg.norm(v - u)
            assert out_diff <= (default_params.a_cl / 4 + 0.1) * in_diff + 1e-12
