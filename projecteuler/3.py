#!/usr/bin/python

# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
# Answer:
#  6857

def highest_prime_factor(n):
    if isprime(n):
        return n
    for x in xrange(2, int(n ** 0.5) + 1):
        if not n % x:
          return highest_prime_factor(n / x)

def isprime(n):
    for x in xrange(2, int(n ** 0.5) + 1):
        if not n % x:
            return False
    return True

print highest_prime_factor(600851475143)
