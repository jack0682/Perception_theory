---
id: EXPERIMENTS-0001
type: experiments/readme
status: active
created: 2026-04-12
---

# Experiments Layer (09_experiments/)

**Purpose:** Central repository for experimental data, validation scripts, and empirical evidence for theoretical claims.

**Scope:** Contains all exp_ID experiments organized by category, theorem, and date.

---

## Directory Structure

```
09_experiments/
├── README.md (this file)
├── experiments_index.md (master registry, organized by exp_ID, category, theorem)
├── experiments_protocol.md (how to document new experiments)
│
├── 01_single_formation_validation/
│   ├── exp01_lambda_sweep.py
│   ├── exp02_phase_transition.py
│   └── [exp01–exp35 category]
│
├── 02_k_field_investigation/
│   ├── exp46_lambda_coupling_sweep.py
│   ├── exp62_mass_sweep_k2.py
│   └── [exp36–exp73 category]
│
├── 03_type_ab_classification/
│   ├── exp65_formation_tracking.py (Type B validation, result: 0/4 observed)
│   └── [Type A/B investigation, RETRACTED]
│
├── 04_closure_operator/
│   ├── exp30_closure_convergence.py
│   └── [closure experiments]
│
├── 05_predicate_alignment/
│   ├── exp31_predicate_energy_bridge.py
│   └── [diagnostic validation]
│
├── 06_confinement_bounds/
│   ├── exp45_confinement_tight.py
│   └── [T-Persist-1(e) validation]
│
├── 07_persistence_validation/
│   ├── exp47_persistence_multi_form.py
│   └── [T-Persist-K-unified validation]
│
├── [future categories based on Option B/C:]
│   ├── 08_k_selection_mechanism/ [if Option B chosen]
│   │   ├── exp76_bic_model_selection.py
│   │   ├── exp77_free_energy_penalty.py
│   │   └── [K-selection axioms validation]
│   └── 09_kinetic_barriers/ [if Option C chosen]
│       ├── exp81_barrier_height.py
│       ├── exp82_residence_time.py
│       └── [kinetic theory validation]
│
└── data/
    ├── exp01_data.json
    ├── exp02_data.json
    └── [results from each exp run]
```

---

## Organization By Category

### Category 1: Single-Formation Validation (exp1–exp35)

**Theorems Validated:**
- T-1 (Existence)
- T-3 (Stability)
- T-6a/b (Closure fixed points)
- T-8-Core/Full (Phase transition)
- T-14 (Gradient flow)

**Key Experiments:**
- exp01–exp10: λ-sweep, phase transition, ablation studies
- exp30–exp35: Closure operator convergence, confinement bounds

**Status:** ✅ All Category A theorems validated

### Category 2: K-Field Investigation (exp36–exp73)

**Theorems Validated:**
- T-Persist-K-Sep (Category B)
- T-Persist-K-Weak (Category C)
- T-Persist-K-Unified (Category B)

**Key Experiments:**
- exp46–exp47: Λ_coupling parameter sweep, geometric-Lambda agreement
- exp62–exp63: Type A vs Type B classification (later invalidated)
- exp65: Type B validation test (0/4 observed, classification RETRACTED)

**Status:** ⚠️ K-field theorems are Category B/C (conditional)

### Category 3: Kramers Rate Theory & Stochastic (exp54–exp59)

**Purpose:** Explore stochastic dynamics, thermal fluctuations, kinetic barriers

**Key Experiments:**
- exp54–exp59: Thermal fluctuation effects, escape time distributions

**Status:** 🔄 Under investigation (OP-0021 low priority)

---

## Master Experiment Registry

**Location:** experiments_index.md

**Tracks:**
- exp_ID (sequential numbering)
- Theorem validated (which T-xxxx)
- Category (which theorem category A/B/C)
- Date run (YYYY-MM-DD)
- Result (✅ validated, ⚠️ conditional, ❌ invalidated, 🔄 in progress)
- Notes (caveats, assumptions, anomalies)

**Example entry:**
```
exp65: Formation Tracking (Type A/B validation)
- Theorem: (proposed Type A/B classification, later retracted)
- Date: 2026-04-12
- Result: ❌ INVALIDATED (Type B never observed, 0/4 configs)
- Reference: M3_validation.md (OP-0004 Type A/B Classification Invalidation)
```

---

## Experimental Validation Path

### Path 1: Single-Formation Theory
- **Experiments:** exp1–exp35
- **Theorems:** T-1, T-3, T-6a/b, T-8-Core/Full, T-14 (15 Category A)
- **Result:** ✅ All validated, high confidence

### Path 2: K-Field Persistence
- **Experiments:** exp46–exp47
- **Theorems:** T-Persist-K-Sep, T-Persist-K-Weak, T-Persist-K-Unified
- **Result:** ✅ 100% geometric-Lambda agreement (69 configs), but conditional on F-1/M-1

### Path 3: Type A/B Classification (RETRACTED)
- **Experiments:** exp62, exp63, exp65
- **Theorems:** (Type A/B framework, proposed but invalidated)
- **Result:** ❌ Type B never observed, classification RETRACTED

### Path 4: K-Selection Mechanism (IF OPTION B CHOSEN)
- **Experiments:** exp76–exp80
- **Theorems:** T-KSel-1, T-KSel-2, new persistence theorems
- **Result:** Pending (4–6 weeks development + validation)

### Path 5: Kinetic Barriers (IF OPTION C CHOSEN)
- **Experiments:** exp81–exp85
- **Theorems:** T-Kinetic-1, T-Kinetic-2, T-Kinetic-3
- **Result:** Pending (4–6 weeks development + validation)

---

## How to Document a New Experiment

**See:** experiments_protocol.md (detailed procedure)

**Quick steps:**
1. Create exp[ID]_[name].py in appropriate category directory
2. Add YAML header with metadata:
   ```python
   # exp[ID]: [Title]
   # id: EXP-[ID]
   # theorem_tested: T-xxxx or OP-xxxx
   # category: [category name]
   # date: YYYY-MM-DD
   # result: [✅|⚠️|❌|🔄]
   # notes: [any caveats]
   ```
3. Document purpose, method, results in code comments
4. Export data to data/exp[ID]_data.json
5. Register in experiments_index.md
6. Reference in appropriate theorem_registry.md entry

---

## Current Experiment Count

| Category | Exp Range | Count | Status |
|----------|-----------|-------|--------|
| Single-Formation | exp1–exp35 | 35 | ✅ Complete |
| K-Field | exp36–exp73 | 38 | ✅ Complete (conditional) |
| Kramers/Stochastic | exp54–exp59 | 6 | 🔄 In progress |
| **Subtotal** | — | **79** | — |
| K-Selection | exp76–exp80 (future) | 5 | ⏳ If Option B |
| Kinetic Barriers | exp81–exp85 (future) | 5 | ⏳ If Option C |

**Total registered:** 79 (with 10 more planned depending on direction choice)

---

## Integration with Theorems

**Theorem validation flow:**
1. Claim C-xxxx proposed
2. Proof P-xxxx written
3. Experiment exp_ID designed
4. exp_ID run and result recorded
5. Result feeds back to theorem_registry.md → promotion decision
6. (If exp supports claim) → Promote C-xxxx to T-xxxx (Category A/B/C)

**See:** 00_meta/promotion_rules.md (detailed promotion criteria)

---

## Integration with Daily Logs

**Experiment role (Phase 4) logs experiments in:**
- 02_roadmap/04_daily_log/YYYY-MM-DD/session_log_experiment.md

**What gets logged:**
- exp_ID run (which exp, what config)
- Result (✅|⚠️|❌|🔄)
- Anomalies or unexpected behaviors
- Validation status (does it match theory prediction?)
- Next experiments to run

**Each quarter:**
- Archivist consolidates completed exp results → 13_archive/experiments_archive/
- Old exp data moved to archive after 6 months

---

## Experiment Safety & Validation

**All experiments must:**
- ✅ Have docstring explaining purpose
- ✅ Compare against theoretical prediction
- ✅ Report FD (finite difference) error to known precision
- ✅ Save data to data/ directory
- ✅ Register in experiments_index.md
- ✅ Reference related theorem or open problem

**FD Validation Standard:**
- Expected accuracy: 1e-9 (double precision)
- Report: actual error, acceptable tolerance

---

## Next Steps

### Phase 4 (Ongoing)

**Experiment role responsibilities:**
1. Run experiments as planned (based on current open problems)
2. Log in daily_log/YYYY-MM-DD/session_log_experiment.md
3. Register results in experiments_index.md
4. Update theorem validation status in theorem_registry.md
5. Archive old experiment data quarterly (Archivist role)

### Post-Direction Decision (2026-04-13+)

**If Option B (K-Selection Mechanism):**
- Create 08_k_selection_mechanism/ category
- Design exp76–exp80 validation suite
- Run 4–6 weeks of experiments

**If Option C (Kinetic Theory):**
- Create 09_kinetic_barriers/ category
- Design exp81–exp85 validation suite
- Run 4–6 weeks of experiments

---

## See Also

- experiments_index.md (master registry of all exp_ID)
- experiments_protocol.md (how to document new experiments)
- 03_context_memory/theorem_registry.md (theorem validation status)
- 02_roadmap/open_problems.md (which experiments should be run next)
- 02_roadmap/04_daily_log/operational_logging_guide.md (Experiment role procedures)

---

**Last updated:** 2026-04-12  
**Status:** Ready for Phase 4 experiment execution  
**Maintained by:** Experiment role (Phase 4+)
