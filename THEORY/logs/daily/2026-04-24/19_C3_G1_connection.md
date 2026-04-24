# 19_C3_G1_connection.md — Formalization of C3-G1 Structural Connection

**Session:** 2026-04-24 (late)
**Origin:** 사용자 지적 — "C3-G1 연결점을 제대로 정식화 혹은 찾아 정리하고 진행해야겠음".
**Purpose:** G1 cluster 의 empirical discoveries (특히 Theorem 1 geometry-specific revision) 와 C3 cluster 의 structural 관계를 정식화. Subset 이상의 conceptual connection 정립.
**Depends on:** `17_post_C2_open_digest.md` (C3 cluster 정의), `18_G1_results.md` (G1 결과), `02_development.md` §5 (Theorem 1 original), `04_orbital_proofs.md` §3 (Lemma 3).

---

## §1. 문제 식별 — 왜 연결 정식화가 필요한가

### 1.1 기존 관점

기존 분류 (per `17_post_C2_open_digest.md`):
- **C3 cluster**: "Goldstone & Spectral Verification", 11 OPs
- **G1 = "next-session priority subset"**: 5 immediate tractable NQs (NQ-128, 137, 141, 129, 131)
- 관계: G1 ⊂ C3, 단지 우선순위 partition

### 1.2 G1 analysis 후 발견된 structural gap

`18_G1_results.md` 의 결과:
- **Theorem 1 이 geometry-specific** 임이 empirically 증명됨 — 3 cases: torus / off-center / center-aligned
- 각 case 가 **서로 다른 mechanism** 를 produce (exact Goldstone / pseudo-Goldstone / genuine orbital)
- C3 의 모든 OP 가 이 3 cases 중 **어느 것에 속하는지** 명시 안 됨

즉 **C3 는 내부 구조를 갖는다**: geometric case 별로 sub-cluster 존재. G1 analysis 가 이 sub-structure 를 발견 했지만 전체 C3 에 소급 정리 안 됨.

### 1.3 연결 정식화의 목표

1. **Geometric classification** 을 C3 전체에 적용
2. 각 C3 OP 가 어느 geometric case 에 속하는지 mapping
3. **Case-specific 정리 / 이론** 명시
4. **Unified / disparate** 내용 구분

이것이 본 파일의 작업.

---

## §2. Core principle — Geometric Taxonomy of Low-Lying Hessian Modes

### 2.1 원칙 선언

> **Geometric Taxonomy Principle (formalized, 2026-04-24 G1):** For any Morse-index-0 local minimum $u^* \in \Sigma_m$ of full SCC energy on graph $G$, every low-lying Hessian eigenmode $\phi_k$ (with $\lambda_k$ below the first "orbital band" break) belongs to **exactly one** of three categories, determined by the pair $(G, u^*)$'s geometric type:
>
> (T) **Translation Goldstone** — $\phi_k$ is a translation-derivative mode $\delta u_x, \delta u_y$ (or linear combination). Eigenvalue $\lambda_k = O(\exp(-d_*/\xi_0))$ on finite graphs with translation pseudo-symmetry, or $\lambda_k \approx 0$ exactly on torus (up to Peierls-Nabarro lattice correction).
>
> (O) **Genuine Orbital** — $\phi_k$ is an orbital excitation intrinsic to $u^*$'s formation structure (Fiedler-like mode, quadrupole, etc.) with eigenvalue $O(\beta)$ (not exponentially small). Applies when translation symmetry is either absent or trivially "already broken by being at $\Gamma$-fixed point".
>
> (M) **Multi-peak Inter-formation** — $\phi_k$ is a mode coupling multiple formations in multi-peak $u^*$ (F≥2). Not a single-formation mode; involves amplitude/phase between different lobes.

### 2.2 Geometric case table

| Graph type | $u^*$ position | Stab$(u^*)$ | Goldstone exists? | Case |
|---|---|---|---|---|
| Torus $T_L$ | any | trivial (generically) | **Yes exact** (up to PN) | **(T) exact** |
| Free-BC $L\times L$ | off-center | $\mathbb{Z}_2$ or smaller | Yes pseudo | **(T) pseudo** |
| Free-BC $L\times L$ | center-aligned | $D_4$ | No | **(O) center** |
| Any | multi-peak (F≥2) | depends on peak arrangement | per-peak varies | **(M)** |

**Case (T)**: 낮은 (near-zero) 첫 eigenvalue 로 확인. 추가 orbital modes 가 Goldstone 위에 쌓인 구조.
**Case (O)**: 모든 low-lying modes 가 genuine orbital. eigenvalue scale $O(\beta)$.
**Case (M)**: Inter-peak coupling 이 multi-peak spectrum 의 주요 feature.

### 2.3 Consequences

- **단일 minimizer $u^*$ 마다 하나의 case 결정**. 단, overlap 가능 (e.g. off-center multi-peak = (T)+(M)).
- 각 case 는 **서로 다른 verification question** 을 야기.
- 각 case 별로 Theorem 1 의 **다른 version** 이 적용.

---

## §3. C3 OP 의 case-based 재분류

### 3.1 Case (T) torus — exact Goldstone
- **NQ-131** (torus Goldstone verification) — core case (T) test
- **NQ-161** (신, G1 발생) — torus direct numerical verification
- Theorem 1 revised, case (a)
- Related: Peierls-Nabarro lattice correction theory

### 3.2 Case (T) off-center — pseudo-Goldstone
- **NQ-130** (boundary-touching Mode 0) — case (T) off-center at boundary
- **NQ-162** (신, G1 발생) — off-center bulk pseudo-Goldstone scaling verification
- **NQ-129** partial (Goldstone scaling fit) — pending off-center data
- Theorem 1 revised, case (b)
- Lemma 3 (Goldstone-saturation) directly applies

### 3.3 Case (O) center-aligned — genuine orbital
- **NQ-128** L=16 F=1 test (G1 resolved: λ_0 = 25.27 confirmed genuine orbital)
- **NQ-136** (Pöschl-Teller shell Schrödinger) — 이 case 에 대한 continuum prediction
- **NQ-137** (continuum vs finite-grid) — center-aligned case 에서 partial match
- **NQ-138** (D_4 mixing $(\xi_0/r_0)^k$) — center-aligned fine structure
- **NQ-144** ($\kappa_{\ell=1}^{D_4}$ exact) — Lemma 3 의 center-aligned version **사용 불가** (Goldstone 없음) — **revised application needed**
- **NQ-146** (ℓ ↔ irrep map) — **universal** (all cases)

### 3.4 Case (M) multi-peak inter-formation
- R23 data 전체 (F≥5) 가 이 case
- **NQ-141** (σ ↔ orbital taxonomy via R23) — case (M) 에서 Cat A verified
- **NQ-163** (신, G1 발생) — multi-peak Mode 0 의 "각 formation 의 local Goldstone" decomposition
- **NQ-143** (F-tie convention) — $\mathcal{F}$ counting for multi-peak
- σ-framework in Axiom S1' v1 — case (M) 에서 가장 rich

### 3.5 모든 case 에 universal
- **σ definition** (Axiom S1' v1): 모든 case 에서 well-defined
- **Lemma 1** (irrep decomposition): 모든 case
- **Lemma 2** (nodal count): 모든 case
- **NQ-146** (ℓ ↔ irrep): 모든 case
- **Theorem 2** (pre-objective disk non-criticality): 모든 case 에서 F=1 → F≥2 (universal)

---

## §4. Case-specific 정리 요약

### 4.1 Case (T) exact torus
**Theorem 1-T (exact Goldstone, Cat C pending):**
$$H(u^*) \delta u_x = 0 \text{ exactly (up to Peierls-Nabarro)}$$

Eigenvalue scaling: $\lambda_0 \sim \exp(-\pi^2 r_0/\xi_0)$ (PN barrier, Frenkel-Kontorova-like).
- **Status**: Cat C, needs NQ-131 / NQ-161 direct numerical test on R18-style torus experiment.
- **Verification path**: Torus F=1 minimizer Hessian spectrum check.

### 4.2 Case (T) off-center — pseudo-Goldstone
**Theorem 1-Toff (pseudo-Goldstone, Cat B):**
$$\langle \delta u_x, H \delta u_x\rangle = O(e^{-d_*/\xi_0})$$

- **Status**: Cat B sketched (02_development.md §5). Needs off-center direct test (NQ-162).
- **Lemma 3** (Goldstone-saturation) **applies**: $\rho_{\ell=1} \geq \kappa$ with $\kappa = 6\sqrt{\pi c \alpha/\beta}/L$ (NQ-144 Cat A).

### 4.3 Case (O) center-aligned
**Theorem 1-O (no Goldstone, genuine orbital, Cat A empirical):**
$$\lambda_0 = O(\beta), \text{ not near-zero}$$

At D_4-center F=1 disk: low-lying modes are Fiedler-like E irrep + subsequent $D_4$ irreps.

- **Status**: Cat A empirical (G1 L=16 direct test: λ_0 = 25.27).
- **Pöschl-Teller prediction**: $\lambda_{n=0, \ell} = \beta + 4\alpha(\ell^2 - 1/4)/r_0^2$ (NQ-136 Cat A) — order of magnitude match (15-20% correction).
- **Irrep labeling**: NQ-146 Cat A provides ℓ ↔ irrep map.

### 4.4 Case (M) multi-peak
**Theorem 1-M (multi-peak spectrum, Cat B):**

R23 data empirically shows:
- Mode 0 "p-dominant" (ℓ=1 multipole) 가 Majority (76/324 observations)
- **No single universal statement** — spectrum 은 F 값, 배치, 에너지 basin 에 의존

**Per-peak Goldstone**: 각 local formation 이 own translation pseudo-Goldstone 을 보유. 이들이 total spectrum 의 low end 를 구성.
**Inter-peak coupling**: Peak 간 distance $d_{jk}$ 에 따라 coupling strength 변화.

- **Status**: Cat B sketched. NQ-163 으로 formalization.
- **R23 empirical content**: σ-taxonomy (NQ-141 Cat A).

### 4.5 Universal (모든 case)
**Theorem 2 (Pre-Objective, Cat A):** F=1 disk 가 full SCC 하에 destabilize → F≥2 multi-peak attractor. 모든 geometry case 에서 valid (Theorem 2-G).

**σ-signature**: 모든 case 에서 (F; {(n_k, [ρ_k], λ_k)}) 로 정의 가능.

---

## §5. 정식화된 C3-G1 connection

### 5.1 Structural statement

> **C3-G1 Connection Theorem (meta, 2026-04-24):** The C3 cluster decomposes under the Geometric Taxonomy (§2) into 4 sub-clusters + universal:
> - C3-T (torus exact): NQ-131, NQ-161
> - C3-Toff (off-center pseudo): NQ-130, NQ-162, NQ-129
> - C3-O (center-aligned orbital): NQ-128, NQ-136, NQ-137, NQ-138, NQ-144
> - C3-M (multi-peak): NQ-141, NQ-143, NQ-163
> - C3-Universal: NQ-146, Lemma 1, Lemma 2, Axiom S1' v1
>
> G1 (originally the "next-session priority subset") corresponds primarily to **C3-O verification + C3-M σ-taxonomy mapping**, with partial coverage of C3-Universal. The **case structure** was implicit in C3 and became explicit via G1 empirical discoveries.

### 5.2 NQ 재분배 summary table

| Sub-cluster | Members | Status | Immediate |
|---|---|---|---|
| **C3-T** (torus exact) | NQ-131, NQ-161 | 2 open | Needs torus numerical (R18-like) |
| **C3-Toff** (off-center pseudo) | NQ-129 partial, NQ-130, NQ-162 | 3 open | Needs off-center experiment |
| **C3-O** (center-aligned orbital) | NQ-128 ✓, NQ-136 ✓, NQ-137 ~, NQ-138, NQ-144 ✓ | 4 resolved + 1 open | NQ-138 needs scan |
| **C3-M** (multi-peak) | NQ-141 ✓, NQ-143, NQ-163 | 1 resolved + 2 open | Conceptual work |
| **C3-Universal** | NQ-146 ✓, σ-framework ✓ | Fully resolved | — |

Total C3: 7 Cat A resolved (including theory-only 14_*.md), 7 open.

### 5.3 G1 의 true contribution

G1 이 단순 "C3 의 일부" 가 아니라:
1. **3-geometry taxonomy discovery** (C3-T / C3-Toff / C3-O distinction)
2. **C3-O direct verification** (L=16 F=1 at center, Theorem 1 revised)
3. **C3-M empirical σ-taxonomy confirm** (NQ-141 Cat A)
4. **C3-Toff expectations** (scaling not observed at center, matches revision)

이 4 기여가 C3 전체의 재조직을 강제. "G1 resolved 4 NQs" 보다 "G1 transformed C3's internal structure" 가 더 정확한 표현.

---

## §6. 남은 작업 — case 별 agenda

### 6.1 C3-T (torus exact) — NQ-131 + NQ-161
**Minimum deliverable**: Torus F=1 minimizer 의 Hessian spectrum 직접 계산 (R18-like experiment).
**Script needed**: `phase_C3T_torus_goldstone.py`
**Expected outcome**:
- $\lambda_0 \leq 10^{-6}$ if exact Goldstone present
- Ratio $\lambda_0 / \lambda_1$ very small
- Verification of Peierls-Nabarro correction formula

### 6.2 C3-Toff (off-center pseudo) — NQ-130 + NQ-162
**Minimum deliverable**: Free-BC $u^*$ enforced off-center, Hessian spectrum + $d_*$ scan.
**Script needed**: `phase_C3Toff_offcenter_scaling.py`
**Expected outcome**:
- $\log \lambda_0 = c - d_*/\xi_0$ linear fit (Theorem 1 case (b))
- Slope ≈ -1 confirmation

### 6.3 C3-O (center-aligned orbital) — NQ-137 + NQ-138
**NQ-137** partial completed. **NQ-138** D_4 mixing $(\xi_0/r_0)^k$ 정량 — 작은 L 에서 관찰, 큰 L 에서 소멸.
**Deliverable**: Center-aligned L sweep Hessian + angular multipole power measurements.
**Script**: `phase_C3O_D4mixing_scan.py`

### 6.4 C3-M (multi-peak) — NQ-163
**Deliverable**: Multi-peak "per-formation Goldstone" concept 의 formalization.
**Theoretical**: 각 peak 주변 local translation 의 spectral contribution.
**Test**: R23 multi-peak modes 의 decomposition (각 peak 위에 local $\partial u$ 모드 기여).

### 6.5 C3-Universal
Remaining: **NQ-143** (F-tie convention) — σ definition 의 strict-max vs plateau-max 처리.

---

## §7. 다음 세션 권고 — case-based priority

### 7.1 Highest priority (single ~5 hour session)

**Case (T) exact torus numerical test**:
- Script: `phase_C3T_torus_goldstone.py`
- Verify: $\lambda_0 \ll \lambda_1$ at torus F=1 minimizer
- Verify: Peierls-Nabarro scaling $\lambda_0 \sim \exp(-c\xi_0^{-1})$
- Expected result: **Theorem 1-T (exact case) Cat C → Cat A**

**Case (T) off-center numerical test**:
- Script: `phase_C3Toff_offcenter_scaling.py`
- Free-BC grid with disk **forced off-center** via initial condition constraint
- Scan $d_*$ from near-boundary to near-center
- Verify: $\log \lambda_0$ linear in $d_*/\xi_0$
- Expected result: **Theorem 1-Toff (pseudo-Goldstone) Cat B → Cat A**

두 experiment 합쳐 **Theorem 1 의 전체 3 cases 가 Cat A** 도달 가능.

### 7.2 Medium priority

- NQ-138 ($D_4$ mixing) Cat B → Cat A via L-scan
- NQ-163 multi-peak per-formation decomposition (theory)
- NQ-143 F-tie convention (conceptual)

### 7.3 Long-term
- NQ-148 (σ-jump) — connects to N-1.A
- C1' cluster (σ-depth)

---

## §8. Theoretical synthesis — Unified Theorem 1

C3-G1 connection 정식화의 결과로 Theorem 1 을 unified form 으로 재작성:

> **Theorem 1 (Unified, post-G1-formalization):**
> Let $u^* \in \Sigma_m$ be a Morse-index-0 local minimum of $\mathcal{E}$ (full SCC, $b_D=0$) with boundary distance $d_* \geq L/4$ and $\mathcal{F}(u^*) = 1$ (single formation). Define $\xi_0 = \sqrt{\alpha/\beta}$.
>
> Let $\mathcal{G}(u^*)$ denote the **geometric class** of $u^*$:
> - $\mathcal{G} = T$ (torus) if $G = (\mathbb{Z}/L)^2$ with periodic BC
> - $\mathcal{G} = T_\text{off}$ if $G$ is free-BC and $u^*$ is off-center (Stab$(u^*) \subsetneq \text{Aut}(G)$)
> - $\mathcal{G} = O$ if $G$ is free-BC and $u^*$ is center-aligned (Stab$(u^*) = \text{Aut}(G)$ at a fixed point)
>
> Then the lowest non-trivial Hessian eigenvalue $\lambda_0$ satisfies:
> $$\lambda_0 = \begin{cases}
> O(\exp(-c_\text{PN}\xi_0^{-1})) & \mathcal{G} = T \text{ (Peierls-Nabarro)} \\
> O(\exp(-d_*/\xi_0)) & \mathcal{G} = T_\text{off} \text{ (pseudo-Goldstone)} \\
> \lambda_0^\text{PT}(\beta, \alpha, r_0, \ell_1) + O((\xi_0/r_0)^2) & \mathcal{G} = O \text{ (genuine orbital)}
> \end{cases}$$
>
> where $\lambda_0^\text{PT}$ is the Pöschl-Teller spectrum (NQ-136 Cat A). Case $T$ and $T_\text{off}$ produce Goldstone-like behavior; case $O$ produces genuine orbital spectrum.

**Cat 분류 (post-G1)**:
- $\mathcal{G} = O$: **Cat A** (G1 L=16 empirical + Pöschl-Teller theory)
- $\mathcal{G} = T$: Cat C (needs torus test, NQ-131/161)
- $\mathcal{G} = T_\text{off}$: Cat B (needs off-center test, NQ-130/162)

→ **Theorem 1 의 현재 status: 1/3 Cat A + 1/3 Cat B + 1/3 Cat C**. 다음 세션에서 $T, T_\text{off}$ 둘 다 Cat A 로 승급 가능.

---

## §9. C3-G1 connection 의 이론적 의의

### 9.1 SCC ontology 에 대한 함의

**Geometric taxonomy** 가 **SCC 의 "pre-objective" 해석에 새 차원** 제공:
- Torus 같은 homogeneous substrate 위 pre-objective formation 은 **translationally degenerate** (exact Goldstone)
- 유한 substrate 위 formation 은 **substrate-localized** (pseudo-Goldstone 또는 genuine orbital)
- Multi-peak 은 **per-peak local pre-objective** 의 결합

이것이 canonical CN 7 (dual-mode self-referentiality) 의 geometric instantiation 의 첫 formal statement. **SCC 의 pre-objective character 가 graph topology 의 구체적 구조 와 interacting 하는 mechanism**.

### 9.2 N-1 reframe 에의 연결

`05_orbital_essence.md` 의 N-1 reframe ("bug → feature: emergence 가 orbital 본질") 과 연결:
- 연속에서 이산 emergence 의 character 는 geometric case 에 따라 다름
- Case (T): **degenerate emergence** (Goldstone band)
- Case (O): **rigid emergence** (orbital spectrum discrete)
- Case (M): **composite emergence** (per-peak + coupling)

이 셋이 σ-framework 의 **mode 구성의 다양성** 을 설명. σ 의 richness 가 universal 하지 않고 geometric case 에 따라 풍부함이 다름.

---

## §10. Summary — 정식화 완료

### 10.1 달성된 formalization

1. **Geometric Taxonomy Principle** 명시화 (3 cases: T / O / M)
2. **C3 의 case-based 재분류** (4 sub-clusters + universal)
3. **Theorem 1 unified form** — 3 cases 통합
4. **G1 의 true contribution** = C3 transformation, not subset
5. **Case-별 verification agenda** 명시

### 10.2 Next-session immediate priority

**Case (T) + Case (T_off) numerical verification**:
- Torus F=1 Goldstone (NQ-131/161)
- Off-center pseudo-Goldstone (NQ-130/162)

두 experiment 가 Theorem 1 의 나머지 2 cases 를 Cat A 로 승급 → **Theorem 1 전체 Cat A**.

### 10.3 Long-range

C3-M (multi-peak) formalization 이 σ-framework 의 가장 rich branch. N-1.B (transition path dynamics) 와 연결. 이것이 후속 multi-session project.

**End of 19_C3_G1_connection.md.**
