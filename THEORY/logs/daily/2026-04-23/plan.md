# plan.md — 2026-04-23 Session Plan

**Session type:** Stage 2 Axiom Audit + Single-formation 안정화 + Multi-formation bridge + Framework extension.
**Prerequisite:** 2026-04-22 R22 완료 — F1-SSU-v5, S1-S4 axiom candidates, Formation Quantization discovery.
**Session working directory:** `THEORY/logs/daily/2026-04-23/`.

---

## §1. 세션 목표

1. **Single-formation 안정화** — 수학적 foundation 재검토 + 가설 심화
2. **Mathematical function taxonomy** — 급격한 log / logistic / tanh 점근 관점에서 SCC transitions 분류
3. **Single → Multi extension** — Formation Quantization의 multi-K 확장 경로
4. **Time evolution theory 초안** — sharp interface + coarsening dynamics
5. **Stochastic/thermal extensions** — Layer 1 softmax near selector transitions
6. **Application layer scoping** — cognitive science / real-world data applications

---

## §2. Deliverables (6 goals)

### G1 — Single-formation 안정화 검토

**목표**: 72 preserved + 5 new Cat A = 77 Cat A를 Three-Layer Hierarchy로 정확히 분류.

**Outputs**:
- `working/SF/layer_classification.md` (신규) — 77 Cat A theorems을 Layer 1/2/3 table로 정리
- `working/SF/step_cohesion.md` §9 보강 (각 layer별 보강된 theorem list)
- 혹시 missed single-formation gap 존재하면 flag

**Deliverable**: Layer classification table commit, 미분류된 theorem 0개.

### G2 — Mathematical Function Taxonomy

**목표**: SCC의 다양한 transitions을 수학적 함수 class로 분류.

**Function classes 탐구**:
- **급격한 log**: $f(\beta) = \log\!\left(\frac{\beta - \beta_c}{\beta_c}\right)$ — divergent, suited for escape rates
- **Logistic (sigmoid)**: $f(\beta) = \sigma(\kappa(\beta - \beta^*))$ — bounded, smooth crossover
- **Tanh with asymptotes**: $f(\beta) = \tanh((\beta - \beta^*)/\xi)$ — bounded, spatial profile-like
- **Heaviside step**: $f(\beta) = H(\beta - \beta^*)$ — discrete, protocol selector
- **Softmax**: $P_k(\beta) \propto e^{-E_k(\beta)/T}$ — stochastic basin selection

**매핑**:
| SCC 현상 | 가장 fit하는 함수 class |
|---|---|
| K-sector selector | **Heaviside step** (protocol-dependent) |
| Within-basin $\widehat K$ shift | **Logistic / tanh** (smooth) |
| Basin escape time at T>0 | **급격한 log** (Kramers rate) |
| Bistable region probability | **Softmax** (stochastic smoothing) |
| Shape regime transition (D1 α) | **Logistic** in α |
| Static mode count $\nu_k(c)$ | **Rational polynomial** (algebraic) |

**Output**: `working/SF/function_taxonomy.md` (신규) — SCC transitions의 수학 class + 각 class의 수학적 properties + limits.

### G3 — Single → Multi Extension

**목표**: Formation Quantization framework을 multi-formation (K≥2)으로 자연스럽게 확장.

**탐구할 가설들** (pre_brainstorm에서 상세):
- **K-sector basin 분해**: $\Sigma_m = \bigsqcup_K \mathcal{B}_K$, 각 $\mathcal{B}_K$는 K-formation basin
- **$\mathcal{M}_K$ moduli space**: K-formation configurations modulo $\mathrm{Aut}(G)$
- **Inter-sector transitions**: $\mathcal{B}_K \to \mathcal{B}_{K+1}$ via nucleation/coarsening
- **Pair interactions**: K=2 case에서 Hessian block-diagonal + 장거리 coupling $\mu_{\mathrm{sep}} \sim e^{-d/\xi_0}$

**Outputs**:
- `working/MF/multi_quantization.md` (신규) — multi-formation as K-sector family of single-formation theories
- `working/MF/from_single.md` §11-§16 reformulation — R22 Formation Quantization 기반으로 rewrite
- **Proof sketch**: Formation Quantization uniqueness (at least for well-separated case)

### G4 — Time Evolution Theory 초안

**목표**: Sharp-interface dynamics + coarsening framework 시작.

**탐구할 영역**:
- **Sharp interface dynamics**: $u \in \{0, 1\}$ step limit에서 motion by curvature ($v_n = \kappa$)
- **Allen-Cahn dynamics**: $\partial_t u = -\nabla \mathcal{E}(u)$ PDE analysis
- **Coarsening (LSW)**: Large-time multi-formation dynamics, Lifshitz-Slyozov-Wagner theory
- **Nucleation rates**: $\mathcal{B}_0 \to \mathcal{B}_1$ rate via Kramers / Langevin

**Outputs**:
- `working/T/time_evolution.md` (신규 디렉토리 + 파일) — time evolution framework 초안
- 3-4 hypotheses로 Cat C 수준 (exploration)

### G5 — Stochastic / Thermal Extensions

**목표**: Finite-T dynamics + Layer 1 softmax at selector transitions.

**탐구할 영역**:
- **Langevin dynamics**: $du = -\nabla \mathcal{E}\,dt + \sqrt{2T}\,dW$
- **Basin softmax at T > 0**: $P(\widehat K = k) \propto e^{-E_k^*/T}$
- **Kramers escape**: 각 basin 간 escape rate $\tau^{-1} \sim \exp(-\Delta\mathcal{F}/T)$
- **Selector transition width**: noise가 Layer 1 step을 sigmoid로 smoothing

**Outputs**:
- `working/T/thermal_softmax.md` (신규) — thermal smoothing of Layer 1 selector
- R20 β=9 bistable region의 thermal interpretation

### G6 — Application Layer Scoping

**목표**: Cognitive science / real-world data에 SCC theory 적용 가능성 탐색.

**탐구할 영역**:
- **Cognitive perception**: object formation, attention gates, pre-objective field
- **Image segmentation**: SCC gradient flow as clustering algorithm
- **Community detection**: graph-based SCC for network community discovery
- **Pattern formation**: chemistry / biology analogies

**Outputs**:
- `working/A/application_scoping.md` (신규 디렉토리 + 파일) — application 방향 초안
- 가능한 실험 설계 3-4개 (real data 대상)

---

## §3. 우선순위

**P0 (반드시)**:
- G1 (Layer classification) — **foundation 명확화**
- G2 (Function taxonomy) — **사용자 요청 최우선**
- G3 (Single → Multi) — **사용자 요청 최우선**

**P1 (주요)**:
- G4 (Time evolution) — Multi-formation의 자연스러운 다음 단계
- G5 (Stochastic) — Layer 1 thermal smoothing

**P2 (스코프 보조)**:
- G6 (Application) — 이론 완성도 확인 목적

---

## §4. Non-goals

- Canonical §13 전면 rewrite — **Stage 3 작업**, 오늘은 scope 외
- Multi-formation numerical experiments — **Stage 5 작업**
- 실제 real data 분석 (application 실행) — **Stage 6 작업**
- CODE 실험 재실행 — 오늘 확보한 11 JSON 결과로 충분

---

## §5. 작업 흐름

1. **Morning** (G1 + G2):
   - 77 Cat A layer classification table 작성
   - Function taxonomy mapping
   - 약 3-4시간

2. **Afternoon** (G3):
   - Multi-formation extension brainstorm
   - $\mathcal{M}_K$ moduli space + K-sector theory
   - 약 3-4시간

3. **Evening** (G4 + G5 scoping):
   - Time evolution + Stochastic 방향 scoping
   - Working files 생성
   - 약 2-3시간

4. **Late** (G6 선택적):
   - Application 방향 brainstorm
   - 총 세션 길이 ~12시간 예상

---

## §6. R22 carry-forward items

이월된 pending items:
- **Q61-Q70**: canonical merge user 결정들 (Stage 2 처리)
- **NQ-46**: Formation selection rules
- **NQ-47**: K transition rates (Kramers-like)
- **NQ-48**: $\mathrm{Aut}(G)$ equivariant Morse
- **NQ-49**: Complete layer classification (G1 해결 대상)
- **NQ-50**: Protocol specification language

---

## §7. 성공 기준

세션 종료 시:
- [ ] 77 Cat A 전원 Layer 1/2/3 분류 완료
- [ ] Function taxonomy (6+ function classes) 완료
- [ ] Multi-formation extension framework 초안 (≥3 Cat B/C 가설)
- [ ] Time evolution scoping (≥2 가설)
- [ ] Stochastic extension scoping (≥2 가설)
- [ ] `working/SF/function_taxonomy.md`, `working/MF/multi_quantization.md`, `working/T/`, `working/A/` 신규 파일들 commit

---

## §8. 종료 기준

다음 조건 중 하나라도 충족되면 세션 종료:
- P0 (G1+G2+G3) 모두 완료 + working files commit
- 12시간 초과 + P0 80% 이상 완료
- 예기치 못한 foundation 문제 발견 → 조기 종료하고 다음 날 재설계

---

**End of plan.md for 2026-04-23.**
**Target: single-formation 안정화 + Multi-formation bridge 확립 + Time/Stochastic/Application scoping.**
