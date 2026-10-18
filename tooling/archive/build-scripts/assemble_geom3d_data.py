import json

sim_map = {
    1: ("u1-sec3", "sim_geom3d_coords"),
    2: ("u2-sec2", "sim_geom3d_planes"),
    3: ("sec-geom3d-3-3", "sim_geom3d_skew_lines"),
    4: ("sec-geom3d-4-3", "sim_geom3d_spheres"),
    5: ("sec-geom3d-5-2", "sim_geom3d_cones_cylinders"),
    6: ("sec-geom3d-6-1", "sim_geom3d_conicoids"),
    7: ("sec-geom3d-7-3", "sim_geom3d_vector_products"),
    8: ("sec-geom3d-8-1", "sim_geom3d_spatial_apps"),
}

units = []

for u_num in range(1, 9):
    fn = f"geom3d_u{u_num}.json"
    with open(fn, "r", encoding="utf-8") as f:
        u_data = json.load(f)

    sec_id, sim_id = sim_map[u_num]
    u_data["simulations"] = [sim_id]

    for s in u_data["sections"]:
        if s.get("id") == sec_id:
            s["simulation"] = sim_id
            s["simulations"] = [sim_id]

    u_data["id"] = f"unit{u_num}"
    u_data["unitId"] = f"unit{u_num}-geom3d"
    u_data["number"] = u_num
    u_data["unitNumber"] = u_num
    u_data["title"] = u_data.get("title", "")
    u_data["leadSummary"] = u_data.get("description", "")

    with open(fn, "w", encoding="utf-8") as f:
        json.dump(u_data, f, indent=2, ensure_ascii=False)

    units.append(u_data)

course_data = {
    "courseId": "geometry-3d",
    "courseTitle": "Three-Dimensional Coordinate & Vector Geometry: Analytical Planes, Lines, Spheres, Quadric Conicoids, and Spatial Vector Calculus",
    "courseDescription": (
        "An exhaustive, university honors-level digital textbook and interactive 3D laboratory covering spatial coordinate geometry and vector analysis: "
        "Rectangular Cartesian coordinates in ℝ³, distance formula, internal and external section ratios, centroid of tetrahedra, direction cosines (l, m, n) and direction ratios (a, b, c), "
        "fundamental quadratic identity l² + m² + n² = 1, angle between two spatial directed lines, orthogonal projections, and coordinate transformations; "
        "Cartesian and vector planes: general linear equation Ax + By + Cz + D = 0, normal vector orientation, point-normal form, intercept form, normal (Hesse) form, "
        "plane passing through three non-collinear points via 4×4 determinants, angle between intersecting planes, orthogonal and parallel criteria, Hesse perpendicular distance from a point to a plane, "
        "planes bisecting dihedral angles, and bundles/pencils of planes through the line of intersection; "
        "Spatial straight lines: parametric, symmetrical, and general two-plane intersection forms, reduction algorithms from non-symmetrical to symmetrical systems, "
        "angle and intersection criteria, coplanarity determinant criterion, skew lines in space, full derivation of the shortest distance formula d = |(r₂ - r₁) · (d₁ × d₂)| / |d₁ × d₂|, "
        "and equations of the common perpendicular; "
        "The sphere in space: standard center-radius form, general quadratic equation x² + y² + z² + 2ux + 2vy + 2wz + d = 0, sphere through four non-coplanar points, diametral endpoint sphere, "
        "circular plane sections (center as foot of normal, radius r = √(R² - p²)), great circles vs small circles, tangent planes, orthogonality condition 2u₁u₂ + 2v₁v₂ + 2w₁w₂ = d₁ + d₂, "
        "radical plane S₁ - S₂ = 0, radical lines, radical centers, and coaxial systems; "
        "Cones and cylinders: homogeneous quadratic equations as quadric cones with vertex at the origin, general second-degree cone criteria via 4×4 discriminant determinants, "
        "right circular cones (vertex, axis direction cosines, semi-vertical angle α), cylindrical surfaces with generators parallel to a fixed vector, right circular cylinders, "
        "and Joachimsthal's enveloping cones and cylinders of spheres (S·S₁ = T²); "
        "Central and non-central conicoids: canonical classification of ellipsoids, hyperboloids of one sheet (doubly ruled surface families), hyperboloids of two sheets, "
        "elliptic paraboloids, hyperbolic paraboloids (doubly ruled saddle surfaces), tangent planes Ax x₁ + By y₁ + Cz z₁ = 1, condition of plane tangency, polar planes, conjugate diameters, "
        "and the director sphere x² + y² + z² = 1/A + 1/B + 1/C; "
        "Vector algebra in space: inner dot product, outer cross product, Levi-Civita permutation symbol, Lagrange's identity, scalar triple product [a, b, c] as oriented parallelepiped volume, "
        "tetrahedral volume V = 1/6 |[a, b, c]|, vector triple product a × (b × c) = (a·c)b - (a·b)c (BAC-CAB theorem), Jacobi's identity, and higher-order four-vector identities; "
        "and applications of vectors in spatial geometry: vector formulations of straight lines and planes, line-plane piercing point intersections, point-to-line distance via cross products, "
        "and the complete theory of reciprocal vector triads (a', b', c') satisfying aᵢ · a'ⱼ = δᵢⱼ and [a', b', c'] = 1/[a, b, c]. "
        "Accompanied by 8 interactive 60 FPS Canvas visualizers and 24 tiered solved university examination problems."
    ),
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

with open("geometry-3d-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"geometry-3d-data.js created successfully with {len(units)} units!")
