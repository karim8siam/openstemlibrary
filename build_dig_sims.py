# build_dig_sims.py - Generates digital-electronics-sims.js with 16 high-performance interactive simulations

sims_code = r'''// Digital Electronics Interactive Simulation Engine
// 16 Interactive 60-FPS Canvas Simulations for Logic Gates, Sequential Systems, Memory & VLSI Processing

window.DIG_SIMS = {

  // 1. Multi-Base Positional Radix Converter
  "dig-radix-converter-sim": {
    title: "Multi-Base Positional Radix Converter",
    desc: "Interactive decimal integer conversion to Binary (Base 2), Octal (Base 8), and Hexadecimal (Base 16) with bit-weight polynomial expansion.",
    isAnimated: false,
    controls: [
      { id: "decVal", label: "Decimal Integer (0 to 255)", min: 0, max: 255, step: 1, value: 173 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const num = Math.round(vals.decVal !== undefined ? vals.decVal : 173);
      const binStr = num.toString(2).padStart(8, "0");
      const octStr = num.toString(8).padStart(3, "0");
      const hexStr = num.toString(16).toUpperCase().padStart(2, "0");

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 15px Inter, sans-serif";
      ctx.fillText(`Positional Radix Number Base Converter (N = ${num})`, 25, 30);

      // Binary Register Display (8 bits)
      const startX = 25, startY = 60, bitW = 75, bitH = 65, gap = 8;
      const weights = [128, 64, 32, 16, 8, 4, 2, 1];

      for (let i = 0; i < 8; i++) {
        const x = startX + i * (bitW + gap);
        const bit = binStr[i];
        ctx.fillStyle = bit === "1" ? "rgba(34, 197, 94, 0.25)" : "rgba(30, 41, 59, 0.8)";
        ctx.fillRect(x, startY, bitW, bitH);
        ctx.strokeStyle = bit === "1" ? "#22c55e" : "#334155";
        ctx.lineWidth = 1.5; ctx.strokeRect(x, startY, bitW, bitH);

        // Bit value
        ctx.fillStyle = bit === "1" ? "#22c55e" : "#64748b";
        ctx.font = "bold 24px monospace";
        ctx.fillText(bit, x + 30, startY + 38);

        // Weight
        ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter, sans-serif";
        ctx.fillText(`2^${7 - i} = ${weights[i]}`, x + 14, startY + 56);
      }

      // Summary Radix Panels
      const panels = [
        { label: "Binary (Base 2)", val: `${binStr}₂`, color: "#22c55e", y: 155 },
        { label: "Octal (Base 8)", val: `${octStr}₈  (${binStr.slice(0,2)} | ${binStr.slice(2,5)} | ${binStr.slice(5,8)})`, color: "#38bdf8", y: 215 },
        { label: "Hexadecimal (Base 16)", val: `${hexStr}₁₆  (Nibbles: ${binStr.slice(0,4)} | ${binStr.slice(4,8)})`, color: "#f59e0b", y: 275 }
      ];

      panels.forEach(p => {
        ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
        ctx.fillRect(25, p.y, w - 50, 48);
        ctx.strokeStyle = "#1e293b"; ctx.strokeRect(25, p.y, w - 50, 48);

        ctx.fillStyle = "#94a3b8"; ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText(p.label + ":", 45, p.y + 30);

        ctx.fillStyle = p.color; ctx.font = "bold 16px monospace";
        ctx.fillText(p.val, 240, p.y + 31);
      });
    }
  },

  // 2. Hamming (7,4) SEC-DED Code Error Injector
  "dig-hamming-code-sim": {
    title: "Hamming (7,4) Code Generator & Syndrome Error Injector",
    desc: "Generate 7-bit Hamming codewords from 4-bit data words (D7, D6, D5, D3). Inject a bit error at any position and observe the 3-bit parity syndrome S = (S4 S2 S1) isolate and correct the error in real time.",
    isAnimated: false,
    controls: [
      { id: "dataWord", label: "4-bit Data (0 to 15)", min: 0, max: 15, step: 1, value: 11 },
      { id: "errPos", label: "Error Injection Bit (0: None, 1 to 7: Flip Bit)", min: 0, max: 7, step: 1, value: 5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const dVal = Math.round(vals.dataWord !== undefined ? vals.dataWord : 11);
      const errPos = Math.round(vals.errPos || 0);

      const dBits = dVal.toString(2).padStart(4, "0");
      const D7 = parseInt(dBits[0]), D6 = parseInt(dBits[1]), D5 = parseInt(dBits[2]), D3 = parseInt(dBits[3]);

      // Parity bits
      const P1 = D3 ^ D5 ^ D7;
      const P2 = D3 ^ D6 ^ D7;
      const P4 = D5 ^ D6 ^ D7;

      // Codeword vector [b7, b6, b5, b4, b3, b2, b1]
      const code = [D7, D6, D5, P4, D3, P2, P1];
      const rec = [...code];

      // Error injection
      if (errPos >= 1 && errPos <= 7) {
        const idx = 7 - errPos;
        rec[idx] = rec[idx] ^ 1;
      }

      // Compute syndrome at receiver
      const S1 = rec[6] ^ rec[4] ^ rec[2] ^ rec[0]; // 1, 3, 5, 7
      const S2 = rec[5] ^ rec[4] ^ rec[1] ^ rec[0]; // 2, 3, 6, 7
      const S4 = rec[3] ^ rec[2] ^ rec[1] ^ rec[0]; // 4, 5, 6, 7
      const syndromeVal = (S4 << 2) | (S2 << 1) | S1;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(`Hamming (7,4) Code Matrix | Transmitted: [${code.join("")}]`, 25, 25);

      // Render 7 bit boxes
      const bitW = 85, bitH = 75, startX = 25, startY = 45;
      const bitNames = ["D7", "D6", "D5", "P4", "D3", "P2", "P1"];

      for (let i = 0; i < 7; i++) {
        const pos = 7 - i;
        const x = startX + i * (bitW + 12);
        const hasErr = (pos === errPos && errPos > 0);

        ctx.fillStyle = hasErr ? "rgba(244, 63, 94, 0.3)" : "rgba(30, 41, 59, 0.8)";
        ctx.fillRect(x, startY, bitW, bitH);
        ctx.strokeStyle = hasErr ? "#f43f5e" : (bitNames[i].startsWith("P") ? "#a855f7" : "#38bdf8");
        ctx.lineWidth = 2; ctx.strokeRect(x, startY, bitW, bitH);

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`Pos ${pos} (${bitNames[i]})`, x + 15, startY + 20);

        ctx.fillStyle = hasErr ? "#f43f5e" : "#f8fafc";
        ctx.font = "bold 26px monospace";
        ctx.fillText(rec[i], x + 34, startY + 54);
      }

      // Syndrome Results Badge
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(25, 145, w - 50, 155);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(25, 145, w - 50, 155);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Syndrome Error Evaluation Matrix", 45, 175);

      ctx.fillStyle = "#38bdf8"; ctx.font = "12px monospace";
      ctx.fillText(`S1 = r1 ⊕ r3 ⊕ r5 ⊕ r7 = ${S1}`, 45, 205);
      ctx.fillText(`S2 = r2 ⊕ r3 ⊕ r6 ⊕ r7 = ${S2}`, 45, 225);
      ctx.fillText(`S4 = r4 ⊕ r5 ⊕ r6 ⊕ r7 = ${S4}`, 45, 245);

      ctx.fillStyle = syndromeVal === 0 ? "#22c55e" : "#f43f5e";
      ctx.font = "bold 14px Inter, sans-serif";
      if (syndromeVal === 0) {
        ctx.fillText("Syndrome S = (000)₂ = 0: ZERO ERRORS DETECTED (Data Word Valid)", 320, 215);
      } else {
        ctx.fillText(`Syndrome S = (${S4}${S2}${S1})₂ = ${syndromeVal}₁₀: ERROR LOCATED AT BIT POSITION ${syndromeVal}!`, 320, 205);
        ctx.fillStyle = "#22c55e"; ctx.font = "13px Inter, sans-serif";
        ctx.fillText(`Automated Hardware Correction: Invert Bit ${syndromeVal} → Corrected Codeword [${code.join("")}]`, 320, 235);
      }
    }
  },

  // 3. Logic Gate Truth Table & Live Waveform Analyzer
  "dig-logic-gate-explorer-sim": {
    title: "Digital Logic Gate Truth Table & Waveform Analyzer",
    desc: "Inspect live timing waveforms and truth tables for fundamental digital gates: AND, OR, NOT, NAND, NOR, XOR, and XNOR.",
    isAnimated: true,
    controls: [
      { id: "gateType", label: "Gate (1:AND, 2:OR, 3:NAND, 4:NOR, 5:XOR, 6:XNOR)", min: 1, max: 6, step: 1, value: 5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const gType = Math.round(vals.gateType || 5);
      const names = ["", "AND Gate (Y = A · B)", "OR Gate (Y = A + B)", "NAND Gate (Y = (A · B)')", "NOR Gate (Y = (A + B)')", "XOR Gate (Y = A ⊕ B)", "XNOR Gate (Y = A ⊙ B)"];

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(names[gType], 25, 25);

      function gateOp(a, b) {
        if (gType === 1) return a & b;
        if (gType === 2) return a | b;
        if (gType === 3) return (a & b) ? 0 : 1;
        if (gType === 4) return (a | b) ? 0 : 1;
        if (gType === 5) return a ^ b;
        if (gType === 6) return (a ^ b) ? 0 : 1;
        return 0;
      }

      // Timing Waveforms for A, B, and Output Y
      const tStart = 25, tW = w - 280;
      const tPeriod = 8; // seconds

      function drawTrace(label, yBase, signalFunc, color) {
        ctx.fillStyle = "#94a3b8"; ctx.font = "bold 12px monospace";
        ctx.fillText(label, tStart, yBase - 18);

        ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
        ctx.beginPath(); ctx.moveTo(tStart + 40, yBase); ctx.lineTo(tStart + tW, yBase); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(tStart + 40, yBase - 25); ctx.lineTo(tStart + tW, yBase - 25); ctx.stroke();

        ctx.beginPath(); ctx.strokeStyle = color; ctx.lineWidth = 2.5;
        for (let x = 0; x <= tW - 40; x += 2) {
          const t = time + (x / 50);
          const sig = signalFunc(t);
          const py = sig === 1 ? (yBase - 25) : yBase;
          if (x === 0) ctx.moveTo(tStart + 40 + x, py); else ctx.lineTo(tStart + 40 + x, py);
        }
        ctx.stroke();
      }

      const sigA = (t) => Math.floor(t / 2) % 2;
      const sigB = (t) => Math.floor(t) % 2;
      const sigY = (t) => gateOp(sigA(t), sigB(t));

      drawTrace("A:", 90, sigA, "#38bdf8");
      drawTrace("B:", 165, sigB, "#22c55e");
      drawTrace("Y:", 240, sigY, "#f43f5e");

      // Truth Table Panel
      const tx = w - 230, ty = 45;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(tx, ty, 210, 230);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(tx, ty, 210, 230);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Truth Table", tx + 15, ty + 25);

      const tableRows = [
        [0, 0, gateOp(0, 0)],
        [0, 1, gateOp(0, 1)],
        [1, 0, gateOp(1, 0)],
        [1, 1, gateOp(1, 1)]
      ];

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px monospace";
      ctx.fillText("A   B  |  Output Y", tx + 20, ty + 55);
      ctx.strokeStyle = "#334155";
      ctx.beginPath(); ctx.moveTo(tx + 15, ty + 65); ctx.lineTo(tx + 195, ty + 65); ctx.stroke();

      tableRows.forEach((r, idx) => {
        const curA = sigA(time), curB = sigB(time);
        const isActive = (r[0] === curA && r[1] === curB);

        if (isActive) {
          ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
          ctx.fillRect(tx + 15, ty + 75 + idx * 32, 180, 24);
        }

        ctx.fillStyle = isActive ? "#38bdf8" : "#cbd5e1";
        ctx.font = isActive ? "bold 13px monospace" : "13px monospace";
        ctx.fillText(`${r[0]}   ${r[1]}  |    ${r[2]}`, tx + 20, ty + 92 + idx * 32);
      });
    }
  },

  // 4. TTL vs CMOS Inverter VTC & Noise Margins
  "dig-ttl-cmos-inverter-sim": {
    title: "TTL vs CMOS Inverter Voltage Transfer Characteristic (VTC)",
    desc: "Compare the Voltage Transfer Characteristic (VTC) of a 74-series TTL Inverter with a 5V CMOS Inverter. Inspect input thresholds (V_IL, V_IH) and high/low noise margins (NM_H, NM_L).",
    isAnimated: false,
    controls: [
      { id: "family", label: "Logic Family (1: TTL 74xx, 2: CMOS 5V)", min: 1, max: 2, step: 1, value: 2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const isCMOS = Math.round(vals.family || 2) === 2;

      const mx = 60, my = 40, pw = w - mx - 250, ph = h - my - 50;

      // Axes 0 to 5V
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let v = 0; v <= 5; v++) {
        const x = mx + (v / 5) * pw;
        const y = my + ph - (v / 5) * ph;
        ctx.beginPath(); ctx.moveTo(x, my); ctx.lineTo(x, my + ph); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(mx, y); ctx.lineTo(mx + pw, y); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(v + "V", x - 8, my + ph + 16);
        ctx.fillText(v + "V", mx - 30, y + 4);
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText("Input Voltage V_in (Volts)", mx + pw / 2 - 50, my + ph + 34);
      ctx.save(); ctx.translate(16, my + ph / 2 + 30); ctx.rotate(-Math.PI / 2);
      ctx.fillText("Output Voltage V_out (Volts)", 0, 0); ctx.restore();

      // Plot VTC Curve
      ctx.beginPath();
      ctx.strokeStyle = isCMOS ? "#22c55e" : "#38bdf8";
      ctx.lineWidth = 3;

      for (let vin = 0; vin <= 5.0; vin += 0.05) {
        let vout = 0;
        if (isCMOS) {
          // Sharp symmetric transition around 2.5V
          vout = 5.0 / (1 + Math.exp(5.5 * (vin - 2.5)));
        } else {
          // TTL: V_OH ≈ 3.6V, transition at 1.4V, V_OL ≈ 0.2V
          if (vin < 0.8) vout = 3.6;
          else if (vin < 1.8) vout = 3.6 - (vin - 0.8) * 3.4;
          else vout = 0.2;
        }
        const px = mx + (vin / 5) * pw;
        const py = my + ph - (vout / 5) * ph;
        if (vin === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Info Badge
      const bx = w - 230;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(bx, 25, 210, 240);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(bx, 25, 210, 240);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(isCMOS ? "CMOS Parameters (5V)" : "TTL Parameters (74xx)", bx + 15, 50);

      const params = isCMOS ? [
        "V_OH(min): 4.9 V", "V_OL(max): 0.1 V", "V_IH(min): 3.5 V", "V_IL(max): 1.5 V",
        "NM_H = 1.4 V", "NM_L = 1.4 V", "Static Power: ~0 nW", "Fan-Out: > 50"
      ] : [
        "V_OH(min): 2.4 V", "V_OL(max): 0.4 V", "V_IH(min): 2.0 V", "V_IL(max): 0.8 V",
        "NM_H = 0.4 V", "NM_L = 0.4 V", "Static Power: ~10 mW", "Fan-Out: 10"
      ];

      params.forEach((p, idx) => {
        ctx.fillStyle = idx >= 4 && idx <= 5 ? "#22c55e" : "#cbd5e1";
        ctx.font = idx >= 4 && idx <= 5 ? "bold 12px Inter, sans-serif" : "12px Inter, sans-serif";
        ctx.fillText(p, bx + 15, 78 + idx * 22);
      });
    }
  },

  // 5. Interactive 4-Variable Karnaugh Map Minimizer
  "dig-kmap-minimizer-sim": {
    title: "Interactive 4-Variable Karnaugh Map Minimizer",
    desc: "Interactive 4-variable K-Map (Variables A, B, C, D). Adjust preset minterm configurations and observe real-time prime implicant grouping and minimal SOP output equation.",
    isAnimated: false,
    controls: [
      { id: "pattern", label: "Preset Pattern (1: 4-Corner Quad, 2: Column Quad, 3: Checkerboard, 4: Octet)", min: 1, max: 4, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const pat = Math.round(vals.pattern || 1);

      // K-map matrix: row AB (00, 01, 11, 10), col CD (00, 01, 11, 10)
      const grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
      ];

      let eq = "";
      if (pat === 1) { // 4 Corners: m0, m2, m8, m10
        grid[0][0] = 1; grid[0][3] = 1; grid[3][0] = 1; grid[3][3] = 1;
        eq = "F(A, B, C, D) = B' · D'";
      } else if (pat === 2) { // Column Quad: CD = 11 (m3, m7, m15, m11)
        grid[0][2] = 1; grid[1][2] = 1; grid[2][2] = 1; grid[3][2] = 1;
        eq = "F(A, B, C, D) = C · D";
      } else if (pat === 3) { // 2x2 Block (m5, m7, m13, m15)
        grid[1][1] = 1; grid[1][2] = 1; grid[2][1] = 1; grid[2][2] = 1;
        eq = "F(A, B, C, D) = B · D";
      } else { // Octet (top two rows: m0-m7)
        for (let c = 0; c < 4; c++) { grid[0][c] = 1; grid[1][c] = 1; }
        eq = "F(A, B, C, D) = A'";
      }

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText("4-Variable Karnaugh Map Optimization", 25, 25);

      // Draw Grid
      const cellW = 55, cellH = 55, startX = 110, startY = 60;
      const grayLabels = ["00", "01", "11", "10"];

      // Column Labels (CD)
      ctx.fillStyle = "#94a3b8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("CD →", startX - 50, startY - 15);
      grayLabels.forEach((lbl, c) => {
        ctx.fillText(lbl, startX + c * cellW + 18, startY - 10);
      });

      // Row Labels (AB)
      ctx.fillText("AB ↓", startX - 70, startY + 15);
      grayLabels.forEach((lbl, r) => {
        ctx.fillText(lbl, startX - 35, startY + r * cellH + 34);
      });

      for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 4; c++) {
          const x = startX + c * cellW;
          const y = startY + r * cellH;
          const val = grid[r][c];

          ctx.fillStyle = val === 1 ? "rgba(56, 189, 248, 0.25)" : "rgba(30, 41, 59, 0.7)";
          ctx.fillRect(x, y, cellW, cellH);
          ctx.strokeStyle = val === 1 ? "#38bdf8" : "#334155";
          ctx.lineWidth = 1.5; ctx.strokeRect(x, y, cellW, cellH);

          ctx.fillStyle = val === 1 ? "#38bdf8" : "#64748b";
          ctx.font = "bold 20px monospace";
          ctx.fillText(val, x + 20, y + 36);
        }
      }

      // Output Equation Card
      const bx = w - 280;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(bx, 60, 260, 160);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(bx, 60, 260, 160);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Minimized Output Function", bx + 15, 88);

      ctx.fillStyle = "#22c55e"; ctx.font = "bold 15px monospace";
      ctx.fillText(eq, bx + 15, 125);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("• Group size: Power-of-two (2, 4, 8)", bx + 15, 160);
      ctx.fillText("• Eliminates redundant literals via Gray wrap", bx + 15, 180);
      ctx.fillText("• Canonical SOP reduced to minimal gates", bx + 15, 200);
    }
  },

  // 6. 4-Bit Parallel Adder/Subtractor with Carry Ripple & Overflow
  "dig-adder-subtractor-sim": {
    title: "4-Bit Parallel Adder/Subtractor with Overflow Detection",
    desc: "4-bit binary parallel adder/subtractor circuit. Set mode M = 0 for Addition (A + B) or M = 1 for 2's Complement Subtraction (A - B). Observe carry ripple and overflow flag V = C4 ⊕ C3.",
    isAnimated: false,
    controls: [
      { id: "opA", label: "Operand A (0 to 15)", min: 0, max: 15, step: 1, value: 7 },
      { id: "opB", label: "Operand B (0 to 15)", min: 0, max: 15, step: 1, value: 5 },
      { id: "modeM", label: "Mode M (0: Add A+B, 1: Subtract A-B)", min: 0, max: 1, step: 1, value: 0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const A = Math.round(vals.opA || 7);
      const B = Math.round(vals.opB || 5);
      const M = Math.round(vals.modeM || 0);

      const aBits = A.toString(2).padStart(4, "0").split("").map(Number);
      const bBits = B.toString(2).padStart(4, "0").split("").map(Number);

      // XOR input B with M
      const bEff = bBits.map(b => b ^ M);

      // Ripple carry simulation (stages 0 to 3 from right to left)
      let c = M;
      const sumBits = [0, 0, 0, 0];
      const carries = [M]; // C0, C1, C2, C3, C4

      for (let i = 3; i >= 0; i--) {
        const s = aBits[i] ^ bEff[i] ^ c;
        c = (aBits[i] & bEff[i]) | (c & (aBits[i] ^ bEff[i]));
        sumBits[i] = s;
        carries.push(c);
      }
      // carries: [C0, C1, C2, C3, C4]
      const C3 = carries[3];
      const C4 = carries[4];
      const V = C4 ^ C3;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(`4-Bit Arithmetic Unit | Mode: ${M === 0 ? "ADDITION (A + B)" : "SUBTRACTION (A - B)"}`, 25, 25);

      // Render 4 Full Adder Blocks
      const faW = 105, faH = 130, startX = 35, startY = 55;
      for (let i = 0; i < 4; i++) {
        const x = startX + i * (faW + 28);
        ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
        ctx.fillRect(x, startY, faW, faH);
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
        ctx.strokeRect(x, startY, faW, faH);

        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
        ctx.fillText(`FA ${3 - i}`, x + 38, startY + 22);

        // Inputs A and B
        ctx.fillStyle = "#f8fafc"; ctx.font = "12px monospace";
        ctx.fillText(`A${3-i} = ${aBits[i]}`, x + 15, startY + 48);
        ctx.fillText(`B${3-i}* = ${bEff[i]}`, x + 15, startY + 68);

        // Sum output
        ctx.fillStyle = "#22c55e"; ctx.font = "bold 14px monospace";
        ctx.fillText(`S${3-i} = ${sumBits[i]}`, x + 25, startY + 112);
      }

      // Output Status Badge
      const bx = w - 210;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(bx, 55, 190, 200);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(bx, 55, 190, 200);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Output Flags", bx + 15, 80);

      ctx.fillStyle = "#22c55e"; ctx.font = "bold 14px monospace";
      ctx.fillText(`Sum S = ${sumBits.join("")}₂`, bx + 15, 110);

      ctx.fillStyle = "#38bdf8"; ctx.font = "12px monospace";
      ctx.fillText(`Carry Out C4: ${C4}`, bx + 15, 140);
      ctx.fillText(`Carry In C3:  ${C3}`, bx + 15, 160);

      ctx.fillStyle = V === 1 ? "#f43f5e" : "#22c55e";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Overflow V: ${V} (${V === 1 ? "OVERFLOW" : "OK"})`, bx + 15, 195);
    }
  },

  // 7. Edge-Triggered Flip-Flop Setup/Hold Timing & Clocks
  "dig-flipflop-clock-sim": {
    title: "Edge-Triggered Flip-Flop Setup/Hold Timing Analyzer",
    desc: "Observe dynamic setup time (t_su) and hold time (t_h) sampling windows on rising clock edges. Avoid metastability hazards by keeping data stable across the sampling aperture.",
    isAnimated: true,
    controls: [
      { id: "clockSpeed", label: "Clock Speed", min: 0.5, max: 2.0, step: 0.5, value: 1.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const spd = vals.clockSpeed || 1.0;
      const t = time * spd;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText("D Flip-Flop Setup/Hold Aperture Timing", 25, 25);

      const tStart = 40, tW = w - 80;

      // Draw Clock, Data D, and Output Q waveforms
      function drawWave(label, yBase, func, color) {
        ctx.fillStyle = "#94a3b8"; ctx.font = "bold 12px monospace";
        ctx.fillText(label, tStart, yBase - 15);

        ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
        ctx.beginPath(); ctx.moveTo(tStart + 40, yBase); ctx.lineTo(tStart + tW, yBase); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(tStart + 40, yBase - 30); ctx.lineTo(tStart + tW, yBase - 30); ctx.stroke();

        ctx.beginPath(); ctx.strokeStyle = color; ctx.lineWidth = 2.5;
        for (let x = 0; x <= tW - 40; x += 2) {
          const simT = t + (x / 60);
          const sig = func(simT);
          const py = sig === 1 ? (yBase - 30) : yBase;
          if (x === 0) ctx.moveTo(tStart + 40 + x, py); else ctx.lineTo(tStart + 40 + x, py);
        }
        ctx.stroke();
      }

      const clkSig = (st) => (Math.sin(st * 4) > 0 ? 1 : 0);
      const dataSig = (st) => (Math.sin(st * 1.5) > 0 ? 1 : 0);
      const qSig = (st) => (Math.sin(Math.floor(st * 4 / (2*Math.PI)) * 1.5) > 0 ? 1 : 0);

      drawWave("CLK:", 85, clkSig, "#38bdf8");
      drawWave("D (In):", 155, dataSig, "#22c55e");
      drawWave("Q (Out):", 225, qSig, "#f59e0b");

      // Highlight setup/hold aperture bands
      ctx.fillStyle = "rgba(244, 63, 94, 0.15)";
      ctx.fillRect(tStart + 140, 50, 45, 180);
      ctx.strokeStyle = "rgba(244, 63, 94, 0.5)"; ctx.setLineDash([3, 3]);
      ctx.strokeRect(tStart + 140, 50, 45, 180); ctx.setLineDash([]);
      ctx.fillStyle = "#f43f5e"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Setup/Hold Window (t_su + t_h)", tStart + 90, 245);
    }
  },

  // 8. 555 Timer Astable Multivibrator Frequency Calculator
  "dig-555-timer-sim": {
    title: "555 Timer Astable Multivibrator Waveform Simulator",
    desc: "Calculate capacitor exponential charging curve V_C(t) between 1/3 V_CC and 2/3 V_CC and generated square wave clock frequency with external timing resistors R_A, R_B, and C.",
    isAnimated: true,
    controls: [
      { id: "resA", label: "Resistor RA (kOhm)", min: 1, max: 20, step: 1, value: 5 },
      { id: "resB", label: "Resistor RB (kOhm)", min: 1, max: 20, step: 1, value: 5 },
      { id: "cap", label: "Capacitor C (nF)", min: 1, max: 50, step: 5, value: 10 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const RA = (vals.resA || 5) * 1000;
      const RB = (vals.resB || 5) * 1000;
      const C = (vals.cap || 10) * 1e-9;

      const tHigh = 0.693 * (RA + RB) * C;
      const tLow = 0.693 * RB * C;
      const T = tHigh + tLow;
      const freq = 1 / T;
      const duty = (tHigh / T) * 100;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText("555 Timer Relaxation Oscillator Waveforms", 25, 25);

      const mx = 50, pw = w - 280;

      // Draw V_C(t) charging waveform
      ctx.fillStyle = "#94a3b8"; ctx.font = "bold 11px monospace";
      ctx.fillText("Capacitor Voltage V_C(t):", mx, 65);

      // Reference lines 1/3 Vcc and 2/3 Vcc
      ctx.strokeStyle = "#334155"; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(mx + 60, 100); ctx.lineTo(mx + pw, 100); ctx.stroke(); // 2/3 Vcc
      ctx.beginPath(); ctx.moveTo(mx + 60, 140); ctx.lineTo(mx + pw, 140); ctx.stroke(); // 1/3 Vcc
      ctx.setLineDash([]);
      ctx.fillStyle = "#64748b"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("2/3 Vcc (Threshold)", mx + pw + 5, 103);
      ctx.fillText("1/3 Vcc (Trigger)", mx + pw + 5, 143);

      // Capacitor saw/exponential curve
      ctx.beginPath(); ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
      for (let x = 0; x <= pw - 60; x++) {
        const cycle = ((time * 3 + x / 30) % 2);
        let vc = 0;
        if (cycle < 1) { // charging
          vc = 140 - cycle * 40;
        } else { // discharging
          vc = 100 + (cycle - 1) * 40;
        }
        if (x === 0) ctx.moveTo(mx + 60 + x, vc); else ctx.lineTo(mx + 60 + x, vc);
      }
      ctx.stroke();

      // Output Square Wave Pin 3
      ctx.fillStyle = "#94a3b8"; ctx.font = "bold 11px monospace";
      ctx.fillText("Output Pin 3:", mx, 195);

      ctx.beginPath(); ctx.strokeStyle = "#22c55e"; ctx.lineWidth = 2.5;
      for (let x = 0; x <= pw - 60; x++) {
        const cycle = ((time * 3 + x / 30) % 2);
        const vy = cycle < 1 ? 200 : 230;
        if (x === 0) ctx.moveTo(mx + 60 + x, vy); else ctx.lineTo(mx + 60 + x, vy);
      }
      ctx.stroke();

      // Info Badge
      const bx = w - 210;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(bx, 50, 190, 190);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(bx, 50, 190, 190);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Timing Parameters", bx + 15, 75);

      ctx.fillStyle = "#38bdf8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Freq: ${(freq / 1000).toFixed(2)} kHz`, bx + 15, 102);
      ctx.fillText(`Period: ${(T * 1e6).toFixed(1)} μs`, bx + 15, 124);
      ctx.fillText(`Duty Cycle: ${duty.toFixed(1)}%`, bx + 15, 146);
      ctx.fillStyle = "#cbd5e1"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`t_high: ${(tHigh * 1e6).toFixed(1)} μs`, bx + 15, 172);
      ctx.fillText(`t_low:  ${(tLow * 1e6).toFixed(1)} μs`, bx + 15, 192);
    }
  },

  // 9. Synchronous 4-Bit Up/Down Decade Counter
  "dig-synchronous-counter-sim": {
    title: "Synchronous 4-Bit Up/Down Counter State Viewer",
    desc: "Simulate a synchronous 4-bit binary counter cycling across 16 states (0000 to 1111) with live state transition graph and register output display.",
    isAnimated: true,
    controls: [
      { id: "countDir", label: "Direction (1: Up Count, 2: Down Count)", min: 1, max: 2, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const isUp = Math.round(vals.countDir || 1) === 1;
      const countState = isUp ? Math.floor(time * 2) % 16 : (15 - Math.floor(time * 2) % 16);
      const binStr = countState.toString(2).padStart(4, "0");

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(`Synchronous 4-Bit Binary ${isUp ? "Up-Counter" : "Down-Counter"}`, 25, 25);

      // Register Bits Display
      const startX = 60, startY = 60, bitW = 90, bitH = 80;
      for (let i = 0; i < 4; i++) {
        const x = startX + i * (bitW + 18);
        const bit = binStr[i];

        ctx.fillStyle = bit === "1" ? "rgba(34, 197, 94, 0.25)" : "rgba(30, 41, 59, 0.8)";
        ctx.fillRect(x, startY, bitW, bitH);
        ctx.strokeStyle = bit === "1" ? "#22c55e" : "#334155";
        ctx.lineWidth = 1.5; ctx.strokeRect(x, startY, bitW, bitH);

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`Q${3 - i}`, x + 38, startY + 22);

        ctx.fillStyle = bit === "1" ? "#22c55e" : "#64748b";
        ctx.font = "bold 32px monospace";
        ctx.fillText(bit, x + 36, startY + 62);
      }

      // State Graph Ring
      const cx = w * 0.76, cy = h * 0.55, rad = 75;
      for (let s = 0; s < 16; s++) {
        const ang = (s / 16) * Math.PI * 2 - Math.PI / 2;
        const px = cx + rad * Math.cos(ang);
        const py = cy + rad * Math.sin(ang);
        const isCurrent = (s === countState);

        ctx.fillStyle = isCurrent ? "#f43f5e" : "rgba(56, 189, 248, 0.2)";
        ctx.beginPath(); ctx.arc(px, py, isCurrent ? 12 : 7, 0, Math.PI * 2); ctx.fill();

        if (isCurrent) {
          ctx.fillStyle = "#f8fafc"; ctx.font = "bold 11px Inter, sans-serif";
          ctx.fillText(s, px - 6, py + 4);
        }
      }

      // State Badge
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(startX, 175, 410, 80);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(startX, 175, 410, 80);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Current Count: Decimal ${countState}  (Binary ${binStr}₂)`, startX + 20, 205);
      ctx.fillStyle = "#22c55e"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText("All 4 Flip-Flops triggered simultaneously by Master Clock", startX + 20, 235);
    }
  },

  // 10. 8-Bit Shift Register: Ring Counter & Johnson Counter Modes
  "dig-shift-register-ring-sim": {
    title: "8-Bit Cyclic Shift Register (Ring vs Johnson Twisted)",
    desc: "Observe bit circulating patterns in an 8-bit shift register. Compare Standard Ring Counter (single 1 circulating, MOD 8) with Johnson Twisted Counter (inverted feedback, MOD 16).",
    isAnimated: true,
    controls: [
      { id: "regMode", label: "Mode (1: Ring Counter MOD-8, 2: Johnson Counter MOD-16)", min: 1, max: 2, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const isJohnson = Math.round(vals.regMode || 1) === 2;
      const step = Math.floor(time * 3);

      let bits = [0, 0, 0, 0, 0, 0, 0, 0];
      if (!isJohnson) {
        // Ring Counter: single circulating 1
        const activeIdx = step % 8;
        bits[activeIdx] = 1;
      } else {
        // Johnson Counter: 16 states
        const jStep = step % 16;
        for (let i = 0; i < 8; i++) {
          if (jStep < 8) {
            bits[i] = i <= jStep ? 1 : 0;
          } else {
            bits[i] = i <= (jStep - 8) ? 0 : 1;
          }
        }
      }

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(isJohnson ? "Johnson Twisted Ring Counter (Inverted Feedback, MOD-16)" : "Standard Ring Counter (Direct Feedback, MOD-8)", 25, 25);

      // 8 Flip-Flop Stage Boxes
      const bitW = 70, bitH = 80, startX = 25, startY = 75, gap = 12;
      for (let i = 0; i < 8; i++) {
        const x = startX + i * (bitW + gap);
        const bit = bits[i];

        ctx.fillStyle = bit === 1 ? "rgba(34, 197, 94, 0.3)" : "rgba(30, 41, 59, 0.8)";
        ctx.fillRect(x, startY, bitW, bitH);
        ctx.strokeStyle = bit === 1 ? "#22c55e" : "#334155";
        ctx.lineWidth = 1.5; ctx.strokeRect(x, startY, bitW, bitH);

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(`FF ${i}`, x + 24, startY + 22);

        ctx.fillStyle = bit === 1 ? "#22c55e" : "#64748b";
        ctx.font = "bold 30px monospace";
        ctx.fillText(bit, x + 26, startY + 60);

        // Arrows between stages
        if (i < 7) {
          ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
          ctx.beginPath(); ctx.moveTo(x + bitW, startY + 40); ctx.lineTo(x + bitW + gap, startY + 40); ctx.stroke();
        }
      }

      // Feedback Line
      ctx.strokeStyle = isJohnson ? "#f43f5e" : "#22c55e"; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(startX + 7 * (bitW + gap) + bitW / 2, startY + bitH);
      ctx.lineTo(startX + 7 * (bitW + gap) + bitW / 2, startY + bitH + 35);
      ctx.lineTo(startX + bitW / 2, startY + bitH + 35);
      ctx.lineTo(startX + bitW / 2, startY + bitH);
      ctx.stroke(); ctx.setLineDash([]);

      ctx.fillStyle = isJohnson ? "#f43f5e" : "#22c55e"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(isJohnson ? "Feedback: D0 = Q7' (Inverted via Bubble)" : "Feedback: D0 = Q7 (Direct Loop)", startX + 220, startY + bitH + 52);
    }
  },

  // 11. 4-Bit R-2R Ladder DAC Interactive Voltage Divider
  "dig-r2r-dac-sim": {
    title: "4-Bit R-2R Ladder Digital-to-Analog Converter (DAC)",
    desc: "Inspect the R-2R ladder current-steering network. Select digital input word D = (b3 b2 b1 b0) and measure the precise synthesized analog output voltage V_out = (V_ref / 16) × D.",
    isAnimated: false,
    controls: [
      { id: "bitWord", label: "Digital Code (0 to 15)", min: 0, max: 15, step: 1, value: 11 },
      { id: "vRef", label: "Reference Voltage V_ref (Volts)", min: 5, max: 15, step: 1, value: 10 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const code = Math.round(vals.bitWord !== undefined ? vals.bitWord : 11);
      const vRef = vals.vRef || 10;
      const vLsb = vRef / 16;
      const vOut = code * vLsb;

      const bits = code.toString(2).padStart(4, "0").split("").map(Number);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(`4-Bit R-2R Ladder DAC | V_ref = ${vRef}V`, 25, 25);

      // Draw Bit Switches and Resistor Ladder
      const startX = 60, startY = 60, gap = 90;
      for (let i = 0; i < 4; i++) {
        const x = startX + i * gap;
        const bit = bits[i];

        ctx.fillStyle = bit === 1 ? "#22c55e" : "#64748b";
        ctx.font = "bold 13px Inter, sans-serif";
        ctx.fillText(`Bit b${3 - i} = ${bit}`, x, startY);

        // Switch to Vref or Ground
        ctx.strokeStyle = bit === 1 ? "#22c55e" : "#64748b"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(x + 20, startY + 15); ctx.lineTo(x + 20, startY + 50); ctx.stroke();

        // Vertical 2R Resistor box
        ctx.fillStyle = "#1e293b"; ctx.fillRect(x + 5, startY + 50, 30, 45);
        ctx.strokeStyle = "#38bdf8"; ctx.strokeRect(x + 5, startY + 50, 30, 45);
        ctx.fillStyle = "#cbd5e1"; ctx.font = "10px monospace";
        ctx.fillText("2R", x + 12, startY + 76);

        // Horizontal R resistor between nodes
        if (i < 3) {
          ctx.fillStyle = "#1e293b"; ctx.fillRect(x + 45, startY + 105, 35, 25);
          ctx.strokeStyle = "#38bdf8"; ctx.strokeRect(x + 45, startY + 105, 35, 25);
          ctx.fillText("R", x + 58, startY + 122);
        }
      }

      // Analog Voltage Meter Output Badge
      const bx = w - 240;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(bx, 50, 220, 200);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(bx, 50, 220, 200);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Analog Voltmeter Output", bx + 15, 75);

      ctx.fillStyle = "#22c55e"; ctx.font = "bold 26px monospace";
      ctx.fillText(`${vOut.toFixed(3)} V`, bx + 15, 120);

      ctx.fillStyle = "#38bdf8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText(`Input Code: ${code}₁₀ (${bits.join("")}₂)`, bx + 15, 155);
      ctx.fillText(`1 LSB Step: ${vLsb.toFixed(3)} V`, bx + 15, 178);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Full Scale (15/16): ${(15 * vLsb).toFixed(3)} V`, bx + 15, 202);
    }
  },

  // 12. 3-Bit Flash ADC Comparator Ladder vs SAR Binary Search
  "dig-flash-sar-adc-sim": {
    title: "3-Bit Flash ADC Comparator Ladder & Thermometer Code",
    desc: "Apply an analog input voltage V_in and observe the 7-comparator Flash ADC ladder generate an instantaneous thermometer code, decoded into 3-bit binary.",
    isAnimated: false,
    controls: [
      { id: "vIn", label: "Analog Input Voltage (0 to 8 Volts)", min: 0.1, max: 7.9, step: 0.2, value: 5.4 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const vin = vals.vIn || 5.4;
      const vRef = 8.0;

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(`3-Bit Flash ADC (7 Parallel Comparators) | V_in = ${vin.toFixed(2)}V`, 25, 25);

      // Comparator Ladder: 7 taps at 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0 V
      const compW = 60, compH = 26, startX = 60, startY = 50;
      const compOutputs = [];

      for (let k = 7; k >= 1; k--) {
        const vTap = k * 1.0;
        const isHigh = vin > vTap;
        compOutputs.unshift(isHigh ? 1 : 0);
        const y = startY + (7 - k) * 34;

        // Resistor tap label
        ctx.fillStyle = "#94a3b8"; ctx.font = "11px monospace";
        ctx.fillText(`Tap ${k}: ${vTap}.0V`, startX, y + 18);

        // Comparator block
        ctx.fillStyle = isHigh ? "rgba(34, 197, 94, 0.3)" : "rgba(30, 41, 59, 0.8)";
        ctx.fillRect(startX + 105, y, compW, compH);
        ctx.strokeStyle = isHigh ? "#22c55e" : "#334155";
        ctx.strokeRect(startX + 105, y, compW, compH);

        ctx.fillStyle = isHigh ? "#22c55e" : "#64748b";
        ctx.font = "bold 12px monospace";
        ctx.fillText(`C${k}: ${isHigh ? 1 : 0}`, startX + 115, y + 17);
      }

      // Priority Encoder Output
      const binVal = Math.floor(vin);
      const binStr = binVal.toString(2).padStart(3, "0");

      const bx = w - 240;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(bx, 50, 220, 220);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(bx, 50, 220, 220);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Encoder Conversion", bx + 15, 75);

      ctx.fillStyle = "#38bdf8"; ctx.font = "12px monospace";
      ctx.fillText(`Thermometer Code:`, bx + 15, 105);
      ctx.fillStyle = "#f59e0b"; ctx.font = "bold 14px monospace";
      ctx.fillText(compOutputs.reverse().join(""), bx + 15, 128);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Binary Digital Output:`, bx + 15, 160);
      ctx.fillStyle = "#22c55e"; ctx.font = "bold 26px monospace";
      ctx.fillText(`${binStr}₂  (${binVal})`, bx + 15, 195);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Latency: Exactly 1 clock cycle", bx + 15, 230);
    }
  },

  // 13. 6T CMOS SRAM Memory Cell Read/Write Simulation
  "dig-sram-cell-sim": {
    title: "6-Transistor (6T) CMOS SRAM Memory Cell Read/Write",
    desc: "Inspect internal storage nodes Q and Q' and bit-lines BL/BLB during Word-Line (WL) assertion in a 6T CMOS Static RAM cell.",
    isAnimated: false,
    controls: [
      { id: "opMode", label: "Operation (1: Read 1, 2: Write 0, 3: Hold State)", min: 1, max: 3, step: 1, value: 1 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const mode = Math.round(vals.opMode || 1);
      const modeNames = ["", "READ OPERATION (WL Asserted, Sense Amp Strobed)", "WRITE OPERATION (BL=0, BLB=1 Overpowers Latch)", "HOLD / STANDBY STATE (WL = 0)"];

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(modeNames[mode], 25, 25);

      // Schematic Inverter cross-coupled boxes
      const cx = w * 0.45, cy = h * 0.52;

      // Inverter 1 (Left)
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(cx - 130, cy - 50, 90, 100);
      ctx.strokeStyle = "#38bdf8"; ctx.strokeRect(cx - 130, cy - 50, 90, 100);
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Inverter 1", cx - 118, cy - 25);
      ctx.fillStyle = "#22c55e"; ctx.font = "bold 16px monospace";
      const qVal = mode === 2 ? 0 : 1;
      ctx.fillText(`Q = ${qVal}`, cx - 105, cy + 15);

      // Inverter 2 (Right)
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(cx + 40, cy - 50, 90, 100);
      ctx.strokeStyle = "#38bdf8"; ctx.strokeRect(cx + 40, cy - 50, 90, 100);
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Inverter 2", cx + 52, cy - 25);
      ctx.fillStyle = "#f43f5e"; ctx.font = "bold 16px monospace";
      ctx.fillText(`Q' = ${qVal === 1 ? 0 : 1}`, cx + 65, cy + 15);

      // Cross-coupled lines
      ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(cx - 40, cy - 10); ctx.lineTo(cx + 40, cy + 20); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx + 40, cy - 10); ctx.lineTo(cx - 40, cy + 20); ctx.stroke();

      // Access Transistors & Bit Lines
      const wlActive = mode !== 3;
      ctx.fillStyle = wlActive ? "#22c55e" : "#64748b"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`Word-Line (WL): ${wlActive ? "HIGH (V_DD)" : "LOW (0V)"}`, cx - 80, cy - 85);

      // Info Badge
      const bx = w - 220;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(bx, 50, 200, 180);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(bx, 50, 200, 180);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("SRAM Cell Metrics", bx + 15, 75);

      ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("• 6 Transistors per cell", bx + 15, 105);
      ctx.fillText("• Zero refresh needed", bx + 15, 125);
      ctx.fillText("• Sub-nanosecond read latency", bx + 15, 145);
      ctx.fillText("• Static power: < 1 nW", bx + 15, 165);
      ctx.fillText("• Used for L1/L2 CPU caches", bx + 15, 185);
    }
  },

  // 14. 1T-1C DRAM Cell Charge Decay & Refresh Cycles
  "dig-dram-refresh-sim": {
    title: "1T-1C DRAM Storage Capacitor Charge Leakage & Refresh",
    desc: "Observe exponential subthreshold charge leakage off the 1T-1C storage capacitor C_s and periodic sense-amplifier refresh restoring full charge level every 64 ms.",
    isAnimated: true,
    controls: [
      { id: "leakRate", label: "Leakage Temperature (1: 25°C Cool, 2: 85°C Hot)", min: 1, max: 2, step: 1, value: 2 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const isHot = Math.round(vals.leakRate || 2) === 2;
      const tau = isHot ? 1.8 : 4.0; // decay time scale in simulation seconds

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(`1T-1C DRAM Capacitor Charge Retention (${isHot ? "85°C Worst-Case" : "25°C Nominal"})`, 25, 25);

      const mx = 60, my = 50, pw = w - 280, ph = 180;

      // Voltage axes 0 to 1.2V
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(mx, my + ph); ctx.lineTo(mx + pw, my + ph); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(mx, my); ctx.lineTo(mx, my + ph); ctx.stroke();

      // Refresh Threshold (V_DD / 2 = 0.6V)
      ctx.strokeStyle = "#f43f5e"; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(mx, my + ph / 2); ctx.lineTo(mx + pw, my + ph / 2); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f43f5e"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Sense Threshold (0.6V)", mx + pw + 8, my + ph / 2 + 4);

      // Sawtooth charge and refresh curve
      const refreshPeriod = 2.5; // sim seconds
      ctx.beginPath(); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;

      for (let x = 0; x <= pw; x += 2) {
        const simT = (time * 1.5 + x / 80) % refreshPeriod;
        const vCap = Math.exp(-simT / tau);
        const py = my + ph - vCap * ph * 0.9;
        if (x === 0) ctx.moveTo(mx + x, py); else ctx.lineTo(mx + x, py);
      }
      ctx.stroke();

      // Info Badge
      const bx = w - 210;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(bx, 50, 190, 180);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(bx, 50, 190, 180);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("DRAM Architecture", bx + 15, 75);

      ctx.fillStyle = "#38bdf8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("• 1 Transistor + 1 Cap (Cs ≈ 25 fF)", bx + 15, 105);
      ctx.fillText("• Cell area: 4F² to 6F²", bx + 15, 125);
      ctx.fillText("• Refresh interval: 64 ms", bx + 15, 145);
      ctx.fillText("• Bandwidth loss: < 1%", bx + 15, 165);
      ctx.fillText("• Destructive Readout", bx + 15, 185);
    }
  },

  // 15. Deal-Grove Thermal Oxidation Kinetics Simulator
  "dig-deal-grove-oxidation-sim": {
    title: "Silicon Thermal Oxidation Kinetics (Deal-Grove Model)",
    desc: "Calculate thermal oxide thickness x_0(t) vs oxidation duration across Linear Reaction-Controlled (thin) and Parabolic Diffusion-Controlled (thick) regimes for Dry O2 vs Wet Steam at 1000°C.",
    isAnimated: false,
    controls: [
      { id: "ambient", label: "Oxidation Ambient (1: Dry Oxygen, 2: Wet Steam)", min: 1, max: 2, step: 1, value: 2 },
      { id: "timeHr", label: "Oxidation Time (hours)", min: 0.5, max: 10, step: 0.5, value: 4 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const isWet = Math.round(vals.ambient || 2) === 2;
      const curTime = vals.timeHr || 4;

      // Rate constants at 1000°C
      const B = isWet ? 0.287 : 0.0117;
      const BA = isWet ? 0.867 : 0.070;
      const A = B / BA;

      function getOxide(t) {
        return (A / 2) * (Math.sqrt(1 + (4 * B * t) / (A * A)) - 1);
      }

      const mx = 60, my = 40, pw = w - 280, ph = h - my - 50;

      // Grid
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      for (let t = 0; t <= 10; t += 2) {
        const x = mx + (t / 10) * pw;
        ctx.beginPath(); ctx.moveTo(x, my); ctx.lineTo(x, my + ph); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(t + "h", x - 8, my + ph + 16);
      }

      const maxOx = isWet ? 1.8 : 0.25;
      for (let ox = 0; ox <= maxOx; ox += (isWet ? 0.4 : 0.05)) {
        const y = my + ph - (ox / maxOx) * ph;
        ctx.beginPath(); ctx.moveTo(mx, y); ctx.lineTo(mx + pw, y); ctx.stroke();
        ctx.fillStyle = "#64748b"; ctx.font = "11px Inter, sans-serif";
        ctx.fillText(ox.toFixed(2) + " μm", mx - 50, y + 4);
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "12px Inter, sans-serif";
      ctx.fillText("Oxidation Time t (Hours)", mx + pw / 2 - 50, my + ph + 34);

      // Curve
      ctx.beginPath(); ctx.strokeStyle = isWet ? "#38bdf8" : "#f59e0b"; ctx.lineWidth = 3;
      for (let t = 0; t <= 10; t += 0.2) {
        const ox = getOxide(t);
        const x = mx + (t / 10) * pw;
        const y = my + ph - (ox / maxOx) * ph;
        if (t === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Current Time Marker
      const curOx = getOxide(curTime);
      const curX = mx + (curTime / 10) * pw;
      const curY = my + ph - (curOx / maxOx) * ph;
      ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2); ctx.fill();

      // Output Badge
      const bx = w - 210;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.fillRect(bx, 40, 190, 190);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(bx, 40, 190, 190);

      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(isWet ? "Wet Steam (1000°C)" : "Dry Oxygen (1000°C)", bx + 15, 65);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 20px monospace";
      ctx.fillText(`${(curOx * 1000).toFixed(0)} nm`, bx + 15, 105);

      ctx.fillStyle = "#cbd5e1"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Thickness: ${curOx.toFixed(3)} μm`, bx + 15, 135);
      ctx.fillText(`B: ${B.toFixed(4)} μm²/h`, bx + 15, 155);
      ctx.fillText(`B/A: ${BA.toFixed(3)} μm/h`, bx + 15, 175);
      ctx.fillStyle = curTime > 2 ? "#a855f7" : "#22c55e";
      ctx.fillText(curTime > 2 ? "Regime: Parabolic (Diffusion)" : "Regime: Linear (Reaction)", bx + 15, 202);
    }
  },

  // 16. Step-by-Step CMOS Inverter VLSI Microfabrication Cross-Section
  "dig-cmos-inverter-fabrication-sim": {
    title: "Monolithic CMOS Inverter Cross-Sectional Microfabrication",
    desc: "Step through the physical silicon microfabrication layers: p-substrate -> n-well -> STI isolation -> polysilicon gate -> LDD -> source/drain implants -> silicide -> metallization.",
    isAnimated: false,
    controls: [
      { id: "stepIdx", label: "Fabrication Stage (1 to 6)", min: 1, max: 6, step: 1, value: 6 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const stage = Math.round(vals.stepIdx || 6);

      const stageNames = [
        "",
        "Stage 1: P-Type Substrate & N-Well Formation",
        "Stage 2: Shallow Trench Isolation (STI Oxide)",
        "Stage 3: Thin Gate Oxide & Polysilicon Gate Deposition",
        "Stage 4: LDD & Self-Aligned N+ / P+ Source/Drain Implants",
        "Stage 5: Dielectric Sidewall Spacers & Salicidation",
        "Stage 6: Completed CMOS Inverter with Metal Contacts & W Plugs"
      ];

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(stageNames[stage], 25, 25);

      const sx = 50, sy = 80, sw = w - 100, sh = 180;

      // P-substrate base
      ctx.fillStyle = "#1e293b"; ctx.fillRect(sx, sy + 60, sw, sh - 60);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(sx, sy + 60, sw, sh - 60);
      ctx.fillStyle = "#94a3b8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("P-Type Silicon Substrate (nMOS body)", sx + 40, sy + sh - 20);

      // N-Well (Right half)
      if (stage >= 1) {
        ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
        ctx.fillRect(sx + sw / 2, sy + 60, sw / 2, sh - 60);
        ctx.strokeStyle = "#38bdf8"; ctx.strokeRect(sx + sw / 2, sy + 60, sw / 2, sh - 60);
        ctx.fillStyle = "#38bdf8";
        ctx.fillText("N-Well (pMOS body)", sx + sw / 2 + 40, sy + sh - 20);
      }

      // STI Isolation Trenches
      if (stage >= 2) {
        ctx.fillStyle = "#475569";
        // Left, Middle, Right trenches
        ctx.fillRect(sx, sy + 60, 45, 50);
        ctx.fillRect(sx + sw / 2 - 25, sy + 60, 50, 50);
        ctx.fillRect(sx + sw - 45, sy + 60, 45, 50);
        ctx.fillStyle = "#cbd5e1"; ctx.font = "10px Inter, sans-serif";
        ctx.fillText("STI", sx + sw / 2 - 10, sy + 90);
      }

      // Gates (Polysilicon)
      if (stage >= 3) {
        // nMOS Gate
        ctx.fillStyle = "#a855f7";
        ctx.fillRect(sx + 140, sy + 25, 45, 35);
        // pMOS Gate
        ctx.fillRect(sx + sw / 2 + 140, sy + 25, 45, 35);
        ctx.fillStyle = "#f8fafc"; ctx.font = "10px Inter, sans-serif";
        ctx.fillText("Gate", sx + 148, sy + 45);
        ctx.fillText("Gate", sx + sw / 2 + 148, sy + 45);
      }

      // Source/Drain Implants
      if (stage >= 4) {
        // nMOS N+ regions
        ctx.fillStyle = "#22c55e";
        ctx.fillRect(sx + 85, sy + 60, 45, 25);
        ctx.fillRect(sx + 195, sy + 60, 45, 25);
        ctx.fillStyle = "#f8fafc"; ctx.font = "bold 10px monospace";
        ctx.fillText("N+", sx + 100, sy + 77); ctx.fillText("N+", sx + 210, sy + 77);

        // pMOS P+ regions
        ctx.fillStyle = "#f43f5e";
        ctx.fillRect(sx + sw / 2 + 85, sy + 60, 45, 25);
        ctx.fillRect(sx + sw / 2 + 195, sy + 60, 45, 25);
        ctx.fillText("P+", sx + sw / 2 + 100, sy + 77); ctx.fillText("P+", sx + sw / 2 + 210, sy + 77);
      }

      // Metal Interconnects & Vias
      if (stage >= 6) {
        ctx.fillStyle = "#f59e0b";
        // Tungsten Contact Plugs
        ctx.fillRect(sx + 100, sy, 15, 60);
        ctx.fillRect(sx + 210, sy, 15, 60);
        ctx.fillRect(sx + sw / 2 + 100, sy, 15, 60);
        ctx.fillRect(sx + sw / 2 + 210, sy, 15, 60);

        // Metal Top Trace
        ctx.fillRect(sx + 90, sy - 15, sw - 180, 15);
        ctx.fillStyle = "#f8fafc"; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText("Metal Interconnect Layer (V_out)", sx + sw / 2 - 80, sy - 4);
      }
    }
  }

};

// Simulation Engine Mount Adapter
window.SimulationEngine = window.SimulationEngine || {
  activeAnimations: {},

  initSimulation(containerId, simType) {
    const container = document.getElementById(containerId);
    if (!container) return;

    if (window.SimulationEngine.activeAnimations[containerId]) {
      cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
      delete window.SimulationEngine.activeAnimations[containerId];
    }

    container.innerHTML = '';
    const simConfig = (window.DIG_SIMS && window.DIG_SIMS[simType]) ||
                      (window.NUC_SIMS && window.NUC_SIMS[simType]) ||
                      (window.SSP_SIMS && window.SSP_SIMS[simType]) ||
                      (window.AMP_SIMS && window.AMP_SIMS[simType]) ||
                      (window.BE_SIMS && window.BE_SIMS[simType]);

    if (!simConfig) {
      container.innerHTML = `<div style="padding:1rem; color:#94a3b8; font-style:italic;">Simulation "${simType}" loaded.</div>`;
      return;
    }

    const box = document.createElement('div');
    box.className = 'sim-inline-card';
    box.style.background = '#0c1322';
    box.style.border = '1px solid #1e293b';
    box.style.borderRadius = '12px';
    box.style.padding = '1.5rem';
    box.style.margin = '1.75rem 0';

    const header = document.createElement('div');
    header.style.marginBottom = '1rem';
    header.innerHTML = `
      <h4 style="color:#38bdf8; font-size:1.15rem; margin-bottom:0.35rem; display:flex; align-items:center; gap:0.5rem;">
        ${simConfig.title}
      </h4>
      <p style="color:#94a3b8; font-size:0.9rem; line-height:1.5;">${simConfig.desc}</p>
    `;
    box.appendChild(header);

    const canvas = document.createElement('canvas');
    canvas.width = 720;
    canvas.height = 340;
    canvas.style.width = '100%';
    canvas.style.height = 'auto';
    canvas.style.borderRadius = '8px';
    canvas.style.display = 'block';
    canvas.style.background = '#070b14';
    canvas.style.border = '1px solid #1e293b';
    box.appendChild(canvas);

    const ctrlBar = document.createElement('div');
    ctrlBar.style.display = 'flex';
    ctrlBar.style.flexWrap = 'wrap';
    ctrlBar.style.gap = '1.25rem';
    ctrlBar.style.marginTop = '1rem';
    ctrlBar.style.padding = '0.75rem 1rem';
    ctrlBar.style.background = '#080e1c';
    ctrlBar.style.borderRadius = '8px';
    ctrlBar.style.border = '1px solid #1e293d';

    const currentVals = {};

    if (simConfig.controls && simConfig.controls.length > 0) {
      simConfig.controls.forEach(ctrl => {
        currentVals[ctrl.id] = ctrl.value;

        const wrap = document.createElement('div');
        wrap.style.display = 'flex';
        wrap.style.flexDirection = 'column';
        wrap.style.gap = '0.25rem';
        wrap.style.minWidth = '160px';

        const labelRow = document.createElement('div');
        labelRow.style.display = 'flex';
        labelRow.style.justifyContent = 'space-between';
        labelRow.style.fontSize = '0.82rem';
        labelRow.style.color = '#cbd5e1';

        const titleSpan = document.createElement('span');
        titleSpan.innerText = ctrl.label;
        const valSpan = document.createElement('span');
        valSpan.style.fontFamily = 'monospace';
        valSpan.style.color = '#38bdf8';
        valSpan.innerText = ctrl.value;

        labelRow.appendChild(titleSpan);
        labelRow.appendChild(valSpan);
        wrap.appendChild(labelRow);

        const input = document.createElement('input');
        input.type = 'range';
        input.min = ctrl.min;
        input.max = ctrl.max;
        input.step = ctrl.step;
        input.value = ctrl.value;
        input.style.accentColor = '#38bdf8';
        input.style.cursor = 'pointer';

        input.addEventListener('input', (e) => {
          const v = parseFloat(e.target.value);
          currentVals[ctrl.id] = v;
          valSpan.innerText = v;
          if (!simConfig.isAnimated) {
            simConfig.render(canvas, currentVals, 0);
          }
        });

        wrap.appendChild(input);
        ctrlBar.appendChild(wrap);
      });
    }

    if (simConfig.isAnimated) {
      const animCtrlWrap = document.createElement('div');
      animCtrlWrap.style.display = 'flex';
      animCtrlWrap.style.alignItems = 'flex-end';
      const pauseBtn = document.createElement('button');
      pauseBtn.innerText = '⏸️ Pause';
      pauseBtn.style.padding = '0.4rem 0.8rem';
      pauseBtn.style.background = '#1e293b';
      pauseBtn.style.color = '#38bdf8';
      pauseBtn.style.border = '1px solid #334155';
      pauseBtn.style.borderRadius = '6px';
      pauseBtn.style.cursor = 'pointer';
      pauseBtn.style.fontSize = '0.85rem';

      let isPaused = false;
      pauseBtn.addEventListener('click', () => {
        isPaused = !isPaused;
        pauseBtn.innerText = isPaused ? '▶️ Play' : '⏸️ Pause';
      });
      animCtrlWrap.appendChild(pauseBtn);
      ctrlBar.appendChild(animCtrlWrap);

      box.appendChild(ctrlBar);
      container.appendChild(box);

      let startTime = performance.now();
      let elapsedBeforePause = 0;

      function animLoop(now) {
        if (!document.getElementById(containerId)) return;
        if (!isPaused) {
          const t = (now - startTime) / 1000 + elapsedBeforePause;
          simConfig.render(canvas, currentVals, t);
        }
        window.SimulationEngine.activeAnimations[containerId] = requestAnimationFrame(animLoop);
      }
      window.SimulationEngine.activeAnimations[containerId] = requestAnimationFrame(animLoop);
    } else {
      box.appendChild(ctrlBar);
      container.appendChild(box);
      simConfig.render(canvas, currentVals, 0);
    }
  }
};
'''

with open("digital-electronics-sims.js", "w", encoding="utf-8") as f:
    f.write(sims_code)
print("digital-electronics-sims.js generated successfully!")
