"""
assemble_spectroscopy_data.py
Assembles the complete master course data for Chemical Spectroscopy (Course #51).
Merges all 10 units, 80 sections, 90 solved problems, 10 interactive simulations,
deep quantum enhancements, and research monographs into chemical-spectroscopy-data.js.
Strictly zero prohibited tokens.
"""

import json
import re
import build_spectroscopy_units_1_2_3 as u123
import build_spectroscopy_units_4_5_6 as u456
import build_spectroscopy_units_7_8_9_10 as u78910
import expand_spectroscopy_section8 as s8
import expand_spectroscopy_problem8 as p8
import expand_spectroscopy_problem9 as p9
import expand_spectroscopy_deep as deep_mod
import expand_spectroscopy_monograph as mono_mod

def build_full_data():
    raw_units = []
    raw_units.extend(u123.get_units_1_2_3())
    raw_units.extend(u456.get_units_4_5_6())
    raw_units.extend(u78910.get_units_7_8_9_10())

    sec8_dict = s8.get_section8_dict()
    prob8_dict = p8.get_problem8_dict()
    prob9_dict = p9.get_unit_problems9()
    deep_dict = deep_mod.get_deep_enhancements()
    mono_dict = mono_mod.get_monograph_enhancements()

    units = []
    for idx, u in enumerate(raw_units, 1):
        # Normalize simulation IDs to strings for app.js compatibility
        raw_sims = u.get("simulations", [])
        sim_ids = [s if isinstance(s, str) else s["id"] for s in raw_sims]

        unit_obj = {
            "id": f"unit-{idx}",
            "unitNumber": idx,
            "title": u["title"],
            "leadSummary": u.get("leadSummary") or u.get("description") or "",
            "simulations": sim_ids,
            "sections": list(u["sections"]),
            "problems": list(u["problems"])
        }

        # Normalize any inline section simulations to string IDs
        for sec in unit_obj["sections"]:
            if "simulations" in sec:
                sec["simulations"] = [s if isinstance(s, str) else s["id"] for s in sec["simulations"]]
            if "simulation" in sec and not isinstance(sec["simulation"], str):
                sec["simulation"] = sec["simulation"]["id"]

        # Append Section 8
        if idx in sec8_dict:
            unit_obj["sections"].append(sec8_dict[idx])

        # Append Problem 8 & Problem 9
        if idx in prob8_dict:
            unit_obj["problems"].append(prob8_dict[idx])
        if idx in prob9_dict:
            unit_obj["problems"].append(prob9_dict[idx])

        # Append Deep Enhancements
        if idx in deep_dict:
            for s_idx, extra in deep_dict[idx].items():
                if s_idx < len(unit_obj["sections"]):
                    unit_obj["sections"][s_idx]["content"] += extra

        # Append Monographs
        if idx in mono_dict:
            for s_idx, extra in mono_dict[idx].items():
                if s_idx < len(unit_obj["sections"]):
                    unit_obj["sections"][s_idx]["content"] += extra

        # Ensure simulation is attached to first section for direct inline rendering
        if unit_obj["simulations"] and len(unit_obj["sections"]) > 0:
            unit_obj["sections"][0]["simulations"] = list(unit_obj["simulations"])

        units.append(unit_obj)

    course_data = {
        "id": "chemical-spectroscopy",
        "courseCode": "",
        "title": "Chemical Spectroscopy",
        "subtitle": "Principles of EM Interaction, Microwave Rotations, Rovibrational & Raman, Atomic & Molecular Electronic Transitions, Multi-Dimensional NMR, ESR, and Mössbauer Spectroscopy",
        "department": "Chemistry",
        "institution": "OpenSTEM Global Academic Press",
        "level": "Advanced Undergraduate / Graduate Honors",
        "author": "Department of Chemistry, OpenSTEM Press",
        "description": "Comprehensive university honors master digital textbook on Chemical Spectroscopy: quantum electrodynamic foundations of radiation-matter interaction, transition dipole moments, Einstein A & B coefficients, spectral linewidths, Doppler broadening, practical signal-to-noise optimization, Fourier transform spectroscopy, and resolution metrics; pure rotational microwave spectroscopy of linear, symmetric, asymmetric, and spherical rotors, centrifugal distortion, Stark splitting, and quadrupole hyperfine coupling; rovibrational spectroscopy of diatomic and polyatomic molecules, harmonic vs Morse oscillators, Dunham expansion, vibration-rotation P/Q/R branches, Coriolis coupling, and Fermi resonances; classical and quantum theory of Raman scattering, polarizability ellipsoids, Kramers-Heisenberg-Dirac dispersion, Stokes/anti-Stokes transitions, depolarization ratios, resonance Raman, SERS, and TERS; electronic spectroscopy of atoms, Russell-Saunders and jj coupling, atomic term symbols, Hund's rules, spin-orbit splitting, normal and anomalous Zeeman effects, and Stark splitting; molecular electronic spectroscopy, Born-Oppenheimer approximation, Franck-Condon principle, vibronic progressions, charge-transfer bands, d-d ligand field transitions, and Tanabe-Sugano diagrams; photophysics, Jablonski diagrams, radiative and non-radiative decay kinetics, fluorescence quenching, Stern-Volmer dynamics, intersystem crossing, phosphorescence, and Förster resonance energy transfer (FRET); nuclear magnetic resonance (NMR) spectroscopy, nuclear Zeeman Hamiltonian, Larmor precession, chemical shifts, diamagnetic and paramagnetic shielding, Bloch equations, spin-lattice (T1) and spin-spin (T2) relaxation, scalar J-coupling, and dynamic NMR line shape exchange; multi-dimensional and solid-state NMR, product operator formalism, 2D COSY, TOCSY, NOESY, HSQC, HMBC, and magic angle spinning (MAS); electron spin resonance (ESR/EPR) and Mössbauer spectroscopy, electron Zeeman interaction, isotropic and anisotropic hyperfine coupling, Kramers theorem, zero-field splitting, nuclear recoil-free gamma-ray resonance, isomer shifts, quadrupole splitting, and magnetic hyperfine sextets. Features 10 interactive 60 FPS Canvas simulations and 90 tiered solved examination problems with complete unskipped mathematical and quantum derivations.",
        "units": units
    }

    return course_data

def audit_banned_tokens(text):
    banned_patterns = [
        r'\bchem\s*\d+',
        r'70\s*\+\s*20\s*\+\s*10',
        r'35\s*\+\s*10\s*\+\s*5',
        r'\b\d+\s*Marks\b',
        r'100\s*Marks',
        r'70\s*Marks',
        r'50\s*Marks',
        r'exam(ination)?\s+marks',
        r'\bgrades?\s*=\s*\d+'
    ]
    violations = []
    for pat in banned_patterns:
        matches = re.findall(pat, text, re.IGNORECASE)
        if matches:
            violations.append((pat, matches[:5]))
    return violations

if __name__ == "__main__":
    course_data = build_full_data()

    # Calculate statistics
    total_words = 0
    total_sections = 0
    total_problems = 0

    desc_words = len(course_data["title"].split()) + len(course_data["description"].split())
    total_words += desc_words

    for u in course_data["units"]:
        u_words = len(u["title"].split()) + len(u["leadSummary"].split())
        total_sections += len(u["sections"])
        total_problems += len(u["problems"])
        for s in u["sections"]:
            u_words += len(s["title"].split()) + len(s["content"].split())
        for p in u["problems"]:
            u_words += len(p["title"].split()) + len(p["statement"].split()) + len(p["solution"].split())
        total_words += u_words

    print("=" * 60)
    print("CHEMICAL SPECTROSCOPY DATA ASSEMBLY AUDIT")
    print("=" * 60)
    print(f"Total Units:    {len(course_data['units'])}")
    print(f"Total Sections: {total_sections} (Required: 80)")
    print(f"Total Problems: {total_problems} (Required: 90)")
    print(f"Total Words:    {total_words} (Target: >55,000)")
    print("=" * 60)

    # Convert to JSON
    json_str = json.dumps(course_data, indent=2, ensure_ascii=False)

    # Run banned token audit
    violations = audit_banned_tokens(json_str)
    if violations:
        print("CRITICAL AUDIT ERROR: Banned tokens found!")
        for pat, matches in violations:
            print(f"Pattern {pat}: {matches}")
        raise ValueError("Banned tokens detected in assembled data!")
    else:
        print("✓ BANNED TOKEN AUDIT PASSED: Zero prohibited tokens found.")

    # Write chemical-spectroscopy-data.js
    out_file = "chemical-spectroscopy-data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Chemical Spectroscopy - Master Course Data\n")
        f.write("// OpenSTEM Global Academic Press - Master Honors Digital Textbook\n")
        f.write("window.COURSE_DATA = ")
        f.write(json_str)
        f.write(";\n")

    print(f"✓ Successfully wrote {out_file} ({len(json_str)} bytes)")
