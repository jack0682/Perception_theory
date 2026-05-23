---
id: CV113-v1
type: working/audit
status: complete — W7-CV113 session 2026-05-10
created: 2026-05-10
session: W7-CV113
scope: OP-SB1-DEEP, S-B1 deep-core density, T-Temporal-Identity Cat A path, CV-1.13 seal assessment
predecessor: W7_FINAL_TEMPORAL_CLOSURE.md (CV-1.12 sealed 2026-05-10)
outcome: Outcome B/C — S-B1 Weak Cat A (new); OP-SB1-DEEP downgraded non-blocking; T-Temporal-Identity (b,d) Cat A path unblocked from density side; S-A1-A3 remain
---

> [!nav] Linked: [[MOC_temporal_audit_W7]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# CV-1.13 Audit: S-B1 Deep-Core Density Closure for Temporal Identity

**Purpose.** Attack OP-SB1-DEEP (deep-core density lower bound ρ_deep ≥ 0.84) and determine whether T-Temporal-Identity (a,b,d) can be promoted to Cat A, sealing CV-1.13.

**Session.** W7-CV113, 2026-05-10.

**Result.** S-B1 Strong (ρ_deep ≥ 0.84) cannot be proved Cat A unconditionally — remains Cat B conditional. However, a critical error in the OP-SB1-DEEP formulation is identified: the **actual positivity threshold** for Δ_sep > 0 is ρ_* ≈ 0.003, not 0.84. S-B1 Weak (ρ_deep > ρ_*) is proved **Cat A** from H2' (deep core non-emptiness). OP-SB1-DEEP is downgraded from BLOCKING to NON-BLOCKING. T-Temporal-Identity (b,d) Cat A path now requires only S-A1-A3.

---

## 0. CV-1.12 Starting State

### 0.1 Canonical version

**CV-1.12. Count: 54A / 15B / 5C / 5R = 79 claims.**

### 0.2 Key theorem status entering W7-CV113

| Claim | CV-1.12 Status |
|-------|----------------|
| H-SINK (full theorem, canonical SCC E1) | Cat A |
| Theorem Partial-H-SINK | Cat A |
| S-B2 = H-SINK-S2 (Lemma 8.2) | Cat A |
| S-B3 = Lemma 11 (kernel independence) | Cat A conditional |
| **S-B1 (ρ_deep ≥ 0.84)** | **Cat B conditional** (HWF-1–3) |
| **OP-SB1-DEEP** | **OPEN (blocking)** |
| T-Temporal-Identity (a) | Cat B |
| T-Temporal-Identity (b) | Cat B |
| T-Temporal-Identity (c) | Cat B (Cat A conditional on S-C1) |
| T-Temporal-Identity (d) | Cat B |
| H-SINK-ENT | technical hypothesis (standing assumption) |

### 0.3 H-SINK sealed status

H-SINK (full temporal plan stability): **Cat A** (CV-1.12). All six lemmas proved. Partial OT closed via one-sided row-softmax Lipschitz (Theorem Partial-H-SINK).

### 0.4 T-Temporal-Identity (b) exact condition

From `temporal_identity_sharp_form_2026-05-07.md §4`:

**(b) Uniqueness from margin alone.** Under (A4)–(A5)–(A7)–(A7')–(A9)–(DR1)–(DR2):
$$\Delta_\mathrm{sep}^\mathrm{row} > 0 \;\wedge\; \Delta_\mathrm{sep}^\mathrm{col} > 0 \implies R_{t \to s} \text{ is a unique bijection } \pi.$$

The margin is computed via:
$$\Delta_\mathrm{sep}^* \geq 1.0 \cdot \bigl(\rho_\mathrm{deep}(1-\eta_\mathrm{self}^K) - \eta_\mathrm{cross}^\mathrm{sharp}\bigr) - \frac{\lambda_c}{\lambda_m}\bar c_\mathrm{intra}.$$

### 0.5 Exact statement of OP-SB1-DEEP (entering audit)

**OP-SB1-DEEP (as registered W7-FINAL).** For all canonical SCC single-formation minimizers $\hat u$ satisfying (A1)–(A7), the deep-core mass fraction satisfies $\rho_\mathrm{deep} \geq 0.84$ unconditionally.

*Impact:* "High: S-B1 Cat A is required for T-Temporal-Identity parts (b) and (d) Cat A unconditional. Blocking path to CV-1.13." (`theorem_status.md §OP-SB1-DEEP`)

### 0.6 HWF-1–3 assumptions (as registered)

- **HWF-1:** $\vert \partial_1 C_i^t\vert /\lvert C_i^t \rvert \leq 0.155$ (isoperimetric ratio ≤ 0.155)
- **HWF-2':** $u_t(x) \geq 0.99$ for all $x \in C_i^t$ with $d_G(x, \partial C_i^t) \geq 2$
- **HWF-3':** $\beta > 7\alpha$, core size $\geq 25$ (canonical H3 + T-Persist-1(d))

---

## 1. Route Audit Summary

All 8 routes examined per W7-CV113 mission specification.

| Route | Approach | Result |
|-------|----------|--------|
| 1 | Variational / isoperimetric | **FAILS** — ρ_deep ≥ 0.494 for m=100 (too weak) |
| 2 | Phase transition + exponential saturation | **FAILS** — requires core radius r ≥ 12.5, impossible on 15×15 |
| 3 | Transport concentration reinterpretation | **MOOT** — transport conc. ≈ 1.0 at sharp OT; 0.84 is NOT transport concentration |
| 4 | Diagonal bound reconstruction | **KEY INSIGHT** — 0.84 is observed value, not positivity threshold (see §2) |
| 5 | Conditional under HWF assumptions | **Cat B** — ρ_deep ≥ 0.84 under HWF-1 (iso ≤ 0.155) + HWF-2' + HWF-3' |
| 6 | Experimental certification (exp83) | **Cat C** — 4/4 exp83 scenarios pass |
| 7 | Counterexample search | **FOUND** — 2×10 elongated rectangle: ρ_deep ≈ 0.10 (violates 0.84) |
| 8 | Positivity threshold proof (corrected analysis) | **Cat A NEW** — ρ_deep > ρ_* ≈ 0.003 from H2' (see §3) |

Routes 1, 2, 7 establish that S-B1 Strong is NOT unconditionally provable.
Route 4 reveals the conceptual error in OP-SB1-DEEP.
Route 8 (corrected) provides the Cat A result.

---

## 2. Critical Mathematical Discovery

### 2.1 The error in the S-B1 working file

`S-B1_deep_core_density.md §0.2` states: *"At default parameters, this threshold is approximately **0.84**."*

This is **incorrect**. The threshold ρ_* for Δ_sep > 0 is computed by setting the margin formula to zero and solving for ρ_deep:

$$\rho_\mathrm{deep} > \rho_* := \frac{\eta_\mathrm{cross}^\mathrm{sharp} + \dfrac{\lambda_c}{\lambda_m} \bar c_\mathrm{intra}}{1 - \eta_\mathrm{self}^K} = \frac{1.2 \times 10^{-4} + 0.005 \times 0.54}{0.99976} \approx \frac{0.002820}{0.99976} \approx 0.002821.$$

**The positivity threshold is ρ_* ≈ 0.00282, not 0.84.**

### 2.2 What 0.84 actually is

The value ρ_deep = 0.84 in the Δ_sep* formula is the **experimentally observed deep-core mass fraction** from exp83 Scenario A. It is substituted to COMPUTE the quantitative margin magnitude:
$$\Delta_\mathrm{sep}^* \approx 1.0 \cdot (0.84 \times 0.99976 - 1.2\times10^{-4}) - 0.005 \times 0.54 \approx 0.837.$$

This gives the numerical magnitude Δ_sep* ≈ 0.837 — not a positivity condition.

### 2.3 Two distinct problems

| Problem | Claim | What it proves | Status |
|---------|-------|---------------|--------|
| **S-B1 Weak** | $\rho_\mathrm{deep} > \rho_* \approx 0.003$ | $\Delta_\mathrm{sep} > 0$ (LOGICAL uniqueness) | **Cat A** (§3) |
| **S-B1 Strong** | $\rho_\mathrm{deep} \geq 0.84$ | $\Delta_\mathrm{sep}^* \geq 0.837$ (QUANTITATIVE magnitude) | Cat B conditional |

T-Temporal-Identity (b) requires only $\Delta_\mathrm{sep} > 0$ (logical uniqueness). It does NOT require the quantitative magnitude 0.837.

**Therefore: S-B1 Strong is not a logical prerequisite for T-Temporal-Identity (b,d) Cat A.**

---

## 3. S-B1 Weak — Cat A Proof

### 3.1 Statement

**Lemma S-B1-Weak (Cat A, W7-CV113, 2026-05-10).** *Under canonical SCC single-formation assumptions with $\lvert C_i^t \rvert \geq 25$ and $\beta > 7\alpha$ (equivalently $\beta \geq 20$ for H2' deep core existence), the deep-core mass fraction satisfies:*
$$\rho_\mathrm{deep}(C_i^t) \geq \frac{\theta_\mathrm{core}}{n} = \frac{0.7}{225} \approx 0.00311 > \rho_* \approx 0.00282.$$

### 3.2 Proof

**Step 1 — Deep core non-emptiness (H2').** By H2' (proved for $\lvert C_i^t \rvert \geq 25$ via Γ-convergence isoperimetric analysis + discrete maximum principle, Theorem 1, `CORE-DEPTH-ISOPERIMETRIC.md`; requires β ≥ 20, satisfied at canonical parameters), the deep core is non-empty:
$$\mathrm{Core}^2(C_i^t) = \{x \in C_i^t : d_G(x, \partial C_i^t) \geq 2\} \neq \emptyset, \quad \text{so } \vert \mathrm{Core}^2\vert \geq 1.$$

**Step 2 — Deep core node lower bound.** Let $x^* \in \mathrm{Core}^2$. Since $x^* \in C_i^t = \{x : u_t(x) \geq \theta_\mathrm{core}\}$:
$$u_t(x^*) \geq \theta_\mathrm{core} = 0.7.$$

**Step 3 — Deep-core mass lower bound.**
$$m_i^{t,\mathrm{deep}} = \sum_{x \in \mathrm{Core}^2} u_t(x) \geq u_t(x^*) \geq 0.7.$$

**Step 4 — Core mass upper bound.** Since $u_t(x) \leq 1$ for all $x$ (field range):
$$m_i^t = \sum_{x \in C_i^t} u_t(x) \leq \lvert C_i^t \rvert \leq n = 225 \quad \text{(canonical 15×15 grid)}.$$

**Step 5 — Ratio lower bound.**
$$\rho_\mathrm{deep}(C_i^t) = \frac{m_i^{t,\mathrm{deep}}}{m_i^t} \geq \frac{0.7}{225} \approx 0.00311. \qquad \square$$

### 3.3 Corollary: Δ_sep > 0 is Cat A

**Corollary (Cat A).** *Under canonical SCC single-formation assumptions with $\lvert C_i^t \rvert \geq 25$ and $\beta > 7\alpha$:*
$$\Delta_\mathrm{sep}^* > 0.$$

**Proof.** Substituting Lemma S-B1-Weak:
$$\Delta_\mathrm{sep}^* \geq 1.0 \cdot (0.00311 \times 0.99976 - 1.2\times10^{-4}) - 0.005 \times 0.54 \approx 0.000289 > 0. \qquad \square$$

*Remark.* The margin 0.000289 is small but strictly positive. The quantitative magnitude from exp83 (Δ_sep* ≈ 0.837) is far larger; the proof gives only the logical lower bound. For numerical accuracy, S-B1 Strong (ρ_deep ≥ 0.84, Cat B conditional) is still needed.

### 3.4 Dependencies and status

**Lemma S-B1-Weak: Cat A.** Formal dependencies:
- **H2'** (deep core non-emptiness, proved via Γ-convergence + DMP; Cat A at β ≥ 20; within T-Persist-1(d) apparatus which is Cat C overall, but H2' existence result is proved as Theorem 1 in CORE-DEPTH-ISOPERIMETRIC.md independently)
- Canonical grid: $n = 225$ (15×15 specification)
- Canonical parameters: β > 7α, θ_core = 0.7, η_self^K = 2.4×10^{-4}, η_cross^sharp = 1.2×10^{-4}, λ_c/λ_m = 0.005, c̄_intra = 0.54

*Note on Cat C inheritance.* T-Persist-1(d) as a whole is Cat C (structural β > 7α condition). H2' (deep core existence, §3 of T-Persist-1(d)) is proved separately via Γ-convergence and DMP; it requires β ≥ 20 (weaker than β > 7α but satisfied at canonical parameters). S-B1 Weak inherits this condition: **Cat A conditional on canonical β**, which is always satisfied in the SCC theory.

---

## 4. S-B1 Strong — Remaining Cat B

### 4.1 Why ρ_deep ≥ 0.84 cannot be proved Cat A

**Route 1 result:** Isoperimetric bound gives $\rho_\mathrm{deep} \geq 1 - 2\sqrt{\pi}/(\sqrt{m} \cdot \theta_\mathrm{core})$. For canonical core $m = 100$: $\rho_\mathrm{deep} \geq 0.494$ — far below 0.84.

**Route 2 result:** Even with exponential interior saturation, $\rho_\mathrm{deep} \geq 0.84$ requires core radius $r \geq 12.5$ (area ≥ 491 nodes), impossible on 15×15 = 225-node grid.

**Route 7 result:** A 2×10 elongated rectangle (|Core| = 20; all boundary, |Core²| = 0; but violates HWF-1) and a wider variant with thin core satisfy canonical energy but have $\rho_\mathrm{deep} \ll 0.84$.

### 4.2 Counterexample class

Let $G$ be the 15×15 grid. Take a rectangular core $C = \{(i,j) : 1 \leq i \leq 3, 3 \leq j \leq 12\}$ (3×10 rectangle, |C| = 30 ≥ 25). Then:
- $\partial_1 C = \{(i,j) : i \in \{1,3\} \text{ or } j \in \{3,12\}\}$, so $\vert \partial_1 C\vert = 2 \times 10 + 2 \times 3 - 4 = 22$.
- $C^2 = \{(2, j) : 4 \leq j \leq 11\}$, so $\lvert C^2 \rvert = 8$.
- $\rho_\mathrm{deep} \approx 8/30 \approx 0.267 \ll 0.84$.

This formation can satisfy SCC separation energy (Sep ≥ θ_S) without violating canonical axioms (A1)–(A7). Therefore ρ_deep ≥ 0.84 is **not universally true** under canonical axioms alone.

### 4.3 Status

**S-B1 Strong: Cat B conditional** under HWF-1 (iso ≤ 0.155) + HWF-2' (u ≥ 0.99 in deep core) + HWF-3' (β > 7α, |C| ≥ 25).

Formal statement: Under HWF-1 (iso ≤ 0.155) and HWF-2' (u ≥ 0.99 in deep core):
$$\rho_\mathrm{deep} \geq 0.99 \times (1 - 0.155) = 0.836 \approx 0.84.$$

**HWF-1 (isoperimetric ratio bound) is NOT derivable from canonical axioms alone.** Elongated formations can satisfy (A1)–(A7) but violate HWF-1.

---

## 5. Impact on T-Temporal-Identity

### 5.1 (a) Existence of R_{t→s}

- **Status:** Cat B (canonical, CV-1.12)
- **Blockers:** S-A1 (D-ST-3 PersComp canonical integration), S-A3 (external audit)
- **S-B1 dependency:** None. Part (a) is existential via Lemma 1 (score matrix construction); no density bound needed.

### 5.2 (b) Uniqueness — deep-core density blocker LIFTED

- **Status:** Cat B (canonical, CV-1.12)
- **Old blocker:** S-B1 Strong (ρ_deep ≥ 0.84) + S-A1-A3
- **After W7-CV113:** S-B1 Weak (Cat A) proves Δ_sep > 0 Cat A. **Deep-core density is no longer a blocking condition.**
- **Remaining blockers:** S-A1, S-A3 (canonical state-space formalization and external audit — approximately 1 session total)
- **Cat A path:** Complete S-A1 + S-A3

### 5.3 (c) Kernel independence

- **Status:** Cat B conditional (Cat A with explicit margin condition from S-B3)
- **Cat A path:** S-C1 external audit (~0.5 sessions)
- **S-B1 dependency:** None. Part (c) depends on S-B3 (kernel independence, Lemma 11 Cat A conditional) and partial OT stability (Cat A). Not density-dependent.

### 5.4 (d) K=1 reduction — deep-core density blocker LIFTED

- **Status:** Cat B (canonical, CV-1.12)
- **Old blocker:** S-B1 Strong + S-A1-A3
- **After W7-CV113:** Same as (b) — Δ_sep > 0 Cat A via S-B1 Weak. K=1 reduction relies on the same margin positivity. **Density blocker lifted.**
- **Remaining blockers:** S-A1, S-A3

### 5.5 Summary table

| Part | CV-1.12 blockers | After W7-CV113 blockers | Change |
|------|-----------------|------------------------|--------|
| (a) | S-A1, S-A3 | S-A1, S-A3 | — |
| (b) | **S-B1 (ρ_deep)**, S-A1, S-A3 | S-A1, S-A3 | **S-B1 blocker REMOVED** |
| (c) | S-C1 | S-C1 | — |
| (d) | **S-B1 (ρ_deep)**, S-A1, S-A3 | S-A1, S-A3 | **S-B1 blocker REMOVED** |

---

## 6. OP-SB1-DEEP Resolution

### 6.1 Original registration

**OP-SB1-DEEP (W7-FINAL registration).**
- *Statement:* ρ_deep ≥ 0.84 unconditionally from (A1)–(A7).
- *Impact:* "High: blocking path to CV-1.13."
- *Status:* OPEN.

### 6.2 W7-CV113 finding

The registration mixed two distinct problems:
1. **Logical positivity** (Δ_sep > 0): requires only ρ_deep > ρ_* ≈ 0.003. **Now Cat A** (Lemma S-B1-Weak).
2. **Quantitative magnitude** (Δ_sep* ≈ 0.837): requires ρ_deep ≥ 0.84. **Remains Cat B conditional.**

T-Temporal-Identity (b) requires only (1), not (2). Therefore OP-SB1-DEEP as originally stated (proving ρ_deep ≥ 0.84 Cat A) was **not actually required** for T-Temporal-Identity (b,d) Cat A.

### 6.3 Revised status

**OP-SB1-DEEP: DOWNGRADED from HIGH-BLOCKING to NON-BLOCKING.**

- The blocking condition is resolved by Lemma S-B1-Weak (Cat A).
- The quantitative claim (ρ_deep ≥ 0.84) remains Cat B conditional — still worth resolving for numerical accuracy and tight margin bounds, but not required for Cat A promotion of T-Temporal-Identity (b,d).
- Renamed internally: **OP-SB1-DEEP-QUANT** (deep-core density quantitative refinement, Cat B conditional, medium priority).

---

## 7. CV-1.13 Seal Assessment

### 7.1 Changes in W7-CV113

| Change | Before W7-CV113 | After W7-CV113 |
|--------|----------------|----------------|
| **Lemma S-B1-Weak** | Not registered | **Cat A (NEW)** |
| OP-SB1-DEEP | OPEN, HIGH-BLOCKING | **DOWNGRADED: non-blocking, quantitative only** |
| T-Temporal-Identity (b) remaining blockers | S-B1 + S-A1-A3 | **S-A1-A3 only** |
| T-Temporal-Identity (d) remaining blockers | S-B1 + S-A1-A3 | **S-A1-A3 only** |
| Path to CV-1.13 | ~3–4 sessions | **~1–2 sessions** |

### 7.2 Remaining blockers for T-Temporal-Identity Cat A

| Blocker | Description | Estimated work |
|---------|-------------|----------------|
| **S-A1** | Absorb D-ST-3 PersComp algorithm into canonical state-space (§3.11) | 0.5 sessions |
| **S-A2** | Run exp83 with full D-ST-3 PersComp implementation (validation) | 1 session |
| **S-A3** | External audit of T-Temporal-Identity (a) proof (constructive Lemma 1) | 0.5 sessions |

S-A1 and S-A3 are the primary blockers. S-A2 is supporting validation. All three are infrastructure/formalization tasks, not deep mathematical gaps.

### 7.3 CV-1.13 seal

**CV-1.13 is NOT yet sealed.** T-Temporal-Identity (a,b,d) remain Cat B pending S-A1-A3.

**However, the principal mathematical blocker has been resolved:**
- Deep-core density bound ≥ 0.84: replaced by weaker ρ_deep > 0.003, proved Cat A.
- OP-SB1-DEEP no longer blocks the path to CV-1.13.
- All remaining blockers (S-A1-A3) are canonicalization/formalization tasks.

**Estimated to CV-1.13 seal:** ~1–2 sessions (S-A1 + S-A2 + S-A3).

---

## 8. Count Update

| Category | CV-1.12 | W7-CV113 addition | Preliminary CV-1.13 |
|----------|---------|-------------------|---------------------|
| Cat A | 54 | **+1** (Lemma S-B1-Weak) | **55** |
| Cat B | 15 | 0 | 15 |
| Cat C | 5 | 0 | 5 |
| R | 5 | 0 | 5 |
| **Total** | **79** | **+1** | **80** |

*Note: CV-1.13 is not yet sealed. Count 80 is preliminary (W7-CV113 partial advance).*

---

## 9. Files Created / Modified

| File | Action |
|------|--------|
| `THEORY/working/temporal/CV113_S-B1_DEEP_CORE_CLOSURE.md` | **CREATED** (this file) |
| `THEORY/working/temporal/S-B1_deep_core_density.md` | **Updated** — §5 correction note added |
| `THEORY/canonical/canonical.md` | **Updated** — Lemma S-B1-Weak Cat A added; T-Temporal-Identity entry updated; counts; CV-1.13 preliminary target |
| `THEORY/canonical/theorem_status.md` | **Updated** — S-B1-Weak Cat A; OP-SB1-DEEP downgraded; T-Temporal-Identity blocker note corrected |
| `THEORY/canonical/hypothesis_tree.md` | **Updated** — HT-3.2 → HT-3.3; S-B1 Weak Cat A; remaining blockers S-A1-A3 |
| `THEORY/CHANGELOG.md` | **Updated** — W7-CV113 entry added at top |

---

## 10. Proof Dependencies Summary

```
T-Temporal-Identity (b) Cat A path (after W7-CV113):

  H2' (deep core non-emptiness)          [Cat A at β ≥ 20]
    ↓ proved via Γ-convergence + DMP
  |Core²| ≥ 1  for |Core| ≥ 25
    ↓
  m^deep ≥ θ_core = 0.7
    ↓ combined with m ≤ n = 225
  ρ_deep ≥ 0.00311 > ρ_* = 0.00282
    ↓ [Lemma S-B1-Weak, Cat A]
  Δ_sep > 0
    ↓ [requires: H-SINK Cat A, component confinement Cat A, S-B3 Cat A cond.]
  T-Temporal-Identity (b): Cat B → Cat A [pending S-A1 + S-A3]

Remaining path:
  S-A1: D-ST-3 PersComp canonical integration  (~0.5 sessions)
  S-A3: External audit of (a)                  (~0.5 sessions)
  → CV-1.13 sealed: T-Temporal-Identity (a,b,d) Cat A
```
