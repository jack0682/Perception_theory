---
id: ROADMAP-0003
type: roadmap/open_problems
status: accepted
last_updated: 2026-04-25
---

# Open Problems Registry (OP-xxxx)

**Purpose:** Catalog all unresolved research questions with severity ratings, status, and impact analysis.

**Format:** Organized by severity (critical → high → medium → low) and category.

---

## CRITICAL PROBLEMS 🔴 (Foundational)

### **OP-0001: F-1 — K=2 Vacuity**

**Statement:**  
K=2 global stability is "vacuous" without external per-formation mass constraint. If masses m_j are allowed to vary, energy minimization always selects K=1 (energetically ~50% cheaper).

**Evidence:**
- exp62, exp63: K=2 energy E ≈ 4.66; K=1 energy E ≈ 2.25
- M-1 analysis: M₂ landscape monotonically decreasing toward K=1
- All K-field theorems assume "m_j fixed externally" (axiom A-0013)

**Impact:**
- All K-field theorems (T-Persist-K-Sep, T-Persist-K-Unified, etc.) depend on this external assumption
- K-field theory is not self-contained
- No mechanism yet explaining why K would be fixed in biological/cognitive systems
- Blocks publication as self-contained theory

**Related problems:** M-1 (root cause), MO-1 (Morse variant)

**Proposed resolutions:**
- **Option A:** Accept "fixed K is external constraint" (current v1.2 approach)
- **Option B:** Develop K-selection mechanism (BIC, free energy, birth-death dynamics)
- **Option C:** Reformulate as kinetic/metastability theory (K>1 as local minima)
- **Option D (taken in W4, 2026-04-24):** Premise dissolution via SCC-intrinsic re-framing — neither A/B/C, but a fourth path where the dichotomy "K=1 cheaper vs observed K>1" itself ceases to be framed.

**Status:** ✅ **SPLIT-RESOLVED (2026-04-24)** — both portions Cat A.

**Resolution (2026-04-24, W4 session):**

F-1 decomposes into two layers, each Cat A resolved:

- **Pure $\mathcal{E}_{\mathrm{bd}}$ portion**: Resolved by T-Merge (b) canonical theorem (already proved, isoperimetric ordering on connected graphs). The "K=1 cheaper" statement in pure $\mathcal{E}_{\mathrm{bd}}$ is a *correct theorem*, not an open problem. Original framing as "open problem" was a misclassification — see also OP-0002 M-1 below.

- **Full SCC portion**: Resolved by **Theorem 2 (i)** (Pre-Objective Mechanism, Cat A graph-class independent via Theorem 2-G). Under full SCC parameters, the F=1 single-disk minimizer of pure $\mathcal{E}_{\mathrm{bd}}$ is **not a critical point** of full $\mathcal{E}$. Therefore, the dichotomy "K=1 cheaper vs observed K>1" does not arise — F=1 is non-critical, F ≥ 2 is the default ground state under full SCC. The premise of F-1 collapses.

**Net effect**: The originally-paradoxical comparison ("global static minimum K=1 vs empirical K>1") is dissolved. Pure $\mathcal{E}_{\mathrm{bd}}$ statement is a proved theorem (T-Merge (b)); full SCC statement is reversed (F ≥ 2 default).

**Severity:** 🔴 ~~CRITICAL~~ → ✅ RESOLVED (no longer blocking)
**Last reviewed:** 2026-04-25 (W4 weekly close)
**References:**
- `THEORY/logs/daily/2026-04-24/16_C2_closure.md` §F-1 resolution
- `THEORY/logs/daily/2026-04-24/11a_C2_generalization.md` (Theorem 2-G)
- `THEORY/logs/daily/2026-04-24/08_C2_phase1_theory.md` (Theorem 2 (i) proof)
- `THEORY/canonical/canonical.md` §13 T-Merge (b) (pure portion) — pre-existing Cat A
- `THEORY/canonical/canonical.md` §13 T-PreObj-1 (full SCC portion) — to be added in W4 merge

---

### **OP-0002: M-1 — K=1 Energetic Preference**

**Statement:**  
The K=2 energy landscape E(m₁, m₂) where m₁ + m₂ = M is monotonically decreasing as one formation size decreases (m₂ → 0). Therefore, K=1 with total mass M is always energetically cheaper than any K=2 split.

**Evidence:**
- Direct calculation: E_K1(M) < E_K2(M/2, M/2) always
- Empirical confirmation: exp62, exp63, exp71–exp73
- Consequence of energy functional form (no K>1 preference mechanism)

**Impact:**
- This is the **root cause of F-1**
- Shows K>1 can never emerge from energy optimization alone
- Requires model selection mechanism (BIC, free energy, etc.) to explain K>1 emergence
- Fundamental limitation of current energy-based framework

**Related problems:** F-1 (consequence), OP-0005 (K selection)

**Status:** ✅ **LAYER-CLARIFIED (2026-04-24)** — proved theorem misframed.

**Clarification (2026-04-24, W4 session):**

M-1 is **not an open problem**; it is the *correct mathematical statement* (T-Merge (b), canonical §13 Cat A) about isoperimetric ordering on the constraint manifold $\Sigma_m$. The original framing as "problem" arose from conflating two distinct quantities:

- **Pure $\mathcal{E}_{\mathrm{bd}}$ layer**: M-1 statement holds — K=1 has lower energy than K=2 by the perimeter minimization (Γ-convergence). This is T-Merge (b), already canonical.

- **Full SCC layer**: The comparison "K=1 cheaper vs K=2" is not even framed, because under full SCC parameters, the F=1 single-disk minimizer is **not a critical point** (Theorem 2 (i)). The "K=1 ground state" of pure $\mathcal{E}_{\mathrm{bd}}$ does not survive into the full SCC landscape.

**Net effect**: M-1 is *proved* (T-Merge (b)); the misframe was treating it as a *problem*. The actual problem (in original framing) was the apparent conflict between this proved theorem and empirically observed K>1 — that conflict is resolved by Static/Dynamic Separation (CN15 candidate, W4 04-23) and Theorem 2 (W4 04-24): static global minimum is K=1 only on pure $\mathcal{E}_{\mathrm{bd}}$, but dynamic protocol-endpoint observables ($\widehat{K}$, $\mathcal{F}$) need not equal it.

**Severity:** 🔴 ~~CRITICAL~~ → ✅ CLARIFIED (proved theorem, not a problem)
**Last reviewed:** 2026-04-25 (W4 weekly close)
**References:**
- `THEORY/canonical/canonical.md` §13 T-Merge (b) (the actual theorem)
- `THEORY/logs/daily/2026-04-24/08_C2_phase1_theory.md` §M-1 layer analysis
- `THEORY/logs/daily/2026-04-24/16_C2_closure.md` §4
- `THEORY/logs/daily/2026-04-23/MF_multi_quantization.md` §7 (Landau monotone) — the same statement under FQ framework

---

### **OP-0003: MO-1 — Morse Theory Inapplicability**

**Statement:**  
The K=2 constrained manifold Σ²_M = {(u¹, u²) : m_1 = m_2 = M/2} is not a smooth manifold; it has corners (at boundary where one formation's mass → 0). Smooth Morse theory requires manifolds without boundary and thus is inapplicable.

**Evidence:**
- Manifold geometry: Σ²_M is the product Σ_m × Σ_m restricted to constraint surface; this is a manifold **with corners**
- Standard Morse theory: Only works on smooth manifolds without boundary
- Implication: Theorems T-8-Core, T-14, etc. may need re-proof using stratified framework

**Impact (original framing):**
- Full global analysis of K=2 energy landscape incomplete
- Smooth bifurcation theory not applicable to M₂
- Workaround: Use existing stable results (don't claim global optimality without proof)
- Alternative: Develop stratified Morse theory analysis (significant effort)

**Related problems:** F-1, M-1 (both related to M₂ properties)

**Status:** ⚪ **SIDESTEPPED (2026-04-24)** — single-formation σ-framework operates on $\Sigma_m$ (no corners). Multi-formation extension to $\Sigma^K_M$ remains open.

**Sidestep mechanism (2026-04-24, W4 session):**

MO-1 was a blocker for global landscape analysis on the multi-formation manifold $\Sigma^K_M$ (corners). The W4 work introduced:

- **σ-framework** (canonical-ready, Cat A definitional): operates on **single-formation** $\Sigma_m$ (smooth simplex, no corners). Hessian eigenvalue/irrep/nodal-count signature $\sigma(u^*) = (\mathcal{F}; \{(n_k, [\rho_k], \lambda_k)\})$ is well-posed.
- **Theorem 2 family** (Cat A graph-class independent): operates on **single-formation** $\Sigma_m$. Pre-objective formation mechanism (F ≥ 2 default under full SCC) does not require multi-formation Morse analysis.

Therefore, the principal results of W4 (Theorem 2 family + σ-framework + F-1 split-resolution) **do not require Morse theory on $\Sigma^K_M$**. MO-1 is not a blocker for current scope.

**Multi-formation extension still open**: Stratified Morse on $\Sigma^K_M$ (multi-formation σ, Phase 5) remains genuine open work. MO-1 returns as an active blocker if/when the theory extends to multi-formation σ.

**Severity:** 🟠 HIGH (within multi-formation scope) → ⚪ NOT BLOCKING (within single-formation scope)
**Last reviewed:** 2026-04-25 (W4 weekly close)
**References:**
- `THEORY/logs/daily/2026-04-24/02_development.md` §2, §5 (σ on Σ_m, single-formation)
- `THEORY/logs/daily/2026-04-24/16_C2_closure.md` §7 (MO-1 sidestep note)
- `THEORY/logs/daily/2026-04-24/99_summary.md` §8 (sidestep vs resolution distinction)
- Multi-formation σ Phase 5: deferred to W5+ (W4 weekly_summary §6.4)

---

## HIGH-PRIORITY PROBLEMS 🟠

### **OP-0004: Type A/B Classification Invalidation**

**Statement:**  
04-07 proposed "Type A vs Type B" classification of K=2 configurations:
- Type A: Centered, stable, no valley-hopping
- Type B: Off-center, swap-prone, valley-hopping

exp65 conducted validation; **Type B was never observed** (0/4 configurations).

**Evidence:**
- exp65_formation_tracking.json: All 4 configs clustered at Type A
- max_center_offset = 0.01–0.08 (all < Type B threshold 0.12)
- swap_count = 0 everywhere (Type B marker absent)

**Impact:**
- Classification framework is **retracted** (unvalidated hypothesis)
- 04-07 interpretation of exp62/exp63 divergence is **rejected**
- exp62/exp63 difference attributed to optimizer strategy, not K-field type
- Branch selection work (exp66–exp73) continues but unrelated to Type A/B

**Status:** ❌ RETRACTED (empirically invalidated)  
**Severity:** 🟠 HIGH (affects theoretical narrative)  
**Last reviewed:** 2026-04-12 audit  
**References:** exp65 data, AUDIT_REPORT_2026-04-12.md

---

### **OP-0005: K Selection Mechanism (Missing)**

**Statement:**  
Theory provides no mechanism for how K (number of formations) is determined. Is it:
- Fixed externally (current assumption A-0012, unresolved F-1)?
- Emerged from energy minimization (contradicted by M-1)?
- Determined by model selection (BIC, free energy)?
- Kinetically determined (metastability barriers)?

**Impact:**
- Cannot predict K from initial conditions alone
- Theory cannot explain K emergence in biological/cognitive systems
- Required for moving from v1.2 to v2.0

**Status:** ❌ OPEN (no proposal yet)  
**Severity:** 🟠 HIGH (foundational question)  
**Related:** F-1, M-1

**2026-04-17 integration note (Phase 4):**
- Current audited `E-0082` surface provides only **weak, proxy-level support** for a persistence-scope reading, not observed-`K` selection closure.
- Current runnable/artifact evidence still lacks `tau`/`T`/`B`/cross-`K` observables and locked reruns remain blocked by `No Type B base found`.
- This is an evidence-boundary alignment note only; it does not change `OP-0005` status or severity.
- OP-0005 therefore remains OPEN; selection-mechanism status is unchanged pending a runnable `E-0082` path plus explicit selection-grade outputs.

---

### **OP-0006: Boundary Definition Precision**

**Statement:**  
Boundary B_t is currently defined via D_t (distinction operator) threshold:
- B_t = {x : D_t(u_t) > threshold}

But this is:
- Not morphologically precise (what is "boundary" exactly?)
- Lacks gradient/articulation measure
- Graded, not crisp

**Impact:**
- Affects articulation diagnostic (part of proto-cohesion d)
- Needed for precise morphological quality measure Q_morph
- Currently incomplete

**Status:** ⚠️ TENTATIVE (D-0013 in development)  
**Severity:** 🟠 HIGH (affects diagnostics)  
**Related:** D-0004 (distinction operator)

---

## MEDIUM-PRIORITY PROBLEMS 🟡

### **OP-0010: Bind Generalization**

**Statement:**  
T-Bind-Proj proved for τ=1/2 only (Category B). General τ ∈ (0,1) case (T-Bind-Full) is Category C (very conditional).

**Question:** Does projection property hold for all τ, or only τ=1/2?

**Impact:**
- Limits use of binding predicate (normalization dependent)
- Affects multi-scale analysis
- Low priority (doesn't block main theory)

**Status:** ⚠️ PARTIAL (τ=1/2 case solved)  
**Severity:** 🟡 MEDIUM (specialty case)  
**References:** theorem_registry.md (T-Bind-Proj, T-Bind-Full)

---

### **OP-0011: Transport Kernel Uniqueness**

**Statement:**  
Current transport kernel M_{t→s} form (entropy-regularized OT) is *one* realization satisfying axioms E1–E5. Is it unique? Are there other realizations?

**Impact:**
- Theoretical completeness
- Robustness of persistence results
- May affect characterization of formation inheritance

**Status:** 🔄 UNDER INVESTIGATION (exp30–exp35)  
**Severity:** 🟡 MEDIUM (impacts formalism)  
**Related:** T-Persist-1(a–e)

---

### **OP-0012: Persistence Composition**

**Statement:**  
T-Persist-Full (composition of persistence across 3+ time steps) is Category C (very conditional). Can general composition formula be proved?

**Impact:**
- Affects long-timescale predictions
- Currently only T-Persist-1 (two-step) fully proved
- Limits temporal theory

**Status:** ❌ UNRESOLVED (Category C conditional)  
**Severity:** 🟡 MEDIUM (temporal extension)  
**References:** theorem_registry.md (T-Persist-Full)

---

### **OP-0013: Closure Operator Convergence Rate**

**Statement:**  
T-6 proves closure operator has fixed point with contraction; exact rate unknown.

**Question:** What is the convergence rate as function of parameters?

**Impact:**
- Affects efficiency of closure-based algorithms
- Currently only asymptotic guarantee known
- Low practical impact

**Status:** 🔄 UNDER INVESTIGATION  
**Severity:** 🟡 MEDIUM (implementation detail)

---

## LOW-PRIORITY PROBLEMS 🟢

### **OP-0020: Dynamic Topology (Out of Scope)**

**Statement:**  
Current theory assumes X_t is fixed. What if graph topology changes over time?

**Status:** Not in current scope  
**Severity:** 🟢 LOW (future extension)

---

### **OP-0021: Stochastic Dynamics**

**Statement:**  
Theory focuses on deterministic gradient descent. How do thermal fluctuations affect dynamics?

**Related:** Kramers rate theory (exp54–exp59); under active investigation

**Status:** 🔄 UNDER INVESTIGATION (exp54–exp59)  
**Severity:** 🟢 LOW (extension work)

---

### **OP-0022: Continuous-Time Limit**

**Statement:**  
Theory on discrete graphs; what is continuous limit?

**Status:** Not addressed  
**Severity:** 🟢 LOW (theoretical extension)

---

## Problem Statistics

**Updated 2026-04-25 (W4 weekly close)**:

| Severity | Count | Blocked By | Status |
|----------|-------|-----------|--------|
| 🔴 ~~CRITICAL~~ | ~~3~~ → **0** | — | **All 3 resolved/clarified/sidestepped in W4 (2026-04-24)** |
| 🟠 **HIGH** | 1 (was 3) | None | OP-0005 K-selection still open (partially addressed by σ-framework + CN15) |
| 🟡 **MEDIUM** | 4 (was 5) | Mostly orthogonal | unchanged |
| 🟢 **LOW** | 4+ | None | Out of scope |
| **Total active open** | **5+** | — | — |
| Resolved/clarified/sidestepped (W4) | 3 | F-1, M-1, MO-1 | new (2026-04-24) |

### Distribution (post-W4, 2026-04-25)

```
Critical blockers (post-W4): NONE — all 3 (F-1, M-1, MO-1) addressed in 2026-04-24 session
                              via Theorem 2 family + T-Merge (b) + σ-framework single-formation scope.

High (affects core theory):  K-Selection (partially addressed via σ-framework, Static/Dynamic
                              Separation CN15 candidate; full mechanism still open)
Medium (extensions):          Boundary precision, Bind τ, Transport uniqueness,
                              Persist composition, Closure convergence rate
Low (future):                 Dynamic topology, Stochastic, Continuous limit
```

**Net effect**: 1년간 publication을 블록하던 Critical 3건이 모두 해소됨. v2.0 release path 가 unblocked. 단, K-Selection (OP-0005) 의 *full* mechanism 은 여전히 active research 대상 (W5+ NQ-148 cluster).

---

## Critical Path to Resolution

### ✅ Completed in W4 (2026-04-19 ~ 2026-04-25)

1. **F-1 SPLIT-RESOLVED** (OP-0001) — Both portions Cat A.
   - Pure $\mathcal{E}_{\mathrm{bd}}$ portion: T-Merge (b) canonical (already proved).
   - Full SCC portion: Theorem 2 (i) Cat A graph-class independent (T-PreObj-1 family, W4 04-24).

2. **M-1 LAYER-CLARIFIED** (OP-0002) — Proved theorem (T-Merge (b)) misframed as problem. Static/Dynamic Separation (CN15 candidate) explains apparent K=1 vs K>1 conflict.

3. **MO-1 SIDESTEPPED** (OP-0003) — Single-formation σ-framework operates on $\Sigma_m$ (no corners); current scope does not require Morse on $\Sigma^K_M$.

4. **Resolution path: Option D (premise dissolution)** — neither original A/B/C, but a fourth path discovered via SCC-intrinsic re-framing.

### Next priorities (W5+, 2026-04-26 onward)

**Immediate (next 1-2 weeks)**:
1. Canonical merge of W4 T1 results (Theorem 2 family → §13; F-1/M-1/MO-1 status updates → this file).
2. NQ-170: ζ_* crossover boundary quantification (Theorem 1 V5b verification).
3. Axiom S1' v1 user decision (canonical §6 vs §11 vs §13).

**Short-term (1–2 months)**:
1. Multi-formation σ extension (Phase 5) — would re-activate MO-1 as blocker.
2. NQ-148 (σ-jump formalization, N-1.A connection) — addresses OP-0005 K-selection partially.
3. Theorem 1 V5b ζ-scan + graph-class extension → V5b Cat A canonical promotion candidate.

**Medium-term (3+ months)**:
1. v2.0 release (path now unblocked by W4 Critical resolution).
2. Address remaining Medium-priority open problems (OP-0010..0013).
3. Multi-formation σ stratified Morse (would re-engage OP-0003).

---

## Problem Lifecycle Example: F-1

**Discovery:** 04-06 audit identified K=2 energy paradox
**Formalization:** 04-12 THEORY_STATUS_2026-04-12.md documented as critical
**Reframing:** 04-19 N-1 (Soft-Hard Switching Asymmetry) discovered as single source of F-1/M-1/MO-1 (W4 reframing)
**Foundation work:** 04-21 K_soft + ℱ_{C+E} framework — F/M/MO architectural dissolution candidate
**Empirical pivot:** 04-23 R23 Orbital Discovery + 56 stable minimizers + closure-eliminates-F=1
**Resolution:** 04-24 Theorem 2 family Cat A (graph-class independent via Theorem 2-G) + T-Merge (b) canonical → SPLIT-RESOLVED
**Current status:** OP-0001 RESOLVED (no longer blocking)
**Resolution path:** Option D (premise dissolution via SCC-intrinsic re-framing)
**Timeline actual:** Reframing-to-resolution: 6 days (04-19 to 04-24)
**Outcome:** v2.0 release path unblocked

---

**Last updated:** 2026-04-25 (W4 weekly close, post-resolution)
**Total problems:** 15+ registered
**Active blockers:** 0 critical (was 3 pre-W4), 1 high (OP-0005 K-Selection partial)
**W4 changes:** F-1 split-resolved, M-1 layer-clarified, MO-1 sidestepped (3 Critical → 0)
**Time to resolution (F-1):** 6 days from N-1 reframing (04-19) to SPLIT-RESOLVED (04-24)

---

See also: **master_problem_map.md**, **dependency_graph.md**, **milestones/** (this folder)
