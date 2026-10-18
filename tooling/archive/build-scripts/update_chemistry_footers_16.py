# -*- coding: utf-8 -*-
"""
update_chemistry_footers_16.py
Cross-links Environmental Chemistry in all 15 existing Chemistry textbooks
and updates Department of Chemistry curriculum description to 16 volumes.
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
    "supramolecular-chemistry.html",
    "organometallic-chemistry.html"
]

target_link = '<a href="environmental-chemistry.html" class="reader-trust-link" style="color:#8b949e; text-decoration:none;">Environmental Chemistry</a>'

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}: not found")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Volume count in Department of Chemistry trust col
    updated = re.sub(
        r'Complete \d+-Volume University Honors Curriculum',
        'Complete 16-Volume University Honors Curriculum',
        content
    )

    # 2. Insert environmental-chemistry link if not already present
    if "environmental-chemistry.html" not in updated:
        # Look for organometallic-chemistry.html link
        organo_match = re.search(r'(<a\s+href="organometallic-chemistry\.html"[^>]*>.*?</a>)', updated, re.DOTALL)
        if organo_match:
            organo_tag = organo_match.group(1)
            replacement = organo_tag + "\n              " + target_link
            updated = updated.replace(organo_tag, replacement, 1)
            print(f"Added Environmental Chemistry link after Organometallic Chemistry in {filepath}")
        else:
            # Fallback before about.html
            about_match = re.search(r'(<a\s+href="about\.html"[^>]*>.*?</a>)', updated, re.DOTALL)
            if about_match:
                about_tag = about_match.group(1)
                replacement = target_link + "\n              " + about_tag
                updated = updated.replace(about_tag, replacement, 1)
                print(f"Added Environmental Chemistry link before about.html in {filepath}")
            else:
                print(f"WARNING: No insertion point found in {filepath}")

    with open(filepath, "w", encoding="utf-8", newline="\n") as f:
        f.write(updated)
    print(f"Updated {filepath}")

def main():
    print(f"Updating footers across {len(chem_files)} chemistry textbooks...")
    for f in chem_files:
        update_file(f)
    print("All chemistry textbook footers updated to 16 volumes!")

if __name__ == "__main__":
    main()
