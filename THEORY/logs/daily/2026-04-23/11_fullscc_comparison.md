# 11 — Full SCC vs Pure Allen-Cahn: Landscape Comparison

**Session:** 2026-04-23 (user executed `--with-closure` full SCC run per recommendation).
**Target:** User의 full SCC run (w_cl=w_sep=w_bd=1) 결과를 pure $\mathcal{E}_{\mathrm{bd}}$ (w_cl=w_sep=0) 결과와 비교. **Closure + Separation이 landscape을 어떻게 수정하는가** 분석. 만약 **F=1 stable minimizer가 완전히 사라진다면**, canonical의 "single formation = single disk" 가정에 major 수정 요구.
**Data sources:**
- Pure $\mathcal{E}_{\mathrm{bd}}$: prior `exp_orbital_fullscale.json` (§10에서 분석).
- Full SCC: 방금 실행된 결과 (user 제공).
- 둘 다 **동일** config: grid 32×32, c=0.5, β=30, n_seeds=30, 3 IC modes.

---

## §1. 단일 문장 답

> **Closure + Separation이 "single-disk" orbital을 landscape에서 제거한다.**
>
> 동일 (32×32, c=0.5, β=30) setup에서:
> - Pure E_bd: F=1 K=1 stable minimizer **존재** (E=125.15).
> - Full SCC: F=1 K=1 stable minimizer **존재하지 않음**. 최저 F stable = **F=5**.

이 발견은 canonical의 "1s ground state = single disk" 암묵 가정을 **empirically 반증**한다.

---

## §2. Side-by-side 핵심 수치

### 2.1 Summary table

| Metric | Pure E_bd (§10) | Full SCC (this) | 변화 |
|---|---|---|---|
| Total runs | 90 | 90 | — |
| Phase 1 runtime | 5.1s | 392.6s | **77× slower** (closure cost) |
| Total distinct clusters | 90 | 90 | — |
| **Stable (Morse=0)** | **56** | **56** | 동일! |
| Saddles (Morse=1) | 34 | 34 | 동일! |
| Distinct (F, K_step) pairs | 52 | 51 | −1 |
| Distinct mode-1 labels | 37 | 39 | +2 |
| **Lowest stable E** | 89.54 (F=13, K=1) | **92.94** (F=8, K=1) | +3 (비슷) |
| **Highest stable E** | 610.58 | 627.66 | +17 |
| **Lowest F in stable** | **1** (K=1, E=125) | **5** (K=2) | **+4!** |
| Highest F in stable | 45 | 63 | +18 |
| **F=1 stable 존재?** | **YES** (E=125.15) | **NO** | **결정적 차이** |

### 2.2 Ground-state basin 이동

Pure E_bd lowest-F stable hierarchy:
- F=1, K=1, E=125.15 (single disk)
- F=2, K=2, E=99.85 (split)
- F=2, K=1, E=100.12 (bilobed)

Full SCC lowest-F stable hierarchy:
- **F=5, K=2, E=168.36** (5 peaks split into 2 groups)
- **F=8, K=1, E=92.94** (8 peaks connected)
- F=11, K=2, E=173.70

**Full SCC's "ground state region"이 F ≥ 5로 시작**.

---

## §3. 주요 발견: Closure의 landscape 재구성

### 3.1 Finding FSC1 — **Single disk (F=1)은 full SCC에서 local min 아님**

90 runs across 3 IC modes (eigmode_combo, fiedler_random, random) 전부에서 F=1 (단일 local max) configuration이 **stable minimum으로 나타나지 않음**.

Pure E_bd에서는 eigmode_combo seed → F=1 minimizer 직접 도달 (E=125 stable). Full SCC에서 같은 seed → F≥8 stable 또는 F=1 saddle.

**Interpretation**: Closure $\mathcal{E}_{\mathrm{cl}}$ (self-referential 항)가 single disk를 **energetically unfavored**로 만들거나 **Hessian-wise unstable**하게 만듦.

### 3.2 Finding FSC2 — 분포가 **high-F**로 이동

Stable minimizer의 F 분포 (stable만):

| F 구간 | Pure E_bd | Full SCC |
|---|---|---|
| F = 1-5 | ~5개 | **1개** (F=5, K=2) |
| F = 6-10 | ~4개 | ~2개 |
| F = 11-20 | ~7개 | ~6개 |
| F = 21-30 | ~10개 | ~7개 |
| F = 31-45 | ~25개 | ~10개 |
| F = 46-63 | (없음) | **~30개** |

**Full SCC가 고-F 영역으로 massive shift**. Pure E_bd엔 F=46+가 전혀 없지만, Full SCC는 **절반 이상이 F≥46**.

### 3.3 Finding FSC3 — Closure가 **multi-peak을 선호**

$\mathcal{E}_{\mathrm{cl}} = \|u - \mathrm{Cl}(u)\|^2$ 는 closure fixed point 근처에서 minimized. Sigmoid closure는 local reinforcement → **큰 disk의 boundary**에서 불만족 (interior는 sigmoid 고정점 근처이지만 boundary는 불안정).

대신 **작은 peak들이 흩어진 구조**는:
- 각 peak가 독자적으로 closure FP에 근접.
- Peak 간 separation term $\mathcal{E}_{\mathrm{sep}}$도 작음 (이웃 peak와 overlap 최소).
- 결과: **low-E + high-F configurations 안정**.

**이론적 예측**: Closure 강도가 높을수록 (w_cl ↑), F 분포가 high-F로 이동. NQ-115 검증 대상.

### 3.4 Finding FSC4 — **동일한 수의 stable modes (56)** 이지만 다른 질

56개 stable modes identical count인 것은 우연이 아닐 가능성:
- 32×32 grid의 **topological capacity** (configuration space dimension)이 유사한 수의 basin 지원.
- Closure의 역할은 "어떤 basins이 stable인가"를 재선택; basin count 자체는 그래프 구조에 의해 제한.

**NQ-116 (new)**: 다른 grid sizes (24, 48, 64)에서 pure vs full SCC stable count 비교 — 이 "equal count" 가 universal인지 확인.

### 3.5 Finding FSC5 — Mode-1 orbital character 보존

Pure: 37 distinct mode-1 labels.
Full SCC: 39 distinct mode-1 labels.

두 분포 모두 **p (ℓ=1) + g (ℓ=4) 주류** + mixed minority.

**즉 orbital 구조는 closure 하에서도 preserved**. 다만 어떤 orbital에 basin이 배치되는지 달라짐.

---

## §4. Implications for canonical theory

### 4.1 "Single formation = single disk" 가정의 empirical 반증

Canonical §13 Cor 2.2, T-Birth-Parametric, 그리고 대부분의 single-formation 논의가 **single connected disk** 를 single formation으로 전제. 

이 세션 결과:
- Pure Allen-Cahn에선 이 가정 성립.
- **Full SCC에선 성립 안 함**. Full SCC의 "single formation"은 **multi-peak-connected 구조** (F=8, F=20, F=23 K=1 등).

**Canonical 수정 필요**: "Single formation"의 정의를 **F=1 (single local max)** 이 아닌 **K_step=1 (single connected)**로 명시화 + F-spectrum을 추가 observable로 요구.

### 4.2 R18 c=0.5 torus K̂=1.00의 재해석 (revisited)

R18 empirical: c=0.5 2D torus β=30 → K_step = 1.00 ± 0.00 across 50 seeds.

**Pure E_bd 해석**: F=1 single disk.
**Full SCC 해석** (이 세션 발견에 따라): **F ≫ 1**인 connected multi-peak. Likely F=20-30 range.

**NQ-92 (기존)의 re-prioritize**: R18 u*의 F를 측정. If F=1, 이상; if F>1, **orbital theory의 강력한 확증**.

### 4.3 Layer 1a vs Layer 1b (§07 §6.4)의 empirical 정당화

- **Layer 1a ($K_{\mathrm{step}}$)**: threshold-dependent, τ=0.5 counting. Full SCC에서 K_step=1이 abundant (많은 stable basin이 K_step=1 giving).
- **Layer 1b ($\mathcal{F}$)**: threshold-independent, local-max count. Full SCC stable minimizers 중 **F≥5** 유일.

**K_step과 F의 divergence가 closure 하에서 더욱 극대화**. Layer 1a/1b 분리가 정당화.

### 4.4 Axiom S1' (Orbital-Augmented FQ) 추가 empirical 지원

S1' formulation:
$$u^* = \sum_{f=1}^{\mathcal{F}(u^*)} \Phi_f^*(n_f, \ell_f, c_f, r_f) + r(u^*)$$

**Full SCC empirical 증거**:
- $\mathcal{F}$가 formation 수를 정확히 측정 (K_step보다 robust).
- 각 $\Phi_f^*$는 small peak (closure-driven local structure).
- $n_f$, $\ell_f$는 per-peak shape mode labels.

**Cat A empirical foundation 확립** — full SCC에서 F-peak decomposition이 자연스러운 표현.

---

## §5. Closure의 quantitative effect

### 5.1 Energy shift across IC modes

| IC mode | Pure E_bd 전형 E | Full SCC 전형 E | 증가율 |
|---|---|---|---|
| eigmode_combo | 68 – 155 | 93 – 188 | ~30% |
| fiedler_random | 220 – 420 | 265 – 505 | ~20% |
| random | 460 – 610 | 510 – 628 | ~10% |

**Low-E minimizers (eigmode_combo)가 closure에 가장 민감** — closure가 smooth configuration을 더 많이 penalize.

### 5.2 Mode-1 eigenvalue shift

Pure E_bd c=0.5 β=30 F=1: λ_1 = 4.75 (soft d-mode).
Full SCC (F=1 stable 없음, 비교 불가직접).

대신 lowest-E stable 비교:
- Pure F=1 K=1 E=125: λ_1 = 25.14 (tightly bound)
- Full SCC F=8 K=1 E=93: λ_1 = 15.38 (softer)

**Full SCC에서 first excited mode가 softer** — basin이 **wider/shallower**. Interpretation: closure가 multiple peaks를 느슨하게 연결된 configuration으로 유지.

### 5.3 F=1 saddle point 존재

Full SCC에서 F=1 K=1은 **saddle point로 존재** (cluster (15, 1, 167): Morse=1). Gradient flow는 여기를 통과 가능하나 stay하지 않음.

즉 **F=1은 sad landscape의 "pass"**에 위치. 안정 basin은 F≥5.

---

## §6. 두 실험의 종합 해석

### 6.1 "유한 graph에서 SCC는 crystal-lattice-like" 가설 (new)

**Claim 6.1 (Cat C, exploratory)**: 유한 connected graph에서 full SCC는 **crystalline minimizers**를 선호. 즉 **많은 local peaks이 정해진 spacing으로 배치**된 구조. Single-disk는 large-ratio $r_0 / \xi_0$ 에서만 안정.

**근거**:
- Pure E_bd: single disk도 local min (F=1 E=125).
- Full SCC: single disk 불안정 (F=1 saddle); many-peak 안정.
- 이는 closure의 **local self-reinforcement** 와 separation의 **inter-peak repulsion**이 **crystal-like 구조 선호**를 의미.

### 6.2 Connection to biological / chemical analog

**Turing patterns (1952)** 에서 activator-inhibitor balance가 spots / stripes pattern 생성. SCC의 closure-separation balance도 **유사 구조**.

| Turing (reaction-diffusion) | SCC |
|---|---|
| Activator (local) | Closure (local self-reinforcement) |
| Inhibitor (long-range) | Separation (inter-peak repulsion) |
| Spots / stripes pattern | Multi-peak crystal minimizer |

**Contrastive (not reductive)**: SCC는 Turing의 **discrete graph + volume-constraint** 버전. 단순 reduce는 아님 (CN5 4-term energy preserved).

### 6.3 "SCC landscape is not Allen-Cahn"

Full SCC는 ≠ Allen-Cahn에 closure 추가한 것이 아닌, **근본적으로 다른 장**. 단일 disk를 잃고 multi-peak pattern을 얻음.

**Canonical CN14 ("closure expands metastability")**: 원래 "barrier 강화"로 해석. 이제 더 풍부: **closure가 landscape의 minima 분포를 근본적으로 재구성**한다.

---

## §7. 사용자의 "≥2 modes" 기준 (다시)

**Pure E_bd**: 56 stable modes ≥2 ✓
**Full SCC**: 56 stable modes ≥2 ✓

**두 landscape 비교**하면 **100+ stable minimizers** 가 두 setup에 걸쳐 존재. 다른 질의 configurations.

**Orbital modes exist**: empirically ≥2 기준 **far exceeded**. Closure 유무에 관계없이 universal.

---

## §8. New observations post-this-comparison

### 8.1 Runtime cost of closure

**Pure**: 5.1s for 90 runs.
**Full SCC**: 392.6s for 90 runs.
**Ratio**: 77×.

Closure는 sigmoid aggregation + Jacobian evaluation → fundamentally costlier. Large-scale exploration은 full SCC에서 어려움 → pragmatic 시엔 pure $\mathcal{E}_{\mathrm{bd}}$로 exploration 후 full SCC로 verification 권고.

### 8.2 Convergence 문제

Full SCC run에서 여러 seeds가 `conv=False`:
- seed 10, 13, 16, 23, 24 (fiedler_random)
- seed 30, 34, 35, 40, 41, 43, 44, 45, 50, 51, 55, 59 (random, 많음)
- seed 70, 78, 89 (eigmode_combo)

총 ~20개 non-converged. 원인: closure 추가로 KKT convergence criterion이 엄격해짐. `max_iter=50000` 충분치 않은 경우 존재. **NQ-117 (new)**: 수렴 기준 완화 또는 max_iter 증가.

### 8.3 Mode spectrum의 "near-degeneracy"

Full SCC F=20 K=1 E=128 의 spectrum: [0, 11.27, 11.32, 11.34, 11.36] — **거의 degenerate**.

Pure E_bd F=1 K=1 E=125: [0, 25.14, 25.20, 25.22, 25.26] — 역시 거의 degenerate.

**High-symmetry configurations에서는 mode spectrum degenerate**. D_4 irrep mixing에서 발생.

**Implication**: mode 구별을 위한 더 세밀한 diagnostic 필요 (angular multipole만으론 부족).

---

## §9. Revised Theorem G-miss-4 (orbital-aware, closure-aware)

§05 §A에서 제시된 3-condition Theorem + §06 multi-perspective extension + §07 orbital + 이 세션 closure effect.

**G-miss-4 v3 (closure-aware)**:

$\widehat K_{\mathrm{step}} = 1$ a.s. on 2D-like K1-preserving $X$ when:

- (S1)-(S9) per §06 (original conditions for pure $\mathcal{E}_{\mathrm{bd}}$).
- (S10-closure): Under full SCC, $\widehat K_{\mathrm{step}} = 1$ does NOT imply $\mathcal{F} = 1$. Many F-values compatible with K_step=1.

**Cat A empirical**: K_step = 1 observation alone is insufficient to determine formation count in full SCC. Must measure F to disambiguate.

---

## §10. Canonical impact (major revision proposal)

### 10.1 Proposed canonical §13 addition

> **C-2026-04-23-Closure-Landscape (Cat A empirical, proposed)**: On finite 2D graphs at supra-critical β, the full-SCC energy landscape (with $\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}} > 0$) does NOT admit F=1 (single local max) stable minimizers at canonical $c = 1/2$. All stable minimizers have $\mathcal{F} \geq 5$ on 32×32 grid.

### 10.2 Revision to CN14

Current CN14: "Closure expands metastability."

Proposed refinement:
> **CN14' (closure landscape restructuring)**: Closure not only expands metastability barriers but **fundamentally restructures the basin landscape**, removing single-disk minimizers and creating multi-peak (crystalline) stable configurations.

### 10.3 Revision to §11 Three Pillars

Pillar I (Nucleation): 수정 — "seeding by Fiedler mode" 대신 "seeding by multi-mode combination with closure-driven local amplification".

Pillar II (Metastability): 수정 — basin structure가 crystal-like, not single-disk-like.

Pillar III (Coarsening): 수정 — coarsening target K_step=1 but F remains large. **"Coarsening"이 F=1로 가는 게 아니라 K_step=1로 가는 것**.

---

## §11. Priority next steps

### 11.1 Immediate (user execution)

```bash
cd /home/jack/Perception_theory/CODE

# NQ-107: Visualize lowest-E stable minimizers (full SCC):
python3 experiments/exp_orbital_fullscale.py --grid 32 --c 0.5 --beta 30 --n-seeds 5 --with-closure --output /home/jack/Perception_theory/CODE/results/viz_test.json
# + plot each cluster's u field
```

### 11.2 Key verification runs

- **NQ-118** (new): Pure E_bd vs Full SCC on **2D torus** (vs free-BC grid). Torus-geometry 효과 분리.
- **NQ-119** (new): Pure E_bd vs Full SCC on **larger grid (48×48, 64×64)**. F=1 재출현하는 scale 있는가?
- **NQ-120** (new): Pure E_bd vs Full SCC at **c=0.3, c=0.7**. c-regime effect.
- **NQ-121** (new): w_cl 에만 (w_sep=0) vs w_sep 에만 (w_cl=0) 분리 — closure와 separation 각각의 기여 구별.

### 11.3 Theoretical follow-up

- **NQ-122** (new): Why does full SCC favor F ≥ 5? Analytic Hessian analysis at F=1 uniform → show eigenvalue sign flip due to closure.
- **NQ-123**: Turing-analog analysis — SCC의 "activator-inhibitor-like" structure formal 유도.

---

## §12. File status

- **Pure vs Full SCC comparison**: side-by-side 완료.
- **Critical finding**: F=1 stable minimizer 제거 (closure effect).
- **Canonical impact**: CN14' proposal + Three Pillars revision.
- **Cumulative 2026-04-23 new NQ**: 69 (prior) + 9 (this file NQ-115..NQ-123) = **78**.
- **Intended promotion**: `working/SF/closure_landscape.md` (신규) — closure-driven landscape restructuring 결과 정식화.

**End of 11_fullscc_comparison.md.**
