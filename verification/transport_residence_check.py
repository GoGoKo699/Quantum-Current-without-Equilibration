"""Deterministic checks of source-weighted residence and absorption identities.

This is a validation script, not a performance benchmark. Dense Lyapunov solves
are paid classical work here. Ill-conditioned symmetric examples also have an
independently supplied exact covariance, so a small solver residual is not
mistaken for a small forward error.
"""

import json
from pathlib import Path

import numpy as np
from scipy.linalg import eigvals, expm, solve_continuous_lyapunov


ROOT = Path(__file__).resolve().parent


def assess(name, h, gl, gr, exact_covariance=None, times=(10.0, 100.0)):
    n = len(h)
    gamma = gl + gr
    w = float(np.trace(gl).real)
    a = -1j * h - gamma / 2
    ev = eigvals(a)
    gap = float(-2 * np.max(ev.real))
    numerical = solve_continuous_lyapunov(a, -gl)
    numerical = (numerical + numerical.conj().T) / 2
    c = numerical if exact_covariance is None else exact_covariance
    residual = np.linalg.norm(a @ c + c @ a.conj().T + gl, ord=2)
    spectrum_c = np.linalg.eigvalsh(c)
    p_left = float(np.trace(gl @ c).real / w)
    p_right = float(np.trace(gr @ c).real / w)
    mean = float(np.trace(c).real / w)
    rho = gl / w
    samples = []
    for t in times:
        k = expm(a * t)
        survive = float(np.trace(k @ rho @ k.conj().T).real)
        right_remaining = float(np.trace(gr @ k @ c @ k.conj().T).real / w)
        samples.append({
            "time": t,
            "survival": survive,
            "markov_bound_from_mean": min(1.0, mean / t),
            "right_absorption_remaining": right_remaining,
        })
    return {
        "name": name,
        "dimension": n,
        "source_weight": w,
        "hamiltonian_norm": float(np.linalg.norm(h, ord=2)),
        "population_decay_gap": gap,
        "mean_residence": mean,
        "capacity_bound_N_over_W": n / w,
        "fraction_of_capacity_bound": mean * w / n,
        "p_left": p_left,
        "p_right": p_right,
        "total_absorption_error": abs(p_left + p_right - 1),
        "covariance_eigenvalue_min": float(spectrum_c[0]),
        "covariance_eigenvalue_max": float(spectrum_c[-1]),
        "lyapunov_residual_2norm": float(residual),
        "exact_covariance_available": exact_covariance is not None,
        "numerical_covariance_forward_error_2norm": (
            None if exact_covariance is None
            else float(np.linalg.norm(numerical - exact_covariance, ord=2))
        ),
        "finite_time_checks": samples,
    }


def three_site(g):
    h = np.array([[0, 1, g], [1, 0, 0], [g, 0, 0]], dtype=complex)
    return h, np.diag([1.0, 0, 0]), np.diag([0.0, 1, 0])


def doubled_internal(internal, j=1.0, gamma=1.0):
    m = len(internal)
    p0 = np.zeros((m, m))
    p0[0, 0] = 1
    x = np.array([[0.0, 1], [1, 0]])
    h = np.kron(internal, np.eye(2)) + j * np.kron(p0, x)
    gl = gamma * np.kron(p0, np.diag([1.0, 0]))
    gr = gamma * np.kron(p0, np.diag([0.0, 1]))
    a2 = -1j * j * x - gamma * np.eye(2) / 2
    c2 = solve_continuous_lyapunov(a2, -gamma * np.diag([1.0, 0]))
    c = np.kron(np.eye(m), c2)
    return h, gl, gr, c


def barrier_internal(length, height=5.0):
    diag = np.array([0.0] + [height] * length + [0.0])
    return np.diag(diag) + np.diag(np.ones(len(diag)-1), 1) + np.diag(np.ones(len(diag)-1), -1)


def disordered_network(g):
    # Three conducting channels, four longitudinal sites, two side clusters.
    rng = np.random.default_rng(19381)
    width, length, side_length = 3, 4, 4
    backbone_n = width * length
    n = backbone_n + 2 * side_length
    h = np.diag(rng.uniform(-0.4, 0.4, n)).astype(complex)
    site = lambda col, row: col * width + row
    for col in range(length):
        for row in range(width):
            u = site(col, row)
            if col + 1 < length:
                v = site(col + 1, row)
                h[u, v] = h[v, u] = 1.0
            if row + 1 < width:
                v = site(col, row + 1)
                h[u, v] = h[v, u] = 0.7
    for branch, attach in enumerate([site(1, 0), site(2, 2)]):
        start = backbone_n + branch * side_length
        h[attach, start] = h[start, attach] = g
        for k in range(side_length - 1):
            hop = 0.6 + 0.2 * rng.random()
            h[start + k, start + k + 1] = h[start + k + 1, start + k] = hop
    gl = np.zeros((n, n))
    gr = np.zeros((n, n))
    for row in range(width):
        gl[site(0, row), site(0, row)] = 1
        gr[site(length - 1, row), site(length - 1, row)] = 1
    return h, gl, gr


def nonsymmetric_barrier_network(barrier_length):
    # Remove the two side clusters, then attach a bounded-strength barrier.
    # The conducting backbone retains its independently disordered onsite terms.
    backbone, source, drain = disordered_network(1.0)
    base_n = 12
    n = base_n + barrier_length + 1
    h = np.zeros((n, n), dtype=complex)
    gl = np.zeros((n, n))
    gr = np.zeros((n, n))
    h[:base_n, :base_n] = backbone[:base_n, :base_n]
    gl[:base_n, :base_n] = source[:base_n, :base_n]
    gr[:base_n, :base_n] = drain[:base_n, :base_n]
    for k in range(barrier_length):
        h[base_n + k, base_n + k] = 5 + 0.13 * np.sin(k + 1)
    h[-1, -1] = 0.17
    h[4, base_n] = h[base_n, 4] = 1
    for k in range(base_n, n - 1):
        h[k, k + 1] = h[k + 1, k] = 1
    return h, gl, gr


def main():
    records = []
    for g in [1.0, 0.1, 0.01, 0.001, 0.0001]:
        record = assess(f"three_site_g={g:g}", *three_site(g))
        record["analytic_p_right"] = 2 / (5 + 2 * g*g)
        record["analytic_mean_residence"] = (6 + 4 * g*g) / (5 + 2 * g*g)
        records.append(record)

    for barrier_length in [1, 2, 3, 4, 5, 6, 7]:
        h, gl, gr, c = doubled_internal(barrier_internal(barrier_length))
        records.append(assess(
            f"symmetric_barrier_length={barrier_length}", h, gl, gr,
            exact_covariance=c,
        ))

    for g in [1.0, 0.1, 0.01, 0.001]:
        records.append(assess(f"disordered_three_channel_g={g:g}", *disordered_network(g)))

    for barrier_length in [1, 2, 3, 4, 5, 6, 7]:
        records.append(assess(
            f"nonsymmetric_barrier_length={barrier_length}",
            *nonsymmetric_barrier_network(barrier_length),
        ))

    summary = {
        "record_count": len(records),
        "max_lyapunov_residual": max(r["lyapunov_residual_2norm"] for r in records),
        "max_absorption_normalization_error": max(r["total_absorption_error"] for r in records),
        "all_covariances_in_0_I_to_tolerance": all(
            r["covariance_eigenvalue_min"] >= -1e-6 and r["covariance_eigenvalue_max"] <= 1 + 1e-6
            for r in records
        ),
        "all_capacity_bounds_hold": all(r["mean_residence"] <= r["capacity_bound_N_over_W"] + 1e-6 for r in records),
    }
    out = {"summary": summary, "records": records}
    assert summary["max_lyapunov_residual"] < 1e-10
    assert summary["max_absorption_normalization_error"] < 1e-8
    assert summary["all_covariances_in_0_I_to_tolerance"]
    assert summary["all_capacity_bounds_hold"]
    for r in records:
        assert r["population_decay_gap"] > 0
        assert 0 <= r["p_right"] <= 1
        for point in r["finite_time_checks"]:
            assert -1e-9 <= point["survival"] <= point["markov_bound_from_mean"] + 1e-8
            assert -1e-9 <= point["right_absorption_remaining"] <= point["survival"] + 1e-8
        if "analytic_p_right" in r:
            assert abs(r["p_right"] - r["analytic_p_right"]) < 1e-7
            assert abs(r["mean_residence"] - r["analytic_mean_residence"]) < 1e-6
    destination = ROOT / "results"
    destination.mkdir(exist_ok=True)
    (destination / "transport_residence_check.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(summary, indent=2))



if __name__ == "__main__":
    main()
