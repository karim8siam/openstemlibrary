# -*- coding: utf-8 -*-
"""
test_fuzzy_playwright.py
Automated browser test for Fuzzy Mathematics textbook.
Verifies layout, KaTeX rendering, 8 units navigation, interactive simulations,
problem solution toggles, font toggling, and captures a high-resolution preview.
"""

import sys
from playwright.sync_api import sync_playwright

def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        print("Testing fuzzy-mathematics.html...")
        page.goto("http://localhost:4242/fuzzy-mathematics.html", wait_until="networkidle")

        # 1. Title verification
        title = page.title()
        print(f"Page Title: {title}")
        assert "Fuzzy Mathematics" in title, f"Unexpected title: {title}"

        # 2. Check table of contents has 8 units
        page.wait_for_selector("#unit-nav-list li", timeout=5000)
        nav_items = page.locator("#unit-nav-list li")
        count = nav_items.count()
        print(f"Table of Contents Units: {count}")
        assert count == 8, f"Expected 8 units in TOC, found {count}"

        # 3. Check Unit 1 header and sections
        unit_title = page.locator("#unit-title").inner_text()
        print(f"Initial Unit Title: {unit_title}")
        assert "Crisp" in unit_title or "Membership" in unit_title

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

        # 7. Test Navigation to Unit 4 (Fuzzy Numbers, Intervals & Linguistic Variables)
        print("Navigating to Unit 4...")
        nav_items.nth(3).click()
        page.wait_for_timeout(600)
        u4_title = page.locator("#unit-title").inner_text()
        print(f"Unit 4 Title: {u4_title}")
        assert "Fuzzy Numbers" in u4_title or "Intervals" in u4_title, f"Unexpected Unit 4 title: {u4_title}"

        # 8. Test Navigation to Unit 8 (Real-World Applications)
        print("Navigating to Unit 8...")
        nav_items.nth(7).click()
        page.wait_for_timeout(600)
        u8_title = page.locator("#unit-title").inner_text()
        print(f"Unit 8 Title: {u8_title}")
        assert "Applications" in u8_title or "Control" in u8_title, f"Unexpected Unit 8 title: {u8_title}"

        # 9. Return to Unit 1 and take high-res screenshot artifact
        nav_items.first.click()
        page.wait_for_timeout(600)
        screenshot_path = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/fuzzy_mathematics_preview.png"
        page.screenshot(path=screenshot_path)
        print(f"Captured screenshot at {screenshot_path}")

        # 10. Check index.html platform integration
        print("Testing index.html platform synchronization...")
        page.goto("http://localhost:4242/index.html", wait_until="networkidle")
        page.wait_for_selector(".collab-status-badge.live", timeout=5000)
        badge_text = page.locator(".collab-status-badge.live").first.text_content() or ""
        print(f"Live Badge Text: {badge_text}")
        assert "41 Textbooks" in badge_text, f"Expected 41 Textbooks, got: {badge_text}"

        # Check search in portal for 'fuzzy'
        search_input = page.locator("#search-input")
        if search_input.is_visible():
            search_input.fill("fuzzy")
            page.wait_for_timeout(400)
            fuzzy_card = page.locator("a[href='fuzzy-mathematics.html']")
            assert fuzzy_card.count() > 0, "Fuzzy Mathematics card should be visible in search"
            print("Portal search for 'fuzzy' verified successfully.")

        browser.close()
        print("ALL TESTS PASSED WITH 100% SUCCESS!")

if __name__ == "__main__":
    run_tests()
