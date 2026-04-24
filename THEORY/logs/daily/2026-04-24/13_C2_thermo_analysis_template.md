# 13_C2_thermo_analysis_template.md — Analysis Template (pre-results)

**Session:** 2026-04-24 (late, 사용자 Phase 3C 실행 대기 중)
**Purpose:** 결과 도착 시 즉시 적용할 분석 framework. 미리 가능한 hypothesis testing structure 준비.

---

## §1. 사용자 결과 도착 후 즉시 분석 절차

```python
# 결과 JSON 형태:
{
  "L_list": [8, 10, 12, 14, 16, 20, 24, 32],
  "results": [
    {"L": 8, "F_pure_min": ..., "F_pure_mode": ...,
     "F_full_min": ..., "F_full_median": ...,
     "F_full_by_ic_random": [...], "F_full_by_ic_fiedler": [...]},
    ...
  ]
}
```

**즉시 추출**:
- $F_*^\text{full}(L)$ = `F_full_min` per L
- $F_*^\text{pure}(L)$ = `F_pure_min` per L
- IC sensitivity ratio = `min(random) / min(fiedler)`

## §2. 4 가능한 결과 시나리오 + 각각의 의미

### 시나리오 S1 — Power-law $F_* \sim L^k$ with $k \approx 1$ (linear in $L$)

**의미**: 
- $F_*$ 가 grid perimeter 와 비례 (boundary 의존)
- "Multi-peak 패턴이 1D-like" — disk 분기가 1D ring 형태 (각 peak 가 angular ladder 의 한 element)
- 연속 limit: $F_*/L \to $ const = "peak density per unit boundary"

**Cat A 승급 가능성**: 본 시나리오 시 $F_*(L) = \alpha L + O(1)$ with $\alpha$ depending on $(\beta, c, \lambda_\text{cl}, \lambda_\text{sep})$. Theorem 2 (iv) Cat B → Cat A.

### 시나리오 S2 — $F_* \sim L^2$ (area-extensive)

**의미**:
- $F_*$ 가 grid area 와 비례 (bulk-driven)
- Multi-peak 패턴이 2D 전반에 걸침 (uniform peak density throughout interior)
- 연속 limit: $F_*/L^2 \to $ const = "peak density per unit area"
- **Pre-objective 가 더 강한 의미**: 모든 area 가 multi-peak

**Cat A 승급 가능성**: 본 시나리오 시 $F_*(L) = \rho L^2 + O(L)$ with $\rho$ being peak-density. Theorem 2 (iv) Cat B → Cat A.

### 시나리오 S3 — $F_*$ saturating at large L

**의미**:
- $F_*$ 가 어떤 finite value 로 수렴
- Multi-peak 가 "small finite cluster" — finite-cluster 가 thermodynamic limit 에서 stable
- 연속 limit: $F_* \to F_\infty < \infty$
- **R23 의 $F_*=5$ 가 thermodynamic limit 의 universal 값일 가능성**

**Cat A 승급 가능성**: 가장 흥미로운 시나리오. $F_\infty$ value 는 finite, $(c, \beta, \lambda_\text{cl}, \lambda_\text{sep})$ 의 함수.

### 시나리오 S4 — IC-dependent: random IC saturates at high F, Fiedler IC reaches low F

**의미**:
- F_*(L) 이 IC 에 강하게 의존
- "True $F_*$" 는 best IC 에서만 도달 — basin attraction 이 IC-biased
- R23 의 $F_*=5$ 가 oneblock-mode IC 에서만 도달

**의미 in NQ-133**: NQ-133 의 sharpened question (basin attraction 의 IC sensitivity) 이 본 시나리오에서 직접 quantified.

## §3. 시나리오 별 후속 statement

### S1 의 경우 (linear)
> **Theorem 2 (iv) refined, S1.** $F_*(L) = \alpha(\beta, c, \lambda_\text{cl}, \lambda_\text{sep}) \cdot L + O(1)$ for sufficiently large $L$. The peak density along boundary scales as $\alpha/L \to 0$ in absolute, $\alpha$ in absolute peak-per-perimeter sense.

### S2 의 경우 (area-extensive)
> **Theorem 2 (iv) refined, S2.** $F_*(L) = \rho(\beta, c, \lambda_\text{cl}, \lambda_\text{sep}) \cdot L^2 + O(L)$. Peak density per unit area $\rho$ is $L$-independent constant in thermodynamic limit.

### S3 의 경우 (saturating)
> **Theorem 2 (iv) refined, S3.** $F_*(L) \to F_\infty(\beta, c, \lambda_\text{cl}, \lambda_\text{sep}) < \infty$ as $L \to \infty$. The pre-objective destabilization saturates to a finite multi-formation cluster.

### S4 의 경우 (IC-dependent)
> **Theorem 2 (iv) refined, S4.** $F_*(L)$ depends on the IC strategy used to access basins. Random IC produces $F_\text{random}(L)$ growing with $L$; adaptive (Fiedler/eigenmode) IC produces $F_\text{adaptive}(L)$ that can reach lower-F basins. The discrepancy quantifies "basin attraction width" of low-F multi-peak configurations.

## §4. NQ-133 의 결과 후 sharpening

본 phase 3C 가 IC type 을 직접 변별 → NQ-133 의 sharpened version:

> **NQ-133 sharpened (post-Phase-3C):** The minimum stable $F_*$ depends on basin-finding protocol. Quantitative measure: $\Delta F_*^\text{IC}(L) := F_\text{random}(L) - F_\text{adaptive}(L) \geq 0$. R23 의 $F_*=5$ at L=32 corresponds to $F_\text{adaptive}(32) = 5$. Phase 3 random-IC F_min=39 corresponds to $F_\text{random}(32) = 39$. Hence $\Delta F_*^\text{IC}(32) \approx 34$.

→ NQ-133 가 IC sensitivity 의 정량화 question 으로 transform.

## §5. Pure E_bd anomaly 진단

L=24, 32 에서 F_pure=0 결과의 source:
- **(D1)** Multi-restart 가 모두 잘못된 attractor 에 진입 (uniform $c\mathbf{1}$ 또는 plateau).
- **(D2)** Optimizer 의 finite iteration 으로 incomplete convergence.
- **(D3)** Pure E_bd 자체의 large-L bifurcation 구조에서 single-disk 가 unstable (= T8-Core 위반?).

Phase 3C 는 8 restarts (mixed IC). 결과:
- (D1) → 적어도 one Fiedler-IC 가 F=1 도달 시 confirmed
- (D2) → max_iter 증가가 도와야 (4000 으로 증가됨)
- (D3) → unlikely (T8-Core Cat A, large $\beta$ 에서 single-disk 항상 stable)

본 phase 3C 결과로 (D1) vs (D2) 식별.

## §6. Theorem 2 의 thermodynamic limit statement (post-3C)

위 시나리오 중 데이터가 confirm 한 형태로:

> **Theorem 2 (Pre-Objective Thermodynamic Limit, post-Phase-3C).** [scenario-specific statement]
>
> The pre-objective destabilization is **[bounded / extensive / linear / IC-dependent]** in the thermodynamic limit $L \to \infty$. SCC 의 pre-objective character 의 [strength] 는 graph size 와 [relation].

본 statement 가 NQ-155 (thermodynamic limit) 의 **direct answer**.

## §7. 결과 도착 시 본 모델의 작업 순서

1. JSON 파싱 → F_pure, F_full, IC-split data 추출
2. 4 시나리오 중 best-fit 식별 (power-law fit, saturation test)
3. 시나리오별 statement 적용 → Theorem 2 (iv) Cat A/B 승급
4. NQ-133 sharpening (IC sensitivity 정량 measure)
5. Pure E_bd anomaly 진단
6. `14_C2_thermo_results.md` 작성:
   - 결과 표
   - 시나리오 식별
   - Theorem 2 (iv) 의 새 Cat 분류
   - NQ-133 의 final status
   - C2 cluster 정복도 update

---

## §8. 추가 NQ 후보 (결과 의존)

- **NQ-158**: 만약 S1: peak-per-perimeter density $\alpha$ 의 $(c, \beta, \lambda)$ dependence — 별도 실험.
- **NQ-159**: 만약 S2: peak-per-area density $\rho$ 의 universality across graphs.
- **NQ-160**: 만약 S3: $F_\infty$ value 와 관계된 conserved quantity (e.g., separation length scale).
- **NQ-161**: 만약 S4: basin attraction 의 measure-theoretic quantification (basin volume vs IC distribution).

위 4 NQ 중 결과에 부합하는 것이 다음 세션 P0 후보.

---

**End of 13_C2_thermo_analysis_template.md.**

대기 중. 결과 도착 시 본 template 에 따라 즉시 분석 후 `14_*.md` 작성.
