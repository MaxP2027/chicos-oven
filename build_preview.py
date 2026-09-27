"""Render the Flask pages into docs/ for GitHub Pages. Run from the repo root."""
from pathlib import Path
import shutil
import sys
from urllib.parse import urlsplit
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'bakery'))
from app import app

DEST = ROOT / 'docs'
DEST.mkdir(exist_ok=True)
routes = [rule.rule for rule in app.url_map.iter_rules()
          if rule.endpoint != 'static' and 'GET' in rule.methods and not rule.arguments]
mapping = {route: ('index.html' if route == '/' else route.strip('/') + '.html')
           for route in routes}
client = app.test_client()
for route, filename in mapping.items():
    response = client.get(route)
    if response.status_code != 200:
        raise RuntimeError(f'{route}: HTTP {response.status_code}')
    html = response.get_data(as_text=True)
    for source, target in mapping.items():
        html = html.replace(f'href="{source}"', f'href="{target}"')
    html = html.replace('href="/static/', 'href="static/').replace('src="/static/', 'src="static/')
    (DEST / filename).write_text(html, encoding='utf-8')
shutil.copytree(ROOT / 'bakery' / 'static', DEST / 'static', dirs_exist_ok=True)
(DEST / '.nojekyll').write_text('', encoding='utf-8')

class LinkCheck(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name not in ('href', 'src') or not value:
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc or not url.path:
                continue
            if url.path.startswith('/') or not (DEST / url.path).is_file():
                raise RuntimeError(f'Broken static link: {value}')

for filename in mapping.values():
    html = (DEST / filename).read_text(encoding='utf-8')
    LinkCheck().feed(html)
    if '{{' in html or '{%' in html:
        raise RuntimeError(f'Unrendered template: {filename}')
print(f'Exported and checked {len(mapping)} pages in {DEST}')
