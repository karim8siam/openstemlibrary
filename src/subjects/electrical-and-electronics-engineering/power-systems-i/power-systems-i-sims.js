/* power-systems-i Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<h3>Three-phase power balance</h3><p>Line-to-line voltage, line current and power factor determine balanced apparent, real and reactive powers.</p><section id=\"controls\"></section><h2>Real power MW</h2><output id=\"result\"></output><p id=\"note\"></p><p class=\"note\"><b>Assumptions:</b> Balanced sinusoidal steady state, lagging current. The numerical models here are for education. They do not authorize contact with energized apparatus, grid switching, protective-relay setting changes or construction. Those activities require licensed professionals, utility procedures and current equipment documentation.</p>",
    init: function(card) {
      try {
"use strict";const cfg=[{"label": "V_LL (V)", "min": 1000, "max": 33000, "value": 11000}, {"label": "I_line (A)", "min": 10, "max": 600, "value": 100}, {"label": "power factor", "min": 0.1, "max": 1, "value": 0.9}];const host=card.querySelector("#" + 'controls'.replace(/^#/, ""));const sliders=[];cfg.forEach((f,i)=>{const label=document.createElement('label');const title=document.createElement('span');title.textContent=f.label+' — ';const val=document.createElement('strong');val.id='value'+i;const input=document.createElement('input');input.type='range';input.min=f.min;input.max=f.max;input.step=(f.max-f.min)/500;input.value=f.value;input.setAttribute('aria-label',f.label);label.append(title,val,input);host.appendChild(label);sliders.push(input);input.addEventListener('input',update);});function update(){const [a,b,c]=sliders.map(x=>Number(x.value));sliders.forEach((x,i)=>document.getElementById('value'+i).textContent=Number(x.value).toFixed(3));let v=NaN;let note='';const S=Math.sqrt(3)*a*b/1e6;let P=S*c;let Q=S*Math.sqrt(Math.max(0,1-c*c));v=P;note=`P=${P.toFixed(3)} MW, Q=${Q.toFixed(3)} MVAr, S=${S.toFixed(3)} MVA (lagging assumed)`;card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?v.toFixed(4):'Undefined model output';card.querySelector("#" + 'note'.replace(/^#/, "")).textContent=note;}update();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: "<h3>Per-unit impedance base</h3><p>A chosen three-phase MVA base and line-to-line kV base give the impedance base in ohms.</p><section id=\"controls\"></section><h2>Reactance (pu)</h2><output id=\"result\"></output><p id=\"note\"></p><p class=\"note\"><b>Assumptions:</b> Uses Zbase = kV_LL squared / MVA_3ph; only magnitude shown. The numerical models here are for education. They do not authorize contact with energized apparatus, grid switching, protective-relay setting changes or construction. Those activities require licensed professionals, utility procedures and current equipment documentation.</p>",
    init: function(card) {
      try {
"use strict";const cfg=[{"label": "V_base line-line (kV)", "min": 1, "max": 230, "value": 132}, {"label": "S_base 3-phase (MVA)", "min": 5, "max": 500, "value": 100}, {"label": "physical reactance (ohm)", "min": 0.1, "max": 100, "value": 17.424}];const host=card.querySelector("#" + 'controls'.replace(/^#/, ""));const sliders=[];cfg.forEach((f,i)=>{const label=document.createElement('label');const title=document.createElement('span');title.textContent=f.label+' — ';const val=document.createElement('strong');val.id='value'+i;const input=document.createElement('input');input.type='range';input.min=f.min;input.max=f.max;input.step=(f.max-f.min)/500;input.value=f.value;input.setAttribute('aria-label',f.label);label.append(title,val,input);host.appendChild(label);sliders.push(input);input.addEventListener('input',update);});function update(){const [a,b,c]=sliders.map(x=>Number(x.value));sliders.forEach((x,i)=>document.getElementById('value'+i).textContent=Number(x.value).toFixed(3));let v=NaN;let note='';let z=a*a/b;v=c/z;note=`Zbase=${z.toFixed(4)} ohm, Zpu=${v.toFixed(5)}; choose bases consistently on each transformer side`;card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?v.toFixed(4):'Undefined model output';card.querySelector("#" + 'note'.replace(/^#/, "")).textContent=note;}update();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: "<h3>Line voltage-drop approximation</h3><p>Sensitivity of an approximate phase voltage drop to resistance, reactance and power factor.</p><section id=\"controls\"></section><h2>Approx phase drop (V)</h2><output id=\"result\"></output><p id=\"note\"></p><p class=\"note\"><b>Assumptions:</b> Small-drop approximation, fixed lagging 0.8 power factor. The numerical models here are for education. They do not authorize contact with energized apparatus, grid switching, protective-relay setting changes or construction. Those activities require licensed professionals, utility procedures and current equipment documentation.</p>",
    init: function(card) {
      try {
"use strict";const cfg=[{"label": "I (A)", "min": 0, "max": 500, "value": 100}, {"label": "R per phase (ohm)", "min": 0, "max": 10, "value": 2}, {"label": "X per phase (ohm)", "min": 0, "max": 15, "value": 4}];const host=card.querySelector("#" + 'controls'.replace(/^#/, ""));const sliders=[];cfg.forEach((f,i)=>{const label=document.createElement('label');const title=document.createElement('span');title.textContent=f.label+' — ';const val=document.createElement('strong');val.id='value'+i;const input=document.createElement('input');input.type='range';input.min=f.min;input.max=f.max;input.step=(f.max-f.min)/500;input.value=f.value;input.setAttribute('aria-label',f.label);label.append(title,val,input);host.appendChild(label);sliders.push(input);input.addEventListener('input',update);});function update(){const [a,b,c]=sliders.map(x=>Number(x.value));sliders.forEach((x,i)=>document.getElementById('value'+i).textContent=Number(x.value).toFixed(3));let v=NaN;let note='';let pf=0.8;v=a*(b*pf+c*Math.sqrt(1-pf*pf));note=`Approx ${v.toFixed(2)} V/phase at assumed lagging pf=0.8`;card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?v.toFixed(4):'Undefined model output';card.querySelector("#" + 'note'.replace(/^#/, "")).textContent=note;}update();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: "<h3>Two-bus lossless power transfer</h3><p>Simplified active-power transfer across a reactance versus phase-angle difference.</p><section id=\"controls\"></section><h2>Transfer power (pu)</h2><output id=\"result\"></output><p id=\"note\"></p><p class=\"note\"><b>Assumptions:</b> Lossless two-bus model with constant voltages and reactance. The numerical models here are for education. They do not authorize contact with energized apparatus, grid switching, protective-relay setting changes or construction. Those activities require licensed professionals, utility procedures and current equipment documentation.</p>",
    init: function(card) {
      try {
"use strict";const cfg=[{"label": "V_s (pu)", "min": 0.8, "max": 1.2, "value": 1}, {"label": "V_r (pu)", "min": 0.8, "max": 1.2, "value": 1}, {"label": "delta (degrees)", "min": 0, "max": 90, "value": 10}];const host=card.querySelector("#" + 'controls'.replace(/^#/, ""));const sliders=[];cfg.forEach((f,i)=>{const label=document.createElement('label');const title=document.createElement('span');title.textContent=f.label+' — ';const val=document.createElement('strong');val.id='value'+i;const input=document.createElement('input');input.type='range';input.min=f.min;input.max=f.max;input.step=(f.max-f.min)/500;input.value=f.value;input.setAttribute('aria-label',f.label);label.append(title,val,input);host.appendChild(label);sliders.push(input);input.addEventListener('input',update);});function update(){const [a,b,c]=sliders.map(x=>Number(x.value));sliders.forEach((x,i)=>document.getElementById('value'+i).textContent=Number(x.value).toFixed(3));let v=NaN;let note='';let X=0.2;v=a*b/X*Math.sin(c*Math.PI/180);note=`P=${v.toFixed(4)} pu on chosen system base at X=0.2 pu`;card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?v.toFixed(4):'Undefined model output';card.querySelector("#" + 'note'.replace(/^#/, "")).textContent=note;}update();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: "<h3>Three-phase symmetrical fault</h3><p>Initial symmetrical rms 3-phase current for line voltage and positive-sequence Thevenin reactance.</p><section id=\"controls\"></section><h2>Fault current (kA)</h2><output id=\"result\"></output><p id=\"note\"></p><p class=\"note\"><b>Assumptions:</b> Positive-sequence purely reactive Thevenin model; not a protection setting. The numerical models here are for education. They do not authorize contact with energized apparatus, grid switching, protective-relay setting changes or construction. Those activities require licensed professionals, utility procedures and current equipment documentation.</p>",
    init: function(card) {
      try {
"use strict";const cfg=[{"label": "Line-line kV", "min": 0.4, "max": 33, "value": 11}, {"label": "X1 (ohm)", "min": 0.1, "max": 15, "value": 2}, {"label": "prefault voltage factor", "min": 0.9, "max": 1.1, "value": 1}];const host=card.querySelector("#" + 'controls'.replace(/^#/, ""));const sliders=[];cfg.forEach((f,i)=>{const label=document.createElement('label');const title=document.createElement('span');title.textContent=f.label+' — ';const val=document.createElement('strong');val.id='value'+i;const input=document.createElement('input');input.type='range';input.min=f.min;input.max=f.max;input.step=(f.max-f.min)/500;input.value=f.value;input.setAttribute('aria-label',f.label);label.append(title,val,input);host.appendChild(label);sliders.push(input);input.addEventListener('input',update);});function update(){const [a,b,c]=sliders.map(x=>Number(x.value));sliders.forEach((x,i)=>document.getElementById('value'+i).textContent=Number(x.value).toFixed(3));let v=NaN;let note='';v=(a*1000/Math.sqrt(3))*c/b/1000;note=`I3ph=${v.toFixed(3)} kA symmetrical rms; excludes DC offset and breaker duty`;card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?v.toFixed(4):'Undefined model output';card.querySelector("#" + 'note'.replace(/^#/, "")).textContent=note;}update();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: "<h3>Economic dispatch with two units</h3><p>Simple unconstrained equal-incremental-cost dispatch for two convex cost curves.</p><section id=\"controls\"></section><h2>Unit 1 dispatch MW</h2><output id=\"result\"></output><p id=\"note\"></p><p class=\"note\"><b>Assumptions:</b> Marginal costs: MC1=b+0.2 P1 and MC2=c+0.1 P2; no limits/losses. The numerical models here are for education. They do not authorize contact with energized apparatus, grid switching, protective-relay setting changes or construction. Those activities require licensed professionals, utility procedures and current equipment documentation.</p>",
    init: function(card) {
      try {
"use strict";const cfg=[{"label": "Demand (MW)", "min": 30, "max": 220, "value": 100}, {"label": "MC1 intercept", "min": 5, "max": 25, "value": 10}, {"label": "MC2 intercept", "min": 5, "max": 25, "value": 14}];const host=card.querySelector("#" + 'controls'.replace(/^#/, ""));const sliders=[];cfg.forEach((f,i)=>{const label=document.createElement('label');const title=document.createElement('span');title.textContent=f.label+' — ';const val=document.createElement('strong');val.id='value'+i;const input=document.createElement('input');input.type='range';input.min=f.min;input.max=f.max;input.step=(f.max-f.min)/500;input.value=f.value;input.setAttribute('aria-label',f.label);label.append(title,val,input);host.appendChild(label);sliders.push(input);input.addEventListener('input',update);});function update(){const [a,b,c]=sliders.map(x=>Number(x.value));sliders.forEach((x,i)=>document.getElementById('value'+i).textContent=Number(x.value).toFixed(3));let v=NaN;let note='';let slope1=.2,slope2=.1;let P1=(c-b+slope2*a)/(slope1+slope2);let P2=a-P1;v=P1;note=`P1=${P1.toFixed(2)} MW and P2=${P2.toFixed(2)} MW; not a feasible constrained dispatch if any output is negative`;card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?v.toFixed(4):'Undefined model output';card.querySelector("#" + 'note'.replace(/^#/, "")).textContent=note;}update();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: "<h3>ZIP load and local voltage</h3><p>Voltage sensitivity of a ZIP demand model using fixed nonnegative weights that sum to one.</p><section id=\"controls\"></section><h2>Normalized demand (pu)</h2><output id=\"result\"></output><p id=\"note\"></p><p class=\"note\"><b>Assumptions:</b> Static ZIP approximation; I weight is capped so components sum to one. The numerical models here are for education. They do not authorize contact with energized apparatus, grid switching, protective-relay setting changes or construction. Those activities require licensed professionals, utility procedures and current equipment documentation.</p>",
    init: function(card) {
      try {
"use strict";const cfg=[{"label": "V/Vnom (pu)", "min": 0.85, "max": 1.1, "value": 0.95}, {"label": "constant-Z weight", "min": 0, "max": 1, "value": 0.3}, {"label": "constant-I weight", "min": 0, "max": 1, "value": 0.2}];const host=card.querySelector("#" + 'controls'.replace(/^#/, ""));const sliders=[];cfg.forEach((f,i)=>{const label=document.createElement('label');const title=document.createElement('span');title.textContent=f.label+' — ';const val=document.createElement('strong');val.id='value'+i;const input=document.createElement('input');input.type='range';input.min=f.min;input.max=f.max;input.step=(f.max-f.min)/500;input.value=f.value;input.setAttribute('aria-label',f.label);label.append(title,val,input);host.appendChild(label);sliders.push(input);input.addEventListener('input',update);});function update(){const [a,b,c]=sliders.map(x=>Number(x.value));sliders.forEach((x,i)=>document.getElementById('value'+i).textContent=Number(x.value).toFixed(3));let v=NaN;let note='';let wI=Math.min(c,1-b),wP=1-b-wI;v=b*a*a+wI*a+wP;note=`P/Pnom=${v.toFixed(4)} (Z weight ${b.toFixed(2)}, I weight ${wI.toFixed(2)}, P weight ${wP.toFixed(2)})`;card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?v.toFixed(4):'Undefined model output';card.querySelector("#" + 'note'.replace(/^#/, "")).textContent=note;}update();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: "<h3>Harmonic distortion</h3><p>Compute total harmonic distortion from rms fundamental and two selected harmonic magnitudes.</p><section id=\"controls\"></section><h2>Current THD (%)</h2><output id=\"result\"></output><p id=\"note\"></p><p class=\"note\"><b>Assumptions:</b> RMS harmonic magnitudes; higher orders and voltage distortion omitted. The numerical models here are for education. They do not authorize contact with energized apparatus, grid switching, protective-relay setting changes or construction. Those activities require licensed professionals, utility procedures and current equipment documentation.</p>",
    init: function(card) {
      try {
"use strict";const cfg=[{"label": "fundamental current I1 (A)", "min": 1, "max": 500, "value": 100}, {"label": "I5 harmonic (A)", "min": 0, "max": 100, "value": 10}, {"label": "I7 harmonic (A)", "min": 0, "max": 100, "value": 5}];const host=card.querySelector("#" + 'controls'.replace(/^#/, ""));const sliders=[];cfg.forEach((f,i)=>{const label=document.createElement('label');const title=document.createElement('span');title.textContent=f.label+' — ';const val=document.createElement('strong');val.id='value'+i;const input=document.createElement('input');input.type='range';input.min=f.min;input.max=f.max;input.step=(f.max-f.min)/500;input.value=f.value;input.setAttribute('aria-label',f.label);label.append(title,val,input);host.appendChild(label);sliders.push(input);input.addEventListener('input',update);});function update(){const [a,b,c]=sliders.map(x=>Number(x.value));sliders.forEach((x,i)=>document.getElementById('value'+i).textContent=Number(x.value).toFixed(3));let v=NaN;let note='';v=100*Math.sqrt(b*b+c*c)/a;note=`Current THD=${v.toFixed(2)}%; only 5th and 7th harmonics included`;card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?v.toFixed(4):'Undefined model output';card.querySelector("#" + 'note'.replace(/^#/, "")).textContent=note;}update();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
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
