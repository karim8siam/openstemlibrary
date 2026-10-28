import glob, re, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

book_meta = {
    'engineering-mechanics': {
        'title': 'Engineering Mechanics',
        'badgeCredits': 'Mechanical engineering core',
        'probSecTitle': 'Step-by-Step Engineering Mechanics Solutions',
        'topics': [
            'Newtonian Mechanics, Particle Statics & Free-Body Diagrams',
            'Force Systems, Moments, Couples & Rigid-Body Equilibrium',
            'Trusses, Frames, Simple Machines & the Method of Joints/Sections',
            'Dry Friction, Coulomb Friction & Capstan Belt Applications',
            'Centroids, Centers of Mass & Moments of Inertia',
            'Kinematics of Particles & Curvilinear Motion',
            'Kinetics of Particles: Newton-Euler, Work-Energy & Impulse-Momentum',
            'Planar Kinetics & Energy Methods for Rigid Bodies'
        ],
        'editorialNote': '<strong>About this textbook.</strong> Original English teaching material for university engineering mechanics and statics/dynamics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating force vectors, beam reactions, trusses, capstan friction, and rigid body kinematics. Numerical checks and an editorial review support this edition.'
    },
    'mechanics-of-solids': {
        'title': 'Mechanics of Solids',
        'badgeCredits': 'Mechanical engineering core',
        'probSecTitle': 'Step-by-Step Mechanics of Solids Solutions',
        'topics': [
            'Stress and Strain Concepts, Normal/Shear Stresses & Hooke’s Law',
            'Axial Loading, Thermal Stresses & St. Venant Principle',
            'Torsion of Circular Shafts & Elastic-Plastic Response',
            'Flexural Bending Stresses & Pure Bending in Beams',
            'Transverse Shear Stresses & Shear Flow in Built-Up Beams',
            'Beam Deflections: Direct Integration & Macaulay’s Method',
            'Plane Stress Transformations, Mohr’s Circle & Yield Criteria',
            'Column Buckling, Euler Stability & Thick/Thin Cylinders'
        ],
        'editorialNote': '<strong>About this textbook.</strong> Original English teaching material for university mechanics of solids and strength of materials courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating axial deformation, torsion, beam curvature, principal stresses, and Euler buckling. Numerical checks and an editorial review support this edition.'
    },
    'engineering-thermodynamics': {
        'title': 'Engineering Thermodynamics',
        'badgeCredits': 'Mechanical engineering core',
        'probSecTitle': 'Step-by-Step Engineering Thermodynamics Solutions',
        'topics': [
            'Thermodynamic Systems, State Variables, Work & Heat Interactions',
            'Pure Substance Phase Behavior, PVT Surfaces & Steam Tables',
            'First Law of Thermodynamics & Open/Closed Control Volumes',
            'Second Law of Thermodynamics, Heat Engines & Carnot Limits',
            'Entropy Calculus, Isentropic Processes & T-ds Relations',
            'Exergy (Availability) Analysis & Second-Law Irreversibility',
            'Vapor & Gas Power Cycles: Rankine, Brayton, Otto & Diesel',
            'Refrigeration Systems, Gas Mixtures & Psychrometric Charts'
        ],
        'editorialNote': '<strong>About this textbook.</strong> Original English teaching material for university engineering thermodynamics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating ideal gas equations of state, nozzle expansion, Carnot limits, Rankine cycles, and psychrometric properties. Numerical checks and an editorial review support this edition.'
    },
    'fluid-mechanics': {
        'title': 'Fluid Mechanics',
        'badgeCredits': 'Mechanical engineering core',
        'probSecTitle': 'Step-by-Step Fluid Mechanics Solutions',
        'topics': [
            'Fluid Properties, Viscosity, Surface Tension & Continuum Concept',
            'Fluid Statics, Hydrostatic Pressure & Buoyancy Calculations',
            'Control Volume Analysis & Reynolds Transport Theorem',
            'Differential Relations, Continuity & Navier-Stokes Equations',
            'Dimensional Analysis, Similitude & Buckingham Pi Theorem',
            'Internal Viscous Pipe Flow, Laminar/Turbulent Friction & Moody Chart',
            'External Aerodynamics, Boundary Layers & Lift/Drag Forces',
            'Turbomachinery Fundamentals & Compressible Flow Shock Waves'
        ],
        'editorialNote': '<strong>About this textbook.</strong> Original English teaching material for university fluid mechanics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating Reynolds numbers, hydrostatic forces, Bernoulli velocities, Moody friction factors, and vortex shedding. Numerical checks and an editorial review support this edition.'
    },
    'manufacturing-processes': {
        'title': 'Manufacturing Processes',
        'badgeCredits': 'Mechanical engineering core',
        'probSecTitle': 'Step-by-Step Manufacturing Processes Solutions',
        'topics': [
            'Metal Casting Science, Fluidity, Mold Design & Solidification',
            'Bulk Deformation Processes: Rolling, Forging, Extrusion & Wire Drawing',
            'Sheet Metal Forming, Shearing, Bending, Deep Drawing & Springback',
            'Machining Science, Orthogonal Cutting, Merchant Circle & Tool Wear',
            'Additive Manufacturing: Powder Bed Fusion, Stereolithography & DED',
            'Fusion & Solid-State Welding, Brazing & Heat-Affected Zones',
            'Polymer Processing: Injection Molding, Extrusion & Thermoforming',
            'Precision Metrology, Surface Metrology, GD&T & Statistical Quality'
        ],
        'editorialNote': '<strong>About this textbook.</strong> Original English teaching material for university manufacturing processes courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating solidification time, forging loads, Taylor tool life, cutting mechanics, and metrology uncertainty. Numerical checks and an editorial review support this edition.'
    }
}

me_dir = os.path.join(ROOT, 'src', 'subjects', 'mechanical-engineering')

for slug, meta in book_meta.items():
    landing_file = os.path.join(me_dir, slug, f"{slug}.html")
    if not os.path.exists(landing_file):
        continue
    with open(landing_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix body dataset bookPath
    content = re.sub(r'data-book-path="[^"]*"', f'data-book-path="{slug}.html"', content)

    # Fix brand-title
    content = re.sub(r'<span class="brand-title">[^<]*</span>', f'<span class="brand-title">{meta["title"]}</span>', content)

    # Fix badge-course
    content = re.sub(r'<span class="badge-pill badge-course">[^<]*</span>', '<span class="badge-pill badge-course">Mechanical Engineering</span>', content)

    # Fix badge-credits
    content = re.sub(r'<span class="badge-pill badge-credits">[^<]*</span>', f'<span class="badge-pill badge-credits">{meta["badgeCredits"]}</span>', content)

    # Fix probSecTitle
    content = re.sub(r'<h2 class="section-title">[^<]*Worked Examples[^<]*</h2>', f'<h2 class="section-title">{meta["probSecTitle"]}</h2>', content)
    content = re.sub(r'<h2>Step-by-Step[^<]*Solutions</h2>', f'<h2>{meta["probSecTitle"]}</h2>', content)

    # Fix stat-editorial-note
    content = re.sub(r'<aside class="stat-editorial-note"[^>]*>[\s\S]*?</aside>', f'<aside class="stat-editorial-note" aria-label="About this textbook">{meta["editorialNote"]}</aside>', content)

    # Fix BreadcrumbList
    breadcrumb_replacement = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "OpenSTEM Library", "item": "https://openstemlibrary.com/"},
            {"@type": "ListItem", "position": 2, "name": "Mechanical Engineering", "item": "https://openstemlibrary.com/#dept-mechanical-engineering"},
            {"@type": "ListItem", "position": 3, "name": meta["title"], "item": f"https://openstemlibrary.com/{slug}"}
        ]
    })
    content = re.sub(r'<script type="application/ld\+json">\{"@context":"https://schema\.org","@type":"BreadcrumbList"[\s\S]*?</script>', f'<script type="application/ld+json">{breadcrumb_replacement}</script>', content)

    # Fix Course/Book JSON-LD about array
    def update_about(match):
        raw_json = match.group(0)
        try:
            m_json = re.search(r'>([\s\S]*)<', raw_json)
            if not m_json:
                return raw_json
            data = json.loads(m_json.group(1))
            data["about"] = meta["topics"]
            return f'<script type="application/ld+json">{json.dumps(data, indent=2)}<'
        except Exception:
            return raw_json

    content = re.sub(r'<script type="application/ld\+json">\{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"(?:Book|Course)"[\s\S]*?</script>', update_about, content)

    # Replace any leftover fundamentals-of-materials-science in links
    content = content.replace('fundamentals-of-materials-science', slug)

    with open(landing_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned {slug}.html")

print("All Batch 1 landing pages cleaned.")
