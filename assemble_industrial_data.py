# -*- coding: utf-8 -*-
"""
assemble_industrial_data.py
Assembles all units and expansions into industrial-chemistry-data.js (#48).
Audits strictly against prohibited course codes, examination marks, and formula patterns.
"""

import json
import re
import sys
import os

import build_industrial_units_1_2_3
import build_industrial_units_4_5_6
import build_industrial_units_7_8_9_10
import expand_industrial_section8
import expand_industrial_problem8
import expand_industrial_problem9
import expand_industrial_deep
import expand_industrial_monograph

def main():
    print("Loading base units...")
    u123 = build_industrial_units_1_2_3.get_units_1_2_3()
    u456 = build_industrial_units_4_5_6.get_units_4_5_6()
    u78910 = build_industrial_units_7_8_9_10.get_units_7_8_9_10()

    units = u123 + u456 + u78910
    print(f"Loaded {len(units)} base units.")

    print("Injecting Section 8 across all units...")
    units = expand_industrial_section8.inject_section_8(units)

    print("Injecting Problem 8 across all units...")
    units = expand_industrial_problem8.inject_problem_8(units)

    print("Injecting Problem 9 across all units...")
    units = expand_industrial_problem9.inject_problem_9(units)

    print("Injecting deep reference flowsheets and thermodynamic tables...")
    units = expand_industrial_deep.enrich_deep_content(units)

    print("Injecting University Honors research monographs...")
    units = expand_industrial_monograph.inject_monographs(units)

    # Verification of unit counts
    total_sections = sum(len(u["sections"]) for u in units)
    total_problems = sum(len(u["problems"]) for u in units)
    print(f"Total units: {len(units)} (Target: 10)")
    print(f"Total sections: {total_sections} (Target: 80)")
    print(f"Total problems: {total_problems} (Target: 90)")

    for idx, u in enumerate(units, 1):
        sec_count = len(u["sections"])
        prob_count = len(u["problems"])
        print(f"  Unit {idx} ({u['id']}): {sec_count} sections, {prob_count} problems")
        if sec_count != 8:
            print(f"ERROR: Unit {idx} has {sec_count} sections, expected 8!", file=sys.stderr)
            sys.exit(1)
        if prob_count != 9:
            print(f"ERROR: Unit {idx} has {prob_count} problems, expected 9!", file=sys.stderr)
            sys.exit(1)

    course_data = {
        "courseCode": "",
        "courseTitle": "Industrial Chemistry: Chemical Processes, Manufacturing Technologies, Process Engineering & Industrial Quality Control",
        "courseSubtitle": "Fiber Science & Synthetic Polymers, Nitrogen & Phosphorus Fertilizers, Cane & Beet Sugar Refining, Portland Cement & Lime Thermochemistry, Saponification & Synthetic Surfactants, Kraft Pulping & Recovery Boilers, Float Glass & High-Temperature Refractories, Chlor-Alkali Membrane Cells, Petroleum Refining & FCC Riser Dynamics, and Blast Furnace Ironmaking & BOF Decarburization",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "General Chemistry Foundations, Physical Chemistry Thermodynamics & Organic Chemistry Reactions",
        "description": "Exhaustive university honors master digital textbook on Industrial Chemistry: chemical reaction engineering, manufacturing technologies, mass and energy transport phenomena, material balances, phase equilibria, and quality assurance across the heavy chemical and process industries. Features 10 complete units with 80 comprehensive sections, 90 fully solved thermodynamic and engineering problems, and 10 interactive real-time 60 FPS simulations covering every primary chemical commodity manufacturing sector.",
        "units": units
    }

    # Serialize to JSON
    json_str = json.dumps(course_data, indent=2, ensure_ascii=False)
    js_content = f"// Industrial Chemistry Master Textbook Data File\n// STRICT CONSTRAINT: ZERO PROHIBITED CODES PERMITTED\nwindow.COURSE_DATA = {json_str};\n"

    # Strict Banned Pattern Audit
    banned_patterns = [
        (r'\bchem\s*\d+', "Course number pattern like 'Chem 401'"),
        (r'70\s*\+\s*20\s*\+\s*10', "Formula '70 + 20 + 10'"),
        (r'35\s*\+\s*10\s*\+\s*5', "Formula '35 + 10 + 5'"),
        (r'\b\d+\s*Marks\b', "Marks pattern like '100 Marks'"),
        (r'exam(ination)?\s+marks', "Examination marks reference"),
        (r'\bgrades?\s*=\s*\d+', "Grade assignment pattern"),
    ]

    print("\nAuditing against prohibited patterns...")
    audit_passed = True
    for pat, desc in banned_patterns:
        matches = re.findall(pat, js_content, re.IGNORECASE)
        if matches:
            print(f"AUDIT VIOLATION: Found pattern '{desc}': {matches}", file=sys.stderr)
            audit_passed = False

    if not audit_passed:
        print("Audit failed! Aborting write.", file=sys.stderr)
        sys.exit(1)
    else:
        print("AUDIT PASSED: Zero prohibited course codes, marks, or credit formulas detected.")

    out_file = "industrial-chemistry-data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(js_content)

    file_size = os.path.getsize(out_file)
    word_count = len(js_content.split())
    print(f"\nSuccessfully generated {out_file}!")
    print(f"File size: {file_size:,} bytes")
    print(f"Word count: {word_count:,} words")

if __name__ == "__main__":
    main()
