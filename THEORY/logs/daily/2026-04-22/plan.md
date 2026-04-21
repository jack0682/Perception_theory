# Plan — 2026-04-22 (C-S2: Stage 1 Second Session — NEB Completion + Working File Updates + Errata Application)

## Target

**Stage 1 둘째 세션 — C-S2 진입.** 어제 (2026-04-21) Stage 5 NEB 부분 성공 + 20 errata 누적 + 28 NQ catalogued 의 후속:
1. **NEB endpoint optimizer 강화** (NQ-26): scipy `trust-constr` 또는 IPOPT 로 high-β (β ≥ 20) 수렴 문제 해결.
2. **Saddle Hessian Morse verification** (NQ-27): β=10 saddle (K_soft=0.99, idx=11) 의 Hessian 직접 계산 → Morse index = 1 확인.
3. **Mechanism filtering protocol 구현** (E-18): K=2-like vs K=3-like saddle 분리 후 mechanism-specific γ_eff 측정.
4. **Working file updates** (5+ files): Stage 5 numerical 결과를 `M1_dissolution.md`, `integer_K_dependency_map.md`, `F_group_axioms.md` 등에 반영.
5. **6 보류 errata 적용**: E-4, E-5, E-6 (Round 2 보류) + E-18, E-19, E-20 (Round 11 신규).
6. **canonical_sub.md 2026-04-22 entry**: Stage 5 후속의 Added/Modified/Pending 정리.

하루 산출은 **Stage 5 의 incomplete points 해소 + Stage 1 의 working file 정밀화**. 내일 (2026-04-23) 의 Stage 1 셋째 세션 (CE-S2 phase diagram) 진입 가능.

## Why now

- 2026-04-21 Stage 5 NEB v4 = 5/8 valid runs. **β=10 만 깨끗** (saddle K_soft=0.99, ΔE=2.28). high β 미해결.
- 20 errata 중 8 만 적용. 12 가 working files / 추후 user review 보류 — **누적이 너무 큼, 정리 필요**.
- canonical_sub.md 2026-04-21 entry 가 매우 길어짐 (725 줄, Round 1-11 누적). 내일 Round 추가 전 cleanup.
- Stage 5 의 가장 substantive 미해결: **β=10 saddle 이 진짜 Morse-1 saddle 인가?** (지금까지 saddle K_soft + interior idx 만 확인, Hessian 미확인).
- C-S2 의 자연 scope = "어제 시도한 numerical 정밀화" — 새 theoretical 영역 진입 (예: Witten Laplacian 구체) 보다 우선순위 높음.

## Context refs (반드시 읽어야 할 자료)

- `THEORY/logs/daily/2026-04-21/13_neb_stage5_final.md` (293줄) — 어제 Stage 5 NEB 의 모든 결과 (Findings 1-5, errata E-18~20).
- `THEORY/logs/daily/2026-04-21/12_code_verification.md` — Round 9 numerical 결과 (T*_uniform 0.1% accuracy 등).
- `THEORY/logs/daily/2026-04-21/10_critical_self_review.md` — E-10~E-13 critique-mode errata.
- `THEORY/logs/daily/2026-04-21/99_summary.md` — 11 라운드 누적 summary.
- `THEORY/canonical/canonical_sub.md` — 2026-04-21 entry (725줄).
- `CODE/scc/k_soft.py` — 어제 만든 영구 모듈.
- `CODE/scripts/neb_beta_sweep_v4.py` — 5/8 success 의 마지막 NEB 스크립트.
- `CODE/scripts/diagnose_neb_collapse.py` — Hessian 진단 스크립트 (이걸 saddle 검증에 재활용).
- `CODE/logs/neb_v4_results.json` — JSON 저장된 NEB chain 데이터.
- `THEORY/working/E/M1_dissolution.md` (200줄) — Stage 5 결과 반영 대상.
- `THEORY/working/integer_K_dependency_map.md` (107줄) — T-Beyond-Weyl/T-d_min 추가 대상.
- `THEORY/canonical/canonical.md` §13 (특히 line 1043-1059 Cat B section).
- 외부 정리:
  - Bovier-Eckhoff-Gayrard-Klein (2002, 2004) — Kramers prefactor on constrained manifold.
  - Henkelman, Uberuaga, Jónsson (2000) — Climbing Image NEB original paper.
  - E, Ren, Vanden-Eijnden (2002) — String method (NEB alternative).
  - Conn, Gould, Toint — Trust-region methods (for trust-constr understanding).

## Current hypotheses / approaches

사용자의 잠정 직감 (에이전트는 이 안에만 머물지 않음 — 출발점):

1. **Trust-constr 가 BFGS 보다 robust** for endpoint convergence at high β. inequality constraints (`u_i ∈ [eps, 1-eps]`) + equality constraint (`Σ u_i = m`) 동시 처리.
2. **β=10 saddle 의 Hessian 이 정확히 1 negative eigenvalue 를 가질 것** (Morse index 1). Saddle K_soft = 0.99 이므로 unstable mode 방향이 K=2 manifold 내부 specific 한 perturbation.
3. **K=3-like saddle (β=8, 12) 가 별개 MEP** — 같은 K=1, K=2 endpoints 사이에 두 saddle 존재. (NQ-28 multi-MEP enumeration).
4. **canonical exp38 의 γ_eff = 0.89 는 specific protocol 의 fit** — 우리 setup 으로 재현 불가는 Round 6 §1 의 분석과 일치.
5. **Mechanism filtering 후 γ_eff 측정 가능** — K=2-mechanism saddles 만 모아서 (β=10, 20, 25) 정밀 fit. 단 endpoint convergence 가 fix 되어야.

핵심 미해소 질문 (에이전트 답변 필수):

- **Q1.** Trust-constr 가 NEB endpoint 에 적용 가능한가? (`scipy.optimize.minimize(method='trust-constr')` 의 `constraints` 인자 형식).
- **Q2.** β=10 saddle 의 Hessian 이 정확히 1 negative eigenvalue 를 갖는가? 만약 그렇다면 진짜 Morse-1 saddle 확인. 아니면 (degenerate, 또는 multiple negatives) Mountain Pass 의 saddle 정의 부족.
- **Q3.** K=3-like saddle (β=8) 의 K_soft = 1.48 이 실제로 K_hard ≈ 3 인지, 아니면 transient 인지 (saddle 의 actual configuration 시각화).
- **Q4.** Mechanism filtering 후 K=2 saddles (β=10, 20, 25 with proper convergence) 의 γ_eff 가 [0.5, 1.0] envelope 안에 들어가는가? 만약 negative 면 protocol-dependence 가 더 깊은 issue.

## Session goals (G1-G7 deliverables)

### G1. NEB v5 with trust-constr endpoints — `CODE/scripts/neb_beta_sweep_v5.py`

- L-BFGS-B 대신 scipy `trust-constr` 사용 — inequality bounds + equality constraint (`Σ u = m`) 동시 처리.
- Endpoint convergence target: |grad| < 0.01 at all β.
- β range: [10, 15, 20, 25, 30, 40, 50] (high-β 까지).
- 각 β 의 K=1, K=2 endpoint 의 g_norm 보고 (E-19 해소 확인).
- 만약 trust-constr 도 high-β 에서 실패하면 IPOPT 시도 (cyipopt 설치 필요).
- 출력: `CODE/logs/neb_v5_results.json`.

### G2. Saddle Hessian Morse verification — `CODE/scripts/saddle_hessian.py`

- β=10 NEB v5 결과의 saddle 구성 추출 (idx=11 또는 NEB v5 가 찾은 idx).
- Hessian via finite differences (n²=256² = 65536 entries; ~5분).
- Project onto T_u Σ_m (`P = I - 11ᵀ/n`).
- Eigenvalue 분석: 정확히 1개 negative 인지 확인 (Morse index = 1 = 1st-order saddle).
- 만약 그렇지 않으면: degenerate critical point (Morse-Bott) 또는 higher-order saddle. NQ-28 multi-MEP 의 indication.
- 출력: `CODE/logs/saddle_hessian_b10.json`.

### G3. Mechanism filtering γ_eff measurement — `CODE/scripts/gamma_eff_filtered.py`

- G1 의 NEB v5 결과 (`neb_v5_results.json`) load.
- Saddle K_soft 로 grouping: `K=2-mechanism (K_soft ∈ [0.85, 1.15])`, `K=3-mechanism (K_soft ∈ [1.35, 1.65])`.
- 각 그룹 별 power-law fit `ΔE = c · β^γ`.
- 두 mechanism 의 γ_eff 와 R² 보고.
- 만약 K=2-mechanism γ_eff ∈ [0.5, 1.0] 면 Round 6 envelope 확인. 만약 negative 면 deeper issue.

### G4. `working/E/M1_dissolution.md` — Stage 5 결과 반영

- §3 Kramers (수치) 부분 update:
  - Round 4 §1.4 numerical T*_uniform = 7.218 (predicted 7.224) 명시.
  - β=10 saddle: K_soft = 0.99, ΔE_barrier = 2.28 (NEB v4 측정).
  - β-dependent mechanism switching (E-18) 보고: K=2 vs K=3 saddle.
- §4 (empirical 재해석) 부분 update:
  - canonical exp38 γ_eff = 0.89 의 reproducibility 시도 결과 — Stage 5 negative result.
  - Round 6 §1 의 honest closure (γ_eff protocol-dependent) numerical 으로 재확인.
- §5 Residuals 추가: R-M1-F (mechanism switching), R-M1-G (high-β endpoint convergence).

### G5. `working/integer_K_dependency_map.md` — Stage 5 후 update

- §2.2 Cat B Retire 목록: **T-Beyond-Weyl + T-d_min-Formula 추가** (Round 2 §05 §5.3 의 발견, 적용 안 됨). 새 행 2개.
- §3 Cat A 22 항목 update (Round 2 §05 §4 enumeration; 19~20 → 22).
- §6 (canonical inconsistencies) 새 항목 추가:
  - 6.3 — γ_eff numerical reproduction 실패 (Stage 5).
  - 6.4 — K=2 endpoint convergence quality 가 β 에 따라 변화 (Stage 5).
- §7 Next Actions 업데이트.

### G6. `working/C/F_group_axioms.md` + `working/CE/free_energy_wellposed.md` 보강

- F3 status: Round 11 의 Theorem F3.1 (Lions-Sznitman + Filippov repair) 가 명시되어 있음을 한 번 더 cross-check.
- ℱ_C+E 의 numerical 검증 사실 추가 (T*_uniform 0.1% accuracy).
- λ_K = γ_K T 의 (φ-sat) commit 강조 확인 (E-11 Applied).

### G7. Errata batch application + canonical_sub.md 2026-04-22 entry

- **6 보류 errata 적용:**
  - **E-4** (entropy η-parameterization): `working/E/F1_dissolution.md` §3.3 cosmetic update.
  - **E-5** (T-Beyond-Weyl + T-d_min retire): G5 의 dependency_map 보수에서 처리.
  - **E-6** (Cat A 22 update): G5 의 §3 update 에서 처리.
  - **E-18** (mechanism switching): G4 의 M1_dissolution §3 / §5 에서 처리.
  - **E-19** (BFGS inadequate): documented in `13_neb_stage5_final.md` §4 → working/CE/free_energy_wellposed.md §4.4 에 cross-reference 만 추가.
  - **E-20** (NEB MEP β-sensitive): documented in `13_neb_stage5_final.md` → cross-reference.

- **canonical_sub.md 2026-04-22 entry**: 본 세션의 working file updates + numerical NEB v5 결과 + saddle Hessian verification (G2) 의 Added / Modified / Pending 항목.

## Non-goals (오늘 안 할 것)

- **NEB on full Σ_m corner (incl. u_i ∈ {0, 1})** — Round 11 §8 의 corner extension 은 C-S3 carry.
- **Witten Laplacian semiclassical full asymptotic** (NQ-12) — post-Stage-1.
- **(T, λ_K) bicritical phase diagram** (NQ-21) — CE-S2.
- **Disconnected-graph M-1 reframing** (NQ-13) — E-S3.
- **Stage 6 canonical merge 자체** — 본 세션은 working level 보강만; canonical 직접 수정 금지.
- **F4 T → 0 recovery 의 35 Cat A 전수 검증** — C-S3.
- **새 NQ 발굴** — 28 NQ 가 이미 catalogued; 추가 발생 시만 기록.
- **scc/ 의 새 모듈 생성** — k_soft.py 외 추가 모듈 금지 (script 만 사용).

## Carry-forward (2026-04-21 로부터)

- **Stage 5 부분 성공:** NEB v4 의 5/8 valid runs. β=10 SUCCESS. high β 미해결.
- **3 numerically verified Cat A:** Cor 4.1 (K_soft Lipschitz), T-Merge (a) (K=2 Hessian PD), T*_uniform (0.1% accuracy).
- **20 errata, 28 NQs catalogued.**
- **9 theory rounds + 1 numerical session (Round 11) = 10 verification rounds.**
- **Working files 6개 + scc/k_soft.py + 5 NEB scripts + diagnose script.**
- **9648 줄 산출 (어제 단일 일).**
- **canonical_sub.md 725 줄 누적.**

## Success criterion for today

**저녁 시점에 G1-G7 7개 deliverable 이 모두 산출되어 있어야 한다.** 특히:

- **G1:** NEB v5 가 적어도 7/7 β values 에서 valid 결과 (saddle interior + endpoint |grad| < 0.01).
- **G2:** β=10 saddle Hessian 의 negative eigenvalue 정확한 개수 보고 (1 → Morse-1 confirmed; >1 → Mountain Pass 의 saddle 정의 부족).
- **G3:** Mechanism-filtered γ_eff 계산. K=2 group 의 fit + R². (Negative slope 면 deeper issue 인정.)
- **G4-G6:** 5 working files 에 Stage 5 결과 반영.
- **G7:** 6 보류 errata 적용 + canonical_sub.md 2026-04-22 entry.

**최소 priority (시간 부족 시):** G1 (NEB v5) 가 가장 우선순위 (Stage 5 의 핵심 incompleteness 해소). G7 의 errata batch 가 두 번째. G2-G6 는 G1 결과에 따라 우선순위 조정.

단계별 체크:
- [ ] G1 `neb_beta_sweep_v5.py` — trust-constr endpoint, 7+ valid runs.
- [ ] G2 `saddle_hessian.py` — β=10 saddle Morse verification.
- [ ] G3 `gamma_eff_filtered.py` — mechanism-filtered fit.
- [ ] G4 `working/E/M1_dissolution.md` — §3, §4, §5 update.
- [ ] G5 `working/integer_K_dependency_map.md` — §2.2 + §3 + §6 update.
- [ ] G6 `working/C/F_group_axioms.md` + `working/CE/free_energy_wellposed.md` — cross-check + numerical 검증 명시.
- [ ] G7 6 errata 적용 + canonical_sub.md 2026-04-22 entry.

하나라도 미달이면 성공 기준 미충족. 우선순위 규칙 상 G1 + G7 가 minimum.

---

## 메모

- 본 plan 은 **2026-04-21 저녁** Stage 5 종료 직후 사용자 + 에이전트 협의로 작성. 어제 9648 줄 산출 한 다음날 진입이라 fatigue 고려해 G1-G7 의 일부는 short-form 가능.
- C-S2 의 자연 scope 는 "어제 시도한 numerical 정밀화 + 누적 errata cleanup". 새 theoretical 영역 (예: bicritical mapping, Witten Laplacian) 은 모두 다음 세션 (2026-04-23+) 으로 carry.
- 만약 G1 에서 trust-constr 도 high-β 실패: IPOPT 시도 (`pip install cyipopt`). 또는 더 극단적: **Newton's method on KKT system** (saddle 직접 search).
- 본 plan 의 G3 gamma_eff_filtered 가 어떤 결과 주든 (positive / negative / undefined) Round 6 §1 의 honest closure 와 일치하는 해석 필요. 즉 "γ_eff = 0.89 reproducible" 시 → Round 6 §1 일부 retract; "negative or noisy" 시 → Round 6 §1 강하게 confirm.
- 저녁 후속 (사용자 할 일):
  1. 7 deliverable 산출물 검토.
  2. canonical_sub.md 2026-04-22 entry 검토 + 필요 시 수정.
  3. 2026-04-23 plan.md 작성 — Stage 1 셋째 세션 후보 (CE-S2 phase diagram 또는 E-S2 §12 재작성).
- 본 plan 의 scope 는 **Stage 1 둘째 세션 = C-S2**. 7 deliverable 이 어제의 6 deliverable 보다 약간 적은 분량 (~10시간 일감). 어제 12-16h 일감 지속 후 오늘 10h 적정.
- **scope creep 주의점:** G1 trust-constr 에서 IPOPT 까지 가면 +2h 추가. G2 의 Hessian 계산이 256² = 65536 FD entry → ~5-10분. Total 시간 배분 신중.
