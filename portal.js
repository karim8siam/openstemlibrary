// Portal Application Logic — Worldwide SEO Edition
// Renders department courses, search filtering, category tabs, and email clipboard utilities

document.addEventListener("DOMContentLoaded", () => {
  const catalog = window.LIBRARY_CATALOG;
  const DEFAULT_CARDS_PER_DEPT = 6;
  const deptExpandedState = {};
  let activeDeptFilter = "all";
  let searchKeyword = "";

  renderDepartmentFilters();
  renderCourses();
  initSearchInput();
  initEmailClipboard();

  // 1. Render Department Tabs with dynamic book counts
  function renderDepartmentFilters() {
    const tabsContainer = document.getElementById("dept-filter-tabs");
    if (!tabsContainer) return;

    tabsContainer.innerHTML = "";

    const activeDepts = catalog.departments.filter(d => 
      d.courses.some(c => c.status === "AVAILABLE")
    );

    const totalBooks = activeDepts.reduce((sum, d) => 
      sum + d.courses.filter(c => c.status === "AVAILABLE").length, 0
    );

    // "All Departments" tab
    const allBtn = document.createElement("button");
    allBtn.className = `dept-pill-btn ${activeDeptFilter === "all" ? 'active' : ''}`;
    allBtn.dataset.dept = "all";
    allBtn.innerText = `🌐 All Subjects (${totalBooks})`;
    allBtn.addEventListener("click", () => selectDept("all"));
    tabsContainer.appendChild(allBtn);

    // Individual Department tabs
    activeDepts.forEach(dept => {
      const availCount = dept.courses.filter(c => c.status === "AVAILABLE").length;
      const btn = document.createElement("button");
      btn.className = `dept-pill-btn ${activeDeptFilter === dept.id ? 'active' : ''}`;
      btn.dataset.dept = dept.id;
      btn.innerText = `${dept.icon} ${dept.name} (${availCount})`;
      btn.addEventListener("click", () => selectDept(dept.id));
      tabsContainer.appendChild(btn);
    });
  }

  function selectDept(deptId) {
    activeDeptFilter = deptId;
    document.querySelectorAll(".dept-pill-btn").forEach(btn => {
      btn.classList.toggle("active", btn.dataset.dept === deptId);
    });
    renderCourses();
  }

  // 2. Render Courses by Department with 6-Card Limit & "See More" Controls
  function renderCourses() {
    const container = document.getElementById("departments-container");
    if (!container) return;

    container.innerHTML = "";

    const deptsToRender = catalog.departments.filter(d => {
      if (activeDeptFilter === "all") return true;
      return d.id === activeDeptFilter;
    });

    let totalCoursesRendered = 0;
    const isSearching = searchKeyword.length > 0;

    deptsToRender.forEach(dept => {
      // Filter courses in department: ONLY AVAILABLE courses, matched by search
      const availableCourses = dept.courses.filter(c => c.status === "AVAILABLE");
      const filteredCourses = availableCourses.filter(course => {
        if (!isSearching) return true;
        const q = searchKeyword.toLowerCase();
        const matchTitle = course.title.toLowerCase().includes(q);
        const matchSubtitle = (course.subtitle || "").toLowerCase().includes(q);
        const matchDesc = course.description.toLowerCase().includes(q);
        const matchKeywords = (course.seoKeywords || "").toLowerCase().includes(q);
        const matchTopic = course.topics.some(t => t.toLowerCase().includes(q));
        return matchTitle || matchSubtitle || matchDesc || matchKeywords || matchTopic;
      });

      if (filteredCourses.length === 0) return;

      totalCoursesRendered += filteredCourses.length;

      // Department Section Element
      const deptSection = document.createElement("section");
      deptSection.className = "department-block";
      deptSection.id = `dept-${dept.id}`;

      // Section Header
      deptSection.innerHTML = `
        <div class="department-header">
          <div class="department-title-wrap">
            <span class="dept-icon">${dept.icon}</span>
            <div>
              <h2 class="dept-title">${dept.name}</h2>
              <p class="dept-desc">${dept.description}</p>
            </div>
          </div>
          <span class="dept-count-badge">${filteredCourses.length} Textbooks Live</span>
        </div>
        <div class="courses-grid" id="grid-${dept.id}"></div>
      `;

      container.appendChild(deptSection);

      const gridEl = deptSection.querySelector(`#grid-${dept.id}`);
      const hasExcess = (activeDeptFilter === "all") && !isSearching && filteredCourses.length > DEFAULT_CARDS_PER_DEPT;
      const isExpanded = Boolean(deptExpandedState[dept.id]);

      // Render Course Cards
      filteredCourses.forEach((c, index) => {
        const isAvailable = c.status === "AVAILABLE";
        const card = document.createElement("div");
        const isExtra = hasExcess && index >= DEFAULT_CARDS_PER_DEPT;

        card.className = `course-card ${isAvailable ? 'available' : ''} ${isExtra ? 'course-card-extra' : ''} ${isExtra && !isExpanded ? 'card-extra-hidden' : ''}`;

        const topicsHtml = c.topics.map(t => `<span class="topic-tag">${t}</span>`).join("");
        const badgeLabel = c.badge || (isAvailable ? '✓ Full Interactive Textbook Live' : '⏳ In Development');

        card.innerHTML = `
          <div class="course-top-meta">
            <span class="course-code-badge">${dept.name}</span>
            <span class="status-badge ${isAvailable ? 'available' : 'coming-soon'}">
              ${badgeLabel}
            </span>
          </div>
          <h3 class="course-title">${c.title}</h3>
          ${c.subtitle ? `<div style="font-size:0.85rem; color:#38bdf8; font-weight:600; margin-top:-0.4rem; margin-bottom:0.75rem;">${c.subtitle}</div>` : ''}
          <p class="course-description">${c.description}</p>
          <div class="course-stats-bar">
            <span class="stat-item">⚡ <strong>Interactive Simulations</strong></span>
            <span class="stat-item">📝 <strong>Solved Problem Sets</strong></span>
            <span class="stat-item">🌐 <strong>100% Free</strong></span>
          </div>
          <div class="course-topics-tags">
            ${topicsHtml}
          </div>
          ${isAvailable ? `
            <a href="${c.url}" class="btn-open-course primary" title="Read ${c.title} Online">
              <span>Read Textbook & Simulations</span>
              <span>→</span>
            </a>
          ` : `
            <button class="btn-open-course disabled" disabled>
              <span>Textbook in Writing • Coming Soon</span>
            </button>
          `}
        `;

        gridEl.appendChild(card);
      });

      // Render "See More / Show Less" Controller if department has more than 6 books and not searching
      if (hasExcess) {
        const excessCount = filteredCourses.length - DEFAULT_CARDS_PER_DEPT;
        const seeMoreWrap = document.createElement("div");
        seeMoreWrap.className = "dept-see-more-wrap";
        seeMoreWrap.id = `see-more-wrap-${dept.id}`;

        seeMoreWrap.innerHTML = `
          <div class="dept-showing-meta">
            Showing <strong class="meta-current-count">${isExpanded ? filteredCourses.length : DEFAULT_CARDS_PER_DEPT}</strong> of <strong>${filteredCourses.length}</strong> textbooks in ${dept.name}
          </div>
          <button class="btn-see-more ${isExpanded ? 'is-expanded' : ''}" data-dept="${dept.id}" aria-expanded="${isExpanded}">
            <span class="btn-see-more-icon">${isExpanded ? '▲' : '📂'}</span>
            <span class="btn-see-more-text">${isExpanded ? `Show Fewer Textbooks (Collapse to ${DEFAULT_CARDS_PER_DEPT})` : `See More ${dept.name} Textbooks (+${excessCount} More)`}</span>
            <span class="btn-see-more-arrow">${isExpanded ? '↑' : '↓'}</span>
          </button>
        `;

        const toggleBtn = seeMoreWrap.querySelector(".btn-see-more");
        toggleBtn.addEventListener("click", () => {
          const currentlyExpanded = Boolean(deptExpandedState[dept.id]);
          const nextExpanded = !currentlyExpanded;
          deptExpandedState[dept.id] = nextExpanded;

          // Toggle visibility of extra cards
          gridEl.querySelectorAll(".course-card-extra").forEach(extraCard => {
            extraCard.classList.toggle("card-extra-hidden", !nextExpanded);
          });

          // Update toggle button state & texts
          toggleBtn.classList.toggle("is-expanded", nextExpanded);
          toggleBtn.setAttribute("aria-expanded", String(nextExpanded));
          toggleBtn.querySelector(".btn-see-more-icon").innerText = nextExpanded ? '▲' : '📂';
          toggleBtn.querySelector(".btn-see-more-text").innerText = nextExpanded 
            ? `Show Fewer Textbooks (Collapse to ${DEFAULT_CARDS_PER_DEPT})`
            : `See More ${dept.name} Textbooks (+${excessCount} More)`;
          toggleBtn.querySelector(".btn-see-more-arrow").innerText = nextExpanded ? '↑' : '↓';

          // Update meta count text
          seeMoreWrap.querySelector(".meta-current-count").innerText = nextExpanded ? filteredCourses.length : DEFAULT_CARDS_PER_DEPT;

          // If collapsing, smoothly scroll back to the top of this department section
          if (!nextExpanded) {
            deptSection.scrollIntoView({ behavior: "smooth", block: "start" });
          }
        });

        deptSection.appendChild(seeMoreWrap);
      }
    });

    if (totalCoursesRendered === 0) {
      container.innerHTML = `
        <div style="text-align:center; padding: 4rem 1rem; color: #94a3b8;">
          <div style="font-size: 3rem; margin-bottom: 1rem;">🔍</div>
          <h3>No textbooks found matching "${searchKeyword}"</h3>
          <p>Try searching for "Quantum", "Mechanics", "Electricity", "Optics", "Algebra", or select "All Subjects".</p>
        </div>
      `;
    }
  }

  // 3. Search Bar Listener
  function initSearchInput() {
    const input = document.getElementById("portal-search-input");
    if (!input) return;

    input.addEventListener("input", (e) => {
      searchKeyword = e.target.value.trim();
      renderCourses();
    });
  }

  // 4. Contact & Email Utilities
  function initEmailClipboard() {
    const copyBtn = document.getElementById("btn-copy-email");
    if (!copyBtn) return;

    copyBtn.addEventListener("click", () => {
      const email = catalog.contactEmail;
      navigator.clipboard.writeText(email).then(() => {
        showPortalToast("✓ Email copied to clipboard: " + email);
        copyBtn.innerText = "Copied!";
        setTimeout(() => {
          copyBtn.innerText = "Copy";
        }, 2500);
      }).catch(() => {
        showPortalToast("Contact email: " + email);
      });
    });
  }

  function showPortalToast(msg) {
    let toast = document.getElementById("portal-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "portal-toast";
      toast.style.cssText = `
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        background: #0f172a;
        color: #38bdf8;
        border: 1px solid #38bdf8;
        padding: 0.85rem 1.5rem;
        border-radius: 8px;
        font-size: 0.88rem;
        font-weight: 600;
        z-index: 1000;
        box-shadow: 0 10px 25px rgba(0,0,0,0.6);
      `;
      document.body.appendChild(toast);
    }
    toast.innerText = msg;
    toast.style.display = "block";
    setTimeout(() => {
      toast.style.display = "none";
    }, 3500);
  }
});
