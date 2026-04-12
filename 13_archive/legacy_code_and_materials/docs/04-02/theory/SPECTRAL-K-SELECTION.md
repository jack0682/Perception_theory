# Spectral K-Selection: How Graph Structure Determines Formation Count

**Date:** 2026-04-02
**Category:** theory
**Status:** hypothesis + experimental validation
**Depends on:** T8-Core (Cat A), Isoperimetric Ordering (Cat A), Coupling Bound Lemma

---

## 1. The Question

Given a graph $G = (V, E)$ with parameters $(\alpha, \beta, m)$, what is the optimal number of formations $K^*$?

Currently $K$ is externally specified (CN6: "K must be emergent"). This note derives a spectral prediction for $K^*$ and identifies the conditions under which $K > 1$ is energetically preferred.

---

## 2. Energy Scaling with K

### 2.1. Total Energy Decomposition

For $K$ equal formations, each with mass $m_k = m/K$ on volume fraction $c_k = c/K$:

$$E_{\text{total}}(K) = \sum_{k=1}^K E_{\text{self}}(u^k) + \sum_{j<k} E_{\text{inter}}(u^j, u^k)$$

When formations are well-separated, $E_{\text{inter}} \approx 0$ and:

$$E_{\text{total}}(K) \approx K \cdot E_{\text{self}}(m/K)$$

### 2.2. Single-Formation Energy at the Minimizer

At a phase-separated minimizer, the boundary-morphology energy dominates:

$$E_{\text{bd}}(\hat{u}) \approx \sigma_{\text{eff}} \cdot |\partial\text{Core}|$$

where $\sigma_{\text{eff}} = \sqrt{2\alpha\beta} \cdot \int_0^1 \sqrt{W(s)} \, ds$ (from Γ-convergence, T11) and $|\partial\text{Core}|$ is the perimeter of the formation support.

### 2.3. Isoperimetric Argument

By the discrete isoperimetric inequality on $\mathbb{Z}^d$, a connected region of area $A$ has:

$$|\partial S| \geq C_d \cdot A^{(d-1)/d}$$

For $K$ equal formations, each with area $A_k \approx m/(K \cdot \bar{u}_{\text{core}})$:

$$E_{\text{total}}(K) \approx K \cdot \sigma_{\text{eff}} \cdot C_d \cdot \left(\frac{m}{K \bar{u}_{\text{core}}}\right)^{(d-1)/d} = \sigma_{\text{eff}} C_d \left(\frac{m}{\bar{u}_{\text{core}}}\right)^{(d-1)/d} \cdot K^{1/d}$$

**On 2D grids ($d = 2$):** $E_{\text{total}}(K) \propto K^{1/2}$, monotonically increasing.

**Conclusion:** On homogeneous graphs, $K = 1$ is always energetically optimal. The isoperimetric inequality guarantees this universally.

---

## 3. When Can K > 1 Win?

### 3.1. Topological Barrier Condition

On a graph with a bottleneck (e.g., barbell graph with bridge weight $w$), a single formation spanning the bottleneck pays an extra cost:

$$\Delta E_{\text{bridge}} = \alpha \cdot w \cdot (\nabla u)_{\text{bridge}}^2 \approx \alpha \cdot w$$

(since the formation has a sharp gradient across the bridge). Splitting into $K = 2$ removes this cost but doubles the boundary:

$$\Delta E_{\text{split}} = \sigma_{\text{eff}} \cdot (2 \cdot |\partial S_1| - |\partial S_{1 \cup 2}|)$$

$K = 2$ is preferred when:

$$\boxed{\Delta E_{\text{bridge}} > \Delta E_{\text{split}}}$$

This happens when the bridge weight $w$ is sufficiently small relative to the boundary cost ratio.

### 3.2. Spectral Characterization

The bridge weight $w$ is encoded in the Laplacian spectrum. A graph with $J$ near-disconnections has $J + 1$ eigenvalues near zero (the "spectral gap" structure):

$$0 = \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_{J+1} \ll \lambda_{J+2} \leq \cdots$$

The phase transition threshold from T8-Core:

$$\lambda_{\text{thresh}} = \frac{\beta |W''(c)|}{4\alpha}$$

**Spectral K-Selection Hypothesis:**

$$\boxed{K^* = \#\{j : \lambda_j < \lambda_{\text{thresh}}\}}$$

**Interpretation:** Each eigenvalue below threshold corresponds to a "direction" in which the graph can support an independent phase-separated formation. The Fiedler eigenvalue determines if K ≥ 1 formation exists; subsequent small eigenvalues determine if additional formations are energetically accessible.

### 3.3. Regime Classification

| Graph type | Spectral structure | K* prediction |
|---|---|---|
| Homogeneous grid | $0 = \lambda_1 \ll \lambda_2 \sim \pi^2/n^{2/d}$ | K* = 1 (always) |
| Barbell ($w \ll 1$) | $\lambda_2 \approx w \ll \lambda_3$ | K* = 2 when $w < \lambda_{\text{thresh}}$ |
| SBM ($J$ communities) | $\lambda_2, \ldots, \lambda_{J+1}$ small | K* = J+1 if all below threshold |
| Disconnected ($J$ components) | $\lambda_1 = \cdots = \lambda_J = 0$ | K* = J (trivially) |
| Expander graph | $\lambda_2 = \Theta(1)$ | K* = 1 |

---

## 4. Formal Statement

**Proposition (Spectral K-Selection).** Let $G$ be a finite connected graph with Laplacian eigenvalues $0 = \lambda_1 < \lambda_2 \leq \cdots \leq \lambda_n$. Define the phase transition threshold:

$$\lambda_{\text{thresh}} = \frac{\beta |W''(c)|}{4\alpha}, \quad W''(c) = 2(1 - 6c + 6c^2)$$

and the spectral prediction $\hat{K} = \#\{j : \lambda_j < \lambda_{\text{thresh}}\}$.

Then:
1. $\hat{K} = 1$ on any graph with $\lambda_2 \geq \lambda_{\text{thresh}}$ (no phase separation possible; T8-Core).
2. $\hat{K} \geq 2$ on graphs with $\lambda_2 < \lambda_{\text{thresh}}$ and $\lambda_3$ sufficiently small (quantified by the topological barrier condition).
3. The actual $K^* = \arg\min_K E_{\text{total}}(K)$ satisfies $K^* \leq \hat{K}$ (spectral count is an upper bound).

**Note:** $K^* \leq \hat{K}$ because the spectral count provides "capacity" for formations, but the isoperimetric penalty may prevent all of them from being energetically realized. The spectral count is a necessary condition, not sufficient.

---

## 5. Experimental Predictions

| ID | Prediction | Test |
|---|---|---|
| SK-1 | E_total(K) monotonically increasing on grids | Phase A: 4 grid sizes, K=1..4 |
| SK-2 | K=2 preferred on barbell when bridge $w < w^*$ | Phase B: bridge sweep |
| SK-3 | $\hat{K}$ correlates with $K^*$ (r > 0.7) | Phase C: all graphs |
| SK-4 | $K^* = J+1$ on $J$-community SBM | Phase D: structured graphs |

---

## 6. Connection to External Literature

### 6.1. Eigengap Heuristic (von Luxburg 2007)

The standard method for determining K in spectral clustering: choose K such that λ₁,...,λ_K are small but λ_{K+1} is large (maximizing the "eigengap" |λ_K - λ_{K+1}|). In the ideal case of K disconnected components, eigenvalue 0 has multiplicity K, with a gap to λ_{K+1} > 0.

**SCC connection:** Our spectral K-selection hypothesis is a phase-field-aware version of the eigengap heuristic. Instead of looking for the gap, we use the **phase transition threshold** λ_thresh = β|W''(c)|/(4α) as the cutoff. This is more principled because it connects to the energy landscape rather than being purely geometric.

Reference: von Luxburg, U. (2007). A tutorial on spectral clustering. *Statistics and Computing*, 17(4), 395-416.

### 6.2. Higher-Order Cheeger Inequalities (Lee, Oveis Gharan, Trevisan 2012)

The key mathematical result: "k eigenvalues close to zero iff the vertex set can be partitioned into k subsets, each defining a sparse cut." Formally, the k-way Cheeger inequality:

$$\frac{\lambda_k}{2} \leq \phi_k(G) \leq O(k^2) \sqrt{\lambda_k}$$

where φ_k(G) is the k-way expansion constant. This provides theoretical justification for using the first k eigenvectors for k-way partitioning.

**SCC connection:** The SCC phase transition threshold λ_thresh acts as a quantitative cutoff for "eigenvalues close to zero." The higher-order Cheeger inequality guarantees that if K eigenvalues are below threshold, the graph admits K well-separated regions — which is exactly what K formations need.

Reference: Lee, J.R., Oveis Gharan, S., & Trevisan, L. (2014). Multiway spectral partitioning and higher-order Cheeger inequalities. *Journal of the ACM*, 61(6), 1-30. arXiv:1111.1055.

### 6.3. SCC Novelty vs. Spectral Clustering

| Aspect | Spectral Clustering | SCC K-Selection |
|---|---|---|
| Cutoff | Eigengap (relative) | Phase transition threshold (absolute, from physics) |
| Criterion | Geometric (cut quality) | Energetic (formation energy minimization) |
| K determination | Heuristic | Derived from variational principle |
| Self-referential | No | Yes (closure operator affects energy landscape) |
| Formation quality | Not assessed | Diagnostic vector d = (Bind, Sep, Inside, Persist) |

The SCC contribution: replacing the heuristic eigengap with a **physically motivated threshold** from the phase transition theory, and adding self-referential structure that creates enhanced metastability for K > 1 formations.

---

## 7. Experimental Result: The Isoperimetric Wall

### exp51 Results (10 graph configurations)

**K* = 1 universally.** On every tested graph — homogeneous grids (8×8 to 15×15), barbell graphs (bridge weight 1.0 to 0.001), SBM with 2 and 3 communities, random geometric — the single-formation K=1 has strictly lower energy than any K>1 configuration.

| Graph | K* | K_spec | K_eigengap | E(1) vs E(2) |
|---|---|---|---|---|
| 8×8 grid | 1 | 10 | 1 | E(1) < E(2) |
| Barbell w=0.001 | 1 | 10 | 2 | E(1) < E(2) |
| SBM 3×25 | 1 | 3 | 3 | E(1) < E(2) |
| SBM 2×35 | 1 | 2 | 2 | E(1) < E(2) |

### Interpretation: Thermodynamic vs Kinetic K

**The isoperimetric inequality is absolute.** On any connected graph, the boundary cost of K formations scales as K^{1/d}, which is always larger than the single-formation boundary cost. No topological structure can overcome this, because:

1. A single formation can always "flow" through bottlenecks
2. The double-well potential makes formation interiors nearly cost-free
3. Only the boundary contributes to energy, and boundaries are minimized at K=1

**K-selection is kinetic, not thermodynamic.** The number of formations K is determined by:
- **Initial conditions** (how many seeds are present)
- **Barrier heights** (how hard is it for formations to merge)
- **Time** (given enough time, K → 1 via coarsening)

This mirrors the Allen-Cahn coarsening phenomenon, with SCC's enhanced metastability (T7-Enhanced) making K > 1 more persistent.

### Implications for SCC Theory

1. **CN6 ("K must be emergent") is answered:** K emerges from dynamics (initial conditions + barriers), not from energy minimization.
2. **The spectral K-selection hypothesis is falsified** as a thermodynamic prediction.
3. **Spectral structure still matters kinetically:** the eigengap correctly identifies graph community structure (SBM K_eigengap = 3 for 3 communities), which determines where formations are LIKELY to nucleate and how long they persist.
4. **The real question shifts to:** What is the coarsening timescale? How does SCC's enhanced metastability affect it compared to Allen-Cahn?

### Revised Hypothesis: Spectral K-Selection as Initial Condition Predictor

The eigengap K_eigengap predicts the number of formations that will **spontaneously nucleate** from a noisy initial condition, even though K=1 is the global minimum. On SBM with 3 communities, initializing with noise will produce 3 formations that are metastable due to barrier heights.

**Testable:** Initialize with random field, run gradient flow, count formations at convergence. Compare with K_eigengap.

---

## 8. Connection to Existing SCC Results

- **T8-Core** → K ≥ 1 threshold: $\beta > 4\alpha\lambda_2/|W''(c)|$
- **Isoperimetric Ordering** → E(u*_{2m}) < 2E(u*_m): single merged formation is always energetically preferred on homogeneous graphs (proved)
- **K=2 Local Stability** → K=2 is a local minimum even when K=1 is global minimum: the metastability is kinetic, not thermodynamic
- **Enhanced Metastability (T7)** → SCC formations resist merging more than Allen-Cahn domains: closure self-referential structure creates enhanced barriers

**Key insight:** K-selection is about the **thermodynamic** question (which K has lowest energy), while multi-formation persistence is about the **kinetic** question (can formations at a given K persist over time). Both matter, but they are different questions.
