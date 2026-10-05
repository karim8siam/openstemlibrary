# build_ssp2_units_5_6.py
# Generates ssp2_u5.json and ssp2_u6.json for Course #18: Solid State Physics II

import json

# =========================================================================
# UNIT 5: Phenomenological Superconductivity: Meissner Effect, London & Ginzburg-Landau
# =========================================================================

u5_data = {
    "title": "Phenomenological Superconductivity: Meissner Effect, London & Ginzburg-Landau",
    "subtitle": "Zero Resistance, Perfect Diamagnetism, London Screening & Abrikosov Vortices",
    "summary": "This unit develops the macroscopic thermodynamic and phenomenological physics of superconductivity. We explore the discovery of zero electrical resistance and persistent supercurrents below Tc, formulate the thermodynamics of the superconducting phase transition, and establish why the Meissner-Ochsenfeld effect distinguishes true superconductivity from ideal classical conductivity. We derive the London equations and London penetration depth, analyze Type-I vs Type-II superconductors, and formulate Ginzburg-Landau theory. Finally, we derive the coherence length, the surface energy criterion kappa = lambda/xi, magnetic flux quantization in units of h/2e, and the Abrikosov mixed vortex state.",
    "sections": [
        {
            "id": "sec-5-1",
            "title": "Zero Electrical Resistance, Critical Temperature Tc & Persistent Supercurrents",
            "content": r"""
<h3>1. Discovery & The Superconducting State</h3>
<p>
In 1911, Heike Kamerlingh Onnes discovered that when pure mercury ($\text{Hg}$) is cooled below a critical temperature $T_c = 4.15\text{ K}$, its electrical resistivity drops abruptly to zero:
</p>
$$\rho(T) = 0 \quad \text{for } T < T_c$$
<p>
Modern experimental measurements on closed superconducting rings place an upper bound on the resistivity of $\rho < 10^{-26}\ \Omega\cdot\text{m}$ (over 18 orders of magnitude lower than high-purity copper). Persistent electrical currents induced in superconducting rings have circulated without measurable decay for decades, implying a carrier lifetime $\tau_{\text{decay}} > 10^5\text{ years}$.
</p>

<h3>2. Empirical Critical Field Law</h3>
<p>
The superconducting state is destroyed and normal electrical resistance is restored when an external magnetic field exceeds a critical value $H_c(T)$. Experimentally, the critical field follows an accurate parabolic temperature dependence:
</p>
$$H_c(T) = H_0 \left[ 1 - \left( \frac{T}{T_c} \right)^2 \right]$$
<p>
where $H_0 = H_c(0)$ is the critical field extrapolated to absolute zero ($T = 0\text{ K}$).
</p>
<p>
Similarly, passing an electrical current through a superconductor creates a self-magnetic field. According to <strong>Silsbee's Rule</strong>, superconductivity is destroyed when the total magnetic field at the specimen surface (from external sources and transport currents combined) reaches $H_c(T)$. For a cylindrical wire of radius $r$, the <strong>critical current</strong> is:
</p>
$$I_c(T) = 2\pi r H_c(T)$$
"""
        },
        {
            "id": "sec-5-2",
            "title": "The Meissner-Ochsenfeld Effect & Perfect Diamagnetism vs Perfect Conductivity",
            "content": r"""
<h3>1. The Meissner-Ochsenfeld Effect</h3>
<p>
In 1933, Walther Meissner and Robert Ochsenfeld discovered that when a superconductor is cooled below $T_c$ in the presence of a constant external magnetic field $\vec{B}$, the magnetic flux is <strong>actively expelled</strong> from the interior of the specimen:
</p>
$$\vec{B}_{\text{interior}} = 0 \quad (\text{Meissner Effect})$$
<p>
Inside the bulk material, the magnetic induction is identically zero:
</p>
$$\vec{B} = \mu_0 (\vec{H} + \vec{M}) = 0 \implies \vec{M} = -\vec{H}$$
<p>
The volume magnetic susceptibility of a bulk superconductor is:
</p>
$$\chi_v = \frac{M}{H} = -1 \quad (\text{Perfect Diamagnetism})$$

<h3>2. Distinction Between a Perfect Conductor and a Superconductor</h3>
<p>
Consider a hypothetical classical perfect conductor with zero resistivity ($\rho = 0$). By Ohm's law, $\vec{E} = \rho \vec{j} = 0$. Faraday's law of induction requires:
</p>
$$\nabla \times \vec{E} = -\frac{\partial\vec{B}}{\partial t} = 0 \implies \frac{\partial\vec{B}}{\partial t} = 0 \implies \vec{B}(t) = \vec{B}(0) = \text{constant}$$
<p>
A perfect conductor <em>traps whatever flux was present</em> when resistance vanished:
</p>
<ul>
  <li>If cooled in zero field, it excludes subsequent fields ($B = 0$).</li>
  <li>If cooled in an applied field $B_0$, it traps $B_0$ inside indefinitely ($\vec{B} = B_0 \ne 0$). The final state depends on thermodynamic history!</li>
</ul>
<p>
In contrast, a true superconductor <strong>always expels the magnetic field</strong> upon cooling through $T_c$, regardless of whether the field was applied before or after cooling:
</p>
$$\vec{B} = 0 \quad \text{always for } T < T_c$$
<p>
The Meissner effect proves that superconductivity is not merely infinite conductivity, but a true <strong>thermodynamic equilibrium phase</strong> governed by an equation of state $\vec{B} = 0$.
</p>
"""
        },
        {
            "id": "sec-5-3",
            "title": "Thermodynamics of the Superconducting Transition: Free Energy & Specific Heat Jump",
            "content": r"""
<h3>1. Free Energy & Condensation Energy Density</h3>
<p>
Because superconductivity is an equilibrium thermodynamic state, we apply the Gibbs free energy per unit volume:
</p>
$$dG = -S dT - \mu_0 M dH$$
<p>
In the normal state ($M_n \approx 0$):
</p>
$$G_n(T, H) = G_n(T, 0)$$
<p>
In the superconducting state ($M_s = -H$):
</p>
$$G_s(T, H) = G_s(T, 0) - \mu_0 \int_0^H (-H') dH' = G_s(T, 0) + \frac{\mu_0 H^2}{2}$$
<p>
At the phase boundary $H = H_c(T)$, the normal and superconducting phases are in thermodynamic equilibrium:
</p>
$$G_s(T, H_c) = G_n(T, H_c) \implies G_s(T, 0) + \frac{\mu_0 H_c^2(T)}{2} = G_n(T, 0)$$
<p>
Rearranging gives the <strong>superconducting condensation energy density</strong>:
</p>
$$\Delta f_{\text{cond}} \equiv G_n(T, 0) - G_s(T, 0) = \frac{\mu_0 H_c^2(T)}{2}$$
<p>
The superconducting state has a lower free energy than the normal state by exactly the magnetic energy density required to expel the critical field.
</p>

<h3>2. Entropy & Discontinuous Specific Heat Jump</h3>
<p>
Differentiating with respect to temperature:
</p>
$$S_n - S_s = -\frac{d}{dT}[G_n(T, 0) - G_s(T, 0)] = -\mu_0 H_c(T) \frac{dH_c}{dT}$$
<ul>
  <li>At $T = T_c$, $H_c(T_c) = 0$, so $S_s(T_c) = S_n(T_c)$. The entropy is continuous: there is <strong>zero latent heat</strong> in zero magnetic field ($Q = T_c \Delta S = 0$).</li>
  <li>Differentiating entropy to obtain the specific heat $C = T \frac{dS}{dT}$:
  $$C_s - C_n = T \frac{d}{dT}(S_s - S_n) = \mu_0 T \left[ \left(\frac{dH_c}{dT}\right)^2 + H_c(T) \frac{d^2H_c}{dT^2} \right]$$
  At $T = T_c$, where $H_c(T_c) = 0$:
  $$\Delta C \equiv C_s(T_c) - C_n(T_c) = \mu_0 T_c \left( \left.\frac{dH_c}{dT}\right|_{T_c} \right)^2 > 0$$</li>
</ul>
<p>
Using the parabolic law $H_c(T) = H_0[1 - (T/T_c)^2]$, the slope at $T_c$ is $\left.\frac{dH_c}{dT}\right|_{T_c} = -\frac{2H_0}{T_c}$:
</p>
$$\Delta C = \mu_0 T_c \left(-\frac{2H_0}{T_c}\right)^2 = \frac{4\mu_0 H_0^2}{T_c}$$
<p>
This finite discontinuity in specific heat with zero latent heat rigorously classifies the superconducting transition in zero field as a <strong>second-order phase transition</strong>.
</p>
"""
        },
        {
            "id": "sec-5-4",
            "title": "The London Phenomenological Theory: London Equations & Magnetic Penetration Depth",
            "content": r"""
<h3>1. The Two London Equations</h3>
<p>
In 1935, Fritz and Heinz London proposed a phenomenological two-fluid model where the electron density divides into a normal component $n_n$ and a superconducting component $n_s$ ($n = n_n + n_s$).
</p>
<p>
Superconducting electrons accelerate without friction under an electric field:
</p>
$$m \frac{d\vec{v}_s}{dt} = -e\vec{E} \implies \frac{\partial \vec{j}_s}{\partial t} = \frac{n_s e^2}{m} \vec{E} \quad (\text{First London Equation})$$
<p>
Taking the curl of both sides and invoking Faraday's law $\nabla \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}$:
</p>
$$\frac{\partial}{\partial t} \left( \nabla \times \vec{j}_s + \frac{n_s e^2}{m} \vec{B} \right) = 0$$
<p>
To encompass the Meissner effect (where $\vec{B} = 0$ is the unique equilibrium state, not merely a conserved constant), the London brothers boldly set the quantity in parentheses identically to zero:
</p>
$$\nabla \times \vec{j}_s = -\frac{n_s e^2}{m} \vec{B} \quad (\text{Second London Equation})$$
<p>
In terms of the magnetic vector potential $\vec{A}$ in the London gauge ($\nabla \cdot \vec{A} = 0$):
</p>
$$\vec{j}_s = -\frac{n_s e^2}{m} \vec{A}$$

<h3>2. The London Penetration Depth $\lambda_L$</h3>
<p>
Taking the curl of Maxwell's Ampère law $\nabla \times \vec{B} = \mu_0 \vec{j}_s$ (neglecting displacement current):
</p>
$$\nabla \times (\nabla \times \vec{B}) = \mu_0 (\nabla \times \vec{j}_s)$$
<p>
Using the vector identity $\nabla \times (\nabla \times \vec{B}) = \nabla(\nabla \cdot \vec{B}) - \nabla^2 \vec{B} = -\nabla^2 \vec{B}$ (since $\nabla \cdot \vec{B} = 0$):
</p>
$$-\nabla^2 \vec{B} = -\mu_0 \frac{n_s e^2}{m} \vec{B} \implies \nabla^2 \vec{B} = \frac{1}{\lambda_L^2} \vec{B}$$
<p>
where $\lambda_L$ is the <strong>London penetration depth</strong>:
</p>
$$\lambda_L \equiv \sqrt{\frac{m}{\mu_0 n_s e^2}}$$
<p>
For a semi-infinite superconductor filling $x \ge 0$ with an external field $B_0 \hat{z}$ at $x = 0$:
</p>
$$B(x) = B_0 \exp\left( -\frac{x}{\lambda_L} \right)$$
<p>
The magnetic field does not vanish discontinuously at the surface, but penetrates exponentially into a thin surface sheath of thickness $\lambda_L \sim 30-100\text{ nm}$, supported by screening supercurrents $\vec{j}_s(x) = \frac{B_0}{\mu_0 \lambda_L} e^{-x/\lambda_L} \hat{y}$.
</p>
<p>
As $T \to T_c$, $n_s(T) \to 0$, causing the penetration depth to diverge:
</p>
$$\lambda_L(T) = \lambda_0 \left[ 1 - \left( \frac{T}{T_c} \right)^4 \right]^{-1/2}$$
""",
            "simulation": "ssp2-meissner-london-sim",
            "simulations": ["ssp2-meissner-london-sim"]
        },
        {
            "id": "sec-5-5",
            "title": "Type-I vs Type-II Superconductors: Critical Fields $H_c, H_{c1}, H_{c2}$ & Surface Energy",
            "content": r"""
<h3>1. Classification: Type-I vs Type-II Superconductors</h3>
<p>
Superconductors are categorized into two fundamentally distinct classes based on their magnetic response:
</p>
<ul>
  <li><strong>Type-I Superconductors (e.g. Pb, Sn, In, Al, Hg):</strong>
  Exhibit complete Meissner expulsion ($\vec{B} = 0$) up to a single sharp thermodynamic critical field $H_c(T)$. When $H > H_c$, superconductivity is destroyed abruptly, and the material reverts to the normal state in a first-order phase transition. Values of $H_c$ are typically low ($< 0.1\text{ T}$), rendering pure Type-I materials useless for high-field electromagnets.</li>
  <li><strong>Type-II Superconductors (e.g. Nb, Nb-Ti, $\text{Nb}_3\text{Sn}$, YBCO, BSCCO):</strong>
  Possess <em>two</em> distinct critical magnetic fields: the <strong>lower critical field</strong> $H_{c1}(T)$ and the <strong>upper critical field</strong> $H_{c2}(T)$.
  <ul>
    <li>For $H < H_{c1}$: Complete Meissner effect ($B = 0$).</li>
    <li>For $H_{c1} < H < H_{c2}$: The <strong>Mixed State (or Shubnikov phase / Vortex state)</strong>. Magnetic flux penetrates the bulk in the form of quantized microscopic flux tubes (vortices), while the intervening matrix remains superconducting. Zero electrical resistance persists!</li>
    <li>For $H > H_{c2}$: The bulk completely transitions to the normal state. $H_{c2}$ can be exceptionally large ($15\text{ T}$ in Nb-Ti, $30\text{ T}$ in $\text{Nb}_3\text{Sn}$, $>100\text{ T}$ in cuprates), enabling modern MRI scanners and particle accelerator magnets.</li>
  </ul>
  </li>
</ul>

<h3>2. The Surface Energy of a Normal-Superconducting Interface</h3>
<p>
Consider a planar interface between a normal domain ($B = H_c$) and a superconducting domain ($B = 0$):
</p>
<ul>
  <li>The magnetic field penetrates a distance $\lambda$ into the superconductor, releasing magnetic expulsion energy $\frac{1}{2}\mu_0 H_c^2 \lambda > 0$ (energy gain).</li>
  <li>The superconducting order parameter $|\psi|^2$ requires a characteristic distance $\xi$ (the coherence length) to recover its bulk value, losing condensation energy $\frac{1}{2}\mu_0 H_c^2 \xi < 0$ (energy cost).</li>
</ul>
<p>
The net surface energy per unit area of the interface is approximately:
</p>
$$\sigma_{\text{ns}} \approx \frac{1}{2}\mu_0 H_c^2 (\xi - \lambda)$$
<ul>
  <li><strong>Positive Surface Energy ($\xi > \lambda$):</strong> The interface costs energy. The system minimizes interface area by remaining either fully superconducting or fully normal $\implies$ <strong>Type-I Superconductor</strong>.</li>
  <li><strong>Negative Surface Energy ($\xi < \lambda$):</strong> Creating interfaces is energetically favorable! The material spontaneously maximizes normal-superconductor boundaries by shredding into a dense array of microscopic magnetic flux tubes $\implies$ <strong>Type-II Superconductor</strong>.</li>
</ul>
"""
        },
        {
            "id": "sec-5-6",
            "title": "The Ginzburg-Landau (GL) Theory: Order Parameter, Free Energy & Coherence Length",
            "content": r"""
<h3>1. The Ginzburg-Landau Order Parameter & Free Energy</h3>
<p>
In 1950, Vitaly Ginzburg and Lev Landau formulated a general phenomenological theory of superconductivity based on Landau's theory of second-order phase transitions. They introduced a complex macroscopic pseudo-wavefunction $\psi(\vec{r}) = |\psi|e^{i\theta}$ as an <strong>order parameter</strong>, whose local density represents the superconducting Cooper pair density:
</p>
$$|\psi(\vec{r})|^2 = \frac{1}{2} n_s(\vec{r})$$
<p>
Near $T_c$, where $|\psi|^2$ is small, the Gibbs free energy density is expanded in powers of $|\psi|^2$ and its spatial gradients:
</p>
$$f_s = f_n + \alpha(T) |\psi|^2 + \frac{\beta}{2} |\psi|^4 + \frac{1}{2m^*} |(-i\hbar\nabla - q^*\vec{A})\psi|^2 + \frac{B^2}{2\mu_0}$$
<p>
where $m^* = 2m$ and $q^* = -2e$ are the mass and charge of a Cooper pair.
</p>
<ul>
  <li>$\beta > 0$ ensures stability.</li>
  <li>$\alpha(T) = \alpha_0 (T - T_c)$:
  <ul>
    <li>For $T > T_c$: $\alpha > 0$, minimized at $|\psi| = 0$ (normal state).</li>
    <li>For $T < T_c$: $\alpha < 0$, minimized at $|\psi_\infty|^2 = -\frac{\alpha}{\beta} = \frac{|\alpha|}{\beta}$.</li>
  </ul>
  </li>
</ul>

<h3>2. The Ginzburg-Landau Equations & Coherence Length $\xi(T)$</h3>
<p>
Minimizing the total free energy functional $\mathcal{F} = \int f_s d^3r$ with respect to $\psi^*$ and $\vec{A}$ yields the <strong>two Ginzburg-Landau equations</strong>:
</p>
$$\frac{1}{2m^*} (-i\hbar\nabla - q^*\vec{A})^2 \psi + \alpha \psi + \beta |\psi|^2 \psi = 0 \quad (\text{First GL Equation})$$
$$\vec{j}_s = \frac{q^*\hbar}{2m^* i} (\psi^* \nabla\psi - \psi \nabla\psi^*) - \frac{(q^*)^2}{m^*} |\psi|^2 \vec{A} = \frac{1}{\mu_0} \nabla \times \vec{B} \quad (\text{Second GL Equation})$$
<p>
In zero magnetic field, the first equation in 1D becomes:
</p>
$$-\frac{\hbar^2}{2m^*|\alpha|} \frac{d^2\psi}{dx^2} - \psi + \frac{\beta}{|\alpha|} \psi^3 = 0$$
<p>
Defining the <strong>Ginzburg-Landau coherence length</strong> $\xi(T)$:
</p>
$$\xi(T) \equiv \sqrt{\frac{\hbar^2}{2m^* |\alpha(T)|}} \propto \left(1 - \frac{T}{T_c}\right)^{-1/2}$$
<p>
$\xi(T)$ represents the characteristic spatial scale over which the superconducting order parameter can vary without excessive gradient energy penalty.
</p>
<p>
We define the dimensionless <strong>Ginzburg-Landau parameter</strong> $\kappa$:
</p>
$$\kappa \equiv \frac{\lambda(T)}{\xi(T)}$$
<p>
The exact boundary derived from GL theory is:
</p>
$$\kappa < \frac{1}{\sqrt{2}} \approx 0.707 \implies \text{Type-I Superconductor}$$
$$\kappa > \frac{1}{\sqrt{2}} \approx 0.707 \implies \text{Type-II Superconductor}$$
"""
        },
        {
            "id": "sec-5-7",
            "title": "Magnetic Flux Quantization $\Phi_0 = h/2e$ & The Abrikosov Mixed Vortex State",
            "content": r"""
<h3>1. Derivation of Magnetic Flux Quantization</h3>
<p>
Consider a thick superconducting cylinder containing a hole or hollow core. Inside the superconducting bulk far from surfaces, $\vec{j}_s = 0$. Writing $\psi(\vec{r}) = |\psi| e^{i\theta(\vec{r})}$:
</p>
$$\vec{j}_s = \frac{q^*}{m^*} |\psi|^2 (\hbar\nabla\theta - q^*\vec{A}) = 0 \implies \hbar\nabla\theta = q^*\vec{A} = -2e\vec{A}$$
<p>
Integrating around a closed path $C$ enclosing the hole deep inside the bulk:
</p>
$$\hbar \oint_C \nabla\theta \cdot d\vec{l} = -2e \oint_C \vec{A} \cdot d\vec{l}$$
<p>
Because $\psi(\vec{r})$ must be single-valued, the phase change around any closed loop must be an integer multiple of $2\pi$: $\oint_C \nabla\theta \cdot d\vec{l} = 2\pi n, n \in \mathbb{Z}$.
</p>
<p>
By Stokes' theorem, $\oint_C \vec{A} \cdot d\vec{l} = \iint (\nabla \times \vec{A}) \cdot d\vec{a} = \iint \vec{B} \cdot d\vec{a} = \Phi$:
</p>
$$2\pi n \hbar = -2e \Phi \implies |\Phi| = n \frac{h}{2e} \equiv n \Phi_0$$
<p>
The magnetic flux enclosed by a superconducting ring is <strong>strictly quantized</strong> in discrete integer units of the <strong>flux quantum</strong> $\Phi_0$:
</p>
$$\Phi_0 \equiv \frac{h}{2e} \approx 2.0678 \times 10^{-15}\text{ Wb} = 2.0678 \times 10^{-7}\text{ G}\cdot\text{cm}^2$$
<p>
The factor of $2e$ provided the first direct experimental proof (Deaver & Fairbank; Doll & Näbauer, 1961) that the fundamental charge carriers in superconductors are <strong>electron pairs</strong> (Cooper pairs).
</p>

<h3>2. The Abrikosov Mixed Vortex State</h3>
<p>
In 1957, Alexei Abrikosov discovered periodic solutions to the GL equations for $\kappa > 1/\sqrt{2}$. In the mixed state ($H_{c1} < H < H_{c2}$):
</p>
<ul>
  <li>Magnetic field penetrates as an array of microscopic cylindrical filaments called <strong>vortices</strong> (or fluxons).</li>
  <li>Each vortex has a <strong>normal core</strong> of radius $\sim \xi(T)$ where $|\psi| \to 0$.</li>
  <li>Surrounding the core, circulating supercurrents decay over radius $\lambda(T)$, screening the magnetic field.</li>
  <li>Each individual vortex carries exactly <strong>one single flux quantum</strong> $\Phi_0 = h/2e$.</li>
  <li>Mutual repulsive forces between circulating supercurrents cause vortices to arrange into a regular <strong>Abrikosov triangular flux line lattice</strong> with lattice parameter $a_{\triangle} = \left(\frac{2\Phi_0}{\sqrt{3}B}\right)^{1/2}$.</li>
  <li>The upper critical field occurs when vortex cores overlap:
  $$B_{c2} = \frac{\Phi_0}{2\pi \xi^2}$$</li>
</ul>
""",
            "simulation": "ssp2-abrikosov-vortex-sim",
            "simulations": ["ssp2-abrikosov-vortex-sim"]
        }
    ],
    "problems": [
        {
            "id": "ssp2-prob-5-1",
            "title": "London Magnetic Screening in a Thin Superconducting Slab",
            "statement": "A superconducting plate of thickness $2d$ occupies the region $-d \\le x \\le +d$ and is infinite along $y$ and $z$. A uniform external magnetic field $B_0 \\hat{z}$ is applied parallel to the slab surfaces at $x = \\pm d$.\\n\\n(a) Solve the London differential equation $\\frac{d^2 B}{dx^2} = \\frac{1}{\\lambda_L^2} B$ with boundary conditions $B(\\pm d) = B_0$ to find the magnetic field profile $B(x)$.\\n(b) Derive the screening supercurrent density profile $j_y(x)$.\\n(c) Calculate the average magnetic induction $\\langle B \\rangle = \\frac{1}{2d}\\int_{-d}^d B(x) dx$ and the effective volume magnetic susceptibility $\\chi_{\\text{eff}}$. Show that for an ultra-thin film ($d \\ll \\lambda_L$), the diamagnetic susceptibility is strongly suppressed.",
            "solution": """**(a) Magnetic Field Profile:**
The London differential equation is:
$$\\frac{d^2 B}{dx^2} - \\frac{1}{\\lambda_L^2} B = 0$$
The general solution is a linear combination of hyperbolic functions:
$$B(x) = C_1 \\cosh(x / \\lambda_L) + C_2 \\sinh(x / \\lambda_L)$$
By reflection symmetry across the mid-plane $x = 0$, $B(x) = B(-x)$, requiring $C_2 = 0$:
$$B(x) = C_1 \\cosh(x / \\lambda_L)$$
Applying the boundary condition at the surfaces $B(d) = B_0$:
$$B_0 = C_1 \\cosh(d / \\lambda_L) \\implies C_1 = \\frac{B_0}{\\cosh(d / \\lambda_L)}$$
The exact internal magnetic field profile is:
$$B(x) = B_0 \\frac{\\cosh(x / \\lambda_L)}{\\cosh(d / \\lambda_L)}$$

**(b) Screening Supercurrent Density:**
Using Ampère's law $\\nabla \\times \\vec{B} = \\mu_0 \\vec{j}_s$:
$$\\mu_0 j_y(x) = -\\frac{dB}{dx} = -B_0 \\frac{\\sinh(x / \\lambda_L)}{\\lambda_L \\cosh(d / \\lambda_L)}$$
$$j_y(x) = -\\frac{B_0}{\\mu_0 \\lambda_L} \\frac{\\sinh(x / \\lambda_L)}{\\cosh(d / \\lambda_L)}$$
The current flows in opposite directions on the two faces ($j_y(d) < 0$ and $j_y(-d) > 0$), producing a diamagnetic shielding loop.

**(c) Average Field & Effective Susceptibility:**
The spatial average of $B(x)$ across the slab is:
$$\\langle B \\rangle = \\frac{1}{2d} \\int_{-d}^d B_0 \\frac{\\cosh(x / \\lambda_L)}{\\cosh(d / \\lambda_L)} dx = \\frac{B_0}{d \\cosh(d / \\lambda_L)} [\\lambda_L \\sinh(x / \\lambda_L)]_0^d = B_0 \\frac{\\lambda_L}{d} \\tanh\\left( \\frac{d}{\\lambda_L} \\right)$$
Using $\\langle B \\rangle = \\mu_0 (H_0 + \\langle M \\rangle)$ with $B_0 = \\mu_0 H_0$:
$$\\langle M \\rangle = \\frac{\\langle B \\rangle}{\\mu_0} - H_0 = H_0 \\left[ \\frac{\\lambda_L}{d} \\tanh\\left( \\frac{d}{\\lambda_L} \\right) - 1 \\right]$$
The effective volume susceptibility is:
$$\\chi_{\\text{eff}} = \\frac{\\langle M \\rangle}{H_0} = \\frac{\\lambda_L}{d} \\tanh\\left( \\frac{d}{\\lambda_L} \\right) - 1$$
**Asymptotic Limits:**
1. *Thick Slab ($d \\gg \\lambda_L$):* $\\tanh(d/\\lambda_L) \\approx 1$, so $\\chi_{\\text{eff}} \\approx \\frac{\\lambda_L}{d} - 1 \\to -1$ (Perfect bulk Meissner diamagnetism).
2. *Ultra-Thin Film ($d \\ll \\lambda_L$):* Expand $\\tanh u \\approx u - \\frac{u^3}{3} + \\dots$ with $u = d/\\lambda_L$:
$$\\frac{\\lambda_L}{d} \\left[ \\frac{d}{\\lambda_L} - \\frac{1}{3}\\left(\\frac{d}{\\lambda_L}\\right)^3 \\right] - 1 = 1 - \\frac{1}{3}\\left(\\frac{d}{\\lambda_L}\\right)^2 - 1 = -\\frac{1}{3} \\left( \\frac{d}{\\lambda_L} \\right)^2$$
$$\\chi_{\\text{eff}} \\approx -\\frac{1}{3} \\left( \\frac{d}{\\lambda_L} \\right)^2$$
For an ultra-thin film, the diamagnetic response is suppressed quadratically by $(d/\\lambda_L)^2$ because the screening current has insufficient thickness to decay the field."""
        },
        {
            "id": "ssp2-prob-5-2",
            "title": "Thermodynamics of Superconductivity: Derivation of the Specific Heat Jump",
            "statement": "The critical magnetic field of a Type-I superconductor follows the parabolic law $H_c(T) = H_0 [1 - (T/T_c)^2]$.\\n\\n(a) Derive the temperature dependence of the entropy difference between normal and superconducting states $\\Delta S(T) = S_n(T) - S_s(T)$.\\n(b) Using the experimental fact that the normal state electronic specific heat is linear $C_n(T) = \\gamma T$, derive the exact temperature dependence of the superconducting electronic specific heat $C_s(T)$.\\n(c) Calculate the ratio of the specific heat jump $\\Delta C = C_s(T_c) - C_n(T_c)$ to the normal state specific heat $C_n(T_c)$, and compare it with the universal BCS theoretical prediction $\\Delta C / C_n = 1.428$.",
            "solution": """**(a) Entropy Difference $\\Delta S(T)$:**
From the condensation energy relation:
$$G_n(T) - G_s(T) = \\frac{1}{2} \\mu_0 H_c^2(T) = \\frac{1}{2} \\mu_0 H_0^2 \\left[ 1 - \\left(\\frac{T}{T_c}\\right)^2 \\right]^2$$
Differentiating with respect to $T$ using $S = -dG/dT$:
$$\\Delta S(T) = S_n(T) - S_s(T) = -\\frac{d}{dT}\\left[ \\frac{1}{2}\\mu_0 H_c^2(T) \\right] = -\\mu_0 H_c(T) \\frac{dH_c}{dT}$$
With $\\frac{dH_c}{dT} = -\\frac{2H_0 T}{T_c^2}$:
$$\\Delta S(T) = -\\mu_0 H_0 \\left[ 1 - \\left(\\frac{T}{T_c}\\right)^2 \\right] \\left( -\\frac{2H_0 T}{T_c^2} \\right) = \\frac{2\\mu_0 H_0^2}{T_c^2} T \\left[ 1 - \\left(\\frac{T}{T_c}\\right)^2 \\right]$$
Notice that at $T = 0$, $\\Delta S(0) = 0$ (Third law of thermodynamics), and at $T = T_c$, $\\Delta S(T_c) = 0$ (no latent heat).

**(b) Superconducting Electronic Specific Heat $C_s(T)$:**
From $C = T \\frac{dS}{dT}$:
$$C_n(T) - C_s(T) = T \\frac{d}{dT}[S_n - S_s] = T \\frac{d}{dT} \\left[ \\frac{2\\mu_0 H_0^2}{T_c^2} \\left( T - \\frac{T^3}{T_c^2} \\right) \\right] = \\frac{2\\mu_0 H_0^2}{T_c^2} T \\left( 1 - \\frac{3T^2}{T_c^2} \\right)$$
At $T = 0$, by the Third Law, $S_s(0) = S_n(0) = 0$. Since $S_n(T) = \\gamma T$, equating $S_n(T_c) = S_s(T_c)$:
$$\\gamma T_c = \\frac{2\\mu_0 H_0^2}{T_c} \\implies \\gamma = \\frac{2\\mu_0 H_0^2}{T_c^2}$$
Substituting $\\gamma$ into $C_n - C_s$:
$$C_n(T) - C_s(T) = \\gamma T \\left( 1 - \\frac{3T^2}{T_c^2} \\right) = \\gamma T - 3\\gamma \\frac{T^3}{T_c^2}$$
Since $C_n(T) = \\gamma T$:
$$C_s(T) = 3\\gamma \\frac{T^3}{T_c^2} = 3\\gamma T_c \\left(\\frac{T}{T_c}\\right)^3$$
In this simple parabolic model, the superconducting electronic specific heat exhibits a cubic $T^3$ temperature dependence! (Microscopic BCS theory actually yields an exponential activation $\\sim e^{-\\Delta/k_B T}$).

**(c) Discontinuous Specific Heat Jump:**
At $T = T_c$:
$$C_s(T_c) = 3\\gamma T_c$$
$$C_n(T_c) = \\gamma T_c$$
The specific heat jump is:
$$\\Delta C = C_s(T_c) - C_n(T_c) = 3\\gamma T_c - \\gamma T_c = 2\\gamma T_c$$
The normalized jump ratio is:
$$\\frac{\\Delta C}{C_n(T_c)} = \\frac{2\\gamma T_c}{\\gamma T_c} = 2.00$$
The empirical parabolic model predicts a ratio of **$2.00$**, which closely approximates the microscopic BCS weak-coupling universal value:
$$\\left(\\frac{\\Delta C}{C_n}\\right)_{\\text{BCS}} = 1.428$$
Strong-coupling superconductors (such as Pb and Hg) experimentally exhibit ratios between $1.8$ and $2.4$, perfectly matching this thermodynamic range."""
        },
        {
            "id": "ssp2-prob-5-3",
            "title": "Ginzburg-Landau Upper and Lower Critical Fields & Surface Energy Criterion",
            "statement": "In a Type-II superconductor with Ginzburg-Landau parameter $\\kappa = \\lambda/\\xi > 1/\\sqrt{2}$, the coherence length is $\\xi = 4.5\\text{ nm}$ and the London penetration depth is $\\lambda = 150\\text{ nm}$.\\n\\n(a) Compute $\\kappa$ and verify that the material is strongly Type-II.\\n(b) Using the single flux quantum $\\Phi_0 = 2.068 \\times 10^{-15}\\text{ Wb}$, calculate the upper critical field $B_{c2} = \\mu_0 H_{c2} = \\frac{\\Phi_0}{2\\pi \\xi^2}$ in Tesla.\\n(c) Using $B_{c1} = \\frac{\\Phi_0}{4\\pi \\lambda^2} \\ln\\kappa$, calculate the lower critical field $B_{c1}$ and the thermodynamic critical field $B_c = \\sqrt{B_{c1} B_{c2} / \\ln\\kappa}$.",
            "solution": """**(a) Ginzburg-Landau Parameter $\\kappa$:**
$$\\kappa = \\frac{\\lambda}{\\xi} = \\frac{150\\text{ nm}}{4.5\\text{ nm}} \\approx 33.33$$
Since $\\kappa = 33.33 \\gg 1/\\sqrt{2} \\approx 0.707$, the material is **strongly Type-II** (negative normal-superconductor surface energy).

**(b) Upper Critical Field $B_{c2}$:**
The upper critical field corresponds to the condition where neighboring vortex cores of radius $\\xi$ overlap:
$$B_{c2} = \\frac{\\Phi_0}{2\\pi \\xi^2} = \\frac{2.068 \\times 10^{-15}\\text{ Wb}}{2\\pi (4.5 \\times 10^{-9}\\text{ m})^2} = \\frac{2.068 \\times 10^{-15}}{2\\pi (20.25 \\times 10^{-18})} = \\frac{2.068 \\times 10^{-15}}{1.2723 \\times 10^{-16}} \\approx 16.25\\text{ Tesla}$$
This enormous upper critical field ($16.25\\text{ T}$) demonstrates why high-$\\kappa$ Type-II superconductors (such as $\\text{Nb}_3\\text{Sn}$) are used for high-field superconducting magnets.

**(c) Lower Critical Field $B_{c1}$ & Thermodynamic Field $B_c$:**
The lower critical field marks the threshold where the first isolated Abrikosov vortex penetrates:
$$\\ln\\kappa = \\ln(33.33) \\approx 3.5065$$
$$B_{c1} = \\frac{\\Phi_0}{4\\pi \\lambda^2} \\ln\\kappa = \\frac{2.068 \\times 10^{-15}}{4\\pi (150 \\times 10^{-9})^2} \\times 3.5065 = \\frac{2.068 \\times 10^{-15}}{2.8274 \\times 10^{-13}} \\times 3.5065 \\approx 7.314 \\times 10^{-3} \\times 3.5065 \\approx 0.0256\\text{ T} = 25.6\\text{ mT}$$
The thermodynamic critical field $B_c$ satisfies the Ginzburg-Landau relation $B_{c2} = \\sqrt{2} \\kappa B_c$:
$$B_c = \\frac{B_{c2}}{\\sqrt{2} \\kappa} = \\frac{16.25}{\\sqrt{2} \\times 33.33} = \\frac{16.25}{47.14} \\approx 0.345\\text{ Tesla} = 345\\text{ mT}$$
Notice the hierarchy:
$$B_{c1} (25.6\\text{ mT}) \\ll B_c (345\\text{ mT}) \\ll B_{c2} (16.25\\text{ T})$$
The mixed vortex state spans the massive field range between $25.6\\text{ mT}$ and $16.25\\text{ T}$."""
        }
    ]
}

# =========================================================================
# UNIT 6: Microscopic Superconductivity & Quantum Tunneling: BCS Theory, Josephson & SQUIDs
# =========================================================================

u6_data = {
    "title": "Microscopic Superconductivity & Quantum Tunneling: BCS Theory, Josephson & SQUIDs",
    "subtitle": "Cooper Pairs, Energy Gap, Josephson Effects, Shapiro Steps & High-Tc",
    "summary": "This unit covers the microscopic quantum mechanical theory of superconductivity and quantum phase coherence. We analyze the Fröhlich electron-phonon-electron attractive interaction, solve the Cooper pair two-electron bound state problem in a filled Fermi sea, and formulate the BCS variational ground state. We derive the temperature-dependent superconducting gap Delta(T), Bogoliubov quasiparticle excitations, and the isotope effect. Finally, we examine single-particle Giaever tunneling, macroscopic phase tunneling in DC/AC Josephson junctions, microwave Shapiro steps, ultra-sensitive DC SQUIDs, and the d-wave pairing of high-Tc cuprates.",
    "sections": [
        {
            "id": "sec-6-1",
            "title": "Microscopic Origin of Pairing: Electron-Phonon Interaction & The Cooper Pair Problem",
            "content": r"""
<h3>1. The Attractive Electron-Phonon Interaction</h3>
<p>
In 1950, Fröhlich pointed out that two electrons can experience an effective attractive interaction mediated by the polarizable positive ion lattice.
</p>
<p>
As an electron moves through the crystal, its negative charge attracts the positive ionic cores, creating a trailing localized concentration of positive charge (lattice polarization). Because the massive ions respond slowly on the timescale of the Debye frequency $\omega_D \sim 10^{13}\text{ s}^{-1}$, this positive wake persists long after the first electron has passed ($t \sim 2\pi/\omega_D \sim 10^{-13}\text{ s}$, during which an electron at the Fermi velocity $v_F \sim 10^6\text{ m/s}$ travels $\sim 100\text{ nm}$).
</p>
<p>
A second electron can then be attracted to this net positive wake. In second-order perturbation theory, the effective interaction between electrons with initial states $\vec{k}$ and $\vec{k}'$ exchanging a phonon $\vec{q}$ is:
</p>
$$V_{\text{eff}}(\vec{q}, \omega) = \frac{e^2}{\epsilon_0 q^2} + \frac{2 |M_{\vec{q}}|^2 \hbar\omega_{\vec{q}}}{(\epsilon_{\vec{k}'} - \epsilon_{\vec{k}})^2 - (\hbar\omega_{\vec{q}})^2}$$
<p>
Whenever $|\epsilon_{\vec{k}'} - \epsilon_{\vec{k}}| < \hbar\omega_D$, the phonon term becomes negative and overcomes the screened Coulomb repulsion, producing a net <strong>attractive pairing interaction</strong>!
</p>

<h3>2. The Cooper Pair Problem (1956)</h3>
<p>
Leon Cooper proved that the filled Fermi sea is fundamentally unstable against arbitrarily weak attraction.
</p>
<p>
Consider two electrons added to an inert, filled Fermi sea with Fermi momentum $k_F$. The pair wavefunction with zero total center-of-mass momentum ($\vec{k}_1 = \vec{k}, \vec{k}_2 = -\vec{k}$) and singlet spin is:
</p>
$$\psi(\vec{r}_1, \vec{r}_2) = \sum_{k > k_F} g(\vec{k}) e^{i \vec{k} \cdot (\vec{r}_1 - \vec{r}_2)} \chi_0^0$$
<p>
The Schrödinger equation is:
</p>
$$(2\epsilon_k - E) g(\vec{k}) + \sum_{k' > k_F} V_{\vec{k}\vec{k}'} g(\vec{k}') = 0$$
<p>
Assuming an attractive potential $-V$ within an energy shell $\hbar\omega_D$ above $E_F$:
</p>
$$V_{\vec{k}\vec{k}'} = \begin{cases} -V, & E_F < \epsilon_k, \epsilon_{k'} < E_F + \hbar\omega_D \\ 0, & \text{otherwise} \end{cases}$$
<p>
Setting $C \equiv \sum_{k'} g(\vec{k}') = \text{const}$:
</p>
$$g(\vec{k}) = \frac{V C}{2\epsilon_k - E} \implies \frac{1}{V} = \sum_{k > k_F} \frac{1}{2\epsilon_k - E} = \int_{E_F}^{E_F + \hbar\omega_D} \frac{N(0)}{2\epsilon - E} d\epsilon$$
<p>
Evaluating the integral:
</p>
$$\frac{1}{N(0)V} = \frac{1}{2} \ln\left( \frac{2E_F + 2\hbar\omega_D - E}{2E_F - E} \right)$$
<p>
Defining the binding energy $\Delta E \equiv 2E_F - E > 0$:
</p>
$$\Delta E \approx 2\hbar\omega_D \exp\left( -\frac{2}{N(0)V} \right)$$
<p>
Crucially, because $\Delta E > 0$ for any $V > 0$, electrons at the Fermi surface always bind into <strong>Cooper pairs</strong>! The non-analytic exponential factor $e^{-2/N(0)V}$ proves that superconductivity can never be derived by finite-order perturbation theory.
</p>
"""
        },
        {
            "id": "sec-6-2",
            "title": "BCS Ground State Wavefunction & The Variational Energy Minimization",
            "content": r"""
<h3>1. The BCS Many-Body Hamiltonian</h3>
<p>
In 1957, John Bardeen, Leon Cooper, and J. Robert Schrieffer published the microscopic <strong>BCS Theory</strong>. The reduced pairing Hamiltonian in second quantization is:
</p>
$$\hat{H}_{\text{BCS}} = \sum_{\vec{k}\sigma} \epsilon_k c_{\vec{k}\sigma}^\dagger c_{\vec{k}\sigma} - V \sum_{\vec{k},\vec{k}'} c_{\vec{k}\uparrow}^\dagger c_{-\vec{k}\downarrow}^\dagger c_{-\vec{k}'\downarrow} c_{\vec{k}'\uparrow}$$
<p>
Because Cooper pairs are bosons formed of fermions, the macroscopic ground state is not a simple Bose-Einstein condensate of independent molecules, but a coherent quantum superposition spanning the entire Fermi sea.
</p>

<h3>2. The BCS Ground State Wavefunction</h3>
<p>
The BCS trial ground state wavefunction is:
</p>
$$|\Psi_{\text{BCS}}\rangle = \prod_{\vec{k}} \left( u_{\vec{k}} + v_{\vec{k}} c_{\vec{k}\uparrow}^\dagger c_{-\vec{k}\downarrow}^\dagger \right) |0\rangle$$
<p>
where:
</p>
<ul>
  <li>$v_{\vec{k}}^2$ is the probability that the Cooper pair state $(\vec{k}\uparrow, -\vec{k}\downarrow)$ is <strong>occupied</strong>.</li>
  <li>$u_{\vec{k}}^2$ is the probability that the state is <strong>empty</strong>.</li>
  <li>Normalization requires $u_{\vec{k}}^2 + v_{\vec{k}}^2 = 1$.</li>
</ul>
<p>
Minimizing the expectation energy $\langle \Psi_{\text{BCS}} | \hat{H} - \mu \hat{N} | \Psi_{\text{BCS}} \rangle$ with respect to $v_{\vec{k}}$ yields:
</p>
$$u_{\vec{k}}^2 = \frac{1}{2} \left( 1 + \frac{\xi_k}{E_k} \right), \quad v_{\vec{k}}^2 = \frac{1}{2} \left( 1 - \frac{\xi_k}{E_k} \right)$$
<p>
where $\xi_k = \epsilon_k - \mu$ is the normal single-electron energy relative to the Fermi level, and $E_k$ is the <strong>Bogoliubov quasiparticle excitation energy</strong>:
</p>
$$E_k = \sqrt{\xi_k^2 + \Delta^2}$$
<p>
The minimum energy required to create a quasiparticle excitation is $E_{\min} = \Delta$. Breaking a Cooper pair requires minimum energy $2\Delta$, opening an <strong>energy gap</strong> $2\Delta$ centered symmetrically at the Fermi level!
</p>
"""
        },
        {
            "id": "sec-6-3",
            "title": "Temperature-Dependent BCS Energy Gap $\Delta(T)$, Quasiparticle Spectrum & Isotope Effect",
            "content": r"""
<h3>1. The BCS Gap Equation</h3>
<p>
At finite temperature $T$, thermal excitations create quasiparticles that block pair states. The self-consistent <strong>BCS gap equation</strong> is:
</p>
$$\frac{1}{N(0)V} = \int_0^{\hbar\omega_D} \frac{\tanh\left( \frac{\sqrt{\xi^2 + \Delta^2(T)}}{2k_B T} \right)}{\sqrt{\xi^2 + \Delta^2(T)}} d\xi$$
<ul>
  <li><strong>At $T = 0\text{ K}$ ($\tanh \to 1$):</strong>
  $$\frac{1}{N(0)V} = \int_0^{\hbar\omega_D} \frac{d\xi}{\sqrt{\xi^2 + \Delta_0^2}} = \operatorname{arcsinh}\left(\frac{\hbar\omega_D}{\Delta_0}\right) \approx \ln\left(\frac{2\hbar\omega_D}{\Delta_0}\right)$$
  $$\Delta(0) = 2\hbar\omega_D \exp\left( -\frac{1}{N(0)V} \right)$$</li>
  <li><strong>At $T = T_c$ ($\Delta \to 0$):</strong>
  $$\frac{1}{N(0)V} = \int_0^{\hbar\omega_D} \frac{\tanh(\xi / 2k_B T_c)}{\xi} d\xi = \ln\left( \frac{1.134 \hbar\omega_D}{k_B T_c} \right)$$
  $$k_B T_c = 1.134 \hbar\omega_D \exp\left( -\frac{1}{N(0)V} \right)$$</li>
</ul>
<p>
Taking the ratio eliminates the interaction parameters $N(0)V$ and $\omega_D$, yielding the <strong>universal BCS ratio</strong>:
</p>
$$\frac{2\Delta(0)}{k_B T_c} = \frac{2 \times 2}{1.134} \approx 3.528$$
<p>
For weakly coupled conventional superconductors, $2\Delta(0)/k_B T_c \approx 3.53$ is an exact universal constant!
</p>

<h3>2. The Isotope Effect</h3>
<p>
Because the Debye frequency $\omega_D \propto \sqrt{K/M} \propto M^{-1/2}$ depends inversely on the square root of the isotopic nuclear mass $M$, BCS theory predicts:
</p>
$$T_c \propto \omega_D \propto M^{-1/2} \implies T_c M^\alpha = \text{const}, \quad \alpha = 0.5$$
<p>
This <strong>isotope effect</strong> was experimentally discovered in mercury isotopes ($\text{Hg}^{198}$ to $\text{Hg}^{204}$) by Maxwell and Reynolds in 1950, providing definitive proof that electron-phonon interactions drive conventional superconductivity.
</p>
""",
            "simulation": "ssp2-bcs-gap-sim",
            "simulations": ["ssp2-bcs-gap-sim"]
        },
        {
            "id": "sec-6-4",
            "title": "Single-Particle Giaever Tunneling in Superconducting Junctions (S-I-N & S-I-S)",
            "content": r"""
<h3>1. Superconducting Density of States</h3>
<p>
From the Bogoliubov quasiparticle dispersion $E = \sqrt{\xi^2 + \Delta^2}$, the quasiparticle density of states $N_s(E)$ is related to the normal density of states $N(0)$ by particle conservation $N_s(E) dE = N(0) d\xi$:
</p>
$$N_s(E) = N(0) \frac{d\xi}{dE} = N(0) \frac{E}{\sqrt{E^2 - \Delta^2}}, \quad |E| > \Delta$$
$$N_s(E) = 0, \quad |E| < \Delta$$
<p>
The density of states vanishes completely inside the gap $|E| < \Delta$ and exhibits an inverse square-root square-integrable singularity at the gap edges $E = \pm\Delta$.
</p>

<h3>2. Giaever Tunneling Experiments</h3>
<p>
In 1960, Ivar Giaever fabricated thin-film planar junctions with an ultra-thin insulating oxide layer ($\sim 2\text{ nm}$ thick, e.g. $\text{Al}_2\text{O}_3$):
</p>
<ul>
  <li><strong>Superconductor-Insulator-Normal Metal (S-I-N) Junction:</strong>
  Applying a bias voltage $V$ shifts the Fermi level of the normal metal by $-eV$. Quasiparticles cannot tunnel until $e|V| \ge \Delta$.
  The tunneling differential conductance at $T \to 0\text{ K}$ directly measures the BCS density of states:
  $$\frac{dI}{dV} \propto N_s(eV) = N(0) \frac{eV}{\sqrt{(eV)^2 - \Delta^2}}$$
  The onset of current at $V = \Delta/e$ provides a direct spectroscopic measurement of the energy gap $\Delta(T)$.</li>
  <li><strong>Superconductor-Insulator-Superconductor (S-I-S) Junction:</strong>
  With two identical superconductors having gap $\Delta$, tunneling is blocked until $e|V| = 2\Delta$. At $V = 2\Delta/e$, the sharp singularity in the filled states of one electrode aligns with the singularity in the empty states of the other, causing a discontinuous jump in current.</li>
</ul>
"""
        },
        {
            "id": "sec-6-5",
            "title": "Cooper Pair Macroscopic Quantum Tunneling: The DC & AC Josephson Effects",
            "content": r"""
<h3>1. The DC Josephson Effect</h3>
<p>
In 1962, Brian Josephson predicted that Cooper pairs can tunnel quantum-mechanically across a thin insulating barrier separating two superconductors <em>without any applied voltage</em>.
</p>
<p>
Let $\psi_1 = \sqrt{n_1} e^{i\theta_1}$ and $\psi_2 = \sqrt{n_2} e^{i\theta_2}$ be the macroscopic wavefunctions of the two superconductors. Coupled Schrödinger equations across the barrier yield:
</p>
$$i\hbar \frac{\partial\psi_1}{\partial t} = E_1 \psi_1 + K \psi_2$$
$$i\hbar \frac{\partial\psi_2}{\partial t} = E_2 \psi_2 + K \psi_1$$
<p>
where $K$ is the coupling tunneling matrix element. Separating real and imaginary parts yields the <strong>DC Josephson Equation</strong>:
</p>
$$I = I_c \sin\phi$$
<p>
where $\phi \equiv \theta_2 - \theta_1$ is the gauge-invariant phase difference across the junction, and $I_c$ is the maximum zero-voltage critical supercurrent given by the Ambegaokar-Baratoff formula:
</p>
$$I_c = \frac{\pi \Delta(T)}{2e R_N} \tanh\left( \frac{\Delta(T)}{2k_B T} \right)$$
<p>
where $R_N$ is the normal-state junction resistance.
</p>

<h3>2. The AC Josephson Effect</h3>
<p>
When a constant DC voltage $V$ is applied across the junction, the energy difference between the Cooper pairs on opposite sides is $\Delta E = 2e V$. The phase evolves according to the <strong>AC Josephson Equation</strong>:
</p>
$$\frac{d\phi}{dt} = \frac{2e V}{\hbar} \implies \phi(t) = \phi_0 + \left( \frac{2e V}{\hbar} \right) t$$
<p>
Substituting into the current relation:
</p>
$$I(t) = I_c \sin\left( \phi_0 + \omega_J t \right)$$
<p>
A static DC voltage produces an <strong>alternating high-frequency supercurrent</strong> oscillating at the Josephson frequency:
</p>
$$\omega_J = \frac{2e V}{\hbar} \implies f_J = \frac{2e}{h} V = \frac{V}{\Phi_0}$$
<p>
Numerically, the frequency-to-voltage conversion ratio is:
</p>
$$\frac{f_J}{V} = \frac{2e}{h} \approx 483.5979\text{ GHz / mV} = 483.6\text{ MHz} / \mu\text{V}$$
<p>
Because frequency can be measured with atomic-clock accuracy, the AC Josephson effect provides the international metrological standard for the Volt.
</p>
"""
        },
        {
            "id": "sec-6-6",
            "title": "Microwave Shapiro Current Steps & Superconducting Quantum Interference Devices (SQUIDs)",
            "content": r"""
<h3>1. Microwave Shapiro Current Steps</h3>
<p>
When a Josephson junction is irradiated with RF microwave radiation of frequency $\omega$ in addition to a DC bias $V_0$:
</p>
$$V(t) = V_0 + V_1 \cos(\omega t)$$
<p>
Integrating the phase evolution equation $\frac{d\phi}{dt} = \frac{2e}{\hbar} V(t)$:
</p>
$$\phi(t) = \phi_0 + \left(\frac{2e V_0}{\hbar}\right) t + \frac{2e V_1}{\hbar\omega} \sin(\omega t)$$
<p>
Using the Jacobi-Anger Bessel function expansion $\sin(\alpha + z\sin\theta) = \sum_{n=-\infty}^\infty J_n(z) \sin(\alpha + n\theta)$:
</p>
$$I(t) = I_c \sum_{n=-\infty}^\infty (-1)^n J_n\left(\frac{2e V_1}{\hbar\omega}\right) \sin\left[ \phi_0 + \left(\frac{2e V_0}{\hbar} - n\omega\right) t \right]$$
<p>
Whenever the Josephson frequency matches an integer harmonic of the microwave frequency:
</p>
$$\frac{2e V_0}{\hbar} = n\omega \implies V_n = n \frac{\hbar\omega}{2e} = n \left(\frac{h\nu}{2e}\right)$$
<p>
The time-dependent term vanishes, producing constant DC current spikes known as <strong>Shapiro steps</strong>.
</p>

<h3>2. The DC SQUID (Superconducting Quantum Interference Device)</h3>
<p>
A DC SQUID consists of two identical Josephson junctions connected in parallel on a superconducting loop enclosing magnetic flux $\Phi$.
</p>
<p>
The total current is the sum of currents through branches $a$ and $b$:
</p>
$$I_{\text{tot}} = I_c \sin\phi_a + I_c \sin\phi_b = 2I_c \cos\left(\frac{\phi_a - \phi_b}{2}\right) \sin\left(\frac{\phi_a + \phi_b}{2}\right)$$
<p>
By flux quantization around the loop, the phase difference across the two junctions is locked to the enclosed magnetic flux:
</p>
$$\phi_a - \phi_b = \frac{2e}{\hbar} \Phi = 2\pi \frac{\Phi}{\Phi_0}$$
<p>
The maximum zero-voltage critical current is modulated by the magnetic flux:
</p>
$$I_{\max}(\Phi) = 2I_c \left| \cos\left( \pi \frac{\Phi}{\Phi_0} \right) \right|$$
<p>
The SQUID exhibits a periodic quantum interference pattern analogous to Young's double-slit experiment. By monitoring the voltage across a current-biased SQUID, magnetic field changes as minute as $10^{-15}\text{ Tesla}$ ($10^{-6} \Phi_0 / \sqrt{\text{Hz}}$) can be detected, enabling magnetoencephalography (MEG) of neural brain activity.
</p>
""",
            "simulation": "ssp2-josephson-squid-sim",
            "simulations": ["ssp2-josephson-squid-sim"]
        },
        {
            "id": "sec-6-7",
            "title": "Unconventional & High-Tc Superconductors: Cuprates, Iron Pnictides & d-Wave Symmetry",
            "content": r"""
<h3>1. Discovery of High-Temperature Cuprate Superconductors</h3>
<p>
In 1986, Georg Bednorz and K. Alex Müller discovered superconductivity in the copper oxide ceramic $\text{La}_{2-x}\text{Ba}_x\text{CuO}_4$ at $T_c = 35\text{ K}$, breaking the theoretical BCS phonon-mediated Eliashberg limit ($T_c \lesssim 30\text{ K}$).
</p>
<p>
Shortly thereafter in 1987, $\text{YBa}_2\text{Cu}_3\text{O}_{7-\delta}$ (YBCO) was discovered with $T_c = 93\text{ K}$, shattering the liquid nitrogen barrier ($77.3\text{ K}$). Subsequently, mercury cuprates reached $T_c = 138\text{ K}$ at ambient pressure and $164\text{ K}$ under $30\text{ GPa}$.
</p>

<h3>2. d-Wave Gap Symmetry & Electronic Pairing</h3>
<p>
High-$T_c$ cuprates possess quasi-2D layered perovskite crystal structures dominated by conducting $\text{CuO}_2$ planes separated by charge-reservoir oxide layers.
</p>
<p>
Key distinctions from conventional BCS superconductors:
</p>
<ul>
  <li><strong>Parent State is a Mott Insulator:</strong> Undoped cuprates ($\text{La}_2\text{CuO}_4$) are antiferromagnetic Mott insulators due to massive on-site Coulomb repulsion $U \approx 8\text{ eV} \gg t$. Superconductivity emerges upon hole-doping ($x \sim 0.05-0.25$) into a strongly correlated pseudogap regime.</li>
  <li><strong>Unconventional $d_{x^2-y^2}$ Order Parameter:</strong> While conventional superconductors have isotropic $s$-wave pairing ($\Delta = \text{const}$), cuprates exhibit $d$-wave pairing symmetry:
  $$\Delta(\vec{k}) = \Delta_0 (\cos k_x a - \cos k_y a)$$
  The gap changes sign across the Brillouin zone diagonals ($k_x = \pm k_y$), creating four gapless <strong>nodes</strong> on the Fermi surface where $\Delta(\vec{k}) = 0$.</li>
  <li><strong>Spin Fluctuation Pairing Mechanism:</strong> Instead of acoustic phonons, Cooper pairing is mediated by antiferromagnetic spin fluctuations (magnons) originating from the nearby Mott insulating phase.</li>
</ul>
<p>
In 2008, iron-based pnictide superconductors ($\text{LaO}_{1-x}\text{F}_x\text{FeAs}$, $T_c = 56\text{ K}$) were discovered, exhibiting multi-band $s_\pm$-wave pairing. In 2015-2020, hydrogen-rich polyhydrides under extreme megabar pressures reached record critical temperatures ($\text{H}_3\text{S}$ at $203\text{ K}$ at $150\text{ GPa}$, and $\text{LaH}_{10}$ at $250\text{ K}$ at $170\text{ GPa}$), representing phonon-driven conventional BCS pairing in ultra-dense hydrogen.
</p>
"""
        }
    ],
    "problems": [
        {
            "id": "ssp2-prob-6-1",
            "title": "Exact Solution of the Cooper Pair Problem in a Fermi Sea",
            "statement": "Two electrons with opposite momenta and spins $(\\vec{k}\\uparrow, -\\vec{k}\\downarrow)$ are added to a filled Fermi sea with Fermi energy $E_F$ and density of states $N(0)$. The attractive interaction is $V_{\\vec{k}\\vec{k}'} = -V$ for $E_F < \\epsilon_k, \\epsilon_{k'} < E_F + \\hbar\\omega_D$, and zero otherwise.\\n\\n(a) Solve the pair Schrödinger equation to derive the eigenvalue integral equation for total energy $E$.\\n(b) Evaluate the integral to derive the binding energy $\\Delta E = 2E_F - E$ in the weak-coupling limit $N(0)V \\ll 1$.\\n(c) Calculate the spatial root-mean-square Cooper pair size (coherence length $\\xi_0 \\sim \\hbar v_F / \\pi\\Delta$) for aluminum ($v_F = 2.02 \\times 10^6\\text{ m/s}, \\Delta = 0.18\\text{ meV}$), and compare it with the average interelectron spacing $r_s \\approx 0.1\\text{ nm}$.",
            "solution": """**(a) Pair Schrödinger Equation & Integral Formulation:**
The two-electron wavefunction expanded over plane waves above the Fermi surface is:
$$\\psi(\\vec{r}_1, \\vec{r}_2) = \\sum_{k > k_F} g(\\vec{k}) e^{i\\vec{k}\\cdot(\\vec{r}_1 - \\vec{r}_2)}$$
Substituting into $(H_0 + V)\\psi = E\\psi$:
$$(2\\epsilon_k - E) g(\\vec{k}) + \\sum_{k' > k_F} V_{\\vec{k}\\vec{k}'} g(\\vec{k}') = 0$$
With $V_{\\vec{k}\\vec{k}'} = -V$ within the energy shell $[E_F, E_F + \\hbar\\omega_D]$:
$$(2\\epsilon_k - E) g(\\vec{k}) - V \\sum_{k' > k_F} g(\\vec{k}') = 0$$
Let $C \\equiv \\sum_{k' > k_F} g(\\vec{k}')$. Then:
$$g(\\vec{k}) = \\frac{V C}{2\\epsilon_k - E}$$
Summing both sides over all $\\vec{k}$ in the shell:
$$C = \\sum_{k} \\frac{V C}{2\\epsilon_k - E} \\implies 1 = V \\sum_k \\frac{1}{2\\epsilon_k - E}$$
Replacing the momentum sum by the single-spin density of states $N(0)$ at $E_F$:
$$\\frac{1}{N(0)V} = \\int_{E_F}^{E_F + \\hbar\\omega_D} \\frac{d\\epsilon}{2\\epsilon - E}$$

**(b) Derivation of the Binding Energy:**
Let $u = 2\\epsilon - E \\implies du = 2d\\epsilon$:
$$\\frac{1}{N(0)V} = \\frac{1}{2} \\int_{2E_F - E}^{2E_F + 2\\hbar\\omega_D - E} \\frac{du}{u} = \\frac{1}{2} \\ln\\left( \\frac{2E_F + 2\\hbar\\omega_D - E}{2E_F - E} \\right)$$
Define the pair binding energy $\\Delta E \\equiv 2E_F - E > 0$:
$$\\frac{2}{N(0)V} = \\ln\\left( 1 + \\frac{2\\hbar\\omega_D}{\\Delta E} \\right)$$
Inverting the logarithm:
$$1 + \\frac{2\\hbar\\omega_D}{\\Delta E} = \\exp\\left( \\frac{2}{N(0)V} \\right)$$
$$\\frac{2\\hbar\\omega_D}{\\Delta E} = e^{2/N(0)V} - 1$$
In the weak-coupling regime $N(0)V \\ll 1$, $e^{2/N(0)V} \\gg 1$:
$$\\Delta E = \\frac{2\\hbar\\omega_D}{e^{2/N(0)V} - 1} \\approx 2\\hbar\\omega_D \\exp\\left( -\\frac{2}{N(0)V} \\right)$$
This proves that the two electrons bind into a lower-energy state ($\Delta E > 0$) for *any* attractive potential $V > 0$, no matter how weak.

**(c) Cooper Pair Size in Aluminum:**
Given:
$$v_F = 2.02 \\times 10^6\\text{ m/s}$$
$$\\Delta = 0.18\\text{ meV} = 0.18 \\times 10^{-3} \\times 1.602 \\times 10^{-19}\\text{ J} \\approx 2.884 \\times 10^{-23}\\text{ J}$$
$$\\hbar = 1.0546 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$$
The Pippard/BCS coherence length is:
$$\\xi_0 = \\frac{\\hbar v_F}{\\pi \\Delta} = \\frac{(1.0546 \\times 10^{-34})(2.02 \\times 10^6)}{\\pi (2.884 \\times 10^{-23})} = \\frac{2.130 \\times 10^{-28}}{9.060 \\times 10^{-23}} \\approx 2.35 \\times 10^{-6}\\text{ m} = 2350\\text{ nm} = 2.35\\ \\mu\\text{m}$$
Comparing with the interelectron spacing $r_s \\approx 0.1\\text{ nm}$:
$$\\frac{\\xi_0}{r_s} = \\frac{2350\\text{ nm}}{0.1\\text{ nm}} \\approx 23{,}500$$
A single Cooper pair spans a gigantic volume enclosing roughly $10^6$ to $10^7$ other overlapping Cooper pairs! This massive spatial overlap prevents pairs from acting as isolated molecules, requiring the full many-body BCS collective wavefunction."""
        },
        {
            "id": "ssp2-prob-6-2",
            "title": "BCS Gap Equation: Analytical Derivation of Delta(0) and the Universal Ratio",
            "statement": "The BCS gap equation is $\\frac{1}{N(0)V} = \\int_0^{\\hbar\\omega_D} \\frac{\\tanh(E/2k_B T)}{E} d\\xi$, where $E = \\sqrt{\\xi^2 + \\Delta^2(T)}$.\\n\\n(a) Evaluate the integral at $T = 0\\text{ K}$ to derive the zero-temperature gap $\\Delta(0) = 2\\hbar\\omega_D e^{-1/N(0)V}$.\\n(b) Evaluate the integral at $T = T_c$ where $\\Delta(T_c) \\to 0$, using the standard integral $\\int_0^X \\frac{\\tanh(x)}{x} dx = \\ln\\left(\\frac{4 e^{-\\gamma} X}{\\pi}\\right)$ (Euler's constant $\\gamma \\approx 0.5772$), to prove $k_B T_c = \\frac{2 e^\\gamma}{\\pi} \\hbar\\omega_D e^{-1/N(0)V} \\approx 1.134 \\hbar\\omega_D e^{-1/N(0)V}$.\\n(c) Take the ratio to prove the universal BCS constant $\\frac{2\\Delta(0)}{k_B T_c} = \\frac{2\\pi}{e^\\gamma} \\approx 3.528$.",
            "solution": """**(a) Gap at $T = 0\\text{ K}$:**
At $T = 0\\text{ K}$, $\\tanh(E/2k_B T) = 1$. The gap equation becomes:
$$\\frac{1}{N(0)V} = \\int_0^{\\hbar\\omega_D} \\frac{d\\xi}{\\sqrt{\\xi^2 + \\Delta_0^2}}$$
Using the standard substitution $\\xi = \\Delta_0 \\sinh u, d\\xi = \\Delta_0 \\cos u du$:
$$\\int_0^{\\hbar\\omega_D} \\frac{d\\xi}{\\sqrt{\\xi^2 + \\Delta_0^2}} = \\operatorname{arcsinh}\\left( \\frac{\\hbar\\omega_D}{\\Delta_0} \\right) = \\ln\\left( \\frac{\\hbar\\omega_D}{\\Delta_0} + \\sqrt{1 + \\left(\\frac{\\hbar\\omega_D}{\\Delta_0}\\right)^2} \\right)$$
In the weak-coupling regime $\\hbar\\omega_D \\gg \\Delta_0$:
$$\\operatorname{arcsinh}\\left(\\frac{\\hbar\\omega_D}{\\Delta_0}\\right) \\approx \\ln\\left( \\frac{2\\hbar\\omega_D}{\\Delta_0} \\right)$$
$$\\frac{1}{N(0)V} = \\ln\\left( \\frac{2\\hbar\\omega_D}{\\Delta_0} \\right) \\implies \\Delta(0) = 2\\hbar\\omega_D \\exp\\left( -\\frac{1}{N(0)V} \\right)$$

**(b) Critical Temperature $T_c$ (where $\\Delta \\to 0$):**
At $T = T_c$, $\\Delta = 0$, so $E = |\\xi| = \\xi$:
$$\\frac{1}{N(0)V} = \\int_0^{\\hbar\\omega_D} \\frac{\\tanh(\\xi / 2k_B T_c)}{\\xi} d\\xi$$
Let $x = \\xi / 2k_B T_c$, with upper limit $X = \\hbar\\omega_D / 2k_B T_c \\gg 1$:
$$\\int_0^X \\frac{\\tanh x}{x} dx = [\\tanh x \\ln x]_0^X - \\int_0^X \\frac{\\ln x}{\\cosh^2 x} dx \\approx \\ln X - \\int_0^\\infty \\frac{\\ln x}{\\cosh^2 x} dx$$
The definite integral evaluates exactly to $\\int_0^\\infty \\frac{\\ln x}{\\cosh^2 x} dx = -\\ln\\left(\\frac{4 e^\\gamma}{\\pi}\\right)$, where $\\gamma = 0.57721566\\dots$ is the Euler-Mascheroni constant:
$$\\int_0^X \\frac{\\tanh x}{x} dx = \\ln X + \\ln\\left(\\frac{4 e^\\gamma}{\\pi}\\right) = \\ln\\left( \\frac{4 e^\\gamma X}{\\pi} \\right) = \\ln\\left( \\frac{4 e^\\gamma}{\\pi} \\frac{\\hbar\\omega_D}{2k_B T_c} \\right) = \\ln\\left( \\frac{2 e^\\gamma}{\\pi} \\frac{\\hbar\\omega_D}{k_B T_c} \\right)$$
Equating to $\\frac{1}{N(0)V}$:
$$\\ln\\left( \\frac{2 e^\\gamma}{\\pi} \\frac{\\hbar\\omega_D}{k_B T_c} \\right) = \\frac{1}{N(0)V}$$
$$k_B T_c = \\frac{2 e^\\gamma}{\\pi} \\hbar\\omega_D \\exp\\left( -\\frac{1}{N(0)V} \\right)$$
Since $\\frac{2 e^\\gamma}{\\pi} = \\frac{2 \\times 1.78107}{3.14159} \\approx 1.13386$:
$$k_B T_c \\approx 1.134 \\hbar\\omega_D \\exp\\left( -\\frac{1}{N(0)V} \\right)$$

**(c) Universal Ratio:**
Dividing $2\\Delta(0)$ by $k_B T_c$:
$$\\frac{2\\Delta(0)}{k_B T_c} = \\frac{2 \\left[ 2\\hbar\\omega_D e^{-1/N(0)V} \\right]}{\\left[ \\frac{2 e^\\gamma}{\\pi} \\hbar\\omega_D e^{-1/N(0)V} \\right]} = \\frac{4}{\\frac{2 e^\\gamma}{\\pi}} = \\frac{2\\pi}{e^\\gamma}$$
Evaluating numerically:
$$\\frac{2\\pi}{e^\\gamma} = \\frac{2 \\times 3.14159265}{1.7810724} \\approx 3.52776 \\approx 3.528$$
This proves that the ratio $\\frac{2\\Delta(0)}{k_B T_c} = 3.528$ is a **universal dimensionless constant** in BCS theory, independent of the material's specific Debye frequency $\\omega_D$, density of states $N(0)$, and coupling strength $V$."""
        },
        {
            "id": "ssp2-prob-6-3",
            "title": "AC Josephson Effect & Microwave Shapiro Current Step Heights",
            "statement": "A Josephson junction with critical current $I_c = 50\\ \\mu\\text{A}$ is subjected to a combined bias voltage $V(t) = V_0 + V_1 \\cos(\\omega t)$, where $\\omega / 2\\pi = 10.0\\text{ GHz}$ and $V_1 = 40.0\\ \\mu\\text{V}$.\\n\\n(a) Compute the voltage spacing $\\Delta V$ between successive microwave Shapiro current steps in $\\mu\\text{V}$.\\n(b) Using the Bessel function expansion $I_n = I_c J_n\\left(\\frac{2e V_1}{\\hbar\\omega}\\right)$, calculate the dimensionless argument $z = \\frac{2e V_1}{\\hbar\\omega}$.\\n(c) Using $J_0(1.93) \\approx 0.282$, $J_1(1.93) \\approx 0.581$, and $J_2(1.93) \\approx 0.334$, compute the critical current step heights for $n = 0, 1, 2$ in $\\mu\\text{A}$.",
            "solution": """**(a) Voltage Spacing of Shapiro Steps:**
The condition for the $n$-th Shapiro step is:
$$V_n = n \\frac{\\hbar\\omega}{2e} = n \\frac{h\\nu}{2e}$$
The spacing between consecutive steps ($n$ and $n+1$) is:
$$\\Delta V = \\frac{h\\nu}{2e} = \\frac{\\nu}{2e/h}$$
Using $\\nu = 10.0\\text{ GHz} = 1.0 \\times 10^{10}\\text{ Hz}$ and $2e/h \\approx 483.5979\\text{ GHz/mV}$:
$$\\Delta V = \\frac{10.0\\text{ GHz}}{483.5979\\text{ GHz/mV}} = 0.020678\\text{ mV} = 20.68\\ \\mu\\text{V}$$
Successive Shapiro current steps occur at intervals of **$20.68\\ \\mu\\text{V}$**.

**(b) Dimensionless Bessel Argument $z$:**
$$z = \\frac{2e V_1}{\\hbar\\omega} = \\frac{V_1}{\\hbar\\omega / 2e} = \\frac{V_1}{\\Delta V}$$
Given $V_1 = 40.0\\ \\mu\\text{V}$ and $\\Delta V = 20.68\\ \\mu\\text{V}$:
$$z = \\frac{40.0\\ \\mu\\text{V}}{20.678\\ \\mu\\text{V}} \\approx 1.934$$

**(c) Shapiro Step Current Heights:**
The DC current height of the $n$-th Shapiro step is $2 I_c |J_n(z)|$:
Given $I_c = 50.0\\ \\mu\\text{A}$:
- For $n = 0$ (Zero-voltage supercurrent step):
$$I_0 = I_c J_0(1.93) = 50.0 \\times 0.282 \\approx 14.1\\ \\mu\\text{A} \\quad (\\text{Half-height } 14.1\\ \\mu\\text{A}, \\text{full step } 28.2\\ \\mu\\text{A})$$
- For $n = 1$ (First Shapiro step at $V_1 = 20.68\\ \\mu\\text{V}$):
$$I_1 = I_c J_1(1.93) = 50.0 \\times 0.581 \\approx 29.05\\ \\mu\\text{A} \\quad (\\text{Full step width } 58.1\\ \\mu\\text{A})$$
- For $n = 2$ (Second Shapiro step at $V_2 = 41.36\\ \\mu\\text{V}$):
$$I_2 = I_c J_2(1.93) = 50.0 \\times 0.334 \\approx 16.7\\ \\mu\\text{A} \\quad (\\text{Full step width } 33.4\\ \\mu\\text{A})$$
Notice that because $z \\approx 1.93$, the first Shapiro step ($n = 1$) is even larger than the zero-voltage supercurrent ($n = 0$), providing a clear experimental signature of phase-locking between the Josephson frequency and the external microwave drive."""
        }
    ]
}

with open("ssp2_u5.json", "w", encoding="utf-8") as f:
    json.dump(u5_data, f, indent=2)

with open("ssp2_u6.json", "w", encoding="utf-8") as f:
    json.dump(u6_data, f, indent=2)

print("Generated ssp2_u5.json and ssp2_u6.json successfully.")
