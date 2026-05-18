"""exp90 — Sanity infra for canonical K=2 substrate cross-reference.

W8-Day1 Track C deliverable. Two operational tools used Day 2-5 as
*duplicate-detection* + *sub-threshold demo regression* guard.

Tools:
  - canonical_k2_hash(fields, theta_core)
      Permutation-invariant SHA256 hash of K=2 core-set structure.
      Same K=2 result re-packaged with different formation labels yields
      the same hash → detects V-AFD/R-2 style label-reshuffling re-packaging.

  - subthreshold_demo_check(fields, graph, params, ...)
      Records (l_second/l_max, Lambda_coupling) on every K=2 result.
      Flags whether the system sits in the *sub-threshold demo* regime
      (small Lambda + low spectral ratio), where R-2-style "K-tuple smooth"
      claims must be checked manually rather than asserted.

W8 anti-goal: scc/ untouched — helpers live in experiments/.

Run:
    cd CODE
    python3 experiments/exp90_sanity_canonical_xref.py
"""

from __future__ import annotations

import hashlib
import os
import sys
from dataclasses import dataclass, asdict
from typing import List, Sequence

import numpy as np

# Ensure scc/ importable when run as script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import coupling_strength, find_k_formations


# =============================================================================
# canonical_k2_hash
# =============================================================================

def canonical_k2_hash(
    fields: Sequence[np.ndarray],
    theta_core: float = 0.5,
) -> str:
    """Permutation-invariant SHA256 hash of K=2 core-set structure.

    The hash depends on the *unordered set* of per-formation core sets
    {{i : u^k(i) > theta_core} : k = 1..K}. Permuting formation labels
    leaves the hash invariant.

    Args:
        fields: list of K field arrays (any length, but only K=2 case is
            audited; K>2 also returns a valid permutation-invariant hash).
        theta_core: threshold on u defining a *core* site.

    Returns:
        64-char hex SHA256 digest.
    """
    if len(fields) == 0:
        return hashlib.sha256(b"empty").hexdigest()

    core_sets: List[tuple] = []
    for u in fields:
        u_arr = np.asarray(u)
        core = tuple(sorted(int(i) for i in np.where(u_arr > theta_core)[0]))
        core_sets.append(core)

    canonical = tuple(sorted(core_sets))
    payload = repr(canonical).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


# =============================================================================
# subthreshold_demo_check
# =============================================================================

@dataclass
class SubthresholdReport:
    l_second: float
    l_max: float
    l_ratio: float
    Lambda: float
    is_subthreshold: bool
    regime: str

    def as_dict(self) -> dict:
        return asdict(self)


def subthreshold_demo_check(
    fields: Sequence[np.ndarray],
    graph: GraphState,
    params: ParameterRegistry,
    lambda_rep: float = 10.0,
    Lambda_threshold: float = 0.5,
    l_ratio_threshold: float = 0.3,
) -> SubthresholdReport:
    """Force-record (l_second/l_max, Lambda_coupling) on a K=2 substrate.

    A *sub-threshold demo* is a K=2 configuration with Lambda below
    Lambda_threshold (weak coupling) and graph spectral ratio l_second/l_max
    below l_ratio_threshold (no strong second-mode resonance). In that
    regime, R-2-style "K-tuple-smooth" claims have repeatedly failed
    audit, and any new claim there must be checked manually.

    Args:
        fields: list of K field arrays.
        graph: underlying GraphState (provides Laplacian).
        params: ParameterRegistry.
        lambda_rep: K-field repulsion strength used in coupling diagnostic.
        Lambda_threshold: upper bound on Lambda for "sub-threshold".
        l_ratio_threshold: upper bound on l_second/l_max for "sub-threshold".

    Returns:
        SubthresholdReport — dataclass with both metrics + flag + regime.
    """
    L = graph.L
    if hasattr(L, "toarray"):
        L = L.toarray()
    eigs = np.sort(np.linalg.eigvalsh(L))
    l_second = float(eigs[1])
    l_max = float(eigs[-1])
    l_ratio = l_second / l_max if l_max > 1e-12 else 0.0

    cdict = coupling_strength(list(fields), graph, params, lambda_rep=lambda_rep)
    Lambda = float(cdict["Lambda"])
    regime = str(cdict.get("predicted_regime", "unknown"))

    is_subthreshold = (Lambda < Lambda_threshold) and (l_ratio < l_ratio_threshold)

    return SubthresholdReport(
        l_second=l_second,
        l_max=l_max,
        l_ratio=l_ratio,
        Lambda=Lambda,
        is_subthreshold=is_subthreshold,
        regime=regime,
    )


# =============================================================================
# Demonstration (run as script)
# =============================================================================

def _make_default_params() -> ParameterRegistry:
    return ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=10.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.5,
    )


def _two_disjoint_fields(n: int, split: int) -> List[np.ndarray]:
    """Synthetic K=2 fields: left half core, right half core (disjoint)."""
    u1 = np.zeros(n)
    u2 = np.zeros(n)
    u1[:split] = 0.9
    u2[split:] = 0.9
    return [u1, u2]


def main() -> int:
    print("=" * 70)
    print("exp90 — Sanity infra (canonical_k2_hash + subthreshold_demo_check)")
    print("=" * 70)

    graph = GraphState.grid_2d(15, 15)
    params = _make_default_params()
    n = graph.n
    print(f"Substrate: 15x15 grid, n = {n}")

    # ---- canonical_k2_hash demo ----
    print("\n[1] canonical_k2_hash — permutation invariance")
    fields_A = _two_disjoint_fields(n, n // 2)
    fields_B = [fields_A[1].copy(), fields_A[0].copy()]  # swapped labels
    h_A = canonical_k2_hash(fields_A)
    h_B = canonical_k2_hash(fields_B)
    print(f"  hash(A)         = {h_A[:16]}...")
    print(f"  hash(B=swap(A)) = {h_B[:16]}...")
    print(f"  invariance      : {'PASS' if h_A == h_B else 'FAIL'}")

    fields_C = _two_disjoint_fields(n, n // 2 + 1)  # shift by one site
    h_C = canonical_k2_hash(fields_C)
    print(f"  hash(C=shift1)  = {h_C[:16]}...")
    print(f"  distinct(A,C)   : {'PASS' if h_A != h_C else 'FAIL'}")

    # ---- subthreshold_demo_check demo ----
    print("\n[2] subthreshold_demo_check — well-separated case")
    rep_well = subthreshold_demo_check(fields_A, graph, params)
    for k, v in rep_well.as_dict().items():
        print(f"  {k:>16s} : {v}")

    print("\n[3] subthreshold_demo_check — overlapping case (forced)")
    u_overlap = np.full(n, 0.55)
    fields_overlap = [u_overlap, u_overlap.copy()]
    rep_over = subthreshold_demo_check(fields_overlap, graph, params)
    for k, v in rep_over.as_dict().items():
        print(f"  {k:>16s} : {v}")

    print("\n[4] Hash idempotence on real K=2 optimizer output")
    results = find_k_formations(graph, params, K=2, max_iter=300, n_restarts=1)
    fields_opt = [r.u for r in results]
    h1 = canonical_k2_hash(fields_opt)
    h2 = canonical_k2_hash(fields_opt)
    print(f"  hash(call1) = {h1[:16]}...")
    print(f"  hash(call2) = {h2[:16]}...")
    print(f"  idempotent  : {'PASS' if h1 == h2 else 'FAIL'}")

    print("\n" + "=" * 70)
    print("exp90 — OK")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(main())
