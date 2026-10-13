"""Independent SciPy/integration checks for Units 8–10; reruns unchanged Units 1–7 checks."""
from pathlib import Path
from fractions import Fraction
import json, math, subprocess
import numpy as np
from scipy import integrate, stats
ROOT=Path(__file__).resolve().parent
subprocess.run(['python',str(ROOT/'check-draft.py')],check=True,capture_output=True)
report=json.loads((ROOT/'draft-checks.json').read_text())
checks=[]
def check(name,actual,expected,tol=1e-9):
    assert math.isclose(actual,expected,rel_tol=tol,abs_tol=tol),(name,actual,expected)
    checks.append(dict(check=name,actual=float(actual),expected=float(expected),tolerance=tol,status='pass'))
# Integrate original-space densities instead of substituting hand-written moments.
check('U8Q1 square event',integrate.quad(lambda x:1/6,3,6)[0],.5)
check('U8Q1 transformed mean',integrate.quad(lambda x:x*x/6,2,8)[0],28)
check('U8Q1 transformed normalization',integrate.quad(lambda y:1/(12*math.sqrt(y)),4,64)[0],1)
for y in [4,9,25,36,64]:
    check('U8Q1 CDF '+str(y),integrate.quad(lambda x:1/6,2,math.sqrt(y))[0],(math.sqrt(y)-2)/6)
check('U8Q1 conditional interval',(stats.uniform.cdf(7,loc=2,scale=6)-stats.uniform.cdf(5,loc=2,scale=6))/stats.uniform.sf(5,loc=2,scale=6),2/3)
e=stats.expon(scale=.5)
check('U8Q2 mean minutes',e.mean()*60,30)
check('U8Q2 median minutes',e.median()*60,30*math.log(2))
check('U8Q2 completion quarter hour',e.cdf(.25),1-math.exp(-.5))
check('U8Q2 conditional survival',e.sf(1.5)/e.sf(1),math.exp(-1))
check('U8Q2 quantile minutes',e.ppf(.9)*60,30*math.log(10))
g=stats.gamma(a=3,scale=.5)
check('U8Q3 mean',g.mean(),1.5)
check('U8Q3 variance',g.var(),.75)
check('U8Q3 survival 2h',g.sf(2),13*math.exp(-4))
check('U8Q3 conditional survival',g.sf(3)/g.sf(1),5*math.exp(-4))
check('U8Q3 convolution density',integrate.quad(lambda x:stats.gamma.pdf(x,a=2,scale=.5)*e.pdf(1-x),0,1)[0],g.pdf(1))
n=stats.norm(loc=100,scale=10)
check('U9Q1 interval',integrate.quad(n.pdf,90,115)[0],.7745375447996848)
check('U9Q1 tail',n.sf(120),.022750131948179195)
check('U9Q1 ninetieth percentile',n.ppf(.9),112.815515655446)
for p,expected in [(.025,80.4003601545995),(.975,119.5996398454005)]:check('U9Q1 central endpoint '+str(p),n.ppf(p),expected)
b=stats.beta(a=2,b=3)
check('U9Q2 normalization',integrate.quad(lambda x:12*x*(1-x)**2,0,1)[0],1)
check('U9Q2 mean',integrate.quad(lambda x:12*x*x*(1-x)**2,0,1)[0],2/5)
check('U9Q2 centered variance',integrate.quad(lambda x:(x-.4)**2*12*x*(1-x)**2,0,1)[0],1/25)
check('U9Q2 tail',b.sf(.5),5/16)
check('U9Q2 interval',b.cdf(.75)-b.cdf(.25),11/16)
check('U9Q2 lower CDF',b.cdf(.25),67/256)
check('U9Q2 upper CDF',b.cdf(.75),243/256)
check('U9Q2 mode density',b.pdf(1/3),16/9)
for x in [.1,.4,.8]:check('U9Q2 polynomial CDF '+str(x),b.cdf(x),6*x*x-8*x**3+3*x**4)
coeff=np.array([2,-3]);means=np.array([10,3])
check('U9Q3 mean',coeff@means+5,16)
check('U9Q3 independent variance',coeff@np.diag([4,1])@coeff,25)
check('U9Q3 tail',stats.norm.sf(21,loc=16,scale=5),.15865525393145707)
check('U9Q3 dependent variance',coeff@np.array([[4,1],[1,1]])@coeff,13)
dependent_tail=float(stats.norm.sf(21,loc=16,scale=math.sqrt(13)))
exact=float(stats.binom.sf(2,200,.01));approx=float(stats.poisson.sf(2,2))
# Independent finite complement in long-double arithmetic.
q=np.longdouble('.99');p=np.longdouble('.01')
complement=1-(q**200+200*p*q**199+math.comb(200,2)*p*p*q**198)
check('U10Q1 exact tail',float(complement),exact)
check('U10Q1 Poisson tail',approx,1-5*math.exp(-2))
check('U10Q1 error bound',200*.01**2,.02)
assert abs(approx-exact)<=.02
check('U10Q1 binomial variance',stats.binom.var(200,.01),1.98)
check('U10Q2 estimate',1940/10000,.194)
check('U10Q2 signed error',1940/10000-.2,-.006)
check('U10Q2 theoretical SE',math.sqrt(stats.bernoulli.var(.2)/10000),.004)
estimated_se=math.sqrt(.194*.806/10000)
# Exact rational arithmetic avoids ceil errors from binary floating point.
check('U10Q2 exact planned count',float(Fraction(4,25)/Fraction(1,500)**2),40000)
check('U10Q2 conservative count',float(Fraction(1,4)/Fraction(1,500)**2),62500)
weights=[.25,.75];rates=[1,3]
mixpdf=lambda x:sum(w*stats.expon.pdf(x,scale=1/r) for w,r in zip(weights,rates))
mean=integrate.quad(lambda x:x*mixpdf(x),0,np.inf)[0]
second=integrate.quad(lambda x:x*x*mixpdf(x),0,np.inf)[0]
check('U10Q3 mean by integration',mean,.5)
check('U10Q3 variance by integration',second-mean*mean,5/12)
survival=integrate.quad(mixpdf,1,np.inf)[0]
check('U10Q3 survival',survival,.25*math.exp(-1)+.75*math.exp(-3))
posterior=.25*math.exp(-1)/survival
check('U10Q3 posterior',posterior,1/(1+3*math.exp(-2)))
remaining=integrate.quad(lambda x:(x-1)*mixpdf(x),1,np.inf)[0]/survival
check('U10Q3 mean remaining',remaining,posterior+(1-posterior)/3)
results=dict(status='pass',scope='Recomputed all saved draft checks for Units 1–7, and independent integration/SciPy/rational/matrix checks for Units 8–10. Finite checks do not constitute proof of every theoretical statement.',existing_checks=len(report['checks']),new_checks=len(checks),total_numeric_checks=len(report['checks'])+len(checks),checks=checks,worked_questions=30,
    evaluated_examples={'U9Q3_dependent_tail':dependent_tail,'U10Q1_exact_tail':exact,'U10Q1_poisson_tail':approx,'U10Q1_signed_error':approx-exact,'U10Q1_relative_absolute_error':abs(approx-exact)/exact,'U10Q2_estimated_SE':estimated_se,'U10Q3_survival':survival,'U10Q3_posterior_A':posterior,'U10Q3_mean_remaining':remaining},
    sources={f.name:__import__('hashlib').sha256(f.read_bytes()).hexdigest() for f in ROOT.glob('unit-*.md')})
(ROOT/'numeric-final-checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({k:v for k,v in results.items() if k in ['status','total_numeric_checks','evaluated_examples']}))
