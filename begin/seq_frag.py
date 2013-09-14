#!/usr/bin/python 

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print 'this is the fragmentation of sequence'
print 'num[3:6]' + '\t' + str(num[3:6])
print 'num[0:1]' + '\t' + str(num[0:1])
print 'num[7:10]' + '\t' + str(num[7:10])
print 'num[-3:-1]' + '\t' + str(num[-3:-1])
print 'num[-3:0]' + '\t' + str(num[-3:0])
print 'num[-3:]' + '\t' + str(num[-3:])
print 'num[:3]' + '\t\t' + str(num[:3])
print 'num[:]' + '\t\t' + str(num[:])

print
print 'the sequence step length'
print 'num[0:10:1]' + '\t' + str(num[0:10:1])
print 'num[0:10:2]' + '\t' + str(num[0:10:2])
print 'num[3:6:3]' + '\t' + str(num[3:6:3])
print 'num[::4]' + '\t' + str(num[::4])
print 'num[8:3:-1]' + '\t' + str(num[8:3:-1])
print 'num[10:0:-2]' + '\t' + str(num[10:0:-2])
print 'num[0:10:-2]' + '\t' + str(num[0:10:-2])
print 'num[::-2]' + '\t' + str(num[::-2])
print 'num[5::-2]' + '\t' + str(num[5::-2])
print 'num[:5:-2]' + '\t' + str(num[:5:-2])

