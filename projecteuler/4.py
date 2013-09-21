#!/usr/bin/python

# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer:
#   906609

from itertools import product

def is_palindrome(num):
      return str(num) == str(num)[::-1]

multiples = ((a, b) for a, b in product(xrange(100, 999), repeat = 2) if is_palindrome(a * b))
x, y = max(multiples, key = lambda (a,b): a * b)
print x * y
