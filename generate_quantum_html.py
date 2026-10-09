"""
generate_quantum_html.py
Generates quantum-chemistry-thermodynamics.html with pre-rendered Unit 1.
Ensures zero prohibited tokens, 60 FPS Canvas simulation slot, and full SEO metadata.
"""

import re
import assemble_quantum_data

def format_markdown(text):
    if not text:
        return ""
    # Convert KaTeX display and inline math safely
    # Headers
    lines = text.split("\n")
    html_lines = []
    in_list = False
    list_type = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_list:
                html_lines.append(f"</{list_type}>")
                in_list = False
                list_type = None
            html_lines.append("")
            continue

        if stripped.startswith("### "):
            if in_list:
                html_lines.append(f"</{list_type}>")
                in_list = False
            html_lines.append(f'<h4 class="content-heading">{stripped[4:]}</h4>')
        elif stripped.startswith("#### "):
            if in_list:
                html_lines.append(f"</{list_type}>")
                in_list = False
            html_lines.append(f'<h5 class="content-subheading">{stripped[5:]}</h5>')
        elif stripped.startswith("##### "):
            if in_list:
                html_lines.append(f"</{list_type}>")
                in_list = False
            html_lines.append(f'<h6 class="content-subheading" style="font-size:0.95rem; font-weight:600; color:#38bdf8;">{stripped[6:]}</h6>')
        elif stripped.startswith("## "):
            if in_list:
                html_lines.append(f"</{list_type}>")
                in_list = False
            html_lines.append(f'<h3 class="sec-subtitle" style="font-size:1.15rem; font-weight:700; color:#e2e8f0; margin-top:1.5rem; margin-bottom:0.75rem;">{stripped[3:]}</h3>')
        elif stripped.startswith("- "):
            if not in_list:
                html_lines.append('<ul class="content-unordered-list">')
                in_list = True
                list_type = "ul"
            html_lines.append(f"<li>{stripped[2:]}</li>")
        elif stripped.startswith("1. ") or stripped.startswith("2. ") or stripped.startswith("3. ") or stripped.startswith("4. ") or stripped.startswith("5. "):
            if not in_list:
                html_lines.append('<ol class="content-ordered-list">')
                in_list = True
                list_type = "ol"
            item_text = stripped[3:]
            html_lines.append(f"<li>{item_text}</li>")
        elif stripped == "---":
            if in_list:
                html_lines.append(f"</{list_type}>")
                in_list = False
            html_lines.append('<hr style="border: 0; border-top: 1px solid #334155; margin: 1.5rem 0;">')
        else:
            if in_list:
                html_lines.append(f"</{list_type}>")
                in_list = False
                list_type = None
            # Check for bold
            formatted_line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', stripped)
            formatted_line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', formatted_line)
            html_lines.append(f"<p>{formatted_line}</p>")

    if in_list:
        html_lines.append(f"</{list_type}>")

    return "\n".join(html_lines)

def build_html():
    course_data = assemble_quantum_data.assemble_course_data()
    unit1 = course_data["units"][0]

    # Pre-render Unit 1 Sections
    sections_html = []
    for s_idx, sec in enumerate(unit1["sections"]):
        sec_num = sec["secNumber"]
        sec_title = sec["title"]
        sec_content_html = format_markdown(sec["content"])

        inline_sim_html = ""
        if s_idx == 0:
            # Mount Unit 1 simulation in section 1.1
            sim_id = "sim_qc_blackbody_compton_wavepacket"
            inline_sim_html = f"""
            <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
              <div class="simulation-slot" id="sim-container-{sim_id}">
                <div style="background:#070d1e; border:1px solid #1e293b; border-radius:8px; padding:12px; margin:16px 0;">
                  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
                    <div>
                      <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Planck Blackbody Radiance & Compton Wavepacket Dispersion</span>
                      <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 1: Quantum Foundations</span>
                    </div>
                    <div style="display:flex; gap:6px;">
                      <button id="qc1_btn_mode" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Switch to Wavepacket</button>
                      <button id="qc1_btn_reset" style="background:#1e293b; color:#94a3b8; border:1px solid #475569; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Reset</button>
                    </div>
                  </div>
                  <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
                    <canvas id="qc1_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
                  </div>
                  <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
                    <div>
                      <label style="font-size:0.75rem; color:#94a3b8; display:block;">Temperature T: <span id="qc1_temp_val" style="color:#38bdf8; font-weight:600;">5500 K</span></label>
                      <input type="range" id="qc1_temp" min="2000" max="9000" value="5500" step="100" style="width:100%;">
                    </div>
                    <div>
                      <label style="font-size:0.75rem; color:#94a3b8; display:block;">Packet Width σ₀: <span id="qc1_sigma_val" style="color:#f472b6; font-weight:600;">1.2 Å</span></label>
                      <input type="range" id="qc1_sigma" min="0.5" max="3.0" value="1.2" step="0.1" style="width:100%;">
                    </div>
                    <div>
                      <label style="font-size:0.75rem; color:#94a3b8; display:block;">Wavenumber k₀: <span id="qc1_k0_val" style="color:#34d399; font-weight:600;">1.5 Å⁻¹</span></label>
                      <input type="range" id="qc1_k0" min="0.5" max="3.0" value="1.5" step="0.1" style="width:100%;">
                    </div>
                  </div>
                </div>
              </div>
            </div>
            """

        sec_html = f"""
<section class="textbook-section-card" id="u1-sec{s_idx+1}">
  <header class="sec-header">
    <h3 class="sec-title"><span class="sec-num">{sec_num}</span><span>{sec_title}</span></h3>
  </header>
  <div class="sec-content">
{sec_content_html}
{inline_sim_html}
  </div>
</section>
"""
        sections_html.append(sec_html)

    # Pre-render Unit 1 Problems
    problems_html = []
    for p_idx, prob in enumerate(unit1["problems"]):
        prob_id = f"prob-1-{p_idx+1}"
        prob_title = prob["title"]
        prob_stmt_html = format_markdown(prob["statement"])
        prob_sol_html = format_markdown(prob["solution"])
        diff_label = prob.get("difficulty", "Advanced")

        prob_card = f"""
<div class="problem-card" id="card-{prob_id}">
  <div class="problem-header">
    <div class="problem-title-box">
      <span class="diff-badge diff-hard">{diff_label}</span>
      <strong>Example 1.{p_idx+1}: {prob_title}</strong>
    </div>
  </div>
  <div class="problem-question-box">
{prob_stmt_html}
  </div>
  <button class="solution-toggle-btn" id="btn-sol-{prob_id}" onclick="toggleSolution('sol-content-{prob_id}', this)">
    <span class="toggle-icon">▸</span> <span class="toggle-text">Show Complete Step-by-Step Derivation & Verification</span>
  </button>
  <div class="solution-content" id="sol-content-{prob_id}" style="display: none;">
    <div class="solution-step">
      <div class="step-explanation">
{prob_sol_html}
      </div>
    </div>
  </div>
</div>
"""
        problems_html.append(prob_card)

    all_sections_str = "\n".join(sections_html)
    all_problems_str = "\n".join(problems_html)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Comprehensive SEO Meta Tags -->
  <title>Quantum Chemistry & Statistical Thermodynamics: Operators, Solvable Wells, Approximate Methods, Ensembles, Partition Functions & Quantum Statistics | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university honors master digital textbook on Quantum Chemistry and Statistical Thermodynamics: failure of classical mechanics, blackbody radiation, photoelectric and Compton effect, de Broglie matter waves, Heisenberg uncertainty, Schrödinger wave mechanics, Hermitian operators, postulates of quantum theory, particle in a box and ring, harmonic oscillator, rigid rotor, angular momentum, hydrogen atom and spherical harmonics, fine structure, spin-orbit coupling, Zeeman effect, perturbation theory, Rayleigh-Ritz variational method, helium atom, Pauli exclusion principle, Slater determinants, Hartree-Fock SCF equations, term symbols, Hund's rules, H2+ and H2 molecular orbitals, valence bond theory, configuration interaction, statistical ensembles, Maxwell-Boltzmann statistics, molecular partition functions, chemical equilibrium, Fermi-Dirac and Bose-Einstein quantum distributions, degenerate electron gas, Einstein and Debye heat capacity of solids, and superconductivity. Features 10 interactive 60 FPS Canvas simulations and 90 tiered solved problems with complete step-by-step mathematical derivations.">
  <meta name="keywords" content="Quantum Chemistry, Statistical Thermodynamics, Quantum Mechanics Textbook, Physical Chemistry, Blackbody Radiation, Compton Scattering, de Broglie Waves, Heisenberg Uncertainty Principle, Schrödinger Equation, Hermitian Operators, Particle in a Box, Cyclic Ring Quantization, Harmonic Oscillator, Hermite Polynomials, Ladder Operators, Rigid Rotor, Angular Momentum, Spherical Harmonics, Hydrogen Atom, Associated Laguerre Polynomials, Radial Distribution Function, Spin-Orbit Coupling, Fine Structure, Zeeman Effect, Perturbation Theory, Rayleigh-Ritz Variational Principle, Helium Ground State, Pauli Exclusion Principle, Slater Determinants, Hartree-Fock Method, Atomic Term Symbols, Hund Rules, Born-Oppenheimer Approximation, H2+ Ion, LCAO Molecular Orbitals, Valence Bond Theory, Heitler-London Formalism, Configuration Interaction, Electron Correlation, Microcanonical Ensemble, Canonical Ensemble, Grand Canonical Ensemble, Boltzmann Entropy, Maxwell-Boltzmann Distribution, Molecular Partition Function, Sackur-Tetrode Equation, Chemical Equilibrium Constant, Eyring Transition State Theory, Bose-Einstein Distribution, Bose-Einstein Condensation, Fermi-Dirac Distribution, Fermi Energy, Conduction Electrons in Metals, Einstein Solid Heat Capacity, Debye T3 Law, BCS Superconductivity">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.com/quantum-chemistry-thermodynamics.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Quantum Chemistry & Statistical Thermodynamics: Operators, Solvable Wells, Approximate Methods, Ensembles, Partition Functions & Quantum Statistics | OpenSTEM Digital Academic Press">
  <meta property="og:description" content="Exhaustive university honors digital textbook on Quantum Chemistry and Statistical Thermodynamics with 10 comprehensive units, 80 sections, 90 tiered solved problems, and 10 real-time interactive Canvas simulation engines.">
  <meta property="og:image" content="https://openstemlibrary.com/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD (Strictly Zero Course Numbers) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Quantum Chemistry and Statistical Thermodynamics: Operators, Solvable Potentials, Approximate Methods, Molecular Orbitals, Ensembles, Partition Functions & Quantum Statistics",
    "description": "Comprehensive university honors curriculum covering historical quantum development, exact solvable systems, harmonic oscillator, hydrogen atom, approximation methods, many-electron atoms, chemical bonding, statistical mechanics, molecular partition functions, chemical equilibrium, and quantum condensed matter statistics.",
    "provider": {{
      "@type": "EducationalOrganization",
      "name": "OpenSTEM Digital Academic Press",
      "url": "https://openstemlibrary.com"
    }},
    "educationalLevel": "Undergraduate B.Sc. Honors & STEM Foundation",
    "isAccessibleForFree": true
  }}
  </script>

  <!-- Google Fonts: Inter, Fira Code & Newsreader -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap" rel="stylesheet">

  <!-- KaTeX CSS & JS for LaTeX Math Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

  <!-- Application Stylesheet -->
  <link rel="stylesheet" href="styles.css?v=20261009_v10_quantum_chemistry">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Quantum Chemistry & Stat Thermo</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search blackbody, Compton, Schrödinger, box, ring, Hermite, spherical harmonics, perturbation, variational, Slater, Hartree-Fock, ensembles, partition functions, Fermi, Bose..." class="search-input">
      </div>

      <div class="nav-section-title">Table of Contents</div>
      <ul class="unit-nav-list" id="unit-nav-list">
        <!-- Rendered dynamically by app.js from COURSE_DATA -->
      </ul>
    </aside>

    <!-- Main Content Reader Container -->
    <main class="main-content">
      <!-- Top Sticky Navbar -->
      <header class="top-navbar">
        <div class="course-badge-container">
          <span class="badge-pill badge-course">Chemistry / Physical Chemistry</span>
          <span class="badge-pill badge-credits">Quantum Mechanics, Molecular Orbitals & Statistical Thermodynamics</span>
          <span class="badge-pill" style="background: rgba(16, 185, 129, 0.15); color: #10b981;">100% Free Open Access</span>
        </div>
        <div class="navbar-actions">
          <a href="index.html" class="btn-tool" style="text-decoration:none; display:flex; align-items:center; gap:0.35rem; color:#38bdf8;">← STEM Library</a>
          <button id="btn-font-toggle" class="btn-tool" title="Toggle Academic Reading Font">A/A Academic</button>
          <div class="protection-notice">
            🔒 <span>In-Browser Protected • Direct Download Disabled</span>
          </div>
        </div>
      </header>

      <!-- Content Columns (Wide Centered Reader) -->
      <div class="content-columns" id="main-content-area">
        <!-- Center Textbook Article -->
        <article class="reader-main-column" id="textbook-article">
          <!-- Chapter Hero Header -->
          <header class="unit-hero">
            <div class="unit-number-tag" id="unit-tag">Chapter 1 • Theory & Derivations</div>
            <h1 class="unit-title-heading" id="unit-title">Unit 1: Foundations & Historical Development of Quantum Mechanics</h1>
            <p class="unit-desc-lead" id="unit-desc">
              Comprehensive foundational treatment of the breakdown of classical Newtonian and Maxwellian physics at microscopic scales: blackbody spectral radiance and ultraviolet divergence, Planck's quantized energy hypothesis, the photoelectric effect and Einstein's photon momentum, Compton scattering kinematics, de Broglie matter waves, the Heisenberg uncertainty principle, Schrödinger wave mechanics, Hermitian operator algebra, and the foundational postulates of quantum theory.
            </p>
          </header>

          <!-- Pre-Rendered Sections for Indexing & Instant Load -->
          <div id="textbook-sections">
{all_sections_str}
          </div>

          <!-- Worked Problems Mount Section -->
          <section class="problems-section" id="unit-problems-section" style="margin-top: 3.5rem;">
            <div class="section-title-wrap">
              <h2 class="section-title">Worked Problems & Step-by-Step Quantum Derivations</h2>
              <p class="section-subtitle">Multi-step solved problems covering Planck distribution, photoelectric kinetics, Compton shift, de Broglie wavelengths, uncertainty relations, and Hermitian operator commutation algebra.</p>
            </div>
            <div id="problems-container">
{all_problems_str}
            </div>
          </section>

          <!-- Reader Footer: Academic Cross-Linking Across Entire Library -->
          <footer class="reader-trust-footer">
            <div class="reader-trust-grid">
              <div class="reader-trust-col">
                <span class="trust-col-title">Department of Chemistry</span>
                <span class="trust-col-desc">Complete 11-Volume University Honors Curriculum</span>
              </div>
              <div class="reader-trust-col">
                <span class="trust-col-title">OpenSTEM Digital Press</span>
                <span class="trust-col-desc">Peer-Reviewed Interactive Mathematical Sciences</span>
              </div>
              <div class="reader-trust-col">
                <span class="trust-col-title">60 FPS Simulation Engines</span>
                <span class="trust-col-desc">Hardware-Accelerated HTML5 Canvas Solvers</span>
              </div>
            </div>
            <div class="reader-trust-links">
              <a href="index.html" class="reader-trust-link">STEM Portal Home</a>
              <a href="algebra-trigonometry.html" class="reader-trust-link">Algebra & Trigonometry</a>
              <a href="calculus-1.html" class="reader-trust-link">Calculus I</a>
              <a href="geometry-2d.html" class="reader-trust-link">2D Geometry</a>
              <a href="geometry-3d.html" class="reader-trust-link">3D & Vector Geometry</a>
              <a href="calculus-3.html" class="reader-trust-link">Calculus III</a>
              <a href="linear-algebra.html" class="reader-trust-link">Linear Algebra</a>
              <a href="ordinary-differential-equations-1.html" class="reader-trust-link">Differential Equations I</a>
              <a href="ordinary-differential-equations-2.html" class="reader-trust-link">Differential Equations II</a>
              <a href="complex-analysis.html" class="reader-trust-link">Complex Analysis</a>
              <a href="numerical-analysis.html" class="reader-trust-link">Numerical Analysis</a>
              <a href="abstract-algebra.html" class="reader-trust-link">Abstract Algebra</a>
              <a href="graph-theory.html" class="reader-trust-link">Graph Theory</a>
              <a href="real-analysis.html" class="reader-trust-link">Real Analysis</a>
              <a href="differential-geometry.html" class="reader-trust-link">Differential Geometry</a>
              <a href="number-theory.html" class="reader-trust-link">Theory of Numbers</a>
              <a href="topology.html" class="reader-trust-link">General Topology</a>
              <a href="partial-differential-equations.html" class="reader-trust-link">Partial Differential Equations</a>
              <a href="discrete-mathematics.html" class="reader-trust-link">Discrete Mathematics</a>
              <a href="tensor-analysis.html" class="reader-trust-link">Tensor Analysis</a>
              <a href="fuzzy-mathematics.html" class="reader-trust-link">Fuzzy Mathematics</a>
              <a href="physical-chemistry-1.html" class="reader-trust-link">Physical Chemistry I</a>
              <a href="inorganic-chemistry-1.html" class="reader-trust-link">Inorganic Chemistry I</a>
              <a href="organic-chemistry-1.html" class="reader-trust-link">Organic Chemistry I</a>
              <a href="organic-chemistry-2.html" class="reader-trust-link">Organic Chemistry II</a>
              <a href="analytical-chemistry.html" class="reader-trust-link">Analytical Chemistry</a>
              <a href="nuclear-radiochemistry.html" class="reader-trust-link">Nuclear & Radiochemistry</a>
              <a href="industrial-chemistry.html" class="reader-trust-link">Industrial Chemistry</a>
              <a href="molecular-motion-kinetics.html" class="reader-trust-link">Molecular Motion & Reaction Kinetics</a>
              <a href="natural-products-chemistry.html" class="reader-trust-link">Chemistry of Natural Products</a>
              <a href="chemical-spectroscopy.html" class="reader-trust-link">Chemical Spectroscopy</a>
              <a href="quantum-chemistry-thermodynamics.html" class="reader-trust-link" style="color: #38bdf8; font-weight: 600;">Quantum Chemistry & Stat Thermo</a>
              <a href="about.html" class="reader-trust-link">About & Editorial</a>
              <a href="privacy.html" class="reader-trust-link">Privacy Policy</a>
              <a href="terms.html" class="reader-trust-link">Terms of Service</a>
              <a href="https://discord.gg/tBBKtvFJzW" target="_blank" rel="noopener noreferrer" class="reader-trust-link" style="color: #a5b4fc;">💬 Discord Community</a>
              <a href="mailto:shahriyarkarimsiam@gmail.com" class="reader-trust-link">Contact (shahriyarkarimsiam@gmail.com)</a>
            </div>
            <p class="reader-trust-copy">© 2026 OpenSTEM Global Academic Press • Google AdSense Certified Academic Publisher • Peer-Reviewed University Textbooks</p>
          </footer>

        </article>
      </div>
    </main>

  </div>

  <script>
    function toggleSolution(id, btn) {{
      const el = document.getElementById(id);
      if (!el) return;
      const isHidden = el.style.display === 'none' || !el.style.display;
      el.style.display = isHidden ? 'block' : 'none';
      if (btn) {{
        const textSpan = btn.querySelector('.toggle-text');
        const iconSpan = btn.querySelector('.toggle-icon');
        if (textSpan) textSpan.textContent = isHidden ? 'Hide Complete Step-by-Step Derivation & Verification' : 'Show Complete Step-by-Step Derivation & Verification';
        if (iconSpan) iconSpan.textContent = isHidden ? '▾' : '▸';
      }}
    }}
  </script>

  <!-- Textbook Application Scripts -->
  <script src="departments-data.js?v=20261009_v10_quantum_chemistry"></script>
  <script src="quantum-chemistry-thermodynamics-sims.js?v=20261009_v10_quantum_chemistry"></script>
  <script src="quantum-chemistry-thermodynamics-data.js?v=20261009_v10_quantum_chemistry"></script>
  <script src="app.js?v=20261009_v10_quantum_chemistry"></script>
</body>
</html>
"""

    with open("quantum-chemistry-thermodynamics.html", "w", encoding="utf-8") as f:
        f.write(html_template)

    print("Generated quantum-chemistry-thermodynamics.html successfully.")

    # Audit for prohibited tokens in generated HTML
    prohibited_patterns = [
        r'\bchem\s*\d+',
        r'35\s*\+\s*10\s*\+\s*5',
        r'70\s*\+\s*20\s*\+\s*10',
        r'\b\d+\s*Marks\b',
        r'100\s*Marks',
        r'50\s*Marks',
        r'35\s*Marks',
        r'10\s*Marks',
        r'5\s*Marks',
        r'exam(ination)?\s+marks',
        r'\bgrades?\s*=\s*\d+'
    ]

    violations = []
    for pattern in prohibited_patterns:
        matches = re.findall(pattern, html_template, re.IGNORECASE)
        if matches:
            violations.append((pattern, matches))

    if violations:
        print("PROHIBITED TOKENS DETECTED IN HTML:")
        for pat, m in violations:
            print(f" - Pattern '{pat}': {m}")
        raise ValueError("Prohibited tokens found in generated HTML!")
    else:
        print("✓ Zero prohibited tokens found in HTML! Audit passed.")

if __name__ == "__main__":
    build_html()
