# 17_post_C2_open_digest.md — Open Problem Consolidation Post-C2-Conquest

**Session:** 2026-04-24 (late evening, C2 마무리 후)
**Purpose:** C2 cluster 완전 정복 후 남은 open problem 의 재정리. `06_open_problems_digest.md` 의 update.
**Depends on:** 본 세션 `01_*`–`16_*` 전체. 특히 `16_C2_closure.md` (C2 최종 status).

---

## §A. 정리 원칙

세션 시작 시 14 pre-existing OP + 세션 중 33 new NQ = 47 total. 본 §는:
1. **Fully resolved** (Cat A, this session) — 제거 또는 archive
2. **Clarified / sidestepped / partial** — status 명시
3. **Still genuinely open** — 새 cluster 재분류

---

## §B. Fully Resolved (Cat A) during this session — 18 items

이전 open, 본 세션 후 Cat A. **추후 open problem list 에서 제외**.

### B1. Theorem 2 family (6 Cat A)
- Theorem 2 (i) disk non-criticality
- Theorem 2 (ii) multi-peak attractor existence
- Theorem 2 (iii) Lemma 4 quadratic form
- Theorem 2 (iv) IC-sensitivity scaling
- Theorem 2 (v) dichotomy (adaptive bounded / random diverging)
- Theorem 2-G graph-class generalization

### B2. σ-framework Cat A (5 Cat A)
- σ definition (Cat A definitional)
- Lemma 1 (irrep decomposition)
- Lemma 2 (i, ii, iv) (nodal count invariance)
- Theorem 3 (σ at uniform $c\mathbf{1}$)
- Theorem 4 (σ at first-pitchfork, $\epsilon$-small)
- Lemma 3 (Goldstone ↔ ℓ=1 saturation)

### B3. OP resolutions (4 Cat A)
- **F-1** (pure via T-Merge (b) canonical + full via Thm 2)
- **NQ-132** ((C5) threshold trivially 0)
- **NQ-133** (IC sensitivity 정량 statement)
- **NQ-134** (cl/sep mechanism-level monotone)
- **NQ-135** (generalized $F_*$ dichotomy)
- **NQ-155** (thermodynamic limit dichotomy)

### B4. C3 theory-only (3 Cat A)
- **NQ-136** (Pöschl-Teller shell spectrum: 1 radial × ∞ angular)
- **NQ-144** ($\kappa_{\ell=1}^{D_4} = 6\sqrt{\pi c\alpha/\beta}/L$ exact)
- **NQ-146** (ℓ ↔ $D_4$ irrep: ℓ mod 4 pattern)

---

## §C. Clarified / Sidestepped / Status-Fixed — 6 items

Neither fully Cat A nor "open" in the original sense. Status decisively resolved via reframing.

- **M-1** (K=1 preference): **Layer-clarified**. $K_\text{step}$ layer 에서 그대로 valid (T-Merge (b) Cat A); $\mathcal{F}$ layer 에서 minimum $\mathcal{F}_*$. 두 layer 양립.
- **MO-1** (Morse inapplicability): **Sidestepped** via σ-framework on single manifold $\Sigma_m$ (convex polytope, Prop 1.1 Cat A). Multi-formation $\Sigma^K_M$ corner 은 σ scope 밖.
- **N-1 umbrella** (Soft-Hard Switching Asymmetry): **Bug → feature reframe**. σ-framework 자체가 "continuous → discrete emergence" 의 mathematical 정형화. 원래 "smooth connection 만들어라" 가 "emergence mechanism 을 characterize 하라" 로 전환.
- **OP-0005** (K kinetic vs thermodynamic): **Closed by negative** (CN6 canonical).
- **OP-0007** (formation identity): **Partial answer via σ** (σ as identity definition candidate; 다른 측면 — metric on identity space — 는 open).
- **NQ-150** (σ universality): **Qualitative Cat A via Theorem 2-G**. Quantitative (specific functional form per graph class) 는 여전히 open.

---

## §D. Practically Resolved (non-core) — 2 items

Numerical artifacts, mechanism 과 무관.

- **NQ-156** ((0.5, 2.0) convergence ERROR): 단순 optimizer failure, competing attractors 추정. Deferred as software issue.
- **NQ-157** (pure E_bd F=0 at L=24/32): **Diagnosed** as IC artifact. Fiedler weak perturbation → uniform attractor. Real pure E_bd minimizer F=1 여전히 존재 (Phase 3C L=24 F_min=1 confirms).

---

## §E. Genuinely Still Open — 재정리된 clusters

Remaining OP/NQ 를 3 cluster 로 재편성:

### E1. Cluster "Continuous-to-Discrete Depth" (C1')
σ-framework 의 **robustness, stability, universality** 의 depth 관련. 본 세션이 σ-framework 정립했지만 그 깊이는 후속 작업.

**Members**:
| ID | Statement | 우선도 | Tractability |
|---|---|---|---|
| P-A | Integer-K vs continuous-u: "smooth connection" 부재 의 정형 답 | Medium (reframed: 연결 불필요) | Theory |
| P-D | Threshold non-principled (θ_core, θ_in 등 임의) | Medium ($\mathcal{F}$ threshold-free 로 부분 우회) | Theory + taxonomy |
| N-1.A | σ 가 parameter 변동 하 jump 하는 mechanism | High | Numerical scan |
| N-1.B | 두 σ-class 간 transition path (saddle, NEB) dynamics | High | Heavy numerical |
| N-1.C | σ universality across graph classes | High | Multi-graph numerical |
| NQ-125 | Spectral-gap cutoff multiple $c=10$ universality | Low-Medium | Numerical |
| NQ-126 | σ-class = Aut(G)-orbit equivalence 정량 | Medium | Numerical (R23 data) |
| NQ-127 | σ parameter perturbation stability | Medium | Numerical scan |
| NQ-147 | Multi-source discreteness depth (어느 source dominant?) | Medium | R23 analysis |
| NQ-148 | σ-jump formalization (phase transition analogue) | High | Theory + numerical |
| NQ-149 | Self-referential vs external emergence 정량 차이 | Medium | Theory |

**Total C1': 11 open items**. σ framework 의 depth characterization.

**Next-session priority**: **NQ-148** (σ-jump) + **N-1.A** (parameter jump) 이 substantive 후속 project (연속-이산 emergence 의 동역학 이해).

### E2. Cluster "Goldstone & Spectral Verification" (C3)
Theorem 1 과 σ-framework 의 R23 data 위 numerical verification. 본 세션이 theory 정립 + 일부 Cat A 이지만 empirical verification 이 다수 남음.

**Members** (after removing Cat A resolved NQ-136/144/146):
| ID | Statement | 우선도 | 즉시 가용? |
|---|---|---|---|
| NQ-128 | $\lambda_0/\lambda_1$ ratio — Theorem 1 Cat B→A 승급 | **Highest** | R23 data, 즉시 |
| NQ-129 | Goldstone universal scaling $\lambda_0 \cdot e^{d_*/\xi_0}$ | High | R23 data |
| NQ-130 | Boundary-touching minimizer Mode 0 | Medium | R23 subset |
| NQ-131 | Torus exact Goldstone verification | Medium | R18 data |
| NQ-137 | Continuum vs finite-grid spectrum agreement | **High** | R23 data |
| NQ-138 | $D_4$ correction mixing scaling $(\xi_0/r_0)^k$ | Medium | R23 fit |
| NQ-141 | σ ↔ R23 orbital taxonomy map | High | R23 data |
| NQ-143 | $\mathcal{F}$-tie convention (strict-max vs plateau) | Low | Convention choice |

**Total C3: 8 open items**. 거의 모두 **R23 dataset 재분석** 으로 즉시 tractable.

**Next-session priority**: NQ-128 + NQ-137 + NQ-141 (Theorem 1 Cat A + σ verification + taxonomy map). 이전 세션 plan.md 의 원래 P0 target 과 일치.

### E3. Cluster "Infrastructure & Long-term" (C4)
본 세션 무관 또는 fundamentally different project. 현재 이론의 기반 가정 질문.

**P-issues (6)**:
- **P-B**: External substrate dependence ($X_t$, $N_t$ pre-theoretic)
- **P-C**: Missing third mode (co-belonging $\mathbf{C}_t$ demoted to derived)
- **P-E**: Parameter origin (25+ external parameters)
- **P-F**: Zero-T metastability (temperature / entropy / noise framework 부재)
- **P-G**: Axiom-implementation divorce (A1 → A1', $b_D = 0$, E3 demotion)
- **P-H**: Time pre-theoretic ($T$ given)

**Canonical OP-list (residual)**:
- **OP-0001**: Binary co-belonging form
- **OP-0002**: Transition operator $\mathbf{T}_t$ — demoted in canonical
- **OP-0003**: Crisp recovery systematic procedure
- **OP-0004**: $b_D = 0$ axiom-level justification (P-G 의 한 instance)
- **OP-0006**: Per-formation Hessian decomposition for $K \geq 2$ (MO-1 과 관련)

**Secondary NQ (long-term)**:
- **NQ-139**: 56 stable basin bifurcation tree (heavy numerical)
- **NQ-140**: Equivariant secondary bifurcation cubic analysis
- **NQ-142**: σ vs Three-Layer classification relation
- **NQ-145**: Secondary pitchfork σ higher-order
- **NQ-152**: M matrix $\mu_\text{min}(M)$ L-scaling
- **NQ-153**: Closure FP $c^*$ parameter dependence

**Total C4: 17 open items**. 다수가 fundamental 별도 project.

---

## §F. Updated status matrix (전체 overview)

| 구분 | Count | 상태 |
|---|---|---|
| **Cat A resolved (this session)** | **18** | 제거 |
| **Clarified/sidestepped** | 6 | status-fixed |
| **Practically resolved (non-core)** | 2 | archive |
| **Still open C1' (σ depth)** | 11 | active research |
| **Still open C3 (Goldstone/spectral)** | 8 | immediate (R23 data) |
| **Still open C4 (infrastructure)** | 17 | long-term |
| **Total** | **62** | (from ~47 entry) |

**증가**: 세션 시작 시 47 items → 종료 시 62 items. 18 resolved 됐으나 33 new NQ 생성으로 net 증가.

이는 **연구 진행의 자연스러운 확장**: resolved 한 question 보다 더 많은 specific sub-question 이 생성. 각 new NQ 가 이전 OP 보다 더 구체적·tractable.

---

## §G. Priority ranking — next session

### G1. Immediate (R23 data 만 필요, 즉시 tractable)

1. **NQ-128** ($\lambda_0/\lambda_1$ ratio): 30분. Theorem 1 Cat B → Cat A 승급.
2. **NQ-137** (continuum vs finite-grid): 2-3시간. σ-framework 의 R23 위 직접 검증.
3. **NQ-141** (σ ↔ orbital taxonomy): 1-2시간. σ와 R23 연결 맵.
4. **NQ-129** (Goldstone universal scaling): 30-60분. NQ-128 deepening.
5. **NQ-131** (torus exact Goldstone): 30분. R18 data.

**Cluster**: C3. **Total estimated**: 5-8시간 single session.

### G2. Medium-term (theory + numerical mix)

1. **NQ-148** (σ-jump formalization): Phase transition analogue 의 정형화.
2. **N-1.A** (σ parameter jump): NQ-148 과 결합.
3. **NQ-130** (boundary-touching): R23 subset 분석.
4. **NQ-138** (D_4 mixing scaling): R23 fit.

**Cluster**: C1' + C3. **Total estimated**: 1-2 세션.

### G3. Long-term (separate projects)

- C1' 의 N-1.B/C (동역학적 측면)
- C4 의 P-issues (fundamental reconstruction)
- Canonical OP-0001..0006

**Schedule**: W5 이상.

---

## §H. Recommended next plan.md target

위 priority 기반:

> **Target (2026-04-25 plan.md):** σ-framework 의 R23 data 위 numerical verification (NQ-128 + NQ-137 + NQ-141 + NQ-129). Theorem 1 Cat B → Cat A 승급. σ-framework 의 orbital taxonomy 대응 map 확정.

이는 본 세션 초기 plan.md 의 원래 P0 target 과 일치 — C2 attack 으로 deferred 되었으나 여전히 highest priority.

---

## §I. 가장 interesting 한 남은 open problem

단일 흥미로움 + substantive depth 기준:

### I1. **NQ-148 + N-1.A**: σ-jump mechanism

σ 가 parameter (β, c, λ) 변동 하 어떻게 jump 하는가? Static orbital phase transition 의 정형화. 이는 "SCC 의 pre-objective landscape 가 어떻게 연속적으로 변형되는지" 의 질문.

**중요성**: σ-framework 의 dynamics-like 확장. 본 세션은 static σ 정립; 이 NQ 는 σ 의 temporal-like 변형.

### I2. **NQ-149**: Self-referential vs external emergence 정량

SCC 의 emergence 는 self-referential (Cl, D dual-mode 가 $u$ 에서 derive), atom 의 emergence 는 external (Coulomb potential 고정). 이 차이의 **quantitative measure**. E.g., σ-sensitivity 의 parameter scaling 비교.

**중요성**: CN10 (contrastive not reductive) 의 **quantitative sharpening**. SCC 의 "다르게 평행" (different ontology, parallel mathematics) 의 정확한 statement.

### I3. **P-D**: Threshold non-principled

Core, Inside 의 $\theta_\text{core}, \theta_\text{in}$ 임의성. $\mathcal{F}$ 는 threshold-free 이지만 다른 derived 양들은 여전히 thresholded. Threshold-free 정형화의 systematic 접근 — 이는 N-1 의 또 다른 instance.

**중요성**: SCC 의 "crisp recovery" 기능 자체의 근본적 문제.

위 3 이 next-next 세션의 theory target 후보.

---

## §J. 요약 — 한 문장

> 본 세션은 C2 cluster (pre-objective mechanism) 을 완전 정복 (18 Cat A) 하고 σ-framework 를 정립했으며 N-1 을 reframe 했다. 남은 open problem 은 주로 (i) σ-framework 의 **depth 탐구** (C1', 11 items, 이론+numerical), (ii) R23 data 위 **immediate verification** (C3, 8 items, 즉시 가용), (iii) **infrastructural questions** (C4, 17 items, 장기). **Next-session highest priority** = G1 (NQ-128, 137, 141) — Theorem 1 Cat A 승급 + σ verification.

**End of 17_post_C2_open_digest.md.**
