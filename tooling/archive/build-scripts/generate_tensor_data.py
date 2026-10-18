# -*- coding: utf-8 -*-
"""
generate_tensor_data.py
Assembles all 8 units into tensor-analysis-data.js
Ensures STRICT ZERO course codes or numbers anywhere in data.
"""

import json
import re
from build_tensor_unit1 import get_unit1
from build_tensor_unit2 import get_unit2
from build_tensor_unit3 import get_unit3
from build_tensor_unit4 import get_unit4
from build_tensor_unit5 import get_unit5
from build_tensor_unit6 import get_unit6
from build_tensor_unit7 import get_unit7
from build_tensor_unit8 import get_unit8

def assemble_tensor_data():
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
        1: ("1.5", "sim_tensor_coord_transform"),
        2: ("2.5", "sim_tensor_algebra_contraction"),
        3: ("3.5", "sim_tensor_metric_geometry"),
        4: ("4.5", "sim_tensor_christoffel_geodesic"),
        5: ("5.5", "sim_tensor_covariant_diff"),
        6: ("6.5", "sim_tensor_riemann_curvature"),
        7: ("7.5", "sim_tensor_weyl_conformal"),
        8: ("8.5", "sim_tensor_einstein_field"),
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
            diff_class = "diff-easy" if "Foundational" in tier or "Fundamentals" in tier else ("diff-medium" if "Advanced" in tier or "Computational" in tier else "diff-hard")
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
            "unitId": f"unit{u_idx}-tensor",
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
        "courseTitle": "Tensor Analysis: Differential Invariants, Riemannian Metrics, Covariant Differentiation & Curvature Tensors",
        "courseSubtitle": "Index Notation & Affine Spaces, Tensor Algebra & Quotient Law, Riemannian Metrics & Index Manipulation, Christoffel Symbols & Geodesics, Covariant Differentiation & Ricci's Theorem, Curvature Tensors & Bianchi Identities, Hypersurfaces & Conformal Curvature, and Physical Applications to Continuum Mechanics, Electrodynamics & Gravitation",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "Multivariable Calculus, Linear Algebra & Differential Geometry",
        "description": "Exhaustive honors-level master digital textbook on tensor analysis and Riemannian differential geometry: Einstein summation convention, dummy and free indices, generalized Kronecker delta and Levi-Civita permutation pseudo-tensors, contravariant and covariant vector transformation laws, affine spaces and tangent spaces, tensor algebra operations including outer product, index contraction, inner products, symmetric and antisymmetric decomposition, the fundamental Quotient Law with unskipped proofs, Riemannian and pseudo-Riemannian metric tensors, conjugate metric determinants, derivative identities and Jacobi formulas, musical isomorphisms for raising and lowering indices, Christoffel symbols of the first and second kinds, non-tensorial inhomogeneous transformation rules, the Levi-Civita metric-compatible connection, contracted connection divergence formulas, geodesic equations derived from the variational principle, geodesic deviation and tidal Jacobi fields, covariant differentiation of general type (r, s) tensors, product rules, Ricci's Theorem proving covariant constancy of the metric, invariant gradient, divergence, curl, and Laplace-Beltrami operators, parallel transport, holonomy and the Foucault pendulum, the Riemann curvature tensor derived from commutators of covariant derivatives, full algebraic symmetries, formula for the n^2(n^2-1)/12 independent components, Ricci tensor, scalar curvature, Einstein tensor, first and second Bianchi differential identities, twice-contracted Bianchi identity and conservation laws, sectional curvature and Schur's Theorem, Riemannian flatness criteria, Weyl conformal curvature tensor in n dimensions, Cotton-York tensor in 3D, geometry of embedded hypersurfaces, first and second fundamental forms, Weingarten shape operator, principal curvatures, Mean and Gaussian curvature, Gauss-Codazzi-Mainardi embedding equations, Cauchy stress and continuum momentum conservation, covariant Maxwell electrodynamics, 4-potential and Faraday field tensor, the geodesic principle and gravitational time dilation / redshift, derivation of the Einstein field equations with cosmological constant, and the exact Schwarzschild black hole solution with planetary perihelion precession and gravitational starlight bending. Features 8 interactive 60 FPS Canvas simulations and 24 tiered solved examination problems with complete line-by-line mathematical proofs.",
        "units": processed_units
    }

    # Verify strictly zero course numbers
    json_str = json.dumps(course_data, ensure_ascii=False, indent=2)
    course_code_matches = re.findall(r'MTH[\s-]*\d+|4202', json_str, re.IGNORECASE)
    if course_code_matches:
        raise ValueError(f"STRICT ERROR: Prohibited course codes detected in data: {course_code_matches}")

    out_file = "tensor-analysis-data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Tensor Analysis Master Textbook Data File\n")
        f.write("// STRICT CONSTRAINT: ZERO COURSE NUMBERS OR CODES PERMITTED\n")
        f.write("window.COURSE_DATA = ")
        f.write(json_str)
        f.write(";\n")

    print(f"Successfully generated {out_file} with {len(processed_units)} units, "
          f"{sum(len(u['sections']) for u in processed_units)} sections, and "
          f"{sum(len(u['problems']) for u in processed_units)} solved problems.")

if __name__ == "__main__":
    assemble_tensor_data()
