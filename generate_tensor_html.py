# -*- coding: utf-8 -*-
"""
generate_tensor_html.py
Generates tensor-analysis.html with exact layout parity to discrete-mathematics.html,
partial-differential-equations.html, topology.html, number-theory.html, real-analysis.html, etc.
Deep SEO meta tags, Schema.org JSON-LD (strictly zero course numbers),
pre-rendered Unit 1 sections & worked problems (fully formatted semantic HTML with callout blockquotes),
interactive Canvas simulations mount, font toggle, live topic search, and comprehensive trust footer.
"""

import re
import build_tensor_unit1

def format_markdown_to_html(text):
    if not text:
        return ""
    clean = text.replace('\r\n', '\n').strip()

    # Pre-isolate display math $$...$$
    def isolate_math(match):
        single = match.group(1).strip().replace('\n', ' ')
        return f"\n\n<div class=\"math-display\">$${single}$$</div>\n\n"
    clean = re.sub(r'\$\$(.*?)\$\$', isolate_math, clean, flags=re.DOTALL)

    lines = clean.split('\n')
    output = []
    i = 0
    para = []

    def flush_para():
        nonlocal para
        if para:
            p = ' '.join(para).strip()
            p = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', p)
            p = re.sub(r'\*(.*?)\*', r'<em>\1</em>', p)
            if p:
                output.append(f"<p>{p}</p>")
            para = []

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            flush_para()
            i += 1
            continue

        # Horizontal rule
        if s == '---' or s == '***':
            flush_para()
            output.append('<hr class="section-divider-hr">')
            i += 1
            continue

        # Pre-wrapped display math or div
        if s.startswith('<div') or (s.startswith('$$') and s.endswith('$$')):
            flush_para()
            output.append(s if s.startswith('<div') else f'<div class="math-display">{s}</div>')
            i += 1
            continue

        # Blockquote (group all consecutive lines starting with >)
        if s.startswith('>'):
            flush_para()
            bq_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                b_raw = lines[i].strip()
                b_content = b_raw[1:].strip()
                bq_lines.append(b_content)
                i += 1

            bq_out = []
            bq_p = []

            def flush_bq_p():
                nonlocal bq_p
                if bq_p:
                    bp = ' '.join(bq_p).strip()
                    bp = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', bp)
                    bp = re.sub(r'\*(.*?)\*', r'<em>\1</em>', bp)
                    if bp:
                        bq_out.append(f"<p>{bp}</p>")
                    bq_p = []

            for b_line in bq_lines:
                bl_strip = b_line.strip()
                if not bl_strip:
                    flush_bq_p()
                elif bl_strip.startswith('$$') and bl_strip.endswith('$$'):
                    flush_bq_p()
                    bq_out.append(f'<div class="math-display">{bl_strip}</div>')
                elif bl_strip.startswith('<div'):
                    flush_bq_p()
                    bq_out.append(bl_strip)
                elif re.match(r'^\d+\.\s', bl_strip):
                    flush_bq_p()
                    item_text = re.sub(r'^\d+\.\s*', '', bl_strip)
                    item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
                    item_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item_text)
                    bq_out.append(f'<p style="margin-left: 1.2rem; margin-bottom: 0.35rem;">• {item_text}</p>')
                elif bl_strip.startswith('- ') or bl_strip.startswith('* '):
                    flush_bq_p()
                    item_text = bl_strip[2:].strip()
                    item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
                    item_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item_text)
                    bq_out.append(f'<p style="margin-left: 1.2rem; margin-bottom: 0.35rem;">• {item_text}</p>')
                else:
                    bq_p.append(b_line)
            flush_bq_p()

            output.append(f'<blockquote class="math-callout">\n' + '\n'.join(bq_out) + '\n</blockquote>')
            continue

        # Headings
        if s.startswith('### '):
            flush_para()
            h_text = s[4:].strip()
            output.append(f"<h4>{h_text}</h4>")
            i += 1
            continue
        if s.startswith('#### '):
            flush_para()
            h_text = s[5:].strip()
            output.append(f"<h5 style=\"color: #38bdf8; font-weight: 600; margin-top: 1rem;\">{h_text}</h5>")
            i += 1
            continue

        # Lists (numbered or bullet)
        if re.match(r'^\d+\.\s', s) or s.startswith('- ') or s.startswith('* '):
            flush_para()
            is_num = bool(re.match(r'^\d+\.\s', s))
            tag = "ol" if is_num else "ul"
            items = []
            while i < len(lines):
                cur = lines[i].strip()
                if (is_num and re.match(r'^\d+\.\s', cur)) or (not is_num and (cur.startswith('- ') or cur.startswith('* '))):
                    it_txt = re.sub(r'^\d+\.\s*', '', cur) if is_num else cur[2:].strip()
                    it_txt = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', it_txt)
                    it_txt = re.sub(r'\*(.*?)\*', r'<em>\1</em>', it_txt)
                    items.append(f"<li>{it_txt}</li>")
                    i += 1
                elif cur.startswith('$$') and cur.endswith('$$'):
                    items.append(f'<div class="math-display">{cur}</div>')
                    i += 1
                elif cur == '':
                    i += 1
                    break
                else:
                    break
            output.append(f"<{tag} class=\"content-list\">\n" + "\n".join(items) + f"\n</{tag}>")
            continue

        # Regular text line accumulates into paragraph
        para.append(line.strip())
        i += 1

    flush_para()
    return '\n\n'.join(output)


def generate_html():
    u1 = build_tensor_unit1.get_unit1()

    # Pre-render Unit 1 Sections
    rendered_sections = []
    for s_idx, sec in enumerate(u1["sections"], 1):
        sec_num = sec["secNumber"]
        sec_title = sec["title"]
        html_body = format_markdown_to_html(sec["content"])

        sim_mount_html = ""
        if s_idx == 5:
            # Mount Simulation 1 in section 1.5
            sim_mount_html = f"""
<div class="simulation-card" style="margin: 1.5rem 0;">
  <div class="sim-header">
    <div class="sim-title">2D Curvilinear Coordinate Transformations & Basis Vectors Engine</div>
    <div class="sim-badge">60 FPS Real-Time Canvas Engine</div>
  </div>
  <div class="canvas-wrapper">
    <canvas id="sim-u1-canvas" width="800" height="420" class="sim-canvas"></canvas>
  </div>
  <div class="sim-controls" id="sim-u1-controls" style="display:flex; flex-wrap:wrap; gap:0.5rem; align-items:center; padding: 0.75rem 1rem; background: #0b1120; border-top: 1px solid #1e293b;">
    <!-- Controls populated dynamically by sim_tensor_coord_transform -->
  </div>
  <div class="sim-desc" style="padding: 0.75rem 1rem; color: #94a3b8; font-size: 0.85rem; line-height: 1.4; border-top: 1px solid rgba(255,255,255,0.05);">
    Interact with curvilinear coordinate transformations across Cartesian, Polar, Elliptic, and Hyperbolic coordinate systems. Drag points to dynamically observe the contravariant tangent basis vectors $\mathbf{{e}}_i = \frac{{\partial \mathbf{{r}}}}{{\partial x^i}}$ and covariant normal dual covector basis $\mathbf{{e}}^i = \nabla x^i$ with live metric component calculations.
  </div>
</div>
"""

        rendered_sections.append(f"""<section class="textbook-section-card" id="u1-sec{s_idx}">
  <header class="sec-header">
    <h3 class="sec-title"><span class="sec-num">§{sec_num}</span><span>{sec_title}</span></h3>
  </header>
  <div class="sec-content">
{html_body}
{sim_mount_html}
  </div>
</section>""")

    all_sections_html = "\n\n".join(rendered_sections)

    # Pre-render Unit 1 Solved Problems
    rendered_problems = []
    for p_idx, prob in enumerate(u1["problems"], 1):
        tier = prob["tier"]
        diff_class = "diff-easy" if "Foundational" in tier or "Fundamentals" in tier else ("diff-medium" if "Advanced" in tier or "Computational" in tier else "diff-hard")
        title = prob["title"]
        stmt_html = format_markdown_to_html(prob["statement"])
        sol_html = format_markdown_to_html(prob["solution"])

        rendered_problems.append(f"""<div class="problem-card" id="prob-u1-p{p_idx}">
  <div class="problem-header">
    <div class="prob-title-row">
      <span class="diff-badge {diff_class}">{tier}</span>
      <h4 class="prob-title">Problem 1.{p_idx}: {title}</h4>
    </div>
  </div>
  <div class="problem-body">
    <div class="problem-statement">
      {stmt_html}
    </div>
    <div class="solution-wrapper">
      <button class="solution-toggle-btn" aria-expanded="false" onclick="toggleSolution('sol-u1-p{p_idx}', this)">
        <span class="toggle-icon">▸</span>
        <span class="toggle-text">Show Complete Step-by-Step Derivation & Verification</span>
      </button>
      <div class="solution-content" id="sol-u1-p{p_idx}" style="display: none;">
        {sol_html}
      </div>
    </div>
  </div>
</div>""")

    all_problems_html = "\n\n".join(rendered_problems)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Comprehensive SEO Meta Tags -->
  <title>Tensor Analysis: Differential Invariants, Riemannian Metrics, Covariant Differentiation & Curvature Tensors | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free comprehensive university honors digital textbook on tensor analysis: Einstein summation convention, generalized Kronecker delta, Levi-Civita permutation pseudo-tensors, contravariant and covariant vectors, tensor algebra and quotient law, Riemannian and pseudo-Riemannian metrics, Christoffel symbols, geodesics, covariant differentiation, Ricci's theorem, differential invariants, Riemann and Ricci curvature tensors, Bianchi identities, sectional curvature, Schur's theorem, Riemannian flatness, Weyl conformal tensor, hypersurfaces and Gauss-Codazzi equations, continuum stress, covariant electrodynamics, and Einstein field equations with the Schwarzschild metric. Features 8 interactive 60 FPS Canvas simulations and 24 tiered solved problems with complete line-by-line mathematical proofs.">
  <meta name="keywords" content="Tensor Analysis, Tensor Calculus, Riemannian Geometry, Differential Geometry, Einstein Summation Convention, Kronecker Delta, Levi-Civita Permutation Symbol, Contravariant Vectors, Covariant Vectors, Tensor Algebra, Quotient Law, Metric Tensor, Reciprocal Metric, Christoffel Symbols, Levi-Civita Connection, Geodesics, Geodesic Deviation, Covariant Differentiation, Ricci Theorem, Differential Invariants, Laplace-Beltrami Operator, Parallel Transport, Holonomy, Riemann Curvature Tensor, Ricci Tensor, Scalar Curvature, Einstein Tensor, Bianchi Identities, Sectional Curvature, Schur Theorem, Conformal Curvature, Weyl Tensor, Cotton Tensor, Hypersurface Geometry, First Fundamental Form, Second Fundamental Form, Shape Operator, Gauss Theorema Egregium, Codazzi-Mainardi Equations, Stress-Energy Tensor, Covariant Maxwell Electrodynamics, Einstein Field Equations, Schwarzschild Metric, Perihelion Precession">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.com/tensor-analysis.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Tensor Analysis: Differential Invariants, Riemannian Metrics, Covariant Differentiation & Curvature Tensors | OpenSTEM Digital Academic Press">
  <meta property="og:description" content="Exhaustive university honors textbook with 8 units, unskipped line-by-line mathematical proofs, 24 tiered solved problems, and 8 real-time interactive Canvas simulation engines.">
  <meta property="og:image" content="https://openstemlibrary.com/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD (Strictly Zero Course Numbers) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Tensor Analysis: Differential Invariants, Riemannian Metrics, Covariant Differentiation & Curvature Tensors",
    "description": "Comprehensive university honors curriculum covering index notation, tensor algebra, Riemannian metrics, Christoffel symbols, geodesics, covariant differentiation, Ricci's theorem, curvature tensors, Bianchi identities, hypersurface geometry, conformal curvature, continuum mechanics, relativistic electrodynamics, and Einstein field equations.",
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
  <link rel="stylesheet" href="styles.css?v=20261008_v9">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Tensor Analysis</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search indices, metrics, Christoffel, covariant derivatives, curvature, Bianchi, Einstein..." class="search-input">
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
          <span class="badge-pill badge-course">Mathematics / Tensor Analysis</span>
          <span class="badge-pill badge-credits">Differential Invariants & Curvature Tensors</span>
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
            <h1 class="unit-title-heading" id="unit-title">Coordinates, Index Notation, Summation Convention & Affine Spaces</h1>
            <p class="unit-desc-lead" id="unit-desc">
              Foundations of tensor calculus: $n$-dimensional Euclidean and affine spaces, Einstein summation convention, dummy and free index discipline, the generalized Kronecker delta $\delta^i_j$, Levi-Civita permutation pseudo-tensors $\epsilon_{{ijk}}$ and $\epsilon^{{ijk}}$, coordinate transformations, and transformation laws for contravariant vectors $A^i$ and covariant vectors $B_i$.
            </p>
          </header>

          <!-- Pre-Rendered Sections for Indexing & Instant Load -->
          <div id="textbook-sections">
{all_sections_html}
          </div>

          <!-- Pre-Rendered Tiered Solved Examination Problems -->
          <div class="unit-problems-section" id="unit-problems">
            <div class="problems-header">
              <h2 class="problems-main-title">Rigorous Tiered Solved Examination Problems</h2>
              <p class="problems-subtitle">Step-by-step unskipped derivations, complete proofs, and verification across Foundational, Advanced, and Honors tiers.</p>
            </div>
            <div id="problems-container">
{all_problems_html}
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
              <a href="numerical-analysis.html" class="reader-trust-link">Numerical Analysis</a>
              <a href="abstract-algebra.html" class="reader-trust-link">Abstract Algebra</a>
              <a href="graph-theory.html" class="reader-trust-link">Graph Theory</a>
              <a href="real-analysis.html" class="reader-trust-link">Real Analysis</a>
              <a href="differential-geometry.html" class="reader-trust-link">Differential Geometry</a>
              <a href="number-theory.html" class="reader-trust-link">Theory of Numbers</a>
              <a href="topology.html" class="reader-trust-link">General Topology</a>
              <a href="partial-differential-equations.html" class="reader-trust-link">Partial Differential Equations</a>
              <a href="discrete-mathematics.html" class="reader-trust-link">Discrete Mathematics</a>
              <a href="tensor-analysis.html" class="reader-trust-link" style="color: #38bdf8; font-weight: 600;">Tensor Analysis</a>
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
  <script src="tensor-analysis-sims.js?v=20261008_v9"></script>
  <script src="tensor-analysis-data.js?v=20261008_v9"></script>
  <script src="app.js?v=20261008_v9"></script>
</body>
</html>
"""

    # Check for strictly zero course numbers
    course_code_matches = re.findall(r'MTH[\s-]*\d+|4202', html_content, re.IGNORECASE)
    if course_code_matches:
        raise ValueError(f"STRICT ERROR: Prohibited course codes detected in HTML: {course_code_matches}")

    with open("tensor-analysis.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Successfully generated tensor-analysis.html with pre-rendered Unit 1 and zero course numbers.")

if __name__ == "__main__":
    generate_html()
