#!/usr/bin/env python3
"""
test_kinetics_playwright.py
Automated Playwright verification test for Molecular Motion and Reaction Kinetics (Textbook #49)
"""

import sys, os
from playwright.sync_api import sync_playwright

def run_tests():
    artifacts_dir = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9"
    os.makedirs(artifacts_dir, exist_ok=True)

    errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1400, 'height': 900})
        page = context.new_page()

        page.on("pageerror", lambda err: errors.append(f"Page Error: {err}"))
        page.on("console", lambda msg: errors.append(f"Console Error: {msg.text}") if msg.type == "error" else None)

        print("1. Navigating to Molecular Motion & Reaction Kinetics (http://localhost:4242/molecular-motion-kinetics.html)...")
        page.goto("http://localhost:4242/molecular-motion-kinetics.html", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # Verify Title
        title = page.title()
        print(f"Page title: {title}")
        assert "Molecular Motion and Reaction Kinetics" in title, f"Page title mismatch: {title}"

        # Verify Header and Subtitle
        course_badge = page.locator(".badge-course").text_content()
        print(f"Badge: {course_badge}")
        assert "Physical Chemistry" in course_badge or "Chemistry" in course_badge, f"Badge mismatch: {course_badge}"

        # Verify KaTeX rendering
        katex_elements = page.locator(".katex").count()
        print(f"KaTeX math elements found: {katex_elements}")
        assert katex_elements > 0, "No KaTeX math elements rendered!"

        # Verify Table of Contents rendered in sidebar (10 Units)
        nav_items = page.locator(".unit-nav-item").count()
        print(f"TOC unit nav items rendered: {nav_items}")
        assert nav_items == 10, f"Expected 10 TOC nav items, found {nav_items}"

        # Capture Hero & Reader Preview Screenshot
        screenshot_path1 = os.path.join(artifacts_dir, "molecular_motion_kinetics_preview.png")
        page.screenshot(path=screenshot_path1)
        print(f"Saved textbook preview screenshot to {screenshot_path1}")

        # Check simulation canvas in Unit 1
        page.wait_for_timeout(500)
        sim_canvas = page.locator("canvas.sim-canvas").first
        if sim_canvas.count() > 0:
            sim_canvas.scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            screenshot_path2 = os.path.join(artifacts_dir, "kinetics_sim_preview.png")
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

        # Test Unit Switching (Click Unit 2 in Sidebar: Ion Transport & Electrolytic Conduction)
        page.evaluate("document.querySelectorAll('.unit-nav-item')[1].click()")
        page.wait_for_timeout(800)
        unit2_title = page.locator("#unit-title").text_content()
        print(f"Unit 2 title after navigation: {unit2_title}")
        assert "Ion Transport" in unit2_title or "Electrolytic" in unit2_title, f"Unit 2 navigation title mismatch: {unit2_title}"

        # Test Unit 3 Switching (Diffusion Phenomena & Brownian Motion)
        page.evaluate("document.querySelectorAll('.unit-nav-item')[2].click()")
        page.wait_for_timeout(800)
        unit3_title = page.locator("#unit-title").text_content()
        print(f"Unit 3 title after navigation: {unit3_title}")
        assert "Diffusion" in unit3_title, f"Unit 3 navigation title mismatch: {unit3_title}"

        # Test Unit 7 Switching (Unimolecular Reactions)
        page.evaluate("document.querySelectorAll('.unit-nav-item')[6].click()")
        page.wait_for_timeout(800)
        unit7_title = page.locator("#unit-title").text_content()
        print(f"Unit 7 title after navigation: {unit7_title}")
        assert "Unimolecular" in unit7_title, f"Unit 7 navigation title mismatch: {unit7_title}"

        # Test Unit 9 Switching (Catalytic Systems, Enzymes & Oscillations)
        page.evaluate("document.querySelectorAll('.unit-nav-item')[8].click()")
        page.wait_for_timeout(800)
        unit9_title = page.locator("#unit-title").text_content()
        print(f"Unit 9 title after navigation: {unit9_title}")
        assert "Catalytic" in unit9_title or "Enzymatic" in unit9_title, f"Unit 9 navigation title mismatch: {unit9_title}"

        # Test Unit 10 Switching (Molecular Reaction Dynamics)
        page.evaluate("document.querySelectorAll('.unit-nav-item')[9].click()")
        page.wait_for_timeout(800)
        unit10_title = page.locator("#unit-title").text_content()
        print(f"Unit 10 title after navigation: {unit10_title}")
        assert "Molecular Reaction Dynamics" in unit10_title, f"Unit 10 navigation title mismatch: {unit10_title}"

        # Check for uncaught runtime errors during textbook navigation
        if errors:
            print(f"Warning: Runtime errors encountered: {errors}")
        assert len([e for e in errors if "Failed to load resource" not in e]) == 0, f"Critical errors found: {errors}"

        # 2. Test Home Portal Integration (index.html)
        print("\n2. Navigating to Home Portal (http://localhost:4242/index.html)...")
        page.goto("http://localhost:4242/index.html", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # Verify live textbook count badge
        badge_text = page.locator(".collab-status-badge.live").first.text_content()
        print(f"Portal badge: {badge_text}")
        assert "49 Textbooks" in badge_text, f"Expected '49 Textbooks' in badge, got: {badge_text}"

        btn_text = page.locator(".collab-btn-active").first.text_content()
        print(f"Portal CTA button: {btn_text}")
        assert "49 Live Textbooks" in btn_text, f"Expected '49 Live Textbooks' in button, got: {btn_text}"

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
        assert card_count == 8, f"Expected 8 courses in Chemistry department, got {card_count}"

        # Check specifically for molecular-motion-kinetics link
        kinetics_card = page.locator("a[href='molecular-motion-kinetics.html']")
        print(f"Molecular Motion & Reaction Kinetics card found: {kinetics_card.count()}")
        assert kinetics_card.count() > 0, "Molecular Motion & Reaction Kinetics card link not found on portal!"

        screenshot_path3 = os.path.join(artifacts_dir, "chemistry_department_8_books.png")
        page.screenshot(path=screenshot_path3)
        print(f"Saved Chemistry department 8 books screenshot to {screenshot_path3}")

        browser.close()
        print("\nALL PLAYWRIGHT TESTS PASSED CLEANLY!")

if __name__ == "__main__":
    run_tests()
