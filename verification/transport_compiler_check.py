"""Validate the short-interval Kraus/OAA and reversible first-exit construction.

Small matrix checks of the derived construction; no hardware benchmark.
"""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

def psqrt(x):
    e, v = np.linalg.eigh((x+x.conj().T)/2)
    assert e.min() > -1e-10
    return (v*np.sqrt(np.maximum(e, 0)))@v.conj().T

def taylor(a, s, degree):
    ans = np.eye(len(a), dtype=complex)
    term = ans.copy()
    for j in range(1, degree+1):
        term = term @ (s*a)/j
        ans += term
    return ans

n = 3
h = np.array([[.1, 1., .19],[1., -.23, .07],[.19,.07,.6]], complex)
gl = np.diag([1.,0.,0.])
gr = np.diag([0.,.8,0.])
g = gl+gr
a = -1j*h-g/2
tau = .45/(np.linalg.norm(h,2)+np.linalg.norm(g,2))
steps = 3
source = np.array([1.,0.,0.], complex)
rho = np.outer(source, source.conj())
physical_r = quad(lambda t: np.trace(gr@expm(a*t)@rho@expm(a.conj().T*t)).real, 0, steps*tau, epsabs=1e-13)[0]
out=[]

for nodes, degree in [(2,2),(4,5),(6,8)]:
    z, weights = leggauss(nodes)
    ts, weights = tau*(z+1)/2, tau*weights/2
    blocks=[taylor(a,tau,degree)]
    for gamma in [gl,gr]:
        for t,w in zip(ts,weights):
            blocks.append(np.sqrt(w)*psqrt(gamma)@taylor(a,t,degree))
    mstack=np.vstack(blocks)
    gram=mstack.conj().T@mstack
    gram_error=np.linalg.norm(gram-np.eye(n),2)
    v=mstack/2
    m=v.shape[0]
    # Rectangular Halmos unitary: first n input columns, first m success rows.
    u=np.block([[v,psqrt(np.eye(m)-v@v.conj().T)],
                [psqrt(np.eye(n)-v.conj().T@v),-v.conj().T]])
    pin=np.diag(np.r_[np.ones(n),np.zeros(m)])
    pg=np.diag(np.r_[np.ones(m),np.zeros(n)])
    unitary_error=np.linalg.norm(u.conj().T@u-np.eye(m+n),2)
    aa=-u@(np.eye(m+n)-2*pin)@u.conj().T@(np.eye(m+n)-2*pg)@u
    expected=mstack@(3*np.eye(n)-gram)/2
    oaa_residual=np.linalg.norm(aa[:m,:n]-expected,2)
    failure_max=np.linalg.norm(aa[m:,:n],2)**2
    assert unitary_error<1e-12 and oaa_residual<1e-12

    labels=(m+n)//n
    padded_labels=2**int(np.ceil(np.log2(labels)))
    upad=np.eye(padded_labels*n,dtype=complex)
    upad[:m+n,:m+n]=aa
    # psi[history_step, history_event, temporary_work, position]
    psi=np.zeros((steps+1,padded_labels,padded_labels,n),complex)
    psi[0,0,0,:]=source
    initial=psi.copy()

    def exchange_history(state,k):
        for b in range(1,padded_labels):
            old=state[0,0,b,:].copy()
            state[0,0,b,:]=state[k,b,0,:]
            state[k,b,0,:]=old

    for k in range(1,steps+1):
        psi[0,0,:,:]=(upad@psi[0,0,:,:].reshape(-1)).reshape(padded_labels,n)
        exchange_history(psi,k)
    right_labels=range(1+nodes,1+2*nodes)
    p_history=sum(np.linalg.norm(psi[k,b,0,:])**2 for k in range(1,steps+1) for b in right_labels)
    norm_error=abs(np.linalg.norm(psi)**2-1)
    workspace_residual=np.linalg.norm(psi[:,:,1:,:])

    qblocks=[aa[j*n:(j+1)*n,:n] for j in range(labels)]
    r=rho.copy()
    p_cp=0.
    for k in range(steps):
        p_cp+=sum(np.trace(qblocks[b]@r@qblocks[b].conj().T).real for b in right_labels)
        r=qblocks[0]@r@qblocks[0].conj().T
    for k in range(steps,0,-1):
        exchange_history(psi,k)
        psi[0,0,:,:]=(upad.conj().T@psi[0,0,:,:].reshape(-1)).reshape(padded_labels,n)
    inverse_error=np.linalg.norm(psi-initial)
    assert norm_error<1e-11 and workspace_residual<1e-12 and inverse_error<1e-11
    assert abs(p_cp-p_history)<1e-12
    out.append(dict(quadrature_nodes=nodes,taylor_degree=degree,
       gram_error=float(gram_error),unitary_error=float(unitary_error),
       oaa_formula_error=float(oaa_residual),maximum_failure_probability=float(failure_max),
       history_norm_error=float(norm_error),reused_workspace_residual=float(workspace_residual),
       history_inverse_error=float(inverse_error),history_vs_kraus_error=float(abs(p_cp-p_history)),
       physical_right_probability=float(physical_r),compiled_right_probability=float(p_history),
       physical_bias=float(abs(p_history-physical_r))))

report=dict(status='passed',purpose='Small finite-matrix construction checks, not a gate benchmark',tau=tau,steps=steps,checks=out)
assert all(c["gram_error"] < bound for c, bound in zip(out, [0.005, 1e-6, 1e-10]))
assert all(c["physical_bias"] < bound for c, bound in zip(out, [5e-4, 1e-7, 1e-10]))
assert all(out[i + 1]["physical_bias"] < out[i]["physical_bias"] for i in range(len(out)-1))
assert all(c["maximum_failure_probability"] < bound for c, bound in zip(out, [2e-5, 1e-12, 1e-20]))
destination = Path(__file__).resolve().parent / "results"
destination.mkdir(exist_ok=True)
(destination / "transport_compiler_check.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"status": report["status"], "compiler_checks": len(out), "finest_physical_bias": out[-1]["physical_bias"]}))
