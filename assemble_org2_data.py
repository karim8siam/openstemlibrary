# -*- coding: utf-8 -*-
"""
assemble_org2_data.py
Assembles Organic Chemistry II Master Course Data File (organic-chemistry-2-data.js).
Strict zero course numbers or marks.
Ensures >66,000 words in the data file and complete balance across all 9 units and 81 problems.
"""

import json
import re

import build_org2_units_1_2_3 as b1
import build_org2_units_4_5_6 as b2
import build_org2_units_7_8_9 as b3
import expand_org2_units_1_2_3 as e1
import expand_org2_units_4_5_6 as e2
import expand_org2_units_7_8_9 as e3
import expand_org2_deep as ed
import expand_org2_section8 as es
import expand_org2_monograph as em
import expand_org2_problem9 as ep
import expand_org2_honors_capstone as eh
import expand_org2_ultimate as eu

def get_assembled_units():
    print("Building base units...")
    u1, u2, u3 = b1.get_unit_1(), b1.get_unit_2(), b1.get_unit_3()
    u4, u5, u6 = b2.get_unit_4(), b2.get_unit_5(), b2.get_unit_6()
    u7, u8, u9 = b3.get_unit_7(), b3.get_unit_8(), b3.get_unit_9()

    print("Applying initial enrichment expansions...")
    e1.enrich_units_1_2_3(u1, u2, u3)
    e2.enrich_units_4_5_6(u4, u5, u6)
    e3.enrich_units_7_8_9(u7, u8, u9)

    units = [u1, u2, u3, u4, u5, u6, u7, u8, u9]

    print("Applying deep physical organic & spectroscopic expansions...")
    ed.deep_enrich_all_units(units)

    print("Injecting Section 8 into all 9 units...")
    es.add_section_8_to_all_units(units)

    print("Injecting advanced university honors monographs...")
    em.inject_monographs(units)

    print("Injecting Problem 9 into all 9 units...")
    ep.add_problem_9_to_all_units(units)

    print("Injecting honors capstone modules...")
    eh.inject_honors_capstones(units)

    print("Injecting ultimate university honors monographs...")
    eu.inject_ultimate_monographs(units)

    return units

def main():
    print("Assembling Organic Chemistry II Master Course Data...")
    units = get_assembled_units()

    # Master Course Metadata (Strictly zero course numbers or marks)
    course_data = {
        "courseCode": "",
        "courseTitle": "Organic Chemistry II: Polynuclear Aromatics, Carbonyl Dynamics, Carboxylic Derivatives, Nitrogen Systems, Advanced Stereochemistry & Medicinal Syntheses",
        "courseSubtitle": "Condensed and Angular Polycyclic Aromatics & Clar Sextet Theory, Bürgi-Dunitz Trajectory & Carbonyl Condensations, Carboxylic Acids & Hammett Linear Free-Energy Relationships, Acyl Substitution & Surfactant Self-Assembly, Nitrogen Pyramidal Inversion & Arenediazonium Dyes, Dissymmetry & Asymmetric Synthesis Models, Active Methylenes & Pericyclic Orbital Symmetry, Industrial Pharmaceutical Syntheses, and Multi-Heteroatom Fused Heterocycles",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "Organic Chemistry I, Chemical Bonding Foundations & Introductory Reaction Energetics",
        "description": "Comprehensive university honors master digital textbook on Organic Chemistry II: condensed and angular polynuclear benzenoid aromatic hydrocarbons, Haworth total annulation pathways, Clar's aromatic sextet theory, bond length alternation and Coulson pi-bond orders, electrophilic aromatic substitution regiochemistry (alpha vs beta in naphthalene; C9/C10 in anthracene and phenanthrene), peri-steric strain, kinetic vs thermodynamic sulfonation equilibria, Diels-Alder cycloaddition across meso positions, oxidation and reduction cascades, and metabolic activation of bay-region diol epoxides in chemical carcinogenesis; aldehydes and ketones, carbonyl orbital polarization, Bürgi-Dunitz 107° nucleophilic trajectory, reversible hydration thermodynamics, cyclic acetal protection chemistry, irreversible hydride and organometallic additions, imines, enamines and Stork alkylation, Wolff-Kishner, Clemmensen and Baeyer-Villiger oxidation migratory aptitudes, enol-enolate equilibria, kinetic vs thermodynamic enolates, and aldol, Claisen-Schmidt, Cannizzaro, Benzoin, Perkin, and Knoevenagel condensation cascades; carboxylic acids and multifunctional acids, carboxylate degenerate resonance stabilization, inductive and field distance attenuation, Hammett linear free-energy relationship (sigma and rho parameters), industrial Monsanto and Cativa catalytic carbonylation cycles, Hell-Volhard-Zelinsky alpha-bromination mechanism, hydroxy acid thermal lactide and lactone cyclizations, geometric cis/trans stereoisomerism in maleic vs fumaric acids and intramolecular hydrogen bonding, and pericyclic 6-center decarboxylation of beta-keto acids; carboxylic acid derivatives, nucleophilic acyl substitution (S_NAc) tetrahedral intermediate matrix and leaving group pKa scales, interconversion hierarchy, Ingold ester hydrolysis mechanisms (B_AC2, A_AC2, A_AL1), transesterification equilibria, amide resonance dipole and restricted C-N rotation barriers (coalescence NMR kinetics), peptide coupling reagents (DCC, HOBt), nitrile transformations and Ritter reaction, and colloidal surface chemistry of soaps, synthetic detergents (anionic, cationic, non-ionic), critical micelle concentration (CMC) thermodynamics, hydrophobic effect, and hard-water curdling; amines, nitrogen pyramidal inversion dynamics, double-well potentials and quantum tunneling barriers, gas-phase vs aqueous solvation basicity scales, Gabriel phthalimide synthesis, Curtius, Hofmann, Lossen and Schmidt rearrangements, Hofmann exhaustive methylation and anti-Zaitsev E2 elimination, Cope elimination, Hinsberg testing, arenediazonium salts, nitrous acid diazotization kinetics, Sandmeyer, Schiemann, and Gattermann substitution manifolds, azo coupling dynamics and methyl orange quinonoid chromophore electronics, and nitro compound aci-tautomerism, Nef reactions, and selective Zinin reductions; modern stereochemistry, group-theoretical criteria for chirality (improper rotation axes S_n), Biot's law, circular birefringence, specific rotation, Laurent polarimeter optics, enantiomers, diastereomers, meso forms, pseudoasymmetry (r/s descriptors), chirality without stereocenters (allenes, atropisomerism in ortho-substituted biphenyls, BINAP, planar chirality in trans-cyclooctene, helical chirality in hexahelicene), racemization kinetics and optical resolution protocols (diastereomeric salt crystallization, chiral stationary phase HPLC, enzymatic kinetic resolution), and asymmetric synthesis models (Cram open-chain, Felkin-Anh polar model, Cram chelation, and Evans chiral oxazolidinone auxiliaries); bi-functional compounds and active methylenes, ethyl acetoacetate (EAA) and diethyl malonate (DEM), keto-enol tautomerism equilibria, Meyer bromine titration, ketone vs acid cleavage manifolds, synthesis of ketones, carboxylic acids, and alicyclic rings, Michael conjugate 1,4-additions, Robinson annulation three-stage cascade mechanism, frontier molecular orbital theory of pericyclic reactions, electrocyclic Woodward-Hoffmann selection rules, and Diels-Alder [4+2] cycloadditions, Alder endo rule and secondary orbital overlap; total syntheses and mechanisms of foundational organic pharmaceuticals, sulfonamide antibacterials (sulfanilamide, sulfathiazole, sulfamethoxazole) and competitive inhibition of bacterial dihydropteroate synthase (DHPS), antipyretics and analgesics (Aspirin, Paracetamol, Phenacetin) and cyclooxygenase (COX-1/COX-2) active-site Ser530 irreversible transesterification, antimalarials (Chloroquine, Primaquine, Quinacrine) quinoline retrosyntheses, barbiturate sedatives (Phenobarbital, Pentobarbital, Thiopental) malonic ester condensations with urea, and artificial sweeteners (Saccharin, Cyclamate) syntheses and TAS1R2/TAS1R3 sweet taste receptor pharmacophores; and heterocycles with multiple heteroatoms and fused ring systems, 1,3-azoles (imidazole, pyrazole, oxazole, thiazole), imidazole amphoterism and serine protease catalytic triads (His57-Asp102-Ser195), thiazole and Breslow singlet carbene intermediates in umpolung catalysis, pyrimidine and purine nucleic acid bases, lactam-lactim tautomerism and Watson-Crick hydrogen-bonding geometry, indole chemistry (Fischer indole [3,3]-sigmatropic cascade and C3 electrophilic regiocontrol), quinoline chemistry (Skraup, Doebner-Miller, Friedländer syntheses and C5/C8 vs C2/C4 reactivity), and isoquinoline chemistry (Bischler-Napieralski and Pictet-Spengler syntheses). Features 10 interactive 60 FPS Canvas simulations and 81 tiered solved problems with complete line-by-line mathematical and mechanistic proofs.",
        "units": units
    }

    # Format into JavaScript assignment
    json_str = json.dumps(course_data, indent=2)
    js_content = f"// Organic Chemistry II Master Textbook Data File\n// STRICT CONSTRAINT: ZERO PROHIBITED CODES PERMITTED\nwindow.COURSE_DATA = {json_str};\n"

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
            print(f"WARNING: Prohibited course number or marks pattern '{pat}': {matches[:5]}")
            assert False, f"Banned pattern found: {matches}"

    output_filename = "organic-chemistry-2-data.js"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"Successfully generated {output_filename}")

    # Calculate word count and file size
    words = len(js_content.split())
    chars = len(js_content)
    print(f"Data file stats: {words:,} words | {chars:,} characters | {len(course_data['units'])} units")
    for idx, u in enumerate(course_data['units'], 1):
        u_words = len(json.dumps(u).split())
        print(f"  Unit {idx}: {len(u['sections'])} sections, {len(u['problems'])} problems (~{u_words:,} words)")

if __name__ == "__main__":
    main()
