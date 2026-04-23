# plan.md — 2026-04-24 Session Plan

**Session type:** Stage 2 Axiom Audit finalization + **Orbital Methodology Phase 1** (Rigorous Structural Identification).
**Prerequisite:** 2026-04-23 세션 완료 상태 — 5 Cat A empirical (orbital hierarchy + 56 stable + F=1 closure-elimination + $\mathcal{F}$ definitional + softmax refutation), Axiom S1' proposal, CN15/16/17 proposals, 32 new NQs, Phase 1-7 methodology scoped (see yesterday's user dialogue).
**Session working directory:** `THEORY/logs/daily/2026-04-24/`.
**Weekly buffer target:** `logs/weekly/2026-04-W4/weekly_draft_storming.md` §2026-04-24 에 end-of-session entry.

---

## §1. 세션 목표

오늘의 주제: **"어제 발견된 orbital structure를 atomic physics 차용 → SCC-intrinsic definition으로 전환"**.

어제 evening pivot의 empirical discovery (A-01~A-03) 는 "analogy-level Cat A at specific config". 오늘은 이것을 **구조적 Cat A** (graph-intrinsic irrep + nodal count 기반)로 승급하는 작업. 새 실험 없음 — 기존 90-run 데이터 재분석 + 이론.

1. **Axiom Audit 최종화** (2026-04-23 99_summary.md §8.1 Option N5) — Layer classification에 orbital sub-layer 통합
2. **M1 Symmetry-Reductive Decomposition** — 90-run Hessian eigenmode의 $D_4$ irrep 분류
3. **M3 Graph-Invariant Nodal Count** — Courant nodal domain count 으로 orbital label 재정의
4. **M2 Continuum Limit Analysis** (이론) — Spherical harmonic emergence rigorous derivation
5. **Axiom S1' Draft v1** — SCC-intrinsic 언어로 재작성 (orbital 용어 제거 후보)
6. **CN15/16/17 sharpening** — 각 CN의 proof-of-need + falsifiability test

---

## §2. Deliverables (5 goals, P0/P1 구분)

### G1 — Axiom Audit Finalization + Orbital Layer Integration (P0)

**목표**: 77 Cat A 의 Three-Layer classification 을 orbital context로 refinement. 어제의 "27% Mixed" 판정에서 얼마나 orbital-layer로 재할당 가능한지 정량.

**구체 작업**:
- 기존 `SF_layer_classification.md` (2026-04-23) 을 base로 re-pass
- Mixed 판정된 21개 claim을 orbital-layer 관점에서 재평가
- NQ-121 (orbital layer assignment): sub-layer 1.5 (orbital mode signature) 또는 Layer 2 refinement 결정
- 각 layer 의존 axiom set 정리 (A1'~A4 closure, Group B-E)

**Outputs**:
- `working/SF/layer_classification_v2.md` (신규) — 4-layer + Mixed table
- NQ-121 resolution 또는 더 구체 NQ로 분할

**Success criterion**: Mixed 비율 27% → 10% 이하 감소 또는 "Mixed가 본질적 범주임" 명시적 수용

### G2 — M1 $D_4$ Irrep Classification (P0)

**목표**: `exp_orbital_fullscale.json` (90 runs × 32×32 × full Hessian spectrum) 을 재로드하여 각 eigenmode의 $D_4$ irrep 분류.

**수학적 준비**:
- $D_4$ irreps: $A_1$ (trivial), $A_2$ (pseudoscalar), $B_1$ ($x^2-y^2$), $B_2$ ($xy$), $E$ (2D, contains $(x, y)$)
- Free-BC 32×32 grid 에서 grid center 기준 $D_4$ preservation
- Character table + projection operator 구현
- 각 eigenvector $\phi_k$에 대해 8 symmetry operation 적용 후 irrep decomposition

**구체 작업**:
- `CODE/scripts/orbital_irrep_classify.py` (신규, ~150줄)
- 90개 stable minimizer × 20 lowest Hessian modes = 1800 modes irrep label
- Angular multipole power (어제 계산) vs irrep label cross-check
- 어제 Cat A A-01의 "Mode 0 = p-dominant, Mode 1 = d-dominant" 재검증:
  - Mode 0 (near-zero eigenvalue) 은 **translation Goldstone (E irrep + broken discrete translation)** 인가 진짜 orbital 인가?
  - Mode 1 은 $A_1$ (radial 2s-like), $B_1$/$B_2$ (angular 2d-like), 또는 $E$ (2p-like) 중 무엇인가?

**Outputs**:
- `working/orbital/M1_irrep_classification.md` — irrep basis rigorous report
- Classification table: (config, mode index, irrep, nodal count, angular power, orbital label old vs new)
- A-01 Cat A entry refinement 권고: 만약 Mode 0 이 translation Goldstone 이면 statement 수정 필요

**Success criterion**: 1800 modes 전부 irrep-labeled, angular power 분해가 irrep projection 과 consistent

### G3 — M3 Nodal Domain Count + Courant Bound Verification (P0)

**목표**: 각 Hessian eigenvector 의 **nodal domain count** 계산, Courant-Fischer bound ($\mathcal{N}(\phi_k) \leq k$) tightness 확인.

**수학적 준비**:
- Graph nodal domain: $\{i : \phi_k(i) > 0\}$ connected components + $\{i : \phi_k(i) < 0\}$ components
- Connected component count via BFS on subgraph
- Strong Courant ($\mathcal{N} \leq k$) + weak Courant variants

**구체 작업**:
- `CODE/scripts/nodal_count.py` (신규, ~80줄)
- 20 lowest modes × 90 configs = 1800 entries
- Courant bound tight 여부 기록
- Full SCC Hessian 에서 $H_{\mathrm{cl,sep}}$ 보정이 nodal ordering 에 미치는 영향:
  - 어제 finding: "Mode 1 d-dominant" 이 만약 순수 Laplacian 대로면 2p 가 먼저여야 하지만 closure/sep 이 ordering 을 흔들 수 있음
  - 정량 확인

**Outputs**:
- `working/orbital/M3_nodal_count.md`
- Table: mode index × nodal count × Courant gap (기대값 - 실제)
- Cat A candidate: **"SCC cohesion mode n = nodal domain count of k-th Hessian eigenvector, Courant-ordered"**

**Success criterion**: Courant tight fraction ≥ 80% + 해석 제공

### G4 — M2 Continuum Limit Theory (P1)

**목표**: $n \to \infty$ 극한에서 SCC Hessian 의 continuous form rigorous 유도. Spherical harmonic $Y_{\ell m}$ eigenbasis 가 자연스럽게 등장하는 이유 증명.

**수학적 approach**:
- Discrete Laplacian $L = D - A \to -\Delta$ (continuous)
- Circular minimizer $u^*(r) = \frac{1}{2}(1 - \tanh((r - r_0)/\xi_0))$ (Cor 2.2)
- Linearize $H_1 = 4\alpha(-\Delta) + \beta W''(u^*) + H_{\mathrm{cl,sep}}$
- Radial coordinates $(r, \theta)$: separate angular + radial
- Angular equation: $Y_\ell(\theta)$ eigenbasis from $SO(2)$ symmetry at continuum
- Radial equation: shell-potential Schrödinger-like problem
  - $V(r) = \beta W''(u^*(r))/(4\alpha)$ — shell well near $r = r_0$
  - **Not Coulomb** — specific shell geometry → SCC-specific orbital spectrum (not hydrogenic)
- Finite-size $D_4$ correction: $V(r, \theta) = V_0(r) + \delta V_4(r) \cos(4\theta) + ...$ → ℓ=2 / ℓ=6 degeneracy splitting 설명

**구체 작업**:
- 이론 집중 session (실험 없음)
- Paper-level mathematical prose, ≥3 pages

**Outputs**:
- `working/orbital/M2_continuum_limit.md`
- Continuum Hessian closed form
- Spherical harmonic derivation proof
- Finite-size $D_4$ correction quantified (어제 "high β에서 mixing" 정량 설명)

**Success criterion**: Proof 이 peer-reviewable level. $SO(2)$ emergence explicit.

### G5 — Axiom S1' Draft + CN Sharpening (P1)

**목표**: Phase 1 결과 (G2-G4) 를 기반으로 Axiom S1' 을 **SCC-intrinsic 언어로 재작성**. CN15/16/17 은 proof-of-need + falsifiability 보강.

**Axiom S1' redraft structure**:
```
Axiom S1' (Cohesion Mode Quantization).
For any local minimum u* of E[u] on Σ_m with Morse index 0, there exists a
discrete signature {(n_k, [ρ_k], E_k)}_{k=1}^F specified by:
- F = |{i ∈ X : u*(i) > u*(j) ∀ j ~ i}|     (local maxima count)
- n_k = nodal domain count of k-th low-lying Hessian eigenvector     (G3)
- [ρ_k] ∈ Irr(Stab(u*) \ Aut(G))            (irrep class, G2)
- E_k = k-th eigenvalue of Hess E(u*)       (energy level)

Formation identity is determined by signature, not by K_step or by single-
observable K. Observables K_step, F, and signature components are derived.
```

**CN proof-of-need 구조 (각)**:
1. Claim statement
2. Without CN: 어떤 contradiction/ambiguity 발생
3. With CN: 무엇이 해소
4. Falsification test: 어떤 실험/관찰이 CN 을 반증 가능한가
5. Independent evidence: currently 존재하는 empirical support

**Outputs**:
- `working/canonical_drafts/axiom_S1_prime_v1.md` (신규 디렉토리 + 파일) ~3-4 pages
- `working/canonical_drafts/CN15_static_dynamic.md` ~1 page
- `working/canonical_drafts/CN16_protocol_parameterized.md` ~0.5 page
- `working/canonical_drafts/CN17_orbital_labeled_FQ.md` ~1 page

**Success criterion**: 각 draft 가 canonical-ready — user 가 weekly merge 시 minimal edit 으로 canonical.md 에 insert 가능한 quality

---

## §3. 우선순위

**P0 (반드시 완료)**:
- G1 (Axiom Audit finalization) — Stage 2 이행 필수
- G2 (M1 irrep classification) — 기존 데이터 재분석만으로 Cat A 승급 가능, highest value/hour
- G3 (M3 nodal count) — G2 와 병렬 실행, ~40% G2 time 추가

**P1 (주요, 시간 허용 시)**:
- G4 (M2 continuum limit) — theory-heavy, 2-3시간 focused prose
- G5 (Axiom S1' + CN drafts) — G1-G4 결과 종합 후 가능, endgame

**P2**: 없음 (오늘은 N5 방향 집중, 분산 금지)

---

## §4. Non-goals (명시적 제외)

- **새 실험 실행** — 모든 M-작업은 기존 90-run 데이터 + 이론으로 완결. 내일 G1-G5 만으로 충분
- **Phase 2 (Weight Simplex Sweep)** — W5 또는 내주 초로 이연 (scope creep 방지)
- **Phase 3-7** (graph generalization, frustration formalization, NEB, molecular) — 내일 범위 아님
- **Canonical.md 직접 수정** — 모든 변경은 `working/` + `logs/weekly/2026-04-W4/weekly_draft_storming.md` 에 accumulate
- **F-1 / M-1 / MO-1 heavy engagement** — orbital 맥락 외에서는 오늘 out of scope
- **Multi-formation orbital 확장** — Phase 5, 오늘 단일 formation만

---

## §5. 작업 흐름

**Morning (3-4시간, P0 병렬)**:
- G2 + G3 병렬 실행:
  - 10:00: 90-run data reload, `orbital_irrep_classify.py` + `nodal_count.py` 작성
  - 11:00: 실행 (전체 ~30분), raw output 수집
  - 11:30-13:00: output 분석, table 작성, Cat A refinement 판단
- 산출물: `working/orbital/M1_irrep_classification.md`, `M3_nodal_count.md`

**Afternoon (3-4시간, G1 + G4)**:
- G1: Layer classification v2, orbital sub-layer 통합 (1.5-2시간)
- G4: Continuum limit rigorous derivation (2-3시간, theory-heavy)

**Evening (2-3시간, G5)**:
- Axiom S1' v1 draft
- CN15/16/17 sharpening
- Weekly buffer 에 2026-04-24 entry append

**Late (buffer, 필요 시 ~1시간)**:
- 세션 summary + NQ triage
- Weekly close prep (W4 final day since 2026-04-25)

총 예상 세션 길이: **10-12시간**

---

## §6. R23 Carry-forward

이월된 pending items:
- **Q23-Q32** (2026-04-23 canonical merge user 결정 목록, 10개): 오늘은 이들에 대한 **stance statement** 작성 (user 결정 재료).
- **NQ-111..NQ-124** (orbital-specific, 14개): G1-G5 결과가 일부 close.
  - NQ-121 (orbital layer assignment): G1에서 해결 시도
  - NQ-92 (R18 F re-measurement): 내일 out of scope, carry
  - NQ-117 (normalize=True): 내일 out of scope
  - NQ-119 (48×48, 64×64 grid): 내일 out of scope, Phase 3 영역
- **32 new NQs (NQ-51..NQ-75)** (오전 scoping): G1 관련 일부 (NQ-51 layer refinement) 답할 수 있음

---

## §7. 성공 기준

세션 종료 시 (in order of priority):

- [ ] **P0-1**: 90-run 전체 modes 가 (irrep, nodal count) signature 로 재분류 완료 (~1800 entries)
- [ ] **P0-2**: Courant bound tight fraction ≥ 80% 확인 또는 deviation 해석
- [ ] **P0-3**: Mode 0 이 translation Goldstone vs 진짜 orbital 판정 → A-01 Cat A statement 검증
- [ ] **P0-4**: 77 Cat A 의 4-layer + Mixed 재할당, Mixed 비율 감소 또는 본질성 확증
- [ ] **P0-5**: `working/SF/layer_classification_v2.md`, `working/orbital/M1_*.md`, `working/orbital/M3_*.md` commit
- [ ] **P1-1**: Continuum limit $SO(2)$ emergence proof ≥ 1 page
- [ ] **P1-2**: Axiom S1' v1 draft ≥ 2 pages (SCC-intrinsic language)
- [ ] **P1-3**: CN15/16/17 proof-of-need 각 ≥ 0.5 page with falsifiability test
- [ ] **P1-4**: `working/orbital/M2_*.md`, `working/canonical_drafts/*.md` commit

**Minimum acceptable outcome**: P0 4/5 + weekly buffer entry.

---

## §8. 종료 기준

다음 조건 하나라도 충족 시 종료:

- P0 전부 + P1 절반 이상 완료 + 모든 working files commit
- 12시간 초과 + P0 80% 이상
- 예기치 못한 methodology 문제 발견 (예: irrep decomposition numerical unstable, Mode 0 classification ambiguous) → 조기 종료, 다음 날 재설계

---

## §9. Stage 가이드라인 (self-check)

**Silent resolution 금지**:
- F-1, M-1, MO-1 은 오늘 직접 target 아님. 우연히 해소 보이면 명시적으로 "partial answer via orbital methodology" 로 기록
- Axiom S1' 이 Formation Quantization 관련 earlier claims 를 silently supersede 하지 않도록 — explicit promotion/retirement statement

**Borrowing trap 방지**:
- "Atomic orbital" 용어는 explanatory only. Definition 에는 irrep + nodal count 만 사용
- 만약 SCC orbital energy 가 $E_n = -1/n^2$ 처럼 hydrogenic form 따르는 우연 발견 시 → structural parallel 확인, 하지만 reduction claim 금지 (Hard Constraint #4)
- G5 Axiom S1' draft 에서 "orbital" 단어 최소화

**Canonical 경계 존중**:
- Canonical.md 직접 수정 없음
- Theorem_status.md 직접 수정 없음
- 모든 변경 제안은 `logs/weekly/2026-04-W4/weekly_draft_storming.md` 또는 `working/canonical_drafts/` 경유

---

**End of plan.md for 2026-04-24.**
**Target: orbital-by-analogy (Apr 23) → orbital-by-structure (Apr 24). Phase 1 closure.**
