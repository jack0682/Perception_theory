---
id: UNIFIED_STRUCTURE
type: axis/unification-candidate
created: 2026-05-26
status: CANONICAL-DIRECTION / NOT YET FORMALIZED (candidate generating structure; 0 proofs; substrate unchanged)
description: 누적된 8개 이론 결이 하나의 생성구조 𝕌의 단면(section)·판독(readout)·전송(transport)·좌표(chart)임을 제시하는 수학적 단일화 후보. 증명 0건. substrate(102 claims) 불변. Prolegomena 위치 확정 포함.
---

> [!nav] Parent: [[THEORY_INDEX]] · Pair: [[THREAD_ATLAS]] · [[CANONICAL_AXIS]] · [[DECLARATION]] · Substrate: [[canonical]]

# Unified Structure — 하나의 생성구조와 그 단면들

> [!warning] 상태 (구속력 있음)
> 본 문서는 **후보 생성구조**다 — *증명된 정리가 아니다*. PAI pivot과 동일한 `CANONICAL-DIRECTION` 등급. 증명 0건, 새 canonical claim 0건. substrate 102 정리는 봉인·불변. 아래 정의는 **타입(typing) 수준에서만 정합적**이며, 존재성·정합성은 OPEN(OP-UNIFY-1..3).

## 동기

[[THREAD_ATLAS]]가 보이듯, 8개 결은 모두 소수의 공유 대상으로 환원되고 분열은 *프레임*에서 일어났다. 단일화의 주장은 다음이다:

> **누적된 모든 결은 하나의 생성구조 𝕌의 단면·판독·전송·좌표·추상단계다. 결들이 갈라진 것은 각자 𝕌의 다른 부분을 고정하고 국소 어휘를 썼기 때문이며, 𝕌의 관점에서 다시 하나로 묶인다.**

이는 [[CANONICAL_AXIS]]의 "one field → projections"를 *슬로건에서 타입 잡힌 구조로* 끌어올리려는 시도다.

## §1 생성구조 𝕌 (후보 정의)

$$\mathbb{U} \;=\; \Bigl\{\, (G,\; o,\; \theta,\; u) \;:\; G\in\mathcal{G},\ o\in \mathcal{M}_{\mathrm{obs}},\ \theta\in\mathcal{M}_{\mathrm{act}},\ u\in \Sigma_m(G) \,\Bigr\}$$

- **base 장:** $u \in \Sigma_m(G) = \{u:X\to[0,1],\ \sum u = m\}$ — substrate 원초 (결 ①).
- **관측자 모듈라이:** $o \in \mathcal{M}_{\mathrm{obs}}$ — 기존 OMS의 $\mathfrak{M}^{\mathrm{obs}}_{\mathrm{SCC}} = \mathcal{M}_{\mathrm{obs}}/G^{(0)}_{\mathrm{SCC}}$ (결 ⑤ observer_moduli). 결 ③④⑨의 "관측자 색인/번역" 어휘가 여기로 수렴.
- **행동/체화 모듈라이:** $\theta \in \mathcal{M}_{\mathrm{act}}$ — DECL-2.0의 체화 파라미터 $\Theta$ (reach/kinematics/end-effector). action-class 선택이 여기 산다.
- **에너지:** 각 fiber에 $E_{o,\theta}[u]$. *현재 substrate에서는 $E$가 $(o,\theta)$-무관* (순수 형태론). $E$가 관측자/행동 조건부인지 = **OP-UNIFY-3 = OP-ACTIONAL-U**.

𝕌 위에 **판독 필트레이션(readout filtration)** $\mathcal{R} = \{\sigma,\ K,\ \pi\}$ 를 얹는다:
- $\sigma$-판독 (지문), $K$-판독 (개수), $\pi$-판독 (사영다발). 아래 §3.

## §2 모든 결 = 𝕌의 한 부분

| 결 | 𝕌에서의 역할 | 형식 |
|---|---|---|
| ① SCC substrate | 고정 $(o,\theta)$에서의 **fiber + 에너지** | $u\in\Sigma_m(G)$, $\min E$ |
| ② PAI 사영 | **판독 사상** $\pi_\bullet:\mathbb{U}\to$ (action-class 타깃) | $\{\pi_{\mathrm{obj}},\pi_{\mathrm{aff}},\pi_{\mathrm{act}},\pi_{\mathrm{ctrl}},\pi_{\mathrm{time}},\pi_{\mathrm{sem}}\}$ |
| ③ Sensing(SSKP) | **상류 chart**: raw→base로 가는 커널 cascade | $\mathcal{K}_i:\mathcal{S}_{i-1}\to\mathcal{S}_i$ → $u$ 생성 |
| ④ PFE (cone/field-eq) | **기하 chart**: $\sigma$를 Minkowski cone, $E$를 stress-energy로 | $g^{(s)}_{\mu\nu}$, $G_{\mu\nu}=\kappa T_{\mu\nu}$ |
| ⑤ AFD | **추상 단계**: order(전이순서) ⟂ rate(전이율) | formation 그래프 $G_{\mathrm{form}}$ |
| ⑥ Multi-K | base **판독(quotient)**: counting functional | $K_\bullet = N_\bullet(u)$ |
| ⑦ σ-framework | base **판독(filtration)**: 지문 정련 | $\sigma_{\mathrm{std}}\subset\sigma_{\mathrm{rich}}\subset\sigma_{T4}\subset\sigma_{\mathrm{inherit}}$ |
| ⑧ Temporal | fiber **전송/접속(connection)** | $M_{t\to s}$, identity = 전송 불변, action-cost = 경로길이 |
| ⑨ Prolegomena | 𝕌의 **base/observer 공리 스펙** | 44 조건 → §4 |

**관건:** 결 ③④⑤와 prolegomena의 4-layer/3-layer/5-stage/NS-무차원수는 *경쟁 이론이 아니라 𝕌의 atlas(좌표·추상단계의 모음)*다. 서로 다른 chart에서 같은 대상을 본 것.

## §3 판독 필트레이션 — 세 결을 하나로

세 substrate-판독은 같은 superlevel 구조의 서로 다른 functional이다:

- **$\sigma$ (결 ⑦):** $\sigma_{\mathrm{std}}$(이진 도달, 봉인) → $\sigma_{\mathrm{rich}}$(centroid·orientation·Wigner, Lipschitz $L_K\le 4L_\phi n$) → $\sigma_{T4}$(H-σ4 차단) → $\sigma_{\mathrm{inherit}}$(시간, Cat C). *하나의 도달관계의 연속 정련*.
- **$K$ (결 ⑥):** $K_{\mathrm{field}}$(chart 파라미터) · $K_{\mathrm{act}}^\varepsilon$(임계 quotient) · $K_{\mathrm{soft}}^\phi$(persistence quotient) · $K_{\mathrm{bar}}$(성분 quotient). 모두 $N_\bullet(u)$; **count-bridge**가 일치 조건. → K_bar/K̂은 형식화 or 은퇴.
- **$\pi$ (결 ②):** action-class별 사영다발. $\pi_{\mathrm{obj}}$는 $\sigma,K$ 판독에 의존 → 즉 *objecthood = 안정화된 affordance 판독*.

판독들이 서로 정합적 단면을 이루는가? = **OP-UNIFY-2 = OP-PROJECTION** (count-bridge의 일반화).

## §4 Prolegomena 위치 확정

**결정:** prolegomena의 44 조건(`3_projections/prolegomena/00,01`)은 *별도의 경쟁 프레임이 아니라* **𝕌의 base+observer 구조에 대한 공리적 스펙**이다 — "관측자 위의 perception 장이 만족해야 할 것". 따라서 prolegomena는 단일화 안으로 흡수된다(떠 있는 9번째 결 해소).

- **매핑됨(전제 어휘):** C6/C7(관측자 색인·번역) → $\mathcal{M}_{\mathrm{obs}}$ (OMS); 자기조직/자율 → $E$ 경사류 + closure A3; 연속성 → A4. 이들은 𝕌의 *기존 정의로 환원*.
- **미매핑(미래 형식화):** prolegomena의 4-layer 후보(McKean-Vlasov / NCG / AQFT / Topos)와 N/S/O 등급의 미해결 조건은 **OP-PROLEGOMENA**로 명시 deferral. 채택 0 — 후보일 뿐.
- 02_framework_skeleton의 4-layer는 §2 의미에서 𝕌의 *추상 단계 atlas*로 재배치(경쟁 아키텍처 아님).

## §5 Open Problems (등록)

| OP | 질문 | 관계 |
|---|---|---|
| **OP-UNIFY-1** | $\mathbb{U}=(\Sigma_m$ over $\mathcal{M}_{\mathrm{obs}}\times\mathcal{M}_{\mathrm{act}})$ 가 단일 정합 객체로 존재/well-defined 한가? (OMS·Θ·Σ_m 합성) | 신규 |
| **OP-UNIFY-2** | 판독 $\{\sigma,K,\pi\}$ 가 상호 정합적 단면인가? (count-bridge 일반화) | = **OP-PROJECTION** |
| **OP-UNIFY-3** | $E$가 관측자/행동 조건부 $E_{o,\theta}$ 인가, 보편인가? | = **OP-ACTIONAL-U** |
| **OP-PROLEGOMENA** | 44 조건 중 무엇이 𝕌의 공리(전제)이고 무엇이 미래 형식화 대상인가 | 신규 |

모두 OPEN, 증명 0. (formal entry는 `theorem_status.md` Open Problems Catalog에 후속 등록 — carry-forward.)

## §6 가드레일 (non-overclaim)

1. 𝕌는 *후보 생성구조*다 — 존재성(OP-UNIFY-1)이 증명되기 전까지 canonical 객체가 아니다.
2. substrate 102 정리·$E$·σ-standard·K_field/K_act 봉인분은 **불변**. 단일화는 그 위의 *조직 프레임*이다.
3. "모든 결이 𝕌의 단면"은 *주장*이며, 각 결→𝕌 환원의 정합성은 OP-UNIFY-2가 검증해야 한다.
4. 8개 retraction 불변; 단일화는 이를 부활시키지 않는다.
5. CV 버전 불변(조직 작업은 claim 수를 안 바꾼다).

## §7 이 문서가 하지 않는 것

- 𝕌의 존재를 증명하지 않는다. 판독 정합성을 증명하지 않는다.
- 결을 물리적으로 병합/삭제하지 않는다(구조적 정리는 별도 선택지였고 미선택).
- prolegomena 후보 수학(Connes/AQFT/Topos)을 채택하지 않는다.

---

*UNIFIED_STRUCTURE, 2026-05-26. 단일화는 방향이다. 하나의 장, 하나의 관측자 모듈라이, 하나의 행동 모듈라이 — 그 위의 판독과 좌표로 모든 결이 다시 하나가 된다. 증명은 OP-UNIFY-1..3.*
