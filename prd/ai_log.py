"""Build the AI conversation log PDF (grouped like the PRD's Use of AI table)."""
import glob, html, json, re, sys
from datetime import datetime, timedelta
from pathlib import Path
import markdown
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
SRC = sys.argv[1]
CHAT = json.load(open(sys.argv[2], encoding='utf-8')) if len(sys.argv) > 2 else {}
OUT = HERE / 'EDTS APM 2027 - Nadia Rahma Prasanti - Universitas Indonesia - AI Conversation.pdf'

msgs = []
for line in open(SRC, encoding='utf-8'):
    try: d = json.loads(line)
    except ValueError: continue
    if d.get('isMeta') or d.get('isCompactSummary') or d.get('isSidechain'): continue
    m, t = d.get('message') or {}, d.get('type')
    c = m.get('content')
    if t == 'user':
        if isinstance(c, list) and any(x.get('type') == 'tool_result' for x in c): continue
        parts = [c] if isinstance(c, str) else [x.get('text', '') for x in c if x.get('type') == 'text'] if isinstance(c, list) else []
        imgs = sum(1 for x in c if isinstance(x, dict) and x.get('type') == 'image') if isinstance(c, list) else 0
        txt = '\n'.join(parts).strip()
        if not txt and not imgs: continue
        msgs.append({'ts': d['timestamp'], 'role': 'user', 'text': txt, 'imgs': imgs})
    elif t == 'assistant' and isinstance(c, list):
        txt = '\n\n'.join(x.get('text', '') for x in c if x.get('type') == 'text').strip()
        if txt: msgs.append({'ts': d['timestamp'], 'role': 'assistant', 'text': txt})

users = [i for i, m in enumerate(msgs) if m['role'] == 'user']

def clean_user(t):
    t = re.sub(r'@"[^"]*/[0-9a-f]+-([^"/]+)"', r'[attached file: \1]', t)
    t = re.sub(r'\[Image: source: [^\]]*\]', '', t)
    t = re.sub(r'<system-reminder>.*?</system-reminder>', '', t, flags=re.S)
    return t.strip()

def clean_ai(t, limit=450):
    t = re.sub(r'(?m)^(Quick update|Now |Next |Committing|Checking|Writing|Rewriting|Screenshots are done|Flowchart is drawn|Full chat log|Testing|Tests pass|The fixes|All good|LibreOffice).*$', '', t).strip()
    t = re.sub(r'(?m)^\|.*$\n?', '', t).strip()
    if len(t) > limit:
        cut = max(t.rfind('\n', 0, limit), t.rfind('. ', 0, limit) + 1)
        t = t[:cut if cut > limit * 0.4 else limit].rstrip() + ' *[…]*'
    return t

def wib(ts):
    d = datetime.fromisoformat(ts.replace('Z', '+00:00')) + timedelta(hours=7)
    return d.strftime('%d %b %Y, %H:%M WIB')

def exchange(n):
    """n-th user message (0-based) plus the assistant replies after it."""
    i = users[n]
    end = users[n + 1] if n + 1 < len(users) else len(msgs)
    u = msgs[i]
    ut = clean_user(u['text'])
    if u.get('imgs'): ut += f"\n\n*[{u['imgs']} screenshot{'s' if u['imgs'] > 1 else ''} attached]*"
    replies = [m['text'] for m in msgs[i + 1:end] if m['role'] == 'assistant']
    ai = replies[-1] if replies else ''
    return u['ts'], ut, clean_ai(ai)

def find(snippet, nth=0):
    hits = [k for k, i in enumerate(users) if snippet.lower() in msgs[i]['text'].lower()]
    return hits[nth if nth >= 0 else len(hits) + nth]

SECTIONS = [
    ('Pain points, features, and flow',
     'Tidied up my pain points, feature list, and funnel into a clear structure',
     'Defined the pain points, features, and funnel, designed the business process (stages, PIC, deadlines, and approval rules), and pointed out the special cases the flow must handle (for example, duplicate leads, leads outside any sales region, and location changes during negotiation)',
     []),
    ('PRD (first draft)',
     'Formatted my pain points, features, and flow into a first PRD draft (text)',
     'Reviewed and edited the draft and used it as the spec for the prototype; updated the PRD whenever a decision changed while prototyping',
     []),
    ('Prototype',
     'Built the HTML prototype based on the PRD, first in Claude chat and then in Claude Code, over many feedback rounds',
     'Reviewed each version and decided layout, wording, and terminology',
     []),
    ('Product decisions (recorded in the PRD)',
     'Discussed the trade-offs of each change I proposed, then updated the PRD and the prototype to match',
     'Decided each change: separate apps for the franchisor and the candidate, roles and access, the 8-stage flow with automatic lead assignment, location-change rules, per-sales targets, and e-signature tracking',
     ['i need an end to end business process', 'submit applicationnya', 'separate this two dashboard', 'musti ada e-sign', 'dua duanya kali ya',
      'minta ganti lokasi di akhir', 'oke usul lu semua diterima', 'yg mandiri gausah dilabel', 'jadi satu sales megang both', 'semua sales ada target dua duanya']),
    ('Testing',
     'Ran automated browser tests on every role and screen size',
     'Defined what "correct" means and checked results',
     [('cek yang redundant atau butuh improve', -1), 'cek dulu semuanya']),
    ('Development and deployment',
     'Set up the GitHub repository, pushed every revision, and guided the Vercel deployment so the live prototype updates automatically on each push',
     'Created the Vercel project, connected it to GitHub, chose the project name, and checked each deployed version',
     ['put all the code to my repo', 'deploy to vercel', 'biar di vercel auto updte', 'terlanjr login pake google', ('i made a new project', -1), 'ganti jadi kopikoma-partnerportal']),
]

md = lambda t: markdown.markdown(t, extensions=['tables', 'sane_lists'])
css = """
@page { size: A4; margin: 18mm 16mm 18mm 16mm; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 10.5pt; color: #1d1d1d; line-height: 1.45; }
h1 { font-size: 18pt; margin: 0 0 4px; } h2 { font-size: 14pt; margin: 26px 0 6px; page-break-after: avoid; border-bottom: 2px solid #3d2a20; padding-bottom: 4px; }
.meta { color: #555; margin-bottom: 14px; } table { border-collapse: collapse; width: 100%; margin: 6px 0; }
td, th { border: 1px solid #999; padding: 5px 7px; vertical-align: top; text-align: left; font-size: 9.5pt; } th { background: #E7E2DA; }
.sum td:first-child { width: 22%; font-weight: bold; }
.ex { margin: 10px 0 14px; page-break-inside: auto; }
.msg { border-radius: 8px; padding: 8px 11px; margin: 6px 0; }
.u { background: #FCE9D2; border-left: 4px solid #C27A2C; } .a { background: #F3F3F1; border-left: 4px solid #6b6b6b; }
.who { font-size: 8.5pt; font-weight: bold; color: #555; margin-bottom: 3px; } .msg p { margin: 4px 0; } .msg ul, .msg ol { margin: 4px 0; padding-left: 20px; }
.msg table td, .msg table th { font-size: 8.5pt; padding: 3px 5px; } code { font-size: 9pt; } blockquote { margin: 4px 0; padding-left: 8px; border-left: 3px solid #bbb; color: #333; }
"""
body = [f'<h1>AI Conversation Log</h1><div class="meta">Nadia Rahma Prasanti - Universitas Indonesia<br>Tool: Claude (Anthropic), in two places: Claude chat (Project "EDTS assessment test") for feature prioritization and the first prototype, then Claude Code for the prototype iterations.<br>'
        'The log is grouped by the activities in the PRD\'s "Use of AI" section. It shows the key moments only: my messages are quoted in full, and the AI replies are shortened to their first lines.</div>',
        '<table class="sum"><tr><th>Activity</th><th>AI did</th><th>I did</th></tr>' +
        ''.join(f'<tr><td>{html.escape(a)}</td><td>{html.escape(b)}</td><td>{html.escape(c)}</td></tr>' for a, b, c, _ in SECTIONS) + '</table>']
import base64
SHOTS = sorted(p for p in (Path(sys.argv[3]) if len(sys.argv) > 3 else HERE / 'ai_shots').glob('*') if p.suffix.lower() in ('.png', '.jpg', '.jpeg'))
if SHOTS:
    body.append('<h2>Original screenshots</h2><p class="small">Screenshots taken directly from the Claude interface, as proof of the original conversation. The pages after this summarize the key moments as text.</p>')
    for f in SHOTS:
        cap = re.sub(r'^\d+[ _-]*', '', f.stem).replace('_', ' ')
        b64 = base64.b64encode(f.read_bytes()).decode()
        body.append(f'<figure style="margin:10px 0 18px;page-break-inside:avoid"><img src="data:image/{"png" if f.suffix.lower() == ".png" else "jpeg"};base64,{b64}" style="max-width:100%;max-height:230mm;border:1px solid #ccc;border-radius:6px"><figcaption class="small" style="margin-top:4px"><i>{html.escape(cap)}</i></figcaption></figure>')
for k, (title, ai_did, i_did, picks) in enumerate(SECTIONS, 1):
    body.append(f'<h2>{k}. {html.escape(title)}</h2><p><b>AI did:</b> {html.escape(ai_did)}<br><b>I did:</b> {html.escape(i_did)}</p>')
    for ut, at in [x for x in CHAT.get({'Pain points, features, and flow': 'Features and flow'}.get(title, title), []) if not re.search(r'\bjir\b', x[0], re.I)]:
        body.append(f'<div class="ex"><div class="msg u"><div class="who">Nadia · Claude chat (Project: EDTS assessment test)</div>{md(ut)}</div>'
                    f'<div class="msg a"><div class="who">Claude</div>{md(at)}</div></div>')
    if title == 'Prototype':
        body.append('<p class="small">This was followed by feedback rounds on layout and wording, first in Claude chat and then in Claude Code.</p>')
    for p in picks:
        snip, nth = p if isinstance(p, tuple) else (p, 0)
        ts, ut, at = exchange(find(snip, nth))
        if re.search(r'\bjir\b', ut, re.I): continue
        body.append(f'<div class="ex"><div class="msg u"><div class="who">Nadia · Claude Code</div>{md(ut)}</div>'
                    f'<div class="msg a"><div class="who">Claude</div>{md(at)}</div></div>')

page = f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(body)}</body></html>'
(HERE / 'ai_log.html').write_text(page, encoding='utf-8')
exe = (glob.glob('/opt/pw-browsers/chromium*/chrome-linux/chrome') or [None])[0]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
    pg = b.new_page(); pg.set_content(page)
    pg.pdf(path=str(OUT), format='A4', print_background=True, display_header_footer=True,
           header_template='<div style="font-size:8px;font-family:Arial;margin-left:16mm;color:#555">Nadia Rahma Prasanti - Universitas Indonesia</div>',
           footer_template='<div style="font-size:8px;font-family:Arial;width:100%;text-align:center;color:#555"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
           margin={'top': '18mm', 'bottom': '16mm', 'left': '16mm', 'right': '16mm'})
    b.close()
print(OUT)
