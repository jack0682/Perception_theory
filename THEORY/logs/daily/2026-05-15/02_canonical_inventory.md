---
type: log/daily/inventory
date: 2026-05-15
session_label: W7-Day6 Stage 1 — Canonical Inventory
canonical_version: CV-1.16 (sealed 2026-05-14, untouched)
prerequisite: 00_plan.md, 01_pre_brainstorm.md, 01b_user_proposal_zfield.md 모두 통독
mode: 검토 / 읽기 전용 인용
stage: 1 of 6
---

> [!nav] Linked: [[00_plan]] · [[DECLARATION]] · [[canonical]] · [[01b_user_proposal_zfield]]


# 02 — Canonical Inventory (Stage 1)

**Session:** 2026-05-15 (W7-Day6)
**Target (from `00_plan.md`):** "사용자의 원래 통찰 (u^* → S_0(u^*) → K_read; D_0 → D_1 → D_2) 이 현재 canonical CV-1.16 에 *이미 담겨 있는지 / 외부 영역인지 / 새 수학 내용인지* 정밀 검토."
**This file covers:** Stage 1 — D_0 / D_1 / D_2 각각이 canonical 어디에 (있다면) 담겨 있는가의 *구체 위치 인용* inventory.
**Depends on reading:** `canonical.md` §2, §3.1–3.11, §7, §11.1 Commitment 16, §13 Cat A 항목들, §14 CN6/CN10/CN15; `DECLARATION.md` 본문; `theorem_status.md` OP-0008/0009/0021.

---

## §1. Stage 1 의 위치와 자기 강제

Stage 1 은 **새 명제를 만들지 않는다**. canonical CV-1.16 의 *현재 상태* 를 D_0 / D_1 / D_2 의 세 층 관점에서 *목록화* 한다.

자기 강제 (`00_plan.md` Decision gate 적용):
- 각 인용은 `canonical.md §X.Y` 또는 `theorem_status.md` 의 *정확한* 위치를 명시한다.
- "어딘가 있다" 식 표현 금지.
- 통찰을 미리 결론짓지 않는다. inventory 는 *사실 수집* 단계.
- 새 어휘 (P1/P2 등) 도입 금지.
- $z_t, K_{z_t}, \mathcal{F}$ 등 사용자 메모 `01b` 의 어휘는 *그 자체로* 평가 대상 — Stage 3 까지는 canonical 어휘 만으로 inventory.

---

## §2. D_2 (응집 후 해석 = 셈 / 판독) Inventory

D_2 의 사용자 측 정의 (`01b §2`, `00_plan §Mission`):

> "응집이 진행된 뒤 *얼마인가* 의 *판독*. 개수는 응집의 원인이 아니라, 응집된 구조의 판독 결과다. $S_0(u^*) \to K_\mathrm{read}$."

### §2.1 K_act = #PersComp — `canonical.md §3.11`

직접 인용 (canonical.md §3.11 line 285):

> $$K_{\mathrm{act}}(\tilde{u}) = \#\mathrm{PersComp}(\tilde{u}) := \bigl\vert \{(b,d) \in \mathrm{Bars}_0(\tilde{u}; G) : b - d > \rho_{\mathrm{pers}}\}\bigr\vert $$
>
> where $\mathrm{Bars}_0(\tilde{u}; G)$ is the $H_0$ persistent homology barcode of $\tilde{u}$ via the superlevel-set filtration on $G$.

이 정의는 **세 가지 핵심 특성** 을 가진다:

1. **입력은 $u^*$ 자체** — formation 의 명단 (list of formations) 이 아니라, *cohesion field 위에서 superlevel-set filtration 으로 H_0 barcode 를 계산한 결과의 cardinality*. 즉 *K 가 응집 결과의 readout* 임이 정의에 명시.
2. **$\rho_{\mathrm{pers}}$ 임계 의존** — "얼마나 두드러진 component 를 셈에 포함시킬지" 라는 *관측 측정 파라미터*. 이는 DECLARATION 의 "관측 조건 의존성" 이 K 의 셈 단계에 직접 들어옴을 보임.
3. **integer-valued, 일반적으로 locally constant on $\mathcal{F}_M \setminus V$** (V = vineyard set). 즉 K 는 *u 의 부드러운 변화에 무감* 하다가 *vineyard crossing* 에서 점프. 이것이 사용자 통찰 "셈은 응집된 구조의 판독" 의 직접적 수학적 형식.

**Cat 분류**: §3.11 자체는 Definition. 셈에 관련된 정리:

- **T-L1-F (Hard-Bar / Active-Count Bridge)** — `canonical.md §13 Cat A`, `theorem_status.md` line 232, CV-1.5.2 promotion. 조건부 Cat A (P0–P11 L1-J regime). $K_{\mathrm{bar}}^{\ell_{\min}}(U) = K_{\mathrm{act}}^{\varepsilon}(\mathbf u)$ + labeled bijection.
- **T-L1-M (Soft-Count Corollary)** — `canonical.md §13 Cat A`, CV-1.5.2 + 2026-05-04 supervised promotion. $K_{\mathrm{soft}}^{\phi} = K_{\mathrm{act}}$ under $\phi \in \Phi_{\mathrm{res}}, \tau < \tau_*^{\mathrm{post-R2}}$.
- **T-K-Select-PF (Cat B)** + **T-K-Select-OBS (Cat B)** — `canonical.md §13 Cat B`, CV-1.10/CV-1.11. K^* selection from posterior / equilibrium sector mass.

### §2.2 Commitment 16 — K_field / K_act 두 층 분해 (`canonical.md §11.1 (16)`)

직접 인용 (canonical.md line 909–919):

> (i) **K_field** — the architectural cap. An external modeling-layer commitment chosen by the modeler before instantiating the K-field architecture (I9). K_field specifies the maximum number of distinguishable formations the analytical framework will track.
>
> (ii) **K_act(t)** — the active stratum index. A derived integer diagnostic computed from the K-field minimizer at time $t$. ...
>
> K_act is dynamic: K-jump events are transitions $K_{\mathrm{act}}(t^{*-}) > K_{\mathrm{act}}(t^{*+})$.

이는 사용자 통찰의 *셈 = 판독* 명제를 *두 층으로* 분해:

- K_field: 모델러의 사전 설정 (관측자의 분해능 가정)
- K_act: 데이터로부터 *읽혀나오는* 활성 개수 (관측 결과)

**DECLARATION 연결**: DECL-1.0 §"관측 조건 의존성" 의 $N_{\text{objects}} = f(\lambda_2, \beta/\alpha, m, \text{distance}, \text{resolution})$ 는 K_act 가 *관측 조건의 함수* 임을 선언. Commitment 16 (ii) 는 이의 *수학적 구현*.

### §2.3 σ_rich — post-stabilization signature (`MOC_sigma_rich_framework.md`, `MF/sigma_rich_*.md`)

σ_rich = (sigma_standard, centroids, orientations, wigner_data) — `CODE/scc/sigma_rich.py` SigmaRich namedtuple. 사용자 통찰의 "응집된 구조" 의 *내부 판독 데이터* 에 해당.

- **derived diagnostic**: u_t 로부터 *유도되는* — primitive 가 아니다.
- σ_standard 의 Wigner-projection 부분 (OP-0008 MERGE/SPLIT) 은 Cat C / 잔여 open.
- centroid / orientation 부분은 Cat B (OP-0008-MERGE; `theorem_status.md` line 200–202).

**중요**: σ_rich 는 K_read 와 *상보적* 인 D_2 readout. K_read 가 "몇 개" 이면 σ_rich 는 "어떻게 생긴 것이 몇 개". 둘 다 응집 *후의* readout.

### §2.4 T-OP6-B (Boundary persistence ridge characterization) — `canonical.md §13 Cat A, CV-1.7`

직접 인용 (canonical.md §13, around line 369–392):

> $d_H\bigl(B_{\mathrm{PersRidge}}(\tilde{u}^*),\; \partial\mathrm{PersComp}(\tilde{u}^*)\bigr) \leq 2 \cdot (\alpha/\beta)^{1/2}$

이는 *boundary 의 자리* 가 *PersComp readout* 과 *2(α/β)^{1/2}* Hausdorff 거리 안에 있음을 Cat A 로 증명. **boundary 도 D_2 readout** (gradient ridge → bar topology 와 동일한 자리) 임을 의미.

### §2.5 D_2 inventory 결론

| 사용자 통찰 (D_2 측) | canonical 대응 | 위치 | 분류 |
|---|---|---|---|
| 셈은 응집 *후* readout | K_act = #PersComp on u^* | §3.11 | **Definition (Cat A)** |
| 관측 조건이 셈을 좌우 | $\rho_{\mathrm{pers}}, \theta_{\mathrm{core}}, \theta_{\mathrm{in}}$ 임계, K_field 사전 설정 | §11.1 (16) | **이미 담김** |
| K_read 의 동역학 | K-jump events, T-K-Select-PF/OBS | §13 Cat A/B | **이미 담김** (Cat A 부분 + Cat B 부분) |
| 응집의 *내부 구조* readout | σ_rich (centroid, orientation, σ_standard) | derived diagnostic | **부분 담김** (Cat B / Cat C 일부) |
| boundary 의 readout | PersRidge / PersComp 경계 | §13 T-OP6-B | **이미 담김** (Cat A) |
| $u^* \to S_0(u^*) \to K_{\mathrm{read}}$ 화살표 | $u^* \to (\mathrm{PersComp}, \sigma_{\mathrm{rich}}) \to K_{\mathrm{act}}$ | §3.11 + Comm.16 | **이미 담김** |

**D_2 정량 평가**: 사용자 통찰의 D_2 측면은 **거의 전체** 가 canonical 에 담겨 있다. 미해소 부분은 σ_standard 의 MERGE/SPLIT Cat C → Cat B 승급 (OP-0008) 와 K-Select-DYN (OP-0005-DYN) 뿐.

---

## §3. D_1 (응집 중 구조) Inventory

D_1 의 사용자 측 정의:

> "u_t 자체. 응집된 cohesion field. 차이가 *서로를 지지하여* 응집된 결과."

### §3.1 u_t — soft cohesion field primitive (`canonical.md §3.3`)

직접 인용 (canonical.md §3.3 line 187–193):

> $$u_t : X_t \to [0,1]$$
>
> The cohesion field $u_t$ is not a posterior probability, not a class membership score, and not a segmentation mask. It is the primary ontological entity of the theory: the graded field from which all further structure — closure, distinction, boundary, persistence — is derived.

이는 사용자 통찰의 D_1 의 *수학적 정체* 그 자체. **u_t 가 *바로* D_1**.

### §3.2 네 에너지 항 + 네 공리 그룹

- **E = λ_cl·E_cl + λ_sep·E_sep + λ_bd·E_bd + λ_tr·E_tr** — `canonical.md §7` (Minimal Energy Principle), `DECLARATION` §"에너지 구조".
- **CN5 (개념적 독립성)** — 네 항은 *수학적* 독립이 아니라 *개념적* 독립. 병합 금지.
- **Axiomatic Groups A (closure), B (adjacency), C (co-belonging), D (distinction), E (transport)** — `canonical.md §6`, axioms A1'/A2/A3/A4 (closure regulation, monotonicity, contraction $a_{\mathrm{cl}}<4$, continuity), B1-B4 (nonneg / sym / local / non-transitive), C1-C4 + C5 (co-belonging, demoted to derived diagnostic v2.0 cycle 2), D1-D4 (distinction), E1-E4 (transport).

**사용자 통찰의 "차이가 서로 지지" = closure 의 A1'/A2/A3** (자기 지지의 수학화). **"차이의 응집" = E_cl + E_sep + E_bd**. **"응집이 진행되면 경계가 선명" = T8** (다음).

### §3.3 T8 — 위상전이 (`canonical.md §13 Cat A, T8-Core / T8-Full`)

직접 인용 (DECLARATION §"중심 정리 — T8"):

> $$\frac{\beta}{\alpha} > \frac{4\lambda_2}{\lvert W''(c) \rvert}$$
>
> 이 임계조건이 성립할 때: 장은 비균일 최솟값을 가진다. 경계가 출현한다. 객체성이 발생한다.

이는 사용자 통찰의 *"응집이 진행되면 경계가 선명해진다 / 분해 한계가 있다 / 두 사과가 하나로 보일 수 있다"* 의 *심장* (DECLARATION 자체 표현). $\lambda_2$ 는 그래프 해상도. 멀어질수록 $\lambda_2 \downarrow$ → 임계 붕괴 → 융합.

### §3.4 Diagnostic 4-vector (`canonical.md §5, §7.2`)

$\mathbf{d}_t = (\mathrm{Bind}, \mathrm{Sep}, \mathrm{Inside}, \mathrm{Persist}) \in [0,1]^4$ — 사용자 통찰의 *응집의 질적 평가* 의 *수학적 정량화*. **Cat A** 전체.

### §3.5 T-PreObj-1 / T-PreObj-1G — Pre-Objective Mechanism (`canonical.md §13 Cat A, CV-1.3`)

> The $\mathcal{F}=1$ single-disk minimizer of pure $\mathcal{E}_{\mathrm{bd}}$ is non-critical under full $\mathcal{E}$, with $\mathcal{F} \geq 2$ as the default ground state.

이는 **객체성 (objecthood) 이 primitive 가 아님** 을 수학적으로 보장. F-1 의 vacuity problem 의 split-resolution. *u_t 가 객체에 의존하지 않는다* 는 사용자의 ontological commitment 의 *Cat A 그래프-class 독립 정리*.

### §3.6 T-Temporal-Identity (4 parts, Cat A) — `canonical.md §13 Cat A, CV-1.13`

사용자 통찰의 *"두 시점의 응집을 같은 것으로 본다"* 의 수학적 정식. CV-1.13 sealed 2026-05-10. 4 parts (a,b,c,d) 모두 Cat A.

### §3.7 D_1 inventory 결론

| 사용자 통찰 (D_1 측) | canonical 대응 | 위치 | 분류 |
|---|---|---|---|
| u_t 자체가 응집장 | u_t : X_t → [0,1] primitive | §3.3 | **Definition (primitive)** |
| 4 에너지 항 (자기 지지 / 대조 / 경계 / 시간 연속) | E_cl, E_sep, E_bd, E_tr | §7, DECLARATION | **이미 담김** |
| 자기 지지 (closure tendency) | A1'/A2/A3 contraction, $a_{\mathrm{cl}}<4$ | §6 Group A | **이미 담김 (Cat A)** |
| 응집의 질적 평가 | (Bind, Sep, Inside, Persist) | §5/§7.2 | **이미 담김 (Cat A)** |
| 위상전이 (해상도 의존) | T8: β/α > 4λ_2/|W''(c)| | §13 T8-Core/Full | **이미 담김 (Cat A)** |
| 객체 비-primitivity | T-PreObj-1, T-PreObj-1G | §13 (Cat A, W4) | **이미 담김 (Cat A)** |
| 시간적 동일성 | T-Temporal-Identity 4 parts | §13 (Cat A, CV-1.13) | **이미 담김 (Cat A)** |
| 위상 안정성 | L-HMORSE-LOCAL, L-CLOSURE-LIFT | §13 (CV-1.16) | **이미 담김 (Cat A/B)** |

**D_1 정량 평가**: 사용자 통찰의 D_1 측면은 **본질적으로 전체** 가 canonical 에 담겨 있다. canonical SCC = D_1 의 수학. 이는 우연이 아니라 *설계상* — SCC 의 출발점이 D_1 (u_t) 임. *사용자 메모 `01b §1` 도 명시*: "기존 SCC 가 이미 D_1 부터 시작".

---

## §4. D_0 (전-응집 약한 차이) Inventory — 결정적 부재 검사

D_0 의 사용자 측 정의 (`01b §1`, `00_plan §Mission`):

> "감각장 → 약한 차이 → 응집 *직전*. 색·밝기·깊이·질감 같은 다채널 감각 미분장이 *u_t 가 형성되기 *전*에* 분포한 상태."

### §4.1 canonical 의 *primitive 계층* 점검

`canonical.md §3` 의 formal universe:

$$\mathfrak{C}^{\mathrm{soft}} = \bigl(T, \{X_t\}, \{u_t\}, \{\mathrm{Cl}_t\}, \{\mathbf{N}_t, \mathbf{D}_t\}, \{\mathbf{M}_{t \to s}\}\bigr)$$

primitive 후보 6개. D_0 후보로 검토할 만한 것:

#### 후보 1: **N_t — soft adjacency kernel (§3.5)**

직접 인용 (line 211–213):

> $\mathbf{N}_t : X_t \times X_t \to [0,\infty)$ is the soft adjacency kernel. It encodes the local relational support structure: $\mathbf{N}_t(x,y)$ measures the degree to which sites $x$ and $y$ are relationally proximate or locally coupled.

**관찰**:
- N_t 는 *주어진다* (primitive). canonical 은 *N_t 가 어디서 오는지* 다루지 않는다.
- B1–B4 (Group B 공리) 는 *N_t 의 성질* 만 규정: nonneg, symmetric, local, non-transitive. *N_t 의 출처* 에 대한 axiom 은 없음.
- 사용자 메모 `01b §3` 의 $K_{z_t}(x,y) = \exp(-d_X^2/2\rho^2)\exp(-d_\mathcal{F}^2/2\sigma^2)$ 는 *N_t 의 한 가지 구체 realization* 이며, 따라서 N_t 와 *형태적으로 동일* (Stage 3 에서 정량화).

#### 후보 2: **X_t — sensory/relational support (§3.2)**

직접 인용 (line 155):

> **On the status of $X_t$.** The relational support space $X_t$ is a domain of relational loci, not a collection of pre-given objects. **The individuation of sites in $X_t$ is a modeling choice at the implementation layer, not an ontological commitment of the theory.**

**결정적**:
- canonical 은 X_t 의 *내부 구조* (어떤 색이 어디 있는지, 어떤 깊이가 어디 있는지) 를 다루지 않는다.
- X_t 는 *site 의 집합 + 의 색인* 뿐. 색·밝기·깊이 같은 *site 별 feature value* 는 canonical 의 ontology 에 없음.
- 따라서 **D_0 (다채널 감각 미분장) 은 SCC 의 primitive 계층에 부재** — *명시적으로 modeling layer 의 외부*.

#### 후보 3: **W_sym = cohesion-weighted adjacency** (§9.4, §10.3)

> $W_{\mathrm{sym}}(x,y) = \sqrt{u_t(x)}\, \mathbf{N}_t(x,y)\, \sqrt{u_t(y)} / d_x$

이는 N_t 와 u_t 의 합성 — 즉 *D_1 의 일부*, D_0 아님.

#### 후보 4: **Fiedler vector, Laplacian L = D − W**

이는 N_t (또는 W_sym) 의 *spectral readout* — N_t 가 primitive 인 한 D_1 의 일부 (그래프 위 객체).

### §4.2 DECLARATION 의 *명시적* D_0 외부화

`DECLARATION.md §"태초의 장면"`:

> ```
> 감각장면
>   → 차이의 발생
>   → 경계 후보
>   → 형태 응집
>   → 깊이 일관성
>   → 하나의 단위로 묶임    ← 이 이론이 다루는 구간
>   → 객체 후보
>   → 이름 / 클래스 부여    ← 이 이론의 범위 밖
> ```

**결정적 관찰**:
- 화살표 6단계 중 SCC 는 "**하나의 단위로 묶임**" 단계만 다룬다고 *명시*.
- "감각장면 → 차이의 발생" 즉 D_0 의 *생성 부분* 은 `이 이론이 다루는 구간` *밖* (위쪽).
- "이름 / 클래스 부여" 는 `이 이론의 범위 밖` *아래쪽*.
- DECL-1.0 (2026-05-07) 작성 시점에 *명시적으로* SCC 의 범위는 D_1 위주, D_2 일부 readout 까지로 *self-limited*.

### §4.3 σ-rich 가 D_0 의 부분일 가능성 검토

σ_rich 는 *u_t 위에서 정의되는* (post-stabilization) derived diagnostic. 즉 *D_2 readout* 이지 D_0 가 아님. centroid·orientation·sigma_standard 가 *공간상 feature dimension* 처럼 보이지만, 모두 *u_t 의 H_0 bar 위에서 계산* (u_t 가 이미 응집 후).

→ σ_rich ≠ D_0.

### §4.4 OMS (Observer Moduli Space) 가 D_0 의 부분일 가능성 검토

OMS-2.0 (canonical Appendix OMS) 는 *observer parameter space* — 관찰자의 weight / threshold configuration 의 stratification. 즉 *D_2 readout 의 보조 공간*이지 D_0 가 아님 (observer 는 응집 *후* 의 해석자).

→ OMS ≠ D_0.

### §4.5 OP 들이 D_0 를 가리키는가

검토할 OP 목록 (`theorem_status.md` §"Open Problems Catalog"):

- **OP-0001 (F-1 follow-up, RESOLVED CV-1.3)** — F-1 의 SPLIT-RESOLVED 와 MO-1 rider. D_1/D_2 영역.
- **OP-0003 (M-1, LAYER-CLARIFIED)** — pure E_bd vs full E. D_1.
- **OP-0005 (K-Selection, EQ/OBS/DYN)** — D_2 readout dynamics.
- **OP-0006 (T-OP6-B, RESOLVED CV-1.7)** — boundary precision. D_2 readout.
- **OP-0008 (σ^A K-jump non-determinism)** — D_2 readout in K-jump events.
- **OP-0009 (Multi-Formation Ontological Foundations)** — D_1/D_2 architectural.
- **OP-0011 (Temporal Identity, RESOLVED CV-1.12)** — D_1 시간연결.
- **OP-0012 (Composition, sub-items SINK/CC/Kjump/Markov)** — D_1 시간연결 +.
- **OP-0021 (T_* registration, OPEN W9+)** — stochastic dynamics axiom. D_1.
- **OP-HMORSE-LOCAL-A / SBM / BROADNESS-CLOSED / SADDLE** — D_1 Hessian regularity (Q3 Package II).
- **OP-SB1-DEEP / OP-SB1-084** — D_1 deep-core density.

**관찰**: 등재된 ~20개 OP 중 *D_0 generation / multi-channel sensor 차이 생성* 을 직접 다루는 OP 는 **0개**. 모두 D_1 (응집 중 구조) 또는 D_2 (응집 후 readout) 영역.

### §4.6 N-1 (Soft-Hard Switching Asymmetry) — `working/open_problems_reframing_2026-04-19.md`

`open_problems_reframing_2026-04-19.md` 은 F-1/M-1/MO-1 을 N-1 (Soft-Hard Switching Asymmetry) 로 통합 재프레이밍. N-1 은 *K 를 정수로 취급할 것인가 연속으로 취급할 것인가* 의 문제 — **D_2 의 셈 단계 ontology** (Commitment 16 의 K_field/K_act 분해가 이를 부분 해소).

N-1 ≠ D_0 problem.

### §4.7 D_0 inventory 결론

| 사용자 통찰 (D_0 측) | canonical 대응 | 위치 | 분류 |
|---|---|---|---|
| 다채널 감각 미분장 ($z_t : X_t \to \mathcal{F}$) | (해당 primitive 없음) | — | **canonical 부재** |
| 색·밝기·깊이·질감의 약한 차이 분포 | X_t 내부 feature 구조 | §3.2 modeling layer note | **명시적으로 외부** |
| feature-space similarity kernel ($K_{z_t}$) | N_t (primitive form) | §3.5, B1-B4 | *형태적 동일* (Stage 3 참조) |
| D_0 → D_1 generative arrow | (canonical 화살표 시작점 위쪽) | DECLARATION 화살표 | **명시적으로 외부** |
| D_0 의 변동성 / 다채널 통합 problem | (해당 OP 없음) | OP 0건 | **부재** |

**D_0 정량 평가**: 사용자 통찰의 D_0 측면 *그 자체로서의 generation* 은 **canonical 의 명시적 외부**. DECLARATION 의 화살표 시작점이 D_1 (=차이 의 발생 후 응집) 인 한, "감각장 → 차이의 발생" 의 *수학화* 는 SCC 의 범위 밖. 

다만 **N_t 의 출처** 가 *암묵적으로 외부에 위임* 된 상태인 것은 사실 — 즉 canonical 은 D_0 부재의 *공백을 명시* 하나, 그 공백을 *채울 수학* 은 갖고 있지 않다. 이것이 Decision A/B/C 결정의 핵심 정보다.

---

## §5. 통찰 화살표 자체 $u^* \to S_0(u^*) \to K_{\mathrm{read}}$ inventory

사용자 통찰의 핵심 화살표 (`00_plan §Mission`):

$$u^* \to S_0(u^*) \to K_{\mathrm{read}}$$

각 단계 위치 매핑:

| 단계 | 사용자 표현 | canonical 대응 | 위치 | 분류 |
|---|---|---|---|---|
| $u^*$ | "응집된 cohesion field" | $u^* = \arg\min_{\Sigma_m} E(u)$ | §3.3 + §7 | **이미 담김** |
| $S_0(u^*)$ | "응집된 구조의 데이터 표현" | $(\mathrm{PersComp}(u^*), \sigma_{\mathrm{rich}}(u^*))$ | §3.11 + σ_rich | **이미 담김** |
| $K_{\mathrm{read}}$ | "셈으로의 readout" | $K_{\mathrm{act}}(u^*) = \#\mathrm{PersComp}(u^*)$ | §3.11 | **이미 담김** |
| 화살표 자체 | "방향: 응집 *후* 셈" | T-L1-F, T-L1-M, Comm.16 (ii) | §13 Cat A | **이미 담김 (Cat A 조건부)** |

**판정**: $u^* \to S_0(u^*) \to K_{\mathrm{read}}$ 화살표는 *canonical 내부에 완전히 존재* 한다 — definition (§3.11) + Cat A 조건부 정리 (T-L1-F/M) + Commitment 16 (ii) 의 조합.

---

## §6. Stage 1 의 정량 평가

D_0 / D_1 / D_2 의 *통찰 담김 비율*:

| 층 | 담김 정도 | 핵심 증거 |
|---|---|---|
| **D_2** | **~95% 담김** | §3.11 + Comm.16 + T-L1-F/M (Cat A 조건부) + σ_rich (derived) + T-OP6-B (Cat A); 잔여: σ_standard MERGE/SPLIT Cat C, K-Select-DYN Cat B |
| **D_1** | **~100% 담김 (by design)** | §3.3 u_t + §7 4-에너지 + Group A-E 공리 + T8 + T-PreObj-1/G + T-Temporal-Identity + L-CLOSURE-LIFT (CV-1.16) |
| **D_0** | **~0% 담김 (by design)** | DECLARATION 화살표 명시적 외부; canonical 의 primitive 계층에 feature field 없음; N_t 는 출처 미규정 primitive; OP 0건 |

**중요 관찰**: 사용자 통찰의 *셋 중 두 층 (D_1, D_2)* 은 canonical 의 *본체*. *D_0 만이 canonical 외부*. 그러나 D_0 외부화는 **DECL-1.0 의 self-declaration** — 즉 사용자 본인의 *의도된 self-limitation* 의 결과.

---

## §7. Stage 1 → Stage 2 연결 메모

Stage 2 (`03_insight_decomposition.md`) 에서는 통찰을 *최소 명제 단위* 로 분해한다. Stage 1 inventory 가 이미 보여준 결정적 사실 두 가지를 잊지 말 것:

1. **D_0 는 canonical 의 *명시적* 외부** (DECL-1.0 화살표 + §3.2 modeling layer note). 따라서 D_0 를 SCC *내부* 수학으로 끌고 들어오는 시도는 *DECLARATION 의 수정* 을 동반한다.
2. **z_t 제안 (`01b`) 은 N_t 의 출처를 *외부 modeling* → *theory primitive* 로 끌어내림** — 즉 *DECLARATION 화살표의 시작점을 위로 이동* 하려는 시도다. 이 시도가 (a) 새 수학을 산출하는지, (b) 단순한 vocabulary 재배치인지가 Stage 3–5 의 핵심 질문.

또한 Stage 4 의 *§8-5 ("proxy 아닌 이유") 검증* 을 위해 다음 사전 자료가 필요:

- $K_{z_t}(x,y) = \exp(-d_X^2/2\rho^2)\exp(-d_\mathcal{F}^2/2\sigma^2)$ 는 다음 표준 도구와 *수식 형태로 동일*:
  - **Bilateral filter** (Tomasi-Manduchi 1998): spatial Gaussian × range Gaussian
  - **Diffusion maps kernel** (Coifman-Lafon 2006): 동일한 product Gaussian
  - **Mean-shift kernel** (Comaniciu-Meer 2002): 동일한 형태
  - **Self-tuning spectral clustering** (Zelnik-Manor-Perona 2004): per-site bandwidth 의 동일한 product
- 즉 *kernel 형태만으로는* SCC 와 위 도구들이 *수식 수준에서 동일*. 차이는 *kernel 이후 무엇을 하는가* — SCC 는 energy minimization on $\Sigma_m$, 위 도구들은 spectral embedding / mean-shift / cluster assignment. 이 차이가 §8-5 verification 의 *결정적 위치*.

---

*Stage 1 종료. Stage 2 (`03_insight_decomposition.md`) 진입.*
