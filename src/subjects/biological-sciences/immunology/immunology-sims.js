/* Immunology Interactive Simulation Suite */
(function(){
"use strict";
const MODELS=[{"id": 0, "unit": 1, "title": "Barrier proxy versus time", "kind": "barrier", "xLabel": "Time after abstract challenge (h)", "yLabel": "Relative tracer passage", "xMin": 0, "xMax": 6, "a": {"label": "Initial passage", "value": 1.0, "min": 0.3, "max": 1.8}, "b": {"label": "Regulation factor", "value": 0.5, "min": 0.1, "max": 1.2}, "warning": "A saturating rise in tracer passage is an illustrative permeability relationship, not a pathogen entry model."}, {"id": 1, "unit": 1, "title": "Cell migration balance", "kind": "traffic", "xLabel": "Time (h)", "yLabel": "Net accumulated cells", "xMin": 0, "xMax": 8, "a": {"label": "Cell influx / h", "value": 80, "min": 10, "max": 180}, "b": {"label": "Exit fraction / h", "value": 0.15, "min": 0.02, "max": 0.4}, "warning": "Assumes no proliferation and homogeneous cell residence."}, {"id": 2, "unit": 2, "title": "Saturating sensor activation", "kind": "sensor", "xLabel": "Ligand concentration (relative)", "yLabel": "Activated sensor fraction", "xMin": 0, "xMax": 10, "a": {"label": "Response gain", "value": 1, "min": 0.5, "max": 1.5}, "b": {"label": "Half-max ligand", "value": 3, "min": 0.5, "max": 7}, "warning": "Single-receptor occupancy proxy with no pathway crosstalk."}, {"id": 3, "unit": 2, "title": "Ideal chemotactic movement", "kind": "chemotaxis", "xLabel": "Gradient strength (relative)", "yLabel": "Directional index proxy", "xMin": 0, "xMax": 10, "a": {"label": "Maximum bias", "value": 0.7, "min": 0.1, "max": 1.0}, "b": {"label": "Gradient half-scale", "value": 3, "min": 0.5, "max": 9}, "warning": "Random motion and heterogeneous cells are omitted."}, {"id": 4, "unit": 3, "title": "One-site epitope occupancy", "kind": "binding", "xLabel": "Free ligand (arbitrary concentration)", "yLabel": "Fraction occupied", "xMin": 0, "xMax": 10, "a": {"label": "Available receptor fraction", "value": 1, "min": 0.3, "max": 1}, "b": {"label": "Dissociation parameter", "value": 2.5, "min": 0.3, "max": 8}, "warning": "Ideal equilibrium curve; multivalency and kinetic effects omitted."}, {"id": 5, "unit": 3, "title": "Antigen presentation saturation", "kind": "presentation", "xLabel": "Processed peptide supply", "yLabel": "Peptide–MHC proxy", "xMin": 0, "xMax": 12, "a": {"label": "Presentation capacity", "value": 80, "min": 15, "max": 150}, "b": {"label": "Half-saturation supply", "value": 3, "min": 1, "max": 10}, "warning": "Bulk MHC display cannot identify a particular peptide complex."}, {"id": 6, "unit": 4, "title": "Toy clonal expansion", "kind": "clone", "xLabel": "Time after activation (days)", "yLabel": "Cell number (relative)", "xMin": 0, "xMax": 7, "a": {"label": "Initial abundance", "value": 10, "min": 1, "max": 30}, "b": {"label": "Doubling interval", "value": 2.5, "min": 1.5, "max": 5}, "warning": "Exponential growth only for early responses; no carrying capacity."}, {"id": 7, "unit": 4, "title": "Cytotoxic survival proxy", "kind": "cytotoxic", "xLabel": "Effector exposure (relative)", "yLabel": "Remaining target fraction", "xMin": 0, "xMax": 10, "a": {"label": "Maximum effect fraction", "value": 0.8, "min": 0.1, "max": 1.0}, "b": {"label": "Effect half-scale", "value": 2.5, "min": 0.5, "max": 8}, "warning": "This is a mathematical proxy and cannot predict therapeutic killing."}, {"id": 8, "unit": 5, "title": "B-cell activation surface", "kind": "bcell", "xLabel": "Receptor stimulus (relative)", "yLabel": "Activation fraction proxy", "xMin": 0, "xMax": 10, "a": {"label": "Helper strength", "value": 0.8, "min": 0.1, "max": 1.0}, "b": {"label": "Half-stimulus", "value": 3, "min": 0.5, "max": 8}, "warning": "No anergy, competition or differentiation included."}, {"id": 9, "unit": 5, "title": "Antibody functional occupancy", "kind": "antibody", "xLabel": "Antibody concentration proxy", "yLabel": "Fraction bound", "xMin": 0, "xMax": 10, "a": {"label": "Max binding fraction", "value": 0.9, "min": 0.3, "max": 1}, "b": {"label": "Half-saturation", "value": 2, "min": 0.5, "max": 7}, "warning": "Binding occupancy alone is not neutralization or protection."}, {"id": 10, "unit": 6, "title": "Peripheral tolerance filter", "kind": "tolerance", "xLabel": "Receptor stimulus", "yLabel": "Responding fraction proxy", "xMin": 0, "xMax": 10, "a": {"label": "Regulatory intensity", "value": 0.5, "min": 0.0, "max": 0.95}, "b": {"label": "Activation half-scale", "value": 3, "min": 0.5, "max": 8}, "warning": "No direct prediction of autoimmunity or immune-system health."}, {"id": 11, "unit": 6, "title": "Mediator response saturation", "kind": "mediator", "xLabel": "Abstract stimulus strength", "yLabel": "Relative mediator release", "xMin": 0, "xMax": 10, "a": {"label": "Max reporter response", "value": 1, "min": 0.2, "max": 2.0}, "b": {"label": "Half-saturation", "value": 3, "min": 0.5, "max": 8}, "warning": "No human allergy risk or trigger threshold is inferable."}, {"id": 12, "unit": 7, "title": "Immune escape trade-off", "kind": "escape", "xLabel": "Immune pressure proxy", "yLabel": "Relative lineage growth", "xMin": 0, "xMax": 10, "a": {"label": "Intrinsic growth", "value": 1.4, "min": 0.5, "max": 2}, "b": {"label": "Recognition cost", "value": 0.15, "min": 0.05, "max": 0.35}, "warning": "No microbial evolution or transmissibility prediction; purely abstract lineages."}, {"id": 13, "unit": 7, "title": "Simple immunity decay", "kind": "waning", "xLabel": "Time (months)", "yLabel": "Relative marker", "xMin": 0, "xMax": 24, "a": {"label": "Initial marker", "value": 1, "min": 0.5, "max": 2}, "b": {"label": "Decay half-life", "value": 9, "min": 3, "max": 18}, "warning": "Marker decay is not equal to waning clinical protection."}, {"id": 14, "unit": 8, "title": "Alloactivation proxy", "kind": "allo", "xLabel": "Mismatch stimulus (relative)", "yLabel": "Activation proxy", "xMin": 0, "xMax": 10, "a": {"label": "Costimulation fraction", "value": 0.7, "min": 0.1, "max": 1}, "b": {"label": "Half-max stimulus", "value": 3, "min": 0.5, "max": 8}, "warning": "Nonclinical illustration; no organ-matching prediction."}, {"id": 15, "unit": 8, "title": "Assay signal saturation", "kind": "assay", "xLabel": "True analyte concentration (relative)", "yLabel": "Detector signal", "xMin": 0, "xMax": 10, "a": {"label": "Detector gain", "value": 1.0, "min": 0.4, "max": 1.5}, "b": {"label": "Saturation scale", "value": 3, "min": 0.5, "max": 8}, "warning": "Illustrates saturation, not actual assay calibration."}];
function curve(kind,x,a,b){
const cap=(v)=>Math.max(0,Math.min(1,v));
switch(kind){
 case "barrier":return a*(1-Math.exp(-b*x))+0.2;
 case "traffic":return a/b*(1-Math.exp(-b*x));
 case "sensor":return cap(a*x/(b+x));
 case "chemotaxis":return cap(a*x/(b+x));
 case "binding":return cap(a*x/(b+x));
 case "presentation":return a*x/(b+x);
 case "clone":return a*Math.pow(2,x/b);
 case "cytotoxic":return Math.max(0,1-a*x/(b+x));
 case "bcell":return cap(a*x/(b+x));
 case "antibody":return cap(a*x/(b+x));
 case "tolerance":return cap((1-a)*x/(b+x));
 case "mediator":return a*x/(b+x);
 case "escape":return a*Math.exp(-b*x);
 case "waning":return a*Math.pow(2,-x/b);
 case "allo":return cap(a*x/(b+x));
 case "assay":return a*x/(b+x);
 default:return x;
}}
function node(tag,attrs,text){const e=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,String(v)));if(text!==undefined)e.textContent=text;return e}
function makeGraph(model,svg,a,b){
 const W=650,H=280,left=55,right=18,top=18,bottom=48;
 const ys=Array.from({length:121},(_,i)=>curve(model.kind,model.xMin+(model.xMax-model.xMin)*i/120,a,b));
 const ref=Array.from({length:121},(_,i)=>curve(model.kind,model.xMin+(model.xMax-model.xMin)*i/120,model.a.value,model.b.value));
 const ymin=Math.min(0,...ys,...ref),ymax=Math.max(...ys,...ref),span=Math.max(0.01,ymax-ymin);
 svg.setAttribute('viewBox',`0 0 ${W} ${H}`);svg.replaceChildren();
 const xy=(i,y)=>[left+(W-left-right)*i/120,H-bottom-(y-ymin)/span*(H-top-bottom)];
 for(let j=0;j<=4;j++){let y=H-bottom-j*(H-top-bottom)/4;svg.appendChild(node('line',{x1:left,y1:y,x2:W-right,y2:y,stroke:'#e3ebef'}));svg.appendChild(node('text',{x:3,y:y+4,class:'axis'},(ymin+span*j/4).toPrecision(3)))}
 const refpts=ref.map((y,i)=>xy(i,y));svg.appendChild(node('path',{d:refpts.map((v,i)=>(i?'L':'M')+v[0].toFixed(1)+' '+v[1].toFixed(1)).join(' '),stroke:'#9ca7af','stroke-width':2,'stroke-dasharray':'5 5',fill:'none'}));
 const pts=ys.map((y,i)=>xy(i,y));svg.appendChild(node('path',{d:pts.map((v,i)=>(i?'L':'M')+v[0].toFixed(1)+' '+v[1].toFixed(1)).join(' '),stroke:'#166b86','stroke-width':3,fill:'none'}));
 svg.appendChild(node('text',{x:left,y:H-13,class:'axis'},String(model.xMin)));
 svg.appendChild(node('text',{x:W-right-40,y:H-13,class:'axis'},String(model.xMax)));
 svg.appendChild(node('text',{x:W/2,y:H-3,'text-anchor':'middle',class:'axis'},model.xLabel));
 svg.appendChild(node('text',{x:W-180,y:top+12,class:'axis'},'Gray dashed: default'));
 svg.setAttribute('role','img');svg.setAttribute('aria-label',`${model.title}: output ${model.yLabel}, x axis ${model.xLabel}. Curve varies with controls.`)
}
function mount(m){const el=document.querySelector(`[data-model="${m.id}"]`);if(!el)return;const s=el.querySelector('svg');const controls=el.querySelectorAll('input');const outputs=el.querySelectorAll('output');
 const paint=()=>{const a=Number(controls[0].value),b=Number(controls[1].value);outputs[0].textContent=a.toPrecision(3);outputs[1].textContent=b.toPrecision(3);makeGraph(m,s,a,b)};
 for(const input of controls)input.addEventListener('input',paint);paint();}
document.addEventListener('DOMContentLoaded',()=>MODELS.forEach(mount));
})();



/* SimulationEngine adapter for Immunology */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof MODELS === 'undefined' || typeof mount !== 'function') return;
    host.replaceChildren();
    var match = (simType || '').match(/(\d+)$/);
    var u = match ? parseInt(match[1], 10) : 1;
    var idx = (u - 1) * 2;
    var m = MODELS[idx] || MODELS[0];
    if (m) {
      var card = document.createElement('div');
      card.className = 'sim-card';
      card.dataset.model = String(m.id);
      card.innerHTML = '<h4>' + m.title + '</h4>' +
        '<div class="controls">' +
        '<label>' + m.a.label + ': <output>' + m.a.value + '</output><br><input type="range" class="a" min="' + m.a.min + '" max="' + m.a.max + '" step="' + ((m.a.max-m.a.min)/100) + '" value="' + m.a.value + '"></label>' +
        '<label>' + m.b.label + ': <output>' + m.b.value + '</output><br><input type="range" class="b" min="' + m.b.min + '" max="' + m.b.max + '" step="' + ((m.b.max-m.b.min)/100) + '" value="' + m.b.value + '"></label>' +
        '</div><svg></svg><p class="readout">' + (m.warning || '') + '</p>';
      host.appendChild(card);
      mount(m);
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

