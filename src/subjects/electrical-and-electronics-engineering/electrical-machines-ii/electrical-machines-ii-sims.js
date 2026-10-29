/* electrical-machines-ii Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<a href=\"index.html\">\u2190 Simulations</a><h3>Three-phase power</h3><p>Interactive simplified classroom model. Change any slider; predicted output updates locally in your browser.</p><div id=\"inputs\"></div><p>Model estimate: <output id=\"out\"></output></p><p class=\"warn\">Assumptions: balanced ideal operating point or the explicitly labelled approximation. Not a device rating or operational instruction. Validate against a manufacturer data before design decisions.</p>",
    init: function(card) {
      try {
const fields=[["voltage (V)", 300, 500, 400], ["current (A)", 1, 35, 12], ["power factor", 0.2, 1, 0.85]];const box=card.querySelector("#" + 'inputs'.replace(/^#/, ""));let controls=[];fields.forEach(([label,min,max,value],i)=>{const wrap=document.createElement('label');const t=document.createElement('span');const n=document.createElement('input');n.type='range';n.min=min;n.max=max;n.step=(max-min)/200;n.value=value;const v=document.createElement('b');wrap.append(t,n,v);box.append(wrap);controls.push(n);n.addEventListener('input',()=>update());t.textContent=label+' ';v.id='v'+i;});function update(){const [a,b,c]=controls.map(x=>+x.value);controls.forEach((x,i)=>document.getElementById('v'+i).textContent=Number(x.value).toFixed(2));let p=0,unit='';p=Math.sqrt(3)*a*b*c; unit="W";card.querySelector("#" + 'out'.replace(/^#/, "")).textContent=p.toFixed(2)+' '+unit;}update();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: "<a href=\"index.html\">\u2190 Simulations</a><h3>Synchronous speed</h3><p>Interactive simplified classroom model. Change any slider; predicted output updates locally in your browser.</p><div id=\"inputs\"></div><p>Model estimate: <output id=\"out\"></output></p><p class=\"warn\">Assumptions: balanced ideal operating point or the explicitly labelled approximation. Not a device rating or operational instruction. Validate against a manufacturer data before design decisions.</p>",
    init: function(card) {
      try {
const fields=[["frequency (Hz)", 10, 80, 50], ["number of poles", 2, 12, 4], ["speed ratio", 0.5, 1.1, 0.96]];const box=card.querySelector("#" + 'inputs'.replace(/^#/, ""));let controls=[];fields.forEach(([label,min,max,value],i)=>{const wrap=document.createElement('label');const t=document.createElement('span');const n=document.createElement('input');n.type='range';n.min=min;n.max=max;n.step=(max-min)/200;n.value=value;const v=document.createElement('b');wrap.append(t,n,v);box.append(wrap);controls.push(n);n.addEventListener('input',()=>update());t.textContent=label+' ';v.id='v'+i;});function update(){const [a,b,c]=controls.map(x=>+x.value);controls.forEach((x,i)=>document.getElementById('v'+i).textContent=Number(x.value).toFixed(2));let p=0,unit='';p=120*a/b*c; unit="rpm";card.querySelector("#" + 'out'.replace(/^#/, "")).textContent=p.toFixed(2)+' '+unit;}update();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: "<a href=\"index.html\">\u2190 Simulations</a><h3>Rotor copper losses</h3><p>Interactive simplified classroom model. Change any slider; predicted output updates locally in your browser.</p><div id=\"inputs\"></div><p>Model estimate: <output id=\"out\"></output></p><p class=\"warn\">Assumptions: balanced ideal operating point or the explicitly labelled approximation. Not a device rating or operational instruction. Validate against a manufacturer data before design decisions.</p>",
    init: function(card) {
      try {
const fields=[["air-gap power (W)", 1000, 30000, 12000], ["slip", 0.01, 0.15, 0.04], ["loss multiplier", 0.8, 1.2, 1]];const box=card.querySelector("#" + 'inputs'.replace(/^#/, ""));let controls=[];fields.forEach(([label,min,max,value],i)=>{const wrap=document.createElement('label');const t=document.createElement('span');const n=document.createElement('input');n.type='range';n.min=min;n.max=max;n.step=(max-min)/200;n.value=value;const v=document.createElement('b');wrap.append(t,n,v);box.append(wrap);controls.push(n);n.addEventListener('input',()=>update());t.textContent=label+' ';v.id='v'+i;});function update(){const [a,b,c]=controls.map(x=>+x.value);controls.forEach((x,i)=>document.getElementById('v'+i).textContent=Number(x.value).toFixed(2));let p=0,unit='';p=a*b*c;unit="W";card.querySelector("#" + 'out'.replace(/^#/, "")).textContent=p.toFixed(2)+' '+unit;}update();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: "<a href=\"index.html\">\u2190 Simulations</a><h3>Synchronous power angle</h3><p>Interactive simplified classroom model. Change any slider; predicted output updates locally in your browser.</p><div id=\"inputs\"></div><p>Model estimate: <output id=\"out\"></output></p><p class=\"warn\">Assumptions: balanced ideal operating point or the explicitly labelled approximation. Not a device rating or operational instruction. Validate against a manufacturer data before design decisions.</p>",
    init: function(card) {
      try {
const fields=[["phase E (V)", 100, 400, 260], ["phase V (V)", 100, 400, 230], ["delta (degrees)", 0, 90, 30]];const box=card.querySelector("#" + 'inputs'.replace(/^#/, ""));let controls=[];fields.forEach(([label,min,max,value],i)=>{const wrap=document.createElement('label');const t=document.createElement('span');const n=document.createElement('input');n.type='range';n.min=min;n.max=max;n.step=(max-min)/200;n.value=value;const v=document.createElement('b');wrap.append(t,n,v);box.append(wrap);controls.push(n);n.addEventListener('input',()=>update());t.textContent=label+' ';v.id='v'+i;});function update(){const [a,b,c]=controls.map(x=>+x.value);controls.forEach((x,i)=>document.getElementById('v'+i).textContent=Number(x.value).toFixed(2));let p=0,unit='';p=3*a*b/5*Math.sin(c*Math.PI/180);unit="W (Xs=5 ohm)";card.querySelector("#" + 'out'.replace(/^#/, "")).textContent=p.toFixed(2)+' '+unit;}update();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: "<a href=\"index.html\">\u2190 Simulations</a><h3>Motor MVA capability</h3><p>Interactive simplified classroom model. Change any slider; predicted output updates locally in your browser.</p><div id=\"inputs\"></div><p>Model estimate: <output id=\"out\"></output></p><p class=\"warn\">Assumptions: balanced ideal operating point or the explicitly labelled approximation. Not a device rating or operational instruction. Validate against a manufacturer data before design decisions.</p>",
    init: function(card) {
      try {
const fields=[["real power (MW)", 0, 10, 8], ["reactive power (MVAr)", 0, 10, 6], ["limit (MVA)", 6, 15, 10]];const box=card.querySelector("#" + 'inputs'.replace(/^#/, ""));let controls=[];fields.forEach(([label,min,max,value],i)=>{const wrap=document.createElement('label');const t=document.createElement('span');const n=document.createElement('input');n.type='range';n.min=min;n.max=max;n.step=(max-min)/200;n.value=value;const v=document.createElement('b');wrap.append(t,n,v);box.append(wrap);controls.push(n);n.addEventListener('input',()=>update());t.textContent=label+' ';v.id='v'+i;});function update(){const [a,b,c]=controls.map(x=>+x.value);controls.forEach((x,i)=>document.getElementById('v'+i).textContent=Number(x.value).toFixed(2));let p=0,unit='';p=Math.sqrt(a*a+b*b);unit="MVA total; limit "+c+" MVA";card.querySelector("#" + 'out'.replace(/^#/, "")).textContent=p.toFixed(2)+' '+unit;}update();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: "<a href=\"index.html\">\u2190 Simulations</a><h3>PMSM torque</h3><p>Interactive simplified classroom model. Change any slider; predicted output updates locally in your browser.</p><div id=\"inputs\"></div><p>Model estimate: <output id=\"out\"></output></p><p class=\"warn\">Assumptions: balanced ideal operating point or the explicitly labelled approximation. Not a device rating or operational instruction. Validate against a manufacturer data before design decisions.</p>",
    init: function(card) {
      try {
const fields=[["pole pairs", 1, 8, 3], ["PM flux linkage (Wb)", 0.02, 0.3, 0.12], ["q-current (A)", 0, 20, 8]];const box=card.querySelector("#" + 'inputs'.replace(/^#/, ""));let controls=[];fields.forEach(([label,min,max,value],i)=>{const wrap=document.createElement('label');const t=document.createElement('span');const n=document.createElement('input');n.type='range';n.min=min;n.max=max;n.step=(max-min)/200;n.value=value;const v=document.createElement('b');wrap.append(t,n,v);box.append(wrap);controls.push(n);n.addEventListener('input',()=>update());t.textContent=label+' ';v.id='v'+i;});function update(){const [a,b,c]=controls.map(x=>+x.value);controls.forEach((x,i)=>document.getElementById('v'+i).textContent=Number(x.value).toFixed(2));let p=0,unit='';p=1.5*a*b*c;unit="N·m (id=0, surface PMSM)";card.querySelector("#" + 'out'.replace(/^#/, "")).textContent=p.toFixed(2)+' '+unit;}update();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: "<a href=\"index.html\">\u2190 Simulations</a><h3>Regenerative energy</h3><p>Interactive simplified classroom model. Change any slider; predicted output updates locally in your browser.</p><div id=\"inputs\"></div><p>Model estimate: <output id=\"out\"></output></p><p class=\"warn\">Assumptions: balanced ideal operating point or the explicitly labelled approximation. Not a device rating or operational instruction. Validate against a manufacturer data before design decisions.</p>",
    init: function(card) {
      try {
const fields=[["inertia (kg m\u00b2)", 0.1, 10, 2], ["initial speed (rad/s)", 30, 200, 100], ["final speed (rad/s)", 0, 100, 50]];const box=card.querySelector("#" + 'inputs'.replace(/^#/, ""));let controls=[];fields.forEach(([label,min,max,value],i)=>{const wrap=document.createElement('label');const t=document.createElement('span');const n=document.createElement('input');n.type='range';n.min=min;n.max=max;n.step=(max-min)/200;n.value=value;const v=document.createElement('b');wrap.append(t,n,v);box.append(wrap);controls.push(n);n.addEventListener('input',()=>update());t.textContent=label+' ';v.id='v'+i;});function update(){const [a,b,c]=controls.map(x=>+x.value);controls.forEach((x,i)=>document.getElementById('v'+i).textContent=Number(x.value).toFixed(2));let p=0,unit='';p=Math.max(0,0.5*a*(b*b-c*c));unit="J before losses";card.querySelector("#" + 'out'.replace(/^#/, "")).textContent=p.toFixed(2)+' '+unit;}update();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: "<a href=\"index.html\">\u2190 Simulations</a><h3>Pump affinity power</h3><p>Interactive simplified classroom model. Change any slider; predicted output updates locally in your browser.</p><div id=\"inputs\"></div><p>Model estimate: <output id=\"out\"></output></p><p class=\"warn\">Assumptions: balanced ideal operating point or the explicitly labelled approximation. Not a device rating or operational instruction. Validate against a manufacturer data before design decisions.</p>",
    init: function(card) {
      try {
const fields=[["baseline power (kW)", 1, 25, 10], ["speed fraction", 0.4, 1.2, 0.8], ["operating hours", 100, 5000, 3000]];const box=card.querySelector("#" + 'inputs'.replace(/^#/, ""));let controls=[];fields.forEach(([label,min,max,value],i)=>{const wrap=document.createElement('label');const t=document.createElement('span');const n=document.createElement('input');n.type='range';n.min=min;n.max=max;n.step=(max-min)/200;n.value=value;const v=document.createElement('b');wrap.append(t,n,v);box.append(wrap);controls.push(n);n.addEventListener('input',()=>update());t.textContent=label+' ';v.id='v'+i;});function update(){const [a,b,c]=controls.map(x=>+x.value);controls.forEach((x,i)=>document.getElementById('v'+i).textContent=Number(x.value).toFixed(2));let p=0,unit='';p=a*Math.pow(b,3);unit="kW (ideal affinity); annual energy "+(p*c).toFixed(0)+" kWh";card.querySelector("#" + 'out'.replace(/^#/, "")).textContent=p.toFixed(2)+' '+unit;}update();
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
