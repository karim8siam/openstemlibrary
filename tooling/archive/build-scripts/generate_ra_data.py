# -*- coding: utf-8 -*-
"""
generate_ra_data.py
Assembles all 8 units into real-analysis-data.js
Ensures STRICT ZERO course codes or numbers anywhere in data.
"""

import json
import re
from build_ra_unit1 import get_unit1
from build_ra_unit2 import get_unit2
from build_ra_unit3 import get_unit3
from build_ra_unit4 import get_unit4
from build_ra_unit5 import get_unit5
from build_ra_unit6 import get_unit6
from build_ra_unit7 import get_unit7
from build_ra_unit8 import get_unit8

def assemble_ra_data():
    raw_units = [
        get_unit1(),
        get_unit2(),
        get_unit3(),
        get_unit4(),
        get_unit5(),
        get_unit6(),
        get_unit7(),
        get_unit8(),
    ]

    sim_map = {
        1: ("1.3", "sim_ra_dedekind_completeness"),
        2: ("2.4", "sim_ra_topology_heine_borel"),
        3: ("3.5", "sim_ra_sequence_cauchy"),
        4: ("4.3", "sim_ra_series_convergence"),
        5: ("5.1", "sim_ra_continuity_epsilon_delta"),
        6: ("6.3", "sim_ra_mvt_taylor"),
        7: ("7.4", "sim_ra_riemann_uniform_conv"),
        8: ("8.3", "sim_ra_multivariable_jacobian"),
    }

    processed_units = []
    for u_idx, raw_u in enumerate(raw_units, 1):
        target_sec_num, target_sim = sim_map.get(u_idx, ("", ""))

        sections = []
        for s_idx, sec in enumerate(raw_u.get("sections", []), 1):
            sec_num = sec.get("secNumber", f"{u_idx}.{s_idx}")
            sec_sims = []
            if sec_num == target_sec_num and target_sim:
                sec_sims = [target_sim]

            sections.append({
                "id": f"u{u_idx}-sec{s_idx}",
                "secNumber": sec_num,
                "title": sec.get("title", ""),
                "heading": sec.get("title", ""),
                "content": sec.get("content", ""),
                "simulations": sec_sims
            })

        problems = []
        for p_idx, prob in enumerate(raw_u.get("problems", []), 1):
            tier = prob.get("tier", "Solved Examination Problem")
            diff_class = "diff-easy" if "Foundational" in tier else ("diff-medium" if "Advanced" in tier else "diff-hard")
            stmt = prob.get("statement") or prob.get("content") or ""
            problems.append({
                "id": f"p{u_idx}-{p_idx}",
                "difficulty": diff_class,
                "difficultyLabel": tier,
                "title": prob.get("title", f"Problem {u_idx}.{p_idx}"),
                "question": stmt,
                "statement": stmt,
                "hints": prob.get("hints", []),
                "solution": prob.get("solution", "")
            })

        processed_units.append({
            "id": f"unit{u_idx}",
            "unitId": f"unit{u_idx}-ra",
            "number": u_idx,
            "unitNumber": u_idx,
            "title": f"Unit {u_idx}: {raw_u['title']}",
            "description": raw_u.get("leadSummary", ""),
            "leadSummary": raw_u.get("leadSummary", ""),
            "simulations": [target_sim] if target_sim else [],
            "sections": sections,
            "problems": problems
        })

    course_data = {
        "courseCode": "",
        "courseTitle": "Real Analysis: Foundations, Topology, Integration & Multivariable Analysis",
        "courseSubtitle": "Completeness Axioms, Euclidean Topology, Sequences & Series, Continuity, Mean Value Theorems, Riemann Integration & Multivariable Calculus",
        "credits": 6,
        "lectureHours": 90,
        "prerequisites": "Single-Variable Calculus & Linear Algebra",
        "description": "Exhaustive honors-level master digital textbook unifying single-variable and multivariable real analysis: axiomatic foundations of the real field, least upper bound property, Dedekind cuts, Archimedean property, denseness of rational and irrational numbers, Cantor's uncountability theorems, metric topology of Euclidean space, open and closed sets, derived sets, the Bolzano-Weierstrass theorem, open covers and the Heine-Borel compactness theorem, topological connectedness, rigorous epsilon-N sequence limits, monotone convergence, Cauchy completeness, infinite series convergence tests (Comparison, Limit Comparison, Cauchy Condensation, Ratio, Root, Integral, Raabe's, Gauss's, Alternating Series, Dirichlet, Abel), Riemann's rearrangement theorem, epsilon-delta functional limits, Heine's sequential characterization, topological continuity via open preimages, the Extreme Value Theorem, Bolzano's Intermediate Value Theorem, uniform continuity and the Heine-Cantor theorem, differentiability and Carathéodory's formulation, Fermat's interior extremum lemma, Darboux's intermediate value theorem for derivatives, Rolle's, Lagrange's, and Cauchy's Generalized Mean Value Theorems, rigorous proof of L'Hôpital's rules, Taylor's theorem with Lagrange, Cauchy, and integral remainders, Darboux sums and the Riemann integrability criterion, Lebesgue's measure-zero criterion, Fundamental Theorem of Calculus Parts 1 and 2, Riemann-Stieltjes integration, uniform convergence of function sequences, the Weierstrass M-test, term-by-term limit/integral/derivative interchange theorems, Euclidean n-space vector geometry, Cauchy-Schwarz inequality, directional and partial derivatives, total Fréchet derivatives, Jacobian matrices, the Multivariable Chain Rule, the Inverse Function Theorem, the Implicit Function Theorem in Rn, multiple integrals, Fubini's theorem, and multivariable change of variables with Jacobian determinants. Features 8 interactive 60 FPS Canvas simulations and 24 tiered solved examination problems with complete line-by-line mathematical proofs.",
        "units": processed_units
    }

    # Verify strictly zero course numbers
    json_str = json.dumps(course_data, ensure_ascii=False, indent=2)
    course_code_matches = re.findall(r'MTH[\s-]*\d+', json_str, re.IGNORECASE)
    if course_code_matches:
        raise ValueError(f"STRICT ERROR: Prohibited course codes detected in data: {course_code_matches}")

    out_file = "real-analysis-data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Real Analysis Master Textbook Data File\n")
        f.write("// STRICT CONSTRAINT: ZERO COURSE NUMBERS OR CODES PERMITTED\n")
        f.write("window.COURSE_DATA = ")
        f.write(json_str)
        f.write(";\n")

    print(f"Successfully generated {out_file} with {len(processed_units)} units, "
          f"{sum(len(u['sections']) for u in processed_units)} sections, and "
          f"{sum(len(u['problems']) for u in processed_units)} solved problems.")

if __name__ == "__main__":
    assemble_ra_data()
