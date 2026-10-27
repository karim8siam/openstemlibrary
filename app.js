// Quantum Mechanics I Textbook Edition Controller
// Manages textbook sections, search indexing, simulations lifecycle, KaTeX rendering, study timer, and protective guards

function startApp() {
  const initialUnitIndex = Math.max(0, Math.min(window.COURSE_DATA.units.length - 1, Number(document.body.dataset.chapterIndex) || 0));
  let activeUnitIndex = initialUnitIndex;
  let mathDebounceTimer = null;

  // Initialize App
  initSidebar();
  loadChapter(initialUnitIndex, true);
  initMobileNavigation();
  initAntiCopyGuards();
  initFontToggle();
  initReadingAppearance();
  initSearch();

  // 1. Sidebar Setup
  function initSidebar() {
    const listEl = document.getElementById("unit-nav-list");
    listEl.innerHTML = "";

    window.COURSE_DATA.units.forEach((unit, idx) => {
      const li = document.createElement("li");
      li.className = `unit-nav-item ${idx === initialUnitIndex ? 'active' : ''}`;
      li.dataset.unitIndex = idx;
      const link = document.createElement('a');
      link.href = chapterUrl(idx);
      link.className = 'unit-nav-link';
      if (idx === initialUnitIndex) link.setAttribute('aria-current', 'page');
      link.innerHTML = `
        <span class="unit-nav-num">Ch.${unit.number || unit.unitNumber || (idx + 1)}</span>
        <span class="unit-nav-text">${unit.title}</span>
      `;
      li.appendChild(link);
      listEl.appendChild(li);
    });
  }

  function chapterUrl(index) {
    const book = document.body.dataset.bookPath || location.pathname.split('/').pop() || 'reader.html';
    return index === 0 ? book.replace(/\.html$/, '') : book.replace(/\.html$/, `-chapter-${index + 1}`);
  }

  function initMobileNavigation() {
    const sidebar = document.querySelector('.sidebar');
    const toolbar = document.querySelector('.top-navbar,.reader-toolbar');
    if (!sidebar || !toolbar) return;
    sidebar.id = 'reader-chapter-navigation';
    sidebar.setAttribute('aria-label', 'Book chapters');
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'btn-tool mobile-chapters-button';
    button.textContent = 'Chapters';
    button.setAttribute('aria-controls', sidebar.id);
    button.setAttribute('aria-expanded', 'false');
    const backdrop = document.createElement('button');
    backdrop.type = 'button';
    backdrop.className = 'chapter-menu-backdrop';
    backdrop.setAttribute('aria-label', 'Close chapter navigation');
    backdrop.hidden = true;
    const closeButton = document.createElement('button');
    closeButton.type = 'button';
    closeButton.className = 'btn-tool chapter-menu-close';
    closeButton.textContent = 'Close chapters';
    function close() {
      document.body.classList.remove('chapter-menu-open');
      button.setAttribute('aria-expanded', 'false');
      backdrop.hidden = true;
      button.focus();
    }
    button.addEventListener('click', () => {
      const open = !document.body.classList.contains('chapter-menu-open');
      document.body.classList.toggle('chapter-menu-open', open);
      button.setAttribute('aria-expanded', String(open));
      backdrop.hidden = !open;
      if (open) closeButton.focus();
    });
    closeButton.addEventListener('click', close);
    backdrop.addEventListener('click', close);
    document.addEventListener('keydown', event => {
      if (!document.body.classList.contains('chapter-menu-open')) return;
      if (event.key === 'Escape') close();
      if (event.key === 'Tab') {
        const focusable = [...sidebar.querySelectorAll('a,button,input')].filter(el => el.getClientRects().length);
        const first = focusable[0], last = focusable[focusable.length - 1];
        if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
        else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
      }
    });
    toolbar.prepend(button);
    sidebar.prepend(closeButton);
    document.body.appendChild(backdrop);
  }

  // 2. Load Chapter View
  function loadChapter(unitIndex, isInitialLoad = false) {
    activeUnitIndex = unitIndex;
    const unit = window.COURSE_DATA.units[unitIndex];

    try {
      // Update Header
      const tagEl = document.getElementById("unit-tag");
      if (tagEl) tagEl.innerText = `Chapter ${unit.number || unit.unitNumber || (unitIndex + 1)} • Theory & Derivations`;
      const titleEl = document.getElementById("unit-title");
      if (titleEl) titleEl.innerText = unit.title;
      const descEl = document.getElementById("unit-desc");
      if (descEl) descEl.innerText = unit.leadSummary || unit.description || "";
    } catch (e) {
      console.warn("Header update notice:", e);
    }

    if (isInitialLoad && document.querySelector("#textbook-sections .textbook-section-card")) {
      // Unit 1 already pre-rendered into HTML! Mount inline simulations safely
      const simTypes = [...new Set([
        ...(unit.simulations || []),
        ...(unit.sections || []).flatMap(section => section.simulation
          ? [section.simulation] : (section.simulations || []))
      ])];
      simTypes.forEach(simType => {
        const simId = `sim-container-${simType}`;
        setTimeout(() => {
          if (window.SimulationEngine && window.SimulationEngine.initSimulation) {
            window.SimulationEngine.initSimulation(simId, simType);
            labelSimulationControls(simId);
          }
        }, 60);
      });
      // Attach listeners to pre-rendered problem toggle buttons
      document.querySelectorAll(".problem-card").forEach(card => {
        const toggleBtn = card.querySelector(".solution-toggle-btn, .btn-solution-toggle");
        const solContent = card.querySelector(".solution-content");
        if (toggleBtn && solContent) {
          toggleBtn.addEventListener("click", () => {
            const isOpen = solContent.classList.toggle("open");
            if (solContent.style.display !== undefined) {
              solContent.style.display = isOpen ? "block" : "none";
            }
            toggleBtn.innerText = isOpen ? "🙈 Hide Solution" : "👁️ Reveal Complete Derivation & Solution";
            toggleBtn.setAttribute('aria-expanded', String(isOpen));
            if (isOpen) renderMath();
          });
        }
      });
      renderMath();
      return;
    }

    try {
      // Render Textbook Sections
      renderTextbookSections(unit.sections);
    } catch (e) {
      console.error("renderTextbookSections error:", e);
    }

    try {
      // Mount Simulations
      mountSimulations(unit.simulations);
    } catch (e) {
      console.error("mountSimulations error:", e);
    }

    try {
      // Render Solved Problems
      renderProblems(unit.problems);
    } catch (e) {
      console.error("renderProblems error:", e);
    }

    // Trigger KaTeX typesetting
    renderMath();
  }

  // 3. Render Textbook Sections (With Direct Inline Simulations)
  function renderTextbookSections(sections) {
    const container = document.getElementById("textbook-sections");
    if (!container) return;
    container.innerHTML = "";

    if (!sections || sections.length === 0) return;

    sections.forEach((sec, sIdx) => {
      const card = document.createElement("section");
      card.className = "textbook-section-card";
      const rawNum = sec.secNumber || (sec.number ? sec.number.toString().replace('§', '') : `${activeUnitIndex + 1}.${sIdx + 1}`);
      const secId = sec.id || `sec-${rawNum.replace('.', '-')}`;
      card.id = secId;

      // Collect inline simulations for this topic
      let simTypes = [];
      if (sec.simulation) {
        simTypes = [sec.simulation];
      } else if (sec.simulations && Array.isArray(sec.simulations)) {
        simTypes = sec.simulations;
      } else if (sIdx === 0 && window.COURSE_DATA && window.COURSE_DATA.units && window.COURSE_DATA.units[activeUnitIndex] && window.COURSE_DATA.units[activeUnitIndex].simulations) {
        simTypes = window.COURSE_DATA.units[activeUnitIndex].simulations;
      }

      let inlineSimHtml = "";
      simTypes.forEach(simType => {
        inlineSimHtml += `
          <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
            <div class="simulation-slot" id="sim-container-${simType}"></div>
          </div>
        `;
      });

      const rawHeading = sec.heading || sec.title || "";
      const cleanHeading = rawHeading
        .replace(/^(?:Lesson\s+\d+(?:\.\d+)?[:\s—\-]+|\d+\.\d+\s*[:—\-]?\s*)/i, "")
        .trim();

      card.innerHTML = `
        <header class="sec-header">
          <h3 class="sec-title">
            <span class="sec-num">§${rawNum}</span>
            <span>${cleanHeading || rawHeading}</span>
          </h3>
        </header>
        <div class="sec-content">
          ${formatMarkdownContent(sec.content)}
        </div>
        ${inlineSimHtml}
      `;
      container.appendChild(card);

      // Mount and start simulations right inside this topic section
      simTypes.forEach(simType => {
        const simId = `sim-container-${simType}`;
        setTimeout(() => {
          if (window.SimulationEngine && window.SimulationEngine.initSimulation) {
            window.SimulationEngine.initSimulation(simId, simType);
            labelSimulationControls(simId);
          }
        }, 60);
      });
    });
  }

  // 4. Mount Fallback Unit Simulations (if any remain unmounted)
  function mountSimulations(simList) {
    const wrap = document.getElementById("sim-section-wrap");
    const container = document.getElementById("simulations-mount");
    if (!container) return;
    container.innerHTML = "";

    if (!simList || simList.length === 0) {
      if (wrap) wrap.style.display = "none";
      return;
    }

    // Filter out simulations that were already mounted inline inside sections
    const unmountedSims = simList.filter(simType => !document.getElementById(`sim-container-${simType}`));

    if (unmountedSims.length === 0) {
      if (wrap) wrap.style.display = "none";
      return;
    }

    if (wrap) wrap.style.display = "block";
    unmountedSims.forEach(simType => {
      const slot = document.createElement("div");
      slot.className = "simulation-slot";
      const simId = `sim-container-${simType}`;
      slot.id = simId;
      container.appendChild(slot);

      setTimeout(() => {
        if (window.SimulationEngine && window.SimulationEngine.initSimulation) {
          window.SimulationEngine.initSimulation(simId, simType);
            labelSimulationControls(simId);
        }
      }, 60);
    });
  }

  // 5. Render Practice Problems
  function renderProblems(problemList) {
    const container = document.getElementById("problems-mount") || document.getElementById("problems-container") || document.getElementById('problem-cards-list');
    if (!container) return;
    container.innerHTML = "";

    if (!problemList || problemList.length === 0) {
      container.innerHTML = "<p class='text-muted'>No worked problems for this chapter yet.</p>";
      return;
    }

    problemList.forEach((prob, idx) => {
      const card = document.createElement("div");
      card.className = "problem-card";
      
      const diffClass = prob.difficulty === 'Easy' ? 'diff-easy' : (prob.difficulty === 'Medium' ? 'diff-medium' : (prob.difficulty && prob.difficulty.startsWith('diff-') ? prob.difficulty : 'diff-hard'));
      const diffLabel = prob.difficultyLabel || prob.difficulty || "Solved Problem";
      const probId = prob.id || `p${activeUnitIndex + 1}-${idx + 1}`;

      let stepsHtml = "";
      if (prob.steps && Array.isArray(prob.steps)) {
        prob.steps.forEach(step => {
          const stepTitle = step.stepName || step.title || step.step || `Step`;
          const mathBlock = (step.math && typeof step.math === 'string')
            ? `<div class="step-math">${step.math.startsWith('$$') ? step.math : `$$${step.math}$$`}</div>`
            : "";
          const explanation = step.explanation || step.detail || "";
          stepsHtml += `
            <div class="solution-step">
              <div class="step-title">${stepTitle}</div>
              ${mathBlock}
              <div class="step-explanation">${formatMarkdownContent(explanation)}</div>
            </div>
          `;
        });
      } else if (prob.solution) {
        stepsHtml += `
          <div class="solution-step">
            <div class="step-explanation">${formatMarkdownContent(prob.solution)}</div>
          </div>
        `;
      }

      if (prob.answer) {
        let answerText = prob.answer;
        if (typeof answerText === 'string' && !answerText.includes('$') && !answerText.includes('\\[') &&
            (/\\(frac|text|sqrt|cos|sin|vec|mathbf|approx|times|pm|in|to)\b/.test(answerText) || answerText.startsWith('d(') || answerText.startsWith("f'(") || answerText.startsWith("g'("))) {
          answerText = "$$" + answerText + "$$";
        }
        stepsHtml += `
          <div class="solution-step" style="border-left-color: #10b981;">
            <div class="step-title" style="color: #10b981;">Final Answer & Physical Insight</div>
            <div class="step-explanation">${formatMarkdownContent(answerText)}</div>
          </div>
        `;
      }

      card.innerHTML = `
        <div class="problem-header">
          <div class="problem-title-box">
            <span class="diff-badge ${diffClass}">${diffLabel}</span>
            <strong>${(prob.title || 'Solved Problem').includes('Example') ? (prob.title || 'Solved Problem') : `Example ${activeUnitIndex + 1}.${idx + 1}: ${prob.title || 'Solved Problem'}`}</strong>
          </div>
        </div>
        <div class="problem-question-box">
          ${formatMarkdownContent(prob.question || prob.statement || "")}
        </div>
        <button class="solution-toggle-btn" id="btn-sol-${probId}">
          👁️ Reveal Complete Derivation & Solution
        </button>
        <div class="solution-content" id="sol-content-${probId}">
          ${stepsHtml}
        </div>
      `;

      container.appendChild(card);

      // Attach Toggle Event
      const toggleBtn = card.querySelector(`#btn-sol-${probId}`);
      const solContent = card.querySelector(`#sol-content-${probId}`);
      if (toggleBtn && solContent) {
        toggleBtn.setAttribute('aria-expanded', 'false');
        toggleBtn.addEventListener("click", () => {
          const isOpen = solContent.classList.toggle("open");
          toggleBtn.innerText = isOpen ? "🙈 Hide Solution" : "👁️ Reveal Complete Derivation & Solution";
          toggleBtn.setAttribute('aria-expanded', String(isOpen));
          if (isOpen) renderMath();
        });
      }
    });
  }

  // 6. Comprehensive Text Formatter (Markdown to HTML)
  function formatMarkdownContent(text) {
    if (!text) return "";
    
    // If already pre-structured semantic HTML with tags, return directly
    if (text.includes("<h4") || text.includes("<p>") || text.includes("<ul") || text.includes("<ol") || text.includes("<div") || text.includes("<table")) {
      return text;
    }

    let clean = text.replace(/\r\n/g, "\n").trim();
    
    // Normalize multi-backslash math delimiters to standard \[ and \]
    clean = clean.replace(/\\+\[/g, "\\[").replace(/\\+\]/g, "\\]");
    // Strip dangling orphan backslash preceding display math
    clean = clean.replace(/\\+\s*(?=\\\[|\$\$)/g, "");

    function normalizeMath(m) {
      return m.replace(/(^|[\s\$\(\[\{\,\+\-\=\>\<\~]|\\(?:quad|qquad|\,|\;|\!|longrightarrow|to|rightleftharpoons))\s*(\^(?:[A-Za-z0-9\+\-]+|\{[^}]+\}))/g, "$1{}$2");
    }

    // Math is text for KaTeX, not HTML. Preserve comparisons and matrix
    // separators when the formatted result is assigned to innerHTML.
    function escapeMathHtml(m) {
      return m.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }

    // Isolate $$...$$ and \[...\]
    clean = clean.replace(/\$\$(.*?)\$\$/gs, function(match, math) {
      const singleLineMath = escapeMathHtml(normalizeMath(math.trim().replace(/\r?\n/g, " ")));
      return "\n\n<div class=\"math-display\">$$" + singleLineMath + "$$</div>\n\n";
    });
    clean = clean.replace(/\\\[(.*?)\\\]/gs, function(match, math) {
      const singleLineMath = escapeMathHtml(normalizeMath(math.trim().replace(/\\+$/, "").replace(/\r?\n/g, " ").trim()));
      return "\n\n<div class=\"math-display\">\\[" + singleLineMath + "\\]</div>\n\n";
    });

    const lines = clean.split("\n");
    const output = [];
    let inUl = false;
    let inOl = false;
    let paraLines = [];

    // Safe inline markdown applicator that protects math delimiters ($...$, \(...\), $$...$$, \[...\])
    function applyInlineMarkdown(str) {
      if (!str) return "";
      const mathTokens = [];
      let protectedStr = str.replace(/(\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$(?:\\\$|[^\$\n])+?(?<!\\)\$)/g, (m) => {
        const id = `@@MATH_TOKEN_${mathTokens.length}@@`;
        mathTokens.push(escapeMathHtml(normalizeMath(m)));
        return id;
      });

      protectedStr = protectedStr
        .replace(/`([^`\n]+)`/g, "<code>$1</code>")
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        .replace(/\*(.*?)\*/g, "<em>$1</em>");

      for (let idx = 0; idx < mathTokens.length; idx++) {
        protectedStr = protectedStr.replace(`@@MATH_TOKEN_${idx}@@`, mathTokens[idx]);
      }
      return protectedStr;
    }

    function flushPara() {
      if (paraLines.length > 0) {
        let p = paraLines.join(" ").trim();
        p = p.replace(/\s*\\+$/, "").trim();
        if (p && p !== "\\") output.push("<p>" + p + "</p>");
        paraLines = [];
      }
    }

    function closeLists() {
      if (inUl) { output.push("</ul>"); inUl = false; }
      if (inOl) { output.push("</ol>"); inOl = false; }
    }

    let i = 0;
    while (i < lines.length) {
      let line = lines[i];
      let s = line.trim();
      if (!s) {
        flushPara();
        closeLists();
        i++;
        continue;
      }

      // Horizontal Rule
      if (s === "---" || s === "***") {
        flushPara();
        closeLists();
        output.push("<hr class=\"section-divider-hr\">");
        i++;
        continue;
      }

      // Fenced Code Blocks (```)
      if (s.startsWith("```")) {
        flushPara();
        closeLists();
        i++;
        const codeLines = [];
        while (i < lines.length && !lines[i].trim().startsWith("```")) {
          let escapedLine = lines[i]
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;");
          codeLines.push(escapedLine);
          i++;
        }
        if (i < lines.length && lines[i].trim().startsWith("```")) {
          i++;
        }
        output.push("<pre class=\"diagram-code-block\" style=\"background: #0b1729; color: #f8fafc; padding: 1rem 1.25rem; border-radius: 8px; overflow-x: auto; font-family: monospace; font-size: 0.92rem; line-height: 1.55; border: 1px solid #334155; margin: 1.25rem 0 1.5rem;\"><code style=\"color: #f8fafc; background: transparent;\">" + codeLines.join("\n") + "</code></pre>");
        continue;
      }


      // Markdown Tables (| Col 1 | Col 2 |)
      if (s.startsWith("|") && s.endsWith("|") && i + 1 < lines.length && lines[i + 1].trim().startsWith("|") && /^\|(?:\s*:?-+:?\s*\|)+$/.test(lines[i + 1].trim())) {
        flushPara();
        closeLists();
        const headerRow = s.split("|").slice(1, -1).map(c => c.trim());
        const sepLine = lines[i + 1].trim();
        const aligns = sepLine.split("|").slice(1, -1).map(c => {
          c = c.trim();
          if (c.startsWith(":") && c.endsWith(":")) return "center";
          if (c.endsWith(":")) return "right";
          if (c.startsWith(":")) return "left";
          return "";
        });
        i += 2;
        const rows = [];
        while (i < lines.length && lines[i].trim().startsWith("|") && lines[i].trim().endsWith("|")) {
          const cells = lines[i].trim().split("|").slice(1, -1).map(c => c.trim());
          rows.push(cells);
          i++;
        }
        let tblHtml = '<div class="stat-table-scroll"><table class="stat-table"><thead><tr>';
        headerRow.forEach((h, colIdx) => {
          const align = aligns[colIdx] ? ` style="text-align: ${aligns[colIdx]};"` : "";
          tblHtml += `<th${align}>${applyInlineMarkdown(h)}</th>`;
        });
        tblHtml += '</tr></thead><tbody>';
        rows.forEach(r => {
          tblHtml += '<tr>';
          r.forEach((cell, colIdx) => {
            const align = aligns[colIdx] ? ` style="text-align: ${aligns[colIdx]};"` : "";
            tblHtml += `<td${align}>${applyInlineMarkdown(cell)}</td>`;
          });
          tblHtml += '</tr>';
        });
        tblHtml += '</tbody></table></div>';
        output.push(tblHtml);
        continue;
      }

      // Pre-wrapped math display
      if (s.startsWith("<div") || (s.startsWith("$$") && s.endsWith("$$")) || (s.startsWith("\\[") && s.endsWith("\\]"))) {
        flushPara();
        closeLists();
        output.push(s.startsWith("<div") ? s : "<div class=\"math-display\">" + s + "</div>");
        i++;
        continue;
      }

      // Blockquotes (> ...)
      if (s.startsWith(">")) {
        flushPara();
        closeLists();
        const bqLines = [];
        while (i < lines.length && lines[i].trim().startsWith(">")) {
          let bRaw = lines[i].trim();
          let bContent = bRaw.substring(1).trim();
          bqLines.push(bContent);
          i++;
        }

        const bqOutput = [];
        let bqPara = [];
        let bqUl = false;
        let bqOl = false;

        function flushBqPara() {
          if (bqPara.length > 0) {
            let bp = applyInlineMarkdown(bqPara.join(" ").trim());
            if (bp) bqOutput.push("<p>" + bp + "</p>");
            bqPara = [];
          }
        }
        function closeBqLists() {
          if (bqUl) { bqOutput.push("</ul>"); bqUl = false; }
          if (bqOl) { bqOutput.push("</ol>"); bqOl = false; }
        }

        bqLines.forEach(bl => {
          let bs = bl.trim();
          if (!bs) {
            flushBqPara();
            closeBqLists();
            return;
          }
          if (bs.startsWith("<div") || (bs.startsWith("$$") && bs.endsWith("$$"))) {
            flushBqPara();
            closeBqLists();
            bqOutput.push(bs.startsWith("<div") ? bs : "<div class=\"math-display\">" + bs + "</div>");
            return;
          }
          if (bs.startsWith("- ") || bs.startsWith("* ")) {
            flushBqPara();
            if (bqOl) { bqOutput.push("</ol>"); bqOl = false; }
            if (!bqUl) { bqOutput.push("<ul>"); bqUl = true; }
            let item = applyInlineMarkdown(bs.substring(2).trim());
            bqOutput.push("  <li>" + item + "</li>");
            return;
          }
          let bOlMatch = bs.match(/^([0-9]+)\.\s+(.*)$/);
          if (bOlMatch) {
            flushBqPara();
            if (bqUl) { bqOutput.push("</ul>"); bqUl = false; }
            if (!bqOl) { bqOutput.push("<ol>"); bqOl = true; }
            let item = applyInlineMarkdown(bOlMatch[2].trim());
            bqOutput.push("  <li>" + item + "</li>");
            return;
          }

          closeBqLists();
          bqPara.push(bs);
        });

        flushBqPara();
        closeBqLists();

        output.push("<blockquote class=\"math-callout\">\n" + bqOutput.join("\n") + "\n</blockquote>");
        continue;
      }

      // Section Headings
      if (s.startsWith("# ")) {
        flushPara();
        closeLists();
        output.push("<h4>" + s.substring(2).trim() + "</h4>");
        i++;
        continue;
      }

      if (s.startsWith("## ")) {
        flushPara();
        closeLists();
        output.push("<h4>" + s.substring(3).trim() + "</h4>");
        i++;
        continue;
      }

      if (s.startsWith("### ")) {
        flushPara();
        closeLists();
        output.push("<h4>" + s.substring(4).trim() + "</h4>");
        i++;
        continue;
      }

      if (s.startsWith("#### ")) {
        flushPara();
        closeLists();
        output.push("<h5>" + s.substring(5).trim() + "</h5>");
        i++;
        continue;
      }

      // Unordered List
      if (s.startsWith("- ") || s.startsWith("* ")) {
        flushPara();
        if (inOl) { output.push("</ol>"); inOl = false; }
        if (!inUl) { output.push("<ul>"); inUl = true; }
        let item = applyInlineMarkdown(s.substring(2).trim());
        output.push("  <li>" + item + "</li>");
        i++;
        continue;
      }

      // Ordered List or Numbered Section
      const olMatch = s.match(/^([0-9]+)\.\s+(.*)$/);
      if (olMatch) {
        let num = olMatch[1];
        let body = olMatch[2].trim();
        if (!inOl && (body.startsWith("**") || body.includes("Method") || body.includes("Law") || body.includes("Equation") || body.includes("Nature") || body.includes("Criteria") || body.includes("Equilibrium") || body.includes("Summing"))) {
          flushPara();
          closeLists();
          let cleanTitle = body.replace(/\*\*/g, "");
          output.push("<h4>" + num + ". " + cleanTitle + "</h4>");
          i++;
          continue;
        } else {
          flushPara();
          if (inUl) { output.push("</ul>"); inUl = false; }
          if (!inOl) { output.push("<ol>"); inOl = true; }
          let item = applyInlineMarkdown(body);
          output.push("  <li>" + item + "</li>");
          i++;
          continue;
        }
      }

      closeLists();
      let formattedLine = applyInlineMarkdown(s);
      paraLines.push(formattedLine);
      i++;
    }

    flushPara();
    closeLists();

    return output.join("\n\n");
  }

  // 7. Math Rendering with KaTeX (Debounced & Memory-Safe)
  function renderMath() {
    if (mathDebounceTimer) clearTimeout(mathDebounceTimer);
    mathDebounceTimer = setTimeout(() => {
      // Ensure all .step-math elements without delimiters are safely enclosed in $$
      document.querySelectorAll(".step-math").forEach(el => {
        const raw = el.textContent.trim();
        if (raw && !raw.startsWith("$$") && !raw.startsWith("\\[") && !el.querySelector(".katex")) {
          el.innerHTML = "$$" + raw + "$$";
        }
      });

      const targets = [
        document.getElementById("main-content-area"),
        document.querySelector(".chapter-article"),
        document.getElementById("textbook-sections"),
        document.getElementById("problems-mount"),
        document.getElementById("problems-container")
      ].filter(Boolean);

      if (window.renderMathInElement && targets.length > 0) {
        targets.forEach(target => {
          try {
            window.renderMathInElement(target, {
              delimiters: [
                { left: "$$", right: "$$", display: true },
                { left: "$", right: "$", display: false },
                { left: "\\[", right: "\\]", display: true },
                { left: "\\(", right: "\\)", display: false }
              ],
              ignoredClasses: ["katex", "katex-html", "katex-display", "inline-simulation-wrapper"],
              throwOnError: false
            });
          } catch (e) {
            console.warn("Math auto-render notice:", e);
          }
        });
      }
      if (typeof window.requestAnimationFrame === 'function') window.requestAnimationFrame(enableKeyboardMathScrolling);
      if (!window.renderMathInElement) {
        // KaTeX bundle may still be loading, retry in 100ms
        setTimeout(renderMath, 100);
      }
    }, 40);
  }


  // Most simulations provide visible labels adjacent to sliders, but their
  // older markup did not associate those labels with the actual control.
  function labelSimulationControls(simId) {
    const host = document.getElementById(simId);
    if (!host) return;
    host.querySelectorAll('input[type="range"]').forEach(input => {
      if ((input.labels && input.labels.length) ||
          input.hasAttribute('aria-label') || input.hasAttribute('aria-labelledby')) return;
      const prev = input.previousElementSibling;
      const label = prev && prev.tagName === 'LABEL'
        ? prev : input.parentElement?.querySelector('label');
      if (label && input.id) {
        label.setAttribute('for', input.id);
        return;
      }
      const idText = (input.id || '').replace(/-(slider|range)$/,'').replace(/[-_]/g,' ').trim();
      const fallback = idText || input.parentElement?.textContent?.trim().slice(0,75)
        || 'Simulation adjustment';
      input.setAttribute('aria-label', fallback);
    });
  }

  // Long equations intentionally scroll on small screens. Make only those
  // overflow regions keyboard-focusable so users can reach the full formula.
  function enableKeyboardMathScrolling() {
    document.querySelectorAll('.katex-display').forEach(el => {
      const css = window.getComputedStyle(el);
      if ((el.scrollWidth > el.clientWidth || el.scrollHeight > el.clientHeight) &&
          (css.overflowX === 'auto' || css.overflowX === 'scroll' ||
           css.overflowY === 'auto' || css.overflowY === 'scroll')) {
        el.setAttribute('tabindex', '0');
        el.setAttribute('title','Use arrow keys to view the rest of this equation');
      } else {
        el.removeAttribute('tabindex');
        el.removeAttribute('title');
      }
    });
  }
  window.addEventListener('resize', enableKeyboardMathScrolling);
  window.addEventListener('load', () => {
    setTimeout(enableKeyboardMathScrolling, 250);
    // CDN typesetting can finish after the first reading-layout pass.
    setTimeout(enableKeyboardMathScrolling, 700);
  });

  // 8. Student-friendly access. Do not trap normal browser gestures.
  // Blocking text selection, printing, and the context menu is not a reliable
  // content-protection mechanism and harms accessibility and study workflows.
  function initAntiCopyGuards() {
    const notice = document.querySelector('.protection-notice');
    if (notice) {
      notice.textContent = 'Read freely · Cite responsibly';
      notice.removeAttribute('title');
    }
  }

  // 11. Font Toggle (Academic Serif vs Modern Sans)
  function initFontToggle() {
    const btn = document.getElementById("btn-font-toggle") || document.getElementById('font-size-toggle');
    if (!btn) return;
    btn.addEventListener("click", () => {
      document.body.classList.toggle("academic-font");
      const isSerif = document.body.classList.contains("academic-font");
      btn.innerText = isSerif ? "Aa Modern" : "Aa Academic";
    });
  }

  // Reader-controlled paper appearance. Keeps interactive simulations on a dark canvas.
  // The button is idempotent because the static HTML generator runs this controller.
  function initReadingAppearance() {
    const toolbar = document.querySelector('.top-navbar .navbar-actions')
      || document.querySelector('.reader-toolbar')
      || document.querySelector('.top-navbar');
    if (!toolbar) return;
    let button = toolbar.querySelector('.reader-theme-toggle');
    if (!button) {
      button = document.createElement('button');
      button.type = 'button';
      button.className = 'btn-tool reader-theme-toggle';
      toolbar.appendChild(button);
    }
    const preferenceKey = 'openstem-reader-theme';
    // Use comfortable paper reading by default; respect existing Night preference.
    let paper = true;
    try { paper = window.localStorage.getItem(preferenceKey) !== 'night'; } catch (_) {
      // Private browsing and restricted storage must not break reading.
    }
    function update() {
      document.body.classList.toggle('reader-paper', paper);
      button.textContent = paper ? 'Night view' : 'Paper view';
      button.setAttribute('aria-pressed', String(paper));
      button.setAttribute('aria-label', paper ? 'Night view — switch to dark reading view' : 'Paper view — switch to paper reading view');
      button.title = paper ? 'Use the original dark reading theme' : 'Use a soft, high-contrast paper background';
    }
    update();
    button.addEventListener('click', () => {
      paper = !paper;
      update();
      try { window.localStorage.setItem(preferenceKey, paper ? 'paper' : 'night'); } catch (_) {}
    });
    // Reader-size controls change only academic reading text, not diagrams/UI.
    const fontSizeKey = 'openstem-reader-size';
    const allowedScales = [1, 1.125, 1.25];
    let sizeIndex = 0;
    try {
      const saved = Number(window.localStorage.getItem(fontSizeKey));
      if (Number.isFinite(saved) && allowedScales.includes(saved))
        sizeIndex = allowedScales.indexOf(saved);
    } catch (_) {}
    const controls = document.createElement('div');
    controls.className = 'reader-text-controls';
    controls.setAttribute('role', 'group');
    controls.setAttribute('aria-label', 'Reading text size');
    const minus = document.createElement('button');
    const plus = document.createElement('button');
    for (const [control, label, text] of [
      [minus, 'A− Decrease reading text size', 'A−'],
      [plus, 'A+ Increase reading text size', 'A+']
    ]) {
      control.type = 'button';
      control.className = 'btn-tool reader-size-button';
      control.setAttribute('aria-label', label);
      control.textContent = text;
      controls.appendChild(control);
    }
    function applySize() {
      const size = allowedScales[sizeIndex];
      document.body.style.setProperty('--openstem-reader-font-scale', String(size));
      minus.disabled = sizeIndex === 0;
      plus.disabled = sizeIndex === allowedScales.length - 1;
      controls.setAttribute('data-reading-scale', String(size));
      if (typeof window.requestAnimationFrame === 'function') window.requestAnimationFrame(enableKeyboardMathScrolling);
      try { window.localStorage.setItem(fontSizeKey, String(size)); } catch (_) {}
    }
    minus.addEventListener('click', () => {
      sizeIndex = Math.max(0, sizeIndex - 1);
      applySize();
    });
    plus.addEventListener('click', () => {
      sizeIndex = Math.min(allowedScales.length - 1, sizeIndex + 1);
      applySize();
    });
    toolbar.appendChild(controls);
    applySize();

  }

  // 12. Search & Filter Input
  function initSearch() {
    const input = document.getElementById("topic-search-input") || document.getElementById('course-search-input');
    if (!input) return;

    input.addEventListener("input", (e) => {
      const term = e.target.value.toLowerCase().trim();
      const items = document.querySelectorAll(".unit-nav-item");

      items.forEach((item, idx) => {
        const unit = window.COURSE_DATA && window.COURSE_DATA.units ? window.COURSE_DATA.units[idx] : null;
        if (!unit) return;
        const matchTitle = (unit.title || "").toLowerCase().includes(term);
        const matchSections = unit.sections && unit.sections.some(s => 
          ((s.heading || s.title || "").toLowerCase().includes(term)) || 
          ((s.content || "").toLowerCase().includes(term))
        );

        if (term === "" || matchTitle || matchSections) {
          item.style.display = "flex";
        } else {
          item.style.display = "none";
        }
      });
    });
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", startApp);
} else {
  startApp();
}

window.addEventListener("load", () => {
  function triggerMath() {
    const target = document.getElementById("main-content-area") || document.body;
    if (window.renderMathInElement && target) {
      try {
        window.renderMathInElement(target, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false },
            { left: "\\[", right: "\\]", display: true },
            { left: "\\(", right: "\\)", display: false }
          ],
          ignoredClasses: ["katex", "katex-html", "katex-display", "inline-simulation-wrapper"],
          throwOnError: false
        });
      } catch (e) {
        console.warn("Math auto-render notice:", e);
      }
    }
  }
  triggerMath();
  if (!window.renderMathInElement) {
    let t = 0;
    const itv = setInterval(() => {
      t++;
      if (window.renderMathInElement) {
        clearInterval(itv);
        triggerMath();
      } else if (t > 20) {
        clearInterval(itv);
      }
    }, 150);
  }
});
