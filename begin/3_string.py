#!/usr/bin/python 

import string
from math import pi
from string import Template

format = "Pi with three decimals: %.3f"
print format % pi

s = Template('$x, $$ glorious $x!')
print s.substitute(x='slurm')

s = Template('A $thing ${x}t never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print s.substitute(d, x='mus')

print '%s plus %s equal %s' % (1, 1, 2)

print 'Price of eggs: $%d' % 42
print 'Price of eggs: %x' % 42
print 'Pi: %f...' % pi
print 'Very inexact estimate of pi: %i' % pi
print 'Using str: %s' % 42L

print '%10f' % pi
print '%10.2f' % pi
print '%.2f' % pi
print '%.5s' % 'Guido van Rossum'
print '%.*s' % (5, 'Guido van Rossum')

print '%010.2f' % pi
print repr('%-10.2f' % pi)
print '% 10.2f' % pi
print '%+10.2f' % pi

print string.digits
print string.letters
print string.lowercase


