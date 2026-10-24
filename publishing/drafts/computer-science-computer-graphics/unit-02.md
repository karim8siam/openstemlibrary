# Computer Graphics — Unit 2: Raster graphics

**Incomplete editorial draft — not approved for publication.**

## 2.1 Clipping
### Clipping removes invisible geometry before raster work
Clipping determines which portion of a geometric primitive lies inside a specified region. In two-dimensional interfaces, a rectangular clip region prevents a scrolling panel from painting outside its viewport. In three-dimensional rendering, the viewing volume is bounded by planes, and primitives crossing a plane may need to be subdivided. Clipping is not the same as culling: culling may reject an entire object based on orientation or bounds, while clipping computes a visible portion of a primitive. An object can pass a bounding-box culling test yet still have individual triangles clipped by the near plane or screen edges.

For a line segment P(t) = P0 + t(P1-P0), where 0 <= t <= 1, rectangular clipping can be expressed as constraints on t. Suppose the horizontal coordinate must satisfy xmin <= x0+t dx <= xmax. If dx is positive, this imposes a lower bound (xmin-x0)/dx and an upper bound (xmax-x0)/dx. If dx is negative, the bounds reverse. The same procedure applies to y. Intersect all resulting intervals with [0,1]; an empty interval means the segment is invisible. This is the central idea behind parametric line clipping. It is robust and concise if zero direction components are handled explicitly.

Consider the segment from (-2,1) to (6,5) and a rectangle 0<=x<=4, 0<=y<=4. Its parametric form is x=-2+8t, y=1+4t. The left boundary requires t>=1/4; the right boundary requires t<=3/4. The bottom boundary is already satisfied for the original segment, while the top requires t<=3/4. The visible segment therefore runs from t=1/4 to t=3/4, with endpoints (0,2) and (4,4). This calculation is a good test because both the x and y boundaries influence the final result. A line parallel to the clip edge needs a different branch: if dx=0 and x0 lies outside the allowed x interval, no t can make the line visible.

Polygon clipping is more complicated because a polygon may acquire additional vertices where its edges cross a boundary. The Sutherland-Hodgman method processes a polygon against one half-plane at a time, keeping inside vertices and inserting edge intersections. It works particularly naturally for clipping against a convex region, such as a rectangular viewport. A concave subject polygon can still be clipped against convex boundaries, but the output representation may need care when disconnected regions occur. A general polygon clipping library must also address holes, coincident edges, numerical tolerances, and winding conventions.

In the GPU pipeline, clipping should be understood in homogeneous clip space. A common canonical condition has the form -w <= x <= w and -w <= y <= w, with depth bounds depending on the API. Performing the perspective divide first can lose the correct relationship between vertices on opposite sides of the camera. Attributes such as texture coordinates also require suitable interpolation for newly created vertices. A simple viewport-only example is useful for teaching but is not a complete replacement for homogeneous triangle clipping in a production renderer.

Numerical robustness is essential at boundaries. A point exactly on the edge should have a documented inclusion rule. Floating-point rounding may put a mathematically on-edge point slightly outside. Applying a large arbitrary epsilon to every comparison can produce cracks between neighboring primitives, so choose tolerances based on representation and algorithm. When testing a clipping function, include inside-inside, outside-outside, entering, exiting, tangent, parallel, and zero-length segments. An oracle based on independently solved t intervals is more trustworthy than a screenshot alone.

Clipping has downstream performance implications. Rejecting invisible primitives reduces raster work, but fine-grained clipping also costs computation. Modern pipelines balance coarse culling, clip-space clipping, and hardware raster rules. The correct strategy depends on scene complexity and geometry distribution. For a simple 2D scientific plot, a carefully implemented line clipper may be sufficient. For a large 3D mesh, rely on a validated graphics pipeline while retaining mathematical tests for custom geometry operations and visualization overlays.


## 2.2 Scan Conversion
### Scan conversion translates continuous primitives into discrete samples
A line or triangle is a continuous geometric object, while a raster image consists of discrete sample locations. **Scan conversion** decides which pixels or samples a primitive covers. The result depends on pixel-centre conventions and boundary inclusion rules, not just on the equation of the line. A mathematical line has zero area, so drawing a visible line requires a stroke-width or sample-coverage rule. Similarly, a triangle edge can pass exactly through a pixel centre; two adjacent triangles must agree about which one owns that sample to avoid gaps or double shading.

Bresenham's line algorithm illustrates incremental decision making. For a shallow line from integer (x0,y0) to (x1,y1) with dx>0 and 0<=dy<=dx, advance x by one pixel at each step and decide whether y should also increase. A decision variable can be updated using integer additions rather than repeated floating-point evaluation of the ideal line equation. One common initialization is d=2dy-dx. At each x step, choose the next y based on the sign of d, then update d by 2dy or 2(dy-dx). Other octants require coordinate swaps or sign handling. A production implementation should test all eight octants and define how endpoints are included.

For the line from (1,1) to (6,3), dx=5 and dy=2. Starting d=4-5=-1, the algorithm initially advances x without advancing y. Subsequent decisions produce a staircase approximating the ideal slope of 2/5. This is not a defect of the algorithm: it reflects the finite raster grid. What can be a defect is a mismatch between the line routine's endpoint rule and the triangle routine's edge rule, causing visible seams when a mesh is overlaid with outlines.

Triangles are the main workhorse of real-time rasterization because three vertices define a planar primitive and support interpolation of per-vertex attributes. An edge function for oriented points A and B can be written E_AB(P)=(Bx-Ax)(Py-Ay)-(By-Ay)(Px-Ax). Its sign tells which side of the directed edge contains P. A point lies inside a consistently oriented triangle when the three oriented edge tests satisfy the chosen inclusion rule. The edge functions are linear in screen coordinates, making incremental evaluation efficient across a tile or scanline.

Suppose A=(0,0), B=(4,0), C=(0,4), and P=(1,1). The oriented area determinant is 16, and the barycentric weights are 1/2 for A and 1/4 each for B and C. The point is strictly inside the triangle because all weights are positive. At P=(2,2), the weight for A becomes zero: the point lies exactly on edge BC. A top-left edge rule assigns such boundary samples consistently between adjacent triangles, preventing double coverage and cracks. Merely testing all weights >=0 for every triangle can count shared-edge samples twice.

Back-face culling uses orientation rather than sample coverage. In a fixed screen convention, a triangle's signed area indicates its winding. Reversing two vertices changes the sign. The renderer may discard triangles whose winding indicates that they face away from the camera, but the choice of clockwise versus counterclockwise front faces must match coordinate and viewport conventions. A negative-determinant model transform can reverse winding. Debugging a disappearing mesh therefore begins with checking both transform orientation and the pipeline's front-face setting.

Scan conversion is also a precision problem. Fixed-point edge functions can provide deterministic raster coverage, while floating-point implementations require careful attention to rounding. Very thin triangles may cover no pixel centres even though they have positive geometric area. That behavior is expected under point-sample coverage, not necessarily a geometry error. Multisample coverage can preserve some thin features by evaluating more sample locations per pixel. The right test suite uses known triangles, shared edges, reversed winding, degenerate triangles, and small subpixel translations to make these conventions visible.


## 2.3 Interpolation
### Interpolation carries vertex information across a primitive
After determining that a pixel sample lies inside a triangle, a renderer must estimate attributes such as color, texture coordinates, depth, normals, or world position at that sample. Barycentric coordinates provide a principled interpolation mechanism. If a point P in a nondegenerate triangle has weights lambda0, lambda1, lambda2 with each weight nonnegative and their sum equal to one, an attribute a may be interpolated as a(P)=lambda0 a0+lambda1 a1+lambda2 a2. Constant attributes remain constant, and affine functions of screen position are reproduced exactly. This property makes barycentric interpolation particularly natural for triangles.

Consider a triangle with vertex scalar values 10, 20, and 50 and a sample whose weights are (1/2,1/4,1/4). The interpolated value is 5+5+12.5=22.5. The calculation is straightforward, but the interpretation depends on the attribute. For a color stored in a nonlinear encoding, directly averaging encoded channel values is not equivalent to averaging light intensities. For a surface normal, the weighted vector may no longer have unit length and should often be normalized before lighting. For an integer material identifier, interpolation may be meaningless; the identifier should instead be flat-shaded or chosen according to an explicit categorical rule.

A major subtlety is **perspective-correct interpolation**. Screen-space barycentric interpolation is not generally correct for attributes that were linear on a triangle before perspective projection. Suppose vertex i has clip-space w_i and an attribute a_i. The perspective-correct value at a screen sample is [sum_i(lambda_i a_i/w_i)]/[sum_i(lambda_i/w_i)]. This expression interpolates a_i/w_i and 1/w_i linearly in screen space, then divides the results. When all w_i are equal, it reduces to ordinary barycentric interpolation. When depths differ significantly, using the affine screen-space formula can make textures slide or warp unnaturally across a surface.

For a numerical example, use two endpoints with screen weights 1/2 each, attributes 0 and 1, and clip w values 1 and 2. Naïve interpolation gives 0.5. Perspective-correct interpolation gives [(0.5*0/1)+(0.5*1/2)]/[(0.5/1)+(0.5/2)] = 0.25/0.75 = 1/3. The difference is large enough to notice in a textured corridor. This example uses two points along an edge for clarity; the same rational formula applies to all three vertices of a triangle.

Depth interpolation has special pipeline conventions. A GPU may interpolate a transformed depth value that is suitable for depth testing, while a scientific application may need the actual camera-space Z coordinate. Those are not interchangeable. Reconstructing view-space position from depth generally requires the projection parameters or inverse projection matrix. A depth buffer is a visibility data structure with a particular mapping, not automatically a metric range image. This distinction matters when a visualization overlays measurement annotations or performs screen-space effects.

Interpolated normals and tangents interact with the coordinate transformations discussed earlier. If a mesh is scaled nonuniformly, first transform normals appropriately using the inverse transpose of the model's linear part, then interpolate and normalize. If the tangent basis is used for normal mapping, it may need reorthogonalization to avoid skewed shading. Interpolation cannot repair an attribute that was expressed in the wrong coordinate frame. All vertices of a primitive should carry attributes in compatible spaces before interpolation begins.

Testing interpolation requires more than checking the triangle centroid. Verify that each vertex reproduces its own attribute, that weights sum to one, that a constant field remains constant, and that an affine field is reproduced. For perspective correction, choose unequal w values and compare against an independently computed rational expression. Reject zero or nonfinite w where division is undefined. Finally, remember that interpolation defines values *within* a primitive; smoothness across adjacent triangles also depends on whether their shared vertex attributes agree.


## 2.4 Antialiasing
### Antialiasing estimates coverage instead of pretending a pixel is a point
A continuous scene contains detail at infinitely many spatial frequencies, while an image stores finitely many samples. Sampling without sufficient filtering can produce jagged edges, moiré patterns, and shimmering motion. These are aliasing artifacts: high-frequency variations are misrepresented as lower-frequency patterns. The sampling theorem explains the issue for band-limited signals, but real polygon edges are discontinuities with unbounded frequency content. A practical renderer therefore estimates the contribution of a pixel's finite footprint rather than simply asking whether its centre is inside a shape.

For a binary black shape on a white background, the ideal pixel intensity under a box filter is related to the fraction of the pixel area covered by the shape. If a shape covers 30% of the pixel and the colors are interpreted in a linear light space, the pixel's linear intensity is a weighted average: 0.3 times shape intensity plus 0.7 times background intensity. A single centre sample can only choose one of the two colors and may be badly wrong near a boundary. More samples per pixel approximate coverage, but they do not make an arbitrary signal perfectly reconstructible.

**Supersampling** renders at a higher sample density and combines samples using a reconstruction filter. If a pixel uses a 2-by-2 grid, four subpixel locations contribute to the final value. If one of four is covered by a dark shape, a simple equal-weight box average produces 25% coverage. The estimate depends on sample locations; rotating or jittering the pattern can reduce systematic artifacts. The cost includes more sample evaluations and potentially more shading. Rendering the entire scene at twice the width and height creates four times as many pixel positions, which can be expensive for complex shading.

**Multisample antialiasing**, or MSAA, usually evaluates geometry coverage at several subpixel locations while allowing some shading work to be shared. It is especially effective for polygon silhouettes and shared edges, but it does not automatically eliminate aliasing inside a triangle from high-frequency textures or procedural shaders. **Temporal antialiasing** combines information from multiple frames, often using motion vectors and history buffers. It can improve stability but may introduce ghosting when history is invalid, motion is misestimated, or previously hidden surfaces become visible. No single technique solves all spatial and temporal aliasing.

Texture minification is a distinct but related problem. A checkerboard texture may contain dozens of checks inside one screen pixel. Sampling one texel can generate false large-scale patterns. Mipmaps precompute filtered versions at decreasing resolutions so the renderer can sample an appropriate level of detail. Anisotropic filtering improves quality when a pixel footprint stretches strongly in one texture direction, as on a road receding toward the horizon. A correct mipmap chain should be generated in a suitable color space and should handle alpha in a way consistent with the intended compositing model.

Filtering interacts with color representation. Most display-oriented RGB encodings are nonlinear. Averaging encoded values of black and white yields a midpoint code value that does not correspond to half the physical light intensity. For physically meaningful lighting and antialiasing, convert encoded colors to linear light before averaging and convert back for display. Similarly, premultiplied alpha avoids several edge artifacts when compositing partially transparent samples, but it must be used consistently throughout the pipeline. A halo around a transparent sprite often indicates a filtering or alpha-representation mismatch rather than a geometry defect.

A useful quantitative test is a slanted edge moving slowly by a fraction of a pixel per frame. Track the sum of covered area and the variance of output intensities as the edge moves. The total coverage should vary smoothly for a stable filter; abrupt changes reveal aliasing. Compare a centre-sampled result with a regular grid and a jittered grid under the same total sample budget. Include a checkerboard whose frequency gradually increases and a translucent edge over two backgrounds. The objective is not to declare one technique universally superior, but to identify which artifact each method addresses and which costs it introduces.


## 2.5 Integrated graphics investigation
### Integrated investigation: drawing a scientific contour over a heat map
A laboratory dashboard displays a measured temperature field as a colored raster and overlays a contour showing where the estimated temperature equals a chosen threshold. The contour is a continuous polyline, the heat map is sampled data, and the screen is a finite grid. A visually persuasive display can still misrepresent the measurement if these representations are mixed carelessly. Begin by documenting whether each heat-map value describes a pixel-centre sample, a cell average, or an interpolation of sparse sensor locations. These have different physical meanings even when drawn with similar colors.

Use a rectangular viewport with a nontrivial clipping boundary. Create a contour segment whose endpoints lie outside the panel but whose middle crosses it. Clip the segment using the parametric interval method before rasterization. For the segment from (-2,1) to (6,5) and panel 0<=x<=4, 0<=y<=4, the visible portion is (0,2) to (4,4). Verify the clipped endpoints numerically and check that resizing the panel updates the transform rather than changing the underlying scientific coordinates. If the horizontal axis is logarithmic, linear interpolation in raw measurement units is not equivalent to linear interpolation in display coordinates.

Draw the contour with a defined stroke width and antialiasing policy. Compare centre-sampled and four-sample coverage near diagonal edges. Then zoom out until the contour contains features narrower than one pixel. At this scale, retaining every tiny bend can create false visual noise. A responsible visualization may simplify the contour geometrically, increase stroke width for legibility, or provide an interactive zoom control. It should not silently alter the reported temperature threshold. The rendering technique and the scientific interpretation must remain separate.

Now interpolate the heat-map values. If a rectangular cell has corner measurements, bilinear interpolation can estimate a value at an interior point as a weighted combination of the four corners. However, this is a modeling assumption, not a direct measurement. It can conceal sharp discontinuities, and it may be inappropriate for categorical fields such as material type or sensor status. If the field is rendered as a triangulated mesh, the choice of diagonal changes the piecewise-linear interpolation within the cell. Compare both diagonals on a synthetic saddle field to make the modeling choice visible.

Color mapping adds another potential source of error. A rainbow palette may create perceptual boundaries where the data vary smoothly. A monotonic luminance palette can be easier to interpret for ordered scalar data, but its suitability depends on background, accessibility requirements, and display conditions. Record the numeric mapping from data values to colors and include a legend. Use a missing-data appearance that cannot be mistaken for a valid low value. Interpolate numerical data before mapping to a nonlinear color scale when the scientific objective is to estimate intermediate measurements.

Finally, build regression tests around a known synthetic field such as T(x,y)=2x+3y. Linear interpolation on any triangle should reproduce this affine field exactly within floating-point tolerance. A contour T=6 has a known straight-line equation 2x+3y=6. Verify the contour intersection points with cell edges independently. The pixel rendering may differ slightly with antialiasing settings, but the geometric contour and interpolated temperatures should not. This separation of geometric, numerical, and perceptual tests is a general method for validating scientific graphics.


## Worked problem: Clip a line to a rectangular viewport
Clip the segment from P0=(-2,1) to P1=(6,5) to the rectangle 0<=x<=4 and 0<=y<=4. Give the surviving parametric interval and endpoints, and identify the behavior for a parallel segment outside the rectangle.

### Parameterize
Write P(t)=P0+t(P1-P0)=(-2+8t,1+4t) for 0<=t<=1. Every rectangle boundary imposes an interval constraint on t.

### Intersect constraints
The x bounds give 0<=-2+8t<=4, or 1/4<=t<=3/4. The y bounds give 0<=1+4t<=4, or -1/4<=t<=3/4. Intersecting with [0,1] leaves [1/4,3/4]. The endpoints are P(1/4)=(0,2) and P(3/4)=(4,4).

### Check degenerate direction
For a vertical line x=c, dx=0. If c lies outside [0,4], the segment is entirely outside regardless of y. Do not divide by dx=0. If c is inside, the x constraint imposes no restriction on t; continue with y.

**Answer:** Visible interval t in [0.25,0.75], endpoints (0,2) and (4,4).

## Worked problem: Compute barycentric interpolation at a sample
For the triangle A=(0,0), B=(4,0), C=(0,4), find barycentric weights at P=(1,1). Vertex temperatures are 10, 20, and 50. Calculate the interpolated temperature and explain the interpretation.

### Derive the weights
Since P=lambdaA A+lambdaB B+lambdaC C, x=4 lambdaB and y=4 lambdaC. Thus lambdaB=1/4 and lambdaC=1/4. The sum-to-one condition gives lambdaA=1/2. All weights are positive, so the point is inside.

### Interpolate
The temperature estimate is (1/2)*10+(1/4)*20+(1/4)*50=5+5+12.5=22.5. This is a piecewise-affine model over the triangle, not an additional sensor measurement.

### Check consistency
At A the weights would be (1,0,0), giving 10; at B they would give 20, and at C they would give 50. The weights sum to one, so adding a constant to all vertex temperatures would add the same constant to the estimate. A discontinuous physical field could invalidate the interpolation assumption.

**Answer:** Barycentric weights (0.5,0.25,0.25); estimated temperature 22.5.

## Worked problem: Distinguish coverage sampling from physical brightness
A dark shape covers exactly one of four equally weighted subpixel sample locations in a pixel. Assume the shape has linear-light intensity 0 and the background intensity 1. Compute the four-sample average. Then explain why averaging gamma-encoded channel values can produce a different physical result.

### Define the sampling estimator
For a four-sample equal-weight box estimate, intensity is the sum of four sample intensities divided by four. Three samples see the white background and one sees the dark shape.

### Calculate
The estimated linear intensity is (0+1+1+1)/4=0.75. This represents a discrete estimate of 25% dark-shape coverage and 75% white-background coverage. A different sample arrangement could give a different estimate for the same true area.

### Explain color-space limitations
Display RGB code values are typically nonlinear functions of light intensity. Averaging code values is not generally equivalent to averaging emitted or reflected light. A physically consistent filter converts encoded colors to linear light, averages there, then encodes for display. The numerical 0.75 is a linear intensity, not necessarily the final displayed code value.

**Answer:** Estimated linear-light intensity 0.75; conversion to display encoding must occur after linear-light averaging.
