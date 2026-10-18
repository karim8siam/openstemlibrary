# -*- coding: utf-8 -*-
"""
generate_pchem1_data.py
Assembles physical-chemistry-1-data.js from Units 1 to 8.
Ensures strictly ZERO course codes or numbers (e.g. Chem. 110F).
"""

import json
import re
import build_pchem1_unit1 as u1
import build_pchem1_unit2 as u2
import build_pchem1_unit3 as u3
import build_pchem1_unit4 as u4
import build_pchem1_unit5 as u5
import build_pchem1_unit6 as u6
import build_pchem1_unit7 as u7
import build_pchem1_unit8 as u8

sim_map = {
    1: "sim_chem_dimensional_matter_converter",
    2: "sim_chem_gas_laws_maxwell_boltzmann",
    3: "sim_chem_calorimetry_hess_cycle",
    4: "sim_chem_crystal_lattice_unit_cell",
    5: "sim_chem_solution_colligative_properties",
    6: "sim_chem_reaction_kinetics_arrhenius",
    7: "sim_chem_equilibrium_le_chatelier",
    8: "sim_chem_galvanic_cell_nernst"
}

diff_class_map = {
    "Foundational Level": "diff-easy",
    "Advanced Level": "diff-medium",
    "Honors / Proof Challenge": "diff-hard"
}

units_raw = [
    u1.get_unit1(),
    u2.get_unit2(),
    u3.get_unit3(),
    u4.get_unit4(),
    u5.get_unit5(),
    u6.get_unit6(),
    u7.get_unit7(),
    u8.get_unit8()
]

formatted_units = []

for idx, u in enumerate(units_raw, 1):
    sim_id = sim_map[idx]
    
    # Process sections
    formatted_sections = []
    for s_idx, sec in enumerate(u["sections"], 1):
        sec_num = sec.get("secNumber", f"{idx}.{s_idx}")
        # Mount simulation inline on section 5 of each unit
        sec_sims = [sim_id] if s_idx == 5 else []
        formatted_sections.append({
            "id": f"sec{idx}-{s_idx}",
            "secNumber": sec_num,
            "title": sec["title"],
            "heading": sec["title"],
            "content": sec["content"],
            "simulations": sec_sims
        })
        
    # Process problems
    formatted_problems = []
    for p_idx, prob in enumerate(u["problems"], 1):
        tier = prob.get("tier", "Solved Problem")
        diff_class = diff_class_map.get(tier, "diff-medium")
        prob_title = prob["title"]
        stmt = prob.get("statement", "")
        sol = prob.get("solution", "")
        
        formatted_problems.append({
            "id": f"p{idx}-{p_idx}",
            "difficulty": diff_class,
            "difficultyLabel": tier,
            "title": f"Problem {idx}.{p_idx}: {prob_title}",
            "question": stmt,
            "statement": stmt,
            "solution": sol
        })
        
    formatted_units.append({
        "id": f"unit{idx}",
        "unitId": f"unit{idx}-pchem1",
        "number": idx,
        "unitNumber": idx,
        "title": f"Unit {idx}: {u['title']}",
        "description": u.get("leadSummary", ""),
        "leadSummary": u.get("leadSummary", ""),
        "simulations": [sim_id],
        "sections": formatted_sections,
        "problems": formatted_problems
    })

course_data = {
    "courseCode": "",
    "courseTitle": "Physical Chemistry I: States of Matter, Thermochemistry, Kinetics, Equilibrium & Electrochemistry",
    "courseSubtitle": "States of Matter, Kinetic Molecular Theory, Real Gases, Thermochemistry, Condensed States & Crystals, Solutions & Colligative Properties, Chemical Kinetics, Dynamic Equilibrium, and Electrochemistry",
    "credits": 4,
    "lectureHours": 60,
    "prerequisites": "General Chemistry, Multivariate Calculus & Introductory Physics",
    "description": (
        "Comprehensive honors-level master digital textbook on physical chemistry: "
        "classification of matter, SI measurement metrics, dimensional analysis, and extensive vs intensive properties; "
        "kinetic molecular theory of gases, Maxwell-Boltzmann speed distributions, real gas non-ideality, van der Waals equation of state, and gas liquefaction; "
        "thermochemical principles, state functions, first law of thermodynamics, enthalpy of reactions, Hess's law cycles, Kirchhoff's law, and bomb calorimetry; "
        "intermolecular forces, liquid surface tension, viscosity, Clausius-Clapeyron vapor pressure, and solid-state crystal lattices (Bravais, Bragg X-ray diffraction, and unit cell geometry); "
        "physical properties of solutions, Raoult's and Henry's laws, colligative phenomena (freezing depression, boiling elevation, osmotic pressure, van 't Hoff factors), and Nernst distribution law; "
        "chemical kinetics, rate laws, integrated rate equations, reaction mechanisms, Arrhenius activation energy, collision theory, transition state theory, and catalysis; "
        "dynamic chemical equilibria, Law of Mass Action, relation between Kp, Kc, and Kx, reaction quotients, Le Châtelier's principle perturbations, van 't Hoff isobar, and aqueous acid-base equilibria; "
        "and electrochemistry, half-reaction ion-electron balancing, galvanic cells, Standard Hydrogen Electrode, standard reduction potentials, Nernst equation, cell thermodynamics (ΔG°, ΔS°, ΔH°), primary/secondary batteries, lithium-ion intercalation, fuel cells, metallic corrosion mechanisms, electrolytic cells, Faraday's laws of electrolysis, overpotentials, and industrial chlor-alkali electrometallurgy. "
        "Features 8 interactive 60 FPS Canvas simulations and 24 tiered solved problems with complete line-by-line mathematical proofs."
    ),
    "units": formatted_units
}

# Serialize to JSON with formatting
json_str = json.dumps(course_data, indent=2, ensure_ascii=False)

# Check strictly for zero course codes/numbers
forbidden_patterns = [r'Chem\.?\s*110F', r'\b110F\b', r'Chem\s+110']
for pattern in forbidden_patterns:
    matches = re.findall(pattern, json_str, re.IGNORECASE)
    if matches:
        raise ValueError(f"CRITICAL ERROR: Found forbidden course number matching pattern '{pattern}': {matches}")

output_js = f"""// Physical Chemistry I Master Textbook Data File
// STRICT CONSTRAINT: ZERO COURSE NUMBERS OR CODES PERMITTED
window.COURSE_DATA = {json_str};
"""

with open("physical-chemistry-1-data.js", "w", encoding="utf-8") as f:
    f.write(output_js)

print("SUCCESS: physical-chemistry-1-data.js generated successfully.")
print(f"Total units: {len(course_data['units'])}")
print(f"Total sections: {sum(len(u['sections']) for u in course_data['units'])}")
print(f"Total problems: {sum(len(u['problems']) for u in course_data['units'])}")
