# 26b_FK_analogy.md — Frenkel-Kontorova Analogy: Deep Theoretical Background

**Session:** 2026-04-24 (while deep dive running)
**Purpose:** PN barrier theory + Aubry transition 의 SCC 적용. SCC 가 진짜 FK-like 이면 어떤 phenomena 예상되는가.

---

## §1. Frenkel-Kontorova model recap

1D discrete chain of atoms in periodic potential:
$$H_\text{FK}(\{u_i\}) = \sum_i \frac{1}{2}(u_{i+1} - u_i - 1)^2 + \sum_i V_0 \cos(2\pi u_i)$$

- First term: elastic coupling (lattice springs), favors uniform spacing
- Second term: periodic substrate, favors commensurate positions

**Competition**: elastic favors incommensurate, substrate favors commensurate.

## §2. Aubry transition (1983)

Near critical coupling $V_\text{AI} = V_0^{crit}$:
- **Commensurate regime** ($V_0 < V_\text{AI}$): soliton smooth, mobile, continuum-like
- **Incommensurate regime** ($V_0 > V_\text{AI}$): soliton pinned to lattice, discrete
- **Transition point**: sharp — analytic soliton on one side, cantor set on other

Aubry: phase transition, associated with cantorus orbit structure.

## §3. SCC analog?

Naive analog:
- $\xi_0$ = soliton width (SCC interface width)
- $a$ = lattice spacing
- $\zeta = \xi_0 / a$ = "smoothness parameter"

**FK Aubry prediction (naively)**: sharp transition at some $\zeta_\text{AI}$.

**But**: FK is 1D + incommensurate conditions. SCC is 2D + commensurate grid. Aubry transition 의 direct analog 확실하지 않음.

**Empirical (our data)**: NO sharp transition observed. Smooth crossover. Inconsistent with Aubry phase transition.

## §4. Peierls-Nabarro barrier (different phenomenon)

PN barrier: energy cost for soliton to move by 1 lattice site.

For 1D FK-like, smooth soliton of width $\xi_0$:
$$E_\text{PN} \approx C \cdot \frac{V_0^2 \xi_0^3}{1} \cdot e^{-\pi^2 \xi_0 / a}$$

For $\xi_0 / a \gg 1$: exponentially small
For $\xi_0 / a \ll 1$: order 1 (substantial pinning)

This is **smooth crossover**, not phase transition. Consistent with our data.

## §5. SCC 의 expected PN structure

Translation mode eigenvalue estimate:
$$\lambda_0^\text{PN} \sim \beta \cdot e^{-c \zeta^{-1}}$$ 

Linear in β (energy scale), exponential in $1/\zeta$.

**For our test**: at β fixed, varying ζ:
$$\log \lambda_0 = \log \beta - c/\zeta + \text{const}$$

Slope of log λ_0 vs 1/ζ should be linear.

**Check with data** (Phase B earlier):
| ζ | 1/ζ | log λ_0 |
|---|---|---|
| 0.2 | 5.0 | 2.81 |
| 0.5 | 2.0 | -1.92 |
| 0.8 | 1.25 | -8.91 |
| 1.0 | 1.0 | -14.70 |

Fit log λ_0 vs 1/ζ:
- (0.2→0.5): slope = (-1.92 - 2.81)/(2 - 5) = -4.73 / -3 = 1.58 
- (0.5→0.8): slope = (-8.91 - (-1.92))/(1.25 - 2) = -6.99 / -0.75 = 9.32
- (0.8→1.0): slope = (-14.70 - (-8.91))/(1.0 - 1.25) = -5.79 / -0.25 = 23.16

Slope grows with increasing ζ — **NOT linear in 1/ζ**. PN formula doesn't fit linearly.

**Alternative**: maybe log λ_0 ~ -c/ζ² or -c/ζ^p with p > 1?

Try fit log λ_0 vs 1/ζ²:
- (0.2→0.5): slope (log λ)/(1/ζ²): (-4.73)/(4-25) = -4.73/-21 = 0.225
- (0.5→0.8): (-6.99)/(1.56-4) = -6.99/-2.44 = 2.86
- (0.8→1.0): (-5.79)/(1-1.56) = -5.79/-0.56 = 10.3

Still growing — not quadratic either.

Maybe the correct fit form is more complex, involving β directly:
Remember β = 1/ζ². So log β = -2 log ζ, and as ζ increases, β decreases toward β_crit.

Landau critical: λ_0 ~ (β - β_crit). Take log:
log λ_0 ~ log(β - β_crit)

For L=16, β_crit = 0.609. β values:
| ζ | β | β - β_crit | log(β - β_crit) |
|---|---|---|---|
| 0.2 | 25.0 | 24.39 | 3.19 |
| 0.5 | 4.0 | 3.39 | 1.22 |
| 0.8 | 1.56 | 0.95 | -0.05 |
| 1.0 | 1.0 | 0.39 | -0.94 |

Observed log λ_0:
| ζ | log λ_0 |
|---|---|
| 0.2 | 2.81 |
| 0.5 | -1.92 |
| 0.8 | -8.91 |
| 1.0 | -14.70 |

Fit log λ_0 vs log(β - β_crit):
- (0.2, 0.5): slope = (-1.92 - 2.81)/(1.22 - 3.19) = -4.73 / -1.97 = 2.40
- (0.5, 0.8): slope = (-8.91 + 1.92)/(-0.05 - 1.22) = -6.99 / -1.27 = 5.51
- (0.8, 1.0): slope = (-14.70 + 8.91)/(-0.94 + 0.05) = -5.79 / -0.89 = 6.51

Slope changing too. So NOT a simple Landau ν = 1 power law.

Actually: Phase 3 will extract this exponent directly.

Maybe the functional form is a combined effect. Let me keep this note for later analysis.

## §6. What does an exponent ν >> 1 mean?

If λ_0 ~ (β - β_crit)^ν with ν > 1 (e.g. ν = 3 or higher):
- Faster decay than mean field
- Standard 2nd-order phase transitions have ν = 1/2 to 1 typically
- ν > 1 is unusual — suggests non-standard critical behavior

Possible interpretations:
- Multiple critical modes interfering
- 2nd-order Landau + higher-order correction
- Something novel to SCC

## §7. 결론 — deep dive 가 구분할 것

**Phase 1 eigenvector overlap**:
- If lowest mode overlaps strongly with Fiedler: **critical soft mode** confirmed
- If lowest mode overlaps strongly with translation: **Goldstone / PN** 

**Phase 2 L=40 decoupled**:
- If near-zero persists at β/β_crit = 20: **genuine Goldstone exists**
- If all orbital scale: **no Goldstone, just critical everywhere**

**Phase 3 exponent**:
- ν = 1: **Landau mean field critical**, FK analog irrelevant
- ν ≈ exponential of 1/ζ: **FK-like PN barrier** dominant
- Neither: novel SCC physics

**End of 26b_FK_analogy.md.**
