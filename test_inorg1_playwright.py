#!/usr/bin/env python3
"""
test_inorg1_playwright.py
Automated Playwright verification test for Inorganic Chemistry I
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

        print("1. Navigating to Inorganic Chemistry I...")
        page.goto("http://localhost:4242/inorganic-chemistry-1.html", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # Verify Title
        title = page.title()
        print(f"Page title: {title}")
        assert "Inorganic Chemistry I" in title, "Page title mismatch!"

        # Verify Header and Subtitle
        course_badge = page.locator(".badge-course").text_content()
        print(f"Badge: {course_badge}")
        assert "Inorganic Chemistry" in course_badge, "Badge mismatch!"

        # Verify KaTeX rendering
        katex_elements = page.locator(".katex").count()
        print(f"KaTeX math elements found: {katex_elements}")
        assert katex_elements > 0, "No KaTeX math elements rendered!"

        # Verify Table of Contents rendered in sidebar
        nav_items = page.locator(".unit-nav-item").count()
        print(f"TOC unit nav items rendered: {nav_items}")
        assert nav_items == 8, f"Expected 8 TOC nav items, found {nav_items}"

        # Capture Hero & Reader Preview Screenshot
        screenshot_path1 = os.path.join(artifacts_dir, "inorganic_chemistry_1_preview.png")
        page.screenshot(path=screenshot_path1)
        print(f"Saved textbook preview screenshot to {screenshot_path1}")

        # Scroll down to simulation in Section 1.5
        sim_canvas = page.locator("#sim-container-sim_chem_bohr_schrodinger_orbitals-canvas")
        if sim_canvas.count() > 0:
            sim_canvas.scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            screenshot_path2 = os.path.join(artifacts_dir, "inorg1_sim_preview.png")
            sim_canvas.screenshot(path=screenshot_path2)
            print(f"Saved simulation canvas screenshot to {screenshot_path2}")
        else:
            print("Warning: Canvas not found")

        # Verify Problem Solution Toggle
        sol_btn = page.locator(".solution-toggle-btn").first
        assert sol_btn.count() > 0, "No solution toggle buttons found!"
        sol_content = page.locator(".solution-content").first
        assert not sol_content.is_visible(), "Solution should be hidden initially"
        sol_btn.click()
        page.wait_for_timeout(300)
        assert sol_content.is_visible(), "Solution failed to toggle visible!"
        print("Solution toggle tested successfully.")

        # Test Unit Switching (Click Unit 2 in Sidebar)
        unit2_nav = page.locator(".unit-nav-item").nth(1)
        unit2_nav.click()
        page.wait_for_timeout(800)
        unit_title = page.locator("#unit-title").text_content()
        print(f"Unit 2 title after navigation: {unit_title}")
        assert "Periodicity" in unit_title or "Unit 2" in unit_title, "Unit 2 navigation failed!"

        # Test index.html
        print("2. Navigating to index.html...")
        page.goto("http://localhost:4242/index.html", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # Check badge for 43 textbooks
        live_badge = page.locator(".collab-status-badge.live").first.text_content()
        print(f"Live badge in index.html: {live_badge}")
        assert "43" in live_badge, "Badge does not state 43 textbooks!"

        # Verify Chemistry department card
        chem_card = page.locator("#departments-container").locator("text=Chemistry").first
        assert chem_card.count() > 0, "Chemistry department card not found!"
        print("index.html 43 textbooks and Chemistry department verified.")

        browser.close()
        print("ALL PLAYWRIGHT TESTS PASSED WITH 100% SUCCESS!")

if __name__ == "__main__":
    run_tests()
