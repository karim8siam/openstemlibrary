window.COURSE_DATA = {
  "courseId": "solid-state-physics",
  "courseTitle": "Solid State Physics: Crystal Structure, Lattice Dynamics, Electron Theory & Semiconductors",
  "courseDescription": "A rigorous, university-grade digital textbook covering the crystalline state, 14 Bravais lattices, X-ray diffraction, cohesive bonding, Madelung constants, phonons and lattice vibrations, Einstein and Debye heat capacities, Sommerfeld free electron theory, energy band gaps, Bloch electrons, effective mass, dielectric phenomena, plasmons, and semiconductor physics with 16 interactive 60 FPS simulations.",
  "units": [
    {
      "unitNumber": 1,
      "unitId": "unit1-crystal-structure",
      "title": "Crystal Structure, Symmetry & X-Ray Diffraction",
      "description": "Comprehensive foundation of crystallography: crystalline state, 14 3D Bravais lattices, primitive and conventional unit cells, Wigner-Seitz construction, Miller indices, atomic packing fractions, reciprocal lattice vectors, first Brillouin zone, Laue equations, and experimental X-ray diffraction methods.",
      "sections": [
        {
          "id": "ssp-1-1",
          "title": "The Crystalline State, Space Lattices & 14 Bravais Lattices",
          "simulation": "ssp-bravais-lattice-sim",
          "content": "<h4>1. The Crystalline State of Condensed Matter</h4>\n<p>Matter in the solid state displays a broad dichotomy in structural organization: <strong>amorphous solids</strong> (e.g., vitreous silica, amorphous polymers), where positional correlations decay rapidly beyond nearest-neighbor atomic separations exhibiting only <em>short-range order</em>, and <strong>crystalline solids</strong> (e.g., metals, diamond, semiconductor silicon, rock-salt), where atomic constituents reside in regular, periodic spatial arrays extending across macroscopic microscopic dimensions of $10^8$ unit intervals, characterized by rigorous <em>long-range translational order</em>.</p>\n\n<h4>2. Mathematical Definition of an Ideal Space Lattice</h4>\n<p>An ideal spatial lattice is a purely geometrical abstraction: an infinite three-dimensional periodic array of mathematical points in Euclidean space, where the physical and chemical environment surrounding any arbitrary lattice point $\\vec{R}'$ is strictly indistinguishable from that around any other point $\\vec{R}$. The translational position vector $\\vec{R}$ connecting the arbitrary origin to any point in the lattice is defined uniquely as an integer linear combination of three linearly independent primitive basis vectors $\\vec{a}_1, \\vec{a}_2, \\vec{a}_3$:</p>\n<div class=\"math-display\">\n$$\\vec{R} = n_1 \\vec{a}_1 + n_2 \\vec{a}_2 + n_3 \\vec{a}_3 \\quad (n_1, n_2, n_3 \\in \\mathbb{Z})$$\n</div>\n<p>A physical <strong>crystal structure</strong> is synthesized mathematically by convolving the geometrical space lattice with an identical group of atoms called the <strong>basis</strong> (or motif) situated at each lattice point:</p>\n<div class=\"math-display\">\n$$\\text{Crystal Structure} = \\text{Space Lattice} + \\text{Basis}$$\n</div>\n<p>If the basis comprises $j = 1, 2, \\dots, s$ atoms with respective atomic numbers $Z_j$, their spatial coordinates within the unit cell relative to the origin of that cell are defined by fractional vectors:</p>\n<div class=\"math-display\">\n$$\\vec{r}_j = x_j \\vec{a}_1 + y_j \\vec{a}_2 + z_j \\vec{a}_3 \\quad (0 \\le x_j, y_j, z_j < 1)$$\n</div>\n\n<h4>3. The 14 Three-Dimensional Bravais Lattices</h4>\n<p>In three spatial dimensions, spatial translational invariance combined with point group rotational and reflection symmetries yields precisely <strong>14 distinct Bravais lattices</strong>, partitioned among <strong>7 crystal systems</strong> characterized by the axial lengths ($a, b, c$) and interaxial angles ($\\alpha, \\beta, \\gamma$):</p>\n<ol>\n<li><strong>Cubic System ($a = b = c, \\alpha = \\beta = \\gamma = 90^\\circ$):</strong> Simple Cubic ($P$), Body-Centered Cubic ($I$), Face-Centered Cubic ($F$).</li>\n<li><strong>Tetragonal System ($a = b \\neq c, \\alpha = \\beta = \\gamma = 90^\\circ$):</strong> Simple Tetragonal ($P$), Body-Centered Tetragonal ($I$).</li>\n<li><strong>Orthorhombic System ($a \\neq b \\neq c, \\alpha = \\beta = \\gamma = 90^\\circ$):</strong> Simple ($P$), Base-Centered ($C$), Body-Centered ($I$), Face-Centered ($F$).</li>\n<li><strong>Hexagonal System ($a = b \\neq c, \\alpha = \\beta = 90^\\circ, \\gamma = 120^\\circ$):</strong> Simple Hexagonal ($P$).</li>\n<li><strong>Trigonal / Rhombohedral System ($a = b = c, \\alpha = \\beta = \\gamma < 120^\\circ \\neq 90^\\circ$):</strong> Primitive Rhombohedral ($R$).</li>\n<li><strong>Monoclinic System ($a \\neq b \\neq c, \\alpha = \\gamma = 90^\\circ \\neq \\beta$):</strong> Simple Monoclinic ($P$), Base-Centered Monoclinic ($C$).</li>\n<li><strong>Triclinic System ($a \\neq b \\neq c, \\alpha \\neq \\beta \\neq \\gamma \\neq 90^\\circ$):</strong> Primitive Triclinic ($P$).</li>\n</ol>"
        },
        {
          "id": "ssp-1-2",
          "title": "Primitive Cells, Wigner-Seitz Construction & Symmetry Operations",
          "content": "<h4>1. Primitive vs. Conventional Unit Cells</h4>\n<p>A <strong>unit cell</strong> is any volume of space that, when translated by the full set of lattice vectors $\\vec{R} = \\sum_i n_i \\vec{a}_i$, completely fills all space without overlapping or leaving voids. A unit cell is categorized as:</p>\n<ul>\n<li><strong>Primitive Cell:</strong> A unit cell having minimum volume that contains precisely <em>one</em> net lattice point ($N_{pts} = 1$). Its volume is calculated as the scalar triple product:\n<div class=\"math-display\">\n$$V_c = |\\vec{a}_1 \\cdot (\\vec{a}_2 \\times \\vec{a}_3)|$$\n</div></li>\n<li><strong>Conventional (Non-Primitive) Cell:</strong> A larger unit cell chosen intentionally to preserve and manifest the full rotational and reflection symmetry of the crystal system (e.g., BCC contains 2 lattice points, FCC contains 4 lattice points).</li>\n</ul>\n\n<h4>2. The Wigner-Seitz Primitive Cell Construction</h4>\n<p>The <strong>Wigner-Seitz cell</strong> is an invariant geometric construction providing a canonical primitive cell that exhibits the full point group symmetry of the Bravais lattice. The algorithm proceeds as follows:</p>\n<ol>\n<li>Select an arbitrary lattice point as the origin $\\vec{0}$.</li>\n<li>Draw straight line vectors connecting this origin to all neighboring lattice points $\\vec{R}_i$.</li>\n<li>Construct planes that perpendicularly bisect each of these vectors at $\\vec{R}_i / 2$.</li>\n<li>The smallest closed polyhedron enclosing the origin bounded by these bisecting planes constitutes the <em>Wigner-Seitz cell</em>.</li>\n</ol>\n<p>For an FCC lattice, the Wigner-Seitz cell is a <strong>rhombic dodecahedron</strong> (12 rhombic faces). For a BCC lattice, the Wigner-Seitz cell is a <strong>truncated octahedron</strong> (8 hexagonal faces and 6 square faces).</p>\n\n<h4>3. Crystallographic Symmetry Operations</h4>\n<p>The symmetry of a crystal consists of operations that map the periodic spatial arrangement onto itself:</p>\n<ul>\n<li><strong>Point Group Operations:</strong> Operations leaving at least one point invariant, comprising rotations $C_n = 2\\pi/n$ (where $n \\in \\{1, 2, 3, 4, 6\\}$ due to the crystallographic restriction theorem), reflections $\\sigma$, inversion $i$, and roto-inversions $S_n$. There exist precisely <strong>32 crystallographic point groups</strong>.</li>\n<li><strong>Space Group Operations:</strong> Combinations of point group operations with fractional and primitive lattice translations, including non-symmorphic <em>glide planes</em> (reflection plus fractional translation) and <em>screw axes</em> (rotation plus translation along the axis). In 3D space, there exist precisely <strong>230 crystallographic space groups</strong>.</li>\n</ul>"
        },
        {
          "id": "ssp-1-3",
          "title": "Miller Indices & Interplanar Spacing of Crystal Planes",
          "content": "<h4>1. Definition and Determination of Miller Indices $(hkl)$</h4>\n<p>A crystal plane is characterized by a set of three coprime integers $(hkl)$, known as its <strong>Miller indices</strong>, which specify its spatial orientation relative to the primitive or conventional crystal axes $\\vec{a}_1, \\vec{a}_2, \\vec{a}_3$:</p>\n<ol>\n<li>Determine the intercepts of the plane along the three crystallographic axes in units of lattice constants: $x_1 a, x_2 b, x_3 c$.</li>\n<li>Take the reciprocals of these fractional intercepts: $1/x_1, 1/x_2, 1/x_3$.</li>\n<li>Clear fractions by multiplying by their least common denominator to obtain the smallest coprime triplet of integers $(h, k, l)$. If an intercept is negative, say $-x_1$, the corresponding index is written with an overbar as $(\\bar{h}kl)$.</li>\n</ol>\n\n<h4>2. Mathematical Derivation of Interplanar Spacing $d_{hkl}$</h4>\n<p>Consider a family of parallel equidistant planes designated by Miller indices $(hkl)$. The distance of the first plane from the coordinate origin along the normal unit vector $\\hat{n}$ is the interplanar spacing $d_{hkl}$.</p>\n<p>In a <strong>Cubic crystal system</strong> ($a = b = c, \\alpha = \\beta = \\gamma = 90^\\circ$), the equation of a plane intersecting the axes at $a/h, a/k, a/l$ is:</p>\n<div class=\"math-display\">\n$$\\frac{x}{a/h} + \\frac{y}{a/k} + \\frac{z}{a/l} = 1 \\implies hx + ky + lz = a$$\n</div>\n<p>The perpendicular distance from the origin $(0,0,0)$ to this plane is given by analytical geometry:</p>\n<div class=\"math-display\">\n$$d_{hkl} = \\frac{|h(0) + k(0) + l(0) - a|}{\\sqrt{h^2 + k^2 + l^2}} = \\frac{a}{\\sqrt{h^2 + k^2 + l^2}}$$\n</div>\n<p>For a general <strong>Orthorhombic system</strong> ($a \\neq b \\neq c, \\alpha = \\beta = \\gamma = 90^\\circ$):</p>\n<div class=\"math-display\">\n$$\\frac{1}{d_{hkl}^2} = \\frac{h^2}{a^2} + \\frac{k^2}{b^2} + \\frac{l^2}{c^2}$$\n</div>\n<p>For a <strong>Hexagonal system</strong> ($a = b \\neq c, \\alpha = \\beta = 90^\\circ, \\gamma = 120^\\circ$):</p>\n<div class=\"math-display\">\n$$\\frac{1}{d_{hkl}^2} = \\frac{4}{3}\\left(\\frac{h^2 + hk + k^2}{a^2}\\right) + \\frac{l^2}{c^2}$$\n</div>"
        },
        {
          "id": "ssp-1-4",
          "title": "Simple Crystal Structures & Atomic Packing Factors",
          "content": "<h4>1. Atomic Packing Fraction (APF) Formalism</h4>\n<p>The <strong>Atomic Packing Fraction (APF)</strong> quantifies the volumetric efficiency with which hard spherical atoms of radius $R$ fill the unit cell volume $V_{cell}$:</p>\n<div class=\"math-display\">\n$$\\text{APF} = \\frac{N_{\\text{eff}} \\times V_{\\text{atom}}}{V_{\\text{cell}}} = \\frac{N_{\\text{eff}} \\times \\frac{4}{3}\\pi R^3}{V_{\\text{cell}}}$$\n</div>\n<p>where $N_{\\text{eff}}$ is the effective number of whole atoms inside the conventional unit cell.</p>\n\n<h4>2. Detailed Comparison of Canonical Metallic and Covalent Structures</h4>\n<ol>\n<li><strong>Simple Cubic (SC):</strong>\n<ul>\n<li>$N_{\\text{eff}} = 8 \\times (1/8) = 1$.</li>\n<li>Touching condition along edge: $a = 2R \\implies R = a/2$.</li>\n<li>$\\text{APF} = \\frac{1 \\times \\frac{4}{3}\\pi (a/2)^3}{a^3} = \\frac{\\pi}{6} \\approx 0.5236$ ($52.4\\%$). Coordination number $CN = 6$.</li>\n</ul></li>\n<li><strong>Body-Centered Cubic (BCC):</strong>\n<ul>\n<li>$N_{\\text{eff}} = 8 \\times (1/8) + 1 = 2$.</li>\n<li>Touching condition along body diagonal: $4R = \\sqrt{3}a \\implies R = \\frac{\\sqrt{3}}{4}a$.</li>\n<li>$\\text{APF} = \\frac{2 \\times \\frac{4}{3}\\pi \\left(\\frac{\\sqrt{3}}{4}a\\right)^3}{a^3} = \\frac{\\sqrt{3}\\pi}{8} \\approx 0.6802$ ($68.0\\%$). Coordination number $CN = 8$.</li>\n</ul></li>\n<li><strong>Face-Centered Cubic (FCC):</strong>\n<ul>\n<li>$N_{\\text{eff}} = 8 \\times (1/8) + 6 \\times (1/2) = 4$.</li>\n<li>Touching condition along face diagonal: $4R = \\sqrt{2}a \\implies R = \\frac{\\sqrt{2}}{4}a$.</li>\n<li>$\\text{APF} = \\frac{4 \\times \\frac{4}{3}\\pi \\left(\\frac{\\sqrt{2}}{4}a\\right)^3}{a^3} = \\frac{\\sqrt{2}\\pi}{6} \\approx 0.7405$ ($74.1\\%$). Coordination number $CN = 12$.</li>\n</ul></li>\n<li><strong>Hexagonal Close-Packed (HCP):</strong>\n<ul>\n<li>Stacking sequence: $ABABAB\\dots$ Ideal axial ratio: $c/a = \\sqrt{8/3} \\approx 1.633$.</li>\n<li>$N_{\\text{eff}} = 12 \\times (1/6) + 2 \\times (1/2) + 3 = 6$.</li>\n<li>$\\text{APF} = \\frac{\\pi}{3\\sqrt{2}} \\approx 0.7405$ ($74.1\\%$). Coordination number $CN = 12$.</li>\n</ul></li>\n<li><strong>Diamond Cubic Structure:</strong>\n<ul>\n<li>FCC lattice with a two-atom basis: $(0,0,0)$ and $\\left(\\frac{1}{4}, \\frac{1}{4}, \\frac{1}{4}\\right)$.</li>\n<li>$N_{\\text{eff}} = 8$ atoms. Touching condition along quarter body diagonal: $8R = \\sqrt{3}a \\implies R = \\frac{\\sqrt{3}}{8}a$.</li>\n<li>$\\text{APF} = \\frac{\\sqrt{3}\\pi}{16} \\approx 0.3401$ ($34.0\\%$). Coordination number $CN = 4$ (tetrahedral $sp^3$ coordination).</li>\n</ul></li>\n<li><strong>Ionic Structures (NaCl, CsCl, ZnS Zincblende):</strong>\n<ul>\n<li><strong>NaCl:</strong> FCC Bravais lattice of $\\text{Cl}^-$ with $\\text{Na}^+$ at $(1/2, 0, 0)$; $CN = 6:6$, $4$ formula units/cell.</li>\n<li><strong>CsCl:</strong> Simple cubic Bravais lattice with $\\text{Cs}^+$ at $(0,0,0)$ and $\\text{Cl}^-$ at $(1/2, 1/2, 1/2)$; $CN = 8:8$, $1$ formula unit/cell.</li>\n<li><strong>ZnS (Zincblende):</strong> FCC lattice of $\\text{S}^{2-}$ with $\\text{Zn}^{2+}$ occupying half the tetrahedral interstitial sites; $CN = 4:4$.</li>\n</ul></li>\n</ol>"
        },
        {
          "id": "ssp-1-5",
          "title": "Reciprocal Lattice, Brillouin Zones & X-Ray Diffraction",
          "simulation": "ssp-bragg-xray-diffraction-sim",
          "content": "<h4>1. Rigorous Definition of the Reciprocal Lattice</h4>\n<p>Given direct lattice primitive basis vectors $\\vec{a}_1, \\vec{a}_2, \\vec{a}_3$ with unit cell volume $V_c = \\vec{a}_1 \\cdot (\\vec{a}_2 \\times \\vec{a}_3)$, the corresponding <strong>reciprocal lattice primitive vectors</strong> $\\vec{b}_1, \\vec{b}_2, \\vec{b}_3$ are defined uniquely by the orthogonality relation:</p>\n<div class=\"math-display\">\n$$\\vec{a}_i \\cdot \\vec{b}_j = 2\\pi \\delta_{ij}$$\n</div>\n<p>Explicit vector formulas for the reciprocal basis vectors are:</p>\n<div class=\"math-display\">\n$$\\vec{b}_1 = 2\\pi \\frac{\\vec{a}_2 \\times \\vec{a}_3}{V_c}, \\quad \\vec{b}_2 = 2\\pi \\frac{\\vec{a}_3 \\times \\vec{a}_1}{V_c}, \\quad \\vec{b}_3 = 2\\pi \\frac{\\vec{a}_1 \\times \\vec{a}_2}{V_c}$$\n</div>\n<p>An arbitrary reciprocal lattice vector $\\vec{G}$ is expressed in terms of integer Miller components $(h, k, l)$:</p>\n<div class=\"math-display\">\n$$\\vec{G}_{hkl} = h \\vec{b}_1 + k \\vec{b}_2 + l \\vec{b}_3$$\n</div>\n<p><strong>Fundamental Theorems of the Reciprocal Lattice:</strong></p>\n<ol>\n<li>The reciprocal lattice vector $\\vec{G}_{hkl}$ is normal to the family of crystal planes $(hkl)$ in direct space.</li>\n<li>The magnitude of $\\vec{G}_{hkl}$ is inversely proportional to the interplanar spacing $d_{hkl}$:\n<div class=\"math-display\">\n$$|\\vec{G}_{hkl}| = \\frac{2\\pi}{d_{hkl}} \\implies d_{hkl} = \\frac{2\\pi}{|\\vec{G}_{hkl}|}$$\n</div></li>\n<li>The reciprocal lattice of an FCC direct lattice is a BCC reciprocal lattice, and vice-versa.</li>\n</ol>\n\n<h4>2. The First Brillouin Zone</h4>\n<p>The <strong>First Brillouin Zone (1st BZ)</strong> is the Wigner-Seitz primitive cell of the <em>reciprocal lattice</em>. It contains all wavevectors $\\vec{k}$ that can propagate through the periodic crystal without undergoing elastic Bragg reflection from the lattice planes. The zone boundaries are defined by the Bragg condition:</p>\n<div class=\"math-display\">\n$$\\vec{k} \\cdot \\left(\\frac{1}{2}\\vec{G}\\right) = \\left(\\frac{1}{2}\\vec{G}\\right)^2 \\implies 2\\vec{k} \\cdot \\vec{G} + G^2 = 0$$\n</div>\n\n<h4>3. Von Laue Diffraction Equations & Bragg's Law</h4>\n<p>When an incident plane wave of X-rays with wavevector $\\vec{k}$ ($|\\vec{k}| = 2\\pi/\\lambda$) scatters elastically from a crystal to wavevector $\\vec{k}'$ ($|\\vec{k}'| = |\\vec{k}|$), the scattering wavevector transfer is $\\Delta \\vec{k} = \\vec{k}' - \\vec{k}$. Constructive interference across the entire crystal occurs if and only if the <strong>Laue condition</strong> is satisfied:</p>\n<div class=\"math-display\">\n$$\\Delta \\vec{k} = \\vec{G}_{hkl}$$\n</div>\n<p>Taking the magnitude squared: $|\\vec{k}' - \\vec{k}|^2 = G^2 \\implies k^2 + k'^2 - 2 k k' \\cos(180^\\circ - 2\\theta) = G^2$. Since $k' = k = 2\\pi/\\lambda$ and $G = 2\\pi/d_{hkl}$:</p>\n<div class=\"math-display\">\n$$2k^2(1 - \\cos(\\pi - 2\\theta)) = 4k^2 \\sin^2\\theta = G^2 \\implies 2\\left(\\frac{2\\pi}{\\lambda}\\right)\\sin\\theta = \\frac{2\\pi}{d_{hkl}} \\implies 2d_{hkl}\\sin\\theta = \\lambda$$\n</div>\n<p>Generalizing to order $n$, this yields <strong>Bragg's Law of X-Ray Diffraction</strong>:</p>\n<div class=\"math-display\">\n$$2d_{hkl} \\sin\\theta = n\\lambda$$\n</div>\n\n<h4>4. Experimental X-Ray Diffraction Techniques</h4>\n<ol>\n<li><strong>Laue Method:</strong> Uses polychromatic (white) continuous X-ray radiation on a stationary single crystal. Each crystal plane $(hkl)$ selects a specific wavelength satisfying $2d\\sin\\theta = \\lambda$. Used to determine crystal orientation and symmetry.</li>\n<li><strong>Rotating Crystal Method:</strong> Uses monochromatic X-ray radiation on a single crystal rotating about a crystallographic axis. Different planes pass through the Bragg angle $\\theta$ sequentially, forming layer lines on a cylindrical film.</li>\n<li><strong>Powder Diffraction (Debye-Scherrer) Method:</strong> Uses monochromatic X-rays incident upon a finely powdered polycrystalline specimen containing millions of randomly oriented crystallites. Diffraction emerges as concentric cones of half-angle $2\\theta$, yielding characteristic diffraction rings used for phase identification.</li>\n</ol>"
        }
      ],
      "problems": [
        {
          "id": "ssp-p-1-1",
          "title": "Interplanar Spacing and Bragg Angle Calculation for Silicon (111)",
          "statement": "Silicon crystallizes in the diamond cubic structure with a conventional lattice parameter of $a = 5.431 \\text{ \u00c5}$. Monochromatic $\\text{Cu } K_\\alpha$ X-rays with wavelength $\\lambda = 1.5406 \\text{ \u00c5}$ are directed at a single-crystal silicon wafer. (a) Calculate the interplanar spacing $d_{111}$ for the (111) planes. (b) Determine the first-order ($n=1$) Bragg diffraction angle $\\theta_{111}$ and the total scattering deflection angle $2\\theta$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate Interplanar Spacing d_111",
              "math": "d_{111} = \\frac{a}{\\sqrt{h^2 + k^2 + l^2}} = \\frac{5.431\\text{ \\AA}}{\\sqrt{1^2 + 1^2 + 1^2}} = \\frac{5.431}{\\sqrt{3}}\\text{ \\AA} \\approx 3.1356\\text{ \\AA}",
              "explanation": "Apply the cubic interplanar spacing formula for Miller indices (h, k, l) = (1, 1, 1)."
            },
            {
              "stepName": "Step 2: Apply Bragg's Law to Find Diffraction Angle theta",
              "math": "\\sin\\theta_{111} = \\frac{n\\lambda}{2d_{111}} = \\frac{1 \\times 1.5406\\text{ \\AA}}{2 \\times 3.1356\\text{ \\AA}} = \\frac{1.5406}{6.2712} \\approx 0.24566",
              "explanation": "Substitute n=1, lambda = 1.5406 Angstroms, and d_111 into Bragg's equation 2 d sin(theta) = n lambda."
            },
            {
              "stepName": "Step 3: Evaluate Arcsin and Deflection Angle 2 theta",
              "math": "\\theta_{111} = \\arcsin(0.24566) = 14.22^\\circ \\implies 2\\theta = 28.44^\\circ",
              "explanation": "Calculate the Bragg angle theta and double it to determine the detector deflection angle 2 theta measured in standard powder and single-crystal diffractometers."
            }
          ],
          "answer": "d_{111} = 3.136 \\text{ \u00c5}, \\quad \\theta_{111} = 14.22^\\circ, \\quad 2\\theta = 28.44^\\circ"
        },
        {
          "id": "ssp-p-1-2",
          "title": "Reciprocal Lattice Volume and Primitive Vectors for FCC Copper",
          "statement": "Copper crystallizes in a face-centered cubic (FCC) lattice with lattice constant $a = 3.615 \\text{ \u00c5}$. (a) Write down the primitive translation vectors of the FCC direct lattice. (b) Calculate the volume of the primitive direct unit cell $V_c$. (c) Derive the primitive reciprocal lattice vectors $\\vec{b}_1, \\vec{b}_2, \\vec{b}_3$ and evaluate the volume of the First Brillouin Zone $V_{BZ}$.",
          "steps": [
            {
              "stepName": "Step 1: Direct Primitive Basis Vectors and Unit Cell Volume",
              "math": "\\vec{a}_1 = \\frac{a}{2}(\\hat{y} + \\hat{z}), \\quad \\vec{a}_2 = \\frac{a}{2}(\\hat{z} + \\hat{x}), \\quad \\vec{a}_3 = \\frac{a}{2}(\\hat{x} + \\hat{y})",
              "explanation": "The primitive vectors of FCC connect the origin to three adjacent face centers. The primitive cell volume is one-fourth of the conventional cubic cell volume:"
            },
            {
              "stepName": "Step 2: Calculate Numerical Value of Direct Primitive Volume V_c",
              "math": "V_c = \\frac{a^3}{4} = \\frac{(3.615\\text{ \\AA})^3}{4} = \\frac{47.241\\text{ \\AA}^3}{4} \\approx 11.810\\text{ \\AA}^3 = 1.181 \\times 10^{-29}\\text{ m}^3",
              "explanation": "Evaluate V_c = a^3 / 4 using the lattice parameter of copper."
            },
            {
              "stepName": "Step 3: Derive Reciprocal Vectors and Brillouin Zone Volume",
              "math": "\\vec{b}_1 = \\frac{2\\pi}{a}(-\\hat{x} + \\hat{y} + \\hat{z}), \\quad \\vec{b}_2 = \\frac{2\\pi}{a}(\\hat{x} - \\hat{y} + \\hat{z}), \\quad \\vec{b}_3 = \\frac{2\\pi}{a}(\\hat{x} + \\hat{y} - \\hat{z})",
              "explanation": "These are the primitive vectors of a Body-Centered Cubic (BCC) reciprocal lattice. The volume of the First Brillouin Zone is given by V_BZ = (2 pi)^3 / V_c:"
            },
            {
              "stepName": "Step 4: Compute First Brillouin Zone Volume V_BZ",
              "math": "V_{BZ} = \\frac{(2\\pi)^3}{V_c} = \\frac{4 (2\\pi)^3}{a^3} = \\frac{32\\pi^3}{(3.615\\text{ \\AA})^3} \\approx \\frac{992.88}{47.241}\\text{ \\AA}^{-3} \\approx 21.017\\text{ \\AA}^{-3} = 2.102 \\times 10^{31}\\text{ m}^{-3}",
              "explanation": "The volume of the First Brillouin Zone in reciprocal space."
            }
          ],
          "answer": "V_c = 11.81 \\text{ \u00c5}^3, \\quad V_{BZ} = 21.02 \\text{ \u00c5}^{-3} = 2.102 \\times 10^{31} \\text{ m}^{-3}"
        },
        {
          "id": "ssp-p-1-3",
          "title": "Debye-Scherrer Powder Diffraction Indexing for BCC Iron",
          "statement": "An X-ray powder diffraction pattern of alpha-iron (BCC structure) is recorded using monochromatic radiation of $\\lambda = 1.5418 \\text{ \u00c5}$. The first two diffraction peaks are observed at scattering angles $2\\theta_1 = 44.67^\\circ$ and $2\\theta_2 = 65.02^\\circ$. (a) Determine the Miller indices $(hkl)$ for these two reflection peaks taking into account the BCC selection rules ($h+k+l = \\text{even}$). (b) Calculate the lattice constant $a$ of iron.",
          "steps": [
            {
              "stepName": "Step 1: Extract Bragg Angles theta_1 and theta_2",
              "math": "\\theta_1 = \\frac{44.67^\\circ}{2} = 22.335^\\circ \\implies \\sin\\theta_1 = \\sin(22.335^\\circ) \\approx 0.38004",
              "explanation": "Convert 2 theta to theta and calculate sin(theta) for the first peak."
            },
            {
              "stepName": "Step 2: Calculate sin(theta) for the Second Peak",
              "math": "\\theta_2 = \\frac{65.02^\\circ}{2} = 32.51^\\circ \\implies \\sin\\theta_2 = \\sin(32.51^\\circ) \\approx 0.53745",
              "explanation": "Convert 2 theta to theta and calculate sin(theta) for the second peak."
            },
            {
              "stepName": "Step 3: Compare Ratio of sin^2(theta) to BCC Selection Rules",
              "math": "\\frac{\\sin^2\\theta_1}{\\sin^2\\theta_2} = \\frac{(0.38004)^2}{(0.53745)^2} = \\frac{0.14443}{0.28885} \\approx 0.5000 = \\frac{1}{2}",
              "explanation": "In a BCC lattice, allowed reflections require h+k+l = even. The lowest permitted values of s = h^2 + k^2 + l^2 are (110) with s=2, and (200) with s=4. The ratio is 2/4 = 1/2, perfectly matching the experimental ratio."
            },
            {
              "stepName": "Step 4: Calculate the Lattice Constant a",
              "math": "a = \\frac{\\lambda \\sqrt{h^2 + k^2 + l^2}}{2\\sin\\theta_1} = \\frac{1.5418\\text{ \\AA} \\times \\sqrt{2}}{2 \\times 0.38004} = \\frac{1.5418 \\times 1.4142}{0.76008} \\approx 2.8686\\text{ \\AA}",
              "explanation": "Using peak 1 with (hkl) = (110), solve for the lattice parameter a."
            }
          ],
          "answer": "\\text{Peak 1: } (110), \\quad \\text{Peak 2: } (200), \\quad a = 2.869 \\text{ \u00c5}"
        }
      ]
    },
    {
      "unitNumber": 2,
      "unitId": "unit2-crystal-bonding",
      "title": "Interatomic Forces & Crystal Bonding",
      "description": "Exhaustive treatment of cohesive energy and binding mechanisms: ionic bonding, exact derivation of the Madelung constant, Born-Mayer repulsive potential, bulk modulus, covalent bonding, Van der Waals dispersion forces, Lennard-Jones 6-12 potential, and metallic cohesion.",
      "sections": [
        {
          "id": "ssp-2-1",
          "title": "Classification of Chemical Bonds & Cohesive Energy",
          "content": "<h4>1. Cohesive Energy of Crystalline Solids</h4>\n<p>The <strong>cohesive energy</strong> (or binding energy) $E_{\\text{coh}}$ of a crystal is defined as the net energy required to disassemble the solid into its constituent neutral free atoms (or ions in ionic physics) at infinite mutual separation at zero temperature ($T = 0\\text{ K}$):</p>\n<div class=\"math-display\">\n$$E_{\\text{coh}} = E_{\\text{isolated atoms}} - E_{\\text{crystal}} > 0$$\n</div>\n<p>Cohesion originates entirely from electromagnetic interactions governed by quantum mechanics. Solids are classified into five primary bonding categories based on the distribution of their valence electrons:</p>\n<ol>\n<li><strong>Ionic Crystals (e.g., $\\text{NaCl}, \\text{CsCl}, \\text{LiF}$):</strong> Electrostatic attraction between positive cations and negative anions formed by complete valence electron transfer. Highly localized electron density, strong binding ($E_{\\text{coh}} \\approx 5 - 10\\text{ eV/atom}$), high melting points, electrical insulators in the solid state.</li>\n<li><strong>Covalent Crystals (e.g., Diamond, $\\text{Si}, \\text{Ge}, \\text{GaAs}$):</strong> Cohesion via quantum mechanical sharing of electron pairs localized along directional bonds formed by overlapping hybridized atomic orbitals ($sp^3$). Extreme hardness, high melting points, semiconductor or insulator band structure.</li>\n<li><strong>Metallic Crystals (e.g., $\\text{Na}, \\text{Cu}, \\text{Fe}, \\text{Al}$):</strong> Valence electrons delocalize completely into an itinerant electron gas (\"Fermi sea\") permeating an array of positively charged ion cores. Non-directional bonding, high electrical and thermal conductivities, ductility.</li>\n<li><strong>Van der Waals (Molecular) Crystals (e.g., Solid $\\text{Ar}, \\text{Kr}, \\text{CH}_4$):</strong> Weak cohesion ($E_{\\text{coh}} \\approx 0.05 - 0.2\\text{ eV/atom}$) arising from fluctuating quantum dipole-induced dipole interactions. Low melting and boiling points, soft mechanical properties.</li>\n<li><strong>Hydrogen-Bonded Crystals (e.g., Ice $\\text{H}_2\\text{O}, \\text{HF}$, nucleic acids):</strong> Directional electrostatic dipole attractions mediated by an electropositive bare proton sandwiched between electronegative lone pairs (O, N, F). Intermediate strength ($0.1 - 0.5\\text{ eV/bond}$).</li>\n</ol>"
        },
        {
          "id": "ssp-2-2",
          "title": "Ionic Crystals: Born-Mayer Potential & Madelung Constant",
          "simulation": "ssp-madelung-potential-sim",
          "content": "<h4>1. Electrostatic Madelung Energy Formalism</h4>\n<p>Consider an ionic crystal consisting of $2N$ ions ($N$ positive cations and $N$ negative anions with charges $\\pm q$). Let $R$ be the nearest-neighbor interionic separation distance. The total electrostatic Coulomb potential energy of ion $i$ interacting with all other ions $j \\neq i$ in the crystal is:</p>\n<div class=\"math-display\">\n$$U_{i,\\text{coul}} = \\sum_{j \\neq i} \\frac{(\\pm q)(\\mp q)}{4\\pi\\varepsilon_0 r_{ij}} = - \\frac{q^2}{4\\pi\\varepsilon_0 R} \\sum_{j \\neq i} \\frac{\\pm 1}{p_{ij}}$$\n</div>\n<p>where $r_{ij} = p_{ij} R$ denotes the distance between ions $i$ and $j$ measured in units of nearest-neighbor distance $R$, and the sign is positive for unlike charges (attraction) and negative for like charges (repulsion).</p>\n<p>The dimensionless sum is defined as the <strong>Madelung Constant</strong> $\\alpha$:</p>\n<div class=\"math-display\">\n$$\\alpha = \\sum_{j \\neq i} \\frac{\\pm 1}{p_{ij}}$$\n</div>\n<p>Multiplying by $N$ ion pairs (to avoid double-counting the pair interactions), the total electrostatic Madelung energy of the crystal is:</p>\n<div class=\"math-display\">\n$$U_{\\text{Madelung}}(R) = - N \\alpha \\frac{q^2}{4\\pi\\varepsilon_0 R}$$\n</div>\n\n<h4>2. Calculation of the Madelung Constant for a One-Dimensional Ionic Chain</h4>\n<p>Consider an infinite 1D chain of alternating cations and anions with nearest-neighbor distance $R$. Choosing an arbitrary positive ion as the origin, its neighbors are situated at distances $R, 2R, 3R, \\dots$ to both the left and right:</p>\n<ul>\n<li>Two opposite ions at distance $1R$: contribution $+2 \\times (1/1)$</li>\n<li>Two identical ions at distance $2R$: contribution $-2 \\times (1/2)$</li>\n<li>Two opposite ions at distance $3R$: contribution $+2 \\times (1/3)$</li>\n</ul>\n<p>The 1D Madelung constant $\\alpha_{\\text{1D}}$ is therefore given by the alternating harmonic series:</p>\n<div class=\"math-display\">\n$$\\alpha_{\\text{1D}} = 2 \\left( 1 - \\frac{1}{2} + \\frac{1}{3} - \\frac{1}{4} + \\frac{1}{5} - \\dots \\right)$$\n</div>\n<p>Recalling the Taylor series expansion of $\\ln(1+x) = x - x^2/2 + x^3/3 - x^4/4 + \\dots$ evaluated at $x = 1$:</p>\n<div class=\"math-display\">\n$$\\sum_{m=1}^{\\infty} \\frac{(-1)^{m-1}}{m} = \\ln(2) \\implies \\alpha_{\\text{1D}} = 2 \\ln(2) \\approx 2 \\times 0.69315 = 1.38629$$\n</div>\n\n<h4>3. Madelung Constants for 3D Ionic Lattices</h4>\n<p>In three dimensions, the summation is conditionally convergent and requires specialized summing techniques (e.g., the <strong>Evjen method</strong> of neutral concentric polyhedra or the <strong>Ewald summation method</strong> in reciprocal space):</p>\n<ul>\n<li><strong>Rock-Salt ($\\text{NaCl}$):</strong> $\\alpha = 1.747565$</li>\n<li><strong>Cesium Chloride ($\\text{CsCl}$):</strong> $\\alpha = 1.762675$</li>\n<li><strong>Zincblende ($\\text{ZnS}$):</strong> $\\alpha = 1.63805$</li>\n<li><strong>Wurtzite ($\\text{ZnS}$):</strong> $\\alpha = 1.64132$</li>\n<li><strong>Fluorite ($\\text{CaF}_2$):</strong> $\\alpha = 5.03878$</li>\n</ul>"
        },
        {
          "id": "ssp-2-3",
          "title": "Cohesive Energy & Bulk Modulus of Ionic Crystals",
          "content": "<h4>1. Total Cohesive Energy with Born-Mayer Repulsion</h4>\n<p>At short interionic separations, the electron clouds of adjacent ions overlap. By the Pauli Exclusion Principle, overlapping closed electron shells must occupy higher unpopulated quantum states, generating a steep quantum mechanical repulsive potential. The total potential energy per ion pair $U_{\\text{tot}}(R)$ is modeled by the <strong>Born-Mayer equation</strong>:</p>\n<div class=\"math-display\">\n$$U_{\\text{tot}}(R) = - \\frac{\\alpha q^2}{4\\pi\\varepsilon_0 R} + z B e^{-R/\\rho}$$\n</div>\n<p>where $z$ is the coordination number (number of nearest neighbors), $B$ is a repulsive strength constant, and $\\rho \\approx 0.33\\text{ \\AA}$ is the characteristic range parameter of core repulsion.</p>\n\n<h4>2. Equilibrium Interionic Separation $R_0$</h4>\n<p>At equilibrium ($R = R_0$), the net mechanical force vanishes: $\\left.\\frac{dU_{\\text{tot}}}{dR}\\right|_{R=R_0} = 0$:</p>\n<div class=\"math-display\">\n$$\\left.\\frac{dU_{\\text{tot}}}{dR}\\right|_{R_0} = \\frac{\\alpha q^2}{4\\pi\\varepsilon_0 R_0^2} - \\frac{z B}{\\rho} e^{-R_0/\\rho} = 0 \\implies z B e^{-R_0/\\rho} = \\frac{\\alpha q^2}{4\\pi\\varepsilon_0 R_0} \\left(\\frac{\\rho}{R_0}\\right)$$\n</div>\n<p>Substituting this repulsive term back into $U_{\\text{tot}}(R_0)$ yields the celebrated <strong>Born-Mayer cohesive energy formula</strong> per ion pair:</p>\n<div class=\"math-display\">\n$$U_{\\text{tot}}(R_0) = - \\frac{\\alpha q^2}{4\\pi\\varepsilon_0 R_0} \\left( 1 - \\frac{\\rho}{R_0} \\right)$$\n</div>\n<p>Since $\\rho / R_0 \\approx 0.33\\text{ \\AA} / 2.82\\text{ \\AA} \\approx 0.12$, core repulsion reduces the pure electrostatic Coulomb binding energy by approximately $10 - 15\\%$.</p>\n\n<h4>3. Derivation of Bulk Modulus $B$</h4>\n<p>The isothermal bulk modulus $B$ measures the resistance of the crystal to uniform hydrostatic compression: $B = - V \\frac{dP}{dV}$. At $T = 0\\text{ K}$, the hydrostatic pressure is $P = - \\frac{dU_{\\text{cryst}}}{dV}$, which implies:</p>\n<div class=\"math-display\">\n$$B = V \\frac{d^2 U_{\\text{cryst}}}{dV^2} = \\left. V_0 \\frac{d^2 U_{\\text{tot}}}{dV^2} \\right|_{V=V_0}$$\n</div>\n<p>For a rock-salt cubic crystal with volume per ion pair $V = 2 R^3$ (where $V_0 = 2 R_0^3$), changing variables via $\\frac{dU}{dV} = \\frac{dU/dR}{dV/dR} = \\frac{1}{6R^2} \\frac{dU}{dR}$ leads directly to:</p>\n<div class=\"math-display\">\n$$B = \\frac{1}{18 R_0} \\left. \\frac{d^2 U_{\\text{tot}}}{dR^2} \\right|_{R=R_0} = \\frac{\\alpha q^2}{72 \\pi \\varepsilon_0 R_0^4} \\left( \\frac{R_0}{\\rho} - 2 \\right)$$\n</div>"
        },
        {
          "id": "ssp-2-4",
          "title": "Van der Waals Crystals & Lennard-Jones (6-12) Potential",
          "simulation": "ssp-lennard-jones-potential-sim",
          "content": "<h4>1. Origin of London Dispersion Forces</h4>\n<p>In inert gas crystals (solid $\\text{Ne}, \\text{Ar}, \\text{Kr}, \\text{Xe}$), atoms possess completely closed electronic shells with spherical symmetry and zero permanent dipole moment ($\\langle \\vec{p} \\rangle = 0$). However, quantum fluctuations in electron cloud positions produce an instantaneous fluctuating electric dipole $\\vec{p}_1(t) \\sim e \\vec{x}(t)$. This instantaneous dipole generates an electric field at distance $R$:</p>\n<div class=\"math-display\">\n$$E_1 \\approx \\frac{p_1}{4\\pi\\varepsilon_0 R^3}$$\n</div>\n<p>This electric field induces a dipole moment in the adjacent neutral atom proportional to its electronic polarizability $\\alpha_{\\text{pol}}$: $\\vec{p}_2 = \\alpha_{\\text{pol}} \\vec{E}_1 \\propto \\frac{\\alpha_{\\text{pol}} p_1}{R^3}$. The resulting dipole-dipole electrostatic interaction energy is attractive and scales inversely with the sixth power of distance:</p>\n<div class=\"math-display\">\n$$U_{\\text{disp}}(R) = - \\vec{p}_2 \\cdot \\vec{E}_1 \\propto - \\frac{\\alpha_{\\text{pol}} p_1^2}{R^6} = - \\frac{C}{R^6}$$\n</div>\n\n<h4>2. The Lennard-Jones (6-12) Potential</h4>\n<p>When two inert gas atoms approach within the distance of their closed electron shells, Pauli core exclusion generates a steep repulsive potential, empirically parameterized as an inverse-twelfth power $1/R^{12}$. The total interaction potential between a pair of atoms separated by distance $R$ is the <strong>Lennard-Jones (6-12) potential</strong>:</p>\n<div class=\"math-display\">\n$$U_{LJ}(R) = 4\\varepsilon \\left[ \\left(\\frac{\\sigma}{R}\\right)^{12} - \\left(\\frac{\\sigma}{R}\\right)^6 \\right]$$\n</div>\n<p>where:</p>\n<ul>\n<li>$\\varepsilon$: Depth of the potential well (binding energy minimum).</li>\n<li>$\\sigma$: Finite distance at which the interatomic potential is zero ($U_{LJ}(\\sigma) = 0$).</li>\n</ul>\n<p>The minimum of the two-body potential occurs where $\\frac{dU_{LJ}}{dR} = 0$:</p>\n<div class=\"math-display\">\n$$\\frac{dU_{LJ}}{dR} = 4\\varepsilon \\left[ -\\frac{12\\sigma^{12}}{R^{13}} + \\frac{6\\sigma^6}{R^7} \\right] = 0 \\implies R_{\\text{min}} = 2^{1/6}\\sigma \\approx 1.122\\sigma$$\n</div>\n<p>At this equilibrium separation, the potential energy minimum is exactly $U_{LJ}(R_{\\text{min}}) = -\\varepsilon$.</p>\n\n<h4>3. Cohesive Energy of Inert Gas FCC Crystals</h4>\n<p>In an FCC crystal of $N$ inert gas atoms, summing over all pairs with $R_{ij} = p_{ij} R$ yields the total crystal potential energy:</p>\n<div class=\"math-display\">\n$$U_{\\text{tot}}(R) = 2 N \\varepsilon \\left[ A_{12} \\left(\\frac{\\sigma}{R}\\right)^{12} - A_6 \\left(\\frac{\\sigma}{R}\\right)^6 \\right]$$\n</div>\n<p>For an FCC lattice, the lattice sums over all neighbors are geometric constants:</p>\n<div class=\"math-display\">\n$$A_{12} = \\sum_{j \\neq 0} p_{0j}^{-12} \\approx 12.13188, \\quad A_6 = \\sum_{j \\neq 0} p_{0j}^{-6} \\approx 14.45392$$\n</div>\n<p>Minimizing $U_{\\text{tot}}(R)$ with respect to $R$ yields the equilibrium crystal nearest-neighbor separation $R_0$ and the total cohesive energy per atom:</p>\n<div class=\"math-display\">\n$$R_0 = \\left( \\frac{2 A_{12}}{A_6} \\right)^{1/6} \\sigma \\approx 1.09 \\sigma, \\quad \\frac{U_{\\text{tot}}(R_0)}{N} = - 2.15 (4\\varepsilon) \\approx - 8.61 \\varepsilon$$\n</div>"
        }
      ],
      "problems": [
        {
          "id": "ssp-p-2-1",
          "title": "Cohesive Energy and Repulsive Exponent of Sodium Chloride (NaCl)",
          "statement": "The experimental equilibrium nearest-neighbor distance in sodium chloride ($\\text{NaCl}$) is $R_0 = 2.820 \\text{ \u00c5}$, and its experimental cohesive energy is $E_{\\text{coh}} = 7.95 \\text{ eV/molecule}$ ($767 \\text{ kJ/mol}$). The Madelung constant for the rock-salt structure is $\\alpha = 1.7476$. Modeling the repulsive potential using the Born power-law form $U_{\\text{rep}}(R) = B / R^n$: (a) Derive the expression for cohesive energy in terms of $n$. (b) Calculate the numerical value of the repulsive exponent $n$.",
          "steps": [
            {
              "stepName": "Step 1: Formulate the Total Potential Energy Function",
              "math": "U(R) = - \\frac{\\alpha e^2}{4\\pi\\varepsilon_0 R} + \\frac{B}{R^n}",
              "explanation": "Write down the potential energy per NaCl molecule combining the attractive Coulomb-Madelung term and the Born power-law repulsive term."
            },
            {
              "stepName": "Step 2: Apply the Equilibrium Condition at R = R_0",
              "math": "\\left.\\frac{dU}{dR}\\right|_{R_0} = \\frac{\\alpha e^2}{4\\pi\\varepsilon_0 R_0^2} - \\frac{n B}{R_0^{n+1}} = 0 \\implies \\frac{B}{R_0^n} = \\frac{\\alpha e^2}{4\\pi\\varepsilon_0 R_0} \\frac{1}{n}",
              "explanation": "Set the first derivative of potential energy with respect to interionic distance to zero at R = R_0."
            },
            {
              "stepName": "Step 3: Substitute B back into Cohesive Energy",
              "math": "E_{\\text{coh}} = - U(R_0) = \\frac{\\alpha e^2}{4\\pi\\varepsilon_0 R_0} \\left( 1 - \\frac{1}{n} \\right)",
              "explanation": "Substitute the repulsive term B / R_0^n back into the expression for U(R_0)."
            },
            {
              "stepName": "Step 4: Numerically Calculate the Pure Electrostatic Energy",
              "math": "U_M = \\frac{\\alpha e^2}{4\\pi\\varepsilon_0 R_0} = \\frac{1.7476 \\times 1.440\\text{ eV}\\cdot\\text{\\AA}}{2.820\\text{ \\AA}} = \\frac{2.5165}{2.820}\\text{ eV} \\approx 8.924\\text{ eV}",
              "explanation": "Evaluate the electrostatic Coulomb energy using e^2 / (4 pi epsilon_0) = 1.440 eV * Angstrom."
            },
            {
              "stepName": "Step 5: Solve for the Repulsive Exponent n",
              "math": "1 - \\frac{1}{n} = \\frac{E_{\\text{coh}}}{U_M} = \\frac{7.95\\text{ eV}}{8.924\\text{ eV}} \\approx 0.8909 \\implies \\frac{1}{n} = 1 - 0.8909 = 0.1091 \\implies n = \\frac{1}{0.1091} \\approx 9.16",
              "explanation": "Equate the theoretical formula to the experimental cohesive energy to extract the Born exponent n."
            }
          ],
          "answer": "n \\approx 9.16 \\quad (\\text{Consistent with the canonical closed-shell } \\text{Na}^+\\text{-}\\text{Cl}^- \\text{ value of } n \\approx 9)"
        },
        {
          "id": "ssp-p-2-2",
          "title": "Bulk Modulus and Compressibility of Potassium Chloride (KCl)",
          "statement": "Potassium chloride ($\\text{KCl}$) crystallizes in the rock-salt structure with equilibrium nearest-neighbor interionic spacing $R_0 = 3.147 \\text{ \u00c5}$, Madelung constant $\\alpha = 1.7476$, and Born-Mayer range parameter $\\rho = 0.330 \\text{ \u00c5}$. (a) Calculate the theoretical isothermal bulk modulus $B$ of $\\text{KCl}$ at $T = 0 \\text{ K}$. (b) Determine the compressibility $\\beta = 1/B$ in units of $\\text{GPa}^{-1}$.",
          "steps": [
            {
              "stepName": "Step 1: State the Formula for Bulk Modulus of Rock-Salt Crystals",
              "math": "B = \\frac{\\alpha e^2}{72 \\pi \\varepsilon_0 R_0^4} \\left( \\frac{R_0}{\\rho} - 2 \\right)",
              "explanation": "Use the bulk modulus formula derived from the second derivative of the Born-Mayer crystal potential."
            },
            {
              "stepName": "Step 2: Evaluate the Dimensionless Factor (R_0 / rho - 2)",
              "math": "\\frac{R_0}{\\rho} = \\frac{3.147\\text{ \\AA}}{0.330\\text{ \\AA}} \\approx 9.5364 \\implies \\left(\\frac{R_0}{\\rho} - 2\\right) = 7.5364",
              "explanation": "Compute the repulsive curvature term."
            },
            {
              "stepName": "Step 3: Evaluate the Prefactor in SI Units",
              "math": "\\frac{\\alpha e^2}{4\\pi\\varepsilon_0} = 1.7476 \\times (2.307 \\times 10^{-28}\\text{ J}\\cdot\\text{m}) \\approx 4.0318 \\times 10^{-28}\\text{ J}\\cdot\\text{m}",
              "explanation": "Calculate the numerator product in SI units."
            },
            {
              "stepName": "Step 4: Compute the Bulk Modulus B",
              "math": "B = \\frac{4.0318 \\times 10^{-28}\\text{ J}\\cdot\\text{m} \\times 7.5364}{18 \\times (3.147 \\times 10^{-10}\\text{ m})^4} = \\frac{3.0385 \\times 10^{-27}}{18 \\times 9.808 \\times 10^{-38}} = \\frac{3.0385 \\times 10^{-27}}{1.7654 \\times 10^{-36}} \\approx 1.721 \\times 10^{10}\\text{ Pa} = 17.21\\text{ GPa}",
              "explanation": "Divide through by 18 R_0^4 to find the bulk modulus in Pascals (N/m^2)."
            },
            {
              "stepName": "Step 5: Calculate the Compressibility beta",
              "math": "\\beta = \\frac{1}{B} = \\frac{1}{17.21\\text{ GPa}} \\approx 0.0581\\text{ GPa}^{-1} = 5.81 \\times 10^{-11}\\text{ Pa}^{-1}",
              "explanation": "Take the reciprocal of bulk modulus to find compressibility beta."
            }
          ],
          "answer": "B = 17.21 \\text{ GPa}, \\quad \\beta = 0.0581 \\text{ GPa}^{-1} = 5.81 \\times 10^{-11} \\text{ Pa}^{-1}"
        },
        {
          "id": "ssp-p-2-3",
          "title": "Cohesive Energy and Nearest-Neighbor Distance of Solid Argon",
          "statement": "Solid Argon crystallizes in an FCC lattice governed by the Lennard-Jones (6-12) potential with parameters $\\varepsilon = 10.42 \\text{ meV} = 1.670 \\times 10^{-21} \\text{ J}$ and $\\sigma = 3.40 \\text{ \u00c5}$. The FCC lattice sums are $A_{12} = 12.1319$ and $A_6 = 14.4539$. (a) Determine the theoretical nearest-neighbor separation $R_0$ and the conventional cubic lattice parameter $a$. (b) Calculate the total cohesive energy per mole of solid Argon in $\\text{kJ/mol}$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Equilibrium Nearest-Neighbor Separation R_0",
              "math": "R_0 = \\left( \\frac{2 A_{12}}{A_6} \\right)^{1/6} \\sigma = \\left( \\frac{2 \\times 12.1319}{14.4539} \\right)^{1/6} (3.40\\text{ \\AA}) = (1.6787)^{0.16667} (3.40\\text{ \\AA}) \\approx 1.0906 \\times 3.40\\text{ \\AA} \\approx 3.708\\text{ \\AA}",
              "explanation": "Compute the equilibrium bond distance using the ratio of the lattice sums."
            },
            {
              "stepName": "Step 2: Relate Nearest-Neighbor Distance to FCC Lattice Parameter a",
              "math": "R_0 = \\frac{a}{\\sqrt{2}} \\implies a = \\sqrt{2} R_0 = \\sqrt{2} \\times 3.708\\text{ \\AA} \\approx 5.244\\text{ \\AA}",
              "explanation": "In an FCC lattice, nearest neighbors touch along face diagonals of length sqrt(2) * a."
            },
            {
              "stepName": "Step 3: Calculate the Cohesive Energy per Atom",
              "math": "u_0 = - \\frac{U_{\\text{tot}}(R_0)}{N} = 2.15 \\times 4\\varepsilon = 8.60 \\times (10.42\\text{ meV}) \\approx 89.61\\text{ meV/atom} = 1.436 \\times 10^{-20}\\text{ J/atom}",
              "explanation": "Evaluate the binding energy per atom at equilibrium."
            },
            {
              "stepName": "Step 4: Convert Cohesive Energy to Molar Basis",
              "math": "E_{\\text{coh, molar}} = u_0 \\times N_A = (1.436 \\times 10^{-20}\\text{ J}) \\times (6.022 \\times 10^{23}\\text{ mol}^{-1}) \\approx 8647\\text{ J/mol} = 8.65\\text{ kJ/mol}",
              "explanation": "Multiply by Avogadro's number N_A to obtain the cohesive energy per mole."
            }
          ],
          "answer": "R_0 = 3.708 \\text{ \u00c5}, \\quad a = 5.244 \\text{ \u00c5}, \\quad E_{\\text{coh}} = 8.65 \\text{ kJ/mol} \\quad (89.61 \\text{ meV/atom})"
        }
      ]
    },
    {
      "unitNumber": 3,
      "unitId": "unit3-lattice-vibrations",
      "title": "Lattice Vibrations, Phonons & Thermal Properties",
      "description": "Rigorous classical and quantum theory of lattice dynamics: monatomic and diatomic 1D chain dispersion relations, acoustic and optical phonon branches, Brillouin zone boundaries, normal modes, inelastic neutron scattering, Einstein and Debye specific heat models, anharmonic lattice expansion, thermal conductivity, and Normal vs Umklapp phonon scattering processes.",
      "sections": [
        {
          "id": "ssp-3-1",
          "title": "Vibrations of a Monatomic 1D Lattice & Acoustic Dispersion",
          "simulation": "ssp-phonon-dispersion-sim",
          "content": "<h4>1. Equation of Motion for a Linear Monatomic Chain</h4>\n<p>Consider an infinite one-dimensional lattice of identical atoms, each of mass $M$, separated at equilibrium by lattice spacing $a$. Let $u_n(t)$ denote the displacement of the $n$-th atom from its equilibrium position $x_n = n a$. Under the <em>harmonic approximation</em>, the restoring force on atom $n$ arises from Hooke's law interactions with its nearest neighbors $n-1$ and $n+1$ with spring constant $C$:</p>\n<div class=\"math-display\">\n$$M \\frac{d^2 u_n}{dt^2} = C (u_{n+1} - u_n) - C (u_n - u_{n-1}) = C (u_{n+1} + u_{n-1} - 2u_n)$$\n</div>\n\n<h4>2. Derivation of the Phonon Dispersion Relation $\\omega(k)$</h4>\n<p>Seeking traveling plane-wave normal-mode solutions of the form $u_n(t) = A e^{i(k n a - \\omega t)}$, where $k$ is the wavevector and $\\omega$ is the angular frequency:</p>\n<div class=\"math-display\">\n$$- M \\omega^2 A e^{i(k n a - \\omega t)} = C A e^{i(k n a - \\omega t)} \\left[ e^{i k a} + e^{- i k a} - 2 \\right]$$\n</div>\n<p>Dividing through by $A e^{i(k n a - \\omega t)}$ and recalling Euler's identity $e^{i k a} + e^{-i k a} = 2\\cos(k a)$:</p>\n<div class=\"math-display\">\n$$- M \\omega^2 = 2C [\\cos(k a) - 1] = - 4C \\sin^2\\left(\\frac{k a}{2}\\right)$$\n</div>\n<p>Taking the positive square root yields the <strong>acoustic dispersion relation</strong> for the monatomic chain:</p>\n<div class=\"math-display\">\n$$\\omega(k) = 2 \\sqrt{\\frac{C}{M}} \\left| \\sin\\left(\\frac{k a}{2}\\right) \\right|$$\n</div>\n\n<h4>3. Long-Wavelength Limit and Brillouin Zone Boundary</h4>\n<ul>\n<li><strong>Long-Wavelength (Continuum / Acoustic) Limit ($k a \\ll 1$):</strong>\n<p>As $k \\to 0$, $\\sin(k a / 2) \\approx k a / 2$, which gives a linear dispersion relation:</p>\n<div class=\"math-display\">\n$$\\omega \\approx 2 \\sqrt{\\frac{C}{M}} \\left(\\frac{k a}{2}\\right) = a \\sqrt{\\frac{C}{M}} k = v_s k$$\n</div>\n<p>where $v_s = a \\sqrt{C/M}$ is the macroscopic <strong>sound velocity</strong> in the crystal. In this limit, the group velocity equals the phase velocity: $v_g = d\\omega/dk = v_s = v_p = \\omega/k$.</p></li>\n<li><strong>First Brillouin Zone Boundary ($k = \\pm \\pi / a$):</strong>\n<p>At the edge of the first Brillouin zone, $\\sin(\\pi / 2) = 1$, yielding the maximum cut-off angular frequency:</p>\n<div class=\"math-display\">\n$$\\omega_{\\text{max}} = 2 \\sqrt{\\frac{C}{M}}$$\n</div>\n<p>The group velocity vanishes at the zone boundary: $\\left. v_g \\right|_{k = \\pi/a} = \\left. \\frac{d\\omega}{dk} \\right|_{\\pi/a} = a \\sqrt{\\frac{C}{M}} \\cos\\left(\\frac{\\pi}{2}\\right) = 0$. The wave becomes a <em>standing wave</em> with adjacent atoms oscillating in exact antiphase: $u_{n+1}/u_n = e^{i\\pi} = -1$.</p></li>\n</ul>"
        },
        {
          "id": "ssp-3-2",
          "title": "Vibrations of a Diatomic 1D Lattice: Acoustic & Optical Branches",
          "content": "<h4>1. Coupled Equations of Motion for a Diatomic Chain</h4>\n<p>Consider a 1D lattice with a two-atom basis: alternating masses $M_1$ and $M_2$ ($M_1 > M_2$) connected by identical nearest-neighbor springs of force constant $C$ with unit cell dimension $a$ (interatomic separation $a/2$). Let $u_n(t)$ denote the displacement of mass $M_1$ in unit cell $n$, and $v_n(t)$ denote the displacement of mass $M_2$ in unit cell $n$:</p>\n<div class=\"math-display\">\n$$M_1 \\frac{d^2 u_n}{dt^2} = C (v_n + v_{n-1} - 2 u_n), \\quad M_2 \\frac{d^2 v_n}{dt^2} = C (u_{n+1} + u_n - 2 v_n)$$\n</div>\n\n<h4>2. Secular Determinant & Two Frequency Branches</h4>\n<p>Substituting harmonic normal-mode trial solutions $u_n = A e^{i(k n a - \\omega t)}$ and $v_n = B e^{i(k n a - \\omega t)}$ yields the linear algebraic system:</p>\n<div class=\"math-display\">\n$$\\begin{pmatrix} 2C - M_1 \\omega^2 & - C (1 + e^{-i k a}) \\\\ - C (1 + e^{i k a}) & 2C - M_2 \\omega^2 \\end{pmatrix} \\begin{pmatrix} A \\\\ B \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix}$$\n</div>\n<p>For non-trivial solutions, the secular determinant must vanish:</p>\n<div class=\"math-display\">\n$$(2C - M_1 \\omega^2)(2C - M_2 \\omega^2) - C^2 |1 + e^{i k a}|^2 = 0 \\implies M_1 M_2 \\omega^4 - 2C(M_1 + M_2)\\omega^2 + 4C^2 \\sin^2\\left(\\frac{k a}{2}\\right) = 0$$\n</div>\n<p>Solving the quadratic equation in $\\omega^2$ yields two distinct branches:</p>\n<div class=\"math-display\">\n$$\\omega^2(k) = C \\left( \\frac{1}{M_1} + \\frac{1}{M_2} \\right) \\pm C \\sqrt{\\left(\\frac{1}{M_1} + \\frac{1}{M_2}\\right)^2 - \\frac{4 \\sin^2(k a / 2)}{M_1 M_2}}$$\n</div>\n\n<h4>3. Physical Significance of Acoustic and Optical Branches</h4>\n<ul>\n<li><strong>Acoustic Branch (Minus Sign):</strong>\n<p>As $k \\to 0$, $\\omega_{\\text{ac}} \\to 0$. In this limit, $A/B \\to +1$: both masses in each unit cell oscillate in phase with identical amplitudes and directions, representing long-wavelength sound waves.</p></li>\n<li><strong>Optical Branch (Plus Sign):</strong>\n<p>At $k = 0$, $\\omega_{\\text{opt}}(0) = \\sqrt{2C \\left(\\frac{1}{M_1} + \\frac{1}{M_2}\\right)} = \\sqrt{\\frac{2C}{\\mu}}$, where $\\mu$ is the reduced mass. In this limit, $M_1 A + M_2 B = 0 \\implies A/B = - M_2 / M_1$: the center of mass of the unit cell remains stationary while adjacent opposite ions oscillate in antiphase against each other. In ionic crystals, this creates an oscillating electric dipole moment that couples strongly to electromagnetic light waves (infrared absorption), hence the name <em>optical branch</em>.</p></li>\n<li><strong>Forbidden Band Gap at Brillouin Zone Boundary ($k = \\pm \\pi / a$):</strong>\n<p>At $k = \\pi / a$, $\\sin^2(k a / 2) = 1$, yielding two discrete frequencies:</p>\n<div class=\"math-display\">\n$$\\omega_{\\text{opt}}\\left(\\frac{\\pi}{a}\\right) = \\sqrt{\\frac{2C}{M_2}}, \\quad \\omega_{\\text{ac}}\\left(\\frac{\\pi}{a}\\right) = \\sqrt{\\frac{2C}{M_1}}$$\n</div>\n<p>Between $\\sqrt{2C/M_1}$ and $\\sqrt{2C/M_2}$, no real solution for $k$ exists. This frequency interval is a <strong>forbidden phononic band gap</strong> where lattice waves cannot propagate and are exponentially attenuated.</p></li>\n</ul>"
        },
        {
          "id": "ssp-3-3",
          "title": "The Phonon Concept, Normal Modes & Inelastic Neutron Scattering",
          "content": "<h4>1. Quantum Mechanics of Lattice Vibrations: Phonons</h4>\n<p>When the classical harmonic Hamiltonian of $N$ coupled lattice oscillators is transformed into normal coordinates $q_{\\vec{k}, s}$ and canonically quantized, it decouples into a sum of $3N$ independent quantum harmonic oscillators:</p>\n<div class=\"math-display\">\n$$\\hat{H} = \\sum_{\\vec{k}, s} \\hbar \\omega_s(\\vec{k}) \\left( \\hat{a}_{\\vec{k},s}^\\dagger \\hat{a}_{\\vec{k},s} + \\frac{1}{2} \\right)$$\n</div>\n<p>where $\\hat{a}_{\\vec{k},s}^\\dagger$ and $\\hat{a}_{\\vec{k},s}$ are creation and annihilation operators. A quantum of lattice vibrational energy is called a <strong>phonon</strong>, carrying energy $\\hbar \\omega_s(\\vec{k})$.</p>\n<p>Because phonons are indistinguishable bosons with zero chemical potential ($\\mu = 0$), their thermal equilibrium occupation number at temperature $T$ is governed strictly by the <strong>Planck distribution</strong>:</p>\n<div class=\"math-display\">\n$$\\langle n_{\\vec{k},s} \\rangle = \\frac{1}{e^{\\hbar \\omega_s(\\vec{k}) / k_B T} - 1}$$\n</div>\n\n<h4>2. Phonon Crystal Momentum $\\hbar \\vec{q}$</h4>\n<p>A phonon carries wavevector $\\vec{q}$ and a quantity $\\hbar \\vec{q}$ known as <strong>crystal momentum</strong>. Unlike physical momentum (the center of mass of the whole crystal does not move during internal vibrations), crystal momentum is conserved only modulo a reciprocal lattice vector $\\vec{G}$:</p>\n<div class=\"math-display\">\n$$\\sum \\vec{k}_{\\text{initial}} = \\sum \\vec{k}_{\\text{final}} + \\vec{G}$$\n</div>\n\n<h4>3. Inelastic Neutron Scattering</h4>\n<p>The experimental dispersion relation $\\omega(\\vec{q})$ across the entire Brillouin zone is determined by <strong>Inelastic Neutron Scattering (INS)</strong>. Thermal neutrons with mass $M_n \\approx 1.675 \\times 10^{-27}\\text{ kg}$ have de Broglie wavelengths comparable to lattice spacings ($\\lambda \\sim 1 - 2\\text{ \\AA}$) and kinetic energies comparable to phonon energies ($E \\sim 10 - 100\\text{ meV}$):</p>\n<ul>\n<li><strong>Energy Conservation:</strong> $E' - E = \\frac{\\hbar^2 k'^2}{2M_n} - \\frac{\\hbar^2 k^2}{2M_n} = \\pm \\hbar \\omega(\\vec{q})$ ($+$ for phonon emission, $-$ for phonon absorption).</li>\n<li><strong>Crystal Momentum Conservation:</strong> $\\vec{k}' - \\vec{k} = \\mp \\vec{q} + \\vec{G}$.</li>\n</ul>\n<p>By measuring the scattered neutron angle and energy, both $\\omega$ and $\\vec{q}$ are mapped simultaneously.</p>"
        },
        {
          "id": "ssp-3-4",
          "title": "Theories of Lattice Specific Heat: Einstein & Debye Models",
          "simulation": "ssp-debye-specific-heat-sim",
          "content": "<h4>1. Classical Dulong-Petit Law & Quantum Failure</h4>\n<p>By the classical equipartition theorem, each of the $3N$ vibrational degrees of freedom in a 3D crystal of $N$ atoms possesses an average thermal energy of $k_B T$, yielding total internal energy $U = 3 N k_B T$. The molar lattice heat capacity at constant volume is the constant <strong>Dulong-Petit value</strong>:</p>\n<div class=\"math-display\">\n$$C_V = \\left(\\frac{\\partial U}{\\partial T}\\right)_V = 3 N_A k_B = 3 R \\approx 24.94\\text{ J}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1}$$\n</div>\n<p>Experimentally, as $T \\to 0\\text{ K}$, $C_V$ vanishes rapidly, violating classical theory.</p>\n\n<h4>2. The Einstein Specific Heat Model</h4>\n<p>Einstein (1907) assumed that all $3N$ normal modes oscillate independently with the <em>same identical frequency</em> $\\omega_E$ (characteristic Einstein temperature $\\Theta_E = \\hbar\\omega_E / k_B$):</p>\n<div class=\"math-display\">\n$$U = 3N \\left( \\frac{\\hbar\\omega_E}{e^{\\hbar\\omega_E / k_B T} - 1} + \\frac{1}{2}\\hbar\\omega_E \\right) \\implies C_V = 3 N k_B \\left(\\frac{\\Theta_E}{T}\\right)^2 \\frac{e^{\\Theta_E / T}}{\\left(e^{\\Theta_E / T} - 1\\right)^2}$$\n</div>\n<ul>\n<li><strong>High-Temperature Limit ($T \\gg \\Theta_E$):</strong> $C_V \\to 3 N k_B$ (recovers Dulong-Petit).</li>\n<li><strong>Low-Temperature Limit ($T \\ll \\Theta_E$):</strong> $C_V \\approx 3 N k_B (\\Theta_E / T)^2 e^{-\\Theta_E / T}$. While this vanishes at $T = 0$, the exponential drop is much steeper than experimental data, which follows a power law.</li>\n</ul>\n\n<h4>3. The Debye Model & The $T^3$ Law</h4>\n<p>Debye (1912) treated the crystal as an elastic isotropic continuum with linear acoustic dispersion $\\omega = v_s k$ across all three acoustic polarizations ($1$ longitudinal, $2$ transverse). The phonon density of states in 3D is:</p>\n<div class=\"math-display\">\n$$g(\\omega) d\\omega = \\frac{V}{2\\pi^2} \\left( \\frac{1}{v_L^3} + \\frac{2}{v_T^3} \\right) \\omega^2 d\\omega = \\frac{3V}{2\\pi^2 v_s^3} \\omega^2 d\\omega$$\n</div>\n<p>Debye imposed a high-frequency cut-off, the <strong>Debye cut-off frequency</strong> $\\omega_D$, to ensure the total number of modes equals $3N$:</p>\n<div class=\"math-display\">\n$$\\int_0^{\\omega_D} g(\\omega) d\\omega = 3N \\implies \\omega_D = v_s \\left( \\frac{6\\pi^2 N}{V} \\right)^{1/3}, \\quad \\Theta_D = \\frac{\\hbar \\omega_D}{k_B}$$\n</div>\n<p>The total thermal vibrational internal energy is:</p>\n<div class=\"math-display\">\n$$U = \\int_0^{\\omega_D} \\frac{\\hbar\\omega}{e^{\\hbar\\omega/k_BT} - 1} g(\\omega) d\\omega = 9 N k_B T \\left(\\frac{T}{\\Theta_D}\\right)^3 \\int_0^{\\Theta_D/T} \\frac{x^3}{e^x - 1} dx \\quad \\left(x = \\frac{\\hbar\\omega}{k_BT}\\right)$$\n</div>\n<p>Differentiating with respect to $T$ in the low-temperature limit ($T \\ll \\Theta_D$), the upper limit goes to infinity: $\\int_0^\\infty \\frac{x^3}{e^x - 1} dx = \\frac{\\pi^4}{15}$. This yields the celebrated <strong>Debye $T^3$ Law</strong>:</p>\n<div class=\"math-display\">\n$$C_V = \\frac{12\\pi^4}{5} N k_B \\left( \\frac{T}{\\Theta_D} \\right)^3 \\propto T^3 \\quad (T \\to 0\\text{ K})$$\n</div>\n<p>This matches experimental specific heat measurements for all non-magnetic insulating solids.</p>"
        },
        {
          "id": "ssp-3-5",
          "title": "Anharmonicity, Thermal Expansion & Normal vs Umklapp Processes",
          "content": "<h4>1. Anharmonic Effects & Thermal Expansion</h4>\n<p>In a purely harmonic potential $V(x) = \\frac{1}{2} c x^2$, the potential well is symmetric about $x = 0$. The thermal average displacement vanishes at all temperatures: $\\langle x \\rangle = \\frac{\\int x e^{-V(x)/k_BT} dx}{\\int e^{-V(x)/k_BT} dx} = 0$, implying zero thermal expansion. Thermal expansion is an intrinsically <em>anharmonic</em> phenomenon.</p>\n<p>Expanding the interatomic potential including cubic ($g x^3$) and quartic ($f x^4$) anharmonic perturbations:</p>\n<div class=\"math-display\">\n$$V(x) = c x^2 - g x^3 - f x^4$$\n</div>\n<p>Calculating the thermal average position using the Boltzmann distribution yields:</p>\n<div class=\"math-display\">\n$$\\langle x \\rangle = \\frac{\\int_{-\\infty}^{\\infty} x e^{-\\beta(cx^2 - gx^3 - fx^4)} dx}{\\int_{-\\infty}^{\\infty} e^{-\\beta(cx^2 - gx^3 - fx^4)} dx} \\approx \\frac{3g}{4c^2} k_B T$$\n</div>\n<p>The linear thermal expansion coefficient $\\alpha_{\\text{th}} = \\frac{1}{a} \\frac{d\\langle x \\rangle}{dT} = \\frac{3g k_B}{4c^2 a}$ is directly proportional to the cubic anharmonic coefficient $g$.</p>\n\n<h4>2. Lattice Thermal Conductivity $\\kappa$</h4>\n<p>Heat conduction by phonons is described by the kinetic theory formula:</p>\n<div class=\"math-display\">\n$$\\kappa = \\frac{1}{3} C_V v_s \\ell_{\\text{ph}}$$\n</div>\n<p>where $C_V$ is the phonon heat capacity per unit volume, $v_s$ is the mean sound velocity, and $\\ell_{\\text{ph}} = v_s \\tau_{\\text{ph}}$ is the phonon mean free path.</p>\n\n<h4>3. Normal ($N$) vs. Umklapp ($U$) Phonon Scattering Processes</h4>\n<p>In three-phonon scattering collisions ($\\vec{q}_1 + \\vec{q}_2 = \\vec{q}_3 + \\vec{G}$):</p>\n<ul>\n<li><strong>Normal ($N$) Processes ($\\vec{G} = 0$):</strong> $\\vec{q}_1 + \\vec{q}_2 = \\vec{q}_3$. Total phonon crystal momentum is conserved. $N$-processes redistribute energy among phonon modes but do not produce thermal resistance (they cannot decay a net heat current).</li>\n<li><strong>Umklapp ($U$) Processes ($\\vec{G} \\neq 0$):</strong> $\\vec{q}_1 + \\vec{q}_2 = \\vec{q}_3 + \\vec{G}$. When two high-energy phonons collide such that $\\vec{q}_1 + \\vec{q}_2$ falls outside the First Brillouin Zone, it is Bragg-reflected back into the zone by subtracting a reciprocal lattice vector $\\vec{G}$. This <em>reverses</em> the direction of the resultant energy flow, destroying net crystal momentum and creating intrinsic <strong>lattice thermal resistivity</strong>.</li>\n</ul>\n<p>At high temperatures ($T \\gg \\Theta_D$), the number of excited high-energy phonons scales as $n_{\\text{ph}} \\propto T$, so $\\ell_{\\text{ph}} \\propto 1/T$, yielding $\\kappa \\propto 1/T$. At very low temperatures, $U$-processes freeze out as $e^{-\\Theta_D / 2T}$, and $\\ell_{\\text{ph}}$ is limited only by sample boundary scattering ($\\ell_{\\text{ph}} \\approx \\text{const}$), so $\\kappa \\propto C_V \\propto T^3$.</p>"
        }
      ],
      "problems": [
        {
          "id": "ssp-p-3-1",
          "title": "Acoustic Cut-Off Frequency and Sound Velocity of Monatomic Aluminum",
          "statement": "Monatomic aluminum crystallizes in a 1D linear model with atomic mass $M = 26.98 \\text{ u} = 4.480 \\times 10^{-26} \\text{ kg}$, interatomic spacing $a = 2.86 \\text{ \u00c5}$, and interatomic spring constant $C = 25.0 \\text{ N/m}$. (a) Calculate the longitudinal sound velocity $v_s$. (b) Determine the maximum acoustic cut-off angular frequency $\\omega_{\\text{max}}$ and corresponding cyclical frequency $\\nu_{\\text{max}}$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Sound Velocity v_s",
              "math": "v_s = a \\sqrt{\\frac{C}{M}} = (2.86 \\times 10^{-10}\\text{ m}) \\sqrt{\\frac{25.0\\text{ N/m}}{4.480 \\times 10^{-26}\\text{ kg}}} = (2.86 \\times 10^{-10}) \\sqrt{5.580 \\times 10^{26}} \\approx (2.86 \\times 10^{-10}) \\times (2.362 \\times 10^{13}) \\approx 6756\\text{ m/s}",
              "explanation": "Evaluate the continuum limit sound velocity v_s = a * sqrt(C / M)."
            },
            {
              "stepName": "Step 2: Calculate the Maximum Cut-Off Angular Frequency",
              "math": "\\omega_{\\text{max}} = 2 \\sqrt{\\frac{C}{M}} = 2 \\times (2.362 \\times 10^{13}\\text{ rad/s}) \\approx 4.724 \\times 10^{13}\\text{ rad/s}",
              "explanation": "At the Brillouin zone boundary k = pi / a, omega_max = 2 * sqrt(C / M)."
            },
            {
              "stepName": "Step 3: Calculate the Cyclical Frequency nu_max",
              "math": "\\nu_{\\text{max}} = \\frac{\\omega_{\\text{max}}}{2\\pi} = \\frac{4.724 \\times 10^{13}\\text{ rad/s}}{2\\pi} \\approx 7.519 \\times 10^{12}\\text{ Hz} = 7.52\\text{ THz}",
              "explanation": "Convert angular frequency to cyclical frequency in Terahertz (THz)."
            }
          ],
          "answer": "v_s = 6756 \\text{ m/s}, \\quad \\omega_{\\text{max}} = 4.72 \\times 10^{13} \\text{ rad/s}, \\quad \\nu_{\\text{max}} = 7.52 \\text{ THz}"
        },
        {
          "id": "ssp-p-3-2",
          "title": "Diatomic Chain Phonon Branches and Band Gap for Sodium Chloride",
          "statement": "Model a 1D chain of rock-salt $\\text{NaCl}$ with alternating sodium ions ($M_1 = 22.99 \\text{ u} = 3.818 \\times 10^{-26} \\text{ kg}$) and chlorine ions ($M_2 = 35.45 \\text{ u} = 5.887 \\times 10^{-26} \\text{ kg}$) connected by springs with constant $C = 15.0 \\text{ N/m}$. (a) Calculate the optical phonon frequency $\\omega_{\\text{opt}}$ at $k = 0$. (b) Calculate the optical and acoustic frequencies at the zone boundary $k = \\pi/a$, and determine the width of the forbidden phononic band gap $\\Delta \\omega$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Reduced Mass mu of the Ion Pair",
              "math": "\\mu = \\frac{M_1 M_2}{M_1 + M_2} = \\frac{(3.818 \\times 10^{-26})(5.887 \\times 10^{-26})}{3.818 \\times 10^{-26} + 5.887 \\times 10^{-26}}\\text{ kg} = \\frac{2.2477 \\times 10^{-51}}{9.705 \\times 10^{-26}} \\approx 2.316 \\times 10^{-26}\\text{ kg}",
              "explanation": "Compute the reduced mass mu = M1 * M2 / (M1 + M2)."
            },
            {
              "stepName": "Step 2: Calculate the Optical Frequency at k = 0",
              "math": "\\omega_{\\text{opt}}(0) = \\sqrt{\\frac{2C}{\\mu}} = \\sqrt{\\frac{2 \\times 15.0\\text{ N/m}}{2.316 \\times 10^{-26}\\text{ kg}}} = \\sqrt{1.295 \\times 10^{27}} \\approx 3.599 \\times 10^{13}\\text{ rad/s} \\implies \\nu_{\\text{opt}}(0) = 5.73\\text{ THz}",
              "explanation": "At the zone center, the optical frequency is governed by the relative oscillation of both masses."
            },
            {
              "stepName": "Step 3: Calculate Zone Boundary Frequencies at k = pi / a",
              "math": "\\omega_1 = \\sqrt{\\frac{2C}{M_2}} = \\sqrt{\\frac{30.0}{5.887 \\times 10^{-26}}} \\approx 2.258 \\times 10^{13}\\text{ rad/s}, \\quad \\omega_2 = \\sqrt{\\frac{2C}{M_1}} = \\sqrt{\\frac{30.0}{3.818 \\times 10^{-26}}} \\approx 2.803 \\times 10^{13}\\text{ rad/s}",
              "explanation": "At k = pi / a, the acoustic branch terminates at sqrt(2C / M_heavy) and the optical branch terminates at sqrt(2C / M_light)."
            },
            {
              "stepName": "Step 4: Compute the Forbidden Phononic Band Gap Delta omega",
              "math": "\\Delta \\omega = \\omega_2 - \\omega_1 = (2.803 - 2.258) \\times 10^{13}\\text{ rad/s} = 0.545 \\times 10^{13}\\text{ rad/s} \\implies \\Delta \\nu \\approx 0.867\\text{ THz}",
              "explanation": "The gap between the top of the acoustic branch and the bottom of the optical branch."
            }
          ],
          "answer": "\\omega_{\\text{opt}}(0) = 3.60 \\times 10^{13} \\text{ rad/s}, \\quad \\Delta \\omega = 5.45 \\times 10^{12} \\text{ rad/s} \\quad (\\Delta \\nu = 0.87 \\text{ THz})"
        },
        {
          "id": "ssp-p-3-3",
          "title": "Debye Temperature and Low-Temperature Heat Capacity of Diamond",
          "statement": "Diamond has a density of $\\rho = 3.515 \\text{ g/cm}^3$ and atomic molar mass $M = 12.011 \\text{ g/mol}$. Its average sound velocity is $v_s = 1.20 \\times 10^4 \\text{ m/s}$. (a) Calculate the atomic number density $N/V$. (b) Determine the Debye cut-off frequency $\\omega_D$ and the Debye temperature $\\Theta_D$. (c) Evaluate the molar lattice heat capacity $C_V$ of diamond at $T = 30 \\text{ K}$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Atomic Number Density N / V",
              "math": "\\frac{N}{V} = \\frac{\\rho N_A}{M} = \\frac{(3.515 \\times 10^6\\text{ g/m}^3)(6.022 \\times 10^{23}\\text{ mol}^{-1})}{12.011\\text{ g/mol}} \\approx 1.762 \\times 10^{29}\\text{ atoms/m}^3",
              "explanation": "Compute atomic number density from mass density and molar mass."
            },
            {
              "stepName": "Step 2: Calculate the Debye Cut-Off Frequency omega_D",
              "math": "\\omega_D = v_s \\left( 6\\pi^2 \\frac{N}{V} \\right)^{1/3} = (1.20 \\times 10^4\\text{ m/s}) \\left[ 6\\pi^2 (1.762 \\times 10^{29}) \\right]^{1/3} = (1.20 \\times 10^4) (1.043 \\times 10^{31})^{1/3} \\approx (1.20 \\times 10^4)(2.185 \\times 10^{10}) \\approx 2.622 \\times 10^{14}\\text{ rad/s}",
              "explanation": "Evaluate the 3D Debye frequency formula."
            },
            {
              "stepName": "Step 3: Calculate the Debye Temperature Theta_D",
              "math": "\\Theta_D = \\frac{\\hbar \\omega_D}{k_B} = \\frac{(1.0546 \\times 10^{-34}\\text{ J}\\cdot\\text{s})(2.622 \\times 10^{14}\\text{ rad/s})}{1.3806 \\times 10^{-23}\\text{ J/K}} \\approx \\frac{2.765 \\times 10^{-20}}{1.3806 \\times 10^{-23}} \\approx 2003\\text{ K}",
              "explanation": "Convert Debye frequency to Debye temperature."
            },
            {
              "stepName": "Step 4: Calculate Molar Heat Capacity at T = 30 K using the T^3 Law",
              "math": "C_V = \\frac{12\\pi^4}{5} R \\left(\\frac{T}{\\Theta_D}\\right)^3 = \\frac{12\\pi^4}{5} (8.314\\text{ J/mol}\\cdot\\text{K}) \\left(\\frac{30\\text{ K}}{2003\\text{ K}}\\right)^3 \\approx 1943.8 \\times (1.498 \\times 10^{-2})^3 \\approx 1943.8 \\times 3.361 \\times 10^{-6} \\approx 6.53 \\times 10^{-3}\\text{ J}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1}",
              "explanation": "Apply the low-temperature Debye T^3 formula since T = 30 K is far below Theta_D = 2003 K."
            }
          ],
          "answer": "\\Theta_D \\approx 2003 \\text{ K}, \\quad C_V(30\\text{ K}) = 6.53 \\times 10^{-3} \\text{ J}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1}"
        }
      ]
    },
    {
      "unitNumber": 4,
      "unitId": "unit4-multielectron-atoms",
      "title": "Multi-Electron Atoms & Chemical Bonding in Solids",
      "description": "Quantum mechanics of many-electron systems: identical particles, exchange symmetry, Pauli exclusion principle, para- and ortho-helium, Hartree and Hartree-Fock self-consistent field methods, atomic multiplets, Hund's rules, characteristic X-ray spectra, and LCAO molecular orbital theory of covalent bonds.",
      "sections": [
        {
          "id": "ssp-4-1",
          "title": "Identical Particles, Permutation Symmetry & Pauli Principle",
          "content": "<h4>1. Indistinguishability & The Permutation Operator</h4>\n<p>In quantum mechanics, identical particles (such as electrons) are fundamentally indistinguishable. Consider a system of two identical particles described by coordinate vectors $\\xi_1 = (\\vec{r}_1, \\sigma_1)$ and $\\xi_2 = (\\vec{r}_2, \\sigma_2)$ combining spatial and spin coordinates. The permutation operator $\\hat{P}_{12}$ exchanges the particles:</p>\n<div class=\"math-display\">\n$$\\hat{P}_{12} \\Psi(\\xi_1, \\xi_2) = \\Psi(\\xi_2, \\xi_1)$$\n</div>\n<p>Because $\\hat{P}_{12}^2 = \\hat{I}$, its eigenvalues are $\\lambda = \\pm 1$. The <strong>Symmetrization Postulate</strong> partitions all physical particles in nature into two disjoint classes:</p>\n<ul>\n<li><strong>Bosons (Integer Spin $S = 0, 1, 2, \\dots$):</strong> Symmetric wavefunctions under exchange:\n<div class=\"math-display\">\n$$\\Psi(\\xi_2, \\xi_1) = + \\Psi(\\xi_1, \\xi_2)$$\n</div></li>\n<li><strong>Fermions (Half-Integer Spin $S = 1/2, 3/2, \\dots$):</strong> Antisymmetric wavefunctions under exchange:\n<div class=\"math-display\">\n$$\\Psi(\\xi_2, \\xi_1) = - \\Psi(\\xi_1, \\xi_2)$$\n</div></li>\n</ul>\n\n<h4>2. The Pauli Exclusion Principle & Slater Determinants</h4>\n<p>Electrons are spin-$1/2$ fermions, so the total wavefunction of an $N$-electron system must be completely antisymmetric under the exchange of any pair of electrons $i$ and $j$. If the electrons occupy single-particle spin-orbitals $\\chi_{\\alpha}(\\xi) = \\phi_a(\\vec{r}) \\chi_s(\\sigma)$, the total antisymmetric wavefunction is represented by a <strong>Slater Determinant</strong>:</p>\n<div class=\"math-display\">\n$$\\Psi(\\xi_1, \\xi_2, \\dots, \\xi_N) = \\frac{1}{\\sqrt{N!}} \\begin{vmatrix} \\chi_{\\alpha_1}(\\xi_1) & \\chi_{\\alpha_2}(\\xi_1) & \\dots & \\chi_{\\alpha_N}(\\xi_1) \\\\ \\chi_{\\alpha_1}(\\xi_2) & \\chi_{\\alpha_2}(\\xi_2) & \\dots & \\chi_{\\alpha_N}(\\xi_2) \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ \\chi_{\\alpha_1}(\\xi_N) & \\chi_{\\alpha_2}(\\xi_N) & \\dots & \\chi_{\\alpha_N}(\\xi_N) \\end{vmatrix}$$\n</div>\n<p>If two electrons occupy the identical quantum state ($\\alpha_1 = \\alpha_2$), two columns of the determinant are identical, causing $\\Psi \\equiv 0$. This establishes the <strong>Pauli Exclusion Principle</strong>: <em>no two electrons can occupy the same quantum state simultaneously</em>.</p>"
        },
        {
          "id": "ssp-4-2",
          "title": "The Helium Atom: Exchange Symmetry, Para- & Ortho-Helium",
          "content": "<h4>1. Helium Hamiltonian & Electron-Electron Repulsion</h4>\n<p>The non-relativistic Hamiltonian of the neutral Helium atom ($Z = 2$) with nucleus at the origin is:</p>\n<div class=\"math-display\">\n$$\\hat{H} = \\left( - \\frac{\\hbar^2}{2m} \\nabla_1^2 - \\frac{2e^2}{4\\pi\\varepsilon_0 r_1} \\right) + \\left( - \\frac{\\hbar^2}{2m} \\nabla_2^2 - \\frac{2e^2}{4\\pi\\varepsilon_0 r_2} \\right) + \\frac{e^2}{4\\pi\\varepsilon_0 |\\vec{r}_1 - \\vec{r}_2|} = \\hat{H}_1 + \\hat{H}_2 + \\hat{V}_{ee}$$\n</div>\n<p>The total two-electron wavefunction factors into spatial and spin parts: $\\Psi(\\xi_1, \\xi_2) = \\psi(\\vec{r}_1, \\vec{r}_2) \\chi_{\\text{spin}}(1, 2)$. Total antisymmetry requires:</p>\n<ul>\n<li><strong>Singlet State ($S = 0$, Para-Helium):</strong> Antisymmetric spin $\\chi_{0,0} = \\frac{1}{\\sqrt{2}}(\\alpha_1 \\beta_2 - \\beta_1 \\alpha_2)$ coupled to a <strong>symmetric spatial wavefunction</strong>:\n<div class=\"math-display\">\n$$\\psi_+(\\vec{r}_1, \\vec{r}_2) = \\frac{1}{\\sqrt{2}} [\\phi_a(\\vec{r}_1)\\phi_b(\\vec{r}_2) + \\phi_b(\\vec{r}_1)\\phi_a(\\vec{r}_2)]$$\n</div></li>\n<li><strong>Triplet State ($S = 1$, Ortho-Helium):</strong> Symmetric spin ($M_S = +1, 0, -1$) coupled to an <strong>antisymmetric spatial wavefunction</strong>:\n<div class=\"math-display\">\n$$\\psi_-(\\vec{r}_1, \\vec{r}_2) = \\frac{1}{\\sqrt{2}} [\\phi_a(\\vec{r}_1)\\phi_b(\\vec{r}_2) - \\phi_b(\\vec{r}_1)\\phi_a(\\vec{r}_2)]$$\n</div></li>\n</ul>\n\n<h4>2. Direct and Exchange Integrals</h4>\n<p>Evaluating the expectation value of the electron-electron Coulomb repulsion $\\hat{V}_{ee}$ in first-order perturbation theory:</p>\n<div class=\"math-display\">\n$$\\langle \\hat{V}_{ee} \\rangle_{\\pm} = \\iint |\\psi_{\\pm}(\\vec{r}_1, \\vec{r}_2)|^2 \\frac{e^2}{4\\pi\\varepsilon_0 r_{12}} d^3r_1 d^3r_2 = J \\pm K$$\n</div>\n<p>where:</p>\n<ul>\n<li><strong>Direct Coulomb Integral $J$:</strong> Classical electrostatic repulsion between the two electron charge clouds:\n<div class=\"math-display\">\n$$J = \\iint |\\phi_a(\\vec{r}_1)|^2 \\frac{e^2}{4\\pi\\varepsilon_0 r_{12}} |\\phi_b(\\vec{r}_2)|^2 d^3r_1 d^3r_2 > 0$$\n</div></li>\n<li><strong>Exchange Integral $K$:</strong> Purely quantum mechanical energy shift arising from the overlap of the two single-particle orbitals:\n<div class=\"math-display\">\n$$K = \\iint \\phi_a^*(\\vec{r}_1) \\phi_b^*(\\vec{r}_2) \\frac{e^2}{4\\pi\\varepsilon_0 r_{12}} \\phi_b(\\vec{r}_1) \\phi_a(\\vec{r}_2) d^3r_1 d^3r_2 > 0$$\n</div></li>\n</ul>\n<p>The total energy eigenvalues are: $E_{\\text{singlet}} = E_0 + J + K$ and $E_{\\text{triplet}} = E_0 + J - K$. The triplet state (ortho-helium) lies lower in energy than the singlet state (para-helium) by the <strong>exchange splitting</strong> $\\Delta E = 2K$. In the triplet state, $\\psi_-(\\vec{r}, \\vec{r}) = 0$, meaning electrons avoid each other in space, reducing Coulomb repulsion.</p>"
        },
        {
          "id": "ssp-4-3",
          "title": "Hartree & Hartree-Fock Self-Consistent Field (SCF) Methods",
          "simulation": "ssp-hartree-scf-sim",
          "content": "<h4>1. The Central Field Approximation</h4>\n<p>In multi-electron atoms and solids with $N$ electrons, the exact many-body Schr\u00f6dinger equation cannot be solved analytically. In the <strong>central field approximation</strong>, each electron moves independently in an effective spherically symmetric potential $V_{\\text{eff}}(r)$ created by the nucleus plus the spherically averaged charge distribution of all other $N-1$ electrons:</p>\n<div class=\"math-display\">\n$$\\hat{H}_i \\phi_i(\\vec{r}_i) = \\left( - \\frac{\\hbar^2}{2m}\\nabla_i^2 + V_{\\text{eff}}(r_i) \\right) \\phi_i(\\vec{r}_i) = \\varepsilon_i \\phi_i(\\vec{r}_i)$$\n</div>\n\n<h4>2. The Hartree Self-Consistent Field (SCF) Method</h4>\n<p>Douglas Hartree (1928) formulated an iterative variational procedure. Assuming a trial product wavefunction $\\Psi = \\phi_1(\\vec{r}_1)\\phi_2(\\vec{r}_2)\\dots\\phi_N(\\vec{r}_N)$, electron $i$ experiences an electrostatic potential produced by the charge density $\\rho_j(\\vec{r}') = -e |\\phi_j(\\vec{r}')|^2$ of all other electrons:</p>\n<div class=\"math-display\">\n$$V_i^{\\text{Hartree}}(\\vec{r}) = - \\frac{Ze^2}{4\\pi\\varepsilon_0 r} + \\sum_{j \\neq i} \\int \\frac{e^2 |\\phi_j(\\vec{r}')|^2}{4\\pi\\varepsilon_0 |\\vec{r} - \\vec{r}'|} d^3r'$$\n</div>\n<p>The self-consistent iteration cycle proceeds as follows:</p>\n<ol>\n<li>Guess an initial set of radial wavefunctions $\\{\\phi_j^{(0)}\\}$.</li>\n<li>Compute the electronic charge density $\\rho^{(0)}(\\vec{r})$ and the Hartree potential $V_i^{(0)}(\\vec{r})$.</li>\n<li>Solve the single-particle Schr\u00f6dinger equations to obtain a new set of wavefunctions $\\{\\phi_j^{(1)}\\}$.</li>\n<li>Repeat steps 2\u20133 iteratively until the input and output potentials converge within a numerical tolerance: $|V^{(k+1)} - V^{(k)}| < \\delta$.</li>\n</ol>\n\n<h4>3. The Hartree-Fock Method & Non-Local Exchange Potential</h4>\n<p>The simple Hartree product fails to satisfy the Pauli principle. Fock (1930) replaced the product with a fully antisymmetric Slater determinant, introducing an additional non-local <strong>exchange potential</strong> $V_{\\text{ex}}$:</p>\n<div class=\"math-display\">\n$$\\left( - \\frac{\\hbar^2}{2m}\\nabla^2 + V_{\\text{nuc}}(\\vec{r}) + V_{\\text{Coulomb}}(\\vec{r}) \\right) \\phi_i(\\vec{r}) - \\sum_{j} \\left[ \\int \\frac{e^2 \\phi_j^*(\\vec{r}') \\phi_i(\\vec{r}')}{4\\pi\\varepsilon_0 |\\vec{r} - \\vec{r}'|} d^3r' \\right] \\phi_j(\\vec{r}) = \\varepsilon_i \\phi_i(\\vec{r})$$\n</div>\n<p>The exchange operator acts only between electrons with parallel spins, creating a surrounding depletion zone known as the <strong>Fermi hole</strong> (or exchange hole).</p>"
        },
        {
          "id": "ssp-4-4",
          "title": "Hund's Rules, Characteristic X-Rays & Molecular LCAO Bonding",
          "simulation": "ssp-lcao-molecular-orbital-sim",
          "content": "<h4>1. Hund's Rules for Atomic Ground States</h4>\n<p>For multi-electron open subshells ($p^n, d^n, f^n$), electrostatic repulsion and spin-orbit coupling determine the energetic ordering of spectroscopic term symbols $^{2S+1}L_J$ via <strong>Hund's three empirical rules</strong>:</p>\n<ol>\n<li><strong>Rule 1 (Maximize Spin Multiplicity $S$):</strong> The ground state term has the maximum total spin $S$ permitted by the Pauli exclusion principle (minimizes Coulomb repulsion by maximizing exchange stabilization).</li>\n<li><strong>Rule 2 (Maximize Total Orbital Angular Momentum $L$):</strong> For a given $S$, the ground state has the maximum total orbital angular momentum $L$ (electrons orbit in the same sense, minimizing spatial close encounters).</li>\n<li><strong>Rule 3 (Spin-Orbit Coupling $J$):</strong>\n<ul>\n<li>If the subshell is <em>less than half full</em>, the lowest energy level has minimum total angular momentum: $J = |L - S|$.</li>\n<li>If the subshell is <em>more than half full</em>, the lowest energy level has maximum total angular momentum: $J = L + S$.</li>\n</ul></li>\n</ol>\n\n<h4>2. Characteristic X-Ray Spectra & Moseley's Law</h4>\n<p>When high-energy electrons eject an inner-core atomic electron, vacancies are filled by radiative transitions from outer shells, producing sharp characteristic X-ray lines:</p>\n<ul>\n<li>$K_\\alpha$ line: transition from $n = 2$ ($L$-shell) to $n = 1$ ($K$-shell).</li>\n<li>$K_\\beta$ line: transition from $n = 3$ ($M$-shell) to $n = 1$ ($K$-shell).</li>\n<li>$L_\\alpha$ line: transition from $n = 3$ ($M$-shell) to $n = 2$ ($L$-shell).</li>\n</ul>\n<p>Henry Moseley (1913) discovered that the frequency $\\nu$ of characteristic X-rays is related linearly to the atomic number $Z$:</p>\n<div class=\"math-display\">\n$$\\sqrt{\\nu} = a (Z - b)$$\n</div>\n<p>For the $K_\\alpha$ line, $b = 1$ (the remaining $1s$ electron screens one unit of nuclear charge), yielding:</p>\n<div class=\"math-display\">\n$$\\nu_{K_\\alpha} = R_c c (Z - 1)^2 \\left( \\frac{1}{1^2} - \\frac{1}{2^2} \\right) = \\frac{3}{4} R_c c (Z - 1)^2$$\n</div>\n\n<h4>3. Molecular Orbital Theory & LCAO Covalent Bonding</h4>\n<p>In solids, atomic orbitals overlap to form extended molecular orbitals. In the simplest diatomic system ($\\text{H}_2^+$ and $\\text{H}_2$), Linear Combination of Atomic Orbitals (LCAO) yields two molecular orbitals from atomic hydrogen $1s$ states $\\phi_A$ and $\\phi_B$:</p>\n<ul>\n<li><strong>Bonding Orbital ($\\sigma_g$):</strong> $\\psi_+ = \\frac{1}{\\sqrt{2(1+S)}} (\\phi_A + \\phi_B)$. Large electron probability density $|\\psi_+|^2$ builds up between the two positively charged nuclei, screening their Coulomb repulsion and lowering the total electronic energy.</li>\n<li><strong>Antibonding Orbital ($\\sigma_u^*$):</strong> $\\psi_- = \\frac{1}{\\sqrt{2(1-S)}} (\\phi_A - \\phi_B)$. Nodal plane ($\\psi = 0$) midway between the nuclei pushes electron density away, increasing nuclear repulsion and raising the energy.</li>\n</ul>"
        }
      ],
      "problems": [
        {
          "id": "ssp-p-4-1",
          "title": "Exchange Splitting in the Helium (1s)(2s) Excited Configuration",
          "statement": "In the excited $(1s)(2s)$ configuration of the Helium atom, the direct Coulomb integral is $J = 8.78 \\text{ eV}$ and the exchange integral is $K = 1.19 \\text{ eV}$. The unperturbed two-electron energy level is $E_0 = -59.38 \\text{ eV}$. (a) Calculate the total energies of the singlet state ($1^1S_0$, para-helium) and the triplet state ($2^3S_1$, ortho-helium). (b) Determine the exchange splitting energy $\\Delta E$ and explain physically why the triplet state lies lower in energy.",
          "steps": [
            {
              "stepName": "Step 1: Formulate Energy Expressions for Singlet and Triplet States",
              "math": "E_{\\text{singlet}} = E_0 + J + K, \\quad E_{\\text{triplet}} = E_0 + J - K",
              "explanation": "In the singlet state, the spatial wavefunction is symmetric (J + K), while in the triplet state it is antisymmetric (J - K)."
            },
            {
              "stepName": "Step 2: Calculate Numerical Energy of the Singlet State (Para-Helium)",
              "math": "E_{\\text{singlet}} = -59.38\\text{ eV} + 8.78\\text{ eV} + 1.19\\text{ eV} = -49.41\\text{ eV}",
              "explanation": "Evaluate E_singlet."
            },
            {
              "stepName": "Step 3: Calculate Numerical Energy of the Triplet State (Ortho-Helium)",
              "math": "E_{\\text{triplet}} = -59.38\\text{ eV} + 8.78\\text{ eV} - 1.19\\text{ eV} = -51.79\\text{ eV}",
              "explanation": "Evaluate E_triplet."
            },
            {
              "stepName": "Step 4: Compute the Exchange Splitting Delta E",
              "math": "\\Delta E = E_{\\text{singlet}} - E_{\\text{triplet}} = 2K = 2 \\times 1.19\\text{ eV} = 2.38\\text{ eV}",
              "explanation": "The exchange splitting equals twice the exchange integral."
            }
          ],
          "answer": "E_{\\text{singlet}} = -49.41 \\text{ eV}, \\quad E_{\\text{triplet}} = -51.79 \\text{ eV}, \\quad \\Delta E = 2.38 \\text{ eV}"
        },
        {
          "id": "ssp-p-4-2",
          "title": "Ground State Spectroscopic Term Symbols for Carbon and Iron",
          "statement": "Use Hund's rules to determine the ground state spectroscopic term symbol $^{2S+1}L_J$ for: (a) Carbon (neutral atom, valence subshell $2p^2$). (b) Iron ($\\text{Fe}^{2+}$ ion, valence subshell $3d^6$).",
          "steps": [
            {
              "stepName": "Step 1: Carbon 2p^2 Configuration (l = 1, 2 electrons)",
              "math": "S = \\frac{1}{2} + \\frac{1}{2} = 1 \\implies 2S+1 = 3 \\quad (\\text{Triplet})",
              "explanation": "Rule 1: Maximize S. Place both electrons with parallel spins in different m_l orbitals: m_s = +1/2, +1/2."
            },
            {
              "stepName": "Step 2: Maximize L for Carbon and Determine J",
              "math": "L = m_{l,1} + m_{l,2} = 1 + 0 = 1 \\implies P \\text{ state}",
              "explanation": "Rule 2: Maximize L using available m_l in {+1, 0, -1}. Placing electrons in m_l = +1 and m_l = 0 gives L = 1."
            },
            {
              "stepName": "Step 3: Determine J for Carbon (Less than Half Full)",
              "math": "J = |L - S| = |1 - 1| = 0 \\implies {^3P_0}",
              "explanation": "Rule 3: The 2p subshell is less than half full (2 of 6 electrons), so J = |L - S| = 0. The ground state is ^3P_0."
            },
            {
              "stepName": "Step 4: Iron Fe^2+ 3d^6 Configuration (l = 2, 6 electrons)",
              "math": "S = 5 \\times \\left(\\frac{1}{2}\\right) - 1 \\times \\left(\\frac{1}{2}\\right) = 2 \\implies 2S+1 = 5 \\quad (\\text{Quintet})",
              "explanation": "Rule 1: Place 5 electrons spin-up in m_l = +2, +1, 0, -1, -2 and the 6th electron spin-down in m_l = +2. S = 2."
            },
            {
              "stepName": "Step 5: Maximize L and Determine J for Fe^2+ (More than Half Full)",
              "math": "L = (+2) + (+1) + (0) + (-1) + (-2) + (+2) = 2 \\implies D \\text{ state}, \\quad J = L + S = 2 + 2 = 4 \\implies {^5D_4}",
              "explanation": "Rule 2: L = 2 (D state). Rule 3: The 3d subshell is more than half full (6 of 10 electrons), so J = L + S = 4. The ground state is ^5D_4."
            }
          ],
          "answer": "\\text{Carbon: } {^3P_0}, \\quad \\text{Iron (Fe}^{2+}\\text{): } {^5D_4}"
        },
        {
          "id": "ssp-p-4-3",
          "title": "Moseley's Law and Characteristic K_alpha X-Ray Wavelength for Copper",
          "statement": "Copper has atomic number $Z = 29$. The Rydberg constant is $R_\\infty = 1.09737 \\times 10^7 \\text{ m}^{-1}$. Using Moseley's law with screening constant $b = 1.0$ for the $K_\\alpha$ transition: (a) Calculate the cyclical frequency $\\nu_{K_\\alpha}$ of the emitted X-ray photon. (b) Determine the wavelength $\\lambda_{K_\\alpha}$ in Angstroms and the photon energy in $\\text{keV}$.",
          "steps": [
            {
              "stepName": "Step 1: Formulate Moseley's Equation for the K_alpha Line",
              "math": "\\nu_{K_\\alpha} = \\frac{3}{4} c R_\\infty (Z - 1)^2",
              "explanation": "The K_alpha transition originates from n=2 to n=1 with screening factor b=1."
            },
            {
              "stepName": "Step 2: Calculate the Cyclical Frequency nu",
              "math": "\\nu_{K_\\alpha} = \\frac{3}{4} \\times (2.9979 \\times 10^8\\text{ m/s}) \\times (1.09737 \\times 10^7\\text{ m}^{-1}) \\times (29 - 1)^2 = (2.4673 \\times 10^{15}) \\times (28)^2 \\approx (2.4673 \\times 10^{15}) \\times 784 \\approx 1.9344 \\times 10^{18}\\text{ Hz}",
              "explanation": "Substitute c, R_infinity, and Z=29 into the formula."
            },
            {
              "stepName": "Step 3: Calculate the Wavelength lambda",
              "math": "\\lambda_{K_\\alpha} = \\frac{c}{\\nu_{K_\\alpha}} = \\frac{2.9979 \\times 10^8\\text{ m/s}}{1.9344 \\times 10^{18}\\text{ s}^{-1}} \\approx 1.5498 \\times 10^{-10}\\text{ m} = 1.550\\text{ \\AA}",
              "explanation": "Compute lambda = c / nu. This closely matches the experimental Cu K_alpha value of 1.541 Angstroms."
            },
            {
              "stepName": "Step 4: Calculate the Photon Energy in keV",
              "math": "E = h \\nu = \\frac{12398.4\\text{ eV}\\cdot\\text{\\AA}}{1.5498\\text{ \\AA}} \\approx 8000\\text{ eV} = 8.00\\text{ keV}",
              "explanation": "Convert wavelength to energy in keV."
            }
          ],
          "answer": "\\nu_{K_\\alpha} = 1.934 \\times 10^{18} \\text{ Hz}, \\quad \\lambda_{K_\\alpha} = 1.550 \\text{ \u00c5}, \\quad E = 8.00 \\text{ keV}"
        }
      ]
    },
    {
      "unitNumber": 5,
      "unitId": "unit5-free-electron-theory",
      "title": "Free Electron Theory of Metals & Fermi Surfaces",
      "description": "Comprehensive electronic transport in metals: classical Drude phenomenology, Sommerfeld quantum free Fermi gas, 1D/2D/3D density of states, Fermi-Dirac statistics, Fermi energy and velocity, linear electronic heat capacity, Pauli paramagnetism, Hall effect, Wiedemann-Franz law, and Matthiessen's rule.",
      "sections": [
        {
          "id": "ssp-5-1",
          "title": "Drude Classical Phenomenology of Electrical & Thermal Conduction",
          "content": "<h4>1. Postulates of the Drude Model (1900)</h4>\n<p>Paul Drude treated valence electrons in a metal as an ideal classical gas of non-interacting point particles of mass $m$ and charge $-e$, moving through a static background of positive ion cores:</p>\n<ol>\n<li><strong>Independent & Free Electron Approximation:</strong> Electron-electron and electron-ion interactions are neglected between collisions.</li>\n<li><strong>Relaxation-Time Approximation:</strong> Collisions are instantaneous, random events occurring with an average probability per unit time $1/\\tau$, where $\\tau$ is the <strong>relaxation time</strong> (mean free time between collisions).</li>\n<li><strong>Thermal Equilibrium:</strong> Electrons emerge from each collision in thermal equilibrium with the local lattice temperature, with zero average drift velocity.</li>\n</ol>\n\n<h4>2. Derivation of Ohm's Law and DC Electrical Conductivity</h4>\n<p>Under an applied macroscopic electric field $\\vec{E}$, the equation of motion for the average drift velocity $\\vec{v}_d$ of an electron is:</p>\n<div class=\"math-display\">\n$$m \\frac{d\\vec{v}_d}{dt} = - e \\vec{E} - \\frac{m \\vec{v}_d}{\\tau}$$\n</div>\n<p>In steady state ($d\\vec{v}_d/dt = 0$):</p>\n<div class=\"math-display\">\n$$\\vec{v}_d = - \\frac{e \\tau}{m} \\vec{E}$$\n</div>\n<p>The macroscopic electric current density $\\vec{J}$ carried by electron density $n$ is:</p>\n<div class=\"math-display\">\n$$\\vec{J} = - n e \\vec{v}_d = \\left( \\frac{n e^2 \\tau}{m} \\right) \\vec{E} = \\sigma_0 \\vec{E}$$\n</div>\n<p>This derives microscopic <strong>Ohm's Law</strong>, with DC electrical conductivity $\\sigma_0$ given by the <strong>Drude formula</strong>:</p>\n<div class=\"math-display\">\n$$\\sigma_0 = \\frac{n e^2 \\tau}{m} = n e \\mu$$\n</div>\n<p>where $\\mu = e\\tau/m$ is the electron drift mobility.</p>\n\n<h4>3. The Classical Wiedemann-Franz Law & Failure of Drude Model</h4>\n<p>Treating electrons as a classical Maxwell-Boltzmann gas with thermal conductivity $\\kappa = \\frac{1}{3} C_v v_{\\text{th}} \\ell$ and heat capacity $C_v = \\frac{3}{2} n k_B$:</p>\n<div class=\"math-display\">\n$$\\frac{\\kappa}{\\sigma T} = \\frac{3}{2} \\left(\\frac{k_B}{e}\\right)^2 \\approx 1.11 \\times 10^{-8}\\text{ W}\\cdot\\Omega\\cdot\\text{K}^{-2}$$\n</div>\n<p>While this qualitatively explained the empirical <strong>Wiedemann-Franz law</strong>, Drude's classical model suffered from a catastrophic failure: it predicted that the electronic heat capacity should contribute $\\frac{3}{2} R$ per mole, which was completely absent in room-temperature measurements.</p>"
        },
        {
          "id": "ssp-5-2",
          "title": "Sommerfeld Quantum Free Fermi Gas: Density of States in 1D, 2D & 3D",
          "simulation": "ssp-fermi-dirac-dos-sim",
          "content": "<h4>1. Schr\u00f6dinger Equation in a 3D Potential Well</h4>\n<p>Arnold Sommerfeld (1928) resolved the Drude paradox by applying quantum mechanics and Fermi-Dirac statistics to the valence electrons. Consider $N$ free electrons confined within a box of volume $V = L_x L_y L_z$ with periodic Born-von K\u00e1rm\u00e1n boundary conditions:</p>\n<div class=\"math-display\">\n$$- \\frac{\\hbar^2}{2m} \\nabla^2 \\psi(\\vec{r}) = E \\psi(\\vec{r}) \\implies \\psi_{\\vec{k}}(\\vec{r}) = \\frac{1}{\\sqrt{V}} e^{i \\vec{k}\\cdot\\vec{r}}$$\n</div>\n<p>The energy eigenvalues are continuous parabolic free-particle dispersions:</p>\n<div class=\"math-display\">\n$$E(\\vec{k}) = \\frac{\\hbar^2 k^2}{2m} = \\frac{\\hbar^2}{2m}(k_x^2 + k_y^2 + k_z^2)$$\n</div>\n<p>where allowed wavevectors form a uniform grid in reciprocal $\\vec{k}$-space: $k_i = \\frac{2\\pi n_i}{L_i}$ ($n_i \\in \\mathbb{Z}$). Each allowed state occupies a volume in $k$-space of $\\Delta k^3 = \\frac{(2\\pi)^3}{V}$.</p>\n\n<h4>2. Derivation of the Density of States $g(E)$ in 3D</h4>\n<p>Taking into account electron spin degeneracy ($g_s = 2$):</p>\n<div class=\"math-display\">\n$$N(k) = 2 \\times \\frac{\\frac{4}{3}\\pi k^3}{(2\\pi)^3 / V} = \\frac{V}{3\\pi^2} k^3$$\n</div>\n<p>Substituting $k = \\left(\\frac{2mE}{\\hbar^2}\\right)^{1/2}$:</p>\n<div class=\"math-display\">\n$$N(E) = \\frac{V}{3\\pi^2} \\left( \\frac{2mE}{\\hbar^2} \\right)^{3/2}$$\n</div>\n<p>The <strong>Density of States (DOS)</strong> $g(E) = \\frac{dN}{dE}$ per unit volume in three dimensions is:</p>\n<div class=\"math-display\">\n$$g_{\\text{3D}}(E) = \\frac{1}{V} \\frac{dN}{dE} = \\frac{1}{2\\pi^2} \\left(\\frac{2m}{\\hbar^2}\\right)^{3/2} E^{1/2} \\propto \\sqrt{E}$$\n</div>\n\n<h4>3. Dimensionality Comparison of Density of States</h4>\n<ul>\n<li><strong>1D (Quantum Wire):</strong> $g_{\\text{1D}}(E) = \\frac{\\sqrt{2m}}{\\pi \\hbar} E^{-1/2} \\propto E^{-1/2}$ (Van Hove singularity).</li>\n<li><strong>2D (Quantum Well):</strong> $g_{\\text{2D}}(E) = \\frac{m}{\\pi \\hbar^2} = \\text{constant}$ (energy-independent step functions).</li>\n<li><strong>3D (Bulk Metal):</strong> $g_{\\text{3D}}(E) = \\frac{m}{\\pi^2 \\hbar^3} \\sqrt{2mE} \\propto E^{1/2}$.</li>\n</ul>"
        },
        {
          "id": "ssp-5-3",
          "title": "Fermi-Dirac Statistics, Fermi Energy & Quantum Degeneracy",
          "content": "<h4>1. The Fermi-Dirac Distribution Function</h4>\n<p>Because electrons are indistinguishable fermions obeying the Pauli exclusion principle, the probability of an electronic state of energy $E$ being occupied at absolute temperature $T$ is given by the <strong>Fermi-Dirac distribution</strong>:</p>\n<div class=\"math-display\">\n$$f(E) = \\frac{1}{e^{(E - \\mu)/k_B T} + 1}$$\n</div>\n<p>where $\\mu(T)$ is the chemical potential. At $T = 0\\text{ K}$, the chemical potential is defined as the <strong>Fermi Energy</strong> $E_F \\equiv \\mu(0)$. The distribution becomes an exact step function:</p>\n<div class=\"math-display\">\n$$f(E) = \\begin{cases} 1, & E < E_F \\\\ 0, & E > E_F \\end{cases}$$\n</div>\n\n<h4>2. Calculation of the Fermi Energy $E_F$ and Fermi Surface</h4>\n<p>At $T = 0\\text{ K}$, $N$ electrons fill all available states in $k$-space up to a maximum radius, the <strong>Fermi wavevector</strong> $k_F$, enclosing a sphere known as the <strong>Fermi Sphere</strong>:</p>\n<div class=\"math-display\">\n$$n = \\frac{N}{V} = \\frac{1}{V} \\int_0^{E_F} g(E) dE = \\frac{k_F^3}{3\\pi^2} \\implies k_F = (3\\pi^2 n)^{1/3}$$\n</div>\n<p>The fundamental ground-state parameters of the free Fermi gas are:</p>\n<ul>\n<li><strong>Fermi Energy:</strong>\n<div class=\"math-display\">\n$$E_F = \\frac{\\hbar^2 k_F^2}{2m} = \\frac{\\hbar^2}{2m} (3\\pi^2 n)^{2/3}$$\n</div></li>\n<li><strong>Fermi Velocity:</strong>\n<div class=\"math-display\">\n$$v_F = \\frac{\\hbar k_F}{m} = \\frac{\\hbar}{m} (3\\pi^2 n)^{1/3}$$\n</div></li>\n<li><strong>Fermi Temperature:</strong>\n<div class=\"math-display\">\n$$T_F = \\frac{E_F}{k_B} \\sim 10^4 - 10^5\\text{ K}$$\n</div></li>\n</ul>\n<p>Because room temperature ($T \\approx 300\\text{ K}$) satisfies $T \\ll T_F$, valence electrons in typical metals form a <strong>highly degenerate Fermi gas</strong>.</p>"
        },
        {
          "id": "ssp-5-4",
          "title": "Electronic Heat Capacity & Pauli Paramagnetism",
          "content": "<h4>1. Quantum Suppression of Electronic Heat Capacity</h4>\n<p>When a metal is heated from $T = 0\\text{ K}$ to temperature $T$, the Pauli exclusion principle dictates that electrons with energies deep below the Fermi surface ($E < E_F - k_BT$) cannot absorb thermal energy, because all states within $\\sim k_BT$ above them are already occupied. Only electrons within a narrow thermal layer of width $\\sim k_BT$ around $E_F$ can undergo transitions.</p>\n<p>The fraction of thermally active electrons is approximately $\\frac{k_B T}{E_F} = \\frac{T}{T_F} \\sim 10^{-2}$. Each of these excited electrons acquires thermal energy $\\sim k_B T$, yielding an excess internal energy:</p>\n<div class=\"math-display\">\n$$\\Delta U_{el} \\approx \\left( N \\frac{T}{T_F} \\right) (k_B T) = N k_B \\frac{T^2}{T_F}$$\n</div>\n<p>Differentiating with respect to $T$ yields a heat capacity linear in temperature:</p>\n<div class=\"math-display\">\n$$C_{el} = \\frac{dU_{el}}{dT} \\approx 2 N k_B \\frac{T}{T_F} \\propto T$$\n</div>\n\n<h4>2. Rigorous Sommerfeld Expansion for $C_{el}$</h4>\n<p>Performing a rigorous Sommerfeld expansion of the internal energy integral $U(T) = \\int_0^\\infty E g(E) f(E) dE$ leads to the exact theoretical formula for the electronic heat capacity:</p>\n<div class=\"math-display\">\n$$C_{el} = \\frac{\\pi^2}{3} g(E_F) k_B^2 T = \\frac{\\pi^2}{2} N k_B \\left(\\frac{T}{T_F}\\right) = \\gamma T$$\n</div>\n<p>where $\\gamma = \\frac{\\pi^2}{3} g(E_F) k_B^2$ is the <strong>Sommerfeld coefficient</strong>.</p>\n<p>At liquid helium temperatures ($T < 10\\text{ K}$), the total heat capacity of a normal non-magnetic metal is the sum of electronic and phononic (Debye) contributions:</p>\n<div class=\"math-display\">\n$$C_V = C_{el} + C_{\\text{ph}} = \\gamma T + A T^3 \\implies \\frac{C_V}{T} = \\gamma + A T^2$$\n</div>\n<p>Plotting $C_V/T$ against $T^2$ yields a straight line whose $y$-intercept is $\\gamma$ and whose slope determines the Debye temperature $\\Theta_D$.</p>\n\n<h4>3. Pauli Paramagnetism of Conduction Electrons</h4>\n<p>In an external magnetic field $B$, electron spin magnetic moments $\\mu_B$ align parallel or antiparallel to the field, shifting the up- and down-spin sub-bands by $\\mp \\mu_B B$. At $T = 0\\text{ K}$, electrons near $E_F$ flip their spins into the lower energy sub-band until the Fermi levels equalize:</p>\n<div class=\"math-display\">\n$$\\Delta N = \\frac{1}{2} g(E_F) (\\mu_B B) - \\left(-\\frac{1}{2} g(E_F) \\mu_B B\\right) = g(E_F) \\mu_B B$$\n</div>\n<p>The resulting net magnetic magnetization is $M = \\Delta N \\mu_B = g(E_F) \\mu_B^2 B$. The <strong>Pauli paramagnetic susceptibility</strong> is:</p>\n<div class=\"math-display\">\n$$\\chi_{\\text{Pauli}} = \\frac{\\mu_0 M}{B} = \\mu_0 \\mu_B^2 g(E_F) = \\frac{3 \\mu_0 n \\mu_B^2}{2 E_F}$$\n</div>\n<p>Unlike classical Curie paramagnetism ($\\chi \\propto 1/T$), Pauli paramagnetism is completely temperature-independent, in perfect agreement with experimental data for alkali and noble metals.</p>"
        },
        {
          "id": "ssp-5-5",
          "title": "The Hall Effect, Wiedemann-Franz Law & Matthiessen's Rule",
          "simulation": "ssp-hall-effect-sim",
          "content": "<h4>1. The Hall Effect & Hall Coefficient $R_H$</h4>\n<p>When an electric current density $J_x$ flows along the $x$-direction of a conductor immersed in a transverse magnetic field $B_z$ in the $z$-direction, the magnetic Lorentz force $\\vec{F}_B = q (\\vec{v}_d \\times \\vec{B})$ deflects charge carriers along the $y$-direction:</p>\n<div class=\"math-display\">\n$$F_{B,y} = q (v_{d,x} B_z) = - e v_{d,x} B_z$$\n</div>\n<p>Charge accumulates on the lateral boundaries, generating a transverse electrostatic <strong>Hall electric field</strong> $E_y$. In steady state, the transverse electrostatic force exactly balances the magnetic Lorentz force ($F_y = 0$):</p>\n<div class=\"math-display\">\n$$q E_y + q v_{d,x} B_z = 0 \\implies E_y = - v_{d,x} B_z$$\n</div>\n<p>Since $J_x = n q v_{d,x} \\implies v_{d,x} = \\frac{J_x}{n q}$:</p>\n<div class=\"math-display\">\n$$E_y = - \\frac{J_x B_z}{n q} = R_H J_x B_z$$\n</div>\n<p>where $R_H$ is the <strong>Hall Coefficient</strong>:</p>\n<div class=\"math-display\">\n$$R_H = \\frac{E_y}{J_x B_z} = \\frac{1}{n q} = - \\frac{1}{n e} \\quad (\\text{for electrons})$$\n</div>\n<p>The Hall effect provides an unambiguous experimental measurement of both the <strong>sign of the charge carriers</strong> (negative for electrons, positive for holes) and the <strong>carrier concentration</strong> $n$.</p>\n\n<h4>2. Quantum Wiedemann-Franz Law & The Lorenz Number</h4>\n<p>Applying Sommerfeld's degenerate Fermi gas theory to electronic thermal conduction ($\\kappa = \\frac{1}{3} C_{el} v_F^2 \\tau$ with $C_{el} = \\frac{\\pi^2}{3} g(E_F) k_B^2 T$) and electrical conductivity ($\\sigma = \\frac{n e^2 \\tau}{m}$) yields the <strong>quantum Wiedemann-Franz law</strong>:</p>\n<div class=\"math-display\">\n$$\\frac{\\kappa}{\\sigma T} = \\frac{\\pi^2}{3} \\left(\\frac{k_B}{e}\\right)^2 = L \\approx 2.443 \\times 10^{-8}\\text{ W}\\cdot\\Omega\\cdot\\text{K}^{-2}$$\n</div>\n<p>where $L = \\frac{\\pi^2}{3}(k_B/e)^2$ is the universal <strong>Lorenz number</strong>, completely independent of carrier density, mass, and material parameters.</p>\n\n<h4>3. Matthiessen's Rule for Electrical Resistivity</h4>\n<p>Electrons in a real metal are scattered by both static structural crystal defects/impurities and dynamic thermal lattice vibrations (phonons). By <strong>Matthiessen's Rule</strong>, independent scattering rates add linearly:</p>\n<div class=\"math-display\">\n$$\\frac{1}{\\tau_{\\text{tot}}} = \\frac{1}{\\tau_{\\text{impurity}}} + \\frac{1}{\\tau_{\\text{phonon}}(T)}$$\n</div>\n<p>Consequently, the total electrical resistivity $\\rho = m / (ne^2\\tau)$ separates into temperature-independent and temperature-dependent terms:</p>\n<div class=\"math-display\">\n$$\\rho(T) = \\rho_{\\text{residual}} + \\rho_{\\text{ideal}}(T)$$\n</div>\n<p>where $\\rho_{\\text{residual}}$ is determined by impurity concentration, and $\\rho_{\\text{ideal}}(T) \\propto T^5$ at low temperatures (Bloch-Gr\u00fcneisen law) and $\\rho_{\\text{ideal}}(T) \\propto T$ at high temperatures ($T > \\Theta_D$).</p>"
        }
      ],
      "problems": [
        {
          "id": "ssp-p-5-1",
          "title": "Fermi Energy, Fermi Velocity and Fermi Temperature of Copper",
          "statement": "Copper is a monovalent metal (one conduction electron per atom) with atomic mass $M = 63.546 \\text{ g/mol}$, density $\\rho = 8.96 \\text{ g/cm}^3$, and electron mass $m = 9.109 \\times 10^{-31} \\text{ kg}$. (a) Calculate the conduction electron number density $n$. (b) Determine the Fermi wavevector $k_F$, the Fermi energy $E_F$ in $\\text{eV}$, the Fermi velocity $v_F$, and the Fermi temperature $T_F$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Electron Density n",
              "math": "n = \\frac{\\rho N_A}{M} = \\frac{(8.96 \\times 10^6\\text{ g/m}^3)(6.022 \\times 10^{23}\\text{ mol}^{-1})}{63.546\\text{ g/mol}} \\approx 8.492 \\times 10^{28}\\text{ electrons/m}^3",
              "explanation": "Compute conduction electron density from mass density and molar mass."
            },
            {
              "stepName": "Step 2: Calculate the Fermi Wavevector k_F",
              "math": "k_F = (3\\pi^2 n)^{1/3} = [3\\pi^2 (8.492 \\times 10^{28})]^{1/3} = (2.5144 \\times 10^{30})^{1/3} \\approx 1.360 \\times 10^{10}\\text{ m}^{-1} = 1.360\\text{ \\AA}^{-1}",
              "explanation": "Evaluate the radius of the spherical Fermi surface in reciprocal space."
            },
            {
              "stepName": "Step 3: Calculate the Fermi Energy E_F in eV",
              "math": "E_F = \\frac{\\hbar^2 k_F^2}{2m} = \\frac{(1.0546 \\times 10^{-34}\\text{ J}\\cdot\\text{s})^2 (1.360 \\times 10^{10}\\text{ m}^{-1})^2}{2(9.109 \\times 10^{-31}\\text{ kg})} = \\frac{2.056 \\times 10^{-47}}{1.8218 \\times 10^{-30}}\\text{ J} \\approx 1.1286 \\times 10^{-18}\\text{ J} \\approx 7.04\\text{ eV}",
              "explanation": "Convert Joules to electron-volts by dividing by 1.6022 x 10^-19 J/eV."
            },
            {
              "stepName": "Step 4: Calculate the Fermi Velocity v_F",
              "math": "v_F = \\frac{\\hbar k_F}{m} = \\frac{(1.0546 \\times 10^{-34}\\text{ J}\\cdot\\text{s})(1.360 \\times 10^{10}\\text{ m}^{-1})}{9.109 \\times 10^{-31}\\text{ kg}} \\approx 1.574 \\times 10^6\\text{ m/s}",
              "explanation": "Compute the velocity of electrons at the Fermi surface."
            },
            {
              "stepName": "Step 5: Calculate the Fermi Temperature T_F",
              "math": "T_F = \\frac{E_F}{k_B} = \\frac{1.1286 \\times 10^{-18}\\text{ J}}{1.3806 \\times 10^{-23}\\text{ J/K}} \\approx 81750\\text{ K} \\approx 8.18 \\times 10^4\\text{ K}",
              "explanation": "Compute the degeneracy temperature."
            }
          ],
          "answer": "n = 8.49 \\times 10^{28} \\text{ m}^{-3}, \\quad E_F = 7.04 \\text{ eV}, \\quad v_F = 1.57 \\times 10^6 \\text{ m/s}, \\quad T_F = 8.18 \\times 10^4 \\text{ K}"
        },
        {
          "id": "ssp-p-5-2",
          "title": "Sommerfeld Electronic Heat Capacity Coefficient for Silver",
          "statement": "Silver has a Fermi energy of $E_F = 5.49 \\text{ eV}$ and atomic molar mass $M = 107.87 \\text{ g/mol}$. (a) Calculate the theoretical Sommerfeld coefficient $\\gamma$ per mole of conduction electrons. (b) Calculate the molar electronic heat capacity $C_{el}$ at liquid helium temperature $T = 4.2 \\text{ K}$, and compare it with the classical value $3R/2$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Fermi Temperature of Silver",
              "math": "T_F = \\frac{E_F}{k_B} = \\frac{5.49\\text{ eV} \\times 1.6022 \\times 10^{-19}\\text{ J/eV}}{1.3806 \\times 10^{-23}\\text{ J/K}} = \\frac{8.796 \\times 10^{-19}\\text{ J}}{1.3806 \\times 10^{-23}\\text{ J/K}} \\approx 63710\\text{ K}",
              "explanation": "Convert Fermi energy to Fermi temperature."
            },
            {
              "stepName": "Step 2: Calculate the Sommerfeld Coefficient gamma",
              "math": "\\gamma = \\frac{\\pi^2}{2} R \\frac{1}{T_F} = \\frac{\\pi^2}{2} \\times (8.314\\text{ J/mol}\\cdot\\text{K}) \\times \\frac{1}{63710\\text{ K}} \\approx \\frac{41.028}{63710}\\text{ J}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-2} \\approx 6.44 \\times 10^{-4}\\text{ J}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-2} = 0.644\\text{ mJ}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-2}",
              "explanation": "Evaluate the theoretical Sommerfeld constant per mole."
            },
            {
              "stepName": "Step 3: Evaluate Electronic Heat Capacity at T = 4.2 K",
              "math": "C_{el}(4.2\\text{ K}) = \\gamma T = (6.44 \\times 10^{-4}\\text{ J}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-2}) \\times (4.2\\text{ K}) \\approx 2.705 \\times 10^{-3}\\text{ J}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1} = 2.71\\text{ mJ}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1}",
              "explanation": "Multiply gamma by T = 4.2 K."
            },
            {
              "stepName": "Step 4: Compare with Classical Prediction",
              "math": "\\frac{C_{el}(4.2\\text{ K})}{C_{\\text{classical}}} = \\frac{2.705 \\times 10^{-3}\\text{ J/mol}\\cdot\\text{K}}{\\frac{3}{2}(8.314\\text{ J/mol}\\cdot\\text{K})} = \\frac{2.705 \\times 10^{-3}}{12.471} \\approx 2.17 \\times 10^{-4}",
              "explanation": "The quantum electronic heat capacity is suppressed by nearly four orders of magnitude compared to the classical prediction."
            }
          ],
          "answer": "\\gamma = 0.644 \\text{ mJ}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-2}, \\quad C_{el}(4.2\\text{ K}) = 2.71 \\text{ mJ}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1} \\quad (0.0217\\% \\text{ of classical } 3R/2)"
        },
        {
          "id": "ssp-p-5-3",
          "title": "Hall Coefficient, Carrier Density and Mobility in Sodium Metal",
          "statement": "A rectangular ribbon of sodium metal of thickness $t = 0.10 \\text{ mm}$ and width $w = 5.0 \\text{ mm}$ carries a longitudinal current $I_x = 10.0 \\text{ A}$ in a transverse magnetic field $B_z = 1.20 \\text{ T}$. A transverse Hall voltage of $V_H = -2.94 \\text{ }\u03bc\\text{V}$ is measured across its width. The electrical resistivity of sodium is $\\rho = 4.75 \\times 10^{-8} \\text{ }\u03a9\\cdot\\text{m}$. (a) Calculate the Hall coefficient $R_H$. (b) Determine the conduction electron density $n$. (c) Calculate the electron drift mobility $\\mu$ and relaxation time $\\tau$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Hall Coefficient R_H",
              "math": "V_H = \\frac{R_H I_x B_z}{t} \\implies R_H = \\frac{V_H t}{I_x B_z} = \\frac{(-2.94 \\times 10^{-6}\\text{ V})(1.0 \\times 10^{-4}\\text{ m})}{(10.0\\text{ A})(1.20\\text{ T})} = \\frac{-2.94 \\times 10^{-10}}{12.0} = - 2.45 \\times 10^{-11}\\text{ m}^3/\\text{C}",
              "explanation": "Solve for the Hall coefficient using the measured Hall voltage, sample thickness, current, and magnetic field."
            },
            {
              "stepName": "Step 2: Determine the Conduction Electron Density n",
              "math": "n = - \\frac{1}{e R_H} = \\frac{1}{(1.6022 \\times 10^{-19}\\text{ C})(2.45 \\times 10^{-11}\\text{ m}^3/\\text{C})} = \\frac{1}{3.9254 \\times 10^{-30}} \\approx 2.548 \\times 10^{28}\\text{ electrons/m}^3",
              "explanation": "Extract the carrier density from R_H = -1 / (n e)."
            },
            {
              "stepName": "Step 3: Calculate the Electron Drift Mobility mu",
              "math": "\\sigma = \\frac{1}{\\rho} = \\frac{1}{4.75 \\times 10^{-8}\\text{ }\\Omega\\cdot\\text{m}} \\approx 2.105 \\times 10^7\\text{ }\\Omega^{-1}\\cdot\\text{m}^{-1} \\implies \\mu = \\sigma |R_H| = (2.105 \\times 10^7)(2.45 \\times 10^{-11})\\text{ m}^2/\\text{V}\\cdot\\text{s} \\approx 5.158 \\times 10^{-4}\\text{ m}^2/\\text{V}\\cdot\\text{s}",
              "explanation": "Compute mobility using mu = sigma * |R_H|."
            },
            {
              "stepName": "Step 4: Calculate the Relaxation Time tau",
              "math": "\\tau = \\frac{m \\mu}{e} = \\frac{(9.109 \\times 10^{-31}\\text{ kg})(5.158 \\times 10^{-4}\\text{ m}^2/\\text{V}\\cdot\\text{s})}{1.6022 \\times 10^{-19}\\text{ C}} \\approx 2.93 \\times 10^{-14}\\text{ s}",
              "explanation": "Evaluate the electron collision relaxation time."
            }
          ],
          "answer": "R_H = -2.45 \\times 10^{-11} \\text{ m}^3/\\text{C}, \\quad n = 2.55 \\times 10^{28} \\text{ m}^{-3}, \\quad \\mu = 5.16 \\times 10^{-4} \\text{ m}^2/\\text{V}\\cdot\\text{s}, \\quad \\tau = 2.93 \\times 10^{-14} \\text{ s}"
        }
      ]
    },
    {
      "unitNumber": 6,
      "unitId": "unit6-band-structure",
      "title": "Electronic Band Structure & Bloch Electron Dynamics",
      "description": "Comprehensive energy band theory in crystals: periodic potential, Bloch theorem, Kronig-Penney solvable model, origin of energy band gaps, reduced and extended zone schemes, nearly free electron approximation, tight-binding LCAO method, semiclassical electron dynamics, group velocity, effective mass tensor, concept of positive holes, and Fermi surfaces.",
      "sections": [
        {
          "id": "ssp-6-1",
          "title": "Periodic Crystal Potential & Bloch's Theorem",
          "content": "<h4>1. Electrons in a Periodic Crystal Potential</h4>\n<p>An electron in a perfect crystalline solid experiences a potential energy $V(\\vec{r})$ that possesses the full discrete translational periodicity of the Bravais lattice:</p>\n<div class=\"math-display\">\n$$V(\\vec{r} + \\vec{R}) = V(\\vec{r}) \\quad \\forall \\vec{R} = n_1 \\vec{a}_1 + n_2 \\vec{a}_2 + n_3 \\vec{a}_3$$\n</div>\n<p>The single-electron Schr\u00f6dinger equation is:</p>\n<div class=\"math-display\">\n$$\\hat{H} \\psi(\\vec{r}) = \\left[ - \\frac{\\hbar^2}{2m} \\nabla^2 + V(\\vec{r}) \\right] \\psi(\\vec{r}) = E \\psi(\\vec{r})$$\n</div>\n\n<h4>2. Formal Statement & Proof of Bloch's Theorem</h4>\n<p>Because the Hamiltonian commutes with all lattice translation operators $\\hat{T}_{\\vec{R}}$ ($[\\hat{H}, \\hat{T}_{\\vec{R}}] = 0$), simultaneous eigenstates of $\\hat{H}$ and $\\hat{T}_{\\vec{R}}$ can be constructed. <strong>Bloch's Theorem</strong> states that the eigenstates of an electron in a periodic potential can be chosen in the form of a plane wave modulated by a periodic function $u_{n,\\vec{k}}(\\vec{r})$ having the periodicity of the lattice:</p>\n<div class=\"math-display\">\n$$\\psi_{n,\\vec{k}}(\\vec{r}) = e^{i \\vec{k} \\cdot \\vec{r}} u_{n,\\vec{k}}(\\vec{r})$$\n</div>\n<p>where $u_{n,\\vec{k}}(\\vec{r} + \\vec{R}) = u_{n,\\vec{k}}(\\vec{r})$ for all lattice vectors $\\vec{R}$. Equivalently, translating by any lattice vector $\\vec{R}$ merely shifts the phase of the wavefunction:</p>\n<div class=\"math-display\">\n$$\\psi_{n,\\vec{k}}(\\vec{r} + \\vec{R}) = e^{i \\vec{k} \\cdot \\vec{R}} \\psi_{n,\\vec{k}}(\\vec{r})$$\n</div>\n<p>The vector $\\vec{k}$ is the <strong>crystal wavevector</strong>, and the integer $n = 1, 2, 3, \\dots$ is the <strong>band index</strong>.</p>\n\n<h4>3. Crystal Momentum vs. Physical Momentum</h4>\n<p>The quantity $\\hbar \\vec{k}$ is known as <strong>crystal momentum</strong>. It is not the eigenvalue of the physical momentum operator $-i\\hbar\\nabla$ (since momentum is not conserved in the presence of the lattice potential). Instead, crystal momentum is conserved in electron-photon, electron-phonon, and electron-electron scattering events modulo an arbitrary reciprocal lattice vector $\\vec{G}$:</p>\n<div class=\"math-display\">\n$$\\vec{k}' = \\vec{k} + \\vec{q} + \\vec{G}$$\n</div>"
        },
        {
          "id": "ssp-6-2",
          "title": "The Kronig-Penney Model & Origin of Energy Band Gaps",
          "simulation": "ssp-kronig-penney-sim",
          "content": "<h4>1. The Kronig-Penney 1D Solvable Model</h4>\n<p>R. de L. Kronig and W. G. Penney (1931) introduced an idealized one-dimensional periodic array of rectangular potential barriers of height $V_0$, barrier width $b$, and well width $a$ (lattice constant $d = a + b$):</p>\n<div class=\"math-display\">\n$$V(x) = \\begin{cases} 0, & 0 < x < a \\\\ V_0, & -b < x < 0 \\end{cases}$$\n</div>\n<p>In Region I ($0 < x < a$), $\\psi_1(x) = A e^{i K x} + B e^{-i K x}$, where $K = \\sqrt{2mE/\\hbar^2}$.</p>\n<p>In Region II ($-b < x < 0$), for $E < V_0$, $\\psi_2(x) = C e^{Q x} + D e^{-Q x}$, where $Q = \\sqrt{2m(V_0 - E)/\\hbar^2}$.</p>\n\n<h4>2. The Dirac Delta-Function Barrier Limit</h4>\n<p>Taking the limit where the barriers become infinitely thin and tall ($b \\to 0, V_0 \\to \\infty$) while their barrier area $P = \\lim \\frac{m V_0 b a}{\\hbar^2}$ remains constant, matching wavefunctions and their derivatives across the boundary using Bloch's theorem yields the famous <strong>Kronig-Penney dispersion relation</strong>:</p>\n<div class=\"math-display\">\n$$P \\frac{\\sin(K a)}{K a} + \\cos(K a) = \\cos(k a)$$\n</div>\n<p>where $P$ is the dimensionless <strong>barrier strength</strong> (representing the strength of the periodic crystal potential).</p>\n\n<h4>3. Origin of Energy Bands and Band Gaps</h4>\n<p>Because the right-hand side is $\\cos(k a)$, real solutions for crystal wavevector $k$ exist <em>if and only if</em> the left-hand side satisfies:</p>\n<div class=\"math-display\">\n$$-1 \\le P \\frac{\\sin(K a)}{K a} + \\cos(K a) \\le +1$$\n</div>\n<ul>\n<li><strong>Allowed Energy Bands:</strong> Values of $E = \\frac{\\hbar^2 K^2}{2m}$ where the condition is satisfied represent allowed energy bands.</li>\n<li><strong>Forbidden Band Gaps ($E_g$):</strong> Energy ranges where the magnitude of the left-hand side exceeds unity ($> +1$ or $< -1$). No traveling Bloch waves can propagate through the crystal at these energies; electron waves undergo destructive interference and total Bragg reflection.</li>\n<li><strong>Limits:</strong>\n<ul>\n<li>$P \\to 0$ (Free Electrons): $\\cos(Ka) = \\cos(ka) \\implies K = k \\implies E = \\frac{\\hbar^2 k^2}{2m}$ (continuous parabolic spectrum).</li>\n<li>$P \\to \\infty$ (Isolated Atoms): $\\sin(Ka) = 0 \\implies Ka = n\\pi \\implies E_n = \\frac{n^2 \\pi^2 \\hbar^2}{2m a^2}$ (discrete bound atomic levels).</li>\n</ul></li>\n</ul>"
        },
        {
          "id": "ssp-6-3",
          "title": "Zone Schemes & Nearly Free Electron (NFE) Approximation",
          "content": "<h4>1. Representation of Energy Bands: Zone Schemes</h4>\n<p>Because energy eigenvalues satisfy $E_n(k + G) = E_n(k)$, the band structure can be represented in three equivalent representations:</p>\n<ol>\n<li><strong>Extended Zone Scheme:</strong> Band $n$ is plotted in the $n$-th Brillouin zone: band 1 in $[-\\pi/a, +\\pi/a]$, band 2 in $[-2\\pi/a, -\\pi/a] \\cup [+\\pi/a, +2\\pi/a]$, etc. Most closely resembles the free-electron parabola $E = \\hbar^2 k^2/2m$.</li>\n<li><strong>Reduced Zone Scheme:</strong> All energy bands are mapped back into the First Brillouin Zone ($-\\pi/a \\le k \\le +\\pi/a$) by translating by appropriate reciprocal lattice vectors $G = 2\\pi n / a$. Standard representation used in modern solid-state physics.</li>\n<li><strong>Periodic (Repeated) Zone Scheme:</strong> The First Brillouin Zone dispersion is repeated periodically across all $k$-space with period $2\\pi/a$. Convenient for visualizing semiclassical electron trajectories.</li>\n</ol>\n\n<h4>2. The Nearly Free Electron (NFE) Approximation</h4>\n<p>When the periodic crystal potential $V(x)$ is weak compared to electron kinetic energies, it can be treated as a perturbation. Expanding the potential in a Fourier series over reciprocal lattice vectors $G$:</p>\n<div class=\"math-display\">\n$$V(x) = \\sum_{G} V_G e^{i G x} \\quad (V_0 = 0)$$\n</div>\n<p>Away from the Brillouin zone boundaries, standard non-degenerate perturbation theory shifts energies insignificantly. However, near the zone boundary $k = \\pm G/2$, the two unperturbed plane-wave states $|k\\rangle$ and $|k - G\\rangle$ are degenerate ($E_0(k) \\approx E_0(k - G)$).</p>\n<p>Applying degenerate perturbation theory with trial state $\\psi = c_1 |k\\rangle + c_2 |k - G\\rangle$ yields the $2 \\times 2$ secular equation:</p>\n<div class=\"math-display\">\n$$\\begin{pmatrix} E_0(k) - E & V_G \\\\ V_G^* & E_0(k - G) - E \\end{pmatrix} \\begin{pmatrix} c_1 \\\\ c_2 \\end{pmatrix} = 0$$\n</div>\n<p>At the exact zone boundary $k = G/2$, $E_0(k) = E_0(k - G) = \\frac{\\hbar^2 (G/2)^2}{2m} = E_0$:</p>\n<div class=\"math-display\">\n$$(E_0 - E)^2 - |V_G|^2 = 0 \\implies E_{\\pm} = E_0 \\pm |V_G|$$\n</div>\n<p>A band gap of magnitude $\\Delta E_g = 2 |V_G|$ opens up at every Brillouin zone boundary. The standing wave solutions $\\psi_+ \\sim \\cos(Gx/2)$ and $\\psi_- \\sim \\sin(Gx/2)$ pile up electronic charge density either at the ion cores (lowering energy by $-|V_G|$) or midway between the ion cores (raising energy by $+|V_G|$).</p>"
        },
        {
          "id": "ssp-6-4",
          "title": "The Tight-Binding Approximation (LCAO for Crystals)",
          "content": "<h4>1. Physical Foundation of Tight-Binding</h4>\n<p>In contrast to the nearly free electron model, the <strong>Tight-Binding Approximation</strong> assumes that electrons are tightly bound to individual atomic cores, spending most of their time in localized atomic orbitals $\\phi(\\vec{r} - \\vec{R}_n)$. When atoms are brought together into a crystal lattice, the overlap between adjacent atomic wavefunctions broadens discrete atomic energy levels into continuous energy bands.</p>\n\n<h4>2. Formulation of the Bloch Sum</h4>\n<p>To satisfy Bloch's theorem, the trial crystal wavefunction is formed as a coherent linear combination of atomic orbitals (LCAO) summed over all $N$ lattice sites $\\vec{R}_n$:</p>\n<div class=\"math-display\">\n$$\\psi_k(\\vec{r}) = \\frac{1}{\\sqrt{N}} \\sum_{n} e^{i \\vec{k}\\cdot\\vec{R}_n} \\phi(\\vec{r} - \\vec{R}_n)$$\n</div>\n\n<h4>3. Derivation of 1D and 3D Tight-Binding Dispersion</h4>\n<p>Evaluating the expectation value of the crystal Hamiltonian $\\hat{H} = \\hat{H}_{\\text{atom}} + \\Delta U(\\vec{r})$:</p>\n<div class=\"math-display\">\n$$E(k) = \\frac{\\langle \\psi_k | \\hat{H} | \\psi_k \\rangle}{\\langle \\psi_k | \\psi_k \\rangle} \\approx \\frac{\\sum_{n, m} e^{i \\vec{k}\\cdot(\\vec{R}_m - \\vec{R}_n)} \\int \\phi^*(\\vec{r} - \\vec{R}_n) \\hat{H} \\phi(\\vec{r} - \\vec{R}_m) d^3r}{N}$$\n</div>\n<p>Retaining only on-site and nearest-neighbor matrix elements:</p>\n<ul>\n<li><strong>On-site atomic energy:</strong> $\\varepsilon_0 = \\int \\phi^*(\\vec{r}) \\hat{H} \\phi(\\vec{r}) d^3r \\approx - E_0 - \\alpha$.</li>\n<li><strong>Nearest-neighbor transfer (hopping) integral:</strong> $t = - \\int \\phi^*(\\vec{r}) \\hat{H} \\phi(\\vec{r} - \\vec{a}) d^3r > 0$.</li>\n</ul>\n<p>For a <strong>one-dimensional chain</strong> with nearest-neighbor distance $a$:</p>\n<div class=\"math-display\">\n$$E(k) = \\varepsilon_0 - 2 t \\cos(k a)$$\n</div>\n<p>The total bandwidth of the tight-binding band is $W = E_{\\text{max}} - E_{\\text{min}} = (\\varepsilon_0 + 2t) - (\\varepsilon_0 - 2t) = 4t$.</p>\n<p>For a <strong>3D Simple Cubic lattice</strong> with nearest-neighbor spacing $a$:</p>\n<div class=\"math-display\">\n$$E(\\vec{k}) = \\varepsilon_0 - 2 t [\\cos(k_x a) + \\cos(k_y a) + \\cos(k_z a)] \\quad (\\text{Bandwidth } W = 12 t)$$\n</div>"
        },
        {
          "id": "ssp-6-5",
          "title": "Semiclassical Electron Dynamics, Effective Mass & Positive Holes",
          "simulation": "ssp-effective-mass-sim",
          "content": "<h4>1. Semiclassical Equations of Motion for Bloch Electrons</h4>\n<p>An electron in an energy band $E_n(\\vec{k})$ is described by a localized wave packet centered at position $\\vec{r}$ and mean wavevector $\\vec{k}$. Its dynamical evolution under external electromagnetic fields $\\vec{E}$ and $\\vec{B}$ is governed by the <strong>semiclassical equations of motion</strong>:</p>\n<ol>\n<li><strong>Group Velocity:</strong>\n<div class=\"math-display\">\n$$\\vec{v}(\\vec{k}) = \\frac{1}{\\hbar} \\nabla_{\\vec{k}} E(\\vec{k})$$\n</div></li>\n<li><strong>Rate of Change of Crystal Momentum:</strong>\n<div class=\"math-display\">\n$$\\hbar \\frac{d\\vec{k}}{dt} = \\vec{F}_{\\text{ext}} = - e [\\vec{E} + \\vec{v}(\\vec{k}) \\times \\vec{B}]$$\n</div></li>\n</ol>\n\n<h4>2. Derivation of the Effective Mass Tensor $m^*$</h4>\n<p>Differentiating the group velocity with respect to time:</p>\n<div class=\"math-display\">\n$$\\frac{d\\vec{v}}{dt} = \\frac{1}{\\hbar} \\frac{d}{dt} \\nabla_{\\vec{k}} E(\\vec{k}) = \\frac{1}{\\hbar} \\sum_{j} \\left( \\frac{\\partial^2 E}{\\partial k_i \\partial k_j} \\right) \\frac{dk_j}{dt}$$\n</div>\n<p>Substituting $\\hbar \\frac{dk_j}{dt} = F_j$:</p>\n<div class=\"math-display\">\n$$\\frac{dv_i}{dt} = \\sum_{j} \\left( \\frac{1}{\\hbar^2} \\frac{\\partial^2 E}{\\partial k_i \\partial k_j} \\right) F_j = \\sum_{j} \\left(\\frac{1}{m^*}\\right)_{ij} F_j$$\n</div>\n<p>Comparing with Newton's second law $\\vec{a} = (m^*)^{-1} \\vec{F}$ defines the <strong>Effective Mass Tensor</strong> $(m^*)_{ij}$:</p>\n<div class=\"math-display\">\n$$\\left(\\frac{1}{m^*}\\right)_{ij} = \\frac{1}{\\hbar^2} \\frac{\\partial^2 E(\\vec{k})}{\\partial k_i \\partial k_j}$$\n</div>\n<p>In an isotropic 1D band: $m^* = \\hbar^2 / \\left(\\frac{d^2E}{dk^2}\\right)$.</p>\n<ul>\n<li>Near the <strong>bottom of a band</strong> ($\\frac{d^2E}{dk^2} > 0$): $m^* > 0$. The electron accelerates in the direction of the applied electric force like a free electron.</li>\n<li>Near the <strong>top of a band</strong> ($\\frac{d^2E}{dk^2} < 0$): $m^* < 0$. The electron accelerates in the direction <em>opposite</em> to the external force because of Bragg reflections from the lattice potential.</li>\n</ul>\n\n<h4>3. The Concept of Positive Holes</h4>\n<p>In a nearly filled band, the absence of an electron from a state with wavevector $\\vec{k}_e$, energy $E_e$, and charge $-e$ is described as a quasiparticle called a <strong>hole</strong>:</p>\n<ul>\n<li><strong>Wavevector:</strong> $\\vec{k}_h = - \\vec{k}_e$</li>\n<li><strong>Energy:</strong> $E_h(\\vec{k}_h) = - E_e(\\vec{k}_e)$</li>\n<li><strong>Velocity:</strong> $\\vec{v}_h = \\vec{v}_e$</li>\n<li><strong>Charge:</strong> $q_h = + e$ (positive charge)</li>\n<li><strong>Effective Mass:</strong> $m_h^* = - m_e^* > 0$ (positive effective mass at the band top)</li>\n</ul>\n<p>Treating valence band transport in terms of positive holes simplifies the quantum statistical mechanics of semiconductors and metals.</p>"
        }
      ],
      "problems": [
        {
          "id": "ssp-p-6-1",
          "title": "Energy Band Gap Opening in the Nearly Free Electron Model",
          "statement": "An electron moves in a 1D crystal with lattice spacing $a = 3.0 \\text{ \u00c5}$ under a weak periodic potential $V(x) = 2 V_1 \\cos(2\\pi x / a)$ with Fourier amplitude $V_1 = 0.75 \\text{ eV}$. (a) Calculate the unperturbed free-electron kinetic energy $E_0$ at the First Brillouin Zone boundary $k = \\pi / a$. (b) Determine the energy values $E_+$ and $E_-$ at the zone boundary and the magnitude of the band gap $\\Delta E_g$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Reciprocal Lattice Vector G",
              "math": "G = \\frac{2\\pi}{a} = \\frac{2\\pi}{3.0 \\times 10^{-10}\\text{ m}} \\approx 2.094 \\times 10^{10}\\text{ m}^{-1} \\implies k_{\\text{edge}} = \\frac{G}{2} = \\frac{\\pi}{a} \\approx 1.047 \\times 10^{10}\\text{ m}^{-1}",
              "explanation": "Compute the First Brillouin Zone boundary wavevector."
            },
            {
              "stepName": "Step 2: Calculate the Unperturbed Free-Electron Energy E_0",
              "math": "E_0 = \\frac{\\hbar^2 k_{\\text{edge}}^2}{2m} = \\frac{(1.0546 \\times 10^{-34}\\text{ J}\\cdot\\text{s})^2 (1.047 \\times 10^{10}\\text{ m}^{-1})^2}{2(9.109 \\times 10^{-31}\\text{ kg})} = \\frac{1.2185 \\times 10^{-47}}{1.8218 \\times 10^{-30}}\\text{ J} \\approx 6.688 \\times 10^{-19}\\text{ J} \\approx 4.174\\text{ eV}",
              "explanation": "Compute unperturbed kinetic energy in electron-volts."
            },
            {
              "stepName": "Step 3: Calculate the Band Gap Delta E_g",
              "math": "\\Delta E_g = 2 |V_G| = 2 V_1 = 2 \\times 0.75\\text{ eV} = 1.50\\text{ eV}",
              "explanation": "In degenerate perturbation theory, the band gap equals twice the Fourier component of the potential."
            },
            {
              "stepName": "Step 4: Determine the Band Edge Energies E_+ and E_-",
              "math": "E_- = E_0 - V_1 = 4.174\\text{ eV} - 0.75\\text{ eV} = 3.424\\text{ eV}, \\quad E_+ = E_0 + V_1 = 4.174\\text{ eV} + 0.75\\text{ eV} = 4.924\\text{ eV}",
              "explanation": "The lower band terminates at E_- and the upper band begins at E_+."
            }
          ],
          "answer": "E_0 = 4.17 \\text{ eV}, \\quad \\Delta E_g = 1.50 \\text{ eV}, \\quad E_- = 3.42 \\text{ eV}, \\quad E_+ = 4.92 \\text{ eV}"
        },
        {
          "id": "ssp-p-6-2",
          "title": "Effective Mass and Group Velocity in a 1D Tight-Binding Band",
          "statement": "The energy dispersion of a 1D tight-binding conduction band is given by $E(k) = - E_0 - 2t \\cos(ka)$, where $E_0 = 1.20 \\text{ eV}$, hopping integral $t = 0.85 \\text{ eV}$, and lattice spacing $a = 2.50 \\text{ \u00c5}$. (a) Calculate the total bandwidth $W$. (b) Derive the expression for effective mass $m^*(k)$ and evaluate its numerical value in units of free electron mass $m_0$ at the band bottom ($k = 0$) and band top ($k = \\pi/a$). (c) Find the wavevector $k$ at which the electron group velocity $v_g$ reaches its maximum value.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Total Bandwidth W",
              "math": "W = E_{\\text{max}} - E_{\\text{min}} = 4t = 4 \\times 0.85\\text{ eV} = 3.40\\text{ eV}",
              "explanation": "In a 1D tight-binding cosine band, the bandwidth equals 4 times the transfer integral t."
            },
            {
              "stepName": "Step 2: Derive the Effective Mass Formula",
              "math": "\\frac{dE}{dk} = 2 t a \\sin(k a) \\implies \\frac{d^2E}{dk^2} = 2 t a^2 \\cos(k a) \\implies m^*(k) = \\frac{\\hbar^2}{2 t a^2 \\cos(k a)}",
              "explanation": "Differentiate E(k) twice with respect to wavevector k."
            },
            {
              "stepName": "Step 3: Evaluate m* at k = 0 (Band Bottom)",
              "math": "m^*(0) = \\frac{\\hbar^2}{2 t a^2} = \\frac{(1.0546 \\times 10^{-34}\\text{ J}\\cdot\\text{s})^2}{2 \\times (0.85 \\times 1.6022 \\times 10^{-19}\\text{ J}) \\times (2.50 \\times 10^{-10}\\text{ m})^2} = \\frac{1.1122 \\times 10^{-68}}{2.7237 \\times 10^{-19} \\times 6.25 \\times 10^{-20}} = \\frac{1.1122 \\times 10^{-68}}{1.7023 \\times 10^{-38}}\\text{ kg} \\approx 6.533 \\times 10^{-31}\\text{ kg} \\implies \\frac{m^*(0)}{m_0} = \\frac{6.533 \\times 10^{-31}}{9.109 \\times 10^{-31}} \\approx 0.717",
              "explanation": "Substitute numerical values to find the effective mass at k = 0."
            },
            {
              "stepName": "Step 4: Evaluate m* at k = pi / a (Band Top)",
              "math": "m^*(\\pi/a) = \\frac{\\hbar^2}{2 t a^2 \\cos(\\pi)} = - m^*(0) = - 0.717 m_0",
              "explanation": "At the zone boundary, cos(pi) = -1, yielding a negative effective mass corresponding to a positive hole mass m_h* = +0.717 m_0."
            },
            {
              "stepName": "Step 5: Determine Maximum Group Velocity",
              "math": "v_g(k) = \\frac{1}{\\hbar}\\frac{dE}{dk} = \\frac{2ta}{\\hbar}\\sin(ka) \\implies \\left. v_g \\right|_{\\text{max}} \\text{ occurs when } \\sin(ka) = 1 \\implies ka = \\frac{\\pi}{2} \\implies k = \\frac{\\pi}{2a}",
              "explanation": "The maximum group velocity occurs at the inflection point k = pi / (2a) where effective mass diverges to infinity."
            }
          ],
          "answer": "W = 3.40 \\text{ eV}, \\quad m^*(0) = +0.717 m_0, \\quad m^*(\\pi/a) = -0.717 m_0, \\quad k_{\\text{max}} = \\pi / (2a)"
        },
        {
          "id": "ssp-p-6-3",
          "title": "Period of Bloch Oscillations in an External Electric Field",
          "statement": "An electron in a crystal with lattice constant $a = 3.50 \\text{ \u00c5}$ is subjected to a uniform external electric field $E_x = 1.50 \\times 10^5 \\text{ V/m}$. Assuming negligible scattering (mean free path exceeds the oscillation length): (a) Calculate the rate of change of crystal wavevector $dk/dt$. (b) Determine the time period $T_B$ and cyclical frequency $\\nu_B$ of the resulting Bloch oscillations.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Rate of Change of Wavevector dk / dt",
              "math": "\\hbar \\frac{dk}{dt} = - e E_x \\implies \\left|\\frac{dk}{dt}\\right| = \\frac{e E_x}{\\hbar} = \\frac{(1.6022 \\times 10^{-19}\\text{ C})(1.50 \\times 10^5\\text{ V/m})}{1.0546 \\times 10^{-34}\\text{ J}\\cdot\\text{s}} \\approx 2.279 \\times 10^{20}\\text{ m}^{-1}\\cdot\\text{s}^{-1}",
              "explanation": "Apply the semiclassical equation of motion in an electric field."
            },
            {
              "stepName": "Step 2: Determine the Wavevector Traversed in One Full Oscillation",
              "math": "\\Delta k = \\frac{2\\pi}{a} = \\frac{2\\pi}{3.50 \\times 10^{-10}\\text{ m}} \\approx 1.795 \\times 10^{10}\\text{ m}^{-1}",
              "explanation": "One full cycle corresponds to traversing the entire First Brillouin Zone of width 2 pi / a."
            },
            {
              "stepName": "Step 3: Calculate the Bloch Oscillation Period T_B",
              "math": "T_B = \\frac{\\Delta k}{|dk/dt|} = \\frac{2\\pi \\hbar}{e E_x a} = \\frac{h}{e E_x a} = \\frac{6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s}}{(1.6022 \\times 10^{-19}\\text{ C})(1.50 \\times 10^5\\text{ V/m})(3.50 \\times 10^{-10}\\text{ m})} = \\frac{6.626 \\times 10^{-34}}{8.4116 \\times 10^{-24}}\\text{ s} \\approx 7.877 \\times 10^{-11}\\text{ s} = 78.8\\text{ ps}",
              "explanation": "Evaluate the Bloch period T_B = h / (e E a)."
            },
            {
              "stepName": "Step 4: Calculate the Bloch Oscillation Frequency nu_B",
              "math": "\\nu_B = \\frac{1}{T_B} = \\frac{1}{7.877 \\times 10^{-11}\\text{ s}} \\approx 1.269 \\times 10^{10}\\text{ Hz} = 12.7\\text{ GHz}",
              "explanation": "Inverted period gives the Bloch oscillation frequency in the microwave / terahertz regime."
            }
          ],
          "answer": "T_B = 78.8 \\text{ ps}, \\quad \\nu_B = 12.7 \\text{ GHz}"
        }
      ]
    },
    {
      "unitNumber": 7,
      "unitId": "unit7-dielectric-properties",
      "title": "Dielectric Properties, Plasmons & Optical Phenomena",
      "description": "Comprehensive macroscopic and microscopic electrodynamics of solids: macroscopic field vs local Lorentz field, polarizabilities, Clausius-Mossotti relation, AC complex permittivity, Debye dielectric relaxation, plasma oscillations, plasma frequency, Thomas-Fermi screening, ferroelectricity, piezoelectricity, and Kramers-Kronig optical relations.",
      "sections": [
        {
          "id": "ssp-7-1",
          "title": "Macroscopic Electric Field & The Microscopic Local Lorentz Field",
          "content": "<h4>1. Macroscopic Polarization $\\vec{P}$ and Electric Displacement $\\vec{D}$</h4>\n<p>In a dielectric solid subjected to an external electrostatic field, bound charges undergo micro-displacements, creating a volume dipole moment density known as the <strong>polarization vector</strong> $\\vec{P}$:</p>\n<div class=\"math-display\">\n$$\\vec{P} = \\lim_{\\Delta V \\to 0} \\frac{1}{\\Delta V} \\sum_{i \\in \\Delta V} \\vec{p}_i$$\n</div>\n<p>The macroscopic electric displacement $\\vec{D}$ and macroscopic electric field $\\vec{E}$ are related in linear, isotropic media by:</p>\n<div class=\"math-display\">\n$$\\vec{D} = \\varepsilon_0 \\vec{E} + \\vec{P} = \\varepsilon_0 (1 + \\chi_e) \\vec{E} = \\varepsilon_0 \\varepsilon_r \\vec{E}$$\n</div>\n<p>where $\\chi_e$ is the electric susceptibility and $\\varepsilon_r = 1 + \\chi_e$ is the relative dielectric permittivity.</p>\n\n<h4>2. Derivation of the Local Lorentz Field $\\vec{E}_{\\text{loc}}$</h4>\n<p>The actual electric field acting on an individual atom inside a condensed solid\u2014the <strong>local microscopic field</strong> $\\vec{E}_{\\text{loc}}$\u2014is not equal to the macroscopic Maxwell average field $\\vec{E}$, because the atom is surrounded by polarized atomic neighbors. Following H. A. Lorentz, we construct a spherical cavity of microscopic radius $R_{\\text{cav}}$ centered at the target atom:</p>\n<div class=\"math-display\">\n$$\\vec{E}_{\\text{loc}} = \\vec{E}_0 + \\vec{E}_1 + \\vec{E}_2 + \\vec{E}_3$$\n</div>\n<ol>\n<li>$\\vec{E}_0$: External field produced by fixed external charges.</li>\n<li>$\\vec{E}_1$: Depolarization field produced by the macroscopic polarization charges on the external outer boundaries of the dielectric specimen ($\\vec{E}_0 + \\vec{E}_1 = \\vec{E}$, the macroscopic field).</li>\n<li>$\\vec{E}_2$: Surface polarization charge field on the spherical cavity boundary. Integrating the bound surface charge density $\\sigma_b = - \\vec{P} \\cdot \\hat{n} = P \\cos\\theta$ over the spherical surface yields:\n<div class=\"math-display\">\n$$\\vec{E}_2 = \\frac{1}{4\\pi\\varepsilon_0} \\int_0^\\pi \\frac{(P \\cos\\theta)(\\cos\\theta)}{R_{\\text{cav}}^2} (2\\pi R_{\\text{cav}}^2 \\sin\\theta d\\theta) \\hat{z} = \\frac{\\vec{P}}{3\\varepsilon_0}$$\n</div></li>\n<li>$\\vec{E}_3$: Microscopic field produced by individual dipoles situated <em>inside</em> the cavity. For sites possessing cubic point-group symmetry (or random isotropic liquids), $\\vec{E}_3 \\equiv 0$.</li>\n</ol>\n<p>Summing these terms yields the celebrated <strong>Lorentz Local Field Relation</strong>:</p>\n<div class=\"math-display\">\n$$\\vec{E}_{\\text{loc}} = \\vec{E} + \\frac{\\vec{P}}{3\\varepsilon_0}$$\n</div>"
        },
        {
          "id": "ssp-7-2",
          "title": "Atomic Polarizabilities & The Clausius-Mossotti Relation",
          "simulation": "ssp-clausius-mossotti-sim",
          "content": "<h4>1. Mechanisms of Microscopic Dielectric Polarization</h4>\n<p>The total microscopic electric dipole moment $\\vec{p}$ induced in an individual atom or molecule is directly proportional to the local field: $\\vec{p} = \\alpha \\vec{E}_{\\text{loc}}$, where $\\alpha$ is the <strong>total polarizability</strong>, composed of three fundamental mechanisms:</p>\n<ol>\n<li><strong>Electronic Polarizability ($\\alpha_e$):</strong> Displacement of the negative valence electron cloud relative to the positive nucleus ($\\sim 10^{-40}\\text{ C}\\cdot\\text{m}^2/\\text{V}$). Resonant at optical frequencies ($\\sim 10^{15}\\text{ Hz}$).</li>\n<li><strong>Ionic (Atomic) Polarizability ($\\alpha_i$):</strong> Relative displacement of positive and negative ions in ionic crystals ($\\sim 10^{-39}\\text{ C}\\cdot\\text{m}^2/\\text{V}$). Resonant at infrared phonon frequencies ($\\sim 10^{13}\\text{ Hz}$).</li>\n<li><strong>Dipolar (Orientation) Polarizability ($\\alpha_d$):</strong> Thermal realignment of permanent molecular electric dipoles $\\vec{p}_0$ against thermal randomization. Described by the Langevin-Debye formula:\n<div class=\"math-display\">\n$$\\alpha_d = \\frac{p_0^2}{3 k_B T}$$\n</div>\n<p>Active at radio and microwave frequencies ($\\sim 10^9 - 10^{11}\\text{ Hz}$), vanishing at higher frequencies.</p></li>\n</ol>\n<p>The total polarizability is: $\\alpha = \\alpha_e + \\alpha_i + \\frac{p_0^2}{3 k_B T}$.</p>\n\n<h4>2. Derivation of the Clausius-Mossotti Relation</h4>\n<p>For a non-polar dielectric with number density $N$ atoms per unit volume, the macroscopic polarization is $\\vec{P} = N \\vec{p} = N \\alpha \\vec{E}_{\\text{loc}}$. Substituting the Lorentz local field $\\vec{E}_{\\text{loc}} = \\vec{E} + \\frac{\\vec{P}}{3\\varepsilon_0}$:</p>\n<div class=\"math-display\">\n$$\\vec{P} = N \\alpha \\left( \\vec{E} + \\frac{\\vec{P}}{3\\varepsilon_0} \\right) \\implies \\vec{P} \\left( 1 - \\frac{N\\alpha}{3\\varepsilon_0} \\right) = N \\alpha \\vec{E}$$\n</div>\n<p>Recalling the macroscopic definition $\\vec{P} = \\varepsilon_0 (\\varepsilon_r - 1) \\vec{E}$, we equate:</p>\n<div class=\"math-display\">\n$$\\varepsilon_0 (\\varepsilon_r - 1) = \\frac{N \\alpha}{1 - \\frac{N\\alpha}{3\\varepsilon_0}} \\implies \\frac{\\varepsilon_r - 1}{\\varepsilon_r + 2} = \\frac{N \\alpha}{3 \\varepsilon_0}$$\n</div>\n<p>This is the <strong>Clausius-Mossotti Relation</strong>. It links a purely macroscopic, experimentally measurable property\u2014the relative dielectric constant $\\varepsilon_r$\u2014directly to the microscopic atomic polarizability $\\alpha$ and atomic density $N$. At optical frequencies where $\\varepsilon_r = n^2$ ($n$ is the refractive index), it is called the <strong>Lorentz-Lorenz equation</strong>.</p>"
        },
        {
          "id": "ssp-7-3",
          "title": "AC Dielectric Response, Debye Relaxation & Dielectric Loss",
          "content": "<h4>1. Complex Dielectric Function $\\tilde{\\varepsilon}(\\omega)$</h4>\n<p>Under an alternating sinusoidal electric field $\\vec{E}(t) = \\vec{E}_0 e^{-i\\omega t}$, dipolar and ionic reorientations exhibit a phase lag relative to the driving field due to internal friction and damping. The dielectric response becomes a complex function of frequency:</p>\n<div class=\"math-display\">\n$$\\tilde{\\varepsilon}(\\omega) = \\varepsilon_1(\\omega) - i \\varepsilon_2(\\omega)$$\n</div>\n<ul>\n<li><strong>Real Part $\\varepsilon_1(\\omega)$:</strong> Quantifies reversible electrostatic energy storage (capacitance).</li>\n<li><strong>Imaginary Part $\\varepsilon_2(\\omega)$:</strong> Quantifies irreversible energy dissipation and dielectric heating loss.</li>\n</ul>\n<p>The <strong>Loss Tangent</strong> (or dissipation factor) is defined as:</p>\n<div class=\"math-display\">\n$$\\tan\\delta = \\frac{\\varepsilon_2(\\omega)}{\\varepsilon_1(\\omega)}$$\n</div>\n\n<h4>2. The Debye Relaxation Equations</h4>\n<p>Peter Debye modeled the time-dependent relaxation of orientation polarization following the removal of a field as an exponential decay: $\\frac{d\\vec{P}_d}{dt} = - \\frac{\\vec{P}_d}{\\tau_D}$, where $\\tau_D$ is the <strong>Debye relaxation time</strong>. Solving under harmonic driving yields:</p>\n<div class=\"math-display\">\n$$\\tilde{\\varepsilon}(\\omega) = \\varepsilon_\\infty + \\frac{\\varepsilon_s - \\varepsilon_\\infty}{1 - i \\omega \\tau_D}$$\n</div>\n<p>Separating into real and imaginary components yields the <strong>Debye equations</strong>:</p>\n<div class=\"math-display\">\n$$\\varepsilon_1(\\omega) = \\varepsilon_\\infty + \\frac{\\varepsilon_s - \\varepsilon_\\infty}{1 + \\omega^2 \\tau_D^2}, \\quad \\varepsilon_2(\\omega) = \\frac{(\\varepsilon_s - \\varepsilon_\\infty) \\omega \\tau_D}{1 + \\omega^2 \\tau_D^2}$$\n</div>\n<p>where $\\varepsilon_s$ is the static low-frequency dielectric constant ($\\omega \\tau_D \\ll 1$) and $\\varepsilon_\\infty$ is the high-frequency electronic limit ($\\omega \\tau_D \\gg 1$). The dielectric absorption loss $\\varepsilon_2(\\omega)$ reaches a sharp maximum at the resonance condition $\\omega = 1/\\tau_D$.</p>"
        },
        {
          "id": "ssp-7-4",
          "title": "Plasmons, Plasma Frequency & Thomas-Fermi Screening",
          "simulation": "ssp-plasma-frequency-sim",
          "content": "<h4>1. Plasma Oscillations of the Free Electron Gas</h4>\n<p>Consider a free electron gas of density $n$ in a metal. If the entire electron cloud is displaced collectively as a rigid slab by a distance $u$ along $x$ relative to the positive ion core background, a surface charge density $\\sigma = \\pm n e u$ accumulates on the opposing ends of the slab. This generates an internal restoring electric field:</p>\n<div class=\"math-display\">\n$$E = \\frac{\\sigma}{\\varepsilon_0} = \\frac{n e u}{\\varepsilon_0}$$\n</div>\n<p>The classical equation of motion for each electron in the displaced cloud is:</p>\n<div class=\"math-display\">\n$$m \\frac{d^2 u}{dt^2} = - e E = - \\frac{n e^2}{\\varepsilon_0} u \\implies \\frac{d^2 u}{dt^2} + \\left(\\frac{n e^2}{\\varepsilon_0 m}\\right) u = 0$$\n</div>\n<p>This is a simple harmonic oscillator. Collective longitudinal density oscillations of the electron gas occur at the <strong>Plasma Frequency</strong> $\\omega_p$:</p>\n<div class=\"math-display\">\n$$\\omega_p = \\sqrt{\\frac{n e^2}{\\varepsilon_0 m}}$$\n</div>\n<p>A quantum of plasma oscillation is a quasiparticle called a <strong>plasmon</strong>, carrying energy $\\hbar \\omega_p \\sim 5 - 20\\text{ eV}$ in typical metals.</p>\n\n<h4>2. Dielectric Function of a Metal & Ultraviolet Transparency</h4>\n<p>Neglecting damping at optical frequencies ($\\omega \\tau \\gg 1$), the Drude dielectric function of a metal reduces to:</p>\n<div class=\"math-display\">\n$$\\varepsilon(\\omega) = 1 - \\frac{\\omega_p^2}{\\omega^2}$$\n</div>\n<ul>\n<li><strong>For $\\omega < \\omega_p$:</strong> $\\varepsilon(\\omega) < 0$. The refractive index $n = \\sqrt{\\varepsilon}$ is purely imaginary ($n = i \\kappa$), causing total reflection ($R \\approx 100\\%$). Metals act as mirrors for visible light.</li>\n<li><strong>For $\\omega > \\omega_p$:</strong> $\\varepsilon(\\omega) > 0$. The refractive index is real and positive. Electromagnetic waves propagate freely through the metal without reflection: the metal undergoes an <strong>ultraviolet transparency transition</strong>.</li>\n</ul>\n\n<h4>3. Thomas-Fermi Electrostatic Screening</h4>\n<p>When a static test charge $Q$ is embedded in a degenerate electron gas, conduction electrons rearrange to screen its Coulomb potential. In the <strong>Thomas-Fermi approximation</strong>, the bare Coulomb potential $V_0(r) = \\frac{Q}{4\\pi\\varepsilon_0 r}$ is screened exponentially:</p>\n<div class=\"math-display\">\n$$V(r) = \\frac{Q}{4\\pi\\varepsilon_0 r} e^{- k_{TF} r} = \\frac{Q}{4\\pi\\varepsilon_0 r} e^{- r / \\lambda_{TF}}$$\n</div>\n<p>where the <strong>Thomas-Fermi screening wavevector</strong> $k_{TF}$ and screening length $\\lambda_{TF}$ are given by:</p>\n<div class=\"math-display\">\n$$k_{TF}^2 = \\frac{e^2}{\\varepsilon_0} g(E_F) = \\frac{3 n e^2}{2 \\varepsilon_0 E_F} \\implies \\lambda_{TF} = \\frac{1}{k_{TF}} = \\sqrt{\\frac{2\\varepsilon_0 E_F}{3 n e^2}} \\sim 0.5 - 1.0\\text{ \\AA}$$\n</div>\n<p>In typical metals, Coulomb interactions are completely screened within an atomic radius, explaining why electron-electron repulsion can often be neglected.</p>"
        },
        {
          "id": "ssp-7-5",
          "title": "Ferroelectricity, Piezoelectricity & Kramers-Kronig Relations",
          "content": "<h4>1. Ferroelectricity & The Soft Phonon Mode</h4>\n<p>A <strong>ferroelectric crystal</strong> (e.g., Barium Titanate $\\text{BaTiO}_3$, $\\text{PbTiO}_3$) exhibits a spontaneous, reversible electric polarization $\\vec{P}_s$ in the absence of an applied electric field below a critical <strong>Curie temperature</strong> $T_C$. Above $T_C$, the crystal undergoes a structural phase transition to a paraelectric phase governed by the <strong>Curie-Weiss law</strong>:</p>\n<div class=\"math-display\">\n$$\\varepsilon_r = \\varepsilon_0 + \\frac{C}{T - T_C} \\quad (T > T_C)$$\n</div>\n<p>In the Lyddane-Sachs-Teller (LST) dynamical theory, the divergence of $\\varepsilon_r(0)$ as $T \\to T_C$ is driven by the condensation of a transverse optical phonon frequency, the <strong>soft mode</strong>:</p>\n<div class=\"math-display\">\n$$\\omega_{TO}^2(T) = \\gamma (T - T_C) \\to 0 \\quad \\text{as } T \\to T_C^+$$\n</div>\n\n<h4>2. Piezoelectricity & Pyroelectricity</h4>\n<ul>\n<li><strong>Piezoelectric Effect:</strong> Induction of electric polarization $\\vec{P}$ proportional to applied mechanical stress $\\sigma$ ($P_i = d_{ijk} \\sigma_{jk}$), and conversely mechanical strain upon application of an electric field. Occurs exclusively in non-centrosymmetric crystal classes ($20$ of the $32$ point groups). Canonical example: Quartz ($\\text{SiO}_2$), PZT.</li>\n<li><strong>Pyroelectric Effect:</strong> Spontaneous polarization changes as a function of temperature: $\\Delta P_i = p_i \\Delta T$. All pyroelectric materials are piezoelectric, but not all piezoelectrics are pyroelectric.</li>\n</ul>\n\n<h4>3. The Kramers-Kronig Dispersion Relations</h4>\n<p>By the fundamental principle of <strong>causality</strong> (an electric displacement response $\\vec{D}(t)$ cannot precede the applied electric field $\\vec{E}(t)$), Cauchy's residue theorem applied in the complex frequency plane establishes the <strong>Kramers-Kronig relations</strong> connecting the real and imaginary parts of the dielectric function:</p>\n<div class=\"math-display\">\n$$\\varepsilon_1(\\omega) - 1 = \\frac{2}{\\pi} \\mathcal{P} \\int_0^\\infty \\frac{\\omega' \\varepsilon_2(\\omega')}{\\omega'^2 - \\omega^2} d\\omega'$$\n</div>\n<div class=\"math-display\">\n$$\\varepsilon_2(\\omega) = - \\frac{2\\omega}{\\pi} \\mathcal{P} \\int_0^\\infty \\frac{\\varepsilon_1(\\omega') - 1}{\\omega'^2 - \\omega^2} d\\omega'$$\n</div>\n<p>where $\\mathcal{P}$ denotes Cauchy's principal value. Measuring the optical absorption spectrum $\\varepsilon_2(\\omega)$ across all frequencies allows exact determination of the real dielectric permittivity $\\varepsilon_1(\\omega)$ and refractive index without adjustable parameters.</p>"
        }
      ],
      "problems": [
        {
          "id": "ssp-p-7-1",
          "title": "Clausius-Mossotti Polarizability Calculation for Solid Germanium",
          "statement": "Solid Germanium crystallizes in the diamond structure with lattice constant $a = 5.658 \\text{ \u00c5}$ and measured static dielectric constant $\\varepsilon_r = 16.0$. (a) Calculate the atomic number density $N$ of Germanium in atoms per $\\text{m}^3$. (b) Using the Clausius-Mossotti relation, determine the electronic polarizability $\\alpha$ of a Germanium atom in SI units ($\\text{C}\\cdot\\text{m}^2/\\text{V}$) and in volume units ($\\text{\u00c5}^3$).",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Atomic Number Density N",
              "math": "N = \\frac{8}{a^3} = \\frac{8}{(5.658 \\times 10^{-10}\\text{ m})^3} = \\frac{8}{1.8113 \\times 10^{-28}\\text{ m}^3} \\approx 4.417 \\times 10^{28}\\text{ atoms/m}^3",
              "explanation": "Diamond cubic conventional unit cell contains 8 atoms."
            },
            {
              "stepName": "Step 2: Solve the Clausius-Mossotti Equation for Polarizability alpha",
              "math": "\\frac{\\varepsilon_r - 1}{\\varepsilon_r + 2} = \\frac{N \\alpha}{3\\varepsilon_0} \\implies \\alpha = \\frac{3\\varepsilon_0}{N} \\left( \\frac{\\varepsilon_r - 1}{\\varepsilon_r + 2} \\right)",
              "explanation": "Isolate the atomic polarizability alpha."
            },
            {
              "stepName": "Step 3: Evaluate the Dimensionless Dielectric Factor",
              "math": "\\frac{\\varepsilon_r - 1}{\\varepsilon_r + 2} = \\frac{16.0 - 1}{16.0 + 2} = \\frac{15.0}{18.0} = \\frac{5}{6} \\approx 0.8333",
              "explanation": "Compute (epsilon_r - 1) / (epsilon_r + 2)."
            },
            {
              "stepName": "Step 4: Compute Polarizability in SI Units",
              "math": "\\alpha = \\frac{3 \\times (8.8542 \\times 10^{-12}\\text{ F/m})}{4.417 \\times 10^{28}\\text{ m}^{-3}} \\times \\left(\\frac{5}{6}\\right) = \\frac{2.6563 \\times 10^{-11} \\times 0.8333}{4.417 \\times 10^{28}} \\approx 5.011 \\times 10^{-40}\\text{ C}\\cdot\\text{m}^2/\\text{V}",
              "explanation": "Evaluate the numerical value in SI units."
            },
            {
              "stepName": "Step 5: Convert Polarizability to Polarizability Volume alpha'",
              "math": "\\alpha' = \\frac{\\alpha}{4\\pi\\varepsilon_0} = \\frac{5.011 \\times 10^{-40}\\text{ C}\\cdot\\text{m}^2/\\text{V}}{4\\pi \\times (8.8542 \\times 10^{-12}\\text{ F/m})} \\approx 4.504 \\times 10^{-30}\\text{ m}^3 = 4.504\\text{ \\AA}^3",
              "explanation": "Compute the polarizability volume alpha' = alpha / (4 pi epsilon_0)."
            }
          ],
          "answer": "N = 4.42 \\times 10^{28} \\text{ m}^{-3}, \\quad \\alpha = 5.01 \\times 10^{-40} \\text{ C}\\cdot\\text{m}^2/\\text{V}, \\quad \\alpha' = 4.50 \\text{ \u00c5}^3"
        },
        {
          "id": "ssp-p-7-2",
          "title": "Plasma Frequency and Ultraviolet Transmission Edge of Aluminum",
          "statement": "Aluminum is a trivalent metal ($Z_{\\text{val}} = 3$) with atomic mass $M = 26.98 \\text{ g/mol}$ and density $\\rho = 2.70 \\text{ g/cm}^3$. (a) Calculate the free electron density $n$. (b) Determine the plasma frequency $\\omega_p$, the plasmon energy $\\hbar \\omega_p$ in $\\text{eV}$, and the critical ultraviolet transparency threshold wavelength $\\lambda_p$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Conduction Electron Density n",
              "math": "n = Z_{\\text{val}} \\frac{\\rho N_A}{M} = 3 \\times \\frac{(2.70 \\times 10^6\\text{ g/m}^3)(6.022 \\times 10^{23}\\text{ mol}^{-1})}{26.98\\text{ g/mol}} = 3 \\times (6.026 \\times 10^{28}) \\approx 1.808 \\times 10^{29}\\text{ electrons/m}^3",
              "explanation": "Each aluminum atom contributes 3 conduction electrons."
            },
            {
              "stepName": "Step 2: Calculate the Angular Plasma Frequency omega_p",
              "math": "\\omega_p = \\sqrt{\\frac{n e^2}{\\varepsilon_0 m}} = \\sqrt{\\frac{(1.808 \\times 10^{29})(1.6022 \\times 10^{-19})^2}{(8.8542 \\times 10^{-12})(9.109 \\times 10^{-31})}} = \\sqrt{\\frac{4.641 \\times 10^{-9}}{8.065 \\times 10^{-42}}} = \\sqrt{5.754 \\times 10^{32}} \\approx 2.399 \\times 10^{16}\\text{ rad/s}",
              "explanation": "Evaluate the plasma frequency formula."
            },
            {
              "stepName": "Step 3: Calculate the Plasmon Energy in eV",
              "math": "E_p = \\hbar \\omega_p = \\frac{(1.0546 \\times 10^{-34}\\text{ J}\\cdot\\text{s})(2.399 \\times 10^{16}\\text{ rad/s})}{1.6022 \\times 10^{-19}\\text{ J/eV}} \\approx \\frac{2.530 \\times 10^{-18}\\text{ J}}{1.6022 \\times 10^{-19}\\text{ J/eV}} \\approx 15.79\\text{ eV}",
              "explanation": "Convert plasmon energy to electron-volts."
            },
            {
              "stepName": "Step 4: Calculate the Critical Transparency Wavelength lambda_p",
              "math": "\\lambda_p = \\frac{2\\pi c}{\\omega_p} = \\frac{2\\pi \\times (2.9979 \\times 10^8\\text{ m/s})}{2.399 \\times 10^{16}\\text{ s}^{-1}} \\approx 7.852 \\times 10^{-8}\\text{ m} = 78.5\\text{ nm}",
              "explanation": "Light with wavelength shorter than 78.5 nm (deep vacuum ultraviolet) passes freely through aluminum."
            }
          ],
          "answer": "\\omega_p = 2.40 \\times 10^{16} \\text{ rad/s}, \\quad \\hbar\\omega_p = 15.79 \\text{ eV}, \\quad \\lambda_p = 78.5 \\text{ nm}"
        },
        {
          "id": "ssp-p-7-3",
          "title": "Thomas-Fermi Screening Length for Conduction Electrons in Copper",
          "statement": "Copper has a conduction electron density $n = 8.49 \\times 10^{28} \\text{ m}^{-3}$ and Fermi energy $E_F = 7.04 \\text{ eV} = 1.128 \\times 10^{-18} \\text{ J}$. (a) Calculate the Thomas-Fermi screening wavevector $k_{\\text{TF}}$. (b) Determine the Thomas-Fermi screening length $\\lambda_{\\text{TF}}$ in Angstroms, and compare it with the interatomic spacing $a = 3.615 \\text{ \u00c5}$.",
          "steps": [
            {
              "stepName": "Step 1: State the Thomas-Fermi Screening Formula",
              "math": "k_{\\text{TF}} = \\sqrt{\\frac{3 n e^2}{2 \\varepsilon_0 E_F}}",
              "explanation": "Use the degenerate electron gas screening relation."
            },
            {
              "stepName": "Step 2: Substitute Physical Constants and Material Parameters",
              "math": "k_{\\text{TF}}^2 = \\frac{3 \\times (8.49 \\times 10^{28}\\text{ m}^{-3}) \\times (1.6022 \\times 10^{-19}\\text{ C})^2}{2 \\times (8.8542 \\times 10^{-12}\\text{ F/m}) \\times (1.128 \\times 10^{-18}\\text{ J})} = \\frac{6.538 \\times 10^{-9}}{1.9975 \\times 10^{-29}} \\approx 3.273 \\times 10^{20}\\text{ m}^{-2}",
              "explanation": "Compute the square of the screening wavevector."
            },
            {
              "stepName": "Step 3: Calculate the Screening Wavevector k_TF",
              "math": "k_{\\text{TF}} = \\sqrt{3.273 \\times 10^{20}\\text{ m}^{-2}} \\approx 1.809 \\times 10^{10}\\text{ m}^{-1} = 1.809\\text{ \\AA}^{-1}",
              "explanation": "Take the square root."
            },
            {
              "stepName": "Step 4: Determine the Screening Length lambda_TF",
              "math": "\\lambda_{\\text{TF}} = \\frac{1}{k_{\\text{TF}}} = \\frac{1}{1.809 \\times 10^{10}\\text{ m}^{-1}} \\approx 5.528 \\times 10^{-11}\\text{ m} = 0.553\\text{ \\AA}",
              "explanation": "The screening distance is approximately half an Angstrom, much smaller than the 3.615 Angstrom lattice constant of copper."
            }
          ],
          "answer": "k_{\\text{TF}} = 1.81 \\times 10^{10} \\text{ m}^{-1}, \\quad \\lambda_{\\text{TF}} = 0.553 \\text{ \u00c5} \\quad (\\text{Screening occurs within } 15\\% \\text{ of the unit cell size})"
        }
      ]
    },
    {
      "unitNumber": 8,
      "unitId": "unit8-semiconductors",
      "title": "Semiconductors, Junction Devices & Quantum Dots",
      "description": "Comprehensive semiconductor physics and low-dimensional quantum transport: direct vs indirect bandgaps, intrinsic carrier statistics, shallow donor and acceptor doping, drift and diffusion transport, Einstein relation, p-n junction electrostatics, Shockley diode equation, LEDs, photovoltaics, and quantum confinement in 2D quantum wells, 1D wires, and 0D quantum dots.",
      "sections": [
        {
          "id": "ssp-8-1",
          "title": "Band Structures: Direct vs Indirect Semiconductors & Effective Masses",
          "content": "<h4>1. Direct vs. Indirect Band Gap Semiconductors</h4>\n<p>In crystalline semiconductors, the electrical and optical properties are governed by the band gap $E_g$ separating the highest occupied <strong>Valence Band Maximum (VBM)</strong> from the lowest unoccupied <strong>Conduction Band Minimum (CBM)</strong>:</p>\n<ul>\n<li><strong>Direct Band Gap Semiconductors (e.g., $\\text{GaAs}, \\text{InP}, \\text{GaN}$):</strong> Both the conduction band minimum and valence band maximum occur at the <em>same crystal wavevector</em> (typically the zone center $\\Gamma$-point, $\\vec{k} = 0$). Optical photon transitions ($\\Delta \\vec{k} \\approx 0$) occur directly via vertical electric dipole absorption and rapid radiative electron-hole recombination ($h\\nu = E_g$). Essential for efficient optoelectronics: LEDs, laser diodes.</li>\n<li><strong>Indirect Band Gap Semiconductors (e.g., $\\text{Si}, \\text{Ge}, \\text{GaP}$):</strong> The conduction band minimum and valence band maximum occur at <em>different wavevectors</em> (e.g., in Silicon, the VBM is at $\\Gamma$ while the CBM is near $0.85$ of the zone edge along $[100]$). Conservation of crystal momentum forbids first-order radiative transitions: photon absorption or emission requires simultaneous absorption or emission of a lattice <strong>phonon</strong> ($\\hbar\\vec{q}$):\n<div class=\"math-display\">\n$$h\\nu = E_g \\pm \\hbar\\omega_{\\text{phonon}}, \\quad \\vec{k}_{\\text{initial}} + \\vec{k}_{\\text{photon}} \\approx \\vec{k}_{\\text{final}} \\pm \\vec{q}$$\n</div>\n<p>Because second-order phonon-assisted transitions are far less probable, indirect semiconductors exhibit long carrier radiative lifetimes, making them ideal for photovoltaic solar cells and CMOS microelectronics, but inefficient as light emitters.</p></li>\n</ul>\n\n<h4>2. Kane Non-Parabolicity & Anisotropic Effective Masses</h4>\n<p>Near band extrema, expanding $E(\\vec{k})$ to quadratic order yields anisotropic effective mass tensors:</p>\n<div class=\"math-display\">\n$$E_c(\\vec{k}) = E_c + \\frac{\\hbar^2}{2} \\left( \\frac{k_l^2}{m_l^*} + \\frac{k_t^2 + k_t'^2}{m_t^*} \\right)$$\n</div>\n<p>where $m_l^*$ is the longitudinal mass and $m_t^*$ is the transverse mass (e.g., in Silicon, $m_l^* = 0.98 m_0$, $m_t^* = 0.19 m_0$). The density-of-states effective mass is $m_d^* = (m_l^* m_t^{*2})^{1/3}$, while the conductivity effective mass is $m_c^* = 3\\left(\\frac{1}{m_l^*} + \\frac{2}{m_t^*}\\right)^{-1}$.</p>"
        },
        {
          "id": "ssp-8-2",
          "title": "Intrinsic Carrier Statistics & The Law of Mass Action",
          "content": "<h4>1. Intrinsic Conduction Electron Density $n$ and Hole Density $p$</h4>\n<p>In a non-degenerate semiconductor ($E_c - E_F \\gg k_BT$ and $E_F - E_v \\gg k_BT$), the Fermi-Dirac distribution is accurately approximated by the classical Maxwell-Boltzmann tail:</p>\n<div class=\"math-display\">\n$$f(E) \\approx e^{-(E - E_F)/k_B T}$$\n</div>\n<p>Integrating over the parabolic conduction band density of states yields the thermal equilibrium electron concentration:</p>\n<div class=\"math-display\">\n$$n = \\int_{E_c}^\\infty g_c(E) f(E) dE = N_c e^{-(E_c - E_F)/k_B T}$$\n</div>\n<p>where $N_c$ is the <strong>effective density of states in the conduction band</strong>:</p>\n<div class=\"math-display\">\n$$N_c = 2 \\left( \\frac{2\\pi m_e^* k_B T}{h^2} \\right)^{3/2}$$\n</div>\n<p>Similarly, the hole concentration in the valence band is:</p>\n<div class=\"math-display\">\n$$p = \\int_{-\\infty}^{E_v} g_v(E) [1 - f(E)] dE = N_v e^{-(E_F - E_v)/k_B T}$$\n</div>\n<p>where $N_v = 2 \\left( \\frac{2\\pi m_h^* k_B T}{h^2} \\right)^{3/2}$ is the effective density of states in the valence band.</p>\n\n<h4>2. The Law of Mass Action & Intrinsic Carrier Concentration $n_i$</h4>\n<p>Multiplying $n$ and $p$ eliminates the Fermi energy $E_F$ entirely, establishing the fundamental <strong>Law of Mass Action</strong>:</p>\n<div class=\"math-display\">\n$$n \\cdot p = N_c N_v e^{-(E_c - E_v)/k_B T} = N_c N_v e^{-E_g / k_B T} = n_i^2$$\n</div>\n<p>where $n_i$ is the <strong>intrinsic carrier concentration</strong>:</p>\n<div class=\"math-display\">\n$$n_i(T) = \\sqrt{N_c N_v} e^{- E_g / 2 k_B T} \\propto T^{3/2} e^{- E_g / 2 k_B T}$$\n</div>\n<p>This product $n \\cdot p = n_i^2$ holds strictly for any semiconductor in thermal equilibrium, regardless of whether it is intrinsic or heavily doped.</p>\n\n<h4>3. The Intrinsic Fermi Level $E_i$</h4>\n<p>In an undoped intrinsic semiconductor, charge neutrality requires $n = p = n_i$. Equating $n$ and $p$ reveals the position of the intrinsic Fermi level:</p>\n<div class=\"math-display\">\n$$E_i = \\frac{E_c + E_v}{2} + \\frac{3}{4} k_B T \\ln\\left( \\frac{m_h^*}{m_e^*} \\right)$$\n</div>\n<p>Because $\\ln(m_h^*/m_e^*) \\sim 0$, the intrinsic Fermi level lies virtually at the exact mid-gap ($E_g/2$).</p>"
        },
        {
          "id": "ssp-8-3",
          "title": "Extrinsic Doping: Donors, Acceptors & Carrier Transport",
          "content": "<h4>1. Shallow Hydrogenic Donor and Acceptor Impurities</h4>\n<p>Extrinsic semiconductors are created by intentionally introducing trace dopant atoms into the host lattice:</p>\n<ul>\n<li><strong>$n$-Type Doping (Group V in Group IV, e.g., P, As in Si):</strong> Donates an extra valence electron. The extra electron orbits the positively charged donor ion core ($+e$) in a hydrogen-like orbit screened by the large dielectric permittivity of the crystal ($\\varepsilon_r \\sim 12$):\n<div class=\"math-display\">\n$$E_d = \\frac{m_e^*}{m_0} \\frac{1}{\\varepsilon_r^2} E_H = \\frac{m_e^*}{m_0} \\frac{13.6\\text{ eV}}{\\varepsilon_r^2} \\sim 10 - 50\\text{ meV}$$\n</div>\n<p>The donor Bohr radius is expanded to $r_d = \\varepsilon_r \\frac{m_0}{m_e^*} a_0 \\sim 30 - 80\\text{ \\AA}$. At room temperature ($k_BT \\approx 26\\text{ meV}$), virtually all donors are thermally ionized, so $n \\approx N_D$.</p></li>\n<li><strong>$p$-Type Doping (Group III in Group IV, e.g., B, Ga in Si):</strong> Lacks one valence electron, creating a bound acceptor state near the valence band edge that accepts an electron, generating mobile positive holes ($p \\approx N_A$).</li>\n</ul>\n\n<h4>2. Drift and Diffusion Transport</h4>\n<p>In the presence of an electric field $\\vec{E}$ and carrier concentration gradients $\\nabla n$ and $\\nabla p$, total electron and hole current densities comprise both <strong>drift</strong> and <strong>diffusion</strong> components:</p>\n<div class=\"math-display\">\n$$\\vec{J}_n = n e \\mu_n \\vec{E} + e D_n \\nabla n$$\n</div>\n<div class=\"math-display\">\n$$\\vec{J}_p = p e \\mu_p \\vec{E} - e D_p \\nabla p$$\n</div>\n<p>where $\\mu_n, \\mu_p$ are carrier mobilities and $D_n, D_p$ are diffusion coefficients. In thermal equilibrium ($\\vec{J} = 0$), the drift and diffusion currents balance identically, deriving the universal <strong>Einstein Relation</strong>:</p>\n<div class=\"math-display\">\n$$\\frac{D_n}{\\mu_n} = \\frac{D_p}{\\mu_p} = \\frac{k_B T}{e}$$\n</div>\n<p>The total electrical conductivity is given by $\\sigma = e (n \\mu_n + p \\mu_p)$.</p>"
        },
        {
          "id": "ssp-8-4",
          "title": "The p-n Junction: Built-in Potential & Shockley Diode Equation",
          "simulation": "ssp-pn-junction-band-sim",
          "content": "<h4>1. Electrostatics of the Equilibrium p-n Junction</h4>\n<p>When $p$-type and $n$-type semiconductor regions are brought into intimate metallurgical contact, the steep concentration gradient drives diffusion of majority electrons from $n$ to $p$ and holes from $p$ to $n$. This recombination uncovers fixed, ionized donor cores ($N_D^+$) on the $n$-side and ionized acceptor cores ($N_A^-$) on the $p$-side, creating a space-charge <strong>depletion region</strong> of width $W = x_p + x_n$.</p>\n<p>The resulting internal electric field opposes further diffusion until equilibrium is established with a flat Fermi level ($dE_F/dx = 0$). The total electrostatic potential barrier across the junction is the <strong>built-in potential</strong> $V_{bi}$:</p>\n<div class=\"math-display\">\n$$V_{bi} = \\frac{k_B T}{e} \\ln\\left( \\frac{N_A N_D}{n_i^2} \\right)$$\n</div>\n<p>Solving Poisson's equation $\\frac{d^2 V}{dx^2} = - \\frac{\\rho(x)}{\\varepsilon_s}$ under the depletion approximation yields the total depletion layer width under applied voltage $V_a$:</p>\n<div class=\"math-display\">\n$$W = \\sqrt{\\frac{2 \\varepsilon_s (V_{bi} - V_a)}{e} \\left( \\frac{1}{N_A} + \\frac{1}{N_D} \\right)}$$\n</div>\n\n<h4>2. The Shockley Ideal Diode Equation</h4>\n<p>Applying a forward bias voltage ($V_a > 0$) lowers the potential barrier to $V_{bi} - V_a$, exponentially increasing minority carrier injection across the depletion region edges. Integrating minority carrier diffusion currents yields the celebrated <strong>Shockley Diode Equation</strong>:</p>\n<div class=\"math-display\">\n$$I(V_a) = I_0 \\left( e^{e V_a / k_B T} - 1 \\right)$$\n</div>\n<p>where $I_0 = e A \\left( \\frac{D_n n_{p0}}{L_n} + \\frac{D_p p_{n0}}{L_p} \\right)$ is the reverse saturation current.</p>\n\n<h4>3. Optoelectronic Devices</h4>\n<ul>\n<li><strong>Light-Emitting Diodes (LEDs):</strong> Under forward bias, electrons and holes are injected across the junction and recombine radiatively, emitting photons with peak energy $h\\nu \\approx E_g$ ($\\lambda \\approx hc/E_g$).</li>\n<li><strong>Photovoltaic Solar Cells:</strong> Photons with $h\\nu > E_g$ generate electron-hole pairs within and near the depletion region. The built-in electric field sweeps electrons to the $n$-side and holes to the $p$-side, producing a photocurrent $I_{sc}$ and open-circuit photovoltage $V_{oc}$.</li>\n</ul>"
        },
        {
          "id": "ssp-8-5",
          "title": "Low-Dimensional Nanostructures: Quantum Wells, Wires & Quantum Dots",
          "simulation": "ssp-quantum-dot-confinement-sim",
          "content": "<h4>1. Quantum Confinement & Dimensionality Hierarchy</h4>\n<p>When the spatial dimensions of a semiconductor crystal are reduced below the exciton Bohr radius $a_B = \\varepsilon_r \\frac{m_0}{\\mu} a_0 \\sim 2 - 10\\text{ nm}$, continuous electronic energy bands quantize into discrete sub-bands due to <strong>quantum confinement</strong>:</p>\n<ol>\n<li><strong>3D (Bulk):</strong> Confinement in $0$ dimensions; $g(E) \\propto \\sqrt{E}$.</li>\n<li><strong>2D (Quantum Well):</strong> Confinement along $1$ dimension ($L_z \\sim \\text{nm}$), free in $x, y$. Energy spectrum: $E(k_x, k_y, n_z) = E_{n_z} + \\frac{\\hbar^2(k_x^2 + k_y^2)}{2m^*}$. Density of states consists of discrete <strong>staircase steps</strong>: $g_{\\text{2D}}(E) = \\frac{m^*}{\\pi\\hbar^2} \\sum_{n} \\Theta(E - E_n)$.</li>\n<li><strong>1D (Quantum Wire):</strong> Confinement along $2$ dimensions ($L_x, L_y \\sim \\text{nm}$), free along $z$. Energy spectrum: $E(k_z, n_x, n_y) = E_{n_x, n_y} + \\frac{\\hbar^2 k_z^2}{2m^*}$. Density of states exhibits sharp <strong>$E^{-1/2}$ Van Hove singularities</strong>: $g_{\\text{1D}}(E) \\propto \\sum_n (E - E_n)^{-1/2}$.</li>\n<li><strong>0D (Quantum Dot):</strong> Confinement along all $3$ spatial dimensions ($L_x, L_y, L_z \\sim \\text{nm}$). Completely discrete \"artificial atom\" spectrum: $E_{n_x, n_y, n_z} = \\frac{\\pi^2\\hbar^2}{2m^*} \\left(\\frac{n_x^2}{L_x^2} + \\frac{n_y^2}{L_y^2} + \\frac{n_z^2}{L_z^2}\\right)$. Density of states is a collection of <strong>Dirac delta-functions</strong>: $g_{\\text{0D}}(E) = 2 \\sum_i \\delta(E - E_i)$.</li>\n</ol>\n\n<h4>2. Size-Dependent Bandgap Tuning in Quantum Dots (Brus Formula)</h4>\n<p>For a spherical semiconductor nanocrystal (quantum dot) of radius $R$, Louis Brus (1984) derived the quantum confinement energy shift using the effective mass approximation:</p>\n<div class=\"math-display\">\n$$E_g(R) = E_{g,\\text{bulk}} + \\frac{\\hbar^2 \\pi^2}{2 \\mu R^2} - \\frac{1.786 e^2}{4\\pi\\varepsilon_0 \\varepsilon_r R}$$\n</div>\n<p>where $\\frac{1}{\\mu} = \\frac{1}{m_e^*} + \\frac{1}{m_h^*}$ is the exciton reduced mass.</p>\n<ul>\n<li>The first correction term ($+ \\hbar^2\\pi^2 / 2\\mu R^2 \\propto 1/R^2$) represents kinetic quantum confinement energy, pushing the effective band gap upward.</li>\n<li>The second correction term ($- 1.786 e^2 / 4\\pi\\varepsilon_0 \\varepsilon_r R \\propto -1/R$) represents screened Coulomb attraction between electron and hole.</li>\n</ul>\n<p>By simply tuning the nanocrystal radius $R$ from $1.5\\text{ nm}$ to $6.0\\text{ nm}$, the emission color of cadmium selenide ($\\text{CdSe}$) quantum dots can be tuned continuously across the entire visible spectrum from vibrant blue to deep red.</p>"
        }
      ],
      "problems": [
        {
          "id": "ssp-p-8-1",
          "title": "Intrinsic Carrier Concentration and Resistivity of Silicon at 300 K",
          "statement": "At $T = 300 \\text{ K}$, Silicon has a band gap $E_g = 1.12 \\text{ eV}$, effective conduction band density of states $N_c = 2.80 \\times 10^{19} \\text{ cm}^{-3}$, effective valence band density of states $N_v = 1.04 \\times 10^{19} \\text{ cm}^{-3}$, electron mobility $\\mu_n = 1450 \\text{ cm}^2/\\text{V}\\cdot\\text{s}$, and hole mobility $\\mu_p = 450 \\text{ cm}^2/\\text{V}\\cdot\\text{s}$. (a) Calculate the intrinsic carrier concentration $n_i$. (b) Determine the electrical conductivity $\\sigma$ and electrical resistivity $\\rho$ of pure intrinsic Silicon.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Product N_c N_v in SI Units",
              "math": "N_c N_v = (2.80 \\times 10^{25}\\text{ m}^{-3})(1.04 \\times 10^{25}\\text{ m}^{-3}) \\approx 2.912 \\times 10^{50}\\text{ m}^{-6} \\implies \\sqrt{N_c N_v} \\approx 1.7065 \\times 10^{25}\\text{ m}^{-3}",
              "explanation": "Convert densities from cm^-3 to m^-3 and compute their geometric mean."
            },
            {
              "stepName": "Step 2: Evaluate the Boltzmann Exponential Factor",
              "math": "\\frac{E_g}{2 k_B T} = \\frac{1.12\\text{ eV}}{2 \\times (0.02585\\text{ eV})} \\approx \\frac{1.12}{0.0517} \\approx 21.663 \\implies e^{-E_g / 2k_BT} = e^{-21.663} \\approx 3.907 \\times 10^{-10}",
              "explanation": "Evaluate the thermal excitation factor at 300 K."
            },
            {
              "stepName": "Step 3: Calculate the Intrinsic Carrier Concentration n_i",
              "math": "n_i = \\sqrt{N_c N_v} e^{-E_g/2k_BT} = (1.7065 \\times 10^{25}\\text{ m}^{-3}) \\times (3.907 \\times 10^{-10}) \\approx 6.67 \\times 10^{15}\\text{ m}^{-3} = 6.67 \\times 10^9\\text{ cm}^{-3}",
              "explanation": "Compute n_i at 300 K."
            },
            {
              "stepName": "Step 4: Compute Intrinsic Electrical Conductivity and Resistivity",
              "math": "\\sigma_i = e n_i (\\mu_n + \\mu_p) = (1.6022 \\times 10^{-19}\\text{ C}) \\times (6.67 \\times 10^{15}\\text{ m}^{-3}) \\times (0.1450 + 0.0450\\text{ m}^2/\\text{V}\\cdot\\text{s}) = (1.069 \\times 10^{-3}) \\times (0.190) \\approx 2.03 \\times 10^{-4}\\text{ }\\Omega^{-1}\\cdot\\text{m}^{-1}",
              "explanation": "Convert mobilities to m^2/V*s and compute sigma_i."
            },
            {
              "stepName": "Step 5: Determine Intrinsic Resistivity rho_i",
              "math": "\\rho_i = \\frac{1}{\\sigma_i} = \\frac{1}{2.03 \\times 10^{-4}\\text{ }\\Omega^{-1}\\cdot\\text{m}^{-1}} \\approx 4926\\text{ }\\Omega\\cdot\\text{m} \\approx 4.93 \\times 10^5\\text{ }\\Omega\\cdot\\text{cm}",
              "explanation": "Take the reciprocal of conductivity."
            }
          ],
          "answer": "n_i = 6.67 \\times 10^9 \\text{ cm}^{-3} \\quad (6.67 \\times 10^{15} \\text{ m}^{-3}), \\quad \\sigma_i = 2.03 \\times 10^{-4} \\text{ }\u03a9^{-1}\\cdot\\text{m}^{-1}, \\quad \\rho_i = 4926 \\text{ }\u03a9\\cdot\\text{m}"
        },
        {
          "id": "ssp-p-8-2",
          "title": "Hydrogenic Donor Binding Energy and Bohr Radius in Silicon",
          "statement": "Phosphorus ($Z = 15$) is added as a donor impurity to Silicon, which has a relative dielectric permittivity $\\varepsilon_r = 11.7$ and an effective electron mass $m_e^* = 0.26 m_0$. Using the hydrogenic donor model: (a) Calculate the donor ionization energy $E_d$ in $\\text{meV}$. (b) Calculate the effective donor Bohr radius $r_d$ in Angstroms, and determine how many Silicon unit cells ($a = 5.43 \\text{ \u00c5}$) are enclosed within the donor electron orbit.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Donor Ionization Energy E_d",
              "math": "E_d = \\left(\\frac{m_e^*}{m_0}\\right) \\frac{1}{\\varepsilon_r^2} E_H = 0.26 \\times \\frac{13.606\\text{ eV}}{(11.7)^2} = \\frac{3.5376\\text{ eV}}{136.89} \\approx 0.02584\\text{ eV} = 25.84\\text{ meV}",
              "explanation": "Scale the hydrogen Rydberg energy (13.6 eV) by the effective mass and dielectric screening factor epsilon_r^2."
            },
            {
              "stepName": "Step 2: Calculate the Effective Donor Bohr Radius r_d",
              "math": "r_d = \\varepsilon_r \\left(\\frac{m_0}{m_e^*}\\right) a_0 = 11.7 \\times \\left(\\frac{1}{0.26}\\right) \\times (0.5292\\text{ \\AA}) \\approx 11.7 \\times 3.846 \\times 0.5292\\text{ \\AA} \\approx 23.81\\text{ \\AA}",
              "explanation": "Scale the atomic Bohr radius a_0 by epsilon_r and m_0 / m_e*."
            },
            {
              "stepName": "Step 3: Calculate the Number of Enclosed Unit Cells",
              "math": "V_{\\text{orbit}} = \\frac{4}{3}\\pi r_d^3 = \\frac{4}{3}\\pi (23.81\\text{ \\AA})^3 \\approx 5.653 \\times 10^4\\text{ \\AA}^3, \\quad V_{\\text{cell}} = a^3 = (5.431\\text{ \\AA})^3 \\approx 160.2\\text{ \\AA}^3 \\implies N_{\\text{cells}} = \\frac{5.653 \\times 10^4}{160.2} \\approx 353\\text{ unit cells}",
              "explanation": "Divide the volume of the donor electron cloud by the unit cell volume of silicon."
            }
          ],
          "answer": "E_d = 25.8 \\text{ meV}, \\quad r_d = 23.8 \\text{ \u00c5}, \\quad N_{\\text{cells}} \\approx 353 \\text{ unit cells}"
        },
        {
          "id": "ssp-p-8-3",
          "title": "Quantum Dot Size-Dependent Emission Tuning for Cadmium Selenide",
          "statement": "Cadmium Selenide ($\\text{CdSe}$) has a bulk band gap $E_{g,\\text{bulk}} = 1.74 \\text{ eV}$, dielectric constant $\\varepsilon_r = 10.6$, electron effective mass $m_e^* = 0.13 m_0$, and hole effective mass $m_h^* = 0.45 m_0$. Using the Brus quantum confinement formula: (a) Calculate the reduced exciton mass $\\mu$. (b) Determine the effective emission bandgap $E_g(R)$ and emission wavelength $\\lambda$ for a spherical $\\text{CdSe}$ quantum dot of radius $R = 2.0 \\text{ nm}$.",
          "steps": [
            {
              "stepName": "Step 1: Calculate the Reduced Exciton Mass mu",
              "math": "\\frac{1}{\\mu} = \\frac{1}{m_e^*} + \\frac{1}{m_h^*} = \\frac{1}{0.13 m_0} + \\frac{1}{0.45 m_0} = \\frac{7.692 + 2.222}{m_0} = \\frac{9.914}{m_0} \\implies \\mu \\approx 0.1009 m_0 \\approx 9.19 \\times 10^{-32}\\text{ kg}",
              "explanation": "Compute the reduced mass of the electron-hole pair."
            },
            {
              "stepName": "Step 2: Calculate the Kinetic Confinement Energy Shift Delta E_kin",
              "math": "\\Delta E_{\\text{kin}} = \\frac{\\hbar^2 \\pi^2}{2 \\mu R^2} = \\frac{(1.0546 \\times 10^{-34}\\text{ J}\\cdot\\text{s})^2 \\pi^2}{2 \\times (9.19 \\times 10^{-32}\\text{ kg}) \\times (2.0 \\times 10^{-9}\\text{ m})^2} = \\frac{1.0978 \\times 10^{-67}}{7.352 \\times 10^{-49}}\\text{ J} \\approx 1.493 \\times 10^{-19}\\text{ J} \\approx 0.932\\text{ eV}",
              "explanation": "Evaluate the particle-in-a-sphere kinetic confinement energy in electron-volts."
            },
            {
              "stepName": "Step 3: Calculate the Screened Coulomb Attraction Energy Shift Delta E_Coul",
              "math": "\\Delta E_{\\text{Coul}} = \\frac{1.786 e^2}{4\\pi\\varepsilon_0 \\varepsilon_r R} = \\frac{1.786 \\times (1.440\\text{ eV}\\cdot\\text{\\AA})}{10.6 \\times (20.0\\text{ \\AA})} = \\frac{2.5718}{212.0}\\text{ eV} \\approx 0.012\\text{ eV}",
              "explanation": "Compute the electrostatic Coulomb correction term."
            },
            {
              "stepName": "Step 4: Compute the Effective Quantum Dot Bandgap E_g(R)",
              "math": "E_g(R) = E_{g,\\text{bulk}} + \\Delta E_{\\text{kin}} - \\Delta E_{\\text{Coul}} = 1.74\\text{ eV} + 0.932\\text{ eV} - 0.012\\text{ eV} \\approx 2.66\\text{ eV}",
              "explanation": "Sum the bulk gap and quantum corrections."
            },
            {
              "stepName": "Step 5: Determine the Emission Wavelength lambda",
              "math": "\\lambda = \\frac{h c}{E_g(R)} = \\frac{1239.84\\text{ eV}\\cdot\\text{nm}}{2.66\\text{ eV}} \\approx 466\\text{ nm} \\quad (\\text{Vibrant Blue Emission})",
              "explanation": "Convert the band gap energy to emission wavelength. Note that while bulk CdSe emits in the deep red (713 nm), 2.0 nm quantum dots emit blue light at 466 nm."
            }
          ],
          "answer": "\\mu = 0.101 m_0, \\quad E_g(R=2\\text{ nm}) = 2.66 \\text{ eV}, \\quad \\lambda = 466 \\text{ nm} \\quad (\\text{Blue Light})"
        }
      ]
    }
  ]
};
