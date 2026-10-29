/* Molecular Biology Interactive Simulation Suite */
(function(global){'use strict';
const definitions=[{"key":"melting","name":"Short-primer Wallace estimate","xlabel":"GC pairs among a model duplex","xmin":0,"xmax":20,"xinit":8,"plabel":"Oligo length (bp)","pmin":20,"pmax":40,"pinit":28,"unit":"°C, rough short-primer rule","limit":"For short oligonucleotides only; ignores salt and nearest-neighbor thermodynamics."},{"key":"entropy","name":"Sequence-base entropy","xlabel":"GC fraction","xmin":0.001,"xmax":0.999,"xinit":0.45,"plabel":"Within-group base bias","pmin":0.1,"pmax":0.9,"pinit":0.5,"unit":"bits/base","limit":"Independent nucleotide frequencies; not genomic compression entropy."},{"key":"fork","name":"Bidirectional fork travel","xlabel":"Replicated region (Mb)","xmin":0.2,"xmax":4.0,"xinit":2.4,"plabel":"Fork speed (nt/s)","pmin":100,"pmax":1400,"pinit":600,"unit":"minutes","limit":"Exactly two symmetric constant-speed forks with no stalls or origin effects."},{"key":"fidelity","name":"Probability of zero copying errors","xlabel":"Template length (kb)","xmin":1,"xmax":200,"xinit":20,"plabel":"Error rate per million bases","pmin":0.1,"pmax":10,"pinit":1,"unit":"% error-free","limit":"Per-base events are independent and do not include further repair or selection."},{"key":"repair","name":"Lesion-marker first-order disappearance","xlabel":"Time (hours)","xmin":0,"xmax":24,"xinit":6,"plabel":"Disappearance rate (per hour)","pmin":0.02,"pmax":1,"pinit":0.18,"unit":"% signal remaining","limit":"Signal decay is not necessarily faithful repair; death and dilution can mimic it."},{"key":"recomb","name":"At least one reporter recombination","xlabel":"Eligible cells","xmin":1,"xmax":50,"xinit":12,"plabel":"Event probability per cell (%)","pmin":0.1,"pmax":25,"pinit":8,"unit":"% with >=1 event","limit":"Independent identical eligible cells and perfect reporter detection."},{"key":"occupancy","name":"Single-site promoter occupancy","xlabel":"Free regulator (nM)","xmin":0,"xmax":100,"xinit":18,"plabel":"Dissociation constant (nM)","pmin":1,"pmax":50,"pinit":6,"unit":"% occupancy","limit":"Equilibrium occupancy does not equal productive transcription."},{"key":"transcripts","name":"RNA production and decay","xlabel":"Time since induction (hours)","xmin":0,"xmax":12,"xinit":4,"plabel":"Removal constant (per hour)","pmin":0.05,"pmax":1.5,"pinit":0.5,"unit":"mean RNA molecules","limit":"Constant initiation at 25 molecules/hour, initial RNA zero; deterministic mean."},{"key":"psi","name":"Splice-junction inclusion","xlabel":"Inclusion-junction reads","xmin":0,"xmax":1000,"xinit":360,"plabel":"Skipping-junction reads","pmin":100,"pmax":1000,"pinit":240,"unit":"% PSI","limit":"Assumes correctly assigned, comparable junction-spanning observations."},{"key":"decay","name":"RNA first-order half-life","xlabel":"Time since shutoff (hours)","xmin":0,"xmax":24,"xinit":10.5,"plabel":"RNA half-life (hours)","pmin":0.5,"pmax":12,"pinit":3.5,"unit":"% remaining","limit":"True shutoff and constant first-order decay are assumed."},{"key":"translation","name":"Ribosome elongation traversal","xlabel":"Polypeptide length (amino acids)","xmin":30,"xmax":900,"xinit":420,"plabel":"Elongation speed (aa/s)","pmin":1,"pmax":30,"pinit":14,"unit":"seconds","limit":"Excludes initiation, termination, pauses and folding delays."},{"key":"repression","name":"Hill-form translation repression","xlabel":"Repressor abundance (relative units)","xmin":0,"xmax":30,"xinit":12,"plabel":"Half-response K (same units)","pmin":1,"pmax":30,"pinit":6,"unit":"% modeled output","limit":"Phenomenological repression curve; not a mechanism diagnosis."},{"key":"chromatin","name":"Sigmoid chromatin access proxy","xlabel":"State drive (relative units)","xmin":-4,"xmax":4,"xinit":0.7,"plabel":"Sigmoid steepness (1/drive)","pmin":0.2,"pmax":6,"pinit":2,"unit":"% modeled access","limit":"Hypothetical control curve, not a directly measured physical probability."},{"key":"feedback","name":"Negative-feedback steady state","xlabel":"Input strength (relative units)","xmin":0,"xmax":30,"xinit":12,"plabel":"Feedback coefficient","pmin":0,"pmax":2,"pinit":0.25,"unit":"steady-state output","limit":"Solves x=u/(1+a*x), not time dynamics or a complete gene circuit."},{"key":"pcr","name":"Ideal PCR amplification","xlabel":"Amplification cycles","xmin":0,"xmax":35,"xinit":20,"plabel":"Per-cycle amplification efficiency","pmin":0.1,"pmax":1.0,"pinit":0.85,"unit":"predicted template copies","limit":"Ten starting templates; no reagent depletion, inhibitors or plateau."},{"key":"coverage","name":"Nominal sequence-read coverage","xlabel":"Number of reads (millions)","xmin":0.1,"xmax":10,"xinit":2,"plabel":"Read length (base pairs)","pmin":75,"pmax":250,"pinit":125,"unit":"mean-fold coverage","limit":"Assumes all read bases map to a 5 Mb reference, uniformly without duplicates."}];
function value(key,x,p){
  const d=definitions.find(d=>d.key===key);
  if(!d)throw new RangeError('Unknown molecular model: '+key);
  if(typeof x!=='number'||typeof p!=='number'||!Number.isFinite(x)||!Number.isFinite(p)||x<d.xmin-1e-10||x>d.xmax+1e-10||p<d.pmin-1e-10||p>d.pmax+1e-10)throw new RangeError('Model input outside documented domain');
  switch(key){
    case 'melting':return 2*(p-x)+4*x;
    case 'entropy':{
      const ps=[(1-x)*(1-p),(1-x)*p,x*p,x*(1-p)];
      return -ps.reduce((a,q)=>a+(q>0?q*Math.log2(q):0),0);
    }
    case 'fork':return x*1000000/(2*p*60);
    case 'fidelity':return 100*Math.pow(1-p*0.000001,x*1000);
    case 'repair':return 100*Math.exp(-x*p);
    case 'recomb':return 100*(1-Math.pow(1-p/100,x));
    case 'occupancy':return 100*x/(p+x);
    case 'transcripts':return 25/p*(1-Math.exp(-p*x));
    case 'psi':return 100*x/(x+p);
    case 'decay':return 100*Math.pow(2,-x/p);
    case 'translation':return x/p;
    case 'repression':return 100/(1+(x/p)*(x/p));
    case 'chromatin':return 100/(1+Math.exp(-p*x));
    case 'feedback':return p===0?x:(2*x)/(1+Math.sqrt(1+4*p*x));
    case 'pcr':return 10*Math.pow(1+p,x);
    case 'coverage':return x*p/5;
  }
  throw new RangeError('Unknown model');
}
function el(tag,cls,text){const e=document.createElement(tag);if(cls)e.className=cls;if(text!==undefined)e.textContent=text;return e;}
const groups={melting:'DNA duplex',entropy:'Sequence composition',fork:'Replication forks',fidelity:'Copying errors',repair:'Damaged bases',recomb:'Break repair',occupancy:'Regulator binding',transcripts:'RNA transcription',psi:'Exon inclusion',decay:'RNA decay',translation:'Ribosome travel',repression:'Translational control',chromatin:'Chromatin state',feedback:'Regulatory circuit',pcr:'PCR cycle',coverage:'Sequencing coverage'};
function schematic(key,x,p,y){
 const dark='#0d2035', blue='#38bdf8',lime='#86efac',amber='#fbbf24',dim='#9eb2c7';
 const symbol=(s,px,py,color=dim,size=14)=>`<text x="${px}" y="${py}" fill="${color}" font-family="system-ui" font-size="${size}">${s}</text>`;
 const line=(a,b,c,d,col=blue,wide=3)=>`<line x1="${a}" y1="${b}" x2="${c}" y2="${d}" stroke="${col}" stroke-width="${wide}" stroke-linecap="round"/>`;
 let fig='';
 if(['melting','entropy','fidelity','repair'].includes(key)){
   fig+=line(32,45,560,45,blue,7)+line(32,78,560,78,lime,7);
   for(let i=0;i<17;i++){const px=44+i*30;fig+=line(px,50,px,73,i%4===0?amber:dim,2.2);}
   fig+=symbol(key==='repair'?'Lesions are markers, not directly confirmed repair':key==='fidelity'?'Every copied base is one idealized trial':key==='entropy'?'Base proportions determine an information proxy':'Model duplex · short-primer rule only',34,108,dim,13);
 }else if(['fork','recomb','transcripts','translation','pcr'].includes(key)){
   fig+=line(32,64,562,64,dim,4);
   if(key==='fork')fig+=line(294,63,155,37,blue,5)+line(294,63,433,37,lime,5);
   else if(key==='translation'){for(let i=0;i<5;i++)fig+=`<circle cx="${105+i*80}" cy="64" r="17" fill="${i<3?blue:lime}" opacity=".87"/>`;}
   else if(key==='pcr'){for(let i=0;i<6;i++){fig+=line(80+i*65,40,80+i*65,90,i%2?blue:lime,5);}}
   else fig+=`<circle cx="270" cy="64" r="25" fill="none" stroke="${amber}" stroke-width="5"/>`;
   fig+=symbol(groups[key]+' · ideal process representation',32,112,dim,13);
 }else{
   fig+=`<rect x="35" y="31" width="166" height="62" rx="9" fill="#143d59" stroke="${blue}" stroke-width="2"/><rect x="390" y="31" width="170" height="62" rx="9" fill="#174f44" stroke="${lime}" stroke-width="2"/>`;
   fig+=line(205,62,382,62,amber,4);fig+=`<path d="M374 54 L387 62 L374 70" fill="none" stroke="${amber}" stroke-width="4"/>`;
   fig+=symbol(key==='psi'?'junction reads':key==='occupancy'?'regulator':key==='chromatin'?'DNA state':key==='feedback'?'network input':key==='repression'?'repressor':key==='decay'?'RNA molecules':'molecular input',48,67,'#e7f5ff',13);
   fig+=symbol('measured output',410,67,'#e7f5ff',13);
   fig+=symbol(groups[key]+' · illustrative state flow',33,112,dim,13);
 }
 return `<svg viewBox="0 0 600 130" role="img" aria-label="Molecular mechanism schematic: ${groups[key]}" xmlns="http://www.w3.org/2000/svg"><title>Conceptual molecular state diagram</title><rect width="600" height="130" rx="11" fill="${dark}"/>${fig}</svg>`;
}
function buildCard(host,key){
 const targetKey = (typeof key === 'string' ? key.replace(/^molecular-/, '').replace(/-\d+$/, '') : '') || (definitions[0] && definitions[0].key);
 const d=definitions.find(d=>d.key===key || d.key===targetKey) || definitions[0];
 if(!d) return;
 host.className='simulator';host.innerHTML='';host.appendChild(el('h4','',d.name));
 host.appendChild(el('p','sim-limit','Model assumptions: '+d.limit));
 const ctl=el('div','control-grid');host.appendChild(ctl);
 function slider(label,min,max,initial,n){
  const w=el('label','control',label),out=el('output','control-value',String(initial));w.appendChild(out);
  const r=el('input');r.type='range';r.min=String(min);r.max=String(max);r.step=(max-min<2)?'.001':(max-min<100?'.1':'1');r.value=String(initial);r.setAttribute('aria-label',label);
  w.appendChild(r);ctl.appendChild(w);return {r,out,initial};
 }
 const a=slider(d.xlabel,d.xmin,d.xmax,d.xinit,'x'),b=slider(d.plabel,d.pmin,d.pmax,d.pinit,'p');
 const readout=el('p','sim-readout');readout.setAttribute('aria-live','polite');host.appendChild(readout);
 const svgMount=el('div','figure');host.appendChild(svgMount);
 const diagram=el('div','figure mechanism');host.appendChild(diagram);
 const reset=el('button','secondary','Reset model');reset.type='button';host.appendChild(reset);
 function draw(){const x=Number(a.r.value),p=Number(b.r.value),y=value(d.key,x,p);a.out.textContent=Number(x.toPrecision(5)).toString();b.out.textContent=Number(p.toPrecision(5)).toString();
   readout.textContent='Modeled output: '+Number(y.toPrecision(7))+' '+d.unit;
   const ys=[],n=72;for(let i=0;i<=n;i++){const xx=d.xmin+(d.xmax-d.xmin)*i/n;ys.push(value(d.key,xx,p));}
   let lo=Math.min(...ys,y),hi=Math.max(...ys,y);if(hi-lo<1e-10){lo-=1;hi+=1;}const pad=(hi-lo)*.07;lo-=pad;hi+=pad;
   const fy=q=>190-154*(q-lo)/(hi-lo),fx=t=>58+520*t;
   const path=ys.map((q,i)=>(i?'L':'M')+fx(i/n).toFixed(2)+' '+fy(q).toFixed(2)).join(' ');
   const xx=fx((x-d.xmin)/(d.xmax-d.xmin)),yy=fy(y);
   svgMount.innerHTML=`<svg viewBox="0 0 610 235" role="img" aria-label="Dynamic model curve for ${d.name}" xmlns="http://www.w3.org/2000/svg"><title>${d.name}: model output against ${d.xlabel}</title><rect width="610" height="235" rx="10" fill="#0d2035"/><path d="M58 28V190H580" stroke="#9db4ca" stroke-width="1.5" fill="none"/><path d="${path}" fill="none" stroke="#38bdf8" stroke-width="3.2"/><circle cx="${xx.toFixed(2)}" cy="${yy.toFixed(2)}" r="7" fill="#fbbf24" stroke="#fff" stroke-width="1"/><text x="10" y="32" font-size="11" fill="#ecf7ff">${Number(hi.toPrecision(3))}</text><text x="10" y="190" font-size="11" fill="#ecf7ff">${Number(lo.toPrecision(3))}</text><text x="60" y="211" font-size="11" fill="#ecf7ff">${d.xmin}</text><text x="546" y="211" font-size="11" fill="#ecf7ff">${d.xmax}</text><text x="210" y="229" font-size="12" fill="#ecf7ff">${d.xlabel}</text></svg>`;
   diagram.innerHTML=schematic(d.key,x,p,y);host.dataset.renderCount=String(1+Number(host.dataset.renderCount||0));
 }
 a.r.addEventListener('input',draw);b.r.addEventListener('input',draw);reset.addEventListener('click',()=>{a.r.value=String(a.initial);b.r.value=String(b.initial);draw();});draw();
}
const api={definitions,value,buildCard};global.MolecularModels=api;
global.OpenSTEMMolecularSims = api; if(typeof module!=='undefined'&&module.exports)module.exports=api;
if(typeof document!=='undefined'){if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>document.querySelectorAll('[data-molecular-model]').forEach(node=>buildCard(node,node.dataset.molecularModel)));else document.querySelectorAll('[data-molecular-model]').forEach(node=>buildCard(node,node.dataset.molecularModel));}
})(typeof window==='undefined'?globalThis:window);



/* SimulationEngine adapter for Molecular Biology */
(function(root) {
  var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = function(containerId, simType) {
    if (previous) { try { previous(containerId, simType); } catch (e) {} }
    var host = document.getElementById(containerId);
    if (!host) return;
    if (root.OpenSTEMMolecularSims && root.OpenSTEMMolecularSims.buildCard) {
      root.OpenSTEMMolecularSims.buildCard(host, simType);
    }
  };
})(typeof window === 'undefined' ? globalThis : window);

