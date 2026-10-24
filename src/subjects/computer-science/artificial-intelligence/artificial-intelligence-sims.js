/* Original OpenSTEM Artificial Intelligence simulations: bounded quantitative teaching models; unpublished editorial draft. */

(function(root){'use strict';
const S={
 'ai-u1-a':{name:'Boolean sensor-state upper bound',unit:1,label:'possible configurations',note:'Exactly n independent Boolean flags imply 2^n encodings; reachable configurations can be fewer.',fn:n=>2**n},
 'ai-u1-b':{name:'Robot grid state upper bound',unit:1,label:'position-heading configurations',note:'n-by-n passable grid with four headings; 4n² encodings, ignoring battery and inaccessible cells.',fn:n=>4*n*n},
 'ai-u2-a':{name:'Full binary search-tree nodes',unit:2,label:'tree nodes through depth n',note:'Branching factor two; root counted at depth zero. Shared graph states and pruning ignored.',fn:n=>2**(n+1)-1},
 'ai-u2-b':{name:'Manhattan distance on square grid',unit:2,label:'unit cardinal moves',note:'Start (0,0), goal (n,n), four-direction unit steps without obstacles. Diagonal moves would change this.',fn:n=>2*n},
 'ai-u3-a':{name:'Propositional truth assignments',unit:3,label:'Boolean assignments',note:'n independent propositional variables; a brute-force truth table contains 2^n rows.',fn:n=>2**n},
 'ai-u3-b':{name:'Unordered variable pairs',unit:3,label:'pairwise relations',note:'n distinct entities; n(n-1)/2 unordered pairs. Not the total size of an arbitrary ontology.',fn:n=>n*(n-1)/2},
 'ai-u4-a':{name:'Positive predictive value',unit:4,label:'percent posterior',note:'Event prior 10%, sensitivity 90%, false-positive rate n/1000. Uses the binary Bayes rule.',fn:n=>100*(0.09/(0.09+0.9*n/1000))},
 'ai-u4-b':{name:'Binary entropy',unit:4,label:'bits',note:'Bernoulli event probability p=n/20, using Shannon entropy -p log2 p -(1-p)log2(1-p).',fn:n=>{const p=n/20;return -p*Math.log2(p)-(1-p)*Math.log2(1-p)}},
 'ai-u5-a':{name:'Three-action sequence count',unit:5,label:'length-n action sequences',note:'Exactly three unrestricted action choices at each step; does not filter preconditions, resources or duplicate reached states.',fn:n=>3**n},
 'ai-u5-b':{name:'Single-resource task duration',unit:5,label:'minutes',note:'One fixed preparation action of 15 minutes followed by n serial tasks of two minutes each.',fn:n=>15+2*n},
 'ai-u6-a':{name:'Classifier recall',unit:6,label:'percent recall',note:'Exactly n true positives and three false negatives; does not represent model training.',fn:n=>100*n/(n+3)},
 'ai-u6-b':{name:'Two-example Brier score',unit:6,label:'mean squared probability error',note:'Forecast p=n/20 for event 1 and 1-p for event 0; mean binary Brier error equals (1-p)^2.',fn:n=>(1-n/20)**2},
 'ai-u7-a':{name:'Padded image patch count',unit:7,label:'image patches',note:'224×224 image, square patches of side n, with padding on right and bottom to complete tiles.',fn:n=>Math.ceil(224/n)**2},
 'ai-u7-b':{name:'Dense attention score count',unit:7,label:'query-key scores',note:'One layer with n tokens and full pairwise attention; n² score entries, excluding heads, masks and implementation optimizations.',fn:n=>n*n},
 'ai-u8-a':{name:'Group-error rate disparity',unit:8,label:'percentage points',note:'Two groups each with 100 examples: group A has n errors and B has 2n errors. Difference in rates is n percentage points.',fn:n=>n},
 'ai-u8-b':{name:'Expected false alerts in rare events',unit:8,label:'expected false alerts',note:'9,900 nonevents and false-positive rate n/1000; output is an expected count, not a realized integer.',fn:n=>9.9*n}
};
function calculate(type,n){
 if(!Object.prototype.hasOwnProperty.call(S,type))throw new RangeError('Unknown type');
 if(!Number.isInteger(n)||n<2||n>16)throw new RangeError('Input n must be integer 2 through 16');
 const meta=S[type],value=meta.fn(n);
 if(!Number.isFinite(value))throw new Error('Model output not finite');
 return {type,n,value,label:meta.label,name:meta.name,note:meta.note,unit:meta.unit};
}
function initSimulation(elementId,type){
 if(typeof document==='undefined')return false;
 const el=document.getElementById(elementId);if(!el||!Object.prototype.hasOwnProperty.call(S,type))return false;
 el.replaceChildren();let title=document.createElement('h3');title.textContent=S[type].name;
 let lab=document.createElement('label');lab.textContent='Change input n (2–16): ';
 let slider=document.createElement('input');slider.type='range';slider.min='2';slider.max='16';slider.step='1';slider.value='6';slider.setAttribute('aria-label','Input for '+S[type].name);lab.append(slider);
 let out=document.createElement('output');out.setAttribute('role','status');out.setAttribute('aria-live','polite');out.style.display='block';
 let note=document.createElement('p');note.style.fontSize='.91rem';
 let reset=document.createElement('button');reset.type='button';reset.textContent='Reset simulation';
 let svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.setAttribute('viewBox','0 0 360 165');svg.setAttribute('role','img');svg.setAttribute('aria-label','Model outputs over 15 integer inputs from 2 to 16');svg.style.width='100%';svg.style.height='auto';
 function render(){
  let n=Number(slider.value),v=calculate(type,n),a=Array.from({length:15},(_,i)=>calculate(type,i+2));
  out.textContent='Input n = '+n+'; output = '+Number(v.value.toPrecision(10))+' '+v.label;
  note.textContent='Assumptions and limits: '+v.note;
  const lo=Math.min(0,...a.map(x=>x.value)),hi=Math.max(0,...a.map(x=>x.value)),range=Math.max(hi-lo,1e-15),zero=10+130*(hi/range);
  svg.replaceChildren();a.forEach((x,i)=>{
   const yy=10+130*(hi-x.value)/range;
   const rect=document.createElementNS('http://www.w3.org/2000/svg','rect');rect.setAttribute('x',String(8+i*23));rect.setAttribute('y',String(Math.min(zero,yy)));rect.setAttribute('height',String(Math.max(2,Math.abs(zero-yy))));rect.setAttribute('width','16');rect.setAttribute('rx','2');rect.setAttribute('fill',x.n===n?'#b67a22':'#247c91');
   const tip=document.createElementNS('http://www.w3.org/2000/svg','title');tip.textContent='n='+x.n+', '+x.value;rect.append(tip);svg.append(rect);
  });
 }
 slider.addEventListener('input',render);reset.addEventListener('click',()=>{slider.value='6';render();});el.append(title,lab,out,svg,note,reset);render();return true;
}
root.OpenSTEMModel={book:'artificial-intelligence',types:Object.keys(S),calculate,initSimulation};
root.SimulationEngine={...(root.SimulationEngine||{}),initSimulation};
})(typeof window==='undefined'?globalThis:window);
