/* mechanical-systems-design-and-optimization Interactive Simulation Suite */
(function(window) {
  'use strict';

  var OPENSTEM_SIM_MODELS = [];

  OPENSTEM_SIM_MODELS.push({
    idx: 1,
    unit: 1,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 01 / 16</div><h3>Drive power and operating cost</h3><p>P = Fv/\u03b7</p></header><p class=\"notice\"><strong>Model scope:</strong> Steady load only. Starting torque, regeneration, duty factor and thermal limits require separate evaluation.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"force\">Linear force (N)</label><input id=\"force\" type=\"number\" value=\"1000\" min=\"10\" max=\"4000\" step=\"10\"><input id=\"r-force\" type=\"range\" value=\"1000\" min=\"10\" max=\"4000\" step=\"10\" aria-label=\"Change Linear force (N)\"></div><div class=\"inp\"><label for=\"speed\">Speed (m/s)</label><input id=\"speed\" type=\"number\" value=\"0.6\" min=\"0.05\" max=\"3\" step=\"0.05\"><input id=\"r-speed\" type=\"range\" value=\"0.6\" min=\"0.05\" max=\"3\" step=\"0.05\" aria-label=\"Change Speed (m/s)\"></div><div class=\"inp\"><label for=\"eff\">Drive efficiency</label><input id=\"eff\" type=\"number\" value=\"0.8\" min=\"0.2\" max=\"1\" step=\"0.01\"><input id=\"r-eff\" type=\"range\" value=\"0.8\" min=\"0.2\" max=\"1\" step=\"0.01\" aria-label=\"Change Drive efficiency\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "force", "min": 10, "max": 4000, "step": 10}, {"name": "speed", "min": 0.05, "max": 3, "step": 0.05}, {"name": "eff", "min": 0.2, "max": 1, "step": 0.01}];
function compute(p){return p.force*p.speed/p.eff/1000;}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' kW';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 2,
    unit: 1,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 02 / 16</div><h3>Requirement performance margin</h3><p>M = (allowable\u2212predicted)/allowable</p></header><p class=\"notice\"><strong>Model scope:</strong> Positive margin presumes lower is better and both quantities share the same definition and units.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"allow\">Allowable value</label><input id=\"allow\" type=\"number\" value=\"120\" min=\"1\" max=\"500\" step=\"1\"><input id=\"r-allow\" type=\"range\" value=\"120\" min=\"1\" max=\"500\" step=\"1\" aria-label=\"Change Allowable value\"></div><div class=\"inp\"><label for=\"actual\">Predicted value</label><input id=\"actual\" type=\"number\" value=\"90\" min=\"0\" max=\"500\" step=\"1\"><input id=\"r-actual\" type=\"range\" value=\"90\" min=\"0\" max=\"500\" step=\"1\" aria-label=\"Change Predicted value\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "allow", "min": 1, "max": 500, "step": 1}, {"name": "actual", "min": 0, "max": 500, "step": 1}];
function compute(p){return (p.allow-p.actual)/p.allow*100;}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' %';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 3,
    unit: 2,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 03 / 16</div><h3>Flow Reynolds number</h3><p>Re = \u03c1VD/\u03bc</p></header><p class=\"notice\"><strong>Model scope:</strong> Reynolds number is a regime indicator, not an exact onset-of-turbulence guarantee.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"rho\">Density (kg/m\u00b3)</label><input id=\"rho\" type=\"number\" value=\"1000\" min=\"100\" max=\"2000\" step=\"10\"><input id=\"r-rho\" type=\"range\" value=\"1000\" min=\"100\" max=\"2000\" step=\"10\" aria-label=\"Change Density (kg/m\u00b3)\"></div><div class=\"inp\"><label for=\"vel\">Mean speed (m/s)</label><input id=\"vel\" type=\"number\" value=\"1\" min=\"0.01\" max=\"10\" step=\"0.01\"><input id=\"r-vel\" type=\"range\" value=\"1\" min=\"0.01\" max=\"10\" step=\"0.01\" aria-label=\"Change Mean speed (m/s)\"></div><div class=\"inp\"><label for=\"dia\">Hydraulic diameter (m)</label><input id=\"dia\" type=\"number\" value=\"0.025\" min=\"0.001\" max=\"0.2\" step=\"0.001\"><input id=\"r-dia\" type=\"range\" value=\"0.025\" min=\"0.001\" max=\"0.2\" step=\"0.001\" aria-label=\"Change Hydraulic diameter (m)\"></div><div class=\"inp\"><label for=\"mu\">Dynamic viscosity (Pa\u00b7s)</label><input id=\"mu\" type=\"number\" value=\"0.001\" min=\"0.0001\" max=\"0.05\" step=\"0.0001\"><input id=\"r-mu\" type=\"range\" value=\"0.001\" min=\"0.0001\" max=\"0.05\" step=\"0.0001\" aria-label=\"Change Dynamic viscosity (Pa\u00b7s)\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "rho", "min": 100, "max": 2000, "step": 10}, {"name": "vel", "min": 0.01, "max": 10, "step": 0.01}, {"name": "dia", "min": 0.001, "max": 0.2, "step": 0.001}, {"name": "mu", "min": 0.0001, "max": 0.05, "step": 0.0001}];
function compute(p){return p.rho*p.vel*p.dia/p.mu;}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' dimensionless';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 4,
    unit: 2,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 04 / 16</div><h3>Thermal capacitance and heat storage</h3><p>E = mc\u209a\u0394T</p></header><p class=\"notice\"><strong>Model scope:</strong> Constant heat capacity, no phase change, heat losses or temperature gradients.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"mass\">Mass (kg)</label><input id=\"mass\" type=\"number\" value=\"10\" min=\"1\" max=\"500\" step=\"1\"><input id=\"r-mass\" type=\"range\" value=\"10\" min=\"1\" max=\"500\" step=\"1\" aria-label=\"Change Mass (kg)\"></div><div class=\"inp\"><label for=\"cp\">Heat capacity (J/kg K)</label><input id=\"cp\" type=\"number\" value=\"900\" min=\"100\" max=\"5000\" step=\"10\"><input id=\"r-cp\" type=\"range\" value=\"900\" min=\"100\" max=\"5000\" step=\"10\" aria-label=\"Change Heat capacity (J/kg K)\"></div><div class=\"inp\"><label for=\"rise\">Temperature change (K)</label><input id=\"rise\" type=\"number\" value=\"30\" min=\"0\" max=\"150\" step=\"1\"><input id=\"r-rise\" type=\"range\" value=\"30\" min=\"0\" max=\"150\" step=\"1\" aria-label=\"Change Temperature change (K)\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "mass", "min": 1, "max": 500, "step": 1}, {"name": "cp", "min": 100, "max": 5000, "step": 10}, {"name": "rise", "min": 0, "max": 150, "step": 1}];
function compute(p){return p.mass*p.cp*p.rise/3600000;}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' kWh';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 5,
    unit: 3,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 05 / 16</div><h3>Pump shaft power</h3><p>Pshaft = \u03c1gQH/\u03b7</p></header><p class=\"notice\"><strong>Model scope:</strong> Hydraulic-to-shaft conversion only. Suction conditions, motor efficiency, and pump curve are not modeled.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"rho\">Density (kg/m\u00b3)</label><input id=\"rho\" type=\"number\" value=\"1000\" min=\"300\" max=\"1500\" step=\"10\"><input id=\"r-rho\" type=\"range\" value=\"1000\" min=\"300\" max=\"1500\" step=\"10\" aria-label=\"Change Density (kg/m\u00b3)\"></div><div class=\"inp\"><label for=\"flow\">Flow (m\u00b3/s)</label><input id=\"flow\" type=\"number\" value=\"0.015\" min=\"0.001\" max=\"0.1\" step=\"0.001\"><input id=\"r-flow\" type=\"range\" value=\"0.015\" min=\"0.001\" max=\"0.1\" step=\"0.001\" aria-label=\"Change Flow (m\u00b3/s)\"></div><div class=\"inp\"><label for=\"head\">Head (m)</label><input id=\"head\" type=\"number\" value=\"25\" min=\"1\" max=\"100\" step=\"1\"><input id=\"r-head\" type=\"range\" value=\"25\" min=\"1\" max=\"100\" step=\"1\" aria-label=\"Change Head (m)\"></div><div class=\"inp\"><label for=\"eff\">Pump efficiency</label><input id=\"eff\" type=\"number\" value=\"0.7\" min=\"0.1\" max=\"1\" step=\"0.01\"><input id=\"r-eff\" type=\"range\" value=\"0.7\" min=\"0.1\" max=\"1\" step=\"0.01\" aria-label=\"Change Pump efficiency\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "rho", "min": 300, "max": 1500, "step": 10}, {"name": "flow", "min": 0.001, "max": 0.1, "step": 0.001}, {"name": "head", "min": 1, "max": 100, "step": 1}, {"name": "eff", "min": 0.1, "max": 1, "step": 0.01}];
function compute(p){return p.rho*9.81*p.flow*p.head/p.eff/1000;}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' kW';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 6,
    unit: 3,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 06 / 16</div><h3>Simple economic break-even quantity</h3><p>Qbreak-even = fixed difference / variable saving</p></header><p class=\"notice\"><strong>Model scope:</strong> Does not include financing, yield, schedule or product changes.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"tooling\">Additional fixed tooling cost</label><input id=\"tooling\" type=\"number\" value=\"12000\" min=\"100\" max=\"100000\" step=\"100\"><input id=\"r-tooling\" type=\"range\" value=\"12000\" min=\"100\" max=\"100000\" step=\"100\" aria-label=\"Change Additional fixed tooling cost\"></div><div class=\"inp\"><label for=\"saving\">Variable cost saving per item</label><input id=\"saving\" type=\"number\" value=\"30\" min=\"1\" max=\"100\" step=\"1\"><input id=\"r-saving\" type=\"range\" value=\"30\" min=\"1\" max=\"100\" step=\"1\" aria-label=\"Change Variable cost saving per item\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "tooling", "min": 100, "max": 100000, "step": 100}, {"name": "saving", "min": 1, "max": 100, "step": 1}];
function compute(p){return p.tooling/p.saving;}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' items';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 7,
    unit: 4,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 07 / 16</div><h3>Cantilever beam deflection</h3><p>\u03b4 = FL\u00b3/(3EI)</p></header><p class=\"notice\"><strong>Model scope:</strong> Small-deflection Euler\u2013Bernoulli beam with ideal clamped root and tip point load.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"force\">Tip load (N)</label><input id=\"force\" type=\"number\" value=\"200\" min=\"10\" max=\"3000\" step=\"10\"><input id=\"r-force\" type=\"range\" value=\"200\" min=\"10\" max=\"3000\" step=\"10\" aria-label=\"Change Tip load (N)\"></div><div class=\"inp\"><label for=\"length\">Length (m)</label><input id=\"length\" type=\"number\" value=\"0.5\" min=\"0.05\" max=\"2\" step=\"0.05\"><input id=\"r-length\" type=\"range\" value=\"0.5\" min=\"0.05\" max=\"2\" step=\"0.05\" aria-label=\"Change Length (m)\"></div><div class=\"inp\"><label for=\"e\">Elastic modulus (GPa)</label><input id=\"e\" type=\"number\" value=\"70\" min=\"2\" max=\"230\" step=\"1\"><input id=\"r-e\" type=\"range\" value=\"70\" min=\"2\" max=\"230\" step=\"1\" aria-label=\"Change Elastic modulus (GPa)\"></div><div class=\"inp\"><label for=\"inertia\">Area moment I (mm\u2074)</label><input id=\"inertia\" type=\"number\" value=\"100000\" min=\"1000\" max=\"2000000\" step=\"1000\"><input id=\"r-inertia\" type=\"range\" value=\"100000\" min=\"1000\" max=\"2000000\" step=\"1000\" aria-label=\"Change Area moment I (mm\u2074)\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "force", "min": 10, "max": 3000, "step": 10}, {"name": "length", "min": 0.05, "max": 2, "step": 0.05}, {"name": "e", "min": 2, "max": 230, "step": 1}, {"name": "inertia", "min": 1000, "max": 2000000, "step": 1000}];
function compute(p){return 1000*p.force*Math.pow(p.length,3)/(3*p.e*1e9*p.inertia*1e-12);}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' mm';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 8,
    unit: 4,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 08 / 16</div><h3>Thermal expansion</h3><p>\u0394L = \u03b1L\u0394T</p></header><p class=\"notice\"><strong>Model scope:</strong> Uniform temperature and unrestrained uniform material; stress requires another model.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"alpha\">Expansion coefficient (10\u207b\u2076/K)</label><input id=\"alpha\" type=\"number\" value=\"23\" min=\"1\" max=\"50\" step=\"1\"><input id=\"r-alpha\" type=\"range\" value=\"23\" min=\"1\" max=\"50\" step=\"1\" aria-label=\"Change Expansion coefficient (10\u207b\u2076/K)\"></div><div class=\"inp\"><label for=\"length\">Original length (m)</label><input id=\"length\" type=\"number\" value=\"1.2\" min=\"0.05\" max=\"5\" step=\"0.05\"><input id=\"r-length\" type=\"range\" value=\"1.2\" min=\"0.05\" max=\"5\" step=\"0.05\" aria-label=\"Change Original length (m)\"></div><div class=\"inp\"><label for=\"dt\">Temperature rise (K)</label><input id=\"dt\" type=\"number\" value=\"30\" min=\"-30\" max=\"150\" step=\"1\"><input id=\"r-dt\" type=\"range\" value=\"30\" min=\"-30\" max=\"150\" step=\"1\" aria-label=\"Change Temperature rise (K)\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "alpha", "min": 1, "max": 50, "step": 1}, {"name": "length", "min": 0.05, "max": 5, "step": 0.05}, {"name": "dt", "min": -30, "max": 150, "step": 1}];
function compute(p){return p.alpha*1e-6*p.length*p.dt*1000;}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' mm';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 9,
    unit: 5,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 09 / 16</div><h3>Natural frequency of one-mode oscillator</h3><p>f = sqrt(k/m)/(2\u03c0)</p></header><p class=\"notice\"><strong>Model scope:</strong> One translational mode, linear stiffness, no damping or coupling.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"stiffness\">Stiffness (N/m)</label><input id=\"stiffness\" type=\"number\" value=\"40000\" min=\"1000\" max=\"500000\" step=\"1000\"><input id=\"r-stiffness\" type=\"range\" value=\"40000\" min=\"1000\" max=\"500000\" step=\"1000\" aria-label=\"Change Stiffness (N/m)\"></div><div class=\"inp\"><label for=\"mass\">Mass (kg)</label><input id=\"mass\" type=\"number\" value=\"10\" min=\"0.5\" max=\"100\" step=\"0.5\"><input id=\"r-mass\" type=\"range\" value=\"10\" min=\"0.5\" max=\"100\" step=\"0.5\" aria-label=\"Change Mass (kg)\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "stiffness", "min": 1000, "max": 500000, "step": 1000}, {"name": "mass", "min": 0.5, "max": 100, "step": 0.5}];
function compute(p){return Math.sqrt(p.stiffness/p.mass)/(2*Math.PI);}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' Hz';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 10,
    unit: 5,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 10 / 16</div><h3>Rotational acceleration torque</h3><p>\u03c4 = J\u03b1 + \u03c4load</p></header><p class=\"notice\"><strong>Model scope:</strong> Neglects variable gear efficiency, friction nonlinearities and peak temperature derating.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"inertia\">Total inertia (kg\u00b7m\u00b2)</label><input id=\"inertia\" type=\"number\" value=\"0.12\" min=\"0.001\" max=\"2\" step=\"0.001\"><input id=\"r-inertia\" type=\"range\" value=\"0.12\" min=\"0.001\" max=\"2\" step=\"0.001\" aria-label=\"Change Total inertia (kg\u00b7m\u00b2)\"></div><div class=\"inp\"><label for=\"alpha\">Angular acceleration (rad/s\u00b2)</label><input id=\"alpha\" type=\"number\" value=\"10\" min=\"-30\" max=\"30\" step=\"0.5\"><input id=\"r-alpha\" type=\"range\" value=\"10\" min=\"-30\" max=\"30\" step=\"0.5\" aria-label=\"Change Angular acceleration (rad/s\u00b2)\"></div><div class=\"inp\"><label for=\"load\">External torque (N\u00b7m)</label><input id=\"load\" type=\"number\" value=\"0.8\" min=\"-20\" max=\"20\" step=\"0.2\"><input id=\"r-load\" type=\"range\" value=\"0.8\" min=\"-20\" max=\"20\" step=\"0.2\" aria-label=\"Change External torque (N\u00b7m)\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "inertia", "min": 0.001, "max": 2, "step": 0.001}, {"name": "alpha", "min": -30, "max": 30, "step": 0.5}, {"name": "load", "min": -20, "max": 20, "step": 0.2}];
function compute(p){return p.inertia*p.alpha+p.load;}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' N·m';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 11,
    unit: 6,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 11 / 16</div><h3>Lifecycle energy cost</h3><p>Annual expense = P \u00d7 h \u00d7 tariff</p></header><p class=\"notice\"><strong>Model scope:</strong> Assumes constant mean power and energy-only billing. Demand charges and seasonal prices omitted.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"power\">Mean electrical demand (kW)</label><input id=\"power\" type=\"number\" value=\"3\" min=\"0.1\" max=\"100\" step=\"0.1\"><input id=\"r-power\" type=\"range\" value=\"3\" min=\"0.1\" max=\"100\" step=\"0.1\" aria-label=\"Change Mean electrical demand (kW)\"></div><div class=\"inp\"><label for=\"hours\">Annual operation (h)</label><input id=\"hours\" type=\"number\" value=\"2500\" min=\"100\" max=\"8760\" step=\"50\"><input id=\"r-hours\" type=\"range\" value=\"2500\" min=\"100\" max=\"8760\" step=\"50\" aria-label=\"Change Annual operation (h)\"></div><div class=\"inp\"><label for=\"tariff\">Energy tariff (currency/kWh)</label><input id=\"tariff\" type=\"number\" value=\"0.18\" min=\"0.01\" max=\"2\" step=\"0.01\"><input id=\"r-tariff\" type=\"range\" value=\"0.18\" min=\"0.01\" max=\"2\" step=\"0.01\" aria-label=\"Change Energy tariff (currency/kWh)\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "power", "min": 0.1, "max": 100, "step": 0.1}, {"name": "hours", "min": 100, "max": 8760, "step": 50}, {"name": "tariff", "min": 0.01, "max": 2, "step": 0.01}];
function compute(p){return p.power*p.hours*p.tariff;}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' currency/year';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 12,
    unit: 6,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 12 / 16</div><h3>Discounted annual savings</h3><p>NPV = \u2212C0 + \u03a3 savings/(1+r)^t</p></header><p class=\"notice\"><strong>Model scope:</strong> Constant real-or-nominal cash-flow convention required; ignore tax, replacement and salvage only for this teaching case.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"cost\">Extra upfront capital</label><input id=\"cost\" type=\"number\" value=\"1000\" min=\"0\" max=\"50000\" step=\"100\"><input id=\"r-cost\" type=\"range\" value=\"1000\" min=\"0\" max=\"50000\" step=\"100\" aria-label=\"Change Extra upfront capital\"></div><div class=\"inp\"><label for=\"save\">End-year annual savings</label><input id=\"save\" type=\"number\" value=\"300\" min=\"0\" max=\"10000\" step=\"100\"><input id=\"r-save\" type=\"range\" value=\"300\" min=\"0\" max=\"10000\" step=\"100\" aria-label=\"Change End-year annual savings\"></div><div class=\"inp\"><label for=\"rate\">Discount fraction</label><input id=\"rate\" type=\"number\" value=\"0.08\" min=\"0\" max=\"0.35\" step=\"0.01\"><input id=\"r-rate\" type=\"range\" value=\"0.08\" min=\"0\" max=\"0.35\" step=\"0.01\" aria-label=\"Change Discount fraction\"></div><div class=\"inp\"><label for=\"years\">Useful life in years</label><input id=\"years\" type=\"number\" value=\"8\" min=\"1\" max=\"20\" step=\"1\"><input id=\"r-years\" type=\"range\" value=\"8\" min=\"1\" max=\"20\" step=\"1\" aria-label=\"Change Useful life in years\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "cost", "min": 0, "max": 50000, "step": 100}, {"name": "save", "min": 0, "max": 10000, "step": 100}, {"name": "rate", "min": 0, "max": 0.35, "step": 0.01}, {"name": "years", "min": 1, "max": 20, "step": 1}];
function compute(p){return (()=>{let y=-p.cost;for(let t=1;t<=Math.round(p.years);t++)y+=p.save/Math.pow(1+p.rate,t);return y})();}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' currency';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 13,
    unit: 7,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 13 / 16</div><h3>Combined independent relative uncertainty</h3><p>ucombined = sqrt(u1\u00b2 + u2\u00b2)</p></header><p class=\"notice\"><strong>Model scope:</strong> First-order uncorrelated uncertainty; covariance and model bias are not included.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"u1\">Relative uncertainty 1 (%)</label><input id=\"u1\" type=\"number\" value=\"2\" min=\"0\" max=\"30\" step=\"0.1\"><input id=\"r-u1\" type=\"range\" value=\"2\" min=\"0\" max=\"30\" step=\"0.1\" aria-label=\"Change Relative uncertainty 1 (%)\"></div><div class=\"inp\"><label for=\"u2\">Relative uncertainty 2 (%)</label><input id=\"u2\" type=\"number\" value=\"1\" min=\"0\" max=\"30\" step=\"0.1\"><input id=\"r-u2\" type=\"range\" value=\"1\" min=\"0\" max=\"30\" step=\"0.1\" aria-label=\"Change Relative uncertainty 2 (%)\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "u1", "min": 0, "max": 30, "step": 0.1}, {"name": "u2", "min": 0, "max": 30, "step": 0.1}];
function compute(p){return Math.hypot(p.u1,p.u2);}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' %';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 14,
    unit: 7,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 14 / 16</div><h3>Series-system survival</h3><p>Rsystem = RA \u00d7 RB \u00d7 RC</p></header><p class=\"notice\"><strong>Model scope:</strong> Independent components, same defined mission; common causes and repair omitted.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"a\">Component A mission survival</label><input id=\"a\" type=\"number\" value=\"0.98\" min=\"0\" max=\"1\" step=\"0.01\"><input id=\"r-a\" type=\"range\" value=\"0.98\" min=\"0\" max=\"1\" step=\"0.01\" aria-label=\"Change Component A mission survival\"></div><div class=\"inp\"><label for=\"b\">Component B mission survival</label><input id=\"b\" type=\"number\" value=\"0.97\" min=\"0\" max=\"1\" step=\"0.01\"><input id=\"r-b\" type=\"range\" value=\"0.97\" min=\"0\" max=\"1\" step=\"0.01\" aria-label=\"Change Component B mission survival\"></div><div class=\"inp\"><label for=\"c\">Component C mission survival</label><input id=\"c\" type=\"number\" value=\"0.99\" min=\"0\" max=\"1\" step=\"0.01\"><input id=\"r-c\" type=\"range\" value=\"0.99\" min=\"0\" max=\"1\" step=\"0.01\" aria-label=\"Change Component C mission survival\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "a", "min": 0, "max": 1, "step": 0.01}, {"name": "b", "min": 0, "max": 1, "step": 0.01}, {"name": "c", "min": 0, "max": 1, "step": 0.01}];
function compute(p){return p.a*p.b*p.c*100;}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' %';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 15,
    unit: 8,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 15 / 16</div><h3>Energy-recovery demonstration balance</h3><p>Pnet = \u03b7generator Pshaft \u2212 Ppump</p></header><p class=\"notice\"><strong>Model scope:</strong> Illustrates power accounting. Excludes additional conversion losses; no free energy or perpetual motion.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"shaft\">Generator shaft input (W)</label><input id=\"shaft\" type=\"number\" value=\"300\" min=\"10\" max=\"3000\" step=\"10\"><input id=\"r-shaft\" type=\"range\" value=\"300\" min=\"10\" max=\"3000\" step=\"10\" aria-label=\"Change Generator shaft input (W)\"></div><div class=\"inp\"><label for=\"eff\">Generator efficiency</label><input id=\"eff\" type=\"number\" value=\"0.9\" min=\"0.1\" max=\"1\" step=\"0.01\"><input id=\"r-eff\" type=\"range\" value=\"0.9\" min=\"0.1\" max=\"1\" step=\"0.01\" aria-label=\"Change Generator efficiency\"></div><div class=\"inp\"><label for=\"pump\">Driving pump electrical input (W)</label><input id=\"pump\" type=\"number\" value=\"500\" min=\"10\" max=\"3000\" step=\"10\"><input id=\"r-pump\" type=\"range\" value=\"500\" min=\"10\" max=\"3000\" step=\"10\" aria-label=\"Change Driving pump electrical input (W)\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "shaft", "min": 10, "max": 3000, "step": 10}, {"name": "eff", "min": 0.1, "max": 1, "step": 0.01}, {"name": "pump", "min": 10, "max": 3000, "step": 10}];
function compute(p){return p.eff*p.shaft-p.pump;}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' W';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 16,
    unit: 8,
    html: "<header class=\"hero\"><div class=\"eyebrow\">Interactive numerical teaching lab \u00b7 16 / 16</div><h3>Design trade-off weighted life energy</h3><p>Energy saved = \u0394P \u00d7 h \u00d7 years</p></header><p class=\"notice\"><strong>Model scope:</strong> Undiscounted electrical energy. Financial savings require tariff and load-profile assumptions.</p><section class=\"inputs\"><div class=\"inp\"><label for=\"watts\">Power reduction (W)</label><input id=\"watts\" type=\"number\" value=\"120\" min=\"1\" max=\"2500\" step=\"1\"><input id=\"r-watts\" type=\"range\" value=\"120\" min=\"1\" max=\"2500\" step=\"1\" aria-label=\"Change Power reduction (W)\"></div><div class=\"inp\"><label for=\"hours\">Annual hours</label><input id=\"hours\" type=\"number\" value=\"2000\" min=\"100\" max=\"8760\" step=\"100\"><input id=\"r-hours\" type=\"range\" value=\"2000\" min=\"100\" max=\"8760\" step=\"100\" aria-label=\"Change Annual hours\"></div><div class=\"inp\"><label for=\"years\">Operating years</label><input id=\"years\" type=\"number\" value=\"7\" min=\"1\" max=\"20\" step=\"1\"><input id=\"r-years\" type=\"range\" value=\"7\" min=\"1\" max=\"20\" step=\"1\" aria-label=\"Change Operating years\"></div></section><div class=\"output\"><div>Calculated result</div><div class=\"num\" id=\"value\" aria-live=\"polite\">\u2014</div><div class=\"sub\">Change any input to recompute. The graph samples the first parameter across its declared range.</div><svg id=\"chart\" class=\"svg\" viewBox=\"0 0 720 180\" role=\"img\" aria-label=\"Output sensitivity curve\"></svg><p id=\"warning\" class=\"sub\"></p></div><p></p>",
    init: function(card) {
      try {
"use strict";
const spec=[{"name": "watts", "min": 1, "max": 2500, "step": 1}, {"name": "hours", "min": 100, "max": 8760, "step": 100}, {"name": "years", "min": 1, "max": 20, "step": 1}];
function compute(p){return p.watts/1000*p.hours*p.years;}
if (typeof module!=="undefined")module.exports={compute,spec};
if (typeof document!=="undefined"){
 const inputs=Object.fromEntries(spec.map(v=>[v.name,document.getElementById(v.name)]));
 const sliders=Object.fromEntries(spec.map(v=>[v.name,document.getElementById('r-'+v.name)]));
 const result=card.querySelector("#" + 'value'.replace(/^#/, ""));const warning=card.querySelector("#" + 'warning'.replace(/^#/, ""));const svg=card.querySelector("#" + 'chart'.replace(/^#/, ""));
 function values(){let p={};for(const v of spec){const n=Number(inputs[v.name].value);if(!Number.isFinite(n)||n<v.min||n>v.max)return null;p[v.name]=n;}return p;}
 function display(){const p=values();if(p===null){result.textContent='Check input bounds';warning.textContent='Inputs must be finite and inside their stated ranges.';svg.innerHTML='';return;}
 let y=compute(p);if(!Number.isFinite(y)){result.textContent='Undefined';warning.textContent='This parameter combination is outside the model.';return;}
 result.textContent=y.toLocaleString(undefined,{maximumFractionDigits:4})+' kWh';warning.textContent='Teaching equation only; verify full operating conditions and model limits before any real engineering decision.';
 const lead=spec[0], arr=[];for(let i=0;i<=50;i++){let x=lead.min+(lead.max-lead.min)*i/50;let pp={...p,[lead.name]:x}, yy=compute(pp);if(Number.isFinite(yy))arr.push([x,yy]);}
 if(arr.length<2){svg.innerHTML='';return;}let ymin=Math.min(...arr.map(v=>v[1])),ymax=Math.max(...arr.map(v=>v[1]));if(ymax-ymin<1e-12){ymax+=1;ymin-=1;}
 const pts=arr.map(([x,z])=>{let X=44+630*(x-lead.min)/(lead.max-lead.min);let Y=150-112*(z-ymin)/(ymax-ymin);return X.toFixed(2)+','+Y.toFixed(2);}).join(' ');
 const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
 const frame=document.createElementNS(ns,'path');frame.setAttribute('d','M 44 20 V 150 H 680');frame.setAttribute('stroke','#b0c2c3');frame.setAttribute('fill','none');svg.appendChild(frame);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('stroke','#187e86');line.setAttribute('stroke-width','3');line.setAttribute('fill','none');svg.appendChild(line);
 const t=document.createElementNS(ns,'text');t.setAttribute('x','50');t.setAttribute('y','16');t.setAttribute('fill','#235461');t.setAttribute('font-size','13');t.textContent=lead.name+' sensitivity ('+ymin.toPrecision(3)+'–'+ymax.toPrecision(3)+')';svg.appendChild(t);
 }
 for(const v of spec){inputs[v.name].addEventListener('input',()=>{sliders[v.name].value=inputs[v.name].value;display();});sliders[v.name].addEventListener('input',()=>{inputs[v.name].value=sliders[v.name].value;display();});}
 display();}
      } catch (err) {
        console.warn('Sim init error in model 16:', err);
      }
    }
  });

  if (!window.SimulationEngine) {
    window.SimulationEngine = {};
  }

  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId || 'sim-container');
    if (!container) return;
    container.innerHTML = '';

    var unitNum = 1;
    if (simType) {
      var m = simType.match(/(\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    } else {
      var bMatch = document.body.dataset.chapterIndex;
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') {
        unitNum = parseInt(bMatch, 10) + 1;
      } else {
        var pMatch = window.location.pathname.match(/chapter-(\d+)/);
        if (pMatch) {
          unitNum = parseInt(pMatch[1], 10);
        }
      }
    }

    if (isNaN(unitNum) || unitNum < 1 || unitNum > 8) unitNum = 1;

    var modelsForUnit = OPENSTEM_SIM_MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = OPENSTEM_SIM_MODELS.slice(0, 2);

    modelsForUnit.forEach(function(m) {
      var card = document.createElement('section');
      card.className = 'me-sim-card';
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
        if (document.getElementById('sim-container')) {
          window.SimulationEngine.initSimulation('sim-container');
        }
      });
    } else {
      if (document.getElementById('sim-container')) {
        window.SimulationEngine.initSimulation('sim-container');
      }
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
