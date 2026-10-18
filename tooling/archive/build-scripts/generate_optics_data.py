import json

units = []

# =========================================================================
# UNIT 1: Interference (Division of Wavefront)
# =========================================================================
u1_sections = [
    {
        "id": "sec-1-1",
        "number": "§1.1",
        "heading": "Huygens-Fresnel Principle, Wave Superposition and Complex Notation",
        "simulation": "young-double-slit",
        "content": """The wave nature of light rests on the fundamental principle that light propagation is governed by harmonic scalar wave equations derived directly from Maxwell's electrodynamics:

$$\\nabla^2 \\psi - \\frac{1}{c^2} \\frac{\\partial^2 \\psi}{\\partial t^2} = 0$$

where $\\psi(\\mathbf{r}, t)$ represents any scalar component of the optical electric field $\\mathbf{E}(\\mathbf{r}, t)$.

<h4>1. Complex Exponential Wave Representation</h4>
In monochromatic optical analysis, real oscillatory fields are most efficiently represented using Euler's complex notation:

$$\\psi(\\mathbf{r}, t) = \\operatorname{Re} \\left\\{ \\tilde{E}(\\mathbf{r}) e^{-i\\omega t} \\right\\} = \\operatorname{Re} \\left\\{ E_0 e^{i(\\mathbf{k} \\cdot \\mathbf{r} - \\omega t + \\phi)} \\right\\}$$

where $\\tilde{E}(\\mathbf{r}) = E_0 e^{i(\\mathbf{k}\\cdot\\mathbf{r} + \\phi)}$ is the complex amplitude (phasor), $k = \\frac{2\\pi}{\\lambda} = \\frac{\\omega}{c}$ is the wave number, $\\omega$ is the angular optical frequency, and $\\phi$ is the initial phase constant.

<h4>2. Linear Superposition of Two Coherent Optical Fields</h4>
Consider two monochromatic electromagnetic waves of identical angular frequency $\\omega$ intersecting at an observation point $P(\\mathbf{r})$. The individual electric field scalar amplitudes are:

$$E_1 = E_{01} e^{i(\\mathbf{k}_1 \\cdot \\mathbf{r} - \\omega t + \\phi_1)}, \\quad E_2 = E_{02} e^{i(\\mathbf{k}_2 \\cdot \\mathbf{r} - \\omega t + \\phi_2)}$$

By the principle of linear superposition in linear dielectric media, the total electric field at $P$ is the algebraic sum of the individual field vectors:

$$E_{\\text{total}} = E_1 + E_2 = \\left( E_{01} e^{i\\delta_1} + E_{02} e^{i\\delta_2} \\right) e^{-i\\omega t}$$

where $\\delta_1 = \\mathbf{k}_1 \\cdot \\mathbf{r} + \\phi_1$ and $\\delta_2 = \\mathbf{k}_2 \\cdot \\mathbf{r} + \\phi_2$.

<h4>3. Observable Optical Intensity and the Interference Term</h4>
Optical detectors (photodiodes, CCD sensors, human eye) cannot track instantaneous optical oscillations ($~10^{14}-10^{15} \\text{ Hz}$). Instead, detectors measure the time-averaged irradiance (optical intensity) $I$:

$$I = \\langle |E_{\\text{total}}|^2 \\rangle = \\frac{1}{2} E_{\\text{total}} E_{\\text{total}}^*$$

Substituting the complex superposition:

$$I = \\frac{1}{2} \\left( E_{01} e^{i\\delta_1} + E_{02} e^{i\\delta_2} \\right) \\left( E_{01} e^{-i\\delta_1} + E_{02} e^{-i\\delta_2} \\right)$$

$$I = \\frac{1}{2} \\left[ E_{01}^2 + E_{02}^2 + E_{01}E_{02} \\left( e^{i(\\delta_1 - \\delta_2)} + e^{-i(\\delta_1 - \\delta_2)} \\right) \\right]$$

Using Euler's identity $e^{i\\delta} + e^{-i\\delta} = 2\\cos \\delta$, and defining the phase difference $\\delta = \\delta_2 - \\delta_1$:

$$I = I_1 + I_2 + 2\\sqrt{I_1 I_2} \\cos \\delta$$

where $I_1 = \\frac{1}{2} E_{01}^2$ and $I_2 = \\frac{1}{2} E_{02}^2$ are the intensities of the independent beams. The term $J_{12} = 2\\sqrt{I_1 I_2} \\cos \\delta$ is the **Interference Term**.

<h4>4. Conditions for Sustained, High-Contrast Interference</h4>
For stable, observable interference fringes to persist in space and time:
<ol>
  <li><strong>Monochromaticity & Frequency Matching:</strong> The interfering beams must possess identical or nearly identical frequencies ($\\omega_1 = \\omega_2$). If frequencies differ by $\\Delta \\omega$, the cross term oscillates at $\\cos(\\Delta \\omega \\cdot t)$ and time-averages to zero.</li>
  <li><strong>Constant Phase Relationship (Coherence):</strong> The relative phase difference $\\delta$ must remain strictly invariant over the observation time interval $T_{\\text{obs}} \\gg \\tau_c$, where $\\tau_c$ is the coherence time of the source.</li>
  <li><strong>Parallel Polarization Vectors:</strong> If the electric fields are orthogonal ($\\mathbf{E}_1 \\perp \\mathbf{E}_2$), their scalar product vanishes: $\\mathbf{E}_1 \\cdot \\mathbf{E}_2 = 0$, giving $I = I_1 + I_2$ with zero interference modulation (Fresnel-Arago Law 1).</li>
  <li><strong>Equal Amplitudes ($I_1 \\approx I_2$):</strong> When $I_1 = I_2 = I_0$, the fringe visibility (contrast) reaches its theoretical maximum of unity:
  
  $$\\mathcal{V} = \\frac{I_{\\text{max}} - I_{\\text{min}}}{I_{\\text{max}} + I_{\\text{min}}} = \\frac{4I_0 - 0}{4I_0 + 0} = 1$$
  
  $$I(\\delta) = 4I_0 \\cos^2\\left(\\frac{\\delta}{2}\\right)$$
  </li>
</ol>"""
    },
    {
        "id": "sec-1-2",
        "number": "§1.2",
        "heading": "Young’s Double-Slit Experiment, Hyperbolic Fringes and Intensity Distribution",
        "simulation": "young-fringe-geometry",
        "content": """In 1801, Thomas Young provided the definitive experimental proof of the wave nature of light by dividing a primary wavefront into two secondary coherent wavelets using two closely spaced narrow slits $S_1$ and $S_2$.

<h4>1. Geometric Path Difference Derivation</h4>
Let two parallel slits separated by center-to-center distance $d$ illuminate a screen placed at distance $D$, where $D \\gg d$. Let the origin $O$ be the center of the screen, and let $P$ be a point on the screen at distance $y$ from $O$.

The physical paths traveled by the two wavelets from slits $S_1(0, d/2)$ and $S_2(0, -d/2)$ to $P(D, y)$ are:

$$r_1 = \\sqrt{D^2 + \\left(y - \\frac{d}{2}\\right)^2} = D \\left[ 1 + \\frac{\\left(y - d/2\\right)^2}{D^2} \\right]^{1/2}$$

$$r_2 = \\sqrt{D^2 + \\left(y + \\frac{d}{2}\\right)^2} = D \\left[ 1 + \\frac{\\left(y + d/2\\right)^2}{D^2} \\right]^{1/2}$$

Applying the binomial expansion $(1 + u)^{1/2} = 1 + \\frac{1}{2}u - \\dots$ for $y, d \\ll D$:

$$r_1 \\approx D + \\frac{(y - d/2)^2}{2D}, \\quad r_2 \\approx D + \\frac{(y + d/2)^2}{2D}$$

The optical path difference $\\Delta = r_2 - r_1$ is:

$$\\Delta = \\frac{(y + d/2)^2 - (y - d/2)^2}{2D} = \\frac{2yd}{2D} = \\frac{y d}{D}$$

In angular coordinates where $\\theta$ is the angle subtended at the slit midpoint: $\\sin \\theta \\approx \\tan \\theta = \\frac{y}{D}$, yielding:

$$\\Delta = d \\sin \\theta$$

<h4>2. Constructive and Destructive Interference Conditions</h4>
The corresponding optical phase difference is:

$$\\delta = \\frac{2\\pi}{\\lambda} \\Delta = \\frac{2\\pi d y}{\\lambda D}$$

<ul>
  <li><strong>Bright Fringes (Intensity Maxima):</strong> Occur when the path difference is an integer multiple of the wavelength:
  
  $$\\Delta = m \\lambda \\implies y_m = m \\frac{\\lambda D}{d}, \\quad m \\in \\{0, \\pm 1, \\pm 2, \\dots\\}$$
  </li>
  <li><strong>Dark Fringes (Intensity Minima):</strong> Occur when the path difference is a half-integral multiple of the wavelength:
  
  $$\\Delta = \\left(m + \\frac{1}{2}\\right) \\lambda \\implies y_m' = \\left(m + \\frac{1}{2}\\right) \\frac{\\lambda D}{d}, \\quad m \\in \\{0, \\pm 1, \\pm 2, \\dots\\}$$
  </li>
</ul>

<h4>3. Linear Fringe Width (Fringe Spacing) $\\beta$</h4>
The distance between any two consecutive bright or dark fringes is constant:

$$\\beta = y_{m+1} - y_m = \\frac{(m+1)\\lambda D}{d} - \\frac{m\\lambda D}{d} = \\frac{\\lambda D}{d}$$

This equation provides a direct, high-precision laboratory method for measuring the optical wavelength $\\lambda = \\frac{\\beta d}{D}$.

<h4>4. 3D Spatial Fringe Shape: Hyperboloids of Revolution</h4>
The locus of all points in 3D space with a constant path difference from two point sources $S_1$ and $S_2$ is defined by:

$$|r_2 - r_1| = \\text{constant} = m\\lambda$$

By classical analytic geometry, this is the definition of a **hyperboloid of two sheets** having $S_1$ and $S_2$ as foci. When intercepted by a flat planar screen placed perpendicular to the central axis at $x = D$, the intersection of these hyperboloids with the plane $x = D$ produces narrow hyperbolic curves. Near the central axis ($y, z \\ll D$), the vertices of these hyperbolas have extremely small curvature, appearing to high precision as straight, equispaced parallel interference fringes."""
    },
    {
        "id": "sec-1-3",
        "number": "§1.3",
        "heading": "Fresnel’s Biprism: Virtual Coherent Sources and Wavelength Determination",
        "simulation": "fresnel-biprism",
        "content": """Augustin-Jean Fresnel designed the biprism to overcome the criticism that Young's fringes were merely edge-diffraction effects produced by the slit edges. The Fresnel biprism produces two mutually coherent virtual sources purely by refraction without any aperture edges between the two beams.

<h4>1. Optical Construction and Refraction by Biprism</h4>
A Fresnel biprism consists of two acute prisms joined at their bases, with an obtuse angle of approximately $179^\\circ$ and two very small refracting angles $\\alpha \\approx 30' \\approx 0.5^\\circ$.

A narrow monochromatic slit $S$ illuminated by wavelength $\\lambda$ is placed at distance $u$ in front of the flat face of the biprism. Light passing through the upper half is deviated downwards by angle $\\delta$, while light passing through the lower half is deviated upwards by the identical angle $\\delta$.

For a thin prism of refractive index $n$ and refracting angle $\\alpha$, the angle of minimum deviation is:

$$\\delta = (n - 1)\\alpha$$

<h4>2. Separation Between Virtual Coherent Sources $d$</h4>
Due to refraction, the light appears to diverge from two virtual point sources $S_1$ and $S_2$ located in the plane of the original slit $S$:

$$d = 2 u \\delta = 2 u (n - 1) \\alpha$$

Because both $S_1$ and $S_2$ originate from the same primary wavefront of slit $S$, they maintain strict mutual phase coherence.

<h4>3. Fringe Width and Screen Separation</h4>
Let the distance from the slit $S$ to the micrometer eyepiece (screen) be $D$. The fringe width on the observation plane is given by the standard interference relation:

$$\\beta = \\frac{\\lambda D}{d} = \\frac{\\lambda D}{2 u (n - 1) \\alpha}$$

<h4>4. The Displacement Method for Direct Measurement of $d$</h4>
Direct physical measurement of the virtual distance $d$ (which is on the order of $0.5 - 2 \\text{ mm}$) introduces significant experimental error. Fresnel solved this by inserting a convex lens between the biprism and the eyepiece.

For a fixed distance $D > 4f$, there exist two conjugate positions of the convex lens that produce sharp real images of $S_1$ and $S_2$ in the focal plane of the micrometer eyepiece:
<ul>
  <li>Position 1 (Magnified image separation $d_1$): $m_1 = \\frac{v_1}{u_1} = \\frac{d_1}{d}$</li>
  <li>Position 2 (Diminished image separation $d_2$): $m_2 = \\frac{v_2}{u_2} = \\frac{d_2}{d}$</li>
</ul>

By the principle of optical reversibility, $u_1 = v_2$ and $v_1 = u_2$, therefore:

$$m_1 \\cdot m_2 = \\frac{d_1}{d} \\cdot \\frac{d_2}{d} = 1 \\implies d^2 = d_1 d_2 \\implies d = \\sqrt{d_1 d_2}$$

Consequently, the optical wavelength is determined with exceptional accuracy without needing to know the refractive index $n$ or biprism angle $\\alpha$:

$$\\lambda = \\frac{\\beta d}{D} = \\frac{\\beta \\sqrt{d_1 d_2}}{D}$$"""
    },
    {
        "id": "sec-1-4",
        "number": "§1.4",
        "heading": "Lloyd’s Mirror: Grazing Incidence and the Fundamental Half-Wave (\\pi) Phase Shift",
        "simulation": "lloyd-mirror",
        "content": """In 1834, Humphrey Lloyd developed a single-reflector interference configuration that definitively confirmed the electromagnetic boundary condition predicting a $\\pi$ phase shift upon external reflection.

<h4>1. Experimental Geometry and Ray Tracing</h4>
A monochromatic primary point source $S_1$ of wavelength $\\lambda$ is placed at a very small height $h$ above the plane of an optical flat front-surface mirror of length $L$. A screen is placed at distance $D$ perpendicular to the mirror plane.

Light from $S_1$ propagates to the screen via two paths:
<ol>
  <li><strong>Direct Wave:</strong> Propagates directly from $S_1$ to the screen at height $y$.</li>
  <li><strong>Reflected Wave:</strong> Strikes the mirror at grazing incidence and reflects to the screen, appearing to originate from the virtual mirror image $S_2$ located at depth $h$ below the mirror surface.</li>
</ol>

The effective distance between the two interfering coherent sources is:

$$d = 2h$$

<h4>2. The Crucial Half-Wave Phase Discontinuity ($\\pi$ Phase Jump)</h4>
From Maxwell's electromagnetic boundary conditions (Fresnel reflection equations), when an optical wave traveling in an optically rarer medium ($n_1 = 1$) reflects at the boundary of a denser medium ($n_2 > 1$) at grazing incidence (angle of incidence $\\theta_i \\to 90^\\circ$):

$$r_{\\perp} = \\frac{\\cos \\theta_i - \\sqrt{n^2 - \\sin^2 \\theta_i}}{\\cos \\theta_i + \\sqrt{n^2 - \\sin^2 \\theta_i}} \\xrightarrow{\\theta_i \\to 90^\\circ} -1 = e^{i\\pi}$$

This reflection introduces an abrupt, non-geometric phase discontinuity of exactly $\\pi$ radians (equivalent to an optical path penalty of $\\frac{\\lambda}{2}$).

The net optical path difference between the reflected and direct waves arriving at height $y$ is:

$$\\Delta_{\\text{net}} = (r_2 - r_1) + \\frac{\\lambda}{2} = \\frac{y d}{D} + \\frac{\\lambda}{2}$$

<h4>3. Inversion of Interference Conditions</h4>
Setting $\\Delta_{\\text{net}}$ equal to integral and half-integral multiples of $\\lambda$:

<ul>
  <li><strong>Dark Fringes (Destructive Interference):</strong>
  
  $$\\frac{y d}{D} + \\frac{\\lambda}{2} = \\left(m + \\frac{1}{2}\\right)\\lambda \\implies y_m = m \\frac{\\lambda D}{d}, \\quad m \\in \\{0, 1, 2, \\dots\\}$$
  </li>
  <li><strong>Bright Fringes (Constructive Interference):</strong>
  
  $$\\frac{y d}{D} + \\frac{\\lambda}{2} = m\\lambda \\implies y_m' = \\left(m - \\frac{1}{2}\\right) \\frac{\\lambda D}{d}, \\quad m \\in \\{1, 2, 3, \\dots\\}$$
  </li>
</ul>

<h4>4. The Vanishing Central Fringe at the Mirror Edge</h4>
At the point of grazing contact with the mirror surface ($y = 0$), the geometric path difference vanishes: $r_2 - r_1 = 0$. In standard Young's double-slit interference, $y = 0$ corresponds to the central **bright** maximum.

However, in Lloyd's mirror, due to the $-\\pi$ phase jump on reflection:

$$\\Delta_{\\text{net}}(y=0) = 0 + \\frac{\\lambda}{2} = \\frac{\\lambda}{2} \\implies I(y=0) = 0$$

Thus, the central fringe in Lloyd's mirror is **strictly dark**. When white light is used, the central fringe is completely achromatic and jet black, unambiguously proving that reflection from a denser medium induces a phase change of $\\pi$ radians."""
    }
]

u1_problems = [
    {
        "difficulty": "diff-medium",
        "difficultyLabel": "Medium",
        "title": "Example 1.1: Quantitative Precision Measurement in Fresnel Biprism",
        "question": "In a Fresnel biprism experiment with sodium light of wavelength $\\lambda = 589.3\\text{ nm}$, the distance between the primary slit and the micrometer eyepiece is $D = 1.20\\text{ m}$. Using a convex lens placed at two conjugate positions, the separations between the magnified and diminished images of the virtual sources are measured to be $d_1 = 4.05\\text{ mm}$ and $d_2 = 2.45\\text{ mm}$ respectively. Calculate: (a) the separation $d$ between the virtual coherent sources, (b) the fringe width $\\beta$ observed on the micrometer scale, and (c) the number of bright fringes observed across a $15\\text{ mm}$ field of view.",
        "steps": [
            {
                "title": "Step 1: Calculate the virtual source separation d using the conjugate displacement formula",
                "math": "$$d = \\sqrt{d_1 d_2} = \\sqrt{(4.05 \\times 10^{-3} \\text{ m}) \\times (2.45 \\times 10^{-3} \\text{ m})} = \\sqrt{9.9225 \\times 10^{-6} \\text{ m}^2} \\approx 3.150 \\times 10^{-3} \\text{ m} = 3.150 \\text{ mm}$$",
                "explanation": "The lens magnification at conjugate positions satisfies $m_1 m_2 = 1$, making the geometric mean of the two image separations equal to the true separation of the virtual sources."
            },
            {
                "title": "Step 2: Determine the linear fringe width beta",
                "math": "$$\\beta = \\frac{\\lambda D}{d} = \\frac{(589.3 \\times 10^{-9} \\text{ m}) \\times (1.20 \\text{ m})}{3.150 \\times 10^{-3} \\text{ m}} = \\frac{7.0716 \\times 10^{-7}}{3.150 \\times 10^{-3}} \\approx 2.245 \\times 10^{-4} \\text{ m} = 0.2245 \\text{ mm}$$",
                "explanation": "Each fringe pair (one bright and one dark interval) occupies exactly $0.2245\\text{ mm}$ on the eyepiece focal plane."
            },
            {
                "title": "Step 3: Calculate the total number of fringes across the field of view",
                "math": "$$N = \\frac{W}{\\beta} = \\frac{15.0 \\text{ mm}}{0.2245 \\text{ mm}} \\approx 66.82 \\implies N = 66 \\text{ complete bright fringes}$$",
                "explanation": "Over a $1.5\\text{ cm}$ field of view, approximately 66 bright interference bands are resolved by the micrometer."
            }
        ]
    },
    {
        "difficulty": "diff-hard",
        "difficultyLabel": "Hard",
        "title": "Example 1.2: Shift of Fringes by Introduction of Thin Transparent Mica Sheet",
        "question": "A thin transparent sheet of mica of refractive index $\\mu = 1.58$ is inserted into the path of one of the interfering beams in a double-slit experiment illuminated by $\\lambda = 550\\text{ nm}$. The central zero-order bright fringe shifts across the screen by a distance equal to the spacing of 14 bright fringes. (a) Derive the general expression for the fringe shift $y_0$. (b) Calculate the precise thickness $t$ of the mica sheet.",
        "steps": [
            {
                "title": "Step 1: Derive the optical path difference introduced by a dielectric plate of thickness t",
                "math": "$$\\text{Path in air} = t, \\quad \\text{Optical path in medium} = \\mu t$$\n$$\\Delta_{\\text{extra}} = \\mu t - t = (\\mu - 1)t$$\n$$\\text{Total path difference at screen position } y: \\quad \\Delta = \\frac{y d}{D} - (\\mu - 1)t$$",
                "explanation": "The medium slows the phase velocity to $c/\\mu$, adding an optical distance $(\\mu - 1)t$ to the traversed arm."
            },
            {
                "title": "Step 2: Relate the central fringe position to the fringe count shift n",
                "math": "$$\\text{At the shifted central fringe } (\\Delta = 0): \\quad \\frac{y_0 d}{D} = (\\mu - 1)t \\implies y_0 = \\frac{D}{d} (\\mu - 1)t$$\n$$\\text{Since fringe width } \\beta = \\frac{\\lambda D}{d}, \\quad y_0 = n \\beta = n \\frac{\\lambda D}{d} \\implies n \\lambda = (\\mu - 1)t$$",
                "explanation": "The number of shifted fringes $n$ depends purely on the extra optical path divided by the wavelength."
            },
            {
                "title": "Step 3: Solve for thickness t with numerical parameters",
                "math": "$$t = \\frac{n \\lambda}{\\mu - 1} = \\frac{14 \\times (550 \\times 10^{-9} \\text{ m})}{1.58 - 1} = \\frac{7.70 \\times 10^{-6} \\text{ m}}{0.58} \\approx 1.328 \\times 10^{-5} \\text{ m} = 13.28 \\ \\mu\\text{m}$$",
                "explanation": "The mica sheet has a physical thickness of $13.28$ micrometers, demonstrating the extreme interferometric sensitivity of optical path measurements."
            }
        ]
    }
]

units.append({
    "number": 1,
    "title": "Interference by Division of Wavefront",
    "description": "Huygens' principle, wave superposition in complex notation, Young's double slit, fringe width & geometry, Fresnel's biprism, and Lloyd's mirror.",
    "sections": u1_sections,
    "problems": u1_problems
})

print("Unit 1 generated successfully.")
