# Three-Regime Synthesis for Multi-Formation Temporal Persistence

**Date:** 2026-03-31
**Session:** Plan_0331 execution — multi-formation regime unification
**Category:** theory
**Status:** complete
**Depends on:** docs/03-31/repair/MULTI-TEMPORAL-THEORY.md, docs/03-31/repair/PERSIST-SYNTHESIS.md, docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md, Canonical Spec v2.0.md

---

## 1. Purpose

This document separates the current multi-formation temporal theory into three mathematically distinct regimes:

1. **well-separated**,
2. **weakly-interacting**,
3. **strongly-interacting**.

The main point is that these three regimes do **not** share the same theorem status.

- The **well-separated** regime is already a proved theorem.
- The **weakly-interacting** regime is a conditional theorem whose dependencies are explicit.
- The **strongly-interacting** regime cannot honestly be stated as a full proved dichotomy; only its **coexistence branch** is conditionally defensible at theorem/proposition level, while the full merge dichotomy remains conjectural.

This regime split is not cosmetic. It is forced by the current mathematical evidence: local continuation is controlled by joint spectral positivity, while merge/birth/death behavior requires additional Morse-type global branch analysis that the repository does not yet contain.

---

## 2. Shared Ambient Structure

All three regimes live on the product constraint manifold
\[
\Sigma_M^K = \Sigma_{m_1} \times \cdots \times \Sigma_{m_K},
\]
with joint energy
\[
\mathcal E_K(u^1,\dots,u^K)
= \sum_{k=1}^K \mathcal E_{\mathrm{self}}(u^k)
+ \sum_{j<k} \lambda_{\mathrm{rep}}\langle u^j,u^k\rangle
+ \lambda_{\mathrm{bar}}\sum_x \max\!\left(0,\sum_k u^k(x)-1\right)^2.
\]

The common local control quantity is the active-set-aware joint Hessian spectral gap. In the current theory the key lower bound is the Weyl-type estimate
\[
\mu_{\mathrm{joint}} \ge \min_k \mu_k - (K-1)\lambda_{\mathrm{rep}},
\]
with the spectral-repulsion compatibility hypothesis
\[
\min_k \mu_k > (K-1)\lambda_{\mathrm{rep}}.
\]

This is the shared continuation mechanism across regimes (`docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:8-35`). The regimes differ in **how much coupling leaks into the core/boundary structure**, and therefore in **how much of the single-formation persistence package survives unchanged**.

---

## 3. Regime I — Well-Separated

### 3.1. Defining condition

The well-separated regime is characterized by a hard distance gap between formations:
\[
d_{\min}(j,k) \ge D_{\mathrm{sep}} \ge 3
\quad\text{for all } j\neq k,
\]
so that core and boundary layers of distinct formations do not interact at leading order (`Canonical Spec v2.0.md:935-939`).

### 3.2. Current theorem status

**Status: proved (conditional on the explicit single-formation hypotheses).**

The repository already treats `T-Persist-K-Sep` as a proved result in the well-separated regime (`Canonical Spec v2.0.md:935-939`, `AGENTS.md:140`, `plan/Plan_0331.md:28`).

### 3.3. What is proved here

Under per-formation hypotheses `(H1-K)`, well-separation `(WS)`, and spectral-repulsion compatibility `(SR)`, the theory provides:

- per-formation minimizer persistence,
- preservation of inter-formation separation,
- preservation of deep-core transport concentration,
- negligible simplex violation,
- no need for strong post-hoc correction.

The underlying reason is geometric decoupling: core/boundary transport estimates are essentially inherited formation-by-formation, while coupling enters only as an exponentially small correction at depth (`Canonical Spec v2.0.md:935-939`).

### 3.4. Mathematical interpretation

This is the regime where the multi-formation theory is closest to a direct product of the single-formation theory. The correct slogan is:

> **well-separated = single-formation persistence plus controlled off-diagonal perturbation.**

No branch-switching or formation-count change needs to be addressed here.

---

## 4. Regime II — Weakly-Interacting

### 4.1. Defining condition

Weak interaction begins when overlap is no longer zero but remains boundary-scale:
\[
|O_{jk}| \le \eta \cdot \min(|\mathrm{Core}_j|,|\mathrm{Core}_k|),
\qquad \eta < 0.2,
\]
so the overlap is small relative to the core mass (`docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:60-67`, `Canonical Spec v2.0.md:982-985`).

### 4.2. Current theorem status

**Status: conditional theorem.**

The repository explicitly marks `T-Persist-K-Weak` as conditionally proved under `(H1-K)`, `(WI)`, `(NB-K)`, `(SR)`, plus the single-formation `T-Persist-1` package (`docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:60-83`, `Canonical Spec v2.0.md:982-985`).

### 4.3. What survives from single-formation persistence

The surviving structure is two-tiered:

1. **deep core remains decoupled**, because overlap corrections are exponentially small away from the boundary;
2. **boundary overlap sites lose full concentration guarantees**, so only shifted-threshold persistence remains available there;
3. **simplex correction remains basin-safe**, but now it must be bounded explicitly.

Thus the weakly-interacting theorem is genuinely stronger than a heuristic, but weaker than a full per-site persistence theorem. Its correct interpretation is:

> **weakly-interacting = joint continuation theorem with deep-core inheritance and boundary fallback.**

### 4.4. Why the theorem is only conditional

The theorem still depends on:

- joint non-bifurcation,
- positive joint spectral gap,
- deep-core existence,
- the single-formation basin/concentration package.

These dependencies matter because weak overlap does **not** remove the bifurcation problem; it only keeps it away from the deep core. So the theorem is stable only in the away-from-bifurcation regime.

---

## 5. Regime III — Strongly-Interacting

### 5.1. Defining condition

Strong interaction begins when overlap becomes core-scale:
\[
|O_{jk}| > \eta \cdot \min(|\mathrm{Core}_j|,|\mathrm{Core}_k|)
\]
for some pair `(j,k)` (`docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:122-123`).

Here the overlap is no longer a boundary perturbation. It becomes part of the dominant local energy geometry.

### 5.2. The old informal claim

The current repair document states a dichotomy:

- **compatible overlap** (`\mu_{\mathrm{overlap}} > 0`) → coexistence persists,
- **incompatible overlap** (`\mu_{\mathrm{overlap}} \le 0`) → merge occurs,

but it also marks that statement as **conjectured** because a Morse-theoretic proof is missing (`docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:120-134`).

### 5.3. Current mathematically honest status

The strong regime must be split into two branches with different epistemic status.

#### (A) Coexistence branch

**Conditionally defensible.**

If the strongly-overlapping branch still satisfies:

- active-set-aware joint non-degeneracy,
- positive overlap-block spectral gap,
- positive barrier separating the current `K`-formation branch from nearby lower-`K` competitors,
- sufficiently gentle temporal perturbation remaining inside the joint basin,

then a **local continuation / coexistence theorem** is defensible. This is the strong-overlap analogue of the weakly-interacting IFT argument. What it proves is only persistence of the same `K`-branch, not global optimality across all branch changes.

#### (B) Merge branch

**Still conjectural in full form.**

From
\[
\mu_{\mathrm{overlap}} \le 0
\]
one obtains instability of the overlap block, but not yet the full conclusion that gradient flow lands in a `(K-1)`-formation minimizer. That stronger claim requires additional Morse/selection inputs:

- merge-mode saddle structure,
- existence of a lower-`K` competitor branch,
- sublevel connectivity/selectability,
- strong-regime transport branch selection.

These are currently missing, and the repair document itself says so (`docs/03-31/repair/MULTI-TEMPORAL-THEORY.md:132-134`, `Canonical Spec v2.0.md:1001`).

### 5.4. Correct slogan

> **strongly-interacting = theorem ladder, not one theorem.**

Concretely:

- **safe non-conjectural statement:** compatible-branch local persistence under explicit positivity/barrier hypotheses;
- **safe instability statement:** negative overlap gap destroys the same local minimizer theorem;
- **remaining conjecture:** instability plus Morse selection implies merge / formation death.

### 5.5. Relation to birth/death

The strong regime is where the theory first touches dynamic changes in formation count (`K_t \to K_s`). But the current state of the mathematics supports only:

- **coexistence branch continuation** under positive local stability,
- **merge-prone instability** under negative overlap stability,

not yet a full birth/death theorem.

---

## 6. Cross-Regime Comparison Table

| Regime | Geometric condition | Best current status | What is genuinely secured | What remains open |
|---|---|---|---|---|
| Well-separated | `d_min >= 3` | **Proved** | Per-formation persistence, separation, deep-core transport concentration, negligible simplex violation | No major regime-internal gap beyond single-formation dependencies |
| Weakly-interacting | boundary-scale overlap | **Conditional theorem** | Joint continuation, deep-core inheritance, shifted-threshold fallback on overlap/boundary sites, basin-safe correction | Dependence on `(NB-K)`, basin hypotheses, strong transport selection |
| Strongly-interacting | core-scale overlap | **Theorem ladder only** | Compatible-branch local continuation is conditionally defensible; instability criterion is meaningful | Full merge dichotomy, formation death theorem, branch selection, birth/split theory |

---

## 7. Three-Regime Theorem Ladder

### 7.1. Global synthesis statement

The strongest mathematically honest three-regime synthesis currently available is:

1. **Well-separated regime:** a proved persistence theorem.
2. **Weakly-interacting regime:** a conditional continuation theorem with deep-core persistence and boundary fallback.
3. **Strongly-interacting regime:** a bifurcation-sensitive theorem ladder where local coexistence is conditionally defensible, but merge remains conjectural unless additional Morse-selection hypotheses are imposed.

### 7.2. Consequence for future theorem writing

Future statements should never compress these three into one uniform theorem. The correct writing discipline is:

- do **not** call strong-regime merge a proved theorem,
- do **not** speak of weak interaction as if it preserved all sites equally,
- do **not** downgrade the well-separated theorem to mere heuristic.

The regimes differ because the **branch geometry** differs.

---

## 8. Open Problems Forced by the Regime Split

The regime synthesis isolates four genuinely open multi-formation problems:

1. **strong-regime merge theorem** — proving branch switching to `(K-1)` under overlap instability;
2. **formation birth theorem** — reverse bifurcation / branch creation;
3. **strong-regime transport selection** — uniqueness/selection of the self-referential transport continuation;
4. **near-bifurcation regime matching** — how the strong-regime ladder couples to the single-formation collapse of basin radius.

---

## 9. Final Assessment

The multi-formation temporal theory is no longer a single unresolved block. It already has a genuine internal hierarchy:

- **Regime I:** settled,
- **Regime II:** conditionally organized,
- **Regime III:** conceptually sharp but not yet globally proved.

That is a mathematically stronger position than simply saying “`T-Persist-K-Strong` is open.” The correct statement is:

> the strong regime is **structured enough to be decomposed into a coexistence proposition, an instability proposition, and a merge conjecture**, but not yet structured enough to collapse these into one proved dichotomy theorem.
