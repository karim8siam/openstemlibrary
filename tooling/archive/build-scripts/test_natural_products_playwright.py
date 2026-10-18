#!/usr/bin/env python3
"""
test_natural_products_playwright.py
Automated Playwright verification test for Chemistry of Natural Products (Textbook #50)
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

        print("1. Navigating to Chemistry of Natural Products (http://localhost:4242/natural-products-chemistry.html)...")
        page.goto("http://localhost:4242/natural-products-chemistry.html", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # Verify Title
        title = page.title()
        print(f"Page title: {title}")
        assert "Chemistry of Natural Products" in title, f"Page title mismatch: {title}"

        # Verify Header and Subtitle
        course_badge = page.locator(".badge-course").text_content()
        print(f"Badge: {course_badge}")
        assert "Natural Products" in course_badge or "Chemistry" in course_badge, f"Badge mismatch: {course_badge}"

        # Verify KaTeX rendering
        katex_elements = page.locator(".katex").count()
        print(f"KaTeX math elements found: {katex_elements}")
        assert katex_elements > 0, "No KaTeX math elements rendered!"

        # Verify Table of Contents rendered in sidebar (10 Units)
        nav_items = page.locator(".unit-nav-item").count()
        print(f"TOC unit nav items rendered: {nav_items}")
        assert nav_items == 10, f"Expected 10 TOC nav items, found {nav_items}"

        # Capture Hero & Reader Preview Screenshot
        screenshot_path1 = os.path.join(artifacts_dir, "natural_products_preview.png")
        page.screenshot(path=screenshot_path1)
        print(f"Saved textbook preview screenshot to {screenshot_path1}")

        # Check simulation canvas in Unit 1
        page.wait_for_timeout(500)
        sim_canvas = page.locator("canvas.sim-canvas").first
        if sim_canvas.count() > 0:
            sim_canvas.scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            screenshot_path2 = os.path.join(artifacts_dir, "natural_products_sim_preview.png")
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

        # Test Unit Switching (Click Unit 2 in Sidebar: Acyclic Monoterpenoids)
        page.evaluate("document.querySelectorAll('.unit-nav-item')[1].click()")
        page.wait_for_timeout(800)
        unit2_title = page.locator("#unit-title").text_content()
        print(f"Unit 2 title after navigation: {unit2_title}")
        assert "Acyclic Monoterpenoids" in unit2_title or "Isoprene" in unit2_title, f"Unit 2 navigation title mismatch: {unit2_title}"

        # Test Unit 3 Switching (Monocyclic & Sesquiterpenoids)
        page.evaluate("document.querySelectorAll('.unit-nav-item')[2].click()")
        page.wait_for_timeout(800)
        unit3_title = page.locator("#unit-title").text_content()
        print(f"Unit 3 title after navigation: {unit3_title}")
        assert "Monocyclic" in unit3_title or "Sesquiterpenoids" in unit3_title, f"Unit 3 navigation title mismatch: {unit3_title}"

        # Test Unit 4 Switching (Monosaccharides)
        page.evaluate("document.querySelectorAll('.unit-nav-item')[3].click()")
        page.wait_for_timeout(800)
        unit4_title = page.locator("#unit-title").text_content()
        print(f"Unit 4 title after navigation: {unit4_title}")
        assert "Monosaccharides" in unit4_title or "Mutarotation" in unit4_title, f"Unit 4 navigation title mismatch: {unit4_title}"

        # Test Unit 6 Switching (Amino Acids & Peptides)
        page.evaluate("document.querySelectorAll('.unit-nav-item')[5].click()")
        page.wait_for_timeout(800)
        unit6_title = page.locator("#unit-title").text_content()
        print(f"Unit 6 title after navigation: {unit6_title}")
        assert "Amino Acids" in unit6_title or "Peptides" in unit6_title, f"Unit 6 navigation title mismatch: {unit6_title}"

        # Test Unit 8 Switching (Alkaloids)
        page.evaluate("document.querySelectorAll('.unit-nav-item')[7].click()")
        page.wait_for_timeout(800)
        unit8_title = page.locator("#unit-title").text_content()
        print(f"Unit 8 title after navigation: {unit8_title}")
        assert "Alkaloids" in unit8_title, f"Unit 8 navigation title mismatch: {unit8_title}"

        # Test Unit 10 Switching (Antibiotics)
        page.evaluate("document.querySelectorAll('.unit-nav-item')[9].click()")
        page.wait_for_timeout(800)
        unit10_title = page.locator("#unit-title").text_content()
        print(f"Unit 10 title after navigation: {unit10_title}")
        assert "Antibiotics" in unit10_title, f"Unit 10 navigation title mismatch: {unit10_title}"

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
        assert "50 Textbooks" in badge_text, f"Expected '50 Textbooks' in badge, got: {badge_text}"

        btn_text = page.locator(".collab-btn-active").first.text_content()
        print(f"Portal CTA button: {btn_text}")
        assert "50 Live Textbooks" in btn_text, f"Expected '50 Live Textbooks' in button, got: {btn_text}"

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
        assert card_count == 9, f"Expected 9 courses in Chemistry department, got {card_count}"

        # Check specifically for natural-products-chemistry link
        nat_card = page.locator("a[href='natural-products-chemistry.html']")
        print(f"Chemistry of Natural Products card found: {nat_card.count()}")
        assert nat_card.count() > 0, "Chemistry of Natural Products card link not found on portal!"

        screenshot_path3 = os.path.join(artifacts_dir, "chemistry_department_9_books.png")
        page.screenshot(path=screenshot_path3)
        print(f"Saved Chemistry department 9 books screenshot to {screenshot_path3}")

        browser.close()
        print("\nALL PLAYWRIGHT TESTS PASSED CLEANLY!")

if __name__ == "__main__":
    run_tests()
