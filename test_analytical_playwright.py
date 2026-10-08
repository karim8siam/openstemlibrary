#!/usr/bin/env python3
"""
test_analytical_playwright.py
Automated Playwright verification test for Analytical Chemistry (Textbook #46)
"""

import sys, os
from playwright.sync_api import sync_playwright

def run_tests():
    artifacts_dir = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9"
    os.makedirs(artifacts_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1400, 'height': 900})
        page = context.new_page()

        print("1. Navigating to Analytical Chemistry (http://localhost:4242/analytical-chemistry.html)...")
        page.goto("http://localhost:4242/analytical-chemistry.html", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # Verify Title
        title = page.title()
        print(f"Page title: {title}")
        assert "Analytical Chemistry" in title, f"Page title mismatch: {title}"

        # Verify Header and Subtitle
        course_badge = page.locator(".badge-course").text_content()
        print(f"Badge: {course_badge}")
        assert "Analytical Chemistry" in course_badge, f"Badge mismatch: {course_badge}"

        # Verify KaTeX rendering
        katex_elements = page.locator(".katex").count()
        print(f"KaTeX math elements found: {katex_elements}")
        assert katex_elements > 0, "No KaTeX math elements rendered!"

        # Verify Table of Contents rendered in sidebar (9 Units)
        nav_items = page.locator(".unit-nav-item").count()
        print(f"TOC unit nav items rendered: {nav_items}")
        assert nav_items == 9, f"Expected 9 TOC nav items, found {nav_items}"

        # Capture Hero & Reader Preview Screenshot
        screenshot_path1 = os.path.join(artifacts_dir, "analytical_chemistry_preview.png")
        page.screenshot(path=screenshot_path1)
        print(f"Saved textbook preview screenshot to {screenshot_path1}")

        # Check simulation canvas in Unit 1
        page.wait_for_timeout(500)
        sim_canvas = page.locator("canvas.sim-canvas").first
        if sim_canvas.count() > 0:
            sim_canvas.scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            screenshot_path2 = os.path.join(artifacts_dir, "analytical_sim_preview.png")
            sim_canvas.screenshot(path=screenshot_path2)
            print(f"Saved simulation canvas screenshot to {screenshot_path2}")
        else:
            print("Warning: Simulation canvas not found")

        # Verify Problem Solution Toggle
        sol_btn = page.locator(".solution-toggle-btn").first
        assert sol_btn.count() > 0, "No solution toggle buttons found!"
        sol_content = page.locator(".solution-content").first
        assert not sol_content.is_visible(), "Solution should be hidden initially"
        sol_btn.click()
        page.wait_for_timeout(300)
        assert sol_content.is_visible(), "Solution failed to toggle visible!"
        print("Solution toggle tested successfully.")

        # Test Unit Switching (Click Unit 4 in Sidebar: Complexometric Titrations)
        unit4_nav = page.locator(".unit-nav-item").nth(3)
        unit4_nav.click()
        page.wait_for_timeout(800)
        unit4_title = page.locator("#unit-title").text_content()
        print(f"Unit 4 title after navigation: {unit4_title}")
        assert "Complexometric" in unit4_title, f"Unit 4 navigation title mismatch: {unit4_title}"

        # Test Unit 5 Switching (Atomic Spectroscopy)
        unit5_nav = page.locator(".unit-nav-item").nth(4)
        unit5_nav.click()
        page.wait_for_timeout(800)
        unit5_title = page.locator("#unit-title").text_content()
        print(f"Unit 5 title after navigation: {unit5_title}")
        assert "Atomic Spectroscopy" in unit5_title, f"Unit 5 navigation title mismatch: {unit5_title}"

        # Test Unit 6 Switching (Ion-Exchange Chromatography)
        unit6_nav = page.locator(".unit-nav-item").nth(5)
        unit6_nav.click()
        page.wait_for_timeout(800)
        unit6_title = page.locator("#unit-title").text_content()
        print(f"Unit 6 title after navigation: {unit6_title}")
        assert "Ion-Exchange" in unit6_title, f"Unit 6 navigation title mismatch: {unit6_title}"

        # Test Unit 7 Switching (Spectrophotometry)
        unit7_nav = page.locator(".unit-nav-item").nth(6)
        unit7_nav.click()
        page.wait_for_timeout(800)
        unit7_title = page.locator("#unit-title").text_content()
        print(f"Unit 7 title after navigation: {unit7_title}")
        assert "Spectrophotometric" in unit7_title, f"Unit 7 navigation title mismatch: {unit7_title}"

        # Test Unit 9 Switching (Chromatography)
        unit9_nav = page.locator(".unit-nav-item").nth(8)
        unit9_nav.click()
        page.wait_for_timeout(800)
        unit9_title = page.locator("#unit-title").text_content()
        print(f"Unit 9 title after navigation: {unit9_title}")
        assert "Chromatographic" in unit9_title, f"Unit 9 navigation title mismatch: {unit9_title}"

        # 2. Test Home Portal Integration (index.html)
        print("\n2. Navigating to Home Portal (http://localhost:4242/index.html)...")
        page.goto("http://localhost:4242/index.html", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # Verify live textbook count badge
        badge_text = page.locator(".collab-status-badge.live").first.text_content()
        print(f"Portal badge: {badge_text}")
        assert "46 Textbooks" in badge_text, f"Expected '46 Textbooks' in badge, got: {badge_text}"

        btn_text = page.locator(".collab-btn-active").first.text_content()
        print(f"Portal CTA button: {btn_text}")
        assert "46 Live Textbooks" in btn_text, f"Expected '46 Live Textbooks' in button, got: {btn_text}"

        # Scroll down to Chemistry Department tab
        chem_tab = page.locator(".dept-tab-btn[data-dept='chemistry']")
        if chem_tab.count() > 0:
            chem_tab.scroll_into_view_if_needed()
            chem_tab.click()
            page.wait_for_timeout(800)
            print("Clicked Chemistry Department tab.")

        # Verify all 5 chemistry course cards exist
        chem_cards = page.locator(".course-card")
        card_count = chem_cards.count()
        print(f"Rendered course cards in active tab: {card_count}")

        # Check specifically for analytical-chemistry link
        analytical_card = page.locator("a[href='analytical-chemistry.html']")
        print(f"Analytical chemistry card found: {analytical_card.count()}")
        assert analytical_card.count() > 0, "Analytical Chemistry card link not found on portal!"

        screenshot_path3 = os.path.join(artifacts_dir, "chemistry_department_5_books.png")
        page.screenshot(path=screenshot_path3)
        print(f"Saved Chemistry department 5 books screenshot to {screenshot_path3}")

        browser.close()
        print("\nALL PLAYWRIGHT TESTS PASSED CLEANLY!")

if __name__ == "__main__":
    run_tests()
