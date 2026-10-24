/* OpenSTEM HCI editorial demonstrations. Illustrative toy models, not empirical human performance predictions. */
(function(root){'use strict';
const models=Object.freeze({
 'hci-u1-a':{title:'Hick–Hyman illustrative choice time',note:'T=0.25+0.15 log2(n+1) seconds; n equally likely alternatives; coefficients are illustrative, not population estimates.',label:'modeled choice time (s)'},
 'hci-u1-b':{title:'Fitts-law illustrative pointing time',note:'T=0.20+0.10 log2(1+240/(10n)) seconds; distance=240 px, target width=10n px. Fitted coefficients are illustrative.',label:'modeled pointing time (s)'},
 'hci-u2-a':{title:'Illustrative issue discovery probability',note:'P=1-(1-0.20)^n; assumes independent sessions and constant detection chance. This is NOT a participant-number rule.',label:'modeled discovery probability'},
 'hci-u2-b':{title:'Illustrative research budget',note:'Cost=150+45n+20 ceil(n/4) arbitrary units; excludes staffing and accommodations.',label:'modeled cost (units)'},
 'hci-u3-a':{title:'Toy cumulative error opportunity',note:'P=1-(1-0.03)^n; assumes independent identical per-step error probabilities. Not a human performance estimate.',label:'modeled probability of at least one error'},
 'hci-u3-b':{title:'Naive undo snapshot memory',note:'64 KiB per snapshot, without compression, deltas or metadata. n is retained snapshot count.',label:'estimated memory (KiB)'},
 'hci-u4-a':{title:'Illustrative prototype iteration effort',note:'T=120+120n+30 ceil(n/3) minutes; n is number of rounds. Budget assumptions are hypothetical, not measured team performance.',label:'estimated total effort (min)'},
 'hci-u4-b':{title:'Independent binary choice configurations',note:'2^n configurations assumes n independent binary decisions, all combinations reachable; it is not a count of real user journeys.',label:'theoretical configurations'},
 'hci-u5-a':{title:'Hypothetical task success fraction',note:'p=n/12 for n successes among exactly 12 independent constructed attempts; not a population estimate.',label:'observed fraction'},
 'hci-u5-b':{title:'Illustrative Wilson interval width',note:'95% Wilson interval width for n successes in 24 independent hypothetical Bernoulli attempts, z=1.96; sampling assumptions are restrictive.',label:'interval width'},
 'hci-u6-a':{title:'Opaque grayscale text contrast against white',note:'sRGB gray channel g=10n+20 (n=2..12); ratio 1.05/(Lgray+0.05). Contrast alone does not establish accessibility.',label:'contrast ratio to white'},
 'hci-u6-b':{title:'Clickable area around a 16px icon',note:'Square hit region with n CSS pixels of padding on each side; area=(16+2n)^2. Real target size also depends on CSS and hit testing.',label:'hit area (CSS px squared)'},
 'hci-u7-a':{title:'Toy physical sensor normalization',note:'Sensor reading s=100+60n, calibrated interval [100,900]; normalized (s-100)/800. This does not model sensor noise.',label:'normalized position'},
 'hci-u7-b':{title:'Illustrative speech word error rate',note:'WER=n/40 for n hypothetical word errors among 40 reference words; no prediction of conversational task success.',label:'word error rate'},
 'hci-u8-a':{title:'Illustrative event retention footprint',note:'240 constructed event records per day, retained for n days; excludes storage overhead and all privacy-law considerations.',label:'retained records'},
 'hci-u8-b':{title:'Possible unordered collaboration pairs',note:'C(n,2)=n(n-1)/2 potential pairs; not a model of actual editing conflicts.',label:'potential pairs'}
});
function calculate(id,n){
 if(!Object.prototype.hasOwnProperty.call(models,id))throw new RangeError('unknown model');
 if(!Number.isInteger(n)||n<2||n>12)throw new RangeError('n must be an integer from 2 to 12');
 if(id==='hci-u1-a')return .25+.15*Math.log2(n+1);
 if(id==='hci-u1-b')return .20+.10*Math.log2(1+240/(10*n));
 if(id==='hci-u2-a')return 1-Math.pow(.8,n);
 if(id==='hci-u2-b')return 150+45*n+20*Math.ceil(n/4);
 if(id==='hci-u3-a')return 1-Math.pow(.97,n);
 if(id==='hci-u3-b')return 64*n;
 if(id==='hci-u4-a')return 120+120*n+30*Math.ceil(n/3);
 if(id==='hci-u4-b')return Math.pow(2,n);
 if(id==='hci-u5-a')return n/12;
 if(id==='hci-u5-b'){const N=24,z=1.96,p=n/N,d=1+z*z/N;return 2*z*Math.sqrt(p*(1-p)/N+z*z/(4*N*N))/d;}
 if(id==='hci-u6-a'){const c=(10*n+20)/255;const L=c<=0.04045?c/12.92:Math.pow((c+0.055)/1.055,2.4);return 1.05/(L+0.05);}
 if(id==='hci-u6-b')return Math.pow(16+2*n,2);
 if(id==='hci-u7-a')return (60*n)/800;
 if(id==='hci-u7-b')return n/40;
 if(id==='hci-u8-a')return 240*n;
 if(id==='hci-u8-b')return n*(n-1)/2;
 throw new Error('unreachable');
}
function init(id,containerId){
 const el=document.getElementById(containerId);if(!el)throw new Error('missing container');
 const m=models[id];if(!m)throw new Error('unknown model');
 const h=document.createElement('h3');h.textContent=m.title;
 const p=document.createElement('p');p.textContent=m.note;
 const label=document.createElement('label');label.textContent='Parameter n: ';
 const input=document.createElement('input');input.type='range';input.min='2';input.max='12';input.step='1';input.value='6';input.setAttribute('aria-label',m.title+' parameter n');label.appendChild(input);
 const output=document.createElement('output');output.setAttribute('aria-live','polite');
 const reset=document.createElement('button');reset.type='button';reset.textContent='Reset';
 const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.setAttribute('viewBox','0 0 320 110');svg.setAttribute('role','img');svg.setAttribute('aria-label',m.title+' response curve');
 const line=document.createElementNS('http://www.w3.org/2000/svg','polyline');line.setAttribute('fill','none');line.setAttribute('stroke','#226b91');line.setAttribute('stroke-width','3');svg.appendChild(line);
 const point=document.createElementNS('http://www.w3.org/2000/svg','circle');point.setAttribute('r','5');point.setAttribute('fill','#a34424');svg.appendChild(point);
 const vals=Array.from({length:11},(_,i)=>calculate(id,i+2));const lo=Math.min(...vals),hi=Math.max(...vals);const y=v=>95-75*(v-lo)/(hi-lo);const x=n=>15+(n-2)*29;
 line.setAttribute('points',vals.map((v,i)=>`${x(i+2)},${y(v)}`).join(' '));
 function render(){const n=Number(input.value),v=calculate(id,n);output.textContent=`n = ${n}; ${m.label} = ${v.toFixed(6)}`;point.setAttribute('cx',String(x(n)));point.setAttribute('cy',String(y(v)));}
 input.addEventListener('input',render);reset.addEventListener('click',()=>{input.value='6';render();});
 el.append(h,p,label,output,reset,svg);render();return {input,output,reset,svg};
}
const api=Object.freeze({calculate,init,models});if(typeof module!=='undefined'&&module.exports)module.exports=api;root.HCISimulations=api;
})(typeof window!=='undefined'?window:globalThis);

/* SimulationEngine adapter for Human-Computer Interaction */
(function(root){
  if (typeof document !== 'undefined') {
    var previous = root.SimulationEngine && root.SimulationEngine.initSimulation;
    root.SimulationEngine = root.SimulationEngine || {};
    root.SimulationEngine.initSimulation = function(containerId, simType) {
      if (root.HCISimulations && root.HCISimulations.models && root.HCISimulations.models[simType]) {
        return root.HCISimulations.init(simType, containerId);
      }
      if (typeof previous === 'function') {
        return previous.call(this, containerId, simType);
      }
    };
  }
})(typeof window !== 'undefined' ? window : globalThis);
