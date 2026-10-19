#!/usr/bin/env python3
"""
Completely remove Google AdSense and third-party advertising scripts,
comments, and dead CSS across the entire OpenSTEM Library codebase,
transitioning the platform to a 100% free open-access model.
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Strip AdSense script tags and comments from all HTML files
html_files = sorted(glob.glob(os.path.join(ROOT, '*.html')))
cleaned_html_count = 0

for h in html_files:
    with open(h, 'r', encoding='utf-8') as fp:
        content = fp.read()
    orig = content

    # Strip Google AdSense comments
    content = re.sub(r'[ \t]*<!--\s*Google AdSense[^\n]*-->\r?\n?', '', content, flags=re.IGNORECASE)
    # Strip pagead2 script tags
    content = re.sub(r'[ \t]*<script[^>]*pagead2\.googlesyndication\.com[^>]*>.*?</script>\r?\n?', '', content, flags=re.DOTALL | re.IGNORECASE)

    if content != orig:
        with open(h, 'w', encoding='utf-8') as fp:
            fp.write(content)
        cleaned_html_count += 1

print(f"Removed AdSense script tags from {cleaned_html_count} HTML files.")

# 2. Update ads.txt to declare no third-party ads
ads_txt_path = os.path.join(ROOT, 'ads.txt')
ads_txt_content = (
    "# OpenSTEM Library (https://openstemlibrary.com)\n"
    "# Free open-access academic library. No third-party advertisements or ad networks are authorized on this domain.\n"
)
with open(ads_txt_path, 'w', encoding='utf-8') as fp:
    fp.write(ads_txt_content)
print("Updated ads.txt with open-access non-commercial policy.")

# 3. Update privacy.html
privacy_path = os.path.join(ROOT, 'privacy.html')
if os.path.exists(privacy_path):
    with open(privacy_path, 'r', encoding='utf-8') as fp:
        priv = fp.read()

    # Update meta descriptions
    priv = priv.replace(
        'Outlines compliance with Google AdSense, cookie policies, GDPR, CCPA, and user data protections.',
        'Outlines open-access policies, privacy protections, cookie policy, GDPR, CCPA, and student data safety.'
    )
    priv = priv.replace(
        'Privacy policy, Google AdSense cookie disclosure, GDPR, and user data protections for OpenSTEM library.',
        'Privacy policy, open-access principles, GDPR, and user data protections for OpenSTEM library.'
    )
    priv = priv.replace(
        'Privacy policy, Google AdSense cookie disclosure, GDPR, and data protections.',
        'Privacy policy, open-access principles, GDPR, and student data protections.'
    )

    # Replace Section 2 & 3
    old_sec2_3 = re.search(r'<h2>2\. Google AdSense & Third-Party Advertising Policy</h2>.*?<h2>4\. GDPR Compliance', priv, flags=re.DOTALL)
    if old_sec2_3:
        new_sec2_3 = (
            '<h2>2. Open-Access & Non-Commercial Policy</h2>\n'
            '      <p>OpenSTEM is dedicated to open, free academic education. We do not display third-party commercial advertisements, serve sponsored behavioral ads, or sell student or visitor data to advertising networks.</p>\n'
            '      \n'
            '      <div class="legal-highlight">\n'
            '        <strong>Commitment to Unrestricted Academic Access:</strong><br>\n'
            '        • All textbooks, mathematical derivations, interactive simulations, and solved exercises are provided 100% free of charge without paywalls, subscriptions, or commercial ad interruptions.<br>\n'
            '        • No ad-tracking networks or behavioral advertising scripts are executed on your device.<br>\n'
            '        • We respect reader privacy, enabling focused, ad-free STEM learning.\n'
            '      </div>\n'
            '\n'
            '      <h2>3. Cookies and Local Storage</h2>\n'
            '      <p>OpenSTEM uses local storage (localStorage) exclusively to enhance your learning experience:</p>\n'
            '      <ul>\n'
            '        <li>Saving your reading position and active chapter preferences across reading sessions.</li>\n'
            '        <li>Persisting study timer and focus tool preferences locally in your browser.</li>\n'
            '        <li>We do not deploy cross-site tracking cookies or advertising tracking pixels.</li>\n'
            '      </ul>\n\n'
            '      <h2>4. GDPR Compliance'
        )
        priv = priv[:old_sec2_3.start()] + new_sec2_3 + priv[old_sec2_3.end() - len('<h2>4. GDPR Compliance'):]
        with open(privacy_path, 'w', encoding='utf-8') as fp:
            fp.write(priv)
        print("Updated privacy.html with non-commercial policy.")

# 4. Update terms.html
terms_path = os.path.join(ROOT, 'terms.html')
if os.path.exists(terms_path):
    with open(terms_path, 'r', encoding='utf-8') as fp:
        terms = fp.read()
    
    old_sec4 = re.search(r'<h2>4\. External Links & Third-Party Advertisements</h2>.*?<h2>5\. Disclaimers', terms, flags=re.DOTALL)
    if old_sec4:
        new_sec4 = (
            '<h2>4. External Links & Open Access</h2>\n'
            '      <p>Our platform is entirely free and open-access for educational purposes without commercial advertising. External links may occasionally point to scholarly references, academic repositories, or open-source scientific tools; OpenSTEM does not control or endorse the content or privacy practices of external third-party websites.</p>\n\n'
            '      <h2>5. Disclaimers'
        )
        terms = terms[:old_sec4.start()] + new_sec4 + terms[old_sec4.end() - len('<h2>5. Disclaimers'):]
        with open(terms_path, 'w', encoding='utf-8') as fp:
            fp.write(terms)
        print("Updated terms.html with open-access terms.")

# 5. Clean dead ad CSS in styles.css
styles_path = os.path.join(ROOT, 'styles.css')
if os.path.exists(styles_path):
    with open(styles_path, 'r', encoding='utf-8') as fp:
        styles = fp.read()
    styles = re.sub(r'/\* Monetization & Google AdSense Placeholders \*/\s*\.ad-slot-box\s*\{.*?\n(?=\.reader-trust-footer|\/\*|$)', '', styles, flags=re.DOTALL)
    with open(styles_path, 'w', encoding='utf-8') as fp:
        fp.write(styles)
    print("Cleaned dead ad CSS from styles.css.")

# 6. Clean dead ad CSS in portal.css
portal_css_path = os.path.join(ROOT, 'portal.css')
if os.path.exists(portal_css_path):
    with open(portal_css_path, 'r', encoding='utf-8') as fp:
        portal = fp.read()
    portal = re.sub(r'/\* Monetization: AdSense Hero & Mid Banner \*/\s*\.portal-ad-banner\s*\{.*?\n(?=\/\* Contact & Author Box|\/\* Academic Collaboration|$)', '', portal, flags=re.DOTALL)
    with open(portal_css_path, 'w', encoding='utf-8') as fp:
        fp.write(portal)
    print("Cleaned dead ad CSS from portal.css.")

# 7. Update app.js toast message
app_js_path = os.path.join(ROOT, 'app.js')
if os.path.exists(app_js_path):
    with open(app_js_path, 'r', encoding='utf-8') as fp:
        app_js = fp.read()
    app_js = app_js.replace(
        'showToast("Right-click is protected to support free ad-supported academic access.");',
        'showToast("Right-click is protected to support free open-access academic reading.");'
    )
    with open(app_js_path, 'w', encoding='utf-8') as fp:
        fp.write(app_js)
    print("Updated app.js toast message.")

# 8. Update tooling/build-library.cjs to auto-remove pagead scripts if encountered
build_cjs_path = os.path.join(ROOT, 'tooling/build-library.cjs')
if os.path.exists(build_cjs_path):
    with open(build_cjs_path, 'r', encoding='utf-8') as fp:
        build_cjs = fp.read()
    if 'script[src*="pagead2"]' not in build_cjs:
        build_cjs = build_cjs.replace(
            "for (const link of doc.querySelectorAll('a[href]')) {",
            "for (const s of doc.querySelectorAll('script[src*=\"pagead2\"]')) s.remove();\n  for (const link of doc.querySelectorAll('a[href]')) {"
        )
        with open(build_cjs_path, 'w', encoding='utf-8') as fp:
            fp.write(build_cjs)
        print("Updated tooling/build-library.cjs to strip AdSense scripts automatically.")

print("\nAdSense removal complete!")
