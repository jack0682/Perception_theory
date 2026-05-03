# sigma_rich_vs_standard_R23.md — σ_rich vs σ_standard Equivalence Test on R23 Dataset

**Status:** working draft (W5 Day 4 PM, Task #35).
**Created:** 2026-04-30 (W5 Day 4 PM).
**Type:** Empirical equivalence + discrimination test design — σ_rich extension vs σ_standard baseline on R23 canonical dataset. OP-0009-Emp (R23 F=9 σ verification) sub-target.
**Author origin:** Task #35; companion to σ_rich foundation cluster (Tasks #1-4, #34, #48).
**Canonical refs:** §11.1 Commitment 14, 14-Multi, 16, 18 (CV-1.7 candidate); §13 T-σ-* family; §15 OP-0008, OP-0009-Emp.
**Working refs:** `sigma_rich_augmentation.md`, `sigma_rich_centroid_derivation.md` (Task #1), `sigma_rich_orientation_derivation.md` (Task #2), `sigma_rich_wigner_derivation.md` (Task #3), `sigma_rich_phi_proof.md` (Task #4), `nq242c_explicit_construction.md` (companion T²_20 numerical anchor).

---

## §1. Mission

> **"R23 canonical dataset 위에서 σ_rich vs σ_standard 의 (E1) compatibility (σ_rich ⊇ σ_standard) 와 (E2) strict discrimination (σ_rich distinguishes σ_standard-degenerate configurations) 를 numerically verify. OP-0009-Emp (R23 F=9 σ verification) sub-target. NQ-242c (T²_20) 와 complementary - real-graph anchor."**

이 working file 은 σ_rich foundation cluster 의 *empirical anchor on canonical dataset*. NQ-242c-Rich (Tasks #6 of `nq242c_explicit_construction.md`) 가 합성 graph $T^2_{20}$ 위에서의 anchor 이며, 이 file 은 R23 (canonical empirical anchor) 위에서의 *실제* σ-framework 검증.

**핵심 deliverables**:
1. R23 dataset config selection (§2).
2. σ_standard computation protocol (§3).
3. σ_rich computation protocol (§4).
4. (E1) compatibility test (§5).
5. (E2) strict discrimination test (§6).
6. NQ-242c cross-validation (§7).
7. Cat criteria for OP-0009-Emp closure (§8).
8. Numerical script outline (§9).

---

## §2. R23 Dataset Configuration Selection

### §2.1 R23 dataset overview

R23 = canonical R23 dataset (per `canonical/canonical.md` references in W4-04-23 measurements). Specifications:
- Graph: 2D lattice (specific dimension per dataset spec).
- Per-formation profile: tanh-disks at canonical default sites.
- Default ground state: F=9 (per OP-0009-Emp current empirical observation).

### §2.2 Test configurations

Three R23 configurations chosen to span Cat A / Cat B σ-framework anchors:

**Config R23-F1**: F=1 uniform minimizer ($u = c\mathbf{1}$ at $\beta < \beta_{\mathrm{crit}}^{(2)}$).
- σ_standard anchor: T-σ-Theorem-3 Cat A (uniform on $D_4$ grid).
- Expected σ_rich: trivial extension — single formation centroid at lattice center; isotropic inertia tensor; no $W_{jk}$ (no cross-pairs).

**Config R23-F2**: F=2 first pitchfork minimizer ($\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$).
- σ_standard anchor: T-σ-Theorem-4 Cat B with finite-L caveat (per `sigma_theorem4_canonical_revision.md` Task #63).
- Expected σ_rich: 2 centroids at axis-aligned positions; 2 inertia tensors (broken $D_4 \to \mathbb{Z}_2$); 1 cross-pair $W_{12}$.

**Config R23-F9**: F=9 default ground state ($\beta \gg \beta_{\mathrm{crit}}^{(2)}$, deep nonlinear regime).
- σ_standard: empirical only (NQ-141, no Cat A theorem).
- Expected σ_rich: 9 centroids; 9 inertia tensors; $\binom{9}{2} = 36$ pairs $W_{jk}$.

### §2.3 Why these three

- **F=1**: trivial-extension verification (E1 compatibility at sanity-check level).
- **F=2**: first-pitchfork validation; intersection with T-σ-Theorem-4 + Wave 3 finite-L finding.
- **F=9**: empirical-anchor verification (OP-0009-Emp) — addresses canonical's lack of Cat A claim at default ground state.

---

## §3. σ_standard Computation Protocol

### §3.1 Per Commitment 14-Multi (D-6a CV-1.5.1)

For each R23 configuration $\mathbf{u}^*$:
$$\sigma_{\mathrm{multi}}^{A,\mathrm{standard}}(\mathbf{u}^*) := (\mathcal{F}_{\mathrm{total}}; \{\sigma_j\}_{j=1}^{K_{\mathrm{act}}}; \{\sigma_{jk}\}_{j<k})$$
where $\sigma_j = (n_j^{(p)}, [\rho_j^{(p)}], \lambda_j^{(p)})_p$ per-formation Hessian eigenvalue/irrep/nodal triples.

### §3.2 Numerical pipeline

Existing infrastructure per `scc/diagnostics.py` (CV-1.5):
1. Load R23 graph + Hessian computation: `scc.diagnostics.compute_hessian_multi(u_star, params)`.
2. Diagonalize per-formation $H_{jj}$ blocks.
3. Identify irrep labels via Aut(G)-orbit analysis on eigenvectors.
4. Count Courant nodal domains.
5. Assemble σ-tuple per Commitment 14-Multi.

### §3.3 Precision convention

Round eigenvalues to $10^{-3}$ precision (qualitative-tuple convention per `nq242c_explicit_construction.md` §2.4). σ-tuple compared as multi-sets modulo $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$.

---

## §4. σ_rich Computation Protocol

### §4.1 Per Commitment 18 (CV-1.7 candidate)

For each R23 configuration $\mathbf{u}^*$:
$$\sigma_{\mathrm{rich}}(\mathbf{u}^*) := (\sigma_{\mathrm{standard}}; \{c_j\}; \{\Theta_j\}; \{W_{jk}\})$$
per Commitment 18 of `commitment_18_sigma_rich_packet.md` §2.

### §4.2 Centroid extraction (Task #1)

$c_j = \sum_x \iota(x) u^{(j)}(x) / \sum_x u^{(j)}(x)$ for each active $j$.
Embedding $\iota$: R23 lattice coordinates (Convention E per `sigma_rich_VR_phase1.md` §3.2).

### §4.3 Orientation extraction (Task #2)

$M_j = \sum_x u^{(j)}(x) (\iota(x) - c_j)(\iota(x) - c_j)^T$; spectral decomposition $\Theta_j = (\mu_{j,\alpha}, [v_{j,\alpha}])_\alpha$ with sign convention (Convention 6.1 of `sigma_rich_orientation_derivation.md`).

### §4.4 Wigner-data extraction (Task #3)

For each pair $(j, k)$:
- Compute cross-block 2×2 sub-Hessian $\tilde H_{jk}$.
- Identify Goldstone-pair subspace $V^{\mathrm{Gold}}_{jk}$ (lowest 2-4 eigenvectors of $\tilde H_{jk}$ corresponding to per-formation translation modes).
- Extract $\Delta_{jk}^{\mathrm{Gold}}$ (gap), $\theta_{jk}^{\mathrm{mix}}$ (mixing angle), $s_{jk}^{\mathrm{trend}}$ (temporal sign — undefined at static).

For static R23 (no trajectory): $s_{jk}^{\mathrm{trend}}$ undefined; report $W_{jk} = (\Delta_{jk}^{\mathrm{Gold}}, \theta_{jk}^{\mathrm{mix}}, \text{N/A})$.

### §4.5 Numerical pipeline

NEW W6+ infrastructure per `scc/sigma_rich.py` module (Task #58, in progress by sigma-rich-coder):
1. `compute_centroid(u_j, graph)` → `c_j`.
2. `compute_inertia_tensor(u_j, graph)` → `M_j`; spectral decomposition.
3. `compute_wigner_data(u_j, u_k, graph, params)` → `W_jk`.
4. Assemble σ_rich tuple.

---

## §5. (E1) Compatibility Test

### §5.1 Claim

**Test (E1)**: For each R23 configuration, $\sigma_{\mathrm{rich}}(\mathbf{u}^*)$ contains $\sigma_{\mathrm{standard}}(\mathbf{u}^*)$ as the first component (definitional inclusion).

### §5.2 Verification

- Extract $\sigma_{\mathrm{rich}}^{\mathrm{tuple}}[0] = \sigma_{\mathrm{standard}}$ component of σ_rich.
- Verify equality (component-wise) with separately-computed $\sigma_{\mathrm{standard}}$ via §3 protocol.

**Pass criterion**: $\sigma_{\mathrm{rich}}^{\mathrm{tuple}}[0] = \sigma_{\mathrm{standard}}$ exactly (modulo numerical precision).

This is **Cat A by definition** — σ_rich definition Commitment 18 §2 explicitly includes $\sigma_{\mathrm{multi}}^{A,\mathrm{standard}}$ as first component. Test is a sanity check; failure indicates implementation bug.

### §5.3 Expected outcome

PASS for all 3 configurations (F=1, F=2, F=9). Fail mode: implementation bug in `scc/sigma_rich.py`.

---

## §6. (E2) Strict Discrimination Test

### §6.1 Claim

**Test (E2)**: σ_rich provides *strict* discrimination beyond σ_standard — i.e., there exist R23 configurations with same σ_standard but distinct σ_rich.

### §6.2 Construction (R23-specific)

R23 supports rotational symmetry; $D_4$-rotated F=2 configurations (e.g., horizontal $\phi_{(1,0)}$ vs vertical $\phi_{(0,1)}$ pitchfork direction):

- **R23-F2-H**: F=2 minimizer with pitchfork along $x$-axis ($u^* = c\mathbf{1} + a_\epsilon \phi_{(1,0)}$).
- **R23-F2-V**: F=2 minimizer with pitchfork along $y$-axis ($u^* = c\mathbf{1} + a_\epsilon \phi_{(0,1)}$).

Per T-σ-Theorem-4 (i') orbit-representative remark: both have *same* σ_standard up to $D_4$-orbit (same eigenvalue/irrep/nodal multi-set).

But σ_rich differentiates:
- Centroid set H: $\{c_1^H = (c_x - r, 0), c_2^H = (c_x + r, 0)\}$ (horizontal axis).
- Centroid set V: $\{c_1^V = (0, c_y - r), c_2^V = (0, c_y + r)\}$ (vertical axis).

These are **distinct centroid configurations** in $\mathbb{R}^2$; they are related by 90° rotation under $\mathrm{Aut}(G) = D_4$. Pair-distance multi-set (Aut-invariant feature per Task #1 Corollary 5.3) is the same: $\{2r\}$. ⇒ Aut-invariant features coincide, BUT canonical embedding-dependent representatives differ.

### §6.3 Refinement: F=9 anisotropy detection

For R23-F9: 9 formations with possibly *different orientation $\Theta_j$* due to anisotropic boundary effects (formations near edges have different shape than central formations).

- σ_standard: per-formation $\sigma_j$ for "near-edge" vs "central" formations may be similar at qualitative-tuple level (close eigenvalues + same irrep + same nodal count under multi-set rounding).
- σ_rich: per-formation $\Theta_j$ (inertia tensor eigenvalues + principal axis) distinguishes near-edge (anisotropic) from central (more isotropic).

### §6.4 Test outcomes

**Pass criterion (E2)**: at least one R23 configuration pair (e.g., R23-F9 with central vs near-edge formation comparison) has same σ_standard at qualitative-tuple level but distinct σ_rich (via $\Theta_j$ or $W_{jk}$ component).

**Cat target**: Cat B post-numerical execution; Cat A everywhere requires R22 audit (per `sigma_theorem4_canonical_revision.md` §4).

---

## §7. NQ-242c Cross-Validation

### §7.1 Cross-graph consistency

NQ-242c (per `nq242c_explicit_construction.md`) tests σ_rich vs σ_standard on $T^2_{20}$ equilateral vs isoceles disk-triangle.

This file (R23) tests on real canonical dataset.

**Cross-validation**: σ_rich strict-discrimination property should hold on **both** graph classes:
- $T^2_{20}$: NQ-242c (translation-invariant, $D_4$ + $\mathbb{Z}_{20}^2$ Aut).
- R23: this file (R23-specific Aut group).

If both pass: σ_rich strict-discrimination is *graph-class universal* — supports CN17 universality intuition.

If only one passes: graph-class-dependence registered as caveat.

### §7.2 Combined result expected

| Graph | (E1) compatibility | (E2) strict discrimination |
|---|---|---|
| $T^2_{20}$ equilateral vs isoceles | PASS (definitional) | PASS (centroid set distinct) |
| R23 F=1 | PASS | N/A (only 1 formation) |
| R23 F=2-H vs F=2-V | PASS | PASS (centroid axis-aligned distinct) |
| R23 F=9 central vs edge | PASS | PASS (orientation $\Theta_j$ distinct) |

If table fully confirmed: σ_rich strict-discrimination universally established.

---

## §8. OP-0009-Emp Closure

### §8.1 OP-0009-Emp recap

Per `theorem_status.md` (Open Problems Catalog) OP-0009 sub-item:
> **OP-0009-Emp (R23 F=9 σ verification)**: σ-framework Cat A claims (CV-1.5) anchored at F=1 uniform / F=2 first-pitchfork; F=9 default ground state σ behavior empirical only (NQ-141). **OPEN** (OAT-7 W6 Day 5+6).

### §8.2 This file's contribution

R23-F9 σ_rich computation provides:
- σ_standard at F=9 (existing infrastructure CV-1.5; may not yield Cat A claim).
- σ_rich at F=9 (NEW W6+ infrastructure): characterizes 9-formation centroid configuration + 9 orientation tensors + 36 cross-pair Wigner-data.

If E1+E2 PASS at F=9: σ_rich provides characterization beyond σ_standard for empirical default ground state — addresses OP-0009-Emp partially.

### §8.3 Cat A path

Cat A claim for F=9 σ_rich requires:
- Theoretical proof of F=9 minimizer existence (T-Birth-Parametric extension to deep nonlinear regime).
- σ_rich Aut-invariance proof (R1 of `sigma_rich_augmentation.md` §10.4 — Tasks #1+#2+#3 establish).
- F=9-specific irrep-decomposition closed-form (W12+ work).

This file's empirical anchor + Tasks #1-4 theory + R22 audit (`sigma_theorem4_canonical_revision.md` §4) collectively address OP-0009-Emp at Cat B target level.

---

## §9. Numerical Script Outline

### §9.1 Script structure

`CODE/scripts/sigma_rich_vs_standard_R23.py`:
```python
"""
σ_rich vs σ_standard equivalence + discrimination test on R23 canonical dataset.
Companion to NQ-242c (T²_20). OP-0009-Emp sub-target.
DO NOT RUN at design phase (W5 Day 4); execute at W6 Day 1-3 once scc/sigma_rich.py module is ready.
"""

import numpy as np
import json
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.diagnostics import compute_sigma_tuple_multi
# from scc.sigma_rich import compute_sigma_rich  # NEW W6 Day 1-3

R23_CONFIGS = {
    'R23-F1': {'beta': 2.0, 'IC': 'uniform', 'expected_F': 1},
    'R23-F2-H': {'beta': 4.5, 'IC': 'pitchfork-x', 'expected_F': 2},
    'R23-F2-V': {'beta': 4.5, 'IC': 'pitchfork-y', 'expected_F': 2},
    'R23-F9': {'beta': 30.0, 'IC': 'r23-default', 'expected_F': 9},
}

def load_R23_graph():
    """Load R23 canonical dataset graph + parameters."""
    return GraphState.load_R23()  # to be implemented; placeholder

def setup_initial_condition(graph, config_id, M=90):
    """Return IC state for given R23 config."""
    if config_id == 'R23-F1':
        return uniform_IC(graph, M)
    elif config_id == 'R23-F2-H':
        return pitchfork_IC(graph, M, axis='x')
    elif config_id == 'R23-F2-V':
        return pitchfork_IC(graph, M, axis='y')
    elif config_id == 'R23-F9':
        return r23_default_IC(graph, M)

def relax_to_minimizer(graph, params, IC, T_max=200, dt=0.01):
    """Gradient flow to minimizer."""
    return gradient_flow(graph, params, IC, T_max, dt)

def test_E1_compatibility(sigma_rich_tuple, sigma_standard_tuple):
    """σ_rich first component equals σ_standard."""
    return sigma_rich_tuple[0] == sigma_standard_tuple

def test_E2_discrimination(configs_results):
    """At least one config pair has same σ_standard but distinct σ_rich."""
    pairs_distinguished = []
    for (id_A, res_A), (id_B, res_B) in itertools.combinations(configs_results.items(), 2):
        if res_A['sigma_standard'] == res_B['sigma_standard']:  # qualitative tuple match
            if res_A['sigma_rich'] != res_B['sigma_rich']:
                pairs_distinguished.append((id_A, id_B))
    return len(pairs_distinguished) > 0, pairs_distinguished

def main():
    graph = load_R23_graph()
    
    results = {}
    for config_id, config in R23_CONFIGS.items():
        params = ParameterRegistry(beta=config['beta'], lambda_rep=0.1, alpha=1.0, a_cl=2.0)
        IC = setup_initial_condition(graph, config_id)
        u_star = relax_to_minimizer(graph, params, IC)
        
        # Verify expected F (sanity)
        F_observed = count_formations(u_star)
        assert F_observed == config['expected_F'], f"{config_id}: expected F={config['expected_F']}, got {F_observed}"
        
        sigma_std = compute_sigma_tuple_multi(graph, params, u_star, precision=1e-3)
        sigma_rich = compute_sigma_rich(graph, params, u_star)
        
        # E1 compatibility
        E1_pass = test_E1_compatibility(sigma_rich, sigma_std)
        
        results[config_id] = {
            'sigma_standard': sigma_std,
            'sigma_rich': sigma_rich,
            'E1_pass': E1_pass,
            'F_observed': F_observed,
            'minimizer': u_star,
        }
    
    # E2 discrimination across all config pairs
    E2_pass, distinguished_pairs = test_E2_discrimination(results)
    
    # Save
    output = {
        'configs': {cid: {k: v for k, v in r.items() if k != 'minimizer'} for cid, r in results.items()},
        'E1_all_pass': all(r['E1_pass'] for r in results.values()),
        'E2_pass': E2_pass,
        'E2_distinguished_pairs': distinguished_pairs,
        'metadata': {'date': '2026-04-30', 'task': '#35'},
    }
    with open('results/sigma_rich_vs_standard_R23.json', 'w') as f:
        json.dump(output, f, indent=2)

if __name__ == '__main__':
    main()
```

### §9.2 Estimated runtime

- Load R23 graph + 4 minimizer extractions (T_max=200): ~30 min.
- σ_standard + σ_rich extraction × 4 configs: ~10 min.
- E1 + E2 tests: <1 min.
- **Total**: ~40 min single CPU.

### §9.3 Output schema

`CODE/scripts/results/sigma_rich_vs_standard_R23.json`:
```json
{
  "configs": {
    "R23-F1": {"sigma_standard": [...], "sigma_rich": [...], "E1_pass": true, "F_observed": 1},
    "R23-F2-H": {...},
    "R23-F2-V": {...},
    "R23-F9": {...}
  },
  "E1_all_pass": true,
  "E2_pass": true,
  "E2_distinguished_pairs": [["R23-F2-H", "R23-F2-V"], ...],
  "metadata": {...}
}
```

---

## §10. Cat Status and Promotion

### §10.1 Pre-execution Cat status

- **Cat A established**: design specification (this file).
- **Cat B target post-execution**: E1 + E2 numerical anchors (W6 Day 1-3).

### §10.2 Validation outcomes

(W1) E1 PASS: σ_rich ⊇ σ_standard verified — Commitment 18 definitional consistency.
(W2) E2 PASS: σ_rich strict discrimination — supports OP-0008 Path B + OP-0009-Emp partial closure.
(W3) NQ-242c cross-validation PASS: graph-class universal — supports CN17.

### §10.3 Promotion

If (W1)+(W2)+(W3) all PASS: Commitment 18 numerical anchor strengthened (CV-1.7 promotion path more confident); OP-0009-Emp PARTIALLY CLOSED.

If (W2) FAIL: σ_rich does not strictly extend σ_standard on R23 — register as graph-class-dependence caveat; revise Commitment 18 §3.4 distinguishing-power claim.

If (W3) FAIL: NQ-242c-only result — graph-class-dependence register; CN17 universality challenged.

---

## §11. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — `working/MF/` only.
- [x] **Silent resolution 0** — Cat status pre/post execution explicit; failure modes (W2/W3 FAIL) registered.
- [x] **No Research OS resurrection** — single-topic test design.
- [x] **Not reductive** — empirical test of theoretical claims; no external reduction.
- [x] **u_t primitive maintained** — both σ_standard and σ_rich operate on $u^{(j)}$.
- [x] **CN5 4-energy not merged** — N/A.
- [x] **K not dual-treated** — F (formation count) per Commitment 11/16; Commitment 18 (σ_rich) inheritance.
- [x] **No metastability claim without P-F flag** — N/A (static σ-extraction at minimizers).
- [x] **OP-0009-Emp explicit** — sub-target identified (§8); PARTIALLY CLOSED at Cat B post (W1)+(W2).
- [x] **Cross-validation explicit** — NQ-242c companion (§7); avoids single-graph anchor.
- [x] **R23 dataset**: existing canonical (no new dataset introduction); no Research OS R-/D-/T- registry resurrection.

---

## §12. References

### §12.1 Working files

- `working/MF/sigma_rich_augmentation.md` (foundation; Path B framework).
- `working/MF/sigma_rich_centroid_derivation.md` (Task #1).
- `working/MF/sigma_rich_orientation_derivation.md` (Task #2).
- `working/MF/sigma_rich_wigner_derivation.md` (Task #3).
- `working/MF/sigma_rich_phi_proof.md` (Task #4).
- `working/MF/sigma_rich_VR_phase1.md` (Task #34, V-R PH).
- `working/MF/nq242c_explicit_construction.md` ($T^2_{20}$ companion test).
- `working/MF/commitment_18_sigma_rich_packet.md` (CV-1.7 packet, Task #48).
- `working/SF/sigma_theorem4_canonical_revision.md` (T-σ-Theorem-4 finite-L caveat, Task #63).
- `working/MF/multi_formation_sigma.md` (D-6a static σ_multi^A).

### §12.2 Canonical refs

- `canonical/canonical.md` §11.1 Commitment 14, 14-Multi, 16, 18 (CV-1.7 candidate).
- `canonical/canonical.md` §13 T-σ-* family (T-σ-Lemma-1/2/3, T-σ-Theorem-3/4, T-σ-multi-A-Static, etc.).
- `canonical/theorem_status.md` OP-0008 (direct connection); OP-0009-Emp (sub-target).

### §12.3 CODE infrastructure

- `CODE/scc/diagnostics.py` (existing): σ_standard via Hessian.
- `CODE/scc/sigma_rich.py` (NEW W6 Day 1-3, Task #58 in_progress): σ_rich extraction.
- `CODE/scripts/sigma_rich_vs_standard_R23.py` (NEW W6 Day 4, this file §9).
- R23 dataset loader (`scc.graph.GraphState.load_R23()` placeholder).

### §12.4 NQ register

- **NQ-141**: original R23 F=9 empirical observation (no Cat A claim).
- **NQ-141 follow-up via this file**: σ_rich characterization adds beyond σ_standard.

---

**End of sigma_rich_vs_standard_R23.md.**

**Status: working draft. Task #35 complete (design phase). σ_rich vs σ_standard equivalence + discrimination test on R23 canonical dataset designed. 4 R23 configurations (F=1, F=2-H, F=2-V, F=9); 2 tests (E1 compatibility, E2 strict discrimination); cross-validation against NQ-242c (T²_20). OP-0009-Emp partial closure target at Cat B post-execution. Numerical script outline at CODE/scripts/sigma_rich_vs_standard_R23.py (NOT run); ~40 min runtime; depends on scc/sigma_rich.py module (Task #58 in_progress). All hard constraints verified. Forward: W6 Day 1-3 scc/sigma_rich.py completion → W6 Day 4 execution.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/sigma_rich_vs_standard_R23.md`
**Created:** 2026-04-30 (W5 Day 4 PM).
**Promotion target:** Commitment 18 CV-1.7 packet supplementary anchor (E1+E2 PASS strengthens promotion confidence).
