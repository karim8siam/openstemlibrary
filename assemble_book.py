# -*- coding: utf-8 -*-
import json
import unit1_data
import unit2_data
import unit3_data
import unit4_data
import unit5_data
import unit6_data

units = [
    unit1_data.UNIT_1,
    unit2_data.UNIT_2,
    unit3_data.UNIT_3,
    unit4_data.UNIT_4,
    unit5_data.UNIT_5,
    unit6_data.UNIT_6
]

course_data = {
    "courseCode": "PHYSICS",
    "courseTitle": "Electrodynamics",
    "edition": "Interactive Digital Textbook Edition",
    "textbookTitle": "Principles of Classical Electrodynamics: Field Equations, Wave Propagation, Radiation & Dispersion",
    "author": "OpenSTEM Academic Press",
    "units": units
}

js_content = "// Electrodynamics — Universal University Standard Textbook Edition\n"
js_content += "// Complete, rigorous, comprehensive academic chapters covering all 6 syllabus units.\n\n"
js_content += "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

output_path = "/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/electrodynamics-data.js"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully assembled {output_path}. Total size: {len(js_content)} bytes")
