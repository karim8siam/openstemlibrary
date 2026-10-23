/* Statistical Simulation and Monte Carlo Methods interactive teaching models and SVG visualizers. */
(function(root){
  'use strict';
  const doc = typeof document !== 'undefined' ? document : null;
  if(!doc) return;

  function range(v, a, b, name){
    if(!Number.isFinite(v) || v < a || v > b) throw Error(name + ' must be between ' + a + ' and ' + b + '.');
    return v;
  }
  function integer(v, a, b, name){
    range(v, a, b, name);
    if(!Number.isInteger(v)) throw Error(name + ' must be an integer.');
    return v;
  }

  function field(id, label, val, min, max, step){
    return `<label class="prob-control" for="${id}"><span>${label}</span><input type="number" id="${id}" value="${val}" min="${min}" max="${max}" step="${step}"/></label>`;
  }
  function select(id, label, options){
    const opts = options.map(([v, t]) => `<option value="${v}">${t}</option>`).join('');
    return `<label class="prob-control" for="${id}"><span>${label}</span><select id="${id}">${opts}</select></label>`;
  }
  function summary(vals){
    return '<div class="prob-summary stat-results" aria-live="polite">' + Object.entries(vals).map(([k, v]) => `<div><strong>${k}:</strong> <span>${v}</span></div>`).join('') + '</div>';
  }
  function fmt(n){
    if(n === null || n === undefined) return 'N/A';
    if(typeof n === 'string') return n;
    return Number.isFinite(n) ? (Math.abs(n) >= 1e4 || (Math.abs(n) < 1e-3 && n !== 0) ? n.toExponential(3) : n.toFixed(4)) : 'NaN';
  }

  // PRNG helper
  function mulberry32(a) {
    return function() {
      var t = a += 0x6D2B79F5;
      t = Math.imul(t ^ t >>> 15, t | 1);
      t ^= t + Math.imul(t ^ t >>> 7, t | 61);
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    }
  }

  // 1. Linear Congruential Generator Simulation Model
  function lcgModel(m, a, c, seed, nPoints){
    integer(m, 4, 1024, 'Modulus m');
    integer(a, 1, m - 1, 'Multiplier a');
    integer(c, 0, m - 1, 'Increment c');
    integer(seed, 0, m - 1, 'Seed x0');
    integer(nPoints, 10, 500, 'Number of Points');

    let x = seed;
    const seq = [];
    const visited = new Map();
    let period = 0;

    for(let i = 0; i < nPoints + 1; i++){
      if(!visited.has(x) && period === 0){
        visited.set(x, i);
      } else if(period === 0){
        period = i - visited.get(x);
      }
      seq.push(x);
      x = (a * x + c) % m;
    }

    if(period === 0) period = visited.size;

    const pairs = [];
    for(let i = 0; i < Math.min(nPoints, seq.length - 1); i++){
      pairs.push([seq[i] / m, seq[i+1] / m]);
    }

    // Hull-Dobell Theorem check
    function gcd(p, q){ while(q){ let t = q; q = p % q; p = t; } return p; }
    const cCoprime = gcd(c, m) === 1;
    let fullPeriodExpected = cCoprime;

    return { pairs, period, fullPeriodExpected, modulus: m };
  }

  // 2. Rejection Sampling Model
  function rejectionModel(cVal, nDraws, seed){
    range(cVal, 1.1, 4.0, 'Bounding constant c');
    integer(nDraws, 50, 600, 'Number of proposals');
    const rand = mulberry32(seed || 42);

    // Target: Beta(2, 4) on [0, 1]: f(x) = 20 * x * (1 - x)^3
    // Mode at x = 1/4 = 0.25; f(0.25) = 20 * 0.25 * 0.75^3 = 5 * 0.421875 = 2.109375
    // Proposal: Uniform(0, 1), g(x) = 1.0. Minimum c = 2.109375.
    const accepted = [];
    const rejected = [];

    for(let i = 0; i < nDraws; i++){
      const u1 = rand();
      const u2 = rand();
      const fx = 20 * u1 * Math.pow(1 - u1, 3);
      const envelope = cVal * 1.0;
      if(u2 * envelope <= fx){
        accepted.push([u1, u2 * envelope]);
      } else {
        rejected.push([u1, u2 * envelope]);
      }
    }

    const curveTarget = [];
    const curveEnvelope = [];
    for(let i = 0; i <= 60; i++){
      const x = i / 60;
      curveTarget.push([x, 20 * x * Math.pow(1 - x, 3)]);
      curveEnvelope.push([x, cVal]);
    }

    const empRate = accepted.length / nDraws;
    const theoRate = 1.0 / cVal;

    return { accepted, rejected, curveTarget, curveEnvelope, empRate, theoRate };
  }

  // 3. Importance Sampling vs Crude Monte Carlo Model
  function importanceModel(threshold, nSample, seed){
    range(threshold, 1.5, 4.5, 'Threshold gamma');
    integer(nSample, 100, 5000, 'Sample size n');
    const rand = mulberry32(seed || 101);

    // Objective: Estimate P(Z > gamma) for standard normal Z ~ N(0, 1)
    // Crude MC: indicator I(Z_i > gamma)
    // Importance Sampling: proposal N(gamma, 1)
    let crudeHits = 0;
    let impSum = 0;
    let impSqSum = 0;

    for(let i = 0; i < nSample; i++){
      // Box-Muller for standard normal
      const u1 = Math.max(1e-12, rand());
      const u2 = rand();
      const z0 = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);

      if(z0 > threshold) crudeHits++;

      // Importance draw: Y ~ N(threshold, 1)
      const u3 = Math.max(1e-12, rand());
      const u4 = rand();
      const z1 = Math.sqrt(-2 * Math.log(u3)) * Math.cos(2 * Math.PI * u4);
      const y = threshold + z1;

      // Likelihood ratio: f(y) / g(y) = exp(-0.5 * y^2) / exp(-0.5 * (y - threshold)^2)
      // = exp(-0.5 * [y^2 - y^2 + 2 * y * threshold - threshold^2]) = exp(-threshold * y + 0.5 * threshold^2)
      let w = 0;
      if(y > threshold){
        w = Math.exp(-threshold * y + 0.5 * threshold * threshold);
      }
      impSum += w;
      impSqSum += w * w;
    }

    const crudeEst = crudeHits / nSample;
    const crudeVar = (crudeEst * (1 - crudeEst)) / nSample;
    const crudeSE = Math.sqrt(crudeVar);

    const impEst = impSum / nSample;
    const impVar = (impSqSum / nSample - impEst * impEst) / nSample;
    const impSE = Math.sqrt(Math.max(0, impVar));

    // Approximate true value using Mill's ratio or complementary error function
    function normalCcdf(x){
      const t = 1.0 / (1.0 + 0.2316419 * Math.abs(x));
      const d = 0.3989422804 * Math.exp(-x * x / 2.0);
      const prob = d * t * (0.31938153 + t * (-0.356563782 + t * (1.781477937 + t * (-1.821255978 + t * 1.330274429))));
      return x > 0 ? prob : 1.0 - prob;
    }
    const trueProb = normalCcdf(threshold);
    const varReduction = crudeSE > 0 ? (crudeVar / Math.max(1e-15, impVar)) : 1.0;

    return { crudeEst, crudeSE, impEst, impSE, trueProb, varReduction };
  }

  // 4. Metropolis-Hastings Random Walk Model
  function metropolisModel(propSigma, nSteps, seed){
    range(propSigma, 0.1, 4.0, 'Proposal sigma');
    integer(nSteps, 200, 3000, 'Number of steps');
    const rand = mulberry32(seed || 555);

    // Target: Bimodal 1D mixture 0.5 * N(-2, 0.7^2) + 0.5 * N(2, 0.7^2)
    function target(x){
      const d1 = (x + 2.0) / 0.7;
      const d2 = (x - 2.0) / 0.7;
      return 0.5 * Math.exp(-0.5 * d1 * d1) + 0.5 * Math.exp(-0.5 * d2 * d2);
    }

    let current = 0.0;
    const chain = [current];
    let accepted = 0;

    for(let i = 0; i < nSteps; i++){
      // Gaussian proposal
      const u1 = Math.max(1e-12, rand());
      const u2 = rand();
      const z = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
      const proposed = current + propSigma * z;

      const alpha = Math.min(1.0, target(proposed) / Math.max(1e-15, target(current)));
      if(rand() < alpha){
        current = proposed;
        accepted++;
      }
      chain.push(current);
    }

    const accRate = accepted / nSteps;
    const mean = chain.reduce((a, b) => a + b, 0) / chain.length;
    const variance = chain.reduce((a, b) => a + Math.pow(b - mean, 2), 0) / chain.length;

    // Subsampled trace for visualization
    const trace = [];
    const step = Math.max(1, Math.floor(chain.length / 120));
    for(let i = 0; i < chain.length; i += step){
      trace.push([i, chain[i]]);
    }

    return { accRate, mean, variance, trace };
  }

  // SVG Chart rendering helper
  function scatterChart(points, title, xLabel, yLabel){
    const W = 620, H = 260, padL = 55, padR = 25, padT = 30, padB = 40;
    const pw = W - padL - padR, ph = H - padT - padB;

    let ptsSvg = '';
    points.forEach(([x, y]) => {
      const sx = padL + Math.min(1, Math.max(0, x)) * pw;
      const sy = padT + (1 - Math.min(1, Math.max(0, y))) * ph;
      ptsSvg += `<circle cx="${sx.toFixed(1)}" cy="${sy.toFixed(1)}" r="2.5" fill="#38bdf8" opacity="0.7"/>`;
    });

    return `<svg role="img" aria-label="${title}" viewBox="0 0 ${W} ${H}" class="stat-chart" style="width:100%;height:auto;background:#0f172a;border-radius:8px;margin-top:1rem;">
      <text x="${W/2}" y="20" fill="#f8fafc" text-anchor="middle" font-size="12" font-weight="600">${title}</text>
      <line x1="${padL}" y1="${padT}" x2="${padL}" y2="${H-padB}" stroke="#475569" stroke-width="1"/>
      <line x1="${padL}" y1="${H-padB}" x2="${W-padR}" y2="${H-padB}" stroke="#475569" stroke-width="1"/>
      <text x="${padL + pw/2}" y="${H-10}" fill="#94a3b8" text-anchor="middle" font-size="11">${xLabel}</text>
      <text x="18" y="${padT + ph/2}" fill="#94a3b8" text-anchor="middle" font-size="11" transform="rotate(-90 18 ${padT+ph/2})">${yLabel}</text>
      ${ptsSvg}
    </svg>`;
  }

  function curveAndPointsChart(curves, accPts, rejPts, title){
    const W = 620, H = 260, padL = 55, padR = 25, padT = 30, padB = 40;
    const pw = W - padL - padR, ph = H - padT - padB;

    const yMax = 4.5;
    function toSvg(x, y){
      const sx = padL + Math.min(1, Math.max(0, x)) * pw;
      const sy = padT + (1 - Math.min(yMax, Math.max(0, y)) / yMax) * ph;
      return [sx, sy];
    }

    let paths = '';
    curves.forEach(c => {
      let d = '';
      c.pts.forEach(([x, y], idx) => {
        const [sx, sy] = toSvg(x, y);
        d += (idx === 0 ? `M ${sx.toFixed(1)} ${sy.toFixed(1)}` : ` L ${sx.toFixed(1)} ${sy.toFixed(1)}`);
      });
      paths += `<path d="${d}" fill="none" stroke="${c.color}" stroke-width="${c.width || 2}" ${c.dash ? `stroke-dasharray="${c.dash}"` : ''}/>`;
    });

    let ptsSvg = '';
    rejPts.slice(0, 150).forEach(([x, y]) => {
      const [sx, sy] = toSvg(x, y);
      ptsSvg += `<circle cx="${sx.toFixed(1)}" cy="${sy.toFixed(1)}" r="2" fill="#ef4444" opacity="0.6"/>`;
    });
    accPts.slice(0, 150).forEach(([x, y]) => {
      const [sx, sy] = toSvg(x, y);
      ptsSvg += `<circle cx="${sx.toFixed(1)}" cy="${sy.toFixed(1)}" r="2.5" fill="#10b981" opacity="0.85"/>`;
    });

    return `<svg role="img" aria-label="${title}" viewBox="0 0 ${W} ${H}" class="stat-chart" style="width:100%;height:auto;background:#0f172a;border-radius:8px;margin-top:1rem;">
      <text x="${W/2}" y="20" fill="#f8fafc" text-anchor="middle" font-size="12" font-weight="600">${title}</text>
      <line x1="${padL}" y1="${padT}" x2="${padL}" y2="${H-padB}" stroke="#475569" stroke-width="1"/>
      <line x1="${padL}" y1="${H-padB}" x2="${W-padR}" y2="${H-padB}" stroke="#475569" stroke-width="1"/>
      <text x="${padL + pw/2}" y="${H-10}" fill="#94a3b8" text-anchor="middle" font-size="11">Candidate Value x ∈ [0, 1]</text>
      <text x="18" y="${padT + ph/2}" fill="#94a3b8" text-anchor="middle" font-size="11" transform="rotate(-90 18 ${padT+ph/2})">Density</text>
      ${paths}
      ${ptsSvg}
    </svg>`;
  }

  function lineChart(series, title, xLabel, yLabel, yMin, yMax){
    const W = 620, H = 260, padL = 55, padR = 25, padT = 30, padB = 40;
    const pw = W - padL - padR, ph = H - padT - padB;

    let xMin = Infinity, xMax = -Infinity;
    series.forEach(([x, y]) => {
      if(x < xMin) xMin = x;
      if(x > xMax) xMax = x;
    });
    if(xMax === xMin) xMax = xMin + 1;

    let d = '';
    series.forEach(([x, y], idx) => {
      const sx = padL + ((x - xMin) / (xMax - xMin)) * pw;
      const sy = padT + (1 - (y - yMin) / (yMax - yMin || 1)) * ph;
      d += (idx === 0 ? `M ${sx.toFixed(1)} ${sy.toFixed(1)}` : ` L ${sx.toFixed(1)} ${sy.toFixed(1)}`);
    });

    return `<svg role="img" aria-label="${title}" viewBox="0 0 ${W} ${H}" class="stat-chart" style="width:100%;height:auto;background:#0f172a;border-radius:8px;margin-top:1rem;">
      <text x="${W/2}" y="20" fill="#f8fafc" text-anchor="middle" font-size="12" font-weight="600">${title}</text>
      <line x1="${padL}" y1="${padT}" x2="${padL}" y2="${H-padB}" stroke="#475569" stroke-width="1"/>
      <line x1="${padL}" y1="${H-padB}" x2="${W-padR}" y2="${H-padB}" stroke="#475569" stroke-width="1"/>
      <text x="${padL + pw/2}" y="${H-10}" fill="#94a3b8" text-anchor="middle" font-size="11">${xLabel}</text>
      <text x="18" y="${padT + ph/2}" fill="#94a3b8" text-anchor="middle" font-size="11" transform="rotate(-90 18 ${padT+ph/2})">${yLabel}</text>
      <path d="${d}" fill="none" stroke="#38bdf8" stroke-width="2"/>
    </svg>`;
  }

  function initSimulation(containerId, simType){
    const el = typeof containerId === 'string' ? doc.getElementById(containerId) : containerId;
    if(!el) return;
    el.innerHTML = '';

    const controls = doc.createElement('div');
    controls.className = 'prob-controls stat-controls';
    const result = doc.createElement('div');
    result.className = 'prob-display';

    let inputsHtml = '';
    if(simType === 'sim-prng-lcg'){
      inputsHtml = field('lcgMod', 'Modulus m', 64, 8, 512, 1) +
                   field('lcgMult', 'Multiplier a', 13, 1, 511, 1) +
                   field('lcgInc', 'Increment c', 1, 0, 511, 1) +
                   field('lcgSeed', 'Seed x0', 1, 0, 511, 1);
    }else if(simType === 'sim-rejection-sampling'){
      inputsHtml = field('rejC', 'Bounding Constant c', 2.5, 1.2, 4.0, 0.1) +
                   field('rejDraws', 'Proposals n', 300, 50, 600, 50);
    }else if(simType === 'sim-importance-sampling'){
      inputsHtml = field('impThresh', 'Threshold gamma', 2.5, 1.5, 4.5, 0.1) +
                   field('impSamples', 'Sample Size n', 1000, 100, 5000, 100);
    }else if(simType === 'sim-mcmc-metropolis'){
      inputsHtml = field('mcmcSigma', 'Proposal Step Sigma', 1.0, 0.1, 4.0, 0.1) +
                   field('mcmcSteps', 'MCMC Steps N', 1000, 200, 3000, 100);
    }

    controls.innerHTML = inputsHtml + '<button type="button" class="btn" data-reset style="margin-top:0.75rem;">Reset Parameters</button>';
    el.appendChild(controls);
    el.appendChild(result);

    const inputs = controls.querySelectorAll('input, select');
    const initial = Array.from(inputs).map(i => i.value);

    function get(id){
      const inp = doc.getElementById(id);
      return inp ? parseFloat(inp.value) : 0;
    }

    function render(){
      try{
        let values = {}, plot = '';
        if(simType === 'sim-prng-lcg'){
          const m = lcgModel(Math.round(get('lcgMod')), Math.round(get('lcgMult')), Math.round(get('lcgInc')), Math.round(get('lcgSeed')), 200);
          values = {
            'Period Length Observed': `${m.period} / ${m.modulus}`,
            'Full Period Theorem': m.fullPeriodExpected ? 'Satisfied (Hull-Dobell)' : 'Not Satisfied',
            'Lattice Pairs Plotted': m.pairs.length
          };
          plot = scatterChart(m.pairs, `LCG 2D Lattice: (x_i/m, x_{i+1}/m) with m=${Math.round(get('lcgMod'))}, a=${Math.round(get('lcgMult'))}`, 'Normalized Value x_i / m', 'Normalized Value x_{i+1} / m');
        }else if(simType === 'sim-rejection-sampling'){
          const m = rejectionModel(get('rejC'), Math.round(get('rejDraws')), 42);
          values = {
            'Theoretical Acceptance Rate': fmt(m.theoRate),
            'Empirical Acceptance Rate': fmt(m.empRate),
            'Accepted Samples': m.accepted.length,
            'Rejected Proposals': m.rejected.length
          };
          plot = curveAndPointsChart([
            { pts: m.curveEnvelope, color: '#f59e0b', width: 2, dash: '4,4' },
            { pts: m.curveTarget, color: '#38bdf8', width: 2.5 }
          ], m.accepted, m.rejected, 'Acceptance-Rejection: Target Beta(2,4) [Cyan] vs Uniform Envelope c [Amber]');
        }else if(simType === 'sim-importance-sampling'){
          const m = importanceModel(get('impThresh'), Math.round(get('impSamples')), 101);
          values = {
            'True Analytical Tail Prob': fmt(m.trueProb),
            'Crude MC Estimate': fmt(m.crudeEst) + ' (SE: ' + fmt(m.crudeSE) + ')',
            'Importance Sampling Est': fmt(m.impEst) + ' (SE: ' + fmt(m.impSE) + ')',
            'Variance Reduction Factor': fmt(m.varReduction) + 'x'
          };
          plot = `<div style="background:#0f172a;padding:1rem;border-radius:8px;margin-top:1rem;color:#f8fafc;font-size:0.9rem;">
            <div style="font-weight:600;margin-bottom:0.5rem;color:#38bdf8;">Simulation Efficiency Comparison (P(Z > ${get('impThresh')})):</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
              <div style="background:#1e293b;padding:0.75rem;border-radius:6px;">
                <div style="color:#94a3b8;font-size:0.8rem;">Crude Monte Carlo</div>
                <div style="font-size:1.2rem;font-weight:700;color:#ef4444;">${fmt(m.crudeEst)}</div>
                <div style="color:#cbd5e1;font-size:0.8rem;">Standard Error: ${fmt(m.crudeSE)}</div>
              </div>
              <div style="background:#1e293b;padding:0.75rem;border-radius:6px;">
                <div style="color:#94a3b8;font-size:0.8rem;">Importance Sampling</div>
                <div style="font-size:1.2rem;font-weight:700;color:#10b981;">${fmt(m.impEst)}</div>
                <div style="color:#cbd5e1;font-size:0.8rem;">Standard Error: ${fmt(m.impSE)}</div>
              </div>
            </div>
          </div>`;
        }else if(simType === 'sim-mcmc-metropolis'){
          const m = metropolisModel(get('mcmcSigma'), Math.round(get('mcmcSteps')), 555);
          values = {
            'Empirical Acceptance Rate': fmt(m.accRate),
            'Target Optimal Acceptance': '0.44 (1D) / 0.234 (High-D)',
            'Estimated Target Mean': fmt(m.mean),
            'Estimated Target Variance': fmt(m.variance)
          };
          plot = lineChart(m.trace, 'Metropolis Random Walk Trace Plot x_t over Iterations', 'Iteration t', 'Sample State x_t', -5, 5);
        }

        result.innerHTML = summary(values) + plot;
      }catch(err){
        result.textContent = err.message;
      }
    }

    inputs.forEach(input => input.addEventListener(input.tagName === 'SELECT' ? 'change' : 'input', render));
    const resetBtn = el.querySelector('[data-reset]');
    if(resetBtn){
      resetBtn.addEventListener('click', () => {
        inputs.forEach((input, i) => input.value = initial[i]);
        render();
      });
    }
    render();
  }

  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = initSimulation;
  root.StatisticalSimulationSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
