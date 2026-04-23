# A_application_scoping.md — Application Layer Scoping

**Session:** 2026-04-23 (G6 deliverable; intended promotion target: `working/A/application_scoping.md`)
**Target (from plan.md §2 G6):** Cognitive / segmentation / community / pattern formation에서의 SCC 적용 가능성. 3-4 concrete experiment designs.
**This file covers:** (a) contrastive (not reductive) positioning of SCC vs existing methods; (b) image segmentation experiment design; (c) SBM community detection experiment design; (d) cognitive perception interpretive framework; (e) limits of reductive claims.
**Depends on reading:** `01_exploration.md` §6 (F1-F4 candidates), Hard Constraint #4 (external framework 환원 금지), CLAUDE.md §Ontological Constraints #4 ("Not fuzzy segmentation, not clustering, not tracking").

---

## §1. Framing: contrastive not reductive

Per Hard Constraint #4 (prompt §8):

> 외부 프레임워크로의 환원 주장 금지. "이것은 결국 Allen-Cahn 이다" / "이것은 clustering 이다" / "이것은 OT 이다" 형식의 reductive 주장 금지. 대조(contrastive)는 허용되지만 환원(reductive)은 금지 (canonical CN10).

CLAUDE.md Ontological Constraint #4: "Not fuzzy segmentation, not clustering, not tracking. No engineering proxies."

**이 파일의 규율**:
- 기존 방법 (Mumford-Shah, Chan-Vese, SBM spectral clustering)과의 **what's different**만 서술.
- SCC-specific feature가 application에서 무엇을 가능케 하는지 구체화.
- "SCC is a form of X"가 아닌 "SCC differs from X in Y respect" 구조.

---

## §2. Cognitive perception — interpretive context only

### 2.1 Contrastive positioning

**Gestalt theory / object perception (Koffka 1935, Kellman 2003)**: perceptual grouping primitives include proximity, similarity, common fate. No formal mathematical primitive.

**SCC correspondence (tentative interpretation)**:
- **Soft cohesion field $u$** ~ graded perceptual unity assignment.
- **Closure $\mathrm{Cl}_t$** ~ Gestalt "closure" law (perceptual completion of boundary).
- **Formation quantum $K$** ~ observed object count (Miller 7±2?).

**This is interpretation, not reduction**. SCC's mathematical structure (4-term energy, analytic PDE) has no empirical cognitive correlate proved.

### 2.2 Scope limitation

- **No experiment design** in this file for cognitive — lacks measurable ground truth in laboratory setting without massive psycholinguistic / perceptual data collection.
- **Keep as "conceptual backdrop"** for interpretive writing in publications, not as empirical test of SCC.

---

## §3. Image segmentation — experiment design

### 3.1 Contrastive positioning

**Mumford-Shah (1989)**: minimizes $\mathcal{E}_{\mathrm{MS}}(u, \Gamma) = \int_\Omega |u - f|^2 + \mu \int_{\Omega \setminus \Gamma} |\nabla u|^2 + \nu |\Gamma|$ (piecewise smooth u + boundary $\Gamma$). Assumes **Euclidean domain**, **gradient-based** boundary term.

**Chan-Vese (2001)**: level-set based; $u$ is piecewise constant; interface is zero level-set of level-set function $\phi$.

**Graph cut segmentation (Boykov-Kolmogorov 2004)**: formulates as max-flow min-cut on graph. Binary label.

**SCC difference**:
- **Graph substrate**: SCC works on arbitrary graph (not just pixel grid).
- **Soft cohesion $u \in [0,1]$**: graded (not binary) assignment primitive.
- **Four-term energy**: closure + separation + boundary + transport. Chan-Vese has only data term + perimeter.
- **Formation Quantization**: $K$ is integer invariant within basin — naturally handles "how many objects."
- **Protocol-dependence**: SCC segmentation depends on initialization protocol (via Layer 1 basin selection).

### 3.2 Experiment design: SCC-Seg vs Chan-Vese on non-grid graphs

**Setup**:
- Build a graph $G = (V, E)$ from input image where edges link both spatially-neighboring pixels AND **feature-similar distant pixels** (k-NN on pixel intensity). This gives non-grid structure.
- Construct cohesion indicator $u_0(x) = f(x)$ from pixel intensity (scaled to $[0,1]$).
- Run SCC gradient flow with canonical energy parameters.
- Extract formations: connected components of $\{u > 0.5\}$ = K formations.

**Input**:
- 20 images with known ground-truth segmentation (Berkeley BSDS dataset).
- 10 images with **topologically non-trivial** structure (e.g., occlusion, dot-patterns) where grid Chan-Vese struggles.

**Metrics**:
- **Intersection-over-Union (IoU)** vs ground truth.
- **Formation count error** $|\widehat K_{\mathrm{SCC}} - K_{\mathrm{GT}}|$.
- **Boundary quality**: Hausdorff distance between SCC boundary and GT.
- **Protocol sensitivity**: std of IoU across 10 random initializations.

**Expected outcome (hypothesis)**:
- On standard images: SCC-Seg IoU **within 5%** of Chan-Vese (neither strongly better).
- On non-grid graphs: SCC-Seg IoU **20%+ better** (Chan-Vese lacks graph support).
- Formation count recovery: SCC-Seg recovers $K_{\mathrm{GT}}$ within ±1 on 70%+ images; Chan-Vese doesn't naturally count objects.

**Success criterion**: SCC-Seg wins on non-grid / topologically structured images, ties or marginal on grid images. This confirms **graph generalization** is the SCC-specific advantage, not pure segmentation quality.

### 3.3 Category

- **Experiment as designed**: testable, empirical Cat C (will generate Cat A findings upon execution).
- **Hypothesis "wins on non-grid"**: Cat C (plausible but not proved).
- **Anti-reduction**: This is not "SCC reduces to segmentation." It's "SCC generalizes to graph substrate."

---

## §4. Community detection on SBM — experiment design

### 4.1 Contrastive positioning

**Stochastic Block Model (SBM, Holland-Laskey-Leinhardt 1983)**: generative graph model with K blocks; intra-block edge prob $p > q$ inter-block.

**Spectral clustering (Shi-Malik 2000, Ng-Jordan-Weiss 2001)**: eigenvectors of Laplacian → k-means → K clusters. Standard baseline.

**Belief propagation (Decelle et al. 2011)**: BP on SBM; optimal for sparse SBM below information-theoretic threshold.

**SCC difference**:
- **Cohesion field as continuous variable**: SCC maintains $u \in [0,1]$, not discrete labels.
- **Formation Quantization emerges**: $K$ is output, not input (spectral clustering requires $K$ as input).
- **Self-referential closure**: iterative closure $\mathrm{Cl}$ ≠ spectral projection.

### 4.2 Experiment design: SCC community detection on SBM

**Setup**:
- Generate SBM graphs with $K_{\mathrm{block}} \in \{2, 4, 8\}$, $n = 1000$, density $p, q$ tuned to various SNR regimes (above, at, below threshold).
- Run SCC gradient flow with uniform-c initialization.
- Extract $\widehat K$ via $K_{\mathrm{step}}$ operator.
- Compare to ground-truth block count $K_{\mathrm{block}}$ and partition.

**Hypothesis**:
$$\widehat K_{\mathrm{SCC}} = K_{\mathrm{block}} \text{ exactly when SNR} > \text{threshold}.$$

**Metrics**:
- **Block count recovery**: exact match rate over 100 samples per (p, q) pair.
- **Partition accuracy** (AMI, NMI, V-measure) vs GT labels (via formation membership).
- **Threshold location**: compare SCC threshold $q/p$ to spectral clustering threshold.

**Expected outcome**:
- **Above threshold**: $\widehat K_{\mathrm{SCC}} = K_{\mathrm{block}}$ with 90%+ recovery; partition AMI > 0.8.
- **Below threshold**: $\widehat K_{\mathrm{SCC}} = 1$ (single formation; block structure undetectable).
- **At threshold**: $\widehat K$ distribution broadens (similar to V7 P3 bistable Gaussian).

**Success criterion**: Threshold location within 10% of spectral clustering + automatic $K_{\mathrm{block}}$ recovery without input. "Automatic $K$" is SCC's specific contribution.

### 4.3 Category

- **Experiment design**: testable Cat C.
- **Hypothesis $\widehat K = K_{\mathrm{block}}$**: Cat C (verifiable).
- **Anti-reduction**: SCC is not clustering. SCC emergent observable $\widehat K$ coincides with block count in specific SBM regime. Different methods would give different results below threshold.

---

## §5. Pattern formation — contrastive note only

### 5.1 Contrastive positioning

**Turing patterns (1952)**: reaction-diffusion equations produce periodic patterns. Requires two fields (activator + inhibitor) with different diffusion rates.

**Cahn-Hilliard (1958)**: one-field phase separation with mass conservation. Produces coarsening.

**SCC difference**:
- **Graph substrate** (not continuum).
- **Three-component energy** (not just $\int |\nabla u|^2$).
- **Volume-constrained simplex** $\Sigma_m$ (not free).
- **Closure self-referentiality**: novel primitive absent from classical pattern formation.

### 5.2 Scope limitation

- **No experiment design** — pattern formation's ground truth is itself the observed pattern; no independent benchmark.
- **Keep as conceptual backdrop** for Stage 2/3 canonical writing on multi-formation.

---

## §6. Consolidated experiment design summary

| Experiment ID | Domain | Input | Output | Expected SCC advantage |
|---|---|---|---|---|
| **EX-Seg-1** | Image segmentation | 30 images (20 BSDS + 10 non-grid) | IoU, formation count, boundary Hausdorff | Non-grid graph support |
| **EX-Seg-2** | Segmentation protocol sensitivity | Same images × 10 random seeds | Std of IoU | Protocol specification importance |
| **EX-SBM-1** | Community detection | 100 SBM samples × (K=2,4,8) × 5 SNR points | Block count recovery + AMI | Automatic $K$ inference |
| **EX-SBM-2** | Threshold localization | Fine SNR scan near critical | $q/p$ threshold | Comparison to spectral clustering threshold |

---

## §7. Reductive claim checklist (to avoid)

**Claims to AVOID** (reductive, violate CN10 + Hard Constraint #4):

- ❌ "SCC is a segmentation algorithm" — SCC is a theory; segmentation is one experimental test domain.
- ❌ "SCC reduces to Chan-Vese in sharp-interface limit" — T11 Γ-convergence is to perimeter minimizer, not to Chan-Vese piecewise-constant optimizer (different framework).
- ❌ "SCC is a variant of spectral clustering" — spectral clustering is SCC's initialization / seed, not its framework.
- ❌ "SCC generalizes Cahn-Hilliard to graphs" — Cahn-Hilliard has mass conservation; SCC's $\Sigma_m$ constraint is similar but 4-term energy differs.

**Claims to PREFER** (contrastive):

- ✅ "SCC provides graph-substrate generalization of cohesion-field theory."
- ✅ "SCC's formation quantum $K$ is an output, unlike clustering methods that require $K$ as input."
- ✅ "SCC's protocol-dependence is a feature distinct from single-output optimization methods."

---

## §8. Testability of SCC framework via applications

### 8.1 What applications can falsify

- **EX-Seg-1**: If SCC IoU loses systematically even on non-grid graphs → graph-substrate advantage is not real. **Falsifies "graph generalization" claim**.
- **EX-SBM-1**: If $\widehat K_{\mathrm{SCC}} \neq K_{\mathrm{block}}$ even above threshold → automatic K is unreliable. **Falsifies Formation Quantization dynamic interpretation**.
- **EX-SBM-2**: If threshold location is wildly different from spectral clustering → SCC dynamics is idiosyncratic. Doesn't falsify framework but suggests SCC for specific regimes only.

### 8.2 What applications cannot falsify

- **Static Cat A theorems** (72 preserved) are mathematical statements. Application falsification doesn't touch them.
- **Axioms S1-S4** (proposed) are organizational; empirical applications can suggest but not disprove.

### 8.3 Applications feedback to framework

- Observed "SCC segmentation of natural images is worse than deep learning" would not falsify framework but suggest **regularization requirements** for real-data domain.
- Observed "SCC recovers $K_{\mathrm{block}}$ exactly at spectral threshold" would **strengthen** Formation Quantization claim empirically.

---

## §9. Limits of application claims

### 9.1 Cognitive perception

- SCC has **no model of cognitive attention, consciousness, or learning**. Mapping to "object count = Miller 7±2" is purely suggestive.
- Application to cognitive data requires massive additional infrastructure (stimulus design, behavioral measurements) outside the SCC framework.

### 9.2 Image segmentation

- SCC **lacks the "data term"** $\int_\Omega |u - f|^2$ of Mumford-Shah. Adding it would make SCC a hybrid (not pure SCC). Pure SCC produces cohesion-only segmentation, which may not match image intensity.

### 9.3 Community detection

- SCC **requires the graph as input**; doesn't build graph from data. SBM has graph; social networks have graph. But text-clustering, for instance, requires graph construction step — separate from SCC.

### 9.4 Pattern formation

- SCC **produces patterns via formation emergence + coarsening**, but its 4-term energy is distinct from classical reaction-diffusion / Cahn-Hilliard. Not a "replacement" for them.

---

## §10. Recommended execution order

For future experimental sessions (NOT today — plan §4 non-goals):

1. **EX-SBM-1** first (most controlled; SBM has strict ground truth).
2. **EX-Seg-1** second (natural images; broader impact).
3. **EX-SBM-2** after EX-SBM-1 (refinement).
4. **EX-Seg-2** in parallel with EX-Seg-1 (protocol sensitivity).

Priority rationale: SBM gives mathematical assurance on framework claims ($\widehat K$ recovery), then segmentation stress-tests on realistic data.

---

## §11. Open questions

### 11.1 NQ-72 — Data-term augmentation

How to add $\int_\Omega |u - f|^2$ data term without breaking SCC canonical structure (4 independent terms, CN5)? Add 5th term? Modify existing?

### 11.2 NQ-73 — Graph construction from image

k-NN? $\epsilon$-ball? Superpixel? Affects result; protocol dependence extended.

### 11.3 NQ-74 — Comparison methodology

Standard IoU, AMI, NMI work, but SCC's protocol dependence means single-run comparison is misleading. Need **ensemble-averaged metrics**.

### 11.4 NQ-75 — Scalability

Current `CODE/scc/` handles small graphs (up to 10,000 nodes). Larger (social networks 10^6 nodes) requires algorithmic engineering.

---

## §12. File status

- **Primary deliverable**: 4 experiment designs (EX-Seg-1, EX-Seg-2, EX-SBM-1, EX-SBM-2) with metrics + expected outcome + success criteria.
- **Contrastive positioning**: explicit per Hard Constraint #4.
- **Cognitive + pattern formation**: kept as interpretive context, no experimental design (insufficient ground truth).
- **Intended promotion**: `working/A/application_scoping.md` (신규 디렉토리 + 파일).

**End of A_application_scoping.md.**
