# -*- coding: utf-8 -*-
"""
generate_pde_data.py
Assembles all 8 units into partial-differential-equations-data.js
Ensures STRICT ZERO course codes or numbers anywhere in data.
"""

import json
import re
from build_pde_unit1 import get_unit1
from build_pde_unit2 import get_unit2
from build_pde_unit3 import get_unit3
from build_pde_unit4 import get_unit4
from build_pde_unit5 import get_unit5
from build_pde_unit6 import get_unit6
from build_pde_unit7 import get_unit7
from build_pde_unit8 import get_unit8

def assemble_pde_data():
    raw_units = [
        get_unit1(),
        get_unit2(),
        get_unit3(),
        get_unit4(),
        get_unit5(),
        get_unit6(),
        get_unit7(),
        get_unit8(),
    ]

    sim_map = {
        1: ("1.5", "sim_pde_lagrange_characteristics"),
        2: ("2.3", "sim_pde_charpit_monge_cone"),
        3: ("3.1", "sim_pde_canonical_classifier"),
        4: ("4.1", "sim_pde_wave_dalembert_modes"),
        5: ("5.5", "sim_pde_heat_diffusion_kernel"),
        6: ("6.2", "sim_pde_laplace_harmonic_potential"),
        7: ("7.3", "sim_pde_cylindrical_drumhead_bessel"),
        8: ("8.5", "sim_pde_greens_function_images"),
    }

    processed_units = []
    for u_idx, raw_u in enumerate(raw_units, 1):
        target_sec_num, target_sim = sim_map.get(u_idx, ("", ""))

        sections = []
        for s_idx, sec in enumerate(raw_u.get("sections", []), 1):
            sec_num = sec.get("secNumber", f"{u_idx}.{s_idx}")
            sec_sims = []
            if sec_num == target_sec_num and target_sim:
                sec_sims = [target_sim]

            sections.append({
                "id": f"sec{u_idx}-{s_idx}",
                "secNumber": sec_num,
                "title": sec["title"],
                "content": sec["content"],
                "simulations": sec_sims
            })

        problems = []
        for p_idx, prob in enumerate(raw_u.get("problems", []), 1):
            tier = prob.get("tier", "Solved Examination Problem")
            diff_class = "diff-easy" if "Foundational" in tier else ("diff-medium" if "Advanced" in tier else "diff-hard")
            stmt = prob.get("statement") or prob.get("content") or ""
            problems.append({
                "id": f"p{u_idx}-{p_idx}",
                "difficulty": diff_class,
                "difficultyLabel": tier,
                "title": prob.get("title", f"Problem {u_idx}.{p_idx}"),
                "question": stmt,
                "statement": stmt,
                "hints": prob.get("hints", []),
                "solution": prob.get("solution", "")
            })

        processed_units.append({
            "id": f"unit{u_idx}",
            "unitId": f"unit{u_idx}-pde",
            "number": u_idx,
            "unitNumber": u_idx,
            "title": f"Unit {u_idx}: {raw_u['title']}",
            "description": raw_u.get("leadSummary", ""),
            "leadSummary": raw_u.get("leadSummary", ""),
            "simulations": [target_sim] if target_sim else [],
            "sections": sections,
            "problems": problems
        })

    course_data = {
        "courseCode": "",
        "courseTitle": "Partial Differential Equations: First-Order Systems, Canonical Reductions, Boundary Value Problems, Fourier Methods & Green's Functions",
        "courseSubtitle": "First-Order PDEs & Lagrange Auxiliary Equations, Cauchy Problems & Monge Cones, Canonical Classification (Hyperbolic, Parabolic, Elliptic), Wave Equation & D'Alembert Formula, Heat Diffusion & Maximum Principles, Elliptic BVPs & Harmonic Functions, Cylindrical/Spherical Harmonics & Special Functions, and Integral Transforms & Green's Functions",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "Multivariable Calculus, Linear Algebra & Ordinary Differential Equations",
        "description": "Exhaustive honors-level master digital textbook on partial differential equations: classification and geometric derivation of first-order PDEs, elimination of arbitrary constants and arbitrary functions, complete integrals, general solutions, envelopes and singular solutions, Lagrange's auxiliary system for quasilinear equations P p + Q q = R, integral surfaces passing through space curves, transversality condition and local Cauchy-Kovalevskaya theorem, traffic flow conservation laws and kinematic waves, non-linear first-order PDEs, Monge cones and contact elements, Charpit's auxiliary equations for general non-linear equations F(x, y, z, p, q) = 0, standard forms I through IV (Clairaut equation), wave steepening and shock formation in Burgers equation, Rankine-Hugoniot jump condition, general second-order linear PDEs in two variables, coordinate invariance of the discriminant Delta = B^2 - AC, canonical reduction of hyperbolic equations to cross-derivative and wave forms, parabolic equations to diffusion forms, elliptic equations to Laplace-Poisson forms, variable-coefficient mixed-type equations and Tricomi's equation, physical derivation of the 1D wave equation, D'Alembert's traveling wave formula, domain of dependence, range of influence and relativistic causality cones, semi-infinite strings and the method of images, Fourier separation of variables into standing normal modes, total mechanical energy conservation and solution uniqueness proofs, physical derivation of the heat equation and Fourier's law of conduction, weak and strong maximum/minimum principles, uniqueness of parabolic initial-boundary value problems, separation of variables for finite rods under Dirichlet, Neumann, and Robin boundaries, Duhamel's principle for time-dependent sources, the Gaussian fundamental solution (heat kernel) and error function convolution, elliptic equations in electrostatics, gravitation, steady heat, and potential fluid flow, properties of harmonic functions, Gauss's Mean Value Property, Strong Maximum Principle, Liouville's theorem, Dirichlet problem on rectangles and disks, Poisson integral formula for disks and half-planes, Dirichlet's energy minimization principle, curvilinear scale factors and Laplacians in cylindrical and spherical coordinates, Frobenius series for Bessel functions J_n and Y_n, vibrations of circular drumheads and Bessel zeros, Legendre differential equation and orthogonal Legendre polynomials P_n(cos theta), multipole expansions, Fourier sine and cosine transforms for semi-infinite domains, bilateral Fourier transform for dispersive waves, Laplace transform operational methods for initial-boundary value problems, Green's first and second identities, distributional Dirac delta sources and free-space fundamental solutions, and construction of Dirichlet Green's functions via the method of images for half-spaces, corners, and spheres. Features 8 interactive 60 FPS Canvas simulations and 24 tiered solved examination problems with complete line-by-line mathematical proofs.",
        "units": processed_units
    }

    # Verify strictly zero course numbers
    json_str = json.dumps(course_data, ensure_ascii=False, indent=2)
    course_code_matches = re.findall(r'MTH[\s-]*\d+', json_str, re.IGNORECASE)
    if course_code_matches:
        raise ValueError(f"STRICT ERROR: Prohibited course codes detected in data: {course_code_matches}")

    out_file = "partial-differential-equations-data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Partial Differential Equations Master Textbook Data File\n")
        f.write("// STRICT CONSTRAINT: ZERO COURSE NUMBERS OR CODES PERMITTED\n")
        f.write("window.COURSE_DATA = ")
        f.write(json_str)
        f.write(";\n")

    print(f"Successfully generated {out_file} with {len(processed_units)} units, "
          f"{sum(len(u['sections']) for u in processed_units)} sections, and "
          f"{sum(len(u['problems']) for u in processed_units)} solved problems.")

if __name__ == "__main__":
    assemble_pde_data()
