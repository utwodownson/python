#!/usr/bin/python 

#assignment the value
name = list('Perl')
print "name = list('Perl')" + '\t' + 'name is ' + str(name)

name[2:] = list('ar')
print "name[2:] = list('ar')" + '\t' + 'name is ' + str(name)

num = [1, 5]
num[1:1] = [2, 3, 4]
print num

num = [1, 2, 3, 4, 5]
num[1:4] = []
print num

num = [1, 2, 3]
num.append(4)
print num

num = [1, 21, 1, [1, 2], [1], 1, 11]
print num.count(1)
print [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 41, 1, 1, 1].count(1)

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
a.extend(b)
print a
print b

a[len(a):] = b
print a

name = ['we', 'are', 'the', 'winner']
print name.index('we')
