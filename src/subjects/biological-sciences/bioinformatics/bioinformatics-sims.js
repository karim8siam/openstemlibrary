/* Bioinformatics Interactive Simulation Suite */
"use strict";
const modelSpecs=[{"id":"q","unit":1,"title":"Phred quality to estimated error","label":"Quality score (Q)","low":5,"high":45,"initial":25,"step":1,"kind":"quality","formula":"P(error) = 10^(−Q/10)","axis":"Estimated error probability"},{"id":"gc","unit":1,"title":"GC fraction in a toy sequence","label":"G or C bases among 100 positions","low":0,"high":100,"initial":42,"step":1,"kind":"fraction","formula":"GC% = 100 × GC bases / total bases","axis":"GC percentage"},{"id":"align","unit":2,"title":"Global matching score with mismatches","label":"Mismatches in 20 aligned bases","low":0,"high":20,"initial":4,"step":1,"kind":"alignment","formula":"Score = 2(20 − m) − m","axis":"Toy alignment score"},{"id":"blast","unit":2,"title":"Search-space effect on a model E-value","label":"Database size multiplier","low":1,"high":50,"initial":10,"step":1,"kind":"evalue","formula":"E = size × 0.001 (toy fixed-score assumption)","axis":"Toy E-value"},{"id":"orf","unit":3,"title":"Coding length to amino-acid count","label":"Coding nucleotides excluding stop","low":30,"high":900,"initial":300,"step":3,"kind":"orf","formula":"amino acids = coding nucleotides / 3","axis":"Amino-acid residues"},{"id":"allele","unit":3,"title":"Allele frequency from sample counts","label":"Alt-allele copies among 200 called chromosomes","low":0,"high":200,"initial":24,"step":1,"kind":"allele","formula":"p = alt copies / called chromosomes","axis":"Observed allele frequency"},{"id":"jc","unit":4,"title":"Jukes–Cantor correction","label":"Observed mismatch fraction (%)","low":1,"high":70,"initial":15,"step":1,"kind":"jc","formula":"d = −¾ ln(1−4p/3) (p < 0.75)","axis":"Estimated substitutions/site"},{"id":"mut","unit":4,"title":"Expected mismatches after substitutions","label":"Model substitution distance (×0.01)","low":1,"high":150,"initial":30,"step":1,"kind":"mut","formula":"p = ¾(1−e^(−4d/3))","axis":"Mismatch fraction"},{"id":"cpm","unit":5,"title":"Counts per million: changing read count","label":"Gene-associated reads, total library=2M","low":0,"high":400,"initial":80,"step":10,"kind":"cpm","formula":"CPM = 10^6 × gene count / library total","axis":"Counts per million"},{"id":"fold","unit":5,"title":"Log2 fold change","label":"Treatment reads (control=20; equal depth)","low":1,"high":160,"initial":80,"step":1,"kind":"fold","formula":"log2FC = log2(treatment/control)","axis":"Log₂ fold change"},{"id":"contact","unit":6,"title":"Contact fraction by Cα cutoff","label":"Contact distance cutoff (Å)","low":3,"high":14,"initial":8,"step":0.5,"kind":"contact","formula":"Fraction = pair distances ≤ cutoff / pairs","axis":"Contact fraction"},{"id":"rmsd","unit":6,"title":"Toy RMS displacement scale","label":"Coordinate displacement multiplier","low":0,"high":5,"initial":2,"step":0.1,"kind":"rmsd","formula":"RMSD = sqrt(mean squared deviations)","axis":"RMS displacement (Å)"},{"id":"bh","unit":7,"title":"BH cutoff at rank 3 of 20 tests","label":"Target FDR (%), rank fixed at 3","low":1,"high":25,"initial":5,"step":1,"kind":"bh","formula":"BH rank cutoff = (3 / 20) × FDR","axis":"Largest p-value eligible at rank 3"},{"id":"prec","unit":7,"title":"Precision under changing false positives","label":"False positives (TP fixed=18)","low":0,"high":30,"initial":5,"step":1,"kind":"precision","formula":"Precision = TP / (TP + FP)","axis":"Precision"},{"id":"parallel","unit":8,"title":"Ideal parallelization lower bound","label":"Independent workers for 12 identical 4-min tasks","low":1,"high":12,"initial":3,"step":1,"kind":"parallel","formula":"Minimum compute time = ceil(12/workers) × 4 min","axis":"Best-case wall time (minutes)"},{"id":"memory","unit":8,"title":"Per-worker memory budget","label":"Concurrent workers in 8 GB system","low":1,"high":8,"initial":4,"step":1,"kind":"memory","formula":"Available per worker = (8 GB − 2 GB overhead)/workers","axis":"GB per worker"}];
const $=(x,root=document)=>root.querySelector(x);
function compute(kind,x){
 const ds=[3.1,4.4,5.2,6.8,7.1,8.4,9.5,11.1,12.8,14.3];
 switch(kind){
 case 'quality':return Math.pow(10,-x/10);
 case 'fraction':return x;
 case 'alignment':return 2*(20-x)-x;
 case 'evalue':return 0.001*x;
 case 'orf':return x/3;
 case 'allele':return x/200;
 case 'jc':return -0.75*Math.log(1-4*(x/100)/3);
 case 'mut':return 0.75*(1-Math.exp(-4*(x/100)/3));
 case 'cpm':return x/2;
 case 'fold':return Math.log2(x/20);
 case 'contact':return ds.filter(v=>v<=x).length/ds.length;
 case 'rmsd':return Math.sqrt((1+4+9)/3)*x;
 case 'bh':return (3/20)*(x/100);
 case 'precision':return 18/(18+x);
 case 'parallel':return Math.ceil(12/x)*4;
 case 'memory':return 6/x;
 default:throw new Error('Unknown educational model: '+kind)
 }
}
function fmt(v){if(!Number.isFinite(v))return 'not defined';if(v===0)return '0';if(Math.abs(v)<0.001)return v.toExponential(3);if(Math.abs(v)<1)return v.toFixed(4);return v.toFixed(2);}
function el(name,attrs={}){const n=document.createElementNS('http://www.w3.org/2000/svg',name);for(const [k,v] of Object.entries(attrs))n.setAttribute(k,String(v));return n;}
function draw(spec,x,svg){
 const w=600,h=175,margin={l:28,r:22,t:12,b:28};svg.setAttribute('viewBox',`0 0 ${w} ${h}`);
 svg.replaceChildren();const samples=Array.from({length:81},(_,i)=>spec.low+(spec.high-spec.low)*(i/80));
 const values=samples.map(t=>compute(spec.kind,t));const min=Math.min(0,...values),max=Math.max(...values);
 const pad=(max-min||1)*0.12;const lo=min-pad,hi=max+pad;
 const sx=a=>margin.l+(a-spec.low)/(spec.high-spec.low)*(w-margin.l-margin.r);
 const sy=a=>margin.t+(hi-a)/(hi-lo)*(h-margin.t-margin.b);
 for(let g=0;g<4;g++){const y=margin.t+(h-margin.t-margin.b)*g/3;svg.appendChild(el('line',{x1:margin.l,y1:y,x2:w-margin.r,y2:y,stroke:'#d9e5eb','stroke-width':1}));}
 svg.appendChild(el('path',{d:values.map((v,i)=>(i===0?'M':'L')+sx(samples[i]).toFixed(2)+' '+sy(v).toFixed(2)).join(' '),fill:'none',stroke:'#087e82','stroke-width':3,'stroke-linecap':'round','stroke-linejoin':'round'}));
 svg.appendChild(el('line',{x1:sx(x),y1:margin.t,x2:sx(x),y2:h-margin.b,stroke:'#d77a41','stroke-width':1.5,'stroke-dasharray':'4 4'}));
 svg.appendChild(el('circle',{cx:sx(x),cy:sy(compute(spec.kind,x)),r:5,fill:'#c9692e',stroke:'#fff','stroke-width':2}));
 for(const [i,label] of [[0,String(spec.low)],[1,String(spec.high)]]){let node=el('text',{x:i? w-margin.r:margin.l,y:h-5,'text-anchor':i?'end':'start','font-size':12,fill:'#385468'});node.textContent=label;svg.appendChild(node);}
}
function init(){for(const spec of modelSpecs){const host=document.getElementById('model-'+spec.id);if(!host)continue;
 const input=$('input',host),output=$('[data-value]',host),svg=$('svg',host);if(!input||!output||!svg)continue;
 const update=()=>{const x=Number(input.value);output.textContent=fmt(compute(spec.kind,x));host.dataset.value=String(compute(spec.kind,x));$('[data-current]',host).textContent=String(x);draw(spec,x,svg);};
 input.addEventListener('input',update);update();}
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
window.OpenSTEMBioinformatics={compute,modelSpecs,init};



/* SimulationEngine adapter for Bioinformatics */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (typeof modelSpecs === 'undefined' || typeof compute !== 'function' || typeof draw !== 'function') return;
    host.replaceChildren();
    var match = (simType || '').match(/(\d+)$/);
    var u = match ? parseInt(match[1], 10) : 1;
    var idx = (u - 1) * 2;
    var spec = modelSpecs[idx] || modelSpecs[0];
    if (spec) {
      var card = document.createElement('div');
      card.className = 'sim-card';
      card.id = 'model-' + spec.id;
      card.innerHTML = '<h4>' + spec.title + '</h4>' +
        '<p class="formula"><code>' + spec.formula + '</code></p>' +
        '<label>' + spec.label + ': <span data-current>' + spec.initial + '</span><br>' +
        '<input type="range" min="' + spec.low + '" max="' + spec.high + '" step="' + spec.step + '" value="' + spec.initial + '"></label>' +
        '<p>Result (' + spec.axis + '): <strong data-value></strong></p><svg></svg>';
      host.appendChild(card);
      var input = card.querySelector('input');
      var output = card.querySelector('[data-value]');
      var svg = card.querySelector('svg');
      var update = function() {
        var x = Number(input.value);
        output.textContent = typeof fmt === 'function' ? fmt(compute(spec.kind, x)) : String(compute(spec.kind, x));
        var cur = card.querySelector('[data-current]');
        if (cur) cur.textContent = String(x);
        draw(spec, x, svg);
      };
      input.addEventListener('input', update);
      update();
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

