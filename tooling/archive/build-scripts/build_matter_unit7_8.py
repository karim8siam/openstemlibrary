# Build Script for Units 7 and 8: Stationary Waves and Sound Waves
import json

# =========================================================================
# UNIT 7: Stationary Waves
# =========================================================================
u7_sections = [
    {
        "id": "sec-7-1",
        "number": "§7.1",
        "heading": "Reflection and Transmission at a Boundary Junction",
        "simulation": "standing-wave-sim",
        "content": """When a traveling wave encounters a discontinuity between two different physical media, part of the incident wave energy is reflected back into the first medium, and part is transmitted into the second medium.

<h4>1. Boundary Conditions at the Interface</h4>
Consider two semi-infinite stretched strings joined seamlessly at $x = 0$ under constant uniform tension $T$.
Medium 1 ($x < 0$) has linear density $\\mu_1$ and wave speed $v_1 = \\sqrt{T/\\mu_1}$.
Medium 2 ($x > 0$) has linear density $\\mu_2$ and wave speed $v_2 = \\sqrt{T/\\mu_2}$.
An incident harmonic wave travels in medium 1:
$$y_i(x, t) = A_i \\cos(k_1 x - \\omega t)$$
Upon striking $x = 0$, it gives rise to a reflected wave $y_r(x, t)$ and a transmitted wave $y_t(x, t)$:
$$y_r(x, t) = A_r \\cos(-k_1 x - \\omega t) = A_r \\cos(k_1 x + \\omega t)$$
$$y_t(x, t) = A_t \\cos(k_2 x - \\omega t)$$
Because both sides vibrate at the driving source frequency, angular frequency $\\omega$ is identical in both media.
The physical interface requires two fundamental boundary conditions at $x = 0$:
<ol>
  <li><strong>Displacement Continuity:</strong> The string must not tear:
  $$y_1(0, t) = y_2(0, t) \\implies y_i(0, t) + y_r(0, t) = y_t(0, t)$$
  $$A_i + A_r = A_t$$</li>
  <li><strong>Transverse Force Continuity:</strong> By Newton's third law, the transverse vertical tension components must balance:
  $$T \\left( \\frac{\\partial y_1}{\\partial x} \\right)_{x=0} = T \\left( \\frac{\\partial y_2}{\\partial x} \\right)_{x=0} \\implies k_1 (A_i - A_r) = k_2 A_t$$</li>
</ol>

<h4>2. Amplitude Reflection and Transmission Coefficients</h4>
Solving the two linear equations:
$$A_r = \\left( \\frac{k_1 - k_2}{k_1 + k_2} \\right) A_i = \\left( \\frac{v_2 - v_1}{v_1 + v_2} \\right) A_i$$
$$A_t = \\left( \\frac{2 k_1}{k_1 + k_2} \\right) A_i = \\left( \\frac{2 v_2}{v_1 + v_2} \\right) A_i$$
Defining the <strong>characteristic mechanical wave impedance</strong> $Z = \\mu v = \\sqrt{\\mu T} = \\frac{T}{v}$:
$$r = \\frac{A_r}{A_i} = \\frac{Z_1 - Z_2}{Z_1 + Z_2}, \\quad t = \\frac{A_t}{A_i} = \\frac{2 Z_1}{Z_1 + Z_2}$$

<h4>3. Phase Inversion Analysis</h4>
<ul>
  <li><strong>Denser second medium ($\mu_2 > \mu_1 \implies Z_2 > Z_1$):</strong>
  The reflection coefficient is negative ($r < 0$).
  Since $\\cos(k_1 x + \\omega t + \\pi) = -\\cos(k_1 x + \\omega t)$, reflection at an acoustically denser medium induces an instantaneous <strong>phase reversal of $\pi$ radians (180°)</strong>!</li>
  <li><strong>Rarer second medium ($\mu_2 < \mu_1 \implies Z_2 < Z_1$):</strong>
  $r > 0$. The wave reflects in-phase (zero phase shift).</li>
  <li><strong>Transmission:</strong> $t > 0$ always. The transmitted wave never undergoes phase inversion.</li>
</ul>

<h4>4. Conservation of Wave Energy Flux</h4>
Wave power is proportional to $Z A^2$:
$$P_i = \\frac{1}{2} Z_1 \\omega^2 A_i^2, \\quad P_r = \\frac{1}{2} Z_1 \\omega^2 A_r^2, \\quad P_t = \\frac{1}{2} Z_2 \\omega^2 A_t^2$$
Defining the energy reflection coefficient $R = P_r / P_i$ and transmission coefficient $T_{trans} = P_t / P_i$:
$$R = \\left( \\frac{Z_1 - Z_2}{Z_1 + Z_2} \\right)^2, \\quad T_{trans} = \\frac{Z_2}{Z_1} \\left( \\frac{2 Z_1}{Z_1 + Z_2} \\right)^2 = \\frac{4 Z_1 Z_2}{(Z_1 + Z_2)^2}$$
$$R + T_{trans} = \\frac{(Z_1 - Z_2)^2 + 4 Z_1 Z_2}{(Z_1 + Z_2)^2} = \\frac{(Z_1 + Z_2)^2}{(Z_1 + Z_2)^2} = 1$$
Energy is strictly conserved across the boundary.

<h4>5. Boundary Conditions for No Reflection: Impedance Matching</h4>
When $Z_1 = Z_2$:
$$R = 0, \\quad T_{trans} = 1$$
Zero energy is reflected back; 100% of the wave power passes unhindered into the second medium. This is the foundational principle of <strong>impedance matching</strong>, critical in ultrasound transducer design (acoustic gel), anti-reflective optical coatings (quarter-wave dielectric layers), and electrical transmission lines."""
    },
    {
        "id": "sec-7-2",
        "number": "§7.2",
        "heading": "Reflection at Fixed and Free Ends: Formation of Standing Waves",
        "simulation": "standing-wave-sim",
        "content": """A stationary (standing) wave is formed when two identical harmonic waves of equal amplitude and frequency propagate in opposite directions through the same medium.

<h4>1. Reflection at a Rigid Fixed End ($x = 0$)</h4>
At an infinitely rigid termination ($Z_2 \\to \\infty$), the displacement must vanish identically for all time: $y(0, t) = 0$.
The incident wave is $y_i(x, t) = A \\cos(kx - \\omega t)$.
To cancel $y_i$ at $x = 0$, the reflected wave must have $A_r = -A$:
$$y_r(x, t) = -A \\cos(kx + \\omega t)$$
Superposing the incident and reflected waves:
$$y(x, t) = y_i(x, t) + y_r(x, t) = A [\\cos(kx - \\omega t) - \\cos(kx + \\omega t)]$$
Using the prosthaphaeresis identity $\\cos(\\alpha - \\beta) - \\cos(\\alpha + \\beta) = 2\\sin\\alpha\\sin\\beta$:
$$y(x, t) = 2 A \\sin(kx) \\sin(\\omega t)$$
Notice the spatial and temporal variables are completely separated!
The amplitude of oscillation at any position $x$ is:
$$A_{standing}(x) = 2 A |\\sin(kx)|$$

<h4>2. Nodes and Antinodes</h4>
<ul>
  <li><strong>Nodes:</strong> Points of permanent zero displacement ($A_{standing} = 0$):
  $$\\sin(kx) = 0 \\implies kx = n\\pi \\implies x_n = n \\frac{\\lambda}{2}, \\quad n = 0, 1, 2, \\dots$$
  Consecutive nodes are separated by half a wavelength: $\\Delta x_{\\text{node}} = \\frac{\\lambda}{2}$.</li>
  <li><strong>Antinodes:</strong> Points of maximum displacement amplitude ($A_{standing} = 2A$):
  $$|\\sin(kx)| = 1 \\implies kx = \\left(n + \\frac{1}{2}\\right)\\pi \\implies x_a = \\left(n + \\frac{1}{2}\\right) \\frac{\\lambda}{2}$$
  Consecutive antinodes are separated by $\\frac{\\lambda}{2}$.
  The distance between an adjacent node and antinode is a quarter wavelength: $\\frac{\\lambda}{4}$.</li>
</ul>

<h4>3. Reflection at a Free End ($x = 0$)</h4>
At an unconstrained frictionless ring / free end, transverse force vanishes: $\\frac{\\partial y}{\\partial x}\\Big|_{x=0} = 0$.
Here $A_r = +A$ (no phase flip):
$$y(x, t) = A [\\cos(kx - \\omega t) + \\cos(kx + \\omega t)] = 2 A \\cos(kx) \\cos(\\omega t)$$
An antinode forms directly at the free boundary."""
    },
    {
        "id": "sec-7-3",
        "number": "§7.3",
        "heading": "Normal Modes and Proper Frequencies of a Stretched String",
        "simulation": "standing-wave-sim",
        "content": """When a string of length $L$ is clamped rigidly at both ends ($x = 0$ and $x = L$), boundary conditions permit only discrete resonant modes of oscillation, known as <strong>normal modes</strong>.

<h4>1. Boundary Conditions and Mode Frequencies</h4>
The general standing wave solution is $y(x, t) = [C_1 \\sin(kx) + C_2 \\cos(kx)] \\cos(\\omega t + \\phi)$.
<ol>
  <li>At $x = 0$: $y(0, t) = 0 \\implies C_2 = 0$. Thus $y(x, t) = C_1 \\sin(kx) \\cos(\\omega t + \\phi)$.</li>
  <li>At $x = L$: $y(L, t) = 0 \\implies C_1 \\sin(kL) = 0$.</li>
</ol>
For non-trivial oscillations ($C_1 \\ne 0$):
$$\\sin(k L) = 0 \\implies k_n L = n \\pi, \\quad n = 1, 2, 3, \\dots$$
The allowed wavenumbers and wavelengths are:
$$k_n = \\frac{n\\pi}{L}, \\quad \\lambda_n = \\frac{2L}{n}$$
Since wave speed is $v = \\sqrt{T/\\mu}$, the allowed <strong>proper (eigen) frequencies</strong> are:
$$f_n = \\frac{v}{\\lambda_n} = \\frac{n v}{2L} = \\frac{n}{2L}\\sqrt{\\frac{T}{\\mu}}, \\quad n = 1, 2, 3, \\dots$$

<h4>2. Harmonic Spectrum of a Stretched String</h4>
<ul>
  <li><strong>Fundamental Mode / First Harmonic ($n = 1$):</strong>
  $$\\lambda_1 = 2L, \\quad f_1 = \\frac{1}{2L}\\sqrt{\\frac{T}{\\mu}}$$
  Contains 2 nodes at the ends and 1 central antinode.</li>
  <li><strong>Second Harmonic / First Overtone ($n = 2$):</strong>
  $$\\lambda_2 = L, \\quad f_2 = 2 f_1$$
  Contains 3 nodes (including center $x = L/2$) and 2 antinodes.</li>
  <li><strong>Third Harmonic / Second Overtone ($n = 3$):</strong>
  $$\\lambda_3 = \\frac{2L}{3}, \\quad f_3 = 3 f_1$$
</ul>
Because all integer multiples $f_n = n f_1$ are present, the overtone spectrum is complete and richly consonant, giving musical string instruments (violin, guitar, piano) their warm, harmonic timbre.

<h4>3. Mersenne's Laws of Vibrating Strings</h4>
Marin Mersenne (1636) summarized the physical dependencies of the fundamental frequency:
<ol>
  <li><strong>Law of Length:</strong> $f \\propto \\frac{1}{L}$ (halving length doubles pitch).</li>
  <li><strong>Law of Tension:</strong> $f \\propto \\sqrt{T}$ (quadrupling tension doubles pitch).</li>
  <li><strong>Law of Density:</strong> $f \\propto \\frac{1}{\\sqrt{\\mu}} = \\frac{1}{r \\sqrt{\\rho}}$ (thicker strings produce lower pitch).</li>
</ol>"""
    },
    {
        "id": "sec-7-4",
        "number": "§7.4",
        "heading": "Standing Waves in Organ Pipes and Acoustic Columns",
        "simulation": "standing-wave-sim",
        "content": """In acoustic columns (organ pipes, flutes, clarinets), standing waves are formed by longitudinal air particle displacements and pressure oscillations.

<h4>1. Displacement vs. Pressure Waves</h4>
In a sound wave, particle displacement $s(x, t)$ and acoustic gauge pressure $p(x, t)$ are out of phase by 90°:
$$s(x, t) = s_0 \\sin(kx - \\omega t) \\implies p(x, t) = -B \\frac{\\partial s}{\\partial x} = -B k s_0 \\cos(kx - \\omega t)$$
Consequently:
<ul>
  <li>A <strong>displacement node</strong> (rigid closed boundary where air cannot move) is always a <strong>pressure antinode</strong> (maximum pressure variation).</li>
  <li>A <strong>displacement antinode</strong> (open pipe end open to atmosphere) is always a <strong>pressure node</strong> (pressure is fixed at atmospheric $p = 0$).</li>
</ul>

<h4>2. Open Pipe (Open at Both Ends)</h4>
Both ends are open to atmosphere $\\implies$ displacement antinodes at both $x = 0$ and $x = L$:
$$\\lambda_n = \\frac{2L}{n}, \\quad f_n = \\frac{n v}{2L} = n f_1, \\quad n = 1, 2, 3, \\dots$$
An open pipe produces all harmonics (both even and odd).

<h4>3. Closed Pipe (Closed at One End, Open at the Other)</h4>
Closed end at $x = 0$ (displacement node); open end at $x = L$ (displacement antinode):
$$L = (2n - 1) \\frac{\\lambda_n}{4} \\implies \\lambda_n = \\frac{4L}{2n - 1}$$
$$f_n = \\frac{(2n - 1) v}{4L} = (2n - 1) f_1, \\quad n = 1, 2, 3, \\dots$$
A closed pipe produces <strong>only odd harmonics</strong> ($f_1, 3f_1, 5f_1, \\dots$). The fundamental frequency of a closed pipe is half that of an open pipe of identical length ($f_{1,\\text{closed}} = \\frac{1}{2} f_{1,\\text{open}}$).

<h4>4. End Correction</h4>
In reality, the acoustic wave reflects slightly outside the open end of a tube of radius $R$.
Lord Rayleigh showed that an acoustic end correction $e \\approx 0.61 R$ must be added for each open end:
<ul>
  <li>Open Pipe: $L_{eff} = L + 2(0.61 R) = L + 1.22 R$.</li>
  <li>Closed Pipe: $L_{eff} = L + 0.61 R$.</li>
</ul>"""
    },
    {
        "id": "sec-7-5",
        "number": "§7.5",
        "heading": "Melde's Experiment and Energy Distribution in Stationary Waves",
        "simulation": "standing-wave-sim",
        "content": """Franz Melde (1859) devised an elegant electro-mechanical apparatus to demonstrate standing waves and verify Mersenne's laws.

<h4>1. Experimental Arrangements of Melde's Apparatus</h4>
A light string of length $L$ and linear density $\\mu$ is tied to one prong of an electrically driven tuning fork of frequency $f_{fork}$ and stretched horizontally over a frictionless pulley with suspended mass $M$ ($T = M g$).
<ol>
  <li><strong>Transverse Arrangement:</strong> The prongs vibrate perpendicular to the length of the string.
  For every oscillation of the fork prong, the string is displaced once:
  $$f_{\\text{string}} = f_{fork}$$
  If the string vibrates in $p$ resonant loops: $L = p \\frac{\\lambda}{2} \\implies \\lambda = \\frac{2L}{p}$.
  $$f_{fork} = \\frac{p}{2L}\\sqrt{\\frac{T}{\\mu}} = \\frac{p}{2L}\\sqrt{\\frac{M g}{\\mu}} \\implies \\frac{T}{p^2} = \\text{constant}$$</li>
  <li><strong>Longitudinal Arrangement:</strong> The prongs vibrate parallel to the length of the string.
  When the prong moves forward, tension drops; when it moves backward, tension peaks. The string is pulled twice during each complete cycle of the tuning fork.
  Hence the frequency of the string is exactly half the tuning fork frequency (parametric excitation):
  $$f_{\\text{string}} = \\frac{1}{2} f_{fork}$$
  $$f_{fork} = \\frac{p}{L}\\sqrt{\\frac{T}{\\mu}}$$</li>
</ol>

<h4>2. Energy Distribution in Stationary Waves</h4>
In a traveling wave, energy flows continuously downstream.
In a stationary wave:
$$y(x, t) = 2 A \\sin(kx) \\cos(\\omega t)$$
<ul>
  <li><strong>Kinetic Energy Density:</strong>
  $$u_K(x, t) = \\frac{1}{2}\\mu \\left(\\frac{\\partial y}{\\partial t}\\right)^2 = 2 \\mu \\omega^2 A^2 \\sin^2(kx) \\sin^2(\\omega t)$$</li>
  <li><strong>Potential Energy Density:</strong>
  $$u_P(x, t) = \\frac{1}{2}T \\left(\\frac{\\partial y}{\\partial x}\\right)^2 = 2 T k^2 A^2 \\cos^2(kx) \\cos^2(\\omega t) = 2 \\mu \\omega^2 A^2 \\cos^2(kx) \\cos^2(\\omega t)$$</li>
</ul>
Notice:
<ul>
  <li>When $\\sin(\\omega t) = 1$ (string passing through equilibrium $y = 0$), potential energy is zero everywhere, and total energy resides purely as kinetic energy concentrated at the <strong>antinodes</strong> ($\sin(kx) = 1$).</li>
  <li>When $\\cos(\\omega t) = 1$ (string at maximum displacement), kinetic energy is zero everywhere, and total energy resides purely as potential elastic energy concentrated at the <strong>nodes</strong> ($\cos(kx) = 1$, where string slope is steepest!).</li>
</ul>
Total energy remains permanently trapped, surging periodically between nodes (elastic potential energy) and antinodes (kinetic energy) with zero net spatial flux across the nodes."""
    }
]

u7_problems = [
    {
        "id": "prob-7-1",
        "difficulty": "Honors Wave Mechanics Standard",
        "title": "Wave Reflection and Transmission at a Composite String Junction",
        "question": "A steel wire of linear density $\\mu_1 = 4.00 \\times 10^{-3}\\text{ kg/m}$ is joined at $x = 0$ to a copper wire of linear density $\\mu_2 = 9.00 \\times 10^{-3}\\text{ kg/m}$. The composite wire is maintained under uniform tension $T = 360\\text{ N}$. A sinusoidal transverse wave of frequency $f = 120\\text{ Hz}$ and amplitude $A_i = 6.00\\text{ mm}$ travels from the steel wire toward the junction.\\n(a) Calculate the wave speed and mechanical impedance in both wires,\\n(b) Determine the amplitude reflection coefficient $r$, amplitude transmission coefficient $t$, and the reflected and transmitted amplitudes $A_r$ and $A_t$, and\\n(c) Compute the energy reflection coefficient $R$ and transmission coefficient $T_{trans}$, verifying conservation of wave power.",
        "steps": [
            {
                "title": "Step 1: Compute wave speeds and mechanical impedances",
                "math": "$$v_1 = \\sqrt{\\frac{T}{\\mu_1}} = \\sqrt{\\frac{360}{4.00 \\times 10^{-3}}} = \\sqrt{90000} = 300.0 \\text{ m/s}$$\n$$v_2 = \\sqrt{\\frac{T}{\\mu_2}} = \\sqrt{\\frac{360}{9.00 \\times 10^{-3}}} = \\sqrt{40000} = 200.0 \\text{ m/s}$$\n$$Z_1 = \\sqrt{\\mu_1 T} = \\sqrt{4.00 \\times 10^{-3} \\times 360} = \\sqrt{1.44} = 1.200 \\text{ kg/s}$$\n$$Z_2 = \\sqrt{\\mu_2 T} = \\sqrt{9.00 \\times 10^{-3} \\times 360} = \\sqrt{3.24} = 1.800 \\text{ kg/s}$$",
                "explanation": "Because tension is constant throughout, impedance is directly proportional to the square root of linear density."
            },
            {
                "title": "Step 2: Amplitude coefficients and reflected/transmitted waves",
                "math": "$$r = \\frac{Z_1 - Z_2}{Z_1 + Z_2} = \\frac{1.200 - 1.800}{1.200 + 1.800} = \\frac{-0.600}{3.000} = -0.200$$\n$$t = \\frac{2 Z_1}{Z_1 + Z_2} = \\frac{2 \\times 1.200}{3.000} = \\frac{2.400}{3.000} = +0.800$$\n$$A_r = |r| A_i = 0.200 \\times 6.00 \\text{ mm} = 1.20 \\text{ mm (with } \\pi \\text{ phase shift)}$$\n$$A_t = t A_i = 0.800 \\times 6.00 \\text{ mm} = 4.80 \\text{ mm (in-phase)}$$",
                "explanation": "The reflected wave has amplitude 1.20 mm and undergoes an immediate 180° phase inversion at the denser junction."
            },
            {
                "title": "Step 3: Energy coefficients and power verification",
                "math": "$$R = r^2 = (-0.200)^2 = 0.0400 = 4.00\\%$$\n$$T_{trans} = \\frac{Z_2}{Z_1} t^2 = \\left( \\frac{1.800}{1.200} \\right) \\times (0.800)^2 = 1.500 \\times 0.640 = 0.9600 = 96.00\\%$$\n$$R + T_{trans} = 0.0400 + 0.9600 = 1.0000 = 100\\%$$",
                "explanation": "Exactly 4.00% of incident wave energy is reflected back into the steel wire, and 96.00% is successfully transmitted into the copper wire."
            }
        ]
    },
    {
        "id": "prob-7-2",
        "difficulty": "Standard Classical Exam Problem",
        "title": "Normal Modes of a Stretched Piano Wire",
        "question": "A steel piano wire of length $L = 0.850\\text{ m}$ has a mass of $M = 5.10\\text{ g}$. It is under tension $T = 720\\text{ N}$.\\n(a) Determine the fundamental frequency $f_1$ of the wire,\\n(b) Find the frequencies of the second and third overtones, and\\n(c) By what percentage must the tension be adjusted to increase the fundamental frequency by one semitone (a factor of $2^{1/12} \\approx 1.05946$)?",
        "steps": [
            {
                "title": "Step 1: Calculate linear density and fundamental frequency",
                "math": "$$\\mu = \\frac{M}{L} = \\frac{5.10 \\times 10^{-3} \\text{ kg}}{0.850 \\text{ m}} = 6.00 \\times 10^{-3} \\text{ kg/m}$$\n$$v = \\sqrt{\\frac{T}{\\mu}} = \\sqrt{\\frac{720}{6.00 \\times 10^{-3}}} = \\sqrt{120000} = 346.41 \\text{ m/s}$$\n$$f_1 = \\frac{v}{2L} = \\frac{346.41}{2 \\times 0.850} = \\frac{346.41}{1.700} = 203.77 \\text{ Hz}$$",
                "explanation": "The fundamental mode corresponds to a half-wavelength spanning the wire length."
            },
            {
                "title": "Step 2: Frequencies of overtones",
                "math": "$$\\text{Second Harmonic (1st overtone, } n = 2): f_2 = 2 f_1 = 2 \\times 203.77 = 407.54 \\text{ Hz}$$\n$$\\text{Third Harmonic (2nd overtone, } n = 3): f_3 = 3 f_1 = 3 \\times 203.77 = 611.31 \\text{ Hz}$$\n$$\\text{Fourth Harmonic (3rd overtone, } n = 4): f_4 = 4 f_1 = 4 \\times 203.77 = 815.08 \\text{ Hz}$$",
                "explanation": "For a fixed-fixed wire, overtones are exact integer multiples of the fundamental."
            },
            {
                "title": "Step 3: Tension adjustment for semitone pitch raise",
                "math": "$$f \\propto \\sqrt{T} \\implies \\frac{f'}{f} = \\sqrt{\\frac{T'}{T}} = 1.05946$$\n$$\\frac{T'}{T} = (1.05946)^2 = 1.12246$$\n$$\\Delta T = (1.12246 - 1) \\times 100\\% = +12.25\\%$$\n$$T' = 720 \\times 1.12246 = 808.2 \\text{ N}$$",
                "explanation": "Raising the pitch by one equal-tempered semitone requires increasing the string tension by 12.25% (to 808 N)."
            }
        ]
    },
    {
        "id": "prob-7-3",
        "difficulty": "Experimental Laboratory Exam Standard",
        "title": "Melde's Experiment: Fork Frequency and Loop Analysis",
        "question": "In a Melde's experiment configured in the transverse arrangement, a string of length $L = 1.80\\text{ m}$ vibrates in 4 resonant loops when a pan carrying mass $M_1 = 50.0\\text{ g}$ is suspended. When the mass is changed to $M_2$, the string vibrates in 5 resonant loops with the same tuning fork.\\n(a) State the relationship between the number of loops $p$ and suspended tension $T$, and determine mass $M_2$,\\n(b) If the linear density of the string is $\\mu = 2.45 \\times 10^{-4}\\text{ kg/m}$, calculate the frequency of the electrically maintained tuning fork. Take $g = 9.80\\text{ m/s}^2$.",
        "steps": [
            {
                "title": "Step 1: Relate loop count to tension",
                "math": "$$\\text{In transverse mode: } f = \\frac{p}{2L} \\sqrt{\\frac{T}{\\mu}} = \\text{constant}$$\n$$p \\sqrt{T} = \\text{constant} \\implies p^2 T = \\text{constant} \\implies p_1^2 M_1 = p_2^2 M_2$$\n$$M_2 = M_1 \\left(\\frac{p_1}{p_2}\\right)^2 = 50.0 \\text{ g} \\times \\left(\\frac{4}{5}\\right)^2 = 50.0 \\times 0.640 = 32.0 \\text{ g}$$",
                "explanation": "Because higher loop numbers require shorter wavelengths, the required tension scales inversely with $p^2$."
            },
            {
                "title": "Step 2: Determine tuning fork frequency",
                "math": "$$T_1 = M_1 g = (0.0500 \\text{ kg}) \\times 9.80 \\text{ m/s}^2 = 0.490 \\text{ N}$$\n$$v_1 = \\sqrt{\\frac{T_1}{\\mu}} = \\sqrt{\\frac{0.490}{2.45 \\times 10^{-4}}} = \\sqrt{2000} = 44.721 \\text{ m/s}$$\n$$f_{\\text{fork}} = \\frac{p_1 v_1}{2L} = \\frac{4 \\times 44.721}{2 \\times 1.80} = \\frac{178.885}{3.60} = 49.69 \\text{ Hz} \\approx 50.0 \\text{ Hz}$$",
                "explanation": "The tuning fork operates at 50 Hz (matching standard AC mains vibrator frequency)."
            },
            {
                "title": "Step 3: Verification with second state",
                "math": "$$T_2 = 0.0320 \\times 9.80 = 0.3136 \\text{ N}$$\n$$v_2 = \\sqrt{\\frac{0.3136}{2.45 \\times 10^{-4}}} = \\sqrt{1280} = 35.777 \\text{ m/s}$$\n$$f = \\frac{5 \\times 35.777}{2 \\times 1.80} = \\frac{178.885}{3.60} = 49.69 \\text{ Hz}$$",
                "explanation": "Both configurations yield identical frequency, confirming Melde's law $p^2 T = \\text{constant}$."
            }
        ]
    }
]

unit7_data = {
    "number": 7,
    "title": "Stationary Waves",
    "leadSummary": "A comprehensive analysis of wave reflection and transmission at media interfaces, impedance matching, standing wave kinematics, nodes and antinodes, normal modes and harmonic overtone spectra of stretched strings, acoustic pipe resonance with Rayleigh end corrections, Melde's experiment, and trapped energy dynamics.",
    "sections": u7_sections,
    "problems": u7_problems
}

with open("matter_u7.json", "w") as f:
    json.dump(unit7_data, f, indent=2)

print("Unit 7 built successfully with", len(u7_sections), "sections and", len(u7_problems), "solved problems!")

# =========================================================================
# UNIT 8: Sound Waves
# =========================================================================
u8_sections = [
    {
        "id": "sec-8-1",
        "number": "§8.1",
        "heading": "Intensity and Sound Intensity Levels: The Decibel Scale",
        "simulation": "sound-beats-doppler-sim",
        "content": """Sound is a mechanical longitudinal compression wave propagating through an elastic medium. Human auditory perception spans an extraordinary dynamic range of twelve orders of magnitude in acoustic power.

<h4>1. Acoustic Intensity</h4>
The <strong>acoustic intensity ($I$)</strong> is defined as the time-averaged sound energy transmitted per unit time across a unit area perpendicular to the direction of wave propagation (W/m²):
$$I = \\langle p(t) v(t) \\rangle = \\frac{p_0^2}{2 \\rho_0 c}$$
where:
<ul>
  <li>$p_0$: Maximum acoustic pressure amplitude (Pa).</li>
  <li>$\\rho_0$: Equilibrium medium density ($1.204 \\text{ kg/m}^3$ for dry air at 20°C).</li>
  <li>$c$: Speed of sound ($343.2 \\text{ m/s}$ in air at 20°C).</li>
  <li>$\\rho_0 c$: Specific acoustic impedance of air ($Z_0 \\approx 413 \\text{ Pa}\\cdot\\text{s/m} = 413 \\text{ Rayls}$).</li>
</ul>
The threshold of human hearing at 1000 Hz is internationally defined as the reference intensity:
$$I_0 = 1.00 \\times 10^{-12} \\text{ W/m}^2 \\quad (\\text{corresponding to } p_0 \\approx 20 \\ \\mu\\text{Pa})$$
The threshold of pain corresponds to $I \\approx 1.0 \\text{ W/m}^2$ ($p_0 \\approx 29 \\text{ Pa}$).

<h4>2. The Decibel (dB) Sound Level Scale</h4>
Because the human ear responds logarithmically (Weber-Fechner Law), acoustic levels are measured on the logarithmic <strong>Decibel Scale</strong>:
$$\\beta = 10 \\log_{10}\\left( \\frac{I}{I_0} \\right) \\quad (\\text{dB})$$
In terms of sound pressure level (SPL):
$$\\text{SPL} = 20 \\log_{10}\\left( \\frac{p_{\\text{rms}}}{p_{\\text{ref}}} \\right) \\quad (\\text{dB, with } p_{\\text{ref}} = 20 \\ \\mu\\text{Pa})$$
Key logarithmic benchmarks:
<ul>
  <li>Threshold of hearing ($I = I_0$): $\\beta = 10 \\log_{10}(1) = 0\\text{ dB}$.</li>
  <li>Whisper: $\\approx 20 - 30\\text{ dB}$.</li>
  <li>Normal conversation: $\\approx 60\\text{ dB}$.</li>
  <li>Heavy city traffic: $\\approx 80 - 85\\text{ dB}$.</li>
  <li>Rock concert / Jet engine takeoff at 50 m: $\\approx 120 - 130\\text{ dB}$ (threshold of pain).</li>
</ul>
<em>Rule of Thumb:</em>
<ul>
  <li>Doubling sound intensity ($I \\to 2I$) produces a $+3.01\\text{ dB}$ increase ($\Delta\\beta = 10\\log_{10} 2 = 3.01\\text{ dB}$).</li>
  <li>A tenfold increase in intensity ($I \\to 10I$) produces a $+10\\text{ dB}$ increase.</li>
</ul>"""
    },
    {
        "id": "sec-8-2",
        "number": "§8.2",
        "heading": "Loudness, Pitch, and Human Psychoacoustics",
        "simulation": "sound-beats-doppler-sim",
        "content": """Human auditory perception differentiates between physical stimulus parameters (intensity, frequency, spectral content) and subjective psychoacoustic sensations (loudness, pitch, timbre).

<h4>1. Pitch and Fundamental Frequency</h4>
<strong>Pitch</strong> is the subjective sensation that orders sounds on a musical frequency scale from low/bass to high/treble.
For pure sinusoidal tones, pitch is predominantly determined by frequency $f$.
For complex multi-harmonic musical tones, the human brain perceives the pitch corresponding to the fundamental frequency $f_1$, even if the fundamental physical harmonic is filtered out or missing (the <em>\"missing fundamental\"</em> psychoacoustic illusion).

<h4>2. Loudness and Equal-Loudness Contours (Fletcher-Munson Curves)</h4>
<strong>Loudness</strong> is the subjective psychological magnitude of sound sensation. The human ear does not exhibit a flat frequency response; it is most sensitive in the range $2000 - 5000\\text{ Hz}$ (due to acoustic resonance in the ear canal).
Harvey Fletcher and Wilden A. Munson (1933) established the standard <strong>Equal-Loudness Contours</strong>:
<ul>
  <li><strong>Phon Scale:</strong> A sound has a loudness level of $L$ phons if it is judged to be equally loud as a $1000\\text{ Hz}$ reference tone having a sound pressure level of $L$ dB.</li>
  <li><strong>Sone Scale:</strong> Developed by S. S. Stevens. 1 sone is defined as the loudness of a 1000 Hz tone at 40 dB SPL (40 phons).
  Subjective loudness doubles with every $+10\\text{ phon}$ increase:
  $$S = 2^{(L_{\\text{phon}} - 40)/10} \\quad (\\text{sones})$$</li>
</ul>

<h4>3. Timbre and Spectral Distribution</h4>
Timbre (tone quality) is the acoustic characteristic that enables a listener to distinguish between two musical instruments (e.g., a trumpet and an oboe) playing the exact same pitch at the exact same loudness.
Timbre is determined by:
<ul>
  <li>The relative amplitude and harmonic distribution of overtones (Fourier spectrum).</li>
  <li>Temporal envelope attack, decay, sustain, and release (ADSR) transients.</li>
</ul>"""
    },
    {
        "id": "sec-8-3",
        "number": "§8.3",
        "heading": "Spherical Waves in Three Dimensions and the Inverse-Square Law",
        "simulation": "sound-beats-doppler-sim",
        "content": """In an isotropic 3D medium, a point acoustic source radiates sound uniformly in all spatial directions.

<h4>1. The 3D Wave Equation in Spherical Coordinates</h4>
The linear acoustic wave equation in three dimensions is:
$$\\nabla^2 p = \\frac{1}{c^2} \\frac{\\partial^2 p}{\\partial t^2}$$
For a spherically symmetric wave where pressure depends only on radial distance $r$ from the source:
$$\\nabla^2 p = \\frac{1}{r^2} \\frac{\\partial}{\\partial r} \\left( r^2 \\frac{\\partial p}{\\partial r} \\right) = \\frac{1}{r} \\frac{\\partial^2 (r p)}{\\partial r^2}$$
Substituting into the wave equation:
$$\\frac{\\partial^2 (r p)}{\\partial r^2} = \\frac{1}{c^2} \\frac{\\partial^2 (r p)}{\\partial t^2}$$
Defining the auxiliary variable $\\psi(r, t) = r p(r, t)$, this reduces to the 1D classical wave equation!
The general solution for outgoing expanding spherical waves is:
$$p(r, t) = \\frac{A}{r} \\cos(k r - \\omega t + \\phi)$$
<em>Critical Consequence:</em> The pressure amplitude of a spherical wave decreases inversely with radial distance:
$$p_0(r) \\propto \\frac{1}{r}$$

<h4>2. The Inverse-Square Law of Acoustic Intensity</h4>
Because acoustic intensity is proportional to pressure amplitude squared ($I \\propto p_0^2$):
$$I(r) = \\frac{P_{\\text{source}}}{4\\pi r^2} \\propto \\frac{1}{r^2}$$
where $P_{\\text{source}}$ is the total acoustic power output of an omnidirectional point source (Watts).
Intensity obeys the <strong>Inverse-Square Law</strong>:
$$\\frac{I_2}{I_1} = \\left(\\frac{r_1}{r_2}\\right)^2$$
On the decibel scale, doubling the distance from a point source reduces the sound level by exactly $6.02\\text{ dB}$:
$$\\beta_2 - \\beta_1 = 10 \\log_{10}\\left( \\frac{I_2}{I_1} \\right) = 10 \\log_{10}\\left( \\frac{r_1}{r_2} \\right)^2 = 20 \\log_{10}\\left( \\frac{r_1}{r_2} \\right) = 20 \\log_{10}(0.5) = -6.02\\text{ dB}$$"""
    },
    {
        "id": "sec-8-4",
        "number": "§8.4",
        "heading": "Interference, Diffraction, and Radiation Efficiency of Sound Sources",
        "simulation": "sound-beats-doppler-sim",
        "content": """Acoustic waves exhibit classical interference and diffraction phenomena governed by wave superposition and boundary conditions.

<h4>1. Interference of Coherent Sound Waves</h4>
When two coherent loudspeakers emit sound waves of wavelength $\\lambda$, the resultant pressure amplitude at observation point $P$ separated from the sources by paths $r_1$ and $r_2$ is:
$$\\Delta r = |r_1 - r_2|$$
<ul>
  <li><strong>Constructive Interference (Maximum Loudness):</strong>
  $$\\Delta r = n \\lambda, \\quad n = 0, 1, 2, \\dots$$</li>
  <li><strong>Destructive Interference (Silence / Minimum):</strong>
  $$\\Delta r = \\left(n + \\frac{1}{2}\\right) \\lambda$$</li>
</ul>
<em>Quincke's Interference Tube:</em> Sound enters a branch split into two paths of lengths $L_1$ and $L_2$. Sliding one tube by $\\Delta L$ produces constructive or destructive interference at the listener's ear, allowing direct precision measurement of acoustic wavelength $\\lambda = 2 \\Delta L$.

<h4>2. Diffraction of Sound Waves</h4>
Sound waves diffract around obstacles and through doorways because their acoustic wavelengths ($\\lambda \\sim 0.1 - 3\\text{ m}$) are comparable to everyday architectural dimensions ($D \\sim 1\\text{ m}$).
By Airy's circular aperture diffraction formula:
$$\\sin\\theta \\approx 1.22 \\frac{\\lambda}{D}$$
<ul>
  <li><strong>Low-frequency bass notes (100 Hz, $\lambda = 3.4\text{ m}$):</strong> $\lambda \\gg D$, sound bends around obstacles into acoustic shadow zones.</li>
  <li><strong>High-frequency treble notes (10 kHz, $\lambda = 3.4\text{ cm}$):</strong> $\lambda \\ll D$, sound forms sharp directional beams and geometric acoustic shadows.</li>
</ul>

<h4>3. Radiation Efficiency of Acoustic Sources</h4>
The ability of a vibrating body to convert mechanical vibrational power into acoustic radiated power is quantified by its <strong>radiation efficiency</strong>:
$$\\eta_{rad} = \\frac{R_{rad}}{\\rho_0 c A}$$
where $R_{rad}$ is the real acoustic radiation resistance.
<ul>
  <li><strong>Monopole (Pulsating sphere):</strong> Net volume displacement changes. High acoustic radiation efficiency at low frequencies.</li>
  <li><strong>Dipole (Unbaffled vibrating loudspeaker cone):</strong> Two out-of-phase pulsating sources separated by small distance. Air simply sloshes back and forth between front and back without radiating efficiently. Installing a baffle board or enclosed cabinet prevents dipole cancellation, dramatically boosting bass output!</li>
</ul>"""
    },
    {
        "id": "sec-8-5",
        "number": "§8.5",
        "heading": "Acoustic Beats and Combination Tones",
        "simulation": "sound-beats-doppler-sim",
        "content": """When two sound waves of slightly different frequencies are sounded simultaneously, the human ear perceives acoustic beats and combination tones.

<h4>1. Mathematical Theory of Beats</h4>
Consider two acoustic pressure signals of equal amplitude $p_0$ and neighboring frequencies $f_1$ and $f_2$ ($f_1 \\approx f_2$):
$$p_1(t) = p_0 \\cos(2\\pi f_1 t), \\quad p_2(t) = p_0 \\cos(2\\pi f_2 t)$$
By superposition:
$$p(t) = p_1(t) + p_2(t) = 2 p_0 \\cos\\left[ 2\\pi \\left( \\frac{f_1 - f_2}{2} \\right) t \\right] \\cos\\left[ 2\\pi \\left( \\frac{f_1 + f_2}{2} \\right) t \\right]$$
The resultant wave represents a carrier vibration at the average frequency $\\bar{f} = \\frac{f_1 + f_2}{2}$ whose envelope amplitude is slowly modulated:
$$A_{\\text{mod}}(t) = 2 p_0 \\left| \\cos\\left( \\pi (f_1 - f_2) t \\right) \\right|$$
Since acoustic intensity is proportional to amplitude squared:
$$I(t) \\propto A_{\\text{mod}}^2(t) = 4 p_0^2 \\cos^2\\left( \\pi (f_1 - f_2) t \\right) = 2 p_0^2 \\left[ 1 + \\cos\\left( 2\\pi (f_1 - f_2) t \\right) \\right]$$
The intensity surges from 0 to $4 p_0^2$ at a rate called the <strong>Beat Frequency ($f_{\\text{beat}}$)</strong>:
$$f_{\\text{beat}} = |f_1 - f_2|$$
Piano tuners adjust wire tension until beat frequency drops to zero, achieving unison tuning.

<h4>2. Tartini Combination Tones</h4>
In 1714, Italian violinist Giuseppe Tartini discovered that when two loud, pure tones of frequencies $f_1$ and $f_2$ ($f_2 > f_1$) are sounded together, the ear perceives additional tones that are not physically present in the acoustic sound field!
These are <strong>subjective combination tones</strong> generated by the non-linear elasticity of the human eardrum and cochlea:
$$x_{\\text{cochlea}} = a_1 p + a_2 p^2 + a_3 p^3 + \\dots$$
When $p = p_1 \\cos(\\omega_1 t) + p_2 \\cos(\\omega_2 t)$, the quadratic term $p^2$ yields:
$$p^2 = \\frac{1}{2}p_1^2 + \\frac{1}{2}p_2^2 + \\frac{1}{2}p_1^2 \\cos(2\\omega_1 t) + \\frac{1}{2}p_2^2 \\cos(2\\omega_2 t) + p_1 p_2 [\\cos((\\omega_2 - \\omega_1)t) + \\cos((\\omega_2 + \\omega_1)t)]$$
This generates:
<ul>
  <li><strong>Difference Tone (Tartini Tone):</strong> $f_{\\text{diff}} = f_2 - f_1$ (very prominent, used by organ builders to generate deep 32-foot bass notes using smaller 16-foot pipes).</li>
  <li><strong>Summation Tone:</strong> $f_{\\text{sum}} = f_1 + f_2$ (fainter, higher in pitch).</li>
  <li><strong>Cubic Combination Tones:</strong> $2f_1 - f_2$ and $2f_2 - f_1$ arising from the cubic term $a_3 p^3$.</li>
</ul>"""
    },
    {
        "id": "sec-8-6",
        "number": "§8.6",
        "heading": "The Doppler Effect and Supersonic Shock Waves",
        "simulation": "sound-beats-doppler-sim",
        "content": """Christian Doppler (1842) demonstrated that the observed frequency of a wave depends on the relative motion between the wave source, the observer, and the propagating medium.

<h4>1. The Classical Acoustic Doppler Equation</h4>
Let:
<ul>
  <li>$c$: Speed of sound in the still medium.</li>
  <li>$v_s$: Velocity of the sound source along the line connecting source and observer (positive when moving toward observer).</li>
  <li>$v_o$: Velocity of the observer along the connecting line (positive when moving toward source).</li>
  <li>$v_w$: Velocity of wind/medium along the line of propagation.</li>
  <li>$f_0$: Emitted source frequency.</li>
</ul>
The general observed frequency $f'$ is:
$$f' = f_0 \\left( \\frac{c \\pm v_o}{c \\mp v_s} \\right)$$
Sign conventions:
<ul>
  <li><strong>Observer moving toward stationary source ($v_o > 0, v_s = 0$):</strong> Observer intercepts more wavefronts per second:
  $$f' = f_0 \\left( \\frac{c + v_o}{c} \\right) > f_0$$</li>
  <li><strong>Source moving toward stationary observer ($v_s > 0, v_o = 0$):</strong> Wavefronts are compressed ahead of the source ($\lambda' = \frac{c - v_s}{f_0}$):
  $$f' = f_0 \\left( \\frac{c}{c - v_s} \\right) > f_0$$</li>
  <li><strong>Approaching systems:</strong> Frequency shifts higher (blueshift).</li>
  <li><strong>Receding systems:</strong> Frequency shifts lower (redshift).</li>
</ul>

<h4>2. Supersonic Motion and Mach Shock Waves</h4>
When the source speed $v_s$ equals the speed of sound $c$ ($M = v_s / c = 1$), wavefronts pile up ahead of the source into a singular pressure barrier.
When the source travels faster than sound ($M > 1$, supersonic):
The circular wavefronts emitted at successive positions lag behind the source, and their envelope forms a conical wavefront called the <strong>Mach Cone</strong>:
The half-angle of the cone (<strong>Mach Angle $\theta$</strong>) is:
$$\\sin\\theta = \\frac{c t}{v_s t} = \\frac{c}{v_s} = \\frac{1}{M}$$
Across this conical discontinuity, pressure, density, and temperature jump discontinuously.
When this conical shock front sweeps past an observer on the ground, the abrupt double pressure jump produces an explosive <strong>Sonic Boom</strong>.

<h4>3. Modern Technical Applications of the Doppler Effect</h4>
<ul>
  <li><strong>Medical Color Doppler Echocardiography:</strong> Measures blood flow velocity and detects heart valve regurgitation non-invasively via ultrasound reflected from erythrocytes.</li>
  <li><strong>Radar Speed Guns:</strong> Police microwave radar detects vehicle speed via $\Delta f = \frac{2 v}{c} f_0$.</li>
  <li><strong>Astronomical Redshifts:</strong> Hubble's discovery of cosmic expansion via Doppler redshift of spectral absorption lines in distant galaxies.</li>
</ul>"""
    }
]

u8_problems = [
    {
        "id": "prob-8-1",
        "difficulty": "Undergraduate Classical Exam Standard",
        "title": "Decibel Sound Intensity Addition and Distance Attenuation",
        "question": "A small construction generator acts as an omnidirectional point acoustic source radiating sound power $P_{\\text{sound}} = 0.500\\text{ W}$ in an open field.\\n(a) Determine the acoustic intensity $I$ and sound level $\\beta$ at distance $r_1 = 5.00\\text{ m}$,\\n(b) Find the sound level $\\beta_2$ at distance $r_2 = 25.0\\text{ m}$, and\\n(c) If four identical generators operate simultaneously at the original location, what is the combined sound level in decibels at $r_1 = 5.00\\text{ m}$? Take $I_0 = 1.00 \\times 10^{-12}\\text{ W/m}^2$.",
        "steps": [
            {
                "title": "Step 1: Calculate intensity and sound level at 5.00 m",
                "math": "$$I_1 = \\frac{P_{\\text{sound}}}{4\\pi r_1^2} = \\frac{0.500}{4\\pi \\times (5.00)^2} = \\frac{0.500}{100\\pi} = \\frac{0.500}{314.16} = 1.5915 \\times 10^{-3} \\text{ W/m}^2$$\n$$\\beta_1 = 10 \\log_{10}\\left( \\frac{I_1}{I_0} \\right) = 10 \\log_{10}\\left( \\frac{1.5915 \\times 10^{-3}}{1.00 \\times 10^{-12}} \\right) = 10 \\log_{10}(1.5915 \\times 10^9)$$\n$$\\beta_1 = 10 \\times (9 + \\log_{10} 1.5915) = 10 \\times (9 + 0.2018) = 92.02 \\text{ dB}$$",
                "explanation": "At 5.0 m, the generator produces a loud industrial level of 92.0 dB."
            },
            {
                "title": "Step 2: Attenuation over distance to 25.0 m",
                "math": "$$\\beta_2 = \\beta_1 - 20 \\log_{10}\\left(\\frac{r_2}{r_1}\\right) = 92.02 - 20 \\log_{10}\\left(\\frac{25.0}{5.00}\\right) = 92.02 - 20 \\log_{10}(5)$$\n$$\\beta_2 = 92.02 - 20 \\times 0.69897 = 92.02 - 13.98 = 78.04 \\text{ dB}$$",
                "explanation": "Increasing the distance fivefold reduces the sound level by 14.0 dB to 78.0 dB."
            },
            {
                "title": "Step 3: Superposition of four identical incoherent sources",
                "math": "$$I_{\\text{tot}} = 4 I_1$$\n$$\\beta_{\\text{tot}} = \\beta_1 + 10 \\log_{10}(4) = 92.02 + 10 \\times 0.60206 = 92.02 + 6.02 = 98.04 \\text{ dB}$$",
                "explanation": "Quadrupling the acoustic power adds $+6.02$ dB, raising the level to 98.0 dB."
            }
        ]
    },
    {
        "id": "prob-8-2",
        "difficulty": "Precision Acoustic Calibration Problem",
        "title": "Acoustic Beats and Tuning Fork Calibration",
        "question": "A standard calibration tuning fork $A$ has a known frequency $f_A = 440.0\\text{ Hz}$. When sounded simultaneously with an unknown fork $B$, $4.00\\text{ beats per second}$ are heard. When a small piece of beeswax is attached to the prong of fork $B$ (which increases its effective inertia), the beat frequency decreases to $2.00\\text{ beats per second}$.\\n(a) Explain why attaching wax alters the frequency of fork $B$,\\n(b) Determine the exact original frequency $f_B$ of fork $B$, and\\n(c) What would happen to the beat frequency if even more wax were added until $f_B$ drops further by $4.00\\text{ Hz}$?",
        "steps": [
            {
                "title": "Step 1: Frequency candidates from initial beat frequency",
                "math": "$$f_{\\text{beat}} = |f_A - f_B| = 4.00 \\text{ Hz}$$\n$$f_B = f_A \\pm 4.00 = 440.0 \\pm 4.00 \\implies f_B = 444.0 \\text{ Hz} \\quad \\text{or} \\quad 436.0 \\text{ Hz}$$",
                "explanation": "Initial beat frequency yields two possible mathematical solutions: 444.0 Hz or 436.0 Hz."
            },
            {
                "title": "Step 2: Effect of mass loading and unique identification",
                "math": "$$f_{\\text{fork}} = \\frac{1}{2\\pi} \\sqrt{\\frac{k}{m}} \\implies \\frac{df}{dm} < 0$$\n$$\\text{Adding wax increases mass, so } f_B' < f_B$$\n$$\\text{If } f_B = 436.0 \\text{ Hz}: \\text{ lowering it would yield } f_B' < 436.0 \\implies |440.0 - f_B'| > 4.00 \\text{ Hz (beat rate increases).}$$\n$$\\text{If } f_B = 444.0 \\text{ Hz}: \\text{ lowering it toward 440 Hz yields } |440.0 - f_B'| < 4.00 \\text{ Hz (beat rate decreases).}$$\n$$\\text{Because the observed beat frequency dropped to } 2.00 \\text{ Hz}, \\text{ the true original frequency was:}$$\n$$f_B = 444.0 \\text{ Hz}$$",
                "explanation": "Because adding inertia lowered the beat count, $f_B$ must have been initially higher than 440 Hz."
            },
            {
                "title": "Step 3: Further wax addition analysis",
                "math": "$$f_B'' = 442.0 - 4.00 = 438.0 \\text{ Hz}$$\n$$f_{\\text{beat}}'' = |440.0 - 438.0| = 2.00 \\text{ Hz}$$",
                "explanation": "Adding more wax lowers $f_B$ through unison (0 beats at 440 Hz) down to 438 Hz, where beats reappear at 2.0 Hz."
            }
        ]
    },
    {
        "id": "prob-8-3",
        "difficulty": "Honors Doppler Effect Exam Standard",
        "title": "Doppler Shift with Reflected Acoustic Echo and Beats",
        "question": "A train locomotive moves at constant speed $v_s = 20.0\\text{ m/s}$ directly toward a sheer vertical rock cliff. The locomotive engineer sounds the train whistle at frequency $f_0 = 500.0\\text{ Hz}$. The speed of sound in still air is $c = 340.0\\text{ m/s}$.\\n(a) What frequency $f_{\\text{cliff}}$ is received by a stationary observer standing at the base of the cliff?\\n(b) What frequency $f'_{\\text{echo}}$ of the reflected echo is heard by the train engineer aboard the moving locomotive?\\n(c) What beat frequency $f_{\\text{beat}}$ does the engineer hear between the direct whistle and the reflected echo from the cliff?",
        "steps": [
            {
                "title": "Step 1: Frequency incident on the cliff",
                "math": "$$f_{\\text{cliff}} = f_0 \\left( \\frac{c}{c - v_s} \\right) = 500.0 \\times \\left( \\frac{340.0}{340.0 - 20.0} \\right) = 500.0 \\times \\frac{340.0}{320.0} = 500.0 \\times 1.0625 = 531.25 \\text{ Hz}$$",
                "explanation": "Wavefronts are compressed ahead of the moving locomotive, striking the cliff at 531.25 Hz."
            },
            {
                "title": "Step 2: Frequency of reflected echo received by the engineer",
                "math": "$$\\text{The cliff acts as a stationary source re-radiating sound at } f_{\\text{cliff}} = 531.25 \\text{ Hz}.$$\n$$\\text{The engineer is an observer moving toward this stationary source with speed } v_o = v_s = 20.0 \\text{ m/s}:$$\n$$f'_{\\text{echo}} = f_{\\text{cliff}} \\left( \\frac{c + v_s}{c} \\right) = f_0 \\left( \\frac{c + v_s}{c - v_s} \\right)$$\n$$f'_{\\text{echo}} = 500.0 \\times \\left( \\frac{340.0 + 20.0}{340.0 - 20.0} \\right) = 500.0 \\times \\frac{360.0}{320.0} = 500.0 \\times 1.125 = 562.50 \\text{ Hz}$$",
                "explanation": "Because the engineer is in motion both when emitting and when intercepting the echo, the Doppler factor applies twice."
            },
            {
                "title": "Step 3: Beat frequency heard by the engineer",
                "math": "$$f_{\\text{beat}} = f'_{\\text{echo}} - f_0 = 562.50 - 500.0 = 62.50 \\text{ Hz}$$",
                "explanation": "The direct whistle (500 Hz) and reflected echo (562.5 Hz) superpose to produce a distinct rapid beat frequency of 62.5 Hz."
            }
        ]
    }
]

unit8_data = {
    "number": 8,
    "title": "Sound Waves",
    "leadSummary": "A comprehensive physical and psychoacoustic study of sound waves, decibel intensity levels, human pitch and loudness perception, 3D spherical wavefront propagation, inverse-square law, interference and diffraction, acoustic radiation efficiency, beats, Tartini combination tones, Doppler frequency shifts, and supersonic Mach shock cones.",
    "sections": u8_sections,
    "problems": u8_problems
}

with open("matter_u8.json", "w") as f:
    json.dump(unit8_data, f, indent=2)

print("Unit 8 built successfully with", len(u8_sections), "sections and", len(u8_problems), "solved problems!")
