"""Multi-formation K-field optimizer.

Implements the K-field architecture from I9: K coupled soft cohesion fields
with simplex participation constraint and inter-formation repulsion.

Energy: E(u^1,...,u^K) = sum_k E_self(u^k) + sum_{j<k} E_inter(u^j, u^k)
where E_inter = lambda_rep * sum_x u^j(x)*u^k(x)
Simplex barrier: lambda_bar * sum_x max(0, sum_k u^k(x) - 1)^2
"""

from __future__ import annotations

import numpy as np
import scipy.sparse.csgraph as csgraph
from typing import List, Optional

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import project_volume, FormationResult
from scc.diagnostics import compute_diagnostics, diagnostic_vector, DiagnosticVector
from scc.transport import transport_fixed_point, TransportResult


def find_k_formations(
    graph: GraphState,
    params: ParameterRegistry,
    K: int,
    lambda_rep: float = 10.0,
    lambda_bar: float = 100.0,
    m_per_formation: Optional[List[float]] = None,
    n_restarts: int = 3,
    max_iter: int = 2000,
    verbose: bool = False,
    init_fields: Optional[List[np.ndarray]] = None,
) -> List[FormationResult]:
    """Find K interacting formations via K-field energy minimization.

    Args:
        graph: GraphState
        params: ParameterRegistry (used for per-formation intra-energy)
        K: number of formations
        lambda_rep: repulsion strength between formations
        lambda_bar: simplex barrier strength (penalizes sum_k u^k > 1)
        m_per_formation: list of volumes per formation (default: equal split)
        n_restarts: number of random restarts
        max_iter: maximum iterations per restart
        verbose: print progress
        init_fields: optional list of K initial fields. When provided, used
            directly for restart 0; subsequent restarts add small perturbation.

    Returns:
        list of FormationResult, one per formation
    """
    n = graph.n

    # Volume allocation
    if m_per_formation is None:
        m_each = params.volume_fraction * n
        masses = [m_each] * K
    else:
        assert len(m_per_formation) == K
        masses = [m * n for m in m_per_formation]

    # Set up energy computer (shared for all formations' intra-energy)
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    best_fields = None
    best_total_energy = float('inf')

    for restart in range(n_restarts):
        if verbose:
            print(f"\n=== Restart {restart+1}/{n_restarts} ===")

        fields = _optimize_k_fields(
            graph, params, ec, K, masses, lambda_rep, lambda_bar,
            max_iter, seed=restart * 17 + 42, verbose=verbose,
            init_fields=init_fields if restart == 0 else None,
            init_perturb=init_fields if restart > 0 and init_fields is not None else None,
            perturb_seed=restart * 17 + 42,
        )

        # Compute total energy for this restart
        total_E = _total_energy(fields, ec, graph, lambda_rep, lambda_bar)
        if verbose:
            print(f"  Total energy: {total_E:.6f}")

        if total_E < best_total_energy:
            best_total_energy = total_E
            best_fields = [u.copy() for u in fields]

    # Compute diagnostics per formation
    assert best_fields is not None
    results = []
    for k in range(K):
        u_k = best_fields[k]
        E_self, terms = ec.energy(u_k)
        diag = compute_diagnostics(u_k, graph, params)
        results.append(FormationResult(
            u=u_k,
            energy=E_self,
            energy_terms=terms,
            diagnostics=diag,
            converged=True,
            n_iter=max_iter,
            energy_history=[],
            grad_norm_history=[],
        ))

    return results


def _optimize_k_fields(
    graph: GraphState,
    params: ParameterRegistry,
    ec: EnergyComputer,
    K: int,
    masses: List[float],
    lambda_rep: float,
    lambda_bar: float,
    max_iter: int,
    seed: int,
    verbose: bool,
    init_fields: Optional[List[np.ndarray]] = None,
    init_perturb: Optional[List[np.ndarray]] = None,
    perturb_seed: int = 0,
) -> List[np.ndarray]:
    """Run one restart of K-field projected gradient descent."""
    n = graph.n
    rng = np.random.RandomState(seed)

    # Initialize K fields
    fields: List[np.ndarray] = []
    if init_fields is not None:
        # Use provided fields directly
        for k in range(K):
            u_k = project_volume(init_fields[k].copy(), masses[k])
            fields.append(u_k)
    elif init_perturb is not None:
        # Perturb provided fields for diversity in later restarts
        prng = np.random.RandomState(perturb_seed)
        for k in range(K):
            noise = prng.randn(n) * 0.05
            u_k = init_perturb[k].copy() + noise
            u_k = project_volume(u_k, masses[k])
            fields.append(u_k)
    else:
        # Default: spatially biased initialization
        for k in range(K):
            c_k = masses[k] / n
            spatial_bias = _spatial_init(n, k, K, graph, rng)
            u_k = c_k + params.eps_init * spatial_bias
            u_k = project_volume(u_k, masses[k])
            fields.append(u_k)

    dt = params.dt_init
    prev_gnorm = float('inf')

    for tau in range(1, max_iter + 1):
        max_gnorm = 0.0

        for k in range(K):
            # Intra-formation gradient
            g_intra = ec.gradient(fields[k])

            # Repulsion gradient: d/du^k [lambda_rep * sum_{j!=k} u^j . u^k]
            # = lambda_rep * sum_{j!=k} u^j
            g_rep = np.zeros(n)
            for j in range(K):
                if j != k:
                    g_rep += fields[j]
            g_rep *= lambda_rep

            # Simplex barrier gradient: d/du^k [lambda_bar * sum_x max(0, S(x)-1)^2]
            # where S(x) = sum_k u^k(x)
            S = sum(fields)
            violation = np.maximum(0.0, S - 1.0)
            g_barrier = lambda_bar * 2.0 * violation

            # Total gradient, projected onto T(Sigma_m)
            g_total = g_intra + g_rep + g_barrier
            g_sigma = g_total - np.mean(g_total)
            gnorm = float(np.linalg.norm(g_sigma) / np.sqrt(n))
            max_gnorm = max(max_gnorm, gnorm)

            # Gradient step
            u_new = fields[k] - dt * g_sigma
            u_new = project_volume(u_new, masses[k])
            fields[k] = u_new

        # Adaptive step size
        if max_gnorm > prev_gnorm * 1.5 and tau > 5:
            dt *= 0.7
            dt = max(dt, 1e-8)
        elif max_gnorm < prev_gnorm * 0.95:
            dt *= 1.05
            dt = min(dt, 0.1)
        prev_gnorm = max_gnorm

        # Convergence check
        if tau > 20 and max_gnorm < params.eps_grad:
            if verbose:
                print(f"  Converged at iter {tau}, max |grad| = {max_gnorm:.2e}")
            break

        if verbose and tau % 500 == 0:
            total_E = _total_energy(fields, ec, graph, lambda_rep, lambda_bar)
            print(f"  iter {tau}: max|grad|={max_gnorm:.2e}, E_total={total_E:.4f}, dt={dt:.2e}")

    return fields


def _spatial_init(
    n: int, k: int, K: int, graph: GraphState, rng: np.random.RandomState,
) -> np.ndarray:
    """Create spatially biased perturbation to break K-fold symmetry.

    For grid graphs, bias formation k toward a different spatial region.
    For general graphs, use Fiedler-based separation.
    """
    try:
        v2 = graph.fiedler_vector()
        v2 = v2 / (np.linalg.norm(v2) + 1e-12)
        # Divide Fiedler vector into K bands
        percentiles = np.linspace(0, 100, K + 1)
        lo = np.percentile(v2, percentiles[k])
        hi = np.percentile(v2, percentiles[k + 1])
        mask = ((v2 >= lo) & (v2 <= hi)).astype(float)
        # Mix spatial bias with random noise
        bias = 0.5 * mask + 0.5 * rng.randn(n)
        return bias / (np.linalg.norm(bias) + 1e-12) * np.sqrt(n)
    except Exception:
        return rng.randn(n)


def _total_energy(
    fields: List[np.ndarray],
    ec: EnergyComputer,
    graph: GraphState,
    lambda_rep: float,
    lambda_bar: float,
) -> float:
    """Compute total K-field energy including interaction terms."""
    K = len(fields)
    E = 0.0

    # Intra-formation energies
    for k in range(K):
        E_k, _ = ec.energy(fields[k])
        E += E_k

    # Repulsion: lambda_rep * sum_{j<k} u^j . u^k
    for j in range(K):
        for k in range(j + 1, K):
            E += lambda_rep * float(fields[j] @ fields[k])

    # Simplex barrier: lambda_bar * sum_x max(0, S(x)-1)^2
    S = sum(fields)
    violation = np.maximum(0.0, S - 1.0)
    E += lambda_bar * float(violation @ violation)

    return E


def transport_k_formations(
    results_t: List[FormationResult],
    graph: GraphState,
    params: ParameterRegistry,
    lambda_rep: float = 10.0,
    lambda_bar: float = 100.0,
    phase2_mode: str = 'correction',
    coupled_cost: bool = False,
    **transport_kwargs,
) -> List[TransportResult]:
    """Transport K formations from time t to time s.

    Phase 1: Transport per formation via transport_fixed_point.
        If coupled_cost=True, uses repulsion-aware cost that penalizes
        sending mass to sites occupied by other formations.
    Phase 2: Post-hoc correction to enforce Σ_k u^k_s(x) ≤ 1.
        phase2_mode='correction': gradient correction (default, backward-compatible)
        phase2_mode='reoptimize': joint re-optimization via find_k_formations
        phase2_mode='none': no correction

    Valid in the well-separated regime (λ_rep large enough that
    formation supports are nearly disjoint). For overlapping formations,
    coupled transport (joint OT) would be needed — this is an open problem.

    Args:
        results_t: K FormationResult objects from find_k_formations at time t
        graph: GraphState (same spatial structure for both times)
        params: ParameterRegistry
        lambda_rep: inter-formation repulsion weight
        lambda_bar: simplex barrier weight
        phase2_mode: 'correction', 'reoptimize', or 'none'
        coupled_cost: if True, use repulsion-aware transport cost in Phase 1
        **transport_kwargs: passed to transport_fixed_point (sigma, gamma, eps_ot, etc.)

    Returns:
        List of K TransportResult objects with corrected u_s fields
    """
    if phase2_mode not in ('correction', 'reoptimize', 'none'):
        raise ValueError(f"phase2_mode must be 'correction', 'reoptimize', or 'none', got '{phase2_mode}'")

    K = len(results_t)
    n = graph.n

    # Phase 1: Transport per formation (optionally with coupled cost)
    tr_results = []
    if coupled_cost:
        # First pass: independent transport to get initial target fields
        initial_results = []
        for k in range(K):
            tr = transport_fixed_point(results_t[k].u, graph, params, **transport_kwargs)
            initial_results.append(tr)
        # Second pass: coupled transport using first-pass results as other_fields_s
        for k in range(K):
            other_fields = [initial_results[j].u_s for j in range(K) if j != k]
            kw = dict(transport_kwargs)
            kw['other_fields_s'] = other_fields
            kw['lambda_rep_transport'] = lambda_rep
            tr = transport_fixed_point(results_t[k].u, graph, params, **kw)
            tr_results.append(tr)
    else:
        for k in range(K):
            tr = transport_fixed_point(results_t[k].u, graph, params, **transport_kwargs)
            tr_results.append(tr)

    # Phase 2: Simplex correction
    fields_s = [tr.u_s.copy() for tr in tr_results]
    masses = [float(f.sum()) for f in fields_s]

    if phase2_mode == 'correction':
        # Existing gradient correction code
        S = sum(fields_s)
        max_violation = float(np.max(np.maximum(0.0, S - 1.0)))

        if max_violation > 0.01:
            dt = 0.001
            for _ in range(200):
                S = sum(fields_s)
                violation = np.maximum(0.0, S - 1.0)
                if float(np.max(violation)) < 0.01:
                    break

                for k in range(K):
                    g_rep = np.zeros(n)
                    for j in range(K):
                        if j != k:
                            g_rep += fields_s[j]
                    g_rep *= lambda_rep

                    g_barrier = lambda_bar * 2.0 * violation

                    g_total = g_rep + g_barrier
                    g_total -= np.mean(g_total)

                    fields_s[k] = fields_s[k] - dt * g_total
                    fields_s[k] = project_volume(fields_s[k], masses[k])

    elif phase2_mode == 'reoptimize':
        # Use transported fields as initialization for joint re-optimization
        reopt_results = find_k_formations(
            graph, params, K,
            lambda_rep=lambda_rep, lambda_bar=lambda_bar,
            init_fields=fields_s,
            max_iter=500, n_restarts=1,
        )
        fields_s = [r.u for r in reopt_results]

    elif phase2_mode == 'none':
        pass  # no correction

    # Build corrected TransportResult objects
    corrected = []
    for k in range(K):
        corrected.append(TransportResult(
            u_s=fields_s[k],
            u_t=tr_results[k].u_t,
            M=tr_results[k].M,
            converged=tr_results[k].converged,
            iterations=tr_results[k].iterations,
            fp_residuals=tr_results[k].fp_residuals,
            transport_energy=tr_results[k].transport_energy,
        ))

    return corrected


def multi_diagnostic_vector(
    results_t: List[FormationResult],
    results_s: Optional[List[FormationResult]],
    transport_results: List[TransportResult],
    graph: GraphState,
    params: ParameterRegistry,
) -> List[DiagnosticVector]:
    """Compute per-formation diagnostic vectors including transport-based persist.

    Args:
        results_t: K FormationResult objects at time t (source)
        results_s: K FormationResult objects at time s (unused, kept for API symmetry)
        transport_results: K TransportResult objects from transport_k_formations
        graph: GraphState
        params: ParameterRegistry

    Returns:
        List of K DiagnosticVector objects
    """
    diagnostics = []
    for k in range(len(results_t)):
        dv = diagnostic_vector(
            transport_results[k].u_s, graph, params,
            u_prev=results_t[k].u,
            M=transport_results[k].M,
        )
        diagnostics.append(dv)
    return diagnostics


def formation_overlap(fields: List[np.ndarray], theta_supp: float = 0.1) -> np.ndarray:
    """Compute pairwise overlap between formations.

    O(j,k) = number of nodes where both u^j >= theta_supp and u^k >= theta_supp.

    Returns:
        K×K symmetric matrix with overlap counts. Diagonal = support size.
    """
    K = len(fields)
    supports = [(f >= theta_supp) for f in fields]
    O = np.zeros((K, K), dtype=float)
    for j in range(K):
        for k in range(j, K):
            count = float(np.sum(supports[j] & supports[k]))
            O[j, k] = count
            O[k, j] = count
    return O


def inter_formation_distances(
    fields: List[np.ndarray],
    graph: GraphState,
    theta_supp: float = 0.1,
) -> np.ndarray:
    """Compute pairwise minimum graph distances between formation supports.

    For each pair (j, k), computes d_min(j,k) = min over x in supp(u^j),
    y in supp(u^k) of d_G(x,y), where supp(u^k) = {x : u^k(x) >= theta_supp}.

    Uses multi-source BFS from each formation's support set.

    Returns:
        K×K matrix with d_min(j,k). Diagonal is 0.
    """
    K = len(fields)
    n = graph.n

    # Compute support sets
    supports = [(f >= theta_supp) for f in fields]

    # Compute all-pairs shortest paths on unweighted graph
    adj_binary = (graph.W > 0).astype(np.float64)
    dist_matrix = csgraph.shortest_path(adj_binary, method="D", directed=False)

    # For each formation k, dist_from_k[x] = min distance from x to supp_k
    # = min over y in supp_k of dist_matrix[x, y]
    dist_from = []
    for k in range(K):
        supp_idx = np.where(supports[k])[0]
        if len(supp_idx) == 0:
            dist_from.append(np.full(n, np.inf))
        else:
            dist_from.append(dist_matrix[:, supp_idx].min(axis=1))

    # d_min(j, k) = min over x in supp_j of dist_from_k[x]
    D = np.zeros((K, K), dtype=float)
    for j in range(K):
        for k in range(K):
            if j == k:
                D[j, k] = 0.0
            else:
                supp_j = np.where(supports[j])[0]
                if len(supp_j) == 0:
                    D[j, k] = np.inf
                else:
                    D[j, k] = float(dist_from[k][supp_j].min())

    return D


def classify_regime(
    fields: List[np.ndarray],
    graph: GraphState,
    theta_supp: float = 0.1,
    D_sep: int = 3,
) -> str:
    """Classify K-formation interaction regime.

    Returns one of:
      'well-separated': all pairs have d_min >= D_sep
      'weakly-interacting': some d_min < D_sep but overlap confined to boundary
      'strongly-interacting': significant bulk overlap between formations
    """
    K = len(fields)
    if K <= 1:
        return 'well-separated'

    D = inter_formation_distances(fields, graph, theta_supp)

    # Check if all off-diagonal distances >= D_sep
    all_separated = True
    for j in range(K):
        for k in range(j + 1, K):
            if D[j, k] < D_sep:
                all_separated = False
                break
        if not all_separated:
            break

    if all_separated:
        return 'well-separated'

    # Compute overlap and core sizes
    O = formation_overlap(fields, theta_supp)
    core_sizes = [float(np.sum(f > 0.5)) for f in fields]
    min_core = min(core_sizes) if core_sizes else 1.0
    min_core = max(min_core, 1.0)  # avoid division by zero

    max_overlap = 0.0
    for j in range(K):
        for k in range(j + 1, K):
            max_overlap = max(max_overlap, O[j, k])

    if max_overlap / min_core < 0.2:
        return 'weakly-interacting'

    return 'strongly-interacting'
