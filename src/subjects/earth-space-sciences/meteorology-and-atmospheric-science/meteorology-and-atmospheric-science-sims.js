/* Meteorology and Atmospheric Science Interactive Simulation Suite */
"use strict";
// OpenSTEM meteorology, offline reactive teaching plots. No external network or eval.
window.METEO_MODELS=(function(){
 const fn={
  density: x => (100000/(287*x)),
  hypsometric: x => (287*x/9.81*Math.log(1000/850)),
  shortwave: x => (640*(1-x)),
  longwave: x => (5.670374419e-8*x**4),
  humidity: x => (100*x/30),
  lcl: x => (125*x),
  geostrophic: x => (x/(1.2*1e-4)),
  rossby: x => (10/(1e-4*x*1000)),
  frontspeed: x => (x*1000/(12*3600)),
  thickness: x => (287*x/9.81*Math.log(1000/500)),
  cape: x => (Math.sqrt(2*x)),
  rain: x => (x*2.5),
  radarrange: x => (2*x*1000/3e8*1e6),
  brier: x => ((x-1)**2),
  chance: x => (100*(1-0.99**x)),
  risk: x => (x*100+(1-x)*20)
 };
 function calculate(id,x){ if(!Object.prototype.hasOwnProperty.call(fn,id))throw new Error('Unknown model '+id);return fn[id](x);}
 function draw(card){
   const data=JSON.parse(card.getAttribute('data-model-json'));
   const input=card.querySelector('input');const x=Number(input.value);const y=calculate(data.id,x);
   const num=v=>Number(v).toLocaleString('en-US',{maximumFractionDigits:3});
   card.querySelector('.live-value').textContent=num(x);
   card.querySelector('output').textContent='Illustrative result: '+num(y)+' '+data.units;
   const svg=card.querySelector('svg');const ns='http://www.w3.org/2000/svg';while(svg.firstChild)svg.removeChild(svg.firstChild);
   const values=Array.from({length:45},(_,i)=>calculate(data.id,data.min+(data.max-data.min)*i/44));
   const yMin=Math.min(...values),yMax=Math.max(...values),dy=(yMax-yMin)||1;
   const path=document.createElementNS(ns,'path');let points='';
   values.forEach((v,i)=>{points+=(i?' L':'M')+(14+230*i/44).toFixed(2)+','+(98-81*(v-yMin)/dy).toFixed(2)});
   path.setAttribute('d',points);path.setAttribute('class','modelline');svg.appendChild(path);
   const dot=document.createElementNS(ns,'circle'); dot.setAttribute('cx',String(14+230*(x-data.min)/(data.max-data.min)));dot.setAttribute('cy',String(98-81*(y-yMin)/dy));dot.setAttribute('r','5');dot.setAttribute('fill','#d76d32');svg.appendChild(dot);
 }
 function boot(){document.querySelectorAll('.model').forEach(card=>{const inp=card.querySelector('input');inp.addEventListener('input',()=>draw(card));draw(card)});}
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();
 return {calculate,boot};
})();


/* SimulationEngine adapter for Earth & Space Sciences */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof MODELS === 'undefined' || typeof compute !== 'function') return;
    host.replaceChildren();
    var match = (simType || '').match(/(\d+)$/);
    var u = match ? parseInt(match[1], 10) : 1;
    var unitModels = MODELS.filter(function(m){ return m.unit === u; });
    if (!unitModels.length) unitModels = [MODELS[0]];
    unitModels.forEach(function(m) {
      var section = document.createElement('section');
      section.className = 'sim-card model';
      section.dataset.model = m.id;
      var titleText = m.name || m.title || m.label || 'Interactive Model';
      var exprText = m.expression || m.formula || '';
      var inUnit = m.input_unit || m.unit || '';
      var outUnit = m.output_unit || m.result_unit || '';
      var minVal = m.min !== undefined ? m.min : 0;
      var maxVal = m.max !== undefined ? m.max : 100;
      var initVal = m.initial !== undefined ? m.initial : (minVal + maxVal)/2;
      var stepVal = m.step || ((maxVal - minVal) / 100) || 1;
      
      section.innerHTML = '<h4>' + titleText + '</h4>' +
        (exprText ? '<p class="formula"><code>' + exprText + '</code></p>' : '') +
        '<label>' + (m.label || 'Input') + (inUnit ? ' (' + inUnit + ')' : '') + ':<br>' +
        '<input type="range" min="' + minVal + '" max="' + maxVal + '" step="' + stepVal + '" value="' + initVal + '">' +
        '</label>' +
        '<p>Output: <output style="color:#38bdf8;font-weight:600;"></output></p>' +
        '<svg viewBox="0 0 500 180" style="width:100%;height:auto;background:#0f172a;border:1px solid #1e293b;border-radius:8px;"></svg>' +
        '<p class="readout">' + (m.note || m.notes || m.description || m.limitations || '') + '</p>';
      host.appendChild(section);
      
      var input = section.querySelector('input');
      var output = section.querySelector('output');
      var plot = section.querySelector('svg');
      
      function update() {
        var x = Number(input.value);
        var y = compute(m.id, x);
        var prettyY = (typeof pretty === 'function') ? pretty(y) : (Number.isFinite(y) ? y.toLocaleString() : 'out of range');
        output.textContent = prettyY + (outUnit ? ' ' + outUnit : '');
        var pts = [];
        var lo = Infinity, hi = -Infinity;
        for (var i = 0; i <= 80; i++) {
          var xx = minVal + (maxVal - minVal) * i / 80;
          var yy = compute(m.id, xx);
          if (!Number.isFinite(yy)) continue;
          pts.push([xx, yy]);
          lo = Math.min(lo, yy);
          hi = Math.max(hi, yy);
        }
        var span = hi - lo || 1;
        var coords = pts.map(function(p){
          return [ (p[0] - minVal) / (maxVal - minVal || 1) * 440 + 38, 142 - (p[1] - lo) / span * 114 ];
        });
        var poly = coords.map(function(c){ return c[0].toFixed(2) + ',' + c[1].toFixed(2); }).join(' ');
        var cx = ((x - minVal) / (maxVal - minVal || 1) * 440 + 38).toFixed(2);
        var cy = (142 - (y - lo) / span * 114).toFixed(2);
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

