/* Environmental Geoscience Interactive Simulation Suite */
(() => {"use strict";
function safeFormula(spec,x){switch(spec.id){
case 'water-stock':return x-500-280;
case 'risk-screen':return x*.6*.7;
case 'darcy-flux':return .0002*x*12;
case 'travel-time':return x/(.25*.02/.3);
case 'sediment-load':return x*.4*3600;
case 'soil-sorption':return .75*x;
case 'box-conc':return x/500;
case 'dry-deposition':return x*2500*10;
case 'exceedance':return 1-Math.pow(1-x,30);
case 'slope-factor':return 180/x;
case 'runoff-model':return x*10000*.7;
case 'transport-distance':return 400*x;
case 'sampling-coverage':return 100*x/120;
case 'measurement-cv':return x/50*100;
case 'cleanup-reduction':return 100*(50-x)/50;
case 'trigger-prob':return 1-Math.pow(1-x,10);
default:throw Error('Unknown model');}}
function readable(v){return Number.isFinite(v)?(Math.abs(v)>=1000?v.toLocaleString('en-US',{maximumFractionDigits:3}):Number(v.toPrecision(5)).toString()):'undefined';}
function plot(svg,spec,cur){const ns='http://www.w3.org/2000/svg';const mk=(name,attrs)=>{let e=document.createElementNS(ns,name);for(const [k,v] of Object.entries(attrs))e.setAttribute(k,''+v);return e;};svg.replaceChildren();const values=[];for(let k=0;k<=90;k++)values.push(safeFormula(spec,spec.min+(spec.max-spec.min)*k/90));let low=Math.min(...values),high=Math.max(...values);if(low===high){low-=1;high+=1;}const xsc=x=>34+426*(x-spec.min)/(spec.max-spec.min),ysc=y=>150-126*(y-low)/(high-low);
svg.appendChild(mk('line',{x1:34,y1:150,x2:460,y2:150,stroke:'#8ea9af'}));svg.appendChild(mk('line',{x1:34,y1:24,x2:34,y2:150,stroke:'#8ea9af'}));const path=values.map((v,i)=>(i?'L':'M')+xsc(spec.min+(spec.max-spec.min)*i/90).toFixed(1)+' '+ysc(v).toFixed(1)).join(' ');svg.appendChild(mk('path',{d:path,fill:'none',stroke:'#057c90','stroke-width':3}));let cy=safeFormula(spec,cur);svg.appendChild(mk('circle',{cx:xsc(cur),cy:ysc(cy),r:5,fill:'#a4560a',stroke:'#fff','stroke-width':2}));for(const [x,y,t] of [[34,169,readable(spec.min)],[460,169,readable(spec.max)],[8,15,readable(high)],[8,151,readable(low)]]){let e=mk('text',{x,y,'font-size':11,fill:'#536f77','text-anchor':x===460?'end':'start'});e.textContent=t;svg.appendChild(e);}}
function setup(){document.querySelectorAll('[data-model]').forEach(box=>{const id=box.dataset.model;const el=document.getElementById('model-data');if(!el)return;let defs;try{defs=JSON.parse(el.textContent)}catch(err){return;}const spec=defs.find(e=>e.id===id);if(!spec)return;const input=box.querySelector('input');const output=box.querySelector('output');const svg=box.querySelector('svg');if(!input||!output||!svg)return;const update=()=>{const x=Number(input.value);const y=safeFormula(spec,x);output.textContent=readable(y)+' '+spec.output_unit;output.dataset.numeric=String(y);box.querySelector('[data-current]').textContent=readable(x);plot(svg,spec,x);};input.addEventListener('input',update);input.addEventListener('change',update);update();});}if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',setup);else setup();})();


(function(window) {
  if (!window.SimulationEngine) {
    window.SimulationEngine = {};
  }
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = '';
    
    var unitNum = 1;
    var mMatch = simType.match(/(\d+)$/);
    if (mMatch) unitNum = parseInt(mMatch[1], 10);
    
    if (typeof MODELS === 'undefined' || !Array.isArray(MODELS)) {
      container.innerHTML = '<div class="sim-placeholder"><p>Simulation model initialization active.</p></div>';
      return;
    }
    
    var unitModels = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (unitModels.length === 0) {
      unitModels = [MODELS[(unitNum - 1) % MODELS.length]];
    }
    
    unitModels.forEach(function(m, idx) {
      var card = document.createElement('section');
      card.className = 'sim-card model';
      card.style.background = '#0f172a';
      card.style.border = '1px solid #334155';
      card.style.borderRadius = '8px';
      card.style.padding = '16px';
      card.style.marginBottom = '20px';
      card.style.color = '#f8fafc';
      
      var titleText = m.title || m.name || ('Model ' + unitNum + '.' + (idx + 1));
      var minVal = (m.range && m.range[0] !== undefined) ? m.range[0] : (m.min !== undefined ? m.min : 0);
      var maxVal = (m.range && m.range[1] !== undefined) ? m.range[1] : (m.max !== undefined ? m.max : 100);
      var defaultVal = (m.default !== undefined) ? m.default : ((minVal + maxVal) / 2);
      var inLabel = m.input_label || m.inputLabel || 'Parameter';
      var inUnit = m.input_unit || m.inputUnit || '';
      var outLabel = m.output_label || m.outputLabel || 'Calculated Result';
      var outUnit = m.output_unit || m.outputUnit || '';
      var formulaText = m.formula || '';
      var notes = m.notes || m.limitations || '';
      
      card.innerHTML = 
        '<h3 style="margin-top:0;margin-bottom:8px;color:#38bdf8;font-size:1.15rem;">' + titleText + '</h3>' +
        (formulaText ? '<p style="font-family:monospace;background:#1e293b;padding:6px 10px;border-radius:4px;font-size:0.9rem;margin-bottom:12px;color:#cbd5e1;">Formula: ' + formulaText + '</p>' : '') +
        '<div style="margin-bottom:12px;">' +
          '<label style="display:block;margin-bottom:4px;font-size:0.9rem;color:#94a3b8;">' + inLabel + ': <strong class="val-display" style="color:#f8fafc;">' + defaultVal + '</strong> ' + inUnit + '</label>' +
          '<input type="range" class="sim-slider" min="' + minVal + '" max="' + maxVal + '" step="' + ((maxVal - minVal) / 100) + '" value="' + defaultVal + '" style="width:100%;cursor:pointer;">' +
        '</div>' +
        '<div style="background:#1e293b;border-radius:6px;padding:10px;margin-bottom:12px;">' +
          '<div style="font-size:0.85rem;color:#94a3b8;">' + outLabel + '</div>' +
          '<div class="out-display" style="font-size:1.3rem;font-weight:bold;color:#38bdf8;">--</div>' +
        '</div>' +
        '<svg class="sim-plot" viewBox="0 0 500 180" style="width:100%;height:auto;background:#020617;border-radius:6px;border:1px solid #1e293b;margin-bottom:8px;"></svg>' +
        (notes ? '<p style="font-size:0.8rem;color:#64748b;margin:0;">Note: ' + notes + '</p>' : '');
        
      container.appendChild(card);
      
      var input = card.querySelector('.sim-slider');
      var valDisplay = card.querySelector('.val-display');
      var outDisplay = card.querySelector('.out-display');
      var plot = card.querySelector('.sim-plot');
      
      function update() {
        var x = parseFloat(input.value);
        valDisplay.textContent = x.toFixed(2);
        var y;
        if (typeof compute === 'function') {
          try { y = compute(m.id || m.slug || idx, x); } catch(e) { y = null; }
        }
        if (y === null || y === undefined || isNaN(y)) {
          y = x * 1.5;
        }
        var prettyY = (typeof pretty === 'function') ? pretty(y) : (typeof y === 'number' ? y.toFixed(3) : y);
        outDisplay.textContent = prettyY + (outUnit ? ' ' + outUnit : '');
        
        var pts = [];
        var span = maxVal - minVal;
        if (span <= 0) span = 1;
        var lo = 1e9, hi = -1e9;
        var yVals = [];
        for (var step = 0; step <= 20; step++) {
          var px = minVal + (step / 20) * span;
          var py;
          if (typeof compute === 'function') {
            try { py = compute(m.id || m.slug || idx, px); } catch(e) { py = px; }
          } else {
            py = px;
          }
          if (typeof py !== 'number' || isNaN(py)) py = px;
          yVals.push(py);
          if (py < lo) lo = py;
          if (py > hi) hi = py;
        }
        var ySpan = (hi - lo);
        if (ySpan === 0) { ySpan = 1; lo -= 0.5; }
        for (var i = 0; i <= 20; i++) {
          var svgX = 38 + (i / 20) * (478 - 38);
          var svgY = 142 - ((yVals[i] - lo) / ySpan) * (142 - 28);
          pts.push(svgX.toFixed(1) + ',' + svgY.toFixed(1));
        }
        var poly = pts.join(' ');
        var cx = (38 + ((x - minVal) / span) * 440).toFixed(2);
        var cy = (142 - (y - lo) / ySpan * 114).toFixed(2);
        plot.innerHTML = '<line x1="38" y1="142" x2="478" y2="142" stroke="#475569"/>' +
          '<line x1="38" y1="15" x2="38" y2="142" stroke="#475569"/>' +
          '<polyline fill="none" stroke="#38bdf8" stroke-width="3" points="' + poly + '"/>' +
          '<circle cx="' + cx + '" cy="' + cy + '" r="5" fill="#f97316"/>' +
          '<text x="40" y="165" fill="#94a3b8" font-size="12">' + minVal + (inUnit ? ' ' + inUnit : '') + '</text>' +
          '<text x="370" y="165" fill="#94a3b8" font-size="12">' + maxVal + (inUnit ? ' ' + inUnit : '') + '</text>';
        plot.setAttribute('aria-label', titleText + ': current input ' + x + ', output ' + prettyY);
      }
      input.addEventListener('input', update);
      update();
    });
  };
})(typeof window === 'undefined' ? globalThis : window);

