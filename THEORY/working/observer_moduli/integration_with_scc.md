---
type: working/theory
created: 2026-05-07
stage: OMS-0.7
project: Observer Moduli Space of SCC
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Integration with SCC Theory — OMS-0.7

Every statement classified: **DEFINED** | **PROVED** | **ASSUMED** | **HYPOTHESIZED** | **OPEN** | **REJECTED**.

---

## §1. Purpose

The OMS is a Level-2 extension of SCC — it uses SCC as its foundation without modifying it. This document maps the OMS structure onto the existing SCC theory layers and identifies dependencies, new open problems, and integration points.

**Principle.** OMS does NOT change any existing SCC theorem. It adds a new layer above the static SCC theory, using SCC objects (energy, optimizer, diagnostics) as input. Any apparent conflict between OMS and SCC must be resolved by refining OMS, not by modifying SCC.

---

## §2. Layer Map

| SCC Layer | Key object | OMS role | OMS dependency |
|---|---|---|---|
| **Static single-formation** | $u^* \in \Sigma_m$, $E_\Theta(u)$, $d_\Theta$ | Foundation: defines readout $P_{\min}$ and formation structure | Direct |
| **Phase transition (T8)** | $\beta/\alpha > 4\lambda_2/|W''(c)|$ | Supplies $q_c(X_t)$; used to define $\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}}$ | Direct |
| **Multi-formation (K-field)** | $K$ formations, $S_K$ labels | Provides label permutation gauge group $S_K$ | Direct |
| **Temporal identity (OT transport)** | $E_{\mathrm{tr}}$, persistence readout | Provides transport weight $\lambda_{\mathrm{tr}}$; face $F_{tr}$ = static observer | Direct |
| **Diagnostic vector** | $d = (\mathrm{Bind, Sep, In, Persist})$ | Provides $P_{\min}$; coarser component of $P_{\mathrm{top}}$ | Direct |
| **σ-Inheritance** | $\sigma$-maps, K-jump | May contribute to $\mathrm{Aut}_{task}$ in multi-formation scenarios | Indirect |
| **Stereo-SCC** | Depth-conditioned multi-formation | Extends the scene graph $X_t$; OMS applies directly | Indirect |

---

## §3. Question-by-Question Integration

### §3.1 Does OMS Require Temporal Theory?

**Short answer:** No for the minimal model; yes for the full model.

**Detail:**
- The minimal static OMS uses $F_{tr}$ (the $\lambda_{\mathrm{tr}} = 0$ face of $\Delta^3$).
- Prop CW2: on static scenes, $\lambda_{\mathrm{tr}}$ is irrelevant for $P_{\min}$.
- The full OMS includes $\lambda_{\mathrm{tr}}$ as a free observer parameter and uses the $\mathrm{Persist}$ component of $d_\Theta$ in $P_{\mathrm{top}}$.
- **If temporal identity theory (T-Temporal-Identity) is not yet canonical:** OMS can restrict to $F_{tr}$ for static-scene results. The temporal component of OMS is conditional on T-Temporal-Identity.

**Classification:** OMS-minimal is INDEPENDENT of temporal theory. OMS-full DEPENDS on temporal theory (T-Temporal-Identity Cat B, pending Cat A promotion → CV-1.12).

### §3.2 Does OMS Require Multi-Formation Theory?

**Short answer:** No for K=1 (Toy Model A); yes for K≥2 (Toy Model B and general).

**Detail:**
- K=1 model: $G = \{e\}$, no label symmetry needed. OMS moduli space is $\Delta^3$.
- K≥2 model: Requires the multi-formation K-field framework for formation labels and the $S_K$ gauge group.
- The multi-formation theory (T-K-Select-OBS, T-K-Select-PF, both Cat B in CV-1.11) must be canonicalized before OMS K≥2 analysis is canonical.

**Classification:** OMS K=1 is INDEPENDENT of multi-formation theory. OMS K≥2 DEPENDS on multi-formation theory (currently Cat B).

### §3.3 Does OMS Change the Phase Transition (T8)?

**Short answer:** No.

**Detail:**
- T8 states: $\beta/\alpha > 4\lambda_2/|W''(c)|$ is the formation condition.
- OMS uses T8 in one direction only: the criticality hypothesis sets $q = q_c(X_t)$, removing $q$ from the observer's free parameters.
- This is an ADDITIONAL ASSUMPTION in OMS (not a modification of T8). T8 remains unchanged.
- OMS is consistent with T8 in the following sense: any observer $\Theta \in \mathcal{M}_{\mathrm{obs}}$ with $q < q_c(X_t)$ will be in the sub-critical regime (no formation); the observer moduli space implicitly includes sub-critical observers (they form a region in $[q_{\min}, q_{\max}] \times \Delta^3 \times B_\xi$ below the phase transition).

**Observation:** The sub-critical region $\{q < q_c(X_t)\}$ of $\mathcal{M}_{\mathrm{obs}}$ is an open set where $P_{\mathrm{top}}(\Theta) = P_{\mathrm{top}}^{\mathrm{trivial}}$ (no formation, $K^* = 0$). All observers in this region are perceptually equivalent under $P_{\mathrm{top}}$. This is a large "trivial basin" in $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$.

**Classification:** T8 is UNCHANGED by OMS. DEFINED: the sub-critical basin as a distinguished region of $\mathfrak{M}$.

### §3.4 Does OMS Change the Diagnostic Vector?

**Short answer:** No. OMS uses the diagnostic vector as input.

**Detail:**
- OMS uses $d_\Theta = (\mathrm{Bind, Sep, Inside, Persist})$ as the $P_{\min}$ component.
- OMS adds topology ($T_\Theta$) to get $P_{\mathrm{top}}$, but does not modify the diagnostic vector definition.
- **Warning INT-1.** The OMS readout audit (readout_map_audit.md) argues that $P_{\min}$ alone is too coarse. This is a statement about the SUFFICIENCY of $P_{\min}$ for OMS purposes, not about the diagnostic vector itself. The diagnostic vector remains fully canonical.

### §3.5 Does OMS Expose New Open Problems for SCC?

**Yes.** The following new open problems arise from OMS that are relevant to main SCC:

| New OP | Connection to SCC |
|---|---|
| OP-OMS-009: $P_{\mathrm{top}}$ continuity | Requires SCC optimizer regularity (continuity of $u^*(\Theta)$) — a gap in existing proofs |
| OP-OMS-010: Admissible $V$ existence | Requires smooth energy landscape analysis — connects to Łojasiewicz theory (already in SCC) |
| OP-OMS-012: Boundary face degeneracy | Connects to SCC ablation experiments (exp1–exp57) — existing data can partially address this |
| OP-OMS-016: Effective DOF via Jacobian | Requires numerical sensitivity analysis of SCC diagnostics — new experiment type |

---

## §4. Structural Dependency Diagram

```
SCC Level 1: Static single-formation
    u_t : X_t → [0,1], E_Θ(u), optimizer
        ↓ supplies: u*(Θ,X), d_Θ, T_Θ
OMS Level 2: Observer parameter space
    M_obs = [q_min,q_max] × Δ³ × B_ξ
    G = S_K × Aut_task
    𝔐 = M_obs / G
        ↑ depends on: T8 (phase transition), K-field (label gauge)
        ↓ defines: perceptual types, basin stratification, effective DOF

SCC T8 (Phase Transition):
    β/α > 4λ₂/|W''(c)|
        → supplies: q_c(X_t) for M_obs^crit

SCC Multi-formation (K-field):
    K formations, u^(1),...,u^(K)
        → supplies: S_K gauge group
        
SCC Temporal Identity:
    E_tr, OT transport, Persist diagnostic
        → supplies: λ_tr component, F_tr face meaning
```

---

## §5. Integration Points with Existing SCC Documents

### §5.1 canonical.md (CV-1.11)

**OMS does not modify canonical.md.** OMS adds a new layer above it.

**Reading order:** After reading canonical.md §2 (Foundational Orientation) and §13 (Theorem Catalog), reading OMS documents becomes natural: OMS is the "observer-side" counterpart to the "scene-side" SCC theory.

**Future canonical addition:** When OMS is promoted, a new §14 (Observer Moduli Space) will be added to canonical.md.

### §5.2 theorem_status.md

**No existing theorem status changes.** OMS introduces its own OP-OMS registry which lives in `open_problems.md`.

**Future addition:** When OMS open problems are resolved, their proofs will be added to canonical.md and theorem_status.md.

### §5.3 hypothesis_tree.md (HT-3.0)

**OMS connects to multiple Q-nodes:**

| Q-question | OMS connection |
|---|---|
| Q1: 경계는 언제 출현하는가? | T8 supplies $q_c$; OMS uses T8 to define critical observer space |
| Q2: 여럿이 공존할 수 있는가? | K-field supplies $S_K$; OMS uses K≥2 for Sym² structure |
| Q3: 어떻게 변하는가? | OMS dynamics (gradient flow on $\mathfrak{M}$) is an observer-level analogue of Q3 |
| Q4: 몇으로 안정화되는가? | K-selection connects to OMS basin structure: stable $K$ corresponds to a perceptual type |
| Q5: 시간이 지나도 같은 것인가? | Temporal identity theory supplies $E_{\mathrm{tr}}$; $\lambda_{\mathrm{tr}}$ is the OMS temporal weight |
| Q6: 분열·합병 후에도 이어지는가? | σ-inheritance may contribute to $\mathrm{Aut}_{task}$ in split/merge scenarios |

**OMS does not belong to any single Q-block.** It is a Level-2 cross-cutting extension, indexed as "Q0" (the question behind all questions: *who is the observer?*).

---

## §6. New Open Problems Exposed by Integration

### OP-OMS-new-1: Sub-Critical Observer Basin

The sub-critical region $\{q < q_c(X_t)\}$ in $\mathcal{M}_{\mathrm{obs}}$ is a large "trivial basin" where all observers produce the same trivial readout (no formation). What is the structure of this region in the moduli space? Is it connected? Is its boundary (the critical manifold $\{q = q_c(X_t)\}$) a basin boundary? **OPEN — registered as part of OP-OMS-003 extension.**

### OP-OMS-new-2: Observer Universality Classes

Different scenes $X_t$ give different criticality conditions $q_c(X_t)$ and different $\mathrm{Aut}_{task}(X_t)$. Do different scenes produce the same OMS topology? Are there "universality classes" of scenes for which the moduli space structure is qualitatively the same? **OPEN — new problem, not yet registered.**

---

## §7. What OMS Does Not Claim

**Warning INT-2.** OMS does NOT claim:
- That observer parameters are fixed over time. (Temporal dynamics of $\Theta$ are Level-3 SCC.)
- That all observers have the same effective DOF. (Scene-dependent, see RG analysis.)
- That the moduli space is species-typical. (Population variation requires $V_{\mathrm{pop}}$, which is empirical.)
- That canonical promotion of OMS follows from canonical promotion of SCC theorems. (OMS has its own promotion checklist.)
- That the basin count is universal (fixed independently of $V$). (Basin count depends on $V \in \mathcal{V}_{\mathrm{adm}}$.)
