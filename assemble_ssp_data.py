import json

units = []
for i in range(1, 9):
    with open(f"ssp_u{i}.json", "r") as f:
        u = json.load(f)
        units.append(u)

course_data = {
    "courseId": "solid-state-physics",
    "courseTitle": "Solid State Physics: Crystal Structure, Lattice Dynamics, Electron Theory & Semiconductors",
    "courseDescription": "A rigorous, university-grade digital textbook covering the crystalline state, 14 Bravais lattices, X-ray diffraction, cohesive bonding, Madelung constants, phonons and lattice vibrations, Einstein and Debye heat capacities, Sommerfeld free electron theory, energy band gaps, Bloch electrons, effective mass, dielectric phenomena, plasmons, and semiconductor physics with 16 interactive 60 FPS simulations.",
    "units": units
}

js_content = f"window.COURSE_DATA = {json.dumps(course_data, indent=2)};\n"

with open("solid-state-data.js", "w") as f:
    f.write(js_content)

print(f"solid-state-data.js successfully written with {len(units)} units!")
