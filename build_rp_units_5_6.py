# -*- coding: utf-8 -*-
"""
Builder for Nuclear Reactor Physics Units 5 & 6
Unit 5: Neutron Diffusion Theory & Fermi Age Slowing Down
Unit 6: Neutron Chain Reactions, Multiplication & The Four/Six-Factor Formulas
"""
import json

u5_data = {
    "title": "Neutron Diffusion Theory & Fermi Age Slowing Down",
    "subtitle": "Boltzmann Transport, Fick's Law, Extrapolated Boundaries, Point Solutions & Fermi Age Equation",
    "summary": "Mathematical formulation of neutron transport and spatial diffusion theory: six-dimensional phase-space angular flux and rigorous derivation of the steady-state Boltzmann integro-differential transport equation; spherical harmonics P1 expansion, transport mean free path, and mathematical derivation of Fick's law of diffusion; one-speed steady-state neutron continuity and diffusion equations; physical boundary conditions, interface flux/current continuity, and the exact extrapolated boundary distance d = 0.7104 lambda_tr from Milne's transport theory; canonical solutions for point, line, and planar neutron sources in infinite moderating media, and thermal diffusion length L = sqrt(D/Sigma_a); Fermi age theory for continuous slowing down, the Fourier-Laplace solution of the age equation nabla^2 q = dq/d tau, and the Gaussian spatial slowing down kernel; migration area M^2 = L^2 + tau, migration length M, and spatial dispersion of fission neutrons.",
    "sections": [
        {
            "id": "sec-5-1",
            "title": "Fundamentals of Neutron Transport: Phase-Space Angular Flux & Boltzmann Equation",
            "content": r"""
<h3>1. Phase Space and Angular Flux</h3>
<p>
A complete statistical description of a neutron gas requires a six-dimensional phase space: position $\vec{r} = (x, y, z)$ and velocity $\vec{v} = v \vec{\Omega}$ (or energy $E = \frac{1}{2} m v^2$ and unit direction vector $\vec{\Omega} \in S^2$).
The <strong>angular neutron density</strong> $n(\vec{r}, \vec{\Omega}, E, t)$ is defined such that:
$$n(\vec{r}, \vec{\Omega}, E, t) \, d^3 r \, d\Omega \, dE$$
is the expected number of neutrons in spatial volume $d^3 r$ around $\vec{r}$, with kinetic energies in $(E, E+dE)$, traveling in direction cone $d\Omega$ around $\vec{\Omega}$ at time $t$.
The fundamental quantity of transport theory is the <strong>angular neutron flux</strong> $\psi$:
$$\psi(\vec{r}, \vec{\Omega}, E, t) \equiv v \, n(\vec{r}, \vec{\Omega}, E, t)$$
Integrating over all $4\pi$ steradians yields the <strong>scalar neutron flux</strong> $\phi$:
$$\phi(\vec{r}, E, t) = \int_{4\pi} \psi(\vec{r}, \vec{\Omega}, E, t) \, d\Omega = v \, n(\vec{r}, E, t)$$
The net <strong>neutron current density vector</strong> $\vec{J}$ is the first directional moment:
$$\vec{J}(\vec{r}, E, t) = \int_{4\pi} \vec{\Omega} \, \psi(\vec{r}, \vec{\Omega}, E, t) \, d\Omega$$
</p>

<h3>2. The Steady-State Boltzmann Neutron Transport Equation</h3>
<p>
Balancing neutron gains and losses in an infinitesimal phase-space cell $d^3 r \, d\Omega \, dE$:
$$\text{Streaming Loss} + \text{Collision Removal} = \text{In-Scattering Gain} + \text{Fission / External Source}$$
$$\mathbf{\vec{\Omega} \cdot \nabla \psi(\vec{r}, \vec{\Omega}, E) + \Sigma_t(\vec{r}, E) \psi(\vec{r}, \vec{\Omega}, E) = \int_{0}^{\infty} dE' \int_{4\pi} d\Omega' \, \Sigma_s(E' \to E, \vec{\Omega}' \to \vec{\Omega}) \psi(\vec{r}, \vec{\Omega}', E') + S(\vec{r}, \vec{\Omega}, E)}$$
This is the linear <strong>Boltzmann Integro-Differential Transport Equation</strong>. Because exact analytical solutions exist only for idealized infinite half-spaces, reactor physics employs systematic angular approximations—principally the <strong>Diffusion ($P_1$) Approximation</strong>.
</p>
"""
        },
        {
            "id": "sec-5-2",
            "title": "The P1 Approximation, Transport Mean Free Path & Derivation of Fick's Law",
            "content": r"""
<h3>1. The Spherical Harmonics $P_1$ Expansion</h3>
<p>
In media where scattering dominates absorption ($\Sigma_s \gg \Sigma_a$) and locations are several mean free paths away from boundaries and localized sources, the angular flux is nearly isotropic with a small directional bias:
$$\psi(\vec{r}, \vec{\Omega}) \approx \frac{1}{4\pi} \phi(\vec{r}) + \frac{3}{4\pi} \vec{\Omega} \cdot \vec{J}(\vec{r})$$
This two-term expansion in Legendre polynomials ($P_0$ and $P_1$) is the <strong>$P_1$ approximation</strong>.
</p>

<h3>2. Derivation of Fick's Law of Diffusion</h3>
<p>
Substitute the $P_1$ expansion into the monoenergetic transport equation:
$$\vec{\Omega} \cdot \nabla \left[ \frac{1}{4\pi} \phi + \frac{3}{4\pi} \vec{\Omega} \cdot \vec{J} \right] + \Sigma_t \left[ \frac{1}{4\pi} \phi + \frac{3}{4\pi} \vec{\Omega} \cdot \vec{J} \right] = \frac{1}{4\pi} \Sigma_s \phi + \frac{3}{4\pi} \Sigma_s \bar{\mu}_0 \vec{\Omega} \cdot \vec{J} + \frac{S}{4\pi}$$
To extract the vector current equation, multiply the entire transport equation by $\vec{\Omega}$ and integrate over all solid angles $\int_{4\pi} d\Omega$:
Using the solid angle identities:
$$\int_{4\pi} \vec{\Omega} \, d\Omega = 0, \qquad \int_{4\pi} \Omega_i \Omega_j \, d\Omega = \frac{4\pi}{3} \delta_{ij}$$
The streaming term becomes:
$$\int_{4\pi} \vec{\Omega} (\vec{\Omega} \cdot \nabla \phi) \, d\Omega = \frac{4\pi}{3} \nabla \phi$$
The collision and scattering terms become:
$$\frac{3}{4\pi} (\Sigma_t - \bar{\mu}_0 \Sigma_s) \int_{4\pi} \vec{\Omega} (\vec{\Omega} \cdot \vec{J}) \, d\Omega = (\Sigma_t - \bar{\mu}_0 \Sigma_s) \vec{J} \equiv \Sigma_{\text{tr}} \vec{J}$$
Equating both sides yields:
$$\frac{1}{3} \nabla \phi + \Sigma_{\text{tr}} \vec{J} = 0 \implies \mathbf{\vec{J}(\vec{r}) = - \frac{1}{3 \Sigma_{\text{tr}}} \nabla \phi(\vec{r}) = - D \nabla \phi(\vec{r})}$$
This is <strong>Fick's Law of Neutron Diffusion</strong>!
The <strong>diffusion coefficient</strong> $D$ is:
$$\mathbf{D = \frac{1}{3 \Sigma_{\text{tr}}} = \frac{1}{3 \Sigma_s (1 - \bar{\mu}_0)} = \frac{\lambda_{\text{tr}}}{3}}$$
</p>

<h3>3. Validity Conditions for Fick's Law</h3>
<p>
Fick's law is valid under four strict physical conditions:
<ol>
  <li>The medium is weakly absorbing: $\Sigma_a \ll \Sigma_s$.</li>
  <li>Scattering is linearly anisotropic in the LAB frame ($\bar{\mu}_0 = 2/(3A)$).</li>
  <li>The point of observation is at least $2\text{ to }3$ mean free paths away from strong localized sources.</li>
  <li>The point of observation is at least $2\text{ to }3$ mean free paths away from vacuum boundaries or material interfaces.</li>
</ol>
</p>
"""
        },
        {
            "id": "sec-5-3",
            "title": "One-Speed Steady-State Neutron Continuity and Diffusion Equation",
            "content": r"""
<h3>1. The Continuity Equation</h3>
<p>
Consider an arbitrary volume $V$ bounded by surface $S$. At steady state, the rate of neutron loss must balance the rate of neutron production:
$$\int_S \vec{J} \cdot d\vec{A} + \int_V \Sigma_a \phi \, dV = \int_V S \, dV$$
Applying Gauss's divergence theorem to the surface leakage integral:
$$\int_V \left( \nabla \cdot \vec{J} + \Sigma_a \phi - S \right) dV = 0$$
Since this holds for any arbitrary volume, the differential <strong>neutron continuity equation</strong> is:
$$\mathbf{\nabla \cdot \vec{J}(\vec{r}) + \Sigma_a \phi(\vec{r}) = S(\vec{r})}$$
</p>

<h3>2. The Steady-State Diffusion Equation</h3>
<p>
Substituting Fick's Law $\vec{J} = -D \nabla\phi$ into the continuity equation (assuming uniform diffusion coefficient $D$):
$$\nabla \cdot (-D \nabla \phi) + \Sigma_a \phi = S(\vec{r})$$
$$\mathbf{-D \nabla^2 \phi(\vec{r}) + \Sigma_a \phi(\vec{r}) = S(\vec{r})}$$
Dividing through by $D$:
$$\mathbf{-\nabla^2 \phi(\vec{r}) + \frac{1}{L^2} \phi(\vec{r}) = \frac{S(\vec{r})}{D}}$$
where $L$ is the fundamental <strong>thermal neutron diffusion length</strong>:
$$\mathbf{L \equiv \sqrt{\frac{D}{\Sigma_a}} = \sqrt{\frac{1}{3 \Sigma_{\text{tr}} \Sigma_a}}}$$
In source-free regions ($S = 0$), the homogeneous diffusion equation reduces to the screened Poisson / Helmholtz form:
$$\mathbf{\nabla^2 \phi(\vec{r}) - \frac{1}{L^2} \phi(\vec{r}) = 0}$$
</p>
"""
        },
        {
            "id": "sec-5-4",
            "title": "Physical Boundary Conditions & Extrapolated Boundary Distance d = 0.71 lambda_tr",
            "content": r"""
<h3>1. Interface Continuity Conditions</h3>
<p>
At an interface between two distinct multiplying or moderating media (Medium 1 and Medium 2):
<ol>
  <li><strong>Continuity of Neutron Flux:</strong>
  $$\phi_1(\vec{r}_{\text{int}}) = \phi_2(\vec{r}_{\text{int}})$$
  (Neutron density cannot jump discontinuously across a mathematical plane).</li>
  <li><strong>Continuity of Normal Current Density:</strong>
  $$-D_1 \left( \nabla \phi_1 \cdot \hat{n} \right) = -D_2 \left( \nabla \phi_2 \cdot \hat{n} \right)$$
  (Neutrons are conserved; no neutrons can accumulate on a boundary of zero thickness).</li>
</ol>
</p>

<h3>2. Vacuum Boundary and Extrapolated Distance</h3>
<p>
At a vacuum boundary (outer surface of a reactor core adjacent to vacuum or air), no neutrons can enter the reactor from the outside:
$$J_-(\vec{r}_s) = \int_{\vec{\Omega} \cdot \hat{n} < 0} |\vec{\Omega} \cdot \hat{n}| \psi(\vec{r}_s, \vec{\Omega}) \, d\Omega = 0$$
Using the $P_1$ partial currents formula:
$$J_{\pm} = \frac{\phi}{4} \mp \frac{D}{2} \frac{d\phi}{dn} = 0 \implies \frac{\phi}{4} + \frac{D}{2} \frac{d\phi}{dn} = 0 \implies \frac{\phi}{|d\phi/dn|} = 2D = \frac{2}{3} \lambda_{\text{tr}}$$
Linear extrapolation predicts that the asymptotic flux vanishes at a distance $d$ outside the physical surface:
$$d = \frac{2}{3} \lambda_{\text{tr}} \approx 0.667 \, \lambda_{\text{tr}} \quad (P_1\text{ approximation})$$
</p>

<h3>3. Exact Transport Result: Milne's Integral Problem</h3>
<p>
A rigorous transport-theoretic solution of the Milne problem (Wiener-Hopf method) demonstrates that the true asymptotic neutron flux vanishes outside the physical boundary at:
$$\mathbf{d = 0.710446 \, \lambda_{\text{tr}} \approx 0.71 \, \lambda_{\text{tr}} = \frac{0.71}{\Sigma_{\text{tr}}}}$$
The <strong>extrapolated boundary</strong> $\tilde{R} = R + d$ allows reactor physicists to apply the simple Dirichlet boundary condition:
$$\mathbf{\phi(\tilde{R}) = \phi(R + d) = 0}$$
</p>
"""
        },
        {
            "id": "sec-5-5",
            "title": "Fundamental Solutions of Diffusion Equation & Thermal Diffusion Length",
            "content": r"""
<h3>1. Point Isotropic Source in an Infinite Medium</h3>
<p>
Consider a point source emitting $S$ monoenergetic neutrons per second at the origin $\vec{r} = 0$ in an infinite homogeneous moderator.
In spherical coordinates with radial symmetry, the source-free diffusion equation for $r > 0$ is:
$$\frac{1}{r^2} \frac{d}{dr}\left( r^2 \frac{d\phi}{dr} \right) - \frac{1}{L^2} \phi(r) = 0$$
Making the substitution $w(r) = r \phi(r)$:
$$\frac{d^2 w}{dr^2} - \frac{1}{L^2} w = 0 \implies w(r) = A e^{-r/L} + C e^{+r/L}$$
Since physical flux must remain bounded as $r \to \infty$, $C = 0$:
$$\phi(r) = \frac{A}{r} e^{-r/L}$$
To evaluate $A$, enforce source conservation as $r \to 0$:
$$\lim_{r \to 0} 4\pi r^2 J(r) = \lim_{r \to 0} \left[ -4\pi r^2 D \frac{d\phi}{dr} \right] = 4\pi D A = S \implies A = \frac{S}{4\pi D}$$
The exact Green's function for a point source in 3D diffusion theory is:
$$\mathbf{\phi(r) = \frac{S}{4\pi D r} e^{-r/L}}$$
</p>

<h3>2. Planar Infinite Sheet Source</h3>
<p>
For an infinite planar sheet source at $x = 0$ emitting $S_{\text{plane}}$ neutrons/$\text{cm}^2\cdot\text{s}$ into an infinite medium:
$$\frac{d^2\phi}{dx^2} - \frac{1}{L^2} \phi = 0 \implies \mathbf{\phi(x) = \frac{S_{\text{plane}} L}{2 D} e^{-|x|/L}}$$
</p>

<h3>3. Physical Interpretation of Diffusion Length $L$</h3>
<p>
The mean square distance $\langle r^2 \rangle$ that a thermal neutron travels from its point of birth (thermalization) to its point of ultimate absorption is:
$$\langle r^2 \rangle = \frac{\int_0^\infty r^2 \, \Sigma_a \phi(r) \cdot 4\pi r^2 dr}{\int_0^\infty \Sigma_a \phi(r) \cdot 4\pi r^2 dr} = \frac{\int_0^\infty r^3 e^{-r/L} dr}{\int_0^\infty r e^{-r/L} dr} = \frac{3! L^4}{1! L^2} = 6 L^2$$
Therefore:
$$\mathbf{L^2 = \frac{1}{6} \langle r^2 \rangle \implies L = \sqrt{\frac{\langle r^2 \rangle}{6}}}$$
$L$ is directly proportional to the root-mean-square net displacement of a thermal neutron before absorption!
</p>
"""
        },
        {
            "id": "sec-5-6",
            "title": "Fast Neutron Slowing Down and Fermi Age Theory: Age Equation & Gaussian Kernel",
            "content": r"""
<h3>1. The Fermi Continuous Slowing Down Model</h3>
<p>
In intermediate and heavy moderators, neutrons undergo many collisions with small fractional energy loss, behaving as a continuous fluid slowing down from birth energy $E_0$ toward thermal energy $E_{\text{th}}$.
Combining the slowing down density $q(\vec{r}, E) = \xi \Sigma_s E \phi(\vec{r}, E)$ with the spatial leakage $-D(E) \nabla^2 \phi$:
$$\nabla \cdot \vec{J}(\vec{r}, E) + \frac{\partial q(\vec{r}, E)}{\partial u} = 0 \implies -D(E) \nabla^2 \phi + \frac{\partial q}{\partial u} = 0$$
Since $\phi = \frac{q}{\xi \Sigma_s E}$, we obtain:
$$\frac{D(E)}{\xi \Sigma_s(E)} \nabla^2 q(\vec{r}, E) = -E \frac{\partial q}{\partial E}$$
</p>

<h3>2. Definition of Fermi Age $\tau$</h3>
<p>
Enrico Fermi defined the <strong>age</strong> parameter $\tau(E)$ (having dimensions of $\text{length}^2 = \text{cm}^2$):
$$\mathbf{\tau(E) \equiv \int_{E}^{E_0} \frac{D(E')}{\xi \Sigma_s(E')} \frac{dE'}{E'} = \int_{0}^{u} \frac{D(u')}{\xi \Sigma_s(u')} du'}$$
By construction, $d\tau = - \frac{D(E)}{\xi \Sigma_s E} dE$. Substituting into the slowing down equation yields the celebrated <strong>Fermi Age Equation</strong>:
$$\mathbf{\nabla^2 q(\vec{r}, \tau) = \frac{\partial q(\vec{r}, \tau)}{\partial \tau}}$$
This equation is mathematically isomorphic to Fourier's classical heat conduction equation $\nabla^2 T = \frac{1}{\alpha} \frac{\partial T}{\partial t}$, where Fermi age $\tau$ plays the role of time!
</p>

<h3>3. Gaussian Spatial Slowing Down Kernel</h3>
<p>
For a point burst of $S$ fission neutrons born at the origin at age $\tau = 0$ ($q(\vec{r}, 0) = S \delta(\vec{r})$), the solution of the Fermi age equation is the 3D Gaussian distribution:
$$\mathbf{q(r, \tau) = \frac{S}{(4\pi \tau)^{3/2}} \exp\left( - \frac{r^2}{4\tau} \right)}$$
The mean square slowing-down distance from fission to thermal energy $\tau_{\text{th}}$ is:
$$\langle r_s^2 \rangle = \frac{\int_0^\infty r^2 q(r, \tau) 4\pi r^2 dr}{\int_0^\infty q(r, \tau) 4\pi r^2 dr} = 6 \tau_{\text{th}}$$
Hence:
$$\mathbf{\tau_{\text{th}} = \frac{1}{6} \langle r_s^2 \rangle \equiv L_s^2}$$
where $L_s$ is the <strong>slowing-down length</strong> of the moderator!
</p>
"""
        },
        {
            "id": "sec-5-7",
            "title": "Migration Area M^2 = L^2 + tau, Migration Length & Spatial Dispersion",
            "content": r"""
<h3>1. The Migration Area $M^2$</h3>
<p>
A neutron born in fission travels a distance while slowing down to thermal energy (characterized by Fermi age $\tau$), and then travels an additional distance as a thermal neutron before being absorbed (characterized by diffusion area $L^2$).
The total mean square displacement from fission birth to ultimate absorption is the sum of the two independent random walks:
$$\langle r_{\text{total}}^2 \rangle = \langle r_{\text{slowing}}^2 \rangle + \langle r_{\text{diffusion}}^2 \rangle = 6 \tau + 6 L^2$$
We define the <strong>Migration Area</strong> $M^2$:
$$\mathbf{M^2 \equiv L^2 + \tau = \frac{1}{6} \langle r_{\text{total}}^2 \rangle}$$
The <strong>Migration Length</strong> $M$ is the square root:
$$\mathbf{M \equiv \sqrt{M^2} = \sqrt{L^2 + \tau}}$$
</p>

<h3>2. Moderating Material Comparison</h3>
<table style="width:100%; border-collapse: collapse; margin: 16px 0; text-align: left;">
  <thead>
    <tr style="border-bottom: 2px solid #4a5568;">
      <th style="padding: 8px;">Moderator</th>
      <th style="padding: 8px;">Diffusion Length $L$ (cm)</th>
      <th style="padding: 8px;">Diffusion Area $L^2\ (\text{cm}^2)$</th>
      <th style="padding: 8px;">Fermi Age $\tau\ (\text{cm}^2)$</th>
      <th style="padding: 8px;">Migration Area $M^2\ (\text{cm}^2)$</th>
      <th style="padding: 8px;">Migration Length $M$ (cm)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Light Water ($\text{H}_2\text{O}$)</td>
      <td style="padding: 8px;">$2.85$</td>
      <td style="padding: 8px;">$8.1$</td>
      <td style="padding: 8px;">$27.0$</td>
      <td style="padding: 8px;">$35.1$</td>
      <td style="padding: 8px;">$\mathbf{5.92}$</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Heavy Water ($\text{D}_2\text{O}$)</td>
      <td style="padding: 8px;">$171$</td>
      <td style="padding: 8px;">$29{,}240$</td>
      <td style="padding: 8px;">$131$</td>
      <td style="padding: 8px;">$29{,}371$</td>
      <td style="padding: 8px;">$\mathbf{171.4}$</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Beryllium ($\text{Be}$)</td>
      <td style="padding: 8px;">$21$</td>
      <td style="padding: 8px;">$441$</td>
      <td style="padding: 8px;">$102$</td>
      <td style="padding: 8px;">$543$</td>
      <td style="padding: 8px;">$\mathbf{23.3}$</td>
    </tr>
    <tr style="border-bottom: 2px solid #4a5568;">
      <td style="padding: 8px;">Graphite ($\text{C}$)</td>
      <td style="padding: 8px;">$59$</td>
      <td style="padding: 8px;">$3481$</td>
      <td style="padding: 8px;">$368$</td>
      <td style="padding: 8px;">$3849$</td>
      <td style="padding: 8px;">$\mathbf{62.0}$</td>
    </tr>
  </tbody>
</table>
<p>
<strong>Key Physical Distinction:</strong> In Light Water, slowing down dominates migration ($M^2 \approx \tau = 27\text{ cm}^2$ vs $L^2 = 8\text{ cm}^2$). In contrast, in Heavy Water, thermal diffusion overwhelmingly dominates migration ($L^2 = 29{,}240\text{ cm}^2 \gg \tau = 131\text{ cm}^2$), because thermal neutrons wander for nearly two meters before being absorbed!
</p>
"""
        }
    ],
    "exercises": [
        {
            "id": "rp-prob-5-1",
            "title": "Point Neutron Source in an Infinite Moderating Medium and Radial Flux Profile",
            "statement": r"""An isotopic Americium-Beryllium ($\text{Am-Be}$) source emits $S = 2.5 \times 10^7\text{ neutrons/second}$ isotropically at the center of a large tank of pure light water.
For thermal neutrons in light water at room temperature:
- Diffusion coefficient $D = 0.16\text{ cm}$
- Macroscopic absorption cross section $\Sigma_a = 0.0197\text{ cm}^{-1}$
(a) Calculate the thermal diffusion length $L$ in $\text{cm}$.
(b) Calculate the thermal neutron flux $\phi(r)$ at radial distances $r = 5.0\text{ cm}$, $r = 15.0\text{ cm}$, and $r = 30.0\text{ cm}$ from the source.
(c) Calculate the net neutron current density vector $\vec{J}(r)$ and evaluate the total leakage rate of neutrons passing outward through a spherical surface of radius $r = 10.0\text{ cm}$.""",
            "solution": r"""**(a) Thermal Diffusion Length $L$:**
$$L = \sqrt{\frac{D}{\Sigma_a}} = \sqrt{\frac{0.16\text{ cm}}{0.0197\text{ cm}^{-1}}} = \sqrt{8.1218\text{ cm}^2} \approx \mathbf{2.850\text{ cm}}$$

**(b) Radial Flux Distribution:**
The Green's function for a point source in infinite diffusion theory is:
$$\phi(r) = \frac{S}{4\pi D r} e^{-r/L}$$
The prefactor is:
$$\frac{S}{4\pi D} = \frac{2.5 \times 10^7}{4\pi \times 0.16} = \frac{2.5 \times 10^7}{2.0106} \approx 1.2434 \times 10^7\text{ cm}^{-1}\cdot\text{s}^{-1}$$
- At $r = 5.0\text{ cm}$:
  $$r/L = 5.0 / 2.850 \approx 1.7544 \implies e^{-1.7544} \approx 0.17301$$
  $$\phi(5.0) = \frac{1.2434 \times 10^7}{5.0} \times 0.17301 \approx \mathbf{4.30 \times 10^5\text{ neutrons/cm}^2\cdot\text{s}}$$

- At $r = 15.0\text{ cm}$:
  $$r/L = 15.0 / 2.850 \approx 5.2632 \implies e^{-5.2632} \approx 0.0051786$$
  $$\phi(15.0) = \frac{1.2434 \times 10^7}{15.0} \times 0.0051786 \approx \mathbf{4.29 \times 10^3\text{ neutrons/cm}^2\cdot\text{s}}$$

- At $r = 30.0\text{ cm}$:
  $$r/L = 30.0 / 2.850 \approx 10.5263 \implies e^{-10.5263} \approx 2.682 \times 10^{-5}$$
  $$\phi(30.0) = \frac{1.2434 \times 10^7}{30.0} \times (2.682 \times 10^{-5}) \approx \mathbf{11.1\text{ neutrons/cm}^2\cdot\text{s}}$$

**(c) Net Leakage Through Spherical Surface of Radius $r = 10.0\text{ cm}$:**
Using Fick's Law:
$$J(r) = -D \frac{d\phi}{dr} = -D \frac{d}{dr}\left[ \frac{S}{4\pi D} \frac{e^{-r/L}}{r} \right] = \frac{S}{4\pi r^2} e^{-r/L} \left( 1 + \frac{r}{L} \right)$$
The total outward neutron current crossing the sphere of area $4\pi r^2$ is:
$$\text{Leakage}(r) = 4\pi r^2 J(r) = S e^{-r/L} \left( 1 + \frac{r}{L} \right)$$
At $r = 10.0\text{ cm}$, $r/L = 10.0 / 2.850 = 3.5088$:
$$e^{-3.5088} \approx 0.02993, \qquad 1 + \frac{r}{L} = 4.5088$$
$$\text{Leakage}(10.0) = (2.5 \times 10^7) \times 0.02993 \times 4.5088 \approx \mathbf{3.374 \times 10^6\text{ neutrons/second}}$$
Of the original $2.5 \times 10^7\text{ n/s}$ emitted, only **$13.5\%$** cross radius $10\text{ cm}$; the remaining $86.5\%$ are absorbed within the inner sphere."""
        },
        {
            "id": "rp-prob-5-2",
            "title": "Derivation of the Extrapolated Boundary Distance d = 0.7104 lambda_tr via Milne Transport",
            "statement": r"""Consider Milne's classic half-space transport problem: a semi-infinite non-absorbing medium occupies $z \ge 0$, bounded by vacuum at $z = 0$.
(a) In elementary diffusion theory, the angular flux is approximated as $\psi(z, \mu) = \frac{1}{2} \phi(z) + \frac{3}{2} \mu J(z)$.
Show that the zero incoming vacuum boundary condition:
$$J_-(0) = \int_{-1}^{0} (-\mu) \psi(0, \mu) \, 2\pi d\mu = 0$$
yields the simple linear extrapolation distance $d = \frac{2}{3} \lambda_{\text{tr}}$.
(b) Explain why the exact integral transport theory solution by Placzek and Seidel yields $d = 0.710446 \lambda_{\text{tr}}$.
(c) For reactor-grade graphite with transport cross section $\Sigma_{\text{tr}} = 0.385\text{ cm}^{-1}$, compute the numerical value of $d$ under both approximations and calculate the absolute difference.""",
            "solution": r"""**(a) Derivation of $d = \frac{2}{3}\lambda_{\text{tr}}$ in Elementary Diffusion Theory:**
The inward partial current across the surface at $z = 0$ is:
$$J_-(0) = 2\pi \int_{-1}^0 (-\mu) \left[ \frac{1}{4\pi} \phi(0) + \frac{3}{4\pi} \mu J(0) \right] d\mu$$
Evaluating the angular integrals:
$$\int_{-1}^0 (-\mu) d\mu = \left[ -\frac{\mu^2}{2} \right]_{-1}^0 = 0 - \left(-\frac{1}{2}\right) = \frac{1}{2}$$
$$\int_{-1}^0 (-\mu^2) d\mu = \left[ -\frac{\mu^3}{3} \right]_{-1}^0 = 0 - \left(-\frac{1}{3}\right) = \frac{1}{3}$$
Multiplying by $2\pi$:
$$J_-(0) = \frac{1}{4} \phi(0) + \frac{1}{2} J(0)$$
Setting $J_-(0) = 0$ at the vacuum interface:
$$\frac{1}{4} \phi(0) + \frac{1}{2} J(0) = 0 \implies \phi(0) = -2 J(0)$$
Substituting Fick's Law $J(0) = -D \left.\frac{d\phi}{dz}\right|_{z=0}$:
$$\phi(0) = 2 D \left.\frac{d\phi}{dz}\right|_{z=0}$$
The linear extrapolation distance $d$ is defined where the tangent line reaches zero: $\phi(-d) = \phi(0) - d \left.\frac{d\phi}{dz}\right|_{z=0} = 0$:
$$d = \frac{\phi(0)}{\left.\frac{d\phi}{dz}\right|_{z=0}} = 2 D$$
Since $D = \frac{1}{3} \lambda_{\text{tr}}$:
$$\mathbf{d = \frac{2}{3} \lambda_{\text{tr}} \approx 0.6667 \lambda_{\text{tr}}} \quad \text{(Q.E.D.)}$$

**(b) Origin of the Exact Transport Correction $0.7104 \lambda_{\text{tr}}$:**
In reality, within $1\text{ to }2$ mean free paths of a vacuum boundary, the angular flux becomes severely anisotropic (peaked grazing along the boundary) because no neutrons arrive from the vacuum hemisphere. The $P_1$ two-term expansion breaks down in this boundary layer (the Knudsen transport boundary layer).
Solving the exact Fredholm integral equation of transport theory via Wiener-Hopf contour integration yields the asymptotic linear profile whose zero-crossing is:
$$d = c \cdot \lambda_{\text{tr}} = \mathbf{0.710446 \lambda_{\text{tr}}}$$
This exact factor represents a $+6.57\%$ correction over the crude $P_1$ approximation.

**(c) Numerical Calculation for Graphite:**
Given $\Sigma_{\text{tr}} = 0.385\text{ cm}^{-1}$:
$$\lambda_{\text{tr}} = \frac{1}{\Sigma_{\text{tr}}} = \frac{1}{0.385\text{ cm}^{-1}} \approx 2.5974\text{ cm}$$
- Under $P_1$ approximation:
  $$d_{P_1} = \frac{2}{3} \times 2.5974\text{ cm} \approx \mathbf{1.7316\text{ cm}}$$
- Under exact Milne transport theory:
  $$d_{\text{exact}} = 0.710446 \times 2.5974\text{ cm} \approx \mathbf{1.8453\text{ cm}}$$
Difference:
$$\Delta d = 1.8453 - 1.7316 = \mathbf{0.1137\text{ cm}} \approx \mathbf{1.14\text{ mm}}$$
In precision reactor criticality calculations, this millimetric difference in extrapolated boundary shifts the calculated eigenvalue $k_{\text{eff}}$ by tens of pcm!"""
        },
        {
            "id": "rp-prob-5-3",
            "title": "Fermi Age, Diffusion Length, and Migration Area Calculations for Beryllium",
            "statement": r"""A nuclear reactor uses high-density Beryllium metal ($\text{Be}$, $A = 9.012$) as both moderator and reflector.
The nuclear parameters at room temperature are:
- Density $\rho = 1.85\text{ g/cm}^3$
- Microscopic scattering cross section $\sigma_s = 6.1\text{ b}$
- Microscopic absorption cross section $\sigma_a = 0.0092\text{ b}$
- Slowing down length for fission neutrons $L_s = 10.1\text{ cm}$
(a) Calculate the transport cross section $\Sigma_{\text{tr}}$ and diffusion coefficient $D$ in $\text{cm}$.
(b) Calculate the thermal diffusion area $L^2$ and diffusion length $L$ in $\text{cm}$.
(c) Determine the Fermi age $\tau$ from fission to thermal energy.
(d) Calculate the migration area $M^2$ and migration length $M$ of Beryllium.""",
            "solution": r"""**(a) Atom Density, Transport Cross Section, and Diffusion Coefficient:**
Atom density of Beryllium:
$$N = \frac{\rho N_A}{M} = \frac{(1.85\text{ g/cm}^3)(6.02214 \times 10^{23}\text{ atoms/mol})}{9.0122\text{ g/mol}} \approx 1.236 \times 10^{23}\text{ atoms/cm}^3 = 0.1236\text{ b}^{-1}\text{cm}^{-1}$$
Macroscopic scattering cross section:
$$\Sigma_s = N \sigma_s = (0.1236\text{ b}^{-1}\text{cm}^{-1})(6.1\text{ b}) \approx 0.7540\text{ cm}^{-1}$$
Average cosine of scattering angle:
$$\bar{\mu}_0 = \frac{2}{3 A} = \frac{2}{3 \times 9.012} = \frac{2}{27.036} \approx 0.07398$$
Transport cross section:
$$\Sigma_{\text{tr}} = \Sigma_s (1 - \bar{\mu}_0) = 0.7540 \times (1 - 0.07398) = 0.7540 \times 0.92602 \approx \mathbf{0.6982\text{ cm}^{-1}}$$
Diffusion coefficient $D$:
$$D = \frac{1}{3 \Sigma_{\text{tr}}} = \frac{1}{3 \times 0.6982\text{ cm}^{-1}} \approx \mathbf{0.4774\text{ cm}}$$

**(b) Thermal Diffusion Area $L^2$ and Length $L$:**
Macroscopic absorption cross section:
$$\Sigma_a = N \sigma_a = (0.1236\text{ b}^{-1}\text{cm}^{-1})(0.0092\text{ b}) \approx 1.1371 \times 10^{-3}\text{ cm}^{-1}$$
Diffusion area $L^2$:
$$L^2 = \frac{D}{\Sigma_a} = \frac{0.4774\text{ cm}}{1.1371 \times 10^{-3}\text{ cm}^{-1}} \approx \mathbf{419.8\text{ cm}^2}$$
Diffusion length $L$:
$$L = \sqrt{419.8\text{ cm}^2} \approx \mathbf{20.49\text{ cm}}$$

**(c) Fermi Age $\tau$:**
By definition, Fermi age to thermal is related to the slowing down length by $\tau = L_s^2$:
$$\tau = (10.1\text{ cm})^2 = \mathbf{102.01\text{ cm}^2}$$

**(d) Migration Area $M^2$ and Migration Length $M$:**
$$M^2 = L^2 + \tau = 419.8\text{ cm}^2 + 102.01\text{ cm}^2 = \mathbf{521.8\text{ cm}^2}$$
Migration length:
$$M = \sqrt{M^2} = \sqrt{521.8\text{ cm}^2} \approx \mathbf{22.84\text{ cm}}$$
In Beryllium, thermal diffusion accounts for **$80.4\%$** of the migration area ($L^2 / M^2 = 419.8 / 521.8$), while fast slowing down accounts for the remaining **$19.6\%$**."""
        }
    ]
}

u6_data = {
    "title": "Neutron Chain Reactions, Multiplication & The Four/Six-Factor Formulas",
    "subtitle": "Critical Multiplications, Neutron Life Cycle, Four-Factor & Six-Factor Reactor Formalisms",
    "summary": "Exhaustive treatment of self-sustaining nuclear fission chain reactions and critical multiplication physics: subcritical, critical, and supercritical operating regimes; infinite medium neutron life cycle and detailed derivation of the classical Four-Factor Formula k_infinity = epsilon * p * eta * f; the fast fission factor epsilon in uranium lattices; resonance escape probability p and Doppler resonance temperature dependence; thermal utilization factor f and competitive absorption balance; reproduction factor eta and the fissile figure of merit; finite core geometry leakage mechanics, fast non-leakage probability P_FNL, thermal non-leakage probability P_TNL, and the complete Six-Factor Formula k_eff = k_infinity * P_FNL * P_TNL; and homogeneous vs heterogeneous lattice design principles.",
    "sections": [
        {
            "id": "sec-6-1",
            "title": "The Self-Sustaining Nuclear Fission Chain Reaction: Critical States & Multiplications",
            "content": r"""
<h3>1. The Multiplication Factor $k$</h3>
<p>
The central parameter governing any nuclear multiplying assembly is the <strong>effective multiplication factor</strong> $k_{\text{eff}}$ (or simply $k$), defined as the ratio of neutrons produced by fission in generation $n+1$ to the total neutrons lost by absorption and leakage in generation $n$:
$$\mathbf{k_{\text{eff}} \equiv \frac{\text{Neutrons produced in generation } n+1}{\text{Neutrons lost (absorption + leakage) in generation } n} = \frac{\text{Production Rate}}{\text{Loss Rate}}}$$
Three distinct physical regimes exist:
<ul>
  <li><strong>Subcritical ($k_{\text{eff}} < 1$):</strong> Loss rate exceeds production rate. A chain reaction cannot sustain itself; neutron population decays exponentially to zero (or to a steady subcritical multiplier equilibrium supported by an external source).</li>
  <li><strong>Critical ($k_{\text{eff}} = 1.00000$):</strong> Production rate perfectly balances total losses. The neutron population and thermal power remain strictly constant in time. This is the normal operating state of all commercial nuclear power reactors.</li>
  <li><strong>Supercritical ($k_{\text{eff}} > 1$):</strong> Production exceeds losses. The neutron population grows exponentially in time.</li>
</ul>
</p>

<h3>2. Static Reactivity $\rho$</h3>
<p>
The fractional departure of a reactor from the exact critical state is the <strong>reactivity</strong> $\rho$:
$$\mathbf{\rho \equiv \frac{k_{\text{eff}} - 1}{k_{\text{eff}}} = \frac{\Delta k}{k}}$$
Units of reactivity:
<ul>
  <li>Dimensionless decimal ($\Delta k/k$).</li>
  <li><strong>Percent ($\% \Delta k/k$):</strong> $1\% = 10^{-2}$.</li>
  <li><strong>Percent Mille ($\text{pcm}$):</strong> $1\text{ pcm} = 10^{-5} = 0.001\%$. A change of $100\text{ pcm}$ is $0.1\% \Delta k/k$.</li>
  <li><strong>Dollars ($\$$) and Cents ($\cancel{\text{c}}$):</strong> Normalized by the effective delayed neutron fraction $\beta$:
  $$\rho\ [\$] \equiv \frac{\rho}{\beta_{\text{eff}}}, \qquad 1\$ = 100\cancel{\text{c}}$$</li>
</ul>
</p>
"""
        },
        {
            "id": "sec-6-2",
            "title": "Infinite Medium Neutron Life Cycle & The Four-Factor Formula",
            "content": r"""
<h3>1. Tracking 1000 Neutrons Through One Generation</h3>
<p>
In an infinite multiplying medium (where leakage is zero by definition), every neutron lost is lost by absorption. Enrico Fermi and his team formulated the classic <strong>Four-Factor Formula</strong> to track the life cycle of neutrons from birth to the next generation:
$$\mathbf{k_\infty = \epsilon \, p \, \eta \, f}$$
Let $N_0$ thermal neutrons be absorbed in fuel nuclei in generation $n$:
<ol>
  <li><strong>Thermal Fission and Fast Birth:</strong> Absorbing $N_0$ neutrons in fuel produces $\eta N_0$ fast fission neutrons ($E \sim 2\text{ MeV}$).</li>
  <li><strong>Fast Fission Boost ($\epsilon$):</strong> Before slowing down, some fast neutrons induce fast fission in fertile ${}^{238}\text{U}$, boosting the population by factor $\epsilon \ge 1$ to $\epsilon \eta N_0$ fast neutrons.</li>
  <li><strong>Resonance Slowing Down ($p$):</strong> As these neutrons slow down through the epithermal resonance region, a fraction $1 - p$ are captured in ${}^{238}\text{U}$ resonances. The surviving population reaching thermal energy is $p \, \epsilon \eta N_0$.</li>
  <li><strong>Thermal Absorption Competition ($f$):</strong> At thermal energy, neutrons are absorbed either in fuel or in non-fuel materials (moderator, clad, coolant, poisons). The fraction absorbed in fuel is $f$, yielding $f \, p \epsilon \eta N_0$ thermal neutrons absorbed in fuel in generation $n+1$.</li>
</ol>
Taking the ratio of absorbed fuel neutrons between generations:
$$k_\infty = \frac{N_{n+1}}{N_n} = \frac{\epsilon \, p \, \eta \, f \, N_0}{N_0} = \mathbf{\epsilon \, p \, \eta \, f}$$
</p>
"""
        },
        {
            "id": "sec-6-3",
            "title": "Fast Fission Factor Epsilon: Fission in Uranium-238",
            "content": r"""
<h3>1. Fast Fission in Fertile Material</h3>
<p>
Although ${}^{238}\text{U}$ cannot fission from thermal neutrons, it possesses a significant fission cross section ($\sigma_f \approx 0.55\text{ b}$) for fast neutrons with energies above $E_{\text{th}} \approx 1.0\text{ MeV}$.
Since approximately $69\%$ of prompt fission neutrons are born above $1.0\text{ MeV}$, some collide with ${}^{238}\text{U}$ before escaping the fuel rod, producing additional second-generation fast neutrons.
The <strong>fast fission factor</strong> $\epsilon$ is defined as:
$$\mathbf{\epsilon \equiv \frac{\text{Total fast neutrons born from all fission (thermal + fast)}}{\text{Fast neutrons born from thermal fission alone}}}$$
</p>

<h3>2. Quantitative Lattice Values</h3>
<p>
In a homogeneous mixture of natural uranium and graphite, $\epsilon \approx 1.000$ because fast neutrons immediately collide with carbon atoms and drop below $1\text{ MeV}$.
In a heterogeneous reactor lattice with tightly packed fuel rods (such as a PWR assembly):
$$\epsilon \approx 1.03\text{ to }1.08$$
This represents a crucial $3\%\text{ to }8\%$ boost to the core neutron population obtained completely free from fertile ${}^{238}\text{U}$!
</p>
"""
        },
        {
            "id": "sec-6-4",
            "title": "Resonance Escape Probability p: Resonance Capture & Doppler Broadening",
            "content": r"""
<h3>1. Epithermal Capture in Uranium-238</h3>
<p>
As neutrons slow through the energy interval between $10\text{ keV}$ and $1\text{ eV}$, they encounter colossal capture resonances in ${}^{238}\text{U}$, such as the famous resonance at $E_0 = 6.67\text{ eV}$ where peak cross section exceeds $\sigma_\gamma > 20{,}000\text{ barns}$!
The <strong>resonance escape probability</strong> $p$ is the fraction of fast neutrons that successfully escape resonance capture during moderation:
$$\mathbf{p = \exp\left( - \frac{N_F}{\overline{\xi \Sigma_s}} I_{\text{eff}} \right)}$$
Typical values in thermal power reactors range from $p \approx 0.75\text{ to }0.90$.
</p>

<h3>2. Doppler Broadening and Inherent Safety</h3>
<p>
Thermal agitation of fuel atoms causes relative velocity motion between target nuclei and incoming neutrons. By Breit-Wigner theory, as fuel temperature increases:
<ul>
  <li>The resonance peak height decreases.</li>
  <li>The resonance width $\Gamma$ broadens (Doppler broadening).</li>
  <li>Because resonances are self-shielded, broadening allows more neutrons to be absorbed in the resonance wings!</li>
</ul>
Consequently, an increase in fuel temperature <strong>decreases</strong> $p$:
$$\frac{dp}{dT_{\text{fuel}}} < 0 \implies \alpha_D \equiv \frac{1}{k} \frac{dk}{dT_{\text{fuel}}} < 0$$
This negative <strong>Fuel Doppler Temperature Coefficient</strong> is the foundational passive safety mechanism of all commercial nuclear power reactors, guaranteeing that an accidental power excursion terminates itself within milliseconds without human or mechanical intervention!
</p>
"""
        },
        {
            "id": "sec-6-5",
            "title": "Thermal Utilization Factor f: Fuel vs Parasitic Absorption Balance",
            "content": r"""
<h3>1. Definition of Thermal Utilization $f$</h3>
<p>
Once neutrons reach thermal equilibrium, they diffuse through the lattice until absorbed. The <strong>thermal utilization factor</strong> $f$ is the fraction of thermal neutrons absorbed in the nuclear fuel ($F$) relative to total absorption in all core materials:
$$\mathbf{f \equiv \frac{\text{Thermal neutrons absorbed in fuel}}{\text{Total thermal neutrons absorbed in all core materials}} = \frac{\Sigma_a^F \phi_F V_F}{\Sigma_a^F \phi_F V_F + \Sigma_a^M \phi_M V_M + \Sigma_a^{\text{struct}} \phi_{\text{st}} V_{\text{st}}}}$$
where $F = \text{fuel}$, $M = \text{moderator}$, and $\text{struct} = \text{cladding, coolant, and structural poisons}$.
</p>

<h3>2. Homogeneous vs Heterogeneous Expressions</h3>
<p>
For an intimate homogeneous mixture where flux is spatially uniform ($\phi_F = \phi_M$):
$$\mathbf{f = \frac{\Sigma_a^F}{\Sigma_a^F + \Sigma_a^M + \Sigma_a^{\text{other}}} = \frac{N_F \sigma_a^F}{N_F \sigma_a^F + N_M \sigma_a^M}}$$
Typical values: $f \approx 0.85\text{ to }0.95$ in enriched reactors.
There is a fundamental design trade-off between $p$ and $f$:
<ul>
  <li>Adding more moderator increases $p$ (more moderation means faster crossing of resonances), but decreases $f$ (more moderator absorbs more thermal neutrons parasitically).</li>
  <li>Plotting $k_\infty = \epsilon p \eta f$ versus moderator-to-fuel ratio $(V_M / V_F)$ reveals a distinct maximum—the <strong>optimum moderation pitch</strong>.</li>
</ul>
</p>
"""
        },
        {
            "id": "sec-6-6",
            "title": "Thermal Reproduction Factor Eta: Fission Neutrons Per Fuel Absorption",
            "content": r"""
<h3>1. Microscopic Definition of $\eta$</h3>
<p>
The <strong>thermal neutron reproduction factor</strong> $\eta$ is the average number of fast fission neutrons emitted per thermal neutron absorbed in the fuel material:
$$\mathbf{\eta \equiv \nu \, \frac{\Sigma_f^F}{\Sigma_a^F} = \nu \, \frac{\sigma_f^F}{\sigma_a^F} = \nu \, \frac{\sigma_f^F}{\sigma_f^F + \sigma_c^F} = \frac{\nu}{1 + \alpha}}$$
where $\nu$ is the average number of neutrons emitted per fission, $\sigma_c$ is radiative capture $(n, \gamma)$ without fission, and $\alpha \equiv \sigma_c / \sigma_f$ is the capture-to-fission ratio.
</p>

<h3>2. Pure Fissile Isotopes at 2200 m/s</h3>
<table style="width:100%; border-collapse: collapse; margin: 16px 0; text-align: left;">
  <thead>
    <tr style="border-bottom: 2px solid #4a5568;">
      <th style="padding: 8px;">Fissile Isotope</th>
      <th style="padding: 8px;">$\nu$</th>
      <th style="padding: 8px;">$\sigma_f\ (\text{b})$</th>
      <th style="padding: 8px;">$\sigma_c\ (\text{b})$</th>
      <th style="padding: 8px;">$\alpha = \sigma_c/\sigma_f$</th>
      <th style="padding: 8px;">$\eta = \nu / (1+\alpha)$</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Uranium-233 (${}^{233}\text{U}$)</td>
      <td style="padding: 8px;">$2.49$</td>
      <td style="padding: 8px;">$531$</td>
      <td style="padding: 8px;">$45.5$</td>
      <td style="padding: 8px;">$0.086$</td>
      <td style="padding: 8px;">$\mathbf{2.29}$ (Highest thermal $\eta$)</td>
    </tr>
    <tr style="border-bottom: 1px solid #2d3748;">
      <td style="padding: 8px;">Uranium-235 (${}^{235}\text{U}$)</td>
      <td style="padding: 8px;">$2.43$</td>
      <td style="padding: 8px;">$585$</td>
      <td style="padding: 8px;">$99$</td>
      <td style="padding: 8px;">$0.169$</td>
      <td style="padding: 8px;">$\mathbf{2.08}$</td>
    </tr>
    <tr style="border-bottom: 2px solid #4a5568;">
      <td style="padding: 8px;">Plutonium-239 (${}^{239}\text{Pu}$)</td>
      <td style="padding: 8px;">$2.88$</td>
      <td style="padding: 8px;">$748$</td>
      <td style="padding: 8px;">$269$</td>
      <td style="padding: 8px;">$0.360$</td>
      <td style="padding: 8px;">$\mathbf{2.12}$</td>
    </tr>
  </tbody>
</table>

<h3>3. $\eta$ in Enriched and Natural Uranium Fuel</h3>
<p>
For a fuel mixture containing both fissile ${}^{235}\text{U}$ ($5$) and fertile ${}^{238}\text{U}$ ($8$):
$$\mathbf{\eta = \frac{\nu_5 \, N_5 \, \sigma_{f, 5}}{N_5 \sigma_{a, 5} + N_8 \sigma_{a, 8}} = \nu_5 \frac{\sigma_{f, 5}}{\sigma_{a, 5} + \frac{N_8}{N_5} \sigma_{a, 8}}}$$
For natural uranium ($N_8/N_5 = 99.28 / 0.72 \approx 138$):
$$\sigma_{a, 8} \approx 2.7\text{ b} \implies 138 \times 2.7 = 372.6\text{ b}$$
$$\sigma_{a, 5} = 684\text{ b}, \quad \sigma_{f, 5} = 585\text{ b}, \quad \nu_5 = 2.43$$
$$\eta_{\text{NatU}} = 2.43 \times \frac{585}{684 + 372.6} = 2.43 \times \frac{585}{1056.6} \approx \mathbf{1.345}$$
Because $\eta_{\text{NatU}} = 1.345$ is so close to $1.0$, a natural uranium reactor has a tiny margin for neutron losses: the product $\epsilon p f$ must exceed $1 / 1.345 = 0.743$, which is impossible in light water!
</p>
"""
        },
        {
            "id": "sec-6-7",
            "title": "Finite Reactor Non-Leakage Probabilities & The Six-Factor Formula",
            "content": r"""
<h3>1. Fast and Thermal Neutron Leakage</h3>
<p>
In a finite real reactor core, neutrons escape across the boundary into the surroundings. We define two non-leakage probabilities:
<ul>
  <li><strong>Fast Non-Leakage Probability ($P_{\text{FNL}}$):</strong> The probability that a fast fission neutron slows down to thermal energy without leaking from the core during moderation:
  $$\mathbf{P_{\text{FNL}} = \exp\left( - B_g^2 \tau \right) \approx \frac{1}{1 + B_g^2 \tau}}$$
  where $B_g^2$ is the geometric buckling of the core and $\tau$ is Fermi age.</li>
  <li><strong>Thermal Non-Leakage Probability ($P_{\text{TNL}}$):</strong> The probability that a thermal neutron does not leak out while diffusing, but is absorbed inside the core:
  $$\mathbf{P_{\text{TNL}} = \frac{1}{1 + B_g^2 L^2}}$$
  where $L^2$ is the thermal diffusion area.</li>
</ul>
</p>

<h3>2. The Six-Factor Formula</h3>
<p>
Combining the infinite multiplication factor with both non-leakage probabilities yields the complete <strong>Six-Factor Formula</strong> for effective multiplication:
$$\mathbf{k_{\text{eff}} = k_\infty \, P_{\text{FNL}} \, P_{\text{TNL}} = \left( \epsilon \, p \, \eta \, f \right) \cdot P_{\text{FNL}} \cdot P_{\text{TNL}}}$$
In the modified one-group diffusion approximation, since $B_g^2 \tau \ll 1$ and $B_g^2 L^2 \ll 1$:
$$P_{\text{FNL}} P_{\text{TNL}} \approx \frac{1}{1 + B_g^2 (L^2 + \tau)} = \mathbf{\frac{1}{1 + M^2 B_g^2}}$$
Thus:
$$\mathbf{k_{\text{eff}} = \frac{k_\infty}{1 + M^2 B_g^2}}$$
where $M^2 \equiv L^2 + \tau$ is the migration area!
</p>
"""
        }
    ],
    "exercises": [
        {
            "id": "rp-prob-6-1",
            "title": "Detailed Four-Factor Formula Evaluation for Natural Uranium / Heavy Water",
            "statement": r"""A homogeneous thermal reactor system consists of natural uranium metal dissolved in pure heavy water ($\text{D}_2\text{O}$) with an atomic ratio $N_D / N_U = 120$.
Thermal microscopic parameters:
- For $^{235}\text{U}$: $\sigma_a = 680\text{ b}, \sigma_f = 582\text{ b}, \nu = 2.43$
- For $^{238}\text{U}$: $\sigma_a = 2.71\text{ b}, \sigma_f = 0\text{ b}$
- For Deuterium (${}^2\text{H}$): $\sigma_a = 0.00053\text{ b}, \sigma_s = 3.4\text{ b}, \xi = 0.725$
- For Oxygen (${}^{16}\text{O}$): $\sigma_a = 0.00020\text{ b}, \sigma_s = 3.8\text{ b}$
Natural uranium contains $0.720\%\ {}^{235}\text{U}$ and $99.280\%\ {}^{238}\text{U}$.
Fast fission factor $\epsilon = 1.005$.
The effective resonance integral for this mixture is $I_{\text{eff}} = 24.5\text{ b}$.
(a) Calculate the reproduction factor $\eta$ for natural uranium.
(b) Calculate the thermal utilization factor $f$.
(c) Calculate the resonance escape probability $p$.
(d) Compute the infinite multiplication factor $k_\infty = \epsilon \, p \, \eta \, f$ and determine whether an infinite critical reactor is possible.""",
            "solution": r"""**(a) Reproduction Factor $\eta$:**
For natural uranium:
$$\frac{N_5}{N_U} = 0.00720, \qquad \frac{N_8}{N_U} = 0.99280$$
$$\bar{\sigma}_{f, U} = 0.00720 \times 582\text{ b} = 4.1904\text{ b}$$
$$\bar{\sigma}_{a, U} = 0.00720 \times 680\text{ b} + 0.99280 \times 2.71\text{ b} = 4.896 + 2.6905 = 7.5865\text{ b}$$
$$\eta = \nu \frac{\bar{\sigma}_{f, U}}{\bar{\sigma}_{a, U}} = 2.43 \times \frac{4.1904\text{ b}}{7.5865\text{ b}} \approx \mathbf{1.3421}$$

**(b) Thermal Utilization Factor $f$:**
Thermal absorption in heavy water per uranium atom ($N_D/N_U = 120$, $N_O/N_U = 60$):
$$\frac{\Sigma_a^M}{N_U} = 120 \times \sigma_{a, D} + 60 \times \sigma_{a, O} = 120(0.00053) + 60(0.00020) = 0.0636 + 0.0120 = 0.0756\text{ b}$$
Thermal absorption in fuel:
$$\frac{\Sigma_a^F}{N_U} = \bar{\sigma}_{a, U} = 7.5865\text{ b}$$
Thermal utilization:
$$f = \frac{\Sigma_a^F}{\Sigma_a^F + \Sigma_a^M} = \frac{7.5865}{7.5865 + 0.0756} = \frac{7.5865}{7.6621} \approx \mathbf{0.9901}$$

**(c) Resonance Escape Probability $p$:**
Slowing down power per uranium atom:
$$\frac{\Sigma_s}{N_U} = 120 \times 3.4\text{ b} + 60 \times 3.8\text{ b} + 1 \times 8.3\text{ b} = 408 + 228 + 8.3 = 644.3\text{ b}$$
Effective decrement:
$$\bar{\xi} \approx \frac{120(3.4)(0.725) + 60(3.8)(0.120)}{644.3} = \frac{295.8 + 27.36}{644.3} \approx 0.5015$$
$$\frac{\xi \Sigma_s}{N_U} = 0.5015 \times 644.3 \approx 323.1\text{ b}$$
Resonance escape probability:
$$p = \exp\left( - \frac{I_{\text{eff}}}{\frac{\xi \Sigma_s}{N_U}} \right) = \exp\left( - \frac{24.5\text{ b}}{323.1\text{ b}} \right) = \exp(-0.07583) \approx \mathbf{0.9270}$$

**(d) Infinite Multiplication Factor $k_\infty$:**
$$k_\infty = \epsilon \cdot p \cdot \eta \cdot f = 1.005 \times 0.9270 \times 1.3421 \times 0.9901$$
$$k_\infty = 1.005 \times 0.9270 \times 1.3288 \approx \mathbf{1.238}$$
Because **$k_\infty = 1.238 > 1$**, this natural uranium / heavy water system is robustly supercritical with $+23.8\%$ excess multiplication, easily overcoming finite reactor leakage!"""
        },
        {
            "id": "rp-prob-6-2",
            "title": "Heterogeneous Lattice Advantage: Resonance Self-Shielding & Spatial Flux Depression",
            "statement": r"""A reactor designer replaces a homogeneous natural uranium / graphite mixture with a square heterogeneous lattice of solid uranium fuel rods ($d = 2.5\text{ cm}$) surrounded by graphite blocks.
In the homogeneous mixture: $p_{\text{hom}} = 0.690$, $f_{\text{hom}} = 0.920$, $\epsilon_{\text{hom}} = 1.000$, $\eta = 1.340$.
In the heterogeneous lattice:
- Resonance self-shielding increases resonance escape to $p_{\text{het}} = 0.885$.
- Fast fission inside the dense fuel rod increases $\epsilon_{\text{het}} = 1.035$.
- Spatial flux depression (thermal flux inside rod is lower than moderator, $\phi_F / \phi_M = 0.82$) reduces thermal utilization to $f_{\text{het}} = 0.875$.
(a) Calculate $k_{\infty, \text{hom}}$ for the homogeneous mixture and show that it cannot achieve criticality.
(b) Calculate $k_{\infty, \text{het}}$ for the heterogeneous lattice.
(c) Calculate the net reactivity gain $\Delta \rho = \frac{k_{\text{het}} - k_{\text{hom}}}{k_{\text{het}}}$ in pcm.""",
            "solution": r"""**(a) Homogeneous Multiplication Factor $k_{\infty, \text{hom}}$:**
$$k_{\infty, \text{hom}} = \epsilon \cdot p \cdot \eta \cdot f = 1.000 \times 0.690 \times 1.340 \times 0.920 \approx \mathbf{0.8506}$$
Because $k_{\infty} = 0.8506 \ll 1$, an infinite homogeneous mixture of natural uranium and graphite **cannot become critical under any circumstances**.

**(b) Heterogeneous Multiplication Factor $k_{\infty, \text{het}}$:**
$$k_{\infty, \text{het}} = \epsilon \cdot p \cdot \eta \cdot f = 1.035 \times 0.885 \times 1.340 \times 0.875$$
Calculating step by step:
$$\epsilon \times p = 1.035 \times 0.885 = 0.915975$$
$$\eta \times f = 1.340 \times 0.875 = 1.1725$$
$$k_{\infty, \text{het}} = 0.915975 \times 1.1725 \approx \mathbf{1.0740}$$
By lumping the fuel into discrete rods, $k_\infty$ jumps from $0.851$ to **$1.074$**, allowing a critical graphite-moderated reactor (such as Enrico Fermi's historic Chicago Pile-1)!

**(c) Net Reactivity Gain:**
$$\Delta \rho = \frac{k_{\text{het}} - k_{\text{hom}}}{k_{\text{het}}} = \frac{1.0740 - 0.8506}{1.0740} = \frac{0.2234}{1.0740} \approx 0.2080$$
In pcm ($1\text{ pcm} = 10^{-5}$):
$$\Delta \rho = 0.2080 \times 10^5 = \mathbf{+20{,}800\text{ pcm}} = \mathbf{+20.8\%\ \Delta k/k}$$
Lumping the fuel into a heterogeneous lattice yields a colossal $+20{,}800\text{ pcm}$ reactivity improvement, turning an impossible reactor into a functioning power plant!"""
        },
        {
            "id": "rp-prob-6-3",
            "title": "Six-Factor Critical Multiplication Factor and Thermal Leakage in a Bare Reactor",
            "statement": r"""A bare cubical research reactor has side length $\tilde{a} = 280\text{ cm}$ (including extrapolation distance).
The core material parameters are:
- $k_\infty = 1.0720$
- Thermal diffusion area $L^2 = 145\text{ cm}^2$
- Fermi age $\tau = 45\text{ cm}^2$
(a) Calculate the geometric buckling $B_g^2$ of the cubical core in $\text{cm}^{-2}$.
(b) Calculate the fast non-leakage probability $P_{\text{FNL}}$ and thermal non-leakage probability $P_{\text{TNL}}$.
(c) Determine the effective multiplication factor $k_{\text{eff}}$ and calculate the net reactivity $\rho$ in pcm.
(d) What side length $\tilde{a}_{\text{crit}}$ would make the reactor precisely critical ($k_{\text{eff}} = 1.0000$)? """,
            "solution": r"""**(a) Geometric Buckling of Cubical Core:**
For a cube of dimension $\tilde{a}$:
$$B_g^2 = 3 \left( \frac{\pi}{\tilde{a}} \right)^2 = 3 \left( \frac{3.14159265}{280\text{ cm}} \right)^2 = 3 \times (0.011220)^2 \approx \mathbf{3.7766 \times 10^{-4}\text{ cm}^{-2}}$$

**(b) Non-Leakage Probabilities:**
- Fast Non-Leakage Probability $P_{\text{FNL}}$:
  $$P_{\text{FNL}} = \frac{1}{1 + B_g^2 \tau} = \frac{1}{1 + (3.7766 \times 10^{-4} \times 45)} = \frac{1}{1 + 0.016995} \approx \mathbf{0.98329}$$
  Fast neutron leakage fraction is $1 - 0.98329 = 1.67\%$.
- Thermal Non-Leakage Probability $P_{\text{TNL}}$:
  $$P_{\text{TNL}} = \frac{1}{1 + B_g^2 L^2} = \frac{1}{1 + (3.7766 \times 10^{-4} \times 145)} = \frac{1}{1 + 0.05476} \approx \mathbf{0.94808}$$
  Thermal neutron leakage fraction is $1 - 0.94808 = 5.19\%$.

**(c) Effective Multiplication Factor $k_{\text{eff}}$ and Reactivity:**
$$k_{\text{eff}} = k_\infty \cdot P_{\text{FNL}} \cdot P_{\text{TNL}} = 1.0720 \times 0.98329 \times 0.94808 \approx \mathbf{0.99938}$$
Reactivity:
$$\rho = \frac{k_{\text{eff}} - 1}{k_{\text{eff}}} = \frac{0.99938 - 1.00000}{0.99938} = \frac{-0.00062}{0.99938} \approx -6.20 \times 10^{-4} = \mathbf{-62\text{ pcm}}$$
The reactor is slightly subcritical with a reactivity deficit of **$-62\text{ pcm}$**.

**(d) Critical Dimensions $\tilde{a}_{\text{crit}}$:**
At criticality, $k_{\text{eff}} = 1.0000 \implies k_\infty = 1 + M^2 B_{g, \text{crit}}^2$:
Migration area:
$$M^2 = L^2 + \tau = 145 + 45 = 190\text{ cm}^2$$
$$B_{g, \text{crit}}^2 = \frac{k_\infty - 1}{M^2} = \frac{1.0720 - 1}{190\text{ cm}^2} = \frac{0.0720}{190} \approx 3.7895 \times 10^{-4}\text{ cm}^{-2}$$
For a cube:
$$3 \left( \frac{\pi}{\tilde{a}_{\text{crit}}} \right)^2 = B_{g, \text{crit}}^2 \implies \frac{\pi}{\tilde{a}_{\text{crit}}} = \sqrt{\frac{3.7895 \times 10^{-4}}{3}} = \sqrt{1.2632 \times 10^{-4}} \approx 0.011239\text{ cm}^{-1}$$
$$\tilde{a}_{\text{crit}} = \frac{\pi}{0.011239} \approx \mathbf{279.5\text{ cm}}$$
Decreasing the side by just $0.5\text{ cm}$ (or tightening the core) restores exact criticality!"""
        }
    ]
}

with open("rp_u5.json", "w", encoding="utf-8") as f:
    json.dump(u5_data, f, indent=2, ensure_ascii=False)

with open("rp_u6.json", "w", encoding="utf-8") as f:
    json.dump(u6_data, f, indent=2, ensure_ascii=False)

print("rp_u5.json and rp_u6.json successfully written!")
