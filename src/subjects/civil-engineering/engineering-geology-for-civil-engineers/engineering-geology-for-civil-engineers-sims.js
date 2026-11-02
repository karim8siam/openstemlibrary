/* Engineering Geology Interactive Simulation Suite */
(function(window) {
  'use strict';

  function egCalc(id, a, b) {
    const rad = Math.PI / 180;
    switch(id) {
      case 1: return a / b;
      case 2: return Math.atan(Math.tan(a * rad) * Math.sin(b * rad)) / rad;
      case 3: return 80 * Math.exp(-a * b);
      case 4: { let x = a * b; return 100 * Math.exp(-x) * (1 + x); }
      case 5: return b / a;
      case 6: return b - a;
      case 7: { let above = Math.min(a, b), below = Math.max(0, a - b); return 18 * above + (20 - 9.81) * below; }
      case 8: return 1000 * b * a / 10;
      case 9: { let v1 = 700, v2 = 2400; let direct = a / v1, crit = 2 * b * Math.sqrt(v2 * v2 - v1 * v1) / (v1 * v2) + a / v2; return 1000 * Math.min(direct, crit); }
      case 10: { let f = a / 100, rRock = 1000, rWater = b; return 1 / ((1 - f) / rRock + f / rWater); }
      case 11: { let ph = 32 * rad, t = a * rad, W = 100, cA = 10, normal = Math.max(0, W * Math.cos(t) - b); return (cA + normal * Math.tan(ph)) / (W * Math.sin(t)); }
      case 12: return a * a * b;
      case 13: { let theta = a * rad, sv = 10, sh = b * sv; return sh + sv - 2 * (sh - sv) * Math.cos(2 * theta); }
      case 14: { let L = a, h = b, q = 40000, E = 1e10, I = h * h * h / 12; return (5 * q * Math.pow(L, 4) / (384 * E * I)) * 1000; }
      case 15: return 0.65 * a * (200 / 120) * b;
      case 16: return 300 * 0.03 * a * b;
      default: return NaN;
    }
  }

  var EG_SPECS = [
  {
    "id": 1,
    "name": "Stratigraphic age\u2013depth reconstruction",
    "a": [
      "Depth below datum (m)",
      15,
      1,
      50,
      0.5
    ],
    "b": [
      "Net deposition (m per thousand years)",
      0.35,
      0.05,
      2,
      0.05
    ],
    "output": "Age estimate (ka)",
    "kind": "age",
    "unit": 1
  },
  {
    "id": 2,
    "name": "Apparent dip in an oblique section",
    "a": [
      "True dip (degrees)",
      42,
      1,
      80,
      1
    ],
    "b": [
      "Section azimuth minus strike (degrees)",
      60,
      0,
      90,
      1
    ],
    "output": "Apparent dip (degrees)",
    "kind": "dip",
    "unit": 1
  },
  {
    "id": 3,
    "name": "Weathering sensitivity of intact UCS",
    "a": [
      "Exposure index (arbitrary years)",
      12,
      0,
      50,
      1
    ],
    "b": [
      "Assumed degradation coefficient (per year)",
      0.04,
      0.005,
      0.15,
      0.005
    ],
    "output": "Remaining intact UCS (MPa)",
    "kind": "weather",
    "unit": 2
  },
  {
    "id": 4,
    "name": "RQD and natural fracture intensity",
    "a": [
      "Joint intensity (fractures/m)",
      5,
      0.1,
      20,
      0.1
    ],
    "b": [
      "Core-piece threshold (m)",
      0.1,
      0.1,
      0.2,
      0.01
    ],
    "output": "Expected RQD (%)",
    "kind": "rqd",
    "unit": 2
  },
  {
    "id": 5,
    "name": "Rock discontinuity spacing and sampling",
    "a": [
      "Natural joint intersections (count)",
      18,
      1,
      60,
      1
    ],
    "b": [
      "Scanline length (m)",
      6,
      1,
      20,
      0.5
    ],
    "output": "Apparent mean spacing (m)",
    "kind": "spacing",
    "unit": 3
  },
  {
    "id": 6,
    "name": "Rock slope daylighting screen",
    "a": [
      "Plane dip (degrees)",
      36,
      1,
      80,
      1
    ],
    "b": [
      "Cut-face dip (degrees)",
      66,
      10,
      89,
      1
    ],
    "output": "Geometric daylight margin (degrees)",
    "kind": "daylight",
    "unit": 3
  },
  {
    "id": 7,
    "name": "Effective stress under a water table",
    "a": [
      "Depth (m)",
      12,
      1,
      40,
      0.5
    ],
    "b": [
      "Water-table depth (m)",
      4,
      0,
      25,
      0.5
    ],
    "output": "Vertical effective stress (kPa)",
    "kind": "effstress",
    "unit": 4
  },
  {
    "id": 8,
    "name": "Fractured-rock Darcy flow",
    "a": [
      "Head difference (m)",
      2,
      0.05,
      10,
      0.05
    ],
    "b": [
      "Equivalent hydraulic conductivity (m/s)",
      0.0001,
      1e-06,
      0.001,
      1e-06
    ],
    "output": "Flow per m\u00b2 (L/s)",
    "kind": "darcy",
    "unit": 4
  },
  {
    "id": 9,
    "name": "Two-layer seismic refraction travel time",
    "a": [
      "Geophone offset (m)",
      45,
      1,
      100,
      1
    ],
    "b": [
      "Upper-layer thickness (m)",
      8,
      1,
      30,
      0.5
    ],
    "output": "First arrival time (ms)",
    "kind": "seismic",
    "unit": 5
  },
  {
    "id": 10,
    "name": "Parallel-path bulk resistivity",
    "a": [
      "Conductive path fraction (%)",
      10,
      0,
      50,
      1
    ],
    "b": [
      "Conductive-path resistivity (ohm-m)",
      10,
      1,
      100,
      1
    ],
    "output": "Equivalent resistivity (ohm-m)",
    "kind": "resistivity",
    "unit": 5
  },
  {
    "id": 11,
    "name": "Planar sliding factor of safety",
    "a": [
      "Failure plane dip (degrees)",
      35,
      10,
      70,
      1
    ],
    "b": [
      "Joint uplift (kN)",
      12,
      0,
      80,
      1
    ],
    "output": "Static factor of safety (-)",
    "kind": "slide",
    "unit": 6
  },
  {
    "id": 12,
    "name": "Rockfall ballistic rebound",
    "a": [
      "Normal restitution (-)",
      0.5,
      0.05,
      0.9,
      0.01
    ],
    "b": [
      "Vertical fall before impact (m)",
      12,
      1,
      40,
      0.5
    ],
    "output": "Rebound rise (m)",
    "kind": "rockfall",
    "unit": 6
  },
  {
    "id": 13,
    "name": "Circular tunnel elastic hoop stress",
    "a": [
      "Position around opening (degrees)",
      60,
      0,
      360,
      2
    ],
    "b": [
      "Horizontal / vertical stress ratio (-)",
      1.5,
      0.5,
      2.5,
      0.05
    ],
    "output": "Hoop stress (MPa)",
    "kind": "tunnel",
    "unit": 7
  },
  {
    "id": 14,
    "name": "Conceptual cavity-roof beam response",
    "a": [
      "Void span (m)",
      4,
      1,
      12,
      0.1
    ],
    "b": [
      "Rock bridge thickness (m)",
      2,
      0.5,
      6,
      0.1
    ],
    "output": "Idealized midspan deflection (mm)",
    "kind": "karst",
    "unit": 7
  },
  {
    "id": 15,
    "name": "Simplified cyclic stress ratio",
    "a": [
      "Peak ground acceleration (g)",
      0.25,
      0.05,
      0.7,
      0.01
    ],
    "b": [
      "Stress reduction factor (-)",
      0.9,
      0.65,
      1,
      0.01
    ],
    "output": "Cyclic stress ratio (-)",
    "kind": "csr",
    "unit": 8
  },
  {
    "id": 16,
    "name": "RUSLE average annual soil loss",
    "a": [
      "Topographic LS factor (-)",
      3,
      0.2,
      12,
      0.1
    ],
    "b": [
      "Vegetation/cover C factor (-)",
      0.2,
      0.02,
      1,
      0.02
    ],
    "output": "Annual soil loss (t/ha/year)",
    "kind": "erosion",
    "unit": 8
  }
];

  var MODELS = EG_SPECS.map(function(spec) {
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

    return {
      idx: spec.id,
      unit: spec.unit,
      html: html,
      init: function(card) {
        try {
          var valA = pA[1], valB = pB[1];
          var valEl = card.querySelector('.val-readout');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(pts, currX, currY) {
            if (!svgEl || !pts.length) return;
            svgEl.innerHTML = '';
            var W = 740, H = 330, L = 70, R = 22, T = 22, B = 52;
            var xs = pts.map(function(p) { return p[0]; });
            var ys = pts.map(function(p) { return p[1]; }).filter(Number.isFinite);
            var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
            var ymin = Math.min(0, Math.min.apply(null, ys), currY);
            var ymax = Math.max.apply(null, ys);
            if (ymax <= ymin) ymax = ymin + 1;

            var xp = function(x) { return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); };
            var yp = function(y) { return H - B - (y - ymin) / (ymax - ymin || 1) * (H - T - B); };

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }

            for (var i = 0; i <= 4; i++) {
              var v = ymin + (ymax - ymin) * i / 4, yPos = yp(v);
              node('line', { x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '3 3' });
              node('text', { x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }, Number(v.toPrecision(3)).toString());
            }
            node('line', { x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' });
            node('line', { x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' });

            var pathPts = pts.map(function(d) { return xp(d[0]).toFixed(1) + ',' + yp(d[1]).toFixed(1); }).join(' ');
            node('polyline', { points: pathPts, fill: 'none', stroke: '#4f46e5', 'stroke-width': '2.5' });

            if (Number.isFinite(currY)) {
              node('circle', { cx: xp(currX), cy: yp(currY), r: 6, fill: '#f59e0b', stroke: '#ffffff', 'stroke-width': '2' });
            }
            node('text', { x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }, pA[0]);
          }

          function render() {
            var inpA = card.querySelector('#eg_' + spec.id + '_a');
            var inpB = card.querySelector('#eg_' + spec.id + '_b');
            if (inpA) {
              valA = Number(inpA.value);
              var lblA = card.querySelector('#v_eg_' + spec.id + '_a');
              if (lblA) lblA.textContent = inpA.value;
            }
            if (inpB) {
              valB = Number(inpB.value);
              var lblB = card.querySelector('#v_eg_' + spec.id + '_b');
              if (lblB) lblB.textContent = inpB.value;
            }

            var res = egCalc(spec.id, valA, valB);
            if (valEl) {
              valEl.textContent = Number.isFinite(res) ? Number(res.toPrecision(4)) : '--';
            }

            var pts = [];
            for (var k = 0; k <= 50; k++) {
              var aX = pA[2] + (pA[3] - pA[2]) * k / 50;
              var ptRes = egCalc(spec.id, aX, valB);
              if (Number.isFinite(ptRes)) pts.push([aX, ptRes]);
            }
            drawGraph(pts, valA, res);
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', render);
          });
          render();
        } catch(err) {
          console.error('EG sim error on lab ' + spec.id, err);
        }
      }
    };
  });

  if (!window.SimulationEngine) window.SimulationEngine = {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId) ||
                    document.getElementById('sim-container') ||
                    document.querySelector('.simulation-slot');
    if (!container) return;
    container.innerHTML = '';
    var unitNum = 1;
    if (simType) {
      var m = simType.match(/(\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    } else {
      var bMatch = document.body.dataset.chapterIndex;
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') unitNum = parseInt(bMatch, 10) + 1;
      else {
        var pMatch = window.location.pathname.match(/chapter-(\d+)/);
        if (pMatch) unitNum = parseInt(pMatch[1], 10);
      }
    }
    if (isNaN(unitNum) || unitNum < 1 || unitNum > 8) unitNum = 1;
    var modelsForUnit = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.filter(function(m) { return m.unit === 1; });
    modelsForUnit.forEach(function(m) {
      var card = document.createElement('section');
      card.className = 'ce-sim-card';
      card.setAttribute('aria-label', 'Interactive Simulation ' + m.idx);
      card.id = 'sim-card-' + m.idx;
      card.innerHTML = m.html;
      container.appendChild(card);
      m.init(card);
    });
  };

  if (typeof document !== 'undefined') {
    var autoInit = function() {
      var slot = document.getElementById('sim-container') || document.querySelector('.simulation-slot');
      if (slot && slot.children.length === 0) {
        window.SimulationEngine.initSimulation(slot.id || 'sim-container');
      }
    };
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', autoInit);
    } else {
      autoInit();
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
