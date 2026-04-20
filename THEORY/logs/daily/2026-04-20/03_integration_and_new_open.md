# 03 — Integration & New Open: Q1–Q4 + Combination Analysis + Recommendation

**Session:** 2026-04-20
**Target (from plan.md):** Q1 (A/E 관계), Q2 (B 단독 가치), Q3 (조합 비용), Q4 (D deferability) 명시 답변 + C+E / B+C / A+C 정밀 비교 + 8 선택지 중 **1개 권고 + 3 근거** + 새 open question 수집. **최종 결정은 사용자 몫.**
**This file covers:** Q1~Q4 (§1–§4) · 조합 비용 정밀 비교 (§5) · B 단독 가치 (§6) · D deferability (§7) · 최종 권고 (§8) · New open questions (§9) · 프롬프트 개선 제안 (§10).
**Depends on reading:** `01_exploration.md` 의 Matrix-1 · Matrix-2 · Cross-reference; `02_development.md` 의 15 세션 스케치.

---

## §1. Q1 — A 와 E 의 관계 (포함 / 병렬 / 독립)

### 1.1 답

**E 는 A 의 구체 경로이다 (strict subset, path specification).**

수학적으로: A 의 scope 를 집합 $S_A = \{$K 얼굴, threshold 얼굴, axiom-switching 얼굴$\}$ 로, E 의 scope 를 $S_E = \{$K 얼굴$\}$ 로 두면 $S_E \subsetneq S_A$. E 는 A 의 **첫 번째 (그리고 가장 구체화된) 실행 경로** 이며, A 의 나머지 두 얼굴 (threshold, axiom) 은 E 의 post-completion 에서 별도 phase 로 수행된다.

### 1.2 근거

**(i) N-1 의 세 얼굴 분해** (`open_problems_reframing_2026-04-19.md` §8):
- N-1 = {P-A (integer-K/continuous-u), P-D (threshold non-principled), P-G (axiom/impl divorce)} 의 공통 원천.
- A 의 commit: "모든 스위칭 제거" → P-A + P-D + P-G.
- E 의 commit: "K 재정의만" → P-A.
- 따라서 $\mathrm{target}(E) = \{P\text{-}A\} \subsetneq \{P\text{-}A, P\text{-}D, P\text{-}G\} = \mathrm{target}(A)$.

**(ii) Matrix-1 cross-check** (`01_exploration.md` §4.1, 2026-04-20 A-E consistency audit 반영):
- A 의 완전해결: **5** (F-1, M-1, MO-1, OP-0005, P-A) — A 가 K-soft 를 declared scope 에 포함하므로 E 와 동일.
- E 의 완전해결: **5** (F-1, M-1, MO-1, OP-0005, P-A).
- A 와 E 는 **Matrix-1 의 5-level 코딩에서 indistinguishable**. 차이는 세션 수 (A 18 vs E 12) · qualitative scope depth (A 는 threshold / axiom 을 '부분 level 에서 더 깊이', E 는 표면만).
- 즉 A ⊇ E 는 scope 포함이되 coarse 매트릭스에서는 drop out. **세션 비용으로만 실질적 구분**.

**(iii) 02_development.md 세션 스케치:**
- A-S2 와 E-S1 은 **동일 topic 에 대한 다른 depth**: A-S2 = "후보 세트 제시 (not yet committed)", E-S1 = "단일 정의 commit + 증명". A-S2 는 E-S1 의 **prerequisite** 과 **광역화** 를 동시에 수행.
- 시간 순서: A 를 선택하면 A-S1 (audit) → A-S2 (K 후보) → A-S3 (threshold) 의 순서로 K 가 3번째 세션에서 attack 되지 않고 4~5번째에야 진입. E 는 E-S1 에서 즉시 K 를 commit.
- 결과: E = "K 를 빠르게, 깊이", A = "N-1 을 넓게, 느리게".

### 1.3 의사결정에의 함의

1. **A 를 고를 때:** purpose 선언문은 "N-1 의 **모든 얼굴** 을 제거" — 선언은 넓지만 **첫 3세션은 E 의 첫 3세션과 유사**. 즉 A 는 실행상 "E-plus-threshold-plus-axiom".
2. **E 를 고를 때:** purpose 선언문은 "K 를 soft 로 재정의" — 선언이 좁지만 완전해결 수 최대. threshold/axiom 얼굴은 **명시적으로 out-of-scope** 으로 선언되어 후속 세션/reformulation 에서 별도 다룸.
3. **실용적 권고:** A 를 고를 바에는 E 를 고르고, E 완료 후 "A-phase 2 = threshold" / "A-phase 3 = axiom" 를 별도 purpose 로 재선언 하는 것이 **scope creep 방지** 에 유리. 이는 plan.md 의 "하루에 너무 많이 풀지 않는다" 원칙 과 reformulation_plan.md §Risks "Scope creep" mitigation 과 일치.

### 1.4 A 와 E 가 독립인 시나리오 (해당 없음)

본 세션은 "A 와 E 가 포함/병렬/독립 중 하나" 를 요구. 분석 결과 **독립** 은 성립하지 않음 — 두 purpose 는 공통 scope (P-A = K 얼굴) 을 공유하므로 최소한 부분 overlap. **병렬** (disjoint but equal priority) 도 성립하지 않음 — $S_E \subsetneq S_A$. 유일한 관계는 **포함**.

---

## §2. Q2 — B 의 단독 가치 (B 단독이 최적인 시나리오?)

### 2.1 답

**존재한다. 매우 좁고 명확한 조건 하에서.**

### 2.2 B 단독이 최적인 시나리오

**시나리오 1 — Publication preparation before reformulation:** 현 canonical 을 학술지/프리프린트에 공개하기 전에 "무엇의 이론이 아닌지" 를 명시화. 출판 후 drift 재발 방지. 본 시나리오에서 B 단독은 **reformulation 자체를 지연시키지 않으면서** 공개의 정직성을 확보.

**시나리오 2 — Unclear purpose → triage:** 사용자가 A/C/D/E 중 어느 것을 선택할지 여전히 확신이 없고, 결정을 1~2주 유보하려는 상태에서 B 는 **결정 유보 기간 동안의 defensible default**. B 완료 시점에 purpose 재평가. 이 경우 B 는 "future reformulation 의 prerequisite infrastructure" 로 기능.

**시나리오 3 — Strict resource constraint:** 사용자가 앞으로 4~5세션만 reformulation 에 할당 가능 (다른 프로젝트 우선). 이 경우 A/C/D/E 중 어느 것도 의미있는 진전 불가 (각 12~20세션 필요 per `02_development.md` §Z). B 는 **4세션으로 완료 가능 (본 세션의 세션 수 추정의 유일 하한)** → 제약된 자원 하에서 유일 feasible 후보.

**시나리오 4 — Risk aversion to Category A loss:** 사용자가 "기존 35 Cat A 를 한 개도 잃고 싶지 않다" 는 **강한 위험 회피**. Matrix-2 에서 B 는 Cat A 상실 0. 다른 모든 단일 후보는 ≥ 5 상실. B 는 유일 **zero-loss** 옵션.

### 2.3 B 단독이 **최적이 아닌** 일반 시나리오

위 4 시나리오 밖에서 B 단독은:
- **이론적 진전 0** (Matrix-1 에서 완전해결 0).
- **Blocking gate 해소** 에 기여하나 이는 "reformulation 시작" 이 아니라 "reformulation 유예 의 공식화".
- `reformulation_plan.md` 의 "1년 가까이 F/M/MO 에 갇혀있었다" 문제 (reframing §0) 를 직접 풀지 않음.

### 2.4 B + (무언가) 조합으로 일반화

실용적으로 B 는 **다른 purpose 의 "first move"** 로 자주 활용 가능:
- **B → 이후 E:** B 로 scope 를 pin 한 후, 다음 purpose 로 E 진입. B 의 CN18 (zero-T commitment) 이 E 의 P-F 부분해결과 일관.
- **B+C 조합:** plan.md 가 이미 고려. B 가 "honest zero-T pin" 을 설정한 후 C 가 "finite T framework" 로 부분해결. 그러나 B 의 CN18 이 "zero-T 만" 을 commit 하면 C 와 **언어 충돌** — 조합시 CN18 을 "잠정 zero-T" 로 wording 조정 필요.

**결론 for Q2:** B 단독은 4 시나리오 (publication prep, triage, resource-constrained, risk-averse) 에서 최적. 일반 reformulation 맥락에서는 **fallback/insurance** 로 기능. 단독 선택의 implicit cost 는 "reformulation 자체의 실질적 시작 유예".

---

## §3. Q3 — 조합 비용의 선형성 (C+E / B+C / A+C)

### 3.1 답

조합의 "비용" 을 두 질문으로 분리:

- **Q3a (raw efficiency):** 조합 추정 세션 수가 단독 후보 세션 수의 단순 합보다 작은가? (Stage 1 공유 · Stage 6 공유 · 중복 제거 측면.)
- **Q3b (interaction direction):** 순수한 상호작용은 긍정 (시너지) / 중립 / 부정 (간섭) 중 어느 쪽인가? (공통 overhead 를 이미 분리한 뒤.)

| 조합 | Naive 합 | 추정 세션 | Q3a 비율 | Q3b 상호작용 |
|---|---|---|---|---|
| **C+E** | 28 | 17 | 0.61 (**강한 준선형**) | **+긍정** (thermal + soft-K 상호 support) |
| **B+C** | 20 | 15 | 0.75 (**준선형**) | **약한 −부정** (CN18 ↔ F4 wording 충돌) |
| **A+C** | 34 | 21 | 0.62 (**강한 준선형**) | **중립** (A audit 과 C 공리 추가가 orthogonal, scope creep 위험만) |

**해석 요령:** Q3a 의 준선형성은 대부분 "Stage 1 declaration 공유" 와 "Stage 6 promotion 공유" 에서 기인 — 이는 조합 고유의 시너지가 아니라 **모든 조합에 적용되는 구조적 overhead 절감**. Q3b 가 순수 상호작용의 부호. 따라서 **Q3a 비율만 비교하지 말고 Q3b 도 같이 봐야** 한다.

### 3.2 C+E 분석 (준선형, 긍정적 상호작용)

**공통 scope:**
- 둘 다 §12 metastability 주장 재작성 (C 는 thermal language, E 는 soft-K language).
- 둘 다 CN6/CN8/CN14 수정.
- 둘 다 γ_eff=0.89 (Cat B) 에 영향.

**중복 제거로 인한 작업 감소:**
- §12 재작성을 **한 번만** 수행 (두 언어를 동시에). 각각 3~4 세션이 2~3세션으로 축소.
- CN6 업데이트를 한 번만.
- γ_eff 의 재해석을 "Kramers at T under soft-K" 로 한 번만.

**상호보완:**
- C 의 entropy 항이 soft-K distribution 의 thermodynamic weight 를 자연스럽게 제공. E 는 soft-K distribution, C 는 그 위의 Gibbs measure. 수학적으로 compatible.
- E 의 $K_{\mathrm{soft}}$ 가 C 의 free energy $\mathcal{F}[u]$ 에 새 term 추가 — $\mathcal{F}[u] = \mathcal{E}[u] - TS[u] + \lambda_K \cdot K_{\mathrm{soft}}(u)$ 식의 변형 가능.

**추정 세션 수:** C 단독 16 + E 단독 12 = 28 naive. Stage 1/6 공유 + §12 공동 재작성 + CN6 공동 수정으로 **17 세션** (02_development.md §Z). Raw 비율 17/28 ≈ 0.61 → **강한 준선형**. 순수 상호작용은 **+긍정** (공유 overhead 제거 후에도 thermal 언어와 soft-K 언어가 상호 정합).

### 3.3 B+C 분석 (raw 준선형, 순수 상호작용 약한 부정)

**공통 scope:**
- B 의 CN18 (zero-T commitment) vs C 의 F-group 공리.
- B 의 §12 erratum vs C 의 §12 rewrite.

**상호간섭:**
- B 의 CN18 "metastability 는 zero-T local-minimum 언어로만" 과 C 의 "유한 T Kramers" 는 직접 충돌. B+C 시 CN18 을 "잠정 zero-T" 로 wording 조정 → 추가 1~2세션.
- B 의 §12 erratum ("metastable 은 정적 의미로만") 과 C 의 §12 재작성 ("Kramers escape") 은 서로 다른 방향으로 §12 를 수정 → 순서 결정 세션 1개.

**상호보완:**
- B 의 CN15-17, CN19-20 (substrate, parameters, time, third-mode) 은 C 와 **orthogonal** — 간섭 없음.
- B 완료 후 C 진입 시 C 가 "honest scope 내에서 thermal 확장" 으로 positioned — 서술적 이득.

**추정 세션 수 (raw):** B 단독 4 + C 단독 16 = 20 naive. Stage 1 공통 3세션 공유 + Stage 6 공통 1세션 공유 → 공유 절감 약 4세션. B 의 orthogonal CN 들 (CN15/16/17/19/20) 은 C 와 간섭 없이 흡수. CN18 ↔ F4 wording 조정 +1 세션, §12 순서 결정 +1 세션 (추가 간섭). 결과 **15 세션** (02_development.md §Z). Raw 비율 15/20 = 0.75 → **준선형** (공유 overhead 절감이 주 원인).

**순수 상호작용 (공유 overhead 를 분리한 뒤):** B 의 substantive 추가 작업 ~2세션 (orthogonal CN). C 의 substantive 작업 ~13세션 (Stage 1/6 제외). 독립 substantive 합 = 15 세션. 상호작용 +2 overhead (wording + 순서) = 실질 17. 그러나 일부 상쇄 (B 의 scope pin 이 C 의 서술 정당화) 로 net 상호작용 **약한 −부정** (+1~2 세션). 따라서 최종 15세션 추정은 공유 overhead 절감이 상호작용 overhead 를 이기는 결과.

**총 평가:** Raw session count 에서는 준선형 (효율적). 순수 상호작용 부호는 약한 부정 (wording 충돌). 두 효과가 공존함을 명시.

### 3.4 A+C 분석 (raw 준선형, 순수 상호작용 중립)

**공통 scope:**
- A 의 audit (switching points) 와 C 의 공리 추가는 **서로 다른 층위**. audit 은 기존 canonical 검토, C 는 신규 공리.
- A 의 K 재정의 (A-S2) 와 C 의 entropy 는 **orthogonal axes** — K 층위 vs thermal 층위.

**상호작용:**
- A 가 K 를 soft 로 만들면 C 의 entropy 가 그 soft-K 의 distribution 에 적용됨. 그러나 **A-S2 에서 K 를 commit 하기 전까지는 C 와 분리 가능**.
- A 의 threshold family · axiom divorce 작업은 C 와 completely orthogonal.

**상호보완:**
- A 가 axiom divorce (P-G) 를 다루는데 C 가 새 F-group 공리를 추가하면 **공리 audit 을 한 번만** 수행 (A 의 audit 가 C 의 공리 정합성 검증에도 기여).

**추정 세션 수 (raw):** A 단독 18 + C 단독 16 = 34 naive. Stage 1/6 공통 공유 ~4세션 + 공리 audit 중복 제거 ~3세션 → **27 세션** 가량 예상. 그러나 A 의 광역 scope (3 얼굴 모두) 와 C 의 thermal 층위 가 cross-product 하는 세션은 예외적으로 적음 (거의 orthogonal). 최종 추정 **21 세션** (02_development.md §Z). Raw 비율 21/34 ≈ 0.62 → **강한 준선형**.

**순수 상호작용:** A 의 K 재정의 (A-S2 의 soft-K candidates) 와 C 의 entropy 는 서로 다른 ontological 축 (K 층위 vs thermal 층위) 에서 작동 → **중립**. A 의 axiom audit (A-S1) 이 C 의 F-group 공리 정합성 검증에 부분 재활용 가능 → 약한 +긍정. A 의 광역 scope 가 scope creep risk 증가 → 약한 −부정. 두 효과 상쇄 → 순 **중립**.

**총 평가:** Raw session count 에서 강한 준선형. 순수 상호작용은 중립. 그러나 C+E 대비 완전해결 수 적고 (4 vs 6) 세션 많음 (21 vs 17) — Pareto 에서 strictly dominated.

### 3.5 조합 순위 (작업량 효율성)

| 조합 | Naive 합 | 추정 | Raw 비율 | 순수 상호작용 | Matrix-1 완전해결 | Matrix-2 Cat A 상실 |
|---|---|---|---|---|---|---|
| **C+E** | 28 | **17** | 0.61 | +긍정 | 6 | 5 |
| **B+C** | 20 | 15 | 0.75 | 약한 −부정 | 2 | 0 |
| **A+C** | 34 | 21 | 0.62 | 중립 | 4 | 5 |

**C+E 가 효율성 최고** — Raw 비율 최저 (0.61) 이면서 완전해결 최대 (6) · 순수 상호작용 유일 +긍정.
**B+C 는 보수적** — 완전해결 적으나 Cat A 상실 0. Raw 비율 0.75 는 공유 overhead 절감 주 원인이며 순수 상호작용은 약한 부정 (CN18 ↔ F4 wording 충돌).
**A+C 는 광역이나 Pareto-dominated** — A-E consistency fix 후 완전해결 6 (C+E 와 동률), Cat A 상실 5~6 (동일), but 세션 21 > C+E 의 17. 순수 상호작용은 중립. C+E 가 세션 수로 A+C 를 weakly Pareto-dominate.

---

## §4. Q4 — D 의 deferability (D 를 미룰 때 선택 purpose 가 D 에 우호적이어야 할 조건)

### 4.1 답

D 를 미룰 때, 선택된 purpose 가 D 와 **compatible** 하려면 다음 구조적 조건 을 만족해야 한다:

**조건 (α) — 공리 언어의 유연성 유지:** 선택 purpose 가 B-group 공리 (B1-B4) 를 **강하게 commit 하지 않음**. Group B 를 CN 으로 "X_t · N_t 는 external" 로 pin 하면 (B 의 CN15 와 같이) D 는 그 CN 을 retract 해야 시작 가능 → retraction overhead.

**조건 (β) — u 의 codomain 확장 가능성:** 선택 purpose 가 u 의 codomain 을 변경한다면 (E 의 simplex-valued, A 의 vector-valued 등), **추가 변경을 허용하는 구조** 를 남겨야. 예: E 가 u 를 $\Delta^{K_{\max}}$ 로 격상하면 D 는 그 후 adjacency 를 u 에서 유도할 때 "site 의 embedding" 을 simplex 로 해석할 수 있어야.

**조건 (γ) — D 의 일부 layer 를 선택 purpose 가 미리 점령하지 않음:** 예를 들어 P-H (time pre-theoretic) 을 C 가 CN 으로 강하게 commit 하면 D 의 "time 도 self-generating" 층위가 차단.

### 4.2 각 단일 후보의 D-compatibility

| 후보 | D 우호성 | 주 이유 |
|---|---|---|
| **A** | **우호** | A 가 "모든 스위칭 제거" 라는 상위 목표이므로 D 는 A 의 자연스러운 후속 ("substrate-level switching = 외부 입력의 비원리성" 을 제거하는 A-phase). 공리 언어도 유연 유지. |
| **B** | **비우호 (조건부 adjustable)** | B 의 CN15 (substrate external) 가 명시적 commitment 로 고정 → D 진입 시 retract 필요. 다만 CN15 를 "잠정 external, 후속 재공식화 대상" 으로 wording 하면 조건부 우호. |
| **C** | **중립** | C 는 substrate 층위를 건드리지 않음. D 와 orthogonal 이므로 간섭 없음. 다만 thermal framework 가 D 의 derived adjacency 의 well-posedness 를 복잡하게 만들 가능성 (noise + u→N 순환). |
| **D** | (D 자체) | — |
| **E** | **우호** | E 는 K 층위만 건드림. substrate 불변. u 의 codomain 변화는 있으나 simplex-valued 는 D 의 substrate derivation 과 양립 (simplex point 간 adjacency 정의 가능). |

### 4.3 조합의 D-compatibility

- **C+E:** 우호 (E 의 우호성 + C 의 중립) — D 에 가장 우호적 조합.
- **B+C:** 비우호 (B 의 CN15 가 차단).
- **A+C:** 우호 (A 의 ontology 광역성 + C 중립).

### 4.4 D 를 아예 첫 purpose 로 선택하는 경우

D 단독 선택 시 (02_development.md §D) 첫 3세션도 "partial D" (sites 고정, adjacency 만 derived) 에 그침. **full D 는 수십 년 단위** 이라는 reformulation_plan.md 의 평가와 일치. 본 reformulation 의 purpose 로 D 를 고르는 것은 사용자의 2026-04-19 carry-forward ("Stage 0 을 저녁에 결정") 관점에서 **후순위 권장** — D 는 장기 background project 로 두고 현 reformulation 은 더 작은 scope 로.

---

## §5. 조합 vs 단일 — 정밀 비교 매트릭스

8 선택지 (A, B, C, D, E, C+E, B+C, A+C) 를 네 축 (완전해결 수, Cat A 상실 수, 추정 세션 수, D-compatibility) 로 한 summary:

| 선택지 | 완전해결 | Cat A 상실 | 세션 | D-우호 | N-1 coverage |
|---|---|---|---|---|---|
| **A** | 5 | 5~6 | 18 | 우호 | K 포함, threshold/axiom 까지 (qualitative 더 깊이) |
| **B** | 0 | 0 | 4 | 비우호 | pin-only |
| **C** | 2 | 0 | 16 | 중립 | hard-side 정당화 |
| **D** | 2 | ≥0 (미지) | 20 | — | orthogonal |
| **E** | 5 | 5~6 | 12 | 우호 | K-얼굴 only |
| **C+E** | 6 | 5~6 | 17 | 우호 | K + thermal |
| **B+C** | 2 | 0 | 15 | 비우호 | pin + thermal |
| **A+C** | 6 | 5~6 | 21 | 우호 | K 포함 (A) + thermal (C), 세션 최대 |

### 5.1 Pareto frontier (2026-04-20 A-E consistency fix 반영)

(완전해결 ↑, Cat A 상실 ↓, 세션 수 ↓) 의 세 축에서 non-dominated 선택지:

1. **B** (0, 0, 4) — "진전 없음" 축의 극단.
2. **B+C** (2, 0, 15) — "zero-loss + minimal 진전" 조합. C 를 strict dominate.
3. **E** (5, 5, 12) — 최소 세션으로 최대 완전해결 (단일 후보 중).
4. **C+E** (6, 5, 17) — 최대 완전해결 (모든 선택지 중).

Dominated:
- **A** (5, 5~6, 18) → **E** (5, 5~6, 12) 가 **weakly Pareto-dominate**: 완전해결 · 상실 같음 + 세션 적음. A 의 qualitative depth (threshold/axiom 더 깊이) 는 이 3축에 잡히지 않음.
- **C** (2, 0, 16) → **B+C** (2, 0, 15) 가 **weakly dominate**: 완전해결 · 상실 같음 + 세션 1 적음 (qualitative thermal depth 로 recovery 가능하나 세 정량 축에서는 dominated).
- **D** (2, 0~1, 20) → dominance 판정은 "미지" 요소로 불확정. 상실 = 0 이면 B+C 에 weakly dominated, 상실 = 1 이면 비교 불능.
- **A+C** (6, 5~6, 21) → **C+E** (6, 5~6, 17) 가 **weakly Pareto-dominate**: 완전해결 · 상실 같음 + 세션 적음. 2026-04-20 A-E fix 후 A+C 와 C+E 의 차이는 오직 세션 수.

### 5.2 Pareto frontier 의 함의

**4개의 rational choice:**
1. "최소 진전, 최대 안전" → **B**
2. "zero-loss 에서 thermal + scope 모두" → **B+C**
3. "단일 후보 중 효율 최고" → **E**
4. "조합의 왕" → **C+E**

나머지 4 선택지는 위 4개 중 하나에 의해 dominated 되거나 (A → E, C → B+C, A+C → C+E) 또는 불확정 (D).

**중요 관찰:** B+C 가 C 를 dominate 함이 수치상 사실이나 **qualitative 비교** 에서는 C 가 thermal depth 에 더 집중 (B 의 CN 작업이 C 의 thermal 핵심을 dilute 할 가능성). 따라서 C 가 "B 의 scope 승급이 실제로 불필요" 한 상황에서는 여전히 선택 가능. 이 qualitative 축은 정량 Pareto 분석이 놓치는 측면.

---

## §6. B 의 단독 가치 재확인 (§2 의 심화)

§2 에서 제시한 4 시나리오 외에 B 가 **조합 내부에서 기여하는 역할**:

- B 의 CN 초안 (CN15-CN20) 은 어떤 purpose 를 고르든 최종 canonical 에 추가될 가치가 있음 — 즉 **모든 purpose 의 Stage 6 (Publication & Promotion) 직전에 B 작업이 부분적으로 수행될 것**.
- 따라서 B 는 "별도 purpose" 라기보다 **다른 purpose 의 마지막 단계에 흡수되는 작업**. 이것이 B 를 단독 purpose 로 declaration 하는 가치를 추가로 희석.

**결론:** B 단독 선택은 §2 의 4 시나리오 밖에서 rational 하지 않음. 대신 **E (또는 C+E) 선택 + Stage 6 에서 B 의 CN 을 흡수** 하는 path 가 일반적으로 우월.

---

## §7. D 의 deferability 재확인 (§4 의 심화)

§4 의 조건 (α), (β), (γ) 에 비추어 **E 단독** 은 D 에 가장 우호 — E 는 K 만 건드리고 substrate 를 그대로 둠. E 가 u 를 simplex 로 격상해도 (E-S1 의 후보 중 하나) 이는 D 의 substrate derivation 과 orthogonal.

**C+E 도 우호** — C 의 thermal framework 는 D 의 derived adjacency 에 약간 complication (noise + u→N 순환) 을 추가하지만 차단 수준은 아님.

**B+C 는 비우호** — B 의 CN15 (substrate external) 가 명시적 commitment 이면 D 진입 시 CN15 retraction 작업 + wording 재작성 추가 세션. 실용적 blocker.

**Recommendation for D deferability:** 만약 사용자가 D 를 "5년 내 수행" 으로 생각한다면 E 또는 C+E 를 권장. "10년+" 로 보류한다면 모든 단일 후보 가능. B+C 만 약한 제약 (retraction 필요).

---

## §8. 최종 권고 — 1개 선택 + 3 근거

### 8.1 권고

**E — Emergent-K framework.**

### 8.2 근거 1 (Matrix-1 기반: 완전해결 수 최대 + 효율)

E 는 단일 후보 중 **완전해결 5개** (OP-0001 F-1, OP-0002 M-1, OP-0003 MO-1, OP-0005 K-selection, P-A Integer-K/Continuous-u Mismatch) 로 **A 와 동률 최대**. A 도 K-soft 작업을 declared scope 에 포함하므로 동일 dissolution 을 achieve. 그러나 E 는 **12 세션** 으로 완료 가능 (A 는 18 세션, threshold/axiom 까지 확장). F/M/MO 삼총사를 단일 reformulation 으로 해소 — plan.md §Why now 의 "1년 가까이 F-1/M-1/MO-1 언어에 갇혀있었던" 상황의 가장 직접적 타개. 조합 C+E 가 6 완전해결로 약간 우위 이나 세션 비용 +40% (17 vs 12). **효율 측면에서 E 단독이 dominant (A 를 weakly Pareto-dominate).** (`01_exploration.md` §4.2 집계)

### 8.3 근거 2 (Matrix-2 기반: Cat A 상실 / 완전해결 ratio 최소)

E 의 Cat A 상실은 5개 (T-Merge (a), Topological Lock, Prop 1.2, Thm 3.1(d), Coupling Bound Lemma — 전부 K-field 전제에 묶인 정리; T-Merge (b) 는 isoperimetric 으로 재증명 유지). 완전해결 5 / 상실 5 = **1:1 ratio**. 단일 formation 정리 19개 Cat A 생존 (T1, T3, T6a, T6b, T6-Stability, T8-Core, T8-Full, T11, T14, T-A2, C-Axioms, QM3, Predicate-Energy Bridge, Deep Core Dom 2b, T-Bind-Proj, T-Bind-Full, T-Persist-1(a), T-Persist-1(b), T-Persist-1(e), Persistence Threshold Equation — 총 19~20 ✓ matrix). **K-field 비용 집중적, 단일 formation 은 보존** — 이것이 E 의 surgical precision. A 는 동일 상실 (5~6) 에 동일 완전해결 (5) 이나 세션 18 > 12 로 E 가 weakly Pareto-superior. (`01_exploration.md` §5.3)

### 8.4 근거 3 (02_development.md 기반: 3세션 내 실질 진입 가능)

E 의 첫 3세션 (E-S1 K_soft 정의 + Lipschitz 증명, E-S2 §12 재작성 골격, E-S3 T-Persist-K-* fate 판정) 은 `02_development.md` §E 에서 **파일명 + 수학 작업 유형 + 건드리는 canonical 섹션** 3요소를 구체적으로 가지며, 특히 E-S1 은 **persistence stability theorem 이라는 확립된 외부 정리** 에 의존. 즉 내일 아침 Stage 1 진입이 즉시 가능. 다른 후보 중 A 는 audit 부터 시작해 K 에 도달하는 데 4~5세션 필요, D 는 full substrate 에 도달하는 데 10+세션, C 는 F-group 공리의 consistency check 에 2~3세션 소요. **E 가 가장 빠르게 substantive 수학 작업에 진입.** (`02_development.md` §E)

### 8.5 권고의 강제력 없음 명시

본 권고는 에이전트의 정량 분석의 귀결이며, **사용자의 최종 결정을 대체하지 않음**. 사용자는:

- **야심 최대화** 를 원하면 **C+E** (완전해결 6, but 세션 17, plan.md §Why now 의 "하루에 너무 많이 풀지 않음" 원칙과 긴장).
- **정직성 최대화** 를 원하면 **B** (세션 4, 이론 진전 0).
- **substrate 혁명** 을 원하면 **D** (세션 20+, 장기 프로젝트).
- **thermal framework 만** 원하면 **C** (세션 16, metastability 정당화).

권고 E 는 **balanced default** 이며, plan.md §Current hypotheses 1 ("E 가 N-1 을 가장 정면 · F/M/MO 삼총사 통합 소멸") 과 일치.

---

## §9. New Open Questions (본 세션에서 드러난 새 물음)

본 세션은 이론을 해결하지 않았지만 — 본 세션의 Non-goal — 아래 물음들이 **작업 중 드러나 수집**. 각 3~5줄 서술. 내일 이후 plan.md 의 Target 후보.

### NQ-1. Soft-K 정의의 uniqueness / canonical choice

`02_development.md` A-S2 에서 4개의 soft-K 정의 후보 (persistence, Betti integral, simplex-valued, measure-valued) 를 제시. E-S1 에서는 persistence 기반 1개를 commit 하되 다른 3개를 "부차적" 로 보류. 물음: **이 4개 중 canonical choice 가 있는가?** 각각이 induce 하는 이론은 같은가 다른가? 예: Betti integral 과 persistence weighted sum 이 같은 $K_{\mathrm{soft}}$ 를 주는지. 2026-04-21 이후 E-phase 2 세션의 candidate target.

### NQ-2. CN7 (dual-mode) 의 원리적 근거

B-S1 CN20 초안 + §1 reframing §3 물음 4. "왜 3 mode 가 아니고 2 mode 인가" 가 canonical 에 원리적으로 답변되지 않음. CN7 은 "특정 구조" 를 긍정하나 "왜 이 특정 구조" 는 미결. 만약 C_t 가 entropy 로 격상 가능하면 (P-C 재프레이밍), 3-mode 체계가 복원될 수 있음. **이는 C purpose 의 후속 작업으로 자연스러움.**

### NQ-3. Persistence vineyard 의 T-Persist-K 대체 가능성

E-S2 에서 제안한 "단일 u 의 persistence diagram flow 로 T-Persist-K 삼총사 대체" 는 vineyard stability (Cohen-Steiner-Edelsbrunner-Morozov 2006) 에 의존. 이 대체가 기존 T-Persist-K-* 의 모든 conclusion 을 회수하는가, 아니면 일부만 회수하는가? **E-phase 3 세션의 core 수학 작업.**

### NQ-4. Q_morph 의 threshold-free 화 의미

A-S3 에서 제안한 integral-over-θ diagnostic. 현 Q_morph 는 이미 superlevel filtration 을 sweep 하지만 최종 diagnostic 에서 threshold 선택이 재등장. **완전 threshold-free Q_morph 가 기존 QM1-4 를 만족하는가?** 만족 안 하면 공리 QM1-4 자체의 재작성 필요.

### NQ-5. B 의 CN 과 C 의 공리 간 wording 충돌

§3.3 에서 드러난 B+C 조합의 "CN18 (zero-T) vs F4 (T > 0 primacy)" 충돌. 이 충돌은 **conservative wording** ("잠정 zero-T") 으로 수동 해결 가능하나, 더 근본적으로는 **"commitment vs axiom" 의 layer 관계** 가 canonical 에 명시되지 않음. CN 이 공리와 충돌할 때의 resolution rule 이 필요. `reformulation_plan.md` 구조에 meta-rule 로 추가 후보.

### NQ-6. D 의 partial variant 의 well-posedness

D-S3 의 fixed-point obstruction 검토는 "u → N[u] → Cl(u)" 의 Banach 식이 $a_{\mathrm{cl}}/4 \cdot L_N < 1$ 을 요구. $L_N$ (N 이 u 에 얼마나 Lipschitz-민감한가) 의 분석이 필요. D 진입시 핵심 prerequisite.

### NQ-7. N-1 의 "axiom-switching 얼굴" 의 scope

§8 reframing 에서 N-1 = P-A + P-D + P-G 로 분해. A 가 세 얼굴 모두 대상이나 "axiom-switching 얼굴 (P-G)" 이 정확히 무엇을 포함하는지 — A1', b_D=0, E3 reclassification 만인가, 아니면 더 많은 "layer-crossing note" 도 포함인가? A 선택 시 첫 세션 (A-S1 audit) 의 core deliverable.

---

## §10. 프롬프트 개선 제안 (MAIN_PROMPT.md 대상)

본 세션 수행 중 MAIN_PROMPT.md (`THEORY/logs/daily/MAIN_PROMPT.md`) 의 다음 점이 마찰을 일으킴:

**P-Prompt-1.** §4 "다중 접근 생성" 이 이론 증명 세션을 전제. 본 세션처럼 **의사결정 재료 생산** 세션은 "다중 접근" 의 자연스러운 interpretation 이 다름 — 접근은 이론 증명 방법이 아니라 **매트릭스 구성 방법** (coverage-first, commitment-first, failure-first). 프롬프트가 이 두 유형을 구분하면 좋음. (해결: 본 세션은 §2 에서 후자로 자연스럽게 해석.)

**P-Prompt-2.** §6 의 출력 파일 3+1 구조 (01, 02, 03, 99) 가 의사결정 세션에도 잘 맞음 — 문제 없음. 다만 파일 이름이 **수학 이론 증명** 을 암시 ("exploration", "development", "integration"). 의사결정 세션에서는 development 가 "세션 스케치" 를 의미하는 게 어색. 파일명 유연성 (alias) 허용 제안.

**P-Prompt-3.** §8 Hard Constraints 10번 "OMC 풀 오케스트레이션 호출 금지" 는 잘 지켜짐. Agent 호출 0회. 본 세션에서 사용자 철학과 일치.

**P-Prompt-4.** §12 예상 오류 패턴 6개 중 "3. derived vs emergent 혼용" 이 본 세션 매트릭스에 반영되어 잘 동작. "E 가 F-1 을 '해결' 하는가 '소멸' 시키는가" 의 구분이 Matrix-1 cell 의 code `완전해결` 의 의미에 미묘한 긴장을 일으켰으나, §7 의 해석 지침으로 완화.

**개선 권장:** MAIN_PROMPT.md 에 "의사결정 세션 (meta-task)" variant 단락 추가 고려. 이론 증명 세션과 meta-task 세션의 기대 산출물 차이 명시. v2 분기 시 반영 제안 — 본 세션은 v1 으로 충분히 작동.

---

## §11. 권고 E 의 반례 시도 (Sensitivity / Counter-arguments)

MAIN_PROMPT §4.4 "반례 시도는 명시적 구성" 원칙의 meta-task 적용. 권고 E 가 **특정 가정 하에서만** 성립함을 명시하여, 그 가정이 깨질 때 권고가 어느 대안으로 이동하는지 지도화. 사용자가 저녁 결정 시 자신의 prioritization 과 본 세션의 가정이 일치하는지 점검.

### 11.1 Counter-scenario CS-1: Soft-K 정의가 well-defined 하지 않으면

**전제:** E 의 핵심 deliverable 은 $K_{\mathrm{soft}}$ 의 엄밀 정의. `02_development.md` E-S1 은 persistence 기반 정의 + Lipschitz via persistence stability theorem 을 가정. 만약 $K_{\mathrm{soft}}$ 가 **canonical 의 다른 구조와 compatible 하지 않는** (예: volume 제약 $\sum u = m$ 과 $K_{\mathrm{soft}}$ 의 minimization 이 상충, 혹은 gradient flow convergence 를 깨는) 것으로 판명되면?

**결과:** E 의 Stage 1 자체가 block. E-S1 이 완료되지 못하면 E-S2 (§12 재작성) · E-S3 (T-Persist-K fate) 로 진입 불가. 실질적으로 E 는 "soft-K 정의의 mathematical exploration phase" 에서 멈춤 — Stage 2 이상 미진입.

**대안으로의 이동:** 이 시나리오에서는 **A (ontology purification)** 가 상대적으로 우위 — A 는 K 정의에 pre-commit 하지 않고 **3~4개 후보 를 병렬 유지** (A-S2). 한 후보가 실패해도 다른 후보로 pivot 가능. E 는 **single bet**, A 는 **portfolio**.

**확률 추정:** 낮음. persistence stability theorem 은 30+ 년 성숙. 그러나 "volume 제약과의 compatibility" 는 novel — 이 세션에서 검증 불가.

### 11.2 Counter-scenario CS-2: Thermal framework 가 결국 필요하다고 판명

**전제:** 본 세션 권고는 "N-1 의 K 얼굴만 우선, thermal framework (P-F) 는 out-of-scope" 로 E 를 선택. 그러나 E 수행 중 "soft-K distribution 의 metastability 를 해석하려면 유한 T 가 필수" 로 판명되면?

**근거:** §8.3 (Kramers integration) 에서 이미 언급 — soft-K distribution 은 본질적으로 확률적 객체. 그것의 "stable modes" 를 정적 언어로만 기술하면 기존 canonical 의 P-F 문제가 **soft-K 로 이전만 된 형태**. 즉 E 는 P-F 를 **해소하지 않고 상속** 함.

**결과:** E 완료 후 즉시 C 진입이 필요. **순차 E → C** 는 **동시 C+E** 보다 비효율 (E-phase 에서 §12 를 soft-K 로 재작성하고, C-phase 에서 다시 thermal 언어로 재작성 — §12 를 두 번 재작성).

**대안으로의 이동:** 이 시나리오에서는 **C+E 조합** 이 처음부터 우위. 세션 17 vs E-only 12 + 후속 C-only 16 = 28. 순차 수행 시 20+ 세션 대비 C+E 동시 17 세션.

**확률 추정:** 중간. 사용자가 "soft-K distribution 의 dynamics" 를 진지하게 연구한다면 thermal framework 는 거의 확실히 필요. 사용자가 정적 카탈로그 (어떤 K 가 가능한가) 에 집중한다면 E-only 로 충분.

**user 판단 요소:** 향후 6개월~1년 내 **metastability 에 대한 claim** 을 쓸 계획이 있는가? 있다면 C+E, 없다면 E.

### 11.3 Counter-scenario CS-3: Publication 우선 순위가 높음

**전제:** 권고는 이론적 진전을 primary value 로 가정. 만약 사용자가 "현 canonical 을 1~2개월 내 학술지/arXiv 에 공개해야 함" 상태라면?

**근거:** B-S3 의 "what this theory is NOT" 서문 단락은 출판 품질의 정직성을 제공. E 의 소프트-K 재정의는 출판 후 v2.0 canonical 의 소관. 출판 전에 소프트-K 를 canonical 에 편입하면 2~3개월 지연.

**결과:** B 단독 (4세션) 이 출판 전 insurance 로 최적. E 는 출판 후 v2.0 작업으로 이전.

**대안으로의 이동:** 이 시나리오에서는 **B 단독** 이 최적. §2.2 의 시나리오 1 과 일치. 그 후 E 는 별도 reformulation cycle 로.

**확률 추정:** 낮음~중간. 2026-04-19 carry-forward 에 "출판" 언급 없음. 그러나 사용자가 "1년 가까이 갇혀있었다" (reframing §0) 는 언급에서 publication pressure 가 간접 시사될 여지.

### 11.4 Counter-scenario CS-4: Substrate 혁명 (D) 을 우선시

**전제:** 권고는 D 를 "장기 프로젝트, 후순위" 로 간주 (§4). 그러나 사용자가 "이론의 pre-objective 주장을 정당화하는 것이 최우선 — substrate 가 external 이면 pre-objective 는 수행적 모순" 이라고 판단한다면?

**근거:** `open_problems_reframing_2026-04-19.md` §6 P-B — "자가참조 이론인데 관계 구조 자체는 자가참조적이지 않다. ... pre-objective 이론이 본질적으로 이산 집합에 의존한다면 철학적 주장과 수학적 토대가 어긋난다." 이 긴장을 가장 심각하게 여기면 D 가 최상위 priority.

**결과:** E 의 소프트-K 재정의는 **철학적으로 부차적** — K 가 soft 이든 integer 이든 substrate 가 external 이면 pre-objective 주장의 근본 문제는 해소되지 않음.

**대안으로의 이동:** **D 단독 우선**. 20+ 세션의 장기 투자 수용. 또는 **B 로 substrate external 을 pin 한 후 미래 D 진입** (단 §4.4 에서 논한 대로 B 의 CN15 는 D 의 blocker — wording 주의).

**확률 추정:** 낮음~중간. 2026-04-19 carry-forward 가 "오늘 의 최우선 과제 = Stage 0 미해소" 를 명시했을 뿐 어느 축이 최우선인지 불명시. 사용자의 철학적 priority 에 의존.

### 11.5 Sensitivity 종합

| 시나리오 | 확률 | 권고 이동 |
|---|---|---|
| CS-1 Soft-K 정의 실패 | 낮음 | E → A |
| CS-2 Thermal 결국 필요 | 중간 | E → C+E |
| CS-3 Publication 우선 | 낮음~중간 | E → B |
| CS-4 Substrate 혁명 우선 | 낮음~중간 | E → D (또는 B → D) |
| 기본 (본 세션 가정) | — | **E** |

**핵심 sensitivity 축:**

1. **Metastability claim 계획 (CS-2):** 가장 중요한 축. 사용자가 향후 6개월 내 "formation 이 어떤 T 에서 안정한가" 식의 주장을 하려면 C+E 필수.
2. **이론적 진전 vs 정직성 (CS-3):** Publication pressure 정도.
3. **철학적 priority (CS-4):** pre-objective ontology 주장 vs 수학적 일관성.

**본 세션의 기본 가정:**
- 사용자는 "F/M/MO 1년 언어 고착 해제" 를 일등 목표로 둠 (plan.md §Why now).
- metastability claim 은 **현재 시점** 에서의 부담이 아님 (향후 세션에서 다룰 수 있음).
- publication timeline 은 즉각적이지 않음.

이 기본 가정들이 유지되면 E 권고 유효. **가정 중 하나가 무너지면 위 매핑에 따라 이동**.

### 11.6 Robust recommendation (가정 불안시)

만약 사용자가 위 3 축 중 어느 하나에 대해서도 확신이 없다면, **E 대신 B 를 first step 으로** 선택하는 robust strategy 고려:

- B (4세션) 완료 후 scope 재검토 — 그 사이에 metastability/publication/substrate priority 가 명확해짐.
- B 의 CN 초안이 어느 후속 purpose 에도 **흡수 가능** (§6 참조).
- Cost 4세션 은 "4세션 지연" 이 아니라 "4세션의 scope-clarification investment".

이는 plan.md §Non-goals ("사용자 대신 최종 결정") 과 일치 — 에이전트의 default 권고는 E 이되, user uncertainty 가 큰 경우 B 를 1-step 완충제로.

---

## §12. Decision Tree — 사용자 priority → 권고 선택지

저녁 결정시 네 개의 yes/no 질문에 순차 답변하여 선택지로 귀착.

```
Q-α. 향후 6개월 내 metastability / Kramers rate / thermal barrier 에 대한
     학술적 주장 을 쓸 가능성이 큰가?
      ├─ YES  → Q-β
      └─ NO   → Q-γ

Q-β (metastability 필요).
    Soft-K framework 도 원하는가 (F/M/MO 통합 소멸)?
      ├─ YES  → 【C+E】 조합. 17 세션. 완전해결 6, Cat A 상실 5~6.
      └─ NO   → Q-β'
                Honest scope pinning (B 의 CN) 도 동시에 원하는가?
                  ├─ YES  → 【B+C】 15 세션. 완전해결 2, Cat A 상실 0. (C 를 dominate)
                  └─ NO   → 【C】 단독. 16 세션. 완전해결 2, Cat A 상실 0.

Q-γ (metastability 현재 불필요).
    Publication pressure 가 높은가 (1~2개월 내 현 canonical 공개 예정)?
      ├─ YES  → 【B】 단독. 4 세션. 진전 0, Cat A 상실 0. 출판 insurance.
      └─ NO   → Q-δ

Q-δ (시간 여유 있음, thermal 불필요).
    Substrate (pre-objective ontology 철학 근거) 가 최우선 priority 인가?
      ├─ YES  → 【D】 단독. 20+ 세션, Cat A 상실 불확정.
      └─ NO   → Q-ε

Q-ε (시간 여유 있음, substrate 후순위).
    가정들이 모두 확실한가 (metastability NO, publication NO, substrate NO)?
      ├─ YES  → 【E】 단독 (본 세션 default 권고). 12 세션. 완전해결 5.
      └─ NO (가정 불확실) → 【B first step, 재검토 후 E 로 pivot】
                             4 세션 B 로 scope clarification, 이후 E 진입.
```

**경로 요약:**

| 최종 권고 | 경로 | 전제 |
|---|---|---|
| **C+E** | α YES → β YES | metastability 필요 + soft-K 원함 |
| **B+C** | α YES → β NO → β' YES | thermal 필요, soft-K 불원, scope pin 동시 원함 |
| **C** | α YES → β NO → β' NO | thermal 만 필요, B 의 CN 불필요 |
| **B** | α NO → γ YES | publication 임박 |
| **D** | α NO → γ NO → δ YES | substrate 철학 최우선 |
| **E** (default) | α NO → γ NO → δ NO → ε 확실 | 본 세션 기본 가정 유지 |
| **B → E** | α NO → γ NO → δ NO → ε 불확실 | 가정 불안정 시 robust 경로 |

### 12.1 A 와 A+C 가 트리에 없는 이유

A 는 E 에 Pareto-dominated (§5.1). A+C 는 C+E 에 Pareto-dominated (§5.1). 따라서 Q-α/β/γ/δ/ε 어느 경로로도 A · A+C 가 최적이 되지 않음. 이들이 선택되는 경우는 "사용자가 E / C+E 에 특별한 거부 이유를 가지는 edge case" 에 한함. 본 트리는 main path 만 다룸.

### 12.2 트리의 한계

- Q-α 는 "6개월 내" 라는 time horizon 에 강하게 민감. 사용자가 "향후 2년 내" 로 해석하면 Q-α YES 확률 증가.
- Q-δ 의 "최우선 priority" 는 scalar 비교를 강제. 실제로 사용자는 여러 priority 를 같은 무게로 둘 수 있음 — 그 경우 트리가 과도 단순화.
- 트리는 본 세션의 Matrix 에 의존. Matrix 의 가정 (예: D 의 Cat A 상실 0 낙관) 이 깨지면 트리 결론도 흔들림.

**권장:** 트리를 **지도** 로 활용하되 **결정문** 으로 쓰지 말 것. `reformulation_purpose.md` 작성시 트리 경로를 한 문장 rationale 로 기록 (예: "Q-α NO, Q-γ NO, Q-δ NO, Q-ε 확실 → E 선택").

---

**Next file:** `99_summary.md` — 세션 요약 + 사용자용 한 줄 메시지.
