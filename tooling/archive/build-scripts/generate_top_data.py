# -*- coding: utf-8 -*-
"""
generate_top_data.py
Assembles all 8 units into topology-data.js
Ensures STRICT ZERO course codes or numbers anywhere in data.
"""

import json
import re
from build_top_unit1 import get_unit1
from build_top_unit2 import get_unit2
from build_top_unit3 import get_unit3
from build_top_unit4 import get_unit4
from build_top_unit5 import get_unit5
from build_top_unit6 import get_unit6
from build_top_unit7 import get_unit7
from build_top_unit8 import get_unit8

def assemble_top_data():
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
        1: ("1.1", "sim_top_metric_balls_p"),
        2: ("2.2", "sim_top_closure_interior_boundary"),
        3: ("3.5", "sim_top_quotient_surfaces"),
        4: ("4.4", "sim_top_countability_hierarchy"),
        5: ("5.2", "sim_top_separation_axioms"),
        6: ("6.3", "sim_top_urysohn_dyadic_potential"),
        7: ("7.3", "sim_top_compact_open_covers"),
        8: ("8.4", "sim_top_connected_sine_curve"),
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
            "unitId": f"unit{u_idx}-top",
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
        "courseTitle": "General Topology: Metric Spaces, Topological Structures, Separation, Compactness & Connectedness",
        "courseSubtitle": "Metric Spaces & Baire Category, Topological Spaces & Bases, Continuity & Quotient Topologies, Countability Axioms, Separation Hierarchy (T0-T4), Urysohn's Lemma & Metrization, Compactness & Tychonoff's Theorem, and Connectedness & Components",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "Real Analysis, Abstract Algebra & Set Theory",
        "description": "Exhaustive honors-level master digital textbook on general point-set topology and metric space theory: definition of metric spaces, classical metric spaces (Euclidean, taxicab, Chebyshev, sequence spaces l^p and l^inf, function space C[a, b], discrete metric, ultrametrics), open balls, open sets, topologies induced by metrics, equivalent metrics (topological vs Lipschitz equivalence), sequences, Cauchy sequences, completeness, Cantor's Intersection Theorem, dense sets, nowhere dense sets, meager (first category) sets, Baire's Category Theorem with complete proof, space of continuous functions with uniform metric, Banach Fixed-Point Contraction Mapping Theorem, axiomatic definition of topological spaces, comparison of topologies (coarser vs finer), classical non-metric topologies (co-finite, co-countable, discrete, indiscrete, Sierpinski), closed sets, interior, closure, boundary, Kuratowski Closure Axioms, neighborhood systems and filters, accumulation and derived points, bases and subbases for a topology, the Basis Criterion Theorem, subspace (relative) topology, hereditary properties, continuous mappings and equivalent characterizations (open preimages, closed preimages, closure inclusions f(cl(A)) subset of cl(f(A))), Pasting (Gluing) Lemma, homeomorphisms and topological invariants, topological embeddings, initial (weak) and final topologies, function algebras C(X, R), quotient spaces and identification maps, classical 2-manifold constructions (cylinder, Mobius strip, torus T^2, Klein bottle, and real projective plane RP^2), countability axioms (first-countable spaces, second-countable spaces, separable spaces, Lindelöf spaces), countability implication hierarchy, metric countability equivalence, the Sorgenfrey line and Sorgenfrey plane product pathology, separation axioms (Kolmogorov T0, Fréchet T1, Hausdorff T2, regular and T3, completely regular T3.5 / Tychonoff, normal T4), uniqueness of limits in Hausdorff spaces, Closed Diagonal Theorem (Delta is closed in X x X iff X is T2), classical separation counterexamples (Line with Two Origins, Zariski topology), Urysohn's Lemma with complete proof via dyadic rational open chains, Tietze Extension Theorem, Urysohn Metrization Theorem, compactness and finite subcovers, Finite Intersection Property (FIP) characterization, compact subsets of Hausdorff spaces are closed, compact Hausdorff spaces are normal, metric compactness characterizations (sequential compactness, limit point compactness, Lebesgue Covering Lemma, total boundedness), locally compact spaces and Alexandroff one-point compactification alpha(X) = X union {infinity}, Tychonoff's Theorem for arbitrary Cartesian products via Alexander's Subbase Theorem, connectedness and clopen sets, continuous image preservation, Intermediate Value Theorem, connected components, closures of connected sets, path-connectedness, the Topologist's Sine Curve (connected but not path-connected), locally connected and locally path-connected spaces, and preservation of connectedness under arbitrary Cartesian products. Features 8 interactive 60 FPS Canvas simulations and 24 tiered solved examination problems with complete line-by-line mathematical proofs.",
        "units": processed_units
    }

    # Verify strictly zero course numbers
    json_str = json.dumps(course_data, ensure_ascii=False, indent=2)
    course_code_matches = re.findall(r'MTH[\s-]*\d+', json_str, re.IGNORECASE)
    if course_code_matches:
        raise ValueError(f"STRICT ERROR: Prohibited course codes detected in data: {course_code_matches}")

    out_file = "topology-data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// General Topology Master Textbook Data File\n")
        f.write("// STRICT CONSTRAINT: ZERO COURSE NUMBERS OR CODES PERMITTED\n")
        f.write("window.COURSE_DATA = ")
        f.write(json_str)
        f.write(";\n")

    print(f"Successfully generated {out_file} with {len(processed_units)} units, "
          f"{sum(len(u['sections']) for u in processed_units)} sections, and "
          f"{sum(len(u['problems']) for u in processed_units)} solved problems.")

if __name__ == "__main__":
    assemble_top_data()
