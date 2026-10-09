# -*- coding: utf-8 -*-
"""
assemble_nuclear_data.py
Assembles the complete nuclear-radiochemistry-data.js master textbook data file.
Integrates Units 1-10, 80 sections, 90 solved problems, deep reference tables, and monographs.
Performs strict audit against all prohibited course numbers, codes, and examination marks.
"""

import json
import re
import sys
import os

import build_nuclear_units_1_2_3
import build_nuclear_units_4_5_6
import build_nuclear_units_7_8_9_10
import expand_nuclear_section8
import expand_nuclear_problem8
import expand_nuclear_problem9
import expand_nuclear_deep
import expand_nuclear_monograph

def main():
    print("Step 1: Gathering Units 1-10...")
    u_123 = build_nuclear_units_1_2_3.get_units_1_2_3()
    u_456 = build_nuclear_units_4_5_6.get_units_4_5_6()
    u_78910 = build_nuclear_units_7_8_9_10.get_units_7_8_9_10()
    units = u_123 + u_456 + u_78910
    print(f"Loaded {len(units)} units.")

    print("Step 2: Appending Section 8 across all units (80 sections total)...")
    units = expand_nuclear_section8.add_section_8_to_units(units)

    print("Step 3: Appending Problem 8 across all units (80 problems)...")
    units = expand_nuclear_problem8.add_problem_8_to_units(units)

    print("Step 4: Appending Problem 9 across all units (90 problems total)...")
    units = expand_nuclear_problem9.add_problem_9_to_units(units)

    print("Step 5: Appending Deep Reference Data across all units...")
    units = expand_nuclear_deep.append_deep_reference_data(units)

    print("Step 6: Appending University Honors Research Monographs across all units...")
    units = expand_nuclear_monograph.append_monographs(units)

    # Unit validation
    total_sections = 0
    total_problems = 0
    for u in units:
        secs = len(u.get('sections', []))
        probs = len(u.get('problems', []))
        total_sections += secs
        total_problems += probs
        print(f"Unit {u['unitNumber']}: {secs} sections, {probs} solved problems, sims: {u.get('simulations', [])}")
        assert secs == 8, f"Unit {u['unitNumber']} has {secs} sections, expected 8!"
        assert probs == 9, f"Unit {u['unitNumber']} has {probs} problems, expected 9!"

    print(f"Total Units: {len(units)}")
    print(f"Total Sections: {total_sections} (Target: 80)")
    print(f"Total Solved Problems: {total_problems} (Target: 90)")
    assert len(units) == 10, "Expected 10 units!"
    assert total_sections == 80, "Expected 80 sections!"
    assert total_problems == 90, "Expected 90 problems!"

    course_data = {
        "courseCode": "",
        "courseTitle": "Nuclear and Radiochemistry: Decay Kinetics, Nuclear Structure, Reaction Cross-Sections, Fission & Fusion Energetics, Radiation Chemistry, and Radioanalytical Instrumentation",
        "courseSubtitle": "The Discovery of Radioactivity, Liquid Drop & Shell Models, Bateman Decay Equations & Branching Equilibria, Quantum S-Matrix Kinematics, Breit-Wigner Resonances, Fission Reactor Kinetics, Gamow Stellar Nucleosynthesis, Track Structure & Water Radiolysis, HPGe Semiconductor Spectroscopy, PUREX Solvent Extraction, and Neutron Activation Analysis",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "General Chemistry Foundations, Physical Chemistry Thermodynamics & Quantum Mechanics Foundations",
        "description": "Exhaustive university honors master digital textbook on Nuclear and Radiochemistry: historical evolution from Becquerel and the Curies through Rutherford scattering kinematics and Soddy displacement laws; nuclear composition, nuclear radius scaling, nuclear density, mass defect, nuclear binding energy systematics, and the semi-empirical mass formula (liquid drop model, Bethe-von Weizsäcker equation); nuclear stability, odd-even pairing effects, magic numbers, single-particle shell model with spin-orbit coupling, and collective rotational-vibrational modes; radioactive decay kinetics, differential decay laws, half-life and mean lifetime, multi-nuclide Bateman equations, secular and transient equilibria, and branched decay branching ratios; nuclear reaction mechanics, kinematics, relativistic and non-relativistic Q-value energetics, threshold energies, Coulomb potential barrier penetration, Breit-Wigner single-level resonance cross-sections, compound nucleus Bohr independence hypothesis, and direct nuclear reactions; nuclear fission physics, symmetric vs asymmetric mass distributions, prompt and delayed neutron kinetics, four-factor and six-factor criticality equations, point reactor kinetics, delayed neutron precursors, decay heat, and commercial nuclear reactor architectures (PWR, BWR, CANDU, Sodium Fast Breeders, Molten Salt SMRs); thermonuclear fusion and stellar nucleosynthesis, Coulomb tunneling, Gamow peak derivation, solar proton-proton chains, CNO catalytic cycles, triple-alpha helium burning, advanced carbon/oxygen/silicon burning, core-collapse supernova shockwaves, s-process, r-process, and magnetic confinement tokamak plasma physics; radiation chemistry and track structure, picosecond radiolysis of liquid water, hydrated electron thermodynamics and spectroscopy, Fricke ferrous sulfate chemical dosimetry, Cerics and alanine dosimetry, radiation processing, and radiolytic corrosion mitigation in reactor water chemistry; nuclear radiation instrumentation, gas-filled ionization chambers, proportional counters, Geiger-Müller tubes with halogen quenching and dead-time corrections, inorganic NaI(Tl) and plastic scintillators, High-Purity Germanium (HPGe) semiconductor detectors, Fano factor limits, multichannel analyzers, and coincidence counting electronics; radiochemical separation and carrier chemistry, coprecipitation, isotopic and non-isotopic carriers, liquid-liquid solvent extraction (the industrial PUREX process, tri-n-butyl phosphate adducts, and trivalent actinide/lanthanide partitioning via TALSPEAK/SANEX), ion-exchange chromatography, and radioisotope generator elution systems (Mo-99/Tc-99m, Ge-68/Ga-68, Sr-82/Rb-82); and applied analytical radiochemistry, thermal neutron activation analysis (k0-NAA), isotope dilution analysis (direct, inverse, and substoichiometric), radiocarbon dating with accelerator mass spectrometry (AMS), targeted alpha radiopharmaceuticals (Ac-225, Bi-213, Ra-223), and positron emission tomography (F-18 FDG, Ga-68 DOTATATE). Features 10 interactive 60 FPS Canvas simulations and 90 tiered solved problems with complete line-by-line mathematical, kinetic, and nuclear physical derivations.",
        "units": units
    }

    # JSON serialization
    json_str = json.dumps(course_data, indent=2, ensure_ascii=False)

    # Prohibited pattern audit
    banned_patterns = [
        r'\bchem\s*\d+',
        r'35\s*\+\s*10\s*\+\s*5',
        r'70\s*\+\s*20\s*\+\s*10',
        r'\b\d+\s*Marks\b',
        r'100\s*Marks',
        r'50\s*Marks',
        r'exam(ination)?\s+marks',
        r'\bgrades?\s*=\s*\d+',
    ]

    print("Step 7: Performing strict regex audit against prohibited codes and marks...")
    for pat in banned_patterns:
        matches = re.findall(pat, json_str, flags=re.IGNORECASE)
        if matches:
            print(f"CRITICAL ERROR: Banned pattern '{pat}' found in output! Matches: {matches[:5]}")
            sys.exit(1)
    print("AUDIT PASSED: Zero prohibited codes, course numbers, credit formulas, or examination marks found.")

    output_js = f"// Nuclear and Radiochemistry Master Textbook Data File\n// STRICT CONSTRAINT: ZERO PROHIBITED CODES PERMITTED\nwindow.COURSE_DATA = {json_str};\n"

    target_path = "nuclear-radiochemistry-data.js"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(output_js)

    file_size = os.path.getsize(target_path)
    words = len(output_js.split())
    lines = len(output_js.splitlines())
    print(f"Successfully generated {target_path}!")
    print(f"File Size: {file_size:,} bytes")
    print(f"Total Words: {words:,} words")
    print(f"Total Lines: {lines:,} lines")

if __name__ == "__main__":
    main()
