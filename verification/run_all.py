"""Run deterministic construction checks and compare numerical reference files."""

import json
import math
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
SCRIPTS = ("transport_residence_check", "transport_compiler_check", "structural_checks", "local_slab_check", "frequency_check")


def compare(actual, expected, location="root"):
    if isinstance(expected, dict):
        assert isinstance(actual, dict) and actual.keys() == expected.keys(), location
        for key in expected:
            compare(actual[key], expected[key], location + "." + key)
    elif isinstance(expected, list):
        assert isinstance(actual, list) and len(actual) == len(expected), location
        for index, (left, right) in enumerate(zip(actual, expected)):
            compare(left, right, f"{location}[{index}]")
    elif isinstance(expected, float):
        assert isinstance(actual, (int, float)) and math.isfinite(actual), location
        assert math.isclose(actual, expected, rel_tol=1e-6, abs_tol=1e-10), (location, actual, expected)
    else:
        assert actual == expected, (location, actual, expected)


def main():
    for name in SCRIPTS:
        completed = subprocess.run([sys.executable, str(ROOT / (name + ".py"))], cwd=ROOT, text=True, capture_output=True)
        if completed.returncode:
            print(completed.stdout, end="")
            print(completed.stderr, end="", file=sys.stderr)
            raise SystemExit(completed.returncode)
        actual = json.loads((ROOT / "results" / (name + ".json")).read_text())
        expected = json.loads((ROOT / "expected" / (name + ".json")).read_text())
        compare(actual, expected, name)
        print(name + ": assertions and reference comparison passed")
    residence = json.loads((ROOT / "results/transport_residence_check.json").read_text())
    compiler = json.loads((ROOT / "results/transport_compiler_check.json").read_text())
    summary = {
        "status": "passed",
        "residence_examples": residence["summary"]["record_count"],
        "compiler_approximations": len(compiler["checks"]),
        "structural_examples": 2,
        "local_slab_examples": 8,
        "flux_examples": 4,
        "residual_certificate_examples": 2,
        "frequency_fixtures": 4,
        "frequency_regularization_cases": 12,
        "maximum_lyapunov_residual": residence["summary"]["max_lyapunov_residual"],
        "finest_compiler_physical_bias": compiler["checks"][-1]["physical_bias"],
    }
    (ROOT / "results/summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
