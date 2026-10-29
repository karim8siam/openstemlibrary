/* proof-theory-and-deductive-systems Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [
  {
    "idx": 1,
    "unit": 1,
    "title": "Entailment truth-table audit",
    "desc": "Check whether P and P\u2192Q entail Q across a bounded set of valuations.",
    "type": "entail",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 2,
    "unit": 1,
    "title": "Certificate rule checker",
    "desc": "Toggle supplied premises and inspect one modus-ponens certificate.",
    "type": "certificate",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 3,
    "unit": 2,
    "title": "Conjunction introduction and projection",
    "desc": "Examine proof construction and two eliminations for paired evidence.",
    "type": "conjunction",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 4,
    "unit": 2,
    "title": "Implication dependency ledger",
    "desc": "Observe an assumption being introduced then discharged.",
    "type": "implication",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 5,
    "unit": 3,
    "title": "Universal finite-domain tester",
    "desc": "Compare one observed predicate value with a universal quantification.",
    "type": "universal",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 6,
    "unit": 3,
    "title": "Existential witness auditor",
    "desc": "Find a bounded witness, and explain local scope.",
    "type": "existential",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 7,
    "unit": 4,
    "title": "Sequent goal decomposition",
    "desc": "Expand an implication and conjunction goal into proof-search obligations.",
    "type": "sequent",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 8,
    "unit": 4,
    "title": "Structural context audit",
    "desc": "Compare contexts with and without weakening and contraction.",
    "type": "structural",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 9,
    "unit": 5,
    "title": "Conjunction detour reducer",
    "desc": "Remove an introduction\u2013elimination pair without changing the conclusion.",
    "type": "detour",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 10,
    "unit": 5,
    "title": "Lambda beta evaluator",
    "desc": "Follow two elementary typed beta-reduction examples.",
    "type": "beta",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 11,
    "unit": 6,
    "title": "Classical tableau branch explorer",
    "desc": "Open and close semantic tableau branches for a selected formula.",
    "type": "tableau",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 12,
    "unit": 6,
    "title": "Resolution clause checker",
    "desc": "Resolve two clauses when they have complementary pivot literals.",
    "type": "resolution",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 13,
    "unit": 7,
    "title": "Rule soundness enumeration",
    "desc": "Enumerate bounded propositional valuations for a valid and an invalid rule.",
    "type": "soundness",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 14,
    "unit": 7,
    "title": "Finite-fragment compactness lens",
    "desc": "Display only what bounded fragments show, not an infinite compactness proof.",
    "type": "compactness",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 15,
    "unit": 8,
    "title": "Two-world Kripke force diagram",
    "desc": "Contrast excluded middle and double-negation at a world with future extensions.",
    "type": "kripke",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  },
  {
    "idx": 16,
    "unit": 8,
    "title": "Proof term type checker",
    "desc": "Check simple identity, pairing and swap types in a tiny fixed grammar.",
    "type": "types",
    "controls": "<div class=\"sim-controls\"><label>Bounded count / depth (1\u20138) <input name=\"n\" type=\"number\" min=\"1\" max=\"8\" value=\"3\" aria-label=\"Bounded count or depth\"></label><label>Parameter A / bit mask <input name=\"a\" type=\"number\" min=\"0\" max=\"255\" value=\"3\" aria-label=\"Parameter A\"></label><label>Parameter B / bit mask <input name=\"b\" type=\"number\" min=\"0\" max=\"255\" value=\"2\" aria-label=\"Parameter B\"></label></div>"
  }
];

  // Original calculation logic adapted for scoped execution
"use strict";
(()=>{
 const input=(name,defaultValue)=>{const e=document.querySelector(`[name="${name}"]`);const n=Number(e?.value);return Number.isFinite(n)?Math.trunc(n):defaultValue};
 const clamp=(x,lo,hi)=>Math.max(lo,Math.min(hi,x));
 const show=(title,lines)=>{const e=document.getElementById('output');if(!e)return;e.replaceChildren();const h=document.createElement('h2');h.textContent=title;e.append(h);const ul=document.createElement('ol');for(const l of lines){const li=document.createElement('li');li.textContent=l;ul.append(li);}e.append(ul);};
 const calculate=()=>{
 const mode=document.body.dataset.kind;
 const n=clamp(input('n',3),1,8),a=clamp(input('a',3),0,255),b=clamp(input('b',2),0,255);
 const tf=x=>x?'T':'F',bit=(m,i)=>(m>>i)&1;
 let o=[];let title='';
 switch(mode){
 case 'entail': {
  title='Truth-table entailment Γ ⊨ Q';let counter=0;for(let p=0;p<2;p++)for(let q=0;q<2;q++){
   const impl=!p||q,legal=Boolean(p&&impl);if(legal&&!q)counter++;o.push(`P=${tf(p)} Q=${tf(q)} | P→Q=${tf(impl)} | both premises=${tf(legal)} | Q=${tf(q)}`);}
  o.push(`Countervaluations for {P,P→Q} ⊨ Q: ${counter}.`);o.push(`Additional user parameter ${n} controls repetitions of certificate checking; the semantic table still has exactly four valuations for two atoms.`);for(let i=0;i<n;i++)o.push(`Certificate pass ${i+1}: from P and P→Q infer Q by →E.`);break;}
 case 'certificate': {
  title='Local modus ponens checker';const hasP=!!(a&1),hasImp=!!(b&1),claimQ=!!(b&2);o=[`Given line 1: P = ${hasP?'present':'absent'}`,`Given line 2: P→Q = ${hasImp?'present':'absent'}`,`Candidate line 3: Q = ${claimQ?'requested':'not requested'}`,`Certificate valid for Q using →E: ${hasP&&hasImp&&claimQ?'YES':'NO'}`,`Rule requires both premises and exactly the conclusion Q. Parameter n=${n} is a display label, not a logical assumption.`];break;}
 case 'conjunction': {
  title='Pair introduction / projections';const P=!!(a&1),Q=!!(b&1);o=[`Proof of P available: ${P}`,`Proof of Q available: ${Q}`,`Can construct P∧Q by ∧I: ${P&&Q}`,`From completed pair, first projection yields P: ${P&&Q}`,`Second projection yields Q: ${P&&Q}`,`Requested ${n} independent copies of the proof are not needed to obtain one pair.`];break;}
 case 'implication': {
  title='Scoped implication proof';const open=n%2===1;const use=!!(a&1);o=[`Goal: P→P. Open temporary assumption h:P.`, `Internal body cites h: ${use?'yes':'no'}`,`Local branch may close with P: ${use}`,`Apply →I to discharge h: ${use?'valid':'invalid: no proof of P'}`,`After discharge, free assumptions: ${use?'none':'proof obligation remains'}`,`Selected display mode: ${open?'show local assumption box':'show outer theorem context'}`];break;}
 case 'universal': {
  title='Finite universal predicate check';const values=Array.from({length:n},(_,i)=>!!bit(a,i));o=values.map((x,i)=>`Predicate P(${i})=${tf(x)}`);o.push(`∀x in the finite domain {0,…,${n-1}} P(x): ${values.every(Boolean)}`);o.push(`P(0) is ${tf(values[0])}; one observed success cannot establish universal truth if another element fails.`);o.push('An arbitrary infinite-domain theorem needs a genuine proof rather than this finite enumeration.');break;}
 case 'existential': {
  title='Finite existential witness';const hits=Array.from({length:n},(_,i)=>i).filter(i=>bit(a,i));o=[`Witness candidates with P(x)=true: ${hits.length?hits.join(', '):'none'}`,`∃x∈{0,…,${n-1}} P(x): ${hits.length>0}`,hits.length?`One valid witness is ${hits[0]}.`:'No witness exists in this finite interpretation.',`Fresh local witness symbol c${b%n}: cannot escape an ∃E subproof as an arbitrarily named constant.`,'This demonstration finds witnesses in a finite data set; it does not certify existential results for all models.'];break;}
 case 'sequent': {
  title='Backward sequent rules';const atom=['P','Q','R','S'][a%4],oth=['Q','R','S','P'][b%4];o=[`Goal: ⇒ ${atom}→(${oth}∧${atom})`,`Apply →R: ${atom} ⇒ (${oth}∧${atom})`,`Apply ∧R: branches ${atom}⇒${oth} and ${atom}⇒${atom}`,`Second branch closes by identity. First branch ${atom}⇒${oth} ${atom===oth?'closes by identity':'remains open unless more assumptions are supplied'}.`,`Number of requested branch duplications: ${n}.`];break;}
 case 'structural': {
  title='Structural-rule scope';const k=n,extra=Array.from({length:k},(_,i)=>`R${i+1}`);o=[`Identity: P ⇒ P`,`Weakening-left: P, ${extra.join(', ')} ⇒ P`,`Contraction request: ${a%2?'P,P ⇒ Q to P ⇒ Q':'not requested'}`,`Contraction is permitted in ordinary LK/LJ contexts, but resource calculi may forbid it.`,`A second parameter b=${b} changes the input annotation, not the rule's legality.`];break;}
 case 'detour': {
  title='Normalizing a conjunction detour';const sel=a%2===0?'left':'right';const left=`evidence_P_${n}`,right=`evidence_Q_${b%7}`;o=[`Input proofs: dP=${left}:P and dQ=${right}:Q`,`Introduce pair (dP,dQ):P∧Q`,`Eliminate ${sel} component: ${sel==='left'?left:right}`,`After normalization: ${sel==='left'?left:right} directly; two inference nodes disappear.`,`Note: a normalization step preserves the proven judgment, not necessarily the exact set of used assumptions.`];break;}
 case 'beta': {
  title='Capture-avoiding beta reduction';const v='u'+n,w='v'+(a%10);o=[`Term: (λx.x) ${v}`,`Beta reduction: ${v}`,`Term: ((λx.λy.x) ${v}) ${w}`,`Beta reduction: ${v}`,`If ${v} had free y, rename bound y before substituting x.`,`This tiny example does not prove strong normalization for any wider calculus.`];break;}
 case 'tableau': {
  title='Tableau for selected target';const isTauto=a%2===0;const target=isTauto?'P→P':'P∨Q';o=[`Target: ${target}`,`Negated target: ${isTauto?'P∧¬P':'¬P∧¬Q'}`,`After expansion: ${isTauto?'P and ¬P on one branch':'¬P and ¬Q on one branch'}`,`Branch status: ${isTauto?'closed (contradiction)':'open (set P=F,Q=F)'}`,`Conclusion: ${isTauto?'target is valid':'target is NOT valid'}`,`Finite display depth parameter: ${n}.`];break;}
 case 'resolution': {
  title='Complementary pivot resolution';const pos=!!(a&1),neg=!!(b&1);o=[`Clause C1: ${pos?'P ∨ R':'Q ∨ R'}`,`Clause C2: ${neg?'¬P ∨ S':'P ∨ S'}`,`Pivot literals complementary: ${pos&&neg}`,pos&&neg?'Resolvent: R ∨ S':'No valid resolution on P from this pair.',`Repeat count n=${n} does not create a missing complementary pivot.`,`Do not confuse an empty clause with an empty collection of clauses.`];break;}
 case 'soundness': {
  title='Finite truth-preservation audit';let failures=0;const useValid=a%2===0;for(let p=0;p<2;p++)for(let q=0;q<2;q++){const premise=useValid?(p&&(!p||q)):(p||q),claim=useValid?q:p;if(premise&&!claim)failures++;o.push(`P=${tf(p)}, Q=${tf(q)}, premises=${tf(premise)}, proposed conclusion=${tf(claim)}`);}o.push(`Rule tested: ${useValid?'P, P→Q / Q':'P∨Q / P'}`);o.push(`Counterexamples: ${failures}; a valid general rule still needs a proof for every valuation.`);break;}
 case 'compactness': {
  title='Bounded finite fragments';for(let k=1;k<=n;k++)o.push(`Finite fragment {c>0,...,c>${k-1}} is satisfied by c=${k} in the standard real numbers.`);o.push('There is no fixed ordinary real greater than every natural number.');o.push('Classical first-order compactness instead guarantees a model in a possibly nonstandard structure if every finite subset of the theory is satisfiable.');o.push(`Input coefficient a=${a} has no effect on this mathematical contrast.`);break;}
 case 'kripke': {
  title='Two-world Kripke model';const rootP=!!(a&1),futureP=true;const emRoot=rootP;const nnRoot=true;o=[`Ordered worlds w0 ≤ w1; P(w0)=${rootP}, P(w1)=${futureP}.`,`At w0, P∨¬P forced: ${emRoot}; at w1 it is forced.`,`At w0, ¬¬P forced: ${nnRoot}.`,`For nontrivial input P(w0)=false, ¬¬P holds without P at root; this refutes intuitionistic ¬¬P→P.`,`Monotonicity requires P true at all future worlds if already true at w0.`,`World display count n=${n} is illustrative; the frame has exactly two worlds.`];break;}
 case 'types': {
  title='Tiny proof-term type-check examples';const choice=a%3;const items=[['λx.x','A → A'],['λp.(snd p,fst p)','(A×B) → (B×A)'],['λa.λb.(a,b)','A → B → (A×B)']];const [term,type]=items[choice];o=[`Selected proof term: ${term}`,`Expected type: ${type}`,`Checker judgment: valid under the fixed product/function typing rules.`,`No arbitrary user expressions are parsed by this demonstration; choice ${choice} is one of three predefined well-typed terms.`,`Parameter n=${n} asks students to replay the same derivation, not to invent a stronger theorem.`];break;}
 default: title='Unknown model';o=['No calculation available.'];}
 show(title,o);
};
document.querySelectorAll('#controls input').forEach(e=>e.addEventListener('input',calculate));calculate();
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
