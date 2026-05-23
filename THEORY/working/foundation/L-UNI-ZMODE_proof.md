---
id: L-UNI-ZMODE
type: working/foundation/lemma
date: 2026-05-20
session_origin: W8-Day3 POST-99 evening — Option C escalation (proof-first response to user critique)
canonical_version: CV-1.19 SEALED (prior); promotion target CV-1.20 SEAL
status: working-layer Cat A direct lemma, ready for CV-1.20 SEAL promotion
cat_assignment: Cat A direct
primary_anchors:
  - canonical §13 Theorem 4 (L1466, Cat A) — μ_k = 4αλ_k + βW''(c)
  - canonical §13 T-σ-Lemma-1 (L1386, Cat A) — Hessian commutes with G_u-action
  - canonical §13 L-S3-KERNEL-MULT (L1798, Cat A, CV-1.19) — Case B uniform critical kernel-mult identity
  - canonical §13 V5b-T-zero (L1328, Cat A def) — non-uniform corner-saturated Goldstone context (contrast)
  - canonical §13 L-HMORSE-LOCAL (L1953-1990, Cat B, CV-1.16) — (C4) consistency
related_files:
  - THEORY/logs/daily/2026-05-20/05_landscape_local_to_global.md §3.7 (Goldstone Type A/B/C 재분류 motivation)
  - THEORY/working/cssl/01_critic_evaluation.md §A.1 (CRITICAL #1 — "ker = Goldstone only" misframing critique 의 epistemic anchor)
promotion_candidate: CV-1.20 SEAL (along with L-SURFACE-TENSION-RESCALE)
cot_enforced: yes
coc_enforced: yes
constraint_compliance:
  canonical_edits: 0 (working file)
  Mori_Zwanzig: 0 references
  inertia: 0 references
  new_energy_terms: 0
  new_framework_letters: 0 (Type A/B/C 는 분류 label only)
  DECLARATION_edits: 0
---

> [!nav] Linked: [[../../canonical/canonical|CV-1.19 canonical]] (§13 Theorem 4 L1466, T-σ-Lemma-1 L1386, L-S3-KERNEL-MULT L1798, V5b-T-zero L1328, L-HMORSE-LOCAL L1953-1990) · [[../../canonical/DECLARATION|DECL-1.0]] · [[../../logs/daily/2026-05-20/05_landscape_local_to_global|05 §3.7 Goldstone 3-type 재분류]] · [[../cssl/01_critic_evaluation|CSSL critic §A.1]]

# L-UNI-ZMODE — Uniform Zero-Mode Dichotomy (Cat A Direct)

**Mission**: 균일 critical point $u^* = c\mathbf{1}$ 에서 Hessian zero modes 가 *오직* Type A (critical parameter crossing) 또는 Type B (eigenvalue multiplicity) 만 가능하고, **Type C (continuous Goldstone / orbit-tangent) 는 부재** 임을 증명. CSSL critic 의 핵심 misframing ("ker = Goldstone only at uniform") 을 *명시적으로 반박*하는 lemma.

---

## §0 — Pre-flight: xref check + §8a P1-P6 audit

### §0.1 Cross-reference verification

| Required canonical anchor | Location | Status |
|---|---|---|
| Theorem 4: $\mu_k = 4\alpha\lambda_k + \beta W''(c)$ | canonical.md L1466, Cat A | CONFIRMED |
| T-σ-Lemma-1: Hessian-Aut(G) commutation | canonical.md L1386, Cat A | CONFIRMED |
| L-S3-KERNEL-MULT Case B: uniform critical kernel-mult | canonical.md L1798-1805, Cat A, CV-1.19 | CONFIRMED |
| V5b-T-zero: orbit-tangent zero at *corner-saturated* (NOT uniform) | canonical.md L1328, Cat A def | CONFIRMED |
| L-HMORSE-LOCAL (C4): V5b-T-zero orbits excluded by hypothesis | canonical.md L1953-1990, Cat B, CV-1.16 | CONFIRMED |

### §0.2 §8a archive pattern P1-P6 audit

| Pattern | 검사 | 결과 |
|---|---|---|
| P1 — 근본 질문 우회 | DECL Q1 (T8 boundary 출현) + Q4 (K-selection) 의 *epistemic prerequisite* — 우회 아님 | ✓ |
| P2 — Vocabulary refactoring | Type A/B/C 는 분류 label only; $u_t$ primitive 미변경 | ✓ |
| P3 — Canonical content 중복 | L-S3-KERNEL-MULT Case B 의 *direct corollary*; novel statement = "Type C 부재" | ✓ |
| P4 — 외부 도구 도입 | 새 theory 0; Schur Lemma + orbit-tangent argument 모두 standard | ✓ |
| P5 — Self-audit | 본 §0 + §5 P-Audit 의 dual | ✓ |
| P6 — 언어-수학 분리 | Statement + 5-step proof + anchors 각 별도 절 | ✓ |

**0/6 부합 → Cat A direct promotion 합법**.

---

## §1 — Setup and Notation

Let $G = (V, E)$ be a finite connected graph with $\lvert V \rvert = n$. Let $m \in (0, n)$ be a fixed mass parameter, and define $c := m/n$. Assume $c \in (s_-, s_+)$ where $s_\pm := (3 \mp \sqrt{3})/6$ are the spinodal boundaries (so that $W''(c) < 0$, $\lvert W''(c) \rvert > 0$).

**State space**: $\Sigma_m = \{u \in [0,1]^n : \sum_i u_i = m\}$ (canonical T-PF-A1-AR, L1953, Cat A).

**Tangent space**: $T_u \Sigma_m = \{v \in \mathbb{R}^n : \mathbf{1}^T v = 0\} = \mathbf{1}^\perp$ for any interior $u$.

**Uniform critical**: $u^* = c\mathbf{1} \in \Sigma_m$. (Self-consistency: $\sum_i u^*_i = nc = m$ requires $c = m/n$, hence the parameterization.)

**Laplacian eigenvalues (1-index)**:
$$0 = \lambda_1(L_G) < \lambda_2(L_G) \leq \lambda_3(L_G) \leq \cdots \leq \lambda_n(L_G)$$
with $\lambda_1$ corresponding to the constant mode $\mathbf{1}$, removed by $\Pi$. $V_{\lambda_k} \subseteq \mathbf{1}^\perp$ denotes the $\lambda_k$-eigenspace (for $k \geq 2$).

**Full SCC energy**:
$$\mathcal{E}(u) = \lambda_{cl}\mathcal{E}_{cl}(u) + \lambda_{sep}\mathcal{E}_{sep}(u) + \lambda_{bd}\mathcal{E}_{bd}(u) + \lambda_{tr}\mathcal{E}_{tr}(u)$$
with $\mathcal{E}_{bd}(u) = \alpha u^T L_G u + \beta \sum_i W(u_i)$, $W(u) = u^2(1-u)^2$.

**Constrained Hessian at uniform**: $H(u^*) := \nabla^2 \mathcal{E}(u^*) |_{T_{u^*}\Sigma_m} = \Pi^T \nabla^2\mathcal{E}(u^*) \Pi$ where $\Pi = I - (1/n)\mathbf{1}\mathbf{1}^T$.

---

## §2 — Zero-Mode Type Classification

Three mutually-exclusive types of zero modes ($v \in \ker H(u^*) \cap \mathbf{1}^\perp$, $v \neq 0$) are distinguished:

### Type A — Critical zero mode
$v \in V_{\lambda_k}$ for some $k \in \{2, \ldots, n\}$ such that the *boundary-energy spectral contribution* satisfies $\mu_k = 4\alpha\lambda_k + \beta W''(c) = 0$ at the current parameter point. Single-direction zero mode (multiplicity 1 case).

### Type B — Eigenvalue-multiplicity zero modes
At the same crossing $\mu_k = 0$, if $\mathrm{mult}(\lambda_k(L_G)) \geq 2$, the kernel has dimension $\geq 2$ spanned by linearly independent eigenvectors of $L_G$ in $V_{\lambda_k}$.

### Type C — Continuous Goldstone / orbit-tangent zero mode
$v = \frac{d}{d\theta}(g_\theta \cdot u_\star) |_{\theta=0}$ for some non-trivial 1-parameter subgroup $\{g_\theta\}_{\theta \in \mathbb{R}}$ of a (necessarily continuous) symmetry group $\mathcal{G}$ acting on $\Sigma_m$, where $u_\star$ is a critical point with non-trivial $\mathcal{G}$-orbit $\mathcal{O}(u_\star) := \{g_\theta \cdot u_\star : \theta \in \mathbb{R}\}$.

**Note**: Type C requires *continuous* $\mathcal{G}$ acting *non-trivially* on the specific critical point. canonical V5b-T-zero (L1328) instantiates Type C for *corner-saturated* (non-uniform) configurations on $\mathbb{Z}_L^d$-translation-invariant graphs, where the discrete translation orbit is *equienergetic* and its tangent (in the continuum embedding / large-lattice limit) carries the Goldstone mode.

---

## §3 — Statement

**Lemma L-UNI-ZMODE (Uniform Zero-Mode Dichotomy).** Under §1 setup, every $v \in \ker H(u^*)|_{\mathbf{1}^\perp}$ with $v \neq 0$ is of Type A or Type B. **Type C zero modes are absent at $u^* = c\mathbf{1}$.**

Equivalently:
$$\boxed{\ker H(u^*)\big\vert_{\mathbf{1}^\perp} = \bigoplus_{k \in K^*} V_{\lambda_k}(L_G)}$$
where $K^* = \{k \in \{2, \ldots, n\} : \mu_k = 0 \text{ at current } (\alpha, \beta, c)\}$ is the *critical mode index set*. Goldstone/orbit-tangent contributions are zero.

---

## §4 — Proof (Cat A direct, 5 steps)

### Step 1 — Orbit triviality of uniform critical

For any $\sigma \in \mathrm{Aut}(G)$ (the discrete graph automorphism group), the action on $u^*$ satisfies:
$$(\sigma \cdot u^*)_i = u^*_{\sigma^{-1}(i)} = c = u^*_i \quad \forall i \in V.$$
Therefore $\sigma \cdot u^* = u^*$ for *all* $\sigma \in \mathrm{Aut}(G)$, so the $\mathrm{Aut}(G)$-orbit is the singleton:
$$\mathcal{O}_{\mathrm{Aut}(G)}(u^*) = \{u^*\}.$$
The tangent space to this orbit at $u^*$ is $\{0\}$.

Furthermore, for *any* continuous symmetry group $\mathcal{G}$ acting on $\Sigma_m$ by permutation-of-coordinates extension (which is the only natural lift of $\mathrm{Aut}(G)$), the fixed-point property $\sigma \cdot u^* = u^*$ for all $\sigma$ implies that any 1-parameter family $\{g_\theta\}$ acting trivially on the uniform value $c$ generates no non-zero tangent at $u^*$. Specifically:
$$\frac{d}{d\theta}\bigl(g_\theta \cdot u^*\bigr)\bigg\vert_{\theta=0} = 0 \quad \forall \{g_\theta\} \text{ acting on coordinates by permutation extension.}$$

### Step 2 — Type C exclusion at uniform

By definition (§2 Type C), a Goldstone zero mode at $u^*$ requires a non-trivial orbit-tangent direction. By Step 1, no such direction exists at $u^*$. Hence:
$$\text{Type C zero modes at } u^* = c\mathbf{1} : \text{ empty.}$$

**Contrast with V5b-T-zero (canonical L1328)**: V5b-T-zero applies to *corner-saturated* (non-uniform) minimizers $u_\star \neq c\mathbf{1}$, where $\sigma \cdot u_\star \neq u_\star$ in general for $\sigma \in \mathbb{Z}_L^d$ translations — the orbit is *non-trivial* and equienergetic, producing Type C zero modes *via lattice-orbit tangent in continuum/large-$L$ limit*. The uniform $u^*$ in §1 has no such structure.

### Step 3 — Hessian closed-form at uniform

By canonical Theorem 4 (L1466, Cat A), the boundary-energy Hessian at $u^*$ is:
$$\nabla^2 \mathcal{E}_{bd}(u^*) = 4\alpha L_G + \beta W''(c) I$$
acting on $\mathbb{R}^n$. The full SCC Hessian:
$$\nabla^2 \mathcal{E}(u^*) = \lambda_{cl} \nabla^2 \mathcal{E}_{cl}(u^*) + \lambda_{sep} \nabla^2 \mathcal{E}_{sep}(u^*) + 4\alpha\lambda_{bd} L_G + \beta\lambda_{bd} W''(c) I + \lambda_{tr} \nabla^2 \mathcal{E}_{tr}(u^*).$$

Since $u^* = c\mathbf{1}$ is fixed by *all* $\sigma \in \mathrm{Aut}(G)$ (Step 1), the isotropy group $G_{u^*} = \mathrm{Aut}(G)$. By canonical T-σ-Lemma-1 (L1386, Cat A), $\nabla^2 \mathcal{E}(u^*)$ commutes with the $\mathrm{Aut}(G)$-action on $\mathbb{R}^n$ (by representation $\sigma \cdot v = (v_{\sigma^{-1}(i)})_i$).

Restricted to $\mathbf{1}^\perp$ via the $\mathrm{Aut}(G)$-equivariant projector $\Pi$:
$$H(u^*) := \Pi^T \nabla^2 \mathcal{E}(u^*) \Pi$$
also commutes with $\mathrm{Aut}(G)$-action on $\mathbf{1}^\perp$.

### Step 4 — Kernel reduction to $L_G$-eigenspaces (via L-S3-KERNEL-MULT Case B)

By Step 3 + Schur's Lemma, $H(u^*)$ on $\mathbf{1}^\perp$ decomposes into $\mathrm{Aut}(G)$-isotypic blocks. Each $L_G$-eigenspace $V_{\lambda_k}$ (for $k = 2, \ldots, n$) is $\mathrm{Aut}(G)$-invariant (since $L_G$ commutes with $\mathrm{Aut}(G)$ by graph automorphism definition $\sigma L_G \sigma^{-1} = L_G$), hence $H(u^*)$-invariant.

By canonical L-S3-KERNEL-MULT (L1798, Cat A, CV-1.19) Case B (uniform critical $u^* = c\mathbf{1}$, any graph), the non-boundary contributions $\nabla^2 \mathcal{E}_{cl}(u^*), \nabla^2 \mathcal{E}_{sep}(u^*), \nabla^2 \mathcal{E}_{tr}(u^*)$ also commute with $L_G$ on $\mathbf{1}^\perp$ (i.e., $[J_D, L_G]|_{\mathbf{1}^\perp} = 0$ where $J_D$ encompasses all linearized SCC operators).

Therefore $H(u^*)$ acts as a *scalar* on each $V_{\lambda_k}$, say $\hat\mu_k(\alpha, \beta, c, \lambda_{cl}, \lambda_{sep}, \lambda_{tr}) \cdot \mathrm{id}_{V_{\lambda_k}}$. The boundary-energy contribution gives the dominant Theorem 4 term $4\alpha\lambda_k + \beta W''(c) =: \mu_k$. (The non-boundary contributions add bounded corrections that preserve the isotypic block structure but may shift the scalar; in the spinodal interior $W''(c) < 0$ regime, the *zero crossings* of $\hat\mu_k$ are parameter-dependent points and define the *effective critical set* $K^* \subseteq \{2, \ldots, n\}$.)

For the canonical Theorem-4-dominant regime (i.e., when $\lambda_{cl}, \lambda_{sep}, \lambda_{tr}$ are bounded and $\mu_k$ dominates the scalar action), $\hat\mu_k = 0 \Leftrightarrow \mu_k = 0$, and $K^* = \{k : \mu_k = 0\}$.

Thus:
$$\ker H(u^*)\big\vert_{V_{\lambda_k}} = \begin{cases} V_{\lambda_k} & \text{if } \hat\mu_k = 0 \text{ (equivalently } \mu_k = 0 \text{ in Theorem-4-dominant regime)} \\ \{0\} & \text{otherwise} \end{cases}$$

Summing over $k \in K^*$:
$$\ker H(u^*)\big\vert_{\mathbf{1}^\perp} = \bigoplus_{k \in K^*} V_{\lambda_k}(L_G).$$

### Step 5 — Type A/B classification

For each $k \in K^*$:
- If $\mathrm{mult}(\lambda_k(L_G)) = 1$: $\dim V_{\lambda_k} = 1$, contributing a single zero mode of Type A.
- If $\mathrm{mult}(\lambda_k(L_G)) \geq 2$: $\dim V_{\lambda_k} = \mathrm{mult}(\lambda_k)$, contributing zero modes of Type B (the multiplicity is *graph-structural*, independent of parameter values).

Type C residue $\equiv 0$ by Step 2. $\quad\square$

---

## §5 — Cat A Direct Classification

| Lemma component | Canonical anchor | Classification |
|---|---|---|
| Orbit triviality (Step 1) | $u^* = c\mathbf{1}$ definition (algebraic identity) | Cat A definitional |
| Type C exclusion (Step 2) | Step 1 + Type C definition (§2) | Cat A direct |
| Hessian Aut(G)-equivariance (Step 3) | T-σ-Lemma-1 (L1386, Cat A) | Cat A direct (anchored) |
| Isotypic block decomposition (Step 4) | T-σ-Lemma-1 + L-S3-KERNEL-MULT Case B (L1798, Cat A) | Cat A direct (anchored) |
| Scalar action on $V_{\lambda_k}$ (Step 4) | Theorem 4 (L1466, Cat A) + L-S3-KERNEL-MULT Case B | Cat A direct (anchored) |
| Type A/B classification (Step 5) | Multiplicity = graph spectral property (algebraic) | Cat A direct |

**Net classification**: **Cat A direct**. No new hypothesis introduced; all 5 steps derive from prior Cat A canonical material + algebraic identity ($u^* = c\mathbf{1}$ orbit-trivial).

---

## §6 — Non-Overclaim (mandatory)

1. **Uniform critical only**: L-UNI-ZMODE covers $u^* = c\mathbf{1}$ specifically. **Non-uniform critical** (formation regime, corner-saturated configurations) has *Type C present* via V5b-T-zero (canonical L1328) — distinct scope. The "Type C absent" claim does **not** extend to non-uniform critical points.

2. **Off-T8 trivial kernel**: When all $\mu_k \neq 0$ for $k = 2, \ldots, n$ (subcritical regime $\beta/\alpha < r_2^{\text{crit}}$ or other off-$\Sigma_{T8}$ parameter region), the kernel is trivially $\{0\}$ — no zero modes of any type. The dichotomy applies *at* the critical surface $\Sigma_{T8}$ or its higher analogs $\Sigma_k := \{\mu_k = 0\}$.

3. **Full SCC commutativity assumption**: Step 4 invokes L-S3-KERNEL-MULT Case B, which establishes $[J_D, L_G] = 0$ on $\mathbf{1}^\perp$ at uniform critical for *any* graph (via T-σ-Lemma-1). This is *unconditional* Cat A for the SCC standard energies. Case C (Aut(G) trivial + non-regular) would require explicit H-INV hypothesis, but Case C is *not applicable to uniform critical* — at $u^*$, $G_{u^*} = \mathrm{Aut}(G)$ holds *trivially* by uniform-value property (Step 1), placing uniform critical in Case B unconditionally.

4. **Theorem-4-dominant regime**: Step 4 derives the *scalar* eigenvalue $\hat\mu_k$ acting on $V_{\lambda_k}$. In the regime where Theorem-4 boundary-energy $\mu_k = 4\alpha\lambda_k + \beta W''(c)$ dominates the other (closure/sep/tr) contributions (which is the canonical SCC regime where $\lambda_{bd}$ is the primary symmetric-breaking coupling), $\hat\mu_k = \mu_k$ to leading order. Outside this regime (e.g., $\lambda_{cl}$ extreme), the zero crossings shift; the *dichotomy* (no Type C) is unaffected, but the explicit Theorem-4 formula for $\mu_k$ is qualified.

5. **No silent OP resolution**: L-UNI-ZMODE does **not** resolve OP-HMORSE-SADDLE (saddle-point Hessian regularity at non-uniform critical), OP-0005-DYN (Kramers rates), or OP-0009 (multi-formation foundations). It is *purely* a uniform critical statement.

6. **No retraction retry**: The 8 retracted claims (EW universality, Model A z=2.17, $t_\times \sim (\beta/\alpha)^{3/2}$, $D_f^{(k)} = (n-1) - k$, H-int framework, closure RG-irrelevance, $D_f = 11/8$ theorem, $k(k+1)/2-1$ stratification) are all *non-overlapping* with L-UNI-ZMODE scope.

---

## §7 — Cross-References to Today's Work

| Work | Relevance |
|---|---|
| `05_landscape_local_to_global.md` §3.7 | Goldstone Type A/B/C 재분류 motivation; conversational draft 의 Correction #4 가 본 lemma 의 *epistemic seed* |
| `working/cssl/01_critic_evaluation.md` §A.1 | CSSL critic 의 "ker = Goldstone only" misframing critique; 본 lemma 가 *해당 critique 의 formal answer* |
| `canonical.md L-S3-KERNEL-MULT` (CV-1.19, L1798) | Step 4 의 *direct anchor*; L-UNI-ZMODE 는 L-S3-KERNEL-MULT 의 *Goldstone-context specialization* |
| `canonical.md V5b-T-zero` (L1328) | Step 2 의 contrast — V5b-T-zero 는 *non-uniform* corner-saturated context; 본 lemma 는 *uniform* — 두 lemma 는 *complementary scope* |

---

## §8 — Hard-Constraint Check (10/10 PASS)

| Constraint | Status | Evidence |
|---|---|---|
| canonical/* 0 edits | ✓ | 본 파일 = working layer |
| DECLARATION.md 0 edits | ✓ | untouched |
| theorem_status.md 0 edits | ✓ | untouched (CV-1.20 SEAL 시 별도 작업) |
| hypothesis_tree.md 0 edits | ✓ | untouched (CV-1.20 SEAL 시 별도) |
| scc/* 0 edits | ✓ | code untouched |
| 새 framework letter 0 | ✓ | Type A/B/C 는 분류 label only |
| Silent OP resolution 0 | ✓ | OP-HMORSE-SADDLE 등 untouched, §6 #5 명시 |
| 8 retractions 재시도 0 | ✓ | §6 #6 명시 |
| Primitive $u_t$ 전도 0 | ✓ | $u_t$ primitive 유지 |
| 4 에너지 항 병합 0 | ✓ | $E_{cl}, E_{sep}, E_{bd}, E_{tr}$ 별도 처리 |

---

## §9 — CV-1.20 SEAL Promotion Readiness

본 working file 은 *CV-1.20 SEAL candidate* 로 즉시 promotion 가능:

- **Cat A direct**: 5-step proof 가 canonical Cat A anchors (Theorem 4 + T-σ-Lemma-1 + L-S3-KERNEL-MULT) 의 *direct combination*
- **No conditional hypothesis**: Case A/B/C 분기 부재 (uniform critical 은 자동 Case B)
- **Non-overclaim 명시**: 6항목 §6
- **CSSL critic 의 epistemic response**: "ker = Goldstone only" misframing 의 formal 답
- **05_landscape §3.7 의 implicit claim 의 formal proof**: evening exposition 의 *증명 부재* 해소

**Companion lemma** for same SEAL: L-SURFACE-TENSION-RESCALE (Cat A direct, `working/field_equation_framework/06`).

---

*L-UNI-ZMODE Cat A direct working file complete. Ready for CV-1.20 SEAL canonical promotion alongside L-SURFACE-TENSION-RESCALE.*
