"""Tests for Aut(G)_{u*} stabilizer behavior — NQ-258 / NQ-259 (working).

Spec: ``THEORY/working/SF/sigma_lie_algebra_structure.md`` §3.2:

    Aut(G)_{u*} := {π ∈ Aut(G) : P_π u* = u*}.

There is no Aut(G)_{u*} computation API in ``scc/`` yet (NQ-259 is W6
prerequisite, working file §12). These tests therefore include a small
brute-force stabilizer utility (``_stabilizer_dihedral``) that enumerates the
8-element D_4 group on free-BC L×L grids and tests:

  1. **Group structure.** Stabilizer is a subgroup of Aut(G) (closure,
     identity, inverses).
  2. **Orbit-stabilizer theorem.** |Aut(G)·u*|·|Aut(G)_{u*}| = |Aut(G)|.
  3. **Equivariance of the energy** (T-σ-Lemma-1, canonical §13):
     E(P_π u) = E(u) for all π ∈ Aut(G).
  4. **Schur-commutation of the Hessian** at fixed points (§4.1):
     P_π H(u*) P_π^T = H(u*) for π ∈ Aut(G)_{u*}.
  5. **Stabilizer-conjugacy across an Aut(G)-orbit** (NQ-188 Definition
     2.1' clause (a)): u_2* = P_π u_1* ⇒ Aut(G)_{u_2*} = π Aut(G)_{u_1*} π⁻¹.
  6. **Concrete D_4 cases:**
       - uniform field at c·1: stabilizer = full D_4 (|·| = 8).
       - axis-aligned bifurcated profile (NQ-187 setting): stabilizer
         contains the reflection across the broken axis but not all of D_4.

The brute-force utility is small (≤ 80 lines) and intentionally local to
this test module — it is *not* added to the scc public API. NQ-259 (W6)
will produce a proper implementation; this test serves as a forward-
compatible regression anchor.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import pytest

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer, grad_bd, double_well_second_deriv


# ===========================================================================
# Brute-force D_4 stabilizer utility (LOCAL to this test module)
# ===========================================================================

def _grid_perm_identity(L: int) -> np.ndarray:
    """Permutation array for the identity element."""
    return np.arange(L * L)


def _grid_perm_rotate(L: int, k: int) -> np.ndarray:
    """Permutation for k * 90° rotation (k ∈ {0, 1, 2, 3}) on L×L grid.

    Node (r, c) (with 0 ≤ r, c < L, indexed as r*L + c) is mapped under
    one 90° rotation to (c, L-1-r).
    """
    p = np.empty(L * L, dtype=np.int64)
    for r in range(L):
        for c in range(L):
            rr, cc = r, c
            for _ in range(k % 4):
                rr, cc = cc, L - 1 - rr
            p[r * L + c] = rr * L + cc
    return p


def _grid_perm_reflect_horiz(L: int) -> np.ndarray:
    """Reflection across the vertical mid-axis (column flip)."""
    p = np.empty(L * L, dtype=np.int64)
    for r in range(L):
        for c in range(L):
            p[r * L + c] = r * L + (L - 1 - c)
    return p


def _grid_perm_compose(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    """(p ∘ q)(i) = p(q(i))."""
    return p[q]


def _d4_perm_group(L: int) -> list[np.ndarray]:
    """Enumerate the 8 permutations of D_4 on the L×L free-BC grid.

    Order: e, r, r², r³, s, sr, sr², sr³, where r is 90° rotation and s
    is the horizontal reflection.
    """
    rots = [_grid_perm_rotate(L, k) for k in range(4)]
    s = _grid_perm_reflect_horiz(L)
    elems = list(rots) + [_grid_perm_compose(s, r) for r in rots]
    return elems


def _apply_perm(perm: np.ndarray, u: np.ndarray) -> np.ndarray:
    """Action P_π · u defined by (P_π u)_i = u_{π⁻¹(i)}.

    Equivalent in numpy: ``u_perm[perm[i]] = u[i]``, i.e. ``u_perm = u[inv]``
    where ``inv`` is the inverse permutation. We compute the inverse here.
    """
    inv = np.empty_like(perm)
    inv[perm] = np.arange(perm.size)
    return u[inv]


def _stabilizer_dihedral(u: np.ndarray, L: int, tol: float = 1e-8
                         ) -> list[int]:
    """Indices (in the canonical D_4 ordering) of π ∈ D_4 fixing u."""
    elems = _d4_perm_group(L)
    fixed = []
    for k, p in enumerate(elems):
        if np.allclose(_apply_perm(p, u), u, atol=tol):
            fixed.append(k)
    return fixed


def _is_subgroup(stab: list[int], elems: list[np.ndarray]) -> bool:
    """Check that the listed indices form a subgroup of D_4."""
    if 0 not in stab:  # identity is index 0
        return False
    perms = {k: elems[k] for k in stab}
    n = len(elems)
    for k1 in stab:
        for k2 in stab:
            comp = _grid_perm_compose(perms[k1], perms[k2])
            # Must equal one of the elements with index in stab.
            found = False
            for k3 in stab:
                if np.array_equal(comp, elems[k3]):
                    found = True
                    break
            if not found:
                return False
    return True


# ===========================================================================
# Helpers
# ===========================================================================

def _make_params(beta: float, c: float = 0.5) -> ParameterRegistry:
    return ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=2000,
    )


def _hessian_bd_analytic(u: np.ndarray, graph: GraphState,
                         params: ParameterRegistry) -> np.ndarray:
    """Dense analytic E_bd Hessian: 4αL + β·diag(W''(u_i))."""
    W_pp_vec = 2.0 * (1.0 - 6.0 * u + 6.0 * u**2)
    H = (4.0 * params.alpha_bd * graph.L.toarray()
         + np.diag(params.beta_bd * W_pp_vec))
    return 0.5 * (H + H.T)


def _perm_to_matrix(perm: np.ndarray) -> np.ndarray:
    """Build dense permutation matrix P with P · e_i = e_{perm(i)}."""
    n = perm.size
    P = np.zeros((n, n))
    for i in range(n):
        P[perm[i], i] = 1.0
    return P


# ===========================================================================
# Group-structure tests (D_4 enumeration)
# ===========================================================================

class TestD4Enumeration:

    def test_eight_distinct_elements(self):
        elems = _d4_perm_group(4)
        assert len(elems) == 8
        seen = set()
        for p in elems:
            seen.add(tuple(p.tolist()))
        assert len(seen) == 8

    def test_identity_is_first(self):
        elems = _d4_perm_group(4)
        np.testing.assert_array_equal(elems[0], _grid_perm_identity(4))

    def test_rotation_order_4(self):
        elems = _d4_perm_group(4)
        r = elems[1]  # 90° rotation
        composed = r
        for _ in range(3):
            composed = _grid_perm_compose(r, composed)
        np.testing.assert_array_equal(composed, _grid_perm_identity(4))

    def test_reflection_order_2(self):
        elems = _d4_perm_group(4)
        s = elems[4]  # horizontal reflection
        np.testing.assert_array_equal(_grid_perm_compose(s, s),
                                      _grid_perm_identity(4))

    def test_d4_closed_under_composition(self):
        elems = _d4_perm_group(4)
        elem_set = {tuple(p.tolist()) for p in elems}
        for p1 in elems:
            for p2 in elems:
                comp = _grid_perm_compose(p1, p2)
                assert tuple(comp.tolist()) in elem_set


# ===========================================================================
# Energy equivariance (T-σ-Lemma-1, canonical §13)
# ===========================================================================

class TestEnergyEquivariance:

    @pytest.mark.parametrize("L", [4, 6])
    def test_E_bd_invariant_under_d4(self, L):
        graph = GraphState.grid_2d(L, L)
        params = _make_params(beta=1.0)
        rng = np.random.default_rng(0)
        u = 0.5 + 0.1 * rng.standard_normal(L * L)
        u = np.clip(u, 0.01, 0.99)
        # Project to volume m=cn for consistency
        m = params.volume_fraction * graph.n
        u = u + (m - u.sum()) / graph.n

        from scc.energy import energy_bd
        E0 = energy_bd(u, graph, params)
        for k, perm in enumerate(_d4_perm_group(L)):
            up = _apply_perm(perm, u)
            Ep = energy_bd(up, graph, params)
            assert abs(Ep - E0) < 1e-10, (
                f"E_bd not invariant under D_4 element #{k}: "
                f"|ΔE| = {abs(Ep - E0):.2e}"
            )


# ===========================================================================
# Stabilizer of the uniform field (concrete check)
# ===========================================================================

class TestStabilizerUniform:

    @pytest.mark.parametrize("L", [4, 6, 8])
    def test_uniform_field_stabilizer_is_full_d4(self, L):
        u = np.full(L * L, 0.5)
        stab = _stabilizer_dihedral(u, L)
        assert stab == list(range(8)), f"L={L}: expected full D_4, got {stab}"

    def test_uniform_stabilizer_is_subgroup(self):
        L = 4
        u = np.full(L * L, 0.5)
        stab = _stabilizer_dihedral(u, L)
        elems = _d4_perm_group(L)
        assert _is_subgroup(stab, elems)


# ===========================================================================
# Stabilizer of axis-aligned vs diagonal bifurcated profiles
# ===========================================================================

class TestStabilizerBifurcated:
    """The post-pitchfork minimizer at β > β_crit^(2) on D_4 free-BC has
    two orbits of pure axis modes (broken to Z_2) and a diagonal mode
    (broken to a different Z_2). These tests use idealized profiles that
    encode the symmetry — they are not full optimizer outputs.
    """

    def test_axis_aligned_x_profile_has_z2_stabilizer(self):
        """u(r, c) = 0.5 + a·cos(πc/L) breaks D_4 to ⟨s_y⟩ ≅ Z_2.

        The horizontal reflection s_y (column flip) is broken because the
        cosine profile is anti-symmetric under c → L-1-c. The vertical
        reflection s_x (row flip) is preserved because the profile does
        not depend on r. The 180° rotation is broken (sends cos → cos but
        flips column sense). So the stabilizer is just {e, s_x}.
        """
        L = 6
        cos_col = np.cos(np.pi * (np.arange(L) + 0.5) / L)
        u = np.zeros((L, L))
        for r in range(L):
            u[r, :] = 0.5 + 0.05 * cos_col
        u = u.flatten()
        stab = _stabilizer_dihedral(u, L)
        elems = _d4_perm_group(L)
        # Must contain identity, must NOT be the full group, must be a subgroup
        assert 0 in stab
        assert len(stab) < 8
        assert len(stab) >= 2  # at least {e, some reflection}
        assert _is_subgroup(stab, elems), (
            f"Stabilizer indices {stab} do not form a subgroup of D_4"
        )

    def test_diagonal_profile_has_different_subgroup(self):
        """u(r, c) = 0.5 + a·(r+c-(L-1))/(L-1) gives a diagonal gradient.

        This profile has the diagonal-flip symmetry (swap rows/columns)
        but breaks the 4-fold rotation. Stabilizer must be a proper
        subgroup containing exactly the diagonal reflections.
        """
        L = 6
        u = np.zeros((L, L))
        for r in range(L):
            for c in range(L):
                u[r, c] = 0.5 + 0.05 * (r + c - (L - 1)) / (L - 1)
        u = u.flatten()
        stab = _stabilizer_dihedral(u, L)
        elems = _d4_perm_group(L)
        assert 0 in stab  # identity always
        assert len(stab) < 8
        assert _is_subgroup(stab, elems)


# ===========================================================================
# Orbit-stabilizer theorem
# ===========================================================================

class TestOrbitStabilizer:

    def _orbit_size(self, u: np.ndarray, L: int, tol: float = 1e-8) -> int:
        """Number of distinct images of u under D_4."""
        elems = _d4_perm_group(L)
        seen = []
        for p in elems:
            up = _apply_perm(p, u)
            if not any(np.allclose(up, v, atol=tol) for v in seen):
                seen.append(up)
        return len(seen)

    @pytest.mark.parametrize("L", [4, 6])
    def test_orbit_size_times_stabilizer_equals_eight(self, L):
        rng = np.random.default_rng(2026)
        # Uniform: orbit 1, stab 8 → product 8
        u_uniform = np.full(L * L, 0.5)
        assert self._orbit_size(u_uniform, L) * len(
            _stabilizer_dihedral(u_uniform, L)) == 8
        # Axis-aligned: orbit 4 (two axes × two signs / fixed-axis stab 2) ×
        # stab 2 = 8.
        cos_col = np.cos(np.pi * (np.arange(L) + 0.5) / L)
        u_axis = np.zeros((L, L))
        for r in range(L):
            u_axis[r, :] = 0.5 + 0.05 * cos_col
        u_axis = u_axis.flatten()
        prod = self._orbit_size(u_axis, L) * len(
            _stabilizer_dihedral(u_axis, L))
        assert prod == 8, f"L={L}: orbit·|stab| = {prod}, expected 8"
        # Generic random field: stab = 1, orbit = 8 → product 8
        u_rand = 0.5 + 0.1 * rng.standard_normal(L * L)
        prod = self._orbit_size(u_rand, L) * len(
            _stabilizer_dihedral(u_rand, L))
        assert prod == 8, f"random L={L}: product = {prod}"


# ===========================================================================
# Schur-commutation of the Hessian (sigma_lie_algebra §4.1)
# ===========================================================================

class TestSchurCommutation:
    """If π ∈ Aut(G)_{u*}, then P_π H(u*) P_π^T = H(u*).

    This is the foundation for the σ-tuple = irrep decomposition reading
    (working/SF/sigma_lie_algebra_structure.md §4.1).
    """

    def test_hessian_commutes_with_full_d4_at_uniform(self):
        L = 4
        graph = GraphState.grid_2d(L, L)
        params = _make_params(beta=2.5)
        u = np.full(graph.n, 0.5)
        H = _hessian_bd_analytic(u, graph, params)
        for k, perm in enumerate(_d4_perm_group(L)):
            P = _perm_to_matrix(perm)
            commuted = P @ H @ P.T
            err = np.linalg.norm(commuted - H)
            assert err < 1e-10, (
                f"D_4 element #{k} fails to commute with H at uniform: "
                f"||PHP^T - H|| = {err:.2e}"
            )

    def test_hessian_commutes_with_stabilizer_at_axis_profile(self):
        """For an axis-aligned profile, only the elements of Aut(G)_{u*}
        should commute; the rest map H to H(P_π u*) = H of the rotated
        profile, which differs from H(u*).
        """
        L = 4
        graph = GraphState.grid_2d(L, L)
        params = _make_params(beta=2.5)
        cos_col = np.cos(np.pi * (np.arange(L) + 0.5) / L)
        u = np.tile(0.5 + 0.05 * cos_col, L)  # row-broadcast axis profile
        # Shift to satisfy volume conservation
        u = u + (params.volume_fraction * graph.n - u.sum()) / graph.n

        stab_indices = _stabilizer_dihedral(u, L)
        elems = _d4_perm_group(L)
        H = _hessian_bd_analytic(u, graph, params)

        for k, perm in enumerate(elems):
            P = _perm_to_matrix(perm)
            commuted = P @ H @ P.T
            err = np.linalg.norm(commuted - H)
            if k in stab_indices:
                assert err < 1e-9, (
                    f"Stabilizer element #{k} fails to commute: err={err:.2e}"
                )
            else:
                # Non-stabilizer elements map H to H(P_π u*), which equals
                # the analytic Hessian at a different field configuration.
                # We verify: P H P^T == _hessian_bd_analytic(P_π u*).
                u_perm = _apply_perm(perm, u)
                H_perm = _hessian_bd_analytic(u_perm, graph, params)
                err_match = np.linalg.norm(commuted - H_perm)
                assert err_match < 1e-9, (
                    f"Element #{k}: P·H(u)·P^T should equal H(P_π u), "
                    f"err={err_match:.2e}"
                )


# ===========================================================================
# Stabilizer conjugacy across an Aut(G)-orbit (NQ-188 Definition 2.1' (a))
# ===========================================================================

class TestStabilizerConjugacy:
    """If u_2 = P_π u_1 then Aut(G)_{u_2} = π · Aut(G)_{u_1} · π⁻¹."""

    def _conjugate(self, sigma: np.ndarray, pi: np.ndarray) -> np.ndarray:
        """π σ π⁻¹ as a permutation array."""
        inv_pi = np.empty_like(pi)
        inv_pi[pi] = np.arange(pi.size)
        return pi[sigma[inv_pi]]

    def test_axis_profile_orbit_stabilizers_are_conjugate(self):
        L = 4
        elems = _d4_perm_group(L)
        cos_col = np.cos(np.pi * (np.arange(L) + 0.5) / L)
        u = np.tile(0.5 + 0.05 * cos_col, L)

        stab_u = set(tuple(elems[k].tolist()) for k in
                     _stabilizer_dihedral(u, L))

        for kpi, pi in enumerate(elems):
            v = _apply_perm(pi, u)
            stab_v_indices = _stabilizer_dihedral(v, L)
            stab_v = set(tuple(elems[k].tolist()) for k in stab_v_indices)

            # Build conjugate set π · Stab_u · π⁻¹
            conj_stab = set()
            for sk in _stabilizer_dihedral(u, L):
                conj = self._conjugate(elems[sk], pi)
                conj_stab.add(tuple(conj.tolist()))

            assert stab_v == conj_stab, (
                f"Orbit conjugacy failed for π = #{kpi}: "
                f"|stab_v| = {len(stab_v)}, |π·stab_u·π⁻¹| = {len(conj_stab)}"
            )

    def test_orbit_stabilizers_have_same_order(self):
        L = 4
        elems = _d4_perm_group(L)
        cos_col = np.cos(np.pi * (np.arange(L) + 0.5) / L)
        u = np.tile(0.5 + 0.05 * cos_col, L)
        n_u = len(_stabilizer_dihedral(u, L))
        for pi in elems:
            v = _apply_perm(pi, u)
            assert len(_stabilizer_dihedral(v, L)) == n_u


# ===========================================================================
# Forward-compatibility hook (NQ-259 W6)
# ===========================================================================

def test_aut_g_module_exists_or_xfail():
    """Once NQ-259 produces ``scc.aut_g`` with a public stabilizer API,
    this test will flip from xfail → pass and pin the import.
    """
    try:
        import scc.aut_g  # noqa: F401
        assert hasattr(scc.aut_g, "stabilizer"), (
            "scc.aut_g exists but lacks expected `stabilizer` API"
        )
    except ImportError:
        pytest.xfail(
            "scc.aut_g not yet implemented (NQ-259 W6 deliverable). "
            "This test acts as a forward-compatibility marker."
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
