# -*- coding: utf-8 -*-
"""
generate_nt_data.py
Assembles all 8 units into number-theory-data.js
Ensures STRICT ZERO course codes or numbers anywhere in data.
"""

import json
import re
from build_nt_unit1 import get_unit1
from build_nt_unit2 import get_unit2
from build_nt_unit3 import get_unit3
from build_nt_unit4 import get_unit4
from build_nt_unit5 import get_unit5
from build_nt_unit6 import get_unit6
from build_nt_unit7 import get_unit7
from build_nt_unit8 import get_unit8

def assemble_nt_data():
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
        1: ("1.2", "sim_nt_euclidean_bezout"),
        2: ("2.4", "sim_nt_continued_fractions_pell"),
        3: ("3.3", "sim_nt_chinese_remainder_crt"),
        4: ("4.4", "sim_nt_primitive_roots_indices"),
        5: ("5.4", "sim_nt_arithmetic_functions_sigma"),
        6: ("6.4", "sim_nt_mobius_ramanujan"),
        7: ("7.1", "sim_nt_pythagorean_fermat_descent"),
        8: ("8.5", "sim_nt_sums_of_squares_lagrange"),
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
            "unitId": f"unit{u_idx}-nt",
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
        "courseTitle": "Theory of Numbers: Divisibility, Congruences, Arithmetical Functions & Diophantine Equations",
        "courseSubtitle": "Divisibility, Fundamental Theorem of Arithmetic, Continued Fractions, Pell's Equation, Linear & System Congruences, Classical Modular Theorems, Arithmetical Functions & Dirichlet Convolution, Möbius Inversion & Average Orders, Non-Linear Diophantine Equations & Quadratic Reciprocity, and Representations as Sums of Squares",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "Foundations of Abstract Algebra, Proof Techniques & Mathematical Induction",
        "description": "Exhaustive honors-level master digital textbook on elementary, algebraic, and analytic number theory: the divisibility relation, Division Algorithm, greatest common divisor, Bézout's identity, the Euclidean Algorithm, prime numbers and Euclid's infinitude theorem, Sieve of Eratosthenes, Fundamental Theorem of Arithmetic (unique factorization), $p$-adic valuations, finite simple continued fractions, infinite continued fractions and irrational numbers, best rational approximations, Dirichlet's Approximation Theorem, Pell's Diophantine equation $x^2 - d y^2 = 1$, fundamental unit, congruence relations and residue classes, linear congruences, system congruences and the Chinese Remainder Theorem, Fermat's Little Theorem, Euler's Totient Theorem, Wilson's Theorem, orders of elements, primitive roots and cyclic units modulo $n$, discrete logarithms (indices), multiplicative arithmetical functions, divisor function $d(n)$, sum-of-divisors function $\\sigma(n)$, Euler's phi function $\\varphi(n)$, Dirichlet convolution algebra, Dirichlet inverse, Möbius function $\\mu(n)$ and Möbius Inversion Formula, average orders of arithmetical functions (Dirichlet divisor problem), Ramanujan sums $c_q(n)$ and finite Fourier analysis, primitive Pythagorean triples $(m^2-n^2, 2mn, m^2+n^2)$, Fermat's Method of Infinite Descent, impossibility of $x^4 + y^4 = z^2$ and FLT for $n=4$, non-existence of right triangles with square area, quadratic residues, Legendre symbol, Euler's Criterion, Gauss's Lemma and the Law of Quadratic Reciprocity, sums of two squares (Fermat's Christmas Theorem), Gaussian integers $\\mathbb{Z}[i]$ and classification of Gaussian primes, general two-square characterization and Jacobi's divisor excess formula $r_2(n) = 4(d_1(n) - d_3(n))$, Euler's four-square identity, Hamilton quaternions $\\mathbb{H}$, Lagrange's Four-Square Theorem via minimal descent, and Legendre's Three-Square Theorem ($n \\ne 4^a(8b+7)$). Features 8 interactive 60 FPS Canvas simulations and 24 tiered solved examination problems with complete line-by-line mathematical proofs.",
        "units": processed_units
    }

    # Verify strictly zero course numbers
    json_str = json.dumps(course_data, ensure_ascii=False, indent=2)
    course_code_matches = re.findall(r'MTH[\s-]*\d+', json_str, re.IGNORECASE)
    if course_code_matches:
        raise ValueError(f"STRICT ERROR: Prohibited course codes detected in data: {course_code_matches}")

    out_file = "number-theory-data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Theory of Numbers Master Textbook Data File\n")
        f.write("// STRICT CONSTRAINT: ZERO COURSE NUMBERS OR CODES PERMITTED\n")
        f.write("window.COURSE_DATA = ")
        f.write(json_str)
        f.write(";\n")

    print(f"Successfully generated {out_file} with {len(processed_units)} units, "
          f"{sum(len(u['sections']) for u in processed_units)} sections, and "
          f"{sum(len(u['problems']) for u in processed_units)} solved problems.")

if __name__ == "__main__":
    assemble_nt_data()
