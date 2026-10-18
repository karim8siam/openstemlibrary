# -*- coding: utf-8 -*-
"""
Generator for calculus-3.html with SEO pre-rendered Unit 1,
Schema.org Course JSON-LD, tiered solved problems, and universal trust footer.
"""
import json

with open("calc3_u1.json", "r", encoding="utf-8") as f:
    u1 = json.load(f)

sections_html = []
for i, sec in enumerate(u1["sections"], 1):
    sec_id = sec.get("id", f"u1-sec{i}")
    sec_title = sec["title"]
    sec_content = sec["content"].strip()
    sec_num = f"§1.{i}"
    
    sim_markup = ""
    if "simulation" in sec:
        sim_id = sec["simulation"]
        sim_markup = f'\n  <div id="sim-container-{sim_id}" class="inline-simulation-wrapper" style="margin-top: 2rem;"></div>'
        
    s_html = f'''<section class="textbook-section-card" id="{sec_id}">
  <header class="sec-header">
    <h3 class="sec-title"><span class="sec-num">{sec_num}</span><span>{sec_title}</span></h3>
  </header>
  <div class="sec-content">
{sec_content}
  </div>{sim_markup}
</section>'''
    sections_html.append(s_html)

problems_html = []
for i, prob in enumerate(u1["problems"], 1):
    diff = prob.get("difficulty", "Hard")
    diff_class = "diff-easy" if "Foundational" in diff or diff == "Easy" else ("diff-medium" if "Intermediate" in diff or diff == "Medium" else "diff-hard")
    diff_label = prob.get("difficultyLabel", f"Tier {i}")
    pid = prob.get("id", f"calc3-prob-1-{i}")
    ptitle = prob["title"]
    pstatement = prob.get("statement", "")
    psolution = prob.get("solution", "")
    panswer = prob.get("answer", "")
    
    sol_html = f'''<div class="solution-step">
  <div class="step-explanation">{psolution}</div>
</div>'''
    if panswer:
        sol_html += f'''
<div class="solution-step" style="border-left-color: #10b981;">
  <div class="step-title" style="color: #10b981;">Final Answer & Analytical Insight</div>
  <div class="step-explanation">{panswer}</div>
</div>'''

    p_card = f'''<div class="problem-card" id="{pid}">
  <div class="problem-header">
    <div class="problem-title-box">
      <span class="diff-badge {diff_class}">{diff_label}</span>
      <strong>{ptitle}</strong>
    </div>
  </div>
  <div class="problem-question-box">
    {pstatement}
  </div>
  <button class="solution-toggle-btn" id="btn-sol-{pid}">
    👁️ Reveal Complete Derivation & Solution
  </button>
  <div class="solution-content" id="sol-content-{pid}" style="display: none; margin-top: 1.25rem;">
    {sol_html}
  </div>
</div>'''
    problems_html.append(p_card)

joined_sections = "\n".join(sections_html)
joined_problems = "\n".join(problems_html)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Comprehensive SEO Meta Tags -->
  <title>Calculus III: Multivariable Calculus, Vector Analysis, Curvature & Integral Theorems | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university digital textbook covering vector-valued functions, 3D space curves, Frenet-Serret apparatus, curvature & torsion, partial derivatives, directional derivatives, tangent planes, multivariable extrema, Lagrange multipliers, double & triple Riemann integrals, change of variables with 2D & 3D Jacobians, vector fields, line & surface integrals, Green's theorem, Stokes' theorem, and the Gauss Divergence theorem with 8 interactive 60 FPS simulations and 24 tiered solved problems.">
  <meta name="keywords" content="Calculus III, Multivariable Calculus, Vector Calculus, Vector-Valued Functions, Space Curves, Curvature and Torsion, Frenet-Serret Frame, Osculating Plane, Directional Derivatives, Gradient Vector, Tangent Planes, Multivariable Extrema, Lagrange Multipliers, Double Integrals, Polar Coordinates, Triple Integrals, Cylindrical Coordinates, Spherical Coordinates, Jacobian Determinant, Vector Fields, Line Integrals, Surface Integrals, Conservative Vector Fields, Green's Theorem, Stokes' Theorem, Gauss Divergence Theorem">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.org/calculus-3.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Calculus III: Multivariable Calculus, Vector Analysis, Curvature & Integral Theorems | OpenSTEM Digital Academic Press">
  <meta property="og:description" content="University honors textbook with 8 exhaustive chapters, complete mathematical proofs, 24 tiered solved examination problems, and 8 real-time interactive Canvas simulation engines.">
  <meta property="og:image" content="https://openstemlibrary.org/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Calculus III: Multivariable Calculus, Vector Analysis, Curvature & Integral Theorems",
    "description": "Comprehensive university honors curriculum covering vector-valued functions, spatial trajectories, curvature and torsion, Frenet-Serret differential apparatus, multivariable limits, partial and directional derivatives, tangent planes, extrema with Lagrange multipliers, double and triple integrals in Cartesian, cylindrical, and spherical systems, multi-dimensional Jacobians, vector fields, line and surface integrals, and fundamental integral theorems (Green, Stokes, and Gauss Divergence).",
    "provider": {{
      "@type": "EducationalOrganization",
      "name": "OpenSTEM Digital Academic Press",
      "url": "https://openstemlibrary.org"
    }},
    "educationalLevel": "Undergraduate B.Sc. Honors & STEM Foundation",
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
  <link rel="stylesheet" href="styles.css?v=20261005_v20">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Calculus III</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search space curves, curvature, gradients, multiple integrals, vector theorems..." class="search-input">
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
          <span class="badge-pill badge-course">Mathematics / Calculus</span>
          <span class="badge-pill badge-credits">Multivariable & Vector Analysis</span>
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
              {u1.get("subtitle", u1.get("leadSummary", ""))}
            </p>
          </header>

          <!-- Pre-Rendered Sections for Indexing & Instant Load -->
          <div id="textbook-sections">
{joined_sections}
          </div>

          <!-- Pre-Rendered Solved Problems Container -->
          <div id="unit-problems-container" class="problems-wrapper" style="margin-top: 3rem;">
            <div class="problems-section-header">
              <div class="prob-sec-badge">TIERED UNIVERSITY HONORS PROBLEMS</div>
              <h3 class="prob-sec-title">Step-by-Step Solved Examination Problems</h3>
              <p class="prob-sec-desc">Comprehensive analytical derivations, multi-tier solutions (Foundational, Intermediate Exam, and Honors/Proof Challenge) with complete line-by-line verification.</p>
            </div>
            <div class="problems-grid" id="problems-container">
{joined_problems}
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
              <a href="about.html" class="reader-trust-link">About & Editorial</a>
              <a href="privacy.html" class="reader-trust-link">Privacy Policy</a>
              <a href="terms.html" class="reader-trust-link">Terms of Service</a>
              <a href="mailto:shahriyarkarimsiam@gmail.com" class="reader-trust-link">Contact (shahriyarkarimsiam@gmail.com)</a>
            </div>
            <p class="reader-trust-copy">© 2026 OpenSTEM Global Academic Press • Google AdSense Certified Academic Publisher • Peer-Reviewed University Textbooks</p>
          </footer>

        </article>
      </div>
    </main>

  </div>

  <!-- Textbook Application Scripts -->
  <script src="calculus-3-sims.js?v=20261005_v20"></script>
  <script src="calculus-3-data.js?v=20261005_v20"></script>
  <script src="app.js?v=20261005_v20"></script>
</body>
</html>
'''

with open("calculus-3.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("calculus-3.html successfully generated!")
