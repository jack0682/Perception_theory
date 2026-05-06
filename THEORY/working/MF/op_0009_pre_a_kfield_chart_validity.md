---
id: OP-0009-Pre-a-WF-2
type: working/architecture-tension
status: open — unresolved architecture migration
last_updated: 2026-05-06
---

# OP-0009-Pre-a: K-Field as Local Chart — Validity Conditions and Architecture Migration

**OP-ID:** OP-0009-Pre-a
**Title:** K-field Σ_M^K is a local coordinate chart within F_M(P), not the foundational state space
**Session:** W6 D4 Session D (2026-05-06)
**Related files:** `pre_objective_K_field_tension.md` (philosophical framing), `k_selection_a_free_energy.md`, `k_selection_b_kramers.md`, canonical §3.9–§3.11, §16 D-ST-4
**Status in theorem_status.md:** PARTIALLY RESOLVED — canonical argument established (D-ST-1..D-ST-4); architecture migration not yet complete

---

## 1. The Tension in One Sentence

The K-field product manifold $\Sigma_M^K = \prod_{j=1}^{K_{\mathrm{field}}} \Sigma_{m_j}$ was used as the foundational state space for multi-formation dynamics (canonical I9), but the correct foundational state space is $\mathcal{F}_M(\mathcal{P}) = \{\tilde{u} \in [0,1]^n : \sum_i \tilde{u}_i = M\}$ (canonical §3.9, D-ST-2), with $K_{\mathrm{act}}(\tilde{u}) = \#\mathrm{PersComp}(\tilde{u})$ as a derived observable (§3.11, D-ST-3).

The K-field chart is not wrong — it is a valid local coordinate system within one energy basin $\mathcal{A}_{K,\alpha}(\mathcal{P})$. The architecture migration question is: **under what conditions is the K-field chart a valid and non-degenerate local chart, and what happens when those conditions fail?**

---

## 2. Foundational State Space vs K-Field Chart

### 2.1 Foundational State Space (canonical)

$$\mathcal{F}_M(\mathcal{P}) = \bigl\{\tilde{u} \in [0,1]^n : \textstyle\sum_i \tilde{u}_i = M\bigr\}$$

This is the single-field mass-constrained space (canonical §3.9, D-ST-2 body). It is:
- **Complete**: every possible formation configuration lives here
- **K-agnostic**: K_act(ũ) is measured post-hoc via #PersComp (§3.11)
- **Topology-aware**: transitions between K-basins are natural (K-jumps are gradient-flow events)
- **The correct integration domain for Z_K**: $\mathcal{B}_K(\mathcal{P}) = \{\tilde{u} \in \mathcal{F}_M(\mathcal{P}) : K_{\mathrm{act}}(\tilde{u}) = K\}$ (D-ST-4)

### 2.2 K-Field Chart (local, derived)

$$\Sigma_M^K = \Sigma_{m_1} \times \cdots \times \Sigma_{m_K}, \quad m_j > 0, \quad \textstyle\sum_j m_j = M$$

This is a product of per-formation simplices (canonical I9). It is:
- **Local**: valid only within a single basin $\mathcal{A}_{K,\alpha}(\mathcal{P})$ where K_act is stable and fixed
- **K-indexed**: requires a fixed K and a labeling of formations j=1..K
- **Mass-partitioned**: requires fixed per-formation masses m_j (or a mass-allocation mechanism)
- **Useful for**: per-formation gradient descent (implemented in `multi.py:transport_k_formations`), sigma-signature computation (T-Commitment-14-Multi-Static)

### 2.3 The Chart Map

There is a natural map from the K-field chart to the foundational space:
$$\phi_K : \Sigma_M^K \to \mathcal{F}_M(\mathcal{P}), \quad \phi_K(u^{(1)}, \ldots, u^{(K)}) = \sum_{j=1}^K u^{(j)}$$

subject to the participation constraint $\sum_j u^{(j)}(x) \leq 1$ for all x. The image of $\phi_K$ lies within $\mathcal{B}_K(\mathcal{P})$ when the formations are well-separated.

The map is **not injective** in general (permutation symmetry: $S_K$ acts on Σ_M^K by label permutation, while $\mathcal{F}_M(\mathcal{P})$ is invariant). The moduli space is $\Sigma_M^K / S_K$ (unordered K-field, Tool A2 from `mathematical_scaffolding_4tools.md`).

---

## 3. Validity Conditions for the K-Field Chart

The K-field chart $\Sigma_M^K$ is a valid local coordinate for $\mathcal{F}_M(\mathcal{P})$ within basin $\mathcal{A}_{K,\alpha}(\mathcal{P})$ if and only if the following conditions hold:

### V1 (K-Stability). K_act is stable on the trajectory.

$K_{\mathrm{act}}(\tilde{u}(t)) = K$ for all $t$ in the time interval of interest. If K_act jumps (K-jump event: two formations merge or one splits), the K-field chart degenerates: one formation index $j$ becomes redundant or a new one needs to be introduced.

*Failure mode:* Near a K-jump event, $u^{(j)} \to 0$ for some j (formation death). The chart coordinate $m_j \to 0$ hits the boundary of $\Sigma_{m_j}$. The K-field chart needs to be replaced by a (K−1)-field chart after the merge.

*Operational check:* `K_act ≥ K_field_threshold` during gradient flow (implemented in `multi.py` via `persistent_component_count`).

### V2 (Basin Localization). The trajectory remains in a single basin $\mathcal{A}_{K,\alpha}(\mathcal{P})$.

If the energy landscape has multiple K-basins (e.g., two different K=2 configurations), the K-field chart tracks one of them. Inter-basin transitions are not captured by the chart.

*Failure mode:* If the gradient flow crosses a basin boundary (escapes to a different K=2 configuration), the labeling of formations j=1,2 may swap or permute. The K-field chart is still valid but the labeling needs updating.

*Operational check:* Monitor $\|\tilde{u}(t) - \tilde{u}^{(K)}_{\mathrm{ref}}\|$ where $\tilde{u}^{(K)}_{\mathrm{ref}}$ is the local minimum of the selected basin. If drift exceeds a threshold, re-identify the basin.

### V3 (Formation Separation). The K formations are well-separated.

$\langle u^{(j)}, u^{(k)} \rangle = \sum_x u^{(j)}(x) u^{(k)}(x) < \varepsilon$ for all $j \neq k$, for small $\varepsilon > 0$.

*Why needed:* The K-field participation constraint $\sum_j u^{(j)}(x) \leq 1$ can be tight. When two formation fields overlap significantly, the constraint is binding and the chart coordinates are not independent — the K-field chart loses its product structure.

*Operational check:* $\lambda_{\mathrm{rep}} \langle u^{(j)}, u^{(k)} \rangle$ repulsion energy is small relative to formation energy.

### V4 (Mass Budget). Each formation has non-negligible mass.

$m_j = \sum_x u^{(j)}(x) > m_{\min} > 0$ for all j.

*Why needed:* If $m_j \to 0$, the simplex $\Sigma_{m_j}$ collapses to a point and the j-th coordinate direction degenerates. The K-field chart has K−1 fewer degrees of freedom than expected.

*Operational check:* $m_j > \varepsilon_{\mathrm{mass}}$ for all j (implemented in `multi.py` as `mass_threshold`).

---

## 4. Unresolved Architecture Migration

The current canonical architecture uses K-field for multi-formation calculations (canonical I9, `multi.py`, sigma-signature). The foundational architecture (F_M(P), D-ST-2..D-ST-3) is registered in §3.9–§3.11 but not yet used as the primary computational framework.

**Migration requirement:** The multi-formation implementation should:
1. Use F_M(P) as the primary state space (single-field relaxation with K_act computed post-hoc)
2. Switch to K-field chart only when V1–V4 are satisfied (as a computational acceleration)
3. Detect V1 failures (K-jumps) and handle them via basin-switching, not K-field chart collapse

**Why this is unresolved:**
- The single-field F_M(P) optimizer in `optimizer.py:find_formation` works for K=1
- Multi-formation dynamics currently requires the K-field architecture (K separate fields with repulsion)
- A single-field optimizer that can find K≥2 configurations requires either: (a) multi-start + K_act post-hoc counting (implemented in `find_multi_formation`), or (b) a topological continuation method that tracks K-jumps
- Option (a) is computationally expensive and may miss configurations; option (b) is not yet implemented

**Architecture migration status:** OPEN (deferred to W11-W12 v2.0 canonical §1 amendment, per OP-0009 resolution timeline).

---

## 5. Σ_M^K vs B_K(P): The Integration Domain Fix

D-ST-4 (canonical §16) introduced the **topological sector** $\mathcal{B}_K(\mathcal{P}) \subset \mathcal{F}_M(\mathcal{P})$ as the correct integration domain for the partition function $Z_K(\mathcal{P})$, replacing the incorrect $\Sigma_M^K$.

Why $\Sigma_M^K$ was wrong as an integration domain:
- $\Sigma_M^K$ over-counts: it counts each K=2 configuration K! times (S_K permutation symmetry)
- $\Sigma_M^K$ under-counts: it misses configurations where K_act = K but the K-field labeling is degenerate (e.g., one formation has mass near zero)
- $\Sigma_M^K$ is K-field-specific: it presupposes the K-field architecture rather than deriving K from the field

Why $\mathcal{B}_K(\mathcal{P})$ is correct:
- $\mathcal{B}_K(\mathcal{P}) = \{\tilde{u} \in \mathcal{F}_M(\mathcal{P}) : K_{\mathrm{act}}(\tilde{u}) = K\}$ — exact K-sector in field space
- No over/under-counting (single-field, no labeling symmetry issue)
- K_act measured by #PersComp (§3.11), which is invariant to labeling

This domain fix is DONE (D-ST-4 registered in canonical §16). The chart validity conditions (§3 above) define when the K-field chart is a valid local coordinate within $\mathcal{B}_K(\mathcal{P})$.

---

## 6. What Remains Unresolved

| Sub-issue | Status | Blocker |
|---|---|---|
| F_M(P) as foundational state space (D-ST-2) | RESOLVED in §3.9 | None — canonical |
| K_act = #PersComp (D-ST-3) | RESOLVED in §3.11 | None — canonical |
| B_K(P) as integration domain (D-ST-4) | RESOLVED in §16 | P-F-A1 for T_* in Z_K |
| Chart validity conditions V1–V4 | FORMALIZED (this file) | Computational: V1 detector in multi.py |
| Architecture migration: F_M(P) primary | OPEN | Deferred v2.0 W11–W12 |
| K-jump handling in single-field optimizer | OPEN | Not implemented |
| Φ_K chart map injectivity (quotiented) | OPEN | Tool A2 in `mathematical_scaffolding_4tools.md` |

**Core unresolved claim:** The statement "Σ_M^K is a local chart within B_K(P)" needs a precise differential-geometric formulation: what is the chart domain, the chart map Φ_K, and the transition maps between charts at different K? This would make the architecture migration mathematically rigorous rather than conceptually stated.

**Promotion target:** v2.0 §1 ontological setup paragraph amendment (W11–W12), per OP-0009 resolution timeline in `theorem_status.md`.

---

---

## 7. Empirical Evidence: exp02d K-Field Endpoint Failure (Session F)

**Session:** W6 D4 Session F (2026-05-06)

exp02d (full 4-term SCC energy, 12×12 grid, β=20) provided a concrete empirical demonstration of V3/V1 chart invalidity when K-field endpoints are used as proxies for F_M(P) minima.

### 7.1 Setup

exp02d used `find_k_formations(graph, params, K=2, lambda_rep=10)` to generate K=2 endpoints for NEB barrier computation. This function minimizes the K-field energy on Σ_M^K (product space with repulsion term), NOT the single-field SCC energy on F_M(P).

### 7.2 The V3 Failure

The K=2 state produced is `ũ_A = clip(u^(1) + u^(2), 0, 1)` where `u^(1), u^(2)` are the two K-field components (repulsion-separated). At the K-field minimum, the repulsion energy `λ_rep⟨u^(1), u^(2)⟩` drives the components apart — creating a valley between the two bumps that is artificially deep relative to what the single-field energy alone would create.

V3 violation: `λ_rep⟨u^(j), u^(k)⟩` was large (λ_rep=10) → non-negligible participation constraint binding → K-field chart loses product structure at ũ_A.

Consequence: `ũ_A` is NOT a critical point of E_SCC(ũ) on F_M(P). Near `ũ_A`, the single-field projected gradient `∇_proj E_SCC(ũ_A) ≠ 0` (pointing toward partial merger or valley-filling). The NEB saddle therefore has LOWER energy than the K-field-derived "minimum", producing systematically negative barriers.

### 7.3 Experimental Results

All 18 conditions tested (3 Δz × 2 λ_z × 3 energy variants: gl_only / full_scc_no_sep / full_scc) showed negative barriers. The suggestive trend (smooth > flat for barrier magnitude) was obscured by the systematic negative offset from the invalid endpoint. All claims from exp02d are null — the barriers are artifacts.

### 7.4 Fix: exp02e

exp02e corrects the endpoint methodology by operating entirely in F_M(P):

1. `make_bimodal_init` — bimodal field with two bumps, no repulsion
2. `single_field_relax` — projected gradient descent on F_M(P) from bimodal init → genuine single-field local minimum ũ*_{K2}
3. `is_local_minimum` — verify ‖∇_proj E_SCC(ũ*_{K2})‖_RMS < tol
4. `k_act_from_barcode` — verify K_act(ũ*_{K2}) = 2 via H0 Union-Find (graph-general)

This ensures the K=2 endpoint is a genuine critical point of E_SCC on F_M(P) before NEB is run.

### 7.5 OP-0009 Interpretation

This confirms the core claim of OP-0009-Pre-a: **K-field Σ_M^K and foundational F_M(P) give different local minima under the same SCC energy.** The K-field product energy (with repulsion λ_rep=10) creates artifacts when the combined field is projected back to F_M(P). Any methodology that uses K-field endpoints as proxies for F_M(P) minima is subject to this error unless V1–V4 are explicitly verified and the endpoint is validated via single-field relaxation.

**Experimental log:** `CODE/stereo_scc/experiments/exp02d_full_scc_smooth_barrier.py` (all 18 conditions, all barriers < 0). Fix: `CODE/experiments/exp02e_single_field_neb.py` (launched W6 D4 Session F, PID 80907).

---

## 8. Architecture Migration Policy (Session G, W6 D4)

**Operational policy derived from exp02d/exp02e evidence (§7):**

### 8.1 Mandatory single-field validation for foundational barrier claims

Any barrier computation used to support a **foundational claim** (theorem in canonical.md, Cat B or higher, P-F-A1 rate claims) **must** use endpoints that are genuine local minima of $\mathcal{E}_{\mathrm{SCC}}$ on $\mathcal{F}_M(\mathcal{P})$. The required validation pipeline:

1. **Generate candidate endpoint** — either bimodal init (exp02e approach) or any other F_M(P)-native initialization
2. **Relax in F_M(P)** — `single_field_relax` with energy-change stopping (NOT u-change; see exp02e bug-fix record)
3. **Verify is_local_minimum** — energy-probe test `|E(u) − E(u − dt·∇proj)| < tol` (NOT KKT-gap; see exp02e bug-fix record)
4. **Verify K_act** — `k_act_from_barcode` (H0 Union-Find, graph-general)

K-field chart endpoints (`find_k_formations` with repulsion) may be used as *initialization* but NOT as validated endpoints without completing steps 2–4.

### 8.2 Architecture interpretation

The exp02d/exp02e contrast embodies the architecture migration in miniature:

| | exp02d | exp02e |
|---|---|---|
| State space | Σ_M^K (K-field product, repulsion) | F_M(P) (single-field, shared pool) |
| Energy | K-field energy + λ_rep repulsion | E_SCC single-field |
| Endpoint validity | NOT F_M(P) local minima | Verified F_M(P) local minima |
| NEB result | All barriers negative (artifacts) | Physical barriers (25% increase at β=10) |

**Conclusion:** Foundational dynamics = single-field / shared-pool on $\mathcal{F}_M(\mathcal{P})$. K-field chart = local computational tool (valid only under V1–V4, for K-stable, well-separated, mass-budgeted trajectories). The foundational level always requires F_M(P) validation.

### 8.3 Scope

This policy applies to:
- T-ST-5b and any smooth barrier-raising claims
- D-ST-4 Kramers rate barriers (ΔE in the exponent)
- Any future multi-formation barrier or saddle computation

It does NOT apply to:
- Exploratory experiments (diagnostic only, not canonical-bound)
- K-field chart experiments used only for K_act statistics (not barrier heights)

---

*Written W6 D4 Session D. Chart validity conditions V1–V4 formalized. Architecture migration registered as OPEN. Deferred to v2.0. §7 added Session F: exp02d K-field endpoint failure documented as empirical V3 violation evidence. §8 added Session G: architecture migration policy formalized from exp02d/exp02e contrast.*
