/* Mathematical Statistics interactive teaching models and Canvas/SVG visualizers. */
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
    let s = (seed >>> 0) || 20261018;
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

  // Lanczos approximation for log-Gamma function ln(Gamma(x))
  function logGamma(z){
    const p = [
      676.5203681218851,
      -1259.1392167224028,
      771.32342877765313,
      -176.61502916214059,
      12.507343278686905,
      -0.13857109583115912,
      9.9843695780195716e-6,
      1.5056327351493116e-7
    ];
    if(z < 0.5){
      return Math.log(Math.PI) - Math.log(Math.sin(Math.PI * z)) - logGamma(1 - z);
    }
    z -= 1;
    let x = 0.99999999999980993;
    for(let i = 0; i < p.length; i++){
      x += p[i] / (z + i + 1);
    }
    const t = z + p.length - 0.5;
    return 0.5 * Math.log(2 * Math.PI) + (z + 0.5) * Math.log(t) - t + Math.log(x);
  }

  function gamma(z){
    return Math.exp(logGamma(z));
  }

  // 1. Sampling Distributions Model (Chi-square, Student's t, Snedecor's F)
  function samplingDistModel(distType, df1, df2){
    integer(df1, 1, 60, 'Degrees of freedom df1');
    if(distType === 'f') integer(df2, 1, 60, 'Degrees of freedom df2');

    let xMin = 0, xMax = 20, points = 120;
    let densityFunc;
    let meanVal = null, varVal = null;

    if(distType === 'chisq'){
      xMin = 0.05;
      xMax = Math.max(15, df1 * 2.5);
      densityFunc = (x) => {
        if(x <= 0) return 0;
        const k = df1;
        const logPdf = (k / 2 - 1) * Math.log(x) - x / 2 - (k / 2) * Math.log(2) - logGamma(k / 2);
        return Math.exp(logPdf);
      };
      meanVal = df1;
      varVal = 2 * df1;
    } else if(distType === 't'){
      xMin = -4.5;
      xMax = 4.5;
      densityFunc = (x) => {
        const v = df1;
        const logPdf = logGamma((v + 1) / 2) - logGamma(v / 2) - 0.5 * Math.log(v * Math.PI) - ((v + 1) / 2) * Math.log(1 + (x * x) / v);
        return Math.exp(logPdf);
      };
      meanVal = df1 > 1 ? 0 : 'Undefined';
      varVal = df1 > 2 ? df1 / (df1 - 2) : (df1 > 1 ? 'Infinite' : 'Undefined');
    } else if(distType === 'f'){
      xMin = 0.02;
      xMax = 5.0;
      const d1 = df1, d2 = df2;
      densityFunc = (x) => {
        if(x <= 0) return 0;
        const num = Math.pow(d1 * x, d1) * Math.pow(d2, d2);
        const den = Math.pow(d1 * x + d2, d1 + d2);
        const logPdf = 0.5 * Math.log(num / den) - Math.log(x) - (logGamma(d1 / 2) + logGamma(d2 / 2) - logGamma((d1 + d2) / 2));
        return Math.exp(logPdf);
      };
      meanVal = d2 > 2 ? d2 / (d2 - 2) : 'Undefined';
      varVal = d2 > 4 ? (2 * d2 * d2 * (d1 + d2 - 2)) / (d1 * (d2 - 2) * (d2 - 2) * (d2 - 4)) : 'Undefined';
    }

    const curve = [];
    const normalRef = [];
    const dx = (xMax - xMin) / (points - 1);
    for(let i = 0; i < points; i++){
      const x = xMin + i * dx;
      curve.push([x, densityFunc(x)]);
      if(distType === 't'){
        // Standard normal reference curve
        const normY = (1 / Math.sqrt(2 * Math.PI)) * Math.exp(-0.5 * x * x);
        normalRef.push([x, normY]);
      }
    }

    return {
      distType, df1, df2, xMin, xMax, curve, normalRef, meanVal, varVal
    };
  }

  // 2. Order Statistics Explorer Model
  function orderStatsModel(n, k, parent, sampleReps = 3000, seed = 20261018){
    integer(n, 2, 50, 'Sample size n');
    integer(k, 1, n, 'Order statistic rank k');
    const random = rng(seed);

    let drawSample;
    let xMin = 0, xMax = 1;
    let theoreticalPdf;

    if(parent === 'uniform'){
      drawSample = () => random();
      xMin = 0; xMax = 1;
      // Beta(k, n - k + 1) density
      theoreticalPdf = (x) => {
        if(x <= 0 || x >= 1) return 0;
        const a = k, b = n - k + 1;
        const logPdf = logGamma(a + b) - logGamma(a) - logGamma(b) + (a - 1) * Math.log(x) + (b - 1) * Math.log(1 - x);
        return Math.exp(logPdf);
      };
    } else if(parent === 'exponential'){
      // Exp(1)
      drawSample = () => -Math.log(random());
      xMin = 0; xMax = 5;
      theoreticalPdf = (x) => {
        if(x <= 0) return 0;
        const F = 1 - Math.exp(-x);
        const f = Math.exp(-x);
        const a = k, b = n - k + 1;
        const logFactorial = logGamma(n + 1) - logGamma(k) - logGamma(n - k + 1);
        const logPdf = logFactorial + (k - 1) * Math.log(F) + (n - k) * Math.log(1 - F) + Math.log(f);
        return Math.exp(logPdf);
      };
    } else { // standard normal
      drawSample = () => randn(random);
      xMin = -3.5; xMax = 3.5;
      theoreticalPdf = (x) => {
        // Normal CDF via erf approximation
        const z = x / Math.SQRT2;
        const t = 1.0 / (1.0 + 0.3275911 * Math.abs(z));
        const poly = t * (0.254829592 + t * (-0.284496736 + t * (1.421413741 + t * (-1.453152027 + t * 1.061405429))));
        const erf = 1.0 - poly * Math.exp(-z * z);
        const F = 0.5 * (1.0 + (z >= 0 ? erf : -erf));
        const f = (1 / Math.sqrt(2 * Math.PI)) * Math.exp(-0.5 * x * x);
        if(F <= 0 || F >= 1) return 0;
        const logFactorial = logGamma(n + 1) - logGamma(k) - logGamma(n - k + 1);
        const logPdf = logFactorial + (k - 1) * Math.log(F) + (n - k) * Math.log(1 - F) + Math.log(f);
        return Math.exp(logPdf);
      };
    }

    // Simulate empirical order statistic draws
    const empirical = [];
    for(let r = 0; r < sampleReps; r++){
      const s = [];
      for(let i = 0; i < n; i++) s.push(drawSample());
      s.sort((a, b) => a - b);
      empirical.push(s[k - 1]);
    }

    empirical.sort((a, b) => a - b);
    const meanEmp = empirical.reduce((a, b) => a + b, 0) / sampleReps;
    const medianEmp = empirical[Math.floor(sampleReps / 2)];
    const q05 = empirical[Math.floor(sampleReps * 0.05)];
    const q95 = empirical[Math.floor(sampleReps * 0.95)];

    // Build histogram
    const numBins = 30;
    const binWidth = (xMax - xMin) / numBins;
    const hist = [];
    for(let b = 0; b < numBins; b++){
      const bMin = xMin + b * binWidth;
      const bMax = bMin + binWidth;
      const count = empirical.filter(v => v >= bMin && v < bMax).length;
      hist.push([bMin + binWidth / 2, count / (sampleReps * binWidth)]);
    }

    // Theoretical curve
    const curve = [];
    const pts = 100;
    const step = (xMax - xMin) / (pts - 1);
    for(let i = 0; i < pts; i++){
      const x = xMin + i * step;
      curve.push([x, theoreticalPdf(x)]);
    }

    return {
      n, k, parent, xMin, xMax, hist, curve, meanEmp, medianEmp, q05, q95
    };
  }

  // 3. Central Limit Theorem Convergence Explorer
  function cltModel(parent, n, sampleReps = 3000, seed = 20261018){
    integer(n, 1, 80, 'Sample size n');
    const random = rng(seed);

    let drawSample, mu, sigma;
    if(parent === 'uniform'){
      drawSample = () => random();
      mu = 0.5;
      sigma = Math.sqrt(1 / 12);
    } else if(parent === 'exponential'){
      drawSample = () => -Math.log(random());
      mu = 1.0;
      sigma = 1.0;
    } else if(parent === 'bernoulli'){
      const p = 0.2;
      drawSample = () => (random() < p ? 1 : 0);
      mu = p;
      sigma = Math.sqrt(p * (1 - p));
    } else { // heavy skewed pareto
      const alpha = 3.0; // finite variance
      drawSample = () => Math.pow(1 - random(), -1 / alpha);
      mu = alpha / (alpha - 1); // 1.5
      sigma = Math.sqrt((alpha) / (Math.pow(alpha - 1, 2) * (alpha - 2))); // sqrt(3 / 4) = 0.866
    }

    // Generate normalized sample means: Z_n = sqrt(n) * (Xbar - mu) / sigma
    const zScores = [];
    for(let r = 0; r < sampleReps; r++){
      let sum = 0;
      for(let i = 0; i < n; i++) sum += drawSample();
      const xbar = sum / n;
      const z = (Math.sqrt(n) * (xbar - mu)) / sigma;
      zScores.push(z);
    }

    const xMin = -4.0, xMax = 4.0;
    const numBins = 32;
    const binWidth = (xMax - xMin) / numBins;
    const hist = [];
    for(let b = 0; b < numBins; b++){
      const bMin = xMin + b * binWidth;
      const bMax = bMin + binWidth;
      const count = zScores.filter(v => v >= bMin && v < bMax).length;
      hist.push([bMin + binWidth / 2, count / (sampleReps * binWidth)]);
    }

    // Standard Normal density reference curve
    const normCurve = [];
    const pts = 100;
    const step = (xMax - xMin) / (pts - 1);
    for(let i = 0; i < pts; i++){
      const x = xMin + i * step;
      normCurve.push([x, (1 / Math.sqrt(2 * Math.PI)) * Math.exp(-0.5 * x * x)]);
    }

    // Compute sample skewness & kurtosis of zScores
    const meanZ = zScores.reduce((a, b) => a + b, 0) / sampleReps;
    let m2 = 0, m3 = 0, m4 = 0;
    for(let i = 0; i < sampleReps; i++){
      const d = zScores[i] - meanZ;
      m2 += d * d;
      m3 += d * d * d;
      m4 += d * d * d * d;
    }
    m2 /= sampleReps;
    m3 /= sampleReps;
    m4 /= sampleReps;
    const skewness = m3 / Math.pow(m2, 1.5);
    const excessKurtosis = m4 / Math.pow(m2, 2) - 3.0;

    return {
      parent, n, hist, normCurve, xMin, xMax, skewness, excessKurtosis
    };
  }

  // 4. Delta Method Approximation Explorer
  function deltaMethodModel(funcType, n, mu, sampleReps = 3000, seed = 20261018){
    integer(n, 5, 100, 'Sample size n');
    range(mu, 0.5, 5.0, 'Parent mean mu');
    const random = rng(seed);

    // Parent is Exponential with mean mu => Var = mu^2
    const sigma = mu;
    let g, gPrime;
    if(funcType === 'sqrt'){
      g = (x) => Math.sqrt(x);
      gPrime = (x) => 1 / (2 * Math.sqrt(x));
    } else if(funcType === 'log'){
      g = (x) => Math.log(x);
      gPrime = (x) => 1 / x;
    } else if(funcType === 'reciprocal'){
      g = (x) => 1 / x;
      gPrime = (x) => -1 / (x * x);
    } else { // quadratic
      g = (x) => x * x;
      gPrime = (x) => 2 * x;
    }

    const gMu = g(mu);
    const asymptoticVar = Math.pow(gPrime(mu), 2) * (sigma * sigma);
    const asymptoticSE = Math.sqrt(asymptoticVar / n);

    // Simulate empirical draws of g(Xbar)
    const empG = [];
    for(let r = 0; r < sampleReps; r++){
      let sum = 0;
      for(let i = 0; i < n; i++) sum += -mu * Math.log(random());
      const xbar = sum / n;
      empG.push(g(xbar));
    }

    empG.sort((a, b) => a - b);
    const meanEmpG = empG.reduce((a, b) => a + b, 0) / sampleReps;
    let s2 = 0;
    for(let i = 0; i < sampleReps; i++){
      const d = empG[i] - meanEmpG;
      s2 += d * d;
    }
    const empSE = Math.sqrt(s2 / (sampleReps - 1));
    const empBias = meanEmpG - gMu;

    // Range for plotting
    const xMin = gMu - 3.5 * asymptoticSE;
    const xMax = gMu + 3.5 * asymptoticSE;
    const numBins = 30;
    const binWidth = (xMax - xMin) / numBins;
    const hist = [];
    for(let b = 0; b < numBins; b++){
      const bMin = xMin + b * binWidth;
      const bMax = bMin + binWidth;
      const count = empG.filter(v => v >= bMin && v < bMax).length;
      hist.push([bMin + binWidth / 2, count / (sampleReps * binWidth)]);
    }

    // Delta method Gaussian density curve
    const deltaCurve = [];
    const pts = 100;
    const step = (xMax - xMin) / (pts - 1);
    for(let i = 0; i < pts; i++){
      const x = xMin + i * step;
      const z = (x - gMu) / asymptoticSE;
      const pdf = (1 / (asymptoticSE * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * z * z);
      deltaCurve.push([x, pdf]);
    }

    return {
      funcType, n, mu, gMu, asymptoticSE, empSE, empBias, hist, deltaCurve, xMin, xMax
    };
  }

  // --- SVG UI & Rendering Engine ---
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

  function chart(seriesList, xMin, xMax, titleStr, vRef = null){
    const W = 620, H = 240, padL = 50, padR = 25, padT = 25, padB = 35;
    const plotW = W - padL - padR, plotH = H - padT - padB;

    let yMax = 0;
    seriesList.forEach(s => {
      s.values.forEach(([x, y]) => {
        if(Number.isFinite(y) && y > yMax) yMax = y;
      });
    });
    if(yMax <= 0) yMax = 1;
    yMax *= 1.15;

    const px = (x) => padL + ((x - xMin) / (xMax - xMin)) * plotW;
    const py = (y) => padT + plotH - (Math.max(0, y) / yMax) * plotH;

    let svg = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${titleStr}" class="prob-chart"><title>${titleStr}</title>`;
    // Background and axes
    svg += `<rect x="${padL}" y="${padT}" width="${plotW}" height="${plotH}" fill="rgba(15, 23, 42, 0.45)" rx="4"/>`;

    // Horizontal grid lines
    for(let i = 0; i <= 4; i++){
      const yVal = (yMax / 4) * i;
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
          const barH = (Math.max(0, y) / yMax) * plotH;
          svg += `<rect x="${px(x) - bW / 2}" y="${py(y)}" width="${bW}" height="${barH}" fill="rgba(56, 189, 248, 0.45)" stroke="#38bdf8" stroke-width="1"/>`;
        });
      } else {
        const d = s.values.map(([x, y], i) => (i === 0 ? 'M' : 'L') + px(x).toFixed(1) + ' ' + py(y).toFixed(1)).join(' ');
        const strokeColor = s.color || (s.dashed ? '#fbbf24' : '#38bdf8');
        const dashArr = s.dashed ? 'stroke-dasharray="4 3"' : '';
        svg += `<path d="${d}" fill="none" stroke="${strokeColor}" stroke-width="${s.width || 2}" ${dashArr}/>`;
      }
    });

    if(vRef !== null && Number.isFinite(vRef)){
      const rx = px(vRef);
      if(rx >= padL && rx <= padL + plotW){
        svg += `<line x1="${rx}" y1="${padT}" x2="${rx}" y2="${padT + plotH}" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>`;
        svg += `<text x="${rx + 4}" y="${padT + 14}" fill="#f43f5e" font-size="11">Ref: ${fmt(vRef)}</text>`;
      }
    }

    svg += `</svg>`;
    return svg;
  }

  function initSimulation(containerId, type){
    const el = doc.getElementById(containerId);
    if(!el || el.dataset.simMounted) return;
    el.dataset.simMounted = 'true';
    el.classList.add('prob-explorer');

    let title = '', note = '', controls = '';
    const f = (key, label, value, min, max, step) => field(containerId + '-' + key, label, value, min, max, step);
    const s = (key, label, options) => select(containerId + '-' + key, label, options);

    if(type === 'stat-sampling-dists'){
      title = 'Exact Sampling Distributions Explorer (Chi-Square, Student\'s t, Snedecor\'s F)';
      note = 'Visualizes density profiles and moments of foundational sampling distributions. Compare Student\'s t against Gaussian limits, and observe right-skewness dynamics of Chi-square and Snedecor\'s F.';
      controls = s('dist', 'Distribution Family', [['chisq', 'Chi-Square (df1)'], ['t', 'Student\'s t (df1) vs Normal'], ['f', 'Snedecor\'s F (df1, df2)']]) +
                 f('df1', 'Degrees of freedom df1 (or numerator)', 5, 1, 60, 1) +
                 f('df2', 'Degrees of freedom df2 (denominator for F)', 10, 1, 60, 1);
    }
    if(type === 'stat-order-stats'){
      title = 'Order Statistics & Quantile Distribution Simulator';
      note = 'Simulates empirical draws of the k-th order statistic X_(k) from a parent Uniform, Exponential, or Gaussian sample of size n. Compares empirical histogram with exact theoretical Beta-envelope density.';
      controls = s('parent', 'Parent Distribution', [['uniform', 'Standard Uniform (0, 1)'], ['exponential', 'Exponential (rate = 1)'], ['normal', 'Standard Normal N(0, 1)']]) +
                 f('n', 'Sample size n', 15, 2, 50, 1) +
                 f('k', 'Order rank k (1 = min, n = max)', 8, 1, 50, 1);
    }
    if(type === 'stat-clt-convergence'){
      title = 'Central Limit Theorem Convergence vs Normal Limit Explorer';
      note = 'Demonstrates the convergence of normalized sample means to standard normality N(0, 1). Observe how skewness and kurtosis vanish as n increases across Uniform, Exponential, Bernoulli, and Pareto parents.';
      controls = s('parent', 'Parent Population', [['uniform', 'Uniform [0, 1] (Symmetric)'], ['exponential', 'Exponential (Skewed)'], ['bernoulli', 'Bernoulli p = 0.2 (Discrete)'], ['pareto', 'Pareto alpha = 3 (Heavy Tail)']]) +
                 f('n', 'Sample size n', 10, 1, 80, 1);
    }
    if(type === 'stat-delta-method'){
      title = 'Delta Method Nonlinear Transformation Variance Explorer';
      note = 'Simulates empirical distribution of g(Xbar) from an Exponential sample of size n. Compares empirical histogram with Delta Method Gaussian approximation N(g(mu), [g\'(mu)]^2 * sigma^2 / n).';
      controls = s('func', 'Nonlinear Function g(x)', [['sqrt', 'Square Root: sqrt(x) (VST)'], ['log', 'Logarithm: ln(x)'], ['reciprocal', 'Reciprocal: 1 / x'], ['quad', 'Quadratic: x^2']]) +
                 f('n', 'Sample size n', 25, 5, 100, 5) +
                 f('mu', 'Parent Mean mu', 2.0, 0.5, 5.0, 0.5);
    }

    if(!title){ el.textContent = 'Unknown simulation.'; return; }
    el.innerHTML = `<h4>${title}</h4><p>${note}</p><div class="prob-fields">${controls}</div><button type="button" data-reset>Reset</button><div class="prob-results" role="status" aria-live="polite"></div>`;

    const inputs = [...el.querySelectorAll('input,select')];
    const initial = inputs.map(i => i.value);
    const result = el.querySelector('.prob-results');
    const get = key => {
      const input = doc.getElementById(containerId + '-' + key);
      return input.tagName === 'SELECT' ? input.value : (input.value.trim() === '' ? NaN : Number(input.value));
    };

    function render(){
      try{
        let values = {}, plot = '';
        if(type === 'stat-sampling-dists'){
          const distType = get('dist'), df1 = get('df1'), df2 = get('df2');
          const m = samplingDistModel(distType, df1, df2);
          values = {
            'Selected Distribution': distType.toUpperCase(),
            'Degrees of Freedom df1': m.df1,
            'Degrees of Freedom df2': distType === 'f' ? m.df2 : 'N/A',
            'Theoretical Mean': fmt(m.meanVal),
            'Theoretical Variance': fmt(m.varVal),
            'Limiting Behavior': distType === 't' ? 'Approaches N(0, 1) as df1 -> infinity' : (distType === 'chisq' ? 'Approaches Normal by CLT' : 'F-ratio of two chi-squares')
          };
          const series = [{ values: m.curve, width: 2.5, color: '#38bdf8' }];
          if(m.normalRef && m.normalRef.length){
            series.push({ values: m.normalRef, width: 2.0, dashed: true, color: '#fbbf24' });
          }
          plot = chart(series, m.xMin, m.xMax, 'Density function: Blue = Exact Density, Yellow dashed = N(0, 1) reference');
        }
        if(type === 'stat-order-stats'){
          const parent = get('parent'), n = get('n'), k = Math.min(get('k'), get('n'));
          const m = orderStatsModel(n, k, parent);
          values = {
            'Parent Population': parent.toUpperCase(),
            'Sample Size n': m.n,
            'Rank k': m.k + (m.k === 1 ? ' (Sample Minimum)' : (m.k === m.n ? ' (Sample Maximum)' : (m.k === Math.ceil(m.n / 2) ? ' (Sample Median)' : ''))),
            'Empirical Mean of X_(k)': fmt(m.meanEmp),
            'Empirical Median of X_(k)': fmt(m.medianEmp),
            'Empirical 90% Coverage': `[${fmt(m.q05)}, ${fmt(m.q95)}]`
          };
          plot = chart([
            { values: m.hist, bars: true },
            { values: m.curve, width: 2.5, color: '#fbbf24' }
          ], m.xMin, m.xMax, 'Order Statistic Distribution: Blue Bars = Monte Carlo Draws, Yellow Curve = Exact Theoretical Beta Envelope');
        }
        if(type === 'stat-clt-convergence'){
          const parent = get('parent'), n = get('n');
          const m = cltModel(parent, n);
          values = {
            'Parent Distribution': parent.toUpperCase(),
            'Sample Size n': m.n,
            'Sample Skewness': fmt(m.skewness),
            'Excess Kurtosis': fmt(m.excessKurtosis),
            'Normality Approximation': Math.abs(m.skewness) < 0.15 && Math.abs(m.excessKurtosis) < 0.25 ? 'High Gaussian Fidelity' : 'Skewness / Kurtosis Drift Present'
          };
          plot = chart([
            { values: m.hist, bars: true },
            { values: m.normCurve, width: 2.5, dashed: true, color: '#fbbf24' }
          ], m.xMin, m.xMax, 'CLT Convergence: Blue Bars = Normalized Sample Mean Z_n, Yellow Dashed = Standard Normal N(0, 1)');
        }
        if(type === 'stat-delta-method'){
          const funcType = get('func'), n = get('n'), mu = get('mu');
          const m = deltaMethodModel(funcType, n, mu);
          values = {
            'Transformation g(x)': funcType === 'sqrt' ? 'sqrt(x)' : (funcType === 'log' ? 'ln(x)' : (funcType === 'reciprocal' ? '1 / x' : 'x^2')),
            'Sample Size n': m.n,
            'Target Value g(mu)': fmt(m.gMu),
            'Delta Method Asymptotic SE': fmt(m.asymptoticSE),
            'Simulated Empirical SE': fmt(m.empSE),
            'Finite-Sample Bias': fmt(m.empBias)
          };
          plot = chart([
            { values: m.hist, bars: true },
            { values: m.deltaCurve, width: 2.5, color: '#fbbf24' }
          ], m.xMin, m.xMax, 'Delta Method Approximation: Blue Bars = Empirical g(Xbar), Yellow Curve = Delta Method Gaussian N(g(mu), V / n)');
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
  root.MathematicalStatisticsSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
