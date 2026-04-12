---
title: Papers & Publication Index
type: index
last_updated: 2026-04-12
total_papers: 2
---

# Papers & Publication — 11_papers/

Central registry and working directory for publication-ready manuscripts.

## Current Papers

### Paper 1: Mathematical Formulation
- **Status:** Draft (IEEEtran format)
- **File:** `paper1_math.tex`
- **Length:** ~11 pages
- **Target:** IEEE/mathematical audience
- **Contents:**
  - SCC axioms (A-0001 through A-0022)
  - 27 Category A theorems
  - Formal definitions and proofs
  - Energy formulation

### Paper 2: Cognitive Science & Integration
- **Status:** Draft (IEEEtran format)
- **File:** `paper2_cogsci.tex`
- **Length:** ~14 pages
- **Target:** Cognitive science audience
- **Contents:**
  - Motivation (pre-objective formation)
  - Soft cohesion field interpretation
  - Gestalt mapping
  - Predictions (P1–P5)
  - Embodied AI implications

## Paper Structure

```
11_papers/
├── outlines/
│   ├── paper1_math_outline.md
│   ├── paper2_cogsci_outline.md
│   └── v2.0_paper_kinetic_outline.md
├── sections/
│   ├── section_1_foundations.tex
│   ├── section_2_axioms.tex
│   ├── section_3_theorems.tex
│   └── [others]
├── figures/
│   └── [symlinks to 14_figures/exported/]
├── bibliography/
│   ├── references.bib
│   └── cited_works.md
├── drafts/
│   ├── paper1_math.tex
│   ├── paper2_cogsci.tex
│   └── v2.0_kinetic_framework.tex
└── compiled/
    ├── paper1_math.pdf
    ├── paper2_cogsci.pdf
    └── [future: paper3_kinetic.pdf]
```

## Version History

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v1.0 | 2026-03-XX | Outline | Initial structure |
| v1.1 | 2026-04-XX | Draft | First complete draft |
| v2.0 | 2026-05-24 | Planned | Kinetic framework (Option C) |

## Future: Paper 3 (Kinetic Theory)

**Planned for v2.0 release (2026-05-24):**
- T-Kinetic-1, T-Kinetic-2, T-Kinetic-3 proofs
- exp81–exp85 results
- K-selection mechanism explanation
- Resolution of F-1/M-1/MO-1

## Compilation Commands

```bash
# Compile paper1
cd /Perception_theory/11_papers/drafts
pdflatex paper1_math.tex
pdflatex paper1_math.tex  # Run twice for refs

# Compile paper2
pdflatex paper2_cogsci.tex
pdflatex paper2_cogsci.tex

# Compile paper3 (when ready)
pdflatex v2.0_kinetic_framework.tex
pdflatex v2.0_kinetic_framework.tex
```

## Figure References

All figures referenced in papers link to:
- `14_figures/source/` — Source files (Python, data)
- `14_figures/exported/` — PDF/PNG for inclusion

## Bibliography

Master bibliography: `11_papers/bibliography/references.bib`

**Cited in v1.2:**
- [List of key citations]

**New citations for v2.0:**
- Kramers rate theory
- Large deviations theory
- Stochastic resonance literature

## Publication Checklist

Before release:

- [ ] All theorems have proofs
- [ ] All experiments have results
- [ ] All figures are publication-ready
- [ ] Bibliography is complete
- [ ] Spelling/grammar reviewed
- [ ] Metadata (authors, affiliations, dates) current

---

**Created:** 2026-04-12
**Papers:** 2 (v1.2) + 1 planned (v2.0)
**Next Major Release:** 2026-05-24 (v2.0 with kinetic framework)
