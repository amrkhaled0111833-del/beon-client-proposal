#!/usr/bin/env python3
"""Make a proposal page for a new client.

Usage:  python new_client.py "اسم العميل" slug
Result: c/<slug>/index.html  ->  https://YOUR-SITE.vercel.app/c/<slug>
"""
import sys, pathlib, re
if len(sys.argv) != 3:
    sys.exit('Usage: python new_client.py "Client Name" slug')
name, slug = sys.argv[1].strip(), sys.argv[2].strip().lower()
if not re.fullmatch(r'[a-z0-9-]+', slug):
    sys.exit('slug: English letters, numbers and - only')
root = pathlib.Path(__file__).parent
html = (root / 'index.html').read_text(encoding='utf8')
old = re.search(r'clientName:\s*"(.*?)"', html).group(1)
html = html.replace(old, name)
out = root / 'c' / slug / 'index.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(html, encoding='utf8')
print(f'Created {out}  ->  /c/{slug}')
