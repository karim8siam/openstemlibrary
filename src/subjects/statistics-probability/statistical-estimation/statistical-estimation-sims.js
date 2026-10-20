/* Statistical Estimation interactive teaching models and Canvas/SVG visualizers. */
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

  // Seeded Pseudo-Random Number Generator (Mulberry32)
  function rng(seed){
    let s = (seed >>> 0) || 20261019;
    return () => {
      s = (s + 0x6D2B79F5) >>> 0;
      let t = s;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  // Box-Muller standard normal generator
  function randn(random){
    let u = 0, v = 0;
    while(u === 0) u = random();
    while(v === 0) v = random();
    return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
  }

  // --- SVG UI & Rendering Helpers ---
  function field(id, label, val, min, max, step){
    return `<label class="prob-control" for="${id}"><span>${label}</span><input type="number" id="${id}" value="${val}" min="${min}" max="${max}" step="${step}"/></label>`;
  }
  function select(id, label, options){
    const opts = options.map(([v, t]) => `<option value="${v}">${t}</option>`).join('');
    return `<label class="prob-control" for="${id}"><span>${label}</span><select id="${id}">${opts}</select></label>`;
  }
  function summary(vals){
    return '<div class="prob-summary">' + Object.entries(vals).map(([k, v]) => `<div><strong>${k}:</strong> <span>${v}</span></div>`).join('') + '</div>';
  }
  function fmt(n){
    if(n === null || n === undefined) return 'N/A';
    if(typeof n === 'string') return n;
    return Number.isFinite(n) ? (Math.abs(n) >= 1e4 || (Math.abs(n) < 1e-3 && n !== 0) ? n.toExponential(3) : n.toFixed(3)) : 'NaN';
  }

  function chart(seriesList, xMin, xMax, titleStr, vRef = null, hRef = null){
    const W = 620, H = 240, padL = 50, padR = 25, padT = 25, padB = 35;
    const plotW = W - padL - padR, plotH = H - padT - padB;

    let yMax = 0, yMin = 0;
    seriesList.forEach(s => {
      s.values.forEach(([x, y]) => {
        if(Number.isFinite(y)){
          if(y > yMax) yMax = y;
          if(y < yMin) yMin = y;
        }
      });
    });
    if(yMax <= yMin) yMax = yMin + 1;
    const ySpan = yMax - yMin;
    const yDispMax = yMax + 0.1 * ySpan;
    const yDispMin = yMin >= 0 ? 0 : yMin - 0.1 * ySpan;

    const px = (x) => padL + ((x - xMin) / (xMax - xMin)) * plotW;
    const py = (y) => padT + plotH - ((y - yDispMin) / (yDispMax - yDispMin)) * plotH;

    let svg = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${titleStr}" class="prob-chart"><title>${titleStr}</title>`;
    svg += `<rect x="${padL}" y="${padT}" width="${plotW}" height="${plotH}" fill="rgba(15, 23, 42, 0.45)" rx="4"/>`;

    // Horizontal grid lines
    for(let i = 0; i <= 4; i++){
      const yVal = yDispMin + ((yDispMax - yDispMin) / 4) * i;
      const yPos = py(yVal);
      svg += `<line x1="${padL}" y1="${yPos}" x2="${padL + plotW}" y2="${yPos}" stroke="rgba(148, 163, 184, 0.15)" stroke-width="1"/>`;
      svg += `<text x="${padL - 8}" y="${yPos + 4}" fill="#94a3b8" font-size="11" text-anchor="end">${fmt(yVal)}</text>`;
    }

    // Horizontal axis labels
    for(let i = 0; i <= 5; i++){
      const xVal = xMin + ((xMax - xMin) / 5) * i;
      const xPos = px(xVal);
      svg += `<line x1="${xPos}" y1="${padT}" x2="${xPos}" y2="${padT + plotH}" stroke="rgba(148, 163, 184, 0.12)" stroke-width="1"/>`;
      svg += `<text x="${xPos}" y="${padT + plotH + 18}" fill="#94a3b8" font-size="11" text-anchor="middle">${fmt(xVal)}</text>`;
    }

    // Render series
    seriesList.forEach(s => {
      if(s.bars){
        const bW = Math.max(2, (plotW / s.values.length) * 0.85);
        s.values.forEach(([x, y]) => {
          const barH = ((y - yDispMin) / (yDispMax - yDispMin)) * plotH;
          svg += `<rect x="${px(x) - bW / 2}" y="${py(y)}" width="${bW}" height="${Math.max(0, barH)}" fill="rgba(56, 189, 248, 0.45)" stroke="#38bdf8" stroke-width="1"/>`;
        });
      } else {
        const d = s.values.map(([x, y], i) => (i === 0 ? 'M' : 'L') + px(x).toFixed(1) + ' ' + py(y).toFixed(1)).join(' ');
        const strokeColor = s.color || (s.dashed ? '#fbbf24' : '#38bdf8');
        const dashArr = s.dashed ? 'stroke-dasharray="4 3"' : (s.dotted ? 'stroke-dasharray="2 2"' : '');
        svg += `<path d="${d}" fill="none" stroke="${strokeColor}" stroke-width="${s.width || 2}" ${dashArr}/>`;
      }
    });

    if(vRef !== null && Number.isFinite(vRef)){
      const rx = px(vRef);
      if(rx >= padL && rx <= padL + plotW){
        svg += `<line x1="${rx}" y1="${padT}" x2="${rx}" y2="${padT + plotH}" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>`;
        svg += `<text x="${rx + 4}" y="${padT + 14}" fill="#f43f5e" font-size="11">Target: ${fmt(vRef)}</text>`;
      }
    }
    if(hRef !== null && Number.isFinite(hRef)){
      const ry = py(hRef);
      if(ry >= padT && ry <= padT + plotH){
        svg += `<line x1="${padL}" y1="${ry}" x2="${padL + plotW}" y2="${ry}" stroke="#e11d48" stroke-width="1.5" stroke-dasharray="4 2"/>`;
        svg += `<text x="${padL + plotW - 6}" y="${ry - 5}" fill="#e11d48" font-size="10" text-anchor="end">Cutoff (${fmt(hRef)})</text>`;
      }
    }

    svg += `</svg>`;
    return svg;
  }

  // --- Simulation Models ---
  function crlbModel(dist, theta, n){
    range(theta, 0.1, 10, 'theta');
    integer(n, 5, 200, 'n');
    let i1 = 0, crlb = 0;
    if(dist === 'exponential'){
      // X ~ Exp(rate=theta), mean=1/theta. i1 = 1 / theta^2
      i1 = 1.0 / (theta * theta);
      crlb = (theta * theta) / n;
    } else if(dist === 'poisson'){
      // X ~ Poisson(theta), i1 = 1 / theta
      i1 = 1.0 / theta;
      crlb = theta / n;
    } else {
      // Normal mean mu = theta, variance sigma^2 = 1. i1 = 1 / 1 = 1
      i1 = 1.0;
      crlb = 1.0 / n;
    }

    // Monte Carlo variance of sample estimator
    const rand = rng(20261019 + n * 7);
    const R = 800;
    let sumT = 0, sumSqT = 0;
    for(let r = 0; r < R; r++){
      let sampleSum = 0;
      for(let i = 0; i < n; i++){
        if(dist === 'exponential'){
          sampleSum += -Math.log(Math.max(1e-12, rand())) / theta;
        } else if(dist === 'poisson'){
          // Knuth Poisson generator
          const L = Math.exp(-theta);
          let k = 0, p = 1;
          do { k++; p *= rand(); } while (p > L);
          sampleSum += (k - 1);
        } else {
          sampleSum += theta + randn(rand);
        }
      }
      const xbar = sampleSum / n;
      let est = xbar;
      if(dist === 'exponential'){
        // Estimating rate theta: MLE is 1/xbar, but UMVUE is (n-1)/(n*xbar)
        est = (n > 1) ? (n - 1) / (n * xbar) : (1.0 / xbar);
      }
      sumT += est;
      sumSqT += est * est;
    }
    const meanEst = sumT / R;
    const empVar = (sumSqT - R * meanEst * meanEst) / (R - 1);
    const eff = crlb / Math.max(1e-9, empVar);

    // Theoretical CRLB curve as n varies from 5 to 100
    const curve = [];
    for(let k = 5; k <= 100; k += 2){
      let bound = 0;
      if(dist === 'exponential') bound = (theta * theta) / k;
      else if(dist === 'poisson') bound = theta / k;
      else bound = 1.0 / k;
      curve.push([k, bound]);
    }

    return {
      n, theta, dist,
      i1,
      totalInfo: i1 * n,
      crlb,
      empVar,
      eff,
      curve
    };
  }

  function likelihoodModel(dist, theta0, n){
    range(theta0, 0.2, 5, 'theta0');
    integer(n, 10, 100, 'n');
    const rand = rng(42001 + n);
    let sampleSum = 0;
    for(let i = 0; i < n; i++){
      if(dist === 'exponential'){
        sampleSum += -Math.log(Math.max(1e-12, rand())) / theta0;
      } else if(dist === 'normal'){
        sampleSum += theta0 + randn(rand);
      } else {
        sampleSum += rand() < Math.min(0.95, Math.max(0.05, theta0 / 5)) ? 1 : 0;
      }
    }
    const xbar = sampleSum / n;
    let mle = xbar;
    if(dist === 'exponential') mle = 1.0 / xbar;
    else if(dist === 'bernoulli') mle = xbar;

    const tMin = Math.max(0.05, mle * 0.3);
    const tMax = mle * 1.8;
    const curve = [];
    let maxLogLik = -Infinity;

    for(let step = 0; step <= 80; step++){
      const t = tMin + ((tMax - tMin) / 80) * step;
      let ll = 0;
      if(dist === 'exponential'){
        ll = n * Math.log(t) - t * sampleSum;
      } else if(dist === 'normal'){
        ll = -0.5 * n * (xbar - t) * (xbar - t);
      } else {
        const p = Math.min(0.999, Math.max(0.001, t / 5));
        ll = sampleSum * Math.log(p) + (n - sampleSum) * Math.log(1 - p);
      }
      curve.push([t, ll]);
      if(ll > maxLogLik) maxLogLik = ll;
    }

    // Shift curve so max is 0 for clarity
    const normCurve = curve.map(([x, y]) => [x, y - maxLogLik]);
    const cutoff = -1.92; // 95% chi-square 1 dof / 2 = 3.84 / 2

    return {
      dist, n, theta0, mle,
      cutoff,
      normCurve,
      tMin, tMax
    };
  }

  function ciCoverageModel(conf, n, itype){
    range(conf, 0.80, 0.99, 'conf');
    integer(n, 5, 50, 'n');
    const rand = rng(10102026 + n * 3);
    const muTrue = 10.0, sigmaTrue = 2.0;
    const alpha = 1.0 - conf;
    // Critical value approx
    let zCrit = 1.96;
    if(conf <= 0.82) zCrit = 1.282;
    else if(conf <= 0.92) zCrit = 1.645;
    else if(conf <= 0.96) zCrit = 1.96;
    else zCrit = 2.576;

    // t-critical approximation via Cornish-Fisher
    const df = n - 1;
    const tCrit = zCrit + (zCrit * zCrit * zCrit + zCrit) / (4 * df);

    const M = 40;
    let covered = 0;
    let totalLen = 0;
    const intervals = [];

    for(let m = 0; m < M; m++){
      let sX = 0, sXX = 0;
      for(let i = 0; i < n; i++){
        const x = muTrue + sigmaTrue * randn(rand);
        sX += x;
        sXX += x * x;
      }
      const xbar = sX / n;
      const s = Math.sqrt(Math.max(1e-9, (sXX - n * xbar * xbar) / (n - 1)));
      const margin = (itype === 't_interval' ? tCrit * s : zCrit * sigmaTrue) / Math.sqrt(n);
      const low = xbar - margin;
      const high = xbar + margin;
      const hit = low <= muTrue && muTrue <= high;
      if(hit) covered++;
      totalLen += (high - low);
      intervals.push({ low, high, xbar, hit });
    }

    return {
      conf, n, itype,
      muTrue,
      coverageRate: (covered / M) * 100,
      avgWidth: totalLen / M,
      intervals
    };
  }

  function renderCiChart(m){
    const W = 620, H = 240, padL = 40, padR = 25, padT = 20, padB = 30;
    const plotW = W - padL - padR, plotH = H - padT - padB;
    const xMin = 7.0, xMax = 13.0;
    const px = (x) => padL + ((x - xMin) / (xMax - xMin)) * plotW;

    let svg = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Confidence Interval Coverage" class="prob-chart"><title>Confidence Interval Coverage</title>`;
    svg += `<rect x="${padL}" y="${padT}" width="${plotW}" height="${plotH}" fill="rgba(15, 23, 42, 0.45)" rx="4"/>`;

    // True mu vertical line
    const xMu = px(m.muTrue);
    svg += `<line x1="${xMu}" y1="${padT}" x2="${xMu}" y2="${padT + plotH}" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 3"/>`;
    svg += `<text x="${xMu}" y="${padT + 12}" fill="#38bdf8" font-size="11" text-anchor="middle">True μ = ${m.muTrue}</text>`;

    // Grid labels
    for(let v = 7; v <= 13; v++){
      const xv = px(v);
      svg += `<line x1="${xv}" y1="${padT}" x2="${xv}" y2="${padT + plotH}" stroke="rgba(148, 163, 184, 0.1)" stroke-width="1"/>`;
      svg += `<text x="${xv}" y="${padT + plotH + 16}" fill="#94a3b8" font-size="10" text-anchor="middle">${v}</text>`;
    }

    const nInt = m.intervals.length;
    const rowH = plotH / (nInt + 1);
    m.intervals.forEach((inv, i) => {
      const y = padT + rowH * (i + 1);
      const x1 = Math.max(padL, px(inv.low));
      const x2 = Math.min(padL + plotW, px(inv.high));
      const col = inv.hit ? '#10b981' : '#f43f5e';
      svg += `<line x1="${x1}" y1="${y}" x2="${x2}" y2="${y}" stroke="${col}" stroke-width="2"/>`;
      svg += `<circle cx="${px(inv.xbar)}" cy="${y}" r="2" fill="${col}"/>`;
    });

    svg += `</svg>`;
    return svg;
  }

  function bayesUpdaterModel(mu0, tau0, xbar, n, sig2){
    range(mu0, -5, 5, 'mu0');
    range(tau0, 0.1, 10, 'tau0');
    range(xbar, -5, 5, 'xbar');
    integer(n, 1, 100, 'n');

    // Conjugate Gaussian update
    // Likelihood precision: tauL = n / sig2
    const tauL = n / sig2;
    // Posterior precision: tauN = tau0 + tauL
    const tauN = tau0 + tauL;
    // Posterior mean: muN = (tau0 * mu0 + tauL * xbar) / tauN
    const muN = (tau0 * mu0 + tauL * xbar) / tauN;
    const sigN = Math.sqrt(1.0 / tauN);
    const sig0 = Math.sqrt(1.0 / tau0);
    const sigL = Math.sqrt(sig2 / n);

    // Plot grid
    const xMin = Math.min(mu0 - 3 * sig0, xbar - 3 * sigL, muN - 3 * sigN);
    const xMax = Math.max(mu0 + 3 * sig0, xbar + 3 * sigL, muN + 3 * sigN);

    const normPdf = (x, m, s) => (1.0 / (s * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * ((x - m) / s) * ((x - m) / s));

    const priorCurve = [], likCurve = [], postCurve = [];
    const steps = 90;
    for(let i = 0; i <= steps; i++){
      const x = xMin + ((xMax - xMin) / steps) * i;
      priorCurve.push([x, normPdf(x, mu0, sig0)]);
      likCurve.push([x, normPdf(x, xbar, sigL)]);
      postCurve.push([x, normPdf(x, muN, sigN)]);
    }

    return {
      mu0, tau0, xbar, n, muN, sigN,
      xMin, xMax,
      priorCurve, likCurve, postCurve,
      hpdLow: muN - 1.96 * sigN,
      hpdHigh: muN + 1.96 * sigN
    };
  }

  function initSimulation(containerId, type){
    const el = doc.getElementById(containerId);
    if(!el || el.dataset.simMounted) return;
    el.dataset.simMounted = 'true';
    el.classList.add('prob-explorer');

    let title = '', note = '', controls = '';
    const f = (key, label, value, min, max, step) => field(containerId + '-' + key, label, value, min, max, step);
    const s = (key, label, options) => select(containerId + '-' + key, label, options);

    if(type === 'stat-est-crlb-explorer'){
      title = 'Cramér–Rao Lower Bound & Empirical Efficiency Explorer';
      note = 'Compares the theoretical Cramér–Rao Lower Bound (CRLB) to the empirical sampling variance across 800 Monte Carlo draws as sample size n increases.';
      controls = s('dist', 'Distribution Family', [
        ['exponential', 'Exponential Exp(θ)'],
        ['poisson', 'Poisson Pois(θ)'],
        ['normal_mean', 'Normal Mean N(θ, 1)']
      ]) + f('theta', 'Parameter θ', 1.0, 0.2, 5.0, 0.2) + f('n', 'Sample Size n', 20, 5, 100, 5);
    }
    if(type === 'stat-est-likelihood-surface'){
      title = 'Likelihood Surface, Curvature & Profile Confidence Cutoff';
      note = 'Plots the normalized log-likelihood curve ℓ(θ) - ℓ(θ̂) and demonstrates how the peak determines the MLE while curvature determines the Fisher information.';
      controls = s('dist', 'Model Family', [
        ['exponential', 'Exponential Exp(θ)'],
        ['normal', 'Normal N(θ, 1)'],
        ['bernoulli', 'Bernoulli Proportion p']
      ]) + f('theta0', 'True Parameter θ₀', 1.5, 0.5, 4.0, 0.25) + f('n', 'Sample Size n', 25, 10, 80, 5);
    }
    if(type === 'stat-est-ci-coverage'){
      title = 'Confidence Interval Coverage & Repeated Sampling Simulator';
      note = 'Generates 40 independent random samples from N(10, 4) and displays their confidence intervals. Green segments capture true μ = 10, red segments miss.';
      controls = s('conf', 'Nominal Confidence Level', [
        ['0.95', '95% Confidence'],
        ['0.90', '90% Confidence'],
        ['0.80', '80% Confidence'],
        ['0.99', '99% Confidence']
      ]) + s('itype', 'Interval Type', [
        ['t_interval', "Student's t-interval (s unknown)"],
        ['z_interval', 'Standard Normal z-interval (σ known)']
      ]) + f('n', 'Sample Size n', 15, 5, 40, 1);
    }
    if(type === 'stat-est-bayes-updater'){
      title = 'Conjugate Normal-Normal Bayesian Posterior Updating';
      note = 'Visualizes Bayesian shrinkage: the prior distribution (yellow dashed) blends with the observed sample likelihood (cyan dotted) to form the posterior (green solid).';
      controls = f('mu0', 'Prior Mean μ₀', 0.0, -3.0, 3.0, 0.5)
        + f('tau0', 'Prior Precision τ₀', 1.0, 0.2, 4.0, 0.2)
        + f('xbar', 'Sample Mean x̄', 2.0, -4.0, 4.0, 0.5)
        + f('n', 'Sample Size n', 10, 1, 50, 1);
    }

    el.innerHTML = `
      <div class="prob-header">
        <div>
          <h3 class="prob-title">${title}</h3>
          <p class="prob-note">${note}</p>
        </div>
        <button type="button" class="prob-reset" data-reset>Reset</button>
      </div>
      <div class="prob-controls">${controls}</div>
      <div class="prob-result" data-result></div>
    `;

    const inputs = el.querySelectorAll('input, select');
    const result = el.querySelector('[data-result]');
    const initial = Array.from(inputs).map(inp => inp.value);

    function get(k){
      const target = el.querySelector('#' + containerId + '-' + k);
      if(!target) return null;
      return target.tagName === 'SELECT' ? target.value : parseFloat(target.value);
    }

    function render(){
      try{
        let values = {}, plot = '';
        if(type === 'stat-est-crlb-explorer'){
          const dist = get('dist'), theta = get('theta'), n = get('n');
          const m = crlbModel(dist, theta, n);
          values = {
            'Model': m.dist.toUpperCase(),
            'True Parameter θ': fmt(m.theta),
            'Sample Size n': m.n,
            'Single Observation Fisher Info I₁(θ)': fmt(m.i1),
            'Total Fisher Info I_n(θ)': fmt(m.totalInfo),
            'Theoretical CRLB (1 / I_n)': fmt(m.crlb),
            'Empirical Monte Carlo Var(T)': fmt(m.empVar),
            'Empirical Efficiency (CRLB / Var)': fmt(m.eff * 100) + '%'
          };
          plot = chart([
            { values: m.curve, width: 2.5, color: '#38bdf8' },
            { values: [[m.n, m.empVar]], width: 6, color: '#f59e0b' }
          ], 5, 100, 'CRLB (Blue Curve) vs Empirical Variance (Yellow Point)', m.n);
        }
        if(type === 'stat-est-likelihood-surface'){
          const dist = get('dist'), theta0 = get('theta0'), n = get('n');
          const m = likelihoodModel(dist, theta0, n);
          values = {
            'Model Family': m.dist.toUpperCase(),
            'True θ₀': fmt(m.theta0),
            'Sample Size n': m.n,
            'Maximum Likelihood Estimate θ̂': fmt(m.mle),
            'Log-Likelihood Cutoff Δℓ': fmt(m.cutoff)
          };
          plot = chart([
            { values: m.normCurve, width: 2.5, color: '#10b981' }
          ], m.tMin, m.tMax, 'Log-Likelihood Function ℓ(θ) - ℓ(θ̂)', m.mle, m.cutoff);
        }
        if(type === 'stat-est-ci-coverage'){
          const conf = get('conf'), itype = get('itype'), n = get('n');
          const m = ciCoverageModel(conf, n, itype);
          values = {
            'Target Parameter μ': fmt(m.muTrue),
            'Nominal Confidence Level': fmt(conf * 100) + '%',
            'Sample Size n': m.n,
            'Simulated Realizations': m.intervals.length,
            'Empirical Coverage Rate': fmt(m.coverageRate) + '%',
            'Mean Interval Width': fmt(m.avgWidth)
          };
          plot = renderCiChart(m);
        }
        if(type === 'stat-est-bayes-updater'){
          const mu0 = get('mu0'), tau0 = get('tau0'), xbar = get('xbar'), n = get('n');
          const m = bayesUpdaterModel(mu0, tau0, xbar, n, 1.0);
          values = {
            'Prior Mean μ₀': fmt(m.mu0),
            'Sample Mean x̄': fmt(m.xbar),
            'Sample Size n': m.n,
            'Posterior Mean μ_n': fmt(m.muN),
            'Posterior SD σ_n': fmt(m.sigN),
            '95% Credible Interval': `[${fmt(m.hpdLow)}, ${fmt(m.hpdHigh)}]`
          };
          plot = chart([
            { values: m.priorCurve, width: 2, dashed: true, color: '#fbbf24' },
            { values: m.likCurve, width: 2, dotted: true, color: '#38bdf8' },
            { values: m.postCurve, width: 2.5, color: '#10b981' }
          ], m.xMin, m.xMax, 'Bayesian Updating: Prior (Yellow), Likelihood (Cyan), Posterior (Green)');
        }
        result.innerHTML = summary(values) + plot;
      }catch(err){
        result.textContent = err.message;
      }
    }

    inputs.forEach(input => input.addEventListener(input.tagName === 'SELECT' ? 'change' : 'input', render));
    el.querySelector('[data-reset]').addEventListener('click', () => {
      inputs.forEach((input, i) => input.value = initial[i]);
      render();
    });
    render();
  }

  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = initSimulation;
  root.StatisticalEstimationSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
