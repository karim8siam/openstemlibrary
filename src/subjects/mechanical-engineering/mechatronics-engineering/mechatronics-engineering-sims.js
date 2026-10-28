/* mechatronics-engineering Interactive Simulation Suite */
(function(window) {
  'use strict';

  var OPENSTEM_SIM_MODELS = [];

  // Core models logic
  (function() {
"use strict";
const models = [{"id": 1, "title": "Arrival time for a sorting gate", "description": "Compute travel time before an object reaches a diverter. Set a safety margin outside this ideal model.", "x": {"name": "distance", "unit": "m", "min": 0.1, "max": 2.0, "step": 0.05, "default": 0.6}, "z": {"name": "belt speed", "unit": "m/s", "min": 0.1, "max": 2.0, "step": 0.05, "default": 0.75}, "expression": "d/v", "result_unit": "s", "warning": "A fixed distance model omits detection and actuator delays.", "formula_js": "p1/p2"}, {"id": 2, "title": "Shaft mechanical power", "description": "Estimate useful shaft power from torque and rotational speed; motor input power is larger when losses are present.", "x": {"name": "torque", "unit": "N m", "min": 0.1, "max": 5, "step": 0.1, "default": 0.5}, "z": {"name": "speed", "unit": "rad/s", "min": 1, "max": 100, "step": 1, "default": 40}, "expression": "tau*omega", "result_unit": "W", "warning": "Allow for friction, efficiency and motor duty cycle.", "formula_js": "p1*p2"}, {"id": 3, "title": "Encoder angular resolution", "description": "Compare angular resolution against encoder lines and decoding edges; do not treat count resolution as accuracy.", "x": {"name": "cycles/rev", "unit": "cycles", "min": 128, "max": 8192, "step": 128, "default": 2048}, "z": {"name": "decoded edges/cycle", "unit": "factor", "min": 1, "max": 4, "step": 1, "default": 4}, "expression": "360/(cycles*edges)", "result_unit": "deg/count", "warning": "Quadrature decoding, backlash and homing conventions matter.", "formula_js": "360/(p1*p2)"}, {"id": 4, "title": "Aliasing of a sampled sinusoid", "description": "Observe how a frequency beyond the Nyquist boundary folds into the measurement spectrum.", "x": {"name": "input frequency", "unit": "Hz", "min": 0, "max": 500, "step": 5, "default": 150}, "z": {"name": "sample rate", "unit": "Hz", "min": 50, "max": 400, "step": 10, "default": 200}, "expression": "abs(f-round(f/fs)fs)", "result_unit": "Hz", "warning": "Use an analog anti-alias filter, not a digital fix after sampling.", "formula_js": "Math.abs(p1-Math.round(p1/p2)*p2)"}, {"id": 5, "title": "DC motor electromagnetic torque", "description": "See the proportional relation of torque constant and armature current, not a continuous rating.", "x": {"name": "current", "unit": "A", "min": 0, "max": 10, "step": 0.2, "default": 3}, "z": {"name": "torque constant", "unit": "N m/A", "min": 0.01, "max": 0.25, "step": 0.005, "default": 0.08}, "expression": "Kt*I", "result_unit": "N m", "warning": "Current limits and thermal rise can reduce available sustained torque.", "formula_js": "p1*p2"}, {"id": 6, "title": "PWM ideal average voltage", "description": "A duty-ratio approximation for bus voltage, excluding semiconductor drops and motor dynamics.", "x": {"name": "duty", "unit": "fraction", "min": 0, "max": 1, "step": 0.025, "default": 0.35}, "z": {"name": "bus voltage", "unit": "V", "min": 5, "max": 48, "step": 1, "default": 24}, "expression": "D*V", "result_unit": "V", "warning": "Do not mistake average voltage for instantaneous winding current.", "formula_js": "p1*p2"}, {"id": 7, "title": "Periodic CPU utilization", "description": "Evaluate a simplified two-task utilization sum; it does not itself prove deadline feasibility.", "x": {"name": "task A execution", "unit": "ms", "min": 0.1, "max": 3, "step": 0.1, "default": 1}, "z": {"name": "task B execution", "unit": "ms", "min": 0.1, "max": 3, "step": 0.1, "default": 2}, "expression": "C1/5+C2/10", "result_unit": "fraction", "warning": "Priority inversion, interrupt latency and blocked tasks are excluded.", "formula_js": "p1/5+p2/10"}, {"id": 8, "title": "ADC nominal voltage step", "description": "Compare ideal quantization steps for a converter with a configurable reference and resolution.", "x": {"name": "ADC bits", "unit": "bits", "min": 8, "max": 16, "step": 1, "default": 12}, "z": {"name": "reference", "unit": "V", "min": 1, "max": 5, "step": 0.1, "default": 3.3}, "expression": "Vref/2^n", "result_unit": "V/LSB", "warning": "Effective resolution includes noise, reference drift and calibration.", "formula_js": "p2/Math.pow(2,p1)"}, {"id": 9, "title": "First-order step response", "description": "Inspect a first-order step response at one time; model gain and initial conditions are idealized.", "x": {"name": "time", "unit": "s", "min": 0, "max": 2, "step": 0.05, "default": 0.2}, "z": {"name": "time constant", "unit": "s", "min": 0.05, "max": 1, "step": 0.05, "default": 0.2}, "expression": "3(1-exp(-t/tau))", "result_unit": "output units", "warning": "Real actuators saturate and often have additional dynamic modes.", "formula_js": "3*(1-Math.exp(-p1/p2))"}, {"id": 10, "title": "Discrete-time decay multiplier", "description": "Explore explicit Euler stability for dx/dt=-a x; magnitude below 1 is required for asymptotic stability.", "x": {"name": "time step", "unit": "s", "min": 0.002, "max": 0.25, "step": 0.002, "default": 0.02}, "z": {"name": "decay rate", "unit": "1/s", "min": 5, "max": 50, "step": 1, "default": 20}, "expression": "abs(1-a dt)", "result_unit": "abs(multiplier)", "warning": "Magnitude >=1 indicates failure of the stability criterion.", "formula_js": "Math.abs(1-p1*p2)"}, {"id": 11, "title": "Two-link robot X coordinate", "description": "Check forward kinematics for links 0.30 and 0.20 m. Angles entered in degrees, trigonometry in radians.", "x": {"name": "joint 1 angle", "unit": "deg", "min": -180, "max": 180, "step": 5, "default": 0}, "z": {"name": "joint 2 angle", "unit": "deg", "min": -180, "max": 180, "step": 5, "default": 90}, "expression": "L1 cos(q1)+L2 cos(q1+q2)", "result_unit": "m", "warning": "This graph does not check joint stops, collisions or motor torques.", "formula_js": "0.30*Math.cos(p1*Math.PI/180)+0.20*Math.cos((p1+p2)*Math.PI/180)"}, {"id": 12, "title": "Ideal braking distance", "description": "Lower-bound stopping travel under constant deceleration; add controller delay and stopping-system uncertainty.", "x": {"name": "speed", "unit": "m/s", "min": 0, "max": 3, "step": 0.05, "default": 0.5}, "z": {"name": "deceleration", "unit": "m/s²", "min": 0.2, "max": 6, "step": 0.1, "default": 2}, "expression": "v^2/(2a)", "result_unit": "m", "warning": "Actual stopping includes detection latency and dynamic brake limitations.", "formula_js": "p1*p1/(2*p2)"}, {"id": 13, "title": "Delay-induced phase lag", "description": "The phase shift of an ideal pure time delay at angular frequency omega.", "x": {"name": "angular frequency", "unit": "rad/s", "min": 0, "max": 100, "step": 1, "default": 10}, "z": {"name": "delay", "unit": "ms", "min": 0, "max": 40, "step": 1, "default": 5}, "expression": "omega*delay", "result_unit": "deg", "warning": "Phase gain and loop stability require the full transfer function.", "formula_js": "p1*p2/1000*180/Math.PI"}, {"id": 14, "title": "Constant-hazard reliability illustration", "description": "An exponential reliability curve under an assumed constant hazard rate, not a warranty prediction.", "x": {"name": "operation time", "unit": "h", "min": 0, "max": 1000, "step": 25, "default": 100}, "z": {"name": "hazard rate", "unit": "1/h", "min": 1e-05, "max": 0.001, "step": 1e-05, "default": 0.0001}, "expression": "exp(-lambda t)", "result_unit": "probability", "warning": "Wear-out and nonstationary conditions violate a constant-hazard model.", "formula_js": "Math.exp(-p1*p2)"}, {"id": 15, "title": "Lead-screw ideal travel", "description": "Convert full turns into translation using lead, before including backlash and compliance.", "x": {"name": "rotations", "unit": "rev", "min": -20, "max": 20, "step": 0.25, "default": 3}, "z": {"name": "lead", "unit": "mm/rev", "min": 1, "max": 20, "step": 0.5, "default": 5}, "expression": "N*lead", "result_unit": "mm", "warning": "Actual positioning errors depend on direction, load and temperature.", "formula_js": "p1*p2"}, {"id": 16, "title": "Ideal pump delivered volume", "description": "Calculate total dose for a constant calibrated flow and elapsed time, ignoring leakage and startup transients.", "x": {"name": "time", "unit": "s", "min": 0, "max": 300, "step": 5, "default": 150}, "z": {"name": "flow", "unit": "L/s", "min": 0.0005, "max": 0.02, "step": 0.0005, "default": 0.002}, "expression": "Q*t", "result_unit": "L", "warning": "A command for pump speed is not proof of actual fluid transfer.", "formula_js": "p1*p2"}];
function calculate(m,p1,p2){switch(m.id){
case 1: return p1/p2;
case 2: return p1*p2;
case 3: return 360/(p1*p2);
case 4: return Math.abs(p1-Math.round(p1/p2)*p2);
case 5: return p1*p2;
case 6: return p1*p2;
case 7: return p1/5+p2/10;
case 8: return p2/Math.pow(2,p1);
case 9: return 3*(1-Math.exp(-p1/p2));
case 10: return Math.abs(1-p1*p2);
case 11: return 0.30*Math.cos(p1*Math.PI/180)+0.20*Math.cos((p1+p2)*Math.PI/180);
case 12: return p1*p1/(2*p2);
case 13: return p1*p2/1000*180/Math.PI;
case 14: return Math.exp(-p1*p2);
case 15: return p1*p2;
case 16: return p1*p2;
default: throw new Error("Unknown model")}}
window.OpenSTEMMechatronics = {models,calculate};
function startSimulation(){
 const id=Number(document.querySelector('[data-model]')?.dataset.model);
 if(!id){return;}
 const m=models[id-1]; const p1=document.querySelector('#p1'),p2=document.querySelector('#p2');
 const display=document.querySelector('#answer'); const svg=document.querySelector('#plot');
 const p1v=document.querySelector('#p1value'),p2v=document.querySelector('#p2value');
 [p1,p2].forEach((el,i)=>{const o=i===0?m.x:m.z;el.min=o.min;el.max=o.max;el.step=o.step;el.value=o.default;});
 const precision=(x)=>Number.isFinite(x)?(Math.abs(x)<.0001&&x!==0?x.toExponential(3):x.toLocaleString('en-US',{maximumFractionDigits:5})):"undefined";
 function redraw(){
  const a=Number(p1.value),b=Number(p2.value),res=calculate(m,a,b);
  p1v.textContent=precision(a)+' '+m.x.unit;p2v.textContent=precision(b)+' '+m.z.unit;
  display.textContent=precision(res)+' '+m.result_unit;
  const series=[]; for(let i=0;i<=90;i++){const x=m.x.min+i*(m.x.max-m.x.min)/90;const y=calculate(m,x,b);if(Number.isFinite(y)){series.push([x,y])}}
  let ymin=Math.min(...series.map(p=>p[1])),ymax=Math.max(...series.map(p=>p[1]));
  if(Math.abs(ymax-ymin)<1e-10){ymin-=1;ymax+=1};const margin=(ymax-ymin)*.08;ymin-=margin;ymax+=margin;
  const X=x=>52+650*(x-m.x.min)/(m.x.max-m.x.min), Y=y=>270-235*(y-ymin)/(ymax-ymin);
  svg.innerHTML='';const NS='http://www.w3.org/2000/svg';
  function node(type,props){const el=document.createElementNS(NS,type);for(let k in props)el.setAttribute(k,props[k]);svg.appendChild(el);return el}
  node('line',{x1:52,y1:35,x2:52,y2:270,stroke:'#638ca0','stroke-width':1});
  node('line',{x1:52,y1:270,x2:702,y2:270,stroke:'#638ca0','stroke-width':1});
  node('polyline',{points:series.map(p=>X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' '),stroke:'#80e3bd','stroke-width':3,fill:'none','stroke-linejoin':'round'});
  node('circle',{cx:X(a),cy:Y(res),r:7,fill:'#f2cb85'});
  function text(x,y,s){const el=node('text',{x,y,fill:'#b9d7e4','font-size':13});el.textContent=s;}
  text(55,20,'Output ('+m.result_unit+'): '+precision(ymax));text(55,289,'Min '+precision(m.x.min));text(568,289,'Max '+precision(m.x.max));text(260,317,m.x.name+' ('+m.x.unit+')');
 }
 p1.addEventListener('input',redraw);p2.addEventListener('input',redraw);redraw();
}
document.addEventListener('DOMContentLoaded',startSimulation);

    window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS = models;
    window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC = typeof calculate !== 'undefined' ? calculate : null;
  })();


  OPENSTEM_SIM_MODELS.push({
    idx: 1,
    unit: 1,
    html: "<h3>Interactive Model 01: Arrival time for a sorting gate</h3><p>Compute travel time before an object reaches a diverter. Set a safety margin outside this ideal model.</p><p><strong>Model:</strong> <code>d/v</code></p><div class=\"panel\"><div class=\"controls\"><label>distance <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>belt speed <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>A fixed distance model omits detection and actuator delays. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[0];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 2,
    unit: 1,
    html: "<h3>Interactive Model 02: Shaft mechanical power</h3><p>Estimate useful shaft power from torque and rotational speed; motor input power is larger when losses are present.</p><p><strong>Model:</strong> <code>tau*omega</code></p><div class=\"panel\"><div class=\"controls\"><label>torque <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>speed <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Allow for friction, efficiency and motor duty cycle. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[1];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 3,
    unit: 2,
    html: "<h3>Interactive Model 03: Encoder angular resolution</h3><p>Compare angular resolution against encoder lines and decoding edges; do not treat count resolution as accuracy.</p><p><strong>Model:</strong> <code>360/(cycles*edges)</code></p><div class=\"panel\"><div class=\"controls\"><label>cycles/rev <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>decoded edges/cycle <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Quadrature decoding, backlash and homing conventions matter. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[2];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 4,
    unit: 2,
    html: "<h3>Interactive Model 04: Aliasing of a sampled sinusoid</h3><p>Observe how a frequency beyond the Nyquist boundary folds into the measurement spectrum.</p><p><strong>Model:</strong> <code>abs(f-round(f/fs)fs)</code></p><div class=\"panel\"><div class=\"controls\"><label>input frequency <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>sample rate <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Use an analog anti-alias filter, not a digital fix after sampling. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[3];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 5,
    unit: 3,
    html: "<h3>Interactive Model 05: DC motor electromagnetic torque</h3><p>See the proportional relation of torque constant and armature current, not a continuous rating.</p><p><strong>Model:</strong> <code>Kt*I</code></p><div class=\"panel\"><div class=\"controls\"><label>current <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>torque constant <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Current limits and thermal rise can reduce available sustained torque. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[4];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 6,
    unit: 3,
    html: "<h3>Interactive Model 06: PWM ideal average voltage</h3><p>A duty-ratio approximation for bus voltage, excluding semiconductor drops and motor dynamics.</p><p><strong>Model:</strong> <code>D*V</code></p><div class=\"panel\"><div class=\"controls\"><label>duty <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>bus voltage <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Do not mistake average voltage for instantaneous winding current. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[5];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 7,
    unit: 4,
    html: "<h3>Interactive Model 07: Periodic CPU utilization</h3><p>Evaluate a simplified two-task utilization sum; it does not itself prove deadline feasibility.</p><p><strong>Model:</strong> <code>C1/5+C2/10</code></p><div class=\"panel\"><div class=\"controls\"><label>task A execution <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>task B execution <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Priority inversion, interrupt latency and blocked tasks are excluded. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[6];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 8,
    unit: 4,
    html: "<h3>Interactive Model 08: ADC nominal voltage step</h3><p>Compare ideal quantization steps for a converter with a configurable reference and resolution.</p><p><strong>Model:</strong> <code>Vref/2^n</code></p><div class=\"panel\"><div class=\"controls\"><label>ADC bits <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>reference <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Effective resolution includes noise, reference drift and calibration. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[7];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 9,
    unit: 5,
    html: "<h3>Interactive Model 09: First-order step response</h3><p>Inspect a first-order step response at one time; model gain and initial conditions are idealized.</p><p><strong>Model:</strong> <code>3(1-exp(-t/tau))</code></p><div class=\"panel\"><div class=\"controls\"><label>time <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>time constant <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Real actuators saturate and often have additional dynamic modes. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[8];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 10,
    unit: 5,
    html: "<h3>Interactive Model 10: Discrete-time decay multiplier</h3><p>Explore explicit Euler stability for dx/dt=-a x; magnitude below 1 is required for asymptotic stability.</p><p><strong>Model:</strong> <code>abs(1-a dt)</code></p><div class=\"panel\"><div class=\"controls\"><label>time step <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>decay rate <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Magnitude &gt;=1 indicates failure of the stability criterion. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[9];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 11,
    unit: 6,
    html: "<h3>Interactive Model 11: Two-link robot X coordinate</h3><p>Check forward kinematics for links 0.30 and 0.20 m. Angles entered in degrees, trigonometry in radians.</p><p><strong>Model:</strong> <code>L1 cos(q1)+L2 cos(q1+q2)</code></p><div class=\"panel\"><div class=\"controls\"><label>joint 1 angle <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>joint 2 angle <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>This graph does not check joint stops, collisions or motor torques. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[10];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 12,
    unit: 6,
    html: "<h3>Interactive Model 12: Ideal braking distance</h3><p>Lower-bound stopping travel under constant deceleration; add controller delay and stopping-system uncertainty.</p><p><strong>Model:</strong> <code>v^2/(2a)</code></p><div class=\"panel\"><div class=\"controls\"><label>speed <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>deceleration <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Actual stopping includes detection latency and dynamic brake limitations. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[11];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 13,
    unit: 7,
    html: "<h3>Interactive Model 13: Delay-induced phase lag</h3><p>The phase shift of an ideal pure time delay at angular frequency omega.</p><p><strong>Model:</strong> <code>omega*delay</code></p><div class=\"panel\"><div class=\"controls\"><label>angular frequency <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>delay <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Phase gain and loop stability require the full transfer function. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[12];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 14,
    unit: 7,
    html: "<h3>Interactive Model 14: Constant-hazard reliability illustration</h3><p>An exponential reliability curve under an assumed constant hazard rate, not a warranty prediction.</p><p><strong>Model:</strong> <code>exp(-lambda t)</code></p><div class=\"panel\"><div class=\"controls\"><label>operation time <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>hazard rate <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Wear-out and nonstationary conditions violate a constant-hazard model. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[13];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 15,
    unit: 8,
    html: "<h3>Interactive Model 15: Lead-screw ideal travel</h3><p>Convert full turns into translation using lead, before including backlash and compliance.</p><p><strong>Model:</strong> <code>N*lead</code></p><div class=\"panel\"><div class=\"controls\"><label>rotations <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>lead <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>Actual positioning errors depend on direction, load and temperature. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[14];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 16,
    unit: 8,
    html: "<h3>Interactive Model 16: Ideal pump delivered volume</h3><p>Calculate total dose for a constant calibrated flow and elapsed time, ignoring leakage and startup transients.</p><p><strong>Model:</strong> <code>Q*t</code></p><div class=\"panel\"><div class=\"controls\"><label>time <strong id=\"p1value\"></strong><input id=\"p1\" type=\"range\" style=\"width:100%\" aria-label=\"First model parameter\"></label><label>flow <strong id=\"p2value\"></strong><input id=\"p2\" type=\"range\" style=\"width:100%\" aria-label=\"Second model parameter\"></label></div><p>Predicted output: <span id=\"answer\" class=\"big\" aria-live=\"polite\"></span></p><svg id=\"plot\" viewBox=\"0 0 740 325\" role=\"img\" aria-label=\"Model output versus first parameter\"></svg></div><h2>Interpretation and limitations</h2><p>A command for pump speed is not proof of actual fluid transfer. The curve sweeps only the first input while holding the second at its selected value. This is an educational analytical curve, not measured equipment data.</p><p>Reproduce the calculation independently, vary the second parameter, and identify the operating conditions outside the assumed model. Compare the result with a limiting case before using it as evidence in a design report.</p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_MECHATRONICS_ENGINEERING_MODELS;
        var calcFunc = window.__OPENSTEM_MECHATRONICS_ENGINEERING_CALC;
        var m = models[15];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
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
