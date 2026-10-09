# -*- coding: utf-8 -*-
"""
verify_env_live.py
Verification of live Cloudflare Pages deployment for Environmental Chemistry (Book 16, Milestone 57).
"""

import time
from playwright.sync_api import sync_playwright

def verify_live():
    print("Connecting to live production deployment...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda exc: console_errors.append(str(exc)))

        # 1. Verify environmental-chemistry.html live
        live_book_url = "https://openstemlibrary.com/environmental-chemistry.html"
        print(f"Navigating to {live_book_url}...")
        resp = page.goto(live_book_url, wait_until="networkidle")
        print(f"Response status: {resp.status if resp else 'N/A'}")
        page.wait_for_timeout(2000)

        title = page.title()
        print(f"Live Page Title: {title}")
        assert "Environmental Chemistry" in title, f"Title mismatch: {title}"

        # Check units count
        nav_items = page.locator(".unit-nav-item")
        print(f"Sidebar units count: {nav_items.count()}")
        assert nav_items.count() == 10, f"Expected 10 units, got {nav_items.count()}"

        # Check sections and problems in Unit 1
        sec_count = page.locator(".textbook-section-card").count()
        prob_count = page.locator(".problem-card").count()
        canvas_count = page.locator("canvas").count()
        print(f"Unit 1: {sec_count} sections, {prob_count} problems, {canvas_count} active canvas simulations")
        assert sec_count == 8, f"Expected 8 sections, got {sec_count}"
        assert prob_count == 9, f"Expected 9 problems, got {prob_count}"
        assert canvas_count >= 1, f"Expected at least 1 canvas, got {canvas_count}"

        # Take live screenshot of book
        book_screenshot = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/live_environmental_chemistry.png"
        page.screenshot(path=book_screenshot, full_page=False)
        print(f"Saved live book screenshot to {book_screenshot}")

        # 2. Test switching to Unit 10 live
        print("\nTesting Unit 10 switch on live production...")
        page.evaluate("() => document.querySelectorAll('.unit-nav-item')[9].click()")
        page.wait_for_timeout(2000)

        u10_sec = page.locator(".textbook-section-card").count()
        u10_prob = page.locator(".problem-card").count()
        u10_canvas = page.locator("canvas").count()
        u10_katex = page.locator(".katex").count()
        print(f"Unit 10 Live: {u10_sec} sections, {u10_prob} problems, {u10_canvas} canvas, {u10_katex} katex elements")
        assert u10_sec == 8, f"Expected 8 sections in Unit 10, got {u10_sec}"
        assert u10_prob == 9, f"Expected 9 problems in Unit 10, got {u10_prob}"
        assert u10_canvas >= 1, "Expected active simulation in Unit 10"

        # 3. Verify index.html portal live
        live_portal_url = "https://openstemlibrary.com/index.html"
        print(f"\nNavigating to {live_portal_url}...")
        resp2 = page.goto(live_portal_url, wait_until="networkidle")
        print(f"Portal status: {resp2.status if resp2 else 'N/A'}")
        page.wait_for_timeout(2000)

        chem_tab = page.locator(".dept-pill-btn", has_text="Chemistry")
        chem_label = chem_tab.inner_text()
        all_tab = page.locator(".dept-pill-btn", has_text="All Subjects")
        all_label = all_tab.inner_text()
        print(f"Live Portal Chemistry Tab: '{chem_label}'")
        print(f"Live Portal All Subjects Tab: '{all_label}'")

        chem_tab.click()
        page.wait_for_timeout(800)

        # Check Environmental Chemistry card
        env_card = page.locator("text=Environmental Chemistry: Atmospheric Kinetics").first
        assert env_card.count() > 0, "Environmental Chemistry card not found on live portal!"
        print("✓ Live Environmental Chemistry card verified in Chemistry department!")

        # Take live screenshot of portal
        portal_screenshot = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/live_portal_chem16.png"
        page.screenshot(path=portal_screenshot, full_page=False)
        print(f"Saved live portal screenshot to {portal_screenshot}")

        print(f"\nLive Console Errors logged: {len(console_errors)}")
        for err in console_errors:
            print(f"  - {err}")

        browser.close()
        print("\n✓ LIVE PRODUCTION VERIFICATION COMPLETE AND 100% SUCCESSFUL!")

if __name__ == "__main__":
    verify_live()
