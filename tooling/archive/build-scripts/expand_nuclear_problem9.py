# -*- coding: utf-8 -*-
"""
expand_nuclear_problem9.py
Injects Problem 9 across all 10 units for Nuclear and Radiochemistry (#47),
bringing total problems from 80 to 90 (9 per unit).
Strictly Zero Course Numbers or Marks.
"""

def add_problem_9_to_units(units):
    prob9_data = {
        1: {
            "id": "prob-1-9",
            "problemNumber": "1.9",
            "title": "Thomson Diffuse Model Versus Rutherford Nuclear Scattering Probability",
            "difficulty": "Advanced",
            "statement": r"""In J.J. Thomson's plum pudding model, an atom of gold ($Z = 79, R = 1.0 \times 10^{-10}\text{ m}$) had positive charge distributed uniformly throughout its volume.
1. Show that the maximum deflection angle $\theta_{\max}$ for a single encounter of a $5.0\text{ MeV}$ alpha particle traversing a Thomson gold atom is $\theta_{\max} \approx 2.0 \times 10^{-4}\text{ radians} \approx 0.011^\circ$.
2. In traversing a foil of $N_{\text{layers}} = 2,000$ atoms, the net deflection is a random walk with root-mean-square deflection $\theta_{\text{rms}} = \sqrt{N} \theta_1 \approx 0.5^\circ$.
3. Compute the Gaussian probability $P(\theta > 90^\circ) = \exp(-[\theta / \theta_{\text{rms}}]^2)$ under Thomson's model and explain why Rutherford's observation of wide-angle scattering refuted the diffuse atomic model.""",
            "solution": r"""### Step 1: Thomson Maximum Single Deflection
The maximum transverse electric field inside a uniformly charged sphere of radius $R$ occurs at the surface:
$$E_{\max} = \frac{1}{4\pi\varepsilon_0} \frac{Z e}{R^2} = \frac{(8.988 \times 10^9)(79)(1.602 \times 10^{-19})}{(1.0 \times 10^{-10})^2} \approx 1.137 \times 10^{13}\text{ N/C}$$
The transverse force on an alpha particle ($q = 2e$) is:
$$F_\perp \approx 2e E_{\max} = 2(1.602 \times 10^{-19})(1.137 \times 10^{13}) \approx 3.64 \times 10^{-6}\text{ N}$$
Transit time across the atom ($v_\alpha \approx 1.55 \times 10^7\text{ m/s}$):
$$\Delta t \approx \frac{2R}{v_\alpha} = \frac{2.0 \times 10^{-10}\text{ m}}{1.55 \times 10^7\text{ m/s}} \approx 1.29 \times 10^{-17}\text{ s}$$
Transverse momentum impulse:
$$\Delta p_\perp \approx F_\perp \Delta t \approx (3.64 \times 10^{-6}\text{ N})(1.29 \times 10^{-17}\text{ s}) \approx 4.70 \times 10^{-23}\text{ kg}\cdot\text{m/s}$$
Forward momentum:
$$p_\parallel = m_\alpha v_\alpha = (6.645 \times 10^{-27}\text{ kg})(1.55 \times 10^7\text{ m/s}) \approx 1.03 \times 10^{-19}\text{ kg}\cdot\text{m/s}$$
Maximum single deflection angle:
$$\theta_1 \approx \frac{\Delta p_\perp}{p_\parallel} \approx \frac{4.70 \times 10^{-23}}{1.03 \times 10^{-19}} \approx 4.56 \times 10^{-4}\text{ rad} \approx 0.026^\circ$$

### Step 2: Multiple Scattering Random Walk
After traversing $2,000$ independent random deflections:
$$\theta_{\text{rms}} \approx \sqrt{2000} \times 0.026^\circ \approx 44.72 \times 0.026^\circ \approx 1.16^\circ \approx 0.020\text{ rad}$$

### Step 3: Probability of $90^\circ$ Deflection Under Thomson's Model
The probability of a deflection exceeding $\theta = 90^\circ = 1.571\text{ rad}$ in a Gaussian distribution is:
$$P(\theta > 90^\circ) \sim \exp\left( -\left[\frac{\theta}{\theta_{\text{rms}}}\right]^2 \right) = \exp\left( -\left[\frac{1.571}{0.020}\right]^2 \right) = \exp\left( -(78.5)^2 \right) = \exp(-6162) \approx 10^{-2676}$$
The probability is less than **$10^{-2600}$**—impossible in the lifetime of the universe!
Yet Geiger and Marsden observed deflections $>90^\circ$ in **$1$ out of every $8,000$** alpha particles ($P \approx 1.25 \times 10^{-4}$). This discrepancy refuted the Thomson model and proved the positive charge is concentrated in a point-like nucleus.""",
            "hints": ["Calculate the maximum transverse impulse delta p = F * delta t in the Thomson sphere.", "Show that multiple random scattering predicts a negligible Gaussian tail for 90-degree deflections."]
        },
        2: {
            "id": "prob-2-9",
            "problemNumber": "2.9",
            "title": "Deuteron Non-Spherical Quadrupole Moment and Tensor Force D-State Mixing",
            "difficulty": "Advanced",
            "statement": r"""The deuteron ($^2_1\text{H}$) is the simplest bound nuclear system ($Z = 1, N = 1$, binding energy $B = 2.2246\text{ MeV}$, spin-parity $J^\pi = 1^+$).
1. If the nuclear force were purely central (spherical), the deuteron ground state would be a pure orbital S-wave ($l = 0, ^3S_1$). Show that a pure S-state must have an electric quadrupole moment $Q = 0$.
2. The measured electric quadrupole moment of the deuteron is $Q_{\text{exp}} = +0.00286\text{ barn} = +0.286\text{ fm}^2$.
Explain how this non-zero, positive quadrupole moment proves the existence of a non-central **tensor nuclear force** and mixing with an orbital D-state ($l = 2, ^3D_1$).
3. If the wave function is $|\psi\rangle = a_S |^3S_1\rangle + a_D |^3D_1\rangle$, state the approximate percentage of D-state admixture ($a_D^2 \approx 4 - 6\%$).""",
            "solution": r"""### Step 1: Quadrupole Moment of a Pure S-State
The electric quadrupole moment operator is defined as:
$$\hat{Q} = \frac{1}{e} \int \rho(\vec{r}) (3 z^2 - r^2) d^3r = \sqrt{\frac{16\pi}{5}} \int \rho(\vec{r}) r^2 Y_{20}(\theta, \phi) d^3r$$
For a pure S-state ($l = 0$), the spatial wave function is spherically symmetric:
$$|\psi_S|^2 = \frac{|u(r)|^2}{4\pi}$$
Evaluating the angular integral:
$$\int_{4\pi} Y_{20}(\Omega) d\Omega = 0$$
Due to spherical symmetry, $\langle 3 z^2 - r^2 \rangle = 0$. Therefore, **any pure S-state has an electric quadrupole moment $Q \equiv 0$**.

### Step 2: Proof of Non-Central Tensor Force
Because the experimental quadrupole moment is finite and positive ($Q = +0.286\text{ fm}^2$):
1. The charge distribution of the deuteron is **prolate** (cigar-shaped, elongated along the spin axis).
2. The nuclear force is **non-central**: it contains a **tensor force** $\hat{S}_{12}$:
$$\hat{S}_{12} = \frac{3}{r^2} (\vec{\sigma}_1 \cdot \vec{r})(\vec{\sigma}_2 \cdot \vec{r}) - (\vec{\sigma}_1 \cdot \vec{\sigma}_2)$$
3. The tensor force mixes states with identical total angular momentum $J = 1$ and parity $\pi = (-1)^l = +1$, coupling the dominant $l = 0$ ($^3S_1$) state with the $l = 2$ ($^3D_1$) state:
$$|\psi_D\rangle = a_S |^3S_1\rangle + a_D |^3D_1\rangle$$

### Step 3: D-State Admixture
The interference between the S and D wave functions produces the quadrupole moment:
$$Q \approx \frac{\sqrt{2}}{10} a_S a_D \int_0^\infty r^2 u_S(r) u_D(r) dr$$
Modern nucleon-nucleon potential models (Argonne $v_{18}$, CD-Bonn) determine that the deuteron ground state contains approximately **$4.5\%$ to $5.8\%$ D-state admixture** ($a_D^2 \approx 0.05$). The deuteron is not spherical!""",
            "hints": ["S-states have spherical symmetry l = 0, giving zero quadrupole moment.", "A non-zero quadrupole moment requires tensor force mixing with an l = 2 D-state."]
        },
        3: {
            "id": "prob-3-9",
            "problemNumber": "3.9",
            "title": "Laplace Transform Solution of Two-Step Successive Decay Chain",
            "difficulty": "Intermediate",
            "statement": r"""Solve the successive radioactive decay chain $N_1 \xrightarrow{\lambda_1} N_2 \xrightarrow{\lambda_2} N_3$ using **Laplace transforms**.
Initial conditions: $N_1(0) = N_1^0$ and $N_2(0) = 0$.
1. Transform the coupled differential equations into the algebraic $s$-domain:
$$\mathcal{L}\left\{\frac{dN_1}{dt}\right\} = s \tilde{N}_1(s) - N_1^0 = -\lambda_1 \tilde{N}_1(s)$$
$$\mathcal{L}\left\{\frac{dN_2}{dt}\right\} = s \tilde{N}_2(s) - 0 = \lambda_1 \tilde{N}_1(s) - \lambda_2 \tilde{N}_2(s)$$
2. Solve algebraically for $\tilde{N}_2(s)$ in the $s$-domain.
3. Use partial fraction expansion and inverse Laplace transformation $\mathcal{L}^{-1}\{1/(s+a)\} = e^{-at}$ to recover the Bateman daughter equation.""",
            "solution": r"""### Step 1: Solve for $\tilde{N}_1(s)$ in the $s$-Domain
$$(s + \lambda_1) \tilde{N}_1(s) = N_1^0 \implies \tilde{N}_1(s) = \frac{N_1^0}{s + \lambda_1}$$

### Step 2: Solve for $\tilde{N}_2(s)$
$$(s + \lambda_2) \tilde{N}_2(s) = \lambda_1 \tilde{N}_1(s) = \frac{\lambda_1 N_1^0}{s + \lambda_1}$$
$$\tilde{N}_2(s) = \frac{\lambda_1 N_1^0}{(s + \lambda_1)(s + \lambda_2)}$$

### Step 3: Partial Fraction Decomposition and Inversion
Expand $\tilde{N}_2(s)$ into partial fractions:
$$\frac{1}{(s + \lambda_1)(s + \lambda_2)} = \frac{A}{s + \lambda_1} + \frac{B}{s + \lambda_2}$$
Multiply by $(s + \lambda_1)(s + \lambda_2)$:
$$1 = A(s + \lambda_2) + B(s + \lambda_1)$$
- Setting $s = -\lambda_1$: $1 = A(\lambda_2 - \lambda_1) \implies A = \frac{1}{\lambda_2 - \lambda_1}$
- Setting $s = -\lambda_2$: $1 = B(\lambda_1 - \lambda_2) \implies B = -\frac{1}{\lambda_2 - \lambda_1}$

Substitute coefficients:
$$\tilde{N}_2(s) = \frac{\lambda_1 N_1^0}{\lambda_2 - \lambda_1} \left[ \frac{1}{s + \lambda_1} - \frac{1}{s + \lambda_2} \right]$$
Taking the inverse Laplace transform:
$$\mathcal{L}^{-1}\left\{\frac{1}{s + \lambda}\right\} = e^{-\lambda t}$$
$$N_2(t) = \frac{\lambda_1 N_1^0}{\lambda_2 - \lambda_1} \left( e^{-\lambda_1 t} - e^{-\lambda_2 t} \right)$$
The Laplace transform method derives the Bateman equation directly without guessing integrating factors!""",
            "hints": ["Laplace transform of dN/dt is s*N(s) - N(0).", "Decompose the product 1 / [(s + lambda_1)(s + lambda_2)] into partial fractions."]
        },
        4: {
            "id": "prob-4-9",
            "problemNumber": "4.9",
            "title": "Breit-Wigner Interference Between Resonant and Potential Elastic Scattering",
            "difficulty": "Advanced",
            "statement": r"""In low-energy neutron elastic scattering $(n, n)$, the total scattering amplitude $f(\theta)$ is the coherent quantum sum of two amplitudes:
1. Hard-sphere potential scattering amplitude: $f_{\text{pot}} = -R$ (where $R$ is the nuclear radius).
2. Resonance Breit-Wigner scattering amplitude: $f_{\text{res}} = -\frac{\lambdabar \Gamma_n / 2}{E - E_0 + i\Gamma/2}$.
1. Formulate the total elastic cross-section $\sigma_{\text{sc}}(E) = 4\pi |f_{\text{pot}} + f_{\text{res}}|^2$.
2. Show that quantum interference produces an asymmetric cross-section profile (Fano resonance) with a deep destructive interference minimum on the low-energy side of the resonance ($E < E_0$).""",
            "solution": r"""### Step 1: Coherent Scattering Cross-Section
The total scattering amplitude is:
$$f(E) = -R - \frac{\lambdabar \Gamma_n / 2}{E - E_0 + i\Gamma/2}$$
Multiplying numerator and denominator of the resonant term by $(E - E_0 - i\Gamma/2)$:
$$f(E) = -R - \frac{\lambdabar \Gamma_n (E - E_0)}{2 [(E - E_0)^2 + \Gamma^2/4]} + i \frac{\lambdabar \Gamma_n \Gamma / 4}{(E - E_0)^2 + \Gamma^2/4}$$
Total scattering cross-section $\sigma_{\text{sc}} = 4\pi |f(E)|^2$:
$$\sigma_{\text{sc}}(E) = 4\pi \left[ \left( R + \frac{\lambdabar \Gamma_n (E - E_0) / 2}{(E - E_0)^2 + \Gamma^2/4} \right)^2 + \left( \frac{\lambdabar \Gamma_n \Gamma / 4}{(E - E_0)^2 + \Gamma^2/4} \right)^2 \right]$$

Expanding the square:
$$\sigma_{\text{sc}}(E) = 4\pi R^2 + \frac{\pi \lambdabar^2 \Gamma_n^2}{(E - E_0)^2 + \Gamma^2/4} + \frac{4\pi R \lambdabar \Gamma_n (E - E_0)}{(E - E_0)^2 + \Gamma^2/4}$$
- The first term is the constant potential scattering cross-section $\sigma_{\text{pot}} = 4\pi R^2$.
- The second term is the symmetric Breit-Wigner resonance peak.
- The third term is the **Quantum Interference Term**!

### Step 2: Destructive Interference Minimum
Notice the sign of the interference term:
- For $E > E_0$: $(E - E_0) > 0$, constructive interference enhances the cross-section.
- For $E < E_0$: $(E - E_0) < 0$, destructive interference depresses the cross-section.

At an energy just below resonance:
$$E_{\min} \approx E_0 - \frac{\lambdabar \Gamma_n}{2 R}$$
The potential scattering amplitude and resonance amplitude have opposite signs and cancel each other destructively! The cross-section drops to a deep minimum near zero (the "resonance dip"). This asymmetry is ubiquitous in neutron transmission spectra.""",
            "hints": ["Add the amplitudes coherently before squaring to get cross-section: sigma = 4*pi*|f_pot + f_res|^2.", "The interference term changes sign as (E - E_0) passes through zero."]
        },
        5: {
            "id": "prob-5-9",
            "problemNumber": "5.9",
            "title": "Thermal Reactor Critical Size and Buckling for Spherical Core",
            "difficulty": "Intermediate",
            "statement": r"""A bare, unreflected spherical nuclear reactor core has an infinite multiplication factor $k_\infty = 1.080$ and a neutron migration area $M^2 = 32.0\text{ cm}^2$.
1. Using one-group diffusion theory ($k_{\text{eff}} = \frac{k_\infty}{1 + M^2 B_g^2} = 1.000$), calculate the required material buckling $B_m^2$ in $\text{cm}^{-2}$.
2. For a spherical reactor of radius $R$, the geometric buckling is $B_g^2 = (\pi / R)^2$. Determine the critical radius $R_{\text{crit}}$ in centimeters and critical volume $V_{\text{crit}}$ in cubic meters.""",
            "solution": r"""### Step 1: Material Buckling $B_m^2$
At exact criticality ($k_{\text{eff}} = 1.000$):
$$\frac{k_\infty}{1 + M^2 B_m^2} = 1.000 \implies 1 + M^2 B_m^2 = k_\infty$$
$$B_m^2 = \frac{k_\infty - 1}{M^2}$$
Given $k_\infty = 1.080$ and $M^2 = 32.0\text{ cm}^2$:
$$B_m^2 = \frac{1.080 - 1.000}{32.0\text{ cm}^2} = \frac{0.080}{32.0} = 0.00250\text{ cm}^{-2}$$

### Step 2: Critical Radius and Volume
For a sphere:
$$B_g^2 = \left(\frac{\pi}{R}\right)^2 = B_m^2 = 0.00250\text{ cm}^{-2}$$
Taking the square root:
$$\frac{\pi}{R_{\text{crit}}} = \sqrt{0.00250} = 0.0500\text{ cm}^{-1}$$
$$R_{\text{crit}} = \frac{\pi}{0.0500\text{ cm}^{-1}} = \frac{3.14159}{0.0500} \approx 62.83\text{ cm}$$

Critical volume:
$$V_{\text{crit}} = \frac{4}{3}\pi R_{\text{crit}}^3 = \frac{4}{3}\pi (62.83\text{ cm})^3 = \frac{4}{3}\pi (248,091\text{ cm}^3) \approx 1,039,200\text{ cm}^3 \approx 1.039\text{ m}^3$$
The critical core has a radius of **$62.8\text{ cm}$** and volume of **$1.04\text{ m}^3$**.""",
            "hints": ["Criticality condition: B^2 = (k_inf - 1) / M^2.", "For a bare sphere, geometric buckling is B^2 = (pi / R)^2."]
        },
        6: {
            "id": "prob-6-9",
            "problemNumber": "6.9",
            "title": "Klein-Nishina Differential Cross-Section and Angular Distribution",
            "difficulty": "Advanced",
            "statement": r"""The Klein-Nishina differential scattering cross-section per electron is:
$$\frac{d\sigma_C}{d\Omega} = \frac{r_e^2}{2} P(E, \theta)^2 [ P(E, \theta) + P(E, \theta)^{-1} - \sin^2\theta ]$$
where $r_e = 2.818\text{ fm}$ ($r_e^2 = 7.94 \times 10^{-26}\text{ cm}^2 = 0.0794\text{ b}$) and $P(E, \theta) = \frac{E'}{E} = \frac{1}{1 + \alpha(1 - \cos\theta)}$ with $\alpha = E / (m_e c^2)$.
1. For an incident gamma energy $E = 1.022\text{ MeV}$ ($\alpha = 2.00$):
   (a) Compute $P$ and $d\sigma_C/d\Omega$ at $\theta = 0^\circ$ (forward scattering).
   (b) Compute $P$ and $d\sigma_C/d\Omega$ at $\theta = 90^\circ$ (perpendicular scattering).
   (c) Compute $P$ and $d\sigma_C/d\Omega$ at $\theta = 180^\circ$ (backscattering).
2. Quantify the forward-peaking asymmetry ratio $(d\sigma/d\Omega)_{0^\circ} / (d\sigma/d\Omega)_{180^\circ}$.""",
            "solution": r"""### Step 1: Evaluations for $\alpha = 2.00$
Constant pre-factor:
$$\frac{r_e^2}{2} = \frac{0.07941\text{ b}}{2} \approx 0.039705\text{ b/sr} = 39.71\text{ mb/sr}$$

1. **At $\theta = 0^\circ$ ($\cos 0^\circ = 1 \implies 1 - \cos\theta = 0, \sin^2 0^\circ = 0$)**:
$$P = \frac{1}{1 + 2(0)} = 1.000$$
$$\text{Bracket} = P + P^{-1} - \sin^2 0^\circ = 1 + 1 - 0 = 2.000$$
$$\left(\frac{d\sigma}{d\Omega}\right)_{0^\circ} = (39.71\text{ mb/sr})(1.000)^2(2.000) = 79.41\text{ mb/sr}$$
(Note: At $\theta = 0^\circ$, Klein-Nishina equals the classical Thomson scattering cross-section $r_e^2$).

2. **At $\theta = 90^\circ$ ($\cos 90^\circ = 0 \implies 1 - \cos\theta = 1, \sin^2 90^\circ = 1$)**:
$$P = \frac{1}{1 + 2(1)} = \frac{1}{3} \approx 0.33333$$
$$\text{Bracket} = \frac{1}{3} + 3 - 1 = \frac{7}{3} \approx 2.33333$$
$$\left(\frac{d\sigma}{d\Omega}\right)_{90^\circ} = (39.71\text{ mb/sr})\left(\frac{1}{3}\right)^2\left(\frac{7}{3}\right) = 39.71 \times \frac{7}{27} \approx 10.29\text{ mb/sr}$$

3. **At $\theta = 180^\circ$ ($\cos 180^\circ = -1 \implies 1 - \cos\theta = 2, \sin^2 180^\circ = 0$)**:
$$P = \frac{1}{1 + 2(2)} = \frac{1}{5} = 0.200$$
$$\text{Bracket} = 0.200 + 5.000 - 0 = 5.200$$
$$\left(\frac{d\sigma}{d\Omega}\right)_{180^\circ} = (39.71\text{ mb/sr})(0.200)^2(5.200) = 39.71 \times 0.040 \times 5.200 = 39.71 \times 0.208 \approx 8.26\text{ mb/sr}$$

### Step 2: Forward-Peaking Asymmetry Ratio
$$\text{Ratio} = \frac{(d\sigma/d\Omega)_{0^\circ}}{(d\sigma/d\Omega)_{180^\circ}} = \frac{79.41\text{ mb/sr}}{8.26\text{ mb/sr}} \approx 9.61$$
At $1\text{ MeV}$, Compton scattering is nearly **$10$ times more probable in the forward direction** than in backward scattering.""",
            "hints": ["Calculate the energy ratio P = 1 / [1 + alpha*(1 - cos(theta))].", "Evaluate bracket [P + 1/P - sin^2(theta)] and multiply by (r_e^2 / 2) * P^2."]
        },
        7: {
            "id": "prob-7-9",
            "problemNumber": "7.9",
            "title": "Fast Neutron-Gamma Pulse Shape Discrimination Figure of Merit (FOM)",
            "difficulty": "Intermediate",
            "statement": r"""In an organic liquid scintillation detector (EJ-301), pulse shape discrimination (PSD) separates fast neutrons (recoil protons) from gamma rays (Compton electrons).
The distribution of the charge ratio $\text{PSD} = Q_{\text{tail}} / Q_{\text{total}}$ reveals two Gaussian peaks:
- Gamma peak: centroid $P_\gamma = 0.185$, $\text{FWHM}_\gamma = 0.035$
- Neutron peak: centroid $P_n = 0.310$, $\text{FWHM}_n = 0.045$
1. Formulate the standard Figure of Merit ($\text{FOM}$) for pulse shape discrimination:
$$\text{FOM} = \frac{P_n - P_\gamma}{\text{FWHM}_n + \text{FWHM}_\gamma}$$
2. Compute the $\text{FOM}$ and determine whether good separation ($\text{FOM} \ge 1.25$) is achieved.
3. Compute the peak separation distance in units of combined standard deviations ($\sigma_\gamma + \sigma_n$).""",
            "solution": r"""### Step 1: Figure of Merit Formulation
$$\text{FOM} = \frac{\Delta \text{Peak}}{\text{FWHM}_n + \text{FWHM}_\gamma} = \frac{P_n - P_\gamma}{\text{FWHM}_n + \text{FWHM}_\gamma}$$

### Step 2: Numerical Calculation
Peak separation:
$$\Delta \text{Peak} = P_n - P_\gamma = 0.310 - 0.185 = 0.125$$
Sum of FWHMs:
$$\text{FWHM}_n + \text{FWHM}_\gamma = 0.045 + 0.035 = 0.080$$
$$\text{FOM} = \frac{0.125}{0.080} = 1.5625$$
Because $\text{FOM} = 1.56 > 1.25$, the detector achieves **clean, excellent discrimination** with less than $0.01\%$ mutual misclassification!

### Step 3: Separation in Standard Deviations
Convert FWHM to $\sigma$ ($FWHM = 2.355 \sigma$):
$$\sigma_n = \frac{0.045}{2.355} \approx 0.01911$$
$$\sigma_\gamma = \frac{0.035}{2.355} \approx 0.01486$$
$$\sigma_n + \sigma_\gamma = 0.03397$$
Number of standard deviations:
$$\text{Separation} = \frac{0.125}{0.03397} \approx 3.68 \sigma$$
The peaks are separated by nearly **$3.7$ standard deviations**, ensuring reliable real-time neutron detection.""",
            "hints": ["Figure of Merit is (Peak_2 - Peak_1) / (FWHM_1 + FWHM_2).", "FWHM = 2.355 * sigma."]
        },
        8: {
            "id": "prob-8-9",
            "problemNumber": "8.9",
            "title": "Epithermal Neutron Activation Resonance Advantage Factor for Trace Arsenic",
            "difficulty": "Intermediate",
            "statement": r"""In biological tissue, Neutron Activation Analysis of trace arsenic ($^{75}\text{As}$, $I_0 = 42.0\text{ b}, \sigma_{\text{th}} = 4.3\text{ b}$) is obscured by high sodium background ($^{23}\text{Na}$, $I_0 = 0.31\text{ b}, \sigma_{\text{th}} = 0.53\text{ b}$).
Epithermal NAA (ENAA) encapsulates the sample in cadmium to filter out thermal neutrons.
1. Calculate the cadmium ratio $R_{\text{Cd}} = 1 + \frac{\sigma_{\text{th}} \Phi_{\text{th}}}{I_0 \Phi_{\text{epi}}}$ for arsenic and sodium assuming a typical reactor flux ratio $\Phi_{\text{th}} / \Phi_{\text{epi}} = 25.0$.
2. Formulate and compute the **Resonance Advantage Factor** $F_{\text{adv}}$ of arsenic over sodium:
$$F_{\text{adv}} = \frac{(I_0 / \sigma_{\text{th}})_{\text{As}}}{(I_0 / \sigma_{\text{th}})_{\text{Na}}}$$
3. Conclude how ENAA enhances the detection limit of trace arsenic in biological samples.""",
            "solution": r"""### Step 1: Cadmium Ratio Calculations
1. **For Arsenic-75**:
$$\frac{\sigma_{\text{th}}}{I_0}(\text{As}) = \frac{4.3\text{ b}}{42.0\text{ b}} \approx 0.10238$$
$$R_{\text{Cd}}(\text{As}) = 1 + (0.10238)(25.0) = 1 + 2.560 = 3.56$$

2. **For Sodium-23**:
$$\frac{\sigma_{\text{th}}}{I_0}(\text{Na}) = \frac{0.53\text{ b}}{0.31\text{ b}} \approx 1.7097$$
$$R_{\text{Cd}}(\text{Na}) = 1 + (1.7097)(25.0) = 1 + 42.74 = 43.74$$

### Step 2: Resonance Advantage Factor
Compute individual $I_0 / \sigma_{\text{th}}$ ratios:
$$\left(\frac{I_0}{\sigma_{\text{th}}}\right)_{\text{As}} = \frac{42.0}{4.3} \approx 9.767$$
$$\left(\frac{I_0}{\sigma_{\text{th}}}\right)_{\text{Na}} = \frac{0.31}{0.53} \approx 0.5849$$
Advantage factor:
$$F_{\text{adv}} = \frac{9.767}{0.5849} \approx 16.70$$

### Step 3: Analytical Conclusion
By filtering out thermal neutrons with cadmium:
The background $^{24}\text{Na}$ activity is suppressed by a factor of $44$, whereas the arsenic signal is reduced by only a factor of $3.6$.
The net signal-to-background ratio for trace arsenic improves by a factor of **$16.7$**, lowering the arsenic detection limit in human hair and nail samples from $50\text{ ppb}$ down to $3\text{ ppb}$!""",
            "hints": ["Resonance advantage factor is (I_0 / sigma_th)_analyte / (I_0 / sigma_th)_matrix.", "Cadmium absorbs thermal neutrons, enhancing isotopes with large resonance integrals I_0."]
        },
        9: {
            "id": "prob-9-9",
            "problemNumber": "9.9",
            "title": "Hot Fusion Superheavy Synthesis Cross-Section of Tennessine-294",
            "difficulty": "Advanced",
            "statement": r"""Tennessine-294 ($^{294}_{117}\text{Ts}$) was synthesized via hot fusion at Dubna using the reaction:
$$^{249}_{97}\text{Bk} + ^{48}_{20}\text{Ca} \longrightarrow [^{297}_{117}\text{Ts}^*] \longrightarrow ^{294}_{117}\text{Ts} + 3 \, ^1_0n$$
The measured reaction cross-section is $\sigma = 0.50\text{ picobarn}$ ($0.50 \times 10^{-36}\text{ cm}^2$).
A berkelium-249 target of area density $\rho x = 0.310\text{ mg/cm}^2$ is bombarded for $t = 150\text{ days}$ ($1.30 \times 10^7\text{ s}$) with a $^{48}\text{Ca}^{5+}$ beam current $I_{\text{beam}} = 1.20\,\mu\text{A}$ ($1.50 \times 10^{12}\text{ ions/second}$).
The chemical and separator transmission efficiency is $\epsilon_{\text{sep}} = 65\%$.
1. Calculate the total number of target $^{249}\text{Bk}$ atoms per square centimeter.
2. Determine the total fluence of $^{48}\text{Ca}$ ions delivered over the 150-day experiment.
3. Calculate the total statistical expected number of detected $^{294}\text{Ts}$ atoms.""",
            "solution": r"""### Step 1: Target Atom Area Density
Molar mass of $^{249}\text{Bk} \approx 249.08\text{ g/mol}$.
$$N_{\text{Bk}} = \frac{0.310 \times 10^{-3}\text{ g/cm}^2}{249.08\text{ g/mol}} \times 6.022 \times 10^{23}\text{ mol}^{-1} \approx 7.495 \times 10^{17}\text{ atoms/cm}^2$$

### Step 2: Total Ion Fluence
Beam particle rate: $\dot{N} = 1.50 \times 10^{12}\text{ ions/second}$.
Over $t = 150\text{ days} = 1.296 \times 10^7\text{ seconds}$:
$$\Phi_{\text{total}} = (1.50 \times 10^{12}\text{ s}^{-1}) \times (1.296 \times 10^7\text{ s}) = 1.944 \times 10^{19}\text{ incident }^{48}\text{Ca ions}$$

### Step 3: Expected Number of Detected Atoms
Cross-section: $\sigma = 0.50\text{ pb} = 0.50 \times 10^{-36}\text{ cm}^2$.
Total nuclear reactions produced:
$$N_{\text{prod}} = \Phi_{\text{total}} \cdot N_{\text{Bk}} \cdot \sigma = (1.944 \times 10^{19})(7.495 \times 10^{17}\text{ cm}^{-2})(0.50 \times 10^{-36}\text{ cm}^2)$$
$$N_{\text{prod}} = 1.457 \times 10^{37} \times 0.50 \times 10^{-36} \approx 7.285\text{ atoms produced}$$

Accounting for separator efficiency $\epsilon_{\text{sep}} = 0.65$:
$$N_{\text{detected}} = 7.285 \times 0.65 \approx 4.74\text{ atoms}$$
Over **5 continuous months of particle accelerator beam time**, the experiment detects only **$\approx 5$ individual atoms** of Tennessine-294!""",
            "hints": ["Target atom density: N_T = (mass / M) * N_A.", "Number of events = Fluence * N_T * sigma * efficiency."]
        },
        10: {
            "id": "prob-10-10",
            "problemNumber": "10.9",
            "title": "ICRP Compartmental Biokinetic Model for Inhaled Insoluble Plutonium-239",
            "difficulty": "Advanced",
            "statement": r"""A radiological worker accidentally inhales insoluble high-fired plutonium dioxide ($^{239}\text{Pu}\text{O}_2$, Type S aerosol, $T_p = 24,110\text{ years}$, alpha energy $E_\alpha = 5.15\text{ MeV}$).
Under the ICRP 66 Human Respiratory Tract Model, $10.0\%$ of the initial intake deposits in the alveolar-interstitial ($AI$) region of the lungs.
For Type S particulates, the biological clearance from the $AI$ region follows two compartments:
- $90\%$ clears with biological half-time $T_{b,1} = 7,000\text{ days}$
- $10\%$ is retained permanently ($T_{b,2} = \infty$)
The mass of the human lung is $m_{\text{lung}} = 1.00\text{ kg}$.
For an acute alveolar intake of $A_0 = 1,000\text{ Bq}$ of $^{239}\text{Pu}$:
1. Calculate the initial alpha energy deposition rate in the lung in Joules per day.
2. Determine the total alpha energy imparted to the lungs over the first year ($365\text{ days}$) in Joules.
3. Compute the cumulative lung absorbed dose in Grays ($Gy$) and the equivalent dose in Sieverts ($Sv$, with $w_R = 20$) over the first year.""",
            "solution": r"""### Step 1: Initial Alpha Energy Deposition Rate
Energy per alpha decay:
$$E_\alpha = 5.15\text{ MeV} = 5.15 \times 1.60218 \times 10^{-13}\text{ J} \approx 8.2512 \times 10^{-13}\text{ J per decay}$$
Activity: $A_0 = 1,000\text{ Bq} = 1,000\text{ decays/second}$.
Daily alpha energy rate:
$$\dot{E} = (1000\text{ s}^{-1}) \times (8.2512 \times 10^{-13}\text{ J}) \times (86,400\text{ s/day}) \approx 7.129 \times 10^{-5}\text{ J/day}$$

### Step 2: Total Energy Imparted Over Year 1
Because $T_{b,1} = 7,000\text{ days} \gg 365\text{ days}$ (and $T_p = 24,110\text{ years}$), clearance over the first year is negligible:
$$\lambda_b = \frac{\ln 2}{7000\text{ d}} \approx 9.902 \times 10^{-5}\text{ d}^{-1} \implies e^{-\lambda_b (365)} \approx 0.9645$$
Average activity over the year:
$$\bar{A} \approx A_0 \left(1 - \frac{1}{2} \lambda_b t\right) = 1000 \times [1 - 0.5(0.0361)] \approx 982\text{ Bq}$$
Total alpha disintegrations in 365 days:
$$N_{\text{decays}} \approx 982\text{ s}^{-1} \times (365 \times 86400\text{ s}) \approx 3.10 \times 10^{10}\text{ decays}$$
Total imparted energy:
$$E_{\text{total}} = (3.10 \times 10^{10}) \times (8.2512 \times 10^{-13}\text{ J}) \approx 0.02558\text{ Joules}$$

### Step 3: Absorbed and Equivalent Lung Dose
1. **Absorbed Dose ($D$)**:
$$D = \frac{E_{\text{total}}}{m_{\text{lung}}} = \frac{0.02558\text{ J}}{1.00\text{ kg}} \approx 0.02558\text{ Gy} = 25.6\text{ mGy}$$

2. **Equivalent Dose ($H$)**:
With alpha radiation weighting factor $w_R = 20$:
$$H_{\text{lung}} = w_R \cdot D = 20 \times 25.58\text{ mGy} \approx 511.6\text{ mSv} \approx 0.512\text{ Sv}$$
A mere $1,000\text{ Bq}$ (barely $0.44\text{ micrograms}$) of insoluble $^{239}\text{Pu}$ delivers over **half a Sievert ($512\text{ mSv}$)** of equivalent dose to the lung in the first year alone, illustrating the extreme radiological hazard of alpha-emitting actinide aerosols!""",
            "hints": ["Energy rate = Activity * Energy per decay * 86,400 seconds/day.", "Equivalent dose H = w_R * Absorbed dose D, with w_R = 20 for alpha particles."]
        }
    }

    for unit in units:
        un = unit["unitNumber"]
        if un in prob9_data:
            p9 = prob9_data[un]
            if not any(p["id"] == p9["id"] for p in unit["problems"]):
                unit["problems"].append(p9)
    return units
