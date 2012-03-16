from base64 import b64encode

def convert(mime, data):
  url = 'data:%s;base64,%s' % (mime, b64encode(data))
  return url

jqueryurl = convert('text/javascript', file('jquery-1.3.2.min.js').read())
lines = []
writing = True
for line in file('set.html'):
  if 'END JQUERY' in line:
    writing = True
    lines.append(
      '<script type="text/javascript" src="'
      + jqueryurl
      + '"></script>\n')

  if writing:
    lines.append(line)

  if 'BEGIN JQUERY' in line:
    writing = False

html = ''.join(lines)
file('seturl.intermediate.html', 'w').write(html)

url = convert('text/html', html)
file('seturl.txt', 'w').write(url)

page_lines = []
page_lines.append('<h1>Offline Set</h1>\n')
page_lines.append('<a href="' + url + '\n')
page_lines.append('">Bookmark this link to play offline</a>\n')
page_html = ''.join(page_lines)
file('set_offline.html', 'w').write(page_html)
