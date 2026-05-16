with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
tag = '<script src="live_patch.js"></script>'
if tag not in html:
    html = html.replace('</body>', tag + chr(10) + '</body>', 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Injected live_patch.js into index.html')
else:
    print('live_patch.js already present')
