"""Generate independent combinatorial/SciPy fixtures for the shipped JavaScript models."""
from pathlib import Path
from itertools import combinations
from scipy import stats
import json,math
ROOT=Path(__file__).resolve().parents[1]
fixtures=[]
def fixture(fn,args,expected,tol=1e-10):fixtures.append(dict(fn=fn,args=args,expected=expected,tolerance=tol))
for n in range(1,13):
 subsets=list(combinations(range(12),n));occupied=[0]*4;good=0
 for s in subsets:
  groups={0 if x<5 else 1 if x<9 else 2 for x in s};occupied[len(groups)]+=1;good+=0 in groups and len(groups)>=2
 fixture('finite',[n],dict(total=len(subsets),qualifying=good,probability=good/len(subsets),occupied=occupied))
for n in range(13):fixture('sampling',[n],dict(hyper=[float(stats.hypergeom.pmf(k,12,6,n)) for k in range(n+1)],binomial=[float(stats.binom.pmf(k,n,.5)) for k in range(n+1)],mean=n/2,hyperVariance=float(stats.hypergeom.var(12,6,n)),binomialVariance=float(stats.binom.var(n,.5))))
for p in [.05,.2,.4,.8,1]:
 for r in [1,3,5]:fixture('waiting',[p,r],dict(mean=r/p,variance=r*(1-p)/p**2,tail=float(stats.nbinom.sf(40-r,r,p)),values=[float(stats.nbinom.pmf(t-r,r,p)) if t>=r else 0 for t in range(41)]))
for k in range(1,7):
 for rate in [.1,1,2,5]:
  for elapsed,extra in [(0,0),(0,2),(1,2),(10,10)]:
   law=stats.gamma(a=k,scale=1/rate);a=float(law.sf(elapsed));b=float(law.sf(elapsed+extra));fixture('survival',[k,rate,elapsed,extra],dict(start=a,end=b,conditional=b/a,fresh=float(law.sf(extra)),mean=k/rate,variance=k/rate**2))
for z in [-10,-7,-5,-3,-2,-1.5,-1,-.5,-.1,0,.1,.5,1,1.5,2,3,5,7,10]:fixture('normalCDF',[z],float(stats.norm.cdf(z)),1e-7)
for mu,sd,lo,hi in [(0,1,-1,1.5),(2,.5,1,3),(-3,2,-10,0),(0,1,7,10),(0,.1,0,0),(0,5,-15,15)]:fixture('normal',[mu,sd,lo,hi],dict(probability=float(stats.norm.cdf(hi,loc=mu,scale=sd)-stats.norm.cdf(lo,loc=mu,scale=sd)),zlo=(lo-mu)/sd,zhi=(hi-mu)/sd),2e-7)
for a in range(1,7):
 for b in range(1,7):
  for lo,hi in [(0,1),(.25,.75),(.5,1),(0,0)]:fixture('beta',[a,b,lo,hi],dict(probability=float(stats.beta.cdf(hi,a,b)-stats.beta.cdf(lo,a,b)),mean=float(stats.beta.mean(a,b)),variance=float(stats.beta.var(a,b))))
for kind in ['triangle','mixed']:
 for lo,hi in [(-1,3),(-1,0),(0,0),(0,2),(.5,1.5),(2,3)]:
  cdf=(lambda x:0 if x<=0 else x*x/2 if x<=1 else 1-(2-x)**2/2 if x<2 else 1) if kind=='triangle' else (lambda x:0 if x<0 else .25+.375*x if x<2 else 1)
  fixture('density',[kind,lo,hi],dict(probability=cdf(hi)-cdf(lo),atom=.25 if kind=='mixed' else 0))
for weights,row in [([.1,.2,.15,.05,.2,.3],0),([.1,.2,.15,.05,.2,.3],1),([0,0,0,1,1,1],0),([1,0,0,0,0,0],0)]:
 total=sum(weights);p=[x/total for x in weights];mx=[sum(p[:3]),sum(p[3:])];my=[p[y]+p[y+3] for y in range(3)];ex=mx[1];ey=my[1]+2*my[2];fixture('joint',[weights,row],dict(p=p,mx=mx,my=my,ex=ex,ey=ey,cov=p[4]+2*p[5]-ex*ey,conditional=[x/mx[row] for x in p[row*3:row*3+3]] if mx[row]>0 else None))
p=ROOT/'publishing/drafts/statistics-probability-probability-and-probability-distributions/simulation-fixtures.json';p.write_text(json.dumps(fixtures,separators=(',',':'))+'\n');print(json.dumps(dict(fixtures=len(fixtures))))
