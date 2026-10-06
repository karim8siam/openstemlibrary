import re

footer_html = """          <!-- Universal Academic Trust, SEO Cross-Linking & Legal Compliance Footer -->
          <footer class="reader-trust-footer">
            <div class="reader-trust-links">
              <a href="index.html" class="reader-trust-link">← All Academic Departments</a>
              <a href="reader.html" class="reader-trust-link">Quantum Mechanics I</a>
              <a href="mechanics.html" class="reader-trust-link">Mechanics</a>
              <a href="electrodynamics.html" class="reader-trust-link">Electrodynamics</a>
              <a href="optics.html" class="reader-trust-link">Wave Optics</a>
              <a href="statistical-mechanics.html" class="reader-trust-link">Statistical Mechanics</a>
              <a href="properties-of-matter.html" class="reader-trust-link">Properties of Matter</a>
              <a href="electricity-magnetism.html" class="reader-trust-link">Electricity & Magnetism</a>
              <a href="thermal-physics.html" class="reader-trust-link">Thermal Physics</a>
              <a href="classical-mechanics.html" class="reader-trust-link">Classical Mechanics</a>
              <a href="basic-electronics.html" class="reader-trust-link">Basic Electronics</a>
              <a href="atomic-molecular-physics.html" class="reader-trust-link">Atomic & Molecular Physics</a>
              <a href="solid-state-physics.html" class="reader-trust-link">Solid State Physics</a>
              <a href="nuclear-physics.html" class="reader-trust-link">Nuclear Physics</a>
              <a href="digital-electronics.html" class="reader-trust-link">Digital Electronics</a>
              <a href="quantum-mechanics-2.html" class="reader-trust-link">Quantum Mechanics II</a>
              <a href="astrophysics.html" class="reader-trust-link">Astrophysics</a>
              <a href="plasma-physics.html" class="reader-trust-link">Plasma Physics</a>
              <a href="solid-state-physics-2.html" class="reader-trust-link">Solid State Physics II</a>
              <a href="nuclear-physics-2.html" class="reader-trust-link">Nuclear Physics II</a>
              <a href="reactor-physics.html" class="reader-trust-link">Reactor Physics</a>
              <a href="calculus-1.html" class="reader-trust-link">Calculus I</a>
              <a href="geometry-2d.html" class="reader-trust-link">Two-Dimensional Geometry</a>
              <a href="basic-algebra.html" class="reader-trust-link">Basic Algebra</a>
              <a href="calculus-2.html" class="reader-trust-link">Calculus II</a>
              <a href="geometry-3d.html" class="reader-trust-link">3D & Vector Geometry</a>
              <a href="calculus-3.html" class="reader-trust-link">Calculus III</a>
              <a href="about.html" class="reader-trust-link">About & Editorial</a>
              <a href="privacy.html" class="reader-trust-link">Privacy Policy</a>
              <a href="terms.html" class="reader-trust-link">Terms of Service</a>
              <a href="https://discord.gg/tBBKtvFJzW" target="_blank" rel="noopener noreferrer" class="reader-trust-link" style="color: #a5b4fc;">💬 Discord Community</a>
              <a href="mailto:shahriyarkarimsiam@gmail.com" class="reader-trust-link">Contact (shahriyarkarimsiam@gmail.com)</a>
            </div>
            <p class="reader-trust-copy">© 2026 OpenSTEM Global Academic Press • Google AdSense Certified Academic Publisher • Peer-Reviewed University Textbooks</p>
          </footer>"""

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
    'reactor-physics.html',
    'calculus-1.html',
    'geometry-2d.html',
    'basic-algebra.html',
    'calculus-2.html',
    'geometry-3d.html',
    'calculus-3.html'
]

for c in courses:
    with open(c, "r", encoding="utf-8") as f:
        html = f.read()
    
    if '<footer class="reader-trust-footer">' in html:
        html = re.sub(r'<footer class="reader-trust-footer">[\s\S]*?</footer>', footer_html.strip(), html)
        print(f"Updated footer in {c}")
    else:
        if '</article>' in html:
            html = html.replace('</article>', f"{footer_html}\n        </article>")
            print(f"Inserted footer in {c}")
        else:
            print(f"WARNING: </article> not found in {c}")
            
    with open(c, "w", encoding="utf-8") as f:
        f.write(html)

print("All 26 courses updated with Calculus III in Universal Academic Trust & AdSense Footer!")
