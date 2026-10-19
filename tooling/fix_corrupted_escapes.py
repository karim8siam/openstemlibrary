#!/usr/bin/env python3
"""
Repair corrupted Python string escapes across drafts in:
- statistical-estimation
- demography-and-population-statistics
- economic-statistics
- sample-surveys-and-sampling-theory
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DIRS = [
    os.path.join(ROOT, 'publishing/drafts/statistics-probability-statistical-estimation'),
    os.path.join(ROOT, 'publishing/drafts/statistics-probability-demography-and-population-statistics'),
    os.path.join(ROOT, 'publishing/drafts/statistics-probability-economic-statistics'),
    os.path.join(ROOT, 'publishing/drafts/statistics-probability-sample-surveys-and-sampling-theory')
]

modified_count = 0

for d in DIRS:
    for f in sorted(glob.glob(os.path.join(d, '*.md'))):
        with open(f, 'rb') as fp:
            data = fp.read()
        orig = data

        # 1. Byte-level control character repairs
        data = data.replace(b'\x0c', b'\\f')
        data = data.replace(b'\x08', b'\\b')
        data = data.replace(b'\x07', b'\\a')
        data = data.replace(b'\x0b', b'\\v')
        data = data.replace(b'\x0dho', b'\\rho')
        data = data.replace(b'\r\n', b'\n').replace(b'\r', b'')

        # 2. Corrupted tabs before LaTeX commands
        data = re.sub(rb'\t(ext|heta|ilde|imes|au|o(?=[\s\$\\\d\)]))', rb'\\t\1', data)

        # Decode to utf-8 text for regex operations
        text = data.decode('utf-8')

        # 3. Broken \right at beginning of line (swallowed \r)
        text = re.sub(r'(\n\s*)ight([\)\]\|\.^_\s])', r'\1\\right\2', text)

        # 4. In case pprox or ar{ has lost its control char
        text = re.sub(r'(?<![a-zA-Z\\])pprox', r'\\approx', text)
        text = re.sub(r'(?<![a-zA-Z\\])ar\{', r'\\bar{', text)

        # 5. Broken newline inside inline math in unit-2 of statistical-estimation
        text = text.replace('\\left(\\frac{n-1-k}{k}\n\\right)^2', '\\left(\\frac{n-1-k}{k}\\right)^2')

        new_data = text.encode('utf-8')
        if new_data != orig:
            with open(f, 'wb') as fp:
                fp.write(new_data)
            modified_count += 1
            rel_path = os.path.relpath(f, ROOT)
            print(f"Repaired: {rel_path} ({len(orig)} -> {len(new_data)} bytes)")

print(f"\nDone! Repaired {modified_count} files.")
