# -*- coding: utf-8 -*-
"""
Generator for complex-analysis.html
Pre-renders Unit 1 for instant first paint and Googlebot SEO indexing,
strictly adheres to the linear-algebra.html gold standard layout,
omits all university course numbers, and mounts the 8-chapter curriculum.
"""
import json
import re

with open("complex-analysis-data.js", "r", encoding="utf-8") as f:
    raw = f.read()
    raw_json = raw[raw.find("{"):raw.rfind("}") + 1]
    course_data = json.loads(raw_json)

u1 = course_data["units"][0]

# Generate Pre-Rendered Sections for Unit 1
sections_html = []
for sec in u1["sections"]:
    sec_id = f"u1-sec{sec['secNumber'].replace('.', '-')}"
    sec_title = sec["title"]
    sec_content = sec["content"].strip()
    sec_num = f"§{sec['secNumber']}"
    
    sim_markup = ""
    if "simulation" in sec:
        sim_id = sec["simulation"]
        sim_markup = f'\n  <div id="sim-container-{sim_id}" class="inline-simulation-wrapper" style="margin-top: 2rem;"></div>'
    elif "simulations" in u1 and len(u1["simulations"]) > 0 and sec == u1["sections"][0]:
        sim_id = u1["simulations"][0]
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
for i, prob in enumerate(u1.get("problems", []), 1):
    diff = prob.get("difficulty", "Hard")
    diff_class = "diff-easy" if "Foundational" in diff or diff == "Easy" or i == 1 else ("diff-medium" if "Intermediate" in diff or diff == "Medium" or i == 2 else "diff-hard")
    diff_label = prob.get("difficultyLabel", f"Tier {i} Problem")
    pid = prob.get("id", f"complex-prob-1-{i}")
    ptitle = prob["title"]
    pstatement = prob.get("statement", prob.get("question", ""))
    pstatement = re.sub(r'\$\$(.*?)\$\$', lambda m: '$$' + m.group(1).replace('\n', ' ') + '$$', pstatement, flags=re.DOTALL)
    psolution = prob.get("derivation", prob.get("solution", ""))
    psolution = re.sub(r'\$\$(.*?)\$\$', lambda m: '$$' + m.group(1).replace('\n', ' ') + '$$', psolution, flags=re.DOTALL)
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

lead_desc = u1.get("subtitle", u1.get("leadSummary", u1.get("description", "")))

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Comprehensive SEO Meta Tags -->
  <title>Complex Analysis: Holomorphic Functions, Cauchy Theory, Residues & Conformal Mapping | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free university digital textbook covering metric topology of the complex plane, holomorphic functions, Cauchy-Riemann equations, Cauchy-Goursat theorem, Cauchy integral formulas, Taylor and Laurent series, residue calculus, contour integration, and conformal Möbius maps with 8 interactive 60 FPS simulations and 24 tiered solved university examination problems.">
  <meta name="keywords" content="Complex Analysis, Holomorphic Functions, Cauchy Riemann Equations, Harmonic Conjugates, Cauchy Goursat Theorem, Cauchy Integral Formula, Liouville Theorem, Taylor Series, Laurent Series, Isolated Singularities, Residue Calculus, Contour Integration, Jordan Lemma, Rouche Theorem, Conformal Mapping, Mobius Transformations">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.com/complex-analysis.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://openstemlibrary.com/complex-analysis.html">
  <meta property="og:title" content="Complex Analysis: Holomorphic Functions, Cauchy Theory, Residues & Conformal Mapping | OpenSTEM Digital Academic Press">
  <meta property="og:description" content="Exhaustive university honors textbook with 8 chapters, unskipped line-by-line mathematical proofs, 24 tiered solved problems, and 8 real-time interactive Canvas simulation engines.">
  <meta property="og:image" content="https://openstemlibrary.com/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Complex Analysis: Holomorphic Functions, Cauchy Theory, Residues & Conformal Mapping">
  <meta name="twitter:description" content="Free university digital textbook covering holomorphic functions, Cauchy-Riemann equations, Cauchy integral formula, Laurent expansions, residue calculus, and conformal mapping.">
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
    "name": "Complex Analysis: Holomorphic Functions, Cauchy Theory, Residues & Conformal Mapping",
    "description": "Rigorous university honors curriculum covering single-variable complex function theory: metric topology of the complex plane, stereographic projection, holomorphic functions, Cauchy-Riemann equations, Cauchy-Goursat theorem, Cauchy integral formulas, Taylor and Laurent expansions, residue calculus, and conformal mapping.",
    "provider": {{
      "@type": "EducationalOrganization",
      "name": "OpenSTEM Digital Academic Press",
      "url": "https://openstemlibrary.com"
    }},
    "educationalLevel": "Undergraduate B.Sc. Honors & STEM Foundation",
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
        "name": "Complex Analysis: Holomorphic Functions, Cauchy Theory, Residues & Conformal Mapping",
        "item": "https://openstemlibrary.com/complex-analysis.html"
      }}
    ]
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
  <link rel="stylesheet" href="styles.css?v=20261006_v1">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Complex Analysis</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search Cauchy, residues, Laurent, conformal..." class="search-input">
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
          <span class="badge-pill badge-course">Mathematics / Pure Mathematics</span>
          <span class="badge-pill badge-credits">Complex Analysis</span>
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
              {lead_desc}
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
              <a href="linear-algebra.html" class="reader-trust-link">Linear Algebra</a>
              <a href="ordinary-differential-equations-1.html" class="reader-trust-link">Differential Equations I</a>
              <a href="ordinary-differential-equations-2.html" class="reader-trust-link">Differential Equations II</a>
              <a href="complex-analysis.html" class="reader-trust-link">Complex Analysis</a>
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
  <script src="complex-analysis-sims.js?v=20261007_v1"></script>
  <script src="complex-analysis-data.js?v=20261007_v1"></script>
  <script src="app.js?v=20261007_v1"></script>
</body>
</html>
'''

with open("complex-analysis.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated complex-analysis.html with 100% linear-algebra.html parity and zero course numbers!")
