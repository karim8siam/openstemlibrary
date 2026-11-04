# Append writer main function to build_cpe_b3_sims_full.py

writer_code = '''

def main():
    sims = {
        'chemical-reaction-engineering-i': build_cre1_sims(),
        'chemical-reaction-engineering-ii': build_cre2_sims(),
        'process-dynamics-and-control': build_pdc_sims(),
        'process-simulation': build_psim_sims()
    }
    for slug, code in sims.items():
        out_dir = os.path.join(ROOT, 'src', 'subjects', 'chemical-process-engineering', slug)
        os.makedirs(out_dir, exist_ok=True)
        out_file = os.path.join(out_dir, f'{slug}-sims.js')
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f'Wrote simulation suite: {out_file} ({len(code):,} bytes)')

if __name__ == '__main__':
    main()
'''

with open('tooling/build_cpe_b3_sims_full.py', 'a') as f:
    f.write(writer_code)
print("Added main writer!")
