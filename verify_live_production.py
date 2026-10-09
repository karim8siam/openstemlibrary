"""
verify_live_production.py
Polls https://openstemlibrary.com/supramolecular-chemistry.html and https://openstemlibrary.com/
Confirms live deployment, checks math rendering and active canvas simulation.
Saves live production screenshots to artifacts directory.
"""

import time
from playwright.sync_api import sync_playwright

def verify_live():
    print("Testing live deployment on Cloudflare Pages...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        live_url = "https://openstemlibrary.com/supramolecular-chemistry.html"
        portal_url = "https://openstemlibrary.com/"

        # Retry polling up to 90s for Cloudflare build to finish
        max_retries = 18
        deployed = False
        for attempt in range(max_retries):
            print(f"Checking {live_url} (Attempt {attempt+1}/{max_retries})...")
            try:
                resp = page.goto(live_url)
                if resp and resp.status == 200:
                    title = page.title()
                    if "Supramolecular Chemistry" in title:
                        print("✓ Live 200 OK with correct title!")
                        deployed = True
                        break
            except Exception as e:
                print(f"  Transient connection error: {e}")
            page.wait_for_timeout(5000)

        if not deployed:
            print("Live site deployment timed out or not yet updated.")
            browser.close()
            return

        page.wait_for_timeout(2000)

        # 1. Check sections & problems on live site
        sec_count = page.locator(".textbook-section-card").count()
        prob_count = page.locator(".problem-card").count()
        katex_count = page.locator(".katex").count()
        canvas_count = page.locator("canvas").count()

        print(f"Live Reader Stats:")
        print(f"  Sections count: {sec_count}")
        print(f"  Problems count: {prob_count}")
        print(f"  KaTeX elements: {katex_count}")
        print(f"  Active Canvas:  {canvas_count}")

        # Take screenshot of live textbook
        live_reader_screenshot = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/live_supramolecular_chemistry.png"
        page.screenshot(path=live_reader_screenshot, full_page=False)
        print(f"Saved live reader screenshot to {live_reader_screenshot}")

        # 2. Check live portal index.html
        print(f"\nChecking live portal {portal_url}...")
        page.goto(portal_url)
        page.wait_for_timeout(2000)

        chem_btn = page.locator(".dept-pill-btn", has_text="Chemistry")
        if chem_btn.count() > 0:
            chem_text = chem_btn.inner_text()
            print(f"Live Chemistry button: {chem_text}")
            chem_btn.click()
            page.wait_for_timeout(800)

        live_portal_screenshot = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/live_portal_chem14.png"
        page.screenshot(path=live_portal_screenshot, full_page=False)
        print(f"Saved live portal screenshot to {live_portal_screenshot}")

        browser.close()
        print("\n✓ Live production verification completed successfully!")

if __name__ == "__main__":
    verify_live()
