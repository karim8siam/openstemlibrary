import json

with open("qm2_u1.json", "r", encoding="utf-8") as f:
    u1 = json.load(f)

# Pre-render Unit 1 sections
sec_html = ""
for s_idx, sec in enumerate(u1["sections"]):
    raw_num = f"1.{s_idx + 1}"
    sim_id = sec.get("simulation")
    sim_html = ""
    if sim_id:
        sim_html = f"""  <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
    <div class="simulation-slot" id="sim-container-{sim_id}"></div>
  </div>
"""

    sec_html += f"""<section class="textbook-section-card" id="{sec['id']}">
  <header class="sec-header">
    <h3 class="sec-title"><span class="sec-num">§{raw_num}</span><span>{sec['title']}</span></h3>
  </header>
  <div class="sec-content">
{sec['content']}
  </div>
{sim_html}</section>
"""

# Pre-render Unit 1 problems
prob_html = ""
for p_idx, prob in enumerate(u1.get("solvedProblems", [])):
    p_num = f"1.{p_idx + 1}"
    
    steps_html = f"""      <div class="solution-step">
        <div class="step-title">Full Rigorous Analytical Solution</div>
        <div class="step-explanation">{prob['solution']}</div>
      </div>
      <div class="solution-step" style="border-left-color: #10b981;">
        <div class="step-title" style="color: #10b981;">Final Answer & Verification</div>
        <div class="step-explanation"><p><strong>Complete rigorous derivation and proof detailed above.</strong></p></div>
      </div>
"""

    statement = prob.get("statement") or prob.get("question") or ""
    prob_html += f"""<div class="problem-card" id="qm2-prob-{p_num.replace('.', '-')}">
  <div class="problem-header">
    <div class="prob-badge">SOLVED PROBLEM {p_num}</div>
    <h4 class="prob-title">{prob['title']}</h4>
  </div>
  <div class="problem-statement">
    <p>{statement}</p>
  </div>
  <div class="solution-container">
    <div class="solution-header">
      <span class="sol-tag">RIGOROUS DERIVATION & EXAM SOLUTION</span>
    </div>
    <div class="solution-steps">
{steps_html}    </div>
  </div>
</div>
"""

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Comprehensive SEO Meta Tags -->
  <title>Quantum Mechanics II: Advanced Dynamics, Perturbation Theory, Scattering & Relativistic Waves | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university digital textbook covering Dirac bra-ket algebra, Hilbert space geometry, operator representations, density matrix formalism, harmonic oscillator matrix mechanics, quantum dynamics across Schrödinger, Heisenberg, and Dirac pictures, Rabi oscillations, time-independent and time-dependent perturbation theory, Hydrogen fine structure, Stark and Zeeman effects, Fermi's Golden Rule, variational methods, semiclassical WKB approximation, Bohr-Sommerfeld quantization, angular momentum Lie algebra, spin-1/2, Clebsch-Gordan coefficients, Wigner-Eckart theorem, identical particles, degenerate Fermi gas, Landau levels, partial wave and Born scattering theory, and relativistic Klein-Gordon and Dirac equations with 16 interactive 60 FPS simulations.">
  <meta name="keywords" content="Quantum Mechanics II Textbook, Dirac Notation, Bra-Ket Algebra, Density Matrix, Heisenberg Picture, Interaction Picture, Rabi Flopping, Time-Independent Perturbation Theory, Degenerate Perturbation, Hydrogen Fine Structure, Relativistic Kinetic Correction, Spin-Orbit Coupling, Darwin Term, Stark Effect, Zeeman Effect, Paschen-Back, Time-Dependent Perturbation, Fermi Golden Rule, Einstein A B Coefficients, Variational Method Helium, WKB Method, Airy Functions, Bohr-Sommerfeld, Alpha Decay Gamow, Adiabatic Theorem, Berry Phase, Angular Momentum, Pauli Matrices, Clebsch-Gordan Coefficients, Wigner-Eckart Theorem, Identical Particles, Slater Determinant, Exchange Interaction, Degenerate Fermi Gas, Landau Levels, Partial Wave Analysis, Phase Shifts, Optical Theorem, Breit-Wigner Resonance, Lippmann-Schwinger, Born Approximation, Rutherford Scattering, Klein-Gordon Equation, Dirac Equation, Gamma Matrices, Clifford Algebra, Electron Spin g=2, Foldy-Wouthuysen, Hole Theory, Positron, Klein Paradox">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.org/quantum-mechanics-2.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Quantum Mechanics II | OpenSTEM Digital Textbook">
  <meta property="og:description" content="University honors course with 8 exhaustive chapters, complete mathematical derivations, 24 solved honors exam problems, and 16 real-time interactive numerical simulations.">
  <meta property="og:image" content="https://openstemlibrary.org/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Quantum Mechanics II: Advanced Dynamics, Perturbation Theory, Scattering & Relativistic Waves",
    "description": "Comprehensive university honors curriculum covering Dirac notation, matrix mechanics, quantum dynamics, perturbation theory, variational and WKB semiclassical methods, angular momentum coupling, identical particles, scattering theory, and relativistic quantum mechanics.",
    "provider": {{
      "@type": "EducationalOrganization",
      "name": "OpenSTEM Digital Academic Press",
      "url": "https://openstemlibrary.org"
    }},
    "educationalLevel": "Undergraduate B.Sc. Honors & Graduate",
    "isAccessibleForFree": true
  }}
  </script>

  <!-- Google Fonts: Inter & Fira Code -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap" rel="stylesheet">

  <!-- KaTeX CSS & JS for LaTeX Math Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

  <!-- Application Stylesheet -->
  <link rel="stylesheet" href="styles.css?v=20261005_v15">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Quantum Mechanics II</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search topics, operators, equations..." class="search-input">
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
          <span class="badge-pill badge-course">Physics / Advanced Theoretical Physics</span>
          <span class="badge-pill badge-credits">Quantum Mechanics II</span>
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
            <h1 class="unit-title-heading" id="unit-title">{u1['title']}</h1>
            <p class="unit-desc-lead" id="unit-desc">
              {u1['description']}
            </p>
          </header>

          <!-- Textbook Sections Container -->
          <div id="textbook-sections">
{sec_html}
          </div>

          <!-- Solved University Exam Problems Section -->
          <section class="solved-problems-section" id="solved-problems-section">
            <div class="solved-section-header">
              <div class="solved-badge">EXAM SUCCESS WORKSHOP</div>
              <h3 class="solved-title">Solved University Examination Problems</h3>
              <p class="solved-desc">Step-by-step mathematical solutions to classic university honors examination questions.</p>
            </div>
            <div class="problem-cards-list" id="problem-cards-list">
{prob_html}
            </div>
          </section>

        </article>
      </div>
    </main>

  </div>

  <!-- Textbook Application Scripts -->
  <script src="qm2-sims.js?v=20261005_v15"></script>
  <script src="qm2-data.js?v=20261005_v15"></script>
  <script src="app.js?v=20261005_v15"></script>
</body>
</html>
"""

with open("quantum-mechanics-2.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("quantum-mechanics-2.html successfully created!")
