#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_spectroscopy_html.py
Generates chemical-spectroscopy.html with exact architectural parity to OpenSTEM master digital textbooks:
- Deep SEO meta tags and Schema.org JSON-LD (strictly zero course numbers or marks)
- Pre-rendered Unit 1 sections & worked problems (semantic HTML with KaTeX math)
- Inline 60 FPS Canvas simulation mount for Unit 1
- Top navbar with breadcrumbs, reading font toggle, anti-copy notice
- Search filter for topics
- Comprehensive 51-textbook reader trust footer
- Cache buster: v=20261009_v9_chemical_spectroscopy
"""

import re
import json

def format_markdown_to_html(text):
    if not text:
        return ""
    clean = text.replace('\r\n', '\n').strip()

    # Pre-isolate display math $$...$$ and \[...\]
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
            p = re.sub(r'`(.*?)`', r'<code>\1</code>', p)
            if p:
                output.append(f"<p>{p}</p>")
            para = []

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        # Blank line
        if not s:
            flush_para()
            i += 1
            continue

        # Math display placeholder
        if s.startswith('<div class="math-display">') and s.endswith('</div>'):
            flush_para()
            output.append(s)
            i += 1
            continue

        # Headings
        if s.startswith('#### '):
            flush_para()
            h_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s[5:])
            output.append(f"<h5 class=\"content-subheading\">{h_text}</h5>")
            i += 1
            continue
        elif s.startswith('### '):
            flush_para()
            h_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s[4:])
            output.append(f"<h4 class=\"content-heading\">{h_text}</h4>")
            i += 1
            continue
        elif s.startswith('## '):
            flush_para()
            h_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s[3:])
            output.append(f"<h3 class=\"content-title\">{h_text}</h3>")
            i += 1
            continue

        # Horizontal rule
        if s == '---':
            flush_para()
            output.append("<hr class=\"content-divider\">")
            i += 1
            continue

        # Code block
        if s.startswith('```'):
            flush_para()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1  # skip closing ```
            code_str = "\n".join(code_lines)
            output.append(f"<pre class=\"ascii-diagram\"><code>{code_str}</code></pre>")
            continue

        # Tables
        if s.startswith('|') and s.endswith('|'):
            flush_para()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|') and lines[i].strip().endswith('|'):
                table_lines.append(lines[i].strip())
                i += 1

            if len(table_lines) >= 2:
                th_cells = [c.strip() for c in table_lines[0].split('|')[1:-1]]
                table_html = ["<div class=\"table-responsive\"><table class=\"data-table\"><thead><tr>"]
                for c in th_cells:
                    c_clean = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', c)
                    table_html.append(f"<th>{c_clean}</th>")
                table_html.append("</tr></thead><tbody>")

                for row in table_lines[2:]:
                    td_cells = [c.strip() for c in row.split('|')[1:-1]]
                    table_html.append("<tr>")
                    for c in td_cells:
                        c_clean = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', c)
                        table_html.append(f"<td>{c_clean}</td>")
                    table_html.append("</tr>")
                table_html.append("</tbody></table></div>")
                output.append("".join(table_html))
            continue

        # Ordered lists
        if re.match(r'^\d+\.\s+', s):
            flush_para()
            list_items = []
            while i < len(lines) and re.match(r'^\d+\.\s+', lines[i].strip()):
                item_text = re.sub(r'^\d+\.\s+', '', lines[i].strip())
                item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
                item_text = re.sub(r'`(.*?)`', r'<code>\1</code>', item_text)
                list_items.append(f"<li>{item_text}</li>")
                i += 1
            output.append(f"<ol class=\"content-ordered-list\">{''.join(list_items)}</ol>")
            continue

        # Unordered lists
        if s.startswith('- ') or s.startswith('* '):
            flush_para()
            list_items = []
            while i < len(lines) and (lines[i].strip().startswith('- ') or lines[i].strip().startswith('* ')):
                item_text = lines[i].strip()[2:]
                item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
                item_text = re.sub(r'`(.*?)`', r'<code>\1</code>', item_text)
                list_items.append(f"<li>{item_text}</li>")
                i += 1
            output.append(f"<ul class=\"content-unordered-list\">{''.join(list_items)}</ul>")
            continue

        # Regular paragraph line
        para.append(s)
        i += 1

    flush_para()
    return '\n\n'.join(output)


def generate_html():
    print("Reading chemical-spectroscopy-data.js for pre-rendering Unit 1...")
    with open("chemical-spectroscopy-data.js", "r", encoding="utf-8") as f:
        js_text = f.read()

    prefix = "window.COURSE_DATA = "
    idx = js_text.find(prefix)
    if idx == -1:
        raise ValueError("Could not find window.COURSE_DATA in chemical-spectroscopy-data.js")
    json_str = js_text[idx + len(prefix):].rstrip().rstrip(';')
    course_data = json.loads(json_str)
    u1 = course_data["units"][0]

    # Pre-render Unit 1 Sections
    rendered_sections = []
    for s_idx, sec in enumerate(u1["sections"], 1):
        sec_num = sec.get("secNumber", f"1.{s_idx}")
        sec_title = sec["title"]
        html_body = format_markdown_to_html(sec["content"])

        sim_mount_html = ""
        if s_idx == 1:
            # Mount Simulation 1 in section 1.1
            sim_mount_html = """
<div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
  <div class="simulation-slot" id="sim-container-sim_spec_electromagnetic_wave_fourier">
    <div style="background:#070d1e; border:1px solid #1e293b; border-radius:8px; padding:12px; margin:16px 0;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
        <div>
          <span style="font-size:0.95rem; font-weight:700; color:#38bdf8;">EM Wave Superposition & Michelson Interferogram FFT</span>
          <span style="font-size:0.8rem; color:#94a3b8; margin-left:8px;">Unit 1: Transition Moments & FT Spectrometry</span>
        </div>
        <div style="display:flex; gap:6px;">
          <button id="spec1_btn_fft" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Toggle FFT Spectrum</button>
          <button id="spec1_btn_reset" style="background:#1e293b; color:#94a3b8; border:1px solid #475569; padding:4px 10px; border-radius:4px; font-size:0.75rem; cursor:pointer;">Reset</button>
        </div>
      </div>
      <div style="position:relative; width:100%; height:340px; background:#040711; border-radius:6px; overflow:hidden;">
        <canvas id="spec1_canvas" class="sim-canvas" style="width:100%; height:100%; display:block;"></canvas>
      </div>
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:10px; background:#0b1329; padding:10px; border-radius:6px;">
        <div>
          <label style="font-size:0.75rem; color:#94a3b8; display:block;">Wave 1 Frequency ν̃₁: <span id="spec1_nu1_val" style="color:#38bdf8; font-weight:600;">1200 cm⁻¹</span></label>
          <input type="range" id="spec1_nu1" min="600" max="2400" value="1200" step="50" style="width:100%;">
        </div>
        <div>
          <label style="font-size:0.75rem; color:#94a3b8; display:block;">Wave 2 Frequency ν̃₂: <span id="spec1_nu2_val" style="color:#f472b6; font-weight:600;">1600 cm⁻¹</span></label>
          <input type="range" id="spec1_nu2" min="600" max="2400" value="1600" step="50" style="width:100%;">
        </div>
        <div>
          <label style="font-size:0.75rem; color:#94a3b8; display:block;">Interferometer Velocity: <span id="spec1_v_val" style="color:#34d399; font-weight:600;">1.0 mm/s</span></label>
          <input type="range" id="spec1_v" min="0.2" max="3.0" value="1.0" step="0.2" style="width:100%;">
        </div>
      </div>
    </div>
  </div>
</div>
"""

        rendered_sections.append(f"""<section class="textbook-section-card" id="u1-sec{s_idx}">
  <header class="sec-header">
    <h3 class="sec-title"><span class="sec-num">{sec_num}</span><span>{sec_title}</span></h3>
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
        tier = prob.get("difficultyLabel", prob.get("difficulty", "Honors Problem"))
        diff_class = "diff-easy" if "Easy" in tier or "Foundational" in tier or "Fundamentals" in tier else ("diff-medium" if "Intermediate" in tier or "Advanced" in tier or "Medium" in tier else "diff-hard")
        title = prob["title"]
        stmt_html = format_markdown_to_html(prob.get("statement", prob.get("question", "")))
        sol_html = format_markdown_to_html(prob.get("solution", ""))

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
  <title>Chemical Spectroscopy: EM Radiation Interaction, Rotational Microwave, Rovibrational & Raman, Atomic & Molecular Electronic Transitions, Multi-Dimensional NMR, ESR & Mössbauer | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free comprehensive university honors digital textbook on Chemical Spectroscopy: electromagnetic radiation-matter interaction, transition dipole moments, Einstein A and B coefficients, Doppler broadening, FTIR interferograms, pure rotational microwave spectra of linear and symmetric rotors, centrifugal distortion, Stark effect, rovibrational P/Q/R branches, anharmonic Morse potential, Dunham expansion, Raman polarizability ellipsoids, Kramers-Heisenberg-Dirac dispersion, atomic term symbols, Hund rules, Zeeman and Paschen-Back splitting, molecular Franck-Condon vibronic progressions, Jablonski diagrams, fluorescence quenching, FRET, 1D/2D NMR Bloch equations, chemical shifts, scalar J-coupling, COSY, TOCSY, HSQC, HMBC, solid-state MAS NMR, electron spin resonance (ESR/EPR) hyperfine interactions, and Fe-57 Mössbauer spectroscopy. Features 10 interactive 60 FPS Canvas simulations and 90 tiered solved problems with complete step-by-step mathematical and quantum derivations.">
  <meta name="keywords" content="Chemical Spectroscopy, Spectroscopy Textbook, Electromagnetic Radiation Interaction, Einstein Coefficients, Transition Dipole Moment, Doppler Broadening, FTIR Spectroscopy, Fellgett Advantage, Jacquinot Advantage, Microwave Spectroscopy, Rigid Rotor, Centrifugal Distortion, Stark Effect, Rovibrational Spectroscopy, P Branch, R Branch, Morse Potential, Dunham Expansion, Raman Spectroscopy, Polarizability Ellipsoid, Depolarization Ratio, Resonance Raman, SERS, TERS, Atomic Term Symbols, Russell-Saunders Coupling, Landé g-factor, Zeeman Effect, Sodium D Lines, Franck-Condon Principle, Vibronic Transitions, Tanabe-Sugano Diagrams, Photophysics, Jablonski Diagram, Fluorescence Lifetime, Stern-Volmer Quenching, FRET, NMR Spectroscopy, Larmor Precession, Bloch Equations, Chemical Shift, Scalar Coupling, Dynamic NMR, 2D NMR, COSY, HSQC, HMBC, Solid-State MAS NMR, ESR Spectroscopy, Hyperfine Coupling, Mössbauer Spectroscopy, Isomer Shift, Quadrupole Splitting">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.com/chemical-spectroscopy.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Chemical Spectroscopy: EM Radiation Interaction, Rotational Microwave, Rovibrational & Raman, Atomic & Molecular Electronic Transitions, Multi-Dimensional NMR, ESR & Mössbauer | OpenSTEM Digital Academic Press">
  <meta property="og:description" content="Exhaustive university honors chemical spectroscopy digital textbook with 10 comprehensive units, 80 sections, 90 tiered solved problems, and 10 real-time interactive Canvas simulation engines.">
  <meta property="og:image" content="https://openstemlibrary.com/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD (Strictly Zero Course Numbers) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Chemical Spectroscopy: EM Radiation Interaction, Rotational Microwave, Rovibrational & Raman, Atomic & Molecular Electronic Transitions, Multi-Dimensional NMR, ESR & Mössbauer",
    "description": "Comprehensive university honors curriculum covering radiation-matter interactions, microwave rotational spectra, rovibrational IR, Raman scattering, atomic and molecular electronic spectroscopy, photophysical luminescence, 1D and 2D NMR, ESR, and Mössbauer spectroscopy.",
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
  <link rel="stylesheet" href="styles.css?v=20261009_v9_chemical_spectroscopy">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Chemical Spectroscopy</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search Einstein A/B, rigid rotor, Stark effect, P/R branch, Raman, term symbols, Franck-Condon, FRET, Bloch, COSY, ESR..." class="search-input">
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
          <span class="badge-pill badge-credits">Molecular Structure, Transitions & Quantum Spectroscopy</span>
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
            <h1 class="unit-title-heading" id="unit-title">Unit 1: Interaction of Electromagnetic Radiation with Matter & Practical Foundations</h1>
            <p class="unit-desc-lead" id="unit-desc">
              Comprehensive quantum electrodynamic and semiclassical treatment of electromagnetic radiation interacting with atomic and molecular systems: quantization of radiation fields, transition dipole moments, Einstein A and B coefficients, spectral transitions across all EM regions, natural vs Doppler vs collisional line broadening, and Fourier Transform instrumentation SNR limits.
            </p>
          </header>

          <!-- Pre-Rendered Sections for Indexing & Instant Load -->
          <div id="textbook-sections">
{all_sections_html}
          </div>

          <!-- Pre-Rendered Worked Problems for Indexing & Instant Load -->
          <section class="solved-problems-container" id="unit-problems-section">
            <div class="problems-header">
              <h3 class="problems-title">Solved Honors Problems & Derivations</h3>
              <p class="problems-subtitle">Step-by-step rigorous solutions with full quantum mechanical, thermodynamic, and spectral assignment validation.</p>
            </div>
            <div id="unit-problems-list">
{all_problems_html}
            </div>
          </section>

          <!-- Master Academic Trust Footer -->
          <footer class="reader-trust-footer">
            <div class="reader-trust-brand">
              <img src="logo.svg" alt="OpenSTEM Academic Press" width="32" height="32">
              <div class="reader-trust-title">OpenSTEM Global Academic Press</div>
            </div>
            <p class="reader-trust-desc">
              OpenSTEM is an open-access digital publishing initiative delivering world-class, peer-reviewed undergraduate and graduate-level textbooks across mathematics, theoretical physics, physical chemistry, organic chemistry, inorganic chemistry, analytical chemistry, nuclear sciences, chemical spectroscopy, and industrial process engineering.
            </p>
            <div class="reader-trust-links">
              <a href="index.html" class="reader-trust-link">Home Library</a>
              <a href="classical-mechanics.html" class="reader-trust-link">Classical Mechanics</a>
              <a href="electrodynamics.html" class="reader-trust-link">Electrodynamics</a>
              <a href="quantum-mechanics-1.html" class="reader-trust-link">Quantum Mechanics I</a>
              <a href="thermal-physics.html" class="reader-trust-link">Thermal Physics</a>
              <a href="statistical-mechanics.html" class="reader-trust-link">Statistical Mechanics</a>
              <a href="special-relativity.html" class="reader-trust-link">Special Relativity</a>
              <a href="general-relativity.html" class="reader-trust-link">General Relativity</a>
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
              <a href="chemical-spectroscopy.html" class="reader-trust-link" style="color: #38bdf8; font-weight: 600;">Chemical Spectroscopy</a>
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
  <script src="departments-data.js?v=20261009_v9_chemical_spectroscopy"></script>
  <script src="chemical-spectroscopy-sims.js?v=20261009_v9_chemical_spectroscopy"></script>
  <script src="chemical-spectroscopy-data.js?v=20261009_v9_chemical_spectroscopy"></script>
  <script src="app.js?v=20261009_v9_chemical_spectroscopy"></script>
</body>
</html>
"""

    # Check for strictly zero course numbers
    forbidden_patterns = [
        r'\bchem\s*\d+',
        r'35\s*\+\s*10\s*\+\s*5',
        r'70\s*\+\s*20\s*\+\s*10',
        r'\b\d+\s*Marks\b',
        r'100\s*Marks',
        r'70\s*Marks',
        r'50\s*Marks',
        r'exam(ination)?\s+marks',
        r'\bgrades?\s*=\s*\d+'
    ]
    for pattern in forbidden_patterns:
        matches = re.findall(pattern, html_content, re.IGNORECASE)
        if matches:
            raise ValueError(f"STRICT ERROR: Prohibited course codes or marks detected in HTML: {matches}")

    output_file = "chemical-spectroscopy.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✓ Successfully generated {output_file} with pre-rendered Unit 1 ({len(html_content)} bytes)")
    print("✓ Banned token audit on HTML passed cleanly.")

if __name__ == "__main__":
    generate_html()
