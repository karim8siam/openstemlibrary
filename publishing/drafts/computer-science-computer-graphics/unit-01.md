# Computer Graphics — Unit 1: Geometry and transforms

**Incomplete editorial draft — not approved for publication.**

## 1.1 Coordinate Systems
### Coordinate frames describe a measurement, not an intrinsic location
A point is a geometric object, while a coordinate tuple is a description of that point relative to a chosen frame. In a two-dimensional image, the tuple (40, 20) might identify a pixel centre measured from the upper-left corner, with the vertical axis pointing down. In a mathematical Cartesian plane, the same tuple usually means forty units right and twenty units up from an origin. The tuples agree as strings of numbers but not as spatial claims. Every graphics interface should therefore specify an origin, axis directions, unit scale, handedness, and whether coordinates refer to pixel corners or centres. Missing any one of these conventions can create a half-pixel displacement, a mirrored object, or a depth test that behaves backward.

A **frame** consists of an origin O and basis vectors e1, e2, and, in three dimensions, e3. A point P with local coordinates (x,y,z) is represented in a common world frame by P = O + x e1 + y e2 + z e3. The local components depend on the frame; P does not. Vectors such as velocity or surface direction have no origin term: v = vx e1 + vy e2 + vz e3. Confusing points and directions is a frequent programming error because both are often stored as three floating-point numbers. A translation should move a point but leave a direction unchanged. Homogeneous coordinates encode this distinction by representing a point as (x,y,z,1) and a direction as (x,y,z,0).

For example, a robot-mounted camera reports a landmark at (2,1,0) metres in camera coordinates. If the camera origin is at (10,0,0) metres in world space and its local x-axis points along world y while local y points along negative world x, then the landmark's world position is (10,0,0) + 2(0,1,0) + 1(-1,0,0) = (9,2,0). Merely adding the camera origin to the raw tuple would produce (12,1,0), a plausible but incorrect position. This illustrates why a frame transformation is not just a numerical offset.

Graphics systems commonly distinguish **model**, **world**, **view**, **clip**, **normalized device**, and **viewport** coordinates. Model coordinates are convenient for authoring an object. World coordinates place multiple objects in a shared scene. View coordinates express the scene relative to a camera. Clip coordinates are the output of projection before division by the homogeneous w component. Normalized device coordinates are obtained after that division and clipping conventions depend on the graphics API. Finally, a viewport transform maps normalized positions into pixel positions. An application should document which stage a coordinate belongs to rather than use an ambiguous variable named `position` everywhere.

A basis need not be orthogonal, but nonorthogonal axes change how lengths and angles are computed. If a skewed two-dimensional basis has e1=(1,0) and e2=(1,1), the local vector (1,1) is the world vector (2,1), whose Euclidean length is sqrt(5), not sqrt(2). Orthogonal unit bases simplify dot products because coordinate dot products then match geometric dot products. When working with a general basis matrix B, use the metric B-transpose times B to compute squared lengths from local components. Treating all frames as orthonormal silently breaks lighting, collision, and geometry measurements.

A useful debugging exercise is to render three short, differently labeled axes at every important transform node and compare a known landmark in each space. Verify a round trip: transform a point from local to world, then apply the inverse and recover the original within a stated floating-point tolerance. Avoid exact equality for computed floating-point coordinates. The meaningful error measure depends on scene scale; an absolute error of one millimetre may be negligible in a city map but disastrous in a microfabrication model. A coordinate contract should state both the representation and the acceptable precision.


## 1.2 Affine Transforms
### Affine transformations and composition order
An affine transformation combines a linear map A with a translation t: p' = A p + t. Linear maps include rotations, scales, shears, and reflections. An affine map preserves straight lines, collinearity, and ratios of distances along a line, but does not generally preserve angles or lengths. The transformation of a rectangle into a parallelogram under shear is affine; a perspective projection that makes parallel railway tracks converge is not affine in ordinary Euclidean coordinates. These distinctions matter because an algorithm relying on metric distances cannot freely operate after arbitrary affine transformations.

In two dimensions, homogeneous coordinates let translation and linear transformations share a single 3-by-3 matrix. For column vectors, translation by (tx,ty) is represented by rows (1,0,tx), (0,1,ty), (0,0,1). A counterclockwise rotation through angle theta has rows (cos theta,-sin theta,0), (sin theta,cos theta,0), (0,0,1). Scaling by (sx,sy) uses diagonal entries sx, sy, and 1. The order of matrix multiplication matters: applying scale S and then translation T to a column vector means T S p, whereas S T p scales the translation itself. A rendering bug may therefore look like an incorrect pivot even when every individual matrix is correct.

Consider a local point (1,2). Scaling by (2,3) produces (2,6); translating by (5,-1) then produces (7,5). Reversing the operations gives translation first (6,1), followed by scaling (12,3). Both are mathematically valid compositions but answer different geometric questions. A developer should describe the intended order in words before writing the product. For a model that must rotate around a nonorigin pivot c, the usual column-vector composition is T(c) R T(-c). The inner translation moves the pivot to the origin, the rotation acts there, and the outer translation restores the pivot's position.

Rotation matrices have useful invariants. In two dimensions, the columns of a pure rotation form an orthonormal basis, R-transpose R = I, and determinant R = +1. A reflection has determinant -1. A scale can have a determinant with magnitude other than one, changing area by the absolute determinant. The determinant of a two-dimensional transform A is also the signed area scale factor. A triangle whose original signed area is three square units becomes a triangle of signed area six under a transform with determinant two. Negative determinant reverses orientation; this may change back-face culling and winding assumptions.

Normals require special care. Under a nonuniform scale, applying A directly to a surface normal usually does not preserve perpendicularity to transformed tangent vectors. The correct unnormalized transformed normal is proportional to inverse-transpose(A) times the original normal, provided A is invertible. Suppose a tangent is (1,1) and a normal is (1,-1). Scale x by two and y by one: the transformed tangent is (2,1). Directly scaling the normal gives (2,-1), whose dot product with the transformed tangent is three, not zero. Inverse-transpose scaling yields (1/2,-1), whose dot product with (2,1) is zero. Renormalize afterward if the lighting model expects unit normals.

A singular transformation, such as scaling x to zero, cannot be inverted. That is not merely an inconvenient software exception: information has been destroyed by flattening a dimension. In a scene graph, track whether a transform must support inverse queries before permitting a zero scale. For interactive selection, it may be safer to transform the picking ray into object coordinates only when the inverse exists; otherwise intersect geometry in world coordinates or explicitly reject the operation. Use double precision for accumulated large-world transformations when single-precision cancellation becomes visible, but still understand the GPU's precision and clipping stages.

A reliable affine-transform test suite should check identity, inverse round trips, noncommutativity, pivot invariance, and normal perpendicularity. Testing only a rotation of ninety degrees can hide sign mistakes because some matrix entries are zero or one. Add a general angle such as thirty-seven degrees and a nonuniform scale. Compare the output against independently calculated coordinates rather than simply applying the same function twice. A test that shares the production bug with its oracle can pass while the geometry remains wrong.


## 1.3 Projections
### Projection as a controlled loss of spatial information
A camera must convert three-dimensional geometry into a two-dimensional image. Under orthographic projection, parallel lines remain parallel and apparent size does not depend on distance from the camera. For a camera looking along its negative z-axis, an idealized orthographic map can simply retain (x,y) while discarding z. Under perspective projection, image coordinates depend on depth. With a pinhole camera, a point (X,Y,Z) in camera coordinates at positive forward depth Z maps to x=fX/Z and y=fY/Z on a virtual image plane in front of the pinhole. Here f is the focal length in the same physical units as X, Y, and Z. Different graphics conventions place the camera forward direction along negative z, but the underlying similar-triangle relationship is the same.

Perspective division is nonlinear in Euclidean coordinates. If two points lie at depths two and four with the same world-space horizontal coordinate, the nearer point appears twice as far from the image centre. This produces a useful depth cue but destroys ordinary Euclidean distance measurements in the image. For example, with f=2, a point (3,1,6) projects to (1,1/3). A point (3,1,3) projects to (2,2/3). Without knowing depth or additional constraints, the image coordinate alone cannot recover the original three-dimensional point: every point along the same viewing ray projects to the same image location.

Real graphics pipelines use a projection matrix that maps camera-space homogeneous coordinates into clip space. The pipeline then clips geometry against a viewing volume and divides x, y, and z by w to obtain normalized device coordinates. The precise z range and sign conventions vary between APIs and configurations. A tutorial that copies a projection matrix without stating the convention may render a scene that looks correct in x and y but has reversed or invalid depth. Developers should verify the mapping of the near plane and far plane numerically rather than assume that all APIs share one normalized depth interval.

The field of view determines how much of the scene is visible. For a symmetric pinhole camera, vertical field of view alpha and focal length measured in units of half the image height satisfy tan(alpha/2)=1/f. In a physical camera, the equivalent relation uses sensor height h: alpha = 2 arctan(h/(2f)). A larger focal length narrows the field of view when sensor size is fixed. Changing the viewport aspect ratio without updating horizontal and vertical scaling can stretch circles into ellipses. A useful check is to render a unit sphere and verify that its projected silhouette is circular when the pixel aspect ratio is one and the camera is configured consistently.

Depth precision is not uniformly distributed under a conventional perspective depth mapping. A typical projection makes stored depth vary approximately with 1/Z. If the near plane is set unnecessarily close to the camera and the far plane is very distant, finite depth-buffer precision may produce z-fighting between nearby surfaces. The correct remedy may be to move the near plane outward, use a reversed-depth scheme with suitable floating-point storage, or subdivide a huge world into more stable coordinate regions. Increasing the far distance without considering precision can degrade the image even though no object visibly moves.

Clipping and projection are separate conceptual operations. A triangle intersecting the near plane must be clipped in an appropriate homogeneous or camera space before perspective division; blindly dividing vertices behind the camera can generate enormous coordinates or inverted polygons. A renderer also must decide how to handle points at Z=0, where the pinhole formula is undefined. Robust software rejects or clips invalid geometry rather than allowing division by zero to contaminate later raster stages with infinities or NaNs.

Projection tests should include known points on the optical axis, points at multiple depths, near-plane crossings, and aspect-ratio changes. For a calibrated virtual camera, compare projected positions against the pinhole formula and confirm that doubling forward depth halves displacement from the principal point. Record the camera convention in the test itself. A perspective image may be visually plausible while the numerical camera model is inconsistent with the one used by a reconstruction or augmented-reality algorithm.


## 1.4 Hierarchical Models
### Hierarchical models turn local motion into coordinated motion
A hierarchical scene represents objects as nodes connected by parent-child relationships. Each node stores a transform relative to its parent, not necessarily a transform relative to the world. A child's world transform is obtained by composing transforms along the path from the root to the child. Under column-vector conventions, if a parent has world matrix Wp and a child has local matrix Lc, then the child's world matrix is Wc = Wp Lc. Reversing this multiplication generally changes the result. A robot hand is positioned relative to the forearm, which is positioned relative to the upper arm, which is positioned relative to the torso; editing the shoulder automatically moves the whole downstream chain.

Suppose a parent translates by (3,0) and then rotates its local frame counterclockwise by ninety degrees. A child has a local translation (2,0). Under a parent transform T(3,0) R(90 degrees), the child's local origin maps to (3,2), not (5,0). The child's offset is rotated because it is expressed in the parent's frame. This is precisely what makes a hierarchical model useful for articulated motion. If the intention were for the child to remain aligned with the world x-axis regardless of parent rotation, the application would need a different parenting arrangement or an explicit compensation transform.

A scene graph can contain more than transforms: geometry references, materials, lights, visibility flags, and bounds may be attached to nodes. It is important to distinguish a *tree* from a more general directed acyclic graph. A tree gives each node one parent and makes transform propagation straightforward. A graph with instancing can let several nodes reference the same geometry without duplicating vertex buffers. If a graph permits multiple parents for a transform node, the meaning of a single world matrix becomes ambiguous unless the instance path is included. Cycles must be rejected or handled with a separate constraint-solving model, because recursively composing a cycle has no finite topological order.

Efficient implementations mark affected nodes as dirty when a local transform changes. A renderer can then recompute world transforms only for nodes whose own local matrix or ancestor world matrix has changed. However, an incorrect dirty-propagation rule creates stale child positions. A safe initial implementation recomputes the whole tree each frame, verifies correctness, and only then adds caching with explicit invalidation tests. Complexity matters: visiting n nodes is O(n), but a naïve algorithm that repeatedly walks from each leaf to the root may perform much more work in a deep hierarchy.

Hierarchies also expose a difference between geometric relationships and animation constraints. A bone chain has a natural parent-child structure, but a character's foot staying planted on the floor is not guaranteed by forward kinematics. The latter is a constraint involving world-space contact. Inverse kinematics chooses joint parameters to satisfy such constraints approximately or exactly, subject to joint limits. A hand reaching a target may require solving a nonlinear optimization problem even though calculating its position from known joint angles is a straightforward sequence of matrix products.

A practical scene-graph contract should specify how transforms are composed, how scale is inherited, how visibility is propagated, and what happens when a node is reparented. Reparenting while preserving the child's world pose requires Lnew = inverse(WnewParent) WoldChild when the inverse exists. Reparenting while preserving local coordinates instead changes the world pose. Both behaviors are legitimate, but the user interface should make the choice explicit. Tests should cover a two-level chain, a deep chain, reparenting, a hidden ancestor, and a noninvertible parent.

For debugging, display the hierarchy beside the rendered view and highlight the exact matrix that changed. Give each node a stable identifier independent of its display name. Record whether the geometry origin is at a meaningful joint pivot or at an arbitrary import origin. Many apparently mysterious animation defects arise because the pivot is in the wrong frame. A small, carefully measured scene with one shoulder, one elbow, and one fingertip often diagnoses these issues faster than a large cinematic scene.


## 1.5 Integrated graphics investigation
### Integrated investigation: a camera mounted on a moving inspection arm
Imagine a manufacturing cell with a rotating base, a sliding carriage, and a camera attached to the carriage. A marker is fixed to a product on a conveyor. The engineering question is not merely whether the marker appears somewhere on the screen; it is whether a point measured in camera coordinates can be transformed into a reliable world-space location and projected back to a predicted pixel. Build a small scene with three transforms: world-to-base, base-to-carriage, and carriage-to-camera. Give every transform a documented direction. A symbol such as T_world_from_camera should mean that multiplying a camera-frame homogeneous point produces a world-frame point. A name like T_camera is too ambiguous for reliable integration.

Start with a marker whose world location is known. Use the inverse camera world matrix to obtain camera coordinates. Confirm that a point in front of the camera has a valid positive forward depth under the selected convention, then apply a pinhole projection. The resulting pixel coordinate requires focal length and principal point in pixel units: u = fx X/Z + cx and v = fy Y/Z + cy, possibly with a sign change for the image's downward vertical axis. These intrinsic parameters are not the same as the camera's rigid world pose, which is extrinsic. A calibration record should distinguish them. If the image is resized, the intrinsics in pixel units must be adjusted consistently.

Run three diagnostic perturbations. First, translate the carriage along its local axis and check that the marker's image motion matches the composed frame direction. Second, rotate the base while leaving the carriage extension fixed and verify that both the camera origin and orientation change. Third, change focal length without moving any object; projected positions should move relative to the principal point but reconstructed world geometry should not change. This separation helps distinguish a transform bug from a projection bug. An apparently correct rendered frame does not prove that the calibration is correct if multiple wrong assumptions cancel each other.

Measurement uncertainty is also part of the geometry. A small angular pose error can create a large positional error at long range. For a camera orientation error of 0.1 degrees, the approximate lateral ray displacement at ten metres is ten times tan(0.1 degrees), or about 17.5 millimetres. This is a first-order approximation, not a complete uncertainty propagation model. A professional system would account for intrinsic calibration error, lens distortion, timestamp misalignment, rolling shutter, and marker detection uncertainty. The idealized graphics projection is a baseline against which these effects can be studied.

Document a failure case: the marker crosses the near plane. The projected coordinate may diverge as depth approaches zero, and the geometry should be clipped rather than treated as a valid detection. Document another failure case: a nonuniformly scaled ancestor changes the camera's orientation basis in a way that no longer represents a rigid pose. Rigid camera calibration should normally use rotation and translation, not arbitrary shear. If scene data contain shear, extract a suitable orthonormal camera orientation deliberately instead of assuming the top-left 3-by-3 matrix is a pure rotation.

A reproducible report contains the original coordinates, the ordered matrices, the intermediate transformed points, the projected image coordinate, the convention for image axes, and a numerical tolerance. It also includes a round-trip test from camera to world and back. Such a report can be reviewed independently and reproduced without opening the rendering application. The main lesson is that coordinate correctness is a chain of contracts: changing one stage without updating the others can produce images that are attractive yet geometrically false.


## Worked problem: Transform a landmark through a rotated frame
A camera frame has world origin O=(10,0), camera x-axis e1=(0,1), and camera y-axis e2=(-1,0). A landmark has camera coordinates (2,1). Find its world coordinates, and recover the camera coordinates from the result. Explain why adding the origin to the tuple is wrong.

### State the mapping
A point expressed in the camera frame is P_world = O + x e1 + y e2. This is a change of coordinate description; the basis directions are part of the data. The origin affects points but not direction vectors.

### Calculate
Substitute x=2 and y=1: P_world=(10,0)+2(0,1)+(-1,0)=(9,2). The two basis vectors form an orthonormal frame. The displacement from the camera origin is (-1,2). Its dot product with e1 is 2; its dot product with e2 is 1.

### Verify and interpret
The recovered camera tuple is (2,1), matching the input. Naïvely adding (10,0) to (2,1) would give (12,1), which assumes the camera axes align with world axes. Check that the world displacement length sqrt(5) equals the camera displacement length sqrt(5), as required for a pure rotation.

**Answer:** World point (9,2); recovered local point (2,1).

## Worked problem: Scale, translate, and transform a normal
Apply a nonuniform scale S=diag(2,1) and then translation t=(5,-1) to point p=(1,2). A surface tangent is (1,1) with normal (1,-1). Find the transformed point and an unnormalized normal perpendicular to the transformed tangent.

### Separate points from vectors
An affine point transform is p’=Sp+t. Tangents transform by S without translation. Normals require S inverse transpose when S is invertible, because perpendicularity must be preserved.

### Calculate
Sp=(2,2), so p’=(7,1). The transformed tangent is (2,1). Since S inverse transpose=diag(1/2,1), the normal becomes (1/2,-1). Its dot product with the transformed tangent is 2(1/2)+1(-1)=0.

### Check the tempting mistake
Directly scaling the original normal would produce (2,-1), whose dot product with (2,1) is 3, not zero. Translation does not enter either direction calculation. The correct normal can be normalized by dividing by sqrt(1.25) when a unit normal is required.

**Answer:** Point (7,1); valid transformed normal (0.5,-1), with zero tangent dot product.

## Worked problem: Project two points at different depths
In an ideal pinhole camera with positive forward depth, focal length f=2, and principal point at the origin, project P=(3,1,6) and Q=(3,1,3). Explain why a single image coordinate cannot uniquely recover 3D depth.

### Write the camera equation
For a pinhole model, x=fX/Z and y=fY/Z for Z>0. The coordinates in this problem are in a virtual image plane, not yet in physical pixel units.

### Calculate
P projects to (2*3/6,2*1/6)=(1,1/3). Q projects to (2*3/3,2*1/3)=(2,2/3). Q is half as far away in forward depth and has twice the displacement from the image centre.

### Explain the ambiguity
For any positive scalar k, (kX,kY,kZ) projects to the same image coordinate because the scale cancels in X/Z and Y/Z. Depth requires additional information such as stereo geometry, known object dimensions, a depth sensor, or motion assumptions. Z=0 must be rejected or clipped.

**Answer:** P maps to (1,1/3); Q maps to (2,2/3); the viewing ray has infinitely many possible positive depths.
