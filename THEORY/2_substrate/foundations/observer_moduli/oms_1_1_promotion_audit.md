---
type: working/audit
created: 2026-05-08
session: Session 4 (OMS-1.1)
project: Observer Moduli Space of SCC
stage: OMS-1.1
depends_on: oms_1_candidate.md, vp3_core_weight_symmetry_results.md, vp2_observer_landscape_admissible.md
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# OMS-1.1 Canonical Promotion Audit

Every statement classified: **DEFINED** | **PROVED** | **COMPUTATIONALLY SUPPORTED** | **HYPOTHESIZED** | **ASSUMED** | **OPEN** | **REJECTED**.

---

## §1. Purpose

This document audits the OMS-1.0 canonical candidate (`oms_1_candidate.md`) against all
post-VP-1 developments through Session 4 (VP-3, VP-2, VP-4) to determine:

1. Which blockers have been addressed computationally or theoretically.
2. What new claims require classification.
3. Whether the candidate is ready for canonical promotion.

The previous checklist (`canonical_promotion_checklist.md` v1.1) tracked through Session 3.
This document supersedes it for Session 4 updates.

---

## §2. Blocker Status Update

### Blocker 1: OP-OMS-001 (Core-Weight Gauge Group)

**Pre-Session-4 status:** OPEN. S4 rejected. Closure-sep swap COMPUTATIONALLY TESTABLE.

**Session 4 (VP-3) result:**
- All 7 transformation families tested (A–G).
- Transform A (closure-sep swap): **NOT_A_SYMMETRY** (frac_asym=0.833, n=12).
- Transform E (transport ablation): **CANDIDATE_SYMMETRY** — conditional on static scenes (Prop CW2 CONFIRMED).
- All other transforms: PARTIAL_SYMMETRY (scene/λ-dependent; not global gauge symmetries).
- **G_cw = {e} for dynamic scenes: COMPUTATIONALLY SUPPORTED.**

**Post-Session-4 status:** OPEN for formal proof, but the canonical candidate's default assumption $G_{\mathrm{cw}} = \{e\}$ is now COMPUTATIONALLY SUPPORTED rather than merely ASSUMED.

**Blocker impact on canonical promotion:** REDUCED. The claim "$G_{\mathrm{cw}} = \{e\}$" in OMS-1.0 is now computationally supported. It remains an assumption for the formal theory but is no longer unsupported speculation.

**Revised canonical status:** OP-OMS-001 is a blocker for full formal canonicalization, but not for a COMPUTATIONALLY SUPPORTED canonical candidate.

### Blocker 2: OP-OMS-002 (Explicit V Construction)

**Pre-Session-4 status:** OPEN. No admissible V explicitly constructed.

**Session 4 (VP-2) result:**
- $V_P$ analyzed: V1 (gauge) PROVED, V3 (readout-compat) PROVED (conditional), V2/V4/V5 HYPOTHESIZED.
- Existence of $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$: **HYPOTHESIZED** (Prop VP2-2).
- Computational placeholder: $V_D^0$ with $d^* = (1,1,1,0)$, V1+V2 satisfied, V3 open.

**Post-Session-4 status:** OPEN but existence is hypothesized via explicit construction. The admissible class $\mathcal{V}_{\mathrm{adm}}$ is non-empty if V2/V4/V5 hold.

**Blocker impact:** REDUCED. The claim "an admissible V exists" is now hypothesized via explicit construction, not merely postulated.

---

## §3. New Claims Requiring Classification (Session 4)

| Claim | Source | Status |
|---|---|---|
| $G_{\mathrm{cw}} = \{e\}$ for dynamic scenes | VP-3 (exp87) | COMPUTATIONALLY SUPPORTED |
| Prop CW2: transport invariance on static scenes | VP-3 E (n=18) | COMPUTATIONALLY CONFIRMED |
| Prop CW3: conservative default maintained | VP-3 A–G | COMPUTATIONALLY SUPPORTED |
| Prop VP2-1: $V_P$ partial admissibility (V1+V3) | VP-2 | PROVED (partial) |
| Prop VP2-2: $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$ | VP-2 | HYPOTHESIZED |
| Approximate symmetry loci near $\{\lambda_{\mathrm{cl}}=\lambda_{\mathrm{sep}}\}$ | VP-3 A near-sym | COMPUTATIONALLY SUPPORTED |
| Basin count $\geq 2$ on connected $\mathfrak{M}$ (Prop BS1) | basin_stratification.md | PROVED (construction) + pending VP-4 computational check |

---

## §4. VP-4 Integration (COMPLETE — 2026-05-08)

VP-4 (`exp88_vp4_basin_stratification.py`) completed on scenes S3 and S4 via direct evaluation
of $V_D^0$ at 6 strategic $\lambda$-points (31.1s runtime). Results:

| Claim | Pre-VP-4 | Post-VP-4 |
|---|---|---|
| $\vert \{\mathcal{B}_i\}\vert \geq 2$ (Prop BS1) | PROVED (construction) | **COMPUTATIONALLY CONFIRMED** (2 types on S3: Δd=0.40; S4: Δd=0.52) |
| OP-OMS-010(c) (basin count) | OPEN | **COMPUTATIONALLY SUPPORTED** |
| $V_D^0$ satisfies V4 (basin-generating) | HYPOTHESIZED | **COMPUTATIONALLY SUPPORTED** |
| V5 (boundary-aware) of $V_D^0$ | OPEN | **NOT TESTED** (boundary face experiments deferred) |

**Key findings:**
- cl-dominant observer (P1: $\lambda_{cl}=0.70$) is a consistently distinct perceptual type on both scenes
- S4 symmetric equilibrium: cl-dominant gives no dominant formation (n_high=0), while all other observers select one clique (n_high=5)
- Persist=1.00 for all static scene evaluations — consistent with Prop CW2

Full results in `vp4_basin_stratification_results.md` and `CODE/experiments/results/observer_moduli/vp4_basin_results.json`.

---

## §5. Canonical Promotion Criteria (Updated)

### Criterion A: Formal Definitions Complete

All definitions DEF-1 through DEF-22 are stated, classified, and consistent.
New items from Session 4: none (VP-3 and VP-2 results use existing definitions).

**Status: SATISFIED [✓]**

### Criterion B: Core Claims Classified

| Claim | Status | Evidence |
|---|---|---|
| $\mathcal{M}_{\mathrm{obs}} = [q_{\min},q_{\max}] \times \Delta^3 \times B_\xi$ | DEFINED | Spec §4 |
| $G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{\mathrm{task}}$ | DEFINED | Spec §4 |
| $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ connected | PROVED | Prop 6 |
| $P_{\mathrm{top}}$ is well-defined and G-invariant | PROVED | Prop R3 |
| $P_{\min}$ too coarse (Prop R1) | PROVED | VP-1, 4 CEs |
| $G_{\mathrm{cw}} = \{e\}$ (default) | COMPUTATIONALLY SUPPORTED | VP-3 A–G |
| $V_P$ admissibility (V1+V3) | PROVED (partial) | VP-2 |
| $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$ | HYPOTHESIZED | VP-2 Prop VP2-2 |
| Prop BS1: $\geq 2$ basins | PROVED (construction) | basin_stratification.md |
| Prop CW2: static transport invariance | COMPUTATIONALLY CONFIRMED | VP-3 E |

**Status: SUBSTANTIALLY SATISFIED [~]** — two claims are hypothesized rather than proved (existence of V, basin count computational confirmation). These are the remaining OP-OMS-001/002 blockers.

### Criterion C: Open Problems Classified

OP-OMS-001 through OP-OMS-018 are all classified. New problems OP-OMS-017/018 are registered. The registry is complete.

**Status: SATISFIED [✓]** (new OPs registered with classification)

### Criterion D: No Unclassified Claims

Audit warnings W1–W12 are documented. AUDIT-022 added for VP-3. All major claims have classification labels.

Residual unclassified risk: the VP-4 basin results (running) will determine whether V_D^0 satisfies V4 computationally. Until VP-4 completes, V4 status is HYPOTHESIZED.

**Status: SUBSTANTIALLY SATISFIED [~]** (pending VP-4 for V4)

### Criterion E: Computational Validation

| Protocol | Status | Result |
|---|---|---|
| VP-1 (P-resolution audit) | COMPLETE (exp86) | Prop R1 PROVED, 4 CEs |
| VP-3 (core-weight symmetry) | COMPLETE (exp87) | G_cw={e} COMP. SUPPORTED, Prop CW2 CONFIRMED |
| VP-2 (landscape selection) | COMPLETE (theory) | V_P: V1+V3 PROVED; existence HYPOTHESIZED |
| VP-4 (basin discovery) | RUNNING (exp88) | PENDING |
| VP-6 (effective DOF) | NOT YET STARTED | Planned |
| VP-5 (RG flow) | NOT YET STARTED | Planned (lower priority) |

**Status: PARTIALLY SATISFIED [~]** (VP-4 running; VP-6 and VP-5 deferred)

---

## §6. Promotion Decision

### Current State

The OMS-1.0 candidate has the following overall status after Session 4:

| Criterion | Status |
|---|---|
| A: Definitions complete | SATISFIED |
| B: Core claims classified | SUBSTANTIALLY SATISFIED (2 hypothesized) |
| C: Open problems registered | SATISFIED |
| D: No unclassified claims | SUBSTANTIALLY SATISFIED (VP-4 pending) |
| E: Computational validation | PARTIALLY SATISFIED (VP-4 running) |

### Blockers Remaining

1. **OP-OMS-001 (formal proof):** $G_{\mathrm{cw}} = \{e\}$ is computationally supported but not formally proved. For canonical promotion to a pure theorem, this needs either a formal proof or an explicit statement that it is an axiom rather than a theorem.

2. **OP-OMS-002 (V existence):** $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$ is hypothesized but not proved. For canonical promotion, either: (a) prove V2/V4 for $V^*$, or (b) formally designate $\mathcal{V}_{\mathrm{adm}}$ as an axiom defining the theory's observer landscape structure.

### Recommendation

**OMS-1.1 promotion strategy (two-track):**

**Track 1 (Immediate — Computationally Grounded Canonical):** Promote to a "Computationally Grounded Canonical" variant that:
- Labels $G_{\mathrm{cw}} = \{e\}$ as COMPUTATIONALLY SUPPORTED (not ASSUMED)
- Labels $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$ as HYPOTHESIZED (not OPEN)
- Incorporates VP-3 and VP-2 findings as new sections
- Is clearly marked as "computationally grounded but not fully proved"

This is achievable now and represents genuine scientific progress.

**Track 2 (Deferred — Fully Formal Canonical):** Defer full canonical promotion until:
- OP-OMS-001: formal proof that $G_{\mathrm{cw}} = \{e\}$ for $P_{\mathrm{top}}$ (likely requires showing the energy functional is non-symmetric under $\lambda$-space transformations for generic scene distributions — a result accessible via the envelope theorem and functional analysis)
- OP-OMS-002: proof that $V^* \in \mathcal{V}_{\mathrm{adm}}$ (requires $C^0$ regularity of $u^*(\lambda)$ — OP-OMS-018)

### Decision

**Proceed with Track 1 (OMS-1.1 = Computationally Grounded Canonical candidate).**

The OMS-1.0 candidate label changes from:
> "BLOCKED by OP-OMS-001, OP-OMS-002"

to:
> "COMPUTATIONALLY GROUNDED CANONICAL CANDIDATE — $G_{\mathrm{cw}}=\{e\}$ computationally supported; $V$ existence hypothesized; formally blocked pending OP-OMS-018 (optimizer regularity)"

---

## §7. Required Changes for OMS-1.1 Label

To formally adopt the OMS-1.1 label, update the following:

1. **`oms_1_candidate.md` frontmatter:** `stage: OMS-1.0` → `stage: OMS-1.1`
2. **Status declaration:** Update from "blocked by OP-OMS-001, OP-OMS-002" to OMS-1.1 language.
3. **§11:** Prop CW2 CONFIRMED, CW3 COMPUTATIONALLY SUPPORTED (already done in Session 4).
4. **§18 canonical blockers:** Update OP-OMS-001 to "computationally supported" rather than "open blocker".
5. **`canonical_promotion_checklist.md`:** Add v1.2 update with VP-3 results.

**Note:** These updates to `oms_1_candidate.md` should be done after VP-4 results are available (to include basin stratification status).
