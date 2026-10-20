/* Statistical Computing teaching models and interactive Canvas/SVG visualizers. */
(function(root){
  'use strict';
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
    let s = (seed >>> 0) || 20261015;
    return () => {
      s = (s + 0x6D2B79F5) >>> 0;
      let t = s;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  // Box-Muller standard normal draw
  function randn(random){
    let u = 0, v = 0;
    while(u === 0) u = random();
    while(v === 0) v = random();
    return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
  }

  // 1. Floating-Point Catastrophic Cancellation vs Welford Algorithm Model
  function floatingPointModel(shiftExp, n, seed = 20261015){
    range(shiftExp, 1, 9, 'Shift exponent log10(c)');
    integer(n, 10, 5000, 'Sample size n');
    const random = rng(seed);
    const c = Math.pow(10, shiftExp);
    
    // Generate true points: x_i = c + z_i where z_i ~ N(0, 1)
    const z = [];
    for(let i = 0; i < n; i++) z.push(randn(random));
    
    // Exact sample variance of z (centered at 0)
    let sumZ = 0, sumZ2 = 0;
    for(let i = 0; i < n; i++){
      sumZ += z[i];
      sumZ2 += z[i] * z[i];
    }
    const trueVar = (sumZ2 - (sumZ * sumZ) / n) / (n - 1);
    
    // Naive one-pass formula on shifted x_i = c + z_i
    let sumX = 0, sumX2 = 0;
    for(let i = 0; i < n; i++){
      const x = c + z[i];
      sumX += x;
      sumX2 += x * x;
    }
    const naiveVar = (sumX2 - (sumX * sumX) / n) / (n - 1);

    // Welford's algorithm on shifted x_i
    let count = 0, mean = 0, M2 = 0;
    for(let i = 0; i < n; i++){
      const x = c + z[i];
      count++;
      const delta = x - mean;
      mean += delta / count;
      const delta2 = x - mean;
      M2 += delta * delta2;
    }
    const welfordVar = M2 / (n - 1);

    const naiveError = Math.abs(naiveVar - trueVar);
    const naiveRelError = trueVar > 0 ? naiveError / trueVar : 0;
    const welfordError = Math.abs(welfordVar - trueVar);
    const welfordRelError = trueVar > 0 ? welfordError / trueVar : 0;

    // Error curve across shift exponents 1 to 9
    const curveNaive = [];
    const curveWelford = [];
    for(let exp = 1; exp <= 9; exp += 0.5){
      const currC = Math.pow(10, exp);
      let sX = 0, sX2 = 0, wM = 0, wM2 = 0;
      for(let i = 0; i < n; i++){
        const x = currC + z[i];
        sX += x;
        sX2 += x * x;
        const d = x - wM;
        wM += d / (i + 1);
        wM2 += d * (x - wM);
      }
      const nv = (sX2 - (sX * sX) / n) / (n - 1);
      const wv = wM2 / (n - 1);
      const errN = Math.max(1e-16, Math.abs(nv - trueVar) / trueVar);
      const errW = Math.max(1e-16, Math.abs(wv - trueVar) / trueVar);
      curveNaive.push([exp, Math.min(10, Math.log10(errN))]);
      curveWelford.push([exp, Math.min(10, Math.log10(errW))]);
    }

    return {
      c, n, trueVar, naiveVar, welfordVar,
      naiveRelError, welfordRelError,
      curveNaive, curveWelford
    };
  }

  // 2. Acceptance-Rejection Sampling Engine
  function rejectionSamplingModel(cMultiplier, targetN, seed = 20261015){
    range(cMultiplier, 1.0, 3.5, 'Bounding constant factor');
    integer(targetN, 50, 2000, 'Target accepted samples N');
    const random = rng(seed);

    // Target f(x): Standard Half-Normal on [0, 4]: f(x) = sqrt(2/pi) exp(-x^2 / 2)
    // Proposal g(x): Exponential(1): g(x) = exp(-x)
    // Optimal c* = sqrt(2e / pi) approx 1.315489
    const cOptimal = Math.sqrt(2.0 * Math.E / Math.PI);
    const c = cOptimal * cMultiplier;

    let totalTrials = 0;
    const accepted = [];
    while(accepted.length < targetN && totalTrials < 50000){
      totalTrials++;
      // Draw proposal Y ~ Exp(1) -> Y = -ln(U)
      const u1 = random();
      const y = -Math.log(u1);
      if(y > 4.0) continue; // truncate for visualization
      const fy = Math.sqrt(2.0 / Math.PI) * Math.exp(-0.5 * y * y);
      const gy = Math.exp(-y);
      const u2 = random();
      if(u2 <= fy / (c * gy)){
        accepted.push(y);
      }
    }

    const empiricalAcceptanceRate = accepted.length / totalTrials;
    const theoreticalAcceptanceRate = 1.0 / c;

    // Histogram of accepted samples (16 bins between 0 and 3.5)
    const bins = 16;
    const maxVal = 3.5;
    const binWidth = maxVal / bins;
    const binCounts = new Array(bins).fill(0);
    accepted.forEach(val => {
      const idx = Math.min(bins - 1, Math.floor(val / binWidth));
      if(idx >= 0) binCounts[idx]++;
    });
    // Normalized density heights
    const hist = binCounts.map((count, idx) => [
      (idx + 0.5) * binWidth,
      count / (accepted.length * binWidth)
    ]);

    // Theoretical curves
    const targetCurve = [];
    const envelopeCurve = [];
    for(let x = 0; x <= maxVal; x += 0.05){
      const fx = Math.sqrt(2.0 / Math.PI) * Math.exp(-0.5 * x * x);
      const cgy = c * Math.exp(-x);
      targetCurve.push([x, fx]);
      envelopeCurve.push([x, cgy]);
    }

    return {
      c, targetN, totalTrials,
      empiricalAcceptanceRate, theoreticalAcceptanceRate,
      hist, targetCurve, envelopeCurve
    };
  }

  // 3. Nonparametric Bootstrap Resampling Model
  function bootstrapModel(sampleSize, replicatesB, statType = 'mean', seed = 20261015){
    integer(sampleSize, 15, 200, 'Original sample size n');
    integer(replicatesB, 100, 2500, 'Bootstrap replicates B');
    const random = rng(seed);

    // Generate right-skewed initial sample from Log-Normal(0, 0.6)
    const originalSample = [];
    for(let i = 0; i < sampleSize; i++){
      originalSample.push(Math.exp(0.6 * randn(random)));
    }

    function calcStat(arr){
      if(statType === 'median'){
        const sorted = [...arr].sort((a,b) => a - b);
        const mid = Math.floor(sorted.length / 2);
        return sorted.length % 2 !== 0 ? sorted[mid] : (sorted[mid - 1] + sorted[mid]) / 2;
      }
      // default: mean
      return arr.reduce((a, b) => a + b, 0) / arr.length;
    }

    const origStat = calcStat(originalSample);

    // Bootstrap resampling
    const bootStats = [];
    for(let b = 0; b < replicatesB; b++){
      const resample = [];
      for(let i = 0; i < sampleSize; i++){
        const idx = Math.floor(random() * sampleSize);
        resample.push(originalSample[idx]);
      }
      bootStats.push(calcStat(resample));
    }
    bootStats.sort((a, b) => a - b);

    let bootSum = 0;
    bootStats.forEach(v => bootSum += v);
    const bootMean = bootSum / replicatesB;

    let bootVarSum = 0;
    bootStats.forEach(v => bootVarSum += (v - bootMean) * (v - bootMean));
    const bootSE = Math.sqrt(bootVarSum / (replicatesB - 1));
    const bootBias = bootMean - origStat;

    // 95% Percentile Confidence Interval
    const loIdx = Math.floor(replicatesB * 0.025);
    const hiIdx = Math.floor(replicatesB * 0.975);
    const ciPercentile = [bootStats[loIdx], bootStats[hiIdx]];

    // 95% Normal Approximation CI
    const ciNormal = [origStat - 1.96 * bootSE, origStat + 1.96 * bootSE];

    // Histogram of bootstrap distribution
    const minVal = bootStats[0];
    const maxVal = bootStats[replicatesB - 1];
    const numBins = 20;
    const binW = (maxVal - minVal) / numBins;
    const counts = new Array(numBins).fill(0);
    bootStats.forEach(v => {
      const idx = Math.min(numBins - 1, Math.floor((v - minVal) / binW));
      counts[idx]++;
    });
    const hist = counts.map((cnt, i) => [
      minVal + (i + 0.5) * binW,
      cnt / (replicatesB * binW)
    ]);

    return {
      sampleSize, replicatesB, statType,
      origStat, bootMean, bootSE, bootBias,
      ciPercentile, ciNormal,
      hist, minVal, maxVal
    };
  }

  // 4. 2D Objective Optimization Explorer (Rosenbrock & Quadratic Bowl)
  function optimizationModel(method, lr, maxIter, funcType = 'quad'){
    range(lr, 0.001, 1.0, 'Learning rate / step size');
    integer(maxIter, 5, 100, 'Max iterations');

    // Define function and gradient
    let f, grad;
    let startX = 2.0, startY = 2.5;
    if(funcType === 'rosenbrock'){
      // f(x, y) = (1 - x)^2 + 10 * (y - x^2)^2 (scaled Rosenbrock)
      f = (x, y) => Math.pow(1 - x, 2) + 10 * Math.pow(y - x * x, 2);
      grad = (x, y) => [
        -2 * (1 - x) - 40 * x * (y - x * x),
        20 * (y - x * x)
      ];
      startX = -1.2; startY = 1.0;
    } else {
      // Anisotropic quadratic bowl: f(x, y) = x^2 + 5 * y^2
      f = (x, y) => x * x + 5 * y * y;
      grad = (x, y) => [2 * x, 10 * y];
    }

    const trajectory = [[startX, startY]];
    let curX = startX, curY = startY;

    if(method === 'gd'){
      // Gradient Descent
      for(let i = 0; i < maxIter; i++){
        const [gx, gy] = grad(curX, curY);
        curX = curX - lr * gx;
        curY = curY - lr * gy;
        trajectory.push([curX, curY]);
        if(Math.sqrt(gx * gx + gy * gy) < 1e-4) break;
      }
    } else if(method === 'momentum'){
      // Momentum Gradient Descent
      let vx = 0, vy = 0;
      const beta = 0.85;
      for(let i = 0; i < maxIter; i++){
        const [gx, gy] = grad(curX, curY);
        vx = beta * vx + (1 - beta) * gx;
        vy = beta * vy + (1 - beta) * gy;
        curX = curX - lr * vx;
        curY = curY - lr * vy;
        trajectory.push([curX, curY]);
        if(Math.sqrt(gx * gx + gy * gy) < 1e-4) break;
      }
    } else if(method === 'newton'){
      // Newton-Raphson
      for(let i = 0; i < maxIter; i++){
        if(funcType === 'quad'){
          // Hessian is diag(2, 10), inverse is diag(0.5, 0.1)
          const [gx, gy] = grad(curX, curY);
          curX = curX - 0.5 * gx;
          curY = curY - 0.1 * gy;
        } else {
          // Damped Newton step on Rosenbrock
          const [gx, gy] = grad(curX, curY);
          const h11 = 2 - 40 * (curY - 3 * curX * curX);
          const h12 = -40 * curX;
          const h22 = 20;
          const det = h11 * h22 - h12 * h12 + 1e-3; // regularized
          const inv11 = h22 / det;
          const inv12 = -h12 / det;
          const inv22 = h11 / det;
          const dx = inv11 * gx + inv12 * gy;
          const dy = inv12 * gx + inv22 * gy;
          curX = curX - lr * dx;
          curY = curY - lr * dy;
        }
        trajectory.push([curX, curY]);
        if(Math.abs(curX - 1) < 1e-3 && Math.abs(curY - 1) < 1e-3) break;
      }
    }

    const finalVal = f(curX, curY);
    const iters = trajectory.length - 1;

    return {
      method, lr, maxIter, funcType,
      startX, startY, finalX: curX, finalY: curY,
      finalVal, iters, trajectory
    };
  }

  const api = {
    floatingPointModel,
    rejectionSamplingModel,
    bootstrapModel,
    optimizationModel
  };

  if(typeof module !== 'undefined' && module.exports) module.exports = api;
  if(root) root.StatisticalComputingMath = api;
  if(!root) return;

  const doc = root.document;
  const fmt = v => v === null ? 'Undefined' : Number.isFinite(v) ? Number(v.toFixed(6)).toLocaleString('en-US', {maximumFractionDigits: 6}) : 'Unavailable';

  function field(id, label, value, min, max, step = 1){
    return `<label for="${id}">${label}<input id="${id}" type="number" value="${value}" min="${min}" max="${max}" step="${step}"></label>`;
  }
  function select(id, label, options){
    return `<label for="${id}">${label}<select id="${id}">${options.map(([v, t]) => `<option value="${v}">${t}</option>`).join('')}</select></label>`;
  }
  function summary(values){
    return '<dl class="prob-summary">' + Object.entries(values).map(([k, v]) => `<div><dt>${k}</dt><dd>${typeof v === 'string' ? v : fmt(v)}</dd></div>`).join('') + '</dl>';
  }

  function chart(series, lo, hi, label, reference, yRange){
    const ymin = yRange ? yRange[0] : 0;
    const ymax = yRange ? yRange[1] : Math.max(0.01, ...series.flatMap(s => s.values.map(p => p[1])), reference || 0) * 1.15;
    const px = x => 50 + 520 * (x - lo) / Math.max(1e-6, hi - lo);
    const py = y => 205 - 170 * (y - ymin) / Math.max(1e-6, ymax - ymin);

    let html = '<line x1="50" y1="205" x2="570" y2="205" stroke="currentColor"/><line x1="50" y1="35" x2="50" y2="205" stroke="currentColor"/>';
    if(reference !== undefined){
      html += `<line x1="50" y1="${py(reference)}" x2="570" y2="${py(reference)}" stroke="#fbbf24" stroke-dasharray="5 4"/>`;
    }

    series.forEach((s, j) => {
      const color = ['#38bdf8', '#fbbf24', '#a78bfa', '#34d399'][j % 4];
      if(s.bars){
        const width = Math.min(28, 450 / (s.values.length + 1));
        s.values.forEach(([x, y]) => {
          html += `<rect x="${px(x) - width/2}" y="${py(y)}" width="${width}" height="${Math.max(1, 205 - py(y))}" fill="${color}" opacity=".7"/>`;
        });
      } else {
        html += `<path d="${s.values.map(([x,y], i) => (i ? 'L' : 'M') + px(x).toFixed(2) + ' ' + py(y).toFixed(2)).join(' ')}" fill="none" stroke="${color}" stroke-width="${s.width || 2.5}" ${s.dashed ? 'stroke-dasharray="4 3"' : ''}/>`;
      }
    });

    for(let i = 0; i < 5; i++){
      const x = lo + (hi - lo) * i / 4;
      html += `<text x="${px(x)}" y="228" fill="currentColor" text-anchor="middle">${fmt(x)}</text>`;
    }
    html += `<text x="43" y="40" fill="currentColor" text-anchor="end">${fmt(ymax)}</text><text x="42" y="208" fill="currentColor" text-anchor="end">${fmt(ymin)}</text>`;
    return `<svg viewBox="0 0 620 245" role="img" aria-label="${label}" class="prob-chart"><title>${label}</title>${html}</svg>`;
  }

  function contourPlot(trajectory, funcType){
    // 2D plane: X in [-2, 2.5], Y in [-1, 3]
    const xMin = -2.0, xMax = 2.5;
    const yMin = -1.0, yMax = 3.0;
    const px = x => 50 + 520 * (x - xMin) / (xMax - xMin);
    const py = y => 205 - 170 * (y - yMin) / (yMax - yMin);

    let html = '<rect x="50" y="35" width="520" height="170" fill="rgba(15, 23, 42, 0.4)" stroke="currentColor"/>';

    // Ellipses or contour rings
    if(funcType === 'quad'){
      for(let r = 0.5; r <= 3.5; r += 0.6){
        const rx = 520 * r / (xMax - xMin);
        const ry = 170 * (r / Math.sqrt(5)) / (yMax - yMin);
        html += `<ellipse cx="${px(0)}" cy="${py(0)}" rx="${rx}" ry="${ry}" fill="none" stroke="rgba(148, 163, 184, 0.25)" stroke-width="1.5"/>`;
      }
      html += `<circle cx="${px(0)}" cy="${py(0)}" r="4" fill="#34d399"/>`;
    } else {
      // Rosenbrock minimum at (1, 1)
      html += `<circle cx="${px(1)}" cy="${py(1)}" r="4" fill="#34d399"/>`;
      for(let c = 0.2; c <= 4; c += 0.8){
        const pts = [];
        for(let x = -1.5; x <= 2.2; x += 0.1){
          const y = x * x + c * 0.1;
          if(y <= yMax && y >= yMin) pts.push([x, y]);
        }
        if(pts.length > 1){
          html += `<path d="${pts.map(([x,y], i) => (i ? 'L' : 'M') + px(x).toFixed(1) + ' ' + py(y).toFixed(1)).join(' ')}" fill="none" stroke="rgba(148, 163, 184, 0.25)" stroke-width="1"/>`;
        }
      }
    }

    // Trajectory path
    const pathStr = trajectory.map(([x, y], i) => (i ? 'L' : 'M') + px(x).toFixed(1) + ' ' + py(y).toFixed(1)).join(' ');
    html += `<path d="${pathStr}" fill="none" stroke="#fbbf24" stroke-width="2.5"/>`;

    // Start and end markers
    const [sx, sy] = trajectory[0];
    const [ex, ey] = trajectory[trajectory.length - 1];
    html += `<circle cx="${px(sx)}" cy="${py(sy)}" r="5" fill="#38bdf8"/>`;
    html += `<circle cx="${px(ex)}" cy="${py(ey)}" r="5" fill="#f43f5e"/>`;

    // Labels
    html += `<text x="${px(sx) + 8}" y="${py(sy) - 5}" fill="#38bdf8" font-size="12">Start (${sx.toFixed(1)}, ${sy.toFixed(1)})</text>`;
    html += `<text x="${px(ex) + 8}" y="${py(ey) - 5}" fill="#f43f5e" font-size="12">End (${ex.toFixed(2)}, ${ey.toFixed(2)})</text>`;

    return `<svg viewBox="0 0 620 245" role="img" aria-label="Optimization Trajectory on 2D Contour" class="prob-chart"><title>Optimization Trajectory</title>${html}</svg>`;
  }

  function initSimulation(containerId, type){
    const el = doc.getElementById(containerId);
    if(!el || el.dataset.simMounted) return;
    el.dataset.simMounted = 'true';
    el.classList.add('prob-explorer');

    let title = '', note = '', controls = '';
    const f = (key, label, value, min, max, step) => field(containerId + '-' + key, label, value, min, max, step);
    const s = (key, label, options) => select(containerId + '-' + key, label, options);

    if(type === 'comp-floating-point'){
      title = 'Catastrophic Cancellation vs Welford Online Variance Explorer';
      note = 'Demonstrates the numerical breakdown of the textbook naive one-pass variance formula as data magnitude c = 10^k increases relative to variance sigma^2 = 1. Blue curve: Log10 relative error of naive formula; Yellow dashed line: Welford online algorithm precision.';
      controls = f('shift', 'Data magnitude exponent log10(c)', 6, 1, 9, 0.5) + f('n', 'Sample size n', 100, 10, 2000, 50);
    }
    if(type === 'comp-rejection-sampling'){
      title = 'Von Neumann Acceptance-Rejection Envelope Simulator';
      note = 'Simulates draws from Half-Normal f(x) using Exponential g(x) bounded by c * g(x). Yellow dashed curve: envelope function c * g(x); Blue curve: target density f(x); Blue bars: empirical histogram of accepted random variates.';
      controls = f('cMult', 'Envelope expansion factor (c / c*)', 1.15, 1.0, 3.0, 0.05) + f('n', 'Accepted samples target N', 300, 50, 1500, 50);
    }
    if(type === 'comp-bootstrap'){
      title = 'Nonparametric Bootstrap Resampling & Confidence Interval Explorer';
      note = 'Generates B bootstrap pseudo-replicates from an asymmetric empirical dataset. Compares 95% Percentile Confidence Interval with Normal-theory interval and quantifies finite-sample plug-in bias.';
      controls = s('stat', 'Statistic of interest', [['mean', 'Sample Mean'], ['median', 'Sample Median']]) +
                 f('n', 'Sample size n', 40, 15, 150, 5) +
                 f('B', 'Bootstrap replicates B', 500, 100, 2000, 100);
    }
    if(type === 'comp-optimization'){
      title = '2D Numerical Optimization Trajectory Explorer';
      note = 'Simulates numerical optimization paths over 2D surfaces. Compare standard Gradient Descent (GD), Momentum GD, and Newton-Raphson across quadratic and Rosenbrock valley geometries.';
      controls = s('func', 'Objective surface', [['quad', 'Anisotropic Quadratic Bowl'], ['rosenbrock', 'Rosenbrock Banana Valley']]) +
                 s('method', 'Optimization method', [['gd', 'Standard Gradient Descent'], ['momentum', 'Momentum GD (beta = 0.85)'], ['newton', 'Newton-Raphson']]) +
                 f('lr', 'Step size / Learning rate', 0.05, 0.005, 0.5, 0.005) +
                 f('iter', 'Max iterations', 40, 5, 100, 5);
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
        if(type === 'comp-floating-point'){
          const shift = get('shift'), n = get('n');
          const m = floatingPointModel(shift, n);
          values = {
            'Shift constant c': fmt(m.c),
            'Sample size n': m.n,
            'True sample variance': fmt(m.trueVar),
            'Welford algorithm estimate': fmt(m.welfordVar),
            'Naive textbook formula estimate': fmt(m.naiveVar),
            'Naive relative error': fmt(m.naiveRelError),
            'Welford relative error': fmt(m.welfordRelError),
            'Numerical condition': m.naiveRelError > 0.01 ? 'CATASTROPHIC CANCELLATION (Total loss of precision)' : 'Stable'
          };
          plot = chart([
            { values: m.curveNaive, width: 2.5 },
            { values: m.curveWelford, width: 2.0, dashed: true }
          ], 1, 9, 'Log10 relative error vs shift exponent: Blue = Naive formula, Yellow = Welford', undefined, [-16, 2]);
        }
        if(type === 'comp-rejection-sampling'){
          const cMult = get('cMult'), n = get('n');
          const m = rejectionSamplingModel(cMult, n);
          values = {
            'Envelope constant c': fmt(m.c),
            'Target accepted samples N': m.targetN,
            'Total candidate trials M': m.totalTrials,
            'Empirical acceptance rate': fmt(m.empiricalAcceptanceRate),
            'Theoretical rate (1 / c)': fmt(m.theoreticalAcceptanceRate),
            'Sampling efficiency': fmt(m.empiricalAcceptanceRate * 100) + '%'
          };
          plot = chart([
            { values: m.hist, bars: true },
            { values: m.targetCurve, width: 2.5 },
            { values: m.envelopeCurve, width: 2.0, dashed: true }
          ], 0, 3.5, 'Acceptance-Rejection: Bars = Accepted Variates, Blue = Target f(x), Yellow = Envelope c*g(x)');
        }
        if(type === 'comp-bootstrap'){
          const stat = get('stat'), n = get('n'), B = get('B');
          const m = bootstrapModel(n, B, stat);
          values = {
            'Original sample statistic': fmt(m.origStat),
            'Bootstrap replicates B': m.replicatesB,
            'Bootstrap mean estimate': fmt(m.bootMean),
            'Bootstrap standard error SE': fmt(m.bootSE),
            'Bootstrap estimated bias': fmt(m.bootBias),
            '95% Percentile interval': `[${fmt(m.ciPercentile[0])}, ${fmt(m.ciPercentile[1])}]`,
            '95% Normal-theory interval': `[${fmt(m.ciNormal[0])}, ${fmt(m.ciNormal[1])}]`
          };
          plot = chart([
            { values: m.hist, bars: true }
          ], m.minVal, m.maxVal, 'Bootstrap Distribution: Bars = Replicates, Yellow = Sample Statistic', m.origStat);
        }
        if(type === 'comp-optimization'){
          const funcType = get('func'), method = get('method'), lr = get('lr'), iter = get('iter');
          const m = optimizationModel(method, lr, iter, funcType);
          values = {
            'Optimization algorithm': m.method.toUpperCase(),
            'Objective surface': m.funcType === 'quad' ? 'Quadratic Bowl' : 'Rosenbrock Valley',
            'Iterations completed': m.iters,
            'Initial coordinates': `(${fmt(m.startX)}, ${fmt(m.startY)})`,
            'Final coordinates': `(${fmt(m.finalX)}, ${fmt(m.finalY)})`,
            'Final objective value f(x, y)': fmt(m.finalVal),
            'Convergence status': m.finalVal < 1e-3 ? 'Converged to global minimum' : 'In progress / Suboptimal'
          };
          plot = contourPlot(m.trajectory, m.funcType);
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
  root.StatisticalComputingSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
