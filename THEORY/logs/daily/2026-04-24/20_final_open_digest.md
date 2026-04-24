# 20_final_open_digest.md — Definitive Open-Problem Digest (post-G1-formalization)

**Session:** 2026-04-24 (final)
**Origin:** 사용자 요청 "남은 open prob 재정리" (after C3-G1 connection formalization).
**Supersedes:** `06_open_problems_digest.md`, `17_post_C2_open_digest.md`.
**Depends on:** 본 세션 01-19 전체; 특히 `16_C2_closure.md`, `18_G1_results.md`, `19_C3_G1_connection.md`.

---

## §1. 원칙 — 본 digest 는 **definitive 스냅샷**

이전 두 digest (`06_*`, `17_*`) 이후 C2 closure + G1 multi-angle + C3-G1 formalization 이 완료. 본 digest 는:
1. 세션 누적 Cat A/B 명시
2. **Geometric Taxonomy** 적용된 새 cluster 구조
3. 명확한 next-session priority

---

## §2. Session total — 누적 산출

### 2.1 Cat A 신규 (본 세션)

| ID | Statement | 출처 |
|---|---|---|
| σ definition | cohesion signature well-defined (Morse-0) | `02_*` §2 |
| Lemma 1 | Hessian irrep decomposition canonical | `02_*` §3 |
| Lemma 2 (i,ii,iv) | nodal count graph-intrinsic, Aut-equivariant | `02_*` §4 |
| Theorem 3 | σ at uniform $c\mathbf{1}$ on $D_4$ grid closed form | `04_*` §1 |
| Theorem 4 | σ at first-pitchfork minimizer (leading ε) | `04_*` §2 |
| Lemma 3 | Goldstone ↔ ℓ=1 saturation (geometry-conditional) | `04_*` §3 |
| Theorem 2 (i) | disk non-criticality | `16_*` §2 |
| Theorem 2 (ii) | multi-peak attractor existence | `16_*` §2 |
| Theorem 2 (iii) | Lemma 4 quadratic form PD | `11_*` §4 |
| Theorem 2 (iv) | IC-sensitivity scaling | `15_*` §3, `16_*` |
| Theorem 2 (v) | thermodynamic dichotomy (adaptive bounded / random diverging) | `16_*` §2 |
| Theorem 2-G | graph-class generalization (qualitative) | `11a_*` |
| F-1 resolved | pure via T-Merge (b), full via Thm 2 | `16_*` §4 |
| NQ-132 | (C5) threshold trivially 0 | `08_*` §4 |
| NQ-133 | IC sensitivity quantified (via Phase 3C S4) | `15_*` |
| NQ-134 | cl/sep mechanism-level monotone | `16_*` §3 |
| NQ-135 | generalized $\mathcal{F}_*$ dichotomy | `16_*` §5 |
| NQ-136 | Pöschl-Teller shell spectrum exact (1 radial × ∞ angular) | `14_*` §3 |
| NQ-141 | σ ↔ orbital taxonomy R23-verified | `18_*` §4 |
| NQ-144 | $\kappa_{\ell=1}^{D_4} = 6\sqrt{\pi c\alpha/\beta}/L$ exact | `14_*` §1 |
| NQ-146 | angular ℓ ↔ $D_4$ irrep: ℓ mod 4 pattern | `14_*` §2 |
| NQ-155 | thermodynamic limit dichotomy | `16_*` §5 |
| NQ-128 (revised) | Theorem 1 geometry-specific (not Goldstone-universal) | `18_*` §2 |
| NQ-129 (negative) | center-aligned no Goldstone scaling confirmed | `18_*` §2 |
| Theorem 1 (case O) | center-aligned genuine orbital | `18_*` §6 |

→ **Cat A 신규 25**. 

### 2.2 Cat B 신규

| ID | Statement | 출처 |
|---|---|---|
| Theorem 1 (case T_off) | pseudo-Goldstone $O(\exp(-d_*/\xi_0))$ | `02_*` §5, `19_*` §4.2 |
| NQ-137 | Pöschl-Teller vs finite-grid 15-20% discrepancy | `18_*` §3 |

→ **Cat B 2개**.

### 2.3 Cat C 신규 (잠정)

- Lemma 2 (iii) Courant bound (signed-Laplacian frustration 조건부)
- Theorem 1 (case T) — torus exact Goldstone, NQ-131/161 test 대기

### 2.4 Other deliverables
- 3 Sharpened CN (CN15, CN16, CN17)
- 1 Axiom proposal (S1' v1)
- 1 Commitment proposal (Commitment 14)
- 1 N-1 reframe (bug → feature)
- **Geometric Taxonomy Principle** (C3 내부 구조 정식화)

---

## §3. Remaining open problems — **Geometric Taxonomy 적용 분류**

### 3.1 C3-T (torus exact Goldstone) — 2 open

| ID | Statement | Cat | 즉시 가용 |
|---|---|---|---|
| NQ-131 | Torus F=1 Goldstone empirical verification | Cat C | **Yes** — new torus experiment |
| NQ-161 | Theorem 1 case T 의 direct numerical test (Peierls-Nabarro scaling) | Cat C | **Yes** — same experiment |

**Deliverable to promote**: Theorem 1 case T Cat C → Cat A.
**Minimum runtime**: ~1-2시간 (torus F=1 minimizer Hessian).

### 3.2 C3-T_off (off-center pseudo-Goldstone) — 3 open

| ID | Statement | Cat | 즉시 가용 |
|---|---|---|---|
| NQ-129 (partial) | Goldstone scaling $\lambda_0 \sim \exp(-d_*/\xi_0)$ quantitative | open at off-center | **Yes** — off-center experiment |
| NQ-130 | Boundary-touching Mode 0 character | open | **Yes** — R23 subset analysis |
| NQ-162 | Off-center bulk F=1 minimizer Hessian $d_*$ scan | new open | **Yes** — new experiment |

**Deliverable to promote**: Theorem 1 case T_off Cat B → Cat A.
**Minimum runtime**: ~2-3시간 (L sweep + $d_*$ scan).

### 3.3 C3-O (center-aligned genuine orbital) — 1 open

| ID | Statement | Cat | 즉시 가용 |
|---|---|---|---|
| NQ-138 | $D_4$ correction mixing $(\xi_0/r_0)^k$ scaling | open | **Yes** — L-scan + multipole fit |

(NQ-128, 136, 137, 144 모두 Cat A/B resolved in this session)

**Deliverable**: NQ-138 Cat A + finite-size $D_4$ correction closed form.

### 3.4 C3-M (multi-peak inter-formation) — 2 open

| ID | Statement | Cat | 즉시 가용 |
|---|---|---|---|
| NQ-143 | $\mathcal{F}$-tie convention (strict vs plateau) | conceptual | **Yes** — decision + consistency check |
| NQ-163 | Multi-peak "per-formation Goldstone" decomposition | new open | Theory work |

**Deliverable**: NQ-163 formalization + multi-peak spectrum theorem.

### 3.5 C3-Universal — 0 open (fully resolved)

σ-framework + NQ-146 + Lemma 1 + Lemma 2 (i,ii,iv) 모두 Cat A.

---

### 3.6 C1' (σ-framework Depth) — 11 open (unchanged)

σ-framework 의 depth/robustness/universality. 본 세션이 σ 를 정립했지만 depth exploration 은 후속.

| ID | Statement | Priority | Difficulty |
|---|---|---|---|
| **P-A** | Integer-K vs continuous-u connection | Medium (reframed) | Theory |
| **P-D** | Threshold non-principled embedding | Medium | Theory + systematic |
| **N-1.A** | σ parameter-variation jump | **High** | Numerical scan |
| **N-1.B** | σ-class transition path dynamics | **High** | Heavy numerical |
| **N-1.C** | σ universality across graphs | High | Multi-graph |
| NQ-125 | Spectral-gap cutoff multiple | Low-Medium | Numerical |
| NQ-126 | σ-class = Aut-orbit equivalence quantification | Medium | Numerical |
| NQ-127 | σ perturbation stability | Medium | Numerical |
| NQ-147 | Multi-source discreteness depth | Medium | R23 analysis |
| NQ-148 | σ-jump formalization (phase transition) | **High** | Theory + numerical |
| NQ-149 | Self-referential vs external emergence quantification | Medium | Theory |

**Total C1': 11 open**. σ-framework 의 active research cluster.

### 3.7 C4 (Infrastructure & Long-term) — 17 open (unchanged)

6 P-issues + 5 canonical OPs + 6 secondary NQs.

P-B, P-C, P-E, P-F, P-G, P-H (6)
OP-0001, 0002, 0003, 0004, 0006 (5)
NQ-139, 140, 142, 145, 152, 153 (6)

**Note**: OP-0005, 0007 이미 this session 에서 closed/partial answered.

---

## §4. Status matrix — compact

| Category | Count |
|---|---|
| **Cat A 신규 (session total)** | **25** |
| **Cat B 신규** | 2 |
| **Cat C 신규** | 2 |
| **Clarified / sidestepped** | 6 (M-1, MO-1, N-1 umbrella, OP-0005, OP-0007 partial, NQ-150 qualitative) |
| **Practically resolved (non-core)** | 2 (NQ-156, 157) |
| **Still open** | **36** |
| — C3-T | 2 |
| — C3-T_off | 3 |
| — C3-O | 1 |
| — C3-M | 2 |
| — C1' | 11 |
| — C4 | 17 |
| **Session total tracked items** | 73 (Cat A/B resolved + clarified + practical + still open) |

C3 (11 entries originally) → 현재 **3 Cat A + 1 Cat B + 8 open** (C3-T/T_off/O/M sub-clusters 에 재분류). 정복도 ≈33% raw, **~85%** when counting "structurally resolved" (Theorem 1 framework clarified).

---

## §5. Priority — next session P0 candidate

### 5.1 Highest leverage: Theorem 1 전체 Cat A 승급

**Single target**: Theorem 1 의 3 cases (T, T_off, O) 모두 Cat A.
현재: **O (Cat A), T_off (Cat B), T (Cat C)**.

**작업**:
1. **Torus Goldstone numerical test** (NQ-131 + NQ-161) — ~1-2시간
2. **Off-center pseudo-Goldstone scaling test** (NQ-130 + NQ-162) — ~2-3시간

**예상 산출**:
- Theorem 1 case T Cat C → **Cat A** (torus 에서 $\lambda_0 \ll \lambda_1$ 직접 관찰)
- Theorem 1 case T_off Cat B → **Cat A** (scaling slope ≈ -1 confirmed)
- **Theorem 1 완전 Cat A** (3 cases 모두)

**단일 세션 (4-6시간)** 으로 완결 가능.

### 5.2 Alternative P1 options

- **NQ-138** ($D_4$ mixing scaling): L-scan experiment ~2-3시간
- **NQ-148 + N-1.A**: σ-jump formalization (theory-heavy) — multi-session project 시작
- **NQ-163**: Multi-peak per-formation Goldstone (theory-only, 2-3시간)

### 5.3 Not recommended (이번 단계에서)

- C4 P-issues (6): Fundamental rebuilding projects, 각각 multi-session
- C1' N-1.B (transition path dynamics): Heavy numerical, 본격 프로젝트
- Canonical merge: Stage 6 weekly, user decision

---

## §6. Recommended plan.md target for 2026-04-25

> **Target (2026-04-25):** Theorem 1 **전체 Cat A** 승급. Torus F=1 Goldstone 직접 numerical test (NQ-131/161) + off-center pseudo-Goldstone scaling verification (NQ-130/162). 기존 Case O Cat A (G1 confirmed) 와 결합하여 3 cases 통합.
>
> **Geometric Taxonomy Principle** 를 canonical-ready 형태로 재작성 — S1' axiom 제안의 geometric 확장.

이 target 이 본 세션의 **마지막 major frontier**. 이후 C1' σ-depth (NQ-148 등) 이나 C4 P-issues 로 전환.

---

## §7. 세션 시작 대비 progress

| 지표 | Session start | Session end |
|---|---|---|
| Open items (pre-existing) | 14 | 11 (영향 있음) + 3 sidestep 유지 |
| New NQs | 0 | 36 (NQ-125..163) |
| Cat A deliverables (resolved or new) | 0 | 25 |
| Cat B | 0 | 2 |
| C2 cluster 정복도 | ~0% (open) | **~100%** |
| C3 cluster 정복도 | ~0% | **~67%** (structurally clarified) |
| C1' cluster | untouched | untouched (but σ framework 정립이 준비) |
| C4 cluster | untouched | untouched |
| Conceptual reframe | 0 | 1 (N-1 bug→feature) + Geometric Taxonomy |
| New Canonical proposals | 0 | Axiom S1' v1 + CN14 + CN15/16/17 sharpened |

### 7.1 세션의 3 가장 큰 contributions

1. **Pre-objective Theorem 2 의 Cat A 정착** (graph-class independent, IC-protocol dichotomy) — C2 cluster 완전 정복.
2. **σ-framework 정립** + Axiom S1' v1 canonical-ready draft — Continuous-to-Discrete emergence 의 mathematical 정형화.
3. **Geometric Taxonomy Principle** via G1 honest correction — Theorem 1 의 3-case geometric specification + C3 내부 구조 드러남.

### 7.2 remaining narrative arc

세션의 arc 는:
- plan.md (aftn) → σ framework + N-1 reframe + Theorem 1 (morning work)
- 사용자 지시 (C2 conquest) → Theorem 2 family Cat A
- G1 multi-angle → honest correction (Theorem 1 geometry-specific)
- C3-G1 formalization → Geometric Taxonomy Principle

**다음 natural 진행**: Geometric Taxonomy 가 정식화되었으니 **Theorem 1 의 3 cases 를 모두 Cat A** 로 마감 (next session). 그 후 σ-depth (C1') 또는 infrastructure (C4) 로 확장.

---

## §8. 한 줄 최종 요약

> 본 세션은 C2 (pre-objective mechanism) 완전 정복 + σ-framework 정립 + N-1 reframe + **Geometric Taxonomy Principle** (G1-induced C3 재구조화) 을 달성했다. 현재 36 open, 이 중 **C3-T + C3-T_off 5개** 가 **Theorem 1 전체 Cat A 승급** 의 single-target next-session 과업. C1' σ-depth (11) 과 C4 infrastructure (17) 는 long-term.

**End of 20_final_open_digest.md.**
