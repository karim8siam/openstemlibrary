import json

unit_sim_map = {
    1: [("sec1-1", "qm2-hilbert-state-sim"), ("sec1-7", "qm2-ladder-operator-sim")],
    2: [("sec2-3", "qm2-heisenberg-dynamics-sim"), ("sec2-6", "qm2-rabi-oscillations-sim")],
    3: [("sec3-4", "qm2-stark-zeeman-levels-sim"), ("sec3-6", "qm2-fermi-golden-rule-sim")],
    4: [("sec4-2", "qm2-variational-helium-sim"), ("sec4-6", "qm2-wkb-tunneling-sim")],
    5: [("sec5-3", "qm2-spherical-harmonics-3d-sim"), ("sec5-6", "qm2-clebsch-gordan-sim")],
    6: [("sec6-4", "qm2-fermi-gas-dos-sim"), ("sec6-5", "qm2-landau-levels-sim")],
    7: [("sec7-2", "qm2-partial-wave-scattering-sim"), ("sec7-7", "qm2-born-approximation-sim")],
    8: [("sec7-5_u8", "qm2-dirac-spinor-sim"), ("sec7-8_u8", "qm2-klein-paradox-sim")],
}

units = []
for i in range(1, 9):
    with open(f"qm2_u{i}.json", "r", encoding="utf-8") as f:
        u = json.load(f)
    
    u["unitNumber"] = i
    u["unitId"] = f"unit{i}-qm2"
    
    # Map simulations to sections
    sim_mappings = unit_sim_map.get(i, [])
    sim_ids = []
    for sec_id, sim_id in sim_mappings:
        sim_ids.append(sim_id)
        for sec in u["sections"]:
            if sec["id"] == sec_id:
                sec["simulation"] = sim_id
    u["simulations"] = sim_ids
    
    # Format problems array for app.js renderer
    problems = []
    for p in u.get("solvedProblems", []):
        prob_obj = {
            "id": f"qm2-p-{i}-{p['number']}",
            "number": p["number"],
            "title": p["title"],
            "difficulty": "Honors Exam",
            "statement": p["statement"],
            "solution": p["solution"],
            "steps": [
                {
                    "stepName": "Full Analytical & Rigorous Solution",
                    "math": "",
                    "explanation": p["solution"]
                }
            ],
            "answer": "Complete analytical derivation provided above."
        }
        problems.append(prob_obj)
    u["problems"] = problems
    
    units.append(u)

course_data = {
    "courseId": "quantum-mechanics-2",
    "courseTitle": "Quantum Mechanics II: Advanced Dynamics, Perturbation Theory, Scattering & Relativistic Waves",
    "courseDescription": "A comprehensive, university-grade digital textbook covering Dirac bra-ket algebra, Hilbert space geometry, operator representations, density matrix formalism, harmonic oscillator matrix mechanics, quantum dynamics in Schrödinger, Heisenberg, and interaction pictures, two-level Rabi oscillations, time-independent (non-degenerate and degenerate) perturbation theory, fine structure of hydrogen, Stark and Zeeman effects, time-dependent perturbation theory and Fermi's Golden Rule, variational methods, semiclassical WKB approximation and alpha decay tunneling, adiabatic theorem and Berry phase, general angular momentum Lie algebra, spin-1/2, Clebsch-Gordan coefficients, Wigner-Eckart theorem, identical particles, permutation symmetry, degenerate Fermi gas, Landau levels, partial wave scattering, Born approximation, Lippmann-Schwinger equation, and relativistic Klein-Gordon and Dirac equations with 16 interactive 60 FPS simulations.",
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

with open("qm2-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"qm2-data.js generated successfully! Total units: {len(units)}")
total_secs = sum(len(u["sections"]) for u in units)
total_probs = sum(len(u["problems"]) for u in units)
total_sims = sum(len(u["simulations"]) for u in units)
print(f"Total sections: {total_secs}, Total problems: {total_probs}, Total sims: {total_sims}")
