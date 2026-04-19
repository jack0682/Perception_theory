"""Diagnostic predicates: Bind, Sep, Inside, Persist -> diagnostic vector [0,1]^4.

Per brainstorming consensus, proto-cohesion is a diagnostic vector rather
than a Boolean conjunction.
"""
from __future__ import annotations
import numpy as np
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.operators import closure, distinction


class DiagnosticVector:
    """Diagnostic vector [Bind, Sep, Inside, Persist] in [0,1]^4."""

    def __init__(self, bind: float, sep: float, inside: float, persist: float = 1.0):
        self.bind = bind
        self.sep = sep
        self.inside = inside
        self.persist = persist

    @property
    def vector(self) -> np.ndarray:
        return np.array([self.bind, self.sep, self.inside, self.persist])

    @property
    def min_score(self) -> float:
        return float(np.min(self.vector))

    @property
    def mean_score(self) -> float:
        return float(np.mean(self.vector))

    def __repr__(self) -> str:
        return (f"DiagnosticVector(Bind={self.bind:.3f}, Sep={self.sep:.3f}, "
                f"Inside={self.inside:.3f}, Persist={self.persist:.3f})")


def bind_predicate(u: np.ndarray, graph: GraphState, params: ParameterRegistry) -> float:
    """Bind = 1 - ||u - Cl_t(u)||_2 / sqrt(n).  (Spec Section 7.1)

    L2 norm divided by sqrt(n) for scale-independence.
    L-inf was proved unsuitable: boundary sites have inherent residuals ~0.21.
    """
    n = len(u)
    Cl_u = closure(u, graph, params)
    residual_norm = np.linalg.norm(u - Cl_u)
    return float(max(0.0, 1.0 - residual_norm / np.sqrt(n)))


def sep_predicate(u: np.ndarray, graph: GraphState, params: ParameterRegistry) -> float:
    """Sep = sum_x u(x)*D_t(x) / sum_x u(x).  (Spec Section 7.1, corrected I8)

    u-weighted average of distinction over formation support.
    The original C_t-weighted-over-all-nodes version averaged ~0.5 regardless
    of formation quality because exterior nodes (D≈0) and interior (D≈1)
    cancel out. Using u as weight naturally restricts to the formation support.
    """
    D_u = distinction(u, graph, params)
    m = np.sum(u)
    if m < 1e-15:
        return 0.0
    return float(np.sum(u * D_u) / m)


def inside_predicate(u: np.ndarray, graph: GraphState) -> float:
    """Inside = Q_morph = l_max * Artic.  (Spec Section 7.1)

    l_max: longest bar in H0 persistence diagram of superlevel-set filtration.
    Artic = 1 - l_second/l_max: articulation ratio.

    Uses graph-aware Union-Find for proper connected component tracking.
    """
    l_max, l_second = _persistence_h0_graph(u, graph)
    if l_max < 1e-15:
        return 0.0
    artic = 1.0 - l_second / l_max
    c = float(np.mean(u))
    if c > 1 - 1e-10:  # near-uniform at ceiling
        return 0.0
    normalized = max(0.0, (l_max - c) / (1.0 - c)) * artic
    return float(normalized)


def _persistence_h0_graph(u: np.ndarray, graph: GraphState) -> tuple[float, float]:
    """H0 persistence of superlevel-set filtration using graph adjacency.

    Process nodes in decreasing u order. When node x appears, connect to
    already-active neighbors. Track birth/death of connected components.
    Returns (l_max, l_second) = lengths of two longest bars.
    """
    n = graph.n
    if n == 0:
        return 0.0, 0.0
    if n == 1:
        return float(u[0]), 0.0

    order = np.argsort(-u)  # decreasing u

    # Build adjacency list
    W_coo = graph.W.tocoo()
    adj: list[list[int]] = [[] for _ in range(n)]
    for i, j in zip(W_coo.row, W_coo.col):
        adj[i].append(j)

    parent = np.arange(n, dtype=int)
    birth_val = np.zeros(n, dtype=float)
    active = np.zeros(n, dtype=bool)
    bars: list[float] = []

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for idx in order:
        active[idx] = True
        birth_val[idx] = u[idx]

        for nb in adj[idx]:
            if not active[nb]:
                continue
            ri, rn = find(idx), find(nb)
            if ri == rn:
                continue
            # Younger component dies (lower birth value = appeared later)
            if birth_val[ri] >= birth_val[rn]:
                # ri is older or same age, rn dies
                bars.append(float(birth_val[rn] - u[idx]))
                parent[rn] = ri
            else:
                bars.append(float(birth_val[ri] - u[idx]))
                parent[ri] = rn

    # The surviving component has an "infinite bar": birth = max(u), death = 0
    infinite_bar = float(np.max(u))

    all_bars = sorted([infinite_bar] + bars, reverse=True)
    l_max = all_bars[0]
    l_second = all_bars[1] if len(all_bars) > 1 else 0.0

    return l_max, l_second


def persist_predicate(u_prev: np.ndarray | None, u_curr: np.ndarray) -> float:
    """Persist in [0,1]: core-overlap approximation.

    Computes the soft overlap between consecutive fields, normalized by the
    larger volume:

        Persist = sum_i min(u_curr_i, u_prev_i) / max(sum u_curr, sum u_prev)

    This is a genuine overlap measure (not just an L2 distance proxy):
    - Returns 1.0 when fields are identical
    - Returns 0.0 when fields have disjoint support
    - Symmetric in (u_prev, u_curr)
    - Returns 1.0 for static (single-time) optimization (u_prev is None)

    NOTE: This does NOT implement the full spec formula (Spec §7.1), which
    requires a transport kernel M_{t->s} and core-to-core structural
    inheritance. That remains an open problem (T-Persist gaps 4-6).
    This core-overlap version is an intermediate approximation that captures
    spatial persistence of the soft field without requiring transport.
    """
    if u_prev is None:
        return 1.0
    overlap = float(np.sum(np.minimum(u_curr, u_prev)))
    max_volume = float(max(np.sum(u_curr), np.sum(u_prev)))
    if max_volume < 1e-12:
        return 0.0
    return float(min(1.0, overlap / max_volume))


def diagnostic_vector(
    u: np.ndarray,
    graph: GraphState,
    params: ParameterRegistry,
    u_prev: np.ndarray | None = None,
    M: np.ndarray | None = None,
) -> DiagnosticVector:
    """Compute the full diagnostic vector for a field u.

    When M (transport plan) and u_prev are provided, uses the spec-correct
    transport-based persist predicate from transport.py. Falls back to the
    core-overlap approximation when M is None.
    """
    if M is not None and u_prev is not None:
        from scc.transport import persist_transport
        persist = persist_transport(u_prev, u, M, params.theta_core)
    else:
        persist = persist_predicate(u_prev, u)

    return DiagnosticVector(
        bind=bind_predicate(u, graph, params),
        sep=sep_predicate(u, graph, params),
        inside=inside_predicate(u, graph),
        persist=persist,
    )


# Alias for optimizer compatibility
compute_diagnostics = diagnostic_vector


def inside_predicate_variance(u: np.ndarray, c: float) -> float:
    """Variance-based articulation proxy (fallback, not spec-compliant).

    Artic = Var(u) / (c*(1-c)). Cheap but does not use persistence.
    """
    max_var = c * (1.0 - c)
    if max_var < 1e-12:
        return 0.0
    return float(min(1.0, np.var(u) / max_var))
