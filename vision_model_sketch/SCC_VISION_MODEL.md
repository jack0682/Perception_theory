# SCC 기반 비전 모델 — 아이디어 청사진

> **상태**: 탐색적 (exploratory). canonical이 아님.
> **작성일**: 2026-04-26
> **위치 정당화**: 이 문서는 이론(`THEORY/`)도 코드(`CODE/`)도 아닌 *응용 아이디어*다. 이론 작업과 명확히 분리하기 위해 별도 디렉토리에 둔다.

---

## 0. 한 줄 요약

> 픽셀 → 응집장(cohesion field) → 자기참조 평형 → 4차원 진단 벡터.
> 라벨 없이도 *사물스러움 자체*를 학습 신호로 쓰는 비전 모델.

---

## 1. 왜 이런 모델이 필요한가

기존 비전 모델은 거의 모두 **"사물이 거기 있다"는 가정에서 출발**한다:
- ImageNet 분류: 객체가 있다 → 클래스를 맞혀라
- COCO detection: 객체가 있다 → 위치를 찾아라
- Segmentation: 객체가 있다 → 마스크를 그려라

**비어있는 자리**: "사물이 *어떻게 사물이 되는지*"에 대한 모델은 없다.

SCC는 정확히 그 빈자리를 다룬다 (T-PreObj-1G Cat A: 사물-이전성은 임의의 유한 연결 그래프에서 증명된 정리).
이론을 비전에 응용한다는 것은 **그 빈자리를 채우는 모델을 만든다**는 뜻이다.

### 표면적 응용 vs. 본질적 응용

- **표면적 응용** (이전 답변에서 다룬 것): 기존 비전 모델 출력에 4차원 점수를 매기는 wrapper
- **본질적 응용** (이 문서): 이론의 핵심 메커니즘을 그대로 구현한 *새 아키텍처*

이 문서는 후자에 집중한다.

---

## 2. 핵심 아키텍처 청사진

```
이미지 (H×W×3)
   ↓
[백본: CNN 또는 ViT]   ← 표준 비전 기술 그대로
   ↓
특징맵 (H'×W'×C)
   ↓
[응집장 헤드]   ← 새로움 시작
   ↓
u^(0) ∈ [0,1]^(H'×W')   초기 응집 추정
   ↓
[폐포 평형 모듈]   ← Cl 연산자 반복, T6b 수렴 보장
   ↓
u* (자기참조 평형 응집장)
   ↓
[분리장 모듈]   ← D(x; 1-u) 계산
   ↓
D 맵
   ↓
[에너지 헤드 + 4차원 진단]
   ↓
출력:
  - u* (graded mask)
  - d = (Bind, Sep, Inside, Persist) ∈ [0,1]^4
  - 에너지 분해: (E_cl, E_sep, E_bd)
  - (선택) 클래스 분류 헤드
```

### 핵심 차이점
- 출력이 *라벨이 아니다* (라벨은 옵션).
- 출력이 *graded mask* + *4차원 점수*.
- **마지막 부분이 미분 가능한 변분 평형**이지 단순 forward pass가 아니다.

---

## 3. 레이어별 상세

### 3.1 백본 (변경 없음)
- ResNet, ConvNeXt, ViT, Swin 등 표준 백본
- 출력: 특징맵 $F \in \mathbb{R}^{H' \times W' \times C}$
- 사전훈련된 가중치 그대로 사용 가능 (DINO, MAE, CLIP backbone 등)

### 3.2 응집장 헤드
$F$를 $u^{(0)} \in [0,1]^{H' \times W'}$로 매핑:
```python
u_init = sigmoid(Linear(F))  # 1채널 출력
```
또는 K개 형태 동시 처리:
```python
u_init_K = softmax(Linear(F), dim=-1)  # K채널, 합=1 (simplex 제약)
```

### 3.3 폐포 평형 모듈
가장 중요한 부분. 이론의 핵심을 그대로 옮긴다:

```python
def closure_equilibrium(u, F, n_iter=10, tol=1e-4):
    for k in range(n_iter):
        # P_t u: 이웃 가중평균 (그래프 메시지 패싱)
        Pu = neighborhood_aggregate(u, kernel=N_t)

        # Cl_t(u): 시그모이드 closure
        z = a_cl * ((1 - eta) * u + eta * Pu - tau_cl)
        u_new = torch.sigmoid(z)

        if torch.norm(u_new - u) < tol:
            break
        u = u_new
    return u  # 평형 응집장 u*
```

수학적으로:
- $a_{\mathrm{cl}} < 4$이면 Banach 수축 (T6b Cat A) → 수렴 보장
- 미분 가능 (implicit function theorem 또는 unrolled iteration)
- *학습 가능 매개변수*: $a_{\mathrm{cl}}, \eta, \tau_{\mathrm{cl}}$, kernel weights

이 모듈은 **DEQ (Deep Equilibrium Model, Bai et al. 2019)와 본질적으로 같은 구조**를 가진다.
즉 GPU 친화적이고 구현 노하우가 이미 있다.

### 3.4 분리장 모듈
```python
def distinction(u, F):
    Pu = neighborhood_aggregate(u)
    P_neg = neighborhood_aggregate(1 - u)
    z = a_D * (Pu - lambda_D * P_neg) - tau_D
    return torch.sigmoid(z)
```

### 3.5 경계/형태 측정
$\mathcal{Q}_{\mathrm{morph}}$는 persistence homology를 사용하므로 GPU에서 어렵다. 두 가지 길:

**Option A**: 미분 가능한 persistence (Carrière et al., 2021의 `gudhi` GPU 포팅) 직접 사용. 정확하지만 느림.

**Option B**: Smoothness 페널티 + double-well로 근사:
```python
E_bd = alpha * laplacian_quadratic(u) + beta * double_well(u)
```
이건 즉시 미분 가능하고 빠르다. Q_morph 자체는 별도로 후처리에서 계산.

### 3.6 4차원 진단 벡터 (출력)
```python
def diagnostic_vector(u, Cl_u, D_u):
    Bind   = 1 - torch.norm(u - Cl_u) / sqrt(n)
    Sep    = (u * D_u).sum() / u.sum()
    Inside = Q_morph(u)         # persistence-based or 근사
    Persist= core_inheritance(u_t, u_s, M)  # 영상의 경우
    return torch.stack([Bind, Sep, Inside, Persist])
```

---

## 4. 손실 함수

### 4.1 자기지도학습 손실 (라벨 없음)

$$\mathcal{L}_{\mathrm{SSL}} = \lambda_{\mathrm{cl}} E_{\mathrm{cl}} + \lambda_{\mathrm{sep}} E_{\mathrm{sep}} + \lambda_{\mathrm{bd}} E_{\mathrm{bd}} + \lambda_{\mathrm{vol}} (||u||_1 - m)^2$$

- $E_{\mathrm{cl}} = \sum (u - \mathrm{Cl}(u))^2$
- $E_{\mathrm{sep}} = \sum u (1 - D(x; 1-u))$
- $E_{\mathrm{bd}} = \alpha \cdot \mathrm{Laplacian} + \beta \cdot \mathrm{DoubleWell}$
- 부피 제약: m은 hyperparameter 또는 학습됨

이 손실 *하나만으로* 모델이 "사물스러운" 응집장을 출력하도록 강제된다.

### 4.2 시간적 일관성 손실 (영상)

$$\mathcal{L}_{\mathrm{tr}} = \mathrm{Sinkhorn}(u_t, u_s; c)$$

여기서 비용 $c$는 *cohesion fingerprint* $\varphi(x) = (u(x), \mathrm{Cl}(u)(x), D(x; 1-u))$ 사이의 거리.
T-Persist-1(e)가 보장: 핵-대-핵 매칭이 지수적으로 집중된다.

### 4.3 (선택) 라벨 손실
```python
L_total = L_SSL + L_tr + lambda_cls * CrossEntropy(classifier(u, F), label)
```
라벨이 *있을 때만* 추가. 모델은 라벨 없이도 작동.

---

## 5. 추론 시 출력의 종류

이 모델 하나가 여러 작업을 *동시에* 한다:

| 출력 | 형태 | 어디에 쓰나 |
|---|---|---|
| $u^*$ | $H' \times W'$ graded mask | soft segmentation |
| $\mathcal{F}(u^*)$ | int | 객체 카운팅 (라벨 없이) |
| $d$ vector | $\mathbb{R}^4$ | 객체-스러움 점수, OOD 감지 |
| 에너지 분해 | $(E_{\mathrm{cl}}, E_{\mathrm{sep}}, E_{\mathrm{bd}})$ | 어떤 조건이 충족 안 되는지 진단 |
| transport plan $M$ | sparse matrix | 시간적 ID 유지 |
| Hessian eigenvectors | 모드들 | $\sigma$-signature, 형태 분류 |

**한 forward pass가 여러 작업의 답을 동시에 낸다.** 기존 비전 모델은 작업마다 head가 다른데, SCC 모델은 통합된 출력 구조를 가진다.

---

## 6. 사전 연구와의 관계

### 6.1 Slot Attention (Locatello et al. 2020)
- **공통**: 객체-중심 표현 학습, 라벨 없는 분해
- **차이**: Slot은 *왜 K개인지*에 이론이 없음. SCC는 K-field architecture(`scc/multi.py`) + T-Persist-K-Sep/Weak/Unified가 답을 줌.
- **통합 가능**: Slot의 K슬롯 위에 SCC 4차원 점수를 측정해 슬롯 품질 향상.

### 6.2 GLOM (Hinton 2021)
- **공통**: 부분-전체 계층, 자기참조적 합의
- **차이**: GLOM은 architecture 제안이고 작동 모델 없음. SCC는 정리 + 코드(`scc/`)가 있음.
- **연결**: GLOM의 "island of agreement"는 SCC의 다중 봉우리 패턴과 본질적으로 같다.

### 6.3 JEPA (LeCun 2023~)
- **공통**: 자기지도, latent 공간 작업
- **차이**: JEPA는 *예측*, SCC는 *형태 형성*. 보완적.
- **통합**: JEPA latent 위에 SCC 헤드를 얹어 두 신호를 함께 사용.

### 6.4 Object-centric SSL (MONet, IODINE, SAVi)
- **공통**: 비지도 객체 발견
- **차이**: 이들은 VAE/recurrent 기반 휴리스틱. SCC는 변분 원리에서 유도.
- **벤치마크**: CLEVR, MOVi 같은 합성 데이터에서 직접 비교 가능.

### 6.5 DEQ (Bai et al. 2019)
- **공통**: implicit equilibrium, 무한 깊이
- **차이**: DEQ는 일반 평형. SCC는 *특정한 변분 평형*(폐포 + 분리 + 형태).
- **활용**: DEQ의 implicit differentiation 코드를 그대로 빌려 쓸 수 있음.

### 6.6 Differentiable Persistent Homology (Carrière et al.)
- **공통**: TDA의 미분가능 버전
- **차이**: 이들은 도구 제공. SCC는 *왜* TDA가 의미 있는지 이론(Q_morph, CN12)을 줌.
- **활용**: $\mathcal{Q}_{\mathrm{morph}}$ 정확 계산에 직접 사용.

---

## 7. 첫 실험 3가지 (구체적, 빠르게 시도 가능)

### 실험 1: 4차원 점수 wrapper (1~2주)
- **목표**: 기존 SAM/Mask2Former 출력에 SCC 점수 매기기
- **구현**: `scc/diagnostics.py`를 PyTorch로 포팅, 이미지 마스크 입력 받게 wrapper
- **측정**: GT 라벨이 있는 데이터셋(COCO)에서 4차원 점수와 IoU의 상관관계
- **성공 기준**: $r > 0.7$ 상관관계 → 4차원 점수가 라벨 없는 품질 신호로 작동

### 실험 2: SSL 손실 추가 (1~2개월)
- **목표**: 기존 segmentation 네트워크를 SCC 손실로 finetuning
- **구현**: U-Net 또는 작은 ViT-based segmentation head + $\mathcal{L}_{\mathrm{SSL}}$
- **데이터**: CLEVR (라벨 없이) + COCO (라벨 부분 사용)
- **측정**:
  - CLEVR에서 라벨 없이 객체 발견 정확도
  - COCO에서 데이터 효율성 (10% 라벨로 100% 라벨 baseline에 얼마나 근접)
- **성공 기준**: 라벨 효율 1.5× 이상

### 실험 3: 비디오 객체 항상성 (3~6개월)
- **목표**: 가려짐을 견디는 객체 ID
- **구현**: 백본 + 응집장 헤드 + transport 모듈, T-Persist-1 형태로 학습
- **데이터**: MOVi, OcclusionVID
- **측정**: 가려짐 후 ID 복원 성공률
- **성공 기준**: 기존 SOTA 트래킹 +5% 이상

이 셋이 *순차적*으로 구현되어야 함. 1번이 작동해야 2번이 의미 있음.

---

## 8. 이론에서 *먼저* 해결되어야 할 것

응용을 진지하게 시작하기 전에 이론에서 닫혀야 할 것:

### 우선 (필수)
- **OP-0005 K-selection 메커니즘** — 모델이 *몇 개* 형태인지 알아야 함. σ-framework가 부분답을 줬지만 미완.
- **다중-형태 σ 확장 (Phase 5)** — 단일 형태 σ는 닫혔지만 multi-formation σ는 미해결. 비전의 "복수 객체"를 다루려면 필수. 단, MO-1 (Morse on $\Sigma^K_M$)이 여기서 다시 활성화됨.

### 권장 (있으면 더 좋음)
- **OP-0011 운반 커널 유일성** — 다른 운반 형태가 가능한지. 현 implementation의 *유일성* 보장이 없음.
- **연속 극한 (OP-0022)** — 픽셀 → 픽셀 사이 보간을 정당화하려면.

### 없어도 시작 가능
- 표면적 4차원 점수 wrapper 정도는 위 모든 미해결 문제를 우회.
- 본격적인 end-to-end 모델은 위 두 우선 항목 해결 후.

---

## 9. 이미 있는 코드 자산

`Perception_theory/CODE/scc/`에서 직접 재사용 가능한 모듈:

| 모듈 | 용도 | 재사용 |
|---|---|---|
| `graph.py` | GraphState (Laplacian, Fiedler) | 이미지 그리드 그래프로 변환 후 사용 |
| `params.py` | ParameterRegistry (a_cl<4 검증) | 학습 매개변수 검증에 직접 사용 |
| `operators.py` | Cl, D, P_t + JVP | PyTorch autograd 호환으로 포팅 |
| `energy.py` | E_cl, E_sep, E_bd 정확 gradient | 손실 함수에 직접 |
| `optimizer.py` | semi-implicit projected gradient | 추론 시 평형 찾기 |
| `diagnostics.py` | Bind, Sep, Inside, Persist | 4차원 점수 헤드 |
| `multi.py` | K-field, transport_k_formations | 다중 객체 슬롯 |
| `transport.py` | log-domain Sinkhorn + cohesion fingerprint | 시간적 매칭 |

**이론 코드 → 비전 코드 포팅의 핵심 작업**:
- numpy → torch
- CPU → GPU
- 명시적 Jacobian → autograd
- 그래프 인덱스 → 이미지 픽셀 좌표

추정 작업량: 한 사람 2~3개월 (테스트 포함).

---

## 10. 가능한 응용 도메인 (어디서 SOTA를 이길 수 있는가)

이 모델이 *모든 비전 작업*에서 이기진 않는다. 다음에서 명확한 우위 예상:

| 도메인 | 우위 이유 | 신뢰도 |
|---|---|---|
| **비지도 객체 발견** | 4차원 점수가 클래스 의존적이지 않음 | 높음 |
| **객체 항상성 (가려짐)** | T-Persist-1(b) IFT 안정성이 수학적 보장 | 높음 |
| **클래스 없는 카운팅** | $\mathcal{F}$가 정확히 답 | 매우 높음 |
| **OOD / Anomaly** | 4차원 점수가 낮으면 비정상 | 중간~높음 |
| **의료영상 (라벨 부족)** | SSL 신호로 라벨 효율 ↑ | 중간 |
| **위성영상 (새 카테고리)** | 객체-스러움 자체 학습 | 중간 |
| **로보틱스 (시간 일관성)** | persist 보장이 SLAM·tracking에 직결 | 높음 |
| ImageNet 분류 | ResNet이 더 빠름 | 낮음 (이기지 않음) |
| COCO detection | 표준 detector가 성숙 | 낮음 |

---

## 11. 현실적 타임라인

전제: 박사 2~3명 또는 그에 준하는 연구 인력.

| 시점 | 마일스톤 |
|---|---|
| 0~3개월 | 4차원 점수 wrapper, 실험 1 |
| 3~9개월 | SSL 손실 학습, 실험 2 |
| 9~18개월 | end-to-end SCC 모델, 단일 형태 |
| 18~30개월 | 다중 형태 σ 통합, 영상으로 확장 |
| 30~48개월 | 객체 항상성 SOTA 도전 |
| 48개월~ | 일반 비전 백본 후보로 |

이 사이에 *이론* 쪽에서 OP-0005, Phase 5가 풀려야 함.

---

## 12. 위험 / 함정

### 함정 1: 이론을 *알고리즘*으로 환원
canonical CN10이 명시: contrastive 비교는 OK, reductive 동일시는 금지.
모델을 만들 때 "SCC = soft segmentation"이라고 부르고 싶은 유혹이 클 것.
*이론의 깊이*(사물-이전성)는 그 환원에서 사라진다.

### 함정 2: 매개변수 폭발
$\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, a_{\mathrm{cl}}, \tau_{\mathrm{cl}}, a_D, \lambda_D, \tau_D, m, ...$
이걸 다 학습 가능하게 두면 학습이 불안정.
이론에서 안 묶이는 부분은 hyperparam search 비용이 큼.
**해결**: 일부는 고정 (이론 권장값), 일부만 학습 가능.

### 함정 3: K 선택 회피하기
"K는 hyperparameter다"라고 두면 일반화 안 됨.
이미지마다 객체 수가 다른데. K-selection이 미해결인 한, 일반 비전 모델로의 길은 막혀 있음.

### 함정 4: 평형이 안 모이는 경우
$a_{\mathrm{cl}} \geq 4$로 학습이 흐를 수 있음.
**해결**: 매개변수 projection (각 step 후 $a_{\mathrm{cl}} = \min(a_{\mathrm{cl}}, 3.99)$).

### 함정 5: 학습된 모델이 *이론적 의미*를 잃음
손실에 SCC를 추가했는데, 모델이 그저 다른 SOTA만큼 작동하면 — 4차원 점수가 단지 fancy regularizer로 끝남.
*이론적 우위가 발현되는 영역*(객체 항상성, 비지도 발견)을 명시적 평가 항목으로 삼아야.

---

## 13. 개방 질문 (이 디렉토리를 다시 들여다볼 때 검토)

1. **K-selection (OP-0005)**이 풀렸는가? 풀렸다면 어떻게? 모델에 어떻게 통합?
2. **다중-형태 σ Phase 5** 진행 상황? Multi-formation Morse on $\Sigma^K_M$?
3. **MO-1 (stratified Morse)** 활성 여부?
4. SCC 코드(`scc/`)에 GPU 친화적 변환이 있었는가?
5. 누군가 비슷한 비전 모델을 발표했는가? (Slot Attention 후속, JEPA 후속)
6. ICLR/NeurIPS에 "object-centric + variational" 조합 논문이 있었는가?
7. Persistent homology의 GPU 라이브러리가 성숙했는가?
8. 이론에서 추가 정리가 비전 응용에 직접 영향을 주었는가?

---

## 14. 한 줄 결론

> **"이 비전 모델은 만들 수 있다. 청사진은 명확하다. 하지만 이론이 OP-0005와 Phase 5에서 닫히기 전에는 본격 시작하지 않는 것이 좋다. 그 사이에 4차원 점수 wrapper(실험 1)는 즉시 가능하고 의미 있다."**

---

## 부록 A: 가장 빠른 첫 실험 (코드 스케치)

```python
# scc_score_wrapper.py
import torch
from PIL import Image
from segment_anything import SamPredictor  # 외부 segmentation
from scc_torch import diagnostic_vector    # 새로 만들 PyTorch 포팅

def score_mask(image, mask):
    """주어진 마스크의 4차원 SCC 점수."""
    u = mask.float()
    Cl_u = closure_equilibrium(u, image)
    D_u  = distinction(u, image)
    return diagnostic_vector(u, Cl_u, D_u)

# 사용
sam = SamPredictor(...)
masks = sam.predict(image)
scores = [score_mask(image, m) for m in masks]
# scores[i] = (Bind, Sep, Inside, Persist)
# 가장 좋은 마스크: argmax(scores.mean(dim=-1))
```

이 정도면 첫 결과를 한 주 안에 볼 수 있다.

---

## 부록 B: 이론과의 정확한 대응

| 이론 (canonical) | 모델 (이 청사진) |
|---|---|
| §3.3 응집장 $u_t$ | 응집장 헤드 출력 |
| §3.4 폐포 $\mathrm{Cl}_t$ + A1'/A2/A3/A4 | 폐포 평형 모듈 (DEQ-like) |
| §3.7 분리 $\mathbf{D}_t$ | 분리장 모듈 |
| §3.8 운반 $\mathbf{M}_{t \to s}$ | transport head (Sinkhorn) |
| §7 proto-cohesion 4차원 | 4차원 진단 출력 |
| §8 에너지 + 부피 제약 | 손실 함수 |
| §13 T-PreObj-1G | 모델이 다중 봉우리 출력하도록 강제됨 (이론 보장) |
| §13 T-Persist-1(e) | 시간적 head의 학습 안정성 |
| §13 T6b 수축 | 평형 모듈의 수렴 |

---

*문서 끝.*
*다음 검토 권장 시점: OP-0005 또는 Phase 5에 진전이 있을 때.*
