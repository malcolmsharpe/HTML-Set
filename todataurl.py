from base64 import b64encode

def convert(mime, data):
  url = 'data:%s;base64,%s' % (mime, b64encode(data))
  return url

jqueryurl = convert('text/javascript', file('jquery-1.3.2.min.js').read())

html = file('set.html').read()
html = html.replace('jquery-1.3.2.min.js', jqueryurl)
html = html.replace(' manifest="set.mf"', '')
file('seturl.intermediate.html', 'w').write(html)

url = convert('text/html', html)
file('seturl.txt', 'w').write(url)

page_lines = []
page_lines.append('<h1>Offline Set</h1>\n')
page_lines.append('<a href="' + url + '\n')
page_lines.append('">Bookmark this link to play offline</a>\n')
page_html = ''.join(page_lines)
file('set_offline.html', 'w').write(page_html)
