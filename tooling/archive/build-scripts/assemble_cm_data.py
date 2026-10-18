# Script to assemble classical-mechanics-data.js from cm_u1.json to cm_u8.json
import json

sim_mappings = {
    1: { "u1-sec2": "rotating-wire-hoop-sim", "u1-sec1": "particle-system-momentum-sim" },
    2: { "u2-sec5": "double-pendulum-sim", "u2-sec1": "brachistochrone-sim" },
    3: { "u3-sec3": "effective-potential-sim", "u3-sec4": "kepler-orbit-sim", "u3-sec6": "rutherford-scattering-sim" },
    4: { "u4-sec4": "tennis-racket-sim", "u4-sec5": "euler-top-sim" },
    5: { "u5-sec1": "phase-space-oscillator-sim" },
    6: { "u6-sec5": "poincare-section-sim" },
    7: { "u7-sec1": "michelson-morley-sim", "u7-sec3": "lorentz-contraction-sim" },
    8: { "u8-sec1": "minkowski-spacetime-sim", "u8-sec4": "relativistic-collision-sim" }
}

units = []
for i in range(1, 9):
    with open(f"cm_u{i}.json", "r", encoding="utf-8") as f:
        u = json.load(f)
    u["id"] = f"unit-{i}"
    u["number"] = i
    u["unitNumber"] = i
    
    # Attach simulations
    mappings = sim_mappings.get(i, {})
    for sec in u["sections"]:
        sec_id = sec["id"]
        if sec_id in mappings:
            sec["simulation"] = mappings[sec_id]
            
    units.append(u)

course_dict = {
    "courseId": "classical-mechanics",
    "courseTitle": "Classical Mechanics & Relativistic Dynamics",
    "courseSubtitle": "Lagrangian & Hamiltonian Formulations, Rigid Bodies, Poisson Brackets & Special Relativity",
    "units": units
}

# Write to classical-mechanics-data.js
js_content = "// Classical Mechanics & Special Relativity Academic Data\n"
js_content += "// Comprehensive university-standard curriculum with complete derivations & solved exam problems\n\n"
js_content += "window.COURSE_DATA = " + json.dumps(course_dict, indent=2, ensure_ascii=False) + ";\n"

with open("classical-mechanics-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("classical-mechanics-data.js successfully assembled!")
