> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q2_multi_formation]] · [[MOC_Q4_K_selection]] · [[MOC_Q5_temporal_identity]] · [[MOC_Q6_sigma_inherit]] · [[THEORY_INDEX]]

# MF_atlas.md — Multi-Formation Atlas v0.1 (skeleton)

**Type**: W8 primary deliverable. *v0.1 skeleton, Day 1 of W8* — 12 sections × ~1 paragraph + xref + gap/new candidate. Sections §3-§9 are skeletons only; *살 채우기 (full ~80-120 lines each)* 가 Day 2-5 의 Track A 작업.
**Version**: v0.1 (skeleton, 2026-05-18).
**Promotion target**: v1.0 P5-ready Day 5 EOD (`THEORY/logs/weekly/2026-05-W3/W8_strategic_plan.md §2 G1`).
**Pre-work xref check**: `grep -r "MF_atlas|multi-formation atlas" THEORY/canonical/ THEORY/working/` → 0 hits. 신규 file. 본 Atlas 의 *novel positioning* = canonical 의 ~40-50% multi-formation 형식화 상태를 *설명 가능한 single index* + *gap 발견 강제 룰* 로 정리.
**Canonical version**: CV-1.17 (sealed 2026-05-15).
**Hypothesis tree**: HT-3.8.
**Each section forced rule**: 끝에 *gap 또는 새 후보 1개 이상* 명시 (W8 plan §2 G1).

---

## §1. Multi-formation primitive (D-6a, K-field architecture, Commitment 16)

Multi-formation 의 *primitive 정의* 는 `canonical.md §3.11 D-6a` (Multi-Static σ-tuple, 2026-04-29 CV-1.5.1) + `§11.1 Commitment 14-Multi` (σ-tuple multi-set) + **`§11.1 Commitment 16`** (K-status: $K_\mathrm{field}$ vs $K_\mathrm{act}$ 분리; $K_\mathrm{field}$ = architectural cap / modeling-layer commitment, $K_\mathrm{act}$ = `#PersComp(u_t)` dynamical count). K-field architecture (I9) 는 *computational accelerator* (canonical §3.11 D-ST-2 + `scc/multi.py` ARCHITECTURE NOTE V1-V4) — *foundational* 은 single-field $u_t : X_t \to [0, 1]$ on $\mathcal{F}_M(\mathcal{P})$ + posthoc `K_act = #PersComp`. Multi-formation 의 *primitive 좌표* 는 $\mathbf{K} = (K_\mathrm{field}, K_\mathrm{act})$ pair; 이론적 *대상* 은 *single u_t field* 의 K_act-decomposition (= `#PersComp`) 의 *분포*.

**xref**: `canonical.md §3.11` (D-6a Multi-Static, D-ST-1..3); `§11.1 Commitment 14-Multi + 16`; `canonical.md §14 CN6` (K kinetically determined; K_act emerges); `working/MF/op_0009_pre_a_kfield_chart_validity.md` (V1-V4 chart validity); `working/MF/K_status_commitment.md`.

**Gap / new candidate**: Commitment 16 의 *full decision* (K_field 의 modeling-layer commitment 이 *amend 가능* 한지, 또는 *fixed* 인지) 미해결. W12+ Commitment 16 최종 결정 plan 후보. 본 W8 의 직접 attack 대상 *아님* (anti-goal §5).

---

## §2. Static layer (T-L1-F/M Cat A, T-Persist-K-Sep/Weak/Unified)

Static multi-formation layer 의 Cat A 정리:
- **T-L1-F** (Hard-Bar / Active-Count Bridge under L1-J Regime $(P0)-(P11)$, Cat A conditional, CV-1.5.2 2026-05-02) — first multi-formation canonical Cat A.
- **T-L1-M** (Soft-Count Corollary under $\Phi_\mathrm{res}(\ell_\mathrm{min}, \tau) + \tau < \tau_*^\mathrm{post-R2}$, Cat A conditional, 2026-05-04 W6 D1 EOD).
- **T-Persist-K-Sep** (Cat B, well-separated regime).
- **T-Persist-K-Weak** (Cat C, weakly-interacting regime).
- **T-Persist-K-Unified** (Cat B, parametric Sep/Weak/Strong family).

Static layer ≈ 95% 형식화 완료 (W8 plan §1 시작 상태 입력 감사). T-L1-F/M 은 *bridge*; OP-0005-EQ (T-K-Select-PF Cat B, CV-1.10 Session R) + OP-0005-OBS (T-K-Select-OBS Cat B, CV-1.11 Session Y) 가 K-selection 의 equilibrium / observation 측면 *partial canonical*. **K-selection dynamics (OP-0005-DYN) 은 OPEN — §3 의 입력**.

**xref**: `canonical.md §13 Category A` (T-L1-F, T-L1-M); `theorem_status.md` lines 380-382 (T-Persist-K-Sep/Weak/Unified); `working/MF/kbar_kact_bridge_L1F_synthesis.md` (T-L1-F 13-step chain).

**Gap / new candidate**: T-Persist-K-Weak Cat C → Cat B 승급 (weakly-interacting regime 의 *finer* condition 필요). 본 W8 *non-target* (anti-goal: secured layer secured 만 정밀화 — OP-HMORSE-LOCAL-A; T-Persist-K-Weak 은 W10+).

---

## §3. Equilibrium K-selection (T-K-Select-PF Cat B target) — *Day 2 채움*

T-K-Select-PF (Cat B canonical, CV-1.10 Session R 2026-05-06) — P-F-A1 Package I (Cat A, CV-1.9) 위의 *equilibrium* K-selection: $p_K = \pi_{T_*}(\mathcal{B}_K) = Z_K / Z$, $K^* = \arg\max_K p_K$. Cat A path: explicit $\sigma_M$-null computation in T-PF-A1-AR coordinates + $K_\mathrm{feas}$ per-instance characterization. 본 W8 의 *non-attack* (OP-HMORSE-LOCAL-A 가 secured layer priority).

**Day 2 채움 범위**: ~80-120 줄. (a) T-K-Select-PF 정리 본문 재기술 + Cat A path 의 3-step gap 명시; (b) `working/MF/k_select_pf_equilibrium.md` 와 `working/MF/k_selection_a_free_energy.md` 의 통합 보기; (c) `working/MF/k_select_obs_posterior.md` (T-K-Select-OBS) 와의 *unified view* 후보 (P-K-Select-Unified Cat B SKETCH, Day 2 새 working file `k_select_pf_obs_unified_view.md`).

**xref**: `canonical.md §13` (T-K-Select-PF, T-PF-A1-AR/SDE/GI/PE); `working/MF/k_selection_compatibility_proof.md`.

**Gap / new candidate**: $K^*$ uniqueness — P-F-A1 만으로는 unique $K^*$ 보장 부재 (`canonical.md §13 T-K-Select-PF` non-overclaim). $K^*$ uniqueness 의 *additional hypothesis* 가 무엇인가가 새 후보 — Day 2 attack 의 *side benefit*.

---

## §4. Observed K-selection (T-K-Select-OBS Cat B target) — *Day 2 채움*

T-K-Select-OBS (Cat B canonical, CV-1.11 Session Y 2026-05-06) — observation-conditioned posterior K-selection: $p_K(\mathfrak{O}_t) = Z_K^\mathrm{obs} / Z^\mathrm{obs}$, $K^*(\mathfrak{O}_t) = \arg\min_K F_\mathrm{obs}(K; \mathcal{P}, \mathfrak{O}_t)$. Bayes on Gibbs prior (Package I) with LM1-LM3 likelihood. exp85 ALL PASSED (3/3 scenarios, 12×12 grid). Cat A path: full stereo likelihood $(H_L, H_R)$ canonicalization + temporal extension.

**Day 2 채움 범위**: ~80-120 줄. T-K-Select-OBS vs T-K-Select-PF 의 *복합 framework* — observation 부재 시 prior recovery + observation 충분 시 likelihood dominance. **P-K-Select-Unified Cat B SKETCH** 후보 (Day 2 working `k_select_pf_obs_unified_view.md`).

**xref**: `canonical.md §13 T-K-Select-OBS`; `working/MF/k_select_obs_posterior.md`; `canonical.md §2.4` (stereo likelihood model).

**Gap / new candidate**: temporal extension — $\{K^*(\mathfrak{O}_t)\}_{t \in T}$ 가 *trajectory* (T-Temporal-Identity 와 결합) 로서 *consistent* 한가? 새 working 후보 `working/MF/k_select_obs_temporal_consistency.md` (W10+ staging).

---

## §5. σ-inheritance (T-σ-Inherit 6 parts) — *Day 3 채움*

T-σ-Inherit (working canonical, CV-1.13 advance 의 distinctive target) — 6 parts:
- (a) CONT centroid + orientation: Cat B candidate (working).
- (b) MERGE centroid + orientation: Cat B candidate (parallel-axis theorem, mass conservation H3).
- (c) MERGE σ_standard: **Cat C** (Wigner-projection Conjecture 8.1, W9+ → **W8 Day 2-4 OP-0008 PRIMARY attack target**).
- (d-direction) SPLIT direction: Cat B candidate (Morse genericity, lowest-eigenvalue mode).
- (d-σ_standard) SPLIT σ_standard: **Cat C** (post-split re-optimization, W9+).
- (e) Birth + death: no inheritance claim.

**Day 3 채움 범위**: ~200 줄 (Atlas 의 *가장 두꺼운 섹션*). 각 part 의 정리 본문 재기술 + 현 Cat 상태 + Day 2-4 의 *공격 결과* 반영.

**xref**: `working/MF/sigma_inherit_k_jump.md`; `working/MF/sigma_rich_wigner_derivation.md §8`; `working/MF/broad_survey_B2.md` (본 W8 Day 1 산출 — 2-route framework); `canonical.md §15 OP-0008`.

**Gap / new candidate**: (c) MERGE σ_standard 의 Cat C → Cat B 승급의 Day 4 EOD gate (W8 plan §2 G3). Gate B fallback (T-σ-Inherit 4 parts partial canonical promotion) 의 *분류 명시* — *어느 4 parts* 가 partial canonical 진입 후보인가 (a, b, d-dir, e? 또는 다른?). 새 후보: `working/MF/t_sigma_inherit_partial_promotion_audit.md` (Day 4 EOD 작성).

---

## §6. Temporal composition (T-Temporal-Identity Cat A + T-CC-StableK-Kernel Cat B) — *Day 4 채움*

T-Temporal-Identity (Cat A, CV-1.13 SEALED 2026-05-10) — all 4 parts (a, b, c, d) Cat A. T-CC-StableK-Kernel (Cat B canonical, CV-1.17 SEALED 2026-05-15) — kernel-composed compositional consistency under stable-K + margin. T-ACT-KERNEL-COMP→REL Cat B conditional (CV-1.15) lift activation by T-CC-StableK-Kernel.

**Day 4 채움 범위**: ~80-120 줄. (a) temporal composition 의 *full 3-step* (T-Temporal-Identity + T-CC-StableK-Kernel + T-ACT-KERNEL-COMP→REL) chain의 *통합 그림*; (b) H-COMP row (`hypothesis_tree.md` HT-3.8 PARTIALLY CLOSED) 의 *full closure* 의 *조건*.

**xref**: `canonical.md §13` (T-Temporal-Identity, T-CC-StableK-Kernel, T-ACT-KERNEL-COMP→REL); `working/CV114_TEMPORAL_COMPOSITION/05_promotion_draft.md`; `working/MF/temporal_identity_sharp_form_2026-05-07.md`.

**Gap / new candidate**: T-ACT-KERNEL-COMP→REL Cat B conditional 의 *unconditional* lift — 현재 (GK) 조건 (T-CC-StableK-Kernel promotion 필요) 가 *full unconditional* 인지 audit. Day 4 작성 직전 verification.

---

## §7. OMS-2.0 Appendix lift — *Day 4 채움*

OMS-2.0 (Observer Moduli Space, Accepted — Static + Full Temporal Conditional on OP-OMS-034, 2026-05-08) — `canonical.md §Appendix OMS` (§2404-2548). Static face logically self-contained (R1-R5, L1-L2, ED1-ED2, C1.1-C1.5, NV-A/B, reduced SB5/SB7/SB8/SN3 at $\lambda_\mathrm{tr} = 0$). 20+ theorem items.

**Day 4 채움 범위**: ~80-120 줄. (a) OMS-2.0 의 *static face* 의 Atlas 위치 (multi-formation 의 *모듈리 공간*); (b) Full Temporal 의 conditional (OP-OMS-034) — W9+ staging; (c) `theorem_status.md` 의 *formal row addition pending* (W8 plan §1 시작 상태).

**xref**: `canonical.md §Appendix OMS`; `working/observer_moduli/` (30+ working files); `theorem_status.md` OMS row pending.

**Gap / new candidate**: OMS-2.0 Appendix 의 *theorem_status.md formal row addition* — W7+ pending. Day 4 채움 시 그 *row 작성 제안* (canonical 직접 수정 아님 — *제안* 만).

---

## §8. Coupling regimes + Λ_coupling 파라미터화 — *Day 5 채움*

$\Lambda_\mathrm{coupling} = \max_{j \neq k} \lambda_\mathrm{rep} \omega_{jk} / \min(\mu_j, \mu_k)$ — *Unified regime parametrization* (`canonical.md §1076`, v2.1). 3 regime thresholds: $\Lambda < 0.01$ (well-separated), $0.01 \leq \Lambda < 1/(K-1)$ (weakly-interacting), $\Lambda \geq 1/(K-1)$ (strongly-interacting). 100% agreement with geometric classification (69 configs, exp46-47). Implementation: `scc/multi.py:coupling_strength()`. *P-Unified-1 FALSIFIED* (exp49-50; persist degradation NOT monotone in $\Lambda$). Λ reclassified *structural classifier, not dynamical predictor*. *MK-1..MK-4* kinetic predictions: nucleation spectral mode, coarsening $\alpha < 1/2$, barrier scaling $\beta^{0.89}$, enhanced metastability from closure.

**Day 5 채움 범위**: ~80-120 줄. (a) Λ_coupling 의 *structural* role 명시; (b) MK-1..MK-4 의 *Atlas 위치* (Track B3 의 nucleation/metastability/coarsening 과 결합); (c) exp94 phase diagram 3-regime grid (Day 5 deliverable) 의 *visual map*.

**xref**: `canonical.md §1076 Unified regime parametrization`; `scc/multi.py:coupling_strength`; W8 plan §"G4 Numerical Probes" exp94.

**Gap / new candidate**: P-Unified-1 falsification 이후의 *Lambda 의 새 의미* — Day 1 Track C 의 `subthreshold_demo_check` 가 Lambda 를 *structural classifier* 로 활용. 본 W8 의 *novel positioning*: Lambda 는 *operational* (sub-threshold demo 의 정의) 만 — dynamical predictor 아님.

---

## §9. Dynamics gap map (OP-0005-DYN/OP-0008/OP-0012-SINK/OP-0021 unlock chain) — *Day 5 채움*

3 unlock chains (W8 plan §1.W8 시작 시 입력 분석):
- **Chain 1 (primary)**: OP-HMORSE-LOCAL-A → Package II EK Cat B → Q3 closure. W8 secured layer focus.
- **Chain 2 (W9+ chain)**: OP-0008-MERGE/SPLIT → T-σ-Inherit full → Q6 completion. W8 distinctive layer focus.
- **Chain 3 (long chain)**: OP-0021 → Package II + Q4-DYN unified rate. W9+.

OP-0012-SINK (L-Sinkhorn-Plan-Composition-Bound Cat C target, Day 4 working) — Q5 의 *sinkhorn composition* gap. 별도 chain.

**Day 5 채움 범위**: ~80-120 줄. (a) 4 open problem 의 *graph 형 unlock chain* 시각화; (b) 각 chain 의 *current edge* 위치 (CV-1.18 SEAL 후 / Day 4 EOD 후); (c) W9-W11 의 *공통* 진입 점 (`W8_strategic_plan.md §11 W9+ Preview` 의 3 Path 모두 활용).

**xref**: `canonical.md §15 OP-list`; `theorem_status.md` OP Quick Index; `hypothesis_tree.md` HT-3.8 H-MORSE / H-COMP / H-EK row.

**Gap / new candidate**: Chain 2 의 Day 4 EOD 의 *Gate A* (수렴 시 Cat B 승급) 또는 *Gate B* (4 parts partial promotion) — Atlas §9 가 EOD 후 갱신될 *Atlas v0.1 → v0.2* 의 *trigger*.

---

## §10. Open problems quick index (multi-formation 관련만 추출)

Active high-priority OPs (multi-formation 관련):
- **OP-0005**: K-Selection. -EQ partially resolved (T-K-Select-PF Cat B). -OBS partially resolved (T-K-Select-OBS Cat B). **-DYN OPEN** (Package II / W9+).
- **OP-0008**: σ^A K-jump non-determinism (now SPLIT into CONT/MERGE/SPLIT/DIST). MERGE σ_standard Cat C → Cat B attack 가 **W8 Day 2-4 primary**.
- **OP-0009**: Multi-Formation Ontological Foundations. 8 sub-items, 1 RESOLVED (K), 7 PARTIALLY RESOLVED.
- **OP-0012**: K-jump → -CC (resolved CV-1.13/CV-1.15), -Kjump (Cat C), -Markov (deferred), -SINK (canonical §8.5 redefinition deferred CV-1.16+).
- **OP-0021**: Stochastic Dynamics + $T_*$ — UNDER INVESTIGATION. dual-naming inconsistency carried to CV-1.17+.
- **OP-HMORSE-LOCAL-A**: L-HMORSE-LOCAL Cat B → Cat A — **W8 secured layer primary, Day 4 SEAL prep**.
- **OP-HMORSE-SADDLE**: saddle-point Hessian regularity — independent of LOCAL-A.
- **OP-HMORSE-SBM**: numerical robustness extension to SBM / barbell / small-world.

**xref**: `theorem_status.md §"OP Quick Index"`; `canonical.md §15`.

**Gap / new candidate**: OP-0009 sub-items 2-7 (F bridge, λ_rep, Architecture, C_t, Pre-objective, Empirical) PARTIAL → READY upgrades via OAT-2..7 — W9+ staging.

---

## §11. Code mapping (scc 함수별 정리/lemma 매핑) — *Day 2-5 누적*

핵심 매핑 (W8 plan §8 의 표 직접 채택):
- `find_k_formations()` (`scc/multi.py:40`) → K-field optimizer; *V1-V4 chart validity* assumption; T-Persist-K-Sep input.
- `transport_k_formations(phase2_mode=...)` (`scc/multi.py:281`) → multi-step temporal composition; T-Temporal-Identity + T-CC-StableK-Kernel input.
- `coupling_strength()` (`scc/multi.py:592`) → Λ_coupling 의 implementation; §8 의 직접 anchor.
- `classify_regime(method="geometric")` (`scc/multi.py:506`) → 3-regime classification; §8 의 implementation anchor.
- `compute_sigma_rich()` (`scc/sigma_rich.py`) → σ_rich tuple (centroid + orientation + Wigner-data); §5 의 input.
- `persist_transport()` (`scc/transport.py`) → Persist chaining; §6 + exp93.
- `k_soft()` (`scc/k_soft.py`, φ-sat default) → soft K count; §2 의 T-L1-M input.
- `persistence_h0()` (`scc/persistence.py`) → H₀ persistence bar; T-L1-F input.
- `EnergyComputer.hessian_finite_diff()` (`scc/energy.py`) → numerical Hessian; §5 의 Wigner-projection numerical anchor.
- *Day 1 신규* `experiments/exp90_sanity_canonical_xref.py:canonical_k2_hash + subthreshold_demo_check` → 모든 K=2 결과 의 *operational guard* (`06_track_C_sanity_infra.md` §2).

**Day 2-5 누적 갱신**: 매 day 의 exp9X 결과를 본 §11 에 *추가*.

**xref**: W8 plan §8 *기존 함수 재사용 표*; `06_track_C_sanity_infra.md`.

**Gap / new candidate**: `scc/multi.py:_optimize_k_fields` 의 *V3 violation* (formation separation < eps) 자동 감지 — `subthreshold_demo_check` 의 *V3-status* 추가 후보 (Day 2-5 의 보조 extension).

---

## §12. W8 daily expansion log

| Day | Date | 추가 (Atlas 의 *prepend* 형식) |
|---|---|---|
| Day 1 (Mon) | 2026-05-18 | **v0.1 skeleton** — 본 file (12 sections × ~1 paragraph + xref + gap/new candidate). Track A 결과 보고: `THEORY/logs/daily/2026-05-18/02_track_A_atlas_skeleton.md`. |
| Day 2 (Tue) | 2026-05-19 | §3 + §4 full (~80-120 줄 each). + `k_select_pf_obs_unified_view.md` (P-K-Select-Unified Cat B SKETCH). |
| Day 3 (Wed) | 2026-05-20 | §5 full (가장 두꺼움, ~200 줄). 6 parts of T-σ-Inherit full audit. |
| Day 4 (Thu) | 2026-05-21 | §6 + §7 full. CV-1.18 SEAL (OP-HMORSE-LOCAL-A) + CV-1.19 Gate A/B 결정 반영. |
| Day 5 (Fri) | 2026-05-22 | §8 + §9 full. v1.0 P5-ready. exp94 phase diagram PNG 결합. |

**Atlas version progression**:
- **v0.1** (Day 1): skeleton + each-section gap.
- **v0.2** (Day 4): §6-§7 full + CV-1.18 SEAL 반영 + CV-1.19 Gate 결정 반영.
- **v1.0** (Day 5): full 12 sections + visual deliverable + Code mapping 누적.

---

## §13. Hard constraint verification (W8 anti-goals + prompt body §8)

- [x] canonical 직접 수정 0 — `working/MF/` only.
- [x] silent OP resolution 0 — 모든 OP 의 *현재 상태* 그대로 인용; 해결 주장 부재.
- [x] Research OS 재도입 0 — Atlas 는 *single working file*, no 등록부 형식.
- [x] reductive 환원 0 — Allen-Cahn / OT / RMT 등의 *contrastive* 만 (§5, §8 명시).
- [x] primitive 전도 0 — single $u_t$ field 위의 derivative 만 (§1 명시).
- [x] 4 에너지 항 병합 0.
- [x] closure idempotence 가정 0.
- [x] K 이중 취급 0 — $K_\mathrm{field}$ vs $K_\mathrm{act}$ 분리 명시 (§1).
- [x] zero-temp metastability flag — §3, §4 (Package II 미수립 시 metastability 주장 부재).
- [x] OMC 풀 오케스트레이션 0 — 본 file 은 Claude session 단독 작성.

---

## §14. Status

**Type**: working multi-formation Atlas, v0.1 skeleton.
**Effort to-date**: 1 session (W8-Day1 Track A).
**Promotion target**: v1.0 P5-ready Day 5 EOD.
**Next session**: Day 2 (Tue 2026-05-19) §3 + §4 full.
**Pre-work xref check date**: 2026-05-18 (`grep -r "MF_atlas|multi-formation atlas" THEORY/canonical/ THEORY/working/` → 0 hits, 신규).

---

*MF_atlas.md v0.1 skeleton 종료. 12 sections × ~1 paragraph + xref + gap/new candidate 모두 작성. Day 2-5 의 살 채우기 입력 준비 완료. canonical 0 edits.*
