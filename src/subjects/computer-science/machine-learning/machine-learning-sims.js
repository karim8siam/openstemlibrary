/* Original OpenSTEM Machine Learning simulations: bounded quantitative teaching models; unpublished editorial draft. */

(function(root){'use strict';
const S={
 'ml-u1-a':{name:'Holdout training examples',unit:1,label:'train observations',note:'A synthetic sample has 100n rows and a fixed 80% training portion; ignores stratification, grouping and temporal dependence.',fn:n=>80*n},
 'ml-u1-b':{name:'Mean squared residuals of integers',unit:1,label:'mean squared residual units',note:'Residuals equal 1,2,...,n; MSE is sum of squares divided by n, not a fitted model result.',fn:n=>(n+1)*(2*n+1)/6},
 'ml-u2-a':{name:'Logistic sigmoid score',unit:2,label:'predicted positive probability',note:'One synthetic logit z=(n/4)-2. The sigmoid maps z to (0,1) but is not evidence of calibration.',fn:n=>1/(1+Math.exp(-(n/4-2)))},
 'ml-u2-b':{name:'One-feature ridge shrinkage',unit:2,label:'fitted coefficient',note:'Normalized XTX/n=1, XTy/n=n, ridge lambda=2, intercept excluded; beta=n/(1+2), not a universal ridge prediction.',fn:n=>n/3},
 'ml-u3-a':{name:'Distinct training pairs',unit:3,label:'unordered pairs',note:'n distinct observations imply n(n-1)/2 unordered pairs; not the number of nearby neighbors for a metric.',fn:n=>n*(n-1)/2},
 'ml-u3-b':{name:'Gaussian kernel similarity',unit:3,label:'kernel similarity',note:'Distance is n/10 in one dimension and Gaussian gamma=1: exp(-distance squared). No feature scaling is learned.',fn:n=>Math.exp(-(n*n)/100)},
 'ml-u4-a':{name:'Two-point squared-error cluster',unit:4,label:'within-cluster squared error',note:'Two scalar points at 0 and n share one centroid n/2. SSE=2(n/2)^2=n^2/2.',fn:n=>n*n/2},
 'ml-u4-b':{name:'Simplified PCA explained variance',unit:4,label:'percent explained variance',note:'Two covariance eigenvalues n and 4. Larger eigenvalue is first only if n>=4; for n=2,3 the leading PC would be 4.',fn:n=>100*Math.max(n,4)/(n+4)},
 'ml-u5-a':{name:'Dense hidden layer parameter count',unit:5,label:'trainable parameters',note:'n input features, 10 fully connected hidden units, 10 biases: 10n+10, excluding outputs and optimizer state.',fn:n=>10*(n+1)},
 'ml-u5-b':{name:'Attention pair-score count',unit:5,label:'query-key scores',note:'Full attention over n tokens forms n² pair scores per head; excludes masks, batching and kernel optimizations.',fn:n=>n*n},
 'ml-u6-a':{name:'Nonterminal Q-learning update',unit:6,label:'updated action value',note:'Current Q=2, reward=3, next-state best Q=n, alpha=0.1, gamma=0.9; terminal transitions differ.',fn:n=>2+0.1*(3+0.9*n-2)},
 'ml-u6-b':{name:'Expected bandit regret',unit:6,label:'expected regret units',note:'Each inferior-arm choice costs 0.2 expected reward. Input n counts such choices; stationary oracle comparison.',fn:n=>n*0.2},
 'ml-u7-a':{name:'Rare-event precision',unit:7,label:'percent positive predictive value',note:'Prevalence n/100, sensitivity=0.9 and false-positive rate=0.05; Bayes identity, not a measured classifier.',fn:n=>{const p=n/100;return 100*(.9*p)/(.9*p+.05*(1-p));}},
 'ml-u7-b':{name:'Single-positive Brier error',unit:7,label:'squared probability error',note:'True label y=1 and predicted probability p=n/20. Binary Brier term (p-1)^2, not population calibration.',fn:n=>(1-n/20)**2},
 'ml-u8-a':{name:'Unit-conversion scale mismatch',unit:8,label:'standardized input units',note:'True Celsius = n but serving client sends Fahrenheit 1.8n+32; incorrect z=(F-20)/5; correct z=(n-20)/5.',fn:n=>(1.8*n+32-20)/5},
 'ml-u8-b':{name:'Batch inference budget',unit:8,label:'milliseconds in model',note:'Simplified latency 10 ms fixed overhead plus 2 ms per item. Ignores queueing, batch hardware and network effects.',fn:n=>10+2*n}
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
root.OpenSTEMModel={book:'machine-learning',types:Object.keys(S),calculate,initSimulation};
root.SimulationEngine={...(root.SimulationEngine||{}),initSimulation};
})(typeof window==='undefined'?globalThis:window);
