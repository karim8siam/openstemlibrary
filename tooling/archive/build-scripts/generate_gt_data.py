# -*- coding: utf-8 -*-
"""
generate_gt_data.py
Assembles all 8 units into graph-theory-data.js
Ensures STRICT ZERO course codes or numbers anywhere in data.
"""

import json
from build_gt_unit1 import get_unit1
from build_gt_unit2 import get_unit2
from build_gt_unit3 import get_unit3
from build_gt_unit4 import get_unit4
from build_gt_unit5 import get_unit5
from build_gt_unit6 import get_unit6
from build_gt_unit7 import get_unit7
from build_gt_unit8 import get_unit8

def assemble_gt_data():
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
        1: ("1.3", "sim_gt_graph_builder"),
        2: ("2.3", "sim_gt_euler_hamilton"),
        3: ("3.4", "sim_gt_spanning_tree"),
        4: ("4.3", "sim_gt_connectivity_cuts"),
        5: ("5.3", "sim_gt_matrix_spectral"),
        6: ("6.4", "sim_gt_digraph_dag"),
        7: ("7.4", "sim_gt_planar_duality"),
        8: ("8.4", "sim_gt_coloring_flows"),
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
            "unitId": f"unit{u_idx}-gt",
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
        "courseTitle": "Graph Theory: Structures, Algorithms, Algebraic Representations & Network Flows",
        "courseSubtitle": "Eulerian & Hamiltonian Circuits, Trees, Connectivity, Matrix Representations, Planarity, Coloring & Network Flows",
        "credits": 3,
        "lectureHours": 45,
        "prerequisites": "Linear Algebra & Discrete Mathematics",
        "description": "Exhaustive honors-level master digital textbook covering the full breadth of graph theory: structural foundations, degree sequences, Handshaking theorems, Havel-Hakimi criterion, isomorphism invariants, walks, paths, Eulerian trails, Fleury's algorithm, Hamiltonian cycles, Dirac and Ore theorems, tree characterizations, distance metrics, Jordan's center theorem, Cayley's formula, Prüfer sequences, Kruskal and Prim MST algorithms, connectivity, cut-vertices, cut-sets, Whitney's inequality, Menger's theorems, incidence, circuit, cut-set and Laplacian matrices, walk counting via matrix powers, Kirchhoff's Matrix Tree Theorem, directed graphs, tournaments, Landau and Rédei theorems, DAGs, Kahn's topological sorting, planar graphs, Euler's formula, Kuratowski and Wagner theorems, geometric duality, vertex coloring, chromatic number, Brooks' theorem, Five-Color theorem, chromatic polynomials, deletion-contraction recurrence, edge coloring, Vizing's theorem, network flows, Ford-Fulkerson algorithm, Max-Flow Min-Cut theorem, and Hall's Marriage Theorem. Features 8 interactive 60 FPS Canvas simulations and 24 tiered solved examination problems with line-by-line proofs.",
        "units": processed_units
    }

    js_content = "// OpenSTEM Digital Textbook - Graph Theory: Structures, Algorithms, Algebraic Representations & Network Flows\n"
    js_content += "// Master consolidated textbook combining Topological, Combinatorial, Algebraic, and Algorithmic Graph Theory\n"
    js_content += "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

    with open("graph-theory-data.js", "w", encoding="utf-8") as f:
        f.write(js_content)

    print("Successfully wrote graph-theory-data.js")
    print(f"Total Units: {len(processed_units)}")
    total_sections = sum(len(u['sections']) for u in processed_units)
    total_problems = sum(len(u['problems']) for u in processed_units)
    print(f"Total Sections: {total_sections}")
    print(f"Total Solved Problems: {total_problems}")

if __name__ == "__main__":
    assemble_gt_data()
