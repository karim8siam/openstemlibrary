/* Sedimentology and Stratigraphy Interactive Simulation Suite */
"use strict";
window.OpenSTEMModels=(()=>{
 const expressions={
  1: x => (560-70-x),
  2: x => (6.2*Math.sin(x*Math.PI/180)),
  3: x => (1000*9.81*x*0.0016),
  4: x => (1650*9.81*Math.pow(x*1e-6,2)/(18*0.001)),
  5: x => (38*Math.exp(-0.05*x)),
  6: x => (0.14*x),
  7: x => (100*x/(x+38)),
  8: x => (0.0002*x),
  9: x => (85-x),
  10: x => (72/x),
  11: x => (0.72/x),
  12: x => (12*(1-0.22)/(1-x)),
  13: x => (100*(1-x/2650)),
  14: x => (x*1850*0.4),
  15: x => (100*x/36),
  16: x => (73/x)
 };
 function fmt(v){return Number(v).toLocaleString(undefined,{maximumFractionDigits:5});}
 function update(card){
  const id=Number(card.dataset.model),input=card.querySelector('input'),x=Number(input.value),m=window.OPENSTEM_MODEL_DATA.find(z=>z.id===id), f=expressions[id];
  if(!f||!m)throw new Error('Unknown model '+id);
  const value=f(x),live=card.querySelector('.live-value'),out=card.querySelector('output');
  live.textContent=fmt(x)+' '+m.input_unit;out.value=fmt(value)+' '+m.output_unit;
  const values=[];
  for(let j=0;j<=64;j++){let px=m.min+(m.max-m.min)*j/64;values.push({x:px,y:f(px)})}
  let ymin=Math.min(...values.map(p=>p.y)),ymax=Math.max(...values.map(p=>p.y)),dy=ymax-ymin||1;
  const path=values.map((p,i)=>(i?'L':'M')+(12+3.6*i).toFixed(1)+','+(98-(p.y-ymin)/dy*82).toFixed(1)).join(' ');
  const currentX=12+(x-m.min)/(m.max-m.min)*64*3.6;
  const y=98-(value-ymin)/dy*82,svg=card.querySelector('svg');
  svg.innerHTML='';
  function node(tag,a){let el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(a).forEach(([k,v])=>el.setAttribute(k,v));svg.appendChild(el);}
  node('path',{d:'M12 12V98H244',stroke:'#8ca3a5','stroke-width':1,fill:'none'});
  node('path',{d:path,stroke:'#147982','stroke-width':2.6,fill:'none'});
  node('circle',{cx:currentX,cy:y,r:4.3,fill:'#bf663f',stroke:'#fff','stroke-width':1});
 }
 function boot(){document.querySelectorAll('.model').forEach(c=>{const inp=c.querySelector('input');inp.addEventListener('input',()=>update(c));update(c)})}
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

