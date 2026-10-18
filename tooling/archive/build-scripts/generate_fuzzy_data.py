# -*- coding: utf-8 -*-
"""
generate_fuzzy_data.py
Assembles all 8 units into fuzzy-mathematics-data.js
Ensures STRICT ZERO course codes or numbers anywhere in data.
"""

import json
import re
from build_fuzzy_unit1 import get_unit1
from build_fuzzy_unit2 import get_unit2
from build_fuzzy_unit3 import get_unit3
from build_fuzzy_unit4 import get_unit4
from build_fuzzy_unit5 import get_unit5
from build_fuzzy_unit6 import get_unit6
from build_fuzzy_unit7 import get_unit7
from build_fuzzy_unit8 import get_unit8

def assemble_fuzzy_data():
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
        1: ("1.5", "sim_fuzzy_membership_designer"),
        2: ("2.5", "sim_fuzzy_set_operations"),
        3: ("3.5", "sim_fuzzy_alpha_cuts_decomposition"),
        4: ("4.5", "sim_fuzzy_number_arithmetic"),
        5: ("5.5", "sim_fuzzy_equations_solver"),
        6: ("6.5", "sim_fuzzy_relations_matrix"),
        7: ("7.5", "sim_fuzzy_relational_equations"),
        8: ("8.5", "sim_fuzzy_control_pendulum"),
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
                "id": f"sec{u_idx}-{s_idx}",
                "secNumber": sec_num,
                "title": sec["title"],
                "content": sec["content"],
                "simulations": sec_sims
            })

        problems = []
        for p_idx, prob in enumerate(raw_u.get("problems", []), 1):
            tier = prob.get("tier", "Solved Examination Problem")
            diff_class = "diff-easy" if "Foundational" in tier or "Fundamentals" in tier else ("diff-medium" if "Advanced" in tier or "Computational" in tier else "diff-hard")
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
            "unitId": f"unit{u_idx}-fuzzy",
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
        "courseTitle": "Fuzzy Mathematics: Fuzzy Sets, Fuzzy Logic, Fuzzy Arithmetic & Relational Systems",
        "courseSubtitle": "Crisp vs Fuzzy Sets, Membership Functions & Logic, Set Operations & t-Norms, α-Cuts & Extension Principle, Fuzzy Numbers & Linguistic Variables, Fuzzy Arithmetic & Equations, Fuzzy Relations & Transitive Closures, and Industrial Applications to Control, Decision Making & AI",
        "credits": 3,
        "lectureHours": 45,
        "prerequisites": "Abstract Set Theory, Real Analysis & Linear Algebra",
        "description": "Exhaustive honors-level master digital textbook on fuzzy set theory, fuzzy logic, fuzzy arithmetic, and relational systems: crisp sets and characteristic functions, classical logic vs infinite-valued fuzzy logic, membership functions (triangular, trapezoidal, Gaussian, generalized bell, sigmoidal), core, support, height, and boundary, normal and subnormal fuzzy sets, convex fuzzy sets and quasiconcavity, standard Zadeh operators and De Morgan laws, axiomatic fuzzy complements, Sugeno and Yager complement families, equilibrium points, triangular norms (t-norms: min, product, bounded difference, drastic) and triangular conorms (s-norms: max, algebraic sum, bounded sum, drastic sum), dual De Morgan pairs, averaging operators and Ordered Weighted Averaging (OWA), crisp α-cuts and strong α-cuts, cut monotonicity and representation theorems, Zadeh's Extension Principle and Nguyen's cut preservation theorem, axiomatic definition of fuzzy numbers and closed intervals, interval arithmetic and non-invertibility of interval subtraction, Triangular Fuzzy Numbers (TFN) and Trapezoidal Fuzzy Numbers (TrFN), linguistic variables and hedges (concentration, dilation, intensification), defuzzification methods (Centroid COG, Bisector BOA, Mean of Maxima MOM, First/Last of Maxima FOM/LOM) and Yager's ranking index, addition and subtraction of fuzzy numbers, quadratic shape distortion in multiplication of TFNs, MIN and MAX lattice operations, linear fuzzy equations A + X = B and solvability spread conditions, multiplicative fuzzy equations A · X = B, fuzzy binary relations on Cartesian products, membership matrices, domain, range, height, and inverse relations, Max-Min and Max-Product relational compositions, fuzzy equivalence and similarity relations, transitive closures and powers, compatibility (tolerance) relations and α-equivalence partitions, fuzzy partial orderings and quasi-orderings, relational morphisms (homomorphisms, isomorphisms), fuzzy relational equations P ∘ R = Q, Sanchez's Theorem for greatest relational solutions via Gödel residuated implication, minimal solutions, Mamdani and Takagi-Sugeno-Kang (TSK) fuzzy inference systems, inverted pendulum dynamic balancing, fuzzy multi-criteria decision making (Fuzzy AHP and TOPSIS), Fuzzy c-Means clustering (FCM) objective minimization, and Adaptive Neuro-Fuzzy Inference Systems (ANFIS). Features 8 interactive 60 FPS Canvas simulations and 24 tiered solved examination problems with complete line-by-line mathematical proofs.",
        "units": processed_units
    }

    # Verify strictly zero course numbers
    json_str = json.dumps(course_data, ensure_ascii=False, indent=2)
    course_code_matches = re.findall(r'MTH[\s-]*\d+|4204', json_str, re.IGNORECASE)
    if course_code_matches:
        raise ValueError(f"STRICT ERROR: Prohibited course codes detected in data: {course_code_matches}")

    out_file = "fuzzy-mathematics-data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Fuzzy Mathematics Master Textbook Data File\n")
        f.write("// STRICT CONSTRAINT: ZERO COURSE NUMBERS OR CODES PERMITTED\n")
        f.write("window.COURSE_DATA = ")
        f.write(json_str)
        f.write(";\n")

    print(f"Successfully generated {out_file} with {len(processed_units)} units, "
          f"{sum(len(u['sections']) for u in processed_units)} sections, and "
          f"{sum(len(u['problems']) for u in processed_units)} solved problems.")

if __name__ == "__main__":
    assemble_fuzzy_data()
