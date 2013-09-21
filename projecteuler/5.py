#!/usr/bin/python

# Smallest multiple
# Problem 5
# 2520 is the amallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
#
# Answer:
#   232792560

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)

def lcm_seq(seq):
    """Return lcm of sequence."""
    return reduce(lcm, seq)

solution = lcm_seq(xrange(1, 21))
print "lcm_seq():", solution

# lcmm(*range(1, 21))
