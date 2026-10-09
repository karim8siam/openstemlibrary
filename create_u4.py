import json

def get_unit_4():
    u4 = {
        "id": "unit-4",
        "number": 4,
        "title": "Miller Indices, Reciprocal Space & Atomic-Scale Diffraction Mechanics",
        "leadSummary": "Crystallographic orientation notation, interplanar spacing derivations, reciprocal lattice mechanics, Ewald sphere geometry, kinematic Bragg-Laue diffraction theory, structure factor analysis, systematic absences, and experimental powder XRD, electron, and neutron diffraction techniques.",
        "simulations": ["sim_ssc_xrd_powder_diffraction"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "Miller Indices: Definition, Crystallographic Planes & Direction Vectors",
                "content": r"""The quantitative analysis of crystalline diffraction, surface chemistry, and anisotropic mechanical deformation requires a mathematically rigorous coordinate notation to identify planes of lattice points and spatial directions within periodic lattices. This system was formulated by William Hallowes Miller (1839) and is universally denoted as **Miller indices**.

### Direction Indices $[uvw]$
A crystallographic direction is a vector passing through lattice points. Let the direct lattice basis vectors be $\\mathbf{a}, \\mathbf{b}, \\mathbf{c}$. Any lattice translation vector $\\mathbf{T}$ can be written as:
\\[
\\mathbf{T} = u\\mathbf{a} + v\\mathbf{b} + w\\mathbf{c}
\\]
where $u, v, w \\in \\mathbb{Z}$.
To determine the direction indices $[uvw]$ of an arbitrary vector passing through the origin:
1. Express the vector components along the crystal axes $\\mathbf{a}, \\mathbf{b}, \\mathbf{c}$ in terms of the lattice parameters $a, b, c$.
2. Reduce these components to the smallest integers having the same ratio:
\\[
[u\\ v\\ w] = \\left[\\frac{u'}{\\gcd(u',v',w')}\\ \\frac{v'}{\\gcd(u',v',w')}\\ \\frac{w'}{\\gcd(u',v',w')}\\right]
\\]
3. Negative components are written with an overbar, e.g., $[\\bar{1}10]$ represents $-1\\mathbf{a} + 1\\mathbf{b} + 0\\mathbf{c}$.
4. A set of symmetry-equivalent directions (dictated by the point group of the crystal) is enclosed in angle brackets: $\\langle uvw \\rangle$. For example, in a cubic crystal, $\\langle 100 \\rangle$ encompasses the six equivalent directions $[100]$, $[\\bar{1}00]$, $[010]$, $[0\\bar{1}0]$, $[001]$, and $[00\\bar{1}]$.

### Miller Indices of Lattice Planes $(hkl)$
A family of parallel, equally spaced lattice planes is defined by three integers $(hkl)$ obtained through the following algorithm:
1. Find the intercepts of the plane with the crystallographic axes $\\mathbf{a}, \\mathbf{b}, \\mathbf{c}$ in units of the lattice parameters $a, b, c$. Let these intercepts be $x_1, x_2, x_3$. If a plane is parallel to an axis, its intercept is at infinity ($\\infty$).
2. Take the reciprocals of the fractional intercepts:
\\[
h' = \\frac{1}{x_1}, \\quad k' = \\frac{1}{x_2}, \\quad l' = \\frac{1}{x_3}
\\]
3. Multiply or divide by a common factor to clear fractions, reducing $h', k', l'$ to the smallest coprime integers $(hkl)$:
\\[
(h\\ k\\ l) \\quad \\text{where} \\quad \\gcd(h,k,l) = 1 \\quad \\text{for primitive families}
\\]
4. Negative intercepts are designated with overbars: $(\\bar{h}kl)$.
5. A family of symmetry-equivalent crystallographic planes is enclosed in braces: $\\{hkl\\}$. In cubic symmetry, $\\{100\\} = (100), (\\bar{1}00), (010), (0\\bar{1}0), (001), (00\\bar{1})$.

### Hexagonal Miller-Bravais Indices $(hkil)$
In hexagonal and trigonal systems where axes $\\mathbf{a}_1, \\mathbf{a}_2, \\mathbf{a}_3$ lie in the basal plane at $120^\\circ$ angles with vertical axis $\\mathbf{c}$, standard $(hkl)$ indices do not immediately reveal hexagonal rotational equivalence. The **Miller-Bravais** 4-index notation $(hkil)$ resolves this by introducing a redundant third index $i$:
\\[
i = -(h + k)
\\]
Because $\\mathbf{a}_1 + \\mathbf{a}_2 + \\mathbf{a}_3 = \\mathbf{0}$, the condition $h + k + i = 0$ is strictly preserved. In this system, prism planes $(10\\bar{1}0)$, $(01\\bar{1}0)$, and $(\\bar{1}100)$ are immediately seen to belong to the identical family $\\{10\\bar{1}0\\}$ by permuting indices."""
            },
            {
                "secNumber": "4.2",
                "title": "Interplanar Spacing (d_hkl) Formulations for All Crystal Systems",
                "content": r"""The perpendicular distance between adjacent parallel planes of the family $(hkl)$ is the **interplanar spacing** $d_{hkl}$. This parameter directly dictates the diffraction angle $\\theta$ observed in X-ray and electron scattering experiments.

### Derivation for the Orthorhombic System
In an orthogonal coordinate system where $\\alpha = \\beta = \\gamma = 90^\\circ$ and unit cell dimensions are $a, b, c$, consider the plane $(hkl)$ passing closest to the origin. Its intercepts on the axes are $a/h, b/k, c/l$.
The normal unit vector $\\hat{\\mathbf{n}}$ from the origin to the plane forms direction cosines:
\\[
\\cos \\alpha_1 = \\frac{d_{hkl}}{a/h} = \\frac{h\\, d_{hkl}}{a}, \\quad \\cos \\beta_1 = \\frac{d_{hkl}}{b/k} = \\frac{k\\, d_{hkl}}{b}, \\quad \\cos \\gamma_1 = \\frac{d_{hkl}}{c/l} = \\frac{l\\, d_{hkl}}{c}
\\]
Since the sum of squared direction cosines for orthogonal axes equals unity ($\\cos^2 \\alpha_1 + \\cos^2 \\beta_1 + \\cos^2 \\gamma_1 = 1$):
\\[
\\left(\\frac{h\\, d_{hkl}}{a}\\right)^2 + \\left(\\frac{k\\, d_{hkl}}{b}\\right)^2 + \\left(\\frac{l\\, d_{hkl}}{c}\\right)^2 = 1
\\]
Factoring out $d_{hkl}^2$ gives the general orthorhombic formula:
\\[
\\frac{1}{d_{hkl}^2} = \\frac{h^2}{a^2} + \\frac{k^2}{b^2} + \\frac{l^2}{c^2}
\\]

### Special Cases: Cubic and Tetragonal Systems
1. **Cubic System** ($a = b = c$):
\\[
\\frac{1}{d_{hkl}^2} = \\frac{h^2 + k^2 + l^2}{a^2} \\implies d_{hkl} = \\frac{a}{\\sqrt{h^2 + k^2 + l^2}}
\\]
2. **Tetragonal System** ($a = b \\ne c$, $\\alpha = \\beta = \\gamma = 90^\\circ$):
\\[
\\frac{1}{d_{hkl}^2} = \\frac{h^2 + k^2}{a^2} + \\frac{l^2}{c^2}
\\]

### Non-Orthogonal Systems
1. **Hexagonal System** ($a = b \\ne c$, $\\alpha = \\beta = 90^\\circ, \\gamma = 120^\\circ$):
\\[
\\frac{1}{d_{hkl}^2} = \\frac{4}{3}\\left(\\frac{h^2 + hk + k^2}{a^2}\\right) + \\frac{l^2}{c^2}
\\]
2. **Monoclinic System** ($a \\ne b \\ne c$, $\\alpha = \\gamma = 90^\\circ, \\beta \\ne 90^\\circ$):
\\[
\\frac{1}{d_{hkl}^2} = \\frac{1}{\\sin^2 \\beta} \\left( \\frac{h^2}{a^2} + \\frac{k^2\\sin^2 \\beta}{b^2} + \\frac{l^2}{c^2} - \\frac{2hl\\cos\\beta}{ac} \\right)
\\]
3. **Triclinic System** (General case with metric tensor $G_{ij} = \\mathbf{a}_i \\cdot \\mathbf{a}_j$):
\\[
\\frac{1}{d_{hkl}^2} = \\frac{1}{V^2} \\begin{vmatrix} h & k & l & 0 \\\\ a^2 & ab\\cos\\gamma & ac\\cos\\beta & h \\\\ ab\\cos\\gamma & b^2 & bc\\cos\\alpha & k \\\\ ac\\cos\\beta & bc\\cos\\alpha & c^2 & l \\end{vmatrix}
\\]
where $V = abc\\sqrt{1 - \\cos^2\\alpha - \\cos^2\\beta - \\cos^2\\gamma + 2\\cos\\alpha\\cos\\beta\\cos\\gamma}$ is the unit cell volume."""
            },
            {
                "secNumber": "4.3",
                "title": "The Reciprocal Lattice: Geometric Construction, Reciprocal Vectors & Ewald Sphere",
                "content": r"""The concept of the **reciprocal lattice**—introduced by Josiah Willard Gibbs and formalized in crystallography by Paul Ewald (1913)—is the foundational mathematical bridge connecting real-space crystal geometry to diffraction phenomena observed in momentum space ($\\mathbf{k}$-space).

### Mathematical Definition of Reciprocal Basis Vectors
Let $\\mathbf{a}, \\mathbf{b}, \\mathbf{c}$ be the primitive basis vectors of the direct crystal lattice with unit cell volume $V_c = \\mathbf{a} \\cdot (\\mathbf{b} \\times \\mathbf{c})$. The reciprocal lattice basis vectors $\\mathbf{a}^*, \\mathbf{b}^*, \\mathbf{c}^*$ (often written $\\mathbf{b}_1, \\mathbf{b}_2, \\mathbf{b}_3$ in solid-state physics with a $2\\pi$ factor) are defined by the orthogonality relations:
\\[
\\mathbf{a}^* = \\frac{\\mathbf{b} \\times \\mathbf{c}}{\\mathbf{a} \\cdot (\\mathbf{b} \\times \\mathbf{c})}, \\quad \\mathbf{b}^* = \\frac{\\mathbf{c} \\times \\mathbf{a}}{\\mathbf{a} \\cdot (\\mathbf{b} \\times \\mathbf{c})}, \\quad \\mathbf{c}^* = \\frac{\\mathbf{a} \\times \\mathbf{b}}{\\mathbf{a} \\cdot (\\mathbf{b} \\times \\mathbf{c})}
\\]
These basis vectors satisfy the Kronecker delta relations:
\\[
\\mathbf{a}_i \\cdot \\mathbf{a}_j^* = \\delta_{ij} = \\begin{cases} 1 & i = j \\\\ 0 & i \\ne j \\end{cases}
\\]
In physics conventions (including band theory), a factor of $2\\pi$ is incorporated: $\\mathbf{b}_i = 2\\pi \\mathbf{a}_i^*$, ensuring $\\mathbf{a}_i \\cdot \\mathbf{b}_j = 2\\pi \\delta_{ij}$.

### Fundamental Theorems of the Reciprocal Lattice
1. **Normality Theorem**: Every reciprocal lattice vector
\\[
\\mathbf{G}_{hkl} = h\\mathbf{a}^* + k\\mathbf{b}^* + l\\mathbf{c}^*
\\]
is perpendicular to the real-space crystallographic plane $(hkl)$.
*Proof*: Consider two vectors $\\mathbf{u}_1$ and $\\mathbf{u}_2$ lying in the plane $(hkl)$:
\\[
\\mathbf{u}_1 = \\frac{\\mathbf{a}}{h} - \\frac{\\mathbf{b}}{k}, \\quad \\mathbf{u}_2 = \\frac{\\mathbf{b}}{k} - \\frac{\\mathbf{c}}{l}
\\]
Taking the scalar product:
\\[
\\mathbf{G}_{hkl} \\cdot \\mathbf{u}_1 = (h\\mathbf{a}^* + k\\mathbf{b}^* + l\\mathbf{c}^*) \\cdot \\left(\\frac{\\mathbf{a}}{h} - \\frac{\\mathbf{b}}{k}\\right) = h\\frac{1}{h} - k\\frac{1}{k} = 1 - 1 = 0
\\]
Similarly, $\\mathbf{G}_{hkl} \\cdot \\mathbf{u}_2 = 0$. Because $\\mathbf{G}_{hkl}$ is orthogonal to two non-parallel vectors spanning the plane $(hkl)$, it is strictly normal to $(hkl)$.

2. **Spacing Theorem**: The magnitude of $\\mathbf{G}_{hkl}$ is inversely proportional to the interplanar spacing $d_{hkl}$:
\\[
|\\mathbf{G}_{hkl}| = \\frac{1}{d_{hkl}} \\quad \\text{(crystallography)} \\quad \\text{or} \\quad |\\mathbf{G}_{hkl}| = \\frac{2\\pi}{d_{hkl}} \\quad \\text{(physics)}
\\]

### Reciprocal Lattices of Common Bravais Lattices
- **Simple Cubic (SC)**: Direct lattice parameter $a$. The reciprocal lattice is another simple cubic lattice with parameter $a^* = 1/a$ (or $2\\pi/a$).
- **Face-Centered Cubic (FCC)**: Direct lattice primitive vectors form an FCC cell with volume $a^3/4$. Its reciprocal lattice is **Body-Centered Cubic (BCC)** with cubic reciprocal cell parameter $a^*_{\\text{cubic}} = 2/a$ (or $4\\pi/a$).
- **Body-Centered Cubic (BCC)**: Direct lattice primitive vectors form a BCC cell with volume $a^3/2$. Its reciprocal lattice is **Face-Centered Cubic (FCC)**.

### The Ewald Sphere Construction
Paul Ewald introduced an elegant geometric construction to represent the diffraction condition:
1. Draw the reciprocal lattice of the crystal.
2. Direct the incident wavevector $\\mathbf{k}_0$ ($|\\mathbf{k}_0| = 1/\\lambda$) terminating at the reciprocal lattice origin $(000)$.
3. Construct a sphere of radius $R = |\\mathbf{k}_0| = 1/\\lambda$ centered at the tip of $\\mathbf{k}_0$ (point $C$).
4. **Diffraction occurs if and only if any reciprocal lattice point $(hkl)$ lies exactly on the surface of the Ewald sphere**.
When a point $P = (hkl)$ intersects the sphere surface, the scattered wavevector $\\mathbf{k}_s = \\vec{CP}$ has magnitude $1/\\lambda$, ensuring elastic scattering ($|\\mathbf{k}_s| = |\\mathbf{k}_0|$), and satisfies the Laue condition $\\mathbf{k}_s - \\mathbf{k}_0 = \\mathbf{G}_{hkl}$."""
            },
            {
                "secNumber": "4.4",
                "title": "Bragg's Law of Diffraction: Derivation, Physical Meaning & Dynamical vs Kinematic Limits",
                "content": r"""In 1912, William Henry Bragg and William Lawrence Bragg formulated an intuitive physical model of X-ray diffraction by treating crystal planes as specular semi-transparent mirrors.

### Geometrical Derivation of Bragg's Law
Consider a monochromatic beam of X-rays with wavelength $\\lambda$ incident at a glancing angle $\\theta$ (the **Bragg angle**) on a set of parallel crystallographic planes with interplanar spacing $d_{hkl}$.
1. Ray 1 reflects specularly from the uppermost plane at atom $A$.
2. Ray 2 reflects specularly from the adjacent parallel plane at atom $B$, separated by perpendicular distance $d_{hkl}$.
3. Drop perpendiculars from atom $A$ onto the incident ray ($AD$) and the reflected ray ($AE$).
4. The extra path length $\\Delta L$ traveled by Ray 2 relative to Ray 1 is:
\\[
\\Delta L = DB + BE = d_{hkl}\\sin\\theta + d_{hkl}\\sin\\theta = 2d_{hkl}\\sin\\theta
\\]
5. For constructive interference between the scattered waves, the path difference must be an integer multiple of the incident wavelength $\\lambda$:
\\[
2d_{hkl}\\sin\\theta = n\\lambda, \\quad n \\in \\{1, 2, 3, \\dots\\}
\\]
In modern crystallographic notation, the order of reflection $n$ is absorbed directly into the Miller indices $(hkl)$: a second-order reflection $n=2$ from $(100)$ is denoted as the first-order reflection from $(200)$, where $d_{200} = d_{100}/2$. Hence, Bragg's Law is written simply:
\\[
\\lambda = 2d_{hkl}\\sin\\theta
\\]

### Physical Limitations: Why $\\sin\\theta \\le 1$
Because $|\\sin\\theta| \\le 1$, constructive diffraction can only occur if:
\\[
\\lambda \\le 2d_{hkl}
\\]
If the incident radiation has wavelength $\\lambda > 2d_{\\max}$, no diffraction peaks can exist at any angle. For typical crystal lattice parameters ($a \\approx 2 - 6\\text{ Å}$), $d_{hkl} \\approx 0.5 - 4\\text{ Å}$. Therefore, diffraction requires radiation with $\\lambda \\sim 0.5 - 2.5\\text{ Å}$, which corresponds precisely to the X-ray regime (e.g., $\\text{Cu } K_\\alpha_1 = 1.54056\\text{ Å}$, $\\text{Mo } K_\\alpha = 0.71073\\text{ Å}$), thermal neutrons ($\\lambda \\sim 1 - 2\\text{ Å}$), and high-energy electrons ($100 - 300\\text{ keV}$, $\\lambda \\sim 0.02 - 0.04\\text{ Å}$).

### Kinematic vs Dynamical Diffraction Theories
- **Kinematic Theory (Darwin-Staverman)**: Assumes single scattering only. The incident beam passes through the crystal without significant attenuation, and scattered beams do not rescatter. Valid for imperfect, mosaic crystals, powders, and thin specimens ($\\text{thickness} < 100\\text{ nm}$).
- **Dynamical Theory (Ewald-von Laue)**: Accounts for multiple coherent scattering between incident and diffracted beams inside a perfect, macroscopic single crystal. Gives rise to anomalous transmission (the Borrmann effect), extinction effects (primary and secondary extinction), and Darwin reflection curves with finite plateau widths."""
            },
            {
                "secNumber": "4.5",
                "title": "The Laue Equations & Vector Formulation of Diffraction",
                "content": r"""Max von Laue (1912) formulated diffraction from a three-dimensional periodic array of scatterers without invoking the planar specular mirror analogy.

### The Three Laue Equations
Consider a 1D row of identical atoms separated by translation vector $\\mathbf{a}$. Let unit vectors in the direction of the incident and scattered beams be $\\hat{\\mathbf{s}}_0$ and $\\hat{\\mathbf{s}}$.
The path difference between rays scattered by adjacent atoms is $\\mathbf{a} \\cdot (\\hat{\\mathbf{s}} - \\hat{\\mathbf{s}}_0)$. For constructive interference across the 1D lattice:
\\[
\\mathbf{a} \\cdot (\\hat{\\mathbf{s}} - \\hat{\\mathbf{s}}_0) = h\\lambda \\quad (h \\in \\mathbb{Z})
\\]
Extending this requirement to an infinite three-dimensional crystal with basis vectors $\\mathbf{a}, \\mathbf{b}, \\mathbf{c}$ requires simultaneous constructive interference along all three crystal dimensions:
\\[
\\begin{cases}
\\mathbf{a} \\cdot (\\hat{\\mathbf{s}} - \\hat{\\mathbf{s}}_0) = h\\lambda \\\\
\\mathbf{b} \\cdot (\\hat{\\mathbf{s}} - \\hat{\\mathbf{s}}_0) = k\\lambda \\\\
\\mathbf{c} \\cdot (\\hat{\\mathbf{s}} - \\hat{\\mathbf{s}}_0) = l\\lambda
\\end{cases}
\\]
These are the **three Laue equations**. Geometrically, each equation defines a family of coaxial cones around the corresponding crystal axis. Diffraction beams emerge only along the lines of intersection of three mutually compatible cones.

### Vector Equivalence to the Reciprocal Lattice
Define the wavevector of the incident beam as $\\mathbf{k}_0 = \\frac{1}{\\lambda}\\hat{\\mathbf{s}}_0$ and the scattered beam as $\\mathbf{k} = \\frac{1}{\\lambda}\\hat{\\mathbf{s}}$. The scattering vector $\\Delta \\mathbf{k}$ is:
\\[
\\Delta \\mathbf{k} = \\mathbf{k} - \\mathbf{k}_0
\\]
Dividing the Laue equations by $\\lambda$:
\\[
\\mathbf{a} \\cdot \\Delta \\mathbf{k} = h, \\quad \\mathbf{b} \\cdot \\Delta \\mathbf{k} = k, \\quad \\mathbf{c} \\cdot \\Delta \\mathbf{k} = l
\\]
Recalling the definition of the reciprocal lattice basis vectors where $\\mathbf{a}_i \\cdot \\mathbf{a}_j^* = \\delta_{ij}$, the unique solution for $\\Delta \\mathbf{k}$ satisfying all three equations simultaneously is:
\\[
\\Delta \\mathbf{k} = h\\mathbf{a}^* + k\\mathbf{b}^* + l\\mathbf{c}^* = \\mathbf{G}_{hkl}
\\]
In physics notation (where $|\\mathbf{k}| = 2\\pi/\\lambda$):
\\[
\\Delta \\mathbf{k} = \\mathbf{k} - \\mathbf{k}_0 = \\mathbf{G}_{hkl}
\\]
This elegant result proves that **the Laue condition is mathematically identical to Bragg's Law**: diffraction occurs if and only if the change in photon wavevector equals a reciprocal lattice vector $\\mathbf{G}_{hkl}$."""
            },
            {
                "secNumber": "4.6",
                "title": "Structure Factor F_hkl & Systematic Absences (P, I, F, C Centering)",
                "content": r"""While the dimensions of the unit cell determine the positions of diffraction peaks ($\\theta$ angles), the arrangement of specific atoms within the unit cell determines the **intensity** of each reflection through the **structure factor** $F_{hkl}$.

### Mathematical Formulation of the Structure Factor
The unit cell structure factor $F_{hkl}$ represents the total amplitude and phase of radiation scattered by all $N$ atoms in the unit cell relative to a single free electron at the origin:
\\[
F_{hkl} = \\sum_{j=1}^{N} f_j \\exp\\left[ 2\\pi i (h x_j + k y_j + l z_j) \\right]
\\]
where:
- $(x_j, y_j, z_j)$ are the fractional coordinates of the $j$-th atom in the unit cell.
- $f_j$ is the **atomic scattering factor** (or atomic form factor) of atom $j$, defined as the Fourier transform of its electron density $\\rho_j(\\mathbf{r})$:
\\[
f_j(q) = \\int \\rho_j(\\mathbf{r}) e^{i \\mathbf{q} \\cdot \\mathbf{r}} d^3\\mathbf{r}
\\]
At zero scattering angle ($q = 0$), $f_j(0) = Z_j$ (the atomic number, total number of electrons). As $\\theta$ increases, destructive interference between rays scattered from different parts of the electron cloud causes $f_j$ to monotonically decrease.

The diffracted intensity $I_{hkl}$ is proportional to the modulus squared:
\\[
I_{hkl} \\propto |F_{hkl}|^2 = \\left( \\sum_{j} f_j \\cos\\phi_j \\right)^2 + \\left( \\sum_{j} f_j \\sin\\phi_j \\right)^2
\\]
where $\\phi_j = 2\\pi (hx_j + ky_j + lz_j)$.

### Systematic Absences (Extinctions) from Lattice Centering
Non-primitive Bravais lattices possess translational centering operators that cause destructive interference for entire classes of reflections:

1. **Body-Centered (I-Centering)**:
   - Coordinates: $(0,0,0)$ and $\\left(\\frac{1}{2}, \\frac{1}{2}, \\frac{1}{2}\\right)$.
   - Structure factor:
   \\[
   F_{hkl} = f \\left[ 1 + e^{\\pi i (h + k + l)} \\right] = f \\left[ 1 + (-1)^{h+k+l} \\right]
   \\]
   - **Selection Rule**: Reflections are observed **only when $h + k + l = \\text{even}$**. If $h + k + l = \\text{odd}$, $F_{hkl} = 0$ (extinction).

2. **Face-Centered (F-Centering)**:
   - Coordinates: $(0,0,0)$, $\\left(\\frac{1}{2}, \\frac{1}{2}, 0\\right)$, $\\left(\\frac{1}{2}, 0, \\frac{1}{2}\\right)$, $\\left(0, \\frac{1}{2}, \\frac{1}{2}\\right)$.
   - Structure factor:
   \\[
   F_{hkl} = f \\left[ 1 + e^{\\pi i (h+k)} + e^{\\pi i (h+l)} + e^{\\pi i (k+l)} \\right] = f \\left[ 1 + (-1)^{h+k} + (-1)^{h+l} + (-1)^{k+l} \\right]
   \\]
   - If $h, k, l$ are **unmixed** (all even or all odd): $(-1)^{h+k} = 1$, so $F_{hkl} = 4f$.
   - If $h, k, l$ are **mixed** (some even, some odd): $F_{hkl} = 0$.
   - **Selection Rule**: Reflections are observed **only when $h, k, l$ are all even or all odd**.

3. **Base-Centered (C-Centering)**:
   - Coordinates: $(0,0,0)$ and $\\left(\\frac{1}{2}, \\frac{1}{2}, 0\\right)$.
   - **Selection Rule**: Observed **only when $h + k = \\text{even}$**.

### Extinctions from Translational Symmetry Elements
- **Glide Planes**: Cause systematic absences in 2D zonal reflections (e.g., an $a$-glide perpendicular to $c$ requires $h = \\text{even}$ for $(hk0)$ reflections).
- **Screw Axes**: Cause systematic absences in 1D axial reflections (e.g., a $2_1$ screw axis along $c$ requires $l = \\text{even}$ for $(00l)$ reflections)."""
            },
            {
                "secNumber": "4.7",
                "title": "Experimental Diffraction Techniques: Powder XRD & Rotating Crystal Method",
                "content": r"""The practical determination of crystal structures, lattice parameters, and phase purity relies on specialized experimental geometries designed to bring reciprocal lattice points into contact with the Ewald sphere.

### The Debye-Scherrer Powder Method
In powder X-ray diffraction (PXRD), the sample is finely ground into millions of randomly oriented crystallites ($1 - 10\\text{ }\\mu\\text{m}$).
- **Diffraction Geometry**: Because all spatial orientations are statistically populated, every reciprocal lattice vector $\\mathbf{G}_{hkl}$ sweeps out a continuous sphere in reciprocal space.
- The intersection of this reciprocal sphere with the Ewald sphere generates a cone of diffracted rays with semi-apex angle $2\\theta_{hkl}$ coaxial with the incident beam.
- These cones intersect a planar detector or cylindrical film as concentric circular rings (**Debye-Scherrer rings**).
- In a modern Bragg-Brentano diffractometer ($\\theta - 2\\theta$ geometry), a scintillation or silicon strip detector rotates along a goniometer circle, recording diffracted intensity as a function of scattering angle $2\\theta$.

### The Rotating Single-Crystal Method
To solve unknown crystal structures without high-resolution single-crystal area detectors, the rotating crystal method (or Weissenberg/precession technique) aligns a single crystal along a known crystallographic axis (e.g., $\\mathbf{c}$):
- The crystal is rotated around $\\mathbf{c}$ inside a monochromatic X-ray beam.
- The reciprocal lattice consists of planar layers perpendicular to the rotation axis spaced by $c^* = 1/c$.
- As the crystal rotates, reciprocal lattice points within each layer intersect the Ewald sphere, producing horizontal parallel rows of spots on a cylindrical film called **layer lines**.
- The spacing between layer lines directly gives the lattice parameter along the rotation axis:
\\[
c = \\frac{n\\lambda}{\\sin \\mu_n}
\\]
where $\\mu_n$ is the angle subtended by the $n$-th layer line from the equatorial line ($n=0$).

### Peak Broadening & The Scherrer Formula
In real nanomaterials, diffraction peaks possess finite angular widths $\\beta$ (full width at half maximum, FWHM) due to crystallite size and lattice strain:
\\[
\\beta(2\\theta) = \\frac{K\\lambda}{L\\cos\\theta} + 4\\varepsilon\\tan\\theta
\\]
where $K \\approx 0.9$ is the Scherrer shape factor, $L$ is the volume-weighted mean crystallite column length, and $\\varepsilon = \\Delta d/d$ is root-mean-square microstrain. Plotting $\\beta\\cos\\theta$ versus $\\sin\\theta$ (**Williamson-Hall plot**) separates the size contribution (intercept) from microstrain (slope)."""
            },
            {
                "secNumber": "4.8",
                "title": "Electron Diffraction & Neutron Diffraction: Principles & Cross-Sections",
                "content": r"""While X-rays scatter from atomic electron clouds, structural chemistry utilizes two complementary quantum probes: **electrons** and **neutrons**.

### Comparison of Quantum Scattering Probes

| Characteristic | X-Ray Diffraction (XRD) | Electron Diffraction (ED/TEM) | Neutron Diffraction (ND) |
| :--- | :--- | :--- | :--- |
| **Primary Interaction** | Electromagnetic with electron cloud $\\rho(\\mathbf{r})$ | Coulombic with electrostatic potential $\\phi(\\mathbf{r})$ | Strong nuclear force with atomic nuclei |
| **Scattering Cross-Section** | $\\sim 10^{-24}\\text{ cm}^2$ (Moderate) | $\\sim 10^{-20}\\text{ cm}^2$ ($10^4 - 10^5\\times$ larger) | $\\sim 10^{-24}\\text{ cm}^2$ (Moderate/Weak) |
| **Penetration Depth** | $10 - 100\\text{ }\\mu\\text{m}$ (Bulk) | $10 - 100\\text{ nm}$ (Thin specimens only) | Several $\\text{cm}$ (Deep bulk probe) |
| **Sensitivity to Light Elements** | Proportional to $Z^2$; insensitive to $\\text{H}, \\text{Li}$ | Good sensitivity to light atoms | High sensitivity (nuclear scattering length $b$) |
| **Isotopic Sensitivity** | None ($Z$ identical) | None | Exceptional (e.g., $^1\\text{H}$ vs $^2\\text{D}$) |
| **Magnetic Moment** | Negligible magnetic scattering | Negligible | Large ($\\mu_n = -1.913\\mu_N$); maps spin order |

### Electron Diffraction in Transmission Electron Microscopy (TEM)
High-energy electrons ($100 - 300\\text{ keV}$) possess extremely short de Broglie wavelengths:
\\[
\\lambda = \\frac{h}{\\sqrt{2m_e e V \\left(1 + \\frac{e V}{2 m_e c^2}\\right)}}
\\]
For $200\\text{ kV}$ electrons, relativistic correction yields $\\lambda = 0.0251\\text{ Å}$.
Because $\\lambda$ is two orders of magnitude smaller than X-ray wavelengths, the Ewald sphere radius $R = 1/\\lambda \\approx 40\\text{ Å}^{-1}$ is virtually planar on the scale of the reciprocal lattice. Consequently, an entire 2D plane of the reciprocal lattice intersects the Ewald sphere simultaneously, yielding instantaneous 2D spot patterns (Selected Area Electron Diffraction, SAED).

### Neutron Diffraction & Magnetic Crystallography
Neutrons produced in spallation sources or nuclear reactors are thermalized to room temperature ($E \\approx 25\\text{ meV}$), giving de Broglie wavelengths $\\lambda \\approx 1.8\\text{ Å}$, ideal for crystal diffraction:
\\[
\\lambda = \\frac{h}{\\sqrt{2m_n E_k}}
\\]
Because neutrons interact via the strong nuclear force, the nuclear scattering length $b$ varies erratically across the periodic table and between isotopes (e.g., $b(^1\\text{H}) = -3.74\\text{ fm}$ vs $b(^2\\text{D}) = +6.67\\text{ fm}$), allowing precise localization of hydrogen in proteins and hydrates via deuteration.
Furthermore, the neutron carries an intrinsic magnetic dipole moment $\\mu_n = -1.913\\mu_N$. The magnetic interaction with unpaired electron spins enables direct determination of antiferromagnetic, ferrimagnetic, and helical spin structures (e.g., the historical discovery of antiferromagnetism in $\\text{MnO}$ by Clifford Shull, 1949)."""
            }
        ],
        "problems": [
            {
                "probNumber": "4.1",
                "title": "Derivation of Interplanar Spacing d_hkl in Orthorhombic and Tetragonal Systems",
                "difficulty": "Foundational",
                "statement": "An orthorhombic crystalline material has unit cell parameters $a = 4.524\\text{ Å}$, $b = 5.612\\text{ Å}$, and $c = 7.185\\text{ Å}$.\\n(a) Derive the general expression for $d_{hkl}$ from vector dot products of reciprocal lattice vectors.\\n(b) Calculate the interplanar spacings for the $(111)$, $(020)$, and $(211)$ crystallographic planes.\\n(c) For a tetragonal crystal with $a = b = 4.524\\text{ Å}$ and $c = 7.185\\text{ Å}$, compute the percentage shift in $d_{111}$ relative to the orthorhombic value.",
                "solution": r"""### Step 1: Vector Derivation of $d_{hkl}$
The reciprocal lattice vector $\\mathbf{G}_{hkl}$ normal to $(hkl)$ is:
\\[
\\mathbf{G}_{hkl} = h\\mathbf{a}^* + k\\mathbf{b}^* + l\\mathbf{c}^*
\\]
For an orthorhombic system, $\\mathbf{a}, \\mathbf{b}, \\mathbf{c}$ are mutually orthogonal, so $\\mathbf{a}^*, \\mathbf{b}^*, \\mathbf{c}^*$ are also mutually orthogonal with magnitudes $|\mathbf{a}^*| = 1/a, |\mathbf{b}^*| = 1/b, |\mathbf{c}^*| = 1/c$.
The norm squared of $\\mathbf{G}_{hkl}$ is:
\\[
|\\mathbf{G}_{hkl}|^2 = \\mathbf{G}_{hkl} \\cdot \\mathbf{G}_{hkl} = h^2|\\mathbf{a}^*|^2 + k^2|\\mathbf{b}^*|^2 + l^2|\\mathbf{c}^*|^2 = \\frac{h^2}{a^2} + \\frac{k^2}{b^2} + \\frac{l^2}{c^2}
\\]
Since $d_{hkl} = 1/|\\mathbf{G}_{hkl}|$, we have:
\\[
\\frac{1}{d_{hkl}^2} = \\frac{h^2}{a^2} + \\frac{k^2}{b^2} + \\frac{l^2}{c^2} \\implies d_{hkl} = \\left( \\frac{h^2}{a^2} + \\frac{k^2}{b^2} + \\frac{l^2}{c^2} \\right)^{-1/2}
\\]

### Step 2: Numerical Calculations for Orthorhombic System
Given $a = 4.524\\text{ Å}$, $b = 5.612\\text{ Å}$, $c = 7.185\\text{ Å}$:
- $1/a^2 = 1/(4.524)^2 = 0.04886\\text{ Å}^{-2}$
- $1/b^2 = 1/(5.612)^2 = 0.03175\\text{ Å}^{-2}$
- $1/c^2 = 1/(7.185)^2 = 0.01937\\text{ Å}^{-2}$

1. **For Plane $(111)$**:
\\[
\\frac{1}{d_{111}^2} = 0.04886(1)^2 + 0.03175(1)^2 + 0.01937(1)^2 = 0.09998\\text{ Å}^{-2}
\\]
\\[
d_{111} = \\frac{1}{\\sqrt{0.09998}} = 3.162\\text{ Å}
\\]

2. **For Plane $(020)$**:
\\[
\\frac{1}{d_{020}^2} = 0 + 0.03175(2)^2 + 0 = 0.12700\\text{ Å}^{-2}
\\]
\\[
d_{020} = \\frac{1}{\\sqrt{0.12700}} = \\frac{b}{2} = \\frac{5.612}{2} = 2.806\\text{ Å}
\\]

3. **For Plane $(211)$**:
\\[
\\frac{1}{d_{211}^2} = 0.04886(2)^2 + 0.03175(1)^2 + 0.01937(1)^2 = 0.19544 + 0.03175 + 0.01937 = 0.24656\\text{ Å}^{-2}
\\]
\\[
d_{211} = \\frac{1}{\\sqrt{0.24656}} = 2.014\\text{ Å}
\\]

### Step 3: Tetragonal Comparison
For the tetragonal cell with $a = b = 4.524\\text{ Å}$ and $c = 7.185\\text{ Å}$:
\\[
\\frac{1}{d_{111}^2} = \\frac{1^2 + 1^2}{(4.524)^2} + \\frac{1^2}{(7.185)^2} = 2(0.04886) + 0.01937 = 0.09772 + 0.01937 = 0.11709\\text{ Å}^{-2}
\\]
\\[
d_{111,\\text{tetra}} = \\frac{1}{\\sqrt{0.11709}} = 2.922\\text{ Å}
\\]
Percentage shift:
\\[
\\Delta d = \\frac{2.922 - 3.162}{3.162} \\times 100\\% = -7.59\\%
\\]"""
            },
            {
                "probNumber": "4.2",
                "title": "Reciprocal Lattice Vector Norm and Angle in Monoclinic Systems",
                "difficulty": "Intermediate",
                "statement": "A monoclinic crystal has direct lattice constants $a = 6.20\\text{ Å}$, $b = 4.80\\text{ Å}$, $c = 8.50\\text{ Å}$, and obtuse monoclinic angle $\\beta = 105.0^\\circ$ (with $\\alpha = \\gamma = 90.0^\\circ$).\\n(a) Calculate the unit cell volume $V_c$.\\n(b) Compute the reciprocal lattice parameters $a^*, b^*, c^*$ and reciprocal angle $\\beta^*$.\\n(c) Calculate the interplanar spacing $d_{101}$ and the angle between reciprocal vectors $\\mathbf{G}_{100}$ and $\\mathbf{G}_{001}$.",
                "solution": r"""### Step 1: Unit Cell Volume
For a monoclinic cell where $\\alpha = \\gamma = 90^\\circ$:
\\[
V_c = abc\\sin\\beta = (6.20)(4.80)(8.50)\\sin(105.0^\\circ)
\\]
Since $\\sin(105^\\circ) = 0.96593$:
\\[
V_c = 252.96 \\times 0.96593 = 244.34\\text{ Å}^3
\\]

### Step 2: Reciprocal Lattice Constants
Using the geometric definitions of reciprocal basis vectors:
\\[
a^* = \\frac{bc\\sin\\alpha}{V_c} = \\frac{bc}{abc\\sin\\beta} = \\frac{1}{a\\sin\\beta} = \\frac{1}{6.20 \\times 0.96593} = \\frac{1}{5.9888} = 0.16698\\text{ Å}^{-1}
\\]
\\[
b^* = \\frac{1}{b} = \\frac{1}{4.80} = 0.20833\\text{ Å}^{-1} \\quad (\\text{since } \\mathbf{b} \\perp \\mathbf{a}, \\mathbf{c})
\\]
\\[
c^* = \\frac{1}{c\\sin\\beta} = \\frac{1}{8.50 \\times 0.96593} = \\frac{1}{8.2104} = 0.12180\\text{ Å}^{-1}
\\]
Reciprocal angle $\\beta^*$:
\\[
\\beta^* = 180^\\circ - \\beta = 180.0^\\circ - 105.0^\\circ = 75.0^\\circ
\\]

### Step 3: Interplanar Spacing $d_{101}$
For $(101)$, $h = 1, k = 0, l = 1$:
The reciprocal vector is $\\mathbf{G}_{101} = \\mathbf{a}^* + \\mathbf{c}^*$.
Its norm squared is:
\\[
|\\mathbf{G}_{101}|^2 = |\\mathbf{a}^*|^2 + |\\mathbf{c}^*|^2 + 2|\\mathbf{a}^*||\\mathbf{c}^*|\\cos\\beta^*
\\]
Substitute the values:
\\[
|\\mathbf{a}^*|^2 = (0.16698)^2 = 0.027883
\\]
\\[
|\\mathbf{c}^*|^2 = (0.12180)^2 = 0.014835
\\]
\\[
2|\\mathbf{a}^*||\\mathbf{c}^*|\\cos(75^\\circ) = 2(0.16698)(0.12180)(0.25882) = 0.010528
\\]
Summing these contributions:
\\[
|\\mathbf{G}_{101}|^2 = 0.027883 + 0.014835 + 0.010528 = 0.053246\\text{ Å}^{-2}
\\]
\\[
d_{101} = \\frac{1}{\\sqrt{|\\mathbf{G}_{101}|^2}} = \\frac{1}{\\sqrt{0.053246}} = 4.334\\text{ Å}
\\]
The angle between $\\mathbf{G}_{100}$ and $\\mathbf{G}_{001}$ is simply $\\beta^* = 75.0^\\circ$."""
            },
            {
                "probNumber": "4.3",
                "title": "Indexing a Cubic Powder XRD Pattern and Lattice Constant Determination",
                "difficulty": "Intermediate",
                "statement": "Powder X-ray diffraction of an unknown transition metal using $\\text{Cu } K_\\alpha$ radiation ($\\lambda = 1.54060\\text{ Å}$) produces diffraction peaks at the following $2\\theta$ angles: $40.26^\\circ, 58.27^\\circ, 73.18^\\circ, 86.94^\\circ, 100.73^\\circ, 115.54^\\circ$.\\n(a) Compute $\\sin^2\\theta$ for all six peaks.\\n(b) Index each peak, establish whether the Bravais lattice is SC, BCC, or FCC, and assign Miller indices $(hkl)$.\\n(c) Calculate the precision lattice parameter $a$ and identify the transition metal from its density given molar mass $M = 95.95\\text{ g/mol}$.",
                "solution": r"""### Step 1: Calculate $\\sin^2\\theta$ Values
For a cubic crystal:
\\[
\\sin^2\\theta = \\frac{\\lambda^2}{4a^2} (h^2 + k^2 + l^2) = A \\cdot s
\\]
where $s = h^2 + k^2 + l^2$ and $A = \\lambda^2/(4a^2)$ is a constant.

| Peak | $2\\theta$ (deg) | $\\theta$ (deg) | $\\sin\\theta$ | $\\sin^2\\theta$ | Ratio to First | Integer $s$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | $40.26$ | $20.13$ | $0.34414$ | $0.11843$ | $1.000$ | $2$ |
| 2 | $58.27$ | $29.135$ | $0.48685$ | $0.23702$ | $2.001$ | $4$ |
| 3 | $73.18$ | $36.59$ | $0.59608$ | $0.35531$ | $3.000$ | $6$ |
| 4 | $86.94$ | $43.47$ | $0.68797$ | $0.47330$ | $3.996$ | $8$ |
| 5 | $100.73$ | $50.365$ | $0.77014$ | $0.59312$ | $5.008$ | $10$ |
| 6 | $115.54$ | $57.77$ | $0.84591$ | $0.71556$ | $6.042$ | $12$ |

### Step 2: Indexing and Lattice Determination
The observed sequence of $s = h^2 + k^2 + l^2$ values is:
\\[
s = 2, 4, 6, 8, 10, 12
\\]
- For **FCC**, selection rule is $h, k, l$ all odd or all even: $s = 3, 4, 8, 11, 12, 16, \\dots$
- For **BCC**, selection rule is $h + k + l = \\text{even}$: $s = 2, 4, 6, 8, 10, 12, 14, \\dots$
The sequence $2, 4, 6, 8, 10, 12$ matches **Body-Centered Cubic (BCC)** exactly!
The assigned $(hkl)$ reflections are:
- $s = 2$: $(110)$
- $s = 4$: $(200)$
- $s = 6$: $(211)$
- $s = 8$: $(220)$
- $s = 10$: $(310)$
- $s = 12$: $(222)$

### Step 3: Lattice Parameter and Metal Identification
From the common multiplier $A = \\sin^2\\theta / s$:
\\[
A_{\\text{avg}} = \\frac{0.11843/2 + 0.23702/4 + 0.35531/6 + 0.47330/8 + 0.59312/10 + 0.71556/12}{6} = 0.05923\\text{ Å}^{-2}
\\]
Since $A = \\frac{\\lambda^2}{4a^2}$:
\\[
a = \\frac{\\lambda}{2\\sqrt{A}} = \\frac{1.54060\\text{ Å}}{2\\sqrt{0.05923}} = \\frac{1.54060}{2(0.24337)} = 3.165\\text{ Å}
\\]
For BCC, $Z = 2$ atoms per unit cell. Density $\\rho$:
\\[
\\rho = \\frac{Z M}{N_A a^3} = \\frac{2 \\times 95.95\\text{ g/mol}}{(6.02214 \\times 10^{23}\\text{ mol}^{-1})(3.165 \\times 10^{-8}\\text{ cm})^3} = \\frac{191.90}{6.02214 \\times 10^{23} \\times 3.1704 \\times 10^{-23}} = 10.05\\text{ g/cm}^3
\\]
With $M = 95.95\\text{ g/mol}$, BCC crystal structure, and $a = 3.165\\text{ Å}$, the material is **Molybdenum (Mo)** (literature: BCC, $a = 3.147\\text{ Å}$, $\\rho = 10.28\\text{ g/cm}^3$)."""
            },
            {
                "probNumber": "4.4",
                "title": "Systematic Absence Analysis and Structure Factor Calculation for Face-Centered Cubic (FCC)",
                "difficulty": "Intermediate",
                "statement": "Consider a monoatomic face-centered cubic (FCC) crystal with atomic scattering factor $f$.\\n(a) Write the fractional coordinates of the four lattice sites and derive the algebraic structure factor $F_{hkl}$.\\n(b) Prove analytically that $F_{hkl} = 0$ when the indices $h, k, l$ have mixed parity (some odd and some even).\\n(c) For copper ($Z = 29$, FCC, $a = 3.615\\text{ Å}$), evaluate the ratio of diffracted intensities $I_{200}/I_{111}$ assuming atomic scattering factors $f(111) = 22.1$ and $f(200) = 20.4$ with Lorentz-polarization factor $\\text{LP}(\\theta) = \\frac{1 + \\cos^2 2\\theta}{\\sin^2\\theta \\cos\\theta}$ and multiplicity factors $p_{111} = 8, p_{200} = 6$ using $\\lambda = 1.5406\\text{ Å}$.",
                "solution": r"""### Step 1: Structure Factor Derivation
The four basis positions of an FCC unit cell are:
\\[
\\mathbf{r}_1 = (0,0,0), \\quad \\mathbf{r}_2 = \\left(\\frac{1}{2},\\frac{1}{2},0\\right), \\quad \\mathbf{r}_3 = \\left(\\frac{1}{2},0,\\frac{1}{2}\\right), \\quad \\mathbf{r}_4 = \\left(0,\\frac{1}{2},\\frac{1}{2}\\right)
\\]
The structure factor is:
\\[
F_{hkl} = \\sum_{j=1}^{4} f \\exp[2\\pi i (h x_j + k y_j + l z_j)]
\\]
\\[
F_{hkl} = f \\left( 1 + e^{\\pi i (h+k)} + e^{\\pi i (h+l)} + e^{\\pi i (k+l)} \\right)
\\]
Since $e^{\\pi i n} = (-1)^n$:
\\[
F_{hkl} = f \\left( 1 + (-1)^{h+k} + (-1)^{h+l} + (-1)^{k+l} \\right)
\\]

### Step 2: Parity Analysis
**Case 1: $h, k, l$ are all unmixed**
- *Subcase 1a (All Even)*: $h, k, l$ are all even $\\implies h+k, h+l, k+l$ are all even $\\implies (-1)^{\\text{even}} = 1$.
  \\[
  F_{hkl} = f(1 + 1 + 1 + 1) = 4f
  \\]
- *Subcase 1b (All Odd)*: $h, k, l$ are all odd $\\implies$ sum of any two odd numbers is even $\\implies h+k, h+l, k+l$ are all even $\\implies (-1)^{\\text{even}} = 1$.
  \\[
  F_{hkl} = f(1 + 1 + 1 + 1) = 4f
  \\]

**Case 2: $h, k, l$ are mixed**
- *Subcase 2a (Two Even, One Odd)*: Let $h, k$ be even, $l$ be odd.
  $h+k = \\text{even} \\implies (-1)^{h+k} = +1$.
  $h+l = \\text{odd} \\implies (-1)^{h+l} = -1$.
  $k+l = \\text{odd} \\implies (-1)^{k+l} = -1$.
  \\[
  F_{hkl} = f(1 + 1 - 1 - 1) = 0
  \\]
- *Subcase 2b (Two Odd, One Even)*: Let $h, k$ be odd, $l$ be even.
  $h+k = \\text{even} \\implies (-1)^{h+k} = +1$.
  $h+l = \\text{odd} \\implies (-1)^{h+l} = -1$.
  $k+l = \\text{odd} \\implies (-1)^{k+l} = -1$.
  \\[
  F_{hkl} = f(1 + 1 - 1 - 1) = 0
  \\]
Thus, for all mixed reflections, destructive interference is complete ($F_{hkl} = 0$).

### Step 3: Intensity Ratio $I_{200}/I_{111}$
Diffracted intensity in powder XRD is:
\\[
I_{hkl} \\propto |F_{hkl}|^2 \\cdot p_{hkl} \\cdot \\text{LP}(\\theta)
\\]
1. **For $(111)$**:
\\[
d_{111} = \\frac{a}{\\sqrt{3}} = \\frac{3.615}{\\sqrt{3}} = 2.0871\\text{ Å}
\\]
\\[
\\sin\\theta_{111} = \\frac{\\lambda}{2d_{111}} = \\frac{1.5406}{2(2.0871)} = 0.36908 \\implies \\theta_{111} = 21.66^\\circ, \\quad 2\\theta = 43.32^\\circ
\\]
\\[
\\text{LP}(111) = \\frac{1 + \\cos^2(43.32^\\circ)}{\\sin^2(21.66^\\circ)\\cos(21.66^\\circ)} = \\frac{1 + (0.7275)^2}{(0.3691)^2(0.9294)} = \\frac{1.5293}{0.1266} = 12.08
\\]
\\[
|F_{111}|^2 = (4 \\times 22.1)^2 = (88.4)^2 = 7814.6
\\]
\\[
I_{111} \\propto 7814.6 \\times 8 \\times 12.08 = 755,\\!200
\\]

2. **For $(200)$**:
\\[
d_{200} = \\frac{a}{2} = \\frac{3.615}{2} = 1.8075\\text{ Å}
\\]
\\[
\\sin\\theta_{200} = \\frac{1.5406}{2(1.8075)} = 0.42617 \\implies \\theta_{200} = 25.22^\\circ, \\quad 2\\theta = 50.44^\\circ
\\]
\\[
\\text{LP}(200) = \\frac{1 + \\cos^2(50.44^\\circ)}{\\sin^2(25.22^\\circ)\\cos(25.22^\\circ)} = \\frac{1 + (0.6369)^2}{(0.4262)^2(0.9047)} = \\frac{1.4056}{0.1643} = 8.555
\\]
\\[
|F_{200}|^2 = (4 \\times 20.4)^2 = (81.6)^2 = 6658.6
\\]
\\[
I_{200} \\propto 6658.6 \\times 6 \\times 8.555 = 341,\\!780
\\]

3. **Ratio**:
\\[
\\frac{I_{200}}{I_{111}} = \\frac{341,\\!780}{755,\\!200} = 0.453 \\quad (45.3\\%)
\\]"""
            },
            {
                "probNumber": "4.5",
                "title": "Structure Factor of Diamond-Cubic Lattice and Forbidden Reflections",
                "difficulty": "Advanced",
                "statement": "The diamond cubic crystal structure consists of an FCC lattice with a two-atom basis located at $(0,0,0)$ and $\\left(\\frac{1}{4}, \\frac{1}{4}, \\frac{1}{4}\\right)$, containing $8$ identical carbon atoms per unit cell.\\n(a) Express $F_{hkl}$ as the product of the FCC lattice sum and the two-atom basis factor.\\n(b) Prove that reflections with $h, k, l$ all even are divided into two classes: observed when $h + k + l = 4n$, and forbidden when $h + k + l = 4n + 2$.\\n(c) Determine whether the following reflections are allowed or forbidden: $(111)$, $(200)$, $(220)$, $(311)$, $(222)$, $(400)$.",
                "solution": r"""### Step 1: Factorization of Structure Factor
The diamond structure can be viewed as an FCC Bravais lattice with an identical copy displaced along the body diagonal by vector $\\boldsymbol{\\tau} = \\frac{1}{4}\\mathbf{a} + \\frac{1}{4}\\mathbf{b} + \\frac{1}{4}\\mathbf{c}$.
The position of any atom can be written as $\\mathbf{R}_{\\text{FCC}} + \\mathbf{d}_p$, where $\\mathbf{d}_1 = (0,0,0)$ and $\\mathbf{d}_2 = \\left(\\frac{1}{4},\\frac{1}{4},\\frac{1}{4}\\right)$.
Therefore, the structure factor factors into:
\\[
F_{hkl} = F_{\\text{FCC}} \\cdot F_{\\text{basis}}
\\]
where:
\\[
F_{\\text{FCC}} = f \\left( 1 + e^{\\pi i (h+k)} + e^{\\pi i (h+l)} + e^{\\pi i (k+l)} \\right)
\\]
\\[
F_{\\text{basis}} = 1 + \\exp\\left[ 2\\pi i \\left( \\frac{h}{4} + \\frac{k}{4} + \\frac{l}{4} \\right) \\right] = 1 + e^{i \\frac{\\pi}{2}(h+k+l)}
\\]
From FCC centering, $F_{\\text{FCC}} = 0$ if $h, k, l$ are mixed. Thus, all mixed reflections are automatically forbidden.

### Step 2: Evaluation of Allowed FCC Reflections
For unmixed reflections, $F_{\\text{FCC}} = 4f$.
The total structure factor is:
\\[
F_{hkl} = 4f \\left[ 1 + e^{i \\frac{\\pi}{2}(h+k+l)} \\right]
\\]

**Case A: $h, k, l$ are all odd**
Let $h + k + l = 2m + 1$ (sum of three odd integers is always odd):
- If $h + k + l = 4n + 1$: $e^{i \\frac{\\pi}{2}(4n+1)} = e^{i \\pi/2} = i$.
  $F_{hkl} = 4f(1 + i) \\implies |F_{hkl}|^2 = 16f^2 |1+i|^2 = 32 f^2$.
- If $h + k + l = 4n + 3$: $e^{i \\frac{\\pi}{2}(4n+3)} = e^{i 3\\pi/2} = -i$.
  $F_{hkl} = 4f(1 - i) \\implies |F_{hkl}|^2 = 16f^2 |1-i|^2 = 32 f^2$.
**Result**: All odd reflections are **allowed** with $|F_{hkl}| = 4\\sqrt{2}f$.

**Case B: $h, k, l$ are all even**
Let $h + k + l = 2m$ (sum of three even integers is always even):
- If $h + k + l = 4n$:
  $e^{i \\frac{\\pi}{2}(4n)} = e^{i 2\\pi n} = 1$.
  $F_{hkl} = 4f(1 + 1) = 8f \\implies |F_{hkl}|^2 = 64f^2$.
  **Result**: Fully **allowed** (strong reflection).
- If $h + k + l = 4n + 2$:
  $e^{i \\frac{\\pi}{2}(4n+2)} = e^{i (2\\pi n + \\pi)} = -1$.
  $F_{hkl} = 4f(1 - 1) = 0$.
  **Result**: Completely **forbidden** (systematic extinction due to the glide component of the diamond space group $Fd\\bar{3}m$).

### Step 3: Analysis of Specified Reflections
1. **$(111)$**: All odd $\\implies h+k+l = 3 = 4(0)+3$. **Allowed** ($|F|^2 = 32f^2$).
2. **$(200)$**: All even, $h+k+l = 2 = 4(0)+2$. **Forbidden** ($F = 0$).
3. **$(220)$**: All even, $h+k+l = 4 = 4(1)$. **Allowed** ($|F|^2 = 64f^2$).
4. **$(311)$**: All odd $\\implies h+k+l = 5 = 4(1)+1$. **Allowed** ($|F|^2 = 32f^2$).
5. **$(222)$**: All even, $h+k+l = 6 = 4(1)+2$. **Forbidden** ($F = 0$).
6. **$(400)$**: All even, $h+k+l = 4 = 4(1)$. **Allowed** ($|F|^2 = 64f^2$)."""
            },
            {
                "probNumber": "4.6",
                "title": "Rotating Crystal Method: Layer Line Spacing and Axial Dimension Calculation",
                "difficulty": "Intermediate",
                "statement": "A single crystal of an unknown orthorhombic compound is mounted on a rotation camera with cylindrical film radius $R = 57.30\\text{ mm}$ and rotated about its $c$-axis. Monochromatic X-rays with $\\lambda = 1.5418\\text{ Å}$ irradiate the crystal perpendicular to the rotation axis.\\n(a) Derive the relationship between the vertical distance $y_n$ of the $n$-th layer line from the central equatorial line ($n=0$) and the lattice parameter $c$.\\n(b) If the distance between the $n = +1$ and $n = -1$ layer lines on the film is measured to be $28.65\\text{ mm}$, calculate the vertical height $y_1$ and subtended angle $\\mu_1$.\\n(c) Determine the lattice parameter $c$ of the crystal.",
                "solution": r"""### Step 1: Geometry of the Cylindrical Rotating Crystal Camera
Let the crystal be aligned with its $\\mathbf{c}$ axis vertical. The incident beam is horizontal.
Constructive interference in the vertical direction requires the third Laue equation to be satisfied:
\\[
\\mathbf{c} \\cdot (\\hat{\\mathbf{s}} - \\hat{\\mathbf{s}}_0) = n\\lambda
\\]
Since $\\hat{\\mathbf{s}}_0$ is perpendicular to $\\mathbf{c}$ (horizontal), $\\mathbf{c} \\cdot \\hat{\\mathbf{s}}_0 = 0$.
If $\\mu_n$ is the elevation angle of the diffracted cone above the horizontal plane, then $\\mathbf{c} \\cdot \\hat{\\mathbf{s}} = c\\sin\\mu_n$.
Therefore:
\\[
c\\sin\\mu_n = n\\lambda \\implies c = \\frac{n\\lambda}{\\sin\\mu_n}
\\]
On a cylindrical film of radius $R$, the diffracted cone forms a horizontal circular line at height $y_n$ above the equatorial plane:
\\[
\\tan\\mu_n = \\frac{y_n}{R} \\implies \\mu_n = \\arctan\\left(\\frac{y_n}{R}\\right)
\\]

### Step 2: Layer Line Distance and Subtended Angle
The distance between the $+1$ and $-1$ layer lines is $\\Delta y = 2y_1 = 28.65\\text{ mm}$.
Therefore, the height of the first layer line is:
\\[
y_1 = \\frac{28.65\\text{ mm}}{2} = 14.325\\text{ mm}
\\]
Given the camera radius $R = 57.30\\text{ mm}$:
\\[
\\tan\\mu_1 = \\frac{y_1}{R} = \\frac{14.325\\text{ mm}}{57.30\\text{ mm}} = 0.25000
\\]
Evaluating the angle:
\\[
\\mu_1 = \\arctan(0.25000) = 14.036^\\circ
\\]
The sine of this angle:
\\[
\\sin\\mu_1 = \\sin(14.036^\\circ) = 0.24254
\\]

### Step 3: Lattice Parameter Calculation
Using the diffraction formula for $n = 1$ with $\\lambda = 1.5418\\text{ Å}$:
\\[
c = \\frac{1 \\times \\lambda}{\\sin\\mu_1} = \\frac{1.5418\\text{ Å}}{0.24254} = 6.357\\text{ Å}
\\]
Thus, the lattice constant along the rotation axis is $c = 6.36\\text{ Å}$."""
            },
            {
                "probNumber": "4.7",
                "title": "Electron de Broglie Wavelength and Relativistic High-Energy Electron Diffraction",
                "difficulty": "Intermediate",
                "statement": "In a Transmission Electron Microscope (TEM), an accelerating voltage of $V = 200.0\\text{ kV}$ is applied to illuminate a thin gold foil (FCC, $a = 4.078\\text{ Å}$).\\n(a) Calculate the non-relativistic de Broglie wavelength of the electrons.\\n(b) Formulate the relativistic energy-momentum relation and compute the exact relativistic electron wavelength $\\lambda_{\\text{rel}}$.\\n(c) For the $(200)$ reflection of gold, calculate the Bragg diffraction angle $\\theta$ and verify why the Ewald sphere can be treated as virtually planar.",
                "solution": r"""### Step 1: Non-Relativistic Wavelength
The kinetic energy is $E_k = e V = 200.0\\text{ keV} = 200.0 \\times 10^3 \\times 1.60218 \\times 10^{-19}\\text{ J} = 3.20436 \\times 10^{-14}\\text{ J}$.
In the non-relativistic regime:
\\[
p = \\sqrt{2 m_e E_k} = \\sqrt{2(9.10938 \\times 10^{-31}\\text{ kg})(3.20436 \\times 10^{-14}\\text{ J})} = 7.6405 \\times 10^{-22}\\text{ kg}\\cdot\\text{m/s}
\\]
\\[
\\lambda_{\\text{non-rel}} = \\frac{h}{p} = \\frac{6.62607 \\times 10^{-34}\\text{ J}\\cdot\\text{s}}{7.6405 \\times 10^{-22}\\text{ kg}\\cdot\\text{m/s}} = 8.672 \\times 10^{-13}\\text{ m} = 0.008672\\text{ nm} = 0.08672\\text{ Å}
\\]

### Step 2: Relativistic Correction
The rest mass energy of an electron is $m_e c^2 = 510.999\\text{ keV}$.
The relativistic momentum is given by:
\\[
(p c)^2 = E^2 - (m_e c^2)^2 = (E_k + m_e c^2)^2 - (m_e c^2)^2 = E_k(E_k + 2m_e c^2)
\\]
\\[
p = \\frac{1}{c}\\sqrt{e V (e V + 2 m_e c^2)} = \\frac{\\sqrt{2 m_e e V \\left(1 + \\frac{e V}{2 m_e c^2}\\right)}}{1}
\\]
The relativistic wavelength is:
\\[
\\lambda_{\\text{rel}} = \\frac{h}{p} = \\frac{h}{\\sqrt{2 m_e e V \\left(1 + \\frac{e V}{2 m_e c^2}\\right)}}
\\]
Calculate the relativistic factor:
\\[
1 + \\frac{e V}{2 m_e c^2} = 1 + \\frac{200.0\\text{ keV}}{2(510.999\\text{ keV})} = 1 + 0.19570 = 1.19570
\\]
\\[
\\sqrt{1.19570} = 1.09348
\\]
Therefore:
\\[
\\lambda_{\\text{rel}} = \\frac{\\lambda_{\\text{non-rel}}}{1.09348} = \\frac{0.086723\\text{ Å}}{1.09348} = 0.07931\\text{ Å} \\quad (\\text{or } 0.002508\\text{ nm} = 0.02508\\text{ Å} \\text{ for relativistic TEM momentum})
\\]
*Precision relativistic calculation*:
\\[
p c = \\sqrt{200.0 \\times (200.0 + 1022.0)} = \\sqrt{200.0 \\times 1222.0} = \\sqrt{244400} = 494.368\\text{ keV}
\\]
\\[
\\lambda = \\frac{h c}{p c} = \\frac{12398.42\\text{ eV}\\cdot\\text{Å}}{494368\\text{ eV}} = 0.025079\\text{ Å} = 2.508\\text{ pm}
\\]

### Step 3: Bragg Angle and Ewald Sphere Curvature
For gold (FCC, $a = 4.078\\text{ Å}$):
\\[
d_{200} = \\frac{a}{2} = \\frac{4.078\\text{ Å}}{2} = 2.039\\text{ Å}
\\]
Using Bragg's Law:
\\[
\\sin\\theta = \\frac{\\lambda}{2d_{200}} = \\frac{0.02508\\text{ Å}}{2(2.039\\text{ Å})} = 0.006150
\\]
Since $\\sin\\theta \\ll 1$, $\\theta \\approx 0.006150\\text{ rad} = 0.352^\\circ$.
The scattering angle $2\\theta = 0.704^\\circ = 12.3\\text{ mrad}$.
The radius of the Ewald sphere is:
\\[
R = \\frac{1}{\\lambda} = \\frac{1}{0.02508\\text{ Å}} = 39.87\\text{ Å}^{-1}
\\]
Because $R \\approx 40\\text{ Å}^{-1}$ is huge compared to reciprocal lattice spacings ($|\\mathbf{G}_{200}| = 1/d_{200} = 0.49\\text{ Å}^{-1}$), the surface curvature across the zero-order Laue zone is negligible ($< 0.3\\%$) over several reciprocal lattice points. This allows simultaneous excitation of dozens of reciprocal lattice spots in a single 2D TEM diffraction pattern."""
            },
            {
                "probNumber": "4.8",
                "title": "Thermal Neutron Diffraction: Wavelength Calculation, Nuclear Scattering and Magnetic Form Factors",
                "difficulty": "Advanced",
                "statement": "A thermal neutron beam extracted from a reactor moderator at $T = 300.0\\text{ K}$ is used to study antiferromagnetic manganese oxide ($\\text{MnO}$, rock salt structure with $a = 4.445\\text{ Å}$).\\n(a) Calculate the root-mean-square kinetic energy $E_k$ and de Broglie wavelength $\\lambda_n$ of the thermal neutrons ($m_n = 1.67493 \\times 10^{-27}\\text{ kg}$).\\n(b) Explain why neutron nuclear scattering factors $b$ do not depend on scattering angle $\\theta$, while magnetic form factors $f_{\\text{mag}}(\\theta)$ decrease rapidly with $\\theta$.\\n(c) In paramagnetic $\\text{MnO}$ ($T > 120\\text{ K}$), the first reflection is $(111)$ at $d = 2.566\\text{ Å}$. When cooled below the Néel temperature ($T_N = 118\\text{ K}$), antiferromagnetic ordering doubles the magnetic unit cell along all three axes ($a_{\\text{mag}} = 2a$). Compute the interplanar spacing and diffraction angle $2\\theta$ for the new magnetic superlattice peak $(111)_{\\text{mag}}$ using $\\lambda = 1.540\\text{ Å}$.",
                "solution": r"""### Step 1: Thermal Neutron de Broglie Wavelength
The mean kinetic energy of thermalized neutrons at $T = 300\\text{ K}$ is:
\\[
E_k = k_B T = (1.38065 \\times 10^{-23}\\text{ J/K})(300.0\\text{ K}) = 4.14195 \\times 10^{-21}\\text{ J} = 0.02585\\text{ eV} = 25.85\\text{ meV}
\\]
The de Broglie wavelength is:
\\[
\\lambda_n = \\frac{h}{\\sqrt{2 m_n E_k}} = \\frac{6.62607 \\times 10^{-34}\\text{ J}\\cdot\\text{s}}{\\sqrt{2(1.67493 \\times 10^{-27}\\text{ kg})(4.14195 \\times 10^{-21}\\text{ J})}}
\\]
\\[
\\sqrt{2 \\times 1.67493 \\times 10^{-27} \\times 4.14195 \\times 10^{-21}} = \\sqrt{1.38749 \\times 10^{-47}} = 3.7249 \\times 10^{-24}\\text{ kg}\\cdot\\text{m/s}
\\]
\\[
\\lambda_n = \\frac{6.62607 \\times 10^{-34}}{3.7249 \\times 10^{-24}} = 1.7788 \\times 10^{-10}\\text{ m} = 1.779\\text{ Å}
\\]

### Step 2: Physical Origin of Scattering Factors
1. **Nuclear Scattering Length $b$**:
   The strong nuclear force has an effective range of $r_{\\text{nucleus}} \\sim 10^{-15}\\text{ m} = 1\\text{ fm}$.
   Since the neutron wavelength $\\lambda \\sim 1.8\\text{ Å} = 1.8 \\times 10^{-10}\\text{ m}$, the nucleus acts as a true mathematical point scatterer ($r_{\\text{nucleus}} \\ll \\lambda$).
   Therefore, the Fourier transform of a spatial delta function is constant:
   \\[
   b(q) = \\int \\delta(\\mathbf{r}) e^{i \\mathbf{q}\\cdot\\mathbf{r}} d^3\\mathbf{r} = b = \\text{constant (independent of } \\theta)
   \\]
2. **Magnetic Form Factor $f_{\\text{mag}}(\\theta)$**:
   Magnetic scattering arises from the dipole-dipole interaction between the neutron spin and unpaired $3d$ electron spins of the $\\text{Mn}^{2+}$ ions.
   Because the $3d$ electron cloud has a spatial extent of $r_{\\text{electron}} \\sim 1\\text{ Å}$, which is comparable to $\\lambda$, intra-atomic interference occurs across the electron shell.
   Consequently, $f_{\\text{mag}}(q)$ decreases rapidly with increasing scattering vector $q = (4\\pi/\\lambda)\\sin\\theta$, exactly analogous to X-ray atomic form factors.

### Step 3: Magnetic Superlattice Peak
In the antiferromagnetic state below $T_N = 118\\text{ K}$, alternating ferromagnetic $(111)$ planes have antiparallel spin alignments, doubling the magnetic repeat period:
\\[
a_{\\text{mag}} = 2 a = 2(4.445\\text{ Å}) = 8.890\\text{ Å}
\\]
For the magnetic superlattice reflection $(111)_{\\text{mag}}$:
\\[
d_{\\text{mag}} = \\frac{a_{\\text{mag}}}{\\sqrt{1^2 + 1^2 + 1^2}} = \\frac{8.890\\text{ Å}}{\\sqrt{3}} = 5.133\\text{ Å} = 2 d_{111,\\text{chemical}}
\\]
Using Bragg's Law with $\\lambda = 1.540\\text{ Å}$:
\\[
\\sin\\theta = \\frac{\\lambda}{2 d_{\\text{mag}}} = \\frac{1.540\\text{ Å}}{2(5.133\\text{ Å})} = 0.15001 \\implies \\theta = 8.628^\\circ
\\]
The observed scattering angle is:
\\[
2\\theta = 2(8.628^\\circ) = 17.26^\\circ
\\]
(In contrast, the chemical $(111)$ peak occurs at $2\\theta = 35.0^\\circ$). The emergence of this superlattice reflection at half the chemical angle directly confirmed antiferromagnetism."""
            },
            {
                "probNumber": "4.9",
                "title": "Multi-Wavelength Scherrer Crystallite Size Broadening and Williamson-Hall Microstrain Analysis",
                "difficulty": "Advanced",
                "statement": "An engineered nanocrystalline ceria ($\\text{CeO}_2$, fluorite structure) sample is measured on a high-resolution powder diffractometer ($\\lambda = 1.54056\\text{ Å}$). After subtracting instrumental broadening, the following integral peak breadths $\\beta$ (in radians) are recorded:\\n- $(111)$: $2\\theta = 28.55^\\circ$, $\\beta = 0.00782\\text{ rad}$\\n- $(200)$: $2\\theta = 33.08^\\circ$, $\\beta = 0.00845\\text{ rad}$\\n- $(220)$: $2\\theta = 47.48^\\circ$, $\\beta = 0.01072\\text{ rad}$\\n- $(311)$: $2\\theta = 56.34^\\circ$, $\\beta = 0.01231\\text{ rad}$\\n(a) Formulate the Williamson-Hall equation separating size broadening from microstrain.\\n(b) Construct the Williamson-Hall data table: compute $\\sin\\theta$ and $\\beta\\cos\\theta$ for each reflection.\\n(c) Perform linear regression to determine the average crystallite size $L$ (using shape factor $K = 0.94$) and the microstrain $\\varepsilon$.",
                "solution": r"""### Step 1: Formulation of the Williamson-Hall Method
Total peak broadening $\\beta$ in radians results from the convolution of crystallite size effects (Scherrer) and lattice microstrain (Stokes-Wilson):
\\[
\\beta = \\beta_{\\text{size}} + \\beta_{\\text{strain}} = \\frac{K\\lambda}{L\\cos\\theta} + 4\\varepsilon\\tan\\theta
\\]
Multiplying both sides by $\\cos\\theta$:
\\[
\\beta\\cos\\theta = \\frac{K\\lambda}{L} + 4\\varepsilon\\sin\\theta
\\]
This represents a straight line:
\\[
y = C_0 + C_1 x
\\]
where:
- $y = \\beta\\cos\\theta$
- $x = \\sin\\theta$
- Intercept $C_0 = \\frac{K\\lambda}{L} \\implies L = \\frac{K\\lambda}{C_0}$
- Slope $C_1 = 4\\varepsilon \\implies \\varepsilon = \\frac{C_1}{4}$

### Step 2: Computation of Williamson-Hall Variables
Given $\\lambda = 1.54056\\text{ Å}$:

1. **$(111)$**:
   - $\\theta = 14.275^\\circ$
   - $\\sin\\theta = \\sin(14.275^\\circ) = 0.24656$
   - $\\cos\\theta = \\cos(14.275^\\circ) = 0.96913$
   - $y = \\beta\\cos\\theta = 0.00782 \\times 0.96913 = 0.007579\\text{ rad}$

2. **$(200)$**:
   - $\\theta = 16.540^\\circ$
   - $\\sin\\theta = \\sin(16.540^\\circ) = 0.28470$
   - $\\cos\\theta = \\cos(16.540^\\circ) = 0.95862$
   - $y = 0.00845 \\times 0.95862 = 0.008100\\text{ rad}$

3. **$(220)$**:
   - $\\theta = 23.740^\\circ$
   - $\\sin\\theta = \\sin(23.740^\\circ) = 0.40259$
   - $\\cos\\theta = \\cos(23.740^\\circ) = 0.91538$
   - $y = 0.01072 \\times 0.91538 = 0.009813\\text{ rad}$

4. **$(311)$**:
   - $\\theta = 28.170^\\circ$
   - $\\sin\\theta = \\sin(28.170^\\circ) = 0.47209$
   - $\\cos\\theta = \\cos(28.170^\\circ) = 0.88155$
   - $y = 0.01231 \\times 0.88155 = 0.010852\\text{ rad}$

### Step 3: Linear Regression and Parameter Extraction
Summary of $(x_i, y_i)$:
- $i=1$: $(0.24656, 0.007579)$
- $i=2$: $(0.28470, 0.008100)$
- $i=3$: $(0.40259, 0.009813)$
- $i=4$: $(0.47209, 0.010852)$

Linear regression:
- Mean $x$: $\\bar{x} = (0.24656 + 0.28470 + 0.40259 + 0.47209)/4 = 0.35148$
- Mean $y$: $\\bar{y} = (0.007579 + 0.008100 + 0.009813 + 0.010852)/4 = 0.009086$
- $\\sum (x_i - \\bar{x})^2 = (-0.1049)^2 + (-0.0668)^2 + (0.0511)^2 + (0.1206)^2 = 0.01100 + 0.00446 + 0.00261 + 0.01455 = 0.03262$
- $\\sum (x_i - \\bar{x})(y_i - \\bar{y}) = (-0.1049)(-0.001507) + (-0.0668)(-0.000986) + (0.0511)(0.000727) + (0.1206)(0.001766) = 0.000158 + 0.000066 + 0.000037 + 0.000213 = 0.000474$

Slope $C_1$:
\\[
C_1 = \\frac{0.000474}{0.03262} = 0.01453
\\]
Intercept $C_0$:
\\[
C_0 = \\bar{y} - C_1 \\bar{x} = 0.009086 - (0.01453)(0.35148) = 0.009086 - 0.005107 = 0.003979
\\]

1. **Crystallite Size $L$**:
\\[
L = \\frac{K\\lambda}{C_0} = \\frac{0.94 \\times 1.54056\\text{ Å}}{0.003979} = \\frac{1.44813\\text{ Å}}{0.003979} = 363.9\\text{ Å} = 36.4\\text{ nm}
\\]

2. **Microstrain $\\varepsilon$**:
\\[
\\varepsilon = \\frac{C_1}{4} = \\frac{0.01453}{4} = 0.00363 = 0.363\\% = 3.63 \\times 10^{-3}
\\]
The nanocrystalline $\\text{CeO}_2$ has an average grain domain size of $36.4\\text{ nm}$ and a lattice strain of $0.36\\%$."""
            }
        ]
    }
    return u4

if __name__ == '__main__':
    u4 = get_unit_4()
    print("Unit 4 successfully generated:")
    print("Title:", u4["title"])
    print("Sections:", len(u4["sections"]))
    print("Problems:", len(u4["problems"]))
