/* refrigeration-and-air-conditioning Interactive Simulation Suite */
(function(window) {
  'use strict';

  var OPENSTEM_SIM_MODELS = [];
  // Core model definitions
const MODELS=[{"id": 1, "title": "Air sensible cooling demand", "formula": "Q = ṁ cₚ ΔT", "unit": "kW", "inputs": [{"label": "Air mass flow", "unit": "kg/s", "min": 0.1, "max": 3, "step": 0.05, "default": 0.7}, {"label": "Heat capacity", "unit": "kJ/(kg K)", "min": 0.95, "max": 1.1, "step": 0.005, "default": 1.005}, {"label": "Temperature reduction", "unit": "K", "min": 2, "max": 22, "step": 0.5, "default": 10}], "expr": "p[0]*p[1]*p[2]", "warning": "Assumes a single phase, constant specific heat and a steady boundary."}, {"id": 2, "title": "Envelope conduction heat rate", "formula": "Q = U A ΔT", "unit": "kW", "inputs": [{"label": "U-value", "unit": "W/(m² K)", "min": 0.1, "max": 2, "step": 0.05, "default": 0.8}, {"label": "Surface area", "unit": "m²", "min": 10, "max": 400, "step": 5, "default": 60}, {"label": "Temperature difference", "unit": "K", "min": 2, "max": 25, "step": 1, "default": 12}], "expr": "p[0]*p[1]*p[2]/1000", "warning": "Steady uniform U-value model; no solar heat or thermal storage."}, {"id": 3, "title": "Cooling coefficient of performance", "formula": "COP = useful cooling / electrical power", "unit": "dimensionless", "inputs": [{"label": "Useful cooling", "unit": "kW", "min": 1, "max": 30, "step": 0.5, "default": 9}, {"label": "Electrical input", "unit": "kW", "min": 0.5, "max": 10, "step": 0.1, "default": 3}], "expr": "p[0]/p[1]", "warning": "System boundary must be identical for the cooling and electrical measurements."}, {"id": 4, "title": "Reversible Carnot COP benchmark", "formula": "COP = Tcold/(Thot − Tcold)", "unit": "dimensionless", "inputs": [{"label": "Cold reservoir", "unit": "K", "min": 245, "max": 293, "step": 1, "default": 278}, {"label": "Hot reservoir", "unit": "K", "min": 300, "max": 350, "step": 1, "default": 318}], "expr": "p[0]/(p[1]-p[0])", "warning": "A reversible upper benchmark, not a physically achievable machine rating."}, {"id": 5, "title": "Compressor specific-work power", "formula": "Ẇ = ṁref (h₂ − h₁)", "unit": "kW", "inputs": [{"label": "Refrigerant flow", "unit": "kg/s", "min": 0.005, "max": 0.2, "step": 0.005, "default": 0.05}, {"label": "Specific enthalpy rise", "unit": "kJ/kg", "min": 15, "max": 100, "step": 1, "default": 45}], "expr": "p[0]*p[1]", "warning": "Thermodynamic flow work only; motor and drive inputs may be higher."}, {"id": 6, "title": "Condenser heat rejection", "formula": "Qcond = Qevap + Wcomp", "unit": "kW", "inputs": [{"label": "Evaporator cooling", "unit": "kW", "min": 1, "max": 30, "step": 1, "default": 12}, {"label": "Compressor input", "unit": "kW", "min": 0.5, "max": 12, "step": 0.5, "default": 4}], "expr": "p[0]+p[1]", "warning": "Steady simple cycle; neglects heat leaks, fan energy and other auxiliaries."}, {"id": 7, "title": "Humidity ratio from water-vapor partial pressure", "formula": "w = 0.62198 pᵥ/(P−pᵥ)", "unit": "kg/kg dry air", "inputs": [{"label": "Vapor partial pressure", "unit": "kPa", "min": 0.2, "max": 3.5, "step": 0.05, "default": 1.8}, {"label": "Total pressure", "unit": "kPa", "min": 80, "max": 105, "step": 1, "default": 101}], "expr": "0.62198*p[0]/(p[1]-p[0])", "warning": "Idealized gas mixture; water partial pressure must be physically compatible with temperature."}, {"id": 8, "title": "Approximate moist-air enthalpy", "formula": "h = 1.006T + w(2501 + 1.86T)", "unit": "kJ/kg dry air", "inputs": [{"label": "Dry-bulb temperature", "unit": "°C", "min": 5, "max": 42, "step": 1, "default": 25}, {"label": "Humidity ratio", "unit": "kg/kg dry air", "min": 0.001, "max": 0.025, "step": 0.001, "default": 0.01}], "expr": "1.006*p[0]+p[1]*(2501+1.86*p[0])", "warning": "Standard engineering approximation near atmospheric conditions; verify psychrometric state."}, {"id": 9, "title": "Simple glazing solar gain", "formula": "Q = A G SHGC", "unit": "kW", "inputs": [{"label": "Glass area", "unit": "m²", "min": 2, "max": 100, "step": 1, "default": 15}, {"label": "Incident irradiance", "unit": "W/m²", "min": 100, "max": 1000, "step": 10, "default": 600}, {"label": "Solar heat gain coefficient", "unit": "fraction", "min": 0.1, "max": 0.9, "step": 0.05, "default": 0.35}], "expr": "p[0]*p[1]*p[2]/1000", "warning": "Does not resolve time-varying sun angle, frame gains or detailed shading."}, {"id": 10, "title": "Occupants and equipment sensible gain", "formula": "Q = N q/person + Qequipment", "unit": "kW", "inputs": [{"label": "Number of occupants", "unit": "people", "min": 1, "max": 100, "step": 1, "default": 25}, {"label": "Assumed sensible gain", "unit": "W/person", "min": 40, "max": 140, "step": 5, "default": 80}, {"label": "Equipment/lighting", "unit": "kW", "min": 0, "max": 10, "step": 0.25, "default": 2}], "expr": "p[0]*p[1]/1000+p[2]", "warning": "A constructed load estimate; excludes latent occupant gains and schedules."}, {"id": 11, "title": "Outdoor-air sensible load", "formula": "Q = ṁair cₚ ΔT", "unit": "kW", "inputs": [{"label": "Outdoor dry-air flow", "unit": "kg/s", "min": 0.05, "max": 2, "step": 0.05, "default": 0.4}, {"label": "Specific heat", "unit": "kJ/(kg K)", "min": 0.95, "max": 1.1, "step": 0.005, "default": 1.005}, {"label": "Temperature difference", "unit": "K", "min": 1, "max": 25, "step": 1, "default": 12}], "expr": "p[0]*p[1]*p[2]", "warning": "Outdoor-air latent load must be estimated separately for humid conditions."}, {"id": 12, "title": "Nominal room air changes", "formula": "ACH = 3600 V̇ / Volume", "unit": "air changes/h", "inputs": [{"label": "Supply volume flow", "unit": "m³/s", "min": 0.03, "max": 2, "step": 0.01, "default": 0.3}, {"label": "Room volume", "unit": "m³", "min": 40, "max": 1200, "step": 20, "default": 350}], "expr": "3600*p[0]/p[1]", "warning": "ACH is not a measured clean-air delivery or exposure reduction metric."}, {"id": 13, "title": "Fan electrical input estimate", "formula": "P = Δp V̇/(1000η)", "unit": "kW", "inputs": [{"label": "Fan pressure rise", "unit": "Pa", "min": 100, "max": 1600, "step": 25, "default": 650}, {"label": "Flow", "unit": "m³/s", "min": 0.1, "max": 3, "step": 0.1, "default": 1}, {"label": "Total efficiency", "unit": "fraction", "min": 0.3, "max": 0.85, "step": 0.05, "default": 0.6}], "expr": "p[0]*p[1]/(1000*p[2])", "warning": "Electrical energy may include additional drive, standby and control loads."}, {"id": 14, "title": "Seasonal cooling COP", "formula": "COPseason = ΣQdelivered/ΣWelectric", "unit": "dimensionless", "inputs": [{"label": "Total cooling delivered", "unit": "kWh", "min": 100, "max": 12000, "step": 100, "default": 3600}, {"label": "Total electricity", "unit": "kWh", "min": 100, "max": 5000, "step": 50, "default": 1000}], "expr": "p[0]/p[1]", "warning": "A ratio of measured energies over the same period and system boundary."}, {"id": 15, "title": "First-order room thermal response", "formula": "T(t) = Teq +(T0−Teq) exp(−t/τ)", "unit": "°C", "inputs": [{"label": "Initial temperature", "unit": "°C", "min": 18, "max": 34, "step": 0.5, "default": 29}, {"label": "Equilibrium temperature", "unit": "°C", "min": 18, "max": 30, "step": 0.5, "default": 23}, {"label": "Elapsed time", "unit": "h", "min": 0, "max": 12, "step": 0.25, "default": 2}, {"label": "Time constant", "unit": "h", "min": 0.5, "max": 8, "step": 0.25, "default": 2}], "expr": "p[1]+(p[0]-p[1])*Math.exp(-p[2]/p[3])", "warning": "Idealized first-order response; ignores disturbances, humidity and controller logic."}, {"id": 16, "title": "Undiscounted project net savings", "formula": "Net = years × annual savings − upfront cost", "unit": "currency units", "inputs": [{"label": "Annual savings", "unit": "currency/year", "min": 100, "max": 6000, "step": 100, "default": 1000}, {"label": "Years", "unit": "years", "min": 1, "max": 20, "step": 1, "default": 8}, {"label": "Initial cost", "unit": "currency units", "min": 500, "max": 30000, "step": 500, "default": 6000}], "expr": "p[0]*p[1]-p[2]", "warning": "Undiscounted screening only; excludes time value, maintenance, replacement and risk."}];
function computeModel(id,p){const m=MODELS.find(x=>x.id===Number(id));if(!m)throw new Error("Unknown model");for(let i=0;i<p.length;i++)if(!Number.isFinite(Number(p[i])))throw Error("Invalid input");switch(Number(id)){
case 1: return p[0]*p[1]*p[2];
case 2: return p[0]*p[1]*p[2]/1000;
case 3: return p[0]/p[1];
case 4: return p[0]/(p[1]-p[0]);
case 5: return p[0]*p[1];
case 6: return p[0]+p[1];
case 7: return 0.62198*p[0]/(p[1]-p[0]);
case 8: return 1.006*p[0]+p[1]*(2501+1.86*p[0]);
case 9: return p[0]*p[1]*p[2]/1000;
case 10: return p[0]*p[1]/1000+p[2];
case 11: return p[0]*p[1]*p[2];
case 12: return 3600*p[0]/p[1];
case 13: return p[0]*p[1]/(1000*p[2]);
case 14: return p[0]/p[1];
case 15: return p[1]+(p[0]-p[1])*Math.exp(-p[2]/p[3]);
case 16: return p[0]*p[1]-p[2];
default:throw new Error("Unknown model");}}
if(typeof module!=="undefined"&&module.exports)module.exports={MODELS,computeModel};



  OPENSTEM_SIM_MODELS.push({
    idx: 1,
    unit: 1,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 01 / 16</div><h3>Air sensible cooling demand</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">Assumes a single phase, constant specific heat and a steady boundary. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">Q = m\u0307 c\u209a \u0394T</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(1);
        document.body.dataset.model = String(1);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 2,
    unit: 1,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 02 / 16</div><h3>Envelope conduction heat rate</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">Steady uniform U-value model; no solar heat or thermal storage. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">Q = U A \u0394T</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(2);
        document.body.dataset.model = String(2);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 3,
    unit: 2,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 03 / 16</div><h3>Cooling coefficient of performance</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">System boundary must be identical for the cooling and electrical measurements. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">COP = useful cooling / electrical power</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(3);
        document.body.dataset.model = String(3);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 4,
    unit: 2,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 04 / 16</div><h3>Reversible Carnot COP benchmark</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">A reversible upper benchmark, not a physically achievable machine rating. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">COP = Tcold/(Thot \u2212 Tcold)</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(4);
        document.body.dataset.model = String(4);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 5,
    unit: 3,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 05 / 16</div><h3>Compressor specific-work power</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">Thermodynamic flow work only; motor and drive inputs may be higher. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">W\u0307 = m\u0307ref (h\u2082 \u2212 h\u2081)</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(5);
        document.body.dataset.model = String(5);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 6,
    unit: 3,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 06 / 16</div><h3>Condenser heat rejection</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">Steady simple cycle; neglects heat leaks, fan energy and other auxiliaries. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">Qcond = Qevap + Wcomp</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(6);
        document.body.dataset.model = String(6);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 7,
    unit: 4,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 07 / 16</div><h3>Humidity ratio from water-vapor partial pressure</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">Idealized gas mixture; water partial pressure must be physically compatible with temperature. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">w = 0.62198 p\u1d65/(P\u2212p\u1d65)</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(7);
        document.body.dataset.model = String(7);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 8,
    unit: 4,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 08 / 16</div><h3>Approximate moist-air enthalpy</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">Standard engineering approximation near atmospheric conditions; verify psychrometric state. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">h = 1.006T + w(2501 + 1.86T)</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(8);
        document.body.dataset.model = String(8);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 9,
    unit: 5,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 09 / 16</div><h3>Simple glazing solar gain</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">Does not resolve time-varying sun angle, frame gains or detailed shading. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">Q = A G SHGC</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(9);
        document.body.dataset.model = String(9);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 10,
    unit: 5,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 10 / 16</div><h3>Occupants and equipment sensible gain</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">A constructed load estimate; excludes latent occupant gains and schedules. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">Q = N q/person + Qequipment</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(10);
        document.body.dataset.model = String(10);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 11,
    unit: 6,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 11 / 16</div><h3>Outdoor-air sensible load</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">Outdoor-air latent load must be estimated separately for humid conditions. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">Q = m\u0307air c\u209a \u0394T</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(11);
        document.body.dataset.model = String(11);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 12,
    unit: 6,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 12 / 16</div><h3>Nominal room air changes</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">ACH is not a measured clean-air delivery or exposure reduction metric. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">ACH = 3600 V\u0307 / Volume</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(12);
        document.body.dataset.model = String(12);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 13,
    unit: 7,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 13 / 16</div><h3>Fan electrical input estimate</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">Electrical energy may include additional drive, standby and control loads. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">P = \u0394p V\u0307/(1000\u03b7)</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(13);
        document.body.dataset.model = String(13);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 14,
    unit: 7,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 14 / 16</div><h3>Seasonal cooling COP</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">A ratio of measured energies over the same period and system boundary. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">COPseason = \u03a3Qdelivered/\u03a3Welectric</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(14);
        document.body.dataset.model = String(14);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 15,
    unit: 8,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 15 / 16</div><h3>First-order room thermal response</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">Idealized first-order response; ignores disturbances, humidity and controller logic. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">T(t) = Teq +(T0\u2212Teq) exp(\u2212t/\u03c4)</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(15);
        document.body.dataset.model = String(15);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 16,
    unit: 8,
    html: "<header class=\"hero\"><div class=\"eyebrow\">INTERACTIVE MODEL 16 / 16</div><h3>Undiscounted project net savings</h3><p class=\"subtitle\">Change an input to explore the indicated analytical relationship entirely offline.</p><div class=\"metrics\"><span>40 lessons</span><span>8 units</span><span>16 offline calculators</span><span>8 synthetic datasets</span></div></header><p class=\"notice\">Undiscounted screening only; excludes time value, maintenance, replacement and risk. Equation-based sensitivity only: not measured performance, equipment design approval or a safety prediction.</p><section class=\"panel\"><h2>Adjust model inputs</h2><div class=\"controls\" id=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"result\" aria-live=\"polite\">\u2014</div><p class=\"formula\">Net = years \u00d7 annual savings \u2212 upfront cost</p><p class=\"status\" id=\"model-status\" aria-live=\"polite\">Model values are bounded teaching assumptions.</p></section><section class=\"panel\"><h2>Sensitivity to the first input</h2><svg class=\"graph\" id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Computed output as first parameter changes; other inputs are held constant\"></svg><p class=\"fine\">The curve shows an equation, not observed experimental measurements. Change the first slider to update the response.</p></section>",
    init: function(card) {
      try {
        card.dataset.model = String(16);
        document.body.dataset.model = String(16);
const target=card.querySelector('main[data-model]');if(!target)return;const id=Number(target.dataset.model);const m=MODELS.find(x=>x.id===id);const root=card.querySelector("#" + 'controls'.replace(/^#/, ""));const out=card.querySelector("#" + 'output'.replace(/^#/, ""));const graph=card.querySelector("#" + 'plot'.replace(/^#/, ""));const st=card.querySelector("#" + 'model-status'.replace(/^#/, ""));const xs=[];
const fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:4});
function render(){const p=xs.map(el=>Number(el.value));let y;try{y=computeModel(id,p)}catch(ex){st.textContent=String(ex);return}out.textContent=`${fmt(y)} ${m.unit}`;xs.forEach((el,i)=>card.querySelector("#" + `value-${i}`).textContent=`${fmt(p[i])} ${m.inputs[i].unit}`);
let yy=[];const first=m.inputs[0];const n=65;for(let j=0;j<n;j++){let copy=p.slice();copy[0]=first.min+(first.max-first.min)*j/(n-1);let val=computeModel(id,copy);yy.push(val)}let lo=Math.min(...yy),hi=Math.max(...yy);if(Math.abs(hi-lo)<1e-9){lo-=1;hi+=1}const points=yy.map((v,j)=>`${50+j*625/(n-1)},${220-(v-lo)/(hi-lo)*165}`.replace(/^#/, "")).join(' ');
graph.innerHTML=`<line x1="50" y1="220" x2="680" y2="220" stroke="#8093ad"/><line x1="50" y1="45" x2="50" y2="220" stroke="#8093ad"/><polyline points="${points}" fill="none" stroke="#75d5bc" stroke-width="4" stroke-linejoin="round"/><text x="52" y="29" fill="#b9c9db" font-size="16">${fmt(hi)} ${m.unit}</text><text x="52" y="248" fill="#b9c9db" font-size="16">${fmt(lo)}</text><text x="460" y="275" fill="#b9c9db" font-size="15">${m.inputs[0].label}: ${fmt(first.min)}–${fmt(first.max)}</text>`;
}
m.inputs.forEach((p,i)=>{const box=document.createElement('div');box.className='control';const label=document.createElement('label');label.textContent=p.label;label.htmlFor=`param-${i}`;const v=document.createElement('strong');v.id=`value-${i}`;const slider=document.createElement('input');slider.type='range';slider.id=`param-${i}`;slider.min=p.min;slider.max=p.max;slider.step=p.step;slider.value=p.default;slider.setAttribute('aria-label',p.label);slider.addEventListener('input',render);box.append(label,v,slider);root.append(box);xs.push(slider)});render();
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
