"""Tests for the allow_outside_spinodal kwarg added in NQ-191 P2 patch.

Phase 4 F17: scc/params.py validate() and scc/optimizer.py find_formation()
both accept allow_outside_spinodal kwarg. Default (False) preserves variational-
use semantics (FATAL on c outside spinodal). True demotes to WARNING for IC-driven
metastable-stationary studies.

See: THEORY/logs/daily/2026-04-28/01_NQ173_v5b_f_verdict.md §6 (motivation).
"""
import numpy as np
import pytest
import scipy.sparse as sp

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation


@pytest.fixture
def small_torus():
    """Small 2D torus L=8 for fast testing."""
    L = 8
    n = L * L
    edges = []
    for i in range(L):
        for j in range(L):
            idx = i * L + j
            edges.append((idx, ((i + 1) % L) * L + j))
            edges.append((idx, i * L + (j + 1) % L))
    rows = [a for a, b in edges] + [b for a, b in edges]
    cols = [b for a, b in edges] + [a for a, b in edges]
    W = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    return GraphState(W), n


def make_params(c, allow_outside_spinodal=False):
    return ParameterRegistry(
        alpha_bd=1.0, beta_bd=4.0, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=500,
    )


def test_default_blocks_outside_spinodal(small_torus):
    """Default behavior: c=0.10 outside spinodal raises FATAL."""
    graph, n = small_torus
    p = make_params(c=0.10)
    valid, V, W = p.validate(fiedler_eigenvalue=graph.fiedler)
    assert not valid, "Default validate should reject c=0.10"
    assert any("outside spinodal" in v for v in V), \
        f"Expected spinodal violation in V, got {V}"


def test_allow_outside_spinodal_demotes_to_warning(small_torus):
    """With allow_outside_spinodal=True, spinodal violation becomes WARNING."""
    graph, n = small_torus
    p = make_params(c=0.10)
    valid, V, W = p.validate(fiedler_eigenvalue=graph.fiedler,
                              allow_outside_spinodal=True)
    # No spinodal in violations
    assert not any("outside spinodal" in v for v in V), \
        f"Expected no spinodal in V, got {V}"
    # WARNING contains spinodal note
    assert any("outside spinodal" in w for w in W), \
        f"Expected spinodal warning in W, got {W}"


def test_default_within_spinodal_passes(small_torus):
    """c within spinodal passes regardless of override."""
    graph, n = small_torus
    p = make_params(c=0.5)
    valid, V, W = p.validate(fiedler_eigenvalue=graph.fiedler)
    assert valid, f"c=0.5 should pass; got V={V}"


def test_find_formation_default_raises_outside_spinodal(small_torus):
    """find_formation() with c=0.10 default raises ValueError."""
    graph, n = small_torus
    p = make_params(c=0.10)
    u_init = np.full(n, 0.10)
    with pytest.raises(ValueError, match="outside spinodal"):
        find_formation(graph, p, normalize=False, verbose=False, u_init=u_init)


def test_find_formation_allow_outside_spinodal_succeeds(small_torus):
    """find_formation() with allow_outside_spinodal=True runs at c=0.10."""
    graph, n = small_torus
    p = make_params(c=0.10)
    # Make an IC localized near (0, 0) for metastable formation
    L = 8
    i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    dx = np.minimum(np.abs(i_idx - 0), L - np.abs(i_idx - 0))
    dy = np.minimum(np.abs(j_idx - 0), L - np.abs(j_idx - 0))
    r = np.sqrt(dx**2 + dy**2).flatten()
    r0 = np.sqrt(0.10 * L * L / np.pi)
    u_init = 0.5 * (1.0 - np.tanh((r - r0) / 0.5))
    u_init = np.clip(u_init, 0.01, 0.99)

    res = find_formation(graph, p, normalize=False, verbose=False,
                         u_init=u_init, allow_outside_spinodal=True)
    # Should produce a result without raising
    assert res is not None
    assert isinstance(res.energy, float)
    # u should preserve volume
    assert abs(res.u.sum() - 0.10 * n) < 0.5  # within projection tolerance
