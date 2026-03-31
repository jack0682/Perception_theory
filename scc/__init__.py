"""Soft Cognitive Cohesion (SCC) computational package.

Implements the SCC theory from the Canonical Specification v2.0.
Core pipeline: field -> operators -> predicates -> energy -> optimization.
"""

from scc.params import ParameterRegistry
from scc.graph import GraphState
from scc.operators import closure, distinction, aggregation
from scc.energy import EnergyComputer
from scc.optimizer import find_formation, FormationResult
from scc.diagnostics import DiagnosticVector, diagnostic_vector, compute_diagnostics
from scc.multi import find_k_formations, transport_k_formations, multi_diagnostic_vector
from scc.transport import (
    cohesion_fingerprint, graph_distance_matrix, transport_cost,
    sinkhorn_partial_ot, transport_field, transport_fixed_point,
    TransportResult, persist_transport,
)

__all__ = [
    "ParameterRegistry",
    "GraphState",
    "closure",
    "distinction",
    "aggregation",
    "EnergyComputer",
    "find_formation",
    "FormationResult",
    "DiagnosticVector",
    "diagnostic_vector",
    "compute_diagnostics",
    "find_k_formations",
    "transport_k_formations",
    "multi_diagnostic_vector",
    "cohesion_fingerprint",
    "graph_distance_matrix",
    "transport_cost",
    "sinkhorn_partial_ot",
    "transport_field",
    "transport_fixed_point",
    "TransportResult",
    "persist_transport",
]
