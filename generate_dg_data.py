# -*- coding: utf-8 -*-
"""
generate_dg_data.py
Assembles all 8 units into differential-geometry-data.js
Ensures STRICT ZERO course codes or numbers anywhere in data.
"""

import json
import re
from build_dg_unit1 import get_unit1
from build_dg_unit2 import get_unit2
from build_dg_unit3 import get_unit3
from build_dg_unit4 import get_unit4
from build_dg_unit5 import get_unit5
from build_dg_unit6 import get_unit6
from build_dg_unit7 import get_unit7
from build_dg_unit8 import get_unit8

def assemble_dg_data():
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
        1: ("1.3", "sim_dg_space_curve_tangent"),
        2: ("2.2", "sim_dg_frenet_frame"),
        3: ("3.1", "sim_dg_helix_bertrand"),
        4: ("4.2", "sim_dg_first_fundamental_form"),
        5: ("5.1", "sim_dg_gauss_map_weingarten"),
        6: ("6.1", "sim_dg_curvatures_principal"),
        7: ("7.3", "sim_dg_dupin_indicatrix"),
        8: ("8.4", "sim_dg_geodesic_egregium"),
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
                "id": f"u{u_idx}-sec{s_idx}",
                "secNumber": sec_num,
                "title": sec.get("title", ""),
                "heading": sec.get("title", ""),
                "content": sec.get("content", ""),
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
            "unitId": f"unit{u_idx}-dg",
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
        "courseTitle": "Differential Geometry: Curves, Surfaces, Fundamental Forms & Curvatures",
        "courseSubtitle": "Space Curves, Frenet-Serret Apparatus, Metric Tensors, Shape Operators, Curvature Invariants, Geodesics & Theorema Egregium",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "Multivariable Calculus, Linear Algebra & Ordinary Differential Equations",
        "description": "Exhaustive honors-level master digital textbook on classical differential geometry in Euclidean 3-space: smooth parametrized curves and regular points, arc-length reparametrization, unit tangent vector, equations of tangent lines and normal planes, contact order and osculating planes, canonical Taylor expansions, curvature and principal normal vector, binormal vector, rectifying planes, Serret-Frenet moving trihedron formulas, torsion and planarity characterization, the Darboux rotation vector, Fundamental Theorem of Space Curves, circular and general cylindrical helices, Lancret's theorem, spherical curves and spherical indicatrices, involutes and string evolutes, evolutes as loci of centers of curvature, Bertrand conjugate mates, smooth coordinate surface patches and regularity, tangent planes and surface unit normals, First Fundamental Form metric tensor E, F, G, positive definiteness and Gram determinant, arc-length of surface curves, local isometries, conformal mappings and isothermal coordinates, angles between tangent directions and orthogonal nets, intrinsic surface area elements and change of variables invariance, spherical Gauss map and its differential, Shape Operator / Weingarten map and self-adjointness, Second Fundamental Form L, M, N, Weingarten equations, Third Fundamental Form III, Cayley-Hamilton operator identity III - 2H II + K I = 0, normal curvature and Meusnier's theorem, principal curvatures and directions as Rayleigh quotient extrema, characteristic quadratic curvature equation, Gaussian curvature K and Mean curvature H, geometric point classifications (elliptic, hyperbolic, parabolic, planar, and umbilical points), minimal surfaces (H = 0) and soap film geometry, surfaces of revolution and Beltrami's pseudosphere, Rodrigues' formula and differential equations of lines of curvature, Euler's theorem on normal curvature, Dupin indicatrix conic sections, asymptotic curves (II = 0), Beltrami-Enneper theorem on asymptotic torsion (tau^2 = -K), conjugate directions, triply orthogonal systems and Dupin's theorem, Gauss's moving frame and Christoffel symbols of the second kind, Gauss and Codazzi-Mainardi compatibility integrability equations, Bonnet's fundamental theorem of surface theory, Gauss's celebrated Theorema Egregium and Brioschi's determinant formula, geodesics as curves of zero geodesic curvature, geodesic Euler-Lagrange equations, Clairaut's relation on surfaces of revolution, geodesic curvature kg, Liouville's formula, and the local Gauss-Bonnet theorem relating curvature to angular excess. Features 8 interactive 60 FPS Canvas simulations and 24 tiered solved examination problems with complete line-by-line mathematical proofs.",
        "units": processed_units
    }

    # Verify strictly zero course numbers
    json_str = json.dumps(course_data, ensure_ascii=False, indent=2)
    course_code_matches = re.findall(r'MTH[\s-]*\d+', json_str, re.IGNORECASE)
    if course_code_matches:
        raise ValueError(f"STRICT ERROR: Prohibited course codes detected in data: {course_code_matches}")

    out_file = "differential-geometry-data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Differential Geometry Master Textbook Data File\n")
        f.write("// STRICT CONSTRAINT: ZERO COURSE NUMBERS OR CODES PERMITTED\n")
        f.write("window.COURSE_DATA = ")
        f.write(json_str)
        f.write(";\n")

    print(f"Successfully generated {out_file} with {len(processed_units)} units, "
          f"{sum(len(u['sections']) for u in processed_units)} sections, and "
          f"{sum(len(u['problems']) for u in processed_units)} solved problems.")

if __name__ == "__main__":
    assemble_dg_data()
