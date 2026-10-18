# -*- coding: utf-8 -*-
"""
assemble_kinetics_data.py
Assembles all 10 units of Molecular Motion and Reaction Kinetics into molecular-motion-kinetics-data.js.
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

import json
import re
import os

from build_kinetics_units_1_2_3 import get_units_1_2_3
from build_kinetics_units_4_5_6 import get_units_4_5_6
from build_kinetics_units_7_8_9_10 import get_units_7_8_9_10
from expand_kinetics_section8 import inject_section_8
from expand_kinetics_problem8 import inject_problem_8
from expand_kinetics_problem9 import inject_problem_9
from expand_kinetics_deep import enrich_deep_content
from expand_kinetics_monograph import inject_monographs

def main():
    print("Gathering all units...")
    all_units = get_units_1_2_3() + get_units_4_5_6() + get_units_7_8_9_10()
    print(f"Base units loaded: {len(all_units)}")

    print("Injecting Section 8 across all units...")
    all_units = inject_section_8(all_units)

    print("Injecting Problem 8 across all units...")
    all_units = inject_problem_8(all_units)

    print("Injecting Problem 9 across all units...")
    all_units = inject_problem_9(all_units)

    print("Enriching deep content (flowsheets, tables, proofs)...")
    all_units = enrich_deep_content(all_units)

    print("Injecting research monographs...")
    all_units = inject_monographs(all_units)

    # Attach simulations to sections[0] of each unit so app.js can mount simulation canvas
    for u in all_units:
        if "simulations" in u and len(u["simulations"]) > 0:
            u["sections"][0]["simulations"] = list(u["simulations"])

    # Verify unit counts
    total_sections = sum(len(u["sections"]) for u in all_units)
    total_problems = sum(len(u["problems"]) for u in all_units)
    print(f"Total units: {len(all_units)}")
    print(f"Total sections: {total_sections}")
    print(f"Total problems: {total_problems}")

    assert len(all_units) == 10, f"Expected exactly 10 units, got {len(all_units)}"
    assert total_sections == 80, f"Expected exactly 80 sections, got {total_sections}"
    assert total_problems == 90, f"Expected exactly 90 problems, got {total_problems}"

    course_data = {
        "courseId": "molecular-motion-reaction-kinetics",
        "courseCode": "",
        "courseTitle": "Molecular Motion and Reaction Kinetics",
        "department": "Chemistry",
        "description": "Comprehensive master digital textbook on molecular transport phenomena, fluid dynamics, empirical and microscopic chemical reaction kinetics, unimolecular and chain reaction dynamics, catalytic systems, and molecular reaction dynamics with 10 interactive simulations, 80 sections, and 90 solved problems.",
        "units": all_units
    }

    js_code = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

    # Strict Banned Regex Audit
    banned_patterns = [
        r'\bchem\s*\d+',
        r'35\s*\+\s*10\s*\+\s*5',
        r'70\s*\+\s*20\s*\+\s*10',
        r'\b\d+\s*Marks\b',
        r'50\s*Marks',
        r'100\s*Marks',
        r'exam(ination)?\s+marks',
        r'\bgrades?\s*=\s*\d+'
    ]

    for pat in banned_patterns:
        m = re.search(pat, js_code, re.IGNORECASE)
        if m:
            raise ValueError(f"Strict prohibited token matched pattern '{pat}': {m.group(0)}")

    out_path = "molecular-motion-kinetics-data.js"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(js_code)

    file_size_kb = os.path.getsize(out_path) / 1024
    words = len(js_code.split())
    print(f"Successfully generated {out_path} ({file_size_kb:.1f} KB, ~{words} words).")
    print("Passed all strict prohibited token audits!")

if __name__ == "__main__":
    main()
