# Plan — 2026-04-25

**Session type:** Numerical + Theory hybrid — Goldstone commensurability splitting 정량화
**Prerequisite:** 2026-04-24 세션 완료 상태 — Theorem 1 V5b (dual-regime + commensurability splitting 발견), C2 ~100%·C3 sub-lattice ~100% 정복, Axiom S1' v1 canonical-ready, ~40 new NQ (NQ-125..171).
**Session working directory:** `THEORY/logs/daily/2026-04-25/`

---

## Target

**NQ-168: 2D Goldstone commensurability splitting의 정량적 characterization.**

Super-lattice regime (ζ = ξ_0/a > 0.5)에서 translation Goldstone이 단일 near-zero eigenvalue가 아니라 **(near-zero λ_x, orbital-scale λ_y) doublet**으로 split함이 어제 deep dive에서 발견되었다 (`27_deep_dive_results.md` §7-8). 이 splitting의:
- disk center position $(x_0, y_0)$에 대한 dependence
- Functional form (Peierls-Nabarro analogy? Fourier decomposition? 다른 기원?)
- x-Goldstone vs y-Goldstone 비대칭의 geometric origin

을 이론적으로 유도하고 수치로 검증하는 것이 오늘의 단일 target.

---

## Why now

어제 세션의 가장 큰 **신규 발견**이 바로 이 splitting이다. V5b가 V5a ("no Goldstone") 를 retract하고 Goldstone existence를 확증했지만, 왜 하나의 2D Goldstone doublet이 **서로 다른 eigenvalue 둘로** split되는가는 미설명이다. 이것이 설명되지 않으면 Theorem 1 V5b 자체가 미완성된 empirical claim에 머문다. 더불어, splitting의 functional form이 확정되면:
- Theorem 1이 Cat B → Cat A 전환 가능
- σ-framework에서 Goldstone mode의 canonical treatment가 가능 (σ에 Goldstone를 어떻게 포함할지)
- NQ-169 (β-scaling ν=5.8의 이론적 기원)에 부분 answer 제공

어제 §9.4의 primary recommendation 그대로 이행.

---

## Context refs (에이전트가 반드시 읽어야 할 소재)

- `THEORY/logs/daily/2026-04-24/27_deep_dive_results.md` §7-9 — 어제 발견의 원본. Eigenvector projection test, decoupled L=40 test, doublet splitting 관측. **필수 선독**.
- `THEORY/logs/daily/2026-04-24/26b_FK_analogy.md` §1-7 — Frenkel-Kontorova (FK) analogy framework. Peierls-Nabarro (PN) barrier 예측의 이론적 골격.
- `THEORY/logs/daily/2026-04-24/02_development.md` §5 — Theorem 1 current statement (V5b 이전 버전, 어제 revision 전).
- `THEORY/logs/daily/2026-04-24/99_summary.md` §9.2-9.5 — session close state, carry-forward.
- `THEORY/canonical/canonical.md` §2 (formal universe), §11 (commitments), §12 (multi-formation) — canonical context.
- CODE/scripts/ — 어제 작성된 deep_dive analysis scripts. 결과 재현 기준.

---

## Current hypotheses / approaches under consideration

- **가설 H1 (Peierls-Nabarro)**: Square lattice는 disk center에 2D periodic potential $V_{\mathrm{PN}}(x_0, y_0) = V_0[\cos(2\pi x_0/a) + \cos(2\pi y_0/a)]$ 를 부과. x-방향 curvature $\partial^2 V_{\mathrm{PN}}/\partial x_0^2 = -(2\pi/a)^2 V_0 \cos(2\pi x_0/a)$. → splitting $\Delta\lambda \propto |\partial^2 V_{\mathrm{PN}}/\partial x_0^2 - \partial^2 V_{\mathrm{PN}}/\partial y_0^2|$ 로 예측. 가장 단순한 closed form 후보.

- **가설 H2 (Fourier decomposition)**: 실제 discrete lattice 효과는 $V_{\mathrm{latt}}(x_0, y_0) = \sum_{m,n} V_{mn} \cos(2\pi m x_0/a)\cos(2\pi n y_0/a)$. 이 중 splitting에 기여하는 leading term은 $(m,n) = (1,0)$ 과 $(0,1)$이 서로 다른 계수를 가질 때 — off-symmetry position에서 발생.

- **가설 H3 (σ-framework 통합)**: Goldstone mode가 super-lattice에서 σ에 포함되어야 한다면, splitting은 σ의 두 번째 구성요소 $[\rho_0]$ (irrep)의 *lifting*으로 해석 가능. 2D $E$-irrep doublet이 lattice 대칭 저하로 $A_1 \oplus B_1$ (또는 유사 분해)로 split될 때 eigenvalue gap 발생.

- **반례 의심**: V5b의 "99% Goldstone overlap" test가 L=40 decoupled β/β_c=10에서 수행됨. 이 specific config에서 overlap이 높다는 것이 **general** super-lattice regime에서도 성립하는가? 혹시 β/β_c 값, ζ 값에 따라 overlap이 달라질 수 있는가?

- **주의**: 어제 25_*의 falsification claim이 부분적으로 틀렸음이 27_*에서 확인됨. 즉 이 문제에서 섣부른 falsification/confirmation 모두 경계.

---

## Session goals

1. **수치 실험 (G1, P0)**: L=40 torus, ζ≈0.7-1.0 (super-lattice), 여러 disk center positions $(x_0, y_0)$ scan에서 lowest 4 Hessian eigenvalues + eigenvectors 측정. x-Goldstone vs y-Goldstone eigenvalue pair의 $(x_0, y_0)$-map 작성.

2. **이론 유도 (G2, P0)**: H1 (PN) 또는 H3 (σ irrep splitting) 중 하나를 primary로 하여 splitting의 analytical approximation 도출. 수치 결과와 비교 (정성적 agreement면 Cat B, 정량적이면 Cat A 후보).

3. **NQ-169 예비 탐색 (G3, P1)**: Goldstone eigenvalue λ_Gold(β)의 두 contribution (PN barrier 기원 + near-critical 기원) 분리 시도. 어제 ν=5.8 empirical에 대한 theoretical explanation의 첫 줄 작성.

---

## Non-goals (scope 제한)

- **C1' cluster (σ-framework depth)** — NQ-147~157 중 σ-framework extension: 다음 세션으로. 오늘은 Goldstone-σ interface에만 접촉.
- **Weekly merge / canonical 직접 수정** — weekly_draft_storming.md에 entry 추가는 세션 끝에 가능하나, canonical.md 직접 편집 없음.
- **C2 cluster 추가 공격** — C2 ~100% 달성됨. 오늘은 scope 아님.
- **Multi-formation orbital 확장 (Phase 5-7)** — 오늘은 single-formation Goldstone characterization에 집중.
- **새로운 graph class 실험 (SBM, barbell 등)** — ζ-regime이 먼저 완전히 이해된 이후.

---

## Carry-forward (어제로부터)

- **Theorem 1 V5b**: sub-lattice (ζ<0.3) Cat A (no Goldstone), super-lattice (ζ>0.5) Cat A (Goldstone confirmed) + **commensurability splitting 관측 but unexplained**. 이 "unexplained" 부분이 오늘의 target.
- **ζ_* ≈ 0.3-0.4 crossover**: smooth, regime boundary (Cat B 잠정). 오늘 splitting mechanism이 밝혀지면 이 boundary의 이론적 기원도 연결 가능.
- **Scripts**: `CODE/scripts/`에 deep_dive 시리즈 (phase1/2/3). 오늘 G1에서 재사용 또는 확장.
- **NQ-125..171** (~40 new NQs) 누적 중. 오늘 G1 결과가 NQ-168 closes (if successful) 또는 NQ-168 splits further.
- **Axiom S1' v1**: Goldstone를 σ-framework에 포함하는 방식이 오늘 G2 이론 결과에 dependent. G2 후 Axiom S1' revision 필요 여부 판단.

---

## Success criterion for today

> **NQ-168이 disk center position의 explicit function (또는 그 근사)으로 표현되고, 이 function이 이론적 메커니즘 (PN-type 또는 irrep splitting) 과 수치적으로 비교 가능한 형태로 도달한다. 실패할 경우, 어떤 specific 조건에서 mechanism 도출이 막히는지 명시되어 다음 세션의 설계를 구체화한다.**

---

## 메모

- 오늘은 어제와 달리 **이론-driven 세션** — 실험이 목적이 아니라 기존 발견의 설명이 목적. "더 실험하는 것" 보다 "이미 본 것을 이해하는 것"이 우선.
- G1 수치 실험은 G2 이론 검증을 위한 것. G1 없이 G2만 쓰는 것도 허용 (이론 예측 → 다음 세션 수치 검증).
- 어제 세션의 핵심 교훈: eigenvector projection이 scalar eigenvalue보다 훨씬 diagnostic. 오늘도 eigenvector overlap analysis 우선.

---

**End of plan.md for 2026-04-25.**
**Target: V5b "splitting observed but unexplained" → "splitting mechanism identified, functional form established".**
