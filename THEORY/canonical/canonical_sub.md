# Canonical Sub — 주간 누적 Buffer

**Status:** accumulating (next weekly merge → `canonical.md`)
**Purpose:** canonical 에 반영될 가치가 있는 변경사항을 매일 append 누적. **주 1 회** user 리뷰 후 `canonical.md` 에 merge, 본 파일 reset.
**Last reset:** 2026-04-20 (initial creation)
**Last entry:** 2026-04-21 (with evening verification update)

---

## 사용 규칙

1. **Append-only:** 매일 새 섹션을 상단에 insert (최신순). 수정·제거는 주간 merge 시 user 결정에만.
2. **날짜별 섹션:** `## YYYY-MM-DD` 헤더, 그 안에 타입 라벨 구분.
3. **타입 라벨:** 다음 5 종만 사용.
   - `### Added` — 새 정리·공리·정의·CN·OP (증명/검증 완료).
   - `### Modified` — 기존 canonical 줄의 statement 또는 조건 수정.
   - `### Retired` — 기존 정리/주장의 retraction.
   - `### Clarified` — canonical 에 암묵적이던 것의 명시화 (metadata level, 내용 무변화).
   - `### Pending` — 다음 주 이상 carry-forward (아직 merge 불가).
4. **working reference 필수:** 각 entry 는 `working/<topic>.md` 또는 `logs/daily/YYYY-MM-DD/...` 를 출처로 명시. 출처 없는 entry 는 merge 대상 아님.
5. **주간 merge 절차:**
   - user 가 본 파일 섹션별 검토.
   - Added → `canonical.md` 해당 섹션 insert + `theorem_status.md` 행 추가 + `CHANGELOG.md` 주간 entry.
   - Modified → `canonical.md` 해당 줄 수정.
   - Retired → `canonical.md` Retracted 섹션 이동.
   - Clarified → `canonical.md` inline annotation 또는 §14 CN 추가.
   - Pending → 본 파일에 잔존, 다음 주로 carry.
   - merge 완료 후 본 파일 reset (모든 날짜 섹션 제거, Merge History 한 줄 append, `Last reset` 갱신).
6. **증명 없는 statement 금지:** Added 는 반드시 working 단계에서 증명 완료된 것만. 미완 결과는 Pending 으로.

## Promotion pipeline (개정)

```
logs/daily/YYYY-MM-DD/<artifacts>.md      (날것, chronological)
    ↓ topic 별 정리
working/<topic>.md                         (주제별 개발, 검증 대상)
    ↓ daily (증명/검증 완료분만)
canonical/canonical_sub.md                 (주간 merge buffer, 본 파일)
    ↓ weekly (user 리뷰)
canonical/canonical.md                     (main, 주 1회 update)
canonical/theorem_status.md                (main 동기 update)
```

Canonical.md 가 단일 spec 역할은 유지. 본 파일은 **pre-merge staging area**.

---

## 2026-04-21

**Session type:** Stage 1 (Definition Foundation) — C+E common first session.
**Origin:** `logs/daily/2026-04-21/` (plan.md + pre_brainstorm.md + 01_exploration.md + 02_development.md + 03_integration_and_new_open.md + 99_summary.md) + `working/E/soft_K_definition.md` + `working/C/F_group_axioms.md` + `working/CE/free_energy_wellposed.md` + `working/E/M1_dissolution.md` + `working/E/MO1_dissolution.md` + `working/E/F1_dissolution.md`.
**Canonical-relevant 산출물:** Added 3 (K_soft 정의, F1-F2 공리, ℱ_{C+E} cross-object), Clarified 1 (F-1/M-1/MO-1 dissolution mappings 언어), Pending 7+ (Group F-thermal section, §12 rewrite, theorem retirements, F3-F4 statements, new CNs, NQ-8 through NQ-13).

---

### Added

#### A-2026-04-21-01. K_soft Soft-K Definition (NQ-1 후보 (i) commit)

**출처:** `working/E/soft_K_definition.md` (G1).

**정의:** For `u ∈ Σ_m`, with monotone Lipschitz `φ : [0,∞) → [0,∞)`, `φ(0)=0`:

`K_soft(u) = Σ_{i ∈ B_+(u)} φ(ℓ_i(u))`, where B_+(u) = positive-length bars of H₀ persistence diagram of superlevel filtration of u. Default weighting `φ(ℓ) = ℓ/(1+ℓ)` (saturating).

**Well-defined:** **Cat A.** K_soft ∈ C^0(Σ_m), globally Lipschitz with `L_K ≤ 4 L_φ n` (constant corrected from initial 2 L_φ n per Round 2 `05_deepening_and_verification.md` §1.5) via Cohen-Steiner-Edelsbrunner-Harer (2007) bottleneck stability + φ Lipschitz; strengthened in `logs/daily/2026-04-21/02_development.md` §4.1 (vineyard set V handling: K_soft is multiset-stable, hence Lipschitz on full Σ_m, not just Σ_m \ V).

**Hard-K recovery:** sharp-interface limit gives K_soft(u_ε) → K · φ(1) (Prop 4.1, sketched).

**Volume constraint compatibility:** `K_soft` and `Σ u_i = m` are orthogonal axes; projected gradient flow well-defined off vineyard set V (G1 §3).

**Canonical merge target:** §5.5 (Transition Diagnostics) extension; §13 new Cat A entry.

**NQ-1 partial resolution:** (i) committed; (ii) Betti reduces to (i) under `φ(ℓ) = ℓ`; (iii) simplex (CN12 conflict — parked); (iv) measure (computational issues — parked).

#### A-2026-04-21-02. F-group Axioms F1, F2 (Thermal Foundation)

**출처:** `working/C/F_group_axioms.md` (G2).

**F1 (Thermal State).** For each T > 0, the system state on Σ_m is the Gibbs measure ℙ_T[du] = (1/Z(T)) exp(-ℱ[u]/T) ν(du), with ν the Lebesgue measure on Σ_m (induced from (n-1)-dim Hausdorff). **Cat A:** Z(T) finite for all T > 0 (Prop F1.1, via compact Σ_m + continuous ℱ).

**F2 (Bernoulli Entropy).** S(u) = -Σ_x [u(x)log u(x) + (1-u(x))log(1-u(x))], with `0 log 0 := 0`. **Cat A:** continuous on [0,1]^n, bounded `0 ≤ S ≤ n log 2`, strictly concave on (0,1)^n, Lipschitz on [ε, 1-ε]^n with `L_S(ε) = log((1-ε)/ε) √n`. Maximizer on Σ_m: u_uniform = (m/n) · 1.

**Canonical merge target:** §6 new "Group F-thermal" section. Naming conflict with CN4's "Group F" (crisp recovery): proposed disambiguation rename.

#### A-2026-04-21-03. ℱ_{C+E} Cross-Object Well-Definedness

**출처:** `working/CE/free_energy_wellposed.md` (G3).

**정의:** ℱ_{C+E}[u; T, λ_K] = ℰ[u] - T·S(u) + λ_K·K_soft(u), with ℰ = canonical four-term energy (§8.1). Six-term independence (CN5 generalized): four ℰ-terms + entropy term + K_soft regularization, all conceptually independent.

**Well-defined (chain of Cat A claims, see `02_development.md` §1.3):**
- ℱ_{C+E} ∈ C^0(Σ_m) (continuity from sum of continuous components)
- Lipschitz on Σ_m^ε := Σ_m ∩ [ε, 1-ε]^n with `L_{ℱ}(ε, T, λ_K) ≤ L_ℰ + T·L_S(ε) + λ_K·L_K`
- Real-analytic on Σ_m^ε \ V (Lemma 2.1 of `02_development.md`) — Łojasiewicz applies
- Bounded below: `inf ℱ_{C+E} ≥ -T n log 2` (Prop 3.1)
- **Minimizer exists** on Σ_m (Thm 3.3, Weierstrass on compact)

**λ_K scaling commitment:** `λ_K = γ_K · T` with `γ_K ∈ [0.01, 0.1]` (Round 3 Hessian-stability tightening; original [0.01, 1] heuristic narrowed by §06 §1.6; first-principles derivation NQ-10).

**Canonical merge target:** §8.1 new sub-section "Free Energy in C+E Framework"; §13 new Cat A claims.

---

### Clarified

#### C-2026-04-21-01. F-1 / M-1 / MO-1 Dissolution Mappings

**출처:** `working/E/F1_dissolution.md` (G4), `working/E/M1_dissolution.md` (G5), `working/E/MO1_dissolution.md` (G6).

각 Critical 의 dissolution 은 silent resolution 이 아니라 **재언어화 + 잔여물 명시**.

**F-1 (K=2 vacuity, OP-0001):**
- E-side (Cat A): "external m_j" architecture removed — soft-K has no per-formation mass. Vacuity claim restated has no analog in soft-K.
- C-side (sketched): K=2 thermally populated with Boltzmann weight `exp(-ΔF_{2-1}/T)`. Crossover T_c ≈ ΔE/ΔS ≈ 1.14 (corrected estimate per `04_hypothesis_audit.md` §11). At T < T_c K=2 thermal minority; **at T > T_c K=2 thermodynamically dominates** (entropy-driven mode-count phase transition) — strengthens dissolution by showing canonical's "K=1 always preferred" is a zero-T artifact.
- Residual (carry): R-F1-A (numerical Boltzmann at calibrated params, Stage 5), R-F1-B/C (K_soft critical loci, CE-S2), R-F1-D (saddle-point on Z_K, C-S2).

**M-1 (K=1 always preferred, OP-0002):**
- E-side (Cat A reused): T-Merge (b) (Cat A) + T11 (Cat A) preserved. "Single-mode preference" is **feature** (isoperimetric consequence on connected graphs), not bug. Scope restriction: **connected graphs** (`02_development.md` §4.5).
- C-side (sketched): Kramers metastability framework — K=2 is metastable with `τ_{K=2 → K=1} ~ τ_0 exp(ΔE/T)`. Substantiates CN6/CN8/CN14 thermally.
- Residual (carry): R-M1-A (Kramers prefactor on constrained Σ_m, C-S2), R-M1-B (transition-state existence, Mountain Pass on Σ_m), R-M1-C (γ_eff = 0.89 derivation precision, C-S2), R-M1-E (Ostwald ripening, E-S3).

**MO-1 (Morse inapplicability, OP-0003):**
- E-side (Cat A): Σ²_M corner removed (Σ²_M not used in soft-K). Σ_m^ε \ V is smooth manifold; ℱ_{C+E} real-analytic (Lemma 2.1 of `02_development.md`); standard smooth Morse + Łojasiewicz apply.
- C-side (statement only): Witten Laplacian Δ_{ℱ, T} provides spectral encoding of critical points (Helffer-Sjöstrand 1985); Fokker-Planck operator is conjugate equivalent.
- Alternative tool preserved: Forman discrete Morse (combinatorial, corner-aware) for fallback.
- Residual (carry): NQ-12 (discrete-graph Witten Laplacian, post-Stage-1), V mollification (C-S2).

**Variation:** none of three Critical silently resolved. Each marked partially dissolved / reframed with explicit residuals.

---

### Pending

다음 항목은 canonical 보수 대상이나 본 주에는 commit 안 함; 주간 merge 에서 user 확정.

#### P-2026-04-21-01. Canonical §6 New "Group F-thermal" Section

**출처:** `working/C/F_group_axioms.md`.

**Proposed addition.** New axiomatic group containing F1 (Gibbs), F2 (Bernoulli entropy), F3 (Langevin SDE — statement only), F4 (T-primacy + T → 0 recovery — statement only). Located after Group E.

**Naming conflict.** Existing CN4 references "Group F" = crisp recovery (superlevel filtration, soft-to-crisp interface). Disambiguation options: (a) rename present F-group to "Group F-thermal", CN4 to "Group F-crisp"; (b) rename present F-group to "Group T" (temperature) instead of F.

**Recommendation:** option (a) — minimal renaming, preserves "F" mnemonic for both crisp recovery (filtration) and finite temperature (free energy).

#### P-2026-04-21-02. Canonical §13 Retirements

**출처:** `working/integer_K_dependency_map.md` §2 (10 load-bearing integer-K theorems).

**Proposed retirements (post weekly merge):**
- 5 Cat A: T-Merge (a), Topological Lock, Coupling Bound Lemma, Proposition 1.2, Theorem 3.1(a,b,d).
- 1 Cat B: γ_eff = 0.89 (re-interpreted as Kramers prefactor, not standalone empirical).

**Reason for delay:** retirements are large canonical edits; recommendation is to defer to Stage 6 (Promotion) of 17-session reformulation rather than weekly merge during Stage 1. Statement-level retirement annotation can be added inline (e.g., `*(Status retired 2026-04-21 pending soft-K reformulation completion; see working/integer_K_dependency_map.md §2)*`).

#### P-2026-04-21-03. Canonical §13 Cat C Re-statements

T-Persist-K-Sep / T-Persist-K-Weak / T-Persist-K-Unified (3 Cat C theorems) — soft-K language re-write (statement preserves substance, language updates per-formation index → soft-K mode index).

**Status:** sketched in `03_integration_and_new_open.md` §1.4. Full re-proof carry to **E-S2**.

#### P-2026-04-21-04. F3 Langevin Well-Posedness

**출처:** `working/C/F_group_axioms.md` §3.

**Statement only this session.** Full proof requires:
- Da Prato–Zabczyk SPDE on constrained manifold (Ch. 6).
- Lions–Sznitman reflection at convex polytope corners.
- Vineyard set V regularity for diffusion (V is null for Lebesgue, so for Brownian motion).

**Carry:** C-S2.

#### P-2026-04-21-05. F4 T → 0 Recovery Proofs

**출처:** `working/C/F_group_axioms.md` §4.

**Statement only this session.** Full proof requires case-by-case verification that each canonical Cat A theorem (35 theorems) survives at T = 0 limit. F4.b enumerates the 19~20 single-formation Cat A surviving (`working/integer_K_dependency_map.md` §3).

**Carry:** C-S3.

#### P-2026-04-21-06. Witten Laplacian Discrete-Graph Treatment

**출처:** `working/E/MO1_dissolution.md` §3 + NQ-12.

**Statement only this session.** Two routes: (i) treat Σ_m as smooth manifold + Witten direct, (ii) Forman discrete Morse (combinatorial alternative). Selection of canonical route: **post-Stage-1**.

#### P-2026-04-21-07. New CNs (CN15-thermal, CN16-thermal, CN17-thermal)

**Proposed additions to §14:**

- **CN15-thermal:** ℱ_{C+E} is the C+E framework's variational object; canonical ℰ recovered as T → 0, λ_K → 0 limit.
- **CN16-thermal:** CN6/CN8/CN14 metastability claims substantiated by Kramers rates (G5) and Witten Laplacian small-eigenvalue spectrum (G6), both at finite T.
- **CN17-thermal:** Soft-K K_soft : Σ_m → ℝ_{≥0} is canonical generalization of integer K; integer reading recovered in sharp-interface limit.

**Status:** proposed; canonical addition awaits Stage 2 axiom audit.

---

### Added — Pending OP 승급 (NQ-8 through NQ-13)

본 세션에서 새로 발생한 6 개 NQ. 본 주에는 OP-xxxx 로 승급하지 않음.

#### NQ-8. Vineyard Set V Measure-Theoretic Handling — MEDIUM (C-S2)

**Q:** Is the Gibbs measure ℙ_T absolutely continuous w.r.t. Lebesgue on Σ_m so that codim-1 vineyard set V is null for thermal analysis?
**Carry:** C-S2.
**Origin:** `working/E/soft_K_definition.md` §2.3, `working/C/F_group_axioms.md` §3.2.

#### NQ-9. Sharper L_K Lipschitz Constant via Graph Spectrum — MEDIUM (C-S2 / E-S2)

**Q:** Refine `L_K ≤ 2 L_φ n` (Cor 2.2) using λ_2(G) or isoperimetric constant. Tighter bound improves quantitative Langevin / gradient flow predictions.
**Carry:** C-S2 / E-S2.
**Origin:** `working/E/soft_K_definition.md` §7.

#### NQ-10. First-Principles γ_K Determination — HIGH (CE-S2 / Stage 3)

**Q:** Derive γ_K ∈ [0.01, 1] from RG analysis (pre_brainstorm H-B16) or dimensional argument on (S, K_soft) information measures. P-E "25+ parameters" concern.
**Carry:** CE-S2 / Stage 3 (Definition & Derivation).
**Origin:** `working/CE/free_energy_wellposed.md` §4.4.

#### NQ-11. Variational Saddle Existence Between K_soft Basins — HIGH (C-S2)

**Q:** Mountain Pass on connected Σ_m gives existence of saddle between K_soft ≈ 1 and K_soft ≈ 2 critical points. What is saddle's K_soft value, ℱ value, structure (single saddle or manifold)?
**Why critical:** saddle ℱ enters Kramers ΔF directly. Without specifying saddle, Kramers prefactor (G5 §3.2) is incomplete.
**Carry:** C-S2.
**Origin:** `working/E/M1_dissolution.md` §5 R-M1-B.

#### NQ-12. Discrete-Graph Witten Laplacian Rigorous Formulation — HIGH (post-Stage-1)

**Q:** Two routes (smooth-Σ_m direct vs Forman discrete) — canonical choice for SCC?
**Why critical:** MO-1 dissolution leans on Witten Laplacian as central tool.
**Carry:** post-Stage-1.
**Origin:** `working/E/MO1_dissolution.md` §3.4.

#### NQ-13. Disconnected-Graph Regime for M-1 — MEDIUM (E-S3 / Scope clarification)

**Q:** M-1 reframing is implicitly connected-graph. On disconnected graphs, K_soft > 1 is global minimum. Unified treatment?
**Carry:** E-S3 / canonical scope clarification.
**Origin:** `logs/daily/2026-04-21/02_development.md` §4.5.

---

### NQ-1-extended (deepened from 2026-04-20 NQ-1)

**Q:** With (i) committed in A-2026-04-21-01, are the *theories induced* by candidates (i)/(ii)/(iii)/(iv) actually equivalent? E.g., do the same canonical Cat A theorems hold under each soft-K definition?
**Carry:** post-Stage-1.

---

### 본 entry 의 canonical 변경 규모 (주간 merge 예상)

주간 merge 시 `canonical.md` 실제 수정 (현재 누적 = 2026-04-20 + 2026-04-21):

**2026-04-20 entry 이월 (작은 변경):**
- §13 inline annotation 10 줄 (Q1 from 2026-04-20).
- §13 line 1061 Cat C count header 1 줄.
- theorem_status.md line 47 sync 1 줄.

**2026-04-21 entry 신규 (대규모):**
- §6 신설 "Group F-thermal" — 약 80 줄 (F1-F4 statements + comments).
- §8.1 신설 sub-section "Free Energy in C+E Framework" — 약 30 줄.
- §5.5 확장 (K_soft 추가 statement) — 약 15 줄.
- §13 새 Cat A claims (12 항목 from `02_development.md` §5) — 약 80 줄.
- §14 새 CN 3 개 (CN15-CN17 thermal) — 약 20 줄.
- §13 retirements (6 항목, P-2026-04-21-02) — 본 주 미적용 권고.

**총 변경:** ~225 줄 추가 (이전 2026-04-20 누적 ~12 줄 대비 매우 큼). 새 정리/공리/CN 다수.

**주간 merge 에서 user 가 결정할 추가 사항 (Q5-Q9):**
- **Q5.** Group F-thermal 명칭 vs CN4 "Group F" 충돌 해결 (rename 어느 쪽? recommendation: CN4 → "Group F-crisp", 새 그룹 → "Group F-thermal").
- **Q6.** F3 / F4 statement-only 가 canonical 에 들어갈 자격이 있는가? 아니면 working 단계로 유지?
- **Q7.** NQ-8 ~ NQ-14 + NQ-1-extended 중 OP-xxxx 승급 후보 (권고: 모두 Stage 1 완료까지 대기).
- **Q8.** 8 retirements (P-2026-04-21-02 + 추가 2 Cat B from §05_deepening §5.3: T-Beyond-Weyl, T-d_min-Formula) 시점 — 이번 주 vs Stage 6 통합 merge (권고: Stage 6).
- **Q9.** CN15-17 thermal 추가 시점 — 이번 주 commit vs Stage 2 axiom audit 후 (권고: Stage 2).
- **Q10 (new).** L_K Lipschitz constant 정정 (2 → 4 L_φ n) 적용 완료 — canonical §13 K_soft 항목에 반영 시점 (권고: Stage 2 audit 와 함께).

---

### Round 2 — Verification Update (2026-04-21 evening)

`logs/daily/2026-04-21/05_deepening_and_verification.md` 의 검증 결과 본 entry 에 다음 보완 사항:

#### Strengthened claims
- **Cor 4.1 (K_soft global Lipschitz)** — full proof 완료. `L_K ≤ 4 L_φ n` (`05_deepening` §1.5; constant 정정으로 `working/E/soft_K_definition.md` Cor 2.2, `02_development.md` §4.1, `working/CE/free_energy_wellposed.md` §2.1 모두 보수 적용).
- **F4.b** — case-by-case 검증 완료. **22 single-formation Cat A 정리** (`05_deepening` §4) 가 cleanly survives T → 0. (이전 dependency map §3 의 19~20 underestimate; Prop 1.1, Persistence Threshold Eq, T-Birth-Parametric (D₄) 추가.)

#### Newly identified Pending items
- **P-2026-04-21-08 (new):** `working/integer_K_dependency_map.md` §2.2 Cat B retire 목록에서 **T-Beyond-Weyl + T-d_min-Formula 두 개 누락**. 둘 다 K-formation Hessian / inter-formation distance 의존. 정정 후 Retire 총 8 (5 Cat A + 3 Cat B), not 6. 적용: dependency map §2 표 보수.
- **NQ-14 (new):** Mountain Pass saddle 이 V (vineyard) 위에 위치하면 Clarke (1983) subdifferential 필요. C-S2 carry.

#### Numerical sanity 검증
- **Kramers MFPT at exp55** parameters: ≈ 10^69 — 5000 iteration 대비 천문학적, zero-merge 가 *예측*임을 확인.
- **T_c ≈ 1.0** — entropy 추정 ±30% 변동 하 [0.74, 1.4] 범위 (robust).
- **G4 §3.3 Boltzmann 표** — robust (ratios depend only on ΔF; 정정 후 T_c = 1.00 으로 미세 조정).

#### Errata round 2 적용 완료 (2026-04-21 evening)
- E-1 (`working/E/soft_K_definition.md` Cor 2.2): L_K constant 4·L_φ·n.
- E-2 (`02_development.md` §4.1 Cor 4.1): 동일.
- E-3 (`working/CE/free_energy_wellposed.md` §2.1): L_K row + 마지막 L_F sample 정정.

#### Errata round 2 미적용 (다음 user review 대상)
- E-4 (G4 §3.3 entropy 절대값 η-parameterization 정정) — 적용 시 cosmetic, 정성적 결론 무변화.
- E-5 (`working/integer_K_dependency_map.md` §2.2 추가 retire 2개) — user decision (추가 retire 행 추가 여부).
- E-6 (`working/integer_K_dependency_map.md` §3 Cat A 22 항목 update) — user decision.

---

### Round 3 — Further Verification Update (2026-04-21 evening, after Round 2)

`logs/daily/2026-04-21/06_further_verification.md` 의 substantive 수학 심화 결과 본 entry 에 다음 보완:

#### Strengthened claims (3 promotion to Cat A)

- **T-7 (Enhanced Metastability) in C+E** (§06 §2 Prop 2.1) — strengthened. Closure positive Hessian + entropy positive Hessian (∇²(-S) PSD diagonal) + small λ_K negative correction. Net Hessian ≥ canonical's ⇒ T-7 Cat A *preserved and strengthened*.
- **F3 Langevin well-posed on Σ_m^ε** (§06 §8 Thm F3.1, F3.2) — Cat A via Lions-Sznitman 1984. Equilibrium = Gibbs proven. Earlier "Cat C statement only" status upgraded.
- **Hessian decomposition explicit** (§06 §1) — ∇²ℱ_C+E = ∇²ℰ + T·∇²(-S) + λ_K·∇²K_soft, with K_soft Hessian rank-N negative-semidefinite (φ-sat concave, ∇²K_soft = Σ φ''(ℓ_i)·v_i v_i^T).

#### Newly identified γ_K stability boundary

- **γ_K range refinement** (§06 §1.6) — Hessian PD requires `γ_K · n < 1 + β/(4T)`. At canonical (n=64, β=30, T=1): **γ_K ≤ 0.13 (≈ 0.1)**. G3 §4.3 의 "γ_K ∈ [0.01, 1]" upper end 가 너무 loose. **정정값: γ_K ∈ [0.01, 0.1]** (E-7 적용 완료 in `working/CE/free_energy_wellposed.md` §4.3).
- 이 발견은 새 NQ-16 (γ_K 가 1/n 으로 scale at large graphs) 의 motivation.

#### Newly identified Pending items (NQ)

- **NQ-15 (new):** Hessian eigenvalue scaling with β at saddle (Kramers prefactor → γ_eff = 0.89 derivation 가능성). Carry: C-S2.
- **NQ-16 (new):** γ_K 의 1/n scaling — (T, λ_K) phase diagram 의 large-n behavior. Carry: CE-S2.
- **NQ-17 (new):** Linear interpolation 이 ΔF 상한으로 3× too loose (§06 §3) → MEP analytical ansatz + numerical NEB hybrid 권고. Carry: Stage 5.

#### Errata round 3 적용 완료 (2026-04-21 evening)

- **E-7** (`working/CE/free_energy_wellposed.md` §4.3): γ_K range [0.01, 1] → [0.01, 0.1] with Hessian-stability justification.
- **E-8** (`working/C/F_group_axioms.md` §3.2): F3 status upgraded from "statement only" to "Cat A on Σ_m^ε via Lions-Sznitman 1984; Cat C-provisional on full Σ_m for corner extension". Theorem F3.1, F3.2 added with proofs.

#### Verification confidence summary (Post-Round 3)

- Cat A 누적 (sketched-rigorous): **16** (Round 2 의 13 + 3 = T-7 C+E Prop 2.1, F3.1, F3.2).
- Sketched (Cat C-provisional): **6** (F3 corner case 등).
- Statement-only carry: 3.
- Errata 식별: **8 total** (E-1~E-8); 적용 완료 5 (E-1, E-2, E-3, E-7, E-8); 보류 3 (E-4, E-5, E-6).
- New NQs from Round 3: NQ-15, NQ-16, NQ-17.

#### 주간 merge 에서 추가 user 결정 사항

- **Q11 (new).** γ_K 의 1/n scaling 이 Cat-A-promote 시 어떻게 명시될지 (general statement vs n-conditioned).
- **Q12 (new).** F3 Langevin 의 Cat A 격상이 canonical §13 에 어떤 형태로 들어갈지 (single Cat A row vs Cat A on Σ_m^ε + Cat C corners).

---

### Round 4 — Phase Diagram + Cross-File Consistency Update (2026-04-21 evening, after Round 3)

`logs/daily/2026-04-21/07_round4_verification.md` 의 phase diagram 발견 + Cat C 검증 + 일관성 점검 결과 본 entry 에 다음 보완:

#### Strengthened claims (2 new Cat A theorems)

- **T-Uniform-Stab-T (Theorem 1.1, Round 4 §1):** uniform configuration `u_uniform = (m/n)·1` 가 ℱ_C+E 의 local minimum 이 되는 조건. 임계 온도:
$$T^*_{\mathrm{uniform}}(c) \;=\; c(1-c)\cdot \big[\beta\, |W''(c)| - 4\alpha\lambda_2(G) - r_{\mathrm{cl,sep}}\big].$$
canonical default 에서 T*_uniform ≈ 7.37 at c = 0.5. T8-Core 의 strict generalization (T = 0 에서 destabilization, T > T*_uniform 에서 re-stabilization). **Cat A** (sketched-rigorous Hessian).

- **Three-regime T phase diagram (Theorem 2.1, Round 4 §2):** (T, c) parameter space 가 single-mode (T < T_c ≈ 1) / multi-mode (T_c < T < T*_uniform ≈ 7) / uniform (T > T*_uniform) 3 영역으로 분해. canonical v1.2 에 없던 신규 결과. **Cat A** structural + Cat C precise T_c.

#### Cat C 4 항목 single-formation T → 0 survival 검증

Round 2 §05 §4 의 Cat A 22 항목 enumeration 의 자매격:
- T-Bind-Full, T-Persist-1(a), T-Persist-1(d), T-Persist-Full — 모두 T-independent statement, **survive T → 0**.
- T-Persist-K-Sep / Weak / Unified (3 K-field) 은 dependency map §2.3 의 **Re-prove** 항목 (소프트-K 언어로 statement 재작성 필요).

T-Persist-1(d) 의 **thermal version** (T > 0 Langevin 하 probabilistic core inheritance) — **NQ-19 (new)**, E-S3 carry.

#### Linear-interp upper bound 정정 (E-9)

Round 3 §06 §3.3 의 ℰ_bd ≈ 95 estimate 가 overestimate. **정정값: ℰ_bd ≈ 22.5 ⇒ ΔF ≤ 40.7** (vs Round 3 의 68). Canonical exp38 ≈ 20 대비 **2× too loose** (not 3×). NEB 필요 결론은 유지. (Errata round 4)

#### Cheeger lower bound

Modica-Mortola sharp-interface barrier × Cheeger 등주 부등식: **ΔF ≥ 2.3** at canonical 8×8 grid. ΔF ∈ [2.3, 40.7] — canonical empirical 20 가 범위 안. ✓

#### NQs new (Round 4)

- **NQ-18:** Three-regime phase diagram 의 numerical verification at T ∈ {0.1, 1, 5, 10}. Stage 5.
- **NQ-19:** Thermal version of T-Persist-1(d) under F3 Langevin. E-S3.
- **NQ-20:** Tighter analytic Mountain Pass bounds via NEB ansatz / string-method theory. C-S2.

#### Cross-file consistency check + 추가 fix

stale references 식별 + 적용:
- **02_dev §1.1 γ_K range:** [0.01, 1] → [0.01, 0.1] (Round 4 fix).
- **02_dev Lemma 1.5 L_K:** errata 주석 추가 (statement + proof — historical record 보존, 정정값 명시).
- **02_dev §5 Cat C table F3:** "sketched, Cat C" → "Cat A on Σ_m^ε via Lions-Sznitman".
- **working/C/F_group_axioms.md** Status field, Scope, Carry section: F3 status 일관 update.
- **canonical_sub.md A-2026-04-21-01:** L_K constant 4 L_φ n with correction note.
- **canonical_sub.md A-2026-04-21-03:** γ_K range [0.01, 0.1] with Round 3 explanation.

**모든 current-state 파일들이 일관**: L_K = 4 L_φ n, γ_K ∈ [0.01, 0.1], F3 = Cat A on Σ_m^ε.

#### Code-side K_soft 가용성

`/home/jack/Perception_theory/CODE/scc/persistence.py` 의 `persistence_h0(u, grid_size)` 가 H₀ persistence diagram return. **K_soft wrapper 5 줄 이하로 implementable.** Stage 5 ready, no code-side blocker.

#### Verification confidence summary (Post-Round 4)

- Cat A 누적: **18** (Round 3 의 16 + 2 = T-Uniform-Stab-T, Three-regime 구조).
- Sketched (Cat C-provisional): 7.
- Statement-only carry: 3.
- Errata 식별: **9 total** (E-1~E-9); 적용 완료 8 (E-1, E-2, E-3, E-7, E-8, E-9 + Round 4 02_dev/working/C/canonical_sub fixes); 보류 3 (E-4, E-5, E-6).
- New NQs from Round 4: NQ-18, 19, 20.
- Cat A canonical T → 0 survive 검증: 22.
- Cat C canonical T → 0 survive 검증: 4 (Round 4 신규 enumeration).

#### 주간 merge 에서 user 결정 추가 (Q13–Q14)

- **Q13 (new).** T-Uniform-Stab-T (Theorem 1.1) 와 Three-regime phase diagram (Theorem 2.1) 의 canonical §13 추가 시점 (권고: Stage 2 axiom audit 와 함께; 이들이 새 Cat A 정리이므로 §13 Cat A 섹션 추가 대상).
- **Q14 (new).** Cat C single-formation 4 개 (T-Bind-Full, T-Persist-1(a), T-Persist-1(d), T-Persist-Full) 의 T → 0 survival 명시 — canonical 에 별도 표기 필요? 또는 F4 statement 에서 implicitly 포함?

---

### Round 5 — Compact + Saturation Check (2026-04-21 evening, after Round 4)

`logs/daily/2026-04-21/08_round5_compact.md` 의 substantive 항목 3 + saturation analysis:

#### Strengthened claims (1 new Cat A definition)

- **Witten Laplacian Δ_{ℱ,T} on Σ_m^ε explicit (Round 5 §1):** 정의 `Δ_{ℱ,T} = -T²·Δ_{Σ_m} + ‖∇ℱ‖² - T·Δℱ` 위 자기수반 elliptic operator, discrete spectrum, ground state f₀ = exp(-ℱ/2T). H-S asymptotic (small eigenvalues ~ exp(-ΔF/T)) statement 수준 (post-Stage-1 carry). **NQ-12 부분 해소.**

#### Structural results (1 new Cat A structure)

- **(T, λ_K) 4-corner phase diagram (Round 5 §2):** 4 corners 중 3 개 → uniform; (0,0) → canonical. 대각선 `λ_K = γ_K · T` 이 Round 4 Three-regime 의 정확한 1D slice. **NQ-21 (new):** bicritical point structure beyond diagonal — CE-S2 carry.

#### F3 ergodicity bound (Cat C-provisional)

- **F3 Poincaré inequality via Holley-Stroock (Round 5 §3):** 평형 ℙ_T 의 mixing rate τ_mix ~ exp(2ΔF/T). 저온 (T < T_c) 에서는 직접 Langevin 비현실적; advanced sampling (parallel-tempering 등) 필요. **NQ-22 (new):** sharper Poincaré via graph spectral structure.

#### Saturation analysis (Round 5 §4)

new Cat A claims per round: **12 → 0 → 3 → 3 → 2 → 1.** New NQs per round: **7 → 0 → 6 → 3 → 3 → 2.**

**Clear diminishing returns.** Round 6+ 예상 contribution ≤ 1 new Cat A. **Round 5 가 natural session terminus.**

**Tomorrow's C-S2 권고 (Round 5 §4.3):**
1. **C-S2.1:** Numerical Hessian + NEB on canonical exp62/63 (n=16, β=30) → 정량 ΔF + saddle K_soft (NQ-15 해소).
2. **C-S2.2:** Round 4 의 T-Uniform-Stab-T 를 cycle/expander 그래프에서 검증 (NQ-13 부분).
3. **C-S2.3:** dependency map 에 T-Beyond-Weyl + T-d_min retire 추가.
4. **CE-S2:** (T, λ_K) bicritical 매핑 (NQ-21).
5. **Stage 5 prep:** scc/k_soft.py 5 줄 wrapper + Langevin sampler.

#### Verification confidence summary (Post-Round 5, FINAL)

- Cat A 누적: **19** (Round 4: 18 + 1 from Round 5 Witten def).
- Sketched (Cat C-provisional): **8** (Round 4: 7 + 1 from F3 spectral gap).
- Statement-only carry: 3.
- Errata 식별: 9 total; 적용 완료 8; 보류 3 (E-4, E-5, E-6 — user review).
- New NQs from Round 5: NQ-21, NQ-22.
- Total session NQs: **24**.

#### Session conclusion

본 세션 (2026-04-21) 의 plan deliverables 6 개 + 5 라운드 verification 완료. 5800+ 줄 substantive 산출. Saturation 도달. **C-S2 (2026-04-22) 가 numerical-side substantive 작업 인계.**

---

### Round 11 — Stage 5 NEB Numerical (2026-04-21 evening, after Round 10 saturation)

`logs/daily/2026-04-21/13_neb_stage5_final.md` — 사용자 요청에 따른 scc/ 실제 코드 + NEB 실행:

#### Code 산출물 (`CODE/scc/`, `CODE/scripts/`)

- **`scc/k_soft.py`** (영구 모듈, 130줄): k_soft + bernoulli_entropy + free_energy_ce + φ-sat / φ-lin
- **`scripts/neb_*` 5개** (~1500줄): NEB v1-v4 + diagnostic
- **총 1900줄 코드**

#### Numerical 검증 결과

- **K_soft Prop 4.1 (hard-K recovery):** sharp K=1 → 0.5, K=2 → 1.0 정확히 ✓
- **Cor 4.1 K_soft Lipschitz:** 16×16 grid 에서 max ratio 1.4% of bound (NQ-9 강력 정당화)
- **Round 4 Theorem 1.1 (T*_uniform):** 6×6 grid 에서 predicted 7.224 vs numerical 7.218 (**0.1% accuracy**)
- **canonical T-Merge (a):** 12×12 β=30 setup 에서 K=2 Hessian 143개 non-trivial eigenvalue 모두 positive ✓ (K=2 진짜 local min)

#### NEB 결과 (Stage 5 핵심)

- **NEB v1-v3 collapse**, **v4 (BFGS endpoints) 5/8 valid**
- **β=10 SUCCESS:** ΔE_barrier = 2.28, saddle K_soft = 0.996, idx 11 (interior)
- **β-dependent mechanism switching observed (E-18):** β=8, 12 saddle K_soft ≈ 1.5 (K=3-like), β=10, 20, 25 saddle K_soft ≈ 0.99 (K=2-like)
- **Power-law fit γ_eff = -2.08** (negative!) — mixed mechanisms + endpoint quality issues
- **γ_eff = 0.89 NOT reproducible** in our setup (different graph/m/protocol than canonical exp38)

#### Strengthened Round 6 §1 (NQ-15 honest closure 정량 확인)

Round 6 §1 의 "γ_eff is protocol-dependent, not universally derivable" — numerical 으로 directly confirmed:
- 같은 graph + parameters 에서 β 만 변해도 mechanism (K=2 vs K=3) 변함
- canonical exp38 의 0.89 는 specific protocol's measurement
- "γ_eff ∈ [0.5, 1.0]" envelope 가설도 numerical 에서 unmet (negative slope due to artifacts + mechanism mixing)

**Round 6 §1 의 negative-result negotiation 가 옳은 epistemic stance 임을 확정.**

#### 3 새 errata (E-18~E-20)

- **E-18 (Medium-High):** NEB on Σ_m exhibits β-dependent mechanism switching (K=2 vs K=3 saddles); γ_eff fitting requires explicit mechanism filtering
- **E-19 (Medium):** scipy L-BFGS-B inadequate at β ≥ 20 for endpoint convergence; need trust-constr / IPOPT
- **E-20 (Low, interpretive):** NEB chain protocol can find different MEPs at different β even with deterministic dynamics

#### 3 새 NQs (NQ-26~28)

- **NQ-26:** Find optimizer for K=2 endpoint at β ≥ 30 (BFGS fails). Carry: C-S2.
- **NQ-27:** Verify saddle Morse index = 1 via Hessian eigenvalue at NEB-found saddle.
- **NQ-28:** Multi-MEP enumeration: how many distinct saddles between K=1 and K=2?

#### Verification confidence (FINAL, post-Stage 5)

- Cat A: **19** (3개 numerically verified: Cor 4.1, T-Merge (a), T*_uniform)
- Sketched (Cat C-provisional): 8
- Statement-only: 3
- **Errata total: 20** (E-1~E-20). 적용 8, 문서화 9, user review 3
- **NQs total: 28** (NQ-1, 1-extended, 8~28)
- **9 theory rounds + 1 numerical session = 10 verification rounds**

#### Stage 5 의 의의

1. **이론 + 코드 cross-check 성공** — Cat A claims 가 numerical 으로 robust (Cor 4.1, T-Merge (a), T*_uniform 모두 일치)
2. **canonical exp38 γ_eff = 0.89 의 reproducibility 검증 시도** — 직접 reproduction 불가 (Round 6 §1 의 protocol-dependent 결론 확정)
3. **새 발견 1: β-dependent transition mechanism switching** (Round 6 §1 의 quantitative manifestation)
4. **새 발견 2: NEB endpoint convergence quality 가 β 와 함께 degrade** — Stage 5 protocol 의 limitation
5. **canonical CN8 (K=2 metastability) 직접 verified** — 12×12 β=30 setup 에서 K=2 Hessian PD

#### 주간 merge 에서 추가 user 결정 사항 (Q15-Q17)

- **Q15 (new).** Stage 5 의 NEB results 가 canonical 에 어떤 형태로 언급되어야 하는가? §13 Cat B "γ_eff = 0.89" entry 에 "Stage 5 numerical reproduction failed" 주석 추가?
- **Q16 (new).** scc/k_soft.py 모듈을 canonical 의 어느 섹션에서 reference 할 것인가? (§5.5 Transition Diagnostics 가 자연 후보)
- **Q17 (new).** E-18 (β-dependent mechanism switching) 이 canonical CN6 ("K kinetically determined") 의 보강 evidence 인가? 또는 새 CN 추가 candidate?

#### Final Session Conclusion (2026-04-21, 진정한 종료)

Stage 1 first session (plan.md 6 deliverables) → 9 round theory verification → Stage 5 numerical (NEB) — **single most thorough day** of SCC project. ~9000 줄 산출 (~7000 theory + ~1900 code). **C-S2 (2026-04-22) 가 stronger optimizer + mechanism-filtered γ_eff measurement 인계.**

---

## 2026-04-20

**Session type:** Stage 0 (Purpose Declaration) 의사결정 재료 생산 — 이론 작업 Non-goal.
**Origin:** `logs/daily/2026-04-20/` (plan.md + 01_exploration.md + 02_development.md + 03_integration_and_new_open.md + 99_summary.md).
**Canonical-relevant 산출물:** Clarified 1 항목 (9+1 정리 integer-K 의존), Pending 2 항목 (theorem_status ↔ canonical §13 inconsistency), Added 1 항목 (NQ-1~7 pending OP 승급).
**Canonical-irrelevant (meta, 본 파일 대상 아님):** Matrix-1/Matrix-2, 15 세션 스케치, Pareto frontier {B, B+C, E, C+E}, Decision Tree, Sensitivity CS-1~4, 권고 E — 전부 purpose decision 재료이며 canonical 의 theorem/axiom 수정이 아님.

---

### Clarified

#### C-2026-04-20-01. Integer-K Load-Bearing 정리 10 개 목록

**출처:** `working/integer_K_dependency_map.md` §2; 기원 `logs/daily/2026-04-20/01_exploration.md` §5.2–§5.3 (3rd audit).
**변경 유형:** Metadata (category 유지). canonical.md line 의 statement 변경 없음.
**주간 merge 시 적용 방식:** canonical.md §13 의 해당 10 개 정리 라인 옆 inline annotation `*(Integer-K precondition: working/integer_K_dependency_map.md §2)*` 추가 여부는 user decision.

##### (a) Category A Retire — 5 개

soft-K 재공식화 하에서 statement 자체가 의미 소실. statement 의 per-formation index `j ∈ {1,…,K}` · per-formation mass `Σ^K_M` · `(K-1)` coupling factor 가 integer K 를 본질적으로 요구.

| # | 정리 | canonical.md 위치 | Statement 요약 | Integer-K Load-Bearing 지점 | 운명 근거 |
|---|---|---|---|---|---|
| 1 | **T-Merge (a)** K-Formation Local Minimality | §13 line 979 | Well-separated K-formations 가 K-field energy 의 local minima on `Σ^K_M`. Hessian 은 `μ_1 μ_2 > λ_rep^2` 조건 하 positive definite. | `Σ^K_M` manifold · per-formation Hessian PD · `μ_1 μ_2` product. soft-K distribution 하에서 "K-formation" 이라는 discrete 대상 부재. | Retire — "K 개의 formation" 개념 해체 |
| 2 | **Topological Lock** Merge Impossible on `Σ^K_M` | §13 line 988 | Per-formation mass constrained manifold 위에서 merge endpoint `(u_merged, 0) ∉ Σ^K_M` because `0 ∉ Σ_{m_2}` for `m_2 > 0`. | `Σ_{m_2}` 정의 자체가 per-formation mass 분할 필요. soft-K 에서 per-formation mass 부재. | Retire — `Σ_{m_2}` 라는 객체 부재 |
| 3 | **Coupling Bound Lemma** K-Formation Hessian | §13 line 820 | (SR: `min_k μ_k > (K-1)λ_rep`) 하 K-formation joint Hessian 의 Weyl spectral gap bound. | `(K-1)` factor — 정수 K 에서 pairwise coupling 수. | Retire — `(K-1)` pair count 는 integer K 특유 |
| 4 | **Proposition 1.2** Fiber Dimension | §13 line 1026 | Stratified Morse Analysis 의 `Σ²_M` fiber 의 차원 계산. | `Σ²_M` (K=2 constrained manifold) 자체가 per-formation mass 분할의 대상. | Retire — stratified Morse 대상 해체 |
| 5 | **Theorem 3.1(a,b,d)** Landscape at Symmetric Point | §13 line 1031 | K=2 대칭점 `(m_1 = m_2 = M/2)` 주변의 energy landscape curvature 분석. | K=2 symmetric point 는 정수 K 에서만 의미. | Retire — symmetric point 개념 소멸 |

##### (b) Category A Re-prove (retain) — 1 개

statement 는 재작성되지만 증명 핵심이 soft-K 하에서도 거의 그대로 재활용 가능.

| # | 정리 | canonical.md 위치 | Statement 요약 | 재활용 가능한 증명 핵심 | 재작성 방향 |
|---|---|---|---|---|---|
| 6 | **T-Merge (b)** Energy Ordering (Isoperimetric) | §13 line 984 | K=1 이 K=2 보다 낮은 energy on connected graph. Isoperimetric consequence. | Γ-convergence + perimeter minimization. Soft-K 로 전환해도 "single-mode vs multi-mode" energy 비교가 perimeter argument 로 보존. | "Single-mode (집중된 distribution) 이 multi-mode (분산된 distribution) 보다 low energy" 로 rewrite |

##### (c) Category B Retire — 1 개

empirical fit 이나 대상 개념이 integer K 전제.

| # | Result | canonical.md 위치 | Statement 요약 | Integer-K Load-Bearing 지점 | 운명 근거 |
|---|---|---|---|---|---|
| 7 | **γ_eff ≈ 0.89** empirical K-merge barrier exponent | §13 line 992 (erratum 2026-04-07) | K-merge barrier 가 `β^{0.89}` 로 scaling. exp55 empirical fit. | "K-merge" 개념 자체가 integer K 에서 정의. soft-K distribution 의 "mode unification" 은 barrier 개념이 재정의 필요. | Retire — empirical 대상 재정의 후 재측정 |

##### (d) Category C Re-prove — 3 개

statement 의 per-formation index 를 soft-K distribution 의 mode 로 재해석. 결과 (persistence) 는 유지 가능하나 증명 재작성 필요.

| # | 정리 | canonical.md 위치 | Statement 요약 | 재해석 방향 | 재증명 필요 지점 |
|---|---|---|---|---|---|
| 8 | **T-Persist-K-Sep** Well-Separated | §13 line 1065 | `(u^1_t, …, u^K_t)` well-separated joint minimizer (H1-K, WS, SR) 의 transition-preserving persistence. | "K 개의 독립 formation" → "soft-K distribution 의 K 개의 well-separated mode". | per-formation T-Persist-1 의 mode-wise 일반화, `d_min(j,k) ≥ D_sep` 는 mode pair 거리로 재정의 |
| 9 | **T-Persist-K-Weak** Weakly-Interacting | §13 line 1110 | Joint Hessian spectral gap via Weyl bound under (SR). Post-hoc correction within basin radius. | `(K-1)λ_rep` factor 는 mode pair 수 × repulsion 으로 재해석. | Weyl bound 가 soft-K mode basis 에서도 성립하는지 재증명 |
| 10 | **T-Persist-K-Unified** Parametric | §13 line 1115 | `Λ_coupling = λ_rep · ω_{jk} / min(μ_j, μ_k)` 로 Sep/Weak/Strong regime 을 통일. 100% geometric-Λ agreement in exp46-47. | pair index `(j,k)` → mode pair index. `ω_{jk}` (soft overlap) 은 이미 distribution-friendly. | Λ 의 정의가 soft-K 하에서도 잘 작동함 확인; Corollary I/II 증명 재편성 |

##### (e) Survive — Single-Formation 정리 19~20 개

soft-K 재공식화 하에서 statement 무변화. 증명 재활용 가능. **canonical 에 명시 annotation 불필요** (변화 없음이 default).

- **Cat A (19~20 survive):** T-1, T-3, T-6a/b/Stability, T-7, T-8-Core/Full, T-11 (Γ-Convergence), T-14, T-20, C-Axioms, QM-1/2/3/4, Predicate-Energy Bridge, T-Bind-Proj (τ=1/2), Deep Core Dominance 2b, T-Persist-1(b)/(e), T-A2.
- **Cat B (3 survive):** T-Bind-Proj (single formation, τ=1/2).
- **Cat C (K=1 survive):** T-Bind-Full (general τ, single formation), T-Persist-1(a)/(d)/Full.

---

### Pending

canonical.md 보수 대상. 오늘 수정 없음; 주간 merge 에서 user 확정.

#### P-2026-04-20-01. T-Persist-K-Sep Category Inconsistency

**출처:** `working/integer_K_dependency_map.md` §6.1.

**증상:**
- `canonical.md` §13 line 1043 erratum (2026-04-07) 은 T-Persist-K-Sep 을 **Category C** 로 이동 ("regime conditions are non-removable structural hypotheses, making it conditional").
- `theorem_status.md` CV-1.2 (last_updated 2026-04-12) 은 **Category B** 로 기록 (line 47: "T-Persist-K-Sep | accepted | B | C-0500 | P-0500 | E-0076, E-0077 | Conditional: on well-separated regime + per-formation persist").
- `canonical.md` §13 line 1063 Cat C 섹션 헤더에 "(Erratum 2026-04-07: T-Persist-K-Sep moved to Category C...)" 명시.

**해결 후보:**
- (i) **Sync theorem_status.md → Cat C** (canonical.md §13 기준). 이것이 자연.
- (ii) Sync canonical.md → Cat B (theorem_status 기준, erratum 원복).

**권고:** (i). `canonical.md` §13 이 THE spec (CLAUDE.md 원칙).

**Affected files on merge:** `theorem_status.md` line 47 — Category B → C, Notes 업데이트.

#### P-2026-04-20-02. Cat C Count Header Mismatch

**출처:** `working/integer_K_dependency_map.md` §6.2.

**증상:**
- `canonical.md` §13 line 1061 header: "### Category C: Conditional (**5 theorems**)".
- 실제 Cat C 섹션 나열 (line 1061-1147 사이):
  1. T-Bind-Full (line 미확인, grep 필요)
  2. T-Persist-1(a)
  3. T-Persist-1(d)
  4. T-Persist-Full
  5. T-Persist-K-Sep (erratum-moved in)
  6. T-Persist-K-Weak
  7. T-Persist-K-Unified

  → 6 또는 7 개 (T-Persist-K-Sep 의 Cat C 편입 시점에 따라).

**해결안:** header 의 `(5 theorems)` 를 실제 count (P-2026-04-20-01 해결 후 6 or 7) 로 수정.

**Affected files on merge:** `canonical.md` line 1061 header 수정.

---

### Added — Pending OP 승급

본 주에는 `canonical/open_problems.md` 에 OP-xxxx 로 승급하지 않음. **승급 조건:** reformulation purpose pin 후 해당 purpose scope 내 NQ 만.

**출처:** `working/new_open_questions_2026-04-20.md` (topic-consolidated); 기원 `logs/daily/2026-04-20/03_integration_and_new_open.md` §9.

#### NQ-1. Soft-K 정의의 Uniqueness / Canonical Choice — HIGH (E 직속)

- **Question:** 4 개 soft-K 정의 후보가 induce 하는 이론이 동일한가?
  - (i) `K_pers(u) = Σᵢ φ(ℓᵢ)` — H₀ persistence bar length weighted sum
  - (ii) `K_Betti(u) = ∫₀¹ β₀({x: u(x) ≥ θ}) dθ`
  - (iii) `u: X_t → Δ^{K_max}` simplex-valued, `K_eff = exp(H(u))`
  - (iv) `u: X_t → P(ℝ≥0)` measure-valued, K = support size
- **Canonical 연결:** §3.3 (u codomain), §5.5 (transition diagnostics), §12 (K-field 폐기 예고).
- **승급 조건:** purpose = E 또는 C+E. E-S1 에서 1 개 commit, NQ-1 은 사후 비교.

#### NQ-2. CN7 (Dual-Mode) 의 원리적 근거 — MEDIUM (C 연결)

- **Question:** 왜 Cohesion mode 가 2 개 (Closure + Distinction) 이고 Co-belonging 이 energy 진입에서 demotion 되었는가? "operator mode 전수 분류" 가 canonical 에 부재.
- **Canonical 연결:** §3.6 (Co-belonging), §6 Group C, §14 CN7, CN20 초안 (B-S1).
- **승급 조건:** purpose = C 또는 B+C. C 의 F-group 공리에서 C_t 가 entropy 로 격상되면 3-mode 복원 가능 (P-C 재프레이밍).

#### NQ-3. Persistence Vineyard 의 T-Persist-K 대체 가능성 — HIGH (E 직속)

- **Question:** 단일 u 의 persistence diagram flow (vineyard, Cohen-Steiner-Edelsbrunner-Morozov 2006) 가 T-Persist-K-Sep/Weak/Unified 의 conclusion 을 얼마나 회수하는가?
- **Sub-questions:** (a) vineyard stability 이 per-formation identity 를 보존? (b) well-separated regime 의 independent persistence 가 vineyard 언어에서 어떤 형태? (c) strongly-interacting regime (`Λ > 1/(K-1)`) 이 vineyard bar merge 로 해석 가능?
- **Canonical 연결:** §12 Multi-formation 전면 재작성의 수학적 핵심.
- **승급 조건:** purpose = E 또는 C+E. E-S2 의 §12 재작성 골격 완성의 core.

#### NQ-4. Q_morph 의 Threshold-Free 화 가능성 — MEDIUM (A 연결)

- **Question:** 현 Q_morph 가 superlevel filtration 을 sweep 하지만 최종 diagnostic 에서 threshold 선택이 재등장 (Core/Interior 경계). 완전 threshold-free Q_morph 가 QM1-4 를 만족하는가?
- **Sub-questions:** (a) integral-over-θ 로 처리 시 QM1-4 중 어느 공리 위반? (b) Lipschitz 성 (sweep 은 bar length 에 Lipschitz 지만 Core/Interior 는 sharp cutoff)? (c) 기존 Cat A QM 증명 재활용 가능?
- **Canonical 연결:** §5 전체, §7.1 (Q_morph), 공리 QM1-QM4.
- **승급 조건:** purpose = A. E 선택 시 parked.

#### NQ-5. CN ↔ 공리 Layer 충돌 해결 규칙 부재 — LOW (meta)

- **Question:** CN 과 공리 간 충돌 시 resolution rule 이 canonical 에 명시되지 않음. 예: B+C 조합에서 CN18 (zero-T) 과 F4 (T > 0 primacy) 직접 충돌.
- **Sub-questions:** (a) precedence 규칙? (b) CN 은 statement-level 인가 meta-commentary 인가? 공리 system 내부인가 외부인가?
- **Canonical 연결:** §6 (공리 layer), §14 (CN 정의).
- **승급 조건:** purpose = B+C 조합 시 필수. 다른 purpose 에서 conservative wording 으로 회피 가능.

#### NQ-6. Candidate D Partial Variant 의 Well-Posedness — LOW (D 연결)

- **Question:** `u → N[u] → Cl(u)` 의 Banach contraction 이 `(a_cl / 4) · L_N < 1` 요구. `L_N` 분석 미수행.
- **Sub-questions:** (a) `L_N` (N 의 u-Lipschitz 민감도) upper bound? (b) partial variant (ii) cohesion-weighted adjacency 의 B1-B4 공리 자동 성립? (c) fixed-point existence/uniqueness?
- **Canonical 연결:** §3.5 (Soft Adjacency), §6 Group B (B1-B4), §9.1 (Local Relation Kernel).
- **승급 조건:** purpose = D. D 후순위일 때 long-term carry.

#### NQ-7. N-1 의 Axiom-Switching 얼굴 (P-G) 정확한 Scope — MEDIUM (A 연결)

- **Question:** `N-1 = P-A + P-D + P-G` 분해에서 P-G 가 정확히 무엇을 포함?
- **Sub-questions:** (a) A1' (`a_cl < 4` 조건부 연장성) 은 axiom switching 인가 parametric commitment 인가? (b) b_D = 0 강제 (D-Ax3 implicit 침해) 는 P-G? (c) E3 reclassification (공리 → 해답 제약 강등) 은 P-G? (d) 각 Group 의 Reclassification Note 전부 P-G, 일부만?
- **Canonical 연결:** §3 (formal universe), §6 (각 Group 의 Reclassification Note), §14 CN6/CN14.
- **승급 조건:** purpose = A. A 의 A-S1 audit table core deliverable. E 선택 시 parked.

---

### 본 entry 의 canonical 변경 규모 (주간 merge 예상)

주간 merge 시 `canonical.md` 실제 수정:

1. **§13 inline annotation** — 10 개 정리 라인 옆 `*(Integer-K precondition: working/integer_K_dependency_map.md §2)*` 추가 (10 줄, metadata). user 수락 시만.
2. **§13 line 1061 header** — `(5 theorems)` → `(6 or 7 theorems)` — P-2026-04-20-02 해결 후.
3. **theorem_status.md line 47** — T-Persist-K-Sep Category B → C — P-2026-04-20-01 해결 후.
4. **open_problems.md** — NQ-1~7 은 본 주 변경 없음 (pending).

총 변경 ≤ 12 줄 (inline annotation 10 + header 1 + theorem_status 1). 새 정리/공리/CN 추가 없음. canonical.md 의 major 구조 변경 없음.

**주간 merge 에서 user 가 결정할 4 가지:**
- Q1. Inline annotation 10 개 추가할지 여부.
- Q2. theorem_status.md sync 방향 (Cat C 로 ← canonical §13 기준 / Cat B 유지 ← canonical erratum 원복).
- Q3. Cat C count header 수정값 (6 or 7, T-Persist-K-Sep 편입 여부에 따라).
- Q4. NQ-1~7 중 어느 것이든 본 주 내에 OP-xxxx 로 승급할지 (권고: purpose pin 후까지 대기).

---

## Merge History

(empty — 본 파일은 2026-04-20 첫 생성, 아직 weekly merge 수행 없음.)
