"""Resolvent C_t wrappers for test compatibility.

Thin wrappers around scc.operators resolvent functions that accept
raw sparse matrices and param dicts instead of GraphState/ParameterRegistry.
"""

from __future__ import annotations

import numpy as np
import scipy.sparse as sp

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.operators import resolvent_diagonal as _resolvent_diagonal


def _make_graph_params(N_t: sp.spmatrix, params: dict):
    """Convert raw sparse matrix + dict to GraphState + ParameterRegistry."""
    graph = GraphState(N_t)
    p = ParameterRegistry(
        alpha_C=params.get("alpha_C", 0.5),
        k_neumann=params.get("k_neumann", 10),
        # Pass through other params that might be needed
        a_cl=params.get("a_cl", 3.5),
        eta_cl=params.get("eta_cl", 0.5),
        tau_cl=params.get("tau_cl", 0.5),
        a_D=params.get("a_D", 5.0),
        lambda_D=params.get("lambda_D", 1.0),
        tau_D=params.get("tau_D", 0.0),
        b_D=params.get("b_D", 0.0),
        alpha_bd=params.get("alpha_bd", 1.0),
        beta_bd=params.get("beta_bd", 10.0),
        volume_fraction=params.get("volume_fraction", 0.3),
        eps_agg=params.get("eps", 1e-10),
    )
    return graph, p


def resolvent_diagonal(u: np.ndarray, N_t: sp.spmatrix, params: dict) -> np.ndarray:
    """Compute diagonal of C_t = (I - alpha_C * W_sym)^{-1}.

    Returns array of C_t(x,x) values.
    """
    graph, p = _make_graph_params(N_t, params)
    return _resolvent_diagonal(u, graph, p)

