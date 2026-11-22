"""Build index.html from src/template.html + data/resources.json.

Why a build step: the page must work as one self-contained file (GitHub Pages,
a claude.ai artifact, or opened straight from disk), so the data is inlined
rather than fetched at runtime.

Usage:  python3 build.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
data = json.loads((ROOT / "data" / "resources.json").read_text(encoding="utf-8"))

# Basic checks so a bad edit fails loudly instead of rendering a broken page.
required = {"name", "org", "country", "roles", "stages", "type", "url",
            "summary", "access", "reliability", "status", "checked"}
for i, r in enumerate(data):
    missing = required - r.keys()
    if missing:
        raise SystemExit(f"Row {i} ({r.get('name')}) is missing {sorted(missing)}")

updated = max(r["checked"] for r in data)
inline = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

html = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
html = (html.replace("/*__DATA__*/[]", inline)
            .replace("__COUNT__", str(len(data)))
            .replace("__UPDATED__", updated))
(ROOT / "index.html").write_text(html, encoding="utf-8")
print(f"Built index.html with {len(data)} resources (updated {updated}).")
