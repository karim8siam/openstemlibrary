# -*- coding: utf-8 -*-
"""
generate_na_data.py
Assembles numerical-analysis-data.js containing all 8 units,
32 comprehensive sections, 24 tiered solved problems, and 8 simulations.
Strictly zero course numbers. Universal master digital textbook.
"""

import json
import build_unit1
import build_unit2
import build_unit3
import build_unit4
import build_unit5
import build_unit6
import build_unit7
import build_unit8

def normalize_problem(prob, unit_num, idx):
    tier_raw = prob.get("tier", idx + 1)
    if tier_raw in (1, "1", "Foundational"):
        diff = "Easy"
        label = "Tier 1: Foundational Concept"
    elif tier_raw in (2, "2", "Advanced"):
        diff = "Medium"
        label = "Tier 2: Advanced Algorithmic"
    else:
        diff = "Hard"
        label = "Tier 3: Honors / Proof Challenge"

    res = {
        "id": prob.get("id", f"na-prob-{unit_num}-{idx+1}"),
        "difficulty": prob.get("difficulty", diff),
        "difficultyLabel": prob.get("difficultyLabel", label),
        "title": prob.get("title", f"Solved Problem {unit_num}.{idx+1}"),
        "statement": prob.get("statement", ""),
        "solution": prob.get("solution", "")
    }
    if "hints" in prob:
        res["hints"] = prob["hints"]
    if "answer" in prob:
        res["answer"] = prob["answer"]
    return res

def build_numerical_analysis_data():
    course = {
        "courseCode": "",
        "courseTitle": "Numerical Analysis & Computational Methods",
        "courseSubtitle": "Algorithms, Error Analysis, Numerical Calculus, Linear Systems & Differential Equations",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "Calculus I, Calculus II, Linear Algebra & Ordinary Differential Equations",
        "description": "Exhaustive honors-level digital textbook covering algorithmic numerical approximations, IEEE floating-point error theory, bracketing and open root-finding, polynomial interpolation and Runge's phenomenon, numerical differentiation and high-order Gaussian quadrature, direct and iterative numerical linear algebra, single-step and multi-step ODE initial value solvers, Dahlquist absolute stability theory, stiff differential equations, and shooting and finite difference boundary value algorithms with 8 interactive 60 FPS simulations and 24 tiered solved examination problems.",
        "units": [],
        "problems": []
    }

    raw_units = [
        build_unit1.get_unit1(),
        build_unit2.get_unit2(),
        build_unit3.get_unit3(),
        build_unit4.get_unit4(),
        build_unit5.get_unit5(),
        build_unit6.get_unit6(),
        build_unit7.get_unit7(),
        build_unit8.get_unit8(),
    ]

    all_course_problems = []

    for u_idx, raw_u in enumerate(raw_units, start=1):
        unit_num = raw_u.get("number", u_idx)
        clean_title = raw_u["title"]
        if not clean_title.startswith(f"Unit {unit_num}:"):
            full_title = f"Unit {unit_num}: {clean_title}"
        else:
            full_title = clean_title

        unit_probs = []
        for p_idx, p in enumerate(raw_u.get("problems", [])):
            norm_p = normalize_problem(p, unit_num, p_idx)
            unit_probs.append(norm_p)
            all_course_problems.append(norm_p)

        sections = []
        for s_idx, sec in enumerate(raw_u.get("sections", []), start=1):
            sec_num = sec.get("secNumber", f"{unit_num}.{s_idx}")
            s_dict = {
                "id": sec.get("id", f"u{unit_num}-sec{s_idx}"),
                "secNumber": sec_num,
                "title": sec["title"],
                "content": sec["content"],
                "simulations": sec.get("simulations", raw_u.get("simulations", []))
            }
            sections.append(s_dict)

        unit_obj = {
            "id": f"unit{unit_num}",
            "unitId": f"unit{unit_num}-na",
            "number": unit_num,
            "unitNumber": unit_num,
            "title": full_title,
            "description": raw_u.get("leadSummary", ""),
            "leadSummary": raw_u.get("leadSummary", ""),
            "simulations": raw_u.get("simulations", []),
            "sections": sections,
            "problems": unit_probs
        }
        course["units"].append(unit_obj)

    course["problems"] = all_course_problems

    js_content = f"// OpenSTEM Digital Textbook - Numerical Analysis & Computational Methods\n// Auto-generated master dataset with 8 comprehensive units\nwindow.COURSE_DATA = {json.dumps(course, indent=2, ensure_ascii=False)};\n"

    output_file = "numerical-analysis-data.js"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"Successfully generated {output_file}!")
    print(f"Total units: {len(course['units'])}")
    total_sections = sum(len(u['sections']) for u in course['units'])
    print(f"Total sections: {total_sections}")
    print(f"Total problems: {len(course['problems'])}")
    print(f"File size: {len(js_content):,} bytes")

if __name__ == "__main__":
    build_numerical_analysis_data()
