# -*- coding: utf-8 -*-
"""
generate_dm_data.py
Assembles all 8 units into discrete-mathematics-data.js
Ensures STRICT ZERO course codes or numbers anywhere in data.
"""

import json
import re
from build_dm_unit1 import get_unit1
from build_dm_unit2 import get_unit2
from build_dm_unit3 import get_unit3
from build_dm_unit4 import get_unit4
from build_dm_unit5 import get_unit5
from build_dm_unit6 import get_unit6
from build_dm_unit7 import get_unit7
from build_dm_unit8 import get_unit8

def assemble_dm_data():
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
        1: ("1.5", "sim_dm_logic_truth_tables"),
        2: ("2.5", "sim_dm_induction_towers"),
        3: ("3.5", "sim_dm_combinatorics_pigeonhole"),
        4: ("4.5", "sim_dm_recurrence_tree"),
        5: ("5.5", "sim_dm_karnaugh_map"),
        6: ("6.5", "sim_dm_euler_hamilton_graph"),
        7: ("7.3", "sim_dm_mst_kruskal_prim"),
        8: ("8.5", "sim_dm_network_max_flow"),
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
            "unitId": f"unit{u_idx}-dm",
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
        "courseTitle": "Discrete Mathematics: Mathematical Reasoning, Combinatorics, Graph Algorithms & Network Flows",
        "courseSubtitle": "Propositional & Predicate Logic, Inference & Proof Techniques, Mathematical Induction & Program Verification, Combinatorial Analysis & Pigeonhole Principle, Recurrence Relations & Generating Functions, Relations, Posets, Lattices & Boolean Algebra, Graph Theory & Hamiltonian Cycles, Trees & Shortest Path Algorithms, and Network Flows & Max-Flow Min-Cut Theorem",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "Introductory Calculus & Linear Algebra",
        "description": "Exhaustive honors-level master digital textbook on discrete mathematics: formal propositional logic and predicate calculus with alternating quantifiers, normal forms (CNF and DNF), Sheffer stroke functional completeness, deductive inference rules and resolution refutation proofs, direct, contrapositive, contradiction, and non-constructive existence proof techniques, the Principle of Mathematical Induction (weak and strong) and equivalence with the Well-Ordering Principle, structural induction on binary trees and formal program verification via Hoare logic, loop invariants, and well-founded termination ranking functions, foundational combinatorial enumeration principles, permutations, combinations, stars-and-bars integer compositions, multinomial coefficients and Vandermonde convolutions, Dirichlet's pigeonhole principle, generalized pigeonhole, Erdős-Szekeres theorem and Ramsey numbers, the Principle of Inclusion-Exclusion (PIE) for surjections and derangements, linear homogeneous and non-homogeneous recurrence relations, the Master Theorem for divide-and-conquer algorithms, ordinary generating functions (OGF) for Catalan sequences, exponential generating functions (EGF), binary relations, transitive closures and Warshall's algorithm, equivalence relations and set partitions, partially ordered sets (posets), Hasse diagrams and topological sorting, complete, distributive, and complemented lattices, Boolean algebra Huntington axiomatization and duality, 4-variable Gray-coded Karnaugh map loops, Quine-McCluskey tabular reduction, graph topology, Handshaking Lemma and Havel-Hakimi graphic sequence test, Eulerian trails and Hierholzer's cycle-splicing algorithm, Hamiltonian cycles, Ore's and Dirac's sufficiency theorems, Traveling Salesperson Problem complexity, characterization of trees, Cayley's labeled tree formula, Huffman prefix codes, Minimum Spanning Trees (MST) with Kruskal's DSU and Prim's algorithm, Dijkstra's single-source shortest path priority queue algorithm, Floyd-Warshall dynamic programming for all-pairs shortest paths with negative cycle detection, flow networks, flow conservation laws, residual capacities and augmenting paths, Edmonds-Karp BFS polynomial bound, Dinic's blocking flows, push-relabel schemes, the Max-Flow Min-Cut Theorem with full duality proof, and reductions to Maximum Bipartite Matching, Hall's Marriage Theorem, and Menger's Theorem for edge-disjoint paths. Features 8 interactive 60 FPS Canvas simulations and 24 tiered solved examination problems with complete line-by-line mathematical proofs.",
        "units": processed_units
    }

    # Verify strictly zero course numbers
    json_str = json.dumps(course_data, ensure_ascii=False, indent=2)
    course_code_matches = re.findall(r'MTH[\s-]*\d+|4107', json_str, re.IGNORECASE)
    if course_code_matches:
        raise ValueError(f"STRICT ERROR: Prohibited course codes detected in data: {course_code_matches}")

    out_file = "discrete-mathematics-data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Discrete Mathematics Master Textbook Data File\n")
        f.write("// STRICT CONSTRAINT: ZERO COURSE NUMBERS OR CODES PERMITTED\n")
        f.write("window.COURSE_DATA = ")
        f.write(json_str)
        f.write(";\n")

    print(f"Successfully generated {out_file} with {len(processed_units)} units, "
          f"{sum(len(u['sections']) for u in processed_units)} sections, and "
          f"{sum(len(u['problems']) for u in processed_units)} solved problems.")

if __name__ == "__main__":
    assemble_dm_data()
