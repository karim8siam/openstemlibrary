import json

units = []
for i in range(1, 7):
    filename = f"nuc_u{i}.json"
    with open(filename, "r", encoding="utf-8") as f:
        u = json.load(f)
        units.append(u)

course_data = {
    "courseId": "nuclear-physics",
    "courseTitle": "Nuclear Physics: Nuclear Structure, Radioactivity, Reactions & Particle Physics",
    "courseDescription": "A comprehensive, university-grade digital textbook covering nuclear constitution, charge radii, mass defect, binding energy systematics, semi-empirical mass formula (SEMF), nuclear models (liquid drop, shell model with spin-orbit coupling), radioactivity decay kinetics, Bateman equations, radiometric dating, alpha, beta, and gamma transitions, Fermi theory, nuclear reactions, fission dynamics, thermonuclear fusion, radiation interactions with matter, radiation detectors (gas, scintillator, semiconductor), particle accelerators, and the Standard Model of particle physics with 16 interactive 60 FPS simulations.",
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

with open("nuclear-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"nuclear-data.js generated successfully! Total units: {len(units)}")
total_secs = sum(len(u["sections"]) for u in units)
total_probs = sum(len(u.get("problems", [])) for u in units)
print(f"Total sections: {total_secs}, Total problems: {total_probs}")
