import json

sim_map = {
    1: ("u1-sec5", "calc1-trans-inverse-sim"),
    2: ("u2-sec4", "calc1-exp-log-hyperbolic-sim"),
    3: ("u3-sec2", "calc1-epsilon-delta-sim"),
    4: ("u4-sec4", "calc1-ivt-bisection-sim"),
    5: ("u5-sec1", "calc1-secant-tangent-sim"),
    6: ("u6-sec2", "calc1-implicit-slope-sim"),
    7: ("u7-sec1", "calc1-mvt-rolle-sim"),
    8: ("u8-sec4", "calc1-curve-optimization-sim"),
}

units = []

for u_num in range(1, 9):
    fn = f"calc1_u{u_num}.json"
    with open(fn, "r", encoding="utf-8") as f:
        u_data = json.load(f)

    sec_id, sim_id = sim_map[u_num]
    u_data["simulations"] = [sim_id]
    
    # assign simulation to the specific section
    for s in u_data["sections"]:
        if s.get("id") == sec_id:
            s["simulation"] = sim_id
            s["simulations"] = [sim_id]

    # ensure standard unit properties
    u_data["id"] = f"unit{u_num}"
    u_data["unitId"] = f"unit{u_num}-calc1"
    u_data["number"] = u_num
    u_data["unitNumber"] = u_num
    if "leadSummary" not in u_data and "description" in u_data:
        u_data["leadSummary"] = u_data["description"]

    # re-save JSON
    with open(fn, "w", encoding="utf-8") as f:
        json.dump(u_data, f, indent=2)

    units.append(u_data)

course_data = {
    "courseId": "calculus-1",
    "courseTitle": "Calculus I: Single-Variable Differential Calculus, Real Analysis Foundations & Optimization",
    "courseDescription": (
        "A rigorous, university honors-level digital textbook and computational laboratory covering single-variable "
        "differential calculus and elementary real analysis: Part A establishes analytical foundations across four units "
        "(real numbers, completeness, functions, algebraic transformations, piecewise operators, and bijectivity; "
        "transcendental functions, exponential and logarithmic bases, trigonometric unit circle geometry, and hyperbolic catenary mechanics; "
        "intuitive limits, one-sided limits, the Cauchy-Weierstrass ε-δ definition, squeeze theorem, and asymptotic infinities; "
        "three-part continuity criteria, topological classifications of discontinuities, the Intermediate Value Theorem IVT, "
        "root bisection algorithms, and the Extreme Value Theorem EVT). Part B explores differential mechanics, theorems, "
        "and optimization across four units (difference quotients, geometric secant-to-tangent limits, differentiability "
        "implying continuity, power rule proofs via binomial expansion, product, quotient, and chain rules via Carathéodory formulation; "
        "implicit differentiation, orthogonal trajectories, inverse function derivatives, and higher-order derivatives with Leibniz's product formula; "
        "Rolle's theorem, Lagrange Mean Value Theorem MVT, Cauchy generalized MVT, rigorous L'Hôpital's rule derivations across all "
        "indeterminate forms 0/0, ∞/∞, 0·∞, 1^∞, 0^0, and Taylor linear approximations; Fermat's stationary point theorem, "
        "First and Second Derivative Tests, concavity, points of inflection, the universal 7-step analytical curve sketching algorithm, "
        "applied geometric/physical optimization, and the related rates framework). Accompanied by 8 interactive 60 FPS geometric "
        "calculators and 24 tiered solved university examination problems (Foundational, Intermediate Exam, and Honors/Proof Challenge)."
    ),
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2) + ";\n"

with open("calculus-1-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"calculus-1-data.js created successfully with {len(units)} units!")
