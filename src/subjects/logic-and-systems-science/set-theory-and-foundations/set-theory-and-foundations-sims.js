/* set-theory-and-foundations Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [
  {
    "idx": 1,
    "unit": 1,
    "title": "Membership versus subset",
    "desc": "Check element membership and subset containment separately.",
    "type": "member",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 2,
    "unit": 1,
    "title": "Finite set operations",
    "desc": "Compute union, intersection, differences, and complements in a declared universe.",
    "type": "operations",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 3,
    "unit": 2,
    "title": "Relation property tester",
    "desc": "Check reflexivity, symmetry, antisymmetry and transitivity of a 3-object relation.",
    "type": "relation",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 4,
    "unit": 2,
    "title": "Finite function inspector",
    "desc": "Inspect the images, injectivity and surjectivity of modular maps.",
    "type": "function",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 5,
    "unit": 3,
    "title": "Induction calculation audit",
    "desc": "Check a closed form against a finite sum and state why induction is still needed.",
    "type": "induction",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 6,
    "unit": 3,
    "title": "Recursion trace",
    "desc": "Trace factorial and a recurrence through finite steps.",
    "type": "recursion",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 7,
    "unit": 4,
    "title": "Matching naturals with evens",
    "desc": "See injectivity and coverage of a restricted initial finite sample.",
    "type": "bijection",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 8,
    "unit": 4,
    "title": "Rational diagonal enumeration",
    "desc": "Enumerate reduced positive fractions by bounded diagonal level.",
    "type": "rationals",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 9,
    "unit": 5,
    "title": "Binary stream diagonal",
    "desc": "Construct an n-coordinate diagonal string missing from n sample rows.",
    "type": "diagonal",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 10,
    "unit": 5,
    "title": "Cantor powerset witness",
    "desc": "Construct D={i:i\u2209f(i)} for a proposed finite map into subsets.",
    "type": "cantor",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 11,
    "unit": 6,
    "title": "Order type: \u03c9+1 versus 1+\u03c9",
    "desc": "Inspect why a greatest new point changes an infinite well-order type.",
    "type": "ordinals",
    "controls": "<div class=\"sim-controls\"><label>Finite preview length (1\u20136) <input aria-label=\"Finite preview length\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 12,
    "unit": 6,
    "title": "Finite cumulative hierarchy",
    "desc": "Compute cardinalities of the first few power-set hierarchy stages.",
    "type": "hierarchy",
    "controls": "<div class=\"sim-controls\"><label>Finite preview length (1\u20136) <input aria-label=\"Finite preview length\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 13,
    "unit": 7,
    "title": "ZF separation on a known set",
    "desc": "Filter a fixed base set without attempting universal comprehension.",
    "type": "separation",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 14,
    "unit": 7,
    "title": "Finite axiom-operation trace",
    "desc": "Show distinct set operations and which ZF axioms justify their existence.",
    "type": "axioms",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 15,
    "unit": 8,
    "title": "Characteristic functions",
    "desc": "Map a finite subset to its bitstring and back without losing information.",
    "type": "characteristic",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  },
  {
    "idx": 16,
    "unit": 8,
    "title": "Graph connectivity versus adjacency",
    "desc": "Inspect direct edges and transitive path connectivity independently.",
    "type": "graph",
    "controls": "<div class=\"sim-controls\"><label>Universe size (1\u20136) <input aria-label=\"Universe size\" name=\"n\" type=\"number\" min=\"1\" max=\"6\" value=\"3\" step=\"1\"></label><label>Input A / relation bitmask / coefficient <input aria-label=\"Input a\" name=\"a\" type=\"number\" min=\"0\" max=\"511\" value=\"5\" step=\"1\"></label><label>Input B / parameter <input aria-label=\"Input b\" name=\"b\" type=\"number\" min=\"0\" max=\"511\" value=\"3\" step=\"1\"></label></div>"
  }
];

  // Original calculation logic adapted for scoped execution
"use strict";
(()=>{
const calculate=()=>{
(() => {
const inp=k=>document.querySelector('[name="'+k+'"]');
const num=(k,d=0)=>inp(k)?Number(inp(k).value):d;
const n=Math.max(1,Math.min(6,num('n',3)));
const a=Math.max(0,Math.floor(num('a',5))), b=Math.max(0,Math.floor(num('b',3)));
const idx=[...Array(n).keys()];
const mask=m=>idx.filter(i=>(m&(1<<i))!==0);
const str=s=>'{'+[...s].join(', ')+'}';
const A=mask(a),B=mask(b), setA=new Set(A),setB=new Set(B);
const eq=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
const gcd=(x,y)=>{while(y){[x,y]=[y,x%y];}return x;};
const kind=document.body.dataset.kind;
let heading='',out=[],notes='Finite example only. A valid general theorem needs a proof.';
switch(kind){
case 'member': {
 const k=b%n;heading='Element versus subset';
 out=[`Universe U=${str(idx)}`,`A=${str(A)}`,
 `${k}∈A: ${setA.has(k)}`,`{${k}}⊆A: ${setA.has(k)}`,
 `A∈P(U): true, because A⊆U.`,`The statement k∈A is type-distinct from {k}⊆A even when both truth values agree.`];
 break;}
case 'operations': {
 const U=new Set(idx),union=[...new Set([...A,...B])].sort((x,y)=>x-y),inter=A.filter(x=>setB.has(x));
 heading='Set algebra under U';out=[`U=${str(idx)}, A=${str(A)}, B=${str(B)}`,
 `A ∪ B=${str(union)}`,`A ∩ B=${str(inter)}`,`A ∖ B=${str(A.filter(x=>!setB.has(x)))}`,
 `U ∖ A=${str(idx.filter(x=>!setA.has(x)))}`,`|P(A)|=${2**A.length}`];break;}
case 'relation': {
 let m=3, R=[...Array(m)].map((_,i)=>[...Array(m)].map((_,j)=>((a>>(i*3+j))&1)===1));
 let refl=R.every((r,i)=>r[i]),sym=R.every((r,i)=>r.every((v,j)=>!v||R[j][i]));
 let antisym=R.every((r,i)=>r.every((v,j)=>i===j||!(v&&R[j][i])));
 let trans=R.every((r,i)=>r.every((v,j)=>!v||R[j].every((w,k)=>!w||R[i][k])));
 heading='Relation axioms';out=[`Domain={0,1,2}, encoded pairs=${R.flatMap((r,i)=>r.flatMap((v,j)=>v?['('+i+','+j+')']:[])).join(' ')||'none'}`,
 `Reflexive: ${refl}`,`Symmetric: ${sym}`,`Antisymmetric: ${antisym}`,`Transitive: ${trans}`,
 `Equivalence relation: ${refl&&sym&&trans}`,`Partial order: ${refl&&antisym&&trans}`];break;}
case 'function': {
 const fn=i=>(a*i+b)%n, vals=idx.map(fn),inj=new Set(vals).size===n,surj=idx.every(y=>vals.includes(y));
 heading='Function map f(i)=(a·i+b) mod n';out=[`n=${n}, a=${a}, b=${b}`,
 ...idx.map(i=>`f(${i})=${fn(i)}`),`Injective: ${inj}`,`Surjective: ${surj}`,
 `Finite equal-size domain/codomain: injective ⇔ surjective. This conclusion does not generalize to all infinite endomaps.`];break;}
case 'induction': {
 const N=n+a%8, sum=N*(N+1)/2, loop=[...Array(N+1).keys()].reduce((v,k)=>v+k,0);
 heading='Natural-number identity';out=[`For N=${N}, Σ(k=0..N) k=${loop}`,`Closed form N(N+1)/2=${sum}`,`Agreement on this instance: ${loop===sum}`,
 `Base N=0: 0=0. Successor: assume S(N)=N(N+1)/2, add N+1 to obtain (N+1)(N+2)/2.`,
 `The last successor equation, not the finite numeric check, establishes the identity for all natural N.`];break;}
case 'recursion': {
 const N=Math.min(10,n+a%5),fact=[1],fib=[0,1];for(let i=1;i<=N;i++)fact.push(fact[i-1]*i);
 for(let i=2;i<=N;i++)fib.push(fib[i-1]+fib[i-2]);
 heading='Two finite recursions';out=[`n=${N}; n! trace: ${fact.join(' → ')}`,
 `Fibonacci trace: ${fib.slice(0,N+1).join(' → ')}`,
 `Factorial rule: 0!=1, (k+1)!=(k+1)k!`, `Fibonacci rule: F0=0,F1=1, F(k+2)=F(k+1)+Fk`,
 `The base and successor rules define each finite stage uniquely.`];break;}
case 'bijection': {
 const N=n+a%8;heading='Countable bijection prototype';out=[...Array(N).keys()].map(i=>`${i} ↦ ${2*i}`);
 out.push('f:N→Evens, f(k)=2k. Distinct k have distinct doubles; every nonnegative even number has a half in N.');
 out.push('This proof, rather than the finite prefix above, establishes bijectivity of the infinite sets.');break;}
case 'rationals': {
 const level=Math.min(14,Math.max(3,n+a%10)),rows=[];
 for(let s=2;s<=level;s++)for(let p=1;p<s;p++){let q=s-p;if(gcd(p,q)===1)rows.push(p+'/'+q);}
 heading='Countability via grid diagonals';out=[`Positive reduced fractions p/q with p+q≤${level}: ${rows.join(', ')}`,
 `Each (p,q) has finite positive level p+q; reduced duplicates are skipped.`,
 `Including 0 and signs gives an enumeration of all rationals, but a finite prefix is not the proof.`];break;}
case 'diagonal': {
 const N=n, rows=idx.map(i=>idx.map(j=> ((i*(a%5+1)+j*(b%5+2)+i*j)%3===0)?'1':'0').join(''));
 const diag=idx.map(i=>rows[i][i]==='1'?'0':'1').join('');heading='Diagonal binary string';
 out=rows.map((r,i)=>`Row ${i}: ${r}`);out.push(`Diagonal-flip string: ${diag}`,
 ...idx.map(i=>`Differs from row ${i} at coordinate ${i}: ${diag[i]!==rows[i][i]}`),
 'For an infinite sequence of infinite rows, the same coordinate rule proves uncountability. Here only an n×n prefix is shown.');break;}
case 'cantor': {
 const N=n, fn=i=>((a*(i+1)+b+2*i*i)>>>0)%(1<<n),D=idx.filter(i=>((fn(i)>>i)&1)===0);
 heading='Power-set surjection obstruction';out=[...idx.map(i=>`f(${i})=${str(mask(fn(i)))}`),
 `Diagonal subset D=${str(D)}`,...idx.map(i=>`D differs from f(${i}) at membership of ${i}: ${D.includes(i)!==mask(fn(i)).includes(i)}`),
 'The same formula D={x∈A:x∉f(x)} works for every set A and every attempted map f:A→P(A).'];break;}
case 'ordinals': {
 const N=n+1,head=idx.map(i=>'n'+i).join(' < ');
 heading='Order-type contrast';out=[`Preview (${n} natural positions): ${idx.join(" < ")} < … < ω; ω is greatest in ω+1.`,
 `Preview (${n} natural positions): ★ < ${idx.join(" < ")} < …; 1+ω has no greatest element.`,
 `ω+1 and 1+ω both have countably many positions but are nonisomorphic well-orders.`,
 `Replacing ω by a finite prefix makes both pictures finite and cannot prove the infinite distinction.`];break;}
case 'hierarchy': {
 const stage=Math.min(4,n),counts=[0];for(let i=0;i<stage;i++)counts.push(2**counts[i]);
 heading='Cumulative hierarchy size';out=counts.map((v,i)=>`|V${i}|=${v}`);out.push('V0=∅, V(α+1)=P(Vα), Vλ=⋃(β<λ)Vβ at limits.',
 'These values are finite starting stages only. At ω the hierarchy uses the limit union rule, not a new power set of V4.');break;}
case 'separation': {
 const even=A.filter(x=>x%2===0),odd=A.filter(x=>x%2!==0);
 heading='Restricted comprehension';out=[`Given set A=${str(A)}`,
 `E={x∈A : x is even}=${str(even)}`,
 `O={x∈A : x is odd}=${str(odd)}`,
 `E∩O=∅: ${even.every(x=>!odd.includes(x))}`,
 'The predicate selects from an existing A. It does not authorize an unrestricted set of all objects satisfying any predicate.'];break;}
case 'axioms': {
 heading='ZF basic constructions';const left=[...new Set(A)],right=[...new Set(B)];
 out=[`Given A=${str(left)}, B=${str(right)}`,
 `Pairing: {A,B} exists; two elements are sets A and B (one if A=B).`,
 `Union of {A,B}: ${str([...new Set([...A,...B])].sort((x,y)=>x-y))}`,
 `Powerset of A: ${2**A.length} members`,
 `Separation: {x∈A : x∉B}=${str(A.filter(x=>!setB.has(x)))}`,
 `The rules start with existing sets. They do not construct a universal set.`];break;}
case 'characteristic': {
 const bits=idx.map(i=>setA.has(i)?1:0),recover=idx.filter(i=>bits[i]===1);
 heading='Subsets and characteristic functions';out=[`U=${str(idx)}, A=${str(A)}`,
 `Characteristic vector χA: ${bits.join('')}`,
 `Recover A from one-bits: ${str(recover)}`,
 `Round-trip identical: ${eq(A,recover)}`,
 `For arbitrary infinite N, this map identifies P(N) with the binary sequence space {0,1}^N.`];break;}
case 'graph': {
 const m=3,R=[...Array(m)].map((_,i)=>[...Array(m)].map((_,j)=>((a>>(i*m+j))&1)===1));
 const C=R.map(row=>row.slice());for(let k=0;k<m;k++)for(let i=0;i<m;i++)for(let j=0;j<m;j++)if(C[i][k]&&C[k][j])C[i][j]=true;
 heading='Adjacency versus reachability';out=[`Directed edges: ${R.flatMap((r,i)=>r.flatMap((v,j)=>v?['('+i+','+j+')']:[])).join(' ')||'none'}`,
 `Direct edge 0→2: ${R[0][2]}`,`Positive-length path 0→2: ${C[0][2]}`,
 `Connected by any finite positive path is the transitive closure of adjacency. A direct edge need not exist.`];break;}
default:heading='Unknown model';out=['No calculation available.'];
}
const target=document.getElementById('output');
if(!target)return;
target.replaceChildren();
const title=document.createElement('h2');title.textContent=heading;target.append(title);
const ul=document.createElement('ul');for(const line of out){const li=document.createElement('li');li.textContent=line;ul.append(li);}target.append(ul);
const foot=document.createElement('p');foot.className='small';foot.textContent=notes;target.append(foot);
})();

};
document.querySelectorAll('#controls input').forEach(el=>el.addEventListener('input',calculate));
calculate();
})();


  if (!window.SimulationEngine) {
    window.SimulationEngine = {};
  }

  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId || 'sim-container');
    if (!container) return;
    container.innerHTML = '';

    var unitNum = 1;
    if (simType) {
      var m = simType.match(/(\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    } else {
      var bMatch = document.body.dataset.chapterIndex || window.location.pathname.match(/chapter-(\d+)/);
      if (bMatch) {
        unitNum = typeof bMatch === 'string' ? (parseInt(bMatch, 10) + 1) : parseInt(bMatch[1], 10);
      }
    }

    var modelsForUnit = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 2);

    modelsForUnit.forEach(function(m, idx) {
      var card = document.createElement('section');
      card.className = 'logic-sim-card';
      card.setAttribute('aria-label', m.title);
      card.id = 'sim-card-' + m.idx;

      var headerHtml = 
        '<div>' +
          '<span class="sim-tag">Unit ' + unitNum + '</span>' +
          '<span class="sim-tag">Interactive Model ' + m.idx + ' of 16</span>' +
        '</div>' +
        '<h3>' + m.title + '</h3>' +
        '<p class="sim-desc">' + m.desc + '</p>';

      var controlsContainer = document.createElement('div');
      controlsContainer.className = 'sim-controls';
      controlsContainer.innerHTML = m.controls || '<div style="color:#94a3b8;font-size:0.88rem;">Model evaluates live parameter derivations.</div>';

      var outputEl = document.createElement('div');
      outputEl.className = 'sim-output';
      outputEl.id = 'output-' + m.idx;
      outputEl.setAttribute('aria-live', 'polite');
      outputEl.innerHTML = '<div style="color:#94a3b8;font-size:0.88rem;">Evaluating local formal semantics…</div>';

      card.innerHTML = headerHtml;
      card.appendChild(controlsContainer);
      card.appendChild(outputEl);
      container.appendChild(card);

      // Scoped update runner
      function runUpdate() {
        document.body.dataset.type = m.type;
        document.body.dataset.kind = m.type;

        // Route document.querySelector / document.getElementById to local card
        var prevOutput = document.getElementById('output');
        var outputWrapper = outputEl;
        
        // Execute update if available
        if (typeof update === 'function') {
          // redirect output
          var oldOut = document.querySelector('#output');
          var tempOut = document.createElement('div');
          tempOut.id = 'output';
          document.body.appendChild(tempOut);
          
          try {
            update();
            outputWrapper.innerHTML = tempOut.innerHTML;
          } catch(e) {
            outputWrapper.innerHTML = '<p class="warn">Evaluating derivation step...</p>';
          } finally {
            tempOut.remove();
          }
        } else if (typeof calculate === 'function') {
          try {
            var num = function(name, defVal) {
              var inp = card.querySelector('[name="' + name + '"], #' + name);
              var v = inp ? Number(inp.value) : defVal;
              return Number.isFinite(v) ? v : defVal;
            };
            var res = calculate(m.type, num('n', 3), num('a', 3), num('b', 2));
            if (res && res.title && res.rows) {
              var h = '<h4 style="margin:0 0 8px;color:#38bdf8;font-size:1rem;">' + res.title + '</h4><ol>';
              res.rows.forEach(function(r) { h += '<li>' + r + '</li>'; });
              h += '</ol>';
              outputWrapper.innerHTML = h;
            }
          } catch(e) {
            outputWrapper.innerHTML = '<p class="warn">Evaluating calculation...</p>';
          }
        } else if (typeof run === 'function') {
          try {
            run();
          } catch(e) {}
        }
      }

      // Attach event listeners
      card.querySelectorAll('input, select').forEach(function(inp) {
        inp.addEventListener('input', runUpdate);
        inp.addEventListener('change', runUpdate);
      });
      var rerunBtn = card.querySelector('#rerun, button');
      if (rerunBtn) rerunBtn.addEventListener('click', runUpdate);

      // Initial run
      runUpdate();
    });
  };

  // Auto-init when DOM is ready if #sim-container is present
  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        if (document.getElementById('sim-container')) {
          window.SimulationEngine.initSimulation('sim-container');
        }
      });
    } else {
      if (document.getElementById('sim-container')) {
        window.SimulationEngine.initSimulation('sim-container');
      }
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
