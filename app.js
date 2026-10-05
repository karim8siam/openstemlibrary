// Quantum Mechanics I Textbook Edition Controller
// Manages textbook sections, search indexing, simulations lifecycle, KaTeX rendering, study timer, and protective guards

function startApp() {
  let activeUnitIndex = 0;

  // Initialize App
  initSidebar();
  loadChapter(0);
  initAntiCopyGuards();
  initFontToggle();
  initSearch();

  // 1. Sidebar Setup
  function initSidebar() {
    const listEl = document.getElementById("unit-nav-list");
    listEl.innerHTML = "";

    window.COURSE_DATA.units.forEach((unit, idx) => {
      const li = document.createElement("li");
      li.className = `unit-nav-item ${idx === 0 ? 'active' : ''}`;
      li.dataset.unitIndex = idx;
      li.innerHTML = `
        <span class="unit-nav-num">Ch.${unit.number || unit.unitNumber || (idx + 1)}</span>
        <span class="unit-nav-text">${unit.title}</span>
      `;
      li.addEventListener("click", () => {
        document.querySelectorAll(".unit-nav-item").forEach(item => item.classList.remove("active"));
        li.classList.add("active");
        loadChapter(idx);
        window.scrollTo({ top: 0, behavior: "smooth" });
      });
      listEl.appendChild(li);
    });
  }

  // 2. Load Chapter View
  function loadChapter(unitIndex) {
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
    setTimeout(renderMath, 40);
    setTimeout(renderMath, 200);
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
      }

      let inlineSimHtml = "";
      simTypes.forEach(simType => {
        inlineSimHtml += `
          <div class="inline-simulation-wrapper" style="margin-top: 2.25rem;">
            <div class="simulation-slot" id="sim-container-${simType}"></div>
          </div>
        `;
      });

      card.innerHTML = `
        <header class="sec-header">
          <h3 class="sec-title">
            <span class="sec-num">§${rawNum}</span>
            <span>${sec.heading || sec.title || ""}</span>
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
        }
      }, 60);
    });
  }

  // 5. Render Practice Problems
  function renderProblems(problemList) {
    const container = document.getElementById("problems-mount") || document.getElementById("problems-container");
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
        stepsHtml += `
          <div class="solution-step" style="border-left-color: #10b981;">
            <div class="step-title" style="color: #10b981;">Final Answer & Physical Insight</div>
            <div class="step-explanation">${formatMarkdownContent(prob.answer)}</div>
          </div>
        `;
      }

      card.innerHTML = `
        <div class="problem-header">
          <div class="problem-title-box">
            <span class="diff-badge ${diffClass}">${diffLabel}</span>
            <strong>${prob.title.includes('Example') ? prob.title : `Example ${activeUnitIndex + 1}.${idx + 1}: ${prob.title}`}</strong>
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
        toggleBtn.addEventListener("click", () => {
          const isOpen = solContent.classList.toggle("open");
          toggleBtn.innerText = isOpen ? "🙈 Hide Solution" : "👁️ Reveal Complete Derivation & Solution";
          if (isOpen) renderMath();
        });
      }
    });
  }

  // 6. Comprehensive Text Formatter (Markdown to HTML)
  function formatMarkdownContent(text) {
    if (!text) return "";
    
    // If already pre-structured semantic HTML with tags, return directly
    if (text.includes("<h4") || text.includes("<p>") || text.includes("<ul") || text.includes("<ol") || text.includes("<div")) {
      return text;
    }

    let clean = text.replace(/\r\n/g, "\n").trim();
    
    // Isolate $$...$$
    clean = clean.replace(/\$\$(.*?)\$\$/gs, function(match, math) {
      return "\n\n<div class=\"math-display\">$$" + math.trim() + "$$</div>\n\n";
    });

    const lines = clean.split("\n");
    const output = [];
    let inUl = false;
    let inOl = false;
    let paraLines = [];

    function flushPara() {
      if (paraLines.length > 0) {
        let p = paraLines.join(" ").trim();
        if (p) output.push("<p>" + p + "</p>");
        paraLines = [];
      }
    }

    function closeLists() {
      if (inUl) { output.push("</ul>"); inUl = false; }
      if (inOl) { output.push("</ol>"); inOl = false; }
    }

    lines.forEach(function(line) {
      let s = line.trim();
      if (!s) {
        flushPara();
        closeLists();
        return;
      }

      if (s.startsWith("<div") || (s.startsWith("$$") && s.endsWith("$$"))) {
        flushPara();
        closeLists();
        output.push(s.startsWith("<div") ? s : "<div class=\"math-display\">" + s + "</div>");
        return;
      }

      if (s.startsWith("### ")) {
        flushPara();
        closeLists();
        output.push("<h4>" + s.substring(4).trim() + "</h4>");
        return;
      }

      if (s.startsWith("#### ")) {
        flushPara();
        closeLists();
        output.push("<h5>" + s.substring(5).trim() + "</h5>");
        return;
      }

      if (s.startsWith("- ") || s.startsWith("* ")) {
        flushPara();
        if (inOl) { output.push("</ol>"); inOl = false; }
        if (!inUl) { output.push("<ul>"); inUl = true; }
        let item = s.substring(2).trim()
          .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
          .replace(/\*(.*?)\*/g, "<em>$1</em>");
        output.push("  <li>" + item + "</li>");
        return;
      }

      const olMatch = s.match(/^([0-9]+)\.\s+(.*)$/);
      if (olMatch) {
        let num = olMatch[1];
        let body = olMatch[2].trim();
        if (!inOl && (body.startsWith("**") || body.includes("Method") || body.includes("Law") || body.includes("Equation") || body.includes("Nature") || body.includes("Criteria") || body.includes("Equilibrium"))) {
          flushPara();
          closeLists();
          let cleanTitle = body.replace(/\*\*/g, "");
          output.push("<h4>" + num + ". " + cleanTitle + "</h4>");
          return;
        } else {
          flushPara();
          if (inUl) { output.push("</ul>"); inUl = false; }
          if (!inOl) { output.push("<ol>"); inOl = true; }
          let item = body
            .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
            .replace(/\*(.*?)\*/g, "<em>$1</em>");
          output.push("  <li>" + item + "</li>");
          return;
        }
      }

      closeLists();
      let formattedLine = s
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        .replace(/\*(.*?)\*/g, "<em>$1</em>");
      paraLines.push(formattedLine);
    });

    flushPara();
    closeLists();

    return output.join("\n\n");
  }

  // 7. Math Rendering with KaTeX
  function renderMath() {
    function execRender() {
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
            throwOnError: false
          });
        } catch (e) {
          console.warn("Math auto-render notice:", e);
        }
      }
    }

    execRender();
    if (!window.renderMathInElement) {
      let tries = 0;
      const timer = setInterval(() => {
        tries++;
        if (window.renderMathInElement) {
          clearInterval(timer);
          execRender();
        } else if (tries > 25) {
          clearInterval(timer);
        }
      }, 100);
    }
  }

  // 8. Anti-Copy & Anti-Download Protection
  function initAntiCopyGuards() {
    // Disable right click
    document.addEventListener("contextmenu", (e) => {
      e.preventDefault();
      showToast("Right-click is protected to support free ad-supported academic access.");
    });

    // Disable keyboard shortcuts for saving or printing
    document.addEventListener("keydown", (e) => {
      if ((e.ctrlKey || e.metaKey) && (e.key === 's' || e.key === 'S' || e.key === 'p' || e.key === 'P')) {
        e.preventDefault();
        showToast("Saving and printing are disabled. Enjoy reading for free online!");
      }
    });
  }

  function showToast(msg) {
    let toast = document.getElementById("app-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "app-toast";
      toast.style.cssText = `
        position: fixed;
        bottom: 75px;
        left: 50%;
        transform: translateX(-50%);
        background: #0f172a;
        color: #38bdf8;
        border: 1px solid #38bdf8;
        padding: 0.65rem 1.25rem;
        border-radius: 8px;
        font-size: 0.82rem;
        z-index: 999;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
      `;
      document.body.appendChild(toast);
    }
    toast.innerText = msg;
    toast.style.display = "block";
    setTimeout(() => {
      toast.style.display = "none";
    }, 3200);
  }

  // 11. Font Toggle (Academic Serif vs Modern Sans)
  function initFontToggle() {
    const btn = document.getElementById("btn-font-toggle");
    if (!btn) return;
    btn.addEventListener("click", () => {
      document.body.classList.toggle("academic-font");
      const isSerif = document.body.classList.contains("academic-font");
      btn.innerText = isSerif ? "Aa Modern" : "Aa Academic";
    });
  }

  // 12. Search & Filter Input
  function initSearch() {
    const input = document.getElementById("topic-search-input");
    if (!input) return;

    input.addEventListener("input", (e) => {
      const term = e.target.value.toLowerCase().trim();
      const items = document.querySelectorAll(".unit-nav-item");

      items.forEach((item, idx) => {
        const unit = window.COURSE_DATA.units[idx];
        const matchTitle = unit.title.toLowerCase().includes(term);
        const matchSections = unit.sections.some(s => s.heading.toLowerCase().includes(term) || s.content.toLowerCase().includes(term));

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
