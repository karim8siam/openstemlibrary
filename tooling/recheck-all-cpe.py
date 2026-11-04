import os
import json
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CPE_DIR = os.path.join(ROOT, 'src', 'subjects', 'chemical-process-engineering')

books = [
    'chemical-engineering-fundamentals',
    'material-and-energy-balances',
    'chemical-engineering-thermodynamics',
    'transport-phenomena',
    'fluid-flow-in-processes',
    'heat-transfer-in-processes',
    'mass-transfer',
    'separation-processes-i',
    'separation-processes-ii',
    'chemical-reaction-engineering-i',
    'chemical-reaction-engineering-ii',
    'process-dynamics-and-control',
    'process-simulation',
    'process-design',
    'process-safety',
    'biochemical-engineering',
    'polymer-process-engineering',
    'petroleum-and-petrochemical-processes'
]

print(f"Auditing all {len(books)} Chemical & Process Engineering textbooks...")
results = []
all_ok = True

for b in books:
    bdir = os.path.join(CPE_DIR, b)
    data_file = os.path.join(bdir, f"{b}-data.js")
    sims_file = os.path.join(bdir, f"{b}-sims.js")
    html_file = os.path.join(bdir, f"{b}.html")

    assert os.path.exists(data_file), f"Missing data file: {data_file}"
    assert os.path.exists(sims_file), f"Missing sims file: {sims_file}"
    assert os.path.exists(html_file), f"Missing html file: {html_file}"

    with open(data_file, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = "window.COURSE_DATA = "
    start_idx = content.find(prefix)
    assert start_idx != -1, f"Could not find window.COURSE_DATA in {data_file}"
    json_str = content[start_idx + len(prefix):].rstrip().rstrip(';')
    data = json.loads(json_str)

    units = data.get('units', [])
    num_units = len(units)

    total_words = 0
    total_problems = 0
    total_worked_problems = 0

    for u in units:
        for sec in u.get('sections', []):
            sec_content = sec.get('content', '')
            words = len(re.findall(r'[a-zA-Z]{2,}', sec_content))
            total_words += words
        probs = u.get('problems', [])
        w_probs = u.get('workedProblems', [])
        total_problems += len(probs)
        total_worked_problems += len(w_probs)

    # Check sims
    with open(sims_file, 'r', encoding='utf-8') as f:
        sim_code = f.read()
    sim_models = len(re.findall(r'idx:\s*\d+', sim_code))

    # Check html canonical
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    canonical_match = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', html)
    if not canonical_match:
        canonical_match = re.search(r'<link[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']', html)
    canonical = canonical_match.group(1) if canonical_match else 'MISSING'
    canonical_valid = (not canonical.endswith('.html')) and canonical.startswith('https://openstemlibrary.com/')

    passed = (total_words >= 25000 and num_units == 8 and total_problems >= 40 and total_worked_problems >= 40 and sim_models == 8 and canonical_valid)
    if not passed:
        all_ok = False

    results.append({
        'slug': b,
        'units': num_units,
        'words': total_words,
        'problems': total_problems,
        'workedProblems': total_worked_problems,
        'sims': sim_models,
        'canonical': canonical,
        'passed': passed
    })

print(f"{'SLUG':<42} | {'WORDS':<7} | {'UNITS':<5} | {'PROBS':<5} | {'W_PROB':<6} | {'SIMS':<4} | {'CANONICAL':<45} | STATUS")
print("-" * 130)
for r in results:
    status = "PASS" if r['passed'] else "FAIL"
    print(f"{r['slug']:<42} | {r['words']:<7} | {r['units']:<5} | {r['problems']:<5} | {r['workedProblems']:<6} | {r['sims']:<4} | {r['canonical']:<45} | {status}")

print("-" * 130)
total_dept_words = sum(r['words'] for r in results)
total_dept_problems = sum(r['problems'] for r in results)
total_dept_sims = sum(r['sims'] for r in results)
print(f"TOTAL DEPARTMENT WORDS: {total_dept_words:,}")
print(f"TOTAL SOLVED PROBLEMS:  {total_dept_problems}")
print(f"TOTAL SIMULATIONS:      {total_dept_sims}")
print(f"\nOVERALL CPE AUDIT STATUS: {'ALL 18 BOOKS PASSED STRICT VERIFICATION!' if all_ok else 'SOME FAILED'}")

if not all_ok:
    exit(1)
