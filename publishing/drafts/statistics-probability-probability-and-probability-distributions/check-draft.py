"""Independent finite enumerations for saved worked solutions; not full book QA."""
from fractions import Fraction as F
from itertools import combinations, product, permutations
from pathlib import Path
import hashlib, json, re
import math

ROOT = Path(__file__).resolve().parent
checks = []

def record(name, actual, expected):
    assert actual == expected, (name, actual, expected)
    checks.append({"check": name, "actual_exact": str(actual), "expected_exact": str(expected), "status": "pass"})

committees = list(combinations(range(12), 3))
department = lambda i: 0 if i < 5 else 1 if i < 9 else 2
record("U1Q1 total committees", len(committees), 220)
good = [s for s in committees if 0 in {department(i) for i in s} and len({department(i) for i in s}) >= 2]
all_three = [s for s in committees if len({department(i) for i in s}) == 3]
record("U1Q1 qualifying probability by enumeration", F(len(good), len(committees)), F(35, 44))
record("U1Q1 all-department probability by enumeration", F(len(all_three), len(committees)), F(3, 11))
record("U1Q1 fixed physics student inclusion", F(sum(0 in s for s in committees), len(committees)), F(1, 4))

# Solve the eight probability constraints by exact elimination, rather than
# substituting the hand-written region-subtraction formulas from the chapter.
patterns = list(product((0, 1), repeat=3))
constraints = [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
rhs = [F(1), F(45,100), F(35,100), F(25,100), F(15,100), F(10,100), F(8,100), F(4,100)]
matrix = [[F(all(p[i] for i in c)) for p in patterns] + [v] for c,v in zip(constraints, rhs)]
for col in range(8):
    pivot = next(row for row in range(col, 8) if matrix[row][col])
    matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
    scale = matrix[col][col]
    matrix[col] = [v / scale for v in matrix[col]]
    for row in range(8):
        if row != col:
            scale = matrix[row][col]
            matrix[row] = [a - scale*b for a,b in zip(matrix[row], matrix[col])]
weights = [matrix[i][-1] for i in range(8)]
assert all(w >= 0 for w in weights)
for count, target in [(0,F(24,100)),(1,F(51,100)),(2,F(21,100)),(3,F(4,100))]:
    record("U1Q2 exactly %s events" % count, sum(w for p,w in zip(patterns, weights) if sum(p)==count), target)
record("U1Q2 union", sum(w for p,w in zip(patterns, weights) if any(p)), F(76,100))
record("U1Q2 independence product", rhs[1]*rhs[2], F(1575,10000))

parity = [p for p in product((0,1), repeat=3) if sum(p) % 2 == 0]
for c in [(0,), (1,), (2,), (0,1), (0,2), (1,2), (0,1,2)]:
    record("U1Q3 intersection %s" % (c,), F(sum(all(p[i] for i in c) for p in parity), len(parity)), F(1,2) if len(c)==1 else F(1,4) if len(c)==2 else F(0))
record("U1Q3 union", F(sum(any(p) for p in parity), len(parity)), F(3,4))

if (ROOT/'unit-2.md').exists():
    # A 100,000-item integer population represents every stipulated source and
    # flag combination exactly; its counts are independent of odds algebra.
    population = [("H", True, 1600), ("H", False, 18400),
                  ("M", True, 1500), ("M", False, 48500),
                  ("L", True, 300), ("L", False, 29700)]
    flagged = sum(n for source, flag, n in population if flag)
    unflagged = sum(n for source, flag, n in population if not flag)
    record("U2Q1 overall flag probability", F(flagged, 100000), F(17,500))
    for source, expected in [("H",F(8,17)),("M",F(15,34)),("L",F(3,34))]:
        record("U2Q1 posterior source "+source, F(sum(n for s,f,n in population if s==source and f), flagged), expected)
    record("U2Q1 H given no flag", F(18400,unflagged), F(4,21))
    record("U2Q1 posterior odds from counts", F(1600,1800), F(8,9))
    record("U2Q1 complement likelihood", F(1800,80000), F(9,400))

    paths = list(permutations(range(12),3))
    marked = lambda i: i < 5
    exact_two = [p for p in paths if sum(marked(i) for i in p)==2]
    mum = [p for p in paths if tuple(marked(i) for i in p)==(True,False,True)]
    history = [p for p in paths if marked(p[0]) and not marked(p[1])]
    record("U2Q2 ordered MUM", F(len(mum),len(paths)), F(7,66))
    record("U2Q2 exactly two", F(len(exact_two),len(paths)), F(7,22))
    record("U2Q2 MUM given exactly two", F(len(mum),len(exact_two)), F(1,3))
    record("U2Q2 first marked given exactly two", F(sum(marked(p[0]) for p in exact_two),len(exact_two)), F(2,3))
    record("U2Q2 third marked given MU", F(sum(marked(p[2]) for p in history),len(history)), F(2,5))

    # Sum the full condition-specific joint tables, then derive conditionals.
    joint = {}
    for first, second in product((0,1), repeat=2):
        joint[first,second] = sum(weight * (rate if first else 1-rate) * (rate if second else 1-rate)
                                  for weight,rate in [(F(2,5),F(4,5)),(F(3,5),F(3,10))])
    record("U2Q3 table total",sum(joint.values()),F(1))
    for pattern, expected in [((1,1),F(31,100)),((1,0),F(19,100)),((0,1),F(19,100)),((0,0),F(31,100))]:
        record("U2Q3 marginal table "+str(pattern),joint[pattern],expected)
    first_pass = sum(v for (a,b),v in joint.items() if a)
    record("U2Q3 first pass",first_pass,F(1,2))
    record("U2Q3 second pass given first",joint[1,1]/first_pass,F(31,50))
    record("U2Q3 high given first pass",F(2,5)*F(4,5)/first_pass,F(16,25))
    record("U2Q3 marginal independence gap",joint[1,1]-F(1,2)**2,F(3,50))

if (ROOT/'unit-3.md').exists():
    original = {-2:F(1,10),-1:F(1,5),0:F(3,10),1:F(1,4),2:F(3,20)}
    squared = {}
    for x,mass in original.items():
        squared[x*x] = squared.get(x*x,F(0)) + mass
    for y,expected in [(0,F(3,10)),(1,F(9,20)),(4,F(1,4))]:
        record("U3Q1 transformed mass "+str(y),squared[y],expected)
    record("U3Q1 tail",sum(p for x,p in squared.items() if x>1),F(1,4))
    record("U3Q1 negative sign given square one",original[-1]/squared[1],F(4,9))
    cumulative = F(0)
    for y in sorted(squared):
        cumulative += squared[y]
        if cumulative >= F(1,2):
            record("U3Q1 generalized inverse median",y,1)
            break

    def close(name, actual, expected, tolerance=1e-10):
        assert abs(actual-expected) <= tolerance, (name,actual,expected)
        checks.append({"check":name,"actual":actual,"expected":expected,"absolute_error":abs(actual-expected),"tolerance":tolerance,"status":"pass"})

    def bisect(cdf,target,lo,hi):
        for _ in range(80):
            mid=(lo+hi)/2
            if cdf(mid)<target: lo=mid
            else: hi=mid
        return (lo+hi)/2

    # Integrate the original piecewise-linear triangular function by trapezoids.
    # Each segment's integral is exact; no published CDF formula is used here.
    def triangle_area(a,b):
        points=sorted(set([a,b]+[x for x in (0,1,2) if a<x<b]))
        height=lambda x: max(0,min(x,2-x))
        return sum((r-l)*(height(l)+height(r))/2 for l,r in zip(points,points[1:]))
    close("U3Q2 density normalization",triangle_area(0,2),1)
    close("U3Q2 interval area",triangle_area(.5,1.5),.75)
    triangle_cdf=lambda x: triangle_area(0,x) if x>0 else 0
    close("U3Q2 median from integrated density",bisect(triangle_cdf,.5,0,2),1)
    close("U3Q2 90th percentile",bisect(triangle_cdf,.9,0,2),2-math.sqrt(.2))

    # Original-space interval geometry, plus independent bisection for quantile.
    def square_cdf(y):
        if y<=0:return 0.0
        root=math.sqrt(y)
        return max(0,min(1,root)-max(-2,-root))/3
    close("U3Q3 boundary CDF at zero",square_cdf(0),0)
    close("U3Q3 CDF at one",square_cdf(1),2/3)
    close("U3Q3 CDF at four",square_cdf(4),1)
    close("U3Q3 median by original-space inversion",bisect(square_cdf,.5,0,4),9/16)
    # Substitute y=t^2 before integrating the two density branches. The
    # integrands become constants, avoiding evaluation of an infinite endpoint.
    close("U3Q3 first density branch integral",(2/3)*(1-0),2/3)
    close("U3Q3 second density branch integral",(1/3)*(2-1),1/3)
    for y in (.04,.25,.81,1.21,2.25,3.61):
        epsilon=1e-6
        derivative=(square_cdf(y+epsilon)-square_cdf(y-epsilon))/(2*epsilon)
        expected=1/(3*math.sqrt(y)) if y<1 else 1/(6*math.sqrt(y))
        close("U3Q3 density versus original-space CDF derivative at "+str(y),derivative,expected,1e-8)

if (ROOT/'unit-4.md').exists():
    def mean_var(pmf):
        mean=sum(x*p for x,p in pmf.items())
        variance=sum((x-mean)**2*p for x,p in pmf.items())
        return mean,variance
    table={(0,0):F(1,10),(0,1):F(1,5),(1,0):F(1,5),(1,1):F(1,10),(2,0):F(1,10),(2,1):F(3,10)}
    px={x:sum(p for (a,b),p in table.items() if a==x) for x in (0,1,2)}
    py={y:sum(p for (a,b),p in table.items() if b==y) for y in (0,1)}
    mx,vx=mean_var(px); my,vy=mean_var(py)
    record("U4Q1 X mean",mx,F(11,10)); record("U4Q1 Y mean",my,F(3,5))
    record("U4Q1 X variance via centered sum",vx,F(69,100))
    mxy=sum(x*y*p for (x,y),p in table.items())
    record("U4Q1 product moment",mxy,F(7,10))
    record("U4Q1 covariance via centered joint sum",sum((x-mx)*(y-my)*p for (x,y),p in table.items()),F(1,25))
    conditional={y:mean_var({x:table[x,y]/py[y] for x in px}) for y in py}
    for y,mean,variance in [(0,F(1),F(1,2)),(1,F(7,6),F(29,36))]:
        record("U4Q1 conditional mean "+str(y),conditional[y][0],mean)
        record("U4Q1 conditional variance "+str(y),conditional[y][1],variance)
    within=sum(py[y]*conditional[y][1] for y in py)
    between=sum(py[y]*(conditional[y][0]-mx)**2 for y in py)
    record("U4Q1 average conditional variance",within,F(41,60))
    record("U4Q1 between-mean variance",between,F(1,150))
    record("U4Q1 total variance",within+between,vx)

    def integrate(f,a,b,n=128):
        h=(b-a)/n
        return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))
    def triangle_expect(g):
        return integrate(lambda y:integrate(lambda x:2*g(x,y),0,y),0,1)
    # Integrate over the original triangular region with numerical Simpson
    # quadrature; published marginal formulas are not used in these checks.
    close("U4Q2 area normalization",triangle_expect(lambda x,y:1),1)
    ex=triangle_expect(lambda x,y:x); ey=triangle_expect(lambda x,y:y)
    exy=triangle_expect(lambda x,y:x*y)
    close("U4Q2 X mean",ex,1/3);close("U4Q2 Y mean",ey,2/3)
    close("U4Q2 product expectation",exy,1/4)
    close("U4Q2 covariance",exy-ex*ey,1/36)
    sum_event=integrate(lambda y:integrate(lambda x:2,0,y),0,.5)+integrate(lambda y:integrate(lambda x:2,0,1-y),.5,1)
    close("U4Q2 sum-region probability",sum_event,.5)
    curve_event=integrate(lambda y:integrate(lambda x:2,0,y*y),0,1)
    close("U4Q2 curved-region probability",curve_event,2/3)
    for y in (.25,.5,.75):
        conditional_mass=integrate(lambda x:1/y,0,y)
        conditional_mean=integrate(lambda x:x/y,0,y)
        conditional_variance=integrate(lambda x:(x-conditional_mean)**2/y,0,y)
        close("U4Q2 conditional normalization at "+str(y),conditional_mass,1)
        close("U4Q2 conditional mean at "+str(y),conditional_mean,y/2)
        close("U4Q2 conditional variance at "+str(y),conditional_variance,y*y/12)

    groups=[(F(1,4),{0:F(1,2),2:F(1,2)}),(F(3,4),{4:F(1,2),8:F(1,2)})]
    marginal={}
    pair={}
    for weight,law in groups:
        for x,prob in law.items():
            marginal[x]=marginal.get(x,F(0))+weight*prob
            for z,second_prob in law.items():
                pair[x,z]=pair.get((x,z),F(0))+weight*prob*second_prob
    mean,variance=mean_var(marginal)
    record("U4Q3 mixture mean",mean,F(19,4))
    record("U4Q3 marginal second moment",sum(x*x*p for x,p in marginal.items()),F(61,2))
    record("U4Q3 marginal centered variance",variance,F(127,16))
    within=sum(w*mean_var(law)[1] for w,law in groups)
    between=sum(w*(mean_var(law)[0]-mean)**2 for w,law in groups)
    record("U4Q3 within variance",within,F(13,4))
    record("U4Q3 between variance",between,F(75,16))
    record("U4Q3 decomposition",within+between,variance)
    record("U4Q3 shared-group covariance by full joint table",sum((x-mean)*(z-mean)*p for (x,z),p in pair.items()),F(75,16))

if (ROOT/'unit-5.md').exists():
    law={-1:F(1,4),3:F(3,4)}
    raw=[sum(F(x)**r*p for x,p in law.items()) for r in range(5)]
    for r,expected in [(1,F(2)),(2,F(7)),(3,F(20)),(4,F(61))]:
        record("U5Q1 raw moment "+str(r),raw[r],expected)
    mean=raw[1]
    central=[sum((x-mean)**r*p for x,p in law.items()) for r in range(5)]
    for r,expected in [(2,F(3)),(3,F(-6)),(4,F(21))]:
        record("U5Q1 centered moment "+str(r),central[r],expected)

    def polynomial_multiply(a,b,degree):
        out=[F(0)]*(degree+1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                if i+j<=degree:out[i+j]+=x*y
        return out
    # Compute log(1+u) as a finite formal series using exact rational
    # multiplication. This does not reuse the printed cumulant identities.
    u=[F(0)]+[raw[r]/math.factorial(r) for r in range(1,5)]
    power=[F(1)]+[F(0)]*4
    logarithm=[F(0)]*5
    for k in range(1,5):
        power=polynomial_multiply(power,u,4)
        for j in range(5):logarithm[j]+=F((-1)**(k+1),k)*power[j]
    for r,expected in [(1,F(2)),(2,F(3)),(3,F(-6)),(4,F(-6))]:
        record("U5Q1 cumulant from formal log coefficient "+str(r),logarithm[r]*math.factorial(r),expected)
    record("U5Q1 kurtosis",central[4]/central[2]**2,F(7,3))
    record("U5Q1 excess kurtosis",central[4]/central[2]**2-3,F(-2,3))
    close("U5Q1 skewness",float(central[3])/float(central[2])**1.5,-2/math.sqrt(3))
    pmf={n:F(0) for n in range(5)}
    for bits in product((0,1),repeat=4):
        probability=F(1)
        for bit in bits:probability*=F(2,5) if bit else F(3,5)
        pmf[sum(bits)]+=probability
    for n,numerator in enumerate((81,216,216,96,16)):
        record("U5Q2 count mass by binary-path enumeration "+str(n),pmf[n],F(numerator,625))
    mean,variance=mean_var(pmf)
    record("U5Q2 count mean",mean,F(8,5))
    record("U5Q2 count variance",variance,F(24,25))
    record("U5Q2 third centered moment",sum((x-mean)**3*p for x,p in pmf.items()),F(24,125))

    # Independent finite numerical check of the completed-square moment
    # integrals. These checks do not establish exponential-moment divergence;
    # that is the analytic tail argument in the unit and review.
    for r in range(1,5):
        computed=integrate(lambda z:math.exp(r*z-z*z/2)/math.sqrt(2*math.pi),r-8,r+8,n=8192)
        expected=math.exp(r*r/2)
        close("U5Q3 raw moment numerical integral r="+str(r),computed,expected,max(1e-10,expected*1e-10))
    ratio=.1*math.exp(20.5)/21
    assert ratio>1
    checks.append({"check":"U5Q3 positive-series consecutive ratio example","t":.1,"r":20,"ratio":ratio,"status":"pass","scope":"Illustration only; divergence for every positive t follows from the analytic ratio limit in the written solution."})

units = []
for file in sorted(ROOT.glob('unit-*.md')):
    text = file.read_text()
    text = re.sub(r'```[\s\S]*?```', ' ', text)
    text = re.sub(r'\$\$[\s\S]*?\$\$', ' ', text)
    text = re.sub(r'\$[^$\n]+\$', ' ', text)
    text = re.sub(r'^#{1,6}.*$', ' ', text, flags=re.M)
    text = re.sub(r'\*\*(?:Question\.|Solution, step [0-9]+:[^*]+)\*\*', ' ', text)
    words = re.findall(r"\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b", text)
    question_count=len(re.findall(r'^## Fully worked question [123]:',file.read_text(),flags=re.M))
    assert question_count==3, (file.name,question_count)
    units.append({"path":file.name, "substantive_draft_words":len(words), "worked_question_headings":question_count, "sha256":hashlib.sha256(file.read_bytes()).hexdigest()})

result = {"scope":"Independent exact arithmetic and conservative draft word measurement only. No claim of full academic, simulation, integration or live-publication review.", "checks":checks, "unit_drafts":units, "substantive_draft_words":sum(u['substantive_draft_words'] for u in units), "method":"Combinatorial enumeration, exact rational elimination, integer-population reconstruction, piecewise density integration, CDF inversion/differentiation, centered rational joint sums and original-region quadrature. Word measurement excludes equations, code, headings and repeated question/solution labels.", "status":"pass"}
(ROOT/'draft-checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({"passed_checks":len(checks),"units":units,"words":result['substantive_draft_words']},indent=2))
