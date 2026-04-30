# lambda_rep_ontology.md — λ_rep의 Ontological Status Audit (5-term vs Architectural Coupling vs Simplex Lagrange)

**Status:** working draft (OAT-3 spawn 2026-04-30 W5 Day 4 morning; post OAT-supplementary `mathematical_scaffolding_4tools.md` Tool A4 partial-fail finding).
**Type:** Theory-only audit (no canonical edits, no compute). Targets CV-1.6 user-decision packet item D-CV1.6-O3.
**Last touched:** 2026-04-30
**Author origin:** OAT-supplementary §5.4 verification에서 SCC bilinear $\sum_{j<k} \lambda_{\mathrm{rep}} \langle u^j, u^k \rangle$ ≠ KKT Lagrange multiplier 정확 일치임을 발견. 4-에이전트 ontological depth analysis (W5 Day 3 EOD) OP-0009-λ 등록 후 후속 작업.
**Canonical refs:** §11 I9 (K-field architecture, line 846 — λ_rep 첫 등장); §14 CN5 (4-term independence, line 1530); §14 CN10 (contrastive vs reductive, line 1546); §11.1 #1 (Commitment 1 u_t primitive); §11.1 #14 / #14-Multi (σ-signature single + multi); §11.1 #16 (K-status two-tier, CV-1.5.1).
**Working refs:** `mathematical_scaffolding_4tools.md` §5.1–§5.6 (Tool A4 partial verification), `K_status_commitment.md` (OAT-1 sister; K_field/K_act decomposition), `multi_formation_sigma.md` §6.1 (N-1 integer K commitment), `sigma_multi_trajectory.md` §2 (K-jump dynamics).
**Open problems:** OP-0009-λ (this file's resolution candidate); OP-0009 parent (Multi-Formation Ontological Foundations 7 sub-items); OP-0008 σ^A K-jump non-determinism (orthogonal — λ_rep ontology resolution not required for OP-0008 status).

---

## §1. Mission Statement

> **"λ_rep $\langle u^j, u^k \rangle$ (the inter-field repulsion bilinear in K-field architecture I9, canonical line 846) — multi-formation σ-framework에서 ontologically 무엇인가? CN5 (4-term independence) 약속과의 관계는?"**

세 candidate 답:

- **Argument A** — λ_rep는 **5번째 conceptually independent term**. CN5 4-term 약속을 multi-formation에서 5-term 약속으로 확장 (CN5+).
- **Argument B** — λ_rep는 **architectural-layer coupling parameter**. CN5 4-term 약속은 single-formation 보존; multi-formation bilinear은 *between-formation interaction* 별 ontological category. CN5+ 신설 안 함.
- **Argument C** — λ_rep는 **simplex constraint $\sum_k u^{(k)}(x) \leq 1$ KKT Lagrange multiplier의 (smooth) realization**. λ_rep 자체는 ontologically 새로운 게 아니라 hard constraint의 soft enforcement.

본 audit은 OAT-supplementary §5.4 verification 결과를 정밀화한다. **결론(요약): Argument C strict version은 verification fail. Argument A는 CN5 약속 위반 (4-term independence가 multi-formation에서 어떤 의미로 보존되는지 새로 논증 필요). Argument B (architectural coupling) + CN10 contrastive comparison이 가장 honest. CN5 amendment는 "single-formation 약속" 명시화로 충분 — 5-term 약속 신설 안 함.**

---

## §2. Three Arguments — Detailed Inventory

### §2.1 Argument A: λ_rep as 5th Conceptually Independent Term (CN5 → CN5+)

**Thesis**: Multi-formation extension에서 λ_rep $\langle u^j, u^k \rangle$은 closure / separation / boundary / transport와 동격의 *5th structural requirement*. CN5의 "4 logically independent structural requirements" 약속을 5-term 약속으로 확장.

**Formal claim** (proposed canonical wording):
> "CN5+ (Multi-formation amendment). The K-field architecture energy comprises five conceptually independent terms — closure, separation, boundary/morphology, transport, and **inter-formation repulsion**. Inter-formation repulsion encodes the structural requirement that distinct formations occupy distinct support regions; it is logically independent of the four single-formation terms."

**Supporting considerations**:
- 다른 4 term은 *within-formation* structural requirement. λ_rep은 *between-formation* — 추상 수준 동급 가능성.
- Independence 검증: 4 term 중 어느 것도 λ_rep을 implies하지 않음 (각 term을 0으로 두고 λ_rep 항만 nonzero인 K-field minimizer가 존재 가능 — *separate* but coexisting bumps 형성).
- σ-framework에서 σ^A K-jump trajectory는 λ_rep 직접 의존 (well-separated → weakly-interacting → strongly-interacting regime이 정확히 $\Lambda_{\mathrm{coupling}} = \lambda_{\mathrm{rep}} \cdot \omega_{jk} / \min(\mu_j, \mu_k)$로 매개되며, T-Persist-K-Unified가 명시).

**Objections** (Critic-flag):
- **CN5 약속의 *minimal* 의미 약화**: "minimal 4-term"이 multi-formation에서 "minimal 5-term"으로 변하면 *minimality*는 multi-formation context-dependent, 즉 약속의 단단함이 약해짐.
- **K=1 시 vacuous**: K=1 single-formation 시 λ_rep 항이 자동 0 ($\sum_{j<k}$ empty sum). 즉 5번째 term은 *K=1 시 사라지는* term — 다른 4 term은 K=1에서도 살아있음. 비대칭 ontological status.
- **Term 수 inflation 위험**: K_step transition energy, σ-tuple discrete action 등 "추가 K-dependent term" 후보가 다수. 모두 5번째, 6번째…로 격상하면 minimal 약속 무의미.

**Verdict**: Argument A는 *form*은 가능하지만 CN5 약속의 minimal-structure 정신을 훼손. **Not recommended**.

### §2.2 Argument B: λ_rep as Architectural-Layer Coupling Parameter

**Thesis**: λ_rep은 **K-field architecture I9의 추가 구조** (additional structure)이며, CN5 4-term은 *within-formation* (per-formation $\mathcal{E}_{\mathrm{self}}(u^{(k)})$)에서 보존. *Between-formation* coupling은 4-term의 generalization이 아닌 *architectural-layer* parameter — `K_field` integer cap (Commitment 16 modeling-layer commitment)와 같은 layer.

**Formal claim** (proposed CN5 amendment, minimal):
> "CN5 (W6+ amended). The four energy terms — closure, separation, boundary/morphology, transport — address four logically independent structural requirements **at the single-formation level** $\mathcal{E}_{\mathrm{self}}(u)$. Multi-formation extension via K-field architecture (Pillar I9) introduces between-formation bilinear coupling $\sum_{j<k} \lambda_{\mathrm{rep}} \langle u^j, u^k \rangle$; this coupling is *between-formation interaction* (architectural-layer parameter, parallel to $K_{\mathrm{field}}$ modeling-layer commitment per Commitment 16), not a 5th conceptually independent term and not a within-formation structural requirement. The four-term independence claim therefore extends to multi-formation as: each $\mathcal{E}_{\mathrm{self}}(u^{(k)})$ retains four-term independence; between-formation coupling is a separate ontological category."

**Supporting considerations**:
- Commitment 16 (CV-1.5.1)이 K를 K_field (modeling-layer commitment) + K_act (derived diagnostic) 분리 — 동일한 layer-distinction logic을 λ_rep에도 적용 자연스러움.
- λ_rep는 K=1 시 vacuous (Argument A objection 2와 같은 관찰)이지만, *architectural-layer parameter*이면 K=1 architecture에서 λ_rep 자체가 정의되지 않음 (architecture는 K_field=1로 설정됨; coupling 개념 없음). 비대칭이 *natural*.
- CN10 contrastive와 양립: Standard N-phase Allen-Cahn (Garcke-Nestler-Stoth 1999, Garcia Trillos-Murray 2017)에 *비교*는 가능하지만 *동일시*는 아님. *(Citations corrected per external references audit 2026-04-30.)*

**Objections**:
- "Architectural-layer parameter"의 정확한 ontological 위치가 어디인가? K_field는 modeling-layer commitment (Commitment 16). λ_rep도 같은 layer? 그렇다면 λ_rep도 modeler가 *외적으로* 설정 — 그러나 CN6 ("K kinetically determined") 정신은 K가 dynamics에서 emerge한다는 것. λ_rep는 *parameter*이지 *dynamic outcome*이 아님 — Commitment 16과 정합 (parameter ≠ derived).
- ⚠️ Architectural-layer는 *u_t primitive와 분리된 추가 layer*. Commitment 1 ("u_t sole primitive")가 이미 multi-formation에서 약화되어 있음 (K-field $u^1, \ldots, u^K$가 K개 primitive 카운트?). 이는 OAT-6 (Pre-objective + K-field tension) 영역; 본 audit 범위 밖이지만 *flag*.

**Verdict**: Argument B는 가장 conservative하고 CN5 minimal 약속을 보존. **Recommended (preferred direction)**.

### §2.3 Argument C: λ_rep as Simplex Constraint KKT Lagrange Multiplier (smooth realization)

**Thesis**: K-field architecture는 simplex inequality constraint $\sum_k u^{(k)}(x) \leq 1\;\forall x$를 가짐. λ_rep $\langle u^j, u^k \rangle$ 항은 이 constraint의 KKT Lagrange multiplier $\mu(x) \geq 0$의 *smooth (quadratic) realization*. λ_rep 자체는 ontologically 새로운 entity가 아니라 hard constraint의 soft penalty.

**Formal claim** (strict version, would-be canonical):
> "λ_rep coupling is a smooth realization of the simplex constraint Lagrange multiplier. The KKT optimality condition for $\sum_k u^{(k)}(x) \leq 1$ is recovered in the limit $\lambda_{\mathrm{rep}} \to \infty$."

**Supporting considerations**:
- Simplex constraint는 분명 *active* — particle conservation + non-overlap의 자연 표현.
- Quadratic penalty $\lambda_{\mathrm{rep}} \langle u^j, u^k \rangle$ 형태가 augmented Lagrangian (Powell 1969 / Hestenes 1969 / Rockafellar 1973)와 형식 유사.
- 만약 strict version이 성립하면, λ_rep은 새로운 ontological category 아님 — 이미 약속된 simplex constraint의 *technical realization*. CN5 4-term 약속에 추가 신설 불필요.

**⚠️ CRITICAL FAILURE — verification (per OAT-supplementary §5.4)**:

Strict KKT identification fails. 정밀 분석:

(i) **KKT setup for inequality constraint**: 
Lagrangian $\mathcal{L}(\mathbf{u}, \mu) = \mathcal{E}_K(\mathbf{u}) + \sum_x \mu(x) \big( \sum_k u^{(k)}(x) - 1 \big)$
with KKT conditions:
- Primal feasibility: $\sum_k u^{(k)}(x) \leq 1\;\forall x$.
- Dual feasibility: $\mu(x) \geq 0\;\forall x$.
- Complementary slackness: $\mu(x) \cdot (\sum_k u^{(k)}(x) - 1) = 0\;\forall x$.
- Stationarity: $\partial \mathcal{L}/\partial u^{(j)}(x) = 0\;\forall j, x$.

(ii) **Stationarity gradient**:
$$\frac{\partial \mathcal{L}}{\partial u^{(j)}(x)} = \frac{\partial \mathcal{E}_K}{\partial u^{(j)}(x)} + \mu(x) = 0.$$

(iii) **SCC bilinear gradient**:
$$\frac{\partial}{\partial u^{(j)}(x)} \Big( \sum_{k<\ell} \lambda_{\mathrm{rep}} \sum_y u^{(k)}(y) u^{(\ell)}(y) \Big) = \lambda_{\mathrm{rep}} \sum_{k \neq j} u^{(k)}(x).$$
(For each pair $(j, k)$ with $k \neq j$: derivative contributes $\lambda_{\mathrm{rep}} u^{(k)}(x)$.)

(iv) **Identification attempt**: SCC stationarity (without additional Lagrange term) reads
$$\frac{\partial \mathcal{E}_{\mathrm{self}}(u^{(j)})}{\partial u^{(j)}(x)} + \lambda_{\mathrm{rep}} \sum_{k \neq j} u^{(k)}(x) = 0.$$
KKT version with simplex enforcement reads
$$\frac{\partial \mathcal{E}_{\mathrm{self}}(u^{(j)})}{\partial u^{(j)}(x)} + \mu(x) = 0.$$

(v) **Exact identification 요구**: $\lambda_{\mathrm{rep}} \sum_{k \neq j} u^{(k)}(x) \stackrel{?}{=} \mu(x)\;\forall j, x$. RHS는 $j$에 *독립* (single function of $x$); LHS는 $j$에 *의존* — 정확히는 $\sum_{k \neq j} u^{(k)}(x) = \big(\sum_k u^{(k)}(x)\big) - u^{(j)}(x)$. **불일치**: $\mu(x)$가 $j$-independent인 반면 LHS에는 $u^{(j)}(x)$ subtraction 있음.

**Conclusion**: Strict KKT identification fails. Argument C strict version은 verification reject. ⚠️ **PARTIAL FAIL** confirmed (per OAT-supplementary §5.4).

**Salvage attempts**:

- **C′ (augmented Lagrangian)**: λ_rep을 quadratic penalty in Powell-Hestenes-Rockafellar augmented Lagrangian framework로 reframe. PHR 정식: $\mathcal{L}_\rho(\mathbf{u}, \mu) = \mathcal{E}_K + \sum_x \big[ \mu(x) g(x) + (\rho/2) g(x)^2 \big]$ where $g(x) = \sum_k u^{(k)}(x) - 1$. Quadratic penalty $(\rho/2) g(x)^2 = (\rho/2) \big(\sum_k u^{(k)}(x) - 1\big)^2$ expanded는 $\sum_{j,k} u^{(j)}(x) u^{(k)}(x) - 2 \sum_k u^{(k)}(x) + 1$. **Cross-term** $\sum_{j \neq k} u^{(j)}(x) u^{(k)}(x) = 2 \sum_{j<k} u^{(j)}(x) u^{(k)}(x)$ — 형식상 SCC bilinear와 *닮음* but 추가로 *diagonal* terms $\sum_k u^{(k)}(x)^2$ + linear term $-2 \sum_k u^{(k)}(x)$ 존재. SCC formulation에는 이 추가 항 없음. **불완전 매칭**. PHR multiplier theory 추가 도입 필요하지만 정확한 SCC 표현이 standard PHR이 *아님*.
- **C″ (interior-penalty / barrier method)**: λ_rep을 barrier function의 quadratic approximation. Barrier methods (interior-point) 표준은 logarithmic barrier $-\log(1 - \sum_k u^{(k)}(x))$; quadratic는 *outer* penalty (보통 augmented Lagrangian) 또는 *exterior* barrier. SCC bilinear은 *exterior* — feasibility region 내부에서도 cost 가짐. Standard barrier method와 매칭 안 됨.

**Verdict**: Argument C는 strict version + salvage 모두 verification fail. **Most honest position**: λ_rep는 simplex constraint와 *관련*되지만 Lagrange multiplier identification은 *exact reduction이 아님* (CN10 contrastive). **C strict 채택 안 함**.

### §2.4 Argument B Deepened — Architectural-Layer Theory (Wave 3 OAT-3 deepening, 2026-04-30)

> **Mission of this subsection**: §2.2 establishes Argument B (architectural-layer coupling) at the *thesis* level and flags two objections (Q1 architectural-layer placement; Q2 u_t primitive tension). Wave 3 OAT-3 deepening provides (a) a *formal definition* of "architectural layer", (b) the exact placement of λ_rep within the SCC layer hierarchy, (c) explicit address of both objections, (d) Tool A1 stratified-space connection, and (e) cross-reference to the F_Kstep_K_triple §7.4.5 layer-distinction table.

#### §2.4.1 Formal definition: SCC layer hierarchy

Distinguish four layers in the multi-formation SCC framework, ranked by ontological primacy (top = most primitive):

| Layer | Members | Status |
|---|---|---|
| **L0 Primitive** | $u_t : X_t \to [0,1]$ (Commitment 1); the soft cohesion field itself | Sole ontological primitive of $\mathfrak{C}^{\mathrm{soft}}$ |
| **L1 Field-derived (intrinsic)** | $\mathcal{F}(u)$, $K_{\mathrm{step}}(u; \tau)$, $\mathcal{E}_{\mathrm{self}}(u)$, $\mathbf{d} = (\mathsf{Bind}, \mathsf{Sep}, \mathsf{Inside}, \mathsf{Persist})$ | Functions of L0; computable from a single $u$ snapshot or its trajectory; CN10-compliant intrinsic measurements |
| **L2 Configuration / trajectory-level** | $K_{\mathrm{act}}(\mathbf{u})$, $\sigma_{\mathrm{multi}}^A(t)$, $\sigma_{\mathrm{multi}}^D$, K-jump events | Functions of L0-tuples or L0-flows; emergent from dynamics on a chosen architecture |
| **L3 Architectural-layer / modeling commitments** | $K_{\mathrm{field}}$ (Commitment 16(i)), $\lambda_{\mathrm{rep}}$, energy weights $(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}})$, choice of $X_t$ structure | *Set ex ante* by modeler; not derived from any $u_t$; parametrize the model space within which L0–L2 live |

**Formal definition (architectural layer L3)**: A quantity $q$ belongs to the **architectural layer** iff
1. $q$ is independent of any specific $u_t \in \mathfrak{C}^{\mathrm{soft}}$ (not a function of L0 or L1/L2 derivatives), AND
2. $q$ is a parameter of the model space (energy functional, configuration manifold, or graph structure) within which L0–L2 quantities are computed, AND
3. $q$ is *fixed by modeler commitment* (per Commitment 16 modeling-layer note for $K_{\mathrm{field}}$; per canonical I9 for λ_rep) prior to dynamical evolution.

#### §2.4.2 Formal Claim B1: λ_rep ∈ L3 architectural layer

**Claim B1 (Wave 3 OAT-3)**: $\lambda_{\mathrm{rep}}$ satisfies all three conditions of the L3 architectural-layer definition (§2.4.1).

**Verification**:
1. **Independence from $u_t$**: $\lambda_{\mathrm{rep}} \in \mathbb{R}_{\geq 0}$ is a scalar parameter; the value of $\lambda_{\mathrm{rep}}$ is not extracted from any $u^{(j)}$ field but is *prescribed* in the K-field architecture I9 (canonical line 846). Differentiating: $\lambda_{\mathrm{rep}}$ is *not* a function of $\mathbf{u}$. ✓
2. **Parameter of model space**: $\lambda_{\mathrm{rep}}$ enters $\mathcal{E}_K(\mathbf{u}) = \sum_k \mathcal{E}_{\mathrm{self}}(u^{(k)}) + \sum_{j<k} \lambda_{\mathrm{rep}} \langle u^j, u^k \rangle$ as the *coefficient of the inter-formation bilinear*. Different choices of $\lambda_{\mathrm{rep}}$ yield different energy landscapes on the *same* configuration space $\widetilde\Sigma^K_M$ — exactly the role of a model-space parameter. ✓
3. **Modeler commitment**: $\lambda_{\mathrm{rep}}$ is fixed before dynamical evolution; no adaptive update during gradient flow; not derived from observed data of a single $u$. (Empirically swept in V5b experiments via the regime parameter $\Lambda_{\mathrm{coupling}} = \lambda_{\mathrm{rep}} \cdot \omega_{jk} / \min(\mu_j, \mu_k)$; sweep is over *modeler choices*.) ✓

**Conclusion B1**: $\lambda_{\mathrm{rep}} \in $ L3 architectural layer, alongside $K_{\mathrm{field}}$ and the four single-formation energy weights. ✓

#### §2.4.3 Formal Claim B2: λ_rep ≠ a 5th L0/L1 within-formation term (CN5 minimal preserved)

**Claim B2**: $\lambda_{\mathrm{rep}} \langle u^j, u^k \rangle$ is *not* a 5th conceptually independent within-formation energy term and *not* an L1 field-derived diagnostic. Hence CN5's "four logically independent structural requirements" promise — interpreted as *single-formation L1-level* claim per §5.1 amendment — is preserved unweakened.

**Verification**:
- **Not within-formation**: the bilinear $\langle u^j, u^k \rangle$ requires *two* distinct formation indices $j \neq k$; for any single fixed formation $u^{(k)}$ in isolation, the bilinear contribution is identically zero (no self-pair). Within-formation energy $\mathcal{E}_{\mathrm{self}}(u^{(k)})$ remains the four canonical terms. ✓
- **K=1 vacuity is *natural* under L3 reading** (resolves §2.2 Critic-flag objection 2): when $K_{\mathrm{field}} = 1$ the *architecture itself* admits no inter-formation pairs ($\sum_{j<k}$ empty); λ_rep is *undefined* (or trivially absent) as a model-space parameter. This is the same naturalness as: in single-formation architecture, the parameter $K_{\mathrm{field}}$ has the trivial value 1 — both architectural-layer parameters degenerate together. The K=1 "asymmetric ontological status" (Argument A objection 2) is therefore *not* a defect of Argument B but a structural feature of L3 layer membership. ✓
- **Term-inflation risk addressed**: any candidate "5th term" must qualify as *within-formation L1* (function of single $u$) AND structurally independent from the four canonical terms. Bilinear $\langle u^j, u^k \rangle$ fails the within-formation test by construction. K_step transition energy and σ-tuple discrete action are L2 trajectory-level (not L1); they do not threaten CN5 minimal-structure either. ✓

**Conclusion B2**: CN5 four-term minimality is *single-formation L1* invariant; multi-formation extension preserves it without amendment to the count. ✓

#### §2.4.4 Formal Claim B3: u_t primitive (Commitment 1) preserved (resolves §2.2 objection 2)

**Claim B3** (addresses §2.2 Critic-flag Q2: "Commitment 1 'u_t sole primitive' weakened in multi-formation?"): Commitment 1 holds *unweakened* — the sole L0 primitive is $u_t$, with the multi-formation extension corresponding to $K_{\mathrm{field}}$ *replicas* of L0, not $K_{\mathrm{field}}$ *additional* primitives.

**Verification**:
- The K-field configuration $\mathbf{u} = (u^{(1)}, \ldots, u^{(K_{\mathrm{field}})})$ consists of $K_{\mathrm{field}}$ instances of *the same primitive type* (each $u^{(j)} : X_t \to [0,1]$ is a soft cohesion field per Commitment 1).
- The architectural-layer commitment $K_{\mathrm{field}}$ specifies *how many copies* the model employs; it does not introduce a new primitive type.
- λ_rep parametrizes the *interaction energy among copies*, not the copies themselves; it is a *coupling parameter on L0 instances*, sitting at L3.
- Under the symmetric-group quotient picture (Tool A2; `mathematical_scaffolding_4tools.md` §3): the *unordered* configuration $\widetilde{\widetilde\Sigma}^K_M = \widetilde\Sigma^K_M / S_{K_{\mathrm{field}}}$ is ontologically primary; ordered labels $j = 1, \ldots, K_{\mathrm{field}}$ are L3 modeling-layer scaffolding for analysis. Pre-objective primacy (CN10, Commitment 1) survives the lift.

**Conclusion B3**: Commitment 1 "u_t sole primitive" extends consistently to multi-formation as "u_t-typed instances are sole primitives, replicated by L3 commitment $K_{\mathrm{field}}$, coupled by L3 parameter $\lambda_{\mathrm{rep}}$". No primitive inflation. ✓

#### §2.4.5 Formal Claim B4: Tool A1 stratified-space integration

**Claim B4**: Within the Whitney-stratified space picture (`mathematical_scaffolding_4tools.md` §2 Tool A1), $\lambda_{\mathrm{rep}}$ parametrizes the *energy functional* defined on $\widetilde\Sigma^K_M$; varying $\lambda_{\mathrm{rep}}$ does *not* change the stratification $\widetilde\Sigma^K_M = \bigsqcup_{K_{\mathrm{act}}=0}^{K_{\mathrm{field}}} S_{K_{\mathrm{act}}}$ but *does* change the stratum-wise critical-point structure of $\mathcal{E}_K|_{S_{K_{\mathrm{act}}}}$ and the gradient-flow dynamics across strata.

**Verification**:
- The configuration space $\widetilde\Sigma^K_M$ depends on graph $G$, total mass $M$, and architectural cap $K_{\mathrm{field}}$ — none on $\lambda_{\mathrm{rep}}$.
- The strata $S_{K_{\mathrm{act}}} = \{\mathbf{u} : \#\{j : \|u^{(j)}\|_1 > \epsilon\} = K_{\mathrm{act}}\}$ are defined by support cardinalities, independent of any energy choice.
- $\lambda_{\mathrm{rep}}$ enters $\mathcal{E}_K = \sum_k \mathcal{E}_{\mathrm{self}}(u^{(k)}) + \lambda_{\mathrm{rep}} \cdot B(\mathbf{u})$ where $B(\mathbf{u}) = \sum_{j<k} \langle u^j, u^k \rangle$ is fixed; $\lambda_{\mathrm{rep}}$ scales the bilinear penalty.
- Critical points of $\mathcal{E}_K$ within each stratum *do* shift with $\lambda_{\mathrm{rep}}$ (well-separated → weakly-interacting → strongly-interacting regimes correspond to different effective Hessian eigenstructures); K-jump events (stratum-boundary crossings, `mathematical_scaffolding_4tools.md` Claim 2.4) shift in *time* but not in *type* with $\lambda_{\mathrm{rep}}$.

**Conclusion B4**: λ_rep is a *parameter on the energy* (architectural-layer L3), not a *parameter of the configuration space* (which is set by $K_{\mathrm{field}}$, $G$, $M$); together $\lambda_{\mathrm{rep}}$ and $K_{\mathrm{field}}$ form the L3 commitments specifying the multi-formation model. ✓

#### §2.4.6 Cross-reference: F_Kstep_K_triple §7.4.5 layer-distinction table

The companion working file `F_Kstep_K_triple.md` §7.4.5 (Wave 3 OAT-2 deepening) presents the four-quantity layer-distinction table: $\mathcal{F}, K_{\mathrm{step}}, K_{\mathrm{act}}$ are L1/L2 PH-derivable diagnostics; $K_{\mathrm{field}}$ is L3 architectural — *not* a PH invariant of any field. Argument B places $\lambda_{\mathrm{rep}}$ at the *same L3 layer* as $K_{\mathrm{field}}$ — consistent with the F-side analysis.

| L3 architectural-layer commitments | Role |
|---|---|
| $K_{\mathrm{field}}$ | Cardinality of the K-field replication |
| $\lambda_{\mathrm{rep}}$ | Strength of inter-formation soft repulsion (between-replica coupling) |
| $(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}})$ | Within-formation four-term weights |
| $G = (X_t, E_t)$ | Graph structure |
| $M$ (or $\{m_j\}$) | Mass conservation budget |

These five categories of L3 commitments together specify the *model space*; L0 ($u_t$) lives within this space; L1/L2 diagnostics are derived.

#### §2.4.7 Naturalness summary of Argument B (Wave 3 deepening)

Argument B becomes the *unique* honest position once the following are made precise:
- (a) L0–L3 layer hierarchy (§2.4.1) makes "architectural layer" mathematically precise — not a vague meta-classification.
- (b) Commitment 1 + Commitment 16 + the new Argument B reading form a *consistent triple*: L0 primitive (single u_t type), L3 commitment ($K_{\mathrm{field}}$ replicas), L3 commitment ($\lambda_{\mathrm{rep}}$ coupling).
- (c) Tool A1 (stratified space) confirms λ_rep is a *parameter of the energy on* $\widetilde\Sigma^K_M$, not *of* $\widetilde\Sigma^K_M$ itself.
- (d) Tool A4 partial-fail (Argument C strict reject) eliminates the only competing reductive identification, leaving Argument B as the natural classification.
- (e) Symmetric K=1 degenerative behavior of $\lambda_{\mathrm{rep}}$ and $K_{\mathrm{field}}$ (both "vanish" as commitments at K=1) is now *expected* under the L3 layer reading, not anomalous.

The §2.2 Critic objections (Q1 architectural-layer placement; Q2 u_t primitive tension) are both formally addressed:
- Q1 → §2.4.1 layer definition + §2.4.2 Claim B1 verification.
- Q2 → §2.4.4 Claim B3 (Commitment 1 preserved via u_t-typed replication, not primitive inflation).

#### §2.4.8 Hard constraint check (this subsection)

- [x] u_t primitive maintained: §2.4.4 Claim B3 explicit.
- [x] CN10 contrastive: λ_rep contrasted to N-phase obstacle / KKT multiplier per §5.4 of `mathematical_scaffolding_4tools.md`; not reductively identified.
- [x] CN5 4-energy not merged: §2.4.3 Claim B2 explicit (within-formation L1 invariant).
- [x] No silent OP resolution: OP-0009-λ remains PARTIALLY RESOLVED (verdict §5.2 unchanged; §2.4 strengthens the Argument B reasoning *behind* the resolution but does not promote to RESOLVED).
- [x] No canonical edits: this is `working/MF/lambda_rep_ontology.md`.
- [x] No new primitive introduced: the L0/L1/L2/L3 stratification is a *classification of existing quantities*, not an addition.

---

## §3. KKT Verification 정밀화 (Tool A4 §5.4 확장)

### §3.1 Equality vs Inequality constraint 차이

Standard N-phase Allen-Cahn은 *equality* constraint $\sum_k u^{(k)}(x) = 1\;\forall x$ (Gibbs simplex). SCC는 *inequality* $\sum_k u^{(k)}(x) \leq 1$ (sub-simplex).

- Equality: $\mu(x) \in \mathbb{R}$ (no sign constraint). Constraint always active.
- Inequality: $\mu(x) \geq 0$ + complementary slackness. Active at $\sum_k = 1$ regions; inactive at $\sum_k < 1$ regions.

SCC's choice (inequality) reflects ontological commitment: 사이트가 *어느* formation에도 강하게 속하지 않을 수 있음 ($\sum_k u^{(k)}(x) < 1$이면 site는 "soft"하게 partially uncommitted). Equality는 모든 사이트가 항상 fully committed — 더 *crisp* 가정.

이 차이는 SCC가 standard N-phase model와 *contrastive* 한 또 다른 이유.

### §3.2 Pairwise vs Total bilinear

차이: SCC은 $-\sum_k (u^{(k)}(x))^2$ 항 (per-formation diagonal subtraction); PHR augmented penalty는 $-2 \sum_k u^{(k)}(x) + 1$ (linear shift). 형식적으로 다른 quadratic.

이 정확한 차이가 §2.3 verification fail의 source. λ_rep 항은 *cross-only* bilinear이지 *total-square* penalty가 아님.

### §3.3 Mass conservation vs simplex

SCC K-field는 $\sum_{j,x} u^{(j)}(x) = M$ (total mass; 또는 per-formation $m_j$ 고정 — canonical I9 binding decision). Simplex constraint는 $\sum_k u^{(k)}(x) \leq 1$ (per-site). 두 constraint가 별개. λ_rep는 simplex 측면 enforcement (Argument C 시도); mass conservation은 별도 Lagrange multiplier (canonical 이미 정식 명시 — 단일-formation $\Sigma_m$에 mass constraint Lagrange가 있음).

Argument C strict는 simplex constraint만 다룸; mass constraint Lagrange는 SCC에 명시적으로 존재 (다른 multiplier). 이중 구조 — λ_rep ≠ simplex multiplier ≠ mass multiplier.

### §3.4 Contrastive comparison to standard N-phase obstacle potentials

Garcke-Nestler-Stoth (1999) obstacle potential *(year corrected from 2004 per external references audit 2026-04-30)*:
$$W^{\mathrm{obs}}(\mathbf{u}) = \begin{cases} \sum_{j<k} \gamma_{jk} u^{(j)} u^{(k)} & \text{if } \mathbf{u} \in \Delta^{K-1} \\ +\infty & \text{otherwise} \end{cases}$$

여기서 $\gamma_{jk}$는 *interfacial energies* (pair-specific); $\mathbf{u}$가 simplex 안에 있을 때만 finite. SCC bilinear $\lambda_{\mathrm{rep}} \langle u^j, u^k \rangle$와 형식 매우 유사 — 단 (a) SCC는 graph-domain (per-site) integration vs continuous; (b) SCC는 inequality constraint의 *enforcement* via penalty (외부에서 들어옴) vs Garcke의 hard constraint + interfacial penalty inside; (c) SCC λ_rep는 *single scalar* $\lambda_{\mathrm{rep}}$ vs Garcke $\gamma_{jk}$ pair-specific.

**Conclusion**: SCC λ_rep는 standard N-phase obstacle potential의 *symmetric simplification*. CN10 contrastive comparison으로 reference 가능; reductive identification은 fail.

---

## §4. Reformulation Options — Detailed Analysis

### §4.1 Option 1: N-phase Reformulation (replace bilinear with multi-well)

**Cost**: V5b family Cat A 결과 retroactive 재검증 필요. **Not recommended**.

### §4.2 Option 2: Augmented Lagrangian Reformulation

**Cost**: Multiplier theory 추가. PHR augmented Lagrangian이 SCC's static energy minimization frame과 잘 맞지 않음. **Not recommended**.

### §4.3 Option 3 (RECOMMENDED): Contrastive Comparison per CN10

**Proposal**: λ_rep는 standard N-phase Allen-Cahn 및 PHR augmented Lagrangian과 **contrastive comparison** 관계 (per CN10). *Reductive identification은 시도하지 않는다*. λ_rep의 ontological status는 **architectural-layer coupling parameter** (Argument B); CN5 4-term 약속은 *single-formation 약속*으로 명시화. 5번째 term 신설 안 함; KKT identification 강제 안 함.

**Cost**: CN5 wording amendment ~3-5 lines + I9 line 846 wording 보강 ~3-5 lines.

**Net effect**: CN5 약속 무결성 보존; CN10 contrastive 강화; verification fail 정직 명시; canonical 변경 minimal.

---

## §5. Recommended Canonical Edits at CV-1.6 (Option 3 채택 가정)

### §5.1 CN5 Amendment (proposed text)

```markdown
5. **Four-term minimal energy structure (W6+ amended).** The canonical energy 
   $\mathcal{E}_{\mathrm{self}}(u)$ comprises four conceptually independent terms — 
   closure, separation, boundary/morphology, and transport — addressing four 
   logically independent structural requirements **at the single-formation level**. 
   Multi-formation extension via K-field architecture (Pillar I9) introduces 
   between-formation bilinear coupling $\sum_{j<k} \lambda_{\mathrm{rep}} \langle u^{(j)}, u^{(k)} \rangle$. 
   Per OP-0009-λ resolution (W6+, OAT-3), this coupling is an architectural-layer 
   parameter (parallel to $K_{\mathrm{field}}$ per Commitment 16); not a 5th 
   conceptually independent term. Per CN10, λ_rep is contrastively compared 
   (not reductively identified) to standard N-phase Allen-Cahn obstacle potentials 
   and augmented Lagrangian quadratic penalties; strict KKT Lagrange multiplier 
   identification fails (verification §5.4 of `mathematical_scaffolding_4tools.md`).
```

### §5.2 OP-0009-λ Status Update at CV-1.6

`open_problems.md` OP-0009-λ entry:
> "PARTIALLY RESOLVED (CV-1.6) by Option 3 contrastive comparison — λ_rep is architectural-layer coupling (between-formation interaction); CN5 4-term independence preserved at single-formation; reductive KKT identification verified to fail."

---

## §6. External References

- Garcke, H., Nestler, B., & Stoth, B. (1999). "A multi-phase field concept" *SIAM J. Appl. Math.* 60(1), 295–315. *(Year corrected from 2004; volume corrected from 64(3) per external references audit 2026-04-30.)*
- Garcia Trillos, N. & Murray, R. W. (2017). "A new analytical approach to consistency and overfitting in regularized empirical risk minimization" *J. Stat. Phys.* **167**(5), 934–958. DOI: 10.1007/s10955-017-1772-4. *(Citation corrected: 2017 paper is Garcia Trillos-Murray, NOT Bertozzi-Esedoğlu-Gillette. Bertozzi-Esedoğlu-Gillette 2007 paper is image processing IEEE. Volume corrected 169 → 167 per gauge-extension audit 2026-04-30 #8.)*
- Modica, L. & Mortola, S. (1977). "Un esempio di Γ-convergenza" *Boll. Un. Mat. Ital. B*.
- Powell, M. J. D. (1969). Augmented Lagrangian. *Optimization* 283–298.
- Hestenes, M. R. (1969). "Multiplier and gradient methods" *J. Optim. Theory Appl.* 4(5), 303–320.
- Rockafellar, R. T. (1973). "A dual approach to solving nonlinear programming" *Math. Programming* 5(1), 354–373.
- Karush, W. (1939); Kuhn, H. W. & Tucker, A. W. (1951). KKT conditions.

---

## §7. Hard Constraint Verification

- [x] canonical 직접 수정 0.
- [x] Silent resolution 0 (Argument C strict verification fail explicit; Option 3 chosen over salvage; OP-0009-λ status PARTIALLY RESOLVED, not silently RESOLVED).
- [x] CN10 contrastive 강화 (standard N-phase + AL 모두 contrastive references).
- [x] u_t primitive maintained (λ_rep is architectural-layer parameter; per-formation $u^{(k)}$ remain primitives).
- [x] 4-energy not merged at single-formation; multi-formation bilinear separate category.
- [x] No reductive equation (Argument C strict reject).

---

## §8. Cross-References

- `K_status_commitment.md` (OAT-1, CV-1.5.1): K_field/K_act layer-distinction logic — λ_rep parallel application.
- `mathematical_scaffolding_4tools.md` §5.1–§5.6 (OAT-supplementary): Tool A4 partial verification source.
- `multi_formation_sigma.md` §6.1 (D-6a): N-1 integer K commitment context.
- `sigma_multi_trajectory.md` §2 (D-6b): K-jump dynamics with $\Lambda_{\mathrm{coupling}}$ regime parameter.

---

## §9. Recommendation Summary

**Recommendation: APPROVE Option 3 (contrastive per CN10)** at CV-1.6 D-CV1.6-O3.

**Effort**: ~10-15 canonical lines (CN5 amendment + OP-0009-λ status update). CV-1.6 packet integration: minimal (1 D-item).

**Net effect**: 4-month implicit ambiguity (5-term vs architectural vs Lagrange) → 1 explicit position. CN5 약속 minimal-structure 보존. CN10 contrastive 강화. Verification fail 정직 기록. σ-framework T-Persist-K-Unified $\Lambda_{\mathrm{coupling}}$ parameter framing 그대로 유지.

---

**End of lambda_rep_ontology.md (OAT-3 deliverable).**
**Status: working draft. Argument B + Option 3 채택 권고. Argument A + C strict 기각. OP-0009-λ PARTIALLY RESOLVED at CV-1.6. Wave 3 OAT-3 deepening (§2.4) provides formal L0–L3 layer-theory backing for Argument B.**
**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/lambda_rep_ontology.md`
**Created:** 2026-04-30 (W5 Day 4)

---

## §10. Wave 3 Revision Log

### 2026-04-30 — Wave 3 OAT Deepening Team (worker-1, Task 1 Subtask B)

**Context**: Wave 3 OAT deepening team work (`.omc/state/team/wave-3-oat-deepening-team-work/`, claim_token `7ec973d4-…`); 3-worker team executing Ontological Audit Track deepening on `working/MF/` files; NO canonical edits; hard constraints u_t primitive + CN10 contrastive + CN5 4-energy not merged + CV-1.6 D-items as targets.

**Changes (this revision)**:
1. **New §2.4 — Argument B Deepened (Architectural-Layer Theory)** (+~115 lines): formalizes Argument B with an explicit L0–L3 layer hierarchy (§2.4.1), four formal claims B1–B4 with verifications (§2.4.2 λ_rep ∈ L3; §2.4.3 CN5 minimal preserved; §2.4.4 Commitment 1 u_t primitive preserved; §2.4.5 Tool A1 stratified-space integration), a layer-commitment table mapping L3 to ${K_\text{field}, \lambda_\text{rep}, (\lambda_\text{cl}, \lambda_\text{sep}, \lambda_\text{bd}, \lambda_\text{tr}), G, M}$ (§2.4.6), naturalness summary (§2.4.7), and hard-constraint checklist (§2.4.8).
2. **§2.2 objections (Q1, Q2) formally addressed**: §2.4.1 layer definition + §2.4.2 Claim B1 directly resolve the "architectural-layer placement" question (Q1 — λ_rep sits at the same L3 layer as $K_\text{field}$, the four energy weights, $G$, and $M$); §2.4.4 Claim B3 directly addresses the "u_t primitive tension" objection (Q2 — Commitment 1 preserved via u_t-typed replication interpretation).
3. **Cross-file consistency**: §2.4.6 explicitly cross-references `F_Kstep_K_triple.md` §7.4.5 layer-distinction table (Wave 3 OAT-2 deepening), placing $\lambda_\text{rep}$ at the *same* L3 architectural layer as $K_\text{field}$ — coherent with the F-side analysis. §2.4.5 cross-references `mathematical_scaffolding_4tools.md` §2 Tool A1 (Whitney stratification) showing $\lambda_\text{rep}$ parametrizes the *energy on* $\widetilde\Sigma^K_M$, not the stratification itself.
4. **§9 status line updated**: now records the §2.4 deepening within the OAT-3 deliverable summary.

**No canonical edits made**; CV-1.6 promotion target (CN5 amendment + OP-0009-λ status) unchanged. OP-0009-λ remains PARTIALLY RESOLVED. The Wave 3 deepening *strengthens the reasoning behind* Argument B (preferred direction per §2.2 verdict) but does not promote to RESOLVED — the verification fail of Argument C strict (§2.3) and the contrastive (not reductive) reading per CN10 are unchanged.
