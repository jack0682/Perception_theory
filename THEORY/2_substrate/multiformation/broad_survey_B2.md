> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q6_sigma_inherit]] · [[sigma_rich_wigner_derivation]] · [[sigma_inherit_k_jump]] · [[sigma_rich_phi_proof]] · [[nq242c_explicit_construction]]

# broad_survey_B2.md — OP-0008 σ_standard MERGE/SPLIT Wigner-Projection 2-Route Attack Framework

**Type**: W8-Day1 Track B PRIMARY broad survey. *Survey only — no proof attempts*. 2-route framework mapping for Day 2-4 OP-0008 attack input.
**Date**: 2026-05-18 (W8-Day1, Mon).
**Author**: Claude session, sole producer.
**Canonical refs**: `canonical.md §11.1 Commitment 14`, `§13 T-σ-multi-A-Static`, `§14 CN5/CN10`, `§15 OP-0008`.
**Working refs**: `sigma_rich_wigner_derivation.md §8.2` (Conjecture 8.1), `sigma_inherit_k_jump.md §3.3 (c)`, `sigma_rich_phi_proof.md §6.2` (Cat A target outline), `nq242c_explicit_construction.md §6` (numerical anchor).
**Pre-work xref check**: 30+ working files reference Wigner-projection / OP-0008 / MERGE-SPLIT. 본 file 의 *novel content* = *2-route mapping* (perturbation theory + RMT) + *convergence framework*; 기존 file 의 *Cat A target outline* 의 *방법론적 확장*. 단순 재정리 아님.

---

## §1. Mission of this broad survey

> **OP-0008 σ_standard MERGE/SPLIT Wigner-projection Cat C → Cat B 승급 path 의 *2-route attack framework* 첫 매핑**. Route (a) = Kato perturbation theory (Reed-Simon IV §XIII.5). Route (b) = RMT (Wigner-Dyson level repulsion). 두 route 의 *수학적 독립성*, *상보적 적용 영역*, *동일 σ_standard map 산출의 수렴 조건* 을 *분석 framework* 형태로 산출. **본 broad survey 는 증명을 시도하지 않는다.** Day 2-3 의 op0008_merge_wigner_{perturbation,rmt}.md 의 *직접 입력*.

W8 strategic plan §2 G3: CV-1.19 SEAL committed target. Day 4 EOD contingency gate A (수렴 시) / Gate B (4 parts partial promotion). 본 file 은 Gate A 진입의 *조건 명시* + Gate B 의 *대체 path* 명시.

---

## §2. Problem statement (precise)

K-jump merger event 에서 두 active formation $(C_{i_1}^t, C_{i_2}^t) \to C_j^s$ 의 σ_standard inheritance:

$$\Phi_{\mathrm{MERGE}}^{\sigma_\mathrm{std}}\;:\; \bigl(\sigma_\mathrm{std}(C_{i_1}^t),\; \sigma_\mathrm{std}(C_{i_2}^t);\; m_{i_1}^t, m_{i_2}^t\bigr) \;\longmapsto\; \sigma_\mathrm{std}(C_j^s)$$

**Open question (OP-0008)**: Is $\Phi_{\mathrm{MERGE}}^{\sigma_\mathrm{std}}$ a *deterministic function* of pre-merger data, or does it require additional post-merger relaxation trajectory information?

**Current status**:
- $\sigma_\mathrm{std}(C_i^t)$ = sorted Hessian eigenvalues of single-formation $u_t^i$ (Commitment 14).
- Post-merger $\sigma_\mathrm{std}(C_j^s)$ = sorted Hessian eigenvalues of single-formation $u_s^j$ at *post-relaxation minimum*.
- Trivial part (centroid + orientation by parallel-axis): **Cat B** (deterministic; `sigma_inherit_k_jump.md §3.3 (b)`).
- σ_standard part: **Cat C** — Conjecture 8.1 of `sigma_rich_wigner_derivation.md §8.2` proposes determinism from Wigner-data $W_{i_1, i_2}^t$ (Goldstone-pair eigenvalues + mixing angle + masses); Cat A path pending W9+.

**B2 의 question**: *어떤 두 개의 mathematically independent routes 가 Conjecture 8.1 의 Cat B 승급을 produce 할 수 있는가, 그리고 그 두 route 가 같은 deterministic map 을 produce 함을 어떻게 확인하는가?*

---

## §3. Route (a) — Kato resolvent perturbation expansion

### §3.1 Mathematical setup

Pre-merger limit 에서 두 formation 의 *cross-block Hessian*:

$$H_{\mathrm{pre}}(t^{*-}) = \begin{pmatrix} H_{i_1, i_1} & H_{i_1, i_2} \\ H_{i_2, i_1} & H_{i_2, i_2} \end{pmatrix}$$

with $H_{i, i} \succ 0$ (formation $i$ 의 self-Hessian, single-formation σ_standard 의 source) 과 cross-block $H_{i_1, i_2}$ which by **Coupling Bound Lemma** (`sigma_rich_wigner_derivation.md §3.3`) satisfies:

$$\lVert H_{i_1, i_2} \rVert_{\mathrm{op}} \leq \lambda_\mathrm{rep} \cdot c \cdot e^{-c_0 \cdot d_{\mathrm{inter}}(i_1, i_2)}$$

where $d_{\mathrm{inter}} = d_\mathrm{graph}(\mathrm{core}(u^{i_1}), \mathrm{core}(u^{i_2}))$.

Define block-diagonal *unperturbed* operator $H_0 = H_{i_1, i_1} \oplus H_{i_2, i_2}$ and *coupling perturbation* $V = H - H_0$ (off-diagonal blocks).

### §3.2 Kato expansion

Reed-Simon IV §XIII.5 (resolvent expansion for *isolated simple eigenvalues* under analytic perturbation):

$$\lambda_a(\varepsilon) = \lambda_a^{(0)} + \varepsilon \langle \phi_a^{(0)}, V \phi_a^{(0)} \rangle + \varepsilon^2 \sum_{b \neq a} \frac{\vert \langle \phi_a^{(0)}, V \phi_b^{(0)} \rangle\vert ^2}{\lambda_a^{(0)} - \lambda_b^{(0)}} + O(\varepsilon^3)$$

with $\varepsilon = \lVert V \rVert_\mathrm{op} / \min_{a \neq b} \vert \lambda_a^{(0)} - \lambda_b^{(0)}\vert $.

### §3.3 Post-merger relation

**Claim (Route (a) target Cat B)**: As $t \to t^*$ (merger), $\lVert V \rVert_\mathrm{op} \uparrow O(\lambda_\mathrm{rep})$, and at $t^{*+}$ the merged $u_s^j$ Hessian $H_\mathrm{post}$ relates to $H_\mathrm{pre}$ via a *Schur-complement reduction* on the merged-mass subspace.

The expansion (§3.2) under Schur-complement boundary condition produces *explicit polynomials* in $(\lambda_{i_1,a}^{(0)}, \lambda_{i_2,b}^{(0)}, \lVert V \rVert, m_{i_1}, m_{i_2})$ that compute $\sigma_\mathrm{std}(C_j^s)$ to any order in $\varepsilon$.

### §3.4 Success conditions (Route (a))

1. **Perturbative regime**: $\lVert V \rVert < \min_a \vert \lambda_a^{(0)} - \lambda_{a+1}^{(0)}\vert $ — eigenvalue spacing exceeds coupling. Equivalently $\lambda_\mathrm{rep} \cdot e^{-c_0 d_\mathrm{inter}} < $ spectral gap of $H_0$.
2. **Simple eigenvalues**: $\lambda_a^{(0)} \neq \lambda_b^{(0)}$ for $a \neq b$ — no symmetry-forced multiplicities.
3. **Analytic family**: $V(\varepsilon)$ smooth in merger parameter $\varepsilon$ — guaranteed by gradient-flow continuity on smooth segments (`sigma_rich_wigner_derivation.md §9`).

### §3.5 Failure modes (Route (a))

- **Deep merger** ($d_\mathrm{inter} \to 0$): $\lVert V \rVert \uparrow$, perturbative gap closes. Series diverges. → Route (b) needed.
- **Goldstone degeneracy**: $H_{i_i}$ 의 lowest eigenvalues 가 graph translation-invariance 의 Goldstone modes — degenerate $\lambda^{(0)} = 0$ (translation-invariant graph case). Simple-eigenvalue 가정 위배. → 2×2 Goldstone-pair Wigner-von Neumann avoided-crossing analysis (`sigma_rich_wigner_derivation.md §3`) 필요.
- **High symmetry**: $\mathrm{Aut}(G)$ 에 의한 forced multiplicity. → Group-theoretic decomposition (Route (c)) 필요.

### §3.6 Expected Cat status (Route (a) alone)

Cat B (conditional on §3.4 conditions). Cat A 는 (a) explicit constants 의 *operator-norm bound* + (b) Schur-complement-reduction 의 *rigorous boundary condition matching* + (c) 다중 K-jump 의 *iterated 적용 condition* 으로 W9+ 작업.

---

## §4. Route (b) — RMT Wigner-Dyson level repulsion

### §4.1 Mathematical setup

For graphs with $\mathrm{Aut}(G)$ *trivial* (no non-trivial graph automorphism beyond identity — *generic* graphs), the merged-formation Hessian $H_\mathrm{post}$ 의 eigenvalue spacing 은 *Wigner-Dyson statistics* 에 *근접* 함이 RMT (random matrix theory) 의 일반 정리.

**Wigner-Dyson nearest-neighbor spacing distribution** (GOE — Gaussian Orthogonal Ensemble, real symmetric matrices):

$$P_\mathrm{GOE}(s) = \frac{\pi s}{2} \exp\!\bigl(-\frac{\pi s^2}{4}\bigr), \quad s = \frac{\Delta \lambda}{\langle \Delta \lambda \rangle}$$

with the *level repulsion* $P(s) \to (\pi/2) s$ as $s \to 0$ (no eigenvalue crossing).

### §4.2 Application to OP-0008

**Approach**: View $H_\mathrm{post}(u_s^j)$ as a *single sample* from an *ensemble* of merger-instances at fixed coarse-grained pre-merger data $(\sigma_\mathrm{std}(C_{i_1}^t), \sigma_\mathrm{std}(C_{i_2}^t); m_{i_1}, m_{i_2})$. The ensemble is generated by varying *fine-scale* data (merger trajectory perturbations within the smooth segment).

**Claim (Route (b) target Cat B)**: For generic $\mathrm{Aut}(G) = 1$, the *distributional* relation

$$\sigma_\mathrm{std}(C_j^s) \,\big\vert\, (\sigma_\mathrm{std}(C_{i_1}^t), \sigma_\mathrm{std}(C_{i_2}^t); m_{i_1}, m_{i_2}) \;\sim\; \mathrm{GOE}\text{-conditional}\bigl[\dots\bigr]$$

is *determined* — even though the *single-instance* σ_standard is not determined.

### §4.3 Success conditions (Route (b))

1. **Generic graph**: $\mathrm{Aut}(G) = 1$ — no symmetry-forced multiplicity.
2. **Deep merger regime** ($d_\mathrm{inter} \to 0$): Route (a) failure regime where RMT genericity activates.
3. **Coarse-grained inheritance**: σ_standard is treated as a *qualitative tuple* (`nq242c_explicit_construction.md §2.4` "qualitative σ-tuple" convention) — small-magnitude differences absorbed.

### §4.4 Failure modes (Route (b))

- **High-symmetry graph** (e.g., $T^2_L$ with $\mathrm{Aut} = \mathbb{Z}_L^2 \rtimes D_4$, complete graph $K_n$, etc.): forced multiplicity. Wigner-Dyson genericity 가 *Aut(G) character data* 에 의해 bypass 됨. → Route (a) (perturbation, low coupling regime) 또는 Route (c) 필요.
- **Small dimension** (n < 20 or so): RMT genericity 의 *asymptotic* nature — finite-dimension 의 *small ensemble* 에서는 distributional convergence 가 slow. NQ-242c 의 T²_20 = 400 site 정도가 borderline.
- **Strong correlation** (φ_rich 의 추가 데이터 부재 시 cross-eigenvalue 가 *correlated*): GOE iid 가정 위배. → Wigner-Dyson 보다는 *block-correlated ensemble* (Tracy-Widom variants) 필요.

### §4.5 Expected Cat status (Route (b) alone)

Cat B *distributional* (조건부 §4.3). Cat A 는 (a) ensemble averaging 의 *rigorous coarse-graining* 정의 + (b) Aut(G) trivial 의 *open dense subset* 통제 + (c) finite-dimension RMT 수렴 bound 으로 W10+ 작업.

---

## §5. 수렴 분석 framework (convergence of two routes)

### §5.1 *Distinct domains*

Route (a) 와 Route (b) 는 **수학적으로 독립** (prompt body §5 의 quality 기준):
- Route (a): *low-coupling regime* ($\lVert V \rVert <$ spectral gap), *deterministic per-instance*.
- Route (b): *high-coupling regime* ($\lVert V \rVert \to O(\lambda_\mathrm{rep})$), *distributional ensemble*.

실패 모드 가 서로 다름:
- Route (a) 실패 = deep merger.
- Route (b) 실패 = high symmetry.

성공 조건 가 서로 다름:
- Route (a) 성공: $\lambda_\mathrm{rep} e^{-c_0 d_\mathrm{inter}} <$ gap.
- Route (b) 성공: $\mathrm{Aut}(G) = 1$.

따라서 **두 route 는 같은 결과의 두 표현이 아니라 *상보적 (complementary) attack*** — prompt body §5 의 "수학적으로 독립" 기준 충족.

### §5.2 *Overlapping regime*: where both routes apply

Route (a) 성공 + Route (b) 성공 의 **교집합** = (i) 적절한 coupling regime ($\lambda_\mathrm{rep}$ moderate), (ii) generic graph ($\mathrm{Aut}(G) = 1$), (iii) merger phase 의 *avoided-crossing* phase (Case B of `sigma_rich_wigner_derivation.md §9.2`).

이 교집합에서 두 route 가 *각각 독립적으로* 같은 σ_standard map 을 produce 하면 → **Cat C → Cat B 승급의 직접 증거**.

### §5.3 *Convergence test (Day 3 exp92 의 입력)*

다음 numerical protocol 이 W8 Day 3 exp92 의 deliverable:

| Step | Action |
|---|---|
| 1 | 8×8 grid (n=64) + 12×12 grid (n=144) 두 substrate 준비 (`grid_2d`, mid-size for RMT borderline test). |
| 2 | K=2 stable formation 두 개 generate via `find_k_formations(K=2)`. |
| 3 | $d_\mathrm{inter}$ 가변: $\{2, 3, 4, 5, 6\}$ sites. Range covers Route (a) success (d ≥ 4) 와 Route (b) success (d ≤ 3) 양쪽. |
| 4 | Route (a) prediction: §3.2 Kato expansion to order $\varepsilon^2$, compute predicted $\sigma_\mathrm{std}(C_j^s)$. |
| 5 | Route (b) prediction: §4.2 RMT distributional, compute Wigner-Dyson cdf of $P_\mathrm{GOE}(s)$ for predicted spectrum. |
| 6 | Numerical merger simulation (semi-implicit gradient flow): obtain $\sigma_\mathrm{std}(C_j^s)$ ground truth. |
| 7 | 3-way 비교: Route (a) vs Route (b) vs ground truth. |
| 8 | Convergence indicator: $\lVert (\sigma_\mathrm{std}^{(a)} - \sigma_\mathrm{std}^{(b)}) \rVert / \lVert \sigma_\mathrm{std}^{(\mathrm{num})} \rVert$. Small for $d \in [3, 5]$ ⇒ overlap regime confirmed. |

### §5.4 Gate A 진입 조건 (Day 4 EOD)

W8 plan §2 G3 의 3-condition safety check 의 *수학적 형태*:

- **(SC-a)** Route (a) 의 Kato 전개가 §3.4 의 perturbative condition 하에서 *closed-form polynomial map* $\Phi^{(a)}$ 산출 — 본 broad survey §3 매핑 완료 후 Day 2 PRIMARY (`op0008_merge_wigner_perturbation.md`) 에서 explicit form 도출.
- **(SC-b)** Route (b) 의 RMT 가 §4.3 의 generic-graph condition 하에서 *distributional map* $\Phi^{(b)}$ 산출 — 본 broad survey §4 매핑 완료 후 Day 3 secondary (`op0008_merge_wigner_rmt.md`) 에서 explicit form 도출.
- **(SC-c)** §5.3 의 numerical protocol exp92 가 8×8 + 12×12 toy 에서 *convergence* (overlap regime 의 $\lVert \Phi^{(a)} - \Phi^{(b)} \rVert < \mathrm{tol}$) 를 confirm.

세 조건 모두 PASS → Gate A 활성 → L-Wigner-Projection-MERGE Cat B 승급 + canonical §13 insertion candidate.

### §5.5 Gate B fallback (수렴 실패 시)

§5.3 의 numerical convergence 가 *상보적 영역 부재* 를 노출 (e.g., 두 route 가 *완전히 disjoint* 한 regime 만 cover) → Gate B 활성:
- T-σ-Inherit (a, b, d-direction, e) 의 *기존* working Cat B 를 *partial canonical promotion* (audit-only).
- σ_standard part (c, d-σ_standard) 는 **여전히 Cat C** — 명시적 carry-forward (silent resolution 금지).
- canonical §13 에 *4 lemma 동시 insert*; 새 Cat B 1건 없음, 다만 partial entry 4건.

---

## §6. Route (c) — Topological / group-theoretic (preserved as alternative, W9+ staging only)

본 broad survey 는 *3-route framework* 의 quality 기준 (prompt body §4.2) 도 함께 보유. Route (c) 는 *Aut(G) 비-trivial high-symmetry regime* 의 대안:

### §6.1 핵심 아이디어

$H_\mathrm{post}$ 의 eigenvalues 가 $\mathrm{Aut}(\mathrm{merged})$ irrep block 으로 *forced decomposition* — character data 가 *deterministic specification* 직접 제공. Route (b) RMT 의 bypass 가 정확히 *Aut(G) character* 의 부재; 반대로 character 가 *풍부* 한 경우 Route (c) 가 가장 명확.

### §6.2 도구

- $\mathrm{Aut}(C_j^s)$ 의 *finite group* representation theory.
- Frobenius character orthogonality.
- $D_n$, $S_n$, $\mathbb{Z}_n$ character tables (canonical example: T²_L torus 의 $\mathbb{Z}_L^2 \rtimes D_4$).

### §6.3 성공 조건

- High-symmetry merged formation ($\mathrm{Aut}(C_j^s) \supsetneq 1$).
- Pre-merger formation 의 *symmetry inheritance* (Aut breaking 패턴 명시 가능).

### §6.4 W9+ staging 사유

Route (c) 는 본 W8 의 Day 2-3 작업 *밖*. 이유:
- Route (a), (b) 가 *generic* regime cover; Route (c) 는 *exceptional* regime 만 cover.
- Aut(G) character framework 의 *SCC 적용* 은 별도 working file (W9+, `working/MF/aut_g_character_op0008.md` 후보, 미작성).
- 본 W8 의 CV-1.19 SEAL gate 는 Route (a)+(b) 의 generic case 만 통과 필요; Route (c) 는 *완전 Cat A 승급* (W10+) 의 입력.

본 broad survey 에서는 **§6 한 단락 보존** 만 — Day 2-3 작업의 *우선 제외 사유* 명시.

---

## §7. 기존 canonical / working 과의 관계

### §7.1 Canonical 위치

- `canonical.md §11.1 Commitment 14-Multi`: σ_standard 정의. 본 B2 는 이 정의의 *post-merger inheritance map* 만 attack.
- `canonical.md §13 T-σ-multi-A-Static`: static Cat A (D-6a CV-1.5.1). 본 B2 는 *dynamic* (K-jump merger) 의 σ_standard 만; static 무관.
- `canonical.md §15 OP-0008`: OPEN. 본 B2 는 *attack framework* 의 mapping; 해결 주장 아님.

### §7.2 Working 위치 (확장 관계)

본 broad_survey_B2 = 다음 working file 들의 *2-route 방법론적 확장*:
- `sigma_rich_wigner_derivation.md §8.2 Conjecture 8.1` — 본 file 의 Conjecture 8.1 의 *Route (a) + Route (b) attack 분해*.
- `sigma_inherit_k_jump.md §3.3 (c)` — Cat C MERGE σ_standard 의 *상태 그대로 인정* + *attack 두 route 의 명시*.
- `sigma_rich_phi_proof.md §6.2` — Cat A target outline (analytic family / Newton-Puiseux / projection formula). 본 file 의 Route (a) 가 그 outline 의 *perturbative wing*, Route (b) 가 *probabilistic wing*.

### §7.3 Silent resolution 회피

- OP-0008 *전체* (CONT/MERGE/SPLIT/DIST 4 sub-cases) 중 본 file 은 **MERGE σ_standard 부분 만 attack**.
- CONT/SPLIT/DIST 의 silent 해결 주장 *없음*.
- Cat C → Cat B 승급 *시도* 만; *완료* 주장 *없음*.

---

## §8. New open questions raised by this survey

| ID | Question | Why this session raised it |
|---|---|---|
| NOQ-B2-1 | Schur-complement reduction 의 *boundary condition matching* 의 rigorous form 은 무엇인가? | Route (a) §3.3 의 *technical gap*. mass-rescaling factor μ(m_j, m_k) = $m_j m_k / (m_j + m_k)$ 가설 (sigma_rich_wigner_derivation.md §8.2) 의 derivation 이 Schur-complement 에서 자연스러운가? |
| NOQ-B2-2 | RMT distributional Cat B 가 *single-instance* Cat B 와 자동으로 결합 가능한가? | Route (b) §4.5 의 *distributional* nature 가 OP-0008 의 *per-instance* statement 와 *호환* 인지 — *coarse-graining* convention 이 canonical-acceptable 인지 미결. |
| NOQ-B2-3 | 8×8 그리드의 finite-dimension RMT convergence rate 은 무엇인가? | Route (b) §4.4 의 small-n failure mode — exp92 의 8×8 case 에서 RMT 가 *meaningful prediction* 인지 numerical pre-check 필요. |
| NOQ-B2-4 | Aut(G) trivial 의 *open dense subset* condition 의 *graph class* 별 측정은 무엇인가? | Route (b) §4.3 의 generic-graph 조건 — random regular graph / SBM / barbell / small-world 각각 의 Aut(G) = 1 분율 미상. exp_hmorse_local_sbm (W7-CV116 weeks?) 의 연속? |
| NOQ-B2-5 | Route (a) 가 *두 번 연속 K-jump* (예: $K=3 \to 2 \to 1$) 에서 iterated 적용 가능한가? | §3.6 의 "iterated 적용 condition" 명시 부재. multi-step temporal Persist chaining (exp93 of Day 4) 의 입력. |

---

## §9. Day 2-3 의 *직접 입력*

본 broad_survey_B2.md 의 Day 2-3 사용 매핑:

| Target file (Day 2-3) | 본 file 의 입력 |
|---|---|
| `op0008_merge_wigner_perturbation.md` (Day 2 PRIMARY) | §3 전체 (Route (a) 의 Kato expansion + 5×5 toy analytic). §3.4 success condition 의 explicit verification. §3.5 failure mode 의 numerical phase boundary. |
| `op0008_merge_wigner_rmt.md` (Day 3) | §4 전체 (Route (b) 의 Wigner-Dyson + GOE 적용). §4.3 generic-graph condition 의 SBM/barbell/small-world test. §5.3 numerical protocol (exp92) 의 입력. |
| `exp92_wigner_projection_robustness.py` (Day 3) | §5.3 의 8-step protocol. Step 7 의 3-way 비교 dataframe schema. |
| Day 4 EOD Gate decision | §5.4 SC-a/-b/-c 3-condition check. §5.5 Gate B fallback path 명시. |

---

## §10. Hard constraint verification (W8 anti-goals + prompt body §8)

- [x] **canonical 직접 수정 0** — `working/MF/` only.
- [x] **silent OP resolution 0** — OP-0008 *전체* 미해결, MERGE σ_standard 만 *attack framework*.
- [x] **Research OS 재도입 0** — 단일 topic file, no D-/S-/T- 등록부 생성.
- [x] **외부 framework reductive 환원 0** — Reed-Simon IV §XIII.5 / Wigner-Dyson 은 *contrastive* 도구; "OP-0008 은 결국 RMT 다" 형식의 reductive 주장 부재.
- [x] **primitive 전도 0** — $H$ 는 $\mathcal{E}_K(\mathbf{u})$ 의 second variation; u_t primitive 유지.
- [x] **4 에너지 항 병합 0** — $\mathcal{E}_K$ 구조 보존.
- [x] **closure idempotence 가정 0** — 본 file 은 closure operator 의 idempotence 사용 안 함; 축약 primitive 유지.
- [x] **K 이중 취급 0** — K = K_act 정수 commit (`canonical.md §11.1 Comm.16`); K_field continuous 미사용.
- [x] **Zero-temp metastability flag** — §5 의 "Gate A 진입" 은 *deterministic σ_standard map* attack; thermal metastability 부재. *명시*.
- [x] **OMC 풀 오케스트레이션 호출 0** — 본 file 은 Claude session 단독 작성.

추가 prompt body §12 예상 오류 회피:
- [x] **K=1 global min 반복 인용 부재** — K=2 → K=1 merger 의 σ_standard 만 다룸; K=1 global min 정리 (isoperimetric) 무관.
- [x] **threshold 원리적 근거 주장 부재** — §2.4 `nq242c_explicit_construction.md` 의 "qualitative σ-tuple" rounding = *configuration-specific*; θ_core 등의 universal 값 주장 부재.
- [x] **derived vs emergent 혼용 부재** — σ_standard 는 *derived* (energy Hessian 의 spectral data); 객체-수준의 *emergent* 주장 부재.
- [x] **metastability thermodynamic vs kinetic 혼동 부재** — 본 file 의 K-jump merger 는 *deterministic gradient flow* 에서의 *static topology change*; thermal Kramers rate 무관 (Package II 별도).
- [x] **자가참조성 구체화 부재** — closure operator + distinction operator 의 dual-mode 가 본 file 의 attack 에 *간접* (Hessian 은 closure 의 stabilization 의 second variation); reductive identification 부재.
- [x] **파라미터 유일성 주장 부재** — $\lambda_\mathrm{rep}$, $c_0$, $\mathrm{tol}$ 등 모두 *configuration-specific*; "이 값이 옳다" 주장 부재.

---

## §11. 자기 평가 (broad survey quality)

| 기준 | 결과 |
|---|---|
| 수학적으로 독립 route ≥ 2 (B2 PRIMARY 의 quality) | Route (a) + Route (b) + Route (c) preserved = **3** |
| 각 route 의 *성공 조건* + *실패 모드* 명시 | §3.4-3.5 (a), §4.3-4.4 (b), §6.3 (c) |
| 두 route 의 *수렴 분석 framework* | §5 (overlap + numerical protocol + Gate A/B 분기) |
| Day 2-3 의 *직접 입력* 으로 사용 가능 granularity | §9 명시 매핑 4건 |
| 기존 working file 과의 *non-duplicate* 관계 | §7.2 명시 (방법론적 확장; 재정리 부재) |
| 새 open question collection | §8 NOQ-B2-1 ~ NOQ-B2-5 = **5** |
| Hard constraint 위반 | 0 (§10) |

본 broad survey 의 *substantive* deliverable = (i) **2-route framework 의 명시적 매핑** + (ii) **수렴 condition 의 formal form (SC-a/-b/-c)** + (iii) **NQ-242c 와 exp92 의 직접 protocol 입력** + (iv) **Gate A/B 분기의 수학적 form** + (v) **5 NOQ 의 후속 attack 입력**.

---

## §12. Status

**Type**: working broad survey, P1 baseline.
**Cat status of contained statements**: 모두 *survey-level* — Conjecture / framework / open question. *Cat 분류 부착 부재* (broad survey 는 *attack 입력* 이며 *증명 산출* 아님).
**Promotion path**: Day 2-3 의 op0008_merge_wigner_{perturbation,rmt}.md → Day 4 EOD Gate decision → Day 5 CV-1.19 SEAL (Gate A) 또는 partial promotion (Gate B) 또는 archive (Gate fail).
**Pre-work xref check date**: 2026-05-18 (본 file 작성 직전, 30+ 기존 working file 의 *방법론적 확장 위치* 확인).
**Cross-references**: §7.2 명시.

---

*broad_survey_B2.md 종료. OP-0008 σ_standard MERGE Wigner-projection 의 2-route attack framework 첫 매핑 완료. Day 2 PRIMARY 입력 준비 완료.*
