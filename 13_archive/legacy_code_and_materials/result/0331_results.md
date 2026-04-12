# Day 4 Results — 2026-03-31

## 세션 개요
T-Persist-1 Gap 4/5/6 증명 강화, transport 구현, multi-formation temporal theory

---

## 정리 성과

| 정리 | 이전 | 이후 |
|------|------|------|
| T-Persist-1(d) H2 | Hypothesis | H2' **Proved** (|Core|≥25, β/α≫1) |
| T-Persist-1(e) FP | Conditional | **Proved** (Schauder, finite-time flow) |
| T-Persist-1(e) fingerprint | 4-component | **3-component** (C demoted) |
| T-Persist-1(e) μ₀ | 6.3 | **3.4** (tightened) |
| T-Persist-1(b) basin | r≥0.210 universal | **r≥0.210 away from bif** (corrected) |
| Δ_bdy | Unknown | **Quantitative Taylor formula** (cubic, <1% error) |
| ‖∂φ/∂u‖_op | 2.83 | **1.75** (formation-conditional) |
| NB-1 | — | **Proved** (basin collapse Δ=O(μ³)) |
| NB-2 | — | **Proved** (deep-core remnant) |
| T-Persist-Full | — | **Experimentally verified** (exp27: 5/5×5/5=100%) |
| T-Persist chain | — | Stress test 84/100 (exp28, all fail at n<64 or β<20) |

## 실험 결과

| 실험 | 핵심 결과 |
|------|----------|
| exp18 | Deep core: 62/62 존재 (|Core|≥25) |
| exp19 | Soft mode: 90%+ boundary weight |
| exp20 | Fingerprint Jacobian ‖∂φ/∂u‖ = 1.43 |
| exp21-23 | r_soft < 0.210 in 21/32 configs |
| exp24 | Empirical basin 3-12× > sublevel |
| exp25 | Hessian diagonal: boundary 최소 확인 |
| exp26 | Chain: (a)(c)(e) universal, (b)(d) basin-switching |
| **exp27** | **Warm-start: 5/5 × 5/5 = 100% PASS** |
| exp28 | Stress: 84/100, n≥64 β≥20 전부 통과 |

## 문서 생성
- `docs/03-31/proof/` — 5개 증명 문서 (CORE-DEPTH, BASIN-ESCAPE, TRANSPORT-CONCENTRATION, H2-CLOSURE, K-STRONG-MORSE)
- `docs/03-31/repair/` — 6개 수리 문서
- `docs/03-31/theory/` — 2개 이론 문서 (NEAR-BIFURCATION, THREE-REGIME-SYNTHESIS)
- `docs/03-31/synthesis/` — T-PERSIST-FULL-PROOF.md (450줄 통합 증명)
- `scc/transport.py` — 3-component fingerprint, 175 tests

## 코드 변경
- transport.py: 3-component fingerprint default
- 174 → 175 tests

## 남긴 문제
- Strong-regime transport selection/uniqueness
- Near-bifurcation persistence (μ→0)
- Product-manifold basin theory
