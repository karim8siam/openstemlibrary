#!/usr/bin/env python3
"""
test_nuclear_playwright.py
Automated Playwright verification test for Nuclear and Radiochemistry (Textbook #47)
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

        print("1. Navigating to Nuclear and Radiochemistry (http://localhost:4242/nuclear-radiochemistry.html)...")
        page.goto("http://localhost:4242/nuclear-radiochemistry.html", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # Verify Title
        title = page.title()
        print(f"Page title: {title}")
        assert "Nuclear and Radiochemistry" in title, f"Page title mismatch: {title}"

        # Verify Header and Subtitle
        course_badge = page.locator(".badge-course").text_content()
        print(f"Badge: {course_badge}")
        assert "Nuclear & Radiochemistry" in course_badge, f"Badge mismatch: {course_badge}"

        # Verify KaTeX rendering
        katex_elements = page.locator(".katex").count()
        print(f"KaTeX math elements found: {katex_elements}")
        assert katex_elements > 0, "No KaTeX math elements rendered!"

        # Verify Table of Contents rendered in sidebar (10 Units)
        nav_items = page.locator(".unit-nav-item").count()
        print(f"TOC unit nav items rendered: {nav_items}")
        assert nav_items == 10, f"Expected 10 TOC nav items, found {nav_items}"

        # Capture Hero & Reader Preview Screenshot
        screenshot_path1 = os.path.join(artifacts_dir, "nuclear_radiochemistry_preview.png")
        page.screenshot(path=screenshot_path1)
        print(f"Saved textbook preview screenshot to {screenshot_path1}")

        # Check simulation canvas in Unit 1
        page.wait_for_timeout(500)
        sim_canvas = page.locator("canvas.sim-canvas").first
        if sim_canvas.count() > 0:
            sim_canvas.scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            screenshot_path2 = os.path.join(artifacts_dir, "nuclear_sim_preview.png")
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

        # Test Unit Switching (Click Unit 2 in Sidebar: Atomic Nucleus)
        unit2_nav = page.locator(".unit-nav-item").nth(1)
        unit2_nav.click()
        page.wait_for_timeout(800)
        unit2_title = page.locator("#unit-title").text_content()
        print(f"Unit 2 title after navigation: {unit2_title}")
        assert "Atomic Nucleus" in unit2_title, f"Unit 2 navigation title mismatch: {unit2_title}"

        # Test Unit 4 Switching (Nuclear Reaction Dynamics)
        unit4_nav = page.locator(".unit-nav-item").nth(3)
        unit4_nav.click()
        page.wait_for_timeout(800)
        unit4_title = page.locator("#unit-title").text_content()
        print(f"Unit 4 title after navigation: {unit4_title}")
        assert "Nuclear Reaction" in unit4_title, f"Unit 4 navigation title mismatch: {unit4_title}"

        # Test Unit 5 Switching (Nuclear Fission Mechanics)
        unit5_nav = page.locator(".unit-nav-item").nth(4)
        unit5_nav.click()
        page.wait_for_timeout(800)
        unit5_title = page.locator("#unit-title").text_content()
        print(f"Unit 5 title after navigation: {unit5_title}")
        assert "Nuclear Fission" in unit5_title, f"Unit 5 navigation title mismatch: {unit5_title}"

        # Test Unit 6 Switching (Radiation Interaction with Matter)
        unit6_nav = page.locator(".unit-nav-item").nth(5)
        unit6_nav.click()
        page.wait_for_timeout(800)
        unit6_title = page.locator("#unit-title").text_content()
        print(f"Unit 6 title after navigation: {unit6_title}")
        assert "Radiation Interaction" in unit6_title, f"Unit 6 navigation title mismatch: {unit6_title}"

        # Test Unit 10 Switching (Radiation Dosimetry)
        page.evaluate("document.querySelectorAll('.unit-nav-item')[9].click()")
        page.wait_for_timeout(800)
        unit10_title = page.locator("#unit-title").text_content()
        print(f"Unit 10 title after navigation: {unit10_title}")
        assert "Radiation Dosimetry" in unit10_title, f"Unit 10 navigation title mismatch: {unit10_title}"

        # 2. Test Home Portal Integration (index.html)
        print("\n2. Navigating to Home Portal (http://localhost:4242/index.html)...")
        page.goto("http://localhost:4242/index.html", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # Verify live textbook count badge
        badge_text = page.locator(".collab-status-badge.live").first.text_content()
        print(f"Portal badge: {badge_text}")
        assert "47 Textbooks" in badge_text, f"Expected '47 Textbooks' in badge, got: {badge_text}"

        btn_text = page.locator(".collab-btn-active").first.text_content()
        print(f"Portal CTA button: {btn_text}")
        assert "47 Live Textbooks" in btn_text, f"Expected '47 Live Textbooks' in button, got: {btn_text}"

        # Scroll down and click Chemistry Department tab
        page.evaluate("document.querySelector('.dept-pill-btn[data-dept=\\'chemistry\\']').click()")
        page.wait_for_timeout(800)
        page.evaluate("document.getElementById('departments-container').scrollIntoView()")
        page.wait_for_timeout(500)
        print("Clicked Chemistry Department tab.")

        # Verify course cards
        chem_cards = page.locator(".course-card")
        card_count = chem_cards.count()
        print(f"Rendered course cards in active tab: {card_count}")

        # Check specifically for nuclear-radiochemistry link
        nuclear_card = page.locator("a[href='nuclear-radiochemistry.html']")
        print(f"Nuclear & Radiochemistry card found: {nuclear_card.count()}")
        assert nuclear_card.count() > 0, "Nuclear & Radiochemistry card link not found on portal!"

        screenshot_path3 = os.path.join(artifacts_dir, "chemistry_department_6_books.png")
        page.screenshot(path=screenshot_path3)
        print(f"Saved Chemistry department 6 books screenshot to {screenshot_path3}")

        browser.close()
        print("\nALL PLAYWRIGHT TESTS PASSED CLEANLY!")

if __name__ == "__main__":
    run_tests()
