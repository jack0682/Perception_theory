# Pre-Brainstorm — 2026-04-22 C-S2 Stage 1 Second Session Hypothesis Map

**Written:** 2026-04-21 저녁 (post-Stage-5).
**Author:** 사용자 + 에이전트 공동.
**Purpose:** 내일 (C-S2) 의 G1-G7 deliverables 진입 전, **어제 Stage 5 의 limitations 해소 + 누적 errata cleanup** 에 leverage 가능한 도구·수치적 strategy·이론 연결을 정리. 어제의 104 가설 풀과 다르게 **focused / narrow** (~30 가설) — 이미 8 round + Stage 5 가 구조화 완료, 이제 specific implementation choices.
**Constraint:** 본 파일은 사전 가설 목록 이지 commit 아님.

---

## 사용 가이드

1. 각 가설 H-X 는 2-4 줄. (도구/strategy) + (성공 기준) + (실패 시 fallback).
2. §A-D 는 G1-G3 (numerical) 직접 활용.
3. §E-F 는 G4-G6 (working file updates) 활용.
4. §G 는 risk / counter-hypothesis.
5. §H 는 long-term carry (post-C-S2).

---

## A. NEB Endpoint Optimizer 강화 (G1)

### A-Numerical: Trust-region / IPOPT

- **H-A1.** `scipy.optimize.minimize(method='trust-constr')` with `LinearConstraint(A=ones, lb=m, ub=m)` for volume + `Bounds(eps, 1-eps)` for box. `gtol=1e-6`, `xtol=1e-9`. 성공 기준: 모든 β 에서 |grad_proj| < 0.01. Fallback: IPOPT.
- **H-A2.** IPOPT (cyipopt): full interior-point method, handles nonlinear constraints + bounds 모두. Install: `pip install cyipopt`. 성공 기준: trust-constr 보다 5x faster + tighter convergence.
- **H-A3.** Custom Newton on KKT: `∇ℰ - μ·1 = 0` solve directly. Newton step: `H · Δu = -∇ℰ + μ·1` with `Σ Δu = 0`. 가장 빠르나 H 직접 필요 (FD 256² = 5min/iter).
- **H-A4.** **Hybrid:** L-BFGS-B coarse → trust-constr fine. L-BFGS 가 첫 90% 수렴 (저렴), trust-constr 이 마지막 10% (정확). 성공 가능성 가장 높음.
- **H-A5.** Restart strategy: 만약 한 optimizer 실패하면 다른 init point 에서 재시도 (multi-start).

### A-Mathematical: Convergence theory

- **H-A6.** Trust-region 의 super-linear convergence on smooth problem 보장 — Conn-Gould-Toint 1992. SCC's ℰ 는 polynomial in u, smooth on Σ_m^ε. 적용 가능.
- **H-A7.** IPOPT 의 polynomial complexity bound (Wachter-Biegler 2006) — large-scale 에서 BFGS 보다 strictly better.
- **H-A8.** Saddle point search 의 Newton method 는 linear convergence 만 보장 (Hessian eigenvalue 가 작아짐). NEB 후 saddle finetune 이 적합한 use case.

---

## B. Saddle Hessian Morse Verification (G2)

### B-Numerical

- **H-B1.** β=10 saddle = NEB v4 결과의 image idx=11 (16×16 grid, 256 sites). FD Hessian 65536 entries. 5-step parallel evaluation 으로 ~1-2분.
- **H-B2.** Project Hessian onto T_u Σ_m: `P = I - 11ᵀ/n`, `H_constr = P H P`. Constrained Hessian 의 eigenvalue 분석.
- **H-B3.** Morse-1 saddle 기대: 1 negative + (n-2) positive + 1 zero (constraint direction). 만약 그렇지 않으면 degenerate.
- **H-B4.** Negative eigenvector 시각화 (16×16 grid 위 heatmap). Unstable mode 가 K=1 ↔ K=2 direction 인지 확인.

### B-Mathematical

- **H-B5.** Mountain Pass theorem (Round 5 §3) 가 Morse-1 saddle 의 존재 보장. NEB 가 found saddle 이 Morse-1 인지 확인은 theorem 의 numerical validation.
- **H-B6.** 만약 Morse index ≥ 2 (multiple negative eigenvalues): NEB 가 finds saddle of higher index → not the optimal MEP.  alternative MEP 존재 가능.
- **H-B7.** 만약 zero eigenvalues (degenerate): Morse-Bott critical submanifold. Round 4 §4.2 에서 언급.
- **H-B8.** Bovier-Eckhoff-Gayrard-Klein (2004) 의 Kramers prefactor formula 가 Morse-1 saddle 가정. Stage 5 의 Kramers extension 의 prerequisite.

---

## C. Mechanism Filtering γ_eff (G3)

### C-Numerical

- **H-C1.** Saddle K_soft 로 grouping: `K=2-mech (K_soft ∈ [0.85, 1.15])`, `K=3-mech (K_soft ∈ [1.35, 1.65])`. 각 group 별 power-law fit `log ΔE = γ · log β + const`.
- **H-C2.** Bootstrap confidence interval on γ: 작은 샘플 (3-5 points) 의 γ 추정 uncertainty quantify.
- **H-C3.** 만약 K=2-mech 만 4+ 점이면: γ_K2 정밀 측정 가능. K=3-mech 는 별도 γ_K3.
- **H-C4.** Compare γ_K2 vs γ_K3: same regime (both ∈ [0.5, 1.0]) 또는 different regime (K=3 path 가 더 가파른가)?

### C-Theoretical

- **H-C5.** Round 6 §1 의 sharp-interface limit (γ=0.5) vs bulk (γ=1.0) 가 mechanism-specific 인가? K=2 path 가 sharper interface (less bulk) → γ_K2 ~ 0.5 가까이 예상.
- **H-C6.** K=3 path 는 transient extra mode → more interface area → γ_K3 ~ 0.5 도 가능, 또는 mixed bulk → γ_K3 ~ 1.0 가능. Numerical 결과로 구분.
- **H-C7.** 만약 두 γ 가 모두 negative: protocol-dependence 가 mechanism level 에서도 강함. canonical exp38 의 0.89 가 third (uncatalogued) mechanism 일 가능성.

---

## D. Canonical exp38 Reproducibility (G3 보조)

### D-Theoretical

- **H-D1.** canonical exp38 의 protocol details 미상. β range [20, 100], R²=0.997 보고. 우리 setup 과 다른 점: graph size, m, c, NEB 설정 추정.
- **H-D2.** 만약 canonical exp38 이 larger grid (e.g., 50×50) 또는 다른 c (e.g., 0.5) 였으면, sharp-interface regime 에 더 가까이 → γ_eff ~ 0.5 가까이 예상.
- **H-D3.** **0.89 의 origin 추정:** 0.5 (Modica-Mortola) + 0.5·log β 의 prefactor contribution = 0.5 + 0.39 ≈ 0.89. 즉 **γ_eff = 0.89 = 0.5 + Hessian-prefactor 0.39**?
  - log scaling: τ = τ_0(β) · exp(c·β^γ/T). log τ = log τ_0 + c·β^γ/T. fit log τ vs log β: log τ_0 ~ 0.5 log β (Hessian)+ const · β^γ ~ β^γ.
  - At fixed T: log τ ≈ γ·log β + 0.5·log β = (γ+0.5)·log β. So measured "γ_eff" = γ_true + 0.5.
  - If canonical 0.89 = γ_true + 0.5 → γ_true = 0.39 ⇒ subdominant power-law.
- **H-D4.** 우리 measurement 는 ΔE_barrier (height), not τ. ΔE_barrier 직접: γ_eff = γ_true. 만약 γ_true = 0.39, log-log fit 직접 → 0.39 (not 0.89). Discrepancy.

---

## E. Working File Updates (G4-G6)

### E-Documentation strategy

- **H-E1.** M1_dissolution.md §3 Kramers update: 어제 §06 §1 의 explicit Hessian + Round 4 Theorem 1.1 numerical 검증 (T*_uniform 0.1%) cross-reference.
- **H-E2.** M1_dissolution.md §4 (empirical 재해석): exp38 γ_eff = 0.89 reproducibility "Stage 5 attempted, see logs/daily/2026-04-21/13_neb_stage5_final.md §3.5".
- **H-E3.** M1_dissolution.md §5 R-M1-F (mechanism switching, Stage 5 §3.1), R-M1-G (high-β endpoint convergence, Stage 5 §3.2) 추가.
- **H-E4.** integer_K_dependency_map.md §2.2 추가 retire: T-Beyond-Weyl, T-d_min-Formula 행 추가 (Round 2 §05 §5.3 finding).
- **H-E5.** integer_K_dependency_map.md §3 update: 22 Cat A survive (not 19~20).
- **H-E6.** F_group_axioms.md / free_energy_wellposed.md: 새 section 없이 cross-reference 만 (Round 11 의 verified Cat A 항목들).

### E-Promotion pipeline integrity

- **H-E7.** working/ 의 update 가 canonical 직접 수정 안 함. canonical_sub.md 에만 promoted candidate 적기.
- **H-E8.** canonical_sub.md 2026-04-21 entry 가 725 줄로 매우 큼. **2026-04-22 entry 가 추가되면 800-900 줄.** Weekly merge 강력 권장 (다음 weekly 가 언제인지 확인).

---

## F. Errata Batch Application (G7)

### F-Strategy

- **H-F1.** E-4 (entropy η-parameterization): F1_dissolution.md §3.3 의 η = 0.85, 0.90 → 직접 nat values (S_1 ≈ 5.5, S_2 ≈ 8) 로 교체. Cosmetic. 5분.
- **H-F2.** E-5 (T-Beyond-Weyl, T-d_min retire): integer_K_dependency_map §2.2 에 2개 행 추가. G5 와 합치기. 10분.
- **H-F3.** E-6 (Cat A 22 update): integer_K_dependency_map §3 의 "19~20 → 22" + Prop 1.1, Persistence Threshold Eq, T-Birth-Parametric (D₄) 추가. 15분.
- **H-F4.** E-18 (mechanism switching): M1_dissolution §5 R-M1-F 추가 (G4 와 합치기).
- **H-F5.** E-19 (BFGS inadequate): free_energy_wellposed.md 에 cross-ref 만. 5분.
- **H-F6.** E-20 (NEB MEP β-sensitive): documented in 13_neb_stage5_final §3.4 — cross-ref. 5분.

### F-Risk

- **H-F7.** errata 너무 많이 한 번에 적용 시 file inconsistency. **하나씩 verify** 필수.
- **H-F8.** 일부 errata 가 사용자 review 가 implicit 한 user decision 필요 (e.g., E-5 의 retire 시점). User decision 보류.

---

## G. Risk / Counter-Hypothesis

- **H-G1.** trust-constr / IPOPT 도 high-β 에서 실패 — energy landscape 가 너무 nonconvex / ill-conditioned. Fallback: 더 작은 grid (12×12) 또는 더 작은 β range.
- **H-G2.** β=10 saddle Hessian 이 Morse-1 가 **아닌** 경우 (e.g., 2 negatives or 0 negatives + zeros). 그러면 NEB v4 의 "saddle" 이 진짜 1st-order saddle 이 아님 — Mountain Pass argument 의 numerical evidence 부족.
- **H-G3.** Mechanism filtering 후에도 K=2-mech γ_eff 가 negative — protocol-dependence 가 measurement bias 가 아니라 진짜 physics. canonical exp38 의 0.89 가 우리 framework 와 incompatible 한 protocol.
- **H-G4.** Working file updates 가 incremental 하게 inconsistency 누적 — 매 update 마다 cross-grep 으로 stale references 점검 필요 (Round 7 §6 의 stale reference 사례 재발 위험).
- **H-G5.** 6 errata batch application → 각 errata 의 정확한 위치 + content 확정 시간 +30분. Total session time 부족 위험.
- **H-G6.** scope creep: G1 trust-constr 가 IPOPT 까지 갈 수도 있고, G2 Hessian 이 Morse-Bott (multiple zero) 진단으로 더 깊어질 수 있음. Plan 내 시간 budget 보호.
- **H-G7.** 어제 9648 줄 산출 한 다음 날 — fatigue. **G1 + G7 minimum 준수** 외에는 융통성.

---

## H. Long-term Carry (post-C-S2, 2026-04-23+)

본 세션 scope 외 (다음 세션 후보):

- **H-H1.** **CE-S2 (T, λ_K) bicritical phase diagram** (NQ-21): Round 5 §2 의 4-corner 분석을 numerical mapping. β-T-λ_K 3D scan.
- **H-H2.** **E-S2 §12 multi-formation 재작성** — soft-K language 로 canonical §12 풀 rewrite (Stage 1 셋째 세션 candidate).
- **H-H3.** **C-S3 corner extension to full Σ_m** (Round 11 §8): F3 Lions-Sznitman 의 corner 처리.
- **H-H4.** **F4 T → 0 recovery 의 35 Cat A 전수 검증** — 어제 22개 verified, 13 remaining.
- **H-H5.** **NQ-13 disconnected-graph M-1 reframing** — connected vs disconnected graph 의 isoperimetric ordering 차이.
- **H-H6.** **NQ-12 Witten Laplacian discrete-graph asymptotic** — Helffer-Sjöstrand 의 finite-dim 변형 정확한 statement.
- **H-H7.** **Stage 6 prep** (canonical merge): 20 errata 누적 + 28 NQ + 19 Cat A claims 의 weekly merge planning.

---

## I. 우선순위 요약

| Goal | Priority | Time est. | Hypotheses (직접 활용) |
|---|---|---|---|
| **G1** trust-constr NEB v5 | HIGH | 2-3h | H-A1, H-A4 (hybrid), H-A2 (IPOPT fallback) |
| **G2** Saddle Hessian Morse | HIGH | 1-2h | H-B1, H-B3, H-B4 |
| **G3** Mechanism-filtered γ_eff | MEDIUM-HIGH | 1h | H-C1, H-C5, H-C6, H-D3 |
| **G4** M1_dissolution update | MEDIUM | 1h | H-E1, H-E2, H-E3 |
| **G5** integer_K_dep update | MEDIUM | 1h | H-E4, H-E5, H-F2, H-F3 |
| **G6** F-group / ℱ_C+E update | LOW | 30분 | H-E6 |
| **G7** Errata batch + canonical_sub | HIGH | 2h | H-F1 ~ H-F6, H-E7 |

**Total: ~10시간 일감.** 어제 12-16시간 의 80% 수준 — fatigue 고려 적정.

**Risk reminders:** H-G1, H-G2, H-G5, H-G6 (scope creep), H-G7 (fatigue).

---

## 가설 풀 통계

- A (Optimizer): 8
- B (Hessian Morse): 8
- C (Mechanism filtering): 7
- D (canonical reproduction): 4
- E (Working file): 8
- F (Errata): 8
- G (Risk): 7
- H (Long-term): 7
- **TOTAL: 57 가설** (어제 104 의 절반 — focused).

본 brainstorm 의 H-A1 ~ H-D7 가 코드 작성 시 직접 reference, H-E ~ H-F 가 working file edit 시 reference, H-G 가 시간 / fatigue check.
