"""
verify_live_production.py
Captures live screenshots and verifies production deployment on Cloudflare Pages.
"""

from playwright.sync_api import sync_playwright

def verify_live():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        print("Navigating to https://openstemlibrary.com/organometallic-chemistry.html...")
        page.goto("https://openstemlibrary.com/organometallic-chemistry.html")
        page.wait_for_timeout(2500)

        # Check title
        title = page.title()
        print(f"Live Page Title: {title}")
        assert "Organometallic Chemistry" in title

        # Verify simulation canvas mounted
        canvas_count = page.locator("canvas").count()
        print(f"Live Canvas Count: {canvas_count}")
        assert canvas_count >= 1

        # Save live reader screenshot
        live_reader_path = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/live_organometallic_chemistry.png"
        page.screenshot(path=live_reader_path, full_page=False)
        print(f"Saved live reader screenshot to {live_reader_path}")

        # Check portal
        print("Navigating to https://openstemlibrary.com...")
        page.goto("https://openstemlibrary.com")
        page.wait_for_timeout(2000)

        chem_tab = page.locator(".dept-pill-btn", has_text="Chemistry")
        chem_tab_text = chem_tab.inner_text()
        print(f"Live Chemistry Tab: {chem_tab_text}")
        assert "15" in chem_tab_text

        all_tab = page.locator(".dept-pill-btn", has_text="All Subjects")
        all_tab_text = all_tab.inner_text()
        print(f"Live All Subjects Tab: {all_tab_text}")
        assert "56" in all_tab_text

        chem_tab.click()
        page.wait_for_timeout(800)

        live_portal_path = "/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/live_portal_chem15.png"
        page.screenshot(path=live_portal_path, full_page=False)
        print(f"Saved live portal screenshot to {live_portal_path}")

        browser.close()
        print("Live production verification completed successfully!")

if __name__ == "__main__":
    verify_live()
