# Plan — 2026-04-22 (SF-S1: Single-Formation Foundation Consolidation + Multi-Formation Reframing)

## Target

**어제 (2026-04-21) Rounds 12-18 의 single-formation audit 결과를 기반으로, 오늘 세션은 두 축으로 진행**:

1. **Axis A — Single-Formation Gap Filling + Commit**: 어제 확정된 4개 Cat A candidates (Prop 1.3a, Prop 1.3b, Cor 2.2 qualitative, Cor 2.2 quantitative) 를 `working/SF/` 에 정식 문서화 + canonical_sub.md 에 등록.

2. **Axis B — Multi-Formation New Perspective**: `(N_unst, ξ_0)` 이라는 single-formation invariants 로부터 **multi-formation 구조 `(K̂, formation size, formation spacing)` 을 derived 로 재구성**. F-1/M-1/MO-1 3 Critical 의 dissolution 을 이 새 foundation 위에서 재정식화.

하루 산출물은 **Stage 1 의 진짜 완성** (C+E layer + SF-audit layer 모두 canonical pipeline 에 들어감) + **Stage 2 (Axiom Audit) 진입 가능한 기반**.

---

## Why now (어제 저녁 Rounds 12-18 의 직접 후속)

- 어제 사용자 직감 ("single formation 쪽 부족 → multi-formation 길 열림") 이 **정량 확정**됨. 부족한 것 = `(N_unst, ξ_0)`.
- 4 Cat A claims 모두 **수치 확정**:
  - Prop 1.3a: `Morse(u_uniform) = N_unst` exact at n=4096 (9/9 PASS)
  - Prop 1.3b: `H_cl_sep` β-invariant structural operator, spectrum [-4.97, +7.00], 1641 negatives
  - Cor 2.2 qualitative: `|B|/Per ∝ ξ_0` (3 independent axes)
  - Cor 2.2 quantitative: `C = π·ln(9)/2 ≈ 3.449` exact at n=262144 (20/20 PASS)
- 이 invariants 는 multi-formation `(K̂, size, spacing)` 을 **derived 로 예측**:
  - K̂ ~ 1 + √N_unst (Round 12 heuristic)
  - formation size ~ m/K̂
  - inter-formation spacing ~ ξ_0 · C (C = some O(1) constant)
- **어제 NEB-중심 plan.md (Stage 5 후속) 보다 SF-foundation consolidation 이 현 시점의 logical continuation**. NEB 정밀화는 C-S2 또는 후속 세션으로 carry.
- NQ-32 (SCC profile perturbation) 발견으로 new research direction 확보.

---

## Context refs (반드시 읽어야 할 자료)

**어제 Round 12-18 산출물 (필수)**:
- `THEORY/logs/daily/2026-04-21/14_single_formation_audit.md` (650줄) — Round 12-18 전체 통합, 4 Cat A + NQ-29~32 + §10 최종 통계
- `CODE/experiments/results/exp_hessian_uniform_v2.json` — Prop 1.3a/1.3b 수치 근거
- `CODE/experiments/results/exp_interface_ansatz.json` — Cor 2.2 quantitative 수치 근거
- `CODE/experiments/results/exp_alpha_scan_v3.json` — NQ-32 SCC profile perturbation 첫 증거

**어제 오전-오후 Stage 1 산출물**:
- `THEORY/logs/daily/2026-04-21/99_summary.md` — Rounds 1-11 요약
- `THEORY/working/E/soft_K_definition.md` (G1) — K_soft commit
- `THEORY/working/CE/free_energy_wellposed.md` (G3) — ℱ_C+E
- `THEORY/working/E/F1_dissolution.md`, `M1_dissolution.md`, `MO1_dissolution.md` (G4-G6)

**Canonical refs**:
- `THEORY/canonical/canonical.md` §13 (Cat A 정리 목록 — 특히 T-1, T-8-Core/Full, T-Birth-Parametric)
- `THEORY/canonical/canonical_sub.md` (Weekly merge buffer, 725줄 누적)
- `THEORY/working/integer_K_dependency_map.md` — 9+1 정리 목록

**외부 정리**:
- Modica-Mortola (1977) — Γ-convergence
- Cahn-Hilliard amplitude equation — mode emergence from spinodal
- Freidlin-Wentzell — Kramers escape rates (C-S2 carry)

---

## Current hypotheses / approaches

사용자의 잠정 방향 (에이전트는 이 안에 머물지 않음 — 출발점):

1. **Multi-formation 을 single-formation 의 "multi-mode instability" 로 재해석 가능**. `N_unst ≥ 2` regime 에서 K=2 가 자발적 — F-1 의 vacuity framing 자체가 integer-K 언어의 artifact 였음.

2. **K_hard 의 정확한 수학적 identification**: `K_hard(β, α, G, c) = #{local minima of ℰ on Σ_m} / |Aut(G)|`. Morse index at uniform (`N_unst`) 는 이 cardinality 의 lower bound.

3. **Inter-formation spacing 의 이론적 formula**: `d_min* ≈ C_1 · ξ_0 + C_2` (currently canonical T-d_min-Formula 의 `√(β/α)` scaling 이 dimensionally 반대). Round 13 Cor 2.2 의 `ξ_0` 가 올바른 scale.

4. **SCC profile = tanh + cl_sep perturbation**. Round 16 의 cl_sep structural operator (β-invariant, 1641 negatives) 가 interface shape 을 perturb. NQ-32 의 정량 조사가 **K=1 minimizer 의 "ideal Allen-Cahn 로부터의 deviation"** 을 설명.

핵심 미해소 질문:

- **Q1.** K̂ ≈ 1 + √N_unst 의 Round 12 heuristic 이 2D grid 이외 (1D, 3D, SBM) 에서도 성립하는가?
- **Q2.** SCC 의 interface profile fit 에서 effective ξ_0^{fitted} 가 theoretical √(α/β) 와 얼마나 벗어나는가? cl_sep 구조와 어떻게 연결되는가?
- **Q3.** M-1 의 "K=1 always preferred" 는 T-Merge (b) 의 long-time limit. 그러나 `N_unst ≥ 2` regime 의 short-time emergence 는 K≥2 — 이 두 timescale 의 분리가 **canonical CN6 ("K kinetically determined")** 의 정량 내용.
- **Q4.** MO-1 의 Σ²_M corner removal 이후, K_hard = `N_crit(Σ_m)` 의 Morse 정리 bound 를 얼마나 tight 하게 도출 가능?

---

## Session goals (G1-G7 deliverables)

### G1. `working/SF/` 신설 + 4 Cat A 정식 문서화

새 디렉토리 `THEORY/working/SF/` 신설:
- `README.md` — SF audit overview (링크 to 14_single_formation_audit.md)
- `mode_count.md` — Prop 1.3a (pure E_bd exact) + 1.3b (cl_sep operator structural)
  - Statement (formal)
  - Proof (Round 12 + Round 16 수치 근거)
  - Numerical verification table (exp_hessian_uniform_v2 9/9 PASS)
  - Multi-formation bridge (N_unst → K̂)
- `interface_scale.md` — Cor 2.2 qualitative + quantitative
  - Statement (formal, with explicit C = π·ln(9)/2 for tanh/edge)
  - Proof (Round 13 + Round 17 수치 근거)
  - Numerical verification table (exp_interface_ansatz 20/20 PASS, grid-invariance)
  - Multi-formation bridge (ξ_0 → formation size + spacing)
- `cardinality_open.md` — G-C 공백 (NQ-31)
- `profile_deviation.md` — NQ-32 (SCC profile perturbation, Round 18)

### G2. canonical_sub.md 2026-04-22 entry

Round 16-18 결과의 canonical merge candidate 기록:
- Added 4 (Prop 1.3a, Prop 1.3b, Cor 2.2 qualitative, Cor 2.2 quantitative)
- Clarified 1 (SCC full ℰ ≠ pure tanh profile, NQ-32)
- Pending (Stage 6 merge 대기):
  - canonical §13 Cat A 에 4개 정리 추가
  - canonical §5/§8 에 "Single-Formation Geometry" 신설 (~30줄)
  - CN18 신규 제안 ("Single-formation invariants (N_unst, ξ_0) determine multi-formation structure")

### G3. Multi-Formation New Perspective 초안 — `working/MF/from_single.md`

**중심 주장**: "multi-formation 은 single-formation 의 mode-count 확장"

구체 내용:
- **K̂ prediction**: `K̂(β, α, T, c, G) = f(N_unst(β, α, T, c, G))` — f 의 후보 3개 (√N_unst, log N_unst, linear). Round 12 heuristic (1 + √N_unst) 검증 필요.
- **Formation size**: `m_k ≈ m / K̂` (equal partition at short time; long-time isoperimetric → 단일 K=1).
- **Inter-formation spacing**: `d_min* ≈ C_spacing · ξ_0 + O(1/graph)` — Cor 2.2 의 C=3.449 와 비례 or 별도 spacing constant (derive 필요).
- **Dynamical picture**: 
  - t=0: u_uniform + noise
  - t < t_emerge: Fiedler-mode saturation → N_unst modes emerge
  - t_emerge < t < t_coarsen: metastable K̂ formations
  - t > t_coarsen: Ostwald ripening → K=1 global min (T-Merge (b))
- **canonical CN6 ("K kinetically determined") 의 정량 재해석**: "kinetic" = "nucleation at uniform instability of N_unst Fiedler-like modes".

### G4. F-1/M-1/MO-1 dissolution 재정식화

어제 `working/E/F1_dissolution.md` / `M1_dissolution.md` / `MO1_dissolution.md` 업데이트:
- **F-1 재정식화**: "K=2 vacuity" 는 integer-K language artifact. `N_unst ≥ 2` regime 에서 K≥2 가 자연 emergence. External m_j assumption 이 왜 불필요한지 `N_unst` 언어로.
- **M-1 재정식화**: T-Merge (b) 는 **long-time limit only**. Short-time `N_unst ≥ 2` emergence 는 K≥2 preferred. Two-timescale structure (emergence vs coarsening) 이 framing 해소.
- **MO-1 재정식화**: Σ²_M corner 제거 이후, K_hard = Morse index counts on Σ_m. Prop 1.3 이 direct lower bound.

각 dissolution 파일에 "Round 18 post-audit 재정식화" 섹션 추가.

### G5. NQ-32 — SCC profile perturbation 초기 조사 (script only, 실행은 사용자 local)

새 script `CODE/experiments/exp_profile_fit.py`:
- Input: SCC minimizer `u*` (from find_formation or loaded)
- Radial profile extraction (bin by distance from center of mass)
- Fit 3 candidate profiles: `tanh(s/ξ)`, `tanh_perturbed(s/ξ, ε_cl)`, `(cl_sep eigenmode)^T u` 기반 modified tanh
- Extract effective `ξ_0^{fitted}` vs theoretical `√(α/β)`
- Compare across (α, β) grid — profile deviation 가 parameters 에 따라 어떻게 scale?
- Write script only; 사용자 local 실행.

### G6. `integer_K_dependency_map.md` 업데이트

Round 12-18 의 관점에서 재작성:
- §2 (Retire 목록): 여전히 6개 정리 retire, 그러나 이유 업데이트 — "integer-K 가 single-formation invariants `(N_unst, ξ_0)` 로 derivable 하므로 integer-K 언어 자체가 불필요".
- §3 (단일 정리 survival): 22 Cat A + 이제 4 new Cat A = **26 total single-formation-basis Cat A**.
- §6 inconsistency 항목 resolve (T-d_min-Formula 의 dimensional reversal 이 Cor 2.2 quantitative 와 직접 충돌 → 재측정 필요, NQ-30).
- §7 Next Actions 업데이트.

### G7. Errata batch application + canonical_sub cleanup

**6 보류 errata 적용** (어제 세션 carry):
- E-4, E-5, E-6 (Round 2 보류): 어제 plan.md 에서 carry 된 것
- E-18, E-19, E-20 (Round 11 NEB 관련): M1_dissolution 에 cross-reference
- canonical_sub.md 의 725줄 누적 cleanup — 중복 제거, 8개 entry 구조 통일

---

## Non-goals (오늘 안 할 것)

- **어제 plan.md 의 NEB v5 / trust-constr 최적화 (G1)** — C-S2 또는 후속 carry. 오늘은 SF 통합.
- **Langevin 실행** (exp_three_regime / exp_mode_emergence) — Langevin sampler 작동 확인 이후 별도 세션.
- **NQ-32 full 조사** — G5 는 초기 script 만. 수치 실험 수 시간.
- **canonical.md 직접 수정** — 여전히 주간 merge 원칙 준수 (Stage 6 에서 통합).
- **Stage 2 Axiom Audit 본격 진입** — 본 세션은 Stage 1 완성 + Stage 2 pre-deliverable.
- **F4 T → 0 recovery 의 35 Cat A 전수 검증** — C-S3 carry.
- **새 Cat A commit (beyond 4 already-identified)** — 오늘은 기존 4개 consolidation.
- **G-D (Aut(G) orbit symmetry) 본격 진입** — post-Stage-1.

---

## Carry-forward (2026-04-21 로부터)

- **4 Cat A Round 16-18 confirmed**: Prop 1.3a/1.3b, Cor 2.2 qual/quant.
- **NQ-29 ~ NQ-32**: Morse inequality full, T-d_min-Formula 재측정, Multi-init survey, SCC profile shape.
- **15 Code files**: 5 어제 아침 + 5 Round 15 + 5 Round 16-18 (v2/v3/ansatz).
- **Langevin sampler + three_regime + mode_emergence**: 작성됨, 미실행. Stage 5 carry.
- **14 Daily files + 6 working files + 3 subdirs (E/, C/, CE/)**. 오늘 +working/SF/ + working/MF/.
- **Canonical merge buffer (canonical_sub.md)**: 725줄 누적. 오늘 +~60줄 예상 (2026-04-22 entry).
- **Session 어제 통계**: 18 rounds, 23 Cat A, 32 NQ, ~12,500줄.

---

## Success criterion for today

**저녁 시점에 G1-G7 7개 deliverable 이 모두 산출되어 있어야 한다.** 특히:

- **G1**: `working/SF/` 디렉토리 + 5 파일 (README, mode_count, interface_scale, cardinality_open, profile_deviation) — 각 100-300줄
- **G2**: `canonical_sub.md` 2026-04-22 entry — Added 4 + Clarified 1 + Pending 3
- **G3**: `working/MF/from_single.md` — K̂ prediction formula + timescale picture + CN6 재해석 (200-300줄)
- **G4**: 3 dissolution 파일 각각에 "Round 18 post-audit 재정식화" 섹션 추가 (각 50-100줄)
- **G5**: `exp_profile_fit.py` script 작성 (실행 x)
- **G6**: `integer_K_dependency_map.md` 재작성 (현재 107줄 → 약 150줄)
- **G7**: 6 errata 적용 + canonical_sub 중복 제거

**최소 priority (시간 부족 시)**: G1 + G2 가 minimum (Cat A commit 공식화). G3 + G4 가 두번째 (multi-formation reframing). G5-G7 은 carry 가능.

단계별 체크:
- [ ] G1 `working/SF/` 5 files
- [ ] G2 canonical_sub.md 2026-04-22 entry
- [ ] G3 `working/MF/from_single.md`
- [ ] G4 3 dissolution files update
- [ ] G5 `exp_profile_fit.py` script
- [ ] G6 `integer_K_dependency_map.md` rewrite
- [ ] G7 errata batch + canonical_sub cleanup

---

## 메모

- 본 plan 은 **2026-04-21 저녁 Round 12-18 완료 직후 작성**. 어제 저녁 NEB-중심 plan 을 대체.
- SF-S1 의 자연 scope = "어제 Round 16-18 결과의 공식화 + multi-formation 재해석 첫 걸음". 새 이론 영역 (예: `(T, λ_K)` phase diagram, disconnected graph) 은 후속 세션.
- `working/MF/` 는 새 directory — 기존 `working/E/` (K_soft, dissolution) 와 분리. E/ 는 "체험적 존재론적 해명", MF/ 는 "single-formation 으로부터의 derivation".
- G3 의 K̂ formula 검증은 오늘 scope 밖 — formula 제안만, 수치 검증은 exp_mode_emergence.py (작성됨) 로 후속.
- G5 의 profile fit 은 local 실행 대기. 어제 패턴 (코드만 작성) 유지.
- 본 plan 의 7 deliverables 은 어제 12-16h 일감 대비 약간 가벼운 수준 (G5 script only, G7 cleanup 중심) — 어제 에너지 회복 고려.
- 저녁 후속 (사용자 할 일):
  1. 7 deliverable 검토
  2. `canonical_sub.md` 2026-04-22 entry 수락 / 수정
  3. `exp_profile_fit.py` local 실행 여부 결정
  4. 2026-04-23 plan.md 작성 (SF-S2 또는 Stage 2 Axiom Audit 진입)
- 본 plan 의 scope 는 **Stage 1 완성 + Stage 2 preparation**. 내일 (2026-04-23) 부터 Stage 2 본격 진입 가능.

---

## 어제 저녁 plan.md (삭제/교체 대상) 의 중요 carry-over

어제 저녁 plan.md 의 G1-G7 중 본 plan 과 **중첩되지 않는 필수 항목**:

- **어제 G7 의 6 pending errata** (E-4/5/6/18/19/20) → 본 plan G7 에 흡수
- **어제 G5 의 integer_K_dependency_map update** → 본 plan G6 에 흡수
- **어제 G4 의 M1_dissolution Stage 5 결과 반영** → 본 plan G4 에 흡수

어제 plan 의 NEB-중심 항목 (G1-G3: trust-constr NEB v5, saddle Hessian Morse, mechanism filtering) 은 **본 plan 에서 제외** — C-S2 또는 후속 세션 carry. 이유: 어제 Round 16-18 의 SF consolidation 이 더 urgent logical continuation.

---

**End of 2026-04-22 SF-S1 plan.**
