/* Fluid Mechanics and Hydraulics Interactive Simulation Suite */
(function(window) {
  'use strict';

  const G = 9.81;
  const LABS={
 hydrostatic:p=>[p[0]*p[2]*p[1]/1000,`Pressure increases linearly with vertical depth.`],
 orifice:p=>{let A=Math.PI*(p[1]/1000)**2/4;return [1000*p[2]*A*Math.sqrt(2*G*p[0]),`This neglects downstream submergence and upstream velocity.`]},
 gate:p=>[p[2]*G*p[1]*p[0]*p[0]/2000,`Center of pressure = ${(2*p[0]/3).toFixed(3)} m below the surface.`],
 float:p=>[Math.min(1,p[0]/p[1])*p[2],p[0]>=p[1]?`Density is at least water density: this body cannot float freely.`:`Freeboard = ${(p[2]*(1-p[0]/p[1])).toFixed(3)} m.`],
 pipe:p=>{let Q=p[0]/1000,D=p[1]/1000,L=p[2],e=p[3]/1000,A=Math.PI*D*D/4,V=Q/A,Re=998*V*D/0.001002;let f=Re<2300?64/Re:Re>4000?0.25/Math.log10(e/(3.7*D)+5.74/(Re**0.9))**2:(64/2300)*(4000-Re)/1700+(0.25/Math.log10(e/(3.7*D)+5.74/(4000**0.9))**2)*(Re-2300)/1700;return [f*(L/D)*(V*V/(2*G)),`Re=${Re.toFixed(0)}; Darcy friction factor=${f.toFixed(4)}. Transition is interpolated and uncertain.`]},
 parallel:p=>{let qa=p[0]/(1+Math.sqrt(p[1]/p[2]));return [qa,`Branch B flow = ${(p[0]-qa).toFixed(2)} L/s; quadratic branch-loss approximation.`]},
 pump:p=>{let Q=Math.sqrt(Math.max(0,(p[0]-p[1])/(p[2]+p[3])));return [1000*Q,`Operating head = ${(p[1]+p[3]*Q*Q).toFixed(2)} m; simplified quadratic curves.`]},
 npsh:p=>[p[0]-p[1]-p[2]-p[3],`Compare with vendor NPSHr plus appropriate margin, not with zero alone.`],
 manning:p=>{let A=p[0]*p[1],P=p[0]+2*p[1],R=A/P;return [A*(R**(2/3))*Math.sqrt(p[2])/p[3],`Area=${A.toFixed(2)} m²; hydraulic radius=${R.toFixed(3)} m.`]},
 critical:p=>{let yc=(p[0]*p[0]/G)**(1/3),Fr=p[0]/(p[1]*Math.sqrt(G*p[1]));return [yc,`Froude number at chosen actual depth = ${Fr.toFixed(3)} (${Fr<1?'subcritical':Fr>1?'supercritical':'critical'}).`]},
 jump:p=>{let Fr=p[1]/Math.sqrt(G*p[0]);if(Fr<=1)return [p[0],`Fr₁=${Fr.toFixed(2)} ≤ 1: no classical supercritical-to-subcritical jump.`];let y2=p[0]/2*(Math.sqrt(1+8*Fr*Fr)-1);let loss=(y2-p[0])**3/(4*p[0]*y2);return [y2,`Fr₁=${Fr.toFixed(2)}, specific-energy loss=${loss.toFixed(3)} m.`]},
 weir:p=>[(2/3)*p[2]*p[1]*Math.sqrt(2*G)*p[0]**1.5,`Free, fully aerated sharp-crested flow only; meter head above crest.`],
 venturi:p=>{let d1=p[1]/1000,d2=p[2]/1000;if(d2>=d1)return [NaN,'Throat diameter must be smaller than inlet diameter.'];let A2=Math.PI*d2*d2/4,beta=d2/d1;return [1000*p[3]*A2*Math.sqrt(2*p[0]*1000/(998*(1-beta**4))),`Assumes single-phase water, incompressible flow and calibrated pressure taps.`]},
 culvert:p=>[p[2]*(Math.PI*p[1]*p[1]/4)*Math.sqrt(2*G*p[0]),`Submerged-orifice capacity only: not inlet-control/outlet-control culvert rating.`],
 scale:p=>[p[1]/1000*p[0]**2.5,`Velocity scale = ${(Math.sqrt(p[0])).toFixed(2)}; model turbulence similarity not established.`],
 uncertainty:p=>{let q=p[0]/1000*(1+p[1]/100),D=p[2]/1000,V=q/(Math.PI*D*D/4);let worst=0.02*(p[3]/D)*V*V/(2*G);let qlow=p[0]/1000*(1-p[1]/100),Vlow=qlow/(Math.PI*D*D/4);return [worst,`Low-discharge estimate = ${(0.02*(p[3]/D)*Vlow*Vlow/(2*G)).toFixed(3)} m; fixed f and no probability claim.`]}
};

  var FM_SPECS = [
  {
    "idx": 1,
    "unit": 1,
    "title": "Hydrostatic pressure profile",
    "desc": "Pressure against adjustable physical inputs",
    "kind": "hydrostatic",
    "controls": [
      [
        "Density",
        "kg/m\u00b3",
        998,
        850,
        1250,
        1
      ],
      [
        "Depth",
        "m",
        3,
        0.2,
        12,
        0.1
      ],
      [
        "Gravity",
        "m/s\u00b2",
        9.81,
        8,
        11,
        0.01
      ]
    ],
    "output": "Pressure",
    "outputUnit": "kPa"
  },
  {
    "idx": 2,
    "unit": 1,
    "title": "Reservoir-orifice discharge",
    "desc": "Discharge against adjustable physical inputs",
    "kind": "orifice",
    "controls": [
      [
        "Head",
        "m",
        4,
        0.2,
        18,
        0.1
      ],
      [
        "Orifice diameter",
        "mm",
        80,
        20,
        250,
        5
      ],
      [
        "Discharge coefficient",
        "\u2013",
        0.62,
        0.45,
        0.95,
        0.01
      ]
    ],
    "output": "Discharge",
    "outputUnit": "L/s"
  },
  {
    "idx": 3,
    "unit": 2,
    "title": "Submerged gate force",
    "desc": "Resultant horizontal force against adjustable physical inputs",
    "kind": "gate",
    "controls": [
      [
        "Water depth",
        "m",
        3.2,
        0.4,
        10,
        0.1
      ],
      [
        "Gate width",
        "m",
        2,
        0.3,
        8,
        0.1
      ],
      [
        "Density",
        "kg/m\u00b3",
        998,
        850,
        1250,
        1
      ]
    ],
    "output": "Resultant horizontal force",
    "outputUnit": "kN"
  },
  {
    "idx": 4,
    "unit": 2,
    "title": "Floating pontoon immersion",
    "desc": "Immersed height against adjustable physical inputs",
    "kind": "float",
    "controls": [
      [
        "Pontoon density",
        "kg/m\u00b3",
        580,
        100,
        1100,
        10
      ],
      [
        "Water density",
        "kg/m\u00b3",
        1000,
        850,
        1100,
        10
      ],
      [
        "Pontoon height",
        "m",
        1.5,
        0.3,
        5,
        0.1
      ]
    ],
    "output": "Immersed height",
    "outputUnit": "m"
  },
  {
    "idx": 5,
    "unit": 3,
    "title": "Darcy pipe friction and Reynolds regime",
    "desc": "Friction headloss against adjustable physical inputs",
    "kind": "pipe",
    "controls": [
      [
        "Discharge",
        "L/s",
        20,
        1,
        90,
        1
      ],
      [
        "Internal diameter",
        "mm",
        150,
        50,
        400,
        5
      ],
      [
        "Pipe length",
        "m",
        220,
        20,
        1000,
        10
      ],
      [
        "Roughness",
        "mm",
        0.08,
        0.005,
        1,
        0.005
      ]
    ],
    "output": "Friction headloss",
    "outputUnit": "m"
  },
  {
    "idx": 6,
    "unit": 3,
    "title": "Parallel pipe flow distribution",
    "desc": "Branch A flow against adjustable physical inputs",
    "kind": "parallel",
    "controls": [
      [
        "Total flow",
        "L/s",
        90,
        5,
        250,
        5
      ],
      [
        "Branch A resistance",
        "s\u00b2/m\u2075",
        850,
        80,
        2500,
        10
      ],
      [
        "Branch B resistance",
        "s\u00b2/m\u2075",
        1500,
        80,
        2500,
        10
      ]
    ],
    "output": "Branch A flow",
    "outputUnit": "L/s"
  },
  {
    "idx": 7,
    "unit": 4,
    "title": "Pump-system intersection",
    "desc": "Operating flow against adjustable physical inputs",
    "kind": "pump",
    "controls": [
      [
        "Pump shutoff head",
        "m",
        48,
        15,
        90,
        1
      ],
      [
        "Static head",
        "m",
        12,
        0,
        65,
        1
      ],
      [
        "Pump curve factor",
        "m/(m\u00b3/s)\u00b2",
        2400,
        400,
        6000,
        100
      ],
      [
        "System curve factor",
        "m/(m\u00b3/s)\u00b2",
        1800,
        300,
        7000,
        100
      ]
    ],
    "output": "Operating flow",
    "outputUnit": "L/s"
  },
  {
    "idx": 8,
    "unit": 4,
    "title": "NPSH availability screen",
    "desc": "Available NPSH against adjustable physical inputs",
    "kind": "npsh",
    "controls": [
      [
        "Atmospheric head",
        "m water",
        10.3,
        7,
        11,
        0.1
      ],
      [
        "Vapor pressure head",
        "m water",
        0.25,
        0.1,
        2.5,
        0.05
      ],
      [
        "Suction lift",
        "m",
        3,
        0,
        9,
        0.1
      ],
      [
        "Suction friction loss",
        "m",
        1.1,
        0,
        4,
        0.1
      ]
    ],
    "output": "Available NPSH",
    "outputUnit": "m"
  },
  {
    "idx": 9,
    "unit": 5,
    "title": "Manning channel flow",
    "desc": "Uniform flow estimate against adjustable physical inputs",
    "kind": "manning",
    "controls": [
      [
        "Channel width",
        "m",
        4,
        1,
        20,
        0.2
      ],
      [
        "Flow depth",
        "m",
        1.2,
        0.15,
        4,
        0.05
      ],
      [
        "Bed slope",
        "m/m",
        0.001,
        0.0001,
        0.01,
        0.0001
      ],
      [
        "Manning n",
        "s/m^(1/3)",
        0.025,
        0.011,
        0.06,
        0.001
      ]
    ],
    "output": "Uniform flow estimate",
    "outputUnit": "m\u00b3/s"
  },
  {
    "idx": 10,
    "unit": 5,
    "title": "Critical flow in rectangular channel",
    "desc": "Critical depth against adjustable physical inputs",
    "kind": "critical",
    "controls": [
      [
        "Flow per unit width",
        "m\u00b2/s",
        3.0,
        0.2,
        10,
        0.1
      ],
      [
        "Actual depth",
        "m",
        1.3,
        0.2,
        5,
        0.05
      ]
    ],
    "output": "Critical depth",
    "outputUnit": "m"
  },
  {
    "idx": 11,
    "unit": 6,
    "title": "Hydraulic jump conjugate depth",
    "desc": "Sequent depth against adjustable physical inputs",
    "kind": "jump",
    "controls": [
      [
        "Upstream depth",
        "m",
        0.45,
        0.1,
        1.5,
        0.05
      ],
      [
        "Upstream velocity",
        "m/s",
        7,
        2,
        15,
        0.25
      ]
    ],
    "output": "Sequent depth",
    "outputUnit": "m"
  },
  {
    "idx": 12,
    "unit": 6,
    "title": "Sharp-crested weir rating",
    "desc": "Free-overflow discharge against adjustable physical inputs",
    "kind": "weir",
    "controls": [
      [
        "Head above crest",
        "m",
        0.3,
        0.05,
        1.2,
        0.01
      ],
      [
        "Crest width",
        "m",
        2.0,
        0.3,
        6.0,
        0.1
      ],
      [
        "Discharge coefficient",
        "\u2013",
        0.62,
        0.4,
        0.85,
        0.01
      ]
    ],
    "output": "Free-overflow discharge",
    "outputUnit": "m\u00b3/s"
  },
  {
    "idx": 13,
    "unit": 7,
    "title": "Venturi pressure differential",
    "desc": "Volumetric discharge against adjustable physical inputs",
    "kind": "venturi",
    "controls": [
      [
        "Pressure difference",
        "kPa",
        14,
        0.5,
        80,
        0.5
      ],
      [
        "Inlet diameter",
        "mm",
        180,
        100,
        400,
        10
      ],
      [
        "Throat diameter",
        "mm",
        100,
        35,
        160,
        5
      ],
      [
        "Discharge coefficient",
        "\u2013",
        0.98,
        0.8,
        1,
        0.01
      ]
    ],
    "output": "Volumetric discharge",
    "outputUnit": "L/s"
  },
  {
    "idx": 14,
    "unit": 7,
    "title": "Submerged outlet capacity screening",
    "desc": "Idealized discharge against adjustable physical inputs",
    "kind": "culvert",
    "controls": [
      [
        "Water-head difference",
        "m",
        2.5,
        0.1,
        10,
        0.1
      ],
      [
        "Circular outlet diameter",
        "m",
        0.9,
        0.3,
        3,
        0.05
      ],
      [
        "Discharge coefficient",
        "\u2013",
        0.65,
        0.4,
        0.9,
        0.01
      ]
    ],
    "output": "Idealized discharge",
    "outputUnit": "m\u00b3/s"
  },
  {
    "idx": 15,
    "unit": 8,
    "title": "Froude physical-model similarity",
    "desc": "Prototype discharge against adjustable physical inputs",
    "kind": "scale",
    "controls": [
      [
        "Prototype/model length ratio",
        "\u2013",
        25,
        4,
        100,
        1
      ],
      [
        "Model flow",
        "L/s",
        8,
        0.5,
        50,
        0.5
      ]
    ],
    "output": "Prototype discharge",
    "outputUnit": "m\u00b3/s"
  },
  {
    "idx": 16,
    "unit": 8,
    "title": "Uncertainty and sensitivity of pipe loss",
    "desc": "Worst-case friction head against adjustable physical inputs",
    "kind": "uncertainty",
    "controls": [
      [
        "Nominal pipe discharge",
        "L/s",
        20,
        2,
        70,
        1
      ],
      [
        "Uncertainty in discharge",
        "%",
        10,
        1,
        30,
        1
      ],
      [
        "Diameter",
        "mm",
        160,
        60,
        350,
        5
      ],
      [
        "Pipe length",
        "m",
        250,
        20,
        600,
        10
      ]
    ],
    "output": "Worst-case friction head",
    "outputUnit": "m"
  }
];

  var MODELS = FM_SPECS.map(function(spec) {
    var controlsHtml = spec.controls.map(function(c, ci) {
      var name = c[0], unit = c[1], def = c[2], min = c[3], max = c[4], step = c[5];
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="fm_' + spec.idx + '_' + ci + '">' + name + ' <span class="unit" style="color:#64748b;">(' + unit + ')</span>: <span id="v_fm_' + spec.idx + '_' + ci + '" style="font-weight:700;color:#0284c7;">' + def + '</span></label>' +
             '<input id="fm_' + spec.idx + '_' + ci + '" data-cidx="' + ci + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + def + '" style="width:100%;accent-color:#0284c7;"></div>';
    }).join('');

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#e0f2fe;color:#0369a1;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Lab ' + spec.idx + ' · Unit ' + spec.unit + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + spec.title + '</h3>' +
               '<p style="margin:0 0 1rem 0;color:#475569;font-size:0.9rem;">' + spec.desc + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#f0fdf4;border-left:4px solid #16a34a;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div style="font-size:0.8rem;color:#166534;font-weight:600;text-transform:uppercase;">' + spec.output + '</div>' +
                 '<div class="val-readout" style="font-size:1.5rem;font-weight:700;color:#15803d;">--</div>' +
                 '<div class="interp-text" style="font-size:0.85rem;color:#14532d;margin-top:0.25rem;"></div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 740 330" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>';

    return {
      idx: spec.idx,
      unit: spec.unit,
      html: html,
      init: function(card) {
        try {
          var p = spec.controls.map(function(c) { return c[2]; });
          var valEl = card.querySelector('.val-readout');
          var interpEl = card.querySelector('.interp-text');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(samples, currP) {
            if (!svgEl || !samples.length) return;
            svgEl.innerHTML = '';
            var W = 740, H = 330, L = 70, R = 22, T = 22, B = 52;
            var ymin = Math.min(0, Math.min.apply(null, samples.map(function(d) { return d[1]; })));
            var ymax = Math.max.apply(null, samples.map(function(d) { return d[1]; }));
            if (ymax <= ymin) ymax = ymin + 1;
            var xmin = samples[0][0], xmax = samples[samples.length - 1][0];
            var xx = function(x) { return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); };
            var yy = function(y) { return H - B - (y - ymin) / (ymax - ymin || 1) * (H - T - B); };

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }

            for (var k = 0; k <= 4; k++) {
              var v = ymin + k * (ymax - ymin) / 4, yPos = yy(v);
              node('line', { x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '3 3' });
              node('text', { x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }, Number(v.toPrecision(3)).toString());
            }
            node('line', { x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' });
            node('line', { x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' });

            var pts = samples.map(function(d) { return xx(d[0]) + ',' + yy(d[1]); }).join(' ');
            node('polyline', { points: pts, fill: 'none', stroke: '#0284c7', 'stroke-width': '2.5' });

            var currRes = LABS[spec.kind](currP);
            var currY = currRes[0];
            if (Number.isFinite(currY)) {
              node('circle', { cx: xx(currP[0]), cy: yy(currY), r: 6, fill: '#ea580c', stroke: '#ffffff', 'stroke-width': '2' });
            }
            node('text', { x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }, spec.controls[0][0] + ' (' + spec.controls[0][1] + ')');
            node('text', { x: L, y: H - B + 18, fill: '#64748b', 'font-size': '10' }, Number(xmin.toPrecision(3)).toString());
            node('text', { x: W - R, y: H - B + 18, 'text-anchor': 'end', fill: '#64748b', 'font-size': '10' }, Number(xmax.toPrecision(3)).toString());
          }

          function render() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var ci = parseInt(inp.dataset.cidx, 10);
              p[ci] = Number(inp.value);
              var vLbl = card.querySelector('#v_fm_' + spec.idx + '_' + ci);
              if (vLbl) vLbl.textContent = inp.value;
            });

            var res = LABS[spec.kind](p);
            var val = res[0], note = res[1];
            if (valEl) {
              valEl.textContent = Number.isFinite(val) ? Number(val.toPrecision(5)) + ' ' + spec.outputUnit : 'Out of range';
            }
            if (interpEl) interpEl.textContent = note;

            // Generate sensitivity points varying first control
            var s = spec.controls[0], samples = [];
            for (var k = 0; k <= 60; k++) {
              var x = s[3] + (s[4] - s[3]) * k / 60;
              var t = p.slice();
              t[0] = x;
              var y = LABS[spec.kind](t)[0];
              if (Number.isFinite(y)) samples.push([x, y]);
            }
            drawGraph(samples, p);
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', render);
          });
          render();
        } catch(err) {
          console.error('FM sim error on lab ' + spec.idx, err);
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
