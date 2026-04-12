# T-Persist-K-Strong: Morse-Theoretic Proof Attempt

**Date:** 2026-03-31
**Session:** Plan_0331 execution — strong-regime multi-formation theorem ladder
**Category:** proof
**Status:** active
**Depends on:** docs/03-31/repair/MULTI-TEMPORAL-THEORY.md, docs/03-31/repair/PERSIST-MORSE-ANALYSIS.md, docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md, Canonical Spec v2.0.md

---

## 1. Purpose

This document does **not** claim a full proof of `T-Persist-K-Strong`. Its purpose is to extract the strongest mathematically honest result currently supported by the repository and to organize the strong-regime claim into a theorem ladder:

1. a **conjecture** capturing the intended dichotomy,
2. a **conditional coexistence theorem** covering the compatible branch,
3. a **local negative theorem** showing what overlap-instability does imply,
4. a **conditional merge proposition** that makes every extra hypothesis explicit.

The central conclusion is that the current materials are sufficient to justify **local persistence of a strongly-overlapping \(K\)-formation state when the overlap block remains spectrally stable**, but **not** sufficient to prove that spectral instability forces convergence to a \((K-1)\)-formation minimizer without additional Morse/selection hypotheses.

---

## 2. Existing Strong-Regime Claim and Its Limitation

The current strong-regime statement appears in `docs/03-31/repair/MULTI-TEMPORAL-THEORY.md`:

> If the overlap block is compatible (\(\mu_{\mathrm{overlap}} > 0\)), the \(K\)-formation state persists;  
> if incompatible (\(\mu_{\mathrm{overlap}} \le 0\)), the pair merges and the flow descends to a \((K-1)\)-formation minimizer.

See:
- `docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:122-134`
- `Canonical Spec v2.0.md:807-809`

The file itself already marks the theorem as **conjectured** and identifies the missing ingredient correctly: one still needs **Morse-theoretic analysis on \(\Sigma_M^K\)** to upgrade the merge branch from heuristic to theorem (`docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:134`).

The main gap is structural:

- negativity of an overlap-restricted eigenvalue proves at most that the relevant critical point is **not a strict local minimum** in that direction,
- but it does **not** by itself prove
  - existence of a lower-energy \((K-1)\)-formation critical point,
  - uniqueness of the descending branch,
  - or that the projected gradient flow selects the merge branch rather than another nearby \(K\)-formation branch.

This is fully consistent with the single-formation basin analysis, where instability near bifurcation only yields directional fragility unless one also controls the actual saddle/barrier geometry (`docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:124-145`, `203-233`).

---

## 3. Fixed Ingredients We May Reuse

### 3.1. Product-manifold local persistence

The weakly-interacting theorem already gives the correct local mechanism:

- joint Hessian on \(\Sigma_M^K\),
- Weyl lower bound
  \[
  \mu_{\mathrm{joint}} \ge \min_k \mu_k - (K-1)\lambda_{\mathrm{rep}},
  \]
- IFT/local continuation when the joint spectral gap stays positive.

See:
- `docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:8-35`
- `docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:60-83`
- `Canonical Spec v2.0.md:936`

This mechanism does **not** fundamentally depend on weak interaction as a set-size condition. It depends on **local non-degeneracy on the relevant tangent space**.

### 3.2. Near-bifurcation fragility

The single-formation persistence synthesis already establishes:

- near bifurcation, \(\mu \to 0\),
- the isotropic basin bound deteriorates,
- exact-threshold persistence fails first,
- only shifted-threshold / local continuation statements remain honest.

See:
- `docs/03-31/repair/PERSIST-SYNTHESIS.md:97-107`
- `docs/03-31/repair/PERSIST-SYNTHESIS.md:120-130`
- `Canonical Spec v2.0.md:813`
- `Canonical Spec v2.0.md:1001`

Hence any strong-regime theorem must be split into:

1. a **positive-gap compatible branch**, and
2. a **bifurcation/instability branch** that is at best conditional unless global energy selection is controlled.

### 3.3. Experimental evidence

The empirical bimodality in strong interaction is real:

- low Persist for some overlapping cases,
- high Persist for others,
- suggesting a compatibility/incompatibility split.

See `docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:138-147`.

This is good evidence for the conjecture, but not a proof of the merge mechanism.

---

## 4. Where the Original Proof Attempt Breaks

### Failure Point A — overlap instability \(\not\Rightarrow\) merge theorem

From
\[
\mu_{\mathrm{overlap}} \le 0
\]
one may conclude there exists a non-positive second-variation direction inside the overlap subspace. This yields:

- loss of strict local minimality,
- or proximity to a bifurcation set,
- or existence of a descending direction for the quadratic approximation.

It does **not** yield:

\[
\text{gradient flow} \longrightarrow (K-1)\text{-formation minimizer}
\]
without extra hypotheses about the global energy landscape, critical-point connectivity, and flow selection.

The precise missing step is the jump from local spectral information to global branch selection in `docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:132-134`.

### Failure Point B — no proved merge competitor

Nothing in the current repository proves that, after instability of the \(K\)-branch, there exists a lower-energy \((K-1)\)-formation minimizer in the same connected component of the relevant sublevel set.

What is available instead:

- a single-formation sublevel-set basin method (`docs/03-31/repair/PERSIST-MORSE-ANALYSIS.md:37-64`),
- a directional barrier refinement (`docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:143-176`),
- but no analogous strong-regime competitor construction on \(\Sigma_M^K\).

### Failure Point C — unresolved strong-regime transport selection

The canonical spec remains explicit that the strong transport regime lacks a full existence/uniqueness/selection theory:

- `Canonical Spec v2.0.md:731`
- `Canonical Spec v2.0.md:813`
- `Canonical Spec v2.0.md:1001`

Therefore the statement “post-hoc correction destroys formation identity, confirming merge” is numerically plausible, but mathematically stronger than what has been established.

---

## 5. Strongest Honest Theorem Ladder

### 5.1. Conjecture C-KS (Strong-Regime Dichotomy)

**Conjecture C-KS.** Let \((u_t^1,\dots,u_t^K)\) be a strongly-interacting joint minimizer of \(\mathcal E_{K,t}\) on \(\Sigma_M^K\), and suppose the overlap set between some pair \((j,k)\) is macroscopic:
\[
|O_{jk}| > \eta \cdot \min(|\mathrm{Core}_j|, |\mathrm{Core}_k|).
\]
Under an \(\varepsilon\)-gentle transition, the temporal evolution exhibits a dichotomy:

1. if the overlap block remains spectrally stable (\(\mu_{\mathrm{overlap}} > 0\)), the \(K\)-formation branch persists;
2. if the overlap block loses stability (\(\mu_{\mathrm{overlap}} \le 0\)), the dynamics selects a merge branch with \(K_s < K_t\).

**Status:** conjecture with experimental support.  
**Evidence:** `docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:138-147`.

### 5.2. Conditional Theorem CT-KS1 (Compatible-Overlap Conditional Coexistence)

**Conditional Theorem CT-KS1.** Let \((u_t^1,\dots,u_t^K)\) be a joint minimizer of \(\mathcal E_{K,t}\) on \(\Sigma_M^K\). Assume:

- per-formation non-degeneracy \(\mu_k > 0\),
- spectral-repulsion compatibility
  \[
  \min_k \mu_k > (K-1)\lambda_{\mathrm{rep}},
  \]
- positive overlap-block stability
  \[
  \mu_{\mathrm{overlap}} > 0,
  \]
- sufficiently small \(\varepsilon\)-gentle transition,
- and a **strong-regime selection hypothesis** asserting that the transported/reoptimized branch stays on the local \(K\)-formation continuation rather than jumping to another nearby branch.

Then the joint minimizer continues locally to a \(K\)-formation critical point \((u_s^1,\dots,u_s^K)\) with \(K_s = K_t\), and the displacement obeys an IFT-style estimate
\[
\|(u_s^1,\dots,u_s^K) - (u_t^1,\dots,u_t^K)\| \le C \varepsilon_1 / \mu_{\mathrm{joint}}.
\]

**Proof.**

1. By the block-Hessian formula and Weyl bound,  
   \[
   \mu_{\mathrm{joint}} \ge \min_k \mu_k - (K-1)\lambda_{\mathrm{rep}} > 0
   \]
   (`docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:25-33`).
2. Hence the constrained Hessian on the product manifold is invertible at the joint critical point.
3. The same implicit-function continuation used in the weakly-interacting theorem applies locally on \(\Sigma_M^K\); weak interaction was used to control *quantitative transport concentration* and *small correction terms*, not to justify the local existence of the continued branch itself (`docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:81-83`).
4. Therefore a nearby \(K\)-formation branch exists for sufficiently gentle perturbation.
5. The extra strong-regime selection hypothesis is what upgrades mere branch existence to an honest “coexistence branch is the realized temporal branch” statement. □

**What this theorem does not prove.**

- It does not prove high Persist values.
- It does not prove correction is negligible.
- It does not prove overlap sites preserve deep-core concentration.
- It does not prove uniqueness of the continued branch.

It proves only the **local persistence of the \(K\)-branch**.

### 5.3. Proposition P-KS2 (Local Negative Theorem from Overlap Instability)

**Proposition P-KS2.** If
\[
\mu_{\mathrm{overlap}} \le 0,
\]
then the strongly-overlapping \(K\)-formation critical point is not a strict local minimizer in the overlap direction; in particular, the current branch cannot support the same local persistence theorem as Proposition P-KS1.

**Proof.** A non-positive minimum eigenvalue of the overlap-restricted Hessian yields a zero or negative second variation along an admissible overlap mode. Hence strict positivity of the local quadratic form fails on that subspace, so the hypothesis needed for the IFT/minimizer-continuation argument fails. □

**Interpretation.** This is an **instability theorem**, not yet a merge theorem.

### 5.4. Proposition P-KS3 (Near-Bifurcation Collapse of the Coexistence Window)

**Proposition P-KS3.** Along any strong-regime parameter path for which the joint or overlap spectral gap tends to zero,
\[
\mu_{\mathrm{joint}} \to 0 \quad \text{or} \quad \mu_{\mathrm{overlap}} \to 0,
\]
the admissible gentle-transition window for local branch persistence collapses. More precisely, any IFT-style persistence estimate of the form
\[
\|(u_s^1,\dots,u_s^K) - (u_t^1,\dots,u_t^K)\| \le C\varepsilon_1/\mu_{\mathrm{joint}}
\]
requires \(\varepsilon_1 = o(\mu_{\mathrm{joint}})\), so near bifurcation no uniform coexistence theorem can hold at fixed perturbation scale.

**Proof.** This is the direct product-manifold analogue of the single-formation non-bifurcation condition, where the persistence budget deteriorates like \(2\varepsilon_1/\mu\) and the theorem explicitly excludes bifurcation windows (`docs/03-31/repair/PERSIST-SYNTHESIS.md:120-130`, `Canonical Spec v2.0.md:993-1001`). Replacing \(\mu\) by \(\mu_{\mathrm{joint}}\) gives the same conclusion. □

**Interpretation.** Near bifurcation, the strongest honest statement is not coexistence or merge, but only: “the stable-branch theorem loses uniform quantitative content.”

### 5.5. Conditional Proposition CT-KS4 (Merge Under Morse-Selection Hypotheses)

**Conditional Proposition CT-KS4.** Assume, in addition to \(\mu_{\mathrm{overlap}} \le 0\), the following:

- **(MS1)** Morse non-degeneracy/transversality for the perturbed product energy near the overlapping branch;
- **(MS2)** existence of a lower-energy \((K-1)\)-formation critical point in the same connected sublevel component;
- **(MS3)** the projected gradient flow from the transported initial condition stays inside that sublevel component and does not enter another \(K\)-formation basin;
- **(MS4)** strong-regime transport selection picks the continuation compatible with that descending branch.

Then the perturbed flow converges to a merged state with \(K_s < K_t\).

**Status:** mathematically plausible but conditional.  
**Reason:** none of (MS1)–(MS4) is currently proved in the repository.

---

## 6. Recommended Status Upgrade Path

### Level 0 — keep canonical theorem as conjecture

This is the current honest status:
- `docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:134`
- `Canonical Spec v2.0.md:809`

### Level 1 — keep full dichotomy as conjecture

This is still the correct top-level status.

### Level 2 — state only a conditional coexistence theorem

This is the strongest safe positive theorem:

> **Conditional coexistence theorem.**  
> Positive joint/overlap spectral gap plus explicit strong-regime branch-selection lets one continue the \(K\)-formation branch locally.

### Level 3 — add only local negative/near-bifurcation propositions

These are safe now:

- overlap-instability destroys strict local minimality of the current \(K\)-branch,
- near-bifurcation collapses the quantitative coexistence window.

### Level 4 — future conditional merge theorem / future full theorem

To fully prove `T-Persist-K-Strong`, one must add:

1. overlap-mode saddle analysis on \(\Sigma_M^K\),
2. existence of a merge competitor branch,
3. a sublevel-set argument ruling out return to another \(K\)-branch,
4. strong-regime transport selection/uniqueness.

---

## 7. Consequence for Plan_0331

The mathematically honest execution order is:

1. **write a 3-regime synthesis** with strong regime explicitly labeled as theorem ladder;
2. **write a near-bifurcation local theory** explaining why positive-gap persistence collapses to shifted-threshold/local continuation statements;
3. only then consider any Canonical Spec upgrade.

At the current stage, the canonical spec should be updated only to:

- preserve `T-Persist-K-Strong` as conjectured,
- add the compatible-branch proposition if desired,
- and sharpen the open problem list around the four missing ingredients in §6.

---

## 8. Final Verdict

**What is defensibly stated now**

- a **conditional coexistence theorem** for the compatible branch,
- an instability proposition showing why the incompatible branch cannot be treated by the same local theorem,
- and a near-bifurcation proposition showing why no uniform coexistence theorem can survive as \(\mu_{\mathrm{joint}}\to 0\).

**What is not proved now**

- that incompatibility forces merge,
- that the flow lands in a \((K-1)\)-formation minimizer,
- or that strong-regime transport has the selection properties needed to choose that branch.

So the correct status is:

- **Conjecture:** full dichotomy,
- **Conditional theorem:** compatible branch persists locally,
- **Proposition:** instability / near-bifurcation collapse,
- **Conditional proposition:** merge branch under explicit Morse-selection assumptions.
