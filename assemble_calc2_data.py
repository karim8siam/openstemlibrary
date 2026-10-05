import json

sim_map = {
    1: ("u1-sec4", "sim_calc2_reduction"),
    2: ("u2-sec2", "sim_calc2_riemann"),
    3: ("u3-sec3", "sim_calc2_solids"),
    4: ("u4-sec3", "sim_calc2_polar"),
    5: ("u5-sec1", "sim_calc2_improper"),
    6: ("u6-sec4", "sim_calc2_gamma_beta"),
    7: ("u7-sec4", "sim_calc2_power_series"),
    8: ("u8-sec2", "sim_calc2_taylor"),
}

units = []

for u_num in range(1, 9):
    fn = f"calc2_u{u_num}.json"
    with open(fn, "r", encoding="utf-8") as f:
        u_data = json.load(f)

    sec_id, sim_id = sim_map[u_num]
    u_data["simulations"] = [sim_id]

    for s in u_data["sections"]:
        if s.get("id") == sec_id:
            s["simulation"] = sim_id
            s["simulations"] = [sim_id]

    u_data["id"] = f"unit{u_num}"
    u_data["unitId"] = f"unit{u_num}-calc2"
    u_data["number"] = u_num
    u_data["unitNumber"] = u_num
    u_data["title"] = u_data.get("unit_title", u_data.get("title", ""))
    u_data["leadSummary"] = u_data.get("unit_subtitle", u_data.get("leadSummary", ""))

    with open(fn, "w", encoding="utf-8") as f:
        json.dump(u_data, f, indent=2, ensure_ascii=False)

    units.append(u_data)

course_data = {
    "courseId": "calculus-2",
    "courseTitle": "Calculus II: Integral Calculus, Geometric Applications, Polar Coordinates, Special Functions & Infinite Series",
    "courseDescription": (
        "An exhaustive, university honors-level digital textbook and interactive calculus laboratory covering single-variable integral calculus and mathematical analysis: "
        "Techniques of integration (repeated integration by parts, tabular integration, rational fraction decomposition over linear and irreducible quadratics via Heaviside cover-up, "
        "powers and products of trigonometric functions, universal Weierstrass half-angle substitution t = tan(x/2), successive reduction recurrence relations for sinⁿx, cosⁿx, secⁿx, "
        "and Wallis' infinite product for π/2); Darboux upper and lower sums, mesh partitions, Cauchy-Riemann integrability criterion, Riemann sums (Left, Right, Midpoint, Trapezoidal rules), "
        "Mean Value Theorem for definite integrals, Cauchy-Schwarz integral inequality, rigorous ε-δ proofs of the First and Second Fundamental Theorems of Calculus, and the general Leibniz integral rule for differentiation under the integral sign; "
        "Cartesian geometric applications: planar area between intersecting curves via vertical (dx) and horizontal (dy) slicing, volumes of revolution via circular disks and annular washers, "
        "cylindrical shells around non-origin axes, general volume by parallel slicing via Cavalieri's principle, arc length of smooth Cartesian and parametric curves, surface area of revolution, "
        "and the Centroid Theorems of Pappus; Graphing in polar coordinates: coordinate frame transformations, symmetries, curve tracing for cardioids, limaçons, rose curves, and lemniscates, "
        "polar tangents and angle ψ between radius vector and tangent tan(ψ) = r/(dr/dθ), polar sector area integration, polar arc length ds = √(r² + (r')²) dθ, and polar surfaces/volumes of revolution; "
        "Improper integrals: Type I infinite intervals and the p-test, Type II unbounded integrand singularities, Cauchy Principal Value (P.V.), Direct and Limit Comparison tests, absolute vs conditional convergence, "
        "Dirichlet's and Abel's tests for oscillating improper integrals, and the Dirichlet sinc integral ∫₀^∞ (sin x)/x dx = π/2; Special functions: Euler's Gamma function Γ(z), fundamental recurrence Γ(z+1) = zΓ(z), "
        "factorial interpolation, half-integer values Γ(1/2) = √π, Euler's reflection formula Γ(z)Γ(1-z) = π/sin(πz), Legendre duplication, Euler's Beta function B(p, q), multi-dimensional transformation proof of B(p, q) = Γ(p)Γ(q)/Γ(p+q), "
        "and n-dimensional Euclidean ball volume Vₙ(R); Infinite series: Cauchy convergence criterion, non-negative tests (Maclaurin-Cauchy Integral test, Comparison tests, d'Alembert Ratio test, Cauchy Root test), "
        "Leibniz alternating series test and truncation error bounds, Riemann Rearrangement Theorem, power series, Cauchy-Hadamard theorem for radius of convergence R = 1/limsup ⁿ√|cₙ|, and term-by-term differentiation and integration theorems; "
        "and Taylor & Maclaurin polynomials: higher-order jet interpolation, Taylor's theorem with Lagrange, Cauchy, and Integral forms of the remainder, high-precision numerical error budgeting, non-elementary integral evaluations, "
        "and applications across relativistic mechanics (Newtonian kinetic energy limit and first relativistic quantum perturbation), economics (Arrow-Pratt risk aversion), and biological growth models. "
        "Accompanied by 8 interactive 60 FPS Canvas visualizers and 24 tiered solved university examination problems."
    ),
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

with open("calculus-2-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"calculus-2-data.js created successfully with {len(units)} units!")
