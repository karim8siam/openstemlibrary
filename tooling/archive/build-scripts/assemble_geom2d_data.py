import json

sim_map = {
    1: ("u1-sec5", "geom2d-coord-transform-sim"),
    2: ("u2-sec5", "geom2d-line-pair-sim"),
    3: ("u3-sec5", "geom2d-circle-radical-sim"),
    4: ("u4-sec5", "geom2d-conic-discriminant-sim"),
    5: ("u5-sec5", "geom2d-parabola-optics-sim"),
    6: ("u6-sec5", "geom2d-ellipse-conjugate-sim"),
    7: ("u7-sec5", "geom2d-hyperbola-asymptotes-sim"),
    8: ("u8-sec5", "geom2d-polar-conic-kepler-sim"),
}

units = []

for u_num in range(1, 9):
    fn = f"geom2d_u{u_num}.json"
    with open(fn, "r", encoding="utf-8") as f:
        u_data = json.load(f)

    sec_id, sim_id = sim_map[u_num]
    u_data["simulations"] = [sim_id]

    for s in u_data["sections"]:
        if s.get("id") == sec_id:
            s["simulation"] = sim_id
            s["simulations"] = [sim_id]

    u_data["id"] = f"unit{u_num}"
    u_data["unitId"] = f"unit{u_num}-geom2d"
    u_data["number"] = u_num
    u_data["unitNumber"] = u_num
    if "leadSummary" not in u_data and "description" in u_data:
        u_data["leadSummary"] = u_data["description"]

    with open(fn, "w", encoding="utf-8") as f:
        json.dump(u_data, f, indent=2)

    units.append(u_data)

course_data = {
    "courseId": "geometry-2d",
    "courseTitle": "Two-Dimensional Coordinate Geometry & Conic Sections: Systems of Coordinates, Pairs of Lines, Circles & Conics",
    "courseDescription": (
        "An exhaustive, university honors-level digital textbook and interactive geometric laboratory covering plane coordinate "
        "geometry and conic sections: Part A establishes analytical coordinate transformations, straight line pairs, and circular systems "
        "across four units (Cartesian metric space axioms, distance and section formulas, harmonic ranges, Euler line, shoelace polygon areas, "
        "polar coordinates, translation and rotation of axes via SO(2) orthogonal matrices, and quadratic invariants; homogeneous second-degree "
        "line pairs ax² + 2hxy + by² = 0, reality discriminant, angle between lines tan θ = 2√(h² - ab)/(a + b), perpendicularity (a + b = 0), "
        "joint angle bisectors (x² - y²)/(a - b) = xy/h, general second-degree line pairs via Δ = 0, intersection points, parallel line distance, "
        "and the homogenization theorem; standard, general, and diametric circles, tangency conditions, slope equations, Joachimsthal's pair of tangents "
        "SS₁ = T², chord of contact, reciprocal pole/polar theory, radical axis S₁ - S₂ = 0, radical center, orthogonal circles 2g₁g₂ + 2f₁f₂ = c₁ + c₂, "
        "and coaxial circle systems with limiting points). Part B presents the complete theory of conic sections across four comprehensive units "
        "(general second-degree equation x^T A x = 0, rigid motion invariants I₁, I₂, I₃ = Δ, classification taxonomy, center determination, "
        "eigenvalue canonical reduction λ₁X² + λ₂Y² + Δ/D = 0, and non-central parabolic reduction Y'² = 4AX'; in-depth study of the parabola y² = 4ax, "
        "parametric form (at², 2at), focal chord theorem t₁t₂ = -1, tangents, intersection of tangents, orthoptic directrix property, co-normal points, "
        "optical reflection property, and constant subnormal 2a; in-depth study of the ellipse x²/a² + y²/b² = 1, focal sum SP + S'P = 2a, auxiliary circle, "
        "eccentric angle, director circle x² + y² = a² + b², conjugate diameters and Apollonius' theorems CP² + CD² = a² + b² and area = 4ab, optical reflection, "
        "and focal perpendicular product p₁p₂ = b²; in-depth study of the hyperbola x²/a² - y²/b² = 1, focal difference |S'P - SP| = 2a, asymptotes y = ±(b/a)x, "
        "conjugate hyperbola 1/e₁² + 1/e₂² = 1, director circle x² + y² = a² - b², rectangular hyperbola x² - y² = a² with e = √2, rotation to asymptotic canonical form "
        "xy = c², and constant tangent-asymptote triangle area 2c²; universal polar conic equation l/r = 1 + e cos θ with focus at pole, unified eccentricity morphing, "
        "periapsis/apoapsis, polar tangents l/r = e cos θ + cos(θ - α), confocal orthogonal conics, and celestial orbital mechanics via Binet's equation and vis-viva energy). "
        "Accompanied by 8 interactive 60 FPS geometric canvas calculators and 24 tiered solved university examination problems."
    ),
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2) + ";\n"

with open("geometry-2d-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"geometry-2d-data.js created successfully with {len(units)} units!")
