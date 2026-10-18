# assemble_plasma_data.py
# Assembles plasma_u1.json through plasma_u8.json into plasma-physics-data.js

import json

SIM_MAPPING = {
    "sec-1-4": "plasma-debye-shielding-sim",
    "sec-1-7": "plasma-dc-discharge-paschen-sim",
    "sec-2-2": "plasma-cyclotron-exb-sim",
    "sec-2-6": "plasma-polarization-drift-sim",
    "sec-3-2": "plasma-gradient-curvature-drift-sim",
    "sec-3-6": "plasma-magnetic-mirror-sim",
    "sec-4-5": "plasma-diamagnetic-drift-sim",
    "sec-4-7": "plasma-flux-freezing-mhd-sim",
    "sec-5-4": "plasma-langmuir-bohm-gross-sim",
    "sec-5-5": "plasma-ion-acoustic-wave-sim",
    "sec-6-2": "plasma-em-wave-cutoff-sim",
    "sec-6-5": "plasma-whistler-faraday-sim",
    "sec-7-2": "plasma-alfven-wave-sim",
    "sec-7-6": "plasma-rayleigh-taylor-kink-sim",
    "sec-8-3": "plasma-vlasov-phase-space-sim",
    "sec-8-6": "plasma-landau-damping-sim"
}

UNIT_SIMS = {
    1: ["plasma-debye-shielding-sim", "plasma-dc-discharge-paschen-sim"],
    2: ["plasma-cyclotron-exb-sim", "plasma-polarization-drift-sim"],
    3: ["plasma-gradient-curvature-drift-sim", "plasma-magnetic-mirror-sim"],
    4: ["plasma-diamagnetic-drift-sim", "plasma-flux-freezing-mhd-sim"],
    5: ["plasma-langmuir-bohm-gross-sim", "plasma-ion-acoustic-wave-sim"],
    6: ["plasma-em-wave-cutoff-sim", "plasma-whistler-faraday-sim"],
    7: ["plasma-alfven-wave-sim", "plasma-rayleigh-taylor-kink-sim"],
    8: ["plasma-vlasov-phase-space-sim", "plasma-landau-damping-sim"]
}

course_data = {
    "courseId": "plasma-physics",
    "courseTitle": "Plasma Physics: Single-Particle Dynamics, Fluid Theory, Waves, MHD & Kinetic Landau Damping",
    "courseDescription": "A comprehensive, university-grade digital textbook covering Debye shielding, plasma parameters, single-particle Lorentz dynamics, guiding center drifts, adiabatic invariants, magnetic mirrors, multi-fluid equations, diamagnetic drift, ideal magnetohydrodynamics (MHD), flux-freezing, electrostatic Langmuir and ion acoustic waves, electromagnetic waves in magnetized plasmas, whistlers, Faraday rotation, shear Alfvén waves, fast/slow magnetosonic modes, Rayleigh-Taylor and kink instabilities, Vlasov kinetic theory, and collisionless Landau damping with 16 interactive 60 FPS simulations.",
    "units": []
}

for i in range(1, 9):
    filename = f"plasma_u{i}.json"
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
            "id": p.get("id", f"plasma-prob-{i}-{p_idx+1}"),
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
        "unitId": f"unit{i}-plasma",
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

js_content = f"window.COURSE_DATA = {json.dumps(course_data, indent=2)};\nwindow.PLASMA_COURSE_DATA = window.COURSE_DATA;\n"

with open("plasma-physics-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"plasma-physics-data.js successfully written ({len(js_content)} bytes, {len(course_data['units'])} units)")
