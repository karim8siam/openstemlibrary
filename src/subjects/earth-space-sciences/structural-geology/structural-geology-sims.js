/* Structural Geology Interactive Simulation Suite */
"use strict";
window.OpenSTEMModels=(()=>{
 const expressions={
  1: x => (Math.atan(Math.tan(36*Math.PI/180)*Math.sin(x*Math.PI/180))*180/Math.PI),
  2: x => (8*Math.sin(x*Math.PI/180)),
  3: x => (100*(x-12)/12),
  4: x => (Math.log(x)),
  5: x => (115-x),
  6: x => (100-x),
  7: x => (240/x),
  8: x => (100*(130-x)/130),
  9: x => (30*Math.tan(x*Math.PI/180)),
  10: x => (60*Math.cos(x*Math.PI/180)),
  11: x => (x/12),
  12: x => (100*x/250),
  13: x => (x/8),
  14: x => (24/x),
  15: x => (100*Math.abs(x-104)/104),
  16: x => (32/x)
 };
 function num(v){return Number(v).toLocaleString(undefined,{maximumFractionDigits:5});}
 function makeSvgNode(svg,tag,attrs){let el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attrs).forEach(([k,v])=>el.setAttribute(k,v));svg.appendChild(el);}
 function update(card){
  const id=Number(card.dataset.model),m=window.OPENSTEM_MODEL_DATA.find(z=>z.id===id),f=expressions[id],inp=card.querySelector('input');
  if(!m||!f||!inp)throw new Error('Model setup missing '+id);
  const x=Number(inp.value),val=f(x);
  if(!Number.isFinite(val))throw new Error('Nonfinite model '+id);
  card.querySelector('.live-value').textContent=num(x)+' '+m.input_unit;
  card.querySelector('output').value=num(val)+' '+m.output_unit;
  const samples=Array.from({length:65},(_,j)=>{const sx=m.min+(m.max-m.min)*j/64;return {x:sx,y:f(sx)}});
  const yy=samples.map(s=>s.y),lower=Math.min(...yy),upper=Math.max(...yy),denom=upper-lower||1;
  const path=samples.map((p,j)=>(j?'L':'M')+(12+3.6*j).toFixed(2)+','+(98-82*(p.y-lower)/denom).toFixed(2)).join(' ');
  const currentX=12+3.6*64*(x-m.min)/(m.max-m.min),currentY=98-82*(val-lower)/denom;
  const svg=card.querySelector('svg');svg.replaceChildren();
  makeSvgNode(svg,'path',{d:'M12 12V98H244',fill:'none',stroke:'#9bb9bc','stroke-width':1});
  makeSvgNode(svg,'path',{d:path,fill:'none',stroke:'#127a82','stroke-width':2.4});
  makeSvgNode(svg,'circle',{cx:currentX,cy:currentY,r:4.4,fill:'#cc7542',stroke:'#fff','stroke-width':1});
 }
 function boot(){document.querySelectorAll('.model').forEach(card=>{const inp=card.querySelector('input');inp.addEventListener('input',()=>update(card));update(card)})}
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

