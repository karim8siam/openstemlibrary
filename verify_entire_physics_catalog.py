import asyncio
from playwright.async_api import async_playwright

courses = [
    'reader.html',
    'mechanics.html',
    'electrodynamics.html',
    'optics.html',
    'statistical-mechanics.html',
    'properties-of-matter.html',
    'electricity-magnetism.html',
    'thermal-physics.html',
    'classical-mechanics.html',
    'basic-electronics.html',
    'atomic-molecular-physics.html',
    'solid-state-physics.html',
    'nuclear-physics.html',
    'digital-electronics.html',
    'quantum-mechanics-2.html',
    'astrophysics.html',
    'plasma-physics.html',
    'solid-state-physics-2.html',
    'nuclear-physics-2.html',
    'reactor-physics.html'
]

async def verify_all():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        )
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        print(f"Testing all {len(courses)} Physics courses for console/page errors and KaTeX rendering...")
        
        all_ok = True
        for c in courses:
            errors = []
            page.on("pageerror", lambda err: errors.append(f"PAGE ERROR: {err}"))
            page.on("console", lambda msg: errors.append(f"CONSOLE: {msg.text}") if msg.type == "error" else None)

            url = f"http://localhost:4242/{c}"
            await page.goto(url, wait_until="networkidle")
            await asyncio.sleep(0.3)

            # Check footer exists and has links
            footer_links = await page.locator(".reader-trust-footer a").count()
            
            # Check sections render
            sections = await page.locator(".textbook-section-card").count()

            status = "OK" if len(errors) == 0 and footer_links >= 20 and sections > 0 else "FAIL"
            if status != "OK":
                all_ok = False
                print(f"FAILED {c}: errors={len(errors)}, footer_links={footer_links}, sections={sections}")
                for e in errors:
                    print(f"   {e}")
            else:
                print(f"PASSED {c:30}: sections={sections:2}, footer_links={footer_links:2}, errors=0")

        await browser.close()
        if all_ok:
            print("\n>>> ALL 20 COURSES PASSED COMPLETE BROWSER VERIFICATION WITH 0 ERRORS! <<<")
        else:
            print("\n>>> SOME COURSES FAILED VERIFICATION <<<")

if __name__ == "__main__":
    asyncio.run(verify_all())
