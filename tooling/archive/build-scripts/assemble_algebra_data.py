import json

sim_map = {
    1: ("sec_1_5", "algebra-complex-plane-sim"),
    2: ("sec_2_5", "algebra-demoivre-roots-sim"),
    3: ("sec_3_5", "algebra-viete-symmetric-sim"),
    4: ("sec_4_5", "algebra-descartes-multiplicity-sim"),
    5: ("sec_5_5", "algebra-series-cis-phasor-sim"),
    6: ("sec_6_5", "algebra-matrix-determinant-sim"),
    7: ("sec_7_5", "algebra-gauss-jordan-rref-sim"),
    8: ("sec_8_5", "algebra-leontief-economy-sim"),
}

units = []

for u_num in range(1, 9):
    fn = f"algebra_u{u_num}.json"
    with open(fn, "r", encoding="utf-8") as f:
        u_data = json.load(f)

    sec_id, sim_id = sim_map[u_num]
    u_data["simulations"] = [sim_id]

    for s in u_data["sections"]:
        if s.get("id") == sec_id:
            s["simulation"] = sim_id
            s["simulations"] = [sim_id]

    u_data["id"] = f"unit{u_num}"
    u_data["unitId"] = f"unit{u_num}-algebra"
    u_data["number"] = u_num
    u_data["unitNumber"] = u_num
    u_data["title"] = u_data.get("unit_title", u_data.get("title", ""))
    u_data["leadSummary"] = u_data.get("unit_subtitle", u_data.get("leadSummary", ""))

    with open(fn, "w", encoding="utf-8") as f:
        json.dump(u_data, f, indent=2, ensure_ascii=False)

    units.append(u_data)

course_data = {
    "courseId": "basic-algebra",
    "courseTitle": "Basic Algebra: Complex Numbers, Theory of Equations, Matrices & Leontief Systems",
    "courseDescription": (
        "An exhaustive, university honors-level digital textbook and interactive algebraic laboratory covering classical and modern algebraic foundations: "
        "Part A establishes the complex number field and trigonometric polynomials across two units (axiomatic construction of C, Argand plane geometry, "
        "modulus and complex conjugates, geometric and reverse triangle inequalities, polar and Euler exponential representations, complex loci for lines, "
        "circles, and Apollonian circles; De Moivre's theorem proof via induction, binomial expansions of cos(nθ) and sin(nθ), power reductions of cosⁿθ and sinⁿθ, "
        "geometry of n-th roots of complex numbers, primitive roots of unity, cyclic group structures, and cyclotomic polynomials). Part B establishes the "
        "theory of equations and series summation across three units (d'Alembert-Gauss Fundamental Theorem of Algebra, conjugate root pair theorem, Viète's "
        "formulas for cubic and quartic polynomials, elementary symmetric polynomials, Newton-Girard recursive power sum identities sₖ, polynomial Euclidean division, "
        "Horner's synthetic scheme, Descartes' rule of signs bounding real and non-real roots, root multiplicity derivative criteria, square-free GCD factorization, "
        "Tschirnhaus root shifts and transformations, reciprocal equations; mathematical induction, finite differences and telescoping sums, factorial polynomials, "
        "arithmetico-geometric progressions (AGP), partial fraction summation, and trigonometric series summation via the C + iS complex phasor method). "
        "Part C establishes matrix algebra, linear systems, and macroeconomic input-output analysis across three comprehensive units (matrix ring M_{m×n}, "
        "transpose, trace cyclic invariance, taxonomy of symmetric, skew-symmetric, orthogonal, Hermitian, skew-Hermitian, unitary, idempotent, and nilpotent matrices; "
        "axiomatic multilinear alternating determinants, Leibniz permutation formula, Laplace cofactor expansion, Cauchy-Binet multiplicativity det(AB) = det(A)det(B), "
        "classical adjugate inversion, Cramer's rule; elementary row operations, elementary matrices, row equivalence, Row Echelon Form, uniqueness of Reduced Row Echelon Form (RREF), "
        "row/column rank equality, Rank-Nullity theorem, Rouché-Capelli consistency theorem, Gauss-Jordan inversion [A | I] → [I | A⁻¹], block matrices and Schur complement inversion; "
        "and the Leontief Input-Output Economic Model: inter-industry technological consumption matrices, the Leontief balance equation (I - C)X = D, Hawkins-Simon economic viability conditions, "
        "Leontief inverse multipliers via Neumann series expansion, and the dual Leontief equilibrium price model). "
        "Accompanied by 8 interactive 60 FPS algebraic canvas calculators and 24 tiered solved university examination problems."
    ),
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

with open("basic-algebra-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"basic-algebra-data.js created successfully with {len(units)} units!")
