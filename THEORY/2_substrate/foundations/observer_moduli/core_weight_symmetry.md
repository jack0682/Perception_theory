---
type: working/theory
created: 2026-05-07
stage: OMS-0.3
project: Observer Moduli Space of SCC
attacks: OP-OMS-001
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Core-Weight Symmetry Discovery — OMS-0.3

Every statement classified: **DEFINED** | **PROVED** | **ASSUMED** | **HYPOTHESIZED** | **COMPUTATIONALLY TESTABLE** | **OPEN** | **REJECTED**.

---

## §1. Problem Statement

**OP-OMS-001.** Is $G_{\mathrm{core\text{-}weight}} = \{e\}$ the correct default, or does a non-trivial compact group act on $\lambda \in \Delta^3$ while preserving the perceptual core?

The question is: does there exist a non-trivial map $g : \Delta^3 \to \Delta^3$ such that

$$P(g(\lambda), q, \xi; X_t) = P(\lambda, q, \xi; X_t) \quad \text{for all } (q, \xi, X_t)?$$

If yes: $g$ generates a gauge symmetry on the energy weight space, and the true moduli space is smaller than $\mathcal{M}_{\mathrm{obs}} / G_{\mathrm{SCC}}^{(0)}$.

If no: $G_{\mathrm{core\text{-}weight}} = \{e\}$ is correct, and the conservative default stands.

---

## §2. Why Permutation of $\lambda$ Components Is NOT a Gauge Symmetry

### §2.1 The $S_4$-Action on $\Delta^3$

The full permutation group $S_4$ acts on $\Delta^3$ by permuting coordinates:
$$\sigma \cdot (\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}}) = (\lambda_{\sigma^{-1}(cl)}, \lambda_{\sigma^{-1}(sep)}, \lambda_{\sigma^{-1}(bd)}, \lambda_{\sigma^{-1}(tr)})$$

**Proposition CW1 (S4 is NOT a weight gauge symmetry).** [PROVED]

$S_4$ is not a perceptual gauge symmetry. In particular, $(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}})$ and $(\lambda_{\mathrm{sep}}, \lambda_{\mathrm{cl}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}})$ (closure-separation swap) generically give different readouts.

**Proof.** The four energy terms have distinct functional forms:

| Energy | Functional form | Source |
|---|---|---|
| $E_{\mathrm{cl}}$ | Closure operator (aggregation-based) | Self-support, shape integrity |
| $E_{\mathrm{sep}}$ | Separation (distinction-weighted average) | Contrast with background |
| $E_{\mathrm{bd}}$ | $2\alpha u^\top L u$ (smoothed boundary) | Laplacian quadratic form |
| $E_{\mathrm{tr}}$ | OT transport between time steps | Temporal coherence |

These are **not interchangeable** in the energy functional. Swapping $\lambda_{\mathrm{cl}} \leftrightarrow \lambda_{\mathrm{sep}}$ changes the energy functional from:
$$E = \lambda_{\mathrm{cl}} E_{\mathrm{cl}} + \lambda_{\mathrm{sep}} E_{\mathrm{sep}} + \ldots$$
to:
$$E' = \lambda_{\mathrm{sep}} E_{\mathrm{cl}} + \lambda_{\mathrm{cl}} E_{\mathrm{sep}} + \ldots$$

Since $E_{\mathrm{cl}} \neq E_{\mathrm{sep}}$ as functionals, $E \neq E'$ in general. Therefore the minimizer $u^*$ changes, and the readout $P$ changes. $\square$

**Audit Warning CW1.** $S_4$ symmetry of $\lambda$ weights is **REJECTED** as a gauge symmetry. Do not assume permutation symmetry of energy weights without explicit justification.

---

## §3. Candidate Transformations to Test

### §3.1 Formal Definition of Discovered Symmetry

**Definition CW1 (Discovered core-weight symmetry group).** [DEFINED]

$$G_{\mathrm{cw}}(P) = \left\{ g \in \mathrm{Diff}(\Delta^3) \;\middle\vert \; P(g(\lambda), q, \xi; X_t) = P(\lambda, q, \xi; X_t) \quad \forall (q, \xi, X_t) \right\}$$

This is the **global** core-weight symmetry group for readout $P$.

**Local version** (on open set $U \subset \mathcal{M}_{\mathrm{obs}}$):
$$G_{\mathrm{cw}}(P, U) = \left\{ g \in \mathrm{Diff}(\Delta^3) \;\middle\vert \; P(g(\lambda), q, \xi; X_t) = P(\lambda, q, \xi; X_t) \quad \forall (\lambda, q, \xi, X_t) \in U \right\}$$

**Default.** $G_{\mathrm{cw}}(P) = \{e\}$ until a non-trivial element is found. [ASSUMED]

### §3.2 Candidate Transformation 1: Closure-Separation Swap ($\mathbb{Z}_2$)

**Transformation:** $g_1(\lambda) = (\lambda_{\mathrm{sep}}, \lambda_{\mathrm{cl}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}})$

**Question:** Is $g_1 \in G_{\mathrm{cw}}(P_{\mathrm{top}})$?

**Analysis.**
- $E_{\mathrm{cl}}$ uses the closure operator $\mathrm{Cl}_t$ (defined via spectral aggregation on the graph).
- $E_{\mathrm{sep}}$ uses the distinction measure (u-weighted average of distinction values $D_i$).
- These are structurally different: $E_{\mathrm{cl}}$ favors configurations where $u$ has high interior mass under the closure map; $E_{\mathrm{sep}}$ favors configurations where $u$-weighted distinction is large.

**Predicted result (COMPUTATIONALLY TESTABLE):** $g_1 \notin G_{\mathrm{cw}}(P_{\mathrm{top}})$ for generic scenes. Specifically: swapping $\lambda_{\mathrm{cl}} \leftrightarrow \lambda_{\mathrm{sep}}$ should produce a different number of formation components $K^*$ in scenes where closure and separation pull in different directions (e.g., convex vs. concave objects).

**Test protocol:** See §5.

### §3.3 Candidate Transformation 2: Boundary-Closure Compensation

**Transformation:** $g_2(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}}) = (\lambda_{\mathrm{cl}} + \delta, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}} - \delta, \lambda_{\mathrm{tr}})$ for small $\delta > 0$.

**Hypothesis:** For small $\delta$, the readout $P_{\mathrm{top}}$ may be approximately preserved because $E_{\mathrm{cl}}$ and $E_{\mathrm{bd}}$ are both "shape integrity" energies that cooperate.

**Classification:** HYPOTHESIZED for small $\delta$. This would give an **approximate local symmetry** near the curve $\{\lambda_{\mathrm{cl}} + \lambda_{\mathrm{bd}} = c\}$ in $\Delta^3$.

**Implication if true:** There exists a 1-parameter family of observer configurations with equivalent readouts. This would define a 1-dimensional manifold in $\Delta^3$ that is "irrelevant" in the sense of RG (see rg_relevance_flow.md).

**Status:** COMPUTATIONALLY TESTABLE. Not assumed.

### §3.4 Candidate Transformation 3: Transport-Independence Subspace

**Observation.** When considering static scenes ($\mathrm{Persist} = 0$ by default since $E_{\mathrm{tr}}$ requires two time steps), the transport weight $\lambda_{\mathrm{tr}}$ does not affect the formation energy. Therefore:

**Proposition CW2 (Static transport invariance).** [PROVED (conditional)]

For static single-frame scenes ($X_t = X_{t+1}$, i.e., no motion):
$$P_{\min}(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}}; X) = P_{\min}(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}}'; X)$$
for any $\lambda_{\mathrm{tr}}, \lambda_{\mathrm{tr}}' \geq 0$ with $\lambda_{\mathrm{cl}} + \lambda_{\mathrm{sep}} + \lambda_{\mathrm{bd}} + \lambda_{\mathrm{tr}} = \lambda_{\mathrm{cl}} + \lambda_{\mathrm{sep}} + \lambda_{\mathrm{bd}} + \lambda_{\mathrm{tr}}' = 1$.

**Proof.** For a static scene, $E_{\mathrm{tr}}(u; X_t, X_{t+1}) = 0$ when $X_t = X_{t+1}$ (no transport cost for identity motion). Hence $\lambda_{\mathrm{tr}}$ only rescales a zero term. $\square$

**Consequence.** On static scenes, the map $g_3 : \lambda_{\mathrm{tr}} \mapsto \lambda_{\mathrm{tr}}'$ (with proportional rescaling of other weights) gives a readout-invariant 1-parameter family. This generates a **genuine gauge direction** on the restriction of $\mathcal{M}_{\mathrm{obs}}$ to static scenes.

**Important caveat.** This is scene-class-specific, not universal. For dynamic scenes, $\lambda_{\mathrm{tr}}$ affects the temporal energy and readout changes. Therefore this is a **conditional symmetry** (conditioned on scene class = static), not a global $G_{\mathrm{cw}}$ element.

### §3.5 Candidate Transformation 4: Energy Scaling (Rejected Globally)

**Transformation:** $g_4(\lambda) = \lambda$ (identity), but rescale $E_\Theta \mapsto c \cdot E_\Theta$ for $c > 0$.

**Rejection.** Rescaling the total energy does not change the minimizer (argmin is invariant under positive scalar multiplication). However, this is not a transformation of $\lambda \in \Delta^3$ — it is a transformation of $E$ itself. Since $\lambda \in \Delta^3$ (normalization $\sum \lambda_i = 1$), scalar rescaling of all weights simultaneously is not possible while remaining in $\Delta^3$. **REJECTED** as not a valid $\Delta^3$-action.

---

## §4. Regime-Specific Approximate Symmetries

### §4.1 High-Contrast Scene Regime

In a high-contrast scene (large $E_{\mathrm{sep}}$ dominates), the closure energy becomes less relevant. Heuristically:

$$P(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}}) \approx P(0, \lambda_{\mathrm{sep}} + \lambda_{\mathrm{cl}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}}) \quad \text{(high contrast)}$$

This would mean that closure weight "flows into" separation weight in the high-contrast limit — an **approximate local symmetry** of $P_{\mathrm{top}}$ in a specific scene regime.

**Classification:** HYPOTHESIZED (regime-specific). Needs explicit numerical verification.

### §4.2 Conservative Conclusion

**Proposition CW3 (Conservative default maintained).** [ASSUMED]

Until an explicit non-trivial $g \in G_{\mathrm{cw}}(P_{\mathrm{top}})$ is computationally identified and verified, the default $G_{\mathrm{core\text{-}weight}} = \{e\}$ is maintained. No continuous gauge group on $\Delta^3$ is assumed.

**Justification:**
1. Permutation symmetry $S_4$ is rejected (Prop CW1).
2. Boundary-closure compensation is hypothesized (local, approximate only).
3. Transport invariance is conditional on scene class.
4. No global gauge direction on $\Delta^3$ has been found.

---

## §5. Computational Test Protocol

### Protocol CW-1: Closure-Separation Swap Test

**Procedure:**
1. Fix scene $X_t$ (e.g., two-object graph with clear separation).
2. Fix $q = q_c(X_t)$, $\xi = \xi_0$ (canonical values).
3. Sample $\lambda^{(1)} = (\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, 0)$ with $\lambda_{\mathrm{cl}} \neq \lambda_{\mathrm{sep}}$.
4. Compute $u^*(\lambda^{(1)}, X_t)$ and $P_{\mathrm{top}}(\lambda^{(1)})$.
5. Compute $\lambda^{(2)} = (\lambda_{\mathrm{sep}}, \lambda_{\mathrm{cl}}, \lambda_{\mathrm{bd}}, 0)$ (swapped).
6. Compute $u^*(\lambda^{(2)}, X_t)$ and $P_{\mathrm{top}}(\lambda^{(2)})$.
7. Measure $\lVert P_{\mathrm{top}}(\lambda^{(1)}) - P_{\mathrm{top}}(\lambda^{(2)}) \rVert$.

**Expected result:** Non-zero difference for $\lambda_{\mathrm{cl}} \neq \lambda_{\mathrm{sep}}$, confirming $g_1 \notin G_{\mathrm{cw}}$.

**If result is zero (or near-zero):** $g_1$ is a candidate gauge symmetry; upgrade status to HYPOTHESIZED for global symmetry.

### Protocol CW-2: Boundary-Closure Compensation Curve

**Procedure:**
1. Fix $\lambda_{\mathrm{sep}}, \lambda_{\mathrm{tr}}, q, \xi$.
2. Vary $\lambda_{\mathrm{cl}} \in [0, 1 - \lambda_{\mathrm{sep}} - \lambda_{\mathrm{tr}}]$, with $\lambda_{\mathrm{bd}} = 1 - \lambda_{\mathrm{cl}} - \lambda_{\mathrm{sep}} - \lambda_{\mathrm{tr}}$.
3. Plot $P_{\mathrm{top}}(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}})$ vs. $\lambda_{\mathrm{cl}}$.
4. Identify flat regions (where $P_{\mathrm{top}}$ is approximately constant).

**Expected result:** Monotone or non-flat profile, confirming no compensation symmetry. If a flat region is found, it defines a local gauge direction.

### Protocol CW-3: Transport Weight Ablation (Static Scene)

**Procedure:**
1. Fix a static scene ($X_t = X_{t+1}$).
2. Vary $\lambda_{\mathrm{tr}} \in [0, 1 - \lambda_{\mathrm{cl}} - \lambda_{\mathrm{sep}} - \lambda_{\mathrm{bd}}]$ with other weights proportionally rescaled.
3. Verify $P_{\mathrm{min}}$ is constant in $\lambda_{\mathrm{tr}}$ (conditional symmetry).

**Expected result:** Flat $P_{\mathrm{min}}$ (confirming Prop CW2). Check whether $P_{\mathrm{top}}$ is also flat (topological persistence may still change).

---

## §6. VP-3 Results (exp87, 2026-05-08)

VP-3 executed Protocols CW-1, CW-2, CW-3 and four additional transformation families on
scenes S3 (6×6 grid) and S4 (two 5-cliques) with volume fraction 0.3.

### VP-3 Complete Results

| Transform | Description | frac_asym | n | Verdict |
|---|---|---|---|---|
| A (CW-1) | Closure-sep swap | **0.833** | 12 | **NOT_A_SYMMETRY** |
| B | Closure-bd swap | 0.500 | 12 | PARTIAL_SYMMETRY |
| C (CW-2) | Boundary-cl compensation | 0.368 | 38 | PARTIAL_SYMMETRY |
| D | Boundary-sep compensation | 0.421 | 38 | PARTIAL_SYMMETRY |
| E (CW-3) | Transport ablation (static) | **0.000** | 18 | **CANDIDATE_SYMMETRY** |
| F | Radial toward centroid | 0.300 | 60 | PARTIAL_SYMMETRY |
| G | Random tangent eps=0.08 | 0.217 | 60 | PARTIAL_SYMMETRY |

**Prop CW2 status: PROVED (conditional) → COMPUTATIONALLY CONFIRMED (VP-3 E, n=18 pairs, all delta_P=0).**

**Prop CW3 status: ASSUMED → COMPUTATIONALLY SUPPORTED (no global gauge direction found).**

**New: Observation VP3-3 (approximate symmetry loci).** [COMPUTATIONALLY SUPPORTED]
- Near $\{\lambda_{\mathrm{cl}} = \lambda_{\mathrm{sep}}\}$: Transform A is locally approximate (VP-3 A near-sym case, $\Delta P_{\mathrm{top}} = 0.0295$).
- Near $F_{\mathrm{bd}}$ face ($\lambda_{\mathrm{bd}} \approx 0.85$): Transforms C and D are locally approximate.
- Registered as **OP-OMS-017** (approximate symmetry loci in $\lambda$-space).

---

## §7. Summary and OP-OMS-001 Status (Post-VP-3)

### Status Update for OP-OMS-001

| Sub-question | Status |
|---|---|
| Is $S_4$ a weight gauge symmetry? | REJECTED (Prop CW1) |
| Is the closure-separation swap a global symmetry? | **NOT_A_SYMMETRY** (VP-3 A, frac_asym=0.833) |
| Is the closure-bd swap a global symmetry? | PARTIAL_SYMMETRY (VP-3 B, scene-dependent) |
| Is there a boundary-closure approximate symmetry? | PARTIAL (VP-3 C — near $F_{\mathrm{bd}}$ only) |
| Is there a boundary-sep approximate symmetry? | PARTIAL (VP-3 D — same) |
| Is transport invariance a global symmetry? | **COMPUTATIONALLY CONFIRMED** conditional (Prop CW2, VP-3 E) |
| Radial toward centroid a symmetry? | PARTIAL_SYMMETRY (VP-3 F) |
| Random tangent a symmetry? | PARTIAL_SYMMETRY (VP-3 G) |
| Default $G_{\mathrm{core\text{-}weight}} = \{e\}$? | **COMPUTATIONALLY SUPPORTED** (VP-3 A–G) |

**OP-OMS-001 remains OPEN** for formal proof, but:
- All major candidate global symmetries have been ruled out computationally.
- The only genuine gauge direction found is $\lambda_{\mathrm{tr}}$ on static-scene restriction (Prop CW2 confirmed).
- PARTIAL_SYMMETRY verdicts for B, C, D, F, G reflect approximate local symmetry loci (OP-OMS-017), not global gauge symmetries.
- The default $G_{\mathrm{cw}} = \{e\}$ for dynamic scenes is now COMPUTATIONALLY SUPPORTED.
