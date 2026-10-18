"""
assemble_quantum_data.py
Assembles the complete master course data for Quantum Chemistry and Statistical Thermodynamics.
Produces quantum-chemistry-thermodynamics-data.js.
Performs word count verification (>55,000 words) and prohibited tokens audit (0 matches).
"""

import json
import re
import build_quantum_units_1_2_3
import build_quantum_units_4_5_6
import build_quantum_units_7_8_9_10
import expand_quantum_section8
import expand_quantum_problem8
import expand_quantum_problem9
import expand_quantum_deep
import expand_quantum_monograph

def assemble_course_data():
    units_1_2_3 = build_quantum_units_1_2_3.get_units_1_2_3()
    units_4_5_6 = build_quantum_units_4_5_6.get_units_4_5_6()
    units_7_8_9_10 = build_quantum_units_7_8_9_10.get_units_7_8_9_10()

    all_units = units_1_2_3 + units_4_5_6 + units_7_8_9_10
    sec8_dict = expand_quantum_section8.get_section8_dict()
    prob8_dict = expand_quantum_problem8.get_problem8_dict()
    prob9_dict = expand_quantum_problem9.get_problem9_dict()
    deep_dict = expand_quantum_deep.get_deep_dict()
    monograph_dict = expand_quantum_monograph.get_monograph_dict()

    sim_mapping = {
        "unit-1": "sim_qc_blackbody_compton_wavepacket",
        "unit-2": "sim_qc_particle_box_ring_quantum",
        "unit-3": "sim_qc_harmonic_oscillator_ladder",
        "unit-4": "sim_qc_hydrogen_orbital_radial_prob",
        "unit-5": "sim_qc_variational_perturbation_solver",
        "unit-6": "sim_qc_helium_h2_molecule_potential",
        "unit-7": "sim_qc_maxwell_boltzmann_microstates",
        "unit-8": "sim_qc_molecular_partition_functions",
        "unit-9": "sim_qc_chemical_equilibrium_stat_mech",
        "unit-10": "sim_qc_fermi_bose_debye_heat_capacity"
    }

    assembled_units = []

    for u_idx, u in enumerate(all_units):
        uid = u["id"]
        # Ensure unit level simulations
        sim_id = sim_mapping[uid]
        u["simulations"] = [sim_id]
        if len(u["sections"]) > 0:
            u["sections"][0]["simulations"] = [sim_id]

        # Add section 8
        if uid in sec8_dict:
            sec8 = dict(sec8_dict[uid])
            # Enrich section 8 with deep operator supplement and research monograph
            supplements = []
            if uid in deep_dict:
                deep = deep_dict[uid]
                supplements.append(f"\n\n---\n\n## {deep['title_append']}\n\n{deep['content']}")
            if uid in monograph_dict:
                mono = monograph_dict[uid]
                supplements.append(f"\n\n---\n\n## {mono['title']}\n\n{mono['content']}")
            
            sec8["content"] += "".join(supplements)
            u["sections"].append(sec8)

        # Add problem 8
        if uid in prob8_dict:
            u["problems"].append(prob8_dict[uid])

        # Add problem 9
        if uid in prob9_dict:
            u["problems"].append(prob9_dict[uid])

        # Normalize problems: ensure prob.statement, prob.question, prob.problem, prob.id, prob.difficulty
        for p_idx, p in enumerate(u["problems"]):
            problem_text = p.get("statement") or p.get("problem") or p.get("question") or ""
            p["id"] = f"prob-{u_idx+1}-{p_idx+1}"
            p["statement"] = problem_text
            p["problem"] = problem_text
            p["question"] = problem_text
            if "difficulty" not in p:
                p["difficulty"] = "Advanced"

        assembled_units.append(u)

    course_data = {
        "id": "quantum-chemistry-thermodynamics",
        "courseCode": "",
        "title": "Quantum Chemistry and Statistical Thermodynamics",
        "department": "Chemistry",
        "level": "Advanced Undergraduate / Graduate",
        "leadSummary": r"""A master digital textbook and computational interactive treatise on quantum mechanics and statistical thermodynamics. Formulates the foundational principles of quantum chemistry—from historical wave mechanics and solvable potentials (box, ring, harmonic oscillator, rigid rotor) to central force dynamics, the hydrogen atom, fine structure, approximation methods (perturbation and variational theory), multi-electron atomic structures, and molecular orbital and valence bond theories. Bridges microscopic quantum mechanics to macroscopic thermodynamic phenomena through classical and quantum statistical thermodynamics—microstates, statistical ensembles, Maxwell-Boltzmann statistics, molecular partition functions, chemical reaction equilibria, Fermi-Dirac and Bose-Einstein quantum distributions, and condensed matter physics (electron gas, Einstein and Debye heat capacities, and superconductivity). Equipped with ten interactive 60 FPS simulations and 90 multi-step solved problems.""",
        "units": assembled_units
    }

    return course_data

def audit_and_save(course_data):
    json_str = json.dumps(course_data, indent=2, ensure_ascii=False)
    
    # 1. Prohibited Tokens Audit
    prohibited_patterns = [
        r'\bchem\s*\d+',
        r'35\s*\+\s*10\s*\+\s*5',
        r'70\s*\+\s*20\s*\+\s*10',
        r'\b\d+\s*Marks\b',
        r'100\s*Marks',
        r'50\s*Marks',
        r'35\s*Marks',
        r'10\s*Marks',
        r'5\s*Marks',
        r'exam(ination)?\s+marks',
        r'\bgrades?\s*=\s*\d+'
    ]

    print("Auditing for prohibited tokens...")
    violations = []
    for pattern in prohibited_patterns:
        matches = re.findall(pattern, json_str, re.IGNORECASE)
        if matches:
            violations.append((pattern, matches))

    if violations:
        print("PROHIBITED TOKENS DETECTED:")
        for pat, m in violations:
            print(f" - Pattern '{pat}': {m}")
        raise ValueError("Prohibited tokens found in assembled course data!")
    else:
        print("✓ Zero prohibited tokens found! Audit passed.")

    # 2. Section and Problem Counts
    total_sections = sum(len(u["sections"]) for u in course_data["units"])
    total_problems = sum(len(u["problems"]) for u in course_data["units"])
    print(f"Total Units: {len(course_data['units'])}")
    print(f"Total Sections: {total_sections} (Goal: 80)")
    print(f"Total Problems: {total_problems} (Goal: 90)")

    # 3. Word Count Verification
    all_text = []
    all_text.append(course_data["title"])
    all_text.append(course_data["leadSummary"])
    for u in course_data["units"]:
        all_text.append(u["title"])
        all_text.append(u["leadSummary"])
        for s in u["sections"]:
            all_text.append(s["title"])
            all_text.append(s["content"])
        for p in u["problems"]:
            all_text.append(p["title"])
            all_text.append(p["statement"])
            all_text.append(p["solution"])

    full_text = " ".join(all_text)
    words = full_text.split()
    total_words = len(words)
    print(f"Total Word Count: {total_words:,} words (Goal: >55,000 words)")
    if total_words < 55000:
        print(f"WARNING: Word count is {total_words}, below 55,000 target!")
    else:
        print(f"✓ Target exceeded! ({total_words:,} > 55,000)")

    # 4. Save to JavaScript file
    js_content = f"// Quantum Chemistry and Statistical Thermodynamics - Master Data\n// OpenSTEM Milestone #52 (11th Chemistry Textbook)\nwindow.COURSE_DATA = {json_str};\nconst courseData = window.COURSE_DATA;\n\nif (typeof module !== 'undefined' && module.exports) {{\n  module.exports = courseData;\n}}\n"

    with open("quantum-chemistry-thermodynamics-data.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    
    print("Saved quantum-chemistry-thermodynamics-data.js successfully.")
    return total_words

if __name__ == "__main__":
    data = assemble_course_data()
    audit_and_save(data)
