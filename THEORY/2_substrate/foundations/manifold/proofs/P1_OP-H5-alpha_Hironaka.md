---
type: working/foundation/proof-attempt
target_OP: OP-H5-α (Hironaka algebraic strengthening of generic Morse via Sard)
target_cat: A (conditional on Lemma L3 Sub-step 2; honest Cat B fallback explicit)
date: 2026-05-19
predecessor:
  - /tmp/scc_proofs_v02/E1_hironaka_literature.md  (Phase 1 E1, direct input)
  - THEORY/logs/daily/2026-05-19/02_H5_morse_spinodal.md §2 (L1-L5 sketch)
  - THEORY/logs/daily/2026-05-19/01_pre_brainstorm.md §6.3 (Hironaka anchor)
canonical_version: CV-1.17 (sealed 2026-05-15, untouched)
canonical_anchors:
  - T-P-F-ε0-K (Cat B, L1818-1833)         # direct Cat A path target
  - SB7 (Cat A, L2495)                       # Σ_Hess = Σ_T8 codim-1
  - SN3 (Cat B conditional, L2501)           # Crandall-Rabinowitz fold sister
  - V5b-T-zero (Cat A definitional, L1328)   # uniform sheet exact zero
  - T-PERSIST-1B-UNCONDITIONAL (Cat A, L2063) # Sard precedent in canonical
  - T8 (canonical central, DECLARATION.md)   # spinodal phase transition
cot_enforced: yes
coc_enforced: yes
silent_failure_policy: 0   # explicit assessment if any sub-step fails
prior_step: Phase 1 E1 literature scan complete (/tmp/scc_proofs_v02/E1_hironaka_literature.md, 339L)
next_step: Phase 3 V1 mathematical rigor verification (Session 2)
status: draft (full proof attempt; Cat A conditional)
---

> [!nav] Linked: [[../../../canonical/canonical|canonical CV-1.17]] · [[../../../logs/daily/2026-05-19/02_H5_morse_spinodal|02_H5 §2 L1-L5 sketch]] · [[../../../logs/daily/2026-05-19/01_pre_brainstorm|01_pre_brainstorm §6.3]] · `/tmp/scc_proofs_v02/E1_hironaka_literature.md`

# P1 — OP-H5-α Full Proof Attempt (Hironaka Algebraic Strengthening)

**Mission**: 02_H5 §2.3 Lemma L3 의 *sketch* 를 *full proof attempt* 로 격상. 즉, SCC 의 *singular locus* 의 $\Theta$-projection 이 $\mathbb{R}^4_{>0}$ 안에서 *real algebraic codim ≥ 1* (Zariski-open dense complement) 임을 명시적으로 증명한다.

**Strategy** (E1 §8 recommended primary path): *Dimension Count + Tarski-Seidenberg*. Hironaka 1964 은 *authority citation* 으로 인용하되, 실제 proof 는 (i) bilinear $(\Theta, u)$ structure 에서의 Jacobian rank 계산 + (ii) Tarski-Seidenberg semialgebraic dimension 보존으로 수행.

**Honest disclaimer (Silent failure policy 0)**: Lemma L3 의 Sub-step 2 (Hessian-determinant 행벡터의 gradient-rows 와의 *generic* 선형독립) 가 *sketch level* 로 머무는 부분 — 본 attempt 의 Cat A 진입은 *이 sub-step 의 symbolic verification 을 W9+ 에서 수행한다는 조건* 하에서만 성립. 실패 시 Cat B (Lebesgue measure zero version 으로 fallback) 가 안전한 ceiling.

---

## §0 Pre-work xref check (§15.1 의무 기록)

```bash
$ grep -nE "OP-H5-α|OP-H5-alpha|Hironaka algebraic strengthening" THEORY/canonical/canonical.md
# 0 hits — canonical 에 미등록 (정상; OP catalog 등록 대기, 02_H5 §4 draft only)

$ grep -rn "P1_OP-H5-alpha" THEORY/working/
# 0 hits — clean slate (본 file 이 첫 작성)

$ grep -nE "polynomial.*generic|Sard.*algebraic|Tarski-Seidenberg" THEORY/canonical/canonical.md
# 1 hit: L2063 T-PERSIST-1B-UNCONDITIONAL 의 Erratum 2026-04-03 (Sard's theorem applied)
# = Sard precedent confirmed in canonical; Tarski-Seidenberg 는 canonical 에 부재 — 본 file 이 처음 도입

$ grep -nE "Σ_Hess.*codim|Σ_T8.*codim" THEORY/canonical/canonical.md
# 2 hits: L2495 (SB7: Σ_Hess = Σ_T8 codim-1 on uniform sheet) + L2627 (temporal envelope)
# = SB7 anchor confirmed for L5 (Σ_T8 codim-1)
```

**verdict**: clean slate for OP-H5-α; novel content = E1 §8 권장 dimension-count proof 의 *완결*. *Canonical 의 SB7 / T-PERSIST-1B-UNCONDITIONAL / V5b-T-zero 와의 정합* 확인 (§8).

---

## §1 Statement (Target Cat A Precise Form)

### §1.1 Σ_degen Definition + Algebraic Subvariety Verification

**Setup**. Fix a finite connected graph $G = (V, E)$ with $\lvert V \rvert = n$, graph Laplacian $L$, second eigenvalue $\lambda_2 = \lambda_2(L) > 0$. Fix mass $m \in (0,1)$ and define the affine simplex
$$\Sigma_m := \{u \in [0,1]^n : \mathbf{1}^\top u = m\}, \qquad T_u \Sigma_m = \{v \in \mathbb{R}^n : \mathbf{1}^\top v = 0\} \quad (\text{intrinsic dim } n-1).$$

SCC energy on $\Sigma_m$ (canonical §13 Theorem 4 + CLAUDE.md "Critical Implementation Details"):
$$\mathcal{E}_\Theta(u) = \lambda_{\mathrm{cl}}\,\mathcal{E}_{\mathrm{cl}}(u) + \lambda_{\mathrm{sep}}\,\mathcal{E}_{\mathrm{sep}}(u) + \alpha\,\mathcal{E}_{\mathrm{bd}}^{\mathrm{Dir}}(u) + \beta\,\mathcal{E}_{\mathrm{bd}}^{\mathrm{DW}}(u),$$
where $\Theta := (\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \alpha, \beta) \in \mathbb{R}^4_{>0}$ (mass $m$ absorbed as $\Sigma_m$ constraint), and the four terms have the explicit polynomial form derived in §3.1 below.

**Definition (Σ_degen)**. The *singular locus*:
$$\boxed{\;\Sigma_{\mathrm{degen}} := \Bigl\{(\Theta, u) \in \mathbb{R}^4_{>0} \times \Sigma_m \;\Big\vert\; \nabla_{\Sigma_m}\mathcal{E}_\Theta(u) = 0 \;\wedge\; \det\bigl(\mathrm{Hess}\,\mathcal{E}_\Theta(u)\vert _{T_u\Sigma_m}\bigr) = 0\Bigr\}\;}$$

**Claim (1)**. $\Sigma_{\mathrm{degen}}$ is a *real algebraic subvariety* (modulo clearing of resolvent denominators; cf. §3.1) of the ambient *semialgebraic* set $\mathbb{R}^4_{>0} \times \Sigma_m$.

> *Rationale (preview)*: $\nabla_{\Sigma_m}\mathcal{E}_\Theta(u) = 0$ contributes $n-1$ polynomial equations (mass-projected gradient components); $\det H = 0$ contributes one polynomial equation. Both are polynomial in $(\Theta, u)$ once the resolvent appearing in $\mathcal{E}_{\mathrm{cl}}$ is cleared (multiply by $\det(\mathrm{Id} + a_{\mathrm{cl}} L)$ which is nowhere zero for $a_{\mathrm{cl}} \in (0, 4/\lambda_n(L))$).

### §1.2 proj_Θ codim ≥ 1 Statement

**Definition**. $\mathrm{proj}_\Theta: \mathbb{R}^4_{>0} \times \Sigma_m \to \mathbb{R}^4_{>0}$, $(\Theta, u) \mapsto \Theta$.

**Claim (2)**. $\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}})$ is a semialgebraic set of *codimension $\geq 1$* in $\mathbb{R}^4_{>0}$:
$$\dim_{\mathbb{R}}\bigl(\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}})\bigr) \;\leq\; 3, \qquad \dim_{\mathbb{R}}(\mathbb{R}^4_{>0}) = 4,$$
hence its complement contains a Zariski-open dense subset.

### §1.3 Consequence (D_Morse Zariski-Open Dense)

**Definition**. The *Morse parameter domain*:
$$\mathcal{D}_{\mathrm{Morse}}(G, m) := \mathbb{R}^4_{>0} \setminus \mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}}).$$

**Consequence**. By (2), $\mathcal{D}_{\mathrm{Morse}}(G, m)$ is *Zariski-open and dense* (in standard topology). For every $\Theta \in \mathcal{D}_{\mathrm{Morse}}$, the restricted energy $\mathcal{E}_\Theta\vert _{\Sigma_m}$ is a *Morse function*: every critical point is non-degenerate (Hessian invertible on $T_u\Sigma_m$).

### §1.4 Implication for T-P-F-ε0-K Cat A Path

**Canonical anchor**. T-P-F-ε0-K (Cat B, L1818-1833)의 (H5) Morse stability 가정이 *generic regime* 에서 trivially satisfied. 즉:

> *(H5) for $\Theta \in \mathcal{D}_{\mathrm{Morse}}$*: every critical point of $\mathcal{E}_\Theta + \varepsilon R$ is non-degenerate for $\varepsilon \in [0, \varepsilon_0]$ sufficiently small (continuity of eigenvalues + invertibility persistence).

Combining the present theorem with canonical SB7 (Cat A, L2495 — $\Sigma_T8$ codim-1 separate stratum) yields the *Cat A promotion path* sketched in 02_H5 §5.2 for (H5') regime restriction:
$$\boxed{\;\text{T-P-F-ε0-K Cat A on } \mathcal{R}_{\mathrm{post}} \cap \mathcal{D}_{\mathrm{Morse}} \;=\; \text{(present theorem)} + \text{SB7}.\;}$$

---

## §2 Multi-Approach (Three Mathematically Independent Paths)

### §2.1 Approach A — Dimension Count + Tarski-Seidenberg (PRIMARY)

**Idea** (E1 §8): Count *variables vs equations* in the bilinear polynomial system defining $\Sigma_{\mathrm{degen}}$. The Jacobian matrix is $n \times (n+3)$; if it has *generic rank $n$*, then $\Sigma_{\mathrm{degen}}$ has algebraic dimension $\leq 3$ in the $(n+3)$-dimensional ambient $\mathbb{R}^4_{>0} \times \Sigma_m$ (intrinsic $\Sigma_m$ dim $= n-1$, plus $\Theta$ dim $= 4$). Tarski-Seidenberg then preserves $\dim \leq 3$ under $\mathrm{proj}_\Theta$.

**Tool tree**:
- Sard 1942 (smooth maps, measure-zero critical values) — *baseline* but only Lebesgue.
- Tarski-Seidenberg 1951/1954 (semialgebraic projection) — *core* for codim ≥ 1.
- Bochnak-Coste-Roy 1998 §2, §5 (real algebraic dimension theory) — *technical backbone*.

**Failure mode**: if the Jacobian rank is *uniformly less than $n$* on $\Sigma_{\mathrm{degen}}$, the dimension bound degrades to $\geq 4$ and codim ≥ 1 fails. This is the *real* gap (§3.3 Sub-step 2).

**Success condition**: bilinear polynomial system + connected $G$ (so $\lambda_2(L) > 0$) + interior of $\Sigma_m$ (so $u_i \in (0,1)$).

### §2.2 Approach B — Hironaka Resolution + Embedded Form (AUTHORITY ANCHOR)

**Idea**: Hironaka 1964 desingularizes any complex algebraic variety (char 0). Apply to the *complexification* $\Sigma_{\mathrm{degen}}^{\mathbb{C}} \subset \mathbb{C}^4 \times \mathbb{C}\Sigma_m$, resolve, then descend to real points via real-algebraic structure.

**Tool tree**:
- Hironaka 1964 *Annals of Math* 79 (resolution, complex char 0).
- Whitney 1957 *Annals of Math* 66 (real algebraic stratification).
- Bierstone-Milman 1988 (canonical resolution, applicable to real-analytic).

**Failure mode**: Hironaka 의 real version 은 더 미묘 — *real* desingularization 은 complex case 의 *직접* corollary 아님 (real points may be empty after complex resolution). 보완은 Bierstone-Milman 의 real-analytic version 또는 Whitney stratification 직접 사용.

**Why secondary**: real-analytic 적용 시 추가 work (real points 추적). Approach A 가 *real semialgebraic* setting 에서 더 직접적.

**Role**: *citation authority* — "polynomial maps 의 singular set 은 algebraic" 의 정당성 (B-K-R 정리도 동치 효과).

### §2.3 Approach C — Federer Finite-Codim Sard (ALTERNATIVE)

**Idea**: Federer 1969 *Geometric Measure Theory* §3.4 — polynomial maps 의 critical values 의 *Hausdorff dimension* upper bound. Yields *measure-theoretic* codim ≥ 1.

**Tool tree**:
- Federer 1969 (Hausdorff dimension + Lipschitz maps).
- Smale 1965 (infinite-dim Sard variant; here finite-dim suffices).
- Yomdin 1983 (semialgebraic complexity bounds).

**Failure mode**: Federer 의 codim 은 *measure-theoretic* (Hausdorff dim), 본 정리의 *algebraic codim* 과 동치 아님 — semialgebraic set 의 Hausdorff dim = algebraic dim 은 별도 보조정리 (BCR §2.8).

**Why secondary**: canonical promotion 시 *algebraic dimension* 명시가 필요 (Zariski-open 의 정확한 의미). Federer 만으로는 Lebesgue 까지만 — Approach A 의 Tarski-Seidenberg 가 algebraic upgrade 의 *직접* tool.

### §2.4 Approach 3-Criteria Check

| Criterion | A (Dim+T-S) | B (Hironaka) | C (Federer) |
|---|---|---|---|
| **Mathematical tool** | semialgebraic dim theory | resolution of singularities | geometric measure theory |
| **Output codim type** | Zariski (algebraic) | Zariski (algebraic) | Hausdorff (measure) |
| **Failure mode** | Jacobian rank < n | real points lost in complex resolution | algebraic ≠ Hausdorff codim |
| **Success condition** | bilinear $(\Theta, u)$ structure | char 0 (auto for $\mathbb{R}$) + real-anal lift | polynomial map (auto) |
| **Cat A path** | yes (primary) | yes (with B-M extension) | partial (Lebesgue only) |

세 approach 의 *수학적 독립* (서로 다른 tool tree) + *실패 모드 다름* (Jacobian rank vs real-lift vs codim notion) + *조건부 성공 조건 다름* — deep-attack 3-criteria PASS.

**Verdict**: Approach A primary; B as authority citation; C as cross-check (Lebesgue-only fallback).

---

## §3 Primary Approach (A) — Detailed Proof

### §3.1 Lemma L1 — SCC E_λ Explicit Polynomial Structure

**Lemma L1**. Let $\mathcal{E}_\Theta(u)$ be the SCC energy as in §1.1. Then there exists a polynomial $\widetilde{\mathcal{E}}(\Theta, u) \in \mathbb{R}[\Theta, u]$ of total degree $\leq 4$ in $u$ and $\leq 1$ in each of $(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \alpha, \beta)$ (i.e., $\Theta$-multilinear, hence linear in $\Theta$), such that on the interior $\{u_i \in (0,1), \mathbf{1}^\top u = m\} \cap \{a_{\mathrm{cl}} < 4/\lambda_n(L)\}$:
$$\det(\mathrm{Id} + a_{\mathrm{cl}} L) \cdot \mathcal{E}_\Theta(u) \;=\; \widetilde{\mathcal{E}}(\Theta, u).$$

**Proof (CoT)**.

*CoT step 1 — Closure term*. The closure energy is
$$\mathcal{E}_{\mathrm{cl}}(u) = u^\top (\mathrm{Id} - P_{\mathrm{cl}})u, \quad P_{\mathrm{cl}} := (\mathrm{Id} + a_{\mathrm{cl}} L)^{-1}\cdot D_{\mathrm{row}}^{-1}\cdot W,$$
where $W = $ cohesion-weighted adjacency, $D_{\mathrm{row}} = $ row-sum diagonal (canonical operators.py). The resolvent $(\mathrm{Id} + a_{\mathrm{cl}} L)^{-1}$ is *rational* in $a_{\mathrm{cl}}$, not polynomial. *Standard clearing*: multiply by $\det(\mathrm{Id} + a_{\mathrm{cl}} L) = \prod_k (1 + a_{\mathrm{cl}} \lambda_k(L))$ to obtain a polynomial. For $a_{\mathrm{cl}} \in (0, 4/\lambda_n(L))$ (canonical $a_{\mathrm{cl}} < 4$ regime + connected $G$ so $\lambda_n(L) \leq 4$ for grids; general bound via $\lambda_n \leq 2\Delta(G)$), this determinant is nonzero. Set
$$\widetilde{\mathcal{E}}_{\mathrm{cl}}(\Theta, u) := \det(\mathrm{Id} + a_{\mathrm{cl}} L) \cdot u^\top(\mathrm{Id} - P_{\mathrm{cl}})u,$$
a polynomial of degree 2 in $u$, degree $\leq n$ in $a_{\mathrm{cl}}$ (from $\det$ expansion), degree 1 in $\lambda_{\mathrm{cl}}$.

*CoT step 2 — Separation term*. canonical:
$$\mathcal{E}_{\mathrm{sep}}(u) = -\frac{\sum_i u_i D_i}{\sum_i u_i}, \quad D_i := \text{degree-weighted distinction (graph-fixed)}.$$
On $\Sigma_m$, the denominator $\sum_i u_i = m$ is *constant*. Hence
$$\mathcal{E}_{\mathrm{sep}}(u)\vert _{\Sigma_m} = -\frac{1}{m}\sum_i u_i D_i,$$
which is *linear in $u$* (degree 1), independent of $\Theta$ except for the $\lambda_{\mathrm{sep}}$ prefactor (degree 1 in $\lambda_{\mathrm{sep}}$).

*Gotcha #5 (E1)*: the rational form $\sum u_i D_i / \sum u_i$ in *general* (off $\Sigma_m$) would obstruct polynomiality; *restriction to $\Sigma_m$* (mass constraint enforced) is what makes it polynomial. This is the *explicit* polynomial form claimed in canonical §13.

*CoT step 3 — Boundary (Dirichlet) term*. canonical CLAUDE.md "Critical Implementation Details":
$$\mathcal{E}_{\mathrm{bd}}^{\mathrm{Dir}}(u) = 2 u^\top L u \quad (\text{factor 2, ordered-pair sum}),$$
quadratic in $u$, $\Theta$-independent except for $\alpha$ prefactor.

*CoT step 4 — Boundary (double-well) term*. canonical "I6 correction":
$$\mathcal{E}_{\mathrm{bd}}^{\mathrm{DW}}(u) = \sum_i u_i^2(1 - u_i)^2 = \sum_i (u_i^2 - 2u_i^3 + u_i^4),$$
quartic in $u$ (each term separable per-vertex), $\Theta$-independent except for $\beta$ prefactor. (Gradient: $W'(u) = 2u(1-u)(1-2u)$ matches I6.)

*CoT step 5 — Aggregation*.
$$\widetilde{\mathcal{E}}(\Theta, u) = \lambda_{\mathrm{cl}}\widetilde{\mathcal{E}}_{\mathrm{cl}} + \det(\mathrm{Id}+a_{\mathrm{cl}}L)\cdot\Bigl[\lambda_{\mathrm{sep}}\cdot(-\tfrac{1}{m}\sum_i u_i D_i) + 2\alpha\, u^\top L u + \beta\sum_i u_i^2(1-u_i)^2\Bigr].$$

This is polynomial in $u$ of degree $\leq 4$ (quartic from double-well dominant), polynomial in $\Theta$ of degree $\leq 1$ in each of $\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \alpha, \beta$ (i.e., $\Theta$-*multilinear* hence $\Theta$-linear in our 4-parameter setting). □

**CoC anchors**:
- canonical §13 Theorem 4 (polynomial form of $\mathcal{E}_\Theta$).
- CLAUDE.md "Critical Implementation Details" (factor 2 ordered-pair, factor 2 in $W'$, double-well shape).
- E1 §6 (variable + equation count).
- Gotcha #5 ($\Sigma_m$ restriction makes $\mathcal{E}_{\mathrm{sep}}$ polynomial).

**Remark (a_cl pole)**: the clearing factor $\det(\mathrm{Id}+a_{\mathrm{cl}}L)$ is nonzero on the canonical open regime $a_{\mathrm{cl}} \in (0, 4/\lambda_n(L))$; the pole $a_{\mathrm{cl}} = -1/\lambda_k(L)$ is outside this regime. Thus the *polynomial form* $\widetilde{\mathcal{E}}$ and the *original* $\mathcal{E}_\Theta$ share the same zero set on the regime — for proving codim ≥ 1 it suffices to work with $\widetilde{\mathcal{E}}$.

---

### §3.2 Lemma L2 — Σ_degen is Real Algebraic Subvariety

**Lemma L2**. $\Sigma_{\mathrm{degen}}$ is a *real algebraic subvariety* (Zariski-closed in the polynomial sense) of $\mathbb{R}^4 \times \mathbb{R}^n$, intersected with the open semialgebraic set $\mathbb{R}^4_{>0} \times \mathrm{int}(\Sigma_m) \cap \{a_{\mathrm{cl}} \in (0, 4/\lambda_n(L))\}$.

**Proof (CoT)**.

*CoT step 1 — Equation count*. $\Sigma_{\mathrm{degen}}$ is defined by:
- $(n-1)$ polynomial equations: $\bigl(\nabla_{\Sigma_m}\widetilde{\mathcal{E}}\bigr)_i = 0$ for $i = 1, \ldots, n-1$ (projection onto $T_u\Sigma_m$; one constraint is absorbed by $\mathbf{1}^\top u = m$);
- 1 polynomial equation: $\det\bigl(\mathrm{Hess}_{\Sigma_m}\widetilde{\mathcal{E}}\bigr) = 0$, where the projected Hessian on $T_u\Sigma_m$ is an $(n-1)\times(n-1)$ matrix.

Total: $n$ polynomial equations.

*CoT step 2 — Polynomial form of gradient*. By L1, $\widetilde{\mathcal{E}}$ is polynomial in $u$ of degree $\leq 4$. Hence $\nabla_u \widetilde{\mathcal{E}}$ is polynomial of degree $\leq 3$ in $u$. The projector $P_\Sigma := \mathrm{Id} - \frac{1}{n}\mathbf{1}\mathbf{1}^\top$ onto $T_u\Sigma_m$ is *constant linear*. Hence $\nabla_{\Sigma_m}\widetilde{\mathcal{E}} = P_\Sigma \nabla_u \widetilde{\mathcal{E}}$ is polynomial in $(\Theta, u)$.

*CoT step 3 — Polynomial form of Hessian determinant*. $\mathrm{Hess}_u \widetilde{\mathcal{E}}$ is polynomial of degree $\leq 2$ in $u$, linear in $\Theta$. Projection to $T_u\Sigma_m$ via $P_\Sigma$ (bilateral conjugation) preserves polynomial structure. The determinant of an $(n-1) \times (n-1)$ polynomial matrix is itself polynomial, of degree $\leq 2(n-1)$ in $u$ and $\leq n-1$ in $\Theta$ (multilinear expansion).

*CoT step 4 — Real algebraic conclusion*. $\Sigma_{\mathrm{degen}}$ is the common zero locus of $n$ polynomial equations in $\mathbb{R}^{n+4}$ (variables: $u \in \mathbb{R}^n$ plus $\Theta \in \mathbb{R}^4$). By definition (BCR §2.1), this is a *real algebraic subvariety* — closed in Zariski topology of $\mathbb{R}^{n+4}$.

Restriction to the open semialgebraic set $\{\Theta_i > 0\} \cap \mathrm{int}(\Sigma_m) \cap \{a_{\mathrm{cl}} < 4/\lambda_n(L)\}$ keeps it *semialgebraic* (intersection of algebraic + open semialgebraic = semialgebraic; BCR §2.2). □

**CoC anchors**:
- BCR Chapter 2 (semialgebraic sets, real algebraic subvarieties).
- E1 §3 (Tarski-Seidenberg setup).
- canonical SB7 (Σ_Hess polynomial form, L2495 — local on uniform sheet, this lemma global).

---

### §3.3 Lemma L3 — Generic Jacobian Rank = n (KEY GAP)

**Lemma L3 (KEY)**. On a *Zariski-open dense subset* of $\Sigma_{\mathrm{degen}}$, the Jacobian matrix
$$J(\Theta, u) := \begin{bmatrix} \dfrac{\partial \bigl(\nabla_{\Sigma_m}\widetilde{\mathcal{E}}\bigr)_i}{\partial(\Theta, u)} \\[1ex] \dfrac{\partial \bigl(\det\mathrm{Hess}_{\Sigma_m}\widetilde{\mathcal{E}}\bigr)}{\partial(\Theta, u)} \end{bmatrix} \in \mathbb{R}^{n \times (n+3)}$$
has rank $n$.

*Note on dimension count*: $\partial / \partial(\Theta, u)$ is a derivative w.r.t. *intrinsic* coordinates — $\Theta$ contributes 4 columns, $u$ on $\Sigma_m$ contributes $n-1$ columns (mass constraint absorbed). Total columns: $n+3$. Total rows: $n-1$ (gradient) $+ 1$ (Hess det) $= n$.

**Proof attempt (CoT)**.

This lemma is the *core remaining gap* (E1 §8 Step 2). Decompose into three sub-steps.

#### §3.3.1 Sub-step 1 — Gradient rows are independent (TRIVIAL)

*Claim 1*. The first $n-1$ rows of $J$ — i.e., partials of $\bigl(\nabla_{\Sigma_m}\widetilde{\mathcal{E}}\bigr)_i$ — are linearly independent on the Zariski-open subset of $\Sigma_{\mathrm{degen}}$ where $\nabla_{\Sigma_m}\widetilde{\mathcal{E}}$ is non-singular.

*Argument*. The block $\frac{\partial \nabla_{\Sigma_m}\widetilde{\mathcal{E}}}{\partial u}\vert _{T_u\Sigma_m}$ is *precisely* the projected Hessian $\mathrm{Hess}_{\Sigma_m}\widetilde{\mathcal{E}}$, an $(n-1) \times (n-1)$ matrix. The first $n-1$ rows of $J$ contain this $(n-1) \times (n-1)$ block (under $\partial/\partial u$ columns) plus $(n-1) \times 4$ block (under $\partial/\partial\Theta$).

Linear independence of the $n-1$ rows fails iff this $(n-1) \times (n+3)$ submatrix has rank $< n-1$. But on $\Sigma_{\mathrm{degen}}$ we *only* know $\det\mathrm{Hess}_{\Sigma_m}\widetilde{\mathcal{E}} = 0$ — this means the *$u$-block* alone can have rank $< n-1$; however the full $(n-1)\times(n+3)$ matrix has *extra columns* from $\partial/\partial\Theta$.

*Key observation*. The $\Theta$-block is
$$\frac{\partial \nabla_{\Sigma_m}\widetilde{\mathcal{E}}}{\partial\Theta} = P_\Sigma \cdot \frac{\partial \nabla_u \widetilde{\mathcal{E}}}{\partial\Theta}.$$
By L1, $\widetilde{\mathcal{E}}$ is *linear* in each $\Theta_j$ (multilinear, hence linear coordinate-wise). Hence
$$\frac{\partial \nabla_u \widetilde{\mathcal{E}}}{\partial \Theta_j} = \nabla_u \widetilde{\mathcal{E}}^{(j)}, \quad \text{where } \widetilde{\mathcal{E}}^{(j)} = \text{the $\Theta_j$-coefficient polynomial}.$$
These four vectors $\{\nabla_u \widetilde{\mathcal{E}}^{(j)}\}_{j=1}^4$ are the *gradients of the four energy components*: $\nabla\mathcal{E}_{\mathrm{cl}}$, $\nabla\mathcal{E}_{\mathrm{sep}}$, $\nabla\mathcal{E}_{\mathrm{bd}}^{\mathrm{Dir}}$, $\nabla\mathcal{E}_{\mathrm{bd}}^{\mathrm{DW}}$ (after $\Sigma_m$-projection and resolvent clearing).

*Linear independence of these 4 gradient vectors*: at a generic $u \in \Sigma_m$, these are:
- $\nabla\mathcal{E}_{\mathrm{cl}}$: spectral-weighted (resolvent-based);
- $\nabla\mathcal{E}_{\mathrm{sep}}$: linear $D = $ degree-distinction (graph-fixed direction in $\mathbb{R}^n$);
- $\nabla\mathcal{E}_{\mathrm{bd}}^{\mathrm{Dir}} = 4\alpha L u$ (Laplacian image);
- $\nabla\mathcal{E}_{\mathrm{bd}}^{\mathrm{DW}}_i = 2u_i(1-u_i)(1-2u_i)$ (per-vertex cubic).

These four vectors span a generic 4-dim subspace of $T_u\Sigma_m$ (provided $n-1 \geq 4$, i.e., $n \geq 5$; for $n \leq 4$ trivially). The cubic per-vertex form $W'(u_i)$ has *no algebraic relation* with the linear-in-$u$ forms $Lu$ and the constant $D$, except at *isolated* $u$ configurations (set of codim ≥ 1 in $\Sigma_m$).

*Sub-step 1 verdict*. The gradient rows of $J$ are linearly independent generically on $\Sigma_{\mathrm{degen}}$, modulo a codim-≥-1 sub-locus where the four component gradients become coplanar.

#### §3.3.2 Sub-step 2 — Hess-det row independent from gradient rows (KEY GAP)

*Claim 2*. The last row of $J$ — i.e., $\partial(\det\mathrm{Hess}_{\Sigma_m}\widetilde{\mathcal{E}})/\partial(\Theta, u)$ — is *not* in the linear span of the first $n-1$ gradient rows, on a Zariski-open dense subset of $\Sigma_{\mathrm{degen}}$.

*Proof attempt*.

By Jacobi's formula:
$$\frac{\partial \det H}{\partial \Theta_j} = \det H \cdot \mathrm{tr}\bigl(H^{-1} \tfrac{\partial H}{\partial \Theta_j}\bigr) \;\;\xrightarrow{\det H = 0}\;\; \frac{\partial \det H}{\partial \Theta_j} = \mathrm{tr}\bigl(\mathrm{adj}(H) \cdot \tfrac{\partial H}{\partial \Theta_j}\bigr),$$
where $\mathrm{adj}(H)$ is the classical adjugate (cofactor matrix transpose). When $\det H = 0$ with rank-deficiency exactly 1 (simple zero eigenvalue, *generic* on $\Sigma_{\mathrm{degen}}$), $\mathrm{adj}(H) = \xi \eta^\top$ (rank-1) for left/right null vectors $\xi, \eta$ of $H$.

Thus:
$$\frac{\partial \det H}{\partial \Theta_j}\bigg\vert_{\Sigma_{\mathrm{degen}}} = \xi^\top \frac{\partial H}{\partial\Theta_j}\, \eta.$$

Since $H$ is symmetric, $\xi = \eta$. So:
$$\frac{\partial \det H}{\partial \Theta_j}\bigg\vert_{\Sigma_{\mathrm{degen}}} = \xi^\top \cdot H^{(j)}\, \xi, \quad H^{(j)} := \frac{\partial H}{\partial\Theta_j} = \mathrm{Hess}_{\Sigma_m}\widetilde{\mathcal{E}}^{(j)},$$
the Hessian of the $j$-th energy component.

For the row to be *independent* from the gradient rows under $\partial/\partial\Theta$, we need the 4-vector
$$\bigl(\xi^\top H^{(1)}\xi,\, \xi^\top H^{(2)}\xi,\, \xi^\top H^{(3)}\xi,\, \xi^\top H^{(4)}\xi\bigr) \in \mathbb{R}^4$$
to *not lie* in the span of the four rows of $\partial(\nabla\widetilde{\mathcal{E}})/\partial\Theta$ at $(\Theta, u)$.

The gradient $\partial(\nabla \widetilde{\mathcal{E}})/\partial\Theta$ block is the $(n-1) \times 4$ matrix whose $j$-th column is $\nabla \widetilde{\mathcal{E}}^{(j)} \in T_u\Sigma_m$. The 4-vector $\xi^\top H^{(j)}\xi$ is a *quadratic form evaluated on $\xi$*, while the gradient columns are *linear forms* in the energy.

*Generic independence argument*. The map
$$\psi: T_u\Sigma_m \setminus \{0\} \to \mathbb{R}^4, \quad \xi \mapsto (\xi^\top H^{(j)}\xi)_{j=1}^4$$
is *quadratic* in $\xi$. Generic $\xi$ (the null direction of $H$) produces a 4-vector whose 4 coordinates are *algebraically independent quadratic forms* (since $H^{(1)} = \mathrm{Hess}\mathcal{E}_{\mathrm{cl}}$, ..., $H^{(4)} = \mathrm{Hess}\mathcal{E}_{\mathrm{bd}}^{\mathrm{DW}}$ are *four functionally independent quadratic forms* on $T_u\Sigma_m$ — recall:
- $H^{(1)}$ involves $\mathrm{Id} - P_{\mathrm{cl}}$ (resolvent-spectral);
- $H^{(2)} = 0$ (since $\mathcal{E}_{\mathrm{sep}}$ is linear in $u$, Hessian vanishes!);
- $H^{(3)} = 4L$ (Laplacian, factor 4 per CLAUDE.md "Critical Implementation Details");
- $H^{(4)} = \mathrm{diag}(W''(u_i)) = \mathrm{diag}(2(1 - 6u_i + 6u_i^2))$ (per-vertex).

**CRITICAL OBSERVATION**: $H^{(2)} = 0$! The separation Hessian vanishes because $\mathcal{E}_{\mathrm{sep}}\vert _{\Sigma_m}$ is *linear* in $u$ (L1 step 2). This forces $\xi^\top H^{(2)}\xi = 0$ for *all* $\xi$ — a *non-trivial structural dependence*.

This means the 4-vector $(\xi^\top H^{(j)}\xi)_j$ always has a *zero $j=2$ component*. The corresponding column in the gradient-rows $\Theta$-block is $\nabla\mathcal{E}_{\mathrm{sep}} = -\tfrac{1}{m} D$ — *non-zero* generically.

*Refined claim*. The last row's $\Theta$-block is $(\xi^\top H^{(1)}\xi, 0, \xi^\top H^{(3)}\xi, \xi^\top H^{(4)}\xi)$. The gradient-rows' $\Theta$-block is the $(n-1) \times 4$ matrix $[\nabla\mathcal{E}_{\mathrm{cl}}, \nabla\mathcal{E}_{\mathrm{sep}}, \nabla\mathcal{E}_{\mathrm{bd}}^{\mathrm{Dir}}, \nabla\mathcal{E}_{\mathrm{bd}}^{\mathrm{DW}}]$.

Linear independence of the last row from the span of the first $n-1$ rows (Sub-step 2) holds if there exists $c_0 \in \mathbb{R}$ and $\mathbf{c} \in \mathbb{R}^{n-1}$ with $(\mathbf{c}, c_0) \neq 0$ such that
$$c_0 \cdot (\xi^\top H^{(1)}\xi, 0, \xi^\top H^{(3)}\xi, \xi^\top H^{(4)}\xi) + \mathbf{c}^\top [\nabla\mathcal{E}_{\mathrm{cl}}, \nabla\mathcal{E}_{\mathrm{sep}}, \nabla\mathcal{E}_{\mathrm{bd}}^{\mathrm{Dir}}, \nabla\mathcal{E}_{\mathrm{bd}}^{\mathrm{DW}}] = 0.$$

The $j=2$ component gives $\mathbf{c}^\top \nabla\mathcal{E}_{\mathrm{sep}} = 0$, i.e., $\mathbf{c}$ is *orthogonal* to the (fixed) graph-determined direction $D \in T_u\Sigma_m$. This is a codim-1 condition on $\mathbf{c}$ — does *not* force $\mathbf{c} = 0$.

*Further constraints*. Combining $j = 1, 3, 4$ with $c_0$ degree of freedom yields a system of 3 linear equations in the $(n-1) + 1$ unknowns $(\mathbf{c}, c_0)$. For *generic* $(\Theta, u, \xi) \in \Sigma_{\mathrm{degen}}$, the coefficient matrix has full row rank 3 — leaving a $(n-3)$-dim solution space (non-trivial for $n \geq 4$).

**This shows the last row of $J$ is generically *dependent* on the gradient rows under $\partial/\partial\Theta$ alone!**

*Saving grace — $\partial/\partial u$ block*. The above analysis only used the *$\Theta$-block* (4 columns). The full row of $J$ has *additional $(n-1)$ columns* from $\partial/\partial u$. We need to examine whether the $\partial/\partial u$ block of the last row $\partial(\det H)/\partial u_k$ is in the span of the *$\partial/\partial u$ blocks* of gradient rows under the same coefficients $(\mathbf{c}, c_0)$.

By Jacobi:
$$\frac{\partial \det H}{\partial u_k}\bigg\vert_{\Sigma_{\mathrm{degen}}} = \xi^\top \frac{\partial H}{\partial u_k} \xi = 2 \sum_{i} \xi_i \frac{\partial^2 \mathcal{E}_\Theta}{\partial u_i \partial u_k}\bigg\vert_{\mathrm{partial}} \cdot \xi_i = \xi^\top T_k \xi,$$
where $T_k := \partial H / \partial u_k$ is the third-derivative tensor sliced at index $k$. By L1, $\widetilde{\mathcal{E}}$ has degree $\leq 4$ in $u$ — so third derivative is *linear in $u$*, generically non-zero.

The gradient rows' $\partial/\partial u$ block is *precisely* $H = \mathrm{Hess}_{\Sigma_m}\widetilde{\mathcal{E}}$ (the $(n-1) \times (n-1)$ projected Hessian).

We need $\xi^\top T_k \xi$ (last row, $u$-block, $k$-th column) to *not* equal $\mathbf{c}^\top H_{\cdot k}$ (gradient rows' $u$-block) for $\mathbf{c}$ satisfying the $\Theta$-block constraints.

**This is the *real* Sub-step 2 gap.** Honest assessment: the bilinear structure $(\Theta, u) \mapsto \widetilde{\mathcal{E}}$ is *favorable* but does *not immediately* yield generic linear independence. The argument requires:

> *Conjectured fact (W9+ symbolic verification)*: For *generic* graph $G$ and generic $u^* \in \Sigma_{\mathrm{degen}}$, the bilinear form $(\xi, \eta) \mapsto \xi^\top T_k \xi$ at the null vector $\xi$ of $H$ has *no global linear relation* with the projected Hessian rows. Equivalently: the *third-order Taylor coefficient* of $\widetilde{\mathcal{E}}$ along $\xi$ is non-zero generically — i.e., the Morse singularity at $u^*$ is a *non-degenerate fold* (not a cusp).

*This conjecture is exactly canonical SN3's (SN-iii)(SN-iv) genericity condition, currently OP-OMS-033b OPEN!*

#### §3.3.3 Sub-step 3 — Combine Sub-steps 1+2

*If* Sub-step 2 holds on a Zariski-open dense subset of $\Sigma_{\mathrm{degen}}$, *then* combined with Sub-step 1, $J$ has rank $n$ on a Zariski-open dense subset of $\Sigma_{\mathrm{degen}}$ — i.e., generic Jacobian rank $= n$.

**Honest failure mode** (Silent failure policy 0): if Sub-step 2 fails — i.e., the third-order Taylor coefficient *vanishes globally* on $\Sigma_{\mathrm{degen}}$ — then the Hess-det row is *redundant*, and $\Sigma_{\mathrm{degen}}$ may have higher-than-expected algebraic dimension. The codim ≥ 1 statement degrades to codim ≥ 0 (vacuous).

**Worst-case scenario**: if SCC has a *hidden integrability* (e.g., the four energy components satisfy an algebraic syzygy at all $u$), the dimension count fails entirely. This is *unlikely* for generic graphs (canonical SCC convention) but requires verification.

**Recovery via Approach C (Federer)**. Even if Sub-step 2 fails for *algebraic* codim ≥ 1, the *Lebesgue* measure-zero version (Sard direct) still holds (L2 in 02_H5 §2.2, which uses *only* polynomial form, no rank statement). Thus Cat A *measure-zero version* is safe; Cat A *algebraic codim* requires Sub-step 2.

### §3.4 Lemma L4 — Σ_degen Dimension ≤ 3

**Lemma L4**. Conditional on Lemma L3 (generic rank $n$ of $J$): $\dim_{\mathbb{R}}\Sigma_{\mathrm{degen}} \leq 3$.

**Proof (CoT)**.

*CoT step 1 — Local manifold structure*. By L3, on the Zariski-open dense subset $\Sigma_{\mathrm{degen}}^{\mathrm{reg}} \subset \Sigma_{\mathrm{degen}}$ where $J$ has full row rank $n$, the implicit function theorem yields: $\Sigma_{\mathrm{degen}}^{\mathrm{reg}}$ is a smooth submanifold of $\mathbb{R}^4_{>0} \times \mathrm{int}(\Sigma_m)$ of dimension
$$\dim = (n + 3) - n = 3.$$

*CoT step 2 — Singular part has lower dim*. The complement $\Sigma_{\mathrm{degen}} \setminus \Sigma_{\mathrm{degen}}^{\mathrm{reg}}$ is itself algebraic (defined by rank $< n$ minor conditions on $J$), and has dimension $\leq 3 - 1 = 2$ (Whitney stratification, §4 below; BCR §9).

*CoT step 3 — Global dimension*. $\dim \Sigma_{\mathrm{degen}} = \max(\dim \Sigma_{\mathrm{degen}}^{\mathrm{reg}}, \dim \text{singular part}) = 3$.

*CoT step 4 — Non-emptiness*. By canonical V5b-T-zero (Cat A, L1328): on translation-invariant graphs, the uniform sheet $u^* = c\mathbf{1}$ has exact zero Goldstone eigenvalue — so $\Sigma_{\mathrm{degen}}$ is *non-empty* (the V5b-T-zero locus is in it). Thus $\dim \Sigma_{\mathrm{degen}} \geq 0$ (and indeed contains the entire spinodal hypersurface $\Sigma_{T8}$ of dim 3, consistent). □

**CoC anchors**:
- canonical V5b-T-zero (Cat A, L1328) — non-emptiness of $\Sigma_{\mathrm{degen}}$, dimension lower bound.
- canonical SB7 (Cat A, L2495) — $\Sigma_{\mathrm{Hess}} = \Sigma_{T8}$ on uniform sheet, dimension 3 confirmed.
- Whitney 1957 / BCR Chapter 9 (stratification of real algebraic).
- IFT (Standard differential topology, e.g., Lee *Smooth Manifolds*).

---

### §3.5 Lemma L5 — Tarski-Seidenberg Projection Preserves Semialgebraic Dimension

**Lemma L5**. Conditional on Lemma L4: $\dim_{\mathbb{R}}\bigl(\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}})\bigr) \leq 3$.

**Proof (CoT)**.

*CoT step 1 — Tarski-Seidenberg*. $\Sigma_{\mathrm{degen}}$ is semialgebraic (L2). The projection $\mathrm{proj}_\Theta: \mathbb{R}^4_{>0} \times \Sigma_m \to \mathbb{R}^4_{>0}$ is a polynomial map. By the Tarski-Seidenberg theorem (BCR Theorem 2.2.1 or 1.4.2), the image $\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}})$ is semialgebraic.

*CoT step 2 — Dimension non-increase*. BCR Theorem 2.8.8 (or Theorem 5.3.6 for the closed-image version): for a semialgebraic map $f: S \to T$ between semialgebraic sets, $\dim f(S) \leq \dim S$. Applied here:
$$\dim_{\mathbb{R}}\bigl(\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}})\bigr) \leq \dim_{\mathbb{R}} \Sigma_{\mathrm{degen}} \leq 3.$$

*CoT step 3 — Codim conclusion*. $\dim_{\mathbb{R}}(\mathbb{R}^4_{>0}) = 4$, hence
$$\mathrm{codim}_{\mathbb{R}}\bigl(\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}}); \mathbb{R}^4_{>0}\bigr) \geq 1.$$ □

**CoC anchors**:
- BCR Theorem 2.2.1 (Tarski-Seidenberg semialgebraicity preservation).
- BCR Theorem 2.8.8 (dimension non-increase under projection).
- E1 §3 (Tarski-Seidenberg setup confirmed).

---

### §3.6 Theorem (Synthesis)

**Theorem (OP-H5-α, Cat A conditional on L3 Sub-step 2)**.
$$\boxed{\;\mathrm{codim}_{\mathbb{R}}\bigl(\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}}); \mathbb{R}^4_{>0}\bigr) \geq 1, \quad \text{hence } \mathcal{D}_{\mathrm{Morse}}(G, m) = \mathbb{R}^4_{>0} \setminus \mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}}) \text{ is Zariski-open dense.}\;}$$

**Proof**. L1 (polynomial form) + L2 ($\Sigma_{\mathrm{degen}}$ real algebraic semialgebraic) + L3 (generic Jacobian rank $n$, conditional on Sub-step 2) + L4 ($\dim \Sigma_{\mathrm{degen}} \leq 3$) + L5 (Tarski-Seidenberg dim preservation) → $\dim \mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}}) \leq 3 < 4 = \dim \mathbb{R}^4_{>0}$ → codim ≥ 1. □

**Cat A conditionality**: This proof is *Cat A modulo Sub-step 2*. Without Sub-step 2 verification, the dimension bound $\dim \Sigma_{\mathrm{degen}} \leq 3$ degrades to $\dim \Sigma_{\mathrm{degen}} \leq 4$ (vacuous), and the conclusion weakens to *Lebesgue measure zero* (via Sard direct on the polynomial map — Cat A unconditional version, E1 §1 / 02_H5 §2.2 L2).

---

## §4 Approach B (Hironaka Resolution) — Alternative Authority Anchor

### §4.1 Hironaka 1964 Statement

**Hironaka 1964** (*Annals of Math* 79, 109-203 + 205-326): For any algebraic variety $X$ over a field of characteristic 0, there exists a smooth variety $\widetilde{X}$ and a proper birational morphism $\pi: \widetilde{X} \to X$ which is an isomorphism over the smooth locus of $X$, and the singular locus is replaced by a normal-crossings divisor.

**Embedded version** (used in §4.2): for $X \subset Y$ smooth ambient, there exists a *blow-up sequence* of smooth centers such that the strict transform of $X$ in the blown-up $\widetilde{Y}$ is smooth, and the exceptional divisor has normal crossings.

### §4.2 Application to Σ_degen

**Complexification**. Let $\Sigma_{\mathrm{degen}}^{\mathbb{C}} := V(\nabla \widetilde{\mathcal{E}}, \det H_{\Sigma_m}) \subset \mathbb{C}^{n+4}$ — the complex algebraic variety defined by the same polynomial equations.

**Hironaka resolution** $\pi: \widetilde{V} \to \Sigma_{\mathrm{degen}}^{\mathbb{C}}$ exists. The dimension of $\widetilde{V}$ equals $\dim_{\mathbb{C}} \Sigma_{\mathrm{degen}}^{\mathbb{C}}$. Generic-rank arguments on $\widetilde{V}$ are equivalent to those on $\Sigma_{\mathrm{degen}}^{\mathbb{C}}$, just on a *smooth* model.

**Projection** $\mathrm{proj}_\Theta^{\mathbb{C}} \circ \pi: \widetilde{V} \to \mathbb{C}^4$ is a *smooth morphism* of smooth varieties. Classical *generic fiber dimension* (Chevalley's theorem): if $\mathrm{proj}_\Theta^{\mathbb{C}}$ has generic fiber of dimension $d$, then $\dim \mathrm{Image} \leq \dim \widetilde{V} - d$ (modulo birational adjustments).

### §4.3 Why Secondary

**Issue 1 — real vs complex**. Hironaka 의 원본은 *complex* (char 0 algebraic geometry). Real reduction:
- Bierstone-Milman 1988: canonical desingularization works in real-analytic category;
- but the *real* image may be a strict subset of the *complex* image projected to $\mathbb{R}^4 \subset \mathbb{C}^4$.

Approach A (Tarski-Seidenberg on *real* semialgebraic) sidesteps this entirely.

**Issue 2 — overkill**. Hironaka resolution is *sufficient* (desingularization) but not *necessary* — for dimension count alone, BCR's semialgebraic dim theory is direct.

**Role in this attempt**: *Citation authority* — "polynomial system's singular set is algebraic" is *standard* (Hironaka and predecessors). Used in §1.1 Claim (1) justification implicitly.

---

## §5 Approach C (Federer Sard Finite-Codim) — Limit

### §5.1 Federer 1969 Finite-Codimensional Sard

**Federer 1969** (*Geometric Measure Theory*, §3.4): For a polynomial map $f: \mathbb{R}^N \to \mathbb{R}^M$, the *critical set* $C(f) := \{x : \mathrm{rank}\, df_x < M\}$ has image $f(C(f)) \subset \mathbb{R}^M$ with *Hausdorff dimension* $\leq M - 1$ (codim ≥ 1 in Hausdorff sense), assuming $N \geq M$.

**Applied to SCC**: take $N = n+3$, $M = 4$ (projection $\mathrm{proj}_\Theta$ from $\Sigma_{\mathrm{degen}}$). Then Hausdorff-dim of $\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}}) \leq 3$.

### §5.2 Why Secondary

**Issue — codim notion mismatch**. Federer's codim is *Hausdorff dimensional* (measure-theoretic). The canonical *Zariski-codim ≥ 1* statement requires *algebraic* containment in a positive-codim subvariety — strictly stronger.

For semialgebraic sets, *Hausdorff dim* $=$ *algebraic dim* (BCR §2.8.4) — so the two are *equivalent* in this setting. Hence Approach C *suffices* for the Cat A measure-theoretic conclusion, but the *algebraic* upgrade requires noting this equivalence explicitly (BCR §2.8).

**Role in this attempt**: *Lebesgue-only fallback* — if Approach A Sub-step 2 fails, Approach C still gives Lebesgue null + Hausdorff codim ≥ 1, hence *some* Cat A version (matching T-PERSIST-1B-UNCONDITIONAL Sard precedent).

---

## §6 Counterexample Attempts (≥3 Explicit)

### §6.1 Attempt 1 — $\mathcal{F}_M(G)$ Boundary Degeneracy ($u_i = 0$ or $u_i = 1$ Extreme)

**Setup**. Consider $u^* \in \partial\Sigma_m$ with some $u_i^* \in \{0, 1\}$. The double-well $W'(u_i^*) = 2u_i^*(1 - u_i^*)(1 - 2u_i^*)$ has special structure at extreme values: $W'(0) = 0$, $W'(1) = 0$ — so gradient is automatically zero in these coordinates. Hessian: $W''(0) = 2 \neq 0$, $W''(1) = 2 \neq 0$ — non-degenerate per-coordinate. *However*, the constraint $u_i \in [0,1]$ + KKT multipliers complicate Morse analysis.

**Failure mode**. The present theorem explicitly restricts to *interior* $\{u_i \in (0,1)\}$ of $\Sigma_m$ — boundary handled separately. Canonical L-BOUNDARY-MODE-EXCLUSION (Cat C, CV-1.16) registers boundary modes as separate concern. *Counterexample fails because outside the scope.*

### §6.2 Attempt 2 — $a_{\mathrm{cl}}$ Rational Pole at $a_{\mathrm{cl}} \to 4$

**Setup**. As $a_{\mathrm{cl}} \to 4/\lambda_n(L)$ (or in general, as $1 + a_{\mathrm{cl}}\lambda_k(L) \to 0$ for some $k$), the resolvent $(\mathrm{Id} + a_{\mathrm{cl}} L)^{-1}$ has a pole — clearing factor $\det(\mathrm{Id} + a_{\mathrm{cl}}L) \to 0$. The "polynomial form" $\widetilde{\mathcal{E}}$ degenerates.

**Failure mode**. Canonical $a_{\mathrm{cl}} < 4$ constraint (CLAUDE.md params.py) + spectral bound $\lambda_k(L) \leq \lambda_n(L)$ guarantee $1 + a_{\mathrm{cl}}\lambda_k > 0$ on the *open* parameter regime. The boundary $a_{\mathrm{cl}} = 4/\lambda_n$ is a *single hypersurface* in $\Theta$-space — codim 1 in $\mathbb{R}^4_{>0}$. Even if codim ≥ 1 of $\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}})$ should *include* this hypersurface, it doesn't reduce the codim claim (codim is bounded below by 1, can be exactly 1 here). *Counterexample fails — it merely identifies one component of the codim-1 locus.*

### §6.3 Attempt 3 — Graph $G$ with $\lambda_2 = 0$ (Disconnected)

**Setup**. If $G$ is disconnected, $\lambda_2(L) = 0$ — Goldstone direction (uniform on each connected component) gives zero eigenvalue at *every* uniform critical point. $\Sigma_{\mathrm{degen}}$ contains entire $\Theta$-fibers (codim 0 in $\Theta$-projection).

**Failure mode**. Canonical SCC framework (CLAUDE.md "Theory Sketch") assumes *finite connected graph* — disconnected case is *outside* canonical scope. The fundamental SCC convention (operators.py, params.py, energy.py) explicitly requires $\lambda_2 > 0$.

*Counterexample fails because outside canonical convention.* In the connected case, $\lambda_2 > 0$ is guaranteed (Fiedler 1973), and the present theorem applies.

**Note**: this counterexample is *informative* — it shows the theorem's *hypothesis* (connected $G$) is essential, not merely convenient.

---

## §7 Cat Self-Classification + Honest Assessment

### §7.1 Cat A *Conditional* on Lemma L3 Sub-step 2

**Verdict**: **Cat A conditional on Lemma L3 Sub-step 2** (i.e., the third-order Taylor coefficient at null direction $\xi$ is non-degenerate generically on $\Sigma_{\mathrm{degen}}$).

**Reasoning**:
- L1, L2, L4, L5 are *Cat A unconditional* (standard polynomial algebra + Tarski-Seidenberg + BCR dimension theory).
- L3 Sub-step 1 (gradient rows independent) is *Cat A* via canonical SB7-style argument.
- L3 Sub-step 2 (Hess-det row independent of gradient rows) is *Cat B sketch* — requires symbolic verification.
- L3 Sub-step 3 follows from Sub-steps 1 + 2.

### §7.2 Sub-step 2 Failure Possibility

*If Sub-step 2 fails entirely* (third-order Taylor coefficient *identically zero* on $\Sigma_{\mathrm{degen}}$):
- $\Sigma_{\mathrm{degen}}$ could have dimension up to $4$ (one less codim from the Hess-det equation being redundant).
- $\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}})$ could have dimension up to $4$ — *codim ≥ 1 violated*.
- Cat A *algebraic codim* claim FAILS.

*If Sub-step 2 holds only outside a codim-1 sub-locus of $\Sigma_{\mathrm{degen}}$* (most likely scenario):
- $\Sigma_{\mathrm{degen}}$ has the expected dimension 3 generically.
- Cat A *algebraic codim* claim HOLDS on Zariski-open dense subset.

### §7.3 Honest Assessment

**The L3 Sub-step 2 gap is a *real* mathematical gap, not a notational issue.** It corresponds *precisely* to:
- The (SN-iii)+(SN-iv) genericity condition in canonical SN3 (Cat B conditional, L2501);
- OP-OMS-033b (OPEN).

Equivalently: the singular locus of SCC's variational problem is *generically* a *fold* (codim-1 simple saddle-node), not a higher-codim catastrophe (cusp, swallowtail, ...). This is a *plausible* but *unverified* conjecture about SCC's specific energy structure.

**Symbolic verification path** (W9+ recommended):
1. SymPy/Macaulay2: compute $\widetilde{\mathcal{E}}(\Theta, u)$ for small graph $G$ (e.g., $C_4$, $C_5$, $K_4$, $2 \times 2$ grid).
2. Compute $\Sigma_{\mathrm{degen}}$ as ideal in $\mathbb{R}[\Theta, u]$.
3. Compute Jacobian $J$ and check generic rank by Gröbner basis / minor analysis.
4. Specifically: verify that the rank-$n$ condition holds on a Zariski-open subset.

**Empirical verification path** (alternative):
1. Random sample $\Theta \in \mathbb{R}^4_{>0}$ via Monte Carlo;
2. Solve $\nabla \mathcal{E}_\Theta(u) = 0$ via optimizer (canonical `find_formation`);
3. Compute $\det H$ at each critical point;
4. Compute null vector $\xi$ when $\det H \approx 0$ and evaluate $\xi^\top T_k \xi$ for $k = 1, \ldots, n$;
5. Check non-degeneracy of resulting 4-vector statistically.

### §7.4 Forward Hook

**W9+ task list**:
- OP-H5-α-1: Lemma L3 Sub-step 2 의 symbolic verification (SymPy/Macaulay2, small graphs);
- OP-H5-α-2: combine with SN3 (SN-iii)(SN-iv) = OP-OMS-033b;
- OP-H5-α-3: extend Approach B (Hironaka) for *direct algebraic* version bypassing Sub-step 2.

After completing OP-H5-α-1 (W9+), present file's Cat A classification becomes *unconditional* — promotion path to canonical OP catalog entry as OP-H5-α (resolved Cat A).

---

## §8 Integration with Canonical

### §8.1 T-P-F-ε0-K (Cat B, L1818-1833) Cat A Path Prerequisite

**Canonical T-P-F-ε0-K**: Kramers Exponent Stability under Bernoulli Regularization. Status Cat B *conditional on (H5)* Morse stability. Cat A promotion path stated at L1833:
> "(i) prove H5 for $\mathcal{E}_{\mathrm{SCC}}$ saddles, (ii) establish spectral gap"

**Present theorem provides path (i)** in the *generic regime* sense: for $\Theta \in \mathcal{D}_{\mathrm{Morse}}(G, m)$ (Zariski-open dense), every critical point of $\mathcal{E}_\Theta$ is non-degenerate, in particular the saddle $\tilde{u}^*_{\mathrm{sad}}$ and minimum $\tilde{u}^*_{\mathrm{min}}$.

**Persistence under Bernoulli regularization**: as $\varepsilon \to 0$, the perturbed Hessian $\mathrm{Hess}(\mathcal{E} + \varepsilon R)$ converges to $\mathrm{Hess}\,\mathcal{E}$. Eigenvalue continuity (Kato 1995 *Perturbation Theory*) + invertibility persistence yields (H5) for small $\varepsilon$.

**Verdict**: T-P-F-ε0-K Cat A path (i) is *unlocked* on $\mathcal{D}_{\mathrm{Morse}} \cap \mathcal{R}_{\mathrm{post}}$ conditional on Sub-step 2. Combined with (ii) spectral gap (separate problem, canonical T-PF-A1-PE Cat A handles Poincaré inequality), full Cat A T-P-F-ε0-K on regime restriction is reachable.

### §8.2 02_H5 §5.2 (H5') Regime Restriction — Mathematical Backing

**02_H5 proposed amendment** (L237):
> *(H5')* Morse stability on $\mathcal{R}_{\mathrm{post}}$ stable basin: $\Theta \in \mathcal{R}_{\mathrm{post}}$ ... both $\tilde{u}^*_{\mathrm{sad}}, \tilde{u}^*_{\mathrm{min}} \in \mathcal{B}_{\mathrm{stable}}(\Theta)$ ... both non-degenerate critical points of $\mathcal{E}_{\mathrm{SCC}}+\varepsilon R$ for $\varepsilon \in [0, \varepsilon_0]$.

**Present theorem's contribution**: $\mathcal{D}_{\mathrm{Morse}}(G, m) \supset \mathbb{R}^4_{>0} \setminus \mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}})$ is Zariski-open dense; intersected with $\mathcal{R}_{\mathrm{post}} \cap \{\text{post-bifurcation stable basin condition}\}$, the Cat A promotion path is *mathematically substantiated*. Spinodal stratum $\Sigma_{T8}$ (codim-1 by SB7) is *separated* — outside the scope of (H5').

### §8.3 OP-H5-β (Equivariant Morse) + OP-H5-γ (Crandall-Rabinowitz) Relationship

**Three sub-OPs**:
- **OP-H5-α** (present file): Hironaka algebraic strengthening of *generic* Morse via Sard;
- **OP-H5-β**: Equivariant Morse on non-trivial $\mathrm{Aut}(G)$ subclass — V5b-T-zero generalization;
- **OP-H5-γ**: Crandall-Rabinowitz fold + (SN-iii)(SN-iv) — direct local analysis of saddle-node points.

**Relationships**:
- OP-H5-α + OP-H5-β are *complementary*: α handles generic graph (Aut trivial), β handles symmetric graph subclass (where α's "generic" set may be misleading due to orbit degeneracy).
- OP-H5-α and OP-H5-γ have *shared gap*: Sub-step 2 of α ≅ (SN-iii)+(SN-iv) of γ. Resolving either unlocks both.
- Joint resolution (OP-H5-α + β + γ) gives *unified Cat A* of (H5) for SCC on the canonical scope.

---

## §9 New Open Questions (≥3)

### §9.1 OP-H5-α-1: Lemma L3 Sub-step 2 Symbolic Verification

**Statement**: For finite connected graphs $G$ of small size ($n \leq 16$, e.g., $C_n$, $K_n$, $T^2_n$, $K_{n,n}$), verify via SymPy/Macaulay2 that the bilinear form $(\xi, k) \mapsto \xi^\top T_k \xi$ on $\Sigma_{\mathrm{degen}}$ has *generically non-trivial* span over $k$ (third-order Taylor coefficient non-degenerate).

**Approach**:
1. Construct $\widetilde{\mathcal{E}}(\Theta, u)$ explicitly for small $G$;
2. Compute ideal $I := \langle \nabla \widetilde{\mathcal{E}}, \det H \rangle \subset \mathbb{R}[\Theta, u]$;
3. Compute $V(I)$ (Gröbner basis);
4. On $V(I)$, compute null vector $\xi$ of $H$ symbolically;
5. Compute 4-vector $(\xi^\top H^{(j)}\xi)_{j=1}^4$ and $n$-vector $(\xi^\top T_k \xi)_{k=1}^n$;
6. Check linear independence from gradient rows.

**Expected outcome**: confirm Cat A unconditionally for these small graphs; extrapolate to generic.

**Estimated effort**: 2-3 days W9+.

### §9.2 OP-H5-α-2: Graph $G$ Class-Specific Generic Spectrum Behavior

**Statement**: Characterize the graph classes where $\mathcal{D}_{\mathrm{Morse}}(G, m)$ has *measure zero* (i.e., theorem vacuous). Conjectured candidates:
- Multipartite $K_{n_1, n_2, \ldots, n_k}$ with $\sum n_i = n$, $\max n_i \geq n/2$: high spectral degeneracy may force $\Sigma_{\mathrm{degen}}$ to contain $\Theta$-hyperplanes;
- Hypercube $Q_d$: $L$ eigenvalues $\{2k\}_{k=0}^d$ with multiplicity $\binom{d}{k}$ — possible Goldstone-mode multiplicity issues;
- Cycle $C_n$ for $n$ even: $\mathbb{Z}_2$ symmetry already covered by V5b-T-zero.

**Approach**: case analysis + numerical sampling.

**Estimated effort**: 1-2 weeks W10+.

### §9.3 OP-H5-α-3: $a_{\mathrm{cl}}$ Rational Dependency — Embedded Resolution

**Statement**: The clearing factor $\det(\mathrm{Id} + a_{\mathrm{cl}} L)$ introduces *polynomial* factors but *destroys* the natural $\Theta$-linearity of $\widetilde{\mathcal{E}}$. Investigate whether a *Hironaka embedded resolution* of the resolvent locus can restore "natural" $\Theta$-coordinates.

**Approach**:
1. Identify the *resolvent locus* $V(\det(\mathrm{Id}+a_{\mathrm{cl}}L))$ in $(\Theta, u)$-space;
2. Apply Hironaka's embedded resolution to get smooth ambient;
3. Compute $\Sigma_{\mathrm{degen}}$ in the resolved space — possibly *strictly* algebraic (no clearing needed);
4. Project back, compare to Approach A result.

**Estimated effort**: 1-2 weeks W11+ (Hironaka technical).

---

## §10 Summary + Self-Cat Verdict

**Main result**: Theorem (OP-H5-α) is *Cat A conditional on Lemma L3 Sub-step 2*; otherwise *Cat A unconditional* in Lebesgue measure-zero version (via Approach C / canonical T-PERSIST-1B-UNCONDITIONAL Sard precedent).

**Five lemmata**:
- L1 (polynomial structure): Cat A unconditional.
- L2 ($\Sigma_{\mathrm{degen}}$ semialgebraic): Cat A unconditional.
- L3 (generic Jacobian rank $n$): **Cat B sketch, Sub-step 2 gap**.
- L4 ($\dim \Sigma_{\mathrm{degen}} \leq 3$): Cat A conditional on L3.
- L5 (Tarski-Seidenberg dim preservation): Cat A unconditional.

**Three approaches**:
- A (Dim + T-S): primary, conditional Cat A.
- B (Hironaka): authority anchor, secondary.
- C (Federer): Lebesgue fallback, unconditional Cat A measure-version.

**Three counterexamples**: all *fail* (out of scope: boundary, pole, disconnected).

**Three new OPs**: OP-H5-α-1 (symbolic), OP-H5-α-2 (graph class), OP-H5-α-3 (resolvent).

**Verdict for canonical promotion**: *Not yet*. Requires OP-H5-α-1 resolution (W9+ symbolic verification, estimated 2-3 days). Until then, the theorem stands as *Cat A 후보 with explicit Sub-step 2 disclaimer* — same status as 02_H5 §2 P1 Sard sketch's L3, *but with detailed proof path identified*.

**§8a Archive Pattern P1-P6 self-check**: 0/6 hits (DECL-1.0 Q1/Q2 direct progress; no vocabulary refactoring; canonical content novel; external tools = canonical Sard precedent extension; xref complete §0; mathematical content separated from framing).

---

## §11 Cross-References + Forward Hooks

**Inputs**:
- E1: `/tmp/scc_proofs_v02/E1_hironaka_literature.md` (Phase 1 literature scan, 339L).
- 02_H5: `THEORY/logs/daily/2026-05-19/02_H5_morse_spinodal.md` §2 (L1-L5 sketch, 02_H5 L83-149).
- pre_brainstorm: `THEORY/logs/daily/2026-05-19/01_pre_brainstorm.md` §6.3 (Hironaka anchor, L397-408).

**Canonical anchors (untouched)**:
- canonical L1818-1833 (T-P-F-ε0-K Cat B, present theorem unlocks Cat A path).
- canonical L2495-2496 (SB7 Cat A, Σ_Hess = Σ_T8 codim-1; L5 reference).
- canonical L2501-2502 (SN3 Cat B conditional, Sub-step 2 ≅ (SN-iii)+(SN-iv)).
- canonical L1328 (V5b-T-zero Cat A definitional, L4 non-emptiness).
- canonical L2063 (T-PERSIST-1B-UNCONDITIONAL Cat A, Sard precedent).

**Forward (W9+ leading questions)**:
- OP-H5-α-1 (§9.1): symbolic Sub-step 2 verification — direct Cat A unconditional path.
- OP-H5-α-2 (§9.2): graph class characterization — scope refinement.
- OP-H5-α-3 (§9.3): Hironaka resolvent — alternative Cat A path bypassing Sub-step 2.

**Integration W9+**:
- OP-H5-α resolution → T-P-F-ε0-K Cat A on $\mathcal{R}_{\mathrm{post}} \cap \mathcal{D}_{\mathrm{Morse}}$ (regime-restricted, 02_H5 §5.2).
- Combined with OP-H5-β / OP-H5-γ → unified Cat A for (H5) on canonical scope.
- Combined with OP-0021 ($T_*$ axiomatic registration, 03_T_star) → P-F-A1 Package II conditional start.

---

*End of P1_OP-H5-alpha_Hironaka.md (Phase 2 D1 deliverable). Cat A conditional on Lemma L3 Sub-step 2. Honest assessment + symbolic verification path identified for W9+.*
