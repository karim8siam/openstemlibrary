#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
assemble_natural_products_data.py
Assembles the complete master course data for Chemistry of Natural Products into
natural-products-chemistry-data.js.
Strictly zero course numbers, codes, credit formulas, or examination marks.
Ensures sections[0]["simulations"] is populated for every unit so app.js mounts simulations.
Performs an automated regex audit against all prohibited tokens.
"""

import json
import re
import os

from build_natural_products_units_1_2_3 import get_units_1_2_3
from build_natural_products_units_4_5_6 import get_units_4_5_6
from build_natural_products_units_7_8_9_10 import get_units_7_8_9_10
from expand_natural_products_section8 import add_section8_to_units
from expand_natural_products_problem8 import add_problem8_to_units
from expand_natural_products_problem9 import add_problem9_to_units
from expand_natural_products_deep import enrich_deep_content
from expand_natural_products_monograph import enrich_monograph_content

def build_full_dataset():
    # 1. Gather all units (7 sections and 7 problems each)
    units = get_units_1_2_3() + get_units_4_5_6() + get_units_7_8_9_10()
    assert len(units) == 10, f"Expected 10 units, got {len(units)}"

    # 2. Append Section 8 (total 8 sections per unit = 80 sections)
    add_section8_to_units(units)

    # 3. Append Problem 8 (total 8 problems per unit = 80 problems)
    add_problem8_to_units(units)

    # 4. Append Problem 9 (total 9 problems per unit = 90 problems)
    add_problem9_to_units(units)

    # 5. Apply Deep Chemical Enrichments (tables, metrics, reaction mechanisms)
    enrich_deep_content(units)

    # 6. Apply Research Monographs and Modern Case Studies
    enrich_monograph_content(units)

    # 7. CRITICAL: Mount simulations on sections[0] of each unit for app.js
    for u in units:
        assert len(u["sections"]) == 8, f"Unit {u['id']} has {len(u['sections'])} sections, expected 8"
        assert len(u["problems"]) == 9, f"Unit {u['id']} has {len(u['problems'])} problems, expected 9"
        if "simulations" in u and u["simulations"]:
            u["sections"][0]["simulations"] = list(u["simulations"])

    course_data = {
        "id": "natural-products-chemistry",
        "courseCode": "",  # STRICT REQUIREMENT: No course numbers or codes
        "title": "Chemistry of Natural Products",
        "subtitle": "Biosynthetic Pathways, Terpenoid Cyclizations, Carbohydrate Stereochemistry, Peptide SPPS, Nucleic Acids, Alkaloid Degradations, Steroid Architecture & Modern Antibiotics",
        "department": "Chemistry",
        "institution": "OpenSTEM Global Academic Press",
        "level": "Advanced Undergraduate / Graduate Honors",
        "author": "Department of Chemistry, OpenSTEM Press",
        "description": "Comprehensive university honors master digital textbook on Chemistry of Natural Products: primary vs specialized secondary metabolites, ecological defense functions, extraction thermodynamics (solvent fractionation, steam codistillation, supercritical fluid CO2), and fundamental biosynthetic fluxes (Mevalonic Acid, MEP/DOXP, Shikimic Acid, and Modular Type I/II Polyketide Synthase pathways); terpenoids, isoprene rules, structural elucidations and total syntheses of acyclic (myrcene, citral) and monocyclic (limonene) monoterpenes; sesquiterpenes (farnesol, cadinene, caryophyllene), Stork-Eschenmoser polyene cyclization hypotheses, and Wagner-Meerwein carbocation rearrangements in terpene cyclases; carbohydrates, Emil Fischer's configuration proof of D-(+)-glucose, Kiliani-Fischer chain extensions, Wohl/Ruff degradations, mutarotation dynamics, chair conformational energetics (4C1 vs 1C4), stereoelectronic anomeric effects, and osazone mechanisms; complex disaccharides and polysaccharides, sucrose structure proof and cane sugar inversion polarimetric kinetics, maltose/cellobiose enzymatic selectivity, amylose helical iodine clathrates, amylopectin branch points, and crystalline cellulose microfibrils; amino acids, peptides, and proteins, Strecker and acetamidomalonate syntheses, zwitterionic speciation and pI calculus, peptide bond planarity, Ramachandran dihedral landscapes, Merrifield solid-phase peptide synthesis (SPPS), Edman degradation, mass spectrometry CID sequencing, and folding thermodynamics; purines, pyrimidines, and nucleic acids, Traube adenine/guanine syntheses, uric acid degradations (alloxan, allantoin), beta-N-glycosidic bond conformations, Watson-Crick B-DNA geometry, hyperchromic effect and cooperative melting Tm calculus, ribozymes, and phosphoramidite oligonucleotide synthesis; alkaloids, extraction, Hofmann exhaustive methylation ring cleavage, Emde reductions, von Braun reactions, zinc dust distillations, and complete structures of ephedrine, atropine (Robinson's biomimetic tropinone synthesis), and morphine; lipids and steroids, fatty acid unsaturation, saponification and iodine value analytics, lipoproteins (LDL/HDL), the cyclopentanoperhydrophenanthrene (CPPP) sterane skeleton, dehydrogenation to Diels' hydrocarbon, functional groups and angular methyls of cholesterol (Barbier-Wieland degradation, Blanc's rule), and cardiotonic glycosides; and antibiotics, 6-APA core, strained beta-lactam reactivity, acid/alkaline degradations, transpeptidase suicide inhibition, beta-lactamase resistance and clavulanate inactivation, and the complete stereochemical elucidation and total synthesis of chloramphenicol. Features 10 interactive 60 FPS Canvas simulations and 90 tiered solved examination problems with complete unskipped mathematical and mechanistic derivations.",
        "units": units
    }

    return course_data

def main():
    course_data = build_full_dataset()
    json_str = json.dumps(course_data, indent=2, ensure_ascii=False)
    js_content = f"// Chemistry of Natural Products - Master Course Data\n// OpenSTEM Global Academic Press - Master Honors Digital Textbook\nwindow.COURSE_DATA = {json_str};\n"

    # Strict Regex Audit for Prohibited Terms
    banned_patterns = [
        (r'\bchem\s*\d+', "Course number like Chem 401"),
        (r'70\s*\+\s*20\s*\+\s*10', "Credit/mark breakdown 70+20+10"),
        (r'35\s*\+\s*10\s*\+\s*5', "Credit/mark breakdown 35+10+5"),
        (r'\b\d+\s*Marks\b', "Mark values like 100 Marks"),
        (r'100\s*Marks', "100 Marks"),
        (r'70\s*Marks', "70 Marks"),
        (r'50\s*Marks', "50 Marks"),
        (r'exam(ination)?\s+marks', "Examination marks"),
        (r'\bgrades?\s*=\s*\d+', "Grade values")
    ]

    for pat, desc in banned_patterns:
        matches = re.findall(pat, js_content, flags=re.IGNORECASE)
        if matches:
            raise ValueError(f"PROHIBITED CONTENT FOUND! Pattern '{desc}' matched: {matches[:5]}")

    target_file = "natural-products-chemistry-data.js"
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(js_content)

    file_size_kb = os.path.getsize(target_file) / 1024
    total_words = len(js_content.split())
    print(f"Successfully assembled {target_file}!")
    print(f"  File size: {file_size_kb:.1f} KB")
    print(f"  Total words: {total_words:,}")
    print(f"  Total units: {len(course_data['units'])}")
    total_sections = sum(len(u['sections']) for u in course_data['units'])
    total_problems = sum(len(u['problems']) for u in course_data['units'])
    print(f"  Total sections: {total_sections}")
    print(f"  Total problems: {total_problems}")
    print(f"  Banned regex audit: PASSED (0 prohibited tokens)")

if __name__ == "__main__":
    main()
