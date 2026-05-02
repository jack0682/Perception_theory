# Proof-Status Audit: \(K_{\mathrm{soft}}\), \(K_{\mathrm{bar}}\), and \(K_{\mathrm{act}}\)

**File:** `THEORY/working/MF/ksoft_kact_bridge_proof_status.md`  
**Document type:** non-canonical proof-status audit.  
**Created:** 2026-05-02, Work Package 3 after WQ-LAT-1.C.  
**Status:** working audit; no canonical promotion.

---

## 1. Status and Scope

This is a **non-canonical proof-status audit**. It does not modify canonical theory and does not promote any working result to canonical status.

This document audits the status of the bridge among:

$$
K_{\mathrm{act}}^\varepsilon,\qquad
K_{\mathrm{bar}}^{\ell_{\min}},\qquad
K_{\mathrm{soft}}^\phi.
$$

It uses WQ-2, WQ-LAT-1, WQ-LAT-1.B, and WQ-LAT-1.C as evidence. It separates definitions, empirical findings, lemma candidates, conjectures, and forbidden overclaims.

It uses the following evidence sources:

| Source | Role in this audit |
|---|---|
| `ksoft_kact_bridge_lemma.md` | WQ-2 bridge lemma and WQ-LAT-1.C phi-class correction |
| `wq_lat1_reservoir_resolution_sweep_results.md` | empirical reservoir-resolution sweep |
| `wq_lat1b_phi_envelope_refinement_results.md` | empirical phi-envelope refinement |
| `latent_index_space_design.md` | finite chart / latent reservoir interpretation |
| `reservoir_reinterpretation_of_K.md` | conceptual reinterpretation of the integer K family |
| `soft_K_definition.md` | base \(K_{\mathrm{soft}}\) definition and CSEH stability skeleton |
| `F_Kstep_K_triple.md` | surrounding count-diagnostic bridge |
| `K_status_commitment.md` | \(K_{\mathrm{field}}\) / \(K_{\mathrm{act}}\) two-tier status |
| `open_problems.md` | OP-0005 and OP-0008 status boundary |
| `theorem_status.md` | canonical theorem-status boundary |

This audit does **not** solve OP-0005. It does **not** solve OP-0008. It does **not** claim \(\sigma_{\mathrm{rich}}\) sufficiency. It does **not** identify \(K_{\mathrm{soft}}^\phi\) and \(K_{\mathrm{act}}^\varepsilon\) globally.

---

## 2. Object Glossary

| Object | Definition | Layer | Status | Meaning / warning |
|---|---|---|---|---|
| \(K_{\mathrm{field}}\) | finite number of available formation slots | finite chart / architectural cap | definitional / architectural | finite resolution of the latent index reservoir in the current finite model; not a primitive ontology |
| \(m_j(\mathbf u)\) | \(m_j(\mathbf u)=\sum_x u^{(j)}(x)\) | Layer II finite chart | definitional | mass assigned to labelled slot \(j\) |
| \(K_{\mathrm{act}}^\varepsilon(\mathbf u)\) | \(K_{\mathrm{act}}^\varepsilon(\mathbf u)=\#\{j:m_j(\mathbf u)>\varepsilon\}\) | Layer II finite chart | definitional | thresholded active-coordinate count; chart-dependent |
| \(U(\mathbf u)\) | \(U(\mathbf u)(x)=\sum_j u^{(j)}(x)\) | projection Layer II to Layer I | definitional | aggregate field; forgets finite labels |
| \(K_{\mathrm{bar}}^{\ell_{\min}}(U)\) | \(K_{\mathrm{bar}}^{\ell_{\min}}(U)=\#\{i:\ell_i(U)\ge\ell_{\min}\}\) | Layer I aggregate morphology | definitional hard-count observable | integer count of persistence-prominent \(H_0\) bars |
| \(K_{\mathrm{soft}}^\phi(U)\) | \(K_{\mathrm{soft}}^\phi(U)=\sum_i\phi(\ell_i(U))\) | Layer I aggregate morphology | definitional once \(\phi\) is fixed | soft morphology count; not chart-invariant for arbitrary \(\phi\) |
| \(\Phi_{\mathrm{res}}(\ell_{\min},\tau)\) | reservoir-admissible envelope class | envelope restriction | working definition | sub-threshold suppression + dominant-bar retention; introduced by WQ-LAT-1.C |

---

## 3. Claim Inventory

| ID | Claim |
|---|---|
| C-01 | \(K_{\mathrm{field}}\) is finite chart rank, not ontology. |
| C-02 | \(K_{\mathrm{act}}\) is chart-dependent. |
| C-03 | \(U\) is the aggregate projection from finite chart to Layer I. |
| C-04 | \(K_{\mathrm{bar}}\) is integer hard morphology count. |
| C-05 | \(K_{\mathrm{soft}}^\phi\) is a smooth / soft morphology count only after \(\phi\) is fixed. |
| C-06 | \(K_{\mathrm{bar}}\) was empirically chart-invariant in WQ-LAT-1. |
| C-07 | Default \(\phi\)-sat failed chart-invariance. |
| C-08 | Hard threshold, logistic \(s=100\), and shifted-sat \(\beta=20\) were empirically chart-invariant in WQ-LAT-1.B. |
| C-09 | Smooth bridge requires \(\phi\in\Phi_{\mathrm{res}}\). |
| C-10 | Under well-separated conditions, \(K_{\mathrm{bar}}\) should equal \(K_{\mathrm{act}}\). |
| C-11 | Under well-separated conditions and \(\phi\in\Phi_{\mathrm{res}}\), \(K_{\mathrm{soft}}^\phi\) should approximate \(K_{\mathrm{act}}\). |
| C-12 | Globally \(K_{\mathrm{soft}}^\phi\neq K_{\mathrm{act}}\); global equality must not be claimed. |
| C-13 | OP-0005 should be reformulated around reservoir-effective morphology count. |
| C-14 | OP-0008 should be reformulated around chart-level observable insufficiency for reservoir resegmentation. |
| C-15 | \(\sigma_{\mathrm{rich}}\) may be interpreted as a finite statistic for reservoir transitions. |

---

## 4. Proof-Status Table

| ID | Claim | Status | Evidence | Dependencies | Risk | Upgrade path |
|---|---|---|---|---|---|---|
| C-01 | \(K_{\mathrm{field}}\) is finite chart rank, not ontology | DEF / working interpretation | `K_status_commitment.md`; `latent_index_space_design.md`; `reservoir_reinterpretation_of_K.md` | Commitment 16; reservoir model | reservoir reading is not canonical | formalize latent index space and truncation map |
| C-02 | \(K_{\mathrm{act}}\) is chart-dependent | DEF + EMP | definition in `K_status_commitment.md`; LAT-C \(K_{\mathrm{act}}=3,4,6,8,12\) | fixed \(\varepsilon\), finite chart | threshold dependence | sensitivity analysis in \(\varepsilon\) and chart choice |
| C-03 | \(U\) is aggregate projection | DEF | `ksoft_kact_bridge_lemma.md`; `latent_index_space_design.md` | Layer II state \(\mathbf u\) | projection loses labels | none; definitional |
| C-04 | \(K_{\mathrm{bar}}\) is integer hard morphology count | DEF | `ksoft_kact_bridge_lemma.md` §5.1 / WQ-LAT-1.C | \(H_0\) superlevel barcode; \(\ell_{\min}\) | threshold sensitivity | prove stability regions for \(\ell_{\min}\) |
| C-05 | \(K_{\mathrm{soft}}^\phi\) is soft count only after \(\phi\) is fixed | DEF | `soft_K_definition.md`; WQ-LAT-1.B | barcode + envelope | bad \(\phi\) leaks chart rank | specify admissible \(\phi\)-class |
| C-06 | \(K_{\mathrm{bar}}\) was empirically chart-invariant in WQ-LAT-1 | EMP | zero integer disagreements across \(K\in\{3,4,6,8,12\}\) | \(T^2_{20}\), Option D-2, LAT-C/A-B geometries | local empirical result | repeat on graph/dynamics families |
| C-07 | default \(\phi\)-sat failed chart-invariance | EMP | range \(0.943\) on LAT-C__A; \(1.162\) on LAT-C__B | default envelope \(\ell/(\ell+\ell_{\min})\) | does not invalidate all soft counts | characterize sub-bar tail contribution |
| C-08 | hard, logistic \(s=100\), shifted-sat \(\beta=20\) passed WQ-LAT-1.B | EMP | ranges \(0.000\), \(\approx0.001\), \(\approx0.005\) | same tested WQ-LAT-1 configuration | local empirical support only | prove envelope-specific error bounds |
| C-09 | smooth bridge requires \(\phi\in\Phi_{\mathrm{res}}\) | LEMMA-CAND + EMP support | WQ-LAT-1.C patch; WQ-LAT-1.B failure/success split | \(\ell_{\min}\), transition width \(\tau\), sub-bar distribution | \(\Phi_{\mathrm{res}}\) is working class | formal envelope axioms and bounds |
| C-10 | well-separated \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) | LEMMA-CAND | bridge lemma §5.2 | one dominant aggregate bar per active slot; no extra dominant bars | condition (5) is currently load-bearing | prove (1)-(4) imply condition (5) with constants |
| C-11 | well-separated \(K_{\mathrm{soft}}^\phi\approx K_{\mathrm{act}}\) for \(\phi\in\Phi_{\mathrm{res}}\) | LEMMA-CAND | corrected §5.3 | C-09 + C-10 | constants not bounded | combine L-1/L-2 and propagate errors |
| C-12 | global equality is forbidden | FORBIDDEN to deny; global equality must not be claimed | F-B1/F-B2/F-B6/F-B7; R23 generic overlap evidence | none | false unification of label count and topology | keep as non-claim |
| C-13 | OP-0005 reservoir-effective morphology reformulation | CONJ / OPEN | reservoir memos; WQ-LAT evidence | accepted reservoir model; selection criterion | could be mistaken for solution | formulate as new OP-0005 subprogram only |
| C-14 | OP-0008 reservoir resegmentation reframe | CONJ / OPEN | reservoir memos; WQ-1.C-R2 notes; OP-0008 still open | \(\sigma\)-observable theory on reservoir transitions | may bypass original K-jump question | write explicit reframe with non-equivalence caveat |
| C-15 | \(\sigma_{\mathrm{rich}}\) as finite statistic for reservoir transitions | CONJ / UNSAFE if promoted | `reservoir_reinterpretation_of_K.md`; `sigma_rich_augmentation.md` context | centroid/orientation/Wigner data; NQ-242c | sufficiency not proven | first prove standard \(\sigma\) insufficiency and packet minimality |

---

## 5. Exact / Definitional Facts

The following are exact by definition once the ambient graph, thresholds, and envelope are fixed.

**Active slot count.**

$$
K_{\mathrm{act}}^\varepsilon(\mathbf u)
=
\#\{j:m_j(\mathbf u)>\varepsilon\}.
$$

**Aggregate projection.**

$$
U(\mathbf u)=\sum_j u^{(j)}.
$$

**Hard-bar count.**

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
\#\{i:\ell_i(U)\ge\ell_{\min}\}.
$$

**Soft count.**

$$
K_{\mathrm{soft}}^\phi(U)=\sum_i\phi(\ell_i(U)).
$$

**Hard threshold identity.** If

$$
\phi_{\mathrm{hard}}(\ell)=\mathbf 1_{\ell\ge\ell_{\min}},
$$

then

$$
K_{\mathrm{soft}}^{\phi_{\mathrm{hard}}}(U)
=
K_{\mathrm{bar}}^{\ell_{\min}}(U).
$$

This last equality is exact by definition. It is not an empirical claim.

---

## 6. Empirically Supported Claims

### WQ-LAT-1 evidence

The WQ-LAT-1 production run used:

$$
K_{\mathrm{field}}\in\{3,4,6,8,12\}
$$

on \(T^2_{20}\), Option D-2 dynamics, LAT-A/LAT-C options, A/B geometries, seed 42, and `max_iter=5000`.

Empirical findings:

| Quantity | WQ-LAT-1 finding | Status |
|---|---|---|
| \(K_{\mathrm{act}}^\varepsilon\) | under LAT-C, final active count tracked finite chart rank \(3,4,6,8,12\) | EMP, chart-dependence evidence |
| aggregate \(U_K\) | aggregate \(L^2\)/vertex max distance \(\le 1.5\times10^{-2}\) | EMP, local convergence |
| dominant bars | top-6 dominant-bar vector distance \(\le 0.027\) | EMP, local convergence |
| \(K_{\mathrm{bar}}^{\ell_{\min}}\) | zero integer disagreements across all tested \(K\) and \(\ell_{\min}\) | EMP, local chart-invariance |
| default \(K_{\mathrm{soft}}^\phi\) | range \(0.943\) on LAT-C__A, \(1.162\) on LAT-C__B | EMP, default smooth failure |

Interpretation: integer morphology was stable; default smooth envelope drifted because sub-resolution bars accumulated as the split-bump chart refined.

### WQ-LAT-1.B evidence

At \(\ell_{\min}=0.10\) on LAT-C__A:

| Envelope | Range | Mean | Reading |
|---|---:|---:|---|
| default \(\phi\)-sat | \(0.943\) | \(1.310\) | failed chart-invariance |
| hard threshold | \(0.000\) | \(1.000\) | exact integer count |
| logistic \(s=100\) | \(\approx0.001\) | \(\approx1.001\) | smooth hard-threshold approximation |
| shifted-sat \(\beta=20\) | \(\approx0.005\) | \(\approx0.938\) | smooth shifted suppressing envelope |

The bar statistics explain the drift: positive bars grew from 4 to 18 under LAT-C \(K=3\to12\), while the dominant bar stayed near \(0.24\). The default \(\phi\)-sat envelope assigned non-negligible mass to many short bars; sub-threshold suppressing envelopes removed the drift in the tested configuration.

These are empirical results on \(T^2_{20}\), Option D-2 dynamics, tested geometries, tested initialization schemes, and tested thresholds. They are not general theorems.

---

## 7. Lemma Candidates

### Lemma Candidate L-1 — Hard-bar / active-count bridge

If \(\mathbf u\in S_A^\varepsilon(G_t)\) is well-separated and the aggregate \(U(\mathbf u)\) has exactly \(|A|\) dominant \(H_0\) bars above \(\ell_{\min}\), then:

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u)
=
|A|.
$$

**Status:** LEMMA-CAND.

**What is already exact:** if condition "exactly \(|A|\) dominant bars" is assumed, and the active set is \(A\), the equality follows directly from definitions.

**Missing:** quantitative conditions guaranteeing one dominant aggregate \(H_0\) bar per active slot and no extra dominant bars.

### Lemma Candidate L-2 — Soft-count / hard-count bridge

If \(\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)\), then:

$$
K_{\mathrm{soft}}^\phi(U)
=
K_{\mathrm{bar}}^{\ell_{\min}}(U)
+
O(\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}+\rho_\phi).
$$

**Status:** LEMMA-CAND with empirical support.

**Missing:** explicit bound in terms of barcode decomposition and \(\phi\) sharpness. In particular:

$$
\rho_{\mathrm{sub}}=\sum_{\ell_i<\ell_{\min}}\phi(\ell_i)
$$

must be bounded by the sub-threshold barcode tail and the chosen envelope's decay below \(\ell_{\min}\).

### Lemma Candidate L-3 — Two-step bridge

Combining L-1 and L-2:

$$
K_{\mathrm{soft}}^\phi(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u)
+
O(\rho_{\mathrm{sep}}+\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}+\rho_\phi).
$$

**Status:** LEMMA-CAND.

**Missing:** complete quantitative proof, including constant propagation and regime boundaries where \(\rho_{\mathrm{sep}}\) or \(\rho_{\mathrm{edge}}\) blow up.

---

## 8. Conjectural or Open Claims

The following remain open or conjectural:

| Claim | Current status |
|---|---|
| A reservoir-effective rank \(K^*_{\mathrm{rank}}\) exists generally | OPEN |
| Persistence-prominence \(K^*_{\mathrm{pers}}\) solves or partially solves K-selection | CONJ / OP-0005 subprogram only |
| \(\Phi_{\mathrm{res}}\) works on arbitrary graphs and dynamics | OPEN |
| WQ-LAT-1 / WQ-LAT-1.B results generalize beyond \(T^2_{20}\) | OPEN |
| \(\sigma_{\mathrm{rich}}\) is sufficient for reservoir transitions | OPEN / unsafe to promote |
| OP-0008 is resolved by the reservoir reframe | OPEN |
| OP-0005 is resolved by \(K_{\mathrm{bar}}\) or \(K_{\mathrm{soft}}^{\Phi_{\mathrm{res}}}\) | OPEN |
| The well-separated hypotheses can be weakened without losing the bridge | OPEN |

---

## 9. Forbidden Overclaims

The following statements must not be made:

1. \(K_{\mathrm{soft}}^\phi=K_{\mathrm{act}}^\varepsilon\) globally.
2. Arbitrary monotone Lipschitz \(\phi\) is enough for reservoir-invariant smooth count.
3. WQ-LAT-1.B proves a theorem.
4. \(K_{\mathrm{bar}}\) is canonical.
5. Reservoir theory is canonical.
6. OP-0005 is solved.
7. OP-0008 is solved.
8. \(\sigma_{\mathrm{rich}}\) is sufficient.
9. \(K_{\mathrm{field}}\) is meaningless.
10. \(K_{\mathrm{act}}\) is useless.
11. \(K_{\mathrm{soft}}\) is always superior to \(K_{\mathrm{act}}\).
12. \(T^2_{20}\) evidence generalizes automatically.
13. The bridge lemma is theorem-grade in its current form.
14. The default \(\phi\)-sat envelope is reservoir-invariant under split-bump refinement.

---

## 10. Dependency Graph

Mathematical dependency:

$$
\Phi_{\mathrm{res}}
\Rightarrow
K_{\mathrm{soft}}^\phi \approx K_{\mathrm{bar}}
$$

$$
\text{well-separated regime}
\Rightarrow
K_{\mathrm{bar}} = K_{\mathrm{act}}
$$

Therefore:

$$
\Phi_{\mathrm{res}} + \text{well-separated}
\Rightarrow
K_{\mathrm{soft}}^\phi \approx K_{\mathrm{act}}.
$$

But globally:

$$
K_{\mathrm{soft}}^\phi \not\equiv K_{\mathrm{act}}.
$$

Layer dependency:

```text
K_field
  |
  v
finite chart rank / architectural cap
  |
  v
Layer II state u = (u^(1), ..., u^(K_field))
  |
  +--> K_act^epsilon
  |      chart-dependent active-coordinate diagnostic
  |
  v
aggregate projection U = sum_j u^(j)
  |
  v
H0 superlevel persistence
  |
  v
K_bar^l_min
  |
  v
admissible phi in Phi_res
  |
  v
K_soft^Phi_res
```

Failure dependency:

```text
non-admissible phi
  |
  v
sub-resolution bars receive positive mass
  |
  v
K_soft^phi drifts with chart rank

overlap / internal multimodality
  |
  v
aggregate H0 features no longer match active labels
  |
  v
K_bar != K_act
```

---

## 11. What Would Be Needed for Cat-A Upgrade

### For L-1

Required:

- formal well-separated hypotheses;
- support separation lower bound;
- overlap upper bound;
- proof that each active slot creates one and only one dominant aggregate \(H_0\) bar;
- proof that no extra dominant aggregate bars appear;
- quantitative threshold admissibility range for \(\ell_{\min}\);
- robustness under small perturbations of \(\mathbf u\).

### For L-2

Required:

- explicit barcode decomposition into dominant, edge, and subdominant parts;
- bound on sub-threshold contribution:

$$
\sum_{\ell_i<\ell_{\min}}\phi(\ell_i);
$$

- bound on edge bars near \(\ell_{\min}\);
- explicit \(\phi\)-sharpness condition;
- normalization bound for dominant bars:

$$
\sum_{\ell_i\ge\ell_{\min}+\tau}|\phi(\ell_i)-1|;
$$

- continuity / differentiability statement appropriate to the selected \(\phi\).

### For L-3

Required:

- combine L-1 and L-2;
- propagate constants;
- identify regimes where constants blow up;
- state failure modes as theorem exclusions, not afterthoughts;
- explicitly separate integer hard-count and smooth-envelope versions.

### For empirical generalization

Repeat WQ-LAT-1.B on:

- other graph sizes;
- non-torus graphs;
- different masses;
- different initializations;
- different dynamics;
- different \(\ell_{\min}\) ranges;
- multiple seeds;
- alternative reservoir refinements beyond LAT-C split-bump.

---

## 12. Recommended Next Actions

Recommended sequence:

1. Formalize L-1 hypotheses.
2. Formalize L-2 barcode error bound.
3. Run graph-generalization sweep only after L-1/L-2 assumptions are explicit.
4. Then update OP-0005 reformulation as a working subprogram, not a resolution.
5. Then proceed to WQ-LAT-2 spectral packet prototype or WQ-LAT-4 OP-0008 reframe.

Additional recommendations:

- Do not proceed to canonical promotion.
- Do not proceed to \(\sigma_{\mathrm{rich}}\) sufficiency claims.
- Treat \(K_{\mathrm{bar}}\) as the primary integer observable.
- Treat \(K_{\mathrm{soft}}^{\Phi_{\mathrm{res}}}\) as a smooth approximation to the integer observable, not as a globally superior count.
- Keep \(K_{\mathrm{act}}\) as the correct Layer II chart diagnostic.

---

## 13. Final Diagnosis

The bridge is **not theorem-grade yet**. The definitional layer is solid: \(K_{\mathrm{act}}\), \(U\), \(K_{\mathrm{bar}}\), and \(K_{\mathrm{soft}}^\phi\) are precise once thresholds and \(\phi\) are fixed.

The empirical support is meaningful but local. WQ-LAT-1 and WQ-LAT-1.B give strong evidence on \(T^2_{20}\), Option D-2 dynamics, and the tested refinement families that \(K_{\mathrm{bar}}\) is the robust integer morphology observable and that smooth \(K_{\mathrm{soft}}^\phi\) requires sub-threshold suppressing envelopes.

The corrected \(\phi\)-restriction fixes the main flaw in the old soft-count bridge: arbitrary monotone Lipschitz \(\phi\) is not enough. The correct smooth bridge must pass through \(\Phi_{\mathrm{res}}(\ell_{\min},\tau)\).

The most important remaining mathematical gap is:

$$
\text{active slot structure}
\Rightarrow
\text{dominant aggregate }H_0\text{ bars}.
$$

That implication is the next proof target. Until it is proved with explicit constants and exclusions, the \(K_{\mathrm{soft}}\) / \(K_{\mathrm{bar}}\) / \(K_{\mathrm{act}}\) bridge should remain a working lemma candidate, not a theorem.
