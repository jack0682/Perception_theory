---
id: RESULTS-0001
type: results/readme
status: active
created: 2026-04-12
---

# Results Layer (10_results/)

**Purpose:** Central repository for processed experimental results, analysis reports, validation metrics, and empirical findings.

**Scope:** Contains outputs from 09_experiments/, organized by category, date, and relevance.

---

## Directory Structure

```
10_results/
├── README.md (this file)
├── results_index.md (master registry, organized by date, category, theorem)
├── results_protocol.md (how to document new results)
│
├── validation_metrics/
│   ├── single_formation_validation.json (exp1–exp35 summary metrics)
│   ├── k_field_validation.json (exp36–exp73 summary metrics)
│   ├── category_a_theorems.json (15 Category A theorems validation status)
│   └── [summary metrics by theorem category]
│
├── error_analysis/
│   ├── fd_error_report_exp1-exp35.json (finite difference errors)
│   ├── fd_error_report_exp36-exp73.json
│   └── [precision analysis by exp range]
│
├── phase_transition_analysis/
│   ├── phase_transition_core.json (T-8-Core validation)
│   ├── phase_transition_full.json (T-8-Full validation)
│   └── [bifurcation analysis]
│
├── k_field_dynamics/
│   ├── k2_energy_landscape.json (exp62, exp63 energy comparison)
│   ├── persistence_multi_formation.json (exp46–exp47 validation)
│   ├── lambda_coupling_analysis.json
│   └── [K-field theorem validation results]
│
├── type_ab_classification/
│   ├── exp65_formation_tracking.json (Type A/B validation data, RETRACTED)
│   ├── type_ab_validation_report.md (Result: INVALIDATED, Type B never observed)
│   └── [Classification retraction documentation]
│
├── critical_findings/
│   ├── F-1_K2_vacuity_analysis.json (K=2 energy paradox)
│   ├── M-1_K1_preference.json (K=1 always cheaper energetically)
│   ├── MO-1_morse_inapplicability.json (Manifold with corners)
│   └── [Critical problem evidence & analysis]
│
├── future_results/ [if Option B/C chosen]
│   └── [Results from exp76–exp85, post-direction decision]
│
└── summary_reports/
    ├── VALIDATION_REPORT_2026-04-12.md (M3 audit summary)
    ├── THEORY_STATUS_2026-04-12.md (complete audit findings)
    ├── weekly_analysis_reports/
    │   └── [Generated weekly by Analyst role, Phase 4+]
    └── quarterly_reviews/
        └── [Generated quarterly, consolidates all results]
```

---

## Result Categories

### Category 1: Validation Metrics (validation_metrics/)

**What:** Summary metrics for each theorem or experiment class

**Format:** JSON with key statistics
```json
{
  "theorem": "T-1",
  "category": "A",
  "experiments": [1, 2, 3],
  "status": "✅ VALIDATED",
  "confidence": "Very high",
  "fd_error": "1e-9 (expected)",
  "validated_date": "2026-04-10",
  "notes": "All single-formation validations converged"
}
```

**Content:**
- Theorem ID and category (A/B/C)
- List of validating experiments
- Validation status (✅/⚠️/❌)
- Confidence level
- FD error metrics
- Date of last validation

### Category 2: Error Analysis (error_analysis/)

**What:** Finite difference (FD) error reports for numerical precision

**Format:** JSON with error distribution
```json
{
  "exp_range": "1-35",
  "category": "Single-Formation Validation",
  "samples": 35,
  "mean_error": 1.2e-9,
  "max_error": 3.4e-9,
  "min_error": 0.5e-9,
  "target_precision": 1e-9,
  "status": "✅ All within tolerance"
}
```

**Use:** Verify numerical reliability of all experiments

### Category 3: Detailed Analysis (phase_transition_analysis/, k_field_dynamics/, etc.)

**What:** In-depth analysis of specific phenomena or theorems

**Format:** JSON + Markdown reports
- Bifurcation diagrams (phase_transition_analysis)
- Energy landscapes (k_field_dynamics)
- Classification results (type_ab_classification)

**Example:** exp65_formation_tracking.json
```json
{
  "exp_id": 65,
  "purpose": "Type A/B classification validation",
  "configs_tested": 4,
  "type_b_observed": 0,
  "status": "❌ INVALIDATED",
  "finding": "Type B configurations never occurred",
  "conclusion": "Type A/B classification hypothesis RETRACTED",
  "reference": "OP-0004, M3_validation.md"
}
```

### Category 4: Critical Findings (critical_findings/)

**What:** Evidence and analysis for critical unresolved problems (F-1, M-1, MO-1)

**Files:**
- F-1_K2_vacuity_analysis.json (K=2 requires external scaffolding)
- M-1_K1_preference.json (K=1 is ~50% cheaper energetically)
- MO-1_morse_inapplicability.json (Manifold with corners invalidates smooth Morse theory)

**Use:** Document empirical evidence for critical problems; support mitigation options

### Category 5: Summary Reports (summary_reports/)

**What:** High-level consolidations of findings, weekly/quarterly

**Files:**
- VALIDATION_REPORT_2026-04-12.md (M3 audit summary, what was validated)
- THEORY_STATUS_2026-04-12.md (complete audit findings, all issues surfaced)
- weekly_analysis_reports/[YYYY-WW]_analysis.md (weekly consolidation by Analyst)
- quarterly_reviews/[YYYY-Q].md (quarterly consolidation)

**Use:** Communicate findings to stakeholders, track progress

---

## Result Organization: By Date vs. By Category

### Option A: Search by Category

**Question:** "What do we know about phase transitions?"

**Path:**
1. Go to 10_results/phase_transition_analysis/
2. Open phase_transition_core.json or phase_transition_full.json
3. Review bifurcation analysis

### Option B: Search by Date

**Question:** "What results did we generate on 2026-04-10?"

**Path:**
1. Go to 10_results/summary_reports/weekly_analysis_reports/
2. Find 2026-16_analysis.md (week 16)
3. Review "Results Generated" section

### Option C: Search by Theorem

**Question:** "Is T-Persist-K-Unified validated?"

**Path:**
1. Go to 10_results/k_field_dynamics/
2. Open persistence_multi_formation.json
3. Check validation status

---

## Master Results Registry

**Location:** results_index.md

**Tracks:**
- result_ID (sequential numbering)
- Category (validation_metrics, error_analysis, critical_findings, etc.)
- Date generated (YYYY-MM-DD)
- Related exp_ID (which experiments generated this result)
- Related theorem (which T-xxxx is validated)
- Status (✅ validated, ⚠️ conditional, ❌ invalidated, 🔄 in progress)
- Location (file path in 10_results/)

**Example entry:**
```
RES-065: Type A/B Classification Validation Result
- Category: type_ab_classification/
- Date: 2026-04-12
- Experiments: exp65 (formation tracking)
- Theorem: (Type A/B classification, later retracted)
- Status: ❌ INVALIDATED (Type B observed 0/4 runs)
- File: 10_results/type_ab_classification/exp65_formation_tracking.json
- Reference: OP-0004
```

---

## Results Workflow

### Step 1: Generate Results (Experiment Role, Phase 4)

**In 09_experiments/:**
1. Run experiment exp_ID
2. Save data to 09_experiments/data/exp[ID]_data.json

### Step 2: Process & Analyze (Analyst Role, Phase 4)

**In 10_results/:**
1. Load exp data
2. Compute metrics (FD error, validation status, etc.)
3. Compare against theoretical prediction
4. Generate analysis JSON or report
5. Log findings in session_log_analyst.md (Phase 4)

### Step 3: Register & Consolidate (Archivist Role, Phase 4)

**At quarter-end:**
1. Create quarterly_reviews/[YYYY-Q].md summarizing all results
2. Archive old result files to 13_archive/experiments_archive/
3. Update results_index.md with new entries

### Step 4: Integrate Back (Lead Role, Phase 4)

**After results ready:**
1. Feed findings back to theorem_registry.md (validation status)
2. Update open_problems.md if results resolve/challenge a problem
3. Update canonical spec if major findings emerge

---

## Validation Terminology

| Status | Meaning | Example |
|--------|---------|---------|
| ✅ VALIDATED | Experiment confirms theory | T-1 existence proved numerically |
| ⚠️ CONDITIONAL | Validated given assumptions | T-Persist-K depends on fixed K (F-1) |
| ❌ INVALIDATED | Experiment contradicts theory | Type A/B classification (exp65) |
| 🔄 IN PROGRESS | Experiment running or pending | K-selection validation (exp76+) |

---

## Critical Results: Evidence for F-1/M-1/MO-1

### F-1: K=2 Vacuity
**Evidence:** 
- exp62, exp63 data: K=2 energy E ≈ 4.66; K=1 energy E ≈ 2.25
- K=1 is ~50% cheaper
- **Result file:** critical_findings/F-1_K2_vacuity_analysis.json

### M-1: K=1 Always Preferred
**Evidence:**
- Direct calculation from energy functional
- Empirical confirmation: exp62, exp63, exp71–exp73
- M₂ landscape monotonically prefers K=1
- **Result file:** critical_findings/M-1_K1_preference.json

### MO-1: Morse Theory Inapplicable
**Evidence:**
- Constrained manifold Σ²_M is manifold with corners
- Smooth Morse theory invalid
- **Result file:** critical_findings/MO-1_morse_inapplicability.json

**See:** THEORY_STATUS_2026-04-12.md for full analysis

---

## Results Quality Standards

**All results must:**
- ✅ Have clear method documentation
- ✅ Report FD/numerical precision
- ✅ Compare against theoretical prediction
- ✅ Be registered in results_index.md
- ✅ Reference related exp_ID or theorem
- ✅ Include date generated and experimental conditions
- ✅ Save raw data (JSON) + analysis (Markdown/JSON)

**FD Validation:**
- Expected accuracy: ≤ 1e-9 (double precision)
- Report actual error achieved
- Flag if error exceeds tolerance

---

## Integration with Daily Logs

**Phase 4 analyst (future role) logs in:**
- 02_roadmap/04_daily_log/YYYY-MM-DD/session_log_analyst.md

**What gets logged:**
- Results processed (which exp data analyzed)
- Metrics computed (FD error, validation status)
- Key findings (matches/mismatches with theory)
- New problems/gaps identified
- Consolidation tasks (weekly/quarterly)

---

## Phase 4 & Beyond

### Phase 4 (Ongoing)

**Weekly consolidation:**
- Analyst role processes results
- Generates weekly_analysis_reports/[WW].md
- Feeds findings back to theorem_registry.md

**Quarterly consolidation:**
- Archivist role consolidates quarter's results
- Generates quarterly_reviews/[Q].md
- Archives old results (6+ month old → 13_archive/)

### Post-Option Decision (2026-04-13+)

**If Option B/C chosen:**
- Create future_results/ subdirectory
- Populate with K-selection or kinetic barrier results (exp76–exp85)
- Integrate new validation metrics

---

## See Also

- results_index.md (master registry of all results)
- results_protocol.md (how to document new results)
- 09_experiments/experiments_index.md (which experiments generate which results)
- 03_context_memory/theorem_registry.md (validation status of all theorems)
- 02_roadmap/open_problems.md (which problems do results address)
- THEORY_STATUS_2026-04-12.md (complete audit findings)

---

**Last updated:** 2026-04-12  
**Status:** Ready for Phase 4 result processing  
**Maintained by:** Analyst role + Archivist role (Phase 4+)
