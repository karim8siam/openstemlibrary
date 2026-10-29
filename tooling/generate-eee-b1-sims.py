import zipfile, re, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARCHIVE = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793271497058_746381a5.zip'

print("Generating Batch 1 EEE Simulation Suites...")

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
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 2);
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

with zipfile.ZipFile(ARCHIVE, 'r') as z:
    # -------------------------------------------------------------
    # 1. circuit-analysis-i
    # -------------------------------------------------------------
    print("Building circuit-analysis-i-sims.js...")
    c1_models = []
    for i in range(1, 17):
        p = f'OpenSTEM-Electrical-and-Electronics-Engineering/books/circuit-analysis-i/simulations/model-{i:02d}.html'
        html = z.read(p).decode('utf-8', errors='ignore')
        t_m = re.search(r'<h1>(.*?)</h1>', html)
        title = t_m.group(1) if t_m else f"Model {i}"
        lead_m = re.search(r'<p class="lead">(.*?)</p>', html)
        lead = lead_m.group(1) if lead_m else ""
        grid_m = re.search(r'<div class="grid">([\s\S]*?)</div>\s*</section>', html)
        grid_html = grid_m.group(1).strip() if grid_m else ""
        
        unit = ((i - 1) // 2) + 1
        c1_models.append({
            'idx': i,
            'unit': unit,
            'title': title,
            'lead': lead,
            'controls': grid_html
        })

    c1_js = """/* Circuit Analysis I Interactive Simulation Suite */
(function(window) {
  'use strict';

  function compute(id, p) {
    const {V=0, R=1, I=0, S=1, R1=1, R2=1, RL=1, V1=0, V2=0, RS=1, C=1, L=1, T=0, RM=1} = p;
    const f = (x, n=4) => Number(x).toPrecision(n);
    const graph = (fn, start=0, end=1) => Array.from({length: 101}, (_, i) => [start + (end - start) * i / 100, fn(start + (end - start) * i / 100)]);
    switch(id) {
      case 1: return {a: ['Current', f(V / R) + ' A'], b: ['Resistor power', f(V * V / R) + ' W'], points: graph(x => x / R, 0, 24), ylabel: 'I (A)'};
      case 2: return {a: ['Signed power', f(V * I * Math.sign(S || 1)) + ' W'], b: ['Interpretation', V * I * Math.sign(S || 1) >= 0 ? 'absorption' : 'delivery'], points: graph(x => x * I * Math.sign(S || 1), -24, 24), ylabel: 'P (W)'};
      case 3: { let eq = R2 * RL / (R2 + RL); return {a: ['Loaded output', f(V * eq / (R1 + eq)) + ' V'], b: ['Unloaded output', f(V * R2 / (R1 + R2)) + ' V'], points: graph(x => x * eq / (R1 + eq), 0, 24), ylabel: 'Vout (V)'}; }
      case 4: return {a: ['Series equivalent', f(R1 + R2) + ' Ω'], b: ['Parallel equivalent', f(R1 * R2 / (R1 + R2)) + ' Ω'], points: graph(x => R1 * x / (R1 + x), 1, 1000), ylabel: 'parallel R (Ω)'};
      case 5: { let x = V * R2 / (R1 + R2); return {a: ['Node voltage', f(x) + ' V'], b: ['KCL residual', f((x - V) / R1 + x / R2) + ' A'], points: graph(y => y * R2 / (R1 + R2), 0, 24), ylabel: 'Vnode (V)'}; }
      case 6: { let a = R1 + RS, b = R2 + RS, d = a * b - RS * RS, i1 = (V1 * b + RS * V2) / d, i2 = (V2 * a + RS * V1) / d; return {a: ['Mesh 1 current', f(i1) + ' A'], b: ['Mesh 2 current', f(i2) + ' A'], points: graph(x => (x * b + RS * V2) / d, 0, 24), ylabel: 'I1 (A)'}; }
      case 7: { let vl = V * RL / (R + RL); return {a: ['Load voltage', f(vl) + ' V'], b: ['Load power', f(vl * vl / RL) + ' W'], points: graph(x => V * x / (R + x), 1, 100), ylabel: 'Vload (V)'}; }
      case 8: { let pow = V * V * RL / (R + RL)**2; return {a: ['Load power', f(pow) + ' W'], b: ['Delivery efficiency', f(100 * RL / (R + RL)) + ' %'], points: graph(x => V * V * x / (R + x)**2, 1, 100), ylabel: 'Pload (W)'}; }
      case 9: return {a: ['Charge', f(C * 1e-6 * V * 1e3) + ' mC'], b: ['Stored energy', f(0.5 * C * 1e-6 * V * V * 1e3) + ' mJ'], points: graph(x => 0.5 * C * 1e-6 * x * x * 1e3, 0, 30), ylabel: 'E (mJ)'};
      case 10: return {a: ['Stored energy', f(0.5 * L * 1e-3 * I * I * 1e3) + ' mJ'], b: ['Flux linkage', f(L * 1e-3 * I) + ' Wb·turn'], points: graph(x => 0.5 * L * 1e-3 * x * x * 1e3, 0, 10), ylabel: 'E (mJ)'};
      case 11: { let tau = R * 1000 * C * 1e-6; return {a: ['V(t)', f(V * (1 - Math.exp(-T / tau))) + ' V'], b: ['Time constant', f(tau) + ' s'], points: graph(t => V * (1 - Math.exp(-t / tau)), 0, Math.max(0.001, 5 * tau)), ylabel: 'Vc (V)'}; }
      case 12: { let tau = L * 0.001 / R, sec = T * 0.001; return {a: ['I(t)', f((V / R) * (1 - Math.exp(-sec / tau))) + ' A'], b: ['Time constant', f(tau * 1000) + ' ms'], points: graph(t => (V / R) * (1 - Math.exp(-t / tau)), 0, Math.max(0.00001, 5 * tau)), ylabel: 'IL (A)'}; }
      case 13: { let ll = L * 0.001, cc = C * 1e-6, alpha = R / (2 * ll), w = 1 / Math.sqrt(ll * cc), crit = 2 * Math.sqrt(ll / cc), state = alpha < w - 1e-8 ? 'underdamped' : alpha > w + 1e-8 ? 'overdamped' : 'critical'; return {a: ['Damping regime', state], b: ['Critical resistance', f(crit) + ' Ω'], points: graph(x => (x / (2 * ll)) / w, 0, 200), ylabel: 'ζ'}; }
      case 14: { let ll = L * 0.001, cc = C * 1e-6, alpha = R / (2 * ll), w = 1 / Math.sqrt(ll * cc); function calc(t) { if (alpha < w) { let wd = Math.sqrt(w * w - alpha * alpha); return V * Math.exp(-alpha * t) * (Math.cos(wd * t) + (alpha / wd) * Math.sin(wd * t)); } if (Math.abs(alpha - w) < 1e-9) return V * Math.exp(-alpha * t) * (1 + alpha * t); let beta = Math.sqrt(alpha * alpha - w * w); return V * Math.exp(-alpha * t) * (Math.cosh(beta * t) + (alpha / beta) * Math.sinh(beta * t)); } return {a: ['Capacitor voltage', f(calc(T * 0.001)) + ' V'], b: ['Damping ratio', f(alpha / w)], points: graph(t => calc(t), 0, 0.05), ylabel: 'Vc (V)'}; }
      case 15: { let eq = R2 * RM / (R2 + RM); return {a: ['Measured voltage', f(V * eq / (R1 + eq)) + ' V'], b: ['Unloaded voltage', f(V * R2 / (R1 + R2)) + ' V'], points: graph(x => V * (R2 * x / (R2 + x)) / (R1 + R2 * x / (R2 + x)), 100, 100000), ylabel: 'Measured V (V)'}; }
      case 16: { let tol = T / 100, high = V * (R2 * (1 + tol)) / (R1 * (1 - tol) + R2 * (1 + tol)), low = V * (R2 * (1 - tol)) / (R1 * (1 + tol) + R2 * (1 - tol)); return {a: ['Worst-case low', f(low) + ' V'], b: ['Worst-case high', f(high) + ' V'], points: graph(x => V * (R2 * (1 + x / 100)) / (R1 * (1 - x / 100) + R2 * (1 + x / 100)), 0, 20), ylabel: 'Vhigh (V)'}; }
      default: return {a: ['Output', '0'], b: ['Status', 'idle'], points: [], ylabel: 'V'};
    }
  }

  function renderGraph(points, ylabel) {
    const W = 700, H = 240, l = 55, r = 20, t = 20, b = 35;
    let xs = points.map(x => x[0]), ys = points.map(x => x[1]);
    let xmin = Math.min(...xs), xmax = Math.max(...xs), ymin = Math.min(0, ...ys), ymax = Math.max(0, ...ys);
    if (ymax - ymin < 1e-10) ymax = ymin + 1;
    const xx = x => l + (x - xmin) / (xmax - xmin || 1) * (W - l - r);
    const yy = y => t + (ymax - y) / (ymax - ymin) * (H - t - b);
    let d = points.map(([x, y], i) => (i ? 'L' : 'M') + xx(x).toFixed(2) + ',' + yy(y).toFixed(2)).join(' ');
    return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Response curve" style="width:100%;height:auto;display:block">
      <rect x="${l}" y="${t}" width="${W - l - r}" height="${H - t - b}" fill="#0f172a" rx="4"/>` +
      Array.from({length: 5}, (_, i) => {
        let y = t + (H - t - b) * i / 4, val = ymax - (ymax - ymin) * i / 4;
        return `<line x1="${l}" y1="${y}" x2="${W - r}" y2="${y}" stroke="#1e293b"/>
                <text x="8" y="${y + 4}" font-size="11" fill="#64748b">${val.toPrecision(3)}</text>`;
      }).join('') +
      `<path d="${d}" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linejoin="round"/>
       <text x="${l}" y="${H - 10}" fill="#94a3b8" font-size="11">input: ${xmin.toPrecision(3)} → ${xmax.toPrecision(3)}</text>
       <text x="${W - r}" y="${H - 10}" fill="#38bdf8" text-anchor="end" font-size="11">${ylabel}</text>
    </svg>`;
  }

  var MODELS = [];
"""
    for m in c1_models:
        esc_controls = json.dumps(f"""<div class="sim-header"><span class="badge">Model {m['idx']:02d}</span><h3>{m['title']}</h3><p>{m['lead']}</p></div><div class="sim-controls">{m['controls']}</div><div class="readouts"><div class="stat-box" id="res-a"><small>-</small><output>-</output></div><div class="stat-box" id="res-b"><small>-</small><output>-</output></div></div><div class="plot" id="sim-chart"></div>""")
        c1_js += f"""
  MODELS.push({{
    idx: {m['idx']},
    unit: {m['unit']},
    html: {esc_controls},
    init: function(card) {{
      try {{
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {{
          var p = {{}};
          inputs.forEach(function(el) {{
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          }});
          var r = compute({m['idx']}, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) {{ ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }}
          if (rb && r.b) {{ rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }}
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }}
        inputs.forEach(function(el) {{ el.addEventListener('input', update); }});
        update();
      }} catch (err) {{
        console.warn('Circuit Analysis I sim error in model {m['idx']}:', err);
      }}
    }}
  }});"""

    c1_js += ENGINE_FOOTER
    c1_path = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'circuit-analysis-i', 'circuit-analysis-i-sims.js')
    os.makedirs(os.path.dirname(c1_path), exist_ok=True)
    with open(c1_path, 'w', encoding='utf-8') as f:
        f.write(c1_js)
    print(f"Wrote {c1_path}")

    # -------------------------------------------------------------
    # 2. circuit-analysis-ii
    # -------------------------------------------------------------
    print("Building circuit-analysis-ii-sims.js...")
    c2_models = []
    for i in range(1, 17):
        p = f'OpenSTEM-Electrical-and-Electronics-Engineering/books/circuit-analysis-ii/simulations/model-{i:02d}.html'
        html = z.read(p).decode('utf-8', errors='ignore')
        t_m = re.search(r'<h1>(.*?)</h1>', html)
        title = t_m.group(1) if t_m else f"Model {i}"
        desc_m = re.search(r'<main><section><p>(.*?)</p>', html)
        desc = desc_m.group(1) if desc_m else ""
        ideal_m = re.search(r'<p><strong>Ideal relation:</strong>\s*<code>(.*?)</code></p>', html)
        ideal = ideal_m.group(1) if ideal_m else ""
        ctrl_m = re.search(r'<div class="controls">([\s\S]*?)</div>\s*</section>', html)
        ctrls = ctrl_m.group(1).strip() if ctrl_m else ""
        unit = ((i - 1) // 2) + 1
        c2_models.append({
            'idx': i,
            'unit': unit,
            'title': title,
            'desc': desc,
            'ideal': ideal,
            'controls': ctrls
        })

    engine_js = z.read('OpenSTEM-Electrical-and-Electronics-Engineering/books/circuit-analysis-ii/simulations/engine.js').decode('utf-8', errors='ignore')
    calc_m = re.search(r'(function calculate\(id,\s*p\)[\s\S]*?)(?=function init\(|if\(typeof module)', engine_js)
    calc_func_body = calc_m.group(1).strip() if calc_m else ""

    c2_header = """/* Circuit Analysis II Interactive Simulation Suite */
(function(window) {
  'use strict';
  const pi = Math.PI, sq = Math.sqrt;
  const logspace = (a, b, n=81) => Array.from({length: n}, (_, i) => a * Math.pow(b / a, i / (n - 1)));
  const line = (fn, xs) => xs.map(x => [x, fn(x)]);
  const format = v => typeof v === 'number' ? (Math.abs(v) >= 1000 || (Math.abs(v) < 0.01 && v !== 0) ? v.toExponential(3) : v.toFixed(3)) : v;

""" + calc_func_body + """

  function draw(svg, points, axis, xlabel) {
    const W = 670, H = 260, pad = 50;
    if (!points || !points.length) return;
    const xs = points.map(d => d[0]), ys = points.map(d => d[1]);
    const minX = Math.min(...xs), maxX = Math.max(...xs);
    let minY = Math.min(...ys), maxY = Math.max(...ys);
    if (minY === maxY) { minY -= 1; maxY += 1; }
    const sx = x => pad + (x - minX) / (maxX - minX || 1) * (W - 2 * pad);
    const sy = y => H - pad - (y - minY) / (maxY - minY || 1) * (H - 2 * pad);
    const pStr = points.map((d, i) => (i ? 'L' : 'M') + sx(d[0]).toFixed(1) + ',' + sy(d[1]).toFixed(1)).join(' ');
    svg.innerHTML = `
      <rect x="${pad}" y="${pad / 2}" width="${W - 2 * pad}" height="${H - 1.5 * pad}" fill="#0f172a" rx="4"/>
      <path d="${pStr}" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="${pad}" y="${H - 10}" fill="#94a3b8" font-size="11">${xlabel || 'Input'}</text>
      <text x="${W - pad}" y="${H - 10}" fill="#38bdf8" text-anchor="end" font-size="11">${axis || 'Output'}</text>
      <text x="${pad}" y="${pad / 2 - 4}" fill="#64748b" font-size="10">${format(maxY)}</text>
      <text x="${pad}" y="${H - pad + 14}" fill="#64748b" font-size="10">${format(minY)}</text>
    `;
  }

  var MODELS = [];
"""
    c2_js = c2_header
    for m in c2_models:
        esc_controls = json.dumps(f"""<div class="sim-header"><span class="badge">Model {m['idx']:02d}</span><h3>{m['title']}</h3><p>{m['desc']}</p><p><code>{m['ideal']}</code></p></div><div class="sim-controls">{m['controls']}</div><div class="readouts" id="metrics"></div><svg id="plot" class="plot" role="img" aria-label="Numerical response graph" viewBox="0 0 670 260"></svg>""")
        c2_js += f"""
  MODELS.push({{
    idx: {m['idx']},
    unit: {m['unit']},
    html: {esc_controls},
    init: function(card) {{
      try {{
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {{
          var p = {{}};
          for (var i = 0; i < inputs.length; i++) {{
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }}
          var r = calculate({m['idx']}, p);
          if (result && r.metrics) {{
            result.innerHTML = r.metrics.map(function(x) {{
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }}).join('');
          }}
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[{m['idx'] - 1}] : r.xlabel) : 'Sweep');
        }}
        inputs.forEach(function(el) {{ el.addEventListener('input', update); }});
        update();
      }} catch (err) {{
        console.warn('Circuit Analysis II sim error in model {m['idx']}:', err);
      }}
    }}
  }});"""

    c2_js += ENGINE_FOOTER
    c2_path = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'circuit-analysis-ii', 'circuit-analysis-ii-sims.js')
    os.makedirs(os.path.dirname(c2_path), exist_ok=True)
    with open(c2_path, 'w', encoding='utf-8') as f:
        f.write(c2_js)
    print(f"Wrote {c2_path}")

    # -------------------------------------------------------------
    # 3. signals-and-systems
    # -------------------------------------------------------------
    print("Building signals-and-systems-sims.js...")
    ss_raw = z.read('OpenSTEM-Electrical-and-Electronics-Engineering/books/signals-and-systems/assets/models.js').decode('utf-8', errors='ignore')
    ss_raw = re.sub(r'if\s*\(\s*typeof document[\s\S]*?$', '', ss_raw)
    ss_raw = re.sub(r'if\s*\(\s*typeof module[\s\S]*?$', '', ss_raw)

    ss_js = """/* Signals and Systems Interactive Simulation Suite */
(function(window) {
  'use strict';
""" + ss_raw + """

  var MODELS = [];
  for (var i = 1; i <= 16; i++) {
    (function(idx) {
      var cfg = configs[idx - 1];
      var unit = Math.floor((idx - 1) / 2) + 1;
      var html = '<div class="sim-header"><span class="badge">Model ' + (idx < 10 ? '0' : '') + idx + '</span><h3>' + cfg.title + '</h3><p>' + cfg.description + '</p></div>' +
        '<div class="sim-controls"><label for="param-' + idx + '">' + cfg.parameterLabel + ': <output id="current-' + idx + '"></output></label>' +
        '<input id="param-' + idx + '" type="range" min="' + cfg.min + '" max="' + cfg.max + '" step="' + cfg.step + '" value="' + cfg.default + '"/></div>' +
        '<div class="plot"><canvas id="plot-' + idx + '" width="680" height="260" role="img" aria-label="Signal response plot"></canvas></div>' +
        '<div class="stat-box" id="status-' + idx + '" aria-live="polite"></div>';
      
      MODELS.push({
        idx: idx,
        unit: unit,
        html: html,
        init: function(card) {
          try {
            var slider = card.querySelector('#param-' + idx);
            var value = card.querySelector('#current-' + idx);
            var output = card.querySelector('#status-' + idx);
            var canvas = card.querySelector('#plot-' + idx);
            function update() {
              var p = Number(slider.value);
              if (value) value.textContent = String(p);
              try {
                var result = evaluate(idx, p);
                draw(canvas, result);
                if (output) output.textContent = result.summary;
              } catch (err) {
                if (output) output.textContent = 'Model error: ' + err.message;
              }
            }
            slider.addEventListener('input', update);
            update();
          } catch (err) {
            console.warn('Signals and Systems sim error in model ' + idx + ':', err);
          }
        }
      });
    })(i);
  }
""" + ENGINE_FOOTER
    ss_path = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'signals-and-systems', 'signals-and-systems-sims.js')
    os.makedirs(os.path.dirname(ss_path), exist_ok=True)
    with open(ss_path, 'w', encoding='utf-8') as f:
        f.write(ss_js)
    print(f"Wrote {ss_path}")

    # -------------------------------------------------------------
    # 4. analog-electronics
    # -------------------------------------------------------------
    print("Building analog-electronics-sims.js...")
    ae_raw = z.read('OpenSTEM-Electrical-and-Electronics-Engineering/books/analog-electronics/assets/models.js').decode('utf-8', errors='ignore')
    specs_m = re.search(r'const specs\s*=\s*(\{[\s\S]*?\});\s*function model', ae_raw)
    specs_code = specs_m.group(1) if specs_m else "{}"
    model_m = re.search(r'(function model\(kind,\s*v\)[\s\S]*?)(?=function render\(\)|p\.addEventListener)', ae_raw)
    model_func_body = model_m.group(1).strip() if model_m else ""

    ae_kinds = [
        ('diode', 'Diode Exponential Current', 'Voltage sweep 0–0.65 V, fixed Is=1 pA, n=1.8, T=300 K; ideal isothermal diode only.', 1),
        ('rectifier', 'Half-Wave Rectifier Peak', 'Peak output across load resistor without filtering capacitor.', 1),
        ('ripple', 'Filter Capacitor Ripple', 'Filter capacitor smoothing ripple voltage under load current.', 2),
        ('zener', 'Zener Voltage Regulator', 'Zener diode shunt breakdown regulation and series current limiting.', 2),
        ('bjt_sat', 'BJT Saturation & Active Line', 'Base-emitter overdrive and collector-emitter saturation boundary.', 3),
        ('bjt_bias', 'Four-Resistor Divider Bias', 'Thermal stability of collector current against beta variations.', 3),
        ('ce_gain', 'Common Emitter Small-Signal Gain', 'Midband transconductance gain with collector and load resistance.', 4),
        ('degen', 'Emitter Degeneration Trade-Off', 'Gain reduction versus linearity and input impedance stabilization.', 4),
        ('mos_square', 'MOSFET Square-Law Conduction', 'Overdrive voltage Vgs-Vt and saturation drain current id.', 5),
        ('cs_stage', 'Common Source Amplifier Gain', 'MOSFET transconductance gm and small-signal stage gain.', 5),
        ('diff_pair', 'Differential Pair Steering', 'Differential input voltage steering current between balanced arms.', 6),
        ('opamp_inv', 'Inverting Op-Amp Closed-Loop', 'Virtual ground and closed-loop feedback gain -Rf/Rin.', 6),
        ('sallen_key', 'Sallen-Key Active Filter', 'Second-order Butterworth low-pass filter cutoff and Q factor.', 7),
        ('feedback', 'Negative Feedback Desensitization', 'Closed-loop gain desensitization vs open-loop gain A and beta.', 7),
        ('pushpull', 'Class-B Push-Pull Crossover', 'Deadband crossover distortion near zero-crossing without diode bias.', 8),
        ('thermal', 'Transistor Junction Thermal Limits', 'Power dissipation, junction-to-ambient thermal resistance and Tj.', 8)
    ]

    ae_js = """/* Analog Electronics Interactive Simulation Suite */
(function(window) {
  'use strict';
  const specs = """ + specs_code + """;
  """ + model_func_body + """

  function renderGraph(kind, v, S) {
    const curr = model(kind, v);
    const W = 680, H = 240, left = 55, right = 20, top = 20, bottom = 35;
    const pts = [];
    for (let i = 0; i <= 60; i++) {
      const x = S[0] + (S[1] - S[0]) * (i / 60);
      pts.push([x, model(kind, x).val]);
    }
    const ymin = Math.min(...pts.map(p => p[1]));
    let ymax = Math.max(...pts.map(p => p[1]));
    if (ymax - ymin < 1e-9) ymax = ymin + 1;
    const mapX = x => left + ((x - S[0]) / (S[1] - S[0] || 1)) * (W - left - right);
    const mapY = y => H - bottom - ((y - ymin) / (ymax - ymin || 1)) * (H - top - bottom);
    const pathD = pts.map((p, i) => (i === 0 ? 'M' : 'L') + mapX(p[0]).toFixed(1) + ',' + mapY(p[1]).toFixed(1)).join(' ');
    const activeY = mapY(Math.min(Math.max(curr.val, ymin), ymax));
    return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Analog transfer curve" style="width:100%;height:auto;display:block">
      <rect x="${left}" y="${top}" width="${W - left - right}" height="${H - top - bottom}" fill="#0f172a" rx="4"/>
      <path d="${pathD}" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <circle cx="${mapX(v).toFixed(1)}" cy="${activeY.toFixed(1)}" r="5" fill="#f59e0b"/>
      <text x="${left}" y="${H - 10}" fill="#94a3b8" font-size="11">${S[0]} ${S[4]}</text>
      <text x="${W - right}" y="${H - 10}" fill="#94a3b8" text-anchor="end" font-size="11">${S[1]} ${S[4]}</text>
      <text x="${left}" y="${top - 6}" fill="#38bdf8" font-size="11">${curr.units} (max: ${ymax.toFixed(2)})</text>
    </svg>`;
  }

  var MODELS = [];
"""
    for idx, (kind, title, desc, unit) in enumerate(ae_kinds, 1):
        ae_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {unit},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>{title}</h3><p>{desc}</p></div>' +
          '<div class="sim-controls"><label for="param-{idx}">Input sweep (' + specs['{kind}'][4] + '): <output id="val-{idx}"></output></label>' +
          '<input id="param-{idx}" type="range" min="' + specs['{kind}'][0] + '" max="' + specs['{kind}'][1] + '" step="' + specs['{kind}'][2] + '" value="' + specs['{kind}'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-{idx}">-</output></div></div>' +
          '<div class="plot" id="plot-{idx}"></div>',
    init: function(card) {{
      try {{
        var slider = card.querySelector('#param-{idx}');
        var valOut = card.querySelector('#val-{idx}');
        var resOut = card.querySelector('#readout-{idx}');
        var plot = card.querySelector('#plot-{idx}');
        var S = specs['{kind}'];
        function update() {{
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('{kind}', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('{kind}', v, S);
        }}
        slider.addEventListener('input', update);
        update();
      }} catch (err) {{
        console.warn('Analog Electronics sim error in model {idx}:', err);
      }}
    }}
  }});"""

    ae_js += ENGINE_FOOTER
    ae_path = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'analog-electronics', 'analog-electronics-sims.js')
    os.makedirs(os.path.dirname(ae_path), exist_ok=True)
    with open(ae_path, 'w', encoding='utf-8') as f:
        f.write(ae_js)
    print(f"Wrote {ae_path}")

    # -------------------------------------------------------------
    # 5. digital-electronics
    # -------------------------------------------------------------
    print("Building digital-electronics-sims.js...")
    de_raw = z.read('OpenSTEM-Electrical-and-Electronics-Engineering/books/digital-electronics/assets/models.js').decode('utf-8', errors='ignore')
    de_model_m = re.search(r'(const MODEL\s*=\s*\{[\s\S]*?\n\};)', de_raw)
    de_model_code = de_model_m.group(1) if de_model_m else ""

    de_models_meta = [
        (1, 1, 'base', 'Radix and Signed Words', 'Explore binary, hexadecimal, and two’s-complement interpretations.', [('n', 'Decimal value', 214), ('width', 'Word width (bits)', 8)]),
        (2, 1, 'gates', 'Logic Gates Truth Table', 'Generate truth tables for primary two-input logic gates.', [('gate', 'Gate (0:AND, 1:OR, 2:NAND, 3:NOR, 4:XOR)', 0), ('a', 'Input A (0 or 1)', 1), ('b', 'Input B (0 or 1)', 0)]),
        (3, 2, 'demorgan', 'De Morgan Theorem Duals', 'Verify equivalence of NAND/NOR expressions against inverted sums.', [('a', 'Input A', 1), ('b', 'Input B', 0)]),
        (4, 2, 'kmap', '4-Variable K-Map Minimizer', 'Sum-of-products minimization across gray-code minterm grids.', [('minterms', 'Minterm mask (0-65535)', 4369)]),
        (5, 3, 'mux', '2-to-1 and 4-to-1 Multiplexer', 'Data routing and selection with binary address control lines.', [('sel', 'Select input (0-3)', 2), ('d0', 'D0', 1), ('d1', 'D1', 0), ('d2', 'D2', 1), ('d3', 'D3', 0)]),
        (6, 3, 'adder', 'Full Adder Binary Arithmetic', 'Calculate sum and carry-out bits for two operands and carry-in.', [('a', 'Bit A', 1), ('b', 'Bit B', 1), ('cin', 'Carry-in', 1)]),
        (7, 4, 'srlatch', 'Active-Low SR Latch', 'Set, reset, hold, and prohibited metastable states.', [('s', 'Set bit (0=active)', 0), ('r', 'Reset bit (0=active)', 1), ('qprev', 'Previous Q', 0)]),
        (8, 4, 'dff', 'D Flip-Flop Edge Trigger', 'Positive edge-triggered data latching and setup/hold timing margin.', [('d', 'Data D', 1), ('clk', 'Clock transition (1=edge)', 1)]),
        (9, 5, 'counter', '3-Bit Synchronous Counter', 'Modulo-8 synchronous up/down counter state progression.', [('dir', 'Direction (1=Up, 0=Down)', 1), ('current', 'Current state (0-7)', 3)]),
        (10, 5, 'shift', '4-Bit Universal Shift Register', 'Parallel load, left shift, right shift, and serial hold.', [('mode', 'Mode (0:Hold, 1:Right, 2:Left, 3:Load)', 1), ('val', 'Current word (0-15)', 9), ('sin', 'Serial in bit', 1)]),
        (11, 6, 'fsm', 'Mealy vs Moore Sequence Detector', '101 bit sequence detection with overlapping state memory.', [('bit', 'Next input stream bit (0/1)', 1), ('state', 'Current state (0-3)', 2)]),
        (12, 6, 'state', 'State Table Minimizer', 'Identify equivalent states and eliminate redundant rows.', [('rows', 'States count (2-8)', 4)]),
        (13, 7, 'cmos', 'CMOS Inverter Transfer Curve', 'Voltage transfer characteristic (VTC), VOH, VOL, and noise margins.', [('vdd', 'Supply Vdd (V)', 5), ('vtn', 'Vtn threshold (V)', 0.8), ('vtp', 'Vtp threshold (V)', -0.8)]),
        (14, 7, 'fanout', 'Propagation Delay vs Fan-Out', 'Capacitive loading delay scaling with fan-out count.', [('fanout', 'Driven load gates count', 4), ('cgate', 'Gate cap (fF)', 15)]),
        (15, 8, 'sram', 'SRAM 6-Transistor Cell Array', 'Differential bitline precharge, sense amplifier, and write margin.', [('word', 'Wordline active (0/1)', 1), ('bit', 'Data write bit (0/1)', 1)]),
        (16, 8, 'pla', 'Programmable Logic Array (PLA)', 'AND-OR matrix configuration for sum-of-products mapping.', [('inputs', 'Active inputs bitmask (0-15)', 5)])
    ]

    de_js = """/* Digital Electronics Interactive Simulation Suite */
(function(window) {
  'use strict';
  """ + de_model_code + """

  var MODELS = [];
"""
    for idx, unit, fn, title, desc, params in de_models_meta:
        p_inputs = "".join([f'<label for="p-{idx}-{pk}">{plabel}<input type="number" id="p-{idx}-{pk}" data-param="{pk}" value="{pdef}" step="any"></label>' for pk, plabel, pdef in params])
        de_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {unit},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>{title}</h3><p>{desc}</p></div>' +
          '<div class="sim-controls">{p_inputs}</div>' +
          '<div class="readouts" id="out-{idx}"></div>',
    init: function(card) {{
      try {{
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-{idx}');
        function update() {{
          var p = {{}};
          inputs.forEach(function(el) {{ p[el.dataset.param] = Number(el.value); }});
          var fn = MODEL['{fn}'];
          if (fn && out) {{
            try {{
              var res = fn(p);
              if (Array.isArray(res)) {{
                out.innerHTML = res.map(function(item) {{
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }}).join('');
              }} else {{
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }}
            }} catch (err) {{
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }}
          }}
        }}
        inputs.forEach(function(el) {{ el.addEventListener('input', update); }});
        update();
      }} catch (err) {{
        console.warn('Digital Electronics sim error in model {idx}:', err);
      }}
    }}
  }});"""

    de_js += ENGINE_FOOTER
    de_path = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'digital-electronics-for-electrical-engineers', 'digital-electronics-for-electrical-engineers-sims.js')
    os.makedirs(os.path.dirname(de_path), exist_ok=True)
    with open(de_path, 'w', encoding='utf-8') as f:
        f.write(de_js)
    print(f"Wrote {de_path}")

    # -------------------------------------------------------------
    # 6. electromagnetic-field-theory-i
    # -------------------------------------------------------------
    print("Building electromagnetic-field-theory-i-sims.js...")
    emf_models_meta = [
        (1, 1, 'Two-Charge Electric Field Sampler', 'Charge superposition in air: two equal positive charges at x=±d/2.', 'Charge (nC)', 1, 10, 1, 2, 'Separation (cm)', 5, 30, 1, 20),
        (2, 2, 'Spherical Gaussian Flux Profiler', 'Flux density D and total enclosed charge across radial shells.', 'Enclosed Q (nC)', 1, 20, 1, 5, 'Outer radius R (cm)', 5, 25, 1, 10),
        (3, 3, '1D Parallel Plate Potential Solver', 'Linear potential fall and constant electric field between conducting plates.', 'Plate voltage V0 (V)', 10, 200, 5, 50, 'Gap distance d (mm)', 1, 10, 1, 4),
        (4, 4, 'Coaxial Dielectric Displacement', 'Radial displacement field and potential gradient with relative permittivity.', 'Inner core potential (V)', 10, 100, 5, 50, 'Relative permittivity εr', 1, 10, 0.5, 3),
        (5, 5, 'Steady Wire Current Density & Resistance', 'Ohmic voltage gradient, current density J, and conductor heating.', 'Applied Voltage (V)', 1, 50, 1, 12, 'Conductivity σ (MS/m)', 10, 60, 5, 35),
        (6, 6, 'Biot-Savart Filamentary Magnetic Field', 'Radial decay of magnetic flux density B around a straight wire.', 'Current I (A)', 1, 50, 1, 10, 'Radial distance max (cm)', 5, 30, 1, 15),
        (7, 7, 'Solenoid Core Magnetic Flux Density', 'Interior uniform magnetic field and permeability boost from magnetic core.', 'Turns count N', 100, 1000, 50, 400, 'Core relative μr', 1, 500, 10, 100),
        (8, 8, 'Magnetic Interface Boundary Refraction', 'Tangential H continuity and normal B continuity at iron-air boundary.', 'Incident angle θ1 (deg)', 5, 85, 5, 45, 'Relative μr of core', 10, 500, 10, 150)
    ]

    emf_js = """/* Electromagnetic Field Theory I Interactive Simulation Suite */
(function(window) {
  'use strict';
  const eps0 = 8.8541878128e-12, mu0 = 4 * Math.PI * 1e-7, k = 1 / (4 * Math.PI * eps0), eta = Math.sqrt(mu0 / eps0);
  const fmt = x => Number(x).toExponential(4);

  function computeModel(mode, a, b) {
    let rows = [], summary = '', curveLabel = '';
    if (mode === 1) {
      const q = a * 1e-9, d = b * 0.01, y = 0.05;
      for (let i = 0; i <= 200; i++) {
        const x = -0.3 + 0.6 * i / 200;
        const r1 = Math.hypot(x + d / 2, y), r2 = Math.hypot(x - d / 2, y);
        const Ex = k * q * ((x + d / 2) / (r1 ** 3) + (x - d / 2) / (r2 ** 3));
        rows.push({x, y: Ex});
      }
      curveLabel = 'Ex along line y=0.05m (V/m)';
      summary = `Peak Ex: ${fmt(Math.max(...rows.map(r => Math.abs(r.y))))} V/m | Charges at ±${(d * 50).toFixed(1)} cm`;
    } else if (mode === 2) {
      const q = a * 1e-9, R = b * 0.01;
      for (let i = 1; i <= 200; i++) {
        const r = 0.3 * i / 200;
        const Dr = r < R ? (q / (4 * Math.PI * R ** 3)) * r : q / (4 * Math.PI * r ** 2);
        rows.push({x: r, y: Dr});
      }
      curveLabel = 'Radial displacement Dr (C/m²)';
      summary = `Peak surface Dr: ${fmt(q / (4 * Math.PI * R ** 2))} C/m² at R=${(R * 100).toFixed(1)} cm`;
    } else if (mode === 3) {
      const V0 = a, d = b * 0.001;
      for (let i = 0; i <= 200; i++) {
        const x = d * i / 200;
        const V = V0 * (1 - x / d);
        rows.push({x, y: V});
      }
      curveLabel = 'Potential V(x) across gap (V)';
      summary = `Uniform Electric Field: ${fmt(V0 / d)} V/m across ${d * 1000} mm gap`;
    } else if (mode === 4) {
      const V0 = a, er = b, a_rad = 0.005, b_rad = 0.025;
      for (let i = 0; i <= 200; i++) {
        const r = a_rad + (b_rad - a_rad) * i / 200;
        const V = V0 * Math.log(b_rad / r) / Math.log(b_rad / a_rad);
        rows.push({x: r, y: V});
      }
      curveLabel = 'Coaxial potential profile V(r) (V)';
      summary = `Capacitance per meter: ${fmt(2 * Math.PI * eps0 * er / Math.log(b_rad / a_rad))} F/m`;
    } else if (mode === 5) {
      const V = a, sigma = b * 1e6, L = 1.0;
      for (let i = 0; i <= 200; i++) {
        const z = L * i / 200;
        const J = sigma * (V / L);
        rows.push({x: z, y: J});
      }
      curveLabel = 'Current density J (A/m²)';
      summary = `Current density: ${fmt(sigma * V / L)} A/m² | Electric Field: ${(V / L).toFixed(2)} V/m`;
    } else if (mode === 6) {
      const I = a, rmax = b * 0.01;
      for (let i = 1; i <= 200; i++) {
        const r = 0.002 + (rmax - 0.002) * i / 200;
        const B = (mu0 * I) / (2 * Math.PI * r);
        rows.push({x: r, y: B});
      }
      curveLabel = 'Magnetic flux density B(r) (Tesla)';
      summary = `B at closest r: ${fmt(rows[0].y)} T | Decay at outer edge: ${fmt(rows[rows.length - 1].y)} T`;
    } else if (mode === 7) {
      const N = a, mur = b, L = 0.2;
      for (let i = 0; i <= 200; i++) {
        const I = 0.05 * i / 200;
        const B = (mu0 * mur * N * I) / L;
        rows.push({x: I, y: B});
      }
      curveLabel = 'Core flux density B vs Current (T)';
      summary = `Permeability multiplier: ${mur}x | Core B at 0.05A: ${fmt(rows[rows.length - 1].y)} T`;
    } else if (mode === 8) {
      const theta1 = a * Math.PI / 180, mur2 = b;
      for (let i = 1; i <= 180; i++) {
        const th1 = i * 0.5 * Math.PI / 180;
        const tanTh2 = mur2 * Math.tan(th1);
        const th2 = Math.atan(tanTh2) * 180 / Math.PI;
        rows.push({x: i * 0.5, y: th2});
      }
      const activeTh2 = Math.atan(mur2 * Math.tan(theta1)) * 180 / Math.PI;
      curveLabel = 'Refracted angle θ2 vs Incident θ1 (degrees)';
      summary = `Incident θ1: ${a}° → Refracted θ2 in iron: ${activeTh2.toFixed(2)}° (normal alignment)`;
    }
    return {rows, summary, curveLabel};
  }

  function drawCanvas(canvas, rows, curveLabel) {
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
    ctx.font = '12px sans-serif';
    ctx.fillText(curveLabel, pad, 25);
    ctx.fillText(minX.toPrecision(3), pad, H - 20);
    ctx.fillText(maxX.toPrecision(3), W - pad - 30, H - 20);
    ctx.fillText(fmt(maxY), 8, pad + 10);
    ctx.fillText(fmt(minY), 8, H - pad);
  }

  var MODELS = [];
"""
    for idx, unit, title, desc, p1_label, p1_min, p1_max, p1_step, p1_def, p2_label, p2_min, p2_max, p2_step, p2_def in emf_models_meta:
        emf_js += f"""
  MODELS.push({{
    idx: {idx},
    unit: {unit},
    html: '<div class="sim-header"><span class="badge">Model {idx:02d}</span><h3>{title}</h3><p>{desc}</p></div>' +
          '<div class="sim-controls">' +
            '<label for="p1-{idx}">{p1_label}: <output id="v1-{idx}"></output>' +
              '<input id="p1-{idx}" type="range" min="{p1_min}" max="{p1_max}" step="{p1_step}" value="{p1_def}"/>' +
            '</label>' +
            '<label for="p2-{idx}">{p2_label}: <output id="v2-{idx}"></output>' +
              '<input id="p2-{idx}" type="range" min="{p2_min}" max="{p2_max}" step="{p2_step}" value="{p2_def}"/>' +
            '</label>' +
          '</div>' +
          '<div class="plot"><canvas id="canvas-{idx}" width="680" height="260" role="img" aria-label="Electromagnetic field curve"></canvas></div>' +
          '<div class="readouts"><div class="stat-box"><output id="summary-{idx}">-</output></div></div>',
    init: function(card) {{
      try {{
        var p1 = card.querySelector('#p1-{idx}');
        var p2 = card.querySelector('#p2-{idx}');
        var v1 = card.querySelector('#v1-{idx}');
        var v2 = card.querySelector('#v2-{idx}');
        var canvas = card.querySelector('#canvas-{idx}');
        var summary = card.querySelector('#summary-{idx}');
        function update() {{
          var a = Number(p1.value), b = Number(p2.value);
          if (v1) v1.textContent = String(a);
          if (v2) v2.textContent = String(b);
          var res = computeModel({idx}, a, b);
          if (summary) summary.textContent = res.summary;
          if (canvas) drawCanvas(canvas, res.rows, res.curveLabel);
        }}
        p1.addEventListener('input', update);
        p2.addEventListener('input', update);
        update();
      }} catch (err) {{
        console.warn('Electromagnetic Field Theory I sim error in model {idx}:', err);
      }}
    }}
  }});"""

    emf_js += ENGINE_FOOTER
    emf_path = os.path.join(ROOT, 'src', 'subjects', 'electrical-and-electronics-engineering', 'electromagnetic-field-theory-i', 'electromagnetic-field-theory-i-sims.js')
    os.makedirs(os.path.dirname(emf_path), exist_ok=True)
    with open(emf_path, 'w', encoding='utf-8') as f:
        f.write(emf_js)
    print(f"Wrote {emf_path}")

print("Batch 1 simulation suites successfully generated!")
