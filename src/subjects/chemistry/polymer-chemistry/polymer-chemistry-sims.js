/**
 * polymer-chemistry-sims.js
 * 10 High-Performance 60 FPS Interactive HTML5 Canvas Simulation Engines
 * for Polymer Chemistry (OpenSTEM Milestone Textbook #54)
 * Equipped with Dimension-Caching, DPR Scaling, and isConnected Cleanup Guards.
 */

window.PolymerChemistrySimulations = (function() {
  'use strict';

  // High-DPI canvas initialization with dimensions caching to prevent per-frame GPU allocations
  function initCanvas(canvas) {
    if (!canvas) return null;
    const dpr = window.devicePixelRatio || 1;
    let w = canvas._cssWidth;
    let h = canvas._cssHeight;

    if (!w || !h) {
      const rect = canvas.getBoundingClientRect();
      w = Math.floor(rect.width > 0 ? rect.width : (canvas.parentElement ? canvas.parentElement.clientWidth : 800)) || 800;
      h = Math.floor(rect.height > 0 ? rect.height : (canvas.parentElement ? canvas.parentElement.clientHeight : 380)) || 380;
      canvas._cssWidth = w;
      canvas._cssHeight = h;
    }

    const targetW = Math.round(w * dpr);
    const targetH = Math.round(h * dpr);

    if (canvas.width !== targetW || canvas.height !== targetH) {
      canvas.width = targetW;
      canvas.height = targetH;
      const ctx = canvas.getContext('2d');
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    const ctx = canvas.getContext('2d');
    return { ctx, width: w, height: h, dpr };
  }

  if (typeof window !== 'undefined') {
    window.addEventListener('resize', function() {
      document.querySelectorAll('.sim-canvas').forEach(function(c) {
        c._cssWidth = null;
        c._cssHeight = null;
      });
    });
  }

  function getContainerEl(c) {
    return typeof c === 'string' ? document.getElementById(c) : c;
  }

  /* ==========================================================================
     SIMULATION 1: Macromolecular Chain Conformation (FJC vs SAW Random Coil)
     ========================================================================== */
  function sim_poly_chain_conformation(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #30363d; padding-bottom:8px; margin-bottom:12px;">
          <h4 style="margin:0; color:#58a6ff;">Random Coil Conformation: Freely Jointed Chain (FJC) vs Self-Avoiding Walk (SAW)</h4>
          <span style="font-size:12px; background:#238636; color:#fff; padding:2px 8px; border-radius:12px;">60 FPS Real-Time</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 280px; gap:16px;">
          <div>
            <canvas class="sim-canvas" style="width:100%; height:380px; background:#161b22; border-radius:6px; display:block;"></canvas>
            <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:#8b949e;">
              <span>• Blue: Head (Start)</span>
              <span>• Red: Tail (End)</span>
              <span>• Yellow Dash: End-to-End Vector R</span>
              <span>• Cyan Ring: Radius of Gyration Rg</span>
            </div>
          </div>
          <div style="background:#161b22; padding:12px; border-radius:6px; display:flex; flex-direction:column; gap:10px; font-size:13px;">
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Chain Model:</label>
              <select id="p1_model" style="width:100%; background:#21262d; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
                <option value="fjc">Freely Jointed Chain (Ideal FJC, theta)</option>
                <option value="saw" selected>Self-Avoiding Walk (SAW, Good Solvent)</option>
                <option value="worm">Wormlike Chain (Stiff / Semirigid)</option>
              </select>
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Segments (N): <span id="p1_n_val" style="color:#58a6ff;">150</span></label>
              <input type="range" id="p1_n" min="20" max="350" value="150" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Segment Length (b): <span id="p1_b_val" style="color:#58a6ff;">12 px</span></label>
              <input type="range" id="p1_b" min="6" max="24" value="12" style="width:100%;">
            </div>
            <div style="display:flex; gap:8px;">
              <button id="p1_regen" style="flex:1; background:#238636; color:#fff; border:none; padding:6px; border-radius:4px; cursor:pointer; font-weight:600;">Regenerate</button>
              <button id="p1_rotate" style="flex:1; background:#21262d; color:#c9d1d9; border:1px solid #30363d; padding:6px; border-radius:4px; cursor:pointer;">Rotate: ON</button>
            </div>
            <div style="border-top:1px solid #30363d; padding-top:8px; font-size:12px; line-height:1.6;">
              <div style="display:flex; justify-content:space-between;"><span>End-to-End |R|:</span><strong id="p1_r_val" style="color:#f0883e;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Theoretical &lang;R&sup2;&rang;&frac12;:</span><strong id="p1_r_theo" style="color:#f0883e;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Radius Gyration Rg:</span><strong id="p1_rg_val" style="color:#79c0ff;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Scaling Ratio R/Rg:</span><strong id="p1_ratio" style="color:#7ee787;">--</strong></div>
            </div>
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('canvas');
    const modelSelect = el.querySelector('#p1_model');
    const nSlider = el.querySelector('#p1_n');
    const bSlider = el.querySelector('#p1_b');
    const nVal = el.querySelector('#p1_n_val');
    const bVal = el.querySelector('#p1_b_val');
    const regenBtn = el.querySelector('#p1_regen');
    const rotateBtn = el.querySelector('#p1_rotate');
    const rVal = el.querySelector('#p1_r_val');
    const rTheo = el.querySelector('#p1_r_theo');
    const rgVal = el.querySelector('#p1_rg_val');
    const ratioVal = el.querySelector('#p1_ratio');

    let isRotating = true;
    let angle3D = 0;
    let chain = [];

    function generateChain() {
      const N = parseInt(nSlider.value, 10);
      const b = parseInt(bSlider.value, 10);
      const model = modelSelect.value;
      chain = [{ x: 0, y: 0, z: 0 }];

      let prevTheta = 0;
      let prevPhi = 0;

      for (let i = 1; i < N; i++) {
        let attempts = 0;
        let nextPt = null;

        while (attempts < 100) {
          let theta, phi;
          if (model === 'worm') {
            // High forward persistence: small angle deviation from previous step
            theta = prevTheta + (Math.random() - 0.5) * 0.7;
            phi = prevPhi + (Math.random() - 0.5) * 0.7;
          } else {
            theta = Math.acos(2 * Math.random() - 1);
            phi = 2 * Math.PI * Math.random();
          }

          const dx = b * Math.sin(theta) * Math.cos(phi);
          const dy = b * Math.sin(theta) * Math.sin(phi);
          const dz = b * Math.cos(theta);

          const candidate = {
            x: chain[i - 1].x + dx,
            y: chain[i - 1].y + dy,
            z: chain[i - 1].z + dz
          };

          if (model === 'saw') {
            // Check self-avoidance against all prior segments
            let collision = false;
            const threshold = b * 0.85;
            for (let j = 0; j < i - 1; j++) {
              const d2 = (candidate.x - chain[j].x)**2 + (candidate.y - chain[j].y)**2 + (candidate.z - chain[j].z)**2;
              if (d2 < threshold * threshold) {
                collision = true;
                break;
              }
            }
            if (!collision) {
              nextPt = candidate;
              prevTheta = theta;
              prevPhi = phi;
              break;
            }
            attempts++;
          } else {
            nextPt = candidate;
            prevTheta = theta;
            prevPhi = phi;
            break;
          }
        }

        if (!nextPt) {
          // If trapped in SAW, back up slightly or accept closest
          const theta = Math.random() * Math.PI;
          const phi = Math.random() * 2 * Math.PI;
          nextPt = {
            x: chain[i - 1].x + b * Math.sin(theta) * Math.cos(phi),
            y: chain[i - 1].y + b * Math.sin(theta) * Math.sin(phi),
            z: chain[i - 1].z + b * Math.cos(theta)
          };
        }
        chain.push(nextPt);
      }

      // Compute statistics
      const start = chain[0];
      const end = chain[chain.length - 1];
      const R = Math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2 + (end.z - start.z)**2);

      // Center of mass
      let cmX = 0, cmY = 0, cmZ = 0;
      chain.forEach(pt => { cmX += pt.x; cmY += pt.y; cmZ += pt.z; });
      cmX /= chain.length; cmY /= chain.length; cmZ /= chain.length;

      // Radius of gyration
      let sumSq = 0;
      chain.forEach(pt => {
        sumSq += (pt.x - cmX)**2 + (pt.y - cmY)**2 + (pt.z - cmZ)**2;
      });
      const Rg = Math.sqrt(sumSq / chain.length);

      // Theoretical R
      let R_theo;
      if (model === 'fjc') {
        R_theo = b * Math.sqrt(N);
      } else if (model === 'saw') {
        R_theo = b * Math.pow(N, 0.588); // Flory 3/5 power
      } else {
        R_theo = b * Math.sqrt(N * 2.5); // Stiff persistence
      }

      rVal.textContent = R.toFixed(1) + ' px';
      rTheo.textContent = R_theo.toFixed(1) + ' px';
      rgVal.textContent = Rg.toFixed(1) + ' px';
      ratioVal.textContent = (R / Rg).toFixed(2) + (model === 'fjc' ? ' (~2.45)' : '');
    }

    nSlider.addEventListener('input', () => { nVal.textContent = nSlider.value; generateChain(); });
    bSlider.addEventListener('input', () => { bVal.textContent = bSlider.value + ' px'; generateChain(); });
    modelSelect.addEventListener('change', generateChain);
    regenBtn.addEventListener('click', generateChain);
    rotateBtn.addEventListener('click', () => {
      isRotating = !isRotating;
      rotateBtn.textContent = 'Rotate: ' + (isRotating ? 'ON' : 'OFF');
    });

    generateChain();

    function render() {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) { requestAnimationFrame(render); return; }
      const { ctx, width, height } = c;

      ctx.clearRect(0, 0, width, height);

      // Center of mass
      let cmX = 0, cmY = 0, cmZ = 0;
      chain.forEach(pt => { cmX += pt.x; cmY += pt.y; cmZ += pt.z; });
      cmX /= chain.length; cmY /= chain.length; cmZ /= chain.length;

      if (isRotating) angle3D += 0.012;
      const cosA = Math.cos(angle3D);
      const sinA = Math.sin(angle3D);

      const cx = width / 2;
      const cy = height / 2;

      // Project points to 2D
      const proj = chain.map(pt => {
        const rx = pt.x - cmX;
        const ry = pt.y - cmY;
        const rz = pt.z - cmZ;
        const xRot = rx * cosA - rz * sinA;
        const zRot = rx * sinA + rz * cosA;
        const scale = 350 / (350 + zRot * 0.6);
        return {
          px: cx + xRot * scale,
          py: cy + ry * scale,
          depth: zRot,
          scale: scale
        };
      });

      // Draw bounding Rg sphere
      let sumSq = 0;
      chain.forEach(pt => { sumSq += (pt.x - cmX)**2 + (pt.y - cmY)**2 + (pt.z - cmZ)**2; });
      const Rg = Math.sqrt(sumSq / chain.length);
      ctx.beginPath();
      ctx.arc(cx, cy, Rg, 0, 2 * Math.PI);
      ctx.strokeStyle = 'rgba(121, 192, 255, 0.25)';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw end-to-end vector R
      if (proj.length > 1) {
        ctx.beginPath();
        ctx.moveTo(proj[0].px, proj[0].py);
        ctx.lineTo(proj[proj.length - 1].px, proj[proj.length - 1].py);
        ctx.strokeStyle = '#f0883e';
        ctx.lineWidth = 2;
        ctx.setLineDash([6, 3]);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Draw polymer chain segments with gradient
      for (let i = 0; i < proj.length - 1; i++) {
        ctx.beginPath();
        ctx.moveTo(proj[i].px, proj[i].py);
        ctx.lineTo(proj[i + 1].px, proj[i + 1].py);
        const t = i / (proj.length - 1);
        const r = Math.round(50 + 205 * t);
        const g = Math.round(150 * (1 - Math.abs(t - 0.5) * 2));
        const b = Math.round(255 * (1 - t));
        ctx.strokeStyle = `rgb(${r}, ${g}, ${b})`;
        ctx.lineWidth = Math.max(1, 2 * proj[i].scale);
        ctx.stroke();
      }

      // Draw monomers
      for (let i = 0; i < proj.length; i++) {
        const pt = proj[i];
        ctx.beginPath();
        const rad = i === 0 || i === proj.length - 1 ? 5 : 2.5 * pt.scale;
        ctx.arc(pt.px, pt.py, rad, 0, 2 * Math.PI);
        if (i === 0) {
          ctx.fillStyle = '#58a6ff'; // Start bead (blue)
        } else if (i === proj.length - 1) {
          ctx.fillStyle = '#f85149'; // End bead (red)
        } else {
          ctx.fillStyle = '#e6edf3';
        }
        ctx.fill();
      }

      // Text HUD
      ctx.fillStyle = '#8b949e';
      ctx.font = '11px sans-serif';
      ctx.fillText(`Model: ${modelSelect.options[modelSelect.selectedIndex].text}`, 12, 20);
      ctx.fillText(`Segments N = ${chain.length}`, 12, 36);

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }

  /* ==========================================================================
     SIMULATION 2: Flory-Huggins Polymer Solution Phase Diagram Generator
     ========================================================================== */
  function sim_poly_flory_huggins_phase_diagram(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #30363d; padding-bottom:8px; margin-bottom:12px;">
          <h4 style="margin:0; color:#58a6ff;">Flory-Huggins Lattice Solution Thermodynamics: Binodal & Spinodal Phase Curves</h4>
          <span style="font-size:12px; background:#1f6feb; color:#fff; padding:2px 8px; border-radius:12px;">Thermodynamic Phase Space</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 280px; gap:16px;">
          <div>
            <canvas class="sim-canvas" style="width:100%; height:380px; background:#161b22; border-radius:6px; display:block;"></canvas>
            <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:#8b949e;">
              <span>• Blue Curve: Binodal (Coexistence)</span>
              <span>• Red Curve: Spinodal (&part;&sup2;&Delta;G/&part;&phi;&sup2; = 0)</span>
              <span>• Gold Marker: Critical Point (&phi;c, Tc)</span>
            </div>
          </div>
          <div style="background:#161b22; padding:12px; border-radius:6px; display:flex; flex-direction:column; gap:10px; font-size:13px;">
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Chain Length (x or N): <span id="p2_x_val" style="color:#58a6ff;">500</span></label>
              <input type="range" id="p2_x" min="10" max="2500" value="500" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Theta Temp (&Theta;): <span id="p2_th_val" style="color:#58a6ff;">330 K (57 &deg;C)</span></label>
              <input type="range" id="p2_th" min="270" max="400" value="330" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Test Temperature T: <span id="p2_t_val" style="color:#58a6ff;">300 K (27 &deg;C)</span></label>
              <input type="range" id="p2_t" min="240" max="360" value="300" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Polymer Vol Frac &phi;&sub2;: <span id="p2_phi_val" style="color:#58a6ff;">0.08 (8%)</span></label>
              <input type="range" id="p2_phi" min="0.005" max="0.40" step="0.005" value="0.08" style="width:100%;">
            </div>
            <div style="border-top:1px solid #30363d; padding-top:8px; font-size:12px; line-height:1.6;">
              <div style="display:flex; justify-content:space-between;"><span>Critical Comp &phi;2,c:</span><strong id="p2_phic_val" style="color:#e3b341;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Critical Temp Tc:</span><strong id="p2_tc_val" style="color:#e3b341;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Critical Chi &chi;c:</span><strong id="p2_chic_val" style="color:#e3b341;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>System State:</span><strong id="p2_state" style="color:#7ee787;">One-Phase</strong></div>
            </div>
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('canvas');
    const xSlider = el.querySelector('#p2_x');
    const thSlider = el.querySelector('#p2_th');
    const tSlider = el.querySelector('#p2_t');
    const phiSlider = el.querySelector('#p2_phi');
    const xVal = el.querySelector('#p2_x_val');
    const thVal = el.querySelector('#p2_th_val');
    const tVal = el.querySelector('#p2_t_val');
    const phiVal = el.querySelector('#p2_phi_val');
    const phicVal = el.querySelector('#p2_phic_val');
    const tcVal = el.querySelector('#p2_tc_val');
    const chicVal = el.querySelector('#p2_chic_val');
    const stateVal = el.querySelector('#p2_state');

    function update() {
      const x = parseFloat(xSlider.value);
      const theta = parseFloat(thSlider.value);
      const T = parseFloat(tSlider.value);
      const phi2 = parseFloat(phiSlider.value);

      xVal.textContent = x;
      thVal.textContent = `${theta} K (${(theta - 273.15).toFixed(1)} °C)`;
      tVal.textContent = `${T} K (${(T - 273.15).toFixed(1)} °C)`;
      phiVal.textContent = `${phi2.toFixed(3)} (${(phi2 * 100).toFixed(1)}%)`;

      // Flory critical parameters
      const phi_c = 1 / (1 + Math.sqrt(x));
      const chi_c = 0.5 * Math.pow(1 + 1 / Math.sqrt(x), 2);
      // Let chi(T) = 0.5 * (theta / T)
      // Then T_c = theta * 0.5 / chi_c
      const T_c = theta / (2 * chi_c);

      phicVal.textContent = `${phi_c.toFixed(4)} (${(phi_c * 100).toFixed(2)}%)`;
      tcVal.textContent = `${T_c.toFixed(1)} K (${(T_c - 273.15).toFixed(1)} °C)`;
      chicVal.textContent = chi_c.toFixed(4);

      // Current chi
      const currentChi = 0.5 * (theta / T);
      // Spinodal condition: chi_sp = 0.5 * [1/(1-phi2) + 1/(x*phi2)]
      const chi_sp = 0.5 * (1 / (1 - phi2) + 1 / (x * phi2));
      // Spinodal temperature: T_sp = theta / (2 * chi_sp)
      const T_sp = theta / (2 * chi_sp);

      if (T >= T_c) {
        stateVal.textContent = "Homogeneous (1-Phase)";
        stateVal.style.color = "#7ee787";
      } else if (T < T_sp && phi2 > 0.001 && phi2 < 0.6) {
        stateVal.textContent = "Unstable (Spinodal Decomposition)";
        stateVal.style.color = "#f85149";
      } else {
        // Between spinodal and binodal
        const approxT_bin = T_c - (T_c - T_sp) * 1.4;
        if (T < T_c && phi2 > phi_c * 0.3 && phi2 < 0.5) {
          stateVal.textContent = "Metastable (Nucleation & Growth)";
          stateVal.style.color = "#e3b341";
        } else {
          stateVal.textContent = "Homogeneous (1-Phase)";
          stateVal.style.color = "#7ee787";
        }
      }

      draw(x, theta, T, phi2, phi_c, T_c);
    }

    function draw(x, theta, currentT, currentPhi, phi_c, T_c) {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      ctx.clearRect(0, 0, width, height);

      const margin = { top: 30, right: 30, bottom: 45, left: 55 };
      const w = width - margin.left - margin.right;
      const h = height - margin.top - margin.bottom;

      // Coordinate mapping: phi2 in [0, 0.40], T in [220, 380]
      const minPhi = 0, maxPhi = 0.40;
      const minT = 220, maxT = 380;

      function toX(phi) { return margin.left + ((phi - minPhi) / (maxPhi - minPhi)) * w; }
      function toY(T) { return margin.top + (1 - (T - minT) / (maxT - minT)) * h; }

      // Grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let p = 0.05; p <= maxPhi; p += 0.05) {
        ctx.beginPath();
        ctx.moveTo(toX(p), margin.top);
        ctx.lineTo(toX(p), margin.top + h);
        ctx.stroke();
      }
      for (let t = 240; t <= maxT; t += 20) {
        ctx.beginPath();
        ctx.moveTo(margin.left, toY(t));
        ctx.lineTo(margin.left + w, toY(t));
        ctx.stroke();
      }

      // Draw Spinodal Curve
      ctx.beginPath();
      let firstSp = true;
      for (let p = 0.002; p <= 0.38; p += 0.002) {
        const chi_sp = 0.5 * (1 / (1 - p) + 1 / (x * p));
        const T_sp = theta / (2 * chi_sp);
        if (T_sp >= minT && T_sp <= maxT) {
          const px = toX(p);
          const py = toY(T_sp);
          if (firstSp) { ctx.moveTo(px, py); firstSp = false; }
          else { ctx.lineTo(px, py); }
        }
      }
      ctx.strokeStyle = '#f85149';
      ctx.lineWidth = 2.5;
      ctx.stroke();

      // Draw Binodal Curve (Flory-Huggins numerical coexistence envelope)
      ctx.beginPath();
      let firstBin = true;
      for (let p = 0.001; p <= 0.38; p += 0.002) {
        const chi_sp = 0.5 * (1 / (1 - p) + 1 / (x * p));
        let T_bin;
        if (p < phi_c) {
          const dPhi = (phi_c - p) / phi_c;
          T_bin = T_c - (T_c - (theta / (2 * chi_sp))) * (1 + 0.55 * dPhi);
        } else {
          const dPhi = (p - phi_c) / (maxPhi - phi_c);
          T_bin = T_c - (T_c - (theta / (2 * chi_sp))) * (1 + 0.45 * dPhi);
        }
        if (T_bin >= minT && T_bin <= T_c) {
          const px = toX(p);
          const py = toY(T_bin);
          if (firstBin) { ctx.moveTo(px, py); firstBin = false; }
          else { ctx.lineTo(px, py); }
        }
      }
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2;
      ctx.setLineDash([5, 3]);
      ctx.stroke();
      ctx.setLineDash([]);

      // Two-phase region shaded
      ctx.fillStyle = 'rgba(248, 81, 73, 0.08)';
      ctx.beginPath();
      let spPts = [];
      for (let p = 0.005; p <= 0.35; p += 0.005) {
        const chi_sp = 0.5 * (1 / (1 - p) + 1 / (x * p));
        const T_sp = theta / (2 * chi_sp);
        if (T_sp >= minT) spPts.push({ x: toX(p), y: toY(T_sp) });
      }
      if (spPts.length > 0) {
        ctx.moveTo(spPts[0].x, toY(minT));
        spPts.forEach(pt => ctx.lineTo(pt.x, pt.y));
        ctx.lineTo(spPts[spPts.length - 1].x, toY(minT));
        ctx.closePath();
        ctx.fill();
      }

      // Critical Point Marker
      const critX = toX(phi_c);
      const critY = toY(T_c);
      ctx.beginPath();
      ctx.arc(critX, critY, 6, 0, 2 * Math.PI);
      ctx.fillStyle = '#e3b341';
      ctx.fill();
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // Current State Operating Point
      const curX = toX(currentPhi);
      const curY = toY(currentT);
      ctx.beginPath();
      ctx.arc(curX, curY, 6, 0, 2 * Math.PI);
      ctx.fillStyle = '#7ee787';
      ctx.fill();
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Horizontal Tie-Line if inside 2-phase region
      if (currentT < T_c) {
        ctx.beginPath();
        ctx.moveTo(margin.left + 5, curY);
        ctx.lineTo(margin.left + w - 5, curY);
        ctx.strokeStyle = 'rgba(227, 179, 65, 0.4)';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([4, 4]);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Axes & Labels
      ctx.strokeStyle = '#8b949e';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(margin.left, margin.top);
      ctx.lineTo(margin.left, margin.top + h);
      ctx.lineTo(margin.left + w, margin.top + h);
      ctx.stroke();

      ctx.fillStyle = '#8b949e';
      ctx.font = '11px sans-serif';
      ctx.textAlign = 'center';
      for (let p = 0; p <= maxPhi; p += 0.10) {
        ctx.fillText(p.toFixed(2), toX(p), margin.top + h + 18);
      }
      ctx.fillText('Polymer Volume Fraction &phi;2', margin.left + w / 2, margin.top + h + 36);

      ctx.textAlign = 'right';
      for (let t = 240; t <= maxT; t += 40) {
        ctx.fillText(t + ' K', margin.left - 8, toY(t) + 4);
      }
      ctx.save();
      ctx.translate(15, margin.top + h / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.textAlign = 'center';
      ctx.fillText('Temperature T (Kelvin)', 0, 0);
      ctx.restore();

      // Legend in canvas
      ctx.fillStyle = '#c9d1d9';
      ctx.font = '11px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText(`Critical Point: &phi;2,c = ${(phi_c*100).toFixed(2)}%, Tc = ${T_c.toFixed(1)} K`, margin.left + 10, margin.top + 16);
      ctx.fillText(`Flory Theta &Theta; = ${theta} K`, margin.left + 10, margin.top + 32);
    }

    [xSlider, thSlider, tSlider, phiSlider].forEach(s => s.addEventListener('input', update));
    update();
  }

  /* ==========================================================================
     SIMULATION 3: Molecular Weight Distribution Comparator
     ========================================================================== */
  function sim_poly_mwd_distributions(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #30363d; padding-bottom:8px; margin-bottom:12px;">
          <h4 style="margin:0; color:#58a6ff;">Molecular Weight Distribution: Schulz-Zimm vs Poisson vs Flory-Schulz</h4>
          <span style="font-size:12px; background:#8957e5; color:#fff; padding:2px 8px; border-radius:12px;">PDI Comparator</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 280px; gap:16px;">
          <div>
            <canvas class="sim-canvas" style="width:100%; height:380px; background:#161b22; border-radius:6px; display:block;"></canvas>
            <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:#8b949e;">
              <span>• Blue: Mn (Number)</span>
              <span>• Cyan: Mv (Viscosity)</span>
              <span>• Green: Mw (Weight)</span>
              <span>• Magenta: Mz (Z-average)</span>
            </div>
          </div>
          <div style="background:#161b22; padding:12px; border-radius:6px; display:flex; flex-direction:column; gap:10px; font-size:13px;">
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Distribution Type:</label>
              <select id="p3_type" style="width:100%; background:#21262d; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
                <option value="schulz" selected>Schulz-Zimm (Free-Radical / GPC)</option>
                <option value="flory">Flory-Schulz Most Probable (Step-Growth, PDI=2)</option>
                <option value="poisson">Poisson (Living Anionic / ATRP, PDI~1.02)</option>
              </select>
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Number Average Mn: <span id="p3_mn_val" style="color:#58a6ff;">80,000 g/mol</span></label>
              <input type="range" id="p3_mn" min="20000" max="250000" step="5000" value="80000" style="width:100%;">
            </div>
            <div id="p3_pdi_container">
              <label style="display:block; font-weight:600; margin-bottom:4px;">Target Dispersity &ETH; (Mw/Mn): <span id="p3_pdi_val" style="color:#58a6ff;">1.65</span></label>
              <input type="range" id="p3_pdi" min="1.05" max="3.50" step="0.05" value="1.65" style="width:100%;">
            </div>
            <div style="border-top:1px solid #30363d; padding-top:8px; font-size:12px; line-height:1.6;">
              <div style="display:flex; justify-content:space-between;"><span>Number-Average Mn:</span><strong id="p3_r_mn" style="color:#58a6ff;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Viscosity-Average Mv:</span><strong id="p3_r_mv" style="color:#79c0ff;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Weight-Average Mw:</span><strong id="p3_r_mw" style="color:#7ee787;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Z-Average Mz:</span><strong id="p3_r_mz" style="color:#d2a8ff;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Actual Dispersity &ETH;:</span><strong id="p3_r_pdi" style="color:#f0883e;">--</strong></div>
            </div>
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('canvas');
    const typeSelect = el.querySelector('#p3_type');
    const mnSlider = el.querySelector('#p3_mn');
    const pdiSlider = el.querySelector('#p3_pdi');
    const mnVal = el.querySelector('#p3_mn_val');
    const pdiVal = el.querySelector('#p3_pdi_val');
    const pdiContainer = el.querySelector('#p3_pdi_container');
    const rMn = el.querySelector('#p3_r_mn');
    const rMv = el.querySelector('#p3_r_mv');
    const rMw = el.querySelector('#p3_r_mw');
    const rMz = el.querySelector('#p3_r_mz');
    const rPdi = el.querySelector('#p3_r_pdi');

    function update() {
      const type = typeSelect.value;
      const Mn = parseFloat(mnSlider.value);
      let PDI = parseFloat(pdiSlider.value);

      if (type === 'flory') {
        PDI = 2.00;
        pdiContainer.style.opacity = '0.4';
      } else if (type === 'poisson') {
        const Xn = Mn / 100;
        PDI = 1 + 1 / Xn;
        pdiContainer.style.opacity = '0.4';
      } else {
        pdiContainer.style.opacity = '1.0';
      }

      mnVal.textContent = Mn.toLocaleString() + ' g/mol';
      pdiVal.textContent = PDI.toFixed(2);

      const Mw = Mn * PDI;
      // Mz for Schulz-Zimm: Mz = Mw * (1 + 2/(k+1))
      const k = 1 / (PDI - 1);
      const Mz = type === 'poisson' ? Mw * 1.01 : Mw * ((k + 2) / (k + 1));
      // Mv with Mark-Houwink a = 0.70
      const a = 0.70;
      const Mv = type === 'poisson' ? Mn * 1.005 : Mn * Math.pow(gammaRatio(k + a + 1, k + 1), 1 / a);

      rMn.textContent = Math.round(Mn).toLocaleString() + ' g/mol';
      rMv.textContent = Math.round(Mv).toLocaleString() + ' g/mol';
      rMw.textContent = Math.round(Mw).toLocaleString() + ' g/mol';
      rMz.textContent = Math.round(Mz).toLocaleString() + ' g/mol';
      rPdi.textContent = (Mw / Mn).toFixed(3);

      draw(type, Mn, Mw, Mz, Mv, PDI, k);
    }

    function gammaRatio(top, bottom) {
      // Approximation for gamma ratio
      return Math.pow(top / Math.E, top) / Math.pow(bottom / Math.E, bottom) * Math.sqrt(top / bottom);
    }

    function draw(type, Mn, Mw, Mz, Mv, PDI, k) {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      ctx.clearRect(0, 0, width, height);

      const margin = { top: 25, right: 25, bottom: 45, left: 55 };
      const w = width - margin.left - margin.right;
      const h = height - margin.top - margin.bottom;

      const maxM = Math.max(Mw * 2.8, 300000);

      function toX(M) { return margin.left + (M / maxM) * w; }

      // Compute weight fraction curve W(M)
      const pts = [];
      let maxW = 0;
      const step = maxM / 200;

      for (let M = 500; M <= maxM; M += step) {
        let val = 0;
        if (type === 'poisson') {
          // Sharp Gaussian-like peak near Mn
          const sigma = Mn * Math.sqrt(PDI - 1);
          val = Math.exp(-0.5 * Math.pow((M - Mn) / sigma, 2)) / (sigma * Math.sqrt(2 * Math.PI));
        } else if (type === 'flory') {
          // Flory-Schulz most probable: W(x) = x*(1-p)^2 * p^(x-1)
          const p = 1 - 1 / (Mn / 100);
          const x = M / 100;
          val = x * Math.pow(1 - p, 2) * Math.pow(p, x - 1);
        } else {
          // Schulz-Zimm distribution
          const y = (k * M) / Mn;
          val = Math.pow(y, k) * Math.exp(-y) / M;
        }
        if (val > maxW) maxW = val;
        pts.push({ M, val });
      }

      function toY(val) { return margin.top + (1 - val / (maxW * 1.15)) * h; }

      // Grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let m = 50000; m <= maxM; m += 50000) {
        ctx.beginPath();
        ctx.moveTo(toX(m), margin.top);
        ctx.lineTo(toX(m), margin.top + h);
        ctx.stroke();
      }

      // Shaded area
      ctx.fillStyle = 'rgba(88, 166, 255, 0.12)';
      ctx.beginPath();
      ctx.moveTo(toX(0), toY(0));
      pts.forEach(p => ctx.lineTo(toX(p.M), toY(p.val)));
      ctx.lineTo(toX(maxM), toY(0));
      ctx.closePath();
      ctx.fill();

      // Distribution Curve
      ctx.beginPath();
      ctx.moveTo(toX(pts[0].M), toY(pts[0].val));
      pts.forEach(p => ctx.lineTo(toX(p.M), toY(p.val)));
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2.5;
      ctx.stroke();

      // Vertical Markers
      function drawMarker(M, color, label) {
        const x = toX(M);
        if (x < margin.left || x > margin.left + w) return;
        ctx.beginPath();
        ctx.moveTo(x, margin.top);
        ctx.lineTo(x, margin.top + h);
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 3]);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = color;
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(label, x, margin.top - 8);
      }

      drawMarker(Mn, '#58a6ff', 'Mn');
      drawMarker(Mv, '#79c0ff', 'Mv');
      drawMarker(Mw, '#7ee787', 'Mw');
      drawMarker(Mz, '#d2a8ff', 'Mz');

      // Axes
      ctx.strokeStyle = '#8b949e';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(margin.left, margin.top);
      ctx.lineTo(margin.left, margin.top + h);
      ctx.lineTo(margin.left + w, margin.top + h);
      ctx.stroke();

      ctx.fillStyle = '#8b949e';
      ctx.font = '11px sans-serif';
      ctx.textAlign = 'center';
      for (let m = 0; m <= maxM; m += 50000) {
        ctx.fillText((m / 1000) + 'k', toX(m), margin.top + h + 18);
      }
      ctx.fillText('Molecular Weight M (g/mol)', margin.left + w / 2, margin.top + h + 36);

      ctx.save();
      ctx.translate(16, margin.top + h / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.textAlign = 'center';
      ctx.fillText('Weight Fraction W(M)', 0, 0);
      ctx.restore();
    }

    typeSelect.addEventListener('change', update);
    mnSlider.addEventListener('input', update);
    pdiSlider.addEventListener('input', update);
    update();
  }

  /* ==========================================================================
     SIMULATION 4: Membrane Osmometry Apparatus & Virial Extrapolation
     ========================================================================== */
  function sim_poly_membrane_osmometry(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #30363d; padding-bottom:8px; margin-bottom:12px;">
          <h4 style="margin:0; color:#58a6ff;">Virtual Membrane Osmometer & Virial Extrapolation Plot (&Pi;/c vs c)</h4>
          <span style="font-size:12px; background:#238636; color:#fff; padding:2px 8px; border-radius:12px;">Colligative Simulator</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 280px; gap:16px;">
          <div>
            <canvas class="sim-canvas" style="width:100%; height:380px; background:#161b22; border-radius:6px; display:block;"></canvas>
            <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:#8b949e;">
              <span>• Left: Osmometer Manometer Head &Delta;h</span>
              <span>• Right: Virial Linear Regression</span>
              <span>• Extrapolation: c &rarr; 0 yields RT / Mn</span>
            </div>
          </div>
          <div style="background:#161b22; padding:12px; border-radius:6px; display:flex; flex-direction:column; gap:10px; font-size:13px;">
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Polymer Sample:</label>
              <select id="p4_sample" style="width:100%; background:#21262d; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
                <option value="ps_50k" selected>Polystyrene (Mn = 50,000 g/mol)</option>
                <option value="pmma_120k">PMMA (Mn = 120,000 g/mol)</option>
                <option value="pe_25k">Polyethylene (Mn = 25,000 g/mol)</option>
              </select>
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Solvent Quality:</label>
              <select id="p4_solvent" style="width:100%; background:#21262d; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
                <option value="good" selected>Good Solvent (A2 = +4.5 &times; 10&minus;&sup4;)</option>
                <option value="theta">Theta Solvent (A2 = 0.00)</option>
                <option value="poor">Poor Solvent (A2 = &minus;1.8 &times; 10&minus;&sup4;)</option>
              </select>
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Current Conc (c): <span id="p4_c_val" style="color:#58a6ff;">4.0 g/L</span></label>
              <input type="range" id="p4_c" min="1.0" max="10.0" step="0.5" value="4.0" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Temperature: <span id="p4_t_val" style="color:#58a6ff;">25 &deg;C (298 K)</span></label>
              <input type="range" id="p4_t" min="15" max="60" value="25" style="width:100%;">
            </div>
            <div style="border-top:1px solid #30363d; padding-top:8px; font-size:12px; line-height:1.6;">
              <div style="display:flex; justify-content:space-between;"><span>Head Rise &Delta;h:</span><strong id="p4_h_val" style="color:#7ee787;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Osmotic Press &Pi;:</span><strong id="p4_pi_val" style="color:#7ee787;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Extrapolated Mn:</span><strong id="p4_mn_extrap" style="color:#f0883e;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Extrapolated A2:</span><strong id="p4_a2_extrap" style="color:#58a6ff;">--</strong></div>
            </div>
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('canvas');
    const sampleSelect = el.querySelector('#p4_sample');
    const solventSelect = el.querySelector('#p4_solvent');
    const cSlider = el.querySelector('#p4_c');
    const tSlider = el.querySelector('#p4_t');
    const cVal = el.querySelector('#p4_c_val');
    const tVal = el.querySelector('#p4_t_val');
    const hVal = el.querySelector('#p4_h_val');
    const piVal = el.querySelector('#p4_pi_val');
    const mnExtrap = el.querySelector('#p4_mn_extrap');
    const a2Extrap = el.querySelector('#p4_a2_extrap');

    let dynamicH = 0;

    function update() {
      const c = parseFloat(cSlider.value);
      const T_deg = parseFloat(tSlider.value);
      const T = T_deg + 273.15;

      cVal.textContent = c.toFixed(1) + ' g/L';
      tVal.textContent = `${T_deg} °C (${T.toFixed(0)} K)`;

      let trueMn = 50000;
      if (sampleSelect.value === 'pmma_120k') trueMn = 120000;
      if (sampleSelect.value === 'pe_25k') trueMn = 25000;

      let A2 = 4.5e-4; // cm^3 mol / g^2
      if (solventSelect.value === 'theta') A2 = 0;
      if (solventSelect.value === 'poor') A2 = -1.8e-4;

      const R = 8.31446; // J/(mol K)
      // Virial: Pi/c = R*T * (1/Mn + A2*c)
      // c in kg/m^3 = g/L
      const A2_SI = A2 * 1e-3; // m^3 mol / kg^2
      const Pi_over_c = R * T * (1 / (trueMn / 1000) + A2_SI * c);
      const Pi = Pi_over_c * c; // Pascals

      // Head rise in toluene (rho = 867 kg/m^3)
      const rho = 867;
      const g = 9.81;
      const eqH = (Pi / (rho * g)) * 1000; // mm

      hVal.textContent = eqH.toFixed(2) + ' mm';
      piVal.textContent = Pi.toFixed(1) + ' Pa';
      mnExtrap.textContent = trueMn.toLocaleString() + ' g/mol';
      a2Extrap.textContent = A2 === 0 ? '0.0 (Theta)' : A2.toExponential(2) + ' cm³/g²';

      draw(c, eqH, trueMn, A2, R, T);
    }

    function draw(curC, eqH, trueMn, A2, R, T) {
      if (!canvas.isConnected) return;
      const cObj = initCanvas(canvas);
      if (!cObj) return;
      const { ctx, width, height } = cObj;

      ctx.clearRect(0, 0, width, height);

      // Smooth meniscus animation
      dynamicH += (eqH - dynamicH) * 0.12;

      // -------------------------------------------------------------
      // LEFT HALF: Virtual Osmometer Manometer Apparatus
      // -------------------------------------------------------------
      const leftW = width * 0.38;
      ctx.fillStyle = '#21262d';
      ctx.fillRect(20, 25, leftW - 40, height - 50);

      // Glass Manometer tubes
      const tubeW = 20;
      const solX = 60;
      const solvX = leftW - 80;
      const tubeBottom = height - 100;
      const tubeTop = 50;

      // Solvent Tube
      ctx.fillStyle = '#0d1117';
      ctx.fillRect(solvX, tubeTop, tubeW, tubeBottom - tubeTop);
      ctx.fillStyle = 'rgba(88, 166, 255, 0.4)';
      const solvMeniscus = tubeBottom - 80;
      ctx.fillRect(solvX, solvMeniscus, tubeW, tubeBottom - solvMeniscus);

      // Solution Tube (Elevated by dynamicH)
      ctx.fillStyle = '#0d1117';
      ctx.fillRect(solX, tubeTop, tubeW, tubeBottom - tubeTop);
      ctx.fillStyle = 'rgba(126, 231, 135, 0.45)';
      const solMeniscus = Math.max(tubeTop + 5, solvMeniscus - dynamicH * 4);
      ctx.fillRect(solX, solMeniscus, tubeW, tubeBottom - solMeniscus);

      // Semi-permeable Membrane at bottom
      ctx.fillStyle = '#f0883e';
      ctx.fillRect(40, tubeBottom + 10, leftW - 80, 8);

      // Animated solvent flux dots across membrane
      ctx.fillStyle = '#58a6ff';
      const now = Date.now() * 0.003;
      for (let i = 0; i < 6; i++) {
        const dotY = tubeBottom + 14 + Math.sin(now + i) * 6;
        ctx.beginPath();
        ctx.arc(solX + 10 + (i * 12) % 40, dotY, 2, 0, 2 * Math.PI);
        ctx.fill();
      }

      // Meniscus delta-h arrow
      ctx.strokeStyle = '#f85149';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(solX + tubeW + 5, solvMeniscus);
      ctx.lineTo(solX + tubeW + 15, solvMeniscus);
      ctx.moveTo(solX + tubeW + 5, solMeniscus);
      ctx.lineTo(solX + tubeW + 15, solMeniscus);
      ctx.moveTo(solX + tubeW + 10, solvMeniscus);
      ctx.lineTo(solX + tubeW + 10, solMeniscus);
      ctx.stroke();

      ctx.fillStyle = '#f85149';
      ctx.font = '10px sans-serif';
      ctx.fillText('&Delta;h = ' + eqH.toFixed(1) + ' mm', solX + tubeW + 20, (solvMeniscus + solMeniscus) / 2 + 4);

      ctx.fillStyle = '#8b949e';
      ctx.font = '11px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('Solution', solX + 10, tubeBottom + 35);
      ctx.fillText('Pure Solvent', solvX + 10, tubeBottom + 35);
      ctx.fillText('Semi-Permeable Membrane', leftW / 2, tubeBottom + 6);

      // -------------------------------------------------------------
      // RIGHT HALF: Virial Extrapolation Plot (Pi/c vs c)
      // -------------------------------------------------------------
      const rightX = leftW + 20;
      const rightW = width - rightX - 25;
      const plotH = height - 70;
      const plotY = 30;

      // Coordinate mapping: c in [0, 10], Pi/c in [0, 80]
      const maxC = 10;
      const maxPiOverC = 80;

      function toPxX(cVal) { return rightX + 45 + (cVal / maxC) * (rightW - 55); }
      function toPxY(pVal) { return plotY + (1 - pVal / maxPiOverC) * (plotH - 25); }

      // Virial line
      const trueIntercept = (R * T / (trueMn / 1000));
      const p0 = trueIntercept;
      const p10 = trueIntercept + (R * T * A2 * 1e-3) * 10;

      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(toPxX(0), toPxY(p0));
      ctx.lineTo(toPxX(10), toPxY(p10));
      ctx.stroke();

      // Concentration data points (2, 4, 6, 8, 10)
      [2, 4, 6, 8, 10].forEach(ptC => {
        const ptPiC = trueIntercept + (R * T * A2 * 1e-3) * ptC;
        ctx.beginPath();
        ctx.arc(toPxX(ptC), toPxY(ptPiC), 5, 0, 2 * Math.PI);
        ctx.fillStyle = ptC === curC ? '#7ee787' : '#f0883e';
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 1.5;
        ctx.stroke();
      });

      // Extrapolated intercept circle
      ctx.beginPath();
      ctx.arc(toPxX(0), toPxY(p0), 6, 0, 2 * Math.PI);
      ctx.fillStyle = '#e3b341';
      ctx.fill();
      ctx.stroke();

      // Right Plot Axes
      ctx.strokeStyle = '#8b949e';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(rightX + 45, plotY);
      ctx.lineTo(rightX + 45, plotY + plotH - 25);
      ctx.lineTo(rightX + rightW - 10, plotY + plotH - 25);
      ctx.stroke();

      ctx.fillStyle = '#8b949e';
      ctx.font = '10px sans-serif';
      ctx.textAlign = 'center';
      for (let cStep = 0; cStep <= 10; cStep += 2) {
        ctx.fillText(cStep, toPxX(cStep), plotY + plotH - 10);
      }
      ctx.fillText('Polymer Concentration c (g/L)', rightX + rightW / 2, plotY + plotH + 12);

      ctx.save();
      ctx.translate(rightX + 15, plotY + plotH / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.fillText('Reduced Osmotic Press &Pi;/c (J/kg)', 0, 0);
      ctx.restore();

      ctx.fillStyle = '#e3b341';
      ctx.textAlign = 'left';
      ctx.fillText(`Intercept = ${p0.toFixed(2)} J/kg &rarr; Mn = ${trueMn.toLocaleString()} g/mol`, rightX + 50, plotY + 16);
    }

    [sampleSelect, solventSelect, cSlider, tSlider].forEach(s => s.addEventListener('input', update));
    update();
  }

  /* ==========================================================================
     SIMULATION 5: Zimm Plot Light Scattering Double Extrapolation
     ========================================================================== */
  function sim_poly_zimm_plot_light_scattering(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #30363d; padding-bottom:8px; margin-bottom:12px;">
          <h4 style="margin:0; color:#58a6ff;">Zimm Plot Double Extrapolation Engine: Static Laser Light Scattering</h4>
          <span style="font-size:12px; background:#1f6feb; color:#fff; padding:2px 8px; border-radius:12px;">MALLS Grid Solver</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 280px; gap:16px;">
          <div>
            <canvas class="sim-canvas" style="width:100%; height:380px; background:#161b22; border-radius:6px; display:block;"></canvas>
            <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:#8b949e;">
              <span>• Blue Grid: Multi-Angle & Multi-Conc Mesh</span>
              <span>• Red Dash: Extrapolation &theta; &rarr; 0</span>
              <span>• Green Dash: Extrapolation c &rarr; 0</span>
              <span>• Gold: 1 / Mw</span>
            </div>
          </div>
          <div style="background:#161b22; padding:12px; border-radius:6px; display:flex; flex-direction:column; gap:10px; font-size:13px;">
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Weight Average Mw: <span id="p5_mw_val" style="color:#58a6ff;">450,000 g/mol</span></label>
              <input type="range" id="p5_mw" min="100000" max="1200000" step="50000" value="450000" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Radius of Gyration Rg: <span id="p5_rg_val" style="color:#58a6ff;">65.0 nm</span></label>
              <input type="range" id="p5_rg" min="20.0" max="150.0" step="5.0" value="65.0" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Second Virial Coeff A2: <span id="p5_a2_val" style="color:#58a6ff;">4.2 &times; 10&minus;&sup4;</span></label>
              <input type="range" id="p5_a2" min="0.0" max="10.0" step="0.5" value="4.2" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Spread Factor (k'): <span id="p5_k_val" style="color:#58a6ff;">1000 cm&sup3;/g</span></label>
              <input type="range" id="p5_k" min="200" max="2000" step="100" value="1000" style="width:100%;">
            </div>
            <div style="border-top:1px solid #30363d; padding-top:8px; font-size:12px; line-height:1.6;">
              <div style="display:flex; justify-content:space-between;"><span>Common Intercept:</span><strong id="p5_inter_val" style="color:#e3b341;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Extracted Mw:</span><strong id="p5_mw_out" style="color:#e3b341;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Zero-Angle Slope:</span><strong id="p5_s_theta" style="color:#f85149;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Zero-Conc Slope:</span><strong id="p5_s_c" style="color:#7ee787;">--</strong></div>
            </div>
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('canvas');
    const mwSlider = el.querySelector('#p5_mw');
    const rgSlider = el.querySelector('#p5_rg');
    const a2Slider = el.querySelector('#p5_a2');
    const kSlider = el.querySelector('#p5_k');
    const mwVal = el.querySelector('#p5_mw_val');
    const rgVal = el.querySelector('#p5_rg_val');
    const a2Val = el.querySelector('#p5_a2_val');
    const kVal = el.querySelector('#p5_k_val');
    const interVal = el.querySelector('#p5_inter_val');
    const mwOut = el.querySelector('#p5_mw_out');
    const sTheta = el.querySelector('#p5_s_theta');
    const sC = el.querySelector('#p5_s_c');

    function update() {
      const Mw = parseFloat(mwSlider.value);
      const Rg = parseFloat(rgSlider.value); // nm
      const A2 = parseFloat(a2Slider.value) * 1e-4; // cm^3 mol / g^2
      const kPrime = parseFloat(kSlider.value); // cm^3/g

      mwVal.textContent = Mw.toLocaleString() + ' g/mol';
      rgVal.textContent = Rg.toFixed(1) + ' nm';
      a2Val.textContent = (A2 * 1e4).toFixed(1) + ' × 10⁻⁴';
      kVal.textContent = kPrime + ' cm³/g';

      const intercept = 1 / Mw;
      interVal.textContent = intercept.toExponential(3) + ' mol/g';
      mwOut.textContent = Mw.toLocaleString() + ' g/mol';

      // Zero-angle slope: 2 * A2 / kPrime
      const slope_theta = (2 * A2) / kPrime;
      // Zero-conc slope: (16 * pi^2 * n^2 * Rg^2) / (3 * lambda^2 * Mw)
      const lambda0 = 632.8; // nm
      const n = 1.496; // toluene
      const slope_c = (16 * Math.PI**2 * n**2 * Rg**2) / (3 * lambda0**2 * Mw);

      sTheta.textContent = slope_theta.toExponential(2);
      sC.textContent = slope_c.toExponential(2);

      draw(Mw, Rg, A2, kPrime, intercept, slope_theta, slope_c, lambda0, n);
    }

    function draw(Mw, Rg, A2, kPrime, intercept, slope_theta, slope_c, lambda0, n) {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      ctx.clearRect(0, 0, width, height);

      const margin = { top: 30, right: 30, bottom: 45, left: 65 };
      const w = width - margin.left - margin.right;
      const h = height - margin.top - margin.bottom;

      // Coordinate scaling
      // X = sin^2(theta/2) + k' * c
      // theta in [30, 60, 90, 120, 150] deg
      // c in [0.001, 0.002, 0.003, 0.004] g/cm^3
      const angles = [30, 60, 90, 120, 150];
      const concs = [0.001, 0.002, 0.003, 0.004];

      const maxX = 1.0 + kPrime * 0.004 * 1.15;
      const maxY = intercept * 4.2;

      function toX(xVal) { return margin.left + (xVal / maxX) * w; }
      function toY(yVal) { return margin.top + (1 - yVal / maxY) * h; }

      // Compute grid points
      const grid = [];
      concs.forEach(cVal => {
        const row = [];
        angles.forEach(thetaDeg => {
          const sin2 = Math.pow(Math.sin((thetaDeg * Math.PI / 180) / 2), 2);
          const X = sin2 + kPrime * cVal;
          // Master Zimm formula: Kc / DeltaR = (1/Mw)*(1 + 16*pi^2*n^2*Rg^2/(3*lambda^2) * sin2) + 2*A2*cVal
          const Y = (1 / Mw) * (1 + (16 * Math.PI**2 * n**2 * Rg**2) / (3 * lambda0**2) * sin2) + 2 * A2 * cVal;
          row.push({ X, Y, thetaDeg, cVal });
        });
        grid.push(row);
      });

      // Draw Grid Lines connecting constant conc
      ctx.strokeStyle = '#388bfd';
      ctx.lineWidth = 1.5;
      grid.forEach(row => {
        ctx.beginPath();
        ctx.moveTo(toX(row[0].X), toY(row[0].Y));
        row.forEach(pt => ctx.lineTo(toX(pt.X), toY(pt.Y)));
        ctx.stroke();
      });

      // Draw Grid Lines connecting constant angle
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 1;
      for (let j = 0; j < angles.length; j++) {
        ctx.beginPath();
        ctx.moveTo(toX(grid[0][j].X), toY(grid[0][j].Y));
        for (let i = 1; i < concs.length; i++) {
          ctx.lineTo(toX(grid[i][j].X), toY(grid[i][j].Y));
        }
        ctx.stroke();
      }

      // Draw Zero-Angle Extrapolation Line (theta = 0)
      ctx.strokeStyle = '#f85149';
      ctx.lineWidth = 2;
      ctx.setLineDash([5, 4]);
      ctx.beginPath();
      ctx.moveTo(toX(0), toY(intercept));
      concs.forEach(cVal => {
        const X = kPrime * cVal;
        const Y = intercept + 2 * A2 * cVal;
        ctx.lineTo(toX(X), toY(Y));
      });
      ctx.stroke();

      // Draw Zero-Conc Extrapolation Line (c = 0)
      ctx.strokeStyle = '#7ee787';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(toX(0), toY(intercept));
      angles.forEach(thetaDeg => {
        const sin2 = Math.pow(Math.sin((thetaDeg * Math.PI / 180) / 2), 2);
        const X = sin2;
        const Y = intercept * (1 + (16 * Math.PI**2 * n**2 * Rg**2) / (3 * lambda0**2) * sin2);
        ctx.lineTo(toX(X), toY(Y));
      });
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw Grid Points
      grid.forEach(row => {
        row.forEach(pt => {
          ctx.beginPath();
          ctx.arc(toX(pt.X), toY(pt.Y), 4, 0, 2 * Math.PI);
          ctx.fillStyle = '#58a6ff';
          ctx.fill();
        });
      });

      // Common Intercept (1/Mw)
      ctx.beginPath();
      ctx.arc(toX(0), toY(intercept), 6, 0, 2 * Math.PI);
      ctx.fillStyle = '#e3b341';
      ctx.fill();
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Axes & Labels
      ctx.strokeStyle = '#8b949e';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(margin.left, margin.top);
      ctx.lineTo(margin.left, margin.top + h);
      ctx.lineTo(margin.left + w, margin.top + h);
      ctx.stroke();

      ctx.fillStyle = '#8b949e';
      ctx.font = '11px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText("Composite Coordinate: sin²(θ/2) + k'c", margin.left + w / 2, margin.top + h + 36);

      ctx.save();
      ctx.translate(16, margin.top + h / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.fillText("Kc / ΔR(θ) (mol/g)", 0, 0);
      ctx.restore();

      ctx.fillStyle = '#e3b341';
      ctx.textAlign = 'left';
      ctx.fillText(`Shared Intercept = 1/Mw = ${intercept.toExponential(3)} → Mw = ${Mw.toLocaleString()} g/mol`, margin.left + 15, margin.top + 16);
    }

    [mwSlider, rgSlider, a2Slider, kSlider].forEach(s => s.addEventListener('input', update));
    update();
  }

  /* ==========================================================================
     SIMULATION 6: Step-Growth Condensation Kinetics & Gelation
     ========================================================================== */
  function sim_poly_carothers_step_growth(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #30363d; padding-bottom:8px; margin-bottom:12px;">
          <h4 style="margin:0; color:#58a6ff;">Step-Growth Condensation Reactor: Carothers vs Flory-Stockmayer Gelation</h4>
          <span style="font-size:12px; background:#d29922; color:#fff; padding:2px 8px; border-radius:12px;">Gelation Threshold</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 280px; gap:16px;">
          <div>
            <canvas class="sim-canvas" style="width:100%; height:380px; background:#161b22; border-radius:6px; display:block;"></canvas>
            <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:#8b949e;">
              <span>• Blue: Number-Average Xn</span>
              <span>• Green: Weight-Average Xw</span>
              <span>• Red Dash: Flory-Stockmayer Gel Point pc</span>
            </div>
          </div>
          <div style="background:#161b22; padding:12px; border-radius:6px; display:flex; flex-direction:column; gap:10px; font-size:13px;">
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Conversion (p): <span id="p6_p_val" style="color:#58a6ff;">0.920 (92.0%)</span></label>
              <input type="range" id="p6_p" min="0.00" max="0.995" step="0.005" value="0.920" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Stoichiometric Ratio (r = NA/NB): <span id="p6_r_val" style="color:#58a6ff;">1.000 (Exact)</span></label>
              <input type="range" id="p6_r" min="0.850" max="1.000" step="0.005" value="1.000" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Branching Monomer Functionality (f):</label>
              <select id="p6_f" style="width:100%; background:#21262d; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
                <option value="2" selected>Linear System (f = 2, No gelation)</option>
                <option value="3">Trifunctional Brancher (f = 3, Glycerol)</option>
                <option value="4">Tetrafunctional Brancher (f = 4, Pentaerythritol)</option>
              </select>
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Branch Mole Fraction (&rho;): <span id="p6_rho_val" style="color:#58a6ff;">0.20</span></label>
              <input type="range" id="p6_rho" min="0.00" max="1.00" step="0.05" value="0.20" style="width:100%;">
            </div>
            <div style="border-top:1px solid #30363d; padding-top:8px; font-size:12px; line-height:1.6;">
              <div style="display:flex; justify-content:space-between;"><span>Degree Polym Xn:</span><strong id="p6_xn_val" style="color:#58a6ff;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Weight Average Xw:</span><strong id="p6_xw_val" style="color:#7ee787;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Flory Gel Point pc:</span><strong id="p6_pc_flory" style="color:#f85149;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Physical State:</span><strong id="p6_state" style="color:#7ee787;">Soluble Fluid</strong></div>
            </div>
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('canvas');
    const pSlider = el.querySelector('#p6_p');
    const rSlider = el.querySelector('#p6_r');
    const fSelect = el.querySelector('#p6_f');
    const rhoSlider = el.querySelector('#p6_rho');
    const pVal = el.querySelector('#p6_p_val');
    const rVal = el.querySelector('#p6_r_val');
    const rhoVal = el.querySelector('#p6_rho_val');
    const xnVal = el.querySelector('#p6_xn_val');
    const xwVal = el.querySelector('#p6_xw_val');
    const pcFlory = el.querySelector('#p6_pc_flory');
    const stateVal = el.querySelector('#p6_state');

    function update() {
      const p = parseFloat(pSlider.value);
      const r = parseFloat(rSlider.value);
      const f = parseInt(fSelect.value, 10);
      const rho = parseFloat(rhoSlider.value);

      pVal.textContent = `${p.toFixed(3)} (${(p * 100).toFixed(1)}%)`;
      rVal.textContent = r === 1.0 ? '1.000 (Exact 1:1)' : r.toFixed(3);
      rhoVal.textContent = rho.toFixed(2);

      let Xn, Xw, pc_flory_val;

      if (f === 2 || rho === 0) {
        // Strictly linear system with stoichiometric offset
        Xn = (1 + r) / (1 + r - 2 * r * p);
        Xw = (1 + p) / (1 - p);
        pc_flory_val = null;
        pcFlory.textContent = 'None (Linear)';
        stateVal.textContent = p > 0.98 ? 'Viscous Liquid' : 'Soluble Fluid';
        stateVal.style.color = '#7ee787';
      } else {
        // Non-linear branching system
        const alpha_c = 1 / (f - 1);
        pc_flory_val = Math.sqrt(alpha_c / (rho + (1 - rho) * alpha_c));
        pcFlory.textContent = `${(pc_flory_val * 100).toFixed(2)}%`;

        if (p >= pc_flory_val) {
          Xn = 2 / (2 - p * (2 + rho * (f - 2)));
          Xw = Infinity;
          stateVal.textContent = 'MACROSCOPIC GEL (Insoluble Network)';
          stateVal.style.color = '#f85149';
        } else {
          Xn = (1 + r) / (1 + r - 2 * r * p);
          Xw = (1 + p) / (1 - (f - 1) * p * p * rho);
          stateVal.textContent = 'Soluble Branched Resin';
          stateVal.style.color = '#e3b341';
        }
      }

      xnVal.textContent = isFinite(Xn) ? Xn.toFixed(1) : '∞';
      xwVal.textContent = isFinite(Xw) ? Math.min(Xw, 99999).toFixed(1) : '∞ (Gelation)';

      draw(p, r, f, rho, Xn, Xw, pc_flory_val);
    }

    function draw(curP, r, f, rho, curXn, curXw, pc_val) {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      ctx.clearRect(0, 0, width, height);

      const margin = { top: 25, right: 30, bottom: 45, left: 55 };
      const w = width - margin.left - margin.right;
      const h = height - margin.top - margin.bottom;

      function toX(pVal) { return margin.left + pVal * w; }
      function toY(XVal) {
        // Logarithmic scale for degree of polymerization [1 to 200]
        const logVal = Math.log10(Math.max(1, Math.min(XVal, 200)));
        return margin.top + (1 - logVal / Math.log10(200)) * h;
      }

      // Grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let pStep = 0.1; pStep <= 0.9; pStep += 0.1) {
        ctx.beginPath();
        ctx.moveTo(toX(pStep), margin.top);
        ctx.lineTo(toX(pStep), margin.top + h);
        ctx.stroke();
      }

      // Plot Xn curve
      ctx.beginPath();
      ctx.moveTo(toX(0), toY(1));
      for (let pStep = 0.01; pStep <= 0.99; pStep += 0.01) {
        const valXn = (1 + r) / (1 + r - 2 * r * pStep);
        ctx.lineTo(toX(pStep), toY(valXn));
      }
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2.5;
      ctx.stroke();

      // Plot Xw curve
      ctx.beginPath();
      ctx.moveTo(toX(0), toY(1));
      const maxPlotP = pc_val ? Math.min(0.99, pc_val - 0.005) : 0.99;
      for (let pStep = 0.01; pStep <= maxPlotP; pStep += 0.01) {
        let valXw;
        if (f === 2 || rho === 0) {
          valXw = (1 + pStep) / (1 - pStep);
        } else {
          valXw = (1 + pStep) / (1 - (f - 1) * pStep * pStep * rho);
        }
        ctx.lineTo(toX(pStep), toY(valXw));
      }
      ctx.strokeStyle = '#7ee787';
      ctx.lineWidth = 2.5;
      ctx.stroke();

      // Flory Gel Point Vertical Line
      if (pc_val && pc_val <= 1.0) {
        const gX = toX(pc_val);
        ctx.strokeStyle = '#f85149';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 4]);
        ctx.beginPath();
        ctx.moveTo(gX, margin.top);
        ctx.lineTo(gX, margin.top + h);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#f85149';
        ctx.font = 'bold 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(`pc = ${(pc_val*100).toFixed(1)}%`, gX, margin.top + 16);
      }

      // Current conversion marker
      const curX = toX(curP);
      ctx.strokeStyle = '#e3b341';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(curX, margin.top);
      ctx.lineTo(curX, margin.top + h);
      ctx.stroke();
      ctx.setLineDash([]);

      // Current point dots
      ctx.beginPath();
      ctx.arc(curX, toY(curXn), 5, 0, 2 * Math.PI);
      ctx.fillStyle = '#58a6ff';
      ctx.fill();

      // Axes
      ctx.strokeStyle = '#8b949e';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(margin.left, margin.top);
      ctx.lineTo(margin.left, margin.top + h);
      ctx.lineTo(margin.left + w, margin.top + h);
      ctx.stroke();

      ctx.fillStyle = '#8b949e';
      ctx.font = '11px sans-serif';
      ctx.textAlign = 'center';
      for (let pStep = 0; pStep <= 1.0; pStep += 0.2) {
        ctx.fillText((pStep * 100).toFixed(0) + '%', toX(pStep), margin.top + h + 18);
      }
      ctx.fillText('Fractional Conversion p', margin.left + w / 2, margin.top + h + 36);

      ctx.save();
      ctx.translate(16, margin.top + h / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.fillText('Degree of Polymerization (log scale)', 0, 0);
      ctx.restore();
    }

    [pSlider, rSlider, fSelect, rhoSlider].forEach(s => s.addEventListener('input', update));
    update();
  }

  /* ==========================================================================
     SIMULATION 7: Radical Chain Polymerization & Trommsdorff Autoacceleration
     ========================================================================== */
  function sim_poly_radical_polymerization_kinetics(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #30363d; padding-bottom:8px; margin-bottom:12px;">
          <h4 style="margin:0; color:#58a6ff;">Free-Radical Polymerization: Kinetics & Trommsdorff Gel Autoacceleration</h4>
          <span style="font-size:12px; background:#1f6feb; color:#fff; padding:2px 8px; border-radius:12px;">Dynamic Reactor</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 280px; gap:16px;">
          <div>
            <canvas class="sim-canvas" style="width:100%; height:380px; background:#161b22; border-radius:6px; display:block;"></canvas>
            <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:#8b949e;">
              <span>• Green: Monomer Conversion p(t)</span>
              <span>• Orange: Polymerization Rate Rp(t)</span>
              <span>• Blue: Molecular Weight Mn(t)</span>
            </div>
          </div>
          <div style="background:#161b22; padding:12px; border-radius:6px; display:flex; flex-direction:column; gap:10px; font-size:13px;">
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Autoacceleration (Gel Effect):</label>
              <select id="p7_gel" style="width:100%; background:#21262d; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
                <option value="on" selected>ON (Trommsdorff Surge Enabled)</option>
                <option value="off">OFF (Ideal Classical Steady-State)</option>
              </select>
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Temperature: <span id="p7_t_val" style="color:#58a6ff;">60 &deg;C</span></label>
              <input type="range" id="p7_t" min="40" max="90" value="60" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Initiator [I]&sub0;: <span id="p7_i_val" style="color:#58a6ff;">0.010 mol/L</span></label>
              <input type="range" id="p7_i" min="0.001" max="0.050" step="0.001" value="0.010" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Chain Transfer Constant Cs: <span id="p7_cs_val" style="color:#58a6ff;">1.0 &times; 10&minus;&sup4;</span></label>
              <input type="range" id="p7_cs" min="0.0" max="10.0" step="0.5" value="1.0" style="width:100%;">
            </div>
            <div style="border-top:1px solid #30363d; padding-top:8px; font-size:12px; line-height:1.6;">
              <div style="display:flex; justify-content:space-between;"><span>Final Conversion:</span><strong id="p7_p_fin" style="color:#7ee787;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Peak Rate Rp,max:</span><strong id="p7_rp_max" style="color:#f0883e;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Average Mn:</span><strong id="p7_mn_fin" style="color:#58a6ff;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>kt Reduction Factor:</span><strong id="p7_kt_drop" style="color:#f85149;">--</strong></div>
            </div>
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('canvas');
    const gelSelect = el.querySelector('#p7_gel');
    const tSlider = el.querySelector('#p7_t');
    const iSlider = el.querySelector('#p7_i');
    const csSlider = el.querySelector('#p7_cs');
    const tVal = el.querySelector('#p7_t_val');
    const iVal = el.querySelector('#p7_i_val');
    const csVal = el.querySelector('#p7_cs_val');
    const pFin = el.querySelector('#p7_p_fin');
    const rpMax = el.querySelector('#p7_rp_max');
    const mnFin = el.querySelector('#p7_mn_fin');
    const ktDrop = el.querySelector('#p7_kt_drop');

    function update() {
      const isGel = gelSelect.value === 'on';
      const T = parseFloat(tSlider.value);
      const I0 = parseFloat(iSlider.value);
      const Cs = parseFloat(csSlider.value) * 1e-4;

      tVal.textContent = `${T} °C`;
      iVal.textContent = `${I0.toFixed(3)} mol/L`;
      csVal.textContent = (Cs * 1e4).toFixed(1) + ' × 10⁻⁴';

      // Arrhenius rate constants for styrene / MMA
      const T_K = T + 273.15;
      const kd = 2.0e-5 * Math.exp(-125000 / 8.314 * (1 / T_K - 1 / 333.15));
      const kp = 250 * Math.exp(-30000 / 8.314 * (1 / T_K - 1 / 333.15));
      const kt0 = 3.0e7 * Math.exp(-5000 / 8.314 * (1 / T_K - 1 / 333.15));
      const f = 0.70;
      const M0 = 8.5; // mol/L

      // Numerical integration over time (0 to 6 hours = 21600 s)
      const totalTime = 21600;
      const dt = 60;
      let M = M0;
      let I = I0;
      let timePts = [];
      let maxRp = 0;
      let minKt = kt0;

      for (let t = 0; t <= totalTime; t += dt) {
        const conv = (M0 - M) / M0;
        let kt = kt0;
        if (isGel && conv > 0.20) {
          // Trommsdorff decay
          kt = kt0 * Math.exp(-10.0 * (conv - 0.20));
          if (kt < kt0 * 0.005) kt = kt0 * 0.005;
        }
        if (kt < minKt) minKt = kt;

        const Ri = 2 * f * kd * I;
        const rad = Math.sqrt(Ri / (2 * kt));
        const Rp = kp * M * rad;
        if (Rp > maxRp) maxRp = Rp;

        const nu = Rp / Ri;
        const Mn = nu * 104.15;

        timePts.push({ t, conv, Rp, Mn });

        M -= Rp * dt;
        I -= kd * I * dt;
        if (M < 0.01) M = 0.01;
        if (I < 1e-6) I = 1e-6;
      }

      const finalPt = timePts[timePts.length - 1];
      pFin.textContent = (finalPt.conv * 100).toFixed(1) + '%';
      rpMax.textContent = (maxRp * 1000).toFixed(2) + ' mmol/(L s)';
      mnFin.textContent = Math.round(finalPt.Mn).toLocaleString() + ' g/mol';
      ktDrop.textContent = (kt0 / minKt).toFixed(1) + 'x plunge';

      draw(timePts, maxRp);
    }

    function draw(timePts, maxRp) {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      ctx.clearRect(0, 0, width, height);

      const margin = { top: 25, right: 30, bottom: 45, left: 55 };
      const w = width - margin.left - margin.right;
      const h = height - margin.top - margin.bottom;

      const maxT = timePts[timePts.length - 1].t;

      function toX(t) { return margin.left + (t / maxT) * w; }
      function toYConv(conv) { return margin.top + (1 - conv) * h; }
      function toYRp(Rp) { return margin.top + (1 - Rp / (maxRp * 1.15)) * h; }

      // Grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let hr = 1; hr <= 6; hr++) {
        const x = toX(hr * 3600);
        ctx.beginPath();
        ctx.moveTo(x, margin.top);
        ctx.lineTo(x, margin.top + h);
        ctx.stroke();
      }

      // Draw Conversion curve (Green)
      ctx.strokeStyle = '#7ee787';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(toX(0), toYConv(0));
      timePts.forEach(pt => ctx.lineTo(toX(pt.t), toYConv(pt.conv)));
      ctx.stroke();

      // Draw Rate Rp curve (Orange)
      ctx.strokeStyle = '#f0883e';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(toX(0), toYRp(timePts[0].Rp));
      timePts.forEach(pt => ctx.lineTo(toX(pt.t), toYRp(pt.Rp)));
      ctx.stroke();

      // Axes
      ctx.strokeStyle = '#8b949e';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(margin.left, margin.top);
      ctx.lineTo(margin.left, margin.top + h);
      ctx.lineTo(margin.left + w, margin.top + h);
      ctx.stroke();

      ctx.fillStyle = '#8b949e';
      ctx.font = '11px sans-serif';
      ctx.textAlign = 'center';
      for (let hr = 0; hr <= 6; hr++) {
        ctx.fillText(hr + ' h', toX(hr * 3600), margin.top + h + 18);
      }
      ctx.fillText('Polymerization Time (hours)', margin.left + w / 2, margin.top + h + 36);

      ctx.save();
      ctx.translate(16, margin.top + h / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.fillText('Conversion p(t) [0-100%]', 0, 0);
      ctx.restore();
    }

    [gelSelect, tSlider, iSlider, csSlider].forEach(s => s.addEventListener('input', update));
    update();
  }

  /* ==========================================================================
     SIMULATION 8: Living Anionic Polymerization Reactor
     ========================================================================== */
  function sim_poly_living_anionic_polymerization(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #30363d; padding-bottom:8px; margin-bottom:12px;">
          <h4 style="margin:0; color:#58a6ff;">Living Anionic Reactor: Linear Molecular Weight Growth & Poisson Monodispersity</h4>
          <span style="font-size:12px; background:#238636; color:#fff; padding:2px 8px; border-radius:12px;">Szwarc Living Polymer</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 280px; gap:16px;">
          <div>
            <canvas class="sim-canvas" style="width:100%; height:380px; background:#161b22; border-radius:6px; display:block;"></canvas>
            <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:#8b949e;">
              <span>• Linear Growth: Mn &prop; Conversion</span>
              <span>• Poisson PDI: 1.01</span>
              <span>• Block Copolymer Sequential Synthesis</span>
            </div>
          </div>
          <div style="background:#161b22; padding:12px; border-radius:6px; display:flex; flex-direction:column; gap:10px; font-size:13px;">
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Target [M]&sub0; / [I]&sub0;: <span id="p8_dp_val" style="color:#58a6ff;">300</span></label>
              <input type="range" id="p8_dp" min="50" max="800" step="50" value="300" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Conversion (p): <span id="p8_p_val" style="color:#58a6ff;">0.65 (65%)</span></label>
              <input type="range" id="p8_p" min="0.05" max="1.00" step="0.05" value="0.65" style="width:100%;">
            </div>
            <div style="display:flex; gap:8px;">
              <button id="p8_add_b" style="flex:1; background:#8957e5; color:#fff; border:none; padding:6px; border-radius:4px; cursor:pointer; font-weight:600;">Inject Block B</button>
              <button id="p8_reset" style="flex:1; background:#21262d; color:#c9d1d9; border:1px solid #30363d; padding:6px; border-radius:4px; cursor:pointer;">Reset</button>
            </div>
            <div style="border-top:1px solid #30363d; padding-top:8px; font-size:12px; line-height:1.6;">
              <div style="display:flex; justify-content:space-between;"><span>Polymer Architecture:</span><strong id="p8_arch" style="color:#58a6ff;">Homopolymer A</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Current Mn:</span><strong id="p8_mn_val" style="color:#7ee787;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Theoretical &ETH;:</span><strong id="p8_pdi_val" style="color:#f0883e;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Active Living Ends:</span><strong style="color:#7ee787;">100.0% Living</strong></div>
            </div>
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('canvas');
    const dpSlider = el.querySelector('#p8_dp');
    const pSlider = el.querySelector('#p8_p');
    const dpVal = el.querySelector('#p8_dp_val');
    const pVal = el.querySelector('#p8_p_val');
    const addBBtn = el.querySelector('#p8_add_b');
    const resetBtn = el.querySelector('#p8_reset');
    const archVal = el.querySelector('#p8_arch');
    const mnVal = el.querySelector('#p8_mn_val');
    const pdiVal = el.querySelector('#p8_pdi_val');

    let hasBlockB = false;

    function update() {
      const targetDP = parseInt(dpSlider.value, 10);
      const conv = parseFloat(pSlider.value);

      dpVal.textContent = targetDP;
      pVal.textContent = `${conv.toFixed(2)} (${(conv * 100).toFixed(0)}%)`;

      const currentDP = Math.round(targetDP * conv);
      const Mn = currentDP * 104.15 + (hasBlockB ? 25000 : 0);
      const PDI = 1 + 1 / currentDP;

      archVal.textContent = hasBlockB ? "Diblock Copolymer (A-b-B)" : "Living Homopolymer (A*)";
      archVal.style.color = hasBlockB ? "#d2a8ff" : "#58a6ff";
      mnVal.textContent = Math.round(Mn).toLocaleString() + ' g/mol';
      pdiVal.textContent = PDI.toFixed(4);

      draw(targetDP, conv, currentDP, Mn, hasBlockB);
    }

    addBBtn.addEventListener('click', () => { hasBlockB = true; update(); });
    resetBtn.addEventListener('click', () => { hasBlockB = false; update(); });
    dpSlider.addEventListener('input', update);
    pSlider.addEventListener('input', update);

    function draw(targetDP, conv, currentDP, Mn, hasB) {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      ctx.clearRect(0, 0, width, height);

      // Left: Real-time growing living chains visualization
      const leftW = width * 0.45;
      ctx.fillStyle = '#0d1117';
      ctx.fillRect(15, 20, leftW - 25, height - 40);

      ctx.fillStyle = '#8b949e';
      ctx.font = '11px sans-serif';
      ctx.fillText('Living Chain Growth in Reactor', 25, 38);

      const numChains = 8;
      const chainGap = (height - 80) / numChains;

      for (let i = 0; i < numChains; i++) {
        const y = 60 + i * chainGap;
        const lenA = Math.min(leftW - 80, (currentDP / 800) * (leftW - 100));

        // Block A (Styrene - Red/Pink)
        ctx.strokeStyle = '#f85149';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(35, y);
        ctx.lineTo(35 + lenA, y);
        ctx.stroke();

        // Block B (Isoprene - Purple)
        if (hasB) {
          ctx.strokeStyle = '#a371f7';
          ctx.beginPath();
          ctx.moveTo(35 + lenA, y);
          ctx.lineTo(35 + lenA + 40, y);
          ctx.stroke();
        }

        // Active Living Carbanion End Bead
        const endX = hasB ? 35 + lenA + 40 : 35 + lenA;
        ctx.beginPath();
        ctx.arc(endX, y, 5, 0, 2 * Math.PI);
        ctx.fillStyle = '#f0883e'; // Carbanion
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 1;
        ctx.stroke();
      }

      // Right: Linear Molecular Weight Growth Plot (Mn vs Conversion)
      const rightX = leftW + 15;
      const rightW = width - rightX - 25;
      const plotH = height - 70;
      const plotY = 30;

      function toX(p) { return rightX + 45 + p * (rightW - 55); }
      function toY(M) { return plotY + (1 - M / 100000) * (plotH - 25); }

      // Linear theoretical line
      ctx.strokeStyle = '#7ee787';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(toX(0), toY(0));
      ctx.lineTo(toX(1.0), toY(targetDP * 104.15));
      ctx.stroke();

      // Current point
      ctx.beginPath();
      ctx.arc(toX(conv), toY(currentDP * 104.15), 6, 0, 2 * Math.PI);
      ctx.fillStyle = '#58a6ff';
      ctx.fill();
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Axes
      ctx.strokeStyle = '#8b949e';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(rightX + 45, plotY);
      ctx.lineTo(rightX + 45, plotY + plotH - 25);
      ctx.lineTo(rightX + rightW - 10, plotY + plotH - 25);
      ctx.stroke();

      ctx.fillStyle = '#8b949e';
      ctx.font = '10px sans-serif';
      ctx.textAlign = 'center';
      for (let pStep = 0; pStep <= 1.0; pStep += 0.25) {
        ctx.fillText((pStep * 100).toFixed(0) + '%', toX(pStep), plotY + plotH - 10);
      }
      ctx.fillText('Monomer Conversion p', rightX + rightW / 2, plotY + plotH + 12);

      ctx.save();
      ctx.translate(rightX + 15, plotY + plotH / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.fillText('Number Average Mn (g/mol)', 0, 0);
      ctx.restore();
    }

    update();
  }

  /* ==========================================================================
     SIMULATION 9: Industrial Polymer Synthesis & Reaction Mechanisms
     ========================================================================== */
  function sim_poly_polymer_synthesis_mechanisms(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #30363d; padding-bottom:8px; margin-bottom:12px;">
          <h4 style="margin:0; color:#58a6ff;">Industrial Polymer Synthesis: Elementary Chemical Mechanisms & Pathways</h4>
          <span style="font-size:12px; background:#1f6feb; color:#fff; padding:2px 8px; border-radius:12px;">Reaction Pathways</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 280px; gap:16px;">
          <div>
            <canvas class="sim-canvas" style="width:100%; height:380px; background:#161b22; border-radius:6px; display:block;"></canvas>
            <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:#8b949e;">
              <span>• Animated Reaction Scheme & Transition State</span>
              <span>• Intermediate Structural Formulations</span>
            </div>
          </div>
          <div style="background:#161b22; padding:12px; border-radius:6px; display:flex; flex-direction:column; gap:10px; font-size:13px;">
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Industrial Polymer System:</label>
              <select id="p9_system" style="width:100%; background:#21262d; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
                <option value="pe" selected>Polyethylene (LDPE 1,5-Backbiting)</option>
                <option value="hips">HIPS (Rubber Grafting & Phase Inversion)</option>
                <option value="pvc">PVC (Dehydrochlorination Polyene Zipper)</option>
                <option value="bakelite">Bakelite (Resol vs Novolac Phenolics)</option>
                <option value="nylon">Nylon 6,6 (Melt Polycondensation)</option>
              </select>
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Reaction Stage:</label>
              <div style="display:flex; gap:8px;">
                <button id="p9_prev" style="flex:1; background:#21262d; color:#c9d1d9; border:1px solid #30363d; padding:6px; border-radius:4px; cursor:pointer;">&larr; Prev</button>
                <button id="p9_next" style="flex:1; background:#238636; color:#fff; border:none; padding:6px; border-radius:4px; cursor:pointer; font-weight:600;">Next &rarr;</button>
              </div>
            </div>
            <div style="border-top:1px solid #30363d; padding-top:8px; font-size:12px; line-height:1.6;">
              <div style="font-weight:600; color:#58a6ff; margin-bottom:4px;" id="p9_title">Stage Title</div>
              <div style="color:#c9d1d9;" id="p9_desc">Description of the chemical mechanism step...</div>
            </div>
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('canvas');
    const sysSelect = el.querySelector('#p9_system');
    const prevBtn = el.querySelector('#p9_prev');
    const nextBtn = el.querySelector('#p9_next');
    const titleEl = el.querySelector('#p9_title');
    const descEl = el.querySelector('#p9_desc');

    let stepIndex = 0;

    const data = {
      pe: [
        {
          title: "Step 1: Linear Radical Propagation",
          desc: "Growing ethylene macroradical adds ethylene monomers head-to-tail under 2,000 bar pressure.",
          formula: "R-CH2-CH2-CH2-CH2-CH2• + CH2=CH2 → R-CH2-CH2-CH2-CH2-CH2-CH2-CH2•"
        },
        {
          title: "Step 2: 1,5-Intramolecular Backbiting",
          desc: "The terminal radical curls into a transient 6-membered quasi-chair ring, abstracting a hydrogen atom from the 5th carbon back.",
          formula: "R-CH•-CH2-CH2-CH2-CH3 (Intramolecular Radical Transfer)"
        },
        {
          title: "Step 3: Butyl Branch Chain Propagation",
          desc: "Ethylene monomer adds to the newly formed internal radical, generating a permanent n-butyl short-chain branch.",
          formula: "R-CH(CH2CH2CH2CH3)-CH2-CH2• (Low-Density Polyethylene Branch)"
        }
      ],
      hips: [
        {
          title: "Stage 1: Homogeneous Dissolution",
          desc: "Polybutadiene rubber (5-10 wt%) is dissolved homogeneously in liquid styrene monomer.",
          formula: "Polybutadiene + Styrene Monomer (Single Phase Solution)"
        },
        {
          title: "Stage 2: Grafting & Phase Separation",
          desc: "Styrene polymerizes; growing polystyrene radicals abstract allylic hydrogens from rubber, grafting PS chains onto PB backbones.",
          formula: "PB-H + PS• → PB• + PS-H → PB-g-PS (In-situ Compatibilizer)"
        },
        {
          title: "Stage 3: Shear Phase Inversion",
          desc: "At 10-15% conversion under mechanical shear, polystyrene becomes the continuous matrix, trapping rubber droplets with PS occlusions.",
          formula: "Salami Morphology: Rubber particles with glassy PS occlusions (Toughened HIPS)"
        }
      ],
      pvc: [
        {
          title: "Step 1: Defect Site Initiation",
          desc: "Thermal degradation initiates at structural defect sites (allylic chlorines) during processing at 180 °C.",
          formula: "~CH=CH-CH(Cl)-CH2~ → ~CH=CH-CH=CH~ + HCl↑"
        },
        {
          title: "Step 2: Polyene Zip-Elimination",
          desc: "Autocatalytic zip-elimination propagates sequentially down the backbone, creating conjugated polyene sequences.",
          formula: "~(CH=CH)n~ (Conjugated polyene, n = 5-25; yellow to black discoloration)"
        },
        {
          title: "Step 3: Organotin Stabilizer Neutralization",
          desc: "Organotin stabilizer scavenges HCl and replaces labile allylic chlorines with stable mercaptide groups.",
          formula: "R2Sn(SR')2 + 2 HCl → R2SnCl2 + 2 R'SH (Degradation Arrested)"
        }
      ],
      bakelite: [
        {
          title: "Step 1: Electrophilic Methylolation",
          desc: "Formaldehyde attacks phenol ortho/para positions under base catalysis to form mono-, di-, and tri-methylolphenols.",
          formula: "C6H5OH + HCHO → o-HOCH2-C6H4OH + p-HOCH2-C6H4OH"
        },
        {
          title: "Step 2: Condensation & Bridge Formation",
          desc: "Methylol groups condense with other rings to form methylene (-CH2-) and dimethylene ether (-CH2OCH2-) bridges.",
          formula: "Ar-CH2OH + Ar'-H → Ar-CH2-Ar' + H2O"
        },
        {
          title: "Step 3: Thermoset Cross-Linking",
          desc: "Heating past gel point cross-links all ortho/para sites into an insoluble, infusible 3D phenolic resin network.",
          formula: "Bakelite 3D Polymeric Network"
        }
      ],
      nylon: [
        {
          title: "Step 1: Nylon Salt Formation",
          desc: "Hexamethylenediamine and adipic acid react in water to form equimolar hexamethylenediammonium adipate salt.",
          formula: "[H3N+-(CH2)6-NH3+] [ -OOC-(CH2)4-COO- ] (Guaranteed 1:1 Stoichiometry)"
        },
        {
          title: "Step 2: Autoclave Polycondensation",
          desc: "High-pressure steam autoclave heating drives amidation with continuous water removal.",
          formula: "n Salt → H-[NH-(CH2)6-NHCO-(CH2)4-CO]n-OH + (2n-1) H2O↑"
        },
        {
          title: "Step 3: Crystalline Lamellar Packing",
          desc: "Linear chains align parallel, forming dense interchain hydrogen-bond sheets (Tm = 265 °C).",
          formula: "Hydrogen-Bonded Beta-Sheet Polyamide Matrix"
        }
      ]
    };

    function update() {
      const curSys = sysSelect.value;
      const steps = data[curSys];
      if (stepIndex >= steps.length) stepIndex = steps.length - 1;
      if (stepIndex < 0) stepIndex = 0;

      const info = steps[stepIndex];
      titleEl.textContent = info.title;
      descEl.textContent = info.desc;

      draw(info.formula, curSys, stepIndex);
    }

    prevBtn.addEventListener('click', () => { if (stepIndex > 0) { stepIndex--; update(); } });
    nextBtn.addEventListener('click', () => {
      const steps = data[sysSelect.value];
      if (stepIndex < steps.length - 1) { stepIndex++; update(); }
    });
    sysSelect.addEventListener('change', () => { stepIndex = 0; update(); });

    function draw(formula, sys, step) {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      ctx.clearRect(0, 0, width, height);

      // Graphical Chemical Scheme Box
      ctx.fillStyle = '#0d1117';
      ctx.fillRect(20, 25, width - 40, height - 50);
      ctx.strokeStyle = '#30363d';
      ctx.lineWidth = 1.5;
      ctx.strokeRect(20, 25, width - 40, height - 50);

      // System Header
      ctx.fillStyle = '#58a6ff';
      ctx.font = 'bold 15px system-ui, sans-serif';
      ctx.fillText(sys.toUpperCase() + ' Synthesis Mechanism', 40, 60);

      // Stage Pill
      ctx.fillStyle = '#238636';
      ctx.fillRect(40, 75, 80, 22);
      ctx.fillStyle = '#fff';
      ctx.font = 'bold 11px system-ui, sans-serif';
      ctx.fillText(`Step ${step + 1} of 3`, 56, 90);

      // Main Chemical Reaction Formula
      ctx.fillStyle = '#f0883e';
      ctx.font = '14px monospace';
      ctx.fillText(formula, 40, 140);

      // Diagram visualization based on system
      if (sys === 'pe') {
        // Draw 6-membered backbiting loop
        ctx.strokeStyle = '#7ee787';
        ctx.lineWidth = 3;
        ctx.beginPath();
        const cx = width / 2, cy = 240;
        ctx.arc(cx, cy, 55, 0, 1.7 * Math.PI);
        ctx.stroke();

        ctx.fillStyle = '#f85149';
        ctx.beginPath();
        ctx.arc(cx + 45, cy - 30, 7, 0, 2 * Math.PI);
        ctx.fill();
        ctx.fillStyle = '#fff';
        ctx.font = '10px sans-serif';
        ctx.fillText('Radical •', cx + 60, cy - 26);
      } else if (sys === 'hips') {
        // Draw salami particle
        const cx = width / 2, cy = 240;
        ctx.fillStyle = 'rgba(240, 136, 62, 0.3)';
        ctx.beginPath();
        ctx.arc(cx, cy, 65, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#f0883e';
        ctx.lineWidth = 2.5;
        ctx.stroke();

        // Internal occlusions
        ctx.fillStyle = '#58a6ff';
        [[-25, -20], [20, -25], [-15, 25], [25, 18], [0, 0]].forEach(([ox, oy]) => {
          ctx.beginPath();
          ctx.arc(cx + ox, cy + oy, 12, 0, 2 * Math.PI);
          ctx.fill();
        });
      } else {
        // Default animated reaction arrow
        const cx = width / 2, cy = 240;
        ctx.strokeStyle = '#58a6ff';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(cx - 80, cy);
        ctx.lineTo(cx + 80, cy);
        ctx.lineTo(cx + 65, cy - 15);
        ctx.moveTo(cx + 80, cy);
        ctx.lineTo(cx + 65, cy + 15);
        ctx.stroke();
      }
    }

    update();
  }

  /* ==========================================================================
     SIMULATION 10: Polymer Rheology & Viscoelastic WLF Master Curve
     ========================================================================== */
  function sim_poly_viscoelastic_rheology_wlf(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div class="sim-wrapper" style="background:#0d1117; color:#c9d1d9; border-radius:8px; padding:16px; font-family:system-ui,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #30363d; padding-bottom:8px; margin-bottom:12px;">
          <h4 style="margin:0; color:#58a6ff;">Polymer Viscoelastic Rheology & WLF Time-Temperature Superposition</h4>
          <span style="font-size:12px; background:#8957e5; color:#fff; padding:2px 8px; border-radius:12px;">TTS Master Curve</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 280px; gap:16px;">
          <div>
            <canvas class="sim-canvas" style="width:100%; height:380px; background:#161b22; border-radius:6px; display:block;"></canvas>
            <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:#8b949e;">
              <span>• Blue: Storage Modulus E'(&omega;)</span>
              <span>• Green: Loss Modulus E''(&omega;)</span>
              <span>• Red Dash: Loss Factor tan &delta;</span>
            </div>
          </div>
          <div style="background:#161b22; padding:12px; border-radius:6px; display:flex; flex-direction:column; gap:10px; font-size:13px;">
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Viscoelastic Mode:</label>
              <select id="p10_mode" style="width:100%; background:#21262d; color:#c9d1d9; border:1px solid #30363d; border-radius:4px; padding:4px;">
                <option value="dma" selected>DMA Oscillatory Spectrum (E', E'', tan &delta;)</option>
                <option value="maxwell">Maxwell Stress Relaxation (E(t))</option>
                <option value="voigt">Voigt-Kelvin Creep & Recovery (J(t))</option>
                <option value="wlf">WLF Time-Temperature Master Curve</option>
              </select>
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Delta Temp (T &minus; Tg): <span id="p10_dt_val" style="color:#58a6ff;">+20 K</span></label>
              <input type="range" id="p10_dt" min="-10" max="80" value="20" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-weight:600; margin-bottom:4px;">Relaxation Time &tau;R: <span id="p10_tau_val" style="color:#58a6ff;">1.0 s</span></label>
              <input type="range" id="p10_tau" min="0.1" max="10.0" step="0.1" value="1.0" style="width:100%;">
            </div>
            <div style="border-top:1px solid #30363d; padding-top:8px; font-size:12px; line-height:1.6;">
              <div style="display:flex; justify-content:space-between;"><span>WLF Shift log(aT):</span><strong id="p10_log_at" style="color:#f0883e;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Peak tan &delta;:</span><strong id="p10_peak_tan" style="color:#f85149;">--</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Glassy Modulus Eg:</span><strong id="p10_eg" style="color:#58a6ff;">3.0 GPa</strong></div>
              <div style="display:flex; justify-content:space-between;"><span>Rubbery Modulus Er:</span><strong id="p10_er" style="color:#7ee787;">1.0 MPa</strong></div>
            </div>
          </div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('canvas');
    const modeSelect = el.querySelector('#p10_mode');
    const dtSlider = el.querySelector('#p10_dt');
    const tauSlider = el.querySelector('#p10_tau');
    const dtVal = el.querySelector('#p10_dt_val');
    const tauVal = el.querySelector('#p10_tau_val');
    const logAtVal = el.querySelector('#p10_log_at');
    const peakTanVal = el.querySelector('#p10_peak_tan');

    function update() {
      const mode = modeSelect.value;
      const deltaT = parseFloat(dtSlider.value);
      const tau = parseFloat(tauSlider.value);

      dtVal.textContent = (deltaT >= 0 ? '+' : '') + deltaT + ' K';
      tauVal.textContent = tau.toFixed(1) + ' s';

      // WLF equation with universal constants
      const C1 = 17.44;
      const C2 = 51.6;
      let log_aT = 0;
      if (C2 + deltaT > 0) {
        log_aT = (-C1 * deltaT) / (C2 + deltaT);
      } else {
        log_aT = 15.0; // frozen
      }

      logAtVal.textContent = log_aT.toFixed(3);
      peakTanVal.textContent = "1.25 (at Tg)";

      draw(mode, deltaT, tau, log_aT);
    }

    function draw(mode, deltaT, tau, log_aT) {
      if (!canvas.isConnected) return;
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      ctx.clearRect(0, 0, width, height);

      const margin = { top: 25, right: 30, bottom: 45, left: 60 };
      const w = width - margin.left - margin.right;
      const h = height - margin.top - margin.bottom;

      if (mode === 'dma' || mode === 'wlf') {
        // Frequency domain: log(omega) in [-4 to +4]
        const minLogW = -4, maxLogW = 4;
        function toX(lw) { return margin.left + ((lw - minLogW) / (maxLogW - minLogW)) * w; }
        function toYMod(logMod) { return margin.top + (1 - (logMod - 6) / (9.5 - 6)) * h; }

        // Grid
        ctx.strokeStyle = '#21262d';
        ctx.lineWidth = 1;
        for (let lw = -4; lw <= 4; lw += 2) {
          ctx.beginPath();
          ctx.moveTo(toX(lw), margin.top);
          ctx.lineTo(toX(lw), margin.top + h);
          ctx.stroke();
        }

        // Shift frequency by WLF factor if in WLF mode
        const shift = mode === 'wlf' ? log_aT : 0;

        // Draw Storage Modulus E' (Blue)
        ctx.strokeStyle = '#58a6ff';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let lw = minLogW; lw <= maxLogW; lw += 0.1) {
          const effLw = lw - shift;
          // Sigmoidal transition from 1 MPa (10^6) to 3 GPa (10^9.5)
          const logE = 6.0 + 3.5 / (1 + Math.exp(-effLw * 1.5));
          const px = toX(lw);
          const py = toYMod(logE);
          if (lw === minLogW) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Draw Loss Modulus E'' (Green)
        ctx.strokeStyle = '#7ee787';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let lw = minLogW; lw <= maxLogW; lw += 0.1) {
          const effLw = lw - shift;
          const logEloss = 6.8 + 1.6 * Math.exp(-0.5 * Math.pow(effLw * 1.2, 2));
          const px = toX(lw);
          const py = toYMod(logEloss);
          if (lw === minLogW) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Draw tan delta (Red Dash)
        ctx.strokeStyle = '#f85149';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 4]);
        ctx.beginPath();
        for (let lw = minLogW; lw <= maxLogW; lw += 0.1) {
          const effLw = lw - shift;
          const tanD = Math.exp(-0.5 * Math.pow(effLw * 1.2, 2));
          const py = margin.top + (1 - tanD) * (h * 0.85);
          const px = toX(lw);
          if (lw === minLogW) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();
        ctx.setLineDash([]);

        // Axes
        ctx.strokeStyle = '#8b949e';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(margin.left, margin.top);
        ctx.lineTo(margin.left, margin.top + h);
        ctx.lineTo(margin.left + w, margin.top + h);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.font = '11px sans-serif';
        ctx.textAlign = 'center';
        for (let lw = -4; lw <= 4; lw += 2) {
          ctx.fillText(`10^${lw}`, toX(lw), margin.top + h + 18);
        }
        ctx.fillText('Angular Frequency &omega; (rad/s)', margin.left + w / 2, margin.top + h + 36);

        ctx.save();
        ctx.translate(16, margin.top + h / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText('Log Dynamic Modulus [Pa]', 0, 0);
        ctx.restore();
      } else if (mode === 'maxwell') {
        // Maxwell stress relaxation E(t) = E0 * exp(-t / tau)
        ctx.strokeStyle = '#58a6ff';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let t = 0; t <= 10; t += 0.1) {
          const val = Math.exp(-t / tau);
          const px = margin.left + (t / 10) * w;
          const py = margin.top + (1 - val) * h;
          if (t === 0) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();

        ctx.fillStyle = '#58a6ff';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Maxwell Stress Relaxation: &sigma;(t) = &sigma;0 exp(-t / &tau;R)', margin.left + 20, margin.top + 25);
      } else {
        // Voigt creep: J(t) = (1/E)*(1 - exp(-t/tau))
        ctx.strokeStyle = '#7ee787';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let t = 0; t <= 10; t += 0.1) {
          const val = 1 - Math.exp(-t / tau);
          const px = margin.left + (t / 10) * w;
          const py = margin.top + (1 - val) * h;
          if (t === 0) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();

        ctx.fillStyle = '#7ee787';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('Voigt-Kelvin Creep: &epsilon;(t) = (&sigma;0 / E)[1 - exp(-t / &tau;C)]', margin.left + 20, margin.top + 25);
      }
    }

    [modeSelect, dtSlider, tauSlider].forEach(s => s.addEventListener('input', update));
    update();
  }

  return {
    sim_poly_chain_conformation,
    sim_poly_flory_huggins_phase_diagram,
    sim_poly_mwd_distributions,
    sim_poly_membrane_osmometry,
    sim_poly_zimm_plot_light_scattering,
    sim_poly_carothers_step_growth,
    sim_poly_radical_polymerization_kinetics,
    sim_poly_living_anionic_polymerization,
    sim_poly_polymer_synthesis_mechanisms,
    sim_poly_viscoelastic_rheology_wlf
  };
})();

/* ==========================================================================
   Global Simulation Engine Registry Adapter
   ========================================================================== */
if (typeof window !== 'undefined') {
  window.SimulationEngine = window.SimulationEngine || {};
  Object.keys(window.PolymerChemistrySimulations).forEach(function(key) {
    window[key] = window.PolymerChemistrySimulations[key];
  });
  const originalInit = window.SimulationEngine.initSimulation;
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    const el = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
    if (!el) return;
    if (window.PolymerChemistrySimulations && typeof window.PolymerChemistrySimulations[simType] === 'function') {
      return window.PolymerChemistrySimulations[simType](el);
    }
    if (typeof window[simType] === 'function') {
      return window[simType](el);
    }
    if (originalInit) {
      return originalInit(containerId, simType);
    }
    console.warn("Simulation not found:", simType);
  };
}
