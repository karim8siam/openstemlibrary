import json

# ==========================================
# UNIT 1: Crystal Structure, Symmetry & X-Ray Diffraction
# ==========================================
u1 = {
    "unitNumber": 1,
    "unitId": "unit1-crystal-structure",
    "title": "Crystal Structure, Symmetry & X-Ray Diffraction",
    "description": "Comprehensive foundation of crystallography: crystalline state, 14 3D Bravais lattices, primitive and conventional unit cells, Wigner-Seitz construction, Miller indices, atomic packing fractions, reciprocal lattice vectors, first Brillouin zone, Laue equations, and experimental X-ray diffraction methods.",
    "sections": [
        {
            "id": "ssp-1-1",
            "title": "The Crystalline State, Space Lattices & 14 Bravais Lattices",
            "simulation": "ssp-bravais-lattice-sim",
            "content": r"""<h4>1. The Crystalline State of Condensed Matter</h4>
<p>Matter in the solid state displays a broad dichotomy in structural organization: <strong>amorphous solids</strong> (e.g., vitreous silica, amorphous polymers), where positional correlations decay rapidly beyond nearest-neighbor atomic separations exhibiting only <em>short-range order</em>, and <strong>crystalline solids</strong> (e.g., metals, diamond, semiconductor silicon, rock-salt), where atomic constituents reside in regular, periodic spatial arrays extending across macroscopic microscopic dimensions of $10^8$ unit intervals, characterized by rigorous <em>long-range translational order</em>.</p>

<h4>2. Mathematical Definition of an Ideal Space Lattice</h4>
<p>An ideal spatial lattice is a purely geometrical abstraction: an infinite three-dimensional periodic array of mathematical points in Euclidean space, where the physical and chemical environment surrounding any arbitrary lattice point $\vec{R}'$ is strictly indistinguishable from that around any other point $\vec{R}$. The translational position vector $\vec{R}$ connecting the arbitrary origin to any point in the lattice is defined uniquely as an integer linear combination of three linearly independent primitive basis vectors $\vec{a}_1, \vec{a}_2, \vec{a}_3$:</p>
<div class="math-display">
$$\vec{R} = n_1 \vec{a}_1 + n_2 \vec{a}_2 + n_3 \vec{a}_3 \quad (n_1, n_2, n_3 \in \mathbb{Z})$$
</div>
<p>A physical <strong>crystal structure</strong> is synthesized mathematically by convolving the geometrical space lattice with an identical group of atoms called the <strong>basis</strong> (or motif) situated at each lattice point:</p>
<div class="math-display">
$$\text{Crystal Structure} = \text{Space Lattice} + \text{Basis}$$
</div>
<p>If the basis comprises $j = 1, 2, \dots, s$ atoms with respective atomic numbers $Z_j$, their spatial coordinates within the unit cell relative to the origin of that cell are defined by fractional vectors:</p>
<div class="math-display">
$$\vec{r}_j = x_j \vec{a}_1 + y_j \vec{a}_2 + z_j \vec{a}_3 \quad (0 \le x_j, y_j, z_j < 1)$$
</div>

<h4>3. The 14 Three-Dimensional Bravais Lattices</h4>
<p>In three spatial dimensions, spatial translational invariance combined with point group rotational and reflection symmetries yields precisely <strong>14 distinct Bravais lattices</strong>, partitioned among <strong>7 crystal systems</strong> characterized by the axial lengths ($a, b, c$) and interaxial angles ($\alpha, \beta, \gamma$):</p>
<ol>
<li><strong>Cubic System ($a = b = c, \alpha = \beta = \gamma = 90^\circ$):</strong> Simple Cubic ($P$), Body-Centered Cubic ($I$), Face-Centered Cubic ($F$).</li>
<li><strong>Tetragonal System ($a = b \neq c, \alpha = \beta = \gamma = 90^\circ$):</strong> Simple Tetragonal ($P$), Body-Centered Tetragonal ($I$).</li>
<li><strong>Orthorhombic System ($a \neq b \neq c, \alpha = \beta = \gamma = 90^\circ$):</strong> Simple ($P$), Base-Centered ($C$), Body-Centered ($I$), Face-Centered ($F$).</li>
<li><strong>Hexagonal System ($a = b \neq c, \alpha = \beta = 90^\circ, \gamma = 120^\circ$):</strong> Simple Hexagonal ($P$).</li>
<li><strong>Trigonal / Rhombohedral System ($a = b = c, \alpha = \beta = \gamma < 120^\circ \neq 90^\circ$):</strong> Primitive Rhombohedral ($R$).</li>
<li><strong>Monoclinic System ($a \neq b \neq c, \alpha = \gamma = 90^\circ \neq \beta$):</strong> Simple Monoclinic ($P$), Base-Centered Monoclinic ($C$).</li>
<li><strong>Triclinic System ($a \neq b \neq c, \alpha \neq \beta \neq \gamma \neq 90^\circ$):</strong> Primitive Triclinic ($P$).</li>
</ol>"""
        },
        {
            "id": "ssp-1-2",
            "title": "Primitive Cells, Wigner-Seitz Construction & Symmetry Operations",
            "content": r"""<h4>1. Primitive vs. Conventional Unit Cells</h4>
<p>A <strong>unit cell</strong> is any volume of space that, when translated by the full set of lattice vectors $\vec{R} = \sum_i n_i \vec{a}_i$, completely fills all space without overlapping or leaving voids. A unit cell is categorized as:</p>
<ul>
<li><strong>Primitive Cell:</strong> A unit cell having minimum volume that contains precisely <em>one</em> net lattice point ($N_{pts} = 1$). Its volume is calculated as the scalar triple product:
<div class="math-display">
$$V_c = |\vec{a}_1 \cdot (\vec{a}_2 \times \vec{a}_3)|$$
</div></li>
<li><strong>Conventional (Non-Primitive) Cell:</strong> A larger unit cell chosen intentionally to preserve and manifest the full rotational and reflection symmetry of the crystal system (e.g., BCC contains 2 lattice points, FCC contains 4 lattice points).</li>
</ul>

<h4>2. The Wigner-Seitz Primitive Cell Construction</h4>
<p>The <strong>Wigner-Seitz cell</strong> is an invariant geometric construction providing a canonical primitive cell that exhibits the full point group symmetry of the Bravais lattice. The algorithm proceeds as follows:</p>
<ol>
<li>Select an arbitrary lattice point as the origin $\vec{0}$.</li>
<li>Draw straight line vectors connecting this origin to all neighboring lattice points $\vec{R}_i$.</li>
<li>Construct planes that perpendicularly bisect each of these vectors at $\vec{R}_i / 2$.</li>
<li>The smallest closed polyhedron enclosing the origin bounded by these bisecting planes constitutes the <em>Wigner-Seitz cell</em>.</li>
</ol>
<p>For an FCC lattice, the Wigner-Seitz cell is a <strong>rhombic dodecahedron</strong> (12 rhombic faces). For a BCC lattice, the Wigner-Seitz cell is a <strong>truncated octahedron</strong> (8 hexagonal faces and 6 square faces).</p>

<h4>3. Crystallographic Symmetry Operations</h4>
<p>The symmetry of a crystal consists of operations that map the periodic spatial arrangement onto itself:</p>
<ul>
<li><strong>Point Group Operations:</strong> Operations leaving at least one point invariant, comprising rotations $C_n = 2\pi/n$ (where $n \in \{1, 2, 3, 4, 6\}$ due to the crystallographic restriction theorem), reflections $\sigma$, inversion $i$, and roto-inversions $S_n$. There exist precisely <strong>32 crystallographic point groups</strong>.</li>
<li><strong>Space Group Operations:</strong> Combinations of point group operations with fractional and primitive lattice translations, including non-symmorphic <em>glide planes</em> (reflection plus fractional translation) and <em>screw axes</em> (rotation plus translation along the axis). In 3D space, there exist precisely <strong>230 crystallographic space groups</strong>.</li>
</ul>"""
        },
        {
            "id": "ssp-1-3",
            "title": "Miller Indices & Interplanar Spacing of Crystal Planes",
            "content": r"""<h4>1. Definition and Determination of Miller Indices $(hkl)$</h4>
<p>A crystal plane is characterized by a set of three coprime integers $(hkl)$, known as its <strong>Miller indices</strong>, which specify its spatial orientation relative to the primitive or conventional crystal axes $\vec{a}_1, \vec{a}_2, \vec{a}_3$:</p>
<ol>
<li>Determine the intercepts of the plane along the three crystallographic axes in units of lattice constants: $x_1 a, x_2 b, x_3 c$.</li>
<li>Take the reciprocals of these fractional intercepts: $1/x_1, 1/x_2, 1/x_3$.</li>
<li>Clear fractions by multiplying by their least common denominator to obtain the smallest coprime triplet of integers $(h, k, l)$. If an intercept is negative, say $-x_1$, the corresponding index is written with an overbar as $(\bar{h}kl)$.</li>
</ol>

<h4>2. Mathematical Derivation of Interplanar Spacing $d_{hkl}$</h4>
<p>Consider a family of parallel equidistant planes designated by Miller indices $(hkl)$. The distance of the first plane from the coordinate origin along the normal unit vector $\hat{n}$ is the interplanar spacing $d_{hkl}$.</p>
<p>In a <strong>Cubic crystal system</strong> ($a = b = c, \alpha = \beta = \gamma = 90^\circ$), the equation of a plane intersecting the axes at $a/h, a/k, a/l$ is:</p>
<div class="math-display">
$$\frac{x}{a/h} + \frac{y}{a/k} + \frac{z}{a/l} = 1 \implies hx + ky + lz = a$$
</div>
<p>The perpendicular distance from the origin $(0,0,0)$ to this plane is given by analytical geometry:</p>
<div class="math-display">
$$d_{hkl} = \frac{|h(0) + k(0) + l(0) - a|}{\sqrt{h^2 + k^2 + l^2}} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$
</div>
<p>For a general <strong>Orthorhombic system</strong> ($a \neq b \neq c, \alpha = \beta = \gamma = 90^\circ$):</p>
<div class="math-display">
$$\frac{1}{d_{hkl}^2} = \frac{h^2}{a^2} + \frac{k^2}{b^2} + \frac{l^2}{c^2}$$
</div>
<p>For a <strong>Hexagonal system</strong> ($a = b \neq c, \alpha = \beta = 90^\circ, \gamma = 120^\circ$):</p>
<div class="math-display">
$$\frac{1}{d_{hkl}^2} = \frac{4}{3}\left(\frac{h^2 + hk + k^2}{a^2}\right) + \frac{l^2}{c^2}$$
</div>"""
        },
        {
            "id": "ssp-1-4",
            "title": "Simple Crystal Structures & Atomic Packing Factors",
            "content": r"""<h4>1. Atomic Packing Fraction (APF) Formalism</h4>
<p>The <strong>Atomic Packing Fraction (APF)</strong> quantifies the volumetric efficiency with which hard spherical atoms of radius $R$ fill the unit cell volume $V_{cell}$:</p>
<div class="math-display">
$$\text{APF} = \frac{N_{\text{eff}} \times V_{\text{atom}}}{V_{\text{cell}}} = \frac{N_{\text{eff}} \times \frac{4}{3}\pi R^3}{V_{\text{cell}}}$$
</div>
<p>where $N_{\text{eff}}$ is the effective number of whole atoms inside the conventional unit cell.</p>

<h4>2. Detailed Comparison of Canonical Metallic and Covalent Structures</h4>
<ol>
<li><strong>Simple Cubic (SC):</strong>
<ul>
<li>$N_{\text{eff}} = 8 \times (1/8) = 1$.</li>
<li>Touching condition along edge: $a = 2R \implies R = a/2$.</li>
<li>$\text{APF} = \frac{1 \times \frac{4}{3}\pi (a/2)^3}{a^3} = \frac{\pi}{6} \approx 0.5236$ ($52.4\%$). Coordination number $CN = 6$.</li>
</ul></li>
<li><strong>Body-Centered Cubic (BCC):</strong>
<ul>
<li>$N_{\text{eff}} = 8 \times (1/8) + 1 = 2$.</li>
<li>Touching condition along body diagonal: $4R = \sqrt{3}a \implies R = \frac{\sqrt{3}}{4}a$.</li>
<li>$\text{APF} = \frac{2 \times \frac{4}{3}\pi \left(\frac{\sqrt{3}}{4}a\right)^3}{a^3} = \frac{\sqrt{3}\pi}{8} \approx 0.6802$ ($68.0\%$). Coordination number $CN = 8$.</li>
</ul></li>
<li><strong>Face-Centered Cubic (FCC):</strong>
<ul>
<li>$N_{\text{eff}} = 8 \times (1/8) + 6 \times (1/2) = 4$.</li>
<li>Touching condition along face diagonal: $4R = \sqrt{2}a \implies R = \frac{\sqrt{2}}{4}a$.</li>
<li>$\text{APF} = \frac{4 \times \frac{4}{3}\pi \left(\frac{\sqrt{2}}{4}a\right)^3}{a^3} = \frac{\sqrt{2}\pi}{6} \approx 0.7405$ ($74.1\%$). Coordination number $CN = 12$.</li>
</ul></li>
<li><strong>Hexagonal Close-Packed (HCP):</strong>
<ul>
<li>Stacking sequence: $ABABAB\dots$ Ideal axial ratio: $c/a = \sqrt{8/3} \approx 1.633$.</li>
<li>$N_{\text{eff}} = 12 \times (1/6) + 2 \times (1/2) + 3 = 6$.</li>
<li>$\text{APF} = \frac{\pi}{3\sqrt{2}} \approx 0.7405$ ($74.1\%$). Coordination number $CN = 12$.</li>
</ul></li>
<li><strong>Diamond Cubic Structure:</strong>
<ul>
<li>FCC lattice with a two-atom basis: $(0,0,0)$ and $\left(\frac{1}{4}, \frac{1}{4}, \frac{1}{4}\right)$.</li>
<li>$N_{\text{eff}} = 8$ atoms. Touching condition along quarter body diagonal: $8R = \sqrt{3}a \implies R = \frac{\sqrt{3}}{8}a$.</li>
<li>$\text{APF} = \frac{\sqrt{3}\pi}{16} \approx 0.3401$ ($34.0\%$). Coordination number $CN = 4$ (tetrahedral $sp^3$ coordination).</li>
</ul></li>
<li><strong>Ionic Structures (NaCl, CsCl, ZnS Zincblende):</strong>
<ul>
<li><strong>NaCl:</strong> FCC Bravais lattice of $\text{Cl}^-$ with $\text{Na}^+$ at $(1/2, 0, 0)$; $CN = 6:6$, $4$ formula units/cell.</li>
<li><strong>CsCl:</strong> Simple cubic Bravais lattice with $\text{Cs}^+$ at $(0,0,0)$ and $\text{Cl}^-$ at $(1/2, 1/2, 1/2)$; $CN = 8:8$, $1$ formula unit/cell.</li>
<li><strong>ZnS (Zincblende):</strong> FCC lattice of $\text{S}^{2-}$ with $\text{Zn}^{2+}$ occupying half the tetrahedral interstitial sites; $CN = 4:4$.</li>
</ul></li>
</ol>"""
        },
        {
            "id": "ssp-1-5",
            "title": "Reciprocal Lattice, Brillouin Zones & X-Ray Diffraction",
            "simulation": "ssp-bragg-xray-diffraction-sim",
            "content": r"""<h4>1. Rigorous Definition of the Reciprocal Lattice</h4>
<p>Given direct lattice primitive basis vectors $\vec{a}_1, \vec{a}_2, \vec{a}_3$ with unit cell volume $V_c = \vec{a}_1 \cdot (\vec{a}_2 \times \vec{a}_3)$, the corresponding <strong>reciprocal lattice primitive vectors</strong> $\vec{b}_1, \vec{b}_2, \vec{b}_3$ are defined uniquely by the orthogonality relation:</p>
<div class="math-display">
$$\vec{a}_i \cdot \vec{b}_j = 2\pi \delta_{ij}$$
</div>
<p>Explicit vector formulas for the reciprocal basis vectors are:</p>
<div class="math-display">
$$\vec{b}_1 = 2\pi \frac{\vec{a}_2 \times \vec{a}_3}{V_c}, \quad \vec{b}_2 = 2\pi \frac{\vec{a}_3 \times \vec{a}_1}{V_c}, \quad \vec{b}_3 = 2\pi \frac{\vec{a}_1 \times \vec{a}_2}{V_c}$$
</div>
<p>An arbitrary reciprocal lattice vector $\vec{G}$ is expressed in terms of integer Miller components $(h, k, l)$:</p>
<div class="math-display">
$$\vec{G}_{hkl} = h \vec{b}_1 + k \vec{b}_2 + l \vec{b}_3$$
</div>
<p><strong>Fundamental Theorems of the Reciprocal Lattice:</strong></p>
<ol>
<li>The reciprocal lattice vector $\vec{G}_{hkl}$ is normal to the family of crystal planes $(hkl)$ in direct space.</li>
<li>The magnitude of $\vec{G}_{hkl}$ is inversely proportional to the interplanar spacing $d_{hkl}$:
<div class="math-display">
$$|\vec{G}_{hkl}| = \frac{2\pi}{d_{hkl}} \implies d_{hkl} = \frac{2\pi}{|\vec{G}_{hkl}|}$$
</div></li>
<li>The reciprocal lattice of an FCC direct lattice is a BCC reciprocal lattice, and vice-versa.</li>
</ol>

<h4>2. The First Brillouin Zone</h4>
<p>The <strong>First Brillouin Zone (1st BZ)</strong> is the Wigner-Seitz primitive cell of the <em>reciprocal lattice</em>. It contains all wavevectors $\vec{k}$ that can propagate through the periodic crystal without undergoing elastic Bragg reflection from the lattice planes. The zone boundaries are defined by the Bragg condition:</p>
<div class="math-display">
$$\vec{k} \cdot \left(\frac{1}{2}\vec{G}\right) = \left(\frac{1}{2}\vec{G}\right)^2 \implies 2\vec{k} \cdot \vec{G} + G^2 = 0$$
</div>

<h4>3. Von Laue Diffraction Equations & Bragg's Law</h4>
<p>When an incident plane wave of X-rays with wavevector $\vec{k}$ ($|\vec{k}| = 2\pi/\lambda$) scatters elastically from a crystal to wavevector $\vec{k}'$ ($|\vec{k}'| = |\vec{k}|$), the scattering wavevector transfer is $\Delta \vec{k} = \vec{k}' - \vec{k}$. Constructive interference across the entire crystal occurs if and only if the <strong>Laue condition</strong> is satisfied:</p>
<div class="math-display">
$$\Delta \vec{k} = \vec{G}_{hkl}$$
</div>
<p>Taking the magnitude squared: $|\vec{k}' - \vec{k}|^2 = G^2 \implies k^2 + k'^2 - 2 k k' \cos(180^\circ - 2\theta) = G^2$. Since $k' = k = 2\pi/\lambda$ and $G = 2\pi/d_{hkl}$:</p>
<div class="math-display">
$$2k^2(1 - \cos(\pi - 2\theta)) = 4k^2 \sin^2\theta = G^2 \implies 2\left(\frac{2\pi}{\lambda}\right)\sin\theta = \frac{2\pi}{d_{hkl}} \implies 2d_{hkl}\sin\theta = \lambda$$
</div>
<p>Generalizing to order $n$, this yields <strong>Bragg's Law of X-Ray Diffraction</strong>:</p>
<div class="math-display">
$$2d_{hkl} \sin\theta = n\lambda$$
</div>

<h4>4. Experimental X-Ray Diffraction Techniques</h4>
<ol>
<li><strong>Laue Method:</strong> Uses polychromatic (white) continuous X-ray radiation on a stationary single crystal. Each crystal plane $(hkl)$ selects a specific wavelength satisfying $2d\sin\theta = \lambda$. Used to determine crystal orientation and symmetry.</li>
<li><strong>Rotating Crystal Method:</strong> Uses monochromatic X-ray radiation on a single crystal rotating about a crystallographic axis. Different planes pass through the Bragg angle $\theta$ sequentially, forming layer lines on a cylindrical film.</li>
<li><strong>Powder Diffraction (Debye-Scherrer) Method:</strong> Uses monochromatic X-rays incident upon a finely powdered polycrystalline specimen containing millions of randomly oriented crystallites. Diffraction emerges as concentric cones of half-angle $2\theta$, yielding characteristic diffraction rings used for phase identification.</li>
</ol>"""
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
                    "math": r"d_{111} = \frac{a}{\sqrt{h^2 + k^2 + l^2}} = \frac{5.431\text{ \AA}}{\sqrt{1^2 + 1^2 + 1^2}} = \frac{5.431}{\sqrt{3}}\text{ \AA} \approx 3.1356\text{ \AA}",
                    "explanation": "Apply the cubic interplanar spacing formula for Miller indices (h, k, l) = (1, 1, 1)."
                },
                {
                    "stepName": "Step 2: Apply Bragg's Law to Find Diffraction Angle theta",
                    "math": r"\sin\theta_{111} = \frac{n\lambda}{2d_{111}} = \frac{1 \times 1.5406\text{ \AA}}{2 \times 3.1356\text{ \AA}} = \frac{1.5406}{6.2712} \approx 0.24566",
                    "explanation": "Substitute n=1, lambda = 1.5406 Angstroms, and d_111 into Bragg's equation 2 d sin(theta) = n lambda."
                },
                {
                    "stepName": "Step 3: Evaluate Arcsin and Deflection Angle 2 theta",
                    "math": r"\theta_{111} = \arcsin(0.24566) = 14.22^\circ \implies 2\theta = 28.44^\circ",
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
                    "math": r"\vec{a}_1 = \frac{a}{2}(\hat{y} + \hat{z}), \quad \vec{a}_2 = \frac{a}{2}(\hat{z} + \hat{x}), \quad \vec{a}_3 = \frac{a}{2}(\hat{x} + \hat{y})",
                    "explanation": "The primitive vectors of FCC connect the origin to three adjacent face centers. The primitive cell volume is one-fourth of the conventional cubic cell volume:"
                },
                {
                    "stepName": "Step 2: Calculate Numerical Value of Direct Primitive Volume V_c",
                    "math": r"V_c = \frac{a^3}{4} = \frac{(3.615\text{ \AA})^3}{4} = \frac{47.241\text{ \AA}^3}{4} \approx 11.810\text{ \AA}^3 = 1.181 \times 10^{-29}\text{ m}^3",
                    "explanation": "Evaluate V_c = a^3 / 4 using the lattice parameter of copper."
                },
                {
                    "stepName": "Step 3: Derive Reciprocal Vectors and Brillouin Zone Volume",
                    "math": r"\vec{b}_1 = \frac{2\pi}{a}(-\hat{x} + \hat{y} + \hat{z}), \quad \vec{b}_2 = \frac{2\pi}{a}(\hat{x} - \hat{y} + \hat{z}), \quad \vec{b}_3 = \frac{2\pi}{a}(\hat{x} + \hat{y} - \hat{z})",
                    "explanation": "These are the primitive vectors of a Body-Centered Cubic (BCC) reciprocal lattice. The volume of the First Brillouin Zone is given by V_BZ = (2 pi)^3 / V_c:"
                },
                {
                    "stepName": "Step 4: Compute First Brillouin Zone Volume V_BZ",
                    "math": r"V_{BZ} = \frac{(2\pi)^3}{V_c} = \frac{4 (2\pi)^3}{a^3} = \frac{32\pi^3}{(3.615\text{ \AA})^3} \approx \frac{992.88}{47.241}\text{ \AA}^{-3} \approx 21.017\text{ \AA}^{-3} = 2.102 \times 10^{31}\text{ m}^{-3}",
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
                    "math": r"\theta_1 = \frac{44.67^\circ}{2} = 22.335^\circ \implies \sin\theta_1 = \sin(22.335^\circ) \approx 0.38004",
                    "explanation": "Convert 2 theta to theta and calculate sin(theta) for the first peak."
                },
                {
                    "stepName": "Step 2: Calculate sin(theta) for the Second Peak",
                    "math": r"\theta_2 = \frac{65.02^\circ}{2} = 32.51^\circ \implies \sin\theta_2 = \sin(32.51^\circ) \approx 0.53745",
                    "explanation": "Convert 2 theta to theta and calculate sin(theta) for the second peak."
                },
                {
                    "stepName": "Step 3: Compare Ratio of sin^2(theta) to BCC Selection Rules",
                    "math": r"\frac{\sin^2\theta_1}{\sin^2\theta_2} = \frac{(0.38004)^2}{(0.53745)^2} = \frac{0.14443}{0.28885} \approx 0.5000 = \frac{1}{2}",
                    "explanation": "In a BCC lattice, allowed reflections require h+k+l = even. The lowest permitted values of s = h^2 + k^2 + l^2 are (110) with s=2, and (200) with s=4. The ratio is 2/4 = 1/2, perfectly matching the experimental ratio."
                },
                {
                    "stepName": "Step 4: Calculate the Lattice Constant a",
                    "math": r"a = \frac{\lambda \sqrt{h^2 + k^2 + l^2}}{2\sin\theta_1} = \frac{1.5418\text{ \AA} \times \sqrt{2}}{2 \times 0.38004} = \frac{1.5418 \times 1.4142}{0.76008} \approx 2.8686\text{ \AA}",
                    "explanation": "Using peak 1 with (hkl) = (110), solve for the lattice parameter a."
                }
            ],
            "answer": "\\text{Peak 1: } (110), \\quad \\text{Peak 2: } (200), \\quad a = 2.869 \\text{ \u00c5}"
        }
    ]
}

# ==========================================
# UNIT 2: Interatomic Forces & Crystal Bonding
# ==========================================
u2 = {
    "unitNumber": 2,
    "unitId": "unit2-crystal-bonding",
    "title": "Interatomic Forces & Crystal Bonding",
    "description": "Exhaustive treatment of cohesive energy and binding mechanisms: ionic bonding, exact derivation of the Madelung constant, Born-Mayer repulsive potential, bulk modulus, covalent bonding, Van der Waals dispersion forces, Lennard-Jones 6-12 potential, and metallic cohesion.",
    "sections": [
        {
            "id": "ssp-2-1",
            "title": "Classification of Chemical Bonds & Cohesive Energy",
            "content": r"""<h4>1. Cohesive Energy of Crystalline Solids</h4>
<p>The <strong>cohesive energy</strong> (or binding energy) $E_{\text{coh}}$ of a crystal is defined as the net energy required to disassemble the solid into its constituent neutral free atoms (or ions in ionic physics) at infinite mutual separation at zero temperature ($T = 0\text{ K}$):</p>
<div class="math-display">
$$E_{\text{coh}} = E_{\text{isolated atoms}} - E_{\text{crystal}} > 0$$
</div>
<p>Cohesion originates entirely from electromagnetic interactions governed by quantum mechanics. Solids are classified into five primary bonding categories based on the distribution of their valence electrons:</p>
<ol>
<li><strong>Ionic Crystals (e.g., $\text{NaCl}, \text{CsCl}, \text{LiF}$):</strong> Electrostatic attraction between positive cations and negative anions formed by complete valence electron transfer. Highly localized electron density, strong binding ($E_{\text{coh}} \approx 5 - 10\text{ eV/atom}$), high melting points, electrical insulators in the solid state.</li>
<li><strong>Covalent Crystals (e.g., Diamond, $\text{Si}, \text{Ge}, \text{GaAs}$):</strong> Cohesion via quantum mechanical sharing of electron pairs localized along directional bonds formed by overlapping hybridized atomic orbitals ($sp^3$). Extreme hardness, high melting points, semiconductor or insulator band structure.</li>
<li><strong>Metallic Crystals (e.g., $\text{Na}, \text{Cu}, \text{Fe}, \text{Al}$):</strong> Valence electrons delocalize completely into an itinerant electron gas ("Fermi sea") permeating an array of positively charged ion cores. Non-directional bonding, high electrical and thermal conductivities, ductility.</li>
<li><strong>Van der Waals (Molecular) Crystals (e.g., Solid $\text{Ar}, \text{Kr}, \text{CH}_4$):</strong> Weak cohesion ($E_{\text{coh}} \approx 0.05 - 0.2\text{ eV/atom}$) arising from fluctuating quantum dipole-induced dipole interactions. Low melting and boiling points, soft mechanical properties.</li>
<li><strong>Hydrogen-Bonded Crystals (e.g., Ice $\text{H}_2\text{O}, \text{HF}$, nucleic acids):</strong> Directional electrostatic dipole attractions mediated by an electropositive bare proton sandwiched between electronegative lone pairs (O, N, F). Intermediate strength ($0.1 - 0.5\text{ eV/bond}$).</li>
</ol>"""
        },
        {
            "id": "ssp-2-2",
            "title": "Ionic Crystals: Born-Mayer Potential & Madelung Constant",
            "simulation": "ssp-madelung-potential-sim",
            "content": r"""<h4>1. Electrostatic Madelung Energy Formalism</h4>
<p>Consider an ionic crystal consisting of $2N$ ions ($N$ positive cations and $N$ negative anions with charges $\pm q$). Let $R$ be the nearest-neighbor interionic separation distance. The total electrostatic Coulomb potential energy of ion $i$ interacting with all other ions $j \neq i$ in the crystal is:</p>
<div class="math-display">
$$U_{i,\text{coul}} = \sum_{j \neq i} \frac{(\pm q)(\mp q)}{4\pi\varepsilon_0 r_{ij}} = - \frac{q^2}{4\pi\varepsilon_0 R} \sum_{j \neq i} \frac{\pm 1}{p_{ij}}$$
</div>
<p>where $r_{ij} = p_{ij} R$ denotes the distance between ions $i$ and $j$ measured in units of nearest-neighbor distance $R$, and the sign is positive for unlike charges (attraction) and negative for like charges (repulsion).</p>
<p>The dimensionless sum is defined as the <strong>Madelung Constant</strong> $\alpha$:</p>
<div class="math-display">
$$\alpha = \sum_{j \neq i} \frac{\pm 1}{p_{ij}}$$
</div>
<p>Multiplying by $N$ ion pairs (to avoid double-counting the pair interactions), the total electrostatic Madelung energy of the crystal is:</p>
<div class="math-display">
$$U_{\text{Madelung}}(R) = - N \alpha \frac{q^2}{4\pi\varepsilon_0 R}$$
</div>

<h4>2. Calculation of the Madelung Constant for a One-Dimensional Ionic Chain</h4>
<p>Consider an infinite 1D chain of alternating cations and anions with nearest-neighbor distance $R$. Choosing an arbitrary positive ion as the origin, its neighbors are situated at distances $R, 2R, 3R, \dots$ to both the left and right:</p>
<ul>
<li>Two opposite ions at distance $1R$: contribution $+2 \times (1/1)$</li>
<li>Two identical ions at distance $2R$: contribution $-2 \times (1/2)$</li>
<li>Two opposite ions at distance $3R$: contribution $+2 \times (1/3)$</li>
</ul>
<p>The 1D Madelung constant $\alpha_{\text{1D}}$ is therefore given by the alternating harmonic series:</p>
<div class="math-display">
$$\alpha_{\text{1D}} = 2 \left( 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \dots \right)$$
</div>
<p>Recalling the Taylor series expansion of $\ln(1+x) = x - x^2/2 + x^3/3 - x^4/4 + \dots$ evaluated at $x = 1$:</p>
<div class="math-display">
$$\sum_{m=1}^{\infty} \frac{(-1)^{m-1}}{m} = \ln(2) \implies \alpha_{\text{1D}} = 2 \ln(2) \approx 2 \times 0.69315 = 1.38629$$
</div>

<h4>3. Madelung Constants for 3D Ionic Lattices</h4>
<p>In three dimensions, the summation is conditionally convergent and requires specialized summing techniques (e.g., the <strong>Evjen method</strong> of neutral concentric polyhedra or the <strong>Ewald summation method</strong> in reciprocal space):</p>
<ul>
<li><strong>Rock-Salt ($\text{NaCl}$):</strong> $\alpha = 1.747565$</li>
<li><strong>Cesium Chloride ($\text{CsCl}$):</strong> $\alpha = 1.762675$</li>
<li><strong>Zincblende ($\text{ZnS}$):</strong> $\alpha = 1.63805$</li>
<li><strong>Wurtzite ($\text{ZnS}$):</strong> $\alpha = 1.64132$</li>
<li><strong>Fluorite ($\text{CaF}_2$):</strong> $\alpha = 5.03878$</li>
</ul>"""
        },
        {
            "id": "ssp-2-3",
            "title": "Cohesive Energy & Bulk Modulus of Ionic Crystals",
            "content": r"""<h4>1. Total Cohesive Energy with Born-Mayer Repulsion</h4>
<p>At short interionic separations, the electron clouds of adjacent ions overlap. By the Pauli Exclusion Principle, overlapping closed electron shells must occupy higher unpopulated quantum states, generating a steep quantum mechanical repulsive potential. The total potential energy per ion pair $U_{\text{tot}}(R)$ is modeled by the <strong>Born-Mayer equation</strong>:</p>
<div class="math-display">
$$U_{\text{tot}}(R) = - \frac{\alpha q^2}{4\pi\varepsilon_0 R} + z B e^{-R/\rho}$$
</div>
<p>where $z$ is the coordination number (number of nearest neighbors), $B$ is a repulsive strength constant, and $\rho \approx 0.33\text{ \AA}$ is the characteristic range parameter of core repulsion.</p>

<h4>2. Equilibrium Interionic Separation $R_0$</h4>
<p>At equilibrium ($R = R_0$), the net mechanical force vanishes: $\left.\frac{dU_{\text{tot}}}{dR}\right|_{R=R_0} = 0$:</p>
<div class="math-display">
$$\left.\frac{dU_{\text{tot}}}{dR}\right|_{R_0} = \frac{\alpha q^2}{4\pi\varepsilon_0 R_0^2} - \frac{z B}{\rho} e^{-R_0/\rho} = 0 \implies z B e^{-R_0/\rho} = \frac{\alpha q^2}{4\pi\varepsilon_0 R_0} \left(\frac{\rho}{R_0}\right)$$
</div>
<p>Substituting this repulsive term back into $U_{\text{tot}}(R_0)$ yields the celebrated <strong>Born-Mayer cohesive energy formula</strong> per ion pair:</p>
<div class="math-display">
$$U_{\text{tot}}(R_0) = - \frac{\alpha q^2}{4\pi\varepsilon_0 R_0} \left( 1 - \frac{\rho}{R_0} \right)$$
</div>
<p>Since $\rho / R_0 \approx 0.33\text{ \AA} / 2.82\text{ \AA} \approx 0.12$, core repulsion reduces the pure electrostatic Coulomb binding energy by approximately $10 - 15\%$.</p>

<h4>3. Derivation of Bulk Modulus $B$</h4>
<p>The isothermal bulk modulus $B$ measures the resistance of the crystal to uniform hydrostatic compression: $B = - V \frac{dP}{dV}$. At $T = 0\text{ K}$, the hydrostatic pressure is $P = - \frac{dU_{\text{cryst}}}{dV}$, which implies:</p>
<div class="math-display">
$$B = V \frac{d^2 U_{\text{cryst}}}{dV^2} = \left. V_0 \frac{d^2 U_{\text{tot}}}{dV^2} \right|_{V=V_0}$$
</div>
<p>For a rock-salt cubic crystal with volume per ion pair $V = 2 R^3$ (where $V_0 = 2 R_0^3$), changing variables via $\frac{dU}{dV} = \frac{dU/dR}{dV/dR} = \frac{1}{6R^2} \frac{dU}{dR}$ leads directly to:</p>
<div class="math-display">
$$B = \frac{1}{18 R_0} \left. \frac{d^2 U_{\text{tot}}}{dR^2} \right|_{R=R_0} = \frac{\alpha q^2}{72 \pi \varepsilon_0 R_0^4} \left( \frac{R_0}{\rho} - 2 \right)$$
</div>"""
        },
        {
            "id": "ssp-2-4",
            "title": "Van der Waals Crystals & Lennard-Jones (6-12) Potential",
            "simulation": "ssp-lennard-jones-potential-sim",
            "content": r"""<h4>1. Origin of London Dispersion Forces</h4>
<p>In inert gas crystals (solid $\text{Ne}, \text{Ar}, \text{Kr}, \text{Xe}$), atoms possess completely closed electronic shells with spherical symmetry and zero permanent dipole moment ($\langle \vec{p} \rangle = 0$). However, quantum fluctuations in electron cloud positions produce an instantaneous fluctuating electric dipole $\vec{p}_1(t) \sim e \vec{x}(t)$. This instantaneous dipole generates an electric field at distance $R$:</p>
<div class="math-display">
$$E_1 \approx \frac{p_1}{4\pi\varepsilon_0 R^3}$$
</div>
<p>This electric field induces a dipole moment in the adjacent neutral atom proportional to its electronic polarizability $\alpha_{\text{pol}}$: $\vec{p}_2 = \alpha_{\text{pol}} \vec{E}_1 \propto \frac{\alpha_{\text{pol}} p_1}{R^3}$. The resulting dipole-dipole electrostatic interaction energy is attractive and scales inversely with the sixth power of distance:</p>
<div class="math-display">
$$U_{\text{disp}}(R) = - \vec{p}_2 \cdot \vec{E}_1 \propto - \frac{\alpha_{\text{pol}} p_1^2}{R^6} = - \frac{C}{R^6}$$
</div>

<h4>2. The Lennard-Jones (6-12) Potential</h4>
<p>When two inert gas atoms approach within the distance of their closed electron shells, Pauli core exclusion generates a steep repulsive potential, empirically parameterized as an inverse-twelfth power $1/R^{12}$. The total interaction potential between a pair of atoms separated by distance $R$ is the <strong>Lennard-Jones (6-12) potential</strong>:</p>
<div class="math-display">
$$U_{LJ}(R) = 4\varepsilon \left[ \left(\frac{\sigma}{R}\right)^{12} - \left(\frac{\sigma}{R}\right)^6 \right]$$
</div>
<p>where:</p>
<ul>
<li>$\varepsilon$: Depth of the potential well (binding energy minimum).</li>
<li>$\sigma$: Finite distance at which the interatomic potential is zero ($U_{LJ}(\sigma) = 0$).</li>
</ul>
<p>The minimum of the two-body potential occurs where $\frac{dU_{LJ}}{dR} = 0$:</p>
<div class="math-display">
$$\frac{dU_{LJ}}{dR} = 4\varepsilon \left[ -\frac{12\sigma^{12}}{R^{13}} + \frac{6\sigma^6}{R^7} \right] = 0 \implies R_{\text{min}} = 2^{1/6}\sigma \approx 1.122\sigma$$
</div>
<p>At this equilibrium separation, the potential energy minimum is exactly $U_{LJ}(R_{\text{min}}) = -\varepsilon$.</p>

<h4>3. Cohesive Energy of Inert Gas FCC Crystals</h4>
<p>In an FCC crystal of $N$ inert gas atoms, summing over all pairs with $R_{ij} = p_{ij} R$ yields the total crystal potential energy:</p>
<div class="math-display">
$$U_{\text{tot}}(R) = 2 N \varepsilon \left[ A_{12} \left(\frac{\sigma}{R}\right)^{12} - A_6 \left(\frac{\sigma}{R}\right)^6 \right]$$
</div>
<p>For an FCC lattice, the lattice sums over all neighbors are geometric constants:</p>
<div class="math-display">
$$A_{12} = \sum_{j \neq 0} p_{0j}^{-12} \approx 12.13188, \quad A_6 = \sum_{j \neq 0} p_{0j}^{-6} \approx 14.45392$$
</div>
<p>Minimizing $U_{\text{tot}}(R)$ with respect to $R$ yields the equilibrium crystal nearest-neighbor separation $R_0$ and the total cohesive energy per atom:</p>
<div class="math-display">
$$R_0 = \left( \frac{2 A_{12}}{A_6} \right)^{1/6} \sigma \approx 1.09 \sigma, \quad \frac{U_{\text{tot}}(R_0)}{N} = - 2.15 (4\varepsilon) \approx - 8.61 \varepsilon$$
</div>"""
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
                    "math": r"U(R) = - \frac{\alpha e^2}{4\pi\varepsilon_0 R} + \frac{B}{R^n}",
                    "explanation": "Write down the potential energy per NaCl molecule combining the attractive Coulomb-Madelung term and the Born power-law repulsive term."
                },
                {
                    "stepName": "Step 2: Apply the Equilibrium Condition at R = R_0",
                    "math": r"\left.\frac{dU}{dR}\right|_{R_0} = \frac{\alpha e^2}{4\pi\varepsilon_0 R_0^2} - \frac{n B}{R_0^{n+1}} = 0 \implies \frac{B}{R_0^n} = \frac{\alpha e^2}{4\pi\varepsilon_0 R_0} \frac{1}{n}",
                    "explanation": "Set the first derivative of potential energy with respect to interionic distance to zero at R = R_0."
                },
                {
                    "stepName": "Step 3: Substitute B back into Cohesive Energy",
                    "math": r"E_{\text{coh}} = - U(R_0) = \frac{\alpha e^2}{4\pi\varepsilon_0 R_0} \left( 1 - \frac{1}{n} \right)",
                    "explanation": "Substitute the repulsive term B / R_0^n back into the expression for U(R_0)."
                },
                {
                    "stepName": "Step 4: Numerically Calculate the Pure Electrostatic Energy",
                    "math": r"U_M = \frac{\alpha e^2}{4\pi\varepsilon_0 R_0} = \frac{1.7476 \times 1.440\text{ eV}\cdot\text{\AA}}{2.820\text{ \AA}} = \frac{2.5165}{2.820}\text{ eV} \approx 8.924\text{ eV}",
                    "explanation": "Evaluate the electrostatic Coulomb energy using e^2 / (4 pi epsilon_0) = 1.440 eV * Angstrom."
                },
                {
                    "stepName": "Step 5: Solve for the Repulsive Exponent n",
                    "math": r"1 - \frac{1}{n} = \frac{E_{\text{coh}}}{U_M} = \frac{7.95\text{ eV}}{8.924\text{ eV}} \approx 0.8909 \implies \frac{1}{n} = 1 - 0.8909 = 0.1091 \implies n = \frac{1}{0.1091} \approx 9.16",
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
                    "math": r"B = \frac{\alpha e^2}{72 \pi \varepsilon_0 R_0^4} \left( \frac{R_0}{\rho} - 2 \right)",
                    "explanation": "Use the bulk modulus formula derived from the second derivative of the Born-Mayer crystal potential."
                },
                {
                    "stepName": "Step 2: Evaluate the Dimensionless Factor (R_0 / rho - 2)",
                    "math": r"\frac{R_0}{\rho} = \frac{3.147\text{ \AA}}{0.330\text{ \AA}} \approx 9.5364 \implies \left(\frac{R_0}{\rho} - 2\right) = 7.5364",
                    "explanation": "Compute the repulsive curvature term."
                },
                {
                    "stepName": "Step 3: Evaluate the Prefactor in SI Units",
                    "math": r"\frac{\alpha e^2}{4\pi\varepsilon_0} = 1.7476 \times (2.307 \times 10^{-28}\text{ J}\cdot\text{m}) \approx 4.0318 \times 10^{-28}\text{ J}\cdot\text{m}",
                    "explanation": "Calculate the numerator product in SI units."
                },
                {
                    "stepName": "Step 4: Compute the Bulk Modulus B",
                    "math": r"B = \frac{4.0318 \times 10^{-28}\text{ J}\cdot\text{m} \times 7.5364}{18 \times (3.147 \times 10^{-10}\text{ m})^4} = \frac{3.0385 \times 10^{-27}}{18 \times 9.808 \times 10^{-38}} = \frac{3.0385 \times 10^{-27}}{1.7654 \times 10^{-36}} \approx 1.721 \times 10^{10}\text{ Pa} = 17.21\text{ GPa}",
                    "explanation": "Divide through by 18 R_0^4 to find the bulk modulus in Pascals (N/m^2)."
                },
                {
                    "stepName": "Step 5: Calculate the Compressibility beta",
                    "math": r"\beta = \frac{1}{B} = \frac{1}{17.21\text{ GPa}} \approx 0.0581\text{ GPa}^{-1} = 5.81 \times 10^{-11}\text{ Pa}^{-1}",
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
                    "math": r"R_0 = \left( \frac{2 A_{12}}{A_6} \right)^{1/6} \sigma = \left( \frac{2 \times 12.1319}{14.4539} \right)^{1/6} (3.40\text{ \AA}) = (1.6787)^{0.16667} (3.40\text{ \AA}) \approx 1.0906 \times 3.40\text{ \AA} \approx 3.708\text{ \AA}",
                    "explanation": "Compute the equilibrium bond distance using the ratio of the lattice sums."
                },
                {
                    "stepName": "Step 2: Relate Nearest-Neighbor Distance to FCC Lattice Parameter a",
                    "math": r"R_0 = \frac{a}{\sqrt{2}} \implies a = \sqrt{2} R_0 = \sqrt{2} \times 3.708\text{ \AA} \approx 5.244\text{ \AA}",
                    "explanation": "In an FCC lattice, nearest neighbors touch along face diagonals of length sqrt(2) * a."
                },
                {
                    "stepName": "Step 3: Calculate the Cohesive Energy per Atom",
                    "math": r"u_0 = - \frac{U_{\text{tot}}(R_0)}{N} = 2.15 \times 4\varepsilon = 8.60 \times (10.42\text{ meV}) \approx 89.61\text{ meV/atom} = 1.436 \times 10^{-20}\text{ J/atom}",
                    "explanation": "Evaluate the binding energy per atom at equilibrium."
                },
                {
                    "stepName": "Step 4: Convert Cohesive Energy to Molar Basis",
                    "math": r"E_{\text{coh, molar}} = u_0 \times N_A = (1.436 \times 10^{-20}\text{ J}) \times (6.022 \times 10^{23}\text{ mol}^{-1}) \approx 8647\text{ J/mol} = 8.65\text{ kJ/mol}",
                    "explanation": "Multiply by Avogadro's number N_A to obtain the cohesive energy per mole."
                }
            ],
            "answer": "R_0 = 3.708 \\text{ \u00c5}, \\quad a = 5.244 \\text{ \u00c5}, \\quad E_{\\text{coh}} = 8.65 \\text{ kJ/mol} \\quad (89.61 \\text{ meV/atom})"
        }
    ]
}

with open("ssp_u1.json", "w") as f:
    json.dump(u1, f, indent=2)
print("ssp_u1.json created successfully!")

with open("ssp_u2.json", "w") as f:
    json.dump(u2, f, indent=2)
print("ssp_u2.json created successfully!")
