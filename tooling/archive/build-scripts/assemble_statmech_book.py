import json

units = []
for i in range(1, 8):
    with open(f'/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/unit{i}_data.json') as f:
        units.append(json.load(f))

course_data = {
    "courseTitle": "Statistical Mechanics",
    "courseCode": "PHYSICS",
    "department": "Department of Physics",
    "institution": "OpenSTEM Global Academic Press",
    "authorContact": "shahriyarkarimsiam@gmail.com",
    "units": units
}

js_content = "// Statistical Mechanics (Physics Core Courseware)\n"
js_content += "// Comprehensive university-standard textbook dataset covering all 7 Units with 64 topics, KaTeX derivations, and 21 solved exam problems.\n\n"
js_content += "window.COURSE_DATA = " + json.dumps(course_data, indent=2) + ";\n"

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/statmech-data.js', 'w') as f:
    f.write(js_content)

total_sections = sum(len(u["sections"]) for u in units)
total_problems = sum(len(u["problems"]) for u in units)
print(f"statmech-data.js compiled successfully with {len(units)} units, {total_sections} sections, and {total_problems} solved problems!")
