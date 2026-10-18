#!/usr/bin/env python3
"""
test_org2_playwright.py
Automated Playwright verification test for Organic Chemistry II (Textbook #45)
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

        print("1. Navigating to Organic Chemistry II (http://localhost:4242/organic-chemistry-2.html)...")
        page.goto("http://localhost:4242/organic-chemistry-2.html", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # Verify Title
        title = page.title()
        print(f"Page title: {title}")
        assert "Organic Chemistry II" in title, f"Page title mismatch: {title}"

        # Verify Header and Subtitle
        course_badge = page.locator(".badge-course").text_content()
        print(f"Badge: {course_badge}")
        assert "Organic Chemistry" in course_badge, f"Badge mismatch: {course_badge}"

        # Verify KaTeX rendering
        katex_elements = page.locator(".katex").count()
        print(f"KaTeX math elements found: {katex_elements}")
        assert katex_elements > 0, "No KaTeX math elements rendered!"

        # Verify Table of Contents rendered in sidebar (9 Units)
        nav_items = page.locator(".unit-nav-item").count()
        print(f"TOC unit nav items rendered: {nav_items}")
        assert nav_items == 9, f"Expected 9 TOC nav items, found {nav_items}"

        # Capture Hero & Reader Preview Screenshot
        screenshot_path1 = os.path.join(artifacts_dir, "organic_chemistry_2_preview.png")
        page.screenshot(path=screenshot_path1)
        print(f"Saved textbook preview screenshot to {screenshot_path1}")

        # Check simulation canvas in Unit 1
        page.wait_for_timeout(500)
        sim_canvas = page.locator("canvas.sim-canvas").first
        if sim_canvas.count() > 0:
            sim_canvas.scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            screenshot_path2 = os.path.join(artifacts_dir, "org2_sim_preview.png")
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

        # Test Unit Switching (Click Unit 2 in Sidebar: Aldehydes and Ketones)
        unit2_nav = page.locator(".unit-nav-item").nth(1)
        unit2_nav.click()
        page.wait_for_timeout(800)
        unit2_title = page.locator("#unit-title").text_content()
        print(f"Unit 2 title after navigation: {unit2_title}")
        assert "Aldehydes" in unit2_title or "Ketones" in unit2_title, f"Unit 2 navigation title mismatch: {unit2_title}"

        # Test Unit 6 Switching (Stereochemistry)
        unit6_nav = page.locator(".unit-nav-item").nth(5)
        unit6_nav.click()
        page.wait_for_timeout(800)
        unit6_title = page.locator("#unit-title").text_content()
        print(f"Unit 6 title after navigation: {unit6_title}")
        assert "Stereochemistry" in unit6_title, f"Unit 6 navigation title mismatch: {unit6_title}"

        # Test Unit 8 Switching (Pharmaceuticals)
        unit8_nav = page.locator(".unit-nav-item").nth(7)
        unit8_nav.click()
        page.wait_for_timeout(800)
        unit8_title = page.locator("#unit-title").text_content()
        print(f"Unit 8 title after navigation: {unit8_title}")
        assert "Pharmaceuticals" in unit8_title or "Medicinal" in unit8_title, f"Unit 8 navigation title mismatch: {unit8_title}"

        # Test Unit 9 Switching (Fused Heterocycles)
        unit9_nav = page.locator(".unit-nav-item").nth(8)
        unit9_nav.click()
        page.wait_for_timeout(800)
        unit9_title = page.locator("#unit-title").text_content()
        print(f"Unit 9 title after navigation: {unit9_title}")
        assert "Heterocycles" in unit9_title, f"Unit 9 navigation title mismatch: {unit9_title}"

        # Test index.html
        print("2. Navigating to index.html (http://localhost:4242/index.html)...")
        page.goto("http://localhost:4242/index.html", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # Check badge for 45 textbooks
        live_badge = page.locator(".collab-status-badge.live").first.text_content()
        print(f"Live badge in index.html: {live_badge}")
        assert "45" in live_badge, f"Badge does not state 45 textbooks: {live_badge}"

        # Verify Chemistry department card contains Organic Chemistry II
        chem_text = page.locator("#departments-container").text_content()
        assert "Organic Chemistry II" in chem_text, "Organic Chemistry II not found in departments container!"
        print("Verified Organic Chemistry II in Chemistry department card on index.html.")

        # Verify footer has Organic Chemistry II
        footer_link = page.locator("a.footer-link[href='organic-chemistry-2.html']").first
        assert footer_link.count() > 0, "Organic Chemistry II link missing in footer of index.html!"
        print("Verified Organic Chemistry II footer link in index.html.")

        browser.close()
        print("ALL PLAYWRIGHT TESTS PASSED CLEANLY!")

if __name__ == "__main__":
    run_tests()
