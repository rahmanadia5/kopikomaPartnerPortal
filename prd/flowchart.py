"""Render the end-to-end process flowchart (flowchart.png) used in the PRD."""
import glob
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
W, H = 920, 1330
ROLE = {  # fill, stroke, label
    'Candidate': ('#FCE9D2', '#C27A2C'),
    'System': ('#E6EEF8', '#4A72A8'),
    'Sales': ('#E4F1E6', '#3F8A50'),
    'Reviewer': ('#EFE6F6', '#7E57A8'),
    'Manager': ('#F7E1E1', '#B04848'),
}
MX, RX, LX = 400, 770, 95  # main, right, left column centers
out = []

def text(x, y, lines, size=13, weight=400, color='#222'):
    lines = lines if isinstance(lines, list) else [lines]
    y0 = y - (len(lines) - 1) * (size + 3) / 2
    for i, ln in enumerate(lines):
        out.append(f'<text x="{x}" y="{y0 + i * (size + 3)}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="middle" dominant-baseline="middle">{ln}</text>')

def box(x, y, lines, role, w=290, h=58):
    f, s = ROLE[role]
    out.append(f'<rect x="{x - w/2}" y="{y - h/2}" width="{w}" height="{h}" rx="8" fill="{f}" stroke="{s}" stroke-width="1.6"/>')
    out.append(f'<text x="{x - w/2 + 8}" y="{y - h/2 + 12}" font-size="9.5" font-weight="700" fill="{s}">{role.upper()}</text>')
    text(x, y + 6, lines, 13, 600)

def diamond(x, y, lines, role, w=230, h=86):
    f, s = ROLE[role]
    out.append(f'<polygon points="{x},{y - h/2} {x + w/2},{y} {x},{y + h/2} {x - w/2},{y}" fill="{f}" stroke="{s}" stroke-width="1.6"/>')
    text(x, y, lines, 12.5, 600)

def term(x, y, label, color, w=170, h=40, dashed=False):
    extra = 'stroke-dasharray="5 4" fill-opacity="0"' if dashed else ''
    out.append(f'<rect x="{x - w/2}" y="{y - h/2}" width="{w}" height="{h}" rx="{h/2}" fill="{color}" stroke="{color}" {extra}/>')
    text(x, y, label, 12.5, 700, color if dashed else '#fff')

def line(pts, label=None, lx=None, ly=None, anchor='start'):
    d = ' '.join(f'{"M" if i == 0 else "L"}{x},{y}' for i, (x, y) in enumerate(pts))
    out.append(f'<path d="{d}" fill="none" stroke="#555" stroke-width="1.5" marker-end="url(#a)"/>')
    if label:
        out.append(f'<text x="{lx}" y="{ly}" font-size="11.5" font-weight="700" fill="#444" text-anchor="{anchor}">{label}</text>')

Y = dict(top=50, d1=160, pres=275, surv=375, d3=480, asm=590, d4=695, quo=805, neg=910, d6=1020, d7=1135, end=1240)

box(MX, Y['top'], 'Registers on Partner Portal', 'Candidate', w=250)
box(LX, Y['top'], ['Adds lead', '(offline channel)'], 'Sales', w=160)
diamond(MX, Y['d1'], ['1. New lead:', 'auto-assign', 'possible?'], 'System')
text(MX + 185, Y['d1'] + 60, ['Auto-assign if same region, not a duplicate,', 'and the regional sales is below lead cap'], 10.5, 400, '#555')
box(RX, Y['d1'], ['Assign sales', 'manually'], 'Manager', w=190)
box(MX, Y['pres'], ['2. Business presentation', '+ send prospectus'], 'Sales')
box(MX, Y['surv'], '3. Location survey', 'Sales')
text(RX, Y['surv'], ['AI location score below 60:', 'discuss with Manager first'], 10.5, 400, '#555')
diamond(MX, Y['d3'], ['Location', 'feasible?'], 'Sales', h=80)
box(MX, Y['asm'], ['4. Eligibility assessment', '(interview, background, finance, KYC)'], 'Reviewer', w=320)
diamond(MX, Y['d4'], 'Eligible?', 'Reviewer', h=76)
box(MX, Y['quo'], ['5. Send quotation version N', '(email + Partner Portal link)'], 'Sales')
box(MX, Y['neg'], ['6. Negotiation: candidate responds', '(in portal, or recorded by Sales)'], 'Candidate', w=320)
diamond(MX, Y['d6'], 'Response?', 'Candidate', h=80)
diamond(MX, Y['d7'], ['7. Final', 'approval?'], 'Manager', h=84)
term(MX, Y['end'], 'Approved (2 of 2)', '#2F7D46', w=200)
term(RX, Y['end'], ['Agreement signed', 'via Privy'], '#2F7D46', w=190, h=50, dashed=True)
for k in ('d3', 'd4', 'd7'):
    term(RX, Y[k], 'Rejected', '#B04848')
term(RX, Y['d6'], 'Withdrawn', '#777')

# arrows
line([(MX, Y['top'] + 29), (MX, Y['d1'] - 43)])
line([(MX + 115, Y['d1']), (RX - 95, Y['d1'])], 'No', MX + 125, Y['d1'] - 8)
line([(MX, Y['d1'] + 43), (MX, Y['pres'] - 29)], 'Yes', MX + 8, Y['d1'] + 80)
line([(RX, Y['d1'] + 29), (RX, Y['pres']), (MX + 145, Y['pres'])])
line([(LX, Y['top'] + 29), (LX, Y['pres']), (MX - 145, Y['pres'])], 'Owned by that sales', LX + 8, Y['pres'] - 40)
line([(MX, Y['pres'] + 29), (MX, Y['surv'] - 29)])
line([(MX, Y['surv'] + 29), (MX, Y['d3'] - 40)])
line([(MX + 115, Y['d3']), (RX - 85, Y['d3'])], 'No', MX + 125, Y['d3'] - 8)
line([(MX, Y['d3'] + 40), (MX, Y['asm'] - 29)], 'Yes', MX + 8, Y['d3'] + 60)
line([(MX, Y['asm'] + 29), (MX, Y['d4'] - 38)])
line([(MX + 115, Y['d4']), (RX - 85, Y['d4'])], 'No', MX + 125, Y['d4'] - 8)
line([(MX, Y['d4'] + 38), (MX, Y['quo'] - 29)], 'Yes', MX + 8, Y['d4'] + 58)
line([(MX, Y['quo'] + 29), (MX, Y['neg'] - 29)])
line([(MX, Y['neg'] + 29), (MX, Y['d6'] - 40)])
line([(MX + 115, Y['d6']), (RX - 85, Y['d6'])], 'Withdraw', MX + 125, Y['d6'] - 8)
line([(MX, Y['d6'] + 40), (MX, Y['d7'] - 42)], 'Agree (1 of 2)', MX + 8, Y['d6'] + 64)
line([(MX - 115, Y['d6']), (180, Y['d6']), (180, Y['quo']), (MX - 145, Y['quo'])], 'Request changes', 188, Y['d6'] - 8)
text(250, Y['quo'] + 46, '(revision, with Manager input)', 10.5, 400, '#555')
line([(MX - 60, Y['d6'] + 20), (MX - 60, Y['d6'] + 62), (40, Y['d6'] + 62), (40, Y['surv']), (MX - 145, Y['surv'])], 'Change location', 48, Y['d6'] + 54)
text(150, Y['surv'] + 46, '(new address, then revised quotation)', 10.5, 400, '#555')
line([(MX + 115, Y['d7']), (RX - 85, Y['d7'])], 'Reject', MX + 125, Y['d7'] - 8)
line([(MX, Y['d7'] + 42), (MX, Y['end'] - 20)], 'Approve (2 of 2)', MX + 8, Y['d7'] + 62)
line([(MX + 100, Y['end']), (RX - 95, Y['end'])])

# legend + footer
lx = 30
for r, (f, s) in ROLE.items():
    out.append(f'<rect x="{lx}" y="{H - 52}" width="14" height="14" rx="3" fill="{f}" stroke="{s}"/>')
    out.append(f'<text x="{lx + 20}" y="{H - 40}" font-size="12" fill="#333">{r}</text>')
    lx += 110
text(W / 2, H - 16, 'Every stage has a deadline. Overdue stages trigger automatic reminders to the PIC and the Manager (dashboard and email).', 11.5, 400, '#444')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Arial, Helvetica, sans-serif">
<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect width="{W}" height="{H}" fill="#fff"/>{"".join(out)}</svg>'''
(HERE / 'flowchart.svg').write_text(svg, encoding='utf-8')

exe = (glob.glob('/opt/pw-browsers/chromium*/chrome-linux/chrome') or [None])[0]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
    pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=2.5)
    pg.set_content(f'<html><body style="margin:0">{svg}</body></html>')
    pg.locator('svg').screenshot(path=str(HERE / 'flowchart.png'))
    b.close()
print('flowchart.png')
