import zipfile, re, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARCHIVE = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793628498354_3f84ba9b.zip'

print("Generating Batch 1 Civil Engineering Simulation Suites...")

def get_engine_footer(book_name, total_units=8):
    return f"""
  if (!window.SimulationEngine) window.SimulationEngine = {{}};
  window.SimulationEngine.initSimulation = function(containerId, simType) {{
    var container = document.getElementById(containerId) ||
                    document.getElementById('sim-container') ||
                    document.querySelector('.simulation-slot');
    if (!container) return;
    container.innerHTML = '';
    var unitNum = 1;
    if (simType) {{
      var m = simType.match(/(\\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    }} else {{
      var bMatch = document.body.dataset.chapterIndex;
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') unitNum = parseInt(bMatch, 10) + 1;
      else {{
        var pMatch = window.location.pathname.match(/chapter-(\\d+)/);
        if (pMatch) unitNum = parseInt(pMatch[1], 10);
      }}
    }}
    if (isNaN(unitNum) || unitNum < 1 || unitNum > {total_units}) unitNum = 1;
    var modelsForUnit = MODELS.filter(function(m) {{ return m.unit === unitNum; }});
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.filter(function(m) {{ return m.unit === 1; }});
    modelsForUnit.forEach(function(m) {{
      var card = document.createElement('section');
      card.className = 'ce-sim-card';
      card.setAttribute('aria-label', 'Interactive Simulation ' + m.idx);
      card.id = 'sim-card-' + m.idx;
      card.innerHTML = m.html;
      container.appendChild(card);
      m.init(card);
    }});
  }};

  if (typeof document !== 'undefined') {{
    var autoInit = function() {{
      var slot = document.getElementById('sim-container') || document.querySelector('.simulation-slot');
      if (slot && slot.children.length === 0) {{
        window.SimulationEngine.initSimulation(slot.id || 'sim-container');
      }}
    }};
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', autoInit);
    }} else {{
      autoInit();
    }}
  }}
}})(typeof window === 'undefined' ? globalThis : window);
"""

with zipfile.ZipFile(ARCHIVE, 'r') as z:
    # =========================================================================
    # 1. Civil Engineering Statics (8 units, 8 simulations)
    # =========================================================================
    print("Building civil-engineering-statics-sims.js...")
    statics_sim_meta = [
        {"kind": "trapezoid", "unit": 1, "title": "Distributed Load Resultant", "desc": "Equilibrium reduction of trapezoidal distributed line loads into a single resultant force and its centroidal line of action."},
        {"kind": "beam", "unit": 2, "title": "Simply Supported Beam Equilibrium", "desc": "Calculation of vertical support reactions under combined point actions and uniform distributed loads."},
        {"kind": "truss", "unit": 3, "title": "Roof Truss Apex Equilibrium", "desc": "Method of joints resolution at a symmetrical two-bar pin-jointed truss apex carrying a centric downward action."},
        {"kind": "cable", "unit": 4, "title": "Parabolic Cable Tension and Sag", "desc": "Horizontal tension, vertical anchor reaction, and maximum tangent tension for a uniformly loaded flexible cable."},
        {"kind": "section", "unit": 5, "title": "Composite Section Centroid and Inertia", "desc": "Parallel-axis theorem calculation of centroid elevation and second moment of area for a structural T-section."},
        {"kind": "stability", "unit": 6, "title": "Friction, Sliding and Overturning Stability", "desc": "Equilibrium comparison of available Coulomb interface friction and overturning moments on a gravity retaining block."},
        {"kind": "lever", "unit": 7, "title": "Virtual Work Equilibrium of a Lever", "desc": "Principle of virtual work equating virtual work of effort and resistance under kinematically admissible virtual displacements."},
        {"kind": "stage", "unit": 8, "title": "Stagewise Construction Load Balance", "desc": "Superposition of permanent dead actions and transient construction loads during sequential erection stages."}
    ]

    statics_models_js = []
    for i, meta in enumerate(statics_sim_meta, 1):
        html_path = f"OpenSTEM-Civil-Engineering/books/civil-engineering-statics/simulations/simulation-0{i}.html"
        raw_html = z.read(html_path).decode('utf-8', errors='ignore')
        ctrl_match = re.search(r'<section class="sim-controls">([\s\S]*?)</section>', raw_html)
        controls_html = ctrl_match.group(1).strip() if ctrl_match else ""

        statics_models_js.append({
            "idx": i,
            "unit": meta["unit"],
            "kind": meta["kind"],
            "title": meta["title"],
            "desc": meta["desc"],
            "controls": controls_html
        })

    statics_js = """/* Civil Engineering Statics Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n) { return Number.isFinite(n) ? n.toFixed(3) : 'not defined'; }
  function line(a, b, c, d, color) { color = color || '#21697b'; return '<line x1="' + a + '" y1="' + b + '" x2="' + c + '" y2="' + d + '" stroke="' + color + '" stroke-width="3"/>'; }
  function text(x, y, t) { return '<text x="' + x + '" y="' + y + '" font-size="12" fill="#1e293b">' + t + '</text>'; }

  var MODELS = [];
"""
    for m in statics_models_js:
        kind = m['kind']
        card_html = (
            f"<div class=\\\"sim-header\\\"><span class=\\\"badge\\\">Model 0{m['idx']} · Unit {m['unit']}</span>"
            f"<h3>{m['title']}</h3><p>{m['desc']}</p></div>"
            f"<section class=\\\"sim-controls\\\">{m['controls']}</section>"
            f"<div class=\\\"diagram\\\" style=\\\"margin:1rem 0;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:0.5rem;\\\"></div>"
            f"<div class=\\\"readouts\\\"><div class=\\\"stat-box out\\\" style=\\\"width:100%;white-space:pre-line;line-height:1.6;font-family:monospace;font-size:0.875rem;\\\"></div></div>"
        )
        card_html_escaped = json.dumps(card_html)
        statics_js += f"""
  MODELS.push({{
    idx: {m['idx']},
    unit: {m['unit']},
    kind: '{kind}',
    html: {card_html_escaped},
    init: function(card) {{
      try {{
        var ranges = Array.prototype.slice.call(card.querySelectorAll('input[type="range"]'));
        var diagramEl = card.querySelector('.diagram');
        var outEl = card.querySelector('.out');
        function rec() {{
          var p = {{}};
          ranges.forEach(function(r) {{
            p[r.id] = Number(r.value);
            var vEl = card.querySelector('#v_' + r.id);
            if (vEl) vEl.textContent = r.value;
          }});
          var L = p.L || 0, a = Math.min(p.a || 0, L);
          var svg = '', result = '';
          var kind = '{kind}';
          if (kind === 'trapezoid') {{
            var W = (p.q1 + p.q2) * L / 2;
            var xx = (p.q1 + p.q2) > 0 ? L * (p.q1 + 2 * p.q2) / (3 * (p.q1 + p.q2)) : 0;
            result = 'Equivalent downward resultant W = ' + f(W) + ' kN\\nLocation x̄ = ' + f(xx) + ' m from left\\nVerification check: uniform loading yields x̄ = L/2';
            svg = '<svg viewBox="0 0 640 240"><polygon points="80,190 550,190 550,' + (185 - 12 * p.q2) + ' 80,' + (185 - 12 * p.q1) + '" fill="#d5edf2" stroke="#287589" stroke-width="3"/>' +
                  line(80, 190, 550, 190) + text(85, 220, 'Left q1=' + p.q1 + ' kN/m') + text(450, 220, 'Right q2=' + p.q2 + ' kN/m') + text(260, 44, 'W=' + f(W) + ' kN at x=' + f(xx) + ' m') + '</svg>';
          }} else if (kind === 'beam') {{
            var RA = p.w * L / 2 + p.P * (L - a) / (L || 1);
            var RB = p.w * L / 2 + p.P * a / (L || 1);
            result = 'Left support reaction RA = ' + f(RA) + ' kN\\nRight support reaction RB = ' + f(RB) + ' kN\\nGlobal equilibrium check: RA + RB = ' + f(RA + RB) + ' kN = wL + P';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 150, 560, 150) + '<polygon points="75,152 60,175 90,175" fill="#2f7184"/><polygon points="560,152 545,175 575,175" fill="#2f7184"/>' +
                  line(75 + 485 * a / (L || 1), 50, 75 + 485 * a / (L || 1), 140, '#b06546') + text(75 + 485 * a / (L || 1), 38, 'P=' + p.P + ' kN') + text(230, 190, 'w=' + p.w + ' kN/m') +
                  text(70, 215, 'RA=' + f(RA)) + text(505, 215, 'RB=' + f(RB)) + '</svg>';
          }} else if (kind === 'truss') {{
            var th = p.theta * Math.PI / 180;
            var F = p.P / (2 * Math.sin(th));
            result = 'Axial compression magnitude in symmetrical diagonals = ' + f(F) + ' kN\\nVertical support reaction per joint = ' + f(p.P / 2) + ' kN\\nDeterminacy note: static equilibrium of concurrent joint system.';
            var dx = 190 * Math.cos(th), dy = 190 * Math.sin(th);
            svg = '<svg viewBox="0 0 640 240">' + line(320 - dx, 205, 320, 205 - dy) + line(320, 205 - dy, 320 + dx, 205) + line(320, 30, 320, 196, '#b06546') +
                  text(325, 25, 'P=' + p.P + ' kN') + text(48, 232, 'Diagonal axial force |N| = ' + f(F) + ' kN') + '</svg>';
          }} else if (kind === 'cable') {{
            var H = p.w * L * L / (8 * (p.f || 0.1));
            var V = p.w * L / 2;
            var T = Math.hypot(H, V);
            result = 'Horizontal cable tension component H = ' + f(H) + ' kN\\nVertical reaction at each anchor V = ' + f(V) + ' kN\\nMaximum end tension T = ' + f(T) + ' kN\\nFormulation: uniform vertical dead load per horizontal metre.';
            var d = 'M 70 65 Q 320 ' + (65 + p.f * 14) + ' 570 65';
            svg = '<svg viewBox="0 0 640 240"><path d="' + d + '" fill="none" stroke="#2a788c" stroke-width="4"/>' + line(70, 65, 70, 220) + line(570, 65, 570, 220) +
                  text(230, 200, 'Sag f=' + p.f + ' m') + text(230, 226, 'H=' + f(H) + ' kN') + '</svg>';
          }} else if (kind === 'section') {{
            var hw = p.h - p.tf;
            var Af = p.b * p.tf, Aw = p.tw * hw, A = Af + Aw;
            var yf = p.h - p.tf / 2, yw = hw / 2;
            var y = (Af * yf + Aw * yw) / (A || 1);
            var If = p.b * Math.pow(p.tf, 3) / 12 + Af * Math.pow(yf - y, 2);
            var Iw = p.tw * Math.pow(hw, 3) / 12 + Aw * Math.pow(yw - y, 2);
            var I = If + Iw;
            result = 'Total cross-sectional area A = ' + f(A) + ' mm²\\nCentroid elevation ȳ = ' + f(y) + ' mm from bottom fiber\\nCentroidal second moment of area Ixx = ' + f(I) + ' mm⁴\\nFormulation: parallel-axis theorem summation.';
            var fx = 320 - p.b * 0.6, fy = 215 - p.h * 0.6;
            svg = '<svg viewBox="0 0 640 240"><rect x="' + (320 - p.tw * 0.6 / 2) + '" y="' + (fy + p.tf * 0.6) + '" width="' + (p.tw * 0.6) + '" height="' + (hw * 0.6) + '" fill="#9fcdd8"/>' +
                  '<rect x="' + fx + '" y="' + fy + '" width="' + (p.b * 0.6) + '" height="' + (p.tf * 0.6) + '" fill="#367f92"/>' +
                  line(120, 215 - y * 0.6, 520, 215 - y * 0.6, '#b06546') + text(340, 215 - y * 0.6 - 7, 'Centroid ȳ=' + f(y) + ' mm') + '</svg>';
          }} else if (kind === 'stability') {{
            var F = p.mu * p.W, ms = p.W * p.B / 2, mo = p.H * p.h;
            var rs = F / (p.H || 1), rm = ms / (mo || 1);
            result = 'Available interface friction capacity μW = ' + f(F) + ' kN\\nSliding safety ratio μW / H = ' + f(rs) + '\\nStabilizing gravity moment W·B/2 = ' + f(ms) + ' kN·m\\nOverturning moment H·h = ' + f(mo) + ' kN·m\\nOverturning safety ratio = ' + f(rm) + '\\nEducational screening: assumes rigid footing contact.';
            svg = '<svg viewBox="0 0 640 240"><rect x="180" y="75" width="250" height="130" fill="#b9dce5" stroke="#34788a"/>' +
                  line(95, 190, 520, 190) + line(400, 99, 510, 99, '#b06546') + text(400, 79, 'H=' + p.H + ' kN') + text(260, 50, 'W=' + p.W + ' kN') + text(100, 231, 'Sliding ratio = ' + f(rs)) + '</svg>';
          }} else if (kind === 'lever') {{
            var effort = p.Q * p.b / (p.a || 1);
            result = 'Ideal equilibrium effort = Q·b/a = ' + f(effort) + ' kN\\nKinematic displacement ratio δx_effort / δx_load = a/b = ' + f(p.a / (p.b || 1)) + '\\nPrinciple of virtual work: effort × δx_effort = resistance × δx_load.';
            svg = '<svg viewBox="0 0 640 240">' + line(80, 135, 560, 135) + '<polygon points="310,137 290,177 330,177" fill="#377b8c"/>' +
                  line(100, 35, 100, 125, '#b06546') + line(520, 50, 520, 130, '#21697b') + text(70, 22, 'Effort = ' + f(effort) + ' kN') + text(484, 32, 'Q=' + p.Q + ' kN') + '</svg>';
          }} else if (kind === 'stage') {{
            var base = p.dead * L / 2, live = p.temp * L / 2;
            var RA = base + live + p.P * (L - a) / (L || 1);
            var RB = base + live + p.P * a / (L || 1);
            result = 'Stage A (permanent dead load): RA = RB = ' + f(base) + ' kN\\nStage B (transient erection loads): RA = ' + f(RA) + ' kN, RB = ' + f(RB) + ' kN\\nTotal Stage B vertical action = ' + f((p.dead + p.temp) * L + p.P) + ' kN.';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 140, 560, 140) + line(75, 120, 560, 120, '#5c94a4') + line(75 + 485 * a / (L || 1), 38, 75 + 485 * a / (L || 1), 130, '#b06546') +
                  text(85, 50, 'Dead=' + p.dead + ' kN/m') + text(270, 70, 'Temp=' + p.temp + ' kN/m') + text(85, 210, 'RA=' + f(RA)) + text(470, 210, 'RB=' + f(RB)) + '</svg>';
          }}
          if (diagramEl) diagramEl.innerHTML = svg;
          if (outEl) outEl.textContent = result;
        }}
        ranges.forEach(function(r) {{ r.addEventListener('input', rec); }});
        rec();
      }} catch (err) {{
        console.warn('Statics sim error in model ' + m.idx + ':', err);
      }}
    }}
  }});"""

    statics_js += get_engine_footer('Civil Engineering Statics', 8)
    statics_dest = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'civil-engineering-statics', 'civil-engineering-statics-sims.js')
    with open(statics_dest, 'w', encoding='utf-8') as f:
        f.write(statics_js)
    print(f"Wrote {statics_dest}")

    # =========================================================================
    # 2. Strength of Materials (9 units, 13 simulation labs)
    # =========================================================================
    print("Building strength-of-materials-sims.js...")
    som_engine_src = z.read('OpenSTEM-Civil-Engineering/books/strength-of-materials/assets/lab-engine.js').decode('utf-8', errors='ignore')

    # Extract definitions and controls
    defs_match = re.search(r'const definitions = (\{[\s\S]*?\});\s*const controls = (\{[\s\S]*?\});', som_engine_src)
    defs_json_str = defs_match.group(1)
    controls_json_str = defs_match.group(2)

    # Extract calculation function
    calc_src = som_engine_src[som_engine_src.find('function calc()'):som_engine_src.find('function createEl(')]
    calc_src = calc_src.replace('function calc(){', 'function calc(labKey, v){')
    calc_src = calc_src.replace('switch(document.body.dataset.lab){', 'switch(labKey){')

    som_lab_to_unit = {
        'axial': 1,
        'material': 3,
        'torsion': 4,
        'beamvm': 5,
        'deflection': 6,
        'section': 1,
        'mohr': 7,
        'combined': 7,
        'buckling': 8,
        'pressure': 9,
        'gauge': 2,
        'fatigue': 9,
        'beamshear': 5
    }

    som_js = f"""/* Strength of Materials Interactive Simulation Suite */
(function(window) {{
  'use strict';

  var svgNS = 'http://www.w3.org/2000/svg';
  var palette = ['#38bdf8', '#34d399', '#f472b6', '#facc15', '#a78bfa', '#fb923c'];
  var escapeHTML = function(s) {{ return String(s).replace(/[&<>"']/g, function(c) {{ return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]; }}); }};
  var f = function(n, d) {{ d = (d === undefined) ? 3 : d; return !Number.isFinite(n) ? '—' : Math.abs(n) >= 1e5 ? n.toExponential(2) : Number(n.toFixed(d)).toLocaleString('en-US', {{maximumFractionDigits: d}}); }};
  var clamp = function(x, a, b) {{ return Math.max(a, Math.min(b, x)); }};
  var arange = function(a, b, n) {{ return Array.from({{length: n}}, function(_, i) {{ return a + (b - a) * i / (n - 1); }}); }};
  var metric = function(k, val, unit, info) {{ return [k, val, unit || '', info || '']; }};

  var definitions = {defs_json_str};
  var controls = {controls_json_str};

  {calc_src}

  function createEl(tag, attrs, txt) {{
    var el = document.createElementNS(svgNS, tag);
    for (var k in attrs) el.setAttribute(k, attrs[k]);
    if (txt !== undefined) el.textContent = txt;
    return el;
  }}

  var MODELS = [];
  var labKeys = Object.keys(definitions);
  var labUnits = {json.dumps(som_lab_to_unit)};

  labKeys.forEach(function(key, idx) {{
    var def = definitions[key];
    var unit = labUnits[key] || 1;
    var controlsHtml = def.keys.map(function(k) {{
      var c = controls[k];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="' + key + '_' + k + '">' + c.label + ' <span id="v_' + key + '_' + k + '" style="font-weight:700;color:#d97706;">' + c.val + ' ' + c.unit + '</span></label>' +
             '<input id="' + key + '_' + k + '" data-key="' + k + '" type="range" min="' + c.min + '" max="' + c.max + '" step="' + c.step + '" value="' + c.val + '" style="width:100%;accent-color:#d97706;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge">Lab ' + (idx + 1) + ' · Unit ' + unit + '</span><h3>' + def.title + '</h3></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<svg class="sim-plot" viewBox="0 0 840 430" style="width:100%;height:auto;background:#091d2f;border-radius:8px;display:block;"></svg>' +
               '<div class="model-note" style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;font-style:italic;"></div>';

    MODELS.push({{
      idx: idx + 1,
      unit: unit,
      key: key,
      html: html,
      init: function(card) {{
        try {{
          var v = {{}};
          def.keys.forEach(function(k) {{ v[k] = controls[k].val; }});
          var plotSvg = card.querySelector('.sim-plot');
          var metricsEl = card.querySelector('.metrics');
          var noteEl = card.querySelector('.model-note');

          function drawPlotLocal(r) {{
            if (!plotSvg) return;
            while (plotSvg.firstChild) plotSvg.removeChild(plotSvg.firstChild);
            var left = 68, right = 770, top = 30, bottom = 355, w = right - left, h = bottom - top;
            var all = [];
            for (var si = 0; si < r.series.length; si++) {{
              var s = r.series[si];
              var rows = s.data !== undefined ? s.data : r.rows;
              for (var ri = 0; ri < rows.length; ri++) {{
                var row = rows[ri];
                var xx = r.xy ? row[s.xj !== undefined ? s.xj : 1] : row[0];
                var yy = row[s.j];
                if (Number.isFinite(xx) && Number.isFinite(yy)) all.push([xx, yy]);
              }}
            }}
            for (var mi = 0; mi < (r.markers || []).length; mi++) all.push([r.markers[mi].x, r.markers[mi].y]);
            if (!all.length) return;
            var xmin = Math.min.apply(null, all.map(function(p) {{ return p[0]; }}));
            var xmax = Math.max.apply(null, all.map(function(p) {{ return p[0]; }}));
            var ymin = Math.min.apply(null, all.map(function(p) {{ return p[1]; }}));
            var ymax = Math.max.apply(null, all.map(function(p) {{ return p[1]; }}));
            if (Math.abs(xmax - xmin) < 1e-12) {{ xmin -= 1; xmax += 1; }}
            if (Math.abs(ymax - ymin) < 1e-12) {{ ymin -= 1; ymax += 1; }}
            var px = (xmax - xmin) * 0.04, py = (ymax - ymin) * 0.13;
            xmin -= px; xmax += px; ymin -= py; ymax += py;
            if (r.xy) {{
              var xmid = (xmin + xmax) / 2, ymid = (ymin + ymax) / 2;
              var unitsPerPixel = Math.max((xmax - xmin) / w, (ymax - ymin) / h);
              xmin = xmid - unitsPerPixel * w / 2; xmax = xmid + unitsPerPixel * w / 2;
              ymin = ymid - unitsPerPixel * h / 2; ymax = ymid + unitsPerPixel * h / 2;
            }}
            var X = function(a) {{ return left + (a - xmin) / (xmax - xmin || 1) * w; }};
            var Y = function(a) {{ return bottom - (a - ymin) / (ymax - ymin || 1) * h; }};

            plotSvg.appendChild(createEl('rect', {{x: left, y: top, width: w, height: h, fill: '#091d2f', rx: '6'}}));
            for (var gi = 0; gi <= 5; gi++) {{
              var gx = left + (right - left) * gi / 5, gy = top + (bottom - top) * gi / 5;
              plotSvg.appendChild(createEl('line', {{x1: gx, y1: top, x2: gx, y2: bottom, stroke: '#27465c', 'stroke-width': 1}}));
              plotSvg.appendChild(createEl('line', {{x1: left, y1: gy, x2: right, y2: gy, stroke: '#27465c', 'stroke-width': 1}}));
              plotSvg.appendChild(createEl('text', {{x: gx, y: bottom + 21, fill: '#b7cad7', 'font-size': 12, 'text-anchor': 'middle'}}, f(xmin + (xmax - xmin) * gi / 5, 2)));
              plotSvg.appendChild(createEl('text', {{x: left - 12, y: gy + 4, fill: '#b7cad7', 'font-size': 12, 'text-anchor': 'end'}}, f(ymax - (ymax - ymin) * gi / 5, 2)));
            }}
            for (var si2 = 0; si2 < r.series.length; si2++) {{
              var s2 = r.series[si2];
              var rows2 = s2.data !== undefined ? s2.data : r.rows;
              var pts = rows2.filter(function(row) {{
                return Number.isFinite(r.xy ? row[s2.xj !== undefined ? s2.xj : 1] : row[0]) && Number.isFinite(row[s2.j]);
              }}).map(function(row) {{
                return X(r.xy ? row[s2.xj !== undefined ? s2.xj : 1] : row[0]) + ',' + Y(row[s2.j]);
              }}).join(' ');
              if (pts) plotSvg.appendChild(createEl('polyline', {{points: pts, fill: 'none', stroke: palette[si2 % palette.length], 'stroke-width': 3, 'stroke-linejoin': 'round', 'stroke-linecap': 'round'}}));
            }}
            for (var mi2 = 0; mi2 < (r.markers || []).length; mi2++) {{
              var m2 = r.markers[mi2];
              plotSvg.appendChild(createEl('circle', {{cx: X(m2.x), cy: Y(m2.y), r: 7, fill: '#f97316', stroke: 'white', 'stroke-width': 1.5}}));
              plotSvg.appendChild(createEl('text', {{x: X(m2.x) + 10, y: Y(m2.y) - 12, fill: '#fed7aa', 'font-size': 14}}, m2.label));
            }}
            plotSvg.appendChild(createEl('text', {{x: 430, y: 408, fill: '#dceaf3', 'font-size': 14, 'text-anchor': 'middle'}}, r.x));
            plotSvg.appendChild(createEl('text', {{transform: 'translate(16 194) rotate(-90)', fill: '#dceaf3', 'font-size': 14, 'text-anchor': 'middle'}}, r.y));
          }}

          function updateLab() {{
            var inputs = card.querySelectorAll('input[type="range"]');
            inputs.forEach(function(inp) {{
              var k = inp.dataset.key;
              v[k] = Number(inp.value);
              var lbl = card.querySelector('#v_' + key + '_' + k);
              if (lbl) lbl.textContent = inp.value + ' ' + controls[k].unit;
            }});
            var res = calc(key, v);
            if (metricsEl) {{
              metricsEl.innerHTML = res.metrics.map(function(x) {{
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + escapeHTML(x[0]) + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + (typeof x[1] === 'string' ? escapeHTML(x[1]) : f(x[1], 3)) + ' ' + escapeHTML(x[2]) + '</output></div>';
              }}).join('');
            }}
            if (noteEl) noteEl.textContent = 'Model boundary: ' + res.note;
            drawPlotLocal(res);
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', updateLab);
          }});
          updateLab();
        }} catch (err) {{
          console.warn('Strength of Materials sim error in lab ' + key + ':', err);
        }}
      }}
    }});
  }});
"""
    som_js += get_engine_footer('Strength of Materials', 9)
    som_dest = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'strength-of-materials', 'strength-of-materials-sims.js')
    with open(som_dest, 'w', encoding='utf-8') as f:
        f.write(som_js)
    print(f"Wrote {som_dest}")

    # =========================================================================
    # 3. Structural Analysis I (8 units, 13 simulation labs)
    # =========================================================================
    print("Building structural-analysis-i-sims.js...")
    sa1_lab_src = z.read('OpenSTEM-Civil-Engineering/books/structural-analysis-i/assets/lab.js').decode('utf-8', errors='ignore')

    # Extract model logic
    m_start = sa1_lab_src.find('switch(lab){')
    m_end = sa1_lab_src.find('return {points,out,equation,explain,xLabel,yLabel}')
    model_body = sa1_lab_src[m_start:m_end].replace('switch(lab){', 'switch(labId){')

    sa1_lab_files = sorted([n for n in z.namelist() if n.startswith('OpenSTEM-Civil-Engineering/books/structural-analysis-i/labs/') and n.endswith('.html')])
    sa1_labs_data = []
    sa1_lab_to_unit = {
        'beam-reactions': 1,
        'shear-moment': 1,
        'beam-deflection': 2,
        'triangle-truss': 3,
        'truss-displacement': 3,
        'three-hinged-arch': 4,
        'cable-sag': 4,
        'cantilever-virtual': 5,
        'moment-influence': 6,
        'axle-train': 6,
        'propped-cantilever': 7,
        'moving-envelope': 8,
        'verification-convergence': 8
    }

    for fpath in sa1_lab_files:
        html_c = z.read(fpath).decode('utf-8', errors='ignore')
        cfg_m = re.search(r'<script type="application/json" id="lab-config">([\s\S]*?)</script>', html_c)
        if not cfg_m: continue
        cfg = json.loads(cfg_m.group(1))
        lab_m = re.search(r'data-lab="([^"]+)"', html_c)
        lab_id = lab_m.group(1) if lab_m else os.path.basename(fpath).replace('.html', '')
        title_m = re.search(r'<h1>(.*?)</h1>', html_c)
        title = title_m.group(1) if title_m else cfg.get('name', lab_id)
        hero_p = re.search(r'<div class="hero">[\s\S]*?<p>(.*?)</p>', html_c)
        desc = hero_p.group(1) if hero_p else ""
        
        sa1_labs_data.append({
            'id': lab_id,
            'title': title,
            'desc': desc,
            'config': cfg,
            'unit': sa1_lab_to_unit.get(lab_id, 1)
        })

    sa1_js = f"""/* Structural Analysis I Interactive Simulation Suite */
(function(window) {{
  'use strict';

  var f = function(n, k) {{ k = (k === undefined) ? 3 : k; return Number(n).toLocaleString('en-US', {{maximumFractionDigits: k}}); }};
  var line = function(n, fn) {{ return Array.from({{length: n + 1}}, function(_, i) {{ return {{x: i / n, y: fn(i / n)}}; }}); }};
  var arrsum = function(a) {{ return a.reduce(function(x, y) {{ return x + y; }}, 0); }};
  var momentOrd = function(L, c, z) {{ return z <= c ? z * (L - c) / L : c * (L - z) / L; }};

  function runModel(labId, vals) {{
    var v = vals, points = [], out = [], equation = '', explain = '', xLabel = 'Position', yLabel = 'Response';
    var add = function(name, unit, value) {{ out.push({{name: name, unit: unit, value: value}}); }};
    var getBeam = function() {{
      var L = v.L || 8, P = v.P !== undefined ? v.P : 28, a = v.a !== undefined ? v.a : 0.45, w = v.w !== undefined ? v.w : 3;
      var loc = a * L;
      var RA = P * (L - loc) / L + w * L / 2, RB = P * loc / L + w * L / 2;
      return {{
        L: L, P: P, a: loc, w: w, RA: RA, RB: RB,
        M: function(x) {{ return RA * x - w * x * x / 2 - P * Math.max(0, x - loc); }},
        V: function(x) {{ return RA - w * x - (x >= loc ? P : 0); }}
      }};
    }};

    {model_body}

    return {{points: points, out: out, equation: equation, explain: explain, xLabel: xLabel, yLabel: yLabel}};
  }}

  var MODELS = [];
  var labsConfig = {json.dumps(sa1_labs_data)};

  labsConfig.forEach(function(labItem, idx) {{
    var labId = labItem.id;
    var unit = labItem.unit;
    var cfg = labItem.config;

    var controlsHtml = cfg.controls.map(function(c) {{
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="' + labId + '_' + c.id + '">' + c.name + ' <span id="v_' + labId + '_' + c.id + '" style="font-weight:700;color:#d97706;">' + c.initial + ' ' + c.unit + '</span></label>' +
             '<input id="' + labId + '_' + c.id + '" data-cid="' + c.id + '" type="range" min="' + c.min + '" max="' + c.max + '" step="' + c.step + '" value="' + c.initial + '" style="width:100%;accent-color:#d97706;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + (idx + 1) + ' · Unit ' + unit + '</span><h3>' + labItem.title + '</h3><p>' + labItem.desc + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<svg class="canvas" viewBox="0 0 760 380" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg>' +
               '<div class="equation" style="font-family:monospace;font-size:0.875rem;background:#f1f5f9;padding:0.75rem;border-radius:6px;margin-top:0.75rem;color:#0f172a;"></div>' +
               '<p class="explain" style="font-size:0.8125rem;color:#475569;margin-top:0.5rem;"></p>';

    MODELS.push({{
      idx: idx + 1,
      unit: unit,
      id: labId,
      html: html,
      init: function(card) {{
        try {{
          var vals = {{}};
          cfg.controls.forEach(function(c) {{ vals[c.id] = c.initial; }});

          var svgEl = card.querySelector('.canvas');
          var metricsEl = card.querySelector('.metrics');
          var eqEl = card.querySelector('.equation');
          var expEl = card.querySelector('.explain');

          function renderChart(points, xLabel, yLabel) {{
            if (!svgEl) return;
            var W = 760, H = 380, margin = {{top: 24, right: 30, bottom: 50, left: 60}};
            var xs = points.map(function(p) {{ return p.x; }}), ys = points.map(function(p) {{ return p.y; }});
            var xMin = Math.min.apply(null, xs), xMax = Math.max.apply(null, xs);
            var yMin = Math.min.apply(null, ys), yMax = Math.max.apply(null, ys);
            if (xMin === xMax) {{ xMin -= 1; xMax += 1; }}
            if (yMin === yMax) {{ yMin -= 1; yMax += 1; }}
            var yPad = (yMax - yMin) * 0.1 || 1; yMin -= yPad; yMax += yPad;
            var tx = function(x) {{ return margin.left + (x - xMin) / (xMax - xMin) * (W - margin.left - margin.right); }};
            var ty = function(y) {{ return H - margin.bottom - (y - yMin) / (yMax - yMin) * (H - margin.top - margin.bottom); }};
            var path = points.map(function(p, i) {{ return (i ? 'L' : 'M') + tx(p.x).toFixed(2) + ',' + ty(p.y).toFixed(2); }}).join(' ');

            var s = '<rect width="' + W + '" height="' + H + '" fill="#ffffff" rx="6"/>';
            for (var i = 0; i <= 4; i++) {{
              var y = yMin + (yMax - yMin) * i / 4, yy = ty(y);
              s += '<line x1="' + margin.left + '" x2="' + (W - margin.right) + '" y1="' + yy + '" y2="' + yy + '" stroke="#e2e8f0"/>' +
                   '<text x="' + (margin.left - 8) + '" y="' + (yy + 4) + '" font-size="11" fill="#64748b" text-anchor="end">' + f(y, 2) + '</text>';
            }}
            for (var j = 0; j <= 5; j++) {{
              var x = xMin + (xMax - xMin) * j / 5, xx = tx(x);
              s += '<line x1="' + xx + '" x2="' + xx + '" y1="' + margin.top + '" y2="' + (H - margin.bottom) + '" stroke="#e2e8f0"/>' +
                   '<text x="' + xx + '" y="' + (H - margin.bottom + 20) + '" text-anchor="middle" fill="#64748b" font-size="11">' + f(x, 2) + '</text>';
            }}
            s += '<path d="' + path + '" stroke="#d97706" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" fill="none"/>' +
                 '<text x="' + (W / 2) + '" y="' + (H - 10) + '" font-size="13" fill="#1e293b" text-anchor="middle">' + xLabel + '</text>' +
                 '<text x="18" y="' + (H / 2) + '" transform="rotate(-90 18 ' + (H / 2) + ')" fill="#1e293b" font-size="13" text-anchor="middle">' + yLabel + '</text>';
            svgEl.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
            svgEl.innerHTML = s;
          }}

          function update() {{
            cfg.controls.forEach(function(c) {{
              var inp = card.querySelector('#' + labId + '_' + c.id);
              if (inp) vals[c.id] = Number(inp.value);
              var lbl = card.querySelector('#v_' + labId + '_' + c.id);
              if (lbl) lbl.textContent = f(vals[c.id]) + ' ' + c.unit;
            }});
            var cur = runModel(labId, vals);
            renderChart(cur.points, cur.xLabel, cur.yLabel);
            if (eqEl) eqEl.textContent = cur.equation;
            if (expEl) expEl.textContent = cur.explain;
            if (metricsEl) {{
              metricsEl.innerHTML = cur.out.map(function(m) {{
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + m.name + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + (typeof m.value === 'number' ? f(m.value, 4) : m.value) + ' ' + m.unit + '</output></div>';
              }}).join('');
            }}
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', update);
          }});
          update();
        }} catch (err) {{
          console.warn('Structural Analysis I sim error in lab ' + labId + ':', err);
        }}
      }}
    }});
  }});
"""
    sa1_js += get_engine_footer('Structural Analysis I', 8)
    sa1_dest = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'structural-analysis-i', 'structural-analysis-i-sims.js')
    with open(sa1_dest, 'w', encoding='utf-8') as f:
        f.write(sa1_js)
    print(f"Wrote {sa1_dest}")

    # =========================================================================
    # 4. Structural Analysis II (8 units, 15 simulation models)
    # =========================================================================
    print("Building structural-analysis-ii-sims.js...")
    sa2_labs_src = z.read('OpenSTEM-Civil-Engineering/books/structural-analysis-ii/assets/labs.js').decode('utf-8', errors='ignore')

    # Extract LABS array
    labs_str = sa2_labs_src[sa2_labs_src.find('const LABS = ['):sa2_labs_src.find('function gaussian(')]
    # Extract helpers and solve
    helpers_str = sa2_labs_src[sa2_labs_src.find('function gaussian('):sa2_labs_src.find('function solve()')]
    solve_and_plots = sa2_labs_src[sa2_labs_src.find('function solve()'):sa2_labs_src.find('function update()')]

    sa2_js = f"""/* Structural Analysis II Interactive Simulation Suite */
(function(window) {{
  'use strict';

  {labs_str}
  {helpers_str}
  {solve_and_plots}

  var MODELS = [];

  LABS.forEach(function(labItem, idx) {{
    var unit = labItem.u;
    var controlsHtml = labItem.inputs.map(function(inp) {{
      var key = inp[0], label = inp[1], def = inp[2], min = inp[3], max = inp[4], step = inp[5];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="sa2_' + labItem.id + '_' + key + '">' + label + ' <span id="v_sa2_' + labItem.id + '_' + key + '" style="font-weight:700;color:#d97706;">' + def + '</span></label>' +
             '<input id="sa2_' + labItem.id + '_' + key + '" data-key="' + key + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#d97706;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + labItem.id + ' · Unit ' + unit + '</span><h3>' + labItem.name + '</h3><p>' + labItem.desc + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts metrics" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;"></div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"></div>' +
               '<div class="diag" style="margin:1rem 0;display:block;"></div>' +
               '<div class="model-note" style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;font-style:italic;"></div>';

    MODELS.push({{
      idx: idx + 1,
      unit: unit,
      id: labItem.id,
      html: html,
      init: function(card) {{
        try {{
          var stateLocal = {{}};
          labItem.inputs.forEach(function(inp) {{ stateLocal[inp[0]] = inp[2]; }});
          var plotEl = card.querySelector('.plot');
          var diagEl = card.querySelector('.diag');
          var metricsEl = card.querySelector('.metrics');
          var noteEl = card.querySelector('.model-note');

          function updateSA2() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              stateLocal[inp.dataset.key] = Number(inp.value);
              var vLbl = card.querySelector('#v_sa2_' + labItem.id + '_' + inp.dataset.key);
              if (vLbl) vLbl.textContent = inp.value;
            }});

            lab = labItem;
            state = stateLocal;
            var res = solve();

            if (plotEl) plotEl.innerHTML = svgPlot(res.pts, res.other, res.yx, res.yy);
            if (diagEl) diagEl.innerHTML = structuralDiagram(res);
            if (metricsEl) {{
              metricsEl.innerHTML = res.metrics.map(function(m) {{
                return '<div class="stat-box" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">' + m[0] + '</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">' + m[1] + '</output></div>';
              }}).join('');
            }}
            if (noteEl) noteEl.textContent = res.notes || '';
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', updateSA2);
          }});
          updateSA2();
        }} catch (err) {{
          console.warn('Structural Analysis II sim error in model ' + labItem.id + ':', err);
        }}
      }}
    }});
  }});
"""
    sa2_js += get_engine_footer('Structural Analysis II', 8)
    sa2_dest = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'structural-analysis-ii', 'structural-analysis-ii-sims.js')
    with open(sa2_dest, 'w', encoding='utf-8') as f:
        f.write(sa2_js)
    print(f"Wrote {sa2_dest}")

    # =========================================================================
    # 5. Concrete Technology (8 units, 14 simulation models)
    # =========================================================================
    print("Building concrete-technology-sims.js...")
    ct_models_src = z.read('OpenSTEM-Civil-Engineering/books/concrete-technology/assets/models.js').decode('utf-8', errors='ignore')

    ct_js = f"""/* Concrete Technology Interactive Simulation Suite */
(function(window) {{
  'use strict';

  var F = function(n, d) {{ d = (d === undefined) ? 2 : d; return Number.isFinite(n) ? Number(n).toFixed(d) : '—'; }};

  {ct_models_src[ct_models_src.find('const base='):ct_models_src.find('function setup()')]}

  var MODELS = [];
  var modelKeys = Object.keys(base);

  modelKeys.forEach(function(key, idx) {{
    var mDef = base[key];
    var unit = mDef.unit;

    var controlsHtml = mDef.inputs.map(function(inp) {{
      var pid = inp[0], label = inp[1], def = inp[2], min = inp[3], max = inp[4], step = inp[5], unitStr = inp[6];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="ct_' + key + '_' + pid + '">' + label + ' <span id="v_ct_' + key + '_' + pid + '" style="font-weight:700;color:#d97706;">' + def + ' ' + unitStr + '</span></label>' +
             '<input id="ct_' + key + '_' + pid + '" data-pid="' + pid + '" data-unit="' + unitStr + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#d97706;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge">Model ' + (idx + 1) + ' · Unit ' + unit + '</span><h3>' + mDef.title + '</h3><p>' + mDef.subtitle + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;">' +
                 '<div class="stat-box" id="stat-main" style="background:#f1f5f9;border-left:4px solid #d97706;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">Primary Metric</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">—</output></div>' +
                 '<div class="stat-box" id="stat-sec" style="background:#f1f5f9;border-left:4px solid #64748b;padding:0.5rem 1rem;border-radius:4px;"><small style="display:block;font-size:0.75rem;color:#64748b;text-transform:uppercase;">Reference Balance</small><output style="font-size:1.125rem;font-weight:700;color:#0f172a;">—</output></div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"></div>' +
               '<div class="equation" style="font-family:monospace;font-size:0.875rem;background:#f1f5f9;padding:0.75rem;border-radius:6px;margin-top:0.75rem;color:#0f172a;">Formula: ' + mDef.formula + '</div>' +
               '<p class="caveat" style="font-size:0.8125rem;color:#475569;margin-top:0.5rem;font-style:italic;">Caveat: ' + mDef.caveat + '</p>';

    MODELS.push({{
      idx: idx + 1,
      unit: unit,
      key: key,
      html: html,
      init: function(card) {{
        try {{
          var v = {{}};
          mDef.inputs.forEach(function(inp) {{ v[inp[0]] = inp[2]; }});
          var plotEl = card.querySelector('.plot');
          var mainStat = card.querySelector('#stat-main output');
          var secStat = card.querySelector('#stat-sec output');

          function updateCT() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var pid = inp.dataset.pid;
              v[pid] = Number(inp.value);
              var lbl = card.querySelector('#v_ct_' + key + '_' + pid);
              if (lbl) lbl.textContent = inp.value + ' ' + (inp.dataset.unit || '');
            }});

            var res = solve(key, v);
            if (plotEl && res.arr) plotEl.innerHTML = ssvg(res.arr, res.xLab, res.yLab);
            if (mainStat) mainStat.textContent = res.main;
            if (secStat) secStat.textContent = res.secondary;
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', updateCT);
          }});
          updateCT();
        }} catch (err) {{
          console.warn('Concrete Technology sim error in model ' + key + ':', err);
        }}
      }}
    }});
  }});
"""
    ct_js += get_engine_footer('Concrete Technology', 8)
    ct_dest = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'concrete-technology', 'concrete-technology-sims.js')
    with open(ct_dest, 'w', encoding='utf-8') as f:
        f.write(ct_js)
    print(f"Wrote {ct_dest}")

print("\nAll 5 simulation suites generated successfully!")
