#!/usr/bin/env python3
"""
sync_platform.py
Synchronizes platform files for Textbook #43: Inorganic Chemistry I
1. departments-data.js
2. index.html
3. sitemap.xml
4. Cross-link reader footers in existing textbooks
"""

import re

def update_departments_data():
    with open("departments-data.js", "r", encoding="utf-8") as f:
        content = f.read()

    inorg_course_entry = r''',
        {
          id: "inorganic-chemistry-1",
          title: "Inorganic Chemistry I: Atomic Structure, Periodic Trends, Chemical Bonding, Acid-Base Equilibria & Redox Systems",
          subtitle: "Quantum Theory of the Atom & Electronic Structure, Periodicity & Relativistic Dirac Effects, Ionic Bonding & Crystal Energetics, Advanced Covalent Architectures & Hypervalency, VSEPR & Molecular Symmetry Group Theory, Valence Bond & Molecular Orbital Frameworks, Secondary Bonding & Generalized Acid-Base Models, and Precipitation & Electrochemical Potential Landscapes",
          status: "AVAILABLE",
          url: "inorganic-chemistry-1.html",
          badge: "✨ NEW • Interactive Master Book Live",
          seoKeywords: "Inorganic Chemistry Textbook, Atomic Structure, Quantum Theory, Bohr Model, Schrödinger Equation, Radial Distribution, Slater Rules, Effective Nuclear Charge, Moseley Law, Periodic Trends, Atomic Radii, Ionization Energy, Electron Affinity, Pauling Electronegativity, Relativistic Effects, Dirac Contraction, Lanthanide Contraction, Inert Pair Effect, Ionic Bonding, Born-Haber Cycle, Lattice Energy, Madelung Constant, Born-Lande Equation, Kapustinskii Equation, Radius Ratio Rules, Fajans Rules, Crystal Defects, Superionic Conduction, Covalent Bonding, Lewis Structures, Hypervalency, 3c-4e Bond, Resonance, Bond Enthalpy, Dipole Moment, VSEPR Theory, Bents Rule, Coulsons Theorem, Group Theory, Point Groups, Molecular Symmetry, Valence Bond Theory, Hybridization, Molecular Orbital Theory, LCAO, Diatomic MO, Paramagnetism of Oxygen, Backbonding, Secondary Bonding, Hydrogen Bonding, Acid-Base Theories, Lux-Flood, Pearson HSAB, Chemical Hardness, Polyprotic Acids, Buffer Capacity, Superacids, Redox Reactions, Nernst Equation, Latimer Diagram, Frost Diagram, Pourbaix Diagram, Corrosion Passivation",
          description: "Comprehensive university honors master digital textbook on inorganic chemistry: quantum theory of the atom, Bohr-Sommerfeld model, de Broglie matter waves, Heisenberg uncertainty principle, Schrödinger wave equation, radial and angular wavefunctions, quantum numbers, electron configurations, Hund's rules, Pauli exclusion principle, and Slater effective nuclear charge; periodic properties of elements, Moseley's law, atomic/ionic/covalent radii, ionization energies, electron affinities, Pauling, Mulliken, Allred-Rochow, and Allen electronegativity scales, inert pair effect, and Dirac relativistic orbital contraction; ionic bonding, Born-Haber thermochemical cycles, Madelung constants, Evjen neutral cell summation, Born-Landé and Kapustinskii equations, radius ratio packing rules, Fajan's polarization rules, crystal point defects, and superionic conductors; covalent bonding, Lewis formalisms, formal charges, Pimentel-Rundle 3c-4e hypervalency, Morse potential, bond enthalpies, percent ionic character, Natural Bond Orbital (NBO) analysis, and Wade's rules; molecular geometries, VSEPR theory, Gillespie-Nyholm axioms, Bent's rule, Coulson's theorem, group theoretical point groups, and vibrational selection rules; quantum theories of bonding, Heitler-London valence bond theory, orbital hybridization, molecular orbital theory, LCAO secular determinants, homonuclear diatomics, 2s-2p mixing, paramagnetism of O2, heteronuclear diatomics, and metal carbonyl pi-backbonding; intermolecular interactions, hydrogen bonding, Arrhenius, Brønsted-Lowry, Lewis, Lux-Flood, and Usanovich acid-base models, Pearson's HSAB principle, absolute hardness, polyprotic speciation, buffer capacity, and superacids; and inorganic reactions, precipitation equilibria, solubility products, redox equation balancing, Nernst equation, Latimer diagrams, Frost oxidation state landscapes, and Pourbaix potential-pH phase diagrams. Features 8 interactive 60 FPS Canvas simulations and 32 tiered solved examination problems with complete line-by-line mathematical proofs.",
          topics: [
            "Quantum Theory of the Atom, Wave Mechanics & Electronic Architecture",
            "Periodicity of the Elements, Electronic Shielding & Relativistic Effects",
            "The Chemical Bond I: Ionic Bonding, Crystal Energetics & Superionic Conductors",
            "The Chemical Bond II: Covalent Bonding, Hypervalency & Cluster Topologies",
            "Molecular Geometry: VSEPR Theory, Bent's Rule & Symmetry Group Theory",
            "Quantum Theories of Bonding: Valence Bond & Molecular Orbital Frameworks",
            "Secondary Bonding, Intermolecular Forces & Advanced Acid-Base Equilibria",
            "Inorganic Chemical Reactions: Precipitation, Redox Spontaneity & Potential Diagrams"
          ]
        }'''

    target = 'url: "physical-chemistry-1.html"'
    if target in content and 'inorganic-chemistry-1' not in content:
        # Find closing of physical-chemistry-1 course object
        pchem_idx = content.find(target)
        closing_brace = content.find('}', pchem_idx)
        # Find topics closing
        topics_idx = content.find('topics:', pchem_idx)
        closing_topics = content.find(']', topics_idx)
        course_closing = content.find('}', closing_topics)

        content = content[:course_closing+1] + inorg_course_entry + content[course_closing+1:]
        with open("departments-data.js", "w", encoding="utf-8") as f:
            f.write(content)
        print("departments-data.js updated with inorganic-chemistry-1.")
    else:
        print("departments-data.js already contains inorganic-chemistry-1 or target not found.")

def update_index_html():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Bump 42 -> 43
    content = content.replace("✓ Live Now • 42 Textbooks", "✓ Live Now • 43 Textbooks")
    content = content.replace("Explore 42 Live Textbooks ↓", "Explore 43 Live Textbooks ↓")

    # Add footer link
    pchem_link = '<a href="physical-chemistry-1.html" class="footer-link" style="color: #38bdf8; font-weight: 600;">Physical Chemistry I</a>'
    inorg_link = '\n      <a href="inorganic-chemistry-1.html" class="footer-link" style="color: #38bdf8; font-weight: 600;">Inorganic Chemistry I</a>'
    
    if pchem_link in content and 'inorganic-chemistry-1.html' not in content:
        content = content.replace(pchem_link, '<a href="physical-chemistry-1.html" class="footer-link">Physical Chemistry I</a>' + inorg_link)

    # Bump cache-busters to v=20261008_v12
    content = re.sub(r'v=20261008_v\d+', 'v=20261008_v12', content)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("index.html updated to 43 live textbooks and cache-busters bumped.")

def update_sitemap():
    with open("sitemap.xml", "r", encoding="utf-8") as f:
        content = f.read()

    pchem_entry = """  <url>
    <loc>https://openstemlibrary.com/physical-chemistry-1.html</loc>
    <lastmod>2026-10-08</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>"""

    inorg_entry = """
  <url>
    <loc>https://openstemlibrary.com/inorganic-chemistry-1.html</loc>
    <lastmod>2026-10-08</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>"""

    if pchem_entry in content and 'inorganic-chemistry-1.html' not in content:
        content = content.replace(pchem_entry, pchem_entry + inorg_entry)
        with open("sitemap.xml", "w", encoding="utf-8") as f:
            f.write(content)
        print("sitemap.xml updated with inorganic-chemistry-1.html.")
    else:
        print("sitemap.xml already contains inorganic-chemistry-1.html or pchem entry not exact.")

def cross_link_footers():
    footers_to_update = [
        "physical-chemistry-1.html",
        "fuzzy-mathematics.html",
        "tensor-analysis.html",
        "discrete-mathematics.html"
    ]

    inorg_link = '              <a href="inorganic-chemistry-1.html" class="reader-trust-link">Inorganic Chemistry I</a>\n'

    for fname in footers_to_update:
        try:
            with open(fname, "r", encoding="utf-8") as f:
                c = f.read()
            if "inorganic-chemistry-1.html" not in c:
                target = '<a href="physical-chemistry-1.html"'
                if target in c:
                    idx = c.find(target)
                    end_line = c.find('\n', idx)
                    c = c[:end_line+1] + inorg_link + c[end_line+1:]
                    with open(fname, "w", encoding="utf-8") as f:
                        f.write(c)
                    print(f"Cross-linked inorganic-chemistry-1 in {fname}.")
        except Exception as e:
            print(f"Error updating {fname}: {e}")

if __name__ == "__main__":
    update_departments_data()
    update_index_html()
    update_sitemap()
    cross_link_footers()
    print("Platform synchronization complete!")
