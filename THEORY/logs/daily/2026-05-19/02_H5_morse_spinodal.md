---
type: log/daily/development
date: 2026-05-19
mode: deep-attack
sub_target: H5 (Morse stability — spinodal Goldstone mode degeneracy)
session_label: W8-Day2 — T_*/H5 Deep Work
canonical_version: CV-1.17 (sealed 2026-05-15, untouched)
status: draft
cot_enforced: yes
coc_enforced: yes
prior_step: 2026-05-18 AUX-1.5 §4.6.6 / §4.9.5 (registry-level diagnosis)
next_step: §5 의 T-P-F-ε0-K regime restriction draft + cross-ref in 03_T_star_fixed_point.md §5
---

> [!nav] Linked: [[00_plan]] · [[01_pre_brainstorm]] · [[03_T_star_fixed_point]] · [[../../canonical/auxiliary_structures_master|AUX-1.5 §4.6.6/§4.9.5]] · [[../../canonical/canonical|canonical §13 T-P-F-ε0-K L1818-1833]]

# 02 — H5 (Morse Stability, Spinodal Goldstone Mode Degeneracy) — Deep Attack

**Mode**: deep-attack (PRIMARY sub-target).
**Target / mission**: H5 (Morse stability) 가 *generic regime* 에서 어떻게 *Cat A 후보* 로 형식화되는가 + *spinodal critical surface* 에서 *intrinsic degeneracy* 가 어떻게 *명시적 codim-1 stratum* 로 분리되는가. 부수: T-P-F-ε0-K (canonical Cat B, L1818-1833) 의 Cat A path 로서의 *regime restriction* 제안.
**CoT enforced for**: §1-§5 모든 lemma/statement/Cat 분류.
**CoC enforced for**: §1-§5 모든 prior_anchor + causation_chain + inverse_causation_check.

---

## §0 Pre-work xref check (§15.1 의무 기록)

```bash
$ grep -nE "Morse stability|H5\b|spinodal.*degenerate" THEORY/canonical/canonical.md
# Result: T-P-F-ε0-K (L1820 (H5) Morse stability) + L1831 (H5 holds generically) + L2495 SB7 (Σ_Hess = Σ_T8 codim-1)
# = 3 hits, 모두 T-P-F-ε0-K 가정 어휘 또는 Σ_Hess 일치 (수학적 content 부재)

$ grep -rn "H5_morse|morse_spinodal" THEORY/working/
# Result: 0 hits (clean slate)

$ grep -nE "§4\.6\.6|§4\.9\.5" THEORY/canonical/auxiliary_structures_master.md
# Result: §4.6.6 (H5 new COB-violation entry) + §4.9.5 (H5 U-잔류 diagnosis)
# = 2 hits, registry-level diagnosis only
```

**verdict**: **1-3 hits, 다른 topic** (AUX-1.5 registry diagnosis + canonical T-P-F-ε0-K assumption 어휘) → 진행 가능. **본 file 의 *novel positioning*** = *registry → theory* 격상 (AUX-1.5 의 *U-잔류 classification* → mathematical *statement + Cat A 후보 path sketch*); H5-MORSE-SPINODAL OP 의 *draft* 본문 (canonical OP catalog 의 *registration prerequisite* 작성).

§ "기존 working 과의 관계" — AUX-1.5 §4.9.5 의 P1 Sard / P2 Equivariant / P3 C-R 표 가 본 file 의 §1-§3 의 *직접 입력*; 본 file 은 AUX-1.5 의 *방법론적 확장 위치* (registry diagnosis → mathematical refinement).

---

## §1 Statement (Refined Drafts)

본 §1 은 plan §A.2 의 A.2.1-A.2.3 draft 를 *수학적 정확한 form* 으로 refinement.

### §1.1 Statement A.2.1 — Generic Morse on Parameter Space

**Statement A.2.1** *(Generic Morse, Cat A 후보 conditional).* SCC energy
$$\mathcal{E}_\lambda(u) = \lambda_{\mathrm{cl}}\,\mathcal{E}_{\mathrm{cl}}(u) + \lambda_{\mathrm{sep}}\,\mathcal{E}_{\mathrm{sep}}(u) + \lambda_{\mathrm{bd}}(u),$$
restricted to the volume-constrained simplex $\Sigma_m = \{u \in [0,1]^n : \sum_i u_i = m\}$, is a polynomial in $u$ of total degree $\leq 4$ (degree 4 from $\mathcal{E}_{\mathrm{bd}}$'s double-well $W$; degree $\leq 2$ from $\mathcal{E}_{\mathrm{cl}}, \mathcal{E}_{\mathrm{sep}}$). Let $\Theta := (\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \alpha, \beta, m) \in \mathbb{R}^{4}_{>0} \times (0,1)$ be the SCC parameter point. Then:
$$\mathcal{D}_{\mathrm{Morse}}(G) := \{\,\Theta \in \mathbb{R}^4_{>0} \times (0,1) \;:\; \text{every critical point of } \mathcal{E}_\Theta\vert _{\Sigma_m} \text{ is non-degenerate}\,\}$$
contains an *open dense* subset (in standard topology); furthermore $\mathcal{D}_{\mathrm{Morse}}(G)$ is *Zariski-open* (i.e., its complement is contained in a real algebraic subvariety of positive codimension).

**CoT step 1**: $\mathcal{E}_\Theta(u)$ 가 $u$ 에 대해 polynomial (canonical-confirmed by §13 Theorem-4 등 다수 row 의 explicit polynomial form) → $\nabla \mathcal{E}_\Theta$ 도 polynomial.
**CoT step 2**: 비특이 Hessian 의 *singular locus* $\{(\Theta, u) : \det \mathrm{Hess}\,\mathcal{E}_\Theta(u) = 0, \nabla \mathcal{E}_\Theta(u) = 0\}$ 가 $(\Theta, u)$-space 의 real algebraic subvariety — finite system of polynomial equations.
**CoT step 3**: Sard 1942 의 algebraic strengthening (Hironaka 1964 resolution) → 본 subvariety 의 $\Theta$-projection 의 measure zero in standard Lebesgue + 더 강한 Zariski-codim ≥ 1.

### §1.2 Statement A.2.2 — Spinodal Stratum is Σ_T8 (Σ_Hess = Σ_T8 일치)

**Statement A.2.2** *(Spinodal critical surface identification, Cat A — direct from canonical SB7).* The Hessian degeneracy locus
$$\Sigma_{\mathrm{Hess}} := \{\,(\Theta, u^*) : u^* \text{ critical, } \det \mathrm{Hess}\,\mathcal{E}_\Theta(u^*)\vert _{T_{u^*}\Sigma_m} = 0\,\}$$
*equals* the T8 phase transition surface
$$\Sigma_{T8} := \{ \,(\Theta, u^*) : \beta/\alpha = 4\lambda_2(G)/ \mid W''(c(u^*)) \mid \, \}$$
on the uniform critical sheet $u^* = c\mathbf{1}$ (c the equilibrium concentration). In particular $\Sigma_{T8}$ is codim-1 in $\Theta$-space (parameterized by $\beta/\alpha$).

**CoC anchors**: canonical §13 Theorem SB7 (Cat A, L2495) provides this identification directly — verbatim "$\Sigma_{\mathrm{Hess}} = \Sigma_{T8}$" + envelope theorem T5 + analyticity 명시.

### §1.3 Statement A.2.3 — Stratified Morse on Post-Bifurcation Stable Basin

**Statement A.2.3** *(Stratified Morse, Cat A 후보 conditional).* For $\Theta$ in the *post-bifurcation supercritical regime*
$$\mathcal{R}_{\mathrm{post}} := \{\,\Theta : \beta/\alpha > 4\lambda_2(G)/\lvert W''(c) \rvert, \; c \in (\tfrac{3-\sqrt{3}}{6}, \tfrac{3+\sqrt{3}}{6})\,\}$$
(spinodal interior + supercritical), the *stable basin* $\mathcal{B}_{\mathrm{stable}}(\Theta) \subset \Sigma_m$ — defined as the union of basins of all local energy minima with $\mathrm{Hess}\,\mathcal{E}_\Theta > 0$ on $T_{u^*}\Sigma_m$ — admits a *stratified Morse decomposition* (in the sense of A.2.1) outside the codim-1 stratum $\Sigma_{T8}$. Equivalently: $\mathcal{E}_\Theta\vert _{\mathcal{B}_{\mathrm{stable}}}$ is Morse for $\Theta$ in an open dense subset of $\mathcal{R}_{\mathrm{post}}$.

**CoT step 1**: $\mathcal{R}_{\mathrm{post}}$ 는 *post-bifurcation* — uniform critical $c\mathbf{1}$ 이 *Hessian-unstable* (T8 supercritical 의 정의) → 새 non-uniform critical (formation) 가 *stable* sheet 으로 출현 (pitchfork bifurcation 의 직접 후속).
**CoT step 2**: A.2.1 의 Generic Morse 가 stable critical sheet 위에서 적용 가능 (non-uniform critical) — uniform $c\mathbf{1}$ 의 spinodal degeneracy (Σ_T8) 와 *분리된* sheet.
**CoC anchors**: canonical V5b-T-zero (Cat A definitional, L1328) 의 exact zero on translation-invariant orbit — uniform $c\mathbf{1}$ sheet 의 Goldstone direction; canonical T-PERSIST-1B-UNCONDITIONAL (Cat A, L2063) 의 post-bifurcation stable basin 의 *unconditional* persistence + Kupka-Smale genericity + Sard 직접 사용 history.

---

## §2 P1 (Sard transversality) Sketch — Cat A 후보 Proof Outline

본 §2 는 A.2.1 (Generic Morse) 의 P1 Sard route 의 *증명 sketch*. 5 lemma 의 chain.

### §2.1 Lemma L1 — Critical map is real-analytic in (Θ, u)

**Lemma L1.** The critical-point map
$$\Phi : \mathbb{R}^4_{>0} \times (0,1) \times \Sigma_m \to \mathbb{R}^{n-1}, \quad (\Theta, u) \mapsto \nabla_{\Sigma_m} \mathcal{E}_\Theta(u)$$
is real-analytic (in fact polynomial) of total degree $\leq 3$ in $(u, \Theta)$ separately.

**Proof (CoT + CoC):**
- CoT step 1: $\mathcal{E}_\Theta(u)$ 는 polynomial in $u$ (총 degree $\leq 4$, A.2.1 statement). Linear in $\Theta = (\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \alpha, \beta, m)$ except for the $\frac{1}{m}$ normalization on $\Sigma_m$ (smooth on $m \in (0,1)$, real-analytic).
- CoT step 2: $\nabla_{\Sigma_m} = (\mathrm{Id} - \frac{1}{n}\mathbf{1}\mathbf{1}^T) \nabla$ (projector onto $T\Sigma_m$) — linear, preserves polynomial.
- CoC anchors: canonical operators.py + energy.py 의 closed-form gradient (FD-verified 1e-9, CLAUDE.md §"Critical Implementation Details") confirms polynomial structure.

### §2.2 Lemma L2 — Generic regularity via Sard's theorem

**Lemma L2.** Let $\mathcal{S}_\Theta := \{\,u \in \Sigma_m : \Phi(\Theta, u) = 0, \; \det \mathrm{Hess}\,\mathcal{E}_\Theta(u)\vert _{T\Sigma_m} = 0\,\}$ be the degenerate critical set at parameter $\Theta$. Let $\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}}) \subset \mathbb{R}^4_{>0}$ be the projection of $\Sigma_{\mathrm{degen}} := \{(\Theta, u) : u \in \mathcal{S}_\Theta\}$. Then $\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}})$ has *Lebesgue measure zero*.

**Proof (CoT + CoC):**
- CoT step 1: $\Sigma_{\mathrm{degen}}$ 는 polynomial equations 의 zero set (L1 + Hessian determinant polynomial form) → real algebraic subvariety of $\mathbb{R}^4_{>0} \times \Sigma_m$.
- CoT step 2: Sard 1942 (Bull. AMS 48:883-890) 의 표준 form — smooth map between manifolds 의 critical values 의 measure zero. 본 case 의 *critical map* 은 $\mathrm{proj}_\Theta : \Sigma_{\mathrm{degen}} \to \mathbb{R}^4_{>0}$; *critical points* 는 *전체 surface* (since codim ≥ 1 by L1 polynomial form).
- CoT step 3: $\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}})$ 가 Sard 의 critical values + algebraic subvariety → Lebesgue-null. □
- CoC anchors: canonical T-PERSIST-1B-UNCONDITIONAL (Cat A, L2063) 의 *Erratum 2026-04-03 unconditional upgrade via Kupka-Smale genericity (NB removal) + Sard's theorem (GT absorption)* 가 same proof technique 의 *기존 활용* — 본 lemma 가 그 technique 의 *generic Morse extension*.

### §2.3 Lemma L3 — Algebraic strengthening (Zariski-open dense)

**Lemma L3.** $\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}}) \subset \mathbb{R}^4_{>0}$ is contained in a real algebraic subvariety of codimension $\geq 1$ (i.e., $\mathcal{D}_{\mathrm{Morse}}(G)$ is Zariski-open dense).

**Proof (CoT + CoC):**
- CoT step 1: $\Sigma_{\mathrm{degen}}$ 는 polynomial equations + polynomial inequalities (open conditions like $\lambda > 0$) 의 *semialgebraic* set — Tarski-Seidenberg quantifier elimination 보장.
- CoT step 2: Projection of semialgebraic 는 semialgebraic (Bochnak-Coste-Roy, *Real Algebraic Geometry*, 1998).
- CoT step 3: Hironaka 1964 resolution of singularities → real algebraic subvariety 의 codim 결정 가능.
- CoC anchors: pre_brainstorm §6.3 (polynomial maps + Hironaka resolution) 의 *direct application*.

**Note**: L3 의 *full proof* 는 본 day 의 scope 외 — *Cat A 후보 path 의 existence* 만 명시; *완결 Cat A 증명 시도 부재* (plan §D 명시).

### §2.4 Lemma L4 — Goldstone direction on uniform sheet is exactly Σ_T8

**Lemma L4.** On the uniform critical sheet $u^* = c\mathbf{1} \in \Sigma_m$ (so $m = c$), the Hessian $\mathrm{Hess}\,\mathcal{E}_\Theta(c\mathbf{1})\vert _{T\Sigma_m}$ has zero eigenvalue *if and only if* $\beta/\alpha = 4\lambda_2(G)/\lvert W''(c) \rvert$ (i.e., $\Theta \in \Sigma_{T8}$).

**Proof (CoT + CoC):**
- CoT step 1: On uniform $c\mathbf{1}$, the Hessian eigenvalues are $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}} - \beta\vert W''(c)\vert $ for $k = 2, \ldots, n$ (canonical §13 Theorem 4 cited).
- CoT step 2: Zero eigenvalue ⟺ $\mu_2 = 0$ (smallest eigenvalue first; $k=1$ excluded by $\Sigma_m$ projection) ⟺ $\beta/\alpha = 4\lambda_2/\lvert W''(c) \rvert$.
- CoT step 3: 본 condition 은 *exactly* T8 phase transition (canonical DECLARATION.md 중심 정리).
- CoC anchors: canonical §13 Theorem 4 (CV-1.5.1, L1466 *spinodal interior* hypothesis discussion 직접 인용); canonical SB7 (Cat A) confirms $\Sigma_{\mathrm{Hess}} = \Sigma_{T8}$ as global identity (본 lemma 는 uniform sheet 에서의 *local* form).

### §2.5 Lemma L5 — Spinodal stratum is intrinsic codim-1 (Cat A — direct from SB7)

**Lemma L5.** $\Sigma_{T8} \subset \mathbb{R}^4_{>0} \times (0,1)$ is a smooth codim-1 hypersurface (parameterized by the single equation $\beta/\alpha = 4\lambda_2/\lvert W''(c) \rvert$, with $\lambda_2 = \lambda_2(G)$ fixed by graph).

**Proof (CoT + CoC):**
- CoT step 1: 본 equation 은 *smooth* function of $(\alpha, \beta, m)$ (since $c = m \in (0,1)$, $W''(c) = 6c - 6c^2 - 1$ smooth nonzero except at spinodal boundary $c = (3 \pm \sqrt{3})/6$).
- CoT step 2: Implicit function theorem (Standard) → $\Sigma_{T8}$ 는 codim-1 smooth submanifold of $\mathbb{R}^4_{>0} \times (0,1)$.
- CoC anchors: canonical SB7 (Cat A, L2495) — codim-1 명시 + envelope theorem 적용 history.

### §2.6 Conclusion of P1 sketch

L1 + L2 + L3 → A.2.1 (Generic Morse Zariski-open dense). L4 + L5 → A.2.2 + A.2.3 (spinodal stratum intrinsic codim-1).

**Self-Cat 분류**: *잠정 Cat A 후보, 검증 필요.*
- *Why 잠정*: L3 의 Zariski-open dense 의 *full algebraic geometry proof* 가 sketch level — Hironaka resolution 적용의 *detail* 미작성 (W9+ staging).
- *Why Cat A 후보 (not Cat B)*: L2 (Sard) 만으로도 *measure zero* Lebesgue version 은 *standard Cat A* (T-PERSIST-1B-UNCONDITIONAL 의 동일 technique reuse).
- *검증 필요 항목*: (a) Hironaka resolution 의 SCC E 의 polynomial form 에 대한 *적용 가능성* 의 명시적 확인, (b) projection of semialgebraic set 의 codim 의 explicit lower bound, (c) graph $G$ 의 $\lambda_2(G) = 0$ degenerate case (disconnected) 의 separation handling.

---

## §3 P2 (Equivariant Morse, Bott 1954) + P3 (Crandall-Rabinowitz fold) — *왜 부차적* 비교

### §3.1 P2 — Equivariant Morse (Bott 1954, Atiyah-Bott 1984)

**Approach**: graph automorphism group $\mathrm{Aut}(G)$ 가 $\Sigma_m$ 에 작용 → critical orbits 의 *Morse-Bott* 처리 (점 아닌 critical manifold). Goldstone modes 가 orbit tangent direction 으로 *exact zero eigenvalue*.

**Limitation (CoC failure chain)**:
- CoT step 1: Generic graph (canonical SCC convention) 의 Aut(G) trivial 또는 매우 작음 (pre_brainstorm §3.2 명시) → equivariant Morse 가 *trivial group action* 으로 환원 → standard Morse 와 동일.
- CoT step 2: P2 가 *오직* translation-invariant graph ($T^d$, $C_n$) 에서 *non-trivial* — 본 case 가 canonical V5b-T-zero (Cat A, L1328) 의 *기존 처리 영역*. **P2 의 mathematical 산출이 V5b-T-zero 와 *중복* (P5 archive risk in §8a)** — 단 본 file 의 *주장* 부재 (auxiliary support only).
- CoT step 3: 결과: P2 가 **specific graph subclass 에서 만 작동**, generic graph 에서는 P1 으로 환원 → *왜 부차적*.

**CoC anchors**:
- Bott 1954 (Annals of Math 60:248-261) — non-degenerate critical manifolds.
- canonical V5b-T-zero (Cat A) — 본 영역의 *existing canonical processing*.

**Verdict**: P2 = *V5b-T-zero 의 일반화 후보*; 본 day 의 *주 산출 부재*. Cat 분류 부적용 (subordinate to P1).

### §3.2 P3 — Crandall-Rabinowitz fold + (SN-iii)(SN-iv)

**Approach**: T8 spinodal critical surface 가 saddle-node (fold) bifurcation locus → Crandall-Rabinowitz 1971 의 simple zero eigenvalue + transversality → curve of nontrivial solutions.

**Limitation (CoC failure chain)**:
- CoT step 1: Crandall-Rabinowitz 의 *Cat A result* 는 (SN-iii)+(SN-iv) genericity conditional — canonical SN3 (Cat B conditional, L2501-2502) 의 직접 inheritance.
- CoT step 2: (SN-iii)+(SN-iv) genericity 의 verification 이 OP-OMS-033b OPEN — 본 day 의 scope 외.
- CoT step 3: T8 spinodal 이 *fold (codim-1)* 인지 *cusp (codim-2)* 인지 의 더 깊은 catastrophe-theoretic 분류 — pre_brainstorm §3.4 의 *부분 평가 only*; 본 day 미작성.

**CoC anchors**:
- Crandall-Rabinowitz 1971 (J. Functional Analysis 8:321-340).
- canonical SN3 (Cat B conditional, L2501) + Lemma SN4 (PROOF SKETCH).
- canonical OP-OMS-033b sub-OP OPEN.

**Verdict**: P3 = *기존 canonical Cat B conditional path 의 자연 후속*; 본 day 의 추가 mathematical 산출 부재 (조건부 inheritance only). Cat 분류 부적용 (subordinate to P1).

### §3.3 P1 vs P2 vs P3 — 3-criteria 의 직접 점검

| Criterion | P1 (Sard) | P2 (Equivariant Morse) | P3 (Crandall-Rabinowitz) |
|---|---|---|---|
| Tool | measure-theoretic + algebraic | group action + Morse-Bott | linearized eigenvalue + IFT |
| Failure mode | polynomial regularity 위반 (unlikely) | Aut(G) trivial (likely generic) | (SN-iii)(SN-iv) genericity (OPEN OP-OMS-033b) |
| Success condition | $\Theta$ ∉ Zariski-codim≥1 subvariety | Aut(G) non-trivial | local simple eigenvalue at saddle-node |
| Cat 후보 | A | A on subclass | B conditional |

세 approach 의 *수학적 독립 + 실패 모드 다름 + 조건부 성공 조건 다름* — deep-attack §5.1 3-criteria PASS (plan §C.3 reconfirmed).

---

## §4 OP-H5-MORSE-SPINODAL — Draft Statement (Registration Recommended Only)

**N.B.**: 본 §4 는 *draft only* — canonical OP catalog 본문 수정 부재 (plan §G non-goal). *Registration recommended* — 후속 결정 plan §E item 5.

### §4.1 OP-H5-MORSE-SPINODAL — Draft

**OP-H5-MORSE-SPINODAL (Draft, ranked HIGH).**

*Statement*: The SCC energy $\mathcal{E}_\Theta(u) = \lambda_{\mathrm{cl}}\mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}}$ on $\Sigma_m$ is Morse for $\Theta$ in a Zariski-open dense subset $\mathcal{D}_{\mathrm{Morse}}(G) \subset \mathbb{R}^4_{>0} \times (0,1)$ (Cat A 후보, P1 Sard route). The complement is contained in the T8 phase transition surface $\Sigma_{T8}$ — a smooth codim-1 hypersurface (Cat A by SB7) — where the Hessian acquires an intrinsic Goldstone zero eigenvalue corresponding to the spinodal symmetry-breaking moment. Stratified Morse holds on the post-bifurcation stable basin $\mathcal{B}_{\mathrm{stable}}(\Theta)$ for $\Theta \in \mathcal{R}_{\mathrm{post}}$ in open dense subset.

*Status*: **OPEN** (Cat A 후보 path identified — P1 Sard sketch §2; Hironaka algebraic strengthening + full proof W9+ staging).

*Sub-problems (≥3 open questions, plan §C.6)*:
- **OP-H5-α**: Hironaka algebraic strengthening of P1 — explicit codim ≥ 1 of $\mathrm{proj}_\Theta(\Sigma_{\mathrm{degen}})$. [Cat A 진입 path 의 *마지막 mile*]
- **OP-H5-β**: P2 Equivariant Morse 의 *non-trivial Aut(G)* subclass 의 mathematical characterization — V5b-T-zero (Cat A) 의 일반화 위치 명시. [W9+ subclass extension]
- **OP-H5-γ**: P3 Crandall-Rabinowitz path 의 (SN-iii)+(SN-iv) genericity — OP-OMS-033b 와 결합. [기존 sub-OP 와의 unification]

*Unlock effect*: T-P-F-ε0-K Cat B → Cat A path (regime restriction to $\mathcal{R}_{\mathrm{post}}$ stable basin); P-F-A1 Package II (Eyring-Kramers) prefactor Cat B 진입의 *부분 H5 replacement*.

*Cat 자기 분류*: **Cat A 후보 conditional on P1 sketch full proof** — currently sketch level (잠정 Cat B until §2.3 Hironaka detail 작성).

---

## §5 T-P-F-ε0-K Regime Restriction — Proposed Wording (Canonical L1818-1833)

**N.B.**: 본 §5 는 *proposed wording only* — canonical 본문 수정 부재 (plan §G non-goal). 후속 결정 plan §E item 5.

### §5.1 Current canonical wording (verbatim from canonical.md L1818-1833)

> **T-P-F-ε0-K. Kramers Exponent Stability under Bernoulli Regularization.** Under T-P-F-ε0 hypotheses (H1)–(H4) and:
> *(H5)* Morse stability: saddle $\tilde{u}^*_{\mathrm{sad}}$ and minimum $\tilde{u}^*_{\mathrm{min}}$ are non-degenerate critical points of $\mathcal{E}+\varepsilon R$ stable for $\varepsilon\in[0,\varepsilon_0]$ (no critical-point bifurcation);
> ...
> *Assumptions:* (H5) Morse stability holds generically (non-degenerate SCC saddles) but is not globally verified for $\mathcal{E}_{\mathrm{SCC}}+\varepsilon R$. No spectral/Eyring-Kramers theorem claimed.
> *Status:* **Cat B** — conditional on H5 (Morse stability). Cat A promotion path: (i) prove H5 for $\mathcal{E}_{\mathrm{SCC}}$ saddles, (ii) establish spectral gap / Poincaré inequality on $\mathcal{F}_M(\mathcal{P})$.

### §5.2 Proposed regime restriction

**Proposed amendment (draft only)**: replace (H5) with the *regime-restricted* form

> *(H5')* Morse stability on $\mathcal{R}_{\mathrm{post}}$ stable basin: $\Theta \in \mathcal{R}_{\mathrm{post}}$ (post-bifurcation supercritical regime, plan §A.2.3 / 본 file §1.3) and both $\tilde{u}^*_{\mathrm{sad}}, \tilde{u}^*_{\mathrm{min}} \in \mathcal{B}_{\mathrm{stable}}(\Theta)$ (stable basin, away from $\Sigma_{T8}$ codim-1 stratum); both non-degenerate critical points of $\mathcal{E}_{\mathrm{SCC}}+\varepsilon R$ for $\varepsilon \in [0, \varepsilon_0]$.

*Promotion path (Cat B → Cat A under (H5'))*: §2 P1 Sard sketch + Hironaka strengthening (OP-H5-α) → $\mathcal{D}_{\mathrm{Morse}}(G) \cap \mathcal{R}_{\mathrm{post}}$ Zariski-open dense → (H5') 가 *generic*. Spinodal critical surface $\Sigma_{T8}$ 는 *separate treatment* (P-F-A1 Package III future work, beyond Eyring-Kramers).

**CoT step 1**: 현재 (H5) 가 *globally unverified* (canonical L1832 명시) → Cat B 의 ceiling 결정 cause.
**CoT step 2**: (H5') 가 *regime restriction* — $\mathcal{R}_{\mathrm{post}}$ + $\mathcal{B}_{\mathrm{stable}}$ 한정으로 *generic Morse* (P1 Sard) 적용 가능 → Cat A path 의 *명시적 prerequisite identification*.
**CoT step 3**: Spinodal stratum 의 *Eyring-Kramers 미적용* 명시 — Cat B → Cat A path 의 *완결* 이 아니라 *scope refinement*.

**CoC anchors**:
- canonical T-P-F-ε0-K (Cat B, L1818-1833) — direct target.
- canonical SB7 (Cat A, L2495) — Σ_T8 codim-1 separation.
- 본 file §1.3 / §2 / §4 — (H5') 정식화의 *수학적 prerequisite*.

**Inverse_causation_check**:
- if §2 P1 Sard sketch fails (e.g., Hironaka non-applicable): (H5') 의 *generic* claim 무효 → Cat A path 부재.
- if SB7 reverse (Σ_Hess ≠ Σ_T8): spinodal stratum separation 무효 → (H5') 의 regime restriction wording 부적용.
- if $\mathcal{R}_{\mathrm{post}}$ 가 empty (sub-critical only): Cat A path 무 (vacuous) — graph-dependent (e.g., $\lambda_2(G)$ 가 매우 작으면 spinodal regime 전체가 sub-critical).

### §5.3 Cross-reference to T_* (full detail in `03_T_star_fixed_point.md` §5)

T-P-F-ε0-K Cat A path 는 H5' + T_* 의 *공동* requirement — T_* 자체의 *axiomatic 위상* (Route C P classification, 03_T_star §5) 이 (H5') 의 Cat A 와 *상보적*. P-F-A1 Package II Eyring-Kramers prefactor 의 *full Cat B 진입* 은 (H5' + Route C T_*) 둘 다 *parallel resolved* 시 — 단 본 day 의 *주장* 부재 (leading question for W9+, pre_brainstorm §7.3 FEP framework).

---

## §6 Summary + Self-Cat Classification

본 file 의 *주요 산출*:

1. **A.2.1 / A.2.2 / A.2.3 refined statements** (§1) — *수학적 정확 form*, plan §A.2 의 draft 의 polished version.
2. **P1 Sard sketch (5 lemma L1-L5)** (§2) — *Cat A 후보 path*; Sard 1942 + Hironaka 1964 (sketch level on Hironaka).
3. **P2 / P3 *왜 부차적* CoC chain** (§3) — Aut(G) trivial / OP-OMS-033b OPEN.
4. **OP-H5-MORSE-SPINODAL draft + 3 sub-problems** (§4) — *registration recommended only*.
5. **T-P-F-ε0-K Cat A path proposal** (§5) — (H5') regime restriction to $\mathcal{R}_{\mathrm{post}} \cap \mathcal{B}_{\mathrm{stable}}$.

**Self-Cat 분류 of overall claim "H5 generic Morse + spinodal stratum split is Cat A 후보 path"**: **잠정 Cat B (검증 필요)**.
- *Cat A 후보 라고 부르는 이유*: P1 Sard route 의 *standard technique* + canonical T-PERSIST-1B-UNCONDITIONAL 의 *기존 사용*.
- *잠정 Cat B 인 이유*: L3 (Hironaka algebraic strengthening) 의 *full proof 부재* + (H5') wording 의 *canonical promotion 미수행*.
- *검증 필요 항목*: (a) Hironaka detail (OP-H5-α); (b) (SN-iii)(SN-iv) generic verification (OP-H5-γ, OP-OMS-033b 와 결합); (c) $\Sigma_{T8}$ 의 spinodal stratum 위 *post-saddle-node basin* 의 *후속 dynamics* (Eyring-Kramers 미적용).

**§8a Archive Pattern P1-P6 자가 점검**: **0/6 부합** (plan §E.3 reconfirmed).
- P1 (근본 질문 우회): 부합 0 — DECL-1.0 Q1 (T8 boundary) 의 직접 답 진척.
- P2 (Vocabulary refactoring): 부합 0 — u_t 본체 미변경, 새 어휘 0 (H5-α/β/γ 는 OP sub-label 표준 form).
- P3 (Canonical content 중복): 부합 0 — H5 mathematical content 가 canonical 에 부재 (registry-level 어휘만, AUX-1.5).
- P4 (외부 도구 도입 계기): 부합 0 — Sard/Bott/C-R 모두 AUX-1.5 §4.9.5 prior diagnosis 의 직접 후속.
- P5 (Self-audit + canonical-xref 미시행): 부합 0 — §0 xref + 본 file §1-§5 의 inline anchors 명시.
- P6 (언어 vs 수학 분리): 부합 0 — 본 file 은 *수학 only* (statement + sketch + Cat 분류); 언어 framing 부재 또는 inline.

---

## §7 Cross-references + Forward Hooks

- **03_T_star_fixed_point.md §5** — T_* Route C 정식화; H5+T_* 의 공동 P-F-A1 Package II blockage 의 cross-ref.
- **99_summary.md (EOD)** — H5 progress + Decision gate 점검 + 다음 day 직접 입력 매핑.
- **Forward (W9+ leading questions)**:
  - OP-H5-α (Hironaka detail) — explicit algebraic geometry proof.
  - OP-H5-β (P2 subclass extension) — V5b-T-zero 와 generic Aut(G) 의 unification.
  - OP-H5-γ (P3 + OP-OMS-033b) — Crandall-Rabinowitz fold 의 (SN-iii)+(SN-iv) genericity verification.
  - pre_brainstorm §7.3 FEP integration — H5 = belief crystallization moment 의 *meta-hypothesis*; W9+ leading question.

---

*End of 02_H5_morse_spinodal.md. Next: 03_T_star_fixed_point.md (T_* SECONDARY).*
