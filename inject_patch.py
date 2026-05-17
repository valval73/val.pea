with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
tag = '<script src="live_patch.js"></script>'
# 1. Supprimer toute occurrence existante (peu importe où elle est)
html_clean = html.replace(tag + chr(10), '').replace(tag, '')
# 2. Injecter juste avant le DERNIER </body>
idx = html_clean.rfind('</body>')
if idx == -1:
    print('ERROR: </body> not found')
else:
    html_new = html_clean[:idx] + tag + chr(10) + html_clean[idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_new)
    print('OK: live_patch.js injected before last </body>')
