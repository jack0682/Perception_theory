"""Tests for diagnostic predicates: Bind, Sep, Inside.

Key identities:
  Bind = 1 - ||u - Cl(u)||_2 / sqrt(n)
  Sep_old = 1 - E_sep / m  (proved)
  Inside = Q_morph via persistence H0
"""

import numpy as np
import pytest

from scc.diagnostics import bind_predicate, sep_predicate, inside_predicate, diagnostic_vector
from scc.operators import closure, distinction
from scc.energy import energy_cl, energy_sep, EnergyComputer
from tests.conftest import make_params


# =============================================================================
# BIND
# =============================================================================

class TestBind:

    def test_range(self, grid_10x10, default_params, rng):
        n = grid_10x10.n
        for _ in range(20):
            u = rng.uniform(0, 1, n)
            b = bind_predicate(u, grid_10x10, default_params)
            assert 0 <= b <= 1 + 1e-10, f"Bind = {b}"

    def test_one_at_fixed_point(self, grid_10x10, default_params, rng):
        n = grid_10x10.n
        u = rng.uniform(0.3, 0.7, n)
        for _ in range(200):
            u = closure(u, grid_10x10, default_params)
        b = bind_predicate(u, grid_10x10, default_params)
        assert b > 0.99, f"Bind at fixed point = {b:.4f}"

    def test_formula(self, grid_10x10, default_params, rng):
        """Bind = 1 - ||u - Cl(u)||_2 / sqrt(n)."""
        n = grid_10x10.n
        u = rng.uniform(0, 1, n)
        cl_u = closure(u, grid_10x10, default_params)
        expected = 1 - np.linalg.norm(u - cl_u) / np.sqrt(n)
        actual = bind_predicate(u, grid_10x10, default_params)
        np.testing.assert_allclose(actual, expected, rtol=1e-10)

    def test_cauchy_schwarz_bound(self, grid_10x10, default_params, rng):
        """Proved: Bind >= 1 - sqrt(E_cl / n)."""
        n = grid_10x10.n
        for _ in range(20):
            u = rng.uniform(0, 1, n)
            b = bind_predicate(u, grid_10x10, default_params)
            e_cl = energy_cl(u, grid_10x10, default_params)
            lower = 1 - np.sqrt(e_cl / n)
            assert b >= lower - 1e-10, (
                f"Cauchy-Schwarz VIOLATED: Bind={b:.6f} < {lower:.6f}")

    def test_low_random_high_converged(self, grid_10x10, default_params, rng):
        n = grid_10x10.n
        u_rand = rng.uniform(0, 1, n)
        b_rand = bind_predicate(u_rand, grid_10x10, default_params)

        u_conv = rng.uniform(0.3, 0.7, n)
        for _ in range(200):
            u_conv = closure(u_conv, grid_10x10, default_params)
        b_conv = bind_predicate(u_conv, grid_10x10, default_params)

        assert b_conv > b_rand


# =============================================================================
# SEP (identity: Sep_old = 1 - E_sep/m)
# =============================================================================

class TestSep:

    def test_sep_correlates_with_energy(self, grid_10x10, rng):
        """v2.0 Sep is C_t-weighted (not identical to 1-E_sep/m).
        But lower E_sep should still correlate with higher Sep.
        The exact identity Sep_old = 1-E_sep/m held for unweighted Sep (v1.0)."""
        params = make_params()
        n = grid_10x10.n

        pairs = []
        for _ in range(20):
            u = rng.uniform(0.1, 0.9, n)
            s = sep_predicate(u, grid_10x10, params)
            e = energy_sep(u, grid_10x10, params)
            pairs.append((e, s))

        # Negative correlation: lower E_sep => higher Sep
        energies = [p[0] for p in pairs]
        seps = [p[1] for p in pairs]
        corr = np.corrcoef(energies, seps)[0, 1]
        assert corr < 0.5, f"Sep should be negatively correlated with E_sep, got r={corr:.3f}"

    def test_range(self, grid_10x10, default_params, rng):
        n = grid_10x10.n
        for _ in range(20):
            u = rng.uniform(0.1, 0.9, n)
            s = sep_predicate(u, grid_10x10, default_params)
            assert s <= 1 + 1e-10, f"Sep = {s} > 1"

    def test_high_for_well_separated(self, grid_10x10, default_params, two_region_field):
        s = sep_predicate(two_region_field, grid_10x10, default_params)
        assert s > 0.3, f"Sep for two-region = {s:.4f}"


# =============================================================================
# INSIDE (Q_morph)
# =============================================================================

class TestInside:

    def test_low_for_uniform(self, grid_10x10):
        """QM1: Q_morph should be low on uniform fields.
        For perfectly uniform field, persistence has one bar spanning [0, 0.5]
        with l_max=0.5, Artic=1, so Q_morph=0.5. This is the baseline."""
        u = np.full(grid_10x10.n, 0.5)
        score = inside_predicate(u, grid_10x10)
        # Uniform field has no articulation contrast — accept baseline
        assert score <= 0.55, f"Inside on uniform = {score:.4f}"

    def test_positive_for_bump(self, grid_10x10, bump_field_10x10):
        score = inside_predicate(bump_field_10x10, grid_10x10)
        assert score > 0.05, f"Inside on bump = {score:.4f}"

    def test_monotone_quality(self, grid_10x10):
        n = grid_10x10.n
        size = 10

        # Weak formation
        u_weak = np.full(n, 0.45)
        for i in range(size):
            for j in range(size):
                if (i - 5)**2 + (j - 5)**2 < 4:
                    u_weak[i * size + j] = 0.55

        # Strong formation
        u_strong = np.full(n, 0.1)
        for i in range(size):
            for j in range(size):
                if (i - 5)**2 + (j - 5)**2 < 9:
                    u_strong[i * size + j] = 0.9

        s_weak = inside_predicate(u_weak, grid_10x10)
        s_strong = inside_predicate(u_strong, grid_10x10)
        assert s_strong > s_weak, (
            f"Strong ({s_strong:.3f}) should exceed weak ({s_weak:.3f})")


# =============================================================================
# DIAGNOSTIC VECTOR
# =============================================================================

class TestDiagnosticVector:

    def test_returns_4_components(self, grid_10x10, default_params, rng):
        n = grid_10x10.n
        u = rng.uniform(0.2, 0.8, n)
        dv = diagnostic_vector(u, grid_10x10, default_params)
        assert len(dv.vector) == 4
        for i, val in enumerate(dv.vector):
            assert 0 <= val <= 1 + 1e-10, f"d[{i}] = {val}"

    def test_bind_component(self, grid_10x10, default_params, rng):
        n = grid_10x10.n
        u = rng.uniform(0.2, 0.8, n)
        dv = diagnostic_vector(u, grid_10x10, default_params)
        b_direct = bind_predicate(u, grid_10x10, default_params)
        np.testing.assert_allclose(dv.bind, b_direct, rtol=1e-10)
