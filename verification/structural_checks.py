"""Small finite-dimensional checks of dark sectors and discrete passivity.

Singular full-space Lyapunov equations are deliberately avoided: the source
covariances are solved on the explicitly known bright subspace and embedded.
This checks the identities in the scientific account, not asymptotic costs.
"""

import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov, solve_discrete_lyapunov


def norm(matrix):
    return float(np.linalg.norm(matrix, 2))


def continuous_dark_sector():
    h_b = np.array([[0.2, 1, 0.3], [1, -0.1, 0.4], [0.3, 0.4, 0.7]], complex)
    h_d = np.array([[0.1, 0.8], [0.8, -0.4]], complex)
    h = np.zeros((5, 5), complex)
    h[:3, :3], h[3:, 3:] = h_b, h_d
    gl = np.diag([0.9, 0, 0, 0, 0])
    gr = np.diag([0, 0.7, 0, 0, 0])
    a = -1j * h - (gl + gr) / 2
    a_b = a[:3, :3]
    c_l, c_r = np.zeros((5, 5), complex), np.zeros((5, 5), complex)
    c_l[:3, :3] = solve_continuous_lyapunov(a_b, -gl[:3, :3])
    c_r[:3, :3] = solve_continuous_lyapunov(a_b, -gr[:3, :3])
    p_b = np.diag([1, 1, 1, 0, 0])
    w_l, w_r = np.trace(gl).real, np.trace(gr).real
    mean_l, mean_r = np.trace(c_l).real / w_l, np.trace(c_r).real / w_r
    capacity_error = abs(w_l * mean_l + w_r * mean_r - 3)
    sum_error = norm(c_l + c_r - p_b)
    residual = norm(a @ c_l + c_l @ a.conj().T + gl)
    source_dark_weight = norm(c_l[3:, :])
    p_total = np.trace((gl + gr) @ c_l).real / w_l
    # An initially occupied dark eigenbasis need not have a static covariance.
    c_initial = np.zeros((5, 5), complex)
    c_initial[3, 3] = 1
    k = expm(a * 1.3)
    dark_rotation = k @ c_initial @ k.conj().T
    dark_change = norm(dark_rotation - c_initial)
    dark_lead_current = abs(np.trace(gr @ dark_rotation).real)
    eigenvalues = np.linalg.eigvalsh((c_l + c_l.conj().T) / 2)
    assert sum_error < 1e-12 and capacity_error < 1e-12
    assert residual < 1e-12 and source_dark_weight < 1e-12
    assert abs(p_total - 1) < 1e-12
    assert eigenvalues.min() > -1e-12 and eigenvalues.max() < 1 + 1e-12
    assert dark_change > 0.1 and dark_lead_current < 1e-12
    return {
        "dimension": 5,
        "bright_dimension": 3,
        "full_lyapunov_residual": residual,
        "source_plus_drain_covariance_minus_bright_projector": sum_error,
        "weighted_residence_sum_error": float(capacity_error),
        "source_dark_weight": source_dark_weight,
        "absorption_normalization_error": float(abs(p_total - 1)),
        "dark_initial_covariance_change": dark_change,
        "dark_initial_lead_current": float(dark_lead_current),
        "mean_source_residence": float(mean_l),
        "bright_source_capacity_bound": float(3 / w_l),
    }


def discrete_passivity():
    h = np.array([[0.3, 1, 0.2], [1, -0.4, 0.7], [0.2, 0.7, 0.1]], complex)
    u_b = expm(-1j * h * 0.7)
    d_b = np.diag([0.6, 0.8, 1])
    a_b = d_b @ u_b
    b_l = np.diag([1 - 0.6 ** 2, 0, 0])
    b_r = np.diag([0, 1 - 0.8 ** 2, 0])
    c_l = solve_discrete_lyapunov(a_b, b_l)
    c_r = solve_discrete_lyapunov(a_b, b_r)
    w = np.trace(b_l).real
    total_effect = u_b.conj().T @ (b_l + b_r) @ u_b
    p_total = np.trace(total_effect @ c_l).real / w
    n = 9
    series, power = np.zeros((3, 3), complex), np.eye(3, dtype=complex)
    for _ in range(n):
        series += power @ (b_l + b_r) @ power.conj().T
        power = power @ a_b
    telescoping_error = norm(series - (np.eye(3) - power @ power.conj().T))
    # Add a dark one-mode unitary to verify no full-space contraction is needed.
    a_full = np.zeros((4, 4), complex)
    a_full[:3, :3], a_full[3, 3] = a_b, np.exp(0.23j)
    c_full = np.zeros((4, 4), complex)
    c_full[:3, :3] = c_l
    b_full = np.zeros((4, 4), complex)
    b_full[:3, :3] = b_l
    residual = norm(c_full - a_full @ c_full @ a_full.conj().T - b_full)
    mean_steps = np.trace(c_l).real / w
    nonnormality = norm(a_b @ a_b.conj().T - a_b.conj().T @ a_b)
    assert norm(c_l + c_r - np.eye(3)) < 1e-12
    assert telescoping_error < 1e-12 and residual < 1e-12
    assert abs(p_total - 1) < 1e-12 and mean_steps <= 3 / w + 1e-12
    assert nonnormality > 0.01 and abs(np.max(np.abs(np.linalg.eigvals(a_full))) - 1) < 1e-12
    return {
        "dimension": 4,
        "bright_dimension": 3,
        "full_spectral_radius": float(np.max(np.abs(np.linalg.eigvals(a_full)))),
        "nonnormality_commutator_norm": nonnormality,
        "finite_passivity_telescoping_error": telescoping_error,
        "full_stein_residual": residual,
        "source_plus_drain_covariance_error": norm(c_l + c_r - np.eye(3)),
        "total_absorption_error": float(abs(p_total - 1)),
        "mean_steps": float(mean_steps),
        "bright_capacity_bound": float(3 / w),
    }


def main():
    report = {"status": "passed", "continuous_dark_sector": continuous_dark_sector(), "discrete_passivity": discrete_passivity()}
    destination = Path(__file__).resolve().parent / "results"
    destination.mkdir(exist_ok=True)
    (destination / "structural_checks.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "structural_cases": 2}))


if __name__ == "__main__":
    main()
