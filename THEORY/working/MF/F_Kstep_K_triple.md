# F_Kstep_K_triple.md — F / K_step / K_act / K_field Quadruple Bridge + F as Derived Diagnostic Canonical Registration (OAT-2)

**Status:** working draft (OAT-2, post W5 Day 4 morning batch session).
**Type:** Theory-only audit; F (peak count) canonical registration as derived diagnostic + 4-quantity (F, K_step, K_act, K_field) mathematical bridge.
**Author origin:** OAT-2 W6 priority advanced to W5 Day 4 per user "지금 하자" + "모든 도구 적극 활용 + 자율" direction. Tool A2 (대칭군 몫) + Tool A3 (persistent homology) verification (`mathematical_scaffolding_4tools.md` §3, §4) 결과 활용.
**Canonical refs:** §3.x (formal universe — F register target); §5 (derived geometric notions — F register location); §12 line 827–832 (F vs K_step duality, W4 04-24 added); §11.1 #16 Commitment 16 K_field/K_act (CV-1.5.1); §13 T-PreObj-1 line 1049 (F definition inline); §14 CN17 σ-Labeled Formation Quantization (line 1572).
**Working refs:** `K_status_commitment.md` (OAT-1, K_field/K_act); `mathematical_scaffolding_4tools.md` (OAT-supplementary, Tool A2 + A3); `from_single.md` §3.3 (R23 F=9); `multi_formation_sigma.md` §1.4 vocabulary.
**Open problems:** OP-0009-F (this file's resolution candidate); OP-0009-K (resolved CV-1.5.1 via Commitment 16); OP-0009-A (architecture choice).

---

## §1. Mission Statement

> **"F (peak count) — canonical에 어떻게 등록되어야 하는가? F vs K_step vs K_act vs K_field 4-quantity의 mathematical mapping은? CN17 σ-Labeled Formation Quantization의 강화는 어떻게?"**

이 working file은 OP-0009-F (Multi-Formation Ontological Foundations sub-item F) 의 resolution candidate.

**핵심 결과**:
1. F는 *derived diagnostic*; canonical §5에 신규 subsection (§5.5) 등록 권고.
2. 4-quantity inequality chain: $K_{\mathrm{step}}(u; \tau) \leq \mathcal{F}(u)$ (within single field) + $K_{\mathrm{act}} \leq K_{\mathrm{field}}$ (architectural).
3. Cognitive correlate distinction: $\mathcal{F}$ = within-formation parts; $K = K_{\mathrm{field}}$ = multi-object cardinality (architectural); $K_{\mathrm{step}}$ = observer artifact (threshold-dependent).
4. CN17 strengthen: σ-tuple은 4-quantity refinement label (single-mode F=1 / multi-mode F≥2 / K-field K=K_field).

---

## §2. Quantity Inventory

### §2.1 F (peak count, threshold-free)

**Definition** (T-PreObj-1 inline, canonical line 1049 + §12 line 827):
$$\mathcal{F}(u) := \#\{x \in X : u(x) > u(y)\;\forall y \sim x\}$$
strict local maxima count over graph adjacency $\sim$. Threshold-free, upper semi-continuous.

**Properties**:
- $\mathcal{F}(u) \geq 0$ integer.
- USCO (upper semi-continuous): $u_n \to u$ implies $\mathcal{F}(u) \geq \limsup \mathcal{F}(u_n)$.
- Aut(G)-invariant: $\mathcal{F}(\sigma \cdot u) = \mathcal{F}(u)$ for $\sigma \in \mathrm{Aut}(G)$.
- Under full SCC, $\mathcal{F} \geq 2$ default ground state (T-PreObj-1 (i) Cat A graph-class independent via T-PreObj-1G).

**Empirical anchor**: R23 90-run enumeration (W4 04-23, `from_single.md` §3.3): F = 9 maximum observed on $32 \times 32$ $D_4$ free-BC grid; F ≥ 5 for all stable minimizers (single-disk F=1 absent).

### §2.2 K_step (connectivity count, threshold-dependent)

**Definition** (canonical §12 line 827–829):
$$K_{\mathrm{step}}(u; \tau) := \#\{\text{connected components of } \{x : u(x) > \tau\} \text{ in graph } G\}$$
parameterized by threshold $\tau \in (0, 1)$.

**Properties**:
- $K_{\mathrm{step}}(u; \tau)$ integer-valued, monotone in $\tau$ (decreasing typically, but not strictly).
- Under T-Merge (b) Cat A: $K_{\mathrm{step}}^* = 1$ on pure $\mathcal{E}_{\mathrm{bd}}$ (canonical §12 line 825).
- Threshold-dependent: $K_{\mathrm{step}}(u; \tau_1) \neq K_{\mathrm{step}}(u; \tau_2)$ generically.

**Inequality** (canonical §12 line 832): $K_{\mathrm{step}}(u; \tau) \leq \mathcal{F}(u)$ for any $\tau$. *(Bilobed K=1 configuration with $u_{\mathrm{bridge}} \in (0.5, 1)$: $K_{\mathrm{step}} = 1$ but $\mathcal{F} = 2$.)*

### §2.3 K_act (active stratum index, derived from K-field state)

**Definition** (Commitment 16 (ii), CV-1.5.1):
$$K_{\mathrm{act}}(\mathbf{u}) := \#\{j \in \{1, \ldots, K_{\mathrm{field}}\} : \|u^{(j)}\|_1 > \epsilon\}$$
where $\epsilon$ is a fixed support threshold (default $\epsilon = 0.01 \cdot \bar{m}$).

**Properties**:
- $K_{\mathrm{act}}(\mathbf{u}) \in \{0, 1, \ldots, K_{\mathrm{field}}\}$.
- Right-continuous in $t$ under gradient flow (decreases at K-jump events).
- Per Tool A1 stratified space (mathematical_scaffolding_4tools.md §2): $K_{\mathrm{act}}$ indexes strata $S_{K_{\mathrm{act}}}$ of $\widetilde\Sigma^K_M$.

### §2.4 K_field (architectural cap, modeling-layer commitment)

**Definition** (Commitment 16 (i), CV-1.5.1): integer-valued external modeling-layer commitment; specifies max formation count.

**Properties**:
- Set ex ante by modeler (architectural choice).
- $K_{\mathrm{field}} \in \mathbb{Z}_{\geq 1}$.
- Comparable to $X_t$ structure choice (canonical §3 modeling-layer note).
- **Not** a primitive of $\mathfrak{C}^{\mathrm{soft}}$.

---

## §3. Quadruple Bridge — Inequalities and Relations

### §3.1 Single-field inequality (canonical §12 established)

For any single field $u : X \to [0, 1]$ and any $\tau \in (0, 1)$:
$$K_{\mathrm{step}}(u; \tau) \leq \mathcal{F}(u).$$

**Proof sketch**: Each connected component of $\{u > \tau\}$ contains at least one local maximum (compactness + continuity). $\mathcal{F}(u)$ counts local maxima globally; $K_{\mathrm{step}}$ counts only those above threshold. ✓

### §3.2 Architectural inequality (Commitment 16)

For any K-field state $\mathbf{u} \in \widetilde\Sigma^K_M$:
$$K_{\mathrm{act}}(\mathbf{u}) \leq K_{\mathrm{field}}.$$

**Proof**: By definition $K_{\mathrm{act}}$ counts active formations $j \in \{1, \ldots, K_{\mathrm{field}}\}$; cannot exceed cap. ✓

### §3.3 Per-formation F (in K-field architecture)

For each active formation $u^{(j)}$ in K-field state $\mathbf{u}$:
$$\mathcal{F}(u^{(j)}) \geq 1$$
(active formation has at least one local maximum, by support nonemptiness $\|u^{(j)}\|_1 > \epsilon$).

Under full SCC at per-formation minimum (T-PreObj-1 (i)):
$$\mathcal{F}(u^{(j)}) \geq 2 \quad \text{(generic full SCC minimizer)}.$$

### §3.4 Aggregate F bridge (K-field ↔ aggregate field)

Define aggregate field $U^*(x) := \sum_k u^{(k)*}(x)$. Then:

**Well-separated regime** ($d_{\mathrm{sep}}(j, k) \geq D_{\mathrm{sep}}$ for all $j \neq k$):
$$\mathcal{F}(U^*) = \sum_j \mathcal{F}(u^{(j)*})$$
(disjoint supports → peaks add up).

**Overlapping regime** (T-Persist-K-Weak):
$$\mathcal{F}(U^*) \leq \sum_j \mathcal{F}(u^{(j)*})$$
(overlap regions may merge peaks; equality when no peak coincides at boundary).

### §3.5 Quadruple chain (proposed)

Combining §3.1–§3.4, well-separated regime:
$$K_{\mathrm{step}}(U^*; \tau) \leq \mathcal{F}(U^*) = \sum_j \mathcal{F}(u^{(j)*}) \geq 2 K_{\mathrm{act}}(\mathbf{u}^*) \quad\text{(under full SCC, F≥2 per formation)}.$$

**Note**: $\mathcal{F}(U^*)$ vs $K_{\mathrm{act}}$ comparison requires *full SCC* hypothesis. Pure $\mathcal{E}_{\mathrm{bd}}$에서는 $\mathcal{F}(U^*) = K_{\mathrm{act}}$ (single peak per formation, T-Merge (b) per formation).

### §3.6 Bridge conjecture (BC-1) — OAT-7 verification result

**Conjecture (OAT-2 BC-1)**: Under full SCC + well-separated K-field minimizer, there exists canonical bijection
$$\Phi : \{u^{(j)*}\}_j \leftrightarrow \mathrm{lobes}(U^*)$$
such that each per-formation $u^{(j)*}$ corresponds to exactly $\mathcal{F}(u^{(j)*})$ peaks of $U^*$ within disjoint support region.

**Verification result (OAT-7, W5 Day 4 numerical)**: **BC-1 fails generic in R23 dataset**.

Per `working/MF/single_high_F_equivalence.md` (511 lines, OAT-7 W5 Day 4):
- R23 fullscale dataset: 56 stable minimizers on $32 \times 32$ $D_4$ free-BC grid.
- $\mathcal{F} \in [5, 63]$ (mean 40.6); $K_{\mathrm{step}} \in [1, 8]$.
- **All 56**: $\mathcal{F} > K_{\mathrm{step}}$ (100%, max gap = 61).
- Well-separated $K_{\mathrm{step}} = \mathcal{F}$ regime: **null set** in R23 generic state.

**Implication**: BC-1 holds in *well-separated* regime (D_sep ≥ 3) only; R23 *generic* ground state is **overlapping regime** (T-Persist-K-Weak territory). Aggregate $\mathcal{F}(U^*) = \sum_j \mathcal{F}(u^{(j)*})$ equality fails generically — peak merging at boundaries.

**Status**: BC-1 well-separated **valid**; BC-1 generic **rejected**. R23 generic state requires *overlapping regime* analysis (NQ-242 W6+ PH pipeline).

---

## §4. Cognitive Correlate Distinction (CN10 downstream)

### §4.1 F: within-formation parts

$\mathcal{F}(u^{(j)})$ counts internal multi-peak structure of single formation. Cognitive correlate: **object parts** (gestalt sub-features within one perceptual unit). 인지과학적 의미: 한 *individuated object*의 내부 articulation.

### §4.2 K_field: multi-object cardinality (modeling)

$K_{\mathrm{field}}$ = architectural cap on number of distinguishable formations. Cognitive correlate: **scene-level multi-object cardinality** (Pylyshyn 1989 multi-object tracking K-slots; Treisman 1982 perceptual grouping K).

### §4.3 K_act: active formation count (dynamics-emergent)

$K_{\mathrm{act}}(t)$ = active formations at time $t$. Cognitive correlate: **gestalt fission/fusion** (perceptual binding with variable formation count over time).

### §4.4 K_step: observer artifact

$K_{\mathrm{step}}(u; \tau)$ = thresholding count. Cognitive correlate: **none** — observer-imposed measurement, not intrinsic to perceptual scene.

### §4.5 CN10 one-way mapping

Per Commitment 16 + Commitment 17 (proposed): SCC ontological flow은
$$u_t \to (K_{\mathrm{field}}, K_{\mathrm{act}}, \mathcal{F}_j) \to \text{cog-sci comparisons}.$$
역방향 forbidden. CN10 강화.

---

## §5. CN17 σ-Labeled Formation Quantization Strengthen

### §5.1 Current CN17 (canonical line 1572)

> "Formation Quantization is characterized by σ-signature (Commitment 14), refining the integer count $K_{\mathrm{step}}$ to a labeled tuple. The single-formation vs multi-formation distinction refines as follows: $\mathcal{F}=1$: single-mode (atomic-like; rare under full SCC by T-PreObj-1)..."

CN17 currently mentions $K_{\mathrm{step}}$ + $\mathcal{F}$; K (architecture index) 누락.

### §5.2 Proposed CN17+ (W6+ amendment)

```markdown
**CN17+. σ-Labeled Formation Quantization (W4 added 2026-04-25; W6+ extended).**

Formation Quantization is characterized by σ-signature (Commitment 14), refining 
the integer counts $\mathcal{F}$ (peak count, threshold-free) and $K_{\mathrm{step}}$ 
(connectivity, threshold-dependent) to labeled tuples. Multi-formation extension 
introduces additional integer diagnostics per Commitment 16:

- **$\mathcal{F}(u)$ (per-formation peak count)**: within-field internal multi-peak 
  structure. Threshold-free, USCO. Under full SCC, $\mathcal{F} \geq 2$ default 
  (T-PreObj-1 (i)).
- **$K_{\mathrm{step}}(u; \tau)$ (connectivity, threshold-dependent)**: 
  $K_{\mathrm{step}} \leq \mathcal{F}$ for all $\tau$.
- **$K_{\mathrm{act}}(\mathbf{u})$ (active formation count, derived diagnostic)**: 
  $K_{\mathrm{act}} \leq K_{\mathrm{field}}$.
- **$K_{\mathrm{field}}$ (architectural cap, modeling-layer commitment)** per 
  Commitment 16 (i).

The σ-tuple refinement applies at all four levels:
- Single-mode F=1 (atomic-like): rare under full SCC.
- Multi-mode F≥2 single-field (within-formation parts): T-PreObj-1 default ground 
  state. Cognitive correlate: object parts.
- Multi-field K-field (between-formation cardinality): K_field architectural 
  commitment. Cognitive correlate: multi-object scene.
- σ_multi^A multi-set under $S_{K_{\mathrm{act}}}$ permutation (D-6a CV-1.5.1 
  T-σ-multi-A-Static): joint invariant on K-field minimizer.

The four-quantity bridge (§3 of `working/MF/F_Kstep_K_triple.md` OAT-2):
$$K_{\mathrm{step}}(U^*; \tau) \leq \mathcal{F}(U^*) \quad\text{(single-field, all }\tau\text{)},$$
$$K_{\mathrm{act}}(\mathbf{u}) \leq K_{\mathrm{field}} \quad\text{(architectural)},$$
$$\mathcal{F}(U^*) = \sum_j \mathcal{F}(u^{(j)*}) \quad\text{(well-separated K-field)}.$$

CN10 one-way: $u_t \to (\mathcal{F}, K_{\mathrm{step}}, K_{\mathrm{act}}, K_{\mathrm{field}}) \to$ cog-sci comparisons.
```

---

## §6. Recommended Canonical Edits at CV-1.6 (D-CV1.6-O3 alongside)

### §6.1 New §5.5 derived diagnostic registration

Canonical §5 (Derived Geometric and Morphological Notions) 끝에 신규 subsection:

```markdown
### 5.5. Auxiliary Discrete Diagnostics (W6+ added 2026-04-30, CV-1.6 candidate)

Beyond the diagnostic vector $\mathbf{d} = (\mathsf{Bind}, \mathsf{Sep}, \mathsf{Inside}, \mathsf{Persist})$ 
(canonical §7.2), three integer diagnostics complement the σ-framework:

**$\mathcal{F}(u)$ (peak count, threshold-free)**:
$$\mathcal{F}(u) := \#\{x \in X : u(x) > u(y)\;\forall y \sim x\}$$
strict local maxima count over graph adjacency. USCO; Aut(G)-invariant. 
Under full SCC, $\mathcal{F} \geq 2$ default per T-PreObj-1 (i) Cat A 
graph-class independent.

**$K_{\mathrm{step}}(u; \tau)$ (connectivity, threshold-dependent)**:
$$K_{\mathrm{step}}(u; \tau) := \#\{\text{connected components of } \{u > \tau\} \text{ in } G\}.$$
Inequality: $K_{\mathrm{step}}(u; \tau) \leq \mathcal{F}(u)$ for any $\tau$.

**$K_{\mathrm{act}}(\mathbf{u})$ (active formation count, K-field)**:
$$K_{\mathrm{act}}(\mathbf{u}) := \#\{j : \|u^{(j)}\|_1 > \epsilon\}, \quad \epsilon = 0.01 \cdot \bar{m}.$$
Per Commitment 16, $K_{\mathrm{act}} \leq K_{\mathrm{field}}$.

These three diagnostics, together with the architectural cap $K_{\mathrm{field}}$ 
(Commitment 16), form the **quadruple count bridge** characterizing formation 
structure at all granularities. See CN17+ for σ-labeled quantization at each 
level. (Working file `F_Kstep_K_triple.md` OAT-2.)
```

### §6.2 CN17 amendment (per §5.2)

### §6.3 OP-0009-F status update

CV-1.6 시점 OP-0009-F: **PARTIALLY RESOLVED**. F as derived diagnostic registered (canonical §5.5); 4-quantity bridge §3.5 documented; CN17+ extended. Bridge conjecture BC-1 (per-formation F ↔ aggregate F lobes bijection) OAT-7 W6+ verification pending.

### §6.4 Net canonical impact

- Lines added: ~50-70 (§5.5 ~30 + CN17+ ~25 + OP status ~5).
- Predicate / energy 변경: 0 (CN10 maintain).
- Theorem status: 0 (no new theorem; F is *registered* not *proved*).

---

## §7. Tool A3 PH Connection

### §7.1 F ↔ $H_0$ persistent homology

Per OAT-supplementary §4 Tool A3:
- $K_{\mathrm{act}}(\mathbf{u}) = \dim H_0(R_r(\mathrm{centroids}(\mathbf{u})))$ at $r \to \infty$.
- $\mathcal{F}(u^{(j)})$ = number of $H_0$ classes in per-formation Vietoris-Rips when filtered by graph distance.
- Aggregate $\mathcal{F}(U^*) = \dim H_0(R_r(\{\text{peaks of } U^*\}))$ at $r \to \infty$.

→ F는 **persistent homology의 0차 invariant**. 4-quantity bridge가 PH 표준 framework로 reformulate됨.

### §7.2 K_step ↔ sublevel set persistent homology

$K_{\mathrm{step}}(u; \tau) = \dim H_0(\{u > \tau\})$ (sublevel set filtration).

$K_{\mathrm{step}}(u; \tau) \leq \mathcal{F}(u)$는 sublevel-set PH의 **standard inequality**: thresholding은 peak counts 줄임.

### §7.3 NQ-242 reframe consistency

OAT-supplementary §12.2: NQ-242 reframe as computational PH pipeline. F + K_step + K_act 모두 PH framework standard quantities. **이 4-quantity bridge가 NQ-242 numerical 작업의 정식 measurement targets**.

### §7.4 Superlevel Set Filtration PH Layer — F as #H_0 Generators (Wave 3 OAT-2 deepening, 2026-04-30)

> **Mission**: §7.1–§7.3는 F ↔ Vietoris-Rips PH on centroid point cloud을 다룬다. 본 subsection은 F를 *u 자체의 superlevel set filtration* 기반 H_0 invariant로 reformulate — Tool A3 PH layer의 *intrinsic field-level* 표현.

#### §7.4.1 Superlevel set filtration on graph

Given soft cohesion field $u : X \to [0,1]$ on graph $G = (X, E)$, define the **superlevel set filtration** indexed by $c \in [0, 1]$ in *decreasing* order:
$$U_c := \{x \in X : u(x) \geq c\}, \qquad U_{c_2} \subseteq U_{c_1} \quad (c_1 \leq c_2).$$

The induced subgraph $G|_{U_c} = (U_c, E \cap U_c \times U_c)$ is finite simplicial; its 0-th simplicial homology $H_0(G|_{U_c}; \mathbb{F})$ counts connected components of the threshold-$c$ superlevel set, with coefficients in field $\mathbb{F}$ (typically $\mathbb{F}_2$ for combinatorial efficiency).

The persistence module (descending parameter convention):
$$\mathbb{V}_*: H_0(G|_{U_{c_1}}) \to H_0(G|_{U_{c_2}}) \to \cdots \quad (c_1 > c_2 > \cdots),$$
where each map is induced by inclusion $U_{c_i} \supseteq U_{c_{i+1}}$. By the structure theorem for persistence modules over a field (Crawley-Boevey 2015 / Zomorodian-Carlsson 2005), $\mathbb{V}_*$ decomposes into interval modules — the **superlevel barcode** $\mathrm{Dgm}_0^{\sup}(u)$.

#### §7.4.2 Formal identity: F = number of H_0 generators *born* at strict local maxima

**Claim 7.4.2 (Wave 3 OAT-2 deepening)**: For graph $G$ with adjacency $\sim$ and field $u : X \to [0,1]$ in generic position (distinct values at neighbors of each strict local max),
$$\mathcal{F}(u) \;=\; \#\big\{\text{intervals in } \mathrm{Dgm}_0^{\sup}(u) \text{ born at } c = u(x_*) \text{ for some } x_* \text{ strict local max}\big\}.$$

**Equivalently**, F equals the number of H_0 generators introduced (as new bars) by the superlevel set filtration over the entire range $c \in [0, 1]$:
$$\mathcal{F}(u) = \sum_{c \in [0,1]} \big[ \dim H_0(G|_{U_{c^-}}) - \dim H_0(G|_{U_{c^+}}) \big]_+$$
(positive part of H_0 jumps under descending $c$).

**Proof sketch**:
- (⊇) Each strict local max $x_* \in X$ (with $u(x_*) > u(y)$ for $y \sim x_*$) births a new H_0 class at $c = u(x_*)$: at $c^+ = u(x_*) + \delta$ the site $x_*$ is excluded; at $c^- = u(x_*) - \delta$ for small $\delta > 0$, $x_*$ enters $U_{c^-}$. By the strict local max property, $x_*$ has *no* neighbor in $U_{c^-}$ (since all neighbors $y$ have $u(y) < u(x_*)$, hence $u(y) < c$ for sufficiently small $\delta$). Thus $\{x_*\}$ is a *new* connected component — fresh H_0 generator. ✓
- (⊆) Conversely, any new H_0 class born at parameter $c^*$ corresponds to a site $x_*$ entering $U_{c^*}$ that has no neighbor already in $U_{c^*}$. This forces $u(y) < u(x_*)$ for all $y \sim x_*$, i.e., $x_*$ is a strict local max. ✓
- Generic position (distinct neighbor values) ensures no ties; for non-generic $u$, infinitesimal perturbation (PH stability §7.4.4) provides the counting reading. ✓

**Cross-reference**: This identity is the *intrinsic* (field-level) version of `mathematical_scaffolding_4tools.md` §4 Tool A3 Claim 4.2(iv), which states $K_{\mathrm{act}}$ corresponds to centroid PH $H_0$ at $r = \infty$. Here the PH lives directly on $X$ via $u$, no centroid abstraction needed.

#### §7.4.3 K_step as superlevel H_0 at fixed threshold

The threshold-dependent diagnostic $K_{\mathrm{step}}(u; \tau)$ corresponds to a **single slice** of the superlevel filtration:
$$K_{\mathrm{step}}(u; \tau) = \dim H_0\big(G|_{\{u > \tau\}}\big) \;=\; \dim H_0(G|_{U_{\tau + 0^+}}).$$

The inequality $K_{\mathrm{step}}(u; \tau) \leq \mathcal{F}(u)$ for all $\tau$ (canonical §12 line 832) is now reread as the *standard* PH fact: the number of H_0 generators *alive at parameter* $\tau$ is at most the total number of H_0 generators ever born. Equality holds iff no merge events occurred above $\tau$.

#### §7.4.4 Stability under perturbation

By Cohen-Steiner-Edelsbrunner-Harer 2007 (stability of persistence diagrams):
$$d_B\big(\mathrm{Dgm}_0^{\sup}(u), \mathrm{Dgm}_0^{\sup}(u')\big) \leq \|u - u'\|_\infty.$$

**Corollary**: $\mathcal{F}$ is *upper semi-continuous* (USCO, already noted §2.1): $u_n \to u$ in $L^\infty$ implies $\mathcal{F}(u) \geq \limsup \mathcal{F}(u_n)$ — peaks may *merge* under perturbation (births coalesce) but cannot *spawn* without perturbation magnitude exceeding the smallest peak prominence. **Peak prominence** $\mathrm{prom}(x_*) := u(x_*) - \max\{c : x_* \text{ in same component as a higher-valued site at parameter } c\}$ is exactly the *bar length* of the H_0 generator born at $x_*$.

**Implication for R23 ground-state F = 9**: each of the 9 peaks has a well-defined prominence (bar length) in $\mathrm{Dgm}_0^{\sup}(u^*)$. Robustness of F = 9 against $L^\infty$-perturbations of magnitude $< \min_i \mathrm{prom}(x_{*,i})$ is automatic from CSEH stability. Empirical numerics on 56 R23 minimizers (`single_high_F_equivalence.md`) provide the prominence distribution.

#### §7.4.5 K_field architectural cap as PH-free invariant

In contrast to F and K_step (both PH-derivable), $K_{\mathrm{field}}$ (Commitment 16, modeling-layer cap) is *not* a PH invariant of any single field $u$ or aggregate $U^*$; it is a *parameter of the model space* $\widetilde\Sigma^K_M$. PH operates *within* a chosen $K_{\mathrm{field}}$ architecture; the architecture itself is exterior to the PH framework. This *layer-distinction*:

| Quantity | PH realization | Layer |
|---|---|---|
| $\mathcal{F}(u)$ | $\#$ H_0 generators in $\mathrm{Dgm}_0^{\sup}(u)$ | field-level (intrinsic) |
| $K_{\mathrm{step}}(u;\tau)$ | $\dim H_0(G\|_{U_\tau})$ | field-level (sliced) |
| $K_{\mathrm{act}}(\mathbf{u})$ | $\dim H_0(R_\infty(C(t)))$ centroid PH | trajectory/configuration-level |
| $K_{\mathrm{field}}$ | (none — parameter, not invariant) | architectural-layer (modeling) |

confirms the four-quantity bridge §3.5 as a *layered PH hierarchy*: three of four quantities have direct PH realizations; the fourth ($K_{\mathrm{field}}$) is the modeling-layer scaffold within which the other three are computed. Per `lambda_rep_ontology.md` §2.2 Argument B (architectural-layer coupling), λ_rep belongs to the same architectural layer as $K_{\mathrm{field}}$ — *not* a PH invariant of the field, but a parameter of the model.

#### §7.4.6 Cross-reference to mathematical_scaffolding_4tools.md Tool A3

This subsection deepens `mathematical_scaffolding_4tools.md` §4 Tool A3 in two specific directions:

1. **§4.1 (centroid Vietoris-Rips PH)** is augmented by the **superlevel set filtration** picture (this §7.4) — providing an *intrinsic* (no centroid abstraction) realization of F. The two PH constructions are *complementary*: superlevel handles within-field peak structure; centroid VR handles between-formation cardinality.
2. **§4.2 Claim 4.2 (identification with σ_multi^A)** is strengthened: per-formation $\mathcal{F}(u^{(j)})$ now realized as superlevel barcode of $u^{(j)}$ alone; aggregate $\mathcal{F}(U^*)$ as superlevel barcode of $U^*$ — both *standard* PH constructions, library-supported (GUDHI `CubicalPersistence` for grid graphs; `SimplexTree` for general graphs).

The NQ-242 computational pipeline (`mathematical_scaffolding_4tools.md` §12.2) gains an additional measurement target: **superlevel barcode prominence distribution** of R23 minimizers as a fingerprint of the F = 9 ground-state regime.

#### §7.4.7 Hard constraint check (this subsection)

- [x] u_t primitive maintained: PH operates on u directly; F is a derived diagnostic of u.
- [x] Canonical 0-edit: this is `working/MF/`. Promotion target unchanged (CV-1.6 §5.5 derived diagnostics).
- [x] CN10 contrastive: superlevel set PH is *standard import* from computational topology (Edelsbrunner-Harer 2010); SCC F is *defined* combinatorially (§2.1); the identity §7.4.2 is a *correspondence*, not a reductive identification.
- [x] CN5 4-energy not merged: PH is a measurement layer on minimizers, orthogonal to the four energy terms.
- [x] No silent OP resolution: OP-0009-F status remains **PARTIALLY RESOLVED** (BC-1 well-separated valid, generic rejected — §3.6); §7.4 adds intrinsic PH realization but does not close the bijection question.

---

## §8. Open Questions

### §8.1 Bridge conjecture BC-1 (OAT-7 verification)

Per-formation $\{u^{(j)*}\}$ ↔ aggregate $\mathrm{lobes}(U^*)$ bijection at well-separated regime: **OAT-7 R23 F=9 ↔ K=9 K-field equivalence test**.

### §8.2 Overlapping regime F bridge

T-Persist-K-Weak overlap regime에서 $\mathcal{F}(U^*) \leq \sum_j \mathcal{F}(u^{(j)*})$: equality 조건은? Boundary peak coincidence가 strict inequality 발생 케이스. NQ-242 numerical measurement.

### §8.3 K-jump ↔ F changes

K-jump 시점 ($K_{\mathrm{act}}$ decreases by 1) → $\mathcal{F}(U^*)$ 변화? Merger event에서 두 peak이 합쳐져 single peak (F 감소 1) vs 두 peak 보존 (F unchanged). σ^A K-jump non-determinism (OP-0008)이 F-side에도 발생 가능?

### §8.4 Continuum limit

Discrete graph adjacency $\sim$를 continuum limit (graph spacing $h \to 0$)에서 $\mathcal{F}$ 정의는? Standard local maximum on continuous domain. Continuum limit OP-0022 (LOW priority) 영역.

---

## §9. External References

- T-PreObj-1 (canonical §13 line 1044-1064): F definition + F ≥ 2 default theorem.
- canonical §12 line 827-832 (W4 04-24): F vs K_step duality original.
- CN17 (canonical §14 line 1572): σ-Labeled FQ original.
- Edelsbrunner-Harer 2010 *Computational Topology: An Introduction* — sublevel set PH.
- Cohen-Steiner et al. 2007 — PH stability.
- Pylyshyn 1989 *Cognition* — multi-object tracking K-slots.
- Treisman 1982 *J. Exp. Psychol.* — perceptual grouping.

---

## §10. Hard Constraint Verification

- [x] canonical 직접 수정 0.
- [x] Silent resolution 0: OP-0009-F PARTIALLY RESOLVED (BC-1 verification pending OAT-7).
- [x] u_t primitive maintained: F is derived from u (counting local maxima).
- [x] 4-energy not merged.
- [x] CN10 contrastive: cognitive correlates 명시적으로 *downstream comparisons*.
- [x] K_field/K_act/F/K_step 4-quantity 모두 derived 또는 modeling-layer (none primitive).

---

## §11. Cross-References

- `K_status_commitment.md` (OAT-1 CV-1.5.1): K_field/K_act 정의.
- `mathematical_scaffolding_4tools.md` §3 (Tool A2 quotient) + §4 (Tool A3 PH).
- `cobelonging_vs_sigmaD.md` (OAT-5): σ_multi^D vs C_t orthogonality.
- `lambda_rep_ontology.md` (OAT-3): λ_rep architectural-layer parameter.
- `pre_objective_K_field_tension.md` (OAT-6): pre-objective + K-field tension.
- canonical §3 (formal universe modeling-layer note); §5 (derived notions); §12 line 827-832 (F/K_step duality); §14 CN17 (σ-Labeled FQ).
- daily/2026-04-30/02_4tool_mapping_summary.md (4-tool 결과).

---

## §12. Recommendation Summary

**Recommendation**: APPROVE F derived diagnostic registration (canonical §5.5 신규) + CN17+ amendment + OP-0009-F status update at CV-1.6 D-CV1.6-O3.

**Effort**: ~50-70 canonical lines.

**Net effect**:
- F as derived diagnostic 명시 — T-PreObj-1 inline definition을 §5 derived diagnostics block로 promote.
- 4-quantity bridge documentation: CN17 strengthen + §5.5 신규.
- Cognitive correlate distinction: CN10 강화 (within-formation parts vs scene cardinality vs observer artifact).
- Tool A3 PH connection: NQ-242 numerical work이 F + K_step + K_act 모두 standard PH measurements.

**Pending**: BC-1 (per-formation F ↔ aggregate F lobes bijection) OAT-7 W6+ verification.

---

**End of F_Kstep_K_triple.md (OAT-2 deliverable).**
**Status: working draft. F as derived diagnostic register at canonical §5.5; CN17+ amendment; 4-quantity inequality bridge documented; Tool A3 PH connection (now extended with superlevel-filtration intrinsic PH layer §7.4 per Wave 3 OAT-2 deepening). OP-0009-F PARTIALLY RESOLVED at CV-1.6.**
**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/F_Kstep_K_triple.md`
**Created:** 2026-04-30 (W5 Day 4 morning, OAT-2 advanced from W6 Day 1).
**Promotion target:** CV-1.6 W6 Day 7 morning (D-CV1.6-O3 candidate).

---

## §13. Wave 3 Revision Log

### 2026-04-30 — Wave 3 OAT Deepening Team (worker-1, Task 1 Subtask A)

**Context**: Wave 3 OAT deepening team work (`.omc/state/team/wave-3-oat-deepening-team-work/`, claim_token `7ec973d4-…`); 3-worker team executing Ontological Audit Track deepening on `working/MF/` files; NO canonical edits; hard constraints u_t primitive + CN10 contrastive + CN5 4-energy not merged + CV-1.6 D-items as targets.

**Changes (this revision)**:
1. **New §7.4 — Superlevel Set Filtration PH Layer** (+~95 lines): introduces the *intrinsic* (field-level, no centroid abstraction) PH realization of F via the superlevel set filtration $U_c = \{x : u(x) \geq c\}$ on graph $G$. Subsections §7.4.1–§7.4.7 cover (a) graph superlevel filtration setup, (b) formal identity $\mathcal{F}(u) = \#$ H_0 generators born at strict local maxima with proof sketch, (c) K_step as single-slice H_0, (d) Cohen-Steiner-Edelsbrunner-Harer stability + peak prominence ↔ bar length, (e) layer-distinction table (F, K_step, K_act = PH-derivable; K_field = architectural / PH-free), (f) cross-reference to `mathematical_scaffolding_4tools.md` §4 Tool A3 deepening (centroid VR + superlevel as complementary PH), (g) hard-constraint verification checklist.
2. **§12 status line updated**: now records the §7.4 superlevel-filtration extension within the OAT-2 deliverable summary.
3. **R23 fingerprint connection**: §7.4.4 establishes that the F = 9 ground-state regime in R23 minimizers (`single_high_F_equivalence.md`) admits a *prominence distribution* fingerprint — an additional NQ-242 measurement target beyond per-formation Hessian σ-tuples.

**No canonical edits made**; CV-1.6 promotion target (§5.5 derived diagnostics) unchanged. OP-0009-F remains PARTIALLY RESOLVED. Cross-file consistency with `mathematical_scaffolding_4tools.md` Tool A3 explicitly documented in §7.4.6.
