"""Tests for parameter validation.

Must catch: a_cl >= 4, c outside spinodal, β < β_crit warning.
Phase transition: β_crit = 4α·λ₂ / |W''(c)|.
"""

import numpy as np
import pytest

from scc.params import ParameterRegistry
from scc.energy import energy_bd, EnergyComputer, double_well_second_deriv
from tests.conftest import make_params


class TestParamValidation:

    def test_a_cl_below_4_valid(self):
        p = ParameterRegistry(a_cl=3.0)
        valid, violations, _ = p.validate()
        fatal = [v for v in violations if 'a_cl' in v.lower()]
        assert len(fatal) == 0

    def test_a_cl_at_4_flagged(self):
        p = ParameterRegistry(a_cl=4.0)
        valid, violations, _ = p.validate()
        assert not valid or any('a_cl' in v.lower() or 'contraction' in v.lower()
                                for v in violations)

    def test_a_cl_above_4_flagged(self):
        p = ParameterRegistry(a_cl=5.0)
        valid, violations, _ = p.validate()
        assert not valid or any('a_cl' in v.lower() or 'contraction' in v.lower()
                                for v in violations)

    def test_volume_in_spinodal_valid(self):
        for c in [0.3, 0.5, 0.7]:
            p = ParameterRegistry(volume_fraction=c)
            valid, violations, _ = p.validate()
            spinodal_violations = [v for v in violations if 'spinodal' in v.lower()
                                   or 'volume' in v.lower()]
            assert len(spinodal_violations) == 0, (
                f"c={c} should be valid, got: {spinodal_violations}")

    def test_volume_outside_spinodal_flagged(self):
        for c in [0.1, 0.2, 0.85, 0.95]:
            p = ParameterRegistry(volume_fraction=c)
            valid, violations, _ = p.validate()
            assert not valid or any('spinodal' in v.lower() or 'volume' in v.lower()
                                    for v in violations), (
                f"c={c} outside spinodal should be flagged")

    def test_spinodal_boundaries(self):
        p = ParameterRegistry()
        c_lo, c_hi = p.spinodal_bounds
        assert abs(c_lo - 0.2113) < 0.001
        assert abs(c_hi - 0.7887) < 0.001


class TestBetaCrit:
    """β_crit = 4α·λ₂ / |W''(c)|."""

    def test_computation(self, grid_10x10):
        params = ParameterRegistry(alpha_bd=1.0, volume_fraction=0.5)
        lam2 = grid_10x10.fiedler
        bc = params.beta_critical(lam2)

        assert bc > 0
        assert np.isfinite(bc)
        # For 10x10: λ₂ ≈ 0.098, |W''(0.5)|=1 => β_crit ≈ 0.39
        assert 0.1 < bc < 2.0, f"β_crit = {bc:.4f}"

    def test_W_double_prime_signs(self):
        for c in [0.3, 0.4, 0.5, 0.6, 0.7]:
            assert double_well_second_deriv(c) < 0
        for c in [0.1, 0.15, 0.85, 0.9]:
            assert double_well_second_deriv(c) >= 0

    @pytest.mark.parametrize("c", [0.3, 0.4, 0.5, 0.6, 0.7])
    def test_uniform_unstable_above_beta_crit(self, grid_10x10, c):
        lam2 = grid_10x10.fiedler
        fiedler = grid_10x10.fiedler_vector()
        n = grid_10x10.n
        alpha = 1.0

        W_pp = double_well_second_deriv(c)
        if abs(W_pp) < 1e-10:
            pytest.skip("Near spinodal boundary")

        beta_crit = 4 * alpha * lam2 / abs(W_pp)
        beta = beta_crit * 2.0

        params = make_params(alpha_bd=alpha, beta_bd=beta, volume_fraction=c)
        u0 = np.full(n, c)
        eps = 0.01
        u_p = u0 + eps * fiedler
        u_p = np.clip(u_p, 0, 1)
        u_p = u_p * (c * n / u_p.sum())

        E0 = energy_bd(u0, grid_10x10, params)
        Ep = energy_bd(u_p, grid_10x10, params)

        assert Ep < E0 + 1e-10, (
            f"Uniform should be UNSTABLE above β_crit: E0={E0:.6f}, Ep={Ep:.6f}")

    @pytest.mark.parametrize("c", [0.3, 0.4, 0.5, 0.6, 0.7])
    def test_uniform_stable_below_beta_crit(self, grid_10x10, c):
        lam2 = grid_10x10.fiedler
        fiedler = grid_10x10.fiedler_vector()
        n = grid_10x10.n
        alpha = 1.0

        W_pp = double_well_second_deriv(c)
        if abs(W_pp) < 1e-10:
            pytest.skip("Near spinodal boundary")

        beta_crit = 4 * alpha * lam2 / abs(W_pp)
        beta = beta_crit * 0.5

        params = make_params(alpha_bd=alpha, beta_bd=beta, volume_fraction=c)
        u0 = np.full(n, c)
        eps = 0.01
        u_p = u0 + eps * fiedler
        u_p = np.clip(u_p, 0, 1)
        u_p = u_p * (c * n / u_p.sum())

        E0 = energy_bd(u0, grid_10x10, params)
        Ep = energy_bd(u_p, grid_10x10, params)

        assert Ep >= E0 - 1e-10, (
            f"Uniform should be STABLE below β_crit: E0={E0:.6f}, Ep={Ep:.6f}")

    @pytest.mark.parametrize("c", [0.3, 0.5, 0.7])
    def test_transition_within_20pct(self, grid_10x10, c):
        lam2 = grid_10x10.fiedler
        fiedler = grid_10x10.fiedler_vector()
        n = grid_10x10.n
        alpha = 1.0
        W_pp = double_well_second_deriv(c)
        beta_crit = 4 * alpha * lam2 / abs(W_pp)

        u0 = np.full(n, c)
        eps = 0.01

        betas = np.linspace(beta_crit * 0.5, beta_crit * 2.0, 30)
        transition_beta = None

        for beta in betas:
            params = make_params(alpha_bd=alpha, beta_bd=beta, volume_fraction=c)
            u_p = u0 + eps * fiedler
            u_p = np.clip(u_p, 0, 1)
            u_p = u_p * (c * n / u_p.sum())

            E0 = energy_bd(u0, grid_10x10, params)
            Ep = energy_bd(u_p, grid_10x10, params)
            if Ep < E0 - 1e-12:
                transition_beta = beta
                break

        assert transition_beta is not None
        ratio = transition_beta / beta_crit
        assert 0.8 <= ratio <= 1.2, (
            f"Transition at β={transition_beta:.4f}, "
            f"predicted={beta_crit:.4f}, ratio={ratio:.3f}")
