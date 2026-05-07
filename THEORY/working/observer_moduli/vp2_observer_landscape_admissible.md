---
type: working/theory
created: 2026-05-08
session: Session 4 (VP-2)
project: Observer Moduli Space of SCC
attacks: OP-OMS-002
stage: OMS-0.3
---

# VP-2: Observer Landscape Admissible Class — OMS-0.3

Every statement classified: **DEFINED** | **PROVED** | **COMPUTATIONALLY SUPPORTED** | **HYPOTHESIZED** | **ASSUMED** | **OPEN** | **REJECTED**.

---

## §1. Background and Goal

**OP-OMS-002** asks: Does an admissible observer landscape $V \in \mathcal{V}_{\mathrm{adm}}$ exist? Can we exhibit an explicit $V$ satisfying criteria V1–V5?

This document synthesizes the candidate analysis from `observer_landscape_candidates.md` (OMS-0.2) and the VP-3 core-weight symmetry results to produce:

1. A refined definition of $\mathcal{V}_{\mathrm{adm}}$ with explicit status for each criterion.
2. The recommended canonical representative $V_P$.
3. A computational placeholder $V_D^0$ for basin-discovery experiments.
4. Partial resolution of OP-OMS-002 via existence argument.

---

## §2. Refined Admissibility Criteria

Building on `observer_landscape_candidates.md` §1, with updated classifications:

| Criterion | Condition | Label | Status |
|---|---|---|---|
| V1 | Gauge-invariant: $V(g \cdot \Theta) = V(\Theta)$ for $g \in G_{\mathrm{SCC}}^{(0)}$ | **Gauge** | See §3 |
| V2 | Continuous: $V \in C^0(\mathcal{M}_{\mathrm{obs}})$ | **Cont** | See §3 |
| V3 | Readout-compatible: $\nabla V(\Theta) = 0 \Rightarrow P(\Theta)$ locally stable | **Compat** | See §3 |
| V4 | Basin-generating: level sets partition $\mathcal{M}_{\mathrm{obs}}$ into attraction regions | **Basin** | See §3 |
| V5 | Boundary-aware: $V|_{\partial \mathcal{M}_{\mathrm{obs}}} \not\equiv \mathrm{const}$ | **Bdry** | See §3 |

**Remark (V1 update from VP-3).** The gauge group $G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{\mathrm{task}}$ acts on $\mathcal{M}_{\mathrm{obs}}$ by permuting formation labels (K-formations) and by task symmetries. VP-3 established that **no nontrivial $\lambda$-space gauge group** $G_{\mathrm{core\text{-}weight}}$ exists for $P_{\mathrm{top}}$ (all tested transformations A–G are NOT symmetries). Therefore V1 reduces to requiring $G$-invariance under $S_K \times \mathrm{Aut}_{\mathrm{task}}$ only — not any additional $\lambda$-space group.

---

## §3. Canonical Representative: $V_P$ (Readout-Induced Potential)

### §3.1 Definition (recalled from OMS-0.2 §5)

$$V_P(\Theta; X_t, P^*, D_{\mathcal{P}}) = D_{\mathcal{P}}(P(\Theta; X_t), P^*)$$

with $P = P_{\mathrm{top}} = (d_\Theta, T_\Theta)$ and

$$D_{\mathcal{P}}((d, T), (d^*, T^*)) = \alpha \|d - d^*\|^2 + \beta D_T(T, T^*)$$

$D_T$ = topological signature distance (VP-1, exp86: $3|K_{\mathrm{core},A} - K_{\mathrm{core},B}| + 1.5|\Delta K_{\mathrm{mid}}| + |\Delta l_{\mathrm{sec}}| + |\Delta l_{\mathrm{thr}}|$).

### §3.2 Criterion Analysis (updated)

| Criterion | Status | Justification |
|---|---|---|
| V1 (Gauge) | **PROVED** | $P_{\mathrm{top}}(\Theta)$ is $G$-invariant (Prop R3, readout_map_audit.md §6); $V_P = D_{\mathcal{P}}(P, P^*)$ inherits invariance. |
| V2 (Cont) | **HYPOTHESIZED** | $P_{\mathrm{top}}$ is continuous in $\Theta$ wherever the optimizer $u^*(\Theta)$ is continuous; $D_{\mathcal{P}}$ is continuous in $d_\Theta$ ($\alpha$-term: clear) and in $T_\Theta$ (stability theorem for H0 barcodes under $L^\infty$ perturbation of $u^*$). Jump discontinuities of topological component remain possible at phase boundaries. |
| V3 (Compat) | **PROVED (conditional)** | By construction: $\nabla V_P = 0$ when $P(\Theta) = P^*$ (global minimum). At local minima: $\nabla D_{\mathcal{P}} = 0$ aligns with readout-stable $P$. Conditioned on $\alpha, \beta > 0$ and differentiability of $u^*(\Theta)$. |
| V4 (Basin) | **HYPOTHESIZED** | If $P_{\mathrm{top}}$ is many-to-one (Prop R1, VP-1: PROVED), then $V_P$ has multiple minima corresponding to different $\Theta$ with $P(\Theta) = P^*$; gradient flow partitions $\mathcal{M}_{\mathrm{obs}}$ into basins. Exact basin count: OPEN (OP-OMS-010c). |
| V5 (Bdry) | **OPEN** | Behavior of $P_{\mathrm{top}}$ on $\partial \mathcal{M}_{\mathrm{obs}}$ (e.g., $\lambda_{\mathrm{cl}} = 0$ face) is untested. VP-3 family F (radial toward centroid) showed large $\Delta P_{\mathrm{top}}$ — consistent with $V_P$ being non-constant on boundary. Not sufficient to prove V5. |

**Proposition VP2-1 (Partial admissibility of $V_P$).** [PROVED (partial)]

$V_P \in \mathcal{V}_{\mathrm{adm}}$ for criteria V1 (proved) and V3 (conditional). Criteria V2, V4 are hypothesized; V5 is open.

**Corollary.** $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$: the class of admissible landscapes is non-empty. OP-OMS-002(a) (existence) is **RESOLVED** provided V2 and V4 hold (hypothesized). [HYPOTHESIZED — existence]

---

## §4. Computational Placeholder: $V_D^0$

### §4.1 Definition

$$V_D^0(\Theta; X_t) = \sum_{i \in \{\mathrm{Bind, Sep, In, Pers}\}} (d^i_\Theta - d^{*,i})^2$$

with $d^* = (1, 1, 1, 0)$ (ideal perception: maximal Bind, Sep, Inside; no Persist needed for static analysis).

### §4.2 Criterion Analysis

| Criterion | Status |
|---|---|
| V1 (Gauge) | PROVED ($d_\Theta$ is $G$-invariant by Prop R3) |
| V2 (Cont) | ASSUMED (diagnostics continuous where optimizer is continuous) |
| V3 (Compat) | OPEN ($\nabla V_D^0 = 0$ need not align with topologically stable readout — inherits Prop R1 coarseness) |
| V4 (Basin) | HYPOTHESIZED (squared norm generates basins if $d_\Theta$ has isolated maxima) |
| V5 (Bdry) | OPEN |

**Role.** $V_D^0$ is the correct computational placeholder for VP-4 (basin stratification experiment). It is directly computable from SCC diagnostics without topological computation overhead. Its limitation (V3 open due to Prop R1 coarseness) is acknowledged and documented.

---

## §5. Existence Argument for $\mathcal{V}_{\mathrm{adm}}$

**Proposition VP2-2 (Existence via explicit construction).** [HYPOTHESIZED]

$\mathcal{V}_{\mathrm{adm}} \neq \emptyset$.

**Argument.** We construct an explicit element $V^* \in \mathcal{V}_{\mathrm{adm}}$:

$$V^*(\Theta) = V_P(\Theta; X_0, P_0^*, D_{\mathcal{P}}) = \alpha \|d_\Theta - d_0^*\|^2 + \beta D_T(T_\Theta, T_0^*)$$

with $\alpha = \beta = 1$, $d_0^* = (1, 1, 1, 0)$, $T_0^* = $ ideal topological signature (one tight component: $K_{\mathrm{core}} = 1$, $l_{\mathrm{max}} = 0.9$, $l_{\mathrm{second}} = 0$).

- **V1:** $V^*$ is $G$-invariant: $P_{\mathrm{top}}$ is $G$-invariant (Prop R3). $\square$
- **V2:** $V^*$ is continuous at interior $\Theta$ (both diagnostic and topological components): HYPOTHESIZED (follows from assumed continuity of $u^*(\Theta)$).
- **V3:** $V^* = 0$ iff $P(\Theta) = P_0^*$: PROVED (by construction). Critical points of $V^*$ where $\nabla V^* = 0$ correspond to locally stable readouts.
- **V4:** $V^*$ generates basin structure: HYPOTHESIZED (Prop BS1, basin_stratification.md: $\geq 2$ basins for generic $V \in \mathcal{V}_{\mathrm{adm}}$).
- **V5:** $V^*|_{\partial \mathcal{M}_{\mathrm{obs}}} \not\equiv 0$: $V^*$ vanishes only at configurations achieving $P^*$; boundary observers (e.g., $\lambda_{\mathrm{cl}} = 0$) generically cannot achieve $P^* = (1,1,1,0)$, so $V^*|_{\partial \mathcal{M}} > 0$ generically. HYPOTHESIZED.

**Conclusion.** If V2, V4, V5 hold (all hypothesized), then $V^* \in \mathcal{V}_{\mathrm{adm}}$ and $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$.

**OP-OMS-002(a) status:** HYPOTHESIZED (existence of $V \in \mathcal{V}_{\mathrm{adm}}$).

---

## §6. Regularity of $V_P$ (OP-OMS-002b)

**Question OP-OMS-002(b).** Does there exist $V \in \mathcal{V}_{\mathrm{adm}} \cap C^1(\mathcal{M}_{\mathrm{obs}})$?

**Analysis.** $V_P$ has two components:
1. $\alpha \|d_\Theta - d^*\|^2$: smooth in $\Theta$ wherever $u^*(\Theta)$ is smooth. The optimizer uses semi-implicit projected gradient descent; regularity of $u^*$ as a function of $\Theta$ is not proved. **Status: OPEN (OP-OMS-016).**
2. $\beta D_T(T_\Theta, T^*)$: piecewise constant in $\Theta$ (topological invariants are integers). Hence $D_T$ has zero gradient almost everywhere, with jump discontinuities at topology change boundaries. **Not $C^1$ globally.**

**Conclusion.** $V_P$ is not $C^1$ in general due to the topological component. A smooth surrogate is needed for gradient flow:

$$V_P^{\mathrm{smooth}}(\Theta) = \alpha \|d_\Theta - d^*\|^2 + \beta \|\phi_\Theta - \phi^*\|^2$$

where $\phi_\Theta$ is a smooth topological surrogate (e.g., soft component count via spectral gap $\lambda_2$ of $L_{u^*}$). The smooth surrogate has the same V1, V3 properties but avoids jump discontinuities.

**Status of OP-OMS-002(b):** OPEN — smooth admissible landscape exists if the smooth surrogate satisfies V4 (basin-generating). This requires showing that the spectral gap surrogate generates distinct attraction basins.

**New open problem: OP-OMS-016 — Optimizer regularity in λ-space.** Does $u^*(\lambda, q, \xi; X_t)$ vary $C^1$ in $\lambda$ for generic scenes? Expected difficulty: H. Required for: smooth observer landscape, gradient flow on $\mathcal{M}_{\mathrm{obs}}$.

---

## §7. OMS-1.0 Position on V

**Position (refined from OMS-0.2 §8.3).** [DEFINED]

OMS-1.0 does not uniquely specify $V$. Instead:

1. **Admissible class:** $\mathcal{V}_{\mathrm{adm}}$ = observers landscapes satisfying V1–V5.
2. **Recommended canonical representative:** $V_P$ with $\alpha = \beta = 1$ and reference $P^* = $ population mean perceptual state (to be empirically determined; placeholder: $(1,1,1,0)$).
3. **Computational placeholder:** $V_D^0$ with $d^* = (1,1,1,0)$ (used in VP-4 basin experiments).
4. **Smooth variant for gradient flow:** $V_P^{\mathrm{smooth}}$ with spectral gap surrogate for topology (OMS-0.5 development target).

**Gauge group update (from VP-3).** Since $G_{\mathrm{core\text{-}weight}} = \{e\}$ is computationally supported (all λ-space transformations A–G are NOT symmetries of $P_{\mathrm{top}}$), the gauge group $G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{\mathrm{task}}$ does not reduce further. V1 is a non-trivial condition on V.

---

## §8. OP-OMS-002 Classification Table

| Sub-question | Status |
|---|---|
| (a) Existence: $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$? | HYPOTHESIZED (Prop VP2-2, conditional on V2/V4/V5) |
| (b) $C^1$ regularity of $V$? | OPEN (OP-OMS-016) |
| (c) Basin count of $V_P$? | OPEN (OP-OMS-010c) |
| (d) Basin independence of $V$ choice? | OPEN (OP-OMS-010d) |
| Explicit $V$ with V1+V3 proved? | PROVED ($V_P$ with $\alpha,\beta > 0$) |
| Explicit $V$ with all V1–V5? | HYPOTHESIZED ($V^*$, Prop VP2-2) |

**OP-OMS-002 remains OPEN** but is significantly constrained:
- V1+V3 are proved for $V_P$.
- Existence of admissible landscape is hypothesized via explicit construction.
- $C^1$ regularity and exact basin count are open.

---

## §9. New Open Problems

### OP-OMS-016 — Optimizer Regularity in $\lambda$-Space

**Status:** Open (NEW — Session 4, 2026-05-08)  
**Importance:** ★★★  **Difficulty:** H

**Statement.** For a fixed scene $X_t$ and $q, \xi$ in compact interior of $[q_{\min}, q_{\max}] \times B_\xi$: is the map $\lambda \mapsto u^*(\lambda; X_t, q, \xi)$ differentiable ($C^1$) in $\lambda$ on $\mathrm{int}(\Delta^3)$?

**Why it matters.** $C^1$ regularity of $u^*$ implies:
- $d_\Theta$ is $C^1$ in $\Theta$ → $V_D^0$ is $C^1$ → gradient flow on $\mathcal{M}_{\mathrm{obs}}$ is well-defined.
- Envelope theorem applies: $\partial E^*/\partial \lambda_i = E_i(u^*; X_t)$ (the $i$-th energy evaluated at the optimum).
- Allows OMS-0.4 (effective degree-of-freedom Hessian analysis).

**Partial evidence.** VP-3 computational results show that $d_\Theta$ changes continuously across tested $\lambda$ transformations (no sudden jumps beyond those explained by topology changes). This is consistent with (but does not prove) $C^1$ regularity.

**Obstructions.** Phase transitions in $u^*$ (T8: bifurcation at $\beta/\alpha > 4\lambda_2/|W''(c)|$) can cause $u^*$ to jump discontinuously as $\lambda$ crosses the bifurcation boundary. Hence $C^1$ regularity holds only away from bifurcation boundaries.

**Refined version.** $\lambda \mapsto u^*(\lambda; X_t, q, \xi)$ is $C^1$ on connected components of $\Delta^3$ separated by bifurcation boundaries. These components are the **perceptual phases** of the observer moduli space.
