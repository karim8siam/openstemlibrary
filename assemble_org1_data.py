import json
import re
from build_org1_units_1_2 import get_unit_1, get_unit_2
from build_org1_units_3_4 import get_unit_3, get_unit_4
from build_org1_units_5_6 import get_unit_5, get_unit_6
from build_org1_units_7_8 import get_unit_7, get_unit_8

def main():
    print("Assembling Organic Chemistry I Master Course Data...")
    
    u1 = get_unit_1()
    u2 = get_unit_2()
    u3 = get_unit_3()
    u4 = get_unit_4()
    u5 = get_unit_5()
    u6 = get_unit_6()
    u7 = get_unit_7()
    u8 = get_unit_8()

    course_data = {
        "courseCode": "",
        "courseTitle": "Organic Chemistry I: Molecular Architecture, Hydrocarbons, Haloalkanes, Oxygen/Sulfur Systems & Fundamental Heterocycles",
        "courseSubtitle": "Quantum Electronic Structure of Carbon, Hybridization & Coulson's Theorem, Alkane & Cycloalkane Conformational Dynamics, Alkene Stereospecific Additions & Criegee Cleavages, Conjugated Dienes & Diels-Alder FMO Theory, Aromaticity & Wheland EAS Regiochemistry, Nucleophilic Substitutions & Eliminations, Oxygen/Sulfur Functionalities, and Fundamental Heteroaromatics",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "General Chemistry, Chemical Bonding Foundations & Introductory Reaction Energetics",
        "description": "Comprehensive university honors master digital textbook on Organic Chemistry I: quantum electronic configuration of carbon, valence bond hybridization, Coulson's theorem, molecular orbital theory of sigma and pi bonds, bond polarization, electric dipole moments, resonance delocalization, and curved-arrow formalisms; alkanes and cycloalkanes, constitutional isomerism, combustion thermodynamics, octane ratings, free-radical halogenation energetics, Hammond's postulate, carbene insertions, Baeyer angle strain theory, cyclohexane chair conformational equilibria, Winstein-Holness A-values, 1,3-diaxial interactions, bicycloalkanes, Bredt's rule, and Wurtz coupling; alkenes, index of hydrogen deficiency, Cahn-Ingold-Prelog E/Z priority rules, E2 and E1 elimination mechanisms, Zaitsev and Hofmann regioselectivity, electrophilic additions, Markovnikov's rule, carbocation rearrangements, stereospecific anti-bromination via cyclic bromonium ions, hydration protocols (acid-catalyzed, oxymercuration-demercuration, hydroboration-oxidation), Criegee ozonolysis mechanism, peracid epoxidation, syn-dihydroxylation, and coordination polymerization; conjugated dienes, 1,2- vs 1,4-additions under kinetic vs thermodynamic control, frontier molecular orbital theory, Diels-Alder [4+2] cycloaddition, Alder endo rule, secondary orbital overlap, diene elastomers, alkynes, sp hybridization acidity, acetylide alkylations, keto-enol tautomerism, and stereoselective reductions (Lindlar vs dissolving metal); benzene structure, resonance stabilization energy, Hückel (4n+2) pi-electron rule, Frost circle polygon mnemonics, annulenes, aromatic ions, non-benzenoid aromatics, electrophilic aromatic substitution, Wheland arenium sigma-complex intermediates, halogenation, nitration, sulfonation, Friedel-Crafts alkylation and acylation, substituent directing and activating effects, and Hammett linear free-energy relationships; alkyl and aryl halides, leaving group ability, SN2 bimolecular kinetics, Walden inversion, SN1 unimolecular solvolysis, ion pairs, E2 anti-periplanar elimination, E1 and E1cB mechanisms, competitive reaction decision matrices, SNAr addition-elimination via Meisenheimer complexes, elimination-addition via benzyne intermediates, and Grignard organometallic reagents; alcohols, phenols, ethers, epoxides, and sulfides, hydrogen bonding, acid-base amphoterism, phenol resonance stabilization, conversion to halides via SNi, oxidation levels, Pinacol-Pinacolone rearrangements, Malaprade periodate glycol cleavage, Kolbe-Schmitt carboxylation, Reimer-Tiemann formylation, Bakelite polymers, Williamson ether synthesis, crown ether supramolecular cation complexation, and acidic vs basic epoxide ring opening regiochemistry; and fundamental heterocycles, heteroaromaticity criteria, pi-excessive vs pi-deficient classifications, Paal-Knorr syntheses, pyrrole, furan, and thiophene electronic structures and C2 vs C3 EAS regioselectivity, pyridine electronic structure and basicity, extreme electrophilic deactivation, nucleophilic Chichibabin amination, and pyridine N-oxide synthetic activation. Features 8 interactive 60 FPS Canvas simulations and 32 tiered solved problems with complete line-by-line mathematical and mechanistic proofs.",
        "units": [u1, u2, u3, u4, u5, u6, u7, u8]
    }

    # Format into JavaScript assignment
    json_str = json.dumps(course_data, indent=2)
    js_content = f"// Organic Chemistry I Master Textbook Data File\n// STRICT CONSTRAINT: ZERO PROHIBITED CODES PERMITTED\nwindow.COURSE_DATA = {json_str};\n"

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

    output_filename = "organic-chemistry-1-data.js"
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
