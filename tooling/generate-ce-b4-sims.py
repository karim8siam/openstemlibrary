#!/usr/bin/env python3
"""
Generate Interactive Simulation Suites for Civil Engineering Batch 4:
14. environmental-engineering
15. transportation-engineering
16. highway-and-pavement-engineering
17. surveying-and-geomatics
18. engineering-geology-for-civil-engineers
"""

import zipfile, re, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ARCHIVE = '/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/.user_uploaded/media_1793628498354_3f84ba9b.zip'

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
    # 1. Environmental Engineering
    # =========================================================================
    print("Building environmental-engineering-sims.js...")
    ee_specs = []
    for i in range(1, 17):
        html = z.read(f"OpenSTEM-Civil-Engineering/books/environmental-engineering/labs/lab-{i:02d}.html").decode("utf-8", errors="ignore")
        m = re.search(r'<script\s+id="spec"\s+type="application/json">([\s\S]*?)</script>', html)
        if m:
            spec = json.loads(m.group(1))
            ee_specs.append(spec)

    ee_js = f"""/* Environmental Engineering Interactive Simulation Suite */
(function(window) {{
  'use strict';

  function eeCalc(id, x, a, b) {{
    switch(id) {{
      case 'cstr': return b / (1 + a * x);
      case 'decay': return a * Math.exp(-b * x);
      case 'mixing': return (a * 2 + x * b) / (a + x);
      case 'oxygen': {{
        let kd = 0.24, kr = b, d0 = 0.5;
        if (Math.abs(kr - kd) < 1e-8) return kd * a * x * Math.exp(-kd * x) + d0 * Math.exp(-kd * x);
        return kd * a / (kr - kd) * (Math.exp(-kd * x) - Math.exp(-kr * x)) + d0 * Math.exp(-kr * x);
      }}
      case 'settling': return 100 * Math.min(1, a / (b / x));
      case 'filter': return (0.001 * x * (a / 3600)) / (1000 * 9.81 * (b * 1e-10));
      case 'disinfect': return a * Math.exp(-b * x);
      case 'fm': return (5000 * a) / (x * b);
      case 'monod': return a * x / (b + x);
      case 'nutrient': return 0.001 * a * (b - x);
      case 'plume': {{
        let sy = 0.12 * Math.pow(x, 0.9), sz = 0.06 * Math.pow(x, 0.85);
        return 1e6 * a / (Math.PI * b * sy * sz) * Math.exp(-900 / (2 * sz * sz));
      }}
      case 'capture': return 1e-6 * x * a * b / 100;
      case 'recycle': return x * a * b * 0.85;
      case 'landfill': return a * b * 1e5 * Math.exp(-a * x);
      case 'exposure': return a * x / b;
      case 'carbon': return x * a * b;
      default: return NaN;
    }}
  }}

  var EE_SPECS = {json.dumps(ee_specs, indent=2)};

  var MODELS = EE_SPECS.map(function(s, idx) {{
    var controlsHtml = s.parameters.map(function(p, pi) {{
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="ee_' + (idx + 1) + '_' + pi + '">' + p.name + ' <span class="unit" style="color:#64748b;">(' + p.unit + ')</span>: <span id="v_ee_' + (idx + 1) + '_' + pi + '" style="font-weight:700;color:#059669;">' + p.default + '</span></label>' +
             '<input id="ee_' + (idx + 1) + '_' + pi + '" data-pidx="' + pi + '" type="range" min="' + p.min + '" max="' + p.max + '" step="' + p.step + '" value="' + p.default + '" style="width:100%;accent-color:#059669;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#d1fae5;color:#065f46;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Lab ' + (idx + 1) + ' · Unit ' + s.unit + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + s.name + '</h3>' +
               '<div style="background:#f0fdf4;padding:0.5rem 0.75rem;border-radius:4px;font-family:monospace;font-size:0.85rem;color:#065f46;margin-bottom:0.75rem;">' + (s.formula || '') + '</div>' +
               '<p style="margin:0 0 1rem 0;color:#475569;font-size:0.9rem;">' + (s.prompt || '') + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#ecfdf5;border-left:4px solid #059669;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div style="font-size:0.8rem;color:#065f46;font-weight:600;text-transform:uppercase;">' + (s.yLabel || 'Result') + '</div>' +
                 '<div class="val-readout" style="font-size:1.5rem;font-weight:700;color:#047857;">--</div>' +
                 '<div class="interp-text" style="font-size:0.85rem;color:#064e3b;margin-top:0.25rem;">' + (s.limits || '') + '</div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 740 330" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>';

    return {{
      idx: idx + 1,
      unit: s.unit,
      html: html,
      init: function(card) {{
        try {{
          var pVals = s.parameters.map(function(p) {{ return p.default; }});
          var valEl = card.querySelector('.val-readout');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(pts, currX, currY) {{
            if (!svgEl || !pts.length) return;
            svgEl.innerHTML = '';
            var W = 740, H = 330, L = 70, R = 22, T = 22, B = 52;
            var xmin = s.xmin, xmax = s.xmax;
            var ys = pts.map(function(p) {{ return p[1]; }}).filter(Number.isFinite);
            var lo = Math.min(0, Math.min.apply(null, ys), currY);
            var hi = Math.max.apply(null, ys);
            if (hi <= lo) hi = lo + 1;

            var xp = function(x) {{ return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); }};
            var yp = function(y) {{ return H - B - (y - lo) / (hi - lo || 1) * (H - T - B); }};

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {{
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }}

            for (var i = 0; i <= 4; i++) {{
              var v = lo + (hi - lo) * i / 4, yPos = yp(v);
              node('line', {{ x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '3 3' }});
              node('text', {{ x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }}, Number(v.toPrecision(3)).toString());
            }}
            node('line', {{ x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});
            node('line', {{ x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});

            var pathPts = pts.map(function(d) {{ return xp(d[0]).toFixed(1) + ',' + yp(d[1]).toFixed(1); }}).join(' ');
            node('polyline', {{ points: pathPts, fill: 'none', stroke: '#059669', 'stroke-width': '2.5' }});

            if (Number.isFinite(currY)) {{
              node('circle', {{ cx: xp(currX), cy: yp(currY), r: 6, fill: '#f59e0b', stroke: '#ffffff', 'stroke-width': '2' }});
            }}
            node('text', {{ x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }}, s.xLabel || 'Input');
          }}

          function render() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var pi = parseInt(inp.dataset.pidx, 10);
              pVals[pi] = Number(inp.value);
              var vLbl = card.querySelector('#v_ee_' + (idx + 1) + '_' + pi);
              if (vLbl) vLbl.textContent = inp.value;
            }});

            var midX = (s.xmin + s.xmax) / 2;
            var currY = eeCalc(s.id, midX, pVals[0], pVals[1] !== undefined ? pVals[1] : 1);
            if (valEl) {{
              valEl.textContent = Number.isFinite(currY) ? Number(currY.toPrecision(4)) + ' ' + (s.yUnit || '') : '--';
            }}

            var pts = [];
            for (var k = 0; k <= 50; k++) {{
              var x = s.xmin + (s.xmax - s.xmin) * k / 50;
              var y = eeCalc(s.id, x, pVals[0], pVals[1] !== undefined ? pVals[1] : 1);
              if (Number.isFinite(y)) pts.push([x, y]);
            }}
            drawGraph(pts, midX, currY);
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', render);
          }});
          render();
        }} catch(err) {{
          console.error('EE sim error on lab ' + (idx + 1), err);
        }}
      }}
    }};
  }});
{get_engine_footer('environmental-engineering')}"""

    ee_out_path = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'environmental-engineering', 'environmental-engineering-sims.js')
    with open(ee_out_path, 'w', encoding='utf-8') as f:
        f.write(ee_js)
    print(f"Wrote {ee_out_path}")

    # =========================================================================
    # 2. Transportation Engineering
    # =========================================================================
    print("Building transportation-engineering-sims.js...")
    te_js_raw = z.read("OpenSTEM-Civil-Engineering/books/transportation-engineering/assets/models.js").decode("utf-8", errors="ignore")
    te_labs_m = re.search(r'const\s+TRANSPORT_LABS\s*=\s*(\[[\s\S]*?\]);', te_js_raw)
    te_labs = json.loads(te_labs_m.group(1)) if te_labs_m else []

    calc_m = re.search(r'function transportationCalc\(key,a,b\)\{([\s\S]*?)\n\}\n\s*(?:function|if|window)', te_js_raw)
    calc_body = calc_m.group(1) if calc_m else ""

    te_js = f"""/* Transportation Engineering Interactive Simulation Suite */
(function(window) {{
  'use strict';

  function transportationCalc(key, a, b) {{
    {calc_body}
  }}

  var TE_LABS = {json.dumps(te_labs, indent=2)};

  var MODELS = TE_LABS.map(function(lab) {{
    var controlsHtml = lab.params.map(function(p, pi) {{
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="te_' + lab.id + '_' + pi + '">' + p.name + ' <span class="unit" style="color:#64748b;">(' + p.unit + ')</span>: <span id="v_te_' + lab.id + '_' + pi + '" style="font-weight:700;color:#d97706;">' + p.default + '</span></label>' +
             '<input id="te_' + lab.id + '_' + pi + '" data-pidx="' + pi + '" type="range" min="' + p.min + '" max="' + p.max + '" step="' + p.step + '" value="' + p.default + '" style="width:100%;accent-color:#d97706;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#fef3c7;color:#b45309;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Lab ' + lab.id + ' · Unit ' + lab.unit + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + lab.title + '</h3>' +
               '<div style="background:#fffbeb;padding:0.5rem 0.75rem;border-radius:4px;font-family:monospace;font-size:0.85rem;color:#b45309;margin-bottom:0.75rem;">' + (lab.equation || '') + '</div>' +
               '<p style="margin:0 0 1rem 0;color:#475569;font-size:0.9rem;">' + (lab.assumption || lab.question || '') + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#fffbeb;border-left:4px solid #d97706;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div style="font-size:0.8rem;color:#92400e;font-weight:600;text-transform:uppercase;">Calculated Output</div>' +
                 '<div class="val-readout" style="font-size:1.5rem;font-weight:700;color:#b45309;">--</div>' +
                 '<div class="interp-text" style="font-size:0.85rem;color:#78350f;margin-top:0.25rem;"></div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 740 330" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>' +
               '<div class="model-note" style="font-size:0.8rem;color:#64748b;margin-top:0.5rem;font-style:italic;">' + (lab.question || '') + '</div>';

    return {{
      idx: lab.id,
      unit: lab.unit,
      html: html,
      init: function(card) {{
        try {{
          var pVals = lab.params.map(function(p) {{ return p.default; }});
          var valEl = card.querySelector('.val-readout');
          var interpEl = card.querySelector('.interp-text');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(pts, currX, currY) {{
            if (!svgEl || !pts.length) return;
            svgEl.innerHTML = '';
            var W = 740, H = 330, L = 70, R = 22, T = 22, B = 52;
            var xs = pts.map(function(p) {{ return p[0]; }});
            var ys = pts.map(function(p) {{ return p[1]; }}).filter(Number.isFinite);
            var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
            var ymin = Math.min(0, Math.min.apply(null, ys), currY);
            var ymax = Math.max.apply(null, ys);
            if (ymax <= ymin) ymax = ymin + 1;

            var xp = function(x) {{ return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); }};
            var yp = function(y) {{ return H - B - (y - ymin) / (ymax - ymin || 1) * (H - T - B); }};

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {{
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }}

            for (var i = 0; i <= 4; i++) {{
              var v = ymin + (ymax - ymin) * i / 4, yPos = yp(v);
              node('line', {{ x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '3 3' }});
              node('text', {{ x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }}, Number(v.toPrecision(3)).toString());
            }}
            node('line', {{ x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});
            node('line', {{ x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});

            var pathPts = pts.map(function(d) {{ return xp(d[0]).toFixed(1) + ',' + yp(d[1]).toFixed(1); }}).join(' ');
            node('polyline', {{ points: pathPts, fill: 'none', stroke: '#d97706', 'stroke-width': '2.5' }});

            if (Number.isFinite(currY)) {{
              node('circle', {{ cx: xp(currX), cy: yp(currY), r: 6, fill: '#ea580c', stroke: '#ffffff', 'stroke-width': '2' }});
            }}
            node('text', {{ x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }}, lab.params[0].name);
          }}

          function render() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var pi = parseInt(inp.dataset.pidx, 10);
              pVals[pi] = Number(inp.value);
              var lbl = card.querySelector('#v_te_' + lab.id + '_' + pi);
              if (lbl) lbl.textContent = inp.value;
            }});

            var res = transportationCalc(lab.key, pVals[0], pVals[1] !== undefined ? pVals[1] : 1);
            if (valEl) {{
              valEl.textContent = Number.isFinite(res.y) ? Number(res.y.toPrecision(4)) + ' ' + (res.unit || '') : '--';
            }}
            if (interpEl) interpEl.textContent = res.secondary || '';

            var pts = [];
            var p0 = lab.params[0];
            for (var k = 0; k <= 50; k++) {{
              var aX = p0.min + (p0.max - p0.min) * k / 50;
              var ptRes = transportationCalc(lab.key, aX, pVals[1] !== undefined ? pVals[1] : 1);
              if (Number.isFinite(ptRes.y)) pts.push([aX, ptRes.y]);
            }}
            drawGraph(pts, pVals[0], res.y);
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', render);
          }});
          render();
        }} catch(err) {{
          console.error('TE sim error on lab ' + lab.id, err);
        }}
      }}
    }};
  }});
{get_engine_footer('transportation-engineering')}"""

    te_out_path = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'transportation-engineering', 'transportation-engineering-sims.js')
    with open(te_out_path, 'w', encoding='utf-8') as f:
        f.write(te_js)
    print(f"Wrote {te_out_path}")

    # =========================================================================
    # 3. Highway and Pavement Engineering
    # =========================================================================
    print("Building highway-and-pavement-engineering-sims.js...")
    hp_labs_json = json.loads(z.read("OpenSTEM-Civil-Engineering/books/highway-and-pavement-engineering/assets/labs.json").decode("utf-8", errors="ignore"))

    hp_js = f"""/* Highway and Pavement Engineering Interactive Simulation Suite */
(function(window) {{
  'use strict';

  const g = 9.81;

  function formula(id, x, a, b) {{
    switch(id) {{
      case 'earthworks': return x * (a + b) / 2;
      case 'profile': return (a / 100) * x + ((b - a) / 100) * x * x / (2 * 200);
      case 'ssd': {{ let v = x / 3.6; return v * a + v * v / (2 * b); }}
      case 'radius': return x * x / (127 * (a + b));
      case 'gradation': return x >= a ? 100 : 100 * Math.pow(Math.max(0, x) / a, b);
      case 'binder': return a * Math.exp(-b * (x - 20));
      case 'stress': return a * (1 - Math.pow(1 + Math.pow(b / x, 2), -1.5));
      case 'fatigue': return b * Math.pow(150 / x, a);
      case 'rut': return 1 + a * Math.pow(x, b);
      case 'plate': return (a * 1000 * Math.pow(x, 3)) / (12 * (1 - b * b));
      case 'joint': return a * 1e-3 * b * x;
      case 'compaction': return Math.max(0, b - 0.045 * Math.pow(x - a, 2));
      case 'endarea': return x * (a + b) / 2;
      case 'runoff': return 0.00278 * b * x * a;
      case 'npv': {{ let s = 0; for (let t = 0; t <= x; t += 7) s += b / Math.pow(1 + a / 100, t); return s; }}
      case 'wetbrake': {{ let v = x / 3.6; return v * b + v * v / (2 * a * g); }}
      default: return NaN;
    }}
  }}

  var HP_LABS = {json.dumps(hp_labs_json, indent=2)};

  var MODELS = HP_LABS.map(function(spec, idx) {{
    var unitNum = spec.unit_number || spec.unit || ((idx >> 1) + 1);
    var controlsHtml = spec.params.map(function(p, pi) {{
      var defVal = p.value !== undefined ? p.value : (p.default !== undefined ? p.default : p.min);
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="hp_' + (idx + 1) + '_' + pi + '">' + p.name + ' <span class="unit" style="color:#64748b;">(' + p.unit + ')</span>: <span id="v_hp_' + (idx + 1) + '_' + pi + '" style="font-weight:700;color:#ea580c;">' + defVal + '</span></label>' +
             '<input id="hp_' + (idx + 1) + '_' + pi + '" data-pidx="' + pi + '" type="range" min="' + p.min + '" max="' + p.max + '" step="' + p.step + '" value="' + defVal + '" style="width:100%;accent-color:#ea580c;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#ffedd5;color:#c2410c;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Lab ' + (idx + 1) + ' · Unit ' + unitNum + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + spec.title + '</h3>' +
               '<div style="background:#fff7ed;padding:0.5rem 0.75rem;border-radius:4px;font-family:monospace;font-size:0.85rem;color:#c2410c;margin-bottom:0.75rem;">' + (spec.formula || '') + '</div>' +
               '<p style="margin:0 0 1rem 0;color:#475569;font-size:0.9rem;">' + (spec.task || '') + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#fff7ed;border-left:4px solid #ea580c;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div style="font-size:0.8rem;color:#9a3412;font-weight:600;text-transform:uppercase;">' + (spec.xlabel || 'Calculated Metric') + '</div>' +
                 '<div class="val-readout" style="font-size:1.5rem;font-weight:700;color:#c2410c;">--</div>' +
                 '<div class="interp-text" style="font-size:0.85rem;color:#7c2d12;margin-top:0.25rem;">' + (spec.limit || '') + '</div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 740 330" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>';

    return {{
      idx: idx + 1,
      unit: unitNum,
      html: html,
      init: function(card) {{
        try {{
          var pVals = spec.params.map(function(p) {{ return p.value !== undefined ? p.value : (p.default !== undefined ? p.default : p.min); }});
          var valEl = card.querySelector('.val-readout');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(pts, currX, currY) {{
            if (!svgEl || !pts.length) return;
            svgEl.innerHTML = '';
            var W = 740, H = 330, L = 70, R = 22, T = 22, B = 52;
            var xs = pts.map(function(p) {{ return p[0]; }});
            var ys = pts.map(function(p) {{ return p[1]; }}).filter(Number.isFinite);
            var xmin = spec.xmin !== undefined ? spec.xmin : Math.min.apply(null, xs);
            var xmax = spec.xmax !== undefined ? spec.xmax : Math.max.apply(null, xs);
            var ymin = Math.min(0, Math.min.apply(null, ys), currY);
            var ymax = Math.max.apply(null, ys);
            if (ymax <= ymin) ymax = ymin + 1;

            var xp = function(x) {{ return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); }};
            var yp = function(y) {{ return H - B - (y - ymin) / (ymax - ymin || 1) * (H - T - B); }};

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {{
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }}

            for (var i = 0; i <= 4; i++) {{
              var v = ymin + (ymax - ymin) * i / 4, yPos = yp(v);
              node('line', {{ x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '3 3' }});
              node('text', {{ x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }}, Number(v.toPrecision(3)).toString());
            }}
            node('line', {{ x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});
            node('line', {{ x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});

            var pathPts = pts.map(function(d) {{ return xp(d[0]).toFixed(1) + ',' + yp(d[1]).toFixed(1); }}).join(' ');
            node('polyline', {{ points: pathPts, fill: 'none', stroke: '#ea580c', 'stroke-width': '2.5' }});

            if (Number.isFinite(currY)) {{
              node('circle', {{ cx: xp(currX), cy: yp(currY), r: 6, fill: '#f59e0b', stroke: '#ffffff', 'stroke-width': '2' }});
            }}
            node('text', {{ x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }}, spec.xlabel || 'Input');
          }}

          function render() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var pi = parseInt(inp.dataset.pidx, 10);
              pVals[pi] = Number(inp.value);
              var vLbl = card.querySelector('#v_hp_' + (idx + 1) + '_' + pi);
              if (vLbl) vLbl.textContent = inp.value;
            }});

            var xmin = spec.xmin !== undefined ? spec.xmin : 0;
            var xmax = spec.xmax !== undefined ? spec.xmax : 100;
            var midX = (xmin + xmax) / 2;
            var curVal = formula(spec.id, midX, pVals[0], pVals[1] !== undefined ? pVals[1] : 1);
            if (valEl) {{
              valEl.textContent = Number.isFinite(curVal) ? Number(curVal.toPrecision(4)) + ' ' + (spec.unit || '') : '--';
            }}

            var pts = [];
            for (var k = 0; k <= 50; k++) {{
              var xV = xmin + (xmax - xmin) * k / 50;
              var yV = formula(spec.id, xV, pVals[0], pVals[1] !== undefined ? pVals[1] : 1);
              if (Number.isFinite(yV)) pts.push([xV, yV]);
            }}
            drawGraph(pts, midX, curVal);
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', render);
          }});
          render();
        }} catch(err) {{
          console.error('HP sim error on lab ' + (idx + 1), err);
        }}
      }}
    }};
  }});
{get_engine_footer('highway-and-pavement-engineering')}"""

    hp_out_path = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'highway-and-pavement-engineering', 'highway-and-pavement-engineering-sims.js')
    with open(hp_out_path, 'w', encoding='utf-8') as f:
        f.write(hp_js)
    print(f"Wrote {hp_out_path}")

    # =========================================================================
    # 4. Surveying and Geomatics
    # =========================================================================
    print("Building surveying-and-geomatics-sims.js...")
    sg_js_raw = z.read("OpenSTEM-Civil-Engineering/books/surveying-and-geomatics/assets/models.js").decode("utf-8", errors="ignore")
    sg_labs_m = re.search(r'const\s+LAB_SPECS\s*=\s*(\[[\s\S]*?\]);', sg_js_raw)
    sg_labs = json.loads(sg_labs_m.group(1)) if sg_labs_m else []

    sg_js = f"""/* Surveying and Geomatics Interactive Simulation Suite */
(function(window) {{
  'use strict';

  function sgCalc(id, p) {{
    switch(id) {{
      case 1: {{ const c = p.L * (p.alpha * 1e-6) * (p.T - 20); return {{ value: p.L + c, other: 'Correction: ' + (c * 1000).toFixed(2) + ' mm' }}; }}
      case 2: {{ const H = Math.sqrt(Math.max(0, p.S * p.S - p.dh * p.dh)); return {{ value: H, other: 'Slope reduction: ' + (p.S - H).toFixed(4) + ' m' }}; }}
      case 3: {{ return {{ value: -p.bias / p.n, other: 'Total misclosure: ' + p.bias.toFixed(3) + ' arcsec' }}; }}
      case 4: {{ const f = p.BS - p.FS - p.known; return {{ value: f * 1000, other: 'Corrected rise: ' + (p.BS - p.FS - f).toFixed(4) + ' m' }}; }}
      case 5: {{ const c = (1 - p.k) * Math.pow(p.d * 1000, 2) / (2 * p.R * 1000); return {{ value: c, other: 'Magnitude: ' + (c * 1000).toFixed(1) + ' mm' }}; }}
      case 6: {{ const L = 2 * p.E + 2 * p.N; return {{ value: -p.mis * p.E / L, other: 'Perimeter: ' + L.toFixed(1) + ' m' }}; }}
      case 7: {{ const w1 = 1 / (0.01 * 0.01), w2 = 1 / Math.pow(p.sigma2 / 100, 2); return {{ value: (w1 * p.x1 + w2 * p.x2) / (w1 + w2), other: 'Uncertainty: ' + (100 * Math.sqrt(1 / (w1 + w2))).toFixed(3) + ' cm' }}; }}
      case 8: {{ return {{ value: p.height * (p.width + p.skew / 2), other: 'Trapezoidal bounds evaluated' }}; }}
      case 9: {{ return {{ value: p.uere * p.hdop, other: 'Vertical: ' + (p.uere * p.vdop).toFixed(3) + ' m' }}; }}
      case 10: {{ return {{ value: p.h - p.N, other: 'Declared geoid error: ±' + p.nerr.toFixed(2) + ' m' }}; }}
      case 11: {{ const gsd = p.H * (p.pitch / 1000) / p.f * 100; return {{ value: gsd, other: 'Ground pixel: ' + (gsd / 100).toFixed(4) + ' m' }}; }}
      case 12: {{ const Z = p.B * 100 / p.p; return {{ value: p.H - Z, other: 'Range: ' + Z.toFixed(2) + ' m' }}; }}
      case 13: {{ return {{ value: p.PRF * 1000 / (p.v * p.W), other: 'Acquisition area: ' + (p.v * p.W).toFixed(0) + ' m²/s' }}; }}
      case 14: {{ const T = p.R * Math.tan(p.Delta / 2 * Math.PI / 180); return {{ value: T, other: 'Curve length: ' + (p.R * p.Delta * Math.PI / 180).toFixed(2) + ' m' }}; }}
      case 15: {{ return {{ value: p.L * (p.A1 + p.A2) / 2, other: 'End-area volume' }}; }}
      case 16: {{ const rmse = Math.sqrt(p.eX * p.eX + p.eY * p.eY); return {{ value: rmse, other: '95% error circle: ' + (2.4477 * rmse).toFixed(3) + ' m' }}; }}
      default: return {{ value: NaN, other: '' }};
    }}
  }}

  var SG_LABS = {json.dumps(sg_labs, indent=2)};

  var MODELS = SG_LABS.map(function(lab) {{
    var unitNum = ((lab.id - 1) >> 1) + 1;
    var controlsHtml = lab.params.map(function(p) {{
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="sg_' + lab.id + '_' + p.id + '">' + p.label + ': <span id="v_sg_' + lab.id + '_' + p.id + '" style="font-weight:700;color:#0284c7;">' + p.default + '</span></label>' +
             '<input id="sg_' + lab.id + '_' + p.id + '" data-pid="' + p.id + '" type="range" min="' + p.min + '" max="' + p.max + '" step="' + p.step + '" value="' + p.default + '" style="width:100%;accent-color:#0284c7;"></div>';
    }}).join('');

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#e0f2fe;color:#0369a1;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Lab ' + lab.id + ' · Unit ' + unitNum + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + lab.name + '</h3>' +
               '<p style="margin:0 0 1rem 0;color:#475569;font-size:0.9rem;">' + (lab.subtitle || '') + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#f0fdf4;border-left:4px solid #16a34a;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div style="font-size:0.8rem;color:#166534;font-weight:600;text-transform:uppercase;">' + (lab.ylabel || 'Geomatics Output') + '</div>' +
                 '<div class="val-readout" style="font-size:1.5rem;font-weight:700;color:#15803d;">--</div>' +
                 '<div class="interp-text" style="font-size:0.85rem;color:#14532d;margin-top:0.25rem;"></div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 740 330" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>' +
               '<div class="model-note" style="font-size:0.8rem;color:#64748b;margin-top:0.5rem;font-style:italic;">' + (lab.caution || '') + '</div>';

    return {{
      idx: lab.id,
      unit: unitNum,
      html: html,
      init: function(card) {{
        try {{
          var pVals = {{}};
          lab.params.forEach(function(p) {{ pVals[p.id] = p.default; }});
          var valEl = card.querySelector('.val-readout');
          var interpEl = card.querySelector('.interp-text');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(pts, currX, currY) {{
            if (!svgEl || !pts.length) return;
            svgEl.innerHTML = '';
            var W = 740, H = 330, L = 70, R = 22, T = 22, B = 52;
            var xs = pts.map(function(p) {{ return p[0]; }});
            var ys = pts.map(function(p) {{ return p[1]; }}).filter(Number.isFinite);
            var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
            var ymin = Math.min(0, Math.min.apply(null, ys), currY);
            var ymax = Math.max.apply(null, ys);
            if (ymax <= ymin) ymax = ymin + 1;

            var xp = function(x) {{ return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); }};
            var yp = function(y) {{ return H - B - (y - ymin) / (ymax - ymin || 1) * (H - T - B); }};

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {{
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }}

            for (var i = 0; i <= 4; i++) {{
              var v = ymin + (ymax - ymin) * i / 4, yPos = yp(v);
              node('line', {{ x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '3 3' }});
              node('text', {{ x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }}, Number(v.toPrecision(3)).toString());
            }}
            node('line', {{ x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});
            node('line', {{ x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});

            var pathPts = pts.map(function(d) {{ return xp(d[0]).toFixed(1) + ',' + yp(d[1]).toFixed(1); }}).join(' ');
            node('polyline', {{ points: pathPts, fill: 'none', stroke: '#0284c7', 'stroke-width': '2.5' }});

            if (Number.isFinite(currY)) {{
              node('circle', {{ cx: xp(currX), cy: yp(currY), r: 6, fill: '#ea580c', stroke: '#ffffff', 'stroke-width': '2' }});
            }}
            node('text', {{ x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }}, lab.params[0].label);
          }}

          function render() {{
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
              var pKey = inp.dataset.pid;
              pVals[pKey] = Number(inp.value);
              var vLbl = card.querySelector('#v_sg_' + lab.id + '_' + pKey);
              if (vLbl) vLbl.textContent = inp.value;
            }});

            var res = sgCalc(lab.id, pVals);
            if (valEl) {{
              valEl.textContent = Number.isFinite(res.value) ? Number(res.value.toPrecision(5)) + ' ' + (lab.unit || '') : '--';
            }}
            if (interpEl) interpEl.textContent = res.other || '';

            var pts = [];
            var p0 = lab.params[0];
            for (var s = 0; s <= 50; s++) {{
              var xV = p0.min + (p0.max - p0.min) * s / 50;
              var curP = Object.assign({{}}, pVals);
              curP[p0.id] = xV;
              var ptRes = sgCalc(lab.id, curP);
              if (Number.isFinite(ptRes.value)) pts.push([xV, ptRes.value]);
            }}
            drawGraph(pts, pVals[p0.id], res.value);
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', render);
          }});
          render();
        }} catch(err) {{
          console.error('SG sim error on lab ' + lab.id, err);
        }}
      }}
    }};
  }});
{get_engine_footer('surveying-and-geomatics')}"""

    sg_out_path = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'surveying-and-geomatics', 'surveying-and-geomatics-sims.js')
    with open(sg_out_path, 'w', encoding='utf-8') as f:
        f.write(sg_js)
    print(f"Wrote {sg_out_path}")

    # =========================================================================
    # 5. Engineering Geology for Civil Engineers
    # =========================================================================
    print("Building engineering-geology-for-civil-engineers-sims.js...")
    eg_specs = []
    for i in range(1, 17):
        html = z.read(f"OpenSTEM-Civil-Engineering/books/engineering-geology-for-civil-engineers/labs/lab-{i:02d}.html").decode("utf-8", errors="ignore")
        m = re.search(r'<script\s+type="application/json"\s+id="lab-spec">([\s\S]*?)</script>', html)
        if m:
            spec = json.loads(m.group(1))
            unit = (i + 1) // 2
            spec['unit'] = unit
            eg_specs.append(spec)

    eg_js = f"""/* Engineering Geology Interactive Simulation Suite */
(function(window) {{
  'use strict';

  function egCalc(id, a, b) {{
    const rad = Math.PI / 180;
    switch(id) {{
      case 1: return a / b;
      case 2: return Math.atan(Math.tan(a * rad) * Math.sin(b * rad)) / rad;
      case 3: return 80 * Math.exp(-a * b);
      case 4: {{ let x = a * b; return 100 * Math.exp(-x) * (1 + x); }}
      case 5: return b / a;
      case 6: return b - a;
      case 7: {{ let above = Math.min(a, b), below = Math.max(0, a - b); return 18 * above + (20 - 9.81) * below; }}
      case 8: return 1000 * b * a / 10;
      case 9: {{ let v1 = 700, v2 = 2400; let direct = a / v1, crit = 2 * b * Math.sqrt(v2 * v2 - v1 * v1) / (v1 * v2) + a / v2; return 1000 * Math.min(direct, crit); }}
      case 10: {{ let f = a / 100, rRock = 1000, rWater = b; return 1 / ((1 - f) / rRock + f / rWater); }}
      case 11: {{ let ph = 32 * rad, t = a * rad, W = 100, cA = 10, normal = Math.max(0, W * Math.cos(t) - b); return (cA + normal * Math.tan(ph)) / (W * Math.sin(t)); }}
      case 12: return a * a * b;
      case 13: {{ let theta = a * rad, sv = 10, sh = b * sv; return sh + sv - 2 * (sh - sv) * Math.cos(2 * theta); }}
      case 14: {{ let L = a, h = b, q = 40000, E = 1e10, I = h * h * h / 12; return (5 * q * Math.pow(L, 4) / (384 * E * I)) * 1000; }}
      case 15: return 0.65 * a * (200 / 120) * b;
      case 16: return 300 * 0.03 * a * b;
      default: return NaN;
    }}
  }}

  var EG_SPECS = {json.dumps(eg_specs, indent=2)};

  var MODELS = EG_SPECS.map(function(spec) {{
    var pA = spec.a, pB = spec.b;
    var controlsHtml = '<div class="param" style="margin-bottom:0.75rem;"><label for="eg_' + spec.id + '_a">' + pA[0] + ': <span id="v_eg_' + spec.id + '_a" style="font-weight:700;color:#4f46e5;">' + pA[1] + '</span></label>' +
                       '<input id="eg_' + spec.id + '_a" data-param="a" type="range" min="' + pA[2] + '" max="' + pA[3] + '" step="' + pA[4] + '" value="' + pA[1] + '" style="width:100%;accent-color:#4f46e5;"></div>' +
                       '<div class="param" style="margin-bottom:0.75rem;"><label for="eg_' + spec.id + '_b">' + pB[0] + ': <span id="v_eg_' + spec.id + '_b" style="font-weight:700;color:#4f46e5;">' + pB[1] + '</span></label>' +
                       '<input id="eg_' + spec.id + '_b" data-param="b" type="range" min="' + pB[2] + '" max="' + pB[3] + '" step="' + pB[4] + '" value="' + pB[1] + '" style="width:100%;accent-color:#4f46e5;"></div>';

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#ede9fe;color:#5b21b6;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Lab ' + spec.id + ' · Unit ' + spec.unit + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + spec.name + '</h3>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#f5f3ff;border-left:4px solid #4f46e5;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div style="font-size:0.8rem;color:#4338ca;font-weight:600;text-transform:uppercase;">' + (spec.output || 'Geological Output') + '</div>' +
                 '<div class="val-readout" style="font-size:1.5rem;font-weight:700;color:#3730a3;">--</div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 740 330" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>';

    return {{
      idx: spec.id,
      unit: spec.unit,
      html: html,
      init: function(card) {{
        try {{
          var valA = pA[1], valB = pB[1];
          var valEl = card.querySelector('.val-readout');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(pts, currX, currY) {{
            if (!svgEl || !pts.length) return;
            svgEl.innerHTML = '';
            var W = 740, H = 330, L = 70, R = 22, T = 22, B = 52;
            var xs = pts.map(function(p) {{ return p[0]; }});
            var ys = pts.map(function(p) {{ return p[1]; }}).filter(Number.isFinite);
            var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
            var ymin = Math.min(0, Math.min.apply(null, ys), currY);
            var ymax = Math.max.apply(null, ys);
            if (ymax <= ymin) ymax = ymin + 1;

            var xp = function(x) {{ return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); }};
            var yp = function(y) {{ return H - B - (y - ymin) / (ymax - ymin || 1) * (H - T - B); }};

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {{
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }}

            for (var i = 0; i <= 4; i++) {{
              var v = ymin + (ymax - ymin) * i / 4, yPos = yp(v);
              node('line', {{ x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '3 3' }});
              node('text', {{ x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }}, Number(v.toPrecision(3)).toString());
            }}
            node('line', {{ x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});
            node('line', {{ x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' }});

            var pathPts = pts.map(function(d) {{ return xp(d[0]).toFixed(1) + ',' + yp(d[1]).toFixed(1); }}).join(' ');
            node('polyline', {{ points: pathPts, fill: 'none', stroke: '#4f46e5', 'stroke-width': '2.5' }});

            if (Number.isFinite(currY)) {{
              node('circle', {{ cx: xp(currX), cy: yp(currY), r: 6, fill: '#f59e0b', stroke: '#ffffff', 'stroke-width': '2' }});
            }}
            node('text', {{ x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }}, pA[0]);
          }}

          function render() {{
            var inpA = card.querySelector('#eg_' + spec.id + '_a');
            var inpB = card.querySelector('#eg_' + spec.id + '_b');
            if (inpA) {{
              valA = Number(inpA.value);
              var lblA = card.querySelector('#v_eg_' + spec.id + '_a');
              if (lblA) lblA.textContent = inpA.value;
            }}
            if (inpB) {{
              valB = Number(inpB.value);
              var lblB = card.querySelector('#v_eg_' + spec.id + '_b');
              if (lblB) lblB.textContent = inpB.value;
            }}

            var res = egCalc(spec.id, valA, valB);
            if (valEl) {{
              valEl.textContent = Number.isFinite(res) ? Number(res.toPrecision(4)) : '--';
            }}

            var pts = [];
            for (var k = 0; k <= 50; k++) {{
              var aX = pA[2] + (pA[3] - pA[2]) * k / 50;
              var ptRes = egCalc(spec.id, aX, valB);
              if (Number.isFinite(ptRes)) pts.push([aX, ptRes]);
            }}
            drawGraph(pts, valA, res);
          }}

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {{
            inp.addEventListener('input', render);
          }});
          render();
        }} catch(err) {{
          console.error('EG sim error on lab ' + spec.id, err);
        }}
      }}
    }};
  }});
{get_engine_footer('engineering-geology-for-civil-engineers')}"""

    eg_out_path = os.path.join(ROOT, 'src', 'subjects', 'civil-engineering', 'engineering-geology-for-civil-engineers', 'engineering-geology-for-civil-engineers-sims.js')
    with open(eg_out_path, 'w', encoding='utf-8') as f:
        f.write(eg_js)
    print(f"Wrote {eg_out_path}")

print("Batch 4 simulation suites generated successfully!")
