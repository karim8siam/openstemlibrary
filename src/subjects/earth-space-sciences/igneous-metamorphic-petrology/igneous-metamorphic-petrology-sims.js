/* Igneous and Metamorphic Petrology Interactive Simulation Suite */
"use strict";
// Locally runnable teaching simulations, not calibrated predictions.
window.OpenSTEMModels = (()=>{
  const calculators = {
    1: x => x-1230,
    2: x => 3300*9.81*x*1000/1e6,
    3: x => 100*x/100,
    4: x => 100*x/(x+29+47),
    5: x => 2.1*Math.pow(x,-0.75),
    6: x => 49*x+71*(1-x),
    7: x => Math.exp(80000/8.314*(1/(x+273.15)-1/1323.15)),
    8: x => 1450*x,
    9: x => 3000*9.81*x*1000/1e9,
    10: x => 3-x+2,
    11: x => x*1e9/(3000*9.81)/1000,
    12: x => Math.sqrt(1e-6*x*365.25*86400),
    13: x => 100*x,
    14: x => 100*(x/50-1),
    15: x => 100*x/(x+44),
    16: x => 487-x
  };
  const round = v => Number(v).toLocaleString(undefined,{maximumFractionDigits:4});
  function update(card){
    const id=Number(card.dataset.model),x=Number(card.querySelector('input').value),m=window.OPENSTEM_MODEL_DATA.find(z=>z.id===id);
    const f=calculators[id],val=f(x);
    const out=card.querySelector('output'), live=card.querySelector('.live-value');
    out.value=round(val)+' '+m.output_unit;live.textContent=round(x)+' '+m.input_unit;
    const svg=card.querySelector('svg'), points=[];
    for(let i=0;i<50;i++){ const v=m.min+(m.max-m.min)*i/49;points.push({x:v,y:f(v)}) }
    const yMin=Math.min(...points.map(p=>p.y)),yMax=Math.max(...points.map(p=>p.y));
    const scaleY=v=>95-(v-yMin)/(yMax-yMin||1)*82;
    const poly=points.map((p,i)=>`${10+i*4.9},${scaleY(p.y).toFixed(2)}`).join(' ');
    const curX=10+(x-m.min)/(m.max-m.min)*49*4.9;
    svg.innerHTML='';
    function el(name,attrs){const e=document.createElementNS('http://www.w3.org/2000/svg',name);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,String(v)));svg.appendChild(e);return e}
    el('path',{d:'M10 11V95H251',stroke:'#8ba4a6','stroke-width':1,fill:'none'});
    el('polyline',{points:poly,stroke:'#126c75','stroke-width':2.3,fill:'none'});
    el('circle',{cx:curX,cy:scaleY(val),r:4.5,fill:'#c36437',stroke:'#fff','stroke-width':1.2});
  }
  function boot(){
    document.querySelectorAll('.model').forEach(card=>{
      const input=card.querySelector('input');input.addEventListener('input',()=>update(card));
      update(card);
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();
  return {calculate:(id,x)=>calculators[id](x),boot};
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

