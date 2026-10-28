/* internal-combustion-engines Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];
  // Core model mathematics
// OpenSTEM engine models: pure static equations for educational sensitivity analysis.
const specs = [{"id": 1, "name": "Engine swept displacement", "formula": "V_d = (π/4) B² S n / 10⁻³", "unit": "L", "inputs": [{"name": "Bore (mm)", "min": 60, "max": 110, "step": 1, "value": 86}, {"name": "Stroke (mm)", "min": 60, "max": 110, "step": 1, "value": 86}, {"name": "Cylinder count", "min": 1, "max": 8, "step": 1, "value": 4}], "warning": "Treat bore and stroke as measured dimensions, not nominal marketing values."}, {"id": 2, "name": "Shaft brake power", "formula": "P = 2π N T / (60 × 1000)", "unit": "kW", "inputs": [{"name": "Speed (rpm)", "min": 500, "max": 6500, "step": 100, "value": 3000}, {"name": "Torque (N·m)", "min": 10, "max": 350, "step": 5, "value": 200}], "warning": "Assumes steady measured torque at the specified shaft speed."}, {"id": 3, "name": "Air-standard Otto efficiency", "formula": "η = 1 − r^(1−γ)", "unit": "%", "inputs": [{"name": "Compression ratio", "min": 6, "max": 16, "step": 0.5, "value": 10}, {"name": "Heat-capacity ratio γ", "min": 1.2, "max": 1.4, "step": 0.02, "value": 1.35}], "warning": "An ideal constant-γ efficiency, not measured fuel economy."}, {"id": 4, "name": "Air-standard Diesel efficiency", "formula": "η = 1−(ρ^γ−1)/[γ (ρ−1) r^(γ−1)]", "unit": "%", "inputs": [{"name": "Compression ratio", "min": 10, "max": 23, "step": 0.5, "value": 17}, {"name": "Cutoff ratio ρ", "min": 1.2, "max": 3, "step": 0.1, "value": 2}], "warning": "γ is fixed at 1.4; real combustion is not constant-pressure heat addition."}, {"id": 5, "name": "Stoichiometric oxygen molecules", "formula": "ν_O₂ = x + y/4 for CₓHᵧ", "unit": "mol O₂ / mol fuel", "inputs": [{"name": "Carbon atoms x", "min": 1, "max": 16, "step": 1, "value": 8}, {"name": "Hydrogen atoms y", "min": 2, "max": 34, "step": 2, "value": 18}], "warning": "For a pure hydrocarbon without oxygen already bound in the fuel."}, {"id": 6, "name": "Relative air–fuel ratio", "formula": "λ = AFR_actual / AFR_stoich", "unit": "—", "inputs": [{"name": "Actual AFR", "min": 8, "max": 25, "step": 0.5, "value": 16.17}, {"name": "Stoichiometric AFR", "min": 9, "max": 18, "step": 0.1, "value": 14.7}], "warning": "Both AFR inputs must use the same air/fuel mass convention."}, {"id": 7, "name": "Compressor exit temperature", "formula": "T₂ = T₁ [1 + (PR^a−1)/ηc]", "unit": "K", "inputs": [{"name": "Inlet temperature (K)", "min": 270, "max": 340, "step": 5, "value": 300}, {"name": "Absolute pressure ratio", "min": 1.1, "max": 3, "step": 0.1, "value": 2}, {"name": "Compressor efficiency", "min": 0.5, "max": 0.9, "step": 0.05, "value": 0.75}], "warning": "Fixed γ=1.4 and adiabatic efficiency; does not assess compressor surge or choke."}, {"id": 8, "name": "Intercooler temperature effectiveness", "formula": "ε = (T_hot,in−T_hot,out)/(T_hot,in−T_cold,in)", "unit": "%", "inputs": [{"name": "Hot inlet T (K)", "min": 350, "max": 450, "step": 5, "value": 400}, {"name": "Hot outlet T (K)", "min": 310, "max": 345, "step": 5, "value": 330}, {"name": "Cold-side inlet T (K)", "min": 270, "max": 305, "step": 5, "value": 300}], "warning": "Requires hot inlet T > cold inlet T; physically meaningful only if outlet lies between them."}, {"id": 9, "name": "Fuel mass per engine cycle", "formula": "m_f = m_air / AFR × 10⁶", "unit": "mg / cycle", "inputs": [{"name": "Trapped air (g/cycle)", "min": 0.2, "max": 0.9, "step": 0.05, "value": 0.5}, {"name": "Target AFR", "min": 10, "max": 20, "step": 0.5, "value": 14.7}], "warning": "This is a fuel mass target; injector latency and wall films are excluded."}, {"id": 10, "name": "First-order transient completion", "formula": "f(t)=100(1−exp(−t/τ))", "unit": "%", "inputs": [{"name": "Time (s)", "min": 0.02, "max": 1, "step": 0.02, "value": 0.1}, {"name": "Time constant (s)", "min": 0.1, "max": 1, "step": 0.05, "value": 0.2}], "warning": "A generic first-order response, not a calibrated engine fuel-film model."}, {"id": 11, "name": "Coolant heat rejection", "formula": "Q = ṁ cₚ ΔT", "unit": "kW", "inputs": [{"name": "Coolant flow (kg/s)", "min": 0.1, "max": 1, "step": 0.05, "value": 0.5}, {"name": "Temperature rise (K)", "min": 2, "max": 20, "step": 1, "value": 8}], "warning": "Fixed water cp=4.18 kJ/(kg·K); transient storage is neglected."}, {"id": 12, "name": "Friction mean effective pressure", "formula": "FMEP = IMEP−BMEP", "unit": "bar", "inputs": [{"name": "Indicated MEP (bar)", "min": 6, "max": 22, "step": 0.5, "value": 12}, {"name": "Brake MEP (bar)", "min": 3, "max": 14, "step": 0.5, "value": 9.5}], "warning": "Both mean effective pressures must use consistent cycle and displacement definitions."}, {"id": 13, "name": "Mass emissions per brake work", "formula": "Intensity = pollutant flow / brake power", "unit": "g/kWh", "inputs": [{"name": "Emission flow (g/h)", "min": 2, "max": 40, "step": 1, "value": 20}, {"name": "Brake output (kW)", "min": 10, "max": 90, "step": 2, "value": 50}], "warning": "A teaching normalization only. Regulatory measurement may require specific procedures."}, {"id": 14, "name": "Aftertreatment conversion", "formula": "η = 100 (1 − m_out/m_in)", "unit": "%", "inputs": [{"name": "Upstream mass (g/h)", "min": 20, "max": 100, "step": 5, "value": 80}, {"name": "Downstream mass (g/h)", "min": 1, "max": 18, "step": 1, "value": 12}], "warning": "Use same analyte, flow basis and test window; does not establish certification."}, {"id": 15, "name": "Combined heat and power utilization", "formula": "U=100 (P_e+Q_useful)/E_fuel", "unit": "%", "inputs": [{"name": "Electrical power (kW)", "min": 10, "max": 45, "step": 1, "value": 32}, {"name": "Useful heat (kW)", "min": 10, "max": 50, "step": 1, "value": 40}, {"name": "Fuel energy rate (kW)", "min": 85, "max": 150, "step": 5, "value": 100}], "warning": "Reject values above 100% as an inconsistent input or boundary; count only genuinely useful heat."}, {"id": 16, "name": "Annual chemical fuel demand", "formula": "E_fuel = E_shaft / η", "unit": "MWh/year", "inputs": [{"name": "Shaft energy demand (MWh/year)", "min": 20, "max": 200, "step": 5, "value": 100}, {"name": "Average brake efficiency", "min": 0.2, "max": 0.5, "step": 0.02, "value": 0.3}], "warning": "Use representative average efficiency over the duty cycle, not peak efficiency."}];
function computeModel(id,p){switch(Number(id)){
case 1:return Math.PI/4*(p[0]/1000)**2*(p[1]/1000)*(p[2])*1000;
case 2:return 2*Math.PI*p[0]*p[1]/60000;
case 3:return 100*(1-Math.pow(p[0],1-p[1]));
case 4:return 100*(1-(Math.pow(p[1],1.4)-1)/(1.4*(p[1]-1)*Math.pow(p[0],.4)));
case 5:return p[0]+p[1]/4;
case 6:return p[0]/p[1];
case 7:return p[0]*(1+(Math.pow(p[1],(1.4-1)/1.4)-1)/p[2]);
case 8:return 100*(p[0]-p[1])/(p[0]-p[2]);
case 9:return 1000*p[0]/p[1];
case 10:return 100*(1-Math.exp(-p[0]/p[1]));
case 11:return p[0]*4.18*p[1];
case 12:return p[0]-p[1];
case 13:return p[0]/p[1];
case 14:return 100*(1-p[1]/p[0]);
case 15:return 100*(p[0]+p[1])/p[2];
case 16:return p[0]/p[1];
default:throw new Error("Unknown model");
}}
if(typeof module!=="undefined")module.exports={specs,computeModel};
if(typeof window!=="undefined")window.OpenSTEMModels={specs,computeModel};


  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 01/16</span><h3>Engine swept displacement</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">V_d = (\u03c0/4) B\u00b2 S n / 10\u207b\u00b3</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">Treat bore and stroke as measured dimensions, not nominal marketing values.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 1;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 1,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 02/16</span><h3>Shaft brake power</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">P = 2\u03c0 N T / (60 \u00d7 1000)</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">Assumes steady measured torque at the specified shaft speed.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 2;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 2,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 03/16</span><h3>Air-standard Otto efficiency</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">\u03b7 = 1 \u2212 r^(1\u2212\u03b3)</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">An ideal constant-\u03b3 efficiency, not measured fuel economy.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 3;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 2,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 04/16</span><h3>Air-standard Diesel efficiency</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">\u03b7 = 1\u2212(\u03c1^\u03b3\u22121)/[\u03b3 (\u03c1\u22121) r^(\u03b3\u22121)]</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">\u03b3 is fixed at 1.4; real combustion is not constant-pressure heat addition.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 4;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 3,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 05/16</span><h3>Stoichiometric oxygen molecules</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">\u03bd_O\u2082 = x + y/4 for C\u2093H\u1d67</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">For a pure hydrocarbon without oxygen already bound in the fuel.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 5;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 3,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 06/16</span><h3>Relative air\u2013fuel ratio</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">\u03bb = AFR_actual / AFR_stoich</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">Both AFR inputs must use the same air/fuel mass convention.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 6;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 4,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 07/16</span><h3>Compressor exit temperature</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">T\u2082 = T\u2081 [1 + (PR^a\u22121)/\u03b7c]</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">Fixed \u03b3=1.4 and adiabatic efficiency; does not assess compressor surge or choke.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 7;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 4,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 08/16</span><h3>Intercooler temperature effectiveness</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">\u03b5 = (T_hot,in\u2212T_hot,out)/(T_hot,in\u2212T_cold,in)</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">Requires hot inlet T &gt; cold inlet T; physically meaningful only if outlet lies between them.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 8;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 9,
    unit: 5,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 09/16</span><h3>Fuel mass per engine cycle</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">m_f = m_air / AFR \u00d7 10\u2076</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">This is a fuel mass target; injector latency and wall films are excluded.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 9;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 10,
    unit: 5,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 10/16</span><h3>First-order transient completion</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">f(t)=100(1\u2212exp(\u2212t/\u03c4))</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">A generic first-order response, not a calibrated engine fuel-film model.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 10;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 11,
    unit: 6,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 11/16</span><h3>Coolant heat rejection</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">Q = m\u0307 c\u209a \u0394T</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">Fixed water cp=4.18 kJ/(kg\u00b7K); transient storage is neglected.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 11;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 12,
    unit: 6,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 12/16</span><h3>Friction mean effective pressure</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">FMEP = IMEP\u2212BMEP</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">Both mean effective pressures must use consistent cycle and displacement definitions.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 12;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 13,
    unit: 7,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 13/16</span><h3>Mass emissions per brake work</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">Intensity = pollutant flow / brake power</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">A teaching normalization only. Regulatory measurement may require specific procedures.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 13;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 14,
    unit: 7,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 14/16</span><h3>Aftertreatment conversion</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">\u03b7 = 100 (1 \u2212 m_out/m_in)</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">Use same analyte, flow basis and test window; does not establish certification.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 14;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 15,
    unit: 8,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 15/16</span><h3>Combined heat and power utilization</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">U=100 (P_e+Q_useful)/E_fuel</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">Reject values above 100% as an inconsistent input or boundary; count only genuinely useful heat.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 15;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 16,
    unit: 8,
    html: "<header class=\"hero\"><span class=\"badge\">INTERACTIVE TEACHING MODEL 16/16</span><h3>Annual chemical fuel demand</h3><p class=\"subtitle\">Modify values to see a directly calculated sensitivity result. Fully offline, no data sent anywhere.</p></header><div class=\"notice\">Illustrative idealized calculation, not a measured performance figure or certified safety/emissions prediction.</div><section class=\"panel\"><h2>Parameters</h2><div id=\"controls\" class=\"controls\"></div><h2>Calculated output</h2><div id=\"output\" class=\"modelout\" aria-live=\"polite\">\u2014</div><p class=\"formula\">E_fuel = E_shaft / \u03b7</p><p id=\"model-status\" class=\"status\" aria-live=\"polite\">Use representative average efficiency over the duty cycle, not peak efficiency.</p></section><section><h2>Sensitivity to the first parameter</h2><svg id=\"plot\" viewBox=\"0 0 740 290\" role=\"img\" aria-label=\"Calculated output along the first input range\"></svg><p class=\"caption\">Other sliders remain at their current positions. The curve is an equation plot, not experimental data.</p></section>",
    init: function(card) {
      try {
        var host = card;
        var id = 16;
        var specs = window.OpenSTEMModels.specs;
        var computeModel = window.OpenSTEMModels.computeModel;
        var model = specs.find(function(item) { return item.id === id; });
        if (!model) return;
        var controls = card.querySelector('#controls');
        var output = card.querySelector('#output');
        var status = card.querySelector('#model-status');
        var plot = card.querySelector('#plot');
        var state = model.inputs.map(function(p) { return p.value; });

        controls.innerHTML = '';
        model.inputs.forEach(function(q, i) {
          var label = document.createElement('label');
          label.className = 'slider';
          var s = document.createElement('span');
          s.textContent = q.name + ': ';
          var val = document.createElement('output');
          val.id = 'param-' + i;
          val.style.marginLeft = '8px';
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = q.min;
          inp.max = q.max;
          inp.step = q.step;
          inp.value = q.value;
          inp.setAttribute('aria-label', q.name);
          inp.addEventListener('input', function() {
            state[i] = Number(inp.value);
            update();
          });
          label.append(s, inp, val);
          controls.append(label);
        });

        function safeCompute(x) {
          try {
            var r = computeModel(id, x);
            return Number.isFinite(r) ? r : null;
          } catch(e) {
            return null;
          }
        }

        function update() {
          var y = safeCompute(state);
          var vals = controls.querySelectorAll('output');
          vals.forEach(function(v, i) {
            v.textContent = Number(state[i]).toLocaleString(undefined, { maximumFractionDigits: 3 });
          });
          var extra = [];
          if (id === 8 && (state[0] <= state[2] || state[1] > state[0] || state[1] < state[2])) extra.push('Temperatures outside the physically meaningful ordering.');
          if (id === 12 && y < 0) extra.push('Negative estimated friction: check the inconsistent input states.');
          if (id === 15 && y > 100) extra.push('Utilization above 100%: inputs violate the stated energy boundary.');
          if (id === 4 && state[1] >= state[0]) extra.push('Cutoff ratio cannot reach or exceed compression ratio in this model.');
          output.textContent = (y === null) ? 'Undefined for current inputs' : (y.toLocaleString(undefined, { maximumFractionDigits: 4 }) + ' ' + model.unit);
          if (status) status.textContent = extra.length ? extra.join(' ') : model.warning;
          var first = model.inputs[0];
          var xy = [];
          for (var z = 0; z <= 50; z++) {
            var x = first.min + (first.max - first.min) * z / 50;
            var p = state.slice();
            p[0] = x;
            var v = safeCompute(p);
            if (v !== null) xy.push([x, v]);
          }
          if (xy.length < 2) return;
          var minY = Math.min.apply(null, xy.map(function(a) { return a[1]; }));
          var maxY = Math.max.apply(null, xy.map(function(a) { return a[1]; }));
          var ymin = minY - Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var ymax = maxY + Math.max(0.001, Math.abs(maxY - minY) * 0.15);
          var sx = function(x) { return 70 + ((x - first.min) / (first.max - first.min)) * 600; };
          var sy = function(yVal) { return 245 - ((yVal - ymin) / (ymax - ymin)) * 190; };
          var path = xy.map(function(a, i) {
            return (i ? 'L' : 'M') + sx(a[0]).toFixed(2) + ' ' + sy(a[1]).toFixed(2);
          }).join(' ');
          var doty = Math.min(245, Math.max(55, sy(y !== null ? y : minY)));
          plot.innerHTML = '<rect x="70" y="54" width="600" height="191" rx="8" fill="#0b1d2d"/>' +
            '<path d="M70 54V245H670" stroke="#748fa2" fill="none" stroke-width="2"/>' +
            '<path d="' + path + '" fill="none" stroke="#74d8c3" stroke-width="3"/>' +
            '<circle cx="' + sx(state[0]).toFixed(2) + '" cy="' + doty.toFixed(2) + '" r="6" fill="#e0ad6e"/>' +
            '<text x="70" y="273" fill="#d8e9ee" font-size="13">' + first.min + '</text>' +
            '<text x="650" y="273" fill="#d8e9ee" font-size="13">' + first.max + '</text>' +
            '<text x="70" y="32" fill="#d8e9ee" font-size="14">' + model.unit + ' · varies ' + first.name + '</text>';
        }
        update();
      } catch(err) {
        console.warn('ICE Sim init error:', err);
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
