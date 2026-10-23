# Finite verification

From the repository root, install the pinned numerical dependencies and run:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The reference run used Python 3.12.14 with NumPy 2.3.5 and SciPy 1.17.0. The
runner executes each script, checks its scientific assertions and compares
the generated data with `expected/`. New data are written to `results/`,
which is excluded from version control. Floating-point reference comparisons
use relative tolerance `1e-6` and absolute tolerance `1e-10`; the scripts also
apply the result-specific bounds below.

| Script | Checked statements | Reference result |
|---|---|---|
| `transport_residence_check.py` | Source covariance lies between zero and the identity; source-weighted absorption probabilities normalize; the mean residence obeys the capacity bound; finite-time survival and remaining drain absorption obey their bounds. | 23 deterministic examples; maximum Lyapunov residual below `2e-14`; normalization error below `9e-15`. |
| `transport_compiler_check.py` | Rectangular unitary dilation and the one-step oblivious-amplification polynomial; reversible first-event history; exact clearing of temporary event work on the reachable state; inverse recovery; equality of recorded and Kraus lead probabilities. | Three increasing quadrature/Taylor orders; finest physical probability bias below `3e-12`. |
| `structural_checks.py` | Source-plus-drain covariance equals the bright projector; the weighted residence sum equals the bright dimension; rotating dark initial covariance carries zero lead current; discrete nonnormal passivity and absorption normalize with a dark unitary sector. | One continuous and one discrete example; identity residuals below `3e-15`. |

| `local_slab_check.py` | Nonseparable cubic-slab covariance, absorption normalization and residence bounds; adjoint current-residual certificates; phase-sensitive current with Peierls flux at two barrier lengths. | Eight slab examples, two adjoint-certificate cases and four flux cases; flux-current difference exceeds `0.13` while the long-barrier decay gap is below `2e-9`. |

| `frequency_check.py` | Parseval normalization; auxiliary-loss and energy-tail bias; resolvent, source-channel contraction and derivative bounds; shifted-solve output error. | Four fixtures at three regularizations, including an exactly dark sector; maximum Parseval discrepancy below `8e-14`. |

The residence examples include a three-site weak-link network, a doubled
internal graph with bounded barrier parameters, and nonsymmetric disordered
multichannel networks. The doubled graph has an independently known covariance,
so the script records the classical solver's forward error rather than using a
small Lyapunov residual alone as a correctness certificate. Extremely small
decay rates are numerical diagnostics and become sensitive to roundoff.

The local-slab script defines the exact procedural onsite terms and phase pattern in `model()`. Its residual certificate bounds the current error in exact arithmetic, independently of the slow gap; the reported floating-point residual is not an interval-arithmetic rounding certificate. The [scientific example](../science/local_slab.md) explains the resolved flux-response signal and its accuracy.

The frequency check uses deterministic small matrices and adaptive scalar integration to audit the classical sampler’s identities and pointwise inequalities. It does not run a large Monte Carlo performance experiment or empirically validate the confidence theorem; the finite-bit and full error proof is in [frequency sampling](../science/frequency_sampling.md).

The compiler check builds dense small matrices, including a Halmos dilation,
to inspect the stated block polynomial and history permutation. It does not
compile the procedural block encoding into elementary quantum gates. The
two-level history swaps are explicit unitary permutations on the full finite
register; the reported work clearing concerns the reachable circuit state.

These checks test finite instances and algebraic constructions. They do not
prove the general residence theorem, quadrature error bound, variable-time
estimation theorem or asymptotic gate and memory costs. They establish no
classical lower bound, transport scaling law, hardware crossover or practical
advantage. Those distinctions remain part of the scientific claims.
