/* fluid-mechanics Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 01</span><h3>Reynolds number</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Mean speed (m/s): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0.03\" max=\"3.0\" step=\"0.01\" value=\"1.515\"/><p>Re: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Reynolds number based on water-like fluid, D=0.05 m, \u03bc=0.001 Pa\u00b7s; not a universal transition threshold.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Mean speed (m/s)", "low": 0.03, "high": 3.0, "step": 0.01, "expression": "1000*u*0.05/0.001", "title": "Reynolds number", "output": "Re", "unit": "", "limitation": "Reynolds number based on water-like fluid, D=0.05 m, μ=0.001 Pa·s; not a universal transition threshold."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return 1000*u*0.05/0.001;}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' ';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Re</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Mean speed (m/s)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 1,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 02</span><h3>Capillary rise</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Capillary radius (mm): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0.1\" max=\"2.0\" step=\"0.01\" value=\"1.05\"/><p>Rise: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Ideal vertical circular tube, full wetting \u03b8=0; ignores contact angle hysteresis.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Capillary radius (mm)", "low": 0.1, "high": 2.0, "step": 0.01, "expression": "1000*2*0.072/(1000*9.81*(u/1000))", "title": "Capillary rise", "output": "Rise", "unit": "mm", "limitation": "Ideal vertical circular tube, full wetting θ=0; ignores contact angle hysteresis."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return 1000*2*0.072/(1000*9.81*(u/1000));}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' mm';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Rise</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Capillary radius (mm)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 2,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 03</span><h3>Hydrostatic gauge pressure</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Depth below free surface (m): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0\" max=\"15\" step=\"0.1\" value=\"7.5\"/><p>Pressure: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Constant-density water, free surface atmospheric, no acceleration.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Depth below free surface (m)", "low": 0, "high": 15, "step": 0.1, "expression": "1000*9.81*u/1000", "title": "Hydrostatic gauge pressure", "output": "Pressure", "unit": "kPa", "limitation": "Constant-density water, free surface atmospheric, no acceleration."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return 1000*9.81*u/1000;}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' kPa';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Pressure</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Depth below free surface (m)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 2,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 04</span><h3>Buoyant force</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Displaced volume (litres): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0\" max=\"50\" step=\"0.2\" value=\"25.0\"/><p>Force: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Fully submerged or displaced volume in fresh water, uniform g.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Displaced volume (litres)", "low": 0, "high": 50, "step": 0.2, "expression": "1000*9.81*(u/1000)", "title": "Buoyant force", "output": "Force", "unit": "N", "limitation": "Fully submerged or displaced volume in fresh water, uniform g."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return 1000*9.81*(u/1000);}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' N';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Force</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Displaced volume (litres)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 3,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 05</span><h3>Volume flow in a pipe</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Mean velocity (m/s): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0\" max=\"7\" step=\"0.05\" value=\"3.5\"/><p>Flow: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Internal diameter 0.08 m; velocity is section mean and density approximately constant.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Mean velocity (m/s)", "low": 0, "high": 7, "step": 0.05, "expression": "Math.PI*(0.08**2)/4*u*1000", "title": "Volume flow in a pipe", "output": "Flow", "unit": "L/s", "limitation": "Internal diameter 0.08 m; velocity is section mean and density approximately constant."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return Math.PI*(0.08**2)/4*u*1000;}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' L/s';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Flow</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Mean velocity (m/s)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 3,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 06</span><h3>Mass flow through a pipe</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Fluid density (kg/m\u00b3): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"500\" max=\"1300\" step=\"10\" value=\"900.0\"/><p>Mass flow: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Volumetric flow fixed at 0.010 m\u00b3/s; density assumed uniform at section.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Fluid density (kg/m³)", "low": 500, "high": 1300, "step": 10, "expression": "u*0.010", "title": "Mass flow through a pipe", "output": "Mass flow", "unit": "kg/s", "limitation": "Volumetric flow fixed at 0.010 m³/s; density assumed uniform at section."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return u*0.010;}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' kg/s';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Mass flow</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Fluid density (kg/m³)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 4,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 07</span><h3>Ideal Bernoulli pressure change</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Downstream speed (m/s): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0\" max=\"10\" step=\"0.1\" value=\"5.0\"/><p>\u0394p downstream\u2212upstream: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Steady, inviscid, horizontal water flow, upstream speed 2 m/s.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Downstream speed (m/s)", "low": 0, "high": 10, "step": 0.1, "expression": "(1000*0.5*(2*2-u*u))/1000", "title": "Ideal Bernoulli pressure change", "output": "Δp downstream−upstream", "unit": "kPa", "limitation": "Steady, inviscid, horizontal water flow, upstream speed 2 m/s."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return (1000*0.5*(2*2-u*u))/1000;}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' kPa';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Δp downstream−upstream</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Downstream speed (m/s)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 4,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 08</span><h3>Ideal tank-outlet velocity</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Outlet depth (m): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0\" max=\"7\" step=\"0.05\" value=\"3.5\"/><p>Speed: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Large open reservoir, no losses or vena contracta; real discharge usually lower.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Outlet depth (m)", "low": 0, "high": 7, "step": 0.05, "expression": "Math.sqrt(2*9.81*u)", "title": "Ideal tank-outlet velocity", "output": "Speed", "unit": "m/s", "limitation": "Large open reservoir, no losses or vena contracta; real discharge usually lower."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return Math.sqrt(2*9.81*u);}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' m/s';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Speed</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Outlet depth (m)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  MODELS.push({
    idx: 9,
    unit: 5,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 09</span><h3>Pipe Reynolds number</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Mean velocity (m/s): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0.05\" max=\"4\" step=\"0.02\" value=\"2.025\"/><p>Re: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Water-like fluid, D=0.04 m. Transitional region uncertain.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Mean velocity (m/s)", "low": 0.05, "high": 4, "step": 0.02, "expression": "1000*u*0.04/0.001", "title": "Pipe Reynolds number", "output": "Re", "unit": "", "limitation": "Water-like fluid, D=0.04 m. Transitional region uncertain."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return 1000*u*0.04/0.001;}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' ';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Re</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Mean velocity (m/s)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  MODELS.push({
    idx: 10,
    unit: 5,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 10</span><h3>Darcy friction head loss</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Mean velocity (m/s): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0\" max=\"4\" step=\"0.02\" value=\"2.0\"/><p>Head loss: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Illustrative fixed Darcy f=0.025, L=40 m, D=0.08 m; fitting losses excluded.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Mean velocity (m/s)", "low": 0, "high": 4, "step": 0.02, "expression": "0.025*(40/0.08)*(u*u)/(2*9.81)", "title": "Darcy friction head loss", "output": "Head loss", "unit": "m", "limitation": "Illustrative fixed Darcy f=0.025, L=40 m, D=0.08 m; fitting losses excluded."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return 0.025*(40/0.08)*(u*u)/(2*9.81);}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' m';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Head loss</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Mean velocity (m/s)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  MODELS.push({
    idx: 11,
    unit: 6,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 11</span><h3>Drag on a bluff body</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Free-stream speed (m/s): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0\" max=\"35\" step=\"0.2\" value=\"17.5\"/><p>Drag: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Air density 1.2 kg/m\u00b3, Cd=0.8, reference area 0.5 m\u00b2 fixed.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Free-stream speed (m/s)", "low": 0, "high": 35, "step": 0.2, "expression": "0.5*1.2*(u*u)*0.8*0.5", "title": "Drag on a bluff body", "output": "Drag", "unit": "N", "limitation": "Air density 1.2 kg/m³, Cd=0.8, reference area 0.5 m² fixed."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return 0.5*1.2*(u*u)*0.8*0.5;}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' N';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Drag</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Free-stream speed (m/s)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  MODELS.push({
    idx: 12,
    unit: 6,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 12</span><h3>Vortex shedding frequency</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Free-stream speed (m/s): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0\" max=\"24\" step=\"0.2\" value=\"12.0\"/><p>Frequency: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Illustrative Strouhal number 0.20, diameter 0.10 m; dependence on Re omitted.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Free-stream speed (m/s)", "low": 0, "high": 24, "step": 0.2, "expression": "0.20*u/0.10", "title": "Vortex shedding frequency", "output": "Frequency", "unit": "Hz", "limitation": "Illustrative Strouhal number 0.20, diameter 0.10 m; dependence on Re omitted."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return 0.20*u/0.10;}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' Hz';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Frequency</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Free-stream speed (m/s)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  MODELS.push({
    idx: 13,
    unit: 7,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 13</span><h3>Pump input power</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Volume flow (L/s): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"1\" max=\"45\" step=\"0.5\" value=\"23.0\"/><p>Input power: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Head 15 m, constant overall efficiency 70%; real efficiency varies with flow.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Volume flow (L/s)", "low": 1, "high": 45, "step": 0.5, "expression": "(1000*9.81*(u/1000)*15/0.70)/1000", "title": "Pump input power", "output": "Input power", "unit": "kW", "limitation": "Head 15 m, constant overall efficiency 70%; real efficiency varies with flow."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return (1000*9.81*(u/1000)*15/0.70)/1000;}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' kW';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Input power</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Volume flow (L/s)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  MODELS.push({
    idx: 14,
    unit: 7,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 14</span><h3>Rectangular channel Froude number</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Channel-mean speed (m/s): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0.05\" max=\"6\" step=\"0.05\" value=\"3.025\"/><p>Fr: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Hydraulic depth equals constant water depth y=0.40 m for rectangular channel.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Channel-mean speed (m/s)", "low": 0.05, "high": 6, "step": 0.05, "expression": "u/Math.sqrt(9.81*0.40)", "title": "Rectangular channel Froude number", "output": "Fr", "unit": "", "limitation": "Hydraulic depth equals constant water depth y=0.40 m for rectangular channel."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return u/Math.sqrt(9.81*0.40);}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' ';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Fr</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Channel-mean speed (m/s)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  MODELS.push({
    idx: 15,
    unit: 8,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 15</span><h3>Ideal Pitot velocity</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Pressure difference (Pa): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0\" max=\"2500\" step=\"10\" value=\"1250.0\"/><p>Speed: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Ideal liquid, density 1000 kg/m\u00b3, low-speed incompressible assumption.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Pressure difference (Pa)", "low": 0, "high": 2500, "step": 10, "expression": "Math.sqrt(2*u/1000)", "title": "Ideal Pitot velocity", "output": "Speed", "unit": "m/s", "limitation": "Ideal liquid, density 1000 kg/m³, low-speed incompressible assumption."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return Math.sqrt(2*u/1000);}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' m/s';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Speed</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Pressure difference (Pa)</text>';
}
input.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  MODELS.push({
    idx: 16,
    unit: 8,
    html: "<div class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 16</span><h3>Instantaneous water-hammer surge</h3><p>Move the slider to explore a precisely stated approximate relation. No network connection required.</p></div><div class=\"model\"><label for=\"slider\">Magnitude of \u0394V (m/s): <strong id=\"ins\">\u2014</strong></label><input id=\"slider\" type=\"range\" min=\"0\" max=\"2.0\" step=\"0.01\" value=\"1.0\"/><p>Surge magnitude: <output id=\"result\" aria-live=\"polite\">\u2014</output></p><svg id=\"graph\" viewBox=\"0 0 590 289\" role=\"img\" aria-label=\"Illustrative response curve and selected operating point\" class=\"chart\"></svg><p class=\"capt\">Response curve calculated locally from the teaching formula; actual measured behavior may differ.</p></div><div class=\"model-info\"><strong>Assumptions and limitations:</strong> Ideal sudden change, wave speed 1000 m/s; pipe transients may differ.</div><h2>Challenge the model</h2><p>Predict the direction of change before moving the slider. Reproduce one value by hand. Identify a plausible real measurement that could disagree with this model. This interactive illustration is not a calibrated simulator or an engineering certification tool.</p>",
    init: function(card) {
      try {
const S={"label": "Magnitude of ΔV (m/s)", "low": 0, "high": 2.0, "step": 0.01, "expression": "1000*1000*u/1000000", "title": "Instantaneous water-hammer surge", "output": "Surge magnitude", "unit": "MPa", "limitation": "Ideal sudden change, wave speed 1000 m/s; pipe transients may differ."};
const input=card.querySelector("#" + 'slider'.replace(/^#/, "")),shown=card.querySelector("#" + 'ins'.replace(/^#/, "")),readout=card.querySelector("#" + 'result'.replace(/^#/, "")),svg=card.querySelector("#" + 'graph'.replace(/^#/, ""));
function formula(u){return 1000*1000*u/1000000;}
function fnum(v){ if(!Number.isFinite(v)) return 'invalid'; if(Math.abs(v)>=10000) return v.toLocaleString('en-US',{maximumFractionDigits:0});return v.toLocaleString('en-US',{maximumFractionDigits:3}); }
function update(){const u=Number(input.value),v=formula(u);shown.textContent=fnum(u);readout.textContent=fnum(v)+' MPa';
 let arr=[];for(let k=0;k<=80;k++){let x=S.low+(S.high-S.low)*k/80;let y=formula(x);if(Number.isFinite(y))arr.push([x,y]);}
 const mn=Math.min(...arr.map(z=>z[1])),mx=Math.max(...arr.map(z=>z[1]));let heightRange=Math.max(1e-9,mx-mn);
 const px=x=>38+510*(x-S.low)/(S.high-S.low);const py=y=>248-195*(y-mn)/heightRange;
 const d=arr.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(1)+','+py(p[1]).toFixed(1)).join(' ');
 const limited=Math.max(mn,Math.min(mx,v));svg.innerHTML='<line x1="38" y1="248" x2="550" y2="248" class="axis"/><line x1="38" y1="38" x2="38" y2="248" class="axis"/><path class="curve" d="'+d+'"/><circle class="dot" cx="'+px(u)+'" cy="'+py(limited)+'" r="6"/><text x="43" y="25" fill="#bdd6ea" font-size="14">Surge magnitude</text><text x="400" y="273" fill="#bdd6ea" font-size="12">Magnitude of ΔV (m/s)</text>';
}
input.addEventListener('input',update);update();
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

    var modelsForUnit = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 2);

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

  // Auto-init when DOM is ready if #sim-container is present
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
