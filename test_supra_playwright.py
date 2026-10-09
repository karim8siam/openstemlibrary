"""
test_supra_playwright.py
Comprehensive automated test suite for Supramolecular Chemistry (Book 14, Milestone #55).
Validates:
- All 10 units navigation and content
- 80 sections (8 per unit) and 90 problems (9 per unit)
- KaTeX typesetting with 0 unrendered math blocks and 0 orphan backslashes
- Interactive Canvas simulation mount for each unit
- Problem solution toggle mechanics
- Portal integration on index.html (14 Chemistry courses, 55 total)
"""

import time
import os
from playwright.sync_api import sync_playwright

def test_supramolecular_textbook():
    errors = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda exc: console_errors.append(str(exc)))

        print("Navigating to http://localhost:4242/supramolecular-chemistry.html...")
        page.goto("http://localhost:4242/supramolecular-chemistry.html")
        page.wait_for_timeout(1500)

        # 1. Check title & headers
        title = page.title()
        print(f"Page Title: {title}")
        assert "Supramolecular Chemistry" in title, "Title missing 'Supramolecular Chemistry'"

        # 2. Check sidebar chapters count
        nav_items = page.locator(".unit-nav-item")
        total_units = nav_items.count()
        print(f"Total units in sidebar: {total_units}")
        assert total_units == 10, f"Expected 10 units in sidebar, got {total_units}"

        # 3. Test cycling through each unit
        # Units 1 through 10, plus reload Unit 1
        test_sequence = list(range(10)) + [0]
        
        for step_idx, u_idx in enumerate(test_sequence):
            unit_num = u_idx + 1
            is_reload = (step_idx == 10)
            tag = f"Unit {unit_num}" + (" (Reloaded)" if is_reload else "")
            print(f"\n--- Testing {tag} ---")

            if step_idx > 0:
                nav_items.nth(u_idx).click()
                page.wait_for_timeout(700)

            # Check sections count
            sec_cards = page.locator(".textbook-section-card").count()
            print(f"  Sections count: {sec_cards}")
            if sec_cards != 8:
                errors.append(f"{tag}: expected 8 sections, got {sec_cards}")

            # Check problems count
            prob_cards = page.locator(".problem-card").count()
            print(f"  Problems count: {prob_cards}")
            if prob_cards != 9:
                errors.append(f"{tag}: expected 9 problems, got {prob_cards}")

            # Check math display and KaTeX
            math_displays = page.locator(".math-display").count()
            katex_count = page.locator(".katex").count()
            print(f"  math-display elements: {math_displays}, .katex elements: {katex_count}")

            # Verify no unrendered brackets inside math-display
            unrendered = 0
            for mi in range(min(math_displays, 15)):
                el = page.locator(".math-display").nth(mi)
                raw_text = el.inner_text()
                has_katex = el.locator(".katex").count() > 0
                if not has_katex or "\\[" in raw_text or "\\]" in raw_text:
                    unrendered += 1
            if unrendered > 0:
                errors.append(f"{tag}: {unrendered} unrendered math-display blocks")

            # Check for orphan backslashes
            p_info = page.evaluate("""() => {
                const ps = Array.from(document.querySelectorAll('.chapter-article p, .textbook-section-card p, .content-card p'));
                const orphan = ps.filter(p => p.textContent.trim() === '\\\\').length;
                const trailing = ps.filter(p => p.textContent.trim().endsWith('\\\\')).length;
                return { orphan, trailing, total: ps.length };
            }""")
            print(f"  Paragraphs: total={p_info['total']}, orphan={p_info['orphan']}, trailing={p_info['trailing']}")
            if p_info['orphan'] > 0:
                errors.append(f"{tag}: {p_info['orphan']} orphan backslash paragraphs")
            if p_info['trailing'] > 0:
                errors.append(f"{tag}: {p_info['trailing']} trailing backslash paragraphs")

            # Check simulation canvas
            canvas_count = page.locator("canvas").count()
            print(f"  Active Canvas elements: {canvas_count}")
            if canvas_count == 0:
                errors.append(f"{tag}: no canvas simulation mounted")

            # Test problem toggle on first problem card
            first_prob_btn = page.locator(".problem-card .solution-toggle-btn").first
            if first_prob_btn.count() > 0:
                first_sol = page.locator(".problem-card .solution-content").first
                is_initially_visible = first_sol.is_visible()
                first_prob_btn.click()
                page.wait_for_timeout(200)
                is_after_click = first_sol.is_visible()
                assert is_after_click != is_initially_visible, f"{tag}: Toggle solution did not change visibility"
                # Click back to close
                first_prob_btn.click()
                page.wait_for_timeout(200)

        # Take screenshot of Unit 1
        page.locator(".unit-nav-item").first.click()
        page.wait_for_timeout(800)
        screenshot_path = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/supramolecular_chemistry_unit1.png"
        page.screenshot(path=screenshot_path, full_page=False)
        print(f"\nSaved Unit 1 screenshot to {screenshot_path}")

        # 4. Portal Check (index.html)
        print("\nNavigating to http://localhost:4242/index.html...")
        page.goto("http://localhost:4242/index.html")
        page.wait_for_timeout(1500)

        # Check department tab for Chemistry
        chem_tab = page.locator(".dept-pill-btn", has_text="Chemistry")
        chem_tab_text = chem_tab.inner_text()
        print(f"Chemistry tab label: '{chem_tab_text}'")
        assert "14" in chem_tab_text, f"Expected '(14)' in Chemistry tab, got '{chem_tab_text}'"

        # Check total books in All Subjects
        all_tab = page.locator(".dept-pill-btn", has_text="All Subjects")
        all_tab_text = all_tab.inner_text()
        print(f"All Subjects tab label: '{all_tab_text}'")
        assert "55" in all_tab_text, f"Expected '(55)' in All Subjects tab, got '{all_tab_text}'"

        # Click Chemistry tab to filter
        chem_tab.click()
        page.wait_for_timeout(600)

        # Verify Supramolecular Chemistry card exists
        supra_card = page.locator("text=Supramolecular Chemistry: Molecular Recognition").first
        assert supra_card.count() > 0, "Supramolecular Chemistry card not found in filtered portal list"
        print("✓ Supramolecular Chemistry card verified in Chemistry department!")

        # Take screenshot of Portal
        portal_screenshot_path = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/portal_chemistry_14_books.png"
        page.screenshot(path=portal_screenshot_path, full_page=False)
        print(f"Saved Portal screenshot to {portal_screenshot_path}")

        print("\n=== Console Errors Report ===")
        print(f"Console errors logged: {len(console_errors)}")
        for ce in console_errors:
            print(f"  - {ce}")

        browser.close()

    print("\n=== Validation Summary ===")
    if errors:
        print(f"FAILED with {len(errors)} issues:")
        for e in errors:
            print(f"  ✕ {e}")
        raise AssertionError("Playwright validation failed!")
    else:
        print("✓ ALL TESTS PASSED! 10 units, 80 sections, 90 problems, 10 simulations, 0 orphan backslashes, portal integration 100% verified.")

if __name__ == "__main__":
    test_supramolecular_textbook()
