# -*- coding: utf-8 -*-
"""
generate_na_html.py
Generates numerical-analysis.html with full layout parity to linear-algebra.html,
deep SEO meta tags, Schema.org JSON-LD (strictly zero course numbers),
pre-rendered Unit 1 sections & worked problems, interactive Canvas simulations mount,
font toggle, live topic search, and comprehensive trust footer.
"""

import build_unit1

def generate_html():
    u1 = build_unit1.get_unit1()

    # Pre-render Unit 1 sections
    sections_html = []
    for s_idx, sec in enumerate(u1["sections"], start=1):
        sec_id = f"u1-sec{s_idx}"
        sec_num = sec.get("secNumber", f"1.{s_idx}")
        sec_title = sec["title"]
        sec_content = sec["content"]
        
        # Simulation mount if section has it
        sim_mount_html = ""
        sims = sec.get("simulations", [])
        if sims:
            for sim_id in sims:
                sim_mount_html += f"""
<div class="simulation-card" id="{sim_id}-container" style="margin: 1.5rem 0;">
  <div class="sim-header">
    <div class="sim-title">Interactive Computational Laboratory: {sec_title}</div>
    <div class="sim-badge">60 FPS Real-Time Canvas Engine</div>
  </div>
  <div class="canvas-wrapper" style="position: relative; width: 100%; height: 380px; background: #0f172a; border-radius: 8px; overflow: hidden;">
    <canvas id="{sim_id}" width="800" height="380" style="width: 100%; height: 100%; display: block;"></canvas>
  </div>
  <div class="sim-controls" id="{sim_id}-controls" style="padding: 1rem; background: #1e293b; border-radius: 0 0 8px 8px; display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center;"></div>
</div>
"""

        s_block = f"""<section class="textbook-section-card" id="{sec_id}">
  <header class="sec-header">
    <h3 class="sec-title"><span class="sec-num">§{sec_num}</span><span>{sec_title}</span></h3>
  </header>
  <div class="sec-content">
{sec_content}
  </div>
  {sim_mount_html}
</section>"""
        sections_html.append(s_block)

    # Pre-render Unit 1 solved problems
    problems_html = []
    for p_idx, prob in enumerate(u1["problems"], start=1):
        prob_id = f"na-prob-1-{p_idx}"
        tier = prob.get("tier", p_idx)
        if tier in (1, "1", "Foundational"):
            diff_class = "diff-easy"
            diff_label = "Tier 1 • Foundational Concept"
        elif tier in (2, "2", "Advanced"):
            diff_class = "diff-medium"
            diff_label = "Tier 2 • Advanced Algorithmic"
        else:
            diff_class = "diff-hard"
            diff_label = "Tier 3 • Honors / Proof Challenge"

        prob_title = prob.get("title", f"Solved Problem 1.{p_idx}")
        statement = prob.get("statement", "")
        solution = prob.get("solution", "")
        answer = prob.get("answer", "")

        answer_html = ""
        if answer:
            answer_html = f"""
<div class="solution-step" style="border-left-color: #10b981;">
  <div class="step-title" style="color: #10b981;">Final Answer & Analytical Insight</div>
  <div class="step-explanation">{answer}</div>
</div>
"""

        p_block = f"""<div class="problem-card" id="{prob_id}">
  <div class="problem-header">
    <div class="problem-title-box">
      <span class="diff-badge {diff_class}">{diff_label}</span>
      <strong>{prob_title}</strong>
    </div>
  </div>
  <div class="problem-question-box">
    {statement}
  </div>
  <button class="solution-toggle-btn" id="btn-sol-{prob_id}">
    👁️ Reveal Complete Derivation & Solution
  </button>
  <div class="solution-content" id="sol-content-{prob_id}" style="display: none; margin-top: 1.25rem;">
    <div class="solution-step">
      <div class="step-explanation">{solution}</div>
    </div>
    {answer_html}
  </div>
</div>"""
        problems_html.append(p_block)

    rendered_sections = "\n".join(sections_html)
    rendered_problems = "\n".join(problems_html)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Comprehensive SEO Meta Tags -->
  <title>Numerical Analysis & Computational Methods: Algorithms, Error Analysis, Quadrature, Linear Systems & Differential Equations | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free comprehensive university honors digital textbook covering algorithmic numerical approximations, IEEE floating-point error theory, bracketing and open root-finding, polynomial interpolation and Runge's phenomenon, numerical differentiation and high-order Gaussian quadrature, direct and iterative numerical linear algebra, single-step and multi-step ODE initial value solvers, Dahlquist absolute stability theory, stiff differential equations, and shooting and finite difference boundary value algorithms with 8 interactive 60 FPS simulations and 24 tiered solved examination problems.">
  <meta name="keywords" content="Numerical Analysis, Computational Methods, Floating Point Error, IEEE 754, Bisection Method, Regula Falsi, Newton-Raphson, Aitken Delta Squared, Polynomial Interpolation, Lagrange Interpolation, Newton Divided Differences, Chebyshev Nodes, Runge Phenomenon, Numerical Differentiation, Richardson Extrapolation, Simpson Rule, Weddle Rule, Gaussian Quadrature, Gauss-Legendre, LU Decomposition, Cholesky Factorization, Jacobi Method, Gauss-Seidel, SOR Method, Picard Iteration, Runge-Kutta, RK4, Butcher Tableau, Local Truncation Error, Global Truncation Error, Discrete Gronwall Inequality, Adaptive Step Size, Dahlquist Test Equation, Absolute Stability Region, Stiff Differential Equations, A-Stability, L-Stability, Linear Multistep Methods, Adams-Bashforth, Adams-Moulton, Predictor-Corrector, BDF, Dahlquist Root Condition, Dahlquist Barriers, Boundary Value Problems, Linear Shooting Method, Nonlinear Shooting Method, Variational Sensitivity Equations, Finite Difference Method, Tridiagonal Matrix Algorithm, Thomas Algorithm">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.org/numerical-analysis.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Numerical Analysis & Computational Methods: Algorithms, Error Analysis, Quadrature, Linear Systems & Differential Equations | OpenSTEM Digital Academic Press">
  <meta property="og:description" content="Exhaustive university honors textbook with 8 chapters, unskipped line-by-line mathematical proofs, 24 tiered solved problems, and 8 real-time interactive Canvas simulation engines.">
  <meta property="og:image" content="https://openstemlibrary.org/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Numerical Analysis & Computational Methods: Algorithms, Error Analysis, Quadrature, Linear Systems & Differential Equations",
    "description": "Comprehensive university honors curriculum covering algorithmic numerical approximations, IEEE floating-point error theory, bracketing and open root-finding, polynomial interpolation and Runge's phenomenon, numerical differentiation and high-order Gaussian quadrature, direct and iterative numerical linear algebra, single-step and multi-step ODE initial value solvers, Dahlquist absolute stability theory, stiff differential equations, and shooting and finite difference boundary value algorithms.",
    "provider": {{
      "@type": "EducationalOrganization",
      "name": "OpenSTEM Digital Academic Press",
      "url": "https://openstemlibrary.org"
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
  <link rel="stylesheet" href="styles.css?v=20261007_v1">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Numerical Analysis</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search root-finding, interpolation, RK4, stiff ODEs, shooting..." class="search-input">
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
          <span class="badge-pill badge-course">Mathematics / Computational Mathematics</span>
          <span class="badge-pill badge-credits">Numerical Analysis & Computational Methods</span>
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
            <h1 class="unit-title-heading" id="unit-title">{u1["title"]}</h1>
            <p class="unit-desc-lead" id="unit-desc">
              {u1["leadSummary"]}
            </p>
          </header>

          <!-- Pre-Rendered Sections for Indexing & Instant Load -->
          <div id="textbook-sections">
{rendered_sections}
          </div>

          <!-- Tiered Solved Practice Problems Section -->
          <div class="practice-problems-section">
            <div class="prob-sec-header">
              <h2 class="prob-sec-title">Tiered Solved Practice Problems & Examination Proofs</h2>
              <p class="prob-sec-desc">Comprehensive analytical derivations, multi-tier solutions (Foundational, Intermediate Algorithmic, and Honors/Proof Challenge) with complete line-by-line verification.</p>
            </div>
            <div class="problems-grid" id="problems-container">
{rendered_problems}
            </div>
          </div>

          <!-- Universal Academic Trust, SEO Cross-Linking & Legal Compliance Footer -->
          <footer class="reader-trust-footer">
            <div class="reader-trust-links">
              <a href="index.html" class="reader-trust-link">← All Academic Departments</a>
              <a href="reader.html" class="reader-trust-link">Quantum Mechanics I</a>
              <a href="mechanics.html" class="reader-trust-link">Mechanics</a>
              <a href="electrodynamics.html" class="reader-trust-link">Electrodynamics</a>
              <a href="optics.html" class="reader-trust-link">Wave Optics</a>
              <a href="statistical-mechanics.html" class="reader-trust-link">Statistical Mechanics</a>
              <a href="properties-of-matter.html" class="reader-trust-link">Properties of Matter</a>
              <a href="electricity-magnetism.html" class="reader-trust-link">Electricity & Magnetism</a>
              <a href="thermal-physics.html" class="reader-trust-link">Thermal Physics</a>
              <a href="classical-mechanics.html" class="reader-trust-link">Classical Mechanics</a>
              <a href="basic-electronics.html" class="reader-trust-link">Basic Electronics</a>
              <a href="atomic-molecular-physics.html" class="reader-trust-link">Atomic & Molecular Physics</a>
              <a href="solid-state-physics.html" class="reader-trust-link">Solid State Physics</a>
              <a href="nuclear-physics.html" class="reader-trust-link">Nuclear Physics</a>
              <a href="digital-electronics.html" class="reader-trust-link">Digital Electronics</a>
              <a href="quantum-mechanics-2.html" class="reader-trust-link">Quantum Mechanics II</a>
              <a href="astrophysics.html" class="reader-trust-link">Astrophysics</a>
              <a href="plasma-physics.html" class="reader-trust-link">Plasma Physics</a>
              <a href="solid-state-physics-2.html" class="reader-trust-link">Solid State Physics II</a>
              <a href="nuclear-physics-2.html" class="reader-trust-link">Nuclear Physics II</a>
              <a href="reactor-physics.html" class="reader-trust-link">Reactor Physics</a>
              <a href="calculus-1.html" class="reader-trust-link">Calculus I</a>
              <a href="geometry-2d.html" class="reader-trust-link">Two-Dimensional Geometry</a>
              <a href="basic-algebra.html" class="reader-trust-link">Basic Algebra</a>
              <a href="calculus-2.html" class="reader-trust-link">Calculus II</a>
              <a href="geometry-3d.html" class="reader-trust-link">3D & Vector Geometry</a>
              <a href="calculus-3.html" class="reader-trust-link">Calculus III</a>
              <a href="linear-algebra.html" class="reader-trust-link">Linear Algebra</a>
              <a href="ordinary-differential-equations-1.html" class="reader-trust-link">Differential Equations I</a>
              <a href="ordinary-differential-equations-2.html" class="reader-trust-link">Differential Equations II</a>
              <a href="complex-analysis.html" class="reader-trust-link">Complex Analysis</a>
              <a href="numerical-analysis.html" class="reader-trust-link" style="color: #38bdf8; font-weight: 600;">Numerical Analysis</a>
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

  <!-- Textbook Application Scripts -->
  <script src="numerical-analysis-sims.js?v=20261007_v1"></script>
  <script src="numerical-analysis-data.js?v=20261007_v1"></script>
  <script src="app.js?v=20261007_v1"></script>
</body>
</html>
"""

    with open("numerical-analysis.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Successfully generated numerical-analysis.html! Size:", len(html_content), "bytes")

if __name__ == "__main__":
    generate_html()
