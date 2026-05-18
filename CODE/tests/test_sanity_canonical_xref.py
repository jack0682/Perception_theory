"""Tests for exp90 sanity infra — canonical_k2_hash + subthreshold_demo_check.

W8-Day1 Track C. Confirms:
  - Hash idempotence (same input -> same output).
  - Hash permutation invariance (label swap leaves hash unchanged).
  - Hash distinguishes genuine structural differences.
  - subthreshold_demo_check returns the (l_second/l_max, Lambda) pair
    and correctly classifies a forced sub-threshold case and an
    overlapping case.

Run:
    cd CODE
    python3 -m pytest tests/test_sanity_canonical_xref.py -v
"""

import numpy as np
import pytest

from scc.graph import GraphState
from experiments.exp90_sanity_canonical_xref import (
    canonical_k2_hash,
    subthreshold_demo_check,
    SubthresholdReport,
)
from tests.conftest import make_params


# =============================================================================
# canonical_k2_hash
# =============================================================================

class TestCanonicalK2Hash:
    """Hash structure-only, label-invariant, idempotent."""

    @staticmethod
    def _disjoint_pair(n: int, split: int):
        u1 = np.zeros(n)
        u2 = np.zeros(n)
        u1[:split] = 0.9
        u2[split:] = 0.9
        return [u1, u2]

    def test_idempotence(self):
        """Same fields called twice -> same hash."""
        fields = self._disjoint_pair(100, 50)
        h1 = canonical_k2_hash(fields)
        h2 = canonical_k2_hash(fields)
        assert h1 == h2
        assert len(h1) == 64  # SHA256 hex

    def test_permutation_invariance(self):
        """Swap formation labels -> same hash (V-AFD/R-2 duplicate detection)."""
        fields_A = self._disjoint_pair(100, 50)
        fields_B = [fields_A[1].copy(), fields_A[0].copy()]
        assert canonical_k2_hash(fields_A) == canonical_k2_hash(fields_B)

    def test_distinguishes_structural_difference(self):
        """Shift the split by one site -> different hash."""
        f_A = self._disjoint_pair(100, 50)
        f_C = self._disjoint_pair(100, 51)
        assert canonical_k2_hash(f_A) != canonical_k2_hash(f_C)

    def test_threshold_dependence(self):
        """Different theta_core can produce different hashes."""
        u1 = np.zeros(20)
        u2 = np.zeros(20)
        u1[:10] = 0.6
        u2[10:] = 0.4
        h_low = canonical_k2_hash([u1, u2], theta_core=0.3)
        h_high = canonical_k2_hash([u1, u2], theta_core=0.5)
        assert h_low != h_high

    def test_empty_fields_returns_valid_digest(self):
        h = canonical_k2_hash([])
        assert isinstance(h, str)
        assert len(h) == 64

    def test_k_geq_2_permutation_invariance(self):
        """Hash is permutation invariant for K=3 as well."""
        n = 60
        u1 = np.zeros(n); u1[:20] = 0.9
        u2 = np.zeros(n); u2[20:40] = 0.9
        u3 = np.zeros(n); u3[40:] = 0.9
        fields_123 = [u1, u2, u3]
        fields_321 = [u3, u2, u1]
        fields_213 = [u2, u1, u3]
        h = canonical_k2_hash(fields_123)
        assert canonical_k2_hash(fields_321) == h
        assert canonical_k2_hash(fields_213) == h


# =============================================================================
# subthreshold_demo_check
# =============================================================================

class TestSubthresholdDemoCheck:
    """(l_second/l_max, Lambda_coupling) recording + classification."""

    @pytest.fixture
    def graph_15x15(self):
        return GraphState.grid_2d(15, 15)

    @pytest.fixture
    def params(self):
        return make_params()

    def test_returns_dataclass_with_all_fields(self, graph_15x15, params):
        n = graph_15x15.n
        u1 = np.zeros(n); u1[: n // 2] = 0.9
        u2 = np.zeros(n); u2[n // 2 :] = 0.9
        rep = subthreshold_demo_check([u1, u2], graph_15x15, params)
        assert isinstance(rep, SubthresholdReport)
        for attr in ("l_second", "l_max", "l_ratio", "Lambda",
                     "is_subthreshold", "regime"):
            assert hasattr(rep, attr)
        assert rep.l_max > 0
        assert 0.0 <= rep.l_ratio <= 1.0

    def test_disjoint_fields_are_subthreshold(self, graph_15x15, params):
        """Well-separated K=2 sits in sub-threshold demo regime."""
        n = graph_15x15.n
        u1 = np.zeros(n); u1[: n // 2] = 0.9
        u2 = np.zeros(n); u2[n // 2 :] = 0.9
        rep = subthreshold_demo_check([u1, u2], graph_15x15, params)
        assert rep.Lambda < 0.5, f"Expected weak coupling, got Lambda={rep.Lambda}"
        assert rep.is_subthreshold is True

    def test_fully_overlapping_fields_are_not_subthreshold(self, graph_15x15, params):
        """Two identical broad fields produce a high coupling and exit sub-threshold."""
        n = graph_15x15.n
        u = np.full(n, 0.55)
        rep = subthreshold_demo_check([u, u.copy()], graph_15x15, params,
                                      Lambda_threshold=0.5)
        assert rep.Lambda >= 0.5 or rep.is_subthreshold is False

    def test_metric_record_is_finite_and_serializable(self, graph_15x15, params):
        n = graph_15x15.n
        u1 = np.zeros(n); u1[: n // 2] = 0.9
        u2 = np.zeros(n); u2[n // 2 :] = 0.9
        rep = subthreshold_demo_check([u1, u2], graph_15x15, params)
        d = rep.as_dict()
        assert np.isfinite(d["l_second"])
        assert np.isfinite(d["l_max"])
        assert np.isfinite(d["l_ratio"])
        assert np.isfinite(d["Lambda"])
        assert isinstance(d["is_subthreshold"], bool)
        assert isinstance(d["regime"], str)
