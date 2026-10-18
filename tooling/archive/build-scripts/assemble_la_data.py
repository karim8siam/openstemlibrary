import json

sim_map = {
    1: ("u1-sec2", "sim_la_linear_systems"),
    2: ("u2-sec2", "sim_la_subspaces"),
    3: ("u3-sec2", "sim_la_span_independence"),
    4: ("u4-sec2", "sim_la_four_subspaces"),
    5: ("u5-sec2", "sim_la_transformations"),
    6: ("u6-sec2", "sim_la_eigen_diagonalization"),
    7: ("u7-sec2", "sim_la_inner_product_gram_schmidt"),
    8: ("u8-sec2", "sim_la_quadratic_forms"),
}

units = []

for u_num in range(1, 9):
    fn = f"la_u{u_num}.json"
    with open(fn, "r", encoding="utf-8") as f:
        u_data = json.load(f)

    sec_id, sim_id = sim_map[u_num]
    u_data["simulations"] = [sim_id]

    for s in u_data["sections"]:
        if s.get("id") == sec_id:
            s["simulation"] = sim_id
            s["simulations"] = [sim_id]

    u_data["id"] = f"unit{u_num}"
    u_data["unitId"] = f"unit{u_num}-la"
    u_data["number"] = u_num
    u_data["unitNumber"] = u_num
    u_data["title"] = u_data.get("title", "")
    u_data["leadSummary"] = u_data.get("description", "")

    with open(fn, "w", encoding="utf-8") as f:
        json.dump(u_data, f, indent=2, ensure_ascii=False)

    units.append(u_data)

course_data = {
    "courseId": "linear-algebra",
    "courseTitle": "Linear Algebra & Spectral Theory: Vector Spaces, Linear Transformations, Eigenvalues, Canonical Forms & Quadratic Systems",
    "courseDescription": (
        "An exhaustive, university honors-level digital textbook and interactive computational laboratory unifying abstract vector space theory, operator algebra, and matrix decompositions: "
        "Matrices and systems of linear equations: matrix algebra, row-echelon and reduced row-echelon forms, Gaussian and Gauss-Jordan elimination, elementary matrices, matrix inversion, LU decomposition, determinant theory via multilinear alternating forms, Laplace expansions, and Cramer's rule; "
        "Abstract vector spaces and subspaces: ten axioms over arbitrary fields, sub-vector spaces, closure criteria, intersection and direct sums of subspaces U ⊕ W, and quotient spaces V / W; "
        "Linear independence, spanning sets, bases, and dimension: linear combinations, span, minimal generating sets, maximal independent sets, the Steinitz Exchange Lemma, finite-dimensional basis theorem, dimension formula dim(U + W) = dim(U) + dim(W) - dim(U ∩ W), and infinite-dimensional spaces; "
        "The Fundamental Theorem of Linear Algebra and four fundamental subspaces: column space C(A), row space C(Aᵀ), null space N(A), left null space N(Aᵀ), orthogonal complements, Rank-Nullity Theorem dim V = rank(T) + nullity(T), and rank inequalities; "
        "Linear transformations, matrix representations, and change of basis: kernel, image, injectivity, surjectivity, isomorphism theorems, transition matrices P_{β→γ}, similarity transformations B = P⁻¹ A P, and trace and determinant invariance; "
        "Eigenvalues, eigenvectors, eigenspaces, and diagonalization: characteristic polynomial, algebraic vs geometric multiplicity, defectiveness, diagonalizability criteria, and the complete proof of the Cayley-Hamilton Theorem via adjugate polynomial matrices; "
        "Inner product spaces, orthogonality, adjoint operators, and the Spectral Theorem: Cauchy-Schwarz and triangle inequalities, Gram-Schmidt orthogonalization, QR factorization, least-squares normal equations, dual spaces V*, Riesz representation theorem, adjoint operators T*, self-adjoint (Hermitian), normal, and unitary operators, and the Real and Complex Spectral Theorems (orthogonal resolution of identity T = ∑ λᵢ Pᵢ); "
        "and canonical forms, bilinear, quadratic, and Hermitian forms: Schur's triangularization theorem, generalized eigenspaces, nilpotent operators and Jordan chains, Jordan Canonical Form (JCF), companion matrices and Rational Canonical Form, bilinear forms, congruence transformations B' = Pᵀ B P, Lagrange reduction by completing squares, Sylvester's Law of Inertia, definiteness classification and Sylvester's leading principal minors criterion, and complex Hermitian forms. "
        "Accompanied by 8 interactive 60 FPS Canvas visualizers and 24 tiered solved university examination problems."
    ),
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

with open("linear-algebra-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"linear-algebra-data.js created successfully with {len(units)} units!")
