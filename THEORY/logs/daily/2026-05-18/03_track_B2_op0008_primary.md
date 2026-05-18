---
type: log/daily/track-report
date: 2026-05-18
track: B2 — PRIMARY (OP-0008 σ_standard MERGE Wigner-projection 2-route framework)
session_label: W8-Day1 Track B2
canonical_version: CV-1.17 (untouched)
status: COMPLETE — broad_survey_B2.md (P1 baseline) 산출
target_metric: OP-0008 attack 초기 input 확보 (Day 1 핵심 metric)
target_metric_status: ✓ 충족 (2-route framework 의 첫 매핑 완료)
---

> [!nav] Linked: [[00_plan]] · [[broad_survey_B2|working/MF/broad_survey_B2.md]] · [[sigma_rich_wigner_derivation]] · [[sigma_inherit_k_jump]]


# 03 — Track B2 PRIMARY Report (W8-Day1, OP-0008)

**Pre-work xref check** (00_plan.md §Track B 의무):

```bash
grep -r "OP-0008|Wigner-projection|MERGE/SPLIT" THEORY/canonical/ THEORY/working/MF/
```

결과: 30+ working file + 4 canonical SEAL 파일 hit. 핵심 ancestor:
- `sigma_rich_wigner_derivation.md §8.2 Conjecture 8.1` — Wigner-projection 의 *Cat A target outline* (mass-rescaling factor μ 의 unknown form).
- `sigma_inherit_k_jump.md §3.3 (c) + §5 (c)` — T-σ-Inherit (c) MERGE σ_standard Cat C 의 정식 표.
- `sigma_rich_phi_proof.md §6.2` — Cat A everywhere proof 의 5-step outline (analytic family / Newton-Puiseux / projection formula).
- `nq242c_explicit_construction.md §6 Step 6` — Wigner-projection numerical anchor target (T²_20 equilateral vs isoceles).

**본 broad_survey_B2.md 의 novel positioning**: 위 ancestor 들의 *Conjecture 8.1* 을 *2-route attack framework* (Route (a) Kato perturbation + Route (b) RMT Wigner-Dyson) 로 분해 + *수렴 분석 framework* + *Gate A/B 분기 condition* 의 *수학적 form* 명시. 기존 file 의 *재정리* 아님 — *방법론적 확장* (broad_survey_B2.md §7.2 명시).

---

## §1. 산출물

| Path | Lines | 목적 |
|---|---|---|
| `THEORY/working/MF/broad_survey_B2.md` | ~330 | 2-route framework + convergence + 3rd route preserved + 5 NOQs |

---

## §2. broad_survey_B2.md 핵심 요약

### §2.1 Mission

OP-0008 σ_standard MERGE Wigner-projection Cat C → Cat B 승급의 *2-route attack framework* 첫 매핑. *증명 시도 없음* — Day 2-4 의 직접 입력.

### §2.2 Route (a) Kato resolvent perturbation

- Setup: cross-block Hessian $H = H_0 + V$, $H_0 = H_{i_1, i_1} \oplus H_{i_2, i_2}$, $\|V\|_\mathrm{op} \leq \lambda_\mathrm{rep} c e^{-c_0 d_\mathrm{inter}}$.
- 도구: Reed-Simon IV §XIII.5 (resolvent expansion for isolated simple eigenvalues).
- Schur-complement reduction → post-merger $\sigma_\mathrm{std}(C_j^s)$ explicit polynomial form (target Cat B).
- 성공 조건: perturbative regime + simple eigenvalues + analytic family.
- 실패 모드: deep merger ($d_\mathrm{inter} \to 0$), Goldstone degeneracy, high symmetry.

### §2.3 Route (b) RMT Wigner-Dyson

- Setup: generic graph ($\mathrm{Aut}(G) = 1$) 에서 $H_\mathrm{post}$ 의 eigenvalue spacing $\sim$ GOE.
- 도구: Wigner-Dyson distribution $P_\mathrm{GOE}(s) = (\pi s / 2) \exp(-\pi s^2 / 4)$, level repulsion $P(s) \to (\pi/2) s$ as $s \to 0$.
- 산출: *distributional* relation (per-instance 가 아님 — coarse-grained ensemble).
- 성공 조건: $\mathrm{Aut}(G) = 1$ + deep merger + qualitative σ-tuple convention.
- 실패 모드: high-symmetry graph (T²_L, $K_n$, etc.), small dimension (n < 20), strong correlation.

### §2.4 두 route 의 수학적 독립성 (prompt body §5 quality 기준 충족)

| 비교 항목 | Route (a) | Route (b) |
|---|---|---|
| 적용 영역 | low coupling ($\|V\| <$ gap) | deep merger ($\|V\| \to O(\lambda_\mathrm{rep})$) |
| 결정성 | deterministic per-instance | distributional ensemble |
| 실패 모드 | deep merger | high symmetry |
| 성공 조건 | $\lambda_\mathrm{rep} e^{-c_0 d_\mathrm{inter}} <$ gap | $\mathrm{Aut}(G) = 1$ |

→ 같은 결과의 두 표현 *아님*. 상보적 attack. **prompt body §5 의 "수학적으로 독립 + 실패 모드 다름 + 조건부 성공 조건 다름" 모두 충족**.

### §2.5 Overlap regime + convergence test

§5.3 의 numerical protocol (Day 3 exp92 입력):
- 8×8 + 12×12 grid.
- $d_\mathrm{inter} \in \{2, 3, 4, 5, 6\}$ sweep.
- Route (a) Kato $O(\varepsilon^2)$ prediction.
- Route (b) RMT Wigner-Dyson cdf.
- Numerical merger ground truth.
- 3-way 비교: $\|\Phi^{(a)} - \Phi^{(b)}\| / \|\sigma^{(\mathrm{num})}\|$ → overlap regime 의 convergence indicator.

### §2.6 Gate A/B 분기 condition

- **Gate A (수렴 성공)**: SC-a (Route (a) closed-form $\Phi^{(a)}$) + SC-b (Route (b) $\Phi^{(b)}$) + SC-c (numerical convergence on 8×8+12×12) 셋 모두 PASS → L-Wigner-Projection-MERGE Cat B 승급 + canonical §13 insert.
- **Gate B (수렴 실패)**: T-σ-Inherit (a, b, d-direction, e) partial canonical promotion 4 entries (audit-only). σ_standard (c, d-σ_standard) 는 **여전히 Cat C** — 명시적 carry-forward (silent resolution 회피).

### §2.7 Route (c) preserved (W9+ staging)

Aut(G) 비-trivial high-symmetry regime 의 group-theoretic 대안. Frobenius character + irrep decomposition. *본 W8 attack 범위 밖* — Route (a)+(b) generic regime 의 Cat A 완성 (W10+) 의 후속 입력.

### §2.8 5 새 open questions (NOQ-B2-1 ~ NOQ-B2-5)

- **NOQ-B2-1**: Schur-complement reduction 의 *boundary condition matching* rigorous form? mass-rescaling $\mu = m_j m_k / (m_j + m_k)$ 가 Schur 에서 자연스러운가?
- **NOQ-B2-2**: RMT distributional Cat B → per-instance Cat B 호환?
- **NOQ-B2-3**: 8×8 그리드의 finite-dim RMT convergence rate?
- **NOQ-B2-4**: $\mathrm{Aut}(G) = 1$ open dense subset 의 graph-class별 측정?
- **NOQ-B2-5**: Route (a) 의 iterated multi-step K-jump 적용 (예: $K=3 \to 2 \to 1$)?

---

## §3. prompt body §4 quality 기준 자가 점검

| 기준 (prompt body §4-5) | 결과 |
|---|---|
| 문제 재진술 (Restatement) | broad_survey_B2.md §2 명시 — Φ_MERGE^{σ_std} 의 deterministic-vs-stochastic 문제로 표면화 |
| 다중 접근 ≥ 3 (Multi-approach) | Route (a) + Route (b) + Route (c) = 3; §6 preserved |
| Primary 선택 + 대안 보존 | Primary = Route (a)+(b) 의 *상보적 결합*; Route (c) 보존 (§6.4 W9+ staging) |
| Primary 심층 전개 | §3 (Route (a) §3.1-§3.6) + §4 (Route (b) §4.1-§4.5) + §5 (수렴 framework) |
| 기존 체계와의 통합 | §7 (canonical / working 위치 + silent-resolution 회피) |
| 새 open question 수집 | §8 NOQ-B2-1 ~ NOQ-B2-5 = 5건 |
| 각 접근 의 (a) 성공 시 결과물 / (b) 실패 모드 / (c) 기존 정리/공리 와의 상호작용 | §3.4-3.6 / §4.3-4.5 / §6.3-6.4 모두 명시 |
| 모든 가정 명시 (수학적 엄밀성 §7 #1) | Route (a)/(b)/(c) 각각 success condition 명시 |
| Cat 자기 분류 (§7 #2) | 본 file 은 broad survey — *증명 산출 아님*; Cat 분류 부착 부재 (§12 명시) |

---

## §4. Day 2 의 *직접 입력* (00_plan.md §"다음 (Day 2) 입력 준비")

broad_survey_B2.md §9 매핑 표 직접 적용:

| Day 2-3 target | broad_survey_B2.md 입력 |
|---|---|
| `op0008_merge_wigner_perturbation.md` (Day 2 PRIMARY, ~80% 시간) | §3 전체 — Kato expansion explicit form + 5×5 toy analytic |
| `op0008_merge_wigner_rmt.md` (Day 3 PRIMARY) | §4 전체 — Wigner-Dyson + SBM/barbell/small-world generic-graph test |
| `exp92_wigner_projection_robustness.py` (Day 3) | §5.3 의 8-step protocol |
| Day 4 EOD Gate decision | §5.4 SC-a/-b/-c + §5.5 Gate B fallback path |

---

## §5. Anti-pattern 회피 자가 점검

| 회피 항목 | 결과 |
|---|---|
| canonical 직접 수정 | 0 — `working/MF/` only |
| silent OP resolution | 0 — OP-0008 *전체* OPEN 유지; MERGE σ_standard 만 *attack framework* |
| Research OS 재도입 | 0 — single-topic file |
| 외부 framework reductive 환원 | 0 — Reed-Simon IV / Wigner-Dyson 은 *contrastive* 도구 |
| primitive 전도 | 0 — $H$ 는 $\mathcal{E}_K(\mathbf{u})$ 의 2nd variation, u_t primitive 유지 |
| K 이중 취급 | 0 — K = K_act 정수 commit (Commitment 16) |
| 새 framework letter 도입 | 0 — Route (a)/(b)/(c) 는 prompt body §6 의 다중 접근 표기 (예시 §4.2 직접 채택) — 새 *theory* 라벨 아님 |
| V-AFD/R-2/z_t 부활 시도 | 0 — Wigner-projection 의 Cat A target 은 5/15 결정 C 이전부터 W9+ staging; *재포장 아님* |
| Engineering proxy | 0 — Hessian + RMT 는 standard mathematical tool, *engineering proxy 부재* |

---

## §6. 자가 평가 (broad survey quality)

- broad_survey_B2.md = **330+ 줄**, 12 sections + 5 NOQs + hard constraint verification 완료.
- 본 broad survey 가 Day 2-3 의 *substantive 직접 입력* 으로 사용 가능 — §9 명시 매핑 4건.
- prompt body §5 의 "수학적으로 독립 route ≥ 3" 충족 (Route (a) + Route (b) + Route (c)).
- 본 broad survey 의 *substantive deliverable* = (i) 2-route framework 명시 매핑 + (ii) 수렴 condition formal form + (iii) NQ-242c / exp92 protocol 입력 + (iv) Gate A/B 분기 수학적 form + (v) 5 NOQ.

---

## §7. Day 1 핵심 metric 충족 여부

00_plan.md §"Decision gate":

> **OP-0008 attack 초기 input 확보**: broad_survey_B2.md 가 *2-route framework 의 첫 매핑* 을 명시적으로 담음 — Day 2 perturbation thrust 의 *직접 입력* 가능

→ **충족** ✓. broad_survey_B2.md §3 (Route (a)) + §4 (Route (b)) + §5 (수렴 framework) + §9 (Day 2 입력 매핑) 모두 작성됨.

---

*Track B2 종료. PRIMARY 산출 complete. Day 2 perturbation thrust 입력 준비 완료. canonical 0 edits. 새 어휘 0 (Route (a)/(b)/(c) 는 prompt body 채택 표기).*
