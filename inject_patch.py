with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
tag = '<script src="live_patch.js"></script>'
if tag not in html:
    # Inserer juste avant </body> mais APRES le dernier </script>
    # Utiliser rfind pour trouver la DERNIERE occurrence de </body>
    idx = html.rfind('</body>')
    if idx != -1:
        html = html[:idx] + tag + chr(10) + html[idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print('Injected live_patch.js into index.html')
    else:
        print('ERROR: </body> not found')
else:
    print('live_patch.js already present')
