---
id: CV114-11-state-space-audit
type: working/audit
created: 2026-05-11
status: read-only audit; no canonical edit
scope: SCC state space definition — Package I–II, H-MORSE context
authority: read-only; quotes canonical/working at audit-time HEAD
parent: THEORY/working/CV114_H_MORSE_PACKAGEII/
---

# 상태공간 정의 감사 보고서

> **작업 모드.** 읽기 전용. canonical / hypothesis_tree / CHANGELOG / 기존 working source 어떤 파일도 수정하지 않았다. claim 승격/강등 수행하지 않았다. 본 파일은 CV114 entry audit 시리즈(`00..10`)의 후속 working note이며, contamination barrier 안쪽(working layer)에만 존재한다.
>
> **저장소 / HEAD.** `/home/user/Perception_theory/`, branch `claude/update-todays-work-sBSGv`, HEAD `c1faaf7 0511_done` (사용자가 명시한 `/home/jack/Perception_theory/`는 현 환경에 존재하지 않아 동일 git 저장소의 실제 경로에서 수행).
>
> **배경 질문.** H-MORSE를 현재의 Euclidean / constrained polytope 상태공간 위에서 해석할 것인가, 아니면 Riemannian 해석을 위해 상태공간 구조 자체를 바꿔야 하는가? 이 보고서는 그 결정을 위한 **선결 자료**이며, 결정 자체를 제안하지 않는다.

---

## 1. 요약

- **단일한 "상태공간"이라는 명칭은 없지만, 일차 작동 정의는 박스+볼륨 제약 폴리토프이다.** Canonical §8.0(line 666–668)이 $\Sigma_m = \{u \in [0,1]^n : \sum_x u_t(x) = m\}$로 정의하고, §13 Prop 1.1(Cat A, line 1558–1561)이 이를 "convex polytope, manifold with corners, contractible"로 격상한다. §3.9(line 242–250)는 같은 공간을 $\mathcal F_M(\mathcal P) = [0,1]^n \cap \{\sum \tilde u = M\}$로 부르며 "the correct foundational state space for SCC dynamics"라고 명시한다.
- **명칭은 셋, 객체는 사실상 하나.** $\Sigma_m$(§8.0, §13), $\mathcal F_M(\mathcal P)$ / $\mathcal F_M(G)$(§3.9, §13 T-PF-A1-AR), $\Omega = \Sigma_m \cap [0,1]^n$(observer_moduli/op_oms_018_regular_u_star.md:29) — 모두 $[0,1]^n \cap \{\mu^\top u = M\}$. CV114/01 §2(line 25–31)에 5층 hierarchy 표가 있다.
- **현재 이론은 Riemannian theory가 아니라 Euclidean projected variational + reflected polytope theory다.** §8.7(line 741–743)에 Shahshahani 메트릭이 "commentary"로 잠시 언급되지만 명시적으로 "implementation question, not a theoretical commitment"로 못 박혀 있다. Gradient/Hessian/projected gradient는 모두 표준 Euclidean inner product 기준이다(working/SF/sigma_m_hessian_convention_audit.md:31; working/C/F_group_axioms.md F3의 $\Pi_{\Sigma_m} = I - (1/n)\mathbf 1\mathbf 1^\top$).
- **Graph는 상태공간 metric이 아니라 energy의 항으로 들어간다.** §8.4(line 714)는 "$2\alpha v^T L v$ … Hessian contribution $4\alpha L$"로 명시한다. Graph Laplacian은 $\mathcal E_{\mathrm{bd}}$ 안의 quadratic form일 뿐, 상태공간의 metric tensor가 아니다.
- **Package I은 boundary/corner를 reflected SDE로 포섭한다 (Cat A).** §13 T-PF-A1-SDE(line 1643–1657): Lions–Sznitman (1984) Theorem 1 **convex case (ii) — no smooth boundary required**; $dK_t \in N_{\tilde C}(X_t)$ inward normal cone; uniform interior cone + uniform exterior sphere (T-PF-A1-AR, line 1634).
- **Package II는 같은 폴리토프 위에 metastability를 얹으려 하지만 H-MORSE / H5 / $T_*$ 모두 OPEN이다.** §13 T-P-F-ε0-K(line 1710 H5 statement, 1723 status Cat B); hypothesis_tree HT-3.5(line 168–184) "H-MORSE … Hessian $H(u^*)|_{T_{u^*}\Sigma_m}$ has $\mu_{\min} > 0$ (mod symmetry-zero eigenvalues)".
- **H-MORSE의 비퇴화성은 일관되게 $T_{u^*}\Sigma_m = \mathbf 1^\perp$ 위에서 요구된다 (interior, projected, Euclidean).** Counterexample 카탈로그(CV114/05) — cycle/torus Goldstone(V5b-T-zero), $D_4$-fixed center, T8-Full bifurcation parameter, $\partial\Sigma_m$ — 가 unconditional H-MORSE를 **provably false** 로 만들었고, 권장안은 strict interiority + trivial stabilizer + sub/super-critical window 하의 **H-MORSE-Local** (CV114/02 §8.A, line 119–132; CV114/09 §4 line 61–75).
- **Quotient(Aut(G)-orbit) 와 stratified-boundary 처리는 현재 부분적으로만 정의돼 있다.** Aut(G) 작용·orbital irrep 분해는 canonical 차원에서 Commitment 14(§11.1, line 888–891)와 §13 Theorem 1 orbital + Theorem 3.1(a) tangent decomposition(Cat A, line 1568–1571)으로 들어와 있지만, "quotient state space"라는 통합 정의는 없다. Stratified Morse / corner-aware framework는 working/E/MO1_dissolution.md과 CV114/05 §6 (Boundary critical point with active constraints, "stratified Morse required")에 등장하나 canonical은 strict interiority로 우회 중이다(observer_moduli/open_problems.md OP-OMS-027 OPEN "Regularity at Corners of $\Omega$").
- **판정.** CV-1.13 기준 SCC의 캐논 상태공간은 **Euclidean ambient $\mathbb R^n$ 안의 compact convex polytope** $[0,1]^n \cap \{\sum u_i = m\}$이며, 위에 reflected Langevin(Cat A, polytope corner 포함)이 정의되고, 변분 구조는 **Euclidean projected gradient/Hessian** 기준이다. Riemannian/quotient/stratified 해석은 모두 **명시적으로 부재 또는 commentary 수준**.

---

## 2. 발견된 정확한 정의들

### 2.1 Canonical §8.0 — 일차 운영 정의 ($\Sigma_m$)

`THEORY/canonical/canonical.md:666–668`
```
\Sigma_m = \Big\{u \in [0,1]^n : \sum_{x \in X_t} u_t(x) = m\Big\}
```
**해석.** Box constraint(요소별 $[0,1]$)와 volume constraint(합 = $m$)를 같이 포함한 형태. 보조 키워드 "constraint manifold"로 호명. 이것이 변분 문제(§8.1)의 작용 영역이다.

### 2.2 Canonical §13 Proposition 1.1 — 상태공간의 수학적 형(Cat A)

`canonical.md:1558–1561`
```
Proposition 1.1. Constraint Manifold Structure.
Σ_m is convex polytope, manifold with corners, contractible.
Status: Proved, Cat A.
```
**해석.** 캐논이 인정하는 가장 강한 구조적 주장. "manifold with corners"가 명시적이라는 점이 결정적 — 즉, smooth manifold가 아니라 polytope-with-corners.

### 2.3 Canonical §3.9 (D-ST-2 migrated, W6 D4) — "foundational state space"

`canonical.md:242–250`
```
F_0(P) = {ũ : P → [0,1]}
F_M(P) = {ũ ∈ F_0(P) : Σ ũ(x) = M}

F_M(P) is the correct foundational state space for SCC dynamics — the
manifold on which gradient flow and energy minimization are defined.
This replaces the K-field product manifold Σ_M^K ... as the foundational
space; Σ_M^K is a local coordinate chart within one energy basin
A_{K,α}(P), not the global state space.
```
**해석.** 명칭은 $\mathcal F_M(\mathcal P)$이지만 객체는 §8.0의 $\Sigma_m$과 동치. CV-1.6 이후 K-field product를 폐기하고 단일 폴리토프를 일차 상태공간으로 못 박았음.

### 2.4 Canonical §13 T-PF-A1-AR — affine reduction (Cat A)

`canonical.md:1627–1639`
```
F_M(G) = {u ∈ [0,1]^n : μ^T u = M}
... compact convex polytope of intrinsic dimension n−1 in H_M = {u : μ^T u = M}
(with at most 2n facets from box constraints u_i = 0 or u_i = 1).
... C̃ := {x ∈ R^{n-1} : u* + Qx ∈ [0,1]^n}.
The map Φ(x) = u* + Qx is an isometry (C̃, |·|) → (F_M(G), |·|).
C̃ is a compact convex polytope with nonempty interior, satisfying the
uniform exterior sphere condition and the uniform interior cone condition.
```
**해석.** "isometry"는 표준 Euclidean norm 기준 — 즉, **이미 metric은 Euclidean으로 못 박혀 있다.** UIC + 외부 sphere 조건은 reflected SDE를 위한 폴리토프 정규성.

### 2.5 Canonical §13 T-PF-A1-SDE — reflected Langevin (Cat A)

`canonical.md:1643–1657`
```
dX_t = −∇Ẽ(X_t) dt + √(2T_*) dB_t + dK_t,   X_0 ∈ C̃
dK_t pointing into the inward normal cone N_{C̃}(X_t).
...
dU_t = −Π_M ∇E_SCC(U_t) dt + √(2T_*) Π_M dW_t + dK̃_t
where Π_M = QQ^T projects onto H_0 and dK̃_t ∈ N_{F_M(G)}(U_t) within H_M.
Proof: ... Lions–Sznitman (1984, CPAM 37(4):511–537) Theorem 1, convex
domain case (ii) (no smooth boundary required).
```
**해석.** Reflected polytope이 **canonical 수준에서 Cat A로 등록**되어 있고, boundary/corner는 normal cone reflection으로 해결된다(다만 Lions–Sznitman convex case로 처리, Tanaka uniqueness).

### 2.6 Canonical §8.7 — 자연 기하 (Shahshahani, commentary only)

`canonical.md:741–743`
```
The constraint manifold Σ_m carries a natural information-geometric
structure. The Shahshahani metric, defined by g_{ij} = δ_{ij}/u_i, induces a
Riemannian structure under which the natural gradient differs from the
Euclidean gradient. ... Whether the natural gradient improves convergence
properties is an implementation question, not a theoretical commitment.
```
**해석.** 저장소 전체에서 발견되는 **유일한 Riemannian metric 언급**. 단 "commentary", "implementation question, not a theoretical commitment" 명문화. Fisher / Wasserstein / graph-Sobolev / operator-induced metric은 본 감사에서 발견되지 않았다.

### 2.7 Canonical §8.4 — graph Laplacian의 위치

`canonical.md:714`
```
For symmetric N_t, this equals 2α v^T L v where L is the graph Laplacian
and v = u_t − c·1, giving a Hessian contribution of 4α L.
```
**해석.** Graph Laplacian은 **에너지 $\mathcal E_{\mathrm{bd}}$ 안의 quadratic form**이며, **상태공간 metric tensor가 아니다.**

### 2.8 Canonical §16 D-ST-4 — topological sector (non-manifold)

`canonical.md:2005–2009`
```
B_K(P) = {ũ ∈ F_0(P) : K_act(ũ) = K} is the K-th topological sector — the
set of all fields with exactly K persistent components. It is not a
manifold; it is a topological stratum of F_0(P).
```
**해석.** Multi-K decomposition은 명시적으로 stratified, "not a manifold". 단 SCC의 dynamics/Gibbs measure는 $\mathcal F_M$ 위에서 정의되고, $\mathcal B_K$는 그 위의 보렐 분할로 들어간다(see T-K-Select-PF, line 1474).

### 2.9 Canonical §13 Theorem 3.1(a) — 접공간 분해 (Cat A)

`canonical.md:1568–1571`
```
Theorem 3.1(a,b,d).
(a) Tangent space decomposes T = T_intra ⊕ T_transfer.
(b) Intra-formation Hessian PD.
(d) Symmetric point has μ_1 = μ_2, is critical on Σ_M^{relax}.
Status: Proved, Cat A.
```
**해석.** 캐논 수준의 접공간 분해는 $K=2$ 대칭점에서만 분해된다(intra/transfer). 일반 점의 $T_{u}\Sigma_m = \mathbf 1^\perp$ 정의는 §11.1 fixed commitment(Commitment 14 §3 안에서 사용)와 CV114/02 §6 line 91, working/SF/sigma_m_hessian_convention_audit.md line 31에서 명시.

### 2.10 working/SF/sigma_m_hessian_convention_audit.md — 두 Hessian convention

`THEORY/working/SF/sigma_m_hessian_convention_audit.md:27–32`
```
§2.1 Σ_m-projection conventions to test
Convention I (centered/intrinsic): project gradient + Hessian onto tangent
simplex T_u Σ_m = {v ∈ R^n : Σ_i v_i = 0}. Equivalently, subtract the mean.
Convention II (Lagrange multiplier extrinsic): H − λ Id_⊥ ...
```
**해석.** Hessian projection이 **명시적으로 Euclidean orthogonal projection** 으로 처리됨. 두 convention 사이의 audit이 활발한 working 이슈.

### 2.11 working/C/F_group_axioms.md §3 — projected SDE 형태

`THEORY/working/C/F_group_axioms.md` §3.1
```
du(t) = −Π_{Σ_m} ∇F[u(t)] dt + √(2T) Π_{Σ_m} dW(t)
Π_{Σ_m} = I − (1/n) 1 1^T is the orthogonal projector onto T_u Σ_m.
additional reflection condition at ∂[0,1]^n ∩ Σ_m corners ...
```
**해석.** Projector가 **표준 Euclidean orthogonal** (1/n 정규화). Reflection은 corner까지 포함. 단 이 파일의 "Cat A on Σ_m^ε"는 W6 이전 working으로, canonical T-PF-A1-SDE에 의해 대체됨(CHANGELOG line 2001).

### 2.12 observer_moduli/op_oms_018_regular_u_star.md — $\Omega$ 표기

`THEORY/working/observer_moduli/op_oms_018_regular_u_star.md:29–31`
```
Ω := Σ_m ∩ [0,1]^n = {u ∈ R^n : 1^T u = m, 0 ≤ u_i ≤ 1}.
Ω is a compact convex polytope of dimension n − 1 (with corners)
```
**해석.** $\Omega = \Sigma_m \cap [0,1]^n$ 표기는 observer_moduli working 파일들의 표준. 본 파일에는 R1(interior nondegenerate), R2(boundary fixed active set + KKT + strict complementarity), corner cases(미해결, OP-OMS-027)이 분리되어 있다(line 78–79).

### 2.13 observer_moduli/open_problems.md OP-OMS-027 — corner regularity 미해결

`THEORY/working/observer_moduli/open_problems.md:520–545`
```
OP-OMS-027 — Regularity at Corners of Ω = Σ_m ∩ [0,1]^n
... a corner of Ω where many box constraints are simultaneously active ...
Open
```

### 2.14 CV114/02_H_MORSE_statement_reconstruction.md — H-MORSE의 영역

`THEORY/working/CV114_H_MORSE_PACKAGEII/02_H_MORSE_statement_reconstruction.md:13`
```
Every critical point of the SCC energy E on the volume-constrained polytope
Σ_m, relevant to metastable transitions, is a nondegenerate critical point
in the Morse sense — its constrained Hessian has no zero eigenvalues other
than those forced by structural symmetry.
```
같은 파일 line 23–35:
```
F_M(P) = [0,1]^n ∩ Σ_m  Field space — closed cube intersected with volume hyperplane
Σ_m^∘                    Interior (strict inequalities 0 < u_i < 1)  Interior critical points (canonical scope)
...
For CV-1.14 H-MORSE entry, the primary domain is Σ_m (single-formation polytope, K=1).
The boundary ∂Σ_m consists of faces where u_i ∈ {0,1}. Critical points on
the boundary require stratified Morse (Goresky-MacPherson) treatment.
CV-1.14 should restrict to interior critical points u* ∈ Σ_m^∘ unless
explicitly stated.
```

### 2.15 Hypothesis Tree HT-3.5 — H-MORSE 진술

`THEORY/canonical/hypothesis_tree.md:168–184`
```
[H-MORSE] Morse 안정성  MAJOR OPEN (Phase 2)
∀ critical point u* of E on Σ_m,
Hessian H(u*)|_{T_{u*}Σ_m} has μ_min > 0 (mod symmetry-zero eigenvalues)
```

---

## 3. 상태공간의 층위

저장소 근거에 기반한 7층 분류(canonical + working 파일 명시):

| 층위 | 객체 / 표기 | 캐논 정의 위치 | 캐논 지위 |
|---|---|---|---|
| **L0. raw field space** | $\mathcal F_0(\mathcal P) = \{u : \mathcal P \to [0,1]\}$ = $[0,1]^n$ | §3.9 line 244 | Cat A definitional |
| **L1. volume-constrained** | $H_M = \{u : \mu^\top u = M\}$ 또는 $\{\sum u = m\}$ (affine hyperplane) | §13 T-PF-A1-AR line 1633 ($H_0$, $H_M$) | Cat A |
| **L2. box+volume admissible** | $\mathcal F_M(\mathcal P) = \Sigma_m = [0,1]^n \cap H_M$ | §3.9 line 248, §8.0 line 666 | **일차 작동 정의** |
| **L3. interior domain** | $\Sigma_m^\circ = \{u : 0 < u_i < 1, \sum u_i = m\}$ | CV114/02 line 29 (interior 표기); canonical 본문에는 명시 표기 없음, $\Sigma_m^\varepsilon$ ε-interior가 working/SF/cardinality_open.md 등에 등장 | working 표준 |
| **L4. reflected / boundary-aware domain** | $\tilde C \subset \mathbb R^{n-1}$ via affine isometry $\Phi$ (UIC + uniform exterior sphere), reflected Langevin in $N_{\tilde C}(\cdot)$ | §13 T-PF-A1-AR/SDE line 1633–1647 | Cat A (Lions–Sznitman) |
| **L5. quotient / symmetry-reduced** | $\mathrm{Aut}(G)$-orbit; $G_{u^*} = \mathrm{Stab}_{\mathrm{Aut}(G)}(u^*)$; orbital decomposition $T_{u^*}\Sigma_m = \bigoplus_\rho V^{[\rho]}$ (Maschke, §13 Theorem 1 orbital, Cat A) | §11.1 Commitment 14 line 888; working/SF/symmetry_moduli.md, schramm_sigma_locality_theorem.md | Commitment level + Cat A tool (단 통합 quotient state space는 미정의) |
| **L6. multi-formation product** | $\widetilde\Sigma_M^{K_{\mathrm{field}}} = \prod_j \Sigma_{m_j}$; 본질적 객체는 K-field; canonical에서 $\Sigma_M^K$는 **local chart**로 강등(§3.9 line 250). Topological sector $\mathcal B_K(\mathcal P) \subset \mathcal F_0$ 는 §16 D-ST-4 line 2007 — **"not a manifold; topological stratum"** | §3.9 line 250; §16 D-ST-4 line 2005–2009; CHANGELOG 3370 (OP-0009-Pre G3.2 $\widetilde{\widetilde\Sigma}^K_M = \Sigma^K_M / S_K$) | Multi-formation: working level only; canonical은 $\mathcal F_M$ 하나로 본다 |
| **L7. temporal / product over time** | $\{X_t, u_t, \mathbf M_{t\to s}\}$ 시퀀스. 두 시점 product $\Sigma_m^t \times \Sigma_m^s$는 working/CE/free_energy_wellposed.md line 28에 명시. T-Temporal-Identity는 transport map $R_{t\to s}$로 처리; canonical 차원에서 product 상태공간 자체를 정의하지는 않음 | working/CE/free_energy_wellposed.md:28; canonical §3.8 line 226 (transport kernel) | Transport kernel level only |

**관찰.** L0–L4는 canonical 차원에서 일관되고 Cat A. L5(quotient)는 캐논 commitment + Cat A tool이지만 **"quotient state space"라는 형식적 정의는 부재**. L6 multi-formation은 의도적으로 $\mathcal F_M$ 단일 폴리토프로 환원("local chart" 강등). L7은 transport map 수준에서만 처리.

---

## 4. 현재 사용 중인 기하학

저장소 근거:

**4.1 Inner product.** 어디서도 비-Euclidean inner product는 채택되지 않았다. 결정적 인용:
- §13 T-PF-A1-AR line 1633: "The map $\Phi(x) = u^* + Qx$ is an **isometry** $(\tilde C, |\cdot|) \to (\mathcal F_M(G), |\cdot|)$" — 표준 Euclidean norm.
- working/C/F_group_axioms.md F3.1: $\Pi_{\Sigma_m} = I - (1/n)\mathbf 1\mathbf 1^\top$ — 표준 orthogonal projector.
- working/SF/sigma_m_hessian_convention_audit.md:31: "Convention I (centered/intrinsic): project gradient + Hessian onto tangent simplex … subtract the mean." — Euclidean centered.

**4.2 Gradient.** Canonical에는 $\nabla\mathcal E$의 정의가 명시적 기호 형태로 §8 본문에 없으나, T-PF-A1-AR line 1635("$\nabla\tilde{\mathcal E}$ is $M_H$-Lipschitz") 및 SDE의 $-\nabla\tilde{\mathcal E}(X_t)\,dt$ 가 표준 Euclidean gradient임을 전제한다. Affine reduction을 통한 $\tilde C$ 위의 gradient는 $Q^\top \nabla\mathcal E$.

**4.3 Hessian.** §13 T-PF-A1-AR line 1637: "$\nabla^2 \tilde{\mathcal E} = Q^\top \nabla^2 \mathcal E_{\mathrm{SCC}}(u^*+Qx) Q$". 이는 표준 Euclidean Hessian의 **접공간 $H_0 = \mathbf 1^\perp$ 위로의 직교 projection**. working/SF/sigma_m_hessian_convention_audit.md는 두 projection convention(centered vs Lagrange-multiplier)의 등가성 audit이 진행 중임을 보여줌(line 1–32) — 둘 다 Euclidean 기반.

**4.4 Projected gradient flow.** §13 T14(언급 line 93 of CV114/02), working/SF/sigma_lie_algebra_structure.md:49 — "projected gradient descent, treating $\Sigma_m^\circ$ as a Riemannian manifold with the **inherited Euclidean metric**". 이는 working 파일이며, "Riemannian"이라는 말이 등장하지만 **inherited Euclidean** 의미.

**4.5 Graph Laplacian의 역할.** §8.4 line 714에서 $\mathcal E_{\mathrm{bd}}$ 안의 quadratic form. CV114/04 Degeneracy #1(line 17): "**H-MORSE is defined on $T_{u^*}\Sigma_m = \mathbf 1^\perp$, where this mode is excluded.**" — 즉 Laplacian의 spectrum은 에너지 spectrum에 들어가지만 **상태공간 metric tensor 역할은 아님**.

**4.6 Riemannian metric의 등장.**
- §8.7(line 741–743): Shahshahani $g_{ij} = \delta_{ij}/u_i$ — **유일한 명시적 Riemannian 메트릭**, 단 "commentary", "not a theoretical commitment".
- Fisher metric, Wasserstein metric, graph-Sobolev metric, operator-induced metric: 본 감사 grep 범위(`THEORY/`, `--include="*.md"`)에서 상태공간 metric으로는 **발견되지 않음**. (Wasserstein/Sinkhorn은 transport `M_{t\to s}` 비용 함수 맥락에만 등장 — `THEORY/working/temporal/H-SINK.md` 등.)

**판정 (저장소 근거).** 현재 SCC는 다음으로 가장 정확히 기술된다:

> **"Euclidean ambient $\mathbb R^n$에서의 affine-constrained reflected polytope variational theory."** 작용 폴리토프 $\mathcal F_M = [0,1]^n \cap \{\mu^\top u = M\}$ 위에서 $\nabla, \nabla^2, \Pi_{\mathbf 1^\perp}$ 모두 표준 Euclidean inner product 기준이며, graph는 $\mathcal E_{\mathrm{bd}}$를 통해 들어간다. Shahshahani 정보기하는 §8.7에 commentary로 *언급*되어 있을 뿐, theoretical commitment가 아니다.

---

## 5. boundary와 reflection 처리

**5.1 Volume constraint $\sum u_i = m$.** §8.0 본문(line 666–676). Fixed Commitment #9(§11.1 line 878): "Volume constraint as structural axiom … not a computational convenience." 처리 방식: 직교 projector $\Pi = I - (1/n)\mathbf 1\mathbf 1^\top$ (F3.1) 또는 등가 affine isometry $\Phi: \tilde C \to \mathcal F_M(G)$ (T-PF-A1-AR line 1633).

**5.2 Box constraint $0 \le u_i \le 1$.** Canonical $\mathcal F_M = \mathcal F_0 \cap H_M$ 에 포함. Polytope의 facet 개수 ≤ $2n$ (T-PF-A1-AR line 1632).

**5.3 Strict interior $0 < u_i < 1$.** 캐논 본문은 strict interior assumption을 **광역적으로 부과하지 않는다.** 단:
- canonical §13 T-σ-framework, T-PreObj-1 등의 critical point 분석은 **암묵적으로 interior** 전제(working/SF/sigma_m_hessian_convention_audit, sigma_theorem4_canonical_revision 다수 인용).
- H-MORSE-Local의 (M-A3) "strict interiority $0 < \delta_0 \le u^*_i \le 1 - \delta_0$"이 명시적 가정으로 등장 (CV114/02 line 124, CV114/09 line 67) — 즉 **strict interiority는 H-MORSE 등록을 위한 *가정*이지 캐논 결과가 아니다.**
- CV114/04 Degeneracy #7(line 101): "Blocks H-MORSE? Only if minimizer reaches boundary. Canonical T-PreObj-1 minimizers in spinodal interior are strictly interior under typical parameters."

**5.4 Reflected polytope / normal reflection.** **Canonical Cat A** 로 등록된 처리:
- T-PF-A1-SDE line 1647: "$dK_t$ pointing into the **inward normal cone** $N_{\tilde C}(X_t)$".
- T-PF-A1-AR line 1634: $\tilde C$는 uniform interior cone + uniform exterior sphere 조건 모두 만족.
- Lions–Sznitman 1984 Theorem 1 convex case (ii) — **no smooth boundary required**; corner 처리가 명시적으로 포함(CHANGELOG 1851 "Corner reflection is the orthogonal projection onto the inward normal cone $N_{\tilde C}(z)$ — well-defined for polytopes, subsumed by convexity in Lions-Sznitman").

**5.5 Stratified / corner-aware Morse.** **부재 또는 deferred:**
- CV114/05 Counterexample 6(line 97 "Boundary critical point with active constraints"), Counterexample verdict (line 107): "**Unconditional H-MORSE FAILS on $\partial\Sigma_m$.** Stratified Morse required."
- working/E/MO1_dissolution.md (line 123, 171, 269)에 Forman discrete Morse, Witten Laplacian 후보가 등장 (working level, deferred).
- observer_moduli/open_problems.md OP-OMS-027 "Regularity at Corners of $\Omega$" Open.
- CV114/02 line 35: "Critical points on the boundary require stratified Morse (Goresky-MacPherson) treatment. **CV-1.14 should restrict to interior critical points** $u^* \in \Sigma_m^\circ$ unless explicitly stated."

**판정.** Reflected SDE 차원에서 boundary/corner 처리는 **Cat A로 완비**. 그러나 **에너지 landscape의 Morse 측면에서는 strict interiority를 가정해 회피하고 있으며, $\partial\Sigma_m$의 stratified Morse는 W7+ deferred.** 두 처리방식의 분리는 명시적.

---

## 6. H-MORSE와 상태공간의 관계

**6.1 영역 일관성.** H-MORSE 모든 등장(`hypothesis_tree.md:168–184`, `canonical.md` line 1710 H5 statement under T-P-F-ε0-K, `CV114/02 §2`, `CV114/05`, `CV114/09 §4`)에서 도메인은 **일관되게 $\Sigma_m$ (또는 $\Sigma_m^\circ$)** 이다 — full $\mathbb R^n$도 아니고 reflected $\tilde C$도 아니고 quotient도 아니다.

**6.2 비퇴화 검사 위치.** Hessian nondegeneracy는 **접공간 $T_{u^*}\Sigma_m = \mathbf 1^\perp$ 위로 projection된 Hessian**에서 요구된다.
- hypothesis_tree HT-3.5 line 170–172: "$H(u^*)|_{T_{u^*}\Sigma_m}$ has $\mu_{\min} > 0$ (mod symmetry-zero eigenvalues)".
- CV114/02 §6 line 91 ("$T_u\Sigma_m^\circ = \mathbf 1^\perp$"), §8.A line 126 ("$H^{\mathrm{proj}}_\mathcal E(u^*) := \Pi_T H_\mathcal E(u^*) \Pi_T$ on $T_{u^*}\Sigma_m = \mathbf 1^\perp$").
- CV114/05 Counterexample 1 verdict: "H-MORSE is defined on $T_{u^*}\Sigma_m = \mathbf 1^\perp$, where [the longitudinal $\mathbf 1$-mode] is excluded."

이것은 **Euclidean projected Hessian** 이다 — working/SF/sigma_m_hessian_convention_audit.md의 Convention I (centered/intrinsic) 또는 II (Lagrange) 둘 다 결과적으로 같다(canonical 차원의 statement는 convention 비특정).

**6.3 무조건성 부정.** CV114/05 (Counterexample Hunter)가 4+1개 구조적 반례를 발견:
- C1 $C_n$ cycle, sub-spinodal: V5b-T-zero에 의해 Goldstone $\mu_{\mathrm{Gold}} = 0$ **exact** (canonical §13 V5b-T-zero, Cat A).
- C2 $T^d$ torus: $d$차원 Morse-Bott degeneracy.
- C3 $D_4$ symmetric minimizer: Hessian PD이지만 2겹 degeneracy — **Morse-Bott, not Morse**.
- C4 bifurcation parameter (T8-Full threshold): zero eigenvalue, codim-1 in parameter space.
- C5 (line 97) boundary critical point with active constraints: stratified Morse required.

→ **Unconditional H-MORSE = FALSE.** CV114/05 line 131.

**6.4 권장 형태(working level).** **H-MORSE-Local** (CV114/02 §8.A, CV114/09 §4):
- (M-A1) canonical parameter window 안 (sub/super-critical + $a_{\mathrm{cl}} < 4$).
- (M-A2) trivial stabilizer $\mathrm{Stab}_{\mathrm{Aut}(G)}(u^*) = \{e\}$ — **이는 quotient를 부분적으로 사용하지만 quotient state space는 아니다. 단지 symmetric minimizer를 배제.**
- (M-A3) strict interiority $0 < \delta_0 \le u^*_i \le 1-\delta_0$ — **boundary stratum 배제.**

→ 결과적으로 H-MORSE는 $\Sigma_m^\circ$의 strict-interior + non-symmetric 부분에서만 진술된다. 도메인은 명시적으로 **canonical $\Sigma_m$의 부분집합**.

**6.5 모호함.** Canonical §13 T-P-F-ε0-K 의 H5(line 1710) 진술은 "saddle $\tilde u^*_{\mathrm{sad}}$ and minimum $\tilde u^*_{\mathrm{min}}$ are non-degenerate critical points of $\mathcal E + \varepsilon R$ stable for $\varepsilon \in [0, \varepsilon_0]$ (no critical-point bifurcation)" 로 되어 있으며, 도메인이 **$\Sigma_m$인지 $\tilde C$인지 명시적이지 않다.** 문맥상 $\mathcal F_M(\mathcal P)$지만, T-P-F-ε0-K의 H5는 "saddle + minimum + 안정성"이라는 세 가지 다른 요구를 묶어둔 형태다. CV114/02 §4의 4가지 해석((i)–(iv))이 정확히 이 모호함을 분해.

**판정.** **H-MORSE는 정확히 $T_{u^*}\Sigma_m^\circ = \mathbf 1^\perp$ 위의 Euclidean projected Hessian의 비퇴화성을 요구한다.** Reflected polytope $\tilde C$나 quotient $\Sigma_m / \mathrm{Aut}(G)$ 위가 아니다. Riemannian 해석은 부재.

---

## 7. Package I과 Package II의 상태공간 일관성

**Package I (CV-1.8–1.9, Cat A 완료).**
- 도메인: $\mathcal F_M(G) = [0,1]^n \cap \{\mu^\top u = M\}$ via isometric reduction to $\tilde C \subset \mathbb R^{n-1}$.
- 처리: reflected SDE with $dK_t \in N_{\tilde C}(\cdot)$, Lions–Sznitman convex case.
- Gibbs $\pi_{T_*} = Z^{-1} e^{-\mathcal E/T_*} d\sigma_M$ unique invariant (T-PF-A1-GI).
- Poincaré $\lambda_1 \ge (\pi^2/n) e^{-\mathrm{osc}(\tilde{\mathcal E})/T_*}$ (T-PF-A1-PE, Cat A).
- **Boundary/corner는 normal cone reflection으로 흡수 — Morse 가정 불필요.**

**Package II (OPEN, conditional on H5 + OP-0021).**
- 도메인: 동일하게 $\Sigma_m$ / $\mathcal F_M$로 의도. CV114/07_Eyring_Kramers_requirements.md table line 11–13:
  ```
  Variant 3: Reflected Langevin EK on convex polytope C̃ — Smooth Morse on
  interior; reflection at ∂C̃ — Yes for interior critical points — Bovier-
  Den Hollander 2015 (book); Bouchet-Reygner 2016
  ```
- 추가 요구: minimum + saddle 모두 비퇴화 (H-MORSE-Local + H-MORSE-Saddle).
- **Package II는 명시적으로 "interior critical points만"** 처리 (CV114/07 line 78).

**상태공간 처리의 (일관성/불일치) 분석.**

| 항목 | Package I | Package II (목표) |
|---|---|---|
| Ambient | $[0,1]^n \cap H_M$ = $\mathcal F_M$ | 동일 |
| Affine reduction | $\tilde C \subset \mathbb R^{n-1}$, isometry $\Phi$ | 동일 (전제) |
| Metric | Euclidean (isometry, $Q^\top Q = I$) | Euclidean projected |
| Boundary 처리 | **Reflected SDE, normal cone, corner 포함** (Cat A) | **Boundary critical points 배제** ($\partial\Sigma_m$ stratified Morse는 deferred) |
| Critical-point 요구 | 없음(dynamics만 정의) | Morse nondegeneracy + 안정성 |
| Symmetry 처리 | invariance만 가짐(reflection의 isometric symmetry) | **Symmetric minimizer 배제** (M-A2) 또는 orbital quotient + Morse-Bott |

**불일치 (또는 작업 분할).**

1. **Package I은 $\partial\tilde C$/corner를 reflected SDE로 다루는 반면, Package II의 H-MORSE-Local은 strict interior로 회피한다.** 두 처리는 **상충하지는 않지만**(다른 종류의 분석을 위한 다른 가정), **다른 상태공간 영역(전체 $\tilde C$ vs $\Sigma_m^\circ$ ∩ {symmetry-broken})에 대한 진술이라는 점은 명시적으로 분리되어 있다.**
2. **Package I의 Gibbs measure 는 전체 $\mathcal F_M$에 supported인 반면, Eyring–Kramers의 transition rate는 interior, non-symmetric, non-bifurcation point에서만 의미를 갖는다.** Bouchet–Reygner / Bovier–Den Hollander의 reflected EK는 corner에서의 prefactor 보정 항이 별도로 필요(CV114/07 line 156 "Bovier-Eckhoff-Gayrard prefactor derivation adapted to reflected polytope — literature available, integration OPEN").
3. **Package I은 quotient를 요구하지 않는다** (Gibbs measure는 Aut(G)-invariant이지만 적분은 ambient $\mathcal F_M$에서 수행); **Package II의 H-MORSE는 사실상 Aut(G) orbit 위로의 reduction이 필요 가능성**(CV114/00 line 36: "H-MORSE must therefore be either **quotient** (mod discrete symmetry), **local** (restricted to symmetry-broken configurations), or **generic** (post small symmetry-breaking perturbation)").

**판정.** Package I과 II는 **동일한 ambient $\mathcal F_M(G)$를 공유**하나, **boundary와 symmetry 처리에서 사용하는 reduction이 다르다.** 이것은 의도적 분업(reflected dynamics ≠ critical-point Morse)이지만, "동일 상태공간"이라는 명목 아래 **두 차원의 추가 가정(strict interior + symmetry-broken)이 Package II에만 부과된다**는 점은 명시적으로 알려져 있다.

---

## 8. 애매한 지점과 갭 (해결하지 않고 목록화)

1. **명칭 다양성, 단일 객체.** $\Sigma_m$(§8.0), $\mathcal F_M(\mathcal P)$ / $\mathcal F_M(G)$(§3.9, §13), $\Omega = \Sigma_m \cap [0,1]^n$(observer_moduli), $\tilde C$(T-PF-A1-AR affine-reduced) — 모두 객체는 동치이거나 isometric. 그러나 캐논 한 곳에서 "공식 이름은 $\mathcal F_M$이며 $\Sigma_m$, $\Omega$, $\tilde C$는 부차적"이라고 못 박지 않음. *(작은 ambiguity, 실질 영향 없음.)*

2. **$\Sigma_m$이 box constraint를 포함하는가? — 캐논 안에서 단언이 일관되지만 잠재적 혼란.** §8.0 line 666–668: $u \in [0,1]^n$ 포함. §3.9도 $[0,1]$ 포함. 그러나 일부 working 파일에서 $\Sigma_m$만 mass-constraint로, $[0,1]$은 별도로 부과하는 식으로 분리해 쓰는 경우가 있어 표기 통일에 약한 균열.

3. **Hessian projection convention의 unresolved audit.** working/SF/sigma_m_hessian_convention_audit.md (W6 D1 EOD placeholder, 28 lines, 본격 audit 미수행) 가 등록되어 있고, T-σ-Theorem-4의 Cat B 강등 사유 중 (γ)가 정확히 이 convention 모호함이다(CHANGELOG line 4612–4614, working/SF/sigma_theorem4_canonical_revision.md). **현재 어느 convention이 "canonical"인지 단언된 문장은 없다.**

4. **Shahshahani metric의 지위.** §8.7 line 741–743: "commentary", "implementation question". 그러나 *완전히 폐기*되었다는 명시도 없다. 만약 Riemannian 재해석이 시도된다면 §8.7이 그 단서가 될 수 있는데, 그 절은 **non-binding** 으로 남아있어 미래 해석을 결정하기에 부족.

5. **§8.4의 "$2\alpha v^T L v$ … gradient $4\alpha L u$" 와 §8.4 본문 "$\alpha \sum \mathbf N_t(x,y)(u(x)-u(y))^2$"의 factor 일관성** — CLAUDE.md "Critical Implementation Details"에서 "E_bd smoothness: $2\alpha u^T L u$ → gradient $4\alpha L u$ (factor 4, ordered-pair sum)"로 정리되어 있으나, ordered/unordered pair convention이 §0 Summation Convention과 어떻게 연결되는지의 명시는 §0에 있는 것으로 보임. (보고서 범위 밖 — implementation note.)

6. **Quotient의 형식적 지위.** Commitment 14(§11.1 line 888–891)는 orbital character를 "constitutive"라 선언하고 σ-tuple은 $\mathrm{Aut}(G)_{u^*}$-irrep decomposition에 의존하나, **$\Sigma_m / \mathrm{Aut}(G)$ 자체를 정식 상태공간으로 등록한 정리는 없다.** working/SF/symmetry_moduli.md와 schramm_sigma_locality_theorem.md가 도구로 사용할 뿐.

7. **Stratified 처리의 부재.** $\partial\Sigma_m$의 face stratification — vertex / edge / facet — 가 canonical 차원에서 형식적으로 정의된 문장은 발견되지 않음. Prop 1.1이 "manifold with corners"라 부르지만, **stratum 라벨링이나 normal cone family는 working 차원에서만**(observer_moduli/basin_stratification.md, stratified_dynamics.md, op_oms_018 §B). OP-OMS-027 Open.

8. **H-MORSE 진술의 도메인 모호함.** T-P-F-ε0-K의 H5는 "saddle 와 minimum이 non-degenerate stable for $\varepsilon \in [0, \varepsilon_0]$"라고만 적혀 있고(canonical line 1710), 도메인이 $\mathcal F_M$인지 $\Sigma_m^\circ$인지 quotient인지 명시되지 않음. CV114/02 §4 (i)–(iv)가 정확히 이 모호함을 4단계로 분해.

9. **Eyring–Kramers in reflected polytope의 표준 reference 통합 미완.** Canonical 차원에서 Bouchet–Reygner 2016, Bovier–Den Hollander 2015 인용은 부재. working/CV114_H_MORSE_PACKAGEII/07 line 84: "literature-available, not yet bibliographically integrated."

10. **Multi-formation 영역의 architecture-state 분리.** Commitment 16(§11.1 line 900–916) 가 $K_{\mathrm{field}}$(architectural cap)과 $K_{\mathrm{act}}(t)$(dynamic stratum index)를 분리하지만, $\widetilde\Sigma_M^{K_{\mathrm{field}}}$의 corner / boundary / Morse structure는 W11–W12 deferred (OP-0009).

11. **$T_*$ (effective temperature)의 캐논 지위.** OP-0021 OPEN. Package I은 임의의 $T_* > 0$에 대해 Cat A이지만, "canonical $T_*$가 무엇인가"는 미정. $T_*$의 정체가 정해지면 Gibbs measure의 정량적 의미가 바뀜.

12. **"State space"라는 용어가 canonical 본문에서 명시적으로 정의된 적이 없음.** §3.9 "foundational state space" 어구가 가장 가깝지만, 글로벌 정의 절은 없음. 이는 documentation 갭 — 객체는 잘 정의되어 있으나 그 객체를 칭하는 어휘가 분산.

---

## 9. 다음에 물어야 할 최소 질문들 (Riemannian 재해석 시도 전 필수)

저장소 현재 상태로 답할 수 없는, **선결되어야 할 질문**들:

1. **H-MORSE가 정확히 어떤 도메인 위의 비퇴화성인가?** Canonical에 명시되어야 한다(현재 $\Sigma_m^\circ \cap \{\text{symmetry-broken}\}$ 으로 해석 가능하지만 *공식 statement 없음*). H-MORSE-Local로 등록되더라도 (M-A1, M-A2, M-A3)가 캐논 axiom인지 working hypothesis인지 결정 필요.

2. **§8.7의 Shahshahani commentary는 살아있는 옵션인가, 닫힌 옵션인가?** "Not a theoretical commitment"는 채택 안 한다는 의미인가, 미래에 채택될 수 있다는 의미인가? 만약 미래에 metric을 도입한다면 §8.7이 binding statement인지 advisory인지 먼저 확정해야 한다.

3. **Shahshahani metric으로 재해석할 경우, T-PF-A1-AR의 "isometry"가 깨진다 — Lions–Sznitman convex case (Cat A)가 그대로 유효한가?** Reflected SDE는 Euclidean reflection이 기본이고, Riemannian reflection은 Bakry–Émery / Wang류 다른 reference가 필요하다. Package I의 Cat A가 유지되는지가 결정적.

4. **Graph Laplacian이 "에너지 항"과 "상태공간 metric" 사이를 자유롭게 옮겨 다닐 수 있는가?** §8.4의 $4\alpha L$ Hessian contribution을 metric의 일부로 흡수하면 $\mathcal E_{\mathrm{bd}}$의 정의가 바뀐다. CN5 "4-term conceptual independence" (Commitment 5, §11.1 line 870)가 깨질 위험. metric 도입의 ontological cost를 정량화해야 한다.

5. **Quotient $\Sigma_m / \mathrm{Aut}(G)$를 공식 상태공간으로 등록할 것인가, 아니면 H-MORSE는 strict interiority + non-symmetric으로 우회할 것인가?** CV114/00 line 36이 제시한 세 옵션(quotient / local / generic) 중 어느 것을 정식 경로로 채택할지가 H-MORSE 진술 자체를 바꾼다. Riemannian 도입은 이 선택과 독립적이지 않다 — quotient 채택 시 metric도 quotient 위에 정의되어야 한다.

6. **$\partial\Sigma_m$의 stratified Morse를 위한 framework를 도입할 것인가?** Goresky–MacPherson(CV114/02 line 35), Forman discrete Morse, Witten Laplacian on simplicial complex(working/E/MO1_dissolution.md) 중 어느 것을 작업 가설로 잡을지 결정해야 비-interior critical point가 H-MORSE에 들어올지 빠질지가 정해진다.

7. **Package II의 saddle은 어디에 있는가? (interior saddle 가정의 정당성)** 현재 H-MORSE-Saddle은 CV-1.15 추가 작업으로 deferred. Riemannian 도입은 saddle의 위치 자체를 바꿀 수 있으므로, **현재 Euclidean 가정 하에서 saddle 위치가 numerically 어디인지** 의 baseline data가 먼저 필요(NQ-187 등은 minimizer 분석; saddle은 미흡).

8. **현재 "Σ_m-Hessian convention audit"(working/SF) 가 미해결인 상태에서 metric을 바꾸면 어떻게 되는가?** T-σ-Theorem-4의 Cat B 강등 사유 (γ)가 정확히 convention 모호함이다. Convention I과 II 중 어느 것이 canonical인지를 먼저 확정해야, Riemannian metric 도입의 "어디로부터의 변경인가"가 명확해진다.

---

## 부록 A. 인용된 핵심 파일

| 파일 | 역할 |
|---|---|
| `THEORY/canonical/canonical.md` | §3.9 (line 242–250), §8.0 (666–668), §8.4 (714), §8.7 (741–743), §11.1 Commitments (878–916), §13 Prop 1.1 (1558–1561), Theorem 3.1 (1568–1571), T-PF-A1-AR/SDE/GI/PE (1627–1686), T-P-F-ε0-K H5 (1708–1723), §16 D-ST-1..5 (1987–2035) |
| `THEORY/canonical/hypothesis_tree.md` | HT-3.5, H-MORSE 노드 (line 168–184), critical path |
| `THEORY/canonical/CV-1.13_SEAL.md` | 현행 캐논 sealed state (59A/14B/5C/5R=83) |
| `THEORY/canonical/theorem_status.md` | 정리 인덱스 + Open Problems Catalog (지면상 인용은 CV114/01에 의해 매개) |
| `THEORY/working/CV114_H_MORSE_PACKAGEII/00..09` | H-MORSE 재구성, 반례 카탈로그, Package II 의존성 맵, Eyring–Kramers 요구사항, CV-1.14 권장안 |
| `THEORY/working/MF/pf_a1_lions_sznitman_freidlin_route.md` | Package I 완전 증명 working source |
| `THEORY/working/MF/pf_tstar_langevin.md` | T-P-F-ε0-K + H5 working source |
| `THEORY/working/C/F_group_axioms.md` | F1/F2/F3 axiom — projected reflected SDE 정의 |
| `THEORY/working/SF/sigma_m_hessian_convention_audit.md` | Hessian projection convention I/II audit (W6 placeholder) |
| `THEORY/working/SF/symmetry_moduli.md`, `schramm_sigma_locality_theorem.md`, `cardinality_open.md` | Aut(G)-orbital / Morse on $\Sigma_m$ working development |
| `THEORY/working/observer_moduli/op_oms_018_regular_u_star.md`, `stratified_dynamics.md`, `basin_stratification.md`, `open_problems.md` (OP-OMS-027) | corner regularity / tangent cone working development |
| `THEORY/working/E/MO1_dissolution.md` | Forman discrete Morse / Witten Laplacian framework (working) |
| `THEORY/CHANGELOG.md` | W6 D4 Sessions M–N–O–P (CV-1.7→1.9), Package I/II split rationale |

---

## 부록 B. 한 문장 요약 (저장소 근거)

> CV-1.13 (2026-05-10) 기준 SCC의 유효 상태공간은 $\mathcal F_M(\mathcal P) = [0,1]^n \cap \{\sum_x u(x) = M\}$ (canonical §3.9 / §8.0의 $\Sigma_m$과 동치, §13 Prop 1.1에 의해 compact convex polytope, manifold with corners, contractible로 Cat A 등록)이며, gradient·Hessian·projected gradient는 모두 표준 Euclidean inner product 위에서 정의되고(T-PF-A1-AR의 affine isometry, F3의 $\Pi = I - (1/n)\mathbf 1\mathbf 1^\top$), graph $L$은 상태공간 metric이 아니라 $\mathcal E_{\mathrm{bd}}$의 quadratic form 안에 들어간다(§8.4). Reflected polytope dynamics는 Lions–Sznitman convex case로 canonical Cat A이며 corner를 normal cone reflection으로 흡수하지만(T-PF-A1-SDE), H-MORSE / Package II의 critical-point Morse 진술은 일관되게 $T_{u^*}\Sigma_m^\circ = \mathbf 1^\perp$ 위의 Euclidean projected Hessian의 비퇴화성을 요구하며 strict interiority + symmetry-broken 추가 가정을 부과한다(CV114/02 §8.A, CV114/09 §4). §8.7의 Shahshahani 정보기하 언급은 명시적으로 "commentary, not a theoretical commitment"로 표기되어 있고, Fisher·Wasserstein·graph-Sobolev metric은 상태공간 metric으로 등장하지 않는다.

---

**감사 종료 메모.** 본 working note는 read-only audit의 산출물이다. canonical / hypothesis_tree / theorem_status / CHANGELOG / 기존 working source 어떤 파일도 수정하지 않았으며, claim 승격/강등을 수행하지 않았다. CV114 entry audit 시리즈(00..10)의 후속 working note로 격납되어 contamination barrier를 준수한다. 본 보고서의 모든 진술은 인용된 파일과 줄 번호로 추적 가능하다.
