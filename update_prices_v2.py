#!/usr/bin/env python3
"""
update_prices_v2.py - GitHub Actions script
Runs every weekday at 17:35 + every Friday at 18:00 (full recalibration)
1. Updates live prices from Yahoo Finance
2. On Friday: recalibrates el/eh/stop/o1/o2/dcfm when price drifts >15% from static
"""

import re, json, sys, os
from datetime import datetime
import urllib.request

def fetch_price(ticker_map, ticker):
    """Fetch live price from Yahoo Finance"""
    yf = ticker_map.get(ticker)
    if not yf:
        return None
    url = f"https://query2.finance.yahoo.com/v8/finance/chart/{yf}?interval=1d&range=1d"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        meta = data['chart']['result'][0]['meta']
        price = meta.get('regularMarketPrice') or meta.get('previousClose')
        return round(float(price), 2) if price else None
    except:
        return None

def recalibrate_zones(old_price, new_price, el, eh, stop, o1, o2, dcfb, dcfm, dcfu):
    """
    When price has moved significantly, scale all zones proportionally.
    This keeps the relative structure intact (upside %, stop distance %).
    """
    if old_price <= 0 or new_price <= 0:
        return el, eh, stop, o1, o2, dcfb, dcfm, dcfu
    
    ratio = new_price / old_price
    
    # Scale all price targets proportionally
    new_el   = round(el   * ratio, 1)
    new_eh   = round(eh   * ratio, 1)
    new_stop = round(stop * ratio, 1)
    new_o1   = round(o1   * ratio, 1)
    new_o2   = round(o2   * ratio, 1)
    new_dcfb = round(dcfb * ratio, 1)
    new_dcfm = round(dcfm * ratio, 1)
    new_dcfu = round(dcfu * ratio, 1)
    
    # Safety checks
    assert new_stop < new_price, f"stop {new_stop} >= price {new_price}"
    assert new_o1 > new_price, f"o1 {new_o1} <= price {new_price}"
    assert new_dcfm > new_price * 0.9, f"dcfm {new_dcfm} too low vs price {new_price}"
    
    return new_el, new_eh, new_stop, new_o1, new_o2, new_dcfb, new_dcfm, new_dcfu

# Yahoo Finance ticker map
YF_MAP = {
    'MC':'MC.PA','AI':'AI.PA','OR':'OR.PA','RMS':'RMS.PA','SAN':'SAN.PA',
    'TTE':'TTE.PA','SAF':'SAF.PA','SU':'SU.PA','AXA':'CS.PA','BNP':'BNP.PA',
    'ACA':'ACA.PA','GLE':'GLE.PA','AIR':'AIR.PA','KER':'KER.PA','PUB':'PUB.PA',
    'ORA':'ORA.PA','VIE':'VIE.PA','RNO':'RNO.PA','SGO':'SGO.PA','CAP':'CAP.PA',
    'DG':'DG.PA','VIV':'VIV.PA','RI':'RI.PA','LR':'LR.PA','WLN':'WLN.PA',
    'DSY':'DSY.PA','STM':'STM.PA','EL':'EL.PA','ML':'ML.PA','ENGI':'ENGI.PA',
    'HO':'HO.PA','GTT':'GTT.PA','ELIS':'ELIS.PA','SEB':'SK.PA','ERF':'ERF.PA',
    'ASML':'ASML.AS','NOVO':'NOVO-B.CO','SAP':'SAP.DE',
    'COFA':'COFA.PA','SPIE':'SPIE.PA','ALO':'ALO.PA','EDENRED':'EDEN.PA',
    'BVI':'BVI.PA','FDJ':'FDJ.PA','NRO':'NRO.PA',
    'PERNOD':'RI.PA','IPSEN':'IPN.PA','REXEL':'RXL.PA',
    'VIRBAC':'VIRP.PA','VIRB2':'VIRP.PA',
    'GTT':'GTT.PA','TRIGANO':'TRI.PA','BOIRON':'BOI.PA',
}

if __name__ == '__main__':
    html_file = 'index.html'
    if not os.path.exists(html_file):
        print(f"ERROR: {html_file} not found")
        sys.exit(1)
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    is_friday = datetime.now().weekday() == 4  # 4 = vendredi
    is_full_recalibration = '--full' in sys.argv or is_friday
    
    print(f"Mode: {'Recalibration complète (vendredi)' if is_full_recalibration else 'Mise à jour prix'}")
    
    updated = 0
    recalibrated = 0
    errors = []
    
    # Find S[] in the file
    s_start = content.find("const S=[")
    s_end_match = re.search(r'\n\];\s*\n\s*\n\s*// ═+\s*CALENDRIER', content[s_start:])
    if not s_end_match:
        print("ERROR: Could not find end of S[]")
        sys.exit(1)
    s_end = s_start + s_end_match.start()
    
    # Process each stock
    for m in re.finditer(r"(\{ticker:'([^']+)'.*?)(?=\n\n\{ticker:|\n\n\];)", 
                          content[s_start:s_end], re.DOTALL):
        block = m.group(1)
        ticker = m.group(2)
        
        # Get current static values
        def gn(key, text=block):
            mx = re.search(r'\b'+key+r':([\d.]+)', text)
            return float(mx.group(1)) if mx else None
        
        old_price = gn('price')
        if not old_price:
            continue
        
        # Fetch live price
        new_price = fetch_price(YF_MAP, ticker)
        if not new_price:
            continue
        
        new_block = block
        
        # Always update price and chg
        chg = round((new_price - old_price) / old_price * 100, 2) if old_price else 0
        new_block = re.sub(r'\bprice:[\d.]+', f'price:{new_price}', new_block, count=1)
        new_block = re.sub(r'\bchg:[-\d.]+', f'chg:{chg}', new_block, count=1)
        updated += 1
        
        # On Friday OR when price has drifted >15%: recalibrate zones
        drift = abs(new_price - old_price) / old_price if old_price else 0
        if is_full_recalibration or drift > 0.15:
            el   = gn('el')
            eh   = gn('eh')
            stop = gn('stop')
            o1   = gn('o1')
            o2   = gn('o2')
            dcfb = gn('dcfb')
            dcfm = gn('dcfm')
            dcfu = gn('dcfu')
            
            if all(v is not None for v in [el, eh, stop, o1, o2, dcfb, dcfm, dcfu]):
                try:
                    new_el, new_eh, new_stop, new_o1, new_o2, new_dcfb, new_dcfm, new_dcfu = \
                        recalibrate_zones(old_price, new_price, el, eh, stop, o1, o2, dcfb, dcfm, dcfu)
                    
                    for key, val in [('el',new_el),('eh',new_eh),('stop',new_stop),
                                     ('o1',new_o1),('o2',new_o2),('dcfb',new_dcfb),
                                     ('dcfm',new_dcfm),('dcfu',new_dcfu)]:
                        new_block = re.sub(r'\b'+key+r':[\d.]+', key+':'+str(val), new_block, count=1)
                    recalibrated += 1
                    print(f"  RECALIBRÉ {ticker}: {old_price}€ → {new_price}€ ({drift*100:.1f}% drift)")
                except AssertionError as e:
                    errors.append(f"{ticker}: {e}")
        
        # Replace block in content
        if new_block != block:
            block_start = s_start + m.start()
            block_end = block_start + len(block)
            content = content[:block_start] + new_block + content[block_end:]
    
    # Update timestamp in header
    ts = datetime.now().strftime('%d/%m à %H:%M')
    content = re.sub(
        r'(\d+ cours mis à jour .* \d+ échecs?\))',
        f'{updated} cours mis à jour le {ts}',
        content
    )
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ {updated} prix mis à jour")
    print(f"✅ {recalibrated} zones recalibrées")
    if errors:
        print(f"⚠️  {len(errors)} erreurs: {errors[:3]}")
    
    sys.exit(0)
