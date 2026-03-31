"""End-to-end integration tests — full SCC pipeline."""

import numpy as np
import pytest

from scc.optimizer import find_formation
from scc.energy import EnergyComputer
from scc.transport import transport_fixed_point
from scc.diagnostics import diagnostic_vector
from scc.multi import find_k_formations


def test_full_pipeline_single_formation(grid_10x10, default_params):
    """Graph → formation → transport → diagnostics."""
    # 1. Find formation
    result = find_formation(grid_10x10, default_params)
    assert result.converged

    # 2. Transport to "next time step" (same graph, slight perturbation)
    u_t = result.u
    tr = transport_fixed_point(u_t, grid_10x10, default_params)
    assert tr.converged

    # 3. Compute diagnostics with transport
    dv = diagnostic_vector(tr.u_s, grid_10x10, default_params, u_prev=u_t, M=tr.M)
    assert all(0 <= v <= 1 for v in [dv.bind, dv.sep, dv.inside, dv.persist])
    assert dv.persist > 0.5  # should be high for similar formations


def test_full_pipeline_multi_formation(grid_10x10, default_params):
    """Graph → K-formation → diagnostics for each."""
    results = find_k_formations(grid_10x10, default_params, K=2)
    assert len(results) == 2
    for r in results:
        assert 0 <= r.diagnostics.bind <= 1


def test_full_pipeline_energy_consistency(grid_10x10, default_params):
    """Energy computed via EnergyComputer matches optimizer's reported energy."""
    result = find_formation(grid_10x10, default_params, normalize=True)
    ec = EnergyComputer(grid_10x10, default_params)
    ec.normalize_weights()  # match optimizer's Hessian normalization
    recomputed, _ = ec.energy(result.u)
    assert abs(recomputed - result.energy) < 1e-6
