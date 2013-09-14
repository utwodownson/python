#!/usr/bin/python 

print "5_line.py==========="

print 'Hello,',
print 'world!'
print

print 'age', 42
print

print 'greeting', ',', 'salutation', 'name'
print 'greeting' + ',', 'salutation', 'name'
print

x, y, z = 1, 2, 3
print x, y, z
print

x, y = y, x
print x, y, z
print

for i in range(3):
  scoundrel = {'name': 'Robin', 'grilfriend': 'Marion'}
  print
  key, value = scoundrel.popitem()
  print key, value
  key, value = scoundrel.popitem()
  print key, value

for i in range(3):
  scoundrel = {'grilfriend': 'Marion', 'name': 'Robin'}
  print
  key, value = scoundrel.popitem()
  print key, value
  key, value = scoundrel.popitem()
  print key, value
print

x = y = 2
print x, y
print

print bool(False)
print bool(None)
print bool([])
print bool(())
print bool({})
print bool("")
print bool(0)
print

print bool([ ])
print

print [] != ()
print


