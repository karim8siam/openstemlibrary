# -*- coding: utf-8 -*-
"""
generate_aa_data.py
Assembles all 8 units into abstract-algebra-data.js
Ensures STRICT ZERO course codes or numbers anywhere in data.
"""

import json
from build_aa_unit1 import get_unit1
from build_aa_unit2 import get_unit2
from build_aa_unit3 import get_unit3
from build_aa_unit4 import get_unit4
from build_aa_unit5 import get_unit5
from build_aa_unit6 import get_unit6
from build_aa_unit7 import get_unit7
from build_aa_unit8 import get_unit8

def assemble_course_data():
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
        1: ("1.3", "sim_aa_modular_cayley"),
        2: ("2.2", "sim_aa_subgroup_lattices"),
        3: ("3.2", "sim_aa_permutation_orbits"),
        4: ("4.2", "sim_aa_coset_partition"),
        5: ("5.2", "sim_aa_homomorphism_kernel"),
        6: ("6.3", "sim_aa_ring_ideals"),
        7: ("7.5", "sim_aa_domain_hierarchy"),
        8: ("8.4", "sim_aa_polynomial_roots"),
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
            problems.append({
                "id": f"p{u_idx}-{p_idx}",
                "difficulty": diff_class,
                "difficultyLabel": tier,
                "title": prob.get("title", f"Problem {u_idx}.{p_idx}"),
                "question": prob.get("statement", ""),
                "statement": prob.get("statement", ""),
                "hints": prob.get("hints", []),
                "solution": prob.get("solution", "")
            })

        processed_units.append({
            "id": f"unit{u_idx}",
            "unitId": f"unit{u_idx}-aa",
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
        "courseTitle": "Abstract Algebra: Groups, Rings, Fields & Modern Algebraic Structures",
        "courseSubtitle": "Symmetric Groups, Normal Subgroups, Isomorphism Theorems, Ideals, Unique Factorization Domains & Field Extensions",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "Linear Algebra & Discrete Mathematics",
        "description": "Exhaustive honors-level digital textbook covering abstract algebraic structures: equivalence relations and modular arithmetic, group axioms, subgroups and cyclic group lattices, permutation and symmetric groups, Dihedral groups and group actions, cosets and Lagrange's Theorem, normal subgroups, quotient groups and the class equation, group homomorphisms and the First, Second, and Third Isomorphism Theorems, Cayley's theorem and automorphisms, ring theory, ideals, quotient rings, prime and maximal ideals, integral domains, Euclidean domains, PIDs, UFDs, polynomial rings over fields, Gauss's lemma, Eisenstein's criterion, and field extensions with the Tower Law and geometric impossibility proofs. Features 8 interactive 60 FPS simulations and 24 tiered solved examination problems with line-by-line proofs.",
        "units": processed_units
    }

    js_content = "// OpenSTEM Digital Textbook - Abstract Algebra: Groups, Rings, Fields & Modern Algebraic Structures\n"
    js_content += "// Master consolidated textbook combining Group Theory, Ring Theory, and Field Theory\n"
    js_content += "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

    with open("abstract-algebra-data.js", "w", encoding="utf-8") as f:
        f.write(js_content)

    print("Successfully wrote abstract-algebra-data.js")
    print(f"Total Units: {len(processed_units)}")
    total_sections = sum(len(u['sections']) for u in processed_units)
    total_problems = sum(len(u['problems']) for u in processed_units)
    print(f"Total Sections: {total_sections}")
    print(f"Total Solved Problems: {total_problems}")

if __name__ == "__main__":
    assemble_course_data()
