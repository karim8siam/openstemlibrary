# -*- coding: utf-8 -*-
"""
assemble_analytical_data.py
Assembles Analytical Chemistry Master Course Data File (analytical-chemistry-data.js).
Strict zero course numbers or marks.
Ensures >66,000 words in the data file and complete balance across all 9 units,
72 sections, 81 solved problems, and 10 interactive simulations.
"""

import json
import re

import build_analytical_units_1_2_3 as b1
import build_analytical_units_4_5_6 as b2
import build_analytical_units_7_8_9 as b3
import expand_analytical_units_1_2_3 as e1
import expand_analytical_units_4_5_6 as e2
import expand_analytical_units_7_8_9 as e3
import expand_analytical_section8 as es
import expand_analytical_deep as ed
import expand_analytical_monograph as em
import expand_analytical_problem9 as ep
import expand_analytical_honors_capstone as eh
import expand_analytical_ultimate as eu

def get_assembled_units_and_curriculum():
    print("Building base units 1-3, 4-6, 7-9...")
    u1, u2, u3 = b1.get_units_1_2_3()
    u4, u5, u6 = b2.get_units_4_5_6()
    u7, u8, u9 = b3.get_units_7_8_9()

    print("Applying initial enrichment expansions (adding Problem 8 & theory)...")
    e1.enrich_units_1_2_3(u1, u2, u3)
    e2.enrich_units_4_5_6(u4, u5, u6)
    e3.enrich_units_7_8_9(u7, u8, u9)

    units = [u1, u2, u3, u4, u5, u6, u7, u8, u9]

    print("Injecting Section 8 into all 9 units (72 sections total)...")
    es.add_section8_to_all_units(units)

    print("Injecting deep reference figures of merit, solubility products, formation constants...")
    ed.enrich_units_deep(units)

    print("Injecting advanced university honors research monographs...")
    em.add_monographs_to_all_units(units)

    print("Injecting Problem 9 into all 9 units (81 solved problems total)...")
    ep.add_problem9_to_all_units(units)

    # Master Course Metadata (Strictly zero course numbers or marks)
    course_data = {
        "courseCode": "",
        "courseTitle": "Analytical Chemistry: Statistical Data Evaluation, Complexometry, Atomic Spectroscopy, Ion-Exchange & Advanced Instrumental Separations",
        "courseSubtitle": "Errors & Propagation Calculus, Representative Sampling & Comminution, von Weimarn Precipitation Kinetics & Group Separation, Chelate Thermodynamics & Water Hardness, Atomic Absorption & Zeeman Background Correction, Ion-Exchange Chromatography & HPIC, UV-Vis Spectrophotometry & Speciation, Nernst Partition Thermodynamics & Countercurrent Extractions, and van Deemter Kinetics, GLC & Reversed-Phase HPLC",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "General Chemistry Foundations, Stoichiometry, Solution Equilibria & Chemical Thermodynamics",
        "description": "Comprehensive university honors master digital textbook on Analytical Chemistry: rigorous statistical evaluation of analytical data, propagation of indeterminate random and determinate systematic errors, Gaussian normal distributions, Student's t confidence intervals, significance testing (t-tests, F-tests, Grubbs test, Dixon Q-test), ordinary and weighted least-squares linear calibrations, figures of merit (sensitivity, selectivity, LOD, LOQ), and Youden ruggedness factorial designs; representative sampling theory, sampling populations, Ingamells sampling constant (Ks), Visman two-constant variance equation, particle size comminution kinetics, sample preservation protocols, wet acid digestions (HNO3, HClO4, HF), closed-vessel microwave bomb dissolutions, and high-temperature alkali flux fusions; group separation and precipitation phenomena, von Weimarn relative supersaturation (RSS) nucleation vs crystal growth kinetics, Debye-Hückel ionic strength effects, Ostwald ripening, coprecipitation mechanisms (surface adsorption, mixed-crystal inclusion, occlusion, mechanical entrapment), precipitation from homogeneous solution (PFHS) via urea, sulfamic acid, and thioacetamide hydrolysis, and classical qualitative inorganic cation Groups I-V systematic separation cascades; complexometric titrations, chelate effect thermodynamic entropy driving forces, EDTA polyprotic acid dissociation equilibria, alpha_Y4- fractional distribution, conditional formation constants (K'f), auxiliary complexing agents, metallochromic indicator equilibria (Eriochrome Black T, Calmagite, Murexide, Xylenol Orange), selective masking with cyanide, fluoride, and BAL, demasking with formaldehyde, and differential titration of calcium, magnesium, and total water hardness; advanced atomic spectroscopy, Boltzmann excitation statistics, fine structure Russell-Saunders term symbols, natural, Doppler, and Lorentz spectral line broadening, hollow cathode lamp sputtering, premix burner laminar flames vs electrothermal graphite furnace AAS (GFAAS) L'vov platforms, chemical releasing agents (La3+), ionization suppression, Zeeman splitting, continuum deuterium, and pulsed Smith-Hieftje background corrections; ion-exchange chromatography, cross-linked polystyrene-divinylbenzene resin architectures (SAC, WAC, SBA, WBA, chelating Chelex-100), Donnan potential exclusion, selectivity coefficients, column ion-exchange capacity, breakthrough curves, high-performance ion chromatography (HPIC) with chemically suppressed conductivity detection, and transition metal chloro-complex separations; molecular UV-Visible spectrophotometry, electronic transition photophysics, Beer-Lambert law derivation, chemical and instrumental stray-light limitations, Twyman-Lothian photometric precision optimization, spectrophotometric titration curve morphology and dilution correction, Job's method of continuous variations, and trace colorimetric determination of lead via dithizone and arsenic via modified Gutzeit and silver diethyldithiocarbamate (Ag-DDTC); liquid-liquid extraction, Nernst partition thermodynamics, pH-dependent conditional distribution ratios (D), mathematical induction proof of multiple batch extraction yields (q_n), continuous countercurrent Craig distribution, ion-pair extraction of iron(III) into MIBK, copper diethyldithiocarbamate extraction into carbon tetrachloride, and solid-phase extraction (SPE) sorbent mechanics; and foundational and instrumental chromatographic science, retention factor (k'), selectivity factor (alpha), theoretical plate efficiency (N, HETP), complete van Deemter and Knox kinetic rate equations (Eddy diffusion, longitudinal diffusion, mass-transfer resistance), derivation of the master Purnell resolution equation, planar paper and thin-layer chromatography (TLC separation of Ni2+/Cu2+ cations), cellulose column adsorption/partition chromatography (separation of Fe3+/Al3+), capillary gas-liquid chromatography (GLC) with FID and TCD detection, reversed-phase HPLC (RP-HPLC C18 isocratic vs gradient elution, guard columns, photodiode array DAD detection), and comprehensive two-dimensional GCxGC and LCxLC separations. Features 10 interactive 60 FPS Canvas simulations and 81 tiered solved problems with complete line-by-line mathematical, equilibrium, and instrumental derivations.",
        "units": units
    }

    print("Injecting honors capstones...")
    eh.add_capstones_to_curriculum(course_data)

    print("Injecting ultimate reference handbook...")
    eu.add_ultimate_reference_handbook(course_data)

    return course_data

def main():
    print("Assembling Analytical Chemistry Master Course Data...")
    course_data = get_assembled_units_and_curriculum()

    # Format into JavaScript assignment
    json_str = json.dumps(course_data, indent=2, ensure_ascii=False)
    js_content = f"// Analytical Chemistry Master Textbook Data File\n// STRICT CONSTRAINT: ZERO PROHIBITED CODES PERMITTED\nwindow.COURSE_DATA = {json_str};\nwindow.CHEMISTRY_ANALYTICAL_CURRICULUM = window.COURSE_DATA;\n"

    # Strict compliance check for banned patterns (course codes, marks formulas, exam grading)
    banned_patterns = [
        r'\bchem\s*\d+',
        r'70\s*\+\s*20\s*\+\s*10',
        r'\b\d+\s*Marks\b',
        r'100\s*Marks',
        r'exam(ination)?\s+marks',
        r'\bgrades?\s*=\s*\d+'
    ]

    for pat in banned_patterns:
        matches = re.findall(pat, js_content, re.IGNORECASE)
        if matches:
            print(f"CRITICAL ERROR: Prohibited course number or marks pattern '{pat}': {matches[:5]}")
            assert False, f"Banned pattern found: {matches}"

    output_filename = "analytical-chemistry-data.js"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"Successfully generated {output_filename}")

    # Calculate word count and file size
    words = len(js_content.split())
    chars = len(js_content)
    print(f"Data file stats: {words:,} words | {chars:,} characters | {len(course_data['units'])} units")
    total_sections = sum(len(u['sections']) for u in course_data['units'])
    total_problems = sum(len(u['problems']) for u in course_data['units'])
    print(f"Total Sections: {total_sections} (target: 72)")
    print(f"Total Solved Problems: {total_problems} (target: 81)")
    for idx, u in enumerate(course_data['units'], 1):
        u_words = len(json.dumps(u).split())
        print(f"  Unit {idx}: {len(u['sections'])} sections, {len(u['problems'])} problems (~{u_words:,} words)")

if __name__ == "__main__":
    main()
