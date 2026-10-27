/* model-theory-and-mathematical-semantics Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [
  {
    "idx": 1,
    "unit": 1,
    "title": "Finite-structure satisfaction",
    "desc": "Compute truth conditions for a directed relation E on a bounded finite domain.",
    "type": "graph",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 2,
    "unit": 1,
    "title": "Term assignment evaluator",
    "desc": "Evaluate the successor term f(f(x)) in modular arithmetic.",
    "type": "terms",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 3,
    "unit": 2,
    "title": "Isomorphism by relabeling",
    "desc": "Transport graph edges through a vertex permutation and check invariance.",
    "type": "iso",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 4,
    "unit": 2,
    "title": "Substructure closure",
    "desc": "Test a subset for closure under an arithmetic operation.",
    "type": "closure",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 5,
    "unit": 3,
    "title": "Homomorphism versus embedding",
    "desc": "Compare a relation-preserving collapse with an injective embedding.",
    "type": "hom",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 6,
    "unit": 3,
    "title": "Reduct and expansion",
    "desc": "Add or forget a unary predicate and compare sentences.",
    "type": "reduct",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 7,
    "unit": 4,
    "title": "Automorphism orbit explorer",
    "desc": "Check which vertices a rotational symmetry can distinguish.",
    "type": "orbit",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 8,
    "unit": 4,
    "title": "Quantifier-rank calculator",
    "desc": "Compare quantifier nesting ranks in a small formula catalogue.",
    "type": "rank",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 9,
    "unit": 5,
    "title": "Semantic entailment table",
    "desc": "Audit the entailment of Q from P and P\u2192Q.",
    "type": "entail",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 10,
    "unit": 5,
    "title": "Equivalence-class model",
    "desc": "Partition a finite domain by congruence modulo a chosen divisor.",
    "type": "equiv",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 11,
    "unit": 6,
    "title": "Countermodel generator",
    "desc": "Construct the smallest asymmetric directed-graph countermodel.",
    "type": "counter",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 12,
    "unit": 6,
    "title": "Compactness prefix builder",
    "desc": "Satisfy finite prefixes of an infinite distinct-constant theory.",
    "type": "compact",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 13,
    "unit": 7,
    "title": "Witness closure sampler",
    "desc": "Observe witness loss when a finite subset excludes successor values.",
    "type": "witness",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 14,
    "unit": 7,
    "title": "Partial-type satisfiability",
    "desc": "Look for witnesses above finitely many thresholds in a bounded order.",
    "type": "type",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 15,
    "unit": 8,
    "title": "One- and two-round EF example",
    "desc": "Distinguish equality-only domains by a bounded number of rounds.",
    "type": "ef",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  },
  {
    "idx": 16,
    "unit": 8,
    "title": "Graph integrity query",
    "desc": "Check whether each node has an outgoing neighbor and show failures.",
    "type": "query",
    "controls": "<div class=\"sim-controls\"><label>Domain / bound n <input id=\"n\" aria-label=\"Domain size or bound\" type=\"number\" min=\"2\" max=\"8\" value=\"5\"></label><label>Parameter a <input id=\"a\" aria-label=\"Parameter a\" type=\"number\" min=\"0\" max=\"40\" value=\"2\"></label><label>Parameter b <input id=\"b\" aria-label=\"Parameter b\" type=\"number\" min=\"0\" max=\"40\" value=\"1\"></label><button id=\"rerun\" type=\"button\">Calculate</button></div>"
  }
];

  // Original calculation logic adapted for scoped execution
"use strict";
(function(){
 const tf=x=>x?'TRUE':'FALSE';
 const range=n=>Array.from({length:n},(_,i)=>i);
 const mod=(a,n)=>((a%n)+n)%n;
 const formatEdges=e=>e.map(([x,y])=>`(${x},${y})`).join(', ')||'∅';
 function calculate(kind,n,a,b){
  n=Math.max(2,Math.min(8,Math.trunc(n)||3));
  a=Math.max(0,Math.min(40,Math.trunc(a)||0));
  b=Math.max(0,Math.min(40,Math.trunc(b)||0));
  const D=range(n),edges=D.map(x=>[x,mod(x+a+1,n)]);
  switch(kind){
   case 'graph':{
    const E=D.map(x=>[x,mod(x+a+1,n)]).filter((_,i)=>i!==b%n);
    const each=D.every(x=>E.some(([u])=>u===x));
    const symmetric=E.every(([u,v])=>E.some(([x,y])=>x===v&&y===u));
    return {title:'Satisfaction in a finite graph',rows:[`Domain D={${D.join(', ')}}`,`E={${formatEdges(E)}}`,`∀x∃y E(x,y): ${tf(each)}`,`∀xy (E(x,y)→E(y,x)): ${tf(symmetric)}`,`Outgoing-edge counterexamples: ${D.filter(x=>!E.some(([u])=>u===x)).join(', ')||'none'}`]};}
   case 'terms':{const x=mod(a,n),f=k=>mod(k+1,n);return {title:'Term evaluation (f is modular successor)',rows:[`D={${D.join(', ')}}; assignment s(x)=${x}`,`f(x)=${f(x)}`,`f(f(x))=${f(f(x))}`,`Constant c interpreted as ${mod(b,n)}`,`f(f(c))=${f(f(mod(b,n)))}`,`These denotations are relative to this interpretation, not general arithmetic.`]};}
   case 'iso':{const shift=mod(a+1,n),p=x=>mod(x+shift,n),old=edges,transport=old.map(([u,v])=>[p(u),p(v)]),wrong=old.map(([u,v])=>[p(u),v]);return {title:'Relation transport under a bijection',rows:[`Permutation p(x)=x+${shift} (mod ${n})`,`Original directed edges: ${formatEdges(old)}`,`Transported edges: ${formatEdges(transport)}`,`An isomorphism exists by construction: TRUE`,`Edges after relabeling sources only: ${formatEdges(wrong)}`,`Relabeling only one coordinate need not preserve the original relation.`]};}
   case 'closure':{const m=Math.max(1,(a%4)+1),S=D.filter(x=>x%m===0),fail=[];for(const x of S)for(const y of S)if(!S.includes(mod(x+y,n)))fail.push([x,y]);return {title:'Substructure under addition mod n',rows:[`Domain Z/${n}Z; subset S={${S.join(',')}}`,`Operation: x+y (mod ${n})`,`Closed under binary addition: ${tf(!fail.length)}`,`First counterexample: ${fail.length?`${fail[0][0]}+${fail[0][1]} mod ${n} ∉ S`:'none'}`,`Contains named constant 0: ${tf(S.includes(0))}`,`This check does not test any additional symbols beyond the stated signature.`]};}
   case 'hom':{const A=[0,1],E=[[0,0],[1,1]],f=x=>0,T=[[0,0]];return {title:'Noninjective relation-preserving map',rows:[`Source relation E={(0,0),(1,1)}; target F={(0,0)}`,`Map f(0)=0, f(1)=0`,`All E edges map to F edges: TRUE`,`Injective: FALSE`,`Can this map be an embedding? FALSE`,`Identity equality distinguishes the two source elements; preservation of some positive relations is insufficient.`]};}
   case 'reduct':{const selected=D.filter(x=>x%2===(a%2));return {title:'Adding a predicate symbol',rows:[`Pure equality domain: ${n} objects`,`Expansion adds P interpreted as ${selected.length?'{'+selected.join(',')+'}':'∅'}`,`Expanded sentence ∃x P(x): ${tf(selected.length>0)}`,`Expanded sentence ∀x P(x): ${tf(selected.length===n)}`,`After taking the reduct to equality alone, neither formula with P belongs to the language.`]};}
   case 'orbit':{const step=mod(a+1,n),seen=new Set();let x=mod(b,n);while(!seen.has(x)){seen.add(x);x=mod(x+step,n);}return {title:'Orbit under a rotation of a cyclic graph',rows:[`Vertices 0,…,${n-1}; rotate by ${step} (mod ${n})`,`Starting vertex: ${mod(b,n)}`,`Automorphism orbit: {${[...seen].join(',')}}`,`Orbit size: ${seen.size}`,`Any parameter-free unary definable subset must be a union of complete automorphism orbits.`,`A union of orbits is not automatically definable in arbitrary structures.`]};}
   case 'rank':{const k=mod(a,3),expr=['P(x) ∧ Q(y)','∀x(P(x)→∃y E(x,y))','∀x∃y∀z R(x,y,z)'][k],rk=[0,2,3][k];return {title:'Quantifier rank (maximum nesting)',rows:[`Selected formula: ${expr}`,`Quantifier rank: ${rk}`,`A conjunction takes the maximum rank of its two operands.`,`Negation leaves rank unchanged.`,`A new quantifier around this formula raises rank to ${rk+1}.`,`Formula character length is not quantifier rank.`]};}
   case 'entail':{let rows=[];for(const p of [false,true])for(const q of [false,true]){const imp=!p||q,pre=p&&imp;rows.push(`P=${tf(p)}, Q=${tf(q)}, P→Q=${tf(imp)}, both premises=${tf(pre)}, violating Q=${tf(pre&&!q)}`);}return {title:'Truth-table entailment',rows:[...rows,'Countermodels to {P,P→Q}⊨Q: 0.','The table proves entailment for the propositional valuations of these two atoms.']};}
   case 'equiv':{const k=Math.max(1,Math.min(n,(a%5)+1)),groups=range(k).map(i=>D.filter(x=>x%k===i)).filter(xs=>xs.length);return {title:'Congruence classes as a finite equivalence relation',rows:[`Domain {${D.join(',')}}`, `Relation xEy iff x≡y (mod ${k})`,`Classes: ${groups.map(x=>'{'+x.join(',')+'}').join(' | ')}`,`Reflexive: TRUE; symmetric: TRUE; transitive: TRUE.`,`Number of classes: ${groups.length}`,`No constraint here forces the same number of classes in every model of the abstract equivalence axioms.`]};}
   case 'counter':{const E=[[0,1]],reverse=E.some(([u,v])=>u===1&&v===0);return {title:'A checked asymmetry countermodel',rows:[`Structure D={0,1}, E={(0,1)}`,`E(0,1): TRUE; E(1,0): ${tf(reverse)}`,`Sentence ∀xy(E(x,y)→E(y,x)): FALSE`,`Witnesses x=0, y=1 refute symmetry.`,`Changing the number of unused isolated vertices cannot repair this specific failure.`]};}
   case 'compact':{const count=Math.max(2,n+a%5),names=range(count).map(i=>'c'+i);return {title:'Finite prefix of distinctness requirements',rows:[`Selected prefix length: ${count}`,`Constants: ${names.join(', ')}`,`Number of inequalities required: ${count*(count-1)/2}`,`A domain of size ${count} satisfies this finite prefix by interpreting each name distinctly.`,`The infinite collection of all pairwise inequalities requires an infinite model.`,`The interactive finite prefix does not prove compactness; the theorem supplies the global model.`]};}
   case 'witness':{const S=D.filter(x=>x<Math.max(1,n-1)),bad=S.filter(x=>x+1<n&&!S.includes(x+1));return {title:'Finite witness-closure warning',rows:[`Ambient domain D={${D.join(',')}}`,`Chosen subset S={${S.join(',')}}`,`Relation E(x,y): y=x+1 (within D)`,`Elements of S with an E-witness in D but not in S: ${bad.join(',')||'none'}`,`A missing witness refutes elementarity for the appropriate existential formula and parameter.`,`Passing this one predicate test cannot prove full elementarity.`]};}
   case 'type':{const threshold=Math.min(n-1,a%Math.max(2,n)),hits=D.filter(x=>x>threshold);return {title:'Realizing a finite partial type',rows:[`Domain D={${D.join(',')}}`,`Finite requirement: x>${threshold}`,`Realizing elements: ${hits.join(',')||'none'}`,`Finitely many inequalities may be realized in a sufficiently large extension.`,`An infinite type such as {x>k:k∈N} has no witness in N itself.`,`This bounded test does not construct a complete elementary extension.`]};}
   case 'ef':{const m=Math.max(1,Math.min(n,a%6+1)),k=Math.max(1,Math.min(n,b%6+1)),rounds=1+(a%2);const same=(r=rounds)=>m>=r&&k>=r || m===k && Math.min(m,k)<r;return {title:'Equality-only EF-game illustration',rows:[`Structures of sizes ${m} and ${k}, language {=} only`,`Rounds: ${rounds}`,`Duplicator has a winning strategy: ${tf(same())}`,`If both sets have at least ${rounds} elements, preserve equality patterns on chosen points.`,`If one has fewer than ${rounds} elements and the other has at least ${rounds}, Spoiler can distinguish them.`,`Winning finitely many rounds does not imply agreement on sentences of all quantifier ranks.`]};}
   case 'query':{const E=edges.filter(([x,y])=>x!==b%n),empty=D.filter(x=>!E.some(([u])=>u===x));return {title:'Finite graph integrity query',rows:[`Domain vertices: ${n}; E={${formatEdges(E)}}`,`Sentence: ∀x∃y E(x,y)`,`Integrity check: ${tf(!empty.length)}`,`Vertices violating constraint: ${empty.join(',')||'none'}`,`Each listed vertex is a concrete counterexample to the sentence.`,`A correct database calculation does not prove the dataset describes every real entity.`]};}
  }
  return {title:'Unknown model',rows:[]};
 }
 if(typeof module!=='undefined'&&module.exports){module.exports={calculate};return;}
 function display(){
 const mode=document.body.dataset.kind;
 const num=id=>Number(document.getElementById(id).value);
 const result=calculate(mode,num('n'),num('a'),num('b'));
 const out=document.getElementById('output');out.replaceChildren();
 const h=document.createElement('h2');h.textContent=result.title;out.append(h);
 const ol=document.createElement('ol');for(const row of result.rows){const li=document.createElement('li');li.textContent=row;ol.append(li);}out.append(ol);
 }
 for(const id of ['n','a','b'])document.getElementById(id)?.addEventListener('input',display);
 document.getElementById('rerun')?.addEventListener('click',display);
 display();
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
