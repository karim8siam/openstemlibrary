# Assemble script for Electricity and Magnetism dataset
import json

units = []
for u in range(1, 9):
    with open(f"em_u{u}.json") as f:
        units.append(json.load(f))

course_data = {
    "courseTitle": "Electricity and Magnetism",
    "courseCode": "PHYSICS",
    "department": "Department of Physics",
    "institution": "OpenSTEM Global Academic Press",
    "authorContact": "shahriyarkarimsiam@gmail.com",
    "units": units
}

js_content = "// Electricity and Magnetism (Physics Core Courseware)\n"
js_content += "// Comprehensive university-standard textbook dataset covering all 8 Units with KaTeX derivations and 24 solved exam problems.\n\n"
js_content += "window.COURSE_DATA = " + json.dumps(course_data, indent=2) + ";\n"

with open("electricity-magnetism-data.js", "w") as f:
    f.write(js_content)

print(f"Successfully generated electricity-magnetism-data.js with {len(units)} units!")
