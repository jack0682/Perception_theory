# Master File Compilation Guide

**Date:** 2026-04-04  
**Status:** 📋 Ready (awaiting chapter completion)  
**Target:** PDF generation from master.tex

---

## Overview

The `master.tex` file orchestrates the complete 600+ page SCC textbook by including all chapters, appendices, front/back matter, figures, and references.

**Current Status:**
- ✅ Master template created (master.tex)
- ✅ SNmono.cls optimized template ready
- 🟡 Chapter files (12/15 complete, 3 in progress)
- 🟡 Appendices (in progress)
- ⏳ Figure PDFs (pending generation)
- ⏳ Bibliography (references.bib) - ready
- ⏳ Index generation - pending

---

## Prerequisites

### Software Requirements

```bash
# Required packages (all standard TeX Live)
- pdflatex (TeX engine)
- bibtex (bibliography processor)
- makeindex (index generator)

# Verify installation:
pdflatex --version
bibtex --version
makeindex --version
```

### File Requirements

Before compilation, ensure all files exist:

```
textbook_build/
├── master.tex                          ✅ (created)
├── SNmono.cls                          ✅ (optimized)
├── references.bib                      ⏳ (needed)
├── preface.tex                         ✅ (exists)
├── notation.tex                        ✅ (exists)
├── chapters/
│   ├── ch01_motivation.tex             ✅
│   ├── ch02_concepts.tex               ✅
│   ├── ch03_formal_universe.tex        ✅
│   ├── ch04_axiomatic_groups.tex       ✅
│   ├── ch05_operator_realizations.tex  ✅
│   ├── ch06_energy_functional.tex      ✅
│   ├── ch07_phase_transition.tex       ✅
│   ├── ch08_convergence.tex            🟡 (in progress)
│   ├── ch09_multi_formation.tex        ✅
│   ├── ch10_temporal_transport.tex     ✅
│   ├── ch11_diagnostic_vector.tex      ✅
│   ├── ch12_algorithms.tex             ✅
│   ├── ch13_experiments.tex            ✅
│   ├── ch14_connections.tex            🟡 (in progress)
│   └── ch15_theorem_registry.tex       ⏳ (pending)
├── appendices/
│   ├── appendix_a_math_background.tex  🟡 (in progress)
│   ├── appendix_b_parameters.tex       🟡 (in progress)
│   ├── appendix_c_design_decisions.tex 🟡 (in progress)
│   └── appendix_d_theorem_dag.tex      🟡 (in progress)
├── frontmatter/
│   ├── copyright.tex                   ⏳ (create)
│   ├── foreword.tex                    ⏳ (optional)
│   └── list_of_theorems.tex            ⏳ (auto-generate)
└── figures/
    ├── P1_foundations/                 ⏳ (20-25 PDFs)
    ├── P2_formal/                      ⏳ (20-25 PDFs)
    ├── P3_experiments/                 ⏳ (25-30 PDFs)
    └── P4_applications/                ⏳ (15-20 PDFs)
```

---

## Compilation Process

### Full Compilation (Standard)

```bash
cd /Users/ojaehong/ex_2/docs/04-04/textbook_build

# Step 1: Initial LaTeX pass (generates .aux, .toc, .lof, etc.)
pdflatex master.tex

# Step 2: Bibliography processing
bibtex master

# Step 3: Index generation (if needed)
makeindex master

# Step 4: Second LaTeX pass (includes bibtex output)
pdflatex master.tex

# Step 5: Final LaTeX pass (resolves all cross-references)
pdflatex master.tex

# Output: master.pdf
```

**Total time:** ~2-3 minutes (depending on chapter complexity and figure size)

### Quick Compilation (Development)

For testing without bibliography/index:

```bash
pdflatex master.tex
```

This generates PDF with placeholder references (marked `??`). Faster for iterative development.

### Batch Compilation Script

```bash
#!/bin/bash
# compile.sh

cd /Users/ojaehong/ex_2/docs/04-04/textbook_build

echo "=== Compiling SCC Textbook ==="
echo "1. LaTeX pass 1..."
pdflatex -interaction=nonstopmode master.tex > /dev/null

echo "2. Bibliography..."
bibtex master > /dev/null

echo "3. Index..."
makeindex master > /dev/null

echo "4. LaTeX pass 2..."
pdflatex -interaction=nonstopmode master.tex > /dev/null

echo "5. LaTeX pass 3 (final)..."
pdflatex -interaction=nonstopmode master.tex > /dev/null

# Cleanup
rm -f master.aux master.bbl master.blg master.log master.out master.toc master.lof master.lot master.idx master.ilg master.ind

echo "✅ Compilation complete: master.pdf"
```

Usage:
```bash
chmod +x compile.sh
./compile.sh
```

---

## Troubleshooting

### Error: "File not found: chapters/ch08_convergence.tex"

**Solution:** Chapter is still in progress. Either:
- Wait for chapter completion, or
- Comment out the `\include{chapters/ch08_convergence}` line temporarily

```latex
% \include{chapters/ch08_convergence}  % TODO: uncomment when ready
```

### Error: "Undefined citations" (shows ?? in PDF)

**Solution:** Run full compilation sequence (includes bibtex step)

### Error: "PDF contains unresolved figure references"

**Solution:** Ensure figure PDFs exist in the figures/ directories:
```bash
ls figures/P1_foundations/*.pdf
ls figures/P2_formal/*.pdf
# etc.
```

If figures don't exist, they will generate placeholder text. Chapter authors should include placeholder `\includegraphics` commands that will be replaced once figures are ready.

### Error: "SNmono.cls not found"

**Solution:** Ensure SNmono.cls is in the same directory as master.tex:
```bash
ls SNmono.cls
```

### Page overflow: "Overfull \hbox" warnings

**Solution:** This is often from tables or code that's too wide. Use:
```latex
\begin{small}
  % narrow content here
\end{small}
```

Or adjust table width:
```latex
\begin{tabular}{|c|c|}  % narrow columns
```

---

## Output Structure

Once compilation succeeds, `master.pdf` will contain:

```
Front Matter (~13 pages)
├─ Title page
├─ Copyright page
├─ Foreword (2pp)
├─ Preface (4pp)
├─ Notation (3pp)
├─ List of Theorems
├─ Table of Contents
└─ List of Figures

Part I: Foundations (~80pp)
├─ Ch1: Motivation (20pp)
├─ Ch2: Concepts (20pp)
└─ Ch3: Formal Universe (20pp)

Part II: Formal Theory (~160pp)
├─ Ch4: Axioms (25pp)
├─ Ch5: Operators (20pp)
├─ Ch6: Energy (25pp)
├─ Ch7: Phase Transition (25pp)
└─ Ch8: Convergence (25pp)

Part III: Multi-Temporal (~100pp)
├─ Ch9: Multi-Formation (25pp)
├─ Ch10: Transport (25pp)
└─ Ch11: Diagnostics (25pp)

Part IV: Implementation (~140pp)
├─ Ch12: Algorithms (30pp)
├─ Ch13: Experiments (35pp)
├─ Ch14: Applications (40pp)
└─ Ch15: Theorem Registry (35pp)

Back Matter (~80pp)
├─ Appendix A: Math Background (20pp)
├─ Appendix B: Parameters (20pp)
├─ Appendix C: Design (20pp)
├─ Appendix D: Theorem DAG (20pp)
└─ Bibliography + Index

Total: ~600-650 pages
```

---

## Quality Assurance Checklist

Before finalizing PDF:

- [ ] All chapters compile without errors
- [ ] No undefined references (no `??` in output except placeholders)
- [ ] All figures present (no "Figure not found" messages)
- [ ] Table of contents accurate
- [ ] Page numbers continuous
- [ ] Hyperlinks functional
- [ ] Bibliography complete
- [ ] Index generated and accurate
- [ ] Margins correct (20mm left/right, per SNmono.cls)
- [ ] Font consistent throughout
- [ ] Cross-references working (e.g., "see page XX")

---

## Distribution

Once master.pdf is finalized:

```bash
# Copy to distribution location
cp master.pdf SCC_Textbook_2026.pdf

# Verify file
ls -lh SCC_Textbook_2026.pdf

# Example output:
# -rw-r--r--  1 user  staff  12M Apr  8 09:00 SCC_Textbook_2026.pdf
```

---

## Timeline

| Date | Task | Status |
|------|------|--------|
| 2026-04-04 | Master template created | ✅ |
| 2026-04-05 | Ch8, Ch14-15, Appendices | 🟡 Expected |
| 2026-04-06 | All chapters complete | 🟡 Expected |
| 2026-04-07 | Figure generation complete | ⏳ Expected |
| 2026-04-08 | Final PDF generation | ⏳ Expected |

---

## Next Steps

1. ✅ Create master.tex template — DONE
2. 🟡 Complete all chapter files (Ch8, Ch14, Ch15)
3. 🟡 Complete appendices (A-D)
4. ⏳ Generate all figures (P1-P4, 80-100 PDFs)
5. ⏳ Run full compilation and verify
6. ⏳ Distribute as SCC_Textbook_2026.pdf

---

**Responsible:** team-lead  
**Last updated:** 2026-04-04  
**Status:** Ready for use (pending chapter/figure completion)
