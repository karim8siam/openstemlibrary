import json

units = []
for i in range(1, 7):
    with open(f"amp_u{i}.json", "r") as f:
        u = json.load(f)
        units.append(u)

course_data = {
    "courseId": "atomic-molecular-physics",
    "courseTitle": "Atomic and Molecular Physics: Special Relativity, Quantum Structure & Spectroscopy",
    "courseDescription": "A rigorous, university-grade digital textbook covering the Special Theory of Relativity, wave-particle duality, X-ray physics, matter waves, the Rutherford-Bohr atom, multi-electron quantum structure, spin-orbit fine structure, Zeeman splitting, chemical bonding, and molecular rotational, vibrational, electronic, and Raman spectroscopy.",
    "units": units
}

js_content = f"window.COURSE_DATA = {json.dumps(course_data, indent=2)};\n"

with open("atomic-molecular-data.js", "w") as f:
    f.write(js_content)

print(f"atomic-molecular-data.js successfully written with {len(units)} units!")
