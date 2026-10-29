import zipfile, re, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARCHIVE = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793271497058_746381a5.zip'

print("Generating Batch 2 EEE Simulation Suites...")

ENGINE_FOOTER = """
  if (!window.SimulationEngine) window.SimulationEngine = {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId || 'sim-container');
    if (!container) return;
    container.innerHTML = '';
    var unitNum = 1;
    if (simType) {
      var m = simType.match(/(\\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    } else {
      var bMatch = document.body.dataset.chapterIndex;
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') unitNum = parseInt(bMatch, 10) + 1;
      else {
        var pMatch = window.location.pathname.match(/chapter-(\\d+)/);
        if (pMatch) unitNum = parseInt(pMatch[1], 10);
      }
    }
    if (isNaN(unitNum) || unitNum < 1 || unitNum > 8) unitNum = 1;
    var modelsForUnit = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 1);
    modelsForUnit.forEach(function(m) {
      var card = document.createElement('section');
      card.className = 'eee-sim-card';
      card.setAttribute('aria-label', 'Interactive Simulation ' + m.idx);
      card.id = 'sim-card-' + m.idx;
      card.innerHTML = m.html;
      container.appendChild(card);
      m.init(card);
    });
  };

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        if (document.getElementById('sim-container')) window.SimulationEngine.initSimulation('sim-container');
      });
    } else {
      if (document.getElementById('sim-container')) window.SimulationEngine.initSimulation('sim-container');
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
"""

def clean_html(raw_html):
    main_m = re.search(r'<main[^>]*>([\s\S]*?)</main>', raw_html)
    content = main_m.group(1) if main_m else raw_html
    content = re.sub(r'<script[^>]*>[\s\S]*?</script>', '', content)
    content = re.sub(r'<div class=[\"\']navline[\"\']>[\s\S]*?</div>', '', content)
    content = re.sub(r'<nav[^>]*>[\s\S]*?</nav>', '', content)
    content = re.sub(r'<a[^>]*href=[\"\']\.\./[^\"\']*[\"\'][^>]*>[\s\S]*?</a>', '', content)
    content = re.sub(r'<h1([^>]*)>', r'<h3\1>', content)
    content = re.sub(r'</h1>', r'</h3>', content)
    return content.strip()

def transform_script(raw_script):
    s = raw_script.strip()
    s = re.sub(r'^\s*\(?\s*\(\s*\)\s*=>\s*\{', '', s)
    s = re.sub(r'\}\s*\)?\s*\(\s*\)\s*;\s*$', '', s)
    s = re.sub(r'document\.getElementById\(([\'\"`][^\'\"]+[\'\"`])\)', r'card.querySelector("#" + \1.replace(/^#/, ""))', s)
    s = re.sub(r'document\.querySelector\(', r'card.querySelector(', s)
    s = re.sub(r'document\.querySelectorAll\(', r'card.querySelectorAll(', s)
    return s.strip()

with zipfile.ZipFile(ARCHIVE, 'r') as z:
    # -------------------------------------------------------------
    # 1. electromagnetic-field-theory-ii
    # -------------------------------------------------------------
    print("Building electromagnetic-field-theory-ii-sims.js...")
    emf2_models_meta = [
        (1, 1, 'Displacement current in a capacitor', 'Ideal sinusoidal excitation V(t)=5 sin(2πft) V.', 'Capacitance', 'pF', 20, 500, 5, 100, 'Frequency', 'MHz', 1, 50, 1, 5, 'Time (ns)', 'Current (mA)'),
        (2, 2, 'Lossless plane-wave propagation', 'Lossless wave velocity, wavelength, and intrinsic impedance.', 'Frequency', 'MHz', 20, 1000, 10, 200, 'Relative permittivity', '', 1, 10, 0.1, 4, 'Propagation distance (m)', 'Electric field (V/m)'),
        (3, 3, 'Normal-incidence Fresnel power reflection', 'Reflection and transmission coefficients at planar dielectric boundary.', 'Incident εr', '', 1, 5, 0.1, 1, 'Transmitted εr', '', 1, 16, 0.2, 4, 'Transmitted relative permittivity', 'Reflected power fraction'),
        (4, 4, 'Lossless line standing-wave profile', 'Voltage standing wave ratio (VSWR) and voltage envelope.', 'Load resistance', 'Ω', 5, 200, 1, 100, 'Frequency', 'MHz', 50, 1000, 10, 200, 'Position from load (m)', 'Voltage magnitude / incident'),
        (5, 5, 'Rectangular TE10 guide cutoff', 'Dispersion relation, cutoff frequency, and phase velocity in metallic guide.', 'Broad wall a', 'mm', 10, 40, 0.5, 22.86, 'Operating frequency', 'GHz', 3, 20, 0.2, 10, 'Frequency (GHz)', 'β/k for air-filled TE10'),
        (6, 6, 'Hertzian element radiation pattern', 'Far-field radiation pattern and directivity of electrically short dipole.', 'Length / wavelength', '', 0.01, 0.1, 0.005, 0.05, 'Radiation efficiency', '', 0.1, 1, 0.05, 0.8, 'Polar angle (degrees)', 'Normalized gain (linear)'),
        (7, 7, 'Enclosure absorption and seam leakage', 'Shielding effectiveness against conducted and radiated interference.', 'Thickness / skin depth', '', 0.2, 6, 0.1, 3, 'Seam SE floor', 'dB', 5, 60, 1, 30, 'Thickness (skin depths)', 'Combined SE (dB)'),
        (8, 8, 'FDTD discrete phase and CFL check', 'Numerical phase velocity error and Courant-Friedrichs-Lewy stability condition.', 'Courant factor', '', 0.5, 1.3, 0.01, 0.9, 'Points / wavelength', '', 5, 40, 1, 15, 'Points per wavelength', 'Discrete phase-shift ratio')
    ]

    emf2_js = """/* Electromagnetic Field Theory II Interactive Simulation Suite */
(function(window) {
  'use strict';
  const c = 299792458, eta0 = 376.7303135;
  const f = n => Number.isFinite(n) ? Number(n).toPrecision(4) : 'not defined';

  function calcModel(mode, a, b) {
    let rows = [], message = '', xLabel = '', yLabel = '';
    if (mode === 1) {
      const C = a * 1e-12, fr = b * 1e6, peak = C * 2 * Math.PI * fr * 5 * 1e3;
      for (let i = 0; i <= 200; i++) {
        const t = i / (200 * fr);
        rows.push({x: t * 1e9, y: peak * Math.cos(2 * Math.PI * fr * t)});
      }
      xLabel = 'Time (ns)'; yLabel = 'Current (mA)';
      message = 'Peak displacement current: ' + f(peak) + ' mA. Ideal capacitor, no dielectric conduction.';
    } else if (mode === 2) {
      const v = c / Math.sqrt(b), wl = v / (a * 1e6), e = 5;
      for (let i = 0; i <= 200; i++) {
        let x = (i / 200) * 3 * wl;
        rows.push({x: x, y: e * Math.cos(2 * Math.PI * x / wl)});
      }
      xLabel = 'Distance (m)'; yLabel = 'E field (V/m)';
      message = 'Wave velocity: ' + f(v) + ' m/s, Wavelength: ' + f(wl) + ' m, Intrinsic impedance: ' + f(eta0 / Math.sqrt(b)) + ' Ω.';
    } else if (mode === 3) {
      for (let i = 0; i <= 200; i++) {
        let eps2 = 1 + i * 15 / 200, z1 = eta0 / Math.sqrt(a), z2 = eta0 / Math.sqrt(eps2), g = (z2 - z1) / (z2 + z1);
        rows.push({x: eps2, y: g * g});
      }
      let z1 = eta0 / Math.sqrt(a), z2 = eta0 / Math.sqrt(b), g = (z2 - z1) / (z2 + z1);
      xLabel = 'Transmitted εr2'; yLabel = 'Power Reflection R';
      message = 'At εr2=' + b + ': Reflection Γ=' + f(g) + ', Power R=' + f(g * g) + ', Transmission T=' + f(1 - g * g) + '.';
    } else if (mode === 4) {
      const g = (a - 50) / (a + 50), wl = c / (b * 1e6), beta = 2 * Math.PI / wl;
      for (let i = 0; i <= 200; i++) {
        const z = (i / 200) * 2 * wl;
        rows.push({x: z, y: Math.sqrt(1 + g * g + 2 * g * Math.cos(2 * beta * z))});
      }
      const vswr = (1 + Math.abs(g)) / (1 - Math.abs(g) || 1e-6);
      xLabel = 'Distance from load (m)'; yLabel = '|V| / |V+|';
      message = 'VSWR: ' + f(vswr) + ', Reflection coefficient: ' + f(g) + ' on 50 Ω reference line.';
    } else if (mode === 5) {
      const fc = (c / (2 * a * 1e-3)) * 1e-9;
      for (let i = 0; i <= 200; i++) {
        const freq = 1 + (25 * i / 200);
        const ratio = freq > fc ? Math.sqrt(1 - (fc / freq) ** 2) : 0;
        rows.push({x: freq, y: ratio});
      }
      const activeRatio = b > fc ? Math.sqrt(1 - (fc / b) ** 2) : 0;
      xLabel = 'Frequency (GHz)'; yLabel = 'β / k (propagation)';
      message = 'Cutoff fc=' + f(fc) + ' GHz. At f=' + b + ' GHz: ' + (b > fc ? 'Propagating mode (β/k=' + f(activeRatio) + ')' : 'Evanescent mode (cutoff)');
    } else if (mode === 6) {
      for (let i = 0; i <= 180; i++) {
        const theta = i * Math.PI / 180;
        rows.push({x: i, y: (Math.sin(theta) ** 2) * b});
      }
      xLabel = 'Polar angle θ (degrees)'; yLabel = 'Gain (linear)';
      message = 'Hertzian dipole sin²(θ) donut pattern. Peak broadside gain at θ=90°: ' + f(1.5 * b) + ' (dBi: ' + f(10 * Math.log10(1.5 * b)) + ').';
    } else if (mode === 7) {
      for (let i = 0; i <= 200; i++) {
        const thick = 0.1 + 6 * i / 200;
        const seAbs = 8.686 * thick;
        const total = Math.min(seAbs + b, 120);
        rows.push({x: thick, y: total});
      }
      xLabel = 'Thickness (skin depths)'; yLabel = 'Shielding SE (dB)';
      message = 'Total SE: ' + f(Math.min(8.686 * a + b, 120)) + ' dB. Absorption: ' + f(8.686 * a) + ' dB, Seam floor limit: ' + b + ' dB.';
    } else if (mode === 8) {
      for (let i = 5; i <= 40; i++) {
        const num = (2 / a) * Math.asin(a * Math.sin(Math.PI / i));
        rows.push({x: i, y: num / (2 * Math.PI / i)});
      }
      xLabel = 'Points per wavelength'; yLabel = 'Phase velocity ratio';
      message = 'Courant number S=' + a + (a > 1 ? ' (UNSTABLE: CFL violated!)' : ' (STABLE).') + ' Numerical dispersion decreases with finer grid sampling.';
    }
    return {rows, message, xLabel, yLabel};
  }

  function drawPlot(canvas, rows, xLabel, yLabel) {
    const ctx = canvas.getContext('2d');
    const W = canvas.width, H = canvas.height;
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, W, H);
    if (!rows || rows.length < 2) return;
    const xs = rows.map(r => r.x), ys = rows.map(r => r.y);
    const minX = Math.min(...xs), maxX = Math.max(...xs);
    let minY = Math.min(...ys), maxY = Math.max(...ys);
    if (minY === maxY) { minY -= 1; maxY += 1; }
    const pad = 50;
    const sx = x => pad + ((x - minX) / (maxX - minX || 1)) * (W - 2 * pad);
    const sy = y => H - pad - ((y - minY) / (maxY - minY || 1)) * (H - 2 * pad);
    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(pad, pad); ctx.lineTo(pad, H - pad); ctx.lineTo(W - pad, H - pad);
    ctx.stroke();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    rows.forEach((r, i) => {
      const x = sx(r.x), y = sy(r.y);
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    });
    ctx.stroke();
    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px sans-serif';
    ctx.fillText(xLabel, W / 2 - 40, H - 15);
    ctx.fillText(yLabel, pad, 25);
    ctx.fillText(f(minX), pad, H - 25);
    ctx.fillText(f(maxX), W - pad - 25, H - 25);
    ctx.fillText(f(maxY), 8, pad + 10);
    ctx.fillText(f(minY), 8, H - pad);
  }

  var MODELS = [];
"""
    for idx, unit, title, desc, p1_name, p1_unit, p1_min, p1_max, p1_step, p1_def, p2_name, p2_unit, p2_min, p2_max, p2_step, p2_def, xl, yl in emf2_models_meta:
        emf2_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {unit},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>{title}</h3><p>{desc}</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-{idx}">{p1_name} ({p1_unit}): <output id="v1-{idx}"></output>' +
              '<input id="p1-{idx}" type="range" min="{p1_min}" max="{p1_max}" step="{p1_step}" value="{p1_def}"/>' +
            '</label>' +
            '<label for="p2-{idx}">{p2_name} ({p2_unit}): <output id="v2-{idx}"></output>' +
              '<input id="p2-{idx}" type="range" min="{p2_min}" max="{p2_max}" step="{p2_step}" value="{p2_def}"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-{idx}" width="680" height="260" role="img" aria-label="EM wave response curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="msg-{idx}">-</output></div></div>',
    init: function(card) {{
      try {{
        var p1 = card.querySelector('#p1-{idx}');
        var p2 = card.querySelector('#p2-{idx}');
        var v1 = card.querySelector('#v1-{idx}');
        var v2 = card.querySelector('#v2-{idx}');
        var canvas = card.querySelector('#canvas-{idx}');
        var msg = card.querySelector('#msg-{idx}');
        function update() {{
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a) + ' {p1_unit}';
          if (v2) v2.textContent = String(b) + ' {p2_unit}';
          var res = calcModel({idx}, a, b);
          if (msg) msg.textContent = res.message;
          if (canvas) drawPlot(canvas, res.rows, res.xLabel, res.yLabel);
        }}
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      }} catch (err) {{
        console.warn('Electromagnetic Field Theory II sim error in model {idx}:', err);
      }}
    }}
  }});"""

    emf2_js += ENGINE_FOOTER
    emf2_path = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'electromagnetic-field-theory-ii', 'electromagnetic-field-theory-ii-sims.js')
    os.makedirs(os.path.dirname(emf2_path), exist_ok=True)
    with open(emf2_path, 'w', encoding='utf-8') as f:
        f.write(emf2_js)
    print(f"Wrote {emf2_path}")

    # -------------------------------------------------------------
    # 2. electrical-machines-i, electrical-machines-ii, power-systems-i, power-systems-ii
    # -------------------------------------------------------------
    batch2_other_slugs = ['electrical-machines-i', 'electrical-machines-ii', 'power-systems-i', 'power-systems-ii']
    for slug in batch2_other_slugs:
        print(f"Building {slug}-sims.js...")
        models = []
        for i in range(1, 9):
            p = f'OpenSTEM-Electrical-and-Electronics-Engineering/books/{slug}/simulations/model-{i:02d}.html'
            if p in z.namelist():
                raw = z.read(p).decode('utf-8', errors='ignore')
                clean_h = clean_html(raw)
                script_m = re.search(r'<script[^>]*>([\s\S]*?)</script>', raw)
                script_body = script_m.group(1) if script_m else ""
                transformed_s = transform_script(script_body)
                models.append({
                    'idx': i,
                    'unit': i,
                    'html': clean_h,
                    'script': transformed_s
                })
                
        out_js = [
            f"/* {slug} Interactive Simulation Suite */",
            "(function(window) {",
            "  'use strict';",
            "",
            "  var MODELS = [];"
        ]
        
        for m in models:
            esc_html = json.dumps(m['html'])
            out_js.append(f"""
  MODELS.push({{
    idx: {m['idx']},
    unit: {m['unit']},
    html: {esc_html},
    init: function(card) {{
      try {{
{m['script']}
      }} catch (err) {{
        console.warn('Sim init error in model {m['idx']}:', err);
      }}
    }}
  }});""")
  
        out_js.append(ENGINE_FOOTER)
        
        target_path = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', slug, f"{slug}-sims.js")
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(out_js))
        print(f"Wrote {target_path}")

print("Batch 2 simulation suites successfully generated!")
