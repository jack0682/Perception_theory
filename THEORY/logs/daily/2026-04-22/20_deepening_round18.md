# 20 — Round 18: $c$-Regime $\widehat K$ Analysis (Regime II vs Regime I)

**Session:** 2026-04-22 (Round 18, numerical continuation)
**Trigger:** User ran `--c 0.5 --seeds 50` after Regime I ($c=0.3$) run. Two complete datasets for comparison.
**Target:** Analyze $c$-dependence of metastable $\widehat K$; test Round 6 3-regime predictions; refine Conjecture 2.1-v3.
**This file covers:** §1 Side-by-side data. §2 Striking findings. §3 Coarsening interpretation. §4 R6 connection. §5 M-1 / F-1 refinement. §6 Category.

---

## §1. Side-by-side comparison data

### 2D square (L=32)

| β | $c=0.3$ (R1, Regime I) | $c=0.5$ (R2, Regime II) | Ratio I/II |
|---|---|---|---|
| 0.5 | $\widehat K=4.76$±1.42 | $\widehat K=1.36$±0.62 | **3.50×** |
| 1.0 | 4.80 | 1.38 | 3.48× |
| 3.0 | 4.96 | 1.42 | 3.49× |
| 10.0 | 5.50 | 1.62 | 3.40× |
| 30.0 | 7.76 | 2.66 | 2.92× |

### 2D torus (L=32)

| β | $c=0.3$ | $c=0.5$ | |
|---|---|---|---|
| 0.5 | 2.66±1.12 | **1.00±0.00** | **퍼펙트 K=1** |
| 1.0 | 2.66 | 1.00 | all 50 seeds K=1 |
| 3.0 | 2.72 | 1.00 | |
| 10.0 | 3.06 | 1.00 | |
| 30.0 | 4.82 | 1.08 | 첫 deviation at saturation |

### 1D cycle ($n=1024$)

| β | $c=0.3$ | $c=0.5$ | Ratio |
|---|---|---|---|
| 0.5 | 29.22 | 31.64 | 0.92 ($c=0.5$가 약간 높음) |
| 3.0 | 30.08 | 34.52 | 0.87 |
| 30.0 | 41.82 | 56.18 | 0.74 |

### Torus/Square 비율

| β | $c=0.3$ | $c=0.5$ | R14 prediction |
|---|---|---|---|
| 0.5 | 0.56 | 0.74 | ~32 (extensive) |
| 10.0 | 0.56 | 0.62 | ~32 |
| 30.0 | 0.62 | 0.41 | ~32 |

모두 1.0 이하. Extensive prediction 완전 부정 확증.

---

## §2. 주요 발견

### 2.1 Regime II (c=0.5) = 단일-도메인 우세 (2D)

c=0.5에서 **2D square $\widehat K \approx 1.4$**, **2D torus $\widehat K = 1.00$ (완벽)**.

c=0.3에서 2D는 $\widehat K \approx 4-5$. 

**2D에서 c가 대칭점(1/2)일 때 단일-도메인 coarsening이 거의 완벽하게 일어남.** 비대칭점(c=0.3)에서는 multiple droplets이 metastable.

### 2.2 Torus + c=0.5 = 완벽 coarsening

**전 50 seeds × 4 β값(β ≤ 10)에서 K=1.** Std=0.000. 

이는 **M-1 dissolution의 DIRECT 실험 확증**: 2-timescale에서, **적절한 geometry (continuous translation) + 대칭 mass fraction**에서는 gradient flow가 정말로 **K=1 global min에 도달**.

Note: 이것은 Γ-convergence (T11) 예측과 정확히 일치.

### 2.3 1D cycle은 c에 거의 무관

c=0.3: K=29, c=0.5: K=32. **~10% 차이만.**

1D 선형 구조에서는 mass fraction이 "얼마나 많은 flip이 있는가"를 결정 (c=0.5 → 50:50 random flip → 더 많은 transitions). 2D처럼 극적이지 않음.

### 2.4 Saturation에서 다른 거동

2D 비대칭 c=0.3, β=30: K=7.76 (증가).
2D 대칭 c=0.5, β=30: K=2.66 (덜 증가, 여전히 작음).

대칭 mass fraction은 모든 β에서 단일 도메인 지향. 비대칭은 β 증가로 더 rich한 구조 얻음.

---

## §3. Coarsening 해석 (spinodal decomposition 관점)

### 3.1 물리적 그림

**대칭 mass (c=0.5):** 
- Double-well $W(u) = u^2(1-u)^2$가 $u \to 1-u$ 대칭.
- u=0과 u=1 두 상태가 energetically equivalent.
- 단일 interface를 두고 두 domain이 balanced → single interface minimizes.

**비대칭 mass (c=0.3):**
- Minority phase (u=1, 30%) droplets, surrounded by majority (u=0, 70%).
- 여러 droplet이 각각 metastable. 합치려면 majority phase를 통해 이동해야 하는 barrier.

이는 **classic binary mixture phase separation**과 동일:
- 50:50: **single flat interface** (domain coalescence)
- 30:70: **droplets of minority in majority** (droplet morphology)

### 3.2 Gradient flow와 Coarsening

Gradient flow는 coarsening을 수행. 결과 K는 **코어싱의 "stopping point"**에 의해 결정:
- c=0.5: coarsening 경로가 clean (대칭 → single interface 빠르게 형성).
- c=0.3: coarsening 경로 복잡 (droplets merging requires migration through majority).

**Optimizer stopping**에서:
- c=0.5: 거의 완전 coarsened → K=1.
- c=0.3: 부분 coarsened → K=4-5.

### 3.3 Torus + c=0.5의 clean-slate effect

Torus는 continuous translation → domain 위치에 pinning 없음. + c=0.5 → single-interface 빠른 coalescence. 조합: **완벽한 coarsening**.

---

## §4. Round 6 c-regime 이론과의 관계

### 4.1 R6 예측

Regime I ($c < c_{\mathrm{bif}}^- \approx 0.385$): $N^{\mathrm{sep}}_{\mathrm{unst}}$가 $c=0.5$ 대비 +10%.
Regime II ($c_{\mathrm{bif}}^- < c < c_{\mathrm{bif}}^+$): baseline.
Regime III ($c > c_{\mathrm{bif}}^+$): -50-56%.

### 4.2 예측과 데이터 비교

**Predicted (mode count):** c=0.3에서 c=0.5 대비 N_unst ~10% 더 많음.
**Observed (our predictor):** c=0.3 N=14, c=0.5 N=27 (2D sq, β=0.5). c=0.5가 2× 더 많음.

**불일치 원인:** Round 6 예측은 $N^{\mathrm{sep}}$ (cl_sep 기여)에 대한 것. 우리 predictor는 $N^{\mathrm{bd}}$ (bd Morse index만)만 계산.

$N^{\mathrm{bd}}$: $|W''(c)|$에 비례. $|W''(0.5)| = 1$, $|W''(0.3)| = 0.52$. c=0.5가 bd-destabilization 더 강함 → N_unst 더 큼.

$N^{\mathrm{sep}}$: Regime I에서 추가 bipartite modes. 우리가 계산한 것에 포함 안됨.

**결론:** 예측과 관측이 consistent (서로 다른 양을 측정). R6 Regime 이론은 $N^{\mathrm{sep}}$에 대한 것, dynamical $\widehat K$는 $N^{\mathrm{bd}}$ 중심의 서로 다른 양.

### 4.3 그러나 dynamical $\widehat K$는 c-regime 강하게 따름

Dynamical $\widehat K$가 c=0.3 (Regime I) vs c=0.5 (Regime II)에서 **3-4배 차이** (2D). 

이는 **몰드 count가 아니라 coarsening dynamics** 때문. Regime II (대칭 mass)은 coarsening 빠르고 깔끔, Regime I (비대칭)은 droplet morphology 유지.

---

## §5. M-1 / F-1 dissolution 정교화

### 5.1 M-1 refined: coarsening 완전성은 조건부

Round 16에서 M-1 dissolution: "gradient flow $\tau_{\mathrm{slow}} \sim e^{d_{\min}/\xi_0}$ 때문에 K=1 절대 도달 안됨."

**Round 18 데이터는 이를 수정해야 함:**
- c=0.5 torus: gradient flow가 **실제로** K=1 도달 (50/50 seeds).
- c=0.3 torus: K=2.66, K=1 못 도달.

**차이:** c=0.5에서 $d_{\min}$은 의미없음 (K=1이 stable). c=0.3에서 여러 droplet 있고, coarsening은 barrier 넘어야 함.

**M-1 dissolution 수정:**
$$\text{Gradient flow 도달 K} = \begin{cases} 1 & c \approx 0.5 \text{ (symmetric mass, smooth coarsening)} \\ \geq 1 & c \ll 0.5 \text{ or } c \gg 0.5 \text{ (droplet metastability)} \end{cases}$$

### 5.2 F-1 refined: K=2 realized in Regime I

F-1 ("K=2 vacuity") was "K=2 abundantly realized" (R16).

**데이터 확인:** c=0.3 square에서 K=2-9 range, K=2 흔히 관측됨. Regime I에서 명확하게 non-vacuous.

**Note:** c=0.5에서는 K=2-3 가끔 관측 (2D square), K=1 대부분. Regime II에서는 K=1이 dominant하지만 K=2 critical configurations는 여전히 exist.

### 5.3 c-regime이 multi-formation을 결정

**핵심 통찰:**
$\widehat K$가 크려면 **비대칭 mass fraction + droplet morphology**가 필요.

Regime I (c<1/2): droplets of minority → multi-formation phase.
Regime II (c≈1/2): single interface → single-formation phase.
Regime III (c>1/2): droplets of minority (role-swapped) → multi-formation (by $u \to 1-u$ symmetry).

**Predict:** c=0.7 (Regime III) on 2D square → K ≈ 4-5 (by symmetry with c=0.3).

---

## §6. Revised Conjecture 2.1-v4

Incorporating R17 + R18 findings:

> **Conjecture 2.1-v4 (Round 18, Cat B empirical, c-augmented).** For gradient-descent optimization:
> $$\widehat K_{\mathrm{metastable}}(G; \beta, c) = \frac{cn}{m_{\mathrm{per}}(\beta, G, c)},$$
> where $m_{\mathrm{per}}$ depends strongly on $c$:
> - $c \approx 1/2$ (Regime II): $m_{\mathrm{per}} \to c n$ (single domain), $\widehat K \to 1$.
> - $c < c_{\mathrm{bif}}^-$ (Regime I): $m_{\mathrm{per}}$ finite (droplet), $\widehat K \gg 1$.
> - $c > c_{\mathrm{bif}}^+$ (Regime III): by $u \to 1-u$ symmetry, same as I.
>
> Graph-class modulation:
> - Torus (continuous translation): full coarsening at c=0.5 ⇒ **perfect K=1**.
> - 2D square (free BC): near-perfect K=1 at c=0.5 but some K=2/3 pinning.
> - 1D cycle: $\widehat K \sim n/\xi_0$ regardless of c (linear packing).

**Three-regime structure in c** matches R6 prediction **qualitatively**, though via different mechanism (coarsening dynamics, not mode count).

---

## §7. Category + cumulative

### 7.1 New Cat A/B claims (Round 18)

1. **Regime II empirically verified**: c=0.5 → $\widehat K \approx 1$ on 2D, especially torus K=1.00 perfectly.

2. **Regime I $\widehat K \approx 3-4\times$ Regime II** on 2D square. Consistent with droplet-morphology vs single-interface.

3. **c=0.5 torus is "perfect coarsening" regime** — direct empirical confirmation of Γ-convergence K=1.

4. **M-1 refined**: coarsening completeness depends on c-regime, not just on $d_{\min}/\xi_0$.

5. **1D cycle $\widehat K$ is c-insensitive** — different mechanism (linear pattern transitions).

6. **Conjecture 2.1-v4** with c-dependence explicit — unifies R17 + R18.

### 7.2 Residuals

- **Regime III (c > 1/2) test** — predict symmetric behavior to Regime I by $u \to 1-u$. User could run `--c 0.7`.
- **Near-boundary c (→$c_-$ or $c_+$)** — spinodal edges may give anomalous behavior.
- **Analytical $m_{\mathrm{per}}(\beta, c, G)$** — coarsening-dynamics derivation.
- **Larger L scaling** — does $\widehat K$ grow with L at fixed c?
- **Langevin short-time** — Conj 2.1 original form test.

### 7.3 Cumulative Cat A/B (post-R18)

- R1-17: 90
- **R18: 6 (Cat A empirical + Cat B structural)**
- **Cumulative: 96 Cat A/B**.

### 7.4 Next候補

1. **$c = 0.7$ test** (Regime III confirmation) — 5 min, direct test of $u \to 1-u$ prediction.
2. **Langevin short-time** — Conj 2.1 original.
3. **Analytical coarsening theory** — derive $m_{\mathrm{per}}$.
4. **Move on to Stage 2 Axiom Audit** (Option B'').

---

## §8. 즉시 follow-up

**추천 (~5분):**
```bash
python3 experiments/exp_k_hat_validation.py --grid 32 --c 0.7 --seeds 50
```

**예측:**
- 2D square: $\widehat K \approx 4-5$ (Regime I와 symmetric).
- 2D torus: $\widehat K \approx 2-3$ (완벽 1이 아님).
- 1D cycle: $\widehat K \approx 30$ (c-insensitive).

이 실행이 예측과 일치하면 c-regime 이론이 $u \to 1-u$ symmetry로 통합되는 증거.

---

**End of 20_deepening_round18.md.**
