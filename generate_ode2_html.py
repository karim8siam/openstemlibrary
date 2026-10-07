#!/usr/bin/env python3
"""
generate_ode2_html.py
Generates ordinary-differential-equations-2.html with complete SEO metadata,
Schema.org JSON-LD, pre-rendered Chapter 1 content, KaTeX rendering, and universal trust footer.
"""

import json

def generate_html():
    with open('ordinary-differential-equations-2-data.js', 'r', encoding='utf-8') as f:
        data_text = f.read()

    # Parse course data
    prefix = 'window.COURSE_DATA = '
    start_idx = data_text.find(prefix) + len(prefix)
    end_idx = data_text.find(';\nwindow.BOOK_DATA')
    course_json = data_text[start_idx:end_idx]
    course_data = json.loads(course_json)

    unit1 = course_data['units'][0]

    # Pre-render sections
    prerendered_sections_html = ""
    for idx, sec in enumerate(unit1['sections']):
        sec_num = sec['secNumber']
        sec_title = sec['title']
        sec_content = sec['content']
        sim_code = ""
        if 'simulation' in sec:
            sim_type = sec['simulation']
            sim_code = f"""
            <div class="simulation-wrapper" style="margin: 2rem 0;">
              <div class="sim-header" style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.75rem;">
                <span style="font-weight:700; color:#38bdf8; font-size:0.95rem; display:flex; align-items:center; gap:0.5rem;">
                  <span>⚡</span> Interactive Numerical Simulation: 2D Autonomous Phase Plane Explorer
                </span>
                <span class="sim-status" style="font-size:0.75rem; background:rgba(56,189,248,0.15); color:#38bdf8; padding:2px 8px; border-radius:4px; font-weight:600;">60 FPS Active</span>
              </div>
              <div id="sim-{sim_type}" class="sim-mount-point" data-sim="{sim_type}" style="min-height:380px;"></div>
            </div>
            """

        prerendered_sections_html += f"""
        <section class="textbook-section-card" id="sec-{sec_num.replace('.', '-')}">
          <div class="section-badge-row">
            <span class="section-counter">Section {sec_num}</span>
            <span class="reading-time">14 min read</span>
          </div>
          <h2 class="section-heading">{sec_title}</h2>
          <div class="section-body">
            {sec_content}
            {sim_code}
          </div>
        </section>
        """

    # Pre-render problems for Chapter 1
    unit1_problems = [p for p in course_data['problems'] if p['id'] in ['prob-01', 'prob-09', 'prob-17']]
    problems_html = ""
    for prob in unit1_problems:
        tier_class = f"tier-{prob['tier']}"
        problems_html += f"""
        <div class="problem-card {tier_class}" id="{prob['id']}">
          <div class="problem-meta">
            <span class="tier-pill">{prob['difficultyLabel']}</span>
            <span class="problem-number">{prob['id'].upper()}</span>
          </div>
          <h3 class="problem-title">{prob['title']}</h3>
          <div class="problem-statement">{prob['statement']}</div>
          <details class="solution-accordion">
            <summary class="solution-toggle">
              <span class="toggle-icon">▶</span>
              <span>View Step-by-Step Derivation & Verification</span>
            </summary>
            <div class="solution-content">
              {prob['solution']}
              <div class="solution-answer">
                <strong>Final Result:</strong> {prob['answer']}
              </div>
            </div>
          </details>
        </div>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ordinary Differential Equations II: First-Order Systems, Series Solutions & Sturm-Liouville Theory | OpenSTEM Digital Academic Press</title>
  
  <!-- Primary SEO Metadata -->
  <meta name="description" content="Comprehensive university honors textbook covering first-order linear systems, phase portraits, matrix exponential Putzer algorithm, Frobenius series solutions, Legendre polynomials, Bessel functions, Sturm-Liouville theory, and Green's functions with 8 interactive 60 FPS simulations and 24 tiered solved university examination problems.">
  <meta name="keywords" content="Ordinary Differential Equations II, Systems of Differential Equations, Phase Portrait, Matrix Exponential, Putzer Algorithm, Frobenius Method, Legendre Polynomials, Bessel Functions, Laguerre Polynomials, Hermite Polynomials, Sturm-Liouville Theory, Green's Functions, Fredholm Alternative">
  <meta name="author" content="OpenSTEM Global Academic Press">
  <link rel="canonical" href="https://openstemlibrary.com/ordinary-differential-equations-2.html">

  <!-- Open Graph / Social Meta -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="OpenSTEM Digital Academic Press">
  <meta property="og:title" content="Ordinary Differential Equations II: First-Order Systems, Series Solutions & Sturm-Liouville Theory">
  <meta property="og:description" content="Comprehensive university honors textbook covering first-order linear systems, matrix exponential, Frobenius method, Legendre and Bessel functions, Sturm-Liouville eigenvalue theory, and Green's functions with 8 interactive simulations.">
  <meta property="og:url" content="https://openstemlibrary.com/ordinary-differential-equations-2.html">
  <meta property="og:image" content="https://openstemlibrary.com/logo.svg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Ordinary Differential Equations II: Honors Digital Textbook">
  <meta name="twitter:description" content="Free university-standard digital textbook with complete proofs, 8 real-time simulations, and 24 solved examination problems.">
  <meta name="twitter:image" content="https://openstemlibrary.com/logo.svg">

  <!-- Favicon Suite -->
  <link rel="icon" href="favicon.ico" sizes="48x48">
  <link rel="icon" href="favicon-48x48.png" type="image/png" sizes="48x48">
  <link rel="apple-touch-icon" href="apple-touch-icon.png" sizes="180x180">
  <link rel="icon" href="logo.svg" type="image/svg+xml">

  <!-- Structured Data: JSON-LD Course and TechArticle -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Course",
        "name": "Ordinary Differential Equations II",
        "courseCode": "MTH 3104",
        "description": "Comprehensive university honors textbook covering first-order linear systems, phase portraits, matrix exponential Putzer algorithm, Frobenius series solutions, Legendre polynomials, Bessel functions, Sturm-Liouville theory, and Green's functions.",
        "provider": {{
          "@type": "Organization",
          "name": "OpenSTEM Global Academic Press",
          "sameAs": "https://openstemlibrary.com"
        }},
        "educationalLevel": "B.Sc. (Honours) / Upper-Division Undergraduate",
        "isAccessibleForFree": true,
        "hasCourseInstance": {{
          "@type": "CourseInstance",
          "courseMode": "Online",
          "courseWorkload": "45 lecture hours + 9 hours individual guidance"
        }}
      }},
      {{
        "@type": "TechArticle",
        "headline": "Ordinary Differential Equations II: First-Order Systems, Series Solutions & Sturm-Liouville Theory",
        "url": "https://openstemlibrary.com/ordinary-differential-equations-2.html",
        "inLanguage": "en-US",
        "publisher": {{
          "@type": "Organization",
          "name": "OpenSTEM Global Academic Press",
          "logo": {{
            "@type": "ImageObject",
            "url": "https://openstemlibrary.com/logo.svg"
          }}
        }},
        "about": [
          "Systems of Linear First-Order ODEs",
          "Phase Plane Analysis",
          "Matrix Exponential and Putzer Algorithm",
          "Frobenius Method",
          "Legendre Polynomials",
          "Bessel Functions",
          "Sturm-Liouville Boundary Value Problems",
          "Green's Functions"
        ]
      }},
      {{
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
            "name": "Mathematics Department",
            "item": "https://openstemlibrary.com/#departments-container"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "Ordinary Differential Equations II (MTH 3104)",
            "item": "https://openstemlibrary.com/ordinary-differential-equations-2.html"
          }}
        ]
      }}
    ]
  }}
  </script>

  <!-- Typography & Preconnect -->
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
          <div class="brand-text">
            <span class="brand-title">OpenSTEM</span>
            <span class="brand-subtitle">Academic Press</span>
          </div>
        </a>
      </div>

      <div class="course-meta-badge">
        <span class="course-code">MTH 3104</span>
        <span class="course-level">Compulsory Honors</span>
      </div>

      <nav class="unit-nav" aria-label="Table of Contents">
        <h3 class="nav-section-title">COURSE MODULES</h3>
        <ol class="unit-nav-list" id="unit-nav-list">
          <!-- Populated dynamically by app.js from COURSE_DATA -->
          <li class="unit-nav-item active" data-unit-index="0">
            <span class="unit-nav-num">Ch.1</span>
            <span class="unit-nav-text">Systems of Linear First-Order ODEs: Foundations & Phase Portraits</span>
          </li>
          <li class="unit-nav-item" data-unit-index="1">
            <span class="unit-nav-num">Ch.2</span>
            <span class="unit-nav-text">Homogeneous Matrix Systems & Generalized Eigenvectors</span>
          </li>
          <li class="unit-nav-item" data-unit-index="2">
            <span class="unit-nav-num">Ch.3</span>
            <span class="unit-nav-text">The Fundamental Matrix, Matrix Exponential & Nonhomogeneous Systems</span>
          </li>
          <li class="unit-nav-item" data-unit-index="3">
            <span class="unit-nav-num">Ch.4</span>
            <span class="unit-nav-text">Series Solutions Near Ordinary Points & Legendre Differential Equation</span>
          </li>
          <li class="unit-nav-item" data-unit-index="4">
            <span class="unit-nav-num">Ch.5</span>
            <span class="unit-nav-text">Regular Singular Points & The Method of Frobenius</span>
          </li>
          <li class="unit-nav-item" data-unit-index="5">
            <span class="unit-nav-num">Ch.6</span>
            <span class="unit-nav-text">Bessel Functions & Classical Orthogonal Systems</span>
          </li>
          <li class="unit-nav-item" data-unit-index="6">
            <span class="unit-nav-num">Ch.7</span>
            <span class="unit-nav-text">Sturm-Liouville Theory, Self-Adjoint Operators & Oscillation Theorems</span>
          </li>
          <li class="unit-nav-item" data-unit-index="7">
            <span class="unit-nav-num">Ch.8</span>
            <span class="unit-nav-text">Nonhomogeneous BVPs, The Fredholm Alternative & Green's Functions</span>
          </li>
        </ol>
      </nav>

      <div class="sidebar-footer">
        <a href="ordinary-differential-equations-1.html" class="catalog-back-btn" style="margin-bottom:0.5rem; color:#38bdf8;">
          <span>←</span> Previous: ODE I (MTH 2103)
        </a>
        <a href="index.html#departments-container" class="catalog-back-btn">
          <span>📚</span> Full Academic Catalog
        </a>
      </div>
    </aside>

    <!-- Main Content Reader -->
    <main class="content-area" id="main-content">
      
      <!-- Sticky Navigation Header -->
      <header class="reader-header">
        <button class="sidebar-toggle-btn" id="sidebar-toggle" aria-label="Toggle Sidebar">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>

        <div class="course-header-info">
          <span class="course-parent-tag">Mathematics • B.Sc. (Honours) Level</span>
          <h1 class="course-main-title">Ordinary Differential Equations II</h1>
        </div>

        <div class="reader-actions">
          <button class="font-toggle-btn" id="font-toggle" title="Toggle Serif / Sans Font">Aa</button>
        </div>
      </header>

      <!-- Textbook Content Container -->
      <div class="content-scroll-container">
        <article class="textbook-unit-article">

          <!-- Chapter Banner Header -->
          <header class="unit-banner">
            <div class="unit-tag" id="unit-tag">Chapter 1 • Theory & Derivations</div>
            <h1 class="unit-title" id="unit-title">{unit1['title']}</h1>
            <p class="unit-desc" id="unit-desc">{unit1['leadSummary']}</p>
          </header>

          <!-- Pre-rendered Chapter 1 Sections for Immediate SEO Indexing -->
          <div id="textbook-sections">
            {prerendered_sections_html}
          </div>

          <!-- Solved Examination Problems Container -->
          <section class="solved-problems-section" id="solved-problems-container" style="margin-top: 3.5rem;">
            <div class="problems-header">
              <span class="section-badge">Examination Practice</span>
              <h2 class="problems-heading">University Solved Examination Problems</h2>
              <p class="problems-sub">Comprehensive multi-tiered examination problems solved with unskipped step-by-step mathematical proofs.</p>
            </div>
            <div id="problems-list">
              {problems_html}
            </div>
          </section>

          <!-- Universal Academic Trust Footer -->
          <footer class="reader-trust-footer" style="margin-top: 5rem; padding: 2.5rem 1.5rem; border-top: 1px solid rgba(148, 163, 184, 0.15); text-align: center;">
            <div class="reader-trust-links" style="display: flex; justify-content: center; flex-wrap: wrap; gap: 1.25rem; margin-bottom: 1rem; font-size: 0.85rem;">
              <a href="index.html" class="reader-trust-link">Academic Catalog</a>
              <a href="index.html#faq-section" class="reader-trust-link">FAQ & Student Guide</a>
              <a href="about.html" class="reader-trust-link">About & Editorial Standards</a>
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
  <script src="ordinary-differential-equations-2-sims.js?v=20261007_v1"></script>
  <script src="ordinary-differential-equations-2-data.js?v=20261007_v1"></script>
  <script src="app.js?v=20261007_v1"></script>
</body>
</html>
"""

    with open('ordinary-differential-equations-2.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    print('Generated ordinary-differential-equations-2.html successfully!')

if __name__ == '__main__':
    generate_html()
