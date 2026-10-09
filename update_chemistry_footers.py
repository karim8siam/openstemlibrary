"""
update_chemistry_footers.py
Cross-links Organometallic Chemistry in all 14 existing Chemistry textbooks
and updates Department of Chemistry curriculum description to 15 volumes.
"""

import re
import os

chem_files = [
    "physical-chemistry-1.html",
    "inorganic-chemistry-1.html",
    "organic-chemistry-1.html",
    "organic-chemistry-2.html",
    "analytical-chemistry.html",
    "nuclear-radiochemistry.html",
    "industrial-chemistry.html",
    "molecular-motion-kinetics.html",
    "natural-products-chemistry.html",
    "chemical-spectroscopy.html",
    "quantum-chemistry-thermodynamics.html",
    "solid-state-chemistry.html",
    "polymer-chemistry.html",
    "supramolecular-chemistry.html"
]

target_link = '<a href="organometallic-chemistry.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Organometallic Chemistry</a>'

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}: not found")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Volume count in Department of Chemistry trust col
    updated = re.sub(
        r'Complete \d+-Volume University Honors Curriculum',
        'Complete 15-Volume University Honors Curriculum',
        content
    )

    # 2. Insert organometallic-chemistry link if not already present
    if "organometallic-chemistry.html" not in updated:
        # Look for supramolecular-chemistry.html link
        supra_match = re.search(r'(<a\s+href="supramolecular-chemistry\.html"[^>]*>.*?</a>)', updated, re.DOTALL)
        if supra_match:
            supra_tag = supra_match.group(1)
            replacement = supra_tag + "\n              " + target_link
            updated = updated.replace(supra_tag, replacement, 1)
            print(f"Added Organometallic link to {filepath}")
        else:
            # Fallback before about.html
            about_match = re.search(r'(<a\s+href="about\.html"[^>]*>.*?</a>)', updated, re.DOTALL)
            if about_match:
                about_tag = about_match.group(1)
                replacement = target_link + "\n              " + about_tag
                updated = updated.replace(about_tag, replacement, 1)
                print(f"Added Organometallic link before about.html in {filepath}")
            else:
                print(f"Warning: could not find insertion point in {filepath}")
    else:
        print(f"Organometallic link already present in {filepath}")

    with open(filepath, "w", encoding="utf-8", newline="\n") as f:
        f.write(updated)

if __name__ == "__main__":
    for f in chem_files:
        update_file(f)
    print("All 14 Chemistry readers processed successfully.")
