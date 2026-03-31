"""Predicate wrappers for test compatibility.

Thin wrappers around scc.diagnostics that accept raw sparse matrices
and param dicts instead of GraphState/ParameterRegistry.
"""

from __future__ import annotations

import numpy as np
import scipy.sparse as sp

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.diagnostics import (
    bind_predicate as _bind,
    sep_predicate as _sep,
    inside_predicate,
)
from scc.persistence import q_morph


def _make_graph_params(N_t: sp.spmatrix, params: dict):
    """Convert raw sparse matrix + dict to GraphState + ParameterRegistry."""
    graph = GraphState(N_t)
    p = ParameterRegistry(
        a_cl=params.get("a_cl", 3.5),
        eta_cl=params.get("eta_cl", 0.5),
        tau_cl=params.get("tau_cl", 0.5),
        a_D=params.get("a_D", 5.0),
        lambda_D=params.get("lambda_D", 1.0),
        tau_D=params.get("tau_D", 0.0),
        b_D=params.get("b_D", 0.0),
        alpha_C=params.get("alpha_C", 0.5),
        k_neumann=params.get("k_neumann", 10),
        alpha_bd=params.get("alpha_bd", 1.0),
        beta_bd=params.get("beta_bd", 10.0),
        volume_fraction=params.get("volume_fraction", 0.3),
        eps_agg=params.get("eps", 1e-10),
    )
    return graph, p


def bind_predicate(u: np.ndarray, N_t: sp.spmatrix, params: dict) -> float:
    """Bind = 1 - ||u - Cl(u)||_2 / sqrt(n).  (Spec §7.1)"""
    graph, p = _make_graph_params(N_t, params)
    return _bind(u, graph, p)


def sep_predicate(u: np.ndarray, N_t: sp.spmatrix, params: dict) -> float:
    """Sep = sum C_t(x,x)*D(x) / sum C_t(x,x).  (Spec §7.1, C_t-weighted)"""
    graph, p = _make_graph_params(N_t, params)
    return _sep(u, graph, p)


def diagnostic_vector(
    u: np.ndarray, N_t: sp.spmatrix, params: dict, grid_size: tuple[int, int] | int | None = None
) -> np.ndarray:
    """Compute diagnostic vector [Bind, Sep, Inside] in [0,1]^3.

    If grid_size is provided, uses it for Q_morph persistence computation.
    Otherwise infers from N_t shape assuming square grid.
    """
    graph, p = _make_graph_params(N_t, params)

    bind = _bind(u, graph, p)
    sep = _sep(u, graph, p)

    if grid_size is not None:
        inside = q_morph(u, grid_size)
    else:
        inside = inside_predicate(u, graph)

    return np.array([bind, sep, inside])
