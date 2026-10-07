# -*- coding: utf-8 -*-
"""
Generator for ordinary-differential-equations-1.html
Pre-renders Unit 1 for instant first paint and Googlebot SEO indexing,
injects Schema.org Course and BreadcrumbList JSON-LD,
links the Google-compliant favicon suite, and mounts the 8-chapter curriculum.
"""
import json
import re

with open("ordinary-differential-equations-1-data.js", "r", encoding="utf-8") as f:
    raw = f.read()
    raw_json = raw[len("window.COURSE_DATA = "):].rstrip(";\n")
    course_data = json.loads(raw_json)

u1 = course_data["units"][0]

# Generate Pre-Rendered Sections for Unit 1
sections_html = []
for sec in u1["sections"]:
    sec_id = sec["id"]
    sec_title = sec["title"]
    sec_content = sec["content"].strip()
    sec_num = f"§{sec['secNumber']}"
    
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

# Generate Pre-Rendered Problems for Unit 1
problems_html = []
for i, prob in enumerate(u1["problems"], 1):
    diff = prob.get("difficulty", "Hard")
    diff_class = "diff-easy" if "Foundational" in diff or diff == "Easy" or i == 1 else ("diff-medium" if "Intermediate" in diff or diff == "Medium" or i == 2 else "diff-hard")
    diff_label = prob.get("difficultyLabel", f"Tier {i} Problem")
    pid = prob.get("id", f"ode1-prob-{i}")
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
  <div class="step-title" style="color: #10b981;">Analytical Answer & Insights</div>
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
  <title>Ordinary Differential Equations I: Analytical Methods, Existence Theory & Modeling | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university digital textbook for MTH 2103 Ordinary Differential Equations I: classifications, Picard-Lindelöf existence and uniqueness theorem, direction fields, exact differential forms, integrating factors, Bernoulli, Riccati, and Clairaut equations, orthogonal trajectories, Wronskian algebra, Abel's identity, reduction of order, constant coefficient and Cauchy-Euler equations, undetermined coefficients, variation of parameters, mechanical vibrations, resonance, RLC networks, and rocket dynamics with 8 interactive 60 FPS simulations and 24 tiered solved university examination problems.">
  <meta name="keywords" content="Ordinary Differential Equations, ODE, Picard Lindelof Theorem, Direction Fields, Exact Equations, Integrating Factor, Bernoulli Equation, Riccati Equation, Clairaut Equation, Orthogonal Trajectories, Wronskian, Abels Formula, Reduction of Order, Cauchy Euler Equation, Undetermined Coefficients, Variation of Parameters, Mechanical Vibrations, Resonance, RLC Circuits, Rocket Motion">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.com/ordinary-differential-equations-1.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://openstemlibrary.com/ordinary-differential-equations-1.html">
  <meta property="og:title" content="Ordinary Differential Equations I: Analytical Methods, Existence Theory & Modeling | OpenSTEM">
  <meta property="og:description" content="Comprehensive university honors course covering analytical first-order and higher-order ODEs, Picard existence theory, Wronskian algebra, mechanical resonance, and 8 real-time interactive numerical simulations.">
  <meta property="og:image" content="https://openstemlibrary.com/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Ordinary Differential Equations I | OpenSTEM Digital Academic Press">
  <meta name="twitter:description" content="Free university digital textbook covering ODE classifications, Picard iterations, exact forms, Wronskian, Cauchy-Euler, variation of parameters, and resonance.">
  <meta name="twitter:image" content="https://openstemlibrary.com/og-image.png">

  <!-- Favicon & Search Engine Icons -->
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="icon" type="image/png" sizes="48x48" href="favicon-48x48.png">
  <link rel="icon" type="image/png" sizes="96x96" href="favicon-96x96.png">
  <link rel="icon" type="image/png" sizes="192x192" href="favicon-192x192.png">
  <link rel="icon" type="image/svg+xml" href="logo.svg">
  <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">

  <!-- Schema.org Educational Course JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "MTH 2103: Ordinary Differential Equations I",
    "description": "Comprehensive university honors curriculum covering classifications, Picard-Lindelof existence and uniqueness, exact equations, integrating factors, Bernoulli, Riccati, Clairaut equations, orthogonal trajectories, linear differential operators, Wronskian, Abels identity, reduction of order, constant coefficient and Cauchy-Euler equations, undetermined coefficients, variation of parameters, mechanical vibrations, resonance, and rocket dynamics.",
    "provider": {{
      "@type": "EducationalOrganization",
      "name": "OpenSTEM Digital Academic Press",
      "url": "https://openstemlibrary.com"
    }},
    "educationalLevel": "Undergraduate B.Sc. Honours & STEM Foundation",
    "isAccessibleForFree": true
  }}
  </script>

  <!-- Schema.org Breadcrumb Navigation -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "OpenSTEM Library",
        "item": "https://openstemlibrary.com/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Department of Mathematics",
        "item": "https://openstemlibrary.com/#mathematics"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "Ordinary Differential Equations I",
        "item": "https://openstemlibrary.com/ordinary-differential-equations-1.html"
      }}
    ]
  }}
  </script>

  <!-- Google Fonts: Inter & Fira Code (Optimized Non-blocking) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap" media="print" onload="this.media='all'">
  <noscript>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap">
  </noscript>

  <!-- KaTeX for High-Fidelity Mathematical Typography -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

  <!-- Textbook Master Stylesheet -->
  <link rel="stylesheet" href="styles.css?v=20261006_v21">
</head>
<body class="academic-theme">

  <div class="app-container">

    <!-- Collapsible Sidebar Navigation -->
    <aside class="sidebar" id="sidebar">
      <div class="brand-header">
        <a href="index.html" style="display:flex; align-items:center; gap:0.75rem; text-decoration:none; color:inherit;">
          <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
          <div>
            <div class="brand-title">Differential Equations I</div>
            <div class="brand-subtitle">MTH 2103 • Honors Digital Text</div>
          </div>
        </a>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search Picard, exact, Wronskian, resonance..." class="search-input" aria-label="Search differential equations textbook topics">
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
          <span class="badge-pill badge-course">Mathematics / MTH 2103</span>
          <span class="badge-pill badge-credits">3 Credits • 45 Lecture Hours</span>
          <span class="badge-pill" style="background: rgba(16, 185, 129, 0.15); color: #10b981;">100% Free Open Access</span>
        </div>
        <div class="navbar-actions">
          <a href="index.html" class="btn-tool" style="text-decoration:none; display:flex; align-items:center; gap:0.35rem; color:#38bdf8;">← STEM Library</a>
          <button id="btn-font-toggle" class="btn-tool" title="Toggle Academic Reading Font" aria-label="Toggle academic font serif sans-serif">A/A Academic</button>
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
{joined_sections}
          </div>

          <!-- Unit Fallback Simulations Mount -->
          <div class="simulations-container" id="sim-section-wrap" style="display:none; margin-top:2.5rem;">
            <div class="section-divider">
              <span class="divider-label">Interactive 60 FPS Numerical Physics & Math Simulators</span>
            </div>
            <div id="simulations-mount"></div>
          </div>

          <!-- Worked Problems Section -->
          <section class="problems-section-wrapper" id="unit-problems-section">
            <div class="section-divider">
              <span class="divider-label">Tiered University Examination Problem Sets (Full Derivations)</span>
            </div>
            <div class="problems-container" id="problems-mount">
{joined_problems}
            </div>
          </section>

          <!-- Chapter Navigation Footer -->
          <nav class="unit-footer-nav" id="unit-footer-nav">
            <button class="nav-btn prev-btn" id="btn-prev-unit" disabled>← Previous Chapter</button>
            <span class="nav-unit-indicator" id="nav-unit-indicator">Chapter 1 of 8</span>
            <button class="nav-btn next-btn" id="btn-next-unit">Next Chapter →</button>
          </nav>

          <!-- Universal Academic Trust Footer -->
          <footer class="reader-trust-footer">
            <div class="reader-trust-grid">
              <div class="reader-trust-col">
                <div class="trust-badge-title">⚖️ Academic Rigor & Citation</div>
                <p>Peer-reviewed undergraduate honors curriculum adhering to the standards of Griffiths, Boyce & DiPrima, Coddington & Levinson, and Zill. Mathematical proofs are complete with unskipped derivations.</p>
              </div>
              <div class="reader-trust-col">
                <div class="trust-badge-title">🎓 Open Educational Resource</div>
                <p>Free, accessible digital scholarship designed for university lecture adoption, international self-study, and competitive mathematical examinations worldwide.</p>
              </div>
              <div class="reader-trust-col">
                <div class="trust-badge-title">📬 Mathematical Errata Desk</div>
                <p>Report typographic discrepancies, alternative proofs, or pedagogical suggestions directly to the academic editorial board at <a href="mailto:shahriyarkarimsiam@gmail.com" style="color:#38bdf8;">shahriyarkarimsiam@gmail.com</a>.</p>
              </div>
            </div>
            <div class="reader-trust-links">
              <a href="index.html" class="reader-trust-link">OpenSTEM Home</a>
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
  <script src="ordinary-differential-equations-1-sims.js?v=20261007_v1"></script>
  <script src="ordinary-differential-equations-1-data.js?v=20261007_v1"></script>
  <script src="app.js?v=20261007_v1"></script>
</body>
</html>
'''

with open("ordinary-differential-equations-1.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated ordinary-differential-equations-1.html successfully!")
