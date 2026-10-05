import json

sim_map = {
    1: ("u1-sec2", "sim_calc3_space_curves"),
    2: ("u2-sec2", "sim_calc3_curvature"),
    3: ("u3-sec3", "sim_calc3_tangent_planes"),
    4: ("u4-sec3", "sim_calc3_optimization"),
    5: ("u5-sec3", "sim_calc3_double_integrals"),
    6: ("u6-sec2", "sim_calc3_triple_integrals"),
    7: ("u7-sec3", "sim_calc3_vector_fields"),
    8: ("u8-sec3", "sim_calc3_flux_divergence"),
}

units = []

for u_num in range(1, 9):
    fn = f"calc3_u{u_num}.json"
    with open(fn, "r", encoding="utf-8") as f:
        u_data = json.load(f)

    sec_id, sim_id = sim_map[u_num]
    u_data["simulations"] = [sim_id]

    for s in u_data["sections"]:
        if s.get("id") == sec_id:
            s["simulation"] = sim_id
            s["simulations"] = [sim_id]

    u_data["id"] = f"unit{u_num}"
    u_data["unitId"] = f"unit{u_num}-calc3"
    u_data["number"] = u_num
    u_data["unitNumber"] = u_num
    u_data["title"] = u_data.get("title", "")
    u_data["leadSummary"] = u_data.get("description", "")

    with open(fn, "w", encoding="utf-8") as f:
        json.dump(u_data, f, indent=2, ensure_ascii=False)

    units.append(u_data)

course_data = {
    "courseId": "calculus-3",
    "courseTitle": "Calculus III: Multivariable Calculus, Vector Analysis, Curvature & Integral Theorems",
    "courseDescription": (
        "An exhaustive, university honors-level digital textbook and interactive multivariable laboratory merging advanced vector functions and multivariable analysis with multiple integration and vector field theory: "
        "Vector-valued functions of a single real variable, trajectory velocity, acceleration, speed, tangent lines, vector differentiation rules (dot and cross products), fundamental orthogonality theorem |r(t)| = c ⇒ r · r' = 0, "
        "arc length integral s(t) = ∫ |r'(u)| du, and natural unit speed reparameterization; "
        "Differential geometry of space curves: the moving Frenet-Serret trihedron (Unit Tangent T, Principal Normal N, Binormal B), osculating, normal, and rectifying planes, "
        "curvature κ in general parametric, Cartesian y = f(x), and polar forms, radius of curvature ρ = 1/κ, center of curvature and evolutes, torsion τ, complete derivation of the Frenet-Serret formulas, and tangential vs normal acceleration components; "
        "Multivariable differential calculus: functions of several variables, domains, contour maps and level surfaces, rigorous ε-δ limits in ℝⁿ, two-path test for non-existence of limits, polar squeeze limits, "
        "partial derivatives, geometric trace tangents, Clairaut's theorem on the equality of mixed partials (f_xy = f_yx), differentiability via linear increments, total differential dz, tangent planes to z = f(x, y), and linear approximation error bounds; "
        "Multivariable chain rules, implicit differentiation via partials, directional derivatives D_u f = ∇f · u, gradient vector ∇f, directions of steepest ascent and descent, gradient orthogonality to level sets, "
        "local extrema, critical points, the Hessian determinant discriminant D = f_xx f_yy - (f_xy)² and Second Derivative Test (local min, max, saddle point), absolute extrema on compact domains, and single- and dual-constraint Lagrange multipliers; "
        "Multiple integration: double Riemann sums, Fubini's theorem on rectangles, double integrals over Type I and Type II general planar regions, reversing the order of integration, laminar plate centroids and moments of inertia, "
        "polar coordinate double integrals with area element dA = r dr dθ, and the closed-form evaluation of the Poisson-Gaussian integral ∫ e^(-x²) dx = √π; "
        "Triple integrals: integration over general bounded spatial regions, Fubini's six permutations, solid volumes, variable density mass distributions, cylindrical coordinate triple integration dV = r dr dθ dz, "
        "spherical coordinate triple integration dV = ρ² sinφ dρ dφ dθ, and the general change of variables theorem in multiple integrals via 2D and 3D Jacobian determinants; "
        "Vector differential calculus and line integrals: scalar and vector fields, divergence ∇ · F (flux density/sources), curl ∇ × F (circulation/vorticity), solenoidal and irrotational vector fields, fundamental identities ∇ × ∇f = 0 and ∇ · (∇ × F) = 0, "
        "line integrals of scalar fields, line integrals of vector fields (work and circulation), conservative vector fields, scalar potentials, path independence, closed loops, and Green's theorem in the plane (standard and flux-divergence forms, planar area via line integrals); "
        "and surface integrals and integral theorems: parametric surfaces r(u, v), surface area element dS = |r_u × r_v| du dv, surface integrals of scalar fields, oriented surfaces and vector flux integrals ∬ F · dS, "
        "Stokes' Theorem ∮ F · dr = ∬ (∇ × F) · dS, independence of capping surfaces, Gauss' Divergence Theorem ∬ F · dS = ∭ (∇ · F) dV, physical applications to Gauss' Law in electrodynamics and fluid continuity equations, and the grand unification via the Generalized Stokes' Theorem for differential forms ∫_∂Ω ω = ∫_Ω dω. "
        "Accompanied by 8 interactive 60 FPS Canvas visualizers and 24 tiered solved university examination problems."
    ),
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

with open("calculus-3-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"calculus-3-data.js created successfully with {len(units)} units!")
