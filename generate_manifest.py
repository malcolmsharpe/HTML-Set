import hashlib

f = file('set.mf', 'w')

print >>f, 'CACHE MANIFEST'

def checkpoint_file(name):
  h = hashlib.sha256()
  h.update(file(name, 'rb').read())
  print >>f
  print >>f, '#', h.hexdigest()
  print >>f, name

checkpoint_file('set.html')
checkpoint_file('jquery-1.3.2.min.js')
