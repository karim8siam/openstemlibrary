/* OpenSTEM Theory of Computation: bounded educational models, draft. */
(function(root){'use strict';
const S={
 'toc-u1-a':{name:'Three-symbol fixed-length word count',unit:1,label:'strings of length n',note:'Exactly three abstract symbols, independent positions; 3^n words, n counts symbols rather than bytes.',fn:n=>3**n},
 'toc-u1-b':{name:'Binary strings up to chosen length',unit:1,label:'strings of length at most n',note:'Binary alphabet and all lengths 0 to n, including the empty word. Geometric sum 2^(n+1)-1.',fn:n=>2**(n+1)-1},
 'toc-u2-a':{name:'Binary DFA residue after reading n',unit:2,label:'final remainder modulo 3',note:'Interprets slider n as a nonnegative binary numeral. DFA state is remainder n mod 3; state zero accepts.',fn:n=>n%3},
 'toc-u2-b':{name:'NFA powerset-state upper bound',unit:2,label:'subsets of n-state set',note:'Maximum of 2^n subsets in construction. Many can be unreachable; this is not a measured DFA size.',fn:n=>2**n},
 'toc-u3-a':{name:'Dyck words with n bracket pairs',unit:3,label:'balanced single-type words',note:'Catalan(n)=binomial(2n,n)/(n+1) counts one bracket type, not all balanced multi-type sequences.',fn:n=>{let x=1;for(let k=0;k<n;k++)x=x*2*(2*k+1)/(k+2);return Math.round(x)}},
 'toc-u3-b':{name:'CYK interval split examinations',unit:3,label:'substring split positions',note:'For length n, sum of candidate interval split positions=(n^3-n)/6; excludes grammar-rule lookup costs.',fn:n=>(n**3-n)/6},
 'toc-u4-a':{name:'Unary incrementer transition count',unit:4,label:'transition steps',note:'Deterministic scanner reads n ones then performs a write-halt transition, n+1 steps in this convention.',fn:n=>n+1},
 'toc-u4-b':{name:'Finite bounded tape configurations',unit:4,label:'abstract configurations',note:'Exactly two states, n head positions, n binary tape cells: 2*n*2^n configurations. Not the unbounded TM model.',fn:n=>2*n*2**n},
 'toc-u5-a':{name:'Finite diagonal-chart cell count',unit:5,label:'cells in n-by-n chart',note:'A finite illustration of positions in a diagonal argument; does NOT solve or prove the halting theorem.',fn:n=>n*n},
 'toc-u5-b':{name:'Binary machine-description prefix space',unit:5,label:'bitstrings through length n',note:'Counts binary strings of length 0..n, including strings that are NOT valid machine descriptions.',fn:n=>2**(n+1)-1},
 'toc-u6-a':{name:'SAT Boolean assignment search space',unit:6,label:'assignments to n variables',note:'Exactly n independent Boolean variables, exhaustive 2^n candidate assignments before any pruning.',fn:n=>2**n},
 'toc-u6-b':{name:'Pairwise witness consistency checks',unit:6,label:'unordered pairs',note:'n distinct certificate entries; checking every unordered pair gives n(n-1)/2, not universal NP verification cost.',fn:n=>n*(n-1)/2},
 'toc-u7-a':{name:'Independent one-sided error bound',unit:7,label:'percent',note:'Assumes independent repeated trials and a specific one-sided all-positive decision rule, each with error at most 1/3; NOT two-sided majority error.',fn:n=>100*(1/3)**n},
 'toc-u7-b':{name:'Toy fixed-parameter search work',unit:7,label:'work units',note:'Assumes cost n*2^n for parameter k=n and polynomial factor n; illustrates growth, not observed vertex-cover runtime.',fn:n=>n*2**n},
 'toc-u8-a':{name:'Two-component product-state bound',unit:8,label:'Cartesian product states',note:'Component A has exactly three states and B exactly n states. 3n possible global states; some may be unreachable.',fn:n=>3*n},
 'toc-u8-b':{name:'Finite directed-chain reachability',unit:8,label:'reachable states',note:'Initial node 0 and directed edges i→i+1 for i=0..n-1, so n+1 reachable states. Does not describe arbitrary graphs.',fn:n=>n+1}
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
root.OpenSTEMModel={book:'theory-of-computation',types:Object.keys(S),calculate,initSimulation};
root.SimulationEngine={...(root.SimulationEngine||{}),initSimulation};
})(typeof window==='undefined'?globalThis:window);
