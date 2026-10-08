#!/usr/bin/env python3
"""
generate_inorg1_data.py
Assembles inorganic-chemistry-1-data.js from Units 1 through 8.
STRICT CONSTRAINT: ZERO COURSE NUMBERS OR CODES ANYWHERE.
"""

import json
import build_inorg1_unit1
import build_inorg1_unit2
import build_inorg1_unit3
import build_inorg1_unit4
import build_inorg1_unit5
import build_inorg1_unit6
import build_inorg1_unit7
import build_inorg1_unit8

def main():
    u1 = build_inorg1_unit1.get_unit1()
    u2 = build_inorg1_unit2.get_unit2()
    u3 = build_inorg1_unit3.get_unit3()
    u4 = build_inorg1_unit4.get_unit4()
    u5 = build_inorg1_unit5.get_unit5()
    u6 = build_inorg1_unit6.get_unit6()
    u7 = build_inorg1_unit7.get_unit7()
    u8 = build_inorg1_unit8.get_unit8()

    raw_units = [u1, u2, u3, u4, u5, u6, u7, u8]

    unit_meta = [
        {
            "id": "unit1",
            "unitId": "unit1-inorg1",
            "number": 1,
            "unitNumber": 1,
            "title": "Unit 1: Quantum Theory of the Atom, Wave Mechanics & Electronic Architecture",
            "description": "Rigorous quantum foundations of atomic structure and electronic configuration: photonic quantization of electromagnetic radiation, classical Rutherford $\\alpha$-scattering and instability of orbiting charges, Bohr-Sommerfeld quantization of hydrogenic angular momentum and Rydberg spectral series, de Broglie matter-wave hypothesis and wave-particle duality, Heisenberg indeterminacy relations, time-independent Schrödinger wave equation, mathematical separation of radial $R_{nl}(r)$ and spherical harmonic $Y_l^m(\\theta,\\phi)$ wavefunctions, quantum numbers $(n, l, m_l, m_s)$, boundary probability topologies and nodal surfaces, electron spin and relativistic Dirac spinors, Pauli exclusion principle, Aufbau principle, Hund's rule of maximum multiplicity, and Slater effective nuclear charge with core screening mechanics.",
            "leadSummary": "Rigorous quantum foundations of atomic structure and electronic configuration: photonic quantization of electromagnetic radiation, classical Rutherford scattering, Bohr-Sommerfeld quantization of angular momentum, de Broglie matter-wave hypothesis, Heisenberg uncertainty principle, the Schrödinger wave equation in spherical coordinates, hydrogenic radial and angular distributions, quantum numbers, electron spin, Aufbau principle, Hund's rules, Pauli exclusion principle, and Slater effective nuclear charge.",
            "simId": "sim_chem_bohr_schrodinger_orbitals"
        },
        {
            "id": "unit2",
            "unitId": "unit2-inorg1",
            "number": 2,
            "unitNumber": 2,
            "title": "Unit 2: Periodicity of the Elements, Electronic Shielding & Relativistic Effects",
            "description": "Macroscopic and quantum periodicity across the periodic table: historical evolution from Döbereiner triads and Newlands octaves to Mendeleev's predictions, Henry Moseley's high-frequency X-ray spectroscopy, square-root frequency linearity and the modern periodic law; Slater empirical screening rules versus Clementi-Raimondi self-consistent field wavefunctions; periodic trajectories in covalent, van der Waals, metallic, and crystal ionic radii; first and successive ionization energies with subshell penetration and pairing repulsion anomalies; electron affinities and the anomalous fluorine-chlorine inversion; Pauling, Mulliken, Allred-Rochow, and Allen electronegativity scales; Dirac relativistic mass dilation, direct $s/p_{1/2}$ orbital contraction, indirect $d/f$ orbital expansion, the physical origin of the color of metallic gold and liquidity of mercury, the lanthanide contraction, the inert pair effect in heavy $p$-block elements, and diagonal periodic relationships.",
            "leadSummary": "Macroscopic and quantum periodicity across the periodic table: historical evolution, Moseley's law and X-ray emission spectra, Slater empirical screening rules versus Clementi-Raimondi SCF wavefunctions, periodic trends in radii, ionization energy anomalies, electron affinity inversions, Pauling, Mulliken, and Allred-Rochow electronegativity scales, Dirac relativistic orbital contraction, the lanthanide contraction, the inert pair effect, and diagonal periodic relationships.",
            "simId": "sim_chem_periodic_trends_explorer"
        },
        {
            "id": "unit3",
            "unitId": "unit3-inorg1",
            "number": 3,
            "unitNumber": 3,
            "title": "Unit 3: The Chemical Bond I: Ionic Bonding, Crystal Energetics & Superionic Conductors",
            "description": "Thermodynamics and electrostatic physics of the ionic crystalline state: endothermicity of gas-phase ion pair generation, Hess's law and the Born-Haber thermochemical cycle, endothermic second electron affinities of oxygen and sulfur; electrostatic Coulombic lattice potentials, Madelung constant convergence in 1D alternating chains, Evjen neutral cube summation, Ewald reciprocal-space summation; Born short-range quantum core repulsion, Born-Landé equation derivation, Born-Mayer exponential potential, structure-independent Kapustinskii lattice energy equation; rigid-sphere geometric packing, limiting radius ratio derivations for trigonal, tetrahedral, octahedral, and cubic coordination; Fajan's rules governing anion polarization, cation charge density, and pseudo-noble gas $d^{10}$ cores; stoichiometric point defects (Schottky, Frenkel), non-stoichiometric F-centers, fast-ion superionic conduction in solid-state battery electrolytes ($\\alpha$-AgI), and archetype crystal topologies (perovskite, spinel, rutile, fluorite).",
            "leadSummary": "Thermodynamics and electrostatic physics of the ionic crystalline state: Born-Haber thermochemical cycles, Madelung constants, Evjen neutral cell summation, Born-Landé and Kapustinskii lattice energy equations, limiting radius ratio rules, Fajan's polarization rules, crystal point defects, color centers, fast-ion superionic conduction, and archetype crystal topologies.",
            "simId": "sim_chem_born_haber_lattice_cycle"
        },
        {
            "id": "unit4",
            "unitId": "unit4-inorg1",
            "number": 4,
            "unitNumber": 4,
            "title": "Unit 4: The Chemical Bond II: Covalent Bonding, Hypervalency & Cluster Topologies",
            "description": "Electronic and quantum foundations of covalent bonding: Lewis shared-pair formalism, octet rule, formal charge bookkeeping and charge conservation theorems; hypercoordination and expanded octets, quantum failure of $d$-orbital hybridization models, Pimentel-Rundle three-center four-electron (3c-4e) molecular orbital architectures in $\\text{XeF}_2$ and $\\text{SF}_6$; Pauling resonance theory, canonical contributing structures, variational superposition wavefunctions, resonance stabilization energy, fractional bond orders, and partial atomic charges; homolytic bond cleavage, Morse potential, spectroscopic well depths, zero-point vibrational corrections, mean bond enthalpies, and reaction thermochemistry; bond dipole moments, percent ionic character, Pauling exponential and Hannay-Smith polynomial formulations, vector dipole moments; Natural Bond Orbital (NBO) analysis, hyperconjugation; and Wade's rules for polyhedral skeletal electron pairs in borane clusters.",
            "leadSummary": "Electronic and quantum foundations of covalent bonding: Lewis formalisms, formal charge conservation, Pimentel-Rundle 3c-4e hypervalency models, Pauling resonance theory, fractional bond orders, Morse potential curves, bond dissociation enthalpies, percent ionic character, Natural Bond Orbital (NBO) analysis, and Wade's rules for polyhedral borane clusters.",
            "simId": "sim_chem_vsepr_molecular_geometry"
        },
        {
            "id": "unit5",
            "unitId": "unit5-inorg1",
            "number": 5,
            "unitNumber": 5,
            "title": "Unit 5: Molecular Geometry: VSEPR Theory, Bent's Rule & Symmetry Group Theory",
            "description": "Three-dimensional molecular architecture and mathematical symmetry: Gillespie-Nyholm Valence Shell Electron Pair Repulsion (VSEPR) theory, Pauli exclusion Fermi holes, steric numbers, ideal electron domain polyhedra; Gillespie-Nyholm repulsion hierarchy, distinction between domain geometry and nuclear shape, derived geometries from linear to pentagonal bipyramidal; non-equivalent equatorial vs axial sites in trigonal bipyramids, bond angle contractions; Drago's rule for heavy congeners; Henry Bent's rule of isovalent rehybridization, quantum justification via core penetration, Coulson's theorem linking interorbital angles with fractional $s/p$ character; mathematical group theory, symmetry operations, point group classification algorithms, character tables, the Great Orthogonality Theorem, normal coordinate analysis, and vibrational selection rules for Infrared and Raman spectroscopy.",
            "leadSummary": "Three-dimensional molecular architecture and mathematical symmetry: VSEPR theory, Gillespie-Nyholm repulsion hierarchy, derived molecular geometries, Drago's rule, Bent's rule of isovalent rehybridization, Coulson's theorem, group theoretical point groups, character tables, and vibrational Infrared and Raman selection rules.",
            "simId": "sim_chem_bent_rule_hybridization"
        },
        {
            "id": "unit6",
            "unitId": "unit6-inorg1",
            "number": 6,
            "unitNumber": 6,
            "title": "Unit 6: Quantum Theories of Bonding: Valence Bond & Molecular Orbital Frameworks",
            "description": "Quantum mechanics of the chemical bond: Heitler-London treatment of $\\text{H}_2$, symmetric singlet vs antisymmetric triplet wavefunctions, Coulomb and quantum exchange integrals; directional orbital overlap, $\\sigma$ and $\\pi$ bonds; Pauling orbital hybridization, mathematical derivation of $sp, sp^2, sp^3$ wavefunctions, orthogonality and normalization proofs; Molecular Orbital (MO) theory, Linear Combination of Atomic Orbitals (LCAO), Rayleigh-Ritz variational principle, Roothaan secular determinants, Coulomb, resonance, and spatial overlap integrals, analytical solution of the homonuclear diatomic secular determinant, fundamental asymmetry theorem of antibonding destabilization; second-row homonuclear diatomics, $2s-2p_z$ orbital mixing crossover, triplet ground state and paramagnetism of $\\text{O}_2$; heteronuclear diatomics ($\\text{CO}, \\text{NO}, \\text{HF}$), frontier orbitals (HOMO/LUMO), Dewar-Chatt-Duncanson $\\pi$-backbonding in transition metal carbonyls; and symmetry-adapted linear combinations (SALCs) for polyatomic molecules.",
            "leadSummary": "Quantum mechanics of the chemical bond: Heitler-London valence bond theory, orbital hybridization wavefunctions and orthogonality proofs, Molecular Orbital theory, LCAO secular determinants, homonuclear diatomics, $2s-2p$ mixing crossover, paramagnetism of $\\text{O}_2$, heteronuclear diatomics, Dewar-Chatt-Duncanson $\\pi$-backbonding, and Symmetry-Adapted Linear Combinations (SALCs).",
            "simId": "sim_chem_molecular_orbital_lcao"
        },
        {
            "id": "unit7",
            "unitId": "unit7-inorg1",
            "number": 7,
            "unitNumber": 7,
            "title": "Unit 7: Secondary Bonding, Intermolecular Forces & Advanced Acid-Base Equilibria",
            "description": "Non-covalent interactions and generalized acid-base equilibria: Keesom dipole-dipole, Debye induction, and London dispersion forces; hydrogen bonding continuum, symmetric single-well potentials in bifluoride $[\text{F}-\text{H}-\text{F}]^-$; Arrhenius, Brønsted-Lowry, and Lewis acid-base theories, solvent leveling and differentiating effects; Lux-Flood oxide-ion transfer concept in metallurgical molten slags; solvo-system autoionization, Usanovich generalized acid-base theory; Pearson's Hard and Soft Acids and Bases (HSAB) principle, Density Functional Theory formulation of absolute hardness $\\eta$ and electronegativity $\\chi$, Klopman-Salem equation, Jørgensen's principle of symbiosis; Drago-Wayland $E/C$ enthalpy parameters; superacids, George Olah's magic acid, fluoroantimonic acid, Hammett acidity function $H_0$; polyprotic acid speciation fractions, Donald Van Slyke buffer capacity equation; and the chelate and macrocyclic effects.",
            "leadSummary": "Non-covalent interactions and generalized acid-base equilibria: intermolecular potentials, hydrogen bonding, Arrhenius, Brønsted-Lowry, Lewis, Lux-Flood, and Usanovich theories, Pearson's HSAB principle, DFT chemical hardness, Drago-Wayland parameters, superacids, Hammett acidity function, polyprotic speciation, buffer capacity, and the chelate and macrocyclic effects.",
            "simId": "sim_chem_acid_base_titration_speciation"
        },
        {
            "id": "unit8",
            "unitId": "unit8-inorg1",
            "number": 8,
            "unitNumber": 8,
            "title": "Unit 8: Inorganic Chemical Reactions: Precipitation, Redox Spontaneity & Potential Diagrams",
            "description": "Equilibria, thermodynamics, and kinetics of inorganic reactions: heterogeneous dissolution equilibria, solubility product constant ($K_{sp}$), common-ion effect suppression, dissolution via coordination complex formation; formal oxidation states, ion-electron half-reaction balancing in acidic and basic media; electrochemical cell thermodynamics, reversible electrical work, Gibbs free energy ($\Delta G^\circ = -nFE^\circ$), Nernst equation derivation, temperature coefficient of cell EMF; Latimer diagrams, non-adjacent step potential averaging via extensive free energy summation, thermodynamic criteria for disproportionation and comproportionation; Frost oxidation state diagrams, slope-potential correspondence, thermodynamic sinks, and dismutation peaks; Pourbaix ($E-pH$) phase diagrams, horizontal, vertical, and slanted boundary equations, thermodynamic stability limits of water, immunity, active corrosion, and oxide passivation domains, cathodic protection, and multi-element stainless steel passivation.",
            "leadSummary": "Equilibria, thermodynamics, and kinetics of inorganic reactions: solubility products, common-ion effect, complexation dissolution, redox balancing in acidic/basic media, Nernst equation, Latimer potential diagrams, Frost stability landscapes, Pourbaix ($E-pH$) phase diagrams, corrosion domains, and industrial passivation.",
            "simId": "sim_chem_redox_latimer_frost_diagram"
        }
    ]

    processed_units = []

    for i, (meta, ru) in enumerate(zip(unit_meta, raw_units), 1):
        u_obj = {
            "id": meta["id"],
            "unitId": meta["unitId"],
            "number": meta["number"],
            "unitNumber": meta["unitNumber"],
            "title": meta["title"],
            "description": meta["description"],
            "leadSummary": meta["leadSummary"],
            "simulations": [meta["simId"]],
            "sections": [],
            "problems": []
        }

        # Process sections
        for s_idx, sec in enumerate(ru["sections"], 1):
            sec_id = sec.get("id", f"sec{i}_{s_idx}")
            title = sec["title"]
            # Clean heading
            heading = title.split(" ", 1)[1] if " " in title else title
            if heading.startswith("§"):
                parts = heading.split(" ", 1)
                heading = parts[1] if len(parts) > 1 else heading

            sec_obj = {
                "id": sec_id,
                "secNumber": f"§{i}.{s_idx}",
                "title": title,
                "heading": heading,
                "content": sec["content"],
                "simulations": [meta["simId"]] if s_idx == len(ru["sections"]) or s_idx == 5 else []
            }
            u_obj["sections"].append(sec_obj)

        # Process problems
        for p_idx, prob in enumerate(ru["problems"], 1):
            tier = prob.get("tier", "Foundational Level")
            diff = "foundational" if "Foundational" in tier else ("advanced" if "Advanced" in tier else "honors")
            prob_obj = {
                "id": f"prob{i}_{p_idx}",
                "difficulty": diff,
                "difficultyLabel": tier,
                "title": prob["title"],
                "question": prob["statement"],
                "statement": prob["statement"],
                "solution": prob["solution"]
            }
            u_obj["problems"].append(prob_obj)

        processed_units.append(u_obj)

    course_data = {
        "courseCode": "",
        "courseTitle": "Inorganic Chemistry I: Atomic Structure, Periodic Trends, Chemical Bonding, Acid-Base Equilibria & Redox Systems",
        "courseSubtitle": "Quantum Mechanical Models of the Atom, Relativistic Periodicity, Ionic Cohesion & Crystal Energetics, Advanced Covalent Architectures, VSEPR & Symmetry Group Theory, Valence Bond & Molecular Orbital Frameworks, Generalized Acid-Base Models & HSAB Theory, and Electrochemical Potential Topologies",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "General Chemistry, Multivariable Calculus & Quantum Physics Foundations",
        "description": "Comprehensive university honors digital textbook on Inorganic Chemistry: quantum theory of the atom, Bohr-Sommerfeld model, de Broglie matter waves, Heisenberg uncertainty, Schrödinger wave equation, radial and angular wavefunctions, quantum numbers, electron configurations, Hund's rules, Pauli exclusion principle, and Slater effective nuclear charge; periodic properties of elements, Moseley's law, atomic/ionic/covalent radii, ionization energies, electron affinities, Pauling, Mulliken, Allred-Rochow, and Allen electronegativity scales, inert pair effect, and Dirac relativistic orbital contraction; ionic bonding, Born-Haber thermochemical cycles, Madelung constants, Evjen neutral cell summation, Born-Landé and Kapustinskii equations, radius ratio packing rules, Fajan's polarization rules, crystal point defects, and superionic conductors; covalent bonding, Lewis formalisms, formal charges, Pimentel-Rundle 3c-4e hypervalency, Morse potential, bond enthalpies, percent ionic character, Natural Bond Orbital (NBO) analysis, and Wade's rules; molecular geometries, VSEPR theory, Gillespie-Nyholm axioms, Bent's rule, Coulson's theorem, group theoretical point groups, and vibrational selection rules; quantum theories of bonding, Heitler-London valence bond theory, orbital hybridization, molecular orbital theory, LCAO secular determinants, homonuclear diatomics, $2s-2p$ mixing, paramagnetism of $O_2$, heteronuclear diatomics, and metal carbonyl $\pi$-backbonding; intermolecular interactions, hydrogen bonding, Arrhenius, Brønsted-Lowry, Lewis, Lux-Flood, and Usanovich acid-base models, Pearson's HSAB principle, absolute hardness, polyprotic speciation, buffer capacity, and superacids; and inorganic reactions, precipitation equilibria, solubility products, redox equation balancing, Nernst equation, Latimer diagrams, Frost oxidation state landscapes, and Pourbaix potential-pH phase diagrams. Features 8 interactive 60 FPS Canvas simulations and 24 tiered solved problems with complete line-by-line mathematical proofs.",
        "units": processed_units
    }

    # Verify zero course numbers or marks
    raw_json = json.dumps(course_data, indent=2)
    banned_patterns = ["Chem 1", "Chem 2", "Chem.", "100 Marks", "50 Marks", "70+20", "35+10", "1 Unit"]
    for bp in banned_patterns:
        if bp.lower() in raw_json.lower():
            print(f"WARNING: Banned pattern '{bp}' found in course data!")
            sys.exit(1)

    output_path = "inorganic-chemistry-1-data.js"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("// Inorganic Chemistry I Master Textbook Data File\n")
        f.write("// STRICT CONSTRAINT: ZERO COURSE NUMBERS OR MARKS PERMITTED\n")
        f.write("window.COURSE_DATA = ")
        f.write(raw_json)
        f.write(";\n")

    print(f"Successfully generated {output_path} with {len(processed_units)} units.")
    
    # Calculate total words in data file
    with open(output_path, "r", encoding="utf-8") as f:
        text = f.read()
    print(f"Total word count of {output_path}: {len(text.split())} words.")

if __name__ == "__main__":
    main()
