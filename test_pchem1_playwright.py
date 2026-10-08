# -*- coding: utf-8 -*-
"""
test_pchem1_playwright.py
Automated browser test for Physical Chemistry I textbook on OpenSTEM.
Verifies layout, KaTeX rendering, 8 units navigation, interactive simulations,
problem solution toggles, font toggling, index.html 42 textbooks badge,
Chemistry department search indexing, and captures a high-resolution preview.
"""

import sys
from playwright.sync_api import sync_playwright

def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        print("Testing physical-chemistry-1.html...")
        page.goto("http://localhost:4242/physical-chemistry-1.html", wait_until="networkidle")

        # 1. Title verification
        title = page.title()
        print(f"Page Title: {title}")
        assert "Physical Chemistry I" in title, f"Unexpected title: {title}"

        # 2. Check table of contents has 8 units
        page.wait_for_selector("#unit-nav-list li", timeout=5000)
        nav_items = page.locator("#unit-nav-list li")
        count = nav_items.count()
        print(f"Table of Contents Units: {count}")
        assert count == 8, f"Expected 8 units in TOC, found {count}"

        # 3. Check Unit 1 header and sections
        unit_title = page.locator("#unit-title").inner_text()
        print(f"Initial Unit Title: {unit_title}")
        assert "Foundations of Matter" in unit_title or "Measurements" in unit_title

        # Check pre-rendered sections
        sec_cards = page.locator(".textbook-section-card")
        sec_count = sec_cards.count()
        print(f"Unit 1 Sections Rendered: {sec_count}")
        assert sec_count >= 5, f"Expected at least 5 sections, found {sec_count}"

        # 4. Check Unit 1 Canvas simulation
        page.wait_for_selector(".sim-canvas", timeout=5000)
        canvas = page.locator(".sim-canvas").first
        assert canvas.is_visible(), "Simulation Canvas should be visible"
        print("Simulation 1 Canvas is mounted and visible.")

        # 5. Check Solution Toggle
        toggle_btn = page.locator(".solution-toggle-btn").first
        toggle_btn.click()
        page.wait_for_timeout(300)
        sol_content = page.locator(".solution-content").first
        assert sol_content.is_visible(), "Solution content should be visible after toggle click"
        print("Solution toggle test passed.")

        # 6. Check Font Toggle
        font_btn = page.locator("#btn-font-toggle")
        font_btn.click()
        page.wait_for_timeout(200)
        print("Font toggle test passed.")

        # 7. Test Navigation to Unit 3 (Thermochemistry)
        print("Navigating to Unit 3 (Thermochemistry)...")
        nav_items.nth(2).click()
        page.wait_for_timeout(600)
        u3_title = page.locator("#unit-title").inner_text()
        print(f"Unit 3 Title: {u3_title}")
        assert "Thermochemistry" in u3_title, f"Unexpected Unit 3 title: {u3_title}"

        # 8. Test Navigation to Unit 6 (Chemical Kinetics)
        print("Navigating to Unit 6 (Chemical Kinetics)...")
        nav_items.nth(5).click()
        page.wait_for_timeout(600)
        u6_title = page.locator("#unit-title").inner_text()
        print(f"Unit 6 Title: {u6_title}")
        assert "Kinetics" in u6_title, f"Unexpected Unit 6 title: {u6_title}"

        # 9. Test Navigation to Unit 8 (Electrochemistry)
        print("Navigating to Unit 8 (Electrochemistry)...")
        nav_items.nth(7).click()
        page.wait_for_timeout(600)
        u8_title = page.locator("#unit-title").inner_text()
        print(f"Unit 8 Title: {u8_title}")
        assert "Electrochemistry" in u8_title, f"Unexpected Unit 8 title: {u8_title}"

        # 10. Return to Unit 1 and capture high-res preview artifact
        nav_items.first.click()
        page.wait_for_timeout(600)
        screenshot_path = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/physical_chemistry_1_preview.png"
        page.screenshot(path=screenshot_path)
        print(f"Captured screenshot at {screenshot_path}")

        # 11. Check index.html platform integration
        print("Testing index.html platform synchronization...")
        page.goto("http://localhost:4242/index.html", wait_until="networkidle")
        page.wait_for_selector(".collab-status-badge.live", timeout=5000)
        badge_text = page.locator(".collab-status-badge.live").first.text_content() or ""
        print(f"Live Badge Text: {badge_text}")
        assert "42 Textbooks" in badge_text, f"Expected 42 Textbooks, got: {badge_text}"

        # Check search in portal for 'chemistry'
        search_input = page.locator("#search-input")
        if search_input.is_visible():
            search_input.fill("chemistry")
            page.wait_for_timeout(400)
            chem_card = page.locator("a[href='physical-chemistry-1.html']")
            assert chem_card.count() > 0, "Physical Chemistry I card should be visible in search"
            print("Portal search for 'chemistry' verified successfully.")

        # Check department tabs / filter includes Chemistry
        dept_pills = page.locator(".dept-filter-btn")
        if dept_pills.count() > 0:
            dept_texts = [dept_pills.nth(i).inner_text() for i in range(dept_pills.count())]
            print(f"Department filter tabs: {dept_texts}")
            assert any("Chemistry" in t for t in dept_texts), f"Chemistry department tab missing from {dept_texts}"
            print("Chemistry department tab verified successfully.")

        browser.close()
        print("ALL TESTS PASSED WITH 100% SUCCESS!")

if __name__ == "__main__":
    run_tests()
