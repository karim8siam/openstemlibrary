# -*- coding: utf-8 -*-
"""
Generate environmental-chemistry-sims.js
Contains 10 interactive, 60 FPS HTML5 Canvas simulations for Environmental Chemistry.
Strictly no marks, no course codes, pure Unix line endings.
"""

def generate_sims_js():
    code = r'''/**
 * environmental-chemistry-sims.js
 * 10 High-Performance 60 FPS Interactive HTML5 Canvas Simulation Engines
 * for Environmental Chemistry (OpenSTEM Milestone Textbook #57)
 * Equipped with Dimension-Caching, DPR Scaling, and isConnected Cleanup Guards.
 */

window.EnvironmentalChemistrySimulations = (function() {
  'use strict';

  function initCanvas(canvas) {
    if (!canvas) return null;
    const dpr = window.devicePixelRatio || 1;
    let w = canvas._cssWidth;
    let h = canvas._cssHeight;

    if (!w || !h) {
      const rect = canvas.getBoundingClientRect();
      w = Math.floor(rect.width > 0 ? rect.width : (canvas.parentElement ? canvas.parentElement.clientWidth : 800)) || 800;
      h = Math.floor(rect.height > 0 ? rect.height : (canvas.parentElement ? canvas.parentElement.clientHeight : 420)) || 420;
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

  if (typeof window !== 'undefined' && typeof window.addEventListener === 'function') {
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
     SIMULATION 1: Photochemical Smog Kinetics (Leighton Photostationary State)
     ========================================================================== */
  function sim_env_photochemical_smog_kinetics(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div style="background:#0d1117; border:1px solid #30363d; border-radius:8px; padding:16px; color:#c9d1d9; font-family:system-ui,-apple-system,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:16px;">Photochemical Smog & Leighton Photostationary Kinetics</h4>
            <div style="font-size:12px; color:#8b949e;">Diurnal NOx-VOC-O3 Evolution & Leighton Relationship: [O3] = (k1/k3) · [NO2]/[NO]</div>
          </div>
          <div style="display:flex; gap:8px;">
            <button id="smog_play" style="background:#238636; color:#fff; border:none; padding:4px 12px; border-radius:4px; cursor:pointer; font-size:12px;">Pause</button>
            <button id="smog_reset" style="background:#21262d; color:#c9d1d9; border:1px solid #30363d; padding:4px 12px; border-radius:4px; cursor:pointer; font-size:12px;">Reset</button>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">VOC Reactivity (ppbC): <span id="smog_voc_val" style="color:#58a6ff; font-weight:600;">600</span></label>
            <input type="range" id="smog_voc" min="50" max="1500" value="600" step="25" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Peak Solar UV Actinide Flux: <span id="smog_uv_val" style="color:#58a6ff; font-weight:600;">1.0x</span></label>
            <input type="range" id="smog_uv" min="0.2" max="2.0" value="1.0" step="0.1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Initial Morning NOx (ppb): <span id="smog_nox_val" style="color:#58a6ff; font-weight:600;">120</span></label>
            <input type="range" id="smog_nox" min="20" max="300" value="120" step="10" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Simulation Hour: <span id="smog_hour_val" style="color:#38ef7d; font-weight:600;">12:00 PM</span></label>
            <input type="range" id="smog_time_scrub" min="0" max="24" value="12" step="0.1" style="width:100%;">
          </div>
        </div>
        <canvas class="sim-canvas" style="width:100%; height:320px; background:#040d1a; border-radius:6px; display:block;"></canvas>
        <div style="display:flex; justify-content:space-around; margin-top:8px; font-size:12px; border-top:1px solid #21262d; padding-top:8px;">
          <div><span style="display:inline-block; width:10px; height:10px; background:#58a6ff; border-radius:50%; margin-right:4px;"></span>NO: <span id="m_no" style="font-weight:600; color:#58a6ff;">--</span> ppb</div>
          <div><span style="display:inline-block; width:10px; height:10px; background:#e3b341; border-radius:50%; margin-right:4px;"></span>NO2: <span id="m_no2" style="font-weight:600; color:#e3b341;">--</span> ppb</div>
          <div><span style="display:inline-block; width:10px; height:10px; background:#f85149; border-radius:50%; margin-right:4px;"></span>O3: <span id="m_o3" style="font-weight:600; color:#f85149;">--</span> ppb</div>
          <div><span style="display:inline-block; width:10px; height:10px; background:#a371f7; border-radius:50%; margin-right:4px;"></span>PAN: <span id="m_pan" style="font-weight:600; color:#a371f7;">--</span> ppb</div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const playBtn = el.querySelector('#smog_play');
    const resetBtn = el.querySelector('#smog_reset');
    const vocS = el.querySelector('#smog_voc');
    const uvS = el.querySelector('#smog_uv');
    const noxS = el.querySelector('#smog_nox');
    const timeS = el.querySelector('#smog_time_scrub');

    let isPlaying = true;
    let animId = null;
    let curHour = 6.0;

    function getConcentrations(t, voc, uv, initNox) {
      // 0 to 24 hr model
      const sun = Math.max(0, Math.sin((t - 6) / 12 * Math.PI)) * uv;
      // Diurnal profiles
      const morningRush = Math.exp(-Math.pow((t - 7.5)/1.8, 2));
      const eveningRush = Math.exp(-Math.pow((t - 18)/2.2, 2));
      
      const no = (initNox * 0.7 * morningRush + initNox * 0.4 * eveningRush + 5) * (1 / (1 + 4 * sun));
      const no2 = (initNox * 0.4 + initNox * 0.5 * morningRush) * (0.3 + 0.7 * Math.exp(-Math.pow((t - 10)/3.5, 2)));
      
      const vocRad = voc * 0.001 * sun;
      const o3Peak = Math.max(10, (120 * sun * (voc / 500) * (no2 / 40) / (1 + no / 30)));
      const o3 = o3Peak * (0.1 + 0.9 * Math.exp(-Math.pow((t - 14)/3.5, 2)));
      const pan = o3 * 0.22 * (voc / 600);

      return { no: Math.max(1, no), no2: Math.max(2, no2), o3: Math.max(5, o3), pan: Math.max(0.5, pan), sun };
    }

    function render() {
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      if (!canvas.isConnected) return;

      const voc = parseFloat(vocS.value);
      const uv = parseFloat(uvS.value);
      const initNox = parseFloat(noxS.value);

      if (isPlaying) {
        curHour += 0.04;
        if (curHour > 24) curHour = 0;
        timeS.value = curHour.toFixed(1);
      } else {
        curHour = parseFloat(timeS.value);
      }

      const hFloor = Math.floor(curHour);
      const mFloor = Math.floor((curHour - hFloor) * 60);
      const ampm = hFloor >= 12 ? 'PM' : 'AM';
      const dispH = hFloor % 12 === 0 ? 12 : hFloor % 12;
      el.querySelector('#smog_hour_val').textContent = `${dispH}:${mFloor < 10 ? '0' : ''}${mFloor} ${ampm}`;

      const curVals = getConcentrations(curHour, voc, uv, initNox);
      el.querySelector('#m_no').textContent = curVals.no.toFixed(1);
      el.querySelector('#m_no2').textContent = curVals.no2.toFixed(1);
      el.querySelector('#m_o3').textContent = curVals.o3.toFixed(1);
      el.querySelector('#m_pan').textContent = curVals.pan.toFixed(1);

      ctx.clearRect(0, 0, width, height);

      // Plot margins
      const padL = 50, padR = 20, padT = 30, padB = 40;
      const plotW = width - padL - padR;
      const plotH = height - padT - padB;

      // Draw background grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let h = 0; h <= 24; h += 3) {
        const x = padL + (h / 24) * plotW;
        ctx.beginPath();
        ctx.moveTo(x, padT);
        ctx.lineTo(x, padT + plotH);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.font = '10px system-ui';
        ctx.textAlign = 'center';
        ctx.fillText(`${h}h`, x, padT + plotH + 16);
      }

      const maxPpb = 220;
      for (let p = 0; p <= maxPpb; p += 50) {
        const y = padT + plotH - (p / maxPpb) * plotH;
        ctx.beginPath();
        ctx.moveTo(padL, y);
        ctx.lineTo(padL + plotW, y);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.textAlign = 'right';
        ctx.fillText(`${p}`, padL - 8, y + 3);
      }

      // Title & Y-axis label
      ctx.fillStyle = '#8b949e';
      ctx.textAlign = 'left';
      ctx.fillText('Mixing Ratio (ppb)', padL, padT - 12);

      // Sun curve background
      ctx.fillStyle = 'rgba(255, 235, 59, 0.06)';
      ctx.beginPath();
      ctx.moveTo(padL, padT + plotH);
      for (let t = 0; t <= 24; t += 0.2) {
        const x = padL + (t / 24) * plotW;
        const s = Math.max(0, Math.sin((t - 6) / 12 * Math.PI)) * uv;
        const y = padT + plotH - (s / 2.0) * (plotH * 0.9);
        ctx.lineTo(x, y);
      }
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.closePath();
      ctx.fill();

      // Plot Curves
      function drawCurve(prop, color) {
        ctx.strokeStyle = color;
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let t = 0; t <= 24; t += 0.2) {
          const x = padL + (t / 24) * plotW;
          const val = getConcentrations(t, voc, uv, initNox)[prop];
          const y = padT + plotH - Math.min(plotH, (val / maxPpb) * plotH);
          if (t === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();
      }

      drawCurve('no', '#58a6ff');
      drawCurve('no2', '#e3b341');
      drawCurve('o3', '#f85149');
      drawCurve('pan', '#a371f7');

      // Draw threshold line for O3 (National 8-hr standard ~ 70 ppb)
      const yO3Thresh = padT + plotH - (70 / maxPpb) * plotH;
      ctx.strokeStyle = 'rgba(248, 81, 73, 0.4)';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(padL, yO3Thresh);
      ctx.lineTo(padL + plotW, yO3Thresh);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = 'rgba(248, 81, 73, 0.8)';
      ctx.textAlign = 'right';
      ctx.fillText('NAAQS O3 (70 ppb)', padL + plotW - 6, yO3Thresh - 4);

      // Current time line
      const curX = padL + (curHour / 24) * plotW;
      ctx.strokeStyle = '#38ef7d';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(curX, padT);
      ctx.lineTo(curX, padT + plotH);
      ctx.stroke();

      // Current time indicator circle
      ctx.fillStyle = '#38ef7d';
      ctx.beginPath();
      ctx.arc(curX, padT + plotH, 5, 0, Math.PI * 2);
      ctx.fill();

      if (isPlaying) {
        animId = requestAnimationFrame(render);
      }
    }

    playBtn.addEventListener('click', () => {
      isPlaying = !isPlaying;
      playBtn.textContent = isPlaying ? 'Pause' : 'Resume';
      playBtn.style.background = isPlaying ? '#238636' : '#1f6feb';
      if (isPlaying) render();
    });

    resetBtn.addEventListener('click', () => {
      curHour = 6.0;
      timeS.value = 6.0;
      vocS.value = 600;
      uvS.value = 1.0;
      noxS.value = 120;
      el.querySelector('#smog_voc_val').textContent = '600';
      el.querySelector('#smog_uv_val').textContent = '1.0x';
      el.querySelector('#smog_nox_val').textContent = '120';
      if (!isPlaying) render();
    });

    [vocS, uvS, noxS].forEach(s => s.addEventListener('input', () => {
      el.querySelector('#smog_voc_val').textContent = vocS.value;
      el.querySelector('#smog_uv_val').textContent = uvS.value + 'x';
      el.querySelector('#smog_nox_val').textContent = noxS.value;
      if (!isPlaying) render();
    }));

    timeS.addEventListener('input', () => {
      if (isPlaying) {
        isPlaying = false;
        playBtn.textContent = 'Resume';
        playBtn.style.background = '#1f6feb';
      }
      render();
    });

    render();
  }

  /* ==========================================================================
     SIMULATION 2: Greenhouse Effect & Radiative Forcing
     ========================================================================== */
  function sim_env_greenhouse_radiative_forcing(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div style="background:#0d1117; border:1px solid #30363d; border-radius:8px; padding:16px; color:#c9d1d9; font-family:system-ui,-apple-system,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:16px;">Greenhouse Effect & Planetary Energy Balance</h4>
            <div style="font-size:12px; color:#8b949e;">Radiative Forcing: ΔF = 5.35 · ln(C/C0) & Atmospheric IR Window (8–14 μm) Closure</div>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Atmospheric CO2 (ppm): <span id="gh_co2_val" style="color:#f85149; font-weight:600;">420</span></label>
            <input type="range" id="gh_co2" min="280" max="1120" value="420" step="10" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Methane CH4 (ppb): <span id="gh_ch4_val" style="color:#e3b341; font-weight:600;">1900</span></label>
            <input type="range" id="gh_ch4" min="700" max="3500" value="1900" step="50" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Surface Albedo (α): <span id="gh_albedo_val" style="color:#58a6ff; font-weight:600;">0.30</span></label>
            <input type="range" id="gh_albedo" min="0.10" max="0.60" value="0.30" step="0.01" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Climate Sensitivity S (K/(W/m²)): <span id="gh_cs_val" style="color:#38ef7d; font-weight:600;">0.80</span></label>
            <input type="range" id="gh_cs" min="0.40" max="1.20" value="0.80" step="0.05" style="width:100%;">
          </div>
        </div>
        <canvas class="sim-canvas" style="width:100%; height:320px; background:#040d1a; border-radius:6px; display:block;"></canvas>
        <div style="display:flex; justify-content:space-around; margin-top:8px; font-size:12px; border-top:1px solid #21262d; padding-top:8px;">
          <div>Radiative Forcing ΔF: <span id="m_dF" style="font-weight:600; color:#f85149;">--</span> W/m²</div>
          <div>Equilibrium Warming ΔTs: <span id="m_dTs" style="font-weight:600; color:#e3b341;">--</span> °C</div>
          <div>Global Mean Temp Ts: <span id="m_Ts" style="font-weight:600; color:#38ef7d;">--</span> °C</div>
          <div>IR Window Transmission: <span id="m_ir_trans" style="font-weight:600; color:#58a6ff;">--</span> %</div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const co2S = el.querySelector('#gh_co2');
    const ch4S = el.querySelector('#gh_ch4');
    const albedoS = el.querySelector('#gh_albedo');
    const csS = el.querySelector('#gh_cs');

    let animId = null;
    let photonPhase = 0;

    function render() {
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      if (!canvas.isConnected) return;

      const co2 = parseFloat(co2S.value);
      const ch4 = parseFloat(ch4S.value);
      const albedo = parseFloat(albedoS.value);
      const cs = parseFloat(csS.value);

      el.querySelector('#gh_co2_val').textContent = co2;
      el.querySelector('#gh_ch4_val').textContent = ch4;
      el.querySelector('#gh_albedo_val').textContent = albedo.toFixed(2);
      el.querySelector('#gh_cs_val').textContent = cs.toFixed(2);

      // Compute Radiative Forcing
      const dF_co2 = 5.35 * Math.log(co2 / 280);
      const dF_ch4 = 0.036 * (Math.sqrt(ch4) - Math.sqrt(700));
      const dF_tot = dF_co2 + dF_ch4;

      const dTs = cs * dF_tot;
      const baseTs = 14.0 + (0.30 - albedo) * 30; // base ~14 C at albedo 0.30
      const Ts = baseTs + dTs;

      const irTrans = Math.max(5, 75 * Math.exp(-0.0012 * (co2 - 280) - 0.0003 * (ch4 - 700)));

      el.querySelector('#m_dF').textContent = '+' + dF_tot.toFixed(2);
      el.querySelector('#m_dTs').textContent = '+' + dTs.toFixed(2);
      el.querySelector('#m_Ts').textContent = Ts.toFixed(2);
      el.querySelector('#m_ir_trans').textContent = irTrans.toFixed(1);

      ctx.clearRect(0, 0, width, height);

      // Left panel: Planetary Energy Balance Animation (45% width)
      // Right panel: IR Emission Spectrum & Window Closure (55% width)
      const leftW = width * 0.45;
      const rightW = width * 0.55;

      // Draw Earth surface
      const surfY = height * 0.78;
      const atmY = height * 0.35;

      // Atmosphere gradient
      const atmGrad = ctx.createLinearGradient(0, atmY - 30, 0, surfY);
      atmGrad.addColorStop(0, 'rgba(56, 189, 248, 0.05)');
      atmGrad.addColorStop(0.5, `rgba(239, 68, 68, ${0.1 + (co2/1120)*0.2})`);
      atmGrad.addColorStop(1, 'rgba(30, 41, 59, 0.8)');
      ctx.fillStyle = atmGrad;
      ctx.fillRect(10, atmY, leftW - 20, surfY - atmY);

      // Atmosphere border
      ctx.strokeStyle = '#38bdf8';
      ctx.setLineDash([3, 3]);
      ctx.strokeRect(10, atmY, leftW - 20, surfY - atmY);
      ctx.setLineDash([]);
      ctx.fillStyle = '#38bdf8';
      ctx.font = '10px system-ui';
      ctx.fillText('Troposphere (CO2, CH4, H2O layer)', 16, atmY + 14);

      // Earth Ground
      ctx.fillStyle = albedo > 0.4 ? '#cbd5e1' : '#22c55e';
      ctx.beginPath();
      ctx.ellipse(leftW * 0.5, surfY + 120, leftW * 0.5, 130, 0, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 12px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText(`Earth Surface: ${Ts.toFixed(1)} °C`, leftW * 0.5, surfY + 28);

      // Incoming solar radiation beam
      ctx.strokeStyle = '#facc15';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(35, 15);
      ctx.lineTo(leftW * 0.3, surfY);
      ctx.stroke();

      // Reflected shortwave
      ctx.strokeStyle = 'rgba(250, 204, 21, 0.6)';
      ctx.lineWidth = 2 + albedo * 4;
      ctx.beginPath();
      ctx.moveTo(leftW * 0.3, surfY);
      ctx.lineTo(leftW * 0.55, 15);
      ctx.stroke();

      // Upwelling terrestrial IR radiation
      photonPhase += 0.05;
      const numIR = 6;
      for (let i = 0; i < numIR; i++) {
        const x = 40 + i * (leftW - 70) / (numIR - 1);
        const yOffset = (photonPhase * 30 + i * 20) % (surfY - atmY);
        const y = surfY - yOffset;
        
        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        ctx.arc(x, y, 3, 0, Math.PI * 2);
        ctx.fill();

        // Downward back-radiation greenhouse flux
        const yBack = atmY + yOffset;
        ctx.fillStyle = 'rgba(248, 113, 113, 0.7)';
        ctx.beginPath();
        ctx.arc(x + 12, yBack, 2.5, 0, Math.PI * 2);
        ctx.fill();
      }

      ctx.fillStyle = '#ef4444';
      ctx.font = '10px system-ui';
      ctx.textAlign = 'left';
      ctx.fillText('↑ Outgoing IR', 16, surfY - 10);
      ctx.fillText('↓ Back-Radiation', 16, atmY + 30);

      // Right Panel: Infrared Window Absorption Spectrum
      const rX = leftW + 30;
      const rY = 40;
      const rW = width - rX - 20;
      const rH = height - 80;

      ctx.strokeStyle = '#30363d';
      ctx.lineWidth = 1;
      ctx.strokeRect(rX, rY, rW, rH);

      ctx.fillStyle = '#8b949e';
      ctx.font = '11px system-ui';
      ctx.textAlign = 'left';
      ctx.fillText('Atmospheric Transmission & 8–14 μm IR Window', rX + 8, rY - 10);

      // Draw IR transmission spectrum (Wavelength 4 to 20 um)
      ctx.beginPath();
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 2;
      for (let wl = 4; wl <= 20; wl += 0.2) {
        const px = rX + ((wl - 4) / 16) * rW;
        // Absorption bands: CO2 at 15 um, CH4 at 7.7 um, H2O < 8 and > 18
        let trans = 1.0;
        if (wl >= 13.5 && wl <= 16.5) { // CO2 15 um band
          const co2Depth = Math.min(0.99, (co2 / 280) * 0.85);
          trans *= (1 - co2Depth * Math.exp(-Math.pow((wl - 15) / 0.8, 2)));
        }
        if (wl >= 7.0 && wl <= 8.5) { // CH4 band
          const ch4Depth = Math.min(0.95, (ch4 / 700) * 0.6);
          trans *= (1 - ch4Depth * Math.exp(-Math.pow((wl - 7.7) / 0.5, 2)));
        }
        if (wl < 8.0) trans *= (0.2 + 0.8 * (wl - 4) / 4);
        if (wl > 17.0) trans *= (0.1 + 0.9 * Math.max(0, (20 - wl) / 3));

        const py = rY + rH - trans * (rH * 0.85);
        if (wl === 4) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Highlight the 8 - 14 um window
      const winX1 = rX + ((8 - 4) / 16) * rW;
      const winX2 = rX + ((14 - 4) / 16) * rW;
      ctx.fillStyle = 'rgba(56, 189, 248, 0.12)';
      ctx.fillRect(winX1, rY, winX2 - winX1, rH);

      ctx.fillStyle = '#38bdf8';
      ctx.font = '10px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText('8–14 μm Window', (winX1 + winX2) * 0.5, rY + 16);
      ctx.fillText(`Trans: ${irTrans.toFixed(0)}%`, (winX1 + winX2) * 0.5, rY + 30);

      // CO2 15 um marker
      const co2X = rX + ((15 - 4) / 16) * rW;
      ctx.fillStyle = '#f85149';
      ctx.fillText('CO2 (15 μm)', co2X, rY + rH - 10);

      // X-axis label
      ctx.fillStyle = '#8b949e';
      ctx.fillText('Wavelength λ (μm)', rX + rW * 0.5, rY + rH + 18);
      ctx.textAlign = 'left';
      ctx.fillText('4', rX, rY + rH + 18);
      ctx.textAlign = 'right';
      ctx.fillText('20', rX + rW, rY + rH + 18);

      animId = requestAnimationFrame(render);
    }

    [co2S, ch4S, albedoS, csS].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 3: Stratospheric Ozone Dynamics & Chapman-Catalytic Cycle
     ========================================================================== */
  function sim_env_stratospheric_ozone_chapman(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div style="background:#0d1117; border:1px solid #30363d; border-radius:8px; padding:16px; color:#c9d1d9; font-family:system-ui,-apple-system,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:16px;">Stratospheric Ozone Dynamics & Catalytic ClOx Depletion</h4>
            <div style="font-size:12px; color:#8b949e;">Chapman Photochemical Mechanism vs Halogen Radical Dimer Catalysis: [O3]ss vs Altitude</div>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Active Chlorine ClOx (ppb): <span id="oz_cl_val" style="color:#f85149; font-weight:600;">2.5</span></label>
            <input type="range" id="oz_cl" min="0.0" max="6.0" value="2.5" step="0.1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Polar Stratospheric Clouds (PSCs): <span id="oz_psc_val" style="color:#58a6ff; font-weight:600;">Active</span></label>
            <input type="range" id="oz_psc" min="0" max="1" value="1" step="1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Solar UV-C Actinic Flux: <span id="oz_uvc_val" style="color:#e3b341; font-weight:600;">1.0x</span></label>
            <input type="range" id="oz_uvc" min="0.5" max="2.0" value="1.0" step="0.1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Polar Vortex Temperature: <span id="oz_temp_val" style="color:#38ef7d; font-weight:600;">192 K (-81°C)</span></label>
            <input type="range" id="oz_temp" min="185" max="230" value="192" step="1" style="width:100%;">
          </div>
        </div>
        <canvas class="sim-canvas" style="width:100%; height:320px; background:#040d1a; border-radius:6px; display:block;"></canvas>
        <div style="display:flex; justify-content:space-around; margin-top:8px; font-size:12px; border-top:1px solid #21262d; padding-top:8px;">
          <div>Column Ozone: <span id="m_dobson" style="font-weight:600; color:#58a6ff;">--</span> Dobson Units (DU)</div>
          <div>Peak O3 Altitude: <span id="m_peak_alt" style="font-weight:600; color:#38ef7d;">--</span> km</div>
          <div>Ozone Loss Rate: <span id="m_loss_rate" style="font-weight:600; color:#f85149;">--</span> %/day</div>
          <div>Ozone Hole Status: <span id="m_hole_stat" style="font-weight:600; color:#e3b341;">--</span></div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const clS = el.querySelector('#oz_cl');
    const pscS = el.querySelector('#oz_psc');
    const uvcS = el.querySelector('#oz_uvc');
    const tempS = el.querySelector('#oz_temp');

    let animId = null;
    let vortexAngle = 0;

    function render() {
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      if (!canvas.isConnected) return;

      const cl = parseFloat(clS.value);
      const psc = parseInt(pscS.value, 10);
      const uvc = parseFloat(uvcS.value);
      const temp = parseFloat(tempS.value);

      el.querySelector('#oz_cl_val').textContent = cl.toFixed(1);
      el.querySelector('#oz_psc_val').textContent = psc === 1 ? 'Active (Type I/II)' : 'Inactive';
      el.querySelector('#oz_uvc_val').textContent = uvc.toFixed(1) + 'x';
      el.querySelector('#oz_temp_val').textContent = `${temp} K (${(temp - 273.15).toFixed(0)}°C)`;

      // Chapman profile vs Depleted profile
      // Altitudes: 10 km to 50 km
      const pscFactor = psc === 1 && temp < 197 ? 1.0 + (197 - temp) * 0.15 : 0.1;
      const lossRate = cl * 0.8 * pscFactor;
      
      let totalDU = 0;
      let peakAlt = 25;
      let maxO3 = 0;

      for (let z = 10; z <= 50; z += 1) {
        // Chapman theoretical production: peaks at 26 km
        const chapmanO3 = 4.5e12 * Math.exp(-Math.pow((z - 26) / 7, 2)) * Math.sqrt(uvc);
        // Depletion localized in lower stratosphere (15 - 24 km)
        let dep = 1.0;
        if (z >= 14 && z <= 26) {
          dep = Math.max(0.05, 1.0 - (lossRate * 0.25) * Math.exp(-Math.pow((z - 20)/4, 2)));
        }
        const actualO3 = chapmanO3 * dep;
        if (actualO3 > maxO3) {
          maxO3 = actualO3;
          peakAlt = z;
        }
        totalDU += actualO3 * 1e5 * 1e-11; // scaling to DU
      }
      totalDU = Math.max(90, Math.min(420, totalDU * 0.08));

      el.querySelector('#m_dobson').textContent = totalDU.toFixed(0);
      el.querySelector('#m_peak_alt').textContent = peakAlt;
      el.querySelector('#m_loss_rate').textContent = (lossRate * 1.5).toFixed(1);
      el.querySelector('#m_hole_stat').textContent = totalDU < 220 ? 'CRITICAL HOLE (<220 DU)' : 'STABLE / NORMAL';
      el.querySelector('#m_hole_stat').style.color = totalDU < 220 ? '#f85149' : '#38ef7d';

      ctx.clearRect(0, 0, width, height);

      // Left panel: Vertical Ozone Density Profile [O3] vs Altitude (z: 10 - 50 km)
      // Right panel: Polar Vortex & ClO Dimer Catalytic Cycle Diagram
      const leftW = width * 0.52;
      const rightX = leftW + 20;
      const rightW = width - rightX - 10;

      // Vertical Profile axes
      const padL = 45, padB = 40, padT = 30;
      const plotW = leftW - padL - 10;
      const plotH = height - padT - padB;

      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      ctx.strokeRect(padL, padT, plotW, plotH);

      // Y-axis: Altitude 10 to 50 km
      ctx.fillStyle = '#8b949e';
      ctx.font = '10px system-ui';
      ctx.textAlign = 'right';
      for (let z = 10; z <= 50; z += 10) {
        const y = padT + plotH - ((z - 10) / 40) * plotH;
        ctx.fillText(`${z} km`, padL - 6, y + 3);
        ctx.beginPath();
        ctx.moveTo(padL, y);
        ctx.lineTo(padL + plotW, y);
        ctx.stroke();
      }

      ctx.textAlign = 'left';
      ctx.fillText('Altitude (km)', 10, padT - 12);
      ctx.textAlign = 'center';
      ctx.fillText('Ozone Number Density [O3] (10¹² cm⁻³)', padL + plotW * 0.5, padT + plotH + 28);

      // Draw Chapman baseline (Unperturbed)
      ctx.strokeStyle = '#38a169';
      ctx.setLineDash([4, 4]);
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let z = 10; z <= 50; z += 0.5) {
        const y = padT + plotH - ((z - 10) / 40) * plotH;
        const chapO3 = 4.5 * Math.exp(-Math.pow((z - 26) / 7, 2)) * Math.sqrt(uvc);
        const x = padL + (chapO3 / 5.0) * plotW;
        if (z === 10) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw Actual Depleted Ozone Profile
      ctx.strokeStyle = totalDU < 220 ? '#f85149' : '#58a6ff';
      ctx.lineWidth = 3;
      ctx.beginPath();
      for (let z = 10; z <= 50; z += 0.5) {
        const y = padT + plotH - ((z - 10) / 40) * plotH;
        const chapO3 = 4.5 * Math.exp(-Math.pow((z - 26) / 7, 2)) * Math.sqrt(uvc);
        let dep = 1.0;
        if (z >= 14 && z <= 26) {
          dep = Math.max(0.05, 1.0 - (lossRate * 0.25) * Math.exp(-Math.pow((z - 20)/4, 2)));
        }
        const actO3 = chapO3 * dep;
        const x = padL + (actO3 / 5.0) * plotW;
        if (z === 10) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Legend
      ctx.fillStyle = '#38a169';
      ctx.textAlign = 'left';
      ctx.fillText('-- Chapman Baseline', padL + 10, padT + 20);
      ctx.fillStyle = totalDU < 220 ? '#f85149' : '#58a6ff';
      ctx.fillText('— Actual Depleted Profile', padL + 10, padT + 36);

      // Right Panel: ClO Dimer Cycle Animation
      vortexAngle += 0.02;
      const cX = rightX + rightW * 0.5;
      const cY = height * 0.48;
      const r = Math.min(rightW * 0.38, 65);

      ctx.fillStyle = '#c9d1d9';
      ctx.font = '11px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText('Molina-Molina ClO Dimer Catalytic Cycle', cX, 25);

      // Catalytic cycle circle
      ctx.strokeStyle = '#a371f7';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(cX, cY, r, 0, Math.PI * 2);
      ctx.stroke();

      // Reaction labels around ring
      const nodes = [
        { label: '2 Cl', angle: 0 },
        { label: '2 ClO', angle: Math.PI * 0.5 },
        { label: 'Cl2O2 (Dimer)', angle: Math.PI },
        { label: 'ClOO + Cl', angle: Math.PI * 1.5 }
      ];

      nodes.forEach((n, idx) => {
        const nx = cX + Math.cos(n.angle + vortexAngle) * r;
        const ny = cY + Math.sin(n.angle + vortexAngle) * r;
        ctx.fillStyle = '#161b22';
        ctx.beginPath();
        ctx.arc(nx, ny, 16, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#58a6ff';
        ctx.stroke();
        ctx.fillStyle = '#f0f6fc';
        ctx.font = 'bold 9px system-ui';
        ctx.fillText(n.label, nx, ny + 3);
      });

      // Net reaction summary box
      ctx.fillStyle = '#161b22';
      ctx.fillRect(rightX + 10, height - 75, rightW - 20, 60);
      ctx.strokeStyle = '#30363d';
      ctx.strokeRect(rightX + 10, height - 75, rightW - 20, 60);

      ctx.fillStyle = '#f85149';
      ctx.font = 'bold 11px system-ui';
      ctx.fillText('Net: 2 O3 + hν → 3 O2', cX, height - 52);
      ctx.fillStyle = '#8b949e';
      ctx.font = '10px system-ui';
      ctx.fillText('1 Chlorine atom destroys > 100,000 O3', cX, height - 32);

      animId = requestAnimationFrame(render);
    }

    [clS, pscS, uvcS, tempS].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 4: Streeter-Phelps Dissolved Oxygen Sag Curve
     ========================================================================== */
  function sim_env_streeter_phelps_dissolved_oxygen(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div style="background:#0d1117; border:1px solid #30363d; border-radius:8px; padding:16px; color:#c9d1d9; font-family:system-ui,-apple-system,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:16px;">Streeter-Phelps Dissolved Oxygen Sag Curve</h4>
            <div style="font-size:12px; color:#8b949e;">Deoxygenation (kd) vs Reaeration (kr) Deficit Dynamics: D(t) = [kd L0 / (kr - kd)] · (e^(-kd t) - e^(-kr t)) + D0 e^(-kr t)</div>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Initial Mixed BOD L0 (mg/L): <span id="sp_bod_val" style="color:#f85149; font-weight:600;">25.0</span></label>
            <input type="range" id="sp_bod" min="5.0" max="60.0" value="25.0" step="1.0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Reaeration Rate kr (day⁻¹): <span id="sp_kr_val" style="color:#58a6ff; font-weight:600;">0.45</span></label>
            <input type="range" id="sp_kr" min="0.10" max="1.20" value="0.45" step="0.05" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Deoxygenation Rate kd (day⁻¹): <span id="sp_kd_val" style="color:#e3b341; font-weight:600;">0.20</span></label>
            <input type="range" id="sp_kd" min="0.05" max="0.50" value="0.20" step="0.02" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">River Flow Velocity (km/day): <span id="sp_vel_val" style="color:#38ef7d; font-weight:600;">30</span></label>
            <input type="range" id="sp_vel" min="10" max="80" value="30" step="5" style="width:100%;">
          </div>
        </div>
        <canvas class="sim-canvas" style="width:100%; height:320px; background:#040d1a; border-radius:6px; display:block;"></canvas>
        <div style="display:flex; justify-content:space-around; margin-top:8px; font-size:12px; border-top:1px solid #21262d; padding-top:8px;">
          <div>Critical Time tc: <span id="m_tc" style="font-weight:600; color:#e3b341;">--</span> days</div>
          <div>Critical Distance xc: <span id="m_xc" style="font-weight:600; color:#58a6ff;">--</span> km</div>
          <div>Minimum DO: <span id="m_min_do" style="font-weight:600; color:#f85149;">--</span> mg/L</div>
          <div>Aquatic Life Status: <span id="m_eco_stat" style="font-weight:600; color:#38ef7d;">--</span></div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const bodS = el.querySelector('#sp_bod');
    const krS = el.querySelector('#sp_kr');
    const kdS = el.querySelector('#sp_kd');
    const velS = el.querySelector('#sp_vel');

    let animId = null;
    let wavePhase = 0;

    function render() {
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      if (!canvas.isConnected) return;

      const L0 = parseFloat(bodS.value);
      const kr = parseFloat(krS.value);
      const kd = parseFloat(kdS.value);
      const vel = parseFloat(velS.value);

      el.querySelector('#sp_bod_val').textContent = L0.toFixed(1);
      el.querySelector('#sp_kr_val').textContent = kr.toFixed(2);
      el.querySelector('#sp_kd_val').textContent = kd.toFixed(2);
      el.querySelector('#sp_vel_val').textContent = vel;

      const DO_sat = 9.0; // Saturation DO at 20 C
      const D0 = 1.5;     // Initial deficit (DO = 7.5 mg/L)

      // Critical time tc and distance xc
      // tc = [1 / (kr - kd)] · ln[ (kr / kd) · (1 - D0(kr - kd) / (kd L0)) ]
      let tc = 0;
      if (Math.abs(kr - kd) > 0.001) {
        const arg = (kr / kd) * (1 - (D0 * (kr - kd)) / (kd * L0));
        tc = arg > 0 ? (1 / (kr - kd)) * Math.log(arg) : 0;
      } else {
        tc = 1 / kd;
      }
      tc = Math.max(0, tc);
      const xc = tc * vel;

      // Deficit at critical point
      const Dc = (kd / kr) * L0 * Math.exp(-kd * tc);
      const minDO = Math.max(0, DO_sat - Dc);

      el.querySelector('#m_tc').textContent = tc.toFixed(2);
      el.querySelector('#m_xc').textContent = xc.toFixed(1);
      el.querySelector('#m_min_do').textContent = minDO.toFixed(2);
      
      const ecoStat = minDO >= 5.0 ? 'HEALTHY (DO ≥ 5)' : minDO >= 2.0 ? 'HYPOXIC STRESS (2–5 mg/L)' : 'SEVERE ANOXIA (<2 mg/L, FISH KILL)';
      el.querySelector('#m_eco_stat').textContent = ecoStat;
      el.querySelector('#m_eco_stat').style.color = minDO >= 5.0 ? '#38ef7d' : minDO >= 2.0 ? '#e3b341' : '#f85149';

      ctx.clearRect(0, 0, width, height);

      // Plot margins: Distance 0 to 150 km, DO from 0 to 10 mg/L
      const padL = 45, padR = 25, padT = 30, padB = 40;
      const plotW = width - padL - padR;
      const plotH = height - padT - padB;
      const maxDist = 150; // km

      // Grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let xDist = 0; xDist <= maxDist; xDist += 25) {
        const px = padL + (xDist / maxDist) * plotW;
        ctx.beginPath();
        ctx.moveTo(px, padT);
        ctx.lineTo(px, padT + plotH);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.font = '10px system-ui';
        ctx.textAlign = 'center';
        ctx.fillText(`${xDist} km`, px, padT + plotH + 16);
      }

      for (let d = 0; d <= 10; d += 2) {
        const py = padT + plotH - (d / 10) * plotH;
        ctx.beginPath();
        ctx.moveTo(padL, py);
        ctx.lineTo(padL + plotW, py);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.textAlign = 'right';
        ctx.fillText(`${d}`, padL - 6, py + 3);
      }

      ctx.textAlign = 'left';
      ctx.fillText('Concentration (mg/L)', padL, padT - 12);

      // Critical fish survival threshold (4.0 mg/L)
      const yCritFish = padT + plotH - (4.0 / 10) * plotH;
      ctx.strokeStyle = 'rgba(239, 68, 68, 0.4)';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(padL, yCritFish);
      ctx.lineTo(padL + plotW, yCritFish);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = 'rgba(239, 68, 68, 0.8)';
      ctx.textAlign = 'right';
      ctx.fillText('Fish Mortality Line (4.0 mg/L)', padL + plotW - 6, yCritFish - 4);

      // DO Saturation line (9.0 mg/L)
      const ySat = padT + plotH - (DO_sat / 10) * plotH;
      ctx.strokeStyle = '#58a6ff';
      ctx.setLineDash([2, 2]);
      ctx.beginPath();
      ctx.moveTo(padL, ySat);
      ctx.lineTo(padL + plotW, ySat);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = '#58a6ff';
      ctx.fillText('DO Saturation (9.0 mg/L)', padL + plotW - 6, ySat - 4);

      // Plot Remaining BOD Curve: L(t) = L0 · e^(-kd t)
      ctx.strokeStyle = '#f85149';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let xDist = 0; xDist <= maxDist; xDist += 1) {
        const t = xDist / vel;
        const BOD = L0 * Math.exp(-kd * t);
        const px = padL + (xDist / maxDist) * plotW;
        const py = padT + plotH - Math.min(plotH, (BOD / 40) * plotH); // scaled
        if (xDist === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Plot Dissolved Oxygen Sag Curve DO(t) = DO_sat - D(t)
      ctx.strokeStyle = '#38ef7d';
      ctx.lineWidth = 3.5;
      ctx.beginPath();
      for (let xDist = 0; xDist <= maxDist; xDist += 0.5) {
        const t = xDist / vel;
        let Def = 0;
        if (Math.abs(kr - kd) > 0.001) {
          Def = (kd * L0 / (kr - kd)) * (Math.exp(-kd * t) - Math.exp(-kr * t)) + D0 * Math.exp(-kr * t);
        } else {
          Def = (kd * L0 * t + D0) * Math.exp(-kd * t);
        }
        const DO_val = Math.max(0, DO_sat - Def);
        const px = padL + (xDist / maxDist) * plotW;
        const py = padT + plotH - (DO_val / 10) * plotH;
        if (xDist === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Critical Point Marker (xc, minDO)
      if (xc <= maxDist) {
        const pxc = padL + (xc / maxDist) * plotW;
        const pyc = padT + plotH - (minDO / 10) * plotH;
        ctx.fillStyle = '#f85149';
        ctx.beginPath();
        ctx.arc(pxc, pyc, 6, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = '#fff';
        ctx.font = 'bold 11px system-ui';
        ctx.textAlign = 'center';
        ctx.fillText(`Sag Minimum: ${minDO.toFixed(2)} mg/L`, pxc, pyc - 10);
      }

      // Animated Water Flow Waves
      wavePhase += 0.04;
      ctx.fillStyle = 'rgba(56, 189, 248, 0.08)';
      ctx.beginPath();
      ctx.moveTo(padL, padT + plotH);
      for (let px = padL; px <= padL + plotW; px += 10) {
        const wy = padT + plotH - 12 + Math.sin((px * 0.03) + wavePhase) * 6;
        ctx.lineTo(px, wy);
      }
      ctx.lineTo(padL + plotW, padT + plotH);
      ctx.closePath();
      ctx.fill();

      // Curve Legend
      ctx.fillStyle = '#38ef7d';
      ctx.textAlign = 'left';
      ctx.font = '11px system-ui';
      ctx.fillText('— Dissolved Oxygen DO(x)', padL + 10, padT + 18);
      ctx.fillStyle = '#f85149';
      ctx.fillText('— Residual BOD Load L(x)', padL + 10, padT + 34);

      animId = requestAnimationFrame(render);
    }

    [bodS, krS, kdS, velS].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 5: Groundwater Arsenic Speciation & Pourbaix Diagram
     ========================================================================== */
  function sim_env_groundwater_arsenic_speciation(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div style="background:#0d1117; border:1px solid #30363d; border-radius:8px; padding:16px; color:#c9d1d9; font-family:system-ui,-apple-system,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:16px;">Groundwater Arsenic Speciation & Pourbaix (Eh–pH) Diagram</h4>
            <div style="font-size:12px; color:#8b949e;">Thermodynamic Stability Fields: As(III) vs As(V) & Fe(III) Reductive Dissolution Boundary</div>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Aquifer pH: <span id="as_ph_val" style="color:#58a6ff; font-weight:600;">7.20</span></label>
            <input type="range" id="as_ph" min="2.0" max="12.0" value="7.20" step="0.1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Redox Potential Eh (mV): <span id="as_eh_val" style="color:#f85149; font-weight:600;">-50</span></label>
            <input type="range" id="as_eh" min="-400" max="800" value="-50" step="10" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Dissolved Fe²⁺ (mg/L): <span id="as_fe_val" style="color:#e3b341; font-weight:600;">6.5</span></label>
            <input type="range" id="as_fe" min="0.1" max="20.0" value="6.5" step="0.5" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Phosphate PO4³⁻ (mg/L): <span id="as_po4_val" style="color:#a371f7; font-weight:600;">1.8</span></label>
            <input type="range" id="as_po4" min="0.0" max="5.0" value="1.8" step="0.2" style="width:100%;">
          </div>
        </div>
        <canvas class="sim-canvas" style="width:100%; height:320px; background:#040d1a; border-radius:6px; display:block;"></canvas>
        <div style="display:flex; justify-content:space-around; margin-top:8px; font-size:12px; border-top:1px solid #21262d; padding-top:8px;">
          <div>Dominant Arsenic Form: <span id="m_as_dom" style="font-weight:600; color:#f85149;">--</span></div>
          <div>As(III) / As(V) Ratio: <span id="m_as_ratio" style="font-weight:600; color:#e3b341;">--</span></div>
          <div>Mobility Index: <span id="m_as_mob" style="font-weight:600; color:#38ef7d;">--</span></div>
          <div>Iron State: <span id="m_fe_state" style="font-weight:600; color:#58a6ff;">--</span></div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const phS = el.querySelector('#as_ph');
    const ehS = el.querySelector('#as_eh');
    const feS = el.querySelector('#as_fe');
    const po4S = el.querySelector('#as_po4');

    let animId = null;

    function render() {
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      if (!canvas.isConnected) return;

      const pH = parseFloat(phS.value);
      const Eh = parseFloat(ehS.value); // in mV
      const Fe = parseFloat(feS.value);
      const PO4 = parseFloat(po4S.value);

      el.querySelector('#as_ph_val').textContent = pH.toFixed(2);
      el.querySelector('#as_eh_val').textContent = Eh;
      el.querySelector('#as_fe_val').textContent = Fe.toFixed(1);
      el.querySelector('#as_po4_val').textContent = PO4.toFixed(1);

      // Compute Speciation
      // As(V)/As(III) boundary at pH: Eh_eq = 658 - 88.74 * pH (mV)
      const Eh_eq = 658 - 88.74 * pH;
      const dEh = Eh - Eh_eq;
      const as3_as5_ratio = Math.pow(10, -dEh / 29.58);

      let domSpecies = '';
      if (Eh > Eh_eq) {
        if (pH < 2.22) domSpecies = 'H3AsO4 (aq)';
        else if (pH < 6.98) domSpecies = 'H2AsO4⁻ (aq)';
        else if (pH < 11.53) domSpecies = 'HAsO4²⁻ (aq)';
        else domSpecies = 'AsO4³⁻ (aq)';
      } else {
        if (pH < 9.22) domSpecies = 'H3AsO3⁰ (Neutral)';
        else domSpecies = 'H2AsO3⁻ (aq)';
      }

      // Iron boundary: Fe(OH)3 / Fe2+ boundary at Eh ~ 1060 - 177 * pH
      const Fe_eq = 1060 - 177 * pH;
      const feState = Eh < Fe_eq ? 'Fe²⁺ (Dissolved Soluble)' : 'Fe(OH)3 (Precipitated Solid)';

      const isMobile = (Eh < Eh_eq) || (PO4 > 1.5) || (Eh < Fe_eq);
      const mobStatus = isMobile ? 'EXTREME MOBILITY (AQUIFER CONTAMINATION)' : 'LOW (IMMOBILIZED ON OXYHYDROXIDES)';

      el.querySelector('#m_as_dom').textContent = domSpecies;
      el.querySelector('#m_as_ratio').textContent = as3_as5_ratio > 1000 ? '>1000 : 1' : as3_as5_ratio < 0.001 ? '<1 : 1000' : as3_as5_ratio.toFixed(2);
      el.querySelector('#m_as_mob').textContent = mobStatus;
      el.querySelector('#m_as_mob').style.color = isMobile ? '#f85149' : '#38ef7d';
      el.querySelector('#m_fe_state').textContent = feState;

      ctx.clearRect(0, 0, width, height);

      // Left 60%: Pourbaix Diagram (pH 2 - 12 vs Eh -400 to +800 mV)
      // Right 40%: Chemical Speciation Pie / Bar Chart
      const leftW = width * 0.60;
      const rightX = leftW + 20;
      const rightW = width - rightX - 10;

      const padL = 45, padR = 20, padT = 30, padB = 40;
      const plotW = leftW - padL - padR;
      const plotH = height - padT - padB;

      // Draw Pourbaix Diagram Boundaries
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      ctx.strokeRect(padL, padT, plotW, plotH);

      // Y-axis: Eh -400 to +800 mV
      ctx.fillStyle = '#8b949e';
      ctx.font = '10px system-ui';
      ctx.textAlign = 'right';
      for (let eh = -400; eh <= 800; eh += 200) {
        const py = padT + plotH - ((eh - (-400)) / 1200) * plotH;
        ctx.fillText(`${eh}`, padL - 6, py + 3);
        ctx.beginPath();
        ctx.moveTo(padL, py);
        ctx.lineTo(padL + plotW, py);
        ctx.stroke();
      }

      // X-axis: pH 2 to 12
      ctx.textAlign = 'center';
      for (let ph = 2; ph <= 12; ph += 2) {
        const px = padL + ((ph - 2) / 10) * plotW;
        ctx.fillText(`${ph}`, px, padT + plotH + 16);
        ctx.beginPath();
        ctx.moveTo(px, padT);
        ctx.lineTo(px, padT + plotH);
        ctx.stroke();
      }

      ctx.textAlign = 'left';
      ctx.fillText('Eh (mV)', padL, padT - 12);
      ctx.textAlign = 'center';
      ctx.fillText('pH', padL + plotW * 0.5, padT + plotH + 28);

      // Draw As(V) / As(III) Boundary: Eh = 658 - 88.74 * pH
      ctx.strokeStyle = '#f85149';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let p = 2; p <= 12; p += 0.5) {
        const e = 658 - 88.74 * p;
        const px = padL + ((p - 2) / 10) * plotW;
        const py = padT + plotH - ((e - (-400)) / 1200) * plotH;
        if (p === 2) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Draw Fe(III) Reductive Dissolution Line: Eh = 1060 - 177 * pH
      ctx.strokeStyle = '#58a6ff';
      ctx.setLineDash([4, 4]);
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let p = 2; p <= 12; p += 0.5) {
        const e = 1060 - 177 * p;
        const px = padL + ((p - 2) / 10) * plotW;
        const py = padT + plotH - ((e - (-400)) / 1200) * plotH;
        if (p === 2) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Phase labels on diagram
      ctx.fillStyle = 'rgba(248, 81, 73, 0.7)';
      ctx.font = 'bold 12px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText('As(V) Field (H2AsO4⁻ / HAsO4²⁻)', padL + plotW * 0.4, padT + 40);
      ctx.fillStyle = 'rgba(56, 239, 125, 0.7)';
      ctx.fillText('As(III) Field (H3AsO3⁰ - Mobile)', padL + plotW * 0.6, padT + plotH - 30);

      // Current Operational Groundwater Condition Pointer
      const curX = padL + ((pH - 2) / 10) * plotW;
      const curY = padT + plotH - ((Eh - (-400)) / 1200) * plotH;

      ctx.fillStyle = '#e3b341';
      ctx.beginPath();
      ctx.arc(curX, curY, 7, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Right Panel: Speciation Percentages & Groundwater Risk Meter
      ctx.fillStyle = '#c9d1d9';
      ctx.font = 'bold 12px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText('Species Distribution', rightX + rightW * 0.5, padT + 10);

      const fAs3 = as3_as5_ratio / (1 + as3_as5_ratio);
      const fAs5 = 1 - fAs3;

      // Bar Chart for As(III) vs As(V)
      const bY = padT + 35;
      const bH = 26;
      ctx.fillStyle = '#161b22';
      ctx.fillRect(rightX, bY, rightW, bH);
      ctx.fillStyle = '#38ef7d';
      ctx.fillRect(rightX, bY, rightW * fAs3, bH);
      ctx.fillStyle = '#f85149';
      ctx.fillRect(rightX + rightW * fAs3, bY, rightW * fAs5, bH);

      ctx.fillStyle = '#f0f6fc';
      ctx.font = 'bold 10px system-ui';
      ctx.textAlign = 'left';
      ctx.fillText(`As(III): ${(fAs3 * 100).toFixed(1)}%`, rightX + 6, bY + 17);
      ctx.textAlign = 'right';
      ctx.fillText(`As(V): ${(fAs5 * 100).toFixed(1)}%`, rightX + rightW - 6, bY + 17);

      // Risk Warning Box
      ctx.fillStyle = '#161b22';
      ctx.fillRect(rightX, padT + 80, rightW, height - padT - 95);
      ctx.strokeStyle = isMobile ? '#f85149' : '#30363d';
      ctx.strokeRect(rightX, padT + 80, rightW, height - padT - 95);

      ctx.fillStyle = isMobile ? '#f85149' : '#38ef7d';
      ctx.font = 'bold 12px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText(isMobile ? '⚠️ HIGH MOBILITY' : '✅ LOW MOBILITY', rightX + rightW * 0.5, padT + 110);

      ctx.fillStyle = '#8b949e';
      ctx.font = '10px system-ui';
      ctx.textAlign = 'left';
      const lines = [
        `• Ferrihydrite Dissolution: ${Eh < Fe_eq ? 'YES' : 'NO'}`,
        `• Phosphate Competition: ${PO4 > 1.0 ? 'SEVERE' : 'MODERATE'}`,
        `• Neutral H3AsO3 Dominance: ${(fAs3 * 100).toFixed(0)}%`,
        `• Bengal Aquifer Analogy:`,
        isMobile ? ' Holocene grey sand' : ' Pleistocene brown sand'
      ];
      lines.forEach((l, idx) => {
        ctx.fillText(l, rightX + 10, padT + 135 + idx * 16);
      });

      animId = requestAnimationFrame(render);
    }

    [phS, ehS, feS, po4S].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 6: Aquatic Food Web Bioaccumulation & Trophic Transfer
     ========================================================================== */
  function sim_env_pesticide_bioaccumulation_foodweb(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div style="background:#0d1117; border:1px solid #30363d; border-radius:8px; padding:16px; color:#c9d1d9; font-family:system-ui,-apple-system,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:16px;">Aquatic Food Web Bioaccumulation & Biomagnification Simulator</h4>
            <div style="font-size:12px; color:#8b949e;">4-Trophic Level Transfer: Phytoplankton (TL1) → Zooplankton (TL2) → Forage Fish (TL3) → Osprey/Tuna (TL4)</div>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Pesticide Lipophilicity log Kow: <span id="bio_kow_val" style="color:#f85149; font-weight:600;">5.8</span></label>
            <input type="range" id="bio_kow" min="1.0" max="8.0" value="5.8" step="0.1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Ambient Water Cw (μg/L): <span id="bio_cw_val" style="color:#58a6ff; font-weight:600;">0.050</span></label>
            <input type="range" id="bio_cw" min="0.005" max="0.500" value="0.050" step="0.005" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Metabolic Depuration Rate k2: <span id="bio_k2_val" style="color:#e3b341; font-weight:600;">0.003 day⁻¹</span></label>
            <input type="range" id="bio_k2" min="0.001" max="0.050" value="0.003" step="0.001" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Prey Assimilation Efficiency α: <span id="bio_alpha_val" style="color:#38ef7d; font-weight:600;">0.80</span></label>
            <input type="range" id="bio_alpha" min="0.30" max="0.95" value="0.80" step="0.05" style="width:100%;">
          </div>
        </div>
        <canvas class="sim-canvas" style="width:100%; height:320px; background:#040d1a; border-radius:6px; display:block;"></canvas>
        <div style="display:flex; justify-content:space-around; margin-top:8px; font-size:12px; border-top:1px solid #21262d; padding-top:8px;">
          <div>Bioconcentration BCF: <span id="m_bcf" style="font-weight:600; color:#58a6ff;">--</span> L/kg</div>
          <div>Bioaccumulation BAF: <span id="m_baf" style="font-weight:600; color:#38ef7d;">--</span> L/kg</div>
          <div>Apex Predator C4: <span id="m_c4" style="font-weight:600; color:#f85149;">--</span> mg/kg</div>
          <div>Trophic Factor TMF: <span id="m_tmf" style="font-weight:600; color:#e3b341;">--</span></div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const kowS = el.querySelector('#bio_kow');
    const cwS = el.querySelector('#bio_cw');
    const k2S = el.querySelector('#bio_k2');
    const alphaS = el.querySelector('#bio_alpha');

    let animId = null;

    function render() {
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      if (!canvas.isConnected) return;

      const logKow = parseFloat(kowS.value);
      const Cw = parseFloat(cwS.value); // ug/L
      const k2 = parseFloat(k2S.value);
      const alpha = parseFloat(alphaS.value);

      el.querySelector('#bio_kow_val').textContent = logKow.toFixed(1);
      el.querySelector('#bio_cw_val').textContent = Cw.toFixed(3);
      el.querySelector('#bio_k2_val').textContent = k2.toFixed(3) + ' day⁻¹';
      el.querySelector('#bio_alpha_val').textContent = alpha.toFixed(2);

      // Model Concentrations across 4 Trophic Levels
      // TL1: Phytoplankton: C1 = BCF * Cw = (10^(0.85*logKow - 0.70)) * Cw
      const BCF = Math.min(2e6, Math.pow(10, 0.85 * logKow - 0.70));
      const C1_mg = (BCF * (Cw * 1e-3)); // mg/kg

      // TL2: Zooplankton: Feeding + gill absorption
      const BMF1_2 = Math.max(1.1, (alpha * 0.08) / (k2 + 0.01) * 0.4);
      const C2_mg = C1_mg * BMF1_2;

      // TL3: Forage Fish
      const BMF2_3 = Math.max(1.2, (alpha * 0.05) / (k2 + 0.005) * 0.45);
      const C3_mg = C2_mg * BMF2_3;

      // TL4: Apex Piscivore
      const BMF3_4 = Math.max(1.5, (alpha * 0.03) / (k2 + 0.002) * 0.5);
      const C4_mg = C3_mg * BMF3_4;

      const BAF = (C4_mg / (Cw * 1e-3));
      const TMF = Math.pow(C4_mg / C1_mg, 1 / 3);

      el.querySelector('#m_bcf').textContent = BCF > 1e5 ? BCF.toExponential(2) : Math.round(BCF);
      el.querySelector('#m_baf').textContent = BAF > 1e5 ? BAF.toExponential(2) : Math.round(BAF);
      el.querySelector('#m_c4').textContent = C4_mg.toFixed(2);
      el.querySelector('#m_tmf').textContent = TMF.toFixed(2);

      ctx.clearRect(0, 0, width, height);

      // Trophic Pyramid Display
      const levels = [
        { name: 'TL4: Apex Piscivore / Osprey', val: C4_mg, color: '#f85149', y: 40, wRatio: 0.35 },
        { name: 'TL3: Forage Fish (Teleost)', val: C3_mg, color: '#e3b341', y: 105, wRatio: 0.55 },
        { name: 'TL2: Herbivorous Zooplankton', val: C2_mg, color: '#58a6ff', y: 170, wRatio: 0.75 },
        { name: 'TL1: Primary Producer (Phytoplankton)', val: C1_mg, color: '#38ef7d', y: 235, wRatio: 0.95 }
      ];

      const cX = width * 0.5;

      levels.forEach((lvl, idx) => {
        const bW = (width - 60) * lvl.wRatio;
        const bX = cX - bW * 0.5;
        const bH = 50;

        // Block background
        ctx.fillStyle = '#161b22';
        ctx.fillRect(bX, lvl.y, bW, bH);
        ctx.strokeStyle = lvl.color;
        ctx.lineWidth = 2;
        ctx.strokeRect(bX, lvl.y, bW, bH);

        // Progress bar inside based on concentration log scale
        const logVal = Math.max(0, Math.log10(lvl.val + 0.01) + 2); // 0 to 6
        const fillW = Math.min(bW, (logVal / 6) * bW);
        ctx.fillStyle = lvl.color + '33';
        ctx.fillRect(bX, lvl.y, fillW, bH);

        // Text
        ctx.fillStyle = '#f0f6fc';
        ctx.font = 'bold 12px system-ui';
        ctx.textAlign = 'left';
        ctx.fillText(lvl.name, bX + 12, lvl.y + 22);

        ctx.fillStyle = lvl.color;
        ctx.font = 'bold 13px system-ui';
        ctx.textAlign = 'right';
        ctx.fillText(`${lvl.val.toFixed(2)} mg/kg`, bX + bW - 12, lvl.y + 22);

        // Subtitle
        ctx.fillStyle = '#8b949e';
        ctx.font = '10px system-ui';
        ctx.textAlign = 'left';
        ctx.fillText(`Bio-enrichment factor: ×${(lvl.val / (Cw * 1e-3)).toFixed(0)} relative to water`, bX + 12, lvl.y + 40);

        // Upward trophic flow arrow
        if (idx < 3) {
          ctx.strokeStyle = '#a371f7';
          ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.moveTo(cX, lvl.y + bH);
          ctx.lineTo(cX, lvl.y + bH + 15);
          ctx.stroke();
        }
      });

      // Water background at very bottom
      ctx.fillStyle = '#38bdf8';
      ctx.font = '11px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText(`Ambient Lake / River Water: Cw = ${Cw.toFixed(3)} μg/L (${(Cw * 1e-3).toFixed(5)} mg/L)`, cX, height - 12);

      animId = requestAnimationFrame(render);
    }

    [kowS, cwS, k2S, alphaS].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 7: Soil Cation Exchange Capacity & Diffuse Double Layer
     ========================================================================== */
  function sim_env_soil_cation_exchange_cec(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div style="background:#0d1117; border:1px solid #30363d; border-radius:8px; padding:16px; color:#c9d1d9; font-family:system-ui,-apple-system,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:16px;">Soil Cation Exchange Capacity (CEC) & Gouy-Chapman DDL</h4>
            <div style="font-size:12px; color:#8b949e;">Clay Platelet Surface Potential, Debye Screening Length κ⁻¹ & Lyotropic Exchange: Al³⁺ > Ca²⁺ > Mg²⁺ > K⁺ > Na⁺</div>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Clay Phyllosilicate Type: <span id="cec_clay_val" style="color:#58a6ff; font-weight:600;">Smectite (2:1)</span></label>
            <select id="cec_clay" style="width:100%; background:#21262d; border:1px solid #30363d; color:#c9d1d9; border-radius:4px; padding:4px;">
              <option value="smectite" selected>Smectite / Montmorillonite (CEC: 100)</option>
              <option value="illite">Illite (CEC: 30)</option>
              <option value="kaolinite">Kaolinite (1:1) (CEC: 8)</option>
            </select>
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Soil Solution Ionic Strength I (M): <span id="cec_i_val" style="color:#f85149; font-weight:600;">0.010</span></label>
            <input type="range" id="cec_i" min="0.001" max="0.100" value="0.010" step="0.002" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Soil pH: <span id="cec_ph_val" style="color:#e3b341; font-weight:600;">5.50</span></label>
            <input type="range" id="cec_ph" min="3.5" max="8.5" value="5.50" step="0.1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Agricultural Lime Dosing (tons/ha): <span id="cec_lime_val" style="color:#38ef7d; font-weight:600;">0.0</span></label>
            <input type="range" id="cec_lime" min="0.0" max="8.0" value="0.0" step="0.5" style="width:100%;">
          </div>
        </div>
        <canvas class="sim-canvas" style="width:100%; height:320px; background:#040d1a; border-radius:6px; display:block;"></canvas>
        <div style="display:flex; justify-content:space-around; margin-top:8px; font-size:12px; border-top:1px solid #21262d; padding-top:8px;">
          <div>Debye Length κ⁻¹: <span id="m_debye" style="font-weight:600; color:#58a6ff;">--</span> nm</div>
          <div>Base Saturation BS%: <span id="m_bs" style="font-weight:600; color:#38ef7d;">--</span> %</div>
          <div>Exchangeable Al³⁺: <span id="m_al" style="font-weight:600; color:#f85149;">--</span> cmol_c/kg</div>
          <div>Flocculation State: <span id="m_floc" style="font-weight:600; color:#e3b341;">--</span></div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const clayS = el.querySelector('#cec_clay');
    const iS = el.querySelector('#cec_i');
    const phS = el.querySelector('#cec_ph');
    const limeS = el.querySelector('#cec_lime');

    let animId = null;

    function render() {
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      if (!canvas.isConnected) return;

      const clay = clayS.value;
      const I = parseFloat(iS.value);
      const pH_base = parseFloat(phS.value);
      const lime = parseFloat(limeS.value);

      // Lime shifts pH upwards
      const pH = Math.min(8.5, pH_base + lime * 0.45);
      el.querySelector('#cec_i_val').textContent = I.toFixed(3);
      el.querySelector('#cec_ph_val').textContent = pH.toFixed(2);
      el.querySelector('#cec_lime_val').textContent = lime.toFixed(1);

      // Debye length kappa^-1 (nm) = 0.304 / sqrt(I)
      const debye = 0.304 / Math.sqrt(I);

      let baseCEC = 100.0;
      let sigma0 = -0.120; // C/m2
      if (clay === 'illite') { baseCEC = 30.0; sigma0 = -0.060; }
      if (clay === 'kaolinite') { baseCEC = 8.0; sigma0 = -0.015; }

      // Cation fractions: Acidic (Al3+, H+) vs Basic (Ca2+, Mg2+, K+, Na+)
      const acidFrac = Math.max(0.02, Math.min(0.85, (7.0 - pH) * 0.22));
      const al_cmol = baseCEC * acidFrac;
      const base_cmol = baseCEC * (1 - acidFrac);
      const BS = (base_cmol / baseCEC) * 100;

      const flocState = (debye < 2.0 || acidFrac > 0.4 || lime > 2.0) ? 'Flocculated (Aggregated)' : 'Dispersed (Suspended)';

      el.querySelector('#m_debye').textContent = debye.toFixed(2);
      el.querySelector('#m_bs').textContent = BS.toFixed(1);
      el.querySelector('#m_al').textContent = al_cmol.toFixed(1);
      el.querySelector('#m_floc').textContent = flocState;
      el.querySelector('#m_floc').style.color = flocState.includes('Flocculated') ? '#38ef7d' : '#f85149';

      ctx.clearRect(0, 0, width, height);

      // Left 50%: Clay Platelet and Diffuse Double Layer Potential Decay Curve
      // Right 50%: Exchange Complex Cation Breakdown & Lime Titration
      const leftW = width * 0.52;
      const rightX = leftW + 20;
      const rightW = width - rightX - 10;

      const padL = 60, padT = 30, padB = 40;
      const plotW = leftW - padL - 10;
      const plotH = height - padT - padB;

      // Clay Platelet solid at x = 0
      ctx.fillStyle = '#8b5a2b';
      ctx.fillRect(padL - 18, padT, 18, plotH);
      ctx.fillStyle = '#f0f6fc';
      ctx.font = 'bold 10px system-ui';
      ctx.save();
      ctx.translate(padL - 6, padT + plotH * 0.5);
      ctx.rotate(-Math.PI * 0.5);
      ctx.textAlign = 'center';
      ctx.fillText(`Clay Platelet (σ₀ = ${sigma0} C/m²)`, 0, 0);
      ctx.restore();

      // Negative charge symbols along clay wall
      ctx.fillStyle = '#f85149';
      for (let y = padT + 15; y <= padT + plotH - 10; y += 22) {
        ctx.fillText('⊖', padL - 14, y);
      }

      // Potential Decay Axes: Distance x (0 to 12 nm) vs Potential psi (0 to -160 mV)
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      ctx.strokeRect(padL, padT, plotW, plotH);

      ctx.fillStyle = '#8b949e';
      ctx.font = '10px system-ui';
      ctx.textAlign = 'right';
      for (let psi = 0; psi >= -160; psi -= 40) {
        const py = padT + (Math.abs(psi) / 160) * plotH;
        ctx.fillText(`${psi} mV`, padL - 6, py + 3);
        ctx.beginPath();
        ctx.moveTo(padL, py);
        ctx.lineTo(padL + plotW, py);
        ctx.stroke();
      }

      ctx.textAlign = 'center';
      for (let x = 0; x <= 12; x += 3) {
        const px = padL + (x / 12) * plotW;
        ctx.fillText(`${x} nm`, px, padT + plotH + 16);
      }
      ctx.fillText('Distance from Clay Surface x (nm)', padL + plotW * 0.5, padT + plotH + 28);

      // Plot Potential Decay: psi(x) = psi0 * exp(-kappa * x)
      const psi0 = sigma0 * 1200; // approx mV
      ctx.strokeStyle = '#58a6ff';
      ctx.lineWidth = 3;
      ctx.beginPath();
      for (let x = 0; x <= 12; x += 0.2) {
        const px = padL + (x / 12) * plotW;
        const psi = psi0 * Math.exp(-x / debye);
        const py = padT + (Math.abs(psi) / 160) * plotH;
        if (x === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Debye length vertical marker
      const debyeX = padL + (debye / 12) * plotW;
      if (debyeX <= padL + plotW) {
        ctx.strokeStyle = '#38ef7d';
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(debyeX, padT);
        ctx.lineTo(debyeX, padT + plotH);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = '#38ef7d';
        ctx.textAlign = 'center';
        ctx.fillText(`κ⁻¹ = ${debye.toFixed(1)} nm`, debyeX, padT + 14);
      }

      // Right Panel: Exchange Complex Composition Bar
      ctx.fillStyle = '#c9d1d9';
      ctx.font = 'bold 12px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText(`Exchange Complex (${baseCEC} cmol_c/kg)`, rightX + rightW * 0.5, padT + 10);

      const cations = [
        { name: 'Ca²⁺ (Dominant base)', pct: (1 - acidFrac) * 0.65, color: '#38ef7d' },
        { name: 'Mg²⁺ (Basic cation)', pct: (1 - acidFrac) * 0.20, color: '#22c55e' },
        { name: 'K⁺ / Na⁺ (Monovalents)', pct: (1 - acidFrac) * 0.15, color: '#58a6ff' },
        { name: 'Al³⁺ (Acidic toxic)', pct: acidFrac * 0.85, color: '#f85149' },
        { name: 'H⁺ (Protons)', pct: acidFrac * 0.15, color: '#e3b341' }
      ];

      let curY = padT + 30;
      cations.forEach(cat => {
        const bH = 22;
        const bW = (cat.pct) * rightW;

        ctx.fillStyle = '#161b22';
        ctx.fillRect(rightX, curY, rightW, bH);
        ctx.fillStyle = cat.color;
        ctx.fillRect(rightX, curY, bW, bH);

        ctx.fillStyle = '#f0f6fc';
        ctx.font = '10px system-ui';
        ctx.textAlign = 'left';
        ctx.fillText(cat.name, rightX + 6, curY + 15);
        ctx.textAlign = 'right';
        ctx.fillText(`${(cat.pct * baseCEC).toFixed(1)} (${(cat.pct * 100).toFixed(0)}%)`, rightX + rightW - 6, curY + 15);

        curY += bH + 8;
      });

      // Agronomic Lime Recommendation Box
      ctx.fillStyle = '#161b22';
      ctx.fillRect(rightX, curY + 10, rightW, height - curY - 20);
      ctx.strokeStyle = BS < 60 ? '#f85149' : '#38ef7d';
      ctx.strokeRect(rightX, curY + 10, rightW, height - curY - 20);

      ctx.fillStyle = BS < 60 ? '#f85149' : '#38ef7d';
      ctx.font = 'bold 11px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText(BS < 60 ? '⚠️ LIME REQUIRED (Al³⁺ TOXICITY)' : '✅ FERTILE BASE SATURATION', rightX + rightW * 0.5, curY + 30);

      ctx.fillStyle = '#8b949e';
      ctx.font = '10px system-ui';
      ctx.fillText(`Kamprath Lime Need: ${(al_cmol * 1.5 * 0.5).toFixed(1)} tons CaCO3/ha`, rightX + rightW * 0.5, curY + 48);

      animId = requestAnimationFrame(render);
    }

    [clayS, iS, phS, limeS].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 8: Activated Sludge Bioreactor & Clarifier Simulator
     ========================================================================== */
  function sim_env_activated_sludge_effluent_treatment(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div style="background:#0d1117; border:1px solid #30363d; border-radius:8px; padding:16px; color:#c9d1d9; font-family:system-ui,-apple-system,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:16px;">Activated Sludge Bioreactor & Clarifier (ETP) Simulator</h4>
            <div style="font-size:12px; color:#8b949e;">Continuous Lawrence-McCarty Kinetics: Substrate S(θc), F/M Ratio, MLVSS & Secondary Clarifier Blanket</div>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Influent BOD S0 (mg/L): <span id="as_s0_val" style="color:#f85149; font-weight:600;">850</span></label>
            <input type="range" id="as_s0" min="200" max="2500" value="850" step="50" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Sludge Age θc (MCRT days): <span id="as_mcrt_val" style="color:#58a6ff; font-weight:600;">7.0</span></label>
            <input type="range" id="as_mcrt" min="1.0" max="20.0" value="7.0" step="0.5" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Hydraulic Retention θ (hrs): <span id="as_hrt_val" style="color:#e3b341; font-weight:600;">16.0</span></label>
            <input type="range" id="as_hrt" min="4.0" max="36.0" value="16.0" step="1.0" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Aeration DO (mg/L): <span id="as_do_val" style="color:#38ef7d; font-weight:600;">2.5</span></label>
            <input type="range" id="as_do" min="0.5" max="6.0" value="2.5" step="0.5" style="width:100%;">
          </div>
        </div>
        <canvas class="sim-canvas" style="width:100%; height:320px; background:#040d1a; border-radius:6px; display:block;"></canvas>
        <div style="display:flex; justify-content:space-around; margin-top:8px; font-size:12px; border-top:1px solid #21262d; padding-top:8px;">
          <div>Effluent BOD S: <span id="m_eff_bod" style="font-weight:600; color:#38ef7d;">--</span> mg/L</div>
          <div>Biomass MLVSS X: <span id="m_mlvss" style="font-weight:600; color:#58a6ff;">--</span> mg/L</div>
          <div>F/M Ratio: <span id="m_fm" style="font-weight:600; color:#e3b341;">--</span> day⁻¹</div>
          <div>Sludge SVI / Bulking: <span id="m_svi" style="font-weight:600; color:#f85149;">--</span></div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const s0S = el.querySelector('#as_s0');
    const mcrtS = el.querySelector('#as_mcrt');
    const hrtS = el.querySelector('#as_hrt');
    const doS = el.querySelector('#as_do');

    let animId = null;
    let bubblePhase = 0;

    function render() {
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      if (!canvas.isConnected) return;

      const S0 = parseFloat(s0S.value);
      const theta_c = parseFloat(mcrtS.value);
      const HRT_h = parseFloat(hrtS.value);
      const DO = parseFloat(doS.value);

      el.querySelector('#as_s0_val').textContent = S0;
      el.querySelector('#as_mcrt_val').textContent = theta_c.toFixed(1);
      el.querySelector('#as_hrt_val').textContent = HRT_h.toFixed(1);
      el.querySelector('#as_do_val').textContent = DO.toFixed(1);

      // Lawrence-McCarty Parameters
      const Y = 0.50; // g VSS/g BOD
      const k = 4.0;  // day^-1
      const Ks = 60.0;// mg/L
      const b = 0.06; // day^-1

      // S = Ks (1 + b theta_c) / [theta_c (Y k - b) - 1]
      const denom = theta_c * (Y * k - b) - 1;
      let S = 0;
      if (denom > 0) {
        S = (Ks * (1 + b * theta_c)) / denom;
      } else {
        S = S0; // Washout!
      }
      S = Math.min(S0, Math.max(2.0, S));

      // X (MLVSS) = (theta_c / theta) * [ Y (S0 - S) / (1 + b theta_c) ]
      const theta_d = HRT_h / 24.0;
      const X = (theta_c / theta_d) * (Y * (S0 - S) / (1 + b * theta_c));

      // F/M = S0 / (theta_d * X)
      const FM = S0 / (theta_d * X);

      // Bulking assessment based on DO and F/M
      let bulking = 'Normal Settling (SVI < 120)';
      let bulkingColor = '#38ef7d';
      if (DO < 1.0) {
        bulking = 'Low-DO Bulking (SVI > 250)';
        bulkingColor = '#f85149';
      } else if (FM > 0.8) {
        bulking = 'Viscous Bulking / High F/M';
        bulkingColor = '#e3b341';
      } else if (FM < 0.1) {
        bulking = 'Pinpoint Floc / Ashing';
        bulkingColor = '#e3b341';
      }

      el.querySelector('#m_eff_bod').textContent = S.toFixed(1);
      el.querySelector('#m_mlvss').textContent = Math.round(X);
      el.querySelector('#m_fm').textContent = FM.toFixed(2);
      el.querySelector('#m_svi').textContent = bulking;
      el.querySelector('#m_svi').style.color = bulkingColor;

      ctx.clearRect(0, 0, width, height);

      // Drawing Plant Schematic:
      // Left: Aeration Tank (55% width)
      // Right: Secondary Clarifier (40% width)
      const tankW = width * 0.52;
      const tankH = height * 0.70;
      const tankX = 20;
      const tankY = 40;

      // Aeration Tank Container
      ctx.fillStyle = '#161b22';
      ctx.fillRect(tankX, tankY, tankW, tankH);
      ctx.strokeStyle = '#30363d';
      ctx.lineWidth = 2;
      ctx.strokeRect(tankX, tankY, tankW, tankH);

      // Wastewater inside aeration basin
      const fluidGrad = ctx.createLinearGradient(0, tankY, 0, tankY + tankH);
      fluidGrad.addColorStop(0, 'rgba(139, 90, 43, 0.4)');
      fluidGrad.addColorStop(1, 'rgba(101, 67, 33, 0.8)');
      ctx.fillStyle = fluidGrad;
      ctx.fillRect(tankX, tankY + 20, tankW, tankH - 20);

      ctx.fillStyle = '#58a6ff';
      ctx.font = 'bold 12px system-ui';
      ctx.textAlign = 'left';
      ctx.fillText(`Aeration Basin (HRT: ${HRT_h}h)`, tankX + 12, tankY + 14);

      // Air bubbles rising from bottom diffusers
      bubblePhase += 0.05;
      ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
      for (let i = 0; i < 16; i++) {
        const bx = tankX + 25 + (i * (tankW - 50) / 15);
        const byOffset = ((i * 35) + bubblePhase * 40) % (tankH - 30);
        const by = tankY + tankH - byOffset;
        ctx.beginPath();
        ctx.arc(bx + Math.sin(by * 0.1) * 3, by, 2.5, 0, Math.PI * 2);
        ctx.fill();
      }

      // Secondary Clarifier (Right)
      const clarX = tankX + tankW + 30;
      const clarW = width - clarX - 20;
      const clarH = tankH;
      const clarY = tankY;

      // Clarifier Hopper Geometry
      ctx.fillStyle = '#161b22';
      ctx.beginPath();
      ctx.moveTo(clarX, clarY);
      ctx.lineTo(clarX + clarW, clarY);
      ctx.lineTo(clarX + clarW, clarY + clarH * 0.65);
      ctx.lineTo(clarX + clarW * 0.5 + 15, clarY + clarH);
      ctx.lineTo(clarX + clarW * 0.5 - 15, clarY + clarH);
      ctx.lineTo(clarX, clarY + clarH * 0.65);
      ctx.closePath();
      ctx.fill();
      ctx.strokeStyle = '#30363d';
      ctx.stroke();

      // Clear supernatant water top layer
      ctx.fillStyle = 'rgba(56, 239, 125, 0.2)';
      ctx.fillRect(clarX, clarY + 15, clarW, clarH * 0.35);

      // Settled Sludge Blanket in clarifier
      const blanketH = Math.min(clarH * 0.6, clarH * (FM > 0.8 ? 0.55 : 0.35));
      ctx.fillStyle = 'rgba(101, 67, 33, 0.85)';
      ctx.beginPath();
      ctx.moveTo(clarX, clarY + clarH - blanketH);
      ctx.lineTo(clarX + clarW, clarY + clarH - blanketH);
      ctx.lineTo(clarX + clarW * 0.5 + 15, clarY + clarH);
      ctx.lineTo(clarX + clarW * 0.5 - 15, clarY + clarH);
      ctx.closePath();
      ctx.fill();

      ctx.fillStyle = '#38ef7d';
      ctx.font = 'bold 12px system-ui';
      ctx.textAlign = 'left';
      ctx.fillText('Secondary Clarifier', clarX + 8, clarY + 14);

      // Effluent discharge pipe
      ctx.fillStyle = '#38ef7d';
      ctx.font = 'bold 11px system-ui';
      ctx.fillText(`Effluent BOD: ${S.toFixed(1)} mg/L`, clarX + 8, clarY + 36);

      // Connecting pipeline between Aeration and Clarifier
      ctx.strokeStyle = '#8b949e';
      ctx.lineWidth = 6;
      ctx.beginPath();
      ctx.moveTo(tankX + tankW, tankY + 50);
      ctx.lineTo(clarX, tankY + 50);
      ctx.stroke();

      // Return Activated Sludge (RAS) recycled line
      ctx.strokeStyle = '#e3b341';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(clarX + clarW * 0.5, clarY + clarH);
      ctx.lineTo(clarX + clarW * 0.5, height - 25);
      ctx.lineTo(tankX + 40, height - 25);
      ctx.lineTo(tankX + 40, tankY + tankH);
      ctx.stroke();

      ctx.fillStyle = '#e3b341';
      ctx.font = '10px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText('← Return Activated Sludge (RAS Recycle)', (tankX + clarX) * 0.5, height - 12);

      animId = requestAnimationFrame(render);
    }

    [s0S, mcrtS, hrtS, doS].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 9: Sanitary Landfill Methane & Leachate Evolution
     ========================================================================== */
  function sim_env_landfill_methane_leachate(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div style="background:#0d1117; border:1px solid #30363d; border-radius:8px; padding:16px; color:#c9d1d9; font-family:system-ui,-apple-system,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:16px;">Sanitary Landfill Biogas (LandGEM) & Leachate Simulator</h4>
            <div style="font-size:12px; color:#8b949e;">First-Order Methane Decay Q_CH4 = Σ 2 k L0 Mi e^(-k ti) & Hydrologic Percolation L = P - R - ET</div>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Waste Accepted (kilo-tons/yr): <span id="lf_w_val" style="color:#58a6ff; font-weight:600;">150</span></label>
            <input type="range" id="lf_w" min="50" max="500" value="150" step="25" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Decay Constant k (yr⁻¹): <span id="lf_k_val" style="color:#f85149; font-weight:600;">0.050</span></label>
            <input type="range" id="lf_k" min="0.020" max="0.120" value="0.050" step="0.005" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Active Operating Years: <span id="lf_yrs_val" style="color:#e3b341; font-weight:600;">15</span></label>
            <input type="range" id="lf_yrs" min="5" max="30" value="15" step="1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Precipitation P (mm/yr): <span id="lf_p_val" style="color:#38ef7d; font-weight:600;">1800</span></label>
            <input type="range" id="lf_p" min="400" max="3000" value="1800" step="100" style="width:100%;">
          </div>
        </div>
        <canvas class="sim-canvas" style="width:100%; height:320px; background:#040d1a; border-radius:6px; display:block;"></canvas>
        <div style="display:flex; justify-content:space-around; margin-top:8px; font-size:12px; border-top:1px solid #21262d; padding-top:8px;">
          <div>Peak Methane Year: <span id="m_peak_yr" style="font-weight:600; color:#e3b341;">--</span></div>
          <div>Peak Biogas Rate: <span id="m_peak_rate" style="font-weight:600; color:#f85149;">--</span> Mm³/yr</div>
          <div>Leachate Flux: <span id="m_leach_vol" style="font-weight:600; color:#58a6ff;">--</span> m³/day</div>
          <div>Electrical Output: <span id="m_power" style="font-weight:600; color:#38ef7d;">--</span> MW</div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const wS = el.querySelector('#lf_w');
    const kS = el.querySelector('#lf_k');
    const yrsS = el.querySelector('#lf_yrs');
    const pS = el.querySelector('#lf_p');

    let animId = null;

    function render() {
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      if (!canvas.isConnected) return;

      const W_ktons = parseFloat(wS.value);
      const W = W_ktons * 1000; // tons/year
      const k = parseFloat(kS.value);
      const activeYrs = parseInt(yrsS.value, 10);
      const P = parseFloat(pS.value);

      el.querySelector('#lf_w_val').textContent = W_ktons;
      el.querySelector('#lf_k_val').textContent = k.toFixed(3);
      el.querySelector('#lf_yrs_val').textContent = activeYrs;
      el.querySelector('#lf_p_val').textContent = P;

      const L0 = 120.0; // m3 CH4/ton
      const totalSimYrs = 50;

      // Compute Methane Generation curve over 50 years
      const Q = [];
      let maxQ = 0;
      let peakYr = activeYrs;

      for (let y = 0; y <= totalSimYrs; y++) {
        let qYr = 0;
        for (let i = 1; i <= Math.min(y, activeYrs); i++) {
          const age = y - i;
          qYr += 2 * k * L0 * W * Math.exp(-k * age);
        }
        Q.push(qYr);
        if (qYr > maxQ) {
          maxQ = qYr;
          peakYr = y;
        }
      }

      // Leachate water balance: L = P * (1 - 0.15) - 1100 mm/yr
      const netPerc_mm = Math.max(100, P * 0.85 - 1100);
      const landfillArea = 50000; // 5 ha
      const annualLeach_m3 = (netPerc_mm * 1e-3) * landfillArea;
      const dailyLeach_m3 = annualLeach_m3 / 365.25;

      // Electrical output at peak (36 MJ/m3, 38% electrical efficiency)
      const peakM3_yr = maxQ * 0.5; // pure methane
      const energyMJ_yr = peakM3_yr * 36.0 * 0.75; // 75% collection
      const powerMW = (energyMJ_yr * 0.38) / (365.25 * 86400);

      el.querySelector('#m_peak_yr').textContent = `Year ${peakYr}`;
      el.querySelector('#m_peak_rate').textContent = (maxQ * 1e-6).toFixed(2);
      el.querySelector('#m_leach_vol').textContent = dailyLeach_m3.toFixed(1);
      el.querySelector('#m_power').textContent = powerMW.toFixed(2);

      ctx.clearRect(0, 0, width, height);

      // Plot LandGEM Curve (0 to 50 years)
      const padL = 50, padR = 25, padT = 30, padB = 40;
      const plotW = width - padL - padR;
      const plotH = height - padT - padB;

      // Grid
      ctx.strokeStyle = '#21262d';
      ctx.lineWidth = 1;
      for (let y = 0; y <= 50; y += 10) {
        const px = padL + (y / 50) * plotW;
        ctx.beginPath();
        ctx.moveTo(px, padT);
        ctx.lineTo(px, padT + plotH);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.font = '10px system-ui';
        ctx.textAlign = 'center';
        ctx.fillText(`Yr ${y}`, px, padT + plotH + 16);
      }

      const qMaxScale = Math.max(5e6, maxQ * 1.15);
      for (let q = 0; q <= qMaxScale; q += (qMaxScale / 4)) {
        const py = padT + plotH - (q / qMaxScale) * plotH;
        ctx.beginPath();
        ctx.moveTo(padL, py);
        ctx.lineTo(padL + plotW, py);
        ctx.stroke();

        ctx.fillStyle = '#8b949e';
        ctx.textAlign = 'right';
        ctx.fillText(`${(q * 1e-6).toFixed(1)}M`, padL - 6, py + 3);
      }

      ctx.textAlign = 'left';
      ctx.fillText('Biogas Production Rate (m³/yr)', padL, padT - 12);

      // Landfill Active Filling Shaded Region
      const closePx = padL + (activeYrs / 50) * plotW;
      ctx.fillStyle = 'rgba(56, 189, 248, 0.08)';
      ctx.fillRect(padL, padT, closePx - padL, plotH);
      ctx.fillStyle = '#38bdf8';
      ctx.font = '10px system-ui';
      ctx.fillText(`Active Filling (Years 1–${activeYrs})`, padL + 8, padT + 20);

      // Landfill Closure Line
      ctx.strokeStyle = '#e3b341';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(closePx, padT);
      ctx.lineTo(closePx, padT + plotH);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = '#e3b341';
      ctx.fillText('Closure & Final Cover', closePx + 6, padT + 36);

      // Draw Methane Curve
      ctx.strokeStyle = '#f85149';
      ctx.lineWidth = 3.5;
      ctx.beginPath();
      for (let y = 0; y <= 50; y++) {
        const px = padL + (y / 50) * plotW;
        const py = padT + plotH - (Q[y] / qMaxScale) * plotH;
        if (y === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Peak Point Indicator
      const peakX = padL + (peakYr / 50) * plotW;
      const peakY = padT + plotH - (maxQ / qMaxScale) * plotH;
      ctx.fillStyle = '#f85149';
      ctx.beginPath();
      ctx.arc(peakX, peakY, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.fillStyle = '#fff';
      ctx.font = 'bold 11px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText(`Peak: ${(maxQ * 1e-6).toFixed(2)} Mm³/yr`, peakX, peakY - 10);

      animId = requestAnimationFrame(render);
    }

    [wS, kS, yrsS, pS].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  /* ==========================================================================
     SIMULATION 10: Green Chemistry Metrics & 12 Principles Radar Dashboard
     ========================================================================== */
  function sim_env_green_chemistry_metrics(container) {
    const el = getContainerEl(container);
    if (!el) return;
    el.innerHTML = `
      <div style="background:#0d1117; border:1px solid #30363d; border-radius:8px; padding:16px; color:#c9d1d9; font-family:system-ui,-apple-system,sans-serif;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <div>
            <h4 style="margin:0; color:#58a6ff; font-size:16px;">Green Chemistry Metrics & 12 Principles Radar Dashboard</h4>
            <div style="font-size:12px; color:#8b949e;">Quantitative Evaluation: Atom Economy (AE), Sheldon E-Factor, PMI & Anastas-Warner Radar Profile</div>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:12px; background:#161b22; padding:10px; border-radius:6px;">
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Synthetic Strategy: <span id="gc_route_val" style="color:#58a6ff; font-weight:600;">Catalytic Addition</span></label>
            <select id="gc_route" style="width:100%; background:#21262d; border:1px solid #30363d; color:#c9d1d9; border-radius:4px; padding:4px;">
              <option value="addition" selected>Catalytic Addition (Diels-Alder / HPPO)</option>
              <option value="condensation">Condensation / Esterification</option>
              <option value="substitution">Classical Nucleophilic Substitution</option>
              <option value="elimination">Elimination / Wittig Olefination</option>
            </select>
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Reaction Chemical Yield: <span id="gc_yield_val" style="color:#38ef7d; font-weight:600;">88%</span></label>
            <input type="range" id="gc_yield" min="20" max="99" value="88" step="1" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Solvent Recycle Rate: <span id="gc_recycle_val" style="color:#e3b341; font-weight:600;">80%</span></label>
            <input type="range" id="gc_recycle" min="0" max="95" value="80" step="5" style="width:100%;">
          </div>
          <div>
            <label style="font-size:11px; color:#8b949e; display:block;">Renewable Carbon Index: <span id="gc_renew_val" style="color:#a371f7; font-weight:600;">75%</span></label>
            <input type="range" id="gc_renew" min="0" max="100" value="75" step="5" style="width:100%;">
          </div>
        </div>
        <canvas class="sim-canvas" style="width:100%; height:320px; background:#040d1a; border-radius:6px; display:block;"></canvas>
        <div style="display:flex; justify-content:space-around; margin-top:8px; font-size:12px; border-top:1px solid #21262d; padding-top:8px;">
          <div>Atom Economy AE: <span id="m_ae" style="font-weight:600; color:#38ef7d;">--</span> %</div>
          <div>Sheldon E-Factor: <span id="m_efactor" style="font-weight:600; color:#f85149;">--</span> kg/kg</div>
          <div>Process Mass Intensity: <span id="m_pmi" style="font-weight:600; color:#58a6ff;">--</span></div>
          <div>Reaction Mass Eff. (RME): <span id="m_rme" style="font-weight:600; color:#e3b341;">--</span> %</div>
        </div>
      </div>
    `;

    const canvas = el.querySelector('.sim-canvas');
    const routeS = el.querySelector('#gc_route');
    const yieldS = el.querySelector('#gc_yield');
    const recycleS = el.querySelector('#gc_recycle');
    const renewS = el.querySelector('#gc_renew');

    let animId = null;

    function render() {
      const c = initCanvas(canvas);
      if (!c) return;
      const { ctx, width, height } = c;

      if (!canvas.isConnected) return;

      const route = routeS.value;
      const yieldPct = parseFloat(yieldS.value);
      const recyclePct = parseFloat(recycleS.value);
      const renewPct = parseFloat(renewS.value);

      el.querySelector('#gc_yield_val').textContent = yieldPct + '%';
      el.querySelector('#gc_recycle_val').textContent = recyclePct + '%';
      el.querySelector('#gc_renew_val').textContent = renewPct + '%';

      let baseAE = 100.0;
      let baseSolventMass = 8.0; // kg/kg
      if (route === 'condensation') { baseAE = 78.0; baseSolventMass = 12.0; }
      if (route === 'substitution') { baseAE = 52.0; baseSolventMass = 25.0; }
      if (route === 'elimination') { baseAE = 34.0; baseSolventMass = 45.0; }

      // Compute Quantitative Metrics
      const AE = baseAE;
      const RME = (AE * (yieldPct / 100.0) * 0.95); // assuming 5% excess

      const netSolvent = baseSolventMass * (1 - recyclePct / 100.0);
      const wasteReactant = (1 / (RME / 100.0)) - 1.0;
      const E_factor = Math.max(0.1, wasteReactant + netSolvent);
      const PMI = E_factor + 1.0;

      el.querySelector('#m_ae').textContent = AE.toFixed(1);
      el.querySelector('#m_efactor').textContent = E_factor.toFixed(2);
      el.querySelector('#m_pmi').textContent = PMI.toFixed(2);
      el.querySelector('#m_rme').textContent = RME.toFixed(1);

      ctx.clearRect(0, 0, width, height);

      // Left 45%: Green Metric Gauges / KPI Bars
      // Right 55%: 12 Principles Radar Polygon
      const leftW = width * 0.44;
      const rightX = leftW + 20;
      const rightW = width - rightX - 10;

      // KPI Gauges on Left
      const kpis = [
        { label: 'Atom Economy (AE)', val: AE, max: 100, unit: '%', color: '#38ef7d' },
        { label: 'Reaction Mass Efficiency', val: RME, max: 100, unit: '%', color: '#22c55e' },
        { label: 'Process Mass Intensity (PMI)', val: Math.min(100, (1 / PMI) * 100), max: 100, unit: ` (PMI: ${PMI.toFixed(1)})`, color: '#58a6ff' },
        { label: 'Renewable Carbon Share', val: renewPct, max: 100, unit: '%', color: '#a371f7' },
        { label: 'Waste Prevention (E-Factor)', val: Math.max(5, 100 - E_factor * 2), max: 100, unit: ` (E: ${E_factor.toFixed(1)})`, color: E_factor < 10 ? '#38ef7d' : '#f85149' }
      ];

      let curY = 35;
      ctx.fillStyle = '#c9d1d9';
      ctx.font = 'bold 12px system-ui';
      ctx.textAlign = 'left';
      ctx.fillText('Quantitative Green Metrics', 25, 20);

      kpis.forEach(kpi => {
        ctx.fillStyle = '#8b949e';
        ctx.font = '10px system-ui';
        ctx.fillText(`${kpi.label}: ${kpi.val.toFixed(1)}${kpi.unit}`, 25, curY);

        ctx.fillStyle = '#161b22';
        ctx.fillRect(25, curY + 6, leftW - 35, 16);
        ctx.fillStyle = kpi.color;
        ctx.fillRect(25, curY + 6, (kpi.val / kpi.max) * (leftW - 35), 16);

        curY += 46;
      });

      // Right: 12 Principles Radar Chart
      const cX = rightX + rightW * 0.5;
      const cY = height * 0.52;
      const radarR = Math.min(rightW * 0.42, height * 0.38);

      ctx.fillStyle = '#c9d1d9';
      ctx.font = 'bold 12px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText('12 Principles Radar Benchmark', cX, 20);

      // Radar Grid Concentric Polygons
      const numP = 12;
      for (let level = 1; level <= 4; level++) {
        const lr = (level / 4) * radarR;
        ctx.strokeStyle = '#21262d';
        ctx.lineWidth = 1;
        ctx.beginPath();
        for (let i = 0; i < numP; i++) {
          const ang = (i / numP) * Math.PI * 2 - Math.PI * 0.5;
          const px = cX + Math.cos(ang) * lr;
          const py = cY + Math.sin(ang) * lr;
          if (i === 0) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.closePath();
        ctx.stroke();
      }

      // 12 Principles scores based on sliders
      const scores = [
        Math.max(20, 100 - E_factor * 2), // 1. Prevention
        AE,                               // 2. Atom Economy
        75,                               // 3. Less Haz Synth
        80,                               // 4. Safer Chemicals
        recyclePct,                       // 5. Safer Solvents
        70,                               // 6. Energy Efficiency
        renewPct,                         // 7. Renewable Feedstocks
        85,                               // 8. Reduce Derivatives
        route === 'addition' ? 95 : 60,   // 9. Catalysis
        renewPct * 0.9,                   // 10. Degradation
        75,                               // 11. Real-time Analysis
        80                                // 12. Accident Prevention
      ];

      // Draw Radar Filled Polygon
      ctx.fillStyle = 'rgba(56, 239, 125, 0.25)';
      ctx.strokeStyle = '#38ef7d';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i < numP; i++) {
        const ang = (i / numP) * Math.PI * 2 - Math.PI * 0.5;
        const dist = (scores[i] / 100) * radarR;
        const px = cX + Math.cos(ang) * dist;
        const py = cY + Math.sin(ang) * dist;
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Axis labels (P1 to P12)
      for (let i = 0; i < numP; i++) {
        const ang = (i / numP) * Math.PI * 2 - Math.PI * 0.5;
        const lx = cX + Math.cos(ang) * (radarR + 14);
        const ly = cY + Math.sin(ang) * (radarR + 14);
        ctx.fillStyle = '#8b949e';
        ctx.font = '9px system-ui';
        ctx.textAlign = 'center';
        ctx.fillText(`P${i + 1}`, lx, ly + 3);
      }

      animId = requestAnimationFrame(render);
    }

    [routeS, yieldS, recycleS, renewS].forEach(s => s.addEventListener('input', () => {
      cancelAnimationFrame(animId);
      render();
    }));

    render();
  }

  return {
    sim_env_photochemical_smog_kinetics,
    sim_env_greenhouse_radiative_forcing,
    sim_env_stratospheric_ozone_chapman,
    sim_env_streeter_phelps_dissolved_oxygen,
    sim_env_groundwater_arsenic_speciation,
    sim_env_pesticide_bioaccumulation_foodweb,
    sim_env_soil_cation_exchange_cec,
    sim_env_activated_sludge_effluent_treatment,
    sim_env_landfill_methane_leachate,
    sim_env_green_chemistry_metrics
  };
})();

/* ==========================================================================
   Global Simulation Engine Registry Adapter
   ========================================================================== */
if (typeof window !== 'undefined') {
  window.SimulationEngine = window.SimulationEngine || {};
  Object.keys(window.EnvironmentalChemistrySimulations).forEach(function(key) {
    window[key] = window.EnvironmentalChemistrySimulations[key];
  });
  const originalInit = window.SimulationEngine.initSimulation;
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    const el = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
    if (!el) return;
    if (window.EnvironmentalChemistrySimulations && typeof window.EnvironmentalChemistrySimulations[simType] === 'function') {
      return window.EnvironmentalChemistrySimulations[simType](el);
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
'''
    with open("environmental-chemistry-sims.js", "w", encoding="utf-8") as f:
        f.write(code)
    print("Saved environmental-chemistry-sims.js successfully.")

if __name__ == "__main__":
    generate_sims_js()
