# -*- coding: utf-8 -*-
"""
generate_inorg1_html.py
Generates inorganic-chemistry-1.html with exact layout parity to the OpenSTEM library,
including deep SEO meta tags, Schema.org JSON-LD (strictly zero course numbers),
pre-rendered Unit 1 sections & worked problems (fully formatted semantic HTML with callout blockquotes),
interactive Canvas simulations mount, font toggle, live topic search, and comprehensive trust footer.
"""

import re
import build_inorg1_unit1

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

        # Code block (``` ... ```)
        if s.startswith('```'):
            flush_para()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            code_str = '\n'.join(code_lines).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            output.append(f'<pre class="code-block" style="background:#0b1120; border:1px solid #1e293b; border-radius:6px; padding:1rem; overflow-x:auto; font-family:var(--font-code); font-size:0.85rem; color:#e2e8f0; margin:1rem 0;"><code>{code_str}</code></pre>')
            continue

        # Table parsing
        if s.startswith('|') and s.endswith('|'):
            flush_para()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|') and lines[i].strip().endswith('|'):
                table_lines.append(lines[i].strip())
                i += 1
            
            if len(table_lines) >= 2:
                th_cells = [c.strip() for c in table_lines[0].split('|')[1:-1]]
                table_html = ['<div class="table-responsive" style="overflow-x:auto; margin: 1.25rem 0;">', '<table class="data-table" style="width:100%; border-collapse:collapse; margin:0.5rem 0;">']
                th_items = []
                for c in th_cells:
                    c_fmt = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', c)
                    th_items.append(f'<th style="border:1px solid #334155; padding:8px 12px; background:#1e293b; color:#38bdf8; text-align:left;">{c_fmt}</th>')
                table_html.append('<thead><tr>' + ''.join(th_items) + '</tr></thead>')
                table_html.append('<tbody>')
                for row_line in table_lines[2:]:
                    cells = [c.strip() for c in row_line.split('|')[1:-1]]
                    row_cells = []
                    for c in cells:
                        formatted_c = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', c)
                        formatted_c = re.sub(r'\*(.*?)\*', r'<em>\1</em>', formatted_c)
                        row_cells.append(f'<td style="border:1px solid #334155; padding:8px 12px; text-align:left;">{formatted_c}</td>')
                    table_html.append('<tr>' + ''.join(row_cells) + '</tr>')
                table_html.append('</tbody></table></div>')
                output.append('\n'.join(table_html))
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
    u1 = build_inorg1_unit1.get_unit1()

    # Pre-render Unit 1 Sections
    rendered_sections = []
    for s_idx, sec in enumerate(u1["sections"], 1):
        sec_num = sec.get("secNumber", f"1.{s_idx}")
        sec_title = sec["title"]
        html_body = format_markdown_to_html(sec["content"])

        sim_mount_html = ""
        if s_idx == 5:
            # Mount Simulation 1 in section 1.5
            sim_mount_html = """
<div class="simulation-card" style="margin: 1.5rem 0;">
  <div class="sim-header">
    <div class="sim-title">3D Atomic Orbital Visualizer & Radial Distribution Engine</div>
    <div class="sim-badge">60 FPS Real-Time Canvas Engine</div>
  </div>
  <div class="canvas-wrapper" style="position: relative; width: 100%; height: 420px; background: #080d19; border-radius: 8px; overflow: hidden;">
    <canvas id="sim-u1-canvas" width="800" height="420" class="sim-canvas" style="width: 100%; height: 100%; display: block;"></canvas>
  </div>
  <div class="sim-controls" id="sim-u1-controls" style="display:flex; flex-wrap:wrap; gap:0.5rem; align-items:center; padding: 0.75rem 1rem; background: #0b1120; border-top: 1px solid #1e293b;">
    <!-- Controls populated dynamically by sim_chem_bohr_schrodinger_orbitals -->
  </div>
  <div class="sim-desc" style="padding: 0.75rem 1rem; color: #94a3b8; font-size: 0.85rem; line-height: 1.4; border-top: 1px solid rgba(255,255,255,0.05);">
    Interact with 3D hydrogenic atomic orbitals (1s, 2s, 2p, 3s, 3p, 3d, 4f). Dynamically inspect radial wavefunctions R(r), radial probability density 4πr²R²(r), angular harmonic cross-sections, and Slater screening mechanics.
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
  <title>Inorganic Chemistry I: Atomic Structure, Periodic Trends, Chemical Bonding, Acid-Base Equilibria & Redox Systems | OpenSTEM Digital Academic Press</title>
  <meta name="description" content="Free comprehensive university honors digital textbook on Inorganic Chemistry: quantum theory of the atom, Bohr-Sommerfeld model, de Broglie matter waves, Heisenberg uncertainty, Schrödinger wave equation, radial and angular wavefunctions, quantum numbers, electron configurations, Hund's rules, Pauli exclusion principle, and Slater effective nuclear charge; periodic properties of elements, Moseley's law, atomic/ionic/covalent radii, ionization energies, electron affinities, Pauling, Mulliken, Allred-Rochow, and Allen electronegativity scales, inert pair effect, and Dirac relativistic orbital contraction; ionic bonding, Born-Haber thermochemical cycles, Madelung constants, Evjen neutral cell summation, Born-Landé and Kapustinskii equations, radius ratio packing rules, Fajan's polarization rules, crystal point defects, and superionic conductors; covalent bonding, Lewis formalisms, formal charges, Pimentel-Rundle 3c-4e hypervalency, Morse potential, bond enthalpies, percent ionic character, Natural Bond Orbital (NBO) analysis, and Wade's rules; molecular geometries, VSEPR theory, Gillespie-Nyholm axioms, Bent's rule, Coulson's theorem, group theoretical point groups, and vibrational selection rules; quantum theories of bonding, Heitler-London valence bond theory, orbital hybridization, molecular orbital theory, LCAO secular determinants, homonuclear diatomics, 2s-2p mixing, paramagnetism of O2, heteronuclear diatomics, and metal carbonyl pi-backbonding; intermolecular interactions, hydrogen bonding, Arrhenius, Brønsted-Lowry, Lewis, Lux-Flood, and Usanovich acid-base models, Pearson's HSAB principle, absolute hardness, polyprotic speciation, buffer capacity, and superacids; and inorganic reactions, precipitation equilibria, solubility products, redox equation balancing, Nernst equation, Latimer diagrams, Frost oxidation state landscapes, and Pourbaix potential-pH phase diagrams. Features 8 interactive 60 FPS Canvas simulations and 32 tiered solved problems with complete line-by-line mathematical proofs.">
  <meta name="keywords" content="Inorganic Chemistry, Atomic Structure, Bohr Model, Schrödinger Equation, Radial Distribution, Quantum Numbers, Electron Configuration, Slater Rules, Effective Nuclear Charge, Moseley Law, Periodic Trends, Atomic Radii, Ionization Energy, Electron Affinity, Pauling Electronegativity, Mulliken Electronegativity, Allred-Rochow, Relativistic Effects, Dirac Contraction, Lanthanide Contraction, Inert Pair Effect, Ionic Bonding, Born-Haber Cycle, Lattice Energy, Madelung Constant, Evjen Method, Born-Lande Equation, Kapustinskii Equation, Radius Ratio Rules, Fajans Rules, Crystal Defects, Superionic Conduction, Covalent Bonding, Lewis Structures, Hypervalency, 3c-4e Bond, Resonance, Bond Enthalpy, Dipole Moment, VSEPR Theory, Bents Rule, Coulsons Theorem, Group Theory, Point Groups, Molecular Symmetry, Valence Bond Theory, Hybridization, Molecular Orbital Theory, LCAO, Secular Determinant, Diatomic MO, Paramagnetism of Oxygen, Backbonding, Secondary Bonding, Hydrogen Bonding, Acid-Base Theories, Lux-Flood, Pearson HSAB, Chemical Hardness, Polyprotic Acids, Buffer Capacity, Superacids, Hammett Acidity, Redox Reactions, Nernst Equation, Latimer Diagram, Frost Diagram, Pourbaix Diagram, Corrosion Passivation">
  <meta name="author" content="Shahriyar Karim Siam">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://openstemlibrary.com/inorganic-chemistry-1.html">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Inorganic Chemistry I: Atomic Structure, Periodic Trends, Chemical Bonding, Acid-Base Equilibria & Redox Systems | OpenSTEM Digital Academic Press">
  <meta property="og:description" content="Exhaustive university honors inorganic chemistry textbook with 8 comprehensive units, 80,000+ words of unskipped line-by-line derivations, 32 tiered solved problems, and 8 real-time interactive Canvas simulation engines.">
  <meta property="og:image" content="https://openstemlibrary.com/logo.svg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="logo.svg">

  <!-- Schema.org Educational Course JSON-LD (Strictly Zero Course Numbers) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "Inorganic Chemistry I: Atomic Structure, Periodic Trends, Chemical Bonding, Acid-Base Equilibria & Redox Systems",
    "description": "Comprehensive university honors curriculum covering quantum theory of the atom, periodic properties and relativistic effects, ionic bonding and crystal energetics, advanced covalent bonding and hypervalency, VSEPR theory and molecular symmetry group theory, valence bond and molecular orbital frameworks, non-covalent forces and advanced acid-base equilibria, and inorganic reaction thermodynamics, Latimer, Frost, and Pourbaix diagrams.",
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
  <link rel="stylesheet" href="styles.css?v=20261008_v12">
</head>
<body>

  <div class="app-container">
    <!-- Left Navigation Sidebar -->
    <aside class="sidebar">
      <div class="brand-header">
        <img src="logo.svg" alt="OpenSTEM Logo" class="brand-logo-img" width="36" height="36">
        <div>
          <div class="brand-title">Inorganic Chemistry I</div>
          <div class="brand-subtitle">OpenSTEM Digital Textbook</div>
        </div>
      </div>

      <!-- Live Search Filter for SEO / Navigation -->
      <div class="search-box-container">
        <input type="text" id="topic-search-input" placeholder="🔍 Search orbitals, Slater, VSEPR, MO theory, HSAB, Latimer, Pourbaix..." class="search-input">
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
          <span class="badge-pill badge-course">Chemistry / Inorganic Chemistry</span>
          <span class="badge-pill badge-credits">Atomic Structure, Periodic Trends, Bonding, Acid-Base & Redox</span>
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
              <a href="tensor-analysis.html" class="reader-trust-link">Tensor Analysis</a>
              <a href="fuzzy-mathematics.html" class="reader-trust-link">Fuzzy Mathematics</a>
              <a href="physical-chemistry-1.html" class="reader-trust-link">Physical Chemistry I</a>
              <a href="inorganic-chemistry-1.html" class="reader-trust-link" style="color: #38bdf8; font-weight: 600;">Inorganic Chemistry I</a>
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
  <script src="inorganic-chemistry-1-sims.js?v=20261008_v12"></script>
  <script src="inorganic-chemistry-1-data.js?v=20261008_v12"></script>
  <script src="app.js?v=20261008_v12"></script>
</body>
</html>
"""

    # Check for strictly zero course numbers
    forbidden_patterns = [r'Chem\.?\s*1', r'Chem\s+1', r'100\s*Marks', r'70\+20\+10']
    for pattern in forbidden_patterns:
        matches = re.findall(pattern, html_content, re.IGNORECASE)
        if matches:
            raise ValueError(f"STRICT ERROR: Prohibited course codes or marks detected in HTML: {matches}")

    with open("inorganic-chemistry-1.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Successfully generated inorganic-chemistry-1.html with pre-rendered Unit 1 and zero course numbers.")

if __name__ == "__main__":
    generate_html()
