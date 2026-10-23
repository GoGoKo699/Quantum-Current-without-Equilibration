#!/usr/bin/env python3
"""Finite audits of the classical current frequency representation.

Runs deterministic small examples, including an exactly dark sector.
The assertions check identities and bounds, not asymptotic performance.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve_continuous_lyapunov


def fixtures():
    h = np.array([[0, 1, .01], [1, 0, 0], [.01, 0, .17]], complex)
    yield "three_site_near_dark", h, [0], [1], 1.0, 3
    # Procedural two-by-three lattice with distinct onsite values.
    h = np.diag([.12, -.31, .08, .23, -.17, .37]).astype(complex)
    for a, b, phase in [(0, 1, .2), (1, 2, -.1), (3, 4, .3),
                        (4, 5, .1), (0, 3, -.2), (1, 4, .4), (2, 5, .15)]:
        h[a, b] = np.exp(1j * phase)
        h[b, a] = h[a, b].conjugate()
    yield "complex_two_by_three", h, [0, 3], [2, 5], .7, 6
    hd = np.zeros((8, 8), complex)
    hd[:6, :6] = h
    hd[6:, 6:] = [[.4, .13], [.13, -.22]]
    yield "exact_dark_two_mode_sector", hd, [0, 3], [2, 5], .7, 6
    # A nonsymmetric transmitting chain with a weak side branch.
    h = np.diag([.2, -.13, .29, .07, -.24]).astype(complex)
    for a, b, g in [(0, 1, 1), (1, 2, .9), (2, 3, 1.1), (1, 4, .003)]:
        h[a, b] = h[b, a] = g
    yield "five_site_side_pocket", h, [0], [3], 1.3, 5


def check_fixture(name, h, left, right, gamma, active_n):
    n = len(h)
    gl = np.zeros((n, n), complex)
    gr = np.zeros((n, n), complex)
    gl[left, left] = gamma
    gr[right, right] = gamma
    sqrt_gr = np.sqrt(gr)
    a = -1j * h - (gl + gr) / 2
    w = gamma * len(left)
    s = n / w
    # The active block is explicitly supplied for the exact-dark fixture.
    c0 = np.zeros((n, n), complex)
    c0[:active_n, :active_n] = solve_continuous_lyapunov(
        a[:active_n, :active_n], -gl[:active_n, :active_n])
    p = float(np.trace(gr @ c0).real / w)
    mean = float(np.trace(c0).real / w)
    assert mean <= s + 1e-9
    assert -1e-9 <= p <= 1 + 1e-9
    hnorm = float(np.linalg.norm(h, 2))
    b = hnorm + gamma
    bound = 2.5 * b / gamma
    result = {"name": name, "dimension": n, "active_dimension": active_n,
              "gamma": gamma, "W": w, "mean_time": mean,
              "capacity_bound": s, "current_fraction": p, "cases": []}
    for kappa in [gamma * .1, gamma * .01, gamma * .001]:
        ak = a - kappa * np.eye(n)
        ck = solve_continuous_lyapunov(ak, -gl)
        pk = float(np.trace(gr @ ck).real / w)
        lyap_residual = float(np.linalg.norm(ak @ ck + ck @ ak.conj().T + gl, 2))
        assert -2e-9 <= p - pk <= 2 * kappa * s + 2e-9

        def resolvent(e):
            return np.linalg.inv(e * np.eye(n) - h + 1j * (gl + gr) / 2
                                 + 1j * kappa * np.eye(n))

        def integrand(e):
            g = resolvent(e)
            return float(np.trace(gr @ g @ gl @ g.conj().T).real / (2 * np.pi * w))

        frequency_value, frequency_error = quad(
            integrand, -np.inf, np.inf, epsabs=2e-10, epsrel=2e-9, limit=600)
        parseval_error = abs(pk - frequency_value)
        assert parseval_error < 2e-7
        max_y = 0.0
        max_derivative_ratio = 0.0
        max_inverse_norm_ratio = 0.0
        max_channel_norm = 0.0
        # Sample points at the energy centre, tails, and near the spectral band.
        energies = np.unique(np.concatenate([
            np.linspace(-4 * b, 4 * b, 81),
            [-100 * b, -20 * b, -b, 0, b, 20 * b, 100 * b]]))
        for e in energies:
            g = resolvent(float(e))
            max_inverse_norm_ratio = max(max_inverse_norm_ratio,
                                         float(kappa * np.linalg.norm(g, 2)))
            block = np.sqrt(gamma) * sqrt_gr @ g[:, left]
            max_channel_norm = max(max_channel_norm, float(np.linalg.norm(block, 2)))
            for x in left:
                z = g[:, x]
                dz = -(g @ z)
                f = float(np.vdot(z, gr @ z).real)
                df = float(2 * np.vdot(z, gr @ dz).real)
                y = f * (e * e + b * b) / (2 * b)
                max_y = max(max_y, y)
                max_derivative_ratio = max(max_derivative_ratio,
                                           abs(df) / (2 * gamma / kappa ** 3))
                assert f <= 1 / gamma + 1e-9
                assert y <= bound + 1e-8
                if abs(e) > hnorm:
                    assert f <= gamma / (abs(e) - hnorm) ** 2 + 1e-9
        assert max_inverse_norm_ratio <= 1 + 1e-9
        assert max_channel_norm <= 1 + 1e-9
        assert max_derivative_ratio <= 1 + 1e-9
        # Test residual-to-forward-error and norm-to-current tolerance directly.
        eps = .1
        rcut = hnorm + 4 * gamma / (np.pi * eps)
        etol = min(1 / kappa, eps * b * kappa /
                   (32 * gamma * (rcut ** 2 + b ** 2)))
        test_e = .37 * rcut
        matrix = test_e * np.eye(n) - h + 1j * (gl + gr) / 2 + 1j * kappa * np.eye(n)
        z = np.linalg.solve(matrix, np.eye(n)[:, left[0]])
        direction = np.arange(1, n + 1).astype(complex)
        direction /= np.linalg.norm(direction)
        zpert = z + etol * direction
        ferr = float(np.linalg.norm(zpert - z))
        residual = float(np.linalg.norm(matrix @ zpert - np.eye(n)[:, left[0]]))
        assert ferr <= residual / kappa + 1e-12
        norm_error = abs(float(np.vdot(zpert, gr @ zpert).real - np.vdot(z, gr @ z).real))
        solve_y_error = norm_error * (test_e ** 2 + b ** 2) / (2 * b)
        assert norm_error <= gamma * (2 * etol / kappa + etol ** 2) + 1e-12
        assert solve_y_error <= eps / 16 + 1e-12
        # Tail integral and the finite-truncation bound.
        tail, tail_quad_error = quad(integrand, rcut, np.inf, epsabs=2e-10, limit=300)
        tail_negative, _ = quad(integrand, -np.inf, -rcut, epsabs=2e-10, limit=300)
        total_tail = tail + tail_negative
        tail_bound = gamma / (np.pi * (rcut - hnorm))
        assert total_tail <= tail_bound + 1e-9
        result["cases"].append({
            "kappa": kappa, "regularized_fraction": pk,
            "regularization_bias": p - pk, "regularization_bound": 2 * kappa * s,
            "lyapunov_residual_norm": lyap_residual,
            "frequency_integral": frequency_value, "quadrature_error_estimate": frequency_error,
            "parseval_absolute_error": parseval_error,
            "maximum_sampled_cauchy_value": max_y, "cauchy_bound": bound,
            "maximum_sampled_inverse_norm_times_kappa": max_inverse_norm_ratio,
            "maximum_sampled_channel_norm": max_channel_norm,
            "maximum_F_derivative_bound_ratio": max_derivative_ratio,
            "solve_forward_tolerance": etol,
            "perturbed_solve_Y_error": solve_y_error,
            "energy_cutoff": rcut, "energy_tail": total_tail,
            "energy_tail_bound": tail_bound,
            "energy_tail_quad_error_estimate": tail_quad_error,
        })
    return result


def main():
    results = [check_fixture(*f) for f in fixtures()]
    output = {"status": "passed", "scope": "finite identity and bound audits; no performance claim",
              "fixtures": results,
              "summary": {"fixture_count": len(results),
                          "regularization_case_count": sum(len(x["cases"]) for x in results),
                          "maximum_parseval_error": max(c["parseval_absolute_error"]
                                                        for x in results for c in x["cases"])}}
    destination = Path(__file__).resolve().parent / "results"
    destination.mkdir(exist_ok=True)
    path = destination / "frequency_check.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output["summary"], indent=2))


if __name__ == "__main__":
    main()
