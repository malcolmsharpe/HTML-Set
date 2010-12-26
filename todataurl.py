from base64 import b64encode

def convert(mime, data):
  url = 'data:%s;base64,%s' % (mime, b64encode(data))
  return url

jqueryurl = convert('text/javascript', file('jquery-1.3.2.min.js').read())
html = file('set.html').read()
html = html.replace('jquery-1.3.2.min.js', jqueryurl)
url = convert('text/html', html)

file('seturl.txt', 'w').write(url)
