import os, glob, re, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

book_meta = {
    'formal-logic': {
        'badgeCredits': 'Formal logic core',
        'probSecTitle': 'Step-by-Step Formal Logic Solutions',
        'topics': [
            'Logical Language, Arguments, Premises and Conclusions',
            'Truth-Functional Connectives, Truth Tables & Semantic Equivalence',
            'Natural Deduction for Propositional Logic & Derivation Rules',
            'Semantic Tableaux & Consistency Testing',
            'Soundness and Completeness of Deductive Systems',
            'First-Order Quantifiers, Variables and Domain Semantics',
            'Multi-Valued & Modal Logics (Kleene Semantics, Kripke Frames)',
            'Conjunctive Normal Form & Automated Satisfiability (SAT)'
        ],
        'editorialNote': '<strong>About this textbook.</strong> Original English teaching material for university formal logic and deductive systems courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating propositional truth tables, validity tests, proof trees, semantic tableaux, quantifier scopes, Kleene tables, and modal accessibility frames. Numerical checks and an editorial review support this edition.'
    },
    'model-theory-and-mathematical-semantics': {
        'badgeCredits': 'Model theory core',
        'probSecTitle': 'Step-by-Step Model Theory Solutions',
        'topics': [
            'First-Order Languages, Signatures, Structures & Domains',
            'Tarskian Truth, Variable Assignments & Satisfaction',
            'Substructures, Homomorphisms, Embeddings & Isomorphisms',
            'Automorphisms, Definable Relations & Congruence Classes',
            'Elementary Equivalence & Ehrenfeucht-Fraïssé Games',
            'Quantifier Rank, Formula Complexity & Preservation Theorems',
            'Compactness Theorem, Nonstandard Models & Finite Satisfiability',
            'Henkin Witness Sets, Types, Realization & Ultraproducts'
        ],
        'editorialNote': '<strong>About this textbook.</strong> Original English teaching material for university model theory and mathematical semantics courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating finite structure satisfaction, term evaluations, relation transport, substructure closures, automorphism orbits, compactness prefixes, and Ehrenfeucht-Fraïssé game rounds. Numerical checks and an editorial review support this edition.'
    },
    'proof-theory-and-deductive-systems': {
        'badgeCredits': 'Proof theory core',
        'probSecTitle': 'Step-by-Step Proof Theory Solutions',
        'topics': [
            'Judgments, Syntactic Derivations & Proof Trees',
            'Natural Deduction Rules for Propositional & First-Order Logic',
            'Gentzen Sequent Calculi (LK for Classical, LJ for Intuitionistic Logic)',
            'Structural Rules: Weakening, Contraction & Exchange',
            'Cut Elimination Theorem & the Subformula Property',
            'Proof Normalization & Detour Contractions in Natural Deduction',
            'Curry-Howard Correspondence & Simply Typed Lambda Calculus',
            'Analytic Tableaux, Resolution Refutations & Automated Proof Search'
        ],
        'editorialNote': '<strong>About this textbook.</strong> Original English teaching material for university proof theory courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating sequent derivations, natural deduction rule certificates, detour contractions, lambda reductions, resolution refutations, and type checking derivations. Numerical checks and an editorial review support this edition.'
    },
    'set-theory-and-foundations': {
        'badgeCredits': 'Set theory core',
        'probSecTitle': 'Step-by-Step Set Theory Solutions',
        'topics': [
            'Axiomatic Foundations & the Paradoxes of Naive Set Theory',
            'Zermelo-Fraenkel Axioms (ZFC): Extensionality, Pairing, Union, Power Set',
            'Axiom of Separation, Comprehension & Class Inclusions',
            'Relations, Equivalence Partitions, Quotients & Orderings',
            'Functions, Injectivity, Surjectivity & the Schröder-Bernstein Theorem',
            'Von Neumann Ordinals & Transfinite Induction and Recursion',
            'Cardinal Numbers, Cantor\'s Theorem & Cardinal Arithmetic',
            'Axiom of Choice, Zorn\'s Lemma & the Well-Ordering Theorem'
        ],
        'editorialNote': '<strong>About this textbook.</strong> Original English teaching material for university set theory and foundations courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating membership vs subset inclusion, set algebra, relation equivalence classes, injectivity/surjectivity, Cantor diagonal cuts, ordinal ranks, and separation filters. Numerical checks and an editorial review support this edition.'
    },
    'symbolic-and-predicate-logic': {
        'badgeCredits': 'Predicate logic core',
        'probSecTitle': 'Step-by-Step Symbolic & Predicate Logic Solutions',
        'topics': [
            'Alphabet, Signatures, Constants, Function & Predicate Symbols',
            'Terms, Atomic Formulas & Inductive Formation Rules',
            'Quantifier Scope, Free vs. Bound Variables & Sentence Criteria',
            'Capture-Avoiding Substitution & Variable Renaming Conventions',
            'Semantic Interpretations, Domains & Truth Conditions',
            'Restricted & Uniquely Existential Quantifiers (∃!)',
            'Prenex Normal Form Transformations & Skolemization Procedures',
            'First-Order Resolution Refutation & Datalog Declarative Querying'
        ],
        'editorialNote': '<strong>About this textbook.</strong> Original English teaching material for university predicate logic courses. Eight units with five solved questions per unit and 16 interactive simulations illustrating quantifier scope shifts, capture-avoiding substitutions, restricted quantification, relation dependency tests, prenex transformations, and resolution derivations. Numerical checks and an editorial review support this edition.'
    }
}

lss_dir = os.path.join(ROOT, 'src', 'subjects', 'logic-and-systems-science')

for slug, meta in book_meta.items():
    book_dir = os.path.join(lss_dir, slug)
    html_files = glob.glob(os.path.join(book_dir, '*.html'))
    print(f"Cleaning {slug}: {len(html_files)} files")
    for fpath in html_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace badge credits
        content = re.sub(
            r'<span class="badge-pill badge-credits">[^<]*</span>',
            f'<span class="badge-pill badge-credits">{meta["badgeCredits"]}</span>',
            content
        )
        
        # Replace prob sec title
        content = re.sub(
            r'<h3 class="prob-sec-title">[^<]*</h3>',
            f'<h3 class="prob-sec-title">{meta["probSecTitle"]}</h3>',
            content
        )
        
        # Replace stat-editorial-note
        content = re.sub(
            r'<aside class="stat-editorial-note" aria-label="About this textbook">[\s\S]*?</aside>',
            lambda m, note=meta["editorialNote"]: f'<aside class="stat-editorial-note" aria-label="About this textbook">{note}</aside>',
            content
        )
        
        # Remove fundamentals-of-materials-science.css link
        content = re.sub(r'<link rel="stylesheet" href="fundamentals-of-materials-science\.css">', '', content)
        
        # Fix about array in JSON-LD
        topics_json = json.dumps(meta['topics'], ensure_ascii=False)
        content = re.sub(
            r'"about":\s*\[[^\]]*\]',
            lambda m, tjson=topics_json: f'"about":{tjson}',
            content
        )
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

print("All HTML files deeply cleaned and standardized.")
