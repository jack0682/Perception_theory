---
type: working/sensing_pipeline/pass12_three_framework_synthesis
version: v0
date: 2026-05-26
status: ACTIVE — Pass 12 Phase F Task 26
purpose: |
  Complete dependency / contribution map of SCC ↔ PAI ↔ PFE.
  Identify natural integration points, unresolved gaps, and discipline-violation risks.
register: SYNTHESIS-MAP
parent: 00_INDEX
prev: 19_delta_interp_synthesis
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  pai_canonical_edits: 0
  modifies_12_perception_cone: 0
  scope: integration map only; no canonical promotion proposed
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[19_delta_interp_synthesis]] · Pass 12 Phase F-3

# Pass 12 Phase F Task 26 — Three-Framework Synthesis

**Question**: SCC, PAI, PFE — what does each *contribute*, what does each *receive*, and where are the unresolved integration gaps?

**Constraint check**: integration *must not require* SCC canonical or PAI canonical edits (per Pass 12 discipline). Any natural integration point that requires substrate modification is flagged as out-of-scope risk.

---

## Contribution Matrix

### What each framework provides

| Framework | Primitives | Structure | Operational anchors |
|-----------|-----------|-----------|----------------------|
| SCC (substrate-canonical, CV-1.13) | $u_t : X_t \to [0,1]$ cohesion field | Energy functional $E[u]$ with 4 terms; gradient flow dynamics; diagnostic vector (Bind, Sep, Inside, Persist) | 215 unit tests; 59 Cat A theorems; spinodal phase transition |
| PAI (substrate-canonical, PIVOT-2026-05-21) | Perception interpretation $\mathcal{I}^P$; action interpretation $\mathcal{I}^A$; PA-formation | $\Delta_{\text{interp}}$ vocabulary (DEFINITION-DRAFT); duality | PAI categorical vocabulary; PA-formation classification |
| PFE (constructed in 12_; weakened in 13-17_) | Event $(t, x)$; stage rate $c_p^{(s)}$ (convention-dep); perception cone $\mathcal{C}^{(s)}$; per-stage metric $g^{(s)}_{\mu\nu}$ | Einstein-form field equation (quasi-static only); local Lorentz metric per stage; geodesic equation | 4 operational tests (Phase C protocols); 15 OPs registered |

### What each framework needs from the others

| Framework | Needs from SCC | Needs from PAI | Needs from PFE |
|-----------|----------------|----------------|----------------|
| SCC | (self-contained) | nothing direct | nothing — PFE proposes *application* of SCC, not modification |
| PAI | $\Delta_{\text{interp}}$ operationalization candidate (Wasserstein, via SCC transport.py) | (self-contained) | bridge propositions (Task 25 Bridge 1-3); empirical $\epsilon$ calibration |
| PFE | $E[u]$ as stress-energy source (Iter 8); $u$ as cohesion field; `transport.py` for OT-based $\Delta_{\text{interp}}$ | $\mathcal{I}^P, \mathcal{I}^A$ definitions; PA-formation criterion (for Bridge 1) | (self-constructed; subject to verification by Pass 12) |

### Asymmetry

SCC is fully **upstream** — it provides primitives + dynamics + diagnostics to both PAI and PFE without requiring anything back.

PAI is **upstream of PFE** for $\Delta_{\text{interp}}$ formalization but **downstream of SCC** for its operational $\Delta$ choice.

PFE is **downstream of both** — it *applies* SCC's $E[u]$ via field-equation coupling, and *operationalizes* PAI's $\Delta_{\text{interp}}$ via Wasserstein.

---

## Integration Map (Dependency Diagram)

```
              SCC (substrate)
              ├── u_t cohesion field
              ├── E[u] = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd + λ_tr E_tr
              ├── gradient flow dynamics
              ├── diagnostic vector (Bind, Sep, Inside, Persist)
              └── transport.py (Sinkhorn OT)
                      |
                      | (provides via application, no SCC modification)
                      v
              PFE (constructed Pass 11; verified Pass 12)
              ├── stress-energy: T_μν^perception := variational derivative of (sqrt(-g) E[u])
              ├── per-stage metric: g_μν^(s) = diag(-c_p^(s)2, 1, 1)
              ├── field equation: G_μν^(s) = κ^(s) T_μν^perception   (Newton-Cartan-like, equilibrium-effective)
              ├── 4 operational tests (Phase C)
              └── 15 OPs (5 original + 10 Pass 12)
                      |
                      | (proposes via bridges, requires PAI substrate decision)
                      v
              PAI (substrate; Δ_interp in DEFINITION-DRAFT)
              ├── perception interpretation I^P
              ├── action interpretation I^A
              ├── PA-formation criterion (currently informal)
              └── Δ_interp (operational form proposed: Wasserstein W_2 from PFE-ground metric)
```

### Bidirectional flows (already permitted)
- SCC → PFE: $u, E, \text{transport}$ via application (no SCC change)
- SCC → PAI: via Δ_interp's computation infrastructure (transport.py)
- PFE → PAI: bridge propositions 1-3 from Task 25 (conditional on PAI substrate decision)
- PAI → PFE: $\mathcal{I}^P, \mathcal{I}^A$ as observer-class identification for P1

### Bidirectional flows (currently blocked by discipline)
- PFE → SCC: any modification of $E[u]$ (e.g., precision-weighted from Friston) — would require SCC canonical edit
- PFE → PAI: committing $\Delta_{\text{interp}}^{(W_2)}$ as PAI canonical operationalization — would require PAI canonical edit
- SCC → PAI: direct identification of PA-formation with SCC formation set — would require PAI canonical edit

---

## Natural Integration Points

### IP-1: SCC stress-energy in PFE
**What**: $T_{\mu\nu}^{\text{perception}} := (2/\sqrt{-g}) \delta(\sqrt{-g} E[u]) / \delta g^{\mu\nu}$

**Compliance**: APPLICATION of SCC; no modification.

**Status**: Defined in Iter 8; structural soundness verified in Phase B Task 6 (dimensional consistency).

**Open issue**: Task 22 dissipative-vs-conservative inconsistency. PFE-SCC dynamical coupling is well-posed only in quasi-static regime.

### IP-2: SCC transport infrastructure → Wasserstein $\Delta_{\text{interp}}$
**What**: `CODE/scc/transport.py` provides Sinkhorn $W_2$; used to compute $\Delta_{\text{interp}}^{(W_2)}$ between PAI's perception/action outcome measures.

**Compliance**: APPLICATION of SCC `transport.py`; no modification.

**Status**: Recommended in Task 25 (Phase F-2). PAI substrate commitment required to formalize as $\Delta_{\text{interp}}$ definition.

### IP-3: PAI observer-class for PFE P1
**What**: PFE's P1 requires equivalence class $\mathcal{O}$ of observers. PAI distinguishes perception observer-class from action observer-class. Natural identification: PFE's $\mathcal{O}$ for "perception cone" = PAI's perception observer-class.

**Compliance**: PAI provides observer-class taxonomy; PFE uses it. No modification needed.

**Status**: Currently informal. Could be formalized as "PFE's $\mathcal{O}$ ⊆ PAI's $\mathcal{I}^P$" without canonical change.

### IP-4: PFE bridges as PAI characterization
**What**: PFE proposes "PA-formation ⟺ small Wasserstein distance between P-measure and A-measure" (Bridge 1).

**Compliance**: PROPOSAL conditional on PAI accepting Wasserstein operationalization.

**Status**: Out of Pass 12 scope (PAI substrate decision required).

---

## Unresolved Gaps

### Gap 1: SCC dynamical-vs-effective tension (Task 22)
PFE's field equation assumes energy-momentum conservation (Bianchi identity). SCC's gradient flow is dissipative — does not conserve energy. Resolution: PFE is *effective-equilibrium* theory only. SCC is *dynamical* theory.

**Implication**: PFE cannot describe SCC's transient dynamics. They are *complementary regimes*, not unified.

### Gap 2: $\kappa^{(s)}$ empirical undetermined
Tasks 6-7 established $[\kappa^{(s)}] = L$ with $\kappa^{(s)} = c \cdot \ell_s$ candidate. The dimensionless prefactor $c$ is unknown. Without it, PFE has $S$ free parameters (one per stage).

**Implication**: PFE not predictively closed until OP-PFE-2 resolved (Pass 13+).

### Gap 3: Postulate count overhead (Task 3)
σ derivation actually requires 4 implicit hypotheses (I1-I4) beyond P1, P2. The clean "2 postulates" claim was overstated.

**Implication**: Framework is honestly *6 commitments*, not *2*. Aesthetic loss; content unchanged.

### Gap 4: PAI substrate decision blocking
Task 25 recommends Wasserstein $\Delta_{\text{interp}}$; bridges 1-3 conditional on PAI accepting. Without PAI substrate commitment, PFE's PAI-side connection is *suggestive*, not *binding*.

**Implication**: Three-framework integration is *partial* until PAI substrate moves $\Delta_{\text{interp}}$ from DEFINITION-DRAFT to committed operationalization.

### Gap 5: Test execution barrier
Phase C established 4 protocols, but only Test 1 is immediately executable (Chichilnisky CRCNS data, Task 15). Tests 2-4 require new experiments (months-years + funding).

**Implication**: Framework remains *measurement scaffold* (Pass 11 Iter 21 register). *Truth* awaits empirical execution.

---

## Discipline-Violation Risks (avoid in Pass 12 and beyond)

### Risk A: Tempting "fix" by SCC modification
Task 24 noted Friston/Fisher/L1 alternatives have features SCC lacks (precision-weighting, sparsity, scale-invariance). Tempting fix: *augment* SCC $E[u]$ with these features.

**Why this is a violation**: Augmenting SCC requires SCC canonical edit. Pass 12 discipline = 0 SCC modifications.

**Correct response**: Test alternatives in mixed-strategy PFE (Task 24 recommendation) without modifying SCC. If empirical winner is non-SCC, the *next* substrate question is for whoever owns SCC canonical to decide.

### Risk B: Tempting "fix" by PAI substrate commitment
Task 25 recommends Wasserstein. Tempting fix: commit it to PAI canonical and proceed.

**Why this is a violation**: PAI substrate commitment requires PAI canonical edit. Out of Pass 12 scope.

**Correct response**: Document recommendation as *conditional proposal*; flag as PAI substrate dependency; do not advance.

### Risk C: Tempting promotion of PFE to canonical track
Pass 12 establishes that PFE survives 18 adversarial patterns (15 from Pass 3-9 + 3 from Phase E). Tempting fix: promote PFE to canonical/.

**Why this is a violation**: PFE is *working/sensing_pipeline* register; canonical promotion requires the promotion pipeline (working → canonical with proofs, audit, etc.). Plus PFE is *measurement scaffold* not *theorem*.

**Correct response**: Keep PFE as working-level construction. Pass 13+ may consider promotion of *individual* sub-claims (e.g., dimensional consistency theorem from Task 6) if they meet promotion criteria.

---

## Aggregate Task 26 verdict

**PASS the integration mapping**. Confidence: high.

The three-framework integration is **structurally well-defined** with clear contribution directions, 4 natural integration points, and 5 explicit unresolved gaps. Discipline preserved (0 canonical edits proposed). 

### Most important integration insight
PFE is **structurally downstream** of both SCC and PAI. It *applies* SCC (via stress-energy) and *operationalizes* PAI (via Wasserstein $\Delta_{\text{interp}}$). PFE is *not* a third independent framework — it is a *coupling layer* that connects SCC's energy structure to PAI's observer-class structure via Einstein-form geometry.

This framing changes the empirical status: PFE's "truth" is *the truth of the coupling*, not a separate empirical claim. Tests 1-4 measure *whether the SCC↔PAI coupling has Einstein form*. If not, PFE form is wrong; SCC and PAI substrates persist independently.

### What was NOT done
- No SCC modification proposed
- No PAI substrate commitment
- No PFE promotion
- No integration diagram formal proof (just informal map)
- No multi-framework theorem proved

---

*Phase F Task 26 v0. Three-framework integration map established. 4 natural integration points; 5 unresolved gaps; 3 discipline-violation risks flagged. PFE positioned as coupling-layer between SCC + PAI substrates. canonical/SCC/PAI/8-retractions 0 modifications. Phase F complete. Next: Phase G consolidation (Task 27) in 21_pass12_final_report.md.*
