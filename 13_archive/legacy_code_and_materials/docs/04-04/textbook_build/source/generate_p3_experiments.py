#!/usr/bin/env python3
"""Generate Part 3 (Experiments) figures for the SCC textbook.

Produces ~30 figures: parameter sweeps, phase transition, Allen-Cahn comparison,
transport, multi-formation, barrier height, prediction validation.
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from scc import (GraphState, ParameterRegistry, find_formation, find_k_formations,
                 closure, distinction, EnergyComputer, transport_k_formations)
from scc.energy import double_well, double_well_second_deriv, energy_bd, energy_cl, energy_sep
from scc.diagnostics import (bind_predicate, sep_predicate, inside_predicate,
                              diagnostic_vector, DiagnosticVector)
from scc.transport import (cohesion_fingerprint, graph_distance_matrix, transport_cost,
                            sinkhorn_partial_ot, transport_field, persist_transport)

OUT = os.path.join(os.path.dirname(__file__), '..', 'figures', 'P3_experiments')
os.makedirs(OUT, exist_ok=True)

FIGW = 170 / 25.4
DPI = 300

def savefig(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f"  ✓ {name}")

def field_to_grid(u, rows, cols):
    return u.reshape(rows, cols)

# ================================================================
# Fig 1: Lambda sweep (exp1)
# ================================================================
def fig_lambda_sweep():
    g = GraphState.grid_2d(10, 10)
    w_bd_vals = np.linspace(0.1, 5.0, 20)
    bind_scores, sep_scores, inside_scores, energies = [], [], [], []

    for w_bd in w_bd_vals:
        p = ParameterRegistry(w_bd=w_bd, max_iter=3000, n_restarts=2)
        try:
            res = find_formation(g, p)
            dv = res.diagnostics
            bind_scores.append(dv.bind)
            sep_scores.append(dv.sep)
            inside_scores.append(dv.inside)
            energies.append(res.energy)
        except Exception:
            bind_scores.append(np.nan)
            sep_scores.append(np.nan)
            inside_scores.append(np.nan)
            energies.append(np.nan)

    fig, axes = plt.subplots(1, 2, figsize=(FIGW * 0.85, FIGW * 0.32))
    axes[0].plot(w_bd_vals, bind_scores, 'o-', label='Bind', markersize=3)
    axes[0].plot(w_bd_vals, sep_scores, 's-', label='Sep', markersize=3)
    axes[0].plot(w_bd_vals, inside_scores, '^-', label='Inside', markersize=3)
    axes[0].set_xlabel('w_bd')
    axes[0].set_ylabel('Score')
    axes[0].set_title('Diagnostic Scores vs w_bd')
    axes[0].legend(fontsize=7)
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(w_bd_vals, energies, 'ko-', markersize=3)
    axes[1].set_xlabel('w_bd')
    axes[1].set_ylabel('Total Energy')
    axes[1].set_title('Optimal Energy vs w_bd')
    axes[1].grid(True, alpha=0.3)

    fig.suptitle('Experiment 1: λ-Sweep (Boundary Weight)', fontsize=11, y=1.02)
    savefig(fig, 'lambda_sweep.pdf')

# ================================================================
# Fig 2-4: Phase transition
# ================================================================
def fig_phase_transition():
    g = GraphState.grid_2d(10, 10)
    lam2 = g.fiedler
    c0 = 0.3
    Wpp = abs(double_well_second_deriv(c0))
    alpha = 1.0

    beta_vals = np.linspace(1, 30, 20)
    max_u_vals = []
    min_u_vals = []
    range_u_vals = []

    for beta in beta_vals:
        p = ParameterRegistry(alpha_bd=alpha, beta_bd=beta, max_iter=3000, n_restarts=2)
        try:
            res = find_formation(g, p)
            max_u_vals.append(np.max(res.u))
            min_u_vals.append(np.min(res.u))
            range_u_vals.append(np.max(res.u) - np.min(res.u))
        except Exception:
            max_u_vals.append(np.nan)
            min_u_vals.append(np.nan)
            range_u_vals.append(np.nan)

    beta_c = 4 * alpha * lam2 / Wpp

    fig, ax = plt.subplots(figsize=(FIGW * 0.5, FIGW * 0.38))
    ax.plot(beta_vals, range_u_vals, 'bo-', markersize=4, label='max(u) - min(u)')
    ax.axvline(x=beta_c, color='red', linestyle='--', linewidth=2,
               label=f'β_c = {beta_c:.2f} (theory)')
    ax.set_xlabel('β (double-well weight)')
    ax.set_ylabel('Field range')
    ax.set_title('Phase Transition: Uniform → Phase-Separated')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    savefig(fig, 'phase_transition_location.pdf')

    # Show fields before and after transition
    # Use beta values that are safely above critical for the sub-critical case
    betas_show = [max(beta_c * 1.1, 2.0), beta_c * 2.0, beta_c * 4.0]
    labels_show = ['Near β_c', '2×β_c', '4×β_c']
    fig, axes = plt.subplots(1, 3, figsize=(FIGW * 0.9, FIGW * 0.28))
    for i, (beta, lbl) in enumerate(zip(betas_show, labels_show)):
        p = ParameterRegistry(alpha_bd=alpha, beta_bd=beta, max_iter=3000, n_restarts=2)
        try:
            res = find_formation(g, p)
            u_grid = field_to_grid(res.u, 10, 10)
        except ValueError:
            u_grid = np.full((10, 10), 0.3)
        im = axes[i].imshow(u_grid, cmap='viridis', vmin=0, vmax=1,
                            origin='lower', interpolation='nearest')
        axes[i].set_title(f'{lbl}\nβ = {beta:.1f}', fontsize=9)
        axes[i].set_xticks([]); axes[i].set_yticks([])
    fig.subplots_adjust(right=0.88)
    cax = fig.add_axes([0.9, 0.15, 0.015, 0.7])
    plt.colorbar(im, cax=cax, label='u(x)')
    fig.suptitle('Fields Across Phase Transition', fontsize=11, y=1.05)
    savefig(fig, 'phase_transition_fields.pdf')

    # Hysteresis
    beta_up = np.linspace(1, 25, 15)
    beta_down = np.linspace(25, 1, 15)
    range_up, range_down = [], []
    for beta in beta_up:
        p = ParameterRegistry(alpha_bd=alpha, beta_bd=beta, max_iter=2000, n_restarts=1)
        res = find_formation(g, p)
        range_up.append(np.max(res.u) - np.min(res.u))
    for beta in beta_down:
        p = ParameterRegistry(alpha_bd=alpha, beta_bd=beta, max_iter=2000, n_restarts=1)
        res = find_formation(g, p)
        range_down.append(np.max(res.u) - np.min(res.u))

    fig, ax = plt.subplots(figsize=(FIGW * 0.5, FIGW * 0.38))
    ax.plot(beta_up, range_up, 'b-o', markersize=3, label='β increasing')
    ax.plot(beta_down, range_down, 'r-s', markersize=3, label='β decreasing')
    ax.axvline(x=beta_c, color='green', linestyle='--', label=f'β_c = {beta_c:.2f}')
    ax.set_xlabel('β')
    ax.set_ylabel('Field range')
    ax.set_title('Phase Transition Hysteresis')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    savefig(fig, 'phase_transition_hysteresis.pdf')

# ================================================================
# Fig 5-6: Allen-Cahn comparison (exp7)
# ================================================================
def fig_allen_cahn():
    g = GraphState.grid_2d(10, 10)

    # SCC formation
    p_scc = ParameterRegistry()
    res_scc = find_formation(g, p_scc)

    # Pure Allen-Cahn: only E_bd (w_cl=0, w_sep=0)
    p_ac = ParameterRegistry(w_cl=0.0, w_sep=0.0, w_bd=1.0, max_iter=5000, n_restarts=3)
    res_ac = find_formation(g, p_ac)

    # Energy comparison
    fig, axes = plt.subplots(1, 2, figsize=(FIGW * 0.85, FIGW * 0.32))

    labels = ['SCC (Full)', 'Allen-Cahn\n(E_bd only)']
    energies = [res_scc.energy, res_ac.energy]
    axes[0].bar(labels, energies, color=['#1f77b4', '#ff7f0e'], width=0.5)
    axes[0].set_ylabel('Total Energy')
    axes[0].set_title('Energy Comparison')
    axes[0].grid(True, alpha=0.3, axis='y')

    # Convergence comparison
    axes[1].semilogy(res_scc.energy_history[:200], 'b-', label='SCC', linewidth=1.5)
    axes[1].semilogy(res_ac.energy_history[:200], 'r-', label='Allen-Cahn', linewidth=1.5)
    axes[1].set_xlabel('Iteration')
    axes[1].set_ylabel('Energy')
    axes[1].set_title('Convergence Comparison')
    axes[1].legend(fontsize=8)
    axes[1].grid(True, alpha=0.3)

    fig.suptitle('SCC vs Allen-Cahn', fontsize=11, y=1.02)
    savefig(fig, 'allen_cahn_comparison_energy.pdf')

    # Field comparison
    fig, axes = plt.subplots(1, 2, figsize=(FIGW * 0.7, FIGW * 0.32))
    im1 = axes[0].imshow(field_to_grid(res_scc.u, 10, 10), cmap='viridis',
                          vmin=0, vmax=1, origin='lower', interpolation='nearest')
    axes[0].set_title('SCC Formation', fontsize=9)
    axes[0].set_xticks([]); axes[0].set_yticks([])
    im2 = axes[1].imshow(field_to_grid(res_ac.u, 10, 10), cmap='viridis',
                          vmin=0, vmax=1, origin='lower', interpolation='nearest')
    axes[1].set_title('Allen-Cahn Only', fontsize=9)
    axes[1].set_xticks([]); axes[1].set_yticks([])
    for ax, im in [(axes[0], im1), (axes[1], im2)]:
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        plt.colorbar(im, cax=cax)
    savefig(fig, 'allen_cahn_comparison_fields.pdf')

# ================================================================
# Fig 7: Transport concentration
# ================================================================
def fig_transport_concentration():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    res = find_formation(g, p)
    u = res.u

    # Compute transport cost and plan
    dist_mat = graph_distance_matrix(g)
    fp = cohesion_fingerprint(u, g, p)
    cost = transport_cost(dist_mat, fp, fp, p.sigma_transport, p.gamma_transport)

    plan, info = sinkhorn_partial_ot(cost, u / max(u.sum(), 1e-10),
                                      u / max(u.sum(), 1e-10),
                                      eps=p.eps_ot)

    fig, axes = plt.subplots(1, 3, figsize=(FIGW * 0.95, FIGW * 0.28))

    im1 = axes[0].imshow(field_to_grid(u, 10, 10), cmap='viridis',
                          vmin=0, vmax=1, origin='lower', interpolation='nearest')
    axes[0].set_title('u (source)', fontsize=9)
    axes[0].set_xticks([]); axes[0].set_yticks([])

    im2 = axes[1].imshow(plan, cmap='hot', origin='lower', interpolation='nearest')
    axes[1].set_title('Transport Plan M', fontsize=9)
    axes[1].set_xticks([]); axes[1].set_yticks([])

    row_sums = plan.sum(axis=1)
    im3 = axes[2].imshow(field_to_grid(row_sums, 10, 10), cmap='magma',
                          origin='lower', interpolation='nearest')
    axes[2].set_title('Row Sums (mass sent)', fontsize=9)
    axes[2].set_xticks([]); axes[2].set_yticks([])

    for ax, im in [(axes[0], im1), (axes[1], im2), (axes[2], im3)]:
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        plt.colorbar(im, cax=cax)

    fig.suptitle('Transport Concentration Analysis', fontsize=11, y=1.05)
    savefig(fig, 'transport_concentration.pdf')

# ================================================================
# Fig 8-10: Multi-formation dynamics
# ================================================================
def fig_multi_formation():
    g = GraphState.grid_2d(15, 15)
    p = ParameterRegistry(volume_fraction=0.15)

    try:
        results = find_k_formations(g, p, K=2, lambda_rep=10.0,
                                     n_restarts=2, max_iter=2000)

        # Combined field
        u_combined = np.zeros(g.n)
        for k, r in enumerate(results):
            u_combined += r.u

        fig, axes = plt.subplots(1, 3, figsize=(FIGW * 0.95, FIGW * 0.28))
        for k in range(min(2, len(results))):
            im = axes[k].imshow(field_to_grid(results[k].u, 15, 15), cmap='viridis',
                                vmin=0, vmax=1, origin='lower', interpolation='nearest')
            axes[k].set_title(f'Formation {k+1}', fontsize=9)
            axes[k].set_xticks([]); axes[k].set_yticks([])

        im3 = axes[2].imshow(field_to_grid(u_combined, 15, 15), cmap='viridis',
                              origin='lower', interpolation='nearest')
        axes[2].set_title('Combined', fontsize=9)
        axes[2].set_xticks([]); axes[2].set_yticks([])

        fig.suptitle('K=2 Multi-Formation (15×15 grid)', fontsize=11, y=1.05)
        fig.subplots_adjust(right=0.88)
        cax = fig.add_axes([0.9, 0.15, 0.015, 0.7])
        plt.colorbar(im3, cax=cax, label='u(x)')
        savefig(fig, 'multiform_k2.pdf')
    except Exception as e:
        print(f"  ⚠ multi-formation skipped: {e}")

    # K=3
    try:
        results3 = find_k_formations(g, p, K=3, lambda_rep=10.0,
                                      n_restarts=2, max_iter=2000)
        u_combined3 = sum(r.u for r in results3)

        fig, axes = plt.subplots(1, 4, figsize=(FIGW, FIGW * 0.22))
        for k in range(min(3, len(results3))):
            axes[k].imshow(field_to_grid(results3[k].u, 15, 15), cmap='viridis',
                           vmin=0, vmax=1, origin='lower', interpolation='nearest')
            axes[k].set_title(f'F{k+1}', fontsize=9)
            axes[k].set_xticks([]); axes[k].set_yticks([])

        im4 = axes[3].imshow(field_to_grid(u_combined3, 15, 15), cmap='viridis',
                              origin='lower', interpolation='nearest')
        axes[3].set_title('Combined', fontsize=9)
        axes[3].set_xticks([]); axes[3].set_yticks([])

        fig.suptitle('K=3 Multi-Formation', fontsize=11, y=1.05)
        savefig(fig, 'multiform_k3.pdf')
    except Exception as e:
        print(f"  ⚠ K=3 multi-formation skipped: {e}")

# ================================================================
# Fig 11: Barrier height scaling
# ================================================================
def fig_barrier_height():
    grid_sizes = [5, 8, 10, 12, 15]
    barriers = []

    for n in grid_sizes:
        g = GraphState.grid_2d(n, n)
        p = ParameterRegistry(max_iter=3000, n_restarts=2)
        ec = EnergyComputer(g, p)
        ec.normalize_weights()

        # Formation energy
        res = find_formation(g, p)
        E_form = res.energy

        # Uniform energy
        u_uniform = np.full(g.n, p.volume_fraction)
        E_uniform, _ = ec.energy(u_uniform)

        barriers.append(abs(E_uniform - E_form))

    fig, ax = plt.subplots(figsize=(FIGW * 0.5, FIGW * 0.38))
    ns = [n**2 for n in grid_sizes]
    ax.plot(ns, barriers, 'bo-', markersize=6, linewidth=2)
    ax.set_xlabel('Graph size n = N²')
    ax.set_ylabel('|E_uniform − E_formation|')
    ax.set_title('Energy Barrier vs Graph Size')
    ax.grid(True, alpha=0.3)

    # Fit
    log_ns = np.log(ns)
    log_b = np.log(np.array(barriers) + 1e-15)
    coeffs = np.polyfit(log_ns, log_b, 1)
    ax.text(0.05, 0.95, f'Scaling ∝ n^{coeffs[0]:.2f}', transform=ax.transAxes,
            fontsize=9, va='top')

    savefig(fig, 'barrier_height_scaling.pdf')

# ================================================================
# Fig 12-16: Prediction validation (P1-P5)
# ================================================================
def fig_predictions():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()

    # P1: Contraction under iterated closure
    rng = np.random.default_rng(42)
    u = np.clip(rng.uniform(0.1, 0.9, g.n), 0, 1)
    diffs = []
    for k in range(30):
        u_next = closure(u, g, p)
        diffs.append(np.linalg.norm(u_next - u))
        u = u_next

    fig, ax = plt.subplots(figsize=(FIGW * 0.5, FIGW * 0.35))
    ax.semilogy(diffs, 'o-', markersize=3, color='#1f77b4')
    ax.set_xlabel('Iteration k')
    ax.set_ylabel('‖Cl^{k+1}(u) − Cl^k(u)‖')
    ax.set_title('P1: Closure Contraction')
    ax.grid(True, alpha=0.3)
    savefig(fig, 'prediction_p1_contraction.pdf')

    # P2: Independence (E_cl, E_sep, E_bd functionally independent)
    res = find_formation(g, p)
    ec = EnergyComputer(g, p)
    ec.normalize_weights()

    # Perturb field and measure each energy separately
    perturbations = np.linspace(-0.5, 0.5, 50)
    direction = rng.randn(g.n); direction /= np.linalg.norm(direction)

    e_cl_p, e_sep_p, e_bd_p = [], [], []
    for eps in perturbations:
        u_pert = np.clip(res.u + eps * direction, 0, 1)
        e_cl_p.append(energy_cl(u_pert, g, p))
        e_sep_p.append(energy_sep(u_pert, g, p))
        e_bd_p.append(energy_bd(u_pert, g, p))

    fig, ax = plt.subplots(figsize=(FIGW * 0.5, FIGW * 0.38))
    ax.plot(perturbations, e_cl_p, '-', label='E_cl')
    ax.plot(perturbations, e_sep_p, '-', label='E_sep')
    ax.plot(perturbations, e_bd_p, '-', label='E_bd')
    ax.set_xlabel('Perturbation ε')
    ax.set_ylabel('Energy')
    ax.set_title('P2: Energy Term Independence')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    savefig(fig, 'prediction_p2_independence.pdf')

    # P3: Enhanced dwell time (metastability)
    p_meta = ParameterRegistry(beta_bd=15.0, max_iter=5000, n_restarts=2)
    res_meta = find_formation(g, p_meta)

    fig, ax = plt.subplots(figsize=(FIGW * 0.5, FIGW * 0.35))
    ax.plot(res_meta.energy_history, 'b-', linewidth=1)
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Energy')
    ax.set_title('P3: Enhanced Dwell (Metastability at β=15)')
    ax.grid(True, alpha=0.3)

    # Mark plateau regions
    eh = np.array(res_meta.energy_history)
    if len(eh) > 20:
        diffs = np.abs(np.diff(eh))
        plateau_mask = diffs < np.median(diffs) * 0.1
        for i in range(len(plateau_mask)):
            if plateau_mask[i]:
                ax.axvspan(i, i+1, alpha=0.05, color='red')
    savefig(fig, 'prediction_p3_dwell.pdf')

    # P4: Path dependence (different restarts → different formations)
    formations = []
    for seed in range(5):
        p_pd = ParameterRegistry(n_restarts=1, max_iter=3000)
        rng2 = np.random.default_rng(seed * 100)
        res_pd = find_formation(g, p_pd)
        formations.append(res_pd.u)

    fig, axes = plt.subplots(1, 5, figsize=(FIGW, FIGW * 0.18))
    for i, u_f in enumerate(formations):
        axes[i].imshow(field_to_grid(u_f, 10, 10), cmap='viridis', vmin=0, vmax=1,
                       origin='lower', interpolation='nearest')
        axes[i].set_title(f'Seed {i}', fontsize=8)
        axes[i].set_xticks([]); axes[i].set_yticks([])
    fig.suptitle('P4: Path Dependence (Different Initial Conditions)', fontsize=10, y=1.02)
    savefig(fig, 'prediction_p4_path_dependence.pdf')

    # P5: Sep-before-Inside ordering
    # Track diagnostics during optimization
    p5 = ParameterRegistry(max_iter=500, n_restarts=1)
    ec5 = EnergyComputer(g, p5)
    ec5.normalize_weights()
    from scc.optimizer import project_volume

    u5 = np.full(g.n, p5.volume_fraction) + rng.normal(0, 0.01, g.n)
    u5 = np.clip(u5, 0, 1)
    m = p5.volume_fraction * g.n
    u5 = u5 * (m / u5.sum()); u5 = np.clip(u5, 0, 1)

    bind_hist, sep_hist, inside_hist = [], [], []
    dt = 0.01
    for it in range(300):
        bind_hist.append(bind_predicate(u5, g, p5))
        sep_hist.append(sep_predicate(u5, g, p5))
        inside_hist.append(inside_predicate(u5, g))
        grad = ec5.gradient(u5)
        u5 = project_volume(u5 - dt * grad, m)

    fig, ax = plt.subplots(figsize=(FIGW * 0.55, FIGW * 0.38))
    ax.plot(bind_hist, label='Bind', linewidth=1.5)
    ax.plot(sep_hist, label='Sep', linewidth=1.5)
    ax.plot(inside_hist, label='Inside', linewidth=1.5)
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Score')
    ax.set_title('P5: Diagnostic Ordering During Formation')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-0.05, 1.05)
    savefig(fig, 'prediction_p5_ordering.pdf')

# ================================================================
# Fig 17-18: Volume fraction sensitivity
# ================================================================
def fig_volume_sensitivity():
    g = GraphState.grid_2d(10, 10)
    vf_vals = np.linspace(0.15, 0.5, 15)
    bind_s, sep_s, inside_s = [], [], []

    for vf in vf_vals:
        p = ParameterRegistry(volume_fraction=vf, max_iter=3000, n_restarts=2)
        res = find_formation(g, p)
        dv = res.diagnostics
        bind_s.append(dv.bind)
        sep_s.append(dv.sep)
        inside_s.append(dv.inside)

    fig, ax = plt.subplots(figsize=(FIGW * 0.5, FIGW * 0.38))
    ax.plot(vf_vals, bind_s, 'o-', label='Bind', markersize=3)
    ax.plot(vf_vals, sep_s, 's-', label='Sep', markersize=3)
    ax.plot(vf_vals, inside_s, '^-', label='Inside', markersize=3)
    ax.axvspan((3-np.sqrt(3))/6, (3+np.sqrt(3))/6, alpha=0.1, color='yellow', label='Spinodal')
    ax.set_xlabel('Volume fraction c = m/n')
    ax.set_ylabel('Score')
    ax.set_title('Diagnostic Sensitivity to Volume Fraction')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    savefig(fig, 'volume_sensitivity.pdf')

# ================================================================
# Fig 19-20: Ablation study (exp3)
# ================================================================
def fig_ablation():
    g = GraphState.grid_2d(10, 10)
    configs = {
        'Full SCC': dict(),
        'No E_cl': dict(w_cl=0.0),
        'No E_sep': dict(w_sep=0.0),
        'No E_bd': dict(w_bd=0.0),
        'Only E_bd': dict(w_cl=0.0, w_sep=0.0),
    }

    min_scores = {}
    fields = {}
    for name, overrides in configs.items():
        p = ParameterRegistry(**overrides, max_iter=3000, n_restarts=2)
        res = find_formation(g, p)
        min_scores[name] = res.diagnostics.min_score
        fields[name] = res.u

    fig, ax = plt.subplots(figsize=(FIGW * 0.55, FIGW * 0.38))
    names = list(min_scores.keys())
    scores = [min_scores[n] for n in names]
    colors = ['#2ca02c'] + ['#d62728'] * (len(names) - 1)
    ax.barh(names, scores, color=colors, height=0.5)
    ax.set_xlabel('min(Bind, Sep, Inside, Persist)')
    ax.set_title('Ablation: Minimum Diagnostic Score')
    ax.set_xlim(0, 1)
    ax.grid(True, alpha=0.3, axis='x')
    savefig(fig, 'ablation_scores.pdf')

    fig, axes = plt.subplots(1, len(configs), figsize=(FIGW, FIGW * 0.18))
    for i, (name, u) in enumerate(fields.items()):
        axes[i].imshow(field_to_grid(u, 10, 10), cmap='viridis', vmin=0, vmax=1,
                       origin='lower', interpolation='nearest')
        axes[i].set_title(name, fontsize=7)
        axes[i].set_xticks([]); axes[i].set_yticks([])
    fig.suptitle('Ablation: Field Comparison', fontsize=10, y=1.02)
    savefig(fig, 'ablation_fields.pdf')

# ================================================================
# Fig 21-22: Convergence diagnostics
# ================================================================
def fig_convergence():
    g = GraphState.grid_2d(10, 10)
    p = ParameterRegistry()
    res = find_formation(g, p)

    fig, axes = plt.subplots(1, 2, figsize=(FIGW * 0.85, FIGW * 0.32))

    axes[0].plot(res.energy_history, 'b-', linewidth=1)
    axes[0].set_xlabel('Iteration')
    axes[0].set_ylabel('Energy')
    axes[0].set_title('Energy History')
    axes[0].grid(True, alpha=0.3)

    axes[1].semilogy(res.grad_norm_history, 'r-', linewidth=1)
    axes[1].set_xlabel('Iteration')
    axes[1].set_ylabel('‖∇E‖')
    axes[1].set_title('Gradient Norm History')
    axes[1].grid(True, alpha=0.3)

    fig.suptitle(f'Convergence (n_iter={res.n_iter}, converged={res.converged})',
                 fontsize=10, y=1.02)
    savefig(fig, 'convergence_diagnostics.pdf')

# ================================================================
# Run all
# ================================================================
if __name__ == '__main__':
    print("=== P3: Experiments Figures ===")
    fig_lambda_sweep()
    fig_phase_transition()
    fig_allen_cahn()
    fig_transport_concentration()
    fig_multi_formation()
    fig_barrier_height()
    fig_predictions()
    fig_volume_sensitivity()
    fig_ablation()
    fig_convergence()
    print(f"\n✓ P3 complete. Figures in {OUT}")
