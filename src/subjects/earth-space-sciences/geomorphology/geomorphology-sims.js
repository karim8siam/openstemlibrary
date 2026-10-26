/* Geomorphology Interactive Simulation Suite */
"use strict";
window.OpenSTEMModels = (() => {
 const expressions = {
  1: x => (100*x/1500),
  2: x => (x*625),
  3: x => (0.03*x),
  4: x => (0.7-x),
  5: x => (12*1.2*x),
  6: x => (1000*1.5*x/(1650*.02)),
  7: x => (.95-x),
  8: x => (12/x),
  9: x => (Math.pow(Math.max(x-.25,0),3)),
  10: x => (100*160/x),
  11: x => (170000-x),
  12: x => (4.1+x),
  13: x => (.5*x),
  14: x => (18/x*1000),
  15: x => (1.96*Math.sqrt(.2*.2+x*x)),
  16: x => (x/9000)
 };
 const fmt=v=>Number(v).toLocaleString(undefined,{maximumFractionDigits:6});
 function draw(svg,tag,attrs){const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attrs).forEach(([k,v])=>el.setAttribute(k,v));svg.appendChild(el);}
 function update(card){
  const id=Number(card.dataset.model), m=window.OPENSTEM_MODEL_DATA.find(z=>z.id===id), f=expressions[id], input=card.querySelector('input');
  if(!m||!f||!input)throw Error('Missing model '+id);
  const x=Number(input.value), result=f(x);
  if(!Number.isFinite(result))throw Error('Nonfinite model output '+id);
  card.querySelector('.live-value').textContent=fmt(x)+' '+m.input_unit;
  card.querySelector('output').value=fmt(result)+' '+m.output_unit;
  const samples=Array.from({length:65},(_,j)=>f(m.min+(m.max-m.min)*j/64));
  if(samples.some(v=>!Number.isFinite(v)))throw Error('Nonfinite curve '+id);
  const lo=Math.min(...samples),hi=Math.max(...samples),dy=hi-lo||1;
  const pts=samples.map((v,j)=>(j?'L':'M')+(12+3.6*j).toFixed(2)+','+(98-82*(v-lo)/dy).toFixed(2)).join(' ');
  const dotX=12+232*(x-m.min)/(m.max-m.min),dotY=98-82*(result-lo)/dy;
  const svg=card.querySelector('svg');svg.replaceChildren();
  draw(svg,'path',{d:'M12 12V98H244',fill:'none',stroke:'#9bb9bc','stroke-width':1});
  draw(svg,'path',{d:pts,fill:'none',stroke:'#127a82','stroke-width':2.4});
  draw(svg,'circle',{cx:dotX,cy:dotY,r:4.5,fill:'#d0793d',stroke:'#fff','stroke-width':1.2});
 }
 function boot(){document.querySelectorAll('.model').forEach(card=>{const input=card.querySelector('input');input.addEventListener('input',()=>update(card));update(card);})}
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();
 return {calculate:(id,x)=>expressions[id](x),boot};
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

