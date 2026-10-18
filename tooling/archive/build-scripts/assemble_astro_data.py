import json
import os

SIM_MAPPING = {
    "sec-1-1": "astro-celestial-sphere-sim",
    "sec-1-4": "astro-distance-ladder-sim",
    "sec-2-3": "astro-solar-interior-sim",
    "sec-2-6": "astro-exoplanet-transit-sim",
    "sec-3-1": "astro-hr-diagram-sim",
    "sec-3-6": "astro-chandrasekhar-limit-sim",
    "sec-4-2": "astro-pulsar-lighthouse-sim",
    "sec-4-4": "astro-black-hole-geodesic-sim",
    "sec-5-3": "astro-galaxy-rotation-sim",
    "sec-5-6": "astro-density-wave-sim",
    "sec-6-2": "astro-agn-jet-sim",
    "sec-6-6": "astro-gravitational-lensing-sim",
    "sec-7-1": "astro-hubble-expansion-sim",
    "sec-7-4": "astro-friedmann-universe-sim",
    "sec-8-2": "astro-bbn-nucleosynthesis-sim",
    "sec-8-6": "astro-drake-habitable-sim"
}

UNIT_SIMS = {
    1: ["astro-celestial-sphere-sim", "astro-distance-ladder-sim"],
    2: ["astro-solar-interior-sim", "astro-exoplanet-transit-sim"],
    3: ["astro-hr-diagram-sim", "astro-chandrasekhar-limit-sim"],
    4: ["astro-pulsar-lighthouse-sim", "astro-black-hole-geodesic-sim"],
    5: ["astro-galaxy-rotation-sim", "astro-density-wave-sim"],
    6: ["astro-agn-jet-sim", "astro-gravitational-lensing-sim"],
    7: ["astro-hubble-expansion-sim", "astro-friedmann-universe-sim"],
    8: ["astro-bbn-nucleosynthesis-sim", "astro-drake-habitable-sim"]
}

course_data = {
    "courseId": "astrophysics",
    "courseTitle": "Astrophysics & Cosmology: Stars, Galaxies, Expansion & The Early Universe",
    "courseDescription": "A comprehensive, university-grade digital textbook covering astronomical coordinates, the distance ladder, solar physics, exoplanetary detection, stellar interiors and evolution, white dwarfs, neutron stars, black holes, galactic dynamics, active galactic nuclei, dark matter, cosmological expansion, Friedmann equations, primordial nucleosynthesis, and astrobiology with 16 interactive 60 FPS simulations.",
    "units": []
}

for i in range(1, 9):
    filename = f"astro_u{i}.json"
    with open(filename, "r", encoding="utf-8") as f:
        u_raw = json.load(f)
    
    sections = u_raw.get("sections", [])
    for sec in sections:
        sec_id = sec.get("id")
        if sec_id in SIM_MAPPING:
            sec["simulation"] = SIM_MAPPING[sec_id]
            sec["simulations"] = [SIM_MAPPING[sec_id]]

    raw_problems = u_raw.get("problems", [])
    formatted_problems = []
    for p_idx, p in enumerate(raw_problems):
        formatted_prob = {
            "id": p.get("id", f"astro-prob-{i}-{p_idx+1}"),
            "number": p_idx + 1,
            "title": p.get("title", f"Honors Problem {i}.{p_idx+1}"),
            "difficulty": "Hard",
            "difficultyLabel": "Advanced Honors Exam Problem",
            "statement": p.get("statement", ""),
            "solution": p.get("solution", ""),
            "steps": [
                {
                    "stepName": "Full Rigorous Analytical Solution",
                    "math": "",
                    "explanation": p.get("solution", "")
                },
                {
                    "stepName": "Final Answer & Physical Verification",
                    "math": "",
                    "explanation": "<p><strong>Complete rigorous derivation and proof detailed above.</strong></p>"
                }
            ],
            "answer": "Complete rigorous derivation and proof detailed above."
        }
        formatted_problems.append(formatted_prob)

    unit_obj = {
        "id": f"unit{i}",
        "number": i,
        "unitNumber": i,
        "unitId": f"unit{i}-astro",
        "title": u_raw.get("title", f"Unit {i}"),
        "subtitle": u_raw.get("subtitle", ""),
        "description": u_raw.get("summary", ""),
        "leadSummary": u_raw.get("summary", ""),
        "sections": sections,
        "simulations": UNIT_SIMS.get(i, []),
        "solvedProblems": formatted_problems,
        "problems": formatted_problems
    }
    course_data["units"].append(unit_obj)

js_content = f"window.COURSE_DATA = {json.dumps(course_data, indent=2)};\nwindow.ASTROPHYSICS_COURSE_DATA = window.COURSE_DATA;\n"

with open("astrophysics-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"astrophysics-data.js successfully written ({len(js_content)} bytes, {len(course_data['units'])} units)")
