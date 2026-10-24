# Computer Graphics — Unit 3: Shape representation

**Incomplete editorial draft — not approved for publication.**

## 3.1 Meshes
### Meshes represent surfaces through connectivity and geometry
A polygon mesh separates a set of vertex positions from the combinatorial rules describing which vertices form edges and faces. This distinction matters because two meshes can occupy exactly the same visible surface while having very different topology. A cube with six independent face patches may duplicate positions at corners so each face can carry a different normal. A welded cube can share eight geometric vertices across all six faces. The images can look identical under flat shading, but the connectivity affects smoothing, subdivision, collision, and editing operations.

A triangle mesh is particularly convenient for rendering. Each face references three vertex indices, and each triangle defines a plane unless its vertices are collinear. A triangle's oriented area vector is half the cross product of its two edge vectors. For vertices A, B, and C, the vector 0.5[(B-A) cross (C-A)] encodes both area and orientation. Its magnitude gives the triangle's area; its direction determines the face normal under a selected winding convention. A triangle with coincident or collinear vertices has zero area, so normalizing its cross product is undefined. Robust mesh loaders should detect such degeneracy instead of allowing NaNs into lighting calculations.

Topology can be stored in a simple index buffer or in a richer half-edge structure. An index buffer is compact and suits the GPU's triangle-processing pipeline. A half-edge structure represents each directed edge occurrence and can link it to the next edge around a face and its opposite across an adjacent face. It makes neighborhood queries, boundary detection, and local mesh editing more convenient. The cost is greater memory use and more invariants to maintain. For a static scanned object that will only be rendered, an indexed triangle list may be sufficient. For a geometry editor that repeatedly splits edges and traverses one-ring neighborhoods, half-edge connectivity may justify its complexity.

The phrase **manifold mesh** has a technical meaning. Locally, an interior point of a two-manifold surface resembles a disk, while a boundary point resembles a half-disk. In a typical closed, consistently oriented triangular two-manifold, every edge belongs to exactly two faces with opposite edge directions. A boundary edge belongs to one face. An edge shared by three faces is nonmanifold and can make normal orientation, inside-outside tests, and physical simulation ambiguous. Some real-world datasets legitimately contain nonmanifold junctions, so the right response is to classify and handle them, not automatically delete them.

Euler's relation offers a useful topology check for appropriate connected closed orientable surfaces: V-E+F=2-2g, where g is the genus, the number of handles. A tetrahedron has V=4, E=6, F=4, giving 2 and genus zero. A torus has Euler characteristic zero and genus one. The formula requires the stated topological assumptions; applying it to a mesh with boundaries or disconnected components without correction can produce a false diagnosis. Counting vertices by their array positions rather than geometric coincidence is also important: duplicated seam vertices can alter the combinatorial counts even when the surface looks welded.

Mesh quality influences numerical behavior. Extremely thin triangles have small areas and can make finite-element calculations ill-conditioned. In rendering, sliver triangles can lead to unstable derivatives, aliasing, and inefficient raster work. Surface reconstruction therefore balances fidelity to measured geometry with triangle aspect ratios, feature preservation, and topology. Uniformly increasing triangle count is not automatically an improvement. A mesh that follows important curvature and sharp edges with well-shaped elements can outperform a much denser mesh whose triangles are badly distributed.

For validation, compute face areas and normals independently, count boundary and nonmanifold edges, and inspect connected components. Test orientation by checking neighboring faces across each interior edge. Render the wireframe together with a shaded view to distinguish geometry problems from material problems. Keep a record of coordinate units and whether the mesh is meant to be watertight. A visually attractive object is not evidence that its topology is suitable for slicing, fluid simulation, or scientific measurement.


## 3.2 Curves
### Curves give controlled shape with fewer parameters
A curve representation should support evaluation at a parameter value, local editing, and predictable smoothness. A polyline connects a finite list of control points with straight segments; it is simple but has discontinuous tangent direction at most vertices. Parametric polynomial curves offer smooth trajectories and silhouettes. A cubic Bézier curve uses four control points P0, P1, P2, and P3, with B(t)=(1-t)^3 P0+3(1-t)^2 t P1+3(1-t)t^2 P2+t^3 P3 for t in [0,1]. The Bernstein basis weights are nonnegative on this interval and sum to one, so the curve lies inside the convex hull of its control points.

The endpoints of a cubic Bézier segment are B(0)=P0 and B(1)=P3. The endpoint derivatives are B'(0)=3(P1-P0) and B'(1)=3(P3-P2). Thus P1 controls the departure direction and P2 controls the arrival direction. A common mistake is to assume the curve passes through both interior control points; it generally does not. If P0=(0,0), P1=(1,2), P2=(2,2), and P3=(3,0), then B(1/2)=(1.5,1.5), not (1.5,2). The derivative at the midpoint is horizontal, giving the arch a smooth crest.

Two Bézier segments joined at a point can satisfy several kinds of continuity. **C0** continuity means they meet at the same position. **G1** continuity means their tangent directions align, though speeds may differ. **C1** continuity means the derivative vectors themselves match under the chosen parameterization. For two cubic segments, matching C1 derivatives at the join requires 3(P3-P2)=3(Q1-Q0) when the first segment ends at P3 and the second starts at Q0=P3. Moving a control point can preserve position continuity while breaking tangent continuity, producing a visible kink.

Splines use multiple polynomial pieces to model longer curves. B-splines provide local control: moving one control point influences only a limited parameter interval determined by the degree and knot vector. This contrasts with a single high-degree Bézier curve, where a control-point change can affect the entire curve. Nonuniform rational B-splines, or NURBS, add weights and can represent conic sections exactly under suitable configurations. Their flexibility comes with more parameters, knot-management rules, and numerical edge cases. A rendering system must still tessellate a spline into samples or segments for most raster pipelines.

Uniform sampling in parameter t does not generally yield equal arc-length spacing. On a Bézier curve, the speed is the magnitude of B'(t), which varies with t. The arc length from a to b is the integral of that speed. For arbitrary cubic control points this integral is usually approximated numerically. An animation that advances t at a constant rate may appear to speed up and slow down along the curve. To approximate constant world-space speed, precompute a monotonic arc-length table and invert it, or use an adaptive numerical method with an explicit error tolerance.

Subdivision of a Bézier curve through de Casteljau's algorithm provides a stable geometric construction. At a chosen t, interpolate consecutive control points, then interpolate the resulting points, and repeat until one point remains. The intermediate points also define two Bézier subcurves whose union is the original curve. This is useful for adaptive tessellation: recursively split segments where a flatness criterion indicates that a straight chord would deviate too far from the curve. A flatness tolerance expressed in world units may not be appropriate when the same object is viewed at different screen scales; a screen-space error criterion can better allocate detail.

Curve tests should check endpoints, endpoint derivatives, convex-hull containment, split consistency, and continuity at joins. Evaluate both polynomial and de Casteljau formulations for representative t values to catch implementation errors. Include repeated control points, nearly coincident points, and very large coordinates. For a motion path, test speed as well as position. Smoothness in a static image does not guarantee comfortable acceleration when the curve is used as an animation trajectory.


## 3.3 Surfaces
### Surfaces extend interpolation into two parameters
A parametric surface maps a two-dimensional parameter domain to three-dimensional space: S(u,v)=(x(u,v),y(u,v),z(u,v)). The parameters are not necessarily physical distances. A rectangular patch may use u and v in [0,1], while a sphere uses angular coordinates. Surface evaluation returns a position; partial derivatives Su and Sv describe tangent directions. Their cross product gives an oriented normal when the tangents are linearly independent. At a parameter singularity, such as a pole in spherical coordinates, the cross product may vanish even though the geometric surface itself is smooth.

A bilinear patch interpolates four corner points using S(u,v)=(1-u)(1-v)P00+u(1-v)P10+(1-u)vP01+uvP11. At u=v=1/2, the weights are all one quarter, so the patch position is the average of the four corners. Bilinear patches need not be planar. If three corners lie on z=0 and the fourth has z=1, the patch has z=uv and bends in three-dimensional space. Tessellating it into two triangles approximates the patch differently depending on which diagonal is chosen. This difference can matter in scientific visualization when interpolation is intended to represent a continuous field rather than just a visual decoration.

Tensor-product Bézier surfaces generalize Bézier curves. A bicubic patch uses a 4-by-4 grid of control points, with a cubic Bernstein basis in each parameter. It provides smooth shape control but requires continuity management across neighboring patches. For a shared boundary, matching positions along the entire edge is stronger than matching only the four corner points. Matching tangent behavior across the boundary requires relationships between neighboring rows or columns of control points. CAD systems often manage complex networks of patches, trims, and seams that require additional geometric bookkeeping.

An implicit surface instead describes points satisfying F(x,y,z)=0. A sphere of radius r centred at the origin satisfies x^2+y^2+z^2-r^2=0. When the gradient of F is nonzero, it is normal to the surface. Implicit descriptions are useful for constructive solid geometry, level sets, and signed-distance methods, but extracting a triangle mesh can require sampling and contouring. A signed distance field ideally returns the distance to the nearest surface with a sign distinguishing inside from outside; an arbitrary implicit function does not automatically have the metric properties of a signed distance field.

Subdivision surfaces offer another approach: start with a coarse polygon control mesh and repeatedly refine it. Under schemes such as Catmull-Clark, repeated refinement converges toward a smoother limit surface under appropriate conditions. The behavior near extraordinary vertices, where the number of neighboring faces differs from the regular case, requires particular care. Subdivision can produce smooth character models from manageable control cages, but it may round off intentionally sharp edges unless creases or boundary rules are specified. Refining a mesh increases polygon count and can expose poor topology rather than fixing it.

A surface can be geometrically smooth while its parameterization is distorted. For texture mapping, local stretching changes the relationship between a texel footprint and a screen pixel footprint. For numerical simulation, a distorted parameterization can affect quadrature and differential operators. The first fundamental form uses the dot products Su·Su, Su·Sv, and Sv·Sv to describe local lengths and angles in parameter space. Even if a graphics course does not require differential geometry in full, understanding that parameter distances differ from surface distances prevents many mistaken assumptions.

Validation should compare known analytic surfaces against sampled approximations. For a sphere, evaluate whether computed normals point radially outward and whether mesh vertices lie near the expected radius. For a bilinear patch, verify exact reproduction of all four corners and the centre average. Check for degenerate tangent frames before normalizing. For an implicit surface, evaluate the residual |F| at generated vertices and report a tolerance in appropriate units. A smooth shaded render can conceal gaps, inverted normals, and large geometric residuals.


## 3.4 Subdivision
### Subdivision trades geometric error against computational cost
A renderer cannot draw an infinitely detailed mathematical curve or surface directly as pixels without approximating it. Tessellation converts higher-level geometry into triangles or line segments. Uniform tessellation splits every region by the same rule; adaptive tessellation concentrates samples where curvature, displacement, or screen-space error is larger. The challenge is to measure error in a way that reflects the intended application. A silhouette viewed close to the camera may need more segments than the same silhouette viewed far away, while a finite-element simulation may prioritize curvature and element quality independent of screen resolution.

For a circle of radius r approximated by a regular n-sided polygon, the maximum radial deviation between an arc and its chord is r[1-cos(pi/n)]. As n grows, the small-angle approximation gives error about r*pi^2/(2n^2). This shows that doubling the segment count reduces the leading-order chord error by roughly a factor of four. It also gives a quantitative way to choose a segment count. For radius 100 pixels and allowable error 0.5 pixel, solve 100[1-cos(pi/n)]<=0.5. The minimum integer n is about 32, because 1-cos(pi/32) is approximately 0.004815, giving 0.4815 pixel. The exact bound and whether a polygon is sufficient depend on the raster and stroke rules.

Subdivision of triangle meshes is not the same as subdivision of curves. Splitting each triangle into four by inserting edge midpoints increases the face count fourfold at each uniform level. Starting from 200 triangles, three levels yield 200*4^3=12,800 triangles. This can improve sampling density but does not automatically smooth the surface; if new vertices are simple edge midpoints and remain on the original triangle planes, the geometry stays piecewise planar. Smoothing schemes move or reweight vertices according to neighboring connectivity, changing the limit shape and potentially shrinking features.

Adaptive tessellation needs a crack-avoidance policy. If two adjacent surface patches independently choose different edge subdivisions, one side may contain a vertex with no matching vertex on the other. The resulting T-junction can create gaps or shading artifacts under some rendering conditions. Solutions include enforcing compatible tessellation factors along shared edges, stitching mismatched boundaries, or using crack-free tessellation rules. The choice affects memory, implementation complexity, and the ability to stream geometry at different levels of detail.

A good error metric distinguishes object-space, world-space, and screen-space tolerances. An object-space deviation of one millimetre is meaningful for a manufactured part, while a screen-space deviation of one pixel is meaningful for an interactive preview. Perspective makes the relationship depth-dependent. For a surface patch at forward depth Z under a pinhole camera, a small transverse world displacement deltaX produces approximately f*deltaX/Z image displacement. Thus a fixed object-space tessellation can be oversampled at a distance and undersampled close up. A practical system may combine a geometric floor with a screen-space budget.

Subdivision also has a memory and bandwidth cost. Fourfold triangle growth at each level quickly overwhelms caches and GPU buffers. A level-of-detail system can select among precomputed meshes or generate tessellation dynamically. Changing levels abruptly may cause popping. Geomorphing, hysteresis, and carefully selected transition distances can reduce visual discontinuities. However, a technique that looks stable on a static screenshot may flicker during camera motion; performance and temporal tests are necessary.

For numerical testing, choose an analytic circle and compare chord deviation against the formula. For a planar mesh, verify that midpoint subdivision does not move vertices off the plane. For an adaptive surface, sample points on each generated edge and measure maximum deviation from the original patch. Count triangles, vertices, and memory bytes at each level. State whether error is measured at vertices, midpoints, or a denser sample set; testing only vertices can miss the maximum error between them. The result should be a reproducible quality-cost curve rather than a claim that a larger mesh is always better.


## 3.5 Integrated graphics investigation
### Integrated investigation: reconstructing a scanned turbine blade
A scanned turbine blade combines smooth aerodynamic surfaces, thin trailing edges, and manufacturing tolerances. The scanner returns noisy samples, often with uneven density and missing regions caused by occlusion. A graphics model intended for visualization may tolerate a smooth approximation, while a metrology model must preserve deviations relevant to inspection. Begin by stating the output contract: a watertight mesh for printing, a smooth CAD surface for redesign, or a faithful triangulated measurement for comparison. These are not interchangeable deliverables.

Clean the point cloud cautiously. Removing statistical outliers can eliminate isolated noise, but it may also remove legitimate thin features. Estimate normals using local neighborhoods and record how neighborhood size changes results. Small neighborhoods preserve detail but are sensitive to noise; large neighborhoods are more stable but blur sharp edges. A reconstructed surface should carry a measure of confidence where the scan is sparse or occluded. Filling a hole with an aesthetically smooth patch does not mean the underlying metal was measured there.

Represent the main blade body with a suitable mesh or spline surface. Use a half-edge structure if repeated local refinement and neighborhood traversal are required. Check for boundary loops, self-intersections, inverted faces, and nonmanifold edges. A mesh may appear watertight from the default camera view yet contain a small gap on the back. Validate topology numerically and inspect a cross-section through the trailing edge. If a repair algorithm changes the surface, record which vertices or patches were modified and by how much.

Choose tessellation based on the downstream objective. For a screen preview, an error budget in pixels may be enough. For dimensional inspection, a world-space deviation bound is more appropriate. Suppose the blade span is half a metre and the acceptable reconstruction deviation is 0.05 millimetre. A screen-space tolerance of one pixel says little about whether the geometry meets this requirement. Conversely, a mesh meeting the metrology tolerance may contain more triangles than necessary for a browser preview. Maintaining separate render and measurement representations can be more efficient and less misleading than forcing one mesh to serve every purpose.

A Bézier or B-spline patch can provide a compact, smooth approximation to the blade surface, but the fitting objective matters. Least-squares fitting minimizes aggregate squared residuals and can conceal a localized defect. A maximum-deviation constraint better reflects some manufacturing requirements but may be sensitive to outliers. Report both typical residuals and worst-case deviations, with confidence intervals or uncertainty estimates where justified. Compare residuals in the normal direction when that is the physically relevant dimension, rather than using arbitrary distances in the parameter domain.

Build three validation views: a wireframe with boundary and nonmanifold edges highlighted, a deviation heat map against the original samples, and a cross-sectional profile compared with a reference curve. The heat map must use a quantitative legend and should distinguish unmeasured regions from low-deviation regions. Add a test in which one vertex is intentionally displaced beyond tolerance and confirm that the deviation analysis detects it. Add another in which two triangles share a position but not an index and confirm that topology validation detects the seam if welding is required.

The investigation shows why shape representation is not merely a rendering choice. Mesh connectivity, curve parameterization, surface fitting, and subdivision influence the scientific claims that can be made from the resulting model. A successful graphics workflow records what was measured, what was interpolated, what was inferred, and what was altered for presentation. That record is as important as the final image when the model supports engineering decisions.


## Worked problem: Compute area and normal of a mesh triangle
A triangle has vertices A=(0,0,0), B=(2,0,0), and C=(0,3,0). Calculate its oriented area vector, area, and unit normal. What changes if B and C are swapped?

### Form edge vectors
Use B-A=(2,0,0) and C-A=(0,3,0). The oriented area vector is one half their cross product. The order of the vertices is essential because cross products reverse sign when their operands are exchanged.

### Calculate the geometry
The cross product (2,0,0) cross (0,3,0) equals (0,0,6). Half of it is (0,0,3), whose magnitude is 3 square units. The normalized face normal is (0,0,1).

### Check orientation and degeneracy
Swapping B and C changes the cross product to (0,0,-6), reversing the unit normal while preserving the area. If the vertices were collinear, the cross product would be zero and the unit normal undefined; the algorithm must detect that case.

**Answer:** Oriented area vector (0,0,3), area 3, normal (0,0,1); swapping B and C reverses the normal.

## Worked problem: Evaluate a cubic Bézier midpoint
A cubic Bézier curve has P0=(0,0), P1=(1,2), P2=(2,2), and P3=(3,0). Evaluate B(1/2), and find its initial and final derivatives.

### Write the Bernstein weights
At t=1/2, the cubic Bernstein weights are (1/8,3/8,3/8,1/8). These sum to one and are all nonnegative. The curve therefore lies inside the convex hull of its four control points.

### Calculate position
The x coordinate is (0+3+6+3)/8=12/8=1.5. The y coordinate is (0+6+6+0)/8=12/8=1.5. The midpoint is (1.5,1.5), below the two interior control points at height 2.

### Differentiate at endpoints
For a cubic Bézier curve, B-prime(0)=3(P1-P0)=(3,6), and B-prime(1)=3(P3-P2)=(3,-6). The endpoint tangent directions are therefore upward-right and downward-right. This matches the expected arch shape.

**Answer:** B(0.5)=(1.5,1.5); endpoint derivatives (3,6) and (3,-6).

## Worked problem: Choose a circle tessellation level
Approximate a circle of radius 100 screen pixels by an inscribed regular n-gon. Find a segment count that guarantees the maximum radial chord error is at most 0.5 pixel. Compare the approximate error for n=16 and n=32.

### Derive the bound
The maximum deviation occurs at the midpoint of a polygon edge: e(n)=r[1-cos(pi/n)]. Require 100[1-cos(pi/n)]<=0.5. The bound applies to geometric chord deviation before rasterization.

### Evaluate candidates
For n=16, cos(pi/16) is about 0.980785, so e is about 1.9215 pixels, which fails. For n=32, cos(pi/32) is about 0.995185, so e is about 0.4815 pixel, which passes. A smaller integer might pass, so evaluate the inverse-cosine bound if the minimum count is needed.

### State the minimum correctly
The exact inequality gives n>=pi/arccos(0.995), approximately 31.40, so the minimum integer is 32. Increasing n improves geometric fidelity but increases raster workload. The result assumes a regular inscribed polygon, a radius measured in pixels, and a fixed screen scale.

**Answer:** Minimum n=32; n=16 error about 1.9215 px, n=32 error about 0.4815 px.
