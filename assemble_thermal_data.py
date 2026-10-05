import json

units = []
for i in range(1, 9):
    with open(f"tp_u{i}.json") as f:
        u = json.load(f)
        units.append(u)

data = {
    "courseId": "thermal-physics",
    "courseTitle": "Thermal Physics",
    "courseSubtitle": "Classical Thermodynamics, Statistical Entropy, Thermodynamic Potentials, Heat Transfer & Kinetic Theory",
    "units": units
}

js_content = f"// Thermal Physics Complete Interactive Textbook Dataset\n// Pure client-side data architecture\nwindow.COURSE_DATA = {json.dumps(data, indent=2)};\n"

with open("thermal-physics-data.js", "w") as f:
    f.write(js_content)

print(f"thermal-physics-data.js compiled successfully. Total size: {len(js_content)} bytes across {len(units)} units.")
