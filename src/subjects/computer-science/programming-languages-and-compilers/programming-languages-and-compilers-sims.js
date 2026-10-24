/* Original OpenSTEM Programming Languages and Compilers simulations.
   Each numeric model is a deliberately simplified, bounded illustration.
   Not an executable parser, compiler, or empirical performance estimator. */
(function(root){'use strict';
const SPEC={
 'plc-u1-a':{name:'Lexical environment-chain search',label:'maximum inspected frames',unit:1,note:'An unindexed chain of n lexical frames searched from inner to outer; worst case visits all n. Real resolvers may precompute lexical addresses or use maps.',fn:n=>n},
 'plc-u1-b':{name:'Call-by-name duplicate evaluations',label:'extra evaluations beyond shared thunk',unit:1,note:'An expression is used exactly n times: call-by-name evaluates n times; call-by-need once if demanded. Difference n-1 assumes success and memoization.',fn:n=>n-1},
 'plc-u2-a':{name:'Unification of a type-variable chain',label:'equality links',unit:2,note:'n fresh variables linked into a chain produce n-1 equality links. This counts one toy constraint family, not general inference complexity.',fn:n=>n-1},
 'plc-u2-b':{name:'Possible pairwise type comparisons',label:'unordered symbol pairs',unit:2,note:'Complete pairwise comparisons among n distinct candidate types: n(n-1)/2. Real type checkers avoid brute force in many cases.',fn:n=>n*(n-1)/2},
 'plc-u3-a':{name:'Ambiguous binary-expression parses',label:'Catalan parse trees',unit:3,note:'Catalan(n) parenthesizations of n binary operators and n+1 operands under an ambiguous binary grammar. No precedence rules are enforced.',fn:n=>{let c=1;for(let k=0;k<n;k++)c=c*2*(2*k+1)/(k+2);return Math.round(c)}},
 'plc-u3-b':{name:'Nested parentheses token length',label:'tokens',unit:3,note:'Expression has n left parentheses, one identifier, n right parentheses: 2n+1 tokens. Nesting may encounter parser recursion limits.',fn:n=>2*n+1},
 'plc-u4-a':{name:'SSA phi incoming operands',label:'phi operands',unit:4,note:'A join block with exactly n incoming predecessor edges requires n tagged phi operands for a value that differs by edge.',fn:n=>n},
 'plc-u4-b':{name:'Maximum edges in a directed acyclic sequence',label:'forward edges',unit:4,note:'n ordered blocks may each link to any later block, yielding n(n-1)/2 forward edges. Real CFGs use sparse structured branches.',fn:n=>n*(n-1)/2},
 'plc-u5-a':{name:'Toy tracing collector reclamation',label:'unreachable objects',unit:5,note:'Assumes 4n allocated objects, exactly n reachable from roots, no external roots; mark-sweep reclaims 3n. Not a prediction for a real heap.',fn:n=>3*n},
 'plc-u5-b':{name:'Pure reference-counting retained cycle',label:'unreachable objects not reclaimed',unit:5,note:'An isolated directed cycle of n objects has one strong reference per node even after external roots drop; basic reference counting does not collect it.',fn:n=>n},
 'plc-u6-a':{name:'Safe constant-expression fold',label:'expression value',unit:6,note:'Exact mathematical-integer expression 2*n+5, with fixed n and no side effects. Overflow or trapping source semantics require separate analysis.',fn:n=>2*n+5},
 'plc-u6-b':{name:'Loop-invariant work reduction',label:'arithmetic evaluations avoided',unit:6,note:'Pure invariant subexpression evaluated once instead of n times in a guaranteed n-iteration loop; saves n-1 evaluations.',fn:n=>n-1},
 'plc-u7-a':{name:'Register pressure above eight registers',label:'concurrent values over capacity',unit:7,note:'n simultaneously live values, exactly eight compatible registers. Pressure excess is max(0,n-8), not exact runtime spill traffic.',fn:n=>Math.max(0,n-8)},
 'plc-u7-b':{name:'Toy aligned stack-frame padding',label:'padding bytes',unit:7,note:'n eight-byte local slots plus eight bytes saved state; round total to a 16-byte multiple. Hypothetical teaching ABI, not a real platform rule.',fn:n=>(16-((8*n+8)%16))%16},
 'plc-u8-a':{name:'Linear stack-VM instruction count',label:'toy bytecode instructions',unit:8,note:'Exactly n independent binary expressions, three instructions each plus one return: 3n+1; sharing and control flow change real counts.',fn:n=>3*n+1},
 'plc-u8-b':{name:'Interpreter versus JIT dispatch-cost illustration',label:'toy interpreted cost minus JIT cost',unit:8,note:'Pure illustrative units: interpreter cost 5n; JIT warm-up 30 plus 2n. Difference 3n-30; negative favors interpreter, positive JIT. Not a benchmark.',fn:n=>3*n-30}
};
function calculate(type,n){
 if(!Object.prototype.hasOwnProperty.call(SPEC,type))throw new RangeError('Unknown simulation type');
 if(!Number.isInteger(n)||n<2||n>16)throw new RangeError('n must be an integer between 2 and 16');
 const t=SPEC[type],v=t.fn(n);
 if(!Number.isFinite(v))throw new RangeError('Nonfinite output');
 return {type,n,value:v,name:t.name,unit:t.unit,unitLabel:t.label,notes:t.note};
}
function initSimulation(elementId,type){
 if(typeof document==='undefined')return false;
 const el=document.getElementById(elementId);
 if(!el||!Object.prototype.hasOwnProperty.call(SPEC,type))return false;
 el.replaceChildren();
 const title=document.createElement('h3');title.textContent=SPEC[type].name;
 const label=document.createElement('label');label.textContent='Input n (2–16): ';
 const slider=document.createElement('input');slider.type='range';slider.min='2';slider.max='16';slider.step='1';slider.value='6';slider.setAttribute('aria-label','Input for '+SPEC[type].name);label.append(slider);
 const output=document.createElement('output');output.setAttribute('role','status');output.setAttribute('aria-live','polite');output.style.display='block';output.style.padding='.5rem 0';
 const assumptions=document.createElement('p');
 const reset=document.createElement('button');reset.type='button';reset.textContent='Reset simulation';
 const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.setAttribute('viewBox','0 0 360 165');svg.setAttribute('role','img');svg.setAttribute('aria-label','Illustrative model outputs for all input values from 2 to 16');svg.style.width='100%';svg.style.maxWidth='560px';
 const render=()=>{
  const n=Number(slider.value),v=calculate(type,n);output.textContent='Input n = '+n+'; output '+Number(v.value.toPrecision(9))+' '+v.unitLabel;
  assumptions.textContent='Model assumptions and limits: '+v.notes;
  svg.replaceChildren();const a=Array.from({length:15},(_,i)=>calculate(type,i+2));
  const min=Math.min(0,...a.map(x=>x.value)), max=Math.max(0,...a.map(x=>x.value)),rng=Math.max(max-min,1e-9),base=10+130*max/rng;
  a.forEach((pt,i)=>{const y=10+130*(max-pt.value)/rng;const rect=document.createElementNS('http://www.w3.org/2000/svg','rect');rect.setAttribute('x',String(8+i*23));rect.setAttribute('y',String(Math.min(y,base)));rect.setAttribute('height',String(Math.max(2,Math.abs(y-base))));rect.setAttribute('width','16');rect.setAttribute('rx','2');rect.setAttribute('fill',pt.n===n?'#df9a37':'#397da0');let tooltip=document.createElementNS('http://www.w3.org/2000/svg','title');tooltip.textContent='n='+pt.n+', output='+pt.value;rect.append(tooltip);svg.append(rect) });
 };
 slider.addEventListener('input',render);reset.addEventListener('click',()=>{slider.value='6';render()});el.append(title,label,output,svg,assumptions,reset);render();return true;
}
root.OpenSTEMModel={book:'programming-languages-and-compilers',types:Object.keys(SPEC),calculate,initSimulation};
root.SimulationEngine={...(root.SimulationEngine||{}),initSimulation};
})(typeof window==='undefined'?globalThis:window);
