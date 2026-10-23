"""Small nonseparable 3D Markov-current examples; no asymptotic/hardness claim."""
from pathlib import Path
import json
import numpy as np
from scipy.linalg import eigvals, expm, solve_continuous_lyapunov

def model(length, barrier, flux=0.0):
 n=length**3+barrier+1
 h=np.zeros((n,n),complex)
 gl=np.zeros((n,n)); gr=gl.copy()
 def site(x,y,z):return x*length**2+y*length+z
 def mixed(x,y,z):
  # Fully specified finite-precision arithmetic; not an i.i.d. disorder claim.
  q=(73856093*x)^(19349663*y)^(83492791*z)^713
  q=((q^(q>>13))*1274126177)&0xffffffff
  q=q^(q>>16)
  return 0.8*((q&0xffff)/65535-.5)
 for x in range(length):
  for y in range(length):
   for z in range(length):
    i=site(x,y,z);h[i,i]=mixed(x,y,z)
    for dx,dy,dz in [(1,0,0),(0,1,0),(0,0,1)]:
     xx,yy,zz=x+dx,y+dy,z+dz
     if max(xx,yy,zz)<length:
      j=site(xx,yy,zz)
      hop=np.exp(1j*flux*x) if dy else 1.0
      h[i,j]=hop;h[j,i]=np.conj(hop)
    if x==0:gl[i,i]=1
    if x==length-1:gr[i,i]=1
 base=length**3
 h[site(length//2,length//2,length//2),base]=1
 h[base,site(length//2,length//2,length//2)]=1
 for k in range(barrier):h[base+k,base+k]=5+((17*k+3)%31)/100
 h[-1,-1]=.17
 for i in range(base,n-1):h[i,i+1]=h[i+1,i]=1
 return h,gl,gr

def main():
 rows=[]
 for length,barrier in [(2,1),(3,1),(4,1),(3,2),(3,3),(3,4),(3,5),(3,6)]:
  h,gl,gr=model(length,barrier)
  a=-1j*h-(gl+gr)/2
  c=solve_continuous_lyapunov(a,-gl);c=(c+c.conj().T)/2
  r=a@c+c@a.conj().T+gl
  re=np.linalg.eigvalsh((r+r.conj().T)/2)
  cert=max(np.clip(re,0,None).sum(),np.clip(-re,0,None).sum())
  w=np.trace(gl).real
  ce=np.linalg.eigvalsh(c)
  assert ce.min()>-1e-6 and ce.max()<1+1e-6
  assert abs(np.trace((gl+gr)@c).real/w-1)<1e-10
  assert np.trace(c).real/w<=len(a)/w+1e-6
  assert cert/w<2e-12
  rows.append({'L':length,'barrier_length':barrier,'N':len(a),'W':w,'p_right':float(np.trace(gr@c).real/w),'mean':float(np.trace(c).real/w),'S':len(a)/w,'population_gap':float(-2*eigvals(a).real.max()),'residual_current_fraction_certificate':float(cert/w)})
 # Independently inspect the adjoint identity on one nonnormal instance.
 h,gl,gr=model(3,2)
 a=-1j*h-(gl+gr)/2
 c=solve_continuous_lyapunov(a,-gl)
 effect=solve_continuous_lyapunov(a.conj().T,-gr)
 ee=np.linalg.eigvalsh((effect+effect.conj().T)/2)
 assert ee.min()>-1e-8 and ee.max()<1+1e-8
 rng=np.random.default_rng(713)
 z=rng.normal(size=a.shape)+1j*rng.normal(size=a.shape)
 chat_cases=[("indefinite",c+.002*(z+z.conj().T)),
             ("finite_time",c-expm(10*a)@c@expm(10*a).conj().T)]
 certificates=[]
 for name,chat in chat_cases:
  residual=a@chat+chat@a.conj().T+gl
  error=np.trace(gr@(c-chat)).real
  dual=np.trace(effect@residual).real
  re=np.linalg.eigvalsh((residual+residual.conj().T)/2)
  upper=np.clip(re,0,None).sum(); lower=-np.clip(-re,0,None).sum()
  assert abs(error-dual)<2e-12 and lower-1e-12<=error<=upper+1e-12
  certificates.append({"case":name,"current_error":float(error),
       "dual_error":float(dual),"identity_residual":float(abs(error-dual)),
       "error_lower_bound":float(lower),"error_upper_bound":float(upper)})
 flux_rows=[]
 for barrier in (1,6):
  values=[]
  for flux in (0.0,np.pi/2):
   h,gl,gr=model(3,barrier,flux)
   a=-1j*h-(gl+gr)/2
   c=solve_continuous_lyapunov(a,-gl);c=(c+c.conj().T)/2
   residual=a@c+c@a.conj().T+gl
   re=np.linalg.eigvalsh((residual+residual.conj().T)/2)
   cert=max(np.clip(re,0,None).sum(),np.clip(-re,0,None).sum())/9
   value=float(np.trace(gr@c).real/9)
   assert cert<2e-12 and 0<value<1
   values.append(value)
   flux_rows.append({"barrier_length":barrier,"flux_over_pi":float(flux/np.pi),
       "p_right":value,"population_gap":float(-2*eigvals(a).real.max()),
       "residual_current_fraction_certificate":float(cert)})
  assert values[0]-values[1]>.1
 report={"status":"passed","meaning":"finite equation checks only; no diffusion law or computational advantage established",
         "rows":rows,"adjoint_effect_min":float(ee.min()),"adjoint_effect_max":float(ee.max()),
         "residual_certificates":certificates,"magnetotransport":flux_rows}
 destination=Path(__file__).resolve().parent/"results"
 destination.mkdir(exist_ok=True)
 (destination/"local_slab_check.json").write_text(json.dumps(report,indent=2)+"\n")
 print(json.dumps({"status":"passed","slab_examples":len(rows),"residual_certificate_examples":len(certificates),"flux_examples":len(flux_rows)}))
if __name__=='__main__':main()
