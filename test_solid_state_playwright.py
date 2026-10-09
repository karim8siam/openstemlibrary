import time
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.goto('http://localhost:4242/solid-state-chemistry.html')
        page.wait_for_timeout(1500)

        nav_items = page.locator('.unit-nav-item')
        total_units = nav_items.count()
        print(f"Total units in nav: {total_units}")

        test_units = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0] # All 10 units + reload Unit 1
        all_passed = True

        for step_i, u_idx in enumerate(test_units):
            if step_i > 0:
                nav_items.nth(u_idx).click()
                page.wait_for_timeout(600)

            math_displays = page.locator('.math-display').count()
            katex_count = page.locator('.katex').count()
            unrendered = 0
            for i in range(math_displays):
                el = page.locator('.math-display').nth(i)
                has_katex = el.locator('.katex').count() > 0
                raw_text = el.inner_text()
                has_brackets = '\\[' in raw_text or '\\]' in raw_text
                if not has_katex or has_brackets:
                    unrendered += 1

            p_info = page.evaluate("""() => {
                const ps = Array.from(document.querySelectorAll('.chapter-article p, .textbook-section-card p, .content-card p'));
                const orphan = ps.filter(p => p.textContent.trim() === '\\\\').length;
                const trailing = ps.filter(p => p.textContent.trim().endsWith('\\\\')).length;
                return { orphan, trailing, total: ps.length };
            }""")

            unit_label = f"Unit {u_idx + 1}" + (" (Reloaded)" if step_i == 10 else "")
            print(f"=== {unit_label} ===")
            print(f"  math-display count:      {math_displays}")
            print(f"  .katex elements:         {katex_count}")
            print(f"  unrendered math-display: {unrendered}")
            print(f"  orphan backslash <p>:    {p_info['orphan']}")
            print(f"  trailing backslash <p>:  {p_info['trailing']}")
            print(f"  total paragraphs:        {p_info['total']}")

            if unrendered > 0 or p_info['orphan'] > 0 or p_info['trailing'] > 0:
                all_passed = False
                print(f"  FAILED in {unit_label}!")

        # Take screenshot of Section 1.3 (the one from user's screenshot)
        page.locator('.unit-nav-item').first.click()
        page.wait_for_timeout(800)

        born_lande = page.locator('text=Born-Landé Power Law Formulation').first
        if born_lande.count() > 0:
            born_lande.scroll_into_view_if_needed()
            page.wait_for_timeout(500)
            page.screenshot(path='/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/solid_state_born_lande_fixed.png')
            print("\nSaved screenshot to solid_state_born_lande_fixed.png")

        page.screenshot(path='/Users/karimsiam/.gemini/antigravity/brain/3c173f38-4977-4566-a968-481f7f22cbe9/solid_state_fixed_full.png')
        print("Saved full page screenshot to solid_state_fixed_full.png")

        browser.close()

        if all_passed:
            print("\n=======================================================")
            print("ALL 10 UNITS PASSED WITH 100% CLEAN MATH RENDERING!")
            print("0 UNRENDERED DISPLAY EQUATIONS ACROSS ALL UNITS")
            print("0 ORPHAN OR TRAILING BACKSLASH PARAGRAPHS")
            print("=======================================================")
        else:
            print("\nSOME CHECKS FAILED!")

if __name__ == '__main__':
    run()
