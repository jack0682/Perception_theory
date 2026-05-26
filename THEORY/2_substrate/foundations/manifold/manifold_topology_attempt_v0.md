---
type: working/foundation/synthesis
date: 2026-05-20
session_label: W8-Day3 (Wed) — Manifold Topology Palette Precision Mapping + Direct Proof Attempt
canonical_version: CV-1.18 (sealed 2026-05-19, untouched)
status: working draft, Cat C synthesis with 1 Cat B-target concrete claim
parent_plan: /Users/ojaehong/.claude/plans/eager-splashing-dream.md
---

> [!nav] Linked: [[../proofs/_SUMMARY_v0.2]] · [[../../canonical/auxiliary_structures_master|AUX-1.5]] · [[../../canonical/canonical#§13|canonical §13]] · [[../../canonical/CV-1.18_SEAL|CV-1.18 SEAL]] · [[../../logs/daily/2026-05-19/02_H5_morse_spinodal|어제 02_H5]]

# Manifold Topology Methodology Palette — Precision Mapping + Direct Proof Attempt

## §0. Mission

본 working file 의 목적:
1. **14-tier manifold topology palette** (Perelman Ricci flow + JSJ + Mostow + surgery + h/s-cobordism + Novikov/Borel/Farrell-Jones + controlled topology + Freedman + Donaldson/Seiberg-Witten + cubulation + minimal surface + Morse/Kirby + computational + Dehn surgery) 의 각 SCC 정밀 매핑 — *어디까지 옮겨지는가*
2. **Critic 검토 통과 corrections** 적용 — 4 specialist agent 산출 + 1 critic adversarial pass 의 결과 통합
3. **Master synthesis theorem** (Cat C 후보) — 4 tier 결합 statement
4. **One concrete new claim** (Cat C → Cat B target): **distance-controlled Poincaré gap** `λ_1 ≥ c_G · dist(Θ, Σ_T8) / T_*` — 본 working day 의 *진짜 deliverable*
5. **Honest gaps** — Cat A 까지의 거리 명시

**Critical caveats (CN10 disclosure preserved)**:
- 모든 4-tier 매핑은 *외부 framework 의 SCC 적용 시도*. SCC primitives (u_t, soft cohesion, 4-energy) 는 이 algebraic-topology machinery 를 *필요로 하지 않음*. 본 file 의 imports 는 *analogies*, *instantiations 아님*. 단 ONE concrete claim (distance-controlled Poincaré) 은 BE framework 의 *내재적* 결과.
- Cat A/B/C status declarations 은 *작업 진행 추정치*. Canonical promotion 은 별도 SEAL pipeline 필요.
- "Bakry-Émery declared CLOSED" 경고 (pf_a1_lions_sznitman_freidlin_route.md L36) 인지 — 본 file 의 BE 재진입은 *CD curvature 의 distance-explicit form* 의 new target, 기존 closure 와 *상충 아님*.

---

## §1. 14-Tier Palette — Precision Mapping Quick Reference

| Tier | manifold topology 원형 | SCC 유비 | 핵심 ingredient | 전이성 등급 | 매핑 상세 |
|---|---|---|---|---|---|
| **1** | Perelman Ricci flow + W-entropy | Reflected Langevin SDE + Bakry-Émery W_SCC | Γ_2 + CD(ρ, ∞) | **높은** (Cat B target) | §2 (정밀) |
| **2** | JSJ + Haken hierarchy 분해 | Σ_T8 Whitney stratification by Goldstone kernel dim | k(k+1)/2-1 codim | **높은** | §3 (정밀) |
| **3** | Mostow-Prasad rigidity | (G, Θ) ↦ landscape isomorphism | hyperbolic 필요 | **misleading** (critic: drop) | §6 (note) |
| **4** | Browder-Novikov-Sullivan-Wall surgery | K-jump algebra: S_K → N_K → R_K (representation ring) | OP-0008 = N⊕R | **부분** (Cat C, critic: R_K not L_K) | §4 (정밀, R_K corrected) |
| **5** | h-/s-cobordism Whitehead torsion | SCC deformation rigidity | Wh(Aut(G)) | **추측** | §6 (note) |
| **6** | Novikov/Borel/Farrell-Jones assembly | (separate from Tier 8) | higher signature | 추측 | §6 (note) |
| **7** | Quinn controlled topology | T11 Γ-convergence + RG analysis | controlled SDE | **부분 작동 중** (Cat A: T11) | §6 (note) |
| **8** | Davis-Lück assembly | CN-COB Assembly Map μ | AUX-1.5 §8 closure | **높은** (Cat B 가능) | §5 (정밀) |
| **9** | Freedman topological 4-manifold | Topological vs smooth dichotomy | Hess sign vs eigenvalue | 추측 | §6 (note) |
| **10** | Donaldson + Seiberg-Witten gauge | Exotic SCC landscape detection | moduli of formations | 추측 | §6 (note) |
| **11** | Agol-Wise cubulation | SCC graph cube complex | Aut(G) cubulate | 추측 | §6 (note) |
| **12** | Schoen-Yau minimal surface | Stable critical hypersurface in Σ_m | T-PreObj-1 부분 | 추측 | §6 (note) |
| **13** | Morse + handle + Kirby | SCC energy E as Morse function | **이미 작동** | — | Phase 0-4 인프라 |
| **14** | Regina/SnapPy computational | scc/ Python (15 modules, 225+1xf) | **이미 작동** | — | 전반 인프라 |

**Critic adversarial pass 후 corrections 통합**:
- Tier 1: Γ_2 sign/normalization (BGL §1.16 convention) 정밀화 — `∇²E ≥ ρ I` (T_* 없음) 또는 `Hess(E/T_*) ≥ ρ I`
- Tier 2: 미니버설 unfolding genericity 가설 명시; "open dense" → "open dense in Aut(G)-equivariant trivial-isotype stratum"
- Tier 4: `L_K^SCC → R_K^SCC` (representation ring of stabilizer); Wall L-theory 표기 폐기
- Tier 8: 63/65 → 정확한 enumeration 필요 (denominator 명시)
- Tier 3 (Mostow): **drop entirely** — hyperbolicity 가설 SCC 부재; Łojasiewicz-Simon rigidity 로 대체 후보

---

## §2. Tier 1 Precision — Bakry-Émery W_SCC (corrected)

### §2.1 Convention 결정 (BGL §1.16)

reflected Langevin SDE (T-PF-A1-SDE Cat A, CV-1.9):
$$dU_t = -\nabla \mathcal{E}(U_t)\,dt + \sqrt{2T_*}\,dB_t \quad (\text{with Neumann reflection at } \partial\tilde{C})$$

Generator (BGL §1.16):
$$Lf = -\nabla \mathcal{E} \cdot \nabla f + T_* \Delta f$$

Carré du champ:
$$\Gamma(f, g) = T_* \nabla f \cdot \nabla g$$

(factor `T_*` from diffusion `σσ^T = 2T_* I`.)

### §2.2 Γ_2 calculation (corrected sign)

**Lemma 2.1 (Γ_2 explicit).** For $L = -\nabla \mathcal{E} \cdot \nabla + T_* \Delta$ on $\tilde{C} \subset \mathbb{R}^{n-1}$ (T-PF-A1-AR Cat A affine chart):
$$\Gamma_2(f) = T_*^2 \vert \mathrm{Hess}(f)\vert _{HS}^2 + T_* \langle \nabla^2 \mathcal{E} \cdot \nabla f, \nabla f \rangle$$

**Proof.** BGL 2014, Example 2.3.2 (overdamped Langevin Γ_2). For drift $b = -\nabla\mathcal{E}$, the Bochner-Weitzenböck identity gives:
$$\Gamma_2(f) = T_*^2\vert \mathrm{Hess}(f)\vert _{HS}^2 + T_* \cdot \mathrm{sym}(-\mathrm{Jac}(b))[\nabla f, \nabla f]$$
where $\mathrm{sym}(-\mathrm{Jac}(b)) = \mathrm{sym}(\nabla^2 \mathcal{E}) = \nabla^2 \mathcal{E}$ (symmetric by smoothness). $\square$

### §2.3 CD(ρ, ∞) condition (corrected — no T_* on RHS in BGL convention)

**Definition 2.2 (BGL convention CD).** The Langevin SDE satisfies $\mathrm{CD}(\rho, \infty)$ iff:
$$\Gamma_2(f) \geq \rho \cdot \Gamma(f, f)$$
for all smooth $f$. Equivalently (using Lemma 2.1):
$$T_*^2 \vert \mathrm{Hess}(f)\vert ^2 + T_* \langle \nabla^2 \mathcal{E} \cdot \nabla f, \nabla f\rangle \geq \rho T_* \vert \nabla f\vert ^2$$

Choosing $f$ linear (Hess = 0):
$$\langle \nabla^2 \mathcal{E} \cdot v, v\rangle \geq \rho \lvert v \rvert^2 \quad \forall v$$

So the *correct* CD condition: $\boxed{\nabla^2 \mathcal{E} \geq \rho \cdot I}$ (NO T_* on RHS).

**Critic finding #1 corrected**: previous notation `∇²E ≥ ρ T_* I` was a units error. ρ here has units of [Energy]/[Field]² (Hessian eigenvalue dimension), independent of T_*.

### §2.4 W_SCC definition (BGL-consistent)

**Definition 2.3.** For probability measure $\mu = \rho \cdot \pi_{T_*}$ on $\tilde{C}$ and $\tau > 0$:
$$\mathcal{W}_{\mathrm{SCC}}(\mu, \tau) := \tau \cdot I(\mu \vert \pi_{T_*}) - T_* \cdot H(\mu \vert \pi_{T_*})$$
where $I = \int \rho \vert \nabla \log\rho\vert ^2 d\pi_{T_*}$, $H = \int \rho \log\rho\,d\pi_{T_*}$.

(*Note*: 이전 agent 정의 `τ·I/T_* - H` 에서 normalization 조정. 결과 dimensionally consistent.)

### §2.5 Monotonicity theorem

**Theorem W-MONO-corrected (Cat C).** Under $\mathrm{CD}(\rho_0, \infty)$ with $\rho_0 > 0$ uniformly on a subset $U \subset \tilde{C}$, for Fokker-Planck flow $\partial_t \rho_t = L\rho_t$ with $\mathrm{supp}(\mu_t) \subset U$:
$$\frac{d}{dt} H = -I, \quad \frac{d}{dt} I \leq -2\rho_0 \cdot I, \quad \frac{d}{dt} \mathcal{W}_{\mathrm{SCC}}(\mu_t, \tau) \leq T_* \cdot I \cdot (1 - 2\rho_0 \tau)$$

For $\tau \geq 1/(2\rho_0)$: $d\mathcal{W}_{\mathrm{SCC}}/dt \leq 0$.

**Proof.** de Bruijn (Step 1) + gradient commutation (Step 2) + Lemma 2.1 + CD(ρ_0, ∞) (Step 3) — standard BGL §4.2 derivation. □

### §2.6 Failure mode on Σ_T8 (Critic interp A clarification)

**Theorem FAIL.** On $\Sigma_{T8}$ (specifically at uniform critical sheet $u = c\mathbf{1}$):
- (a) $\nabla^2 \mathcal{E}_{bd}(c\mathbf{1})\vert _{T\Sigma_m} \geq 0$ (PSD), with Fiedler direction $\phi_2$ giving exact zero eigenvalue
- (b) For any $\rho_0 > 0$: $\mathrm{CD}(\rho_0, \infty)$ fails *pointwise on $\Sigma_{T8}$* because $\langle\nabla^2\mathcal{E}\,\phi_2,\phi_2\rangle = 0 < \rho_0 \vert \phi_2\vert ^2$
- (c) **Critic ambiguity resolution**: CD failure is *pointwise on $\Sigma_{T8}$*, NOT *in neighborhood*. In bulk neighborhood, $\rho_0 > 0$ holds — this is the content of §2.7 (distance-controlled).

**Critic finding #5 corrected**: previous statement `"on Σ_T8: CD(0,∞) holds but CD(ρ_0>0,∞) FAILS"` was ambiguous (Interpretation A pointwise vs B neighborhood). The correct reading is **Interpretation A (pointwise on Σ_T8)**. In open complement of Σ_T8, CD holds with $\rho_0 > 0$ depending on distance — §2.7.

### §2.7 The ONE concrete new claim — Distance-controlled CD bound

**Lemma 2.4 (Distance-controlled Hessian — Cat C, target Cat B).** There exists $c_G > 0$ depending only on $(G, m)$ such that for all $\Theta \in \tilde{C}_\Theta := \mathbb{R}^4_{>0} \times I_{sp}$ with $d(\Theta) := \mathrm{dist}(\Theta, \Sigma_{T8}) > 0$:
$$\inf_{u \in \tilde{C}, \lvert v \rvert=1, v \perp \mathbf{1}} \langle \nabla^2 \mathcal{E}_\Theta(u) \cdot v, v\rangle \geq c_G \cdot d(\Theta)$$

**Proof sketch (Łojasiewicz approach).** The Fiedler eigenvalue
$$\mu_2(\Theta, c) = 4\alpha\lambda_2(L_G) + \beta W''(c)$$
is smooth in $\Theta$, and $\mu_2 = 0$ defines $\Sigma_{T8}$ (SB7 Cat A). By the implicit function theorem + smooth dependence + compactness of $\tilde{C}$:
$$\mu_2(\Theta, c) \geq c_G \cdot d(\Theta) \quad \forall \Theta, c$$
for some $c_G > 0$ (the local Lipschitz / Łojasiewicz constant of $\mu_2$ on $\Sigma_{T8}$).

Other eigenvalues $\mu_k = 4\alpha\lambda_k + \beta W''(c) \geq \mu_2$ for $k \geq 3$, so the Hessian-restricted-to-tangent-space spectral lower bound is at least $\mu_2 \geq c_G \cdot d(\Theta)$. $\square$

(*Gap*: Łojasiewicz step requires explicit constant — currently sketch only.)

**Corollary 2.5 (Sharp Poincaré gap — Cat C target).** Under Lemma 2.4 + BGL convention:
$$\boxed{\lambda_1(L_{T_*}^{\Theta}) \geq c_G \cdot d(\Theta) / 1}$$
(Note: BGL $\lambda_1 \geq \rho_0$ when CD($\rho_0, \infty$) holds, and $\rho_0 = c_G \cdot d(\Theta)$.)

**This *strictly beats* T-PF-A1-PE Cat A bound `λ_1 ≥ (π²/n)·exp(-osc(E)/T_*)`** when:
$$c_G \cdot d(\Theta) > (\pi^2/n) \cdot e^{-\mathrm{osc}/T_*}$$

i.e., **away from Σ_T8 by sufficient distance**, the bulk-regime BE bound is sharper than the canonical Cat A bound.

**This is the ONE genuinely new mathematical content** of the synthesis. Everything else is structural reorganization.

### §2.8 Gaps for Cat A status (Tier 1)

| Gap | 내용 | 작업 |
|---|---|---|
| G1.1 | Lemma 2.4 의 $c_G$ explicit form | Łojasiewicz constant 계산 |
| G1.2 | Boundary terms in Γ_2 (Neumann at $\partial\tilde{C}$) | BGL §4.7 manifolds-with-boundary regularization |
| G1.3 | Uniform CD lower bound 의 domain — bulk vs. small basin | local restriction theorem 필요 |
| G1.4 | T_* registration (OP-0021, now Route C via CV-1.18 §N) | already partial |
| G1.5 | Soliton characterization | Goldstone orbit invariance proof |

**ETA**: Corollary 2.5 Cat C → Cat B = ~3 sessions (Łojasiewicz step + boundary regularization).

---

## §3. Tier 2 Precision — Σ_T8 Whitney Stratification (corrected)

### §3.1 Setup

Parameter space: $\mathcal{P} = \mathbb{R}^4_{>0} \times I_{sp}$, $\dim = 5$. Σ_T8 codim-1 in $\mathcal{P}$ (SB7 Cat A, canonical L2495-2510). $\dim \Sigma_{T8} = 4$.

### §3.2 Stratification by Goldstone kernel dim

**Definition 3.1.** For $k \geq 1$:
$$\Sigma_{T8}^{(k)} := \{(G, \Theta, u^*) \in \Sigma_{T8} : \dim \ker(\mathrm{Hess}(\mathcal{E}_\Theta)(u^*)\vert _{T\Sigma_m}) = k\}$$

### §3.3 Codimension formula (corrected with miniversal hypothesis)

**Hypothesis (H-min, miniversal genericity)**: The Hessian map $\Phi: \mathcal{P} \times I_{sp} \to \mathrm{Sym}^{n-1}(\mathbb{R})$ is *miniversally unfolded* in the sense of Arnold-catastrophe theory, i.e., transverse to the determinantal varieties $\Sigma^{\geq k} := \{A : \dim \ker A \geq k\}$.

**Theorem 3.2 (codim formula, conditional on H-min).** Under H-min:
$$\mathrm{codim}_{\Sigma_{T8}}(\Sigma_{T8}^{(k)}) = \frac{k(k+1)}{2} - 1 \quad \text{for } k \geq 1$$

**Derivation**: Codim in symmetric matrix space of $\{ker \geq k\}$ is $k(k+1)/2$ (Arnold 1972, Golubitsky-Guillemin §VI). Σ_T8 itself is codim-1 in $\mathcal{P}$. Net codim of $\Sigma_{T8}^{(\geq k)}$ inside $\Sigma_{T8}$ = $k(k+1)/2 - 1$.

| $k$ | $\mathrm{codim}_{\Sigma_{T8}}$ | $\dim \Sigma_{T8}^{(k)}$ | Local model |
|---|---|---|---|
| 1 | 0 | 4 | Generic neck (pitchfork) |
| 2 | 2 | 2 | Cap (Morse-Bott) |
| 3 | 5 | (empty for 4-dim Σ_T8) | Higher cusp |

### §3.4 Critic correction — "Open dense" precision

**Critic finding #2 corrected**: Generic-position claim requires *equivariant transversality* statement. The correct statement:

**Proposition 3.3 (Critic-corrected open dense).** Σ_T8^(1) is open dense in $\Sigma_{T8}$ **restricted to the Aut(G)-equivariant trivial-isotype Fiedler stratum**, i.e., the set of parameters where the Fiedler eigenspace of $L_G$ is *simple* and carries the trivial irrep of $\mathrm{Aut}(G)$.

On translation-invariant graphs (V5b-T setting), the Fiedler space is typically *not* trivial-isotype (carries reflection / translation irreps); on such graphs Σ_T8^(2) or higher may be open dense locally. The "generic" hypothesis is graph-class-dependent.

### §3.5 Local model on Σ_T8^(1) (generic neck)

Lyapunov-Schmidt at $p_0 = (G, \Theta_0, c_0\mathbf{1}) \in \Sigma_{T8}^{(1)}$:
- 1-dim kernel $\mathrm{span}\{\psi_1\}$ (Fiedler vector)
- Reduced bifurcation equation: $f(t, \beta) = t \cdot g(t^2, \beta)$ (parity from $W(u)=W(1-u)$)
- Crandall-Rabinowitz 1971 → supercritical pitchfork
- Normal form: $E_{red}(t) = (\beta - \beta_{crit}) t^2/2 + A t^4/4 + O(t^6)$ with $A > 0$

**Conditional Cat A**: Cat A *given* (SN-iii)(SN-iv) genericity (OP-OMS-033b OPEN).

### §3.6 Local model on Σ_T8^(2) (cap, equivariant Morse-Bott)

2-dim kernel (e.g., two coincident Laplacian eigenvalues on cylindrical graph):
- Equivariant Lyapunov-Schmidt to ℝ²
- Reduced potential: $E_{red}(t_1, t_2) = a(t_1^2 + t_2^2) + b(t_1^2 + t_2^2)^2 + \tilde{c}\,t_1^2 t_2^2 + O(\lvert t \rvert^6)$
- D_4 symmetry breaks O(2) to D_4 at quartic order → 4 minima selected
- Morse-Bott structure on circle $t_1^2 + t_2^2 = r^2$

### §3.7 Whitney conditions (Mather 1970)

**Theorem 3.4 (Cat C, conditional H-min)**: Σ_T8 = ⊔_k Σ_T8^(k) satisfies Whitney conditions (a) and (b) by Mather's general theorem for kernel-rank strata of smooth maps (Mather *Notes on Topological Stability* 1970, Ch. 2).

### §3.8 Aut(G)-equivariance (Cat A via T-σ-Theorem-3)

**Proposition 3.5 (Cat A)**: ker(Hess) at $u^* = c\mathbf{1}$ = Fiedler eigenspace = $\mathrm{Aut}(G)$-submodule of $T_{u^*}\Sigma_m$.

**Proof**: Hess = $4\alpha L_G + \beta W''(c) I$, commutes with $\mathrm{Aut}(G)$-action (canonical theorem 4 + T-σ-Theorem-3 Cat A). $\square$

### §3.9 Gaps for Cat A (Tier 2)

| Gap | 내용 | OP reference |
|---|---|---|
| G2.1 | Hironaka algebraic strengthening (H-min hypothesis) | OP-H5-α (HIGH, canonical) |
| G2.2 | (SN-iii)(SN-iv) genericity for Σ_T8^(1) pitchfork | OP-OMS-033b |
| G2.3 | Non-translation-invariant graph case (Σ_T8^(2)) | OP-H5-β |
| G2.4 | Equivariant Lyapunov-Schmidt for k ≥ 2 | OP-H5-γ (W10+) |
| G2.5 | $\Sigma_{T8}^{(0)}$ undefined (k=0 case is the *complement* of Σ_T8) | terminology fix |

---

## §4. Tier 4 Precision — Surgery-Analog Sequence (corrected to R_K)

### §4.1 Critic correction — L_K^SCC → R_K^SCC

**Critic finding #3**: Wall L-theory uses Witt groups of quadratic forms (with involution), not K_0. The SCC analog uses representation rings (additive K_0 of group rings), which is the *representation theory* not L-theory.

**Renaming**:
- ~~L_K^SCC := K_0(ℂ[Stab])~~ (incorrect terminology)
- **R_K^SCC := R(Stab) ≅ K_0(ℂ[Stab])** (representation ring of per-formation stabilizer)

The 4-term sequence becomes:
$$R_{K+1}^{\mathrm{SCC}} \xrightarrow{\partial} \mathcal{S}_K^{\mathrm{SCC}} \xrightarrow{\eta} \mathcal{N}_K^{\mathrm{SCC}} \xrightarrow{\theta} R_K^{\mathrm{SCC}}$$

This is NOT a surgery exact sequence (no quadratic form structure). It is a *representation-ring obstruction sequence* — structurally analogous but algebraically lighter.

### §4.2 Definitions (with basin equivalence specified)

**Critic finding #4 corrected**: basin equivalence pinned down to:

**Definition 4.1 (basin equivalence)**: $(u_1^*, K) \sim_{\mathrm{basin}} (u_2^*, K)$ iff $u_1^*, u_2^*$ lie in the same $\mathrm{Aut}(G) \wr S_K$-orbit on the set of critical points in $\mathcal{B}_K(G, \Theta)$.

(Choice: orbit equivalence, not gradient-flow homotopy. Reason: generically critical points are isolated, so gradient-flow homotopy classes = singletons; the orbit equivalence is the natural collapse that captures "same up to symmetry/relabeling".)

**Definition 4.2**: $\mathcal{S}_K^{\mathrm{SCC}}(G, \Theta) := \{\text{admissible K-configs}\} / \sim_{\mathrm{basin}}$

**Definition 4.3**: $\mathcal{N}_K^{\mathrm{SCC}}(G, \Theta) := \{\nu(u^*) = (v_1, \lambda_1, \mathrm{stab}(v_1))\}/\sim_{\mathrm{Aut}(G)_{u^*}}$ (Goldstone direction data at K-jump spinodal)

**Definition 4.4**: $R_K^{\mathrm{SCC}}(G, \Theta) := \bigoplus_{k=1}^K R(\mathrm{Aut}(G)_{u^{(k)*}})$

### §4.3 Maps

- **η: S → N** — extract softest Hessian eigenvector. Well-defined modulo basin choice.
- **θ: N → R** — compute σ-inheritance Wigner-projection class:
$$\theta(\nu) = [\sigma^A(\text{post-jump})] - \Phi_*([\sigma^A(u^*)]) \in R_K^{\mathrm{SCC}}$$
where $\Phi_*$ is the algebraic inheritance map.
- **∂: R_{K+1} → S_K** — boundary obstruction action

### §4.4 D_4 worked example (K=1 → K=2 SPLIT)

For $D_4$-symmetric graph:
- $R_1^{\mathrm{SCC}} = R(D_4) \cong \mathbb{Z}^5$ (5 irreps: $A_1, A_2, B_1, B_2, E$)
- $R_2^{\mathrm{SCC}} = R(\mathrm{Aut}(G)_{u^{(1)*}}) \oplus R(\mathrm{Aut}(G)_{u^{(2)*}})$
- $\mathcal{N}_1$: Goldstone direction $v_1$ transforms as $B_1$ or $B_2$ (T-V5b-T direction)
- $\theta(v_1)$: Wigner-projection class in $\mathbb{Z}^5$

The exactness assertion: $v_1$ is realizable SPLIT iff $\theta(v_1) = 0$ iff post-split σ-tuples are consistent with parent representation content.

### §4.5 Status (Cat C, exactness unproved)

The sequence is structurally well-defined under Def 4.1-4.4. **Exactness is unproved**. The map $\theta$ is well-defined modulo OP-0008-SPLIT-σ Cat C. The map $\partial$ is sketch only.

### §4.6 OP-0008 connection (explicit)

**Direct identification**:
- OP-0008-SPLIT-**direction** (Cat B) = element of $\mathcal{N}_K^{\mathrm{SCC}}$
- OP-0008-SPLIT-**σ_standard** (Cat C) = obstruction class $\theta(\nu) \in R_K^{\mathrm{SCC}}$
- OP-0008-MERGE-σ (Cat C) = similar via merge boundary map

The surgery-analog framework *organizes* OP-0008 into N⊕R decomposition. Not yet *solves* it.

### §4.7 Gaps for Cat A (Tier 4)

| Gap | 내용 |
|---|---|
| G4.1 | Exactness proof of 4-term sequence (currently sketch) |
| G4.2 | $\partial: R_{K+1} → S_K$ explicit formula |
| G4.3 | OP-0008-MERGE-σ / SPLIT-σ Cat C → Cat B |
| G4.4 | Pointed-set vs group structure on $\mathcal{S}_K$ |
| G4.5 | Validity beyond $\mathrm{Aut}(G) \wr S_K$ orbit equivalence |

---

## §5. Tier 8 Precision — CN-COB Assembly Map

### §5.1 Source category

$$\mathrm{Source} := \mathcal{D}(G) \otimes \mathcal{A}(u) \otimes \mathcal{P}(\mathrm{OMS\text{-}1}, \xi)$$

Three pieces:
- $\mathcal{D}(G)$: derived invariants of graph G ($\lambda_2(L)$, Fiedler vector, PH_0, Hess spectrum, $K_{act}$, $\sigma_{standard}$, etc.) — AUX-1.5 §8.1.1 (~30 items)
- $\mathcal{A}(u)$: fixed axiom content ($W$ form, $\Sigma_m$ form, $a_{cl} < 4$, $b_D = 0$, E1-E4, etc.) — AUX-1.5 §8.1.2 (~25 items)
- $\mathcal{P}(\mathrm{OMS\text{-}1}, \xi)$: observer-personal $(q, \lambda, \xi) \in \mathcal{M}_{obs}$ — AUX-1.5 §8.1.3 (~18 items, incl. $T_*$ via CV-1.18 §N)

### §5.2 Target

$$\mathrm{Inv}_{\mathrm{SCC}}(G, \Theta) := \{\text{all derivable invariants of } (\Sigma_m, E_\Theta)\}$$

### §5.3 Assembly map μ

$$\mu(d \otimes a \otimes p) = \text{derived invariant assembled from } (d, a, p)$$

Three explicit factorizations:
1. **T8 phase transition**: $\mu(\lambda_2(L), W, q=\beta/\alpha) = \mathbb{1}[\text{formation exists}]$
2. **K_act**: $\mu(\mathrm{PH}_0(u^*), \text{filtration}, \rho_{pers}) = K_{act}$
3. **Gibbs sector mass**: $\mu(B_K, E_1\text{-}E_4, T_*) = p_K = \pi_{T_*}(B_K)$

### §5.4 Surjectivity (Cat B, AUX-1.5 §8 enumeration)

**Theorem 5.1 (Cat B, Critic-corrected denominator)**: μ surjects onto $\mathrm{Inv}_{\mathrm{SCC}} \setminus \{H5\text{-related}\}$.

**Proof (counting)**: AUX-1.5 §8.1 enumerates 65 auxiliary items with D/A/P/Hybrid/External classification:
- D-classified: 30 items
- A-classified: 25 items
- P-classified: 18 items (incl. $T_*$ via CV-1.18 §N)
- Hybrid: 2 (Wigner, P7)
- External: 1 ($I_t$ raw)
- U-residuals: **1** (H5, after CV-1.18 absorbed T_* into P)

**Critic finding correction**: previously stated "63/65 = 97%" is misleading. The correct count post-CV-1.18:
- Total CN-COB-relevant items: 64 (65 minus external $I_t$)
- Classified: 63 (D + A + P + Hybrid)
- Residual: 1 (H5)
- **Closure: 63/64 ≈ 98.4%**, single residual = H5

$\mu$ surjective on the 63 classified items by construction (each item is its own factorization). $\square$

### §5.5 Injectivity (Cat D speculative, no Mostow)

**Critic finding #5 — Mostow analogy DROPPED**: hyperbolicity 가설 SCC 부재. Mostow-Prasad rigidity 는 negative curvature 의 산물; SCC 는 CD(0+, ∞) (non-negative + Goldstone flat).

**Replacement (Łojasiewicz-Simon rigidity)**: 
**Conjecture 5.2 (replacement for Mostow-analog)**: For generic $(G, \Theta) \neq (G', \Theta')$ in CD($\rho_0$, ∞) regime, $\mu(\mathcal{D}(G) \otimes \mathcal{A} \otimes \mathcal{P}(\Theta)) \neq \mu(\mathcal{D}(G') \otimes \mathcal{A} \otimes \mathcal{P}(\Theta'))$.

**Approach** (not Mostow): use Łojasiewicz-Simon convergence theorem (T14 Cat A) to show that energy landscape determines $(G, \Theta)$ up to graph isomorphism in the generic-Hessian regime.

### §5.6 Cross-tier factorizations

- Tier 1 W_SCC: depends on $(\pi_{T_*}, E, \tau)$, all factor through μ
- Tier 2 Σ_T8: $\mu^{-1}(\{\text{critical value of phase function}\})$ = level set of μ
- Tier 4 K-jump: $\mathrm{Aut}(G) \wr S_{K_{act}} \subset \mu(\mathcal{D}(G))$

### §5.7 Gaps for Cat A (Tier 8)

| Gap | 내용 |
|---|---|
| G8.1 | Categorical formalization of source ($\infty$-category structure) |
| G8.2 | Explicit factorization for all 63 items (case-by-case) |
| G8.3 | H5 residual = CD curvature degeneracy on Σ_T8 (connect to Tier 1) |
| G8.4 | Injectivity (Conjecture 5.2) Cat D → Cat C |

---

## §6. Tiers 3, 5, 6, 7, 9-12 (notes only — low-priority but enumerated)

### §6.1 Tier 3 — Mostow Rigidity (DROPPED per Critic #5)

**Status**: Misleading analogy. Drop entirely. Use Łojasiewicz-Simon rigidity instead (Tier 8 §5.5).

### §6.2 Tier 5 — h-/s-Cobordism + Whitehead Torsion

**Candidate**: SCC deformation rigidity. Two formations are *deformation trivial* iff Whitehead-like torsion vanishes in $Wh(\mathrm{Aut}(G))$. Status: Cat D speculative.

### §6.3 Tier 6 — Novikov / Borel / Farrell-Jones (subsumed by Tier 8)

**Subsumed**: Tier 8 assembly map IS the SCC version of Novikov/Borel/Farrell-Jones assembly. Separate enumeration unnecessary.

### §6.4 Tier 7 — Controlled Topology / Quinn

**Connection**: T11 Γ-convergence Cat A 이미 작동 (canonical line 1168). RG analysis (canonical L1082) OPEN. Phase 2 (no-collapsing 확장)의 자연 결합.

### §6.5 Tier 9 — Freedman Topological 4-Manifold

**Candidate**: SCC topological vs smooth landscape equivalence. Possibly leads to:
- Topological equiv: Hess sign pattern only (Morse index)
- Smooth equiv: Hess eigenvalues exact
- T-OP6-B (Cat A) provides partial precedent ($d_H \leq 2\sqrt{\alpha/\beta}$)

Status: Cat D speculative.

### §6.6 Tier 10 — Gauge Theory (Donaldson / SW)

**Candidate**: Exotic SCC landscape detection via moduli-of-formations intersection form. Status: Cat D highly speculative.

### §6.7 Tier 11 — Cubulation (Agol-Wise)

**Candidate**: SCC graph cube complex extension. Status: Cat D, low-priority.

### §6.8 Tier 12 — Schoen-Yau Minimal Surface

**Candidate**: Stable critical hypersurface in $\Sigma_m$ provides phase-transition obstruction. Connection to T-PreObj-1 Cat A unclear. Status: Cat D speculative.

---

## §7. Master Synthesis Theorem (Cat C synthesis)

### §7.1 Statement

**SCC Energy Landscape Structure Theorem (Cat C synthesis, W8-Day3 candidate)**

Let $(G, \Theta)$ be a finite connected graph with $\Theta = (\alpha, \beta, \lambda_{cl}, \lambda_{sep}, c) \in \mathbb{R}^4_{>0} \times I_{sp}$ in the post-bifurcation regime $\beta/\alpha > 4\lambda_2(L_G)/\lvert W''(c) \rvert$ (T8). Let $\mathcal{E}_\Theta: \Sigma_m \to \mathbb{R}$ be the SCC energy with $T_* \in B_\xi^{\mathrm{OMS\text{-}1}}$ (CV-1.18 §N).

The energy landscape $(\Sigma_m, \mathcal{E}_\Theta)$ admits the following 4-part decomposition:

**(I) Bulk Bakry-Émery curvature** *(Tier 1, Cat C target Cat B)*:
For $\Theta \notin \Sigma_{T8}$ with $d := \mathrm{dist}(\Theta, \Sigma_{T8}) > 0$:
$$\nabla^2 \mathcal{E}_\Theta(u) \geq c_G \cdot d \cdot I \text{ on } T\Sigma_m \quad \forall u \in \tilde{C}$$
(distance-controlled CD($c_G \cdot d$, ∞) condition, Lemma 2.4).
Consequences:
- $\mathcal{W}_{\mathrm{SCC}}$ is monotone along Langevin flow (Theorem W-MONO)
- Poincaré gap $\lambda_1 \geq c_G \cdot d$ (Corollary 2.5, BGL convention)
- Sharpens T-PF-A1-PE Cat A bound for $d > (\pi^2/n) e^{-\mathrm{osc}/T_*}/c_G$

**(II) Critical stratum** *(Tier 2, Cat B-target conditional H-min)*:
$\Sigma_{T8}$ admits Whitney stratification $\Sigma_{T8} = \bigsqcup_{k\geq 1} \Sigma_{T8}^{(k)}$ with $\mathrm{codim}_{\Sigma_{T8}}(\Sigma_{T8}^{(k)}) = k(k+1)/2 - 1$. $\Sigma_{T8}^{(1)}$ open dense in Aut(G)-equivariant trivial-isotype stratum. CD curvature vanishes precisely along Goldstone direction = Fiedler eigenspace.

**(III) Transition algebra** *(Tier 4, Cat C representation-ring sequence)*:
K-jumps at $\Sigma_{T8}$ are governed by:
$$R_{K+1}^{\mathrm{SCC}} \xrightarrow{\partial} \mathcal{S}_K^{\mathrm{SCC}} \xrightarrow{\eta} \mathcal{N}_K^{\mathrm{SCC}} \xrightarrow{\theta} R_K^{\mathrm{SCC}}$$
with obstruction class $\theta(\nu) \in R_K^{\mathrm{SCC}} = K_0(\mathbb{C}[\mathrm{Stab}])$ = σ-inheritance Wigner-projection class (OP-0008).

**(IV) Closure** *(Tier 8, Cat B)*:
All landscape invariants factor through assembly map:
$$\mu: \mathcal{D}(G) \otimes \mathcal{A}(u) \otimes \mathcal{P}(\mathrm{OMS\text{-}1}, \xi) \to \mathrm{Inv}_{\mathrm{SCC}}(G, \Theta)$$
$\mu$ surjective on $\mathrm{Inv}_{\mathrm{SCC}} \setminus \{H5\text{-residual}\}$. Closure ratio 63/64 ≈ 98.4%. Single residual = H5 = Goldstone CD curvature vanishing on $\Sigma_{T8}$.

### §7.2 Proof sketch

Each component proved in §2-§5 with full referencing. Synthesis = (I) + (II) + (III) + (IV) is a *coherent description*, not a single new proof; the unification is the *content*. The one place where genuinely new mathematical content appears is **§2.7 Lemma 2.4 + Corollary 2.5** (distance-controlled Poincaré gap).

### §7.3 What's NEW vs CV-1.18

Three new structural items:

1. **Three formerly independent obstructions identified as one**: H5 failure (Morse stability gate), Goldstone zero-mode (V5b-T-zero Cat A), and codim-1 algebraic singularity of $\Sigma_{T8}$ (SB7 Cat A) are the *same phenomenon* expressed in three formalisms (Bakry-Émery curvature degeneracy / kernel of Hessian / Whitney stratum).

2. **Distance-controlled curvature lower bound** (§2.7): $\rho_0(\Theta) \geq c_G \cdot \mathrm{dist}(\Theta, \Sigma_{T8})$ — first parameter-explicit (Θ-distance-explicit) curvature bound in SCC. T-PF-A1-PE Cat A bound is $T_*$-explicit but not Θ-distance-explicit.

3. **Categorical home for OP-0008**: $R_K^{\mathrm{SCC}} = K_0(\mathbb{C}[\mathrm{Stab}])$ identifies σ_standard inheritance class with rep-ring obstruction. Organizes (not solves) OP-0008.

### §7.4 H5 location

H5 sits at **exactly one place**: the failure of CD($\rho_0 > 0$, ∞) along the Goldstone direction on $\Sigma_{T8}^{(k)}$. Formally: $\ker \nabla^2 \mathcal{E}_\Theta\vert _{\Sigma_{T8}^{(k)}}$ is the $k$-dim Aut(G)-submodule on which Bakry-Émery curvature is exactly zero. This is the **sole** residual under assembly map μ.

H5 is therefore not "missing" — it is **localized to a codim-$(k(k+1)/2-1)$ stratum and identified as Goldstone curvature vanishing**.

### §7.5 Strongest concrete corollary (Cat C → Cat B target)

**Corollary 7.1 (Distance-controlled Poincaré gap)**:
For $\Theta$ in bulk regime with $d := \mathrm{dist}(\Theta, \Sigma_{T8}) > 0$:
$$\boxed{\lambda_1(\Sigma_m, \mathcal{E}_\Theta, T_*) \geq c_G \cdot d}$$
where $c_G > 0$ depends only on $(G, m)$.

**This is the ONE piece of genuinely new mathematical content** the synthesis produces. Cat C currently; Cat B target after Łojasiewicz-Simon explicit constant.

### §7.6 Cat status (honest assessment)

| Component | Status | Critic verdict |
|---|---|---|
| Master theorem overall | **Cat C synthesis** | Coherent in scope, gaps in components |
| (I) Bulk CD | **Cat C target Cat B** | Bakry-Émery convention fixed; Łojasiewicz step needed |
| (II) Stratification | **Cat B-target conditional** | H-min hypothesis OP-H5-α; equivariant transversality OP-H5-β |
| (III) Surgery sequence | **Cat C sketch** | Exactness unproved; renamed L→R |
| (IV) Assembly μ | **Cat B (enumeration)** | 63/64 AUX-1.5 §8 enumeration; injectivity Conjecture only |
| Corollary 7.1 | **Cat C target Cat B** | One concrete new claim, ~3 sessions to Cat B |

---

## §8. Gaps Consolidated

총 17 gap, 우선순위 순:

| Priority | Gap | Tier | ETA | Result |
|---|---|---|---|---|
| **1** | G1.1 Łojasiewicz constant $c_G$ explicit | 1 | 3 세션 | Corollary 7.1 Cat C → Cat B |
| 2 | G2.1 Hironaka algebraic (H-min) | 2 | 5 세션 | Theorem 3.2 Cat A |
| 3 | G2.2 (SN-iii)(SN-iv) genericity | 2 | OP-OMS-033b |
| 4 | G4.1 4-term exactness proof | 4 | 5 세션 | Sequence Cat B |
| 5 | G4.3 OP-0008-σ Cat C → Cat B | 4 | OP-0008 W9+ |
| 6 | G1.2 Boundary terms in Γ_2 | 1 | 2 세션 |
| 7 | G8.1 Categorical source formalization | 8 | 5 세션 |
| 8 | G2.3 Non-trans-invariant Σ_T8^(2) | 2 | OP-H5-β |
| 9 | G2.4 Equivariant LS for k≥2 | 2 | OP-H5-γ |
| 10 | G4.2 ∂: R_{K+1} → S_K explicit | 4 | 3 세션 |
| 11 | G1.3 Bulk vs basin CD domain | 1 | 2 세션 |
| 12 | G4.4 Pointed-set vs group | 4 | 2 세션 |
| 13 | G1.4 T_* OP-0021 (partial via Route C) | 1 | CV-1.18 부분 |
| 14 | G1.5 Soliton characterization | 1 | 4 세션 |
| 15 | G8.2 63 items explicit factorization | 8 | 5 세션 (case-by-case) |
| 16 | G8.3 H5 residual = CD degeneracy (Tier 1↔8) | 8 | already in synthesis |
| 17 | G8.4 Injectivity Conjecture 5.2 | 8 | open-ended |

---

## §9. Recommended Next Mathematical Work

### §9.1 Priority 1 (3 세션) — Distance-controlled CD bound

**Goal**: Prove Lemma 2.4 (Łojasiewicz step) with explicit $c_G > 0$ depending only on $(G, m)$. This promotes Corollary 7.1 from Cat C to Cat B.

**Approach**:
- Use $\mu_2(\Theta, c) = 4\alpha\lambda_2(L_G) + \beta W''(c)$ smooth in $\Theta$
- Implicit function theorem on Σ_T8 (smooth codim-1, SB7 Cat A)
- Compactness of $\tilde{C}$ gives uniform Lipschitz constant

**Deliverable**: Cat B distance-controlled Poincaré gap, sharper than T-PF-A1-PE in bulk regime.

### §9.2 Priority 2 (5 세션) — Σ_T8 stratification Cat A

**Goal**: H-min (miniversal unfolding) hypothesis verification = Theorem 3.2 Cat A.

**Approach**: 
- Hironaka algebraic strengthening of Sard (OP-H5-α, HIGH canonical)
- Equivariant transversality (Aut(G)-equivariant context)

**Deliverable**: Theorem 3.2 Cat A, Σ_T8 structure fully classified.

### §9.3 Priority 3 (continuous) — Cat A status verification

**Goal**: Re-check all status claims with strict canonical promotion pipeline.

**Note**: Cat A/B/C labels in this working file are *agent estimates*, NOT canonical declarations. Promotion requires SEAL event with explicit proof artifacts.

### §9.4 Anti-priority (DO NOT)

- Tier 3 Mostow injectivity (drop, replaced by Łojasiewicz-Simon)
- Tier 10 Gauge theory exotic detection (too speculative)
- 65/65 closure if H5 stays residual (focus on (I)-(IV) surjectivity, not injectivity, until concrete)

---

## §10. Verification

### §10.1 Critic-flagged issues resolved

| Critic finding | Resolution |
|---|---|
| #1 BE Γ_2 sign/normalization | §2.3 BGL convention adopted; ρ has Hessian eigenvalue dimension |
| #2 codim "open dense" premature | §3.4 Aut(G)-equivariant trivial-isotype restriction stated |
| #3 L-theory vs K_0 category error | §4.1 renamed L_K → R_K (representation ring) |
| #4 basin equivalence undefined | §4.2 Def 4.1 $\mathrm{Aut}(G)\wr S_K$ orbits |
| #5 Mostow analogy misleading | §6.1 dropped; §5.5 Łojasiewicz-Simon replacement |

### §10.2 Canonical-protection check

- canonical 0 edits ✓
- DECLARATION 0 edits ✓
- scc/ 0 edits ✓
- 새 framework letter 0 ✓ (W_SCC, l_SCC, Ṽ_SCC, R_SCC, R_K^SCC = Perelman + BGL + 표준 algebra 표기 의 *직접 적용*)
- silent OP resolution 0 ✓ (OP-H5-α/β/γ + OP-0008-σ 모두 *명시 reference*)
- CN10 disclosure 준수 ✓ (analogies, not instantiations)

### §10.3 Cat status sanity check

- Cat A 등록 claim 0 ✓ (모든 Cat A 는 *기존 canonical* 참조만)
- Cat B target claim 1: Corollary 7.1 distance-controlled Poincaré gap (post Łojasiewicz)
- Cat C synthesis claim: Master Theorem §7.1
- Cat D speculative: Tier 5, 6, 9-12

### §10.4 Promotion pipeline compatibility

본 working file 가 canonical/auxiliary_structures_master.md §8.2 의 H5 row 의 *frontal-attack candidate paths* 으로 등록 가능:
- "H5 residual = CD curvature degeneracy on Σ_T8 Whitney stratum, recommended attack: Tier 1 (Lemma 2.4 Łojasiewicz) + Tier 2 (H-min H-iro)"

별도 SEAL 시 본 file 의 Lemma 2.4 + Corollary 7.1 이 Cat B 후보로 canonical promotion 가능.

---

## §11. Closing

### §11.1 본 session 의 *진짜 산출물*

1. **14-tier palette 정밀 매핑** (§1 quick reference + §2-6 정밀)
2. **Critic 검토 통과 corrections** (§10.1)
3. **Master synthesis theorem (Cat C)** (§7.1)
4. **One concrete new claim (Cat C → Cat B target)**: distance-controlled Poincaré gap $\lambda_1 \geq c_G \cdot \mathrm{dist}(\Theta, \Sigma_{T8})$ (Corollary 7.1)
5. **17 gaps 우선순위** (§8)
6. **Priority 1 next-session entry point** (§9.1, 3-세션 ETA Cat B)

### §11.2 H5 정면 돌파의 진정한 모양

본 working file 이 보여주는 것:
> **H5 는 "객체가 발생하는 순간의 수학적 도구의 본질적 깨짐" 이지만, 이 깨짐은 *내재적으로 분류 가능* 하다 — Bakry-Émery CD curvature 가 Whitney-stratified codim-(k(k+1)/2-1) 박막 위에서 정확히 vanish 하는 형식.**
>
> **H5 정면 돌파는 *그 박막을 제거하는* 것이 아니라 *그 박막을 정확히 분류하는* 것. 본 synthesis 가 그 분류의 첫 줄.**

### §11.3 Slogan

> **"SCC 에너지장의 형태"는, 4-tier 결합 framework (BE bulk curvature + Σ_T8 Whitney stratification + R-rep surgery algebra + CN-COB assembly closure) 안에서, *정확히 한 점에서 깨지는* — 그 한 점이 H5 = Goldstone direction CD curvature 0. 이 깨짐의 *위치 + 차원 + 알고리즘적 obstruction class* 가 모두 결정됨. *우회는 H5'(regime restriction). 정면 돌파는 distance-controlled $\lambda_1 \geq c_G \cdot d$ + Whitney stratum k-dim 분류*. 본 working day 의 *진짜 첫 번째 정리* = Corollary 7.1.**

---

## §12. References

### §12.1 SCC canonical (CV-1.18, 2026-05-19)
- T14 (Cat A) — gradient flow convergence Łojasiewicz
- T-PF-A1-AR / SDE / GI / PE (Cat A) — Langevin reflected SDE + Gibbs + Poincaré-PE
- SB7 (Cat A, L2495-2510) — Σ_Hess = Σ_T8 codim-1
- T8-Core (Cat A) — phase transition
- T-V5b-T / V5b-T-zero (Cat A, L1328) — Goldstone exact zero
- T-σ-Theorem-3 (Cat A) — Aut(G)-equivariant Hessian decomposition
- T-PERSIST-1B-UNCONDITIONAL (Cat A, L2063) — Kupka-Smale + Sard 이미 배치
- T-Temporal-Identity (Cat A, CV-1.13) — 4 parts persistent identity
- T-OP6-B (Cat A) — boundary equivalence d_H ≤ 2√(α/β)
- T-CC-StableK-Kernel (Cat B, CV-1.17)
- L-HMORSE-LOCAL (Cat B, CV-1.16) — P4 closure target
- CV-1.18 SEAL §N — T_* ξ resident formal entry
- AUX-1.5 §7 (CN-COB) + §8 (D/A/P classification)
- 02_H5_morse_spinodal.md (2026-05-19) — H5 deep-attack predecessor

### §12.2 External literature
- Bakry, Gentil, Ledoux (2014) — *Analysis and Geometry of Markov Diffusion Operators*. Springer. §1.11, §1.16 (Γ_2 + CD convention), §4.2 (Poincaré-CD), §4.7 (boundary)
- Otto, Villani (2000) — Wasserstein gradient flow / log-Sobolev
- Lions, Sznitman (1984) — reflected SDE
- Sard (1942) — critical values measure zero
- Hironaka (1964) — resolution of singularities
- Arnold (1972) — degenerate critical points normal forms
- Whitney (1965) — Whitney conditions
- Mather (1970) — topological stability notes
- Crandall, Rabinowitz (1971) — bifurcation from simple eigenvalues
- Golubitsky, Guillemin (1973) — Stable mappings and their singularities, Ch. VI
- Bochnak, Coste, Roy (1998) — Real algebraic geometry
- Browder (1972) — Surgery on simply-connected manifolds
- Wall (1970) — Surgery on compact manifolds
- Ranicki (2002) — Algebraic and geometric surgery
- Davis, Lück (1998) — Assembly map machinery (Farrell-Jones)
- Loday (1976) — Algebraic K-theory assembly
- Bott (1954) — Non-degenerate critical manifolds (Morse-Bott)
- Mostow (1968) — *Strong Rigidity of Locally Symmetric Spaces* (NOTE: dropped per Critic #5)
- Łojasiewicz (1963) — Łojasiewicz inequality / Łojasiewicz-Simon convergence

---

*End of working file. Session 2026-05-20 (W8-Day3). canonical_version: CV-1.18 sealed 2026-05-19, untouched throughout. Next session entry: §9.1 Priority 1 — Lemma 2.4 Łojasiewicz step with explicit $c_G$.*
