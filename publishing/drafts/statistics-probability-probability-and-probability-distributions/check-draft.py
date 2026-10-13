"""Independent finite enumerations for saved worked solutions; not full book QA."""
from fractions import Fraction as F
from itertools import combinations, product, permutations
from pathlib import Path
import hashlib, json, re

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

units = []
for file in sorted(ROOT.glob('unit-*.md')):
    text = file.read_text()
    text = re.sub(r'```[\s\S]*?```', ' ', text)
    text = re.sub(r'\$\$[\s\S]*?\$\$', ' ', text)
    text = re.sub(r'\$[^$\n]+\$', ' ', text)
    text = re.sub(r'^#{1,6}.*$', ' ', text, flags=re.M)
    words = re.findall(r"\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b", text)
    units.append({"path":file.name, "substantive_draft_words":len(words), "worked_question_headings":len(re.findall(r'^## Fully worked question [123]:',file.read_text(),flags=re.M)), "sha256":hashlib.sha256(file.read_bytes()).hexdigest()})

result = {"scope":"Independent exact arithmetic and conservative draft word measurement only. No claim of full academic, simulation, integration or live-publication review.", "checks":checks, "unit_drafts":units, "substantive_draft_words":sum(u['substantive_draft_words'] for u in units), "method":"Combinatorial enumeration, exact rational elimination and parity enumeration. Word measurement excludes equations, code and headings.", "status":"pass"}
(ROOT/'draft-checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({"passed_checks":len(checks),"units":units,"words":result['substantive_draft_words']},indent=2))
