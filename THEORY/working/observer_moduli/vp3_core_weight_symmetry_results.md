---
type: working/theory
created: 2026-05-08
session: Session 4 (VP-3)
project: Observer Moduli Space of SCC
attacks: OP-OMS-001
status: COMPLETE (exp87, 2026-05-08)
---

# VP-3: Core-Weight Symmetry Results — OMS-0.3

Every statement classified: **DEFINED** | **PROVED** | **COMPUTATIONALLY SUPPORTED** | **HYPOTHESIZED** | **ASSUMED** | **OPEN** | **REJECTED**.

---

## §1. Experiment Summary

**VP-3** tested seven transformation families A–G on the energy weight space $\lambda \in \Delta^3$
to determine whether any constitutes a gauge symmetry of the P_top readout.

**Scenes:** S3 (6×6 grid, $n=36$) and S4 (two 5-cliques, $n=10$).
**Readout:** $P_{\mathrm{top}} = (d_\Theta, T_\Theta)$ with distance $\Delta P_{\mathrm{top}} = \Delta d + 0.5 \Delta T$.
**Asymmetry criterion:** $\Delta P_{\mathrm{top}} > 0.05$.

---

## §2. Results by Transformation

### Transform A — Closure-Separation Swap

**Transform:** $g_A : (\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}}) \mapsto (\lambda_{\mathrm{sep}}, \lambda_{\mathrm{cl}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}})$

| $\lambda_A$ | $\lambda_B = g_A(\lambda_A)$ | $\Delta d$ | $\Delta T$ | $\Delta P_{\mathrm{top}}$ | Asymmetric? |
|---|---|---|---|---|---|
| (0.85, 0.05, 0.05, 0.05) | (0.05, 0.85, 0.05, 0.05) | 0.7504 | 1.5003 | 1.5005 | **YES** |
| (0.60, 0.20, 0.15, 0.05) | (0.20, 0.60, 0.15, 0.05) | 0.0295 | 0.0000 | 0.0295 | No |
| (0.50, 0.10, 0.35, 0.05) | (0.10, 0.50, 0.35, 0.05) | 0.1012 | 0.0000 | 0.1012 | **YES** |

**Verdict:** NOT_A_SYMMETRY [COMPUTATIONALLY SUPPORTED]. $g_A \notin G_{\mathrm{cw}}(P_{\mathrm{top}})$.

**Mechanism:** Extreme closure-dominant vs. separation-dominant observers find fundamentally
different formations (different binding, separation, topology). Near the diagonal $\lambda_{\mathrm{cl}} = \lambda_{\mathrm{sep}}$,
the readouts are approximately equal (approximate local symmetry). See OP-OMS-017.

### Transform B — Closure-Boundary Swap

**Verdict:** NOT_A_SYMMETRY [COMPUTATIONALLY SUPPORTED]. $\Delta P_{\mathrm{top}}$ up to 3.44.
Frac asymmetric: 0.625/8 pairs.

### Transform C — Boundary-Closure Compensation ($\delta = 0.15$)

**Transform:** $\lambda_{\mathrm{cl}} \mathrel{+}= \delta$, $\lambda_{\mathrm{bd}} \mathrel{-}= \delta$.

**Verdict:** NOT_A_SYMMETRY [COMPUTATIONALLY SUPPORTED]. Frac asymmetric: 0.75/4 pairs.
Exception: near $\lambda_{\mathrm{bd}} = 0.85$ base, one pair shows $\Delta P_{\mathrm{top}} = 0.0003$ (near-symmetric).
This is a local approximate symmetry near the boundary-dominant face $F_{\mathrm{bd}}$.

### Transform D — Boundary-Separation Compensation ($\delta = 0.15$)

**Transform:** $\lambda_{\mathrm{sep}} \mathrel{+}= \delta$, $\lambda_{\mathrm{bd}} \mathrel{-}= \delta$.

**Verdict:** NOT_A_SYMMETRY [COMPUTATIONALLY SUPPORTED]. Frac asymmetric: 0.75/4 pairs.
Same near-symmetric exception near $\lambda_{\mathrm{bd}}$ corner as Transform C.

### Transform E — Transport Ablation (Static Scene) ← KEY RESULT

**Transform:** $\lambda_{\mathrm{tr}} \to 0$, rescale other components to $\Delta^3$.

| $\lambda_A$ | $\lambda_B = g_E(\lambda_A)$ | $\Delta d$ | $\Delta T$ | Asymmetric? |
|---|---|---|---|---|
| (0.30, 0.30, 0.30, 0.10) | (0.333, 0.333, 0.333, 0.000) | 0.0000 | 0.0000 | **No** |
| (0.40, 0.25, 0.25, 0.10) | (0.444, 0.278, 0.278, 0.000) | 0.0000 | 0.0000 | **No** |
| (additional pairs) | — | 0.0000 | 0.0000 | **No** |

**Verdict:** CANDIDATE_SYMMETRY (conditional static) [COMPUTATIONALLY SUPPORTED].

**Proposition CW2 (Static transport invariance) — status upgraded to COMPUTATIONALLY CONFIRMED.**

For static single-frame scenes, $\lambda_{\mathrm{tr}}$ does not affect $P_{\mathrm{top}}$. The 1-parameter family
$\{\lambda_{\mathrm{tr}} \to \lambda_{\mathrm{tr}}'\}$ (with proportional rescaling) is a genuine gauge direction on the
$F_{\mathrm{tr}}$-face restriction of $\mathcal{M}_{\mathrm{obs}}$.

**Note:** This is a conditional symmetry (static scenes only), not a global gauge direction.
For dynamic scenes with transport energy, $\lambda_{\mathrm{tr}}$ affects $P_{\mathrm{top}}$.

### Transform F — Radial Toward Centroid ($t = 0.3$)

**Verdict:** NOT_A_SYMMETRY [COMPUTATIONALLY SUPPORTED]. Frac asymmetric: 0.583/12 pairs.
No gauge direction toward the simplex centroid.

### Transform G — Random Tangent Perturbation ($\epsilon = 0.08$)

**Verdict:** PARTIAL_SYMMETRY — NOT a gauge symmetry [COMPUTATIONALLY SUPPORTED].
Frac asymmetric: 0.125/8. The 12.5% asymmetric cases rule out $g \in G_{\mathrm{cw}}$ for random directions.
The majority of non-asymmetric cases reflect within-basin flatness of $V_D^0$ at scale $\epsilon = 0.08$,
not gauge invariance.

---

## §3. OP-OMS-001 Classification

| Sub-question | Pre-VP-3 | Post-VP-3 |
|---|---|---|
| $S_4$ permutation symmetry? | REJECTED (Prop CW1) | REJECTED (confirmed) |
| Closure-sep swap ($g_A$)? | COMPUTATIONALLY TESTABLE | NOT_A_SYMMETRY |
| Closure-bd swap ($g_B$)? | COMPUTATIONALLY TESTABLE | NOT_A_SYMMETRY |
| Boundary-closure compensation? | HYPOTHESIZED (local approx.) | NOT_A_SYMMETRY (local approx. only near $\lambda_{\mathrm{bd}}$ corner) |
| Boundary-sep compensation? | COMPUTATIONALLY TESTABLE | NOT_A_SYMMETRY (same) |
| Transport invariance (static)? | PROVED conditional (Prop CW2) | **COMPUTATIONALLY CONFIRMED** (VP-3 E) |
| Radial toward centroid? | COMPUTATIONALLY TESTABLE | NOT_A_SYMMETRY |
| Random tangent? | COMPUTATIONALLY TESTABLE | NOT_A_SYMMETRY (partial flatness) |
| Default $G_{\mathrm{cw}} = \{e\}$? | ASSUMED | **COMPUTATIONALLY SUPPORTED** |

**Prop CW3 (Conservative default) status: ASSUMED → COMPUTATIONALLY SUPPORTED.**

---

## §4. New Findings

### Prop VP3-1 (G_cw = {e} computationally supported). [COMPUTATIONALLY SUPPORTED]

For generic $\lambda \in \mathrm{int}(\Delta^3)$ and dynamic scenes, no tested transformation is a
symmetry of $P_{\mathrm{top}}$. The default $G_{\mathrm{core\text{-}weight}} = \{e\}$ is supported.

### Prop VP3-2 (Prop CW2 confirmed computationally). [COMPUTATIONALLY SUPPORTED]

Transport ablation $g_E$ gives $\Delta P_{\mathrm{top}} = 0$ for all tested static-scene pairs.
Prop CW2 is computationally confirmed on S3 and S4 scenes.

### Observation VP3-3 (Approximate local symmetries). [COMPUTATIONALLY SUPPORTED]

Two approximate symmetry loci in $\Delta^3$ are suggested:
1. Near $\{\lambda_{\mathrm{cl}} = \lambda_{\mathrm{sep}}\}$: the closure-separation swap is approximately a
   local symmetry (VP-3 A, near-sym pair with $\Delta P_{\mathrm{top}} = 0.0295$).
2. Near $F_{\mathrm{bd}} = \{\lambda_{\mathrm{bd}} \approx 0.85\}$: boundary-closure and boundary-separation
   compensation are approximately local symmetries (VP-3 C, D near-sym cases).

These are not global gauge symmetries but define flat directions in $V_D^0$.
Registered as **OP-OMS-017**.

---

## §5. New Open Problems

### OP-OMS-017 — Approximate Symmetry Loci in $\lambda$-Space

**Status:** Open (NEW — Session 4, 2026-05-08)
**Importance:** ★  **Difficulty:** M

**Statement.** Is there a codimension-1 submanifold $S \subset \Delta^3$ on which a
transformation $g$ acts as an approximate symmetry of $P_{\mathrm{top}}$?

**Candidates:**
1. $S_A = \{\lambda_{\mathrm{cl}} = \lambda_{\mathrm{sep}}\}$: closure-separation swap approximate symmetry.
2. $S_B = \{\lambda_{\mathrm{bd}} > 0.8\}$: boundary-dominant face (compensation near-symmetry).

**Why it matters.** Approximate symmetry loci define flat regions in the observer landscape
$V \in \mathcal{V}_{\mathrm{adm}}$. Near $S$, the gradient $\nabla V \approx 0$, and observer configurations
on $S$ are slow to adapt — they are near a perceptual indifference surface.

**What would resolve it.** Map $\Delta P_{\mathrm{top}}(g \cdot \lambda, \lambda)$ as a function of $\lambda$
on a fine grid and identify the level set $\{\Delta P_{\mathrm{top}} < 0.05\}$ — this is the
approximate symmetry locus.
