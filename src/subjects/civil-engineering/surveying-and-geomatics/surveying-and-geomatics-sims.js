/* Surveying and Geomatics Interactive Simulation Suite */
(function(window) {
  'use strict';

  function sgCalc(id, p) {
    switch(id) {
      case 1: { const c = p.L * (p.alpha * 1e-6) * (p.T - 20); return { value: p.L + c, other: 'Correction: ' + (c * 1000).toFixed(2) + ' mm' }; }
      case 2: { const H = Math.sqrt(Math.max(0, p.S * p.S - p.dh * p.dh)); return { value: H, other: 'Slope reduction: ' + (p.S - H).toFixed(4) + ' m' }; }
      case 3: { return { value: -p.bias / p.n, other: 'Total misclosure: ' + p.bias.toFixed(3) + ' arcsec' }; }
      case 4: { const f = p.BS - p.FS - p.known; return { value: f * 1000, other: 'Corrected rise: ' + (p.BS - p.FS - f).toFixed(4) + ' m' }; }
      case 5: { const c = (1 - p.k) * Math.pow(p.d * 1000, 2) / (2 * p.R * 1000); return { value: c, other: 'Magnitude: ' + (c * 1000).toFixed(1) + ' mm' }; }
      case 6: { const L = 2 * p.E + 2 * p.N; return { value: -p.mis * p.E / L, other: 'Perimeter: ' + L.toFixed(1) + ' m' }; }
      case 7: { const w1 = 1 / (0.01 * 0.01), w2 = 1 / Math.pow(p.sigma2 / 100, 2); return { value: (w1 * p.x1 + w2 * p.x2) / (w1 + w2), other: 'Uncertainty: ' + (100 * Math.sqrt(1 / (w1 + w2))).toFixed(3) + ' cm' }; }
      case 8: { return { value: p.height * (p.width + p.skew / 2), other: 'Trapezoidal bounds evaluated' }; }
      case 9: { return { value: p.uere * p.hdop, other: 'Vertical: ' + (p.uere * p.vdop).toFixed(3) + ' m' }; }
      case 10: { return { value: p.h - p.N, other: 'Declared geoid error: ±' + p.nerr.toFixed(2) + ' m' }; }
      case 11: { const gsd = p.H * (p.pitch / 1000) / p.f * 100; return { value: gsd, other: 'Ground pixel: ' + (gsd / 100).toFixed(4) + ' m' }; }
      case 12: { const Z = p.B * 100 / p.p; return { value: p.H - Z, other: 'Range: ' + Z.toFixed(2) + ' m' }; }
      case 13: { return { value: p.PRF * 1000 / (p.v * p.W), other: 'Acquisition area: ' + (p.v * p.W).toFixed(0) + ' m²/s' }; }
      case 14: { const T = p.R * Math.tan(p.Delta / 2 * Math.PI / 180); return { value: T, other: 'Curve length: ' + (p.R * p.Delta * Math.PI / 180).toFixed(2) + ' m' }; }
      case 15: { return { value: p.L * (p.A1 + p.A2) / 2, other: 'End-area volume' }; }
      case 16: { const rmse = Math.sqrt(p.eX * p.eX + p.eY * p.eY); return { value: rmse, other: '95% error circle: ' + (2.4477 * rmse).toFixed(3) + ' m' }; }
      default: return { value: NaN, other: '' };
    }
  }

  var SG_LABS = [
  {
    "id": 1,
    "name": "EDM temperature correction",
    "subtitle": "A steel-tape temperature model, not an EDM atmospheric model",
    "params": [
      {
        "id": "L",
        "label": "Observed tape length (m)",
        "min": 80,
        "max": 250,
        "default": 120,
        "step": 1
      },
      {
        "id": "T",
        "label": "Tape temperature (\u00b0C)",
        "min": -5,
        "max": 50,
        "default": 30,
        "step": 1
      },
      {
        "id": "alpha",
        "label": "Expansion (\u00b5m/m/\u00b0C)",
        "min": 8,
        "max": 15,
        "default": 11.5,
        "step": 0.5
      }
    ],
    "unit": "m",
    "ylabel": "Corrected physical length",
    "caution": "Correction applies to tape scale only; reference T\u2080=20\u00b0C. Tension, sag and calibration omitted."
  },
  {
    "id": 2,
    "name": "Slope-to-horizontal reduction",
    "subtitle": "Convert a sloped total-station line to a horizontal span",
    "params": [
      {
        "id": "S",
        "label": "Slope distance (m)",
        "min": 30,
        "max": 300,
        "default": 125,
        "step": 1
      },
      {
        "id": "dh",
        "label": "Height difference (m)",
        "min": 0,
        "max": 50,
        "default": 15,
        "step": 0.5
      },
      {
        "id": "unused",
        "label": "Target centering tolerance (mm)",
        "min": 0,
        "max": 10,
        "default": 2,
        "step": 1
      }
    ],
    "unit": "m",
    "ylabel": "Horizontal distance",
    "caution": "Vertical offset refers to target and instrument centers; Earth curvature and grid scale omitted."
  },
  {
    "id": 3,
    "name": "Polygon angle misclosure",
    "subtitle": "Distribute an angular closure under equal observation reliability",
    "params": [
      {
        "id": "n",
        "label": "Number of polygon sides",
        "min": 3,
        "max": 12,
        "default": 5,
        "step": 1
      },
      {
        "id": "bias",
        "label": "Total angle excess (arcseconds)",
        "min": -90,
        "max": 90,
        "default": 25,
        "step": 1
      },
      {
        "id": "weight",
        "label": "Weight ratio diagnostic",
        "min": 1,
        "max": 5,
        "default": 1,
        "step": 1
      }
    ],
    "unit": "arcsec",
    "ylabel": "Equal correction per angle",
    "caution": "Equal weighting only; a weighted angular adjustment requires per-angle variances."
  },
  {
    "id": 4,
    "name": "Leveling line adjustment",
    "subtitle": "Distribute measured height misclosure by run length",
    "params": [
      {
        "id": "BS",
        "label": "Sum of backsights (m)",
        "min": 1,
        "max": 8,
        "default": 4.546,
        "step": 0.001
      },
      {
        "id": "FS",
        "label": "Sum of foresights (m)",
        "min": 1,
        "max": 8,
        "default": 2.5,
        "step": 0.001
      },
      {
        "id": "known",
        "label": "Known elevation rise (m)",
        "min": -2,
        "max": 5,
        "default": 2.014,
        "step": 0.001
      }
    ],
    "unit": "mm",
    "ylabel": "Leveling closure",
    "caution": "The simplified correction assumes length-proportional random-error growth and valid benchmark control."
  },
  {
    "id": 5,
    "name": "Curvature and refraction",
    "subtitle": "Approximate level-sight curvature-refraction displacement",
    "params": [
      {
        "id": "d",
        "label": "Sight distance (km)",
        "min": 0.1,
        "max": 3,
        "default": 1,
        "step": 0.05
      },
      {
        "id": "k",
        "label": "Refraction coefficient",
        "min": 0,
        "max": 0.3,
        "default": 0.13,
        "step": 0.01
      },
      {
        "id": "R",
        "label": "Earth radius (km)",
        "min": 6300,
        "max": 6400,
        "default": 6371,
        "step": 1
      }
    ],
    "unit": "m",
    "ylabel": "Net curvature-refraction magnitude",
    "caution": "This is a highly idealized combined magnitude. Refraction can change rapidly; sign convention must be declared."
  },
  {
    "id": 6,
    "name": "Traverse Bowditch correction",
    "subtitle": "Explore coordinate closure and correction allocation",
    "params": [
      {
        "id": "E",
        "label": "Nominal east/west leg length (m)",
        "min": 40,
        "max": 300,
        "default": 120,
        "step": 5
      },
      {
        "id": "N",
        "label": "Nominal north/south leg length (m)",
        "min": 40,
        "max": 300,
        "default": 90,
        "step": 5
      },
      {
        "id": "mis",
        "label": "East closure error (mm)",
        "min": -80,
        "max": 80,
        "default": 40,
        "step": 1
      }
    ],
    "unit": "mm",
    "ylabel": "East correction on first leg",
    "caution": "Simplified rectangle with east closure error on return leg; no angular stochastic model."
  },
  {
    "id": 7,
    "name": "Weighted coordinate estimation",
    "subtitle": "Combine two independent observations with different precisions",
    "params": [
      {
        "id": "x1",
        "label": "First position estimate (m)",
        "min": 95,
        "max": 105,
        "default": 100.01,
        "step": 0.01
      },
      {
        "id": "x2",
        "label": "Second position estimate (m)",
        "min": 95,
        "max": 105,
        "default": 99.99,
        "step": 0.01
      },
      {
        "id": "sigma2",
        "label": "Second standard error (cm)",
        "min": 0.5,
        "max": 10,
        "default": 2,
        "step": 0.5
      }
    ],
    "unit": "m",
    "ylabel": "Weighted position estimate",
    "caution": "First observation standard error fixed at 1 cm; both observations assumed independent and unbiased."
  },
  {
    "id": 8,
    "name": "Shoelace land area",
    "subtitle": "Calculate area of a four-corner skewed parcel",
    "params": [
      {
        "id": "width",
        "label": "Base width (m)",
        "min": 5,
        "max": 80,
        "default": 20,
        "step": 1
      },
      {
        "id": "height",
        "label": "Parcel height (m)",
        "min": 5,
        "max": 70,
        "default": 10,
        "step": 1
      },
      {
        "id": "skew",
        "label": "Top right corner offset (m)",
        "min": -10,
        "max": 20,
        "default": 4,
        "step": 1
      }
    ],
    "unit": "m\u00b2",
    "ylabel": "Area of parcel",
    "caution": "Planar coordinates only; requires simple non-self-crossing polygon in a suitable map projection."
  },
  {
    "id": 9,
    "name": "GNSS geometry and DOP",
    "subtitle": "Estimate geometry-scaled uncertainty under fixed ranging noise",
    "params": [
      {
        "id": "uere",
        "label": "User equivalent range error (m)",
        "min": 0.1,
        "max": 3,
        "default": 0.7,
        "step": 0.1
      },
      {
        "id": "hdop",
        "label": "Horizontal DOP",
        "min": 0.8,
        "max": 8,
        "default": 1.6,
        "step": 0.1
      },
      {
        "id": "vdop",
        "label": "Vertical DOP",
        "min": 1,
        "max": 12,
        "default": 2.5,
        "step": 0.1
      }
    ],
    "unit": "m",
    "ylabel": "Simplified horizontal error scale",
    "caution": "HDOP\u00d7UERE is a conceptual illustration; field accuracy depends on multipath, modes, corrections, systematics."
  },
  {
    "id": 10,
    "name": "Ellipsoid-geoid-orthometric heights",
    "subtitle": "Explore height conversion across a specified reference model",
    "params": [
      {
        "id": "h",
        "label": "Ellipsoid height h (m)",
        "min": 0,
        "max": 150,
        "default": 58.24,
        "step": 0.01
      },
      {
        "id": "N",
        "label": "Geoid separation N (m)",
        "min": -40,
        "max": 40,
        "default": -17.65,
        "step": 0.05
      },
      {
        "id": "nerr",
        "label": "Geoid model uncertainty (m)",
        "min": 0,
        "max": 0.5,
        "default": 0.1,
        "step": 0.01
      }
    ],
    "unit": "m",
    "ylabel": "Orthometric height H",
    "caution": "Formula valid only with compatible vertical datum/frame and identified geoid model; no site-specific guarantee."
  },
  {
    "id": 11,
    "name": "Photogrammetry ground sampling",
    "subtitle": "Relate flight height and camera geometry to nominal GSD",
    "params": [
      {
        "id": "H",
        "label": "Height above terrain (m)",
        "min": 40,
        "max": 500,
        "default": 120,
        "step": 5
      },
      {
        "id": "pitch",
        "label": "Pixel pitch (\u00b5m)",
        "min": 1,
        "max": 8,
        "default": 2.4,
        "step": 0.1
      },
      {
        "id": "f",
        "label": "Focal length (mm)",
        "min": 12,
        "max": 60,
        "default": 24,
        "step": 1
      }
    ],
    "unit": "cm",
    "ylabel": "Nominal ground sampling distance",
    "caution": "Nadir pinhole-camera approximation. Image footprint is not positional accuracy; terrain relief changes actual GSD."
  },
  {
    "id": 12,
    "name": "Ideal stereo height",
    "subtitle": "Understand parallax-height sensitivity",
    "params": [
      {
        "id": "B",
        "label": "Camera baseline (m)",
        "min": 40,
        "max": 180,
        "default": 120,
        "step": 5
      },
      {
        "id": "p",
        "label": "Image parallax (mm)",
        "min": 12,
        "max": 35,
        "default": 20,
        "step": 0.5
      },
      {
        "id": "H",
        "label": "Camera height above datum (m)",
        "min": 400,
        "max": 1100,
        "default": 700,
        "step": 10
      }
    ],
    "unit": "m",
    "ylabel": "Estimated object elevation",
    "caution": "Assumes ideal vertical stereo, f=100 mm, and matched units; not a complete bundle-adjustment solution."
  },
  {
    "id": 13,
    "name": "Lidar acquisition point density",
    "subtitle": "Estimate average pulse density from flight parameters",
    "params": [
      {
        "id": "PRF",
        "label": "Laser pulses per second (kHz)",
        "min": 50,
        "max": 500,
        "default": 200,
        "step": 10
      },
      {
        "id": "v",
        "label": "Airborne speed (m/s)",
        "min": 20,
        "max": 100,
        "default": 50,
        "step": 5
      },
      {
        "id": "W",
        "label": "Nominal swath width (m)",
        "min": 100,
        "max": 1000,
        "default": 400,
        "step": 20
      }
    ],
    "unit": "pulses/m\u00b2",
    "ylabel": "Ideal acquisition pulse density",
    "caution": "Uniform distribution assumed; excludes scan geometry, multiple returns, overlap, filtering and ground visibility."
  },
  {
    "id": 14,
    "name": "Horizontal circular curve",
    "subtitle": "Compute arc and tangent geometry for route staking",
    "params": [
      {
        "id": "R",
        "label": "Curve radius (m)",
        "min": 60,
        "max": 1000,
        "default": 300,
        "step": 10
      },
      {
        "id": "Delta",
        "label": "Intersection angle (degrees)",
        "min": 5,
        "max": 85,
        "default": 30,
        "step": 1
      },
      {
        "id": "unused",
        "label": "Stake interval (m)",
        "min": 5,
        "max": 50,
        "default": 20,
        "step": 5
      }
    ],
    "unit": "m",
    "ylabel": "Curve tangent length",
    "caution": "Simple circular curve only, not spiral transitions, superelevation or design speed standards."
  },
  {
    "id": 15,
    "name": "Road grade and chainage",
    "subtitle": "Convert elevation differences to longitudinal grade",
    "params": [
      {
        "id": "dz",
        "label": "End minus start elevation (m)",
        "min": -10,
        "max": 12,
        "default": 2.8,
        "step": 0.1
      },
      {
        "id": "chain",
        "label": "Horizontal chainage separation (m)",
        "min": 20,
        "max": 500,
        "default": 140,
        "step": 5
      },
      {
        "id": "offset",
        "label": "Station zero (m)",
        "min": 0,
        "max": 1000,
        "default": 0,
        "step": 20
      }
    ],
    "unit": "%",
    "ylabel": "Longitudinal grade",
    "caution": "Straight-grade segment approximation; vertical curves and local slope variability omitted."
  },
  {
    "id": 16,
    "name": "Deformation time-series trend",
    "subtitle": "Fit a straight displacement rate to synthetic monitoring epochs",
    "params": [
      {
        "id": "rate",
        "label": "True modeled trend (mm/month)",
        "min": -10,
        "max": 10,
        "default": 2,
        "step": 0.5
      },
      {
        "id": "noise",
        "label": "Alternating measurement disturbance (mm)",
        "min": 0,
        "max": 6,
        "default": 1.5,
        "step": 0.5
      },
      {
        "id": "offset",
        "label": "Initial displacement (mm)",
        "min": -10,
        "max": 10,
        "default": 0,
        "step": 1
      }
    ],
    "unit": "mm/month",
    "ylabel": "OLS estimated movement rate",
    "caution": "Illustrative independent synthetic epochs, not a structural safety threshold; reference stability unverified."
  }
];

  var MODELS = SG_LABS.map(function(lab) {
    var unitNum = ((lab.id - 1) >> 1) + 1;
    var controlsHtml = lab.params.map(function(p) {
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="sg_' + lab.id + '_' + p.id + '">' + p.label + ': <span id="v_sg_' + lab.id + '_' + p.id + '" style="font-weight:700;color:#0284c7;">' + p.default + '</span></label>' +
             '<input id="sg_' + lab.id + '_' + p.id + '" data-pid="' + p.id + '" type="range" min="' + p.min + '" max="' + p.max + '" step="' + p.step + '" value="' + p.default + '" style="width:100%;accent-color:#0284c7;"></div>';
    }).join('');

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

    return {
      idx: lab.id,
      unit: unitNum,
      html: html,
      init: function(card) {
        try {
          var pVals = {};
          lab.params.forEach(function(p) { pVals[p.id] = p.default; });
          var valEl = card.querySelector('.val-readout');
          var interpEl = card.querySelector('.interp-text');
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
            node('polyline', { points: pathPts, fill: 'none', stroke: '#0284c7', 'stroke-width': '2.5' });

            if (Number.isFinite(currY)) {
              node('circle', { cx: xp(currX), cy: yp(currY), r: 6, fill: '#ea580c', stroke: '#ffffff', 'stroke-width': '2' });
            }
            node('text', { x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }, lab.params[0].label);
          }

          function render() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var pKey = inp.dataset.pid;
              pVals[pKey] = Number(inp.value);
              var vLbl = card.querySelector('#v_sg_' + lab.id + '_' + pKey);
              if (vLbl) vLbl.textContent = inp.value;
            });

            var res = sgCalc(lab.id, pVals);
            if (valEl) {
              valEl.textContent = Number.isFinite(res.value) ? Number(res.value.toPrecision(5)) + ' ' + (lab.unit || '') : '--';
            }
            if (interpEl) interpEl.textContent = res.other || '';

            var pts = [];
            var p0 = lab.params[0];
            for (var s = 0; s <= 50; s++) {
              var xV = p0.min + (p0.max - p0.min) * s / 50;
              var curP = Object.assign({}, pVals);
              curP[p0.id] = xV;
              var ptRes = sgCalc(lab.id, curP);
              if (Number.isFinite(ptRes.value)) pts.push([xV, ptRes.value]);
            }
            drawGraph(pts, pVals[p0.id], res.value);
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', render);
          });
          render();
        } catch(err) {
          console.error('SG sim error on lab ' + lab.id, err);
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
