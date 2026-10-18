# -*- coding: utf-8 -*-
"""
Assembler for nuclear-physics-2-data.js
Combines nuc2_u1.json through nuc2_u8.json into window.COURSE_DATA and window.NUC2_COURSE_DATA
"""
import json

units = []
for i in range(1, 9):
    with open(f"nuc2_u{i}.json", "r", encoding="utf-8") as f:
        u = json.load(f)
    
    # Ensure simulations array if simulation present
    for sec in u.get("sections", []):
        if "simulation" in sec and "simulations" not in sec:
            sec["simulations"] = [sec["simulation"]]
            
    unit_obj = {
        "id": f"unit{i}",
        "number": i,
        "unitNumber": i,
        "unitId": f"unit{i}-nuc2",
        "title": u["title"],
        "subtitle": u.get("subtitle", ""),
        "leadSummary": u.get("summary", ""),
        "sections": u.get("sections", []),
        "problems": u.get("problems", [])
    }
    units.append(unit_obj)

course_data = {
    "courseId": "nuclear-physics-2",
    "courseTitle": "Nuclear Physics II: Two-Body Bound States, Nuclear Forces, Reaction Models & Hadron Symmetries",
    "courseDescription": "An advanced theoretical treatment of modern nuclear and subatomic physics: Part A covers the two-nucleon bound state (deuteron ground-state properties, central potential depth-radius relation, electric quadrupole moment, non-central tensor force, photodisintegration kinematics), low-energy and high-energy nucleon-nucleon scattering (partial-wave phase shifts, scattering lengths, effective range expansion, hard repulsive core, backward charge-exchange peak, coherent ortho- and para-hydrogen scattering), fundamental nuclear forces and meson theory (charge independence and charge symmetry, isospin SU(2)_I formalism, One-Boson-Exchange OBE model, Yukawa pion potential, Majorana/Bartlett/Heisenberg exchange operators), and interaction of nuclei with electromagnetic radiation (multipole expansion, electric and magnetic transition operators, Weisskopf single-particle estimates, two-body radiative capture n+p -> d+γ, internal conversion coefficients, E0 monopole decay, and Giant Dipole Resonance collective Lorentzian absorption). Part B investigates advanced nuclear structure models (Fermi gas model, 3D harmonic oscillator and Woods-Saxon potentials with Mayer-Jensen spin-orbit coupling, magic numbers 2, 8, 20, 28, 50, 82, 126, Nordheim coupling rules, Schmidt magnetic moment limits, Bohr-Mottelson collective surface vibrations and deformed spheroidal rotations, Nilsson single-particle diagram, Coriolis pair-breaking backbending), nuclear reaction mechanisms and scattering (Q-values and laboratory threshold kinematics, phenomenological Optical Model complex potentials, partial-wave S-matrix, transmission coefficients, direct stripping/pickup reactions, Niels Bohr compound nucleus hypothesis, Bethe level density, Breit-Wigner single-level dispersion resonance with potential interference), and modern elementary particle physics across two comprehensive units (the four fundamental interactions, gauge bosons, quantum conservation laws, Gell-Mann-Nishijima formula, deep inelastic scattering and Bjorken scaling, Cornell quark confinement potential, discrete spacetime symmetries P, C, T, Madame Wu's 60Co beta decay parity violation, Cronin-Fitch neutral kaon CP violation, Sakharov baryogenesis, Lie algebra su(3) flavor Eightfold Way, hadron multiplet decompositions 3 ⊗ 3̄ = 8 ⊕ 1 and 3 ⊗ 3 ⊗ 3 = 10 ⊕ 8 ⊕ 8 ⊕ 1, Gell-Mann-Okubo mass formula, prediction and discovery of the Ω- hyperon, non-Abelian SU(3)_C Quantum Chromodynamics with asymptotic freedom, Glashow-Weinberg-Salam SU(2)_L × U(1)_Y electroweak unification, Higgs mechanism, CKM quark mixing, and PMNS neutrino oscillations with solar MSW matter resonance), accompanied by 16 interactive 60 FPS numerical simulations and 24 rigorous honors examination problems.",
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\nwindow.NUC2_COURSE_DATA = window.COURSE_DATA;\n"

with open("nuclear-physics-2-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"nuclear-physics-2-data.js successfully written! Total units: {len(units)}")
