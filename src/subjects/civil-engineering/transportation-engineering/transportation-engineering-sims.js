/* Transportation Engineering Interactive Simulation Suite */
(function(window) {
  'use strict';

  function transportationCalc(key, a, b) {
    
 let y, unit, secondary='',note='';
 switch(key){
 case 'greenshields': y=a*b/4;unit='modelled veh/h/lane';secondary=`Critical density ${(b/2).toFixed(2)} veh/km/lane; critical speed ${(a/2).toFixed(2)} km/h`;break;
 case 'bottleneck': y=Math.max(0,a-b)*0.5;unit='veh accumulated in 30 min';secondary=`Net flow ${(a-b).toFixed(0)} veh/h`;break;
 case 'phf':y=(a+b)/(4*a);unit='dimensionless PHF';secondary=y>1?'Inconsistent counts: PHF above 1':'Peak-hour factor within its expected upper bound';break;
 case 'ssd':{const v=a/3.6;const reaction=2.5*v,brake=v*v/(2*9.81*b);y=reaction+brake;unit='m stopping distance';secondary=`Reaction ${reaction.toFixed(1)} m; braking ${brake.toFixed(1)} m`;break;}
 case 'curve':y=a*a/(127*(b+0.1));unit='m idealized minimum radius';secondary=`Combined lateral factor ${(b+0.1).toFixed(3)}`;break;
 case 'profile':{const L=a,g1=.03,g2=b/100,x=.5*L;y=100+g1*x+(g2-g1)*x*x/(2*L);unit='m elevation at x=L/2';secondary=`Midpoint gradient ${((g1+g2)/2*100).toFixed(2)} %`;break;}
 case 'signal':{const g=Math.min(a,b-1);y=1800*g/b;unit='veh/h capacity';secondary=`v/c at 720 veh/h: ${(720/y).toFixed(2)}`;break;}
 case 'webster':y=(1.5*a+5)/(1-b);unit='s idealized cycle';secondary=y>180?'Result not operationally plausible; further design required':'Analytical estimate only, check all clearance constraints';break;
 case 'signalqueue':{let q=0,peak=0;for(let t=0;t<900;t++){let inGreen=(t%90)<b;let mu=inGreen?0.5:0;q=Math.max(0,q+a-mu);peak=Math.max(peak,q);}y=q;unit='vehicles queued after ten cycles';secondary=`Peak during 10 cycles: ${peak.toFixed(1)} vehicles`;break;}
 case 'axle':y=Math.pow(a/80,b);unit='relative damage index';secondary=`Compared with 80 kN reference axle`;break;
 case 'plate':{const h=a/1000,E=b*1e9; y=E*Math.pow(h,3)/(12*(1-0.2*0.2))/1e3;unit='kN·m plate rigidity';secondary='Linear elastic plate rigidity; no wheel-load analysis';break;}
 case 'runoff':y=0.00278*.85*a*b;unit='m³/s peak runoff';secondary=`Impervious-screening runoff coefficient 0.85`;break;
 case 'culvert':{const D=a,S=b/100,Area=Math.PI*D*D/4,R=D/4;y=Area*Math.pow(R,2/3)*Math.sqrt(S)/.013;unit='m³/s full-flow benchmark';secondary='Does not include entrance or tailwater control';break;}
 case 'transit':y=60/a*b;unit='passengers/hour/direction';secondary=`${(60/a).toFixed(1)} buses/h`;break;
 case 'pedestrian':y=a/b;unit='s moving time';secondary='Start-up/clearance and adopted legal rules excluded';break;
 case 'bayes':{let alpha=2*b,beta=2;y=(alpha+a)/(beta+1);unit='crashes/year posterior mean';secondary=`Prior ${b.toFixed(2)}/year; observed ${a.toFixed(0)} in one year`;break;}
 default:throw Error('Unknown model');
 }
 if(!Number.isFinite(y))throw Error('Nonfinite model output');
 return {y,unit,secondary,note};
  }

  var TE_LABS = [
  {
    "id": 1,
    "title": "Speed\u2013Flow\u2013Density Explorer",
    "unit": 1,
    "key": "greenshields",
    "params": [
      {
        "name": "Free-flow speed",
        "unit": "km/h",
        "min": 50,
        "max": 120,
        "step": 5,
        "default": 85
      },
      {
        "name": "Jam density",
        "unit": "veh/km/lane",
        "min": 70,
        "max": 220,
        "step": 5,
        "default": 140
      }
    ],
    "equation": "v = vf (1 \u2212 k/kj), q = kv",
    "assumption": "The parabolic flow\u2013density relation is an idealization. The resulting capacity often exceeds field observations.",
    "question": "How does the location of the calculated peak change as you change jam density?"
  },
  {
    "id": 2,
    "title": "Demand and Bottleneck Queue",
    "unit": 2,
    "key": "bottleneck",
    "params": [
      {
        "name": "Arrival demand",
        "unit": "veh/h",
        "min": 300,
        "max": 2600,
        "step": 50,
        "default": 1700
      },
      {
        "name": "Discharge capacity",
        "unit": "veh/h",
        "min": 500,
        "max": 2400,
        "step": 50,
        "default": 1450
      }
    ],
    "equation": "Q(t) = max[0,(arrival \u2212 service)t] for constant rates",
    "assumption": "Assumes a deterministic continuous queue and no storage limit or upstream metering.",
    "question": "Identify the threshold where queue accumulation changes sign."
  },
  {
    "id": 3,
    "title": "Peak-Hour Factor",
    "unit": 2,
    "key": "phf",
    "params": [
      {
        "name": "Peak 15-minute count",
        "unit": "veh/15min",
        "min": 60,
        "max": 600,
        "step": 10,
        "default": 310
      },
      {
        "name": "Other 45-minute total",
        "unit": "veh",
        "min": 180,
        "max": 1500,
        "step": 20,
        "default": 690
      }
    ],
    "equation": "PHF = (peak 15min + other 45min)/(4 \u00d7 peak 15min)",
    "assumption": "User inputs must represent a possible set of counts; this model does not validate the count composition.",
    "question": "When does the PHF exceed unity, and what does that tell you about inconsistent inputs?"
  },
  {
    "id": 4,
    "title": "Stopping Sight Distance",
    "unit": 3,
    "key": "ssd",
    "params": [
      {
        "name": "Travel speed",
        "unit": "km/h",
        "min": 30,
        "max": 120,
        "step": 5,
        "default": 80
      },
      {
        "name": "Tire-road friction",
        "unit": "fraction",
        "min": 0.15,
        "max": 0.65,
        "step": 0.01,
        "default": 0.35
      }
    ],
    "equation": "SSD = vt + v\u00b2/(2gf), t = 2.5s, level road",
    "assumption": "Uses fixed reaction time, friction and grade zero for a conceptual comparison.",
    "question": "Which speed increment changes SSD more: 40\u219260 or 80\u2192100 km/h?"
  },
  {
    "id": 5,
    "title": "Horizontal Curve Radius",
    "unit": 3,
    "key": "curve",
    "params": [
      {
        "name": "Design speed",
        "unit": "km/h",
        "min": 30,
        "max": 120,
        "step": 5,
        "default": 80
      },
      {
        "name": "Superelevation",
        "unit": "fraction",
        "min": 0,
        "max": 0.12,
        "step": 0.005,
        "default": 0.06
      }
    ],
    "equation": "R = V\u00b2/[127(e + f)] with f = 0.10",
    "assumption": "Illustrative lateral equilibrium only; side-friction design values are not universal.",
    "question": "What curve radius is implied if superelevation is reduced at unchanged speed?"
  },
  {
    "id": 6,
    "title": "Vertical Road Profile",
    "unit": 3,
    "key": "profile",
    "params": [
      {
        "name": "Curve length",
        "unit": "m",
        "min": 80,
        "max": 500,
        "step": 20,
        "default": 200
      },
      {
        "name": "End grade",
        "unit": "%",
        "min": -8,
        "max": 2,
        "step": 0.5,
        "default": -2
      }
    ],
    "equation": "y(x) = y0 + g1 x + (g2\u2212g1)x\u00b2/(2L), g1=+3%",
    "assumption": "Geometric parabolic curve only, with no sight-distance certification.",
    "question": "Where is the highest elevation, and how does it move when the end grade changes?"
  },
  {
    "id": 7,
    "title": "Signal Capacity and V/C",
    "unit": 4,
    "key": "signal",
    "params": [
      {
        "name": "Effective green",
        "unit": "s",
        "min": 10,
        "max": 70,
        "step": 2,
        "default": 32
      },
      {
        "name": "Cycle length",
        "unit": "s",
        "min": 60,
        "max": 180,
        "step": 5,
        "default": 90
      }
    ],
    "equation": "Capacity = 1800 \u00d7 green/cycle (veh/h)",
    "assumption": "Assumes 1800 veh/h saturation flow and demand 720 veh/h for one lane group.",
    "question": "For what green split is degree of saturation below one?"
  },
  {
    "id": 8,
    "title": "Webster Signal Cycle",
    "unit": 4,
    "key": "webster",
    "params": [
      {
        "name": "Cycle lost time",
        "unit": "s",
        "min": 4,
        "max": 20,
        "step": 1,
        "default": 12
      },
      {
        "name": "Critical flow ratio sum",
        "unit": "fraction",
        "min": 0.3,
        "max": 0.94,
        "step": 0.02,
        "default": 0.76
      }
    ],
    "equation": "C0 = (1.5L+5)/(1\u2212Y)",
    "assumption": "Near Y=1, sensitivity is extreme and the mathematical optimum is not operational guidance.",
    "question": "Why does a modest increase in Y create very large cycle estimates?"
  },
  {
    "id": 9,
    "title": "Traffic Signal Queue Evolution",
    "unit": 4,
    "key": "signalqueue",
    "params": [
      {
        "name": "Arrival rate",
        "unit": "veh/s",
        "min": 0.06,
        "max": 0.5,
        "step": 0.01,
        "default": 0.2
      },
      {
        "name": "Effective green",
        "unit": "s",
        "min": 10,
        "max": 70,
        "step": 2,
        "default": 40
      }
    ],
    "equation": "Q(t+\u0394t) = max[0,Q(t) + arrivals \u2212 departures]",
    "assumption": "Cycle 90s; saturation discharge 0.50 veh/s; deterministic simulation for 10 cycles.",
    "question": "When will queues build from cycle to cycle rather than fully clear?"
  },
  {
    "id": 10,
    "title": "Axle Load Damage Sensitivity",
    "unit": 5,
    "key": "axle",
    "params": [
      {
        "name": "Axle load",
        "unit": "kN",
        "min": 40,
        "max": 180,
        "step": 5,
        "default": 120
      },
      {
        "name": "Damage exponent",
        "unit": "dimensionless",
        "min": 2.5,
        "max": 5.5,
        "step": 0.25,
        "default": 4
      }
    ],
    "equation": "Relative damage = (P/80)^n",
    "assumption": "This is a simplified sensitivity index, not a certified equivalent single-axle load calculation.",
    "question": "How much does changing exponent affect apparent damage from heavy vehicles?"
  },
  {
    "id": 11,
    "title": "Pavement Plate Rigidity",
    "unit": 5,
    "key": "plate",
    "params": [
      {
        "name": "Concrete thickness",
        "unit": "mm",
        "min": 120,
        "max": 350,
        "step": 10,
        "default": 230
      },
      {
        "name": "Elastic modulus",
        "unit": "GPa",
        "min": 20,
        "max": 45,
        "step": 1,
        "default": 30
      }
    ],
    "equation": "D = Eh\u00b3/[12(1\u2212\u03bd\u00b2)] with \u03bd=0.20",
    "assumption": "Ideal elastic plate rigidity per unit width, not wheel-load stress or required design thickness.",
    "question": "Why does 10% greater thickness affect stiffness more than 10% greater modulus?"
  },
  {
    "id": 12,
    "title": "Rational Roadway Runoff",
    "unit": 6,
    "key": "runoff",
    "params": [
      {
        "name": "Rainfall intensity",
        "unit": "mm/h",
        "min": 20,
        "max": 160,
        "step": 5,
        "default": 70
      },
      {
        "name": "Runoff area",
        "unit": "ha",
        "min": 0.2,
        "max": 8,
        "step": 0.2,
        "default": 2
      }
    ],
    "equation": "Q = 0.00278 C i A, C=0.85",
    "assumption": "Rational method peak rate only; time of concentration and local IDF must be checked.",
    "question": "How much peak flow results from doubling area at fixed intensity?"
  },
  {
    "id": 13,
    "title": "Culvert Full-Flow Manning",
    "unit": 6,
    "key": "culvert",
    "params": [
      {
        "name": "Pipe diameter",
        "unit": "m",
        "min": 0.5,
        "max": 2.5,
        "step": 0.1,
        "default": 1.0
      },
      {
        "name": "Longitudinal slope",
        "unit": "%",
        "min": 0.1,
        "max": 3,
        "step": 0.1,
        "default": 0.6
      }
    ],
    "equation": "Q=(1/n) A R^(2/3) S^0.5, n=0.013, R=D/4",
    "assumption": "Assumes full circular flow and uniform conditions; inlet and tailwater control omitted.",
    "question": "How does diameter sensitivity differ from slope sensitivity?"
  },
  {
    "id": 14,
    "title": "Transit Fleet Capacity",
    "unit": 7,
    "key": "transit",
    "params": [
      {
        "name": "Bus headway",
        "unit": "min",
        "min": 3,
        "max": 30,
        "step": 1,
        "default": 8
      },
      {
        "name": "Usable capacity",
        "unit": "people/bus",
        "min": 25,
        "max": 120,
        "step": 5,
        "default": 60
      }
    ],
    "equation": "Passenger capacity = 60/headway \u00d7 people/bus",
    "assumption": "Assumes regular dispatch and fully usable stated capacity; not a demand forecast.",
    "question": "How would unreliable headway adherence affect practical service?"
  },
  {
    "id": 15,
    "title": "Pedestrian Clearance Screening",
    "unit": 7,
    "key": "pedestrian",
    "params": [
      {
        "name": "Crossing width",
        "unit": "m",
        "min": 6,
        "max": 36,
        "step": 1,
        "default": 18
      },
      {
        "name": "Walking speed",
        "unit": "m/s",
        "min": 0.6,
        "max": 1.6,
        "step": 0.05,
        "default": 1.0
      }
    ],
    "equation": "Motion time = distance/speed",
    "assumption": "Excludes startup, legal clearance rules, refuge stages and accessibility design factors.",
    "question": "What is the consequence of selecting a walking speed that excludes some users?"
  },
  {
    "id": 16,
    "title": "Crash-Count Bayesian Update",
    "unit": 8,
    "key": "bayes",
    "params": [
      {
        "name": "Observed annual crashes",
        "unit": "crashes",
        "min": 0,
        "max": 18,
        "step": 1,
        "default": 3
      },
      {
        "name": "Comparable-site prior mean",
        "unit": "crashes/year",
        "min": 0.5,
        "max": 10,
        "step": 0.5,
        "default": 2
      }
    ],
    "equation": "Posterior mean=(\u03b1+N)/(\u03b2+1), \u03b1=2\u00d7prior mean, \u03b2=2",
    "assumption": "Toy gamma\u2013Poisson example; does not account for exposure, site types or severity.",
    "question": "How does posterior estimate move between the prior mean and observed count?"
  }
];

  var MODELS = TE_LABS.map(function(lab) {
    var controlsHtml = lab.params.map(function(p, pi) {
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="te_' + lab.id + '_' + pi + '">' + p.name + ' <span class="unit" style="color:#64748b;">(' + p.unit + ')</span>: <span id="v_te_' + lab.id + '_' + pi + '" style="font-weight:700;color:#d97706;">' + p.default + '</span></label>' +
             '<input id="te_' + lab.id + '_' + pi + '" data-pidx="' + pi + '" type="range" min="' + p.min + '" max="' + p.max + '" step="' + p.step + '" value="' + p.default + '" style="width:100%;accent-color:#d97706;"></div>';
    }).join('');

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

    return {
      idx: lab.id,
      unit: lab.unit,
      html: html,
      init: function(card) {
        try {
          var pVals = lab.params.map(function(p) { return p.default; });
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
            node('polyline', { points: pathPts, fill: 'none', stroke: '#d97706', 'stroke-width': '2.5' });

            if (Number.isFinite(currY)) {
              node('circle', { cx: xp(currX), cy: yp(currY), r: 6, fill: '#ea580c', stroke: '#ffffff', 'stroke-width': '2' });
            }
            node('text', { x: (L + W - R) / 2, y: H - 12, 'text-anchor': 'middle', fill: '#334155', 'font-size': '12', 'font-weight': '600' }, lab.params[0].name);
          }

          function render() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var pi = parseInt(inp.dataset.pidx, 10);
              pVals[pi] = Number(inp.value);
              var lbl = card.querySelector('#v_te_' + lab.id + '_' + pi);
              if (lbl) lbl.textContent = inp.value;
            });

            var res = transportationCalc(lab.key, pVals[0], pVals[1] !== undefined ? pVals[1] : 1);
            if (valEl) {
              valEl.textContent = Number.isFinite(res.y) ? Number(res.y.toPrecision(4)) + ' ' + (res.unit || '') : '--';
            }
            if (interpEl) interpEl.textContent = res.secondary || '';

            var pts = [];
            var p0 = lab.params[0];
            for (var k = 0; k <= 50; k++) {
              var aX = p0.min + (p0.max - p0.min) * k / 50;
              var ptRes = transportationCalc(lab.key, aX, pVals[1] !== undefined ? pVals[1] : 1);
              if (Number.isFinite(ptRes.y)) pts.push([aX, ptRes.y]);
            }
            drawGraph(pts, pVals[0], res.y);
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', render);
          });
          render();
        } catch(err) {
          console.error('TE sim error on lab ' + lab.id, err);
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
