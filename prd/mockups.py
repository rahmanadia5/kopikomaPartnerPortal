"""Capture prototype screenshots for the PRD Mock Ups section."""
import glob
from pathlib import Path
from playwright.sync_api import sync_playwright
HERE = Path(__file__).parent; OUT = HERE / 'mockups'
URL = (HERE.parent / 'index.html').as_uri()
exe = (glob.glob('/opt/pw-browsers/chromium*/chrome-linux/chrome') or [None])[0]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
    pg = b.new_page(viewport={'width': 1366, 'height': 820}, device_scale_factor=1.5)
    pg.goto(URL); pg.evaluate('localStorage.clear()'); pg.reload()
    shot = lambda n, full=False: (pg.wait_for_timeout(500), pg.screenshot(path=str(OUT / f'{n}.png'), full_page=full))
    shot('01_login')
    pg.evaluate("quickLogin('laras')"); shot('02_pipeline')
    a = pg.evaluate("state.apps.find(a=>a.stage==='negosiasi').id")
    pg.evaluate(f"openDetail('{a}')"); pg.evaluate("setTab('quotation')"); shot('03_detail')
    pg.evaluate("state.sel=null;render()"); pg.evaluate(f"openApproval('{a}')"); shot('04_status')
    pg.evaluate("state.apv=null;render();setView('dashboard')"); shot('05_target')
    pg.evaluate("setView('sales')"); shot('06_sales')
    m = b.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=2)
    m.goto(URL + '#mitra'); pg = m
    m.evaluate("openPortal('form')"); shot('07_portal_form')
    em = m.evaluate(f"state.apps.find(a=>a.id==='{a}').email")
    m.evaluate("openPortal('track')"); m.evaluate(f"portalLookup('{a}','{em}')"); shot('08_portal_tracker')
    m.evaluate("(document.getElementById('pq-confirm')||document.body).scrollIntoView({block:'center'})"); shot('09_portal_quote')
    b.close()
